"""Deterministic scenario probes for the *documented* public instruction contracts.

These tests exercise real published CSV routing and explicit, synthetic workflow
states. They are not a language-model agent, a CV generator, a web researcher,
or proof of independent ChatGPT runtime behavior.
"""
from __future__ import annotations

import csv
import re
import unittest
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "info_for_ai"
MODIFIERS = {"#SHORT", "#MEDIUM", "#LONG"}


class RoutingError(ValueError):
    """The public router is required to stop for this input."""


@dataclass(frozen=True)
class Decision:
    command: str
    modifier: str | None
    argument: str
    domain: str | None
    module: str | None
    mode: str


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def resolve_command(message: str) -> Decision:
    """Resolve a compact command from the *real* registry; never infer semantics."""
    text = message.strip()
    if not text:
        raise RoutingError("Empty input")
    parts = text.split(maxsplit=1)
    modifier = None
    if parts[0].upper() in MODIFIERS:
        modifier = parts[0].upper()
        if len(parts) != 2:
            raise RoutingError("Missing content after length modifier")
        text = parts[1]
        parts = text.split(maxsplit=1)
        if parts[0].upper() in MODIFIERS:
            raise RoutingError("Conflicting length modifiers")
    token = parts[0]
    if not re.fullmatch(r"#[A-Za-z][A-Za-z0-9_]*", token):
        raise RoutingError("Not a compact-command invocation")
    name = token.upper()
    lookup = {row["command"].upper(): int(row["line"]) for row in read_csv(AI / "comandos_lookup.csv")}
    if name not in lookup:
        raise RoutingError("Unregistered command: do not infer a meaning")
    registry = read_csv(AI / "comandos.csv")
    location = lookup[name] - 2
    if location < 0 or location >= len(registry):
        raise RoutingError("Invalid registry lookup")
    row = registry[location]
    if row["command"].upper() != name:
        raise RoutingError("Registry and lookup inconsistent")
    argument = parts[1].strip() if len(parts) == 2 else ""
    if row["mode"] == "route" and not argument:
        raise RoutingError("Missing required arguments: " + row["usage"])
    if row["mode"] == "help":
        return Decision(name, modifier, argument, None, None, "help")
    if row["mode"] != "route":
        raise RoutingError("Unsupported mode")
    domains = {entry["dominio"]: entry for entry in read_csv(AI / "indice_dominios.csv")}
    domain = row["domains"]
    if domain not in domains:
        raise RoutingError("Domain unavailable in public index")
    entry = domains[domain]
    for relative in (entry["core"], entry["indice"], row["modules"]):
        if not (AI / relative).is_file():
            raise RoutingError("Missing route target: " + relative)
    return Decision(name, modifier, argument, domain, row["modules"], "route")


def next_cv_phase(phase: str, message: str, *, same_application: bool) -> str:
    """Conservative synthetic approval gate, not a generated CV."""
    if phase != "strategy" or not same_application:
        return phase
    return "materialization" if message.strip().lower() == "ok" else phase


def cv_edit_policy(*, existing_cv: bool, material_target_change: bool) -> str:
    """The classification is supplied by the scenario, not inferred from natural language."""
    if not existing_cv:
        return "need_existing_cv"
    return "strategy_approval" if material_target_change else "local_edit"


def blog_units(*, has_latex_assets: bool, wants_images: bool,
               wants_distribution: bool) -> tuple[str, ...]:
    phases = ["1", "2", "3", "4"]
    if has_latex_assets:
        phases.append("5")
    if wants_images:
        phases.extend(("6A", "6B"))
    if wants_distribution:
        phases.append("7")
    return tuple(phases)


def next_blog_phase(current: str, message: str, *, units: tuple[str, ...],
                    same_article: bool, image_plan_approved: bool = False) -> str:
    """One-next-unit probe; 6B is inaccessible before an approved 6A."""
    if not same_article or message.strip().lower() != "ok":
        return current
    if current not in units:
        raise RoutingError("Invalid active blog unit")
    index = units.index(current)
    if index + 1 >= len(units):
        return current
    if current == "6A" and not image_plan_approved:
        return current
    return units[index + 1]


