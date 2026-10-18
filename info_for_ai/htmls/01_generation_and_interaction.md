# HTML generation and interaction

Open this module when creating or revising an HTML page or self-contained web artifact. It controls implementation, responsive behavior, prose, ordinary visual design, and the general shell in which specialized interaction may run.

Apply `htmls/00_core.md` first. Load specialized modules from `htmls/indice_htmls.csv` only when their activation conditions match the task. Before delivery, always load `htmls/05_verification.md`.

When the artifact contains audience-facing stateful controls such as filters, selectors, tabs, toggles, progressive disclosure, modals, drawers, popovers, or replaceable explanatory states, load `interactive_controls.md`. Do not load it merely for presentation navigation or the presentation authoring editor, which are owned by their specialized modules.

## Efficient implementation cycle

**Default:** Produce one coherent complete implementation before making cosmetic micro-adjustments. Once that implementation exists, perform the strongest practical structural or rendered check available before entering repeated correction passes.

Collect related defects found by the same verification pass and fix them together when practical. Avoid sequences of tiny source-replacement patches when one coherent edit can address the same verified issues. Prefer the cycle `implement -> verify -> consolidate fixes -> reverify`.

Do not spend repeated passes tuning geometry speculatively before inspecting the rendered result when rendering is available. Further iterations are appropriate when verification reveals new or independent defects; the goal is to reduce speculative churn, not to avoid evidence-driven refinement.

## Default viewing scale

**Default:** Unless the user explicitly specifies another zoom level, treat `125%` browser zoom as the intended base viewing condition for desktop and laptop HTML. Size typography, spacing, navigation, diagrams, controls, and content widths so the artifact feels correctly proportioned and comfortably usable at `125%`, while remaining responsive and usable around `100%` and `150%`.

This is a design and verification baseline, not a forced browser setting. Do not try to change the user's browser zoom programmatically, and do not simulate the baseline with page-wide CSS `zoom`, `transform: scale(...)`, or equivalent global scaling that distorts responsive behavior. On narrow mobile layouts, use the normal responsive viewport rather than reproducing desktop browser zoom semantics.

## Responsive layout and robust navigation

**Invariant:** Normal reading mode must remain naturally scrollable and usable at common desktop, laptop, tablet, and mobile viewport sizes. Do not create scroll traps, frozen sections, inaccessible overflow, or keyboard navigation that prevents the browser's expected reading behavior.

- Use normal document flow for the primary reading experience. Avoid page-wide `overflow: hidden`, fixed-height content regions, or nested scroll containers unless they are necessary for a specific component.
- Prefer fluid sizing with `min()`, `max()`, `clamp()`, flexible grids, wrapping, and bounded content widths. Avoid assumptions that only work at one viewport or projector resolution.
- Account for dynamic mobile viewport units when full-height sections are useful. Do not let `100vh`-style layouts hide content behind browser chrome or make content impossible to reach.
- Interactive components must not capture wheel, touch, Space, PageUp, PageDown, or arrow-key behavior globally unless the active mode genuinely requires those keys.
- Never call `preventDefault()` for navigation keys at page scope merely to implement custom movement. If a control has focus, preserve that control's native keyboard behavior.
- Keep focus states visible and the tab order coherent. Do not make hover the only way to access essential information.
- A section may use sticky or snap behavior only when it improves comprehension and still allows the user to move through the document reliably. Prefer forgiving scrolling over aggressive scroll snapping.

Before delivery, verify at least one desktop/laptop viewport and one narrow mobile viewport. Check that the user can move from the start to the end by mouse wheel or trackpad, touch where applicable, scrollbar, and keyboard without getting stuck.

## Audience-facing prose and content voice

**Default:** Ordinary explanatory HTML does not add the `blog_writing` domain solely to obtain a prose style. Keep the text natural, connected, technically responsible, and free of slogan-like or marketing-copy rhythm using this module plus the applicable content domain. Add `blog_writing` only when the underlying deliverable is itself an article/blog or the user explicitly asks to reuse that editorial contract.

