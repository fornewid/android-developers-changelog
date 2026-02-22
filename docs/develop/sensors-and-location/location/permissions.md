---
title: https://developer.android.com/develop/sensors-and-location/location/permissions
url: https://developer.android.com/develop/sensors-and-location/location/permissions
source: md.txt
---

To protect user privacy, apps that use location services must request location
permissions.

Multiple permissions are related to location. Which permissions you request,
and how you request them,
depend on the location requirements for your app's use case.

This page describes the different types of location requirements and explains
how to request location permissions in each case.

To request location permissions, follow the best practices for all
[runtime permissions](https://developer.android.com/training/permissions/requesting).

## Types of location access

Each permission has a combination of the following characteristics:

- **Category** : Either [foreground location](https://developer.android.com/develop/sensors-and-location/location/permissions#foreground) or [background location](https://developer.android.com/develop/sensors-and-location/location/permissions/background).
- **[Accuracy](https://developer.android.com/develop/sensors-and-location/location/permissions#accuracy)**: Either precise location or approximate location.

### Foreground location

If your app contains a feature that shares or receives location information only
once, or for a defined amount of time, then that feature requires foreground
location access. Some examples include the following:

- Within a navigation app, a feature allows users to get turn-by-turn directions.
- Within a messaging app, a feature allows users to share their current location with another user.

The system considers your app to be using foreground location if a feature of
your app accesses the device's current location in one of the following
situations:

- An activity that belongs to your app is visible.
- Your app is running a foreground service. When a foreground service is
  running, the system raises user awareness by showing a persistent
  notification. Your app retains access when it's placed in the background,
  such as when the user presses the **Home** button on their device or turns
  their device's display off.

  Additionally, you should declare a [foreground service type](https://developer.android.com/guide/topics/manifest/service-element#foregroundservicetype) of
  `location`, as shown in the following code snippet. On Android
  10 (API level 29) and higher, you must declare this foreground service type.  

      <!-- Recommended for Android 9 (API level 28) and lower. -->
      <!-- Required for Android 10 (API level 29) and higher. -->
      <service
          android:name="MyNavigationService"
          android:foregroundServiceType="location" ... >
          <!-- Any inner elements would go here. -->
      </service>

You declare a need for foreground location when your app requests either the
[`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) permission or the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission, as shown in the following snippet:  

    <manifest ... >
      <!-- Always include this permission -->
      <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

      <!-- Include only if your app benefits from precise location access. -->
      <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    </manifest>

| **Note:** Beginning with Android 12, your app can call [`getLocationPowerSaverMode()`](https://developer.android.com/reference/android/os/PowerManager#getLocationPowerSaveMode()) to check how the device's location features behave when Battery Saver is active. If this returns [`LOCATION_MODE_FOREGROUND_ONLY`](https://developer.android.com/reference/android/os/PowerManager#LOCATION_MODE_FOREGROUND_ONLY), your app will continue to receive location updates while in the foreground or running a foreground service when Battery Saver is on, even if the screen is off.

### Background location

An app requires background location access if a feature within the app
constantly shares location with other users or uses the [Geofencing API](https://developer.android.com/training/location/geofencing).
Several examples include the following:

- Within a family location sharing app, a feature allows users to continuously share location with family members.
- Within an IoT app, a feature allows users to configure their home devices such that they turn off when the user leaves their home and turn back on when the user returns home.

The system considers your app to be using background location if it accesses the
device's current location in any situation other than the ones described in the
[foreground location](https://developer.android.com/develop/sensors-and-location/location/permissions#foreground) section. The background location precision is the same
as the [foreground location precision](https://developer.android.com/develop/sensors-and-location/location/permissions#accuracy), which depends on the location
permissions that your app declares.

On Android 10 (API level 29) and higher, you must declare the
[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION) permission in your app's manifest in order to
[request background location access](https://developer.android.com/develop/sensors-and-location/location/permissions/background) at runtime. On earlier versions of
Android, when your app receives foreground location access, it automatically
receives background location access as well.  

    <manifest ... >
      <!-- Required only when requesting background location access on
           Android 10 (API level 29) and higher. -->
      <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
    </manifest>

| **Note:** The Google Play Store has a [location policy](https://support.google.com/googleplay/android-developer/answer/9799150) concerning device location, restricting background location access to apps that need it for their core features and meet related policy requirements.

### Accuracy

Android supports the following levels of location accuracy:

Approximate
:   Provides a device location estimate. If this location estimate is
    from the `LocationManagerService` or [`FusedLocationProvider`](https://developers.google.com/location-context/fused-location-provider), this
    estimate is accurate to within about 3 square kilometers (about 1.2 square
    miles). Your app can receive locations at this level of accuracy when you
    declare the `ACCESS_COARSE_LOCATION` permission but not the
    `ACCESS_FINE_LOCATION` permission.

Precise
:   Provides a device location estimate that is as accurate as possible.
    If the location estimate is from `LocationManagerService` or
    `FusedLocationProvider`, this estimate is usually within about 50 meters
    (160 feet) and is sometimes as accurate as within a few meters (10 feet) or
    better. Your app can receive locations at this level of accuracy when you
    declare the `ACCESS_FINE_LOCATION` permission.

If the [user grants the approximate location permission](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime#approximate-request), your app only has
access to approximate location, regardless of which location permissions your
app declares.

Your app should still work when the user grants only approximate location
access. If a feature in your app absolutely requires access to precise location
using the `ACCESS_FINE_LOCATION` permission, you can ask the user to [allow your
app to access precise location](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime#upgrade-to-precise).

### Reminder of background location grant

On Android 10 (API level 29) and higher, when a feature in your app accesses
device location in the background for the first time after the user grants
background location access, the system schedules a notification to send to the
user. This notification reminds the user that they've allowed your app to access
device location all the time. An example notification appears in figure 8.

## Check for location requirements in your app's SDK dependencies

Check whether your app uses any SDKs that depend on location permissions,
especially the `ACCESS_FINE_LOCATION` permission. Read the [Getting to know the
behaviors of your SDK dependencies](https://medium.com/androiddevelopers/getting-to-know-the-behaviors-of-your-sdk-dependencies-f3dfed07a311) blog post on Medium for
more.

## Additional resources

For more information about location permissions in Android, view the following
materials:

### Codelabs

- [Privacy best practices](https://developer.android.com/codelabs/android-privacy-codelab)

### Videos

- [How to find possible background location usage](https://www.youtube.com/watch?v=xTVeFJZQ28c)

### Samples

- [Sample app](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/permission) to demonstrate the use of location permissions.