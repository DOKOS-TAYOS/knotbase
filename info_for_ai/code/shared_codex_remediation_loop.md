# Shared ChatGPT-first remediation loop for intensive code audits

## Activation and ownership

Use this module only for the direct post-inventory workflow of `#BUG`, `#DEAD`, `#OPT`, and `#REFACT`. Load it after the initial inventory when the user replies with an isolated `ok`, reuse it when the user returns Codex execution output for review, and reuse it when an isolated `ok` resumes a human checkpoint created by this loop.

**Invariant:** This module owns the direct-command continuation state machine for `#BUG`, `#DEAD`, `#OPT`, and `#REFACT`. For those direct invocations, its `ok`, ChatGPT remediation, remote-publication, Codex-handoff, remote-review, checkpoint, and completion rules supersede older direct-continuation wording in the specialized audit module. The specialized module still owns finding semantics, prioritization, correction safety, measurement or equivalence requirements, verification, stopping criteria, and the technical execution contract applied to every correction.

**Invariant:** Do not activate this module merely because one of the audit modules is reused by `#FIX`, `#CYCLE`, `#REFAC`, or another delegating workflow. Those workflows retain their own authorization and execution semantics unless they explicitly select this module.

The first audit response remains inventory-only under `shared_intensive_audit.md`. Do not load GitHub integration or prompting responsibilities during that first turn solely in anticipation of later remediation.

## State 1: isolated `ok` after the inventory

**Invariant:** In the direct continuation of the same audit, a user response consisting only of `ok`, case-insensitively and ignoring surrounding whitespace, authorizes ChatGPT to continue remediation directly over the current actionable inventory. This authorization includes the in-scope code, tests, documentation, verification, and routine safe remote publication or integration needed by the selected specialized workflow. It does not authorize unrelated changes, public-contract changes outside the finding contract, protection bypasses, or unresolved human decisions.

**Invariant:** The isolated `ok` is an executable state transition, not a conversational acknowledgment. In the same assistant turn that receives it, activate this module and begin the ChatGPT-first execution below using the existing inventory. Do not reply only with an acknowledgment such as "perfect", "understood", or "OK", do not merely restate the authorization, and do not wait for another user message before starting work. If a yield condition is already true before any safe remediation action can be taken, execute the applicable handoff or checkpoint behavior in that same turn instead.

If the user adds other text, changes repository, changes objective, selects only some findings, or introduces another responsibility, interpret that message normally instead of using this shorthand.

### ChatGPT-first execution

ChatGPT should do as much of the authorized remediation as it can safely perform and independently verify with the capabilities available in the current environment. Do not delegate work to Codex merely because the inventory is large or because Codex could also perform it.

For each correction unit:

1. select the next highest-priority safely actionable finding under the specialized module;
2. apply that module's correction, compatibility, measurement, and verification contract;
3. use structured repository and GitHub capabilities directly when they can make and verify the change safely;
4. use repository-native remote CI or checks when they can provide the required evidence without a separate local execution environment;
5. inspect the task diff and preserve unrelated work;
6. publish verified task-related state through the repository's normal safe GitHub flow when publication is authorized;
7. when the current correction unit is ready for integration and remote integration is authorized, complete the repository's normal pull-request review and integration path, then freshly verify that the default branch contains the intended correction before selecting the next independent finding;
8. refresh the default branch after that integration and base the next independent correction unit on this current state. Do not create sibling task branches from the same stale base for sequential independent findings. A small tightly related group deliberately defined as one correction unit may share one branch and pull request and cross this barrier once as that unit.

A correction unit remains bounded and reviewable even when several units are completed before the next user-facing checkpoint. The absence of a user-facing checkpoint never removes the integration barrier between independent correction units. Do not stop after each small unit merely to request another `ok`, but do not advance to an independent finding merely because the previous unit was committed, pushed, or opened as a pull request.

### When ChatGPT must yield

Continue the ChatGPT-first loop until one of these conditions is reached:

