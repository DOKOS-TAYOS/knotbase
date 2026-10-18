# Repository identity, authorship, and metadata

## Activation

Use this module when asked to prepare, complete, or review a repository's legal and editorial identity: README, license, authorship, contact details, NOTICE, third-party licenses, academic citation, contribution guidance, or package metadata.

## Default data, subject to relevance

- Author: **[configured author name]**.
- Professional contact: `[configured professional contact]`.
- Preferred license for original code: **MIT**.

Before adding other information, consult `../info_user/indice_info_user.csv` and open only the relevant records. Do not invent an affiliation, URL, identifier, third-party copyright, version, start year, DOI, or author.

## Procedure

1. Inspect existing files, package manifests, contribution history, dependencies, and repository policy. Detect authorship, licensing, or trademark conflicts before changing anything.
2. Explain which files exist, which are missing, and which facts can be confirmed. If ownership of existing code is unclear, stop and request a decision: do not relicense third-party code or attribute work to the user that is not theirs.
3. Create or update only what applies:
   - `README.md`: purpose, audience, installation or quick start, usage, and links to licensing and contribution guidance.
   - `LICENSE`: the complete canonical MIT text with a confirmed holder and year. Do not guess the year.
   - `NOTICE`: required attribution, notices, or provenance clarification; never use it as a substitute for dependency licenses.
   - `THIRD_PARTY_LICENCES.md`, or the project's existing equivalent: a reproducible inventory of redistributed dependencies, versions, origins, licenses, and required notices.
   - `CITATION.cff`: only for citable or scientific software, or when requested. Produce valid CFF and omit any unconfirmed DOI, version, or date.
   - `CONTRIBUTING.md`: actual environment requirements, contribution flow, tests, style, and issue-reporting process.
   - Ecosystem manifests: synchronize author, license, repository, and contact fields only when the schema supports them and the facts are confirmed.
4. Verify consistency across all files. The license named in the README, manifests, and `LICENSE` must agree.
5. Report files created or changed, pending decisions, and the source of any reused personal information.

## Minimum result

Provide a table with `file`, `action`, `confirmed data`, and `pending`. State explicitly when MIT cannot yet be applied because ownership or compatibility is uncertain.
