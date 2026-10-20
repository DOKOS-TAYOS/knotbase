"""Offline structural checks for Knotbase's scoped public router.

These tests do not claim that a ChatGPT consumer activates AGENTS.md or
that CV/blog artifacts execute end to end.
"""
from __future__ import annotations

import csv
import hashlib
import io
import os
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "info_for_ai"
EXPECTED_COMMANDS = ("#HELP", "#PROMPT", "#DEEP", "#LIT", "#SOTA", "#READ", "#PAPER", "#ARG", "#PROOF", "#OPP", "#EXPL", "#NOTES", "#VIDEO", "#CLASS", "#TFG", "#TFM", "#BLOG", "#HTML", "#CV", "#CVEDIT", "#MAIL", "#LINKEDIN", "#CONTACT", "#DELIVER", "#REC", "#IDENT", "#ASSESS", "#REV", "#COM", "#DIFF", "#RESP", "#RESUB", "#INIT", "#REPRO", "#REFAC", "#DOC", "#READY", "#BUG", "#OPT", "#DEAD", "#TEST", "#FIX", "#CYCLE", "#REFACT", "#JOURNAL", "#PAPERFIT", "#PR", "#ISSUE", "#SYNC", "#RELEASE", "#BITACORA", "#SHIP")
EXPECTED_SOURCE = {
    "AGENTS.md": ("611a06672cf2fb99889268741c3f3eecb4e53696", "public-routing-adapted"),
    "info_for_ai/indice_dominios.csv": ("c5a3b7cb29e83719dd8303e1f4f93dde04e7692f", "public-routing-adapted"),
    "info_for_ai/comandos.csv": ("8c57e847df45dd80d92a74bbc0efd6129d4e32e0", "public-subset-adapted"),
    "info_for_ai/comandos_lookup.csv": ("890701beb36f8a4ed80437341f16a080f1cd26aa", "public-routing-adapted"),
    "info_for_ai/iterative_continuation.md": ("89f7ff26efd2ad8db17b64e1a12c43e3274e819b", "verbatim"),
}
PRIVATE_TOKENS = (
    "Alejandro Mata Ali",
    "papers_alejandro_mata_ali.csv",
    "DOKOS-TAYOS/dokos-instructions-knowledge",
    "standard-cv-html-template",
    "03_formato_europass.md",
)


def csv_rows(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.reader(stream))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")  # normalize Windows text checkout to source LF
    envelope = b"blob " + str(len(data)).encode("ascii") + b"\x00" + data
    return hashlib.sha1(envelope).hexdigest()


