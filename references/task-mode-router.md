# Task Mode Router — Generation vs Editing

Determine the operation mode before any prompt, generation, or edit.

## Modes

```yaml
task_mode: create-new | edit-existing | reconstruct-approved | deterministic-render
```

## `create-new`

Use when no source artifact is being modified.

The normal semantic, framework, relation, color, composition, and QA pipeline applies.

## `edit-existing`

Use when the user asks to change, fix, replace, correct, recolor, relabel, retouch, repair, or adjust an existing artifact.

Required priority:

```text
preservation > semantic correctness > readability > requested local change > visual creativity
```

Hard rule:

> Explicitly requested changes are mutable. Everything else is immutable by default.

Do not reinterpret the request as permission to redesign, restyle, rebalance, simplify, or regenerate the whole figure.

If the source artifact is missing or unusable, return `BLOCKED` and request the actual source image/vector/document.

## `reconstruct-approved`

Use only when:

- the original is not editable;
- a local edit cannot be performed safely;
- the user explicitly approves reconstruction;
- the Skill explains that reconstruction is not object-preserving editing.

Reconstruction creates a new artifact from a validated canonical specification. It does not claim pixel/object preservation.

## `deterministic-render`

Use when exactness dominates synthesis, including:

- formulas;
- dense Chinese labels;
- strict topology;
- precise alignment;
- object-level preservation;
- complex sequence diagrams;
- repeated edits to the same technical figure.

See `deterministic-escalation.md`.

## Mode-switch prohibition

Do not silently switch:

```text
edit-existing → create-new
```

or:

```text
edit-existing → reconstruct-approved
```

A mode switch requires explicit user approval.

## Visual preset is not a mode switch

`visual_preset` defaults to `aicareer-blueprint`. Changing or overriding the visual preset does not switch task mode and does not relax preservation, completeness, or escalation rules.
