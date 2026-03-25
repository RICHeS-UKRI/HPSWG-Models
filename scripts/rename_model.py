#!/usr/bin/env python3
"""
rename_model.py -- Reusable model folder rename utility for HPSWG-Models.

Usage:
    python scripts/rename_model.py --dry-run   # Report only, no changes made
    python scripts/rename_model.py             # Execute all changes

Run from the repository root.

Edit the RENAMES list below before each use.
Each entry is a tuple of (old_folder_name, new_folder_name).
"""

import argparse
import csv
import io
import os
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION -- edit this list before each run
# ---------------------------------------------------------------------------

RENAMES = [
    #("production_event", "production"),
    #("sample_taking_event", "sample_taking"),
    #("sampling_event", "sampling_activity"),
    #("sample_imaging_event", "sample_imaging"),
    #("sample_preparation_event", "sample_preparation"),
]

# ---------------------------------------------------------------------------
# PATHS -- relative to repository root
# ---------------------------------------------------------------------------

MODELS_DIR = Path("models")
MANIFEST_PATH = Path("conversion_manifest.csv")
SCRIPTS_DIR = Path("scripts")

# README template files to scan for manual-review hits
README_TEMPLATES = [
    Path("README.template.md"),
    Path("models/README.template.md"),
    Path("reports/README.template.md"),
    Path("forms/README.template.md"),
    Path("CONTRIBUTING.md"),
]

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def find_ng_models_tsv():
    """Return the path to the latest ng_models_v*.tsv file, or None."""
    candidates = sorted(MODELS_DIR.glob("ng_models_v*.tsv"))
    return candidates[-1] if candidates else None


def all_tsv_files(exclude_folder=None):
    """Yield all .tsv files under MODELS_DIR, optionally skipping one folder."""
    for tsv in MODELS_DIR.rglob("*.tsv"):
        if exclude_folder and tsv.parts[1] == exclude_folder:
            continue
        yield tsv


