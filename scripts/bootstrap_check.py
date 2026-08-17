#!/usr/bin/env python3
"""Validate readiness to generate the first bounded implementation PR."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = (
    "Identity",
    "Scope",
    "Architecture",
    "Bounded contexts / modules",
    "Authoritative sources",
    "Critical invariants",
    "Quality gates",
    "CI model",
    "AI-assisted workflow",
    "Confidentiality and publication constraints",
    "Current roadmap",
)

REQUIRED_IDENTITY_FIELDS = (
    "Project",
    "Purpose",
    "Primary users/stakeholders",
    "Repository",
    "Default/base branch",
)

PLACEHOLDER_RE = re.compile(r"<[^>\n]+>")
BLOCKER_RE = re.compile(r"TBD\s*[—-]\s*BLOCKER", re.IGNORECASE)


def section_names(text: str) -> set[str]:
    return {
        match.group(1).strip()
        for match in re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    }


def find_field(text: str, field: str) -> str | None:
    pattern = re.compile(
        rf"^\s*-\s+\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$",
        flags=re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def roadmap_path(text: str) -> str | None:
    pattern = re.compile(
        r"^\s*-\s+Active roadmap:\s*`([^`]+)`\s*$",
        flags=re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    context = root / "PROJECT_CONTEXT.md"
    agents = root / "AGENTS.md"

    if not context.is_file():
        return ["PROJECT_CONTEXT.md is missing."]
    if not agents.is_file():
        errors.append("AGENTS.md is missing.")

    text = context.read_text(encoding="utf-8")

    sections = section_names(text)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            errors.append(f"PROJECT_CONTEXT.md is missing required section: {name}")

    for field in REQUIRED_IDENTITY_FIELDS:
        value = find_field(text, field)
        if value is None:
            errors.append(f"PROJECT_CONTEXT.md is missing required identity field: {field}")
        elif PLACEHOLDER_RE.search(value):
            errors.append(f"Identity field still contains a template placeholder: {field}")

    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
    if placeholders:
        sample = ", ".join(placeholders[:5])
        suffix = "" if len(placeholders) <= 5 else f" (+{len(placeholders)-5} more)"
        errors.append(f"Unresolved template placeholders remain: {sample}{suffix}")

    if BLOCKER_RE.search(text):
        errors.append("Unresolved 'TBD — BLOCKER' marker remains in PROJECT_CONTEXT.md.")

    active_roadmap = roadmap_path(text)
    if active_roadmap is None:
        errors.append("Current roadmap does not define an `Active roadmap` path.")
    elif not (root / active_roadmap).is_file():
        errors.append(f"Active roadmap does not exist: {active_roadmap}")

    if "Last completed bounded PR:" not in text:
        errors.append("Current roadmap does not state the last completed bounded PR.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate template bootstrap readiness.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory).",
    )
    args = parser.parse_args()

    errors = validate(args.root.resolve())
    if errors:
        print("BOOTSTRAP CHECK: BLOCKED")
        for item in errors:
            print(f"- {item}")
        return 1

    print("BOOTSTRAP CHECK: READY")
    print("- Required project-context sections are present.")
    print("- No unresolved template placeholders or blockers were found.")
    print("- Active roadmap exists.")
    print("- Root AGENTS.md exists.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
