# Prompt Template: Implement One Bounded PR

```text
Repository: <owner/repo>
Base branch: <branch>
PR/task: <id and title>
PR-specific prompt: <path>

Implement exactly the bounded PR described by the PR-specific prompt.

Before changing files:
1. Inspect the current branch/repository state.
2. Read root AGENTS.md and every applicable local AGENTS.md for touched areas.
3. Read PROJECT_CONTEXT.md, relevant architecture context/principles/ADRs, active roadmap, standards, and the PR-specific prompt.
4. Inspect existing implementation and tests in the affected area before designing changes.
5. Confirm scope, dependencies, invariants, and non-goals.

Implementation rules:
- Stay strictly inside the bounded PR.
- Reuse existing abstractions and patterns when appropriate.
- Do not introduce material architecture decisions that are absent from authoritative context.
- If implementation requires such a decision, stop and report an architecture blocker.
- Do not weaken tests or bypass invariants to obtain a passing result.
- Do not perform unrelated refactoring or dependency upgrades.
- Check symmetric/equivalent execution paths when an invariant is affected.
- Add/update tests and documentation required by the change.

Validation:
- Run the smallest relevant checks first.
- Run the broader regression checks required by repository standards.
- If a failure appears pre-existing and matters to acceptance, reproduce it on the base branch before classifying it as baseline.
- Record exact commands, pass/fail counts where available, and any known baseline defect.
- Do not claim hosted CI results unless actually observed.

Before completion, perform a self-review of the full diff against scope, invariants, tests, documentation, and repository standards.

Final report:
1. Summary of implementation.
2. Files changed.
3. Architecture/behavior notes.
4. Validation commands and factual results.
5. Known issues or baseline failures.
6. Confirmation that non-goals were not implemented.

Do not merge or approve the PR unless explicitly instructed by an authorized human.
```