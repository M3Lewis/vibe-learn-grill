# vibe-learn-grill

[English](README.md) | [中文](README.zh-CN.md)

一个轻量级 Codex/Claude Skill：通过做一个小项目来学习技术主题，并用代码讲解、单题追问和复习卡片把理解留下来。

它不做沉重的教学系统。核心只围绕两个项目文件：

- `VIBE-PLAN.md`：项目计划，以及从网页规划到 IDE 编码的交接文件。
- `LEARN-GRILL.md`：薄弱概念、错误记录、复习提示、活跃/已掌握卡片分区，以及可选的模块-卡片索引。

## 它做什么

- 把学习目标转成一个小而可构建的 vibe-coding 项目。
- 按小模块推进实现，而不是做课程式的大流程。
- 按模块边界讲代码：用途、关键部分、数据流、设计原因和常见混淆点。
- 一次只问一个追问题，重点考迁移、调试和预测能力。
- 用中文维护轻量复习卡片，只记录真正答错、半懂或无法迁移的概念。
- 用 `Active Cards` / `Mastered Cards` 分区控制默认读取范围，普通复习优先读活跃卡片，默认跳过已掌握卡片正文。
- 当卡片积累起来时，提供模块-卡片索引，帮助你看到薄弱点集中在哪些模块。

## 核心学习层次

这个 skill 把学习拆成四层。前三层是核心循环，第四层是可选的迁移引导。

| 层次 | 含义 | 当前评级 | 关键机制 | 评价 |
|---|---|---|---|---|
| 第一层：知道 | 听过概念 | 优 | 概念模式拷问 + 项目模式初始 grill | 直接命中，用户必须承认是否接触过该概念。 |
| 第二层：理解 | 知道为什么存在 | 良+ | 设计类 grill 问题（“为什么放这里？”“为什么这样设计？”）+ codewalk 中的设计原理解释 | 能有效测试“知道原因”，但依赖 AI 问题质量。 |
| 第三层：应用 | 能在项目中做正确决策 | 良+（仍在优化中） | 无代码复述 + 假设性改动问题（“需求变 Y，改哪个文件？”） | 用户必须自己组织实现逻辑并表达决策，不只是复述 AI 讲过的内容。这是从“理解”到“应用”的关键跃迁。 |
| 第四层：迁移 | 在其他领域识别相同模式 | 中~良 | `references/codewalk-and-grill.md` 中新增的可选迁移提示 | 种下了意识和轻量练习，但不持久化、不考核。从“缺失”升级为“有引导”。 |

## 工作模式

- **Plan Mode**：把学习目标转成可执行的 `VIBE-PLAN.md`。
- **Build Mode**：从 `VIBE-PLAN.md` 继续，构建一个小模块或一组文件，然后暂停做 codewalk。
- **Codewalk Mode**：解释当前模块，不默认逐行讲解。
- **Review Mode**：读取 `LEARN-GRILL.md`，在新工作前复习 3-5 张到期或薄弱卡片。

## 安装

把本目录复制到 Codex 或 Claude 的 skills 目录。

Claude 风格的项目 skills：

```bash
mkdir -p .claude/skills
cp -R vibe-learn-grill .claude/skills/
```

Codex skills 示例：

```bash
mkdir -p ~/.codex/skills
cp -R vibe-learn-grill ~/.codex/skills/
```

如果使用 Claude Code，也可以把 `references/claude-registry-snippet.md` 中的片段加入项目的 `CLAUDE.md`。

## 可选：初始化项目学习文件

在你的项目根目录运行：

```bash
python .claude/skills/vibe-learn-grill/scripts/init_learning_files.py --all
```

这会根据模板创建 `VIBE-PLAN.md` 和 `LEARN-GRILL.md`。默认不会覆盖已有文件，除非传入 `--force`。

## 复习卡片、活跃分区和模块索引

`LEARN-GRILL.md` 应保持小巧。只有当学习者答错、回答不稳、混淆概念、讲不清数据流，或无法把思路迁移到相近改动时，才应该创建或更新卡片。

卡片仍然只放在一个文件里，但按复习活跃度分成两个主区：

- `Active Cards`：存放 `weak`、`shaky`、`stable` 卡片。
- `Mastered Cards`：只存放 `mastered` 卡片。

普通复习从 `Active Cards` 开始。`Mastered Cards` 默认只扫描标题和元数据；只有用户点名、随机抽查选中，或做全局整理/索引任务时，才读取已掌握卡片正文。卡片 ID 永不重编号。跨区移动在会话结束时批量处理，并追加到目标区末尾。

当卡片达到约 8-10 张，或用户主动要求时，skill 可以询问是否生成/更新 `LEARN-GRILL.md` 顶部的 `模块-卡片索引`。这个索引按文件或模块归类卡片，并允许用简单箭头或缩进表示模块关系。

## 典型用法

1. 在网页端 ChatGPT/Claude 中说：“我想学 X，把它变成一个小型 vibe coding 项目，并输出 `VIBE-PLAN.md`。”
2. 把 `VIBE-PLAN.md` 放到项目根目录。
3. 在 Claude Code/Cursor 中说：“从 `VIBE-PLAN.md` 继续。先构建模块 1，然后 codewalk 并 grill me。”
4. 把 `LEARN-GRILL.md` 留在仓库里，跨会话复习。

## 文件结构

- `SKILL.md`：skill 触发说明、工作模式、规则和注意事项。
- `templates/VIBE-PLAN.template.md`：项目交接模板。
- `templates/LEARN-GRILL.template.md`：复习卡片模板，包含可选模块-卡片索引。
- `references/codewalk-and-grill.md`：代码讲解格式和追问模式。
- `references/review-cards.md`：复习卡片调度和模块-卡片索引维护规则。
- `scripts/init_learning_files.py`：在项目中初始化学习文件的辅助脚本。
