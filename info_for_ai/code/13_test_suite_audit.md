# Test-suite audit and iterative hardening

## Activation

Use this module to audit the quality and effectiveness of a repository's automated tests and improve them later in bounded, verified batches.

This workflow is for test-suite quality: whether the tests provide credible protection for supported behavior, contracts, failure modes, numerical properties, and important integration paths. It is not a substitute for the bug, performance, security, dead-code, or refactoring workflows.

## Core contract

**Invariant:** The first response is inventory-only. Do not modify files or remote state during the initial audit.

**Invariant:** A testing finding must describe a concrete gap in the suite's ability to detect a realistic regression or validate an important contract. Do not create findings merely because a line, branch, file, or function lacks coverage.

**Invariant:** Coverage is evidence, not the objective. Do not optimize for 100% line or branch coverage, add tests that exercise code without meaningful assertions, or duplicate equivalent cases simply to increase a percentage.

**Invariant:** Test improvements must preserve intended production behavior. Do not silently change production semantics, public contracts, error behavior, numerical results, formats, or compatibility merely to make a new test pass.

**Invariant:** When the audit exposes an actual product defect, do not encode the defective behavior as the expected result and do not silently fix it under the testing workflow. Record the boundary clearly and route the production correction through the bug workflow or a separately authorized correction workflow.

**Default:** Prefer tests that protect stable observable behavior, domain invariants, and realistic integration boundaries over tests tightly coupled to private implementation details.

## What to inspect

Inspect the existing suite, test configuration, fixtures, helpers, CI execution surfaces when relevant, and the production contracts needed to judge whether the tests are meaningful.

Look for supported, evidenced problems such as:

- primary user-facing or library behavior with no meaningful automated protection;
- public APIs, CLIs, serialization formats, file formats, or configuration contracts tested only superficially;
- important error and validation paths that are untested despite realistic supported inputs;
- assertions that are absent, vacuous, overly broad, tautological, or incapable of distinguishing correct from materially incorrect behavior;
- tests that only check that code executes without validating the result that matters;
- tests whose expected values are derived by the same implementation logic they are meant to verify;
- excessive mocking that bypasses the behavior, integration boundary, protocol, or dependency interaction that actually needs protection;
- mocks, stubs, or fixtures that no longer represent realistic dependency behavior;
- integration gaps between components that are individually tested but can fail when composed;
- missing round-trip, persistence, parsing, serialization, migration, or compatibility checks where those contracts matter;
- flaky tests caused by time, randomness, concurrency, shared state, test ordering, filesystem state, network assumptions, resource races, or environment leakage;
- order-dependent tests or fixtures that do not clean up state reliably;
- tests coupled so tightly to private implementation details that harmless refactoring causes unnecessary failures;
- snapshot or golden-file tests whose assertions are too broad to reveal the semantically important change or too easy to update blindly;
- duplicated tests that add maintenance cost without materially increasing behavioral protection;
- skipped, disabled, or broadly `xfail`-marked tests that conceal an important unsupported or broken path;
- platform, runtime, dependency-version, locale, timezone, encoding, or architecture gaps when the repository explicitly supports those surfaces;
- concurrency or async behavior without tests for realistic ordering, cancellation, retry, or shared-state conditions when those behaviors are part of supported use;
- security-sensitive validation represented only by happy-path tests when a plausible exposed boundary requires negative cases;
- test helpers whose own bugs can make many tests pass for the wrong reason;
- CI or test-runner configuration that omits an important test group that repository policy intends to execute;
- expensive tests whose cost causes meaningful parts of the suite to be skipped in ordinary verification, when a smaller representative structure can preserve confidence.

A long test file, a low raw coverage percentage, a high raw coverage percentage, or a large test count is not a finding by itself.

## Evidence standard

Each finding should connect three things whenever they are available:

1. the production behavior or contract that matters;
2. the current test behavior or absence of protection;
3. a realistic regression that the current suite would fail to detect or would detect unreliably.

Prefer direct evidence such as existing tests, fixtures, supported interfaces, documented behavior, representative inputs, coverage reports, test-runner output, historical failures, or a small characterization experiment.

