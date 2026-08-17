# Bootstrap FAQ

## Do I need to fill every template file before coding?

No. Follow `BOOTSTRAP.md`. Fill the minimum authoritative project contract, establish the first roadmap, pass readiness gates, and only open deeper templates when a real decision requires them.

## Can the AI choose missing architecture decisions for me?

It may propose alternatives, but a material unresolved decision is a blocker until an authorized human/project authority resolves it.

## Do I need hosted CI?

No. `PROJECT_CONTEXT.md` defines whether hosted CI, local validation, or a hybrid model is authoritative. Exact observed evidence is required either way.

## Why exactly one bounded PR?

It keeps scope, acceptance, review, and rollback tractable and prevents a roadmap from becoming one opaque AI-generated batch.

## Is the validator an architecture checker?

No. It catches structural adoption errors only. Architecture quality and semantic completeness remain review responsibilities.

## Can I replace the Python validator?

Yes. Keep an equivalent fail-fast readiness contract and update `BOOTSTRAP.md`, project context, and validation documentation accordingly.