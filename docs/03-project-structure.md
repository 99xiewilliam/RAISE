# 03 Project Structure

```text
raise/
├── src/raisex/
│   ├── api/
│   ├── core/
│   ├── cli/
│   ├── pipelines/
│   │   ├── text/
│   │   └── multimodal/
│   ├── search/
│   └── llmfactory/
├── configs/
├── data/datasets/
├── experiments/
└── docs/
```

| 模块 | 职责 |
|---|---|
| `src/raisex/core` | 配置加载、校验、评估编排、算法调度 |
| `src/raisex/pipelines` | 文本/多模态 pipeline |
| `src/raisex/search/algorithms` | 搜索算法实现 |
| `configs` | 搜索空间与实验配置 |
| `data/datasets` | 数据集资源 |
| `experiments` | 大规模对比实验与分析 |
