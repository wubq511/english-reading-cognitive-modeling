---
name: research
description: Investigate a question against high-trust primary sources and capture a provenance-aware Markdown asset in this research repository. Use for literature, standards, API facts, or a Wayfinder research decision.
---

Run the research in a background Agent only when the user and current platform policy permit delegation. Otherwise perform the same bounded investigation in the current session; delegation is an optimization, not a correctness requirement.

## Contract

1. Run project preflight and identify the canonical owner before writing. Standalone research usually belongs in `reports/research/`; a result that changes a current project claim must update that claim's owner under `reports/` instead of creating a competing note.
2. Prefer primary sources: local paper/standard originals with stable source IDs, official documentation, source code, specifications, and first-party datasets/APIs. Follow consequential claims to the source that owns them.
3. For local full-text claims, require `scripts/sources doctor` and cite stable source ID plus page/section/table/figure. Mark `ABSTRACT-ONLY`, `UNKNOWN`, or inaccessible evidence honestly.
4. Separate source statements from `PROJECT-INFERENCE`; record applicability, alternatives, contrary evidence, and what remains unresolved.
5. Write one Markdown asset with question, method/search boundary, evidence table, findings, limitations, decision implications, and exact citations.
6. If resolving a Wayfinder ticket, link the asset in the resolution comment. Do not paste the report into the Issue.
7. Run proportionate link/source/repository verification. Research is complete when the artifact and citations are reviewable, not when the prose sounds decisive.
