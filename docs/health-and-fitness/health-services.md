---
title: https://developer.android.com/health-and-fitness/health-services
url: https://developer.android.com/health-and-fitness/health-services
source: md.txt
---

Wear OS 3 and higher includes a service called
[Health Services](https://developer.android.com/jetpack/androidx/releases/health).
Health Services acts as an intermediary to the various sensors and related
algorithms on the device to provide apps with high-quality data related to
activity, exercise, and health.

See the
[Health Services samples repository](https://github.com/android/health-samples/tree/main/health-services)
on GitHub for example fitness apps.

## How Health Services helps app developers

Without Health Services, apps must connect to one or multiple sensors,
configure each of them appropriately, receive raw sensor data, and use their
own algorithms to derive meaningful information. For example, an app might
register for updates of
[`Sensor.TYPE_PRESSURE`](https://developer.android.com/reference/kotlin/android/hardware/Sensor#type_pressure)
to get the current air pressure, use it to compute the current altitude, and
aggregate this data over time to show the elevation changes during a user's
activity session.

Health Services automatically configures all fitness and health
related sensors appropriately for the use-case, collects sensor data, and
computes metrics like heart rate, distance, calories, elevation, floors, speed,
pace, and more. Apps can register for this data directly from Health Services.
![Health Services architecture diagram](https://developer.android.com/static/wear/images/with_health_services.png) **Figure 1**: Health Services architecture

Some of the benefits of using Health Services include the following:

- Takes advantage of powerful algorithms running natively on the platform.
- Conserves battery by using sensor configurations from Health Services that are optimized for power efficiency.
- Future-proofs an app for Wear 3+ devices. The Health Services API is consistent across Wear 3+ devices, making it easier to keep your app up to date.
- Verifies data consistency across all applications on the same device by using standardized platform computations.
- Enables activity-aware experiences, including the ability to detect an ongoing exercise started from another app.

These benefits let developers focus on developing unique features and user
experiences, while relying on the platform to provide robust and consistent
metrics in a power-efficient manner.

## Health Services concepts

Keep the following concepts in mind when developing with Health Services.

### Data types

Health Services offers a variety of data collected and continuously updated
from all the available sources on the device. The data falls into two
broad categories: data sampled at a single point in time, such as
`HEART_RATE_BPM`, and data taken over a time interval, such as `DISTANCE`.

For more information, see the full list of [Data types](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/DataType).

### Events

Apps receive events when the user reaches a certain goal state or event. For
example, a user can register a distance goal within an exercise app, and then
the app notifies the user when they have run a certain distance.
Alternatively, use a passive goal for situations like the user hitting a
certain step count or falling asleep.

For more information, see [Exercise goals](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseGoal) and
[Passive goals](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/PassiveGoal).

### Exercise types

Health Services treats exercise as a core feature and supports a
multitude of exercise types, such as running or skiing. While an exercise is in
progress, Health Services can collect metrics on selected data types and report
back to the app that manages the exercise.

For more information, see the full list of [exercise types](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseType).

## Create apps using Health Services

Create apps using Health Services as described in the following
sections.

### Passive experiences

Using
[`PassiveMonitoringClient`](https://developer.android.com/reference/kotlin/androidx/health/services/client/PassiveMonitoringClient),
your app implements a `PassiveListenerService` that receives updates about a
data type or an event. This is suited for long-lived experiences where data
updates are relatively infrequent.

See [Passive data updates](https://developer.android.com/training/wearables/health-services/passive)
for more information.

### Active experiences

Using `MeasureClient`, your app registers listeners to receive rapid data
updates. This is suited for short-lived experiences, such as while the user
looks at your app UI. Try to minimize the time your app
spends with a registered listener, because it increases the sensor sampling rate
and thus increases power consumption. This API is not intended for background
capture or workout tracking.

See [Take spot health measurements with MeasureClient](https://developer.android.com/training/wearables/health-services/active-data/measure-client)
for more information.

Using `ExerciseClient`, your app can manage a user's workout, set exercise
goals, and listen for updates about the current exercise state. Your app can
also receive rapid data updates through this API, as long as the exercise
belongs to your app. `ExerciseClient` can be used for apps such as a running app
that lets users record their run, displays live metrics on their device, and
records data for further analysis.

See [Record an exercise with ExerciseClient](https://developer.android.com/training/wearables/health-services/active-data)
for more information.

### Test with synthetic data

To test that your app is receiving data updates from Health Services, manually
set your device to emit data as if a user were engaged in an exercise.

See [Use synthetic data with Health Services](https://developer.android.com/training/wearables/health-services/synthetic-data) for more
information.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Record an exercise with ExerciseClient](https://developer.android.com/training/wearables/health-services/active-data)
- [Take spot health measurements with MeasureClient](https://developer.android.com/training/wearables/health-services/active-data/measure-client)
- [Passive data updates](https://developer.android.com/training/wearables/health-services/passive)
- [Enhance app compatibility across Wear OS devices](https://developer.android.com/training/wearables/health-services/compatibility)