---
title: https://developer.android.com/guide/sdk-extensions
url: https://developer.android.com/guide/sdk-extensions
source: md.txt
---

# SDK Extensions leverage[modular system components](https://source.android.com/docs/core/ota/modular-system)to add APIs to the public SDK for certain previously released API levels. These APIs are delivered to devices when end-users receive module updates through[Google Play system updates](https://support.google.com/product-documentation/answer/11462338). App developers can utilize these APIs in their apps to provide additional functionality that wasn't originally available in the SDK for these previous versions of Android.

## API Versioning

Starting with Android 11 (API level 30), Android devices include a set of SDK Extensions. When new APIs are added, they are included in an API level, but may also be included in an SDK extension of a particular version. For example, the[`ACTION_PICK_IMAGES`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_PICK_IMAGES)API for Photo Picker was added to the public SDK in Android 13 (API level 33), but is also available through SDK extensions starting in R Extensions Version 2.[SDK Extension names](https://developer.android.com/guide/sdk-extensions#extension-names)correspond to an integer constant--either a constant from[`Build.VERSION_CODES`](https://developer.android.com/reference/android/os/Build.VERSION_CODES), or one defined in the`SdkExtensions`class (such as[`SdkExtensions.AD_SERVICES`](https://developer.android.com/reference/android/os/ext/SdkExtensions#AD_SERVICES)).

## Determine which SDK Extensions to use

Before you can use SDK Extension APIs, you first need to determine which SDKs include the APIs that support your app's use cases.

The API reference pages for SDK Extension APIs specify the earliest SDK extension version that your app can use to access an API. If the documentation also specifies an Android platform version (referenced by API level), then that API is also available for all devices running that version of Android or higher.

For example,`ACTION_PICK_IMAGES`is available generally in the public SDK starting with Android 13 (API level 33), but is also available on devices as far back as Android 11 (API level 30) so long as the device has at least R Extensions Version 2:

![APIs that are part of SDK Extensions show their extension version in the API reference docs](https://developer.android.com/static/images/guide/sdk-extensions/extension-version.png)

To use this API, you need to compile against an SDK that is at least API level 33, or Extension Level at least 2.

To use an extension SDK, follow these steps:

1. Look up the minimum extensions version that you need by checking the feature documentation and API reference for the APIs that you want to use.
2. After you determine the required extension version for your feature set, open the SDK Manager in Android Studio.
3. Select the Android SDK Platform entry with the corresponding extension version (or a higher version, as the APIs are additive). For example: Android SDK Platform 33, Extension Level 4.
4. Declare these values in your app's`build.gradle.kts`or`build.gradle`file:

   ### Groovy

   ```groovy
   android {
       compileSdk 33
       compileSdkExtension 4
       ...
   }
   ```

   ### Kotlin

   ```kotlin
   android {
       compileSdk = 33
       compileSdkExtension = 4
       ...
   }
   ```

## Check whether SDK Extensions are available

Your app can check what SDK Extension versions are available at runtime, and while developing you can look up the extension versions using Android Debug Bridge (adb) commands, as described in the following sections.

### Check at runtime

Your app can check at runtime whether SDK Extensions are available for a given platform version using the[`getExtensionVersion()`](https://developer.android.com/reference/android/os/ext/SdkExtensions#getExtensionVersion(int))method. For example, the following code would check whether extension version 2 or higher for the Android 11 (API level 30) SDK Extension is available:  

### Kotlin

```kotlin
fun isPhotoPickerAvailable(): Boolean {
    return SdkExtensions.getExtensionVersion(Build.VERSION_CODES.R) >= 2
    // Safely use extension APIs that are available with Android 11 (API level 30) Extensions Version 2, such as Photo Picker.
}
```

### Java

```java
public static final boolean isPhotoPickerAvailable() {
    return SdkExtensions.getExtensionVersion(Build.VERSION_CODES.R) >= 2;
}
```

This is similar to doing a check based on[`Build.VERSION.SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT):  

### Kotlin

```kotlin
fun isPhotoPickerAvailable(): Boolean {
    return Build.VERSION.SDK_INT >= 33
}
```

### Java

```java
public static final boolean isPhotoPickerAvailable() {
    return Build.VERSION.SDK_INT >= 33;
}
```

This`SDK_INT`check is still safe and valid, but`isPhotoPickerAvailable`would return false on some devices even though the extension API is available. As a result, the`SDK_INT`check is not optimal, and the extension version check is a better way to check for API availability. All devices with`SDK_INT`greater than or equal to`33`(Android 13 or higher) have the Photo Picker APIs in the public SDK, but there are devices with`SDK_INT`less than 33 (such as Android 11, 12, and 12L) that could also access the APIs if they have R extension versions of at least`2`.

In this case, using an extension version check can help your app deliver additional functionality to more users. See[SDK Extension names and constants](https://developer.android.com/guide/sdk-extensions#extension-names)for a list of all the constants that you can use to check for certain SDK Extensions on a device.

#### Ad Services Extensions

Similar to the general set of SDK Extensions, the`AdServices`API reference sometimes indicates that an API is part of an "Ad Services Extensions" version. Unlike the general SDK Extensions, Ad Services Extensions use the`SdkExtensions.AD_SERVICES`constant to determine which version is on a device:  

### Kotlin

```kotlin
fun isAdServicesAvailable(): Boolean {
    return SdkExtensions.getExtensionVersion(SdkExtensions.AD_SERVICES) >= 4
}
```

### Java

```java
public static final boolean isAdServicesAvailable() {
    return SdkExtensions.getExtensionVersion(SdkExtensions.AD_SERVICES) >= 4;
}
```

To learn more about the features in Ad Services Extensions and how to get started, see the[Ad Services Extensions documentation](https://developer.android.com/design-for-safety/privacy-sandbox/program-overview).

#### Utility methods

In some cases, SDK Extensions have Jetpack utility methods for checking the availability of their SDK Extension APIs. For example, you can use a[Jetpack library function to check for PhotoPicker availability](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia#isPhotoPickerAvailable(android.content.Context)), which abstracts away the conditional version checks.

#### Tools support

In Android Studio Flamingo \| 2022.2.1 or higher, the lint tool can scan for issues with SDK Extension versions as part of its NewAPI check. In addition, Android Studio can auto-generate the correct version checks for APIs that are launched using SDK Extensions.
![](https://developer.android.com/static/images/guide/sdk-extensions/extensions-lint-check.png)The lint tool flags instances where the minimum SDK Extensions version required to call an API has not been met.

#### SDK Extension names and constants

The following table describes how the different sets of SDK Extensions that are listed in API reference documentation map to constants that your app can use to check for API availability at runtime. The general set of SDK Extensions for each public SDK maps to values of[`Build.VERSION_CODES`](https://developer.android.com/reference/android/os/Build.VERSION_CODES).

|   SDK Extension name   |             Constant              |           Eligible devices           |
|------------------------|-----------------------------------|--------------------------------------|
| R Extensions           | `VERSION_CODES.R`                 | Android 11 (API Level 30) and higher |
| S Extensions           | `VERSION_CODES.S`                 | Android 12 (API Level 31) and higher |
| T Extensions           | `VERSION_CODES.TIRAMISU`          | Android 13 (API level 33) and higher |
| U Extensions           | `VERSION_CODES.UPSIDE_DOWN_CAKE`  | Android 14 (API level 34) and higher |
| V Extensions           | `VERSION_CODES.VANILLA_ICE_CREAM` | Android 15 (API level 35) and higher |
| Ad Services Extensions | `SdkExtensions.AD_SERVICES`       | Android 13 (API level 33) and higher |

### Check using adb

To check which SDK Extensions are available on a device using adb, run the following command:  

```
adb shell getprop | grep build.version.extensions
```

After running the command, you'll see output that looks similar to this:  

    [build.version.extensions.r]: [3] # Android 11 (API level 30) and higher
    [build.version.extensions.s]: [3] # Android 12 (API level 31) and higher
    [build.version.extensions.t]: [3] # Android 13 (API level 33) and higher

Each line shows an SDK Extension that's present on the device along with their corresponding extensions version (3 in this case).