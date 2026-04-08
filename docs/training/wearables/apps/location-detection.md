---
title: https://developer.android.com/training/wearables/apps/location-detection
url: https://developer.android.com/training/wearables/apps/location-detection
source: md.txt
---

A watch's small, glanceable form factor makes Wear OS an ideal platform for apps
that record, report, and respond to user location. As examples, you can build
apps that give users real-time updates on their distance, speed, and direction,
or provide glanceable cues about users' surroundings.

For more information, see [Build location-aware apps](https://developer.android.com/training/location).

Some watches have a built-in GPS sensor that retrieves location data without
requiring a connected phone. When you request location data in a watch app, the
system retrieves the location from either the phone or the watch using the most
power-efficient method. Therefore, even without a GPS sensor in the watch, you
can still get location information.

To reduce the effect of location data acquisition on battery life, call
[`setPriority()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#setPriority(int)) with the value [`PRIORITY_BALANCED_POWER_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#PRIORITY_BALANCED_POWER_ACCURACY).
Different priority settings may [optimize chips differently](https://developer.android.com/guide/topics/location/battery#accuracy).

When possible, conserve battery by asking for location no more than once per
minute using [`setInterval()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setintervalmillis-long-intervalmillis).

As described in later sections, your app needs to [handle the loss of location
data](https://developer.android.com/training/wearables/apps/location-detection#notFound) when a watch without a sensor becomes disconnected from a phone.

## Choose your method

There are two ways to provide location data to a Wear OS app. You can use the
[Fused Location Provider (FLP)](https://developer.android.com/training/wearables/apps/location-detection#fused) or [Wear Health Services (WHS)](https://developer.android.com/training/wearables/health-services). FLP is a
Google Play services API.

Use FLP in the following circumstances:

- You want location data in the moment but not continuously, such as marking the location of a parked car.
- You want location continuously but don't need the location history.

Use WHS in the following circumstances:

- You want data from other sensors or are likely to want data from other sensors in the future.
- Your app is a workout or exercise app that needs to track location data over the course of a specific time interval.

> [!NOTE]
> **Note:** WHS is recommended for all workout tracking because it is more power efficient.

## Use the Fused Location Provider

On a watch, get location data using the [`FusedLocationProviderClient`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient). The
FLP may use location data from the phone. For more information, see [Create
location services client](https://developer.android.com/training/location/retrieve-current#play-services).

For information about requesting location updates and continuously tracking a
user's location, see [Request location updates](https://developer.android.com/training/location/request-updates).

> [!NOTE]
> **Note:** When creating a `LocationRequest`, consider batching using the [`setMaxWaitTime()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest#public-locationrequest-setmaxwaittime-long-millis) because it can consume less battery and provide a more accurate location, depending on the device's hardware capabilities.

## Detect on-board GPS

If a user goes jogging with a watch that lacks a built-in GPS sensor and leaves
the paired phone behind, your watch app can't get location data through the
connected device. Detect this situation in your app and warn the user that
location capabilities are unavailable.

To determine whether a watch has a built-in GPS sensor, call the
[`hasSystemFeature()`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)) method with
[`PackageManager.FEATURE_LOCATION_GPS`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LOCATION_GPS). The following code detects whether
the watch has a built-in GPS sensor when you start an activity:


```kotlin
class LocationActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // ...
    }
    fun hasGps(): Boolean =
        packageManager.hasSystemFeature(PackageManager.FEATURE_LOCATION_GPS)
}
```

<br />

## Handle disconnection events

If a watch has no built-in GPS sensor and loses connection to a phone, the watch
loses its location data stream. If your app expects a constant stream of data,
your app must detect the loss of a connection, warn the user, and gracefully
degrade in functionality.

As with a mobile device, when you request location updates using
[`FusedLocationProviderClient.requestLocationUpdates()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20android.app.PendingIntent)), you pass in either
a [`LocationCallback`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback#public-void-onlocationavailability-locationavailability-locationavailability) or a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent). Both of these include the
location information and the [`LocationAvailability`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability) status.

When using the `LocationCallback` option, override
[`onLocationAvailability()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback#public-void-onlocationavailability-locationavailability-locationavailability) to receive updates regarding location
availability status.

When using the `PendingIntent` option and an [`Intent`](https://developer.android.com/reference/android/content/Intent) is returned, extract
the location availability status from the `Intent` using the
[`LocationAvailability.extractLocationAvailability(Intent)`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability#extractLocationAvailability(android.content.Intent)) method.

## Handle location not found

When the GPS signal is lost, you can retrieve the last known location of the
user's watch. Retrieving the last known location is helpful when you can't get a
GPS fix and when the watch lacks built-in GPS and loses its connection with the
phone. For more information, see [Get the last known location](https://developer.android.com/training/location/retrieve-current).

## Flush location with batched calls

If you are using batched calls, call [`flushLocations()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#public-taskvoid-flushlocations) when the screen
comes back on or returns from ambient mode to immediately return any batched
locations to all registered `LocationListeners`, `LocationCallbacks`, and
`Pending Intents`.

## Testing considerations

Simulate location and other sensor data using the Wear OS emulator's extended
controls. For more information, see [Simulating sensors](https://developer.android.com/training/wearables/get-started/emulator#simulating-sensors).

## Recommended for you

- [Optimize location for battery](https://developer.android.com/develop/sensors-and-location/location/battery)
- [Create a notification](https://developer.android.com/develop/ui/views/notifications/build-notification)
- [Detect when users start or end an activity](https://developer.android.com/develop/sensors-and-location/location/transitions)