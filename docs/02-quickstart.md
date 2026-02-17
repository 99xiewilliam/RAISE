# 02 Quick Start

## 安装
```bash
cd /Users/xiaohaoxie/Desktop/raise
python -m pip install -e .
```

## 评估（文本）
```bash
python -m raisex.cli.eval_cli data/datasets/triviaqa/qa.json data/datasets/triviaqa/corpus.json configs/demo.yaml both
```

## 评估（多模态）
```bash
python -m raisex.cli.eval_cli multimodal data/datasets/longbench-multifield/qa.json data/datasets/longbench-multifield/corpus.json configs/demo.yaml both
```

## Python API
```python
from raisex.api.public import evaluate_rag

res = evaluate_rag(
    qa_json_path="data/datasets/triviaqa/qa.json",
    corpus_json_path="data/datasets/triviaqa/corpus.json",
    config_path="configs/demo.yaml",
    eval_mode="both",
)
print(res["eval_report"])
```

## 算法运行
```bash
python -m raisex.cli.algo_cli --algorithm randomalgo \
  --qa_json data/datasets/triviaqa/qa.json \
  --corpus_json data/datasets/triviaqa/corpus.json \
  --config_yaml configs/algorithms/default.yaml \
  --eval_mode avg \
  --samples 1 \
  --seed 1
```
