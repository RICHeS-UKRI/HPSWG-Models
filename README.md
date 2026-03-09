# Heritage Science Modelling at the National Gallery

This repository defines a set of semantic models describing paintings, samples, and associated
heritage-science entities. The goal is to support clear documentation, interoperability, and
FAIR-aligned data sharing across the National Gallery, RICHeS partners, and potential future
collaborations such as the ECHOES project.

All models are defined as **CIDOC CRM-aligned** triple structures using simple TSV files and are
designed for use with the **National Gallery Dynamic Modeller**. These models support ongoing work
to prepare and publish research data through platforms such as **ResearchSpace** and the **HSDS**
(UKRI RICHeS) repository.

Work on these models is supported by **UKRI RICHeS – Heritage Science Data Service (HSDS)** funding,
with contributions from researchers, conservators, and technical specialists across partner
institutions. Additional collaborators will be acknowledged as models continue to evolve.

---

## Visual Overview of All Models

<!-- BEGIN AUTO: NG-MODEL-VISUAL -->
```mermaid
%%{init: {'flowchart': {'wrappingWidth': 600}}}%%
flowchart LR
classDef object stroke:#2C5D98,fill:#2C5D98,color:white,rx:5px,ry:5px;
classDef event stroke:#5C811F,fill:#5C811F,color:white,rx:5px,ry:5px;


O0("Heritage Sample<br>S13_Sample and<br>E19_Physical_object")
class O0 object;

O1("Sample Taking<br>S2_Sample_Taking")
class O1 event;
O0["Heritage Sample<br>S13_Sample and<br>E19_Physical_object"] -- "O5i_was_removed_by #40;1 to 1#41;" -->O1["Sample Taking<br>S2_Sample_Taking"]

O2("Heritage Object<br>E22_Human-Made Object")
class O2 object;
O1["Sample Taking<br>S2_Sample_Taking"] -- "O3_sampled_from #40;1 to 1#41;" -->O2["Heritage Object<br>E22_Human-Made Object"]

O3("Sample Splitting<br>S24_Sample_splitting")
class O3 event;
O0["Heritage Sample<br>S13_Sample and<br>E19_Physical_object"] -- "O1i_was_diminished_by #40;0 to 1#41;" -->O3["Sample Splitting<br>S24_Sample_splitting"]

O4("Heritage Sample<br>S13_Sample and<br>E19_Physical_object#-1")
class O4 object;
O3["Sample Splitting<br>S24_Sample_splitting"] -- "O29_removed_sub-sample #40;1 to n#41;" -->O4["Heritage Sample<br>S13_Sample and<br>E19_Physical_object"]
;
```
<!-- END AUTO: NG-MODEL-VISUAL -->

---

## Available Models

The following models are defined in this repository.  
Each entry links to its model page, the latest raw TSV file, and the interactive visualisation
in the Dynamic Modeller.

<!-- BEGIN AUTO: MODEL-LIST -->
### Semantic workflow overviews

CIDOC CRM-aligned inter-model connectivity references. These act as the canonical reference for shared node labels across individual models.

