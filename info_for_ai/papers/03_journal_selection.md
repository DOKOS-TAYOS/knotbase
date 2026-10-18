# Journal selection workflow

## Activation and scope

Use this module when the user already has a scientific paper and wants either to identify realistic publication venues or to continue from that decision into journal-format adaptation.

The paper may be an arXiv identifier/URL, manuscript repository, uploaded TeX project or ZIP, another directly accessible artifact, or the single unambiguous manuscript already established in the current task.

### Selection mode

Use selection mode when `#JOURNAL` has no target journal. If the manuscript is not explicit, resolve it only from one unambiguous current-task source; never guess among multiple manuscripts.

Selection mode is read-only. It ranks publication venues and does not modify the manuscript, adapt templates, submit, or contact editors.

### Adaptation handoff mode

Use adaptation handoff mode when both one TeX manuscript repository and one target journal are identified, either directly as `#JOURNAL <repo>; <journal|URL|requirements...>` or in an unambiguous direct continuation of the selection task.

Do not rerun selection unless the user asks to reconsider the venue. Load `02_journal_adaptation.md` and the additional code responsibility it requires. The identified repository plus journal authorizes only the bounded local adaptation owned there; it does not authorize pushing, pull requests, merging, submission, editor contact, or unrelated scientific changes.

The adaptation must be performed in exactly the supplied manuscript repository. Preserve useful verified evidence from the immediately preceding selection, but reverify current official requirements where `02_journal_adaptation.md` requires it.

The remainder applies only to selection mode.

## 1. Establish the manuscript profile

Inspect enough of the manuscript to establish:

- title, abstract, topic, area, research objective, contribution, and claimed novelty;
- methodology, theory, experiments/data, validation level, principal results, and limitations;
- likely readership, article type, and manuscript scale when they affect venue eligibility.

Base the search on the manuscript itself, not repository names or the authors' broader profile.

## 2. Acquire evidence through `research`

Journal indexing, quartiles, fees, policies, collections, and publication profiles change over time. Load `../research/00_core.md` and only the applicable research modules. Use `../research/05_source_discovery.md` for systematic discovery; add deep-research or state-of-the-art modules only when their distinct method is necessary.

Research supporting mode applies: reuse its search, traceability, source verification, version handling, and evidence discipline without emitting standalone research sections or bibliography artifacts unless this workflow actually needs them.

Prefer, as applicable:

1. official journal/publisher material for scope, article types, author instructions, fee routes, and collections;
2. Scopus Sources or Clarivate/JCR for current indexing and quartile evidence;
3. SCImago as a secondary Scopus-based quartile source when needed;
4. DOAJ for open-access/no-APC evidence;
5. recognized scholarly societies, COPE, or similarly authoritative governance sources;
6. credible secondary discussion only when it adds material reputation or submission-risk context that primary sources cannot establish.

Record the year and genuinely relevant subject category for each quartile used in the final ranking.

## 3. Staged candidate funnel

**Default:** Do not fully verify every discovered journal before establishing basic manuscript fit. Use a staged funnel to reduce redundant searches while preserving all final eligibility gates.

1. **Broad discovery:** generate enough plausible venues to avoid anchoring on the first familiar journal.
2. **Cheap fit screen:** use readily available aims/scope, readership, contribution type, article type, and obvious policy incompatibilities to discard clearly unsuitable venues. Stop investigating a candidate once a decisive exclusion is established; do not then verify unrelated quartile, fee, collection, or reputation details merely for completeness.
3. **Finalist verification:** for the plausible shortlist, verify every mandatory eligibility gate below and collect the evidence needed for ranking.
4. **Ranking evidence:** only for eligible finalists, inspect selectivity, recent comparable papers, editorial bar, collections, and other detail needed to distinguish realistic acceptance probability.

A journal may appear in the ranked recommendation table only after passing every mandatory gate. Preliminary fit evidence is never enough for final eligibility.

## 4. Mandatory eligibility gates

### 4.1 Current indexing

**Invariant:** The journal must have current verifiable indexing in Scopus or the Web of Science Core Collection unless the user explicitly names another accepted system. Exclude candidates whose required indexing cannot be verified.

