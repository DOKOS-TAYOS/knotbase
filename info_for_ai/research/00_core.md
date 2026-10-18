# Shared research rules

## Activation and scope

Read this file before using any `research/` module. Select the module whose activation condition matches the task and combine modules only when each contributes a distinct method or output.

This domain owns evidence gathering, source verification, paper analysis, argument review, mathematical proofs, research-opportunity assessment, and state-of-the-art analysis.

**Default: supporting mode.** When another routed workflow loads a `research/` module only to obtain evidence, verification, comparison, or analysis for its own result, apply the research module's method and evidence rules but let the parent workflow own the user-facing structure and artifacts. Do not automatically emit the research module's standalone sections, reading paths, bibliographic exports, working files, or other deliverables unless the parent workflow requires them or the user explicitly requests them. This changes presentation only: preserve every source check and scientific conclusion needed to support the parent workflow's final claims.

## Scope and traceability

- Define the question, time horizon, field, and success criteria before searching. State any necessary scope assumptions.
- Distinguish established results, the source authors' interpretation, your inference, uncertainty, limitations, and research proposals.
- For each material source, record the author or organization, title, publication date, source type, canonical link, DOI when present, access date, and reason for relevance. In supporting mode this metadata may remain internal unless the parent workflow needs it in the final answer.
- Preserve titles, quotations, bibliographic metadata, and conventional technical terms in their natural or original language when appropriate.
- Prioritize primary and peer-reviewed sources: indexed journal articles, selective proceedings, original datasets, standards, and scientific bodies as appropriate. Use systematic reviews, monographs, and preprints for context or when they are the accessible version of an identified work.
- Never invent references, results, dates, authors, quotations, metrics, links, or DOIs. State evidence gaps explicitly.

## DOI, URL, and version verification

1. Locate the formal journal or proceedings version first. Verify that its DOI or canonical URL resolves to the correct title, authors, year, and venue.
2. When the published version is paywalled or unreadable, find a lawful accessible version such as an arXiv preprint, institutional repository copy, or author manuscript. State exactly which version was read when material to the answer.
3. Open and check every URL and DOI that will be returned as verified evidence or materially relied on for a final claim. Exclude broken links, redirects to a different work, and unconfirmed DOIs. Candidate sources discarded before they support a conclusion do not need redundant link-by-link verification after exclusion.
4. Preserve both the formal publication link and open-access link when valid and useful. Never substitute one for the other without saying so.

## Critical reading and uncertainty

- Read the relevant abstract, methods, results, figures, tables, appendices, and limitations before attributing a conclusion to a paper.
- Separate what a study measures from author interpretation and your extrapolation. Report sample size, assumptions, uncertainty, reproducibility, bias, and conflicts of interest when they affect the conclusion.
- Match certainty language to the evidence. Do not convert correlation into causation or a conditional proof into an unconditional claim.
- Write user-facing output in Spanish unless another language is requested. Keep formulas, symbols, and units unambiguous and define notation before use.

## Working artifacts

- Create a dated, descriptively named Markdown working file only when the selected standalone module or parent workflow requires durable notes, a bibliography, or a proof draft. Preserve source links and interpretation decisions. Do not add it to permanent knowledge without updating the canonical index.
- For an exportable bibliography, produce a valid `.bib` with stable keys. If APA is requested, provide APA instead of BibTeX unless both are requested.
- Use `research/plantilla_entrada.md` for research that must persist in this package and add its row to `research/indice_research.csv`.

## Limits

Do not diagnose, replace professional advice, or claim that a research direction guarantees publication, impact, or industrial return. Report coverage limits, access limitations, the cutoff date, and the evidence available when they materially affect the result.
