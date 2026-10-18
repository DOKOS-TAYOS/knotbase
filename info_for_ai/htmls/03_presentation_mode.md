# Presentation mode for talks and classes

Open this module when an HTML artifact is intended to support a talk, lecture, class, workshop, live presentation, or when presentation mode is explicitly requested.

Apply `htmls/00_core.md` and `htmls/01_generation_and_interaction.md` first. Before delivery, also apply `htmls/05_verification.md`.

**Invariant:** When an HTML artifact is intended to support a talk, lecture, class, workshop, or live presentation, include a presentation mode unless the user explicitly opts out.

Reading mode and presentation mode should use the same underlying content. Presentation mode may reorganize that content into full-screen sections or slide-like steps, but it must not require a second independent copy that can drift out of sync.

**Invariant:** Presentation mode must preserve the complete audience-facing content of reading mode. Every substantive section, explanatory block, reference/resource area, final links, further-reading item, callout, and other learner-facing content that is visible in reading mode must also be reachable in presentation mode unless the user explicitly requests its omission there. Presentation mode may split, regroup, or progressively reveal that content for fit, but it must not silently drop tail sections or ancillary learner-facing material merely because they fall outside the main slide sequence.

**Invariant:** The opening cover or introductory surface of the HTML must also be the first step of presentation mode unless the user explicitly requests a different presentation opening. Entering presentation mode from the normal initial page must begin on that same cover and preserve its learner-facing title, framing, branding, and other opening elements.

**Invariant:** A cover logo or equivalent brand mark must keep a stable rendered size when presentation mode is entered at the same viewport. Preserve its aspect ratio and prevent presentation-specific layout rules from enlarging it materially; it may become smaller when necessary for fit, but should not become larger unless the user explicitly requests that treatment.

## Authoring for presentation from the source layout

**Invariant:** When presentation mode is part of the artifact, design the reading-mode section structure from the beginning so that its substantive sections can become effective presentation steps naturally. Do not first author an arbitrary long-form page and then rely on presentation-only geometry, artificial minimum heights, padding, scaling, or decorative filler to make weak sections resemble slides.

**Default:** Treat the normal HTML structure as the primary composition source. Group concepts so each major section has enough substantive material, visual structure, or explanatory progression to stand on its own when presented. Combine fragments that would otherwise produce thin, under-filled presentation steps, and split sections that are too dense to present clearly. Prefer meaningful composition through explanations, examples, diagrams, comparisons, controls, worked steps, callouts, or other pedagogically useful elements rather than adding content solely to occupy space.

Presentation mode should therefore be primarily a change in navigation, focus, visibility, and responsive arrangement of an already well-composed document. It may reflow or split content when necessary for fit, but it should not need to manufacture a different visual body for each step merely to compensate for poorly proportioned source sections.

**Invariant:** Do not make this authoring constraint global to HTML. Apply it only when this presentation module is active. HTML artifacts without presentation mode should keep the section granularity and page rhythm that best serve their own reading or interaction purpose.

## Static derivatives

When the user requests `pdf` or another static derivative, load `htmls/static_pdf_export.md`. That module owns export-state selection, static pagination, editor-chrome removal, and PDF-specific verification. Do not load those rules during ordinary presentation authoring when no static derivative is requested.

## Presentation viewport fit

**Default:** Primary teaching content should fit comfortably inside typical laptop/projector viewports, using approximately `1280x720` and `1366x768` as conservative references while remaining responsive.

**Invariant:** Presentation mode must remain legible, collision-free, and reachable as the effective viewport shrinks, including ordinary browser zoom or text scaling. At representative desktop/laptop conditions, test `100%`, `125%`, and `150%` zoom when possible, or equivalent reduced effective viewport sizes when direct zoom control is unavailable.

**Invariant:** Scrolling is a fallback for genuine content overflow, not permanent presentation chrome. If a step's meaningful content fits, no vertical scrollbar should remain. If it does not fit, prefer reflow, removal of nonessential chrome, concise progressive disclosure, hierarchy reorganization, or splitting into coherent steps before accepting deliberate vertical scrolling. Never preserve a one-screen composition by overlap, clipping, unreadably small typography, or artificial fixed/minimum container footprints.

When scrolling is genuinely required, prefer document/viewport-level scrolling so the primary scrollbar stays at the browser edge. Use nested scroll areas only for components that genuinely need independent scrolling.

Keep primary teaching content in normal flow, Grid, or Flexbox whenever practical. Geometry that can create collisions under text growth or viewport reduction is acceptable only for deliberate overlays or decoration that cannot obscure instructional content.

## Header navigation contract

**Invariant:** When presentation mode exists, use one compact top header as the canonical location for presentation controls. The header must include:

- a mode button labelled exactly `Presentar` when inactive and `Presentando` when active;
- an `Índice` button;
- previous and next controls using `<` and `>` or visually equivalent chevrons;
- a slide-position indicator between them in the conceptual form `n/m`.

**Invariant:** When previous and next chevrons are displayed inside circular controls, each glyph must be visually centered within its circle, not merely mathematically centered by incidental font metrics. Use layout centering for the control and normalize the glyph itself when needed with an icon/SVG, controlled line-height, transform, or equivalent technique. Verify the rendered result for both directions; do not assume `<` and `>` share identical optical bounds in the active font.

Keep these controls adjacent, visually stable, and available during presentation. If the same controls appear in reading mode, keep them in the same header rather than creating a second navigation pattern. The mode control may also be the explicit exit from presentation mode when its active state is clear.

## Index dialog

**Invariant:** `Índice` must open a dismissible navigation window or dialog that shows the ordered session structure, clearly indicates the current step, and lets the user navigate directly to another step.

Use sufficiently large click targets, a visible close control, and `Escape`. Selecting an item should normally navigate and close the index. If the index exceeds the viewport, its own content may scroll without trapping the page after closure.

## Keyboard and behavior

Presentation mode should:

- provide a clear enter/exit path without breaking reading mode;
- support visible previous/next controls and keyboard navigation;
- use Space, ArrowRight, and PageDown for next, and Shift+Space, ArrowLeft, and PageUp for previous, only while presentation mode is active and focus is not inside a control that needs those keys;
- support Home/End when useful and Escape to leave presentation mode unless an open modal or overlay should consume Escape first;
- avoid automatic transitions or autoplay that make the speaker wait for the interface;
- keep the `n/m` indicator synchronized after every navigation path.

Focused sliders, inputs, selects, editable fields, media controls, and other keyboard-operated widgets take priority over slide navigation.

## Presentation-specific verification

Before delivery, verify presentation mode at representative normal and reduced effective viewports under the fit contract above. Confirm navigation, index, cover, branding, interactive state, deliberate overflow behavior, parity with the complete learner-facing content of reading mode including final resources or links when present, and rendered optical centering of circular previous/next chevrons in both directions when those controls are used. Also inspect the source sectioning itself: representative presentation steps should derive from sections with sufficient substantive composition to work naturally in presentation, without presentation-only minimum heights, filler, or other geometry whose sole purpose is to make an under-filled source section look like a slide. `htmls/05_verification.md` controls the evidence/reporting discipline and does not duplicate these concrete requirements.
