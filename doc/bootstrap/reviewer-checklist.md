# Bootstrap Reviewer Checklist

Use this when reviewing a project's bootstrap PR before product implementation begins.

- [ ] `PROJECT_CONTEXT.md` is project-specific and machine validation reports `READY`.
- [ ] Scope and explicit non-goals are coherent.
- [ ] Architecture/module ownership is sufficiently explicit for the first roadmap item.
- [ ] Authoritative sources have clear precedence.
- [ ] Critical invariants are observable and relevant.
- [ ] Validation commands and CI/local-evidence policy are realistic.
- [ ] Confidentiality/publication constraints are explicit.
- [ ] The active roadmap exists and the first candidate has satisfied dependencies.
- [ ] The candidate is one bounded objective rather than a batch of unrelated work.
- [ ] Material architecture decisions are resolved or correctly block implementation.
- [ ] Human architecture and merge authority remain explicit.

Approve bootstrap readiness only when an implementation agent can proceed without inventing project truth.