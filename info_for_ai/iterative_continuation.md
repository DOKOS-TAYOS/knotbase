# Shared iterative continuation contract

Use this transverse contract only when a selected workflow explicitly requires it. It is not a standalone routing domain and does not define what the workflow's unit of work is, how many units exist, what each unit produces, or what authorization is needed for mutations. Consumer workflows retain those responsibilities.

## Active workflow identity

Reuse iterative state only in a direct continuation of the same active workflow and the same target resource. Do not carry state merely because a later task uses a similar command, domain, topic, or procedure.

Maintain enough state to identify the active resource, current unit, next pending unit, completed work, user constraints or corrections that still apply, and any blocker that prevents the current unit from completing. A consumer may require additional state.

## Isolated `ok`

**Invariant:** When the consumer workflow defines progressive advancement by isolated `ok`, a trimmed user message consisting only of `ok`, case-insensitively, authorizes at most exactly the next pending unit defined by that workflow. It never authorizes skipping an additional pending unit or pre-executing later units.

The consumer defines the unit: for example, one explanation batch, one editorial phase, one study unit, or one final-assembly phase. This contract does not make those units equivalent.

If no pending unit exists, an isolated `ok` does not invent a new phase, restart the workflow, or silently broaden scope.

## Native continuation button

**Default:** When a selected iterative workflow is active, one next unit is pending, the workflow currently accepts an isolated `ok`, and the ChatGPT interface supports a native action button, show one compact continuation button near the end of the response instead of making the user type `OK`. For ordinary read-only educational progress use the label `Continuar`. Make the button genuinely functional: its direct click action must synchronously submit exactly the new user message `ok` (for example, `GenUI.issueNewTurn("ok")`) into the same conversation, without additional words, prefixes, form payloads, or hidden instructions. This is a presentation convenience, not a new workflow command or authorization path.

**Invariant:** Apply the existing isolated-`ok` contract unchanged after a button click: at most one next pending unit, the same resource and active workflow, the same phase gates and mutation permissions, and no automatic progression beyond that one unit. Manually typing `OK` remains fully supported. A substantive user message, correction, or question must never be treated as a button click or silently consume the next unit.

**Invariant:** Do not offer continuation when there is no pending unit, the current unit is blocked, the workflow is no longer the same, or an additional explicit decision is required before advancing. A visible button from an earlier response can remain clickable; do not assume it encodes its original workflow identity or bypass current-state checks merely because the action sends `ok`. When a workflow's `ok` approves consequential work, use a clearly scoped action label such as `Aprobar y ejecutar este lote` only when the exact proposal and authorization are unambiguous; otherwise retain an explicit conversational approval rather than presenting a misleading generic `Continuar` button.

**Default:** If native actions are unsupported, omit the button and briefly state that an isolated `OK` continues. Do not simulate buttons with decorative text, inert UI controls, a form, or a static HTML artifact. Other actions such as `Profundizar` or `Otro ejemplo` are substantive requests, not replacements for isolated `ok`.

## Substantive user messages

A substantive correction, question, preference, or scope adjustment is not equivalent to isolated `ok`. Apply it to the current state when compatible, preserve the resulting constraints for later units, and do not consume the next isolated-`ok` advancement merely because the state was edited.

If the user explicitly asks both to handle substantive input and to advance, follow the consumer workflow's own limits for that combined action. Do not infer advancement from an ordinary correction or question.

## Blockers and state integrity

When the current unit is blocked, preserve completed work and keep the blocked unit current until the blocker is resolved or the user explicitly changes the workflow. Do not mark blocked work complete merely to enable the next unit.

When pending structure changes because of a correction or new evidence, preserve already completed unit identities or numbering whenever the consumer requires them to remain stable, and update only future state needed to keep execution coherent.