---
title: https://developer.android.com/guide/topics/manifest/manifest-element
url: https://developer.android.com/guide/topics/manifest/manifest-element
source: md.txt
---

# &lt;manifest>

syntax:
:

    ```xml
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
              package="string"
              android:sharedUserId="string"
              android:sharedUserLabel="string resource" 
              android:sharedUserMaxSdkVersion="integer"
              android:versionCode="integer"
              android:versionName="string"
              android:installLocation=["auto" | "internalOnly" | "preferExternal"] >
        ...
    </manifest>
    ```

contained in:
:   *none*

must contain:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)

can contain:
:   [<attribution>](https://developer.android.com/guide/topics/manifest/attribution-element)  
    [<compatible-screens>](https://developer.android.com/guide/topics/manifest/compatible-screens-element)  
    [<instrumentation>](https://developer.android.com/guide/topics/manifest/instrumentation-element)  
    [<permission>](https://developer.android.com/guide/topics/manifest/permission-element)  
    [<permission-group>](https://developer.android.com/guide/topics/manifest/permission-group-element)  
    [<permission-tree>](https://developer.android.com/guide/topics/manifest/permission-tree-element)  
    [<queries>](https://developer.android.com/guide/topics/manifest/queries-element)  
    [<supports-gl-texture>](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element)  
    [<supports-screens>](https://developer.android.com/guide/topics/manifest/supports-screens-element)  
    [<uses-configuration>](https://developer.android.com/guide/topics/manifest/uses-configuration-element)  
    [<uses-feature>](https://developer.android.com/guide/topics/manifest/uses-feature-element)  
    [<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)  
    [<uses-permission-sdk-23>](https://developer.android.com/guide/topics/manifest/uses-permission-sdk-23-element)  
    [<uses-sdk>](https://developer.android.com/guide/topics/manifest/uses-sdk-element)

description:
:   The root element of the`AndroidManifest.xml`file. It must contain an[<application>](https://developer.android.com/guide/topics/manifest/application-element)element and specify`xmlns:android`and`package`attributes.

attributes:
:

    `xmlns:android`
    :   Defines the Android namespace. This attribute is always set to`"http://schemas.android.com/apk/res/android"`.

    `package`
    :   The value of the`package`attribute in the APK's manifest file represents your app's universally unique application ID. It is formatted as a full Java-language-style package name for the Android app. The name can contain uppercase or lowercase letters, numbers, and underscores ('_'). However, individual package name parts can only start with letters.

        Be careful not to change the`package`value, since that essentially creates a new app. Users of the previous version of your app don't receive an update and can't transfer their data between the old and new versions.

        In the Gradle-based build system, starting with AGP 7.3, don't set the`package`value in the source manifest file directly. For more information, see[Set the application ID](https://developer.android.com/studio/build/configure-app-module#set-application-id).

    `android:sharedUserId`

    :   **This constant is deprecated as of API level 29.**   
        Shared user IDs cause non-deterministic behavior within the package manager. As such, their use is strongly discouraged and might be removed in a future version of Android. Instead, use proper communication mechanisms, such as services and content providers, to facilitate interoperability between shared components. Existing apps can't remove this value, as migrating off a shared user ID isn't supported. In these apps, add[`android:sharedUserMaxSdkVersion="32"`](https://developer.android.com/guide/topics/manifest/manifest-element#uidmaxsdk)to avoid using shared user ID on new user installs.

        The name of a Linux user ID that is shared with other apps. By default, Android assigns each app its own unique user ID. However, if this attribute is set to the same value for two or more apps, they all share the same ID, provided that their certificate sets are identical. Apps with the same user ID can access each other's data and, if desired, run in the same process.

    `android:targetSandboxVersion`
    :   The target sandbox for this app to use. The higher the sandbox version number, the higher the level of security. Its default value is`1`; you can also set it to`2`. Setting this attribute to`2`switches the app to a different SELinux sandbox.

        The following restrictions apply to a level-2 sandbox:

        - The default value of[`usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic)in the Network Security Config is false.
        - Uid sharing isn't permitted.

        For Android Instant Apps targeting Android 8.0 (API level 26) or higher, this attribute is set to`2`. You can set the sandbox level in the installed version of your app to the less restrictive level`1`. But if you do so, your app doesn't persist app data from the instant app to the installed version of your app. You must set the installed app's sandbox value to`2`for the data to persist from the instant app to the installed version.

        Once an app is installed, you can only update its target sandbox value to a higher value. To downgrade the target sandbox value, uninstall the app and replace it with a version whose manifest contains a lower value for this attribute.

    `android:sharedUserLabel`

    :   **This constant is deprecated as of API level 29.**   
        Shared user IDs cause non-deterministic behavior within the package manager. As such, their use is strongly discouraged and might be removed in a future version of Android. Instead, use proper communication mechanisms, such as services and content providers, to facilitate interoperability between shared components. Existing apps can't remove this value, as migrating off a shared user ID is not supported.

        A user-readable label for the shared user ID. The label is set as a reference to a string resource. It can't be a raw string.

        This attribute was introduced in API level 3. It is meaningful only if the[sharedUserId](https://developer.android.com/guide/topics/manifest/manifest-element#uid)attribute is also set.

    `android:sharedUserMaxSdkVersion`

    :   Shared user IDs cause non-deterministic behavior within the package manager. As such, their use is strongly discouraged and might be removed in a future version of Android. Instead, use proper communication mechanisms, such as services and content providers, to facilitate interoperability between shared components.

        The maximum SDK version where the system still uses`android:sharedUserId`. If your app is newly installed on a device running an SDK version higher than the specified value, your app behaves as if you never defined`android:sharedUserId`.

        This attribute was introduced in API level 33. It is meaningful only if the[sharedUserId](https://developer.android.com/guide/topics/manifest/manifest-element#uid)attribute is also set.

    `android:versionCode`
    :   An internal version number. This number is used only to determine whether one version is more recent than another, with higher numbers indicating more recent versions. This isn't the version number shown to users, which is set by the`versionName`attribute.

        The value is set as a positive integer greater than 0. You can define it however you want, as long as each successive version has a higher number. For example, it can be a build number, or you can translate a version number in "x.y" format to an integer by encoding the "x" and "y" separately in the lower and upper 16 bits. Or you can increase the number by one each time a new version is released.

    `android:versionName`
    :   The version number shown to users. This attribute is set as a raw string or as a reference to a string resource. The string has no other purpose than to display to users. The`versionCode`attribute holds the significant version number used internally.

    `android:installLocation`
    :   The default install location for the app. The following keyword strings are accepted:

        |       Value        |                                                                                                                                                      Description                                                                                                                                                      |
        |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | `"internalOnly"`   | The app installs on internal device storage only. If this is set, the app never installs on external storage, such as an SD card. If the internal storage is full, then the system doesn't install the app. This is the default behavior if you don't define`android:installLocation`.                                |
        | `"auto"`           | The app can install on external storage, but the system installs the app on internal storage by default. If the internal storage is full, then the system installs it on the external storage. Once installed, the user can move the app to either internal or external storage through the system settings.          |
        | `"preferExternal"` | The app prefers to be installed on external storage. There is no guarantee that the system honors this request. The app might install on internal storage if the external media is unavailable or full. Once installed, the user can move the app to either internal or external storage through the system settings. |

        **Note:** By default, your app installs on internal storage and can't install on external storage unless you define this attribute to be either`"auto"`or`"preferExternal"`.

        When an app installs on external storage:

        - The APK file is saved to the external storage, but any app data, such as databases, still saves on the internal device memory.
        - The container in which the APK file is saved is encrypted with a key that lets the app operate only on the device that installed it. The user can't transfer the SD card to another device and use apps installed on the card. Multiple SD cards can be used with the same device.
        - At the user's request, the app can be moved to the internal storage.

        The user might also request to move an app from the internal storage to the external storage. However, the system doesn't let the user move the app to external storage if this attribute is set to`"internalOnly"`, which is the default setting.

        For more information about using this attribute, including how to maintain backward compatibility, see[App install location](https://developer.android.com/guide/topics/data/install-location).

        Introduced in: API level 8.

introduced in:
:   API level 1 for all attributes, unless noted otherwise in the attribute description.

see also:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)