#!/usr/bin/env python3
"""
check_consistency.py
--------------------
Analyses all TSV model files in the HPSWG-Models repository and produces a
consistency report at reports/consistency_report.md.

What it checks
--------------
1. Node inventory: every distinct node name, which models use it, how many times.
2. Predicate-scoped variant detection: where the same CRM/CRMsci property
   connects nodes with the same class-code prefix but different labels across
   models. These are genuine candidates for inter-model join breaks.
3. Cross-model shared nodes: nodes (exact name) that appear in more than one
   model -- the intended linking points between models.
4. Workflow/overview vs individual model discrepancies: highlights cases where
   the workflow TSVs (the closest thing to a canonical reference) use a
   different label than individual models for what appears to be the same concept.

Usage
-----
  python scripts/check_consistency.py

RAW_BASE environment variable is not required for this script.
Output is written to reports/consistency_report.md (created if absent).
"""

import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
REPORTS_DIR = REPO_ROOT / "reports"
REPORT_FILE = REPORTS_DIR / "consistency_report.md"

EXCLUDED_FOLDERS = {"old_samples", "user_workflows"}
WORKFLOW_FOLDERS = {"workflows"}

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class Triple(NamedTuple):
    subject: str          # canonical (stripped of #-N suffix and format class)
    predicate: str
    obj: str              # canonical
    subject_raw: str      # as it appears in the file
    obj_raw: str
    source_file: Path


class ModelFile(NamedTuple):
    path: Path
    folder: str           # parent folder name
    is_workflow: bool


# ---------------------------------------------------------------------------
# TSV parsing
# ---------------------------------------------------------------------------

# Matches CRM/CRMsci class code prefix: E22, S13, EX_Digital_Image, etc.
CLASS_CODE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_/]*(?::[A-Za-z0-9_/]*)?):\s*")

# Strip trailing #-N instance suffixes (e.g. #-1, #-2)
INSTANCE_SUFFIX_RE = re.compile(r"#-\d+$")

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")


def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
    """Extract version tuple from a filename like 'model_v1.2.tsv' -> (1, 2)."""
    m = VERSION_RE.search(filename)
    if not m:
        return None
    try:
        return tuple(int(p) for p in m.group(1).split("."))
    except ValueError:
        return None

# Lines to skip: directives, comments, subgraph markers
SKIP_RE = re.compile(r"^\s*//")

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")


def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
    """Extract version tuple from a filename like 'sample_model_v1.2.tsv' -> (1, 2)."""
    m = VERSION_RE.search(filename)
    if not m:
        return None
    try:
        return tuple(int(p) for p in m.group(1).split("."))
    except ValueError:
        return None


def strip_instance_suffix(name: str) -> str:
    return INSTANCE_SUFFIX_RE.sub("", name).strip()


def extract_class_code(name: str) -> Optional[str]:
    """
    Extract the CRM class code prefix from a node name.
    'E22: Painting' -> 'E22'
    'S13/E19: Sample' -> 'S13/E19'
    'EX_Digital_Image: Foo' -> 'EX_Digital_Image'
    Returns None if no recognisable prefix.
    """
    # Split on first colon
    parts = name.split(":", 1)
    if len(parts) < 2:
        return None
    candidate = parts[0].strip()
    # Must look like a CRM code: letters/digits/underscores/slashes
    if re.match(r"^[A-Za-z][A-Za-z0-9_/]*$", candidate):
        return candidate
    return None


def parse_node(raw: str) -> str:
    """
    Strip format class from a node value (e.g. 'object-fs32' suffix from Format col
    is not present in Subject/Object cols -- but clean whitespace and instance suffixes).
    """
    return strip_instance_suffix(raw.strip())


def parse_tsv_file(path: Path) -> List[Triple]:
    """
    Parse a TSV file and return a list of Triple objects.
    Skips directive lines, comment lines, and lines with fewer than 3 columns.
    """
    triples: List[Triple] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: could not read {path}: {e}", file=sys.stderr)
        return triples

    for line in text.splitlines():
        # Skip comments and directives
        if SKIP_RE.match(line):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        subj_raw = parts[0].strip()
        pred = parts[1].strip()
        obj_raw = parts[2].strip()

        if not subj_raw or not pred or not obj_raw:
            continue

        # Skip tooltip lines -- these are metadata, not structural triples
        if pred.lower() == "tooltip":
            continue
        if pred.lower() == "has note":
            continue

        subj = parse_node(subj_raw)
        obj = parse_node(obj_raw)

        triples.append(Triple(
            subject=subj,
            predicate=pred,
            obj=obj,
            subject_raw=subj_raw,
            obj_raw=obj_raw,
            source_file=path,
        ))

    return triples


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def latest_tsv_in_folder(folder: Path) -> Optional[Path]:
    """
    Return the highest-versioned *_v*.tsv file in a folder, or None if absent.
    Uses the same version-tuple logic as update_readmes.py.
    """
    versioned = []
    for tsv in folder.glob("*_v*.tsv"):
        v = parse_version(tsv.name)
        if v is not None:
            versioned.append((v, tsv))
    if not versioned:
        return None
    versioned.sort(reverse=True, key=lambda vp: vp[0])
    return versioned[0][1]


