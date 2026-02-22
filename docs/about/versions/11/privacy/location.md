---
title: https://developer.android.com/about/versions/11/privacy/location
url: https://developer.android.com/about/versions/11/privacy/location
source: md.txt
---

To further protect user privacy, Android 11 adds one-time
location access and changes how users grant background location access. These
updates affect all apps that run on Android 11 and higher.

## One-time access

![](https://developer.android.com/static/images/about/versions/11/one-time-perm-prompt.svg) **Figure 1.** System dialog for the foreground location permission includes an option called **Only this time**.

On Android 11 and higher, whenever your app requests access to
[foreground location](https://developer.android.com/training/location/permissions#foreground), the system
permissions dialog includes an option called **Only this time**, as shown in
figure 1. This option give users more control over when an app can access
location information.

Learn more about how the system handles [one-time
permissions](https://developer.android.com/guide/topics/permissions/overview#one-time).

## Background location access

Android 11 changes how a feature in your app can gain access to
[background location](https://developer.android.com/training/location/permissions#background). This section
describes each of these changes.

If a feature in your app accesses location from the background, verify that such
access is necessary. Consider getting the information that the feature needs in
other ways, as described on the page about how to [access
location in the background](https://developer.android.com/training/location/background).

### Request background location separately

As described in the guide on how to [request location access at
runtime](https://developer.android.com/training/location/permissions#request-location-access-runtime), you
should perform incremental location requests. If your app targets
Android 11 or higher, the system enforces this best practice. If
you request a foreground location permission and the background location
permission at the same time, the system ignores the request and doesn't grant
your app either permission.

### Permission dialog changes

### Change details

**Change Name** : `BACKGROUND_RATIONALE_CHANGE_ID`

**Change ID** : `147316723`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:  

    adb shell am compat enable (<var translate="no">147316723</var>|<var translate="no">BACKGROUND_RATIONALE_CHANGE_ID</var>) <var translate="no">PACKAGE_NAME</var>
    adb shell am compat disable (<var translate="no">147316723</var>|<var translate="no">BACKGROUND_RATIONALE_CHANGE_ID</var>) <var translate="no">PACKAGE_NAME</var>

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

When a feature in your app requests background location on a device that runs
Android 11 or higher, the system dialog doesn't include a button
to enable background location access. In order to enable background location
access, users must set the **Allow all the time** option for your app's location
permission on a settings page, as described in the guide on how to [Request
background location](https://developer.android.com/training/location/permissions#request-background-location).

### Additional resources

For more information about accessing background location, view the following
materials:

#### Videos

- [How to find possible background location
  usage](https://www.youtube.com/watch?v=xTVeFJZQ28c)