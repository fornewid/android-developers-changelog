---
title: https://developer.android.com/health-and-fitness/health-connect/features/skin-temperature
url: https://developer.android.com/health-and-fitness/health-connect/features/skin-temperature
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

Health Connect provides a *skin temperature* data type to measure peripheral
body temperature. This measurement is a particularly useful signal for detecting
sleep quality, reproductive health, and the potential onset of illness.

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

To determine whether a user's device supports skin temperature on Health Connect, check the availability of `FEATURE_SKIN_TEMPERATURE` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_SKIN_TEMPERATURE
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

See [Check for feature availability](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability) to learn more. **Note:** The skin temperature data type isn't meant to measure core body temperature. If your app requires this measurement, use classes such as [`BodyTemperatureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyTemperatureRecord) and [`BasalBodyTemperatureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BasalBodyTemperatureRecord).

## Required permissions

Access to skin temperature is protected by the following permissions:

- `android.permission.health.READ_SKIN_TEMPERATURE`
- `android.permission.health.WRITE_SKIN_TEMPERATURE`

To add skin temperature capability to your app, start by requesting
permissions for the `SkinTemperature` data type.

Here's the permission you need to declare to be able to write
skin temperature:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_SKIN_TEMPERATURE" />
    ...
    </application>

To read skin temperature, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_SKIN_TEMPERATURE" />
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
      HealthPermission.getReadPermission(SkinTemperatureRecord::class),
      HealthPermission.getWritePermission(SkinTemperatureRecord::class)
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

## Information included in a skin temperature record

Skin temperature measurements are organized into *records*. Each record consists
of the following information:

- **Baseline temperature**, in degrees Celsius or degrees Fahrenheit. This is an optional value that is most useful for visualization in your app's UI.
- A **list of deltas** in skin temperature, each showing the change in skin temperature since the last measurement. If the baseline temperature is provided, these deltas should use the same temperature units.
- The **location** on the user's body where the measurement was taken: finger, toe, or wrist.

## Supported aggregations

<br />

The following aggregate values are available for
`SkinTemperatureRecord`:

- [`TEMPERATURE_DELTA_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_AVG())
- [`TEMPERATURE_DELTA_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_MAX())
- [`TEMPERATURE_DELTA_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_MIN())

<br />

## Example usage

The following code snippets show how to read and write skin temperature
measurements.

### Read skin temperature record

The following code snippet demonstrates how to read a skin temperature
measurements using the Jetpack library:

    suspend fun readSkinTemperatures() {
        // Error handling, permission check, and feature availability check
        // aren't included.

        // Record includes measurements during the past hour.
        val recordEndTime = Instant.now()
        val recordStartTime = recordEndTime.minusSeconds(60 * 60)

        val response = healthConnectClient.readRecords(
            ReadRecordsRequest<SkinTemperatureRecord>(
                timeRangeFilter = TimeRangeFilter.between(
                    recordStartTime, recordEndTime
                )
            )
        )

        for (skinTemperatureRecord in response.records) {
            // Process each skin temperature record here.
        }
    }

### Write a skin temperature record

The following code snippet shows how to write skin temperature
measurements using the Jetpack library:


    suspend fun writeSkinTemperatures(): InsertRecordsResponse {
        // Error handling, permission check, and feature availability check
        // aren't included.

        // Record includes measurements during the past hour.
        val recordEndTime: ZonedDateTime = now()
        val recordStartTime: ZonedDateTime = recordEndTime.minusHours(1)

        healthConnectClient.insertRecords(
            // For this example, there's only one skin temperature record.
            listOf(
                SkinTemperatureRecord(
                    baseline = Temperature.celsius(37.0),
                    startTime = recordStartTime.toInstant(),
                    startZoneOffset = recordStartTime.offset,
                    endTime = recordEndTime.toInstant(),
                    endZoneOffset = recordEndTime.offset,
                    deltas = listOf(
                        SkinTemperatureRecord.Delta(
                            recordEndTime.minusMinutes(50).toInstant(), celsius(0.5)
                        ), SkinTemperatureRecord.Delta(
                            recordEndTime.minusMinutes(30).toInstant(), celsius(-0.7)
                        )
                    ),
                    measurementLocation = SkinTemperatureRecord.MEASUREMENT_LOCATION_FINGER,
                    metadata = Metadata.autoRecorded(
                        device = Device(type = Device.TYPE_RING)
                    ),
                )
            )
        )
    }