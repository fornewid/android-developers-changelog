---
title: Use a local-only Wi-Fi hotspot  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/wifi/localonlyhotspot
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Use a local-only Wi-Fi hotspot Stay organized with collections Save and categorize content based on your preferences.




You can use a local-only hotspot to enable applications on devices connected to
the Wi-Fi hotspot to communicate with each other. The network created by this
method will not have Internet access. Each application can make a single request
for the hotspot, but multiple applications can request the hotspot at the same
time. When multiple applications have successfully registered concurrently, they
share the underlying hotspot.
[`LocalOnlyHotspotCallback.onStarted(LocalOnlyHotspotReservation)`](/reference/android/net/wifi/WifiManager.LocalOnlyHotspotCallback#onStarted(android.net.wifi.WifiManager.LocalOnlyHotspotReservation))
is called when the hotspot is ready for use.

If your app targets Android 13 (API level 33) or higher, you must request the
[`NEARBY_WIFI_DEVICES`](/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES)
to use a local-only hotspot, as shown in the following code snippet. Apps that
target an earlier version of Android must request `ACCESS_FINE_LOCATION`
instead.

```
<manifest ...>
    <<!-- If your app targets Android 13 (API level 33)
          or higher, you must declare the NEARBY_WIFI_DEVICES permission. -->
    <uses-permission android:name="android.permission.NEARBY_WIFI_DEVICES"
                     <!-- If your app derives location information from
                          Wi-Fi APIs, don't include the "usesPermissionFlags"
                          attribute. -->
                     android:usesPermissionFlags="neverForLocation" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
                     <!-- If any feature in your app relies on
                          precise location information, don't include the
                          "maxSdkVersion" attribute. -->
                     android:maxSdkVersion="32" />
    <application ...>
        ...
    </application>
</manifest>
```

For more details on using local-only hotspots, see
[`startLocalOnlyHotspot()`](/reference/android/net/wifi/WifiManager#startLocalOnlyHotspot(android.net.wifi.WifiManager.LocalOnlyHotspotCallback,%20android.os.Handler)).