#!/usr/bin/env python3
"""
generate_overview.py
--------------------
Generates an inter-model overview diagram from //links directives in formed model TSVs.

Discovers all formed model TSVs (latest versioned TSV per folder, excluding
workflow folders and EXCLUDED_FOLDERS), parses each for its key entity and
//links directives, then writes two outputs:

  models/overview_mermaid.mmd         -- self-contained Mermaid diagram
  models/overview/overview_v*.tsv     -- Dynamic Modeller TSV (auto-versioned)
"""

import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
OVERVIEW_DIR = MODELS_DIR / "overview"
OVERVIEW_MMD = MODELS_DIR / "overview_mermaid.mmd"
OVERVIEW_LINK_FILE = MODELS_DIR / "overview_link.md"

OVERVIEW_LINK_FALLBACK_BASE = (
    "https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main"
)

EXCLUDED_FOLDERS = {"old_samples", "heritage_object_part_types", "frame", "frame_part", "overview"}
WORKFLOW_FOLDERS = {"workflows", "user_workflows"}

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")
SKIP_RE = re.compile(r"^\s*//")
SUBGRAPH_START_RE = re.compile(
    r"^\s*//subgraph(?:-(?:TB|TD|BT|RL|LR))?\s+Linked Entities", re.IGNORECASE
)
SUBGRAPH_ANY_START_RE = re.compile(
    r"^\s*//subgraph(?:-(?:TB|TD|BT|RL|LR))?\b", re.IGNORECASE
)
SUBGRAPH_END_RE = re.compile(r"^\s*//end", re.IGNORECASE)
LINKS_RE = re.compile(
    r"^\s*//links\s+(.+?)\s*-->\s*(.+?)\s*(\[confirmed\])?\s*$", re.IGNORECASE
)
INSTANCE_SUFFIX_RE = re.compile(r"#-\d+$")
CRM_CODE_RE = re.compile(r"^[A-Za-z]\d+(?:/[A-Za-z]\d+)*$")

# ---------------------------------------------------------------------------
# Format class mapping
# ---------------------------------------------------------------------------

CRM_CLASS_TO_FORMAT = {
    "E7": "event", "E9": "event", "E11": "event", "E12": "event",
    "E65": "event", "S2": "event", "S24": "event", "S27": "event",
    "E21": "actor", "E39": "actor", "E74": "actor",
    "E22": "object", "E18": "object", "E20": "object", "E70": "object", "E57": "object","E78": "object",
    "E26": "place", "E53": "place",
    "E31": "document", "E73": "document", "E29": "document",
    "E54": "dims",
    "E55": "type",
    "E41": "name",
    "E52": "period",
    "D1": "digital2", "D9": "digital2",
    "S13": "object", "S10": "object",
    "E94": "place2",
}


def class_code_to_format(code: str, blank_node: bool = False) -> str:
    """Map a CRM class code to a Dynamic Modeller format class string."""
    base = CRM_CLASS_TO_FORMAT.get(code.split("/")[0].strip(), "crm")
    suffix = "_bn" if blank_node else ""
    return f"{base}{suffix}-fs24"


def ontology_format_class(ref: str) -> str:
    """Determine the TSV format class for an ontology terminal node."""
    parts = ref.split(":", 1)
    if len(parts) < 2:
        return "digital2_bn-fs24"
    code = parts[1].strip()
    if CRM_CODE_RE.match(code):
        return class_code_to_format(code, blank_node=True)
    return "digital2_bn-fs24"


def format_class_to_mermaid_class(format_class: str) -> str:
    """Strip the -fs24 suffix to get the Mermaid classDef name."""
    return format_class.replace("-fs24", "")


# ---------------------------------------------------------------------------
# Hardcoded Mermaid preamble + full classDef block
# ---------------------------------------------------------------------------

