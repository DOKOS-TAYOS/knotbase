# Authorized public CV workflow deviations

The private DIK CV workflow is the source of this public `professional_documents` domain. The owner expressly authorized creating standard CVs **without a mandatory template**. The public package also removes original-owner facts, private source dependencies and the Europass template route. DIK is unchanged.

## Canonical origin and verified public blobs

| Source path under `info_for_ai/professional_documents/` | DIK Git blob SHA | Knotbase Git blob SHA |
|---|---|---|
| `00_core.md` | `69ae969e51ccca01f70be69b837da3fe361f97f9` | `ece1ed9378390cf78c7159084d9b8701401d01bc` |
| `01_crear_cv.md` | `fedf562d5687847fba876e84945f15b1c1694bff` | `bef0dde30213012a26050afcc91fbc982f51c7ff` |
| `02_reajustar_cv.md` | `6fe19168096af2e92a12f8a9e238d628db10243a` | `9c50521c66e3194cb0d4279a5701075803422c91` |
| `standard_cv_rendering.md` | `5c9e58b16f6f1cc2f15754de19569a40a43e4284` | `8b8e2124820edc3baf8e9131f447afca6302f7c1` |
| `indice_professional_documents.csv` | `80606d7937caa69c0cc6cf346b989a39da1816dc` | `dc5468c146fe4fbf4f682f88cd4b5a4d649accc0` |

The manifest status for each of these five files is `authorized-workflow-adapted`. Its SHA field identifies the canonical *DIK* blob, not the public target. Public target hashes above were verified by fetching each complete file from the branch.

## Documented differences

- `00_core.md`: keeps the evidence-led, two-stage strategy and explicit approval checkpoint, applicant-specific evidence selection, publication verification, privacy, and relevance ranking. Replaces private-profile lookups and personal defaults (employer email, nationality, phone authorization, named projects/platforms) with explicit user-provided or user-authorized evidence. Replaces the fixed-template output rule with generation of new semantic HTML.
- `01_crear_cv.md`: preserves phase-1-only initial invocation and the explicit OK before generating a CV. The source of facts is the current user's authorized evidence, not DIK's private profile records. Removes mandatory asset lookup and the Europass branch.
- `02_reajustar_cv.md`: preserves the distinction between local changes and substantial retargeting, and the approval checkpoint for strategic retargeting. Removes private profile lookups, private asset dependencies and Europass routing.
- `standard_cv_rendering.md`: preserves PDF-first default, optional editable DOCX, final visual inspection, native text extraction and ATS reading-order checks. Replaces compulsory owner-specific HTML/CSS template, prescribed colors, logo grid and asset catalog with task-specific semantic HTML, optional legally usable assets and selectable design. A DOCX may be built with a reliable editable equivalent rather than an exact HTML conversion when necessary; editorial content and links must match.
- `indice_professional_documents.csv`: removes the unpublished Europass module, retains the index and its four resolvable entries for core, creation, adjustment and rendering.

## Acceptance limits

- No named applicant, company, employer, personal email, phone, nationality, projects, or contact facts are bundled.
- Only factual claims supported by the user's sources can appear in a generated CV. Placeholder content must be removed.
- A missing private template does **not** prevent generating a standard CV.
- Format generation requires available artifact tools; do not claim a PDF or DOCX exists without verifying the actual output.
- Phase 1 must still stop for explicit approval before phase-2 construction; local edits to an already approved CV are handled according to the adjustment contract.
- Relevant PDF output requires visual inspection and native ATS text extraction, not OCR. DOCX output requires editability and visual inspection.
- The excluded Europass workflow and private profile sources are not redistributed.
- This is a source-level migration. Global command routing and end-to-end Knotbase runtime compatibility remain unverified. A separate synthetic-data HTML/PDF/DOCX smoke test supports rendering feasibility, not the full runtime.
