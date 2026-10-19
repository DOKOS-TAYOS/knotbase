# Public pilot router: scope, parity, and acceptance limits

This note records the **scoped public routing adaptation** enabled by the Knotbase root `AGENTS.md`. The private source DIK is unchanged. The public router is a selected-subset instructional contract, not a complete or verbatim copy of the DIK global contract and not a standalone command-executing application.

## Canonical source trace

| Public path | Canonical DIK Git blob SHA | Public Git blob SHA | Manifest status |
|---|---|---|---|
| `AGENTS.md` | `611a06672cf2fb99889268741c3f3eecb4e53696` | `d8d5e715255c1bc9ebe7a080ddd222ac2b71c418` | `public-routing-adapted` |
| `info_for_ai/indice_dominios.csv` | `c5a3b7cb29e83719dd8303e1f4f93dde04e7692f` | `77b28a94b0fe5f2a56681e35642531ff816207a2` | `public-routing-adapted` |
| `info_for_ai/comandos.csv` | `8c57e847df45dd80d92a74bbc0efd6129d4e32e0` | `c3d43dbc6b9bb03b7879698142efcd89b102c03e` | `public-subset-adapted` |
| `info_for_ai/comandos_lookup.csv` | `890701beb36f8a4ed80437341f16a080f1cd26aa` | `12ba5ab46ce5fff60c4fb7b80e2ae96dd3825378` | `public-routing-adapted` |
| `info_for_ai/iterative_continuation.md` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `verbatim` |

The public registry contains twenty-five exact DIK semantic command rows, and `comandos_lookup.csv` maps them to lines 2 through 26. The DIK source blob remains recorded in the manifest. Unregistered commands are unavailable and cannot be inferred or activated.

The public domain index contains `professional_documents`, `blog_writing`, `research`, `htmls`, `prompting`, `education`, and `interactions`. The first two descriptions are neutralized for public use; the research domain row is copied from the source index and maps to its already published unchanged research core and modules. Index paths are relative to `info_for_ai/` exactly once.

## Behavioral boundaries

- `#CV` invokes an evidence-led first phase and requires explicit approval before composing the final CV. The standard public CV generates HTML, PDF and optional editable DOCX without private personal templates.
- `#CVEDIT` distinguishes local adjustments from changes requiring a new target strategy and explicit approval.
- `#BLOG` uses the original seven-phase editorial workflow and the **verbatim** shared iterative continuation rules for an isolated `OK`. The public edition does not enforce the original author's personal voice.
- `#HELP` exposes only the twenty-five installed commands. Eight research commands, general `#HTML` and `#PROMPT` now have indexed public routes and retain their canonical argument and authorization contracts.
- Research modules support evidence gathering and technical verification under eight explicitly registered research commands. `#SOTA` loads both listed modules; `#PAPER` retains its staged approval contract.
- Do not load unpublished personal records, fixed CV layouts, private article inventories or unlicensed assets. Missing evidence or a missing publication dependency must be reported, never invented.
- User-facing changes to professional facts, publication and remote actions require the same authorization gates as the source modules.
- The adapted `AGENTS.md` deliberately omits DIK's personal-knowledge, private maintenance and broad uninstalled command routing. This is an authorized **public pilot**, not a claim of full semantic parity.

## Structural verification and runtime acceptance

Before merging, verify that the twenty-five command rows are exact original DIK registry rows, public lookup line numbers match, every routed core/index/module path exists in the target repository, `iterative_continuation.md` has the immutable DIK blob SHA, the manifest records 139 unique source records, including four new records for two generic HTML runtime assets and their privacy-scoped lookup indices, and the public router files do not contain private user-specific facts.

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
