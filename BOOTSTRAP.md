# Bootstrap a New Project

This is the shortest path from cloning the template to a first implementation-ready bounded PR.

Do **not** read the repository front to back. Complete the gates below in order and open deeper documentation only when a gate points to it.

## Target outcome

Bootstrap is complete when the repository has:

- a project-specific `PROJECT_CONTEXT.md` with no unresolved required placeholders;
- explicit scope, architecture boundaries, invariants, and validation commands;
- one active roadmap with a clearly identified first admissible item;
- exactly one PR-specific implementation prompt for that item;
- a bounded PR whose acceptance criteria and validation evidence are reviewable.

## Gate 0 — Clone and create a bootstrap branch

```bash
git clone <your-repository-url>
cd <repository>
git switch -c chore/bootstrap-project
```

Do not start product implementation on this branch.

## Gate 1 — Fill the minimum project contract

Open `PROJECT_CONTEXT.md` and replace the placeholders in these sections first:

1. Identity
2. Scope — both in-scope and explicit non-goals
3. Architecture
4. Bounded contexts / modules
5. Authoritative sources
6. Critical invariants
7. Quality gates
8. CI model
9. AI-assisted workflow
10. Confidentiality/publication constraints
11. Current roadmap

If a required fact is unknown, write `TBD — BLOCKER: <decision needed>` rather than inventing it. A blocker affecting scope, architecture, security, data compatibility, or acceptance prevents implementation PR generation.

Use `doc/bootstrap/project-context-checklist.md` as the human-readable completion gate.

## Gate 2 — Adopt repository governance

Read only:

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `doc/architecture/principles.md`
- `doc/standards/code-quality.md`
- `doc/standards/testing.md`
- `doc/standards/prompt-design.md`

Then decide whether the project has bounded contexts/modules needing local instructions. For each material boundary, copy `templates/bounded-context-AGENTS.template.md` into that area as `AGENTS.md` and customize it.

Do not create local `AGENTS.md` files merely to duplicate root rules.

## Gate 3 — Establish the first roadmap

Copy `doc/roadmaps/roadmap-template.md` to a project-specific roadmap, for example:

`doc/roadmaps/<project>-roadmap.md`

Describe outcomes and dependency order, not a large implementation dump. Each roadmap item must be independently reviewable and small enough to become one bounded PR.

Update `PROJECT_CONTEXT.md` so **Current roadmap** points to this file and identifies the current phase/item.

## Gate 4 — Run automated and human adoption checks

Run the stdlib-only validator from the repository root:

```bash
python scripts/bootstrap_check.py
```

On systems where the interpreter is exposed as `python3`:

```bash
python3 scripts/bootstrap_check.py
```

The command exits with code `0` and prints `BOOTSTRAP CHECK: READY` only when the minimum machine-checkable contract is satisfied. It checks required `PROJECT_CONTEXT.md` sections, unresolved template placeholders/blockers, root `AGENTS.md`, and the active roadmap path.

Then complete `doc/bootstrap/adoption-checklist.md` for qualitative checks the script cannot safely infer, such as whether architecture boundaries are meaningful and roadmap decomposition is reviewable.

Stop if either check is blocked. Resolve architecture decisions explicitly; use an ADR when the decision is consequential, durable, or constrains future work.

## Gate 5 — Generate exactly one first bounded PR

Use `doc/prompts/bootstrap-first-pr.md`.

The assistant must inspect repository state and authoritative context, choose exactly one admissible roadmap item, and either:

- create one PR-specific prompt under `doc/codex-prompts/<roadmap-or-task>/`; or
- stop with an architecture/bootstrap blocker.

It must not implement the product change during this step.

## Gate 6 — Implement

Give the generated PR-specific prompt to the coding agent. The agent must follow root and applicable local `AGENTS.md`, remain inside the bounded scope, run the required local validation, and record exact results.

Do not silently widen scope to fix unrelated defects. Record pre-existing failures separately.

## Gate 7 — Independent review

Use `doc/prompts/pr-review.md` with a reasoning-capable reviewer that did not author the implementation where practical.

A PR is ready only when mandatory blockers are absent and the required validation evidence is present. Hosted CI is not assumed unless `PROJECT_CONTEXT.md` makes it mandatory.

## Bootstrap completion checklist

- [ ] `PROJECT_CONTEXT.md` is project-specific and passes its checklist.
- [ ] `python scripts/bootstrap_check.py` reports `BOOTSTRAP CHECK: READY`.
- [ ] Root governance is understood and local ownership rules exist where necessary.
- [ ] One active roadmap exists and is referenced from project context.
- [ ] Architecture blockers required for the first item are resolved.
- [ ] Exactly one first PR-specific implementation prompt exists.
- [ ] The first bounded implementation PR has explicit scope, non-goals, acceptance criteria, and validation.
- [ ] Independent review can determine `APPROVE` or `REQUEST CHANGES` from repository evidence.

After this point, use the normal loop in `doc/workflow.md`: next bounded PR → implementation → review → remediation if required → merge → roadmap update.