# Owner-authorized editorial-style exclusions

The Knotbase author explicitly requested that the public blog-writing package **not reproduce the original DIK author's personal writing style**. This is an authorized behavioral adaptation, distinct from identity redaction. The private DIK remains unchanged.

## Scope and reproducibility

The following file transformations were applied to the previously public Knotbase sources using uniquely matching exact-string replacements. No other instruction was edited in those files. Each published file was fetched again and compared with the intended complete transformed content.

| File under `info_for_ai/blog_writing/` | Previous public blob SHA | New public blob SHA | Exact edits |
|---|---|---|---:|
| `00_core.md` | `2c96416110d0b0c196c9b8b0c9f2c607e4e88386` | `99ffd764fc2a0e59ac100fdc19cbb613a4b71ab1` | 5 |
| `02_voz_pedagogia_y_ritmo.md` | `961f3646be66f488d8e22ffae9c3fbb83bee8845` | `4603325b3bc073d3f21b083c0f68eb71bd41c20b` | 2 |
| `03_revision.md` | `d91a125fde62ff7207668f38f1d45ea6e486a6f4` | `38f184b896e074dfe67d7460d286f7a6729cc964` | 1 |
| `publication_materialization.md` | `9ad2bdb918079936f5387eca93efb19f8e14c33a` | `42313621003190e74590e17c789aa33e9052568a` | 2 |

The 10 edits remove or replace the following original-author-specific defaults:

1. Mandatory presentation in the original author's researcher voice.
2. Ranking fidelity to that original author's reasoning style as a priority.
3. Specific bans on emoji, em dashes, and particular rhetorical tone markers.
4. Requirements to imitate the original author's verbal identity or favored critical style.
5. A blanket preference against a specific contrast rhetorical formula.
6. The fixed original voice model in the prose module, replaced with configurable audience/author voice.
7. Default usage of straight double quotes as a personal typographic convention.
8. The automatic Spanish-from-Spain language preference instead of the user's requested locale.
9. Personal constraints on the tone and conventions of social distribution.
10. Mandatory fixed original-author LinkedIn sign-off.

The public GitHub PR diff supplies the precise changed lines. Canonical DIK source blob SHAs remain unchanged in `manifests/source_parity.csv`, which now supports four documented statuses:

- `verbatim`: exact canonical DIK Git blob.
- `privacy-adapted`: personal-data redactions only.
- `authorized-editorial-adapted`: editorial-style changes explicitly authorized by the owner.
- `privacy-and-editorial-adapted`: both categories apply.

**Preserved:** all seven `#BLOG` phases, the `OK` continuation gate, ordering of argument design and factual review, mathematical verification and publication formatting stages, link evidence rules, and image-planning approval boundaries. The source index and state-machine file remain unchanged and retain their canonical blob hashes.

**Not claimed:** end-to-end command/runtime functionality in Knotbase. The public system still needs its global router and relevant data dependencies.

The historical published hashes in `docs/PRIVACY_ADAPTATIONS.md` describe the original privacy-only snapshot. The table above supersedes those **target** hashes for the three now privacy-plus-editorial files while retaining the canonical DIK source hashes documented there.
