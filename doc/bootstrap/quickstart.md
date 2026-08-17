# Five-Minute Bootstrap Quickstart

This page is for a new user who wants the shortest possible path to the first governed AI-assisted change.

## 1. Create the project

Use the repository as a GitHub template or clone it and remove the original remote.

## 2. Fill only the required project truth

Edit `PROJECT_CONTEXT.md`. Do not write essays. Record:

- project purpose and users;
- explicit in-scope and out-of-scope boundaries;
- runtime/architecture choices already decided;
- modules/bounded contexts and ownership;
- authoritative sources in precedence order;
- critical invariants;
- exact validation commands;
- CI/local-validation policy;
- confidentiality constraints;
- active roadmap.

Unknown material decisions should be written as `TBD — BLOCKER: ...`, not guessed.

## 3. Create the first roadmap

Copy:

```text
doc/roadmaps/roadmap-template.md
```

to a project-specific roadmap. Define the smallest useful sequence of bounded outcomes and their dependencies.

## 4. Run the readiness check

```bash
python scripts/bootstrap_check.py
```

Do not continue until the command prints:

```text
BOOTSTRAP CHECK: READY
```

Then complete `doc/bootstrap/adoption-checklist.md`.

## 5. Ask for exactly one first PR

Use `doc/prompts/bootstrap-first-pr.md` with a reasoning-capable assistant. It must return either:

- one PR-specific prompt under `doc/codex-prompts/`; or
- a bootstrap/architecture blocker.

Do not ask it to implement the entire roadmap.

## 6. Implement and review

Give the PR-specific prompt to the coding agent, record exact validation results, then use `doc/prompts/pr-review.md` for independent full-diff review.

That is enough to enter the normal recurring workflow. Read deeper documentation only when a concrete decision or review requires it.