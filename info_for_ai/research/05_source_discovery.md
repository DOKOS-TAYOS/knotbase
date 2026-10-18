# Scientific source discovery

## Activation

Use this module to find relevant scientific literature and establish a verified selection rationale. When source discovery itself is the requested deliverable, also provide the standalone summary and bibliography below. When loaded only as supporting research for another workflow, apply the search and verification method but let the parent workflow own output and artifacts under `00_core.md` supporting mode.

## Search method

1. Turn the topic into queries using synonyms, acronyms, techniques, applications, time constraints, and inclusion and exclusion criteria.
2. When the search tool supports multiple queries in one request, batch the initial candidate-discovery queries instead of issuing serial searches for closely related works or subquestions. Deduplicate candidate works before any follow-up search.
3. Search indexed journals and proceedings first. Supplement with preprint repositories, especially arXiv, when a published work is paywalled, an open version is needed, or no formal publication exists.
4. Once a candidate work has been located, reuse the existing result or open its canonical source directly. Do not repeat a semantically equivalent search for the same work unless a material metadata field, version, source claim, or coverage gap remains unresolved. Keep that follow-up query targeted to the unresolved item.
5. When a tool exposes result-length or response-size controls, request the shortest output sufficient for candidate location or metadata verification; expand only when substantive reading or ambiguity requires it.
6. Follow references from reviews and key works and inspect recent citations when this can materially change coverage or selection. Avoid routine citation chasing after the evidence set already satisfies the stated scope and success criteria, and avoid coverage biased by one database or keyword.
7. Record selection criteria, cutoff date, and foreseeable gaps in language, access, databases, dates, or publication types; surface them when they materially affect the final result.

## Standalone chat output

When literature discovery itself is the requested result, provide a table or list with at least a short reference, year or date, source type, brief contribution summary, relevance to the request, verified DOI or link, and open-access link when available. Sort by relevance and distinguish foundational papers, reviews, and recent results when useful.

In supporting mode, return source details only through the parent workflow's required shape. Do not add a separate literature table merely because this module was used internally.

## Bibliographic export

- Do not emit BibTeX or create a `.bib` artifact by default for standalone source-discovery requests when the normal bibliography already satisfies the task.
- Provide copyable BibTeX entries when the user explicitly requests BibTeX or when the parent workflow requires that representation.
- Generate a valid `.bib` with stable keys only when the user explicitly requests an export, the parent workflow requires a durable bibliography, or continued work materially benefits from a reusable bibliographic artifact.
- In supporting mode, do not generate BibTeX, `.bib`, APA, or another bibliographic artifact unless the parent workflow needs it or the user explicitly requests it.
- If the user requests APA or another style, provide that style and omit BibTeX unless also requested.
- When volume, pages, or DOI are unconfirmed, include only verified fields and state that the metadata is incomplete.
