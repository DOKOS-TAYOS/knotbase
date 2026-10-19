# Knotbase public instruction router (scoped pilot)

This is a **public, scoped adaptation** of the DIK global routing contract. It is not a literal DIK `AGENTS.md` copy and is **not** a claim of full source/command parity. Only the domains and compact commands explicitly indexed in this repository's public registries are activated. The canonical private DIK remains unchanged. Document the differences under `docs/PUBLIC_ROUTER_SCOPE.md`.

## Routing invariants

1. Respect the user's explicit instructions, repository instructions, safety limits, and active workflow's phase gates. Do not invent professional evidence or user-specific records.
2. Interpret indexed routes relative to **`info_for_ai/` exactly once**. Never guess equivalent paths under the repository root or load all instruction files in advance.
3. If the first token of a trimmed message is `#SHORT`, `#MEDIUM`, or `#LONG` (case-insensitive), consume exactly one modifier plus its following whitespace and apply it only to this answer's presentation length. Require a nonempty remainder. Two consecutive modifiers are conflicting; report that conflict instead of executing.
4. After that preprocessing, inspect only whether the new first token has the form `#NAME`. Treat it as opaque until resolved from `info_for_ai/comandos_lookup.csv` and the exact canonical row of `info_for_ai/comandos.csv`. Match case-insensitively. The lookup locates the row; the command registry owns meaning, required arguments, mode, scope and maximum authorization. **If unregistered, stop and explain that the command is unavailable in this public distribution. Do not guess a meaning or fall back to semantic routing.**
5. Without a leading compact command, read `info_for_ai/indice_dominios.csv` and select only the public domain or domains relevant to the request. For each, load the declared core, then that domain's index, then only the task-relevant indexed module.
6. For `mode=route` commands, load `info_for_ai/indice_dominios.csv`, then the owning domain core and index before its specialized module(s). A semicolon-delimited `modules` field names all required modules in order. When `modules` is empty, select only the specialized module required by the domain index and the command's parsed arguments; `#PROMPT` selects exactly one Codex or Chat target module. For `mode=help`, display registered commands without loading a domain. Never route to unpublished paths.
7. Parse registry arguments in declared order: trim only surrounding whitespace and split on `;` only enough times for preceding argument fields. A final `...` field consumes the remainder, including semicolons/newlines. Respect optional `?` fields. For `#PROMPT`, require `Codex` or `Chat`, a semicolon and a nonempty request; for any invalid target or missing required argument, show the canonical usage.
8. Do not run repository-wide search, recursive inventory or broad private-data discovery to compensate for missing public indices. If an expected public index or dependency is missing, report the exact blocker. Public files are not evidence of personal achievements or contact details.
9. In continuing a prior workflow, preserve the same objective, artifact, user constraints and approved evidence. An isolated `OK` only advances when the **active selected module** expressly permits it. No earlier or unrelated task is revived merely by `OK`.

## Enabled pilot commands and behavior

The registry currently supports fourteen public commands: `#HELP`, `#PROMPT`, `#DEEP`, `#LIT`, `#SOTA`, `#READ`, `#PAPER`, `#ARG`, `#PROOF`, `#OPP`, `#BLOG`, `#HTML`, `#CV` and `#CVEDIT`. Its exact rows are authoritative, not this summary.

- **`#CV`**: route to `professional_documents/01_crear_cv.md` after its core and index. The first turn executes *strategy only* and asks for explicit approval. Only after an unambiguous `OK` on that same candidature may generation proceed under `standard_cv_rendering.md`. Only user-provided/authorized evidence is available; no personal profile, fixed template, phone, nationality, company email or Europass is bundled.
- **`#CVEDIT`**: route to `professional_documents/02_reajustar_cv.md` after its core and index. Local changes may run directly; a material new target requires the phase-1 approval gate. Never invent a prior CV when none was supplied or established in the current conversation.
- **`#BLOG`**: route to `blog_writing/04_flujo_iterativo_de_generacion.md` after its core and index. That module defines seven editorial phases and when `research` or other supporting modules are needed. Load `info_for_ai/iterative_continuation.md` when the selected blog workflow requires it. The first invocation performs phase 1 only; a valid isolated `OK` advances at most one pending phase. The public version does not impose the private DIK author's personal writing voice.
- **`#PROMPT`**: load the prompting core and index, then exactly one target-specific module according to `Codex; request` or `Chat; request`. Codex-targeted prompts, including cross-domain handoffs, must apply the indexed Codex contract, including single-agent operation; this command never authorizes external mutation.
- **Research commands** (`#DEEP`, `#LIT`, `#SOTA`, `#READ`, `#PAPER`, `#ARG`, `#PROOF`, `#OPP`): load the research core and index, then the declared module(s). `#SOTA` requires both modules; `#PAPER` preserves the original staged `OK` approvals. Do not mutate permanent knowledge unless separately authorized.
- **`#HTML`**: load the general HTML core and index, the generation module and mandatory verification module, plus only other modules required by the requested artifact. Do not enable excluded personal workflows or external publication.
- **`#HELP`**: show only commands registered in the public lookup, with no claims about omitted DIK commands.

## Evidence, artifacts and privacy

Use the material attached or supplied for the current task and legitimately accessible public resources when necessary. Missing evidence is a limitation, not permission to infer identity, credentials, employment, private user records or article metadata. Distinguish verified claims from hypotheses and never publish a file, apply to a vacancy or post an article unless separately authorized.

**Invariant:** The user's explicit phase approvals are mandatory. An `OK` for a CV or for `#BLOG` is not approval of unrelated steps or external publication. Reuse `info_for_ai/iterative_continuation.md` for blog's precise continuation policy.

**Invariant:** A publication-ready CV requires actual accessible PDF/DOCX tools for the requested output, final visual inspection, native PDF text/ATS checks where applicable, and verified contacts/links. A mere collection of instructions does not prove successful artifact generation.

**Invariant:** A publication-ready blog article requires the supporting research, sourcing, link audit and publication-materialization checks defined by its source module. The original owner's private article inventory and other unpublished dependencies are not distributed. Do not represent missing dependencies as installed.

## Language and output

Default to Spanish for user-facing responses unless the audience, task or user requires otherwise. Source code, public technical documents, PRs and commit messages should normally be in English. Use relevant native visuals only when they improve the task and have adequate evidence. Explain operational limitations precisely; never report a PR, export, check or task as completed without verification.

## Scope boundary

This pilot intentionally **does not register** `#DEP`, `#SEC`, `#SHIP`, personal-data synchronization, maintenance commands, excluded private-recipient workflows or other unlisted DIK commands. Their original contracts, scopes and permissions must not be inferred from their names. Additional published domains are not yet exposed by this limited top-level router.

The public source files are instructions for a capable ChatGPT client; Knotbase is **not** a standalone executable or independently validated full DIK runtime. Activation depends on loading this repository's `AGENTS.md` in the actual consumer environment. Test command parsing, index resolution, phase gates, privacy and artifact generation in that environment before claiming functional parity.
