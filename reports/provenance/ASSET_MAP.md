# Asset Map

| Asset | Purpose | Authority/use | Public Git default |
| --- | --- | --- | --- |
| root `README.md`, `AGENTS.md`, `CONTEXT.md` | orientation and rules | canonical | include |
| `reports/project_state/` | current status and plan | canonical | include |
| `reports/synthesis/` | recovered system/research design | canonical with claim labels | include under CC BY 4.0 policy |
| `reports/protocols/` | AI/human/experiment gates | canonical | include |
| `reports/research/` | primary-source audits and exact acquisition queues | canonical scoped research | include |
| `reports/provenance/` | audit trail and crosswalk | canonical provenance | include, excluding sensitive content |
| `reports/literature/a-e/` | detailed paper deep reads | derived research asset; verify against PDF for high-stakes claims | include after source-link cleanup |
| `reports/literature/ui-interaction/` | UI paper notes | derived research asset | include after rename/link cleanup |
| `papers/catalog.yaml` | stable paper identity, versions, paths, acquisition channel, rights and exact bytes | canonical machine index | include under the metadata license scope in `LICENSES/README.md` |
| `papers/checksums.sha256` | exact local versions | integrity | include |
| `papers/**/*.pdf` | third-party full text local cache | primary scientific source | exclude unless individually rights-cleared and separately approved |
| `webchat_raw_materials/chatgpt_chathistory/` | full recovery transcript | highest historic project-state evidence | exclude; local frozen |
| `webchat_raw_materials/handoff/` | compact session handoff | historic derivative evidence | exclude; local frozen |
| `webchat_raw_materials/chatgpt_migration_package/` | GPT-produced migration proposal/reference | lowest recovery authority | exclude; local frozen |
| future `data/human/` | H2/H3 participant data | restricted research data | always exclude |
| future `data/synthetic/` | engineering/simulation data | simulation-only, provenance required | include selectively after license/size review |

## Completed stage-2 physical reorganization

On 2026-08-14 the historical paths `reports/A-E_analyses`, `reports/ui_interation_behavior_literature_research`, `papers/chatgpt_A-E`, and `papers/ui_interation_behavior` were moved to the current neutral `reports/literature/*` and `papers/library/*` paths. Catalog, checksums, crosswalk and navigation were updated together; PDF bytes and filenames were preserved.

Still open: determine UIB-088 origin and preferred same-work PDF versions before any deletion.

No file is deleted as part of a rename migration without an explicit post-migration audit and user-approved cleanup.
