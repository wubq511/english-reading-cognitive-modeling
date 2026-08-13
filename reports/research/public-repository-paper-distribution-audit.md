# Public Repository Paper Distribution Audit

Status: `CURRENT`
Audit date: 2026-08-14
Decision scope: how public-repository collaborators and their Agents obtain the same paper originals

This is a research-engineering and rights-governance design, not legal advice.

## Conclusion

The public Git repository should **not** contain the current third-party PDF corpus by default, and Git LFS does not solve the underlying problem. The correct default is:

```text
public Git: catalog + version identity + source/license evidence + SHA-256 + tooling
local machine: verified PDF originals
acquisition: rights-cleared direct sync, otherwise exact human acquisition request
optional distribution: only version-specific rights-cleared PDFs, after separate release approval
```

This preserves Agent research quality without converting every local research copy into a public redistribution.

## First-principles requirements

A viable design must satisfy all five properties:

1. **Identity**: two researchers can prove they used the same paper version.
2. **Availability**: an Agent immediately detects missing originals rather than silently researching from metadata or memory.
3. **Legality**: the project does not infer redistribution permission from “downloadable,” “open to read,” DOI presence or local possession.
4. **Reproducibility**: the paper set used for a claim or run is machine-checkable.
5. **Operational simplicity**: a new collaborator has one preflight command and one exact recovery path.

A DOI alone satisfies bibliographic identity only partially; it does not guarantee version identity, full-text access or redistribution rights. A PDF committed to Git improves availability but may fail legality and makes immutable binary history a permanent maintenance burden.

## Current corpus facts

The current 74-file local corpus is 171,855,215 bytes (163.89 MiB); the largest PDF is 27.81 MiB. Therefore ordinary Git's single-file hard limit is not the immediate blocker. GitHub nevertheless warns on files above 50 MiB, blocks ordinary Git objects above 100 MiB, and recommends keeping repositories small, ideally below 1 GiB ([GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).

The decisive blocker is rights provenance: the original 62 recovered records still have `redistribution_status: UNKNOWN`; the 12 newly audited files split into six conservatively marked `REDISTRIBUTION_ALLOWED` and six `RESTRICTED`. Local access is not evidence of public redistribution permission.

## Why the obvious options fail

### Commit every PDF to ordinary Git

Rejected as the default.

- Public cloning makes copies available to an unrestricted audience.
- Binary replacements remain in Git history even if the working-tree file is later changed.
- The corpus will grow, while researchers need exact versions rather than arbitrary latest files.
- Removing an erroneously published PDF later requires history rewriting and does not retract copies already obtained.

### Put every PDF in Git LFS

Rejected as the default.

Git LFS changes storage mechanics, not copyright status. It also gives a weaker failure mode than the proposed preflight: when quota is exhausted, clones may retrieve pointer files rather than actual content. GitHub currently measures full-file versions against the repository owner's storage and collaborator/fork downloads against the repository owner's bandwidth; GitHub Free includes 10 GiB storage and 10 GiB monthly bandwidth ([Git LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)). That is workable for some rights-cleared assets, but it is not a reliable or rights-aware paper dependency manager.

### Upload every PDF as a GitHub Release asset

Rejected as the default; allowed only for audited, redistribution-cleared versions after explicit publication approval.

