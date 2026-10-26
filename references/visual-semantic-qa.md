# Visual Semantic QA

After generation, compare the image against the approved Content Spec.

Audit:

1. exact text;
2. group membership and containment;
3. peer hierarchy and spatial meaning;
4. connector endpoints and line semantics;
5. color-role and accent-context mapping;
6. explicit state-color consistency when state coloring is actually used;
7. icon semantics;
8. output-context compliance;
9. reference-layout copying.

For color, do not infer that green/orange/red has one universal meaning. Verify instead:

- heading/body/formula/annotation roles use stable reading tokens;
- module identity is separated from reading color;
- equivalent roles match across modules;
- surrounding colors did not propagate;
- local edits did not spill into unrelated styling.

Use `semantic-color-policy.md` and `color-consistency-qa.md`.


Color accents may be visual identity without fixed semantics. Reject only when color explicitly creates a false state, hierarchy, relation, or inconsistent module accent context.
