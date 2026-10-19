"""Offline structural checks for Knotbase's scoped public router.

These tests do not claim that a ChatGPT consumer activates AGENTS.md or
that CV/blog artifacts execute end to end.
"""
from __future__ import annotations

import csv
import hashlib
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "info_for_ai"
EXPECTED_COMMANDS = ("#HELP", "#PROMPT", "#DEEP", "#LIT", "#SOTA", "#READ", "#PAPER", "#ARG", "#PROOF", "#OPP", "#EXPL", "#NOTES", "#VIDEO", "#CLASS", "#TFG", "#TFM", "#BLOG", "#HTML", "#CV", "#CVEDIT", "#MAIL", "#LINKEDIN", "#CONTACT", "#DELIVER", "#REC", "#IDENT", "#ASSESS", "#REV", "#COM", "#DIFF", "#RESP", "#RESUB", "#INIT", "#REPRO", "#REFAC", "#DOC", "#READY", "#BUG", "#OPT", "#DEAD", "#TEST", "#FIX", "#CYCLE", "#REFACT", "#JOURNAL", "#PAPERFIT", "#PR", "#ISSUE", "#SYNC", "#RELEASE", "#BITACORA")
EXPECTED_SOURCE = {
    "AGENTS.md": ("611a06672cf2fb99889268741c3f3eecb4e53696", "public-routing-adapted"),
    "info_for_ai/indice_dominios.csv": ("c5a3b7cb29e83719dd8303e1f4f93dde04e7692f", "public-routing-adapted"),
    "info_for_ai/comandos.csv": ("8c57e847df45dd80d92a74bbc0efd6129d4e32e0", "public-subset-adapted"),
    "info_for_ai/comandos_lookup.csv": ("890701beb36f8a4ed80437341f16a080f1cd26aa", "public-routing-adapted"),
    "info_for_ai/iterative_continuation.md": ("89f7ff26efd2ad8db17b64e1a12c43e3274e819b", "verbatim"),
}
PRIVATE_TOKENS = (
    "info_user/",
    "assets_for_ai/",
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

    def test_published_domain_routes(self) -> None:
        domains = csv_rows(AI / "indice_dominios.csv")
        self.assertEqual(len(domains[0]), 8)
        mapping = {row[0]: row for row in domains[1:]}
        self.assertEqual(set(mapping), {"professional_documents", "blog_writing", "research", "htmls", "prompting", "education", "interactions", "code", "papers", "github"})
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
        for domain in ("professional_documents", "blog_writing", "research", "htmls", "prompting", "education", "interactions", "code", "papers", "github"):
            index = csv_rows(AI / domain / f"indice_{domain}.csv")
            for row in index[1:]:
                self.assertTrue((AI / row[1]).is_file(), row[1])

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


if __name__ == "__main__":
    unittest.main()
