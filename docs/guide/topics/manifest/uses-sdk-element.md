---
title: https://developer.android.com/guide/topics/manifest/uses-sdk-element
url: https://developer.android.com/guide/topics/manifest/uses-sdk-element
source: md.txt
---

# &lt;uses-sdk>

Google Play uses the`<uses-sdk>`attributes declared in your app manifest to filter your app from devices that don't meet its platform version requirements. Before setting these attributes, make sure that you understand[Google Play filters](https://developer.android.com/google/play/filters).

syntax:
:

    ```xml
    <uses-sdk android:minSdkVersion="integer"
              android:targetSdkVersion="integer"
              android:maxSdkVersion="integer" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Lets you express an application's compatibility with one or more versions of the Android platform by means of an API level integer. The API level expressed by an application is compared to the API level of a given Android system, which can vary among different Android devices.

    Despite its name, this element is used to specify the API level,*not*the version number of the software development kit (SDK) or Android platform. The API level is always a single integer. You can't derive the API level from its associated Android version number. For example, it isn't the same as the major version or the sum of the major and minor versions.

    It's not possible to specify that an app either targets or requires a minor SDK version.

    Also read the document about[versioning your applications](https://developer.android.com/tools/publishing/versioning).

attributes:
:

    `android:minSdkVersion`

    :   An integer designating the minimum API level required for the application to run. The Android system prevents the user from installing the application if the system's API level is lower than the value specified in this attribute. Always declare this attribute.**Caution:** If you don't declare this attribute, the system assumes a default value of "1", which indicates that your application is compatible with all versions of Android. If it*isn't* , and you didn't declare the proper`minSdkVersion`, then when installed on a system with an incompatible API level, the application crashes during runtime when attempting to access the unavailable APIs. For this reason, be certain to declare the appropriate API level in the`minSdkVersion`attribute.

    `android:targetSdkVersion`
    :   An integer designating the API level that the application targets. If not set, the default value equals that given to`minSdkVersion`.

        This attribute informs the system that you have tested against the target version, and the system doesn't enable any compatibility behaviors to maintain your app's forward-compatibility with the target version. The application is still able to run on lower versions (down to`minSdkVersion`).

        As Android evolves with each new version, some behaviors and even appearances might change. However, if the API level of the platform is higher than the version declared by your app's`targetSdkVersion`, the system can enable compatibility behaviors so that your app continues to work the way you expect. You can disable such compatibility behaviors by specifying`targetSdkVersion`to match the API level of the platform on which it's running.

        For example, setting this value to "11" or higher lets the system apply the Holo default theme to your app when running on Android 3.0 or higher and also disables[screen compatibility mode](https://developer.android.com/guide/practices/screen-compat-mode)when running on larger screens, because support for API level 11 implicitly supports larger screens.

        There are many compatibility behaviors that the system can enable based on the value you set for this attribute. Several of these behaviors are described by the corresponding platform versions in the[Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES)reference.

        To maintain your application along with each Android release, increase the value of this attribute to match the latest API level, then thoroughly test your application on the corresponding platform version.

        *Introduced in: API level 4*

    :   An integer designating the maximum API level on which the application is designed to run.In Android 1.5, 1.6, 2.0, and 2.0.1, the system checks the value of this attribute when installing an application and when re-validating the application after a system update. In either case, if the application's`maxSdkVersion`attribute is lower than the API level used by the system itself, then the system doesn't let the application install. In the case of re-validation after system update, this effectively removes your application from the device.

        To illustrate how this attribute can affect your application after system updates, consider the following example:

        An application declaring`maxSdkVersion="5"`in its manifest is published on Google Play. A user whose device is running Android 1.6 (API level 4) downloads and installs the app. After a few weeks, the user receives an over-the-air system update to Android 2.0 (API level 5). After the update is installed, the system checks the application's`maxSdkVersion`and successfully re-validates it.

        The application functions as normal. However, some time later, the device receives another system update, this time to Android 2.0.1 (API level 6). After the update, the system can no longer re-validate the application because the system's own API level (6) is now higher than the maximum supported by the application (5). The system prevents the application from being visible to the user, in effect removing it from the device.

        **Warning:**We don't recommend declaring this attribute. First, there is no need to set the attribute as a means of blocking deployment of your application onto new versions of the Android platform as they are released. By design, new versions of the platform are fully backward-compatible. Your application works properly on new versions, provided it uses only standard APIs and follows development best practices. Second, in some cases declaring the attribute can result in your application being removed from users' devices after a system update to a higher API level. Most devices on which your application is likely to be installed receive periodic system updates over the air, so consider their effect on your application before setting this attribute.

        *Introduced in: API level 4*  
        Some versions of Android (beyond Android 2.0.1) don't check or enforce the`maxSdkVersion`attribute during installation or re-validation. Google Play continues to use the attribute as a filter, however, when presenting users with applications available for download.

introduced in:
:   API level 1

## What is API level?

API level is an integer value that uniquely identifies the framework API revision offered by a version of the Android platform.

The Android platform provides a framework API that applications can use to interact with the underlying Android system. The framework API consists of:

- A core set of packages and classes
- A set of XML elements and attributes for declaring a manifest file
- A set of XML elements and attributes for declaring and accessing resources
- A set of intents
- A set of permissions that applications can request, as well as permission enforcements included in the system

Each successive version of the Android platform can include updates to the Android application framework API that it delivers.

Updates to the framework API are designed so that the new API remains compatible with earlier versions of the API. That is, most changes in the API are additive and introduce new or replacement functionality. As parts of the API are upgraded, the older replaced parts are deprecated but aren't removed, so that existing applications can still use them.

In a very small number of cases, parts of the API are modified or removed, although typically such changes are only needed to support API robustness and application or system security. All other API parts from earlier revisions are carried forward without modification.

The framework API that an Android platform delivers is specified using an integer identifier called*API level*. Each Android platform version supports exactly one API level, although support is implicit for all earlier API levels (down to API level 1). The initial release of the Android platform provided API level 1, and subsequent releases have incremented the API level.

The following table specifies the API level supported by each version of the Android platform. For information about the relative numbers of devices that are running each version, see the[Distribution dashboard](https://developer.android.com/about/dashboards).

|                                          Platform Version                                           |                                 API level                                 |                                                      VERSION_CODE                                                       |                                           Notes                                            |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [Android 16](https://developer.android.com/about/versions/16)                                       | [36](https://developer.android.com/sdk/api_diff/36/changes "Diff Report") | [`BAKLAVA`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#BAKLAVA)                             | [Platform Highlights](https://developer.android.com/about/versions/16/summary)             |
| [Android 15](https://developer.android.com/about/versions/15)                                       | [35](https://developer.android.com/sdk/api_diff/35/changes "Diff Report") | [`VANILLA_ICE_CREAM`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#VANILLA_ICE_CREAM)         | [Platform Highlights](https://developer.android.com/about/versions/15/summary)             |
| [Android 14](https://developer.android.com/about/versions/14)                                       | [34](https://developer.android.com/sdk/api_diff/34/changes "Diff Report") | [`UPSIDE_DOWN_CAKE`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#UPSIDE_DOWN_CAKE)           | [Platform Highlights](https://developer.android.com/about/versions/14/summary)             |
| [Android 13](https://developer.android.com/about/versions/13)                                       | [33](https://developer.android.com/sdk/api_diff/33/changes "Diff Report") | [`TIRAMISU`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)                           | [Platform Highlights](https://developer.android.com/about/versions/13/summary)             |
| [Android 12](https://developer.android.com/about/versions/12)                                       | [32](https://developer.android.com/sdk/api_diff/32/changes "Diff Report") | [`S_V2`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S_V2)                                   | [Platform Highlights](https://developer.android.com/about/versions/12/12L/summary)         |
| [Android 12](https://developer.android.com/about/versions/12)                                       | [31](https://developer.android.com/sdk/api_diff/31/changes "Diff Report") | [`S`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S)                                         | [Platform Highlights](https://developer.android.com/about/versions/12/features)            |
| [Android 11](https://developer.android.com/about/versions/11)                                       | [30](https://developer.android.com/sdk/api_diff/30/changes "Diff Report") | [`R`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#R)                                         | [Platform Highlights](https://developer.android.com/about/versions/11/features)            |
| [Android 10](https://developer.android.com/about/versions/10)                                       | [29](https://developer.android.com/sdk/api_diff/29/changes "Diff Report") | [`Q`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#Q)                                         | [Platform Highlights](https://developer.android.com/about/versions/10/features)            |
| [Android 9](https://developer.android.com/about/versions/pie)                                       | [28](https://developer.android.com/sdk/api_diff/28/changes "Diff Report") | [`P`](https://developer.android.com/reference/android/os/Build.VERSION_CODES#P)                                         | [Platform Highlights](https://developer.android.com/about/versions/pie/android-9.0)        |
| [Android 8.1](https://developer.android.com/about/versions/oreo/android-8.1)                        | [27](https://developer.android.com/sdk/api_diff/27/changes "Diff Report") | [O_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#O_MR1)                                   | [Platform Highlights](https://developer.android.com/about/versions/oreo/android-8.1)       |
| [Android 8.0](https://developer.android.com/about/versions/oreo)                                    | [26](https://developer.android.com/sdk/api_diff/26/changes "Diff Report") | [O](https://developer.android.com/reference/android/os/Build.VERSION_CODES#O)                                           | [Platform Highlights](https://developer.android.com/about/versions/oreo/android-8.0)       |
| [Android 7.1.1 Android 7.1](https://developer.android.com/about/versions/nougat/android-7.1)        | [25](https://developer.android.com/sdk/api_diff/25/changes "Diff Report") | [N_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#N_MR1)                                   | [Platform Highlights](https://developer.android.com/about/versions/nougat)                 |
| [Android 7.0](https://developer.android.com/about/versions/nougat/android-7.0)                      | [24](https://developer.android.com/sdk/api_diff/24/changes "Diff Report") | [N](https://developer.android.com/reference/android/os/Build.VERSION_CODES#N)                                           | [Platform Highlights](https://developer.android.com/about/versions/nougat)                 |
| [Android 6.0](https://developer.android.com/about/versions/marshmallow/android-6.0)                 | [23](https://developer.android.com/sdk/api_diff/23/changes "Diff Report") | [M](https://developer.android.com/reference/android/os/Build.VERSION_CODES#M)                                           | [Platform Highlights](https://developer.android.com/about/versions/marshmallow)            |
| [Android 5.1](https://developer.android.com/about/versions/android-5.1)                             | [22](https://developer.android.com/sdk/api_diff/22/changes "Diff Report") | [LOLLIPOP_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#LOLLIPOP_MR1)                     | [Platform Highlights](https://developer.android.com/about/versions/lollipop)               |
| [Android 5.0](https://developer.android.com/about/versions/android-5.0)                             | [21](https://developer.android.com/sdk/api_diff/21/changes "Diff Report") | [LOLLIPOP](https://developer.android.com/reference/android/os/Build.VERSION_CODES#LOLLIPOP)                             | [Platform Highlights](https://developer.android.com/about/versions/lollipop)               |
| Android 4.4W                                                                                        | [20](https://developer.android.com/sdk/api_diff/20/changes "Diff Report") | [KITKAT_WATCH](https://developer.android.com/reference/android/os/Build.VERSION_CODES#KITKAT_WATCH)                     | KitKat for Wearables Only                                                                  |
| [Android 4.4](https://developer.android.com/about/versions/android-4.4)                             | [19](https://developer.android.com/sdk/api_diff/19/changes "Diff Report") | [KITKAT](https://developer.android.com/reference/android/os/Build.VERSION_CODES#KITKAT)                                 | [Platform Highlights](https://developer.android.com/about/versions/kitkat)                 |
| [Android 4.3](https://developer.android.com/about/versions/android-4.3)                             | [18](https://developer.android.com/sdk/api_diff/18/changes "Diff Report") | [JELLY_BEAN_MR2](https://developer.android.com/reference/android/os/Build.VERSION_CODES#JELLY_BEAN_MR2)                 | [Platform Highlights](https://developer.android.com/about/versions/jelly-bean)             |
| [Android 4.2, 4.2.2](https://developer.android.com/about/versions/android-4.2)                      | [17](https://developer.android.com/sdk/api_diff/17/changes "Diff Report") | [JELLY_BEAN_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#JELLY_BEAN_MR1)                 | [Platform Highlights](https://developer.android.com/about/versions/jelly-bean#android-42)  |
| [Android 4.1, 4.1.1](https://developer.android.com/about/versions/android-4.1)                      | [16](https://developer.android.com/sdk/api_diff/16/changes "Diff Report") | [JELLY_BEAN](https://developer.android.com/reference/android/os/Build.VERSION_CODES#JELLY_BEAN)                         | [Platform Highlights](https://developer.android.com/about/versions/jelly-bean#android-41)  |
| [Android 4.0.3, 4.0.4](https://developer.android.com/about/versions/android-4.0.3)                  | [15](https://developer.android.com/sdk/api_diff/15/changes "Diff Report") | [ICE_CREAM_SANDWICH_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#ICE_CREAM_SANDWICH_MR1) | [Platform Highlights](https://developer.android.com/about/versions/android-4.0-highlights) |
| [Android 4.0, 4.0.1, 4.0.2](https://developer.android.com/about/versions/android-4.0)               | [14](https://developer.android.com/sdk/api_diff/14/changes "Diff Report") | [ICE_CREAM_SANDWICH](https://developer.android.com/reference/android/os/Build.VERSION_CODES#ICE_CREAM_SANDWICH)         | [Platform Highlights](https://developer.android.com/about/versions/android-4.0-highlights) |
| [Android 3.2](https://developer.android.com/about/versions/android-3.2)                             | [13](https://developer.android.com/sdk/api_diff/13/changes "Diff Report") | [HONEYCOMB_MR2](https://developer.android.com/reference/android/os/Build.VERSION_CODES#HONEYCOMB_MR2)                   |                                                                                            |
| [Android 3.1.x](https://developer.android.com/about/versions/android-3.1)                           | [12](https://developer.android.com/sdk/api_diff/12/changes "Diff Report") | [HONEYCOMB_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#HONEYCOMB_MR1)                   | [Platform Highlights](https://developer.android.com/about/versions/android-3.1-highlights) |
| [Android 3.0.x](https://developer.android.com/about/versions/android-3.0)                           | [11](https://developer.android.com/sdk/api_diff/11/changes "Diff Report") | [HONEYCOMB](https://developer.android.com/reference/android/os/Build.VERSION_CODES#HONEYCOMB)                           | [Platform Highlights](https://developer.android.com/about/versions/android-3.0-highlights) |
| [Android 2.3.4 Android 2.3.3](https://developer.android.com/about/versions/android-2.3.3)           | [10](https://developer.android.com/sdk/api_diff/10/changes "Diff Report") | [GINGERBREAD_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#GINGERBREAD_MR1)               | [Platform Highlights](https://developer.android.com/about/versions/android-2.3-highlights) |
| [Android 2.3.2 Android 2.3.1 Android 2.3](https://developer.android.com/about/versions/android-2.3) | [9](https://developer.android.com/sdk/api_diff/9/changes "Diff Report")   | [GINGERBREAD](https://developer.android.com/reference/android/os/Build.VERSION_CODES#GINGERBREAD)                       | [Platform Highlights](https://developer.android.com/about/versions/android-2.3-highlights) |
| [Android 2.2.x](https://developer.android.com/about/versions/android-2.2)                           | [8](https://developer.android.com/sdk/api_diff/8/changes "Diff Report")   | [FROYO](https://developer.android.com/reference/android/os/Build.VERSION_CODES#FROYO)                                   | [Platform Highlights](https://developer.android.com/about/versions/android-2.2-highlights) |
| [Android 2.1.x](https://developer.android.com/about/versions/android-2.1)                           | [7](https://developer.android.com/sdk/api_diff/7/changes "Diff Report")   | [ECLAIR_MR1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#ECLAIR_MR1)                         | [Platform Highlights](https://developer.android.com/about/versions/android-2.0-highlights) |
| [Android 2.0.1](https://developer.android.com/about/versions/android-2.0.1)                         | [6](https://developer.android.com/sdk/api_diff/6/changes "Diff Report")   | [ECLAIR_0_1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#ECLAIR_0_1)                         | [Platform Highlights](https://developer.android.com/about/versions/android-2.0-highlights) |
| [Android 2.0](https://developer.android.com/about/versions/android-2.0)                             | [5](https://developer.android.com/sdk/api_diff/5/changes "Diff Report")   | [ECLAIR](https://developer.android.com/reference/android/os/Build.VERSION_CODES#ECLAIR)                                 | [Platform Highlights](https://developer.android.com/about/versions/android-2.0-highlights) |
| [Android 1.6](https://developer.android.com/about/versions/android-1.6)                             | [4](https://developer.android.com/sdk/api_diff/4/changes "Diff Report")   | [DONUT](https://developer.android.com/reference/android/os/Build.VERSION_CODES#DONUT)                                   | [Platform Highlights](https://developer.android.com/about/versions/android-1.6-highlights) |
| [Android 1.5](https://developer.android.com/about/versions/android-1.5)                             | [3](https://developer.android.com/sdk/api_diff/3/changes "Diff Report")   | [CUPCAKE](https://developer.android.com/reference/android/os/Build.VERSION_CODES#CUPCAKE)                               | [Platform Highlights](https://developer.android.com/about/versions/android-1.5-highlights) |
| [Android 1.1](https://developer.android.com/about/versions/android-1.1)                             | 2                                                                         | [BASE_1_1](https://developer.android.com/reference/android/os/Build.VERSION_CODES#BASE_1_1)                             |                                                                                            |
| Android 1.0                                                                                         | 1                                                                         | [BASE](https://developer.android.com/reference/android/os/Build.VERSION_CODES#BASE)                                     |                                                                                            |

## Uses of API level in Android

The API level identifier serves a key role in helping ensure the best possible experience for users and application developers:

- It lets the Android platform describe the maximum framework API revision that it supports.
- It lets applications describe the framework API revision that they require.
- It lets the system negotiate the installation of applications on the user's device so that version-incompatible applications aren't installed.

Each Android platform version stores its API level identifier internally, in the Android system itself.

Applications can use a manifest element provided by the framework API---`<uses-sdk>`---to describe the minimum and maximum API levels under which they are able to run as well as the preferred API level that they are designed to support. The element offers three key attributes:

- `android:minSdkVersion`: the minimum API level on which the application is able to run. The default value is "1".
- `android:targetSdkVersion`: the API level on which the application is designed to run. In some cases, this lets the application use manifest elements or behaviors defined in the target API level, rather than being restricted to using only those defined for the minimum API level.
- `android:maxSdkVersion`: the maximum API level on which the application is able to run.**Important:** Read the[information about this attribute](https://developer.android.com/guide/topics/manifest/uses-sdk-element#maxsdk)on this page before using it.

For example, to specify the minimum system API level that an application requires in order to run, the application includes in its manifest a`<uses-sdk>`element with a`android:minSdkVersion`attribute. The value of`android:minSdkVersion`is the integer corresponding to the API level of the earliest version of the Android platform under which the application can run.

When the user attempts to install an application, or when revalidating an application after a system update, the Android system first checks the`<uses-sdk>`attributes in the application's manifest and compares the values against its own internal API level. The system lets the installation begin only if these conditions are met:

- If a`android:minSdkVersion`attribute is declared, its value is less than or equal to the system's API level integer. If not declared, the system assumes that the application requires API level 1.
- If a`android:maxSdkVersion`attribute is declared, its value is equal to or greater than the system's API level integer. If not declared, the system assumes that the application has no maximum API level. Read the[description of this attribute](https://developer.android.com/guide/topics/manifest/uses-sdk-element#maxsdk)for more information about how the system handles it.

When declared in an application's manifest, a`<uses-sdk>`element might look like this:  

```xml
<manifest>
  <uses-sdk android:minSdkVersion="5" />
  ...
