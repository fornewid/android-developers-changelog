---
title: https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element
url: https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element
source: md.txt
---

# &lt;uses-permission-sdk-23>

syntax:
:

    ```xml
    <uses-permission-sdk-23 android:name="string"
            android:maxSdkVersion="integer" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Specifies that an app wants a particular permission, but only if the app is installed on a device running Android 6.0 (API level 23) or higher. If the device runs API level 22 or lower, the app doesn't want the specified permission.This element is useful when you update an app to include a new feature that requires an additional permission. If a user updates an app on a device that is running API level 22 or lower, the system prompts the user at install time to grant all new permissions that are declared in that update. If a new feature is minor enough, you might prefer to disable the feature altogether on those devices, so the user doesn't have to grant additional permissions to update the app.

    By using the`<uses-permission-sdk-23>`element instead of[`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element), you can request the permission*only* if the app is running on platforms that support the[runtime permissions](https://developer.android.com/training/permissions/requesting)model, in which the user grants permissions to the app while it is running.

    For more information on permissions, see the[Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)section in the app manifest overview and the[Permissions on Android](https://developer.android.com/guide/topics/permissions)guide. A list of permissions defined by the base platform is available at[android.Manifest.permission](https://developer.android.com/reference/android/Manifest.permission).

attributes:
:

    `android:name`
    :   The name of the permission. This permission can be one defined by the app with the[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)element, it can be a permission defined by another app, or it can be one of the standard system permissions, such as["android.permission.CAMERA"](https://developer.android.com/reference/android/Manifest.permission#CAMERA)or["android.permission.READ_CONTACTS"](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS).

    `android:maxSdkVersion`
    :   The highest API level at which this permission is granted to your app. If the app installs on a device with a later API level, the app isn't granted the permission and can't use any related functionality.

introduced in:
:   API level 23

see also:
:
    - [<permission>](https://developer.android.com/guide/topics/manifest/permission-element)
    - [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
    - [<uses-feature>](https://developer.android.com/guide/topics/manifest/uses-feature-element)