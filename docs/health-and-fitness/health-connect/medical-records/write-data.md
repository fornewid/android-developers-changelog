---
title: https://developer.android.com/health-and-fitness/health-connect/medical-records/write-data
url: https://developer.android.com/health-and-fitness/health-connect/medical-records/write-data
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-beta02](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-beta02).

To write medical data using Medical Records in Health Connect,
follow these steps:

1. Check for feature availability
2. Request write permissions
3. Create a data source ([`MedicalDataSource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource))
4. Write a medical resource ([`MedicalResource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource))

## Feature availability

To determine whether a user's device supports Medical Records on Health Connect, check the availability of `FEATURE_PERSONAL_HEALTH_RECORD` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_PERSONAL_HEALTH_RECORD
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

See [Check for feature availability](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability) to learn more.

## Required permissions

Writing medical data is protected by the following permission:

- `android.permission.health.WRITE_MEDICAL_DATA`

Declare these permissions in the Play Console for your app, as well as in your
app's manifest:  

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_MEDICAL_DATA" />
    </application>

You are responsible for declaring all the appropriate permissions you intend to
use in your devices and apps. You should also check that each permission has
been granted by the user before use.

### Request permissions from the user

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.  

    // Create a set of permissions for required data types
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_WRITE_MEDICAL_DATA

    val PERMISSIONS =
        setOf(
           PERMISSION_WRITE_MEDICAL_DATA
    )

Use [`getGrantedPermissions`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#getGrantedPermissions()) to see if your app already has the
required permissions granted. If not, use
[`createRequestPermissionResultContract`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#createRequestPermissionResultContract(kotlin.String)) to request
those permissions. This displays the Health Connect permissions screen.  

    // Create the permissions launcher
    val requestPermissionActivityContract = PermissionController.createRequestPermissionResultContract()

    val requestPermissions = registerForActivityResult(requestPermissionActivityContract) { granted ->
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions successfully granted
      } else {
        // Lack of required permissions
      }
    }

    suspend fun checkPermissionsAndRun(healthConnectClient: HealthConnectClient) {
      val granted = healthConnectClient.permissionController.getGrantedPermissions()
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions already granted; proceed with inserting or reading data
      } else {
        requestPermissions.launch(PERMISSIONS)
      }
    }

Because users can grant or revoke permissions at any time, your app needs to
periodically check for granted permissions and handle scenarios where
permission is lost.

## Data Sources