MERMAID_PREAMBLE = """\
%%{init: {'flowchart': {'wrappingWidth': 600}}}%%
flowchart LR
classDef crm stroke:#333333,fill:#DCDCDC,color:#333333,rx:5px,ry:5px;
classDef thing stroke:#2C5D98,fill:#D0E5FF,color:#2C5D98,rx:5px,ry:5px;
classDef event stroke:#5C811F,fill:#5C811F,color:white,rx:5px,ry:5px;
classDef event_bn stroke:#4A6719,fill:#D0DDBB,color:#4A6719,rx:20px,ry:20px;
classDef object stroke:#2C5D98,fill:#2C5D98,color:white,rx:5px,ry:5px;
classDef object_bn stroke:#1E3F67,fill:#94abc5,color:#1E3F67,rx:20px,ry:20px;
classDef actor stroke:#4e4403,fill:#fdde29,color:#4e4403,rx:5px,ry:5px;
classDef actor_bn stroke:#564F26,fill:#ffee8c,color:#564F26,rx:20px,ry:20px;
classDef missing stroke:#A32D2D,fill:#FCEBEB,color:#501313,rx:5px,ry:5px;
classDef sg1 stroke:black,fill:#fefcf4,color:black,rx:10px,ry:10px;
classDef sg2 stroke:black,fill:#fffffb,color:black,rx:10px,ry:10px;
classDef sg2-5-10 stroke:black,fill:#fffffb,color:black,rx:10px,ry:10px,stroke-dasharray:5 10;
classDef sg2-5-2 stroke:black,fill:#fffffb,color:black,rx:10px,ry:10px,stroke-dasharray:5 2;
classDef idea stroke:#1f0e9a,fill:#1f0e9a,color:white,rx:5px,ry:5px;
classDef idea_bn stroke:#1f0e9a,fill:#e7e5f6,color:#1f0e9a,rx:20px,ry:20px;
classDef document stroke:#2C5D98,fill:#33B0FF,color:2C5D98,rx:5px,ry:5px;
classDef document_bn stroke:#1E3F67,fill:#B8E3FE,color:#1E3F67,rx:20px,ry:20px;
classDef type stroke:#502604,fill:#FAB565,color:#502604,rx:20px,ry:20px;
classDef dims stroke:#9A6D3B,fill:#9A6D3B,color:white,rx:5px,ry:5px;
classDef dims_bn stroke:#674928,fill:#d4bda4,color:#674928,rx:20px,ry:20px;
classDef place stroke:#bd4512,fill:#bd4512,color:white,rx:5px,ry:5px;
classDef place_bn stroke:#9D390F,fill:#eecaba,color:#9D390F,rx:20px,ry:20px;
classDef name stroke:#563800,fill:#FEF3BA,color:#563800,rx:20px,ry:20px;
classDef period stroke:#6340b1,fill:#6340b1,color:white,rx:5px,ry:5px;
classDef period_bn stroke:#6340b1,fill:#dacef5,color:#6340b1,rx:20px,ry:20px;
classDef url stroke:#2C5D98,fill:white,color:#2C5D98,rx:5px,ry:5px;
classDef note stroke:#2C5D98,fill:#D8FDFF,color:#2C5D98,rx:5px,ry:5px;
classDef literal stroke:black,fill:#f0f0e0,color:black,rx:2px,ry:2px,max-width:100px;
classDef base stroke:black,fill:white,color:black,rx:5px,ry:5px;
classDef event2 stroke:blue,fill:#96e0f6,color:black,rx:20px,ry:20px;
classDef object2 stroke:black,fill:#E1BA9C,color:black,rx:20px,ry:20px;
classDef actor2 stroke:black,fill:#FFBDCA,color:black,rx:20px,ry:20px;
classDef dims2 stroke:black,fill:#c6c6c6,color:black,rx:20px,ry:20px;
classDef digital2 stroke:#999,fill:#eee,color:black,rx:5px,ry:5px;
classDef type2 stroke:red,fill:#FAB565,color:black,rx:20px,ry:20px;
classDef name2 stroke:orange,fill:#FEF3BA,color:black,rx:20px,ry:20px;
classDef infoobj stroke:#907010,fill:#fffa40,color:black,rx:20px,ry:20px;
classDef timespan stroke:blue,fill:#ddfffe,color:black,rx:20px,ry:20px;
classDef place2 stroke:#3a7a3a,fill:#aff090,color:black,rx:20px,ry:20px;
classDef classstyle stroke:black,fill:white,color:black,rx:5px,ry:5px;"""


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ModelInfo:
    folder: str
    key_entity: Optional[str]                       # e.g. "E22: Heritage Object"
    key_class_code: Optional[str] = None            # e.g. "E22" or "E22/S13"
    links: List[Tuple[str, str]] = field(default_factory=list)
    # links: list of (entity_label, target_raw)
    # target_raw is either a folder name or ontology ref (e.g. "crm:E31")


