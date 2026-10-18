# Performance audit and optimization

## Activation

Use this module to evaluate a repository for meaningful performance improvements and define the technical optimization contract for later remediation. Apply `shared_intensive_audit.md` for the shared inventory, coverage, saturation, presentation, and bounded-batch mechanics.

For a direct `#OPT` invocation, the initial response is the audit inventory. After that inventory, `shared_codex_remediation_loop.md` owns the direct-command `ok` handoff, ChatGPT-first optimization, minimal Codex handoffs when representative execution is necessary, remote review, human checkpoints, and completion semantics. The measurement and optimization requirements in this module remain authoritative whether work is executed directly by ChatGPT, delegated narrowly to Codex, or reused by another workflow.

This workflow targets execution time, latency, throughput, memory use, allocation pressure, I/O cost, and other measurable resource bottlenecks that matter under realistic supported workloads. It does not authorize behavior changes merely to obtain better benchmark numbers.

## Evidence and acceptance contract

**Invariant:** A performance finding is actionable only when it is supported by a reproducible or otherwise defensible baseline measurement tied to a realistic workload. Do not create actionable findings from intuition, micro-optimizations without evidence, contrived workloads, unsupported environments, or benchmark noise.

**Invariant:** A suspected bottleneck may still be included in the initial inventory as `requires validation` when source evidence, complexity analysis, profiling signals, repeated work, allocation behavior, I/O structure, or another defensible signal makes it materially worth measuring later. Such candidates must be clearly distinguished from measured actionable findings, must not claim measured savings, and must not be corrected until a reliable baseline is obtained.

**Invariant:** Before changing an actionable target, measure the relevant time and/or memory baseline. After the change, rerun the same benchmark or workload under materially comparable conditions and report both before and after values. When statistical variability is material, use repeated runs and an appropriate aggregate such as median or distribution rather than a single favorable sample.

**Invariant:** Do not accept an optimization that changes required functionality, public contracts, observable results, numerical correctness, supported behavior, or data semantics unless the user explicitly authorizes that tradeoff. Run correctness and regression checks in addition to performance measurements.

**Invariant:** A correction is not considered successful merely because code is theoretically faster. It must show a meaningful measured improvement in at least one relevant metric without a material regression in another relevant metric or in correctness. If measurements are inconclusive, classify the result as inconclusive and do not claim an improvement.

## Performance-specific coverage

Inspect all applicable surfaces with plausible performance relevance under the shared coverage ledger and saturation contract:

- hot paths identified by profiling or representative timing;
- repeated allocations, copies, conversions, serialization, parsing, or data movement;
- algorithmic complexity on realistic input sizes;
- unnecessary I/O, network, filesystem, database, or subprocess work;
- cache behavior and repeated recomputation;
- vectorization, batching, concurrency, synchronization, queueing, and scheduling overhead when applicable;
- memory peaks, retained objects, allocation churn, buffer sizing, and data representation;
- startup, build, import, inference, training, request, CLI, or pipeline latency when these are material product behaviors;
- repeated initialization, compilation, graph construction, model loading, preprocessing, postprocessing, or setup work across otherwise independent operations;
- cross-layer data conversions, device transfers, format changes, temporary materialization, and avoidable intermediate representations;
- scaling behavior as realistic data size, batch size, request count, graph size, tensor size, or concurrency grows;
- benchmark and test infrastructure itself when it can conceal relevant production costs or systematically measure an unrepresentative path.

Prefer repository-native benchmarks and profilers. If none exist, create the smallest reproducible benchmark harness needed for the finding, keeping it separate from production behavior unless a permanent regression benchmark is justified.

Identify representative supported workloads rather than measuring only one convenient path. Use profiling or targeted timing for dominant costs where practical, but also inspect scaling and repeated-work patterns that a short profile may miss. Inspect adjacent callers and consumers after finding a bottleneck so repeated instances are not left for later rediscovery.

