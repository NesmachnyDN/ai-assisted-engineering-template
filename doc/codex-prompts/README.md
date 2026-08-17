# PR-Specific Prompts

Store generated implementation prompts here when prompt traceability is part of the project workflow.

Recommended structure:

```text
doc/codex-prompts/
└── <roadmap-or-task>/
    └── pr-<id>-<short-name>.md
```

These are **project-specific execution artifacts**, unlike the reusable templates under `doc/prompts/`.

A PR-specific prompt should include:

- authoritative context to read;
- objective and rationale;
- dependencies;
- exact scope and non-goals;
- architecture boundaries and invariants;
- acceptance criteria;
- required tests/validation;
- documentation/roadmap updates;
- explicit stop conditions for unresolved architecture decisions.

Projects may choose to keep only the currently active prompt in a roadmap/task directory to reduce stale context. If prompts are retained historically, mark their status clearly and do not allow an agent to treat merged prompts as current instructions.