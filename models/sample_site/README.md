# Sample site

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
<summary><strong>Sample site</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.6.tsv">v1.6</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v1.6 | 2026-03-24 | 2026-03-24 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.6.tsv) |
|  | v1.5 | 2026-03-07 | 2026-03-23 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.5.tsv) |
|  | v1.4 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.4.tsv) |
|  | v1.3 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.3.tsv) |
|  | v1.1 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.1.tsv) |
|  | v1.0 | 2026-03-07 | 2026-03-07 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.0.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/sample_site`](../models/sample_site/) | [v1.6](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.6.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.6.tsv)

This model defines the relationships surrounding the Sample Site within the context of sampling events on paintings following CIDOC CRM and CRMsci principles. The Sample Site (E26) represents the precise point or small area on the painting from which a material sample was taken. It is physically located on the painting or a defined Painting Part (E22) and may also be situated within a broader Area of Interest (E26) allowing multiple related sampling points or observations to be grouped together. Each Sample Site can be linked to digital image regions that visually represent its position and to descriptive or contextual notes incorporated within related documents. The model records both its role in the Sample Taking event (S2) and its former association with the removed Sample (S13). These relationships establish a clear and reusable structure for documenting where samples originate how they are contextualized within the painting and how they relate to analytical and descriptive records across digital and physical domains.

_The specific point or area on the painting where the sample was taken. Can also be considered as a E53 Place._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| Optional | Sample Site PID | Persistent Identifier (PID); PID | E42 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Various types of PIDs can be used here, please note that again IGSNs are an option. Any of the IDs defined could be flagged as a preferred ID within a documentation system. |
| ✓ | Unique System Label or ID | Database or System ID; Sample Site System ID | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Sample Site Name/Number | Site Label; Site Name; Site Code | E41 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The name, number or code given to identify the sample site for humans. An agreed local protocol for the structure of this name is still recommended. |
| ✓ | Sample Site Description | Description Text; Description | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A concise description of the physical location and appearance of the sampling point on the object. This should describe where the site is and any relevant visual or material features, without explaining why it was chosen, e.g. shadow of red drapery of the saint, left edge. |
| Optional | Site Selection Comment | -- | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Any additional text describing any observations recorded about the specific sample site (e.g. area of over-paint, degraded area etc) that do not fit in the general description. Any uncertainty over the exact sample site location can also be described here. |
| Optional | Sample Site Coordinates (object) | -- | E54 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The measured height, width, and position of the sample site relative to the physical Heritage Object. |
| Optional | Sample Site Coordinates (annotation image) | Digital Image Region; Image Annotation | E54 | ![behaviour: Automatic](https://img.shields.io/badge/%2F%2F-Automatic-32383f) | The recorded pixel dimensions; shape, height, width, and or position of the sample site relative to a define annotation image depicting the Heritage Object. It is not required but this is expected to be achieved via the use of IIIF based solutions. Analogue annotations (on a print/photograph) are expected to be transferred to a digital image to create these values. |
| Optional | Reason for Sample Site Selection | Site Selection Description | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | An optional explanation of why this specific location was selected for sampling. Use this only when the choice of site requires additional justification beyond the overall reason for the sample taking event. |
| Optional | Area of Interest | Object Part | E26 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | This optional field is a link to a wider area/place/feature on an object or object part within which the sample site lies. This allows, for example, 3 samples from the same red drapery to be linked. Any text description of this would sit on the Area of interest entity. |
| Optional | Report or Document | Related Document; Reports; Publications; Summaries | E31 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Primarily related to reports and publications, however there is a whole range of documents that can be created to describe or reference the sample site. |
| ✓ | Heritage Object | Link to Heritage Object | E22 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A human-made work of art that forms the physical source object from which the sample is taken. |
| Optional | Heritage Object Part | Link to Heritage Object Part | E22 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Optional connection to a defined sub part of a heritage object if a relevant one has been defined. E.g. back/front/extension etc. Could also be defined as a E25 Human made feature. |
| ✓* | Heritage Sample | Sample | S13 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) |  (Cross-reference to Sample; Removed; Sample; Created, a reference to the sample that was taken from this sample site – Class to be Confirmed as dual S13/E22 construct may be needed for the sample.) |
| ✓ | Sample Taking | Cross-reference to Sample Taking; Sample Creation | S2 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The specific Sample Taking event to which the sample site is related. |
| Optional | EX_Digital_Image: Sample Site reference image | Digital Image; Reference Image; Reference Detail; Main Site Image | EX_Digital_Image: Sample Site reference image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to an image that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | EX_Digital_Image: Other Site Image | Site Image | EX_Digital_Image: Other Site Image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to any additional images that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | EX_Digital_Image_Region | Image Annotation; Digital Image Region | EX_Digital_Image_Region | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A defined digital region on an image corresponding to the physical sample site on the painting. |

_\* Required status could not be derived from the model and has been set to required by default. Please verify._

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