def discover_model_files() -> List[ModelFile]:
    """
    Find the latest versioned TSV file in each model folder under models/.
    Only the newest version of each model is included -- older versions are
    not expected to be consistent and would generate noise.
    Workflow files follow the same rule: only the latest version is included.
    """
    files: List[ModelFile] = []
    if not MODELS_DIR.exists():
        return files

    for child in sorted(MODELS_DIR.iterdir()):
        if not child.is_dir():
            continue
        if child.name in EXCLUDED_FOLDERS:
            continue
        is_workflow = child.name in WORKFLOW_FOLDERS
        latest = latest_tsv_in_folder(child)
        if latest is not None:
            files.append(ModelFile(
                path=latest,
                folder=child.name,
                is_workflow=is_workflow,
            ))

    return files


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def short_name(path: Path) -> str:
    """Return a readable short name: folder/filename."""
    return f"{path.parent.name}/{path.name}"


def analyse(files: List[ModelFile]) -> Dict:
    """
    Build the full analysis structure from all parsed triples.
    Returns a dict with keys:
      node_index        -- node_name -> set of short file names
      predicate_variants -- predicate -> class_code -> {label -> set of files}
      shared_nodes      -- node names in more than one model (non-workflow)
      workflow_labels   -- {(predicate, class_code) -> set of labels} from workflow files
      individual_labels -- {(predicate, class_code) -> {label -> set of files}} from non-workflow
    """
    # node name (canonical) -> set of short file names
    node_index: Dict[str, Set[str]] = defaultdict(set)

    # (predicate, class_code) -> {label -> set of short file names}
    # built separately for workflow and individual models
    workflow_labels: Dict[Tuple[str, str], Set[str]] = defaultdict(set)
    individual_labels: Dict[Tuple[str, str], Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))

    for mf in files:
        triples = parse_tsv_file(mf.path)
        sname = short_name(mf.path)

        for t in triples:
            for node in (t.subject, t.obj):
                node_index[node].add(sname)

            # For each node in the triple, index (predicate, class_code) -> label
            for node in (t.subject, t.obj):
                code = extract_class_code(node)
                if code is None:
                    continue
                # label is everything after "CODE: "
                label_parts = node.split(":", 1)
                label = label_parts[1].strip() if len(label_parts) > 1 else node

                key = (t.predicate, code)
                if mf.is_workflow:
                    workflow_labels[key].add(label)
                else:
                    individual_labels[key][label].add(sname)

    # Shared nodes: appear in more than one file (across any combination)
    shared_nodes = {
        node: files_set
        for node, files_set in node_index.items()
        if len(files_set) > 1
    }

    # Predicate-scoped variants: for each (predicate, class_code),
    # collect all labels seen across individual models
    # Flag where more than one distinct label exists
    predicate_variants: Dict[Tuple[str, str], Dict[str, Set[str]]] = {}
    for key, label_map in individual_labels.items():
        if len(label_map) > 1:
            predicate_variants[key] = dict(label_map)

    # Workflow vs individual discrepancies:
    # Build a model-centric index: for each individual model file, collect the
    # changes it needs to make to align with the workflow canonical labels.
    # Structure: {short_file_name -> [{predicate, class_code, current_label, canonical_labels}]}
    model_centric: Dict[str, List[Dict]] = defaultdict(list)

    for key, wf_labels in workflow_labels.items():
        ind = individual_labels.get(key)
        if not ind:
            continue
        ind_labels = set(ind.keys())
        only_in_individual = ind_labels - wf_labels
        if not only_in_individual:
            continue
        # For each non-canonical label, record which files use it
        for label in sorted(only_in_individual):
            for sname in sorted(ind[label]):
                model_centric[sname].append({
                    "predicate": key[0],
                    "class_code": key[1],
                    "current_label": label,
                    "canonical_labels": wf_labels,
                })

    return {
        "node_index": dict(node_index),
        "shared_nodes": shared_nodes,
        "predicate_variants": predicate_variants,
        "model_centric": dict(model_centric),
        "individual_labels": individual_labels,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def md_table_row(*cells: str) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


def generate_report(
    files: List[ModelFile],
    analysis: Dict,
) -> str:
    lines: List[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    individual_files = [f for f in files if not f.is_workflow]
    workflow_files = [f for f in files if f.is_workflow]

    lines += [
        "# Model Consistency Report",
        "",
        f"_Generated: {now}_",
        "",
        f"**Individual model files analysed:** {len(individual_files)}  ",
        f"**Workflow/overview files analysed:** {len(workflow_files)}  ",
        "",
        "This report identifies potential inconsistencies in node naming across "
        "the HPSWG-Models TSV files. It is generated automatically on each push "
        "and is intended as a working tool for model authors, not a definitive "
        "quality assessment.",
        "",
        "---",
        "",
    ]

    # -----------------------------------------------------------------------
    # Section 1: Model update checklist (workflow-centric)
    # -----------------------------------------------------------------------
    model_centric = analysis["model_centric"]
    lines += [
        "## 1. Model update checklist",
        "",
        "Each entry below lists an individual model file that contains node labels "
        "which differ from the canonical labels used in the workflow/overview TSV. "
        "The workflow is treated as the reference. Update the model file to use the "
        "canonical label, then increment its version number.",
        "",
    ]

    if not model_centric:
        lines.append("_All individual models are consistent with the workflow labels._\n")
    else:
        # Summary count
        total_changes = sum(len(v) for v in model_centric.values())
        lines += [
            f"**Models requiring updates:** {len(model_centric)}  ",
            f"**Total label changes needed:** {total_changes}  ",
            "",
        ]
        for sname in sorted(model_centric.keys()):
            changes = model_centric[sname]
            lines += [
                f"### `{sname}`",
                "",
                md_table_row("Class code", "Current label", "Change to"),
                md_table_row("---", "---", "---"),
            ]
            for c in sorted(changes, key=lambda x: (x["class_code"], x["current_label"])):
                canonical = " or ".join(f"`{l}`" for l in sorted(c["canonical_labels"]))
                lines.append(md_table_row(
                    f"`{c['class_code']}`",
                    f"`{c['current_label']}`",
                    canonical,
                ))
            lines.append("")

    # -----------------------------------------------------------------------
    # Section 2: Predicate-scoped variants across individual models
    # -----------------------------------------------------------------------
    variants = analysis["predicate_variants"]
    lines += [
        "## 2. Predicate-scoped label variants across individual models",
        "",
        "These cases show where the same CRM property connects nodes with the "
        "same class code but different labels in different individual models. "
        "Some of these will be intentional (an `E22` node genuinely represents "
        "different things in different models); others may be unintentional drift. "
        "Review each group to confirm intent.",
        "",
    ]

    if not variants:
        lines.append("_No predicate-scoped label variants detected across individual models._\n")
    else:
        lines += [
            md_table_row("Property", "Class code", "Label", "Files"),
            md_table_row("---", "---", "---", "---"),
        ]
        for (pred, code), label_map in sorted(variants.items(), key=lambda x: (x[0][1], x[0][0])):
            first = True
            for label, file_set in sorted(label_map.items()):
                pred_cell = f"`{pred}`" if first else ""
                code_cell = f"`{code}`" if first else ""
                first = False
                files_str = ", ".join(sorted(file_set))
                lines.append(md_table_row(pred_cell, code_cell, f"`{label}`", files_str))
        lines.append("")

    # -----------------------------------------------------------------------
    # Section 3: Shared nodes (exact match across models)
    # -----------------------------------------------------------------------
    shared = analysis["shared_nodes"]
    lines += [
        "## 3. Shared nodes (exact name match across models)",
        "",
        "Nodes that appear with exactly the same name in more than one model file. "
        "These are the current inter-model linking points. Consistency here is good; "
        "this section is informational.",
        "",
        md_table_row("Node", "Appears in"),
        md_table_row("---", "---"),
    ]

    for node, file_set in sorted(shared.items()):
        files_str = ", ".join(sorted(file_set))
        lines.append(md_table_row(f"`{node}`", files_str))
    lines.append("")

    # -----------------------------------------------------------------------
    # Section 4: Files analysed
    # -----------------------------------------------------------------------
    lines += [
        "## 4. Files analysed",
        "",
        md_table_row("File", "Type"),
        md_table_row("---", "---"),
    ]
    for mf in sorted(files, key=lambda f: (f.is_workflow, f.folder, f.path.name)):
        label = "Workflow/overview" if mf.is_workflow else "Individual model"
        lines.append(md_table_row(f"`{short_name(mf.path)}`", label))
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

    print(f"Found {len(files)} TSV file(s). Analysing...")

    analysis = analyse(files)

    report = generate_report(files, analysis)

    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")

    print(f"Report written to {REPORT_FILE.relative_to(REPO_ROOT)}")

    # Summary to stdout for Action log
    n_models = len(analysis["model_centric"])
    n_changes = sum(len(v) for v in analysis["model_centric"].values())
    n_var = len(analysis["predicate_variants"])
    n_shared = len(analysis["shared_nodes"])
    print(f"  Models needing updates:      {n_models}")
    print(f"  Total label changes needed:  {n_changes}")
    print(f"  Predicate-scoped variants:   {n_var}")
    print(f"  Shared nodes (exact match):  {n_shared}")


if __name__ == "__main__":
    main()
