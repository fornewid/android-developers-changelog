---
title: https://developer.android.com/build/releases/agp-7-3-0-release-notes
url: https://developer.android.com/build/releases/agp-7-3-0-release-notes
source: md.txt
---

Android Gradle Plugin 7.3.0 is a major release that includes a variety of new
features and improvements.

## Compatibility


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 7.4 | 7.4 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 23.1.7779620 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Support for custom C/C++ build systems

You can now create a custom C/C++ build system by making a shell script that
writes build information in the [Ninja](https://ninja-build.org/)
build file format. To learn more about custom C/C++ build systems see
[Integrate custom C/C++ build systems using Ninja (experimental)](https://developer.android.com/studio/build/cxx-ninja).

![Screenshot of custom C/C++ build system](https://developer.android.com/static/studio/images/releases/cxx-ninja.png)

## Minimum Kotlin plugin version is 1.5.20

Starting with Android Gradle plugin 7.3.0-alpha08, AGP requires Kotlin plugin
version 1.5.20 or higher. To stay compatible, make sure to specify Kotlin plugin
version 1.5.20 or higher in your `build.gradle` file:

    org.jetbrains.kotlin:kotlin-gradle-plugin:1.5.20

## Archived APK generation enabled

Starting with AGP 7.3, all Android App Bundles built have
[Store Archival](https://android-developers.googleblog.com/2022/03/freeing-up-60-of-storage-for-apps.html) enabled by
default. Archival is a new app bundle feature that in the future will allow
users with low storage to effectively manage their app space, if supported by
the store.

To opt out of the generation of archived APKs, modify the app-level
`build.gradle` file as follows:

    android {
      bundle {
        storeArchive {
          enable = false
        }
      }
    }

## Package attribute in manifest file is deprecated

Starting with AGP 7.3.0-alpha04, if you use Gradle to build your project,
AGP generates a warning if you use the `package` attribute in the
manifest file. To set the namespace for your app, use the `namespace`
property in the module-level `build.gradle` file. To learn more, see
[Set a namespace](https://developer.android.com/studio/build/configure-app-module#set-namespace).

To get help moving to the new namespace DSL, use the AGP Upgrade
Assistant (**Tools \> AGP Upgrade Assistant**).

## Android platform support

Starting with AGP 7.3.0-beta05, the highest supported minimum SDK version is 33
(you can use `minSdk = 33`). The minimum SDK represents the minimum version of
Android that your app can run on and is set in the app-level `build.gradle`
file.