When the HTML is a class, course, workshop, training resource, or other educational artifact, the applicable `education/` instructions control pedagogical structure, learning progression, density, audience adaptation, and the role of each element. HTML may use shorter paragraphs, labels, controls, compact explanations, visual callouts, or discrete lists; prefer the representation that communicates the teaching point most clearly rather than forcing article-like prose.

Avoid a synthetic presentation-copy rhythm built from repeated rhetorical questions, slogan-like headings, abrupt one-line claims, or identical card structures. Vary sentence and paragraph length according to the idea, connect causal steps explicitly, and prefer wording that sounds natural when read aloud by a presenter or read independently by the audience.

## Visual signal-to-noise

**Default:** Every visible element should contribute to content, navigation, hierarchy, comprehension, branding, or deliberate visual composition. Remove UI chrome that does not serve one of those purposes.

**Default:** Educational and presentation HTML should read visually as teaching material, not as a marketing landing page or promotional brochure. Use hierarchy to support orientation and explanation rather than spectacle.

- Avoid oversized hero headlines, slogan-like composition, excessive centered copy, giant numbers, marketing-style eyebrow labels, or decorative emphasis whose main purpose is visual impact.
- Keep headings proportionate to the amount and role of the content. A title should identify the current concept or section without consuming a disproportionate part of the viewport.
- As a practical starting range, keep the main page title around `clamp(2rem, 4vw, 3rem)` and ordinary presentation-section titles around `clamp(1.5rem, 2.5vw, 2.25rem)`, adjusting only when the user, brand, room, or content provides a clear reason.
- Prefer document-like hierarchy, diagrams, examples, comparison structure, and whitespace over promotional hero composition.

**Default:** Card, tile, and box layouts should use the available width proportionately to the number and role of their items. Do not spread a small set of cards across an unnecessarily wide container with large empty gaps merely because a generic multi-column grid is available. When only two or three items are present, constrain the group width, widen the items, reduce the inter-item gap, or choose a different grid/flex distribution so the composition reads as one coherent visual unit. Preserve enough whitespace for clarity, but avoid sparse layouts in which connectors or empty tracks dominate the content.

- Prefer content-aware column sizing such as `repeat(auto-fit, minmax(...))`, bounded `max-width`, or explicit tracks chosen for the actual item count over fixed templates that create oversized gaps.
- For short process diagrams or sequences, let box width and connector spacing work together. A connector should occupy only the visual interval needed to express the relation, not a large fraction of the row.
- Re-evaluate spacing after responsive reflow. A layout that is balanced with four items may be too sparse with two or three, and a desktop gap that is appropriate at `100%` may become excessive at `125%` or `150%`.

**Default:** Use decorative light, glow, shine, and comparable effects sparingly and only when they serve the content, an established brand, or a supplied visual reference. Prefer restrained fills, conventional shadows, borders, spacing, contrast, and typography for hierarchy.

**Default:** Keep typography consistent across the artifact whenever practical. Prefer one primary type family and a small, coherent scale of sizes and weights rather than mixing unrelated fonts or ad hoc text styles. Reuse the same typographic treatment for the same semantic role across sections and files. Introduce an additional typeface only when it has a clear functional or brand purpose, and preserve sensible system fallbacks when the preferred font is unavailable.

**Invariant:** Use bold emphasis consistently. Equivalent semantic roles should use the same font weight across sections, components, and interactive states. Do not make one item bold merely because it is selected if equivalent selected states elsewhere use another treatment, and do not let active/inactive state changes alter text weight when that causes reflow, alignment changes, or visual instability. Use bold to encode a deliberate hierarchy or emphasis, not as an arbitrary decorative difference.

Avoid turning every paragraph into a card, adding badges without semantic value, repeating labels already implied by hierarchy, overusing pills, borders, shadows, icons, gradients, counters, ornamental metrics, or decorative containers that compete with the main message.

Decoration is allowed when it produces a coherent visual identity, rhythm, emphasis, or atmosphere. It should support the content rather than create another layer of information to parse.

Prefer a small, consistent visual vocabulary and generous spacing over many competing component styles. Reuse the same component for the same meaning across a package.
