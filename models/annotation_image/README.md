# Annotation image

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
<summary><strong>Annotation image</strong>: latest version <a href="https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/annotation_image/annotation_image_v0.1.tsv">v0.1</a></summary>

| | Version | Created | Last modified | Open in Modeller |
| :---: | :---: | :---: | :---: | --- |
| :heavy_check_mark: | v0.1 | 2026-04-11 | 2026-04-12 | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/annotation_image/annotation_image_v0.1.tsv) |

</details>

## Field reference

This table lists the fields defined for data entry or display, derived from `//field` and `//field-via` directives in the model. See the [forms folder](../../forms/field-tables.md) for the aggregated cross-model view.

[`models/annotation_image`](../models/annotation_image/) | [v0.1](https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/annotation_image/annotation_image_v0.1.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/RICHeS-UKRI/HPSWG-Models/refs/heads/main/models/annotation_image/annotation_image_v0.1.tsv)

This model records a digital image used as an annotation base. It captures identification, image metadata, capture provenance, rights, annotation group classification, and links to the heritage object depicted. The image may also be linked optionally to a dataset record where it forms part of a formal analytical output. Annotation of the image itself -- the spatial recording of sample sites, areas of interest, and examination positions -- is handled in the annotation_image workflow and related models, not here.

_A digital image designated for use as an annotation base within a heritage science documentation system. Annotation images provide the visual reference against which sample sites, areas of interest, condition features, and local examination and analysis events are spatially documented. The same image may serve multiple annotation purposes simultaneously. Images are uploaded independently and associated with one or more annotation group types. A link to a dataset record is optional where the image also forms part of a formal analytical output._

| Required | Human understandable Label | Alternative Labels | CRM Code | Behaviour | Label Description |
|----------|---------------------------|-------------------|----------|-----------|-------------------|
| ✓ | Image Label | Image Code | E41 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A human-readable name or code used to identify this image within documentation or reporting systems. |
| Optional | Image File Name | -- | E41 | -- | The original file name of the digital image file. Note: ResearchSpace may require a system-specific property for this value -- to be confirmed during implementation. (Note: may require a system-specific property in ResearchSpace. behaviour:free-text) |
| Optional | IIIF URL | Source URL | E42 | -- | The source IIIF URL for this image. Where ResearchSpace is used for annotation, images must be ingested into the system and an internal reference will also be assigned. Note: the IIIF URL could alternatively be modelled as a link to an E31 document (IIIF info.json or manifest) -- this remains an open design question to be resolved during implementation. (IIIF source URL for this image. May alternatively be modelled as a link to an E31 document (info.json or IIIF manifest) -- open design question. behaviour:url) |
| ✓ | Unique System Label or ID | System Label | E41 | ![behaviour: System ID](https://img.shields.io/badge/%2F%2F-System%20ID-57606a) | Required within some documentation or database systems, such as ResearchSpace required label. |
| ✓ | Capture Technique | Image Type | E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The technique used to capture this image. Drawn from a controlled list (e.g., visible light photography, raking light, ultraviolet fluorescence, infrared reflectography, X-radiography). Provides a summary classification; fuller detail is recorded in the linked imaging protocol. |
| Optional | File Format | Image Format | E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The file format of this image. Drawn from a controlled list (e.g., TIFF, JPEG, PNG). |
| Optional | Annotation Group Type | Annotation Purpose | E55 | -- | The type or group of annotations for which this image is currently being used (e.g., Sample Site Annotations, Area of Interest Annotations, Condition Mapping, Local Examination and Analysis Annotations). The same image may be associated with multiple annotation group types simultaneously. Drawn from a controlled list -- vocabulary still under development. (An image may be associated with multiple annotation group types simultaneously. behaviour:select) |
| Optional | Description | -- | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A concise description of the image content and any notable features relevant to its use as an annotation base. |
| Optional | Default Caption | Image Caption | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | A default human-readable caption suitable for display alongside the image in reports or interfaces. |
| ✓ | Image Credit | Credit Line | E73 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | Credit line or source statement for this image. |
| ✓ | Image Reuse Licence | -- | E73 | -- | The licence or rights statement governing reuse of this image. Where a standard licence URL exists (e.g. a Creative Commons licence), a URL is preferred over a free-text statement. Consistency with the Licence URL / Licence Statement pattern used in the data_set model is recommended. (Prefer a licence URL where a standard licence exists. behaviour:free-text) |
| ✓ | Image Width | Image Width (pixels); Pixel Width | E54 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The width of this image in pixels. |
| ✓ | Image Height | Image Height (pixels); Pixel Height | E54 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The height of this image in pixels. |
| Optional | Relative Resolution | Pixels per mm | E54 | -- | The resolution of this image expressed as pixels per millimetre on the object surface. This value is often unknown and should only be recorded where it has been formally established. (Only record where formally established. behaviour:free-text) |
| Optional | Date of Image Capture | Capture Date | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The date on which this image was captured. |
| Optional | Captured By | Photographer | E65 > E39 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The person or institution responsible for capturing this image. |
| Optional | Imaging Protocol | Method Statement | E65 > E29 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The imaging protocol or method statement used to create this image. |
| Optional | Date Designated for Annotation | Annotation Date | E52 | ![behaviour: Free Text](https://img.shields.io/badge/%2F%2F-Free%20Text-0969da) | The date on which this image was designated for use as an annotation base. |
| Optional | Designated By | Designated for Annotation By | E13 > E39 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | The person or institution responsible for designating this image for annotation use. |
| Optional | condition state type | Condition State at Capture; Object Condition at Capture | E3 > E55 | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The condition or treatment state of the heritage object at the time of image capture. |
| ✓* | Heritage Object | -- | P62_depicts > E22 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Required link to the heritage object depicted in this image. |
| ✓* | Heritage Object Part | Feature | P62_depicts > E22 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Optional link to a defined part or feature of the heritage object. E25 Human-Made Feature may be more appropriate in some cases -- to be reviewed. |
| ✓* | Related Document | Report | P70i_is_documented_in > E31 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | A document referencing or providing context for this image. |
| ✓* | Digital Dataset | -- | P165i_is_incorporated_in > D1 | ![behaviour: External ID](https://img.shields.io/badge/%2F%2F-External%20ID-0e7490) | Optional link to a dataset record where this image forms part of a formal analytical output. |

_\* Required status could not be derived from the model and has been set to required by default. Please verify._

## Contributing

If you would like to contribute to this model, please refer to the [repository contributing guidelines](../../CONTRIBUTING.md) and the [ontology reference](../../ONTOLOGIES.md). The TSV triple format is documented in the [Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/) interface.
