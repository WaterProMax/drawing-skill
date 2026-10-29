# Drawing Skill 结构校验

这些检查保护 `drawing-skill` 的目录、版本和治理用例。它们不是画图时要加载的运行时参考。

## 怎么跑

在仓库根目录执行：

```bash
python3 tests/validate_structure.py
```

通过时进程退出码为 0，并打印多行 `PASS`。任一检查失败会打印 `FAIL:` 并以退出码 1 结束。

## 脚本检查什么

`tests/validate_structure.py` 会确认：

- `SKILL.md` 前置存在，`name` 为 `drawing-skill`，`metadata.version` 为 `0.8.0`，`visual_preset` 为 `aicareer-blueprint`，并且描述里保留别名 `aicareer-diagram-style`；
- `SKILL.md` 体积不超过 20000 字符，仍写明四种任务模式和 `PASS` / `REVISE` / `REJECT` / `BLOCKED`；
- `SKILL.md` 与 `README.md` 里出现的 `references/...`、`templates/...`、`assets/...` 路径在磁盘上真实存在；
- 已退役的短笔记不再作为独立文件残留，也不再被 `SKILL.md` 或 `README.md` 引用；
- 合并后的 `references/diagram-routing.md`、`references/generation-gates.md`、`references/topology-preservation.md`、`references/semantic-color-policy.md` 仍包含原先短笔记里的规则原文；
- `templates/*.yaml` 都能被 YAML 解析，且带有各自必需字段（含编辑契约「最多两次局部返修、默认禁止整图重生成」）；
- `tests/regression-cases.yaml` 能被解析，每条用例都有 `id`、`name`、`task_mode`、`input` 和 `expected.status` / `required_action` / `forbidden_actions`；
- `SKILL.md`、`README.md` 标题和 `CHANGELOG.md` 最新条目的当前版本都是 `v0.8.0`。

## 回归用例

`regression-cases.yaml` 是行为规格，不会真的去调用图像模型。它锁住这些治理结果：

- `create-new` 缺少源事实 → `BLOCKED`；
- `edit-existing` 只改一处文字 → 必须写 Edit Contract、Preservation Ledger、Canonical Content Lock 和 Differential Verification，而不是整图重画；
- 公式失真且两次局部生成式返修都失败 → `REJECT` 并升级到 `deterministic-render`；
- 非蓝占比超过约 10%，或整卡非蓝填充 → 颜色 QA `REJECT`；
- 约 160 mm 的 Word 插图带外圈整框或重复标题 → `REJECT`。

另外覆盖了原图缺失、视觉预设切换仍不放宽门禁，以及超限时序图禁止纯图像重画消息几何。
