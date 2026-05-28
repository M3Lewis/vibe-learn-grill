#!/usr/bin/env python3
"""Create VIBE-PLAN.md and/or LEARN-GRILL.md from bundled templates.

This helper is intentionally small. It never overwrites existing files unless
--force is provided.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
TARGETS = {
    "plan": (TEMPLATES / "VIBE-PLAN.template.md", "VIBE-PLAN.md"),
    "cards": (TEMPLATES / "LEARN-GRILL.template.md", "LEARN-GRILL.md"),
}


def write_from_template(kind: str, force: bool) -> str:
    src, target_name = TARGETS[kind]
    dst = Path.cwd() / target_name
    if dst.exists() and not force:
        return f"skip: {target_name} already exists"
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return f"wrote: {target_name}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="create both files")
    parser.add_argument("--plan", action="store_true", help="create VIBE-PLAN.md")
    parser.add_argument("--cards", action="store_true", help="create LEARN-GRILL.md")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    args = parser.parse_args()

    selected = []
    if args.all or args.plan:
        selected.append("plan")
    if args.all or args.cards:
        selected.append("cards")
    if not selected:
        parser.error("choose --all, --plan, or --cards")

    for kind in selected:
        print(write_from_template(kind, args.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
