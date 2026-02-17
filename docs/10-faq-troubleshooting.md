# 10 FAQ & Troubleshooting

## Q1: 推荐启动方式是什么？
A: 先执行 `python -m pip install -e .`，再使用 `python -m raisex.cli.eval_cli ...`。

## Q2: 数据集路径在哪里？
A: 统一在 `data/datasets/...`。

## Q3: 配置文件路径在哪里？
A: 统一在 `configs/search_space`、`configs/algorithms`、`configs/experiments`。

## Q4: 如何调用 Python API？
A: 使用 `from raisex.api.public import ...`。
