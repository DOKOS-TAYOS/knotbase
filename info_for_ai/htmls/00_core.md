# HTML domain core

Open this core for every task routed to the `htmls` domain. It defines the universal contract and the selective module routing for HTML artifacts.

If the task only records an already identified HTML page or web reference in the knowledge package, use `htmls/plantilla_entrada.md` after the domain index and do not load creation modules unnecessarily.

## Selective module routing

**Invariant:** After this core, open `htmls/indice_htmls.csv` and load only the modules whose activation conditions match the task.

For creation or revision work:

- load `htmls/01_generation_and_interaction.md` for implementation, responsive behavior, prose, ordinary visual design, and the general interaction shell;
- load `htmls/05_verification.md` before delivering any created or revised HTML;
- additionally load `htmls/interactive_controls.md` when the audience-facing content contains stateful filters, selectors, tabs, toggles, progressive disclosure, modals, drawers, popovers, replaceable explanatory states, or comparable content interaction not already fully owned by another selected specialized module;
- additionally load `htmls/02_visuals_and_diagrams.md` when the artifact contains diagrams, charts, plots, matrices, coordinate maps, structured tables, or comparable visual structures;
- additionally load `htmls/03_presentation_mode.md` when the artifact supports a talk, lecture, class, workshop, live presentation, or an explicitly requested presentation mode;
- additionally load `htmls/presentation_editor.md` whenever `htmls/03_presentation_mode.md` is active, or when the user explicitly asks for an editable post-generation presentation surface;
- load `htmls/presentation_editor_verification.md` only at the delivery/verification gate for an editor-enabled artifact;
- additionally load `htmls/04_multi_html_packages.md` when the request is for an ordered package or coordinated set of multiple HTML files;
- load `htmls/static_pdf_export.md` only when the user requests a PDF or another static derivative from HTML.

Presentation navigation and presentation-editor chrome do not by themselves activate `interactive_controls.md`; their specialized modules own those controls.

When an HTML teaches, explains, publishes, or presents material owned by another content domain, apply that content domain as well. The HTML domain controls implementation and presentation behavior, not subject-matter truth.

## Workflow precedence

**Invariant:** For HTML work governed by this repository, follow the routing, phase gates, review workflow, and verification requirements defined by the selected HTML modules and applicable content-domain modules before generic external development methodologies or skills. Do not add auxiliary process or working artifacts unless they are required by the selected repository workflow, the task, or materially improve verification.

This precedence does not weaken correctness requirements. HTML artifacts still need to be implemented and verified carefully enough for reliable live use, but they are presentation and teaching artifacts unless the user explicitly says they are production web applications.

## Delivery baseline

**Default:** Produce a self-contained HTML artifact that opens directly from `file://` without a build step, server, package installation, or network dependency. Allow remote assets only when the user explicitly requests them or the requested brand/resource genuinely requires them.

Target current Chromium behavior that works correctly in both Chrome and Edge. Prefer semantic HTML, CSS layout primitives, and small dependency-free JavaScript over framework-like complexity.

Keep reading mode functional without JavaScript whenever practical. JavaScript may enhance interaction or presentation behavior, but it should not be required merely to reveal the main content.

## Public-facing cleanliness and AI traces

**Invariant:** Unless the user explicitly asks for provenance, source notes, AI diagnostics, generation metadata, or presenter-only information, the visible HTML must contain only audience-facing content and must not expose internal production, provenance, debugging, or workflow metadata.

**Invariant:** Internal ownership or production-context labels are metadata, not audience content. This includes labels whose purpose is to identify who owns or presents a block, which source file or source section supplied material, how responsibilities were divided, or how the artifact was assembled. Use such information internally to select and organize the correct content, then omit it from headings, badges, captions, slide labels, footers, or other visible HTML unless the user explicitly says that label itself belongs in the audience-facing material.

Research and verification may still be performed internally when another domain requires them. Keep that process out of the public artifact by default. If the user explicitly requests citations or a bibliography, present human-readable references appropriate for the audience rather than internal working-file names.

**Default:** For educational or presentation HTML, treat the visible artifact as learner-facing unless the user explicitly asks for presenter metadata. If presenter notes or delivery annotations are requested, keep them clearly separate from the learner-facing content rather than mixing them into the main teaching surface.

Do not add self-descriptive implementation or capability labels unless the label itself has a user-facing function.

## Verification gate

**Invariant:** Never deliver a created or revised HTML without applying `htmls/05_verification.md`. If structured visuals, presentation mode, stateful learner-facing interaction, the presentation editing layer, or static export are present, also execute the verification requirements defined in their selected modules. For the presentation editor, the concrete delivery matrix is owned by `htmls/presentation_editor_verification.md`.
