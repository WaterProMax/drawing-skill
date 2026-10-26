# Constrained Edit Prompt Skeleton

```text
TASK MODE
edit-existing

SOURCE ARTIFACT
[exact source file/image/vector]

REQUESTED CHANGES — MUTABLE
- [element/property/change]

IMMUTABLE BASELINE — PRESERVE EXACTLY
- all text not listed as mutable
- all formulas not listed as mutable
- all arrows, endpoints, borders, groups, spacing, alignment, and hierarchy not listed as mutable
- intentional line breaks
- semantic color-role assignments

CANONICAL LOCKS
Exact text:
- [id]: [literal]

Formulas:
- [id]: [canonical LaTeX/token sequence]

Topology:
- preserve relation ledger exactly

WRAP POLICY
- [text id]: locked-single-line | locked-lines | flexible

EDIT METHOD
Use the smallest safe scope:
object edit → deterministic overlay → local masked edit.
Do not regenerate the whole image.

COLOR / CONTEXT POLICY
Use only existing tokens.
Preserve reading-role colors.
Apply context accent only to declared high-salience structural roles.
Do not recolor unrelated elements.

POST-EDIT VERIFICATION
1. verify requested change;
2. ask “what changed that was not supposed to change?”;
3. run exact-text, formula, topology, hierarchy, line-wrap, color-context, and differential checks;
4. reject any unauthorized change.
```
