# Code Quality Standard

Project-specific rules override this generic baseline when documented in `AGENTS.md`.

## Design

- Keep ownership and dependency direction explicit.
- Prefer cohesive modules with narrow public contracts.
- Reuse established abstractions before adding parallel implementations.
- Avoid speculative generalization.
- Apply SOLID/DRY to reduce meaningful coupling and duplication, not as mechanical goals.
- Treat error/failure semantics as part of the design.

## Change discipline

- Keep each PR bounded to one objective.
- Do not mix feature work with unrelated refactoring, formatting, or dependency upgrades.
- Inspect callers/consumers before changing contracts.
- Inspect symmetric paths when changing shared invariants.

## Maintainability

Define project limits here if useful:

- Maximum source file size: `<project rule or N/A>`
- Maximum function/method size: `<project rule or N/A>`
- Complexity threshold: `<project rule or N/A>`

Large files/functions are review signals, not automatic refactoring mandates when splitting would damage cohesion.

## Safety

- No secrets or production data in code, tests, fixtures, prompts, logs, or documentation.
- No swallowed exceptions or fallback behavior that hides corruption/invalid state.
- No disabling validation merely to make a test pass.
- Preserve backward compatibility unless the bounded change explicitly owns the migration/breaking change.