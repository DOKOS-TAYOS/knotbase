# Chat prompt generation

Use this module only when the parsed `target` is `Chat`. Apply `00_core.md` first; this module owns only Chat-specific execution-package behavior.

Create a self-contained prompt package that preserves the relevant context, desired outcome, constraints, evidence, and requested output format while removing irrelevant conversational history.

1. Make established conclusions explicit so the target Chat model does not need the original conversation to recover them.
2. Leave genuine reasoning work to the target model when that reasoning has not already been resolved in the current conversation.
3. Do not overconstrain the target with implementation choices, assumptions, or decisions that were never established.
4. Preserve ambiguity only when it is real and useful. Bound unresolved uncertainty rather than silently choosing an interpretation.
5. Apply the shared delivery-shape, ZIP, length, and output contracts from `00_core.md` without adding Codex-specific model, reasoning-effort, local-checkout, or single-agent requirements.