GitHub Releases currently permit up to 1,000 assets per release, each below 2 GiB, with no total release-size or bandwidth limit ([GitHub Releases quotas](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases#storage-and-bandwidth-quotas)). This solves capacity, not permission. Release publication also creates a public distribution endpoint and is therefore a separate red-line action.

### Share a private folder containing every PDF

Not a universal solution. It may be appropriate under an institution-approved group license or access-controlled collaboration agreement, but the project cannot assume that a personal cloud folder has the necessary sharing rights. It also leaves Agents without version, checksum and missing-file enforcement unless it uses the same catalog contract.

## Rights boundary

Under the current Chinese Copyright Law, reproduction and making works available over information networks are rights controlled by the copyright owner. The research/teaching exceptions include personal research and, in a narrower institutional setting, limited copying for teaching or scientific researchers; the latter explicitly may not be published or distributed. Publicly posting a complete paper to an unrestricted GitHub repository should therefore not be treated as the same act as keeping a lawful local research copy ([Copyright Law of the People's Republic of China, Articles 10 and 24](https://www.npc.gov.cn/c2/c30834/202011/t20201119_308796.html)).

For this project, a PDF is publicly redistributable only when the **specific local version** has affirmative evidence such as:

- a license permitting redistribution (for example, an applicable Creative Commons license);
- public-domain status;
- explicit author/publisher permission covering this distribution; or
- another documented legal basis reviewed for this use.

“Open access,” an accessible author webpage, ResearchGate availability, a DOI, or lack of a login screen is not by itself a redistribution license.

## Implemented collaboration contract

The repository now treats papers as content-addressed research dependencies:

1. `papers/catalog.yaml` records stable ID, work/version metadata, expected local path, SHA-256, requirement state, source URL, direct-download URL and redistribution status.
2. `papers/checksums.sha256` freezes the exact local bytes used by the project.
3. `scripts/papers doctor` fails closed if a required PDF is missing, not a PDF, or has different bytes. The error contains ID, DOI/source, target path and import command.
4. `scripts/papers sync` auto-downloads only HTTPS files marked `acquisition_status: DIRECT_PUBLIC`. Acquisition status is independent of redistribution status: an official free-download endpoint may support a lawful local copy while its PDF remains `RESTRICTED` from public redistribution. Redirects are revalidated and credentials are never embedded.
5. `scripts/papers import ID FILE` verifies the PDF magic and expected SHA-256, installs atomically and never overwrites different content.
6. `scripts/verify` checks the catalog-backed paper state together with project links and provenance manifests.

This means an Agent starting from a clone cannot silently continue without the full corpus:

```bash
scripts/papers doctor
scripts/papers sync
scripts/papers doctor
```

If an item remains unavailable, the Agent must stop the full-text-dependent task and ask its user to lawfully obtain the exact work/version, then run:

```bash
scripts/papers import PAPER_ID /path/to/downloaded.pdf
scripts/papers doctor
```

## Acquisition state machine

| State | Machine action | Human action | Public redistribution |
| --- | --- | --- | --- |
| `OPEN_ACCESS` / `PUBLIC_DOMAIN` / `REDISTRIBUTION_ALLOWED` with verified HTTPS download | `sync` downloads and validates | none | only if the recorded license also covers redistribution of this exact version and publication is separately approved |
| Free-to-read or author manuscript, rights not yet verified | fail closed / manual list | verify source, version and license; then update catalog | no |
| Subscription/paywalled but lawfully accessible to collaborator | fail closed / manual list | download through own authorized institutional access and `import` | no |
| No lawful access channel found | fail closed | request author/library/lab assistance or replace the dependency with an explicitly justified source | no |
| Different PDF version obtained | hash mismatch | register as a distinct version or obtain the expected version; never silently substitute | depends on that version's rights |

## Agent rules

- Never summarize a required paper from title/abstract snippets when `doctor` reports its PDF missing.
- Never bypass authentication, publisher controls or institutional access conditions.
- Never change a catalog hash to make an arbitrary download pass.
- A version substitution is a research change: register provenance, compare relevant passages and update affected claims.
- Record the catalog/checksum snapshot in experiments and literature audits.
- When only part of the corpus is needed, a future scoped manifest may narrow the preflight, but the scope must be explicit and frozen; silent partial availability is forbidden.

## Future extension, only if needed

If collaboration scale makes manual acquisition burdensome, add an institution-controlled paper cache behind authenticated access. It should expose objects by SHA-256 and enforce per-item authorization while retaining the same public catalog. The public repository remains the coordination and provenance layer; the private cache is an optional transport layer. Do not introduce DVC, object storage or a reference manager merely for architectural completeness: adopt one only after measuring repeated acquisition failures and confirming institutional rights and governance.

## Decision

The user's proposed “PDFs remain on each member's computer; pull triggers immediate download or a human request” is retained, with two corrections:

1. a DOI is not enough—the manifest freezes the exact version, expected bytes, source and rights state;
2. an Agent does not merely receive a reminder—the preflight fails closed until required originals are present and verified.

No third-party PDF will enter the first public Git history. Rights-cleared PDFs may later be published as a separately reviewed release or dataset, never by blanket rule.
