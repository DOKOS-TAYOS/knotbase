# Prompt generation compatibility router

Use this module only as a compatibility entry point for callers that still route prompt generation here explicitly. New indexed routing should apply `00_core.md`, inspect `indice_prompting.csv`, resolve the explicit target, and load the corresponding target-specific module directly.

1. Apply `00_core.md` first.
2. Resolve the target exactly as defined there from `#PROMPT`, the global Codex-prompt output gate, or an explicit natural-language/calling destination.
3. Load exactly one target module:
   - `Codex`: `01_codex_prompt_generation.md`;
   - `Chat`: `02_chat_prompt_generation.md`.
4. If the target remains invalid or unresolved, use the failure behavior defined by `00_core.md` instead of selecting both modules or inferring from generic words such as implementation, agent, prompt, or code.

Do not duplicate shared packaging rules or target-specific behavior here. This file is a compatibility selector only.
