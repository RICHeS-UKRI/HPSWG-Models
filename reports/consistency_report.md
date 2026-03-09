# Model Consistency Report

_Generated: 2026-03-09 14:56 UTC_

**Individual model files analysed:** 14  
**Workflow/overview files analysed:** 1  

This report checks consistency of inter-model linking nodes declared in each model's `//subgraph Linked Entities` block. Only declared linked entities are checked -- high-multiplicity classes such as E55 type terms are not flagged unless explicitly declared.

## Link declaration syntax

Each linked entity in a model's `//subgraph Linked Entities` block should have a `//links` directive declaring what it connects to. Two target types are supported:

**Repo model targets** -- point to another model folder in this repository:
```
//links E39: Project Owner --> person, institution
//links E7: Parent Project --> project
```

**Ontology references** -- follow standard CRM/extension ontology structure with no bespoke repo model needed:
```
//links E31: Related Documents --> crm:E31
//links E94: Sampling Point --> crmsci:E94
//links D1: Digital Object --> crmdig:D1
```

Multiple targets are comma-separated or joined with `or`.

---

**Status key:**
- ✅ Consistent -- repo model, class codes match exactly
- 🔵 Hierarchy match -- repo model, related via CRM hierarchy, confirm intent
- ⚠️ Class mismatch -- classes not related, check required
- ❓ Unknown target -- declared target folder not found in repo
- 📖 Ontology reference -- follows standard CRM/extension ontology structure
- 📖🔵 Ontology via hierarchy -- related class, confirm intent
- 📖⚠️ Ontology mismatch -- class code does not match reference
- ⚠ No declaration -- `//links` directive missing, suggestions provided

---

## 1. Per-model link validation

Each model's linked entities are listed with their declared target models and consistency status. Where no `//links` declaration exists, possible targets are suggested based on matching class codes.

<details>
<summary><strong>heritage_object/heritage_object_v1.4.tsv</strong> -- 2 confirmed, 1 to review, 7 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Institution or Person` | `E39` | `person` → `E21: Person` | 🔵 Hierarchy match -- confirm intent |
|  |  | `institution` | ❓ Target folder not found in repo |
| `E53: Institution or Place` | `E53` | `location` → `E53: Location` | ✅ Consistent |
| `E54: Dimensions` | `E54` | _No matching models found_ | ⚠ No declaration |
| `E78: Collection (Curated Holding)` | `E78` | _No matching models found_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E57: Medium` | `E57` | _No matching models found_ | ⚠ No declaration |
| `E57: Other Material` | `E57` | _No matching models found_ | ⚠ No declaration |
| `E22: Support` | `E22` | `heritage_object_part` | ⚠️ Class mismatch -- check required |
| `E12: Production Event` | `E12` | `production_event` → `E12: Production` | ✅ Consistent |
| `EX_Digital_Image: Main Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |

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
<summary><strong>person/person_v1.1.tsv</strong> -- 4 confirmed</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E74: Organisation (Affiliation)` | `E74` | `organisation` → `E74: Organisation` | ✅ Consistent |
| `E74: Group (Membership)` | `E74` | `crm:E74` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E41: Contact Point` | `E41` | `crm:E41` (ontology) | 📖 Ontology reference -- follows standard CRM structure |
| `E53: Place (Residence)` | `E53` | `location` → `E53: Location` | ✅ Consistent |

</details>

<details>
<summary><strong>production_event/production_event_v1.0.tsv</strong> -- 4 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Painting` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E39: Group or Artist` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Place of Production` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Production Documents` | `E31` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>project/project_v1.0.tsv</strong> -- 4 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Project Owner` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E39: Other Actors` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E31: Related Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E7: Parent Project` | `E7` | _Suggested: `sampling_event` (`E7: Sampling Event`), `workflows` (`E7: Sampling Event`)_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample/sample_v1.6.tsv</strong> -- 11 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S2: Sample Taking` | `S2` | _Suggested: `sample_taking_event` (`S2: Sample Taking`)_ | ⚠ No declaration |
| `S24: Sample Splitting` | `S24` | _No matching models found_ | ⚠ No declaration |
| `E53: Storage Location` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E39: Institution or Person` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Institution or Address` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Sample Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E16: Measurement` | `E16` | _No matching models found_ | ⚠ No declaration |
| `S27: Observation` | `S27` | _No matching models found_ | ⚠ No declaration |
| `E11: Sample Modification` | `E11` | _Suggested: `sample_modification` (`E11: Sample Modification`)_ | ⚠ No declaration |
| `EX_Digital_Image: Main Sample Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Sample Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample_modification/sample_modification_v1.3.tsv</strong> -- 7 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `S13: Sample` | `S13` | _Suggested: `sample` (`S13/E19: Sample`)_ | ⚠ No declaration |
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
| `E22: Heritage Object` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `S13: Sample` | `S13` | _Suggested: `sample` (`S13/E19: Sample`)_ | ⚠ No declaration |
| `S2: Sample Taking` | `S2` | _Suggested: `sample_taking_event` (`S2: Sample Taking`)_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Main Site Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Site Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `E22: Heritage Object Part` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
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
<summary><strong>sample_taking_event/sample_taking_event_v1.4.tsv</strong> -- 7 undeclared</summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Heritage Object` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `S13: Sample` | `S13` | _Suggested: `sample` (`S13/E19: Sample`)_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E29: Method or Procedure` | `E29` | _No matching models found_ | ⚠ No declaration |
| `E39: Institution or Person` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Sampling Location` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
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
| `E22: Heritage Object` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E7: Project` | `E7` | _Suggested: `project` (`E7: Project`), `workflows` (`E7: Sampling Event`)_ | ⚠ No declaration |

</details>

## 2. Models missing Linked Entities subgraph

These formed model files do not contain a `//subgraph Linked Entities` block. Add the block to enable consistency checking.

- `frame_part/frame_part_v1.0.tsv`
- `heritage_object_part/heritage_object_part_v1.0.tsv`
