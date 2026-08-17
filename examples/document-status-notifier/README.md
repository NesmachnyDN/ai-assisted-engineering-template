# Worked Example — Document Status Notifier

This example demonstrates how the template can be filled for a small but realistic service.

The fictional system receives document-status changes, persists delivery state, and sends notifications to an external channel. It is deliberately small so that the workflow remains visible.

## Example flow

```text
Roadmap item PR-1.1
    ↓
PR-specific prompt
    ↓
Implementation
    ↓
Tests
    ↓
Independent review
    ↓
Remediation if needed
    ↓
Merge + roadmap update
```

Files in this example:

- `PROJECT_CONTEXT.md` — filled project context;
- `roadmap.md` — small executable roadmap;
- `pr-1.1-idempotent-delivery.md` — example PR-specific implementation prompt;
- `review-example.md` — example review output after implementation.

This is an example of the **workflow artifacts**, not a complete application.