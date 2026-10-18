# Refactoring audit and iterative cleanup

## Activation

Use this module to audit a repository for meaningful refactoring opportunities and apply them later in bounded, verified batches. Apply `shared_intensive_audit.md` for the shared inventory, coverage, saturation, presentation, and bounded-batch mechanics.

This workflow is for structural quality problems that are not primarily correctness defects, dead code, or measured performance bottlenecks. Its purpose is to reduce accidental complexity while preserving the software's useful behavior, public contracts, and relevant performance characteristics.

`#REFAC` remains the direct bounded-refactoring workflow. `#REFACT` is the audit-first workflow defined here.

For a direct `#REFACT` invocation, the initial response is the audit inventory. After that inventory, `shared_codex_remediation_loop.md` owns the direct-command `ok` handoff, ChatGPT-first refactoring, minimal Codex handoffs when necessary, remote review, human checkpoints, and completion semantics. The refactoring requirements in this module remain authoritative whether work is executed directly by ChatGPT or delegated narrowly to Codex.

## Core contract

**Invariant:** Refactoring is justified only when there is a concrete, defensible improvement in readability, maintainability, cohesion, coupling, testability, understandable data flow, necessary scalability, or reduction of future change risk. Do not create findings merely because code could be written differently.

**Invariant:** Preserve public APIs, observable results, data semantics, documented errors, file and wire formats, CLI behavior, supported configuration, serialization compatibility, numerical behavior, and other externally relevant contracts unless the user explicitly authorizes a change.

**Invariant:** Prefer the smallest structural change that achieves the improvement. Do not turn refactoring into a rewrite, architecture migration, framework introduction, speculative extensibility project, or broad style cleanup.

**Invariant:** Do not accept a refactor that introduces a material performance regression on a relevant workload. Benchmark only when the changed surface is performance-sensitive; do not add measurement ceremony to trivial changes.

## Refactoring-specific coverage

Inspect every materially applicable structural surface below under the shared coverage ledger and saturation contract:

- primary source modules and main execution or domain paths that define responsibility boundaries;
- package, module, class, function, and method boundaries, especially high-change or high-centrality areas;
- call chains and dependency direction around orchestration, stateful components, adapters, service boundaries, and shared utilities;
- data flow and ownership of important intermediate or mutable state;
- error propagation and recovery structure where exceptions, result types, retries, fallbacks, or validation are distributed across layers;
- configuration, dependency-injection surfaces, registries, factories, wrappers, plugins, hooks, and other indirection that can obscure ownership;
- repeated implementation patterns, local conventions, parallel abstractions, and cross-module duplication that create divergence risk even when no code is strictly dead;
- test structure where production design is difficult to characterize, isolate, or verify because of coupling or hidden state;
- public and internal APIs whose shape forces callers to understand unnecessary implementation detail or repeatedly assemble the same behavior;
- build, packaging, scripts, examples, and integration glue when they materially affect code organization or create duplicated orchestration;
- generated or AI-produced scaffolding, speculative extension points, defensive layers, and generalized interfaces that have no demonstrated present consumer;
- scientific or numerical pipelines where algorithm steps, state construction, numerical transformations, experiment orchestration, and result extraction are structurally difficult to audit or reproduce.

Look for concrete cognitive and maintenance costs such as oversized responsibilities, deeply nested flow, scattered mutable state, unnecessary coupling or indirection, misleading names, premature abstractions, fragmented configuration, opaque error handling, testability barriers, and AI-generated scaffolding without a demonstrated need.

Static complexity metrics, file length, searches, or import graphs are candidate signals rather than findings by themselves. Follow important call chains, consumers, state transitions, configuration paths, and test seams far enough to determine whether observed complexity is local, systemic, intentional, or repeated elsewhere. In the shared saturation pass, revisit high-centrality modules, weakly inspected boundaries, state ownership, cross-cutting helpers, testability barriers, and analogous areas after proving one repeated structural pattern.

## Boundaries with other workflows