def run_git_mv(src, dst, dry_run):
    """Execute or report a git mv operation."""
    if dry_run:
        return f"  [git mv] {src} --> {dst}"
    result = subprocess.run(
        ["git", "mv", str(src), str(dst)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return f"  [ERROR] git mv {src} --> {dst}\n    {result.stderr.strip()}"
    return f"  [done]  git mv {src} --> {dst}"


def search_tsv_content(tsv_path, old_name):
    """
    Search a TSV file for content references to old_name.
    Returns list of (line_number, line_content) for hits.
    Targets: node labels, has note values, Document Note: text.
    Excludes //links lines (those are handled separately).
    """
    hits = []
    try:
        lines = tsv_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return hits
    pattern = re.compile(re.escape(old_name), re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        if line.startswith("//links"):
            continue
        if pattern.search(line):
            hits.append((i, line.rstrip()))
    return hits


def find_links_references(tsv_path, old_name):
    """
    Find //links lines in a TSV file that reference old_name as a target.
    Returns list of (line_number, line_content) for hits.
    """
    hits = []
    try:
        lines = tsv_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return hits
    # Match: --> old_name optionally followed by comma, space, [confirmed], or end
    pattern = re.compile(
        r"(//links\s+.*?-->\s*(?:[^,\n]*,\s*)*)(" + re.escape(old_name) + r")(\s*(?:,|or|\[confirmed\]|$).*)",
        re.IGNORECASE
    )
    for i, line in enumerate(lines, 1):
        if pattern.search(line):
            hits.append((i, line.rstrip()))
    return hits


def replace_links_in_file(tsv_path, old_name, new_name, dry_run):
    """
    Replace //links references to old_name with new_name in a TSV file.
    Returns (changed: bool, new_content: str).
    """
    try:
        content = tsv_path.read_text(encoding="utf-8")
    except Exception:
        return False, ""
    pattern = re.compile(
        r"(//links\s+.*?-->\s*(?:[^,\n]*,\s*)*)(" + re.escape(old_name) + r")(\b.*)",
        re.IGNORECASE
    )
    new_content, count = pattern.subn(
        lambda m: m.group(1) + new_name + m.group(3),
        content
    )
    if count > 0 and not dry_run:
        tsv_path.write_text(new_content, encoding="utf-8")
    return count > 0, new_content


def update_manifest(manifest_path, old_name, new_name, dry_run):
    """
    Update proposed_output_path and notes columns in conversion_manifest.csv.
    Returns list of (row_number, old_path, new_path) for reporting.
    """
    changes = []
    try:
        content = manifest_path.read_text(encoding="utf-8")
        reader = csv.DictReader(io.StringIO(content))
        rows = list(reader)
        fieldnames = reader.fieldnames
    except Exception as e:
        return [(-1, str(e), "")]

    old_prefix = f"models/{old_name}/"
    new_prefix = f"models/{new_name}/"
    rename_note = f"renamed from {old_name}"

    updated_rows = []
    for i, row in enumerate(rows, 2):  # row 1 is header
        old_path = row.get("proposed_output_path", "")
        if old_prefix in old_path:
            # Replace folder name and filename stem in one pass
            # e.g. models/production_event/production_event_v1.0.tsv
            #   -> models/production/production_v1.0.tsv
            new_path = old_path.replace(old_prefix, new_prefix)
            # Now replace old_name stem within the filename portion
            path_obj = Path(new_path)
            new_stem = path_obj.stem.replace(old_name, new_name)
            new_path = str(path_obj.parent / (new_stem + path_obj.suffix))
            existing_notes = row.get("notes", "")
            new_notes = (existing_notes + f"; {rename_note}").lstrip("; ")
            changes.append((i, old_path, new_path))
            row["proposed_output_path"] = new_path
            row["notes"] = new_notes
        updated_rows.append(row)

    if changes and not dry_run:
        output = io.StringIO()
        writer = csv.DictWriter(
            output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(updated_rows)
        manifest_path.write_text(output.getvalue(), encoding="utf-8")

    return changes


def search_readme_templates(old_name):
    """
    Search README template files for references to old_name.
    Returns dict of {path: [(line_num, line)]} for hits.
    """
    results = {}
    pattern = re.compile(re.escape(old_name), re.IGNORECASE)
    for template in README_TEMPLATES:
        if not template.exists():
            continue
        hits = []
        for i, line in enumerate(template.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                hits.append((i, line.rstrip()))
        if hits:
            results[template] = hits
    return results


# ---------------------------------------------------------------------------
# MAIN REPORT / EXECUTION
# ---------------------------------------------------------------------------

def process_rename(old_name, new_name, dry_run, summary):
    """Process a single rename pair. Appends to summary dict."""

    mode = "DRY RUN -- " if dry_run else ""
    print(f"\n{'=' * 70}")
    print(f"{mode}RENAME: {old_name}  -->  {new_name}")
    print(f"{'=' * 70}")

    old_folder = MODELS_DIR / old_name
    new_folder = MODELS_DIR / new_name

    # ------------------------------------------------------------------
    # 1. Check source folder exists
    # ------------------------------------------------------------------
    if not old_folder.exists():
        print(f"\n  [SKIP] Folder not found: {old_folder}")
        summary["skipped"].append(old_name)
        return

    # ------------------------------------------------------------------
    # 2. Folder and file renames
    # ------------------------------------------------------------------
    print(f"\n--- 1. Folder and file renames ---")

    git_ops = []

    # Snapshot folder contents before any git mv operations
    # (used later for manifest untracked-file check)
    files_in_folder = sorted(old_folder.iterdir())
    for f in files_in_folder:
        if f.name == "README.md":
            # Auto-generated; will be rebuilt by the Action -- skip
            continue
        new_stem = f.stem.replace(old_name, new_name)
        new_filename = new_stem + f.suffix
        git_ops.append((f, old_folder / f.name, old_folder / new_filename))

    # Execute file renames first
    for original, src, dst in git_ops:
        if src != dst:
            msg = run_git_mv(src, dst, dry_run)
            print(msg)
            summary["git_ops"] += 1

    # Then rename the folder itself
    msg = run_git_mv(old_folder, new_folder, dry_run)
    print(msg)
    summary["git_ops"] += 1

    # ------------------------------------------------------------------
    # 3. //links references in other TSV files
    # ------------------------------------------------------------------
    print(f"\n--- 2. //links references in other TSV files ---")

    links_found = False
    for tsv in all_tsv_files(exclude_folder=old_name):
        hits = find_links_references(tsv, old_name)
        if hits:
            links_found = True
            changed, _ = replace_links_in_file(tsv, old_name, new_name, dry_run)
            for lineno, line in hits:
                action = "[will update]" if dry_run else "[updated]"
                print(f"  {action} {tsv}  line {lineno}:")
                print(f"    {line}")
            summary["links_updated"] += len(hits)

    # Also check ng_models TSV
    ng_tsv = find_ng_models_tsv()
    if ng_tsv:
        hits = find_links_references(ng_tsv, old_name)
        if hits:
            links_found = True
            replace_links_in_file(ng_tsv, old_name, new_name, dry_run)
            for lineno, line in hits:
                action = "[will update]" if dry_run else "[updated]"
                print(f"  {action} {ng_tsv}  line {lineno}:")
                print(f"    {line}")
            summary["links_updated"] += len(hits)

    if not links_found:
        print(f"  [none found]")

    # ------------------------------------------------------------------
    # 4. conversion_manifest.csv
    # ------------------------------------------------------------------
    print(f"\n--- 3. conversion_manifest.csv ---")

    manifest_changes = update_manifest(MANIFEST_PATH, old_name, new_name, dry_run)
    if manifest_changes:
        for rownum, old_path, new_path in manifest_changes:
            if rownum == -1:
                print(f"  [ERROR] {old_path}")
            else:
                action = "[will update]" if dry_run else "[updated]"
                print(f"  {action} row {rownum}:")
                print(f"    {old_path}")
                print(f"    --> {new_path}")
        summary["manifest_rows"] += len([c for c in manifest_changes if c[0] != -1])
    else:
        print(f"  [none found]")

    # Warn about files in the folder that have no manifest entry
    try:
        manifest_content = MANIFEST_PATH.read_text(encoding="utf-8")
        covered_paths = set(
            row["proposed_output_path"]
            for row in csv.DictReader(io.StringIO(manifest_content))
        )
    except Exception:
        covered_paths = set()

    untracked = []
    for f in files_in_folder:
        if f.name == "README.md":
            continue
        expected_old = f"models/{old_name}/{f.name}"
        if expected_old not in covered_paths:
            new_stem = f.stem.replace(old_name, new_name)
            expected_new = f"models/{new_name}/{new_stem}{f.suffix}"
            untracked.append((f.name, expected_new))

    if untracked:
        print(f"\n  [WARNING] Files in folder with no manifest entry -- add manually:")
        for fname, new_path in untracked:
            print(f"    {fname}  -->  {new_path}")
        summary["manifest_warnings"] += len(untracked)

    # ------------------------------------------------------------------
    # 5. TSV content hits for manual review (node labels, has note, etc.)
    # ------------------------------------------------------------------
    print(f"\n--- 4. TSV content -- manual review required ---")

    content_hits_found = False
    # Search the renamed folder's own TSV files (using new path if not dry run)
    search_folder = old_folder if dry_run else new_folder
    if search_folder.exists():
        for tsv in sorted(search_folder.glob("*.tsv")):
            hits = search_tsv_content(tsv, old_name)
            if hits:
                content_hits_found = True
                print(f"  [review] {tsv}:")
                for lineno, line in hits:
                    print(f"    line {lineno}: {line[:120]}")
                summary["manual_review"] += len(hits)

    if not content_hits_found:
        print(f"  [none found]")

    # ------------------------------------------------------------------
    # 6. README template hits for manual review
    # ------------------------------------------------------------------
    print(f"\n--- 5. README templates -- manual review required ---")

    template_hits = search_readme_templates(old_name)
    if template_hits:
        for path, hits in template_hits.items():
            print(f"  [review] {path}:")
            for lineno, line in hits:
                print(f"    line {lineno}: {line[:120]}")
        summary["manual_review"] += sum(len(h) for h in template_hits.values())
    else:
        print(f"  [none found]")


def main():
    parser = argparse.ArgumentParser(
        description="Rename HPSWG-Models model folders with git history preservation."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report all changes without executing them."
    )
    args = parser.parse_args()

    # Check we are running from the repository root
    if not MODELS_DIR.exists() or not MANIFEST_PATH.exists():
        print(
            "ERROR: Run this script from the repository root.\n"
            f"  Expected to find: {MODELS_DIR}/  and  {MANIFEST_PATH}"
        )
        sys.exit(1)

    dry_run = args.dry_run

    print(f"\nHPSWG-Models rename utility")
    print(f"Mode: {'DRY RUN (no changes will be made)' if dry_run else 'EXECUTE'}")
    print(f"Pairs to process: {len(RENAMES)}")

    summary = {
        "git_ops": 0,
        "links_updated": 0,
        "manifest_rows": 0,
        "manifest_warnings": 0,
        "manual_review": 0,
        "skipped": [],
    }

    for old_name, new_name in RENAMES:
        process_rename(old_name, new_name, dry_run, summary)

    # ------------------------------------------------------------------
    # Final summary
    # ------------------------------------------------------------------
    print(f"\n{'=' * 70}")
    print(f"SUMMARY ({'DRY RUN' if dry_run else 'EXECUTED'})")
    print(f"{'=' * 70}")
    print(f"  git mv operations : {summary['git_ops']}")
    print(f"  //links updated   : {summary['links_updated']}")
    print(f"  manifest rows     : {summary['manifest_rows']}")
    if summary["manifest_warnings"]:
        print(f"  manifest warnings : {summary['manifest_warnings']} files not in manifest -- add manually")
    print(f"  manual review hits: {summary['manual_review']}")
    if summary["skipped"]:
        print(f"  skipped (not found): {', '.join(summary['skipped'])}")
    if dry_run:
        print(f"\nNo changes were made. Run without --dry-run to execute.")
    else:
        print(f"\nAll automated changes complete.")
        if summary["manual_review"] > 0:
            print(f"  Review the items flagged above before committing.")
        print(f"  Stage and commit with: git add -A && git commit -m 'rename: model folder renames'")


if __name__ == "__main__":
    main()
