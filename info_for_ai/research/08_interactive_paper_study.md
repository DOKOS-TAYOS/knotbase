# Interactive paper study HTML

## Activation

Use this module when the user supplies a LaTeX paper project, normally as a ZIP, and wants to study the original paper through a progressively enriched interactive HTML artifact. This workflow is distinct from an ordinary `#READ`: it is iterative, artifact-producing, and advances through direct-continuation `ok` turns.

Read `research/00_core.md` first. Reuse the evidence and study-mode rules from `research/02_paper_explanation.md` rather than duplicating them here. Apply `../iterative_continuation.md` as the shared contract for direct-continuation state and isolated `ok` advancement.

## Outcome contract

**Invariant:** Completion produces exactly one self-contained `.html` artifact. That file contains the authoritative compiled paper copy, the complete primary reading surface, all study explanations, page and annotation data, and required runtime assets. It must open locally without sibling files, network access, a PDF plugin, or browser-native PDF embedding as the required reading surface.

The final artifact must:

- preserve the verified original compiled PDF as the canonical source copy embedded inside the HTML;
- use embedded rendered page images as the primary paper-reading surface;
- render mathematical explanations visibly, preferably as standards-based MathML assembled before delivery;
- let every annotation navigate to its 1-based paper page and named target;
- provide a visible clickable page marker for every annotation and an optional translucent target-region overlay only when normalized coordinates are evidence-backed;
- keep paper markers/overlays and selected notes synchronized while visually separating study explanations from the authors' original content;
- provide responsive wide-screen split paper/notes reading and a direct paper/notes switch on narrow screens;
- remain touch-friendly, safe-area aware, free of page-level horizontal overflow, and locally scrollable for long mathematics or code where necessary.

Use the paper's actual title as the output filename when it can be determined reliably. Sanitize only invalid or unsafe filename characters and repeated whitespace. If the title cannot be established reliably, use `paper-study.html`.

## Source handling

1. Treat the supplied LaTeX project as read-only source material.
2. Unpack it into an isolated working directory.
3. Identify the main document, included files, bibliography, figures, macros, and existing compiled PDF when present.
4. Compile the project when a compatible local TeX toolchain is available, preferring the project's documented build command and otherwise the smallest conventional build path that preserves the manuscript.
5. If compilation is unavailable or fails for an environmental reason, use a trustworthy compiled PDF already present in the project. If no readable PDF can be obtained, report the blocker instead of fabricating a representation.
6. Preserve title, authors, section structure, equation numbering, figure/table numbering, labels, bibliography links, and page references whenever recoverable.
7. During final assembly, rasterize the verified PDF at a practical resolution that keeps normal text and equations crisp without making file size needlessly large.

## Iterative state machine

In this workflow, the unit pending under `../iterative_continuation.md` is one recorded phase: preparation, one study unit, or final assembly. The initial invocation performs preparation. Each later isolated `ok` can authorize exactly the next recorded phase, and a blocked phase remains current under the shared blocker contract.

Working files are internal implementation artifacts and never part of normal final delivery. Maintain an internal manifest containing at least paper identity/title, source and PDF paths, ordered study units, current/next phase, completed notes, annotation identifiers/locations, unresolved blockers, and final output filename.

### Phase 0: preparation and study map

On the initial invocation:

1. inspect the complete project and obtain the readable paper PDF;
2. read enough of the full paper to understand its contribution, argument, notation, prerequisites, dependencies, important equations/figures/appendices, and likely cognitive bottlenecks;
3. create internal `00_plan.md` and the state manifest;
4. divide the paper into ordered critical study units sized for deep analysis rather than mechanically matching editorial sections;
5. isolate unusually dense equations, proofs, algorithms, conceptual transitions, or result interpretations when useful, and combine easy neighboring material when separation adds no value;
6. stop after a concise preparation summary and identification of the next unit.

### Study-unit phases

For each subsequent `ok` while study units remain:

1. process exactly the next pending unit;
2. reread the relevant source, PDF pages, definitions, equations, figures, appendices, and dependencies;
3. create one internal Markdown note using a stable numeric prefix;
4. add only explanations that materially improve understanding;
5. update the manifest and stop.

A study-unit note should include, as applicable, the exact paper location, local argumentative purpose, omitted derivation steps, required definitions/notation, intuition, assumptions, examples/limits, cross-connections, clearly separated external context, proposed annotation title/type, and optional evidence-backed normalized page coordinates.

Do not annotate every paragraph. Prefer high-value explanations over annotation density.

### Final assembly phase

When no study units remain, the next `ok` performs exactly final assembly:

1. review internal notes for notation consistency, duplication, unsupported claims, broken references, and conflicts with the paper;
2. resolve the ordered annotation set and page targets;
3. open the indexed `paper-study-html-template` asset and use it as the visual/runtime base;
4. assemble the single final HTML so it satisfies the Outcome contract above, embedding the verified PDF copy, rendered page images, visible mathematics, annotation data, page markers, and only evidence-backed overlays;
5. replace all template placeholders and ensure none remain;
6. verify the artifact locally against the complete Outcome contract, including page count/order, annotation navigation and synchronization, marker behavior, responsive wide/narrow reading modes, touch targets, safe areas, horizontal overflow, and absence of required sibling/network resources;
7. deliver only the final HTML unless the user explicitly requests diagnostic working material.

After final assembly no pending unit remains. Under `../iterative_continuation.md`, a later isolated `ok` does not restart the study or invent an additional phase.

## Annotation and navigation semantics

Preserve the reusable template's data semantics:

- stable unique annotation `id`;
- 1-based `page`;
- human-readable `target`;
- short pedagogical `title`;
- compact `type`;
- one- or two-sentence `summary`;
- safe semantic `bodyHtml` with visible mathematics;
- `sourceKind` distinguishing paper, derivation, inference, and external context when material;
- optional normalized `anchor` `{x, y, w, h}` in `[0,1]`, omitted unless robustly mapped and geometrically valid.

The page-image data is an ordered JSON array containing page number, image MIME type, and embedded image data, with optional intrinsic dimensions. Embedded JSON must be escaped safely, including `<` where needed to prevent premature script termination.

Page-level clickable markers are mandatory for every annotation. Coordinate overlays are optional enhancements and must never be fabricated. On narrow screens, annotation navigation must switch directly to the relevant note view; returning to the paper should navigate to the correct page and, when practical, center an available anchor.

## Direct-continuation behavior

Direct-continuation identity, isolated `ok`, substantive user messages, blockers, and state integrity are governed by `../iterative_continuation.md`. This module adds only the requirement to keep its manifest synchronized with the active phase and paper-study state.

## Quality bar

The artifact is a study layer over the paper, not a substitute manuscript or generic summary. Keep the reader anchored to the authors' original sequence and add explanations where they reduce the cost of understanding omitted reasoning, prerequisites, notation, assumptions, derivations, interpretation, or cross-connections. Avoid paraphrasing passages that are already clear merely to increase coverage.
