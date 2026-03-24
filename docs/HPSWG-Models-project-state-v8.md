

HPSWG-Models-project-state-v7.md
md


sampling_activity_v1.1.tsv
tsv

Hi, I would like to continue working to add //field comments to some additional sample related models - can we work on the sample_activity model next please. Here also is the word document table for reference Required?Human understandable LabelAlternative Labels (Types)CRM CodeLabel descriptionOptionalSampling activity PIDPersistent Identifier (PID)E42An optional public unique identifier (PID) for the sample activity✓Unique System Label or IDDatabase or System iD/LabelE41Required within some documentation or database systems, such as ResearchSpace. Any of the IDs defined could be flagged as a preferred ID within a documentation system.OptionalReason for sampling activityOverall purposeE73The overall motivation for carrying out the sampling activity/session (at object level). This describes any wider research, conservation, or technical questions being addressed that apply to more than one of the individual sample takings.OptionalSampling activity commentsDescriptionE73Any additional relevant information about the taking of the samples.  ✓Cross-reference to Heritage ObjectHeritage Object, Link to Heritage ObjectE22The selected object for the sample taking activity. (This relationship is required to simplify the workflow - Objects will also be related at Sample Taking level as needed by the CRM Sci, but these values from a form point of view will be the same for all sample taking events within a given sampling event.)OptionalCross-reference to projectProjectE7Link to a project to which the sample taking belongs, e.g. conservation treatment, cataloguing programme etc, and to the project metadata (e.g. the conservator carrying out a treatment, the curator in charge of cataloguing, the dates of the project etc)OptionalRelated Document(s)Reports, Publications, Summaries, etcE31Primarily related to authored notes, reports and publications, however there is a whole range of relevant documents that can reference or be linked to this event.✓Date of sampling activitySampling Date, DateVia E52The date (DD/MM/YYYY) when the samples were taken.OptionalMethodProcedureE29A defined sampling protocol or procedure that may be referenced for standard approaches.✓Planned byE39Name of person (or institution) responsible for planning the sampling activity - this is likely to be the same person (or institution) who actually takes the individual related sample(s), but it might not be. When person is unknown, ‘unknown person’ or the institution (which is usually known) should be recorded.✓Location of sampling activityLocation, Sampling LocationE53The physical place where the sampling activity occurred.OptionalStatus of heritage object (overall) at time of sampling  E3 via S4The state of the object as a whole at the time of sampling (e.g. During cleaning)✓Cross-reference to sample takingS2A reference to the separate sample taking events relating to this sampling activity.

Show more
23 Mar

Viewed 2 files
Viewed 2 files
Good, I have the file and the context. Let me also check the project state's //field directive syntax section before drafting, so I have the full picture.


Viewed 2 files
Viewed 2 files
Good, I have everything I need. Let me now map the Word document table against the TSV nodes to plan the //field directives.

Here is my proposed mapping before I write anything. Let me walk through each row in the Word table and match it to the corresponding node in the TSV:

Word table row → TSV node → proposed //field or //field-via

Sampling activity PID → E42: Persistent Identifier (UUID) -- P48 predicate, (1 to 1), Optional in Word → behaviour:pid
Unique System Label or ID → E41: Unique System Label or ID -- P1, (1 to 1), Required → behaviour:system-id
Reason for sampling activity → E73: Reason for Sampling -- P17, (0 to 1), Optional → behaviour:free-text
Sampling activity comments → E73: Description -- P67i, (1 to 1), Required → behaviour:free-text
Cross-reference to Heritage Object → E22: Heritage Object -- P12, (1 to 1), Required → behaviour:select
Cross-reference to project → E7: Project -- P9i/crm:P9i_forms_part_of, (0 to n) Optional → behaviour:select
Related Document(s) → E31: Report or Document -- P70i, (0 to n), Optional → behaviour:select
Date of sampling activity → E52: Sampling Date -- P4, (1 to 1), Required → //field-via via E52: Sampling Date, or just field on E52: Sampling Date directly since it is directly on the main entity
Method → E29: Method or Procedure -- P33, (1 to n), Optional → behaviour:select
Planned by → E39: Institution or Person -- P14, (1 to n), Required → behaviour:select
Location of sampling activity → E53: Sampling Location -- P7, (1 to 1), Optional → behaviour:select
Status of heritage object (overall) at time of sampling → E3: Condition state (Object Status) -- reached via S4: Observation → P9_consists_of then O8_observed / O16_observed_value then P2_has_type. This is a //field-via via S4: Observation. But the actual captured value is E55: condition state type → behaviour:list. The intermediate is complex (two hops through S4). Worth discussing.
Cross-reference to sample taking → S2: Sample Taking -- P9, (1 to n), Required → behaviour:select
A few points to discuss before I write this up:

Item 8 (Date): E52: Sampling Date is a direct predicate on E7: Sampling Event, so this is a straightforward //field on E52: Sampling Date, not a //field-via. The E52 node does not currently have a tooltip in the model body (only the (1 to 1) multiplicity is noted in the predicate, and there is a tooltip). Actually it does have a tooltip on line 41. Good.

Item 12 (Object status): The path is E7: Sampling Event → P9_consists_of → S4: Observation → O16_observed_value → E3: Condition state (Object Status) → P2_has_type → E55: condition state type. That is three hops from the primary entity, well beyond what //field-via handles (which is a single intermediate). What do you think is the right approach here? Options are:

A //field-via on E55: condition state type via S4: Observation -- this collapses the path notation but the CRM code path in the table would read S4 > E55, losing the intermediate E3 step. That might be acceptable given it is a summary table.
Leave it as a //field on E3: Condition state (Object Status) with a note that the type is what is captured, relying on the tooltip to explain the structure.
A //field-via on E3: Condition state (Object Status) via S4: Observation since E3 is probably the meaningful unit from a data entry point of view, with the E55 type being the actual entered value. The description can explain that a type is selected.
My inclination is //field-via E3: Condition state (Object Status) via S4: Observation with behaviour:list and an explicit description that captures both the nature of the field and the fact that a controlled type is selected -- this keeps it consistent with how other similar fields are handled and doesn't try to express every hop in the path.

Do you agree with the above mapping and the proposed approach for item 12? Also, one small note: the Word table marks the PID as Optional (no tick) but the TSV predicate reads (1 to 1) -- should the multiplicity on P48 be corrected to (0 to 1) to match the Word table intent?


//flowchart LR E7: Sampling Activity tooltip The overall sampling session or campaign event in which one or more individual sample extractions were carried out. event-fs32 E7: Sampling Activity has note Document Note: Sampling Activity Model Overview Document Note: Sampling Activity Model Overview t

pasted

Sorry, I needed to make a few changes tot he sampling activity model as a result of the name change

23 Mar
No problem. I can see the updated file -- the key changes are the rename from "Sampling Event" to "Sampling Activity" throughout, and the E7: Sampling Activity primary node label is now consistent.

Your mapping analysis still holds. Let me just confirm my reading of the updated predicates for multiplicity:

P48 is still (1 to 1) -- you noted this should probably be (0 to 1) to match the Word table (Optional). Worth correcting in the same pass.
crm:P9i_forms_part_of on the Project link has no multiplicity brackets -- the field table parser will flag this as ✓* (required, defaulted). Should be (0 to n) since the Word table marks it Optional.
Do you want to fix both of those multiplicity issues as part of this pass? And do you agree with the //field-via E3: Condition state (Object Status) via S4: Observation approach for item 12, with behaviour:list and an explicit description?


//flowchart LR E7: Sampling Activity tooltip The overall sampling session or campaign event in which one or more individual sample extractions were carried out. event-fs32 E7: Sampling Activity has note Document Note: Sampling Activity Model Overview Document Note: Sampling Activity Model Overview t

pasted

With the condition state this is an actual literal value in the Sampling Activity form so we are not going via a linked entity - the semantics will need to be sorted, but the actual value in a potential form is more straight forward and yes it would be from a list. I have fixed the two multiplicity issues see attached.

23 Mar
Both multiplicity fixes confirmed. And the clarification on the condition state is helpful -- it is a directly entered list value within the sampling activity form, so treating it as //field-via E3: Condition state (Object Status) via S4: Observation with behaviour:list is the right call. The multi-hop semantics are a modelling concern; from a form perspective it is a single field.

Here are the proposed //field directives in full. Please review before I produce the updated file.

//field E42: Persistent Identifier (UUID) | 1 | Sampling Activity PID; PID | behaviour:pid
//field E41: Unique System Label or ID | 2 | Database or System ID; Label | behaviour:system-id
//field E22: Heritage Object | 3 | Heritage Object; Link to Heritage Object | behaviour:select
//field E73: Reason for Sampling | 4 | Reason for Sampling Activity; Overall Purpose | behaviour:free-text
//field E73: Description | 5 | Sampling Activity Comments | behaviour:free-text
//field E31: Report or Document | 6 | Related Document(s); Reports; Publications; Summaries | behaviour:select
//field E52: Sampling Date | 7 | Date of Sampling Activity; Sampling Date; Date | behaviour:free-text
//field E29: Method or Procedure | 8 | Method; Procedure | behaviour:select
//field E39: Institution or Person | 9 | Planned By | behaviour:select
//field E53: Sampling Location | 10 | Location of Sampling Activity; Location; Sampling Location | behaviour:select
//field E7: Project | 11 | Project | behaviour:select
//field-via E3: Condition state (Object Status) via S4: Observation | 12 | Status of Heritage Object at Time of Sampling; Object Status | The state of the object as a whole at the time of sampling, for example during cleaning. | behaviour:list
//field S2: Sample Taking | 13 | Cross-reference to Sample Taking | behaviour:select
A few points to confirm before I write the file:

E52: Sampling Date -- I have used behaviour:free-text since dates are typically typed directly. If your forms use a date-picker widget that would be better tagged differently, but there is no current date behaviour tag. Let me know if you want to add one or use free-text for now.
E73: Description -- the human label derived from the node will be "Description", which is generic. The Word table label is "Sampling activity comments". I have put "Sampling Activity Comments" as an alternative, but given the design note that node labels should be improved rather than compensated for with alternatives, it might be worth renaming the node to E73: Sampling Activity Comments in the model. Worth doing in this pass or leave for the tooltip audit?
Order -- I have followed the Word table row order. These are provisional as noted in the project state; final order will be set once the ordering document is produced.
E7: Project -- the node label will render as "Project" in the field table, which is fine.

//flowchart LR E7: Sampling Activity tooltip The overall sampling session or campaign event in which one or more individual sample extractions were carried out. event-fs32 E7: Sampling Activity has note Document Note: Sampling Activity Model Overview Document Note: Sampling Activity Model Overview t

pasted

I am currently working with

23 Mar
Good -- this version is clean and the changes all look correct. A few small things to flag before I confirm it is ready:

1. Stale reference on line with E73: Description

There is a leftover reference to the old node name in the body:

E73: Description	P45i_is incorporated in (0 to n)	E31: Report or Document	|document
This should now read E73: Sampling Activity Comment to match the renamed node. Otherwise the Dynamic Modeller will render it as a separate orphaned node.

2. E39: Planned by alternatives

The current alternatives in the //field line are Institution; Person, which are really the types of actor rather than alternative labels for the field name. The Word table has "Planned by" as the primary label with no stated alternatives. Since the node label now reads well as plain language ("Planned by"), the alternatives could either be dropped or replaced with something more useful like Responsible Actor; Sampler. Worth a quick decision -- drop them, keep them, or replace?

3. E52: Sampling Date tooltip

The tooltip currently says "The period of the full event including all the time spans of all of the related sample taking events." That is accurate semantically but reads oddly as a field description in a form context. It may be worth a light edit -- something like "The date or date range of the sampling activity, spanning all related sample taking events." -- but this is a tooltip audit concern rather than a blocker.

Shall I produce the corrected file with just the E73: Description fix applied, and your decision on the E39 alternatives?


sample_taking_v1.7.tsv
tsv

