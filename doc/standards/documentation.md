# Documentation Standard

Documentation should preserve decisions and operational knowledge that cannot be safely inferred from code alone.

## Update documentation when changing

- architecture or bounded-context ownership;
- public APIs/events/schemas/configuration;
- persistence or migration behavior;
- deployment/operations;
- security/trust boundaries;
- developer workflow or validation commands;
- roadmap state;
- a durable architectural decision.

## ADR rule

Create or supersede an ADR when a decision is:

- architecturally material;
- expected to survive beyond one PR;
- non-obvious or involves meaningful trade-offs;
- likely to be questioned or revisited later.

Do not create ADRs for routine implementation choices.

## Documentation quality

- Prefer precise statements and executable examples over aspirational prose.
- Identify authoritative vs explanatory documents.
- Avoid duplicating the same rule across multiple files; link to the authority.
- Mark deprecated/superseded material explicitly.
- Keep examples free of secrets, production data, personal data, and confidential internal identifiers.

## Roadmap updates

Roadmaps describe repository reality and intended sequencing. Do not mark work complete merely because an agent claims completion. Use merged implementation and validation/review evidence as the basis for state changes.