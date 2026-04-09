---
title: https://developer.android.com/develop/connectivity/bluetooth/bt-permissions
url: https://developer.android.com/develop/connectivity/bluetooth/bt-permissions
source: md.txt
---

To use Bluetooth features in your app, you must [declare several
permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions#declare). You should also [specify whether your app requires
support](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions#features) for Bluetooth classic or Bluetooth Low Energy (BLE). If your
app doesn't require Bluetooth classic or BLE but can still benefit from these
technologies, you can [check for availability at runtime](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions#availability).

## Declare permissions

The set of permissions that you declare in your app depends on your app's target
SDK version.

### Target Android 12 or higher

**Note:** On Android 8.0 (API level 26) and higher, the
[Companion
Device Manager (CDM)](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) provides a more streamlined method of connecting to
companion devices, compared to the permissions described in this section. The
CDM system provides a pairing UI on behalf of your app and doesn't require
location permissions.

If you want more control over the pairing and connecting experience, use
the permissions described in this section.
![Bluetooth permissions dialog](https://developer.android.com/static/images/develop/connectivity/bluetooth/nearby-devices.svg) System permissions dialog, asking the user to grant an app permission to discover, advertise, and connect to nearby devices.

If your app targets Android 12 (API level 31) or higher, declare the following
permissions in your app's manifest file:

1. If your app [looks for Bluetooth
   devices](https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices), such as BLE peripherals, declare the [`BLUETOOTH_SCAN`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN) permission.
2. If your app [makes the current device discoverable to other Bluetooth
   devices](https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices#enable-discoverability), declare the [`BLUETOOTH_ADVERTISE`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE) permission.
3. If your app [communicates with already-paired Bluetooth
   devices](https://developer.android.com/develop/connectivity/bluetooth/transfer-data), declare the [`BLUETOOTH_CONNECT`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT) permission.
4. For your legacy Bluetooth-related permission declarations, set `android:maxSdkVersion` to 30. This app compatibility step helps the system grant your app only the Bluetooth permissions that it needs when installed on devices that run Android 12 or higher.
5. If your app uses Bluetooth scan results to derive physical location, declare the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission. Otherwise, you can [strongly assert that your app doesn't derive
   physical location](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions#assert-never-for-location) and set `android:maxSdkVersion` to 30 for the `ACCESS_FINE_LOCATION` permission.

The `BLUETOOTH_ADVERTISE`, `BLUETOOTH_CONNECT`, and `BLUETOOTH_SCAN` permissions
are [runtime permissions](https://developer.android.com/develop/permissions/overview#runtime).
Therefore, you must explicitly [request user
approval](https://developer.android.com/training/permissions/requesting) in your app before you can look for
Bluetooth devices, make a device discoverable to other devices, or communicate
with already-paired Bluetooth devices. When your app requests at least one of
these permissions, the system prompts the user to allow your app to access
**Nearby devices**, as shown in figure 1.

The following code snippet demonstrates how to declare Bluetooth-related
permissions in your app if it targets Android 12 or higher:

    <manifest>
        <!-- Request legacy Bluetooth permissions on older devices. -->
        <uses-permission android:name="android.permission.BLUETOOTH"
                         android:maxSdkVersion="30" />
        <uses-permission android:name="android.permission.BLUETOOTH_ADMIN"
                         android:maxSdkVersion="30" />

        <!-- Needed only if your app looks for Bluetooth devices.
             If your app doesn't use Bluetooth scan results to derive physical
             location information, you can
             <a href="#assert-never-for-location">strongly assert that your app
             doesn't derive physical location</a>. -->
        <uses-permission android:name="android.permission.BLUETOOTH_SCAN" />

        <!-- Needed only if your app makes the device discoverable to Bluetooth
             devices. -->
        <uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE" />

        <!-- Needed only if your app communicates with already-paired Bluetooth
             devices. -->
        <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />

        <!-- Needed only if your app uses Bluetooth scan results to derive
             physical location. -->
        <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
        ...
    </manifest>

#### Strongly assert that your app doesn't derive physical location

If your app doesn't use Bluetooth scan results to derive physical location, you
can make a strong assertion that your app never uses the Bluetooth permissions
to derive physical location. To do so, complete the following steps:

1. Add the `android:usesPermissionFlags` attribute to your `BLUETOOTH_SCAN`
   permission declaration, and set this attribute's value to `neverForLocation`.

   > [!NOTE]
   > **Note:** If you include `neverForLocation` in your `android:usesPermissionFlags`, some BLE beacons are filtered from the scan results.

2. If location isn't otherwise needed for your app, remove the
   `ACCESS_FINE_LOCATION` permission from your app's manifest.

The following code snippet shows how to update your app's manifest file:

    <manifest>
        <!-- Include "neverForLocation" only if you can strongly assert that
             your app never derives physical location from Bluetooth scan results. -->
        <uses-permission android:name="android.permission.BLUETOOTH_SCAN"
                         android:usesPermissionFlags="neverForLocation" />

        <!-- Set maxSdkVersion to 30 if you can strongly assert that, on
             Android 12 and higher, your app never derives physical location from
             Bluetooth scan results and doesn't need location access for any other
             purpose. -->
        <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
                         android:maxSdkVersion="30" />
        ...
    </manifest>

### Target Android 11 or lower

If your app targets Android 11 (API level 30) or lower, declare the following
permissions in your app's manifest file:

- [`BLUETOOTH`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH) is necessary to perform any Bluetooth classic or BLE communication, such as requesting a connection, accepting a connection, and transferring data.
- [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) is necessary because, on Android 11 and lower, a Bluetooth scan could potentially be used to gather information about the location of the user.

> [!NOTE]
> **Note:** On devices that run Android 8.0 or higher, you can use the [`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager) to perform a scan of nearby companion devices on behalf of your app without requiring the location permission. For more on this option, see [Companion
> device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing).

Because location permissions are [runtime permissions](https://developer.android.com/guide/topics/permissions/overview#runtime),
you must [request these permissions at runtime](https://developer.android.com/training/permissions/requesting)
along with declaring them in your manifest.

## Discover local Bluetooth devices

If you want your app to initiate device discovery or manipulate Bluetooth
settings, you must declare the
[`BLUETOOTH_ADMIN`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADMIN)
permission. Most apps need this permission solely for the ability to discover
local Bluetooth devices. Don't use the other abilities granted by this
permission unless the app is a "power manager" that modifies Bluetooth settings
upon user request. Declare the permission in your app manifest file. For
example:

    <manifest>
    ...
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    ...
    </manifest>

If your app supports a service and can run on Android 10 (API level 29) or
Android 11, you must also declare the
[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)
permission to discover Bluetooth devices. For more information on this
requirement, see [Access location in the
background](https://developer.android.com/training/location/background).

The following code snippet shows how to declare the `ACCESS_BACKGROUND_LOCATION`
permission:

    <manifest>
    ...
    <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
    ...
    </manifest>

See the [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
reference for more information about declaring app permissions.

## Specify Bluetooth feature usage

If Bluetooth is a critical piece of your app, you can add flags to your manifest
file indicating this requirement. The
[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) element allows
you to specify the type of hardware your app uses and whether or not it is
required.

This example shows how to indicate that Bluetooth classic is required for your
app.

    <uses-feature android:name="android.hardware.bluetooth" android:required="true"/>

If your app relies on Bluetooth Low Energy, you can use the following:

    <uses-feature android:name="android.hardware.bluetooth_le" android:required="true"/>

If you say the feature is required for your app, then the Google Play store will
hide your app from users on devices lacking those features. For this reason, you
should only set the required attribute to `true` if your app can't work without
the feature.

## Check feature availability at runtime

To make your app available to devices that don't support Bluetooth classic or
BLE, you should still include the `<uses-feature>` element in your app's
manifest, but set `required="false"`. Then, at run-time, you can determine
feature availability by using
[`PackageManager.hasSystemFeature()`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)):

### Kotlin

```kotlin
// Check to see if the Bluetooth classic feature is available.
val bluetoothAvailable = packageManager.hasSystemFeature(PackageManager.FEATURE_BLUETOOTH)

// Check to see if the BLE feature is available.
val bluetoothLEAvailable = packageManager.hasSystemFeature(PackageManager.FEATURE_BLUETOOTH_LE)
```

### Java

```java
// Use this check to determine whether Bluetooth classic is supported on the device.
// Then you can selectively disable BLE-related features.
boolean bluetoothAvailable = getPackageManager().hasSystemFeature(PackageManager.FEATURE_BLUETOOTH);

// Use this check to determine whether BLE is supported on the device. Then
// you can selectively disable BLE-related features.
boolean bluetoothLEAvailable = getPackageManager().hasSystemFeature(PackageManager.FEATURE_BLUETOOTH_LE);
```