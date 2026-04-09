---
title: https://developer.android.com/health-and-fitness/health-services/permissions
url: https://developer.android.com/health-and-fitness/health-services/permissions
source: md.txt
---

Health Services on Wear OS uses the following distinct permissions:

- [`READ_HEART_RATE`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_HEART_RATE) for reading heart rate information.
- [`ACTIVITY_RECOGNITION`](https://developer.android.com/reference/android/Manifest.permission#ACTIVITY_RECOGNITION)
- [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
- [`BODY_SENSORS`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS) on Wear OS 5.1 (API level 35) and lower
- [`BODY_SENSORS_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS_BACKGROUND) between Wear OS 4 (API level 33) and Wear OS 5.1 (API level 35), inclusive

| **Note:** For apps that target Wear OS 6 Developer Preview (API level 36) or higher, any API previously requiring `BODY_SENSORS` or `BODY_SENSORS_BACKGROUND` requires the corresponding `android.permissions.health` permission. See the [migration steps](https://developer.android.com/health-and-fitness/health-services/permissions#migrate-support-api-36) section for more information.

Consult the following table to determine which permissions are necessary for
your app, based on the types of fitness data that you want to present to users.
Make sure to follow the basic principles for [requesting permissions](https://developer.android.com/training/permissions/requesting),
including asking for permissions in context.

If your app targets API level 36 or higher, and if it uses
[`PassiveMonitoringClient`](https://developer.android.com/reference/kotlin/androidx/health/services/client/PassiveMonitoringClient) to access body sensor information in the
background, request the [`READ_HEALTH_DATA_IN_BACKGROUND`](https://developer.android.com/reference/android/health/connect/HealthPermissions#READ_HEALTH_DATA_IN_BACKGROUND) permission.
If your app targets an API level between 33 and 35 inclusive, request both the
`BODY_SENSORS` and `BODY_SENSORS_BACKGROUND` permissions instead.
| **Note:** If you specify `isGpsEnabled = true` in your `ExerciseConfig`, Health Services also uses GNSS to improve the accuracy of metrics like distance, speed, and pace, but requires the user to grant the `ACCESS_FINE_LOCATION` permission to your app.

| Data type | Permission |
|---|---|
| [`CALORIES`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#CALORIES) [`CALORIES_DAILY`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#DISTANCE_DAILY) [`DISTANCE_DAILY`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#DISTANCE_DAILY) [`DECLINE_DISTANCE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#DECLINE_DISTANCE) [`DISTANCE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#DISTANCE) [`ELEVATION_GAIN`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#ELEVATION_GAIN) [`ELEVATION_LOSS`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#ELEVATION_LOSS) [`FLAT_GROUND_DISTANCE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#FLAT_GROUND_DISTANCE) [`FLOORS`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#FLOORS) [`FLOORS_DAILY`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#FLOORS_DAILY) [`GOLF_SHOT_COUNT`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#GOLF_SHOT_COUNT) [`INCLINE_DISTANCE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#INCLINE_DISTANCE) [`PACE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#PACE) [`REP_COUNT`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#REP_COUNT) [`RUNNING_STEPS`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#RUNNING_STEPS) [`SPEED`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#SPEED) [`STEPS`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#STEPS) [`STEPS_DAILY`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#STEPS_DAILY) [`STEPS_PER_MINUTE`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#STEPS_PER_MINUTE) [`SWIMMING_LAP_COUNT`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#SWIMMING_LAP_COUNT) [`SWIMMING_STROKES`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#SWIMMING_STROKES) [`CALORIES_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#CALORIES_TOTAL) [`WALKING_STEPS`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#WALKING_STEPS) [`UserActivityInfo`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/UserActivityInfo) [`UserActivityState`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/UserActivityState) | `ACTIVITY_RECOGNITION` |
| [`HEART_RATE_BPM`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#HEART_RATE_BPM) | `READ_HEART_RATE` |
| [`ABSOLUTE_ELEVATION`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#ABSOLUTE_ELEVATION) [`LOCATION`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType#LOCATION) | `ACCESS_FINE_LOCATION` |

## Migrate to support API level 36

If your app targets Wear OS 6 (API level 36) or higher, follow these steps
to migrate your app to supporting the latest versions of the Wear OS platform:

1. In your manifest file, add the `maxSdkVersion` for the legacy permission,
   as well as the modern `READ_HEART_RATE` permission:

       <uses-permission android:name="android.permission.BODY_SENSORS"
                        android:maxSdkVersion="35" />
       <uses-permission android:name="android.permission.health.READ_HEART_RATE" />

2. If your app requires access to body sensors while running in the background,
   add the `maxSdkVersion` for the legacy background permission, and add the
   modern `READ_HEALTH_DATA_IN_BACKGROUND` permission:

       <uses-permission android:name="android.permission.BODY_SENSORS_BACKGROUND"
                        android:maxSdkVersion="35" />
       <uses-permission android:name="android.permission.health.READ_HEALTH_DATA_IN_BACKGROUND" />

3. Request and confirm that the heart rate permission is granted everywhere your
   app checks for the `BODY_SENSOR` and `BODY_SENSORS_BACKGROUND` permission,
   filtering by Wear OS version. For example:

       if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA) {
           this.add(HealthPermissions.READ_HEART_RATE)
       }