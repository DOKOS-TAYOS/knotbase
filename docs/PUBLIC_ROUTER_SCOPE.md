# Public pilot router: scope, parity, and acceptance limits

This note records the **scoped public routing adaptation** enabled by the Knotbase root `AGENTS.md`. The private source DIK is unchanged. The public router is a selected-subset instructional contract, not a complete or verbatim copy of the DIK global contract and not a standalone command-executing application.

## Canonical source trace

| Public path | Canonical DIK Git blob SHA | Public Git blob SHA | Manifest status |
|---|---|---|---|
| `AGENTS.md` | `611a06672cf2fb99889268741c3f3eecb4e53696` | `ad0952f40fd9d0a79e9e9810f7978caa3f9f2403` | `public-routing-adapted` |
| `info_for_ai/indice_dominios.csv` | `c5a3b7cb29e83719dd8303e1f4f93dde04e7692f` | `d27fd759b4085fba5ab0cc5975a88dbc5f8b3090` | `public-routing-adapted` |
| `info_for_ai/comandos.csv` | `8c57e847df45dd80d92a74bbc0efd6129d4e32e0` | `c230a2cdb6da6638fa9b68b473130f2ce8f7e261` | `public-subset-adapted` |
| `info_for_ai/comandos_lookup.csv` | `890701beb36f8a4ed80437341f16a080f1cd26aa` | `85d61ef2646dc0491062ba4083ec14294d668b94` | `public-routing-adapted` |
| `info_for_ai/iterative_continuation.md` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `verbatim` |

The public registry contains 64 commands, including 52 source-identical public rows and twelve owner-scoped adaptations; `comandos_lookup.csv` maps them to lines 2 through 65. The DIK source blob remains recorded in the manifest. Unregistered commands are unavailable and cannot be inferred or activated.

The public domain index contains `professional_documents`, `blog_writing`, `research`, `htmls`, `prompting`, `education`, `interactions`, `code`, `papers`, and `github`. The first two descriptions are neutralized for public use; the research domain row is copied from the source index and maps to its already published unchanged research core and modules. Index paths are relative to `info_for_ai/` exactly once.

## Behavioral boundaries

- `#CV` invokes an evidence-led first phase and requires explicit approval before composing the final CV. The standard public CV generates HTML, PDF and optional editable DOCX without private personal templates.
- `#CVEDIT` distinguishes local adjustments from changes requiring a new target strategy and explicit approval.
- `#BLOG` uses the original seven-phase editorial workflow and the **verbatim** shared iterative continuation rules for an isolated `OK`. The public edition does not enforce the original author's personal voice.
- `#HELP` exposes the sixty-four registered commands. Eight research commands, general `#HTML` and `#PROMPT` now have indexed public routes and retain their canonical argument and authorization contracts.
- Research modules support evidence gathering and technical verification under eight explicitly registered research commands. `#SOTA` loads both listed modules; `#PAPER` retains its staged approval contract.
- Do not load unpublished personal records, fixed CV layouts, private article inventories or unlicensed assets. Missing evidence or a missing publication dependency must be reported, never invented.
- User-facing changes to professional facts, publication and remote actions require the same authorization gates as the source modules.
- The adapted `AGENTS.md` deliberately omits DIK's personal-knowledge, private maintenance and broad uninstalled command routing. This is an authorized **public pilot**, not a claim of full semantic parity.

## Structural verification and runtime acceptance

Before merging, verify that the fifty-two command rows are exact original DIK registry rows, public lookup line numbers match, every routed core/index/module path exists in the target repository, `iterative_continuation.md` has the immutable DIK blob SHA, the manifest records 139 unique source records, including four new records for two generic HTML runtime assets and their privacy-scoped lookup indices, and the public router files do not contain private user-specific facts.

**Structural validity is not the same as runtime validation.** The executable consumer must load the root `AGENTS.md`, honor the lookup/registry and phase gates, obtain real supporting evidence without private DIK access, and create/inspect genuine artifacts before a functional `#CV` or `#BLOG` claim can be made. A text-only fake run, the DIK source's prior validation or a synthetic CV-conversion smoke test is insufficient evidence of end-to-end routing behavior.

The source manifest is an inventory of **published source records**, not an inventory of every added documentation or test file. Later PRs must keep this distinction and maintain current status counts.

## Research, HTML and prompt expansion

The extension adds the eight canonical DIK research commands `#DEEP`, `#LIT`, `#SOTA`, `#READ`, `#PAPER`, `#ARG`, `#PROOF`, and `#OPP`; the general-purpose `#HTML`; and `#PROMPT` with explicit `Codex; request` or `Chat; request` target parsing. The original DIK commands' side-effect and authorization fields were not expanded. Prompt routing selects exactly one target-specific module. The public index exposes already published generic HTML and prompting cores/indices. Recipient-specific private HTML workflows remain excluded. Static routing CI is not independent ChatGPT runtime acceptance.

