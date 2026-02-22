---
title: https://developer.android.com/health-and-fitness/health-connect/features/exercise-routes
url: https://developer.android.com/health-and-fitness/health-connect/features/exercise-routes
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

Exercise routes allow users to track a GPS route for associated exercise
activities and share maps of their workouts with other apps.

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

This guide provides information on how to request permissions from the user and
also outlines how apps receive permission to write route data as part of
an exercise session.

The read and write functionality for exercise routes includes:

1. Apps create a new write permission for exercise routes.
2. Insertion happens by writing an exercise session with a route as its field.
3. Reading:
   1. For the session owner, data is accessed using a session read.
   2. From a third-party app, through a dialog that allows the user to grant a one-time read of a route.

If the user doesn't have write permissions and the route is not set, the route
doesn't update.

If your app has a route write permission and tries to update a session by
passing in a session object without a route, the existing route is deleted.

## Feature availability

To determine whether a user's device supports planned exercise on Health Connect, check the availability of `FEATURE_PLANNED_EXERCISE` on the client:

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

Access to exercise route is protected by the following permissions:

- `android.permission.health.READ_EXERCISE_ROUTES`
- `android.permission.health.WRITE_EXERCISE_ROUTE`

Note: For this permission type, `READ_EXERCISE_ROUTES` is plural, while `WRITE_EXERCISE_ROUTE` is singular.

To add exercise route capability to your app, start by requesting
permissions for the `ExerciseSession` data type.

Here's the permission you need to declare to be able to write
exercise route:

    <application>
      <uses-permission
    android:name="android.permission.health.WRITE_EXERCISE_ROUTE" />
    ...
    </application>

To read exercise route, you need to request the following permissions:

    <application>
      <uses-permission
    android:name="android.permission.health.READ_EXERCISE_ROUTES" />
    ...
    </application>

You also have to declare an exercise permission, as each route is associated
with an exercise session (one session = one workout).

To request permissions, use the
`PermissionController.createRequestPermissionResultContract()` method when you
first connect your app to Health Connect. Several permissions that you might
want to request are:

- Read health and fitness data, including route data: `HealthPermission.getReadPermission(ExerciseSessionRecord::class)`
- Write health and fitness data, including route data: `HealthPermission.getWritePermission(ExerciseSessionRecord::class)`
- Write exercise route data: `HealthPermission.PERMISSION_WRITE_EXERCISE_ROUTE`

| **Note:** If the user doesn't grant all of the permissions that your app requests, your app should still run, and it should perform as many tasks as it can with the permissions that the user granted.

