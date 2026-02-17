# 09 Migration Guide

## 必做迁移
1. API 导入切换到 `raisex.api.public`。
2. CLI 切换到 `python -m raisex.cli.eval_cli` 与 `python -m raisex.cli.algo_cli`。
3. 数据路径切换到 `data/datasets/...`。
4. 配置路径切换到 `configs/...`。

## 核验
- 新入口命令能执行。
- 返回结构字段与迁移前一致。
