# Preliminary software-idea assessment

## Activation

Use this module before designing or implementing an idea to determine whether a credible tool, framework, SDK, or library already provides the intended functionality.

## What counts as existing

A solution exists when it covers the main capability sufficiently and is reasonably stable and maintained. At minimum, verify usage documentation, an identifiable license, usable releases or published versions, credible activity or maintenance, and adoption or evidence of real use. Classify an unfinished, unlicensed, or unmaintained repository as **preliminary**, not as an existing solution.

## Required research

For external evidence gathering and source verification, also load `../research/00_core.md` and `../research/05_source_discovery.md`. This module owns the software-capability and integration decision; the research domain owns evidence quality and source verification.

1. Bound the problem: users, functions, inputs, outputs, constraints, platform, performance, security, budget, and success criteria.
2. Search current primary sources: official sites and documentation, official repositories, package registries, and license texts. Do not use SEO lists or abandoned repositories as primary evidence.
3. For each candidate, assess functional coverage, maturity, maintenance, interoperability, license, cost, usage constraints, and integration risks. Separate confirmed facts from inference.
4. Treat licenses such as MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, and Zlib as permissive unless a concrete incompatibility applies. Do not classify copyleft, commercial, source-available, custom, or uncertain licenses as permissive without explicit analysis.

## Decision

- **A permissively licensed solution exists:** report it as integrable and pause design or development until the user chooses whether to adopt it or continue.
- **A solution exists but is not permissively licensed:** continue assessing an original alternative. Treat it as competition or inspiration; do not copy code, protected documentation, distinctive designs, or assets.
- **A sufficiently useful preliminary solution exists:** treat it as inspiration or a comparison reference, not as a direct dependency without an explicit decision.
- **No complete solution exists:** decompose the idea into capabilities. Classify each as permissively licensed and integrable, non-permissive or preliminary and inspiration-only, or absent and requiring implementation. Propose the resulting architecture, costs, dependencies, and implementation order.

## Report format

Start with an executive summary and a table containing `candidate`, `capability covered`, `maturity`, `license`, `integrable`, `primary evidence`, and `decision`. Then provide the missing-capability map, risks, and a clear recommendation. Include URLs and access dates. Do not present a license conclusion as legal advice.
