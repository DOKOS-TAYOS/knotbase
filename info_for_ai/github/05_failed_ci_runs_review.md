# Failed CI and Actions runs review

## Activation and scope

Use this module when the user asks to review failed CI, GitHub Actions, workflows, checks, or comparable automated runs across one repository or across all of the user's accessible repositories.

This module owns remote discovery, current-health classification, diagnosis, bounded remediation, and evidence-based retry decisions for failed automation runs. If a repair requires modifying repository code or configuration locally, also route to the applicable `code/` instructions before making those changes. Do not turn a repository-wide run review into a general code audit.

**Default:** When the user says to review runs across "all my repositories", resolve the repository set through the inventory required by `00_core.md`, exclude archived and frozen repositories, and inspect only the remaining in-scope repositories. Do not assume that a repository with unavailable Actions data has no failed runs; classify access gaps explicitly.

When the user explicitly names a repository that the inventory marks as archived or frozen, do not inspect or repair its workflows, checks, or runs unless the user also explicitly asks to include that repository despite that status.

When the request supplies a specific pull request or branch target, restrict discovery, diagnosis, repair, rerun, and final health claims to automation relevant to that target. Do not use unrelated default-branch, release, scheduled, or other pull-request runs as substitutes for the target's current state. When no target is supplied for a single repository, use the current relevant automation surfaces under the normal rules below.

## 1. Establish current automation health

**Invariant:** Treat the current state of a repository as the latest relevant completed execution of each active workflow, not as the repository's single most recent run and not as the set of historical failures.

A repository can have several independent workflows. A recent successful CI run does not supersede a still-current failed publish, scheduled-maintenance, security, or release workflow. Conversely, an old failed run is not a current problem when the same workflow and relevant context have since succeeded or the workflow/context is no longer active.

Use the smallest number of remote queries that can establish this state:

1. identify the active workflows or equivalent current automation surfaces;
2. retrieve recent runs in bulk when the available API can cover several workflows at once, then keep only the latest relevant completed run for each active workflow;
3. query an individual workflow only when the bulk result does not establish its current state;
4. do not start by enumerating all runs with `failure`, `timed_out`, or other conclusions across repository history;
5. do not fetch jobs, logs, annotations, artifacts, or historical comparison runs for workflows whose current relevant execution is healthy.

Interpret relevance by workflow purpose:

- for normal CI, scheduled maintenance, dependency, security, or default-branch validation, prefer the latest execution in the currently supported/default-branch context;
- for pull-request workflows, consider only open or otherwise currently relevant pull requests;
- for release or publish workflows, the latest supported release/tag execution may remain operationally current even when newer unrelated CI runs exist;
- for workflows replaced, disabled, deleted, or tied only to obsolete branches or closed experiments, do not treat their old failures as current health defects.

If an active workflow has never run, if its latest run is still in progress, or if access is insufficient to determine its state, report that state explicitly instead of treating it as healthy.

## 2. Classify only current problematic executions

A current execution needs diagnosis when its terminal result indicates that the intended automation did not complete successfully. Treat at least these conclusions as problematic when applicable:

- `failure`;
- `timed_out`;
- `action_required`;
- `cancelled` only when cancellation was unexpected or evidence indicates an underlying failure;
- another terminal result that demonstrably leaves the intended automation incomplete.

Successful, neutral, intentionally skipped, or intentionally cancelled executions do not require diagnosis. Historical failures may be consulted only when they are needed to explain a current failure or determine whether it is recurrent.

**Default:** For GitHub-managed automation such as Dependabot or dependency-graph jobs, do not classify a `cancelled` result as a repository-code failure merely because it is terminal. When the available metadata shows that no runner was assigned and no workflow steps executed, classify it as a GitHub-managed infrastructure or scheduling cancellation unless contrary evidence exists. Report it as degraded automation health when it is the latest relevant execution, but do not inspect repository code, propose a repository patch, or fetch deeper logs unless additional evidence points to a repository-controlled cause.

For every current problematic execution, record the repository, workflow/check name, branch/tag/commit, trigger, run date, failing job or step, and the best available root-cause evidence. Do not infer a root cause from the red status alone; inspect jobs, logs, annotations, or structured failure metadata when accessible.

Classify the cause into the narrowest supported category, for example:

- repository code or tests;
- workflow or repository configuration;
- dependency or runtime compatibility;
- permissions or GitHub configuration;
- secret or credential requirement;
- external-service configuration;
- quota, infrastructure, or transient failure;
- uncertain because available evidence is insufficient.

## 3. Decide whether repair is low effort

Classify the likely repair as `small`, `moderate`, `substantial`, or `uncertain`.

A repair is normally `small` only when the failure has a narrow, well-supported cause and can be corrected with a bounded change that has low regression risk, for example:

