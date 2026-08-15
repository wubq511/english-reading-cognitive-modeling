# 常设环境配置（每机一次）

登记与完成规则见 [README.md](README.md)。配置完成后 Agent 在检索前会自动识别；未配置时 Agent 会暂停检索并点名本文件。

## 待办

- [ ] **OpenAlex API key**（2026-08-15 由 Wayfinder #5 登记）。OpenAlex 匿名日额度按出口 IP 计，本机走共享代理，额度常被同出口他人烧光（HTTP 429「Insufficient budget」，UTC 零点重置；加 `mailto=` 无效）。注册免费 key——认证说明见 https://docs.openalex.org ——然后在 shell 环境中暴露为变量 `OPENALEX_API_KEY`（Agent 检索时以 `api_key=` 传递）。
- [ ] **Semantic Scholar API key**（2026-08-15 由 Wayfinder #5 登记）。无 key 时共享限流在 2026-08-15 检索中反复触发 429。在 https://www.semanticscholar.org/product/api 申请免费 key，然后暴露为环境变量 `S2_API_KEY`。

密钥只进环境变量，不进仓库、日志或任何提交文件。
