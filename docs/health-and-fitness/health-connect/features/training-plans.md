---
title: https://developer.android.com/health-and-fitness/health-connect/features/training-plans
url: https://developer.android.com/health-and-fitness/health-connect/features/training-plans
source: md.txt
---

<br />

| **Note:** This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

<br />

Health Connect provides a *planned exercise* data type to enable training apps
to write training plans and enable workout apps to read training plans. Recorded
exercises (workouts) can be read back for personalized performance analysis to
help users achieve their training goals.

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

To determine whether a user's device supports training plans on Health Connect, check the availability of `FEATURE_PLANNED_EXERCISE` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_PLANNED_EXERCISE
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

See [Check for feature availability](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability) to learn more.

## Required permissions

Access to planned exercise is protected by the following permissions:

- `android.permission.health.READ_PLANNED_EXERCISE`
- `android.permission.health.WRITE_PLANNED_EXERCISE`

To add planned exercise capability to your app, start by requesting
permissions for the `PlannedExerciseSession` data type.

Here's the permission you need to declare to be able to write
planned exercise:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_PLANNED_EXERCISE" />
    ...
    </application>

To read planned exercise, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_PLANNED_EXERCISE" />
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
      HealthPermission.getReadPermission(HeartRateRecord::class),
      HealthPermission.getWritePermission(HeartRateRecord::class),
      HealthPermission.getReadPermission(PlannedExerciseSessionRecord::class),
      HealthPermission.getWritePermission(PlannedExerciseSessionRecord::class),
      HealthPermission.getReadPermission(ExerciseSessionRecord::class),
      HealthPermission.getWritePermission(ExerciseSessionRecord::class)
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

### Related permissions

Training plans are linked to *exercise sessions*. Therefore, the user must give
permission to use each record type related to a training plan in order to fully
utilize this feature of Health Connect.

For example, if a training plan measures a user's heart rate during a series
of runs, the following permissions might need to be declared by the developer
and granted by the user in order to write the exercise session and read the
results for later evaluation:

- `android.permission.health.READ_EXERCISE`
- `android.permission.health.READ_EXERCISE_ROUTES`
- `android.permission.health.READ_HEART_RATE`
- `android.permission.health.WRITE_EXERCISE`
- `android.permission.health.WRITE_EXERCISE_ROUTE`
- `android.permission.health.WRITE_HEART_RATE`

However, often the app that creates training plans and evaluates performance
against plans isn't the same as the app that consumes training plans and writes
actual exercise data. Depending on the type of app, not all read and write
permissions would be needed. For example, you may only need these permissions
for each type of app:

| Training plan app | Workout app |
|---|---|
| `WRITE_PLANNED_EXERCISE` | `READ_PLANNED_EXERCISE` |
| `READ_EXERCISE` | `WRITE_EXERCISE` |
| `READ_EXERCISE_ROUTES` | `WRITE_EXERCISE_ROUTE` |
| `READ_HEART_RATE` | `WRITE_HEART_RATE` |

| **Key Point:** Write permission also provides you read access to records you have written using that permission. It isn't always necessary to request both read and write permission for a data type.

## Information included in a planned exercise session record

- Title of the session.
- A list of [planned exercise blocks](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PlannedExerciseBlock).
- Start and end time of the session.
- Exercise type.
- Notes for the activity.
- Metadata.
- Completed exercise session ID --- This is written automatically after an exercise session related to this planned exercise session is completed.

### Information included in a planned exercise block record

A planned exercise block contains a list of exercise steps, to support
repetition of different groups of steps (for example, do a sequence of arm
curls, burpies, and crunches five times in a row).

- Description of the block.
- A list of [planned exercise steps](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PlannedExerciseStep).
- Number of repetitions.

### Information included in a planned exercise step record

