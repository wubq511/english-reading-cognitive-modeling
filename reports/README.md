# Reports

`reports/` 是项目的 canonical 研究资产层。新研究从这里开始，不从网页聊天或迁移包开始。

## Navigation

- [`project_state/`](project_state/)：当前状态、研究问题、路线图。
- [`synthesis/`](synthesis/)：恢复后的系统设计、可观测性、测量验证、benchmark 和文献综合。
- [`protocols/`](protocols/)：AI、真人研究、数据和实验门禁。
- [`research/`](research/)：回到论文原文、标准和官方来源形成的专项审计。
- [`provenance/`](provenance/)：来源权威、冲突、恢复记录、论文 crosswalk。
- [`literature/a-e/`](literature/a-e/)：A/A+/B/C/D/E 深读报告；旧 basename 与 provenance 缺口由 crosswalk 记录。
- [`literature/ui-interaction/`](literature/ui-interaction/)：UI 行为论文笔记与稳定编号映射。

## Evidence labels

Canonical 报告中的重要判断应使用下列状态之一：

- `OBSERVED`：由当前文件、代码或实验直接证明。
- `SOURCE-RECOVERED`：完整聊天/handoff 明确记录，但本地尚未重新实验。
- `PAPER-SUPPORTED`：已由论文原文或正式标准核验。
- `PROJECT-INFERENCE`：项目从多项证据作出的设计推论。
- `EXPERIMENT-GATE`：存在合理候选，必须由本项目实验裁决。
- `OPEN`：证据或必要资产不足。
- `REJECTED`：因逻辑、测量或治理边界不采用。

预测准确率、模型拟合、simulation recovery 和人类构念效度必须分别报告。
