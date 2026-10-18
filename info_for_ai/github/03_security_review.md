# GitHub security review and remediation

## Activation

Use this module when the user asks to review security issues, alerts, or vulnerabilities across repositories and automatically fix those with small, robust remediations.

The request authorizes inspection of accessible security surfaces and minor verifiable technical remediation. It does not authorize revealing secrets, disabling controls, silently accepting risk, or performing major migrations without reporting them.

## Security surfaces

When enabled and accessible, inspect each relevant category independently:

1. **Dependabot alerts:** known dependency vulnerabilities.
2. **Code scanning alerts:** CodeQL or other SARIF analyzer findings.
3. **Secret scanning alerts:** detected credentials or secrets.
4. **Repository security advisories:** private or published advisories associated with the repository.
5. Vulnerability-related Dependabot pull requests.

An empty result from one category says nothing about the others.

## Capability preflight and access

Resolve repository scope, live-metadata policy, private-resource uncertainty, fallback between authorized GitHub surfaces, and multi-repository coverage through `00_core.md` and `repository_inventory_and_scope.md`.

**Default:** Before iterating over a multi-repository scope, probe each security surface once using the best available authenticated capability and classify it as `available`, `disabled`, `permission-blocked`, or `unavailable-in-runtime`. Perform this capability preflight before any live per-repository metadata sweep. Reuse the result for the run instead of repeating the same failing request repository by repository, unless evidence shows that availability differs materially by repository. For a category established as globally blocked or unavailable, do not enumerate or refresh repository metadata solely for that category; for accessible categories, defer targeted live repository metadata until a result, mutation, material discrepancy, or tool contract requires it under the shared inventory policy.

Prefer organization-level endpoints when the official API exposes an equivalent alert inventory and the authenticated principal has permission to use them. Use repository-level queries only for surfaces that lack a suitable bulk endpoint or when repository-specific confirmation is required.

Do not repeatedly retry a category after the preflight has established a stable permission or runtime limitation. Continue with the remaining categories and report the blocked surface once. Treat an explicitly disabled scanner as `disabled` rather than as evidence of zero alerts or a repository failure.

## Inventory and prioritization

For every repository and accessible security category in scope, record open alerts by category, severity, affected file, dependency or location, default branch, an existing remediation pull request, date and state, available technical evidence, and whether safe automatic remediation is possible. Group duplicates with the same root cause.

Do not create per-repository placeholder records for a category already established as globally `permission-blocked` or `unavailable-in-runtime`; record the capability limitation once and continue with categories that can be inspected.

Prioritize approximately as follows, adjusted for exposure, reachability, production use, and availability of a fix:

1. valid or potentially valid secrets;
2. critical vulnerabilities;
3. high vulnerabilities;
4. exploitable or clearly impactful code-scanning findings;
5. medium severity;
6. low or informational findings.

## Dependabot alerts

When a compatible update remediates a vulnerability, look for an existing corrective pull request and evaluate it with [02_dependabot_review.md](02_dependabot_review.md). If no pull request exists and the fix is a small update, use `../code/00_core.md` plus the relevant code module to prepare it, verify it, and then use [01_integration_and_publication.md](01_integration_and_publication.md) to publish and integrate it when authorized.

Do not dismiss an alert merely because updating is inconvenient. A false-positive, tolerable-risk, or unused-code resolution requires evidence and must state the real reason.

## Code scanning

If code scanning is explicitly disabled for a repository, record that state and skip alert enumeration. Do not recommend enabling it unless the user asked for security-hardening recommendations or enabling scanners is otherwise within scope.

For each alert, inspect the rule, location, and data flow when available; determine applicability or reproducibility; make a localized correction only when the solution is clear and preserves important contracts; add or adjust tests when the vulnerability can be covered; and verify that configured analysis, tests, and current-SHA CI pass and the finding is properly resolved.

Do not label a finding as a false positive merely to make CI green. Report instead of improvising when remediation requires non-trivial architectural, cryptographic, permissions, or security-design decisions.

## Secret scanning

**Invariant:** Never print or reproduce a secret, assume deleting a file revokes the credential, or mark a real secret resolved merely because it is absent from `HEAD`.

1. Identify the secret type without reproducing its value.
2. Determine whether it may still be valid and locate only the appearances needed for remediation.
3. Remove it from code or configuration when safe and replace its use with the project's supported secret mechanism when the correction is small.
4. Determine whether provider-side revocation or rotation is still required.

If authorized tools cannot revoke or rotate the credential, state clearly that this external action remains. Never mark an alert `revoked` without evidence. Rewriting repository history is high impact and requires explicit authorization and a safe strategy.

## Repository security advisories

If accessible, identify relevant open or draft advisories without publishing private details. Correcting code does not by itself authorize creating, publishing, requesting a CVE for, or closing an advisory; those actions require the request to include that purpose.

## Remediation classification

### A. Fix and integrate

Use for a small, clear, verifiable fix such as upgrading to a patched dependency, correctly sanitizing or validating input, fixing localized unsafe configuration, replacing an unsafe call with its direct safe alternative, or removing an accidental credential and using an already-supported secret mechanism.

### B. Fix but do not close yet

Use when code is corrected but an external action remains, such as credential rotation or scanner confirmation.

### C. Report without modifying

Use for a non-trivial authentication, authorization, or cryptographic redesign; major migration; infrastructure rotation without access; broad history rewrite; risk-acceptance decision; or insufficient evidence for safe remediation.

## Verification and output

After a correction, run the applicable local checks through the selected `code/` module, inspect current-SHA CI, and verify the alert when the surface permits it. Do not treat visual disappearance alone as proof when an external action remains.

Report each category inspected and distinguish `fixed`, `integrated`, `alert verified as resolved`, `disabled`, `permission-blocked`, `unavailable-in-runtime`, and `external action pending`. Report unavailable categories under the shared GitHub access contract rather than interpreting them as empty.
