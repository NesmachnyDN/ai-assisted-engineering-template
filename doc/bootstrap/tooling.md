# Bootstrap Tooling

The template keeps bootstrap automation intentionally small.

## Included

- `scripts/bootstrap_check.py` — structural readiness gate;
- `tests/test_bootstrap_check.py` — validator regression tests;
- `doc/bootstrap/*` — human-readable readiness, decision, and smoke-test guidance;
- `doc/prompts/bootstrap-first-pr.md` — reasoning gate that produces one implementation-ready PR prompt or a blocker.

## Design constraint

Automation may validate structure and explicit repository facts. It must not silently promote itself into an architecture decision engine. Semantic quality, ownership, decomposition, security implications, and acceptance policy remain subject to explicit review.