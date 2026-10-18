# PAPERFIT iterative execution contract

## Activation

Load this module only after `04_journal_targeted_review.md` has produced the first `Prioritized revision backlog` for the same manuscript and target journal and a direct continuation advances into batch proposal or execution.

Reuse the established manuscript, journal, verified evidence, stable `PF-###` identifiers, priorities, dependencies, owners, and completed/pending state. Do not rerun the complete journal-fit review unless the manuscript, target journal, or evidence base changed materially.

## State and authorization

The iterative states are:

1. `batch proposal` / `awaiting approval`;
2. `approved batch execution`;
3. `awaiting Codex evidence` when code work exists;
4. `batch completion`.

An isolated `ok` has state-dependent meaning:

- immediately after the first inventory or after a completed batch, it authorizes preparation of exactly the next batch proposal and **no mutation**;
- while `awaiting approval`, it authorizes exactly the displayed batch and the minimum corrective iterations needed to satisfy those already stated `PF-###` acceptance criteria.

If the user changes, removes, or adds proposed items before approval, rebuild the proposal and require a new `ok`. Approval never expands to unrelated backlog items, disruptive changes to the paper's identity, merging code branches, journal submission, or editor contact.

## Select one coherent safe batch

Choose the amount of work that is safe and useful to execute and verify together; there is no fixed item count and a batch need not be a strict prefix of the backlog.

Group items when shared manuscript surfaces, evidence, experiments, code paths, or hard dependencies materially reduce duplicated work. Preserve dependency correctness: never schedule a dependent item before an unresolved hard prerequisite, and do not combine unrelated high-risk changes merely for throughput.

Among equally executable items, prefer acceptance impact and shared context over numerical backlog order. Keep the batch independently reviewable and attributable if something fails.

## Compact batch proposal

Before any mutation, start with `Proposed revision batch` and list selected items in execution order.

Prefer one compact block per item:

`PF-### [OWNER] — title`

- **Problema/Afecta:** current weakness or acceptance risk plus the relevant claims, sections, figures, experiments, code surfaces, or evidence chain;
- **Acción:** smallest concrete modification or investigation planned now;
- **Dependencia:** only when it changes execution order.

Do not repeat impact, background, or backlog text already established unless it materially changed. Explain at batch level why non-contiguous items were grouped only when that choice would otherwise be surprising.

Stop after the proposal and wait for approval.

## Execute one approved batch

### Partition by owner and dependency

After approval, partition selected items into:

- unblocked `ChatGPT/TeX` work;
- `Codex/code` work;
- TeX work blocked on verified code/experiment evidence.

Execute independent TeX work without waiting for unrelated code work. For `Mixed` items, never write numerical results, interpretations, figures, tables, or claims until the required evidence has been verified.

### Manuscript-side changes

Use the smallest manuscript change that credibly resolves each approved item. Reuse the minimal-resolution discipline from `peer_review/assessment.md` without loading unrelated peer-review stages.

Preserve unaffected wording and structure; avoid opportunistic prose polishing, global terminology cleanup, unrelated refactoring, or invented citations/results/requirements. Compile or otherwise validate the manuscript whenever applicable tooling is available.

If the approved batch changes compiled manuscript content, load `peer_review/visual_diff.md` at that stage only. Apply its rendering contract with one PAPERFIT-specific baseline: compare the manuscript state at the start of the approved batch against the final revised state. Keep that baseline immutable through the batch and maintain one cumulative diff if TeX changes occur both before and after code work.

### Codex/code work

When approved items require scientific experiment code, load `../code/experimental_scientific_code.md` only then and preserve its minimalism contract.

Whenever an execution package for Codex is needed, follow the global Codex-prompt gate directly: load `../prompting/00_core.md`, `../prompting/indice_prompting.csv`, and the indexed Codex target module `../prompting/01_codex_prompt_generation.md`. Do not route through the compatibility router and do not recreate prompt-count, ZIP, model/reasoning, no-subagents, or generic report-format rules here.

Supply prompting with only the PAPERFIT-specific execution context it needs:

- approved `PF-###` items and explicit exclusion of unapproved backlog work;
- resolved scientific objective and dependency context;
- relevant repository evidence and paths already established;
- concrete acceptance criteria and experiment/test/validation requirements;
- authorization to commit and push verified code changes to a safe work branch when remote publication is available, with **no merge**.

Execute at most one Codex stage at a time. A packaged later stage is not evidence that an earlier one succeeded.

### Verify Codex evidence

When Codex output returns, inspect enough of the actual repository, commit, artifacts, tests, or experiment evidence to determine whether the approved items and acceptance criteria were satisfied; do not accept the report at face value when direct verification is available.

If work is incomplete, incorrect, or insufficiently validated, generate the smallest corrective Codex package that remains within the same approved `PF-###` items and criteria. No new `ok` is needed for such a correction. Require a new proposal and approval if the remedy would add a backlog item, materially change the approved scientific work, or introduce a different experiment family.

Do not mark a code-dependent item complete until its relevant evidence is verified.

### Apply dependent TeX work

Once code/experiment evidence is verified, automatically complete TeX work in the same approved batch that depended on it. Use only verified artifacts/results, update the cumulative visual diff when applicable, recompile/revalidate, and keep claims proportionate to the evidence.

## Complete the batch

A batch is complete only when every selected item is either resolved and verified within approved scope or explicitly blocked by evidence/decision that requires new input or expanded scope.

Report concisely:

- completed/blocked `PF-###` identifiers;
- material manuscript changes and visual-diff status when applicable;
- manuscript compilation/validation result;
- for code work, verified branch/commit and only the material experiment/validation evidence;
- any changed dependency affecting remaining backlog work.

Do not repeat unchanged backlog items or earlier diagnosis. State that the batch is complete; a later isolated `ok` prepares the next proposal only and does not auto-execute it.

Across batches, preserve stable identifiers/status, do not silently reopen completed items without new material evidence, never merge Codex work branches, never submit/contact the journal, and do not broaden the paper's central topic, objective, core contribution, or research programme.