## Public runtime asset dependency closure

The mandatory paper-study HTML runtime asset and optional presentation editor runtime are now published as identical DIK blobs with a privacy-scoped two-row asset registry. Their source and public hashes, IDs, selected-use constraints and runtime-verification limits are described in [`PUBLIC_ASSETS_SCOPE.md`](PUBLIC_ASSETS_SCOPE.md). The general `#HTML` creation route can produce ordinary HTML without a presentation editor; presentation-oriented authoring must use the registered editor runtime when its indexed module activates, unless the user explicitly opts out under that module's conditions. `#PAPER` must have the runtime available for its final assembly phase. The module contracts and phase gates remain unchanged.

## Education command expansion (PR #20)

The six canonical education commands `#EXPL`, `#NOTES`, `#VIDEO`, `#CLASS`, `#TFG` and `#TFM` have been added as **exact original DIK semantic rows**, with lookup positions 12–17. The public `education` domain row is copied from the source domain index and routes to the already published, source-identical education core, index and specialized modules. Topic is required for each invocation; context/student-profile fields are optional as declared. Content must be adapted to evidence-backed learner prerequisites and must not infer original-owner teaching history, personal profile information, or the user's likeness. These changes activate no external publishing action.

This adds **zero source-file records** to the manifest, which remains at 139. The public router/registry/index target blob hashes in the trace table above were verified after remote writes. Structural CI verifies resolution; independent user-facing model behavior remains deferred until the final acceptance phase.

## Bilingual professional-interaction command expansion (PR #21)

Five original DIK semantic rows are registered without modification: `#MAIL`, `#LINKEDIN`, `#CONTACT`, `#DELIVER`, and `#REC`. Their lookup lines are 22–26, and the `interactions` domain row matches the canonical DIK index. The previously migrated shared interaction core, bilingual index and both language branches already contain every required personal/corporate email, LinkedIn, first-contact, project-delivery and recommendation-letter module. `modules` remains empty in these five original records because the active workflow is selected by recipient language and purpose through the published domain index.

All five commands have original `read-only` effect and **draft-only authorization**. They cannot send emails or direct messages, sign recommendations, claim nonexistent delivery, invent third-party evidence, or load private sender/recipient profiles. The appropriate single language branch is loaded by the existing public interaction core; optional style references remain conditional. This integration changes routing, structural tests and documentation only; the source-parity ledger remains **139 records**, and independent consumer-runtime acceptance remains deferred.

## Code assessment and manuscript peer review (PR #22)

Seven canonical DIK semantic rows are newly enabled **verbatim**, with public lookup lines 27–33: `#IDENT`, `#ASSESS`, `#REV`, `#COM`, `#DIFF`, `#RESP`, and `#RESUB`. Original `effect`, ordered arguments, module paths, authorization and phase boundaries are unchanged. The full canonical `code` and `papers` domain rows have been copied without modification, including the intentionally **empty** `papers.core` value. A blank core means no core is declared; the papers index and the parent peer-review workflow must be loaded in their original order. `#REV` and `#RESUB` retain the canonical `papers; code` domain set, with the second domain loaded only as appropriate to the selected workflow.

The already published code assessment sources and papers peer-review parent/stage modules are reused as-is. The publication provides no personal professional profile, original-owner repo inventory, private manuscripts or code. `#IDENT` and `#ASSESS` remain read-only; the paper commands retain read-only or artifact-only effects exactly as recorded. Private-profile-dependent optional facts are unavailable unless the current user provides or authorizes them. No remote manuscript/code changes, journal submission or signing are activated.

No new migrated sources were copied. The manifest remains **139** records, including the same four adapted public router files. This is structural routing activation, not an independently validated consumer-runtime implementation. Manual functional tests remain postponed until after migration completion.

## Local-only repository workflows (PR #23)

Five more public commands are enabled by adding their **exact canonical DIK rows** in lookup positions 34–38: `#INIT`, `#REPRO`, `#REFAC`, `#DOC` and `#READY`. All original source modules already exist in the public `code` domain; no instruction text was rewritten, simplified or generalized for this batch. The commands preserve their original `local-write` effects, ordered argument grammar and module-specific bounded validation requirements.

In particular, `#REPRO` does not authorize a bug fix; `#REFAC` must preserve observable behavior; `#READY` does not authorize remote publication; and `#INIT` must stop for unresolved ownership and cannot fabricate a configured author/contact. None of these commands grants GitHub push, PR or merge authority. Private owner profiles and inventories remain omitted, and a consumer without verified author evidence must report the gap. The manifest remains at **139 source records**, with only public router adaptation, registry, static checks and documentation updated. Independent end-to-end acceptance remains deferred.

## Phase-gated audits and journal workflows (PR #24)

