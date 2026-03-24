# Sample taking

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
<summary><strong>Sample taking</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.7.tsv">v1.7</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.7 | 2026-03-07 | 2026-03-24 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.7.tsv) |
|  | v1.6 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.6.tsv) |
|  | v1.5 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.5.tsv) |
|  | v1.4 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.4.tsv) |
|  | v1.3 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.3.tsv) |
|  | v1.2 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.2.tsv) |
|  | v1.1 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.0.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/sample_taking`](../models/sample_taking/) | [v1.7](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.7.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking/sample_taking_v1.7.tsv)

This model captures metadata specific to an individual sample taking event within a broader Sampling Activity. Many fields here are optional because values defined at the Sampling Activity level -- such as date, method, location, and responsible actor -- apply to all sample takings within that activity and do not need to be repeated unless they differ for this specific event. Fields that are always recorded at this level include the link to the sample produced, the sample site, the heritage object, and the system identifier.

_The event in which a material sample was physically removed from the painting._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| ✓ | Sample taking PID | Persistent Identifier (PID); PID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | An optional public unique identifier (PID) for the sample taking event. Any of the IDs defined could be flagged as a preferred ID within a documentation system. |
| ✓ | Unique System Label or ID | Database or System ID; Sample Taking System ID | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| Optional | Sampling Date | Sample Taking Date; Date | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The optional defined period of the specific sample taking event – if different from the parent sampling activity. |
| Optional | Sample taken by | Sampler; Taken by; Sampling carried out by | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Name of person (or institution) who took the sample (if different from the person/institution defined at sampling activity level). When person is unknown, ‘unknown person’ or the institution (which is usually known) should be recorded. |
| Optional | Reason for Sampling | -- | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Sample-specific reasons (different to the general reason indicated at the Sampling Activity Level). |
| ✓ | Sample taking comment | Description | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A brief factual description of the specific sampling event, focusing on any notable aspects of how the sample was removed or the nature of the material extracted. Use this to record observations, exceptions, or deviations from standard procedures, rather than to restate the sampling method, motivation, or site details. |
| ✓ | Condition state (Sample Site Status) | State of Sampling Site at Time of Sampling; Object Status | S4 > E3 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | The condition or treatment state of the sample site at the time of sampling, for example varnish removed. |
| Optional | Method or Procedure | Sampling Method; Method; Procedure | E29 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The defined process or protocol followed during the sampling or analysis activity (if different from method indicated in sampling activity). |
| Optional | Sampling Location | Location of Sample Taking Event | E53 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The physical place where the sampling event occurred, typically within an organisation or laboratory. |
| Optional | Report or Document | Related Document; Reports; Publications; Summaries | E31 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Primarily related to authored notes, reports and publications, however there is a whole range of relevant documents that can reference or be linked to this event. |
| ✓* | Heritage Sample | -- | S13 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) |  (Cross-reference to Sample; Removed; Sample; Created, a reference to the sample that was taken in this sample taking event – Class to be Confirmed as dual S13/E22 construct may be needed for the sample.) |
| ✓ | Sample Site | Cross-reference to Sample Site | E26 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The specific point or small area on the heritage object where the sample was taken. |
| ✓ | Heritage Object | Cross-reference to Heritage Object; Link to Heritage Object | E22 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | E22 is a duplicate to the one defined at the parent activity but a key property is required here for the CRM Sci linking the S2, via an O3 to the E22. |

_\* Required status could not be derived from the model and has been set to required by default. Please verify._

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
