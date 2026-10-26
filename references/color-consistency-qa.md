# Cross-Module Color Role and Accent QA

Run after every generated figure and every color edit.

## 1. Role inventory

List all visible colored elements and classify each:

```text
module identity
heading
body text
secondary description
metadata
icon
border
connector
formula
annotation
emphasis
state
```

No unclassified colored element may pass.

## 2. Role-to-token matrix

Build a matrix:

| Role | Module A | Module B | Module C | Expected strategy | Result |
|---|---|---|---|---|---|
| card heading | text.strong | text.strong | text.strong | same | PASS |
| body text | text.primary | text.primary | semantic.change | same | FAIL |

Equivalent roles must follow the same strategy.

## 3. Reading/identity separation

Check:

- body text did not inherit module identity;
- headings did not inherit state color unless the heading itself is a state label;
- formulas/annotations did not inherit card border color;
- long-form readable content uses text tokens.

## 4. No-neighbor inference

Check whether any element was recolored merely because it sits inside or beside a colored object.

Examples of failure:

- orange border causes all body text to become orange;
- green icon causes the formula to become green;
- a neighboring module causes an unrelated connector to inherit its accent.

## 5. Accent-context audit

For every declared non-blue accent:

- verify it is local and compact;
- verify it does not replace the blueprint-blue structural backbone;
- verify reading roles did not inherit the accent;
- verify main module borders and major connectors remain blue by default;
- verify the accent token comes from the existing token set;
- verify total non-blue visual share remains sparse.

Do **not** require green/orange/red to prove a fixed global semantic state.

If the color is explicitly used as a state/status code, verify only that the declared local state meaning is consistent within its scope.

## 6. Exception audit

Every deviation must have:

- element;
- property;
- token;
- semantic reason;
- local scope.

Missing reason => REVISE or REJECT when meaning changes.

## 7. Local edit isolation

Compare before/after or target/preserve declarations.

Fail when a localized edit changes:

- unrelated text roles;
- icons;
- borders;
- formulas;
- connectors;
- other modules.

## 8. Token-source audit

Fail if any color:

- is not in the existing token set;
- is approximated from a screenshot;
- is created by opacity/blending without an approved token rule;
- is independently lightened/darkened;
- is named only by raw hex in the prompt when a token exists.

## 9. Blue structural dominance

Fail or revise when:

- a large card/panel/module uses non-blue fill without explicit permission;
- a complete major module border becomes non-blue;
- a long or central flow becomes non-blue;
- non-blue color visually competes with the blueprint-blue family;
- non-blue accents spread beyond approximately 10% of visual share without an approved exception.

Target ordinary figures at roughly 5–8% non-blue visual share.

## 10. Bounded accent context closure

For each compact accent cluster, compare only its intended accent-bearing roles:

- status dot/badge;
- small icon accent;
- narrow indicator strip;
- short local label;
- short local status connector.

Require one coherent accent strategy inside that compact cluster.

Do not expand the accent to the whole module merely for visual closure.

## Decision

- `PASS`: blue remains structurally dominant; non-blue accents are sparse/local; reading colors and token rules are consistent.
- `REVISE`: meaning intact but non-blue usage is too broad or a local role mapping is inconsistent.
- `REJECT`: color changes/falsely implies technical hierarchy/state/relation, a large non-blue region becomes a competing structural system, or a local edit changes unrelated locked styling.
- Do not reject a valid accent solely because green/orange/red does not match a universal predefined meaning.
