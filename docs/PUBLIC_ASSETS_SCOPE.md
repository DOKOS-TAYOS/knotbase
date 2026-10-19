# Public reusable runtime assets — PR #19

This scoped publication provides the two original, generic, self-contained HTML resources required by the **already-published** research and HTML instruction modules. The private DIK repository is unchanged.

## Canonical origin and target

| Published file | Canonical DIK blob SHA | Public blob SHA | Status |
|---|---|---|---|
| `assets_for_ai/paper_study/paper_study_template.html` | `0aa057406d3965f6d2566825afb86b739fc62aa3` | `0aa057406d3965f6d2566825afb86b739fc62aa3` | `verbatim` |
| `assets_for_ai/htmls/presentation_editor_base.html` | `349765691f9e11cddf8b37e4bb652fa089747968` | `349765691f9e11cddf8b37e4bb652fa089747968` | `verbatim` |
| `assets_for_ai/indice_assets.csv` | `5e30265f9ca7c0b527bb1c0d73e81f8ae249c32a` | `704e474130388d50cd8d865c28811b443d92b1a2` | `privacy-adapted` |
| `assets_for_ai/indice_assets_lookup.csv` | `27ef2b23cce4e3a250d51969d04e9ff0faa362bc` | `7b40af1e6a185878a5fbafae7e49ca9ea7418a7c` | `privacy-adapted` |

The public indices contain **only** `paper-study-html-template` (line 2) and `presentation-editor-html-base` (line 3), with paths resolved relative to `assets_for_ai/` exactly once. The original private DIK indices enumerate additional portraits, templates, icons and unpublished assets, none of which are included here.

## Contracts enabled

- **`#PAPER`**: the final assembly step in `info_for_ai/research/08_interactive_paper_study.md` can load the canonical paper-study HTML runtime. It must still use a user-provided LaTeX project, compile/verify the actual paper, preserve the multi-phase isolated-`ok` gates, embed the final page images and PDF, and check the rendered output before claiming delivery.
- **`#HTML` presentation editing**: `info_for_ai/htmls/presentation_editor.md` can locate its canonical, reusable editor runtime. The runtime is a technical reference, not a mandatory content layout or an excuse to include demonstration content. Load `presentation_editor_verification.md` at the delivery gate and confirm clean authoring-chrome-free export.

These resources contain demonstration text, placeholders and UI code; they are not applicant facts, personal data, finished study results, a compiled scientific paper or a user-ready published presentation. Replace or remove demo placeholders when creating an artifact. Asset identity, internal indices and file integrity can be checked statically; **actual HTML behavior and PDF/visual verification remain untested** until final consumer acceptance.

A source scan found no original-owner identity names, private addresses or network asset dependencies in these two source files. A scan cannot establish security or license ownership for arbitrary derivatives; maintain the normal source and media provenance checks when creating new content.

## Ledger

The parity manifest now contains **139** unique canonical-source records: 105 `verbatim`, 21 `privacy-adapted`, 3 `privacy-and-editorial-adapted`, 1 `authorized-editorial-adapted`, 5 `authorized-workflow-adapted`, 3 `public-routing-adapted`, 1 `public-subset-adapted`. Exactly four records were added to the previous 135-source ledger. Historical counts in earlier migration checkpoint sections are retrospective.
