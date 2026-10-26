# Fidelity and Preservation Policy

This policy governs constrained editing of existing technical visuals.

## Core law

> Preserve the validated artifact and apply the smallest semantically authorized change.

## 1. Immutable baseline

Before editing, establish a baseline that records:

- source artifact identifier/path;
- dimensions and orientation;
- semantic regions;
- exact visible text;
- formulas;
- numbers/units;
- relations and topology;
- hierarchy;
- intentional line breaks;
- existing color-role assignments;
- high-risk elements.

The baseline must distinguish:

```yaml
mutable:
  - explicitly requested elements/properties
immutable:
  - everything else
```

## 2. Minimal regeneration surface

Use this order:

1. deterministic object-level edit in the source format;
2. deterministic text/vector overlay;
3. localized masked generative edit;
4. localized region reconstruction;
5. full-image regeneration — only with explicit approval.

For every edit, minimize:

- affected pixels;
- affected objects;
- affected semantic regions;
- affected topology;
- affected text.

## 3. Preservation contract

Every edit must declare:

```yaml
edit_scope:
  requested_changes: []
  mutable_regions: []
  mutable_properties: []
  immutable_regions: []
  preserve_exact_text: []
  preserve_formulas: []
  preserve_topology: true
  preserve_hierarchy: true
  preserve_line_wraps: true
  preserve_color_roles: true
```

Any change outside the mutable scope is a regression.

## 4. No aesthetic reinterpretation

Do not change an immutable element for:

- symmetry;
- attractiveness;
- local visual balance;
- consistency with nearby modules;
- cleaner alignment;
- stylistic improvement;
- inferred user intent.

Aesthetic improvement is a separate request.

## 5. Latest-correct-region rule

When an edit fixes one defect but introduces another:

1. preserve the latest correct regions;
2. isolate only the new defect;
3. repair only that defect;
4. repeat differential verification.

Do not return to whole-image regeneration by default.

## 6. Edit-loop stopping rule

Maximum generative attempts for one localized defect:

- initial local edit;
- up to two local repair attempts.

If the same defect or a new regression persists, stop generative editing and escalate to a deterministic method or `BLOCKED`.

## 7. Success criterion

An edit succeeds only when both are true:

```text
requested change = correct
AND
unauthorized changes = none
```

The primary validation question is:

> What changed that was not supposed to change?