- the selected audit's practical stopping criterion is satisfied;
- a material product, compatibility, security, architecture, data, or tradeoff decision requires the user;
- the next necessary implementation or verification step materially requires capabilities that are unavailable or materially less reliable in ChatGPT's current environment, such as local reproduction, repository-native execution that remote CI cannot answer, representative benchmarks, hardware-specific measurement, difficult iterative debugging, or a local artifact that must be inspected directly;
- a verified correction unit cannot cross its required integration barrier because of failing required checks, repository protections, a non-trivial conflict, unavailable integration evidence, or another blocker that must be resolved before the default branch can advance;
- continuing in the current turn would create a meaningful risk of exhausting the available reasoning or tool budget before a coherent verified checkpoint can be preserved.

**Invariant:** The last condition is a human checkpoint, not a reason to invent Codex work. Publish or preserve the safest verified current state when possible, report the exact remaining findings and next action, and stop. A later isolated `ok` resumes the ChatGPT-first loop from that remote state.

## Minimal Codex handoff

Use Codex only when a concrete next dependency satisfies the yield criteria above and Codex is the preferable execution surface for that dependency.

Whenever this module emits Codex-targeted text, apply the global Codex-prompt output gate: load `../prompting/00_core.md`, then `../prompting/indice_prompting.csv`, then `../prompting/01_codex_prompt_generation.md`.

**Invariant:** Emit exactly one Codex prompt for the minimum necessary next step. Do not create a ZIP, do not prepare a multi-stage package, and do not pre-generate later prompts that may become stale after remote review. Include the model and reasoning-effort recommendation required by the prompting contract. Prefer the cheapest reliable eligible configuration; in particular, use Luna when the prepared task is robustly within its capability and escalate to Sol only when the residual difficulty justifies it.

Before delegating, publish ChatGPT's verified current task state when safe so Codex can work from an explicit remote branch, pull request, and commit rather than reconstructing local context.

Every Codex handoff must:

- explicitly require single-agent execution with no subagents, parallel agents, background agents, agent pools, or equivalent delegation;
- identify the exact repository, current remote branch or pull request when available, relevant commit, finding or narrow dependency, and acceptance criteria;
- provide the already-established technical conclusions needed to avoid repeating the audit or broad repository exploration;
- ask Codex only for the implementation, reproduction, tests, benchmark, comparison, fine adjustment, or other execution step that ChatGPT cannot complete reliably itself;
- preserve unrelated work and the specialized audit's correction contract;
- run the repository-native checks or measurements required for that narrow step;
- commit and push verified task-related changes to the current safe work branch or pull request when a code change is needed, then freshly verify the remote state before finishing;
- avoid merging by default so ChatGPT can independently review the published result; merge only when the prompt explicitly authorizes it and the repository's normal policy makes that mechanically safe;
- stop after publishing the delegated correction or verification result; do not start a second independent finding or create another sibling task branch, because ChatGPT owns the remote review and integration barrier before remediation advances;
- return a concise execution report with the finding or dependency handled, files changed, commands and checks actually run, measurement results when applicable, commit SHA or SHAs, remote branch, pull request when present, and every blocker or unresolved issue.

If ChatGPT genuinely needs a Codex-produced file that cannot appropriately be committed, published, or represented faithfully in the execution report, Codex must return the exact path or paths the user should upload. Do not require manual file upload when remote state or concise reported evidence is sufficient.

## State 2: returned Codex output

When the user returns Codex execution output, treat it as evidence to review, not as proof of completion.

**Invariant:** Inspect the current remote GitHub state corresponding to the Codex report before accepting it. At that phase load `../github/00_core.md`, then `../github/indice_github.csv`, and the indexed GitHub integration module required for the published state. Verify the relevant commit or branch, changed files or diff, pull request when present, current checks when material, and the final remote state.

Compare the remote evidence and Codex report against the exact delegated dependency, the specialized audit contract, repository-local instructions and protections, and absence of unrelated changes.

After review:

