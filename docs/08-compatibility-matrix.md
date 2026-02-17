# 08 Compatibility Matrix (Post-Cleanup)

本项目当前仅支持新接口族。

## Supported Interfaces
| Interface Type | Supported Path |
|---|---|
| Python API | `raisex.api.public` |
| Evaluation CLI | `python -m raisex.cli.eval_cli ...` |
| Algorithm CLI | `python -m raisex.cli.algo_cli --algorithm ...` |
| Search space config | `configs/search_space/*` |
| Datasets | `data/datasets/*` |

## Removed Legacy Layer
- 旧根目录入口层已整体下线。
- 旧重复配置副本已清理，仅保留 `configs/` 内版本。