- a clearly obsolete Actions version or runtime version with an evident supported replacement;
- a broken path, filename, cache key, matrix value, or command caused by a recent local change;
- a deterministic lint, formatting, metadata, or test failure with a small isolated correction;
- a dependency or workflow pin update whose compatibility can be verified with the repository's normal checks;
- a permissions declaration that is demonstrably missing and can be restored with least privilege.

Do not classify a repair as small merely because the diff would be short. Treat it as moderate, substantial, or uncertain when it requires architectural decisions, broad dependency upgrades, secrets or credential changes, external-service configuration, unclear test redesign, large code changes, unsupported runtimes, or a choice between materially different fixes.

**Invariant:** Do not modify repository files to compensate for a failure whose verified cause is external configuration, unavailable credentials, quota, or external infrastructure unless the repository configuration itself is demonstrably wrong. Report the external action required instead.

## 4. Retry policy

A retry must test a supported hypothesis, not merely attempt to turn a red run green.

- A run may be rerun once without repository changes when the evidence reasonably supports a transient, runner, network, GitHub-managed infrastructure, or known flaky-external-dependency explanation and a rerun can distinguish that explanation from a deterministic repository failure.
- Do not repeatedly rerun the same deterministic failure on an unchanged commit. If the evidence already points to code, tests, workflow configuration, permissions, a missing secret, or another stable cause, diagnose or repair that cause instead of retrying first.
- If the one evidence-based transient rerun fails in the same materially relevant way, stop treating blind retry as an adequate remedy. Reassess the cause from the new evidence and do not enter a retry loop.
- After a repository change, the next equivalent run on the new commit is validation of the repair, not a retry of the old commit. Always require fresh equivalent automation evidence for the new SHA before declaring the issue resolved.
- Do not use reruns to bypass required checks, consume excessive CI capacity, or conceal an unresolved reproducible failure.

## 5. Repair small failures when authorized

When the user's request includes repairing failed runs, apply small repairs without asking again if the root cause is sufficiently verified and the required mutation stays within the scope of the failed automation.

For a repair that changes repository files:

1. route to the applicable `code/` module and follow the target repository's local instructions;
2. change only the files necessary to address the demonstrated failure;
3. run the relevant local validation or targeted tests when feasible;
4. update or rerun the remote check when the available workflow and authorization permit it;
5. verify the new run or equivalent current check before marking the failure resolved.

Do not disable, remove, skip, weaken, or mark a failing check as non-blocking merely to make the repository green. Do not delete tests, suppress diagnostics, lower coverage thresholds, relax security rules, or remove supported platforms unless the user explicitly chooses that policy change and the repository context justifies it.

## 6. Escalate non-trivial decisions

When a failure cannot be repaired safely with small effort, do not choose a consequential repair strategy silently. Present the user with the smallest set of realistic options and explain the trade-off of each.

Examples include:

- upgrading or dropping a supported language/runtime version;
- replacing an unmaintained action or external CI service;
- introducing or rotating a secret or credential;
- changing deployment, release, signing, or publishing infrastructure;
- rewriting a brittle test suite or broad workflow architecture;
- accepting a substantial dependency migration;
- intentionally retiring a workflow or leaving it disabled.

If the failed execution is historical and no longer represents the latest relevant state of an active workflow, leave it as historical evidence rather than spending effort fixing an irrelevant commit. If a workflow itself should be retired, require an explicit user decision before disabling or deleting it.

## 7. Recheck after changes

After every repair attempt, inspect the fresh equivalent automation result for the repaired workflow and relevant context. A historical failed run remains historically failed; the success criterion is that the current equivalent workflow/check on the repaired commit, active branch, pull request, release, or supported context passes, or that the user explicitly decided to retire or leave the failure unresolved.

If a rerun fails differently, treat the new failure as new evidence and reassess rather than repeatedly patching symptoms. Stop automatic repair when the scope ceases to be small or the cause becomes uncertain.

Do not rescan historical failures after a successful repair unless the new evidence suggests a broader recurrent problem.

## 8. Final report

Always finish with a concise report grouped by repository. For every current problematic workflow, state:

- what currently fails and in which branch, pull request, release, tag, commit, or workflow context;
- the verified or best-supported cause;
- whether it was repaired, blocked, externally actionable, or requires a user decision;
- what change was made and why, when applicable;
- what fresh validation confirms the result;
- any unresolved options or blockers.

Historical or superseded failures should normally be summarized only as an aggregate or omitted unless they materially explain the current state.

End with aggregate counts when useful, such as repositories inspected, active workflows evaluated, current failed workflows found, failures repaired, external blockers, and failures awaiting a decision.

Do not claim that all repositories are healthy unless the accessible repository set and the latest relevant execution of every active workflow in scope were actually inspected and no unresolved current failures remain.
