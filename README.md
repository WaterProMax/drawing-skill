# AICareer Diagram Style Skill v0.7.0

A framework-aware, relation-audited, semantic-color-role-based, **fidelity-constrained generation and editing** Skill for AICareer technical figures.

## v0.7 focus

Generative image models probabilistically reconstruct images. v0.7 treats technical-diagram editing as a preservation and regression-control problem.

It now:

- distinguishes `create-new` from `edit-existing`;
- treats requested changes as mutable and everything else as immutable;
- minimizes regeneration surface;
- locks exact text, formulas, topology, hierarchy, and line wrapping;
- verifies edits by semantic-region differential checks;
- explicitly audits high-risk Chinese text, formulas, borders, arrows, and dense labels;
- prevents “fix A, break B” full-regeneration loops;
- escalates to deterministic vector/document workflows when exactness is required;
- adds high-salience visual-context closure while preserving global reading-color rules.

## Install

Import the ZIP or place the folder at:

```text
.agents/skills/aicareer-diagram-style/
```

Keep `SKILL.md` at the root.

## Editing default

```text
explicitly requested changes = mutable
everything else = preserve
```

A successful edit must include both the requested correction and zero unauthorized regressions.

## Color policy note (v0.7.1)

The Skill uses a strict global reading-color strategy plus declared module accent contexts. Accent colors may be used for visual identity without a universal semantic meaning. If a color is intentionally used as a state/status code, that local meaning must be declared and consistent.


## v0.7.2 color refinement

- Blueprint blue is the only default structural color family.
- Non-blue colors are limited to compact local accents/status markers.
- Large non-blue panels, fills, full module borders, and long primary flows are prohibited by default.
- Ordinary figures target roughly 5–8% non-blue visual share and normally stay below 10%.
- Non-blue accent semantics remain optional and local.