**Invariant:** Do not use the requirement for a measured baseline as a reason to stop discovery after a small number of expensive measurements. Continue source- and profiler-led discovery across the applicable performance surface, reporting defensible unmeasured candidates as `requires validation` rather than silently omitting them.

**Default:** When several candidates compete for measurement effort, measure representative high-impact candidates first and retain the remaining materially supported candidates in the inventory with the exact workload, metric to establish, evidence, and validation requirement needed to promote them to actionable status.

**Invariant:** The low-finding deepening thresholds in `shared_intensive_audit.md` apply to the combined inventory of measured findings and materially supported validation candidates. They trigger additional discovery and measurement effort, never speculative findings or fabricated baselines.

## Finding contract and severity

The initial inventory uses the shared presentation contract with severity sections in this exact order: `HIGH`, `MEDIUM`, `LOW`.

Each finding must use an `OPT-ID` and include, when applicable:

- **Estado:** `open`, `fixed`, `not reproducible`, `accepted`, `inconclusive`, `requires validation`, or `requires decision`.
- **Tipo:** confirmed performance bottleneck, probable performance bottleneck, or requires validation.
- **Ubicación:** file, symbol, pipeline stage, query, configuration, or other precise target.
- **Carga:** realistic workload and input size used for measurement, or the exact workload that must be measured for a validation candidate.
- **Métrica:** time, latency, throughput, peak memory, allocations, I/O, or another relevant metric.
- **Baseline:** measured value, repetitions/statistic when material, and measurement method; for `requires validation`, state explicitly that the baseline is pending and what measurement is required.
- **Evidencia:** profiler trace, benchmark result, complexity evidence, repeated-work evidence, allocation/I/O structure, or other defensible support.
- **Impacto:** why the measured or strongly suspected cost matters in practical use.
- **Condición:** realistic trigger, scale, or operating condition under which the cost appears.
- **Hipótesis de mejora:** concise mechanism that could plausibly improve the metric without changing required behavior.
- **Confianza:** confidence level and material uncertainty.

Within each severity, rank measured actionable findings ahead of validation candidates of otherwise equal practical priority. Do not report speculative savings as measured results.

Severity:

- `HIGH`: a primary workflow or hot path has a large, frequent, or scaling performance cost that materially blocks normal use, exceeds a stated target, or causes realistic memory/resource exhaustion.
- `MEDIUM`: a meaningful bottleneck or resource inefficiency affects a bounded but relevant workload and is worth correcting.
- `LOW`: a localized measurable inefficiency with modest practical impact and a low-risk correction path.

Do not use `CRITICAL` merely because an optimization is large. If the observed behavior is an outage, corruption, security defect, or correctness failure, route that responsibility to the appropriate bug or security workflow instead.

## First response and stopping criterion

Follow the shared initial-inventory contract. Ephemeral local measurement artifacts may be used but must not be persisted in the repository. A materially supported candidate that lacks a reliable baseline may be included as `requires validation` with the exact pending measurement requirement and may not be corrected until validated.

If a reliable baseline cannot be obtained for a suspected bottleneck, report it only when materially useful as `inconclusive` or `requires validation`. Do not rank an unmeasured candidate ahead of a measured actionable finding of comparable practical impact.

The audit reaches its stopping condition when the shared coverage and saturation passes reveal no remaining meaningful measured optimization opportunities or materially supported candidates under realistic supported workloads, or when remaining opportunities require product-level tradeoffs, architectural changes, unavailable hardware/data, or measurement conditions that cannot be established safely.

For a direct `#OPT` invocation, do not modify files or remote state after the inventory merely because findings are actionable. Wait for the isolated `ok` defined by `shared_codex_remediation_loop.md`; after that authorization, execute its ChatGPT-first remediation loop. Delegate only the minimum concrete benchmark, reproduction, fine-tuning, or other execution dependency that cannot be established reliably with ChatGPT's available tools and remote CI.

## Performance correction execution contract

