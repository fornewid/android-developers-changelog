---
title: https://developer.android.com/about/versions/10/privacy/changes
url: https://developer.android.com/about/versions/10/privacy/changes
source: md.txt
---

Android 10 (API level 29) introduces a number of features and behavior changes
to better protect users' privacy. These changes extend the transparency and
control that users have over their data and the capabilities they give to apps.
These features might mean that specific behaviors or data that your app is
depending on may behave differently compared to older versions of the platform.
The impacts on your app should be minimal if your app is following current best
practices for handling user data.

This page lists a summary of each change.

> [!NOTE]
> **Note:** In addition to the changes listed on this page, Android 10 introduces other features and changes that affect aspects of the platform other than privacy. To learn more, see the [Features \& APIs](https://developer.android.com/about/versions/10/features) page, the [changes for all apps](https://developer.android.com/about/versions/10/behavior-changes-all) page, and the [changes for apps targeting API
> level 29](https://developer.android.com/about/versions/10/behavior-changes-10) page.

## Top changes

This section includes the key changes in Android 10 related to
privacy.

### External storage access scoped to app files and media

By default, apps targeting Android 10 and higher are given
[scoped
access into external storage](https://developer.android.com/training/data-storage/files/external-scoped), or
*scoped storage*. Such apps can see the following types of files within an
external storage device without needing to request any storage-related user
permissions:

- Files in the app-specific directory, accessed using [`getExternalFilesDir()`](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)).
- Photos, videos, and audio clips that the app created from the [media
  store](https://developer.android.com/training/data-storage/files/media).

To learn more about scoped storage, as well as how to share, access, and modify
files that are saved on external storage devices, see the guides on how to
[manage files in external storage](https://developer.android.com/training/data-storage/files/external) and
[access and modify media files](https://developer.android.com/training/data-storage/files/media).

### Access to device location in the background requires permission

To support the additional control that users have over an app's access to
location information, Android 10 introduces the
[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)
permission.

Unlike the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
and
[`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)
permissions, the `ACCESS_BACKGROUND_LOCATION` permission only affects an app's
access to location when it runs in the background. An app is considered to be
accessing location in the background unless one of the following conditions is
satisfied:

- An activity belonging to the app is visible.
- The app is running a foreground service that has declared a [foreground
  service type](https://developer.android.com/guide/topics/manifest/service-element#foregroundservicetype) of
  `location`.

  To declare the foreground service type for a service in your app, set your
  app's `targetSdkVersion` or `compileSdkVersion` to `29` or higher. Learn
  more about how foreground services can [continue user-initiated
  actions](https://developer.android.com/training/location/receive-location-updates#continue-user-initiated-action)
  that require access to location.

If your app [creates and monitors geofences](https://developer.android.com/training/location/geofencing) and
targets Android 10 (API level 29) or higher, you must declare the
`ACCESS_BACKGROUND_LOCATION` permission.

#### Access granted automatically when targeting Android 9 or lower

If your app runs on Android 10 or higher but targets Android 9
(API level 28) or lower, the platform applies the following behavior:

- If your app declares a [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) element for either [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) or [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION), the system automatically adds a `<uses-permission>` element for `ACCESS_BACKGROUND_LOCATION` during installation.
- If your app requests either `ACCESS_FINE_LOCATION` or `ACCESS_COARSE_LOCATION`, the system automatically adds `ACCESS_BACKGROUND_LOCATION` to the request.

#### Access when device is upgraded to Android 10

If a user grants your app access to device location -- either
[`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)
or
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
-- then upgrades their device from Android 9 to Android 10,
the system automatically updates the set of location-based permissions granted
to your app. The set of permissions that your app receives after the upgrade
depends on its target SDK version and its defined permissions, as shown in
the following table:

**Table 1.** Changes in location permission state
after device upgrade to Android 10

| Target platform version | Coarse or fine permission granted? | Background permission defined in manifest? | Updated default permission state |
|---|---|---|---|
| Android 10 | Yes | Yes | Foreground and background access |
| Android 10 | Yes | No | Foreground access only |
| Android 10 | No | (Ignored by system) | No access |
| Android 9 or lower | Yes | Automatically added by the system at device upgrade time | Foreground and background access |
| Android 9 or lower | No | (Ignored by system) | No access |

Note that the user can change this level of access even after the system
automatically updates your app's access to device location. For example, the
user might reduce your app's access to foreground only or revoke access
entirely. Before attempting to access the device's location, particularly within
a foreground service, your app should check whether the user still allows your
app to receive this location information.

#### Access revoked when updating target API level on Android 10 devices

Consider the case where your app is already installed on a device that runs
Android 10. If you update your app to target
Android 10 in this situation, the device revokes the
`ACCESS_BACKGROUND_LOCATION` permission.

For more information on how to retrieve the device's location while your app is
in the background, see the guide on [receiving periodic location
updates](https://developer.android.com/training/location/receive-location-updates).

### Restrictions on starting activities from the background

Starting in Android 10, the system places [restrictions on
starting activities from the
background](https://developer.android.com/guide/components/activities/background-starts). This behavior
change helps minimize interruptions for the user and keeps the user more in
control of what's shown on their screen. As long as your app starts activities
as a direct result of user interaction, your app most likely isn't affected by
these restrictions.

To learn more about the recommended alternative to starting activities from the
background, see the guide on how to [alert users of time-sensitive
events](https://developer.android.com/training/notify-user/time-sensitive) in your app.

## Identifiers and data

This section lists changes specific to working with device identifiers and data.

### Removal of contacts affinity

Starting in Android 10, the platform doesn't keep track of
contacts affinity information. As a result, if your app conducts a search on the
user's contacts, the results aren't ordered by frequency of interaction.

The guide about `ContactsProvider` contains a notice describing the specific
[fields and methods that are
obsolete](https://developer.android.com/guide/topics/providers/contacts-provider#ObsoleteData) on all devices
starting in Android 10.

### MAC address randomization

On devices that run Android 10 or higher, the system transmits
randomized MAC addresses by default.

If your app handles an [enterprise use
case](https://developers.google.com/android/work/), the platform provides
APIs for several operations related to MAC addresses:

- **Obtain randomized MAC address:** Device owner apps and profile owner apps can retrieve the randomized MAC address assigned to a specific network by calling [`getRandomizedMacAddress()`](https://developer.android.com/reference/android/net/wifi/WifiConfiguration#getRandomizedMacAddress()).
- **Obtain actual, factory MAC address:** Device owner apps can retrieve a device's actual hardware MAC address by calling [`getWifiMacAddress()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getWifiMacAddress(android.content.ComponentName)). This method is useful for tracking fleets of devices.

### Restriction on access to /proc/net filesystem

On devices that run Android 10 or higher, apps cannot access
`/proc/net`, which includes information about a device's network state. Apps
that need access to this information, such as VPNs, should use the
[`NetworkStatsManager`](https://developer.android.com/reference/android/app/usage/NetworkStatsManager) or
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) class.

### Restriction on non-resettable device identifiers

Starting in Android 10, apps must have the
`READ_PRIVILEGED_PHONE_STATE` privileged permission in order to access the
device's non-resettable identifiers, which include both IMEI and serial number.

> [!CAUTION]
> **Caution:** Third-party apps installed from the Google Play Store cannot declare privileged permissions.

Affected methods include the following:

- `Build`
  - [`getSerial()`](https://developer.android.com/reference/android/os/Build#getSerial())
- `TelephonyManager`
  - [`getImei()`](https://developer.android.com/reference/android/telephony/TelephonyManager#getImei(int))
  - [`getDeviceId()`](https://developer.android.com/reference/android/telephony/TelephonyManager#getDeviceId(int))
  - [`getMeid()`](https://developer.android.com/reference/android/telephony/TelephonyManager#getMeid(int))
  - [`getSimSerialNumber()`](https://developer.android.com/reference/android/telephony/TelephonyManager#getSimSerialNumber())
  - [`getSubscriberId()`](https://developer.android.com/reference/android/telephony/TelephonyManager#getSubscriberId())

If your app doesn't have the permission and you try asking for information about
non-resettable identifiers anyway, the platform's response varies based on
target SDK version:

- If your app targets Android 10 or higher, a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException) occurs.
- If your app targets Android 9 (API level 28) or lower, the method returns `null` or placeholder data if the app has the [`READ_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE) permission. Otherwise, a `SecurityException` occurs.

> [!NOTE]
> **Note:** If your app is the [device or profile owner
> app](https://developers.google.com/android/work/overview#android_devices_enterprise_use_cases), you need only the [`READ_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE) permission to access non-resettable device identifiers, even if your app targets Android 10 or higher. Also, if your app has [special carrier
> permissions](https://source.android.com/devices/tech/config/uicc), you don't need any permissions to access the identifiers.

Many use cases don't need non-resettable device identifiers. For example, if
your app uses non-resettable device identifiers for ad-tracking or user
analytics purposes, [use an Android Advertising
ID](https://developer.android.com/training/permissions/usage-notes#d_create_a_unique_identifier_for_advertising_or_user_analytics)
for those specific use cases instead. To learn more, see [best practices for
unique identifiers](https://developer.android.com/training/articles/user-data-ids).

### Limited access to clipboard data

Unless your app is the default [input method editor
(IME)](https://developer.android.com/guide/topics/text/creating-input-method) or is the app that currently
has focus, your app cannot access clipboard data on Android 10 or
higher.

### Protection of USB device serial number

If your app targets Android 10 or higher, your app cannot read
the serial number until the user has granted your app permission to access the
USB device or accessory.

To learn more about working with USB devices, see the guide on how to [configure
USB hosts](https://developer.android.com/guide/topics/connectivity/usb/host).

## Camera and connectivity

This section lists changes specific to camera metadata and connectivity APIs.

### Restriction on access to camera details and metadata

Android 10 changes the breadth of information that the
[`getCameraCharacteristics()`](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics(java.lang.String))
method returns by default. In particular, your app must have the
[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) permission in order to
access potentially device-specific metadata that is included in this method's
return value.

To learn more about these changes, see the section about [camera fields that
require permission](https://developer.android.com/guide/topics/media/camera#permission-camera-fields).

### Restriction on enabling and disabling Wi-Fi

Apps targeting Android 10 or higher cannot enable or disable
Wi-Fi. The
[`WifiManager.setWifiEnabled()`](https://developer.android.com/reference/android/net/wifi/WifiManager#setWifiEnabled(boolean))
method always returns `false`.

If you need to prompt users to enable and disable Wi-Fi, use a [settings
panel](https://developer.android.com/about/versions/10/features#settings-panels).

### Restrictions on direct access to configured Wi-Fi networks

To protect user privacy, manual configuration of the list of Wi-Fi networks is
restricted to system apps and
[device policy controllers (DPCs)](https://developer.android.com/work/dpc/build-dpc). A given DPC can be
either the device owner or the profile owner.

If your app targets Android 10 or higher, and it isn't a system
app or a DPC, then the following methods don't return useful data:

- The
  [`getConfiguredNetworks()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getConfiguredNetworks())
  method always returns an empty list.

  > [!NOTE]
  > **Note:** If a carrier app calls `getConfiguredNetworks()`, the system returns a list containing only the networks that the carrier configured.

- Each network operation method that returns an integer
  value---[`addNetwork()`](https://developer.android.com/reference/android/net/wifi/WifiManager#addNetwork(android.net.wifi.WifiConfiguration))
  and
  [`updateNetwork()`](https://developer.android.com/reference/android/net/wifi/WifiManager#updateNetwork(android.net.wifi.WifiConfiguration))---always
  returns -1.

- Each network operation that returns a boolean
  value---[`removeNetwork()`](https://developer.android.com/reference/android/net/wifi/WifiManager#removeNetwork(int)),
  [`reassociate()`](https://developer.android.com/reference/android/net/wifi/WifiManager#reassociate()),
  [`enableNetwork()`](https://developer.android.com/reference/android/net/wifi/WifiManager#enableNetwork(int,%20boolean)),
  [`disableNetwork()`](https://developer.android.com/reference/android/net/wifi/WifiManager#disableNetwork(int)),
  [`reconnect()`](https://developer.android.com/reference/android/net/wifi/WifiManager#reconnect()),
  and
  [`disconnect()`](https://developer.android.com/reference/android/net/wifi/WifiManager#disconnect())---always
  returns `false`.

If your app needs to connect to Wi-Fi networks, use the following alternative
methods:

- To trigger an instant local connection to a Wi-Fi network, use [`WifiNetworkSpecifier`](https://developer.android.com/reference/android/net/wifi/WifiNetworkSpecifier) in a standard [`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest) object.
- To add Wi-Fi networks for consideration for providing internet access to the user, work with [`WifiNetworkSuggestion`](https://developer.android.com/reference/android/net/wifi/WifiNetworkSuggestion) objects. You can add and remove networks that appear in the auto-connect network selection dialog by calling [`addNetworkSuggestions()`](https://developer.android.com/reference/android/net/wifi/WifiManager#addNetworkSuggestions(java.util.List%3Candroid.net.wifi.WifiNetworkSuggestion%3E)) and [`removeNetworkSuggestions()`](https://developer.android.com/reference/android/net/wifi/WifiManager#removeNetworkSuggestions(java.util.List%3Candroid.net.wifi.WifiNetworkSuggestion%3E)), respectively. These methods don't require any location permissions.

### Some telephony, Bluetooth, Wi-Fi APIs require FINE location permission

If your app targets Android 10 or higher, it must have the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission in order to use several methods within the Wi-Fi, Wi-Fi Aware,
or Bluetooth APIs. The following sections list the affected classes and methods.

> [!NOTE]
> **Note:** If your app runs on Android 10 or higher but targets Android 9 (API level 28) or lower, you can use the affected APIs (except for [`WifiP2pManager`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager) APIs) as long as your app has declared either the [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) or the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission.

#### Telephony

- [`TelephonyManager`](https://developer.android.com/reference/android/telephony/TelephonyManager)
  - `getCellLocation()`
  - `getAllCellInfo()`
  - `requestNetworkScan()`
  - `requestCellInfoUpdate()`
  - `getAvailableNetworks()`
  - `getServiceState()`
- [`TelephonyScanManager`](https://developer.android.com/reference/android/telephony/TelephonyScanManager)
  - `requestNetworkScan()`
- [`TelephonyScanManager.NetworkScanCallback`](https://developer.android.com/reference/android/telephony/TelephonyScanManager.NetworkScanCallback)
  - `onResults()`
- [`PhoneStateListener`](https://developer.android.com/reference/android/telephony/PhoneStateListener)
  - `onCellLocationChanged()`
  - `onCellInfoChanged()`
  - `onServiceStateChanged()`

#### Wi-Fi

- [`WifiManager`](https://developer.android.com/reference/android/net/wifi/WifiManager)
  - `startScan()`
  - `getScanResults()`
  - `getConnectionInfo()`
  - `getConfiguredNetworks()`
- [`WifiAwareManager`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager)
- [`WifiP2pManager`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager)
- [`WifiRttManager`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager)

#### Bluetooth

- [`BluetoothAdapter`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter)
  - `startDiscovery()`
  - `startLeScan()`
- [`BluetoothAdapter.LeScanCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter.LeScanCallback)
- [`BluetoothLeScanner`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner)
  - `startScan()`

## Permissions

This section describes updates to the Android permissions model.

> [!NOTE]
> **Note:** Each change described in this section affects **all** apps on devices that run Android 10 or higher, even apps that target Android 9 (API level 28) or lower.

### Restricted access to screen contents

To protect users' screen contents, Android 10 prevents silent
access to the device's screen contents by changing the scope of the
`READ_FRAME_BUFFER`, `CAPTURE_VIDEO_OUTPUT`, and `CAPTURE_SECURE_VIDEO_OUTPUT`
permissions. As of Android 10, these permissions are
[signature-access](https://developer.android.com/guide/topics/permissions/overview#signature_permissions)
only.

Apps that need to access the device's screen contents should use the
[`MediaProjection`](https://developer.android.com/reference/android/media/projection/MediaProjection)
API, which displays a prompt asking the user to provide consent.

### User-facing permission check on legacy apps

If your app targets Android 5.1 (API level 22) or lower, users see a permissions
screen when using your app on a device that runs Android 10 or
higher for the first time, as shown in Figure 1. This screen gives users the
opportunity to revoke access to permissions that the system previously granted
to your app at install time.

> [!CAUTION]
> **Caution:** If you want to publish your app on Google Play, you must target Android 9 (API level 28) or higher. To learn more, see the guide on how to [meet
> Google Play's target API level
> requirement](https://developer.android.com/distribute/best-practices/develop/target-sdk).

![Screen capture of dialog](https://developer.android.com/static/images/about/versions/10/legacy-app-permissions.svg) **Figure 1.**User-facing dialog that allows review of legacy permissions

### Physical activity recognition

Android 10 introduces the
[`android.permission.ACTIVITY_RECOGNITION`](https://developer.android.com/reference/android/Manifest.permission#ACTIVITY_RECOGNITION)
runtime permission for apps that need to detect the user's step count or
classify the user's physical activity, such as walking, biking, or moving in a
vehicle. This is designed to give users visibility of how device sensor data is
used in Settings.

Some libraries within Google Play services, such as the [Activity
Recognition API](https://developers.google.com/location-context/activity-recognition/)
and the [Google Fit
API](https://developers.google.com/fit/android/authorization#android_permissions),
don't provide results unless the user has granted your app this permission.

The only [built-in sensors](https://developer.android.com/guide/topics/sensors/sensors_overview) on the
device that require you to declare this permission are the [step
counter](https://developer.android.com/guide/topics/sensors/sensors_motion#sensors-motion-stepcounter) and
[step
detector](https://developer.android.com/guide/topics/sensors/sensors_motion#sensors-motion-stepdetector)
sensors.

If your app targets Android 9 (API level 28) or lower, the system auto-grants
the `android.permission.ACTIVITY_RECOGNITION` permission to your app, as needed,
if your app satisfies each of the following conditions:

- The manifest file includes the `com.google.android.gms.permission.ACTIVITY_RECOGNITION` permission.
- The manifest file **doesn't** include the `android.permission.ACTIVITY_RECOGNITION` permission.

If the system-auto grants the `android.permission.ACTIVITY_RECOGNITION`
permission, your app retains the permission after you update your app to target
Android 10. However, the user can revoke this permission at any
time in system settings.

### Permission groups removed from UI

As of Android 10, apps cannot look up how [permissions are
grouped](https://developer.android.com/guide/topics/permissions/overview#perm-groups) in the UI.