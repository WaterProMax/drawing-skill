# Diagram Routing, Families, and Framework Experts

Consolidated routing reference for `drawing-skill`. This file is the single source for diagram-type selection, family gates, framework examples, and the C4 / DSRM / CRISP-DM expert notes.

Former standalone notes folded here without dropping their rules: `diagram-type-router.md`, `diagram-types.md`, `family-gates.md`, `framework-routing-examples.md`, `experts/c4-architecture.md`, `experts/crisp-dm-data-mining.md`, `experts/dsrm-research.md`, `experts/dsrm-crispdm-combined.md`.

Use C4 / DSRM / CRISP-DM only when they fit the actual question. Record diagram family, selected framework, scope, confidence, and rejected alternatives.

## Diagram type and framework router

First ask: **What single question must the figure answer?**

Route:

- static software architecture → C4;
- artifact-centered software/information-systems research → DSRM;
- data/ML lifecycle → CRISP-DM;
- DSRM outer lifecycle + CRISP-DM nested workstream when both genuinely apply;
- generic workflow, IA, experiment, mapping, metric, or local process → `none` unless a mature framework fits without distortion.

## Diagram type rules

- Architecture: boundaries, peers, responsibilities, labeled relations.
- Workflow: stages/lanes/decisions; cards only when justified.
- Pipeline/data lineage: layers and transformations.
- Research route: problem → objectives/method → demonstration/evaluation as supported.
- Experiment: dataset, ground truth, compared methods, evaluation, error analysis, findings.
- State: distinct states, decisions, transitions.
- Composite: one dominant panel and supporting panels; avoid dashboard drift.

## Diagram family gates

- Decision flow: every branch needs terminal/next/retry/unresolved semantics; do not invent loops.
- Schema: ownership/scope/containment must be explicit.
- IA: responsibility text, navigation, data flow, and containment are distinct.
- Mapping: explicit adjacent-layer mapping pairs required.
- Comparison: distinguish neutral comparison framework from evidence-backed evaluated comparison.
- Temporal: explicit retained/added/strengthened/weakened/replaced/removed status and replacement pairs.
- Sequence: explicit participants/messages; parallel execution must not become serial chaining.

## Framework routing examples

- Product in environment → C4 system context.
- Applications/services/data stores → C4 container when boundaries are real.
- Main Agent internals → C4 component.
- One request runtime → C4 dynamic / sequence style.
- Overall artifact-centered research → DSRM.
- New-job identification lifecycle → CRISP-DM.
- Local six-step user workflow → none.

## C4 architecture expert

Select one primary zoom level: system context, container, component, code, landscape, dynamic, or deployment.

Do not mix abstraction levels as peers. External elements stay outside the owned boundary. Every relationship needs meaningful interaction semantics.

## CRISP-DM expert

Distinguish business understanding, data understanding, data preparation, modeling, evaluation, and deployment/operationalization.

Preserve real iteration; do not force absent phases or confuse model metrics with complete project validity.

## DSRM research expert

Distinguish problem/motivation, solution objectives, design/development, demonstration, evaluation, and communication.

Do not force a decorative six-box chain or treat implementation as sufficient evaluation. Draw iteration only when the source says what feedback changes.

## DSRM + CRISP-DM combined

Use DSRM as the outer artifact-centered research lifecycle and CRISP-DM only inside the relevant data/ML workstream. Prefer overview and detail figures; do not flatten both into one chain.
