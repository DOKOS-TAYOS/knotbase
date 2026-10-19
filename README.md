# Knotbase

Knotbase is an incremental, public distribution of indexed AI instruction workflows derived from the privately validated DIK instruction repository.

## Current status

**Scoped public routing pilot in progress — not a validated functional release.** The source parity manifest currently records **134 unique source records**:

- 103 `verbatim` (Git blob identical to the DIK source);
- 18 `privacy-adapted`;
- 3 `privacy-and-editorial-adapted`;
- 1 `authorized-editorial-adapted`;
- 5 `authorized-workflow-adapted` (the public template-free CV module);
- 3 `public-routing-adapted` (scoped public router and indices);
- 1 `public-subset-adapted` (four exact DIK command rows).

The published source domains include code, GitHub, research, papers, education, prompting, interactions, blog writing, and the public standard-CV workflow, plus a **partial** HTML domain. Publication status and canonical DIK source blob SHA values are recorded in [the source parity manifest](manifests/source_parity.csv).

Identical DIK source files retain their exact instructions. Deviations are limited to documented privacy adaptations and specific owner-authorized exclusions of the original author's blog-writing style and the fixed personal CV template. See [privacy adaptations](docs/PRIVACY_ADAPTATIONS.md), [editorial exclusions](docs/EDITORIAL_EXCLUSIONS.md), and [authorized CV workflow deviations](docs/AUTHORIZED_CV_DEVIATIONS.md). These changes are explicit exceptions to literal source parity; they are not presented as verbatim copies.

The standard CV workflow uses an evidence-led **two-phase strategy with explicit approval** before drafting a new CV and can render its own HTML, PDF, and optionally DOCX **without an existing template or required private assets**. The personal source/profile layer and the Europass template and rendering workflow are not published. A scoped root router and four-command registry are now provided, but their operation inside a consumer runtime still needs end-to-end verification.

**Important runtime limitation:** the new public `AGENTS.md`, `comandos.csv`, `comandos_lookup.csv`, limited domain index and shared continuation contract expose only `#HELP`, `#BLOG`, `#CV` and `#CVEDIT`. This is an instructional pilot, **not a standalone program or an end-to-end-validated runtime**. Commands beyond those four are unregistered. The `htmls` domain remains partial, the blog's private article-inventory layer is unavailable, and no personal evidence records are bundled. Actual ChatGPT client dispatch, authorization phases, sourcing and artifact generation still require independent acceptance tests. See [public router scope](docs/PUBLIC_ROUTER_SCOPE.md).

Source publications must preserve original DIK behavior and algorithms except for documented privacy and owner-authorized deviations. Do not add private or restricted data, personal contact details, proprietary templates, or unlicensed third-party media.

## Migration handoff

For verified migration checkpoints, limitations, and remaining steps, read [migration continuity](docs/MIGRATION_CONTINUITY.md).

## License

Original materials published in this repository are available under the [MIT License](LICENSE). Third-party materials, trademarks, and assets are not sublicensed by this license.
