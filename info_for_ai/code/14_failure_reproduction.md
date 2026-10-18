# Targeted failure reproduction

## Activation

Use this module when the user provides one concrete problem in one repository and wants it reproduced, minimized, and evidenced without correcting it.

This workflow is narrower than the bug audit. It starts from a reported failure, error, traceback, incorrect behavior, issue description, or other concrete symptom. Do not turn it into a repository-wide defect search.

## Objective

Establish whether the supplied problem can be reproduced under realistic supported use, identify the minimal sufficient conditions that trigger it, and leave concise evidence that can be used by a later correction workflow.

A successful reproduction does not authorize a fix.

## Allowed local artifacts

**Default:** Prefer a no-mutation reproduction when commands, inputs, environment details, and observed output are enough to demonstrate the problem.

When persistent executable evidence materially improves reliability, you may create exactly the smallest task-scoped local artifact needed to reproduce the problem, normally one of:

- a focused regression test that deliberately fails against the current defective behavior;
- a minimal reproduction harness or script;
- a small fixture required only by that regression test or reproduction harness.

Keep these artifacts local. Do not modify production behavior merely to make reproduction easier. Do not create generic debugging frameworks, broad test scaffolding, unrelated cleanup, or speculative instrumentation.

## Procedure

1. Read the supplied problem literally and identify the claimed observable symptom, expected behavior when known, and any stated inputs, environment, configuration, or sequence.
2. Inspect only the repository surface needed to understand and exercise that problem. Respect repository-local instructions and supported versions.
3. Attempt the most direct realistic reproduction first. Preserve the exact command, input, environment facts, and observed result that matter.
4. If the problem reproduces, vary one condition at a time to determine the minimal sufficient conditions. Remove incidental setup until further reduction would stop reproducing the symptom or would make the scenario unrealistic.
5. If a stable local artifact is justified, create the smallest regression test or reproduction harness that demonstrates the symptom without repairing it.
6. Inspect the execution path only far enough to identify a plausible immediate location or mechanism that explains the reproduction. Distinguish observed evidence from hypotheses.
7. Stop once the supplied problem is reliably classified and the evidence is sufficient for a later correction decision. Do not continue into a broad bug audit.

## Reproduction status

Report exactly one primary status:

- `reproduced`: the supplied symptom was observed under realistic supported conditions with repeatable evidence.
- `partially reproduced`: a materially related symptom was observed, but one or more supplied conditions, outputs, or consequences could not be matched.
- `not reproduced`: a reasonable bounded attempt under supported conditions did not produce the supplied symptom.
- `insufficient evidence`: the problem cannot be tested responsibly because required inputs, environment, access, state, or other essential evidence is unavailable.

Do not convert `not reproduced` into `reproduced` by changing the problem, using an unsupported environment, or inventing missing preconditions.

## Realistic scope

**Invariant:** Reproduction must reflect realistic supported use. Do not manufacture success through pathological inputs, unsupported platforms, intentionally corrupted state with no credible route from normal use, unrealistic resource exhaustion, or other artificial breakage unless the supplied problem explicitly concerns that condition and the repository supports it.

Security-relevant adversarial inputs remain valid when they represent a plausible exposed attack surface.

## Minimization

When reproduction succeeds, identify the minimal sufficient conditions that remain evidenced. Separate:

- required input or data;
- required configuration or state;
- required environment or supported version;
- required action sequence;
- the smallest implicated component or execution path that the evidence supports.

Do not claim that a condition is necessary merely because it appeared in the original report. Verify removals or variations when practical.

## Boundaries with other workflows

Do not fix the defect under this workflow. Do not alter production code, public contracts, dependency versions, schemas, behavior, or remote state.

Do not publish branches, commits, pull requests, issues, comments, CI reruns, or other GitHub mutations. Local reproduction artifacts may remain in the working tree for later use, but remote publication requires separate authorization under the appropriate workflow.

If the task becomes a broad search for additional defects, use the bug-audit workflow instead. If the user later authorizes correction of an already identified finding, use the applicable correction workflow rather than silently extending reproduction into implementation.

## Verification

A `reproduced` result requires direct observed evidence, not inference alone. Re-run the minimized reproduction when practical to confirm stability.

A `partially reproduced`, `not reproduced`, or `insufficient evidence` result must state what was actually attempted and the material limitation or mismatch. Do not imply that the repository is defect-free merely because one reported problem was not reproduced.

## User-facing result

Keep the result compact and operational. Include:

- `Estado:` with exactly one reproduction status;
- `Síntoma:` the observed behavior or the closest observed mismatch;
- `Condiciones mínimas:` the minimal sufficient conditions when established;
- `Evidencia:` commands, inputs, outputs, test result, or other direct observation;
- `Localización probable:` only when supported, clearly separating evidence from hypothesis;
- `Artefacto local:` the regression test or reproduction harness created, or `ninguno`;
- `Siguiente paso:` the narrowest appropriate next action, without executing it.

Do not append speculative bug inventories or unrelated improvement suggestions.