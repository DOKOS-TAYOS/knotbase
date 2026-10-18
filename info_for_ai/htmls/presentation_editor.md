# Presentation editing layer

Open this module whenever `htmls/03_presentation_mode.md` is active, or when the user explicitly asks for an editable post-generation HTML surface for presentation material.

Apply `htmls/00_core.md` and `htmls/01_generation_and_interaction.md` first. When presentation mode is present, also apply `htmls/03_presentation_mode.md`. Before delivery, apply `htmls/05_verification.md` and `htmls/presentation_editor_verification.md`.

## Activation and purpose

**Default:** Presentation-oriented HTML should include a lightweight authoring layer for last-mile refinement unless the user explicitly opts out, asks only for a clean final artifact, or the requested output is a static derivative that cannot meaningfully preserve editing.

The editor is for small human corrections after generation, not for replacing the HTML layout system with a visual page builder. It should let the user correct wording, typography, alignment, bounded position, selected element sizes, palette values, and replace designated images without returning to the AI for ordinary micro-adjustments.

**Invariant:** The editor-enabled HTML and presentation mode must operate on the same underlying audience content. Do not create a second editable copy of headings, paragraphs, images, or slides that can drift out of sync with the reading or presentation surface.

**Invariant:** Treat the editor-enabled source as an authoring artifact and the clean saved/exported HTML as the audience-ready derivative. The minimal `Editar` launcher and editor chrome are a deliberate exception to the ordinary audience-only cleanliness rule while working in the editable source; they must not appear in the clean derivative.

The authoring layer is also an explicit utility exception to the pedagogical interactivity threshold in `01_generation_and_interaction.md`: its value is efficient refinement rather than explanation. This exception does not authorize decorative controls or unrelated interface chrome.

## Canonical implementation resource

**Invariant:** Use the registered asset `presentation-editor-html-base` as the canonical technical reference for the editing runtime. Resolve that exact ID through `assets_for_ai/indice_assets_lookup.csv`, then read only the indicated canonical row of `assets_for_ai/indice_assets.csv`; do not open `info_for_ai/RECURSOS_OPCIONALES.md` as an intermediate step when the required asset ID is already known.

Treat that asset as an implementation and interaction reference, not as a visual-content template. Preserve the presentation's own design, section structure, branding, controls, prose, diagrams, and content. Reuse or adapt only the editor runtime and its explicit editability contract.

**Default:** Prefer transplanting the editor-owned runtime marked by `data-editor-runtime` together with the required `data-edit` metadata patterns. Do not copy the demonstration presentation content, demo layout, or presentation controls from the canonical asset merely to obtain the editor.

Do not duplicate the complete canonical editor source inside instruction files. If the canonical asset evolves, future HTML generation should follow the current registered asset together with this behavioral contract.

## Explicit editability contract

**Invariant:** Only elements intentionally marked as editable may be modified by the authoring layer. Use explicit metadata such as `data-edit` capabilities rather than inferring editability from arbitrary DOM structure.

The canonical capability vocabulary is:

- `text`: edit the element's textual content directly;
- `font-size`: adjust typography within explicit or safe bounds;
- `align`: choose left, center, right, or justified text alignment when meaningful for that text block;
- `move`: apply a bounded horizontal and vertical offset for last-mile positioning;
- `size`: adjust a supported element dimension, normally width, within bounded limits;
- `image`: replace a designated image with a user-selected local image.

Capabilities may be combined on one element. Expose only controls that are valid for the selected element.

**Default:** Mark the content people are likely to refine manually, such as principal titles, section headings, explanatory text blocks, captions, important callouts, selected cards or containers, logos, and meaningful images. Do not mark every DOM node merely because it can technically be edited.

## Editor activation and closed state

**Invariant:** An editable source must provide a clear, discoverable control for opening the editor, normally labelled `Editar`, and an unambiguous way to close it.

**Invariant:** Keep the editor closed by default. While closed, its runtime must not resize or reflow the reading or presentation surface, capture ordinary pointer or keyboard input, or otherwise change the learner-facing geometry. Only the explicit launcher may remain available as authoring chrome.

Opening the editor should use a floating or overlay surface rather than permanently reducing the presentation viewport. Closing and reopening the editor must preserve the current unsaved edit state during the same page session; closing is not a reset action.

## Text editing and alignment

**Invariant:** A text element with the `text` capability must become normally editable after selection. A single normal click must be sufficient to place or preserve the caret and type continuously; the user must not need to hold the mouse button, repeatedly reselect the element, or fight selection logic while typing.

Keep editor selection logic from resetting `contenteditable`, focus, or the browser selection on every click inside the currently selected text element.

