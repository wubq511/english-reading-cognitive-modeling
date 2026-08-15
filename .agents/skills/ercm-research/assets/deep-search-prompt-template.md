# Web-AI deep-search prompt template

Bundled asset of `ercm-research` step 4. Build the copy-paste prompt by filling every `<slot>` from the current search protocol, then hand it to the user. The user pastes it into the web AI chat of their choice (deep-research modes preferred) and relays the raw answer back. Verification of whatever returns is the agent's job, per SKILL.md step 4 — the template's job is to keep the AI on the discovery task and prevent drift.

Why the constraints exist:

- **Discovery only, no synthesis.** The AI's prose conclusions are not evidence and tend to anchor the later verdict. The prompt therefore asks for candidates and forbids review-style conclusions.
- **DOI-or-URL plus UNVERIFIED marking.** AI chats invent plausible citations. Requiring a resolvable identifier per item, with an explicit UNVERIFIED fallback, makes hallucinated entries detectable instead of silent.
- **Per-item source query.** Knowing which query surfaced a hit lets the agent rerun it and judge channel coverage.
- **Explicit contrary and Chinese-language asks.** Web AIs default to the canonical, English, confirming set; both have to be requested by name.
- **Held anchors listed.** Prevents the round from re-spending its budget rediscovering what the library already holds.

## Template

```text
You are a literature-discovery assistant. Your only job is to FIND candidate primary sources for the research question below. Do not write a review, do not synthesize conclusions, and do not tell me what the answer to the question is — I only need a verified candidate list.

## Research question

<one paragraph: the exact question, copied from the search protocol>

## Inclusion criteria

<population, task, method, date range — copied from the protocol>

## Exclusion criteria

<copied from the protocol>

## Already held — do NOT return these

<list of anchor sources already in the local library: author year + title, one per line; delete this section if none>

## What to return

At most <N, default 15> candidates. For each candidate, exactly these fields:

1. Title, authors, venue, year
2. DOI, or a stable URL if no DOI exists. If you cannot point to a real bibliographic record, mark the item UNVERIFIED — never invent a DOI, title, or author list. It is much better to return fewer items than to return one fabricated citation.
3. One sentence: why this item plausibly bears on the question (which inclusion criterion it meets)
4. The exact search query you used when this item surfaced

## Coverage requirements

- Search in both English and Chinese where the question could have Chinese-language literature; include the Chinese query terms you used.
- Actively look for studies whose findings CONTRADICT the mainstream or expected direction, and for null results — list them like any other candidate.
- Prefer primary empirical studies and meta-analyses over textbooks, blog posts, and secondary summaries.

## Final section of your answer

After the candidate list, add a section "Queries actually run" listing every search query you executed, in every language, one per line. If you ran none and answered from memory, say so explicitly.
```

## After the answer comes back

1. Confirm each item's bibliographic reality via Crossref/ERIC/DOI resolution before it enters the acquisition queue; drop or mark UNVERIFIED what does not resolve.
2. Check the AI's one-sentence relevance claim against the paper itself (or at least a fetched abstract) before using it — never quote the AI's prose as the paper's own words.
3. Feed the "Queries actually run" list into the asset's search boundary as the record of this channel.
