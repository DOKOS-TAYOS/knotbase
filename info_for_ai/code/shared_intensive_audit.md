# Shared intensive-audit contract

## Activation

Load this module only when the selected workflow is the bug audit, dead-code audit, performance audit, or refactoring audit. It owns the mechanics shared by those first-inventory audits and later bounded batches. The specialized module still owns its audit surfaces, evidence thresholds, practical-scope exclusions, finding semantics, severity semantics, correction authorization, measurement or equivalence requirements, and stopping rules. For user-facing presentation, specialized field lists define semantic information requirements rather than a mandatory one-bullet-per-field layout; the compact presentation rules in this module control how that information is rendered.

## Initial inventory state

**Invariant:** The first response is inventory-only. Do not modify files or remote state during the initial audit. Ephemeral local measurement artifacts are allowed only when the selected specialized module explicitly permits them.

**Invariant:** The initial inventory is a comprehensive audit result within the practical supported scope, not a sample, shortlist, top-N report, or collection of the first findings discovered. Report every materially supported finding reached through the required coverage process, subject to the specialized module's evidence rules.

**Invariant:** Finding count is never by itself a stopping criterion. Do not stop because several strong findings have already been identified. Discovery of the first actionable findings does not establish audit completion; coverage saturation does.

## Coverage depth

**Invariant:** Maintain an internal coverage ledger during the initial audit. For every audit surface required by the specialized module, establish one of three states before finalizing the inventory: meaningfully inspected, demonstrated not applicable, or blocked by a concrete access, environment, data, hardware, or verification limitation. A keyword search, one representative file, or one successful test is not sufficient coverage of a substantive surface when other relevant paths remain unexamined.

**Default:** Build repository coverage incrementally. Start from a bounded top-level listing, then inspect only materially relevant source, test, benchmark, configuration, documentation, and integration directories at the depth needed by the selected audit. Prefer several bounded directory listings over one oversized recursive repository tree that may include irrelevant material or be truncated. Request a complete recursive tree only when the repository is demonstrably small or the full tree is specifically needed to establish coverage.

**Default:** Minimize redundant evidence acquisition while preserving coverage. For files large enough that a full read is likely to truncate, prefer bounded line-range reads or other scoped retrieval over repeated full-file reads. When variants or generated copies are substantially duplicated, inspect one representative implementation deeply, then use focused comparison or search to inspect divergences and repeated defect patterns in the others; do not reread equivalent blocks without a concrete evidence need. Do not clone or create a local checkout merely to mirror content already available through structured remote reads; use local execution or checkout only when it materially improves reproduction, measurement, testing, or another verification step required by the active audit.

**Default:** Use complementary discovery techniques when they can expose materially different classes of findings. Searches, metrics, profiles, reference counts, or one successful execution identify candidates; they do not replace the evidence standard or coverage depth defined by the specialized module.

**Invariant:** After the primary coverage pass, perform a saturation pass from a different angle over high-risk, weakly inspected, cross-cutting, and previously uncovered areas. Revisit assumptions created by the first findings and inspect adjacent consumers, callers, configurations, tests, error paths, repeated patterns, and integration boundaries when they can expose distinct issues.

**Default:** For a repository that is not demonstrably tiny or single-purpose, if fewer than 10 supported findings are discovered after the primary coverage pass, perform at least one additional independent deepening pass before producing the inventory. If fewer than 20 findings have been discovered and substantive applicable surfaces remain only shallowly inspected, continue auditing those surfaces before responding.

**Invariant:** The numerical thresholds above trigger additional audit effort only. Never invent, split, duplicate, exaggerate, weaken the evidence standard for, or reclassify findings merely to reach a count. Once the required coverage and saturation work is complete, any resulting count is valid, including zero.

**Default:** When many valid findings exist, preserve inventory breadth. Compress repetitive explanation and shared verification context before omitting supported findings merely to keep the response short. Do not hide lower-severity valid findings simply because higher-severity findings already make the report useful.

## Shared initial-inventory presentation

Keep the audit readable while minimizing repeated metadata:

