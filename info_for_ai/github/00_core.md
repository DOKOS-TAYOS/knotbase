# Shared rules for remote GitHub work

## Activation and boundary

Read this file before using any instruction in `github/`. Select only the specialized module whose activation condition matches the request.

This domain owns remote GitHub state and operations: pull requests, push and merge, Dependabot, security surfaces, remote branches, worktrees, and publication. If remote work requires local code changes, also load `../code/00_core.md` and only the code module needed for those changes. Do not repeat generic local code-quality procedures here.

When work concerns the user's own GitHub repositories and either the exact repository must be located or selected, the task spans multiple or all repositories, or the selected workflow performs repository-maintenance operations whose scope depends on archival/development status, also load `repository_inventory_and_scope.md` before repository discovery or mutation.

## Identification and scope

1. Identify the exact repository or repository set in scope.
2. Before any mutation, determine the owner, primary remote, actual default branch, current branch, Git state, associated pull requests, and repository rules.
3. Interpret "my repositories" as the user's or accessible organization's repositories, but limit actions to the operation requested.
4. Do not mix unrelated local, remote, or other-task changes into the operation.
5. Before moving, deleting, switching, or rewriting anything, determine the owner and purpose of uncommitted changes and active worktrees.

## Authorization and protections

Apply this precedence:

1. The user's explicit request.
2. Target-repository rules and protections.
3. The selected `github/` instruction.
4. General operating preferences.

Explicit authorization to publish, integrate, close, resolve, or clean permits the routine remote steps needed for that outcome. It does not permit unrelated mutations, disclosure of sensitive data, or bypassing safeguards.

Never disable branch protection, rulesets, required checks, mandatory reviews, signatures, merge queues, or other safeguards. Never force-push or rewrite shared remote history unless it is necessary, safe, and clearly within the authorized scope. Never delete a branch or worktree that contains unique or unverified work, and never silence a security alert by misclassifying it.

## Tools and sensitive data

- Prefer a structured GitHub integration for pull requests, issues, checks, metadata, and remote operations when available.
- **Invariant:** Reuse an already available capability when it is sufficient. Do not perform tool or capability discovery for an operation that an already loaded or available capability can complete. When tool discovery is necessary, discover only the specific missing operation, or retry discovery only after an available capability has failed because of a concrete capability limitation. Query narrowly for that operation and do not load broad tool catalogs or unrelated schemas.
- Use `gh` for GitHub CLI, Actions, authenticated queries, or official API operations; use `git` for history, commits, diffs, remotes, branches, and worktrees.
- If the primary tool does not expose a relevant capability, try another authorized surface before concluding that the resource does not exist.
- **Invariant:** For remote repository files, prefer bounded line-range reads for large text files and use the same bounded strategy whenever a text file may be large. If a full-content read is truncated, do not request the same file in full again during the same task; continue with bounded ranges, or obtain exactly one reusable complete copy through a capability that can return the whole file when complete content is genuinely required.
- **Invariant:** Treat non-text repository assets as binary from their format, extension, or metadata. Do not attempt a UTF-8 text/blob read for a resource already known to be binary, including XLSX, images, archives, and PDFs; use metadata, a binary-aware download, or a format-specific reader instead.
- Never expose tokens, secrets, authorization headers, or sensitive values in commands, logs, or responses.

## Verification and permissions

Before mutating GitHub or history, refresh remote information when needed, confirm the actual default branch, inspect the diff and exclusive commits, check relevant pull requests and merge state, and identify allowed merge methods and required checks. A check on an old SHA does not validate a changed branch; recheck applicable CI after the SHA changes.

Do not declare success until the final remote state is freshly verified. Depending on the task, verify that the expected commit is on the default branch, the pull request is merged, required checks pass on the current SHA, the branch or worktree is gone, or the alert has a justified resolution.

Classify the result as `verified`, `probable but not verifiable with available access`, `blocked by permissions or protections`, or `requires human decision`.

A `403`, `404`, empty result, or unavailable tool function does not prove that a private resource is absent. Determine whether authentication, permissions, a disabled feature, a tool limitation, or genuine absence is the likely cause; try another authorized surface when useful; and report exactly what was and was not inspected.

## Output

Keep the final response concise and actionable: repositories or pull requests inspected, actions taken, checks verified, blockers or pending work, and any local code changes. Include useful pull-request or alert links when available.
