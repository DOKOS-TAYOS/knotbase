# Cyclic agent workflow

## Activation

Use this module together with another `code/` module when iterative improvement through independent assessment and correction batches is requested. It does not replace safety rules, human review, or Git protections.

**Invariant:** This workflow is the sole exception to the Codex single-agent rule in `00_core.md`. When and only when `#CYCLE` actively selects this module, subagents may be used for the roles defined below. Do not generalize this permission to the underlying BUG or DEAD workflow when it is run without `#CYCLE`, and do not use subagents outside the bounded cyclic roles defined here.

## Roles

- **Evaluator agent:** inspects the current state, applies the selected module, and produces a prioritized evidence-backed report. For every `MEDIUM` or `LOW` finding, it must state whether correction is recommended in the current cycle and briefly justify that recommendation. It does not make fixes during evaluation.
- **Corrector subagents:** receive only their relevant findings and fix independent batches with tests and diff review. They do not redefine evaluation criteria.
- **New evaluator:** runs the next audit from clean context without previous reports or applied solutions. It may read the repository and selected module but not earlier diagnoses, reducing confirmation bias.

## Cycle

1. Run the evaluator and retain its report for traceability.
2. Split all `CRITICAL` and `HIGH` findings, together with every `MEDIUM` or `LOW` finding that the evaluator recommends correcting in the current cycle, into non-overlapping batches. Assign each batch to a new corrector whose context is limited to the repository, module rules, and assigned findings.
3. Integrate only changes that pass relevant tests and conflict review.
4. Run a new clean evaluator on the integrated state.
5. Stop when the new evaluation contains no `CRITICAL` or `HIGH` findings and no `MEDIUM` or `LOW` findings recommended for correction in the current cycle. Otherwise continue with another batch. Never exceed ten correction batches; at the limit, deliver the residual report and request a human decision.

## Coordination rules

- Do not edit the same file in parallel unless regions are divided or changes are sequenced. Resolve conflicts before reevaluation.
- Each corrector must report addressed findings, changes, tests, limits, and untreated findings; it must not mark unverified work as fixed.
- The evaluator reopens a finding when the problem remains; the new report supersedes the previous label.
- Record each batch's finding count by severity, correctors used, verification, and stopping reason.
- A `MEDIUM` or `LOW` finding may remain untreated only when the current evaluator explicitly does not recommend correcting it in this cycle, or when a blocker or the batch limit prevents correction. Record the reason rather than silently converting recommended work into debt.

## Closing result

Provide a table by batch and a final state. Present remaining `MEDIUM` or `LOW` items as prioritized debt with the evaluator's reason for not recommending correction in the current cycle, or with the blocker that prevented correction. If the batch limit, a blocker, or risk leaves any `CRITICAL`, `HIGH`, or recommended `MEDIUM` or `LOW` findings, put them at the start of the report.
