# Run artifacts

`artifacts/` 保存机器运行输出，不是 canonical 结论层。每次实验写入独立 `runs/<experiment_id>/<run_id>/`，禁止覆盖旧 run；目录至少包含 run manifest、日志、metric 输出和文件 hash。

大体积运行目录默认不进 Git。需要协作的结果应发布经审查的小型 summary/manifest，正式解释写入 `reports/` 并回链 run ID。人类原始数据、AI provider 原始敏感 payload、密钥和身份信息不得进入可公开 artifact。
