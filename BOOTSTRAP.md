# Knotbase user bootstrap

This file describes the **consumer's own installation**. The upstream public Knotbase repository is a template, never a destination for a user's personal records or routine maintenance changes.

**Implementation status:** The public checkout now includes `config/instance.csv` with unset values and header-only `info_user` templates. These are a static scaffold, not an installed or verified personal instance. Indexed portable `maintenance_for_ai` procedures and an offline target-tree validator are included. Owner-specific onboarding still requires a real private instance, verified remote permissions, explicit authorization and independent consumer tests. Do not interpret this document's presence as successful bootstrap or as authorization to activate omitted commands.

## Bootstrap trigger

At the start of a newly adopted Knotbase instance, inspect `config/instance.csv`. If `instance_repository` or `github_owner` is empty, perform this bootstrap before selecting owner-specific GitHub commands, reading user facts as verified, or making repository mutations. Ask for the missing values conversationally, one decision at a time; do not guess from the original author's repository or from the currently connected GitHub account.

1. Ask which **user-owned fork or private instance repository** is the maintained Knotbase (`owner/repo`). It must be a repository the user is authorized to edit. Never default to `DOKOS-TAYOS/knotbase` or `DOKOS-TAYOS/dokos-instructions-knowledge`.
2. Ask which GitHub owner(s) and actual repositories are in scope. For multi-repository operations, populate and verify the inventory at `info_for_ai/info_user/repositorios_github.csv`, including archived and frozen status. An empty inventory never means “all repositories”.
3. Ask where the user wants their **private knowledge** to live. Recommended: a private fork or private knowledge repository accessible only to them. The `knowledge_repository` may equal `instance_repository` only if the instance is private. Personal data must never be pushed to the public upstream repository.
4. Offer **flexible, optional personal-profile onboarding** using the source and interaction choices in the next section. The user can provide one item, several sources, a simple self-description, or no profile yet. Do not require a CV, a particular platform, a fixed questionnaire or a completed profile. Empty tables remain empty, not fabricated. Generic read-only educational/research workflows remain available when personal onboarding is deferred.
5. Record the configuration in the user's own private instance, only with their permission, and confirm that the repository and access rights actually exist. No credentials, tokens, passwords or sensitive material belong in the configuration or the chat transcript.
6. Check `info_for_ai/indice_dominios.csv`, `info_for_ai/info_user/indice_info_user.csv` and `maintenance_for_ai/indice_mantenimiento.csv` before declaring relevant owner workflows ready. Do not announce functional readiness for missing modules or validators.

## Flexible profile and evidence onboarding

**Default:** Let the user start with whichever sources or interaction style are easiest for them. Offer a few concise options in conversation, not a compulsory form. These are **alternative and combinable paths**, not steps that all users must complete. Profile collection is optional and can continue over several chats or be resumed later using only actually accessible saved records or re-supplied materials.

### Ways the user can provide information

- **Upload a CV or professional document:** PDF, DOCX, text, Markdown, a portfolio, a biography, certificates, a publications list, references or a project description. Extract only readable, relevant content supported by the actual file.
- **Share screenshots or images:** captures of LinkedIn sections (About, Experience, Education, Skills), GitHub, ORCID, Google Scholar, a personal website, a portfolio or other professional pages. Read what is **visible in the image**; distinguish screenshot text from independent verification, and ask for another capture only if a material part is cut off or illegible.
- **Paste links:** public LinkedIn or other professional-profile URLs, GitHub repositories, portfolio pages, publication pages, DOI/ORCID records and comparable sources. Inspect only the provided, authorized links when the current tools can actually access them. A URL is not its contents: if blocked by login, rate limits, permissions or tooling, explain the limitation and offer a screenshot, file export or pasted text instead. Never claim to have inspected an inaccessible page.
- **Paste text or an existing description:** a short biography, work history, skills, completed projects, teaching, research contributions, career goals or an unstructured collection of notes. The user's statements are valid *user-provided assertions*, not automatic independent verification.
- **Describe experience conversationally:** the user can simply tell the assistant what they have done, know, are learning or want to do. If voice messages or transcriptions are supported in the active client, those can be used in the same manner; do not assume audio or video inputs are available.
- **Provide structured exports or lists:** CSV/JSON exports where supported, publication catalogs, GitHub repository lists, course records or an existing profile knowledge base. Preserve the original meaning and schema, and read only the user-authorized scope.
- **Choose guided questions only:** if the user has no documents or prefers not to upload anything, ask **one useful question at a time**. Start from their goal and capture the minimum facts required for that goal. They may say “I don't know”, “skip”, “later” or “I don't want to share that”.
- **Mix routes freely:** for example, a CV plus LinkedIn screenshots plus GitHub links plus corrections supplied in chat. Do not force the user to convert everything to a single format.

**Opening offer (adapt the language to the user):**

> Para conocer tu perfil, puedes adjuntar tu CV, subir capturas de LinkedIn u otros perfiles, compartir enlaces públicos, pegar una descripción de lo que has hecho o contarme tu trayectoria en una conversación. También podemos ir pregunta por pregunta. Elige una o varias opciones; no tienes que completarlo todo ahora. Antes de guardar nada, revisaremos juntos qué datos son correctos y dónde se almacenarán.

