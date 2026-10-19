# Knotbase

Knotbase is an incremental, public distribution of indexed AI instruction workflows derived from the privately validated DIK instruction repository.

## Current status

**Source migration in progress — not a functional release.** The source parity manifest currently records **129 unique source files**:

- 102 `verbatim` (Git blob identical to the DIK source);
- 18 `privacy-adapted`;
- 3 `privacy-and-editorial-adapted`;
- 1 `authorized-editorial-adapted`;
- 5 `authorized-workflow-adapted` (the public template-free CV module).

The published source domains include code, GitHub, research, papers, education, prompting, interactions, blog writing, and the public standard-CV workflow, plus a **partial** HTML domain. Publication status and canonical DIK source blob SHA values are recorded in [the source parity manifest](manifests/source_parity.csv).

Identical DIK source files retain their exact instructions. Deviations are limited to documented privacy adaptations and specific owner-authorized exclusions of the original author's blog-writing style and the fixed personal CV template. See [privacy adaptations](docs/PRIVACY_ADAPTATIONS.md), [editorial exclusions](docs/EDITORIAL_EXCLUSIONS.md), and [authorized CV workflow deviations](docs/AUTHORIZED_CV_DEVIATIONS.md). These changes are explicit exceptions to literal source parity; they are not presented as verbatim copies.

The standard CV workflow uses an evidence-led **two-phase strategy with explicit approval** before drafting a new CV and can render its own HTML, PDF, and optionally DOCX **without an existing template or required private assets**. The personal source/profile layer and the Europass template and rendering workflow are not published. The CV module has not yet been integrated into a working global command runtime.

**Important runtime limitation:** the global `AGENTS.md` router, command registry/lookup, personal-profile-independent evidence routing and some dependencies are not yet published and validated in Knotbase. The `htmls` domain is partial, and the blog article-inventory dependency is not supplied. These source files do **not** yet establish a fully functional portable `#BLOG`, `#CV` or general command dispatcher. Prior DIK validation supports confidence in the unmodified sources, but it does not replace end-to-end validation of this public repository.

Source publications must preserve original DIK behavior and algorithms except for documented privacy and owner-authorized deviations. Do not add private or restricted data, personal contact details, proprietary templates, or unlicensed third-party media.

## Migration handoff

For verified migration checkpoints, limitations, and remaining steps, read [migration continuity](docs/MIGRATION_CONTINUITY.md).

## License

Original materials published in this repository are available under the [MIT License](LICENSE). Third-party materials, trademarks, and assets are not sublicensed by this license.