- Incorrect behavior, security defects, corruption, or contract violations belong primarily to the bug or security workflow.
- Unused code, obsolete paths, unused dependencies, and code that can simply be removed belong primarily to the dead-code workflow.
- Measured latency, memory, throughput, or resource bottlenecks belong primarily to the performance workflow.
- A refactoring finding may mention overlap when structural quality contributes to another problem, but do not duplicate the same finding across audits merely to increase coverage.

If the audit discovers a material bug or security issue, report that boundary clearly rather than silently changing behavior under a refactoring label.

## Practical scope and stopping criterion

**Invariant:** Be systematic and intensive, but do not target a finding count. Report every sufficiently supported opportunity that matters under realistic maintenance or supported use, whether that produces three findings or thirty.

Do not inflate the inventory with purely subjective style preferences, theoretical rewrites with no clear maintenance benefit, micro-abstractions, fashionable architecture patterns, hypothetical extensibility, contrived edge cases, disproportionate defensive layers, arbitrary size thresholds, or generalization that makes current behavior harder to understand.

Security-relevant adversarial scenarios remain in scope when there is a plausible attack surface. The audit is complete when no remaining refactoring opportunity has a sufficiently favorable benefit-to-risk ratio. Code can be considered adequately refactored even when alternative implementations remain imaginable.

## Finding contract and severity

The initial inventory uses the shared presentation contract with severity sections in this exact order: `HIGH`, `MEDIUM`, `LOW`. Add `Cobertura:` before the severity sections with compact bullets summarizing materially relevant structural surfaces inspected, notable surfaces demonstrated not applicable, and concrete blocked or weakly verified areas.

Do not use `CRITICAL` merely for severe maintainability problems. If the current structure already causes corruption, security failure, systemic outage, or materially incorrect behavior, route that responsibility to the corresponding defect workflow.

Each finding must use a `REFACT-ID` and include, when applicable:

- **Estado:** `open`, `refactored`, `accepted`, `rejected`, `not applicable`, or `requires decision`.
- **Tipo:** excessive complexity, responsibility concentration, unnecessary indirection, premature abstraction, coupling, state or data-flow opacity, naming or structure problem, error-path complexity, scattered related logic, testability barrier, architectural inconsistency, or requires validation.
- **Ubicación:** precise files, symbols, classes, functions, modules, or configuration surfaces.
- **Problema:** why the current structure is unnecessarily difficult to understand, maintain, or evolve.
- **Evidencia:** concrete source evidence supporting the finding.
- **Impacto de mantenimiento:** practical cost in comprehension, review, testing, modification, coupling, divergence risk, or future defect risk.
- **Frecuencia o alcance:** how often maintainers, callers, tests, or adjacent subsystems encounter the structural cost when material to priority.
- **Propuesta:** the smallest plausible refactoring direction without pretending the exact patch is already validated.
- **Archivos implicados:** expected change surface and important consumers.
- **Riesgo del cambio:** realistic regression or compatibility risks.
- **Contratos a preservar:** relevant public behavior, formats, results, interfaces, numerical properties, or performance-sensitive behavior.
- **Alcance mínimo:** explicit boundary preventing rewrite or unrelated cleanup.
- **Verificación:** tests, characterization checks, builds, type checks, benchmarks, or other equivalence evidence required.
- **Confianza:** confidence level and any material uncertainty.

Severity:

- `HIGH`: structural complexity materially blocks safe work on a primary subsystem, creates dangerous coupling, makes important behavior unusually difficult to reason about, or substantially raises defect risk during normal maintenance.
- `MEDIUM`: a clear maintainability or design problem creates meaningful recurring cognitive or modification cost in a bounded area.
- `LOW`: a localized simplification with modest but real maintenance value and a low-risk correction path.

## Minimal-design discipline

**Invariant:** The preferred refactor is the simplest implementation that correctly expresses the required behavior and satisfies current repository contracts.

Prefer, in order when applicable:

1. removing accidental complexity;
2. making data flow and ownership explicit;
3. consolidating genuinely related logic;
4. improving names and boundaries;
5. introducing a new abstraction only when it demonstrably reduces the complexity of current code.

Do not add factories, registries, dependency-injection layers, service/repository layers, plugin systems, configuration frameworks, class hierarchies, wrappers, extensibility hooks, or generalized APIs unless the current repository has a concrete need for them.

