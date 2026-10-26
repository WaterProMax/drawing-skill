# QA Checklist

## Content and exact text

- [ ] All required elements exist; no invented element.
- [ ] All visible strings match `exact_text`.
- [ ] Numbers, units, dates, and labels are exact.
- [ ] Group membership and abstraction are correct.

## Relation QA

- [ ] Every required relation has correct source, target, direction, and line semantics.
- [ ] Endpoint ledger is traceable without guessing.

## Semantic color QA

- [ ] Every colored element has a semantic role.
- [ ] Same role uses the same strategy across modules.
- [ ] Headings follow heading tokens, not module color.
- [ ] Body/content follows reading tokens, not module color.
- [ ] Formula and annotation colors follow their roles.
- [ ] Icons, borders, and connectors are independently classified.
- [ ] No child inherited color from container/neighbor.
- [ ] Green/orange/red each have genuine state evidence.
- [ ] Exceptions are explicit and local.
- [ ] Only existing tokens are used.
- [ ] Localized edit did not recolor unrelated properties/modules.
- [ ] `color-consistency-qa.md` is complete.

## Visual/style/output

- [ ] Blueprint visual family is preserved.
- [ ] Icon family and line language are consistent.
- [ ] Chrome matches output context.
- [ ] Figure is readable at Word width.

## Decision

- PASS: semantic, color-role, and readability checks pass.
- REVISE: meaning is intact but role mapping or local color isolation is inconsistent.
- REJECT: color implies false meaning/state/relation or an edit altered unrelated semantics.
- BLOCKED: source facts are insufficient or selected generation mode is unsafe.
## Editing preservation QA

- [ ] Task mode was explicitly classified.
- [ ] The real source artifact was available and recorded.
- [ ] Requested changes were declared mutable.
- [ ] Everything else was declared immutable.
- [ ] The smallest safe edit method was used.
- [ ] Exact text and line-wrap locks were preserved.
- [ ] Formula tokens/structure were verified.
- [ ] Topology, arrowheads, borders, groups, and hierarchy were preserved.
- [ ] High-risk elements received explicit checks.
- [ ] Differential verification found no unauthorized change.
- [ ] Visual context closure is consistent for high-salience structural roles.
- [ ] No whole-image regeneration occurred without explicit approval.
- [ ] Repeated generative regressions triggered deterministic escalation.
