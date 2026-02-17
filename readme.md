# raise

项目已完成架构收敛，只保留专业化新结构与新入口。

## Project Overview
**中文**：raise 是一个面向文本与多模态 RAG 的超参数搜索与评估工具，提供统一 API/CLI、可复现实验流程和分层配置体系。  
**English**: raise is a hyper-parameter search and evaluation toolkit for text and multimodal RAG with unified APIs/CLI and reproducible workflows.

## Repository Layout
```text
raise/
├── src/raisex/
├── configs/
│   ├── search_space/
│   ├── algorithms/
│   └── experiments/
├── data/
│   └── datasets/
├── docs/
├── experiments/
├── pyproject.toml
└── requirements.txt
```

## Supported Entry Points
- Python API: `from raisex.api.public import ...`
- Eval CLI: `python -m raisex.cli.eval_cli ...`
- Algo CLI: `python -m raisex.cli.algo_cli --algorithm <name> ...`

## Quick Start
```bash
cd /Users/xiaohaoxie/Desktop/raise
python -m pip install -e .
python -m raisex.cli.eval_cli data/datasets/triviaqa/qa.json data/datasets/triviaqa/corpus.json configs/demo.yaml both
```

## Docs Index
- [docs/01-overview.md](docs/01-overview.md)
- [docs/02-quickstart.md](docs/02-quickstart.md)
- [docs/03-project-structure.md](docs/03-project-structure.md)
- [docs/04-api-reference.md](docs/04-api-reference.md)
- [docs/05-cli-reference.md](docs/05-cli-reference.md)
- [docs/06-config-system.md](docs/06-config-system.md)
- [docs/07-experiments.md](docs/07-experiments.md)
- [docs/08-compatibility-matrix.md](docs/08-compatibility-matrix.md)
- [docs/09-migration-guide.md](docs/09-migration-guide.md)
- [docs/10-faq-troubleshooting.md](docs/10-faq-troubleshooting.md)
- [docs/en/README.md](docs/en/README.md)
