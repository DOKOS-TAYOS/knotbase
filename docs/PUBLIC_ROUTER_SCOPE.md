# Public pilot router: scope, parity, and acceptance limits

This note records the **scoped public routing adaptation** enabled by the Knotbase root `AGENTS.md`. The private source DIK is unchanged. The public router is a selected-subset instructional contract, not a complete or verbatim copy of the DIK global contract and not a standalone command-executing application.

## Canonical source trace

| Public path | Canonical DIK Git blob SHA | Public Git blob SHA | Manifest status |
|---|---|---|---|
| `AGENTS.md` | `611a06672cf2fb99889268741c3f3eecb4e53696` | `aa48657947851b8041f00cfdb755f330e03578cb` | `public-routing-adapted` |
| `info_for_ai/indice_dominios.csv` | `c5a3b7cb29e83719dd8303e1f4f93dde04e7692f` | `2b847b1745428ac47844389638ca38dbc6af15ff` | `public-routing-adapted` |
| `info_for_ai/comandos.csv` | `8c57e847df45dd80d92a74bbc0efd6129d4e32e0` | `b21eec9899eee84c3461f2a919bd1b6dd65eb4dd` | `public-subset-adapted` |
| `info_for_ai/comandos_lookup.csv` | `890701beb36f8a4ed80437341f16a080f1cd26aa` | `22d6343cf926a8b00d1425267a82cddb099230ec` | `public-routing-adapted` |
| `info_for_ai/iterative_continuation.md` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `89f7ff26efd2ad8db17b64e1a12c43e3274e819b` | `verbatim` |

The public registry contains exactly the current DIK semantic rows for `#HELP`, `#BLOG`, `#CV` and `#CVEDIT`, in that public order. Their original full-blob SHA remains in the manifest, while `comandos_lookup.csv` correctly targets public registry lines 2 through 5. No other DIK command is registered or implicitly authorized.

The pilot domain index contains `professional_documents`, `blog_writing`, and `research`. The first two descriptions are neutralized for public use; the research domain row is copied from the source index and maps to its already published unchanged research core and modules. Index paths are relative to `info_for_ai/` exactly once.

## Behavioral boundaries

- `#CV` invokes an evidence-led first phase and requires explicit approval before composing the final CV. The standard public CV generates HTML, PDF and optional editable DOCX without private personal templates.
- `#CVEDIT` distinguishes local adjustments from changes requiring a new target strategy and explicit approval.
- `#BLOG` uses the original seven-phase editorial workflow and the **verbatim** shared iterative continuation rules for an isolated `OK`. The public edition does not enforce the original author's personal voice.
- `#HELP` exposes only the four installed commands.
- Research modules may be selected to support evidence gathering and technical verification, but this pilot does not register independent research compact commands.
- Do not load unpublished personal records, fixed CV layouts, private article inventories or unlicensed assets. Missing evidence or a missing publication dependency must be reported, never invented.
- User-facing changes to professional facts, publication and remote actions require the same authorization gates as the source modules.
- The adapted `AGENTS.md` deliberately omits DIK's personal-knowledge, private maintenance and broad uninstalled command routing. This is an authorized **public pilot**, not a claim of full semantic parity.

## Structural verification and runtime acceptance

Before merging, verify that the four command rows are exact original registry rows, public lookup line numbers match, every routed core/index/module path exists in the target repository, `iterative_continuation.md` has the immutable DIK blob SHA, the manifest has 134 unique source rows and exactly five new provenance entries, and the public router files do not contain private user-specific facts.

**Structural validity is not the same as runtime validation.** The executable consumer must load the root `AGENTS.md`, honor the lookup/registry and phase gates, obtain real supporting evidence without private DIK access, and create/inspect genuine artifacts before a functional `#CV` or `#BLOG` claim can be made. A text-only fake run, the DIK source's prior validation or a synthetic CV-conversion smoke test is insufficient evidence of end-to-end routing behavior.

The source manifest is an inventory of **published source records**, not an inventory of every added documentation or test file. Later PRs must keep this distinction and maintain current status counts.
