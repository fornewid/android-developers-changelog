---
title: https://developer.android.com/build/releases/agp-3-1-0-release-notes
url: https://developer.android.com/build/releases/agp-3-1-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.1.0 (March 2018)

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 4.4 | 4.4 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 27.0.3 | 27.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. Keep in mind, you no longer need to specify a version for the build tools using the android.buildToolsVersion property---the plugin uses the minimum required version by default. |

<br />

<br />

## New DEX compiler, D8

By default, Android Studio now uses a new DEX compiler called D8. DEX
compilation is the process of transforming `.class` bytecode into
`.dex` bytecode for the Android Runtime (or Dalvik, for older
versions of Android). Compared to the previous compiler, called DX, D8
compiles faster and outputs smaller DEX files, all while having the same or
better app runtime performance.

D8 shouldn't change your day-to-day app development workflow. However, if
you experience any issues related to the new compiler, please
[report a bug](https://developer.android.com/studio/report-bugs). You can temporarily
disable D8 and use DX by including the following in your project's
`gradle.properties` file:

          android.enableD8=false
        
For projects that
[use Java 8 language features](https://developer.android.com/studio/write/java8-support),
incremental desugaring is enabled by default. You can disable it by
specifying the following in your project's `gradle.properties` file:

          android.enableIncrementalDesugaring=false.
        

**Preview users:** If you're already using a preview version of D8, note
that it now compiles against libraries included in the
[SDK build tools](https://developer.android.com/studio/releases/build-tools)---not the JDK.
So, if you are accessing APIs that exist in the JDK but not in the SDK build
tools libraries, you get a compile error.

<br />

<br />

## Behavior changes

- When building multiple APKs that each target a different ABI, the
  no longer generates APKs for the following ABIs by default:
  `mips`, `mips64`, and `armeabi`.

  If you want to build APKs that target these ABIs, you must use
  [NDK r16b or lower](https://developer.android.com/ndk/downloads/revision_history) and
  specify the ABIs in your `build.gradle` file, as shown below:

  ```groovy
            splits {
                abi {
                    include 'armeabi', 'mips', 'mips64'
                    ...
                }
            }
          
  ```

  ```kotlin
            splits {
                abi {
                    include("armeabi", "mips", "mips64")
                    ...
                }
            }
          
  ```
- The Android plugin's [build
  cache](https://developer.android.com/studio/build/build-cache) now evicts cache entries that are older than 30 days.

- Passing `"auto"` to
  [`resConfig`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:resConfig(java.lang.String))
  no longer automatically picks string resources to package into your APK.
  If you continue to use `"auto"`, the plugin packages all string
  resources your app and its dependencies provide. So, you should instead
  specify each locale that you want the plugin to package into your APK.

- Because local modules can't depend on your app's test APK, adding
  dependencies to your instrumented tests using the
  `androidTestApi` configuration, instead of
  `androidTestImplementation`, causes Gradle to issue the
  following warning:

  ```groovy
          WARNING: Configuration 'androidTestApi' is obsolete
          and has been replaced with 'androidTestImplementation'
          
  ```

  ```kotlin
          WARNING: Configuration 'androidTestApi' is obsolete
          and has been replaced with 'androidTestImplementation'
          
  ```

<br />

<br />

## Fixes

- Fixes an issue where Android Studio doesn't properly recognize dependencies in composite builds.
- Fixes an issue where you get a project sync error when loading the Android plugin multiple times in a single build--for example, when multiple subprojects each include the Android plugin in their buildscript classpath.

<br />