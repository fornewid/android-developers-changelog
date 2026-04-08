---
title: Build a basic fitness app  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/fitness/basic-app/overview
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Fitness Guides](https://developer.android.com/health-and-fitness/fitness)

# Build a basic fitness app Stay organized with collections Save and categorize content based on your preferences.




**Note:** This guide uses `SensorManager` for retrieving steps data. We recommend
using the [Recording API on mobile](/health-and-fitness/guides/recording-api)
for recording steps in a power-efficient way.

This guide walks you through building a basic mobile step counter app, which
is a common foundation for many Health & Fitness apps.

This workflow integrates the following APIs:

* [SensorManager](/guide/topics/sensors/sensors_motion) for retrieving steps data from a mobile device.
* [Room](/training/data-storage/room) for local data storage.
* [Health Connect](/health-and-fitness/guides/health-connect) for storing and sharing health and fitness data on device.

For additional support on data reading and the tools necessary, refer to [Use
Android Sensor Manager to track steps from a mobile device](/health-and-fitness/guides/basic-fitness-app/read-step-count-data).

If you haven't already set up your development environment for using
[Health Connect](/health-and-fitness/guides/health-connect), follow these [getting started](/health-and-fitness/guides/health-connect/develop/get-started) steps.

## Request permissions on handheld device

Before getting exercise data you must request and be granted the appropriate
permissions.

As a best practice, only request the permissions you need, and make sure to
[request each permission in context](/training/permissions/requesting#workflow_for_requesting_permissions), instead of requesting all
permissions at once when the user starts the app.

The [step counter sensor](/guide/topics/sensors/sensors_motion#sensors-motion-stepcounter), which many exercise apps rely on, uses the
`ACTIVITY_RECOGNITION` permission. Add this permission in your
AndroidManifest.xml file:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  xmlns:tools="http://schemas.android.com/tools">

  <uses-permission android:name="android.permission.ACTIVITY_RECOGNITION"/>

</manifest>
```

To request the `ACTIVITY_RECOGNITION` permission at runtime refer to the
[permission request documentation](/training/permissions/requesting#request-permission).

You will also need to declare a `FOREGROUND_SERVICE` in the manifest. Since you
are requesting the `ACTIVITY_RECOGNITION` permission, declare
`FOREGROUND_SERVICE_TYPE_HEALTH`:

```
<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_HEALTH"/>
```

Visit [Foreground services](/develop/background-work/services/fgs)
to learn more about foreground services and foreground service types.

## Manage UI state using a ViewModel

To properly manage the UI state, use a ViewModel.
[Jetpack Compose and ViewModels](/jetpack/compose/libraries#viewmodel) offers you a more in-depth look at this
workflow.

Also, use UI layering, which is a critical part for building UIs with Compose
and lets you follow architecture best practices, such as
[Unidirectional Data Flow](/jetpack/compose/architecture#udf). To learn more about UI layering, refer to the
[UI layer documentation](/topic/architecture/ui-layer).

In this example app, the UI has three basic states:

* **Loading:** Shows a spinning circle.
* **Content:** Shows information about your steps for today.
* **Error:** Shows a message when something goes wrong.

The `ViewModel` exposes these states as a Kotlin `Flow`. Use a sealed class to
contain the classes and objects that represent the possible states:

```
class TodayScreenViewModel(...) {

  val currentScreenState: MutableStateFlow<TodayScreenState> = MutableStateFlow(Loading)

  [...]

}

sealed class TodayScreenState {
    data object Loading : TodayScreenState()
    data class Content(val steps: Long, val dailyGoal: Long) : TodayScreenState()
    data object Error: TodayScreenState()
}
```

Compose UI then collects this `Flow` as a Compose `State` and acts on it:

```
val state: TodayScreenState = todayScreenViewModel.currentScreenState.collectAsState().value
```