# Bootstrap Documentation

Use this directory together with the root [`BOOTSTRAP.md`](../../BOOTSTRAP.md).

Recommended order:

1. [`quickstart.md`](quickstart.md) — shortest path for a new user.
2. [`project-context-checklist.md`](project-context-checklist.md) — verify that `PROJECT_CONTEXT.md` contains enough authoritative project truth.
3. Run `python scripts/bootstrap_check.py` — fail fast on mechanical adoption errors.
4. [`validator.md`](validator.md) — understand what the automated gate does and intentionally does not decide.
5. [`adoption-checklist.md`](adoption-checklist.md) — perform qualitative architecture, roadmap, and engineering readiness checks.
6. [`decision-table.md`](decision-table.md) — resolve common bootstrap ambiguities consistently.
7. Run [`../prompts/bootstrap-first-pr.md`](../prompts/bootstrap-first-pr.md) — select exactly one first admissible bounded PR or stop with a bootstrap blocker.

The machine validator and the human/reviewer checklists are complementary: automation detects structural mistakes; reviewers retain responsibility for architecture quality and decomposition.