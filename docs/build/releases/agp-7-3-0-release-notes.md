---
title: Android Gradle Plugin 7.3.0 (Sep 2022)  |  Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-7-3-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

# Android Gradle Plugin 7.3.0 (Sep 2022) Stay organized with collections Save and categorize content based on your preferences.




Android Gradle Plugin 7.3.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 7.4 | 7.4 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 23.1.7779620 | [Install](/studio/projects/install-ndk#specific-version) or [configure](/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](/studio/intro/studio-config#jdk). |

## Support for custom C/C++ build systems

You can now create a custom C/C++ build system by making a shell script that
writes build information in the [Ninja](https://ninja-build.org/)
build file format. To learn more about custom C/C++ build systems see
[Integrate custom C/C++ build systems using Ninja (experimental)](/studio/build/cxx-ninja).

![Screenshot of custom C/C++ build system](/static/studio/images/releases/cxx-ninja.png)

## Minimum Kotlin plugin version is 1.5.20

Starting with Android Gradle plugin 7.3.0-alpha08, AGP requires Kotlin plugin
version 1.5.20 or higher. To stay compatible, make sure to specify Kotlin plugin
version 1.5.20 or higher in your `build.gradle` file:

```
org.jetbrains.kotlin:kotlin-gradle-plugin:1.5.20
```

## Archived APK generation enabled

Starting with AGP 7.3, all Android App Bundles built have
[Store Archival](https://android-developers.googleblog.com/2022/03/freeing-up-60-of-storage-for-apps.html) enabled by
default. Archival is a new app bundle feature that in the future will allow
users with low storage to effectively manage their app space, if supported by
the store.

To opt out of the generation of archived APKs, modify the app-level
`build.gradle` file as follows:

```
android {
  bundle {
    storeArchive {
      enable = false
    }
  }
}
```

## Package attribute in manifest file is deprecated

Starting with AGP 7.3.0-alpha04, if you use Gradle to build your project,
AGP generates a warning if you use the `package` attribute in the
manifest file. To set the namespace for your app, use the `namespace`
property in the module-level `build.gradle` file. To learn more, see
[Set a namespace](/studio/build/configure-app-module#set-namespace).

To get help moving to the new namespace DSL, use the AGP Upgrade
Assistant (**Tools > AGP Upgrade Assistant**).

## Android platform support

Starting with AGP 7.3.0-beta05, the highest supported minimum SDK version is 33
(you can use `minSdk = 33`). The minimum SDK represents the minimum version of
Android that your app can run on and is set in the app-level `build.gradle`
file.