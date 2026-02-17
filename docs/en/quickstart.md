# Quickstart (EN)

## Install
```bash
cd /Users/xiaohaoxie/Desktop/raise
python -m pip install -e .
```

## Evaluate
```bash
python -m raisex.cli.eval_cli data/datasets/triviaqa/qa.json data/datasets/triviaqa/corpus.json configs/demo.yaml both
```

## Run algorithm
```bash
python -m raisex.cli.algo_cli --algorithm randomalgo --help
```
