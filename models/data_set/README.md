# Data set

![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen)

This folder contains versioned model files for use with the [National Gallery Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/). Models are expressed as tab-separated triples aligned to CIDOC CRM and related extension ontologies.

## Ontologies

See [`ONTOLOGIES.md`](../ONTOLOGIES.md) for full version details, source links, and compatibility notes. Ontologies currently in use:

| Ontology | Version | Prefix |
|----------|---------|--------|
| [CIDOC CRM](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html) | 7.1.3 | `crm` |
| [CRMdig](https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v4.0.html) | 4.0 | `crmdig` |
| [CRMsci](https://cidoc-crm.org/crmsci/ModelVersion/crmsci-3.0) | 3.0 | `crmsci` |
| [ResearchSpace](https://github.com/researchspace/researchspace) | _see notes_ | `rs` |

## Model versions

<details>
<summary><strong>Data set</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/data_set/data_set_v0.1.tsv">v0.1</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v0.1 | 2026-04-11 | 2026-04-12 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/data_set/data_set_v0.1.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/data_set`](../models/data_set/) | [v0.1](https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/data_set/data_set_v0.1.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/data_set/data_set_v0.1.tsv)

This model records a digital dataset produced by a heritage science observation event. It captures identification, description, dataset typing, rights and access conditions, version information, and links to constituent file records or file groups. Links back to the generating observation event and optionally to a method or protocol document. Raw-to-processed dataset relationships are not modelled here; these will be handled by a future data_processing event model or resolved at the digital_file level.

_A digital dataset produced as the output of a scientific or technical observation event. Covers the full range of digital outputs in heritage science including images, spectra, elemental maps, numerical datasets, and documentary records. May incorporate individual file records or grouped collections of files. Versioning is supported via a version number and links to related dataset versions._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| ✓ | Persistent Identifier (PID) | PID; DOI; Dataset ID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | A globally unique and persistent identifier for this dataset, such as a DOI, ARK, or handle. Supports citation and long-term discovery. |
| ✓ | Unique System Label or ID | System Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Dataset Title | Title | E35 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A human-readable title for this dataset, suitable for display in interfaces and publications. |
| Optional | Repository Record URL | Repository URL; External Deposit URL | E42 |  | A URL pointing to an external repository record for this dataset, such as a Zenodo, B2SHARE, or institutional repository deposit. Use where the dataset or a copy of it has been deposited externally. Distinct from the preferred PID. |
| Optional | Description | Abstract | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A concise description or abstract of the dataset content, scope, and any notable features relevant to its interpretation or reuse. |
| ✓ | Dataset Type | -- | E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The type of data output represented by this dataset (e.g., XRF spectrum, Raman spectrum, FORS spectrum, EDS map, multispectral image stack, X-radiograph, IRR image, numerical dataset, documentary record). |
| Optional | Technique Type | Technique; Method Type | E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The analytical or imaging technique used to produce this dataset at a summary classification level (e.g., XRF, Raman spectroscopy, FORS, IRR, X-radiography, optical microscopy). Provides a discovery-level term. Fuller procedural detail is recorded in the linked method or protocol document. |
| Optional | Keywords | -- | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | Subject or content keywords supporting discovery. May be drawn from a controlled vocabulary or entered as free text. |
| Optional | Licence URL | -- | E42 |  | A URL pointing to the licence under which this dataset is made available (e.g., https://creativecommons.org/licenses/by/4.0/). Preferred over a licence statement where a standard licence URL exists. |
| Optional | Licence Statement | -- | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A free-text licence statement for cases where no standard licence URL is available. Use the Licence URL field in preference where possible. |
| ✓ | Access Status | -- | E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The access status of this dataset. Drawn from a controlled list: open, restricted, embargoed. |
| Optional | Embargo End Date | -- | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The date on which an embargo on this dataset expires and the dataset becomes available under its stated licence. Only applicable where Access Status is embargoed. |
| Optional | Version Number | -- | E54 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The version number of this dataset. Increment when a new version of the dataset is created. Version ordering is established by this number or by the creation date of the associated observation event. |
| ✓* | Related Dataset Version | Related Version; Previous Version | P130_shows_features_of > D1 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Related dataset version -- used for version succession and related dataset links. Ordering established by version number or creation date. |
| ✓* | Observation Event | -- | P94i_was_created_by > S27 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The observation or examination event that produced this dataset. |
| ✓* | Method / Protocol | Method; Protocol | P33i_was_used_by > E29 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The method or protocol document used to produce this dataset. |
| ✓* | Related Document | Report | P70i_is_documented_in > E31 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | A document referencing or providing context for this dataset. |
| ✓ | Rights Holder | -- | E30 > E39 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The person or organisation holding rights over this dataset. Multiple rights holders are permitted. |
| ✓* | File Group or File Record | File Group; File Record | P165_incorporates > D1 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | A file group or individual file record incorporated within this dataset. File groups may be nested. |

_\* Required status could not be derived from the model and has been set to required by default. Please verify._

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