Ok, I have made those changes, moving on here is the sample taking table This metadata relates to individual samples taken within an overall sampling activity. The purpose of this separate category is to avoid having to copy/paste more general info at the individual sample level. Any information specific to this sample taking event - for example if this metadata is different to that within the wider sampling activity - should be required here.
Required?
Human understandable Label
Alternative Labels - (Types)
CRM Code
Label description
Optional
Sample taking PID
Persistent Identifier (PID)
E42
An optional public unique identifier for the sample taking event
✓
Sample Taking System iD
Database or System iD/Label, Unique System Label or ID
E42
Required within some documentation or database systems, such as ResearchSpace required label. Any of the IDs defined could be flagged as a preferred ID within a documentation system.
Optional
Sample taking date
Date
E52
The optional defined period of the specific sample taking event – if different from the parent sampling activity.
Optional
Sample taking comment
Description
E73
Any additional relevant information about the taking of the sample.
Optional
Reason for Sampling
E73
Sample-specific reasons (different to the general reason indicated at the Sampling Activity Level)
Optional
Related Document
Reports, Publications, Summaries, etc
E31
Primarily related to authored notes, reports and publications, however there is a whole range of relevant documents that can reference or be linked to this event.
✓
Cross-reference to sample
Removed, Sample, Created
S13
A reference to the sample that was taken in this sample taking event – Class to be Confirmed as dual S13/E22 construct may be needed for the sample.
✓
Cross-reference to sample site
Sample Site
E26
A reference to the sample site relating to this sample taking event
Optional
Sampling method
Method, Procedure
E29
The defined process or protocol followed during the sampling or analysis activity (if different from method indicated in sampling activity).
Optional
Location of Sample taking event
E53
Location where the sample taking took place. Again optional if different from the parent activity.
Optional
Sample taken by
Sampler, Taken by, Sampling carried out by, (Institution or Person)
E39
Name of person (or institution) who took the sample (if different from the person/institution defined at sampling event level). When person is unknown, ‘unknown person’ or the institution (which is usually known) should be recorded.
Optional
State of sampling site at time of sampling
Via S4
State of the object at the sampling site at the time of the sample taking, e.g. varnish removed 
✓
Cross-reference to Heritage Object
Heritage Object, Link to Heritage Object
E22
 E22 is a duplicate to the one defined at the parent activity but a key property is required here for the CRM Sci linking the S2, via an O3 to the E22. and the last version of the model

Show more
23 Mar
Let me read the sample taking model first.


Reading the sample taking TSV file
Reading the sample taking TSV file
Good. I have the model. Now let me map the Word table against the TSV nodes carefully, noting anything that needs discussion.

Proposed mapping:

Sample taking PID → E42: Persistent Identifier (UUID) -- P48, (1 to 1). Word table says Optional, but the predicate is (1 to 1). Same issue as sampling activity -- should this be corrected to (0 to 1) in the same pass? I will flag this.
Sample Taking System ID → E41: Unique System Label or ID -- P1, (1 to 1), Required. behaviour:system-id.
Sample taking date → E52: Sampling Date -- P4, (1 to 1). Word table says Optional. Again the predicate says required. Worth discussing -- is the date genuinely optional at sample taking level (since it may be inherited from the parent activity)?
Sample taking comment → E73: Description -- P67i, (1 to 1). behaviour:free-text.
Reason for Sampling → E73: Reason for Sampling -- P17, (0 to 1), Optional. behaviour:free-text.
Related Document → E31: Report or Document -- P70i, (0 to n), Optional. behaviour:select.
Cross-reference to sample → E22/S13: Heritage Sample -- O5_removed, (1 to 1), Required. behaviour:select. The node label will render as "Heritage Sample" -- the Word table label is "Cross-reference to sample". The alternative labels "Removed; Sample; Created" could be used. Worth noting the "Class to be Confirmed" caveat in the Word table, but the E22/S13 placeholder is the current approach so we proceed with it.
Cross-reference to sample site → E26: Sample Site -- O4_sampled_at, (1 to 1), Required. Word table says Optional. Another multiplicity discrepancy to flag.
Sampling method → E29: Method or Procedure -- P33, (1 to n). Word table says Optional but (1 to n) is required. Flag.
Location of Sample taking event → E53: Sampling Location -- P7, (1 to 1). Word table says Optional. Flag.
Sample taken by → E39: Organisation or Person -- P14, (1 to n). Word table says Optional but (1 to n) is required. Flag.
State of sampling site at time of sampling → //field-via E3: Condition state (Sample Site Status) via S4: Observation -- behaviour:list. Same pattern as sampling activity. Description: "The condition or treatment state of the sample site at the time of sampling, for example varnish removed."
Cross-reference to Heritage Object → E22: Heritage Object -- O3_sampled_from, (1 to 1), Required. behaviour:select. The Word table note explains this is structurally required for CRMsci even though it duplicates the parent activity link.
Multiplicity discrepancies to resolve before writing directives:

There are several cases where the Word table says Optional but the TSV predicate says (1 to 1) or (1 to n). These are:

Field	TSV multiplicity	Word table
E42: Persistent Identifier (UUID)	(1 to 1)	Optional
E52: Sampling Date	(1 to 1)	Optional
E26: Sample Site	(1 to 1)	Optional
E29: Method or Procedure	(1 to n)	Optional
E53: Sampling Location	(1 to 1)	Optional
E39: Organisation or Person	(1 to n)	Optional
The date, method, location, and person fields are all flagged as optional in the Word table because they may be inherited from the parent sampling activity -- they only need recording here if different. That is a reasonable design intent, but it means the multiplicities in the TSV should be (0 to 1) or (0 to n) respectively. Do you want to correct all of these in this pass? And similarly for E42 -- (0 to 1)?

E26: Sample Site being Optional is a separate question -- is the sample site genuinely not always known or recorded at sample taking level?

How would you like to handle these before I produce the directives?


//flowchart LR S2: Sample Taking tooltip The event in which a material sample was physically removed from the painting. event-fs32 S2: Sample Taking has note Document Note: Sample Taking Model Overview Document Note: Sample Taking Model Overview tooltip This model defines the Sample Taking event (S2

pasted

1: I have changed to "Sample Taking PID" to make it easier, but it will probably need to be 1 to 1. 2: This one does not want to be confused with the previous one so best leave the filed name as in the TSV (though I may come back to this). 3: Probably optional due to inheritance, as noted, so have changed. 4:  Have changed the STV label to "Sample taking comment" 5&6: ok. 7: I think we want to stick with heritage sample here but may revisit. 8: We will need a site, but the accuracy of it may well be variable. 9: Again and inheritance thing, have changed 1 to 0. 10: Ok, 11: have changed label to "Sample taken by" and made it optional, again an inheritance thing. 12: ok 13: ok. BY file is currently as attached did I miss anything

Show more
23 Mar
There is one small issue to flag before writing the directives. The //links directive for E39 still references the old node label:

//links E39: Organisation or Person --> person, organisation [confirmed]
This should be updated to match the renamed node:

//links E39: Sample taken by --> person, organisation [confirmed]
Also, E42: Sample taking PID does not yet have a tooltip in the body of the model. Given you added one for the equivalent node in the sampling activity model, it would be consistent to add one here too. Something like:

E42: Sample taking PID	tooltip	An optional public unique identifier (PID) for the sample taking event. Any of the IDs defined could be flagged as a preferred ID within a documentation system.
The Word table also notes that the PID and System ID should not be confused with each other. The E41 tooltip already handles this implicitly, but it may be worth a small addition to the E42 tooltip to clarify that this is the externally minted PID rather than the system-assigned label -- though that may be sufficient from the behaviour tags alone (pid vs system-id).

Everything else looks consistent. Shall I proceed with those two fixes and produce the full updated file with //field directives appended?

I have made those changes can you please draft the //field lines

23 Mar
Based on the current file, here are the proposed //field lines:

//field E42: Sample taking PID | 1 | Persistent Identifier (PID); PID | behaviour:pid
//field E41: Unique System Label or ID | 2 | Database or System ID; Sample Taking System ID | behaviour:system-id
//field E52: Sampling Date | 3 | Sample Taking Date; Date | behaviour:free-text
//field E73: Sample taking comment | 4 | Description | behaviour:free-text
//field E73: Reason for Sampling | 5 |  | behaviour:free-text
//field E31: Report or Document | 6 | Related Document; Reports; Publications; Summaries | behaviour:select
//field E22/S13: Heritage Sample | 7 | Cross-reference to Sample; Removed; Sample; Created | behaviour:select
//field E26: Sample Site | 8 | Cross-reference to Sample Site | behaviour:select
//field E29: Method or Procedure | 9 | Sampling Method; Method; Procedure | behaviour:select
//field E53: Sampling Location | 10 | Location of Sample Taking Event | behaviour:select
//field E39: Sample taken by | 11 | Sampler; Taken by; Sampling carried out by | behaviour:select
//field-via E3: Condition state (Sample Site Status) via S4: Observation | 12 | State of Sampling Site at Time of Sampling; Object Status | The condition or treatment state of the sample site at the time of sampling, for example varnish removed. | behaviour:list
//field E22: Heritage Object | 13 | Cross-reference to Heritage Object; Heritage Object; Link to Heritage Object | behaviour:select
Two things to note:

Item 5 (E73: Reason for Sampling) -- the alternatives column is empty because the Word table gives no alternatives and the node label already reads clearly. If you want "Overall Purpose" carried across from the sampling activity model for consistency, I can add it.

Item 7 (E22/S13: Heritage Sample) -- the human label derived from the node will be "Heritage Sample". The alternatives "Removed; Sample; Created" come from the Word table. "Created" is slightly odd as an alternative label for a cross-reference field -- it may be worth dropping it, or it may reflect a workflow term you want to retain. Worth a quick decision.

Can you help me with the format of this one //field S13: Heritage Sample | 7 | | behaviour:select; | Cross-reference to Sample; Removed; Sample; Created, a reference to the sample that was taken in this sample taking event – Class to be Confirmed as dual S13/E22 construct may be needed for the sample. the description is not appearing in the table

23 Mar
The issue is column order. The //field syntax is:

//field NODE | ORDER | ALTERNATIVES | OPTIONAL NOTE
There is no separate description column for //field -- the description is always taken from the node's tooltip line in the model body. The text you have placed in what you are treating as a description column is actually being read as the optional note, and the behaviour tag has been split awkwardly with a trailing | and semicolon.

For //field the solution is to put that descriptive text into the tooltip line on E22/S13: Heritage Sample in the model body. However, E22/S13: Heritage Sample is a subgraph name in the Linked Entities block, not a regular node, so it does not currently have a body tooltip.

You have two options:

Option A -- Add a tooltip on the E22/S13: Heritage Sample subgraph name in the model body (after the Linked Entities block closes), which will serve as the field description:

E22/S13: Heritage Sample	tooltip	A reference to the sample that was taken in this sample taking event. Class to be confirmed as dual S13/E22 construct may be needed.
Then the //field line becomes:

//field E22/S13: Heritage Sample | 7 | Removed; Sample; Created | behaviour:select
Option B -- Convert it to a //field-via which does accept an explicit description column. But there is no meaningful intermediate node here, so this would be a misuse of that syntax.

Option A is the right approach. Does the subgraph tooltip pattern work in your implementation, or would you like to check that first?


//flowchart LR E26: Sample Site tooltip The specific point or area on the painting where the sample was taken. Can also be considered as a E53 Place. place-fs32| E26: Sample Site has note Document Note: Sample Site Model Overview Document Note: Sample Site Model Overview tooltip This model defines t

pasted

The last one for me to do at this stage is the sample site: here is the current model and here is the word table Required?Human understandable LabelAlternative Labels (Types)CRM CodeLabel descriptionOptionalSample Site PIDPersistent Identifier (PID)E42A unique identifier for the sample site✓Sample Site System iDDatabase or System iD/LabelE42Required within some documentation or database systems, such as ResearchSpace. Any of the IDs defined could be flagged as a preferred ID within a documentation system.✓Sample Site Name/NumberSite Label, Site Name, Site CodeE41The name, number or code given to identify the sample site for humans. An agreed protocol for the structure of this name is still required.OptionalSample Site DescriptionDescription Text, DescriptionE73Text describing the point from where the sample has been taken e.g. shadow of red drapery of the saint, left edge.OptionalReason for Sample Site SelectionSite selection descriptionE73A description of the reason why a sample has been taken from this specific site OptionalSample site commentAny additional text describing any observations recorded about the specific sample site (e.g. area of overpaint, degraded area etc) that do not fit in the general description. Any uncertainty over the exact sample site location can also be described here.OptionalCross reference to Area of interestObject PartE26This optional field is a link to a wider area/place/feature on an object or object part within which the sample site lies. This allows, for example, 3 samples from the same red drapery to be linked. Any text description of this would sit on the Area of interest entity.  OptionalSample Site Coordinates on objectVia E16The coordinates of the sample site as measured on the actual object.OptionalSample Site Coordinates on imageDigital Image Region, Image Annotation, or actual values ....Ex regionThe coordinates of the sample site as in the annotated image. Analogue annotations (on a print/photograph) are expected to be transferred to a digital image to create these values.OptionalSample Site reference imageDigital Image, Reference Image, Reference Detail, Main Site ImageEX_Dig.Reference to an image that indicates the sample site (e.g. a scan of an annotated photograph)OptionalOther Sample Site imagesSite ImageEX_Dig.Any other images of the sample site.OptionalRelated DocumentReports, Publications, Summaries, etcE31Primarily related to reports and publications, however there is a whole range of documents that can be created to describe the sample site.✓Cross-reference to Heritage ObjectHeritage Object, Link to Heritage ObjectE22The object from which a sample was takenOptionalCross-reference to Heritage Object PartHeritage Object Part, Link to Heritage Object PartE22Optional connection to a defined sub part of a heritage object if a relevant one has been defined. E.g. back/front/extension etc.✓Cross reference to Physical SampleSampleE22The link to the physical sample.✓Cross reference to Sample TakingSample creationS2The specific Sample Taking event to which the sample site is related.

