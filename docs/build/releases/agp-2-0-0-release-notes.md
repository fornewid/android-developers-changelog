---
title: https://developer.android.com/build/releases/agp-2-0-0-release-notes
url: https://developer.android.com/build/releases/agp-2-0-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 2.0.0 (April 2016)

<br />

Dependencies:
New:
:
    - Enables [Instant Run](https://developer.android.com/tools/building/building-studio#instant-run) by supporting bytecode injection, and pushing code and resource updates to a running app on the emulator or a physical device.
    - Added support for incremental builds, even when the app isn't running. Full build times are improved by pushing incremental changes through the [Android Debug Bridge](https://developer.android.com/tools/help/adb) to the connected device.
    - Added [`maxProcessCount`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.DexOptions.html#com.android.build.gradle.internal.dsl.DexOptions:maxProcessCount) to control how many worker dex processes can be spawned concurrently. The following code, in the module-level `build.gradle` file, sets the maximum number of concurrent processes to 4:

      ### Groovy

      ```groovy
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```
    - Added an experimental code shrinker to support pre-dexing and reduce re-dexing of dependencies, which are not supported with Proguard. This improves the build speed of your debug build variant. Because the experimental shrinker does not support optimization and obfuscation, you should enable Proguard for your release builds. To enable the experimental shrinker for your debug builds, add the following to your module-level `build.gradle` file:

      ### Groovy

      ```groovy
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

      ```kotlin
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
    - Added logging support and improved performance for the resource shrinker. The resource shrinker now logs all of its operations into a `resources.txt` file located in the same folder as the Proguard log files.

Changed behavior:
:
    - When `minSdkVersion` is set to 18 or higher, APK signing uses SHA256.
    - DSA and ECDSA keys can now sign APK packages.
      **Note:** The [Android keystore](https://developer.android.com/training/articles/keystore) provider no
      longer supports [DSA keys on Android 6.0](https://developer.android.com/about/versions/marshmallow/android-6.0-changes#behavior-keystore) (API level 23) and higher.


Fixed issues:
:
    - Fixed an issue that caused duplicate AAR dependencies in both the test and main build configurations.