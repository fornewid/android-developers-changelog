---
title: https://developer.android.com/guide/practices/compatibility
url: https://developer.android.com/guide/practices/compatibility
source: md.txt
---

Android is designed to run on many different devices, such as phones,
tablets, and televisions. The range of devices provides a huge potential
audience for your app. For your app to be successful on all devices, it must
tolerate feature variability and provide a flexible user interface that adapts
to different screen configurations.

To help with device compatibility, Android provides a dynamic app framework
in which you can provide configuration-specific
[app resources](https://developer.android.com/guide/topics/resources/overview) in static
files, such as different XML layouts for different screen sizes. Android then
loads the appropriate resources based on the current device configuration. With
forethought to your app design and additional app resources, you can publish a
single application package (APK) that optimizes the user experience on a variety
of devices.

If necessary, however, you can specify your app's feature requirements and
control which types of devices can install your app from the Google Play Store.
This document explains how you can control which devices have access to your
apps and how to prepare your apps to reach the right audience.

## What does "compatibility" mean?

With regard to Android development, there are two types of compatibility:
*device compatibility* and *app compatibility*.

Because Android is an open-source project, any hardware manufacturer can
build a device that runs the Android operating system. But a device is
"Android compatible" only if it can correctly run apps written for the
*Android execution environment* . The exact details of the Android
execution environment are defined by the
[Android
compatibility program](https://source.android.com/compatibility/overview.html). Each device must pass the Compatibility Test Suite
(CTS) to be considered compatible.

As an app developer, you don't need to worry about whether a device is
Android compatible, because only devices that are Android compatible include
Google Play Store. So, if a user installs your app from Google Play Store, they
are using an Android compatible device.

However, you need to consider whether your app is compatible with each
potential device configuration. Because Android runs on a wide range of device
configurations, some features aren't available on all devices. For example, some
devices might not include a compass sensor. If your app's core functionality
requires a compass sensor, then your app is compatible only with devices that
include that feature.

## Control your app's availability to devices

Android supports a variety of features your app can leverage through platform
APIs. Some features are hardware based, such as a compass sensor; some are
software based, such as app widgets; and some depend on the platform version.
Not every device supports every feature, so you might need to control your app's
availability to devices based on your app's required features.

To achieve the largest user base possible for your app, support as many
device configurations as possible using a single APK or AAB. In most situations,
you can do so by disabling optional features at runtime and
[providing app
resources](https://developer.android.com/guide/topics/resources/providing-resources) with alternatives for different configurations, such as different
layouts for different screen sizes. If necessary, you can restrict your app's
availability to certain devices through Google Play Store based on the following
device characteristics:

- [Device features](https://developer.android.com/guide/practices/compatibility#Features)
- [Platform version](https://developer.android.com/guide/practices/compatibility#Versions)
- [Screen configuration](https://developer.android.com/guide/practices/compatibility#Screens)

### Device features

To manage your app's availability based on device features, Android defines
*feature IDs* for any hardware or software feature that might not be
available on all devices. For example, the feature ID for the compass sensor is
[FEATURE_SENSOR_COMPASS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_COMPASS),
and the feature ID for app widgets is
[FEATURE_APP_WIDGETS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_APP_WIDGETS).

If necessary, you can prevent users from installing your app when their
devices don't provide a necessary feature by declaring the feature using a
[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)
element in your app's
[manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro).

For example, if your app doesn't make sense on a device that lacks a compass
sensor, you can declare the compass sensor as a requirement with the following
manifest tag:  

```xml
<manifest ... >
    <uses-feature android:name="android.hardware.sensor.compass"
                  android:required="true" />
    ...
</manifest>
```

Google Play Store compares the features that your app requires to the
features available on each user's device to determine whether your app is
compatible with each device. If the device doesn't have all the features your
app requires, the user can't install your app.

However, if your app's primary functionality doesn't *require* a
device feature, set the
[`required`](https://developer.android.com/guide/topics/manifest/uses-feature-element#required)
attribute to `"false"` and check for the device feature at runtime.
If the app feature isn't available on the current device, gracefully degrade the
corresponding app feature. For example, you can query whether a feature is
available by calling
[hasSystemFeature()](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))
like this:  

### Kotlin

```kotlin
if (!packageManager.hasSystemFeature(PackageManager.FEATURE_SENSOR_COMPASS)) {
    // This device doesn't have a compass. Turn off the compass feature.
    disableCompassFeature()
}
```

### Java

```java
PackageManager pm = getPackageManager();
if (!pm.hasSystemFeature(PackageManager.FEATURE_SENSOR_COMPASS)) {
    // This device doesn't have a compass. Turn off the compass feature.
    disableCompassFeature();
}
```

For information about all the filters you can use to control the availability
of your app through Google Play Store, see the
[Filters on Google Play](https://developer.android.com/google/play/filters)
documentation.
| **Note:** Some [system permissions](https://developer.android.com/guide/topics/permissions) implicitly require the availability of a device feature. For example, if your app requests permission to access [BLUETOOTH](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH), this implicitly requires the [FEATURE_BLUETOOTH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BLUETOOTH) device feature. You can disable filtering based on this feature and make your app available to devices without Bluetooth by setting the `required` attribute to `"false"` in the `<uses-feature>` tag. For more information about implicitly required device features, read [Permissions
| that imply feature requirements](https://developer.android.com/guide/topics/manifest/uses-feature-element#permissions).

### Platform version

Different devices might run different versions of the Android platform, such
as Android 12 or Android 13. Each successive platform version often adds APIs
not available in the previous version. To indicate which set of APIs are
available, each platform version specifies an
[API level](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels).
For example, Android 12 is API level 31, and Android 13 is API level 33.

You must specify the
[`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)
and
[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)
values in your `build.gradle` file:  

### Kotlin

```kotlin
android {
    defaultConfig {
        applicationId = "com.example.myapp"

        // Defines the minimum API level required to run the app.
        minSdkVersion(30)

        // Specifies the API level used to test the app.
        targetSdkVersion(36)
        ...
    }
}
```

### Groovy

```groovy
android {
    defaultConfig {
        applicationId 'com.example.myapp'

        // Defines the minimum API level required to run the app.
        minSdkVersion 30

        // Specifies the API level used to test the app.
        targetSdkVersion 36
        ...
    }
}
```

For more information about the `build.gradle` file, read
[Configure your build](https://developer.android.com/studio/build).

Each successive version of Android provides compatibility for apps built
using the APIs from previous platform versions, so your app is compatible with
future versions of Android while using the documented Android APIs.
| **Note:** The `targetSdkVersion` attribute doesn't prevent your app from being installed on platform versions that are higher than the specified value, but it's important because it indicates to the system whether your app inherits behavior changes in newer versions. If you don't update the `targetSdkVersion` to the latest version, the system assumes that your app requires backward compatibility when running on the latest version.

However, if your app uses APIs added in a more recent platform version, but
doesn't require them for its primary functionality, check the API level at
runtime and gracefully degrade the corresponding features when the API level is
too low. In this case, set the `minSdkVersion` to the lowest value
possible for your app's primary functionality, then compare the current system's
version,
[SDK_INT](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT),
to the codename constant in
[Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES)
that corresponds to the API level you want to check, as shown in the following
example:  

### Kotlin

```kotlin
if (Build.VERSION.SDK_INT < Build.VERSION_CODES.HONEYCOMB) {
    // Running on something older than API level 11, so disable
    // the drag and drop features that use ClipboardManager APIs.
    disableDragAndDrop()
}
```

### Java

```java
if (Build.VERSION.SDK_INT < Build.VERSION_CODES.HONEYCOMB) {
    // Running on something older than API level 11, so disable
    // the drag and drop features that use ClipboardManager APIs.
    disableDragAndDrop();
}
```

### Screen configuration

Android runs on devices of various sizes such as phones, tablets, and TVs. To
categorize devices by their screen type, Android defines two characteristics for
each device: screen size (the physical size of the screen) and screen density
(the physical density of the pixels on the screen, known as
DPI). To simplify the different
configurations, Android generalizes these variants into groups that make them
easier to target:

- Four generalized sizes: small, normal, large, and xlarge
- Several generalized densities: mdpi (medium), hdpi (high), xhdpi (extra high), xxhdpi (extra-extra high), and others

By default, your app is compatible with all screen sizes and densities,
because the system makes adjustments to your UI layout and image resources as
necessary for each screen. Provide optimized bitmap images for common screen
densities.

Optimize the user experience by using flexible layouts as much as possible.
Where there are layouts for large configuration changes, such as portrait and
landscape, or large versus small window sizes, consider providing alternate
layouts that are flexible to smaller changes in the configuration. This improves
the user experience on form factors such as tablets, phones, and foldables. It
also helps when windows change size in multi-window mode.

For information about how to create alternative resources for different
screens and how to restrict your app to certain screen sizes when necessary,
read the
[screen compatibility
overview](https://developer.android.com/training/basics/supporting-devices/screens) and see the
[large screen app
quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality).

## Control your app's availability for business reasons

In addition to restricting your app's availability based on device
characteristics, you might need to restrict your app's availability for business
or legal reasons. For this type of situation, Google Play Store provides
filtering options in the Play Console that let you control your app's
availability for nontechnical reasons such as user locale or wireless
carrier.

Filtering for technical compatibility---such as required hardware
components---is always based on information contained within your APK or AAB
file. But filtering for nontechnical reasons---such as geographic
locale---is always handled in the
[Google Play Console](https://developer.android.com/distribute/console).

## Additional resources:

[App resources overview](https://developer.android.com/guide/topics/resources/providing-resources)
:   Information about how Android apps are structured to separate app
    resources from the app code, including how you can provide alternative
    resources for specific device configurations.

[Filters on Google Play](https://developer.android.com/google/play/filters)
:   Information about the different ways Google Play Store can prevent your
    app from being installed on different devices.

[Permissions on Android](https://developer.android.com/guide/topics/permissions)
:   How Android restricts app access to certain APIs with a permission system
    that requires the user's consent for your app to use those APIs.