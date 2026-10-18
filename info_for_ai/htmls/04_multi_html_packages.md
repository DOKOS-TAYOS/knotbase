# Packages containing several HTML files

Open this module when the user requests an ordered package or coordinated set of multiple HTML files.

Apply `htmls/00_core.md` and `htmls/01_generation_and_interaction.md` first. When the package is for a class, course, workshop, or structured training, also follow `education/03_preparacion_clases.md`; its Phase 1 approval gate controls when real lesson deliverables may begin. Before delivering each real HTML, apply `htmls/05_verification.md` and any other selected HTML modules.

**Invariant:** When the user requests a package or ordered set of multiple HTML files, do not generate the whole set in one batch unless the user explicitly overrides this review workflow.

During package planning, define the complete set: position, filename, purpose, key message, approximate sections, any interaction that is genuinely justified, and shared visual/navigation conventions. For structured training, record this map in the Markdown master required by `education/03_preparacion_clases.md`. Use the planning pass to remove duplication and keep terminology, progression, branding, and interaction patterns consistent across the set.

Every filename must begin with its one-based position in the package, preferably zero-padded for stable sorting, for example `01_introduccion.html`, `02_caso_practico.html`, `03_simulacion.html`.

## Optional visual prototype during planning

When the applicable planning workflow permits a visual prototype, create at most one minimal HTML style prototype. It may demonstrate branding, typography, spacing, controls, presentation mode, or a representative interaction, but it must use placeholder or representative content rather than implementing the first lesson. Name it so that it cannot be confused with a package deliverable, for example `00_prototipo_visual.html`.

The prototype is disposable unless the user asks to keep it and does not count as approval of any required content-planning gate.

## Iterative generation

After all applicable planning and approval gates have been satisfied:

1. Generate or revise only the first pending real HTML.
2. Present that HTML for review and stop before generating the next file.
3. If the user answers `ok` or otherwise approves it, continue with the next HTML.
4. If the user reports problems, fix the current HTML and keep iterating on it until approved before moving forward.
5. Carry approved visual, navigation, component, interaction, terminology, and content decisions forward so later files remain consistent with the package plan and, when applicable, the Markdown master.
6. If a package-wide decision changes, update its canonical planning source first, then apply the change to the current and subsequent files as appropriate.

**Invariant:** Package-wide decisions persist across review rounds until an explicit later instruction revises them. The canonical planning source remains authoritative for those shared decisions.

## Package completion shorthand

**Invariant:** Once every planned real HTML in the package has been generated and the iterative review rounds are complete, interpret a standalone user reply `ok` as approval of the completed package and return a ZIP containing the final HTML deliverables. Preserve their ordered filenames and include only the intended package files and assets needed for direct use unless the user explicitly asks for additional working files.

Before the last real HTML has been generated, `ok` retains its iterative meaning of approving the current HTML and advancing to the next pending file. Do not create the final ZIP prematurely.

**Default:** After at least one real HTML has been generated, interpret a standalone user reply `pdf` as a request for static PDF derivatives of the currently generated HTML scope. Load and apply `htmls/static_pdf_export.md` to every HTML in scope. Package ordering determines which HTMLs are included and their order; presentation mode is canonical for export only on the HTMLs where it actually exists.
