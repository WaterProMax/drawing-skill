# Generation Gates — Completeness, Review, Composition, Context, and Sequence

Consolidated pre-generation reference for `drawing-skill`. Run these gates before pixels are produced. A visual-preset override (default `visual_preset = aicareer-blueprint`) does not skip any gate in this file.

Former standalone notes folded here without dropping their rules: `source-completeness-gate.md`, `semantic-review-gate.md`, `composition-policy.md`, `output-context-profiles.md`, `reference-image-policy.md`, `sequence-reliability.md`.

## Source completeness gate

Statuses:

- `READY` — enough facts exist.
- `READY_NEUTRAL` — only neutral structure is supported.
- `BLOCKED` — requested semantics would require invention.

Require explicit evidence for mappings, evaluated comparisons, temporal classifications, branch destinations, and sequence endpoints.

`BLOCKED` is correct governance, not a rendering failure. Do not invent technical content to get out of `BLOCKED`.

Skill-wide review statuses remain `PASS` / `REVISE` / `REJECT` / `BLOCKED`. Completeness uses `READY` / `READY_NEUTRAL` / `BLOCKED` before generation; it does not replace those four review statuses after a figure exists.

## Diagram semantic review gate

Before generation verify:

1. one clear purpose;
2. complete and supported logic chain;
3. explicit relation semantics;
4. no false feedback loop;
5. no duplicated concepts;
6. stable system boundary;
7. canonical terminology;
8. consistent abstraction level;
9. cross-document consistency.

For complex figures perform two passes: structural review, then consistency review.

Output `Ready to Generate: YES/NO`. Stop on meaning-changing uncertainty.

If `Ready to Generate = NO`, stop. Do not proceed to generation or to a full regeneration that would hide the gap.

## Composition policy — structure before cards

Prefer direct relations, layers/bands, lanes, timelines, hierarchy/tree, matrix, and bounded groups before cards.

Prefer, in this order:

```text
direct relationships
→ bands/layers
→ lanes
→ timelines
→ hierarchy/tree
→ matrix
→ boundaries
→ cards
```

Cards are justified only when an item has independent internal anatomy such as a metric, insight, numbered process step, or comparable method.

The reference controls visual language, not universal layout.

## Output context profiles

Default:

```yaml
output_context: word-embedded-figure
caption_external: true
title_mode: compact
chrome_profile: standard
```

Standard Word chrome: no complete perimeter frame, no four large corner crosshairs, no decorative footer, and no full internal title when an external caption exists.

Target readability is approximately 160 mm width in Word/WPS. At that size, an outer perimeter frame and a title that duplicates the external caption are both failures (`REJECT` or `REVISE` until removed).

Use full chrome only for genuine hero/overview figures; normally no more than roughly 20% of a document figure set.

## Reference image policy

Primary default reference:

```text
assets/reference-blueprint.png
```

Preset id: `visual_preset = aicareer-blueprint` (AICareer Research Engineering Blueprint). Use the reference for visual language, not topology or layout copying. Another project, course, or competition preset may replace the reference image only when that preset is explicitly declared. The choice of reference never authorizes copying its topology.

Choose `full-reference` or `style-baseline-only`.

Use `style-baseline-only` when the task topology overlaps the reference or when another diagram family could be biased by its layout.

When task topology substantially overlaps the reference, use `style-baseline-only`.

Never copy central-hub layout, panel arrangement, footer, full chrome, or card grammar without structural justification.

## Complex sequence reliability

Image-only mode only when participants <= 6, messages <= 8, and no complex parallel + loop/alt combination.

Otherwise use a deterministic/hybrid skeleton and apply AICareer visual styling without letting the image model redraw message geometry. If unavailable, split/simplify or return BLOCKED.

When `visual_preset` is not `aicareer-blueprint`, apply the declared preset's styling in that same deterministic/hybrid skeleton. The image model still must not redraw message geometry.

Parallel execution must not become serial chaining. Sequence family gate: explicit participants and messages are required.
