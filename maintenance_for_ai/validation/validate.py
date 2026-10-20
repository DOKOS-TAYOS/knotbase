#!/usr/bin/env python3
"""Canonical offline validator for the installed Knotbase instance.

Checks local structure, routing, evidence schemas, privacy and logbook; remote
permissions and actual ChatGPT consumer behavior require independent checks.
"""
from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AI = ROOT / "info_for_ai"
CONFIG = ROOT / "config/instance.csv"
PUBLIC_UPSTREAM = os.environ.get("GITHUB_REPOSITORY", "").casefold() == "dokos-tayos/knotbase"
REQUIRED_CONFIG = ("instance_repository", "github_owner", "knowledge_repository",
                   "knowledge_storage", "onboarding_state")
SAFE_ID = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
TRACE_COLUMNS = {
    "fuentes.csv": "source_id",
    "hechos.csv": "fact_id",
    "capacidades.csv": "capability_id",
    "relaciones.csv": "relation_id",
}
VALID_VISIBILITY = {"public", "restricted", "private"}
VALID_REVIEW = {"verified", "needs_review", "superseded", "deprecated"}
VALID_CONFIDENCE = {"A", "B", "C", "D"}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f"{path}: missing or duplicate CSV headers")
        result = list(reader)
        for line, row in enumerate(result, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{path}:{line}: incorrect number of columns")
        return result


def inspect(errors: list[str]) -> None:
    def fail(message: str) -> None:
        errors.append(message)

    try:
        pairs = read_rows(CONFIG)
        keys = [row.get("key", "") for row in pairs]
        if len(keys) != len(set(keys)) or not set(REQUIRED_CONFIG) <= set(keys):
            fail("config/instance.csv: missing or duplicate configuration keys")
        cfg = {row["key"]: row["value"] for row in pairs}
        for key in cfg:
            if re.search(r"token|password|secret|api[_-]?key", key, re.I):
                fail(f"config/instance.csv: forbidden credential key {key}")
        for key in ("instance_repository", "knowledge_repository"):
            if cfg.get(key) and not SAFE_ID.fullmatch(cfg[key]):
                fail(f"config/instance.csv: invalid owner/repo for {key}")
        if cfg.get("onboarding_state") not in {"unconfigured", "configured", "partial"}:
            fail("config/instance.csv: invalid onboarding_state")
        if cfg.get("onboarding_state") == "configured" and not (
            cfg.get("instance_repository") and cfg.get("github_owner")
            and cfg.get("knowledge_repository")
            and cfg.get("knowledge_storage") == "private"
        ):
            fail("config/instance.csv: configured requires verified private storage and owner fields")
        if PUBLIC_UPSTREAM and any(cfg.get(key) for key in
                                   ("instance_repository", "github_owner", "knowledge_repository")):
            fail("Public upstream must remain unconfigured")
    except (OSError, ValueError, csv.Error, KeyError) as exc:
        fail(str(exc))

    try:
        domains = read_rows(AI / "indice_dominios.csv")
        names = [row["dominio"] for row in domains]
        if len(names) != len(set(names)):
            fail("Duplicate routed domain")
        for row in domains:
            for key in ("core", "indice"):
                route = row[key]
                if route and (route.startswith("/") or ".." in Path(route).parts
                              or not (AI / route).is_file()):
                    fail(f"Unknown or unsafe {key} route: {route}")
        for name in names:
            index = AI / name / f"indice_{name}.csv"
            if not index.is_file():
                fail(f"Missing domain index: {index.relative_to(ROOT)}")
                continue
            for record in read_rows(index):
                relative = record["ruta"]
                if relative.startswith("/") or ".." in Path(relative).parts:
                    fail(f"Unsafe indexed route: {relative}")
                    continue
                path = AI / relative
                if not (path.is_dir() if relative.endswith("/") else path.is_file()):
                    fail(f"Missing indexed route: {relative}")
    except (OSError, ValueError, csv.Error, KeyError) as exc:
        fail(str(exc))

    try:
        registry = read_rows(AI / "comandos.csv")
        lookup = read_rows(AI / "comandos_lookup.csv")
        commands = [row["command"] for row in registry]
        if len(commands) != len(set(x.upper() for x in commands)):
            fail("Duplicate compact command")
        if "#NOAH" in commands or len(commands) != 64:
            fail("Exactly 64 public commands excluding #NOAH are required")
        expected_lookup = [{"command": command, "line": str(i)}
                           for i, command in enumerate(commands, 2)]
        if lookup != expected_lookup:
            fail("Command lookup does not match physical registry lines")
        modes = {"help", "maintenance", "route"}
        active_domains = {row["dominio"] for row in read_rows(AI / "indice_dominios.csv")}
        procedures = {row["ruta"] for row in read_rows(ROOT / "maintenance_for_ai/indice_mantenimiento.csv")}
        for record in registry:
            cmd, mode = record["command"], record["mode"]
            if mode not in modes:
                fail(f"{cmd}: invalid mode {mode}")
            if mode == "maintenance" and record["domains"]:
                fail(f"{cmd}: maintenance mode cannot have domains")
            if mode == "route":
                for d in record["domains"].split(";"):
                    if d.strip() and d.strip() not in active_domains:
                        fail(f"{cmd}: missing domain {d}")
            for module in (m.strip() for m in record["modules"].split(";") if m.strip()):
                if mode == "maintenance":
                    if module.removeprefix("maintenance_for_ai/") not in procedures:
                        fail(f"{cmd}: missing maintenance procedure {module}")
                elif not (AI / module).is_file():
                    fail(f"{cmd}: missing command module {module}")
    except (OSError, ValueError, csv.Error, KeyError) as exc:
        fail(str(exc))

    profile = AI / "info_user"
    source_ids: set[str] = set()
    for filename, pk in TRACE_COLUMNS.items():
        try:
            rows = read_rows(profile / "_data" / filename)
            ids = [row[pk] for row in rows]
            if len(ids) != len(set(ids)) or any(not field for field in ids):
                fail(f"{filename}: duplicate or empty primary identifier")
            if filename == "fuentes.csv":
                source_ids = set(ids)
            for record in rows:
                if record.get("visibility") not in VALID_VISIBILITY:
                    fail(f"{filename}: invalid visibility")
                if record.get("review_status") not in VALID_REVIEW:
                    fail(f"{filename}: invalid review_status")
                if record.get("confidence") not in VALID_CONFIDENCE:
                    fail(f"{filename}: invalid confidence")
                if filename != "fuentes.csv":
                    references = [s.strip() for s in record.get("source_id", "").split(";")]
                    if not references or any(not s or s not in source_ids for s in references):
                        fail(f"{filename}: missing or unknown source_id")
        except (OSError, ValueError, csv.Error, KeyError) as exc:
            fail(str(exc))
    try:
        inventory = read_rows(profile / "repositorios_github.csv")
        lookup = read_rows(profile / "repositorios_github_lookup.csv")
        names = [record["nombre"].casefold() for record in inventory]
        if len(names) != len(set(names)):
            fail("Repository inventory has duplicate case-insensitive names")
        if lookup != [{"nombre": record["nombre"], "line": str(n)}
                      for n, record in enumerate(inventory, start=2)]:
            fail("Repository inventory lookup is stale")
        for row in inventory:
            if row.get("archivado") not in {"si", "no"}:
                fail(f"Repository inventory: invalid archived status for {row['nombre']}")
            if row.get("estado_desarrollo") not in (
                "finalizado", "pendiente", "continuo", "congelado", "no_determinado"
            ):
                fail(f"Repository inventory: invalid development state for {row['nombre']}")
    except (OSError, ValueError, csv.Error, KeyError) as exc:
        fail(str(exc))

    if PUBLIC_UPSTREAM:
        for path in profile.rglob("*.csv"):
            if path.name == "indice_info_user.csv":
                continue
            try:
                if read_rows(path):
                    fail(f"Public upstream contains personal data rows: {path.relative_to(ROOT)}")
            except (OSError, ValueError, csv.Error) as exc:
                fail(str(exc))

    try:
        sys.path.insert(0, str(ROOT))
        from maintenance_for_ai.validation.logbook import validate_logbook
        errors.extend(f"{issue.path}: {issue.code}: {issue.message}"
                      for issue in validate_logbook(ROOT))
    except (ImportError, OSError, ValueError) as exc:
        fail(f"logbook: {exc}")


def main() -> int:
    errors: list[str] = []
    inspect(errors)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover",
         "-s", "tests", "-p", "test_*.py", "-v"],
        cwd=ROOT, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
