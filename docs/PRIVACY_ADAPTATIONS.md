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

## GitHub domain: three ownership references

Each source file was fetched from current private DIK. Only occurrences of the original owner's possessive personal name were replaced by the neutral phrase `the user's`. No algorithm, branch, condition, path, field, example, or surrounding punctuation was changed.

### Shared GitHub core

- Published path: `info_for_ai/github/00_core.md`
- Canonical source Git blob SHA: `9fccfd155f93e6ba9b4464a414f5eba5248cc1f7`
- Published Git blob SHA: `c2484e42e7e15e44162c7d19f7b24c8683d6569c`
- Exact change: line 9, replace **one** original owner-name possessive phrase with `the user's`. No other changes.

### Repository inventory and scope

- Published path: `info_for_ai/github/repository_inventory_and_scope.md`
- Canonical source Git blob SHA: `7035b0b2fde07c1b41d5d8c4471c41217983fdbd`
- Published Git blob SHA: `64e93ee6a70b957d585bcca8ffad4ddaa66151b7`
- Exact changes: lines 5 and 17, replace **one** original owner-name possessive phrase at each location with `the user's`. No other changes.

### GitHub repository entry template

- Published path: `info_for_ai/github/plantilla_entrada.md`
- Canonical source Git blob SHA: `8ea0f9cede81d3fa6cba718a5a50e5f2fe2aca45`
- Published Git blob SHA: `9a89b4b4cf7d46aacf76cd2deb77851d8bee8183`
- Exact change: line 13, replace **one** original owner-name possessive phrase with `the user's`. No other changes.

For all three files, exact source-text substitution and full-text target comparison were performed against the canonical private source and the branch copy, with zero extra differences. The deleted private name is redacted in this public diff ledger to avoid redisclosing a personal identifier; these source/published hashes and line positions are sufficient to reproduce and independently audit the nonredacted diffs with access to DIK. The maintained private repository inventory referenced by the original procedures is not redistributed or replaced with fabricated entries.

## Codex prompting module

- Published path: `info_for_ai/prompting/01_codex_prompt_generation.md`.
- Canonical source Git blob SHA: `2d7dc003395b8407e571dbb8bcf3af2b3507d558`.
- Published Git blob SHA: `ef81d9e85b658c3f5a1ee5976cf20502a14fb665`.
- Manifest status: `privacy-adapted`.
- Exact privacy substitution: canonical line 38, replace the **single possessive occurrence of the private original owner's first name**, leaving every surrounding character unchanged, with `the user's`. The public ledger redacts the removed private given name; the complete exact textual diff is reproducible using the recorded canonical source hash under authorized DIK access.
- Verification: applying exactly this one substitution to the source text yields the entire published blob with no additional differences. All original instructions, dependency paths, procedure ordering and conditional behavior remain intact.
- Rationale: make the hard-coded personal owner reference neutral without redefining the original Codex-prompt workflow.
- Outstanding portability limitation: references to the original `dokos-instructions-knowledge` checkout and Dokos Knowledge remain literal because changing them could change dependency behavior. Migration of the global Knotbase runtime and any configuration of this dependency require separate review; no runtime portability is claimed.

## Blog writing domain

Four source files have only owner-identity privacy substitutions. Their complete canonical content, after precisely the listed substitutions, has been compared to the published files with **no other differences**. All substantive instructions and the workflow's original phase ordering are retained. Personal source identifiers are redacted from this public record; exact original spans are reproducible from the recorded source hashes by an authorized reader of DIK.

### Editorial core

- Path: `info_for_ai/blog_writing/00_core.md`
- Canonical Git blob SHA: `60ffbc848cac318f86ac3fb770f61c915dc4f9ab`
- Published Git blob SHA: `2c96416110d0b0c196c9b8b0c9f2c607e4e88386`
- Exactly two replacements: canonical line 1, original owner's full name in the headline becomes `del usuario actual` (the preceding `de` is included in the replaced span); line 20, original owner's given name in the criterion becomes `del usuario actual` (the preceding `de` is included). All other text unchanged.

### Argument architecture

- Path: `info_for_ai/blog_writing/01_arquitectura_del_razonamiento.md`
- Canonical Git blob SHA: `6da93c3dc5a6f4a021fd1ff4a2c7ae87035965b8`
- Published Git blob SHA: `0c62994c7e2b951ddd549ec88ef5165df5056678`
- Exactly one replacement: canonical line 73, the original explicitly owner-named article-inventory path becomes `info_user/articulos_medium_linkedin_usuario.csv`. The rest of the paragraph is unchanged.
- **Dependency limitation:** the private article inventory is not published; the generic counterpart must be supplied by the eventual runtime/user data layer. This replacement is privacy-driven, not evidence that the generic article inventory currently exists.

### Editorial voice and rhythm

- Path: `info_for_ai/blog_writing/02_voz_pedagogia_y_ritmo.md`
- Canonical Git blob SHA: `aded78e14de03e43bf9da4ddb83859164ae853d8`
- Published Git blob SHA: `961f3646be66f488d8e22ffae9c3fbb83bee8845`
- Exactly one replacement: canonical line 5, `de` plus the original owner's given name becomes `del usuario actual`. Surrounding text unchanged.

### Publication materialization

- Path: `info_for_ai/blog_writing/publication_materialization.md`
- Canonical Git blob SHA: `984e76accebf4d67df26523dde9871b85d184675`
- Published Git blob SHA: `9ad2bdb918079936f5387eca93efb19f8e14c33a`
- Exactly two replacements: canonical lines 3 and 138, each original owner's given name preceded by `de` becomes `del usuario actual`. Other content, including the original required Spanish LinkedIn closing phrase, is unchanged.

The remaining four files in this domain have byte-identical original and published Git blob SHAs. None of these changes establishes functional runtime parity, and no original author-specific data file is transferred.

## Bilingual interactions domain

Ten of the 16 original files contain owner-specific references. Exactly **17 substitutions** were made to neutralize those references, while preserving all shared workflow behavior, activation conditions, language branches, recipient restrictions and substantive procedures. The other six files were copied byte-for-byte.
**Exact diff convention:** source-name spans are not reproduced verbatim in this public adaptation ledger to avoid re-disclosing personal identifiers. Each affected span is identified by its original line number and its exact neutral published replacement. The original deleted span is recoverable from the specified original Git blob under authorized DIK access. Full original-text plus exactly these substitutions matched the entire published file, with no additional differences.

### `info_for_ai/interactions/00_core.md`

- Canonical source Git blob SHA: `e53705f88ab9283c428b00544f6c060cbfaba081`.
- Published Git blob SHA: `fcfee5b6c7f0f47daba367e3032381c1607810a5`.
- Exact privacy diff: canonical line 29, the original owner's given name in the rejection authorization clause becomes `el usuario actual`; all surrounding text remains exactly unchanged.
- Rationale: remove a personal hard-coded authorization subject without altering the prohibition on promising future possibilities without authorization.

### `info_for_ai/interactions/indice_interactions.csv`

- Canonical source Git blob SHA: `6fddf7ac339d3f3b79127fc9b6012d0dbdb93823`.
- Published Git blob SHA: `cc1954d8c88104d8877217ea5ad0946ee8fa03b9`.
- Exact privacy diff: line 5: Spanish possessive owner phrase becomes `del usuario actual`; line 12: English owner possessive becomes `the user's`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/es/02_correo_personal.md`

