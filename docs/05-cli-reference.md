# 05 CLI Reference

## Eval CLI
```bash
python -m raisex.cli.eval_cli <qa_json> <corpus_json> <config_yaml> [eval_mode]
python -m raisex.cli.eval_cli multimodal <qa_json> <corpus_json> <config_yaml> [eval_mode]
```

## Algo CLI
```bash
python -m raisex.cli.algo_cli --algorithm <name> --qa_json ... --corpus_json ... --config_yaml ...
python -m raisex.cli.algo_cli --algorithms randomalgo,greedy --qa_json ... --corpus_json ... --config_yaml ...
```

## 常用参数
- `--algorithm`（单算法）
- `--algorithms`（逗号分隔多算法）
- `--qa_json`
- `--corpus_json`
- `--config_yaml`
- `--eval_mode`
- `--score_weights`
- `--verbose`（输出 report_path/stdout/stderr）

## 默认输出与退出码
- 默认输出：JSON 数组，元素结构为 `algorithm + metrics + status`。
- `--algorithm` 也使用同一数组结构（长度为 1）。
- 部分失败策略：若任一算法失败，CLI 退出码为 `1`，但会继续输出其他算法结果。
