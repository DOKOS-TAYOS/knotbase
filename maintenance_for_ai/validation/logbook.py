#!/usr/bin/env python3
"""Generate and validate the repository logbook indexes."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

MONTH_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
DAY_RE = re.compile(r"^(?P<date>\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))\.md$")
ENTRY_RE = re.compile(
    r"^## (?P<time>([01]\d|2[0-3]):[0-5]\d) - (?P<title>\S.*)$", re.MULTILINE
)
ORIGINS = {"ChatGPT", "Codex", "Mixto", "Manual"}
REQUIRED_FIELDS = ("Origen", "Commits", "PR", "Acciones", "Motivo", "Validación")
SUMMARY_LIMIT = 240


@dataclass(frozen=True)
class Issue:
    path: str
    code: str
    message: str


@dataclass(frozen=True)
class DayRecord:
    date: str
    month: str
    changes: int
    summary: str
    path: Path


def _compact(text: str) -> str:
    return " ".join(text.split())


def _short_summary(summaries: list[str]) -> str:
    if not summaries:
        return "Sin cambios registrados."
    text = "; ".join(summaries[:3])
    if len(summaries) > 3:
        text += "; …"
    if len(text) <= SUMMARY_LIMIT:
        return text
    return text[: SUMMARY_LIMIT - 1].rstrip() + "…"


def _parse_day(path: Path) -> tuple[DayRecord | None, list[Issue]]:
    display = path.as_posix()
    issues: list[Issue] = []
    match = DAY_RE.fullmatch(path.name)
    if not match:
        return None, [
            Issue(display, "logbook-day-name", "daily file name must be YYYY-MM-DD.md")
        ]

    date = match.group("date")
    month = date[:7]
    if path.parent.name != month:
        issues.append(
            Issue(
                display, "logbook-day-folder", f"{date} must be stored under {month}/"
            )
        )

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return None, [Issue(display, "logbook-day-read", str(error))]

    lines = text.splitlines()
    if not lines or lines[0].strip() != f"# {date}":
        issues.append(
            Issue(display, "logbook-day-heading", f"first line must be '# {date}'")
        )

    changes_match = re.search(r"(?m)^Cambios:\s*(\d+)\s*$", text)
    summary_match = re.search(r"(?m)^Resumen:\s*(\S.*)$", text)
    changes = int(changes_match.group(1)) if changes_match else -1
    summary = _compact(summary_match.group(1)) if summary_match else ""
    if changes_match is None:
        issues.append(Issue(display, "logbook-day-count", "missing 'Cambios: <n>'"))
    if not summary:
        issues.append(
            Issue(display, "logbook-day-summary", "missing non-empty 'Resumen:'")
        )

    entries = list(ENTRY_RE.finditer(text))
    if changes >= 0 and changes != len(entries):
        issues.append(
            Issue(
                display,
                "logbook-day-count-mismatch",
                f"Cambios declares {changes} but {len(entries)} entries were found",
            )
        )
    if changes == 0:
        issues.append(
            Issue(
                display,
                "logbook-day-empty",
                "daily files must contain at least one change",
            )
        )

    for index, entry in enumerate(entries):
        start = entry.end()
        end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        block = text[start:end]
        label = f"{display}:{entry.group('time')}"
        for field in REQUIRED_FIELDS:
            if not re.search(rf"(?m)^{re.escape(field)}:\s*(?:\S.*)?$", block):
                issues.append(
                    Issue(label, "logbook-entry-field", f"missing '{field}:' field")
                )

        origin_match = re.search(r"(?m)^Origen:\s*(\S.*)$", block)
        if origin_match:
            origin = _compact(origin_match.group(1))
            if origin not in ORIGINS:
                issues.append(
                    Issue(
                        label,
                        "logbook-entry-origin",
                        f"Origen must be one of {', '.join(sorted(ORIGINS))}",
                    )
                )

    record = DayRecord(
        date=date,
        month=month,
        changes=max(changes, 0),
        summary=summary,
        path=path,
    )
    return record, issues


def _collect_days(root: Path) -> tuple[list[DayRecord], list[Issue]]:
    package = root / "logbook"
    issues: list[Issue] = []
    if not package.is_dir():
        return [], [Issue("logbook", "logbook-missing", "logbook/ is required")]
    if not (package / "CONTRACT.md").is_file():
        issues.append(
            Issue(
                "logbook/CONTRACT.md",
                "logbook-contract-missing",
                "CONTRACT.md is required",
            )
        )

    days: list[DayRecord] = []
    for child in sorted(package.iterdir()):
        if not child.is_dir():
            continue
        if not MONTH_RE.fullmatch(child.name):
            issues.append(
                Issue(
                    f"logbook/{child.name}",
                    "logbook-month-name",
                    "month directories must use YYYY-MM",
                )
            )
            continue
        for path in sorted(child.glob("*.md")):
            if path.name == "README.md":
                continue
            record, day_issues = _parse_day(path)
            issues.extend(day_issues)
            if record is not None:
                days.append(record)
    return days, issues


def _render_root(days: list[DayRecord]) -> str:
    by_month: dict[str, list[DayRecord]] = {}
    for day in days:
        by_month.setdefault(day.month, []).append(day)

    lines = [
        "# Logbook",
        "",
        "> Índice generado automáticamente. No editar manualmente.",
        "> Contrato: [CONTRACT.md](CONTRACT.md).",
        "",
        "Inicio del registro: primera tarea de mantenimiento.",
        "Zona horaria canónica: `Europe/Madrid`.",
        "",
        "| Mes | Días con cambios | Cambios | Resumen |",
        "|---|---:|---:|---|",
    ]
    for month in sorted(by_month, reverse=True):
        month_days = sorted(by_month[month], key=lambda item: item.date, reverse=True)
        total = sum(day.changes for day in month_days)
        summary = _short_summary([day.summary for day in month_days])
        lines.append(
            f"| [{month}]({month}/) | {len(month_days)} | {total} | {summary} |"
        )
    if not by_month:
        lines.append("| _Sin entradas_ | 0 | 0 | Sin cambios registrados. |")
    return "\n".join(lines) + "\n"


def _render_month(month: str, days: list[DayRecord]) -> str:
    ordered = sorted(days, key=lambda item: item.date, reverse=True)
    total = sum(day.changes for day in ordered)
    lines = [
        f"# {month}",
        "",
        "> Índice generado automáticamente. No editar manualmente.",
        "",
        f"Días con cambios: {len(ordered)}",
        f"Cambios: {total}",
        "",
        "| Día | Cambios | Resumen |",
        "|---|---:|---|",
    ]
    for day in ordered:
        filename = day.path.name
        lines.append(f"| [{day.date}]({filename}) | {day.changes} | {day.summary} |")
    return "\n".join(lines) + "\n"


def write_indexes(root: Path) -> list[Issue]:
    days, issues = _collect_days(root)
    if issues:
        return issues

    package = root / "logbook"
    package.mkdir(parents=True, exist_ok=True)
    (package / "README.md").write_text(_render_root(days), encoding="utf-8")

    by_month: dict[str, list[DayRecord]] = {}
    for day in days:
        by_month.setdefault(day.month, []).append(day)
    for month, month_days in by_month.items():
        (package / month / "README.md").write_text(
            _render_month(month, month_days),
            encoding="utf-8",
        )
    return []


def validate_logbook(root: Path) -> list[Issue]:
    days, issues = _collect_days(root)
    if issues:
        return issues

    package = root / "logbook"
    root_index = package / "README.md"
    expected_root = _render_root(days)
    try:
        actual_root = root_index.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        issues.append(Issue("logbook/README.md", "logbook-index-read", str(error)))
    else:
        if actual_root != expected_root:
            issues.append(
                Issue(
                    "logbook/README.md",
                    "logbook-index-stale",
                    "global index is stale; run 'python maintenance_for_ai/validation/logbook.py --write'",
                )
            )

    by_month: dict[str, list[DayRecord]] = {}
    for day in days:
        by_month.setdefault(day.month, []).append(day)

    for month, month_days in sorted(by_month.items()):
        index = package / month / "README.md"
        expected = _render_month(month, month_days)
        try:
            actual = index.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            issues.append(
                Issue(f"logbook/{month}/README.md", "logbook-index-read", str(error))
            )
            continue
        if actual != expected:
            issues.append(
                Issue(
                    f"logbook/{month}/README.md",
                    "logbook-index-stale",
                    "monthly index is stale; run 'python maintenance_for_ai/validation/logbook.py --write'",
                )
            )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="regenerate derived logbook indexes"
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]

    issues = write_indexes(root) if args.write else validate_logbook(root)
    for issue in issues:
        print(f"{issue.path}: {issue.code}: {issue.message}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
