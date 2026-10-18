# Journal-targeted paper review workflow

## Activation and purpose

Use this module when a manuscript has already been adapted to a selected journal and the user wants a detailed review aimed at increasing realistic acceptance probability.

Canonical form: `#PAPERFIT <repo>; <journal>`.

This workflow is distinct from journal selection (`03_journal_selection.md`), journal adaptation (`02_journal_adaptation.md`), and responses to actual reviewer/editor comments (`01_peer_review_response.md`).

This module owns the **first inventory and planning phase**: journal-specific diagnosis, the stable `PF-###` backlog, prioritization, approval state, manuscript-side revision workflow, and coordination of approved code work. It does not own later approved execution mechanics; after the first inventory, load the indexed `paperfit_execution.md` only when a direct continuation advances into batch proposal or execution.

The first invocation is read-only. It must not modify TeX, code, repository state, or remote state.

## 1. Establish the evidence baseline

Inspect the manuscript repository deeply enough to understand the paper as one scientific argument. Read the manuscript, bibliography, figures, tables, appendices, supplementary material, and repository evidence that materially supports its claims.

Establish at least:

- research question, objective, contribution, and claimed novelty;
- target audience and why the work belongs in the selected journal;
- theoretical/methodological/experimental evidence supporting the claims;
- strongest and weakest links in the evidence chain;
- positioning relative to close prior work;
- limitations, assumptions, threats to validity, and generalization boundaries;
- relationships among claims, figures, tables, experiments, proofs, and conclusions;
- material reproducibility, data/code, ethics, reporting, or transparency obligations.

Evaluate the manuscript itself, not repository presentation or author reputation.

When external literature, novelty, frontier comparison, or independent argument validation is needed, load `../research/00_core.md` and only the applicable research modules. Supporting mode applies: consume their methods and verified evidence without inheriting standalone research sections or bibliography artifacts. Use `../research/05_source_discovery.md` for literature discovery, `../research/01_deep_research.md` plus `../research/07_state_of_the_art.md` for current positioning/frontier comparison, and `../research/03_argument_review.md` for independent argument, calculation, derivation, or proof assessment.

## 2. Reconstruct the journal acceptance target

Use current external evidence because scope, article types, editorial policies, reporting requirements, and publication profile can change.

Prefer, in order:

1. current official aims and scope;
2. official author instructions, article-type/editorial criteria, reporting, data/code, ethics, and submission policies;
3. official section/collection requirements when applicable;
4. recent genuinely comparable papers from the journal;
5. publisher or scholarly-society material clarifying expectations;
6. credible secondary evidence only when it adds material context unavailable from primary sources.

Use source-discovery support for comparable papers. Add deep-research/SOTA only when those comparisons are actually used to judge novelty, competitiveness, or frontier position.

Formatting compliance is not scientific fit. Report residual format/policy issues only when they are blockers or materially affect editorial review.

## 3. Review dimensions

Review the complete manuscript and create a finding only when there is manuscript-specific evidence that a change has a plausible path to improving acceptance probability. Do not inflate the backlog with generic or cosmetic advice.

Assess when applicable:

- **Journal fit and framing:** readership, title/abstract/introduction/conclusion framing, article type, desk-rejection risk.
- **Novelty and positioning:** defensibility of novelty claims, closest competing work, over/underclaiming, journal-level contribution bar.
- **Methodological/theoretical rigor:** assumptions, derivations, proofs, algorithms, statistics, baselines, controls, parameter choices, experimental design, and unsupported leaps.
- **Experimental/empirical evidence:** sufficiency of experiments, baselines, ablations, robustness/sensitivity, uncertainty/statistical treatment, error analysis, and bounded additional validation.
- **Results/discussion/limitations:** proportionality of conclusions, distinction between evidence and interpretation, negative/boundary cases, threats to validity.
- **Literature/citations:** missing close work, technically unfair comparisons, stale positioning, and citations that materially change reviewer risk.
- **Reproducibility/reporting:** code/data/seeds/hyperparameters/preprocessing/hardware/tolerances/splits/evaluation detail plus journal-specific transparency or ethics requirements.
- **Scientific communication:** figures, tables, equations, notation, definitions, structure, repetition, and ordering that materially affects technical evaluation.

Use the corresponding research module before issuing a conclusion that depends on external scientific evidence or independent validation.

## 4. Scope boundary

The objective is to maximize realistic acceptance probability while preserving the paper's identity.

