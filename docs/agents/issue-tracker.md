# Issue tracker: GitHub

Repository: `wubq511/english-reading-cognitive-modeling`

GitHub Issues are the collaboration surface for maps, decisions, specs and evidence slices. Use `gh` from inside the clone and infer the repository from `origin`. Scientific and dynamic-state ownership remains defined in [`research-workflow.md`](research-workflow.md) and [`../../reports/provenance/SOURCE_POLICY.md`](../../reports/provenance/SOURCE_POLICY.md).

## Safety and identity

- Resolve the repository with `gh repo view --json nameWithOwner,url`; never write to a repository inferred only from prose.
- Read before write and read back every created/edited Issue, label and relationship.
- Refer to issues in human-facing prose with a descriptive linked title, not a bare number.
- Never paste secrets, third-party restricted originals, human data or private recovery materials into an Issue.
- Issue/label publication is authorized when the user explicitly invokes the relevant project workflow. Push/PR/Release remains a separate publication boundary.

## Labels

| Label | Meaning |
| --- | --- |
| `wayfinder:map` | Parent decision map |
| `wayfinder:research` | Primary-source decision investigation |
| `wayfinder:prototype` | Disposable artifact for a human decision |
| `wayfinder:grilling` | Human-owned decision conversation |
| `wayfinder:task` | Access/manual prerequisite for a decision |
| `workflow:spec` | Spec publication/tracking Issue |
| `spec:implementation` | Software/UI/data-pipeline behavior contract |
| `spec:experiment` | Tracking surface for canonical `EXP-*` |
| `spec:hybrid` | Parent linking implementation and experiment contracts |
| `workflow:ticket` | Executable evidence slice |
| `work:research` | Research evidence slice |
| `work:source` | Source/item/data-rights closure slice |
| `work:experiment` | Experiment design/run/analysis slice |
| `work:code` | Executable implementation slice |
| `work:data` | Versioned dataset/transformation slice |
| `work:governance` | Protocol/ADR/audit/collaboration slice |
| `ready-for-agent` | Contract is sufficiently specified; still check dependencies and external gates |
| `workflow:in-progress` | Explicitly claimed execution ticket |
| `workflow:needs-review` | Delivered branch/PR/result awaits review |

Create missing labels idempotently from the repository label manifest maintained with the skills. Do not repurpose generic `bug`/`enhancement` labels for workflow state.

```bash
scripts/workflow labels-check
# labels-install changes the public repository; run only inside an authorized publication workflow.
scripts/workflow labels-install
```

## Core operations

```bash
gh issue create --title "..." --body-file <file> --label "..."
gh issue view <number> --comments --json number,title,url,body,state,labels,assignees
gh issue edit <number> --add-label "..." --remove-label "..."
gh issue edit <number> --add-assignee @me
gh issue comment <number> --body-file <file>
gh issue close <number> --comment "..."
```

Use temporary files outside the repository for multiline `--body-file` payloads and delete them after the command. Do not use shell interpolation that can execute body text.

## Native hierarchy and blocking

The parent map/spec and children are ordinary Issues. GitHub database IDs, not display numbers or node IDs, are required by relationship endpoints.

```bash
owner_repo=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
child_id=$(gh api "repos/$owner_repo/issues/<child-number>" --jq .id)

# Attach child to parent.
gh api --method POST \
  "repos/$owner_repo/issues/<parent-number>/sub_issues" \
  -F sub_issue_id="$child_id"

# Make <ticket-number> blocked by <blocker-number>.
blocker_id=$(gh api "repos/$owner_repo/issues/<blocker-number>" --jq .id)
gh api --method POST \
  "repos/$owner_repo/issues/<ticket-number>/dependencies/blocked_by" \
  -F issue_id="$blocker_id"
```

Read relationships back with the corresponding `GET` endpoints. Native relationships are canonical. Only when the repository/API demonstrably lacks the feature may the Agent use `Part of: <linked title>` and `Blocked by: <linked title>` body lines; it must record that downgrade in the Issue.

## Frontier and claim

- Wayfinder frontier: open sub-issue, all native blockers closed, no assignee.
- Execution frontier: open `workflow:ticket` + `ready-for-agent`, all native blockers closed, every external gate satisfied, no assignee.
- If no ticket is named, query the relevant frontier read-only, report at most three titled URLs, and recommend one using downstream unlocks, evidence/gate readiness and the user's stated goal. Explain when another option is preferable. Do not mutate GitHub or the worktree.
- Wayfinder requires one user-named decision frontier ticket before assignment or work.
- Implement requires the user to name one execution ticket. After validation, assignment to `@me` is the claim; remove `ready-for-agent` and add `workflow:in-progress`.
- Never reassign a ticket owned by another member without an explicit human decision recorded on the Issue.

## Branch and completion

- Stay on an existing non-protected work branch when it matches the ticket.
- From `main` or another protected/default branch, create `<agent>/<member-id>/issue-<number>-<slug>`: use `codex/` for Codex and `claude/` for Claude Code. Do not share one mutable branch between members.
- Local completion produces a commit and member log but does not close the Issue.
- After an authorized PR is merged and required CI passes, link the merge/result, remove active status labels, and close the ticket.
