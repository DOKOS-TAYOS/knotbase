# HTML verification before delivery

Open this module before delivering any created or revised HTML artifact.

Apply `htmls/00_core.md` first. Also apply every specialized HTML module selected for the artifact: those modules own the concrete behavioral, visual, presentation, editing, stateful-interaction, diagram, package, export, and derivative invariants that must be verified. Do not restate those specialized checklists here.

These artifacts are expected to work reliably in teaching and presentation contexts, but they do not require production-web engineering ceremony unless the user explicitly requests production readiness.

## Verification contract

**Invariant:** Before delivery, perform the strongest practical verification available in the current environment against the actual artifact and every applicable invariant from the loaded HTML modules. Fix any issue that could plausibly break live use or materially violate the intended presentation.

**Invariant:** Report only checks that were actually executed and supported by the observed result. Source inspection alone does not verify a runtime property. If an intended rendered, interactive, responsive, presentation, editing, export, or browser check could not be executed, distinguish that limitation explicitly from checks that did run and do not invent a reason for the limitation.

**Invariant:** Verify the user-observable result, not merely the implementation signal. Exercise the actual rendered state, geometry, interaction, presentation, editing, saved/exported derivative, or package behavior required by the modules that are active.

When browser execution is available, open the artifact through its intended delivery path, normally `file://`, in a current Chromium-compatible browser and exercise the relevant flows. Use representative wide and narrow viewports and any additional viewport or zoom conditions required by the selected modules.

At minimum, as applicable, establish that:

- the artifact opens through its intended delivery path without unexpected build, server, package, asset, or network requirements;
- reading, navigation and primary content remain usable at representative responsive sizes;
- meaningful interactions and recovery paths behave correctly in the rendered artifact;
- every selected specialized module passes its own verification contract, including stateful content controls, visuals, presentation mode, the default presentation editor, static export or multi-file packaging when active;
- public-facing content satisfies the cleanliness contract in `00_core.md` and the applicable content-domain requirements;
- there are no blocking JavaScript errors, broken internal references, missing required assets, unreachable primary content, or stale state introduced by resizing or interaction.

When the presentation editor is active by the default presentation route, load `presentation_editor_verification.md` at this delivery gate; that module is authoritative for the full editor test matrix and clean-export/reopen checks. When a PDF or other static derivative is requested, `static_pdf_export.md` owns derivative-specific state selection and verification. This file does not replace or weaken either contract.

Prefer direct browser smoke-testing and focused structural checks over heavyweight test harnesses for ordinary presentation HTML. Add automated tests only when they materially reduce a concrete failure risk, the interaction logic is complex enough to justify them, or the user explicitly requests them.

If browser execution or another required verification surface is unavailable, perform the strongest applicable structural or static checks available and report the unverified runtime properties separately to the user, never inside the public HTML itself.
