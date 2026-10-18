# Presentation editor verification

Open this module only before delivering an editor-enabled presentation or an export derived from one. The implementation contract remains in `presentation_editor.md`; this module owns the rendered verification matrix so ordinary authoring turns do not need to carry it.

Apply `htmls/00_core.md`, `htmls/presentation_editor.md`, and `htmls/05_verification.md`. When presentation mode is active, also apply `htmls/03_presentation_mode.md`.

## Verification matrix

Exercise the actual rendered editor rather than checking source markers alone. As applicable, verify:

- the editor starts closed, opens from its launcher, closes cleanly, and does not alter the layout while closed;
- selecting a text element and typing normally after a single click, including caret continuity;
- plain-text paste or equivalent sanitization does not inject unintended markup into directly editable text;
- font-size adjustment within its bounds;
- every exposed alignment state and its persistent selected control;
- horizontal and vertical movement plus position reset, without overwriting existing transforms;
- supported size adjustment without breaking surrounding layout;
- palette updates and palette reset;
- local image replacement when editable images are present;
- selected-element reset and complete reset;
- current edits persist through editor close/reopen, slide navigation, and reading/presentation mode toggling during the page session;
- keyboard isolation between editing controls and presentation navigation;
- `Guardar HTML final` produces a clean artifact with the accepted visual/content changes preserved and the authoring runtime and metadata actually removed;
- the saved clean HTML is reopened independently and still renders, navigates, and presents correctly without the editing layer.

After representative edits, re-check both reading-mode usability and presentation fit at the representative viewport and zoom conditions required by the selected HTML modules. If an intentionally extreme user edit can exceed safe composition bounds, keep the controls bounded rather than attempting to guarantee arbitrary geometry.
