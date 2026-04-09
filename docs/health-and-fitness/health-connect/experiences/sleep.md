---
title: Develop Sleep Experiences with Health Connect  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-connect/experiences/sleep
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Health Connect Guides](https://developer.android.com/health-and-fitness/health-connect)

# Develop Sleep Experiences with Health Connect Stay organized with collections Save and categorize content based on your preferences.




**Note:** This guide is compatible with Health Connect version [1.1.0](/jetpack/androidx/releases/health-connect#1.1.0).

If you're looking to build a sleep tracking experience in your app, you can use
Health Connect to do things like:

* Write sleep sessions
* Write sleep stage data
* Write sleep data such as heart rate, oxygen saturation, and respiratory rate
* Read sleep data from other apps

This guide describes how to build these sleep features, covering data types,
background execution, permissions, recommended workflows, and best practices.

## Overview: Building a Comprehensive Sleep Tracker

You can build a comprehensive sleep tracking experience using Health Connect by
following these core steps:

* Correctly implementing permissions based on Health Permissions.
* Recording sessions using `SleepSessionRecord`.
* Writing data types like sleep stages, heart rate, and oxygen saturation
  consistently during the session.
* Managing background execution properly to verify continuous data capture
  overnight.
* Reading session data for post-sleep summaries and analysis.

This workflow enables interoperability with other Health Connect apps and
verifies user-controlled data access.

## Before you begin

Before implementing sleep features:

* [Integrate Health Connect](/health-and-fitness/health-connect/get-started#step-1) using the appropriate dependency.
* [Create a `HealthConnectClient`](/health-and-fitness/health-connect/get-started#step-2) instance.
* Verify your app implements runtime [permission flows based on Health
  Permissions](/health-and-fitness/health-connect/get-started#declare-permissions).

## Key concepts

Health Connect represents sleep data using a few core components. A
`SleepSessionRecord` acts as the central record for sleep,
containing details like start or end times and sleep stages. During a
session, various data types such as `HeartRateRecord` or
`OxygenSaturationRecord` can be recorded.

### Sleep sessions

Sleep data is represented by `SleepSessionRecord`. Each record stores:

* `startTime`
* `endTime`
* `stages`: A list of `SleepSessionRecord.Stage` including deep, light, REM,
  and awake sleep.
* Optional session metadata (title, notes)

Apps may write multiple data types associated with a session.

### Data types

Common data types recorded during a sleep session include:

* [`SleepSessionRecord`](/health-and-fitness/health-connect/features/sleep-sessions): Records sleep duration and stages including
  deep, light, REM, and awake sleep.
* [`HeartRateRecord`](/health-and-fitness/health-connect/data-types/vitals#heart-rate): Records heart rate during sleep.
* [`OxygenSaturationRecord`](/health-and-fitness/health-connect/data-types/vitals#oxygen-saturation): Records oxygen saturation (SpO2) during
  sleep.
* [`RespiratoryRateRecord`](/health-and-fitness/health-connect/data-types/vitals#respiratory-rate): Records respiratory rate during sleep.

Each data type is stored as an individual record.

## Development considerations

Sleep tracking apps often need to run for extended periods, frequently
in the background when the screen is off. When building your sleep
features, it's important to consider how to manage background execution
and request the necessary permissions for sleep data.

### Background execution

Sleep tracking apps commonly run overnight with the screen off. When in this
state, you should use:

* Foreground services for data collection
* `WorkManager` for deferred write or syncing
* Batching strategies for regular record writes of granular data such as
  heart rate

Maintain continuity by keeping session ID consistent across all writes.

### Permissions

Your app must request the relevant Health Connect permissions before reading or
writing sleep data. For a complete list of data types, see
[Health Connect data types](/health-and-fitness/health-connect/data-types). Common permissions for sleep include sleep
sessions and metrics like heart rate or oxygen saturation.

Access to sleep is protected by the following permissions:

* `android.permission.health.READ_SLEEP`
* `android.permission.health.WRITE_SLEEP`

To add sleep capability to your app, start by requesting
permissions for the `SleepSession` data type.

Here's the permission you need to declare to be able to write
sleep:

```
<application>
  <uses-permission
android:name="android.permission.health.WRITE_SLEEP" />
...
</application>
```

To read sleep, you need to request the following permissions:

```
<application>
  <uses-permission
android:name="android.permission.health.READ_SLEEP" />
...
</application>
```

The following shows an example of how to request permissions for a sleep
session that includes heart rate, oxygen saturation, and respiratory rate data:

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.

```
// Create a set of permissions for required data types
val PERMISSIONS =
    setOf(
  HealthPermission.getReadPermission(SleepSessionRecord::class),
  HealthPermission.getWritePermission(SleepSessionRecord::class),
  HealthPermission.getReadPermission(HeartRateRecord::class),
  HealthPermission.getWritePermission(HeartRateRecord::class),
  HealthPermission.getReadPermission(OxygenSaturationRecord::class),
  HealthPermission.getWritePermission(OxygenSaturationRecord::class),
  HealthPermission.getReadPermission(RespiratoryRateRecord::class),
  HealthPermission.getWritePermission(RespiratoryRateRecord::class)
)
```

Use [`getGrantedPermissions`](/reference/kotlin/androidx/health/connect/client/PermissionController#getGrantedPermissions()) to see if your app already has the
required permissions granted. If not, use
[`createRequestPermissionResultContract`](/reference/kotlin/androidx/health/connect/client/PermissionController#createRequestPermissionResultContract(kotlin.String)) to request
those permissions. This displays the Health Connect permissions screen.

```
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
```

Because users can grant or revoke permissions at any time, your app needs to
check for permissions every time before using them and handle scenarios where
permission is lost.

## Implement a sleep session

This section describes the recommended workflow for recording sleep data.

To align data types like `HeartRateRecord` or `OxygenSaturationRecord` with a
sleep session, record them with timestamps that fall between the session's
`startTime` and `endTime`. Health Connect doesn't use a session identifier to
link sleep sessions with granular data. Instead, association is implicit through
overlapping time intervals. When reading sleep data, you can use a session's
time range to query for associated data types, as shown in
[Reading sleep data](#reading-sleep-data).

### Write a session

While granular data such as heart rate can be recorded throughout a sleep
session, the `SleepSessionRecord` itself must only be written to Health
Connect once the session has finished, for example when the user wakes up. The
record must include the
session `startTime`, `endTime`, and a list of `SleepSessionRecord.Stage`
objects recorded during the session, as `SleepSessionRecord` requires `endTime`
to be after `startTime`.

To write a sleep session:

1. Generate a unique client record ID.
2. When the user wakes up, or sleep tracking is stopped, gather all sleep
   stages and construct a `SleepSessionRecord`.
3. Insert the record using `insertRecords`.

**Best Practice:** Use Client IDs When creating records, set a
**metadata.clientRecordId**. This is the most effective way to prevent
duplicates during sync retries. See [Best practices](#best-practices)
for a code example.

Example:

```
val clientRecordId = UUID.randomUUID().toString()
val sessionStartTime = LocalDateTime.of(2023, 10, 30, 22, 0).toInstant(ZoneOffset.UTC)
val sessionEndTime = LocalDateTime.of(2023, 10, 31, 7, 0).toInstant(ZoneOffset.UTC)

val stages = mutableListOf<SleepSessionRecord.Stage>()
// Add recorded stages, for example:
stages.add(SleepSessionRecord.Stage(
    startTime = sessionStartTime.plusSeconds(3600),
    endTime = sessionStartTime.plusSeconds(7200),
    stage = SleepSessionRecord.STAGE_TYPE_LIGHT)
)
stages.add(SleepSessionRecord.Stage(
    startTime = sessionStartTime.plusSeconds(7200),
    endTime = sessionStartTime.plusSeconds(10800),
    stage = SleepSessionRecord.STAGE_TYPE_DEEP)
)
// ... other stages

val session = SleepSessionRecord(
    startTime = sessionStartTime,
    startZoneOffset = ZoneOffset.UTC,
    endTime = sessionEndTime,
    endZoneOffset = ZoneOffset.UTC,
    stages = stages,
    metadata = Metadata(clientRecordId = clientRecordId)
)

healthConnectClient.insertRecords(listOf(session))
```

## Reading sleep data

Apps can read sleep sessions and their associated data to summarize activity,
provide health insights, or sync data with an external server. For example, you
can read a `SleepSessionRecord` and then query the `HeartRateRecord`
that occurred during that same time interval.

### Read session with associated data

You can read sleep sessions using a `ReadRecordsRequest` with
`SleepSessionRecord` as the record type, filtered by a time range. To read
associated data for a given session, make a second request for the selected
data type, such as `HeartRateRecord`—filtering by the `startTime` and `endTime`
of the sleep session.

The following example shows how to read sleep sessions with associated heart
rate data for a given time range:

```
suspend fun readSleepSessionsWithAssociatedData(
    healthConnectClient: HealthConnectClient,
    startTime: Instant,
    endTime: Instant
) {
    val response = healthConnectClient.readRecords(
        ReadRecordsRequest(
            recordType = SleepSessionRecord::class,
            timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
        )
    )

    for (sleepRecord in response.records) {
        // Process each session
        val stages = sleepRecord.stages
        val notes = sleepRecord.notes

        // To read specific granular data (like heart rate) that occurred during
        // this session, use the session's startTime and endTime to filter
        // the request for that data type.
        val hrResponse = healthConnectClient.readRecords(
            ReadRecordsRequest(
                recordType = HeartRateRecord::class,
                timeRangeFilter = TimeRangeFilter.between(
                    sleepRecord.startTime,
                    sleepRecord.endTime
                )
            )
        )
        for (heartRateRecord in hrResponse.records) {
            for (sample in heartRateRecord.samples) {
                val bpm = sample.beatsPerMinute
            }
        }
    }
}
```

## Best practices

Follow these guidelines to improve data reliability and user experience:

* **Write frequently during active tracking**: For active tracking, write data as it becomes available or at a maximum interval of 15 minutes.
* **Use WorkManager for background syncs**: Use [`WorkManager`](/reference/androidx/work/WorkManager) for deferred writes. Aim for a 15-minute interval to strike a balance between real-time data and battery efficiency.
* **Batch write requests**: Don't write every single sensor event individually. Chunk your requests. Health Connect handles up to 1000 records per write request.
* **Keep session IDs stable and unique**: Use consistent identifiers for your sessions. If a session is edited or updated, using the same ID prevents it from being treated as a new, separate session.
* **Use batching for data types**: To reduce Input/Output overhead and preserve battery life, group your data points into a single `insertRecords` call rather than writing each point individually.
* **Avoid writing duplicate data: Use Client IDs**: When creating records, set a `metadata.clientRecordId`. Health Connect uses this to identify unique records. If you attempt to write a record with a `clientRecordId` that already exists, Health Connect will ignore the duplicate or update the existing record rather than creating a new one. Setting a `metadata.clientRecordId` is the most effective way to prevent duplicates during sync retries or app reinstalls.  

  ```
  val record = StepsRecord(
      count = 100,
      startTime = startTime,
      endTime = endTime,
      startZoneOffset = ZoneOffset.UTC,
      endZoneOffset = ZoneOffset.UTC,
      metadata = Metadata(
          // Use a unique ID from your own database
          clientRecordId = "daily_steps_2023_10_27_user_123"
      )
  )
  ```
* **Check existing data**: Before syncing, query the time range to see if records from your app already exist.
* **Ensure timestamps do not overlap**: Verify that a new session does not start before the previous one ends. Overlapping sessions can cause conflicts in fitness dashboards and summary calculations.
* **Provide clear rationales for permission**: Use the `Permission.createIntent` flow to explain why your app needs access to health data, for example: 'To monitor your blood pressure trends and provide insights.'
* **Test long-running sessions**: Monitor battery consumption during sessions lasting several hours to verify your batching interval and sensor usage don't drain the device.
* **Align timestamps with sensor rates**: Match your record timestamps to the actual frequency of your sensors to maintain data high-fidelity.

## Testing

To verify data correctness and a high-quality user experience, follow these
testing strategies and refer to the official [Test top use cases](/health-and-fitness/health-connect/test/test-cases)
documentation.

### Verification tools

* **[Health Connect Toolbox](/health-and-fitness/health-connect/test/health-connect-toolbox):** Use this companion app to manually inspect
  records, delete test data, and simulate changes to the database. It is the
  best way to verify that your records are being stored correctly.
* **[Unit testing with `FakeHealthConnectClient`](/health-and-fitness/health-connect/test/unit-tests):** Use the testing library
  to verify how your app handles edge cases, like permission revocation or API
  exceptions without needing a physical device.

### Quality checklist

**Confirm records in Health Connect:** Open the
Health Connect app and navigate to Data and access to verify records appear
with expected values.

**Read data from other apps:** Test your app's
ability to read sessions written by other apps to verify ecosystem
compatibility. See [Reading sleep data](#reading-sleep-data).

**Balance write frequency:** Monitor battery usage.
Frequent writes provide high detail but increase drain.

## Typical architecture

A sleep tracking implementation commonly includes:

| Component | Manages |
| --- | --- |
| Session controller | Session state Timer Batching logic Data types controllers Data collection |
| Repository layer (wraps Health Connect operations:) | Insert session Insert data types Inserts sleep stages Read session summaries |
| UI Layer (Displays): | Duration Live data types Sleep stage visualization |

## Troubleshooting

| Symptom | Possible cause | Resolution |
| --- | --- | --- |
| Missing data types (for example, Heart Rate) | Missing write permissions or incorrect time filters. | Check that you have requested and the user has granted the specific data type permission. Verify your `ReadRecordsRequest` uses a `TimeRangeFilter` that matches the session. See [Permissions](#permissions). |
| Session fails to write | Overlapping timestamps. | Health Connect may reject records that overlap with existing data from the same app. Validate that the `startTime` of a new session is after the `endTime` of the previous one. |
| No sensor data recorded during sleep | Foreground service was killed or inactive. | To collect sensor data overnight while the screen is off, you can use a [Foreground Service](/develop/background-work/services/fgs) with `foregroundServiceType="health"`. |
| Duplicate records appear | Missing `clientRecordId`. | Assign a unique `clientRecordId` in the `Metadata` of each record. This allows Health Connect to perform de-duplication if the same data is written twice during a sync retry. See [Best practices](#best-practices). |

### Common debugging steps

|  |  |
| --- | --- |
| Check permission state. | Always call `getPermissionStatus()` before attempting a read or write operation. Users can revoke permissions in system settings at any time. |
| Verify execution mode. | If your app is not collecting data in the background, verify that you have declared the correct permissions in your `AndroidManifest.xml` file and that the user hasn't placed the app into "Battery Restricted" mode. |