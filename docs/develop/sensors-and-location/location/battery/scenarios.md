---
title: https://developer.android.com/develop/sensors-and-location/location/battery/scenarios
url: https://developer.android.com/develop/sensors-and-location/location/battery/scenarios
source: md.txt
---

This section describes some typical location-gathering scenarios, along with
recommendations for optimal use of the geofencing and fused location provider
APIs.

## User visible or foreground updates

Example: A mapping app that needs frequent, accurate updates with very low
latency. All updates happen in the foreground: the user starts an activity,
consumes location data, and then stops the activity after a short time.

Use the [`setPriority()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setpriority-int-priority) method with a value of
[`PRIORITY_HIGH_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_high_accuracy) or [`PRIORITY_BALANCED_POWER_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_balanced_power_accuracy).

The interval specified in the [`setIntervalMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setintervalmillis-long-intervalmillis) method depends on the
use case: for real time scenarios, set the value to few seconds; otherwise,
limit to a few minutes (approximately two minutes or greater is recommended to
minimize battery usage).

## Know the location of the device

Example: A weather app wants to know the device's location.

Use the [`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#public-abstract-tasklocation-getlastlocation) method, which returns the most recently
available location (which in rare cases may be null). This method provides a
straightforward way of getting location and doesn't incur costs associated with
actively requesting location updates. Use in conjunction with the
[`isLocationAvailable()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability#public-boolean-islocationavailable) method, which returns `true` when the location
returned by [`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#public-abstract-tasklocation-getlastlocation) is reasonably up-to-date.

## Start updates when a user is at a specific location

Example: Requesting updates when a user is within a certain distance of work,
home, or another location.

Use [geofencing](https://developer.android.com/develop/sensors-and-location/location/geofencing) in conjunction with fused location provider updates.
Request updates when the app receives a geofence entrance trigger, and remove
updates when the app receives a geofence exit trigger. This ensures that the app
gets more granular location updates only when the user has entered a defined
area.

The typical workflow for this scenario could involve surfacing a notification
upon the geofence enter transition, and launching an activity which contains
code to request updates when the user taps the notification.

## Start updates based on the user's activity state

Example: Requesting updates only when the user is driving or riding a bike.

Use the [Activity Recognition API](https://developers.google.com/location-context/activity-recognition/) in conjunction with fused location
provider updates. Request updates when the targeted activity is detected, and
remove updates when the user stops performing that activity.

The typical workflow for this use case could involve surfacing a notification
for the detected activity, and launching an activity which contains code to
request updates when the user taps the notification.

## Long running background location updates tied to geographical areas

Example: The user wants to be notified when the device is within proximity of a
retailer.

This is an excellent use case for geofencing. Because the use case almost
certainly involves background location, use the
[`addGeofences(GeofencingRequest, PendingIntent)`](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient#public-abstract-taskvoid-addgeofences-geofencingrequest-request,-pendingintent-pendingintent) method.

You should set the following configuration options:

- If you're tracking dwell transitions, use the [`setLoiteringDelay()`](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder#public-geofence.builder-setloiteringdelay-int-loiteringdelayms)
  method passing a value of approximately five minutes or less.

- Use the [`setNotificationResponsiveness()`](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder#public-geofence.builder-setnotificationresponsiveness-int-notificationresponsivenessms), passing a value of
  approximately five minutes. However, consider using a value of approximately
  ten minutes if your app can manage the extra delay in responsiveness.

An app may only register a maximum of 100 geofences at a time. In a use case
where an app wants to track a large number of retailer options, the app may want
to register large geofence (at the city level) and dynamically register smaller
geofences (for locations within the city) for stores within the larger geofence.
When a user enters a large geofence, add smaller geofences; when the user exits
the larger geofence, remove the smaller geofences and re-register geofences for
a new area.

## Long running background location updates without a visible app component

Example: An app that passively tracks location

> [!NOTE]
> **Note:** Consider if you really need to collect location in the background, since this can lead to undesirable battery drain. Also, consider geofencing as an option, since geofencing APIs are optimized for performance.

Use the [`setPriority()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setpriority-int-priority) method with the [`PRIORITY_PASSIVE`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_passive) option if
possible because it incurs almost no battery drain. If using `PRIORITY_PASSIVE`
isn't possible, use [`PRIORITY_BALANCED_POWER_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_balanced_power_accuracy) or
[`PRIORITY_LOW_POWER`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_low_power), but avoid using [`PRIORITY_HIGH_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_high_accuracy) for
sustained background work because this option substantially drains battery.

If you need more location data, use passive location by calling the
[`setMinUpdateIntervalMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setminupdateintervalmillis-long-minupdateintervalmillis) method passing a smaller value than what
you pass to [`setIntervalMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setintervalmillis-long-intervalmillis). When combined with the
[`PRIORITY_PASSIVE`](https://developers.google.com/android/reference/com/google/android/gms/location/Priority#public-static-final-int-priority_passive) option, passive location can opportunistically deliver
location computed by other apps at no extra cost.

Moderate frequency by adding some latency, using the
[`setMaxUpdateDelayMillis()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setmaxupdatedelaymillis-long-maxupdatedelaymillis) method. For example, if you use the
`setIntervalMillis()` method with a value of approximately 10 minutes, you
should consider calling `setMaxUpdateDelayMillis()` with a value between 30 to
60 minutes. Using these options, location is computed for your app
approximately every 10 minutes, but the app is only woken up every 30 to 60
minutes with some location data available as a batch update. This approach
trades latency for more data available and better battery performance.

## Frequent high accuracy updates while the user interacts with other apps

Example: A navigation or fitness app that continues to work when the user either
turns off the screen or opens a different app.

Use a foreground service. If expensive work is potentially going to be done by
your app on behalf of the user, making the user aware of that work is a
recommended best practice. A foreground service requires a persistent
notification. For more information, see [Notifications Overview](https://developer.android.com/develop/ui/views/notifications).