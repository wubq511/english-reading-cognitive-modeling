# Manual Action Queue

Status: `ACTIVE`
Owner by default: project lead + laboratory/institution contact
Rule: these actions require credentials, institutional authority, author contact or human judgment; Agents must not simulate completion.

## Now: source acquisition that improves Phase 0

| Priority | Action | Exact target | Why manual | Completion evidence |
| ---: | --- | --- | --- | --- |
| P0 | Use laboratory/CNKI access or request author copy | Ma & Du 2022, DOI [`10.19360/j.cnki.11-3303/g4.2022.12.001`](https://doi.org/10.19360/j.cnki.11-3303/g4.2022.12.001) | official full text is access-controlled | lawful PDF imported with SHA/version; methods, item count and data statement audited |
| P0 | Use institutional access or request author manuscript | Du & Ma, *Thinking Skills and Creativity* 59, 102022, DOI [`10.1016/j.tsc.2025.102022`](https://doi.org/10.1016/j.tsc.2025.102022) | publisher page is abstract-only | lawful version imported; N=886 selection, instrument and Q-matrix lineage checked |
| P1 | Use institutional access or request author manuscript | Du & Ma 2021 PELDiaG, DOI [`10.1007/s11145-021-10124-x`](https://doi.org/10.1007/s11145-021-10124-x) | subscription full text, no verified OA copy | lawful version imported; 43/41-item claims, appendices, data/access and rights audited |
| P1 | Obtain through library subscription or corresponding author | Kottner et al. 2011 GRRAS, DOI [`10.1016/j.ijnurstu.2011.01.016`](https://doi.org/10.1016/j.ijnurstu.2011.01.016) | no verified OA full text found | PDF imported as a distinct catalog item; reporting-rule passages checked |
| P2 | Download official OA copy in a normal browser or request author copy | Shin 2025, DOI [`10.1111/jcal.70089`](https://doi.org/10.1111/jcal.70089) | official Wiley PDF endpoints returned HTTP 403 to the research environment | official/author PDF imported; version/license verified; AI-vs-human agreement claims checked |

The arXiv preprint `2306.00176` is intentionally **not** a missing requirement: the catalog keeps the formal ICWSM successor (`METHOD-007`) to avoid duplicate versions. Add the preprint only if a version-comparison question arises.

## Before Candidate Bank V1

1. Ask Wenbo Du / Xiaomei Ma for a compact lineage table covering the 2022 CSE paper, TSC 2026 and J. Intell. 2026:

   - `instrument_version_id` and item mapping;
   - collection batch, raw N, exclusion rules and final N;
   - whether any participant-response matrix was reused;
   - Q-matrix/construct changes by version;
   - answer-key authority and item/passages provenance;
   - data dictionary, de-identification and permitted research/sharing use.

2. If requesting J. Intell. empirical data from the corresponding author, first obtain the laboratory's data-governance approval. Do not send or accept person-level data through personal email/cloud without an approved transfer and storage route.
3. For `ITEM-002` S2, have at least two qualified English-reading/content experts independently answer every item and mark evidence spans; resolve disagreement without showing S3 model outputs. Record item-level source/right status. S3's Doubao answers are never the gold key.
4. If existing materials cannot be cleared, build an original passage/item package. Record authorship, source inspiration, answer rationale, evidence span, candidate skill mapping, allowed use and version from creation time.

Phase 0 remains open until at least one package satisfies all of: usable rights, passage/item/options, independent answer key, evidence spans, candidate tags, observability gradient and versioned pilot selection rules.

## Before inviting any team-external person

The user currently has no confirmed formal recruitment/ethics channel. Keep that as an explicit dependency, not an assumed future capability.

Ask the responsible laboratory/school in writing:

1. Which committee reviews this non-medical educational/HCI/cognitive study, and who must be PI/responsible investigator?
2. Can the institution issue a written H1 non-research/debug determination for bug-only smoke tests?
3. What review route applies to H2 feasibility pilot and H3 formal study, and can an approved pilot feed formal analysis?
4. What rules govern recruiting acquaintances, classmates or students, especially dependency/grade relationships and minors?
5. What consent, storage, retention, sharing and amendment rules apply to event logs, screen/audio recording, stimulated recall, Webcam and eye tracking?
6. What institutional storage and data-transfer channel is approved for collaborators and AI/LLM processing?

Until written answers exist:

- H0 synthetic/team engineering may proceed;
- an H1 external-person smoke test may produce only `NONRESEARCH_DEBUG_ONLY` defect tickets under the narrow rules in `HUMAN_RESEARCH_GATES.md`;
- H2/H3 systematic logs, performance, interviews, cognitive labels or publishable data must not start;
- Webcam/eye tracking remains an optional M1 amendment, not a baseline dependency.

## Before public GitHub publication

This step is intentionally pending explicit user approval after the final local audit.

- Confirm the tracked file list contains no raw chats, PDF bytes, human/private data, secrets or machine-local artifacts.
- Publish only catalog/checksums/source/right metadata for third-party PDFs; do not upload the local `papers/library/**/*.pdf` tree.
- If any rights-cleared PDF is later distributed, review the exact version, third-party credit lines and attribution; publish it through a separate approved release, never a directory-wide rule.
- After repository creation, enable branch protection/required verification as a simple follow-up; no complex deployment or data infrastructure is needed initially.

## Recording completion

For every completed manual action, update the relevant audit/catalog and add:

```yaml
action_id: stable-id
completed_at: YYYY-MM-DD
actor_role: project-lead | lab | library | author | ethics-office
evidence_path_or_url: string
artifact_sha256: string-or-null
result: completed | denied | unavailable | superseded
constraints: []
```

Do not mark an action complete from an email promise or a search snippet; completion requires the actual document, institutional determination, data-use agreement or other inspectable evidence.