1. Start with `AUDITORÍA`.
2. Use at most one concise unlabelled context paragraph, and include it only when verification, environment, workload, repository state, or a concrete limitation materially changes how the result should be interpreted.
3. Add one compact line beginning exactly with `Resultado:` that summarizes finding counts by the specialized module's severities, distinguishes validation or inconclusive states when material, and states compactly that the initial inventory did not mutate files or remote state.
4. Add a specialized coverage summary only when the selected module explicitly requires it or when blocked, not-applicable, or weakly verified surfaces materially affect confidence in the inventory.
5. Emit non-empty severity sections in the exact order defined by the specialized module. Omit empty severity sections. `LOW` is the final section in the severity order and, when present, ends the initial response; otherwise the final emitted severity section ends the response. If there are no findings at all, end after `Resultado:` with one short `Sin hallazgos accionables.` statement.

### Compact finding layout

**Invariant:** Format findings for scanning. Each finding starts with its numbered identifier and short title. Keep a blank line between findings.

**Invariant:** Preserve all decision-relevant semantics required by the specialized module, but do not mechanically emit one bullet for every named field. Consolidate adjacent fields when doing so preserves the evidence, practical consequence, execution boundary, and uncertainty needed to understand or act on the finding. Use no more than four bullets by default; exceed that only when an additional field materially changes the decision or safe implementation path.

Use these defaults unless the specialized module genuinely requires more:

- Always retain a precise `Ubicación:` when one exists.
- Retain `Evidencia:` or an equivalent measurement/problem statement sufficient to support the finding.
- Retain the practical consequence or execution-relevant interpretation, normally as `Impacto:`, `Medición:`, `Problema:`, or an equivalent workflow-specific line.
- Omit `Estado: open` in an initial inventory. Surface a non-default state only when it changes actionability, preferably as a compact tag in the finding heading or the relevant evidence line.
- Omit a separate `Tipo:` when the identifier, title, or evidence already makes the class clear. Surface `probable`, `requires validation`, `inconclusive`, or another decision-relevant class compactly when needed.
- Omit `Confianza:` when confidence is high and the evidence already supports the claim. State material uncertainty only when it changes priority, actionability, or verification requirements.
- Omit `Condición:` when the trigger is already clear from `Evidencia:`, `Impacto:`, workload, or location. Keep it only when the finding would otherwise be overgeneralized.

Workflow-specific compaction defaults:

- Bug audit: prefer `Ubicación`, `Evidencia`, and `Impacto`; fold the realistic trigger into evidence or impact unless it needs separate emphasis.
- Dead-code audit: prefer `Ubicación`, `Evidencia`, and one `Impacto` line combining maintenance cost with removal risk when that risk is material.
- Performance audit: combine workload, metric, baseline, repetitions/statistic, and measurement method into `Medición:`. Keep separate `Evidencia:` only for an unmeasured validation candidate or when measurement alone does not explain the bottleneck. Add a compact improvement hypothesis only when it is materially useful for the next action.
- Refactoring audit: combine structural problem, evidence, maintenance impact, and frequency/scope into `Problema:`; combine proposal, expected change surface, and minimum scope into `Dirección:`; combine material change risk, contracts to preserve, and required equivalence checks into `Guardas:` or `Verificación:` as appropriate.

## Shared bounded-batch presentation

**Invariant:** Every authorized post-inventory checkpoint reports only the batch just executed since the previous checkpoint plus the minimum remaining-state context needed for the next step.

When `shared_codex_remediation_loop.md` executes several bounded correction units before yielding control, treat the current ChatGPT turn as one checkpoint report. Aggregate only those executed units; do not force one user-facing response or one additional `ok` per correction unit.

Start directly with `Resultado:` unless one short sentence is genuinely needed to disambiguate the batch. Then use only the sections that carry material information:

- `Resultado:` with the outcome, remaining state, and final local/remote state relevant to that batch;
- `Cambios:` with concise bullets for the findings and files actually changed;
- any specialized evidence section required by the module, such as `Medición:`;
- `Verificación:` with only checks actually run and their outcomes;
- `Pendiente:` only when useful for remaining identifiers, counts, blockers, or next priority.

When the specialized stopping criterion is reached, state it in `Resultado:` or `Pendiente:` within the same layout. Do not repeat unchanged repository context, audit methodology, or previously reported findings in later batches.
