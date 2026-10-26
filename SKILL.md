---
name: aicareer-diagram-style
description: Create or edit semantically rigorous AICareer technical diagrams with a consistent Research Engineering Blueprint visual language. Distinguish new generation from constrained editing, lock critical text/formulas/topology, minimize regeneration scope, bind existing color tokens by global reading role and local accent context, run differential regression checks, and escalate to deterministic rendering when generative image models cannot guarantee fidelity.
compatibility: Agent Skills-compatible agents. Best with tools that support local image editing, masks, vector/document objects, or reference images. If reliable editing is unavailable, produce a preservation contract and deterministic edit plan instead of silently regenerating the full artifact.
metadata:
  project: AICareer
  version: "0.7.2"
  mode: fidelity-constrained-generation-and-editing
---

# AICareer Diagram Style Skill

## Purpose

Create or edit document-ready technical figures that:

1. preserve exact technical meaning;
2. preserve validated source artifacts during edits;
3. use the smallest semantically authorized change surface;
4. belong to one coherent AICareer visual family;
5. remain readable at approximately 160 mm width in Word/WPS;
6. use mature diagram/research frameworks when appropriate;
7. stop rather than invent missing facts;
8. use existing color tokens through semantic-role and visual-context rules;
9. prevent regressions introduced by probabilistic image reconstruction;
10. escalate to deterministic rendering when exactness dominates creativity.

## Core operating principles

> **Visual generation must never become a second author of technical content.**

> **For editing: explicitly requested changes are mutable; everything else is immutable by default.**

> **Preserve a validated artifact and apply the smallest semantically authorized change.**

> **An edit succeeds only when the requested change is correct and unrelated content remains unchanged.**

## Task mode routing — mandatory

Read `references/task-mode-router.md` first.

```text
request
→ create-new
OR
→ edit-existing
OR
→ reconstruct-approved
OR
→ deterministic-render
```

Never silently convert an edit into full regeneration.

If the requested source artifact is missing, unusable, or not actually available, return `BLOCKED`.

## Default workflow

### Create-new

```text
single communication question
→ diagram type / framework routing
→ Source Completeness Gate
→ family-specific preflight
→ Diagram Content Spec + relation/message/mapping ledgers
→ semantic/framework audit
→ output context and composition
→ canonical content lock
→ color-role/accent-context classification
→ generation
→ exact-text / formula / endpoint / visual-semantic QA
→ Word/WPS QA
```

### Edit-existing

```text
source artifact validation
→ immutable baseline snapshot
→ Edit Contract
→ canonical text/formula/topology/hierarchy locks
→ high-risk element inventory
→ smallest safe edit method
→ local edit
→ differential verification
→ preservation/regression QA
→ local repair only
→ deterministic escalation if needed
```

## Hard rules

- If `Ready to Generate = NO`, stop.
- Use `PASS / REVISE / REJECT / BLOCKED` as distinct statuses.
- `BLOCKED` is correct governance, not a rendering failure.
- Do not invent technical content, relations, mappings, states, evaluation results, or feedback loops.
- Do not paraphrase locked text.
- Do not treat formulas as decorative pixels.
- Do not modify topology unless explicitly requested.
- Do not change locked line breaks to solve layout pressure.
- Do not solve a local edit by global regeneration without explicit approval.
- Do not infer permission to redesign from a repair request.
- Use only existing color tokens in `visual-baseline.md`.
- A local edit must preserve unrelated text, icons, borders, formulas, connectors, and modules.

## Status policy

Use:

- `PASS`
- `REVISE`
- `REJECT`
- `BLOCKED`

`BLOCKED` means the source is incomplete, the requested artifact is unavailable, or the chosen rendering method cannot meet required fidelity without a deterministic alternative.

## Source completeness and family routing

Read:

- `references/source-completeness-gate.md`
- `references/family-gates.md`
- `references/diagram-type-router.md`
- `references/diagram-types.md`

Use C4 / DSRM / CRISP-DM only when they fit the actual question.

## Fidelity and preservation — mandatory for edits

Read:

- `references/fidelity-preservation-policy.md`
- `references/task-mode-router.md`
- `references/canonical-content-lock.md`
- `references/formula-integrity.md`
- `references/topology-preservation.md`
- `references/differential-verification.md`
- `references/high-risk-elements.md`
- `references/deterministic-escalation.md`

For `edit-existing`, create:

- Edit Contract;
- Preservation Ledger;
- Canonical Content Lock;
- Differential Verification record.

Use the templates in `templates/`.

## Minimal regeneration surface

For editing, prefer in this order:

1. original vector/object-level edit;
2. deterministic text/formula/SVG overlay;
3. masked local image edit;
4. bounded local-region regeneration;
5. full-image regeneration only with explicit approval.

Minimize pixels, objects, and semantic elements exposed to regeneration.

## Immutable baseline

Before editing, classify every region/property:

```text
requested change → mutable
not requested → immutable
```

Lock unchanged:

- text;
- Chinese glyphs;
- numbers/units;
- formulas;
- topology;
- grouping;
- hierarchy;
- line wrapping where intentional;
- unaffected color-role bindings;
- unaffected layout/alignment.

Do not reinterpret immutable content for attractiveness, symmetry, visual consistency, or style improvement.

## Canonical content lock

Read `references/canonical-content-lock.md`.

Critical content includes:

