# Canonical Claim Ledger

Source IDs:

- `CHAT-1/2/3`: complete transcript and turn number;
- `HO-1/2`: handoff files;
- `USER-LOCAL-2026-08-14`: decisions made during local recovery;
- paper IDs resolve through `papers/catalog.yaml`.

Line numbers refer to the frozen local recovery files and are protected by `RAW_SOURCE_MANIFEST.sha256`.

| Claim | State | Recovery locator | Scientific evidence requirement |
| --- | --- | --- | --- |
| Project seeks process/cognition/skill evidence beyond final correctness | `SOURCE-RECOVERED` | `CHAT-1/T1/L40+`; `HO-1/L9-L34` | research question, not external fact |
| First build a runtime baseline without LLM/Agent; later vertical/horizontal AI extensions | `SOURCE-RECOVERED + CURRENT-DECISION` | `CHAT-1/T16/L6768+`; `CHAT-2/T2/L60-L74`; `HO-2/L39-L72`; user local clarification | AI policy governs experiments |
| AI is allowed and important for research, experiments and synthetic assistance | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | `AI_RESEARCH_TOOLING_POLICY.md` |
| Low-interference UI uses left passage, one question at right, free navigation, underline/eliminate/change | `SOURCE-RECOVERED` | `CHAT-1/T14/L4251+`; `HO-1/L81-L113`; `HO-2/L190-L226` | usability must still be tested |
| Raw events must not contain cognition and should be append-only/object-centric | `SOURCE-RECOVERED + PROJECT-INFERENCE` | `CHAT-1/T12/L3181+`; `HO-1/L155-L218`; `HO-2/L259-L316` | instrumentation benchmark required |
| Viewport/pointer/dwell/revisit cannot be directly equated with attention/difficulty/confusion | `SOURCE-RECOVERED + PAPER-SUPPORTED` | `CHAT-1/T8/L1753+`; `HO-2/L118-L188` | B/C report Evidence Index |
| The final architecture is a layered partial-observation evidence system | `PROJECT-INFERENCE` | `HO-2/L318-L421` | synthesis of A–E/UIB, not a single-paper claim |
| Unknown and competing hypotheses are mandatory | `SOURCE-RECOVERED + MEASUREMENT-LOGIC` | `CHAT-2/T23/L10443+`; `CHAT-3/T7/L725-L1857`; `HO-2/L118-L188` | validate abstention/calibration |
| Phase 2A item-independent design is closed, Phase 2B waits for items/pilot | `SOURCE-RECOVERED` | `CHAT-3/T7/L725-L1857` | design status only |
| Phase 3 has a draft, not a completed benchmark | `VERIFIED-CURRENT` | `CHAT-3/T8/L1863-L2305`; `T9/L2306-L2318` | local repo has no runs/results |
| Phase 4 was announced but not delivered in raw chat | `VERIFIED-CURRENT` | `CHAT-3/T10/L2319-L2331` | package additions cannot upgrade status |
| Multiple algorithm candidates must be resolved by local experiments | `SOURCE-RECOVERED` | `CHAT-2/T21/L10413-L10439`; `HO-2/L74-L116` | same-data benchmark |
| Synthetic data cannot establish real behavior→cognition validity | `SOURCE-RECOVERED + PAPER-SUPPORTED` | `HO-2/L902-L1011`; `CHAT-3/T8/L1869+` | AI policy sources + human anchor data |
| Webcam and eye tracking are optional research sub-studies, not baseline dependencies | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | M1 ethics gate before use |
| H1 casual testing is debug-only; research data starts at H2 | `CURRENT-DECISION + OFFICIAL-RULE` | `USER-LOCAL-2026-08-14` | `HUMAN_RESEARCH_GATES.md` |
| Raw chats remain local frozen evidence, not daily assets or public Git content | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | source policy + checksums |
| PDFs use manifest/local cache and rights-aware sync rather than blanket public Git | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | per-paper rights audit still open |
| A public download endpoint and public redistribution permission are independent states | `OFFICIAL-RULE + CURRENT-DESIGN` | `USER-LOCAL-2026-08-14`; copyright/GitHub audit | `acquisition_status` and `redistribution_status` remain separate in catalog |
| The 2026 J. Intell. study directly inherits attributes/Q-matrices from TSC 2026, not an explicitly declared 2022 data lineage | `PRIMARY-SOURCE-SUPPORTED` | `ITEM-001`; Phase 0 source audit | 2022→2026 same test/matrix is `NOT FOUND`; family relation only `INFERENCE` |
| J. Intell. S2 contains a 20-item test but is not a deployable gold item bank | `PRIMARY-SOURCE-SUPPORTED` | `ITEM-002`; Phase 0 source audit | independent answer key, evidence spans and item-level rights required |