### Request permissions from the user

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.

    // Create a set of permissions for required data types
    val PERMISSIONS =
        setOf(
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
| **Note:** Even if your app has been granted "Always allow" access to exercise route data, background access to routes created by other apps is restricted.

## Information included in an exercise session record

Each exercise session record contains the following information:

- The exercise **type**, for example, biking.
- The exercise **route**, which contains information such as latitude, longitude, and altitude.

## Supported aggregations

<br />

The following aggregate values are available for
`ExerciseSessionRecord`:

- [`EXERCISE_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSessionRecord#EXERCISE_DURATION_TOTAL())

<br />

## Example usage

The following code snippets show how to read and write an exercise route.

### Read exercise route

Your app can't read exercise route data created by other apps when it runs in
the background.

When your app runs in the background and tries to read an exercise route created
by another app, Health Connect returns an `ExerciseRouteResult.ConsentRequired`
response, even if your app has **Always allow** access to exercise
route data.

For this reason, we strongly recommend that you request routes upon deliberate
user interaction with your app, when the user is actively engaged with your
app's UI.

To learn more about background reads, see [Background read example](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example).

The following code snippet demonstrates how to read a session in Health Connect
and request a route from that session:

    suspend fun readExerciseSessionAndRoute() {
        val endTime = Instant.now()
        val startTime = endTime.minus(Duration.ofHours(1))

        val grantedPermissions =
            healthConnectClient.permissionController.getGrantedPermissions()
        if (!grantedPermissions.contains(
              HealthPermission.getReadPermission(ExerciseSessionRecord::class))) {
            // The user doesn't allow the app to read exercise session data.
            return
        }

        val readResponse =
          healthConnectClient.readRecords(
            ReadRecordsRequest(
              ExerciseSessionRecord::class,
              TimeRangeFilter.between(startTime, endTime)
            )
          )
        val exerciseRecord = readResponse.records.first()
        val recordId = exerciseRecord.metadata.id

        // See https://developer.android.com/training/basics/intents/result#launch
        // for appropriately handling ActivityResultContract.
        val requestExerciseRouteLauncher = fragment.registerForActivityResul
        (ExerciseRouteRequestContract()) { exerciseRoute: ExerciseRoute? ->
                if (exerciseRoute != null) {
                    displayExerciseRoute(exerciseRoute)
                } else {
                    // Consent was denied
                }
            }

        val exerciseSessionRecord =
          healthConnectClient.readRecord(ExerciseSessionRecord::class, recordId).record

        when (val exerciseRouteResult = exerciseSessionRecord.exerciseRouteResult) {
            is ExerciseRouteResult.Data ->
                displayExerciseRoute(exerciseRouteResult.exerciseRoute)
            is ExerciseRouteResult.ConsentRequired ->
                requestExerciseRouteLauncher.launch(recordId)
            is ExerciseRouteResult.NoData -> Unit // No exercise route to show
            else -> Unit
        }
      }

      fun displayExerciseRoute(route: ExerciseRoute?) {
        val locations = route.route.orEmpty()
        for (location in locations) {
          // Handle location.
        }
      }

### Write an exercise route

The following code demonstrates how to record a session that includes an
exercise route:

    suspend fun InsertExerciseRoute(healthConnectClient: HealthConnectClient) {
        val grantedPermissions =
            healthConnectClient.permissionController.getGrantedPermissions()
        if (!grantedPermissions.contains(
              getWritePermission(ExerciseSessionRecord::class))) {
            // The user doesn't allow the app to write exercise session data.
            return
        }

        val sessionStartTime = Instant.now()
        val sessionDuration = Duration.ofMinutes(20)
        val sessionEndTime = sessionStartTime.plus(sessionDuration)

        val exerciseRoute =
            if (grantedPermissions.contains(PERMISSION_WRITE_EXERCISE_ROUTE)) ExerciseRoute(
                listOf(
                    ExerciseRoute.Location(
                        // Location times must be on or after the session start time
                        time = sessionStartTime,
                        latitude = 6.5483,
                        longitude = 0.5488,
                        horizontalAccuracy = Length.meters(2.0),
                        verticalAccuracy = Length.meters(2.0),
                        altitude = Length.meters(9.0),
                    ), ExerciseRoute.Location(
                        // Location times must be before the session end time
                        time = sessionEndTime.minusSeconds(1),
                        latitude = 6.4578,
                        longitude = 0.6577,
                        horizontalAccuracy = Length.meters(2.0),
                        verticalAccuracy = Length.meters(2.0),
                        altitude = Length.meters(9.2),
                    )
                )
            )
            else
            // The user doesn't allow the app to write exercise route data.
                null
        val exerciseSessionRecord = ExerciseSessionRecord(
            startTime = sessionStartTime,
            startZoneOffset = ZoneOffset.UTC,
            endTime = sessionEndTime,
            endZoneOffset = ZoneOffset.UTC,
            exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_BIKING,
            title = "Morning Bike Ride",
            exerciseRoute = exerciseRoute,
            metadata = Metadata.manualEntry(
                device = Device(type = Device.TYPE_PHONE)
            ),
        )
        val response = healthConnectClient.insertRecords(listOf(exerciseSessionRecord))
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

### Delete an exercise session

There are two ways to delete an exercise session:

1. By time range.
2. By UID.

Here's how you delete subtype data according to time range:

    suspend fun deleteExerciseSessionByTimeRange(
        healthConnectClient: HealthConnectClient,
        exerciseRecord: ExerciseSessionRecord,
    ) {
        val timeRangeFilter = TimeRangeFilter.between(exerciseRecord.startTime, exerciseRecord.endTime)
        healthConnectClient.deleteRecords(ExerciseSessionRecord::class, timeRangeFilter)
        // delete the associated distance record
        healthConnectClient.deleteRecords(DistanceRecord::class, timeRangeFilter)
    }

You can also delete subtype data by UID. Doing so only deletes the
exercise session, not the associated data:

    suspend fun deleteExerciseSessionByUid(
        healthConnectClient: HealthConnectClient,
        exerciseRecord: ExerciseSessionRecord,
    ) {
        healthConnectClient.deleteRecords(
            ExerciseSessionRecord::class,
            recordIdsList = listOf(exerciseRecord.metadata.id),
            clientRecordIdsList = emptyList()
        )
    }