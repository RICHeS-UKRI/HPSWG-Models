# Model Consistency Report

_Generated: 2026-03-07 16:04 UTC_

**Individual model files analysed:** 32  
**Workflow/overview files analysed:** 2  

This report identifies potential inconsistencies in node naming across the HPSWG-Models TSV files. It is generated automatically on each push and is intended as a working tool for model authors, not a definitive quality assessment.

---

## 1. Workflow/overview vs individual model discrepancies

These are cases where the workflow (overview) TSV uses a different label than one or more individual models for a node with the same CRM class code connected via the same property. These are the highest-priority candidates for review, as they represent likely inter-model join breaks.

| Property | Class code | Workflow label(s) | Individual model label(s) | Files affected |
| --- | --- | --- | --- | --- |
| `O3_sampled_from (1 to 1)` | `E22` | `Heritage Object` | `Heritage Object`: sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv<br/>`Painting` ⚠: sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv | 12 |
| `P138i_has_representation (0 to n)` | `E22` | `Heritage Object<br/>Physical Sample` | `Heritage Object`: heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv | 2 |
| `P56i_is_found_on (1 to 1)` | `E22` | `Heritage Object` | `Heritage Object`: sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv<br/>`Painting` ⚠: sample_site/sample_site_v1.0.tsv | 4 |
| `P138i_has_representation (0 to n)` | `E26` | `Sample Site` | `Area of Interest` ⚠: sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv<br/>`Sample Site`: sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv | 2 |
| `P55_has_current_location (0 to 1)` | `E53` | `Storage Location` | `Institution or Address` ⚠: sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv | 4 |
| `P2_has_type (1 to 1)` | `E55` | `IIIF selector point (image-space)` | `Identifier Type` ⚠: location/location_v1.0.tsv, person/person_v0.9.tsv<br/>`condition state type` ⚠: heritage_object/heritage_object_v1.2.tsv, project/project_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv<br/>`family-name` ⚠: person/person_v0.9.tsv<br/>`given-name` ⚠: person/person_v0.9.tsv<br/>`honorific-title` ⚠: person/person_v0.9.tsv<br/>`sample format` ⚠: sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv<br/>`sample material type` ⚠: sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv<br/>`sample type` ⚠: sample/sample_v1.1.tsv | 12 |
| `P168_place_is_defined_by (0 to n)` | `E94` | `Sampling Point` | `Geometry (Space Primitive)` ⚠: location/location_v1.0.tsv | 1 |
| `P138i_has_representation (0 to n)` | `EX_Digital_Image` | `Analytical Sample Image<br/>Annotation Image<br/>Sample Image` | `Object Image` ⚠: heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv<br/>`Sample Image`: sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv<br/>`Site Image` ⚠: sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv | 9 |
| `O35i_was_observed_by (0 to n)` | `S13` | `Material Sample` | `Sample` ⚠: sample/sample_v0.9.tsv, sample/sample_v1.0.tsv | 2 |
| `O5_removed (1 to 1)` | `S13` | `Material Sample` | `Sample` ⚠: sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv | 5 |
| `O5i_was_removed_by (1 to 1)` | `S13` | `Material Sample` | `Sample` ⚠: sample/sample_v0.9.tsv, sample/sample_v1.0.tsv | 2 |
| `P31i_was_modified_by (0 to n)` | `S13` | `Material Sample` | `Sample` ⚠: sample/sample_v0.9.tsv, sample/sample_v1.0.tsv | 2 |

## 2. Predicate-scoped label variants across individual models

These cases show where the same CRM property connects nodes with the same class code but different labels in different individual models. Some of these will be intentional (an `E22` node genuinely represents different things in different models); others may be unintentional drift. Review each group to confirm intent.