An abstraction is justified when it reduces real duplication or coupling, represents several required existing variants, encapsulates a stable responsibility, materially improves testability, or is required by an existing architectural contract. "It may be useful later" is not sufficient. If the refactored version is harder for a competent maintainer to understand than the version it replaces, the refactor has failed even if it is more abstract.

## Scientific and experimental code

When generated or modified code is scientific or experimental under the activation condition in `00_core.md`, load and apply `experimental_scientific_code.md`. That module owns the scientific-experiment minimalism contract.

For such code, judge refactoring quality through the clarity of the algorithm, data construction, numerical transformations, experiment flow, reproducibility, and validation while preserving the experiment's actual purpose and contracts.

## Edge cases and defensive code

Evaluate edge-case handling proportionally to realistic supported use. Before adding or preserving defensive complexity, consider whether the state can realistically occur, its impact and frequency, whether the boundary is externally controllable, security implications, and the complexity introduced by the protection.

Do not preserve or introduce several layers of fallback, validation, exception translation, or state repair for scenarios with no credible path in normal supported operation and no security relevance.

## Direct continuation and remediation loop

**Invariant:** In the direct continuation of the same `#REFACT` audit, a user response consisting only of `ok`, case-insensitively and ignoring surrounding whitespace, activates `shared_codex_remediation_loop.md` for the current actionable refactoring inventory.

The isolated `ok` authorizes ChatGPT to apply, verify, and safely publish in-scope behavior-preserving refactors under this module until the stopping criterion is reached, a human decision is required, a human checkpoint is prudent, or a concrete execution or verification dependency is better delegated to Codex. It does not authorize public-contract changes, unrelated cleanup, speculative architecture, or unjustified dependency expansion.

Do not load GitHub integration during the inventory-only first turn. After the isolated `ok`, load the indexed GitHub integration responsibility only when remote mutation or verification actually begins.

## Refactoring correction execution contract

Apply this section to every correction unit in direct `#REFACT` remediation, whether executed by ChatGPT or delegated to Codex.

For each correction unit:

1. select the highest-priority safely actionable open finding, or a small tightly related group that forms one coherent structural change;
2. establish the current behavioral contract from tests, documentation, interfaces, and representative use;
3. add characterization tests only when important behavior is insufficiently protected and the test provides real equivalence evidence;
4. load and follow `05_readable_refactoring.md` for the actual refactoring work;
5. apply the smallest coherent change that resolves the structural problem;
6. preserve unrelated work and avoid opportunistic cleanup outside the selected finding;
7. run affected tests, type checks, lint, builds, integration checks, and repository-native validation as appropriate;
8. when the changed surface is performance-sensitive, compare a materially comparable before/after workload or benchmark;
9. review the complete correction diff for accidental behavior changes, unnecessary abstractions, and scope expansion;
10. update the finding state only when equivalence and structural improvement are sufficiently demonstrated.

A correction unit should remain small enough to review independently and revert without disentangling unrelated refactors. Reject or revert an attempt when it makes behavior less clear, materially worsens performance without authorization, changes public contracts, adds unjustified abstractions, or cannot be verified with sufficient confidence.

When this contract is executed by Codex, the entire delegated unit must run in the same Codex agent. Do not spawn or delegate to subagents, parallel agents, background agents, agent pools, or equivalent delegated workers.

## Remote publication for direct `#REFACT`

For direct `#REFACT`, the post-inventory isolated `ok` authorizes routine safe remote publication and integration of verified in-scope refactors under `shared_codex_remediation_loop.md`. Reuse an existing safe task branch or pull request when appropriate; otherwise publish through the repository's normal GitHub flow.

Any delegated Codex step publishes only the verified task-related state needed for ChatGPT to review and continue. ChatGPT independently verifies the remote diff and checks before integrating or advancing.

This direct remote-publication authorization does not transfer to `#REFAC` or to another workflow that reuses this module without explicitly selecting the shared remediation loop.

## Completion criterion

The objective is not "perfect" code. The workflow is complete when the changed repository is sufficiently clear, maintainable, and proportionate for its real purpose, with no remaining actionable structural findings whose expected maintenance benefit clearly justifies their risk and complexity.
