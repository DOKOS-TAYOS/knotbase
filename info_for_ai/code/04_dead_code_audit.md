# Dead, unnecessary, or redundant code audit

## Activation

Use this module to locate unused, duplicated, unnecessarily complex, or redundant code and define the technical cleanup contract while preserving external behavior. Apply `shared_intensive_audit.md` for the shared inventory, coverage, saturation, presentation, and bounded-batch mechanics.

For a direct `#DEAD` invocation, the initial response is the audit inventory. After that inventory, `shared_codex_remediation_loop.md` owns the direct-command `ok` handoff, ChatGPT-first cleanup, minimal Codex handoffs when necessary, remote review, human checkpoints, and completion semantics. The cleanup requirements in this module remain authoritative whether cleanup is executed directly by ChatGPT, delegated narrowly to Codex, or reused by another workflow.

## Dead-code-specific coverage

Systematically inspect every applicable surface below under the shared coverage ledger and saturation contract:

- modules, files, classes, functions, methods, constants, branches, helpers, wrappers, adapters, and internal APIs for reachability and actual consumers;
- imports, exports, re-exports, package entry points, CLI entry points, plugin registrations, hooks, decorators, callbacks, reflection, dynamic imports, registries, serialization names, and other indirect consumers;
- duplicate implementations, repeated transformations, parallel helpers, compatibility shims, legacy code paths, and copy-pasted logic that may have diverged;
- dependencies, optional dependencies, extras, build requirements, development requirements, scripts, tools, and transitive-looking packages that may actually be direct runtime requirements;
- configuration keys, environment variables, feature flags, defaults, fallback branches, platform-specific paths, version gates, and obsolete migration or compatibility settings;
- tests, fixtures, snapshots, mocks, utilities, benchmark helpers, generated-test support, and redundant tests whose asserted behavior is already covered more directly;
- documentation, examples, comments, changelog references, scripts, packaging metadata, and user-facing instructions that refer to removed, renamed, or obsolete elements;
- unnecessary abstractions and internal APIs whose only consumers are pass-through wrappers or whose indirection can be removed without losing required reuse, compatibility, or clarity;
- impossible branches or validations made unreachable by stronger upstream invariants, schemas, types, or control flow;
- repeated instances adjacent to a proven dead or redundant pattern, so the audit does not report one representative example while leaving equivalent occurrences undiscovered.

**Invariant:** Do not classify code as unused solely from textual reference counts. Establish relevant direct and indirect consumers, public or package contracts, runtime registration, reflection, generated use, serialization compatibility, platform/version branches, and distribution behavior before treating removal as sufficiently evidenced.

Use call-site and import tracing, repository-native tests/builds, package metadata inspection, static analysis, symbol/reference search, duplicate-pattern inspection, configuration comparison, and executable entry-point checks when they provide materially different evidence. In the shared saturation pass, inspect siblings and analogous subsystems after proving one obsolete wrapper, duplicate helper, stale configuration family, unused dependency, or similar pattern.

## Finding contract and severity

The initial inventory uses the shared presentation contract with severity sections in this exact order: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.

Each finding must use a `DEAD-ID` and include, when applicable:

- **Estado:** `open`, `removed`, `consolidated`, `false positive`, `accepted`, or `requires decision`.
- **Tipo:** dead code, duplication, impossible branch, unused dependency, obsolete configuration, unnecessary abstraction, internal API without consumers, redundant test, stale documentation, or requires validation.
- **Ubicación:** file, symbol, configuration key, dependency, test, documentation section, or other precise location.
- **Evidencia:** concise evidence of use, non-use, duplication, obsolescence, or why further validation is still required.
- **Riesgo de retirada:** compatibility, runtime, plugin, reflection, packaging, public API, data, or other concrete risk introduced by removing or consolidating it.
- **Impacto de mantenimiento:** concrete complexity, divergence, dependency, review, testing, documentation, or operational cost caused by keeping it.
- **Condición:** relevant scope or precondition under which the finding is actually redundant or removable, when needed to avoid overclaiming.
- **Confianza:** confidence level and any material uncertainty.

