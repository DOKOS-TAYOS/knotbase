# Privacy-only adaptations from canonical DIK

This document records intentional minimal privacy substitutions in the published source batches. Unlisted source files in `manifests/source_parity.csv` are required to preserve their canonical Git blob SHA exactly.

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

## Code domain core

- Published path: `info_for_ai/code/00_core.md`
- Canonical source Git blob SHA: `b38e402d6fd61ad946d46a8ca1dedf2bc54fe781`
- Published Git blob SHA: `f8ee8906f657852bb5fb747d8c534858512f2ecf`
- Manifest status: `privacy-adapted`
- Modification: **exactly two reference replacements**, in the clause that identifies the current GitHub-repository owner and the clause that identifies the subject of personal-fact lookup. Both refer to the current user rather than a hard-coded original owner.
- Verification: applying only those two replacements to the canonical text reproduces the complete published file exactly.
- Remaining limitations: the code domain index, repository-identity module and global command dispatcher are not yet published. This is not an operational code-domain installation.

## Code repository identity

- Published path: `info_for_ai/code/01_repository_identity.md`
- Canonical source Git blob SHA: `0c1231b1b27d47511e041da7e3531ac8070da2d0`
- Published Git blob SHA: `923c1a9805f592ec39840c3b897d54cd142335ca`
- Manifest status: `privacy-adapted`
- Exactly three source-to-target substitutions (line numbers in the canonical 33-line source):
  1. Line 9, bold author-name value: replace the original personal full name with `[configured author name]`, retaining the surrounding bold markers.
  2. Line 10, backticked professional-contact value: replace the original personal email with `[configured professional contact]`, retaining the surrounding backticks.
  3. Line 18, authorship-conflict clause: replace `attribute work to [PERSONAL NAME] that is not his` with `attribute work to the user that is not theirs`.
- All other bytes are unchanged. Verification: the original private canonical file with **only** the three exact substitutions applied matches the published file in full, including its final newline.
- Privacy-preserving diff record: the original name and email values are intentionally redacted in this public ledger, rather than republished as deleted lines. The full exact source-to-target comparison was executed against DIK's private source, with zero additional differences.
- Rationale: replace owner-specific defaults and a personal attribution reference with user-configurable or neutral wording while preserving the legal/editorial procedure.
