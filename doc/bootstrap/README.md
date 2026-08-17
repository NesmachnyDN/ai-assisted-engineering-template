# Bootstrap Documentation

Use this directory together with the root [`BOOTSTRAP.md`](../../BOOTSTRAP.md).

Recommended order:

1. [`project-context-checklist.md`](project-context-checklist.md) — verify that `PROJECT_CONTEXT.md` contains enough authoritative project truth.
2. Run `python scripts/bootstrap_check.py` — fail fast on mechanical adoption errors.
3. [`validator.md`](validator.md) — understand what the automated gate does and intentionally does not decide.
4. [`adoption-checklist.md`](adoption-checklist.md) — perform qualitative architecture, roadmap, and engineering readiness checks.
5. Run [`../prompts/bootstrap-first-pr.md`](../prompts/bootstrap-first-pr.md) — select exactly one first admissible bounded PR or stop with a bootstrap blocker.

The machine validator and the human/reviewer checklists are complementary: automation detects structural mistakes; reviewers retain responsibility for architecture quality and decomposition.