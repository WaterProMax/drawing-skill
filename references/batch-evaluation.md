# Batch Evaluation and Acceptance Metrics

Use four statuses:

- `PASS`
- `REVISE`
- `REJECT`
- `BLOCKED`

`BLOCKED` means generation correctly stopped because source facts were insufficient or the selected rendering mode was unsafe. Never count it as `REJECT`.

## Metrics

- Exact-text pass rate: target 100%.
- Endpoint pass rate: target 100%.
- Word-context compliance: target 100%.
- Full-chrome share: normally <= 20%.
- Reference-layout-copy rate: target 0.
- Structural diversity: use appropriate non-card compositions across varied families; avoid unjustified `card-grid` dominance.

Record composition class:

`direct-relationship | band/layer | lane | timeline | hierarchy/tree | matrix | state/decision | sequence | card-grid | composite`

## Production batch acceptance

- 0 `REJECT` among generated figures;
- endpoint pass rate = 100%;
- exact-text pass rate = 100%;
- Word-context compliance = 100%;
- full-chrome share <= 20%;
- reference-layout-copy rate = 0;
- structurally varied tasks use multiple appropriate non-card composition classes.
