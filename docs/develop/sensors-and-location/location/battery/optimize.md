---
title: https://developer.android.com/develop/sensors-and-location/location/battery/optimize
url: https://developer.android.com/develop/sensors-and-location/location/battery/optimize
source: md.txt
---

Take the following actions to [improve your app's
impact on a device's battery life](https://developer.android.com/develop/sensors-and-location/location/battery) when using location services.

## Remove location updates

A common source of unnecessary battery drain is the failure to remove location
updates when they are no longer needed.

This can happen when an activity's [`onStart()`](https://developer.android.com/reference/android/app/Activity#onStart()) or [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume())
lifecycle methods contain a call to [`requestlocationUpdates()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20android.app.PendingIntent)) without a
corresponding call to [`removeLocationUpdates()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#removeLocationUpdates(com.google.android.gms.location.LocationCallback)) in the [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) or
[`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()) lifecycle methods.

You can use lifecycle-aware components to better manage the lifecycle of the
activities in your app. For more information, see [Handling Lifecycles with
Lifecycle-Aware Components](https://developer.android.com/topic/libraries/architecture/lifecycle).

## Set timeouts

To guard against battery drain, set a reasonable timeout when location updates
should stop. The timeout ensures that updates don't continue indefinitely, and
it protects the app in scenarios where updates are requested but not removed
(for example, because of a bug in the code).

For a fused location provider request, add a timeout by calling
[`setDurationMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#setDurationMillis(long)), which receives a parameter that represents the
time in milliseconds since the method was last called. You can also use the
method to express the expiration time in terms of duration.

To add a timeout to a geofence location request, call the
[`setExpirationDuration()`](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder.html#setExpirationDuration(long)) method.

## Batch requests

For all non-foreground use cases, batch multiple requests together. Use the
[`setIntervalMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#setIntervalMillis(long)) method to specify the interval at which you would like
location to be computed. Then, use the [`setMaxUpdateDelayMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#setMaxUpdateDelayMillis(long)) method to set
the interval at which location is *delivered* to your app. Pass a value to the
`setMaxUpdateDelayMillis()` method that is a multiple of the value passed to the
`setIntervalMillis()` method. For example, consider the following location request:

### Kotlin

    val request = LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 10 * 60 * 1000)
    .setMaxUpdateDelayMillis(60 * 60 * 1000)
    .build()

### Java

    LocationRequest request = new LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 10 * 60 * 1000)
        .setMaxUpdateDelayMillis(60 * 60 * 1000)
        .build();

In this case, the system computes location roughly every ten minutes and
delivers approximately six location data points in a batch approximately every
hour. While you still get location updates every ten minutes or so, you conserve
battery because your device wakes up only every hour or so.

## Use passive location updates

In background use cases, it is a good idea to throttle location updates. Android
8.0 (API level 26) limits enforce this practice, but apps running on lower
devices should strive to limit background location as much as possible.

It is likely that while your app is in the background, another app may be
frequently requesting location updates in the foreground. Location services
makes these updates available to your app. Consider the following location
request, which opportunistically consumes location data:

### Kotlin

    val request = LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 15 * 60 * 1000)
    .setMinUpdateIntervalMillis(2 * 60 * 1000)
    .build()

### Java

    LocationRequest request = new LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 15 * 60 * 1000)
        .setMinUpdateIntervalMillis(2 * 60 * 1000)
        .build();

In the previous example, the app's location computes roughly every 15 minutes.
If other apps request location, the app receives the data at a maximum interval
of two minutes.

While consuming location passively incurs no battery drain, take extra care in
cases where the receipt of location data triggers expensive CPU or I/O
operations. To minimize battery costs, the interval specified in
[`setMinUpdateIntervalMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setmaxupdateagemillis-long-maxupdateagemillis(long)) shouldn't be too small.