Do not claim that a test is flaky from one isolated failure when a deterministic defect, environment issue, or infrastructure failure remains a plausible explanation. Reproduce or gather repeated evidence when feasible.

Do not claim that a path is untested solely from source inspection when parametrization, generated cases, integration tests, or indirect contract tests may cover it. Trace the relevant test behavior before classifying the gap.

## Coverage, mutation, and generated testing

Use line and branch coverage to locate suspiciously unprotected surfaces, not to rank findings mechanically.

Mutation testing can provide strong evidence that assertions are weak when the repository already has suitable tooling or when a focused local experiment is practical without changing the repository. Do not introduce a new mutation-testing dependency merely to satisfy this audit unless separately justified and authorized.

Property-based or generative testing is useful when the behavior has meaningful invariants, a broad structured input space, parsers or serializers, algebraic properties, numerical domains, or many equivalent edge cases. Recommend or add it only when it provides more protection than a small explicit example set. Do not add a new property-testing dependency automatically when the repository does not already use one.

Parameterized tests are preferred when several cases exercise the same contract cleanly. Do not compress cases into parameterization when separate tests communicate materially different contracts or failure semantics more clearly.

## Scientific and numerical software

For scientific, mathematical, simulation, or numerical repositories, prioritize tests that establish scientific correctness rather than merely code execution.

Relevant protection may include:

- analytically solvable or independently known reference cases;
- dimensional, shape, dtype, domain, symmetry, normalization, conservation, monotonicity, positivity, or boundedness invariants when mathematically justified;
- stable tolerances that account for expected floating-point behavior without masking materially incorrect results;
- comparisons against an independent implementation or reference value when feasible;
- reproducibility of seeded stochastic calculations where deterministic replay is part of the contract;
- statistical validation for genuinely stochastic outputs instead of brittle equality assertions;
- boundary regimes, singular limits, small-system instances, or reduced cases whose expected behavior can be independently established;
- tests that distinguish numerical instability from acceptable floating-point variation;
- validation that experiment configuration, data construction, and result extraction preserve the intended scientific meaning.

Do not require exact floating-point equality unless exact equality is itself the intended contract. Do not choose arbitrary tolerances solely to make a failing test pass; justify them from numerical scale, algorithmic error, or established repository behavior.

## Boundaries with other workflows

Route the primary responsibility correctly:

- Incorrect production behavior, materially wrong results, contract violations, corruption, or functional failures belong to the bug workflow.
- Security vulnerabilities belong to the security or bug workflow depending on the repository's established routing.
- Measured test or application performance bottlenecks belong primarily to the performance workflow when optimization is the objective.
- Unused or obsolete test code that can simply be removed belongs primarily to the dead-code workflow.
- Structural production changes whose main purpose is maintainability belong to the refactoring workflow.

A testing batch may make a small behavior-preserving refactor when it is demonstrably necessary to test an important contract cleanly. In that case, load and follow `05_readable_refactoring.md` for the refactoring portion, keep the change minimal, and preserve all production contracts.

If a proposed test requires changing production behavior to define a previously ambiguous contract, mark the finding `requires decision` rather than choosing the contract implicitly.

## Practical scope and stopping criterion

**Invariant:** Be systematic, but do not target a finding count, coverage percentage, mutation score, test count, or testing-framework feature checklist.

Do not inflate the audit with:

- trivial getters, constant declarations, or mechanically obvious glue with negligible regression risk;
- impossible or unsupported environments;
- contrived edge cases with no credible route from supported use;
- several tests that exercise the same contract without adding distinct failure detection;
- implementation-detail assertions that make legitimate refactoring harder;
- generalized test infrastructure for hypothetical future requirements;
- new frameworks or dependencies when the existing test stack can express the required protection clearly;
- expensive end-to-end tests when a smaller integration or contract test provides equivalent confidence;
- stylistic preferences about test organization that do not materially affect reliability, clarity, or maintenance.

The audit is complete when no remaining testing opportunity has a sufficiently favorable reduction in realistic regression risk relative to its maintenance cost, runtime cost, brittleness, and implementation complexity.

