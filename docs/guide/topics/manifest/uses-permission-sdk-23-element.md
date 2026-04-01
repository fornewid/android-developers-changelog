---
title: <uses-permission-sdk-23>  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# <uses-permission-sdk-23> Stay organized with collections Save and categorize content based on your preferences.




syntax:
:   ```
    <uses-permission-sdk-23 android:name="string"
            android:maxSdkVersion="integer" />
    ```

contained in:
:   `<manifest>`

description:
:   Specifies that an app wants a particular permission, but only if the app is
    installed on a device running Android 6.0 (API level 23) or higher. If the device
    runs API level 22 or lower, the app doesn't want the specified
    permission.

    This element is useful when you update an app to include a new
    feature that requires an additional permission. If a user updates an app on a
    device that is running API level 22 or lower, the system prompts the user
    at install time to grant all new permissions that are declared in that
    update. If a new feature is minor enough, you might prefer to disable
    the feature altogether on those devices, so the user doesn't have to grant
    additional permissions to update the app.

    By using the
    `<uses-permission-sdk-23>` element instead of [`<uses-permission>`](/guide/topics/manifest/uses-permission-element),
    you can request the permission *only* if the app is running on
    platforms that support the [runtime permissions](/training/permissions/requesting)
    model, in which the user
    grants permissions to the app while it is running.

    For more information on permissions, see the [Permissions](/guide/topics/manifest/manifest-intro#perms)
    section in the app manifest overview and the [Permissions on Android](/guide/topics/permissions)
    guide. A list of permissions defined by the base platform is available
    at `android.Manifest.permission`.

attributes:
:   `android:name`
    :   The name of the permission. This permission can be one defined by the
        app with the `<permission>`
        element, it can be a permission defined by another app, or it can be one
        of the standard system permissions, such as
        `"android.permission.CAMERA"`
        or `"android.permission.READ_CONTACTS"`.

    `android:maxSdkVersion`
    :   The highest API level at which this permission is granted to your
        app. If the app installs on a device with a later API level, the app
        isn't granted the permission and can't use any related functionality.

introduced in:
:   API level 23

see also:
:   * `<permission>`
    * [`<uses-permission>`](/guide/topics/manifest/uses-permission-element)
    * `<uses-feature>`