| Property | Class code | Label | Files |
| --- | --- | --- | --- |
| `P125_used_object_of_type (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P126_employed (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P14_carried_out_by (1 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P16_used_specific_object (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P1_is_identified_by (1 to 1)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P2_has_type (1 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P31_has_modified (1 to 1)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P32_used_general_technique (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P33_used_specific_technique (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P48_has_preferred_identifier (1 to 1)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P4_has_time-span (1 to 1)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P67i_is_referred_to_by (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P70i_is_documented_in (0 to n)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `P7_took_place_at (1 to 1)` | `E11` | `Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Sample Modification` | sample_modification/sample_modification_v1.3.tsv |
| `O3_sampled_from (1 to 1)` | `E22` | `Heritage Object` | sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv |
|  |  | `Painting` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
| `P102_has_title (0 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P102_has_title (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P108i_was_produced_by (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P1_is_identified_by (0 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P1_is_identified_by (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P2_has_type (1 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P43_has_dimension (0 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P44_has_condition (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P45_consists_of (1 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P46_is_composed_of (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Heritage Object Support` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Painting Support` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Support` | heritage_object/heritage_object_v1.3.tsv |
| `P46i_forms_part_of (0 to 1)` | `E22` | `Heritage Object Part` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P46i_forms_part_of (0 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P48_has_preferred_identifier (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P50_has_current_keeper (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P52_has_current_owner (1 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P54_has_current_permanent_location (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P56i_is_found_on (1 to 1)` | `E22` | `Heritage Object` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Painting` | sample_site/sample_site_v1.0.tsv |
| `P67_refers_to (1 to n)` | `E22` | `Heritage Object Part` | sample_site/sample_site_v1.1.tsv |
|  |  | `Painting Part` | sample_site/sample_site_v1.0.tsv |
| `P67i_is_referred_to_by (0 to n)` | `E22` | `Painting` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P67i_is_referred_to_by (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P70i_is_documented_in (0 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting` | heritage_object/heritage_object_v1.0.tsv |
| `P138i_has_representation (0 to n)` | `E26` | `Area of Interest` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Sample Site` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `P89_falls_within (0 to n)` | `E26` | `Area of Interest` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Sample Site` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `P89_falls_within (1 to n)` | `E26` | `Area of Interest` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv |
|  |  | `Sample Site` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv |
| `O16_observed_value (1 to 1)` | `E3` | `Condition state (Object Status)` | sample_taking_event/sample_taking_event_v1.3.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Condition state (Sample Site Status)` | sample_taking_event/sample_taking_event_v1.4.tsv |
| `P2_has_type (1 to 1)` | `E3` | `Condition state` | sample/sample_v1.1.tsv |
|  |  | `Condition state (Object Status)` | heritage_object/heritage_object_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Condition state (Project Status)` | project/project_v1.0.tsv |
|  |  | `Condition state (Sample Site Status)` | sample_taking_event/sample_taking_event_v1.4.tsv |
|  |  | `Condition state (Sample Status)` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P44_has_condition (1 to 1)` | `E3` | `Condition state` | sample/sample_v1.1.tsv |
|  |  | `condition state` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv |
| `P44_has_condition (1 to n)` | `E3` | `Condition state (Object Status)` | heritage_object/heritage_object_v1.2.tsv |
|  |  | `Condition state (Project Status)` | project/project_v1.0.tsv |
|  |  | `Condition state (Sample Status)` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P45i_is incorporated in (0 to n)` | `E31` | `Heritage Object Documents` | heritage_object/heritage_object_v1.1.tsv |
|  |  | `Location Documents` | location/location_v1.0.tsv |
|  |  | `Modification Documents` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Painting Documents` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Person Documents` | person/person_v0.9.tsv |
|  |  | `Production Documents` | production_event/production_event_v1.0.tsv |
|  |  | `Related Documents` | project/project_v1.0.tsv |
|  |  | `Report or Document` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sample Documents` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `Storage Documents` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P67i_is_referred_to_by (0 to n)` | `E31` | `Location Documents` | location/location_v1.0.tsv |
|  |  | `Modification Documents` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Painting Documents` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Production Documents` | production_event/production_event_v1.0.tsv |
|  |  | `Sample Documents` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `P70i_is_documented_in (0 to n)` | `E31` | `Heritage Object Documents` | heritage_object/heritage_object_v1.1.tsv |
|  |  | `Modification Documents` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
|  |  | `Painting Documents` | heritage_object/heritage_object_v1.0.tsv |
|  |  | `Production Documents` | production_event/production_event_v1.0.tsv |
|  |  | `Related Documents` | project/project_v1.0.tsv |
|  |  | `Report or Document` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sample Documents` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P2_has_type (1 to 1)` | `E35` | `Alternate Title` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Full Title` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `P14_carried_out_by (1 to n)` | `E39` | `Group or Artist` | production_event/production_event_v1.0.tsv |
|  |  | `Institution or Person` | sample_modification/sample_modification_v1.3.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Modifier (Actor)` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
| `P50_has_current_keeper (1 to 1)` | `E39` | `Institution or Person` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `Storage Keeper` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P1_is_identified_by (0 to 1)` | `E41` | `Family Name` | person/person_v0.9.tsv |
|  |  | `Given Name` | person/person_v0.9.tsv |
|  |  | `Honorific / Title` | person/person_v0.9.tsv |
|  |  | `Unique System Label or ID` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `P1_is_identified_by (1 to 1)` | `E41` | `Sample Label` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
|  |  | `Sample Site Name/Number` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Unique System Label` | heritage_object/heritage_object_v1.0.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_site/sample_site_v1.0.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
|  |  | `Unique System Label or ID` | project/project_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P2_has_type (1 to 1)` | `E41` | `Family Name` | person/person_v0.9.tsv |
|  |  | `Given Name` | person/person_v0.9.tsv |
|  |  | `Honorific / Title` | person/person_v0.9.tsv |
| `P1_is_identified_by (0 to n)` | `E42` | `Alternative Identifier` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `Alternative Identifiers` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `External Identifier` | person/person_v0.9.tsv |
|  |  | `External Place Identifier` | location/location_v1.0.tsv |
| `P1_is_identified_by (1 to 1)` | `E42` | `Accession Number (custodian)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Custodian Identifier` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `P2_has_type (1 to 1)` | `E42` | `Accession Number (custodian)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `External Identifier` | person/person_v0.9.tsv |
|  |  | `External Place Identifier` | location/location_v1.0.tsv |
|  |  | `Persistent Identifier (PID)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P48_has_preferred_identifier (1 to 1)` | `E42` | `Persistant Identifier (PID)` | sample_site/sample_site_v1.0.tsv |
|  |  | `Persistent Identifier (IGSN)` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
|  |  | `Persistent Identifier (PID)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `Persistent Identifier (UUID)` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Persistent Identifier (e.g. IGSN)` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P4_has_time-span (0 to 1)` | `E52` | `Birth Date` | person/person_v0.9.tsv |
|  |  | `Death Date` | person/person_v0.9.tsv |
| `P4_has_time-span (1 to 1)` | `E52` | `Activity Timespan` | person/person_v0.9.tsv |
|  |  | `Modification Date` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
|  |  | `Production date` | production_event/production_event_v1.0.tsv |
|  |  | `Project Dates` | project/project_v1.0.tsv |
| `P54_has_current_permanent_location (1 to 1)` | `E53` | `Institution or Place` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Location` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P7_took_place_at (1 to 1)` | `E53` | `Place of Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
|  |  | `Place of Production` | production_event/production_event_v1.0.tsv |
|  |  | `Sampling Location` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P43_has_dimension (0 to n)` | `E54` | `Dimensions` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Heritage Object Dimensions` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
|  |  | `Painting Dimensions` | heritage_object/heritage_object_v1.0.tsv |
| `P43_has_dimension (1 to n)` | `E54` | `Sample dimension` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
|  |  | `Sample size` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P177_assigned_property_type` | `E55` | `sample attribute format` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `sample attribute status` | sample_modification/sample_modification_v1.3.tsv |
| `P2_has_type` | `E55` | `sample keywords` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
|  |  | `sample type` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `P2_has_type (0 to 1)` | `E55` | `Geometry Type` | location/location_v1.0.tsv |
|  |  | `storage status` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P2_has_type (0 to n)` | `E55` | `Discipline` | person/person_v0.9.tsv |
|  |  | `sample keywords` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `P2_has_type (1 to 1)` | `E55` | `Identifier Type` | location/location_v1.0.tsv, person/person_v0.9.tsv |
|  |  | `condition state type` | heritage_object/heritage_object_v1.2.tsv, project/project_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `family-name` | person/person_v0.9.tsv |
|  |  | `given-name` | person/person_v0.9.tsv |
|  |  | `honorific-title` | person/person_v0.9.tsv |
|  |  | `sample format` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `sample material type` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `sample type` | sample/sample_v1.1.tsv |
| `P2_has_type (1 to n)` | `E55` | `Project Type` | project/project_v1.0.tsv |
|  |  | `modification type` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
|  |  | `object type` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `production type` | production_event/production_event_v1.0.tsv |
|  |  | `sample status` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `storage type` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P45_consists_of (0 to n)` | `E57` | `Colourant` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
|  |  | `Other Material` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `P45_consists_of (1 to n)` | `E57` | `Binding Medium` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
|  |  | `Medium` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Painting Medium` | heritage_object/heritage_object_v1.0.tsv |
| `P10_falls_within (0 to 1)` | `E7` | `Parent Project` | project/project_v1.0.tsv |
|  |  | `Project` | project/project_v1.0.tsv |
| `P1_is_identified_by (1 to 1)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P4_has_time-span (1 to 1)` | `E7` | `Period of Activity` | person/person_v0.9.tsv |
|  |  | `Project` | project/project_v1.0.tsv |
| `P67i_is_referred_to_by (1 to 1)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P70i_is_documented_in (0 to n)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `crm:P9i_forms_part_of` | `E7` | `Project` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P45i_is incorporated in (0 to n)` | `E73` | `Credit Line` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Description` | sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Description Text` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
|  |  | `Physical Description` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Project Description` | project/project_v1.0.tsv |
|  |  | `Reason for Sampling` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Site Selection Comment` | sample_site/sample_site_v1.4.tsv |
|  |  | `Site Selection Description` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `P67i_is_referred_to_by (0 to 1)` | `E73` | `Credit Line` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Site Selection Comment` | sample_site/sample_site_v1.4.tsv |
|  |  | `Site Selection Description` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `P67i_is_referred_to_by (1 to 1)` | `E73` | `Description` | sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Description Text` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, production_event/production_event_v1.0.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
|  |  | `Physical Description` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
|  |  | `Project Description` | project/project_v1.0.tsv |
|  |  | `Site Selection Description` | sample_site/sample_site_v1.0.tsv |
| `P138i_has_representation (0 to n)` | `EX_Digital_Image` | `Object Image` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Sample Image` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `Site Image` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `PX_has_main_representation (0 to 1)` | `EX_Digital_Image` | `Main Object Image` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `Main Sample Image` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
|  |  | `Main Site Image` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `has legend` | `Properties` | `P46=is composed of (part–whole); P198=holds or supports (mechanical support between distinct objects); P56=bears feature (inseparable surface/embedded feature).` | frame_part/frame_part_v1.0.tsv |
|  |  | `P46=is composed of (part–whole); P198=holds or supports / P198i=is held or supported by (mechanical support between distinct objects); P56=bears feature (inseparable surface/embedded feature).` | heritage_object_part/heritage_object_part_v1.0.tsv |
| `P2_has_type` | `aat` | `300055642` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
|  |  | `300387580` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `P2_has_type (1 to 1)` | `aat` | `300312355` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `300387580` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `300417209` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
|  |  | `300417227` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |

## 3. Shared nodes (exact name match across models)

Nodes that appear with exactly the same name in more than one model file. These are the current inter-model linking points. Consistency here is good; this section is informational.

| Node | Appears in |
| --- | --- |
| `Addition/Extension (integrated) (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Addition/Extension (separable) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `E11: Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
| `E11: Sample Modification` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E12: Production Event` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E16: Measurement` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E18: Modified Thing` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
| `E22: Heritage Object` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E22: Heritage Object Part` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `E22: Heritage Object Support` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
| `E22: Painting` | heritage_object/heritage_object_v1.0.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_site/sample_site_v1.0.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
| `E26: Area of Interest` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `E26: Sample Site` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E29: Method / Protocol` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E29: Method or Procedure` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E31: Modification Documents` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
| `E31: Report or Document` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E31: Sample Documents` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E35: Alternate Title` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E35: Full Title` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E39: Institution or Person` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E39: Modifier (Actor)` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv |
| `E3: Condition state (Object Status)` | heritage_object/heritage_object_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E3: Condition state (Sample Status)` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E3: condition state` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv |
| `E41: Sample Label` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `E41: Sample Site Name/Number` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `E41: Unique System Label` | heritage_object/heritage_object_v1.0.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_site/sample_site_v1.0.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
| `E41: Unique System Label or ID` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, project/project_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E42: Accession Number (custodian)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E42: Alternative Identifier` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E42: Alternative Identifiers` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E42: Custodian Identifier` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `E42: Persistent Identifier (IGSN)` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `E42: Persistent Identifier (PID)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, project/project_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `E42: Persistent Identifier (UUID)` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E42: Persistent Identifier (e.g. IGSN)` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E52: Modification Date` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E52: Sampling Date` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E53: Institution or Address` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E53: Institution or Place` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E53: Place of Modification` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E53: Sampling Location` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E53: Storage Location` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E54: Heritage Object Dimensions` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
| `E54: Sample dimension` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `E54: Sample size` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E55: Identifier Type` | location/location_v1.0.tsv, person/person_v0.9.tsv |
| `E55: condition state` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `E55: condition state type` | heritage_object/heritage_object_v1.2.tsv, project/project_v1.0.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E55: material of interest` | sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv |
| `E55: modification type` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E55: object type` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E55: sample format` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E55: sample keywords` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E55: sample material type` | sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E55: sample type` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv |
| `E55: technique` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E55: tool/equipment` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E55:condition state type` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `E57: Binding Medium` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
| `E57: Colourant` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv |
| `E57: Material Used` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E57: Other Material` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E70: Tool / Equipment` | sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E73: Credit Line` | heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E73: Description` | sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E73: Description Text` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv |
| `E73: Physical Description` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `E73: Reason for Sampling` | sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E73: Site Selection Description` | sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `E78: Collection (Curated Holding)` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `E7: Project` | project/project_v1.0.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E7: Sampling Event` | sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `EX_Digital_Image: Main Object Image` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `EX_Digital_Image: Main Sample Image` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `EX_Digital_Image: Main Site Image` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `EX_Digital_Image: Object Image` | heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `EX_Digital_Image: Sample Image` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `EX_Digital_Image: Site Image` | sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv |
| `EX_Digital_Image_Region` | sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `Fixtures/Fittings/Hardware (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Formats: object=E22 Human-Made Object; object_bn=S20 Rigid Physical Feature (linked with P46); place_bn=S20 Rigid Physical Feature (linked with P56); idea_bn=to review/interpretive.` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Gilding Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Ground/Preparation (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Ground/Preparation Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Inscriptions/Numbers (painted/incised) (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Label/Seal (attached object) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Painting (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Repairs/Mends to Support (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Restoration Additions (general) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Restoration Retouch/Reconstruction (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `S13/E19: Sample` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv |
| `S13: Sample` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv |
| `S24: Sample Splitting` | sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S27: Observation` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S2: Sample Taking` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample/sample_v1.1.tsv, sample/sample_v1.2.tsv, sample/sample_v1.3.tsv, sample/sample_v1.4.tsv, sample/sample_v1.5.tsv, sample_site/sample_site_v1.0.tsv, sample_site/sample_site_v1.1.tsv, sample_site/sample_site_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.0.tsv, sample_taking_event/sample_taking_event_v1.1.tsv, sample_taking_event/sample_taking_event_v1.2.tsv, sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S4: Observation` | sample_taking_event/sample_taking_event_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `Sample Sites/Voids (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Surface Coatings (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Surface Dirt/Accretion/Efflorescence (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Varnish Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `aat:300055642` | sample/sample_v0.9.tsv, sample/sample_v1.0.tsv |
| `aat:300312355` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `aat:300387580` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample/sample_v0.9.tsv, sample/sample_v1.0.tsv, sample_modification/sample_modification_v1.0.tsv, sample_modification/sample_modification_v1.1.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `aat:300417209` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |
| `aat:300417227` | heritage_object/heritage_object_v1.0.tsv, heritage_object/heritage_object_v1.1.tsv, heritage_object/heritage_object_v1.2.tsv, heritage_object/heritage_object_v1.3.tsv |

## 4. Files analysed

| File | Type |
| --- | --- |
| `frame_part/frame_part_v1.0.tsv` | Individual model |
| `heritage_object/heritage_object_v1.0.tsv` | Individual model |
| `heritage_object/heritage_object_v1.1.tsv` | Individual model |
| `heritage_object/heritage_object_v1.2.tsv` | Individual model |
| `heritage_object/heritage_object_v1.3.tsv` | Individual model |
| `heritage_object_part/heritage_object_part_v1.0.tsv` | Individual model |
| `location/location_v1.0.tsv` | Individual model |
| `person/person_v0.9.tsv` | Individual model |
| `production_event/production_event_v1.0.tsv` | Individual model |
| `project/project_v1.0.tsv` | Individual model |
| `sample/sample_v0.9.tsv` | Individual model |
| `sample/sample_v1.0.tsv` | Individual model |
| `sample/sample_v1.1.tsv` | Individual model |
| `sample/sample_v1.2.tsv` | Individual model |
| `sample/sample_v1.3.tsv` | Individual model |
| `sample/sample_v1.4.tsv` | Individual model |
| `sample/sample_v1.5.tsv` | Individual model |
| `sample_modification/sample_modification_v1.0.tsv` | Individual model |
| `sample_modification/sample_modification_v1.1.tsv` | Individual model |
| `sample_modification/sample_modification_v1.3.tsv` | Individual model |
| `sample_site/sample_site_v1.0.tsv` | Individual model |
| `sample_site/sample_site_v1.1.tsv` | Individual model |
| `sample_site/sample_site_v1.3.tsv` | Individual model |
| `sample_site/sample_site_v1.4.tsv` | Individual model |
| `sample_storage_unit/sample_storage_unit_v1.0.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.0.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.1.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.2.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.3.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.4.tsv` | Individual model |
| `sampling_event/sampling_event_v1.0.tsv` | Individual model |
| `sampling_event/sampling_event_v1.1.tsv` | Individual model |
| `workflows/workflow_cidoc_sample_taking_v1.0.tsv` | Workflow/overview |
| `workflows/workflow_user_sample_taking_v1.0.tsv` | Workflow/overview |
