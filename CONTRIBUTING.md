# Contributing

Contributions should preserve the repository's primary goal: provide a small, reusable, architecture-governed workflow for AI-assisted software engineering.

## What belongs here

Good contributions improve one of these areas:

- project/architecture context templates;
- bounded-PR decomposition;
- AI implementation/review/remediation prompts;
- testing and evidence practices;
- architecture decision traceability;
- examples that clarify the workflow without tying it to one technology stack.

Avoid turning the repository into a large prompt catalog, framework-specific starter kit, or generic software-engineering handbook.

## Change process

1. Open or select one bounded issue/objective.
2. Keep the change focused; separate unrelated cleanup.
3. Update examples when a template change would otherwise become ambiguous.
4. Review documentation links and terminology for consistency.
5. Use `.github/pull_request_template.md` for the PR body.

## Design criteria

A proposed addition should answer at least one of these questions better than the current template:

- How does an AI agent know what context is authoritative?
- How do we prevent it from inventing architecture?
- How do we keep one PR bounded and traceable?
- How do we validate implementation claims?
- How do we distinguish baseline failures from regressions?
- How do we perform an independent review?
- How do we preserve human governance over material decisions?

## Compatibility

Template consumers may copy and adapt files. Prefer additive evolution and clear migration notes when changing file names, directory structure, or prompt semantics.

## Security and privacy

Do not contribute real credentials, internal company identifiers, production data, private architecture diagrams, customer information, or confidential prompts. Use fictional examples.