# ---------------------------------------------------------------------------
# Helpers shared with check_consistency.py
# ---------------------------------------------------------------------------

def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
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
    parts = name.split(":", 1)
    if len(parts) < 2:
        return None
    candidate = parts[0].strip()
    if re.match(r"^[A-Za-z][A-Za-z0-9_/]*$", candidate):
        return candidate
    return None


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
    """Return True if target is an ontology reference like 'crm:E31' or 'rs:EX_Digital_Image'."""
    return ":" in target


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


def discover_model_folders() -> List[Path]:
    """Return latest TSV paths for all formed model folders, excluding workflows and excluded folders."""
    if not MODELS_DIR.exists():
        return []
    result = []
    for child in sorted(MODELS_DIR.iterdir()):
        if not child.is_dir():
            continue
        if child.name in EXCLUDED_FOLDERS:
            continue
        if child.name in WORKFLOW_FOLDERS:
            continue
        latest = latest_tsv_in_folder(child)
        if latest is not None:
            result.append(latest)
    return result


# ---------------------------------------------------------------------------
# TSV parsing
# ---------------------------------------------------------------------------

def parse_model_tsv(tsv_path: Path) -> ModelInfo:
    folder = tsv_path.parent.name
    key_entity: Optional[str] = None
    key_class_code: Optional[str] = None
    links: List[Tuple[str, str]] = []

    try:
        lines = tsv_path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"Warning: could not read {tsv_path}: {e}", file=sys.stderr)
        return ModelInfo(folder=folder, key_entity=None)

    linked_depth = 0
    nested_depth = 0

    for line in lines:
        # Track Linked Entities subgraph depth
        if SUBGRAPH_START_RE.match(line):
            linked_depth = 1
            continue

        if linked_depth > 0 and not SUBGRAPH_START_RE.match(line) and SUBGRAPH_ANY_START_RE.match(line):
            nested_depth += 1
            continue

        if SUBGRAPH_END_RE.match(line):
            if linked_depth > 0:
                if nested_depth > 0:
                    nested_depth -= 1
                else:
                    linked_depth = 0
            continue

        # Parse //links directives (at any depth inside or outside Linked Entities block)
        links_match = LINKS_RE.match(line)
        if links_match:
            entity_label = strip_instance_suffix(links_match.group(1).strip())
            targets = parse_targets(links_match.group(2))
            for target in targets:
                links.append((entity_label, target))
            continue

        # Skip remaining comment/directive lines
        if SKIP_RE.match(line):
            continue

        # Only interested in the key entity (outside Linked Entities block)
        if linked_depth > 0:
            continue

        parts = line.split("\t")
        if len(parts) < 2:
            continue

        subj_raw = parts[0].strip()
        pred = parts[1].strip().lower()
        if not subj_raw or not pred:
            continue

        # Skip metadata/tooltip predicates when looking for key entity
        if pred in ("has note", "from list", "tooltip"):
            continue

        canonical = strip_instance_suffix(subj_raw)
        if extract_class_code(canonical) is None:
            continue

        if key_entity is None:
            key_entity = canonical
            key_class_code = extract_class_code(canonical)

    return ModelInfo(folder=folder, key_entity=key_entity, key_class_code=key_class_code, links=links)


# ---------------------------------------------------------------------------
# Node ID sanitisation
# ---------------------------------------------------------------------------

def sanitise_id(name: str) -> str:
    """Convert a name to a valid Mermaid/TSV node ID (alphanumeric and underscore only)."""
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)


def ontology_node_id(ref: str) -> str:
    """crm:E31 -> crm_E31, rs:EX_Digital_Image -> rs_EX_Digital_Image"""
    return sanitise_id(ref)


# ---------------------------------------------------------------------------
# Graph building
# ---------------------------------------------------------------------------

