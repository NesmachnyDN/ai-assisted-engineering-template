# Project Context Readiness Checklist

Use this checklist immediately after filling `PROJECT_CONTEXT.md`. The goal is not exhaustive documentation; it is enough authoritative context for an AI agent to make bounded, reviewable changes without guessing material project facts.

## Blocking checks

All items below must pass before generating an implementation PR.

### Identity and scope

- [ ] Project purpose is specific enough to distinguish desired outcomes from implementation mechanisms.
- [ ] Primary users/stakeholders are identified.
- [ ] Repository and base branch are correct.
- [ ] At least one in-scope capability is stated.
- [ ] At least one explicit non-goal prevents obvious scope drift.

### Architecture boundary

- [ ] Architecture style is stated.
- [ ] Primary language/runtime is stated.
- [ ] Material frameworks, persistence, messaging/integration, deployment, and security choices are stated or explicitly marked not applicable.
- [ ] Material bounded contexts/modules and their responsibilities are identified.
- [ ] Ownership or authoritative documentation is named for each material boundary.

### Authority and invariants

- [ ] Authoritative sources are listed in precedence order.
- [ ] Conflicts between sources have a deterministic resolution rule.
- [ ] Critical compatibility/data/security invariants are explicit.
- [ ] No invariant required for the first roadmap item remains an unresolved `TBD — BLOCKER`.

### Validation

- [ ] Local formatting/lint command is known or marked not applicable with reason.
- [ ] Local unit-test command is known or marked not applicable with reason.
- [ ] Other mandatory checks are explicit.
- [ ] CI model states whether hosted CI, local evidence, or both are authoritative.
- [ ] A reviewer can tell which failed checks block merge and which may be pre-existing baseline failures.

### AI and publication controls

- [ ] Human architecture/decision owner is identified by role.
- [ ] Merge authority remains explicit.
- [ ] Confidentiality/publication constraints state what must never enter prompts, commits, logs, screenshots, or public artifacts.

### Roadmap

- [ ] Exactly one active roadmap is referenced.
- [ ] Current phase/item is stated.
- [ ] Last completed bounded PR is stated or explicitly `none — new project`.

## Placeholder check

Search for unresolved template markers:

```bash
grep -R "<[^>][^>]*>" PROJECT_CONTEXT.md
```

Review every result. Required placeholders must be replaced. Literal angle-bracket syntax that belongs to the project may remain only when clearly intentional.

Also search for blockers:

```bash
grep -n "TBD — BLOCKER" PROJECT_CONTEXT.md
```

Any blocker affecting the proposed first PR must be resolved before implementation prompt generation.

## Exit criterion

The context is ready when every blocking check passes and an independent reviewer could determine the first PR's scope, governing constraints, and required validation without inventing project facts.