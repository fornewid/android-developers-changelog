---
title: https://developer.android.com/build/releases/agp-1-5-0-release-notes
url: https://developer.android.com/build/releases/agp-1-5-0-release-notes
source: md.txt
---

<br />

# Android plugin for Gradle, revision 1.5.0 (November 2015)

Dependencies:
General Notes:
:
    - Integrated the Data Binding plugin into the Android plugin for Gradle. To enable it, add the following code to each per-project `build.gradle` file that uses the plugin:

    ```groovy
    android {
        dataBinding {
            enabled = true
        }
    }
            
    ```

    ```kotlin
    android {
        dataBinding {
            enabled = true
        }
    }
            
    ```
    - Added a new [Transform API](https://google.github.io/android-gradle-dsl/javadoc/1.5/) to allow third-party plugins to manipulate compiled `.class` files before they're converted to `.dex` files. The Transform API simplifies injecting custom class manipulations while offering more flexibility regarding what you can manipulate. To insert a transform into a build, create a new class implementing one of the `Transform` interfaces, and register it with `android.registerTransform(theTransform)` or `android.registerTransform(theTransform, dependencies)`. There's no need to wire tasks together. Note the following about the Transform API:
      - A transform can apply to one or more of the following: the current project, subprojects, and external libraries.
      - A transform must be registered globally, which applies them to all variants.
      - Internal code processing, through the Java Code Coverage Library (JaCoCo), ProGuard, and MultiDex, now uses the Transform API. However, the Java Android Compiler Kit (Jack) doesn't use this API: only the `javac/dx` code path does.
      - Gradle executes the transforms in this order: JaCoCo, third-party plugins, ProGuard. The execution order for third-party plugins matches the order in which the transforms are added by the third party plugins; third-party plugin developers can't control the execution order of the transforms through an API.
    - Deprecated the `dex` getter from the `ApplicationVariant` class. You can't access the `Dex` task through the variant API anymore because it's now accomplished through a transform. There's currently no replacement for controlling the dex process.
    - Fixed incremental support for assets.
    - Improved MultiDex support by making it available for test projects, and tests now automatically have the `com.android.support:multidex-instrumentation` dependency.
    - Added the ability to properly fail a Gradle build and report the underlying error cause when the Gradle build invokes asynchronous tasks and there's a failure in the worker process.
    - Added support for configuring a specific Application Binary Interface (ABI) in variants that contain multiple ABIs.
    - Added support for a comma-separated list of device serial numbers for the `ANDROID_SERIAL` environment variable when installing or running tests.
    - Fixed an installation failure on devices running Android 5.0 (API level 20) and higher when the APK name contains a space.
    - Fixed various issues related to the Android Asset Packaging Tool (AAPT) error output.
    - Added JaCoCo incremental instrumentation support for faster incremental builds. The Android plugin for Gradle now invokes the JaCoCo instrumenter directly. To force a newer version of the JaCoCo instrumenter, you need to add it as a build script dependency.
    - Fixed JaCoCo support so it ignores files that aren't classes.
    - Added vector drawable support for generating PNGs at build time for backward-compatibility. Android plugin for Gradle generates PNGs for every vector drawable found in a resource directory that doesn't specify an API version or specifies an `android:minSdkVersion` attribute of 20 or lower in the `<uses-sdk>` element in the app manifest. You can set PNG densities by using the `generatedDensities` property in the `defaultConfig` or `productFlavor` sections of a `build.gradle` file.
    - Added sharing of the mockable `android.jar`, which the plugin generates only once and uses for unit testing. Multiple modules, such as `app` and `lib`, now share it. Delete `$rootDir/build` to regenerate it.
    - Changed the processing of Java resources to occur before the obfuscation tasks instead of during the packaging of the APK. This change allows the obfuscation tasks to have a chance to adapt the Java resources following packages obfuscation.
    - Fixed an issue with using Java Native Interface (JNI) code in the experimental library plugin.
    - Added the ability to set the platform version separately from the `android:compileSdkVersion` attribute in the experimental library plugin.

<br />