---
title: https://developer.android.com/health-and-fitness/health-connect/experiences/vitals
url: https://developer.android.com/health-and-fitness/health-connect/experiences/vitals
source: md.txt
---

<br />

> [!NOTE]
> **Note:** This guide is compatible with Health Connect version [1.1.0](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0).

<br />

If you're looking to build an app that manages user vitals, you can use Health
Connect to do things like:

- Read vitals data like blood pressure, heart rate, and body temperature from other apps
- Write vitals data recorded by your app or connected devices
- Monitor trends and provide health insights based on vitals data

This guide describes how to work with vitals data types, covering permissions,
read and write workflows, and best practices.

## Overview: Building a Comprehensive Vitals Tracker

You can build a comprehensive vitals tracking experience using Health Connect by
following these core steps:

- Requesting the appropriate permissions for vitals data types.
- Writing vitals data using records like [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord), [`HeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord), and other vitals records.
- Reading vitals data for display, analysis, or syncing.
- Using batching for efficient data writing and reading.

This workflow enables interoperability with other Health Connect apps and
verifies user-controlled data access.

## Before you begin

Before implementing vitals features:

- [Integrate Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started#step-1) using the appropriate dependency.
- [Create a `HealthConnectClient`](https://developer.android.com/health-and-fitness/health-connect/get-started#step-2) instance.
- Verify your app implements runtime [permission flows based on Health Permissions](https://developer.android.com/health-and-fitness/health-connect/get-started#declare-permissions).

## Key concepts

Vitals data in Health Connect is represented by various record types, each
corresponding to a specific physiological measurement. Unlike workout sessions,
vitals are often recorded as point-in-time or interval-based data.

### Vitals data types

Vitals data is represented by individual record types. Common types include:

- [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord): Represents a single blood pressure reading, including systolic and diastolic pressure, and body position.
- [`HeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord): Represents a series of heart rate measurements.
- [`RestingHeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord): Represents a single measurement of resting heart rate.
- [`BodyTemperatureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyTemperatureRecord): Represents a single body temperature reading, including measurement location.
- [`BloodGlucoseRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodGlucoseRecord): Represents a single blood glucose reading, including relation to meal and specimen source.
- [`OxygenSaturationRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/OxygenSaturationRecord): Represents a single blood oxygen saturation reading.
- [`RespiratoryRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RespiratoryRateRecord): Represents a single respiratory rate measurement.

For a complete list of data types, see [Health Connect data types](https://developer.android.com/health-and-fitness/health-connect/data-types).

## Development considerations

Vitals data can be sensitive, and apps may need to write data in response to
measurements from sensors or user input, or sync data from a backend.
Permissions are crucial for handling vitals data.

### Permissions

Your app must request the relevant Health Connect permissions before reading or
writing vitals data. Common permissions for vitals include blood pressure,
heart rate, body temperature, blood glucose, oxygen saturation, and
respiratory rate. This includes the following:

- **Blood Pressure:** Read and write permissions for [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord).
- **Heart Rate:** Read and write permissions for [`HeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord).
- **Resting Heart Rate:** Read and write permissions for [`RestingHeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord).
- **Body Temperature:** Read and write permissions for [`BodyTemperatureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyTemperatureRecord).
- **Blood Glucose:** Read and write permissions for [`BloodGlucoseRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodGlucoseRecord).
- **Oxygen Saturation:** Read and write permissions for [`OxygenSaturationRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/OxygenSaturationRecord).
- **Respiratory Rate:** Read and write permissions for [`RespiratoryRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RespiratoryRateRecord).

The following shows an example of how to request permissions for blood pressure,
heart rate, and body temperature:

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.

    // Create a set of permissions for required data types
    val PERMISSIONS =
        setOf(
      HealthPermission.getReadPermission(BloodPressureRecord::class),
      HealthPermission.getWritePermission(BloodPressureRecord::class),
      HealthPermission.getReadPermission(HeartRateRecord::class),
      HealthPermission.getWritePermission(HeartRateRecord::class),
      HealthPermission.getReadPermission(BodyTemperatureRecord::class),
      HealthPermission.getWritePermission(BodyTemperatureRecord::class)
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

To request permissions, call the `checkPermissionsAndRun` function:

    if (!granted.containsAll(PERMISSIONS)) {
        requestPermissions.launch(PERMISSIONS)
        // Check if required permissions are not granted, and return
      }
    // Permissions already granted; proceed with inserting or reading data

If you only need to request permissions for a single data type, such as blood
pressure, include only that data type in your permissions set:

Access to blood pressure is protected by the following permissions:

- `android.permission.health.READ_BLOOD_PRESSURE`
- `android.permission.health.WRITE_BLOOD_PRESSURE`

To add blood pressure capability to your app, start by requesting
permissions for the `BloodPressureRecord` data type.

Here's the permission you need to declare to be able to write
blood pressure:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_BLOOD_PRESSURE" />
    ...
    </application>

To read blood pressure, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_BLOOD_PRESSURE" />
    ...
    </application>

## Write vitals data

This section describes how to write vitals data to Health Connect. Vitals data
is typically written as individual records. If you are writing multiple records
at once, such as syncing from a sensor or backend, use batching.

> [!NOTE]
> **Best Practice:** Use Client IDs When creating records, set a **metadata.clientRecordId** . This is the most effective way to prevent duplicates during sync retries. See [Best practices](https://developer.android.com/health-and-fitness/health-connect/experiences/vitals#best-practices) for a code example.

Example of writing a [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord):

```kotlin
suspend fun writeBloodPressureRecord(healthConnectClient: HealthConnectClient) {
    val record = BloodPressureRecord(
        time = Instant.now(),
        zoneOffset = ZoneOffset.UTC,
        systolic = Pressure.millimetersOfMercury(120.0),
        diastolic = Pressure.millimetersOfMercury(80.0),
        bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
        measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST
    )
    healthConnectClient.insertRecords(listOf(record))
}
```

### Batch writing

If your app needs to write multiple data points, such as syncing data from a
connected device or a backend service, you should batch writes to improve
efficiency and reduce battery consumption. Health Connect can handle up to 1000
records in a single write request.

The following code shows how to batch-write multiple records at once:

```kotlin
suspend fun writeBatchRecords(healthConnectClient: HealthConnectClient) {
    val bloodPressureRecord = BloodPressureRecord(
        time = Instant.now(),
        zoneOffset = ZoneOffset.UTC,
        systolic = Pressure.millimetersOfMercury(120.0),
        diastolic = Pressure.millimetersOfMercury(80.0),
        bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
        measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST
    )
    val heartRateRecord = HeartRateRecord(
        startTime = Instant.now().minusSeconds(60),
        startZoneOffset = ZoneOffset.UTC,
        endTime = Instant.now(),
        endZoneOffset = ZoneOffset.UTC,
        samples = listOf(HeartRateRecord.Sample(time = Instant.now().minusSeconds(30), beatsPerMinute = 80))
    )
    healthConnectClient.insertRecords(listOf(bloodPressureRecord, heartRateRecord))
}
```

## Reading vitals data

Apps can read vitals data to display measurements, analyze trends, or sync data
with an external server. To read vitals, use a `ReadRecordsRequest` with the
specific record type and filter by a time range.

Example of reading [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord) data:

```kotlin
suspend fun readBloodPressureRecords(
    healthConnectClient: HealthConnectClient,
    startTime: Instant,
    endTime: Instant
) {
    val response = healthConnectClient.readRecords(
        ReadRecordsRequest(
            recordType = BloodPressureRecord::class,
            timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
        )
    )

    for (record in response.records) {
        // Process each blood pressure record
        val systolic = record.systolic
        val diastolic = record.diastolic
    }
}
```

If you need to sync vitals data with a backend server, or keep your app's
datastore up-to-date with Health Connect, use ChangeLogs. This lets you retrieve
a list of inserted, updated, or deleted records since a specific point in time,
which is more efficient than manually tracking changes or repeatedly reading all
data. For more information, see [Sync data with Health Connect](https://developer.android.com/health-and-fitness/health-connect/sync-data).

## Best practices

Follow these guidelines to improve data reliability and user experience:

- **Write frequency and batching** : To reduce Input/Output overhead and preserve battery life, group data points into a single `insertRecords` call with batches of up to 1000 records, rather than writing each point individually.
  - **Live Tracking:** For frequent updates from sensors (like continuous glucose monitors or heart rate monitors), write data in batches at intervals of up to 15 minutes to balance real-time updates with battery efficiency.
  - **Background Sync:** Use `WorkManager` for deferred writes, such as syncing data from a companion device or backend service. Aim for a 15-minute interval for batch writes.
- **Avoid writing duplicate data: Use Client IDs** When creating records, set
  a `metadata.clientRecordId`. Health Connect uses this to identify unique
  records. If you attempt to write a record with a `clientRecordId` that
  already exists, Health Connect will ignore the duplicate or update the
  existing record rather than creating a new one. Setting a
  `metadata.clientRecordId` is the most effective way to prevent duplicates
  during sync retries or app reinstalls.

  ```kotlin
  val record = BloodPressureRecord(
      time = Instant.now(),
      zoneOffset = ZoneOffset.UTC,
      systolic = Pressure.millimetersOfMercury(120.0),
      diastolic = Pressure.millimetersOfMercury(80.0),
      bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
      measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST,
      metadata = Metadata(
          // Use a unique ID from your own database
          clientRecordId = "bp_20240101_user123"
      )
  )
  ```
- **Check existing data:** Before syncing data, query Health Connect for
  records within the sync time range to see if data from your app already
  exists, to avoid duplicates or overwriting newer data.

- **Provide clear rationales for permission:** Use the
  `Permission.createIntent` flow to explain why your app needs access to
  health data, such as "To monitor your blood pressure trends and provide
  insights."

- **Align timestamps with measurements:** Verify record timestamps accurately
  reflect when measurements were taken. For interval data like
  [`HeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord), verify `startTime` and `endTime` are correct.