**Invariant:** Do not recommend replacing the central research question, moving to a substantially different topic, replacing the core contribution/method, or starting a new research programme that would effectively create a different paper.

Permitted work may include substantial but bounded reframing, literature comparison, limited new experiments/baselines/ablations/robustness checks within the existing pipeline, stronger validation/error analysis, theoretical clarification, limitations/reproducibility improvements, figures/tables, and correction of unsupported claims.

If the selected journal would require a disruptive scope change, report journal-paper fit as the limitation rather than treating that change as an ordinary backlog item.

## 5. Ownership and dependencies

Classify every backlog item as:

- `ChatGPT/TeX` for manuscript-side scientific wording, structure, equations, bibliography integration, and direct manuscript assets;
- `Codex/code` for experiment code, computational analyses, validated numerical artifacts, or substantial code-repository changes;
- `Mixed` when verified code evidence must feed a manuscript change.

For `Mixed`, record dependency direction; normally code evidence precedes TeX interpretation.

Do not load code or prompting instructions during the first inventory merely because a future item may use them. Those responsibilities are loaded by `paperfit_execution.md` only when an approved batch actually needs them.

Do not invent a code repository, file path, experiment result, or command that has not been established from accessible evidence.

## 6. Build a dependency-aware prioritized backlog

Assign stable identifiers `PF-001`, `PF-002`, ... and preserve them in direct continuations even if priority changes.

Order items by hard dependencies first, then expected contribution to acceptance probability. Prioritize scientific validity, reviewer/editor risk, journal fit, evidentiary strength, and desk-rejection risk ahead of cosmetic improvement; break close ties by lower implementation cost and broader downstream benefit.

Use qualitative impact only: `critical`, `high`, `medium`, or `low`. `Critical` can independently invalidate the manuscript, create material non-compliance, or make rejection highly likely; `high` is a substantial acceptance risk/opportunity; `medium` is meaningful but non-dominant; `low` must still be worth doing. Omit negligible items.

Do not claim numerical acceptance-probability gains per item without unusually strong evidence.

## 7. Compact first-phase output

Start with exactly one section titled `Prioritized revision backlog`.

Each item must preserve all decision-relevant semantics but should not print one line for every attribute. Prefer this compact form:

`PF-### [IMPACT][OWNER] — concise action title`

Then normally use no more than four bullets:

- **Problema:** why it matters specifically for this manuscript and journal, including the affected section/evidence/figure/experiment when useful;
- **Acción:** smallest concrete change or investigation needed;
- **Dependencias:** only when not `none`, including dependency direction for `Mixed` items;
- **Tipo:** only when it materially helps distinguish manuscript-only revision, bounded new analysis/experiment, or journal-policy/compliance work.

Do not emit `Dependencias: none`, repeat impact/owner below the heading, or split location, rationale, task class, and action into separate bullets when they can be combined without ambiguity. The backlog remains authoritative and complete despite the compact presentation.

After the backlog, add only sections containing material information:

### `Journal-paper fit diagnosis`

Summarize strongest fit signals, main editorial/scientific risks, and the most plausible current rejection reasons.

### `Cross-cutting observations`

Include only patterns affecting several backlog items and not already obvious from them.

### `Evidence gaps and uncertainties`

Include only gaps that prevented a stronger conclusion or must be resolved before safe execution. Distinguish unavailable evidence from checked-but-insufficient evidence.

Do not append a generic checklist or repeat backlog recommendations in diagnostic sections.

## 8. First-phase stopping and continuation

Stop after the complete backlog and material diagnostic sections. The first invocation must not edit TeX/code, run new experiments merely to fill a suspected gap, prepare Codex prompts, commit/push/merge, submit, or contact the journal.

The backlog must be detailed enough that later work does not rerun the full journal-fit review unless the manuscript, journal, or evidence base changes materially.

After this inventory, a direct-continuation user response consisting only of `ok` authorizes **only preparation of the next revision batch proposal**. It does not authorize mutation. At that point load the indexed `paperfit_execution.md`, preserve the established manuscript, journal, evidence baseline, stable `PF-###` identifiers and statuses, prepare its `Proposed revision batch`, and stop for separate approval.

The deferred execution owner preserves the established workflow semantics without reloading them here: a selected batch does not need to be a strict prefix of the backlog; manuscript diff rendering retains removals in red, additions in green; Codex stages delegate package construction to prompting; corrective work remains within the same approved `PF-###` items; and `batch completion` returns to proposal-only state for the next isolated `ok`.
