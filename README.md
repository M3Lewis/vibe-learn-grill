# vibe-learn-grill

[English](README.md) | [中文](README.zh-CN.md)

A lightweight Codex/Claude skill for learning technical topics by building a small project, then keeping understanding alive through codewalks, one-question grills, and review cards.

It avoids a heavy coaching system. The workflow centers on two durable project files:

- `VIBE-PLAN.md` — project plan and web-to-IDE handoff.
- `LEARN-GRILL.md` — weak concepts, mistakes, review prompts, and an optional module-card index.

## What it does

- Turns a learning goal into a small, buildable vibe-coding project.
- Guides implementation in small modules instead of a large course-like sequence.
- Explains code by module boundaries: purpose, key pieces, data flow, design reasons, and likely confusion points.
- Asks one grill question at a time, focused on transfer, debugging, and prediction.
- Maintains lightweight review cards in Chinese for concepts the learner actually missed or half-understood.
- Offers a module-card index when review cards accumulate, so weak spots can be seen by module.

## Core learning layers

This skill treats learning as four layers. The first three are the core loop; the fourth is optional guidance for transfer.

| Layer | Meaning | Current rating | Key mechanism | Comment |
|---|---|---|---|---|
| Layer 1: Know | Hear about the concept | Good | Concept-mode questions + project-mode initial grill | Directly hits the target: the user must acknowledge whether they have encountered the concept. |
| Layer 2: Understand | Know why it exists | Good+ | Design-oriented grill questions (“why here?”, “why this design?”) + design reasoning in codewalks | Effectively tests causal understanding, but depends on the quality of the AI's questions. |
| Layer 3: Apply | Make correct decisions inside the project | Good+ and still improving | Code-free restatement + hypothetical change questions (“requirement becomes Y; which file changes?”) | The user must organize the implementation logic themselves instead of passively repeating the AI. This is the key bridge from understanding to application. |
| Layer 4: Transfer | Recognize the same pattern in other domains | Medium to good | Optional migration prompts in `references/codewalk-and-grill.md` | Plants transfer awareness with light practice, but does not persist or test it. It upgrades the skill from “missing step” to “guided transfer.” |

## Operating modes

- **Plan Mode**: convert a learning goal into a practical `VIBE-PLAN.md`.
- **Build Mode**: continue from `VIBE-PLAN.md`, implement one small module or file group, then pause for codewalk.
- **Codewalk Mode**: explain the current module without going line by line unless asked.
- **Review Mode**: use `LEARN-GRILL.md` to ask 3-5 due or weak review questions before new work.

## Install

Copy this folder to your Codex or Claude skills directory.

For Claude-style project skills:

```bash
mkdir -p .claude/skills
cp -R vibe-learn-grill .claude/skills/
```

For Codex skills, place it under your Codex skills directory, for example:

```bash
mkdir -p ~/.codex/skills
cp -R vibe-learn-grill ~/.codex/skills/
```

Optionally add the snippet in `references/claude-registry-snippet.md` to your project `CLAUDE.md` when using Claude Code.

## Optional project init

From your project root:

```bash
python .claude/skills/vibe-learn-grill/scripts/init_learning_files.py --all
```

This creates `VIBE-PLAN.md` and `LEARN-GRILL.md` from templates, without overwriting existing files unless `--force` is passed.

## Review cards and module index

`LEARN-GRILL.md` is intentionally small. Cards should be created only when the learner gets something wrong, gives a shaky answer, confuses concepts, misses data flow, or cannot transfer an idea to a nearby change.

When the file reaches roughly 8-10 cards, or when the user asks, the skill can offer to generate/update a `模块-卡片索引` block at the top of `LEARN-GRILL.md`. The index groups cards by file/module and leaves room for simple arrows or indentation to show module relationships.

## Typical use

1. In web ChatGPT/Claude: “I want to learn X. Turn it into a small vibe coding project and output `VIBE-PLAN.md`.”
2. Put `VIBE-PLAN.md` in the project root.
3. In Claude Code/Cursor: “Continue from `VIBE-PLAN.md`. Build module 1, then codewalk and grill me.”
4. Keep `LEARN-GRILL.md` in the repo for review across sessions.

## Files

- `SKILL.md` — skill trigger, modes, rules, and gotchas.
- `templates/VIBE-PLAN.template.md` — project handoff template.
- `templates/LEARN-GRILL.template.md` — review-card template with optional module-card index.
- `references/codewalk-and-grill.md` — codewalk and question patterns.
- `references/review-cards.md` — review card scheduling and module-card index maintenance rules.
- `scripts/init_learning_files.py` — helper for initializing learning files in a project.