- if a concrete problem remains and ChatGPT can correct and verify it safely with available capabilities, fix it directly, publish the corrected state when safe, and continue the ChatGPT-first remediation loop;
- if the next concrete dependency still requires Codex, emit one new minimal Codex handoff under the contract above;
- if a material human decision is required, stop at that decision and provide the minimum evidence needed to make it;
- if the Codex step passes, complete the current correction unit's integration barrier when integration is authorized and safe, freshly verify the updated default branch, and only then resume the ChatGPT-first remediation loop automatically without requiring another `ok`; if integration is blocked, stop at that blocker instead of starting the next independent finding.

Do not bounce a correction back to Codex when ChatGPT can resolve it more cheaply and reliably. Do not continue from Codex's local-only claims when the prompt required publication and the remote state does not contain the reported work.

## Manual-user fallback

Prefer ChatGPT execution first and Codex execution second. Ask the user to perform a technical action only when neither surface can perform the indispensable step safely.

When manual action is unavoidable, provide the exact minimal commands or UI action required, including the repository, branch, working directory, expected output, and what the user should return to ChatGPT. Do not give vague instructions such as "run the tests" when exact commands are known.

## Remote publication and integration

After the post-inventory `ok`, load the GitHub integration responsibility only when remote mutation or verification actually begins. Reuse an existing safe task branch or pull request when practical; otherwise create one through the repository's normal policy.

**Invariant: integration barrier between independent correction units.** For direct `#BUG`, `#DEAD`, `#OPT`, and `#REFACT`, a correction unit is not complete for sequencing purposes merely because it is committed, pushed, or represented by an open pull request. When integration is authorized and safe, complete the repository's normal integration path and freshly verify the default branch before starting the next independent correction unit. If required checks, protections, review, conflicts, or another blocker prevent integration, stop at that checkpoint rather than opening or advancing an independent sibling branch from stale history. Only a small tightly related group intentionally defined as one correction unit may accumulate on the same branch or pull request before crossing the barrier.

ChatGPT may commit, publish, update a pull request, and integrate verified in-scope corrections directly when repository protections and the specialized workflow allow it. A changed SHA invalidates prior CI evidence. Before integration, verify the current remote head, relevant checks, the task diff, and any freshness requirement. After integration, refresh the actual default branch and use that refreshed state as the base for the next independent correction.

When Codex is delegated a step, prefer continuing the same reviewable branch or pull request so ChatGPT can inspect the exact published delta and continue from it. Do not create parallel branches merely to separate execution surfaces, and do not create sequential sibling branches from the same stale default branch.

Publication stops before any action that would create material risk, including secret exposure, unresolved destructive effects, uncertain security consequences, non-trivial conflicts, unrelated or unreviewable changes, or prohibited history rewrites.

## Completion and checkpoints

After the last correction, perform a final bounded verification against the original actionable inventory and current remote state. Confirm that targeted findings are resolved or correctly reclassified, required checks or measurements are satisfactory, no material regression or unrelated change is evident, and the publication or integration state is coherent.

When the specialized stopping criterion is satisfied, report completion using the shared checkpoint presentation.

When a human checkpoint is needed only because the current ChatGPT turn should end before tool or reasoning exhaustion, report the verified remote state, corrections completed in that checkpoint, remaining finding identifiers, and the next priority. A later isolated `ok` resumes the same loop without rebuilding the audit.

## Cost and context discipline

Reuse the audit inventory, accepted decisions, prior remote verification, and current branch or pull-request state. ChatGPT should absorb problem framing, architecture decisions, remote review, simple edits, and mechanically verifiable corrections whenever its tools are sufficient.

Codex must receive only the smallest task-specific context needed for the immediate dependency. Do not make Codex rediscover findings, architecture, repository layout, or acceptance criteria that ChatGPT has already established reliably. Do not create ZIP context bundles for this workflow.

Escalate Codex model capability or reasoning effort only when the concrete delegated step justifies it under the prompting contract.
