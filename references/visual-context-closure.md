# Bounded Accent Context Closure

## Purpose

Keep small non-blue accent clusters internally coherent without turning green/orange/red into a second structural color system.

## Core rule

> The blueprint-blue family owns the structural backbone. Non-blue accent closure is local, compact, and bounded.

## Default structural roles

These remain blue by default:

- main module border;
- group/container boundary;
- major heading hierarchy;
- primary structural icon;
- primary flow connector;
- long dependency/reference connector;
- engineering divider/chrome.

## Permitted compact accent roles

A local accent context may cover:

- status dot;
- compact badge;
- small state icon;
- narrow accent strip;
- short label;
- short underline or border segment;
- short local status connector.

Example:

```yaml
accent_context:
  id: review-status
  accent_token: semantic.positive
  scope: compact_local
  permitted_roles:
    - status_badge
    - state_icon
    - narrow_indicator_strip
```

## Closure rule

Within one compact accent cluster, equivalent accent-bearing elements should use one coherent token.

Do not produce:

```text
green status badge
+ orange status icon
```

for the same local state unless explicitly justified.

## Anti-expansion rule

Do not infer:

```text
green badge
→ green module title
→ green full border
→ green primary icon
→ green long connector
```

The accent must remain local.

## Reading roles remain global

Body text, formulas, annotations, metadata, and long descriptions use the global reading-color system.

## Area rule

Non-blue accents should normally remain within approximately 5–8% of visual share and should not exceed roughly 10% without an explicit exception.

## Regression rule

Treat any of the following as a visual regression:

- a large non-blue filled panel;
- a full non-blue module background;
- a long non-blue primary flow;
- a complete non-blue border system around a major module;
- non-blue becoming visually co-dominant with blueprint blue;
- local accent spreading into unrelated regions.

A token being valid does not make excessive usage valid.
