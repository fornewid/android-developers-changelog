---
title: https://developer.android.com/health-and-fitness/health-connect/features/mindfulness
url: https://developer.android.com/health-and-fitness/health-connect/features/mindfulness
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-rc01](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-rc01).

Health Connect provides a *mindfulness* data type to measure various aspects
of mental health, such as stress and anxiety. Mindfulness is a data type
that is part of overall wellness in Health Connect.

## Check Health Connect availability

Before attempting to use Health Connect, your app should verify that Health Connect is available
on the user's device. Health Connect might not be pre-installed on all devices or could be disabled.
You can check for availability using the `https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#getSdkStatus(android.content.Context,kotlin.String)`
method.

#### How to check for Health Connect availability

```kotlin
fun checkHealthConnectAvailability(context: Context) {
    val providerPackageName = "com.google.android.apps.healthdata" // Or get from HealthConnectClient.DEFAULT_PROVIDER_PACKAGE_NAME
    val availabilityStatus = HealthConnectClient.getSdkStatus(context, providerPackageName)

    if (availabilityStatus == HealthConnectClient.SDK_UNAVAILABLE) {
      // Health Connect is not available. Guide the user to install/enable it.
      // For example, show a dialog.
      return // early return as there is no viable integration
    }
    if (availabilityStatus == HealthConnectClient.SDK_UNAVAILABLE_PROVIDER_UPDATE_REQUIRED) {
      // Health Connect is available but requires an update.
      // Optionally redirect to package installer to find a provider, for example:
      val uriString = "market://details?id=$providerPackageName&url=healthconnect%3A%2F%2Fonboarding"
      context.startActivity(
        Intent(Intent.ACTION_VIEW).apply {
          setPackage("com.android.vending")
          data = Uri.parse(uriString)
          putExtra("overlay", true)
          putExtra("callerId", context.packageName)
        }
      )
      return
    }
    // Health Connect is available, obtain a HealthConnectClient instance
    val healthConnectClient = HealthConnectClient.getOrCreate(context)
    // Issue operations with healthConnectClient
}
```

Depending on the status returned by `getSdkStatus()`, you can guide the user
to install or update Health Connect from the Google Play Store if necessary.

## Feature availability

To determine whether a user's device supports mindfulness session records on Health Connect, check the availability of `FEATURE_MINDFULNESS_SESSION` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_MINDFULNESS_SESSION
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

See [Check for feature availability](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability) to learn more.

## Required permissions

Access to mindfulness is protected by the following permissions:

- `android.permission.health.READ_MINDFULNESS`
- `android.permission.health.WRITE_MINDFULNESS`

To add mindfulness capability to your app, start by requesting
permissions for the `MindfulnessSession` data type.

Here's the permission you need to declare to be able to write
mindfulness:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_MINDFULNESS" />
    ...
    </application>

To read mindfulness, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_MINDFULNESS" />
    ...
    </application>

### Request permissions from the user

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.

    // Create a set of permissions for required data types
    val PERMISSIONS =
        setOf(
      HealthPermission.getReadPermission(MindfulnessSessionRecord::class),
      HealthPermission.getWritePermission(MindfulnessSessionRecord::class)
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

## Information included in a mindfulness session record

Each mindfulness session record captures any type of mindfulness session
a user performs, for example meditation, breathing, and movement. The record
can also include additional notes about the session.

## Supported aggregations

<br />

The following aggregate values are available for
`MindfulnessSessionRecord`:

- [`MINDFULNESS_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MindfulnessSessionRecord#MINDFULNESS_DURATION_TOTAL())

<br />

## Read mindfulness session

The following code snippet demonstrates how to read a mindfulness session:

    if (healthConnectClient.features.getFeatureStatus(FEATURE_MINDFULNESS_SESSION) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {
            healthConnectClient.insertRecords(listOf(MindfulnessSessionRecord(
                startTime = Instant.now().minus(Duration.ofHours(1)),
                startZoneOffset = ZoneOffset.UTC,
                endTime = Instant.now(),
                endZoneOffset = ZoneOffset.UTC,
                mindfulnessSessionType = MindfulnessSessionRecord.MINDFULNESS_SESSION_TYPE_MEDITATION,
                title = "Lake meditation",
                notes = "Meditation by the lake",
                metadata = Metadata.activelyRecorded(
                    clientRecordId = "myid",
                    clientRecordVersion = 0.0,
                    device = Device(type = Device.TYPE_PHONE)
                ),
            )))
        }