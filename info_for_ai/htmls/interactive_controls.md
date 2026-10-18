# Stateful HTML controls and reversible interaction

Open this module only when an HTML artifact contains audience-facing stateful controls such as filters, selectors, tabs, toggles, progressive disclosure, modals, drawers, popovers, replaceable explanatory states, or comparable content interaction that is not already fully owned by another selected specialized module.

Apply `htmls/00_core.md` and `htmls/01_generation_and_interaction.md` first. Before delivery, also apply `htmls/05_verification.md`.

Do not load this module merely because presentation navigation or the presentation authoring editor exists; `03_presentation_mode.md` and `presentation_editor.md` own those specialized controls. Load it when the learner-facing content itself adds stateful interaction beyond those surfaces.

## Interactivity threshold

**Default:** Add interactivity only when it changes what the user can understand, compare, inspect, simulate, control, or reveal meaningfully. Static content is preferable when interaction does not add explanatory value.

For every proposed interactive element, be able to state the concrete question it helps answer. Good uses include parameter exploration, before/after comparison, simulation, meaningful filtering, progressive disclosure of secondary detail, spatial manipulation, or stepping through a process whose states matter.

Do not add controls merely to make the page look interactive. Avoid decorative toggles, counters, arbitrary tabs, hover trivia, meaningless click targets, novelty animations, or interactions that reveal information that would be clearer if shown directly.

Keep interactive state understandable, reversible, and resettable when state changes could confuse the user. Do not hide essential content behind interaction unless progressive disclosure has a clear pedagogical or usability purpose.

## Functional filters, selectors, and state controls

**Invariant:** A visible filter, selector, tab, toggle, or state button must produce the user-facing change its label implies. Never ship a control that only changes its own active styling while leaving the intended target content unchanged.

**Invariant:** When several visible controls represent mutually exclusive or selectable states, the current selection must remain immediately distinguishable after interaction. The selected control must use a persistent, clearly contrasted visual treatment that includes a meaningful change in color, fill, or surface relative to unselected controls; subtle hover-only, focus-only, or near-identical shades are not sufficient. For ordinary selectable buttons, do not add a checkmark, tick, or equivalent success-looking glyph merely to indicate selection. Selection is a state, not evidence that the selected answer or option is correct. Keep the visual selection synchronized with the actual interaction state and its `aria-pressed`, `aria-selected`, or equivalent semantic state.

**Default:** When the options themselves carry meaningful semantics and doing so improves comprehension, choose the selected color from the meaning of the option rather than applying one generic active color to every choice. Within the artifact's visual system, prefer a green-family treatment for correct, recommended, successful, or safe states; a red-family treatment for negative, incorrect, prohibited, or dangerous states; an amber/orange-family treatment for warning, caution, conditional, or intermediate-risk states; and a neutral or brand color for states that are merely categorical or selected without positive/negative meaning. Adapt the exact tones and contrast to the HTML's palette and context. Do not force semantic colors when the options have no such meaning, and do not imply correctness merely because an option is currently selected.

- For filters, change the actual visible item set, grouping, count, or view as intended. An `All`, reset, or equivalent neutral state must restore the complete applicable set.
- Use one explicit source of truth for the interaction state and derive both control styling and target-content visibility from that state.
- Test every filter, selector, tab, toggle, or state option at least once, including switching away from and back to the initial state. Verify the actual rendered result together with the persistent visual selection and semantic state; confirm that hidden content remains hidden under the final styles and that hover or focus does not masquerade as selection. When practical, exercise cases that produce one item, several items, and no items or a clear empty state.

## Stable interactive layout and reversible UI

**Invariant:** User interaction must not make unrelated content visibly jump, shake, or shift when changing between equivalent states. This applies in reading mode and, when the presentation module is active, in presentation mode as well.

When several controls replace one explanatory panel with another, design the component so the surrounding layout remains geometrically stable. Prefer, as appropriate:

- reserving enough space for the largest expected state;
- rendering alternative states in the same grid area or bounded panel footprint;
- keeping control rows, headings, navigation, and neighboring content at fixed positions while only the intended content region changes;
- using consistent padding, borders, line-height, button dimensions, and panel structure across states;
- avoiding animations that introduce reflow, delayed height changes, or decorative motion without pedagogical value.

Do not solve layout stability by clipping meaningful content. If alternatives differ greatly in length, redesign the content, split the interaction into smaller states, or use a deliberate bounded detail area whose behavior is obvious to the user.

**Invariant:** Anything presented as dismissible, temporary, modal, overlaid, expanded, or opened on top of other content must also have an unambiguous way to close or reverse it. Modal dialogs, drawers, popovers, index windows, expanded details, and similar components must not leave the user trapped in an intermediate state.

- Provide a visible close control whenever the UI metaphor implies a window, overlay, drawer, or modal.
- Support `Escape` for modal or overlay-style components when focus is not inside a control that needs the key.
- Restore focus sensibly after closing a modal or overlay.
- Allow toggled or expanded states to be collapsed again when the user may reasonably need to return to the previous view.
- Outside-click dismissal may be added when appropriate, but it must not be the only closing mechanism.
