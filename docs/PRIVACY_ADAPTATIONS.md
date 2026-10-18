# Privacy-only adaptations from canonical DIK

This document records the **only intentional text difference** in the fourth public source batch. Unlisted source files in `manifests/source_parity.csv` are required to preserve their canonical Git blob SHA exactly.

## Paper entry template

- Published path: `info_for_ai/papers/plantilla_entrada.md`
- Canonical source Git blob SHA: `52af649b185998ea928516498350c51bfb2ac54c`
- Published Git blob SHA: `b0777286669c5df2840f1a001e5fd4fafc2c86a6`
- Manifest status: `privacy-adapted`
- Modification: **one Markdown section heading only**. Replace the personal name in the heading describing how a paper relates to its owner's work with the neutral wording `## Relation to the user's work`.
- No other characters, instructions, algorithms, sections, ordering or placeholders were changed.
- Purpose: avoid embedding the original owner's identity as the default subject of a reusable public template.
- Verification: compare the canonical source with the published file after applying precisely that one heading substitution; their contents must then match exactly.

The remaining 10 files in the `papers` batch were copied verbatim. The overall package remains an incremental source publication, not an operational command runtime.
