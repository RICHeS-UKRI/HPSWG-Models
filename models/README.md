# Models

This folder contains all model definitions used in this project.  
Models are expressed as simple TSV triple structures and are designed for use with the
**National Gallery Dynamic Modeller**.

These models support CIDOC CRM v7.1.3-aligned documentation of:

- Paintings and their components
- Heritage samples and analytical context
- Conservation, technical imaging, and material relationships
- Higher-level NG-wide relationships

Each model is maintained in its own subfolder and may contain multiple versioned TSV files.
Version history and detail is documented in the individual model README pages.

---

## Folder Structure

models/
ng_models_vX.Y.tsv
<model_name>/
<model_name>_vA.B.tsv
README.md

---

## Available Model Folders

<!-- BEGIN AUTO: MODEL-FOLDERS -->
### NG-wide model versions

| Version | Raw TSV | Visualisation |
|---------|---------|---------------|
| 0.1 | [TSV](https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/ng_models_v0.1.tsv) | [Open in Modeller](https://research.nationalgallery.org.uk/lab/modelling/?url=https://raw.githubusercontent.com/jpadfield/HPSWG-Models/refs/heads/main/models/ng_models_v0.1.tsv) |

### Model folders

- [`frame_part/`](./frame_part)
- [`heritage_object/`](./heritage_object)
- [`heritage_object_part/`](./heritage_object_part)
- [`location/`](./location)
- [`old_samples/`](./old_samples)
- [`person/`](./person)
- [`production_event/`](./production_event)
- [`project/`](./project)
- [`sample/`](./sample)
- [`sample_modification/`](./sample_modification)
- [`sample_site/`](./sample_site)
- [`sample_storage_unit/`](./sample_storage_unit)
- [`sample_taking_event/`](./sample_taking_event)
- [`sampling_event/`](./sampling_event)
- [`workflows/`](./workflows)
<!-- END AUTO: MODEL-FOLDERS -->

---

## Creating or Updating a Model

1. Add a new folder inside `models/`.
2. Add a TSV file using the pattern `<model>_v0.1.tsv`.
3. Commit and push; the GitHub Action will:
   - Create or update that model’s README  
   - Update the top-level README  
   - Integrate the model into the master list

---

If you would like help constructing new models or integrating them with CIDOC CRM, please open an
issue or contact the maintainers.
