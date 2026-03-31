# Sampling activity

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
<summary><strong>Sampling activity</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.2.tsv">v1.2</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.2 | 2026-03-23 | 2026-03-31 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.2.tsv) |
|  | v1.1 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.0.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/sampling_activity`](../models/sampling_activity/) | [v1.2](https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.2.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/sampling_activity/sampling_activity_v1.2.tsv)

This model defines a broader Sampling Activity (E7) at the Object level, that groups shared metadata (who, when, where, why, and documentation) for one or more individual sample extraction activities. Each extraction is represented as a nested S2: Sample Taking event linked from the Sampling Activity. This allows shared context to be captured once, while extraction-specific links (sample site, removed sample, and observation) are recorded per individual Sample Taking event.

_The overall sampling session or campaign event in which one or more individual sample extractions were carried out._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| Optional | Sampling activity PID | Persistent Identifier (UUID); PID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | An optional public unique identifier (PID) for the sample activity. Any of the IDs defined could be flagged as a preferred ID within a documentation system. |
| ✓ | Unique System Label or ID | Database or System ID; Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Heritage Object | Link to Heritage Object | E22 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A human-made work of art that forms the physical source object from which the sample is taken. |
| Optional | Project | -- | E7 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A project to which the sample taking belongs, e.g. conservation treatment, cataloguing programme etc, and to the project metadata (e.g. the conservator carrying out a treatment, the curator in charge of cataloguing, the dates of the project etc) |
| ✓ | Sampling Date | Date of Sampling Activity; Date | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The date or date range of the sampling activity, spanning all related sample taking events. |
| ✓ | Planned by | Institution; Person | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Name of person (or institution) responsible for planning the sampling activity - this is likely to be the same person (or institution) who actually takes the individual related sample(s), but it might not be. When person is unknown, ‘unknown person’ or the institution (which is usually known) should be recorded. |
| Optional | Reason for Sampling | Reason for Sampling Activity; Overall Purpose | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The overall motivation for carrying out the Sampling Activity/session. This describes the research, conservation, or technical question being addressed and may apply to one or more individual sample takings. |
| ✓ | Sampling Activity Comment | Description | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A brief factual description of the overall Sampling Activity/session (global context), focusing on notable session-level circumstances or exceptions, without repeating details that belong to individual sample taking events. |
| ✓ | Condition state | Status of Heritage Object at Time of Sampling; Object Status | S4 > E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | The state of the object as a whole at the time of sampling, for example during cleaning. |
| ✓ | Method or Procedure | Method; Procedure | E29 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A defined sampling protocol or procedure that may be referenced for standard approaches. |
| ✓ | Sampling Location | Location of Sampling Activity; Location | E53 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The physical place where the sampling activity occurred, typically within an institution or laboratory. |
| Optional | Report or Document | Related Document(s); Reports; Publications; Summaries | E31 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Primarily related to authored notes, reports and publications, however there is a whole range of relevant documents that can reference or be linked to this event. |
| ✓ | Sample Taking | Cross-reference to Sample Taking | S2 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The individual event of taking a sample. |

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
