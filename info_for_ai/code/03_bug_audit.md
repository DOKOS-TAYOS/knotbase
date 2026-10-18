# Bug audit and debugging

## Activation

Use this module to evaluate a repository for defects and define the technical correction contract for later remediation. Apply `shared_intensive_audit.md` for the shared inventory, coverage, saturation, presentation, and bounded-batch mechanics.

For a direct `#BUG` invocation, the initial response is the audit inventory. After that inventory, `shared_codex_remediation_loop.md` owns the direct-command `ok` handoff, ChatGPT-first remediation, minimal Codex handoffs when necessary, remote review, human checkpoints, and completion semantics. The correction requirements in this module remain authoritative whether a correction is executed directly by ChatGPT, delegated narrowly to Codex, or reused by another workflow.

## Bug-specific coverage

Systematically inspect every applicable defect surface below under the shared coverage ledger and saturation contract:

- primary execution paths and core domain logic;
- input parsing, validation, normalization, boundary values, malformed but realistic input, and error propagation;
- state transitions, persistence, serialization, caching, data integrity, migrations, and recovery behavior when present;
- public APIs, internal APIs with important consumers, CLIs, entry points, configuration, environment variables, and feature flags;
- filesystem, network, database, subprocess, device, accelerator, and other external integration boundaries that the supported product actually uses;
- concurrency, asynchronous execution, ordering, cancellation, retries, idempotency, synchronization, and resource lifecycle when applicable;
- numerical correctness, precision, shape or dimensional assumptions, overflow/underflow, randomness, reproducibility, and scientific validity when applicable;
- security-relevant trust boundaries, authentication, authorization, unsafe deserialization, injection surfaces, path handling, secret handling, and externally controllable resources when applicable;
- tests for missing realistic cases, assertions that encode incorrect behavior, fixtures that conceal defects, and test-production mismatches;
- packaging, installation, imports, optional dependencies, supported platforms, runtime versions, build paths, and distribution metadata;
- executable examples and documentation whose commands or documented behavior form part of normal supported use;
- cross-module interactions and consumers adjacent to already discovered findings, especially where one defect suggests a repeated pattern.

Use repository-native tests, targeted tests, static inspection, type/lint output, call-site tracing, configuration comparison, focused searches, minimal reproductions, and representative workflows when they provide materially different evidence. In the shared saturation pass, deliberately look for defect classes not represented in the findings already collected and repeated instances of patterns already proven defective.

## Finding contract and severity

The initial inventory uses the shared presentation contract with severity sections in this exact order: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.

Each finding must use a `BUG-ID` and include, when applicable:

- **Estado:** `open`, `fixed`, `not reproducible`, `accepted`, or `requires decision`.
- **Tipo:** confirmed bug, probable risk, or requires validation.
- **Ubicación:** file, symbol, line, configuration key, or other precise location.
- **Evidencia:** concise reproducible evidence.
- **Impacto:** concrete user, product, data, security, or operational consequence.
- **Condición:** realistic trigger or precondition.
- **Confianza:** confidence level and any material uncertainty.

Classification:

- `CRITICAL`: severe data loss or exposure, unauthorized execution, general outage, or systemic corruption.
- `HIGH`: major failure of a primary function, exploitable security issue, materially incorrect results, or frequent blocking failure without a workaround.
- `MEDIUM`: bounded failure, relevant edge case, notable degradation, or recoverable inconsistency.
- `LOW`: nuisance, minor validation defect, misleading message, or localized issue without significant impact.

## Practical scope and stopping criterion

**Invariant:** Treat as actionable bugs only defects that are plausible under reasonable supported use and whose impact is meaningful enough to justify correction. Prioritize failures that users, maintainers, integrations, normal malformed input, realistic load, supported platforms, or ordinary operational mistakes can reasonably encounter.

Do not inflate the audit with scenarios that require deliberately trying to break the product, contrived or extraordinarily improbable state combinations, unsupported environments, unrealistic resource exhaustion, pathological inputs with no credible route from normal use, or speculative hardening whose implementation cost and complexity outweigh the realistic risk. Security-relevant adversarial behavior remains in scope when the product exposes a plausible attack surface.

Prefer the smallest robust correction over defensive layers, abstractions, validations, or fallback machinery that are not justified by a realistic failure mode. A theoretical possibility alone is not sufficient evidence for a finding.

The audit is complete when no confirmed or sufficiently probable actionable findings remain under this practical scope after the shared coverage and saturation passes. When only excluded, speculative, unsupported, or disproportionate-hardening scenarios remain, report that the practical bug audit has reached its stopping condition.

