---
title: https://developer.android.com/about/versions/oreo/background-location-limits
url: https://developer.android.com/about/versions/oreo/background-location-limits
source: md.txt
---

# Background Location Limits

In an effort to reduce power consumption, Android 8.0 (API level 26) limits how frequently an app can retrieve the user's current location while the app is[running in the background](https://developer.android.com/guide/background). Under these conditions, apps can receive location updates only a few times each hour.

**Note:** These limitations apply to all apps used on devices running Android 8.0 (API level 26) or higher,**regardless of an app's target SDK version**.

This location retrieval behavior is particularly important to keep in mind if your app relies on real-time alerts or motion detection while running in the background.

## Foreground app behavior is preserved

If an app is in the foreground on a device running Android 8.0 (API level 26), the location update behavior is the same as on Android 7.1.1 (API level 25) and lower.

**Warning:**If your app retrieves near real-time location updates over a long period of time, the device's battery life becomes significantly shorter.

## Tuning your app's location behavior

Consider whether your app's use cases for running in the background cannot succeed at all if your app receives infrequent location updates. If this is the case, you can retrieve location updates more frequently by performing one of the following actions:

- Bring your app to the foreground.
- Start a[foreground service](https://developer.android.com/guide/components/foreground-services)in your app by calling[startForegroundService()](https://developer.android.com/reference/android/content/Context#startForegroundService(android.content.Intent)). When such a foreground service is active, it appears as an ongoing notification in the[notification area](https://developer.android.com/guide/topics/ui/notifiers/notifications).

  **Caution:** If your app starts a foreground service while running in the background on a device that runs Android 11 (API level 30) or higher, your app cannot access location information unless the user has granted the[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)permission to your app. For more information, view the guidance about the[while-in-use restrictions](https://developer.android.com/guide/components/foreground-services#while-in-use-restrictions)that are associated with foreground services.
- Use elements of the Geofencing API, such as the[`GeofencingClient`](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient), which are optimized for minimizing power use.
- Use a passive location listener, which may receive faster location updates if there are foreground apps requesting location updates at a faster rate.

**Note:** If your app needs access to location history that contains time-frequent updates, use the batched version of the Fused Location Provider API elements, such as the[`FusedLocationProviderApi`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderApi)interface. When your app is running in the background, this API receives the user's location more frequently than the non-batched API. Keep in mind, however, that your app still receives updates in batches only a few times each hour.

## Affected APIs

The changes to location retrieval behavior in background apps affect the following APIs:

[Fused Location Provider (FLP)](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderApi)
:
    - If your app is running in the background, the location system service computes a new location for your app only a few times each hour. This is the case even when your app is requesting more frequent location updates.

      By using the[batched version](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest#setMaxWaitTime(long))of FLP, however, you have access to more time-frequent location history after your app receives a batch update, which also occurs only a few times each hour.
    - If your app is running in the foreground, there is no change in location sampling rates compared to Android 7.1.1 (API level 25).

Geofencing
:
    - Background apps can receive geofencing transition events more frequently than updates from the Fused Location Provider.
    - The average responsiveness for a geofencing event is every couple of minutes or so.

GNSS Measurements and GNSS Navigation Messages
:
    - When your app is in the background, callbacks that are registered to receive outputs from[GnssMeasurement](https://developer.android.com/reference/android/location/GnssMeasurement)and[GnssNavigationMessage](https://developer.android.com/reference/android/location/GnssNavigationMessage)stop executing.

Location Manager
:
    - Location updates are provided to background apps only a few times each hour.

      <br />

      **Note:** If your app is running on a device with Google Play services installed, it is highly recommended that you use the[Fused Location Provider (FLP)](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderApi)instead.

Wi-Fi Manager
:   The[startScan()](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan())method performs a full scan for background apps only a few times each hour. If a background app calls the method again soon afterward, the[WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager)class provides cached results from the previous scan.