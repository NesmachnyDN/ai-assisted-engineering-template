# Manual Bootstrap Smoke Test

Use this after material changes to bootstrap tooling.

1. Create a temporary repository from the template.
2. Run `python scripts/bootstrap_check.py` without editing `PROJECT_CONTEXT.md` and confirm it reports `BLOCKED`.
3. Fill all required project-context sections with non-placeholder values.
4. Create the active roadmap referenced from `PROJECT_CONTEXT.md`.
5. Re-run the validator and confirm it reports `READY`.
6. Add `TBD — BLOCKER: test` to `PROJECT_CONTEXT.md` and confirm validation returns to `BLOCKED`.
7. Remove the blocker and run `python -m unittest discover -s tests`.
8. Use `doc/prompts/bootstrap-first-pr.md` and confirm it selects exactly one first bounded PR or reports a material bootstrap blocker without implementing product code.

This smoke test checks the adoption loop end to end without requiring a specific application stack.