---
title: https://developer.android.com/about/versions/10/setup-sdk
url: https://developer.android.com/about/versions/10/setup-sdk
source: md.txt
---

# Set up the Android 10 SDK

Android 10 is a major release and includes a variety of[features and capabilities](https://developer.android.com/about/versions/10/features)you can use to extend your app. Android 10 also includes behavior changes (for[apps targeting Android 10](https://developer.android.com/about/versions/10/behavior-changes-10)and for[all apps](https://developer.android.com/about/versions/10/behavior-changes-all)) and[privacy changes](https://developer.android.com/about/versions/10/privacy)that help improve battery life and security.

To develop with Android 10 APIs and test your app with the Android 10 behavior changes, follow the instructions on this page to set up the Android 10 SDK in Android Studio and build and run your app on Android 10.

## Get the latest Android Studio

The Android 10 SDK includes changes that are not compatible with some lower versions of Android Studio. So, for the best development experience, we recommend that you install the latest version of[Android Studio](https://developer.android.com/studio).

[Get Android Studio](https://developer.android.com/studio)

You can compile and test Android 10 apps using Android Studio 3.3 and higher, but some users of the Android 10 SDK may encounter Gradle sync failures and warnings about outdated dependencies.

## Get the Android 10 SDK

After you install and open Android Studio, install the Android 10 SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms** tab, expand the**Android 10.0 ("Q")** section and select the**Android SDK Platform 29**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 34** section and select the latest`29.x.x`version.
4. Click**Apply \> OK**to download and install the selected packages.

## Update your build configuration

To fully test your app's compatibility with Android 10 and begin using the APIs introduced in this version of the platform, open your module-level`build.gradle`file and update the`compileSdkVersion`and`targetSdkVersion`as shown here:  

### Groovy

```groovy
android {
    compileSdkVersion 29

    defaultConfig {
        targetSdkVersion 29
    }
    ...
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion(29)

    defaultConfig {
        targetSdkVersion(29)
    }
    ...
}
```

To learn about the changes in Android 10 that might affect your app and begin testing them, read[Android 10 behavior changes affecting all apps](https://developer.android.com/about/versions/10/behavior-changes-all),[Android 10 behavior changes affecting apps targeting Android 10](https://developer.android.com/about/versions/10/behavior-changes-10), and[Android 10 privacy changes](https://developer.android.com/about/versions/10/privacy).

To learn more about the APIs available starting in Android 10, read[Android 10 features and APIs](https://developer.android.com/about/versions/10/features).