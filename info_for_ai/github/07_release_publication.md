# Release publication

## Activation and scope

Use this module when a prepared repository version must be published as a release through GitHub. Load `00_core.md` first. If release-specific local files still need to be changed, also load `../code/00_core.md`, [../code/11_release_preparation.md](../code/11_release_preparation.md), and [../code/08_integration_preparation.md](../code/08_integration_preparation.md).

This workflow owns publication of the prepared release commit, CI gating, bounded release-blocking corrections, creation and publication of the exact release tag, GitHub Release creation when available, and final verification.

## 1. Establish publication state

Before mutation, determine the target repository, primary remote, actual default branch, current branch and upstream, worktree state, prepared release version `V`, current release-related commit or branch, existing pull requests, applicable repository protections, allowed integration methods, existing tags and releases for `V`, and the release-relevant workflows or checks.

**Invariant:** The version written in the repository is authoritative for the tag created by this workflow. The exact tag name must be the repository's established tag representation of `V`. Do not create a tag whose version disagrees with the prepared release files.

If a conflicting tag or release already exists, do not overwrite, move, recreate, or delete it automatically. Stop and report the conflict unless it is demonstrably the same already-completed release state.

## 2. Publish the prepared release changes

Use [01_integration_and_publication.md](01_integration_and_publication.md) for normal branch, push, pull-request, and integration mechanics. Publish all and only the prepared release-related changes and leave them integrated in the repository's intended release branch or default branch before tagging unless repository policy explicitly requires another release point.

Do not create the release tag from an unintegrated work branch merely to avoid the repository's normal checks or review flow.

## 3. Require fresh release-relevant automation

After the release changes are on the intended remote commit, inspect the relevant CI, integration, build, packaging, publication-dry-run, or other release-gating automation for that exact commit.

Use [05_failed_ci_runs_review.md](05_failed_ci_runs_review.md) for diagnosis and bounded repair behavior. A check or run from an older SHA does not validate the release commit.

Proceed to tagging only when every required or materially release-relevant check for the current release commit has completed successfully, or when a non-success result is verified as intentionally neutral or irrelevant under repository policy. Do not tag while a required or materially release-relevant run is pending, failing, or unverifiable.

## 4. Repair only small release blockers automatically

When fresh automation exposes a small, well-supported defect caused by the release preparation, apply the smallest correction needed under the applicable `code/` instructions, publish it through the normal integration flow, and require fresh equivalent automation on the new commit.

Examples include a missed version assertion, generated metadata that legitimately embeds the version, a deterministic packaging metadata mismatch, or a changelog formatting error.

**Invariant:** Any correction made before the release tag is created belongs to release `V`. When it warrants changelog documentation, record it in the `V` release section rather than the next unreleased area.

Do not automatically resolve moderate, substantial, uncertain, secret-dependent, policy-changing, externally configured, or semantically consequential failures. Stop and report the required decision or external action.

After every repository change, re-establish the exact release version from the repository and verify that all applicable release-facing locations still agree before continuing.

## 5. Create and publish the exact tag

Only after the final release commit is settled and its required release-relevant checks pass:

1. identify the exact commit that contains the released files;
2. derive the tag name from the repository's established tag convention and canonical version `V`;
3. create the tag pointing exactly to that commit;
4. prefer an annotated tag when the repository convention or available tooling supports it; use a concise release summary based on the `V` changelog section as the annotation when useful;
5. publish the tag to the primary remote;
6. verify remotely that the tag resolves to the intended release commit.

Never move an existing published tag to a different commit automatically. Never tag a commit that lacks the exact version represented by the tag.

## 6. Create a GitHub Release when possible

After the tag is remotely verified and the release commit is settled, create a GitHub Release for that tag when the repository and available permissions or tooling support releases.

By default:

- use the canonical tag name or established project convention as the release name;
- derive the body from the changelog section for `V`, editing only as needed for concise release notes and valid Markdown;
- do not invent changes, compatibility claims, migration notes, binaries, checksums, or artifacts;
- attach or publish release artifacts only when the repository's documented release process produces and verifies them.

If GitHub Release creation is unavailable but the tag was published successfully, report the tag as published and the release object as `not created: unavailable with current access`; do not misrepresent that as full release-object publication.

## 7. Final verification

Do not declare completion until you freshly verify all applicable final state:

1. the release changes are present on the intended integrated branch;
2. the final repository version is exactly `V` in every applicable authoritative or release-facing location;
3. the changelog contains the correct release section for `V` and the repository's next unreleased area when expected;
4. relevant checks for the final release commit pass;
5. the remote tag exists and resolves exactly to the final release commit;
6. the GitHub Release exists for that tag when creation was possible and authorized;
7. any release artifacts or post-tag workflows required by repository policy are successful or explicitly classified if externally blocked.

Classify the result as `verified release`, `verified tag only`, `blocked before tag`, `blocked after tag`, or `requires human decision`.

## Release-specific boundaries

In addition to the shared GitHub protections in `00_core.md`, do not move or overwrite a published release tag, change versioning policy silently, or fabricate release notes or artifact publication.

## Result

Report the exact released version, final commit, tag, GitHub Release state, release-relevant CI result, any bounded corrections made, and any remaining blocker or externally required action.
