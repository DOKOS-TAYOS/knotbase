# Change integration and publication

## Activation

Use this module when the user asks to upload or push code, integrate a branch, synchronize a work branch with its base, open or merge a pull request, squash, rebase, or leave changes incorporated into the default branch.

Authorization to publish, integrate, merge, push, synchronize, or equivalent permits the routine steps necessary for that outcome, subject to the shared protections in `00_core.md`. If local code must change, load `../code/00_core.md` and the one relevant code module; for local readiness before handoff, use [../code/08_integration_preparation.md](../code/08_integration_preparation.md).

## Objective

Publish, synchronize, or integrate the requested change with coherent history and valid CI, then verify the final remote state before reporting success.

## Procedure

### 1. Inspect

Determine the repository and primary remote, actual default branch, current branch and upstream, uncommitted changes, unpublished local commits, work-branch differences from base, an existing pull request for the branch, checks, reviews, protections, and allowed merge methods.

Do not assume the correct flow is always `push -> pull request -> merge`; choose it from the actual state.

### 2. Obtain local readiness

If the task includes local changes, use `../code/08_integration_preparation.md` to prepare and verify them. Do not duplicate its local quality workflow here and do not include unrelated files or modifications.

### 3. Choose the flow

#### Unpublished local work branch

By default:

1. synchronize the base;
2. publish the branch;
3. open or reuse a pull request;
4. wait for or inspect required checks;
5. integrate with an allowed method;
6. verify the default branch.

#### Existing open pull request

Do not open another. Update the existing pull request if needed, inspect its checks, and continue from it.

#### Standalone work-branch synchronization

Use this flow when the requested outcome is only to bring one work branch up to date with its base and leave it ready for continued work or review.

1. Resolve the exact work branch and its intended base from the pull request, branch configuration, repository convention, or explicit user input. Do not guess a base when several plausible targets exist.
2. Refresh both refs and compare their current heads before changing history.
3. Preserve uncommitted or unpublished unrelated work. Stop rather than switching, rebasing, resetting, or rewriting over ambiguous local state.
4. Choose the repository's established update strategy when documented or mechanically implied by the active pull-request workflow.
5. If no repository-specific strategy is established, prefer a non-rewriting merge of the base into a branch that is already published or shared. Prefer rebase only for a private or clearly rewrite-safe work branch when linear history is the repository convention or the user explicitly requests rebase. Apply the shared history-rewrite protections in `00_core.md`; Never force-push merely to make synchronization succeed.
6. Resolve only trivial conflicts whose correct result is mechanically evident from the surrounding code and repository contracts.
7. Stop on semantic conflicts with more than one materially reasonable resolution, including competing behavior, public API/schema choices, deletion-versus-modification, incompatible dependency/generated-file outcomes, uncertain test expectations, or security/policy choices.
8. After synchronization, run checks materially affected by the update when repository policy or conflict resolution requires them.
9. If publication is authorized, publish through the normal safe path and verify the remote branch head. A changed head invalidates earlier CI evidence.

A standalone synchronization is complete when the work branch contains the intended current base history, no unresolved conflict remains, task-related checks are satisfactory or precisely reported, and the intended local or remote branch head is freshly verified.

#### Change already merged locally

If repository policy permits updating the default branch this way without bypassing protections, verify the history before publishing. Use a pull request when policy requires one.

#### Direct push to the default branch

Use it only when repository policy permits it. Never use direct push to avoid required reviews or checks.

## Select the integration method

Follow repository configuration and policy first.

### Squash merge

Prefer it when the branch contains intermediate commits without lasting historical value, the repository keeps one logical commit per pull request, or a compact linear history is intended. Before squashing, ensure the final title and message accurately describe the complete change.

### Merge commit

Use it when the repository explicitly preserves commit structure or expects this method.

### Rebase merge

Use it when a linear history retaining individual commits is required and permitted.

Do not arbitrarily change the project's established strategy.

## Outdated branch

When the pull request must be current with its base, use the standalone synchronization policy above, rerun relevant checks on the updated head, and continue integration only after the applicable merge-readiness requirements are satisfied.

**Invariant:** Before integration, refresh the current default branch. If it advanced since the task branch diverged and base-side and task-side changes touch any of the same files, do not integrate the stale result directly. Reapply the task changes onto the current base, rerun relevant validation, and review the final diff against that current base.

## CI failures

If checks fail because of the change, investigate the failure, make only minor in-scope corrections through the relevant `code/` module, publish the correction, and recheck CI. If a failure is external, intermittent, or pre-existing, document the evidence and follow repository policy rather than misreporting it as passing.

## Post-integration verification

After integration:

1. confirm the pull request is shown as merged or the remote push exists;
2. confirm the default branch contains the expected commit or change;
3. inspect relevant post-integration checks when present;
4. delete the work branch only if it contains no unique work and policy permits deletion.

## Integration-specific boundaries

In addition to the shared protections in `00_core.md`, do not choose a semantic conflict resolution without authoritative evidence, include unrelated changes, or delete a branch with unintegrated exclusive commits.

## Result

Report the final state precisely, for example `pushed`, `pull request opened`, `merged`, `squash-merged`, `branch synchronized`, `updated and awaiting CI`, `blocked by protection`, or `blocked by semantic conflict`. Include the pull-request link when relevant and a brief summary of completed verification.
