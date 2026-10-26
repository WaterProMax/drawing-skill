# Example — Semantic Color Classification

A Human-in-the-loop card with green feedback semantics:

```yaml
element:
  id: human-review
  state: positive
  identity_group: human-feedback

color_bindings:
  heading_text: text.strong
  body_text: text.primary
  icon: semantic.positive
  border: semantic.positive
  feedback_connector: semantic.positive
```

The green border/icon/connector does not recolor the heading or body text.
