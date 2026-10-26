# Canonical Content Lock

## Purpose

Build a deterministic representation of critical content before generation/editing.

The image model renders this representation; it does not rewrite it.

## Locked categories

### Exact text

Store exact literal strings for:

- titles;
- Chinese labels;
- technical abbreviations;
- numbers;
- units;
- ordered step labels.

Do not:

- paraphrase;
- shorten;
- translate;
- normalize terminology;
- alter capitalization;
- substitute similar Chinese characters;
- invent missing words.

### Line wrapping

Use:

- `locked-single-line`;
- `locked-lines`;
- `flexible`.

If `locked-single-line`, solve pressure spatially:

- enlarge container;
- redistribute adjacent space;
- simplify non-content decoration;
- increase figure width if allowed.

Do not rewrite or break the label.

### Formula

Store a canonical structured representation, preferably LaTeX or a token sequence.

Example:

```yaml
canonical_latex: "s_{final}(o,s,t^*)=0.5\\times[z(s_{TA}(o,s,t^*))+z(s_{DE}(o,s,t^*))]"
```

### Relations

Lock:

- source;
- target;
- direction;
- line style when meaningful;
- branch label;
- containment owner.

### Hierarchy

Lock:

- global title;
- section/module title;
- card title;
- body;
- annotation;
- emphasized result.

## Validation

Post-render, compare canonical content against visible content character-by-character or token-by-token.

Approximate visual similarity is not acceptance.