## First response

Follow the shared initial-inventory contract. Do not propose patches. Never target a finding count or inflate the list with false positives, speculative concerns, or impractical edge cases.

For a direct `#BUG` invocation, do not modify files or remote state after the inventory merely because findings are actionable. Wait for the isolated `ok` defined by `shared_codex_remediation_loop.md`; after that authorization, execute its ChatGPT-first remediation loop and delegate only concrete execution or verification dependencies that meet its Codex handoff criteria.

Do not load the GitHub integration module during the inventory-only first turn. Remote GitHub work starts only after the isolated `ok`, when ChatGPT begins authorized remediation or publication, or when returned Codex state must be reviewed.

## Bug correction execution contract

Apply this section to every correction unit in direct `#BUG` remediation, whether executed by ChatGPT or delegated to Codex, and whenever another workflow explicitly delegates a bounded bug correction to this module.

Fix the highest-priority safely actionable open findings first: `CRITICAL`, then `HIGH`, then `MEDIUM`, then `LOW`. A correction unit may contain one finding or a small tightly related group that can be reviewed and verified coherently. Do not expand a correction unit merely because more findings are available.

When a delegated workflow executes such a correction unit, use the shared bounded-batch presentation from `shared_intensive_audit.md` for the batch just executed, unless the delegating workflow defines a stricter presentation contract. This presentation compatibility does not reintroduce bounded-batch continuation semantics for direct `#BUG`; direct continuation remains owned by `shared_codex_remediation_loop.md`.

For each corrected finding:

1. reproduce the defect or create the smallest reliable test that demonstrates it when feasible;
2. apply the smallest robust change that resolves the realistic failure mode;
3. preserve unrelated behavior and public contracts outside the demonstrated defect;
4. run the affected repository-native checks and inspect for regressions;
5. inspect the final diff for unrelated changes;
6. link the correction to verification evidence before classifying it as resolved.

Track each finding as `open`, `fixed`, `not reproducible`, `accepted`, or `requires decision`. Do not claim a finding is fixed merely because the implementation looks plausible.

When this contract is executed by Codex, the entire authorized correction unit must run in the same Codex agent. Do not spawn or delegate to corrector subagents, parallel agents, background agents, agent pools, or equivalent delegated workers. The only exception is an independently activated `#CYCLE` workflow under its own contract.

## Remote publication and integration for authorized bug corrections

When the enclosing workflow authorizes remote publication, verified bug corrections follow routine remote publication and integration through the repository's normal policy. Load [../github/00_core.md](../github/00_core.md), [../github/indice_github.csv](../github/indice_github.csv), and [../github/01_integration_and_publication.md](../github/01_integration_and_publication.md) only when publication or remote verification actually begins, then publish through the target repository's standard GitHub flow.

Reuse an existing work branch or pull request when appropriate; otherwise use a dedicated branch, publish the task-related commits, open or update a pull request when repository policy uses one, inspect required checks on the current SHA, integrate with an allowed method when authorized and verified, and confirm the final remote state.

An unavailable local checkout changes the implementation route rather than the delivery contract when authenticated structured remote-write tooling can safely apply the bounded change.

**Invariant:** Publication stops before any remote action that would create material risk, including secret or sensitive-data exposure, unresolved destructive or irreversible data/schema effects, uncertain security consequences, non-trivial conflicts, unrelated or unreviewable changes, or a required shared-history rewrite. Integration additionally requires passing required checks and resolved material behavioral or public-contract questions.

When merge risk is material but an isolated remote branch and pull request are safe, publish or update the pull request and stop before merge. When publication itself is unsafe, keep the change unpublished and report the concrete blocker and what would be required to proceed safely.

For direct `#BUG`, `shared_codex_remediation_loop.md` authorizes ChatGPT to publish and integrate verified in-scope corrections directly when safe. Any delegated Codex step must publish its verified task state when safe, return the resulting identifiers, and yield control to ChatGPT for independent remote review before remediation continues.

## Delegated continuation compatibility

When another workflow explicitly reuses this bug correction contract, such as `#FIX`, that delegating workflow owns continuation authorization. In that context, a response consisting only of `ok` may authorize exactly one further correction batch when the delegating workflow says so, and remote-authorized bug corrections retain routine remote publication and integration. This compatibility clause does not change the direct `#BUG` state machine owned by `shared_codex_remediation_loop.md`.

For repeated autonomous cleanup without the direct ChatGPT/Codex review loop, use `06_cyclic_agent_workflow.md` only when `#CYCLE` is explicitly selected.