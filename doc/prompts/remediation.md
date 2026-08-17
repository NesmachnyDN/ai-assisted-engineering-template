# Prompt: Remediate Review Blockers

```text
Repository: <owner/repo>
Pull request: <URL or number>
Current branch: <existing PR branch>
Review findings: <paste/link authoritative review>

Remediate the current PR in place. Do not create a new PR or start the next roadmap phase.

Before changing code:
1. Read root/local AGENTS.md and applicable repository standards.
2. Read the active roadmap and PR-specific prompt.
3. Inspect the current PR HEAD and each reported blocker in repository context.
4. Determine root cause rather than patching only the observed symptom.
5. When a blocker concerns an invariant, inspect symmetric/equivalent cases that may share the defect.

Rules:
- Fix all mandatory blockers that are valid for this PR scope.
- Do not expand into unrelated cleanup or future roadmap work.
- Preserve architecture boundaries and non-goals.
- Do not weaken tests.
- If a blocker requires a new material architecture decision not determined by authoritative context, stop and report an architecture blocker.
- Preserve existing branch/PR continuity.

Validation:
- Run targeted tests for each remediation.
- Run the required regression slice.
- Run repository quality checks applicable to touched files.
- For suspected baseline failures, compare against the base branch and report exact evidence.

Update the PR description with factual validation results when repository workflow requires it.

Return one consolidated report:
1. Blockers addressed and root causes.
2. Changes made.
3. Validation commands and exact results.
4. Remaining warnings/known baseline issues.
5. Whether the PR is ready for independent re-review.

Do not merge, approve, resolve review threads, or begin another roadmap item unless explicitly instructed.
```