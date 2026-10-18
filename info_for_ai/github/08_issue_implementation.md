# GitHub issue implementation

## Activation and scope

Use this module when the user asks to analyze and implement one specific GitHub issue through a reviewable repository change.

The supplied repository and issue define the complete task scope. This module owns issue interpretation, orchestration of the bounded implementation, pull-request linkage, and the issue-resolution gate. Reuse the existing specialized workflows instead of duplicating them: load the `code/` core and index for local implementation, use `../code/08_integration_preparation.md` for local readiness, `01_integration_and_publication.md` for publication and integration, and `05_failed_ci_runs_review.md` for failing CI when needed.

**Invariant:** Load those dependencies only at their owning phase. Do not load the `code/` domain during issue-state inspection or outcome interpretation; load it when phase 4 begins. Do not load `../code/08_integration_preparation.md` until the issue implementation is ready for local-readiness review, do not load `01_integration_and_publication.md` until publication begins, and do not load `05_failed_ci_runs_review.md` unless relevant CI actually fails.

Do not broaden one issue into a repository-wide audit, backlog cleanup, unrelated refactor, or opportunistic feature work.

## 1. Establish the authoritative issue state

Before changing anything, inspect enough current evidence to establish:

- the exact issue number, title, body, state, labels, and relevant discussion;
- explicit acceptance criteria, reproduction details, linked designs, referenced files, or other authoritative constraints;
- linked or existing pull requests and branches that may already be implementing the issue;
- the repository's current default branch, protections, contribution rules, and local instructions;
- whether the issue is already resolved, superseded, duplicated, or otherwise no longer actionable.

If the issue is closed, do not reopen it automatically. Determine whether the requested implementation is already present or whether a new user decision is required.

## 2. Interpret the requested outcome

Treat the issue body and its material follow-up discussion as the primary task specification, subject to higher-precedence repository contracts and the user's explicit instructions.

Translate the issue into the smallest coherent implementation target and identify the validation evidence that would demonstrate completion. Preserve stated acceptance criteria exactly when they are compatible with repository contracts.

Proceed without clarification when one technically reasonable implementation is well supported by the issue and repository evidence. Stop and request a decision when material ambiguity remains about public behavior, architecture, compatibility, data migration, security policy, ownership, or another consequential contract.

Do not invent acceptance criteria merely to make the issue easier to close.

## 3. Select or create the work branch

Reuse an existing issue branch or pull request when it is clearly the active implementation path and can be continued safely.

Otherwise create a dedicated work branch from the current intended base. Keep unrelated local or remote work out of the branch.

If an existing branch is stale, synchronize it under the standalone work-branch synchronization policy in `01_integration_and_publication.md` before continuing when repository policy or merge readiness requires it.

## 4. Implement the issue locally

Load `../code/00_core.md` and `../code/indice_code.csv` before local implementation. Select only the indexed code module or modules whose responsibilities actually match the issue. When no specialized code module matches a necessary implementation responsibility, follow the code core and target-repository rules directly rather than forcing the work through an unrelated audit workflow.

Implementation rules:

1. Change only what is required to satisfy the issue and its established acceptance criteria.
2. Preserve existing public contracts unless the issue explicitly and authoritatively changes them.
3. Add or update tests when the behavior or contract being implemented warrants protection.
4. Update documentation, examples, generated files, schemas, or migrations only when the implementation makes them necessary.
5. Do not silently fold unrelated defects or cleanup into the issue branch.
6. Review the complete issue diff before publication.

Use `../code/08_integration_preparation.md` to obtain local readiness before remote publication.

## 5. Publish the implementation through a pull request

Load and follow `01_integration_and_publication.md` for push, pull-request creation or reuse, checks, and integration.

The pull request must identify the issue and summarize how the implementation satisfies its material acceptance criteria. Use an automatic closing keyword such as `Closes #<issue>` only when the pull request is intended to resolve the complete issue. For partial implementations, reference the issue without a closing keyword and keep the issue open.

Do not create a second pull request when an existing active pull request already represents the same implementation branch.

## 6. CI and correction loop

Required or materially relevant checks must validate the current pull-request head SHA. Checks from an older SHA do not establish completion.

If CI fails, use `05_failed_ci_runs_review.md`. Apply only repairs authorized by that workflow or corrections that are already unambiguously part of the issue implementation. After any branch change, require fresh equivalent verification.

Stop when a failure requires a material unrelated repair, a secret or external permission, a policy change, or another decision outside the issue's established scope.

## 7. Issue-resolution gate

Do not close the issue merely because code was written, a branch was pushed, or a pull request exists.

Treat the issue as resolved only when all of the following are true:

- the implemented behavior satisfies the material issue specification and acceptance criteria;
- the final integrated diff contains no unresolved material issue-scoped finding;
- required checks and repository protections are satisfied for the integrated change;
- the change is present on the intended base branch, or the repository's documented equivalent completion state is verified;
- no known required follow-up remains that would make claiming resolution misleading.

When the pull request is merged and an authorized closing keyword closes the issue automatically, verify the resulting issue state. If automatic closure was not used, close the issue manually only after the same resolution gate is satisfied and the command authorization permits it.

If review, protections, CI, permissions, or a material decision prevent integration, leave the pull request and issue open and report the blocker precisely.

## 8. Final verification and result

Freshly verify the final pull-request state, integrated commit or change, relevant checks, and issue state before reporting success.

Report one of:

- `implemented and issue closed`;
- `implemented and merged; issue remains open for documented follow-up`;
- `pull request ready; awaiting review or required checks`;
- `blocked by issue ambiguity`;
- `blocked by verification, permissions, or protections`.

Include the issue and pull-request references and summarize only the material verification evidence and remaining blockers.