If the user has **already attached or pasted material**, begin with that material and ask only about missing information needed for the current purpose; do not make them select an input method they already selected. Do not require a separate form, nor make them re-enter content that is actually accessible.

### From supplied materials to trustworthy records

1. **Intake:** Establish which supplied documents, screenshots, URLs or statements the user wants included, the immediate goal (general profile, CV, GitHub inventory, papers, etc.) and the preferred visibility of personal data. Do not collect every possible detail by default. Inspect supported attachments directly; do not imply that external sites, accounts or connectors have been read without a successful access.
2. **Evidence extraction:** Produce a concise proposed profile organized only by supported fields: identity where authorized, education, roles, responsibilities, individual contributions, projects, skills with demonstrated scope, publications, teaching, links, preferences, and goals. Differentiate **what the user did** from what a team, organization or repository did. Keep plans, interests and ambitions distinct from completed experience.
3. **Provenance:** Retain the origin of each material claim (user statement, named CV/document, screenshot and visible section, inspected URL and access date, structured export). A screenshot is a time-bounded observation, a CV may be outdated, and a web profile may be inaccessible or incomplete. Preserve dates when present, visible evidence, ambiguity and the appropriate review/visibility status. Do not call user-provided statements externally verified without actually verifying them.
4. **Reconciliation:** Detect overlap, outdated entries and material contradictions across sources. Never silently combine incompatible job titles, dates, authorship, proficiency or project ownership; present the discrepancy and ask the smallest necessary question. A profile, project topic or listed technology does not by itself prove unrestricted personal expertise.
5. **User review:** Present a readable summary of proposed facts and source limitations. Allow corrections, omissions, scope adjustments and visibility choices such as `public`, `restricted` or `private`. If the user prefers not to save, they may use the material only for the current task where available. Do not silently persist whole uploaded CVs, screenshots or other raw source files.
6. **Authorized persistence:** Only after verifying the exact **private** knowledge destination, access and specific user authorization, write reviewed records to the installed canonical `info_user` schema using the selected indexed maintenance procedures. Preserve source IDs, traceability, visibility, confidence and review status as required by that schema. Do not create unsupported fields, treat raw uploads as public assets, or publish private evidence to a public fork. If the environment cannot perform a permitted write, provide a reviewable draft or patch and report that it is **not saved**.
7. **Incremental continuation:** Mark optional areas as unprovided rather than failures. Summarize what has genuinely been recorded, what is provisional, and which useful follow-up information could improve the user's chosen workflows. Never imply cross-chat persistence unless the private repository actually contains the records or a connected source is accessible.

For screenshots and documents, handle personal information about **third parties** conservatively; do not copy irrelevant contact details, private messages or sensitive fields into the knowledge store. Allow the user to redact screenshots/files before sharing. Never request passwords, access tokens or other secrets as a bootstrap source. Links that require login are not permission to bypass access controls.

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

- Replace the original owner's publication catalog path with an explicitly indexed user catalog, preserving its CSV columns and publication-update semantics. Until an actual configured user and writable private catalog are verified, `#PAPSYNC` must not mutate any repository.
- Keep the original user-knowledge canonical layers and their source IDs, statuses, dates and visibility fields; publish only empty headers and blank derived views. Without verified owner-specific evidence and private storage, `#ME`, `#BIO`, `#CVSYNC` and profile-maintenance commands must fail closed instead of fabricating records.
- Keep `repositorios_github.csv` and its line-number lookup together. Bootstrap must verify allowed owners, repository identity, archived/frozen status and inventory completeness before `#DEP`, `#SEC`, `#CLEAN`, `#RUNS`, `#TRIAGE` or a bulk synchronization. Even when a repository is explicitly supplied, retain the original workflow's eligibility and protection checks.
- Translate maintenance's hard-coded repository name into the configured *user instance* only after a verified selection. A copied procedure referring to original-owner publication files, a fixed GitHub owner, or a project instruction mirror must not be considered portable until those references have been reviewed and adapted individually.
- Port the canonical maintenance validator, dependency index and logbook procedures with equivalent checks against the configured instance. `#KBCHK` must run the installed canonical offline validator against the exact target tree, plus remote and consumer-runtime checks when claiming those capabilities; it cannot claim full functionality from structural checks alone.
- Preserve the original distinction between user assertions and independently verified claims. Public templates contain no user facts, and private records should not be committed to upstream or placed in examples.

**Activation status:** Blank schemas, indexed user-knowledge domain, portable maintenance procedures, canonical offline validator and 12 owner-scoped command registrations are present. `#NOAH` stays excluded. The public upstream is unconfigured; commands requiring an owner's credentials, inventory, records or permissions must fail closed until those prerequisites are verified. Command registration alone does not establish end-to-end operational readiness.

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
10. Multisource onboarding: test CV/document intake, profile screenshots, accessible/inaccessible links, free-text assertions, guided-question-only setup and a mixed-source case. Verify origin and confidence labels, conflict handling, partial setup, and that no personal record is saved without explicit authorization.
11. Privacy and permissions: test that raw screenshots/CVs are not published by default, inaccessible links are not represented as inspected, and public forks cannot receive private profile records.
