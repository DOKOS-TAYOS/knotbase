# Knotbase user bootstrap

This file describes the **consumer's own installation**. The upstream public Knotbase repository is a template, never a destination for a user's personal records or routine maintenance changes.

**Implementation status:** The public checkout now includes `config/instance.csv` with unset values and header-only `info_user` templates. These are a static scaffold, not an installed or verified personal instance. Portable `maintenance_for_ai` procedures and executable owner-specific onboarding are not installed. Do not interpret this document's presence as successful bootstrap or as authorization to activate omitted commands.

## Bootstrap trigger

At the start of a newly adopted Knotbase instance, inspect `config/instance.csv`. If `instance_repository` or `github_owner` is empty, perform this bootstrap before selecting owner-specific GitHub commands, reading user facts as verified, or making repository mutations. Ask for the missing values conversationally, one decision at a time; do not guess from the original author's repository or from the currently connected GitHub account.

1. Ask which **user-owned fork or private instance repository** is the maintained Knotbase (`owner/repo`). It must be a repository the user is authorized to edit. Never default to `DOKOS-TAYOS/knotbase` or `DOKOS-TAYOS/dokos-instructions-knowledge`.
2. Ask which GitHub owner(s) and actual repositories are in scope. For multi-repository operations, populate and verify the inventory at `info_for_ai/info_user/repositorios_github.csv`, including archived and frozen status. An empty inventory never means “all repositories”.
3. Ask where the user wants their **private knowledge** to live. Recommended: a private fork or private knowledge repository accessible only to them. The `knowledge_repository` may equal `instance_repository` only if the instance is private. Personal data must never be pushed to the public upstream repository.
4. Offer optional self-description, CV, publications and professional profile records. Accept sources only when the user supplies or authorizes them. Empty tables remain empty, not fabricated. The user may defer personal setup and still use generic read-only educational/research workflows.
5. Record the configuration in the user's own private instance, only with their permission, and confirm that the repository and access rights actually exist. No credentials, tokens, passwords or sensitive material belong in the configuration or the chat transcript.
6. Check `info_for_ai/indice_dominios.csv`, `info_for_ai/info_user/indice_info_user.csv` and `maintenance_for_ai/indice_mantenimiento.csv` before declaring relevant owner workflows ready. Do not announce functional readiness for missing modules or validators.

## Safe operation

- If the configured instance is not writable, offer read-only guidance and report the blocker.
- For omitted explicit repository arguments, resolve only from the verified private inventory; ask when selection is ambiguous or incomplete.
- The canonical repository owner, publication catalog, knowledge-store location and command targets belong to the current user, **not** to the original DIK author.
- Changing the instance or owners is a scope change: reconfirm authorization and revalidate inventory.
- Distinguish onboarding templates from documented evidence: a blank CSV or Markdown profile is never proof of any personal fact.
- Public upstream updates should be integrated separately from user private data. Never propose a pull request that copies private instance files into upstream.

## Minimal completion criteria

`instance_repository` and `github_owner` have verified, nonempty values in the user's own instance; private knowledge storage has been chosen or explicitly deferred; no user secrets have been stored. Additional features require their own indexed dependencies and acceptance tests.

## Migration dependency contract

**Storage ownership.** A public Knotbase checkout contains routing instructions and empty templates only. Bootstrap must resolve the user's instance and private knowledge repository and verify read/write permissions *before* any command is permitted to persist personal facts, source records, repository inventory, or maintenance logs. A read-only answer may still be given from permitted public material when setup is incomplete.

**Path resolution.** Distinguish three namespaces: (a) upstream public instruction files, (b) the user-controlled instance and its maintenance procedures, and (c) the user-controlled knowledge files. Relative `info_for_ai/` and `maintenance_for_ai/` paths resolve against the configured instance or knowledge repository according to their indexed responsibility. Never infer a destination from the canonical DIK owner's literal paths or names. Cross-repository reads and writes require their own access and authorization checks.

**Required schema-preserving substitutions before activation:**

- Replace the original owner's publication catalog path with an explicitly indexed user catalog, preserving its CSV columns and publication-update semantics. Until that mapping is installed, `#PAPSYNC` must not run.
- Keep the original user-knowledge canonical layers and their source IDs, statuses, dates and visibility fields; publish only empty headers and blank derived views. Until their index and owner-specific storage are installed, `#ME`, `#BIO`, `#CVSYNC` and profile-maintenance commands must fail closed instead of fabricating records.
- Keep `repositorios_github.csv` and its line-number lookup together. Bootstrap must verify allowed owners, repository identity, archived/frozen status and inventory completeness before `#DEP`, `#SEC`, `#CLEAN`, `#RUNS`, `#TRIAGE` or a bulk synchronization. Even when a repository is explicitly supplied, retain the original workflow's eligibility and protection checks.
- Translate maintenance's hard-coded repository name into the configured *user instance* only after a verified selection. A copied procedure referring to original-owner publication files, a fixed GitHub owner, or a project instruction mirror must not be considered portable until those references have been reviewed and adapted individually.
- Port the canonical maintenance validator, dependency index and logbook procedures with equivalent checks against the configured instance. `#KBCHK` cannot claim full validity from Knotbase's existing subset-only structural suite; it requires validation of the exact installed target tree.
- Preserve the original distinction between user assertions and independently verified claims. Public templates contain no user facts, and private records should not be committed to upstream or placed in examples.

**Activation order:** publish and test configuration plus blank schemas; then index and test the user-knowledge domain; then adapt and validate maintenance procedures; then add the remaining 12 original commands, preserving their source-specific scopes and approval gates. `#NOAH` stays excluded. A public command is not operational merely because its row appears in a lookup.

## Acceptance conditions for a user instance

1. Unconfigured bootstrap: no write, no automatic cross-repository discovery and no fallback to the upstream author's repositories.
2. Verified private instance: records are written only to the selected authorized destination, never the public upstream.
3. Empty personal profile: `#ME` and `#BIO` report missing evidence rather than invented biography.
4. Repository inventory absent, incomplete, frozen or archived: the affected bulk command stops or excludes the target exactly as its original module requires.
5. Owner-scoped maintenance: a supplied CV, publication or repository update changes only its canonical record and genuinely affected derived views, retaining traceability and review status.
6. Validation and logging: maintenance operations run the portable canonical validator against the exact target tree and create only the required logbook records; missing validator or permission is a blocker, not success.
7. Remote mutation: checks, reviews, protection, current-head verification and authorization remain mandatory; a configured account alone grants no consent to publish or merge.
8. Source parity and regression: all retained original constraints are tested; any privacy or ownership adaptation is documented and must not weaken protections.
9. Functional acceptance: independent consumer runs must demonstrate actual routing, evidence selection, continuation gates and resulting artifacts. Structural CI alone is insufficient.
