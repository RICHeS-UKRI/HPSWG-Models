# Ontologies

This document records the semantic ontologies used across the HPSWG-Models repository, including the versions in use, canonical namespaces, and links to source documentation.

All models in this repository are expressed using CIDOC CRM 7.1.3 as the core ontology. Extension ontologies (CRMdig, CRMsci) have been lightly adjusted for compatibility with this version -- see the notes column below for details.

ResearchSpace-specific classes and properties are included where the National Gallery's ResearchSpace deployment requires them. CRM-aligned alternatives are planned for future inclusion alongside these terms.

## Ontology reference

| Ontology | Version | Prefix | Namespace | Documentation | Download |
|----------|---------|--------|-----------|---------------|----------|
| CIDOC CRM | 7.1.3 | `crm` | `http://www.cidoc-crm.org/cidoc-crm/` | [Link](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html) | [RDFS](https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3.rdfs) |
| CRMdig | 4.0 | `crmdig` | `http://www.ics.forth.gr/isl/CRMdig/` | [Link](https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v4.0.html) | [RDFS](https://cidoc-crm.org/crmdig/ModelVersion/version-4.0) |
| CRMsci | 3.0 | `crmsci` | `http://www.ics.forth.gr/isl/CRMsci/` | [Link](https://cidoc-crm.org/crmsci/ModelVersion/crmsci-3.0) | [RDFS](https://cidoc-crm.org/crmsci/ModelVersion/crmsci-3.0) |
| ResearchSpace | _see notes_ | `EX` | `https://www.researchspace.org/resource/system/` | [Link](https://github.com/researchspace/researchspace) | -- |

## Compatibility notes

**CRMdig and CRMsci** have each been adjusted at a small number of points to ensure compatibility with CIDOC CRM 7.1.3. Where adjustments have been made, the relevant classes and properties remain semantically equivalent to the published versions. Full details of any deviations will be recorded here as the models mature.

**ResearchSpace terms** are used pragmatically within the National Gallery's ResearchSpace deployment. These are not part of a published ontology standard. Work is planned to document CRM-equivalent alternatives for each ResearchSpace term used, making the models portable beyond the ResearchSpace platform.

## Updating this file

This file is maintained manually. When ontology versions are updated, update both this file and `scripts/ontologies.json`, which drives the short ontology reference tables in the model READMEs.
