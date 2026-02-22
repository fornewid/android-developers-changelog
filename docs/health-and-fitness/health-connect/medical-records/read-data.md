---
title: https://developer.android.com/health-and-fitness/health-connect/medical-records/read-data
url: https://developer.android.com/health-and-fitness/health-connect/medical-records/read-data
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-beta02](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-beta02).

To read medical data using Medical Records in Health Connect,
follow these steps:

1. Check for feature availability.
2. Request read permissions.
3. Read medical records ([`MedicalResource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource)).
4. Read data sources ([`MedicalDataSource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource)).

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

Reading medical data is protected by the following permission:

- `android.permission.health.READ_MEDICAL_DATA_ALLERGIES_INTOLERANCES`
- `android.permission.health.READ_MEDICAL_DATA_CONDITIONS`
- `android.permission.health.READ_MEDICAL_DATA_LABORATORY_RESULTS`
- `android.permission.health.READ_MEDICAL_DATA_MEDICATIONS`
- `android.permission.health.READ_MEDICAL_DATA_PERSONAL_DETAILS`
- `android.permission.health.READ_MEDICAL_DATA_PRACTITIONER_DETAILS`
- `android.permission.health.READ_MEDICAL_DATA_PREGNANCY`
- `android.permission.health.READ_MEDICAL_DATA_PROCEDURES`
- `android.permission.health.READ_MEDICAL_DATA_SOCIAL_HISTORY`
- `android.permission.health.READ_MEDICAL_DATA_VACCINES`
- `android.permission.health.READ_MEDICAL_DATA_VISITS`
- `android.permission.health.READ_MEDICAL_DATA_VITAL_SIGNS`

Declare these permissions in the Play Console for your app, as well as in your
app's manifest:  

    <application>
      <uses-permission
       android:name="android.permission.health.READ_MEDICAL_DATA_ALLERGIES_INTOLERANCES" />
      <uses-permission
       android:name="android.permission.health.READ_MEDICAL_DATA_CONDITIONS" />
      ...
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
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_ALLERGIES_INTOLERANCES
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_CONDITIONS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_LABORATORY_RESULTS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_MEDICATIONS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_PERSONAL_DETAILS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_PRACTITIONER_DETAILS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_PREGNANCY
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_PROCEDURES
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_SOCIAL_HISTORY
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_VACCINES
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_VISITS
    import androidx.health.connect.client.permission.HealthPermission.Companion.PERMISSION_READ_MEDICAL_DATA_VITAL_SIGNS

    val PERMISSIONS =
        setOf(
            PERMISSION_READ_MEDICAL_DATA_ALLERGIES_INTOLERANCES
            PERMISSION_READ_MEDICAL_DATA_CONDITIONS
            PERMISSION_READ_MEDICAL_DATA_LABORATORY_RESULTS
            PERMISSION_READ_MEDICAL_DATA_MEDICATIONS
            PERMISSION_READ_MEDICAL_DATA_PERSONAL_DETAILS
            PERMISSION_READ_MEDICAL_DATA_PRACTITIONER_DETAILS
            PERMISSION_READ_MEDICAL_DATA_PREGNANCY
            PERMISSION_READ_MEDICAL_DATA_PROCEDURES
            PERMISSION_READ_MEDICAL_DATA_SOCIAL_HISTORY
            PERMISSION_READ_MEDICAL_DATA_VACCINES
            PERMISSION_READ_MEDICAL_DATA_VISITS
            PERMISSION_READ_MEDICAL_DATA_VITAL_SIGNS
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

## Medical resources

You can read any medical resource ([`MedicalResource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource))
written to Health Connect for the user, including those added by other apps.

### Get MedicalResource records

Filter a get request by specifying the `medicalResourceType`. Make sure to use
paged requests and be mindful of [rate limiting](https://developer.android.com/health-and-fitness/guides/health-connect/plan/rate-limiting).  

    // Read `MedicalResource`s back from the `MedicalDataSource`
    // Read 100 resources / page. See `pageSize` doc for defaults and limits.
    val pageSize = 100
    // Prepare the initial read request.
    // All `MedicalResource`s in the given `MedicalDataSource`s and of given `medicalResourceType`
    // will be retrieved.
    val initialRequest: ReadMedicalResourcesRequest =
        ReadMedicalResourcesInitialRequest(
            MEDICAL_RESOURCE_TYPE_LABORATORY_RESULTS,
            setOf(medicalDataSource.id),
            pageSize = pageSize,
        )
    // Continue reading pages until all `MedicalResource`s are read
    var pageToken: String? = null
    do {
        // Prepare paged request if needed
        val request: ReadMedicalResourcesRequest =
            if (pageToken == null) initialRequest
            else ReadMedicalResourcesPageRequest(pageToken, pageSize = pageSize)
        // Read `MedicalResource`s
        val response: ReadMedicalResourcesResponse =
            healthConnectClient.readMedicalResources(request)
        // Process `MedicalResource`s
        val resources: List<MedicalResource> = response.medicalResources
        // Advance to next page
        pageToken = response.nextPageToken
    } while (pageToken != null)

### Get MedicalResource records by ID

You can also retrieve a `MedicalResource` using an ID:  

    // Retrieve `fhirResourceType` type `MedicalResource`s with the specified `id`s from the
    // provided `MedicalDataSource`
    val retrievedMedicalResources: List<MedicalResource> =
        healthConnectClient.readMedicalResources(
            medicalResources.map { medicalResource: MedicalResource ->
                MedicalResourceId(
                    dataSourceId = medicalDataSource.id,
                    fhirResourceType = medicalResource.id.fhirResourceType,
                    fhirResourceId = medicalResource.id.fhirResourceId
                )
            }
        )

## Data Sources

You can read any data source ([`MedicalDataSource`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource))
written to Health Connect for the user, including those added by other apps.

### Get a MedicalDataSource record by package name

Use `GetMedicalDataSourcesRequest` to request by package name (app):  

    // Retrieve all `MedicalDataSource`s created by any of the specified package names
    // Package names may be found in other `MedicalDataSource`s or from arbitrary input
    val medicalDataSources: List<MedicalDataSource> =
        healthConnectClient.getMedicalDataSources(
            GetMedicalDataSourcesRequest(listOf(medicalDataSource.packageName, anotherPackageName))
        )

### Get a MedicalDataSource record by ID

Or, request by `id` if you know it:  

    // Retrieve all `MedicalDataSource` with `id` matching any of the given ids
    val medicalDataSources: List<MedicalDataSource> =
        healthConnectClient.getMedicalDataSources(listOf(medicalDataSource.id, anotherId))