def build_graph(
    models: List[ModelInfo],
) -> Tuple[
    Dict[str, Optional[str]],          # repo_nodes: folder -> key_entity
    Dict[str, Optional[str]],          # repo_class_codes: folder -> key_class_code
    Dict[str, str],                     # ontology_nodes: node_id -> original_ref
    Set[str],                           # missing_nodes: sanitised target names
    List[Tuple[str, str, str]],         # edges: (source_id, label, target_id)
]:
    """
    Classify all nodes and collect edges from the parsed model data.

    Returns:
      repo_nodes      -- all discovered model folders (with key entities)
      repo_class_codes -- key entity class code per folder
      ontology_nodes  -- ontology ref targets (node_id -> original ref string)
      missing_nodes   -- declared folder targets not present in the repo
      edges           -- (source_node_id, entity_label, target_node_id)
    """
    all_folders: Set[str] = {m.folder for m in models}

    repo_nodes: Dict[str, Optional[str]] = {m.folder: m.key_entity for m in models}
    repo_class_codes: Dict[str, Optional[str]] = {m.folder: m.key_class_code for m in models}
    ontology_nodes: Dict[str, str] = {}
    missing_nodes: Set[str] = set()
    edges: List[Tuple[str, str, str]] = []

    for model in models:
        src_id = model.folder
        for entity_label, target_raw in model.links:
            if is_ontology_ref(target_raw):
                tgt_id = ontology_node_id(target_raw)
                ontology_nodes[tgt_id] = target_raw
            elif target_raw.lower() in {f.lower() for f in all_folders}:
                # Resolve case-insensitively to the actual folder name
                tgt_id = next(
                    f for f in all_folders if f.lower() == target_raw.lower()
                )
            else:
                tgt_id = sanitise_id(target_raw)
                missing_nodes.add(tgt_id)

            edges.append((src_id, entity_label, tgt_id))

    return repo_nodes, repo_class_codes, ontology_nodes, missing_nodes, edges


# ---------------------------------------------------------------------------
# Mermaid output
# ---------------------------------------------------------------------------

def _mermaid_escape_label(text: str) -> str:
    """Wrap a label in double quotes, escaping any internal double quotes."""
    return '"' + text.replace('"', '#quot;') + '"'