</manifest>
```

The principal reason that an application declares an API level in`android:minSdkVersion`is to tell the Android system that it uses APIs that were*introduced*in the API level specified.

If the application somehow installs on a platform with a lower API level, then it crashes at runtime when it tries to access APIs that don't exist. The system prevents this outcome by not letting the application install if the lowest API level it requires is higher than that of the platform version on the target device.

## Development considerations

The following sections provide information related to API level that you need to consider when developing your application.

### Application forward compatibility

Android applications are generally forward-compatible with new versions of the Android platform.

Because almost all changes to the framework API are additive, an Android application developed using any given version of the API, as specified by its API level, is forward-compatible with later versions of the Android platform and higher API levels. The application can run on all later versions of the Android platform, except in isolated cases where the application uses a part of the API that is later removed for some reason.

Forward compatibility is important because many Android-powered devices receive over-the-air (OTA) system updates. The user might install your application and use it successfully, then later receive an OTA update to a new version of the Android platform. Once the update is installed, your application runs in a new runtime version of the environment, but one that still has the API and system capabilities that your application depends on.

Changes*below*the API, such those in the underlying system itself, can affect your application when it is run in the new environment. It's important for you, as the application developer, to understand how the application looks and behaves in each system environment.

To help you test your application on various versions of the Android platform, the Android SDK includes multiple platforms that you can download. Each platform includes a compatible system image that you can run in an AVD to test your application.

### Application backward compatibility

Android applications aren't necessarily backward-compatible with versions of the Android platform older than the version against which they were compiled.

Each new version of the Android platform can include new framework APIs, such as those that give applications access to new platform capabilities or replace existing API parts. The new APIs are accessible to applications when running on the new platform and also when running on later versions of the platform, as specified by API level. But because earlier versions of the platform don't include the new APIs, applications that use the new APIs can't run on those platforms.

Although an Android-powered device isn't likely to be downgraded to a previous version of the platform, it's important to realize that there are likely to be many devices in the field that run earlier versions of the platform. Even among devices that receive OTA updates, some might lag and might not receive an update for a significant amount of time.

### Select a platform version and API level

When you are developing your application, you choose the platform version against which you compile the application. In general, compile your application against the lowest possible version of the platform that your application can support.

You can determine the lowest possible platform version by compiling the application against successively lower build targets. After you determine the lowest version, create an AVD using the corresponding platform version and API level, and fully test your application. Make sure to declare a`android:minSdkVersion`attribute in the application's manifest and set its value to the API level of the platform version.

### Declare a minimum API level

If you build an application that uses APIs or system features introduced in the latest platform version, set the`android:minSdkVersion`attribute to the API level of the latest platform version. This is so that users are only able to install your application if their devices are running a compatible version of the Android platform. In turn, this helps ensure that your application can function properly on their devices.

If your application uses APIs introduced in the latest platform version but does*not* declare a`android:minSdkVersion`attribute, then it runs properly on devices running the latest version of the platform, but*not*on devices running earlier versions of the platform. In the latter case, the application crashes at runtime when it tries to use APIs that don't exist on the earlier versions.

### Test against higher API levels

After compiling your application, make sure to test it on the platform specified in the application's`android:minSdkVersion`attribute. To do so, create an AVD that uses the platform version required by your application. Additionally, to check forward-compatibility, run and test the application on all platforms that use a higher API level than that used by your application.

The Android SDK includes multiple platform versions that you can use, including the latest version, and provides an updater tool that you can use to download other platform versions as necessary.

To access the updater, use the`android`command-line tool, located in the \<sdk\>/tools directory. You can launch the SDK updater by executing`android sdk`. You can also double-click the`android.bat`(Windows) or`android`(OS X/Linux) file.

To run your application against different platform versions in the emulator, create an AVD for each platform version that you want to test. For more information about AVDs, see[Create and manage virtual devices](https://developer.android.com/tools/devices). If you are using a physical device for testing, make sure that you know the API level of the Android platform it runs. See the table in this document for a list of platform versions and their API levels.

## Filter the reference documentation by API level

Android platform reference documentation pages offer an "API level" control in the top-left area of each page. You can use the control to show documentation only for parts of the API that are actually accessible to your application, based on the API level that it specifies in the`android:minSdkVersion`attribute of its manifest file.

To use filtering, select the API level specified by your application from the menu. APIs introduced in a later API level are then grayed out and their content is masked, since they aren't accessible to your application.

Filtering by API level in the documentation doesn't provide a view of what is new or introduced in each API level. It provides a way to view the entire API associated with a given API level, while excluding API elements introduced in later API levels.

To return to viewing the full documentation, select**REL**, at the top of the API level menu. By default, API level filtering is disabled, so that you can view the full framework API, regardless of API level.

The reference documentation for individual API elements specifies the API level at which each element is introduced. The API level for packages and classes is specified as "Added in API level" at the top-right corner of the content area on each documentation page. The API level for class members is specified in their detailed description headers, at the right margin.