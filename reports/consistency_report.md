# Model Consistency Report

_Generated: 2026-04-10 13:10 UTC_

**Individual model files analysed:** 19  
**Workflow/overview files analysed:** 1  

This report checks consistency of inter-model linking nodes declared in each model's `//subgraph Linked Entities` block. Only declared linked entities are checked -- high-multiplicity classes such as E55 type terms are not flagged unless explicitly declared.

<details>
<summary><strong>Link declaration syntax and status key</strong></summary>

### Link declaration syntax

Each linked entity in a model's `//subgraph Linked Entities` block should have a `//links` directive declaring what it connects to. Two target types are supported:

**Repo model targets** -- point to another model folder in this repository:
```
//links E39: Project Owner --> person, organisation
//links E7: Parent Project --> project
```

**Ontology references** -- follow standard CRM/extension ontology structure with no bespoke repo model needed:
```
//links E31: Related Documents --> crm:E31
//links E94: Sampling Point --> crmsci:E94
//links D1: Digital Object --> crmdig:D1
```

Multiple targets are comma-separated or joined with `or`.

**Confirming intentional hierarchy matches** -- where a linked entity uses a subclass or superclass of the target model's key entity and this is deliberate, add `[confirmed]` to suppress the 'confirm intent' flag:
```
//links E39: Group or Artist --> person, organisation [confirmed]
```

### Status key

| Icon | Meaning |
|------|---------|
| ✅ | Consistent -- repo model, class codes match exactly |
| ✅ | Consistent (confirmed hierarchy match) |
| 🔵 | Hierarchy match -- repo model, related via CRM hierarchy, confirm intent |
| ⚠️ | Class mismatch -- classes not related, check required |
| ❓ | Missing target -- declared target folder not found in repo |
| 📖 | Ontology reference -- follows standard CRM/extension ontology structure |
| 📖 | Ontology reference (confirmed hierarchy match) |
| 📖🔵 | Ontology via hierarchy -- related class, confirm intent |
| 📖⚠️ | Ontology mismatch -- class code does not match reference |
| ⚠ | No declaration -- `//links` directive missing, suggestions provided |

</details>

---

## 1. Per-model link validation

Each model's linked entities are listed with their declared target models and consistency status. Where no `//links` declaration exists, possible targets are suggested based on matching class codes.

<details>
<summary><strong>document_creation/document_creation_v1.0.tsv</strong> -- 4 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Document` | `E31` | `simple_document` → `E31: Simple Document` | ✅ Consistent |
| `E31: Influenced By` | `E31` | `simple_document` → `E31: Simple Document` | ✅ Consistent |
| `E39: Author` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |

</details>

<details>
<summary><strong>document_update/document_update_v0.1.tsv</strong> -- 3 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Document` | `E31` | `simple_document` → `E31: Simple Document` | ✅ Consistent |
| `E39: Editor` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |

</details>

