# Adoption Checklist

Run this after project context is complete and before generating the first implementation prompt.

## Repository adoption

- [ ] Template-specific sample values have been removed from active project documents.
- [ ] `PROJECT_CONTEXT.md` passes `project-context-checklist.md`.
- [ ] Root `AGENTS.md` rules are compatible with the project.
- [ ] Local `AGENTS.md` files exist only where a real ownership or architectural boundary needs additional rules.
- [ ] Architecture principles are applicable; project-specific exceptions are documented.
- [ ] Required ADRs exist for consequential decisions already made.

## Roadmap readiness

- [ ] One active project roadmap exists.
- [ ] Roadmap items express outcomes and dependencies.
- [ ] The first candidate item has satisfied predecessors.
- [ ] The first candidate can be delivered as one reviewable bounded PR.
- [ ] Non-goals for the first candidate are identifiable.

## Engineering readiness

- [ ] The repository can be built/tested locally to the extent required by `PROJECT_CONTEXT.md`.
- [ ] Mandatory validation commands are executable or an explicit bootstrap PR exists to establish them.
- [ ] Baseline failures, if any, are recorded rather than silently treated as failures introduced by future PRs.
- [ ] Secrets, credentials, proprietary material, and sensitive examples are absent from the public/template-derived repository.

## First-PR gate

Before running `doc/prompts/bootstrap-first-pr.md`, answer yes to all four:

1. Can an assistant identify the authoritative sources without asking the user to restate them? **Yes / No**
2. Can it determine the first item's architecture boundaries and invariants? **Yes / No**
3. Can it tell exactly what evidence is required to accept the PR? **Yes / No**
4. Can it distinguish an architecture decision from an implementation detail? **Yes / No**

Any **No** is a bootstrap blocker. Resolve the missing context before asking an implementation agent to write code.