Severity:

- `CRITICAL`: redundancy or obsolete code that causes a vulnerability, corruption, incorrect publication, or inability to operate the project.
- `HIGH`: duplication or an obsolete path that produces divergent results, introduces dangerous dependencies, or blocks important changes.
- `MEDIUM`: complexity, duplication, or a dependency that raises maintenance cost without usually affecting results.
- `LOW`: local cleanup, an obsolete comment, unreachable validation, or a low-risk simplification.

## First response

Follow the shared initial-inventory contract. Cover dead code, duplication, impossible branches, unused dependencies, obsolete configuration, unnecessary abstractions, internal APIs without consumers, redundant tests, and documentation for removed elements. Do not force a finding count or label dynamic, public, reflection-loaded, generated, serialized-compatibility, entry-point, or plugin code as dead without evidence.

For a direct `#DEAD` invocation, do not modify files or remote state after the inventory merely because findings are actionable. Wait for the isolated `ok` defined by `shared_codex_remediation_loop.md`; after that authorization, execute its ChatGPT-first remediation loop and delegate only concrete execution or verification dependencies that meet its Codex handoff criteria.

## Dead-code cleanup execution contract

Apply this section to every cleanup unit in direct `#DEAD` remediation, whether executed by ChatGPT or delegated to Codex, and whenever another workflow explicitly delegates a bounded dead-code cleanup to this module.

Address the highest-priority sufficiently evidenced open findings first: `CRITICAL`, then `HIGH`, then `MEDIUM`, then `LOW`. A cleanup unit may contain one finding or a small tightly related group that can be reviewed and verified coherently. Do not expand a cleanup unit merely because more findings are available.

Before removing or consolidating anything:

1. identify direct and indirect consumers, entry points, plugins, reflection, runtime registration, distribution files, serialized compatibility, supported platform/version gates, and public compatibility relevant to the target;
2. confirm that deletion or consolidation is justified by current evidence rather than reference-count absence alone;
3. choose the smallest removal or consolidation that preserves supported external behavior;
4. update affected tests, documentation, packaging, configuration, or metadata only when the cleanup makes them stale;
5. run the relevant build, tests, packaging, static checks, entry-point checks, or other repository-native verification;
6. inspect the final diff for unrelated changes and for accidental removal of supported behavior.

Track each finding as `open`, `removed`, `consolidated`, `false positive`, `accepted`, or `requires decision`. Do not claim removal safety without evidence covering the material consumer and compatibility surfaces.

When this contract is executed by Codex, the entire authorized cleanup unit must run in the same Codex agent. Do not spawn or delegate to corrector subagents, parallel agents, background agents, agent pools, or equivalent delegated workers. The only exception is an independently activated `#CYCLE` workflow under its own contract.

## Publication semantics

For a direct `#DEAD` workflow, the isolated `ok` authorizes the ChatGPT-first remediation loop to publish and integrate verified in-scope cleanup through the target repository's authenticated remote when safe. At publication time load `../github/00_core.md`, `../github/indice_github.csv`, and the applicable indexed GitHub integration module. Any delegated Codex step publishes only its verified task state to the current safe work branch or pull request by default, then yields control to ChatGPT for independent remote review.

**Invariant:** Direct `#DEAD` publication stops before any remote action that would create material risk, including uncertain removal safety, secret exposure, non-trivial conflicts, unrelated or unreviewable changes, destructive shared-history changes, or required checks that do not support safe integration. A safe reviewable branch or pull request may be published while integration remains blocked.

**Invariant:** When this dead-code cleanup contract is reused by `#FIX`, `#CYCLE`, or another delegating workflow that has not explicitly selected `shared_codex_remediation_loop.md`, do not inherit the direct `#DEAD` remote-publication authorization. Preserve the delegating workflow's own publication envelope. In particular, delegated dead-code cleanup remains local-only when that workflow says so.

For direct `#DEAD`, ChatGPT reviews every returned Codex publication against the current remote state and then resumes direct remediation whenever its available tools are sufficient.