<details>
<summary><strong>heritage_object/heritage_object_v1.8.tsv</strong> -- 13 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Organisation or Person` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Institution or Place` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E54: Dimensions` | `E54` | `crm:E54` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E78: Collection (Curated Holding)` | `E78` | `crm:E78` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E57: Medium` | `E57` | `crm:E57` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E57: Other Material` | `E57` | `crm:E57` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E22: Support` | `E22` | `heritage_object_part` → `E22/S20: Heritage Object Part` | ✅ Consistent |
| `E12: Production Event` | `E12` | `production` → `E12: Production` | ✅ Consistent |
| `EX_Digital_Image: Main Object Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `EX_Digital_Image: Object Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `S27: Observation` | `S27` | `observation` → `S27: Observation` | ✅ Consistent |

</details>

<details>
<summary><strong>heritage_object_part/heritage_object_part_v1.1.tsv</strong> -- 6 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E57: Material` | `E57` | `crm:E57` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E54: Dimensions` | `E54` | `crm:E54` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E12: Production Event` | `E12` | `production` → `E12: Production` | ✅ Consistent |
| `E22/S13: Heritage Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |

</details>

<details>
<summary><strong>location/location_v1.1.tsv</strong> -- 2 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Location Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E94: Geometry (Space Primitive)` | `E94` | `crm:E94` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>observation/observation_v1.0.tsv</strong> -- 7 confirmed, 1 missing target</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S15: Observed Entity` | `S15` | `crmsci:S15` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E39: Institution or Person` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method / Protocol` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `D1: Digital Result` | `D1` | `data_set` | ❓ Missing target -- folder not found in repo |
| `E26: Area of Interest` | `E26` | `crm:E26` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>organisation/organisation_v1.0.tsv</strong> -- 4 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E21: Person (Member)` | `E21` | `person` → `E21: Person` | ✅ Consistent |
| `E53: Location (Place of Organisation)` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Organisation Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E74: Parent Organisation` | `E74` | `organisation` → `E74: Organisation` | ✅ Consistent |

</details>

<details>
<summary><strong>person/person_v1.2.tsv</strong> -- 3 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E74: Organisation (Affiliation)` | `E74` | `organisation` → `E74: Organisation` | ✅ Consistent |
| `E53: Place (Residence)` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Person Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>production/production_v1.1.tsv</strong> -- 5 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E39: Group or Artist` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Place of Production` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Production Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>project/project_v1.3.tsv</strong> -- 6 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Project Owner` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E39: Other Actors` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E31: Related Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E7: Parent Project` | `E7` | `project` → `E7: Project` | ✅ Consistent |

</details>

<details>
<summary><strong>sample/sample_v1.9.tsv</strong> -- 14 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S2: Sample Taking` | `S2` | `sample_taking` → `S2: Sample Taking` | ✅ Consistent |
| `S24: Sample Splitting` | `S24` | `sample_splitting` → `S24: Sample Splitting` | ✅ Consistent |
| `E39: Sample Owner` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Organisation or Address` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E39: Sample Keeper` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E31: Sample Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `S27: Observation` | `S27` | `observation` → `S27: Observation` | ✅ Consistent |
| `E11: Sample Modification` | `E11` | `sample_modification` → `E11: Sample Modification` | ✅ Consistent |
| `EX_Digital_Image: Main Sample Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `EX_Digital_Image: Sample Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E53: Storage Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E22: Storage Unit` | `E22` | `sample_storage_unit` → `E22: Storage Unit` | ✅ Consistent |

</details>

<details>
<summary><strong>sample_modification/sample_modification_v1.5.tsv</strong> -- 6 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22/S13: Heritage Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |
| `E39: Institution or Person` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method / Protocol` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>sample_site/sample_site_v1.6.tsv</strong> -- 10 confirmed, 1 missing target</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E22/S13: Heritage Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |
| `S2: Sample Taking` | `S2` | `sample_taking` → `S2: Sample Taking` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `EX_Digital_Image: Annotation Image` | `EX_Digital_Image` | `annotation_image` | ❓ Missing target -- folder not found in repo |
| `EX_Digital_Image: Sample Site reference image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `EX_Digital_Image: Other Site Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E22: Heritage Object Part` | `E22` | `heritage_object_part` → `E22/S20: Heritage Object Part` | ✅ Consistent |
| `E26: Area of Interest` | `E26` | `crm:E26` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E54: Sample Site Coordinates (object)` | `E54` | `crm:E54` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E54: Sample Site Coordinates (annotation image)` | `E54` | `crm:E54` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>sample_splitting/sample_splitting_v1.1.tsv</strong> -- 7 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22/S13: Source Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |
| `E22/S13: Sub-Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |
| `E39: Undertaken by` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method or Procedure` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>sample_storage_unit/sample_storage_unit_v1.1.tsv</strong> -- 5 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Storage Keeper` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Storage Location (Place)` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Storage Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Storage Method / Protocol` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>sample_taking/sample_taking_v1.7.tsv</strong> -- 8 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E22/S13: Heritage Sample` | `E22/S13` | `sample` → `E22: Physical Sample` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method or Procedure` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E39: Sample taken by` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Sampling Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E26: Sample Site` | `E26` | `sample_site` → `E26: Sample Site` | ✅ Consistent |

</details>

<details>
<summary><strong>sampling_activity/sampling_activity_v1.2.tsv</strong> -- 8 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method or Procedure` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E39: Planned by` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Sampling Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `S2: Sample Taking` | `S2` | `sample_taking` → `S2: Sample Taking` | ✅ Consistent |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E7: Project` | `E7` | `project` → `E7: Project` | ✅ Consistent |

</details>

<details>
<summary><strong>simple_document/simple_document_v1.1.tsv</strong> -- 5 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E1: Documented Entity` | `E1` | `crm:E1` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E65: Document Creation` | `E65` | `document_creation` → `E65: Document Creation` | ✅ Consistent |
| `E13: Document Update` | `E13` | `document_update` → `E13: Document Update` | ✅ Consistent |
| `EX_Digital_Image: Incorporated Image` | `EX_Digital_Image` | `rs:EX_Digital_Image` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E31: Simple Document (Part)` | `E31` | `simple_document` → `E31: Simple Document` | ✅ Consistent |

</details>

## 2. Models missing Linked Entities subgraph

These formed model files do not contain a `//subgraph Linked Entities` block. Add the block to enable consistency checking.

- `user_workflows/workflow_user_sample_taking_v1.0.tsv`
