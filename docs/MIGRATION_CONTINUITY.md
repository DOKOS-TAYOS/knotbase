# Migration continuity and public integration contract

This file is a durable handoff for future Knotbase migration sessions. It documents the verified **public** repository state and the owner's non-negotiable acceptance criteria. It does not replace canonical instruction files.

## Canonical-source fidelity: mandatory

- Canonical instructions, algorithms, schemas, routing rules, contracts, phases, ordering, conditions, exceptions, and examples must be preserved **exactly** when transferred into Knotbase.
- Start from the latest actual canonical source file, not a summary or a previously generalized candidate. Do not paraphrase, simplify, redesign, optimize, modernize, or infer equivalent behavior.
- If the file is publishable as-is, copy it byte-for-byte. If it contains personal information, substitute **only** the smallest necessary spans with neutral/configurable equivalents. Document each change and prove that applying exactly the authorized substitutions to the source recreates the published file. Any unrelated difference blocks integration.
- Deliberately excluded functionality must be explicitly authorized and narrowly isolated; **Europass and related branded templates/assets are excluded**. Do not use that exclusion to rewrite unrelated contracts.
- Keep private/restricted content, identifiable profile/contact records, local private archive files, secrets, internal repository inventories, and third-party material without redistribution rights out of the public repository.
- Never modify the canonical private repository during this public migration unless the owner separately authorizes that change.

## Publication strategy

- Work directly with the existing public `DOKOS-TAYOS/knotbase` repository; a private staging repository is **not required**.
- Publish small coherent verified source batches as they become safe, without waiting for whole-project completion.
- For each batch: inspect live source and target state, prepare an isolated branch, review privacy and licensing, check diff/PR scope, compare Git blob SHAs, update the provenance manifest and privacy-delta documentation as required, check applicable tests and CI, merge by repository policy, and **reverify files on `main`**.
- A Git branch and PR in this repository are publicly visible even before merge: do not upload sensitive material to a draft PR.
- Treat tool/policy blocks as genuine blockers; do not evade them. A partially prepared branch is not an integrated release.
- No broad release, tag, or functional-parity approval has been given. Source publication is not runtime readiness.

## Verified public baseline (2026-10-18)

