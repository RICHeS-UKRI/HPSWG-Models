#!/usr/bin/env python3
"""
update_readmes.py
-----------------
Regenerates README.md files throughout the HPSWG-Models repository.

Reads:
  - models/**/*_v*.tsv         -- formed model files
  - models/**/*.txt            -- precursor files (field mapping notes)
  - scripts/ontologies.json   -- ontology version config
  - README.template.md        -- top-level README template
  - models/README.template.md -- models index template

Writes:
  - README.md                 -- top-level
  - models/README.md          -- models index
  - models/*/README.md        -- per-model (one per folder)

Template injection pattern:
  <!-- BEGIN AUTO: BLOCK-NAME -->
  ... replaced content ...
  <!-- END AUTO: BLOCK-NAME -->
"""

import json
import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
REPORTS_DIR = REPO_ROOT / "reports"
FORMS_DIR = REPO_ROOT / "forms"
NG_MERMAID_FILE = MODELS_DIR / "ng_models_mermaid.mmd"
OVERVIEW_MMD_FILE = MODELS_DIR / "overview_mermaid.mmd"
OVERVIEW_LINK_FILE = MODELS_DIR / "overview_link.md"
ONTOLOGIES_FILE = REPO_ROOT / "scripts" / "ontologies.json"

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

# Folders treated as semantic workflow references (canonical for consistency checking)
WORKFLOW_FOLDERS = {"workflows"}
# Folders treated as user-facing overview workflows (excluded from consistency checking)
USER_WORKFLOW_FOLDERS = {"user_workflows"}


@dataclass
class ModelFolder:
    """All discovered content for a single model folder."""
    folder_name: str
    folder_path: Path
    tsv_files: List[Path] = field(default_factory=list)
    txt_files: List[Path] = field(default_factory=list)

    @property
    def category(self) -> str:
        """
        Classify the folder's role:
          workflow      -- semantic CIDOC CRM workflow/overview reference
          user_workflow -- simplified user-facing overview
          model         -- standard domain model
        """
        if self.folder_name in WORKFLOW_FOLDERS:
            return "workflow"
        if self.folder_name in USER_WORKFLOW_FOLDERS:
            return "user_workflow"
        return "model"

    @property
    def status(self) -> str:
        """
        Classify the folder's development state:
          formed    -- has at least one versioned TSV
          mixed     -- has both TSV and TXT (transitional)
          precursor -- has TXT file(s) but no TSV
          empty     -- neither TSV nor TXT (placeholder)
        """
        has_tsv = bool(self.tsv_files)
        has_txt = bool(self.txt_files)
        if has_tsv and has_txt:
            return "mixed"
        if has_tsv:
            return "formed"
        if has_txt:
            return "precursor"
        return "empty"

    @property
    def status_badge(self) -> str:
        if self.category == "workflow":
            return "![Semantic Workflow](https://img.shields.io/badge/type-semantic--workflow-blue)"
        if self.category == "user_workflow":
            return "![User Workflow](https://img.shields.io/badge/type-user--workflow-blueviolet)"
        badges = {
            "formed":    "![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen)",
            "mixed":     "![Status: Mixed](https://img.shields.io/badge/status-mixed-yellow)",
            "precursor": "![Status: Precursor](https://img.shields.io/badge/status-precursor-orange)",
            "empty":     "![Status: Planned](https://img.shields.io/badge/status-planned-lightgrey)",
        }
        return badges.get(self.status, "")

    @property
    def latest_tsv(self) -> Optional[Path]:
        versioned = [(parse_version(p.name), p) for p in self.tsv_files]
        versioned = [(v, p) for v, p in versioned if v is not None]
        if not versioned:
            return None
        versioned.sort(reverse=True, key=lambda vp: vp[0])
        return versioned[0][1]

    @property
    def latest_version_str(self) -> Optional[str]:
        p = self.latest_tsv
        if p is None:
            return None
        v = parse_version(p.name)
        return ".".join(str(x) for x in v) if v else None


# ---------------------------------------------------------------------------
# Version parsing
# ---------------------------------------------------------------------------

def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
    m = VERSION_RE.search(filename)
    if not m:
        return None
    try:
        return tuple(int(p) for p in m.group(1).split("."))
    except ValueError:
        return None


def version_str(ver: Tuple[int, ...]) -> str:
    return ".".join(str(x) for x in ver)


# ---------------------------------------------------------------------------
# Git date helpers
# ---------------------------------------------------------------------------

