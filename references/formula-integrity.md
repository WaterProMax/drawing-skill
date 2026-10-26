# Formula Integrity Policy

Formulas are structured technical data, not visual decoration.

## Canonical representation

For each formula, store at least one authoritative representation:

- canonical LaTeX;
- MathML;
- a verified token sequence;
- source equation text.

Prefer two representations for high-risk equations.

## Verification dimensions

Verify exactly:

- variable names;
- subscripts;
- superscripts;
- coefficients;
- operators;
- brackets;
- function nesting;
- argument order;
- punctuation;
- equality/inequality signs.

A formula that merely looks similar is incorrect.

## Rendering policy

Use deterministic formula rendering whenever formula correctness matters.

Preferred:

1. LaTeX/MathJax/KaTeX/SVG rendering;
2. vector/text overlay;
3. object-level edit in Figma/PowerPoint/document drawing tool.

Pure generative rendering is allowed only for non-authoritative decorative formula fragments.

## Edit rule

When the request changes one formula:

- replace only that formula region;
- preserve all surrounding labels, borders, arrows, spacing, and formulas;
- compare the rendered result with the canonical representation.

## Decision

- exact semantic/syntactic match → `PASS`;
- visually similar but token mismatch → `REJECT`;
- deterministic formula rendering unavailable for an authoritative formula → `BLOCKED` or escalate.