def generate_mermaid(
    repo_nodes: Dict[str, Optional[str]],
    repo_class_codes: Dict[str, Optional[str]],
    ontology_nodes: Dict[str, str],
    missing_nodes: Set[str],
    edges: List[Tuple[str, str, str]],
) -> str:
    lines = [MERMAID_PREAMBLE, ""]

    # --- Node declarations ---
    for folder, key_entity in sorted(repo_nodes.items()):
        node_id = folder
        code = repo_class_codes.get(folder) or ""
        fmt = class_code_to_format(code) if code else "crm-fs24"
        mermaid_class = format_class_to_mermaid_class(fmt)
        label_line1 = key_entity if key_entity else folder
        label_line2 = folder
        display = f"{label_line1}\\n{label_line2}"
        lines.append(f'  {node_id}["{display}"]:::{mermaid_class}')

    for node_id, original_ref in sorted(ontology_nodes.items()):
        fmt = ontology_format_class(original_ref)
        mermaid_class = format_class_to_mermaid_class(fmt)
        lines.append(f'  {node_id}["{original_ref}"]:::{mermaid_class}')

    for node_id in sorted(missing_nodes):
        lines.append(f'  {node_id}["{node_id}"]:::missing')

    lines.append("")

    # --- Edges (using ---->|"label"| fix syntax) ---
    for src_id, label, tgt_id in edges:
        quoted = _mermaid_escape_label(label)
        lines.append(f"  {src_id} ---->|{quoted}|{tgt_id}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# TSV output
# ---------------------------------------------------------------------------

def generate_tsv(
    repo_nodes: Dict[str, Optional[str]],
    repo_class_codes: Dict[str, Optional[str]],
    ontology_nodes: Dict[str, str],
    missing_nodes: Set[str],
    edges: List[Tuple[str, str, str]],
) -> str:
    lines = ["// Overview", "//Flowchart LR fix"]

    # --- Node declarations (tooltip + format class, first mention only) ---
    for folder, key_entity in sorted(repo_nodes.items()):
        label = key_entity if key_entity else folder
        code = repo_class_codes.get(folder) or ""
        fmt = class_code_to_format(code) if code else "crm-fs24"
        lines.append(f"{folder}\ttooltip\t{label}\t{fmt}|")

    for node_id, original_ref in sorted(ontology_nodes.items()):
        fmt = ontology_format_class(original_ref)
        lines.append(f"{node_id}\ttooltip\t{original_ref}\t{fmt}|")

    for node_id in sorted(missing_nodes):
        lines.append(f"{node_id}\ttooltip\t{node_id}\tmissing-5-5|")

    # --- Edges ---
    for src_id, label, tgt_id in edges:
        lines.append(f"{src_id}\t{label}\t{tgt_id}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# TSV version management
# ---------------------------------------------------------------------------

def latest_overview_version(tsv_dir: Path) -> Optional[Tuple[Tuple[int, ...], Path]]:
    """Return (version_tuple, path) for the latest overview TSV, or None."""
    files = []
    for p in tsv_dir.glob("overview_v*.tsv"):
        m = VERSION_RE.search(p.name)
        if m:
            ver = tuple(int(x) for x in m.group(1).split("."))
            files.append((ver, p))
    if not files:
        return None
    return max(files, key=lambda vp: vp[0])


def next_minor_version(ver: Tuple[int, ...]) -> Tuple[int, ...]:
    """Increment the last component: (1, 0) -> (1, 1), (2, 3) -> (2, 4)."""
    return ver[:-1] + (ver[-1] + 1,)


def version_str(ver: Tuple[int, ...]) -> str:
    return ".".join(str(x) for x in ver)


def write_overview_tsv(tsv_dir: Path, content: str) -> Optional[Path]:
    """
    Write a new versioned overview TSV if content has changed.
    Returns the path written, or None if content was unchanged.
    """
    tsv_dir.mkdir(exist_ok=True)

    latest = latest_overview_version(tsv_dir)
    if latest is not None:
        existing_ver, existing_path = latest
        existing_content = existing_path.read_text(encoding="utf-8")
        if existing_content == content:
            return None
        new_ver = next_minor_version(existing_ver)
    else:
        new_ver = (1, 0)

    filename = f"overview_v{version_str(new_ver)}.tsv"
    out_path = tsv_dir / filename
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Overview link file
# ---------------------------------------------------------------------------

def write_overview_link(tsv_path: Path) -> None:
    """Write models/overview_link.md with a Dynamic Modeller link to tsv_path."""
    raw_base = os.environ.get("RAW_BASE", "").rstrip("/") or OVERVIEW_LINK_FALLBACK_BASE
    rel = tsv_path.relative_to(REPO_ROOT).as_posix()
    raw_url = f"{raw_base}/{rel}"
    modeller_url = f"https://research.nationalgallery.org.uk/lab/modelling/?url={raw_url}"
    OVERVIEW_LINK_FILE.write_text(f"[Open in Dynamic Modeller]({modeller_url})\n", encoding="utf-8")
    print(f"Overview link written to {OVERVIEW_LINK_FILE.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    tsv_paths = discover_model_folders()
    if not tsv_paths:
        print("No formed model TSVs found. Exiting.")
        sys.exit(0)

    print(f"Found {len(tsv_paths)} formed model(s). Parsing...")

    models = [parse_model_tsv(p) for p in tsv_paths]

    repo_nodes, repo_class_codes, ontology_nodes, missing_nodes, edges = build_graph(models)

    print(
        f"  Repo model nodes:     {len(repo_nodes)}\n"
        f"  Ontology terminals:   {len(ontology_nodes)}\n"
        f"  Missing targets:      {len(missing_nodes)}\n"
        f"  Edges:                {len(edges)}"
    )

    # Write Mermaid
    mermaid_content = generate_mermaid(repo_nodes, repo_class_codes, ontology_nodes, missing_nodes, edges)
    OVERVIEW_MMD.write_text(mermaid_content, encoding="utf-8")
    print(f"Mermaid diagram written to {OVERVIEW_MMD.relative_to(REPO_ROOT)}")

    # Write TSV (versioned)
    tsv_content = generate_tsv(repo_nodes, repo_class_codes, ontology_nodes, missing_nodes, edges)
    written = write_overview_tsv(OVERVIEW_DIR, tsv_content)
    if written:
        current_tsv = written
        print(f"Overview TSV written to {written.relative_to(REPO_ROOT)}")
    else:
        print("Overview TSV unchanged -- no new version written.")
        latest = latest_overview_version(OVERVIEW_DIR)
        current_tsv = latest[1] if latest else None

    # Write companion link file
    if current_tsv is not None:
        write_overview_link(current_tsv)

    if missing_nodes:
        print(f"\nNote: {len(missing_nodes)} declared target(s) not found in repo: "
              + ", ".join(sorted(missing_nodes)))


if __name__ == "__main__":
    main()