Show more
23 Mar
Let me map this carefully before drafting, as this model has more complexity than the previous two -- particularly the coordinate fields and the image fields.

Straightforward mappings:

Sample Site PID → E42: Persistent Identifier (PID)#-1 -- P48, (1 to 1). Word table Optional, so should be (0 to 1). Flag.
Sample Site System ID → E41: Unique System Label or ID#-1 -- P1, (1 to 1). Required. behaviour:system-id.
Sample Site Name/Number → E41: Sample Site Name/Number -- P1, (1 to 1). Required. behaviour:free-text.
Sample Site Description → E73: Physical Description -- P67i, (1 to 1). Required. behaviour:free-text.
Reason for Sample Site Selection → E73: Site Selection Description -- P67i, (0 to 1). Optional. behaviour:free-text.
Sample site comment → E73: Site Selection Comment -- P67i, (0 to 1). Optional. behaviour:free-text.
Cross reference to Area of Interest → E26: Area of Interest -- P89, (0 to n). Optional. behaviour:select.
Sample Site reference image → EX_Digital_Image: Main Site Image -- PX_has_main_representation, (0 to 1). Optional. behaviour:select.
Other Sample Site images → EX_Digital_Image: Site Image -- P138i, (0 to n). Optional. behaviour:select.
Related Document → E31: Report or Document -- P70i, (0 to n). Optional. behaviour:select.
Cross-reference to Heritage Object → E22: Heritage Object -- P56i, (1 to 1). Required. behaviour:select.
Cross-reference to Heritage Object Part → E22: Heritage Object Part -- P46i, (0 to 1). Optional. behaviour:select.
Cross reference to Physical Sample → this is the S13: Sample node via P53i_is_former_or_current_location_of. The node label is S13: Sample -- word table says Required. behaviour:select. Worth noting the node label S13: Sample will render as "Sample" in the field table, which is fine.
Cross reference to Sample Taking → S2: Sample Taking -- O4i_was_sampling_location_of, (1 to 1). Required. behaviour:select.
Three fields needing discussion:

Sample Site Coordinates on object -- the Word table says "Via E16". There is no E16 node currently in this model. This field is not yet modelled, so it cannot have a //field directive. Options are: add a placeholder E16 node and comment it out as planned, or note it as out of scope for this pass.

Sample Site Coordinates on image -- maps to EX_Digital_Image_Region -- P138i, (0 to n). The Word table description is broader ("coordinates on the image, analogue annotations transferred to digital") but the node as modelled covers this. behaviour:select since it is a link to a defined region entity. The human label from the node will be "Digital Image Region" -- the Word table label is "Sample Site Coordinates on image". This is worth discussing: "Digital Image Region" is semantically accurate but "Coordinates on image" is what a user would understand. Should the node be renamed, or handled with alternatives?

//links directive -- I notice EX_Digital_Image_Region has //link (singular, missing the s) rather than //links. That is a typo in the model that should be corrected.

Multiplicity fix needed:

E42: Persistent Identifier (PID)#-1 from (1 to 1) to (0 to 1)
How do you want to handle the two coordinate fields and the EX_Digital_Image_Region label question before I draft the directives?


//flowchart LR E26: Sample Site tooltip The specific point or area on the painting where the sample was taken. Can also be considered as a E53 Place. place-fs32| E26: Sample Site has note Document Note: Sample Site Model Overview Document Note: Sample Site Model Overview tooltip This model defines t

pasted

I have updated the model a bit, specifically the three E73, can you update the mappings based on this

23 Mar
Noted. The three E73 node renames are:

E73: Physical Description → E73: Sample Site Description
E73: Site Selection Description → E73: Reason for Sample Site Selection
E73: Site Selection Comment → unchanged
Also I can see you have updated P53i_is_former_or_current_location_of to point to E22/S13: Heritage Sample rather than S13: Sample -- so item 13 now maps to the E22/S13: Heritage Sample subgraph node, consistent with the other sample domain models.

Updated mappings in full:

#	Word table label	Node	Multiplicity	Required	Behaviour
1	Sample Site PID	E42: Persistent Identifier (PID)#-1	(0 to 1)	Optional	pid
2	Sample Site System ID	E41: Unique System Label or ID#-1	(1 to 1)	✓	system-id
3	Sample Site Name/Number	E41: Sample Site Name/Number	(1 to 1)	✓	free-text
4	Sample Site Description	E73: Sample Site Description	(1 to 1)	✓	free-text
5	Reason for Sample Site Selection	E73: Reason for Sample Site Selection	(0 to 1)	Optional	free-text
6	Sample site comment	E73: Site Selection Comment	(0 to 1)	Optional	free-text
7	Cross reference to Area of Interest	E26: Area of Interest	(0 to n)	Optional	select
8	Sample Site Coordinates on image	EX_Digital_Image_Region	(0 to n)	Optional	select
9	Sample Site reference image	EX_Digital_Image: Main Site Image	(0 to 1)	Optional	select
10	Other Sample Site images	EX_Digital_Image: Site Image	(0 to n)	Optional	select
11	Related Document	E31: Report or Document	(0 to n)	Optional	select
12	Cross-reference to Heritage Object	E22: Heritage Object	(1 to 1)	✓	select
13	Cross-reference to Heritage Object Part	E22: Heritage Object Part	(0 to 1)	Optional	select
14	Cross reference to Physical Sample	E22/S13: Heritage Sample	(1 to n)	✓	select
15	Cross reference to Sample Taking	S2: Sample Taking	(1 to 1)	✓	select
Three things to confirm before I draft the directives:

Item 8 (EX_Digital_Image_Region) -- the human label derived from the node will be "Digital Image Region". The Word table label is "Sample Site Coordinates on image". Should the node be renamed in the model to something like EX_Digital_Image_Region: Sample Site Coordinates to produce a better field label, or do you want to handle it with alternatives in the //field line?

Item 8 also -- the //link typo (missing s) is still present in this version. Worth fixing in the same pass.

Coordinate fields -- "Sample Site Coordinates on object (Via E16)" remains unmodelled. Confirm we are leaving that out of scope for this pass and I will add a comment line as a placeholder reminder.


//Flowchart LR fix //subgraph Documentation E7: Sampling Event P9_consists_of (1 to n) S2: Sample Taking event|event E7: Sampling Event P9i_forms_part_of (0 to n) E7: Project |event E7: Project tooltip High-level grouping associating multiple sampling events within the same research, conservation, c

pasted

1 - 7 seems ok but 8 needs to be unpicked as the model currently does not actually define the coordinates, I will need to come back to 9 -15. I will need to integrate some of the information in the attached model, but not all of it. The region image is basically a crop from the annotation image that covers the sample site, but the exact site is generally a point or area in that cropped image.  so the actual coordinates would be the E94 and related E63 literal

23 Mar
That is a helpful clarification. Let me make sure I understand the structure correctly before you integrate anything.

From the attached workflow model, the coordinate chain is:

E26: Sample Site --> P168 --> E94: Sampling Point --> P190 --> E62: point coordinate (literal)
With EX_Digital_Image_Region as an intermediate representation layer -- a crop from the annotation image that contextualises the point -- rather than the coordinate itself. So the two Word table fields map as:

Sample Site Coordinates on image → the actual captured value is E62: point coordinate reached via E94: Sampling Point, which is itself reached via E26: Sample Site --> P168. This would be a //field-via E62: point coordinate via E94: Sampling Point with an explicit description, and behaviour:auto since the coordinates are described in the workflow model as automatically generated from the sampling point.
Sample Site Coordinates on object (Via E16) → still unmodelled in the sample site model, leave out of scope for now.
EX_Digital_Image_Region → this is the image crop/region context, not the coordinate entry point. From a form perspective it is probably behaviour:select -- a user selects or links a pre-existing region rather than entering coordinates directly.
So the question before integrating is: which parts of the workflow model do you want to bring into the sample site model? The minimum needed to support the coordinate fields would be:

E26: Sample Site  P168  E94: Sampling Point
E94: Sampling Point  P190  E62: point coordinate
With EX_Digital_Image_Region remaining as the representation link it already has. Does that feel right, or do you want to bring in more of the E94 structure (the IIIF annotation URI, the type, the image links)?


//flowchart LR E26: Sample Site tooltip The specific point or area on the painting where the sample was taken. Can also be considered as a E53 Place. place-fs32| E26: Sample Site has note Document Note: Sample Site Model Overview Document Note: Sample Site Model Overview tooltip This model defines t

pasted

Ok, the E94 is supposed to be used in relation to the Earth or other planets etc. So I have gone for a simpler approach, see attached. Now in these models I do not tend to include to many links between linked entities but in this case I think we will need a few more. The Image region in researchspace is an actual iiif annotation and a cropped defined by said annotation. I did not originally want to bring in the actual annotation image as that will be a separate model, but we could include it as a linked entity. So basically to define a sample site, if an annotation image is being used, an annotation can be applied to an annotation image. This will create the image region which would define the site coordinates (annotation image) dimensions. I am not looking to create an overly complex model here just the sample site related issues. what might you recommend for the model, before we go back to the //field details

Show more
10:05
This is a good moment to step back and think about what the model needs to express versus what belongs elsewhere.

What you have now is clean and sufficient for most purposes:

E26: Sample Site carries two E54 dimension nodes -- one for object-space coordinates, one for annotation-image coordinates. That is simple, direct, and does not require bringing in the annotation image or the region machinery. For institutions not using IIIF or ResearchSpace this is perfectly workable.

The question is whether to add the ResearchSpace/IIIF annotation chain.

The chain would be something like:

EX_Digital_Image: Annotation Image  -->  EX_Digital_Image_Region  -->  E26: Sample Site
Where the region (created by the IIIF annotation) both represents the site (P138i) and implicitly defines the annotation-image coordinates. The E54: Sample Site Coordinates (annotation image) on E26 would then be understood as the formalised numerical expression of what the region defines visually.

My recommendation is a light addition rather than a full annotation chain. Specifically:

Add EX_Digital_Image: Annotation Image as a linked entity, and add a single triple in the model body:

EX_Digital_Image_Region  L1i_is_part_of (0 to 1)  EX_Digital_Image: Annotation Image
This expresses that the region is a part of an annotation image without pulling in the full IIIF selector, URI, and point coordinate machinery from the workflow model. The E54 nodes already handle the coordinate values themselves. The annotation image model, when developed, will be the place for the fuller chain.

This gives you three things in the sample site model:

EX_Digital_Image_Region -- the annotation-created crop, linked to the site via existing P138i
EX_Digital_Image: Annotation Image -- the source image the annotation was applied to, linked to the region via L1i_is_part_of
E54: Sample Site Coordinates (annotation image) -- the numerical coordinate values on the site itself
What you would deliberately leave out: the IIIF annotation URI, the selector type, and the point coordinate literal -- all of which belong in the annotation image model.

Does that feel like the right level of detail, or would you prefer to keep the model even simpler and leave the region-to-annotation-image link for the annotation image model entirely?

Would it not need to be EX_Digital_Image_Region  L1i_is_part_of (1 to 1)  EX_Digital_Image: Annotation Image as we can not have a region without the image it was taken from

10:09
Yes, that is correct. A region cannot exist independently of the image it was derived from, so (1 to 1) is the right lower bound -- every EX_Digital_Image_Region must be part of exactly one annotation image. Good catch.

So the addition to the model body would be:

EX_Digital_Image_Region	L1i_is_part_of (1 to 1)	EX_Digital_Image: Annotation Image	|digital2
And EX_Digital_Image: Annotation Image would be added to the Linked Entities block:

EX_Digital_Image: Annotation Image	tooltip	A digital image to which annotations have been applied to define the position of the sample site. The image region (EX_Digital_Image_Region) is derived from this annotation.	digital2-fs24|
//links EX_Digital_Image: Annotation Image --> rs:EX_Digital_Image
One small consequential point: the //link typo on EX_Digital_Image_Region (missing s) should be fixed in the same pass, and the EX_Digital_Image_Region linked entity tooltip could also be updated slightly to reflect the annotation image relationship, for example: "A defined digital region derived from an annotation applied to an annotation image, corresponding to the position of the sample site."

Shall I now produce the full updated model with these additions plus the //field directives, or would you like to review the model structure first before the directives are added?

Where does the "is_part_of" property come from

10:14
Good question. L1i_is_part_of is the inverse of L1_has_part which comes from CRMdig. It is defined there for digital objects and their parts, which fits the region-as-part-of-image relationship reasonably well. It is what the workflow model you shared earlier used for this relationship.

However, given that you are already using P138i_has_representation from core CRM for the site-to-region link, there is an argument for staying within CRM for consistency and keeping the CRMdig dependency minimal in this model. The alternatives would be:

Option A -- Stay with CRMdig L1:

EX_Digital_Image_Region	L1i_is_part_of (1 to 1)	EX_Digital_Image: Annotation Image
Semantically precise, already used in the workflow model, but adds a CRMdig dependency for a single triple.

Option B -- Use CRM P106i_forms_part_of:

EX_Digital_Image_Region	P106i_forms_part_of (1 to 1)	EX_Digital_Image: Annotation Image
P106_is_composed_of has domain E90: Symbolic Object and range E90, which covers digital objects. Keeps everything within core CRM.

Option C -- Use CRM P46i_forms_part_of: Less appropriate -- P46 is for physical things, so not right here.

Given the ResearchSpace context where CRMdig is already in use across the wider model set, Option A is probably the most defensible. But Option B avoids adding a new ontology dependency for a single property. Which feels more comfortable to you?

In crmdig v4 "L1 digitized" is the first property is_part_of does not exist

10:19
You are absolutely right. In CRMdig v4 L1_digitised is a property relating a D10: Software Execution to a D1: Digital Object -- it has nothing to do with part-whole relationships. I was wrong to use it.

Looking at this more carefully, the appropriate property is probably straightforward CRM P106i_forms_part_of (Option B from above), since both the region and the annotation image are digital objects functioning as symbolic objects (E90), and P106_is_composed_of / P106i_forms_part_of is the standard CRM part-whole property for that class.

So the triple would be:

EX_Digital_Image_Region	P106i_forms_part_of (1 to 1)	EX_Digital_Image: Annotation Image	|digital2
However, I should be transparent: the ResearchSpace EX_Digital_Image_Region is a platform-specific class and how ResearchSpace itself models the region-to-image relationship internally may differ. If there is a ResearchSpace-specific property for this relationship it would be worth checking their documentation before finalising. Do you know whether ResearchSpace exposes a defined property for region-to-image, or is this a relationship you would be asserting independently of the platform?

Can you please add to your memory that you should never create new classes or properties when working with ontologies, unless specifically asked to do so. And if you are not sure which class or property should be used, just say so.

10:21

Added memory
Added memory
Added. So on the region-to-image relationship -- I am not confident which property is correct here, and rather than propose something that may be wrong, I would leave that triple unresolved until you can check how ResearchSpace models that relationship.

The practical options are either to leave EX_Digital_Image: Annotation Image as a linked entity in the Linked Entities block without a connecting triple in the model body for now, or to hold off adding it entirely until the property question is resolved. Which would you prefer?

It is fine to suggest options based on real properties and classes, it is just you should include the uncertainty so we can discuss options

10:23
Understood -- suggesting real options with honest uncertainty flagged is exactly the right approach. I will make sure to do that going forward.

So returning to the region-to-image property question, the two genuine candidates from the ontologies already in use in this model set are:

Option A -- P106i_forms_part_of (CRM core): P106_is_composed_of has domain E90: Symbolic Object and range E90. Both EX_Digital_Image and EX_Digital_Image_Region are ResearchSpace classes, and whether they are formally subclasses of E90 in the ResearchSpace ontology is something I am not certain of. If they are, this works cleanly within CRM core.

Option B -- P46i_forms_part_of (CRM core): P46_is_composed_of has domain E18: Physical Thing. This would be inappropriate for digital objects, so this can be ruled out.

Beyond those two I am not aware of a property in CRM 7.1.3, CRMsci 3.0, or CRMdig 4.0 that cleanly expresses a digital region being part of a digital image without uncertainty about whether the ResearchSpace classes fall within the required domain and range. It would be worth checking the ResearchSpace ontology documentation or their own example data to see how they express this relationship internally before committing to a triple. Shall we leave the annotation image as a linked entity for now and park the connecting triple pending that check?


//flowchart LR E26: Sample Site tooltip The specific point or area on the painting where the sample was taken. Can also be considered as a E53 Place. place-fs32| E26: Sample Site has note Document Note: Sample Site Model Overview Document Note: Sample Site Model Overview tooltip This model defines t

pasted

Option A seems better for now. So I now have the attached. So any further connection such as between the E54 and the Region would be covered in an annotation image model.

10:27
Good. The model looks well-structured and the decision to defer the E54-to-region connection to the annotation image model is sensible -- that is where the fuller IIIF/annotation chain belongs.

Two small things to flag before moving to the //field directives:

1. The //link typo on EX_Digital_Image_Region is still present (missing s). This should be //links EX_Digital_Image_Region --> rs:EX_Digital_Image_Region.

2. The //links for EX_Digital_Image: Annotation Image points to annotation_image as a repo model target. Does an annotation_image folder exist in the repository yet, or should this be rs:EX_Digital_Image to match the other image nodes for now?

Once those are confirmed I can draft the full //field directives. As a reminder, the coordinate fields will map as:

Sample Site Coordinates (object) → //field-via E54: Sample Site Coordinates (object) via E54: Sample Site Coordinates (object) -- actually this is a direct //field since E54 is directly connected to E26 via P43. behaviour:free-text seems right but given the note in the tooltip about IIIF solutions, behaviour:auto might be more appropriate for the annotation image coordinates at least. Worth a quick decision on behaviour tags for both E54 nodes.
Sample Site Coordinates (annotation image) → same pattern, direct //field.
What behaviour tags feel right for those two?

The "annotation model does not exist yet so this will be flagged as an issue in the report, but I would like to move on to that one next so it seemed good to put it in

10:30
That makes sense -- having the //links declaration in place now means the consistency report will flag it as a missing target, which is exactly the right prompt to develop that model next. No change needed there.

On the two E54 behaviour tags -- given that:

Object-space coordinates would typically be manually measured and entered, behaviour:free-text seems right for E54: Sample Site Coordinates (object)
Annotation image coordinates are expected to be IIIF/annotation-derived and auto-generated from the region, so behaviour:auto seems right for E54: Sample Site Coordinates (annotation image)
Does that match your thinking? And to confirm -- for the //field directives, all the nodes I need to cover are:

E42: Sample Site PID -- behaviour:pid
E41: Unique System Label or ID#-1 -- behaviour:system-id
E41: Sample Site Name/Number -- behaviour:free-text
E73: Sample Site Description -- behaviour:free-text
E73: Reason for Sample Site Selection -- behaviour:free-text
E73: Site Selection Comment -- behaviour:free-text
E26: Area of Interest -- behaviour:select
EX_Digital_Image_Region -- behaviour:select
EX_Digital_Image: Sample Site reference image -- behaviour:select
EX_Digital_Image: Other Site Image -- behaviour:select
E54: Sample Site Coordinates (object) -- behaviour:free-text
E54: Sample Site Coordinates (annotation image) -- behaviour:auto
E31: Report or Document -- behaviour:select
E22: Heritage Object -- behaviour:select
E22: Heritage Object Part -- behaviour:select
E22/S13: Heritage Sample -- behaviour:select
S2: Sample Taking -- behaviour:select
Confirm those behaviour tags and I will draft the directives.

The old word table for this one is Required?
Human understandable Label
Alternative Labels - (Types)
CRM Code
Label description
Optional
Sample Site PID
Persistent Identifier (PID)
E42
A unique identifier for the sample site
✓
Sample Site System iD
Database or System iD/Label
E42
Required within some documentation or database systems, such as ResearchSpace. Any of the IDs defined could be flagged as a preferred ID within a documentation system.
✓
Sample Site Name/Number
Site Label, Site Name, Site Code
E41
The name, number or code given to identify the sample site for humans. An agreed protocol for the structure of this name is still required.
Optional
Sample Site Description
Description Text, Description
E73
Text describing the point from where the sample has been taken e.g. shadow of red drapery of the saint, left edge.
Optional
Sample site comment
Any additional text describing any observations recorded about the specific sample site (e.g. area of overpaint, degraded area etc) that do not fit in the general description. Any uncertainty over the exact sample site location can also be described here.
Optional
Sample Site Coordinates on object
Via E16
The coordinates of the sample site as measured on the actual object.
Optional
Sample Site Coordinates on image
Digital Image Region, Image Annotation, or actual values ....
Ex region
The coordinates of the sample site as in the annotated image. Analogue annotations (on a print/photograph) are expected to be transferred to a digital image to create these values.
Optional
Reason for Sample Site Selection
Site selection description
E73
A description of the reason why a sample has been taken from this specific site 
Optional
Cross reference to Area of interest
Object Part
E26
This optional field is a link to a wider area/place/feature on an object or object part within which the sample site lies. This allows, for example, 3 samples from the same red drapery to be linked. Any text description of this would sit on the Area of interest entity.  
Optional
Related Document
Reports, Publications, Summaries, etc
E31
Primarily related to reports and publications, however there is a whole range of documents that can be created to describe the sample site.
✓
Cross-reference to Heritage Object
Heritage Object, Link to Heritage Object
E22
The object from which a sample was taken
Optional
Cross-reference to Heritage Object Part
Heritage Object Part, Link to Heritage Object Part
E22
Optional connection to a defined sub part of a heritage object if a relevant one has been defined. E.g. back/front/extension etc.
✓
Cross reference to Physical Sample
Sample
E22
The link to the physical sample.
✓
Cross reference to Sample Taking
Sample creation
S2
The specific Sample Taking event to which the sample site is related.
Optional
Sample Site reference image
Digital Image, Reference Image, Reference Detail, Main Site Image
EX_Dig.
Reference to an image that indicates the sample site (e.g. a scan of an annotated photograph)
Optional
Other Sample Site images
Site Image
EX_Dig.
Any other images of the sample site. but we have updated a couple of things

Show more
10:33
Yes, comparing the Word table against the current model, the key differences are:

"Sample Site Coordinates on object" -- was "Via E16" in the Word table, now modelled as E54: Sample Site Coordinates (object) via P43
"Sample Site Coordinates on image" -- was EX_Digital_Image_Region in the Word table, now modelled as E54: Sample Site Coordinates (annotation image) via P43, with EX_Digital_Image_Region becoming a separate field for the image region itself
EX_Digital_Image_Region -- is now a field in its own right rather than the coordinate carrier
EX_Digital_Image: Annotation Image -- is a new linked entity not in the original Word table, but it is a linked entity rather than a form field so no //field directive needed
"Sample site comment" -- the Word table has no separate "Reason for Sample Site Selection" row, but the model now has both E73: Reason for Sample Site Selection and E73: Site Selection Comment as distinct nodes
Also noting that the Word table order differs slightly from my earlier list. Aligning to Word table order and incorporating the model updates, here are the proposed directives:

//field E42: Sample Site PID | 1 | Persistent Identifier (PID); PID | behaviour:pid
//field E41: Unique System Label or ID#-1 | 2 | Database or System ID; Sample Site System ID | behaviour:system-id
//field E41: Sample Site Name/Number | 3 | Site Label; Site Name; Site Code | behaviour:free-text
//field E73: Sample Site Description | 4 | Description Text; Description | behaviour:free-text
//field E73: Site Selection Comment | 5 |  | behaviour:free-text
//field E54: Sample Site Coordinates (object) | 6 |  | behaviour:free-text
//field E54: Sample Site Coordinates (annotation image) | 7 | Digital Image Region; Image Annotation | behaviour:auto
//field E73: Reason for Sample Site Selection | 8 | Site Selection Description | behaviour:free-text
//field E26: Area of Interest | 9 | Object Part | behaviour:select
//field E31: Report or Document | 10 | Related Document; Reports; Publications; Summaries | behaviour:select
//field E22: Heritage Object | 11 | Heritage Object; Link to Heritage Object | behaviour:select
//field E22: Heritage Object Part | 12 | Heritage Object Part; Link to Heritage Object Part | behaviour:select
//field E22/S13: Heritage Sample | 13 | Sample | behaviour:select
//field S2: Sample Taking | 14 | Cross-reference to Sample Taking; Sample Creation | behaviour:select
//field EX_Digital_Image: Sample Site reference image | 15 | Digital Image; Reference Image; Reference Detail; Main Site Image | behaviour:select
//field EX_Digital_Image: Other Site Image | 16 | Site Image | behaviour:select
//field EX_Digital_Image_Region | 17 | Image Annotation; Digital Image Region | behaviour:select
Three things to confirm:

Item 5 (E73: Site Selection Comment) -- the Word table has no alternative labels for this one. I have left the alternatives column empty. Fine to leave as is?

Items 6 and 7 -- the Word table alternatives for the coordinate fields were written when the model used a different approach. I have carried across only the ones that still make sense. "Via E16" has been dropped as it no longer reflects the model.

Item 13 (E22/S13: Heritage Sample) -- the human label will render as "Heritage Sample". The Word table label is "Cross reference to Physical Sample" with alternative "Sample". Should "Cross reference to Physical Sample" be added as an alternative, or does "Heritage Sample" read clearly enough on its own in form context?