Apply this section to every correction unit in direct `#OPT` remediation, whether executed by ChatGPT or delegated to Codex, and whenever another workflow explicitly delegates a bounded performance correction to this module.

A correction unit should contain one measured performance finding or a small group of tightly related measured findings that can be reviewed and verified coherently. A `requires validation` candidate must first obtain a reliable baseline and become actionable before production code is changed for it. Prefer the highest-priority safely actionable findings first: `HIGH`, then `MEDIUM`, then `LOW`.

**Invariant:** When this workflow is executed by Codex without `#CYCLE`, perform the entire correction batch in the same Codex agent. Do not spawn or delegate to corrector subagents, parallel agents, background agents, agent pools, or equivalent delegated workers. The only exception is when `#CYCLE` actively selects `06_cyclic_agent_workflow.md`, whose own bounded subagent contract then governs the cycle.

For every corrected finding:

1. reproduce the baseline on the current pre-change state when feasible;
2. identify the smallest optimization that addresses the measured bottleneck;
3. preserve functionality and public behavior;
4. rerun the same performance measurement under comparable conditions;
5. run affected correctness, regression, type, lint, build, and repository-native checks;
6. inspect the diff for unrelated changes;
7. accept the change only when the improvement is meaningful and repeatable enough for the workload and no material regression is introduced.

Revert or leave unapplied an attempted optimization that is slower, materially more memory-hungry without an authorized tradeoff, behavior-changing, unstable, or inconclusive.

## Measurement discipline

Use the strongest practical measurement design supported by the repository.

**Invariant:** Run ad-hoc performance measurements in a fresh isolated process when a long-lived or stateful analysis runtime could retain unrelated imports, instrumentation, caches, prior allocations, GUI state, or previous executions that can affect timing, memory, reliability, or reproducibility. Load only the target workload and dependencies required for that measurement; do not use a materially contaminated shared analysis session as the baseline.

**Invariant:** When a measurement attempt fails or becomes materially unreliable because of the execution environment, do not keep retrying the same contaminated stateful runtime. Switch to a fresh execution surface when one is available; otherwise classify the measurement as unavailable or inconclusive rather than fabricating or overclaiming a baseline.

- keep hardware, runtime, dependency versions, dataset/input, process mode, warmup policy, concurrency, and benchmark command comparable before and after;
- distinguish cold-start from steady-state performance when both matter;
- use several repetitions when noise is non-trivial and report the statistic used;
- avoid comparing debug against optimized/release builds or different dependency states unless that difference is the intended change;
- report absolute values and percentage deltas when meaningful;
- measure peak memory or allocation behavior with a method appropriate to the runtime rather than inferring memory savings from source changes;
- record unavoidable comparability limitations and lower confidence accordingly.

A benchmark added for regression protection should test a stable performance contract or trend and avoid brittle thresholds that fail from ordinary CI variance unless the repository has controlled runners.

Every accepted optimization report must include comparable before/after time and/or memory values, repetitions/statistic when material, percentage delta when meaningful, and the benchmark command or method. An accepted optimization always reports these before/after measurements.

## Remote publication and integration for authorized performance corrections

When the enclosing workflow authorizes remote publication, load `../github/00_core.md`, `../github/indice_github.csv`, and `../github/01_integration_and_publication.md` only when publication or remote verification actually begins. Publish through the repository's normal GitHub flow and integrate only when the performance evidence is conclusive, required correctness checks pass, the benchmark is comparable, material tradeoffs are resolved, and repository protections permit it.

A safe reviewable pull request may be published without merge when verification is incomplete but the isolated change is useful for review. Never bypass protections, force shared history merely to complete a correction, expose sensitive data, or include unrelated work.

For direct `#OPT`, `shared_codex_remediation_loop.md` authorizes ChatGPT to publish and integrate verified measured optimizations directly when safe. Any delegated Codex step must publish its verified task state when safe, return the resulting identifiers and before/after evidence, and yield control to ChatGPT for independent remote review before remediation continues.
