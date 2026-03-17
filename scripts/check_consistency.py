#!/usr/bin/env python3
"""
check_consistency.py
--------------------
Analyses HPSWG-Models TSV files for consistency of inter-model linking nodes.

Phase 1 strategy
----------------
Each formed model should declare:
  1. A '//subgraph Linked Entities' block listing inter-model join nodes.
  2. '//links <node> --> <folder>, <folder>' directives declaring which model(s)
     each linked entity connects to.

The checker:
  A. Validates declared links against target model key entities, using the CRM
     class hierarchy (scripts/crm_hierarchy.json) to resolve subclass relationships.
  B. For undeclared linked entities, suggests possible target models based on
     matching class codes across all model key entities.
  C. Flags formed models missing the Linked Entities subgraph entirely.
  D. Lists verified consistent shared nodes (informational).

Workflow TSVs (models/workflows/) are the canonical label reference.
User workflow TSVs (models/user_workflows/) are excluded entirely.

Output: reports/consistency_report.md
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
REPORTS_DIR = REPO_ROOT / "reports"
REPORT_FILE = REPORTS_DIR / "consistency_report.md"
HIERARCHY_FILE = REPO_ROOT / "scripts" / "crm_hierarchy.json"

EXCLUDED_FOLDERS = {"old_samples", "user_workflows"}
WORKFLOW_FOLDERS = {"workflows"}

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")
SKIP_RE = re.compile(r"^\s*//")
SUBGRAPH_START_RE = re.compile(r"^\s*//subgraph\s+Linked Entities", re.IGNORECASE)
SUBGRAPH_END_RE = re.compile(r"^\s*//end", re.IGNORECASE)
LINKS_RE = re.compile(
    r"^\s*//links\s+(.+?)\s*-->\s*(.+?)\s*(\[confirmed\])?\s*$", re.IGNORECASE
)
INSTANCE_SUFFIX_RE = re.compile(r"#-\d+$")


# ---------------------------------------------------------------------------
# CRM hierarchy helpers
# ---------------------------------------------------------------------------

def load_hierarchy() -> Dict[str, Set[str]]:
    """
    Load crm_hierarchy.json and return a flat dict:
      class_code -> set of all known subclass codes (direct and indirect).
    Returns empty dict if file not found.
    """
    if not HIERARCHY_FILE.exists():
        return {}
    with HIERARCHY_FILE.open(encoding="utf-8") as f:
        raw = json.load(f)
    # Remove the comment key if present
    return {
        k: set(v)
        for k, v in raw.items()
        if not k.startswith("_")
    }


def are_related(code_a: str, code_b: str, hierarchy: Dict[str, Set[str]]) -> bool:
    """
    Return True if code_a and code_b are the same, or one is a subclass of the other.
    """
    if code_a == code_b:
        return True
    # a is subclass of b
    if code_b in hierarchy and code_a in hierarchy[code_b]:
        return True
    # b is subclass of a
    if code_a in hierarchy and code_b in hierarchy[code_a]:
        return True
    return False


# ---------------------------------------------------------------------------
# Node helpers
# ---------------------------------------------------------------------------

def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
    m = VERSION_RE.search(filename)
    if not m:
        return None
    try:
        return tuple(int(p) for p in m.group(1).split("."))
    except ValueError:
        return None


def short_name(path: Path) -> str:
    return f"{path.parent.name}/{path.name}"


def strip_instance_suffix(name: str) -> str:
    return INSTANCE_SUFFIX_RE.sub("", name).strip()


def extract_class_code(name: str) -> Optional[str]:
    parts = name.split(":", 1)
    if len(parts) < 2:
        return None
    candidate = parts[0].strip()
    if re.match(r"^[A-Za-z][A-Za-z0-9_/]*$", candidate):
        return candidate
    return None


def normalise_code(code: str) -> str:
    """Normalise compound codes like S13/E19 -> use first part S13 for hierarchy lookup."""
    return code.split("/")[0].strip()


def parse_targets(raw: str) -> List[str]:
    """
    Parse the target side of a //links directive.
    'person, organisation' or 'person or organisation' -> ['person', 'organisation']
    Ontology references (e.g. 'crm:E31', 'crmsci:S13') are preserved as-is.
    """
    raw = raw.strip()
    parts = re.split(r"\s+or\s+|,\s*", raw, flags=re.IGNORECASE)
    return [p.strip() for p in parts if p.strip()]


def is_ontology_ref(target: str) -> bool:
    """Return True if target is an ontology reference like 'crm:E31' or 'crmsci:S13'."""
    return ":" in target


def ontology_class_code(target: str) -> str:
    """Extract class code from an ontology reference: 'crm:E31' -> 'E31'."""
    return target.split(":", 1)[1].strip()


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class ModelFile:
    def __init__(self, path: Path, folder: str, is_workflow: bool):
        self.path = path
        self.folder = folder
        self.is_workflow = is_workflow
        self.short = short_name(path)


class LinkedEntity:
    def __init__(self, full_name: str):
        self.full_name = full_name          # e.g. 'E39: Project Owner'
        self.class_code = extract_class_code(full_name) or ""
        self.label = full_name.split(":", 1)[1].strip() if ":" in full_name else full_name
        self.declared_targets: List[str] = []   # folder names from //links
        self.confirmed: bool = False            # True if [confirmed] flag present


class ModelAnalysis:
    def __init__(self, model_file: ModelFile):
        self.model_file = model_file
        self.key_entity: Optional[str] = None
        self.key_class_code: Optional[str] = None
        self.linked_entities: List[LinkedEntity] = []
        self.has_linked_block: bool = False


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def latest_tsv_in_folder(folder: Path) -> Optional[Path]:
    versioned = [
        (parse_version(p.name), p)
        for p in folder.glob("*_v*.tsv")
        if parse_version(p.name) is not None
    ]
    if not versioned:
        return None
    versioned.sort(reverse=True, key=lambda vp: vp[0])
    return versioned[0][1]


def discover_model_files() -> List[ModelFile]:
    files: List[ModelFile] = []
    if not MODELS_DIR.exists():
        return files
    for child in sorted(MODELS_DIR.iterdir()):
        if not child.is_dir() or child.name in EXCLUDED_FOLDERS:
            continue
        latest = latest_tsv_in_folder(child)
        if latest is not None:
            files.append(ModelFile(
                path=latest,
                folder=child.name,
                is_workflow=child.name in WORKFLOW_FOLDERS,
            ))
    return files


# ---------------------------------------------------------------------------
# TSV parsing
# ---------------------------------------------------------------------------

def parse_model_file(mf: ModelFile) -> ModelAnalysis:
    ma = ModelAnalysis(mf)
    try:
        lines = mf.path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"Warning: could not read {mf.path}: {e}", file=sys.stderr)
        return ma

    in_linked_block = False
    # Track linked entities by name for //links association
    linked_by_name: Dict[str, LinkedEntity] = {}

    for line in lines:
        # Detect subgraph start
        if SUBGRAPH_START_RE.match(line):
            in_linked_block = True
            ma.has_linked_block = True
            continue

        # Detect subgraph end
        if SUBGRAPH_END_RE.match(line) and in_linked_block:
            in_linked_block = False
            continue

        # Parse //links directives (inside or just after the block)
        links_match = LINKS_RE.match(line)
        if links_match:
            node_name = strip_instance_suffix(links_match.group(1).strip())
            targets = parse_targets(links_match.group(2))
            confirmed = bool(links_match.group(3))
            # Match against known linked entities
            if node_name in linked_by_name:
                linked_by_name[node_name].declared_targets = targets
                linked_by_name[node_name].confirmed = confirmed
            else:
                # Store for later matching (directive may precede node declaration)
                le = LinkedEntity(node_name)
                le.declared_targets = targets
                le.confirmed = confirmed
                linked_by_name[node_name] = le
            continue

        # Skip remaining comment/directive lines
        if SKIP_RE.match(line):
            continue

        parts = line.split("\t")
        if len(parts) < 3:
            continue

        subj_raw = parts[0].strip()
        pred = parts[1].strip().lower()
        if not subj_raw or not pred:
            continue
        # Inside the Linked Entities block, tooltip lines ARE the node declarations.
        # Extract the subject from tooltip lines when inside the block.
        # Outside the block, skip tooltip/metadata lines as usual.
        if pred in ("has note", "from list"):
            continue
        if pred == "tooltip" and not in_linked_block:
            continue

        canonical = strip_instance_suffix(subj_raw)
        code = extract_class_code(canonical)
        if code is None:
            continue

        # Key entity: first subject with a class code seen outside the block
        # (never a tooltip line, since those are skipped outside the block)
        if ma.key_entity is None and not in_linked_block:
            ma.key_entity = canonical
            ma.key_class_code = code

        # Linked entities: subjects inside the block (including tooltip declarations)
        if in_linked_block and canonical not in linked_by_name:
            le = LinkedEntity(canonical)
            linked_by_name[canonical] = le

    # Finalise linked entities list (preserve declaration order)
    ma.linked_entities = list(linked_by_name.values())
    return ma


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyse(
    analyses: List[ModelAnalysis],
    hierarchy: Dict[str, Set[str]],
) -> Dict:
    """
    For each non-workflow model, evaluate each linked entity:
      - If //links declared: check class code relationship to target key entity
      - If //links absent: suggest possible targets from other models' key entities
    """
    # Build lookup: folder_name -> ModelAnalysis
    by_folder: Dict[str, ModelAnalysis] = {
        ma.model_file.folder: ma for ma in analyses
    }

    # Build candidate index for suggestions:
    # class_code -> list of (folder_name, key_entity_label)
    candidates: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for ma in analyses:
        if ma.key_entity and ma.key_class_code:
            norm = normalise_code(ma.key_class_code)
            candidates[norm].append((ma.model_file.folder, ma.key_entity))

    results: List[Dict] = []
    missing_subgraph: List[str] = []

    for ma in analyses:
        if ma.model_file.is_workflow:
            continue

        if not ma.has_linked_block:
            missing_subgraph.append(ma.model_file.short)
            continue

        entity_results: List[Dict] = []

        for le in ma.linked_entities:
            if not le.class_code:
                continue

            norm_code = normalise_code(le.class_code)

            if le.declared_targets:
                # Evaluate each declared target
                target_checks: List[Dict] = []
                for target in le.declared_targets:
                    if is_ontology_ref(target):
                        # Ontology reference -- check class code matches
                        ref_code = normalise_code(ontology_class_code(target))
                        if norm_code == ref_code:
                            status = "ontology_ref"
                        elif are_related(norm_code, ref_code, hierarchy):
                            status = "confirmed_ontology_hierarchy" if le.confirmed else "ontology_hierarchy"
                        else:
                            status = "ontology_mismatch"
                        target_checks.append({
                            "folder": target,
                            "status": status,
                            "target_key": None,
                            "target_code": ref_code,
                            "is_ontology": True,
                        })
                        continue

                    target_ma = by_folder.get(target.lower())
                    if target_ma is None:
                        target_checks.append({
                            "folder": target,
                            "status": "unknown_target",
                            "target_key": None,
                            "target_code": None,
                            "is_ontology": False,
                        })
                        continue

                    target_code = target_ma.key_class_code or ""
                    target_key = target_ma.key_entity or ""
                    norm_target = normalise_code(target_code)

                    if norm_code == norm_target:
                        status = "consistent"
                    elif are_related(norm_code, norm_target, hierarchy):
                        status = "confirmed_hierarchy" if le.confirmed else "hierarchy_match"
                    else:
                        status = "class_mismatch"

                    target_checks.append({
                        "folder": target,
                        "status": status,
                        "target_key": target_key,
                        "target_code": target_code,
                        "is_ontology": False,
                    })

                entity_results.append({
                    "entity": le.full_name,
                    "class_code": le.class_code,
                    "declared": True,
                    "target_checks": target_checks,
                    "suggestions": [],
                })

            else:
                # No declaration -- suggest candidates with matching class code
                suggestions = [
                    (folder, key)
                    for folder, key in candidates.get(norm_code, [])
                    if folder != ma.model_file.folder
                ]
                entity_results.append({
                    "entity": le.full_name,
                    "class_code": le.class_code,
                    "declared": False,
                    "target_checks": [],
                    "suggestions": suggestions,
                })

        results.append({
            "model": ma.model_file.short,
            "entities": entity_results,
        })

    return {
        "model_results": results,
        "missing_subgraph": missing_subgraph,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

STATUS_ICONS = {
    "consistent":                  "✅",
    "confirmed_hierarchy":         "✅",
    "hierarchy_match":             "🔵",
    "class_mismatch":              "⚠️",
    "unknown_target":              "❓",
    "ontology_ref":                "📖",
    "confirmed_ontology_hierarchy":"📖",
    "ontology_hierarchy":          "📖🔵",
    "ontology_mismatch":           "📖⚠️",
}

STATUS_NOTES = {
    "consistent":                  "Consistent",
    "confirmed_hierarchy":         "Consistent (confirmed hierarchy match)",
    "hierarchy_match":             "Hierarchy match -- confirm intent",
    "class_mismatch":              "Class mismatch -- check required",
    "unknown_target":              "Target folder not found in repo",
    "ontology_ref":                "Ontology reference -- follows standard CRM structure",
    "confirmed_ontology_hierarchy":"Ontology reference (confirmed hierarchy match)",
    "ontology_hierarchy":          "Ontology reference via hierarchy -- confirm intent",
    "ontology_mismatch":           "Ontology reference class mismatch -- check required",
}

# Statuses that count as positive for the accordion summary
POSITIVE_STATUSES = {"consistent", "ontology_ref", "confirmed_hierarchy", "confirmed_ontology_hierarchy"}
PARTIAL_STATUSES = {"hierarchy_match", "ontology_hierarchy"}


def md_row(*cells: str) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


def generate_report(result: Dict, files: List[ModelFile]) -> str:
    lines: List[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    individual = [f for f in files if not f.is_workflow]
    workflows = [f for f in files if f.is_workflow]

    lines += [
        "# Model Consistency Report",
        "",
        f"_Generated: {now}_",
        "",
        f"**Individual model files analysed:** {len(individual)}  ",
        f"**Workflow/overview files analysed:** {len(workflows)}  ",
        "",
        "This report checks consistency of inter-model linking nodes declared in "
        "each model's `//subgraph Linked Entities` block. "
        "Only declared linked entities are checked -- high-multiplicity classes "
        "such as E55 type terms are not flagged unless explicitly declared.",
        "",
        "<details>",
        "<summary><strong>Link declaration syntax and status key</strong></summary>",
        "",
        "### Link declaration syntax",
        "",
        "Each linked entity in a model's `//subgraph Linked Entities` block should "
        "have a `//links` directive declaring what it connects to. Two target types "
        "are supported:",
        "",
        "**Repo model targets** -- point to another model folder in this repository:",
        "```",
        "//links E39: Project Owner --> person, organisation",
        "//links E7: Parent Project --> project",
        "```",
        "",
        "**Ontology references** -- follow standard CRM/extension ontology structure "
        "with no bespoke repo model needed:",
        "```",
        "//links E31: Related Documents --> crm:E31",
        "//links E94: Sampling Point --> crmsci:E94",
        "//links D1: Digital Object --> crmdig:D1",
        "```",
        "",
        "Multiple targets are comma-separated or joined with `or`.",
        "",
        "**Confirming intentional hierarchy matches** -- where a linked entity uses a "
        "subclass or superclass of the target model's key entity and this is deliberate, "
        "add `[confirmed]` to suppress the 'confirm intent' flag:",
        "```",
        "//links E39: Group or Artist --> person, organisation [confirmed]",
        "```",
        "",
        "### Status key",
        "",
        "| Icon | Meaning |",
        "|------|---------|",
        "| ✅ | Consistent -- repo model, class codes match exactly |",
        "| ✅ | Consistent (confirmed hierarchy match) |",
        "| 🔵 | Hierarchy match -- repo model, related via CRM hierarchy, confirm intent |",
        "| ⚠️ | Class mismatch -- classes not related, check required |",
        "| ❓ | Unknown target -- declared target folder not found in repo |",
        "| 📖 | Ontology reference -- follows standard CRM/extension ontology structure |",
        "| 📖 | Ontology reference (confirmed hierarchy match) |",
        "| 📖🔵 | Ontology via hierarchy -- related class, confirm intent |",
        "| 📖⚠️ | Ontology mismatch -- class code does not match reference |",
        "| ⚠ | No declaration -- `//links` directive missing, suggestions provided |",
        "",
        "</details>",
        "",
        "---",
        "",
    ]

    # -----------------------------------------------------------------------
    # Section 1: Per-model link validation
    # -----------------------------------------------------------------------
    lines += [
        "## 1. Per-model link validation",
        "",
        "Each model's linked entities are listed with their declared target models "
        "and consistency status. Where no `//links` declaration exists, possible "
        "targets are suggested based on matching class codes.",
        "",
    ]

    model_results = result["model_results"]
    if not model_results:
        lines.append("_No individual models with Linked Entities blocks found._\n")
    else:
        for mr in sorted(model_results, key=lambda x: x["model"]):
            # Compute match summary for accordion header
            all_checks = [
                tc
                for er in mr["entities"]
                for tc in er.get("target_checks", [])
            ]
            declared_count = sum(1 for er in mr["entities"] if er["declared"])
            total_count = len(mr["entities"])
            positive = sum(
                1 for tc in all_checks if tc["status"] in POSITIVE_STATUSES
            )
            partial = sum(
                1 for tc in all_checks if tc["status"] in PARTIAL_STATUSES
            )
            undeclared = total_count - declared_count

            if all_checks:
                summary_parts = []
                if positive:
                    summary_parts.append(f"{positive} confirmed")
                if partial:
                    summary_parts.append(f"{partial} to review")
                if undeclared:
                    summary_parts.append(f"{undeclared} undeclared")
                summary_str = f" -- {', '.join(summary_parts)}" if summary_parts else ""
            else:
                summary_str = f" -- {undeclared} undeclared" if undeclared else ""

            lines += [
                f"<details>",
                f"<summary><strong>{mr['model']}</strong>{summary_str}</summary>",
                "",
                md_row(
                    "Linked entity", "Class code",
                    "Declared target(s)", "Status"
                ),
                md_row("---", "---", "---", "---"),
            ]

            for er in mr["entities"]:
                entity = f"`{er['entity']}`"
                code = f"`{er['class_code']}`"

                if er["declared"]:
                    for tc in er["target_checks"]:
                        icon = STATUS_ICONS.get(tc["status"], "?")
                        note = STATUS_NOTES.get(tc["status"], tc["status"])
                        if tc.get("is_ontology"):
                            target_cell = f"`{tc['folder']}` (ontology)"
                        elif tc["target_key"]:
                            target_cell = f"`{tc['folder']}` → `{tc['target_key']}`"
                        else:
                            target_cell = f"`{tc['folder']}`"
                        lines.append(md_row(
                            entity, code,
                            target_cell,
                            f"{icon} {note}",
                        ))
                        entity = ""  # only show entity name on first row
                        code = ""
                else:
                    if er["suggestions"]:
                        sugg_str = ", ".join(
                            f"`{f}` (`{k}`)" for f, k in er["suggestions"]
                        )
                        lines.append(md_row(
                            entity, code,
                            f"_Suggested: {sugg_str}_",
                            "⚠ No declaration",
                        ))
                    else:
                        lines.append(md_row(
                            entity, code,
                            "_No matching models found_",
                            "⚠ No declaration",
                        ))

            lines += ["", "</details>", ""]

    # -----------------------------------------------------------------------
    # Section 2: Models missing Linked Entities subgraph
    # -----------------------------------------------------------------------
    missing = result["missing_subgraph"]
    lines += [
        "## 2. Models missing Linked Entities subgraph",
        "",
        "These formed model files do not contain a `//subgraph Linked Entities` "
        "block. Add the block to enable consistency checking.",
        "",
    ]
    if not missing:
        lines.append("_All individual models have a Linked Entities subgraph._\n")
    else:
        for sname in sorted(missing):
            lines.append(f"- `{sname}`")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    files = discover_model_files()
    if not files:
        print("No TSV files found. Exiting.")
        sys.exit(0)

    individual = [f for f in files if not f.is_workflow]
    workflows = [f for f in files if f.is_workflow]
    print(
        f"Found {len(individual)} individual model(s) and "
        f"{len(workflows)} workflow file(s). Analysing..."
    )

    hierarchy = load_hierarchy()
    if not hierarchy:
        print(
            "Warning: crm_hierarchy.json not found or empty. "
            "Hierarchy matching will be skipped.",
            file=sys.stderr,
        )

    analyses = [parse_model_file(f) for f in files]
    result = analyse(analyses, hierarchy)
    report = generate_report(result, files)

    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Report written to {REPORT_FILE.relative_to(REPO_ROOT)}")

    n_missing = len(result["missing_subgraph"])
    n_models = len(result["model_results"])
    print(f"  Models checked:               {n_models}")
    print(f"  Missing subgraph:             {n_missing}")


if __name__ == "__main__":
    main()
