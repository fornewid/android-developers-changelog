---
title: https://developer.android.com/develop/sensors-and-location/location/permissions/runtime
url: https://developer.android.com/develop/sensors-and-location/location/permissions/runtime
source: md.txt
---

When a feature in your app needs location access, wait until the user interacts
with the feature before making the permission request. This workflow follows the
best practice of asking for runtime permissions in context, as described in the
guide that explains how to [request app permissions](https://developer.android.com/training/permissions/requesting).

Figure 1 shows an example of how to perform this process. The app contains a
"share location" feature that requires foreground location access. The app
doesn't request the location permission, however, until the user selects the
**Share location** button.
![After the user selects the Share Location button, the
system's location permission dialog appears](https://developer.android.com/static/images/training/location/feature-requires-foreground.svg) **Figure 1.** Location-sharing feature that requires foreground location access. The feature is enabled if the user selects **Allow only while using the app**.

## User can grant only approximate location

On Android 12 (API level 31) or higher, users can request that your app retrieve
only approximate location information, even when your app requests the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) runtime permission.

To handle this potential user behavior, don't request the `ACCESS_FINE_LOCATION`
permission by itself. Instead, request both the `ACCESS_FINE_LOCATION`
permission and the [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) permission in a single runtime
request. If you try to request only `ACCESS_FINE_LOCATION`, the system ignores
the request on some releases of Android 12. If your app targets
Android 12 or higher, the system logs the following error message
in [Logcat](https://developer.android.com/studio/command-line/logcat):

    ACCESS_FINE_LOCATION must be requested with ACCESS_COARSE_LOCATION.

> [!NOTE]
> **Note:** To better respect user privacy, it's recommended that you only request `ACCESS_COARSE_LOCATION`. You can fulfill most use cases even when you have access to only approximate location information. [Figure 2](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime#fig-approximate-only) shows the user-facing dialog that appears when your app targets Android 12 and requests only `ACCESS_COARSE_LOCATION`.

<br />

When your app requests both `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION`,
the system permissions dialog includes the following options for the user:

- **Precise**: Allows your app to get precise location information.
- **Approximate**: Allows your app to get only approximate location information.

[Figure 3](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime#fig-approximate-full-prompt) shows that the dialog contains a visual cue for both options, to
help the user choose. After the user decides on a location accuracy, they tap
one of three buttons to select the duration of the permission grant.

On Android 12 and higher, users can navigate to system settings
to set the preferred location accuracy for any app, regardless of that app's
target SDK version. This is true even when your app is installed on a device
running Android 11 or lower, and then the user upgrades the
device to Android 12 or higher.

> [!CAUTION]
> **Caution:** If the user downgrades your app's location access from precise to approximate, either from the permission dialog or in system settings, the system restarts your app's process. For these reasons, it's especially important that you follow best practices for [requesting runtime permissions](https://developer.android.com/training/permissions/requesting).

![The dialog refers only to approximate location and
contains 3 buttons, one above the other](https://developer.android.com/static/images/training/location/approximate-only.svg) **Figure 2.** System permissions dialog that appears when your app requests `ACCESS_COARSE_LOCATION` only. ![The dialog has 2 sets of options, one above the other](https://developer.android.com/static/images/training/location/approximate-full-prompt.svg) **Figure 3.** System permissions dialog that appears when your app requests both `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` in a single runtime request.

<br />

### User choice affects permission grants

The following table shows the permissions that the system grants your app,
based on the options that the user chooses in the permissions runtime dialog:

<br />

|   | Precise | Approximate |
|---|---|---|
| **While using the app** | `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` | `ACCESS_COARSE_LOCATION` |
| **Only this time** | `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` | `ACCESS_COARSE_LOCATION` |
| **Deny** | No location permissions | No location permissions |

To determine which permissions the system has granted to your app, check the
return value of your permissions request. You can use Jetpack libraries in code
that's similar to the following, or you can use platform libraries, where you
[manage the permission request code yourself](https://developer.android.com/training/permissions/requesting#manage-request-code-yourself).


### Kotlin

```kotlin
@RequiresApi(Build.VERSION_CODES.N)
fun requestPermissions() {
    val locationPermissionRequest = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { permissions ->
        when {
            permissions.getOrDefault(Manifest.permission.ACCESS_FINE_LOCATION, false) -> {
                // Precise location access granted.
            }
            permissions.getOrDefault(Manifest.permission.ACCESS_COARSE_LOCATION, false) -> {
                // Only approximate location access granted.
            }
            else -> {
                // No location access granted.
            }
        }
    }

    // Before you perform the actual permission request, check whether your app
    // already has the permissions, and whether your app needs to show a permission
    // rationale dialog. For more details, see Request permissions:
    // https://developer.android.com/training/permissions/requesting#request-permission
    locationPermissionRequest.launch(
        arrayOf(
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
        )
    )
}
```

### Java

```java
private void requestPermissions() {

    ActivityResultLauncher<String[]> locationPermissionRequest =
            registerForActivityResult(new ActivityResultContracts
                            .RequestMultiplePermissions(), result -> {

                Boolean fineLocationGranted = null;
                Boolean coarseLocationGranted = null;

                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
                    fineLocationGranted = result.getOrDefault(
                            Manifest.permission.ACCESS_FINE_LOCATION, false);
                    coarseLocationGranted = result.getOrDefault(
                            Manifest.permission.ACCESS_COARSE_LOCATION,false);
                }

                if (fineLocationGranted != null && fineLocationGranted) {
                    // Precise location access granted.
                } else if (coarseLocationGranted != null && coarseLocationGranted) {
                    // Only approximate location access granted.
                } else {
                    // No location access granted.
                }
            }
        );

    // ...

    // Before you perform the actual permission request, check whether your app
    // already has the permissions, and whether your app needs to show a permission
    // rationale dialog. For more details, see Request permissions.
    locationPermissionRequest.launch(new String[] {
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
    });
}
```

<br />

### Request an upgrade to precise location

You can ask the user to upgrade your app's access from approximate location to
precise location. Before you ask the user to upgrade your app's access to
precise location, however, consider whether your app's use case absolutely
requires this level of precision. If your app needs to pair a device with nearby
devices over Bluetooth or Wi-Fi, consider using [companion device pairing](https://developer.android.com/guide/topics/connectivity/companion-device-pairing)
or [Bluetooth permissions](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions), instead of requesting the `ACCESS_FINE_LOCATION`
permission.

To request that the user upgrade your app's location access from approximate to
precise, do the following:

1. If necessary, [explain why your app needs the permission](https://developer.android.com/training/permissions/requesting#explain).
2. Request the `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` permissions together again. Because the user has already allowed the system to grant approximate location to your app, the system dialog is different this time, as shown in figure 4 and figure 5:

![The dialog contains the options 'Change to precise
location', 'Only this time', and 'Deny'.](https://developer.android.com/static/images/training/location/upgrade-to-precise-while-using-the-app.svg) **Figure 4.** The user previously selected **Approximate** and **While using the app** (in the dialog from figure 3). ![The dialog contains the options 'Only this time' and
'Deny'.](https://developer.android.com/static/images/training/location/upgrade-to-precise-only-this-time.svg) **Figure 5.** The user previously selected **Approximate** and **Only this time** (in the dialog from figure 3).

<br />

## Request only foreground location initially

Even if several features in your app require location access, it's likely that
only some of them require background location access. Therefore, it's
recommended that your app performs *incremental requests* for location
permissions, asking for foreground location access and then background location
access. By performing incremental requests, you give users more control and
transparency because they can better understand which features in your app need
background location access.

> [!CAUTION]
> **Caution:** If your app targets Android 11 (API level 30) or higher, the system enforces this best practice. If you request a foreground location permission and the background location permission at the same time, the system ignores the request and doesn't grant your app either permission.

Figure 6 shows an example of an app that's designed to handle incremental
requests. Both the "show current location" and "recommend nearby places"
features require foreground location access. Only the "recommend nearby places"
feature, however, requires background location access.
![The button that enables foreground location access is
positioned half a screen length away from the button that enables background
location](https://developer.android.com/static/images/training/location/incremental-permission-request.svg) **Figure 6.** Both features require location access, but only the "recommend nearby features" feature requires background location access.

The process for performing incremental requests is as follows:

1. At first, your app should guide users to the features that require
   foreground location access, such as the "share location" feature in Figure 1
   or the "show current location" feature in Figure 2.

   It's recommended that you disable user access to features that require
   background location access until your app has foreground location access.
2. At a later time, when the user explores features that require
   background location access, you can [request background
   location](https://developer.android.com/develop/sensors-and-location/location/permissions/background) access.

## Additional resources

For more information about location permissions in Android, view the following
materials:

### Codelabs

- [Privacy best practices](https://developer.android.com/codelabs/android-privacy-codelab)

### Videos

- [How to find possible background location usage](https://www.youtube.com/watch?v=xTVeFJZQ28c)

### Samples

- [Sample app](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/permission) to demonstrate the use of location permissions.