# Prompt generation core

Use this core for every task routed to the `prompting` domain and whenever the global Codex-prompt output gate in `AGENTS.md` activates prompt generation as an additional responsibility. It owns only the behavior shared by Codex and Chat prompt generation. After applying this core, inspect `indice_prompting.csv` and select exactly one target-specific module from the resolved `target`.

## Input contract

The active request, command, or calling route establishes:

- `target`: exactly `Codex` or `Chat`, matched case-insensitively;
- `request`: the complete prompt-generation request or handoff to package.

For `#PROMPT`, use the parsed `target` and `request` arguments. When natural language or a calling instruction explicitly identifies the intended prompt destination as Codex or Chat, resolve that explicit destination as `target` without requiring `#PROMPT`. When the global Codex-prompt output gate in `AGENTS.md` activates because the response will contain Codex-targeted prompt text, resolve `target=Codex`.

If `target` is not one of those two values, return the canonical command usage when a command supplied it, or report the unresolved target to the caller when no command did. Do not silently reinterpret another target. Do not infer a target merely from generic words such as implementation, agent, prompt, code, or model when no intended destination is explicit.

## Context synthesis

**Invariant:** Treat the current conversation as working context for the prompt package. Resolve references such as “what we discussed”, “the method above”, or “implement this” from the relevant established discussion before drafting.

1. Extract only context that materially affects the requested task: objective, established decisions, technical conclusions, definitions, constraints, interfaces, repository or file references, examples, edge cases, expected outputs, and unresolved limitations.
2. Give precedence to the latest explicit user instruction when it conflicts with earlier discussion.
3. Synthesize the useful state. Do not paste or summarize the conversation turn by turn.
4. Do not invent missing facts, repository state, APIs, paths, experimental results, or decisions.
5. When a detail is genuinely unresolved and cannot be derived safely from the available context, keep the uncertainty explicit and bounded instead of fabricating precision.
6. Inspect additional sources only when they are available under the active task rules and materially resolve execution-critical uncertainty. Do not perform broad research merely to make the package longer or more impressive.

## Delivery-shape decision

**Default:** Use one prompt and no ZIP. Escalate only when another shape materially improves reliability, reduces duplicated context, lowers expected model cost, or prevents expensive reruns.

Choose the smallest useful shape:

1. **One prompt:** use when one target-model run can execute the task coherently with bounded context and verification.
2. **Two or three sequential prompts:** use only when distinct stages have a real dependency or checkpoint and separating them improves reliability or cost. Present the prompts separately in exact execution order.
3. **Supporting ZIP:** create a compact ZIP when the target benefits from persistent instructions, context, resolved design notes, reference material, examples, schemas, or other reusable files that would otherwise bloat or duplicate the prompt. A ZIP may accompany one, two, or three prompts when useful.
4. **Four or more prompts:** do not emit four or more full prompts separately in the chat. Create a ZIP containing one numbered Markdown file per prompt and a `README.md` that gives the exact order, purpose, inputs, expected outputs, and any target-specific configuration required by the selected module for each stage.

Do not split work merely because the prompt is long. Do not create a ZIP merely because artifact creation is available.

### ZIP discipline

When a ZIP is justified:

- include only files the target model is expected to read or use;
- prefer concise Markdown or text files for synthesized instructions and context;
- avoid duplicating the same context across prompt files;
- use stable descriptive names and numbered prompt files such as `01_prompt.md`, `02_prompt.md`, and so on;
- include `README.md` whenever the bundle contains multiple files, stating what to read first and the execution order;
- if a prompt depends on bundle files, name those files explicitly in the prompt;
- prefer pointing to an already accessible repository file or source over copying it into the ZIP when copying adds no execution value;
- never include secrets, unrelated conversation history, or unsupported personal/private data.

## Length discipline

**Default:** Produce the shortest prompt package that preserves execution-critical information and makes the requested result likely to succeed.

- Remove duplicated requirements, conversational filler, discarded alternatives, motivational language, and background that does not change the task.
- Prefer precise constraints and acceptance criteria over lengthy explanation.
- Use longer prompts or supporting files when the task genuinely needs substantial technical state, but never make length an objective by itself.
- Keep rationale only when it changes a decision, guards against a likely mistake, or explains a non-obvious constraint.
- Across sequential prompts and ZIP files, store shared context once whenever practical instead of repeating it.

## Output contract

**Invariant:** Return only the execution package and minimal target-specific configuration metadata needed to use it. Do not expose internal analysis, hidden reasoning, or a transcript of how decisions were reached.

**Default:** When prompt text is emitted directly in chat, render each prompt body inside a fenced Markdown code block tagged `text` (```text ... ```), not in a Writing Block or other document-style wrapper. Keep prompt labels and any target-specific configuration metadata outside the fence. This presentation rule changes only the chat rendering, not the prompt contents or delivery-shape decision.

- With one prompt and no ZIP, return the finished prompt ready to paste.
- With two or three prompts, present each prompt separately in execution order.
- When a supporting ZIP accompanies one to three prompts, provide the ZIP artifact and make every dependency on its files explicit in the corresponding prompt.
- When four or more prompts are justified, provide the ZIP artifact instead of dumping all prompts into the chat. Its `README.md` must contain the exact execution order, purpose, inputs, expected outputs, and any configuration required by the selected target module for every stage.
- Omit ZIPs, extra prompts, and configuration metadata that are not needed by the selected target.

Every prompt must be understandable in a fresh target conversation without requiring access to the original chat, except for resources that the prompt explicitly identifies as expected inputs or accessible project state.
