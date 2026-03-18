# Model Consistency Report

_Generated: 2026-03-18 13:58 UTC_

**Individual model files analysed:** 14  
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
| ❓ | Unknown target -- declared target folder not found in repo |
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
<summary><strong>heritage_object/heritage_object_v1.6.tsv</strong> -- 10 confirmed, 2 undeclared</summary>

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
| `E12: Production Event` | `E12` | `production_event` → `E12: Production` | ✅ Consistent |
| `EX_Digital_Image: Main Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>heritage_object_part/heritage_object_part_v1.1.tsv</strong> -- 5 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E57: Material` | `E57` | `crm:E57` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E54: Dimensions` | `E54` | `crm:E54` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E12: Production Event` | `E12` | `production_event` → `E12: Production` | ✅ Consistent |
| `S13: Material Sample` | `S13` | `sample` → `E22: Physical Sample` | ⚠️ Class mismatch -- check required |

</details>

<details>
<summary><strong>location/location_v1.1.tsv</strong> -- 2 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Location Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E94: Geometry (Space Primitive)` | `E94` | `crm:E94` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

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
<summary><strong>production_event/production_event_v1.1.tsv</strong> -- 5 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `E39: Group or Artist` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Place of Production` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Production Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |

</details>

<details>
<summary><strong>project/project_v1.1.tsv</strong> -- 6 confirmed</summary>

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
<summary><strong>sample/sample_v1.8.tsv</strong> -- 10 confirmed, 2 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S2: Sample Taking` | `S2` | `sample_taking_event` → `S2: Sample Taking` | ✅ Consistent |
| `S24: Sample Splitting` | `S24` | `sample_splitting` | ❓ Target folder not found in repo |
| `E39: Organisation or Person` | `E39` | `person` → `E21: Person` | ✅ Consistent (confirmed hierarchy match) |
|  |  | `organisation` → `E74: Organisation` | ✅ Consistent (confirmed hierarchy match) |
| `E53: Organisation or Address` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E31: Sample Documents` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E16: Measurement` | `E16` | `crm:E16` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `S27: Observation` | `S27` | `crmsci:S27` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E11: Sample Modification` | `E11` | `sample_modification` → `E11: Sample Modification` | ✅ Consistent |
| `EX_Digital_Image: Main Sample Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Sample Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `E53: Storage Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E22: Storage Unit` | `E22` | `sample_storage_unit` → `E22: Storage Unit` | ✅ Consistent |

</details>

<details>
<summary><strong>sample_modification/sample_modification_v1.3.tsv</strong> -- 7 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S13: Sample` | `S13` | _No matching models found_ | ⚠ No declaration |
| `E39: Institution or Person` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Place of Modification` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E29: Method / Protocol` | `E29` | _No matching models found_ | ⚠ No declaration |
| `E57: Material Used` | `E57` | _No matching models found_ | ⚠ No declaration |
| `E70: Tool / Equipment` | `E70` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample_site/sample_site_v1.4.tsv</strong> -- 8 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `heritage_object_part` (`E22/S20: Heritage Object Part`), `sample` (`E22: Physical Sample`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `S13: Sample` | `S13` | _No matching models found_ | ⚠ No declaration |
| `S2: Sample Taking` | `S2` | _Suggested: `sample_taking_event` (`S2: Sample Taking`)_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Main Site Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Site Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `E22: Heritage Object Part` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `heritage_object_part` (`E22/S20: Heritage Object Part`), `sample` (`E22: Physical Sample`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E26: Area of Interest` | `E26` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample_storage_unit/sample_storage_unit_v1.0.tsv</strong> -- 4 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Storage Keeper` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Storage Location (Place)` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Storage Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E29: Storage Method / Protocol` | `E29` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample_taking_event/sample_taking_event_v1.5.tsv</strong> -- 4 confirmed, 1 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | `heritage_object` → `E22: Heritage Object` | ✅ Consistent |
| `S13: Sample` | `S13` | `sample` → `E22: Physical Sample` | ⚠️ Class mismatch -- check required |
| `E31: Report or Document` | `E31` | `crm:E31` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E29: Method or Procedure` | `E29` | `crm:E29` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E39: Organisation or Person` | `E39` | `person. organisation` | ❓ Target folder not found in repo |
| `E53: Sampling Location` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E26: Sample Site` | `E26` | _Suggested: `sample_site` (`E26: Sample Site`)_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sampling_event/sampling_event_v1.1.tsv</strong> -- 7 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E29: Method or Procedure` | `E29` | _No matching models found_ | ⚠ No declaration |
| `E39: Institution or Person` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Sampling Location` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `S2: Sample Taking` | `S2` | _Suggested: `sample_taking_event` (`S2: Sample Taking`)_ | ⚠ No declaration |
| `E22: Heritage Object` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `heritage_object_part` (`E22/S20: Heritage Object Part`), `sample` (`E22: Physical Sample`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E7: Project` | `E7` | _Suggested: `project` (`E7: Project`), `workflows` (`E7: Sampling Event`)_ | ⚠ No declaration |

</details>

## 2. Models missing Linked Entities subgraph

These formed model files do not contain a `//subgraph Linked Entities` block. Add the block to enable consistency checking.

- `frame_part/frame_part_v1.0.tsv`