| Name | Type / Status | Folder | Latest TSV | Visualisation |
|------|--------------|--------|-----------|---------------|
| Workflows | ![Semantic Workflow](https://img.shields.io/badge/type-semantic--workflow-blue) | [`models/workflows`](models/workflows/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/workflows/workflow_cidoc_sample_taking_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/workflows/workflow_cidoc_sample_taking_v1.0.tsv) |

### User workflow overviews

Simplified overviews for communication and stakeholder agreement. Not part of the semantic consistency check.

| Name | Type / Status | Folder | Latest TSV | Visualisation |
|------|--------------|--------|-----------|---------------|
| User workflows | ![User Workflow](https://img.shields.io/badge/type-user--workflow-blueviolet) | [`models/user_workflows`](models/user_workflows/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/user_workflows/workflow_user_sample_taking_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/user_workflows/workflow_user_sample_taking_v1.0.tsv) |

### Domain models

Individual CIDOC CRM domain models, each covering a specific aspect of heritage science documentation.

| Name | Type / Status | Folder | Latest TSV | Visualisation |
|------|--------------|--------|-----------|---------------|
| Frame | ![Status: Planned](https://img.shields.io/badge/status-planned-lightgrey) | [`models/frame`](models/frame/) | -- | -- |
| Frame part | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/frame_part`](models/frame_part/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/frame_part/frame_part_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/frame_part/frame_part_v1.0.tsv) |
| Heritage object | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/heritage_object`](models/heritage_object/) | [v1.4](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.4.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object/heritage_object_v1.4.tsv) |
| Heritage object component | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/heritage_object_component`](models/heritage_object_component/) | _Precursor files only_ | -- |
| Heritage object image | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/heritage_object_image`](models/heritage_object_image/) | _Precursor files only_ | -- |
| Heritage object layer | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/heritage_object_layer`](models/heritage_object_layer/) | _Precursor files only_ | -- |
| Heritage object part | ![Status: Mixed](https://img.shields.io/badge/status-mixed-yellow) | [`models/heritage_object_part`](models/heritage_object_part/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object_part/heritage_object_part_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/heritage_object_part/heritage_object_part_v1.0.tsv) |
| Location | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/location`](models/location/) | [v1.1](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/location/location_v1.1.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/location/location_v1.1.tsv) |
| Organisation | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/organisation`](models/organisation/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/organisation/organisation_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/organisation/organisation_v1.0.tsv) |
| Person | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/person`](models/person/) | [v1.1](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/person/person_v1.1.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/person/person_v1.1.tsv) |
| Production event | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/production_event`](models/production_event/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/production_event/production_event_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/production_event/production_event_v1.0.tsv) |
| Project | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/project`](models/project/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/project/project_v1.0.tsv) |
| Sample | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sample`](models/sample/) | [v1.6](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.6.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample/sample_v1.6.tsv) |
| Sample component | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/sample_component`](models/sample_component/) | _Precursor files only_ | -- |
| Sample image | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/sample_image`](models/sample_image/) | _Precursor files only_ | -- |
| Sample imaging event | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/sample_imaging_event`](models/sample_imaging_event/) | _Precursor files only_ | -- |
| Sample layer | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/sample_layer`](models/sample_layer/) | _Precursor files only_ | -- |
| Sample modification | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sample_modification`](models/sample_modification/) | [v1.3](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_modification/sample_modification_v1.3.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_modification/sample_modification_v1.3.tsv) |
| Sample preparation event | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/sample_preparation_event`](models/sample_preparation_event/) | _Precursor files only_ | -- |
| Sample site | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sample_site`](models/sample_site/) | [v1.4](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.4.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_site/sample_site_v1.4.tsv) |
| Sample storage unit | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sample_storage_unit`](models/sample_storage_unit/) | [v1.0](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_storage_unit/sample_storage_unit_v1.0.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_storage_unit/sample_storage_unit_v1.0.tsv) |
| Sample taking event | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sample_taking_event`](models/sample_taking_event/) | [v1.4](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking_event/sample_taking_event_v1.4.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sample_taking_event/sample_taking_event_v1.4.tsv) |
| Sampling event | ![Status: Formed](https://img.shields.io/badge/status-formed-brightgreen) | [`models/sampling_event`](models/sampling_event/) | [v1.1](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sampling_event/sampling_event_v1.1.tsv) | [Open](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/sampling_event/sampling_event_v1.1.tsv) |
| Simple descriptive document | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/simple_descriptive_document`](models/simple_descriptive_document/) | _Precursor files only_ | -- |
| Timespan | ![Status: Precursor](https://img.shields.io/badge/status-precursor-orange) | [`models/timespan`](models/timespan/) | _Precursor files only_ | -- |
<!-- END AUTO: MODEL-LIST -->

---

## How to Use These Models

1. Open any TSV file directly in the Dynamic Modeller using the “Visualisation” links above.  
2. Review the model-specific page to explore version history and related documentation.  
3. Use these models as a starting point for:
   - ResearchSpace ingestion
   - FAIR data packaging in HSDS
   - ECHOES Digital Twin prototyping
   - Internal NG interoperability work
4. Models are intentionally simple to enable discussion and refinement.  
   CIDOC CRM alignment will be strengthened in future iterations.

---

## Design Principles

- **CIDOC CRM v7.1.3 alignment**
- **Modular, extensible structure**
- **Transparent and easy to review**
- **Supports FAIR Digital Object approaches**
- **Designed for cross-project reusability**

---

## Acknowledgements

This work is supported by **UKRI – RICHeS HSDS** and builds on ongoing collaboration with the
National Gallery’s Heritage Science team and wider partners.  
Additional contributors will be acknowledged as the models evolve.
