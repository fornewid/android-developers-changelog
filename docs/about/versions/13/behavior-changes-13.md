---
title: https://developer.android.com/about/versions/13/behavior-changes-13
url: https://developer.android.com/about/versions/13/behavior-changes-13
source: md.txt
---

Like earlier releases, Android 13 includes behavior changes that may affect your
app. The following behavior changes apply exclusively to apps that are targeting
Android 13 or higher. If your app is targeting Android 13 or higher, you should
modify your app to support these behaviors properly, where applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 13](https://developer.android.com/about/versions/13/behavior-changes-all).

## Privacy

### Notification permission affects foreground service appearance

If the user denies the
[notification permission](https://developer.android.com/guide/topics/ui/notifiers/notification-permission),
they don't see notices related to foreground services in the
[notification drawer](https://developer.android.com/guide/topics/ui/notifiers/notifications#appearances).
However, users still see notices related to foreground services in the
[Task Manager](https://developer.android.com/about/versions/13/changes/fgs-manager),
regardless of whether the notification permission is granted.

### New runtime permission for nearby Wi-Fi devices

On previous versions of Android, the user needs to grant your app the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission to complete several common Wi-Fi use cases.

Because it's difficult for users to associate location permissions with Wi-Fi
functionality, Android 13 (API level 33) introduces a runtime permission in the
[`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES)
permission group for apps that manage a device's connections to nearby access
points over Wi-Fi. This permission,
[`NEARBY_WIFI_DEVICES`](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES),
fulfills Wi-Fi use cases such as the following:

- Find or connect to nearby devices, such as printers or media casting devices. This workflow allows your app to accomplish these sorts of tasks:
  - Receive AP information out of band, such as through BLE.
  - Discover and connect to devices over Wi-Fi Aware and connect using a local-only hotspot.
  - Discover and connect to devices over Wi-Fi Direct.
- Initiate a connection to a known SSID, such as a car or smart home device.
- Start a local-only hotspot.
- Range to nearby Wi-Fi Aware devices.

As long as your app doesn't derive physical location information from the Wi-Fi
APIs, request `NEARBY_WIFI_DEVICES` instead of `ACCESS_FINE_LOCATION` when you
target Android 13 or higher and use Wi-Fi APIs. When you declare
the `NEARBY_WIFI_DEVICES` permission, strongly assert that your app never
derives physical location information from Wi-Fi APIs. To do so, set the
`android:usesPermissionFlags` attribute to `neverForLocation`. This process is
similar to the one you do in Android 12 (API level 31) and higher when you
[assert that Bluetooth device information is never used for
location](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#assert-never-for-location).
| **Note:** This change affects your app only if you call a Wi-Fi API. View the [list of affected APIs](https://developer.android.com/guide/topics/connectivity/wifi-permissions#check-for-apis-that-require-permission).

Learn more about how to
[request permission to access nearby Wi-Fi devices](https://developer.android.com/guide/topics/connectivity/wifi-permissions).

### Granular media permissions

![The 2 buttons for the dialog, from top to bottom, are Allow and Don't
allow](https://developer.android.com/static/images/about/versions/13/storage-permission-split.svg) **Figure 1.** System permissions dialog that the user sees when you request the `READ_MEDIA_AUDIO` permission.

If your app targets Android 13 or higher and needs to
[access media files that other apps have
created](https://developer.android.com/training/data-storage/shared/media#storage-permission), you must
request one or more of the following granular media permissions instead of the
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
permission:

| Type of media | Permission to request |
|---|---|
| Images and photos | [`READ_MEDIA_IMAGES`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES) |
| Videos | [`READ_MEDIA_VIDEO`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO) |
| Audio files | [`READ_MEDIA_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_AUDIO) |

Before you access another app's media files, verify that the user has granted
the appropriate granular media permissions to your app.

Figure 1 shows an app that requests the `READ_MEDIA_AUDIO` permission.

If you request both the `READ_MEDIA_IMAGES` permission and the
`READ_MEDIA_VIDEO` permission at the same time, only one system permission
dialog appears.

If your app was previously granted the
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
permission, then any requested `READ_MEDIA_*` permissions are granted
automatically when upgrading. You can use the following ADB command to review
upgraded permissions:  

```
adb shell cmd appops get --uid PACKAGE_NAME
```

<br />

| **Note:** If your app only needs to access images, photos, and videos, consider using the [photo picker](https://developer.android.com/about/versions/13/features/photopicker) instead of declaring the `READ_MEDIA_IMAGES` and `READ_MEDIA_VIDEO` permissions.

### Use of body sensors in the background requires new permission

Android 13 introduces the concept of "while in use" access for
body sensors, such as heart rate, temperature, and blood oxygen percentage. This
access model is very similar to the one that the system introduced for [location
in Android 10 (API level 29)](https://developer.android.com/about/versions/10/privacy/changes#app-access-device-location).

If your app targets Android 13 and requires access to body sensor
information while running in the background, you must declare the new
[`BODY_SENSORS_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS_BACKGROUND)
permission in addition to the existing
[`BODY_SENSORS`](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS)
permission.
| **Note:** This is a "hard-restricted" permission that cannot be held by an app until the device's installer allowlists the permission for your app. For more details, see this guide on [restricted permissions](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/permission/Permissions.md#restricted-permissions).

## Performance and battery

### Battery Resource Utilization

If the user places your app in the
["restricted" state](https://developer.android.com/topic/performance/background-optimization#bg-restrict) for
background battery usage
while your app targets Android 13, the system doesn't deliver the
`BOOT_COMPLETED` broadcast or the `LOCKED_BOOT_COMPLETED` broadcast until the
app is started for other reasons.

## User experience

### Media controls derived from `PlaybackState`

For apps targeting Android 13 (API level 33) and higher, the system derives
media controls from
[`PlaybackState`](https://developer.android.com/reference/android/media/session/PlaybackState) actions. This
allows the system to show a richer set of controls that are technically
consistent between phones and tablet devices, and also align with how media
controls are rendered on other Android platforms such as Android Auto and
Android TV.

Figure 2 shows an example of how this looks on a phone and tablet device,
respectively.
![Media controls in terms of how they appear on phone and tablets devices,
using an example of a sample track showing how the buttons may appear](https://developer.android.com/static/images/about/versions/13/media-controls-phone-tablet.png) **Figure 2:**Media controls on phone and tablet devices

Prior to Android 13, the system displayed up to five actions from the `MediaStyle`
notification in the order in which they were [added](https://developer.android.com/reference/android/app/Notification.Builder#addAction(android.app.Notification.Action)).
In compact mode---for example, in the collapsed quick settings---up to
three actions specified with [`setShowActionsInCompactView()`](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle#setShowActionsInCompactView(int...))
were shown.

Starting with Android 13, the system displays up to five action buttons based
on the `PlaybackState` as described in the following table. In compact mode, only the first three
action slots will be displayed. For apps that don't target Android 13 or those
that don't include a `PlaybackState`, the system will display controls based on
the `Action` list added to the `MediaStyle` notification as described in the
previous paragraph.

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

| Slot | Action | Criteria |
|---|---|---|
| 1 | Play | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is one of the following: - `STATE_NONE` - `STATE_STOPPED` - `STATE_PAUSED` - `STATE_ERROR` |
| 1 | Loading spinner | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is one of the following: - `STATE_CONNECTING` - `STATE_BUFFERING` |
| 1 | Pause | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is none of the above. |
| 2 | Previous | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) include `ACTION_SKIP_TO_PREVIOUS`. |
| 2 | Custom | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) do not include `ACTION_SKIP_TO_PREVIOUS` and `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 2 | Empty | `PlaybackState` [extras](https://developer.android.com/reference/android/media/session/PlaybackState#getExtras()) include a `true` boolean value for key [`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV). |
| 3 | Next | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) include `ACTION_SKIP_TO_NEXT`. |
| 3 | Custom | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) do not include `ACTION_SKIP_TO_NEXT` and `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 3 | Empty | `PlaybackState` [extras](https://developer.android.com/reference/android/media/session/PlaybackState#getExtras()) include a `true` boolean value for key [`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT). |
| 4 | Custom | `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 5 | Custom | `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |

<br />

Custom actions are placed in the order in which they were added to the
`PlaybackState`.

### App color theme applied automatically to WebView content

For apps targeting Android 13 (API level 33) or higher, the
[`setForceDark()`](https://developer.android.com/reference/android/webkit/WebSettings#setForceDark(int))
method is deprecated, resulting in a no-op if the method is called.

Instead, WebView now always sets
the media query `prefers-color-scheme` according to the app's theme attribute,
[`isLightTheme`](https://developer.android.com/reference/android/R.styleable#Theme_isLightTheme). In other
words, if `isLightTheme` is `true` or not specified, `prefers-color-scheme` is
`light`; otherwise, it is `dark`. This behavior means that the web content's
light or dark style is applied automatically to match the app's theme if the
content supports it.

For most apps, the new behavior should apply the appropriate app styles
automatically, however you should test your app to check for any cases where you
might've been manually controlling dark mode settings.

If you still need to customize your app's color theme behavior, use the
[`setAlgorithmicDarkeningAllowed()`](https://developer.android.com/reference/android/webkit/WebSettings#setAlgorithmicDarkeningAllowed(boolean))
method instead. For backward compatibility with previous Android versions, we
recommend using the equivalent
[`setAlgorithmicDarkeningAllowed()`](https://developer.android.com/reference/androidx/webkit/WebSettingsCompat#setAlgorithmicDarkeningAllowed(android.webkit.WebSettings,%20boolean))
method in AndroidX.

See the documentation for that method to learn more about what behavior you can
expect in your app depending on your app's
[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) and theme
settings.

## Connectivity

### BluetoothAdapter#enable() and BluetoothAdapter#disable() deprecated

For apps targeting Android 13 (API level 33) or higher, the
[`BluetoothAdapter#enable()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#enable()) and
[`BluetoothAdapter#disable()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#disable()) methods are deprecated and always
return `false`.

The following types of apps are exempt from these changes:

- Device Owner apps
- Profile Owner apps
- System apps

## Google Play services

### Permission required for advertising ID

Apps that use Google Play services [advertising
ID](https://support.google.com/googleplay/android-developer/answer/6048248) and
target Android 13 (API level 33) and higher must
declare the [`AD_ID`](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info#public-string-getid) normal permission in their app's
manifest file, as follows:  

    <manifest ...>
        <!-- Required only if your app targets Android 13 or higher. -->
        <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

        <application ...>
            ...
        </application>
    </manifest>

If your app does not declare this permission when targeting Android 13 or
higher, the advertising ID is automatically removed and replaced with a string
of zeroes.

If your app uses SDKs that declare the `AD_ID` permission in the library's
manifest, then the permission is merged with your app's manifest file by
default. In this case, you don't need to declare the permission in your app's
manfiest file.

To learn more, see [Advertising
ID](https://support.google.com/googleplay/android-developer/answer/6048248) in
the Play Console Help.

## Updated non-SDK restrictions

Android 13 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 13, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API
level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see [Updates to
non-SDK interface restrictions in Android 13](https://developer.android.com/about/versions/13/changes/non-sdk-13).
To learn more about non-SDK interfaces generally, see [Restrictions on non-SDK
interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).