The first six pull requests (#1 through #6) were merged on `main`. At this handoff, `manifests/source_parity.csv` contains **75 unique source-file records**: **73 `verbatim`** and **2 `privacy-adapted`**. All 75 published blobs have been checked against the recorded target: verbatim rows match their recorded source blob SHA; the two adapted rows match the independently documented published blob SHAs. Both adapted files were additionally compared against their current canonical source text with precisely the documented substitutions.

- `code`: 15 initial verbatim source modules, plus the privacy-adapted domain core and verbatim knowledge template from PR #5. **Incomplete**; the canonical domain index and repository-identity module remain absent.
- `github`: eight verbatim workflow modules. **Incomplete**; core, index and other dependencies remain absent.
- `research`: original complete domain source (11 files).
- `papers`: original index, workflows and template (11 files; one template-heading privacy adaptation).
- `education`: complete original domain source (28 files), including core, index, workflows, audience profiles and note-writing rules. All 28 published blobs match the manifest.

The two privacy changes and original/published hashes are recorded in [PRIVACY_ADAPTATIONS.md](PRIVACY_ADAPTATIONS.md). The source SHA ledger is [source_parity.csv](../manifests/source_parity.csv). Merged PRs: [#1](https://github.com/DOKOS-TAYOS/knotbase/pull/1), [#2](https://github.com/DOKOS-TAYOS/knotbase/pull/2), [#3](https://github.com/DOKOS-TAYOS/knotbase/pull/3), [#4](https://github.com/DOKOS-TAYOS/knotbase/pull/4), [#5](https://github.com/DOKOS-TAYOS/knotbase/pull/5), [#6](https://github.com/DOKOS-TAYOS/knotbase/pull/6).

No complete application runtime is currently asserted. The global `AGENTS.md`, cross-domain index, command registry/lookup, full code/GitHub routing and related prerequisites are **not yet installed**. Do not present copied source modules as registered commands. The last inspected main commit had no reported combined CI status contexts; this is **not evidence of passing CI**.

## Next migration checkpoints

1. Recheck live remote state, PRs, branch policies, the source ledger, privacy-delta records and any changes since this handoff.
2. Finish `code` and `github` cores/indices and outstanding modules from original source with fidelity validation. The canonical `code/01_repository_identity.md` contains owner-specific author/contact defaults; publish only after minimal privacy substitutions. Past tool safety controls blocked attempted writes of that module and `code/indice_code.csv`; verify what is actually possible, and **do not circumvent a block**.
3. Continue other index-listed domains through source-first copying and minimal, individually audited privacy substitutions. Pay particular attention to personal profiles, style, credentials, paths, letters and assets.
4. Bring over the original global `AGENTS.md`, domain index, command registry and physical lookup only when their references can be accurately generalized and their dependent files are present. Preserve routing semantics; never invent or register incomplete commands.
5. Validate index paths, referenced module existence, command lookup/registry consistency, privacy and licenses, applicable automated tests and actual end-to-end workflows. Maintain clear distinctions among source fidelity, technical validation and functional parity.
6. The previously developed local HTML/CV/PDF/DOCX implementations and private Phase 16 review archives are **not in this public repository merely because they exist locally**. Audit any future code integration separately for original-contract fidelity, privacy, third-party rights and runtime acceptance. Do not restore Europass. Do not activate `#CV` or `#CVEDIT` merely from synthetic tests.

## Handoff procedure for a fresh conversation

Read the live canonical private repository's `AGENTS.md` directly at the start of the new task and follow its indexed routing before interpreting commands or choosing a procedure. Use this public document only as historical, non-authoritative migration state; refresh all critical GitHub evidence. Work in Spanish with the owner. Continue meaningful, bounded public integrations rather than creating more throwaway generalized instruction sets or waiting for the entire migration. Report exact verified PRs, on-`main` source parity, missing prerequisites and blockers without claiming full functional readiness.

Last verified main immediately before this handoff document: `b3b0b5c1791e7be83023bcde220b169af185e308` (PR #6).

## Code-domain completion checkpoint (2026-10-18)

The original `info_for_ai/code/indice_code.csv` was copied verbatim with Git blob SHA `85d85f9f45d12dfc272594b8b658e770d35b07d7`. The original `info_for_ai/code/01_repository_identity.md` was copied with only three individually documented personal-reference substitutions (canonical blob `0c1231b1b27d47511e041da7e3531ac8070da2d0`; public blob `923c1a9805f592ec39840c3b897d54cd142335ca`). Exact substituted-source comparison established no additional changes.

The missing original `info_for_ai/code/08_integration_preparation.md` was also copied verbatim (Git blob SHA `69a8aa36542c12b1cfc1728398b42e76f94a5ea2`). The code index's 19 file entries all correspond to files present in the publication batch. Its source domain is complete, but the global routing/command system and original personal-data dependencies are not yet installed, so **functional parity is not established**.

The source-parity ledger now has **78 records: 75 verbatim and 3 privacy-adapted**. These counts describe migrated source files, not verified runtime behavior. GitHub core and outstanding domain modules remain priorities.

## GitHub-domain source checkpoint (PR #9)

The complete original `info_for_ai/github/` instruction source set is included in PR #9 as a **source-only** migration: 14 files including the original index. Its index lists 13 files, all present. The three newly published verbatim sources have matching Git blob SHAs to DIK:

- `indice_github.csv`: `97f314bc5509918b31292426cd472396ddea4dbb`.
- `02_dependabot_review.md`: `8ddb37b6d8aba8c539a7b15f322b7881349a6074`.
- `09_repository_triage.md`: `071d5e56bf2e1c966ccb9d97976b54e271ce03f5`.

The other three newly published sources have only four original-owner possessive-name substitutions in total: one in `00_core.md`, two in `repository_inventory_and_scope.md`, and one in `plantilla_entrada.md`. Full canonical-to-public substitution comparison found no other differences. Source and published hashes and positions are recorded in `docs/PRIVACY_ADAPTATIONS.md`.

Following integration, `manifests/source_parity.csv` records **84 source files: 78 verbatim and six privacy-adapted**. The original personal repository inventory has not been published; the source package does **not** provide a functioning, tested global command runtime.

**Known documentation limitation:** a security-control block prevented updating `README.md` in this batch. It still displays the historical 78-file count and describes the GitHub domain as incomplete. The authoritative current migrated-source inventory is the CSV manifest, not that earlier README snapshot. Do not attempt to bypass controls to amend the README. Correct it only when the normal permitted GitHub edit becomes available.

## Prompting-domain source checkpoint (PR #10)

The original `info_for_ai/prompting/` source domain is published as five source files, including the canonical four-row domain index. Four files are copied byte-for-byte and preserve their source Git blob SHAs:

- `00_core.md`: `44a259bc90ac34bc1c75e70f667a9ebdc2ca0de3`
- `indice_prompting.csv`: `480a791ea43b9bd04e5f7600d421b3581b6d8323`
- `01_prompt_generation.md`: `f416f334d9cea91794a859663e83d21bfc2114c7`
- `02_chat_prompt_generation.md`: `258c8a8ab856aecf6fd9323b9155d8bc30ce5301`

`01_codex_prompt_generation.md` (canonical Git blob `2d7dc003395b8407e571dbb8bcf3af2b3507d558`; published `ef81d9e85b658c3f5a1ee5976cf20502a14fb665`) has precisely one owner-name privacy substitution on original line 38; its complete content otherwise matches DIK. See `docs/PRIVACY_ADAPTATIONS.md` for the exact verification rule.

After this source-only integration, `manifests/source_parity.csv` has **89 distinct entries, 82 verbatim and seven privacy-adapted**. The original Codex module's dependency on a local `dokos-instructions-knowledge` checkout was **not** reinterpreted or redesigned for Knotbase. This source is not yet a general-purpose functioning runtime. The global routing and command dispatcher, personal inventory substitution, integration tests, and actual functional proof remain pending.

The README retains the earlier historical count owing to the previously documented blocked GitHub edit. The source ledger and this continuity appendix contain the later verified counts. No alternate path has been used to bypass the security control.

## HTML-domain generic source checkpoint (PR #11)

This integration adds **11 original, byte-for-byte identical HTML-domain source files** under `info_for_ai/htmls/`, including the shared core, generation and interaction, stateful controls, visuals, presentation mode, presentation editing and verification, static PDF export, multi-HTML packages, general verification, and the generic entry template. Every published file's Git blob SHA equals the corresponding live DIK source SHA recorded in `manifests/source_parity.csv`. No privacy transformation is necessary for these 11 files.

**Intentionally not yet included:** the original HTML-domain index and one recipient-specific interactive-letter workflow with personal content and a separate asset dependency. Neither is to be reconstructed or silently replaced with a shortened version. The original full domain index cannot yet be asserted as operational in Knotbase. No personal template assets, media, or private archives have been published.

Following this batch, the source ledger has **100 distinct source-file records: 93 verbatim and seven privacy-adapted**. This remains a source-only checkpoint, not an implementation of the separately developed HTML/PDF/DOCX runtime, nor evidence of working editor/export features. The global router, command registry and real behavioral tests remain pending.

The README still contains an earlier historical tally due to the previously documented blocked edit. Counts here and in the source ledger reflect the later published state. No alternative write path was used for that blocked change.

## Blog-writing source checkpoint (PR #12)

The complete original `info_for_ai/blog_writing/` instruction source is included as eight source files, including the canonical original index. Four files were copied byte-for-byte: `indice_blog_writing.csv`, `03_revision.md`, `04_flujo_iterativo_de_generacion.md`, and `plantilla_entrada.md`. Four have only six individually documented original-owner privacy substitutions: two in `00_core.md`, one in `01_arquitectura_del_razonamiento.md`, one in `02_voz_pedagogia_y_ritmo.md`, and two in `publication_materialization.md`.

For every adapted file, applying exactly the specified substitutions to the current original DIK text reproduces the published text in full; no additional rules, phases, examples or procedures were changed. See `docs/PRIVACY_ADAPTATIONS.md` for original/published Git blob SHAs and line positions.

The source ledger after publication has **108 unique source entries: 97 verbatim and 11 privacy-adapted**. The domain index's seven file entries resolve to all seven modules in this source batch. The original user-specific article-inventory CSV is **not** redistributed, so the renamed neutral article-inventory path remains an unfulfilled runtime dependency until a separate privacy-safe data layer is configured.

This publication inherits the previously documented README editing limitation; `manifests/source_parity.csv` and this continuity record contain the current source counts. Source fidelity benefits from DIK's prior validation, but has not independently proven the new repository's end-to-end command dispatch, file-path resolution, configuration or export behavior.

## Bilingual interactions source checkpoint (PR #13)

All 16 original `info_for_ai/interactions/` instruction-source files, including the original index and both complete `es/` and `en/` language branches, are included in this batch. Six files are identical to their current DIK originals by Git blob SHA. Ten files have only **17 precise privacy substitutions** replacing hard-coded original-owner/gender references with neutral current-user wording. No workflow procedure, activation condition, ordering, authorization, or language routing was rewritten. Every adapted file matched its actual original DIK source after only the documented substitutions, with no extra changes. Details and hashes are recorded individually in `docs/PRIVACY_ADAPTATIONS.md`.

All 15 rows in the original interaction-domain index resolve to the published files; 16 files exist including the index. The domain core and language selection contracts remain unchanged.

The source manifest after publication contains **124 unique entries: 103 verbatim and 21 privacy-adapted**. This source batch does not include personal email accounts, credentials, recipient data, signatures or private records. The global Knotbase command runtime and other incomplete dependencies are still absent. An already-validated DIK procedure increases confidence in behavioral fidelity if its exact source is preserved, but this alone does not certify execution inside the new repository.

The README still contains an earlier historical tally due to the previously recorded blocked edit. Use the current ledger and this continuity document for up-to-date counts; do not bypass any security control.

**Branch-history privacy correction:** the initial working-branch commit for the shared interactions core contained one original-owner given-name reference. The final PR-diff review detected this; a subsequent commit replaced exactly that reference with neutral current-user wording, and the source parity ledger and adaptation documentation were corrected. The final branch-head file and intended squash-merge snapshot contain no such hard-coded name. The earlier commit was already publicly accessible and may remain retrievable through GitHub history even if it is excluded from `main` by squash merge. This is disclosed rather than represented as erased; no history rewrite or security-control bypass was attempted.

## Owner-authorized blog style exclusion checkpoint (PR #14)

The original owner expressly directed that the public `blog_writing` domain should **not carry over the original owner's editorial voice**. This permits a bounded behavioral difference beyond privacy-only replacements. Ten verified exact-span edits across `00_core.md`, `02_voz_pedagogia_y_ritmo.md`, `03_revision.md`, and `publication_materialization.md` remove voice imitation, personal rhetorical/typographic norms, forced Spain-specific language preferences and the required personal LinkedIn sign-off. Published previous/current Git blob hashes and the changes are documented in `docs/EDITORIAL_EXCLUSIONS.md`. The original DIK files remain unchanged.

The seven-phase blog creation state machine (`04_flujo_iterativo_de_generacion.md`), indexed routing, evidence requirements, argument-design algorithm, phase gates and publishing format protocol have not been rewritten. The original blog domain index still resolves its seven listed modules.

The manifest now records **124 unique sources: 102 verbatim, 18 privacy-only, 3 privacy-and-editorial adapted, and 1 editorial-only adapted**. Source blob SHA fields continue to identify the immutable DIK originals, not public targets. Previously documented privacy-only published hashes for the affected files are superseded by the new published hashes in `docs/EDITORIAL_EXCLUSIONS.md`.

This remains a source-level change, not proof of execution in the future Knotbase command runtime; the earlier README security-control issue and unresolved generic article-inventory dependency remain outstanding.

## Template-free professional documents checkpoint (CV source batch)

The five public `info_for_ai/professional_documents/` sources were selected from the currently verified DIK source hashes and adapted with the user's explicit authorization to **create standard CVs without the mandatory personal HTML template**. Their changes and both source/target Git blob hashes are documented in `docs/AUTHORIZED_CV_DEVIATIONS.md`; the private DIK source repository remains unchanged.

The public package preserves two-stage strategy and explicit OK approval, evidence and relevance prioritization, strategic-versus-local CV adjustments, factual/publication verification, default PDF output, optional editable DOCX, final visual inspection and native-text ATS ordering checks. It removes the owner's private profile references and specific contact defaults, mandatory brand/icon/layout assets, and the Europass branch. The public domain index resolves to four published files (core, creation, adjustment and rendering); no private profile data, Europass assets or fixed CV template were included.

The source manifest now has **129 unique canonical-source records: 102 verbatim, 18 privacy-only, 3 privacy-and-editorial, 1 editorial-only and 5 workflow-adapted**. All five new rows have `authorized-workflow-adapted` status; their SHA fields are the original DIK blob SHAs.

A template-free CV feasibility test using fictional applicant information generated HTML, PDF and DOCX and checked native PDF text extraction and rendered output. This does not validate the complete two-phase workflow within Knotbase. The source package still lacks its global runtime, command registry/lookup, portable evidence-source configuration and functional end-to-end integration tests. Earlier sections document historical checkpoints and their counts; the 129-row ledger is authoritative for the current batch.

The README has been refreshed to correct obsolete source totals and GitHub-domain claims, while distinguishing public source publication from a functional release.

## Public scoped router checkpoint (proposed PR #16)

A public, restricted root `AGENTS.md` and command-dispatch files have been prepared on a separate working branch for `#HELP`, `#BLOG`, `#CV` and `#CVEDIT`. The registry reproduces those **four exact DIK command rows**, but the public registry is intentionally a subset, and its lookup uses new public line numbers. The scope and exact source/target blob hashes are recorded in `docs/PUBLIC_ROUTER_SCOPE.md`.

The domain index exposes the template-free `professional_documents` package, the author-neutral `blog_writing` package and already-published `research` support. No original personal-profile domain, maintenance commands or unpublished workflows are enabled. The cross-domain iterative-continuation contract is **verbatim** from DIK and retains its canonical blob hash.

The manifest now contains **134 unique source records**: 103 verbatim, 18 privacy-adapted, 3 privacy-and-editorial-adapted, 1 editorial-adapted, 5 workflow-adapted, 3 public-routing-adapted and 1 public-subset-adapted. The private DIK remains unchanged. The README reflects the restricted pilot and these current counts; earlier historical counts elsewhere in this continuity document refer to older migration checkpoints.

Structural verification of paths, SHA parity, registry lookup, authorization gates and privacy is required before integration. A merge would publish the routing **instructions**, but it would not demonstrate that a ChatGPT consumer activates them automatically or that an entire seven-phase blog workflow or CV generation completes end-to-end. The private blog article inventory and any user-provided evidence remain separate runtime concerns.

## Public HTML domain index checkpoint (proposed PR #18)

The public `htmls` domain now has its own resolvable `indice_htmls.csv`, adapted from the original DIK index without changing the eleven published general HTML modules. The original private, recipient-specific interactive-letter workflow was intentionally excluded: its unpublished personal template and media are neither copied nor replaced with invented public equivalents.

Source trace: canonical DIK index Git blob `05189871f4a37f1d8c7d8079996e7ddeec44eea4`; adapted public index Git blob `abdb61041c9d57b843f676ae2485b60c8387c3b0`. The `privacy-adapted` difference and omission are explained in `docs/HTML_PUBLIC_SCOPE.md`. The manifest now has **135 unique source records**, of which **103 are verbatim and 19 privacy-adapted**. The original DIK repository is unchanged.

This checkpoint completes the general HTML **source index**, not top-level activation of `#HTML`, any excluded personal workflow, or all original DIK commands. The limited root router and four-command registry remain unchanged. Structural GitHub Actions checks apply to the packaged source index; independent end-to-end consumer tests are deferred until after the remaining public routing work.

## Public research, HTML and prompting command extension (PR #19)

The public command registry was extended from four to **fourteen** commands. Exact canonical DIK rows were selected for eight research workflows (`#DEEP`, `#LIT`, `#SOTA`, `#READ`, `#PAPER`, `#ARG`, `#PROOF`, `#OPP`), general-purpose `#HTML`, and `#PROMPT`, alongside the original four commands. The lookup was updated to exact public line numbers 2–15.

The public index now includes `htmls` and `prompting` in addition to `professional_documents`, `blog_writing`, and `research`. All source modules were already published. The public root router is adapted for multi-module research commands, explicit Codex-vs-Chat prompt selection, and the existing authorization and output gates; no personal-profile or private letter workflow is reintroduced.

There are still **135 provenance records**. This phase updates four previously adapted routing files, tests and documentation but adds no new source-file entry. Its current source and public blob hashes are documented in `docs/PUBLIC_ROUTER_SCOPE.md`. DIK remains unmodified. The PR's source/structural CI and subsequent independent ChatGPT functional routing verification are distinct; the latter remains deferred until the full public command migration is finished.

## Runtime assets for PAPER and HTML editor (PR #19 review correction)

The pre-integration review found a missing mandatory `#PAPER` HTML study template and an unavailable presentation-editor resource referenced by the published generic `#HTML` modules. These were missing *packaging dependencies*, not structural-test failures. Both original, generic, self-contained DIK HTML assets have now been copied **verbatim** to `assets_for_ai/paper_study/paper_study_template.html` and `assets_for_ai/htmls/presentation_editor_base.html`. Their minimal source-derived asset index and lookup expose precisely those two public IDs, without private portraits, unrelated media or personal templates.

Source parity now records **139 source entries**: 105 verbatim, 21 privacy-adapted, 3 privacy-and-editorial, 1 authorized-editorial, 5 authorized-workflow, 3 public-routing and 1 public-subset. Four records were added beyond the prior 135: the two verbatim HTML assets and two privacy-scoped indices. The older 135 entry count above is a historical state of this PR before its dependency correction, not the final state. See `docs/PUBLIC_ASSETS_SCOPE.md` for original and public Git blob hashes, intended use and limitations.

The structural unittest now normalizes Windows CRLF checkout text to canonical LF for Git blob verification, without modifying the original `info_for_ai/iterative_continuation.md` file or its expected SHA. No independent consumer routing, paper HTML assembly or presentation-editor interaction has been claimed; the owner requested those manual integration checks only after the public migration is complete.

## Education command subset (PR #20)

After verifying integration of PR #19 in `main` at `85f6132da6d5058078e1b69831777570e305da7a`, the public command subset was extended from fourteen to **twenty** with six exact DIK education records: `#EXPL`, `#NOTES`, `#VIDEO`, `#CLASS`, `#TFG`, and `#TFM`. The public `education` domain row, its canonical core and index, and all six command destinations resolve to previously published source-identical education modules.

The education workflows require a topic and accept context only as declared by their original argument grammar; content or format generation is bounded by the selected module and no external publication is authorized. Learner prerequisites are determined from supplied context, not from any private original-owner profile. Readiness checks include registry/lookup integrity and the already-published education domain's module references.

No new source files are included in this command-expansion batch, so the manifest continues to record **139 unique source entries**. The branch updates only scoped public routing, static tests, README and documentation. No edits to canonical DIK or private assets are made. These checks do not replace independent ChatGPT consumer acceptance tests, which remain deferred to the final migration phase.

## Professional-interaction commands (PR #21)

A bounded command-only batch extends the scoped public registry from twenty to **twenty-five** commands with five exact canonical DIK rows: `#MAIL`, `#LINKEDIN`, `#CONTACT`, `#DELIVER`, and `#REC`. Their read-only, draft-only authorization is preserved. The canonical `interactions` domain-index row is exposed through the public router, backed by all previously published bilingual interaction source modules. The lookup assigns lines 22–26; no private user profile, contact data or recipient-specific personal template is added.

Structural checks cover canonical row identity, lookup correspondence, published route dependencies, both language branches and the unchanged provenance inventory. `manifests/source_parity.csv` remains at **139 records**, because no source is newly published. No email, message or letter is actually sent or signed. Independent functional routing acceptance is still deliberately postponed until migration completion. DIK remains untouched.

## Code identity/assessment and scientific peer-review command subset (PR #22)

The next coherent public command group registers **seven unchanged DIK semantic command rows**: `#IDENT`, `#ASSESS`, `#REV`, `#COM`, `#DIFF`, `#RESP` and `#RESUB`, increasing the scoped public router from 25 to **32** commands. Lookup lines 27–33 correspond to these canonical rows. The exact canonical `code` and `papers` domain-index rows are enabled, without copying new source modules or exposing private evidence. The papers domain intentionally has no separate core; the already published parent peer-review module selects only stage-relevant submodules. The `papers; code` multi-domain set for `#REV` and `#RESUB` remains unchanged.

All seven original read-only or artifact-write effects, argument order, authorization and phase conditions are preserved. No source modules are rewritten, and no private author/contact/repository records or manuscripts are added. Only the scoped router, its indices, static checks and current-state documentation change. The provenance manifest remains **139**. Structural checks and final-HEAD CI are required before merging; independent ChatGPT consumer acceptance continues to be deferred until the complete migration is ready.

## Local repository workflow subset (PR #23)

Five source-identical DIK commands `#INIT`, `#REPRO`, `#REFAC`, `#DOC`, and `#READY` are added to the public registry as lookup lines 34–38, raising the scoped catalog from 32 to **37** commands. The original `local-write` effect, argument syntax, module mapping and original authorization fields are unchanged. Existing public `code` source modules are reused without any new publication, so the provenance ledger stays at **139** source entries.

Remote publication remains outside the scope of all five original commands. No user-specific identity information, private repository inventory, or private DIK edits are included. This checkpoint requires structural validation and passing final-HEAD GitHub CI before integration; independent functional consumer routing tests remain deliberately postponed until the migration has finished.

## Integrated command batches #24 and #25

PR #24 added nine exact DIK audit/journal rows, taking the public subset to 46 commands. Squash commit `905cebd7695885abcc106ef843d7189e43ad08a8`; post-merge GitHub Actions success confirmed. PR #25 added five exact repository-scoped GitHub rows (`#PR`, `#ISSUE`, `#SYNC`, `#RELEASE`, `#BITACORA`), raising the count to 51. It was squash-merged manually after verified head CI, producing `a2166be668e2eec3005bc87e1924285aa6fbd884`; post-merge GitHub Actions run `39313473940` completed successfully. The source manifest remains at 139 entries throughout. No DIK private source files were modified.

## Scoped SHIP and public portability exclusions (PR #26)

The next command-only batch adds `#SHIP` as the exact DIK row at lookup line 53. This raises the scoped public total to 52 of the original 65 and preserves code-first technical-readiness and GitHub publication gates. The 13 remaining original commands depend on original-owner private profile/maintenance records, a repository inventory unavailable publicly for broad operational workflows, or recipient-specific private media. These are not activated or silently reimplemented with weaker semantics. No additional source record is published and the manifest stays at 139.

Final validation still requires independent end-to-end consumer tests after the public subset is complete. Passing structural tests and GitHub CI verify indexed packaging but not actual ChatGPT runtime activation or authorization behavior.
