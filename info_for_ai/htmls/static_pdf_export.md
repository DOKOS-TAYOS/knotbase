# Static PDF export from HTML

Open this module only when the user requests a PDF or another static derivative from one or more HTML artifacts.

Apply `htmls/00_core.md` and `htmls/05_verification.md`. When presentation mode exists, also apply `htmls/03_presentation_mode.md`; its presentation order, composition, and visible states are canonical for the export. When no presentation mode exists, derive the PDF from the current reading-mode structure without inventing a parallel content source.

## Export contract

**Default:** Treat the PDF as a derivative of the current HTML, not as an independent authoring source.

- Produce one PDF per HTML in the requested scope, preserving package order and normally reusing each HTML basename. Combine several HTMLs only when the user explicitly requests a combined PDF.
- When presentation mode exists, export at least one page per presentation step and preserve instructional order and hierarchy.
- Without presentation mode, preserve the reading order and use natural page breaks or coherent section breaks rather than manufacturing slide semantics.
- Omit navigation-only chrome and authoring chrome that have no useful static representation.
- For mutually exclusive explanatory selectors whose options reveal materially different teaching content, export one page per meaningful option with that option visibly active.
- Do not multiply pages for states that only sort, filter, recolor, decorate, or otherwise change presentation without adding materially different explanatory content.
- For independent progressive disclosures, normally export one complete state with all meaningful disclosures open. Reflow or split only when needed for legibility.
- For continuous or combinatorial controls, choose the smallest pedagogically distinct state set rather than an exhaustive Cartesian product.
- Do not add new teaching content, internal metadata, provenance notes, or working-state labels solely for export.

## Editable presentation sources

When the source includes the presentation editor, the PDF must reflect the accepted visible content state while omitting editor chrome, selection outlines, editability metadata, temporary authoring state, and other editor-only surfaces. Apply `presentation_editor_verification.md` before delivery when the editor is active.

## Verification

Verify the produced PDF itself, not only the source HTML. Check representative pages for ordering, clipping, missing content, unintended chrome, broken images or diagrams, unreadable scale, and state-selection mistakes. When several HTMLs are exported, confirm scope and filename/package ordering against the requested set.
