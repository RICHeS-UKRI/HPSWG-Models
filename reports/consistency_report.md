# Model Consistency Report

_Generated: 2026-03-07 18:02 UTC_

**Individual model files analysed:** 13  
**Workflow/overview files analysed:** 1  

This report checks consistency of inter-model linking nodes -- the entities declared in each model's `//subgraph Linked Entities` block and each model's key entity. High-multiplicity classes (E55 type terms, identifiers, images) are ignored unless explicitly declared as linked entities.

---

## 1. Model update checklist (workflow conflicts)

These models contain linked entity labels that differ from the canonical labels used in the workflow/overview TSV. Update the model to use the canonical label and increment its version number.

**Models requiring updates:** 1  
**Total label changes needed:** 1  

### `project/project_v1.0.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E7` | `Project` | `Sampling Event` |

## 2. Inter-model disagreements (no workflow reference)

These class codes appear as linked entities in more than one model with different labels, and are not covered by the workflow. Human decision needed: agree on a canonical label, then add it to the workflow and update the affected models.

### `E22`

| Label | Used in |
| --- | --- |
| `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
| `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |

## 3. Models missing Linked Entities subgraph

These formed model files do not contain a `//subgraph Linked Entities` block. Their linking nodes cannot be checked for consistency until the block is added.

- `frame_part/frame_part_v1.0.tsv`
- `heritage_object_part/heritage_object_part_v1.0.tsv`

## 4. Verified shared nodes

Linked entity nodes that are consistent between the workflow and at least one individual model. These are the confirmed inter-model join points.

| Class code | Canonical label | Consistent in |
| --- | --- | --- |
| `E7` | `Sampling Event` | sampling_event/sampling_event_v1.1.tsv |
