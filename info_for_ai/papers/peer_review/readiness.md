# Peer-review resubmission readiness

## Activation

Load this module after reviewer-driven changes when the task is to identify newly introduced weaknesses or decide whether the manuscript is ready for resubmission.

Use the parent `../01_peer_review_response.md` workflow for shared evidence, repository, and artifact requirements.

## Review newly introduced weaknesses

Inspect the manuscript and optional code repository for only weaknesses that are highly recommended to solve before resubmission, with special attention to new inconsistency, unsupported wording, reproducibility gaps, invalidated results, and mismatch between manuscript and code evidence.

Do not conduct a generic perfectionist audit. For every finding, give the concrete evidence and location, why it can materially weaken the revised submission, the smallest focused corrective action, and whether it blocks resubmission or is an explicit caveat.

## Final resubmission readiness review

Check the TeX and optional code repositories against the reviewer comments, agreed responses, current commits, response-letter draft, visual diff, generated artifacts, and applicable compilation/test/experiment results.

Report exactly one verdict:

- **Ready:** no known blocking mismatch remains.
- **Ready with stated caveats:** no blocking mismatch remains, but list the explicit caveats that must be preserved in the response or submission.
- **Not ready:** list only concrete blocking actions, evidence gaps, or contradictions.

Do not mark readiness from intent alone. Confirm that each claimed response is present in the current manuscript or supported artifact, and that the response letter, visual diff, and repositories agree.