A [`MedicalDataSource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource) in Health Connect represents a
user-facing source of data, such as a healthcare organization, a hospital, or an
API.

Medical records stored in Health Connect are organized into a
`MedicalDataSource`. This allows separation of medical records for the same
individual that come from different sources such as APIs or healthcare systems.

Consider the following when creating `MedicalDataSource` records:

- If all records originate from the same source, create one `MedicalDataSource`.
- If records originate from multiple sources, you can create a single `MedicalDataSource` if:
  - The data is reconciled.
  - All records have a unique combination of FHIR resource type and FHIR resource ID. Within a `MedicalDataSource`, there can only be one record of a FHIR resource type with any FHIR resource ID.
- Otherwise, to prevent duplicate IDs, create a `MedicalDataSource` for each data source.

All medical records must be associated with a `MedicalDataSource`, so this must
be created before writing the resources.

Properties of `MedicalDataSource`:

- Display Name (required) - User facing display name for the data source, uniquely identified per writing app.
- FHIR Base URI (required) - For data coming from a FHIR server this should be
  the [FHIR base URL](https://hl7.org/fhir/R4/http.html#root) (for example,
  `https://example.com/fhir/`). Multiple data sources can be associated with
  the same FHIR base URL.

  If the data is generated by an app without an
  FHIR URL, this should be a unique and understandable URI defined by the app
  (for example, `myapp://..`) that points to the source of the data.

  As an example, if a client app supports [deep linking](https://developer.android.com/training/app-links/deep-linking),
  this deeplink could be used as the FHIR Base URI. The maximum length for the
  URI is 2000 characters.
- Package name (populated automatically) - The app writing the data.

- FHIR Version (required) - The FHIR version. Must be a
  [supported version](https://developer.android.com/health-and-fitness/guides/medical-records/data-format).

### Create a MedicalDataSource record

Create a record for each healthcare organization or entity your app is linked
to.  

    // Create a `MedicalDataSource`
    // Note that `displayName` must be unique across `MedicalDataSource`s
    // Each `MedicalDataSource` is assigned an `id` by the system on creation
    val medicalDataSource: MedicalDataSource =
        healthConnectClient.createMedicalDataSource(
            CreateMedicalDataSourceRequest(
                fhirBaseUri = Uri.parse("https://fhir.com/oauth/api/FHIR/R4/"),
                displayName = "Test Data Source",
                fhirVersion = FhirVersion(4, 0, 1)
            )
        )

### Delete a MedicalDataSource record

| **Note:** Your app can only delete records that it has written. An app cannot delete records written by another app.
| **Caution:** Be careful when using this API, as deleting a `MedicalDataSource` also deletes **all** medical resource records associated with that data source.

The previous example returns an `id` by the system on creation. If you need to
delete the `MedicalDataSource` record, reference that same `id`:  

    // Delete the `MedicalDataSource` that has the specified `id`
    healthConnectClient.deleteMedicalDataSourceWithData(medicalDataSource.id)

## Medical resources

A [`MedicalResource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource) in Health Connect represents an FHIR
resource (which contains a medical record), along with metadata.

Properties of `MedicalResource`:

- DataSourceId (required) - Data source as described for a `MedicalDataSource`.
- FHIR Version (required) - The FHIR version. Must be a [supported
  version](https://developer.android.com/health-and-fitness/guides/medical-records/data-format).
- FHIR Resource (required) The JSON-encoded FHIR resource instance.
- Medical Resource type (populated automatically) - The [user-facing
  category](https://developer.android.com/health-and-fitness/guides/medical-records/data-format#medical-resource-types) of the resource, mapping to user-facing permissions.

### Prepare FHIR resources in JSON

Prior to writing medical resources to Health Connect, prepare your FHIR resource
records in JSON. Store each JSON in its own variable for inserting as a medical
resource.

If you need help with the FHIR JSON format, refer to the [example data provided
by the HL7 organization](https://hl7.org/fhir/R4/patient-examples.html).

### Insert or update MedicalResource records

Use `UpsertMedicalResourceRequest` to insert new or update existing
`MedicalResource` records for a `MedicalDataSource`:  

    // Insert `MedicalResource`s into the `MedicalDataSource`
    val medicalResources: List<MedicalResource> =
        healthConnectClient.upsertMedicalResources(
            listOf(
                UpsertMedicalResourceRequest(
                    medicalDataSource.id,
                    medicalDataSource.fhirVersion,
                    medicationJsonToInsert // a valid FHIR json string
                )
            )
        )

    // Update `MedicalResource`s in the `MedicalDataSource`
    val updatedMedicalResources: List<MedicalResource> =
        healthConnectClient.upsertMedicalResources(
            listOf(
                UpsertMedicalResourceRequest(
                    medicalDataSource.id,
                    medicalDataSource.fhirVersion,
                    // a valid FHIR json string
                    // if this resource has the same type and ID as in `medicationJsonToInsert`,
                    // this `upsertMedicalResources()` call will update the previously inserted
                    // `MedicalResource`
                    updatedMedicationJsonToInsert
                )
            )
        )

### Example FHIR resource

In the previous example, the variable `medicationJsonToInsert` represented a
valid FHIR JSON string.

Here is an example of what that JSON might look like, using AllergyIntolerance
as the FHIR resource type, which would map to the Medical Resource Type of
`FHIR_RESOURCE_TYPE_ALLERGY_INTOLERANCE` in Medical Records:  

    {
      "resourceType": "AllergyIntolerance",
      "id": "allergyintolerance-1",
      "criticality": "high",
      "code": {
        "coding": [
          {
            "system": "http://snomed.info/sct",
            "code": "91936005",
            "display": "Penicillin allergy"
          }
        ],
        "text": "Penicillin allergy"
      },
      "recordedDate": "2020-10-09T14:58:00+00:00",
       "asserter": {
        "reference": "Patient/patient-1"
      },
      "lastOccurrence": "2020-10-09",
      "patient": {
        "reference": "Patient/patient-1",
        "display": "B., Alex"
      }
      ...
    }

### Delete a MedicalResource record

| **Note:** Your app can only delete records that it has written. An app cannot delete records written by another app.

`MedicalResource` records may be deleted by ID:  

    // Delete `MedicalResource`s matching the specified `dataSourceId`, `type` and `fhirResourceId`
    healthConnectClient.deleteMedicalResources(
        medicalResources.map { medicalResource: MedicalResource ->
            MedicalResourceId(
                dataSourceId = medicalDataSource.id,
                fhirResourceType = medicalResource.id.fhirResourceType,
                fhirResourceId = medicalResource.id.fhirResourceId
            )
        }
    )

Or they can be deleted by `medicalResourceType`:  

    // Delete all `MedicalResource`s that are in any pair of provided `dataSourceIds` and
    // `medicalResourceTypes`
    healthConnectClient.deleteMedicalResources(
        DeleteMedicalResourcesRequest(
            dataSourceIds = setOf(medicalDataSource.id),
            medicalResourceTypes = setOf(MEDICAL_RESOURCE_TYPE_MEDICATIONS)
        )
    )