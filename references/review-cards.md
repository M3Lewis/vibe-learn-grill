
# 复习卡片参考

`LEARN-GRILL.md` 是唯一的持久化学习状态文件。它应该保持小巧且有用。

## 卡片创建条件

仅在用户出现以下情况时创建或更新卡片：

- 回答错误
- 答案模糊或凭记忆蒙对
- 混淆两个概念
- 无法解释数据流
- 无法预测边界情况
- 无法将想法迁移到相近的改动
- 遗漏项目中高频的核心概念

**不要**为每个事实都创建卡片。

## 卡片格式

```md
## CARD-001

Topic（主题）:
File（关联文件）:
Status（状态）: weak | shaky | stable | mastered
Strength（强度）: 1/5
Last reviewed（上次复习）:
Next review（下次复习）:

Question（问题）:

Ideal answer（理想答案）:

My mistake（我当时的错误/盲点）:

Review prompt（复习提示）:
```

> 注意：`Status` 字段建议使用英文 `weak/shaky/stable/mastered`，以便与调度规则中的表格对应。但你也可以在填写时使用中文“弱/不稳/稳定/掌握”，调度规则同样理解。

## 调度规则

使用简单的规则，而不是完整的间隔重复引擎：

| 结果 | 更新 |
|---|---|
| 回答错误 | `Status: weak`，`Strength: 1/5`，`Next review: next-session` |
| 回答不稳（半对半错） | `Status: shaky`，`Strength + 1`，`Next review: next-session` 或 tomorrow |
| 正确但较慢 | `Status: stable`，`Strength + 1`，`Next review: 3 days` |
| 正确且能举例/预测边界 | `Strength + 2`，`Next review: 7 days` |
| 连续两次答得又好又稳 | `Status: mastered`，之后只随机抽查 |

## 会话热身

每次编码/学习会话开始时：

1. 加载 `LEARN-GRILL.md`（若存在）。
2. 选择 3 张卡片，最多 5 张。
3. 优先选 `weak`、`shaky`、到期、以及当前模块相关的卡片。
4. 一次只问一张卡片的问题。
5. 用户回答后更新卡片状态（如果明确允许写入文件）。
6. 热身完成后继续构建/学习。

如果用户要求跳过复习，则跳过本次，但在会话结束前提示“还有 X 张弱卡片未复习”。

