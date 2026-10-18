# Codex prompt generation

Use this module only when the resolved `target` is `Codex`. Apply `00_core.md` first; this module owns only Codex-specific execution-package behavior.

## Universal applicability and cost objective

**Invariant:** Apply this module to every Codex prompt or stage, regardless of how it originated or how small it appears. There is no exemption for natural-language prompt requests, assistant-proposed corrective prompts, retry prompts, continuation prompts, one-line or localized fixes, prompts embedded in another workflow, or prompts produced without `#PROMPT`.

**Invariant:** Optimize for minimum expected total Codex consumption consistent with robust execution. ChatGPT should absorb all problem framing and technical reasoning it can resolve from the current conversation and permitted evidence before delegation. Minimize Codex-side context, repository exploration, planning, reasoning effort, number of stages, and avoidable reruns. Do not save ChatGPT work by exporting reasoning or decision-making to Codex when it can be resolved reliably before the handoff.

## Problem framing and delegation

**Invariant:** perform as much of the expensive problem framing and technical reasoning as possible before producing the prompt package. Delegate implementation and verification to Codex, not rediscovery of decisions that ChatGPT can already resolve from the conversation.

Before writing the prompt package:

1. Determine the concrete implementation objective and observable desired behavior.
2. Resolve architecture, algorithm, interfaces, invariants, edge cases, migration choices, and scope boundaries when the conversation contains enough evidence to do so.
3. Translate discussion into actionable implementation instructions. Prefer exact behavior and constraints over rationale or brainstorming history.
4. Include known relevant repositories, files, symbols, APIs, commands, tests, benchmarks, or artifacts when established. If a location is unknown, instruct Codex to locate only the minimal relevant surface rather than broadly exploring the repository.
5. State acceptance criteria and verification commands or verification behavior whenever they can be derived.
6. Preserve existing contracts and unrelated work unless the request explicitly changes them.
7. Choose the delivery shape under `00_core.md` to minimize expected total Codex consumption, including context, reasoning, exploration, and reruns. Do not add planning stages that ChatGPT can resolve itself.
8. When a ZIP is useful, move stable resolved context or instructions into the bundle so later Codex stages can consult them without repeated exploration or duplicated prompt text.

The resulting Codex prompt should normally contain only the sections that add execution value, typically some subset of objective, resolved implementation design, required behavior and constraints, relevant code or artifacts, edge cases and non-goals, and validation and acceptance criteria.

Use operational instructions rather than vague metacognitive directives. Do not repeat open-ended analysis already completed here or ask Codex to choose among alternatives that can be decided from the current context. Do not include hidden reasoning or a transcript of how the decision was reached.

## Single-agent execution

**Invariant:** Every prompt or stage whose target is Codex must explicitly instruct Codex to work without subagents. State that it must not spawn, invoke, delegate to, or rely on subagents, parallel agents, background agents, agent pools, or equivalent delegated agent workers, and that the user must not be asked to enable them.

The sole exception is a prompt whose explicit task is to execute the repository's `#CYCLE` workflow. Only in that case may the prompt permit subagents according to the loaded cyclic-workflow contract.

## Local Dokos Knowledge reuse

**Default:** When a Codex task materially benefits from Dokos Knowledge instructions, prefer reusing the user's local `dokos-instructions-knowledge` checkout instead of duplicating those instructions in the generated prompt or support ZIP.

1. Assume that a checkout normally exists directly under the current user's Documents directory as `dokos-instructions-knowledge`. Resolve the Documents directory from the execution environment rather than hard-coding a username or machine-specific absolute path.
2. Use the local checkout selectively. Do not require Codex to consult it for small, self-contained tasks when the generated prompt already supplies the execution-critical instructions and verification criteria.
3. Consultation is normally justified for complex, delicate, multi-stage, or convention-sensitive work, and whenever loading a specific Dokos Knowledge contract materially shortens the prompt, reduces duplicated context, or lowers the risk of inconsistent execution.
4. When consultation is justified, instruct Codex to read the checkout's `AGENTS.md` first and follow its indexed routing. Do not instruct Codex to scan, recursively inspect, or preload the repository broadly.
5. When the applicable Dokos Knowledge responsibility or module is already known, identify that responsibility or relevant path in the generated prompt so Codex can minimize navigation while still respecting the bootstrap and routing contract defined by `AGENTS.md`.
6. Treat the local checkout as read-only unless the user's task explicitly authorizes modifying `dokos-instructions-knowledge`. Do not instruct Codex to `git pull`, checkout, reset, clean, or otherwise synchronize or mutate the checkout merely in order to consume its instructions.
7. The target repository's own instructions retain their normal precedence over Dokos Knowledge instructions.
8. If the local checkout cannot be found or read, make that dependency explicit and require Codex to continue from the self-contained task instructions when they are sufficient, or report the missing dependency when the referenced Dokos Knowledge contract is execution-critical. Do not invent the missing contract.

## Scientific experimental code

**Invariant:** When the Codex task concerns scientific or research code whose main purpose is experimental execution, inspection, or reproduction rather than application or production software, load `../code/experimental_scientific_code.md` and carry its current scientific-experiment minimalism contract into the execution package without reimplementing that contract here.

## Codex model and reasoning recommendation

