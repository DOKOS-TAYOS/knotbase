# Repository work triage

## Activation and objective

Use this module when the user asks for `#TRIAGE` over one repository or over the maintained active repository inventory.

**Invariant:** This workflow is strictly read-only. Its purpose is to identify, deduplicate, prioritize, and route actionable repository work to the existing specialized commands. It must not execute delegated commands or mutate local or remote repository state; the user must invoke the recommended command separately.

## Scope

When a repository is supplied, inspect exactly that repository, subject to the GitHub core inventory rules for archived and frozen repositories.

When no repository is supplied, resolve the maintained repository set through `../info_user/repositorios_github.csv` as required by `00_core.md` and exclude archived and frozen entries. Preserve explicit coverage of the resolved set and report repositories or surfaces that could not be inspected.

Do not broaden the scope to repositories outside the maintained inventory merely because they are visible through GitHub search.

## Surfaces to inspect

Inspect only enough current remote evidence to determine whether actionable work exists. Prefer bulk or bounded queries over exhaustive history.

1. Open pull requests that plausibly need review, correction, synchronization, or integration.
2. Current problematic CI or Actions state, using the current-health semantics of `05_failed_ci_runs_review.md`; historical superseded failures are not backlog items.
3. Open Dependabot pull requests and dependency-update work.
4. Accessible repository-security surfaces when supported. Distinguish genuine zero results from disabled, permission-blocked, or unavailable surfaces.
5. Open issues that are sufficiently concrete and actionable to merit implementation or a user decision.
6. Branch or worktree cleanup opportunities only when remote evidence makes them clearly relevant; do not perform local cleanup discovery unless the user later invokes the dedicated cleanup workflow.

Do not turn triage into a code audit, test audit, refactoring audit, performance audit, release audit, or general source inspection. Those activities begin only when the corresponding specialized command is invoked.

## Evidence and deduplication

Treat one underlying problem as one triage item even when it appears on several surfaces. Examples include a pull request whose only blocker is failing CI, a Dependabot pull request that also resolves a security alert, or an issue already represented by an active implementation pull request.

For each item, record only the evidence needed to support prioritization:

- repository;
- current remote object or surface;
- concise problem or opportunity;
- why it is actionable now;
- material blocker or dependency;
- recommended specialized command.

Do not infer severity, exploitability, urgency, or implementation cost without evidence. Mark uncertainty explicitly.

## Prioritization

Rank actionable items primarily by expected value of attention, not by age or raw count. Use these factors in order, adjusting when repository evidence clearly warrants it:

1. Security exposure, leaked credentials, critical vulnerabilities, or other high-consequence risk.
2. Work blocking integration, release, deployment, or the repository's current development path.
3. Current failing required automation or pull requests that are otherwise close to completion.
4. Small, well-bounded dependency or maintenance work with clear value and low decision cost.
5. Actionable issues with a clear specification and no higher-priority blocker.
6. Cleanup or housekeeping that is safe but not blocking current work.

Within a level, prefer items that unblock other work, have clearer evidence, and can be completed with lower technical or decision cost. Do not manufacture numeric priority scores unless the user asks for them.

Classify the resulting queue as `HIGH`, `MEDIUM`, or `LOW`. Use `requires decision` when the next useful step depends on a material user choice rather than execution.

## Delegation

Route each item to the narrowest existing command rather than duplicating its procedure:

- `#PR <repo>; <pull request>` for review and possible integration of one pull request.
- `#CI <repo>; [pull request|branch]` for current failing CI on one repository or target.
- `#DEP [repo]` for Dependabot pull-request review and integration.
- `#SEC [repo]` for repository security review and bounded remediation.
- `#ISSUE <repo>; <issue>` for implementation of one actionable issue.
- `#SYNC <repo>; [branch]` when the primary problem is branch synchronization.
- `#CLEAN [repo]` when clearly finished branches or worktrees are the actionable concern.
- `#RELEASE <repo>; [version]` only when evidence shows that release preparation/publication is the actual next task.

If no registered specialized command precisely covers an item, describe the next action without inventing a command.

## Query discipline

Use the smallest set of queries that can establish current actionable state. Reuse already-fetched metadata across surfaces when it remains current. For multi-repository scope, follow the GitHub core batching and coverage rules and stop further discovery if rate limiting makes complete coverage unsafe.

Do not fetch full logs, complete diffs, issue histories, release notes, or source trees merely to classify an item when summary metadata establishes enough context. Deeper inspection belongs to the delegated workflow.

## Output

Return a concise prioritized queue. For each item state:

- priority;
- repository and object;
- why it matters now;
- blocker or dependency when relevant;
- exact recommended specialized command when one exists.

Finish with a short coverage statement: repositories inspected, material surfaces unavailable or permission-blocked, and whether the queue is complete for the resolved scope.

If no actionable work is found, say so only for the surfaces and repository scope actually verified. Do not equate unavailable access with an empty backlog.
