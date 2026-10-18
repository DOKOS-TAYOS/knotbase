# Safe branch and worktree cleanup

## Activation

Use this module when the user asks to find unnecessary branches, remove branches whose work is integrated, or clean worktrees.

The request authorizes deletion only for branches and worktrees demonstrably finished. It does not authorize discarding unique work, uncommitted changes, or branches whose relationship to the default branch is ambiguous.

## Objective

Remove residue from completed work without losing commits, local changes, or branches that still contain useful work.

## Initial inspection

For each repository, identify the actual default branch, fetch and refresh relevant remote references, enumerate local and relevant remote branches, enumerate worktrees using stable machine-readable output, find associated open, closed, and merged pull requests where possible, and detect commits exclusive to each branch. Never use a branch name alone as deletion evidence. Treat an exclusive commit SHA as evidence to investigate, not as proof of unique effective work: squash, rebase, cherry-pick, and consolidation can preserve the change under different history.

## Branch classification

### A. Safe to delete

Deletion is safe only when evidence shows that the branch contributes no remaining unique effective work. That can be established when the work is incorporated into the default branch by ancestry, when its own pull request is merged and equivalent content is present, or when the work was carried through another merged consolidation or integration pull request and the branch's effective changes are present or superseded in the default branch. The branch may still contain commit SHAs absent from the default branch after squash, rebase, cherry-pick, or consolidation; those exclusive SHAs are not a deletion veto once content or effect equivalence is proven.

The branch must also have no uncommitted work in any worktree; it must not be protected, the default branch, or an active required branch; and it must not be the base of another active pull request.

Use the strongest practical equivalence evidence for the case: whole-tree equality, equality of the changed file blobs, patch or diff equivalence, a reviewed merged pull request containing the same effective changes, or a historical integration point followed by later default-branch evolution that clearly retains or supersedes the branch change. Exact current blob equality is sufficient when present but is not required after later evolution.

For squash, rebase, cherry-pick, or consolidation, do not rely only on `git branch --merged` or on original commit ancestry. Verify the integration path and effective content instead.

### B. Potentially obsolete but unproven

Do not preserve or delete a branch solely from commit ancestry. Commits absent from the base require equivalence investigation. Preserve the branch when it has an open pull request, a worktree containing changes, effective branch-only content whose integration or supersession cannot be proven, uncertain squash/rebase/cherry-pick/consolidation status, or divergence whose purpose remains unclear. Report the unresolved evidence.

### C. Clearly active

Keep a branch with an open pull request, active worktree, recent unintegrated work, or use as a base for subsequent work.

## Local cleanup

For each category-A branch, confirm it is not checked out, remove a completed associated worktree first, and use the normal safe deletion mechanism. Do not force deletion to hide unverified exclusive commits. If `git branch -d` rejects a branch known to have been squash-merged, verify the pull request and content equivalence explicitly before considering `-D`.

## Remote cleanup

Delete a remote branch only when it is integrated or superseded, unprotected, not needed by an open pull request, within the user's permissions, and contains no unique work. Prune stale local references afterward. Age alone is never sufficient evidence.

## Worktrees

Use parseable inspection such as `git worktree list --porcelain` when using Git CLI. A worktree may be removed only when it is not the main worktree, belongs to a finished task, is clean, its branch is integrated or the worktree is demonstrably disposable, and it is not locked for a valid reason.

Use Git's worktree-removal mechanism for an existing worktree; do not manually delete its directory as the first approach. Preserve and report any worktree with modified or relevant untracked files, unpublished commits, an unintegrated branch, unclear ownership, or evidence that another agent is using it.

When the directory is already absent and Git marks the metadata as prunable, use `git worktree prune` or its equivalent. Do not force removal of a dirty or locked worktree without explicit authorization to discard its contents.

## Recommended order

1. Fetch and refresh references.
2. Inventory branches and worktrees.
3. Identify pull requests, exclusive commits, and content equivalence.
4. Remove finished worktrees.
5. Delete safe local branches.
6. Delete safe remote branches.
7. Prune stale references and worktree metadata.
8. Enumerate again and verify the final state.

## Special cases

- **Squash merge:** Git ancestry may show the branch as unmerged; verify remote pull-request state and effective content.
- **Rebase or cherry-pick:** changed or exclusive SHAs do not alone prove unique work; compare effective content and pull-request evidence.
- **Consolidation branch or pull request:** a source branch may have no merged pull request of its own and still be fully integrated through another branch or pull request. Trace that integration path and verify that the source branch contributes no remaining unique effective change.
- **Later evolution after integration:** when the default branch later changes the same files, establish equivalence at the historical integration point or merged pull request, then verify that later default-branch history retains or supersedes the integrated change. Do not require current blob equality when the later evolution explains the difference.
- **Remote branch gone but local branch remains:** local deletion is safe only when no unique effective work remains and the task is finished.
- **Worktree used by another agent:** preserve it whenever activity or changes cannot be confidently attributed.

## Output

List deleted local and remote branches and removed worktrees with their evidence of integration. List every preserved ambiguous or active item with the reason. If nothing is safe to clean, report that and make no destructive change.
