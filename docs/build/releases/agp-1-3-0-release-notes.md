---
title: https://developer.android.com/build/releases/agp-1-3-0-release-notes
url: https://developer.android.com/build/releases/agp-1-3-0-release-notes
source: md.txt
---

<br />

# Android plugin for Gradle, revision 1.3.0 (July 2015)

**Dependencies:**

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 2.2.1 | 2.2.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**General Notes:**

- Added support for the `com.android.build.threadPoolSize`
  property to control the `Android` task thread pool size from
  the `gradle.properties` file or the command line. The
  following example sets this property to 4.

              
              -Pcom.android.build.threadPoolSize=4
              
            
- Set the default build behavior to exclude `LICENSE` and `LICENSE.txt` files from APKs. To include these files in an APK, remove these files from the `packagingOptions.excludes` property in the `build.gradle` file. For example:

  ```groovy
  android {
        packagingOptions.excludes = []
      }
        
  ```

  ```kotlin
  android {
        packagingOptions.excludes.clear()
      }
      
  ```
- Added the `sourceSets` task to inspect the set of all available source sets.
- Enhanced unit test support to recognize multi-flavor and [build variant](https://developer.android.com/tools/building/configuring-gradle#workBuildVariants) source folders. For example, to test an app with multi-flavors `flavor1` and `flavorA` with the `Debug` build type, the test source sets are:
  - test
  - testFlavor1
  - testFlavorA
  - testFlavor1FlavorA
  - testFlavor1FlavorADebug

  Android tests already recognized multi-flavor source folders.
- Improved unit test support to:
  - Run `javac` on main and test sources, even if the `useJack` property is set to `true` in your build file.
  - Correctly recognize dependencies for each build type.
- Added support for specifying instrumentation test-runner arguments from the command line. For example:

  ```
  ./gradlew connectedCheck 

     -Pandroid.testInstrumentationRunnerArguments.size=medium 

     -Pandroid.testInstrumentationRunnerArguments.class=TestA,TestB
          
  ```
- Added support for arbitrary additional Android Asset Packaging Tool (AAPT) parameters
  in the `build.gradle` file. For example:

  ```groovy
  android {
      aaptOptions {
        additionalParameters "--custom_option", "value"
      }
  }
        
  ```

  ```kotlin
  android {
      aaptOptions {
        additionalParameters += listOf("--custom_option", "value")
      }
  }
        
  ```
- Added support for a [test APK module](https://developer.android.com/tools/studio/studio-features#test-module) as a separate test module, using the `targetProjectPath` and `targetVariant` properties to set the APK path and target variant.

  **Note:** A test APK module does not support product
  flavors and can only target a single variant. Also, Jacoco is not supported yet.
- Added resource name validation before merging resources.
- When building an AAR (Android ARchive) package for library modules, do not provide an automatic `@{applicationId}` placeholder in the [manifest merger](https://developer.android.com/tools/building/manifest-merge) settings. Instead, use a different placeholder, such as `@{libApplicationId}` and provide a value for it if you want to include application Ids in the archive library.

<br />