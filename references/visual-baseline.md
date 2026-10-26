# Visual Baseline — Research Engineering Blueprint

The bundled `assets/reference-blueprint.png` is the visual reference.

## Overall temperament

- precise, structured, technical, auditable;
- white background with faint cool-blue engineering grid;
- medium-high density with disciplined alignment;
- blue-family reading text rather than black;
- no visual spectacle for its own sake.

## Existing color tokens — authoritative values

The tokens already exist. **Do not create or modify values.** Usage is governed by `semantic-color-policy.md`.

### Blueprint blue family

| Token | Hex |
|---|---|
| `blue.deep` | `#061D81` |
| `blue.core` | `#0C379C` |
| `blue.strong` | `#2E499C` |
| `blue.medium` | `#4B66AD` |
| `blue.secondary` | `#657FBB` |
| `blue.light` | `#7895CD` |
| `blue.border` | `#91A9D6` |
| `blue.subtle` | `#B8C8E7` |
| `blue.grid` | `#E3EAF7` |
| `surface.background` | `#FFFFFF` |
| `surface.soft` | `#F7FAFE` |

### Text family

| Token | Hex |
|---|---|
| `text.strong` | `#082B6F` |
| `text.primary` | `#163A73` |
| `text.secondary` | `#38588A` |
| `text.muted` | `#6479A0` |

### Accent palette (existing tokens; semantics optional)

| Token | Hex | Meaning |
|---|---|---|
| `semantic.positive` | `#2F8F70` | green accent token; may express identity or an explicitly declared local state |
| `semantic.change` | `#C97A20` | orange accent token; may express identity or an explicitly declared local state |
| `semantic.critical` | `#B54747` | red accent token; may express identity or an explicitly declared local state |

Accent colors are sparse and local. They do not replace reading colors or the blueprint-blue structural system. Token names are legacy identifiers and do not impose a mandatory global semantic mapping.

**Blue structural dominance:** non-blue accents should normally occupy only about 5–8% of visual share and should not exceed roughly 10% without an explicit exception. Large non-blue filled regions are not part of the default AICareer visual language.

## Typography feeling

- Chinese: Noto Sans SC / Source Han Sans style.
- English/numbers: Inter style.
- Figure title: 42 px hero or 20–26 px compact Word title.
- Section title: 20 px.
- Core title: 24 px.
- Node/card title: 16–17 px.
- Body: 14 px.
- Technical annotation: 13–14 px.
- Metric value: 30 px.

These are relative guides, not permission to shrink text below Word readability.

## Geometry feeling

- 4 px base grid, 8 px major rhythm;
- balanced density;
- 48 px canvas margin on a 1086 px source canvas;
- 16 px node padding;
- thin borders, slightly stronger core boundary;
- little or no shadow.

## Component language

Use generic visual primitives: entity, actor, process, metric, insight, group, chart, annotation. Business nouns such as Agent, database, or frontend are semantic hints, not separate styling systems.

## Connectors

- primary flow: `blue.core`, solid;
- dependency/reference: `blue.medium` or `blue.secondary`, thinner/dashed as defined;
- major and long structural connectors stay in the blue family;
- non-blue connectors are limited to short, local status/emphasis cues;
- explicit state/status coloring is optional and local;
- relation meaning must remain understandable from topology, direction, line style, and labels rather than color alone.

## Chrome

Use full chrome only for hero figures. Standard/minimal chrome is the Word default.
