---
title: https://developer.android.com/about/versions/marshmallow/android-6.0-changes
url: https://developer.android.com/about/versions/marshmallow/android-6.0-changes
source: md.txt
---

Along with new features and capabilities, Android 6.0 (API level 23) includes a variety of
system changes and API behavior changes. This document highlights
some of the key changes that you should understand and account for in your apps.

If you have previously published an app for Android, be aware that these changes in the
platform affect your app.

## Runtime Permissions

This release introduces a new permissions model, where users can now directly manage
app permissions at runtime. This model gives users improved visibility and control over
permissions, while streamlining the installation and auto-update processes for app developers.
Users can grant or revoke permissions individually for installed apps.

On your apps that target Android 6.0 (API level 23) or higher, make sure to check for and request
permissions at runtime. To determine if your app has been granted a permission, call the
new `https://developer.android.com/reference/android/content/Context#checkSelfPermission(java.lang.String)`
method. To request a permission, call the new
`https://developer.android.com/reference/android/app/Activity#requestPermissions(java.lang.String[], int)`
method. Even if your app is not targeting Android 6.0 (API level 23), you should test your app under
the new permissions model.

For details on supporting the new permissions model in your app, see
[Working with System Permissions](https://developer.android.com/training/permissions). For tips on how to assess the impact on your app,
see [Permissions Usage Notes](https://developer.android.com/training/permissions/usage-notes#testing).

## Doze and App Standby

This release introduces new power-saving optimizations for idle devices and apps. These
features affect all apps so make sure to test your apps in these new modes.

- **Doze** : If a user unplugs a device and leaves it stationary, with its screen off, for a period of time, the device goes into *Doze* mode, where it attempts to keep the system in a sleep state. In this mode, devices periodically resume normal operations for brief periods of time so that app syncing can occur and the system can perform any pending operations.
- **App Standby**: App Standby allows the system to determine that an app is idle when the user is not actively using it. The system makes this determination when the user does not touch the app for a certain period of time. If the device is unplugged, the system disables network access and suspends syncs and jobs for the apps it deems idle.

To learn more about these power-saving changes, see
[Optimizing for Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby).

## Apache HTTP Client Removal

Android 6.0 release removes support for the Apache HTTP client. If your app is using this client and
targets Android 2.3 (API level 9) or higher, use the `https://developer.android.com/reference/java/net/HttpURLConnection` class
instead. This API is more efficient because it reduces network use through transparent compression
and response caching, and minimizes power consumption. To continue using the Apache HTTP APIs, you
must first declare the following compile-time dependency in your `build.gradle` file:

```text
android {
    useLibrary 'org.apache.http.legacy'
}
```

## BoringSSL

Android is moving away from OpenSSL to the
[BoringSSL](https://boringssl.googlesource.com/boringssl/)
library. If you're using the Android NDK in your app, don't link against cryptographic libraries
that are not a part of the NDK API, such as `libcrypto.so` and `libssl.so`. These
libraries are not public APIs, and may change or break without notice across releases and devices.
In addition, you may expose yourself to security vulnerabilities. Instead, modify your
native code to call the Java cryptography APIs via JNI or to statically link against a
cryptography library of your choice.

## Access to Hardware Identifier

To provide users with greater data protection, starting in this release, Android
removes programmatic access to the device's local hardware identifier for
apps using the Wi-Fi and Bluetooth APIs. The
`https://developer.android.com/reference/android/net/wifi/WifiInfo#getMacAddress()` and the
`https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getAddress()` methods
now return a constant value of `02:00:00:00:00:00`.

To access the hardware identifiers of nearby external devices via Bluetooth and Wi-Fi scans,
your app must now have the `https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION` or
`https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION` permissions:

- `https://developer.android.com/reference/android/net/wifi/WifiManager#getScanResults()`
- `https://developer.android.com/reference/android/bluetooth/BluetoothDevice#ACTION_FOUND`
- `https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner#startScan(android.bluetooth.le.ScanCallback)`

**Note**: When a device running Android 6.0 (API level 23) initiates a
background Wi-Fi or Bluetooth scan, the operation is visible to external devices as
originating from a randomized MAC address.

## Notifications


This release removes the `Notification.setLatestEventInfo()` method. Use the
`https://developer.android.com/reference/android/app/Notification.Builder` class instead to construct notifications. To update a
notification repeatedly, reuse the `https://developer.android.com/reference/android/app/Notification.Builder` instance. Call the
`https://developer.android.com/reference/android/app/Notification.Builder#build()` method to get
updated `https://developer.android.com/reference/android/app/Notification` instances.

The `adb shell dumpsys notification` command no longer prints out your notification text.
Use the `adb shell dumpsys notification --noredact` command instead to print out the text
in a notification object.

## AudioManager Changes

Setting the volume directly or muting specific streams via the `https://developer.android.com/reference/android/media/AudioManager`
class is no longer supported. The `https://developer.android.com/reference/android/media/AudioManager#setStreamSolo(int, boolean)` method is deprecated, and you should call the
`https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener, int, int)`
method instead. Similarly, the
`https://developer.android.com/reference/android/media/AudioManager#setStreamMute(int, boolean)` method is
deprecated; instead, call the `https://developer.android.com/reference/android/media/AudioManager#adjustStreamVolume(int, int, int)` method and pass in the direction value
`https://developer.android.com/reference/android/media/AudioManager#ADJUST_MUTE` or
`https://developer.android.com/reference/android/media/AudioManager#ADJUST_UNMUTE`.

## Text Selection

![Screen showing new text selection features within a floating toolbar](https://developer.android.com/static/images/android-6.0/text-selection.gif)

When users select text in your app, you can now display text selection actions such as
*Cut* , *Copy* , and *Paste* in a
[floating toolbar](https://material.io/guidelines/patterns/selection.html#selection-text-selection). The user interaction implementation is similar to that
for the contextual action bar, as described in
[Enabling the contextual action mode for individual views](https://developer.android.com/guide/topics/ui/menus#CABforViews).

To implement a floating toolbar for text selection, make the following changes in your existing
apps:

1. In your `https://developer.android.com/reference/android/view/View` or `https://developer.android.com/reference/android/app/Activity` object, change your `https://developer.android.com/reference/android/view/ActionMode` calls from `startActionMode(Callback)` to `startActionMode(Callback, ActionMode.TYPE_FLOATING)`.
2. Take your existing implementation of `ActionMode.Callback` and make it extend `https://developer.android.com/reference/android/view/ActionMode.Callback2` instead.
3. Override the `https://developer.android.com/reference/android/view/ActionMode.Callback2#onGetContentRect(android.view.ActionMode, android.view.View, android.graphics.Rect)` method to provide the coordinates of the content `https://developer.android.com/reference/android/graphics/Rect` object (such as a text selection rectangle) in the view.
4. If the rectangle positioning is no longer valid, and this is the only element to be invalidated, call the `https://developer.android.com/reference/android/view/ActionMode#invalidateContentRect()` method.

If you are using [Android Support Library](https://developer.android.com/tools/support-library) revision 22.2, be aware that floating toolbars are not
backward-compatible and appcompat takes control over `https://developer.android.com/reference/android/view/ActionMode` objects by
default. This prevents floating toolbars from being displayed. To enable
`https://developer.android.com/reference/android/view/ActionMode` support in an
`https://developer.android.com/reference/android/support/v7/app/AppCompatActivity`, call
`https://developer.android.com/reference/android/support/v7/app/AppCompatActivity#getDelegate()`, then call
`https://developer.android.com/reference/android/support/v7/app/AppCompatDelegate#setHandleNativeActionModesEnabled(boolean)` on the returned
`https://developer.android.com/reference/android/support/v7/app/AppCompatDelegate` object and set the input
parameter to `false`. This call returns control of `https://developer.android.com/reference/android/view/ActionMode` objects to
the framework. In devices running Android 6.0 (API level 23), that allows the framework to support
`https://developer.android.com/reference/android/support/v7/app/ActionBar` or floating toolbar modes, while on devices running
Android 5.1 (API level 22) or lower, only the `https://developer.android.com/reference/android/support/v7/app/ActionBar` modes are
supported.

## Browser Bookmark Changes

This release removes support for global bookmarks. The
`android.provider.Browser.getAllBookmarks()` and `android.provider.Browser.saveBookmark()`
methods are now removed. Likewise, the `READ_HISTORY_BOOKMARKS` and `WRITE_HISTORY_BOOKMARKS`
permissions are removed. If your app targets Android 6.0 (API level 23) or higher, don't access
bookmarks from the global provider or use the bookmark permissions. Instead, your app should store
bookmarks data internally.

## Android Keystore Changes

With this release, the
[Android Keystore provider](https://developer.android.com/training/articles/keystore) no longer supports
DSA. ECDSA is still supported.

Keys which do not require encryption at rest will no longer be deleted when secure lock screen
is disabled or reset (for example, by the user or a Device Administrator). Keys which require
encryption at rest will be deleted during these events.

## Wi-Fi and Networking Changes

This release introduces the following behavior changes to the Wi-Fi and networking APIs.

- Your apps can now change the state of `https://developer.android.com/reference/android/net/wifi/WifiConfiguration` objects only if you created these objects. You are not permitted to modify or delete `https://developer.android.com/reference/android/net/wifi/WifiConfiguration` objects created by the user or by other apps.
- Previously, if an app forced the device to connect to a specific Wi-Fi network by using `https://developer.android.com/reference/android/net/wifi/WifiManager#enableNetwork(int, boolean)` with the `disableAllOthers=true` setting, the device disconnected from other networks such as cellular data. In This release, the device no longer disconnects from such other networks. If your app's `targetSdkVersion` is `"20"` or lower, it is pinned to the selected Wi-Fi network. If your app's `targetSdkVersion` is `"21"` or higher, use the multinetwork APIs (such as `https://developer.android.com/reference/android/net/Network#openConnection(java.net.URL)`, `https://developer.android.com/reference/android/net/Network#bindSocket(java.net.Socket)`, and the new `https://developer.android.com/reference/android/net/ConnectivityManager#bindProcessToNetwork(android.net.Network)` method) to ensure that its network traffic is sent on the selected network.

## Camera Service Changes

In This release, the model for accessing shared resources in the camera service has been changed
from the previous "first come, first serve" access model to an access model where high-priority
processes are favored. Changes to the service behavior include:

- Access to camera subsystem resources, including opening and configuring a camera device, is awarded based on the "priority" of the client application process. Application processes with user-visible or foreground activities are generally given a higher-priority, making camera resource acquisition and use more dependable.
- Active camera clients for lower priority apps may be "evicted" when a higher priority application attempts to use the camera. In the deprecated `https://developer.android.com/reference/android/hardware/Camera` API, this results in `https://developer.android.com/reference/android/hardware/Camera.ErrorCallback#onError(int, android.hardware.Camera)` being called for the evicted client. In the `https://developer.android.com/reference/android/hardware/camera2/package-summary` API, it results in `https://developer.android.com/reference/android/hardware/camera2/CameraDevice.StateCallback#onDisconnected(android.hardware.camera2.CameraDevice)` being called for the evicted client.
- On devices with appropriate camera hardware, separate application processes are able to independently open and use separate camera devices simultaneously. However, multi-process use cases, where simultaneous access causes significant degradation of performance or capabilities of any of the open camera devices, are now detected and disallowed by the camera service. This change may result in "evictions" for lower priority clients even when no other app is directly attempting to access the same camera device.
- Changing the current user causes active camera clients in apps owned by the previous user account to be evicted. Access to the camera is limited to user profiles owned by the current device user. In practice, this means that a "Guest" account, for example, will not be able to leave running processes that use the camera subsystem when the user has switched to a different account.

## Runtime

The ART runtime now properly implements access rules for the
`https://developer.android.com/reference/java/lang/reflect/Constructor#newInstance(java.lang.Object...)` method. This
change fixes a problem where Dalvik was checking access rules incorrectly in previous versions.
If your app uses the
`https://developer.android.com/reference/java/lang/reflect/Constructor#newInstance(java.lang.Object...)` method and you
want to override access checks, call the
`https://developer.android.com/reference/java/lang/reflect/AccessibleObject#setAccessible(boolean)` method with the input
parameter set to `true`. If your app uses the
[v7 appcompat library](https://developer.android.com/tools/support-library/features#v7-appcompat) or the
[v7 recyclerview library](https://developer.android.com/tools/support-library/features#v7-recyclerview),
you must update your app to use to the latest versions of these libraries. Otherwise, make sure that
any custom classes referenced from XML are updated so that their class constructors are accessible.

This release updates the behavior of the dynamic linker. The dynamic linker now understands the
difference between a library's `soname` and its path
([public bug 6670](https://code.google.com/p/android/issues/detail?id=6670)), and search by `soname` is now
implemented. Apps which previously worked that have bad `DT_NEEDED` entries
(usually absolute paths on the build machine's file system) may fail when loaded.

The `dlopen(3) RTLD_LOCAL` flag is now correctly implemented. Note that
`RTLD_LOCAL` is the default, so calls to `dlopen(3)` that didn't explicitly use
`RTLD_LOCAL` will be affected (unless your app explicitly used `RTLD_GLOBAL`). With
`RTLD_LOCAL`, symbols will not be made available to libraries loaded by later calls to
`dlopen(3)` (as opposed to being referenced by `DT_NEEDED` entries).

<br />


On previous versions of Android, if your app requested the system to load a shared library with
text relocations, the system displayed a warning but still allowed the library to be loaded.
Beginning in this release, the system rejects this library if your app's target SDK version is 23
or higher. To help you detect if a library failed to load, your app should log the
`dlopen(3)` failure, and include the problem description text that the `dlerror(3)`
call returns. To learn more about handling text relocations, see this
[guide](https://wiki.gentoo.org/wiki/Hardened/Textrels_Guide).

## APK Validation

The platform now performs stricter validation of APKs. An APK is considered corrupt if a file is
declared in the manifest but not present in the APK itself. An APK must be re-signed if any of the
contents are removed.

## USB Connection

Device connections through the USB port are now set to charge-only mode by default. To access
the device and its content over a USB connection, users must explicitly grant permission for such
interactions. If your app supports user interactions with the device over a USB port, take into
consideration that the interaction must be explicitly enabled.

## Android for Work Changes

This release includes the following behavior changes for Android for Work:

- **Work contacts in personal contexts.** The Google Dialer Call Log now displays work contacts when the user views past calls. Setting `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileCallerIdDisabled(android.content.ComponentName, boolean)` to `true` hides the work profile contacts in the Google Dialer Call Log. Work contacts can be displayed along with personal contacts to devices over Bluetooth only if you set `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setBluetoothContactSharingDisabled(android.content.ComponentName, boolean)` to `false`. By default, it is set to `true`.
- **Wi-Fi configuration removal:** Wi-Fi configurations added by a Profile Owner (for example, through calls to the `https://developer.android.com/reference/android/net/wifi/WifiManager#addNetwork(android.net.wifi.WifiConfiguration)` method) are now removed if that work profile is deleted.
- **Wi-Fi configuration lockdown:** Any Wi-Fi configuration created by an active Device Owner can no longer be modified or deleted by the user if `https://developer.android.com/reference/android/provider/Settings.Global#WIFI_DEVICE_OWNER_CONFIGS_LOCKDOWN` is non-zero. The user can still create and modify their own Wi-Fi configurations. Active Device Owners have the privilege of editing or removing any Wi-Fi configurations, including those not created by them.
- **Download device policy controller via Google account addition:** When a Google account that requires management via a device policy controller (DPC) app is added to a device outside of a managed context, the add account flow now prompts the user to install the appropriate WPC. This behavior also applies to accounts added via **Settings \> Accounts** and in the initial device setup wizard.
- **Changes to specific `https://developer.android.com/reference/android/app/admin/DevicePolicyManager` API behaviors:**
  - Calling the `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCameraDisabled(android.content.ComponentName, boolean)` method affects the camera for the calling user only; calling it from the managed profile doesn't affect camera apps running on the primary user.
  - In addition, the `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyguardDisabledFeatures(android.content.ComponentName, int)` method is now available for Profile Owners, as well as to Device Owners.
  - A Profile Owner can set these keyguard restrictions:
    - `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_TRUST_AGENTS` and `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_FINGERPRINT`, which affect the keyguard settings for the profile's parent user.
    - `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_UNREDACTED_NOTIFICATIONS`, which only affects notifications generated by applications in the managed profile.
  - The `DevicePolicyManager.createAndInitializeUser()` and `DevicePolicyManager.createUser()` methods have been deprecated.
  - The `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setScreenCaptureDisabled(android.content.ComponentName, boolean)` method now also blocks the assist structure when an app of the given user is in the foreground.
  - `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_DEVICE_ADMIN_PACKAGE_CHECKSUM` now defaults to SHA-256. SHA-1 is still supported for backwards compatibility but will be removed in future. `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_DEVICE_ADMIN_SIGNATURE_CHECKSUM` now only accepts SHA-256.
  - Device initializer APIs which existed in the Android 6.0 (API level 23) are now removed.
  - `EXTRA_PROVISIONING_RESET_PROTECTION_PARAMETERS` is removed so NFC bump provisioning cannot programmatically unlock a factory reset protected device.
  - You can now use the `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE` extra to pass data to the device owner app during NFC provisioning of the managed device.
  - Android for Work APIs are optimized for M runtime permissions, including Work profiles, assist layer, and others. New `https://developer.android.com/reference/android/app/admin/DevicePolicyManager` permission APIs don't affect pre-M apps.
  - When users back out of the synchronous part of the setup flow initiated through an `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROVISION_MANAGED_PROFILE` or `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROVISION_MANAGED_DEVICE` intent, the system now returns a `https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED` result code.
- **Changes to other APIs** :
  - Data Usage: The `android.app.usage.NetworkUsageStats` class has been renamed `https://developer.android.com/reference/android/app/usage/NetworkStats`.
- **Changes to global settings** :
  - These settings can no longer be set via `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalSetting(android.content.ComponentName, java.lang.String, java.lang.String)`:
    - `BLUETOOTH_ON`
    - `DEVELOPMENT_SETTINGS_ENABLED`
    - `MODE_RINGER`
    - `NETWORK_PREFERENCE`
    - `WIFI_ON`
  - These global settings can now be set via `https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalSetting(android.content.ComponentName, java.lang.String, java.lang.String)`:
    - `https://developer.android.com/reference/android/provider/Settings.Global#WIFI_DEVICE_OWNER_CONFIGS_LOCKDOWN`