**Invariant:** For every Codex execution package, recommend the least expensive currently available Codex-capable GPT model from GPT-6 onward, together with the reasoning-effort configuration that is expected, with high confidence, to complete each stage correctly using the prepared prompt. GPT-6 is a hard minimum generation: never recommend GPT-5.x or any earlier generation, even when it would be cheaper or otherwise sufficient. Do not recommend a newer, stronger, or more expensive eligible model merely because it is available.

**Invariant:** Within the eligible GPT-6-or-newer Codex-capable GPT models, use this project cost/capability ladder for model selection: Luna is the baseline and cheapest model, Sol is the intermediate and more capable model, and Astra is the strongest and most expensive model. Evaluate eligible configurations from cheapest to most expensive: recommend Luna whenever an eligible Luna configuration is expected to complete the task robustly; escalate to Sol only when no eligible Luna configuration is expected to be sufficiently reliable; escalate to Astra only when no eligible Sol configuration is expected to be sufficiently reliable. If a cheaper eligible tier can safely complete the prepared task, choosing a stronger tier is not justified.

**Default:** The operational sensitivity or irreversibility of an action does not by itself require a stronger model when the task is mechanically simple, tightly specified, and protected by explicit preflight and verification steps. Escalate model capability for residual cognitive difficulty, ambiguity, subtle integration, difficult debugging, algorithmic or numerical correctness, concurrency, architecture-heavy changes, or another concrete reason that makes the cheaper tier materially less reliable.

1. Treat current model availability, Codex compatibility, and supported reasoning-effort values as time-sensitive. Reuse qualifying verification already established in the current conversation when it comes from current official OpenAI documentation on the current local date and directly supports the needed facts. Otherwise verify only the missing facts once in a bounded pass against current official OpenAI documentation, then reuse them across the package. Do not repeatedly re-verify equivalent facts per stage.
2. The Luna < Sol < Astra cost/capability ordering above is a project-level operating assumption and does not require a fresh pricing lookup for every prompt. Verify current official pricing only when quoting exact prices, when a concrete product change casts doubt on this ordering, or when another pricing fact is necessary to choose safely.
3. Evaluate capability bottom-up rather than top-down. If the prepared prompt makes Luna clearly robust enough, stop there; do not compare Sol or Astra merely to find a theoretically better performer. Use Sol for work whose remaining complexity materially exceeds Luna's comfortable margin. Reserve Astra for cases where Sol itself lacks a reliable margin or where a demonstrated capability requirement makes Astra necessary.
4. Typical Luna candidates include tightly specified bounded edits, routine documentation work, straightforward repository administration, simple CI or review follow-ups, and other tasks where ChatGPT has already resolved the hard decisions. Typical Sol candidates include ordinary multi-file implementation, moderate integration work, nontrivial debugging, or broader repository reasoning. Astra is for exceptional high-complexity work such as subtle algorithms, difficult numerical or concurrency correctness, architecture-wide reasoning, or hard debugging that still remains unresolved after prompt preparation. These examples are guidance, not a substitute for the bottom-up reliability test.
5. Choose reasoning effort independently for each stage and use the lowest supported effort that is still expected to be robust: normally low for tightly specified or mechanical work, medium for ordinary multi-file or integration work, and high for subtle algorithms, numerical correctness, concurrency, architecture-heavy changes, or difficult debugging. Use any effort above high only when supported and clearly justified.
6. Because ChatGPT should resolve major framing and design decisions before delegation, reduce both model tier and reasoning effort whenever the resulting prompt makes a cheaper configuration reliably sufficient.
7. If multiple prompts have materially different complexity, recommend model and reasoning effort separately for each stage while still applying the same cheapest-reliable-first rule.
8. If current availability or Codex compatibility cannot be verified when verification is required, do not invent support. Recommend only among GPT-6-or-newer configurations whose required availability is established, and state the limitation compactly. If no qualifying GPT-6-or-newer Codex-capable GPT configuration is currently established as available, state that compactly and do not fall back to GPT-5.x or any earlier generation.

## Codex output metadata

**Invariant:** Whenever a Codex prompt is displayed directly in chat, put its complete paste-ready body in a fenced Markdown code block tagged `text` (the copyable plain-text block). Immediately below the closing `text` fence, outside the prompt block and before any explanation, display the concrete model and reasoning effort on one line. For Spanish responses, use this exact presentation pattern, substituting the selected verified configuration:

Configuración recomendada: **GPT-6 Luna, razonamiento Low**.

**Invariant:** Render this recommendation as extra-small, subdued secondary text, never as a default-size paragraph or heading. When supported by ChatGPT, use a native text component with `size="xs"` and `color="secondary"`, keeping the model and effort in bold. Use an equivalent small-caption style when necessary. Never display component markup as literal text. Keep the model name and reasoning level together in **bold**, but leave the label unbolded. Do not put the recommendation inside the Codex prompt, separate it from its prompt with a heading, or replace the concrete values with generic tier names. If a brief justification or availability qualification is needed, put it after this recommendation without displacing the line.

- With one prompt and no ZIP, show the recommendation immediately under its `text` block.
- With two or three prompts, repeat this exact block-then-recommendation layout for each prompt, using its own selected configuration.
- With four or more prompts packaged in a ZIP, keep the paste-ready prompt files free of configuration metadata; in `README.md`, place the same bold configuration line immediately below each stage's prompt-file reference, alongside the execution order required by `00_core.md`.
- For non-Spanish user-facing output, translate the label and `razonamiento` naturally while preserving the placement, bold span, and concrete model and effort.