**Invariant:** Direct text editing is content editing, not arbitrary HTML authoring. Prevent rich-text paste or other browser editing behavior from injecting uncontrolled markup into an element. Prefer plain-text paste or equivalent sanitization, and preserve the intended semantic structure of the surrounding HTML.

**Default:** Apply direct `text` editing primarily to leaf-like text blocks. Do not make a container directly text-editable when it contains links, equations, code, interactive descendants, or important inline markup that ordinary `contenteditable` operations could destroy. Mark safer child text nodes separately or use a structure-preserving editing path.

For headings, labels, captions, and other semantically single-line roles, do not let Enter create arbitrary nested block structure. Allow multiline text only where the original semantic role supports it.

For `font-size`, constrain changes to a range that preserves legibility and the intended hierarchy. Prefer element-specific bounds when the semantic role has known limits.

For `align`, provide persistent left, center, right, and justified states when they are meaningful. Keep the visible control state synchronized with the actual computed alignment.

## Position and size

**Invariant:** Movement is a refinement offset, not a replacement layout model. Keep the element in normal document, Grid, or Flexbox flow and apply bounded relative translation or an equivalent reversible offset. Do not convert editable presentation content to arbitrary absolute positioning merely to support movement.

Use movement ranges small enough for last-mile composition changes and expose a clear way to return the selected element to its original position. Moving one item must not unexpectedly reconfigure unrelated sections.

**Invariant:** Do not destroy a pre-existing transform, animation, or positioning behavior when adding edit offsets. Compose movement through dedicated CSS custom properties, a safe wrapper, or another mechanism that preserves the element's original visual transformation semantics.

For `size`, use bounded controls appropriate to the element. Prefer proportional width or similarly stable dimensions over unconstrained arbitrary geometry. Preserve image aspect ratio unless the user explicitly requests cropping or distortion.

Because manual movement and resizing can create collisions, the generated starting layout must already be valid before editing. The editor is not an excuse to leave unresolved layout defects for the user.

## Palette and images

**Default:** Expose a small semantic palette backed by CSS custom properties, such as page background, surface, primary text, secondary text, primary accent, and secondary accent. Changing the palette should update the existing design system rather than patching unrelated individual colors throughout the DOM.

For `image`, allow a local image to replace the selected designated image. When the artifact is meant to remain a single self-contained HTML file, embed the chosen image in the document so the saved result does not depend on the original local file path. Preserve useful existing alternative text unless the replacement changes its meaning and the user supplies or requests a new description.

Do not make image replacement depend on a server, upload endpoint, or network connection when the surrounding HTML is expected to work from `file://`.

## Editor state and presentation interaction

**Invariant:** Editor controls, editable fields, sliders, file inputs, and active text editing take keyboard priority over presentation navigation. Presentation shortcuts must not fire while the user is operating those controls.

Changes made in the editor must remain visible when the user closes and reopens the editor, navigates between presentation steps, or toggles between reading and presentation modes during the same page session. Do not require persistence across a full browser reload unless the user explicitly requests it.

Provide clear recovery actions for the selected element and the complete edit state. At minimum, a user must be able to reset an edited element and reset all authoring changes without reloading or manually reversing every property.

The editor UI is authoring chrome, not learner-facing content. Keep it visually distinct from the presentation and ensure it is absent from the clean saved artifact.

## Clean final export

**Invariant:** `Guardar HTML final` or the equivalent final-save action must serialize the current edited state into a self-contained clean HTML artifact and remove the authoring layer itself, not merely hide it.

The clean export must preserve the user's accepted text, typography, alignment, position, size, palette, and image changes while removing editor-only UI, runtime CSS, runtime JavaScript, temporary selection state, `contenteditable`, editability metadata such as `data-edit`, editor labels and bounds, and other authoring-only attributes.

Do not remove ordinary presentation navigation, interactive teaching behavior, or content JavaScript that belongs to the final artifact. The exported file should behave as though the accepted refinements had been authored directly into the presentation from the beginning.

**Invariant:** Final saving must work for the normal self-contained `file://` delivery model without requiring a server, network call, or permission to overwrite the source file. A browser-native Blob/download flow is an acceptable baseline. Prefer a clear derivative filename such as `<original>-final.html` when the browser cannot safely replace the original file.

**Invariant:** Static PDF or print derivatives made from an editable presentation must also omit editor chrome, selection outlines, editability metadata, and transient authoring state.

**Default:** When the user asks for both an editable source and an audience-ready version, keep them distinct: the editable source retains the authoring layer and the audience-ready derivative is the clean exported form.

## Verification handoff

Before delivery, load and apply `presentation_editor_verification.md`. That module owns the rendered editor test matrix and clean-export/reopen checks. Do not duplicate that matrix during ordinary authoring turns.