## Initial inventory report layout

Use this structure only for the first inventory response:

1. Start with `AUDITORÍA`.
2. Add at most one concise unlabelled context paragraph, and only when the inspected surfaces, verification environment, or a concrete limitation materially changes how the inventory should be interpreted.
3. Add one compact line beginning exactly with `Resultado:` that summarizes finding counts by severity, distinguishes confirmed gaps from items requiring validation when material, and states that no files or remote state were modified.
4. Emit only non-empty severity sections, in this exact order when present: `HIGH`, `MEDIUM`, `LOW`. If there are no findings, end after `Resultado:` with one short `Sin hallazgos accionables.` statement.

Do not use `CRITICAL` merely for a severe test gap. If evidence demonstrates an actual critical production or security defect, route that defect to the appropriate workflow.

## Finding layout

**Invariant:** Format findings for scanning. Each finding starts with its numbered `TEST-ID` and short title. Preserve all decision-relevant semantics below when applicable, but do not mechanically emit one bullet per named field. Use no more than four bullets by default; exceed that only when an additional field materially changes priority, actionability, or safe implementation.

The semantic fields remain:

- **Estado:** `open`, `improved`, `accepted`, `not applicable`, `requires validation`, `requires bug fix`, or `requires decision`.
- **Tipo:** missing contract protection, weak assertion, excessive mocking, integration gap, flaky test, state leakage, brittle implementation coupling, fixture or helper risk, CI execution gap, numerical validation gap, redundant testing, disabled protection, or another precise testing-quality category.
- **Ubicación:** exact production and test files, symbols, fixtures, configuration, or CI surface.
- **Contrato o comportamiento:** the supported behavior that deserves protection.
- **Evidencia:** concise evidence showing the current suite's limitation.
- **Riesgo:** the realistic regression or incorrect state that could escape detection or produce unreliable verification.
- **Propuesta:** the smallest plausible improvement in the test suite.
- **Cambios esperados:** test, fixture, helper, configuration, or minimal behavior-preserving production surfaces likely to change.
- **Verificación:** tests, coverage comparison, repeated runs, mutation experiment, platform checks, or other evidence needed to validate the improvement.
- **Confianza:** confidence level and material uncertainty.

Compact presentation defaults:

- retain a precise `Ubicación:` whenever one exists;
- normally combine the protected contract, current evidence, and realistic missed regression into one or two `Evidencia:` / `Riesgo:` lines rather than repeating them across separate bullets;
- normally combine `Propuesta` and `Cambios esperados` into a single `Dirección:` line, keeping `Verificación:` separate only when it materially affects implementation or acceptance;
- omit `Estado: open`, a separate `Tipo:` that is already evident from the title/evidence, and `Confianza:` when confidence is high and the evidence already supports the finding;
- surface non-default states such as `requires validation`, `requires bug fix`, or `requires decision`, and material uncertainty, compactly where they affect actionability.

Keep a blank line between findings. Omit empty severity sections instead of adding no-findings filler for each severity.

## Severity

- `HIGH`: an important primary contract has little or misleading automated protection, the suite can pass while a major realistic regression remains undetected, or flakiness or infrastructure problems materially undermine trust in ordinary verification.
- `MEDIUM`: a meaningful bounded behavior, integration path, error condition, numerical property, or maintenance surface lacks reliable protection and creates a realistic regression risk.
- `LOW`: a localized test-quality improvement has modest but real value and a low-risk implementation path.

Severity represents the risk created by inadequate verification, not an assertion that the underlying product currently contains a defect of the same severity.

## Continuation with `ok`

**Invariant:** In the direct continuation of the same `#TEST` audit, a user response consisting only of `ok`, case-insensitively and ignoring surrounding whitespace, authorizes exactly the next bounded test-improvement batch on the same repository and scope.

The first such `ok` after the inventory authorizes the first batch. Each later direct-continuation `ok` authorizes one further batch. Additional text, a changed repository, a changed scope or objective, or another responsibility must be interpreted normally rather than as shorthand authorization.

