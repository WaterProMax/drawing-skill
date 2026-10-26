# Diagram Content Spec

```yaml
task_mode: create-new
purpose: ""
diagram_type: architecture
diagram_family: ""
selected_framework: none
framework_scope: ""
source_of_truth: []
known_uncertainty: []
abstraction_level: module
orientation: landscape

output_context: word-embedded-figure
caption_external: true
title_mode: compact
chrome_profile: standard
composition_mode: structural-first
reference_mode: style-baseline-only

approved_token_source: visual-baseline.md

emphasis:
  primary: ""
  secondary: []

groups: []

elements:
  - id: element-1
    label: ""
    kind: entity
    role: standard
    group: null
    icon_hint: null
    description: null
    state: default
    identity_group: null

relations:
  - id: r01
    source: element-1
    target: element-2
    relation: flow
    direction: forward
    line_style: solid
    label: null
    semantic: ""

exact_text: []
prohibited_additions: []

color_policy:
  mode: semantic-role-based
  inheritance: prohibited
  role_map: semantic-color-policy.md
  identity_groups: []
  exceptions: []
  local_edit_scope: null

semantic_review:
  ready_to_generate: false
```

## Rules

- Business nouns do not determine color.
- `state` must be supported by the source.
- `identity_group` affects only approved identity-bearing properties.
- Reading roles remain stable across modules.
- Relations and color roles must be explicit enough for QA.
## Edit-existing extension

```yaml
edit_contract: templates/edit-contract.yaml
preservation_ledger: templates/preservation-ledger.yaml
canonical_content_lock: templates/canonical-content-lock.yaml
differential_verification: templates/differential-verification.yaml
accent_context_ledger: templates/accent-context-ledger.yaml
```