Nine more semantic DIK commands were copied **without changing their original rows**, effects, scope, arguments, or permissions: `#BUG`, `#OPT`, `#DEAD`, `#TEST`, `#FIX`, `#CYCLE`, `#REFACT`, `#JOURNAL`, and `#PAPERFIT` (lookup lines 39–47). The unchanged `github` domain-index row is now public solely as a supporting domain for commands whose canonical workflow requires it; this does not register any omitted GitHub command.

The four intensive code-audit workflows begin with **read-only inventory**. Only a valid isolated direct-continuation `ok` enters the source-defined remediation loop and any deferred GitHub responsibility. `#TEST` uses one approved test-improvement batch per continuation; `#FIX` is limited to independently identified existing findings; `#CYCLE` remains local-only with a ten-batch cap and is the sole code-workflow exception to the normal no-subagent rule. Codex handoffs, if genuinely necessary in a later user task, must follow the published prompting contract. These activations do not relax repository protections or permit unrelated mutations.

`#JOURNAL` preserves its **optional** input, its read-only selection mode and its conditional local adaptation mode. `#PAPERFIT` remains inventory-only on its first invocation, with later proposal and execution phases requiring the original explicit approvals. Journal submission, editor contact, and merging work branches are not enabled by either command.

Every referenced source module was already present; no source instructions were rewritten or additional private documents copied. The manifest remains at **139** unique records. Structural validation is not independent user-facing runtime acceptance, which remains deferred until migration completion.

## Repository-scoped GitHub commands (proposed PR #25)

Five original DIK records are present in the work branch without semantic edits: `#PR`, `#ISSUE`, `#SYNC`, `#RELEASE`, and `#BITACORA` (lookup lines 48–52). Each requires an explicit repository and is bounded by its original authorization. The associated source modules already exist in the public `github` and `code` domains, so no personal inventory, private identity record, or new migrated source is required.

The original `#ISSUE` owner module controls its issue-inspection phase and explicitly defers code implementation, local readiness and remote publication dependencies. The original `#RELEASE` starts with code release preparation and loads release publication only after its local gate. `#PR` requires current-head review and protected integration; `#SYNC` must establish the intended base without guessing; `#BITACORA` requires traceable notes and an authorized destination. No user-specific evidence, remote mutation or completion claim may be fabricated.

**Integration condition:** the public `AGENTS.md` command enumeration and owner-module phase routing must be consistent with this registry. The source modules and registry cannot alone prove that the runtime will honor these gates. The structural checks and final-head CI must be passing before integration; independent consumer-runtime acceptance remains deferred. The provenance manifest remains at **139** records.

## Completion-of-command-subset review (PR #26)

The canonical `#SHIP` row is published unchanged at lookup line 53. The supplied-repository scope, optional branch, remote-write effect, and protections are identical to DIK. Its initial code readiness module hands off to the original GitHub integration module; no publication is permitted before the required readiness and verification gates. All referenced modules were already in the published source manifest.

The canonical DIK registry contains 65 commands. The current portable subset contains **64**, excluding only `#NOAH`. The remaining original workflows rely on unpublished personal records or maintenance infrastructure, private repository-inventory and archived/frozen status checks for broad operational work, or a private recipient-specific letter template. Do not activate them by inventing missing inventory or weakening the canonical contract. This is a portability exclusion, not a claim that the full DIK command set is public.

The manifest remains **139 source records**. No personal inventory, restricted evidence or proprietary media has been newly published. Structural CI verifies command and routing integrity, but independent end-to-end ChatGPT consumer tests for real routing, approval gates, asset assembly, and remote publication remain separate acceptance requirements.

## Read-only onboarding entrypoint (not an installed instance)

The public root `AGENTS.md` now explicitly recognizes **natural-language requests to initialize a user's own Knotbase** and points to `BOOTSTRAP.md`. The public upstream entrypoint is read-only and fail-closed. An unset `config/instance.csv`, header-only `info_user` domain, maintenance contracts and the twelve owner-scoped command rows are published, but a verified private user instance is not installed. No new compact commands have been registered. The existing 52 commands retain their current behavior, and `#NOAH` remains excluded.

A public upstream checkout and a private installed fork have different privacy obligations: the public upstream must not ship personal-data rows or instance assignments, but a configured private fork must be allowed to store validated user evidence. Structural checks protect schema parity and public blank-data packaging without requiring the private fork's evidence tables to remain empty. No consumer-runtime acceptance is inferred.

## Portable owner-scoped registration

The source registry has 65 commands. Knotbase now indexes 64, excluding the private-recipient-specific `#NOAH`. The original 52 public command rows are preserved; twelve owner-dependent rows adapt original private owner and publication targets to explicit instance configuration. No personal records or configured GitHub owners are distributed. A public command registration is not a consumer runtime test or authorization to mutate upstream; empty profile and repository inventory must fail closed. Maintenance checks now use `maintenance_for_ai/validation/validate.py` on the exact configured target tree.
