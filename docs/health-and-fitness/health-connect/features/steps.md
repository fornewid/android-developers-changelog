---
title: https://developer.android.com/health-and-fitness/health-connect/features/steps
url: https://developer.android.com/health-and-fitness/health-connect/features/steps
source: md.txt
---

Health Connect provides a *steps* data type for recording step counts using
the [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord). Steps are a fundamental measurement in health
and fitness tracking.

<br />

| **Note:** This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

<br />

## Read mobile steps

With Android 14 (API level 34) and SDK Extension version 20 or higher,
Health Connect provides on-device step counting. If any app has been granted
the `READ_STEPS` permission, Health Connect starts capturing steps from the
Android-powered device, and users see steps data automatically added to
Health Connect **Steps** entries.

To check if on-device step counting is available, you need to verify that the
device is running Android 14 (API level 34) and has at least SDK extension
version 20. You can use the following code:

    val isStepTrackingAvailable =
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE &&
            SdkExtensions.getExtensionVersion(Build.VERSION_CODES.UPSIDE_DOWN_CAKE) >= 20

Mobile steps captured by Health Connect have their
[`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin) set to the package name `android`. If your app
simply reads aggregated step counts using [`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary) and
doesn't filter by `DataOrigin`, on-device steps are automatically included in
the total.

If your app needs to read on-device steps, or if it displays step data
broken down by source application or device, you can query for records
where the `DataOrigin` is `android`. If your app shows attribution for step
data, you should attribute data from the android package to the current device.
You can do this by using a label such as "Your phone", retrieving the device
name with `Settings.Global.getString(resolver, Settings.Global.DEVICE_NAME)`,
or inspecting the [`Device`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Device) field in the record's metadata.

The following example shows how to read aggregated mobile step count data by
filtering for the `android` data origin:

    suspend fun readStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                    dataOriginFilter = setOf(DataOrigin("android"))
                )
            )
            // The result may be null if no data is available in the time range
            val stepCount = response[StepsRecord.COUNT_TOTAL]
        } catch (e: Exception) {
            // Run error handling here
        }
    }

| **Note:** If your app has significant users on Android 13 and lower, we recommend also maintaining or adding an integration with the local [Recording API](https://developer.android.com/health-and-fitness/recording-api).

### On-Device Step Counting

Diving deeper into the on-device step counting feature:

- **Sensor Usage** : Health Connect utilizes the [`TYPE_STEP_COUNTER`](https://developer.android.com/reference/android/hardware/Sensor#TYPE_STEP_COUNTER) sensor from `SensorManager`. This sensor is optimized for low power consumption, making it ideal for continuous background step tracking.
- **Data Granularity**: To conserve battery life, step data is typically batched and written to the Health Connect database no more frequently than once per minute.
- **Attribution** : As mentioned earlier, all steps recorded by this on-device feature are attributed to the `android` package name in the [`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin).
- **Activation** : The on-device step counting mechanism is active only when at least one application on the device has been granted the `READ_STEPS` permission within Health Connect.

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

## Required permissions

Access to steps is protected by the following permissions:

- `android.permission.health.READ_STEPS`
- `android.permission.health.WRITE_STEPS`

To add steps capability to your app, start by requesting
permissions for the `Steps` data type.

Here's the permission you need to declare to be able to write
steps:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_STEPS" />
    ...
    </application>

To read steps, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_STEPS" />
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
      HealthPermission.getReadPermission(StepsRecord::class),
      HealthPermission.getWritePermission(StepsRecord::class)
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

## Information included in a Steps record

Each `StepsRecord` contains the following information:

- **`count`** : The number of steps taken in the time interval, as a `Long`.
- **`startTime`**: The start time of the measurement interval.
- **`endTime`**: The end time of the measurement interval.
- **`startZoneOffset`**: The zone offset for the start time.
- **`endZoneOffset`**: The zone offset for the end time.

## Supported aggregations

<br />

The following aggregate values are available for
`StepsRecord`:

- [`COUNT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord#COUNT_TOTAL())

The following aggregate values are available for
`StepsCadenceRecord`:

- [`RATE_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_AVG())
- [`RATE_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_MAX())
- [`RATE_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_MIN())

<br />

## Example usage

The following sections show how to read and write `StepsRecord` data.

### Write steps data

Your app can write step count data by inserting [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord)
instances. The following example shows how to record 1000 steps taken by a user:

    suspend fun writeStepsData(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant,
        startZoneOffset: ZoneOffset,
        endZoneOffset: ZoneOffset
    ) {
        try {
            val stepsRecord = StepsRecord(
                startTime = startTime,
                startZoneOffset = startZoneOffset,
                endTime = endTime,
                endZoneOffset = endZoneOffset,
                count = 1000
            )
            healthConnectClient.insertRecords(listOf(stepsRecord))
        } catch (e: Exception) {
            // Run error handling
        }
    }

### Read aggregate data

The most common way to read step data is to aggregate the total steps over a
time period. The following example shows how to read the total step count for a
user within a certain time range:

    suspend fun readStepsAggregate(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            // The result may be null if no data is available in the time range
            val stepCount = response[StepsRecord.COUNT_TOTAL]
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Read raw data

The following example shows how to read raw [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord) data
between a start and end time:

    suspend fun readStepsRaw(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.readRecords(
                ReadRecordsRequest(
                    recordType = StepsRecord::class,
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            for (record in response.records) {
                // Process each record
            }
        } catch (e: Exception) {
            // Run error handling here
        }
    }