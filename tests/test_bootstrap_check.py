import tempfile
import unittest
from pathlib import Path

from scripts.bootstrap_check import validate


VALID_CONTEXT = """# Project Context

## Identity
- **Project:** Demo
- **Purpose:** Demonstrate bootstrap validation
- **Primary users/stakeholders:** Engineering team
- **Repository:** owner/demo
- **Default/base branch:** main

## Scope
- In scope: demo capability
- Out of scope: unrelated capability

## Architecture
- **Architecture style:** modular monolith

## Bounded contexts / modules
- demo

## Authoritative sources
1. roadmap

## Critical invariants
- preserve compatibility

## Quality gates
- **Unit tests:** python -m unittest discover -s tests

## CI model
Local validation is authoritative.

## AI-assisted workflow
- Coding agent: any
- Merge authority: human

## Confidentiality and publication constraints
- no secrets

## Current roadmap
- Active roadmap: `doc/roadmaps/demo.md`
- Current phase/item: PR-1
- Last completed bounded PR: none — new project
"""


class BootstrapCheckTests(unittest.TestCase):
    def make_repo(self, context: str = VALID_CONTEXT) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        root = Path(temp_dir.name)
        (root / "PROJECT_CONTEXT.md").write_text(context, encoding="utf-8")
        (root / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
        (root / "doc" / "roadmaps").mkdir(parents=True)
        (root / "doc" / "roadmaps" / "demo.md").write_text("# Roadmap\n", encoding="utf-8")
        return root

    def test_ready_context_passes(self):
        self.assertEqual([], validate(self.make_repo()))

    def test_template_placeholders_block_readiness(self):
        root = self.make_repo(VALID_CONTEXT.replace("owner/demo", "<owner/repository>"))
        errors = validate(root)
        self.assertTrue(any("placeholder" in error.lower() for error in errors))

    def test_explicit_blocker_blocks_readiness(self):
        root = self.make_repo(VALID_CONTEXT + "\nTBD — BLOCKER: choose security model\n")
        errors = validate(root)
        self.assertTrue(any("blocker" in error.lower() for error in errors))

    def test_missing_roadmap_blocks_readiness(self):
        root = self.make_repo()
        (root / "doc" / "roadmaps" / "demo.md").unlink()
        errors = validate(root)
        self.assertTrue(any("roadmap does not exist" in error.lower() for error in errors))

    def test_missing_required_section_blocks_readiness(self):
        context = VALID_CONTEXT.replace("## Critical invariants\n- preserve compatibility\n\n", "")
        errors = validate(self.make_repo(context))
        self.assertTrue(any("Critical invariants" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
