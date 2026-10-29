#!/usr/bin/env python3
"""Static checks for drawing-skill v0.8.0.

Validates SKILL.md frontmatter and size, resolves references/, templates/, and
assets/ paths cited by SKILL.md and README.md, parses template YAML and
tests/regression-cases.yaml, and checks that the current version matches
across SKILL.md, README.md, and CHANGELOG.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.8.0"
SKILL_CHAR_BUDGET = 20_000

PATH_RE = re.compile(
    r"(?:references|templates|assets)/[A-Za-z0-9_./-]+\.(?:md|yaml|yml|png|svg|json)"
)

REMOVED_PATHS = (
    "references/composition-policy.md",
    "references/diagram-type-router.md",
    "references/diagram-types.md",
    "references/example.md",
    "references/family-gates.md",
    "references/framework-routing-examples.md",
    "references/output-context-profiles.md",
    "references/reference-image-policy.md",
    "references/relation-ledger.md",
    "references/semantic-review-gate.md",
    "references/sequence-reliability.md",
    "references/source-completeness-gate.md",
    "references/experts/c4-architecture.md",
    "references/experts/crisp-dm-data-mining.md",
    "references/experts/dsrm-crispdm-combined.md",
    "references/experts/dsrm-research.md",
)

TEMPLATE_REQUIRED_KEYS: dict[str, tuple[str, ...]] = {
    "accent-context-ledger.yaml": ("accent_contexts",),
    "canonical-content-lock.yaml": ("text_items", "formulas", "ordered_steps", "hierarchy"),
    "color-role-ledger.yaml": (
        "approved_token_source",
        "inheritance",
        "role_defaults",
        "identity_groups",
        "exceptions",
        "accent_contexts",
    ),
    "diagram-content-spec.yaml": (
        "task_mode",
        "purpose",
        "diagram_type",
        "diagram_family",
        "selected_framework",
        "output_context",
        "caption_external",
        "title_mode",
        "chrome_profile",
        "composition_mode",
        "reference_mode",
        "relations",
        "exact_text",
        "semantic_review",
    ),
    "differential-verification.yaml": (
        "regions",
        "requested_change_result",
        "immutable_region_result",
        "high_risk_result",
        "topology_result",
        "formula_result",
        "final_decision",
    ),
    "edit-contract.yaml": (
        "task_mode",
        "source_artifact",
        "requested_changes",
        "mutable",
        "immutable",
        "edit_method",
        "attempt_policy",
    ),
    "family-preflight.yaml": (
        "diagram_family",
        "source_completeness",
        "family_gate",
        "reference_mode",
    ),
    "framework-mapping.yaml": (
        "selected_framework",
        "framework_scope",
        "source_mapping",
        "omitted_or_out_of_scope",
        "deviations",
        "unresolved",
    ),
    "preservation-ledger.yaml": ("baseline", "regions"),
    "relation-ledger.yaml": ("relations", "endpoint_ledger"),
}

REQUIRED_CASE_IDS = (
    "create_new_missing_source_facts",
    "edit_existing_local_text_fix",
    "formula_distortion_escalates_deterministic",
    "non_blue_share_color_qa",
    "word_embedded_figure_chrome",
)

TASK_MODES = {
    "create-new",
    "edit-existing",
    "reconstruct-approved",
    "deterministic-render",
}
STATUSES = {"PASS", "REVISE", "REJECT", "BLOCKED"}

PRESERVED_SNIPPETS: dict[str, tuple[str, ...]] = {
    "references/diagram-routing.md": (
        "What single question must the figure answer?",
        "static software architecture → C4",
        "generic workflow, IA, experiment, mapping, metric, or local process → `none`",
        "Architecture: boundaries, peers, responsibilities, labeled relations.",
        "Composite: one dominant panel and supporting panels; avoid dashboard drift.",
        "Decision flow: every branch needs terminal/next/retry/unresolved semantics; do not invent loops.",
        "parallel execution must not become serial chaining.",
        "Product in environment → C4 system context.",
        "Local six-step user workflow → none.",
        "Select one primary zoom level: system context, container, component, code, landscape, dynamic, or deployment.",
        "Do not mix abstraction levels as peers.",
        "Distinguish business understanding, data understanding, data preparation, modeling, evaluation, and deployment/operationalization.",
        "Preserve real iteration; do not force absent phases",
        "confuse model metrics with complete project validity.",
        "Distinguish problem/motivation, solution objectives, design/development, demonstration, evaluation, and communication.",
        "Do not force a decorative six-box chain",
        "Draw iteration only when the source says what feedback changes.",
        "Use DSRM as the outer artifact-centered research lifecycle",
        "do not flatten both into one chain.",
    ),
    "references/generation-gates.md": (
        "`READY` — enough facts exist.",
        "`READY_NEUTRAL` — only neutral structure is supported.",
        "`BLOCKED` — requested semantics would require invention.",
        "Require explicit evidence for mappings, evaluated comparisons, temporal classifications, branch destinations, and sequence endpoints.",
        "Output `Ready to Generate: YES/NO`.",
        "Stop on meaning-changing uncertainty.",
        "two passes: structural review, then consistency review.",
        "Cards are justified only when an item has independent internal anatomy",
        "The reference controls visual language, not universal layout.",
        "output_context: word-embedded-figure",
        "caption_external: true",
        "title_mode: compact",
        "chrome_profile: standard",
        "no complete perimeter frame",
        "no more than roughly 20%",
        "Choose `full-reference` or `style-baseline-only`.",
        "Use `style-baseline-only` when the task topology overlaps the reference",
        "Never copy central-hub layout, panel arrangement, footer, full chrome, or card grammar",
        "participants <= 6, messages <= 8",
        "apply AICareer visual styling without letting the image model redraw message geometry.",
        "If unavailable, split/simplify or return BLOCKED.",
    ),
    "references/topology-preservation.md": (
        "preserve_topology: true",
        "Reject ambiguous shared rails.",
        "After generation record visible source, target, arrowhead endpoint, line style, and traceability.",
        "line_style: solid",
    ),
    "references/semantic-color-policy.md": (
        "id: human-review",
        "state: positive",
        "identity_group: human-feedback",
        "The green border/icon/connector does not recolor the heading or body text.",
        "heading_text: text.strong",
        "feedback_connector: semantic.positive",
    ),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_yaml(path: Path) -> object:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid YAML: {exc}")
    if loaded is None:
        fail(f"{path.relative_to(ROOT)} is empty")
    return loaded


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        fail("SKILL.md is missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter is not closed")
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        fail(f"SKILL.md frontmatter is not valid YAML: {exc}")
    if not isinstance(data, dict):
        fail("SKILL.md frontmatter must be a mapping")
    return data


def check_frontmatter(skill_text: str) -> None:
    meta = parse_frontmatter(skill_text)
    if meta.get("name") != "drawing-skill":
        fail(f"SKILL.md name must be drawing-skill, got {meta.get('name')!r}")
    description = meta.get("description")
    if not isinstance(description, str) or "aicareer-diagram-style" not in description:
        fail("SKILL.md description must mention the aicareer-diagram-style alias")
    if "aicareer-blueprint" not in description:
        fail("SKILL.md description must name the aicareer-blueprint preset")
    nested = meta.get("metadata")
    if not isinstance(nested, dict):
        fail("SKILL.md metadata mapping is missing")
    if str(nested.get("version")) != VERSION:
        fail(f"SKILL.md metadata.version must be {VERSION}, got {nested.get('version')!r}")
    if nested.get("visual_preset") != "aicareer-blueprint":
        fail("SKILL.md metadata.visual_preset must be aicareer-blueprint")
    if nested.get("alias") != "aicareer-diagram-style":
        fail("SKILL.md metadata.alias must be aicareer-diagram-style")
    if len(skill_text) > SKILL_CHAR_BUDGET:
        fail(f"SKILL.md is {len(skill_text)} characters; budget is {SKILL_CHAR_BUDGET}")

    for mode in TASK_MODES:
        if mode not in skill_text:
            fail(f"SKILL.md is missing task mode {mode}")
    for status in STATUSES:
        if status not in skill_text:
            fail(f"SKILL.md is missing status {status}")
    for token in (
        "visual_preset = aicareer-blueprint",
        "assets/reference-blueprint.png",
        "references/diagram-routing.md",
        "references/generation-gates.md",
        "5–8%",
        "Edit Contract",
        "Differential Verification",
    ):
        if token not in skill_text:
            fail(f"SKILL.md is missing required token: {token}")


def check_versions(skill_text: str, readme_text: str, changelog_text: str) -> None:
    frontmatter = parse_frontmatter(skill_text)
    skill_version = str(frontmatter["metadata"]["version"])
    if skill_version != VERSION:
        fail(f"SKILL.md version {skill_version} != {VERSION}")

    title = readme_text.splitlines()[0]
    if f"v{VERSION}" not in title:
        fail(f"README.md title must declare v{VERSION}: {title}")

    headings = re.findall(r"^## (\d+\.\d+\.\d+)\s*$", changelog_text, flags=re.MULTILINE)
    if not headings:
        fail("CHANGELOG.md has no ## version headings")
    if headings[0] != VERSION:
        fail(f"CHANGELOG.md latest version is {headings[0]}, expected {VERSION}")
    if skill_version != headings[0]:
        fail("SKILL.md version and CHANGELOG.md latest version differ")
    print(f"PASS: version {VERSION} is consistent across SKILL.md, README.md, and CHANGELOG.md")


def check_cited_paths(documents: dict[str, str]) -> None:
    missing: list[str] = []
    seen: set[str] = set()
    for name, text in documents.items():
        for match in PATH_RE.findall(text):
            seen.add(match)
            if not (ROOT / match).is_file():
                missing.append(f"{name} -> {match}")
    if missing:
        fail("missing cited paths:\n  " + "\n  ".join(missing))
    if not seen:
        fail("no references/, templates/, or assets/ paths were found to check")
    print(f"PASS: {len(seen)} cited references/templates/assets paths exist")


def check_removed_snippets(skill_text: str, readme_text: str) -> None:
    for relative in REMOVED_PATHS:
        if (ROOT / relative).exists():
            fail(f"retired snippet still exists: {relative}")
        for label, text in (("SKILL.md", skill_text), ("README.md", readme_text)):
            if relative in text:
                fail(f"{label} still links to retired path {relative}")
    if (ROOT / "references" / "experts").exists():
        fail("references/experts/ should be removed after consolidation")
    print("PASS: retired snippet files are gone and unlinked")


def check_preserved_rules() -> None:
    for relative, snippets in PRESERVED_SNIPPETS.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        missing = [snippet for snippet in snippets if snippet not in text]
        if missing:
            fail(f"{relative} dropped consolidated rules:\n  " + "\n  ".join(missing))
    print("PASS: consolidated references still contain the retired snippet rules")


def check_templates() -> None:
    template_dir = ROOT / "templates"
    found = sorted(path.name for path in template_dir.glob("*.yaml"))
    expected = sorted(TEMPLATE_REQUIRED_KEYS)
    if found != expected:
        fail(
            "template set mismatch: "
            f"missing={sorted(set(expected) - set(found))}, "
            f"extra={sorted(set(found) - set(expected))}"
        )
    for name, keys in TEMPLATE_REQUIRED_KEYS.items():
        loaded = load_yaml(template_dir / name)
        if not isinstance(loaded, dict):
            fail(f"templates/{name} must be a mapping")
        for key in keys:
            if key not in loaded:
                fail(f"templates/{name} is missing required key {key}")
    edit = load_yaml(template_dir / "edit-contract.yaml")
    assert isinstance(edit, dict)
    attempt = edit.get("attempt_policy")
    method = edit.get("edit_method")
    if not isinstance(attempt, dict) or attempt.get("max_local_repairs") != 2:
        fail("edit-contract.yaml attempt_policy.max_local_repairs must be 2")
    if not isinstance(method, dict) or method.get("full_regeneration_allowed") is not False:
        fail("edit-contract.yaml must forbid full regeneration by default")
    print(f"PASS: {len(found)} template YAML files parse and contain required keys")


def check_regression_cases() -> None:
    path = ROOT / "tests" / "regression-cases.yaml"
    loaded = load_yaml(path)
    if not isinstance(loaded, dict):
        fail("tests/regression-cases.yaml must be a mapping")
    if loaded.get("version") != 1:
        fail("regression-cases.yaml version must be 1")
    if loaded.get("skill_version") != VERSION:
        fail(f"regression-cases.yaml skill_version must be {VERSION}")
    purpose = loaded.get("purpose")
    if not isinstance(purpose, str) or len(purpose.strip()) < 20:
        fail("regression-cases.yaml purpose must be a descriptive string")
    cases = loaded.get("cases")
    if not isinstance(cases, list) or len(cases) < len(REQUIRED_CASE_IDS):
        fail("regression-cases.yaml cases must cover the required governance scenarios")

    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(f"case #{index} is not a mapping")
        cid = case.get("id")
        if not isinstance(cid, str) or len(cid) < 8:
            fail(f"case #{index} needs a stable id")
        if cid in seen:
            fail(f"duplicate regression case id {cid}")
        seen.add(cid)
        name = case.get("name")
        if not isinstance(name, str) or len(name.strip()) < 8:
            fail(f"case {cid} needs a name")
        mode = case.get("task_mode")
        if mode not in TASK_MODES:
            fail(f"case {cid} has invalid task_mode {mode!r}")
        text = case.get("input")
        if not isinstance(text, str) or len(text.strip()) < 20:
            fail(f"case {cid} input is missing or too short")
        expected = case.get("expected")
        if not isinstance(expected, dict):
            fail(f"case {cid} expected must be a mapping")
        status = expected.get("status")
        if status not in STATUSES:
            fail(f"case {cid} expected.status {status!r} is not PASS/REVISE/REJECT/BLOCKED")
        action = expected.get("required_action")
        if not isinstance(action, str) or len(action.strip()) < 20:
            fail(f"case {cid} expected.required_action is missing or too short")
        forbidden = expected.get("forbidden_actions")
        if not isinstance(forbidden, list) or len(forbidden) < 2:
            fail(f"case {cid} expected.forbidden_actions needs at least two items")
        for item in forbidden:
            if not isinstance(item, str) or len(item.strip()) < 10:
                fail(f"case {cid} has a forbidden action that is too short: {item!r}")
        nxt = expected.get("next_task_mode")
        if nxt is not None and nxt not in TASK_MODES:
            fail(f"case {cid} next_task_mode {nxt!r} is invalid")

    missing_ids = [cid for cid in REQUIRED_CASE_IDS if cid not in seen]
    if missing_ids:
        fail(f"regression cases missing required ids: {missing_ids}")

    by_id = {case["id"]: case for case in cases if isinstance(case, dict)}
    blocked = by_id["create_new_missing_source_facts"]["expected"]["status"]
    if blocked != "BLOCKED":
        fail("create-new with missing source facts must expect BLOCKED")
    edit = by_id["edit_existing_local_text_fix"]["expected"]["required_action"]
    for artifact in ("Edit Contract", "Preservation Ledger", "Differential Verification"):
        if artifact not in edit:
            fail(f"local text-fix case must require {artifact}")
    if "full" not in edit.lower() and "regenerat" not in edit.lower():
        fail("local text-fix case must forbid full regeneration")
    formula = by_id["formula_distortion_escalates_deterministic"]["expected"]
    if formula.get("next_task_mode") != "deterministic-render":
        fail("formula distortion must escalate to deterministic-render")
    if formula.get("status") != "REJECT":
        fail("distorted formula must be REJECT before escalation")
    color = by_id["non_blue_share_color_qa"]["expected"]
    if color.get("status") != "REJECT":
        fail("excess non-blue share must be REJECT")
    word = by_id["word_embedded_figure_chrome"]["expected"]
    if word.get("status") != "REJECT":
        fail("Word figure with an outer frame and duplicate title must be REJECT")
    print(f"PASS: {len(cases)} regression cases parse and cover the governance scenarios")


def check_readme_suite(readme_text: str) -> None:
    required = (
        "团队 AI 协作三件套",
        "dev-skill",
        "writing-skill",
        "drawing-skill",
        "场景 A",
        "场景 B",
        "场景 C",
        "create-new",
        "edit-existing",
        "deterministic-render",
        "python3 tests/validate_structure.py",
        "5–8%",
        "160 mm",
    )
    missing = [item for item in required if item not in readme_text]
    if missing:
        fail(f"README.md is missing suite or template markers: {missing}")
    print("PASS: README.md carries the suite context and prompt templates")


def main() -> None:
    skill_path = ROOT / "SKILL.md"
    readme_path = ROOT / "README.md"
    changelog_path = ROOT / "CHANGELOG.md"
    for path in (skill_path, readme_path, changelog_path):
        if not path.is_file():
            fail(f"missing {path.name}")
    if not (ROOT / "assets" / "reference-blueprint.png").is_file():
        fail("assets/reference-blueprint.png is missing")

    skill_text = skill_path.read_text(encoding="utf-8")
    readme_text = readme_path.read_text(encoding="utf-8")
    changelog_text = changelog_path.read_text(encoding="utf-8")

    check_frontmatter(skill_text)
    print(f"PASS: SKILL.md frontmatter and budget ({len(skill_text)}/{SKILL_CHAR_BUDGET} characters)")
    check_versions(skill_text, readme_text, changelog_text)
    check_cited_paths({"SKILL.md": skill_text, "README.md": readme_text})
    check_removed_snippets(skill_text, readme_text)
    check_preserved_rules()
    check_templates()
    check_regression_cases()
    check_readme_suite(readme_text)
    print("PASS: drawing-skill structure is valid")


if __name__ == "__main__":
    sys.exit(main())
