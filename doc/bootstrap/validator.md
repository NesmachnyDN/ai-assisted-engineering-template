# Bootstrap Validator Contract

`scripts/bootstrap_check.py` is a deliberately small, stdlib-only readiness gate. It exists to catch mechanical adoption errors before an AI reviewer spends time interpreting the project.

## What it checks

- `PROJECT_CONTEXT.md` exists;
- root `AGENTS.md` exists;
- required top-level project-context sections exist;
- required identity fields are present and no longer contain template placeholders;
- unresolved `<...>` template placeholders are absent from `PROJECT_CONTEXT.md`;
- unresolved `TBD — BLOCKER` markers are absent;
- `Current roadmap` names an active Markdown roadmap path;
- that roadmap file exists;
- the last completed bounded PR is stated.

## What it intentionally does not check

The validator must not pretend to make architecture judgments. It does not decide whether:

- the chosen architecture is appropriate;
- bounded-context boundaries are semantically correct;
- a roadmap item is small enough;
- acceptance criteria are complete;
- validation commands actually provide sufficient coverage;
- an ADR is technically sound;
- confidential information is semantically present in otherwise ordinary text.

Those remain qualitative review responsibilities and are covered by the adoption checklist and independent review prompts.

## Usage

From the repository root:

```bash
python scripts/bootstrap_check.py
```

or:

```bash
python3 scripts/bootstrap_check.py
```

To validate another repository root:

```bash
python scripts/bootstrap_check.py --root /path/to/repository
```

Success:

```text
BOOTSTRAP CHECK: READY
```

Blocked adoption returns exit code `1` and prints each detected problem.

## Regression tests

```bash
python -m unittest discover -s tests
```

The tests cover a ready context, unresolved placeholders, explicit blockers, a missing active roadmap file, and a missing required section.

## Portability

The script uses only Python's standard library. Projects that do not want Python in their toolchain may replace it with an equivalent validator, but should keep the same conceptual contract: machine-checkable adoption defects fail fast; architectural quality stays under explicit review.