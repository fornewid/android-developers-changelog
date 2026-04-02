---
title: https://developer.android.com/develop/sensors-and-location/location/permissions/background
url: https://developer.android.com/develop/sensors-and-location/location/permissions/background
source: md.txt
---

This page discusses the following:

- How to request background location access.
- How to handle the request based on your app's target SDK version.
- How user preferences for approximate location affect how your app gets background location.

> [!NOTE]
> **Note:** If a feature in your app accesses location from the background, verify that access is necessary. Consider getting the information that the feature needs in other ways. To learn more about background location access, see the [Access location in the background](https://developer.android.com/training/location/background) page.

![](https://developer.android.com/static/images/training/location/request-device-location-background-11.svg) **Figure 7.** Settings page includes an option called **Allow all the time**, which grants background location access.

## Permission dialog contents depend on target SDK version

When a feature in your app requests background location on a device that runs
Android 10 (API level 29), the system permissions dialog includes an option
named **Allow all the time**. If the user selects this option, the feature in
your app gains background location access.

On Android 11 (API level 30) and higher, however, the system dialog doesn't
include the **Allow all the time** option. Instead, users must enable background
location on a settings page, as shown in figure 7.

You can help users navigate to this settings page by following best practices
when requesting the background location permission. The process for granting the
permission depends on your app's target SDK version.

### App targets Android 11 or higher

If your app hasn't been granted the `ACCESS_BACKGROUND_LOCATION` permission, and
[`shouldShowRequestPermissionRationale()`](https://developer.android.com/reference/androidx/core/app/ActivityCompat#shouldShowRequestPermissionRationale(android.app.Activity,%20java.lang.String)) returns `true`, show an
educational UI to users that includes the following:

- A clear explanation of why your app's feature needs access to background location.
- The user-visible label of the settings option that grants background location (for example, **Allow all the time** in figure 7). You can call [`getBackgroundPermissionOptionLabel()`](https://developer.android.com/reference/android/content/pm/PackageManager#getBackgroundPermissionOptionLabel()) to get this label. The return value of this method is localized to the user's device language preference.
- An option for users to decline the permission. If users decline background location access, they should be able to continue using your app.

![Users can tap the system notification to change location
settings for an app](https://developer.android.com/static/images/training/location/location-access-reminder.svg) **Figure 8.**Notification reminding the user that they've granted background location access to an app.

### App targets Android 10 or lower

When a feature in your app requests background location access, users see a
system dialog. This dialog includes an option to navigate to your app's location
permission options on a settings page.

As long as your app already follows best practices for requesting location
permissions, you don't need to make any changes to support this behavior.

## User can affect background location accuracy

If the [user requests approximate location](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime#approximate-request), the user's choices in the
location permissions dialog also apply to background location. In other words,
if the user grants your app the `ACCESS_BACKGROUND_LOCATION` permission but
grants only approximate location access in the foreground, your app has only
approximate location access in the background as well.

## Additional resources

For more information about location permissions in Android, view the following
materials:

### Codelabs

- [Privacy best practices](https://developer.android.com/codelabs/android-privacy-codelab)

### Videos

- [How to find possible background location usage](https://www.youtube.com/watch?v=xTVeFJZQ28c)

### Samples

- [Sample app](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/permission) to demonstrate the use of location permissions.