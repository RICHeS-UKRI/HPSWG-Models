# Forms and Data Input Resources

This folder contains resources to support the design of forms and data input interfaces derived from the HPSWG semantic models. The materials here are intended for data managers, system implementers, and anyone planning how metadata will be captured in practice.

The semantic models in this repository define how heritage science data is structured and connected using CIDOC CRM. The resources in this folder translate that structure into a more accessible format, identifying which fields are relevant for data entry, their human-readable labels, alternative names, whether they are required or optional, and the expected mode of data entry.

## Field behaviour key

The Behaviour column in each field table uses colour-coded badges to indicate how a user is expected to interact with the field. The badges use the `//` prefix to indicate field behaviour, consistent with the `//field` directive syntax used in the source model files.

| Badge | Tag | Meaning |
|-------|-----|---------|
| ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | `free-text` | User types a value directly; no controlled format |
| ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | `list` | User selects from a pick list or dropdown |
| ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | `select` | User searches for and links to an existing entity record |
| ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | `pid` | User looks up or pastes an externally minted persistent identifier |
| ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | `system-id` | Value is pre-structured or auto-populated; user may edit if permitted |
| ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | `ingested` | Value arrives via a batch or import process; user does not enter directly |
| ![behaviour: Inherited](https://img.shields.io/badge/%2F%2F-Inherited-bc4c00) | `inherited` | Value is pre-filled from a parent entity; user may edit if needed |
| ![behaviour: Automatic](https://img.shields.io/badge/%2F%2F-Automatic-32383f) | `auto` | System-assigned read-only value; user cannot edit |

Fields without a behaviour badge have not yet been tagged. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidance on adding behaviour tags to a model.

## Contents

<!-- BEGIN AUTO: FORMS-LISTING -->
| Model | Field table |
|-------|-------------|
| Heritage object | [field-tables.md](field-tables.md#heritage-object) |
| Project | [field-tables.md](field-tables.md#project) |
| Sample | [field-tables.md](field-tables.md#sample) |
| Sample site | [field-tables.md](field-tables.md#sample-site) |
| Sample taking | [field-tables.md](field-tables.md#sample-taking) |
| Sampling activity | [field-tables.md](field-tables.md#sampling-activity) |
<!-- END AUTO: FORMS-LISTING -->

## Relationship to the models

The field tables in this folder are generated automatically from `//field` and `//field-via` directives embedded in the TSV model files. If a model does not yet contain these directives it will not appear here. The canonical source of truth remains the model TSV files -- if there is any discrepancy between a field table and its source model, the model takes precedence.

For guidance on how to add or edit `//field` and `//field-via` directives in a model, see [CONTRIBUTING.md](../CONTRIBUTING.md).