class PublicRouterTests(unittest.TestCase):
    def test_public_commands_and_lookup_lines(self) -> None:
        registry = csv_rows(AI / "comandos.csv")
        lookup = csv_rows(AI / "comandos_lookup.csv")
        self.assertEqual(len(registry), len(EXPECTED_COMMANDS) + 1)
        self.assertEqual(len(registry[0]), 11)
        self.assertEqual(tuple(row[0] for row in registry[1:]), EXPECTED_COMMANDS)
        self.assertEqual(lookup[0], ["command", "line"])
        self.assertEqual(lookup[1:], [[command, str(i + 2)] for i, command in enumerate(EXPECTED_COMMANDS)])
        for row in registry[1:]:
            self.assertEqual(len(row), 11)
            self.assertIn(row[2], ("help", "route"))
            if row[2] == "route":
                self.assertTrue(row[7])
            else:
                self.assertEqual(row[0], "#HELP")

    def test_router_command_summary_matches_registry(self) -> None:
        router = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        prefix = "The registry currently supports "
        summary = next((line for line in router.splitlines() if line.startswith(prefix)), None)
        self.assertIsNotNone(summary)
        self.assertIn(": ", summary)
        named = tuple(piece.strip("`") for piece in summary.split(": ", 1)[1].split(". Its exact rows", 1)[0].replace(" and ", ", ").split(", "))
        self.assertEqual(named, EXPECTED_COMMANDS)

    def test_unregistered_command_summary_matches_registry(self) -> None:
        router = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        excluded = next(
            (line for line in router.splitlines()
             if line.startswith("This pilot intentionally **does not register**")),
            None,
        )
        self.assertIsNotNone(excluded)
        import re
        excluded_commands = set(re.findall(r"`(#[A-Z0-9_]+)`", excluded.split("These thirteen commands", 1)[0]))
        registry_commands = set(EXPECTED_COMMANDS)
        self.assertTrue(excluded_commands.isdisjoint(registry_commands),
                        "A published command cannot be described as excluded")
        self.assertEqual(excluded_commands, {
            "#PAPSYNC", "#CVSYNC", "#REPOSYNC", "#KBCHK",
            "#DEP", "#SEC", "#CLEAN", "#RUNS", "#CI", "#TRIAGE",
            "#BIO", "#ME", "#NOAH",
        })
        self.assertIn("`#SHIP` **is registered**", excluded)

    def test_published_domain_routes(self) -> None:
        domains = csv_rows(AI / "indice_dominios.csv")
        self.assertEqual(len(domains[0]), 8)
        mapping = {row[0]: row for row in domains[1:]}
        self.assertEqual(set(mapping), {"professional_documents", "blog_writing", "research", "htmls", "prompting", "education", "interactions", "code", "papers", "github", "info_user"})
        for domain, row in mapping.items():
            self.assertEqual(len(row), 8)
            core = AI / row[3]
            index = AI / row[4]
            if row[3]:
                self.assertTrue(core.is_file(), str(core))
            self.assertTrue(index.is_file(), str(index))
        for row in csv_rows(AI / "comandos.csv")[2:]:
            declared_domains = [item.strip() for item in row[7].split(";") if item.strip()]
            self.assertTrue(declared_domains)
            for domain in declared_domains:
                self.assertIn(domain, mapping)
            modules = [module.strip() for module in row[8].split(";") if module.strip()]
            if row[0] == "#PROMPT":
                self.assertFalse(modules)
                modules = ["prompting/01_codex_prompt_generation.md", "prompting/02_chat_prompt_generation.md"]
            for module in modules:
                route = AI / module
                self.assertTrue(route.is_file(), str(route))
        for domain in ("professional_documents", "blog_writing", "research", "htmls", "prompting", "education", "interactions", "code", "papers", "github", "info_user"):
            index = csv_rows(AI / domain / f"indice_{domain}.csv")
            for row in index[1:]:
                self.assertTrue((AI / row[1]).is_dir() if row[3] == "container" else (AI / row[1]).is_file(), row[1])

    def test_generic_user_scaffold_is_unconfigured(self) -> None:
        config = dict(csv_rows(ROOT / "config/instance.csv")[1:])
        self.assertEqual(config["onboarding_state"], "unconfigured")
        for field in ("instance_repository", "github_owner", "knowledge_repository", "knowledge_storage"):
            self.assertEqual(config[field], "")
        index = csv_rows(AI / "info_user/indice_info_user.csv")
        self.assertEqual(len(index[0]), 10)
        self.assertGreater(len(index), 20)
        for entry in index[1:]:
            self.assertEqual(len(entry), 10)
            path = AI / entry[1]
            self.assertTrue(path.is_dir() if entry[3] == "container" else path.is_file(), entry[1])
        for name in ("papers.csv", "articulos.csv", "citas_papers.csv", "citas_por_paper.csv",
                     "repositorios_github.csv", "repositorios_github_lookup.csv", "cursos.csv", "videos.csv"):
            self.assertEqual(len(csv_rows(AI / "info_user" / name)), 1)

    def test_continuation_and_approval_gates(self) -> None:
        iterative = AI / "iterative_continuation.md"
        self.assertEqual(git_blob_sha(iterative), EXPECTED_SOURCE["info_for_ai/iterative_continuation.md"][0])
        blog = (AI / "blog_writing/04_flujo_iterativo_de_generacion.md").read_text(encoding="utf-8")
        cv = (AI / "professional_documents/00_core.md").read_text(encoding="utf-8")
        self.assertIn("../iterative_continuation.md", blog)
        self.assertIn("OK", blog)
        self.assertIn("OK explícito", cv)
        self.assertIn("standard_cv_rendering.md", cv)

    def test_source_ledger(self) -> None:
        rows = csv_rows(ROOT / "manifests/source_parity.csv")
        self.assertEqual(rows[0], ["path", "source_git_blob_sha", "status"])
        self.assertEqual(len(rows), 140)  # header + 139 sources
        paths = [row[0] for row in rows[1:]]
        self.assertEqual(len(paths), len(set(paths)))
        lookup = {row[0]: row[1:] for row in rows[1:]}
        for path, source in EXPECTED_SOURCE.items():
            self.assertIn(path, lookup)
            self.assertEqual(tuple(lookup[path]), source)
            self.assertTrue((ROOT / path).is_file(), path)
        for row in rows[1:]:
            self.assertEqual(len(row), 3)
            self.assertEqual(len(row[1]), 40)
        self.assertEqual(
            sum(row[2] == "verbatim" for row in rows[1:]), 105
        )
        self.assertEqual(sum(row[2] == "privacy-adapted" for row in rows[1:]), 21)

    def test_html_index_is_complete_without_personal_letter_flow(self) -> None:
        rows = csv_rows(AI / "htmls/indice_htmls.csv")
        self.assertEqual(len(rows), 12)  # header + 11 general public modules
        self.assertEqual(len(rows[0]), 6)
        routes = []
        for row in rows[1:]:
            self.assertEqual(len(row), 6)
            self.assertNotIn("letter", " ".join(row).lower())
            path = AI / row[1]
            self.assertTrue(path.is_file(), str(path))
            routes.append(row[1])
        self.assertEqual(len(set(routes)), 11)
        self.assertIn("htmls/00_core.md", routes)
        self.assertIn("htmls/05_verification.md", routes)
        manifest = {row[0]: row for row in csv_rows(ROOT / "manifests/source_parity.csv")[1:]}
        self.assertEqual(
            manifest["info_for_ai/htmls/indice_htmls.csv"][1:],
            ["05189871f4a37f1d8c7d8079996e7ddeec44eea4", "privacy-adapted"],
        )

    def test_two_public_runtime_assets(self) -> None:
        lookup = csv_rows(ROOT / "assets_for_ai/indice_assets_lookup.csv")
        index = csv_rows(ROOT / "assets_for_ai/indice_assets.csv")
        self.assertEqual(lookup[0], ["id", "line"])
        self.assertEqual(len(index), 3)
        self.assertEqual(
            lookup[1:],
            [["paper-study-html-template", "2"], ["presentation-editor-html-base", "3"]],
        )
        sha_expected = {
            "paper-study-html-template": "0aa057406d3965f6d2566825afb86b739fc62aa3",
            "presentation-editor-html-base": "349765691f9e11cddf8b37e4bb652fa089747968",
        }
        for label, line in lookup[1:]:
            entry = index[int(line) - 1]
            self.assertEqual(entry[0], label)
            path = ROOT / "assets_for_ai" / entry[1]
            self.assertTrue(path.is_file(), str(path))
            self.assertEqual(git_blob_sha(path), sha_expected[label])
            markup = path.read_text(encoding="utf-8")
            self.assertIn("</html>", markup.lower())
            self.assertNotIn("info_user/", markup)
            self.assertNotIn("photos_/", markup)
        source_records = {row[0]: row for row in csv_rows(ROOT / "manifests/source_parity.csv")[1:]}
        for suffix in (
            "assets_for_ai/indice_assets.csv",
            "assets_for_ai/indice_assets_lookup.csv",
        ):
            self.assertEqual(source_records[suffix][2], "privacy-adapted")

    def test_no_private_identity_in_router_files(self) -> None:
        for relative in EXPECTED_SOURCE:
            text = (ROOT / relative).read_text(encoding="utf-8")
            for token in PRIVATE_TOKENS:
                self.assertNotIn(token, text, f"{relative}: {token}")


    def test_portable_bootstrap_is_fail_closed_until_dependencies_exist(self) -> None:
        bootstrap = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        for required in (
            "config/instance.csv",
            "instance_repository",
            "github_owner",
            "knowledge_repository",
            "maintenance_for_ai/indice_mantenimiento.csv",
            "## Acceptance conditions for a user instance",
        ):
            self.assertIn(required, bootstrap)
        router = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("## Portable-instance onboarding (draft entrypoint)", router)
        self.assertIn("BOOTSTRAP.md", router)
        self.assertIn("read-only setup guide", router)
        self.assertIn("not installed yet", router)
        registered = {row[0] for row in csv_rows(AI / "comandos.csv")[1:]}
        self.assertNotIn("#NOAH", registered)

        user_commands = {"#ME", "#BIO"}
        maintenance_commands = {"#PAPSYNC", "#CVSYNC", "#REPOSYNC", "#KBCHK"}
        bulk_commands = {"#DEP", "#SEC", "#CLEAN", "#RUNS", "#TRIAGE", "#CI"}
        if registered & (user_commands | maintenance_commands | bulk_commands):
            self.assertTrue((ROOT / "config/instance.csv").is_file(),
                            "Do not activate owner workflows before instance configuration exists")
            self.assertTrue((AI / "info_user/00_core.md").is_file())
            self.assertTrue((AI / "info_user/indice_info_user.csv").is_file())
            self.assertTrue((AI / "info_user/repositorios_github.csv").is_file())
            self.assertTrue((AI / "info_user/repositorios_github_lookup.csv").is_file())
        if registered & maintenance_commands:
            self.assertTrue((ROOT / "maintenance_for_ai/00_core.md").is_file())
            self.assertTrue((ROOT / "maintenance_for_ai/indice_mantenimiento.csv").is_file())
            self.assertTrue((ROOT / "maintenance_for_ai/validation/validate.py").is_file(),
                            "KBCHK and maintenance commands require the portable validator")

        schemas = {
            "info_for_ai/info_user/_data/fuentes.csv": "source_id,source_name,source_type,priority,confidence,review_status,visibility,location,valid_from,valid_to,observed_at,scope,notes",
            "info_for_ai/info_user/_data/hechos.csv": "fact_id,category,assertion_type,confidence,subject,predicate,value,review_status,visibility,valid_from,valid_to,observed_at,source_id,notes",
            "info_for_ai/info_user/_data/capacidades.csv": "capability_id,capability,capability_domain,capability_group,claim_type,confidence,review_status,visibility,evidence,source_id,valid_from,valid_to,observed_at,notes",
            "info_for_ai/info_user/_data/relaciones.csv": "relation_id,assertion_type,confidence,review_status,subject,predicate,object,visibility,valid_from,valid_to,observed_at,source_id,notes",
            "info_for_ai/info_user/repositorios_github.csv": "nombre,url,descripcion_resumen,tipo,visibilidad,estado_desarrollo,archivado,es_fork,dependabot_dias_versiones,ultima_verificacion,notas",
            "info_for_ai/info_user/repositorios_github_lookup.csv": "nombre,line",
        }
        # An installed private fork may hold authorized user records. Upstream
        # PR validation must reject published personal rows, including CSVs
        # added after this fixed list of canonical schemas.
        is_public_upstream = os.environ.get("GITHUB_REPOSITORY", "").lower() == "dokos-tayos/knotbase"
        profile_root = AI / "info_user"
        if (profile_root / "00_core.md").is_file():
            self.assertTrue((profile_root / "indice_info_user.csv").is_file())
            for required in schemas:
                self.assertTrue((ROOT / required).is_file(),
                                "Published info_user is missing required schema: " + required)
        for relative, header in schemas.items():
            path = ROOT / relative
            if not path.exists():
                continue
            rows = csv_rows(path)
            self.assertEqual(rows[0], header.split(","), relative)
        if is_public_upstream and profile_root.exists():
            for path in profile_root.rglob("*.csv"):
                if path.name == "indice_info_user.csv":
                    continue  # routing metadata, not a personal-data record
                rows = csv_rows(path)
                self.assertEqual(len(rows), 1,
                                 "Public upstream must ship header-only profile CSVs: " + str(path))
                self.assertTrue(rows[0] and any(field.strip() for field in rows[0]),
                                "Public CSV must have a nonempty header: " + str(path))

        config_path = ROOT / "config/instance.csv"
        if config_path.exists():
            configuration = csv_rows(config_path)
            self.assertEqual(configuration[0], ["key", "value"])
            self.assertTrue(all(len(record) == 2 and record[0].strip()
                                for record in configuration[1:]))
            values = dict(configuration[1:])
            self.assertEqual(len(values), len(configuration) - 1,
                             "Instance configuration keys must be unique")
            for key in ("instance_repository", "github_owner",
                        "knowledge_repository", "knowledge_storage", "onboarding_state"):
                self.assertIn(key, values)
            for key in values:
                self.assertIsNone(re.search(r"token|password|secret|api[_-]?key", key, re.I),
                                  "Never store credentials in the instance manifest")
            for key in ("instance_repository", "knowledge_repository"):
                if values[key]:
                    self.assertRegex(values[key], r"^[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+$")
            if values["onboarding_state"] == "configured":
                self.assertTrue(values["instance_repository"] and values["github_owner"])
            if is_public_upstream:
                self.assertFalse(values["instance_repository"],
                                 "Do not bootstrap a public upstream to a user's private instance")
                self.assertFalse(values["github_owner"])
                self.assertFalse(values["knowledge_repository"])


if __name__ == "__main__":
    unittest.main()
