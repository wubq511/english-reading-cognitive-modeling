# Recovery Log

## 2026-08-14 — Local canonical recovery

### Inputs audited

- `chat1.md`: 22 turns, 8,044 lines, SHA-256 `e4179574…9534`；
- `chat2.md`: 28 turns, 10,923 lines, SHA-256 `b0e65242…e6b7`；
- `chat3.md`: 12 turns, 2,377 lines, SHA-256 `e99ddc00…702c`；
- `handoff1to2.md`: 936 lines, SHA-256 `009cd698…35d9`；
- `handoff2to3.md`: 1,823 lines, SHA-256 `018a9c62…97a`；
- migration package: checksum 文件自身与包内 checksum 均通过；这只证明包未损坏，不证明总结无损或科学结论正确。

两份 migration-package legacy handoff 与 `handoff/` 对应文件逐字节相同。`integrated_synthesis_snapshot.txt` 是 GPT 综合稿，保留不可解析的网页附件引用，不作为独立论文证据。

### Existing assets audited at recovery start

- A–E: 44 PDFs + 6 deep-reading reports；
- UI behavior: 18 PDFs + 2 notes/index files；
- 初始 62/62 PDF 可由 Poppler 解析并提取首页文本，0 加密；
- 0 个 byte-identical PDF；D5/UIB-005 与 D6/UIB-007 是同一学术作品的不同 PDF 版本；
- 34 个 B–E 报告旧 PDF basename 与当前路径不一致；已由 crosswalk 解析；
- UI 旧“论文 1–18”与稳定 UIB ID 已建立 crosswalk；`UIB-088` 暂不纠正。

### Contradictions resolved

- migration package 的“package wins”规则被当前用户来源政策覆盖；
- Phase 0/3/4 的完成状态下调到 raw evidence 支持的真实级别；
- package-only 的 ADEMP/DOE/OC-Bench/T0–T18/tool stack 降级为 proposal；
- “无 AI”边界澄清为 runtime baseline，不禁止研究/实验外环使用 AI；
- 真人 casual test 拆为 H1 debug-only 与 H2 research pilot；
- 第三方 PDF 从“全部传 GitHub”改为 rights-aware manifest + local cache + fail-closed preflight。

### Canonical assets created

- root navigation and Agent rules；
- project state, research questions and roadmap；
- system, observability, measurement, benchmark and literature synthesis；
- source policy, conflict register, claim ledger, asset map and raw checksum manifest；
- AI tooling and human research protocols；
- typed source catalog, checksum file and source/report crosswalk（初始 62 份，首轮专项审计后 74 份，本轮用户原文补齐后 80 份）；
- local source collaboration CLI、`tmp/pdfs` 收件箱和自动 Git hooks（由测试与 verifier 证明）。

### Primary-source augmentation after recovery

- Phase 0 审计回到 J. Intell./TSC/CSE/PELDiaG/Jin & Liu 及 OECD/IEA/NCES 官方来源；`DOMAIN-004` 到手后，2022/TSC 的初始/最终题数、6+2 属性、专家/学生流程及 `20×8` Q-matrix 已足以确认共享研发谱系，但同题本文字与响应数据复用仍保持 `NOT FOUND/INFERENCE`；
- 新增 3 份 Phase 0 本地全文/附件；S2 虽含 20 题，但无独立官方 answer key 与 item-level rights，不升级为可用 Candidate Bank；
- 方法/治理审计覆盖两份协议的 25/25 个外部来源，新增 7 份方法原文和 2 份标准；
- 当前 catalog 为 80 份；每份区分 `asset_type`、`acquisition_status` 与 `redistribution_status`，免费可下载不再被误当成可公开再分发；
- 用户补齐 TSC 2026、PELDiaG 2021、Ma & Du 2022、Shin 2025 与 GRRAS，并新增 Zhang et al. 2024；当前没有未完成的论文全文获取项，Phase 0 的外部依赖转为题本、答案、数据、谱系声明与使用权；
- 高杠杆文献主张已对 7 份本地 PDF 作重点复核，固定 `SUPPORTED/PARTIAL/PROJECT-INFERENCE/OVERSTATED` 边界。

### Explicitly not done yet

- no runtime system/code implementation；
- no benchmark or empirical result；
- no human recruitment/data collection；
- no GitHub remote/publication；
- no destructive cleanup of raw materials；
- no claim that all cited method papers or item assets are locally complete；
- historical `interation`/`chatgpt_A-E` directories were physically reorganized only after catalog and crosswalk creation; this item is now complete。