- Canonical source Git blob SHA: `8dab8bc913320a5112f0e0992eb4e16090ecc35b`.
- Published Git blob SHA: `78d1d4850ec6078b89bb1c37340b1f861bb601ea`.
- Exact privacy diff: line 5: `de` plus original owner given name becomes `del usuario actual`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/es/03_correo_empresa.md`

- Canonical source Git blob SHA: `54d9c11b629d53d0a7b27dd2b906ca74179cd36f`.
- Published Git blob SHA: `adbcd9665f890a34a7e3b79598db165c7dea76ad`.
- Exact privacy diff: lines 5 and 9: at each location, `de` plus original owner given name becomes `del usuario actual`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/es/04_primer_contacto.md`

- Canonical source Git blob SHA: `f2f6a6c90bcda6b2d11a46bdb35545ca2fb2a5e5`.
- Published Git blob SHA: `1bf3851f581ac456395d716a3e28956f0bc7e3fb`.
- Exact privacy diff: line 15: `de` plus original owner given name becomes `del usuario actual`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/es/06_carta_recomendacion.md`

- Canonical source Git blob SHA: `70cd7bfb9e20f9baebedbeec72798c42e1940f58`.
- Published Git blob SHA: `c1ecf15ed901ae9f835ba0c0e14dc8057654f2f4`.
- Exact privacy diff: line 5: `de` plus original owner given name becomes `del usuario actual`; line 11: original owner given name after `relación` becomes `el usuario actual`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/en/02_personal_email.md`

- Canonical source Git blob SHA: `6284eb7389e8c9397a69ab514f34769ce56419c8`.
- Published Git blob SHA: `28ffa0849c138a61c320d23cd0c13c229d2708a2`.
- Exact privacy diff: line 5: owner-name possessive becomes `the user's`; line 13: plain original owner name becomes `the user`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/en/03_company_email.md`

- Canonical source Git blob SHA: `a6ffabcdf1b0d8387a3cf387e95cc0b983de8825`.
- Published Git blob SHA: `418b50fd008956bbea851bca0b108703a178c4ab`.
- Exact privacy diff: lines 5 and 9: owner-name possessive becomes `the user's` once in each line.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/en/04_first_contact.md`

- Canonical source Git blob SHA: `2b25dbfe2a18a0c2844d5a0e750c2e9c1e1f23db`.
- Published Git blob SHA: `6462a618422548a67a7f95a049838ece080ac00f`.
- Exact privacy diff: line 15: owner-name possessive becomes `the user's`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

### `info_for_ai/interactions/en/06_recommendation_letter.md`

- Canonical source Git blob SHA: `38157fc479c6ada29ad531946f5f7e2472dd1217`.
- Published Git blob SHA: `b63b6c1d83965be8e92e38a4c404b15f74e7af31`.
- Exact privacy diff: line 5: owner-name possessive becomes `the user's`, and original male-specific `why he recommends` becomes `why they recommend`; line 11: original owner name plus `is` becomes `the user is`.
- Rationale: remove the hard-coded original owner or gender reference while maintaining the unchanged workflow contract.

The Spanish/English optional style notes, LinkedIn replies and project-delivery modules are literal original copies. The shared core requires the single owner-name substitution documented above. No email addresses, signatures, third-party content or private accounts have been published. As in other domains, privacy substitution and source parity do not constitute end-to-end command-runtime verification.