# Prompt: Independent Full-Diff PR Review

```text
Repository: <owner/repo>
Pull request: <URL or number>
Base branch: <branch>

Perform a strict, independent full-diff review of the current PR HEAD using the repository's current authoritative workflow.

Restore context yourself before judging the change:
- root and applicable local AGENTS.md files;
- PROJECT_CONTEXT.md;
- architecture context, principles, and applicable ADRs;
- code quality, testing, and documentation standards;
- active roadmap/state/history;
- PR-specific implementation prompt;
- PR metadata, dependencies, actual diff, tests, and available validation evidence.

Do not rely on the PR description or implementation summary as proof. Inspect repository reality.

Review:
1. PR metadata and bounded scope.
2. Dependency/predecessor completion.
3. Scope vs PR-specific prompt and roadmap traceability.
4. Architecture boundaries and invariants.
5. Runtime correctness, edge cases, failure semantics, and symmetric cases.
6. Duplication, reuse, maintainability, and unnecessary complexity.
7. File/function size and repository-specific quality rules.
8. Tests: adequacy, regression coverage, and factual results.
9. Documentation/ADR/roadmap impact.
10. Security, privacy, compatibility, and migration concerns where applicable.
11. CI status when CI exists; when repository policy explicitly uses local validation, unavailable hosted CI is not itself a blocker.

If a reported test failure may be pre-existing, require evidence against the base branch before treating it as baseline rather than regression.

Do not limit review to lines changed after an earlier review when a fix affects an architectural invariant or symmetric cases.

Classify findings:
- BLOCKER: mandatory before merge.
- WARNING: important but not independently merge-blocking.

Output structure:
# PR Review Summary
## Scope and Traceability
## Architecture and Design
## Runtime Correctness
## Engineering Quality
## Tests and Validation
## Documentation
## Blockers
## Warnings
## Final Recommendation

Final Recommendation must be APPROVE only when no mandatory blockers remain; otherwise REQUEST CHANGES.

Do not comment on GitHub, approve, request changes, resolve threads, or merge unless explicitly authorized by the user.
```