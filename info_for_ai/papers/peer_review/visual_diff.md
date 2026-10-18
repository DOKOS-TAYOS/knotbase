# Peer-review visual manuscript diff

## Activation

Load this module when the task is to compare a submitted TeX manuscript commit with a current commit and produce a reviewer-ready visual diff.

Use the parent `../01_peer_review_response.md` workflow for shared repository, evidence, and readiness rules.

## Contract

Given a TeX repository, a submitted commit, and a current commit, prepare an independent diff TeX source and reproducible compilation instructions for a reviewer-ready PDF. Use the two requested versions, not a working-tree snapshot, unless the user explicitly asks otherwise.

The compiled diff must show removals in red and additions in green. Configure the available diff tooling for the smallest possible changed span:

- highlight only changed words in prose;
- highlight only changed terms or expressions in equations;
- highlight only changed cells, entries, captions, or table text when possible.

Do not mark an entire paragraph, equation, or table when only a smaller part changed. If the available TeX/diff tooling cannot achieve this precision, identify the limitation, show the closest reproducible output, and do not misrepresent it as minimal.

Keep the generated diff source, build command, required TeX packages, and output location separate from the normal manuscript source. Verify that it compiles when the required local tooling is available.
