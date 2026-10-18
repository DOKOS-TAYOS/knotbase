# Peer-review comment assessment

## Activation

Load this module when the task is to interpret reviewer or editor comments, determine what evidence addresses them, define the smallest credible resolution, or reassess whether individual comments are resolved in the current manuscript.

Use the parent `../01_peer_review_response.md` workflow for shared inputs, repository boundaries, evidence discipline, implementation ordering, and durable-state rules.

## Comment identity and quotation

Preserve the complete reviewer/editor text in the supplied source and in any durable working note required by the parent workflow. For chat output, assign stable identifiers such as `R1-C1`, `R1-C2`, or `ED-C1` and normally use only a short identifying excerpt or concise paraphrase of the request. Reproduce the complete comment only when exact wording is materially necessary to interpret ambiguity, defend a decision, draft submission-facing text, or the user asks for it.

Never let output compaction weaken the assessment: each status must still be grounded in the full comment and verified manuscript/code evidence.

## Initial assessment

Return one section per reviewer/editor and one compact item per comment. Each item must preserve these semantics without requiring one separate field for each:

- **Interpretation:** literal request plus the underlying concern, including material uncertainty;
- **Evidence:** precise submitted/current manuscript or code/experiment evidence;
- **Resolution:** the smallest credible manuscript, code, or experimental action and why it is sufficient;
- **Scope:** implementation owner/dependencies, material risks or invariants, and effort (`simple`, `moderate`, or `substantial`) when it helps planning.

Prefer three or four compact bullets per comment. Combine scope and effort when straightforward; omit an effort label when it adds no decision value. If a textual clarification cannot support the claim, state the additional evidence or experiment actually required.

Maximize credibility, not diff size.

## Resolution assessment

Assess each comment against the current version using exactly one status:

1. **Completely resolved:** output the stable identifier, status, and only enough excerpt/context to identify the comment. Do not repeat analysis once verified.
2. **Resolved with caveats:** identify the comment compactly and state only the remaining qualification or wording needed.
3. **Partially resolved:** identify it compactly, separate what is already addressed from what remains, and give the smallest next step.
4. **Unresolved:** use the compact initial-assessment semantics above.

Do not classify a comment as completely resolved merely because the manuscript mentions the topic; locate evidence that it addresses the full reviewer concern.
