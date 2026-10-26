# Blue Structural Dominance and Sparse Accent Policy

## Purpose

Keep the AICareer diagram family visually stable by making the blueprint-blue family the only primary structural color system.

Non-blue colors remain available, but only as small, local accents.

> **Blue carries structure. Non-blue carries local emphasis or status.**

This policy does not impose universal semantic meanings on green, orange, or red.

## 1. Blue is the default structural system

Use the blueprint-blue family for:

- primary and secondary connectors;
- arrows and flow lines;
- module/container borders;
- group boundaries;
- standard icons;
- normal structural headings;
- technical dividers;
- large structural surfaces and engineering chrome.

Large-area surfaces may use only:

- `surface.background`;
- `surface.soft`;
- pale blue-family structural tones already defined in the token system.

## 2. Non-blue colors are sparse local accents

Existing non-blue accent tokens may appear only in small visual regions by default.

Preferred uses:

- status dot;
- compact badge;
- small icon accent;
- narrow left/right/top indicator strip;
- short state label;
- short local underline;
- small local border segment;
- small emphasis mark;
- short status-specific connector segment when necessary.

Do not use non-blue accents as the visual backbone of the figure.

## 3. Prohibited default uses of non-blue

Unless the user explicitly requests an exception, do not use non-blue colors for:

- full card backgrounds;
- large module backgrounds;
- full-width bands;
- large filled panels;
- large section headers;
- complete module border systems;
- the majority of a module's icons/headings/connectors simultaneously;
- long primary flow paths;
- large chart regions;
- large decorative blocks.

A technically valid non-blue token can still be a visual regression when used at excessive area or salience.

## 4. Accent area budget

For ordinary technical-document figures:

- target non-blue visual share: **5–8%**;
- normal upper bound: **10%**;
- above 10% requires an explicit exception.

This is a visual-share rule, not a literal pixel-perfect measurement requirement.

The validator should judge whether non-blue color has become a second dominant visual system.

## 5. Module accent rule

A module may declare one non-blue accent token, but that does not mean the entire module becomes green/orange/red.

Example:

```yaml
accent_context:
  accent_token: semantic.change
  scope: local
  permitted_roles:
    - status_badge
    - small_icon_accent
    - narrow_indicator_strip
```

The module's:

- main border;
- structural connector;
- body text;
- formula;
- long annotation;
- general heading hierarchy

remain governed by the blue/text system unless explicitly overridden.

## 6. Structural connectors stay blue

Primary relation meaning should remain in the blue connector system.

Non-blue connectors are allowed only when:

- the relation is a short, local status/emphasis cue;
- it does not become a major flow path;
- the same relation remains understandable without depending on color.

Do not recolor long or central flows merely because the source/target module has an accent.

## 7. Reading colors remain unchanged

This policy does not change the reading-color system.

Body text, descriptions, formulas, annotations, and metadata continue to use the text tokens defined in `visual-baseline.md`.

## 8. No automatic accent closure across the whole module

High-salience closure is now **local and bounded**.

If a compact accent cluster exists, its own small elements should be internally coherent.

But do not force:

```text
non-blue heading
+ non-blue icon
+ non-blue full border
+ non-blue connector
```

across an entire module by default.

That would turn the accent into a second structural color system.

## 9. Explicit exception

A larger non-blue region is allowed only when explicitly requested or semantically indispensable.

Record:

```yaml
non_blue_exception:
  region: "..."
  token: "existing-token"
  reason: "..."
  expected_visual_share: "..."
  scope: local
```

“Looks more attractive” is not enough.

## 10. Validation question

After generation/edit, ask:

> If all non-blue accents were removed, would the diagram still retain its complete structural hierarchy and connectivity?

If no, non-blue has been used as structure rather than accent and the figure must be revised.
