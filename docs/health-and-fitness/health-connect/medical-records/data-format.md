---
title: https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format
url: https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format
source: md.txt
---

<br />

Medical Records data is stored in the [HL7 FHIR](https://www.hl7.org/fhir/overview.html)
format.

Medical Records supports the following Fast Health Interoperable Resources
(FHIR) versions:

- [R4 (v4.0.1)](https://hl7.org/fhir/R4/)
- [R4B (v4.3.0)](https://hl7.org/fhir/R4B/)

## Medical Resource Types

FHIR is made up of a set of modular components called *resources* . The supported
set of FHIR resources and corresponding categories are based roughly on the
[International Patient Summary sections](https://build.fhir.org/ig/HL7/fhir-ips/).

These resources are mapped to data categories in Health Connect, referred to as
Medical Resource Types in the API. Observation resources are mapped based on
content such as Logical Observation Identifiers Names and Codes (LOINC) codes
and FHIR categories.

Observations not belonging to any of these categories are not written to Health
Connect.

<br />

| Health Connect Medical Resource Type | FHIR resource(s) | Health Connect permission declaration |
|---|---|---|
| Allergies | AllergyIntolerance | `android.permission.health.READ_MEDICAL_DATA_ALLERGIES_INTOLERANCES` |
| Conditions | Condition | `android.permission.health.READ_MEDICAL_DATA_CONDITIONS` |
| Laboratory | Observation - `laboratory` FHIR category | `android.permission.health.READ_MEDICAL_DATA_LABORATORY_RESULTS` |
| Medications | Medication, MedicationRequest, MedicationStatement | `android.permission.health.READ_MEDICAL_DATA_MEDICATIONS` |
| Personal details | Patient | `android.permission.health.READ_MEDICAL_DATA_PERSONAL_DETAILS` |
| Practitioner details | Practitioner, PractitionerRole | `android.permission.health.READ_MEDICAL_DATA_PRACTITIONER_DETAILS` |
| Pregnancy | Observation - Pregnancy LOINC codes | `android.permission.health.READ_MEDICAL_DATA_PREGNANCY` |
| Procedures | Procedure | `android.permission.health.READ_MEDICAL_DATA_PROCEDURES` |
| Social history | Observation - Social History LOINC codes - `social-history` FHIR category | `android.permission.health.READ_MEDICAL_DATA_SOCIAL_HISTORY` |
| Vaccines | Immunization | `android.permission.health.READ_MEDICAL_DATA_VACCINES` |
| Visits | Encounter, Location, Organization | `android.permission.health.READ_MEDICAL_DATA_VISITS` |
| Vital signs | Observation - Vital Signs LOINC codes - `vital-signs` FHIR category | `android.permission.health.READ_MEDICAL_DATA_VITAL_SIGNS` |
[*Table 1: Health Connect Medical Resource Types*]

<br />

### Patient resources

Health Connect is intended to store medical records data for a single individual
only at this time. Therefore all FHIR resources written should belong to the
same person.

It is not uncommon for multiple FHIR Patient resources to exist in a system for
a single individual. It is preferred that apps reconcile data and
write a single Patient resource to Health Connect. However, this is not enforced
to accommodate the different organizational structures that may exist.

## Data validation

The Medical Records APIs accept valid FHIR resources from supported versions,
and Health Connect performs some validation to confirm that the FHIR
specification for each supported version is followed.

Validation checks marked as
Coming soon are not yet enforced,
but will be in a future release. We recommend developing against all listed
validation checks to maintain compatibility with future releases.

| Level | Validation Check |
|---|---|
| Valid JSON | Data is compliant with the JSON format. |
| Supported FHIR | FHIR version declared by the writing application is supported. The following FHIR versions are supported by Health Connect: - 4.0.1 - 4.3.0 |
| Supported FHIR | FHIR resource type recorded in the resource instance is supported. The following FHIR resource types are supported by Health Connect: - AllergyIntolerance - Condition - Encounter - Immunization - Location - Medication - MedicationRequest - MedicationStatement - Observation - Organization - Patient - Practitioner - PractitionerRole - Procedure |
| Unique resource ID | Resource has an ID field with a value that meets [regular expression requirements](https://hl7.org/FHIR/datatypes.html#id). |
| Unique resource ID | Resource does not share an ID with another FHIR resource of the same resource type from the same `MedicalDataSource`. |
| Business Rules | Does not include a [contained FHIR resource](https://build.fhir.org/references.html#contained). Contained resources are FHIR resources nested within a "parent" resource. They are used when the parent resource needs to reference another resource, but the system does not have sufficient information to create this as a standalone resource with independent existence. |
| Valid Base FHIR | Top-level fields in the FHIR JSON exist in the FHIR specification for the given resource type. |
| Valid Base FHIR | Top-level fields don't have JSON null values. |
| Valid Base FHIR | Top-level required fields are all present. |
| Valid Base FHIR | Top-level fields defined as [repeating elements in FHIR](https://www.hl7.org/fhir/json.html#repeat) have a JSON `array` data type. |
| Valid Base FHIR | Top-level fields (including elements within JSON `array`s) defined as [Complex types](https://www.hl7.org/fhir/json.html#complex) in FHIR have a JSON `object` data type. |
| Valid Base FHIR | Top-level fields (including elements within JSON `array`s) defined as [Primitive types](https://www.hl7.org/fhir/json.html#primitive) in FHIR have the correct JSON data type. | FHIR data type | JSON data type | |---|---| | integer, unsignedInt, positiveInt, decimal | number | | boolean | boolean | | instant, time, date, dateTime, string, code, markdown, id uri, url, oid, uuid, canonical, integer64, base64Binary | number | Coming soon |
| Valid Base FHIR | Top-level fields defined as [Primitive types](https://build.fhir.org/datatypes.html#primitive) in FHIR meet regular expression requirements. Coming soon |
| Valid Base FHIR | [Extensions to Primitive types](https://www.hl7.org/fhir/json.html#primitive) exist in the FHIR specification and have a JSON `object` data type. |
| Valid Base FHIR | No more than one field is recorded for [Choice fields](https://hl7.org/FHIR/formats.html#choice) (`fieldname[x]`).For example, `effectiveDateTime` and `effectivePeriod` cannot both be present in the same resource instance. |
| Valid Base FHIR | [Complex data types](https://build.fhir.org/datatypes.html#complex) contain fields and data types that match the FHIR specification. Coming soon |
| Valid Base FHIR | [Backbone elements](https://hl7.org/FHIR/types.html#BackboneElement) (and elements within complex types) contain fields and data types that match the FHIR specification. Coming soon |
| Valid Base FHIR | [Extensions element](https://www.hl7.org/fhir/extensibility.html#extension) `value[x]` fields are a valid type and contain contents according to that data type. Extension elements can be included in any resource to represent additional information not part of the base spec. They contain a field `url` which links to the definition of the extension, and a field `value[x]` which contains the extension value. `value[x]` must be from set list of accepted data types. Coming soon |
[*Table 2: Health Connect validation of FHIR data*]

### Transformed FHIR data

Some apps transform FHIR data to meet their own requirements. For example:

- Merging data from different sources (typically FHIR APIs).
- Mapping codes to global terminologies (for example, SNOMED, LOINC, ICD) and standardizing units.
- Consolidating and deduplicating data.
- Fixing formatting or other data quality issues.
- Filtering records based on app-specific business rules.

Either the untransformed and transformed FHIR data could be written to Health
Connect, provided they comply with the FHIR R4 specification. We
recommend that you write transformed data where possible. But keep in mind the
following considerations:

- Apps with narrow use-cases may filter out a significant number of records that other apps in the ecosystem could create user value from. In such situations, it may be beneficial to write the untransformed FHIR that is more complete. However, make sure to inform users that this wider dataset is being shared.
- If merging data that originates from different sources, you can write data to a single `MedicalDataSource` in Health Connect. You must also assign a new ID to each resource to avoid clashes, and update resource references to point to the new IDs.
- Merging data from multiple sources into a single `MedicalDataSource` can obscure the data origin. As it is often useful for data consumers to understand the provenance of data, we recommend populating the `meta.source` field for each resource with the original source of the record (typically a FHIR base URL).