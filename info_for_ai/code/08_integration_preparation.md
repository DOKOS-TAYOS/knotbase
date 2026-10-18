# Technical preparation for integration

## Activation

Use this module when development work must be technically ready for publication or integration. It covers only local preparation. For push, pull requests, merge, squash, rebase, branch cleanup, and remote verification, route directly to [../github/01_integration_and_publication.md](../github/01_integration_and_publication.md).

This module does not authorize any GitHub mutation. If the request explicitly includes publishing or integrating, also select the GitHub integration module.

## Procedure

1. Check the repository, current branch, uncommitted changes, recent history, and local rules. Do not mix unrelated work into the deliverable.
2. Run the repository's required tests, formatting, lint, type, and build checks.
3. Review the complete diff and confirm that documentation, versions, lockfiles, and changelog are updated when applicable.
4. Split or reorganize changes only when needed to make the local change set coherent and reviewable. Do not rewrite another person's work.
5. Create descriptive local commits when the tool and workflow require them.
6. Hand the prepared state to [../github/01_integration_and_publication.md](../github/01_integration_and_publication.md), which owns all remote decisions and actions.

## Readiness criteria

Before considering a change ready for integration:

- the diff contains only task-related changes;
- every applicable local check has run, or the report states exactly why it could not run;
- no known error introduced by the change remains;
- relevant risks, migrations, and manual steps are identified;
- all pre-existing unrelated work is preserved.

## Boundary

Technical preparation alone does not authorize push, opening or merging a pull request, remote squash or rebase, branch deletion, bypassing protections, or changing CI state. Do not perform or reproduce those workflows here; follow the selected `github/` instruction and the user's explicit authorization.

## Result

Report the local state as `ready for integration`, `blocked by verification`, or `requires technical decision`. If publication or integration is in scope, continue with [../github/01_integration_and_publication.md](../github/01_integration_and_publication.md) rather than treating local readiness as remote completion.
