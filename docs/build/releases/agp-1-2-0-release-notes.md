---
title: https://developer.android.com/build/releases/agp-1-2-0-release-notes
url: https://developer.android.com/build/releases/agp-1-2-0-release-notes
source: md.txt
---

<br />

# Android plugin for Gradle, revision 1.2.0 (April 2015)

Dependencies:
General Notes:
:
    - Enhanced support for running unit tests with Gradle.
      - Added support to include Java-style resources in the classpath when running unit tests directly from Gradle.
      - Added unit test dependency support for Android Archive (AAR) artifacts.
      - Added support for the `unitTestVariants` property so unit test variants can be manipulated using the `build.gradle` file.
      - Added the `unitTest.all` code block under `testOptions` to configure customized tasks for unit test. The following sample code shows how to add unit test configuration settings using this new option:

        ```groovy
        android {
          testOptions {
            unitTest.all {
              jvmArgs '-XX:MaxPermSize=256m' // Or any other gradle option.
            }
          }
        }
        ```

        ```kotlin
        android {
          testOptions {
            unitTest.all {
              jvmArgs += listOf("-XX:MaxPermSize=256m") // Or any other gradle option.
            }
          }
        }
                    
        ```
      - Fixed the handling of enums and public instance fields in the packaging of the `mockable-android.jar` file.
      - Fixed library project task dependencies so test classes recompile after changes.
    - Added the `testProguardFile` property to apply [ProGuard](https://developer.android.com/tools/help/proguard) files when minifying a test APK.
    - Added the `timeOut` property to the `adbOptions` code block for setting the maximum recording time for [Android Debug Bridge](https://developer.android.com/tools/help/adb) screen recording.
    - Added support for 280 dpi resources.
    - Improved performance during project evaluation.

<br />