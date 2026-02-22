---
title: Set up the Android 17 SDK  |  Android Developers
url: https://developer.android.com/about/versions/17/setup-sdk
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Set up the Android 17 SDK Stay organized with collections Save and categorize content based on your preferences.




To develop with Android 17 APIs and test your app with the Android 17 behavior
changes, you need to set up the Android 17 SDK. Follow the instructions on this
page to set up the Android 17 SDK in Android Studio and build and run your app
on Android 17.

## Get Android Studio

The Android 17 SDK includes changes that are not compatible with some lower
versions of Android Studio. For the best
development experience with the Android 17 SDK, use the [latest preview
version](/studio/preview) of Android Studio. Remember that you can keep your existing version
of Android Studio installed, as you can [install multiple versions
side-by-side](/studio/preview/install-preview).

[Get Android Studio](/studio/preview)

## Update your app's build configuration

**Warning:** If your project does not use Android Gradle plugin 8.9.0-rc01 or
higher, first run the [Android Gradle plugin Upgrade Assistant](/r/tools/upgrade-assistant/agp-upgrade-assistant) to upgrade to
at least AGP 8.9.0-rc01.

To access Android 17 APIs, open your app's `build.gradle` or `build.gradle.kts`
file and update the `compileSdk` for Android 17 as follows:

### Groovy

```
android {
    compileSdkPreview = "CinnamonBun"
}
```

### Kotlin

```
android {
    compileSdkPreview = "CinnamonBun"
}
```

Android Studio can provide contextual information about the
behavior changes through the
[Android SDK Upgrade Assistant](/r/studio-ui/ide/android-sdk-upgrade-assistant).
Once you're ready to opt in to the new runtime behaviours for Android 17,
update your app's `targetSdk` as follows:

### Groovy

```
android {
    defaultConfig {
        targetSdkPreview = "CinnamonBun"
    }
}
```

### Kotlin

```
android {
    defaultConfig {
        targetSdkPreview = "CinnamonBun"
    }
}
```

### Manually install the SDK

Within Android Studio, you can install the Android 17 SDK as follows:

1. Click **Tools > SDK Manager**.
2. In the **SDK Platforms tab**, expand the **Android Cinnamon Bun Preview**
   section and select the **Android SDK Platform Cinnamon Bun** package.
3. In the **SDK Tools** tab, expand the **Android SDK Build-Tools 37** section
   and select the latest `37.x.x` version.
   These labels might have a suffix such
   as **rc1** or **rc2**.
4. Click **OK** to install the SDK.

## Next steps

To learn about the changes that might affect your app, and to learn how to test
these changes in your app, read the following topics:

* [Behavior changes that affect all apps](/about/versions/17/behavior-changes-all)
* [Behavior changes that affect only apps that target Android 17](/about/versions/17/behavior-changes-17)

To learn more about new APIs and features available in Android 17, read [Android
17 features](/about/versions/17/features).