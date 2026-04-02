---
title: Track sleep sessions  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-connect/features/sleep-sessions
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Health Connect Guides](https://developer.android.com/health-and-fitness/health-connect)

# Track sleep sessions Stay organized with collections Save and categorize content based on your preferences.



> This guide is compatible with Health Connect version [1.1.0-alpha11](/jetpack/androidx/releases/health-connect#1.1.0-alpha11).

Health Connect provides a *sleep session* data type, to store information about
a user's sleep, such as a nightly session or daytime nap.
The `SleepSessionRecord` data type is used to represent these sessions.

Sessions allow users to measure time-based performance over a period of time,
such as continuous heart rate or location data.

`SleepSessionRecord` sessions contain data that records sleep stages, such as
`AWAKE`, `SLEEPING` and `DEEP`.

**Subtype** data is data that "belongs" to a session and is only meaningful when
it's read with a parent session. For example, sleep stage.

**Associated data**, on the other hand, refers to data that is recorded
independently but falls within the time range of a session. For example, if a
user records Heart Rate during their sleep session, the Heart Rate data would
be associated data. Unlike subtype data which is part of the session record,
associated data consists of independent records, each with its own UUID.

## Check Health Connect availability

Before attempting to use Health Connect, your app should verify that Health Connect is available
on the user's device. Health Connect might not be pre-installed on all devices or could be disabled.
You can check for availability using the `HealthConnectClient.getSdkStatus()`
method.

#### How to check for Health Connect availability

```
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

There is no feature availability flag for this data type.

## Required permissions

Access to sleep session is protected by the following permissions:

* `android.permission.health.READ_SLEEP`
* `android.permission.health.WRITE_SLEEP`

To add sleep session capability to your app, start by requesting
permissions for the `SleepSession` data type.

Here's the permission you need to declare to be able to write
sleep session:

```
<application>
  <uses-permission
android:name="android.permission.health.WRITE_SLEEP" />
...
</application>
```

To read sleep session, you need to request the following permissions:

```
<application>
  <uses-permission
android:name="android.permission.health.READ_SLEEP" />
...
</application>
```

### Request permissions from the user

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
  HealthPermission.getWritePermission(SleepSessionRecord::class)
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

## Supported aggregations

The following aggregate values are available for
`SleepSessionRecord`:

* [`SLEEP_DURATION_TOTAL`](/reference/kotlin/androidx/health/connect/client/records/SleepSessionRecord#SLEEP_DURATION_TOTAL())

## General guidance

Here are some best practice guidelines on how to work with sleep sessions in
Health Connect.

* Sessions should be used to add data from a specific sleep session,
  for sleep:

```
suspend fun writeSleepSession(healthConnectClient: HealthConnectClient) {
    healthConnectClient.insertRecords(
        listOf(
            SleepSessionRecord(
                startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
                startZoneOffset = ZoneOffset.of("-08:00"),
                endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
                endZoneOffset = ZoneOffset.of("-08:00"),
                title = "My Sleep"
            ),
        )
    )
}
```

* Subtype data needs to be aligned in a session with sequential timestamps
  that don't overlap. Gaps are allowed, however.
* Subtype data doesn't contain a UUID, but associated data has distinct UUIDs.
* Sessions are useful if the user wants data to be associated with (and
  tracked as part of) a session, rather than recorded continuously.

## Sleep sessions

You can read or write sleep data in Health Connect. Sleep data is displayed as a
session, and can be divided into 8 distinct sleep stages:

* `UNKNOWN`: Unspecified or unknown if the user is sleeping.
* `AWAKE`: The user is awake within a sleep cycle, not during the day.
* `SLEEPING`: Generic or non-granular sleep description.
* `OUT_OF_BED`: The user gets out of bed in the middle of a sleep session.
* `AWAKE_IN_BED`: The user is awake in bed.
* `LIGHT`: The user is in a light sleep cycle.
* `DEEP`: The user is in a deep sleep cycle.
* `REM`: The user is in a REM sleep cycle.

These values represent the type of sleep a user experiences within a time range.
Writing sleep stages is optional, but recommended if available.

### Write sleep sessions

The `SleepSessionRecord` data type has two parts:

1. The overall session, spanning the entire duration of sleep.
2. Individual stages during the sleep session such as light sleep or deep
   sleep.

Here's how you insert a sleep session without stages:

```
SleepSessionRecord(
      title = "weekend sleep",
      startTime = startTime,
      endTime = endTime,
      startZoneOffset = ZoneOffset.UTC,
      endZoneOffset = ZoneOffset.UTC,
)
```

Here's how to add stages that cover the entire period of a sleep session:

```
val stages = listOf(
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T01:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_SLEEPING,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T01:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T02:30:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_LIGHT,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T02:30:00.000Z"),
        endTime = Instant.parse("2022-05-11T05:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_DEEP,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T05:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_REM,
    ),
)

SleepSessionRecord(
        title = "weekend sleep",
        startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
        startZoneOffset = ZoneOffset.of("-08:00"),
        endZoneOffset = ZoneOffset.of("-08:00"),
        stages = stages,
)
```

### Read a sleep session

For every sleep session returned, you should check whether sleep stage data is
also present:

```
suspend fun readSleepSessions(
    healthConnectClient: HealthConnectClient,
    startTime: Instant,
    endTime: Instant
) {
    val response =
        healthConnectClient.readRecords(
            ReadRecordsRequest(
                SleepSessionRecord::class,
                timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
            )
        )
    for (sleepRecord in response.records) {
        // Retrieve relevant sleep stages from each sleep record
        val sleepStages = sleepRecord.stages
    }
}
```

### Delete a sleep session

This is how to delete a session. For this example, we've used a sleep session:

```
suspend fun deleteSleepSession(
    healthConnectClient: HealthConnectClient,
    sleepRecord: SleepSessionRecord,
) {
    val timeRangeFilter = TimeRangeFilter.between(sleepRecord.startTime, sleepRecord.endTime)
    healthConnectClient.deleteRecords(SleepSessionRecord::class, timeRangeFilter)
}
```

**Note:** Deleting a session does not automatically delete data associated with that
session.