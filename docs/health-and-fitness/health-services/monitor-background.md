---
title: https://developer.android.com/health-and-fitness/health-services/monitor-background
url: https://developer.android.com/health-and-fitness/health-services/monitor-background
source: md.txt
---

Passive data updates are suited for apps that need to monitor Health Services
data in the background. They are intended for use cases that span hours, days,
or even longer. If you need to store or process health and fitness data when
your app isn't running and the user is not explicitly engaged in an exercise,
use Health Service's passive client.

For examples of passive data usage, see the
[Passive Data](https://github.com/android/health-samples/tree/main/health-services/PassiveDataCompose)
and
[Passive Goals](https://github.com/android/health-samples/tree/main/health-services/PassiveGoalsCompose)
samples on GitHub.

## Add dependencies

To add a dependency on Health Services, you must add the Google Maven repository
to your project. For more information, see
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven).

In your module-level `build.gradle` file, add the following dependency:

### Groovy

```groovy
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-rc01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-rc01")
}
```

## Check capabilities

Before registering for data updates, check that the device can provide the type
of data your app needs. Checking capabilities lets you enable or disable
certain features or modify your app's UI to compensate for features that are
not available.

    val healthClient = HealthServices.getClient(this /*context*/)
    val passiveMonitoringClient = healthClient.passiveMonitoringClient
    lifecycleScope.launchWhenCreated {
        val capabilities = passiveMonitoringClient.capabilities.await()
        // Supported types for passive data collection
        supportsHeartRate =
            DataType.HEART_RATE_BPM in capabilities.supportedDataTypesPassiveMonitoring
        // Supported types for PassiveGoals
        supportsStepsGoal =
            DataType.STEPS_DAILY in capabilities.supportedDataTypesPassiveGoals
    }

## Register for passive data

You can receive passive data through a service, a callback, or both. A
service lets your app receive data in the background when no part of your
app is visible in the foreground. When you receive data in the background, it is
delivered in batches. The callback receives data at a slightly faster rate, but
only while the app is running and the callback is successfully notified.

Whichever method you use, first create a `PassiveListenerConfig`
that determines which data types to receive, as shown in the following example:

    val passiveListenerConfig = PassiveListenerConfig.builder()
        .setDataTypes(setOf(DataType.HEART_RATE_BPM))
        .build()

To receive data using a callback, define and register the callback, as shown in
the following example:

    val passiveListenerCallback: PassiveListenerCallback = object : PassiveListenerCallback {
        override fun onNewDataPointsReceived(dataPoints: DataPointContainer) {
            // TODO: Do something with dataPoints
        }
    }

    passiveMonitoringClient.setPassiveListenerCallback(
        passiveListenerConfig,
        passiveListenerCallback
    )

    // To remove the listener
    passiveMonitoringClient.clearPassiveListenerCallbackAsync()

Using a service is similar, but instead of creating a class derived from
`PassiveListenerCallback`, derive from `PassiveListenerService`, as shown in
the following example:

    class PassiveDataService : PassiveListenerService() {
        override fun onNewDataPointsReceived(dataPoints: DataPointContainer) {
            // TODO: Do something with dataPoints
        }
    }

    passiveMonitoringClient.setPassiveListenerServiceAsync(
        PassiveDataService::class.java,
        passiveListenerConfig
    )

Next, declare the service in your `AndroidManifest.xml` file. Require a Health
Services permission, which verifies that only Health Services is able to bind
to the service:

    <service android:name=".PassiveDataService"
        android:permission="com.google.android.wearable.healthservices.permission.PASSIVE_DATA_BINDING"
        android:exported="true" />

### Interpret time

The data you receive from Health Services is batched, so you may receive data
points of different types, or multiple data points of the same type, in the same
batch. Use the timestamps included within these objects rather than the time
they were received by your app to determine the correct ordering of events.

Obtain timestamps for each `DataPoint` by first calculating the boot timestamp,
as shown in the following example:

    val bootInstant =
        Instant.ofEpochMilli(System.currentTimeMillis() - SystemClock.elapsedRealtime())

This value can then be passed to
[`getStartInstant()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/IntervalDataPoint#getstartinstant)
or
[`getEndInstant()`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/IntervalDataPoint#getendinstant).

## Restore registrations after boot

Passive data registrations don't persist across reboots. To receive data after a
device is restarted, re-create your registrations using a `BroadcastReceiver`
that listens for the [`ACTION_BOOT_COMPLETED`](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED)
system broadcast.

In the receiver, don't attempt to restore the registrations directly. Instead,
delegate this functionality to a `WorkManager` worker. When the
device is starting up, Health Services might take 10 seconds or more to
acknowledge a passive data registration request, and this might exceed the
allowable execution time of a `BroadcastReceiver`. In contrast, `WorkManager`
workers have a [10-minute execution limit](https://developer.android.com/reference/kotlin/androidx/work/WorkManager).

The following snippet shows what a `BroadcastReceiver` might look like:

    class StartupReceiver : BroadcastReceiver() {

       override fun onReceive(context: Context, intent: Intent) {
           if (intent.action != Intent.ACTION_BOOT_COMPLETED) return


           // TODO: Check permissions first
           WorkManager.getInstance(context).enqueue(
               OneTimeWorkRequestBuilder<RegisterForPassiveDataWorker>().build()
           )
       }
    }

    class RegisterForPassiveDataWorker(
       private val appContext: Context,
       workerParams: WorkerParameters
    ) : Worker(appContext, workerParams) {

       override fun doWork(): Result {
           runBlocking {
               HealthServices.getClient(appContext)
                    .passiveMonitoringClient
                    .setPassiveListenerCallback(...)
           }
           return Result.success()
       }
    }

To arrange for the system to execute this code when the device boots up, make
two changes to the `AndroidManifest.xml` file.

First, add the following permission as a child of `<manifest>`:

    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />

Second, add the following receiver intent filter as a child of `<application>`:

    <receiver
        android:name=".StartupReceiver"
        android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.BOOT_COMPLETED" />
        </intent-filter>
    </receiver>

## Activity state

The passive client can also provide high-level information on user state, such
as whether the user is sleeping. To receive these updates, follow these steps:

1. Request the `ACTIVITY_RECOGNITION` permission.
2. Call `setShouldUserActivityInfoBeRequested(true)` in the `PassiveListenerConfig` builder.

Override the `onUserActivityInfoReceived()` method in your callback or service
and make use of the returned `UserActivityInfo`, as shown in the following
example:

    override fun onUserActivityInfoReceived(info: UserActivityInfo) {
        val stateChangeTime: Instant = info.stateChangeTime // may be in the past!
        val userActivityState: UserActivityState = info.userActivityState
        if (userActivityState == UserActivityState.USER_ACTIVITY_ASLEEP) {
            // ...
        }
    }

## Passive goals

You can configure a passive client to notify the app when passive goals
are reached, such as the user completing 10,000 steps in a day.

To do this, create a goal, as shown in the following example:

    val dailyStepsGoal by lazy {
        val condition = DataTypeCondition(
            dataType = DataType.STEPS_DAILY,
            threshold = 10_000, // Trigger every 10000 steps
            comparisonType = ComparisonType.GREATER_THAN_OR_EQUAL
        )
        PassiveGoal(condition)
    }

Add this goal to your `PassiveListenerConfig`, as shown in the following
example:

    val passiveListenerConfig = PassiveListenerConfig.builder()
        .setDailyGoals(setOf(dailyStepsGoal))
        .build()

Override the `onGoalCompleted()` method in your callback or service
and make use of the returned `PassiveGoal`, as shown in the following example:

    override fun onGoalCompleted(goal: PassiveGoal) {
        when (goal.dataTypeCondition.dataType) {
            DataType.STEPS_DAILY -> {
                // ...
            }
        }
    }

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Active data and exercises](https://developer.android.com/training/wearables/health-services/active)
- [Get started with tiles](https://developer.android.com/training/wearables/tiles/get_started)
- [Add a splash screen](https://developer.android.com/training/wearables/apps/splash-screen)