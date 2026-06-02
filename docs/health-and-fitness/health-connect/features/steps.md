---
title: https://developer.android.com/health-and-fitness/health-connect/features/steps
url: https://developer.android.com/health-and-fitness/health-connect/features/steps
source: md.txt
---

Health Connect provides a *steps* data type for recording step counts using
the [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord). Steps are a fundamental measurement in health
and fitness tracking.

<br />

> [!NOTE]
> **Note:** This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

<br />

## Read mobile steps

> [!WARNING]
> **Warning:** Starting with the Health Connect update in June 2026, on-device steps are attributed to a device-specific **Synthetic Package Name (SPN)** instead of the generic `"android"` package name. See [Attribution change for on-device steps](https://developer.android.com/health-and-fitness/health-connect/features/steps#attribution-change) for details.

With Android 14 (API level 34) and SDK Extension version 20 or higher,
Health Connect provides on-device step counting. If any app has been granted
the `READ_STEPS` permission, Health Connect starts capturing steps from the
Android-powered device, and users see steps data automatically added to
Health Connect **Steps** entries.

To check if on-device step counting is available, verify that the device is
running Android 14 (API level 34) and has at least SDK extension version 20:

    val isStepTrackingAvailable =
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE &&
            SdkExtensions.getExtensionVersion(Build.VERSION_CODES.UPSIDE_DOWN_CAKE) >= 20

If your app reads aggregated step counts using
[`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary) and doesn't filter by `DataOrigin`, on-device
steps are automatically included in the total, and no changes are required for
the June 2026 update.

### Attribution change for on-device steps

Starting with the June 2026 update, steps tracked natively by Health
Connect are attributed to a **Synthetic Package Name (SPN)** , such as
`com.android.healthconnect.phone.jd5bdd37e1a8d3667a05d0abebfc4a89e`.

Previously, built-in steps were attributed to the package name `android`.
Historical step data recorded before June 2026 retains the `android` package
name.

SPNs are device-specific and scoped on a per-application basis to protect
user privacy:

- **Stable:** The SPN for the current device is stable for your application.
- **Application-Scoped:** Different applications on the same device see different SPNs for on-device step data.

#### Query for on-device steps

Because SPNs are scoped and device-specific, you **must not** hardcode SPN
values. Instead, use the `getCurrentDeviceDataSource()` API to retrieve the
SPN for the current device.

While on-device step counting requires SDK extension version 20 or higher,
the `getCurrentDeviceDataSource()` API is available on Android 14 (API level
34) with SDK extension version 11 or higher.

The `getCurrentDeviceDataSource()` API is not yet available in the Health
Connect Jetpack library. The following examples use the Android framework API
instead:

    import android.content.Context
    import android.health.connect.HealthConnectManager

    val healthConnectManager = context.getSystemService(HealthConnectManager::class.java)
    val deviceDataSource = healthConnectManager?.getCurrentDeviceDataSource()
    val currentDeviceSpn = deviceDataSource?.deviceDataOrigin?.packageName

If your app needs to read on-device steps, or if it displays step data
broken down by source application or device, you must query for records
where the `DataOrigin` is `android` **or** matches the device's SPN. If
your app shows attribution for step data, use [`metadata.device`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Device)
to identify the source device for individual records. For on-device steps
identified by an SPN in aggregated data, you can use device metadata such as
`model` or `manufacturer` from `DeviceDataSource` for attribution, or use a
generic label like "Your phone" for on-device steps.

The following example shows how to read aggregated on-device step count data
by filtering for both `android` and the current device SPN:

    import android.content.Context
    import android.health.connect.HealthConnectManager
    import android.os.Build
    import android.os.ext.SdkExtensions
    import androidx.health.connect.client.HealthConnectClient
    import androidx.health.connect.client.records.StepsRecord
    import androidx.health.connect.client.records.metadata.DataOrigin
    import androidx.health.connect.client.request.AggregateRequest
    import androidx.health.connect.client.time.TimeRangeFilter
    import java.time.Instant

    suspend fun readDeviceStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        context: Context,
        startTime: Instant,
        endTime: Instant
    ) {
        // 1. Check if SDK Extension 11+ is available for getCurrentDeviceDataSource()
        val isDataSourceApiAvailable = Build.VERSION.SDK_INT >= Build.VERSION_CODES.U &&
                SdkExtensions.getExtensionVersion(Build.VERSION_CODES.U) >= 11

        try {
            val healthConnectManager = context.getSystemService(HealthConnectManager::class.java)

            // 2. Safely fetch the package name only if API is available and data exists
            val currentDeviceSpn = if (isDataSourceApiAvailable) {
                healthConnectManager?.getCurrentDeviceDataSource()?.deviceDataOrigin?.packageName
            } else {
                null
            }

            val dataOriginFilters = mutableSetOf(DataOrigin("android"))

            // 3. Explicit null-safety check using .let
            currentDeviceSpn?.let {
                dataOriginFilters.add(DataOrigin(it))
            }

            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                    dataOriginFilter = dataOriginFilters
                )
            )

            val stepCount = response[StepsRecord.COUNT_TOTAL]

        } catch (e: Exception) {
            // Now this catch block only handles actual runtime exceptions, 
            // rather than Errors from missing methods.
        }
    }

> [!NOTE]
> **Note:** If your app has significant users on Android 13 and lower, we recommend also maintaining or adding an integration with the local [Recording API](https://developer.android.com/health-and-fitness/recording-api).

### On-Device Step Counting

- **Sensor Usage** : Health Connect utilizes the [`TYPE_STEP_COUNTER`](https://developer.android.com/reference/android/hardware/Sensor#TYPE_STEP_COUNTER) sensor from `SensorManager`. This sensor is optimized for low power consumption, making it ideal for continuous background step tracking.
- **Data Granularity**: To conserve battery life, step data is typically batched and written to the Health Connect database no more frequently than once per minute.
- **Attribution** : Steps recorded by this feature before June 2026 are attributed to the `android` package name in the [`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin). After this date, they are attributed to a device-specific SPN. See [Attribution change for on-device steps](https://developer.android.com/health-and-fitness/health-connect/features/steps#attribution-change).
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
    android:name="android.permission.health.WRITE_STE>PS&qu<ot; /
    ...
    /a>pplication

To read steps, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_STE>PS&qu<ot; /
    ...
    /a>pplication

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
check for permissions every time before using them and handle scenarios where
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


```kotlin
val zoneOffset = ZoneOffset.systemDefault().rules.getOffset(startTime)
val stepsRecord = StepsRecord(
    count = 120,
    startTime = startTime,
    endTime = endTime,
    startZoneOffset = zoneOffset,
    endZoneOffset = zoneOffset,
    metadata = Metadata(
        device = Device(type = Device.TYPE_WATCH),
        recordingMethod = Metadata.RECORDING_METHOD_AUTOMATICALLY_RECORDED
    )
)
healthConnectClient.insertRecords(listOf(stepsRecord))
```

<br />

### Read aggregate data

The most common way to read step data is to aggregate the total steps over a
time period. The following example shows how to read the total step count for a
user within a certain time range:


```kotlin
suspend fun readStepsAggregate(startTime: Instant, endTime: Instant): Long {
    val response = healthConnectClient.aggregate(
        AggregateRequest(
            metrics = setOf(StepsRecord.COUNT_TOTAL),
            timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
        )
    )
    return response[StepsRecord.COUNT_TOTAL] ?: 0L
}
```

<br />

### Read raw data

The following example shows how to read raw [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord) data
between a start and end time:


```kotlin
val response = healthConnectClient.readRecords(
    ReadRecordsRequest(
        StepsRecord::class,
        timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
    )
)
response.records.forEach { record ->
    /* Process records */
}
```

<br />