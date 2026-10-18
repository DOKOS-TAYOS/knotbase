# Release preparation

## Activation and boundary

Use this module when a repository is being prepared for a concrete release before any release tag is created. It owns selection of one exact release version and synchronization of release-facing local files. Remote publication, CI gating, tags, GitHub Releases, and post-release verification belong to [../github/07_release_publication.md](../github/07_release_publication.md).

**Invariant:** Keep release execution staged. Do not load the GitHub domain or its release, integration, or CI modules while local release preparation is still in progress. After the release-specific edits are complete, load and follow [08_integration_preparation.md](08_integration_preparation.md) for normal local readiness checks; only after that local gate succeeds hand the prepared state to [../github/07_release_publication.md](../github/07_release_publication.md), which owns later GitHub dependencies.

This module does not authorize remote mutation by itself.

## 1. Establish the exact release version

Inspect the target repository's local instructions, current version source or sources, changelog structure, package metadata, release documentation, existing tags, and any established versioning convention that materially affects the release.

Resolve one canonical release version `V`:

- when the user supplied a version, validate it against the repository's version scheme and current release history before editing;
- when the version is omitted, derive the next version only when repository policy, an explicit pending version, or another deterministic convention makes the answer unambiguous;
- if choosing between patch, minor, major, prerelease, or another materially different version would require judgment not fixed by the repository, stop before mutation and request that decision;
- do not reuse a version that already identifies a different release or tag.

**Invariant:** The release must have one exact canonical version. Do not silently add or remove prefixes such as `v`, normalize away prerelease/build identifiers, or allow different release-facing files to describe different versions.

## 2. Synchronize every applicable version location

Update the smallest complete set of release-facing files required by the repository. Inspect at least the following when they exist or are relevant:

- `pyproject.toml` and other authoritative package or project metadata;
- source-level version constants such as `__version__`, generated version modules, CLI version output, or equivalent program metadata;
- README text, badges, installation examples, or compatibility statements that intentionally state the current project version;
- tests, fixtures, snapshots, or expected outputs that intentionally assert the current version;
- lockfiles or generated metadata only when the repository's normal tooling embeds the project version and can update them reproducibly.

Use targeted repository search for the old version and known version identifiers when needed to find additional release-facing locations. Do not mechanically replace unrelated dependency versions, historical examples, old changelog entries, citations, dates, protocol numbers, or arbitrary matching text.

When the project uses dynamic SCM-derived versioning or another single source of truth, preserve that design. Do not create duplicated version declarations merely to satisfy this checklist.

## 3. Transition the changelog

When the repository uses an `Unreleased` section or equivalent pending-release section:

1. preserve the accumulated pending entries;
2. move or rename those entries into the release section for `V`, following the repository's established heading and date format;
3. create a fresh empty `Unreleased` section above the newly released section for subsequent development;
4. keep the release section for `V` as the source for release notes unless repository policy defines another canonical source.

Do not rewrite historical release sections or invent changelog entries for work that is not evidenced by the repository.

**Invariant:** If small release-blocking corrections are made after the initial release-preparation changes have already been published but before the tag is created, any changelog entry for those corrections belongs in the current release section for `V`, not in the new `Unreleased` section.

If the repository uses a different changelog convention, preserve its established semantics while achieving the same state: the content being released is attributable to `V`, and a distinct location remains for future unreleased work.

## 4. Validate local coherence

Before remote publication:

1. verify that every applicable release-facing version location agrees with `V`;
2. verify that the changelog contains the release section for `V` and the next unreleased area required by repository convention;
3. run the repository's release-relevant tests, formatting, lint, type, build, package, and documentation checks as required by local instructions;
4. load and follow [08_integration_preparation.md](08_integration_preparation.md) for final local readiness and diff review;
5. preserve unrelated work and do not fold unrelated cleanup into the release.

A failing check may justify only a bounded correction whose cause is understood. Do not weaken tests or change intended behavior merely to make the release pass.

## Result

Hand off exactly one prepared release version `V` and the verified task-related change set to [../github/07_release_publication.md](../github/07_release_publication.md). Report local preparation as `ready for release publication`, `blocked by version decision`, or `blocked by verification`.