# Semantic-Role Color Usage Policy

## Scope

The color tokens already exist. This policy controls **how existing tokens are used**.

The goal is visual consistency, not a universal color language.

> **Module color provides visual identity. Reading color provides stable readability. Color may carry semantics when explicitly declared, but no accent color is required to have one fixed meaning everywhere.**

This replaces rigid color semantics with:

```text
Global Reading Color Strategy
+
Blueprint-Blue Structural System
+
Sparse Local Accent Context
+
Optional Explicit State Semantics
```

Read `blue-structure-accent-policy.md` for the structural dominance rule.

## Core law

> Classify the visual role first. Bind an existing token second.

Never choose color merely because a nearby object uses it.

## 1. Global reading roles — strict and cross-module

These roles follow the same strategy across all modules:

| Visual role | Default token strategy |
|---|---|
| figure title | `text.strong` |
| section/group/card heading | `text.strong` or `text.primary` according to hierarchy |
| standard node title | `text.primary`; `text.strong` only for genuine hierarchy |
| body/content text | `text.primary` |
| secondary description | `text.secondary` |
| metadata/helper text | `text.muted` |
| formula/equation | `text.primary`; emphasized result may use `text.strong` |
| technical annotation | `text.secondary`; low-priority note may use `text.muted` |

Reading roles must not inherit the surrounding module accent automatically.

A green/orange/blue module does **not** imply green/orange/blue body text.

## 2. Structural roles — may follow a module accent

A module or local visual context may declare one approved accent token.

Example:

```yaml
accent_context:
  id: human-review-module
  accent_token: semantic.positive
  reason: visual_identity
```

The accent may apply only to a **small, bounded accent cluster** by default:

- compact badge/status label;
- small icon accent;
- narrow indicator strip;
- short local underline or border segment;
- short local status connector when genuinely useful.

The module's main border, primary flow connectors, and general structural backbone remain in the blueprint-blue family.

This is a **visual consistency rule**, not a requirement that the accent token carry a fixed semantic meaning.

## 3. Accent token meaning is optional, not global

Existing accent tokens include:

- `semantic.positive`;
- `semantic.change`;
- `semantic.critical`.

Their historical names do **not** create a global hard mapping in this Skill.

They may be used in two ways:

### A. Visual identity use

```yaml
accent_token: semantic.positive
reason: visual_identity
```

This means “use the green accent consistently for this visual context.” It does **not** automatically mean success, growth, confirmation, or upward movement.

### B. Explicit semantic/state use

```yaml
accent_token: semantic.critical
reason: explicit_state
state_meaning: rejected
```

When a color is intentionally used to encode state, that local semantic mapping must remain consistent within the figure or explicitly declared scope.

Therefore:

> Color semantics are optional and local. They are not globally inferred from the token name.

## 4. Same role, same strategy

Across modules:

- body text uses the same reading strategy;
- equivalent headings use the same hierarchy strategy;
- formulas use the same formula strategy;
- equivalent high-salience structural roles use their declared module accent consistently.

Do not create module-specific rules such as:

```text
blue module body = blue
orange module body = orange
green module formula = green
```

## 5. Identity color vs reading color

Accent/identity color may appear on small local roles such as:

- compact identity/status badge;
- small icon accent;
- narrow accent strip;
- short underline/border segment;
- short local status connector.

Large module borders, major headings, and primary structural connectors should remain blue by default.

It must not automatically propagate into:

- body text;
- long descriptions;
- formulas;
- technical annotations;
- metadata;
- unrelated connectors;
- neighboring modules.

## 6. No-neighbor inference

Never infer a token because of:

- parent container color;
- nearest border;
- nearest icon;
- neighboring module;
- local visual balance;
- reference-image proximity.

Each colored property must come from:

1. its global reading role; or
2. its declared accent context; or
3. an explicit local exception.

## 7. Bounded accent-context closure

Read `visual-context-closure.md`.

Accent closure applies only inside a compact local accent cluster.

Do not expand a non-blue accent across the whole module merely to make all high-salience roles match.

The blueprint-blue family remains the global structural backbone.

This closure does not apply to body text, formulas, long annotations, metadata, main module borders, or major flow connectors.

## 8. Connectors

Connector meaning should be communicated primarily by:

- source/target;
- direction;
- line style;
- labels;
- grouping/topology.

Color may reinforce a local accent or explicit state, but relation semantics must not depend on color alone.

Do not require “feedback = green”, “warning = orange”, or “failure = red” globally.

## 9. Explicit exceptions

A deviation must be documented only when it breaks the normal role/context mapping.

```yaml
exception:
  element_id: "..."
  property: icon | border | connector | label | formula | annotation
  token: "existing-token-name"
  reason: "explicit local visual or semantic reason"
  scope: local
```

Valid reasons include:

- `visual_identity`;
- `hierarchy_emphasis`;
- `explicit_state`;
- `relation_distinction`.

“Looks better here” or “nearby element uses it” is not sufficient.

## 10. Local edit isolation

For localized edits:

```yaml
edit_scope:
  targets: [element-id]
  properties: [primary_icon]
  preserve:
    - body_text
    - formulas
    - unrelated_borders
    - unrelated_connectors
    - sibling_modules
```

Changing one accent role must not recolor unrelated roles or regions.

## 11. Cross-module consistency

After generation/edit:

1. group equivalent roles across modules;
2. compare their reading strategy;
3. compare each module's high-salience accent closure;
4. confirm differences are declared, not accidental;
5. do **not** reject an accent merely because its token name does not match a fixed semantic meaning.

## Decision

- `PASS`: reading roles are globally consistent; each accent context is internally coherent; no accidental inheritance/spillover exists.
- `REVISE`: visual identity or equivalent-role strategy is inconsistent, but meaning is intact.
- `REJECT`: color changes technical meaning, creates a false hierarchy/state/relation, or a localized edit changes unrelated locked styling.

Also `REJECT` when non-blue visual share exceeds the normal upper bound (about 10%) or when a full card/module is filled with a non-blue color. See `blue-structure-accent-policy.md` and `color-consistency-qa.md`.

## Example — semantic color classification

Formerly `example.md`. A Human-in-the-loop card with green feedback semantics:

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

Under blue structural dominance, that green border is a short local accent segment, not a complete major-module border and not a full-card non-blue fill. If the card face itself is filled with `semantic.positive`, color QA returns `REJECT`.
