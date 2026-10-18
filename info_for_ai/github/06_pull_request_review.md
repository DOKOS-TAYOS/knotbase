# Pull-request review

## Activation and scope

Use this module when the user asks to review a specific pull request and decide whether it can be corrected and integrated safely.

The supplied repository and pull request define the complete remote scope. Review the pull request at its current head SHA. Do not broaden the task into a repository-wide audit or include unrelated branch work.

This module owns pull-request review, bounded correction decisions, and the merge-readiness verdict. Reuse the existing specialized modules instead of duplicating their procedures: use `05_failed_ci_runs_review.md` for failing CI or checks, the applicable `code/` module for code corrections, and `01_integration_and_publication.md` for publication and integration.

## 1. Establish the current pull-request state

Before deciding anything, inspect enough current evidence to establish:

- pull-request intent, base branch, head branch, and current head SHA;
- the complete changed-file diff relevant to the current head;
- current review submissions and unresolved material review threads when accessible;
- required and relevant checks for the current head SHA;
- repository protections, contribution instructions, and target-repository instructions that govern integration.

Do not treat reviews or successful checks from an older head SHA as evidence that the current head is ready.

## 2. Review the change

Review for correctness, regressions, scope discipline, compatibility, tests, documentation when materially affected, security implications, and repository-specific quality requirements.

Classify every material issue as one of:

- `clear`: the issue and the smallest safe correction are well supported;
- `requires decision`: more than one materially different solution is reasonable, a contract or architecture decision is involved, or the intended behavior is ambiguous;
- `blocked`: permissions, secrets, external configuration, protections, unavailable evidence, or another external condition prevents safe completion.

Do not manufacture findings to justify changes. Prefer leaving correct code unchanged.

## 3. Apply only small unambiguous corrections

When the command authorization permits mutation, a `clear` issue may be corrected on the pull-request branch only when all of the following hold:

1. the correction is small, directly in scope, and has low regression risk;
2. the intended behavior is established by the pull request, repository contracts, tests, or other authoritative evidence;
3. the branch is writable under repository policy;
4. the correction can be verified with appropriate targeted checks;
5. no unrelated cleanup, refactoring, dependency work, or redesign is required.

Route the correction through the applicable `code/` instructions. If the correction corresponds to previously identified findings, use the indexed finding-application workflow rather than re-running a broad audit.

Stop before changing the branch when the repair is moderate, substantial, uncertain, architectural, changes a public contract materially, or requires a consequential policy choice.

## 4. Handle CI without duplicating CI logic

When current checks fail, load and follow `05_failed_ci_runs_review.md` scoped to this pull request and its current head. Do not implement an independent retry or CI-repair policy here.

After any branch change, discard older check conclusions for merge-readiness purposes and require fresh equivalent checks on the new head SHA.

## 5. Merge-readiness gate

A pull request may be integrated only when all of the following are true for the current head SHA:

- the pull-request intent is sufficiently clear;
- no material review finding remains unresolved;
- no material review thread remains unresolved when repository policy or the substance of the thread makes it blocking;
- required checks pass, or repository policy explicitly establishes an equivalent acceptable state;
- approvals, branch protections, permissions, and other repository requirements are satisfied;
- the diff contains no unrelated or unreviewable changes;
- integration does not require a material unresolved decision.

When this gate is satisfied, load and follow `01_integration_and_publication.md` for the actual integration operation and final remote-state verification.

When an isolated pull request is safe but merge risk remains material, leave the pull request open and report the blocker. Never bypass protections, dismiss a material review concern merely to merge, weaken checks, or merge an unverified new head.

## 6. Final report

Report concisely:

- the reviewed pull request and head SHA;
- material findings and any bounded corrections applied;
- the fresh verification state;
- whether the pull request was merged, left open as reviewable, or blocked;
- any concrete decision or external action still required.
