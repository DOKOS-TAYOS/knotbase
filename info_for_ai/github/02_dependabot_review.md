# Autonomous Dependabot review

## Activation

Use this module when the user asks to review open Dependabot pull requests and automatically accept or integrate the advisable ones.

A request to evaluate and accept suitable Dependabot updates authorizes the review, necessary minor corrections, publication of those corrections, and integration of pull requests that become verified. It does not authorize material migrations or unrelated code changes.

## Scope

Resolve repository identity, archival/frozen exclusions, multi-repository batching, coverage accounting, ambiguous empty results, private-access uncertainty, live-metadata refresh, and rate-limit-safe discovery through `00_core.md` and `repository_inventory_and_scope.md`. This module adds only Dependabot-specific scope rules.

Limit the review to named repositories when the user specifies them. For "my repositories," use the maintained in-scope repository set and search it for open pull requests authored by Dependabot.

For a global routine review, use `dependabot_dias_versiones` from `../info_user/repositorios_github.csv` to select only repositories whose recorded weekly version-update schedule includes either the current local weekday or the immediately preceding local weekday. Process the current-day set first, then the previous-day set; if a repository is scheduled on both days, process it only once in the current-day pass. A repository explicitly supplied by the user is not affected by this schedule filter.

**Invariant:** For a global routine `#DEP` review, that weekday field is a scope criterion for Dependabot version-update discovery. Repositories outside the two-day schedule scope are outside that run; this does not prove they have no already-open pull requests and does not govern security updates. Security-alert review remains owned by [03_security_review.md](03_security_review.md).

Preserve the resolved repository set in Dependabot pull-request discovery. Apply the shared bounded-coverage contract rather than broadening to unscoped GitHub search.

**Default:** When a scheduled or explicit scope contains four or fewer repositories and an available repository-scoped pull-request listing can completely enumerate their open pull requests, query those repositories directly and filter Dependabot authorship from the returned pull requests. Do not first perform a generic multi-repository search whose empty result would then require the same repository-scoped verification. Use generic batched search for larger scopes or when the repository-scoped surface cannot establish the needed state.

**Default:** Process useful discovered pull requests before continuing unnecessary discovery when doing so reduces queries and does not compromise required coverage. Complete the current-day pass before the previous-day pass unless a discovered dependency relationship requires another order.

Distinguish dependency-update pull requests from Dependabot security alerts without pull requests and from other update bots. This module covers Dependabot pull requests. Also use [03_security_review.md](03_security_review.md) for security alerts without a pull request.

## Objective

Autonomously integrate dependency updates that are small, compatible, and verified. Never accept a pull request merely because Dependabot generated it.

## Procedure for each pull request

### 1. Identify

Collect at least the repository and pull-request number, dependency or group, previous and new versions, ecosystem, changed files, approximate update type, relationship to other open Dependabot pull requests, checks/CI, merge state, and conflicts.

### 2. Evaluate technically

Inspect release notes or changelogs whenever compatibility may change. Assess runtime versus development-only impact, supported language and framework versions, relevant peer dependencies, engines, ABI or platform requirements, manifests and lockfiles, unexpected non-dependency changes, deprecations, breaking changes, packaging, build, and the actual environments used by the project.

Do not assume every patch is safe or every major update must be rejected.

### 3. Verify

Inspect available remote checks. When local changes or additional evidence are needed, load `../code/00_core.md` and the relevant code module, then run the repository's applicable tests and ecosystem checks. A green result on a previous SHA does not validate an updated branch.

### 4. Order dependent updates

When several pull requests modify the same manifest or lockfile, determine a safe order. It may be correct to integrate one update, refresh another branch on the new base, resolve a mechanical conflict, rerun CI, and then integrate the next. Do not reject a pull request only because an earlier integration made it outdated.

#### Direct continuation while waiting for CI

**Invariant:** When an already-reviewed Dependabot pull request is waiting only on CI for its refreshed current SHA, preserve that pull request and CI checkpoint as the active continuation state. A direct-continuation message consisting only of `ok` performs exactly one fresh status check of that checkpoint: if CI is still pending, keep the checkpoint active; if it succeeds and no new material blocker exists, resume the already-authorized `#DEP` workflow; if it fails or a new blocker appears, stop at that blocker rather than broadening the task.

### 5. Classify

#### A. Directly integrable

Use when the change is reasonably compatible, the diff is expected, required CI passes, and there is no material regression signal. Integrate with the repository's established method.

#### B. Integrable after a minor adjustment

Use when the correction is small, localized, and evident, such as a mechanical lockfile refresh, minimal API adaptation, lint or type fix, small configuration adjustment, outdated-branch refresh, or trivial conflict resolution. Apply the relevant `code/` module, verify the current SHA, and integrate only when correct.

#### C. Do not integrate automatically

Stop when the update requires a major migration, architectural redesign, extensive API replacement, material behavior change, broad configuration change, product decision, feature removal, substantial research without enough evidence, or acceptance of degradation or risk. Explain why and what intervention is required.

### 6. Integrate A and B

Confirm the branch is mergeable, verify required checks on the current SHA, integrate with the established method, confirm the default branch contains the change, and preserve all unrelated work under the shared GitHub protections.

## Special criteria

- **Major versions:** a major update may be integrated when breaking changes have been reviewed, relevant tests pass, the repository is already compatible, and no material migration is required.
- **Development tools:** Ruff, linters, formatters, type checkers, and build tools may change outputs without affecting runtime. Run the new tool and inspect any generated diff.
- **Runtime and frameworks:** require stronger evidence for runtime dependencies, frameworks, Electron, databases, serialization, or networking than for auxiliary dependencies.
- **Grouped pull requests:** evaluate the group as a unit and inspect failures before attributing them to one dependency.

## Output

**Default:** Present the operational result grouped by status:

1. **Integradas y mergeadas**: integrated or freshly verified merged pull requests, with dependency/version change and relevant verification.
2. **PR pero pendiente de mergear**: valid candidates blocked by current-SHA CI, rebase, conflict, review, or dependency ordering.
3. **Pendientes**: unresolved work inside scope, including coverage or access gaps reported under the shared inventory contract.
4. **Rechazados**: updates not suitable for automatic integration, with the concrete reason and decision or work required.

For schedule-aware global reviews, add a brief closing sentence stating whether both schedule passes completed over the selected maintained scope.
