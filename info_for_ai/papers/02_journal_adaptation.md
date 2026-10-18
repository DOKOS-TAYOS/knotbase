# Journal adaptation workflow

## Activation and scope

Use this module when adapting an identified TeX manuscript repository to the submission format of a target journal or publisher. The user may provide the journal name, an official author-instructions page, a journal template archive, or a combination of these.

This module owns the manuscript-side adaptation plan and the journal-specific formatting contract. It does not replace:

- [code instructions](../code/indice_code.csv) for local repository edits, compilation, testing, and reproducible file changes;
- [GitHub instructions](../github/indice_github.csv) when the user asks for remote repository state, branches, commits, pull requests, or publication;
- [research instructions](../research/indice_research.csv) when external scientific evidence or literature assessment is required beyond checking journal requirements.

**Invariant:** Adapt the submission format without silently changing the scientific meaning. Do not alter claims, equations, numerical results, citations, authorship, acknowledgements, funding statements, or interpretation merely to fit a template. Make scientific or substantive edits only when the journal explicitly requires them or the user authorizes them.

## Inputs and authority

Establish the target manuscript repository, branch or commit when relevant, and the intended journal or submission track. Accept journal requirements from any of these forms:

- an official author-instructions or submission-guidelines page;
- an official or user-supplied template archive containing TeX classes, styles, examples, bibliography files, or documentation;
- explicit requirements pasted by the user;
- a journal or publisher name from which the current official requirements must be located.

When a URL is supplied or discovered, verify that it is the current official source when possible. Treat a supplied template archive as implementation material, not automatically as the highest-authority statement of policy. If the template, official instructions, and explicit user constraints conflict, preserve the conflict in the working notes and follow the most authoritative current requirement unless the user directs otherwise. Never invent a missing journal rule.

Do not execute arbitrary scripts from a downloaded template archive merely because they are present. Inspect the archive first and run only tooling necessary for the adaptation and reasonably safe in the task environment.

## 1. Build the journal requirements contract

Before editing, extract the requirements that can materially affect the source or compiled submission. Check, as applicable:

- document class, class options, required style files, and supported TeX engine;
- title, author, affiliation, corresponding-author, ORCID, abstract, keywords, and running-title format;
- anonymous-review or double-blind requirements;
- section structure, heading levels, appendices, supplementary material, data/code statements, declarations, acknowledgements, funding, conflicts of interest, and author-contribution statements;
- page, word, abstract, title, figure, table, reference, or supplementary limits;
- figure and table placement, caption style, resolution, file format, and naming rules;
- equation, theorem, algorithm, listing, footnote, and cross-reference conventions when specified;
- citation and bibliography style, `.bib` expectations, DOI handling, and reference-order rules;
- line numbering, page numbering, manuscript spacing, review mode, or track-change requirements;
- source-package restrictions, required file names, excluded auxiliary files, and submission-system constraints.

Separate requirements into `required`, `recommended`, `optional`, and `unresolved`. Record the source for every non-obvious requirement that drives a manuscript change.

## 2. Inspect and baseline the manuscript

Before modifying the repository:

1. identify the main TeX entry point, bibliography sources, figure/table assets, custom macros, local style files, and build tooling;
2. read the target repository's local instructions and preserve unrelated work;
3. compile the existing manuscript when the environment supports it and record the command and result;
4. identify source constructs that are incompatible with the target journal contract;
5. distinguish formatting changes from substantive changes that require user judgment.

If the original manuscript does not compile, do not disguise the baseline problem as a journal-adaptation failure. Report the pre-existing error separately and proceed only where the remaining work can be verified safely.

## 3. Apply the template with a smallest-change strategy

Prefer the smallest coherent source transformation that satisfies the journal contract. Reuse the journal's provided class, style, bibliography, and sample structure when appropriate, but do not copy irrelevant example content or overwrite manuscript text mechanically.

Preserve the manuscript's internal organization, labels, macro definitions, figure files, bibliography database, and reusable source structure when they remain compatible. Do not refactor the TeX tree merely to imitate the sample template's file layout.

Do not edit publisher-provided class or style files unless the official instructions explicitly require a local change or there is a demonstrated incompatibility that cannot be solved from the manuscript source. If such a modification is necessary, isolate it, explain it, and verify that it does not create submission risk.

For every adaptation, ensure that:

- author and affiliation metadata remain factually correct and are transformed only into the required syntax;
- bibliography style changes do not drop references or alter citation identity;
- figure and table transformations preserve content and references;
- custom macros remain semantically equivalent or are replaced transparently;
- anonymization removes identifying material only for the anonymous submission artifact and does not destroy the canonical author information;
- declarations and journal-specific sections are populated only with information actually supported by the manuscript or user-provided facts.

Never invent missing ORCIDs, funding identifiers, conflicts, contribution roles, data-availability claims, ethics approvals, or supplementary artifacts.

## 4. Validate source and compiled output

After adaptation, compile from a clean or reproducible build state using the journal-compatible toolchain. Run the repository's applicable checks and inspect the resulting PDF, not only the TeX log.

Verify at minimum:

- successful compilation or a precisely documented external blocker;
- absence of unresolved references, citations, missing assets, and avoidable TeX errors;
- correct front matter, section order, bibliography rendering, captions, figures, tables, equations, and appendices;
- compliance with explicit journal limits that can be checked locally;
- no accidental loss or duplication of manuscript content;
- no unsupported substantive wording introduced during formatting;
- no unnecessary auxiliary, build, or template-example files in the intended submission package.

Because journal conversion can substantially alter pagination and layout, do not use visual similarity to the original PDF as the acceptance criterion. Instead, verify semantic preservation and journal-format compliance. When feasible, compare the manuscript text, labels, references, equations, figures, and tables before and after adaptation to detect accidental content changes.

## 5. Final handoff

Return or prepare the adapted manuscript in the user's requested repository or artifact form. Summarize concisely:

- which journal requirements were implemented;
- which source files materially changed;
- the compilation and validation evidence;
- any unresolved or contradictory journal requirement;
- any item that still requires a factual choice from the author rather than formatting judgment.

Do not claim that the manuscript is acceptable to the journal merely because it compiles or matches the template. The completion criterion is a verified, submission-ready adaptation against the requirements available to the task, with remaining uncertainties stated explicitly.
