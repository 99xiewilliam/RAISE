# 06 Config System

## 配置目录
- 搜索空间：`configs/search_space/text.yaml`、`configs/search_space/multimodal.yaml`
- 算法配置：`configs/algorithms/default.yaml`
- 实验配置：`configs/experiments/*.yaml`

## 解析优先级
1. 显式传入路径
2. 环境变量（`RAGSEARCH_CONFIG` / `RAGSEARCH_CONFIG_MULTIMODAL`）
3. 默认新路径（`configs/search_space/*`）