### 4.2 Quartile

Prefer Q1 and Q2 journals. Q3 is acceptable when fit or realistic publication probability is materially better. Exclude Q4 by default. If no credible Q1-Q3 option survives, say so instead of silently lowering the standard.

### 4.3 No mandatory author payment

**Invariant:** Verify a compliant publication route with no mandatory author payment.

Eligible routes include subscription/closed publication without unavoidable charges, hybrid journals with optional OA and a free subscription route, and genuinely fee-free diamond/platinum OA.

Exclude unavoidable APCs, submission/publication/processing fees, or mandatory page charges for a standard compliant article. Do not treat discretionary waivers, discounts, coupons, or uncertain funding agreements as guaranteed zero-cost routes. If the fee model remains ambiguous, do not present the journal as satisfying this gate.

### 4.4 Reputation

Exclude venues with credible evidence of predatory behavior, deceptive editorial practice, severely compromised peer review, or comparably poor scholarly reputation. Do not infer predatory status from one informal blacklist or anecdote; use current indexing, transparent editorial information, publisher/society identity, and material warning signals together.

## 5. Finalist fit assessment

For every retained journal assess only the dimensions material to ranking:

- topical/methodological scope and readership fit;
- fit of contribution type, novelty level, and existing evidence;
- likely desk-rejection risk and scientific bar;
- article-type/length compatibility when material;
- verified indexing, relevant quartile, zero-mandatory-fee route, and material reputation concerns;
- active special issue, collection, or section only when genuinely relevant and currently usable.

Collections never bypass the same indexing, reputation, and fee gates and do not change the journal's quartile by themselves.

## 6. Revision scenarios

All estimates assume routine conversion to the journal's required format; formatting alone is not a scientific manuscript change.

### Minor-change scenario

Allow bounded changes that preserve the manuscript essentially as written: sharper framing, modest related-work updates, clearer motivation/limitations/relevance, local exposition or figure/table improvements, and small checks derivable from existing results. Do not assume new central experiments, datasets, methods, or objectives.

### Bounded-major-change scenario

Allow substantial but realistic revisions that preserve the paper's identity and core contribution: limited additional experiments/baselines/ablations/robustness checks using the existing pipeline, stronger validation/error analysis, substantial positioning revision, expanded theoretical justification, or restructuring for the target audience.

**Invariant:** Never raise a venue's estimate by assuming a disruptive scope change, different central problem, replacement core method, fundamentally new experimental programme, or a different paper. Treat such a venue as poor fit.

## 7. Acceptance-probability estimates

Probabilities are manuscript-specific decision-support estimates, not guarantees or journal acceptance rates. Base them on verified venue evidence plus scope fit, novelty threshold, methodological strength, validation completeness, selectivity, desk-rejection risk, article type, and revision burden.

Use approximate percentages, normally sensible 5-point increments. Keep minor and bounded-major scenarios distinct. The bounded-major-change probability must stay within the scenario above and must never assume disruptive work. An official acceptance rate may inform but never replace manuscript-specific judgment.

## 8. Required output

Begin with a comparison table containing only journals that passed all mandatory gates, except for a clearly separated excluded candidate when explaining an obvious rejection is materially useful.

| Journal | Quartile | Acceptance probability with minor changes | Acceptance probability with bounded major changes | Comments |
| --- | --- | --- | --- | --- |

In `Quartile`, include source/year or relevant category only when useful. In `Comments`, include only decision-relevant facts such as the zero-fee route, scope caveat, useful collection, or material policy/reputation issue.

Sort by bounded-major probability, then minor-change estimate, then scientific fit.

After the table, provide manuscript-specific sections only for the top three ranked journals:

1. **Why it fits:** concrete match between contribution, audience, scope, and journal bar.
2. **What should change:** minor package first, then bounded-major additions that materially raise the estimate.
3. **Submission-relevant notes:** only material quartile/indexing nuance, zero-fee route, collection/section fit, rejection risk, or uncertainty.

When fewer than three eligible journals can be verified, return only the verified set and explain the limiting constraint instead of weakening the gates.
