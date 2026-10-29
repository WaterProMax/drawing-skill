# Changelog

## 0.8.0

- Renamed the skill to `drawing-skill` and aligned the declared version on `0.8.0` across `SKILL.md`, `README.md`, and this changelog. The previous name `aicareer-diagram-style` remains an alias.
- Positioned the skill as general technical-diagram generation and fidelity-constrained editing. The AICareer Research Engineering Blueprint (`assets/reference-blueprint.png`) is the default visual preset (`visual_preset = aicareer-blueprint`). Projects, courses, and competitions may override the preset without waiving task-mode routing, the source completeness gate, canonical content lock, the immutable baseline, differential verification, or deterministic escalation.
- Consolidated the short routing and gate notes into `references/diagram-routing.md` and `references/generation-gates.md`. Moved the relation ledger into `references/topology-preservation.md` and the semantic-color example into `references/semantic-color-policy.md`. Retired snippet filenames are no longer separate files; their rules are preserved in those consolidated documents.
- Rewrote `README.md` in Chinese with the three-skill suite handoff (`dev-skill`, `writing-skill`, `drawing-skill`) and copy-ready prompts for `create-new`, `edit-existing`, and `deterministic-render`.
- Added `tests/validate_structure.py`, `tests/regression-cases.yaml`, and `tests/README.md` for frontmatter, path, YAML, version, and governance-regression checks.

## 0.7.2

- Added Blue Structural Dominance and Sparse Accent Policy.
- Blueprint blue is now the only default primary structural color family.
- Restricted non-blue colors to small, local accent/status roles.
- Added ordinary non-blue visual-share target of roughly 5–8% and normal upper bound of 10%.
- Prohibited large non-blue card/module fills, full-width bands, complete major module border systems, and long primary non-blue flow paths by default.
- Major connectors and structural boundaries now remain blue unless an explicit exception is approved.
- Replaced module-wide high-salience accent closure with bounded local accent-cluster closure.
- Preserved global reading-color strategy and optional/local state semantics.
- Added QA rejection/revision rules for excessive non-blue area and structural color competition.

## 0.7.1

- Relaxed rigid global semantic color mappings.
- Green/orange/red accent tokens no longer require universal meanings such as positive/change/critical.
- Preserved strict global reading-color roles for headings, body text, formulas, annotations, and metadata.
- Preserved module-level high-salience accent closure for headings, primary icons, borders, local connectors, and badges.
- Added `visual_identity` as a first-class accent reason.
- State/status semantics are now optional and local; when explicitly declared, they must remain consistent within that scope.
- Relation meaning must be readable from topology, direction, line style, and labels rather than color alone.
- Updated cross-module color QA to check consistency and spillover instead of enforcing universal green/orange/red semantics.

## 0.7.0

- Added mandatory Task Mode Router for `create-new`, `edit-existing`, `reconstruct-approved`, and `deterministic-render`.
- Added immutable baseline and explicit mutable-scope rules.
- Added minimal regeneration-surface hierarchy.
- Added Edit Contract and Preservation Ledger.
- Added Canonical Content Lock for exact text, formulas, numbers, ordered steps, hierarchy, and line wrapping.
- Added Formula Integrity Policy and deterministic formula escalation.
- Added Topology Preservation Policy.
- Added Differential Verification by semantic region.
- Added High-Risk Element Registry.
- Added deterministic escalation and hybrid workflow rules.
- Added edit-loop stopping rule: initial local edit plus at most two local repairs.
- Added `locked-single-line`, `locked-lines`, and `flexible` wrap policies.
- Added visual-hierarchy preservation checks.
- Added High-Salience Visual Context Closure for identity headings, icons, borders, and owned local connectors, while keeping body/formula/annotation colors global.
- Added constrained edit prompt and new editing templates.
- Existing design-token values, semantic framework routing, and unrelated visual rules were preserved.

## 0.6.0

- Added mandatory Semantic Color Usage Policy.
- Added role-first token binding and explicit role taxonomy.
- Separated module identity color from reading color.
- Added no-container/no-neighbor color inheritance rule.
- Added fixed default mappings for headings, body text, descriptions, metadata, formulas, annotations, icons, borders, connectors, emphasis, and state.
- Added explicit semantic exception records and precedence rules.
- Added localized edit isolation and preservation requirements.
- Added cross-module role-to-token matrix and Color Consistency QA.
- Added `color-role-ledger.yaml`.
- Updated prompt, content spec, visual QA, feedback, and batch acceptance rules.
- Existing token values and unrelated visual/semantic rules were preserved.
