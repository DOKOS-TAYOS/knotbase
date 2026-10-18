# Apply selected findings

## Activation and scope

Use this module when the user supplies one or more previously identified findings and asks to fix them without re-running the originating audit or a broader cyclic workflow.

The supplied repository and findings define the complete correction scope. Findings may be supplied as identifiers from the direct conversation context or as complete finding text. Resolve an identifier only when its originating finding is unambiguous from the current direct context or other authoritative supplied evidence. If an identifier cannot be resolved confidently, stop before mutation rather than guessing or re-running a broad audit.

This module is a dispatcher and bounded-correction wrapper. It must reuse the correction contracts already owned by other indexed modules instead of reproducing them here.

## 1. Validate and classify the selected findings

Before changing files, confirm that each selected finding still applies to the repository state being modified. Reproduce the problem, verify the stale or redundant code path, or otherwise establish current evidence appropriate to the finding type. If a finding is stale, already fixed, not reproducible, or contradicted by the current repository state, do not force a change merely because it appeared in an older report.

Classify each selected finding into the narrowest applicable owner:

- bug, defect, error, incorrect behavior, or comparable correctness finding;
- dead, unused, duplicate, redundant, obsolete, or unnecessary code;
- another bounded repository finding.

Do not silently reinterpret an ambiguous finding when that classification would materially change mutation or publication behavior.

## 2. Bug findings: delegate to the existing bug correction contract

For bug or defect findings, load `03_bug_audit.md` and follow its post-inventory correction behavior exactly for the selected findings.

Treat the `#FIX` invocation itself as authorization for one bounded correction batch containing only the selected, still-valid bug findings. The delegated bug workflow begins directly in its post-inventory correction state for that batch.

Reuse the bug module's correction-iteration rules, smallest-robust-change requirement, verification requirements, correction-batch reporting, and remote publication and integration policy. In particular, verified bug corrections follow the routine remote publication and integration behavior defined by `03_bug_audit.md` and its GitHub routing requirements.

If selected bug findings remain after the executed bounded batch, a direct-continuation response consisting only of `ok` authorizes exactly one further bug correction batch under the same post-inventory contract.

## 3. Dead-code findings: delegate to the existing cleanup contract

For dead, unused, duplicate, redundant, obsolete, or unnecessary code findings, load `04_dead_code_audit.md` and follow its post-inventory cleanup behavior exactly for the selected findings.

Treat the `#FIX` invocation itself as authorization for one bounded cleanup batch containing only the selected, still-valid dead-code findings. The delegated dead-code workflow begins directly in its post-inventory cleanup state for that batch.

Reuse the dead-code module's safety checks, correction ordering, verification, reporting, and local-only mutation behavior. Remote publication remains governed by the delegated `#DEAD` contract unless separately authorized, regardless of the outer `#FIX` command's maximum effect class.

If selected dead-code findings remain after the executed bounded batch, a direct-continuation response consisting only of `ok` authorizes exactly one further cleanup batch under the same post-inventory contract.

## 4. Other findings: apply the minimum complete correction

For selected findings not owned by the bug or dead-code workflows, first load another indexed specialized `code/` module when the finding clearly belongs to one. Otherwise use the shared code rules plus this section.

Apply the minimum coherent change that fully resolves the verified finding while keeping the result readable, maintainable, scalable, and efficient. Interpret those qualities through scope discipline rather than speculative redesign:

- modify only files and behavior required by the finding;
- preserve public and observable contracts unless the finding itself demonstrates that a contract must change and that change is authorized;
- prefer existing abstractions and repository patterns over new machinery;
- do not combine the fix with unrelated cleanup, formatting, dependency upgrades, or opportunistic refactoring;
- do not add defensive layers, configuration, abstractions, or generalized infrastructure without evidence they are needed for the finding;
- avoid both knowingly fragile shortcuts and over-engineering: the smallest change must still be robust under realistic supported use;
- verify the affected behavior with the narrowest meaningful reproduction, tests, validators, static checks, or other repository-native evidence.

For these other findings, `#FIX` authorizes the required local repository correction and verification. Remote publication occurs only when the delegated specialized module already authorizes it or when remote publication is separately authorized; do not infer publication merely from the command's maximum effect class.

## 5. Mixed finding sets

When the supplied findings span different delegated contracts, do not merge them into one mutation batch merely for convenience. Partition them by owner and execute only one coherent bounded batch at a time, beginning with the highest-risk or highest-priority actionable findings. Preserve each delegated workflow's publication semantics.

A direct-continuation `ok` authorizes exactly the next remaining bounded batch from the already selected findings. It does not authorize newly discovered or unrelated work.

## 6. Completion report

Use the report layout owned by the delegated correction workflow for the current batch. Include only the selected findings handled in that batch, the files changed, verification actually performed, publication or integration state when applicable, and the identifiers or count of selected findings still pending.
