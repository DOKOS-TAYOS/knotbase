# Shared rules for local code work

## Activation

Read this file before using any instruction in `code/`. Select only the specialized module whose activation condition matches the task.

This domain owns local repository analysis, implementation, testing, refactoring, documentation, and technical preparation for integration. Remote GitHub state and actions belong to `../github/`.

When the selected workflow is the bug audit, dead-code audit, performance audit, or refactoring audit, also load `shared_intensive_audit.md` before performing the initial inventory.

**Invariant:** For a direct `#BUG`, `#DEAD`, `#OPT`, or `#REFACT` workflow, do not load `shared_codex_remediation_loop.md` during the inventory-only first turn. Load it only after that inventory when an isolated `ok` starts the ChatGPT-first remediation loop, and reuse it when reviewing returned Codex execution output or resuming a human checkpoint. Treat that isolated `ok` as a workflow control token, not a conversational acknowledgment: in the same turn, load the shared module and begin executing its State 1 remediation behavior. Do not answer with a bare acknowledgment, confirmation, or request for another instruction. That shared module owns the direct-command post-inventory state machine; the specialized audit module continues to own the technical correction and verification contract. Do not activate the shared remediation loop when the same audit module is reused by `#FIX`, `#CYCLE`, `#REFAC`, or another delegating workflow unless that workflow explicitly selects it.

When generated or modified code is scientific or research code whose primary purpose is experimental execution, inspection, or reproduction rather than production/application software, also load `experimental_scientific_code.md` before designing or changing that code.

## Codex execution model

**Invariant:** When any `code/` workflow is executed by or delegated to Codex, Codex must operate in single-agent mode. Do not spawn, invoke, or delegate work to subagents, parallel agents, background agents, agent pools, or equivalent delegated agent workers, and do not require the user to enable subagents.

**Invariant:** The sole exception is when `06_cyclic_agent_workflow.md` is actively selected through `#CYCLE`. Only that cyclic workflow may use subagents, and only according to the roles and coordination rules defined there. Loading a bug, performance, dead-code, testing, refactoring, reproduction, correction, or other code workflow without `#CYCLE` never authorizes subagents.

## Precedence and repository context

Apply instructions in this order:

1. The user's explicit request.
2. Instructions in the target repository, including `AGENTS.md`, `CONTRIBUTING.md`, CI configuration, and project documentation.
3. The selected `code/` instruction.
4. General operating preferences.

Before editing, identify the repository, current branch, Git status, relevant local rules, project tooling, and supported versions. Preserve unrelated work; do not revert, delete, or reformat changes outside the task.

When the task concerns one of the user's GitHub repositories but the exact repository or repository path has not been supplied and must be located or selected, first resolve it from `../info_user/repositorios_github.csv`. If repository selection also requires remote GitHub inspection, load `../github/00_core.md` and follow its repository-inventory routing. Do not substitute an unscoped GitHub-wide repository search for the maintained inventory while it is available.

## Evidence and traceability

- Distinguish verified facts, hypotheses, risks, and proposals.
- Cite the files, tests, commands, and sources that support material conclusions.
- Do not invent requirements, author data, versions, URLs, DOIs, test results, or licenses.
- Reproduce or otherwise demonstrate a reported problem before fixing it when feasible.
- Review the complete task diff and provide fresh verification evidence before declaring completion.

## Technical quality

- Follow the repository's established style, tools, and versions.
- Keep changes compatible with Windows and Linux unless the repository declares a different target.
- Include types in every new or modified function definition when the language supports them or the project expects them.
- Make small, reviewable changes tied to a concrete finding.
- Do not intentionally change public interfaces, observable results, formats, data contracts, or performance without explicit authorization.
- Do not add a dependency without justifying its need, maintenance, compatibility, and license.
- Run the checks supplied by the repository. Report precisely which checks could not run and why.
- In Python projects configured with Ruff, finish with `ruff check . --fix` and `ruff format .`, then rerun any tests affected by those changes.

## Creator information

For facts about the current user, consult `../info_user/indice_info_user.csv` first and open only the records relevant to the task. Reuse only public data that serves the repository's purpose. Do not disclose `private` or `restricted` information or fill unknown fields by assumption.
