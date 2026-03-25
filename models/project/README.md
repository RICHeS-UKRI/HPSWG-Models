# Project

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
<summary><strong>Project</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.3.tsv">v1.3</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.3 | 2026-03-07 | 2026-03-20 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.3.tsv) |
|  | v1.2 | 2026-03-07 | 2026-03-19 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.2.tsv) |
|  | v1.1 | 2026-03-07 | 2026-03-17 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.0.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/project`](../models/project/) | [v1.3](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.3.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.3.tsv)

This model defines a Project (E7) as a high-level activity used to group and manage related work (e.g., sampling campaigns, research initiatives, surveys). It brings together identifiers, title, ownership and participation, a short descriptive summary, dates/time-span, related documentation, and simple status/type flags. Projects may optionally sit within a broader parent project or programme.

_An organised activity or campaign with a defined purpose, scope, ownership, and timeframe. In practice this may represent a research project, survey, or documentation campaign._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| Optional | Persistent Identifier (PID) | Project ID; PID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Optional public unique identifier for the project. |
| ✓ | Unique System Label or ID | Database or System ID/Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Project Title | Name | E35 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Human-readable title for the project or campaign. |
| ✓ | Project Owner | Responsible Institution or Person | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The primary organisation or individual responsible for the project. |
| Optional | Other Actors | Contributors; Collaborators | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Other individuals or organisations involved in the project. |
| ✓ | Project Description | Summary; Scope | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Short description outlining the purpose and scope of the project. |
| ✓ | Project Dates | Start Date; End Date | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The timeframe during which the project was active. |
| Optional | Related Documents | Reports; Publications; Proposals | E31 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Documents associated with the project. |
| Optional | Parent Project | Programme; Umbrella Project | E7 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A broader project or programme within which this project is situated. Note: sometimes treated as E89 Propositional Object in other mappings, but can be implemented as E7 Activity in ResearchSpace. |
| ✓ | Project Type | Campaign; Research Project; Survey | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | A simple classification describing the nature of the project. |
| ✓ | condition state type | Planned; Ongoing; Completed; Legacy | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | Indicates the current state or completion level of the project. |

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
