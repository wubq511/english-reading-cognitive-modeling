# Workflow Completion Audit

Status: `COMPLETE`
Audit date: 2026-08-14
Branch: `codex/research-workflow-skills`

This audit tests the user-approved objective against current evidence. “Implemented” is not treated as “complete” where runtime or remote proof is still absent.

| Requirement | Evidence | Status |
| --- | --- | --- |
| Use the named grilling process before edits | Seven frontier decisions were asked; user settled Q2–Q7, then explicitly approved the remaining router decision | PASS |
| Load disabled `skill-creator` directly from its files | Full local skill instructions/schema/scripts inspected; eval files follow its `evals/evals.json` schema; its quick validator was executed | PASS |
| Wayfinder → Spec → Tickets → Implement state machine | [`research-workflow.md`](research-workflow.md) defines missing-decision/contract/slice/evidence transitions and reopen rules | PASS |
| Do not split work into “research” versus “implementation” | State machine and evidence-slice types allow literature, code, data and experiments in the same route | PASS |
| Adapt Wayfinder for the research repository | Repository skill creates decision maps/sub-issues, preserves fog, evidence states, human gates and no-auto-research behavior | PASS |
| Adapt To Spec for implementation, experiment and hybrid contracts | GitHub implementation spec, canonical `EXP-*`, experiment tracking Issue, and hybrid parent rules are explicit | PASS |
| Adapt To Tickets for scientific and engineering work | Evidence-slice template covers types, provenance, claims, gates, null results, blockers and one-context sizing | PASS |
| Adapt Implement without automatic ticket selection | Without an Issue it gives bounded read-only recommendations and waits; with one user-named Issue it checks eligibility before claim, dispatches by work type, reviews/logs/commits locally, and stops before push | PASS |
| Distribute every required skill in the repository | 13 physical skill directories under `.agents/skills/`, including all transitive support skills | PASS |
| Distinguish project adaptations from upstream/global skills | All 13 project variants use the `ercm-` directory/frontmatter/display namespace; bootstrap migrates obsolete generated mappings | PASS |
| Preserve user-only invocation for public entry skills | Five entry skills have Claude `disable-model-invocation: true` and Codex `allow_implicit_invocation: false`; supporting skills retain on-demand invocation | PASS |
| Claude Code uses the same skill source | 13 generated, Git-ignored `.claude/skills/` mappings resolve to the tracked `.agents/skills/` directories on macOS | PASS |
| Windows and macOS support | GitHub Actions run [31795159885](https://github.com/wubq511/english-reading-cognitive-modeling/actions/runs/31795159885) passed `skill-portability` on both `macos-latest` and `windows-latest`, including generated mapping and clean-checkout assertions | PASS |
| GitHub Issues for all workflow artifacts | Tracker contract requires Issues for maps, decisions, all spec forms and evidence slices while preserving scientific canonical owners | PASS |
| Native parent/dependency collaboration | 19 labels plus parent map #2, 12 native sub-issues and all dependency counts were created and read back on the configured repository | PASS |
| Full isolated behavioral path | 16 committed evals plus Claude/Codex read-only dry runs cover every stage, refusals, hybrid routing, H2 gate and recommendation-without-claim invariants | PASS after current recommendation eval reruns |
| UI research is not omitted | RQ0, ROADMAP instrument lane, CURRENT_STATE, workflow contract and real map decisions cover UI reliability, variants, H2 and held-out confirmation | PASS |
| Single-source maintenance | Workflow/tracker owners added to `SOURCE_POLICY`; stage skills point to them; root Claude rules use one `@AGENTS.md` import | PASS |
| Repository verification | 55 unit tests, local and public `scripts/verify`, source doctor, skill doctor, eval doctor, label read-back and diff check pass | PASS |
| Public push boundary | The user explicitly approved pushing this branch and opening a PR; draft [PR #15](https://github.com/wubq511/english-reading-cognitive-modeling/pull/15) is published, while merge and Release remain outside that approval | PASS |

## Remote acceptance evidence

Commit `06c63bb` on `codex/research-workflow-skills` supplied the final namespace and selection-assistance behavior to draft PR #15. GitHub Actions run 31795159885 passed the normal public `verify` job and both portability jobs. Windows generated ignored junction mappings, ran the mapping doctor and wrapper/unit checks, and retained a clean checkout. No acceptance check was weakened, and no merge or Release was performed.
