---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-2-0-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.




# Android Gradle Plugin 2.0.0 (April 2016)

Dependencies:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 2.10 | 2.10 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

New:
:   * Enables [Instant Run](/tools/building/building-studio#instant-run) by
      supporting bytecode injection, and pushing code and resource updates to a
      running app on the emulator or a physical device.
    * Added support for incremental builds, even when the app isn’t running.
      Full build times are improved by pushing incremental changes through the
      [Android Debug Bridge](/tools/help/adb) to the
      connected device.
    * Added [`maxProcessCount`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.DexOptions.html#com.android.build.gradle.internal.dsl.DexOptions:maxProcessCount) to control how many worker dex processes can be
      spawned concurrently. The following code, in the module-level
      `build.gradle` file, sets the maximum number of concurrent processes
      to 4:

      ### Groovy

      ```
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```

      ### Kotlin

      ```
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```
    * Added an experimental code shrinker to support pre-dexing and reduce re-dexing
      of dependencies, which are not supported with Proguard. This improves the build
      speed of your debug build variant. Because the experimental shrinker does not
      support optimization and obfuscation, you should enable Proguard for your
      release builds. To enable the experimental shrinker for your debug builds, add
      the following to your module-level `build.gradle` file:

      ### Groovy

      ```
      android {
        ...
        buildTypes {
          debug {
            minifyEnabled true
            useProguard false
          }
          release {
            minifyEnabled true
            useProguard true // this is a default setting
          }
        }
      }
      ```

      ### Kotlin

      ```
      android {
        ...
        buildTypes {
          getByName("debug") {
            minifyEnabled = true
            useProguard = false
          }
          getByName("release") {
            minifyEnabled = true
            useProguard = true // this is a default setting
          }
        }
      }
      ```
    * Added logging support and improved performance for the resource shrinker.
      The resource shrinker now logs all of its operations into a `resources.txt`
      file located in the same folder as the Proguard log files.

Changed behavior:
:   * When `minSdkVersion` is set to 18 or higher, APK signing uses
      SHA256.
    * DSA and ECDSA keys can now sign APK packages.

      **Note:** The [Android keystore](/training/articles/keystore) provider no
      longer supports [DSA keys on Android 6.0](/about/versions/marshmallow/android-6.0-changes#behavior-keystore) (API level 23) and higher.

Fixed issues:
:   * Fixed an issue that caused duplicate AAR dependencies in both
      the test and main build configurations.