This shorthand authorizes the test, fixture, helper, test-configuration, and minimal behavior-preserving production changes needed by exactly that batch, plus verification and routine remote publication and integration when safe. It does not authorize unrelated cleanup, silent production bug fixes, public-contract changes, speculative architecture, dependency expansion without justification, or bypassing repository protections.

## Test-improvement batches

For each authorized batch:

1. Select the highest-priority safely actionable open finding, or a small group of tightly related findings that form one coherent verification improvement.
2. Reconfirm the supported production contract from code, documentation, tests, interfaces, and representative use.
3. Establish why the current suite would miss or unreliably detect the target regression.
4. Apply the smallest test change that provides materially stronger protection.
5. Modify fixtures, helpers, or test configuration only when required for that protection.
6. If a small production refactor is necessary for testability, keep it behavior-preserving and use the refactoring workflow for that portion.
7. If the test reveals a real defect, classify the boundary and route the production correction through the appropriate workflow.
8. Run the new or changed tests first, then the materially affected broader suite and repository-native checks.
9. When flakiness is the target, run enough repeated or order-varied executions to provide evidence that the specific source of nondeterminism has been addressed.
10. When coverage or mutation evidence motivated the finding, compare the relevant evidence after the change, but judge success by improved regression detection rather than the raw metric.
11. Review the complete batch diff for brittle implementation coupling, unnecessary test duplication, weakened assertions, unjustified dependencies, and unrelated changes.
12. Update the finding state only when the improved protection and required verification are sufficiently demonstrated.

**Invariant:** Assertion strength, tolerances, retries, timeouts, skips, and expected-failure markers may change only when evidence establishes that the revised expectation is the intended contract; they are not mechanisms for obtaining a green suite by themselves.

## Remote publication and integration

**Default:** After an authorized batch is implemented and verification provides sufficient confidence, publish it through the repository's normal GitHub flow and normally integrate it when protections and checks permit.

Before remote mutation, load `../github/00_core.md`, `../github/indice_github.csv`, and `../github/01_integration_and_publication.md`, then follow their current-state, protection, CI, and final-verification requirements.

A changed head invalidates earlier CI evidence. Require fresh relevant checks for the batch before integration when the repository uses them.

If the new tests expose a production defect and therefore required checks fail for a legitimate reason, keep the result reviewable when safe, report the defect boundary, and route the production correction through the appropriate workflow before integration.

**Invariant:** Never bypass branch protection, required checks, review requirements, or other repository safeguards. Do not merge a batch with unresolved material test failures, ambiguous contract decisions, unjustified behavior changes, or unrelated modifications.

## Batch report layout

**Invariant:** Every authorized post-inventory test-improvement iteration uses this compact batch report and includes only the batch just executed plus the minimum remaining-state context needed for the next step.

Start directly with `Resultado:` unless one short opening sentence is genuinely needed to disambiguate the batch. Then use only sections that carry material information:

- `Resultado:` with the finding or findings improved, what remains, and the final local/remote state relevant to the batch;
- `Cambios:` with concise bullets for tests, fixtures, helpers, configuration, or minimal testability refactors actually changed;
- `Verificación:` with only checks actually run and their outcomes, including repeated-run, coverage, mutation, CI, or remote evidence when material;
- `Pendiente:` only when useful for remaining findings, a production bug, a contract decision, or another blocker.

Do not repeat unchanged repository context, audit methodology, or previously reported findings in later batches.

## Prompt handoff to Codex

Structure findings so a later `#PROMPT Codex; ...` request can delegate one testing improvement without forcing Codex to rediscover the audit.

Useful handoff context includes the finding identifier, exact files and symbols, production contract, current test gap, realistic missed regression, intended minimal test direction, out-of-scope production changes, fixtures or helpers involved, existing test commands, and acceptance criteria.

Do not duplicate the prompt-generation workflow here.

## Completion criterion

The objective is not maximum coverage or the largest possible suite. The workflow is complete when the repository has proportionate, maintainable, and credible automated protection for its important supported behavior and no remaining actionable testing finding clearly justifies its maintenance and execution cost.
