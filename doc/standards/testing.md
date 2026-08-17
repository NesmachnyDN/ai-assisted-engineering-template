# Testing and Validation Standard

## Test pyramid / strategy

Define the project's actual test layers:

| Layer | Purpose | Command |
| --- | --- | --- |
| Unit | `<...>` | `<...>` |
| Integration | `<...>` | `<...>` |
| Contract | `<...>` | `<...>` |
| End-to-end | `<...>` | `<...>` |
| Static/lint/type | `<...>` | `<...>` |

Remove layers that do not apply.

## PR validation rules

- Run targeted tests for changed behavior first.
- Run the broader regression slice required for the affected subsystem.
- Add regression tests for defects when they provide stable value.
- Never modify a test merely to encode incorrect implementation behavior.
- Record exact commands and results in the PR description.

## Baseline failures

When a relevant test fails on the PR branch and may be pre-existing:

1. reproduce the same command or minimal equivalent on the base branch;
2. record both results;
3. verify the PR did not worsen the failure;
4. classify it as baseline only when evidence supports that conclusion.

A confirmed pre-existing failure outside the bounded PR is not automatically a blocker. A regression introduced or worsened by the PR is a blocker unless explicitly accepted by project policy.

## CI

Hosted CI is optional for this template. Select the project model in `PROJECT_CONTEXT.md`:

- **Hosted CI authoritative** — required checks must pass.
- **Local validation authoritative** — exact local commands/results are the primary evidence; absence of hosted CI is not a blocker.
- **Hybrid** — define which checks run where.

Never report a CI or local test result that was not actually observed.