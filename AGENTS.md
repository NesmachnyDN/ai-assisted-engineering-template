# AGENTS.md

## Purpose

This file defines repository-wide operating rules for human contributors and AI coding agents. Replace project placeholders before production work begins.

## Instruction precedence

Apply instructions in this order:

1. Explicit task/PR acceptance criteria.
2. The nearest applicable local `AGENTS.md` for the files being changed.
3. This root `AGENTS.md`.
4. Architecture decisions and principles under `doc/architecture/`.
5. The active roadmap and PR-specific prompt.
6. General standards under `doc/standards/`.

If authoritative sources conflict materially, stop and report an architecture/governance blocker instead of guessing.

## Required context before implementation

Before modifying code or project structure, inspect:

- `PROJECT_CONTEXT.md`;
- this `AGENTS.md` and any local `AGENTS.md` in the affected subtree;
- `doc/architecture/context.md` and `doc/architecture/principles.md`;
- applicable ADRs in `doc/architecture/decisions/`;
- the active roadmap;
- the PR-specific prompt;
- relevant quality, testing, and documentation standards;
- the current repository state and existing implementation/tests in the affected area.

Do not rely only on a task description when repository evidence is available.

## Architecture rules

- Preserve established bounded-context and module ownership boundaries.
- Prefer existing abstractions and extension points over parallel implementations.
- Do not introduce a new framework, infrastructure dependency, persistence technology, cross-context contract, or architectural pattern without explicit justification and authoritative approval.
- Treat public APIs, schemas, events, migrations, persisted data, security boundaries, and deployment contracts as architecture-sensitive changes.
- Record material, durable architecture decisions as ADRs.
- Do not silently resolve architecture ambiguity. Raise a blocker when the decision is material and not determined by authoritative context.

## PR decomposition

- One PR must have one bounded architectural or engineering objective.
- Keep unrelated cleanup, refactoring, formatting, dependency upgrades, and feature work out of the PR.
- Respect roadmap dependencies. Do not implement a downstream item before required predecessor work is complete.
- If implementation reveals that the requested scope is materially larger than the bounded PR, stop and propose decomposition.
- A PR-specific prompt must state scope, non-goals, dependencies, invariants, acceptance criteria, validation, and documentation impact.

## Engineering quality

- Prefer simple, explicit designs over speculative abstractions.
- Follow SOLID/DRY where they reduce real coupling or duplication; do not create abstraction solely to satisfy a slogan.
- Preserve semantic symmetry: when an invariant applies to equivalent paths/cases, inspect all relevant cases rather than patching one observed branch.
- Avoid hidden fallback behavior that masks invalid state.
- Keep files and functions within repository-defined maintainability limits.
- Remove dead code introduced or made obsolete by the PR when it is safely inside scope.
- Never commit secrets, credentials, tokens, private keys, production data, personal data, or confidential organization-specific material.

## Testing and validation

- Add or update tests for changed behavior when technically meaningful.
- Run the smallest relevant test slice first, then the broader regression slice required by project standards.
- Record exact commands and factual results in the PR description.
- Distinguish a pre-existing baseline failure from a regression by reproducing it on the base branch when necessary.
- A pre-existing baseline defect outside the PR scope is not automatically a blocker if the PR does not worsen it and the evidence is recorded.
- Hosted CI is not assumed. If the project explicitly relies on local validation, unavailable GitHub Actions/CI is not itself a blocker.
- Never claim a test passed if it was not executed.

## Documentation

Update documentation when the PR changes:

- architecture or ownership boundaries;
- public contracts or configuration;
- operational/deployment behavior;
- developer workflow;
- durable architectural decisions;
- roadmap state.

Do not update roadmap items to `done` before repository reality supports that state.

## Independent review

A reviewer must inspect the actual PR diff and current repository state. Do not accept implementation summaries as evidence.

Review at minimum:

- scope and non-goals;
- dependency/roadmap traceability;
- architecture boundaries and invariants;
- runtime correctness and edge cases;
- duplication and reuse;
- maintainability;
- tests and validation evidence;
- documentation;
- security/privacy impact;
- repository-specific quality gates.

Classify mandatory defects as `BLOCKER` and non-blocking risks/improvements as `WARNING`. Recommend `APPROVE` only when no mandatory blockers remain.

## Agent write boundaries

Unless the task explicitly requires otherwise, an AI agent must not:

- merge or approve pull requests;
- modify unrelated files;
- rewrite repository history;
- weaken tests to make a change pass;
- remove security controls;
- expose secrets or confidential information;
- mark unresolved work as complete;
- invent test/CI results;
- silently expand scope.

## Definition of Done

A bounded PR is done when:

- requested scope is implemented and non-goals remain untouched;
- architecture invariants are preserved;
- applicable tests/validation have been executed and recorded;
- required documentation is updated;
- no mandatory review blockers remain;
- the PR is traceable to its roadmap/task context;
- known residual risks are explicitly documented.