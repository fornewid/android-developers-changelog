---
title: https://developer.android.com/about/versions/11/setup-sdk
url: https://developer.android.com/about/versions/11/setup-sdk
source: md.txt
---

Android 11 contains a variety of great ways you can extend your
app. Android 11
also includes behavior changes to improve battery life and security, and to
[enhance user privacy](https://developer.android.com/about/versions/11/privacy). Some of these behavior changes [only affect apps that
target Android 11](https://developer.android.com/about/versions/11/behavior-changes-11), while others [affect all apps when they are running on an
Android 11 device](https://developer.android.com/about/versions/11/behavior-changes-all), regardless of an app's `targetSDKVersion`.

To develop with Android 11 APIs and test your app with the
Android 11 behavior changes, follow the instructions on this page
to set up the Android 11 SDK in Android Studio and build and run
your app on Android 11.

## Get Android Studio

The Android 11 SDK includes changes that are not compatible with
some lower versions of Android Studio. For the best development experience with
the Android 11 SDK, use Android Studio 4.2 or higher.

[Get Android Studio](https://developer.android.com/studio)

You can compile and test Android 11 apps using Android Studio
3.3 and higher, but some users of the Android 11 SDK may
encounter Gradle sync failures and warnings about outdated dependencies.
Remember, you can keep your existing version of Android Studio installed,
because you can [install multiple versions side by side](https://developer.android.com/studio/preview/install-preview).

## Get the Android 11 SDK

After you install and open Android Studio, install the Android 11
SDK as follows:

1. Click **Tools \> SDK Manager** , then click **Show Package Details**.
2. In the **SDK Platforms** tab, expand the **Android 11.0 ("R")** section and select the **Android SDK Platform 30** package.
3. In the **SDK Tools** tab, expand the **Android SDK Build-Tools 34** section and select the latest `30.x.x` version.
4. Click **Apply \> OK** to download and install the selected packages.

## Update your build configuration

Changing your app's build configuration to target Android 11 gives your app
access to the Android 11 APIs and lets you fully test your app's compatibility
as you [prepare to add full support for Android 11](https://developer.android.com/about/versions/11/migration#setup_sdk). To do this, open your
module-level `build.gradle` file and update the `compileSdkVersion` and
`targetSdkVersion`:  

### Groovy

```groovy
android {
    compileSdkVersion 30

    defaultConfig {
        targetSdkVersion 30
    }
    ...
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion(30)

    defaultConfig {
        targetSdkVersion(30)
    }
    ...
}
```
| **Note:** If you're not ready yet to fully support Android 11, you can still perform app compatibility testing using a debuggable app, an Android 11 device, and the [compatibility framework](https://developer.android.com/guide/app-compatibility/test-debug), without changing either your app's `compileSdkVersion` or `targetSdkVersion`.

To learn about the changes in Android 11 that might affect your
app so you can begin testing for them, read the following pages:

- [Android 11 behavior changes affecting all apps](https://developer.android.com/about/versions/11/behavior-changes-all)
- [Android 11 behavior changes affecting apps that target Android 11](https://developer.android.com/about/versions/11/behavior-changes-11)
- [Android 11 privacy changes](https://developer.android.com/about/versions/11/privacy)

To learn more about new APIs available in Android 11, read
[Android 11 features and APIs](https://developer.android.com/about/versions/11/features).