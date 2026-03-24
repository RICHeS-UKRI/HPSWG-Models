# Sample

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
<summary><strong>Sample</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.8.tsv">v1.8</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.8 | 2026-03-18 | 2026-03-24 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.8.tsv) |
|  | v1.7 | 2025-11-28 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.7.tsv) |
|  | v1.6 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.6.tsv) |
|  | v1.5 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.5.tsv) |
|  | v1.4 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.4.tsv) |
|  | v1.3 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.3.tsv) |
|  | v1.2 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.2.tsv) |
|  | v1.1 | 2025-11-28 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.0.tsv) |
|  | v0.9 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v0.9.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/sample`](../models/sample/) | [v1.8](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.8.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.8.tsv)

This model defines a Sample using a dual-layer structure: E22 (Physical Sample) is the curated physical artefact carrying persistent identifiers, custody, condition records, and images; S13 (Material Sample) is the removed matter that is the subject of scientific events. Both are created through a Sample Taking event. The E22 carries/contains the S13 via P46. Connections to other models (Heritage Object, Sample Site, analytical events) are distributed across both entities as semantically appropriate.

_A curated physical artefact that contains or carries the sampled matter (S13). Serves as the object-management layer: it holds identifiers, condition records, custody, storage, and images. P46 is used as a pragmatic contains/carries proxy for collection management purposes._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| ✓ | Persistent Identifier (e.g. IGSN) | Sample PID; PID; Persistent Identifier | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | For samples not defined with a fully resolvable PID like an IGSN the preferred ID is likely to be the same as or based on the E41: Sample Label/No/ID. |
| ✓ | Unique System Label or ID | Sample System ID; Database ID; System Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as the ResearchSpace required label. |
| ✓ | Sample Name or Code | Sample ID; Sample No; Sample Code; Sample Name | E41 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A human-readable name or number used to identify the sample in documentation or images, typically visible on labels or microscope slides. This field will generally need to follow an agreed local naming protocol. |
| Optional | Alternative Identifier | Alternative Sample ID; Sample No; Sample Code | E42 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Any other identifier or code by which the sample may be known in external systems, publications, or legacy records. This also includes identifiers assigned by other systems and organisations. |
| Optional | Sample description | Sample Description; Description | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | This could include a whole range of descriptions relating to the sample. |
| ✓ | sample format | Sample Format | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | The physical form of the sample as a material object. The format of the sample may change over time. |
| ✓ | sample material type | Sample Material Type; Material Class; Material of Interest | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | The material or substance type of the removed matter (e.g. paint, ground, varnish, adhesive, metal, stone). |
| Optional | sample keywords | Sample Keyword; Keywords | E55 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | Keywords or classification terms used for discovery, retrieval, and contextualisation of the sample record (e.g., class, technique, composition). |
| ✓ | Sample size | Sample Size; Size Class; Size Range | E54 | ![behaviour: Controlled List](https://img.shields.io/badge/%2F%2F-Controlled%20List-1a7f37) | Dimensions or size class of the sample, controlled list:<br/>micro-sample (< 0.01 m),<br/>small-sample (0.01 – 0.1 m),<br/>medium-sample (0.1 – 0.3 m),<br/>large-sample (0.3 – 1.0 m),<br/>very-large-fragment (> 1.0 m) |
| Optional | Main Sample Image | Reference Image; Preferred Image | EX_Digital_Image |  | The primary representative image of the curated physical sample. |
| Optional | Sample Image | Digital Image | EX_Digital_Image |  | Additional documentary images of the curated physical sample. |
| ✓ | Sample Owner | Current Owner of Sample | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The legal owner of the sample. |
| ✓ | Sample Keeper | Current Keeper of Sample | E39 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The organisation responsible for the care, storage, or management of the physical sample. |
| Optional | Storage Location | Current Permanent Location | E53 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A named place where a sample is permanently stored, such as an institution, department, building, or room. Use this option when no physical storage unit record exists for the sample. If a storage unit is known, link to that instead and allow the location to be inherited through the unit's own records. |
| Optional | Storage Unit | Current Storage Unit; Cabinet; Drawer | E22 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A discrete physical container in which a sample is stored, such as a cabinet, drawer, box, or tray. Storage units should themselves carry a permanent location (E53) or link to a larger containing unit, which in turn resolves to a named location. Units may be nested to any depth before resolving to a place. Use this option in preference to a direct location link when the specific unit is known. |
| Optional | Organisation or Address | Current Location; Sample Temporary Location | E53 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The current location of the sample if different to its permanent location. |
| Optional | Observation | Sample Examination Event; Sample Observation; Sample Measurement | S27 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | An observation or examination event related to the sample, ranging from simple visual inspection or interpretation to quantitative measurement or analytical investigation. These events may or may not result in recorded images, data, or other outputs. (S27 is a parent of the standard Core CRM Measurement) |
| Optional | Sample Modification | Sample Modification Event; Sample Preparation | E11 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | An event that altered the sample after its initial removal, such as preparation, embedding, or coating. |
| Optional | Sample Documents | Related Document; Related Documents; Reports; Publications | E31 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Primarily related to authored notes, reports and publications, however there is a whole range of relevant documents that can reference or be linked to this sample. |
| ✓ | Sample Taking | Source Event; Sample Taking Event; Sample Splitting Event | S2 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The event during which the sample was physically removed from its source object. |

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