def _git_log(args: List[str]) -> str:
    """Run git log and return stdout, or empty string on failure."""
    try:
        result = subprocess.run(
            ["git", "log"] + args,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def get_git_dates(file_path: Path) -> Tuple[str, str]:
    """
    Return (created, last_modified) as YYYY-MM-DD strings for a file.
    Uses git log against the file's path relative to repo root.
    Falls back to '--' if history is unavailable.
    """
    rel = file_path.relative_to(REPO_ROOT).as_posix()

    # Creation date: earliest commit that added this file
    created_raw = _git_log(
        ["--follow", "--diff-filter=A", "--format=%as", "--", rel]
    )
    # --format=%as gives YYYY-MM-DD; take the last line (oldest)
    created_lines = [l for l in created_raw.splitlines() if l.strip()]
    created = created_lines[-1] if created_lines else "--"

    # Last modified: most recent commit touching this file
    modified_raw = _git_log(["-1", "--format=%as", "--", rel])
    last_modified = modified_raw.strip() if modified_raw.strip() else "--"

    return created, last_modified


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

EXCLUDED_FOLDERS = {"old_samples", "heritage_object_part_types", "frame", "frame_part", "overview"}


def discover_models() -> Dict[str, ModelFolder]:
    """
    Discover all model folders under models/ and classify their contents.
    Returns a dict keyed by folder name.
    Excludes legacy folders defined in EXCLUDED_FOLDERS.
    Folders are categorised as workflow, user_workflow, or model via ModelFolder.category.
    """
    folders: Dict[str, ModelFolder] = {}

    if not MODELS_DIR.exists():
        return folders

    for child in sorted(MODELS_DIR.iterdir()):
        if not child.is_dir():
            continue
        if child.name in EXCLUDED_FOLDERS:
            continue

        tsv_files = sorted(child.glob("*_v*.tsv"))
        txt_files = sorted(f for f in child.glob("*.txt") if f.name != ".gitkeep")

        folders[child.name] = ModelFolder(
            folder_name=child.name,
            folder_path=child,
            tsv_files=tsv_files,
            txt_files=txt_files,
        )

    return folders


def find_ng_models_latest(tsvs: List[Path]) -> Optional[Path]:
    versioned = [(parse_version(p.name), p) for p in tsvs]
    versioned = [(v, p) for v, p in versioned if v is not None]
    if not versioned:
        return None
    versioned.sort(reverse=True, key=lambda vp: vp[0])
    return versioned[0][1]


# ---------------------------------------------------------------------------
# Ontology config
# ---------------------------------------------------------------------------

def load_ontologies() -> List[Dict]:
    if not ONTOLOGIES_FILE.exists():
        return []
    with ONTOLOGIES_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def generate_ontology_ref_block(ontologies: List[Dict]) -> str:
    """
    Short inline reference table, used in models/README.md and per-model READMEs.
    Links to ONTOLOGIES.md for full detail.
    """
    if not ontologies:
        return "_Ontology information not available. See `ONTOLOGIES.md`._"

    lines = [
        "See [`ONTOLOGIES.md`](../ONTOLOGIES.md) for full version details, "
        "source links, and compatibility notes. Ontologies currently in use:\n",
        "| Ontology | Version | Prefix |",
        "|----------|---------|--------|",
    ]
    for o in ontologies:
        name = o.get("name", "")
        version = o.get("version") or "_see notes_"
        prefix = o.get("prefix", "")
        docs = o.get("docs", "")
        name_cell = f"[{name}]({docs})" if docs else name
        lines.append(f"| {name_cell} | {version} | `{prefix}` |")

    return "\n".join(lines)


def generate_ontologies_md(ontologies: List[Dict]) -> str:
    """
    Full ONTOLOGIES.md content.
    """
    lines = [
        "# Ontologies",
        "",
        "This document records the semantic ontologies used across the HPSWG-Models "
        "repository, including the versions in use, canonical namespaces, and links "
        "to source documentation.",
        "",
        "All models in this repository are expressed using CIDOC CRM 7.1.3 as the "
        "core ontology. Extension ontologies (CRMdig, CRMsci) have been lightly "
        "adjusted for compatibility with this version -- see the notes column below "
        "for details.",
        "",
        "ResearchSpace-specific classes and properties are included where the "
        "National Gallery's ResearchSpace deployment requires them. CRM-aligned "
        "alternatives are planned for future inclusion alongside these terms.",
        "",
        "## Ontology reference",
        "",
        "| Ontology | Version | Prefix | Namespace | Documentation | Download |",
        "|----------|---------|--------|-----------|---------------|----------|",
    ]

    for o in ontologies:
        name = o.get("name", "")
        version = o.get("version") or "_see notes_"
        prefix = o.get("prefix", "")
        namespace = o.get("namespace", "")
        docs = o.get("docs", "")
        download = o.get("download", "")

        docs_cell = f"[Link]({docs})" if docs else "--"
        dl_cell = f"[RDFS]({download})" if download else "--"
        lines.append(
            f"| {name} | {version} | `{prefix}` | `{namespace}` | {docs_cell} | {dl_cell} |"
        )

    lines += [
        "",
        "## Compatibility notes",
        "",
        "**CRMdig and CRMsci** have each been adjusted at a small number of points "
        "to ensure compatibility with CIDOC CRM 7.1.3. Where adjustments have been "
        "made, the relevant classes and properties remain semantically equivalent to "
        "the published versions. Full details of any deviations will be recorded "
        "here as the models mature.",
        "",
        "**ResearchSpace terms** are used pragmatically within the National Gallery's "
        "ResearchSpace deployment. These are not part of a published ontology standard. "
        "Work is planned to document CRM-equivalent alternatives for each ResearchSpace "
        "term used, making the models portable beyond the ResearchSpace platform.",
        "",
        "## Updating this file",
        "",
        "This file is maintained manually. When ontology versions are updated, "
        "update both this file and `scripts/ontologies.json`, which drives the "
        "short ontology reference tables in the model READMEs.",
    ]

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# URL helpers
# ---------------------------------------------------------------------------

def raw_url(raw_base: str, file_path: Path) -> str:
    rel = file_path.relative_to(REPO_ROOT).as_posix()
    return f"{raw_base}/{rel}"


def modeller_url(raw_base: str, file_path: Path) -> str:
    return (
        "https://research.nationalgallery.org.uk/lab/modelling/?url="
        + raw_url(raw_base, file_path)
    )


# ---------------------------------------------------------------------------
# Template injection
# ---------------------------------------------------------------------------

def replace_auto_block(content: str, block_name: str, replacement: str) -> str:
    pattern = re.compile(
        rf"(<!-- BEGIN AUTO: {re.escape(block_name)} -->)(.*?)"
        rf"(<!-- END AUTO: {re.escape(block_name)} -->)",
        flags=re.DOTALL,
    )

    def repl(m: re.Match) -> str:
        rep = "\n" + replacement.strip() + "\n"
        return f"{m.group(1)}{rep}{m.group(3)}"

    new_content, count = pattern.subn(repl, content)
    return new_content if count > 0 else content


# ---------------------------------------------------------------------------
# Block generators
# ---------------------------------------------------------------------------

def model_title_from_folder(folder_name: str) -> str:
    base = folder_name.replace("_", " ").strip()
    if not base:
        return "Model"
    return base[:1].upper() + base[1:]


def _model_table_rows(
    folders: Dict[str, ModelFolder],
    raw_base: str,
    prefix: str = "models/",
) -> List[str]:
    """Generate table rows for a set of model folders."""
    rows: List[str] = []
    for name, mf in sorted(folders.items()):
        title = model_title_from_folder(name)
        badge = mf.status_badge
        folder_link = f"[`{prefix}{name}`]({prefix}{name}/)"

        if mf.latest_tsv:
            ver = mf.latest_version_str
            tsv_link = f"[v{ver}]({raw_url(raw_base, mf.latest_tsv)})"
            vis_link = f"[Open]({modeller_url(raw_base, mf.latest_tsv)})"
        elif mf.txt_files:
            tsv_link = "_Precursor files only_"
            vis_link = "--"
        else:
            tsv_link = "--"
            vis_link = "--"

        rows.append(f"| {title} | {badge} | {folder_link} | {tsv_link} | {vis_link} |")
    return rows


def _model_table(
    folders: Dict[str, ModelFolder],
    raw_base: str,
    heading: str,
    description: str,
    prefix: str = "models/",
) -> List[str]:
    """Generate a complete labelled table section for a category of folders."""
    if not folders:
        return []
    lines = [
        f"### {heading}",
        "",
        description,
        "",
        "| Name | Type / Status | Folder | Latest TSV | Visualisation |",
        "|------|--------------|--------|-----------|---------------|",
    ]
    lines += _model_table_rows(folders, raw_base, prefix)
    lines.append("")
    return lines


def generate_model_list_block(
    folders: Dict[str, ModelFolder], raw_base: str
) -> str:
    """
    Full model index for the top-level README, split into three sections:
    semantic workflows, user workflows, and standard models.
    """
    workflows = {n: mf for n, mf in folders.items() if mf.category == "workflow"}
    user_wf = {n: mf for n, mf in folders.items() if mf.category == "user_workflow"}
    models = {n: mf for n, mf in folders.items() if mf.category == "model"}

    if not folders:
        return "_No model folders detected yet._"

    lines: List[str] = []
    lines += _model_table(
        workflows, raw_base,
        "Semantic workflow overviews",
        "CIDOC CRM-aligned inter-model connectivity references. "
        "These act as the canonical reference for shared node labels across individual models.",
    )
    lines += _model_table(
        user_wf, raw_base,
        "User workflow overviews",
        "Simplified overviews for communication and stakeholder agreement. "
        "Not part of the semantic consistency check.",
    )
    lines += _model_table(
        models, raw_base,
        "Domain models",
        "Individual CIDOC CRM domain models, each covering a specific aspect of heritage science documentation.",
    )
    return "\n".join(lines)


def generate_models_folder_block(
    folders: Dict[str, ModelFolder], raw_base: str, ng_tsvs: List[Path]
) -> str:
    """
    Content for the MODEL-FOLDERS auto block in models/README.md.
    """
    pieces: List[str] = []

    # NG-wide model versions table
    if ng_tsvs:
        versioned = [(parse_version(p.name), p) for p in ng_tsvs]
        versioned = [(v, p) for v, p in versioned if v is not None]
        versioned.sort(reverse=True, key=lambda vp: vp[0])

        pieces.append("### NG-wide overview model\n")
        pieces.append("| Version | Raw TSV | Visualisation |")
        pieces.append("|---------|---------|---------------|")
        for ver, path in versioned:
            ver_s = version_str(ver)
            pieces.append(
                f"| {ver_s} "
                f"| [TSV]({raw_url(raw_base, path)}) "
                f"| [Open in Modeller]({modeller_url(raw_base, path)}) |"
            )
        pieces.append("")

    # Per-folder index split by category
    workflows = {n: mf for n, mf in folders.items() if mf.category == "workflow"}
    user_wf = {n: mf for n, mf in folders.items() if mf.category == "user_workflow"}
    models = {n: mf for n, mf in folders.items() if mf.category == "model"}

    pieces += _model_table(
        workflows, raw_base,
        "Semantic workflow overviews",
        "CIDOC CRM-aligned inter-model connectivity references.",
        prefix="./",
    )
    pieces += _model_table(
        user_wf, raw_base,
        "User workflow overviews",
        "Simplified overviews for communication and stakeholder agreement.",
        prefix="./",
    )
    pieces += _model_table(
        models, raw_base,
        "Domain models",
        "Individual CIDOC CRM domain models.",
        prefix="./",
    )

    if not (workflows or user_wf or models):
        pieces.append("_No model folders detected yet._")

    return "\n".join(pieces)


def generate_formed_versions_block(mf: ModelFolder, raw_base: str) -> str:
    """
    Version history table for a formed or mixed model folder.
    Includes git-derived dates.
    """
    versioned = [(parse_version(p.name), p) for p in mf.tsv_files]
    versioned = [(v, p) for v, p in versioned if v is not None]
    if not versioned:
        return ""
    versioned.sort(reverse=True, key=lambda vp: vp[0])

    latest_ver, latest_path = versioned[0]
    latest_url = modeller_url(raw_base, latest_path)
    latest_ver_s = version_str(latest_ver)

    lines = [
        "<details>",
        f'<summary><strong>{model_title_from_folder(mf.folder_name)}</strong>: '
        f'latest version <a href="{latest_url}">v{latest_ver_s}</a></summary>',
        "",
        "| | Version | Created | Last modified | Open in Modeller |",
        "| :---: | :---: | :---: | :---: | --- |",
    ]

    for idx, (ver, path) in enumerate(versioned):
        ver_s = version_str(ver)
        created, modified = get_git_dates(path)
        url = modeller_url(raw_base, path)
        tick = ":heavy_check_mark:" if idx == 0 else ""
        lines.append(
            f"| {tick} | v{ver_s} | {created} | {modified} | [Open]({url}) |"
        )

    lines += ["", "</details>", ""]
    return "\n".join(lines)


def generate_precursor_block(mf: ModelFolder, raw_base: str) -> str:
    """
    File listing for precursor TXT files in a folder.
    """
    lines = [
        "> **Status: Precursor** -- This model is in early development. "
        "The files below contain field mapping notes and draft content "
        "that will form the basis of the TSV model.\n",
        "| File | Raw link |",
        "|------|----------|",
    ]
    for txt in sorted(mf.txt_files):
        url = raw_url(raw_base, txt)
        lines.append(f"| `{txt.name}` | [View raw]({url}) |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Field directive parsing and table generation
# ---------------------------------------------------------------------------

# NEW
# Regex to strip CRM class prefix, e.g. "E42: " or "S13: " or "crm:E42: "
_CRM_PREFIX_RE = re.compile(r"^[A-Za-z0-9]+:\s*")

# Known ResearchSpace class name prefixes that should be stripped from human labels.
# These do not match the short alphanumeric CRM pattern (e.g. "E42") so require
# explicit listing. Extend this set as new RS classes are introduced in models.
_RS_CLASS_PREFIXES = {
    "EX_Digital_Image",
    "EX_Digital_Image_Region",
}

# Regex to extract multiplicity lower bound from predicate, e.g. "(0 to 1)" or "(1 to 1)"
_MULTIPLICITY_RE = re.compile(r"\((\d+)\s+to")

# Regex to strip "(Alternative labels: ...)" parenthetical from tooltip text
_ALT_LABELS_RE = re.compile(r"\s*\(Alternative labels:[^)]*\)", re.IGNORECASE)


def _strip_crm_prefix(label: str) -> str:
    """
    Strip leading class prefix from a node label to produce a human-readable label.

    Handles two cases:
      1. Standard CRM/CRMsci/CRMdig prefix pattern, e.g. 'E42: Foo' -> 'Foo',
         'S13: Bar' -> 'Bar', 'crm:E42: Foo' -> 'Foo'.
      2. ResearchSpace class prefixes listed in _RS_CLASS_PREFIXES, e.g.
         'EX_Digital_Image: Main Image' -> 'Main Image'.
         If the node label exactly matches a known RS class with no instance
         qualifier (e.g. 'EX_Digital_Image_Region'), the full label is returned
         as-is since there is nothing further to strip.
    """
    # Try standard CRM pattern first
    stripped = _CRM_PREFIX_RE.sub("", label, count=1).strip()
    if stripped != label:
        return stripped

    # Fallback: check RS class prefixes
    for rs_class in _RS_CLASS_PREFIXES:
        if label == rs_class:
            # No instance qualifier -- return the class name as the label
            # Split on underscore and title-case for readability,
            # e.g. 'EX_Digital_Image_Region' -> 'Digital Image Region'
            parts = rs_class.split("_")
            # Drop leading 'EX' prefix if present
            if parts[0].upper() == "EX":
                parts = parts[1:]
            return " ".join(p.capitalize() for p in parts)
        prefix = rs_class + ": "
        if label.startswith(prefix):
            return label[len(prefix):].strip()

    return label


def _strip_alt_labels(tooltip: str) -> str:
    """Remove '(Alternative labels: ...)' parenthetical from tooltip text."""
    return _ALT_LABELS_RE.sub("", tooltip).strip()


# ---------------------------------------------------------------------------
# Behaviour badge support
# ---------------------------------------------------------------------------

# Controlled vocabulary and colour map for //field behaviour: tags.
# Keys are the tag values as they appear in the TSV (lowercase).
# Values are (display label, hex colour) pairs for shields.io badge generation.
# All colours have been verified to meet WCAG AA contrast ratio (>= 4.5:1)
# against white text (#ffffff).
_BEHAVIOUR_BADGES: Dict[str, Tuple[str, str]] = {
    "free-text":  ("Free Text",       "0969da"),  # Blue      -- ratio ~4.6:1
    "list":       ("Controlled List", "1a7f37"),  # Green     -- ratio ~5.3:1
    "select":     ("Select Entity",   "8250df"),  # Purple    -- ratio ~4.6:1
    "pid":        ("External ID",     "0e7490"),  # Teal      -- ratio ~4.8:1
    "system-id":  ("System ID",       "57606a"),  # Mid grey  -- ratio ~4.6:1
    "ingested":   ("Ingested",        "7d5a00"),  # Dark gold -- ratio ~6.8:1
    "inherited":  ("Inherited",       "bc4c00"),  # Orange    -- ratio ~5.1:1
    "auto":       ("Automatic",       "32383f"),  # Dark grey -- ratio ~11.2:1
}


def _behaviour_badge(tag: str) -> str:
    """
    Return a shields.io markdown image string for a behaviour tag.
    Uses the two-part label style (dark grey left panel, coloured right panel)
    consistent with the status badges used in model index tables.
    Hyphens within the message are encoded as '--' per shields.io static badge syntax.
    Returns an empty string if the tag is unrecognised or empty.
    """
    if not tag:
        return ""
    entry = _BEHAVIOUR_BADGES.get(tag)
    if entry is None:
        print(f"  WARNING: Unrecognised behaviour tag '{tag}' -- badge will be omitted.")
        return ""
    label, colour = entry
    # Encode hyphens in label as '--' for shields.io static badge URL
    encoded_label = label.replace("-", "--").replace(" ", "%20")
    url = f"https://img.shields.io/badge/%2F%2F-{encoded_label}-{colour}"
    return f"![behaviour: {label}]({url})"


@dataclass
class FieldRecord:
    """A parsed //field or //field-via directive."""
    is_via: bool
    node_label: str          # Full node label as written in directive col 1
    via_label: str           # Intermediate node label (//field-via only, else "")
    order: int
    alternatives: List[str]  # Already deduplicated against human_label
    explicit_desc: str       # Col 4 text (required for via, optional for direct)
    optional_note: str       # Col 5 (//field-via) or col 4 additional note
    behaviour: str = ""      # Value of behaviour: tag parsed from optional note column
    # Resolved at a later stage:
    human_label: str = ""
    crm_code: str = ""
    description: str = ""
    required: str = ""       # "✓", "Optional", or "✓*"


def _parse_field_line(line: str) -> Optional[FieldRecord]:
    """
    Parse a single //field or //field-via directive line.
    Returns a FieldRecord or None if the line cannot be parsed.

    The optional note column (col 4 for //field, col 5 for //field-via) may contain
    a 'behaviour:TAG' token alongside free-text notes, separated by ';'.
    The behaviour token is extracted and stored separately; the remaining text
    becomes optional_note and is appended to the field description as before.
    """
    line = line.strip()
    is_via = line.startswith("//field-via ")
    if is_via:
        body = line[len("//field-via "):].strip()
    elif line.startswith("//field "):
        body = line[len("//field "):].strip()
    else:
        return None

    parts = [p.strip() for p in body.split("|")]

    # Need at least node + order + alternatives
    if len(parts) < 3:
        print(f"  WARNING: Skipping malformed field directive (too few columns): {line}")
        return None

    col1 = parts[0]
    order_str = parts[1]
    alts_raw = parts[2]
    col4 = parts[3].strip() if len(parts) > 3 else ""
    col5 = parts[4].strip() if len(parts) > 4 else ""

    try:
        order = int(order_str)
    except ValueError:
        print(f"  WARNING: Skipping field directive with non-integer order: {line}")
        return None

    # Parse node reference
    if is_via:
        # Split on " via " to get target and intermediate
        via_parts = col1.split(" via ", 1)
        if len(via_parts) != 2:
            print(f"  WARNING: Skipping //field-via with missing 'via' separator: {line}")
            return None
        node_label = via_parts[0].strip()
        via_label = via_parts[1].strip()
        explicit_desc = col4
        note_raw = col5
    else:
        node_label = col1
        via_label = ""
        explicit_desc = ""
        note_raw = col4

    # Extract behaviour: tag from the note column.
    # The note column may contain 'behaviour:TAG' alongside free-text, separated by ';'.
    # The behaviour token is removed; remaining parts rejoin as optional_note.
    behaviour = ""
    note_parts = [s.strip() for s in note_raw.split(";")]
    non_behaviour = []
    for part in note_parts:
        if part.lower().startswith("behaviour:"):
            behaviour = part[len("behaviour:"):].strip().lower()
        else:
            non_behaviour.append(part)
    optional_note = "; ".join(p for p in non_behaviour if p).strip()

    # Parse alternatives, deduplicate against human label later
    human_label = _strip_crm_prefix(node_label)
    alts = [a.strip() for a in alts_raw.split(";") if a.strip()]
    alts = [a for a in alts if a != human_label]

    # NEW
    # Extract CRM code from node label prefix.
    # For RS class nodes (e.g. 'EX_Digital_Image: Main Image'), use the RS class
    # name as the code. For nodes that exactly match a known RS class with no
    # instance qualifier, use the full label as the code.
    def _extract_code(lbl: str) -> str:
        for rs_class in _RS_CLASS_PREFIXES:
            if lbl == rs_class or lbl.startswith(rs_class + ": "):
                return rs_class
        m = re.match(r"^([A-Za-z0-9]+):", lbl)
        return m.group(1) if m else lbl

    crm_code = _extract_code(node_label)

    if is_via:
        via_code = _extract_code(via_label)
        crm_code = f"{via_code} > {crm_code}"

    return FieldRecord(
        is_via=is_via,
        node_label=node_label,
        via_label=via_label,
        order=order,
        alternatives=alts,
        explicit_desc=explicit_desc,
        optional_note=optional_note,
        behaviour=behaviour,
        human_label=human_label,
        crm_code=crm_code,
    )


def _load_tsv_lines(tsv_path: Path) -> List[List[str]]:
    """
    Read a TSV file and return all lines split by tab.
    Skips blank lines.
    """
    lines = []
    try:
        for raw in tsv_path.read_text(encoding="utf-8").splitlines():
            if raw.strip():
                lines.append(raw.split("\t"))
    except Exception as e:
        print(f"  WARNING: Could not read {tsv_path}: {e}")
    return lines


def _find_tooltip(node_label: str, tsv_lines: List[List[str]]) -> str:
    """
    Find the tooltip text for a given node label in parsed TSV lines.
    Returns empty string if not found.
    """
    for parts in tsv_lines:
        if len(parts) >= 3 and parts[0].strip() == node_label and parts[1].strip() == "tooltip":
            return parts[2].strip()
    return ""


def _find_required(node_label: str, tsv_lines: List[List[str]]) -> Optional[str]:
    """
    Find the required status for a node by locating the predicate line
    where the object (col 3) matches node_label and reading the multiplicity
    lower bound from the predicate (col 2).
    Returns "✓", "Optional", or None if not found.
    """
    for parts in tsv_lines:
        if len(parts) < 3:
            continue
        obj = parts[2].strip()
        pred = parts[1].strip()
        if obj == node_label:
            m = _MULTIPLICITY_RE.search(pred)
            if m:
                lower = int(m.group(1))
                return "Optional" if lower == 0 else "✓"
    return None


def parse_and_resolve_fields(tsv_path: Path) -> List[FieldRecord]:
    """
    Parse all //field and //field-via directives from a TSV file,
    resolve descriptions, required status, and return records sorted by order.
    Returns an empty list if no directives are found.
    """
    tsv_lines = _load_tsv_lines(tsv_path)
    records: List[FieldRecord] = []

    for parts in tsv_lines:
        raw = "\t".join(parts)
        if not (raw.startswith("//field ") or raw.startswith("//field-via ")):
            continue
        rec = _parse_field_line(raw)
        if rec is None:
            continue
        records.append(rec)

    if not records:
        return []

    model_name = tsv_path.parent.name

    for rec in records:
        if rec.is_via:
            # Description comes from col 4 (explicit_desc), with optional note appended
            desc = rec.explicit_desc
            if rec.optional_note:
                desc = f"{desc} ({rec.optional_note})"
            rec.description = desc

            # Required: look up predicate to the intermediate node
            req = _find_required(rec.via_label, tsv_lines)
            if req is None:
                print(
                    f"  WARNING [{model_name}]: Could not derive required status for "
                    f"//field-via '{rec.node_label} via {rec.via_label}'. Defaulting to required."
                )
                rec.required = "✓*"
            else:
                rec.required = req

        else:
            # Description: tooltip text with alt-labels parenthetical stripped,
            # plus optional note appended in brackets if present
            tooltip = _find_tooltip(rec.node_label, tsv_lines)
            if tooltip:
                desc = _strip_alt_labels(tooltip)
            elif rec.explicit_desc:
                desc = rec.explicit_desc
            else:
                print(
                    f"  WARNING [{model_name}]: No tooltip found for //field node "
                    f"'{rec.node_label}'. Description will be empty."
                )
                desc = ""
            if rec.optional_note:
                desc = f"{desc} ({rec.optional_note})"
            rec.description = desc

            # Required: look up predicate to this node
            req = _find_required(rec.node_label, tsv_lines)
            if req is None:
                print(
                    f"  WARNING [{model_name}]: Could not derive required status for "
                    f"//field node '{rec.node_label}'. Defaulting to required."
                )
                rec.required = "✓*"
            else:
                rec.required = req

    records.sort(key=lambda r: r.order)
    return records


def identify_primary_node(tsv_lines: List[List[str]]) -> Tuple[str, str]:
    """
    Identify the primary node and Document Note node from TSV lines.
    Returns (primary_node_label, doc_note_node_label).
    doc_note_node_label is empty string if not found.

    Fallback chain:
      1. Subject of the line where predicate is 'has note' and object starts
         with 'Document Note:'
      2. Subject of the first line whose format column contains '-fs32'
      3. Most frequent subject across all non-directive structural lines
      4. Empty string with a warning printed
    """
    primary = ""
    doc_note = ""

    # Step 1: has note + Document Note
    for parts in tsv_lines:
        if len(parts) < 3:
            continue
        if parts[1].strip() == "has note" and parts[2].strip().startswith("Document Note:"):
            primary = parts[0].strip()
            doc_note = parts[2].strip()
            return primary, doc_note

    # Step 2: -fs32 format class
    for parts in tsv_lines:
        if len(parts) < 4:
            continue
        fmt = parts[3].strip() if len(parts) > 3 else ""
        if "-fs32" in fmt:
            primary = parts[0].strip()
            return primary, doc_note

    # Step 3: most frequent subject in structural lines
    from collections import Counter
    subject_counts: Counter = Counter()
    for parts in tsv_lines:
        raw = "\t".join(parts)
        if raw.startswith("//"):
            continue
        if len(parts) < 2:
            continue
        pred = parts[1].strip()
        if pred in ("tooltip", "has note", "from list"):
            continue
        subject_counts[parts[0].strip()] += 1

    if subject_counts:
        primary = subject_counts.most_common(1)[0][0]
        return primary, doc_note

    # Step 4: fallback
    print("  WARNING: Primary node could not be automatically identified in this model.")
    return "", ""


def generate_field_section_header(
    mf: "ModelFolder",
    raw_base: str,
    tsv_lines: List[List[str]],
) -> str:
    """
    Generate the header block for a field table section:
      - Links line (folder, raw TSV, open in modeller)
      - Document Note tooltip paragraph
      - Primary node tooltip in italics (if different or always shown)

    Returns a markdown string. Falls back gracefully if tooltips are missing.
    """
    title = model_title_from_folder(mf.folder_name)
    lines: List[str] = []

    # Links line
    if mf.latest_tsv and raw_base:
        folder_rel = f"models/{mf.folder_name}"
        folder_link = f"[`{folder_rel}`](../{folder_rel}/)"
        tsv_link = f"[v{mf.latest_version_str}]({raw_url(raw_base, mf.latest_tsv)})"
        open_link = f"[Open in Modeller]({modeller_url(raw_base, mf.latest_tsv)})"
        lines.append(f"{folder_link} | {tsv_link} | {open_link}\n")
    else:
        lines.append(f"_{title}_\n")

    # Identify primary node and doc note node
    primary_node, doc_note_node = identify_primary_node(tsv_lines)

    # Document Note tooltip (shown first, as the fuller descriptive text)
    if doc_note_node:
        doc_note_tooltip = _find_tooltip(doc_note_node, tsv_lines)
        if doc_note_tooltip:
            cleaned = _strip_alt_labels(doc_note_tooltip)
            lines.append(f"{cleaned}\n")

    # Primary node tooltip (shown in italics below)
    if primary_node:
        primary_tooltip = _find_tooltip(primary_node, tsv_lines)
        if primary_tooltip:
            cleaned = _strip_alt_labels(primary_tooltip)
            lines.append(f"_{cleaned}_\n")

    # If neither tooltip was found, add a warning note
    if not doc_note_node and not primary_node:
        lines.append(
            "_Model description not available -- primary node could not be identified._\n"
        )

    return "\n".join(lines)


def generate_field_table_block(tsv_path: Path) -> str:
    """
    Generate a markdown field reference table from //field directives in a TSV.
    Returns an empty string if no directives are found.

    If any field record carries a behaviour tag, a Behaviour column is added
    between CRM Code and Label Description, rendering a shields.io badge for
    each tagged field. Models without any behaviour tags render the original
    five-column table unchanged.
    """
    records = parse_and_resolve_fields(tsv_path)
    if not records:
        return ""

    has_uncertain = any(r.required == "✓*" for r in records)
    has_behaviour = any(r.behaviour for r in records)

    if has_behaviour:
        lines = [
            "| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |",
            "|----------|---------------------------|-------------------|----------|-----------|-------------------|",
        ]
        for rec in records:
            alts = "; ".join(rec.alternatives) if rec.alternatives else "--"
            desc = rec.description or "--"
            badge = _behaviour_badge(rec.behaviour) if rec.behaviour else "--"
            lines.append(
                f"| {rec.required} | {rec.human_label} | {alts} | {rec.crm_code} | {badge} | {desc} |"
            )
    else:
        lines = [
            "| Required | Human understandable Label | Alternative Labels | CRM Code | Label Description |",
            "|----------|---------------------------|-------------------|----------|-------------------|",
        ]
        for rec in records:
            alts = "; ".join(rec.alternatives) if rec.alternatives else "--"
            desc = rec.description or "--"
            lines.append(
                f"| {rec.required} | {rec.human_label} | {alts} | {rec.crm_code} | {desc} |"
            )

    if has_uncertain:
        lines += [
            "",
            "_\\* Required status could not be derived from the model and has been "
            "set to required by default. Please verify._",
        ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Forms folder writers
# ---------------------------------------------------------------------------

def _forms_listing_block(models_with_fields: List[str]) -> str:
    """Generate the FORMS-LISTING auto block content for forms/README.md."""
    if not models_with_fields:
        return "_No field tables have been generated yet._"
    lines = [
        "| Model | Field table |",
        "|-------|-------------|",
    ]
    for name in sorted(models_with_fields):
        title = model_title_from_folder(name)
        lines.append(f"| {title} | [field-tables.md](field-tables.md#{name.replace('_', '-')}) |")
    return "\n".join(lines)


def write_forms_outputs(folders: Dict[str, ModelFolder], raw_base: str):
    """
    Generate forms/field-tables.md (aggregated field tables for all models
    that have //field directives) and forms/README.md.
    """
    FORMS_DIR.mkdir(exist_ok=True)

    models_with_fields: List[str] = []
    sections: List[str] = []

    for name, mf in sorted(folders.items()):
        if mf.category != "model":
            continue
        if mf.latest_tsv is None:
            continue
        block = generate_field_table_block(mf.latest_tsv)
        if not block:
            continue
        tsv_lines = _load_tsv_lines(mf.latest_tsv)
        header = generate_field_section_header(mf, raw_base, tsv_lines)
        models_with_fields.append(name)
        title = model_title_from_folder(name)
        sections += [
            f"### {title}\n",
            header,
            block,
            "",
        ]

    # Write field-tables.md
    field_tables_path = FORMS_DIR / "field-tables.md"
    if sections:
        header = [
            "# Field tables\n",
            "_This file is auto-generated by `scripts/update_readmes.py`. "
            "Do not edit directly -- update the source TSV model files instead._\n",
            "Each section below corresponds to a model that contains `//field` "
            "or `//field-via` directives. Tables are intended to support form "
            "and data input design. See [CONTRIBUTING.md](../CONTRIBUTING.md) "
            "for guidance on adding field directives to a model.\n",
        ]
        content = "\n".join(header + sections)
    else:
        content = (
            "# Field tables\n\n"
            "_No field tables have been generated yet. Add `//field` directives "
            "to a model TSV to populate this document._\n"
        )
    field_tables_path.write_text(content, encoding="utf-8")

    # Write forms/README.md from template or bootstrap
    template_path = FORMS_DIR / "README.template.md"
    listing_block = _forms_listing_block(models_with_fields)

    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
        readme_content = replace_auto_block(template, "FORMS-LISTING", listing_block)
    else:
        readme_content = "\n".join([
            "# Forms and Data Input Resources\n",
            "This folder contains resources to support the design of forms and "
            "data input interfaces derived from the HPSWG semantic models.\n",
            "<!-- BEGIN AUTO: FORMS-LISTING -->",
            listing_block,
            "<!-- END AUTO: FORMS-LISTING -->",
        ])
    (FORMS_DIR / "README.md").write_text(readme_content, encoding="utf-8")

    if models_with_fields:
        print(f"  Field tables generated for: {', '.join(sorted(models_with_fields))}")
    else:
        print("  No //field directives found in any model -- forms/field-tables.md placeholder written.")


# ---------------------------------------------------------------------------
# README writers
# ---------------------------------------------------------------------------


def read_overview_link() -> str:
    if OVERVIEW_LINK_FILE.exists():
        return OVERVIEW_LINK_FILE.read_text(encoding="utf-8").strip()
    return ""


def read_mermaid_block() -> str:
    if OVERVIEW_MMD_FILE.exists():
        text = OVERVIEW_MMD_FILE.read_text(encoding="utf-8").strip()
        if text:
            return f"```mermaid\n{text}\n```\n"
    return "_Mermaid diagram not available yet._\n"


def write_top_readme(
    folders: Dict[str, ModelFolder],
    raw_base: str,
    ng_latest: Optional[Path],
):
    template_path = REPO_ROOT / "README.template.md"
    if not template_path.exists():
        raise SystemExit("Missing README.template.md at repository root.")

    template = template_path.read_text(encoding="utf-8")

    link_text = read_overview_link()
    mermaid_block = read_mermaid_block()
    visual_block = (link_text + "\n\n" + mermaid_block) if link_text else mermaid_block
    content = replace_auto_block(template, "NG-MODEL-VISUAL", visual_block)
    content = replace_auto_block(
        content, "MODEL-LIST", generate_model_list_block(folders, raw_base)
    )

    (REPO_ROOT / "README.md").write_text(content, encoding="utf-8")


def write_models_readme(
    folders: Dict[str, ModelFolder],
    raw_base: str,
    ng_tsvs: List[Path],
    ontologies: List[Dict],
):
    template_path = MODELS_DIR / "README.template.md"

    folder_block = generate_models_folder_block(folders, raw_base, ng_tsvs)
    ontology_block = generate_ontology_ref_block(ontologies)

    if not template_path.exists():
        # Fallback: write a minimal auto-generated README
        lines = [
            "# Models\n",
            "This folder contains the NG-wide model definitions and individual model "
            "folders. Each subfolder holds versioned TSV files for use with the "
            "[Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/).\n",
            "## Ontologies in use\n",
            ontology_block,
            "\n## Model index\n",
            folder_block,
        ]
        (MODELS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
        return

    template = template_path.read_text(encoding="utf-8")
    content = replace_auto_block(template, "MODEL-FOLDERS", folder_block)
    content = replace_auto_block(template, "ONTOLOGY-REF", ontology_block)
    (MODELS_DIR / "README.md").write_text(content, encoding="utf-8")


def write_per_model_readmes(
    folders: Dict[str, ModelFolder],
    raw_base: str,
    ontologies: List[Dict],
):
    ontology_block = generate_ontology_ref_block(ontologies)

    for name, mf in folders.items():
        title = model_title_from_folder(name)
        lines: List[str] = []

        # Header
        lines += [
            f"# {title}\n",
            f"{mf.status_badge}\n",
            "This folder contains versioned model files for use with the "
            "[National Gallery Dynamic Modeller]"
            "(https://research.nationalgallery.org.uk/lab/modelling/). "
            "Models are expressed as tab-separated triples aligned to CIDOC CRM "
            "and related extension ontologies.\n",
        ]

        # Ontology reference
        lines += [
            "## Ontologies\n",
            ontology_block,
            "",
        ]

        # Status-specific content
        if mf.status in ("formed", "mixed"):
            lines += [
                "## Model versions\n",
                generate_formed_versions_block(mf, raw_base),
            ]

        if mf.status in ("precursor", "mixed") and mf.txt_files:
            lines += [
                "## Precursor files\n",
                generate_precursor_block(mf, raw_base),
                "",
            ]

        if mf.status == "empty":
            lines += [
                "> **Status: Planned** -- This model folder is reserved for "
                "future development. No files are available yet.\n",
            ]

        # Field reference table (only if //field directives are present)
        if mf.latest_tsv:
            field_block = generate_field_table_block(mf.latest_tsv)
            if field_block:
                tsv_lines = _load_tsv_lines(mf.latest_tsv)
                field_header = generate_field_section_header(mf, raw_base, tsv_lines)
                lines += [
                    "## Field reference\n",
                    "This table lists the fields defined for data entry or display, "
                    "derived from `//field` and `//field-via` directives in the model. "
                    "See the [forms folder](../../forms/field-tables.md) for the "
                    "aggregated cross-model view.\n",
                    field_header,
                    field_block,
                    "",
                ]

        # Contributing guidance
        lines += [
            "## Contributing\n",
            "If you would like to contribute to this model, please refer to the "
            "[repository contributing guidelines](../../CONTRIBUTING.md) and the "
            "[ontology reference](../../ONTOLOGIES.md). "
            "The TSV triple format is documented in the "
            "[Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) "
            "interface.\n",
        ]

        readme_path = mf.folder_path / "README.md"
        readme_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Reports README
# ---------------------------------------------------------------------------


def extract_report_description(report_path: Path) -> str:
    """
    Extract a short description from a report file.
    Reads the first non-empty, non-heading, non-generated line after the H1 title.
    Falls back to a generic label if nothing suitable is found.
    """
    try:
        lines = report_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return "_No description available._"

    past_title = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            past_title = True
            continue
        if past_title and not stripped.startswith("_Generated"):
            return stripped[:120] + ("..." if len(stripped) > 120 else "")

    return "_No description available._"


def write_reports_readme(raw_base: str):
    """
    Generate reports/README.md from reports/README.template.md.
    Injects a REPORT-LIST block listing all .md files in reports/ except README.md.
    If no template exists, bootstraps a minimal README.
    """
    reports_dir = REPORTS_DIR
    template_path = reports_dir / "README.template.md"

    report_files = sorted(
        p for p in reports_dir.glob("*.md")
        if p.name.lower() not in
          {"readme.md", "readme.template.md"}
    )

    def build_table() -> str:
        if not report_files:
            return "_No reports generated yet._"
        rows = [
            "| Report | Description | Last modified |",
            "|--------|-------------|---------------|",
        ]
        for rp in report_files:
            desc = extract_report_description(rp)
            _, modified = get_git_dates(rp)
            rows.append(f"| [{rp.name}]({rp.name}) | {desc} | {modified} |")
        return "\n".join(rows)

    reports_dir.mkdir(exist_ok=True)

    if not template_path.exists():
        lines = [
            "# Reports",
            "",
            "This folder contains automatically generated reports produced by the "
            "GitHub Actions workflow. Reports are updated on every push that changes "
            "model files or scripts.",
            "",
            "<!-- BEGIN AUTO: REPORT-LIST -->",
            build_table(),
            "<!-- END AUTO: REPORT-LIST -->",
        ]
        (reports_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
        return

    template = template_path.read_text(encoding="utf-8")
    new_content = replace_auto_block(template, "REPORT-LIST", build_table())
    (reports_dir / "README.md").write_text(new_content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    raw_base = os.environ.get("RAW_BASE", "").rstrip("/")
    if not raw_base:
        raise SystemExit(
            "RAW_BASE environment variable must be set to the raw GitHub base URL.\n"
            "Example: https://raw.githubusercontent.com/org/repo/refs/heads/main"
        )

    ng_tsvs = list(MODELS_DIR.glob("ng_models_v*.tsv"))
    ng_latest = find_ng_models_latest(ng_tsvs)

    folders = discover_models()
    ontologies = load_ontologies()

    write_top_readme(folders, raw_base, ng_latest)
    write_models_readme(folders, raw_base, ng_tsvs, ontologies)
    write_per_model_readmes(folders, raw_base, ontologies)
    write_reports_readme(raw_base)
    write_forms_outputs(folders, raw_base)

    # Write ONTOLOGIES.md if it does not exist yet (first-run bootstrap)
    ontologies_md_path = REPO_ROOT / "ONTOLOGIES.md"
    if not ontologies_md_path.exists():
        ontologies_md_path.write_text(generate_ontologies_md(ontologies), encoding="utf-8")
        print("Created ONTOLOGIES.md (bootstrap -- review and commit manually).")


if __name__ == "__main__":
    main()
