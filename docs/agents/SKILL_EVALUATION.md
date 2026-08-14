# Project Skill Evaluation

Status: `LOCAL PASS / REMOTE PORTABILITY PENDING`
Evaluation date: 2026-08-14

## Scope

The repository skill set was evaluated against the explicit workflow contract rather than generic prose quality. The evaluated path is:

```text
research-workflow router
  -> wayfinder decision map
  -> implementation / EXP / hybrid spec routing
  -> evidence-slice tickets
  -> one user-selected ticket implementation contract
```

Committed eval definitions use the `skill-creator` `evals/evals.json` schema under each of the five explicit entry skills. `scripts/skill-evals doctor` validates schema, explicit invocation and minimum coverage.

## Structural results

| Check | Result |
| --- | --- |
| Physical skills under `.agents/skills/` | PASS — 13 |
| Generated Claude mappings resolving to the same directories | PASS — 13/13 on macOS; mapping paths are Git-ignored |
| Explicit entry skills with both platform invocation controls | PASS — 5/5 |
| Supporting skills left available on demand | PASS — 8/8 |
| `skill-creator` eval suites | PASS — 5 skills / 16 cases |
| Label manifest schema | PASS — 19 labels |
| Root Claude single-source import | PASS — exact `@AGENTS.md` shim |

The bundled `skill-creator/scripts/quick_validate.py` rejects Claude Code's valid `disable-model-invocation` extension because its allowlist does not include that field. It was not used to erase the field. Repository validation instead checks both Claude and Codex invocation controls directly; eval files retain the skill-creator schema.

## Dynamic dry-run matrix

All dynamic prompts explicitly disabled commands, file changes, network and GitHub publication. This validates routing and refusal behavior without polluting the public tracker.

| Platform | Case | Expected | Result |
| --- | --- | --- | --- |
| Claude Code 2.1.228 | mixed UI research/code/data request, no map | route to Wayfinder | PASS |
| Claude Code 2.1.228 | chart UI instrument decision map | parent + typed decision children + fog; no execution | PASS |
| Claude Code 2.1.228 | hybrid UI + H2 contract | Issue implementation spec + canonical `EXP-*` + tracking Issue | PASS |
| Claude Code 2.1.228 | `PROPOSED` EXP to tickets | refuse before frozen review | PASS |
| Claude Code 2.1.228 | Implement without exact ticket | refuse automatic selection | PASS |
| Claude Code 2.1.228 | Implement with open H2 blocker | refuse participant activity | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | frozen EXP without slices | route to Tickets | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | several ready tickets | refuse automatic selection | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | hybrid contract with unresolved estimand/detail | classify hybrid and return to Wayfinder | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | frozen hybrid decomposition | evidence slices, blockers, claim bounds, approval gate | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | Wayfinder map with several decision-frontier children but no named child | refuse selection and assignment | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | Implement without exact ticket | refuse automatic selection | PASS |
| Codex 0.148.0-alpha.9 / GPT-5.6-sol | ready code ticket contract | eligibility before claim; TDD; dual review; log; local commit; stop before publication | PASS |

One initial Codex batch incorrectly passed `$skill-name` inside shell double quotes, causing shell variable expansion. Those runs were excluded. The batch was rerun with single-quoted prompts and the explicit skill name was confirmed in the Codex input transcript before grading.

## Flow-level assertions

- Mixed activities never decide the stage; missing decision/contract/slice/evidence does.
- Wayfinder produces decision tickets and stops; it does not auto-run research children.
- Wayfinder reports but never auto-selects or claims a decision frontier; the user names the child.
- Scientific experiment prose has one owner in `EXP-*`; GitHub remains the collaboration/publication surface.
- To Tickets refuses an unfrozen experiment and produces typed evidence slices for a frozen hybrid.
- Implement never chooses a ready ticket, never converts an H2-blocked activity into a smoke test, and never equates local completion with public completion.
- UI is treated as a measurement instrument with engineering, H2 and held-out confirmation boundaries.

## Real GitHub tracker smoke

After dry-run validation, the user-authorized tracker path was exercised against the public repository:

- 19 workflow labels were installed idempotently and read back with exact color/description checks.
- [Freeze the non-AI baseline-to-H2 contract portfolio](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2) was created as the parent map.
- 12 decision tickets were attached as native GitHub sub-issues.
- All dependency edges were created with native Issue dependencies and their `blocked_by`/`blocking` counts were read back.
- The initial unblocked frontier contains two research tickets and two external/task tickets; no execution ticket was created or claimed.

This proves the map/sub-issue/dependency operations on the configured repository. Spec publication, execution-ticket creation and Implement mutation remain intentionally unexercised on the public tracker until their real decisions/contracts exist.

## Remaining external proof

The local macOS implementation and model dry runs pass. Windows uses a directory-junction generation path that cannot be executed on macOS; the `skill-portability` GitHub Actions matrix is the acceptance evidence for both `macos-latest` and `windows-latest`. The mappings are generated under a Git-ignored root so installation must leave the checkout clean. Until the branch is published and both jobs pass, cross-platform status remains `PENDING`, not complete.
