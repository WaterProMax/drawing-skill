# Prompt Skeleton

```text
TASK MODE
create-new

Create one standalone technical figure for a formal technical document.
Default visual_preset = aicareer-blueprint (AICareer Research Engineering Blueprint) unless the task explicitly supplies another visual_preset.
A preset override does not waive source completeness, canonical content lock, or QA.

TECHNICAL PURPOSE
[exact purpose]

EXACT CONTENT
[approved elements, groups, relations, exact visible text]

OUTPUT CONTEXT
output_context: [word-embedded-figure/...]
title_mode: [none/compact/full]
chrome_profile: [minimal/standard/full]
composition_mode: structural-first
reference_mode: [full-reference/style-baseline-only]

SEMANTIC COLOR POLICY
Use only the existing tokens from visual-baseline.md.
Do not invent, approximate, lighten, darken, or blend colors.
Classify every property by semantic visual role before applying color.

Role bindings:
- headings → text.strong
- body/content → text.primary
- secondary descriptions → text.secondary
- metadata/low-priority notes → text.muted
- formulas/equations → text.primary; emphasized result → text.strong
- default icons → blue.core
- standard borders → blue.border
- primary borders → blue.core
- primary flow → blue.core
- dependency/reference → blue.medium/blue.secondary according to the approved line rule
- genuine feedback → semantic.positive
- genuine change/warning → semantic.change
- genuine failure/rejection → semantic.critical

Reading colors do not inherit module identity.
A colored border/icon/container does not recolor heading, body, formula, annotation, connector, or child elements.
Use approved semantic exceptions only:
[exceptions or NONE]

LOCAL EDIT ISOLATION
Targets: [...]
Properties allowed to change: [...]
Preserve unchanged: [...]

VISUAL LANGUAGE
Use the Research Engineering Blueprint baseline: white/pale surface, cool blueprint blue, outline icons, thin technical lines, restrained grid and chrome.

PROHIBITIONS
- no new colors;
- no module-specific body-text logic;
- no color inheritance from nearby elements;
- no unrelated recoloring;
- no false state colors;
- no invented content or relations;
- no dark/neon/3D/cartoon/rainbow styling.

READABILITY
Readable at approximately 160 mm in Word/WPS; no microtext.
```
