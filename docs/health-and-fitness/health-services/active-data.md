---
title: https://developer.android.com/health-and-fitness/health-services/active-data
url: https://developer.android.com/health-and-fitness/health-services/active-data
source: md.txt
---

Health Services provides support for workout apps through the
[`ExerciseClient`](https://developer.android.com/reference/kotlin/androidx/health/services/client/ExerciseClient).
With `ExerciseClient`, your app can control when an
exercise is in progress, add exercise goals, and get updates about the exercise
state, [exercise events](https://developer.android.com/training/wearables/health-services/active-data/exercise-events),
or other metrics. For more information, see the full list of
[exercise types](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseType)
that Health Services supports.

See the
[Exercise sample](https://github.com/android/health-samples/tree/main/health-services/ExerciseSampleCompose)
on GitHub.

## Add dependencies

To add a dependency on Health Services, you must add the Google Maven repository
to your project. For more information, see
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven).

Then, in your module-level `build.gradle` file, add the following dependency:

### Groovy

```groovy
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-beta01")
}
```
| **Note:** This API is asynchronous and relies on `ListenableFuture` extensively. See [Using a ListenableFuture](https://developer.android.com/guide/background/listenablefuture) for more information about this concept.

## App structure

Use the following app structure when building an exercise app with
Health Services:

- Keep your screens and navigation within a main activity.
- Manage the workout state, sensor data, [ongoing activity](https://developer.android.com/training/wearables/ongoing-activity), and data with a [foreground service](https://developer.android.com/guide/components/foreground-services).
- Store data with [Room](https://developer.android.com/jetpack/androidx/releases/room), and use [WorkManager](https://developer.android.com/jetpack/androidx/releases/work) to upload data.

When [preparing for a workout](https://developer.android.com/health-and-fitness/health-services/active-data#prepare) and during the workout, your activity
might be stopped for a variety of reasons. The user might switch to another app
or return to the watch face. The system might display something on top of your
activity, or the screen might turn off after a period of inactivity.
Use a continuously running [`ForegroundService`](https://developer.android.com/guide/components/foreground-services)
in conjunction with `ExerciseClient` to help ensure correct operation for the
entire workout.

Using a `ForegroundService` lets you use the
[Ongoing Activity API](https://developer.android.com/training/wearables/notifications/ongoing-activity) to show
an indicator on your watch surfaces, letting the user quickly return to the
workout.

It's essential that you request location data appropriately in your foreground
service. In your manifest file, specify the necessary [foreground service
types](https://developer.android.com/guide/topics/manifest/service-element#foregroundservicetype) and
[permissions](https://developer.android.com/training/location/permissions#foreground):

```xml
<manifest ...>
  <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <application ...>
    
      <!-- If your app is designed only for devices that run Wear OS 4
           or lower, use android:foregroundServiceType="location" instead. -->
      <service
          android:name=".MyExerciseSessionRecorder"
          android:foregroundServiceType="health|location">
      </service>
      
    </application>
</manifest>
```
| **Note:** If your exercise is prematurely ended with an `ExerciseEndReason` of `AUTO_ENDED_PERMISSION_LOST` errors, this is likely caused by a missing `ForegroundService` with appropriate location permissions.

Use
[`AmbientLifecycleObserver`](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientLifecycleObserver)
for your pre-workout activity, that contains the `prepareExercise()` call and
for your workout activity. However, don't update the display during the workout
during ambient mode: This is because Health Services batches workout data
when the device screen is in ambient mode to save power, so the information
displayed may not be recent. During workouts, show data that makes sense to the
user, displaying either up-to-date information or a blank screen.

## Check capabilities

Each `ExerciseType` supports certain data types for metrics and for
exercise goals. Check these capabilities at startup, because they can
vary depending on the device. A device might not support a certain
exercise type, or it might not support a specific function, such as
auto-pause. Additionally, the capabilities of a device might change over
time, such as after a software update.

On app startup, query the device capabilities and store and process the
following:

- The exercises that the platform supports.
- The features that are supported for each exercise.
- The data types supported for each exercise.
- The permissions required for each of those data types.

Use `ExerciseCapabilities.getExerciseTypeCapabilities()` with
your selected exercise type to see what kind of metrics you can request, what
exercise goals you can configure, and what other features are available for
that type. This is shown in the following example:

    val healthClient = HealthServices.getClient(this /*context*/)
    val exerciseClient = healthClient.exerciseClient
    lifecycleScope.launch {
        val capabilities = exerciseClient.getCapabilitiesAsync().await()
        if (ExerciseType.RUNNING in capabilities.supportedExerciseTypes) {
            runningCapabilities =
                capabilities.getExerciseTypeCapabilities(ExerciseType.RUNNING)
        }
    }

Inside the returned `ExerciseTypeCapabilities`,
[`supportedDataTypes`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#supportedDataTypes())
lists the data types that you can request data for. This varies by device, so
take care not to request a `DataType` that isn't supported, or your request
might fail.

Use the
[`supportedGoals`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#supportedGoals())
and
[`supportedMilestones`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#supportedMilestones())
fields to determine whether the exercise can support an exercise goal that you
want to create.

If your app lets the user use auto-pause, you
must check that this functionality is supported by the device using
[`supportsAutoPauseAndResume`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#supportsAutoPauseAndResume()).
`ExerciseClient` rejects requests that are not supported on the
device.

The following example checks the support for the `HEART_RATE_BPM` data type,
the `STEPS_TOTAL` goal capability, and the auto-pause functionality:

    // Whether we can request heart rate metrics.
    supportsHeartRate = DataType.HEART_RATE_BPM in runningCapabilities.supportedDataTypes

    // Whether we can make a one-time goal for aggregate steps.
    val stepGoals = runningCapabilities.supportedGoals[DataType.STEPS_TOTAL]
    supportsStepGoals =
        (stepGoals != null && ComparisonType.GREATER_THAN_OR_EQUAL in stepGoals)

    // Whether auto-pause is supported.
    val supportsAutoPause = runningCapabilities.supportsAutoPauseAndResume

## Register for exercise state updates

Exercise updates are delivered to a listener. Your app can only register a
single listener at a time. Set up your listener before starting the workout,
as shown in the following example.
Your listener only receives updates about exercises your app owns.

    val callback = object : ExerciseUpdateCallback {
        override fun onExerciseUpdateReceived(update: ExerciseUpdate) {
            val exerciseStateInfo = update.exerciseStateInfo
            val activeDuration = update.activeDurationCheckpoint
            val latestMetrics = update.latestMetrics
            val latestGoals = update.latestAchievedGoals
        }

        override fun onLapSummaryReceived(lapSummary: ExerciseLapSummary) {
            // For ExerciseTypes that support laps, this is called when a lap is marked.
        }

        override fun onAvailabilityChanged(
            dataType: DataType<*, *>,
            availability: Availability
        ) {
            // Called when the availability of a particular DataType changes.
            when {
                availability is LocationAvailability -> // Relates to Location/GPS.
                availability is DataTypeAvailability -> // Relates to another DataType.
            }
        }
    }
    exerciseClient.setUpdateCallback(callback)

## Manage the exercise lifetime

Health Services supports, at most, one exercise at a time across all apps on
the device. If an exercise is being tracked and a different app starts tracking
a new exercise, the first exercise terminates.

Before starting your exercise, do the following:

- Check whether an exercise is already being tracked, and react accordingly. For example, ask the user for confirmation before overriding a previous exercise and starting to track a new one.

The following example shows how to check for an existing exercise with
`getCurrentExerciseInfoAsync`:

    lifecycleScope.launch {
        val exerciseInfo = exerciseClient.getCurrentExerciseInfoAsync().await()
        when (exerciseInfo.exerciseTrackedStatus) {
            OTHER_APP_IN_PROGRESS -> // Warn user before continuing, will stop the existing workout.
            OWNED_EXERCISE_IN_PROGRESS -> // This app has an existing workout.
            NO_EXERCISE_IN_PROGRESS -> // Start a fresh workout.
        }
    }

### Permissions

When using `ExerciseClient`, make sure your app requests and maintains the
[necessary permissions](https://developer.android.com/health-and-fitness/guides/health-services/permissions).
If your app uses `LOCATION` data, make sure your app requests and maintains the
appropriate permissions for that as well.

For all data types, before calling `prepareExercise()` or `startExercise()`,
do the following:

- Specify the appropriate permissions for the requested datatypes in your `AndroidManifest.xml` file.
- Verify that the user has granted the necessary permissions. For more information, see [Request app permissions](https://developer.android.com/training/permissions/requesting). Health Services rejects the request if the necessary permissions are not already granted.

For location data, do the following additional steps:

- Check that GPS is enabled on the device using [`isProviderEnabled(LocationManager.GPS_PROVIDER)`](https://developer.android.com/reference/android/location/LocationManager#isProviderEnabled(java.lang.String)). Prompt the user to open the [location settings](https://developer.android.com/reference/android/provider/Settings#ACTION_LOCATION_SOURCE_SETTINGS) if necessary.
- Make sure that a `ForegroundService` with the appropriate `foregroundServiceType` is maintained throughout the workout.

## Prepare for a workout

Some sensors, like GPS or heart rate, might take a short time to warm up, or the
user might want to see their data before starting their workout. The optional
[`prepareExerciseAsync()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/ExerciseClient#prepareExerciseAsync(androidx.health.services.client.data.WarmUpConfig))
method lets these sensors warm up and data be received without starting
the timer for the workout. The `activeDuration` is not affected by this
preparation time.

Before making the call to `prepareExerciseAsync()`, check the following:

- Check the platform-wide location setting. The user controls this setting in
  the main Settings menu; it is different from the app-level permissions
  check.

  If the setting is off, notify the user that they've denied access to
  location, and prompt them to enable it if your app requires location.
- Confirm that your app has runtime permissions for body sensors
  (API level 35 or lower) or heart rate (API level 36+), activity recognition, and
  fine location. For missing permissions, prompt the user for runtime permissions,
  providing adequate context. If the user does not grant a specific permission,
  remove the data types associated with that permission from the call to
  `prepareExerciseAsync()`. If neither body sensor (heart rate on API level 36+)
  nor location permissions are given, don't call `prepareExerciseAsync()`, as the
  prepare call is specifically for acquiring a stable heart rate or GPS fix prior
  to starting an exercise. The app can still get step-based distance, pace, speed,
  and other metrics that don't require those permissions.

| **Note:** A synchronous version of `prepareExercise` is also available.

Do the following to verify that your call to `prepareExerciseAsync()` can
succeed:

- Use [`AmbientLifecycleObserver`](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientLifecycleObserver) for the pre-workout activity that contains the prepare call.
- Call `prepareExerciseAsync()` from your foreground service. If it is not in a service and is tied to the activity lifecycle, then the sensor preparation might be unnecessarily killed.
- Call `endExercise()` to turn off the sensors and reduce power usage if the user navigates away from the pre-workout activity.

The following example shows how to call `prepareExerciseAsync()`:

    val warmUpConfig = WarmUpConfig(
        ExerciseType.RUNNING,
        setOf(
            DataType.HEART_RATE_BPM,
            DataType.LOCATION
        )
    )
    // Only necessary to call prepareExerciseAsync if body sensor (API level 35
    // or lower), heart rate (API level 36+), or location permissions are given.
    exerciseClient.prepareExerciseAsync(warmUpConfig).await()

    // Data and availability updates are delivered to the registered listener.

Once the app is in the `PREPARING` state, sensor availability updates are
delivered in the `ExerciseUpdateCallback` through `onAvailabilityChanged()`.
This information can then be presented to the user so they can decide whether
to start their workout.

## Start the workout

When you want to start an exercise, create an `ExerciseConfig` to configure the
exercise type, the data types for which you want to receive metrics, and any
exercise goals or milestones.

Exercise goals consist of a `DataType` and a
condition. Exercise goals are a one-time goal that are triggered when a
condition is met, such as when the user runs a certain distance. An exercise
milestone can also be set. Exercise milestones can be triggered multiple times,
such as each time the user
runs a certain point past their set distance.

The following sample shows how to create one goal of each type:

    const val CALORIES_THRESHOLD = 250.0
    const val DISTANCE_THRESHOLD = 1_000.0 // meters

    suspend fun startExercise() {
        // Types for which we want to receive metrics.
        val dataTypes = setOf(
            DataType.HEART_RATE_BPM,
            DataType.CALORIES_TOTAL,
            DataType.DISTANCE
        )

        // Create a one-time goal.
        val calorieGoal = ExerciseGoal.createOneTimeGoal(
            DataTypeCondition(
                dataType = DataType.CALORIES_TOTAL,
                threshold = CALORIES_THRESHOLD,
                comparisonType = ComparisonType.GREATER_THAN_OR_EQUAL
            )
        )

        // Create a milestone goal. To make a milestone for every kilometer, set the initial
        // threshold to 1km and the period to 1km.
        val distanceGoal = ExerciseGoal.createMilestone(
            condition = DataTypeCondition(
                dataType = DataType.DISTANCE_TOTAL,
                threshold = DISTANCE_THRESHOLD,
                comparisonType = ComparisonType.GREATER_THAN_OR_EQUAL
            ),
            period = DISTANCE_THRESHOLD
        )

        val config = ExerciseConfig(
            exerciseType = ExerciseType.RUNNING,
            dataTypes = dataTypes,
            isAutoPauseAndResumeEnabled = false,
            isGpsEnabled = true,
            exerciseGoals = mutableListOf<ExerciseGoal<Double>>(calorieGoal, distanceGoal)
        )
        exerciseClient.startExerciseAsync(config).await()
    }

You can also mark laps for all exercises. Health Services provides an
[`ExerciseLapSummary`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseLapSummary) with metrics aggregated over the
lap period.

The previous example shows the use of `isGpsEnabled`, which must be true
when requesting location data. However, using GPS can also assist with other
metrics. If the `ExerciseConfig` specifies distance as a `DataType`,
this defaults to using steps to estimate distance. By optionally enabling GPS,
location information can be used instead to estimate distance.

## Pause, resume, and end a workout

You can pause, resume, and end workouts using the appropriate method, such as
[`pauseExerciseAsync()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/ExerciseClient#pauseexerciseasync)
or
[`endExerciseAsync()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/ExerciseClient#endexerciseasync).

Use the state from `ExerciseUpdate` as the source of truth. The workout is not
considered paused when the call to `pauseExerciseAsync()` returns, but instead
when that state is reflected in the `ExerciseUpdate` message. This is especially
important to consider when it comes to UI states. If the user presses pause,
disable the pause button and call `pauseExerciseAsync()` on
Health Services. Wait for Health Services to reach the paused
state using `ExerciseUpdate.exerciseStateInfo.state`, and then switch the button
to resume. This is because Health Services state updates can take longer to
be delivered than the button press, so if you tie all UI changes to button
presses, the UI can get out of sync with the Health Services state.

Keep this in mind in the following situations:

- **Auto-pause is enabled:** the workout can pause or start without user interaction.
- **Another app starts a workout:** your workout might be terminated without user interaction.

If your app's workout is terminated by another app, your app must gracefully
handle the termination:

- Save the partial workout state so that a user's progress is not erased.
- Remove the Ongoing Activity icon and send the user a notification letting them know that their workout was ended by another app.

Also, handle the case where permissions are revoked during an
ongoing exercise. This is sent using the `isEnded` state, with an
[`ExerciseEndReason`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseStateInfo#endReason())
of `AUTO_END_PERMISSION_LOST`. Handle this case in a similar way to the
termination case: save the partial state, remove the Ongoing Activity
icon, and send a notification about what happened to the user.

The following example shows how to check for termination correctly:

    val callback = object : ExerciseUpdateCallback {
        override fun onExerciseUpdateReceived(update: ExerciseUpdate) {
            if (update.exerciseStateInfo.state.isEnded) {
                // Workout has either been ended by the user, or otherwise terminated
            }
            ...
        }
        ...
    }

## Manage active duration

During an exercise, an app can display the active duration of
the workout. The app, Health Services, and the device Micro Controller Unit
(MCU)---the low-power
processor responsible for exercise tracking---all need to be in sync, with
the same current active duration. To help manage this, Health Services sends an
`ActiveDurationCheckpoint` that provides an anchor point from which the app can
start its timer.

Because the active duration is sent from the MCU and can take a small amount of
time to arrive in the app, `ActiveDurationCheckpoint` contains two properties:

- `activeDuration`: how long the exercise has been active for
- `time`: when the active duration was calculated

Therefore, in the app the active duration of an exercise can be
calculated from `ActiveDurationCheckpoint` using the following equation:
> *(now() - checkpoint.time) + checkpoint.activeDuration*

This accounts for the small delta between active duration being calculated
on the MCU and arriving at the app. This can be used to seed a chronometer in
the app and help ensure the app's timer is perfectly aligned with the time
in Health Services and the MCU.

If the exercise is paused, the app waits to restart the timer in the UI
until the calculated time has gone past what the UI displays.
This is because the pause signal reaches Health Services and the MCU with a
slight delay. For example, if the app is paused at t=10 seconds, Health
Services might not deliver the `PAUSED` update to the app until t=10.2 seconds.

### Work with data from ExerciseClient

Metrics for the data types your app has registered for are delivered in
[`ExerciseUpdate`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseUpdate)
messages.

The processor delivers messages only when awake or when a maximum reporting
period is reached, such as every 150 seconds. Don't rely on the
`ExerciseUpdate` frequency to advance a chronometer with the
`activeDuration`. See the [Exercise sample](https://github.com/android/health-samples/tree/deprecated/health-services/ExerciseSample)
on GitHub for an example of how to implement an independent chronometer.

When a user starts a workout, `ExerciseUpdate` messages can be delivered
frequently, such as every second. As the user starts the workout, the screen
might turn off. Health Services can then deliver data less often, but still
sampled at the same frequency, to avoid waking the main processor. When the user
looks at the screen, any data in the process of being batched is immediately
delivered to your app.

### Control the batching rate

In some scenarios, you may want to control the frequency at which your app
receives certain data types while the screen is off. A
[`BatchingMode`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/BatchingMode)
object allows your app to override the default batching behavior to get data
deliveries more frequently.
| **Caution:** Health Services's default batching behavior is appropriate for most exercise cases. Because of the impact to battery performance, use `BatchingMode` only in scenarios where it is absolutely necessary. A blog post includes some possible [scenarios for which `BatchingMode` is
| appropriate](https://medium.com/androiddevelopers/wear-os-home-workouts-with-health-services-b9951fa9e0dc), including continuously streaming heart rate from the watch to display on the mobile device.

To configure the batching rate, complete the following steps:

1. Check whether the particular `BatchingMode` definition is supported by the device:

       // Confirm BatchingMode support to control heart rate stream to phone.
       suspend fun supportsHrWorkoutCompanionMode(): Boolean {
           val capabilities = exerciseClient.getCapabilities()
           return BatchingMode.HEART_RATE_5_SECONDS in
                   capabilities.supportedBatchingModeOverrides
       }

2. Specify that the `ExerciseConfig` object should use a particular
   `BatchingMode`, as shown in the following code snippet.

   | **Note:** Although you can include additional `DataType` objects as usual, they're only delivered as frequently as the default batching behavior.

       val config = ExerciseConfig(
           exerciseType = ExerciseType.WORKOUT,
           dataTypes = setOf(
               DataType.HEART_RATE_BPM,
               DataType.TOTAL_CALORIES
           ),
           // ...
           batchingModeOverrides = setOf(BatchingMode.HEART_RATE_5_SECONDS)
       )

3. Optionally, you can dynamically configure `BatchingMode` during the workout,
   instead of having a specific batching behavior persist throughout the duration
   of the workout:

       val desiredModes = setOf(BatchingMode.HEART_RATE_5_SECONDS)
       exerciseClient.overrideBatchingModesForActiveExercise(desiredModes)

4. To clear the customized `BatchingMode` and return to the default behavior,
   pass an empty set into
   `exerciseClient.overrideBatchingModesForActiveExercise()`.

### Timestamps

The point-in-time of each data point represents the duration since the device
booted. To convert this to a timestamp, do the following:

    val bootInstant =
        Instant.ofEpochMilli(System.currentTimeMillis() - SystemClock.elapsedRealtime())

This value can then be used with [`getStartInstant()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/IntervalDataPoint#getStartInstant(java.time.Instant))
or [`getEndInstant()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/IntervalDataPoint#getEndInstant(java.time.Instant))
for each data point.

#### Data accuracy

Some data types can have accuracy information associated with each data point.
This is represented in the [`accuracy`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/IntervalDataPoint#accuracy()) property.

`HrAccuracy` and `LocationAccuracy` classes can be populated for the
`HEART_RATE_BPM` and `LOCATION` data types, respectively. Where present, use the
`accuracy` property to determine whether each data point is of sufficient
accuracy for your application.

## Store and upload data

Use [Room](https://developer.android.com/jetpack/androidx/releases/room) to persist data delivered from Health
Services. Data upload happens at the end of the exercise using a mechanism
like [Work Manager](https://developer.android.com/jetpack/androidx/releases/work). This helps to verify
that network calls to upload data are deferred until the exercise is over,
minimizing power consumption during the exercise and simplifying the work.

## Integration checklist

Before publishing your app that uses Health Services' `ExerciseClient`, consult
the following checklist to verify your user experience avoids some common
issues. Confirm that:

- Your app [checks the capabilities](https://developer.android.com/training/wearables/health-services/active#capabilites) of the exercise type and the capabilities of the device each time the app runs. That way, you can detect when a particular device or exercise doesn't support one of the data types your app needs.
- You request and maintain the necessary permissions and specify these in your manifest file. Before calling `prepareExerciseAsync()`, your app confirms the runtime permissions are granted.
- Your app uses `getCurrentExerciseInfoAsync()` to handle [the cases where](https://developer.android.com/training/wearables/health-services/active#lifetime):
  - An exercise is already being tracked, and your app overrides the previous exercise.
  - Another app has terminated your exercise. This could happen when the user re-opens the app, they are met with a message explaining that the exercise stopped because another app took over.
- If you are using `LOCATION` data:
  - Your app maintains a `ForegroundService` with the corresponding `foregroundServiceType` throughout the duration of the exercise (including the prepare call).
  - Check that GPS is enabled on the device using `isProviderEnabled(LocationManager.GPS_PROVIDER)`, and prompts the user to open location settings if necessary.
  - For demanding use cases, where receiving location data with low latency is of great importance, consider integrating the [Fused
    Location Provider](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html) (FLP) and using its data as an initial location fix. When more stable location information is available from Health Services, use that instead of FLP.
- If your app requires data upload, any network calls to upload data are deferred until the exercise has ended. Otherwise, throughout the exercise, your app makes any necessary network calls sparingly.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Passive data updates](https://developer.android.com/training/wearables/health-services/passive)
- [Health Services on Wear OS](https://developer.android.com/training/wearables/health-services)
- [Get started with tiles](https://developer.android.com/training/wearables/tiles/get_started)