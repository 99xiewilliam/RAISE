# 05 CLI Reference

## Eval CLI
```bash
python -m raisex.cli.eval_cli <qa_json> <corpus_json> <config_yaml> [eval_mode]
python -m raisex.cli.eval_cli multimodal <qa_json> <corpus_json> <config_yaml> [eval_mode]
```

## Algo CLI
```bash
python -m raisex.cli.algo_cli --algorithm <name> --qa_json ... --corpus_json ... --config_yaml ...
```

## 常用参数
- `--qa_json`
- `--corpus_json`
- `--config_yaml`
- `--eval_mode`
- `--score_weights`
