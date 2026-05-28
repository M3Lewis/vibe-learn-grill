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