Your points seem ok, I have adjusted item 13 slightly now so it appears better in the table //field S13: Heritage Sample | 13 | Sample | behaviour:select; Cross-reference to Sample; Removed; Sample; Created, a reference to the sample that was taken from this sample site – Class to be Confirmed as dual S13/E22 construct may be needed for the sample. - I would like to ask about the python script that generates the table. I think the step of parsing the label and ontology code could be improved. The last three fields //field EX_Digital_Image: Sample Site reference image | 15 | Digital Image; Reference Image; Reference Detail; Main Site Image | behaviour:select
//field EX_Digital_Image: Other Site Image | 16 | Site Image | behaviour:select
//field EX_Digital_Image_Region | 17 | Image Annotation; Digital Image Region | behaviour:select render as (https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | The specific Sample Taking event to which the sample site is related. |
| Optional | EX_Digital_Image: Sample Site reference image | Digital Image; Reference Image; Reference Detail; Main Site Image | EX_Digital_Image: Sample Site reference image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to an image that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | EX_Digital_Image: Other Site Image | Site Image | EX_Digital_Image: Other Site Image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to any additional images that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | EX_Digital_Image_Region | Image Annotation; Digital Image Region | EX_Digital_Image_Region | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A defined digital region on an image corresponding to the physical sample site on the painting. | where as ideally they might appear something like | Optional | Sample Site reference image | Digital Image; Reference Image; Reference Detail; Main Site Image | EX_Digital_Image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to an image that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | Other Site Image | Site Image | EX_Digital_Image | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | Reference to any additional images that indicates the sample site (e.g. a scan of an annotated photograph). |
| Optional | Digital Image Region | Image Annotation; Digital Image Region | EX_Digital_Image_Region | ![behaviour: Select Entity](https://img.shields.io/badge/%2F%2F-Select%20Entity-8250df) | A defined digital region on an image corresponding to the physical sample site on the painting. | what changes might work without risking other things breaking?

Show more
10:51
Good question. The issue is that the label-parsing logic assumes a PREFIX: Label pattern with a colon as the separator, which works cleanly for CRM nodes like E42: Sample Site PID but breaks down for ResearchSpace nodes where the "prefix" is the full class name (EX_Digital_Image) and the instance label follows a colon-space, or where there is no colon at all (EX_Digital_Image_Region).

The desired output suggests two things need to change:

1. Human label extraction

Currently the script strips everything up to and including the first colon-space to get the human label. For EX_Digital_Image: Sample Site reference image this produces EX_Digital_Image: Sample Site reference image unchanged (or possibly the full string) because EX_Digital_Image is not recognised as a prefix to strip.

The fix would be to extend the stripping logic to recognise ResearchSpace class names as prefixes. A clean approach would be to maintain a set of known non-CRM prefixes to strip, alongside the existing CRM code pattern. Something like:

python
RS_CLASS_PREFIXES = {
    'EX_Digital_Image',
    'EX_Digital_Image_Region',
    # extend as needed
}
Then in the label extraction function, after the existing CRM prefix strip fails to match, check whether the node label starts with any of these and strip accordingly.

2. CRM code extraction

Currently the code column shows the full node label for these nodes. The desired output shows just EX_Digital_Image or EX_Digital_Image_Region -- i.e. the class name without the instance qualifier. The same prefix set above could drive this: if the node matches a known RS class prefix, use that prefix as the CRM code column value.

For EX_Digital_Image_Region with no colon at all, the node label and the class name are the same, so no special handling is needed beyond recognising it in the prefix set.

Risk assessment

The main risk is that the prefix stripping is applied too broadly and affects nodes it should not. The safest approach is to make the RS prefix check a fallback that only fires when the existing CRM pattern (E\d+:, S\d+:, O\d+: etc.) does not match. That way all existing CRM nodes are unaffected.

Would you like me to draft the specific changes to the parsing function in update_readmes.py? If you can paste the current version of that function (or the relevant section) I can make the edit precise rather than working from description alone.

Ok, I think adding in the RS_CLASS_PREFIXES = {
    'EX_Digital_Image',
    'EX_Digital_Image_Region',
    # extend as needed
} option sounds good - for the last field, to get a cleaner human readable label something like the following could be used, after the changes you have suggested //field EX_Digital_Image_Region: Image Region | 17 | Image Annotation; Digital Image Region | behaviour:select

10:55
Yes, that works cleanly. Renaming the node in the //field line to EX_Digital_Image_Region: Image Region means:

The RS prefix strip produces "Image Region" as the human label
The CRM code column shows "EX_Digital_Image_Region"
However, this only works if the node label in the //field directive matches the node label used in the model body exactly. EX_Digital_Image_Region appears in several structural triples and in the Linked Entities block -- none of those would be changed by this, so the //field line would reference a label that does not exist as a node in the model, which would likely cause the script to fail to find a tooltip for it.

The cleaner fix is probably to rename the node itself in the model body to EX_Digital_Image_Region: Image Region throughout -- in the Linked Entities tooltip line, the //links directive, and all structural triples. That is a small number of occurrences and would make the node label consistent everywhere.

Alternatively, if you prefer not to rename the node in the model body, the RS prefix stripping approach in the script would handle it automatically without any change to the //field line -- EX_Digital_Image_Region would render as "Digital Image Region" once the prefix set recognises it as a class name with no instance qualifier to strip.

So the decision is really:

Rename the node throughout the model to EX_Digital_Image_Region: Image Region → gives "Image Region" as the label
Leave the node as is and rely on the script change → gives "Digital Image Region" as the label
Which do you prefer?


update_readmes.py
py

Ok, I will leave it for now - what changes need to be made to the update_readmes.py

10:58

Viewed 3 files
Viewed 3 files
Good, I have the key functions. The changes needed are confined to two places: _strip_crm_prefix (lines 593--595) and the CRM code extraction block (lines 736--743). Here are the precise edits:

Change 1 -- Add the RS prefix set and update _strip_crm_prefix to use it as a fallback:


Checking exact text around _strip_crm_prefix for precise replacement
Checking exact text around _strip_crm_prefix for precise replacement
Here are the two changes needed, shown as precise before/after blocks ready to apply as str_replace edits when you have the file in your working environment:

Change 1 -- Replace the _strip_crm_prefix block (lines 583--595):

python
# OLD
# Regex to strip CRM class prefix, e.g. "E42: " or "S13: " or "crm:E42: "
_CRM_PREFIX_RE = re.compile(r"^[A-Za-z0-9]+:\s*")


def _strip_crm_prefix(label: str) -> str:
    """Strip leading CRM class prefix from a node label, e.g. 'E42: Foo' -> 'Foo'."""
    return _CRM_PREFIX_RE.sub("", label, count=1).strip()
python
# NEW
# Regex to strip CRM class prefix, e.g. "E42: " or "S13: " or "crm:E42: "
_CRM_PREFIX_RE = re.compile(r"^[A-Za-z0-9]+:\s*")

# Known ResearchSpace class name prefixes that should be stripped from human labels.
# These do not match the short alphanumeric CRM pattern (e.g. "E42") so require
# explicit listing. Extend this set as new RS classes are introduced in models.
_RS_CLASS_PREFIXES = {
    "EX_Digital_Image",
    "EX_Digital_Image_Region",
}


def _strip_crm_prefix(label: str) -> str:
    """
    Strip leading class prefix from a node label to produce a human-readable label.

    Handles two cases:
      1. Standard CRM/CRMsci/CRMdig prefix pattern, e.g. 'E42: Foo' -> 'Foo',
         'S13: Bar' -> 'Bar', 'crm:E42: Foo' -> 'Foo'.
      2. ResearchSpace class prefixes listed in _RS_CLASS_PREFIXES, e.g.
         'EX_Digital_Image: Main Image' -> 'Main Image'.
         If the node label exactly matches a known RS class with no instance
         qualifier (e.g. 'EX_Digital_Image_Region'), the full label is returned
         as-is since there is nothing further to strip.
    """
    # Try standard CRM pattern first
    stripped = _CRM_PREFIX_RE.sub("", label, count=1).strip()
    if stripped != label:
        return stripped

    # Fallback: check RS class prefixes
    for rs_class in _RS_CLASS_PREFIXES:
        if label == rs_class:
            # No instance qualifier -- return the class name as the label
            # Split on underscore and title-case for readability,
            # e.g. 'EX_Digital_Image_Region' -> 'Digital Image Region'
            parts = rs_class.split("_")
            # Drop leading 'EX' prefix if present
            if parts[0].upper() == "EX":
                parts = parts[1:]
            return " ".join(p.capitalize() for p in parts)
        prefix = rs_class + ": "
        if label.startswith(prefix):
            return label[len(prefix):].strip()

    return label
Change 2 -- Replace the CRM code extraction block (lines 736--743):

python
# OLD
    # Extract CRM code from node label prefix
    m = re.match(r"^([A-Za-z0-9]+):", node_label)
    crm_code = m.group(1) if m else node_label

    if is_via:
        m_via = re.match(r"^([A-Za-z0-9]+):", via_label)
        via_code = m_via.group(1) if m_via else via_label
        crm_code = f"{via_code} > {crm_code}"
python
# NEW
    # Extract CRM code from node label prefix.
    # For RS class nodes (e.g. 'EX_Digital_Image: Main Image'), use the RS class
    # name as the code. For nodes that exactly match a known RS class with no
    # instance qualifier, use the full label as the code.
    def _extract_code(lbl: str) -> str:
        for rs_class in _RS_CLASS_PREFIXES:
            if lbl == rs_class or lbl.startswith(rs_class + ": "):
                return rs_class
        m = re.match(r"^([A-Za-z0-9]+):", lbl)
        return m.group(1) if m else lbl

    crm_code = _extract_code(node_label)

    if is_via:
        via_code = _extract_code(via_label)
        crm_code = f"{via_code} > {crm_code}"
Summary of what these changes do:

EX_Digital_Image: Sample Site reference image → human label "Sample Site reference image", code "EX_Digital_Image"
EX_Digital_Image: Other Site Image → human label "Other Site Image", code "EX_Digital_Image"
EX_Digital_Image_Region → human label "Digital Image Region", code "EX_Digital_Image_Region"
All existing CRM nodes are unaffected since the RS prefix check only fires when the standard CRM regex does not match. The _extract_code inner function is defined inside _parse_field_line to keep it close to its only point of use -- if you prefer it as a module-level function that is equally fine.


HPSWG-Models-project-state-v7.md
md

Do we need to update the project state document and or any other documents as a result of this work

11:04
Let me check the relevant sections of the project state document against what we have done.


Reading the field directives and outstanding items sections
Reading the field directives and outstanding items sections
Yes, several updates are needed. Here is what I would change and where:

1. Key design decisions -- add two new entries

The RS prefix handling in update_readmes.py is a design decision that should be recorded. Add after the existing node label entry (line 387):

ResearchSpace class node labels -- nodes using RS class names as prefixes (e.g. EX_Digital_Image: Sample Site reference image, EX_Digital_Image_Region) are handled by _RS_CLASS_PREFIXES in update_readmes.py. The set must be extended manually when new RS classes are introduced in models. The human label is derived by stripping the RS class prefix; for nodes with no instance qualifier the class name itself is title-cased and de-underscored. The CRM code column uses the RS class name as the code.

Also, the annotation_image model has been declared as a //links target in sample_site before the folder exists. This pattern should be noted:

//links targets for planned models -- it is acceptable to declare a //links target pointing to a planned but not yet created model folder. The consistency report will flag it as a missing target (❓), which serves as a reminder to develop that model. This is the intended workflow for incrementally building out the inter-model graph.

2. Outstanding items -- update the //field directives item

The current text at line 462--465 lists sampling_activity, sample_taking, sample_site, sample as the priority batch. The first three are now done. Update to:

//field directives -- roll out to remaining models The project model (v1.3) and heritage_object model are the reference implementations including behaviour tags and //field-via lines. The aim is to add //field directives with behaviour tags to all formed models. Node labels should be reviewed and improved where needed as part of this work. A separate ordering document defines preferred field display order; ORDER integers in existing models should be updated once that document is finalised.

//field directives have been added to: sampling_activity, sample_taking, sample_site, project, heritage_object.

Next priority: sample, then remaining formed models.

3. Models table -- update versions

The sample_taking entry at line 430 still shows v1.6. It should be updated to v1.7 (or whatever version you saved the updated file as). Similarly sampling_activity and sample_site should be added to the table if they are not already there -- checking the table, neither sampling_activity nor sample_site appear in the sample domain models table, which currently only lists sample, sample_taking, sample_modification, sample_observation, and sample_splitting. They should be added with their current versions.

4. Outstanding items -- add a new item for the annotation_image model

Since you have decided to develop that next, it is worth adding a brief entry:

annotation_image model (planned -- next) Declared as a //links target from sample_site. Will cover the relationship between EX_Digital_Image: Annotation Image, EX_Digital_Image_Region, and the fuller IIIF/annotation chain including the region-to-image property (currently unresolved -- check ResearchSpace ontology for the correct property). The E54-to-region connection deferred from sample_site also belongs here.

5. update_readmes.py script changes section

There is no dedicated section for script changes in the project state, but the _RS_CLASS_PREFIXES addition is significant enough that the key design decisions entry (point 1 above) covers it adequately.

Shall I draft the full updated project state document with all of these changes applied, or would you prefer to make the edits yourself from this summary?

v1.6 is the new version of the sample_taking I had just renumbered the file at the start of the work - yes please create a new version of the project state document

11:11
Let me read the full project state document first so I can produce a complete and accurate updated version.


Viewed 3 files
Viewed 3 files
Now I have everything I need. Let me produce the updated document.


Created a file, read a file
Created a file, read a file
Here is the updated v8 document. A summary of what changed from v7:

Key design decisions -- two new entries added:

_RS_CLASS_PREFIXES handling for ResearchSpace class node labels in update_readmes.py
//links targets for planned models (declaring a missing target is intentional and expected)
Models table -- updated with current versions and notes:

sampling_activity and sample_site added as new rows
sample_taking version corrected to v1.6 with //field directives noted
Notes on sample_site reflect the E54 and annotation image additions
sample_site added to the E22/S13 placeholder list in the dual-layer resolution item
Outstanding items:

//field directives item updated to show what has been completed and that sample is next
New annotation_image model item added, noting the open property question
sample_site added to the dual-layer resolution dependent models list
Everything else is carried forward unchanged from v7.

Hpswg models project state v8
Document · MD 


Want to be notified when Claude responds?



Claude is AI and can make mistakes. Please double-check responses.
Hpswg models project state v8 · MD
Copy

# HPSWG-Models: Project State Document
 
**Repository:** `jpadfield/HPSWG-Models`  
**Last updated:** March 2026 (v8)  
**Purpose:** Paste this document at the start of a new Claude conversation to restore project context without re-explanation.
 
---
 
## What this repository is
 
A GitHub repository storing CIDOC CRM-based semantic data models as TSV files for the Heritage and Paintings Science Working Group (HPSWG) at the National Gallery, London. Models are used with the **Dynamic Modeller** browser tool at `https://research.nationalgallery.org.uk/lab/modelling/` which renders Mermaid flow diagrams from tab-separated triples.
 
---
 
## TSV format
 
Each line is a triple with four tab-separated columns:
 
```
Subject  Predicate  Object  Format
```
 
- **Format column** uses `|` to separate Subject format (left) and Object format (right)
- Lines starting with `//` are directives, comments, or structural markers
- First line of a formed model is always a `//` directive
- `//subgraph TITLE ... //end` creates subgraphs
- `//subgraph-LR TITLE`, `//subgraph-TB TITLE` etc. set flow direction for that subgraph; all five Mermaid orientations are supported as suffixes: `TB`, `TD`, `BT`, `RL`, `LR`. Direction inheritance in nested subgraphs is not always consistent in Mermaid.
- `//Flowchart LR` or `//Flowchart TB` (and other Mermaid orientations) sets the top-level flow direction (LR is default)
- `tooltip` predicate adds hover text (not a structural triple)
- `has note` and `from list` are metadata predicates, not structural
- **Subgraph names act as node IDs** -- a `has note` or structural triple can use a subgraph name as its subject or object, referencing the subgraph as a node in the diagram
- `#-1`, `#-2` suffixes denote multiple instances of the same class in one diagram
- Format classes are only needed on the **first mention** of a node; subsequent references including tooltip lines do not repeat them
- The `_bn` suffix on a format class (e.g. `event_bn`, `object_bn`) renders the node as a rounded stub, used for blank nodes or simple inline values not separately addressable as records
- The `dims` base class and its variants (`dims_bn`, `dims2`) relate to dimensions and measurements
- Lowercase values used with format class `type` indicate controlled list terms rather than new named classes (e.g. `E55: given-name`)
- Format class values are compositional. The base class (e.g. `event`, `actor`, `place`) can be extended with optional suffixes in order:
  - `-fs[size]` sets font size in pixels, e.g. `-fs24` or `-fs32`. Default Mermaid font size is 16px. `-fs24` is used for nodes within `//subgraph Linked Entities` blocks; `-fs32` for the primary entity of each model
  - `-[line]-[gap]` adds a dotted border, where `line` is dash length and `gap` is space length, e.g. `-5-10` for long dashes or `-2-2` for fine dots
  - Both suffixes can be combined, e.g. `event-fs64-2-10`
- Any base class can be applied to nodes or subgraphs; to apply to a subgraph add it to the `//end` line, e.g. `//end sg2` or `//end event-5-10`
 
**Node format classes:**
 
| Class | Class | Class | Class |
|-------|-------|-------|-------|
| `crm` | `thing` | `event` | `event_bn` |
| `object` | `object_bn` | `actor` | `actor_bn` |
| `idea` | `idea_bn` | `document` | `document_bn` |
| `type` | `dims` | `dims_bn` | `place` |
| `place_bn` | `name` | `period` | `period_bn` |
| `url` | `note` | `literal` | `base` |
| `digital2` | `event2` | `object2` | `actor2` |
| `dims2` | `type2` | `name2` | `infoobj` |
| `timespan` | `place2` | `classstyle` | |
 
---
 
## Repository structure
 
```
HPSWG-Models/
  models/
    workflows/           # Semantic CIDOC CRM workflow overviews (canonical reference)
    user_workflows/      # Simplified user-facing overviews (excluded from consistency check)
    <model_name>/        # ~24 domain model folders, each containing:
      <model_name>_vA.B.tsv   # Formed model (versioned)
      <model_name>_notes.txt  # Precursor notes (optional)
      README.md               # Auto-generated
    ng_models_v*.tsv     # NG-wide overview model (feeds top-level Mermaid diagram)
    ng_models_mermaid.mmd    # Auto-fetched Mermaid output
    README.template.md   # Human-authored; AUTO blocks injected by script
    README.md            # Auto-generated
  scripts/
    update_readmes.py    # Main README generator (run by GitHub Action)
    check_consistency.py # Consistency checker (run by GitHub Action)
    rename_model.py      # Reusable model folder rename utility (run manually)
    ontologies.json      # Ontology version config (human-maintained)
    crm_hierarchy.json   # CRM class hierarchy for consistency checking (human-maintained)
  reports/
    consistency_report.md    # Auto-generated by check_consistency.py
    README.template.md       # Human-authored intro
    README.md                # Auto-generated listing of reports
  forms/
    field-tables.md          # Auto-generated aggregated field tables for all models
    README.template.md       # Human-authored intro, behaviour badge key, and purpose
    README.md                # Auto-generated listing
  docs/
    README.md                # Human-authored orientation note
    project-state.md         # This document -- update when decisions change
  README.template.md     # Root human-authored template
  README.md              # Auto-generated
  ONTOLOGIES.md          # Human-authored ontology reference
  CONTRIBUTING.md        # Contributor guidance including //field directive syntax
  .github/workflows/
    update-readmes.yml   # GitHub Actions workflow
  conversion_manifest.csv  # Historical migration record from source xlsx files; no longer actively maintained
```
 
---
 
## Ontologies in use
 
| Ontology | Version | Prefix | Notes |
|----------|---------|--------|-------|
| CIDOC CRM | 7.1.3 | `crm` | Core ontology |
| CRMdig | 4.0 | `crmdig` | Adjusted for CRM 7.1.3 compatibility |
| CRMsci | 3.0 | `crmsci` | Adjusted for CRM 7.1.3 compatibility |
| ResearchSpace | -- | `rs` | Platform-specific classes and properties used within the ResearchSpace deployment at the National Gallery. CRM-aligned alternatives are planned. |
 
ResearchSpace has been added to `ontologies.json` with `"version": null`, namespace `https://www.researchspace.org/resource/system/`, and the `rs` prefix. Use `rs:EX_Digital_Image` in `//links` directives for ResearchSpace image nodes.
 
---
 
## GitHub Actions workflow
 
Single workflow (`update-readmes.yml`) triggers on push to model TSVs, TXT precursors, scripts, templates, and report files (excluding `reports/README.md` to prevent loops). Uses `fetch-depth: 0` for full git history (required for git-derived dates).
 
Steps:
1. Fetch Mermaid diagram from Dynamic Modeller API for latest `ng_models_v*.tsv`
2. Run `scripts/update_readmes.py` -- regenerates all READMEs including `reports/README.md`
3. Run `scripts/check_consistency.py` -- regenerates consistency report
4. `git add -A`, commit, `git pull --rebase`, push
 
`RAW_BASE` environment variable is set in the workflow to the raw GitHub URL base and passed to both Python scripts.
 
---
 
## README system
 
Template/inject pattern. Humans edit `.template.md` files; the script fills `<!-- BEGIN AUTO: BLOCK-NAME --> ... <!-- END AUTO: BLOCK-NAME -->` markers.
 
### Auto blocks in use
 
| File | Block name | Content |
|------|-----------|---------|
| `README.template.md` (root) | `NG-MODEL-VISUAL` | Mermaid diagram |
| `README.template.md` (root) | `MODEL-LIST` | Three-section model index table |
| `models/README.template.md` | `ONTOLOGY-REF` | Ontology reference table |
| `models/README.template.md` | `MODEL-FOLDERS` | Three-section folder index |
| `reports/README.template.md` | `REPORT-LIST` | Report listing table |
| `forms/README.template.md` | `FORMS-LISTING` | Table of models with field tables |
 
### Three-section model index structure
 
Tables are split into three sections in this order:
1. **Semantic workflow overviews** (`workflows/` folder) -- blue badge
2. **User workflow overviews** (`user_workflows/` folder) -- purple badge
3. **Domain models** (all other folders) -- status badges (formed/mixed/precursor/planned)
 
### Folder status classification
 
Determined dynamically by `ModelFolder.category` and `ModelFolder.status`:
- `formed` -- has at least one versioned TSV
- `mixed` -- has both TSV and TXT
- `precursor` -- has TXT only
- `empty` -- neither (placeholder)
 
### Per-model READMEs
 
Auto-generated (no template). Include: status badge, ontology reference, version history table with git-derived created/last-modified dates, precursor file listing (if applicable), field reference table (if `//field` directives are present), contributing guidance.
 
---
 
## Consistency checker
 
**File:** `scripts/check_consistency.py`  
**Output:** `reports/consistency_report.md`
 
### What it checks
 
Only nodes declared in each model's `//subgraph Linked Entities` block and the model's key entity (first subject node). High-multiplicity classes (E55 type terms, EX_Digital_Image, E42 identifiers) are ignored unless explicitly declared as linked entities.
 
**Critical:** tooltip lines inside the Linked Entities block ARE treated as node declarations. The Dynamic Modeller receives linked entities as tooltip-only lines with no structural triple. The checker must extract subjects from these lines when inside the block.
 
### Nested subgraphs within the Linked Entities block
 
The Linked Entities block may contain nested subgraphs (e.g. `//subgraph E22/S13: Heritage Sample`). The checker tracks nesting depth using two counters:
 
- `linked_depth` -- goes to 1 when the Linked Entities block opens, back to 0 when its `//end` is reached
- `nested_depth` -- increments for each further `//subgraph` inside the block, decrements on each `//end`
 
**Nodes declared inside a nested subgraph are treated as internal display nodes and excluded from independent consistency checking.** The subgraph name itself (e.g. `E22/S13: Heritage Sample`) is registered as the linked entity in their place, provided it has a parseable class code. `//links` directives on internal nodes are also suppressed.
 
This means only the subgraph-level `//links` directive is needed for a nested dual-entity block:
 
```
//subgraph E22/S13: Heritage Sample
E22: Physical Sample    tooltip    ...    object_bn-fs24|
S13: Material Sample    tooltip    ...    object_bn-fs24|
//end sg2-10-10
//links E22/S13: Heritage Sample --> sample
```
 
The two inner nodes do not require their own `//links` directives and any added will be silently ignored.
 
### `//links` directive syntax
 
Declared inside or immediately after the `//subgraph Linked Entities` block:
 
```
//links E39: Project Owner --> person, institution
//links E7: Parent Project --> project
//links E31: Related Documents --> crm:E31
//links E94: Sampling Point --> crmsci:E94
//links D1: Digital Object --> crmdig:D1
//links EX_Digital_Image: Main Image --> rs:EX_Digital_Image
```
 
- **Repo model targets:** folder name (no colon) -- checker validates class code against target model's key entity
- **Ontology references:** `prefix:ClassCode` (with colon) -- checker validates class code matches the reference; no repo model needed. Supported prefixes: `crm`, `crmsci`, `crmdig`, `rs`
- **Multiple targets:** comma-separated or `or`-separated
- **Confirmed hierarchy matches:** add `[confirmed]` to suppress "confirm intent" flag when a subclass/superclass relationship is intentional:
 
```
//links E39: Group or Artist --> person, organisation [confirmed]
```
 
### Status icons in the report
 
| Icon | Meaning |
|------|---------|
| ✅ | Consistent -- class codes match exactly |
| ✅ | Consistent (confirmed hierarchy match) |
| 🔵 | Hierarchy match -- related via CRM hierarchy, confirm intent |
| ⚠️ | Class mismatch -- check required |
| ❓ | Missing target -- declared folder not found in repo |
| 📖 | Ontology reference -- follows standard CRM/extension ontology structure |
| 📖 | Ontology reference (confirmed hierarchy match) |
| 📖🔵 | Ontology via hierarchy -- confirm intent |
| 📖⚠️ | Ontology reference class mismatch |
| ⚠ | No `//links` declaration -- suggestions provided |
 
### Report accordion summary
 
Each model accordion header shows a count summary, e.g. `3 confirmed, 1 to review, 1 mismatch, 1 missing target, 2 undeclared`. All four problem categories are now visible in the header:
 
- **confirmed** -- `consistent`, `ontology_ref`, `confirmed_hierarchy`, `confirmed_ontology_hierarchy`
- **to review** -- `hierarchy_match`, `ontology_hierarchy`
- **mismatch** -- `class_mismatch`, `ontology_mismatch`
- **missing target** -- `unknown_target` (declared folder not found in repo)
- **undeclared** -- no `//links` directive present
 
### Report structure
 
- **Header:** syntax and status key in a collapsible accordion
- **Section 1:** Per-model link validation -- collapsible accordion per model, header shows summary
- **Section 2:** Models missing Linked Entities subgraph
 
### `scripts/crm_hierarchy.json`
 
Covers classes currently used across models only. Keys are parent class codes, values are arrays of all known subclass codes (direct and indirect). Extend manually as new classes are introduced. The `_comment` key is ignored by the script.
 
### `scripts/ontologies.json`
 
Config file read at runtime to generate ontology reference tables in READMEs. `"version": null` renders as `_see notes_`. Maintain manually when ontology versions change; update `ONTOLOGIES.md` at the same time. ResearchSpace entry added with `"prefix": "rs"`.
 
---
 
## Field directives and form table generation
 
`//field` and `//field-via` directives are embedded in TSV model files to declare fields for data entry or display. They are used by `update_readmes.py` to generate human-readable field reference tables, written to each per-model README and aggregated in `forms/field-tables.md`. All `//field` and `//field-via` lines should be placed at the bottom of the model file, after all structural triples. The Dynamic Modeller ignores these lines.
 
The internal delimiter within a `//field` line is `|`. The alternatives list uses `;` as separator. Commas must not be used as alternative label separators -- the Dynamic Modeller normalises comma-separated values to tabs during processing. The optional note column may also contain a `behaviour:` tag (see below). The tag is extracted automatically and does not appear in the rendered description.
 
### `//field` syntax
 
```
//field NODE | ORDER | ALTERNATIVES | OPTIONAL NOTE
```
 
- **NODE**: full node label as it appears in the model, e.g. `E42: Persistent Identifier (PID)`
- **ORDER**: integer controlling row order in the generated table
- **ALTERNATIVES**: semicolon-separated alternative labels, e.g. `Project ID; PID`
- **OPTIONAL NOTE**: optional fourth field; appended in brackets to the label description in the table. May also contain a `behaviour:TAG` token (see Behaviour tags below), separated from any plain-text note by `;`
 
The human-readable label is derived by stripping the CRM prefix from the node label. The label description is taken from the node's `tooltip` line (with the `(Alternative labels: ...)` parenthetical stripped). Required status is derived from the multiplicity lower bound in the predicate connecting the node to its parent. Alternative labels that duplicate the human label are silently removed.
 
For ResearchSpace class nodes (e.g. `EX_Digital_Image: Sample Site reference image`), the RS class name is stripped as a prefix in the same way as CRM codes. See the `_RS_CLASS_PREFIXES` design decision below.
 
### `//field-via` syntax
 
```
//field-via TARGET via INTERMEDIATE | ORDER | ALTERNATIVES | DESCRIPTION | OPTIONAL NOTE
```
 
- **TARGET**: the terminal node being captured, e.g. `E39: Creator` -- the human label is derived from this node label by stripping the CRM prefix
- **INTERMEDIATE**: the node in the current model through which the target is reached, e.g. `E12: Production Event`
- **ORDER**: integer controlling row order in the generated table
- **ALTERNATIVES**: semicolon-separated alternative labels
- **DESCRIPTION**: required explicit description, since there is no tooltip to draw from in the current model
- **OPTIONAL NOTE**: optional fifth field; may contain a `behaviour:TAG` token
 
The CRM Code column in the generated table displays the navigation path as `INTERMEDIATE_CODE > TARGET_CODE`, e.g. `E12 > E39`. Required status is derived from the predicate connecting the intermediate node to the primary entity of the model.
 
Example:
```
//field-via E39: Creator via E12: Production Event | 21 | Artist; Creator | The actor who carried out the production. | behaviour:ingested
//field-via E52: Date of Production via E12: Production Event | 22 | Date of Production | The date or timespan during which the object was produced. | behaviour:ingested
//field-via E53: Place of Production via E12: Production Event | 23 | Place of Production | The location where the object was created. | behaviour:ingested
```
 
### Behaviour tags
 
A `behaviour:TAG` token may be included in the optional note column of any `//field` or `//field-via` directive. It describes how a user is expected to interact with the field and is rendered as a colour-coded shields.io badge in the Behaviour column of the generated field table. The token is separated from any plain-text note by `;` and is stripped from the description before rendering.
 
```
//field E55: Project Type | 10 | Campaign; Research Project; Survey | behaviour:list
//field E7: Parent Project | 9 | Programme; Umbrella Project | behaviour:select; Could be mapped as E89.
```
 
Badges use the `//` left-panel label (consistent with the directive prefix convention) and a colour-coded right panel. All colours meet WCAG AA contrast ratio against white text. The Behaviour column is only added to the table if at least one field in the model carries a behaviour tag; models without any tags render the original five-column table unchanged.
 
Valid behaviour tags (defined in `_BEHAVIOUR_BADGES` in `scripts/update_readmes.py`):
 
| Tag | Label | Hex | Meaning |
|-----|-------|-----|---------|
| `free-text` | Free Text | `#0969da` | User types a value directly; no controlled format |
| `list` | Controlled List | `#1a7f37` | User selects from a pick list or dropdown |
| `select` | Select Entity | `#8250df` | User searches for and links to an existing entity record |
| `pid` | External ID | `#0e7490` | User looks up or pastes an externally minted persistent identifier |
| `system-id` | System ID | `#57606a` | Value is pre-structured or auto-populated; user may edit if permitted |
| `ingested` | Ingested | `#7d5a00` | Value arrives via a batch or import process; user does not enter directly |
| `inherited` | Inherited | `#bc4c00` | Value is pre-filled from a parent entity; user may edit if needed |
| `auto` | Automatic | `#32383f` | System-assigned read-only value; user cannot edit |
 
An unrecognised tag produces a warning in the GitHub Actions log and the badge is omitted. Extend the vocabulary in `_BEHAVIOUR_BADGES` when new tags are needed.
 
### Required status
 
- `✓` -- lower bound of multiplicity is 1 or more
- `Optional` -- lower bound is 0
- `✓*` -- multiplicity could not be derived; defaulted to required. A warning is printed to the GitHub Actions log and a footnote is added to the table. Verify and correct the model or directive.
 
### Primary node and model description identification
 
The field table section header includes two tooltip texts drawn from the model:
 
1. The tooltip on the Document Note node (the object of the `has note` predicate on the primary node) -- shown as a plain paragraph
2. The tooltip on the primary node itself -- shown in italics below
 
Primary node identification uses a four-step fallback chain:
1. Subject of the line where predicate is `has note` and object starts with `Document Note:` (preferred)
2. Subject of the first line whose format column contains `-fs32`
3. Most frequent subject across all non-directive structural lines
4. If none found: a warning note is inserted and a warning printed to the Actions log
 
### `forms/` folder
 
Generated by `write_forms_outputs()` in `update_readmes.py`:
- `forms/field-tables.md` -- aggregated field tables for all models with `//field` directives, one section per model including links and model description
- `forms/README.md` -- generated from `forms/README.template.md` via `FORMS-LISTING` block
 
Models without `//field` directives are silently omitted from both outputs.
 
### Tooltip conventions for field-bearing nodes
 
- Tooltip text serves dual purpose: it is both the diagram hover text and the field table label description. Write tooltips to serve both contexts.
- The `(Alternative labels: ...)` parenthetical in tooltip text is stripped automatically when used as a table description.
- Where a tooltip is missing from a node declared in a `//field` directive, a warning is printed to the Actions log and the description cell will be empty. All field-bearing nodes must have tooltips.
- Tooltips on nodes in the Linked Entities block and on the same node in the model body are separate lines and may differ. The body tooltip is used for the field table. Align both for diagram hover consistency.
- Illustrative examples within tooltip descriptions (e.g. "e.g. canvas, panel") are acceptable even where they reference a specific material type, provided the opening statement is generic.
 
### Field table ordering
 
The ORDER integer in `//field` and `//field-via` lines controls the row sequence in the generated table. Order values step by 1 in the reference implementation (`project` model) but any integer sequence is valid. A separate ordering document is maintained outside the TSV to define the preferred display order; update ORDER values in the TSV once that document is finalised.
 
---
 
## Key design decisions
 
- **No hardcoded counts or folder names** anywhere in scripts (except `EXCLUDED_FOLDERS`, `WORKFLOW_FOLDERS`, `USER_WORKFLOW_FOLDERS` sets -- extend these rather than hardcoding)
- **Latest version only** checked for consistency -- older versions not expected to be consistent
- **Workflow TSVs are the canonical label reference** -- individual models align to workflow node labels, not vice versa
- **Tooltip lines inside Linked Entities blocks** are node declarations -- critical, easy to miss
- **`[confirmed]`** flag on `//links` promotes hierarchy match to consistent status; use when subclass/superclass relationship is intentional. Has no effect on a `class_mismatch` -- only hierarchy relationships can be confirmed
- **Nested subgraph names in the Linked Entities block** act as the linked entity proxy for their contents; internal nodes are suppressed from checking. Only the subgraph-level `//links` directive is needed.
- **Subgraph names are node IDs** -- structural triples and `has note` predicates can reference a subgraph name as subject or object
- **`P108_has_produced`** is the correct property for a physical event producing an `E22: Physical Man-Made Thing`. `P94_has_created` has range `E28: Conceptual Object` and must not be used for physical sample creation
- **`P31_has_modified`** has range `E18: Physical Thing`, which covers `E22` correctly. `S13` holds via the CRMsci hierarchy (`S13` is a subclass of `E18` via `S10`), but strictly the modification acts on the material. The `E22/S13` subgraph placeholder is used pending dual-layer resolution
- **`E22/S13: Heritage Sample`** is a deliberate placeholder used in the modification, observation, splitting, sample taking, and sample site models to represent the dual-layer sample entity. It will be resolved consistently across all dependent models once the sample model dual-layer structure is finalised
- **`rs:EX_Digital_Image`** is the correct `//links` target for ResearchSpace image nodes. Use `rs:EX_Digital_Image` as an ontology reference rather than pointing to a repo model folder
- **`git add -A`** in workflow -- ensures all generated files are staged
- **`git pull --rebase`** before push -- prevents non-fast-forward errors
- **`fetch-depth: 0`** in checkout -- required for git-derived dates
- **`user_workflows/`** excluded from consistency checking; `workflows/` is canonical reference
- **`old_samples/`, `frame`, `frame_part`, `heritage_object_part_types`** excluded from all discovery via `EXCLUDED_FOLDERS` in both scripts
- **`reports/README.md`** excluded from Action trigger paths to prevent loop
- **Node labels are the human-readable label source** -- the human label in field tables is always derived by stripping the CRM prefix from the node label. Where a node label reads poorly as plain language it should be improved in the model rather than compensated for with alternatives in the `//field` directive
- **ResearchSpace class node labels** -- nodes using RS class names as prefixes (e.g. `EX_Digital_Image: Sample Site reference image`, `EX_Digital_Image_Region`) are handled by `_RS_CLASS_PREFIXES` in `update_readmes.py`. The set must be extended manually when new RS classes are introduced in models. The human label is derived by stripping the RS class prefix; for nodes with no instance qualifier (e.g. `EX_Digital_Image_Region`) the class name is title-cased and de-underscored (e.g. "Digital Image Region"). The CRM code column uses the RS class name as the code. Current entries: `EX_Digital_Image`, `EX_Digital_Image_Region`.
- **Tooltip text serves dual purpose** -- for nodes included via `//field` directives, the tooltip is both the diagram hover text and the field table label description. Write tooltips to serve both contexts. The `(Alternative labels: ...)` parenthetical is stripped automatically when used as a table description
- **`;` is the alternative labels separator in `//field` lines** -- commas must not be used; the Dynamic Modeller normalises comma-separated content to tabs during processing
- **`//field` and `//field-via` lines go at the bottom of the model** -- after all structural triples, for easier editing
- **`forms/` follows the same pattern as `reports/`** -- human-authored `README.template.md`, auto-generated `README.md` and `field-tables.md`
- **Behaviour tags in `//field` lines** use a `behaviour:TAG` token in the optional note column. Valid tags are defined in `_BEHAVIOUR_BADGES` in `update_readmes.py`. The Behaviour column uses shields.io two-part badges (`//` left panel, colour-coded right panel) consistent with the status badges in the model index tables. Colours verified against WCAG AA (white text, minimum 4.5:1 contrast ratio). The column is only rendered when at least one field in the model carries a tag.
- **`E41: Unique System Label or ID`** is present in all models. Its tooltip is deliberately generic: "Required within some documentation or database systems, such as ResearchSpace required label." It always carries `behaviour:system-id`. The `has note` value on E41 nodes across models may still carry `Automatic: Preferred TBC` placeholders pending resolution of automation rules -- these are deferred and do not block field table generation.
- **`//field-via` TARGET node is col 1, INTERMEDIATE node follows `via`** -- the human label is derived from the TARGET (col 1), and the CRM code path in the table reads `INTERMEDIATE > TARGET`. Do not reverse these.
- **`//field-via` requires an explicit DESCRIPTION** -- there is no tooltip in the current model to fall back on for via fields. The description column (col 4) is mandatory.
- **`//links` targets for planned models** -- it is acceptable to declare a `//links` target pointing to a planned but not yet created model folder. The consistency report will flag it as a missing target (`❓`), which serves as a reminder to develop that model. This is the intended workflow for incrementally building out the inter-model graph.
 
---
 
## Sample domain model decisions
 
The sample domain uses a dual-layer structure. This is still under active discussion but the current working model is:
 
- **`E22: Physical Sample`** -- the curated physical artefact (object-management layer): carries persistent identifiers, alternative identifiers, system label, condition records, custody (owner, keeper), storage, format type, keywords, dimensions, and images. Created by `S2: Sample Taking` via `P108_has_produced`.
- **`S13: Material Sample`** -- the removed matter (scientific layer): subject of measurement (`E16`), observation (`S27`), modification (`E11`), and splitting (`S24`) events. Connected to `S2` via `O5_removed`. Carries material type.
- **`E22` carries/contains `S13`** via `P46_is_composed_of` / `P46i_forms_part_of`.
- **Keywords** (`E55: sample keywords`) sit on `E22` as collection management and discovery terms, not on `S13`.
- **Sample format** (`E55: sample format`) sits on `E22` as it describes physical preparation of the curated object.
- **Material type** (`E55: sample material type`) sits on `S13` as it describes the matter itself.
- **Storage** is modelled via a nested `//subgraph Storage Options` within the Linked Entities block, containing `E53: Storage Location` (Option A, direct place link) and `E22: Storage Unit` (Option B, physical container chain). These are mutually exclusive; a `has note` on the Storage Options subgraph explains the choice. `E22: Physical Sample` connects via `P54` to the Storage Options subgraph node.
- **Sub-samples** produced by splitting follow the same dual-layer structure, shown as stub nodes (`object_bn`) within a `//subgraph Sub-Sample Entity` block.
 
### Property selection for sample events
 
| Event | Property to sample | Notes |
|---|---|---|
| `S2: Sample Taking` creates physical sample | `P108_has_produced` --> `E22: Physical Sample` | Not `P94` |
| `S2: Sample Taking` removes material | `O5_removed` --> `S13: Material Sample` | CRMsci property |
| `S24: Sample Splitting` creates new physical sample | `P108_has_produced` --> `E22: Physical Sample#-1` | Not `P94` |
| `S24: Sample Splitting` removes sub-sample material | `O29_removed_sub-sample` --> `S13: Material Sample#-1` | CRMsci property |
| `S24: Sample Splitting` splits source material | `O27_split` --> `S13: Material Sample` | CRMsci property |
| `E22: Physical Sample` diminished by splitting | `O1i_was_diminished_by` --> `S24` | On the E22 side |
 
---
 
## Models in this domain (current versions)
 
| Model | Version | Key entity | Notes |
|---|---|---|---|
| `sample` | v1.8 | `E22: Physical Sample` / `S13: Material Sample` | Dual-layer; under active development |
| `sampling_activity` | v1.1 | `E7: Sampling Activity` | `//field` directives added |
| `sample_taking` | v1.6 | `S2: Sample Taking` | `//field` directives added; renamed from `sample_taking_event` |
| `sample_site` | v1.1 | `E26: Sample Site` | `//field` directives added; `E54` coordinate nodes added; annotation image linked entity added |
| `sample_modification` | v1.4 | `E11: Sample Modification` | `E22/S13` placeholder in use |
| `sample_observation` | v0.1 | `S27: Observation` | New; `E22/S13` placeholder; outputs via `P94` to `EX_Digital_Image`, `D1`, `E73` |
| `sample_splitting` | v0.1 | `S24: Sample Splitting` | New; dual subgraphs for source and sub-sample |
 
**Note on `S27: Observation`:** S27 is the CRMsci superclass of `S21: Measurement` (`E16`). The observation model covers the full range of scientific examination from visual inspection to instrumental analysis. Outputs are: `EX_Digital_Image` for images (ResearchSpace-compatible), `D1: Digital Object` for spectra and datasets (CRMdig), and `E73: Observation Record` for documentary outputs. Interpretation and knowledge creation from outputs are out of scope in this model.
 
---
 
## Outstanding items and planned work
 
### E22/S13 dual-layer resolution (in progress)
The sample model (`sample_v1_8.tsv`) is the primary location for working through the dual-layer structure. Once finalised, all dependent models currently using the `E22/S13: Heritage Sample` placeholder (`sample_taking`, `sample_modification`, `sample_observation`, `sample_splitting`, `sample_site`) should be updated consistently in a single pass.
 
### Phase 2 consistency checking (deferred)
Extend the checker to scan the body of each model file (outside the Linked Entities block) for references to nodes whose class codes match known canonical linked entities. For example, `E22: Painting` in the sample model body should be flagged against canonical `E22: Heritage Object`. Defer until Phase 1 is verified across all models.
 
### Top-level inter-model diagram generation (planned)
Once all models have consistent `//links` declarations, a new script will auto-generate a top-level overview model from the declared links. The nested subgraph proxy node pattern (`E22/S13: Heritage Sample --> sample`) is designed with this in mind -- only the subgraph-level node participates in the inter-model graph.
 
### Model alignment work (in progress)
Individual models need `//links` directives added or verified. The consistency report Section 1 shows undeclared linked entities with suggested targets.
 
### `E41: Unique System Label` `has note` placeholders
Several models have `Automatic: Preferred TBC` as the `has note` value on `E41`. These need resolving to actual automation rules before models are finalised.
 
### ResearchSpace CRM alternatives
Work planned to document CRM-equivalent alternatives for each ResearchSpace-specific term, making models portable beyond the platform.
 
### Vocabulary/SKOS config
Planned: `scripts/vocabularies.json` parallel to `ontologies.json`, recording selected controlled terms with their SKOS URIs and source vocabulary. Not yet started.
 
### `//field` directives -- roll out to remaining models
The `project` model (v1.3) and `heritage_object` model are the reference implementations including behaviour tags and `//field-via` lines. The aim is to add `//field` directives with behaviour tags to all formed models. Node labels should be reviewed and improved where needed as part of this work. A separate ordering document defines preferred field display order; ORDER integers in existing models should be updated once that document is finalised.
 
`//field` directives have been added to: `project`, `heritage_object`, `sampling_activity`, `sample_taking`, `sample_site`.
 
Next priority: `sample`, then remaining formed models.
 
### `annotation_image` model (planned -- next priority)
Declared as a `//links` target from `sample_site` (currently flagged as `❓` missing target in the consistency report). Will cover the relationship between `EX_Digital_Image: Annotation Image`, `EX_Digital_Image_Region`, and the fuller IIIF/annotation chain. The `E54`-to-region connection deferred from `sample_site` also belongs here. An open question remains on the correct property to express `EX_Digital_Image_Region` as part of `EX_Digital_Image: Annotation Image` -- the ResearchSpace ontology should be checked for a defined property before this is finalised.
 
### Tooltip consistency audit
Tooltip descriptions and the label descriptions in the parallel Word document have drifted apart across multiple models. A one-off audit should compare tooltip text against the Word document descriptions and align them, with the TSV tooltip becoming the single source of truth going forward. This is a Claude Code task -- the script should parse the `.docx` table and the TSVs and produce a diff per model.
 
### Dynamic Modeller: ignore `//field` lines in pre-processing
The Dynamic Modeller currently normalises comma-separated content to tabs during pre-processing, which affects `//field` lines. A fix should be added to exclude lines starting with `//field` and `//field-via` from this normalisation step. Currently mitigated by using `;` as the alternatives separator.
 
### GitHub Actions trigger paths: add `forms/`
The `update-readmes.yml` workflow trigger paths should include `forms/README.template.md` so that edits to the forms template trigger a rebuild.
 
### Overview TSV (`ng_models_v*.tsv`) update
Current overview does not include all domain models. Once consistency is confirmed, update to reflect the full inter-model connection set. May be partially automatable from `//links` directives.
 
### Per-model READMEs for `workflows/` and `user_workflows/`
Currently use the standard model template. A distinct branch for workflow folders would be more appropriate.
 
---
 
## Model rename utility
 
`scripts/rename_model.py` is a reusable script for renaming model folders with git history preservation. Run manually from the repository root.
 
```bash
python scripts/rename_model.py --dry-run   # Report only, no changes made
python scripts/rename_model.py             # Execute all changes
```
 
Edit the `RENAMES` list at the top of the script before each use. Clear it after each completed rename batch. The script handles: `git mv` for folders and files, `//links` reference updates in all TSV files including `ng_models_v*.tsv`, and `conversion_manifest.csv` path updates. It flags but does not auto-change node labels, `has note` values, `Document Note:` text, and README template references -- these require manual review.
 
### Renames applied March 2026
 
| Old name | New name | Type |
|---|---|---|
| `production_event` | `production` | Formed |
| `sample_taking_event` | `sample_taking` | Formed |
| `sampling_event` | `sampling_activity` | Formed |
| `sample_imaging_event` | `sample_imaging` | Precursor |
| `sample_preparation_event` | `sample_preparation` | Precursor |
 
---
 
## Precursor model triage decisions (March 2026)
 
The following decisions were made during a triage of all precursor folders. These are recorded here to avoid revisiting them without cause.
 
| Folder | Decision | Rationale |
|---|---|---|
| `sample_component` | **Park -- design decision pending** | Scope covers sub-parts of samples at any depth (particle in a layer, sub-particle in a particle) linked to analysis results. Distinct from `sample_splitting` and the E22/S13 dual-layer. Decision needed on whether a single generic `component` model can serve both samples and heritage objects, or whether two separate models are needed. |
| `heritage_object_component` | **Park -- design decision pending** | Same scope question as `sample_component`. May be consolidatable into a single model. Check precursor notes against `heritage_object_part` v1.1 to confirm whether any content is unmodelled there. |
| `heritage_object_layer` | **Park -- design decision needed** | Overlaps with `heritage_object_part`. Previous attempts to relate sample layers to object layers produced mixed results. Keep separate from `sample_layer`. Lower priority than sample domain work. |
| `heritage_object_image` | **Precursor -- develop after sample domain stable** | Analogous to `sample_image` but distinct metadata. Develop in parallel with `sample_image`. |
| `sample_image` | **Precursor -- develop after sample domain stable** | Different default metadata from heritage object images. Develop in parallel with `heritage_object_image`. |
| `sample_imaging` | **Precursor -- design question open** | Imaging events are a type of observation (`S27`). Resolve whether this should be a specialisation within `sample_observation` or a standalone model before developing further. |
| `sample_layer` | **Precursor -- medium priority** | Commonly discussed; distinct from `heritage_object_layer`. Develop after `sample` dual-layer resolution is complete. |
| `sample_preparation` | **Precursor -- check against modification** | Preparation events may be a typed instance of `sample_modification` rather than a separate model. Check precursor notes for metadata requirements that are structurally distinct from modification before developing. |
| `simple_descriptive_document` | **Precursor -- park, still under discussion** | Covers condition reports, treatment reports, examination reports as primary entities. Not urgent while `E73` handles documentary outputs within event models. |
| `timespan` | **Precursor -- genuine planned model** | Added due to discussions about date ranges and confidence levels. Design not yet settled. Keep as planned; develop once main formed models are stable. |
| `frame` | **Excluded** | Added to `EXCLUDED_FOLDERS`. May be redundant with `heritage_object`; confirm whether any structurally distinct properties exist before deciding to remove or retain. |
| `frame_part` | **Excluded** | Added to `EXCLUDED_FOLDERS`. Same question as `frame` relative to `heritage_object_part`. |
 
---
 
## How to start a new conversation
 
Paste this document, then state the specific task. Always include the current version of any file being edited -- do not rely on Claude inferring file state from this document alone.
 
Examples:
- *"I want to add `//links` directives to a model -- here is the file: [paste]"*
- *"I want to build a new model for the `person` domain -- here is a precursor notes file: [paste]"*
- *"The consistency checker needs to handle X -- here is the current script: [paste]"*
- *"I want to update the GitHub Action to also run a new script"*
- *"Here is the current sample model, I want to continue working on the dual-layer structure: [paste]"*
- *"I want to add `//field` directives to a model -- here is the file: [paste]"*
- *"Here is `update_readmes.py`, I want to extend the field table generation to handle X: [paste]"*
 
You do not need to re-explain the TSV format, the `//links` syntax, the `//field` and `//field-via` syntax, the README system, the three-section table structure, the dual-layer sample pattern, or the `E22/S13` placeholder convention.
 
























