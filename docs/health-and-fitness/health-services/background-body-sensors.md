---
title: Request background access to body sensor data  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-services/background-body-sensors
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Fitness Guides](https://developer.android.com/health-and-fitness/fitness)

# Request background access to body sensor data Stay organized with collections Save and categorize content based on your preferences.



Android 13 and Wear OS 4 introduce a way for apps to access body sensors, such
as heart rate, from the background. This new access model is similar to the one
that introduced [background location access in Android 10 (API level 29)](/training/location/permissions#request-background-location).

If your app needs to access body sensor information in background, such as when
[monitoring Health Services data in the background](/health-and-fitness/guides/health-services/monitor-background), you must request the
[`BODY_SENSORS_BACKGROUND`](/reference/android/Manifest.permission#BODY_SENSORS_BACKGROUND) permission.

**Note:** `BODY_SENSORS_BACKGROUND` is a restricted permission which cannot be held
by your app until the installer adds your app to an allowlist, or until the user
lets your app have the permission.

As described on the [privacy best practices](/privacy/best-practices) page, apps should only ask for
the `BODY_SENSORS_BACKGROUND` permission when it is critical to the user-facing
feature, and they should properly disclose this to users.

The process for granting the permission depends on your app's target SDK
version.

## App targets Android 13 or higher

In addition to the existing [`BODY_SENSORS`](/reference/android/Manifest.permission#BODY_SENSORS) permission, declare the
`BODY_SENSORS_BACKGROUND` permission in your manifest file:

```
<uses-permission android:name="android.permission.BODY_SENSORS">
<uses-permission android:name="android.permission.BODY_SENSORS_BACKGROUND">
```

Then, your app must [request](/training/permissions/requesting) the permissions in separate operations:

1. Check if `BODY_SENSORS` is granted. If not, request the permission.
2. Check if `BODY_SENSORS_BACKGROUND` is granted. If not, request the
   permission.

![The all-the-time option is the first list item on the settings screen](/static/training/wearables/images/system-sensors.svg)


**Figure 1.** Sensors setting includes an option called **All the
time**, which grants background sensor data access.

**Caution:** If your app requests both body sensor permissions at the
same time, the system ignores the request and doesn't grant your app either
permission.

On Android 13 (API level 33) and higher, the runtime permission dialog doesn't
include the "Allow all the time" option. Instead, users must enable all-the-time
background sensor access from system settings, as shown in figure 1. When you
request the `BODY_SENSORS_BACKGROUND` permission after granting the
`BODY_SENSORS` permission, you can help users navigate to this settings page. If
users decline all-the-time access, they should be able to continue using your
app.

## App targets an earlier version

![The link text is 'go to settings'](/static/training/wearables/images/go-to-system-settings.svg)


**Figure 2.** Permission dialog includes a link to navigate users to
the app's sensor permissions in system settings.

When your app targets a version of Android earlier than Android 13, background
access isn't granted automatically when you request the `BODY_SENSORS`
permission. Instead, users see a system dialog that invites users to navigate to
your app's sensor permission settings, as shown in figure 2. Then, users must
enable background sensor usage on that settings page.

Users can decline the background access. It has the same effect as revoking the
`BODY_SENSORS` permission while your app is running in the background. When an
app is using [`PassiveMonitoringClient`](/reference/kotlin/androidx/health/services/client/PassiveMonitoringClient) without background access permission
and goes into the background, the app loses the `BODY_SENSORS` permission, and
the [`onPermissionLost()`](/reference/kotlin/androidx/health/services/client/PassiveListenerService#onPermissionLost()) callback is called. For these reasons, it's
especially important that you follow best practices for requesting runtime
permissions.