# Wayfinder #6 决策记录：baseline 作答 UI 候选变体与不变量仪器行为

> Status: `CURRENT`
> 决策票：[Freeze baseline UI variants and invariant instrument behavior](https://github.com/wubq511/english-reading-cognitive-modeling/issues/6)（父地图 [#2](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2)）
> 票型：`wayfinder:prototype`
> 决议日期：2026-08-22

## 结论速览

- **核心结论**：baseline 候选变体集 = 参照系 V0（已锁定的双栏低干扰设计）+ 五个单因子变体——V1 纵向堆叠布局、V2 侧栏导航、V3 篇章分页、V4 拖拽排除（含 WCAG 强制的单指替代路径）、V5 可见倒计时。每个变体相对 V0 只改一个因子；8 条不变量合同在所有变体下不得破坏。本票冻结的是**候选集与不变量**，不断言任何变体在测量上更优——方向性主张超出预 H2 主张预算。
- **怎么得出的**：因子选择全部锚在 [#5 证据审计](../research/ui-instrument-effects-evidence-audit.md)（UIE-01..64）的主张分级上；一次性单文件 HTML 原型把六个变体做成可亲手操作的单因子对照，六个变体共享完全相同的 canonical V1 事件发射器，使「不变量是否可比」可现场核查。
- **未决项**：within-mode 变体构念等价性文献不可证伪，只能由 H2-gated 变体研究回答；计时政策终案、V3 翻页是否触发 schema v1.1、指针采样率与设备/浏览器范围冻结流向 #8；变体 estimand 与探索-确认边界流向 #13。

## 问题

哪些 baseline 作答 UI 候选变体应当被原型化；变体之间允许哪些单因子差异；哪些交互/状态/事件/无障碍属性必须保持 invariant。决议依据与门禁：低干扰 paper-native 边界、无障碍/设备范围、raw-event 语义、H1 `NONRESEARCH_DEBUG_ONLY` 规则；原型反应是决策，不是研究数据。

## 决议一：候选变体集（每变体 = V0 + 恰好一个因子）

V0 参照系为 `reports/synthesis/SYSTEM_DESIGN.md` §2 的已锁定设计：篇章独立滚动、一次一题、Prev/Next + 题号跳转、选文/划线/删划线、排除/恢复、自由改答案、无强制顺序/逐题提交/解释/confidence。

| 变体 | 单因子（相对 V0） | 证据锚点（判定见 #5 审计） | 留给人的判决点 |
| --- | --- | --- | --- |
| V1 纵向堆叠 | 空间排布：左右双栏 → 上下堆叠（改滚动需求与 split-attention 方向） | UIE-34：屏上距离/滚动需求改变交互时序（B=.264, p<.001；「不应要求滚动」），`METHOD-016` PDF pp.7–10；UIE-37：空间整合降解题时间 74.7→55.4s（γ=−0.27, p<.001）但成绩 null，`METHOD-033`（几何 MC，迁移阅读为 `PROJECT-INFERENCE`）；UIE-24：SC 1.4.10 要求 320 CSS px 等效宽度重排（`STANDARD-003`） | V1 几乎必然是 V0 在 reflow 下的法定终态（合同义务）；但它是否也作为**起始布局**进 H2 变体研究是另一个问题 |
| V2 侧栏导航 | 导航方案：题号行 → 常驻题目列表侧栏（改导航 affordance 与访问成本） | UIE-03：布局 affordance 塑造导航选择（`B2` p.10，`PARTIAL`）；UIE-04：访问需求移动导航量与导航-成绩关系（b=3.16/0.35，`B3` pp.7, 11–12）；UIE-56：导航增量预测 ΔR²≈23%、回访意义任务依赖（`METHOD-024` pp.98–103） | 导航分布变 →「未导航」的缺失成因也变，直接影响导航派生指标口径 |
| V3 篇章分页 | 篇章导航：连续滚动 → 离散翻页 | UIE-12：分页是压缩可观察行为空间的设计决策（`B7` pp.4–5）；UIE-56：PISA 页级导航 → 区域可见性的映射是未验证 `PROJECT-INFERENCE` | canonical V1 无翻页事件：要么接受观测压缩，要么扩 schema（=仪器合同变更，不是 UI 小改），二选一须显式记录 |
| V4 拖拽排除 | 排除操作反应格式：按钮切换 → 拖入托盘 + SC 2.5.7 强制单指替代（按钮保留） | UIE-01/02：反应格式同时移动过程指标与产品分数（OR=1.40，任务权变），`B7` pp.1, 6, 9；UIE-31：表面特征移动策略分布（log-OR 4.690/0.922, p<.001），`METHOD-016` pp.6–9；UIE-35：格式移动三种阅读任务的执行层指标（时间 d=−0.62、点击 d=−1.13）且低表现亚组分数 d=0.57，`METHOD-032` pp.12–22；UIE-58：格式是操作性阅读机考脱离行为最强预测因子（simple MC RG OR=23.10），`METHOD-023` pp.15–20；UIE-23：SC 2.5.7 单指针替代（`STANDARD-003`） | 格式因子是唯一有「移动 estimand」直接证据的层级，故入选；但替代路径本身是另一种反应格式，两路径过程可比性不能假定、必须实测 |
| V5 可见倒计时 | 计时显示：无 → 有（原型仅显示、不强制执行） | UIE-25：SC 2.2.1 计时可调；援引「essential」例外 = 构念主张（`STANDARD-003`）；UIE-46：时间压力调节模式效应（限时 −0.26 vs 自定 −0.09，QB=4.12, p=.04），`METHOD-018` pp.9–13；UIE-50：限时 −0.468 vs 自由 +0.192（ns），`METHOD-022`；UIE-61：是否设时限本身是构念决策（`METHOD-026` pp.2–3） | baseline 限不限时、限值、显示方式都不是工程默认值，是构念主张，必须在仪器合同显式声明 |

## 决议二：不变量合同（8 条，任何变体不得破坏）

1. **事件词汇与字段 invariant**：canonical V1 词汇（`session_started` / `session_submitted` / `question_navigated` / `answer_option_clicked` / `option_elimination_toggled` / `text_selection_committed` / `underline_created` / `underline_removed` / `passage_scroll_sampled` / `passage_scroll_ended` / `viewport_changed` / `visibility_changed` / `layout_changed` / `pointer_sampled`）与必备字段（UTC `wall_time`、单调 `mono_ms`、session-local `sequence`、type+schema version、语义对象 ID、当时 UI/layout context、producer/version）逐变体相同；append-only；raw 事件不写认知标签。
2. **一次一题**；`displayed_question_id` 只是 UI context，不得当作学生思考内容的证据。
3. **自由跳题、自由改答案、排除/恢复**；不强制顺序、不逐题提交、不要求解释或 confidence（`COL-L2` 仅研究面）。
4. **无对错反馈、无提示、无自适应**——反馈会重组行为并改变被测构念（UIE-07）。
5. **篇章动作不自动归属当前显示题**（SYSTEM_DESIGN §2 锁定）。
6. **缺席信号 = 设计依赖状态**，不是仪器故障，绝不插补（UIE-11：66.3% 无导航；UIE-13：光标 58.8% 时间不活跃）。
7. **变体不得新增事件类型**；需要新词汇 = 仪器合同变更 + schema 版本升级（V3 翻页即演示案例）。
8. **WCAG 2.2 地板**：SC 2.5.7（拖拽必有单指替代）、SC 1.4.10（320px 重排）、SC 2.2.1（计时可调；essential 例外 = 记录的构念主张）、SC 2.5.8（指针目标 ≥24×24 CSS px）。

## 被否替代

- **Mouselab 式隐藏正文**：用改变自然搜索过程换取整洁观测，SYSTEM_DESIGN §2 已锁定否决。
- **对错反馈/提示/自适应**：改变被测构念（UIE-07）；baseline 是测量仪器不是教学系统。
- **逐题提交/提交锁定**：消灭答案修改行为，违反锁定边界。
- **作答中要求解释/confidence**：属 `COL-L2`，仅研究面可用。
- **多因子捆绑变体**：效应不可归因，违背单因子对照的全部意义。
- **纯视觉变体（配色/字体/密度）**：非仪器层结构因子；措辞粒度级变化在 N=206,153 中零效应（UIE-40）划定了粒度下限。
- **侧栏带作答状态点**：把进度可见性混入导航因子造成混杂；如需要应单列因子。
- **给分页变体偷加翻页事件类型**：词汇表变更必须走仪器合同（不变量 7），不能借 UI 变体偷跑。

## 污染风险

- 原型不是仪器：时序常量、采样率、DOM 与真实 runtime 不同，`BENCH-E0` 必须在真仪器上重建信度证据。
- 原型篇章/题目为合成占位，不是 Candidate Bank 资产，不支持任何题目级主张。
- 任何人（含团队成员）对原型的反应是设计决策，不是研究数据；不触发 H1/H2，但也不得入档为证据。
- 凭偏好或「感觉更好」选变体违背 #5 证据（Class-1 缺口为领域共识级，UIE-61）；本票只冻结候选集，方向性断言一律留待 H2。
- 冻结后的任何变体变更都是潜在 estimand 变更，必须版本化为仪器变更。

## 不确定性与下游含义

- **→ #8（BENCH-E0 logging/replay 验收合同）**：canonical V1 词汇与字段冻结；V3 暴露的翻页事件取舍（schema v1.1 与否）；V5 暴露的计时政策（计时器状态属被记录 UI context）；指针采样率/空闲语义（已发表仪器论文自身即省略采样率，#5 审计 Class-3 节）；320px reflow 合规的实测义务。
- **→ #13（UI-variant estimands 与探索-确认边界）**：各因子 estimand 假设、亚组交互（UIE-35）与缺失口径。
- **→ H2-gated 变体研究**：within-mode 变体构念等价性只能真人实测；探索性 pilot 数据不得同时充当确认性证据。
- 设备/浏览器范围冻结按 `METHOD-015` 举证责任规则处理（UIE-30）。

## 证据与资产

- 证据基础：[`reports/research/ui-instrument-effects-evidence-audit.md`](../research/ui-instrument-effects-evidence-audit.md)（#5 决议记录：[`wayfinder-5-ui-instrument-effects.md`](wayfinder-5-ui-instrument-effects.md)）；设计边界：`reports/synthesis/SYSTEM_DESIGN.md` §2/§4。
- 决策辅助原型（一次性，非仪器、非证据）：分支 `kimi/robert/issue-6-ui-variant-prototype`，路径 `tmp/prototypes/issue-6-ui-variants/`（`index.html` 六变体可交互原型、`explainer.html` 图文说明、`shots/` 验证截图）。
- 原型验证（2026-08-22，Playwright 真实浏览器）：六个变体渲染正确、console 零错误；V0 作答/排除/导航触发正确事件且派生状态可由事件流重算；V4 拖入托盘触发 `option_elimination_toggled {mechanism:"drag"}` 且单指按钮路径保留（`mechanism:"button"`）；V3 翻页确认产生零 canonical 事件（设计意图）；V5 倒计时运行。

## 评审与谱系

2026-08-22 以聊天简报 + 可交互原型 + `explainer.html` 图文说明提交研究成员审查并获 sign-off；决议记录按 [ADR 0008](../../docs/adr/0008-wayfinder-decision-records-in-repo.md) 落档为本文件，resolution 摘要评论发布于 #6。
