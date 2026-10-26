# Differential Verification

Validate the result against the source artifact by semantic regions.

## Region ledger

```yaml
regions:
  - id: region-title
    intended_change: none
    expected_preservation:
      - exact_text
      - position
      - size
      - color_role
    actual_change: none
    result: PASS

  - id: region-formula-02
    intended_change: replace_formula
    expected_preservation:
      - surrounding_border
      - adjacent_labels
      - connector_geometry
    actual_change:
      - formula_replaced
    result: PASS
```

## Verification order

1. confirm requested changes;
2. inspect every immutable semantic region;
3. inspect high-risk elements;
4. compare topology;
5. compare hierarchy and line wrapping;
6. compare semantic color roles;
7. record unauthorized changes.

## Optional pixel/object diff

When tools permit:

- use pixel difference within immutable regions;
- compare vector/object IDs and properties;
- compare bounding boxes;
- compare text objects;
- compare connector paths.

Pixel differences alone are insufficient. Semantic-region verification remains mandatory.

## Regression rule

Any unauthorized modification outside approved scope is a regression, even when the edit target is correct.

## Decision

- requested change correct + no regression → `PASS`;
- requested change correct + non-semantic visual drift → `REVISE`;
- immutable text/formula/topology/hierarchy changed → `REJECT`;
- safe comparison impossible → `BLOCKED` or deterministic escalation.
