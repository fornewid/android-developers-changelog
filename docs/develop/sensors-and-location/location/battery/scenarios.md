---
title: https://developer.android.com/develop/sensors-and-location/location/battery/scenarios
url: https://developer.android.com/develop/sensors-and-location/location/battery/scenarios
source: md.txt
---

# Optimize location use for real-world scenarios

This section describes some typical location-gathering scenarios, along with recommendations for optimal use of the geofencing and fused location provider APIs.

## User visible or foreground updates

Example: A mapping app that needs frequent, accurate updates with very low latency. All updates happen in the foreground: the user starts an activity, consumes location data, and then stops the activity after a short time.

Use the[`setPriority()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setPriority(int))method with a value of[`PRIORITY_HIGH_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest#PRIORITY_HIGH_ACCURACY)or[`PRIORITY_BALANCED_POWER_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_BALANCED_POWER_ACCURACY).

The interval specified in the[`setInterval()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setInterval(long))method depends on the use case: for real time scenarios, set the value to few seconds; otherwise, limit to a few minutes (approximately two minutes or greater is recommended to minimize battery usage).

## Know the location of the device

Example: A weather app wants to know the device's location.

Use the[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())method, which returns the most recently available location (which in rare cases may be null). This method provides a straightforward way of getting location and doesn't incur costs associated with actively requesting location updates. Use in conjunction with the[`isLocationAvailable()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability.html#isLocationAvailable())method, which returns`true`when the location returned by[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())is reasonably up-to-date.

## Start updates when a user is at a specific location

Example: Requesting updates when a user is within a certain distance of work, home, or another location.

Use[geofencing](https://developer.android.com/training/location/geofencing)in conjunction with fused location provider updates. Request updates when the app receives a geofence entrance trigger, and remove updates when the app receives a geofence exit trigger. This ensures that the app gets more granular location updates only when the user has entered a defined area.

The typical workflow for this scenario could involve surfacing a notification upon the geofence enter transition, and launching an activity which contains code to request updates when the user taps the notification.

## Start updates based on the user's activity state

Example: Requesting updates only when the user is driving or riding a bike.

Use the[Activity Recognition API](https://developers.google.com/location-context/activity-recognition/)in conjunction with fused location provider updates. Request updates when the targeted activity is detected, and remove updates when the user stops performing that activity.

The typical workflow for this use case could involve surfacing a notification for the detected activity, and launching an activity which contains code to request updates when the user taps the notification.

## Long running background location updates tied to geographical areas

Example: The user wants to be notified when the device is within proximity of a retailer.

This is an excellent use case for geofencing. Because the use case almost certainly involves background location, use the[`addGeofences(GeofencingRequest, PendingIntent)`](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient#addGeofences(com.google.android.gms.location.GeofencingRequest,%20android.app.PendingIntent))method.

You should set the following configuration options:

- If you're tracking dwell transitions, use the[`setLoiteringDelay()`](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder.html#setLoiteringDelay(int))method passing a value of approximately five minutes or less.

- Use the[`setNotificationResponsiveness()`](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder.html#setNotificationResponsiveness(int)), passing a value of approximately five minutes. However, consider using a value of approximately ten minutes if your app can manage the extra delay in responsiveness.

An app may only register a maximum of 100 geofences at a time. In a use case where an app wants to track a large number of retailer options, the app may want to register large geofence (at the city level) and dynamically register smaller geofences (for locations within the city) for stores within the larger geofence. When a user enters a large geofence, add smaller geofences; when the user exits the larger geofence, remove the smaller geofences and re-register geofences for a new area.

## Long running background location updates without a visible app component

Example: An app that passively tracks location
| **Note:** Consider if you really need to collect location in the background, since this can lead to undesirable battery drain. Also, consider geofencing as an option, since geofencing APIs are optimized for performance.

Use the[`setPriority()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setPriority(int))method with the[`PRIORITY_NO_POWER`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_NO_POWER)option if possible because it incurs almost no battery drain. If using`PRIORITY_NO_POWER`isn't possible, use[`PRIORITY_BALANCED_POWER_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_BALANCED_POWER_ACCURACY)or[`PRIORITY_LOW_POWER`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_LOW_POWER), but avoid using[`PRIORITY_HIGH_ACCURACY`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_HIGH_ACCURACY)for sustained background work because this option substantially drains battery.

If you need more location data, use passive location by calling the[`setFastestInterval()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setFastestInterval(long))method passing a smaller value than what you pass to[`setInterval()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setInterval(long)). When combined with the[`PRIORITY_NO_POWER`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#PRIORITY_NO_POWER)option, passive location can opportunistically deliver location computed by other apps at no extra cost.

Moderate frequency by adding some latency, using the[`setMaxWaitTime()`](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.html#setMaxWaitTime(long))method. For example, if you use the`setinterval()`method with a value of approximately 10 minutes, you should consider calling`setMaxWaitTime()`with a value between 30 to 60 minutes. Using these options, location is computed for your app approximately every 10 minutes, but the app is only woken up every 30 to 60 minutes with some location data available as a batch update. This approach trades latency for more data available and better battery performance.

## Frequent high accuracy updates while the user interacts with other apps

Example: A navigation or fitness app that continues to work when the user either turns off the screen or opens a different app.

Use a foreground service. If expensive work is potentially going to be done by your app on behalf of the user, making the user aware of that work is a recommended best practice. A foreground service requires a persistent notification. For more information, see[Notifications Overview](https://developer.android.com/develop/ui/views/notifications).