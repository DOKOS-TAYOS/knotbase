# Peer-review response workflow

## Activation and boundaries

Use this module when responding to reviewer or editor comments on an identified scientific manuscript, assessing a revision, preparing a resubmission, creating a manuscript diff, drafting a response letter, or checking readiness for the next review round.

This file orchestrates the workflow. Load only the specialized module required by the current stage:

- `peer_review/assessment.md` for comment assessment or reassessment;
- `peer_review/visual_diff.md` for reviewer-ready TeX diffs;
- `peer_review/response_letter.md` for the submission-facing response letter;
- `peer_review/readiness.md` for newly introduced weakness checks and final readiness.

Do not preload later stages.

This workflow does not replace `research` for external evidence or argument validation, `code` for implementation/experiments, or `github` for authorized remote state/actions. When reviewer work changes scientific experiment code, load `../code/experimental_scientific_code.md` and reuse its minimalism contract rather than duplicating it here.

Do not promise acceptance. Prefer the smallest credible change that fully answers a comment, but recommend larger bounded work when the evidence requires it. Avoid unrelated refactors, experiments, or manuscript rewrites.

## Inputs, evidence, and continuity

Establish when applicable:

- TeX repository plus current and originally submitted commits;
- optional code/experiment repository and relevant commit;
- complete reviewer/editor comments with grouping preserved;
- journal requirements, deadlines, rebuttal limits, and diff rules;
- accessible compilation, experiment, and validation evidence.

Keep reviewer requests, verified evidence, interpretation, proposed action, and unresolved decisions distinct. Treat unavailable repositories, commits, builds, or experiments as evidence gaps.

For multi-stage or multi-turn work where durable handoff state materially reduces re-analysis, create or update one private Markdown working note in the manuscript repository or another user-approved location. Preserve the complete reviewer text there and track interpretation, evidence, decision, required actions, status, and open questions. Do not create or rewrite this note merely for a one-shot assessment whose state is already fully contained in the current task, and never include it in submission-facing material unless requested.

## Workflow stages

### 1. Assess comments

Load `peer_review/assessment.md`. Interpret each comment, locate evidence, determine the smallest credible resolution, estimate effort when useful, and later reassess whether the concern is resolved. Do not implement an ambiguous concern as though its interpretation were established.

### 2. Prepare implementation work

Generate implementation prompts only after assessment and decisions are sufficiently resolved. The peer-review workflow supplies the task-specific payload: repository/commit context, exact reviewer concern and interpretation, bounded implementation objective, relevant evidence, acceptance criteria, validation requirements, dependencies, and any required experiment-code minimalism constraint.

When code and TeX work interact, state the dependency order; normally verified code/experiment evidence precedes manuscript text that depends on it. Generate any prerequisite files completely before handing off their use.

Whenever text will be sent to Codex, follow the global Codex-prompt gate: load `../prompting/00_core.md`, `../prompting/indice_prompting.csv`, and the indexed Codex target module. Prompt packaging, model/reasoning recommendation, no-subagents wording, ZIP decisions, and generic Codex report requirements belong there and must not be reimplemented in this workflow.

Every TeX implementation prompt that changes compiled PDF content must require the visual diff defined in `peer_review/visual_diff.md`.

### 3. Produce a visual diff when required

Load `peer_review/visual_diff.md` only when the journal, selected stage, or requested implementation requires a reviewer-ready diff between submitted and current manuscript states.

### 4. Review revised state

After reviewer-driven changes, reassess affected comments with `peer_review/assessment.md`. When preparing for resubmission, load `peer_review/readiness.md` to check only material newly introduced weaknesses and blocking mismatches.

### 5. Draft response letter

Once relevant changes are evidenced, load `peer_review/response_letter.md`. Ground every claimed change, experiment, and validation in accessible submitted/current evidence.

### 6. Final readiness

Load `peer_review/readiness.md` and issue its exact verdict only after checking consistency among comments, agreed responses, current repositories, response-letter draft, required visual diff, generated artifacts, and applicable validation evidence.