class PublicRouterScenarioTests(unittest.TestCase):
    def test_resolves_actual_registered_command_destinations(self) -> None:
        examples = (
            ("#CV Oferta ficticia de ingeniería", "#CV", "professional_documents/01_crear_cv.md"),
            ("#CVEDIT Ajusta el enlace de un CV ficticio", "#CVEDIT", "professional_documents/02_reajustar_cv.md"),
            ("#BLOG Ejemplo didáctico sobre una estructura de datos", "#BLOG", "blog_writing/04_flujo_iterativo_de_generacion.md"),
        )
        for message, command, module in examples:
            with self.subTest(command=command):
                decision = resolve_command(message)
                self.assertEqual(decision.command, command)
                self.assertEqual(decision.module, module)
                self.assertTrue((AI / module).is_file())

    def test_modifiers_and_multiline_argument_survive(self) -> None:
        with self.assertRaises(RoutingError):
            resolve_command("#LONG #SHORT #BLOG Un tema de prueba")
        result = resolve_command("#LONG #BLOG Un tema de prueba; nivel introductorio\nSin imágenes")
        self.assertEqual(result.modifier, "#LONG")
        self.assertIn("; nivel introductorio\nSin imágenes", result.argument)
        self.assertEqual(resolve_command("#medium #cv Contexto ficticio").modifier, "#MEDIUM")

    def test_conflicting_modifiers_and_missing_arguments_stop(self) -> None:
        inputs = ("#LONG #SHORT #CV Oferta", "#SHORT", "#CV", "#CVEDIT", "#BLOG")
        for message in inputs:
            with self.subTest(message=message), self.assertRaises(RoutingError):
                resolve_command(message)

    def test_unknown_commands_are_not_guessed(self) -> None:
        for message in ("#DEP", "#UNREGISTERED Do something", "#PROMPT Whatever"):
            with self.subTest(message=message), self.assertRaisesRegex(RoutingError, "Unregistered"):
                resolve_command(message)

    def test_help_is_read_only_without_domain_load(self) -> None:
        for message in ("#HELP", "#HELP CAREER"):
            result = resolve_command(message)
            self.assertEqual(result.mode, "help")
            self.assertIsNone(result.domain)
            self.assertIsNone(result.module)

    def test_cv_first_turn_requires_approval(self) -> None:
        cv = (AI / "professional_documents/01_crear_cv.md").read_text(encoding="utf-8")
        self.assertIn("no generes DOCX/PDF antes del OK explícito", cv)
        self.assertIn("no cargues `standard_cv_rendering.md`", cv)
        self.assertEqual(next_cv_phase("strategy", "Por favor, cambia la sección", same_application=True), "strategy")
        self.assertEqual(next_cv_phase("strategy", "ok", same_application=False), "strategy")
        self.assertEqual(next_cv_phase("strategy", "OK", same_application=True), "materialization")

    def test_cvedit_local_change_does_not_require_new_strategy(self) -> None:
        self.assertEqual(cv_edit_policy(existing_cv=False, material_target_change=False), "need_existing_cv")
        self.assertEqual(cv_edit_policy(existing_cv=True, material_target_change=False), "local_edit")
        self.assertEqual(cv_edit_policy(existing_cv=True, material_target_change=True), "strategy_approval")
        module = (AI / "professional_documents/02_reajustar_cv.md").read_text(encoding="utf-8")
        self.assertIn("Los cambios locales pueden ejecutarse directamente", module)
        self.assertIn("espera un OK explícito", module)

    def test_blog_short_path_has_no_phantom_phases(self) -> None:
        units = blog_units(has_latex_assets=False, wants_images=False, wants_distribution=True)
        self.assertEqual(units, ("1", "2", "3", "4", "7"))
        current = "1"
        for expected in units[1:]:
            current = next_blog_phase(current, " OK ", units=units, same_article=True)
            self.assertEqual(current, expected)
        self.assertEqual(next_blog_phase("7", "OK", units=units, same_article=True), "7")

    def test_blog_visual_plan_requires_explicit_acceptance(self) -> None:
        units = blog_units(has_latex_assets=True, wants_images=True, wants_distribution=True)
        self.assertEqual(units, ("1", "2", "3", "4", "5", "6A", "6B", "7"))
        self.assertEqual(next_blog_phase("4", "ok", units=units, same_article=True), "5")
        self.assertEqual(next_blog_phase("5", "ok", units=units, same_article=True), "6A")
        self.assertEqual(next_blog_phase("6A", "ok", units=units, same_article=True), "6A")
        self.assertEqual(
            next_blog_phase("6A", "ok", units=units, same_article=True, image_plan_approved=True),
            "6B",
        )
        self.assertEqual(next_blog_phase("6B", "ok", units=units, same_article=True), "7")

    def test_blog_corrections_or_new_tasks_do_not_advance(self) -> None:
        units = blog_units(has_latex_assets=False, wants_images=True, wants_distribution=True)
        for message, same_article in (("Cambiar el título", True), ("Ok, añade fuentes", True), ("ok", False)):
            self.assertEqual(next_blog_phase("2", message, units=units, same_article=same_article), "2")

    def test_documented_blog_phase_gates_exist(self) -> None:
        module = (AI / "blog_writing/04_flujo_iterativo_de_generacion.md").read_text(encoding="utf-8")
        continuation = (AI / "iterative_continuation.md").read_text(encoding="utf-8")
        for expected in ("../iterative_continuation.md", "6A. Planificación visual", "6B. Generación visual", "Fase 7. Distribución"):
            self.assertIn(expected, module)
        self.assertIn("siguiente unidad pendiente", continuation)


if __name__ == "__main__":
    unittest.main()
