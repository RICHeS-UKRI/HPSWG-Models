# Reports

This folder contains automatically generated reports produced by the GitHub Actions workflow on every push that changes model files or scripts. Reports are intended as working tools for model authors and contributors -- they are updated automatically and should not be edited by hand.

## Available reports

<!-- BEGIN AUTO: REPORT-LIST -->
| Report | Description | Last modified |
|--------|-------------|---------------|
| [consistency_report.md](consistency_report.md) | **Individual model files analysed:** 16 | 2026-03-25 |
<!-- END AUTO: REPORT-LIST -->

## Adding new reports

New report files placed in this folder will be listed here automatically on the next workflow run. To add a new report:

1. Add a script to `scripts/` that writes its output to `reports/<report-name>.md`
2. Add a step to `.github/workflows/update-readmes.yml` to run the script
3. The reports README will update automatically on the next push
