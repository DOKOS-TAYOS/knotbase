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

The code index's 19 file entries all correspond to files present in the publication batch. Its source domain is complete, but the global routing/command system and original personal-data dependencies are not yet installed, so **functional parity is not established**.

The source-parity ledger now has **77 records: 74 verbatim and 3 privacy-adapted**. These counts describe migrated source files, not verified runtime behavior. GitHub core and outstanding domain modules remain priorities.