- Description of the step.
- [Exercise category](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PlannedExerciseStep#constants).
- [Exercise type](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSegment).
- A list of [performance targets](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExercisePerformanceTarget).
- [Completion goal](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseCompletionGoal).

## Supported aggregations


There are no supported aggregations for this data type.

<br />

## Example usage

Suppose a user plans a 90 minute run two days from now. This run will feature
three laps around a lake with a target heart rate between 90 and 110 bpm.

1. A planned exercise session with the following is defined by the user in a training plan app:
   1. Planned start and end of the run
   2. The type of exercise (running)
   3. Number of laps (repetitions)
   4. Performance target for heart rate (between 90 and 110 bpm)
2. This information is grouped into exercise blocks and steps and written to Health Connect by the training plan app as a `PlannedExerciseSessionRecord`.
3. The user performs the planned session (running).
4. Exercise data related to the session is recorded either:
   1. By a wearable during the session. For example, heart rate. This data is written to Health Connect as the record type for the activity. In this case, `HeartRateRecord`.
   2. Manually by the user after the session. For example, indicating the start and end of the actual run. This data is written to Health Connect as an `ExerciseSessionRecord`.
5. At a later time, the training plan app reads data from Health Connect to evaluate the actual performance against the targets set by the user in the planned exercise session.

### Plan exercises and set targets

A user may plan their exercise in the future and set targets. Write this to
Health Connect as a *planned exercise session*.

In the example described in [Example usage](https://developer.android.com/health-and-fitness/health-connect/features/training-plans#example-usage),
the user plans a 90 minute run two days from now. This run will feature three
laps around a lake with a target heart rate between 90 and 110 bpm.

A snippet like this may be found in the form handler for an app that logs
planned exercise sessions to Health Connect. It could also be found in the
ingest point for integrations, say with a service that offers training.

    // Verify the user has granted all necessary permissions for this task
    val grantedPermissions =
        healthConnectClient.permissionController.getGrantedPermissions()
    if (!grantedPermissions.contains(
          HealthPermission.getWritePermission(PlannedExerciseSessionRecord::class))) {
        // The user hasn't granted the app permission to write planned exercise session data.
        return
    }

    val plannedDuration = Duration.ofMinutes(90)
    val plannedStartDate = LocalDate.now().plusDays(2)

    val plannedExerciseSessionRecord = PlannedExerciseSessionRecord(
        startDate = plannedStartDate,
        duration = plannedDuration,
        exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_RUNNING,
        blocks = listOf(
            PlannedExerciseBlock(
                repetitions = 1, steps = listOf(
                    PlannedExerciseStep(
                        exerciseType = ExerciseSegment.EXERCISE_SEGMENT_TYPE_RUNNING,
                        exercisePhase = PlannedExerciseStep.EXERCISE_PHASE_ACTIVE,
                        completionGoal = ExerciseCompletionGoal.RepetitionsGoal(repetitions = 3),
                        performanceTargets = listOf(
                            ExercisePerformanceTarget.HeartRateTarget(
                                minHeartRate = 90.0, maxHeartRate = 110.0
                            )
                        )
                    ),
                ), description = "Three laps around the lake"
            )
        ),
        title = "Run at lake",
        notes = null,
        metadata = Metadata.manualEntry(
          device = Device(type = Device.Companion.TYPE_PHONE)
        )
    )
    val insertedPlannedExerciseSessions =
        healthConnectClient.insertRecords(listOf(plannedExerciseSessionRecord)).recordIdsList
    val insertedPlannedExerciseSessionId = insertedPlannedExerciseSessions.first()

### Log exercise and activity data

Two days later, the user logs the actual exercise session. Write this to Health
Connect as an *exercise session*.

In this example, the user's session duration matched the planned duration
exactly.

The following snippet might be found in the form handler for an app that logs
exercise sessions to Health Connect. It might also be found in data ingest and
export handlers for a wearable capable of detecting and logging exercise
sessions.

`insertedPlannedExerciseSessionId` here is reused from the previous example. In
a real app, the ID would be determined by the user selecting a planned exercise
session from a list of existing sessions.

    // Verify the user has granted all necessary permissions for this task
    val grantedPermissions =
        healthConnectClient.permissionController.getGrantedPermissions()
    if (!grantedPermissions.contains(
          HealthPermission.getWritePermission(ExerciseSessionRecord::class))) {
        // The user doesn't granted the app permission to write exercise session data.
        return
    }

    val sessionDuration = Duration.ofMinutes(90)
    val sessionEndTime = Instant.now()
    val sessionStartTime = sessionEndTime.minus(sessionDuration)

    val exerciseSessionRecord = ExerciseSessionRecord(
        startTime = sessionStartTime,
        startZoneOffset = ZoneOffset.UTC,
        endTime = sessionEndTime,
        endZoneOffset = ZoneOffset.UTC,
        exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_RUNNING,
        segments = listOf(
            ExerciseSegment(
                startTime = sessionStartTime,
                endTime = sessionEndTime,
                repetitions = 3,
                segmentType = ExerciseSegment.EXERCISE_SEGMENT_TYPE_RUNNING
            )
        ),
        title = "Run at lake",
        plannedExerciseSessionId = insertedPlannedExerciseSessionId,
        metadata = Metadata.manualEntry(
          device = Device(type = Device.Companion.TYPE_PHONE)
        )
    )
    val insertedExerciseSessions =
        healthConnectClient.insertRecords(listOf(exerciseSessionRecord))

A wearable also logs their heart rate throughout the run. The following snippet
could be used to generate records within the target range.

In a real app, the primary pieces of this snippet might be found in the handler
for a message from a wearable, which would write measurement to Health Connect
upon collection.

    // Verify the user has granted all necessary permissions for this task
    val grantedPermissions =
        healthConnectClient.permissionController.getGrantedPermissions()
    if (!grantedPermissions.contains(
          HealthPermission.getWritePermission(HeartRateRecord::class))) {
        // The user doesn't granted the app permission to write heart rate record data.
        return
    }

    val samples = mutableListOf<HeartRateRecord.Sample>()
    var currentTime = sessionStartTime
    while (currentTime.isBefore(sessionEndTime)) {
        val bpm = Random.nextInt(21) + 90
        val heartRateRecord = HeartRateRecord.Sample(
            time = currentTime,
            beatsPerMinute = bpm.toLong(),
        )
        samples.add(heartRateRecord)
        currentTime = currentTime.plusSeconds(180)
    }

    val heartRateRecord = HeartRateRecord(
        startTime = sessionStartTime,
        startZoneOffset = ZoneOffset.UTC,
        endTime = sessionEndTime,
        endZoneOffset = ZoneOffset.UTC,
        samples = samples,
        metadata = Metadata.autoRecorded(
          device = Device(type = Device.Companion.TYPE_WATCH)
        )
    )
    val insertedHeartRateRecords = healthConnectClient.insertRecords(listOf(heartRateRecord))

### Evaluate performance targets

The day after the user's workout, you can retrieve the logged exercise, check
for any planned exercise targets, and evaluate additional data types to
determine if set targets were met.

A snippet like this would likely be found in a periodic job to evaluate
performance targets or when loading a list of exercises and displaying a
notification about performance targets in an app.

    // Verify the user has granted all necessary permissions for this task
    val grantedPermissions =
         healthConnectClient.permissionController.getGrantedPermissions()
    if (!grantedPermissions.containsAll(
            listOf(
                HealthPermission.getReadPermission(ExerciseSessionRecord::class),
                HealthPermission.getReadPermission(PlannedExerciseSessionRecord::class),
                HealthPermission.getReadPermission(HeartRateRecord::class)
            )
        )
    ) {
        // The user doesn't granted the app permission to read exercise session record data.
        return
    }

    val searchDuration = Duration.ofDays(1)
    val searchEndTime = Instant.now()
    val searchStartTime = searchEndTime.minus(searchDuration)

    val response = healthConnectClient.readRecords(
        ReadRecordsRequest<ExerciseSessionRecord>(
            timeRangeFilter = TimeRangeFilter.between(searchStartTime, searchEndTime)
        )
    )
    for (exerciseRecord in response.records) {
        val plannedExerciseRecordId = exerciseRecord.plannedExerciseSessionId
        val plannedExerciseRecord =
            if (plannedExerciseRecordId == null) null else healthConnectClient.readRecord(
                PlannedExerciseSessionRecord::class, plannedExerciseRecordId
            ).record
        if (plannedExerciseRecord != null) {
            val aggregateRequest = AggregateRequest(
                metrics = setOf(HeartRateRecord.BPM_AVG),
                timeRangeFilter = TimeRangeFilter.between(
                    exerciseRecord.startTime, exerciseRecord.endTime
                ),
            )
            val aggregationResult = healthConnectClient.aggregate(aggregateRequest)

            val maxBpm = aggregationResult[HeartRateRecord.BPM_MAX]
            val minBpm = aggregationResult[HeartRateRecord.BPM_MIN]
            if (maxBpm != null && minBpm != null) {
                plannedExerciseRecord.blocks.forEach { block ->
                    block.steps.forEach { step ->
                        step.performanceTargets.forEach { target ->
                            when (target) {
                                is ExercisePerformanceTarget.HeartRateTarget -> {
                                    val minTarget = target.minHeartRate
                                    val maxTarget = target.maxHeartRate
                                    if(
                                        minBpm >= minTarget && maxBpm <= maxTarget
                                    ) {
                                      // Success!
                                    }
                                }
                                // Handle more target types
                                }
                            }
                        }
                    }
                }
            }
        }
    }

## Exercise sessions

Exercise sessions can include anything from running to badminton.

### Write exercise sessions

This is how to build an insertion request that includes a session:

    suspend fun writeExerciseSession(healthConnectClient: HealthConnectClient) {
        healthConnectClient.insertRecords(
            listOf(
                ExerciseSessionRecord(
                    startTime = START_TIME,
                    startZoneOffset = START_ZONE_OFFSET,
                    endTime = END_TIME,
                    endZoneOffset = END_ZONE_OFFSET,
                    exerciseType = ExerciseSessionRecord.ExerciseType.RUNNING,
                    title = "My Run",
                    metadata = Metadata.manualEntry()
                ),
                // ... other records
            )
        )
    }

### Read an exercise session

Here's an example of how to read an exercise session:

    suspend fun readExerciseSessions(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        val response =
            healthConnectClient.readRecords(
                ReadRecordsRequest(
                    ExerciseSessionRecord::class,
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
        for (exerciseRecord in response.records) {
            // Process each exercise record
            // Optionally pull in with other data sources of the same time range.
            val distanceRecord =
                healthConnectClient
                    .readRecords(
                        ReadRecordsRequest(
                            DistanceRecord::class,
                            timeRangeFilter =
                                TimeRangeFilter.between(
                                    exerciseRecord.startTime,
                                    exerciseRecord.endTime
                                )
                        )
                    )
                    .records
        }
    }

### Write subtype data

Sessions can also be comprised of optional subtype data, that enrich the
session with additional information.

For example, exercise sessions can include the `ExerciseSegment`, `ExerciseLap`
and `ExerciseRoute` classes:

    val segments = listOf(
      ExerciseSegment(
        startTime = Instant.parse("2022-01-02T10:10:10Z"),
        endTime = Instant.parse("2022-01-02T10:10:13Z"),
        segmentType = ActivitySegmentType.BENCH_PRESS,
        repetitions = 373
      )
    )

    val laps = listOf(
      ExerciseLap(
        startTime = Instant.parse("2022-01-02T10:10:10Z"),
        endTime = Instant.parse("2022-01-02T10:10:13Z"),
        length = 0.meters
      )
    )

    ExerciseSessionRecord(
      exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_CALISTHENICS,
        startTime = Instant.parse("2022-01-02T10:10:10Z"),
        endTime = Instant.parse("2022-01-02T10:10:13Z"),
      startZoneOffset = ZoneOffset.UTC,
      endZoneOffset = ZoneOffset.UTC,
      segments = segments,
      laps = laps,
      route = route,
      metadata = Metadata.manualEntry()
    )