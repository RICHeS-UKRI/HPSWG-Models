# Heritage object

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
<summary><strong>Heritage object</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.7.tsv">v1.7</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.7 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.7.tsv) |
|  | v1.6 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.6.tsv) |
|  | v1.5 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.5.tsv) |
|  | v1.4 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.4.tsv) |
|  | v1.3 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.3.tsv) |
|  | v1.2 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.2.tsv) |
|  | v1.1 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.0.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/heritage_object`](../models/heritage_object/) | [v1.7](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.7.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.7.tsv)

This model defines the Heritage Object (E22) as the core object from which technical study data, and descriptive documentation are derived. It records ownership, collection context, dimensions, support, and medium, linking the artwork to its production event, associated documentation, and any related scientific or curatorial information. Together, these relationships provide a foundation for integrating technical study, provenance, and contextual research across connected datasets.

_A human-made work of art; the primary entity in this model, from which ownership, collection context, production, documentation, and scientific data are all derived._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| ✓ | Persistent Identifier (PID) | External ID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | A unique identifier for the heritage object as defined by an institution external to the keeper or owner of the object (e.g. Getty ID, a URI, WikiData ID, Cultural Object Name Authority). Any of the IDs defined could be flagged as a preferred ID within a documentation system. |
| Optional | Unique System Label or ID | System Label or ID; Database or System ID/Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Accession Number (custodian) | Accession Number; Inventory Number | E42 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | A unique identifier for the heritage object as defined by the keeper or owner of the object (e.g. an institutional persistent identifier). Any of the IDs defined could be flagged as a preferred ID within a documentation system. |
| Optional | Alternative Identifiers | Other Identifiers | E42 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | A wide range of different additional identifiers can be associated to a Heritage Object from historic codes to other globally resolvable PIDs. |
| ✓ | Full Title | -- | E35 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The official long title given to the object. |
| Optional | Alternate Title | Alternative Title | E35 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | Another version of the title, commonly shorter and often used for web and software presentations, or historic titles used in the past. |
| ✓ | object type | Object Type; Object Class; Type; Class | E55 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | Multiple values selected from a defined controlled list. |
| ✓ | Organisation or Person | Current Heritage Object Owner; Owner | E39 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The legal owner or holding institution of the Heritage Object. |
| ✓ | Organisation or Person#-1 | Current Heritage Object Keeper; Keeper | E39 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The institution or person currently responsible for the Heritage Object’s care or location. |
| Optional | Collection (Curated Holding) | Collection; Curated Holding | E78 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The collection or sub-collection to which the Heritage Object formally belongs. |
| ✓ | Institution or Place | Current Permanent Location; Location | E53 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The physical location or site where the Heritage Object is housed or displayed. |
| ✓ | Dimensions | Values and Ranges | E54 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The measured height, width, and optionally depth of the Heritage Object, recorded as dimensional attributes. |
| ✓ | Medium | -- | E57 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The medium of the material used in creating the object on the support (e.g. paint binding medium, drawing material, pastel etc). |
| Optional | Other Material | Other Materials | E57 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | Any material forming part of the original composition or manufacture of a heritage object or sample, beyond media or supports. |
| ✓ | Support | Primary Support | E22 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The physical base material or structure of the heritage object. This can include designation of different types of support, for example, primary support (eg original canvas) and secondary support (eg lining canvas) as parts of a painting. |
| Optional | Description Text | Description | E73 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | A brief statement describing the heritage object. |
| ✓ | Credit Line | -- | E73 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | A brief text, commonly relating to the acquisition or an influence on the acquisition - commonly a description of the actor who has funded it. |
| Optional | Report or Document | Related Document; Reports; Publications | E31 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | Any document, catalogue entry, publication, or report relating to the Heritage Object’s description, study, or conservation. |
| Optional | Main Object Image | -- | EX_Digital_Image | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The primary selected image representing the heritage object, used for thumbnails, search results, and default display. Normally a current, full front-facing view of the object. |
| Optional | Object Image | Other Images | EX_Digital_Image | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | All other images associated with the heritage object held in the system. Acts as a catch-all to support simple image lists and gallery displays; image type and capture technique are defined on the image record or related creation event. |
| ✓* | Creator | Creator of Heritage Object; Artist | E12 > E39 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The actor (artist, studio, workshop) who carried out the production. |
| ✓* | Date of Production | -- | E12 > E52 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The date or timespan during which the heritage object was produced. |
| ✓* | Place of Production | -- | E12 > E53 | ![behaviour: Ingested](https://img.shields.io/badge/%2F%2F-Ingested-7d5a00) | The location where the heritage object was created. |

_\* Required status could not be derived from the model and has been set to required by default. Please verify._

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
