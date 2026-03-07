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
NG_MERMAID_FILE = MODELS_DIR / "ng_models_mermaid.mmd"
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

EXCLUDED_FOLDERS = {"old_samples"}


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
# README writers
# ---------------------------------------------------------------------------

def read_mermaid_block() -> str:
    if NG_MERMAID_FILE.exists():
        text = NG_MERMAID_FILE.read_text(encoding="utf-8").strip()
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

    mermaid_block = read_mermaid_block() if ng_latest else "_Mermaid diagram not available yet._"
    content = replace_auto_block(template, "NG-MODEL-VISUAL", mermaid_block)
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
        if p.name.lower() != "readme.md"
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
            raw_link = f"{raw_base}/{rp.relative_to(REPO_ROOT).as_posix()}"
            rows.append(f"| [{rp.name}]({raw_link}) | {desc} | {modified} |")
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

    # Write ONTOLOGIES.md if it does not exist yet (first-run bootstrap)
    ontologies_md_path = REPO_ROOT / "ONTOLOGIES.md"
    if not ontologies_md_path.exists():
        ontologies_md_path.write_text(generate_ontologies_md(ontologies), encoding="utf-8")
        print("Created ONTOLOGIES.md (bootstrap -- review and commit manually).")


if __name__ == "__main__":
    main()
