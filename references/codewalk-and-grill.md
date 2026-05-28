# Codewalk and Grill Reference

Use this when the user asks to understand files, modules, functions, classes, components, APIs, or code generated during vibe coding.

> **Also used in Concept mode**: The question patterns here apply equally to pure concept grilling. When no code file is involved, simply ask about the concept itself (e.g., “What would happen if you removed `key` from a React list?”).

## When to codewalk

Codewalk after a meaningful unit is created or changed:

- a file with real behavior
- a public function/class/component
- an API route or service module
- a data model or schema
- a test that defines behavior
- a bug fix whose cause teaches something

Avoid codewalking every small helper unless the user asks.

## Codewalk format

```md
## Codewalk: <file or module>

Purpose:
What problem does this file/module solve?

Key pieces:
- <function/class/component>: what it owns
- <function/class/component>: what it delegates

Data flow:
Where does data come from, how is it transformed, where does it go?

Design reason:
Why is it shaped this way instead of the obvious alternative?

Common confusion:
What would a learner likely misunderstand here?

Grill:
Ask one question that checks understanding.
```

## Good grill question patterns

Prefer:

- Why is this responsibility placed here instead of in `<other file>`?
- What would break if we removed `<dependency>`?
- Where would a bug appear if `<input>` is missing or malformed?
- If the requirement changed to `<variation>`, which function/module changes first?
- Explain the data flow from `<entry point>` to `<output>`.

Avoid unless useful:

- Pure definition questions.
- Questions whose answer is a literal line of code.
- Multiple questions at once.

## Answer handling

Classify the user's answer silently as:

- `understood`: answer is correct and causal.
- `shaky`: partly correct but vague, memorized, or missing edge cases.
- `wrong`: incorrect model, wrong data flow, or wrong ownership.

For `shaky` or `wrong`:

1. Correct briefly.
2. Ask one smaller follow-up or transfer question.
3. Add/update a `LEARN-GRILL.md` card if the issue is worth revisiting.

## Migration prompts (fourth layer)

When you identify a design pattern, architectural principle, or constraint that is **not unique** to the current project, you may optionally add a migration prompt after the grill question. Do not force this every time; use it when the pattern is particularly transferable.

**How to prompt**:

1. Briefly point out the pattern: “这个‘X 不直接控制 Y’的模式，其实不只在当前项目中出现。”
2. Give one short analogy from another domain (e.g., frontend state management, hardware design, game development, or even non-programming fields).
3. Ask a simple open-ended question: “你还在哪个别的场景里见过类似的结构？哪怕不是编程领域也行。”

**Example** (after explaining that UI triggers actions but doesn’t know protocol details):

> 这个“UI 发出意图，底层模块负责执行”的模式，在 Redux 里叫做 action + reducer，在硬件里可能是一个按钮控制继电器。
>
> 你能想到另一个你熟悉的系统也用了同样的分离吗？想不起来也没关系，可以跳过。

**Important**:

- Do not interrupt the core learning loop. If the user seems tired or wants to move on, skip the migration prompt.
- Do not demand a correct answer. The goal is to plant the seed for transfer, not to test it.
