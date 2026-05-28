# vibe-learn-grill

A lightweight Claude Skill for learning technical topics through vibe coding.

It replaces a heavy coaching system with two durable files:

- `VIBE-PLAN.md` — project plan and web-to-IDE handoff.
- `LEARN-GRILL.md` — weak concepts and review cards.

## Install

Copy this folder to your Claude skills directory, for example:

```bash
mkdir -p .claude/skills
cp -R vibe-learn-grill .claude/skills/
```

Optionally add the snippet in `references/claude-registry-snippet.md` to your project `CLAUDE.md`.

## Optional project init

From your project root:

```bash
python .claude/skills/vibe-learn-grill/scripts/init_learning_files.py --all
```

This creates `VIBE-PLAN.md` and `LEARN-GRILL.md` from templates, without overwriting existing files unless `--force` is passed.

## Typical use

1. In web ChatGPT/Claude: “I want to learn X. Turn it into a small vibe coding project and output `VIBE-PLAN.md`.”
2. Put `VIBE-PLAN.md` in the project root.
3. In Claude Code/Cursor: “Continue from `VIBE-PLAN.md`. Build module 1, then codewalk and grill me.”
4. Keep `LEARN-GRILL.md` in the repo for review across sessions.
