---
title: https://developer.android.com/about/versions/11/privacy/permissions
url: https://developer.android.com/about/versions/11/privacy/permissions
source: md.txt
---

Android 11 gives users the ability to specify more granular
permissions for location, microphone, and camera. Additionally, the system
resets the permissions of unused apps that target Android 11 or
higher, and apps might need to update the permissions that they declare if they
use the system alert window or read information related to phone numbers.

## One-time permissions

Starting in Android 11, whenever your app requests a permission
related to location, microphone, or camera, the user-facing permissions dialog
contains an option called **Only this time** . If the user selects this option in
the dialog, your app is granted a temporary *one-time permission*.

Learn more about how the system handles [one-time
permissions](https://developer.android.com/training/permissions/requesting#one-time).

> [!NOTE]
> **Note:** If your app already follows best practices when it [requests runtime
> permissions](https://developer.android.com/training/permissions/requesting), you don't need to change your app to support one-time permissions.

## Auto-reset permissions from unused apps

If your app targets Android 11 or higher and isn't used for a few
months, the system protects user data by automatically resetting the sensitive
runtime permissions that the user had granted your app. This action has the same
effect as if the user viewed a permission in system settings and changed your
app's access level to **Deny** . If your app follows best practices for
[requesting permissions at runtime](https://developer.android.com/training/permissions/requesting), you
shouldn't need to make any changes to your app. That's because, as the user
interacts with features in your app, you should verify that the features have
the permissions that they need.

> [!NOTE]
> **Note:** The system resets only [runtime
> permissions](https://developer.android.com/guide/topics/permissions/overview#runtime_requests_android_60_and_higher), which are the permissions that display a runtime prompt to the user when requested.

Learn more about how the system [auto-resets permissions of unused
apps](https://developer.android.com/training/permissions/requesting#auto-reset-permissions-unused-apps).

## Permission dialog visibility

Starting in Android 11, if the user taps **Deny** for a
specific permission more than once during your app's lifetime of installation on
a device, the user doesn't see the system permissions dialog if your app
requests that permission again. The user's action implies "don't ask again." On
previous versions, users would see the system permissions dialog each time your
app requested a permission, unless the user had previously selected a "don't ask
again" checkbox or option. This behavior change in Android 11 discourages
repeated requests for permissions that users have chosen to deny.

To identify whether an app has been permanently denied permissions (for debugging
and testing purposes), use the following command:

```
adb shell dumpsys package PACKAGE_NAME
```

Where <var translate="no">PACKAGE_NAME</var> is the name of the package to inspect.

The output of the command contains sections that look like this:

```
...
runtime permissions:
  android.permission.POST_NOTIFICATIONS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
  android.permission.ACCESS_FINE_LOCATION: granted=false, flags=[ USER_SET|USER_FIXED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
  android.permission.BLUETOOTH_CONNECT: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
...
```

Permissions that have been denied once by the user are flagged by `USER_SET`.
Permissions that have been denied permanently by selecting **Deny** twice are
flagged by `USER_FIXED`.

During testing you might want to reset these flags to ensure that testers aren't
surprised when the request dialog isn't shown. To do this, use the command:

<br />

```
adb shell pm clear-permission-flags PACKAGE_NAME PERMISSION_NAME user-set user-fixed
```

<br />

<var translate="no">PERMISSION_NAME</var> is the name of the permission you want to
reset. To view a complete list of Android app permissions, visit the [permissions API
reference page](https://developer.android.com/reference/android/Manifest.permission#constants_1).

> [!NOTE]
> **Note:** If your app already follows [best practices related to
> permissions](https://developer.android.com/privacy/best-practices#permissions), you don't need to change your app to support this behavior change.

Learn more about how to [handle permission
denial](https://developer.android.com/training/permissions/requesting#handle-denial) in your app.

## System alert window changes

Android 11 makes several changes to how apps are granted the
[`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
permission. The changes are intended to protect users by making the permission
grant more intentional.

#### Certain apps are automatically granted SYSTEM_ALERT_WINDOW permission upon request

Certain classes of apps are automatically granted the `SYSTEM_ALERT_WINDOW`
permission upon request:

- Any app that has
  [`ROLE_CALL_SCREENING`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_CALL_SCREENING)
  and requests `SYSTEM_ALERT_WINDOW` is automatically granted the permission. If
  the app loses `ROLE_CALL_SCREENING`, it loses the permission.

- Any app that is capturing the screen via a
  [`MediaProjection`](https://developer.android.com/reference/android/media/projection/MediaProjection)
  and requests `SYSTEM_ALERT_WINDOW` is automatically granted the permission
  unless the user has explicitly denied the permission to the app. When the app
  stops capturing the screen, it loses the permission. This use case is primarily
  intended for game livestreaming apps.

These apps do not need to send
[`ACTION_MANAGE_OVERLAY_PERMISSION`](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_OVERLAY_PERMISSION)
to get the `SYSTEM_ALERT_WINDOW` permission; the apps can simply request
`SYSTEM_ALERT_WINDOW` directly.

#### MANAGE_OVERLAY_PERMISSION intents always bring user to system permissions screen

Beginning with Android 11,
[`ACTION_MANAGE_OVERLAY_PERMISSION`](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_OVERLAY_PERMISSION)
intents always bring the user to the top-level **Settings** screen, where the
user can grant or revoke the
[`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
permissions for apps. Any `package:` data in the intent is ignored.

In earlier versions of Android, the `ACTION_MANAGE_OVERLAY_PERMISSION` intent
could specify a package, which would bring the user to an app-specific screen
for managing the permission. This functionality isn't supported as of
Android 11. Instead, the user must first select the app they wish
to grant or revoke the permission to. This change is intended to protect users
by making the permission grant more intentional.

## Phone numbers

Android 11 changes the phone-related permission that your app
uses when reading phone numbers.

If your app targets Android 11 or higher and needs to access the
phone number APIs shown in the following list, you must request the
[`READ_PHONE_NUMBERS`](https://developer.android.com/reference/kotlin/android/Manifest.permission#read_phone_numbers)
permission, instead of the `READ_PHONE_STATE` permission.

- The `getLine1Number()` method in both the [`TelephonyManager`](https://developer.android.com/reference/kotlin/android/telephony/TelephonyManager#getline1number) class and the [`TelecomManager`](https://developer.android.com/reference/kotlin/android/telecom/TelecomManager#getline1number) class.
- The unsupported `getMsisdn()` method in the [`TelephonyManager`](https://developer.android.com/reference/kotlin/android/telephony/TelephonyManager) class.

If your app declares `READ_PHONE_STATE` to call methods other than the ones in
the previous list, you can continue to request `READ_PHONE_STATE` across all
Android versions. If you use the `READ_PHONE_STATE` permission only for the
methods in the previous list, however, update your manifest file as follows:

1. Change your declaration of `READ_PHONE_STATE` so that your app uses the permission only on Android 10 (API level 29) and lower.
2. Add the `READ_PHONE_NUMBERS` permission.

The following manifest declaration snippet demonstrates this process:

```xml
<manifest>
    <!-- Grants the READ_PHONE_STATE permission only on devices that run
         Android 10 (API level 29) and lower. -->
    <uses-permission android:name="android.permission.READ_PHONE_STATE"
                     android:maxSdkVersion="29" />
    <uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
</manifest>
```

## Additional resources

For more information about the changes to permissions in Android 11, view the
following materials:

### Videos

[Developing with the latest privacy changes in
Android 11](https://www.youtube.com/watch?v=MXlVj-EYgIQ)