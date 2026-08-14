# Asset Map

| Asset | Purpose | Authority/use | Public Git default |
| --- | --- | --- | --- |
| root `README.md`, `AGENTS.md`, `CONTEXT.md` | orientation, rules and terminology | canonical; `CLAUDE.md` symlinks to `AGENTS.md` | include |
| `docs/project-management/` | Agent startup, source synchronization and repository collaboration | canonical project operations | include |
| `logs/` | per-member research/change intent, verification and follow-ups | canonical append-only collaboration history; exact diffs remain in Git | include; exclude sensitive or licensed payloads |
| `reports/project_state/` | current status and plan | canonical | include |
| `reports/synthesis/` | recovered system/research design | canonical with claim labels | include under CC BY 4.0 policy |
| `reports/protocols/` | AI/human/experiment gates | canonical | include |
| `reports/research/` | scientific primary-source audits and exact research acquisition queues | canonical scoped research | include |
| `reports/provenance/` | audit trail and crosswalk | canonical provenance | include, excluding sensitive content |
| `reports/literature/a-e/` | detailed paper deep reads | derived research asset; verify against PDF for high-stakes claims | include after source-link cleanup |
| `reports/literature/ui-interaction/` | UI paper notes | derived research asset | include after rename/link cleanup |
| `sources/catalog.yaml` | stable external-source identity, type, version, path, acquisition channel, rights and exact bytes | canonical machine index | include under the metadata license scope in `LICENSES/README.md` |
| `sources/checksums.sha256` | exact local source versions | integrity | include |
| `sources/library/` | third-party papers, standards, study materials and datasets | primary external evidence/input | exclude unless individually rights-cleared and separately approved |
| `src/` | baseline runtime implementation boundary | future code; currently normative skeleton only | include |
| `experiments/` | experiment specifications and run-manifest templates | canonical experiment design layer | include |
| `data/` | project-generated, derived or human data | governed by data role | include documentation; generated/human data excluded by policy |
| `artifacts/` | reproducible run outputs | non-canonical machine output | exclude bulk/sensitive runs; include reviewed small manifests only |
| `webchat_raw_materials/chatgpt_chathistory/` | full recovery transcript | highest historic project-state evidence | exclude; local frozen |
| `webchat_raw_materials/handoff/` | compact session handoff | historic derivative evidence | exclude; local frozen |
| `webchat_raw_materials/chatgpt_migration_package/` | GPT-produced migration proposal/reference | lowest recovery authority | exclude; local frozen |
| future `data/human/` | H2/H3 participant data | restricted research data | always exclude |
| future `data/synthetic/` | engineering/simulation data | simulation-only, provenance required | include selectively after license/size review |

## Completed physical reorganizations

On 2026-08-14 the historical report paths were moved to `reports/literature/*`; the historical `papers/chatgpt_A-E` and `papers/ui_interation_behavior` names first became a neutral local library. A later confirmed source-boundary migration replaced the misleading `papers/` root with typed `sources/library/{papers,standards,study-materials,datasets}` paths. Catalog, checksums, crosswalk, navigation and tooling were updated together; existing source bytes were preserved.

Human-acquired paper PDFs now enter only through `tmp/pdfs/`. After catalog identity and target bytes are verified, `scripts/sources inbox` removes the temporary duplicate; unresolved files stay in the inbox.

Still open: determine UIB-088 origin and preferred same-work PDF versions before any deletion.

No canonical source is deleted as part of a rename migration. Inbox cleanup is separately authorized and only occurs after verified import.
