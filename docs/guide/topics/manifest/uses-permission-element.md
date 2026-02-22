---
title: https://developer.android.com/guide/topics/manifest/uses-permission-element
url: https://developer.android.com/guide/topics/manifest/uses-permission-element
source: md.txt
---

# &lt;uses-permission>

**Note:** In some cases, the permissions that you request through`<uses-permission>`can affect how Google Play filters your application. If you request a hardware-related permission, such as`CAMERA`, Google Play assumes that your application requires the underlying hardware feature and filters the application from devices that don't offer it.

To control filtering, always explicitly declare hardware features in`<uses-feature>`elements, rather than relying on Google Play to "discover" the requirements in`<uses-permission>`elements. Then, if you want to disable filtering for a particular feature, you can add a`android:required="false"`attribute to the`<uses-feature>`declaration.

For a list of permissions that imply hardware features, see the documentation for the[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element#permissions-features)element.

syntax:
:

    ```xml
    <uses-permission android:name="string"
            android:maxSdkVersion="integer" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Specifies a system permission that the user must grant for the app to operate correctly. The user grants permissions when the application installs, on devices running Android 5.1 and lower, or while the app runs, on devices running Android 6.0 and higher.<br />

    For more information on permissions, see the[Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)section in the app manifest overview and the[Permissions on Android](https://developer.android.com/guide/topics/permissions)guide. A list of permissions defined by the base platform is at[android.Manifest.permission](https://developer.android.com/reference/android/Manifest.permission).

attributes:
:

    `android:name`
    :   The name of the permission. It can be a permission defined by the application with the[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)element, a permission defined by another application, or one of the standard system permissions, such as["android.permission.CAMERA"](https://developer.android.com/reference/android/Manifest.permission#CAMERA)or["android.permission.READ_CONTACTS"](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS). As these examples show, a permission name typically includes the package name as a prefix.

    `android:maxSdkVersion`

    :   The highest API level at which this permission is granted to your app. Setting this attribute is useful if the permission your app requires is no longer needed beginning at a certain API level.<br />

        For example, beginning with Android 4.4 (API level 19) it's no longer necessary for your app to request the[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)permission to write to its own application-specific directories on external storage, which are provided by[getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)).

        However, the permission*is required*for API level 18 and lower. So you can declare that this permission is needed only up to API level 18 with a declaration like the following:  

        ```xml
        <uses-permission
             android:name="android.permission.WRITE_EXTERNAL_STORAGE"
             android:maxSdkVersion="18" />
        ```

        This way, beginning with API level 19, the system no longer grants your app the`WRITE_EXTERNAL_STORAGE`permission.

        Added in API level 19.

introduced in:
:   API level 1

see also:
:
    - [<permission>](https://developer.android.com/guide/topics/manifest/permission-element)
    - [`<uses-permission-sdk-23>`](https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element)
    - [<uses-feature>](https://developer.android.com/guide/topics/manifest/uses-feature-element)