# Bootstrap Validator Acceptance Criteria

The validator is acceptable when all of the following hold:

- a fully populated project context with an existing active roadmap returns exit code `0`;
- unresolved template placeholders return exit code `1`;
- explicit `TBD — BLOCKER` markers return exit code `1`;
- a missing active roadmap file returns exit code `1`;
- a missing required project-context section returns exit code `1`;
- output clearly distinguishes `READY` from `BLOCKED`;
- the implementation uses only Python standard-library modules;
- tests run with `python -m unittest discover -s tests`;
- the validator does not attempt to judge architectural quality or roadmap semantics.

These criteria deliberately separate structural readiness from architectural correctness.