- titles;
- labels;
- Chinese characters;
- formulas;
- numbers and units;
- technical abbreviations;
- ordered steps;
- relation endpoints/directions;
- hierarchy;
- intentional line breaks.

Image generation renders this content; it does not author it.

## Formula rule

Read `references/formula-integrity.md`.

A formula is structured data.

Validate:

- variables;
- subscripts;
- superscripts;
- coefficients;
- operators;
- brackets;
- function nesting;
- argument order.

Visual resemblance is insufficient.

Prefer LaTeX/MathJax/KaTeX/SVG or other deterministic formula rendering when exactness is required.

## Graph topology rule

Read `references/topology-preservation.md` and `references/relation-ledger.md`.

Treat as semantic structure:

- arrows;
- arrowheads;
- source/target endpoints;
- connectors;
- solid/dashed style when meaningful;
- containers;
- group boundaries;
- loops;
- branches;
- containment.

A broken border or missing arrowhead is potentially a semantic regression.

## Color roles, blue structural dominance, and bounded accent-context closure

Read:

- `references/semantic-color-policy.md`
- `references/blue-structure-accent-policy.md`
- `references/color-consistency-qa.md`
- `references/visual-context-closure.md`

The existing token system remains authoritative.

Color does not need a fixed global semantic meaning. When a local state/relation color meaning is explicitly declared, keep that mapping consistent within its scope.

The blueprint-blue family is the only default structural color system. Non-blue colors are small, local accents only. Ordinary figures should keep non-blue visual share around 5–8% and normally below 10%.

Do not use non-blue for large card/module fills, complete major module borders, or long primary flow paths unless an explicit exception is approved.

Do not propagate context accent into body text, formulas, annotations, or the entire module structure.

## Output context

Read `references/output-context-profiles.md`.

Default:

```text
output_context = word-embedded-figure
caption_external = true
title_mode = compact
chrome_profile = standard
```

For standard Word figures:

- no complete perimeter frame;
- no four large corner crosshairs;
- no decorative footer;
- no duplicated full internal title when caption is external.

## Composition

Read `references/composition-policy.md`.

Prefer:

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

Cards are justified only when the content has independent anatomy.

## Reference image

Primary reference:

```text
assets/reference-blueprint.png
```

Use it for visual language, not topology/layout copying.

Read `references/reference-image-policy.md`.

When task topology substantially overlaps the reference, use `style-baseline-only`.

## Generation workflow

1. Freeze approved content.
2. Select task mode.
3. Run source/family/semantic gates.
4. Build canonical content locks and relation/message/mapping ledgers.
5. Select output context, composition, reference mode, and rendering method.
6. Generate or edit.
7. Run exact-text/formula/endpoint QA.
8. Run visual-semantic and color-role QA.
9. For edits, run Differential Verification against the source.
10. Reject unauthorized changes.
11. Repair locally; do not restart the full image.
12. Escalate to deterministic rendering when thresholds are met.

## Differential verification — mandatory after edits

Read `references/differential-verification.md`.

For every semantic region record:

```text
intended change
expected preservation
actual change
unauthorized changes
result
```

The central question is:

> **What changed that was not supposed to change?**

not merely:

> Did the requested edit appear?

## High-risk checks

Always inspect:

- Chinese text;
- formulas;
- small typography;
- dense labels;
- dashed borders;
- arrowheads;
- overlapping connectors;
- repeated symbols;
- similar-looking characters;
- long locked single-line headings.

## Anti-regression loop rule

If editing introduces a new defect:

```text
preserve latest correct regions
→ isolate the new defect
→ repair only that defect
→ re-run Differential Verification
```

Do not restart from the original/full image unless explicitly required.

Allow:

- initial local edit;
- at most two local generative repair attempts.

If still unstable, escalate to deterministic rendering.

## Deterministic escalation

Read `references/deterministic-escalation.md`.

Escalate when exact typography, formulas, geometry, alignment, or object-level preservation dominates the task.

Prefer:

- original vector/document edit;
- SVG;
- HTML/CSS;
- diagrams-as-code;
- Figma/PowerPoint/WPS objects;
- deterministic overlay;
- structured layout systems.

Do not hide image-model limitations with repeated full regeneration.

## QA

Read:

- `references/qa-checklist.md`
- `references/visual-semantic-qa.md`
- `references/color-consistency-qa.md`

A document-ready figure requires:

- exact-text PASS;
- formula integrity PASS where applicable;
- endpoint/topology PASS;
- visual-semantic PASS;
- color-role/accent-context PASS;
- Word/WPS readability PASS;
- for edits: zero unauthorized regressions.

## Batch evaluation

For multi-agent/multi-figure validation, read `references/batch-evaluation.md`.

Report `BLOCKED` separately from `REJECT`.

Track:

- exact-text success;
- endpoint success;
- Word-context compliance;
- full-chrome share;
- structural diversity;
- reference-layout-copy rate;
- edit-regression rate when editing tests are included.

## Prompt skeletons

- new generation → `references/prompt-skeleton.md`
- constrained editing → `references/edit-prompt-skeleton.md`

## Human decision boundary

Ask only when:

- source-of-truth conflict changes meaning;
- missing facts block the requested claim;
- user must approve a neutral fallback;
- a repair requires full reconstruction;
- deterministic escalation materially changes the deliverable/workflow.

Otherwise follow the frozen content and this Skill.
