# Drawing Skill (`drawing-skill` `v0.8.0`)

> **画图 Skill — 技术图的生成与保真约束编辑：架构图、机制图、时序图、研究路线图与实验图**  
> **General Technical Diagram Generation & Fidelity-Constrained Editing**

默认视觉预设是 **AICareer Research Engineering Blueprint**（`visual_preset = aicareer-blueprint`，参考图 `assets/reference-blueprint.png`）。课程、比赛或业务项目可以换一套视觉预设；任务模式路由、源事实门禁、正文锁定、不可变基线、差分核验和确定性升级这些治理规则不跟着换掉。

旧名 `aicareer-diagram-style`（v0.7.x）仍是别名。`.agents/skills/drawing-skill/` 与 `.agents/skills/aicareer-diagram-style/` 加载的是同一份技能。

---

## 为什么需要这个 Skill？（团队 AI 协作三件套）

团队里三份技能各管一段，交接时不互相改写对方的真源：

1. 🛠️ **开发 Skill（[`WaterProMax/dev-skill`](https://github.com/WaterProMax/dev-skill)）**：从一句话需求收到可验收的契约、文件白名单和不变量。架构边界、模块职责、状态枚举以契约为准。
2. 📝 **写作 Skill（[`WaterProMax/writing-skill`](https://github.com/WaterProMax/writing-skill)）**：把仓库证据写成知识库、申报书或技术文档，并逐行核对断言。正文里的图注、公式和结论必须能回到证据，不能靠配图“补完”。
3. 🎨 **画图 Skill（本仓库 `WaterProMax/drawing-skill`）**：把已经说清楚的结构画成可放进 Word 的技术图，并在改图时锁住没被点名的区域。

交接方式：

- `dev-skill` 的契约、模块边界和状态机是图的**事实来源**。图不发明契约里没有的调用、存储或评测结论。
- `writing-skill` 引用成图时，图注写在文档侧。图内不再重复一整条标题，也不要把知识库目录画成架构。
- 图若发现事实不够，返回 `BLOCKED`，把缺口交回开发或写作去补证据，而不是在像素里编一个看起来完整的闭环。

---

## `v0.8.0` 核心机制一览

### 1. 四种任务模式（Task Mode）

先读 `references/task-mode-router.md`。禁止把编辑悄悄换成整图重画。

| 模式 | 何时使用 | 硬要求 |
|---|---|---|
| **`create-new`** | 没有可修改的原图，从零画一张 | 先过源事实门禁和语义审查；`Ready to Generate = NO` 就停 |
| **`edit-existing`** | 在已有图片 / 矢量 / 文档对象上改字、改色、改局部 | 点名的区域可变，其余默认不可变；必须留下 Edit Contract、Preservation Ledger、Canonical Content Lock、Differential Verification |
| **`reconstruct-approved`** | 原件无法对象级编辑，且用户**明确同意**重绘 | 重绘是按锁定规范新做一张图，不宣称像素级保留 |
| **`deterministic-render`** | 公式、密集中文、严格拓扑、复杂时序，或局部生成修了两次仍不稳 | 改走 SVG、HTML+CSS、Mermaid、Draw.io、原矢量或确定性叠层 |

### 2. 状态词与 Source Completeness Gate

全技能评审只用四个互不相同的状态：

| 状态 | 含义 |
|---|---|
| **`PASS`** | 请求的变更正确，且无关内容没有被改动 |
| **`REVISE`** | 技术含义还在，但保真、版式或颜色需要局部返工 |
| **`REJECT`** | 未授权改动、公式或拓扑失真、颜色越界，或语义被改写 |
| **`BLOCKED`** | 源事实不够、原件不可用，或当前画法达不到所需保真。这是治理结果，不是渲染失败 |

动笔前的 Source Completeness Gate（`references/generation-gates.md`）另用三个内部记号：

- `READY`：事实够用；
- `READY_NEUTRAL`：只够画中性结构；
- `BLOCKED`：再往下画就必须编造。

映射、已评测的对比、时间演化分类、分支去向、时序端点，都要有明确证据。语义审查输出 `Ready to Generate: YES/NO`，为 `NO` 时停止。

### 3. 不可变基线与 Canonical Content Lock

编辑前把每个区域分成「点名要改」和「没点名」。没点名的一律锁死，包括：

- 正文与标题原文；
- 中文字形；
- 数字和单位；
- 公式（变量、上下标、系数、运算符、括号、函数嵌套、参数顺序）；
- 拓扑（箭头、端点、虚实线、容器、分组、回路、分支）；
- 有意保留的换行、层级和未受影响的颜色角色。

图像模型负责**渲染**这些内容，不负责**改写**它们。公式看起来像是不够的。

### 4. Blueprint-Blue 结构主导（5–8% 非蓝点缀）

默认预设里，蓝族是唯一的结构色：主流程、模块边框、分组边界、常规图标走 `references/visual-baseline.md` 里的蓝。非蓝只做小范围点缀或显式声明的局部状态。

- 普通图的非蓝视觉占比目标约 **5–8%**，常规上限约 **10%**。
- 超过约 10%，或整张卡片 / 整个模块被非蓝填满、整圈主边框改成非蓝、长主流程改成非蓝：颜色 QA 给 **`REJECT`**。
- 点缀不得染进正文、公式、注释或整个模块骨架。

### 5. Differential Verification（差分核验）

每次编辑后按语义区域记录：打算改什么、应该保住什么、实际改了什么、未授权改动、结论。

要回答的是：**不该变的地方变了什么？** 不是只问「要求的那一处看起来改了没有」。

### 6. Deterministic Escalation（确定性升级）

局部编辑允许：第一次局部修改，外加最多两次局部生成式返修。仍不稳（尤其是公式变形）就升级到 `deterministic-render`，不要第三次整图重抽。

复杂时序只有在参与者 ≤ 6、消息 ≤ 8、且没有「并行 + 循环/alt」缠在一起时，才允许纯图像模式。否则用确定性骨架，禁止让图像模型重画消息几何；做不到就拆图、简化，或返回 `BLOCKED`。

---

## 一键复制话术模板（直接喂给 Cursor / Claude Code / Cloud Agent）

### 场景 A：从零新建架构图 / 机制图 / 时序图（`create-new`）

```text
请严格加载并遵循 `drawing-skill`（SKILL.md，别名 `aicareer-diagram-style`）的 create-new 流程。
我要新建一张技术图：【在这里写单一问题，例如：画本系统容器级架构，标出三个服务和它们之间已经写进契约的调用】

视觉预设：
- 默认 visual_preset = aicareer-blueprint，参考 assets/reference-blueprint.png，只学视觉语言，不复制它的拓扑和版式。
- 若本项目另有视觉预设，在这里声明；未声明则用默认预设。换预设不得放宽下面的门禁。

硬门禁：
1. 先读 references/task-mode-router.md、references/diagram-routing.md、references/generation-gates.md。
2. 先做 Source Completeness Gate。映射、评测对比、分支去向、时序端点没有证据时返回 BLOCKED，禁止编造。Ready to Generate = NO 时停止，不要出图。
3. 用 templates/diagram-content-spec.yaml、templates/framework-mapping.yaml、templates/family-preflight.yaml、templates/relation-ledger.yaml 写清目的、框架、关系和锁定原文。
4. 默认 output_context = word-embedded-figure，caption_external = true，title_mode = compact，chrome_profile = standard。约 160 mm 宽的 Word 插图不要外圈整框，不要四角大十字准星，不要装饰页脚，不要在图内再放一条与外部图注重复的完整标题。
5. 非蓝点缀约 5–8%，不超过约 10%。禁止整卡非蓝填充。
6. 框架只在真正贴合时使用 C4 / DSRM / CRISP-DM；局部流程用 none，不要硬套六框。
```

### 场景 B：基于已有图片做局部受限修改（`edit-existing`，锁死无关区域防回归）

```text
请严格加载并遵循 `drawing-skill`（SKILL.md）的 edit-existing 流程。
原图：【在这里给出已经存在的图片 / SVG / 绘图文件路径】
只改这一处：【在这里写局部修改，例如：把模块标题「检索服务」改成「召回服务」，其他一律不动】

硬门禁：
1. 任务模式保持 edit-existing。禁止悄悄改成 create-new，禁止整图重生成。原图缺失或打不开时返回 BLOCKED，向我要原件。
2. 先建立不可变基线：没被点名的正文、中文字形、数字单位、公式、拓扑、分组、层级、有意换行、无关配色和布局全部锁死。
3. 必须落盘四份记录，而不是只回一张新图：
   - templates/edit-contract.yaml（Edit Contract）
   - templates/preservation-ledger.yaml（Preservation Ledger）
   - templates/canonical-content-lock.yaml（Canonical Content Lock）
   - templates/differential-verification.yaml（Differential Verification）
4. 编辑手段按这个顺序：原矢量/对象级修改 → 确定性文字或公式叠层 → 蒙版局部修改 → 有界局部重绘。整图重生成必须我明确同意。
5. 差分核验要回答「不该变的地方变了什么」。出现新缺陷时只修那一处，并再跑一次差分核验。局部生成式返修最多两次，仍不稳就升级 deterministic-render。
6. 无关文字、图标、边框、公式、连线和模块必须与原图一致。
```

### 场景 C：复杂公式 / 密集拓扑升级为确定性渲染（`deterministic-render`）

```text
请严格加载并遵循 `drawing-skill`（SKILL.md）的 deterministic-render 流程。
对象：【在这里说明公式、密集中文标签或复杂时序/拓扑；若已有图，给出路径】
失败背景：【例如：公式上下标已经变形，或局部生成式返修已用满两次仍不稳定】

硬门禁：
1. 读 references/deterministic-escalation.md、references/formula-integrity.md、references/generation-gates.md 的时序可靠性一节。
2. 不要再做第三次生成式重画，也不要用整图重抽掩盖模型限制。
3. 交付确定性载体，并说明选它的原因。优先顺序：原矢量/文档对象编辑、SVG、HTML+CSS、Mermaid 或其他 diagrams-as-code、Draw.io、Figma/PowerPoint/WPS 对象、确定性叠层。
4. 公式按结构化数据核对：变量、上下标、系数、运算符、括号、函数嵌套、参数顺序。看起来像不算通过。
5. 时序图若参与者 > 6、消息 > 8，或同时有并行和循环/alt，禁止纯图像模式重画消息几何；做不到确定性骨架就拆图、简化，或返回 BLOCKED。
6. 视觉仍服从当前 visual_preset（默认 aicareer-blueprint）：蓝族结构主导，非蓝约 5–8%。确定性渲染同样接受颜色 QA 和 Word 160 mm 版式 QA（无外圈整框、无重复标题）。
7. 若这是从 edit-existing 升级而来，已锁内容继续有效；升级本身如果会改变交付形式（例如从 PNG 改为 SVG），先向我说明再替换交付物。
```

---

## 目录结构（Repository Layout）

```text
drawing-skill/
├── SKILL.md                                      # 技能入口：模式路由、预设、门禁、保真与升级
├── README.md                                     # 本说明与一键复制话术
├── CHANGELOG.md                                  # 版本记录（当前 v0.8.0）
├── assets/
│   └── reference-blueprint.png                   # 默认预设 aicareer-blueprint 的参考图
├── references/
│   ├── diagram-routing.md                        # 图类型、家族门禁、框架例子、C4/DSRM/CRISP-DM
│   ├── generation-gates.md                       # 源事实、语义审查、构图、输出语境、参考图、时序可靠性
│   ├── task-mode-router.md                       # create-new / edit-existing / reconstruct-approved / deterministic-render
│   ├── fidelity-preservation-policy.md           # 编辑保真策略
│   ├── canonical-content-lock.md                 # 原文、中文、公式、换行锁定
│   ├── formula-integrity.md                      # 公式结构化核验
│   ├── topology-preservation.md                  # 拓扑保留 + 关系账本
│   ├── differential-verification.md              # 差分核验
│   ├── high-risk-elements.md                     # 高风险元素
│   ├── deterministic-escalation.md               # 确定性升级
│   ├── visual-baseline.md                        # 默认预设色板与几何感觉
│   ├── semantic-color-policy.md                  # 语义角色配色 + 分类示例
│   ├── blue-structure-accent-policy.md           # 蓝结构主导与稀疏点缀
│   ├── color-consistency-qa.md                   # 颜色一致性 QA
│   ├── visual-context-closure.md                 # 有界点缀闭合
│   ├── visual-semantic-qa.md                     # 视觉语义 QA
│   ├── qa-checklist.md                           # 成图检查单
│   ├── batch-evaluation.md                       # 多图批评估
│   ├── content-spec.md                           # 内容规格说明
│   ├── prompt-skeleton.md                        # 新建图提示骨架
│   ├── edit-prompt-skeleton.md                   # 受限编辑提示骨架
│   └── feedback-template.md                      # 返修反馈模板
├── templates/
│   ├── diagram-content-spec.yaml                 # 新建图内容规格
│   ├── framework-mapping.yaml                    # 框架映射
│   ├── family-preflight.yaml                     # 家族预检
│   ├── relation-ledger.yaml                      # 关系与端点账本
│   ├── edit-contract.yaml                        # 编辑契约
│   ├── preservation-ledger.yaml                  # 保留账本
│   ├── canonical-content-lock.yaml               # 正文/公式锁定
│   ├── differential-verification.yaml            # 差分核验记录
│   ├── color-role-ledger.yaml                    # 颜色角色账本
│   └── accent-context-ledger.yaml                # 点缀语境账本
└── tests/
    ├── README.md                                 # 如何运行静态校验
    ├── validate_structure.py                     # 前置、引用、YAML 与版本一致性
    └── regression-cases.yaml                     # 路由与治理回归用例
```

v0.8.0 把原先只有几百字节的路由、门禁、专家笔记和关系账本并进上面的 `diagram-routing.md`、`generation-gates.md`、`topology-preservation.md` 与 `semantic-color-policy.md`。规则没有删，只是不再拆成十几次跳转。

---

## 一键校验（Verification Commands）

在仓库根目录执行：

```bash
python3 tests/validate_structure.py
```

脚本会检查 `SKILL.md` 前置与体积、`SKILL.md` / `README.md` 里引用的 `references/`、`templates/`、`assets/` 路径是否真实存在、模板 YAML 与 `tests/regression-cases.yaml` 能否解析并带有必需字段，以及 `SKILL.md`、`README.md`、`CHANGELOG.md` 的当前版本是否都是 `v0.8.0`。