## Testing

To verify data correctness and a high-quality user experience, follow these
testing strategies and refer to the official [Test top use cases](https://developer.android.com/health-and-fitness/health-connect/test/test-cases)
documentation.

### Verification tools

- **[Health Connect Toolbox](https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox):** Use this companion app to manually inspect records, delete test data, and simulate changes to the database. It is the best way to verify that your records are being stored correctly.
- **[Unit testing with `FakeHealthConnectClient`](https://developer.android.com/health-and-fitness/health-connect/test/unit-tests):** Use the testing library to verify how your app handles edge cases, like permission revocation or API exceptions without needing a physical device.

### Quality checklist

**Confirm records in Health Connect:** Open the Health Connect app and navigate to Data and access to verify records appear with expected values. **Read data from other apps:** Test your app's ability to read vitals written by other apps to verify ecosystem compatibility. See [Reading vitals data](https://developer.android.com/health-and-fitness/health-connect/experiences/vitals#reading-vitals-data). **Balance write frequency:** Monitor battery usage if writing frequently. Frequent writes provide high detail but can increase drain.

## Typical architecture

A vitals implementation commonly includes:

| Component | Manages |
|---|---|
| Vitals controller | Sensor/Input reading Batching logic |
| Repository layer (wraps Health Connect operations:) | Insert vitals records Read vitals records |
| UI Layer (Displays): | Live readings Historical data Charts and trends |

## Troubleshooting

| Symptom | Possible cause | Resolution |
|---|---|---|
| Missing data types (For example, Blood Pressure) | Missing write permissions or incorrect time filters. | Check that you have requested and the user has granted the specific data type permission. Verify your `ReadRecordsRequest` uses a `TimeRangeFilter` that covers the time of measurement. See [Permissions](https://developer.android.com/health-and-fitness/health-connect/experiences/vitals#permissions). |
| Records fail to write | Incorrect units or values outside valid range. | Health Connect validates record values. For example, blood pressure values must be in a physiologically plausible range. Check data type documentation for valid ranges and units. |
| Duplicate records appear | Missing `clientRecordId` | Assign a unique `clientRecordId` in the `Metadata` of each record. This allows Health Connect to perform de-duplication if the same data is written twice during a sync retry. See [Best practices](https://developer.android.com/health-and-fitness/health-connect/experiences/vitals#best-practices). |

### Common debugging steps

- **Check Permission state:** Always call `getPermissionStatus()` before attempting a read or write operation. Users can revoke permissions in system settings at any time.