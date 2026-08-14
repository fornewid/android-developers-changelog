---
title: https://developer.android.com/build/releases/agp-1-1-0-release-notes
url: https://developer.android.com/build/releases/agp-1-1-0-release-notes
source: md.txt
---

# Android plugin for Gradle, revision 1.1.0 (February 2015)

Dependencies:
General Notes:
:
    - Added new unit test support
      - Enabled [unit
        tests](https://developer.android.com/training/activity-testing/activity-unit-testing) to run on the local JVM against a special version of the `android.jar` file that is compatible with popular mocking frameworks, for example Mockito.
      - Added new test tasks `testDebug`, `testRelease`, and `testMyFlavorDebug` when using product flavors.
      - Added new source folders recognized as unit tests: `src/test/java/`, `src/testDebug/java/`, `src/testMyFlavor/java/`.
      - Added new configurations in the `build.gradle` file for declaring test-only dependencies, for example, `testCompile 'junit:junit:4.11'`, `testMyFlavorCompile 'some:library:1.0'`.

        **Note:** Test-only dependencies
        are not compatible with Jack (Java Android Compiler Kit).
      - Added the `android.testOptions.unitTests.returnDefaultValues` option to control the behaviour of the mockable android.jar.
    - Replaced `Test` in test task names with `AndroidTest`. For example, the `assembleDebugTest` task is now `assembleDebugAndroidTest` task. Unit test tasks still have `UnitTest` in the task name, for example `assembleDebugUnitTest`.
    - Modified [ProGuard](https://developer.android.com/tools/help/proguard) configuration files to no longer apply to the test APK. If minification is enabled, ProGuard processes the test APK and applies only the mapping file that is generated when minifying the main APK.
    - Updated dependency management
      - Fixed issues using `provided` and `package` scopes.

        **Note:** These scopes are
        incompatible with AAR (Android ARchive) packages and
        cause a build with AAR packages to fail.
      - Modified dependency resolution to compare the dependencies of an app under test and the test app. If an artifact with the same version is found for both apps, it's not included with the test app and is packaged only with the app under test. If an artifact with a different version is found for both apps, the build fails.
    - Added support for `anyDpi` [resource
      qualifier](https://developer.android.com/guide/topics/resources/providing-resources) in resource merger.
    - Improved evaluation and IDE sync speeds for projects with a large number of Android [modules](https://developer.android.com/studio/projects).