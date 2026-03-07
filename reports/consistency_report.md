# Model Consistency Report

_Generated: 2026-03-07 20:20 UTC_

**Individual model files analysed:** 13  
**Workflow/overview files analysed:** 1  

This report checks consistency of inter-model linking nodes declared in each model's `//subgraph Linked Entities` block. Only declared linked entities are checked -- high-multiplicity classes such as E55 type terms are not flagged unless explicitly declared.

**Status key:**
- ✅ Consistent -- class codes match exactly
- 🔵 Hierarchy match -- related via CRM class hierarchy, confirm intent
- ⚠️ Class mismatch -- classes not related, check required
- ❓ Unknown target -- declared target folder not found in repo
- ⚠ No declaration -- `//links` directive missing, suggestions provided

---

## 1. Per-model link validation

Each model's linked entities are listed with their declared target models and consistency status. Where no `//links` declaration exists, possible targets are suggested based on matching class codes.

<details>
<summary><strong>heritage_object/heritage_object_v1.3.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Institution or Person` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Institution or Place` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E54: Dimensions` | `E54` | _No matching models found_ | ⚠ No declaration |
| `E78: Collection (Curated Holding)` | `E78` | _No matching models found_ | ⚠ No declaration |
| `E31: Report or Document` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E57: Medium` | `E57` | _No matching models found_ | ⚠ No declaration |
| `E57: Other Material` | `E57` | _No matching models found_ | ⚠ No declaration |
| `E22: Support` | `E22` | _Suggested: `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E12: Production Event` | `E12` | _Suggested: `production_event` (`E12: Production`)_ | ⚠ No declaration |
| `EX_Digital_Image: Main Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |
| `EX_Digital_Image: Object Image` | `EX_Digital_Image` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>location/location_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E31: Location Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E94: Geometry (Space Primitive)` | `E94` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>person/person_v0.9.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E40: Legal Body (Affiliation)` | `E40` | _No matching models found_ | ⚠ No declaration |
| `E74: Group (Membership)` | `E74` | _No matching models found_ | ⚠ No declaration |
| `E51: Contact Point` | `E51` | _No matching models found_ | ⚠ No declaration |
| `E53: Place (Residence)` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |

</details>

<details>
<summary><strong>production_event/production_event_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E22: Painting` | `E22` | _Suggested: `heritage_object` (`E22: Heritage Object`), `sample_storage_unit` (`E22: Storage Unit`)_ | ⚠ No declaration |
| `E39: Group or Artist` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Place of Production` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Production Documents` | `E31` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>project/project_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Project Owner` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E39: Other Actors` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E31: Related Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E7: Parent Project` | `E7` | _Suggested: `sampling_event` (`E7: Sampling Event`), `workflows` (`E7: Sampling Event`)_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample/sample_v1.6.tsv</strong></summary>

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
<summary><strong>sample_modification/sample_modification_v1.3.tsv</strong></summary>

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
<summary><strong>sample_site/sample_site_v1.4.tsv</strong></summary>

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
<summary><strong>sample_storage_unit/sample_storage_unit_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |
| `E39: Storage Keeper` | `E39` | _No matching models found_ | ⚠ No declaration |
| `E53: Storage Location (Place)` | `E53` | _Suggested: `location` (`E53: Location`)_ | ⚠ No declaration |
| `E31: Storage Documents` | `E31` | _No matching models found_ | ⚠ No declaration |
| `E29: Storage Method / Protocol` | `E29` | _No matching models found_ | ⚠ No declaration |

</details>

<details>
<summary><strong>sample_taking_event/sample_taking_event_v1.4.tsv</strong></summary>

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
<summary><strong>sampling_event/sampling_event_v1.1.tsv</strong></summary>

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
