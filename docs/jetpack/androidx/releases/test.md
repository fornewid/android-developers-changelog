---
title: https://developer.android.com/jetpack/androidx/releases/test
url: https://developer.android.com/jetpack/androidx/releases/test
source: md.txt
---

# Test

[User Guide](https://developer.android.com/training/testing) [Code Sample](https://github.com/android/testing-samples)  
API Reference  
[androidx.test.core.app](https://developer.android.com/reference/kotlin/androidx/test/core/app/package-summary)  
[androidx.test.espresso](https://developer.android.com/reference/kotlin/androidx/test/espresso/package-summary)  

<br />

Testing in Android.  


This table lists all the artifacts in the `androidx.test` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| annotation | [1.0.1](https://developer.android.com/jetpack/androidx/releases/test#annotation-1.0.1) | - | - | [1.1.0-alpha04](https://developer.android.com/jetpack/androidx/releases/test#annotation-1.1.0-alpha04) |
| core | [1.7.0](https://developer.android.com/jetpack/androidx/releases/test#core-1.7.0) | [1.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#core-1.7.0-rc01) | - | - |
| espresso | [3.7.0](https://developer.android.com/jetpack/androidx/releases/test#espresso-3.7.0) | [3.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#espresso-3.7.0-rc01) | - | - |
| espresso-device | [1.1.0](https://developer.android.com/jetpack/androidx/releases/test#espresso-device-1.1.0) | [1.1.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#espresso-device-1.1.0-rc01) | - | - |
| ext.junit | [1.3.0](https://developer.android.com/jetpack/androidx/releases/test#ext.junit-1.3.0) | [1.3.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#ext.junit-1.3.0-rc01) | - | - |
| ext:junit-gtest | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/test#ext:junit-gtest-1.0.0-alpha01) |
| ext.truth | [1.7.0](https://developer.android.com/jetpack/androidx/releases/test#ext.truth-1.7.0) | [1.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#ext.truth-1.7.0-rc01) | - | - |
| monitor | [1.8.0](https://developer.android.com/jetpack/androidx/releases/test#monitor-1.8.0) | [1.8.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#monitor-1.8.0-rc01) | - | - |
| orchestrator | [1.6.1](https://developer.android.com/jetpack/androidx/releases/test#orchestrator-1.6.1) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#orchestrator-1.6.0-rc01) | - | - |
| runner | [1.7.0](https://developer.android.com/jetpack/androidx/releases/test#runner-1.7.0) | [1.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#runner-1.7.0-rc01) | - | - |
| rules | [1.7.0](https://developer.android.com/jetpack/androidx/releases/test#rules-1.7.0) | [1.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#rules-1.7.0-rc01) | - | - |
| services | [1.6.0](https://developer.android.com/jetpack/androidx/releases/test#services-1.6.0) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/test#services-1.6.0-rc01) | - | - |

This library was last updated on: July 31, 2025 **Note:** This page includes release notes for Test components that shipped in the AndroidX library. For earlier updates that appeared in the support library see the [archive page](https://developer.android.com/jetpack/androidx/releases/archive/test).

## Declaring dependencies

To add a dependency on androidx.test, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    // To use the androidx.test.core APIs
    androidTestImplementation "androidx.test:core:1.7.0"
    // Kotlin extensions for androidx.test.core
    androidTestImplementation "androidx.test:core-ktx:1.7.0"

    // To use the androidx.test.espresso
    androidTestImplementation "androidx.test.espresso:espresso-core:3.7.0"

    // To use the JUnit Extension APIs
    androidTestImplementation "androidx.test.ext:junit:1.3.0"
    // Kotlin extensions for androidx.test.ext.junit
    androidTestImplementation "androidx.test.ext:junit-ktx:1.3.0"

    // To use the Truth Extension APIs
    androidTestImplementation "androidx.test.ext:truth:1.7.0"

    // To use the androidx.test.runner APIs
    androidTestImplementation "androidx.test:runner:1.7.0"

    // To use android test orchestrator
    androidTestUtil "androidx.test:orchestrator:1.6.1"

}
```

### Kotlin

```kotlin
dependencies {
    // To use the androidx.test.core APIs
    androidTestImplementation("androidx.test:core:1.7.0")
    // Kotlin extensions for androidx.test.core
    androidTestImplementation("androidx.test:core-ktx:1.7.0")

    // To use the androidx.test.espresso
    androidTestImplementation("androidx.test.espresso:espresso-core:3.7.0")

    // To use the JUnit Extension APIs
    androidTestImplementation("androidx.test.ext:junit:1.3.0")
    // Kotlin extensions for androidx.test.ext.junit
    androidTestImplementation("androidx.test.ext:junit-ktx:1.3.0")

    // To use the Truth Extension APIs
    androidTestImplementation("androidx.test.ext:truth:1.7.0")

    // To use the androidx.test.runner APIs
    androidTestImplementation("androidx.test:runner:1.7.0")

    // To use android test orchestrator
    androidTestUtil("androidx.test:orchestrator:1.6.1")
}
```

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:192735+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192735&template=840510)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Annotation 1.1.0

### Annotation 1.1.0-alpha04

April 26, 2024

`androidx.test:annotation:1.1.0-alpha04}` is released.

### Annotation 1.1.0-alpha03

January 26, 2024

`androidx.test:annotation:1.1.0-alpha03}` is released.

**API Changes**

- Un-hide ExperimentalTestApi

### Annotation 1.1.0-alpha02

November 29, 2023

`androidx.test:annotation:1.1.0-alpha02}` is released.

**API Changes**

- minSdkVersion is now 19, targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### Annotation 1.1.0-alpha01

March 21, 2023

`androidx.test:annotation:1.1.0-alpha01` is released.

**Dependency changes**

- Update to kotlin stdlib 1.7.22
- Major release toolchain update: now compiled to java8 bytecode

## Annotation 1.0.1

### Annotation 1.0.1

November 8, 2022

`androidx.test:annotation:1.0.1` is released.

Changes since 1.0.0 include:

**Dependency changes**

- Update to kotlin stdlib 1.7.10

### Annotation 1.0.1-rc01

October 26, 2022

`androidx.test:annotation:1.0.1-rc01` is released.

### Annotation 1.0.1-beta01

October 6, 2022

`androidx.test:annotation:1.0.1-beta01` is released.

**Dependency changes**

- Update to kotlin stdlib 1.7.10

### Annotation 1.0.1-alpha01

June 1, 2022

`androidx.test:annotation:1.0.1-alpha01` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

## Annotation 1.0.0

### Annotation 1.0.0

Dec 13, 2021

`androidx.test:annotation:1.0.0` is released.

New artifact, currently for internal androidx.test use.

### Annotation 1.0.0-rc01

Nov 18, 2021

`androidx.test:annotation:1.0.0-rc01` is released.

### Annotation 1.0.0-beta01

Nov 8, 2021

`androidx.test:annotation:1.0.0-beta01` is released.

### Annotation 1.0.0-alpha02

Oct 4, 2021

`androidx.test:annotation:1.0.0-alpha02` is released.

### Annotation 1.0.0-alpha01

Sept 28, 2021

`androidx.test:annotation:1.0.0-alpha01` is released.

**API Changes**

- Add new ExperimentalTestApi and InternalTestApi annotations

## Core 1.7.0

### Core Core-ktx 1.7.0

July 30, 2025

`androidx.test:core:1.7.0` and `androidx.test:core-ktx:1.7.0` are released.

Changes since last stable release 1.6.0 include:

**Bug Fixes**

- Fix `Rect` handling in `ViewCapture` for SDK \>= 34 for non root views.
- Fix bug reporting the status code when PixelCopy fails in ViewCapture.generateBitmapFromPixelCopy.
- Improving wording of a failure message.

**API Changes**

- Update to minSdkVersion 21

**Dependency Updates**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - androidx.concurrent futures 1.2.0
  - kotlin 1.9.0
  - kotlin coroutines 1.10.1

### Core Core-ktx 1.7.0-rc01

July 14, 2025

`androidx.test:core:1.7.0-rc01` and `androidx.test:core-ktx:1.7.0-rc01` are released.

### Core Core-ktx 1.7.0-beta01

June 30, 2025

`androidx.test:core:1.7.0-beta01` and `androidx.test:core-ktx:1.7.0-beta01` are released.

### Core Core-ktx 1.7.0-alpha03

April 23, 2025

`androidx.test:core:1.7.0-alpha03` and `androidx.test:core-ktx:1.7.0-alpha03` are released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### Core Core-ktx 1.7.0-alpha02

March 27, 2025

`androidx.test:core:1.7.0-alpha02` and `androidx.test:core-ktx:1.7.0-alpha02` are released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - androidx.concurrent futures 1.2.0
  - kotlin 2.1.0
  - kotlin coroutines 1.10.1

### Core Core-ktx 1.7.0-alpha01

February 03, 2025

`androidx.test:core:1.7.0-alpha01` and `androidx.test:core-ktx:1.7.0-alpha01` are released.

**Bug Fixes**
\* Fix `Rect` handling in `ViewCapture` for SDK \>= 34 for non root views.
\* Fix bug reporting the status code when PixelCopy fails in ViewCapture.generateBitmapFromPixelCopy.
\* Improving wording of a failure message.

**API Changes**

- Update to minSdkVersion 21

### Core Core-ktx 1.6.1

June 26, 2024

`androidx.test:core:1.6.1` and `androidx.test:core-ktx:1.6.1` are released.

### Core Core-ktx 1.6.0

June 24, 2024

`androidx.test:core:1.6.0` and `androidx.test:core-ktx:1.6.0` are released.

Changes since last stable release 1.5.0 include:

**API Changes**

- Added ApplicationInfoBuilder.setFlags(int)
- Add new lower level screenshot APIs View.captureToBitmap, WindowCapture.captureToBitmap, Bitmap.writeToTestStorage and DeviceCapture.takeScreenshot screenshots.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency
- Fix using ActivityScenario#launchActivityForResult with an implicit Intent
- Update Activity Scenario reference documentation to fix missing links
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Reference doc cleanup - document previously missing parameters, fix links, etc
- Activity starts are automatically opted in to allow background activity launches when targetSdk \>= 34
- Fix issue where Activity#isChangingConfigurations is incorrectly false during ActivityScenario#recreate

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update: now compiled to java8 bytecode

### Core Core-ktx 1.6.0-rc01

May 30, 2024

`androidx.test:core:1.6.0-rc01` and `androidx.test:core-ktx:1.6.0-rc01` are released.

### Core Core-ktx 1.6.0-beta01

May 16, 2024

`androidx.test:core:1.6.0-beta01` and `androidx.test:core-ktx:1.6.0-beta01` are released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency
- Revert back to androidx.concurrent 1.1.0

### Core Core-ktx 1.6.0-alpha06

April 26, 2024

`androidx.test:core:1.6.0-alpha06` and `androidx.test:core-ktx:1.6.0-alpha06` are released.

**Bug Fixes**

- Make ViewCapture use ControlledLooper API instead of hardcoding is Robolectric check
- Fix using ActivityScenario#launchActivityForResult with an implicit Intent

**API Changes**

- Added ApplicationInfoBuilder.setFlags(int)
- Make suspend function versions of ViewCapture/WindowCapture/DeviceCapture APIs,  
  and rename existing methods as \*Async variants that return ListenableFutures
- Make Bitmap.writeToTestStorage use the registered PlatformTestStorage instead of hardcoding TestStorage
- Remove ExperimentalTestApi/RequiresOptIn restrictions from captureToBitmap and takeScreenshot APIs

### Core Core-ktx 1.6.0-alpha05

January 26, 2024

`androidx.test:core:1.6.0-alpha05` and `androidx.test:core-ktx:1.6.0-alpha05` are released.

**Bug Fixes**

- Update Activity Scenario reference documentation to fix missing links
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Reference doc cleanup - document previously missing parameters, fix links, etc

### Core Core-ktx 1.6.0-alpha04

December 05, 2023

`androidx.test:core:1.6.0-alpha04` and `androidx.test:core-ktx:1.6.0-alpha04` are released.

**Bug Fixes**

- Activity starts are automatically opted in to allow background activity launches when targetSdk \>= 34

### Core Core-ktx 1.6.0-alpha03

November 29, 2023

`androidx.test:core:1.6.0-alpha03` and `androidx.test:core-ktx:1.6.0-alpha03` are released.

**Bug Fixes**

- Fix ActivityScenario.launchActivityWithResult when targetSdk = 34

**API Changes**

- targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### Core Core-ktx 1.6.0-alpha02

September 18, 2023

`androidx.test:core:1.6.0-alpha02` and `androidx.test:core-ktx:1.6.0-alpha02` are released.

**Features**
\* Updates ViewCapture to accept an optional Rect so that it can work for Compose.

**Bug fixes**

- Fix issue where Activity#isChangingConfigurations is incorrectly false during ActivityScenario#recreate
- Move UiAutomation#takeScreenshot call off main thread.
- Fix captureToBitmap for Views inside a Dialog on APIs \>= 26.

**Dependency changes**
\* minSdkVersion is now 19

### Core Core-ktx 1.6.0-alpha01

March 21, 2023

`androidx.test:core:1.6.0-alpha01` and `androidx.test:core-ktx:1.6.0-alpha01` are released.

**Features**
\* Preliminary support for robolectric was added to ViewCapture.captureToBitmap

**Bug fixes**

- Fix captureToBitmap for DecorView's
- Attempt to improve reliability of DeviceCapture by retrying takeScreenshot

**Dependency changes**

- Update to kotlin stdlib 1.7.22
- Major release toolchain update: now compiled to java8 bytecode
- Update to androidx.test:monitor:1.70-alpha01

## Core 1.5.0

### Core Core-ktx 1.5.0

November 8, 2022

`androidx.test:core:1.5.0` and `androidx.test:core-ktx:1.5.0` are released.

Changes since 1.4.0 include:

**New features**

- Record android Trace spans for ActivityScenario launch and close.
- Add new experimental APIs for screenshots. These APIs will automatically select the highest fidelity for taking screenshots based on platform API level, and support the Automated Test Device (ATD) emulator images.
  - View.captureToBitmap extension function
  - Window.captureRegionToBitmap extension function
  - takeScreenshot()
- Add experimental Bitmap.writeToTestStorage API

**API changes**

- Add ActivityScenario#launchActivityForResult API and modify ActivityScenario#launch to remove use of Bootstrap Activity API. This change should improve performance and stability of ActivityScenario#launch. ActivityScenario#getResult will now enforce that it can only be used with ActivityScenario#launchActivityForResult

**Bug fixes**

- Fix ActivityScenario#launch when targeting and running on Android 33
- Use elapsedRealtime instead of currentTimeMillis to track ActivityScenario timeouts.
- Fix ActivityScenario's issue with starting an Activity from intent with package name in self-instrumenting tests.
- Reduce ActivityScenario overhead by using plain whitebackground and disabling transition animations in internal Activities

**Dependency changes**

- Update to
  - kotlin stdlib 1.7.10
  - androidx.lifecycle:lifecycle-common:2.3.1
  - androidx.annotation:annotation:1.2.0
- Add
  - androidx.test.services:storage:1.4.2
  - com.google.guava:listenablefuture:1.0
  - androidx.concurrent:concurrent-futures:1.1.0

### Core Core-ktx 1.5.0-rc01

October 26, 2022

`androidx.test:core:1.5.0-rc01` and `androidx.test:core-ktx:1.5.0-rc01` are released.

### Core Core-ktx 1.5.0-beta01

October 6, 2022

`androidx.test:core:1.5.0-beta01` and `androidx.test:core-ktx:1.5.0-beta01` are released.

**API changes**

- Annotate new APIs with NonNull/Nullable

### Core Core-ktx 1.5.0-alpha02

August 22, 2022

`androidx.test:core:1.5.0-alpha02` and `androidx.test:core-ktx:1.5.0-alpha02` are released.

**API changes**

- Modify ActivityScenario#launch to remove use of Bootstrap Activity API. This change should improve performance and stability of ActivityScenario#launch. ActivityScenario#getResult will now enforce that it can only be used with ActivityScenario#launchActivityForResult

**Bug fixes**

- Fix ActivityScenario#launch when targeting and running on Android T
- Use elapsedRealtime instead of currentTimeMillis to track ActivityScenario timeouts.

**Dependency changes**

- Update to kotlin stdlib 1.7.10

### Core Core-ktx 1.5.0-alpha01

June 21, 2022

`androidx.test:core:1.5.0-alpha01` and `androidx.test:core-ktx:1.5.0-alpha01` are released.

**API changes**

- Add ActivityScenario#launchActivityForResult API. This API will replace use of ActivityScenario#launch when retrieving activity results.

## Core 1.4.1

### Core Core-ktx 1.4.1-alpha07

June 1, 2022

`androidx.test:core:1.4.1-alpha07` and `androidx.test:core-ktx:1.4.1-alpha07` are released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

**Dependency changes**

- Update to kotlin stdlib 1.6.21

### Core Core-ktx 1.4.1-alpha06

April 28, 2022

`androidx.test:core:1.4.1-alpha06` and `androidx.test:core-ktx:1.4.1-alpha06` are released.

**Bug fixes**
\* Fix ActivityScenario's issue with starting an Activity from intent with package name in self-instrumenting tests.

### Core Core-ktx 1.4.1-alpha05

Mar 21, 2022

`androidx.test:core:1.4.1-alpha05` and `androidx.test:core-ktx:1.4.1-alpha05` are released.

### Core Core-ktx 1.4.1-alpha04

Feb 11, 2022

`androidx.test:core:1.4.1-alpha04` and `androidx.test:core-ktx:1.4.1-alpha04` are released.

**New Features**

- Record android Trace spans for ActivityScenario launch and close.

**Dependency Changes**

- Add androidx.tracing dependency
- Update to kotlin stdlib 1.6.10

### Core Core-ktx 1.4.1-alpha03

Oct 4, 2021

`androidx.test:core:1.4.1-alpha03` and `androidx.test:core-ktx:1.4.1-alpha03` are released.

**Bug fixes**

- Fix visibility of View.captureToBitmap and Window.captureRegionToBitmap extensions
- Add clearer exception handling to Bitmap.writeToTestStorage and screenshot methods

### Core Core-ktx 1.4.1-alpha02

Sept 28, 2021

`androidx.test:core:1.4.1-alpha02` and `androidx.test:core-ktx:1.4.1-alpha02` are released.

**New Features**

- Add new experimental APIs for screenshots:
  - View.captureToBitmap extension function
  - Window.captureRegionToBitmap extension function
  - takeScreenshot()
- Add experimental Bitmap.writeToTestStorage API

**Dependency Changes**

- Add dependencies to
  - kotlin stdlib 1.5.31
  - androidx.test.services:storage:1.4.1-alpha02
  - com.google.guava:listenablefuture:1.0
  - androidx.concurrent:concurrent-futures:1.1.0
- Update dependency versions to
  - androidx.lifecycle:lifecycle-common:2.3.1
  - androidx.annotation:annotation:1.2.0

### Core Core-ktx 1.4.1-alpha01

Aug 23, 2021

`androidx.test:core:1.4.1-alpha01` and `androidx.test:core-ktx:1.4.1-alpha01` are released.

**Bug Fixes**

- Reduce ActivityScenario overhead by using plain whitebackground and disabling transition animations in internal Activities

**Dependency Changes**

- -ktx: Explicitly depend on kotlin stdlib 1.4.30

## Espresso 3.7.0

### Espresso 3.7.0

July 30, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0`
- `androidx.test.espresso:espresso-core:3.7.0`
- `androidx.test.espresso:espresso-contrib:3.7.0`
- `androidx.test.espresso:espresso-idling-resource:3.7.0`
- `androidx.test.espresso:espresso-intents:3.7.0`
- `androidx.test.espresso:espresso-remote:3.7.0`
- `androidx.test.espresso:espresso-web:3.7.0`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0`
- `androidx.test.espresso.idling:idling-net:3.7.0`

Changes since last stable 3.6.1 release include:

**Bug Fixes**

- Fix deadlock in espresso in Robolectric INSTRUMENTATION_TEST + paused looper.
- Refactor espresso's MessageQueue access into a TestLooperManagerCompat class, and use new TestLooperManager APIs when available.
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - androidx.concurrent-futures 1.2.0
  - kotlin 1.9.0
- Only hold main Looper's TestLooperManager during interrogation
- Fix #2349, where multi-process + different rotation on 2 activities would instantly timeout when waiting for the UI to rotate.
- Use getSystemService instead of reflective InputManager.getInstance

**API Changes**

- Update to minSdkVersion 21

### Espresso 3.7.0-rc01

July 14, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-rc01`
- `androidx.test.espresso:espresso-core:3.7.0-rc01`
- `androidx.test.espresso:espresso-contrib:3.7.0-rc01`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-rc01`
- `androidx.test.espresso:espresso-intents:3.7.0-rc01`
- `androidx.test.espresso:espresso-remote:3.7.0-rc01`
- `androidx.test.espresso:espresso-web:3.7.0-rc01`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-rc01`
- `androidx.test.espresso.idling:idling-net:3.7.0-rc01`

### Espresso 3.7.0-beta01

June 30, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-beta01`
- `androidx.test.espresso:espresso-core:3.7.0-beta01`
- `androidx.test.espresso:espresso-contrib:3.7.0-beta01`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-beta01`
- `androidx.test.espresso:espresso-intents:3.7.0-beta01`
- `androidx.test.espresso:espresso-remote:3.7.0-beta01`
- `androidx.test.espresso:espresso-web:3.7.0-beta01`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-beta01`
- `androidx.test.espresso.idling:idling-net:3.7.0-beta01`

### Espresso 3.7.0-alpha04

June 13, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-alpha04`
- `androidx.test.espresso:espresso-core:3.7.0-alpha04`
- `androidx.test.espresso:espresso-contrib:3.7.0-alpha04`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-alpha04`
- `androidx.test.espresso:espresso-intents:3.7.0-alpha04`
- `androidx.test.espresso:espresso-remote:3.7.0-alpha04`
- `androidx.test.espresso:espresso-web:3.7.0-alpha04`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-alpha04`
- `androidx.test.espresso.idling:idling-net:3.7.0-alpha04`

**Bug Fixes**

- Fix #2349, where multi-process + different rotation on 2 activities would instantly timeout when waiting for the UI to rotate.
- Use getSystemService instead of reflective InputManager.getInstance

### Espresso 3.7.0-alpha03

April 23, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-alpha03`
- `androidx.test.espresso:espresso-core:3.7.0-alpha03`
- `androidx.test.espresso:espresso-contrib:3.7.0-alpha03`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-alpha03`
- `androidx.test.espresso:espresso-intents:3.7.0-alpha03`
- `androidx.test.espresso:espresso-remote:3.7.0-alpha03`
- `androidx.test.espresso:espresso-web:3.7.0-alpha03`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-alpha03`
- `androidx.test.espresso.idling:idling-net:3.7.0-alpha03`

**Bug Fixes**

- Downgrade to kotlin 1.9
- Only hold main Looper's TestLooperManager during interrogation

### Espresso 3.7.0-alpha02

March 27, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-alpha02`
- `androidx.test.espresso:espresso-core:3.7.0-alpha02`
- `androidx.test.espresso:espresso-contrib:3.7.0-alpha02`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-alpha02`
- `androidx.test.espresso:espresso-intents:3.7.0-alpha02`
- `androidx.test.espresso:espresso-remote:3.7.0-alpha02`
- `androidx.test.espresso:espresso-web:3.7.0-alpha02`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-alpha02`
- `androidx.test.espresso.idling:idling-net:3.7.0-alpha02`

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - androidx.concurrent-futures 1.2.0
  - kotlin 2.1.0

### Espresso 3.7.0-alpha01

February 03, 2025

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.7.0-alpha01`
- `androidx.test.espresso:espresso-core:3.7.0-alpha01`
- `androidx.test.espresso:espresso-contrib:3.7.0-alpha01`
- `androidx.test.espresso:espresso-idling-resource:3.7.0-alpha01`
- `androidx.test.espresso:espresso-intents:3.7.0-alpha01`
- `androidx.test.espresso:espresso-remote:3.7.0-alpha01`
- `androidx.test.espresso:espresso-web:3.7.0-alpha01`
- `androidx.test.espresso.idling:idling-concurrent:3.7.0-alpha01`
- `androidx.test.espresso.idling:idling-net:3.7.0-alpha01`

**Bug Fixes**

- Fix deadlock in espresso in Robolectric INSTRUMENTATION_TEST + paused looper.
- Refactor espresso's MessageQueue access into a TestLooperManagerCompat class, and use new TestLooperManager APIs when available.

**API Changes**

- Update to minSdkVersion 21

### Espresso 3.6.1

June 26, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.1`
- `androidx.test.espresso:espresso-core:3.6.1`
- `androidx.test.espresso:espresso-contrib:3.6.1`
- `androidx.test.espresso:espresso-idling-resource:3.6.1`
- `androidx.test.espresso:espresso-intents:3.6.1`
- `androidx.test.espresso:espresso-remote:3.6.1`
- `androidx.test.espresso:espresso-web:3.6.1`
- `androidx.test.espresso.idling:idling-concurrent:3.6.1`
- `androidx.test.espresso.idling:idling-net:3.6.1`

**Bug Fixes**

- Upgrade accessibilitytestframework version (back) to 3.1.2.

### Espresso 3.6.0

June 24, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0`
- `androidx.test.espresso:espresso-core:3.6.0`
- `androidx.test.espresso:espresso-contrib:3.6.0`
- `androidx.test.espresso:espresso-idling-resource:3.6.0`
- `androidx.test.espresso:espresso-intents:3.6.0`
- `androidx.test.espresso:espresso-remote:3.6.0`
- `androidx.test.espresso:espresso-web:3.6.0`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0`
- `androidx.test.espresso.idling:idling-net:3.6.0`

Changes since last stable release 3.5.1 include:

**Bug Fixes**

- Remove unused androidx.test.annotation dependency
- Fix slow inRoot operations in Robolectric
- Use PlatformTestStorageRegistry.getInstance consistently instead of passing a reference around
- Remove TODO from InteractionResponse public ref docs
- Fix typo in AdapterDataLoaderAction error message
- Replace use of guava with Java collections and inlining
- Reference doc cleanup - document previously missing parameters, fix links, etc
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Stop posting empty tasks to background threads when running in non-remote mode
- Better handle exceptions that may occur in DefaultFailureHandler's hierarchy capture and screenshot process.
- Fix the description of IsPlatformPopup to match the behavior.
- Fix deprecated obtainMovement impl that used the wrong coordinates.
- Replace broken links to junit.org javadoc with @link.

**API Changes**

- Add ViewActions.captureToBitmap
- Add waitForClose to DrawerActions.
- Mark generated IInteractionExecutionStatus class as RestrictTo LIBRARY_GROUP
- Remove ExperimentalTestApi from RuntimePermissionStubber
- Adding a new IsActivatedMatcher to verify if it is activated or not.
- Makes Espresso.onIdle() work on the main thread to allow for draining the main thread from the main thread.
- minSdkVersion is now 19, targetSdkVersion is now 34
- Add scrollTo variant that allows scrolling to 90+% displayed views
- Deprecate EspressoOptional in favor of @Nullable.
- Allow customizing espresso's default failure handler to disable screenshots on failures

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17. This should resolve IncompatibleClassChangeErrors (https://github.com/android/android-test/issues/1642)
  - remove internal guava usage, which resulted in a binary size reduction
  - release aars are no longer proguarded

### Espresso 3.6.0-rc01

May 30, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-rc01`
- `androidx.test.espresso:espresso-core:3.6.0-rc01`
- `androidx.test.espresso:espresso-contrib:3.6.0-rc01`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-rc01`
- `androidx.test.espresso:espresso-intents:3.6.0-rc01`
- `androidx.test.espresso:espresso-remote:3.6.0-rc01`
- `androidx.test.espresso:espresso-web:3.6.0-rc01`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-rc01`
- `androidx.test.espresso.idling:idling-net:3.6.0-rc01`

### Espresso 3.6.0-beta01

May 16, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-beta01`
- `androidx.test.espresso:espresso-core:3.6.0-beta01`
- `androidx.test.espresso:espresso-contrib:3.6.0-beta01`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-beta01`
- `androidx.test.espresso:espresso-intents:3.6.0-beta01`
- `androidx.test.espresso:espresso-remote:3.6.0-beta01`
- `androidx.test.espresso:espresso-web:3.6.0-beta01`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-beta01`
- `androidx.test.espresso.idling:idling-net:3.6.0-beta01`

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### Espresso 3.6.0-alpha04

April 26, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-alpha04`
- `androidx.test.espresso:espresso-core:3.6.0-alpha04`
- `androidx.test.espresso:espresso-contrib:3.6.0-alpha04`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-alpha04`
- `androidx.test.espresso:espresso-intents:3.6.0-alpha04`
- `androidx.test.espresso:espresso-remote:3.6.0-alpha04`
- `androidx.test.espresso:espresso-web:3.6.0-alpha04`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-alpha04`
- `androidx.test.espresso.idling:idling-net:3.6.0-alpha04`

**Bug Fixes**

- Fix slow inRoot operations in Robolectric
- Use PlatformTestStorageRegistry.getInstance consistently instead of passing a reference around
- Remove TODO from InteractionResponse public ref docs

**New Features**

- Add waitForClose to DrawerActions.

**API Changes**

- Adapt to ViewCapture API changes
- Delete ViewInteraction.captureToBitmap in favor of ViewActions.captureToBitmap, and promote to a stable API from ExperimentalTestApi

### Espresso 3.6.0-alpha03

January 26, 2024

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-alpha03`
- `androidx.test.espresso:espresso-core:3.6.0-alpha03`
- `androidx.test.espresso:espresso-contrib:3.6.0-alpha03`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-alpha03`
- `androidx.test.espresso:espresso-intents:3.6.0-alpha03`
- `androidx.test.espresso:espresso-remote:3.6.0-alpha03`
- `androidx.test.espresso:espresso-web:3.6.0-alpha03`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-alpha03`
- `androidx.test.espresso.idling:idling-net:3.6.0-alpha03`

**Bug Fixes**

- Fix typo in AdapterDataLoaderAction error message
- Remove Kotlin collect stdlib calls in Java from espresso
- Reference doc cleanup - document previously missing parameters, fix links, etc
- Remove Kotlin StringKt calls from Java code
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Stop posting empty tasks to background threads when running in non-remote mode
- Better handle exceptions that may occur in DefaultFailureHandler's hierarchy capture and screenshot process.

**API Changes**

- Mark generated IInteractionExecutionStatus class as RestrictTo LIBRARY_GROUP
- Remove ExperimentalTestApi from RuntimePermissionStubber

### Espresso 3.6.0-alpha02

November 29, 2023

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-alpha02`
- `androidx.test.espresso:espresso-core:3.6.0-alpha02`
- `androidx.test.espresso:espresso-contrib:3.6.0-alpha02`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-alpha02`
- `androidx.test.espresso:espresso-intents:3.6.0-alpha02`
- `androidx.test.espresso:espresso-remote:3.6.0-alpha02`
- `androidx.test.espresso:espresso-web:3.6.0-alpha02`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-alpha02`
- `androidx.test.espresso.idling:idling-net:3.6.0-alpha02`

**Bug Fixes**

- Fix the description of IsPlatformPopup to match the behavior.
- Fix deprecated obtainMovement impl that used the wrong coordinates.
- Replace broken links to junit.org javadoc with @link.

**API Changes**

- Adding a new IsActivatedMatcher to verify if it is activated or not.
- Makes Espresso.onIdle() work on the main thread to allow for draining the main thread from the main thread.
- minSdkVersion is now 19, targetSdkVersion is now 34
- Add scrollTo variant that allows scrolling to 90+% displayed views

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### Espresso 3.6.0-alpha01

March 21, 2023

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.6.0-alpha01`
- `androidx.test.espresso:espresso-core:3.6.0-alpha01`
- `androidx.test.espresso:espresso-contrib:3.6.0-alpha01`
- `androidx.test.espresso:espresso-idling-resource:3.6.0-alpha01`
- `androidx.test.espresso:espresso-intents:3.6.0-alpha01`
- `androidx.test.espresso:espresso-remote:3.6.0-alpha01`
- `androidx.test.espresso:espresso-web:3.6.0-alpha01`
- `androidx.test.espresso.idling:idling-concurrent:3.6.0-alpha01`
- `androidx.test.espresso.idling:idling-net:3.6.0-alpha01`

**API changes**

- Deprecate EspressoOptional in favor of @Nullable.
- Allow customizing espresso's default failure handler to disable screenshots on failures

**Dependency changes**

- Update to androidx.test:monitor:1.7.0-alpha01, androidx.test:core:1.6.0-alpha01 and androidx.test:runner:1.6.0-alpha01
- Update to kotlin stdlib 1.7.22
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11. This should resolve IncompatibleClassChangeErrors (https://github.com/android/android-test/issues/1642)
  - remove internal guava usage with kotlin stdlib, which resulted in a binary size reduction
  - release aars are no longer proguarded

## Espresso 3.5.0

### Espresso 3.5.1

January 3, 2023

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.1`
- `androidx.test.espresso:espresso-core:3.5.1`
- `androidx.test.espresso:espresso-contrib:3.5.1`
- `androidx.test.espresso:espresso-idling-resource:3.5.1`
- `androidx.test.espresso:espresso-intents:3.5.1`
- `androidx.test.espresso:espresso-remote:3.5.1`
- `androidx.test.espresso:espresso-web:3.5.1`
- `androidx.test.espresso.idling:idling-concurrent:3.5.1`
- `androidx.test.espresso.idling:idling-net:3.5.1`

**Bug fixes**

- Reference doc cleanup: Correct parameter names and remove obsolete 'beta' statements from IdlingThreadPoolExecutor and UriIdlingResource

**Dependency changes**

- Update to androidx.test:monitor:1.6.1 to supporting saving screenshots on espresso test failures without test storage

### Espresso 3.5.0

November 8, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0`
- `androidx.test.espresso:espresso-core:3.5.0`
- `androidx.test.espresso:espresso-contrib:3.5.0`
- `androidx.test.espresso:espresso-idling-resource:3.5.0`
- `androidx.test.espresso:espresso-intents:3.5.0`
- `androidx.test.espresso:espresso-remote:3.5.0`
- `androidx.test.espresso:espresso-web:3.5.0`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0`
- `androidx.test.espresso.idling:idling-net:3.5.0`

**New Features**

- Record android Trace spans for Espresso actions
- Espresso's DefaultFailureHandler now saves a screenshot on test failures to TestStorage
- Add experimental ViewInteraction.captureToBitmap extension function
- Save view hierarchy to a file on failures

**API changes**

- Promote ViewMatchers hasTextColor and hasBackground as stable APIs
- Add IntentsRule
- Add inverted matchers for IntentMatchers.hasExtraWithKey() and BundleMatchers.hasKey()
- Add a ViewAction that scrolls to the last position in a RecyclerView.
- Add IntentMatcher.hasExtra API

**Bug fixes**

- Preserve tool type on up event
- Make IdlingRegistry more thread-safe.
- Support other views for scrollTo()
- Remove unnecessary `interruptEspressoTasks` warning logs for each Espresso interaction on Robolectric.
- Remove timeout in CloseKeyboardAction when running under Robolectric
- Use consistent InputDevice source for input gesture injection
- Support simulating ActivityNotFoundExceptions in Espresso Intents.
- Truncate view hierarchy in exception messages when it gets too large.
- Display number and list of ambiguously matched views.
- Validate that onView.check/perform() is invoked on the UI thread

**Dependency changes**

- Update to
  - kotlin stdlib 1.7.10
  - jsr305:2.0.2
  - tagsoup:1.2.1
  - androidx.annotation:1.2.0
- contrib:
  - update to drawer 1.1.1, recycler view 1.2.1, material 1.4.0

### Espresso 3.5.0-rc01

October 26, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-rc01`
- `androidx.test.espresso:espresso-core:3.5.0-rc01`
- `androidx.test.espresso:espresso-contrib:3.5.0-rc01`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-rc01`
- `androidx.test.espresso:espresso-intents:3.5.0-rc01`
- `androidx.test.espresso:espresso-remote:3.5.0-rc01`
- `androidx.test.espresso:espresso-web:3.5.0-rc01`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-rc01`
- `androidx.test.espresso.idling:idling-net:3.5.0-rc01`

### Espresso 3.5.0-beta02

October 21, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-beta02`
- `androidx.test.espresso:espresso-core:3.5.0-beta02`
- `androidx.test.espresso:espresso-contrib:3.5.0-beta02`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-beta02`
- `androidx.test.espresso:espresso-intents:3.5.0-beta02`
- `androidx.test.espresso:espresso-remote:3.5.0-beta02`
- `androidx.test.espresso:espresso-web:3.5.0-beta02`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-beta02`
- `androidx.test.espresso.idling:idling-net:3.5.0-beta02`

**API changes**

- Promote ViewMatchers hasTextColor and hasBackground as stable APIs

**Bug fixes**

- Fix recyclerview ClassNotFoundExceptions in scrollTo

**Dependency changes**

### Espresso 3.5.0-beta01

October 6, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-beta01`
- `androidx.test.espresso:espresso-core:3.5.0-beta01`
- `androidx.test.espresso:espresso-contrib:3.5.0-beta01`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-beta01`
- `androidx.test.espresso:espresso-intents:3.5.0-beta01`
- `androidx.test.espresso:espresso-remote:3.5.0-beta01`
- `androidx.test.espresso:espresso-web:3.5.0-beta01`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-beta01`
- `androidx.test.espresso.idling:idling-net:3.5.0-beta01`

**API changes**

- Annotate new APIs introduced since 3.4.0 with NonNull/Nullable
- Add IntentsRule API

**Bug fixes**

- Make IdlingRegistry more thread-safe.
- Support other views for scrollTo()

**Dependency changes**

- Update to kotlin stdlib 1.7.10
- Update to jsr305:2.0.2
- Update to tagsoup:1.2.1

### Espresso 3.5.0-alpha07

June 1, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha07`
- `androidx.test.espresso:espresso-core:3.5.0-alpha07`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha07`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha07`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha07`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha07`
- `androidx.test.espresso:espresso-web:3.5.0-alpha07`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha07`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha07`

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

**Dependency changes**

- Update to kotlin stdlib 1.6.21

### Espresso 3.5.0-alpha06

April 28, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha06`
- `androidx.test.espresso:espresso-core:3.5.0-alpha06`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha06`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha06`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha06`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha06`
- `androidx.test.espresso:espresso-web:3.5.0-alpha06`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha06`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha06`

**Bug Fixes**

- Remove unncessary `interruptEspressoTasks` warning logs for each Espresso interaction on Robolectric.

### Espresso 3.5.0-alpha05

Mar 21, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha05`
- `androidx.test.espresso:espresso-core:3.5.0-alpha05`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha05`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha05`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha05`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha05`
- `androidx.test.espresso:espresso-web:3.5.0-alpha05`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha05`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha05`

**Bug Fixes**

- Remove timeout in CloseKeyboardAction when running under Robolectric

### Espresso 3.5.0-alpha04

Feb 11, 2022

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha04`
- `androidx.test.espresso:espresso-core:3.5.0-alpha04`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha04`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha04`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha04`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha04`
- `androidx.test.espresso:espresso-web:3.5.0-alpha04`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha04`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha04`

**API Changes**

- Add inverted matchers for IntentMatchers.hasExtraWithKey() and BundleMatchers.hasKey()
- Add a ViewAction that scrolls to the last position in a RecyclerView.

**New Features**

- Record android Trace spans for Espresso actions

**Bug Fixes**

- Use consistent InputDevice source for input gesture injection
- Support simulating ActivityNotFoundExceptions in Espresso Intents.
- Truncate view hierarchy in exception messages when it gets too large.
- Display number and list of ambiguously matched views.

**Dependency Changes**

- Update to kotlin stdlib 1.6.10

### Espresso 3.5.0-alpha03

Oct 4, 2021

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha03`
- `androidx.test.espresso:espresso-core:3.5.0-alpha03`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha03`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha03`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha03`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha03`
- `androidx.test.espresso:espresso-web:3.5.0-alpha03`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha03`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha03`

**New features**

- Espresso's DefaultFailureHandler now saves a screenshot on test failures to TestStorage

**Bug fixes**

- Fix visibility and functionality of ViewInteraction.captureToBitmap
- Validate that onView.check/perform() is invoked on the UI thread

### Espresso 3.5.0-alpha02

Sept 28, 2021

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha02`
- `androidx.test.espresso:espresso-core:3.5.0-alpha02`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha02`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha02`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha02`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha02`
- `androidx.test.espresso:espresso-web:3.5.0-alpha02`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha02`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha02`

**New features**

- Add experimental ViewInteraction.captureToBitmap extension function

**Dependency Changes**

- all:
  - update to androidx.annotation:1.2.0
- core:
  - update to kotlin stdlib 1.5.31
- contrib:
  - update to drawer 1.1.1, recycler view 1.2.1, materual 1.4.0

### Espresso 3.5.0-alpha01

Aug 23, 2021

The following artifacts were released:

- `androidx.test.espresso:espresso-accessibility:3.5.0-alpha01`
- `androidx.test.espresso:espresso-core:3.5.0-alpha01`
- `androidx.test.espresso:espresso-contrib:3.5.0-alpha01`
- `androidx.test.espresso:espresso-idling-resource:3.5.0-alpha01`
- `androidx.test.espresso:espresso-intents:3.5.0-alpha01`
- `androidx.test.espresso:espresso-remote:3.5.0-alpha01`
- `androidx.test.espresso:espresso-web:3.5.0-alpha01`
- `androidx.test.espresso.idling:idling-concurrent:3.5.0-alpha01`
- `androidx.test.espresso.idling:idling-net:3.5.0-alpha01`

**New features**

- Save view hierarchy to a file on failures

**API Changes**

- Add IntentMatcher.hasExtra API

**Dependency Changes**

- core: Depend on kotlin stdlib 1.4.30

## Espresso Device 1.1.0

### Espresso Device 1.1.0

July 30, 2025

`androidx.test.espresso:espresso-device:1.1.0` is released.

Changes since last stable 1.0.1 release include:

**Bug Fixes**

- Fix DisplaySizeRule not consistently restoring to original emulator state for failing tests
- Support using DisplaySizeRule without an activity in the resumed state
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - gRPC 1.71.0
  - kotlin 1.9.0
  - kotlin coroutines 1.10.1
- Add support for setting screen orientation with multiple resumed activities
- Fix concurrent modification issue when setting screen orientation and fold modes
- Adjust reference docs to state set up guide is now located at https://developer.android.com/studio/test/espresso-api#set_up_your_project_for_the_espresso_device_api

**API Changes**

- Update WidthSizeClass and HeightSizeClass to use androidx.window size classes
- Update to minSdkVersion 21

### Espresso Device 1.1.0-rc01

July 14, 2025

`androidx.test.espresso:espresso-device:1.1.0-rc01` is released.

### Espresso Device 1.1.0-beta01

June 30, 2025

`androidx.test.espresso:espresso-device:1.1.0-beta01` is released.

### Espresso Device 1.1.0-alpha03

April 23, 2025

`androidx.test.espresso:espresso-device:1.1.0-alpha03` is released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### Espresso Device 1.1.0-alpha02

March 27, 2025

`androidx.test.espresso:espresso-device:1.1.0-alpha02` is released.

**Bug Fixes**

- Fix DisplaySizeRule not consistently restoring to original emulator state for failing tests
- Support using DisplaySizeRule without an activity in the resumed state
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - gRPC 1.71.0
  - kotlin 2.1.0
  - kotlin coroutines 1.10.1

### Espresso Device 1.1.0-alpha01

February 03, 2025

`androidx.test.espresso:espresso-device:1.1.0-alpha01` is released.

**Bug Fixes**

- Add support for setting screen orientation with multiple resumed activities
- Fix concurrent modification issue when setting screen orientation and fold modes
- Adjust reference docs to state set up guide is now located at https://developer.android.com/studio/test/espresso-api#set_up_your_project_for_the_espresso_device_api

**API Changes**
\* Update WidthSizeClass and HeightSizeClass to use androidx.window size classes
\* Update to minSdkVersion 21

### Espresso Device 1.0.1

June 26, 2024

`androidx.test.espresso:espresso-device:1.0.1` is released.

### Espresso Device 1.0.0

June 24, 2024

`androidx.test.espresso:espresso-device:1.0.0` is released.

Initial release!

**New Features**

- APIs for rotating and folding devices
- APIs for filtering tests based on device mode and display

### Espresso Device 1.0.0-rc01

May 30, 2024

`androidx.test.espresso:espresso-device:1.0.0-rc01` is released.

**Bug Fixes**

- Add support for setting screen orientation with multiple resumed activities
- Fix concurrent modification issue when setting screen orientation and fold modes

### Espresso Device 1.0.0-beta01

May 16, 2024

`androidx.test.espresso:espresso-device:1.0.0-beta01` is released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### Espresso Device 1.0.0-alpha09

April 26, 2024

`androidx.test.espresso:espresso-device:1.0.0-alpha09` is released.

**Bug Fixes**
\* Clarify error messaging for setting screen orientation without a resumed activity
\* Support setting screen orientation on half-folded API 34 physical devices

**API Changes**

- Made ScreenOrientationRule's defaultOrientation parameter optional

### Espresso Device 1.0.0-alpha08

January 26, 2024

`androidx.test.espresso:espresso-device:1.0.0-alpha08` is released.

**Bug Fixes**

- Add better error messaging when process does not have INTERNET permission
- Make exception class references in Espresso Device documentation clickable links

**API Changes**
\* Remove ExperimentalTestApi from androidx.test.filter.CustomFilter

### Espresso Device 1.0.0-alpha07

November 29, 2023

`androidx.test.espresso:espresso-device:1.0.0-alpha07` is released.

**API Changes**

- Support setting device modes on physical devices

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### Espresso Device 1.0.0-alpha06

September 18, 2023

The following artifacts were released:

- `androidx.test.espresso:espresso-device:1.0.0-alpha06`

**API changes**
\* Support setting screen orientation on physical devices that are open
\* Remove ActionContext interface

**Dependency changes**
\* minSdkVersion is now 19

### Espresso Device 1.0.0-alpha05

May 4, 2023

The following artifacts were released:

- `androidx.test.espresso:espresso-device:1.0.0-alpha05`

**API changes**

- Add experimental APIs for rotating and folding emulators

## JUnit Extensions 1.3.0

### ext.junit 1.3.0

July 30, 2025

`androidx.test.ext:junit:1.3.0` and `androidx.test.ext:junit-ktx:1.3.0`
are released.

Changes since last stable release 1.2.1 include:

**Bug Fixes**

- Fixed the link to the deprecated `androidx.test.rule.ActivityTestRule` in the class description.
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - kotlin 1.9.0

**API Changes**

- Update to minSdkVersion 21

### ext.junit 1.3.0-rc01

July 14, 2025

`androidx.test.ext:junit:1.3.0-rc01` and `androidx.test.ext:junit-ktx:1.3.0-rc01`
are released.

### ext.junit 1.3.0-beta01

June 30, 2025

`androidx.test.ext:junit:1.3.0-beta01` and `androidx.test.ext:junit-ktx:1.3.0-beta01`
are released.

### ext.junit 1.3.0-alpha03

April 23, 2025

`androidx.test.ext:junit:1.3.0-alpha03` and `androidx.test.ext:junit-ktx:1.3.0-alpha03`
are released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### ext.junit 1.3.0-alpha02

March 27, 2025

`androidx.test.ext:junit:1.3.0-alpha02` and `androidx.test.ext:junit-ktx:1.3.0-alpha02`
are released.

**Bug Fixes**

- Fixed the link to the deprecated `androidx.test.rule.ActivityTestRule` in the class description.
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
  - kotlin 2.1.0

### ext.junit 1.3.0-alpha01

February 03, 2025

`androidx.test.ext:junit:1.3.0-alpha01` and `androidx.test.ext:junit-ktx:1.3.0-alpha01` are released.

**API Changes**

- Update to minSdkVersion 21

### ext.junit 1.2.1

June 26, 2024

`androidx.test.ext:junit:1.2.1` and `androidx.test.ext:junit-ktx:1.2.1` are released.

### ext.junit 1.2.0

June 24, 2024

`androidx.test.ext:junit:1.2.0` and `androidx.test.ext:junit-ktx:1.2.0` are released.

Changes since last stable release 1.1.5 include:

**API changes**

- Create DeleteFilesRule: an API for removing files between test case execution
- Add AppComponentFactoryRule
- minSdkVersion is now 19, targetSdkVersion is now 34

**Bug Fixes**

- Reference doc cleanup - document previously missing parameters, fix links, etc

**New features**

- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17.
- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### ext.junit 1.2.0-rc01

May 30, 2024

`androidx.test.ext:junit:1.2.0-rc01` and `androidx.test.ext:junit-ktx:1.2.0-rc01` are released.

### ext.junit 1.2.0-beta01

May 16, 2024

`androidx.test.ext:junit:1.2.0-beta01` and `androidx.test.ext:junit-ktx:1.2.0-beta01` are released.

### ext.junit 1.2.0-alpha04

April 26, 2024

`androidx.test.ext:junit:1.2.0-alpha04` and `androidx.test.ext:junit-ktx:1.2.0-alpha04` are released.

**Bug Fixes**

- Use PlatformTestStorage instead of TestStorage in DeleteFilesRule

### ext.junit 1.2.0-alpha03

January 26, 2024

`androidx.test.ext:junit:1.2.0-alpha03` and `androidx.test.ext:junit-ktx:1.2.0-alpha03` are released.

**Bug Fixes**

- Reference doc cleanup - document previously missing parameters, fix links, etc

### ext.junit 1.2.0-alpha02

November 29, 2023

`androidx.test.ext:junit:1.2.0-alpha02` and `androidx.test.ext:junit-ktx:1.2.0-alpha02` are released.

**API Changes**

- Add AppComponentFactoryRule
- minSdkVersion is now 19, targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### ext.junit 1.2.0-alpha01

March 21, 2023

`androidx.test.ext:junit:1.2.0-alpha01` and `androidx.test.ext:junit-ktx:1.2.0-alpha01` are released.

**API changes**

- Create DeleteFilesRule: an API for removing files between test case execution

**Dependency changes**

- Update to androidx.test:monitor:1.7.0-alpha01, androidx.test:core:1.6.0-alpha01, androidx.test.services:storage:1.5.0-alpha01
- Update to kotlin stdlib 1.7.22
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11.

## JUnit Extensions 1.1.5

### ext.junit 1.1.5

January 3, 2023

`androidx.test.ext:junit:1.1.5` and `androidx.test.ext:junit-ktx:1.1.5` are released.

**Bug fixes**

- Fix reference doc formatting for ActivityScenarioRule

## JUnit Extensions 1.1.4

### ext.junit 1.1.4

November 8, 2022

`androidx.test.ext:junit:1.1.4` and `androidx.test.ext:junit-ktx:1.1.4` are released.

Changes since 1.1.3 include:

**Dependency changes**

- Update to kotlin stdlib 1.7.10
- Update to org.junit:junit:4.13.2

### ext.junit 1.1.4-rc01

October 26, 2022

`androidx.test.ext:junit:1.1.4-rc01` and `androidx.test.ext:junit-ktx:1.1.4-rc01` are released.

### ext.junit 1.1.4-beta01

October 6, 2022

`androidx.test.ext:junit:1.1.4-beta01` and `androidx.test.ext:junit-ktx:1.1.4-beta01` are released.

**Dependency changes**

- Update to kotlin stdlib 1.7.10

### ext.junit 1.1.4-alpha07

June 1, 2022

`androidx.test.ext:junit:1.1.4-alpha07` and `androidx.test.ext:junit-ktx:1.1.4-alpha07` are released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

**Dependency changes**

- Update to kotlin stdlib 1.6.21

### ext.junit 1.1.4-alpha06

April 28, 2022

`androidx.test.ext:junit:1.1.4-alpha06` and `androidx.test.ext:junit-ktx:1.1.4-alpha06` are released.

**Bug Fixes**

- Minor fix to the `AndroidJUnit4` javadoc.

### ext.junit 1.1.4-alpha05

Mar 21, 2022

`androidx.test.ext:junit:1.1.4-alpha05` and `androidx.test.ext:junit-ktx:1.1.4-alpha05` are released.

### ext.junit 1.1.4-alpha04

Feb 11, 2022

`androidx.test.ext:junit:1.1.4-alpha04` and `androidx.test.ext:junit-ktx:1.1.4-alpha04` are released.

\*\* Dependency Changes

- Update to kotlin stdlib 1.6.10

### ext.junit 1.1.4-alpha03

Oct 4, 2021

`androidx.test.ext:junit:1.1.4-alpha03` and `androidx.test.ext:junit-ktx:1.1.4-alpha03` are released.

### ext.junit 1.1.4-alpha02

Sept 28, 2021

`androidx.test.ext:junit:1.1.4-alpha02` and `androidx.test.ext:junit-ktx:1.1.4-alpha02` are released.

**Dependency Changes**

- Update to
  - kotlin stdlib 1.5.31
  - org.junit:junit:4.13.2

### ext.junit 1.1.4-alpha01

Aug 23, 2021

`androidx.test.ext:junit:1.1.4-alpha01` and `androidx.test.ext:junit-ktx:1.1.4-alpha01` are released.

**Dependency Changes**

- -ktx: Explicitly depend on kotlin stdlib 1.4.30

## Junit-Gtest 1.0

### Junit-Gtest 1.0.0-alpha01

March 23, 2022

`androidx.test.ext:junit-gtest:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868/test/ext/junit-gtest)

**Features in first release**

- JUnit Gtest is a new library which includes a JUnit runner for running Gtest suites on connected devices.

## Truth Extensions 1.7.0

### ext.truth 1.7.0

July 30, 2025

`androidx.test.ext:truth:1.7.0` is released.

Changes since last stable 1.6.0 release include:

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

**API Changes**

- Update to minSdkVersion 21

### ext.truth 1.7.0

July 30, 2025

`androidx.test.ext:truth:1.7.0` is released.

### ext.truth 1.7.0-rc01

July 14, 2025

`androidx.test.ext:truth:1.7.0-rc01` is released.

### ext.truth 1.7.0-beta01

June 30, 2025

`androidx.test.ext:truth:1.7.0-beta01` is released.

### ext.truth 1.7.0-alpha03

April 23, 2025

`androidx.test.ext:truth:1.7.0-alpha03` is released.

### ext.truth 1.7.0-alpha02

March 27, 2025

`androidx.test.ext:truth:1.7.0-alpha02` is released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

### ext.truth 1.7.0-alpha01

February 03, 2025

`androidx.test.ext:truth:1.7.0-alpha01` is released.

**API Changes**

- Update to minSdkVersion 21

### ext.truth 1.6.0

June 24, 2024

`androidx.test.ext:truth:1.6.0` is released.

Changes since last stable release 1.5.0 include:

**API Changes**

- Remove unused androidx.test.annotation dependency
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- minSdkVersion is now 19, targetSdk is now 34
- Added `PersistableBundleSubject`

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17.

### ext.truth 1.6.0-rc01

May 30, 2024

`androidx.test.ext:truth:1.6.0-rc01` is released.

### ext.truth 1.6.0-beta01

May 16, 2024

`androidx.test.ext:truth:1.6.0-beta01` is released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### ext.truth 1.6.0-alpha04

April 26, 2024

`androidx.test.ext:truth:1.6.0-alpha04` is released.

**New Features**

- Added `byteArray()` method to `BundleSubject`.

### ext.truth 1.6.0-alpha03

January 26, 2024

`androidx.test.ext:truth:1.6.0-alpha03` is released.

**Bug Fixes**

- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)

**New Features**

- Added `PersistableBundleSubject`

### ext.truth 1.6.0-alpha02

November 29, 2023

`androidx.test.ext:truth:1.6.0-alpha02` is released.

**API Changes**

- minSdkVersion is now 19, targetSdk is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### ext.truth 1.6.0-alpha01

March 21, 2022

`androidx.test.ext:truth:1.6.0-alpha01` is released.

**Dependency changes**

- Update to androidx.test:core:1.6.0-alpha01
- Update to kotlin stdlib 1.7.22
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11.

## Truth Extensions 1.5.0

### ext.truth 1.5.0

November 8, 2022

`androidx.test.ext:truth:1.5.0` is released.

Changes since 1.4.0 include:

**API changes**

- Add BundleSubject#stringArray
- Add ParcelableSubject.marshallsEquallyTo()
- Add BundleSubject#doubleFloat

**Bug fixes**

- Make Intent matchers fail explicitly for null intent

**Dependency Changes**

- Update to
  - com.google.guava:guava:30.1.1-android
  - com.google.truth:truth:1.1.3

### ext.truth 1.5.0-rc01

October 26, 2022

`androidx.test.ext:truth:1.5.0-rc01` is released.

### ext.truth 1.5.0-beta02

October 21, 2022

`androidx.test.ext:truth:1.5.0-beta02` is released.

**API changes**

- Promote IntentCorrespondences#all as stable API.

### ext.truth 1.5.0-beta01

October 6, 2022

`androidx.test.ext:truth:1.5.0-beta01` is released.

**API changes**

- Annotate new APIs introduced since 1.4.0 with NonNull/Nullable
- Add BundleSubject#stringArray

### ext.truth 1.5.0-alpha07

June 1, 2022

`androidx.test.ext:truth:1.5.0-alpha07` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### ext.truth 1.5.0-alpha06

April 28, 2022

`androidx.test.ext:truth:1.5.0-alpha06` is released.

### ext.truth 1.5.0-alpha05

Mar 21, 2022

`androidx.test.ext:truth:1.5.0-alpha05` is released.

**Bug fixes**

- Make Intent matchers fail explicitly for null intent

### ext.truth 1.5.0-alpha04

Feb 11, 2022

`androidx.test.ext:truth:1.5.0-alpha04` is released.

### ext.truth 1.5.0-alpha03

Oct 4, 2021

`androidx.test.ext:truth:1.5.0-alpha03` is released.

### ext.truth 1.5.0-alpha02

Sept 28, 2021

`androidx.test.ext:truth:1.5.0-alpha02` is released.

**API Changes**

- Add ParcelableSubject.marshallsEquallyTo()

**Dependency Changes**

- Update to
  - com.google.guava:guava:30.1.1-android
  - com.google.truth:truth:1.1.3

### ext.truth 1.5.0-alpha01

Aug 23, 2021

`androidx.test.ext:truth:1.5.0-alpha01` is released.

**API Changes**

- Add BundleSubject#doubleFloat

## Monitor 1.8.0

### monitor 1.8.0

July 30, 2025

`androidx.test:monitor:1.8.0` is released.

Changes since last stable 1.7.2 release include:

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0a
  - kotlin 1.9.0

**New Features**

- Adds @Supersedes to ServiceLoaderWrapper so it's possible to choose one implementation over another when multiple exist.

**API Changes**

- Update to minSdkVersion 21
- Make ReflectionException a RuntimeException

### monitor 1.8.0-rc01

July 14, 2025

`androidx.test:monitor:1.8.0-rc01` is released.

### monitor 1.8.0-beta01

June 30, 2025

`androidx.test:monitor:1.8.0-beta01` is released.

**New Features**

- Adds @Supersedes to ServiceLoaderWrapper so it's possible to choose one implementation over another when multiple exist.

### monitor 1.8.0-alpha03

April 23, 2025

`androidx.test:monitor:1.8.0-alpha03` is released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### monitor 1.8.0-alpha02

March 27, 2025

`androidx.test:monitor:1.8.0-alpha02` is released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0a
  - kotlin 2.1.0

### monitor 1.8.0-alpha01

February 03, 2025

`androidx.test:monitor:1.8.0-alpha01` is released.

**API Changes**

- Update to minSdkVersion 21
- Make ReflectionException a RuntimeException

### monitor 1.7.2

August 14, 2024

`androidx.test:monitor:1.7.2` is released.

**Bug Fixes**

- Fix ActivityInvoker$-CC ClassNotFoundErrors when used with older androidx.test:core

### monitor 1.7.1

June 26, 2024

`androidx.test:monitor:1.7.1` is released.

**Bug Fixes**

- Catch and log NoSuchMethodError on forceEnableAppTracing calls

### monitor 1.7.0

June 24, 2024

`androidx.test:monitor:1.7.0` is released.

Changes since last stable release 1.6.1 include:

**API Changes**

- Make DeviceController a public API
- Move PlatformTestStorage to a public API
- Add internal ControlledLooper#isDrawCallbacksSupported.
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- minSdkVersion is now 19, targetSdkVersion is now 34

**Bug Fixes**

- Remove unused androidx.test.annotation dependency
- Fix synchronization in IntentMonitorImpl callbacks

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update: now compiled to java8 bytecode

**Known issues**

- monitor has a dependency on androidx.tracing:1.1.0. Depending on configuration, gradle may downgrade this to 1.0.0 at runtime causing 'No static method forceEnableAppTracing' errors. As a workaround, add an explicit 'implementation androidx.tracing:1.1.0' dependency. See https://github.com/android/android-test/issues/1755

### monitor 1.7.0-rc01

May 30, 2024

`androidx.test:monitor:1.7.0-rc01` is released.

### monitor 1.7.0-beta01

May 16, 2024

`androidx.test:monitor:1.7.0-beta01` is released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### monitor 1.7.0-alpha05

April 26, 2024

`androidx.test:monitor:1.7.0-alpha05` is released.

**API Changes**
\* Make DeviceController an public API from ExperimentalTestApi
\* Move PlatformTestStorage to a public API
\* Add internal ControlledLooper#isDrawCallbacksSupported.

### monitor 1.7.0-alpha04

January 26, 2024

`androidx.test:monitor:1.7.0-alpha04` is released.

**Bug Fixes**

- Fix synchronization in IntentMonitorImpl callbacks
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)

**API Changes**
\* Move androidx.test.platform.tracing back to an internal API

### monitor 1.7.0-alpha03

November 29, 2023

`androidx.test:monitor:1.7.0-alpha03` is released.

**API Changes**

- targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### monitor 1.7.0-alpha02

September 18, 2023

`androidx.test:monitor:1.7.0-alpha02` is released.

**API change**
\* Add AppComponentFactory Rule

**Features**
\* Dump thread states when idling resources time out

**Bug fixes**
\* Fix captureToBitmap for Views inside a Dialog on APIs \>= 26.

**Dependency changes**
\* minSdkVersion is now 19

### monitor 1.7.0-alpha01

March 21, 2023

`androidx.test:monitor:1.7.0-alpha01` is released.

**Dependency changes**

- Update to kotlin stdlib 1.7.22
- Major release toolchain update: now compiled to java8 bytecode

## Monitor 1.6.0

### monitor 1.6.1

January 3, 2023

`androidx.test:monitor:1.6.1` is released.

**Bug fixes**

- Fix the default implementation of PlatformTestStorage. This will enable espresso to save screenshots on test failures when androidx.test.services is not configured
- Reference doc cleanup

### monitor 1.6.0

November 8, 2022

`androidx.test:monitor:1.6.0` is released.

Changes since 1.5.0 include:

**API changes**

- Internal API changes to support ActivityScenario#launchActivityForResult
- Add internal API for supporting different tracing libraries.

**Bug fixes**

- Remove 'Activities that are still in CREATED to STOPPED' log spam

**Dependency Changes**

- Add dependency on androidx.tracing

### monitor 1.6.0-rc01

October 26, 2022

`androidx.test:monitor:1.6.0-rc01` is released.

### monitor 1.6.0-beta01

October 6, 2022

`androidx.test:monitor:1.6.0-beta01` is released.

### monitor 1.6.0-alpha05

August 22, 2022

`androidx.test:monitor:1.6.0-alpha05` is released.

**API changes**

- Internal API changes to support ActivityScenario#launchActivityForResult

## Monitor aka Platform 1.6.0

### monitor 1.6.0-alpha04

June 1, 2022

`androidx.test:monitor:1.6.0-alpha04` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### monitor 1.6.0-alpha03

April 28, 2022

`androidx.test:monitor:1.6.0-alpha03` is released.

**Bug fixes**

- Remove 'Activities that are still in CREATED to STOPPED' log spam

### monitor 1.6.0-alpha02

Mar 21, 2022

`androidx.test:monitor:1.6.0-alpha02` is released.

**Bug fixes**

- Make HardwareRendererCompat logging less severe.
- Ensure Trace.endSection is called before Instrumentation#finish.

### monitor 1.6.0-alpha01

Feb 11, 2022

`androidx.test:monitor:1.6.0-alpha01` is released.

**API Changes**

- Add internal plugin API for supporting different tracing libraries.

**Dependency Changes**

- Add dependency on androidx.tracing

## Monitor aka Platform 1.5.0

### monitor 1.5.0

Dec 13, 2021

`androidx.test:monitor:1.5.0` is released.

Changes since last 1.4.0 stable release are:

**API Changes**

- Add HardwareRendererCompat
- Add PlatformTestStorage
- Deprecate androidx.test.annotation.Beta

### monitor 1.5.0-rc01

Nov 18, 2021

`androidx.test:monitor:1.5.0-rc01` is released.

### monitor 1.5.0-beta01

Nov 8, 2021

`androidx.test:monitor:1.5.0-beta01` is released.

### monitor 1.5.0-alpha03

Oct 4, 2021

`androidx.test:monitor:1.5.0-alpha03` is released.

### monitor 1.5.0-alpha02

Sept 28, 2021

`androidx.test:monitor:1.5.0-alpha02` is released.

**API Changes**

- Remove HardwareRendererCompat#enableDrawingIfNecessary
- Remove ExperimentalTestApi from HardwareRendererCompat
- Deprecate androidx.test.annotation.Beta

### monitor 1.5.0-alpha01

Aug 23, 2021

`androidx.test:monitor:1.5.0-alpha01` is released.

**API Changes**

- Add HardwareRendererCompat
- Add PlatformTestStorage

## Orchestrator 1.6.1

### orchestrator 1.6.1

July 31, 2025

`androidx.test:orchestrator:1.6.1` is released.

**Bug Fixes**

- Remove use of guava. Fixes https://github.com/android/android-test/issues/2422

### orchestrator 1.6.0

July 30, 2025

`androidx.test:orchestrator:1.6.0` is released.

Changes since last stable 1.5.1 release include:

**Bug Fixes**

- Fix a bug where the instrumentation test application would not startup if the arguments passed to `ORCHESTRATOR_FORWARDED_INSTRUMENTATION_ARGS` contains spaces.
- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3

**API Changes**

- Update to minSdkVersion 21

### orchestrator 1.6.0-rc01

July 14, 2025

`androidx.test:orchestrator:1.6.0-rc01` is released.

### orchestrator 1.6.0-beta01

June 30, 2025

`androidx.test:orchestrator:1.6.0-beta01` is released.

**Bug Fixes**

- Fix a bug where the instrumentation test application would not startup if the arguments passed to `ORCHESTRATOR_FORWARDED_INSTRUMENTATION_ARGS` contains spaces.

### orchestrator 1.6.0-alpha04

April 23, 2025

`androidx.test:orchestrator:1.6.0-alpha04` is released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### orchestrator 1.6.0-alpha03

March 27, 2025

`androidx.test:orchestrator:1.6.0-alpha03` is released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3

### orchestrator 1.6.0-alpha02

February 03, 2025

`androidx.test:orchestrator:1.6.0-alpha02` is released.

### orchestrator 1.6.0-alpha01

November 20, 2024

`androidx.test:orchestrator:1.6.0-alpha01` is released.

**API Changes**

- Update to minSdkVersion 21

### orchestrator 1.5.1

October 15, 2024

`androidx.test:orchestrator:1.5.1` is released.

**Bug Fixes**

- Fix execution of test names containing whitespace

### orchestrator 1.5.0

June 24, 2024

`androidx.test:orchestrator:1.5.0` is released.

Changes since last stable release 1.4.2 include:

**New Features**

- Introduce Instrumentation Params Proxying which allows the user to proxy instrumentation arguments to the APK under test (eg: --no-hidden-api-checks).
- Major release toolchain update. APK is now signed with a different key and you will need to uninstal any previous orchestrator ('adb uninstall androidx.test.orchestrator')

**API Changes**

- minSdkVersion is now 19

**Bug Fixes**

- Fix crash when test name is too long

### orchestrator 1.5.0-rc01

May 30, 2024

`androidx.test:orchestrator:1.5.0-rc01` is released.

### orchestrator 1.5.0-beta01

May 16, 2024

`androidx.test:orchestrator:1.5.0-beta01` is released.

### orchestrator 1.5.0-alpha04

April 26, 2024

`androidx.test:orchestrator:1.5.0-alpha04` is released.

### orchestrator 1.5.0-alpha03

February 29, 2024

`androidx.test:orchestrator:1.5.0-alpha03` is released.

**New Features**

- Introduce Instrumentation Params Proxying which allows the user to proxy instrumentation arguments to the APK under test (eg: --no-hidden-api-checks).

### orchestrator 1.5.0-alpha02

November 29, 2023

`androidx.test:orchestrator:1.5.0-alpha02` is released.

**API Changes**

- minSdkVersion is now 19

**Bug Fixes**

- Fix crash when test name is too long

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### orchestrator 1.5.0-alpha01

March 21, 2023

`androidx.test:orchestrator:1.5.0-alpha01` is released.

**Dependency changes**

- Major release toolchain update. APK is now signed with a different key and you will need to uninstal any previous orchestrator ('adb uninstall androidx.test.orchestrator')

## Orchestrator 1.4.2

### orchestrator 1.4.2

November 8, 2022

`androidx.test:orchestrator:1.4.2` is released.

### orchestrator 1.4.2-rc01

October 26, 2022

`androidx.test:orchestrator:1.4.2-rc01` is released.

### orchestrator 1.4.2-beta01

October 6, 2022

`androidx.test:orchestrator:1.4.2-beta01` is released.

### orchestrator 1.4.2-alpha04

June 1, 2022

`androidx.test:orchestrator:1.4.2-alpha04` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### orchestrator 1.4.2-alpha03

April 28, 2022

`androidx.test:orchestrator:1.4.2-alpha03` is released.

### orchestrator 1.4.2-alpha02

Mar 21, 2022

`androidx.test:orchestrator:1.4.2-alpha02` is released.

### orchestrator 1.4.2-alpha01

Feb 11, 2022

`androidx.test:orchestrator:1.4.2-alpha01` is released.

## Orchestrator 1.4.1

### orchestrator 1.4.1

Dec 13, 2021

`androidx.test:orchestrator:1.4.1` is released.

The notable changes since previous 1.4.0 stable release are:

**Bug Fixes**

- Delete obsolete OrchestrationXmlTestRunListener , in part to prevent error messages on Android 11+
- Support for android API 31

### orchestrator 1.4.1-rc01

Nov 18, 2021

`androidx.test:orchestrator:1.4.1-rc01` is released.

### orchestrator 1.4.1-beta01

Nov 8, 2021

`androidx.test:orchestrator:1.4.1-beta01` is released.

### orchestrator 1.4.1-alpha03

Oct 4, 2021

`androidx.test:orchestrator:1.4.1-alpha03` is released.

### orchestrator 1.4.1-alpha02

Sept 28, 2021

`androidx.test:orchestrator:1.4.1-alpha02` is released.

### orchestrator 1.4.1-alpha01

Aug 23, 2021

`androidx.test:orchestrator:1.4.1-alpha01` is released.

**Bug Fixes**

- Delete obsolete OrchestrationXmlTestRunListener , in part to prevent error messages on Android 11+

## Runner 1.7.0

### runner 1.7.0

July 30, 2025

`androidx.test:runner:1.7.0` is released.

Changes since last stable 1.6.1 release include:

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
- Exceptions during `@AfterClass` were not being reported via `InstrumentationResultPrinter`.
- Exceptions arising in AndroidJUnitRunner.buildRequest are now handled.
- Assumption failures during a ClassRule or BeforeClass are now reported more consistently via `InstrumentationResultPrinter`
- Clarify SdkSuppress reference docs

**API Changes**

- Update to minSdkVersion 21
- Deprecate androidx.test.filters.Suppress in favor of org.junit.Ignore

### runner 1.7.0-rc01

July 14, 2025

`androidx.test:runner:1.7.0-rc01` is released.

### runner 1.7.0-beta01

June 30, 2025

`androidx.test:runner:1.7.0-beta01` is released.

### runner 1.7.0-alpha03

April 23, 2025

`androidx.test:runner:1.7.0-alpha03` is released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### runner 1.7.0-alpha02

March 27, 2025

`androidx.test:runner:1.7.0-alpha02` is released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

### runner 1.7.0-alpha01

February 03, 2025

`androidx.test:runner:1.7.0-alpha01` is released.

**Bug Fixes**

- Exceptions during `@AfterClass` were not being reported via `InstrumentationResultPrinter`.
- Exceptions arising in AndroidJUnitRunner.buildRequest are now handled.
- Assumption failures during a ClassRule or BeforeClass are now reported more consistently via `InstrumentationResultPrinter`
- Clarify SdkSuppress reference docs

**API Changes**

- Update to minSdkVersion 21
- Deprecate androidx.test.filters.Suppress in favor of org.junit.Ignore

### runner 1.6.2

August 14, 2024

`androidx.test:runner:1.6.2` is released.

### runner 1.6.1

June 26, 2024

`androidx.test:runner:1.6.1` is released.

### runner 1.6.0

June 24, 2024

`androidx.test:runner:1.6.0` is released.

Changes since last stable release 1.5.2 include:

**API Changes**

- Mark androidx.test.services.\*\* as RestrictTo LIBRARY_GROUP
- Add CustomFilter API
- Add PackagePrefixClasspathSuite API
- Mark PermissionRequester as RestrictTo LIBRARY_GROUP instead of ExperimentalTestApi
- minSdkVersion is now 19

**Bug Fixes**

- Remove unused androidx.test.annotation dependency
- When logging test exceptions, use Log's built-in support for throwables to avoid stack truncation
- Internal changes to support GrantPermissionRule using UiAutomation#grantRuntimePermissions
- Attempt to clarify limitations and deprecation reasons in RequiresDevice documentation
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Fix that "-e class" and "-e notClass" on the same class/method should perform the same result (no tests run)
- `TestDiscoveryEventServiceConnection.send()` will correctly fail the test instead of hanging if the instrumentation throws a RuntimeException.
- Stop reparsing all args for every AndroidJUnit4 test class. This should address initialization errors like in #1948.
- Force initialization of instrumentationRunListener, to prevent NPEs when instrumenting system server process.
- Attempt to avoid outputting a test result summary which exceeds binder transaction limit.
- Wait up to 2 seconds for activity finisher to run, to prevent situations where it finishes activities mid-test
- Improve error reporting when there is a junit class mismatch due to a custom classloader
- Fix reporting in logOnly mode for @Ignore-d classes
- Move instantiation of InstrumentationResultPrinter to after multidex is loaded
- Register TestStorage before using it in RunnerArgs parsing
- Execute test classes in order provided to TestRequestBuilder.

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17.

### runner 1.6.0-rc01

May 30, 2024

`androidx.test:runner:1.6.0-rc01` is released.

### runner 1.6.0-beta01

May 16, 2024

`androidx.test:runner:1.6.0-beta01` is released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### runner 1.6.0-alpha07

April 26, 2024

`androidx.test:runner:1.6.0-alpha07` is released.

**Bug Fixes**

- When logging test exceptions, use Log's built-in support for throwables to avoid stack truncation
- Internal changes to support GrantPermissionRule using UiAutomation#grantRuntimePermissions

### runner 1.6.0-alpha06

January 26, 2024

`androidx.test:runner:1.6.0-alpha06` is released.

**Bug Fixes**

- Attempt to clarify limitations and deprecation reasons in RequiresDevice documentation
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)
- Fix that "-e class" and "-e notClass" on the same class/method should perform the same result (no tests run)

**API Changes**

- Mark androidx.test.services.\*\* as RestrictTo LIBRARY_GROUP
- Remove ExperimentalTestApi from CustomFilter - making it public
- Remove ExperimentalTestApi from PackagePrefixClasspathSuite - make it public
- Mark PermissionRequester as RestrictTo LIBRARY_GROUP instead of ExperimentalTestApi

### runner 1.6.0-alpha05

November 29, 2023

`androidx.test:runner:1.6.0-alpha05` is released.

**Bug Fixes**

- `TestDiscoveryEventServiceConnection.send()` will correctly fail the test instead of hanging if the instrumentation throws a RuntimeException.
- Stop reparsing all args for every AndroidJUnit4 test class. This should address initialization errors like in #1948.

**API Changes**

- minSdkVersion is now 19

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### runner 1.6.0-alpha04

August 21, 2023

`androidx.test:runner:1.6.0-alpha04` is released.

**Bug fixes**

- Force initialization of instrumentationRunListener, to prevent NPEs when instrumenting system server process.

**Dependency changes**

- Upgrade to androidx.annotation:1.7.0-beta01

### runner 1.6.0-alpha03

June 30, 2023

`androidx.test:runner:1.6.0-alpha03` is released.

**Bug fixes**

- Attempt to avoid outputting a test result summary which exceeds binder transaction limit.

### runner 1.6.0-alpha02

April 25, 2023

`androidx.test:runner:1.6.0-alpha02` is released.

**Bug fixes**

- Wait up to 2 seconds for activity finisher to run, to prevent situations where it finishes activities mid-test

### runner 1.6.0-alpha01

March 21, 2023

`androidx.test:runner:1.6.0-alpha01` is released.

**Bug fixes**

- Improve error reporting when there is a junit class mismatch due to a custom classloader
- Fix reporting in logOnly mode for @Ignore-d classes
- Move instantiation of InstrumentationResultPrinter to after multidex is loaded
- Register TestStorage before using it in RunnerArgs parsing
- Execute test classes in order provided to TestRequestBuilder.

**Dependency changes**

- Update to androidx.test:monitor:1.7.0-alpha01
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11.

## Runner 1.5.0

### runner 1.5.2

January 3, 2023

`androidx.test:runner:1.5.2` is released.

**Bug fixes**

- Reference doc cleanup

### runner 1.5.1

November 9, 2022

`androidx.test:runner:1.5.1` is released.

**Bug fixes**

- Truncate trace name in TraceRunListener to prevent crash on long test names

### runner 1.5.0

November 8, 2022

`androidx.test:runner:1.5.0` is released.

Changes since 1.4.0 include:

**New features**

- Record android Trace spans for test lifecycle events

**API changes**

- Denote the long standing @Beta/@ExperimentalTestApi androidx.test.runner.screenshot as stable but deprecated (in favor of new androidx.test.core/espresso screenshot APIs)
- Deprecate the '-e timeout' runtime parameter in favor of JUnit's Timeout rule.
- Add an AbstractFilter class.
- Add AndroidClasspathSuite and experimental PackagePrefixClasspathSuite
- No-op and deprecate Google Analytics

**Bug fixes**

- Add support for reading from TestStorage in -e testFile
- Handle case where app crashes before instrumentationResultPrinter is set.
- Report the process crash immediately in the orchestrator instrumentation listener.
- Support parameterized test names with commas and hashes.
- Improve error handling during test discovery phase in orchestrator
- Enhance error handling in exception scenarios (app crashes, etc)

**Dependency Changes**

- Update to
  - org.junit:junit:4.13.2

### runner 1.5.0-rc01

October 26, 2022

`androidx.test:runner:1.5.0-rc01` is released.

### runner 1.5.0-beta02

October 21, 2022

`androidx.test:runner:1.5.0-beta02` is released.

**API changes**

- Denote the long standing @Beta/@ExperimentalTestApi androidx.test.runner.screenshot as stable but deprecated

**Bug fixes**

- Add support for reading from TestStorage in -e testFile

### runner 1.5.0-beta01

October 6, 2022

`androidx.test:runner:1.5.0-beta01` is released.

**API changes**

- Deprecate the '-e timeout' runtime parameter in favor of JUnit's Timeout rule.
- Add an AbstractFilter class.

**Bug fixes**

- Fix trace errors for long test names
- Handle case where app crashes before instrumentationResultPrinter is set.

### runner 1.5.0-alpha04

June 1, 2022

`androidx.test:runner:1.5.0-alpha04` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### runner 1.5.0-alpha03

April 28, 2022

`androidx.test:runner:1.5.0-alpha03` is released.

**Bug fixes**

- Report the process crash immediately in the orchestrator instrumentation listener.

### runner 1.5.0-alpha02

Mar 21, 2022

`androidx.test:runner:1.5.0-alpha02` is released.

**Bug Fixes**

- Ensure Trace.endSection is called before Instrumentation#finish.

### runner 1.5.0-alpha01

Feb 11, 2022

`androidx.test:runner:1.5.0-alpha01` is released.

**API Changes**

- Add AndroidClasspathSuite and PackagePrefixClasspathSuite

**New Features**

- Record android Trace spans for test lifecycle events

**Bug Fixes**

- Support parameterized test names with commas and hashes.
- Improve error handling during test discovery phase in orchestrator

## Runner 1.4.1

### runner 1.4.1-alpha03

Oct 4, 2021

`androidx.test:runner:1.4.1-alpha03` is released.

**Bug fixes**

- Reports the exception when an error is thrown out of the test executor.

### runner 1.4.1-alpha02

Sept 28, 2021

`androidx.test:runner:1.4.1-alpha02` is released.

**API Changes**

- Replace androidx.test.annotaton.Beta references with ExperimentalTestApi

**Bug fixes**

- No-op and deprecate Google Analytics

**Dependency Changes**

- Update to
  - org.junit:junit:4.13.2

### runner 1.4.1-alpha01

Aug 23, 2021

`androidx.test:runner:1.4.1-alpha01` is released.

**Bug Fixes**

- Enhance error handling in exception scenarios (app crashes, etc)

## Rules 1.7.0

### rules 1.7.0

July 30, 2025

`androidx.test:rules:1.7.0` is released.

Changes since last stable 1.6.0 release include:

**API Changes**

- `ServiceTestRule.startService` will now throw if the provided intent does not launch a service.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

**API Changes**

- Update to minSdkVersion 21

### rules 1.7.0-rc01

July 14, 2025

`androidx.test:rules:1.7.0-rc01` is released.

### rules 1.7.0-beta01

June 30, 2025

`androidx.test:rules:1.7.0-beta01` is released.

**Breaking Changes**

- `ServiceTestRule.startService` will now throw if the provided intent does not launch a service.

### rules 1.7.0-alpha03

April 23, 2025

`androidx.test:rules:1.7.0-alpha03` is released.

**Bug Fixes**

- Downgrade to kotlin 1.9

### rules 1.7.0-alpha02

March 27, 2025

`androidx.test:rules:1.7.0-alpha02` is released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

### rules 1.7.0-alpha01

February 03, 2025

`androidx.test:rules:1.7.0-alpha01` is released.

**API Changes**

- Update to minSdkVersion 21

### rules 1.6.1

June 26, 2024

`androidx.test:rules:1.6.1` is released.

### rules 1.6.0

June 24, 2024

`androidx.test:rules:1.6.0` is released.

Changes since last stable release 1.5.0 include:

**API Changes**

- minSdkVersion is now 19, targetSdkVersion is now 34
- Recommend use of UiAutomation#grantRuntimePermissions instead of GrantPermissionRule

**Bug Fixes**

- Replace broken links to junit.org javadoc with @link.
- Make GrantPermissionRule use UiAutomation to grant permissions on APIs \> =28 to fix issues running on automotive.

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17.

### rules 1.6.0-rc01

May 30, 2024

`androidx.test:rules:1.6.0-rc01` is released.

### rules 1.6.0-beta01

May 16, 2024

`androidx.test:rules:1.6.0-beta01` is released.

**Bug Fixes**

- Remove unused androidx.test.annotation dependency

### rules 1.6.0-alpha04

April 26, 2024

`androidx.test:rules:1.6.0-alpha04` is released.

**Bug Fixes**

- Make GrantPermissionRule use UiAutomation to grant permissions on APIs \> =28 to fix issues running on automotive.

### rules 1.6.0-alpha03

January 26, 2024

`androidx.test:rules:1.6.0-alpha03` is released.

**Bug Fixes**

- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)

**API Changes**

- Recommend use of UiAutomation#grantRuntimePermissions instead of GrantPermissionRule

### rules 1.6.0-alpha02

November 29, 2023

`androidx.test:rules:1.6.0-alpha02` is released.

**Bug Fixes**

- Replace broken links to junit.org javadoc with @link.

**API Changes**

- minSdkVersion is now 19, targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### rules 1.6.0-alpha01

March 21, 2023

`androidx.test:rules:1.6.0-alpha01` is released.

**Dependency changes**

- Update toandroidx.test:runner:1.6.0-alpha01
- Update to kotlin stdlib 1.7.22
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11.

## Rules 1.5.0

### rules 1.5.0

November 8, 2022

`androidx.test:rules:1.5.0` is released.

Changes since 1.4.0 include:

**API Changes**

- Promote long standing @Beta/@ExperimentalTestApi GrantPermissionRule and ServiceTestRule as stable APIs
- Promote long standing @Beta/@ExperimentalTestApi AtraceLogger and ProviderTestRule as stable but deprecated APIs

**Dependency Changes**

- Update to
  - org.junit:junit:4.13.2

## Rules 1.5.0

### rules 1.5.0-rc01

October 26, 2022

`androidx.test:rules:1.5.0-rc01` is released.

### rules 1.5.0-beta01

October 21, 2022

`androidx.test:rules:1.5.0-beta01` is released.

**API Changes**

- Promote long standing @Beta/@ExperimentalTestApi GrantPermissionRule and ServiceTestRule as stable APIs
- Promote long standing @Beta/@ExperimentalTestApi AtraceLogger and ProviderTestRule as stable but deprecated APIs

## Rules 1.4.1

### rules 1.4.1-beta01

October 6, 2022

`androidx.test:rules:1.4.1-beta01` is released.

### rules 1.4.1-alpha07

June 1, 2022

`androidx.test:rules:1.4.1-alpha07` is released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### rules 1.4.1-alpha06

April 28, 2022

`androidx.test:rules:1.4.1-alpha06` is released.

### rules 1.4.1-alpha05

Mar 21 2022

`androidx.test:rules:1.4.1-alpha05` is released.

### rules 1.4.1-alpha04

Feb 11 2022

`androidx.test:rules:1.4.1-alpha04` is released.

### rules 1.4.1-alpha03

Oct 4, 2021

`androidx.test:rules:1.4.1-alpha03` is released.

### rules 1.4.1-alpha02

Sept 28, 2021

`androidx.test:rules:1.4.1-alpha02` is released.

**API Changes**

- Replace androidx.test.annotaton.Beta references with ExperimentalTestApi

**Dependency Changes**

- Update to
  - org.junit:junit:4.13.2

### rules 1.4.1-alpha01

Aug 23, 2021

`androidx.test:rules:1.4.1-alpha01` is released.

No significant changes

## Services 1.6.0

### services 1.6.0

July 30, 2025

`androidx.test.services:test-services:1.6.0` `androidx.test.services:storage:1.6.0` are released.

Changes since last stable 1.5.0 release include:

**New Features**

- StackTrimmer now reports suppressed exceptions
- Adding a LocalSocket-based protocol for the ShellExecutor to talk to the ShellMain. This obsoletes SpeakEasy; if androidx.test.services is killed (e.g. by the low memory killer) between the start of the app_process that invokes LocalSocketShellMain and the start of the test, the test is still able to talk to LocalSocketShellMain.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0
- The obsolete FileObserver protocol has been removed in favor of the LocalSocket-based protocol.
- TestStorage: Use input directory location for internal files
- StackTrimmer: harden against exceptions coming from Failure.getMessage().

**API Changes**

- Update to minSdkVersion 21

### services 1.6.0-rc01

July 14, 2025

`androidx.test.services:test-services:1.6.0-rc01` `androidx.test.services:storage:1.6.0-rc01` are released.

### services 1.6.0-beta01

June 30, 2025

`androidx.test.services:test-services:1.6.0-beta01` `androidx.test.services:storage:1.6.0-beta01` are released.

### services 1.6.0-alpha04

April 23, 2025

`androidx.test.services:test-services:1.6.0-alpha04` `androidx.test.services:storage:1.6.0-alpha04` are released.

**Bug Fixes**

- Downgrade to kotlin 1.9

**New Features**

- StackTrimmer now reports suppressed exceptions

### services 1.6.0-alpha03

March 27, 2025

`androidx.test.services:test-services:1.6.0-alpha03` `androidx.test.services:storage:1.6.0-alpha03` are released.

**Bug Fixes**

- Update bazel toolchain:
  - bazel version 7.5.0
  - rules_jvm_external 6.7
  - rules_java 8.6.3
  - rules_kotlin 2.1.3
  - rules_android 0.6.3
- Update dependencies to:
  - androidx.annotation 1.7.0

### services 1.6.0-alpha02

February 03, 2025

`androidx.test.services:test-services:1.6.0-alpha02` `androidx.test.services:storage:1.6.0-alpha02` are released.

**Bug Fixes**

- The obsolete FileObserver protocol has been removed in favor of the LocalSocket-based protocol.

### services 1.6.0-alpha01

November 20, 2024

`androidx.test.services:test-services:1.6.0-alpha01` `androidx.test.services:storage:1.6.0-alpha01` are released.

**Bug Fixes**

- TestStorage: Use input directory location for internal files
- StackTrimmer: harden against exceptions coming from Failure.getMessage().

**New Features**

- Adding a LocalSocket-based protocol for the ShellExecutor to talk to the ShellMain. This obsoletes SpeakEasy; if androidx.test.services is killed (e.g. by the low memory killer) between the start of the app_process that invokes LocalSocketShellMain and the start of the test, the test is still able to talk to LocalSocketShellMain.

**API Changes**

- Update to minSdkVersion 21

### services 1.5.0

June 24, 2024

`androidx.test.services:test-services:1.5.0` `androidx.test.services:storage:1.5.0` are released.

Changes since last stable 1.4.2 release include:

**API Changes**

- Make TestStorage an internal API from experimental
- minSdkVersion is now 19, targetSdkVersion is now 34

**Bug Fixes**

- Reduce HostedFile log spam
- Remove unused androidx.test.annotation dependency
- TestStorage: use local cache dir to store output files when running as non system user
- When files are opened for writing, TestStorage now truncates the file unless it is explicitly opened for appending. This prevents bytes from a prior write to the file from remaining at the end of the file.
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)

**New Features**

- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 17.
  - APK is now signed with a different key and you will need to uninstall any previous APK ('adb uninstall androidx.test.services')

### services 1.5.0-rc01

May 30, 2024

`androidx.test.services:test-services:1.5.0-rc01` `androidx.test.services:storage:1.5.0-rc01` are released.

### services 1.5.0-beta01

May 16, 2024

`androidx.test.services:test-services:1.5.0-beta01` `androidx.test.services:storage:1.5.0-beta01` are released.

**Bug Fixes**

- Reduce HostedFile log spam
- Remove unused androidx.test.annotation dependency

### services 1.5.0-alpha04

April 26, 2024

`androidx.test.services:test-services:1.5.0-alpha04` `androidx.test.services:storage:1.5.0-alpha04` are released.

**Bug Fixes**

- TestStorage: use local cache dir to store output files when running as non system user

**API Changes**

- Make TestStorage an internal API from experimental

### services 1.5.0-alpha03

January 26, 2024

`androidx.test.services:test-services:1.5.0-alpha03` `androidx.test.services:storage:1.5.0-alpha03` are released.

**Bug Fixes**

- When files are opened for writing, TestStorage now truncates the file unless it is explicitly opened for appending. This prevents bytes from a prior write to the file from remaining at the end of the file.
- Remove all support for Android SDKs \< 19. Minimum is API 19 (Android Kit Kat 4.4)

### services 1.5.0-alpha02

November 29, 2023

`androidx.test.services:test-services:1.5.0-alpha02` `androidx.test.services:storage:1.5.0-alpha02` are released.

**Bug Fixes**

- Attempt to avoid outputting a test result summary which exceeds binder transaction limit

**API Changes**

- minSdkVersion is now 19, targetSdkVersion is now 34

**New Features**

- Artifacts are now signed. See [verify dependencies](https://developer.android.com/jetpack/getting-started#verify_dependencies) for more details.

### services 1.5.0-alpha01

March 21, 2022

`androidx.test.services:test-services:1.5.0-alpha01` `androidx.test.services:storage:1.5.0-alpha01` are released.

**Dependency changes**

- Update to androidx.test:monitor:1.7.0-alpha01
- Major release toolchain update:
  - classes are now compiled to java8 bytecode
  - javac compiler switched to OpenJDK 11.
  - APK is now signed with a different key and you will need to uninstal any previous orchestrator ('adb uninstall androidx.test.services')

## Services 1.4.2

### services 1.4.2

November 8, 2022

`androidx.test.services:test-services:1.4.2` `androidx.test.services:storage:1.4.2` are released.

### services 1.4.2-rc01

October 26, 2022

`androidx.test.services:test-services:1.4.2-rc01` `androidx.test.services:storage:1.4.2-rc01` are released.

### services 1.4.2-beta01

October 6, 2022

`androidx.test.services:test-services:1.4.2-beta01` `androidx.test.services:storage:1.4.2-beta01` are released.

### services 1.4.2-alpha04

June 1, 2022

`androidx.test.services:test-services:1.4.2-alpha04` `androidx.test.services:storage:1.4.2-alpha04` are released.

**Bug fixes**

- Revert to javac 11 to prevent IncompatibleClassChangeErrors \[#1351\]

### services 1.4.2-alpha03

April 28, 2022

`androidx.test.services:test-services:1.4.2-alpha03` `androidx.test.services:storage:1.4.2-alpha03` are released.

### services 1.4.2-alpha02

Mar 21, 2022

`androidx.test.services:test-services:1.4.2-alpha02` `androidx.test.services:storage:1.4.2-alpha02` are released.

### services 1.4.2-alpha01

Feb 11, 2022

`androidx.test.services:test-services:1.4.2-alpha01` `androidx.test.services:storage:1.4.2-alpha01` are released.

## Services 1.4.1

### services 1.4.1

Dec 13, 2021

`androidx.test.services:test-services:1.4.1` `androidx.test.services:storage:1.4.1` are released.

The notable changes since previous 1.4.0 stable release are:

\*\* Bug Fixes\*\*

- Fix execution on Android API 31 by using real uid for ToolConnection \[#1042\]

### services 1.4.1-rc01

Nov 18, 2021

`androidx.test.services:test-services:1.4.1-rc01` `androidx.test.services:storage:1.4.1-rc01` are released.

### services 1.4.1-beta01

Nov 8, 2021

`androidx.test.services:test-services:1.4.1-beta01` `androidx.test.services:storage:1.4.1-beta01` are released.

### services 1.4.1-alpha03

Oct 4, 2021

`androidx.test.services:test-services:1.4.1-alpha03` `androidx.test.services:storage:1.4.1-alpha03` are released.

### services 1.4.1-alpha02

Sept 28, 2021

`androidx.test.services:test-services:1.4.1-alpha02` `androidx.test.services:storage:1.4.1-alpha02` are released.

### services 1.4.1-alpha01

Aug 23, 2021

`androidx.test.services:test-services:1.4.1-alpha01` `androidx.test.services:storage:1.4.1-alpha01` are released.

\*\* Bug Fixes\*\*

- Fix execution on Android S Beta4 by using real uid for ToolConnection \[#1042\]

## Version 1.4.0

### Version 1.4.0

June 30, 2021

This is the stable release of AndroidX Test 1.4.0 + Espresso 3.4.0.
It contains updates to the following libraries:

- Core 1.4.0
- Espresso 3.4.0
- Intents 3.4.0
- JUnit 1.1.3
- Monitor 1.4.0
- Orchestrator 1.4.0
- Runner 1.4.0
- Rules 1.4.0
- Truth 1.4.0
- Test Services 1.4.0

There are no changes since 1.4.0-rc01.
Here is a summary of the changes since the 1.3.0 release:

**New Features**

- Add Espresso ViewMatcher APIs for negative conditions
- Allow unregistering Loopers from Espresso IdlingRegistry
- Support specifying junit RunListeners via java.util.ServiceLoader
- Introduce Espresso BoundedDiagnosingMatcher base class API that offers better error messaging, and apply it to various Espresso matchers
- Support using UIThreadTest at the class level
- Several utility methods added to ext.truth's LocationSubject
- Add `SparseBooleanArraySubject` Truth `Subject` for making assertions about `SparseBooleanArray`

**Bug Fixes**

- Improve handling for large stack traces on test failures \[#729, #269\]
  - Remove test runner framework related stack frames
  - Truncate stack traces to a max limit of 64KB, to avoid binder limit transaction errors
- Add support for classpath scanning test discovery for multidex instrumentation apks on android APIs \< 21.
- Espresso: Improve error messaging when no activity is present
- Improve Instrumentation#runOnMainSync exception error handling
- Improve documentation for -e timeout_msec and AndroidJUnit4.
- Send ActivityOptions to BootstrapActivity \[#685\]
- Improve ViewMatchers#assertThat error messaging by enabling it to use Matcher.describeMismatch
- Fix the missing desugar ThrowableExtension errors when using espresso remote \[issuetracker.google.com/170228109\]
- Fix espresso web on \< Android API 19 by including the androidx.test.espresso.web.bridge classes
- Unregister ActivityResultWaiter in InstrumentationActivityInvoker if it wasn't already unregistered
- Runner: Reduce TestEventClient 'not primary instr' log message to a warning, as its an expected condition in multi process tests
- Espresso: Update HasSiblingMatcher to only check siblings (not self)
- Fix artifact name for espresso.idling.resource \[#809\]
- Expose setMasterPolicyTimeoutWhenDebuggerAttached functionality \[#814\]
- Remove overly verbose ActivityLifecycleMonitorImpl callback logging.

**Dependency Changes**

- Update espresso.accessibility and espresso.contrib to depend on the androidx-compatible com.google.android.apps.common.testing.accessibility.framework:accessibility-test-framework:3.1. This release will thus require java8 source/target compatiblity. \[#492\]

**Known Issues**

- Using orchestrator on APIS 30+ requires Studio/AGP 4.2+

### Version 1.4.0-rc01

June 21, 2021

This is a release candidate of AndroidX Test 1.4.0/Espresso 3.4.0. APIs are stable.
It contains updates to the following libraries:

- Core 1.4.0-rc01
- Espresso 3.4.0-rc01
- Intents 3.4.0-rc01
- JUnit 1.1.3-rc01
- Monitor 1.4.0-rc01
- Orchestrator 1.4.0-rc01
- Runner 1.4.0-rc01
- Rules 1.4.0-rc01
- Truth 1.4.0-rc01
- Test Services 1.4.0-rc01

This release candidate is equivalent to the 1.4.0-beta02/3.4.0-beta02 release, aside from the version number.

### Version 1.4.0-beta02

June 7, 2021

This is a beta release of AndroidX Test 1.4.0. APIs are not expected to change.
It contains updates to the following libraries:

- Core 1.4.0-beta02
- Espresso 3.4.0-beta02
- Intents 3.4.0-beta02
- JUnit 1.1.3-beta02
- Monitor 1.4.0-beta02
- Orchestrator 1.4.0-beta02
- Runner 1.4.0-beta02
- Rules 1.4.0-beta02
- Truth 1.4.0-beta02
- Test Services 1.4.0-beta02

Here is a summary of the changes since the 1.4.0-beta01 release:

**Bug fixes**

- Switch back to classic desugaring to address backwards compatiblity and core-library desugaring issues with beta-1 \[Fixes #968 \]

### Version 1.4.0-beta01

May 17, 2021

This is the beta release of AndroidX Test 1.4.0. APIs are not expected to change.
It contains updates to the following libraries:

- Core 1.4.0-beta01
- Espresso 3.4.0-beta01
- Intents 3.4.0-beta01
- JUnit 1.1.3-beta01
- Monitor 1.4.0-beta01
- Orchestrator 1.4.0-beta01
- Runner 1.4.0-beta01
- Rules 1.4.0-beta01
- Truth 1.4.0-beta01
- Test Services 1.4.0-beta01

Here is a summary of the changes since the 1.4.0-alpha06 release:

**New API cleanup**

- Remove InstrumentationProvider
- Undeprecate BoundedMatcher
- Restore CursorMatcher to inherit from BoundedMatcher

### Version 1.4.0-alpha06

April 29, 2021

This is the alpha release of AndroidX Test 1.4.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.4.0-alpha06
- Espresso 3.4.0-alpha06
- Intents 3.4.0-alpha06
- JUnit 1.1.3-alpha06
- Monitor 1.4.0-alpha06
- Orchestrator 1.4.0-alpha06
- Runner 1.4.0-alpha06
- Rules 1.4.0-alpha06
- Truth 1.4.0-alpha06
- Test Services 1.4.0-alpha06

Here is a summary of the changes since the 1.4.0-alpha05 release:

**Bug Fixes**

- Support compiling against SDKS \< 29 by removing forceQueryable from manifest \[#917\]

### Version 1.4.0-alpha05

March 15, 2021

This is the alpha release of AndroidX Test 1.4.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.4.0-alpha05
- Espresso 3.4.0-alpha05
- Intents 3.4.0-alpha05
- JUnit 1.1.3-alpha05
- Monitor 1.4.0-alpha05
- Orchestrator 1.4.0-alpha05
- Runner 1.4.0-alpha05
- Rules 1.4.0-alpha05
- Truth 1.4.0-alpha05
- Test Services 1.4.0-alpha05

Here is a summary of the changes since the 1.4.0-alpha04 release:

**API Changes**

- \[Truth\] Add `SparseBooleanArraySubject` Truth `Subject` for making assertions about `SparseBooleanArray`.

**Bug Fixes**

- Add QUERY_ALL_PACKAGES permission to the Android Test Orchestrator and Android Test Services APK to work properly on Android API R+.
- Add support for classpath scanning test discovery for multidex instrumentation apks on android APIs \< 21.

### Version 1.4.0-alpha04

February 8, 2021

This is the alpha release of AndroidX Test 1.4.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.4.0-alpha04
- Espresso 3.4.0-alpha04
- Intents 3.4.0-alpha04
- JUnit 1.1.3-alpha04
- Monitor 1.4.0-alpha04
- Orchestrator 1.4.0-alpha04
- Runner 1.4.0-alpha04
- Rules 1.4.0-alpha04
- Truth 1.4.0-alpha04
- Test Services 1.4.0-alpha04

Here is a summary of the changes since the 1.3.1-alpha03 release:

**New Features**

- \[Espresso\] Improve error messaging for various Espresso assertions
- \[Truth\] Several utility methods added to LocationSubject

**API Changes**

- Added `InstrumentationRegistry.registerInstrumentationProvider`

**Bug Fixes**

- Remove overly verbose ActivityLifecycleMonitorImpl callback logging.

**Dependency Changes**

## Version 1.3.1

### Version 1.3.1-alpha03

January 11, 2021

This is the alpha release of AndroidX Test 1.3.1. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.1-alpha03
- Espresso 3.4.0-alpha03
- Intents 3.4.0-alpha03
- JUnit 1.1.3-alpha03
- Monitor 1.3.1-alpha03
- Orchestrator 1.3.1-alpha03
- Runner 1.3.1-alpha03
- Rules 1.3.1-alpha03
- Truth 1.3.1-alpha03
- Test Services 1.3.1-alpha03

Here is a summary of the changes since the 1.3.1-alpha02 release:

**New Features**

- Support using UIThreadTest at the class level

**Bug Fixes**

- Unregister ActivityResultWaiter in InstrumentationActivityInvoker if it wasn't already unregistered
- Runner: Reduce TestEventClient 'not primary instr' log message to a warning, as its an expected condition in multi process tests
- Espresso: Update HasSiblingMatcher to only check siblings (not self).
- Fix artifact name for espresso.idling.resource \[#809\]
- Expose setMasterPolicyTimeoutWhenDebuggerAttached functionality \[#814\]

**Dependency Changes**

- Update espresso.accessibility and espresso.contrib to depend on the androidx-compatible com.google.android.apps.common.testing.accessibility.framework:accessibility-test-framework:3.1. This release will thus require java8 source/target compatiblity. \[#492\]

### Version 1.3.1-alpha02

October 20, 2020

This is the alpha release of AndroidX Test 1.3.1. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.1-alpha02
- Espresso 3.4.0-alpha02
- Intents 3.4.0-alpha02
- JUnit 1.1.3-alpha02
- Monitor 1.3.1-alpha02
- Orchestrator 1.3.1-alpha02
- Runner 1.3.1-alpha02
- Rules 1.3.1-alpha02
- Truth 1.3.1-alpha02
- Test Services 1.3.1-alpha02

Here is a summary of the changes since the 1.3.1-alpha01 release:

**New Features**

- Early look at new Espresso BoundedDiagnosingMatcher base class API that offers better error messaging.

**Bug Fixes**

- Fix orchestrator clearPackageData on API 30 \[#743\]

### Version 1.3.1-alpha01

October 15, 2020

This is the alpha release of AndroidX Test 1.3.1. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.1-alpha01
- Espresso 3.4.0-alpha01
- Intents 3.4.0-alpha01
- JUnit 1.1.3-alpha01
- Monitor 1.3.1-alpha01
- Orchestrator 1.3.1-alpha01
- Runner 1.3.1-alpha01
- Rules 1.3.1-alpha01
- Truth 1.3.1-alpha01
- Test Services 1.3.1-alpha01

Here is a summary of the changes since the 1.3.0 release:

**New Features**

- Add Espresso ViewMatcher APIs for negative conditions
- Allow unregistering Loopers from Espresso IdlingRegistry
- Support specifying junit RunListeners via java.util.ServiceLoader

**Bug Fixes**

- Improve handling for large stack traces on test failures \[#729, #269\]
  - Remove test runner framework related stack frames
  - Truncate stack traces to a max limit of 64KB, to avoid binder limit transaction errors
- Espresso: Improve error messaging when no activity is present
- Improve Instrumentation#runOnMainSync exception error handling
- Add package visibility entries for Orchestrator and Services to fix Orchestator when using targetSdk 30 \[#743\]
- Improve documentation for -e timeout_msec and AndroidJUnit4.
- Send ActivityOptions to BootstrapActivity \[#685\]
- Improve ViewMatchers#assertThat error messaging by enabling it to use Matcher.describeMismatch
- Fix the missing desugar ThrowableExtension errors when using espresso remote \[issuetracker.google.com/170228109\]
- Fix espresso web on \< Android API 19 by including the androidx.test.espresso.web.bridge classes

## Version 1.3.0

### Version 1.3.0

August 25, 2020

This is the stable release of AndroidX Test 1.3.0.
It contains updates to the following libraries:

- Core 1.3.0
- Espresso 3.3.0
- Intents 3.3.0
- JUnit 1.1.2
- Monitor 1.3.0
- Orchestrator 1.3.0
- Runner 1.3.0
- Rules 1.3.0
- Truth 1.3.0
- Test Services 1.3.0

There are no changes since 1.3.0-rc03.
Here is a summary of the changes since the 1.2.0 release:

**New Features**

- Support filtering by prerelease SDKs via SdkSuppress#codeName
- Add truth extensions for Location
- Add truth assertions for Bundle string and parceable arrays.
- Support ActivityOptions in ActivityScenario
- Make activity lifecycle transition timeout configurable
- Handle Activities launched via implicit intents. (Fixes #496)
- Add a BundleMatchers.isEmpty() and isEmptyOrNull() methods
- Allow Intents.release without Intents.init
- Add ViewMatchers.isFocused()

**API Changes**

- ActivityTestRule is deprecated in favor of ActivityScenario/ActivityScenarioRule
- Allow subclasses of ServiceTestRule to customize timeout

**Bug Fixes**

- Fix filtering parameterized methods
  - This also fixes running parameterized tests with Orchestrator \[#215, https://issuetracker.google.com/119838413\]
- Fix 'runtime permission dialog appears' when running on API 29
- Skip starting and finish animations for the empty activity used in ActivityScenario. (Fixes #411)
- Handle Activities launched via implicit intents. (Fixes #496)
- Make kotlin package names unique, fixing log spam when building with AGP 4.1 \[#680\]
- Only delegate to RobolectricTestRunner in AndroidJUnit4 runner if its on the classpath
- Espresso contrib: Replace usages of RecyclerView.findViewHolderForPosition method with its replacement
- Fix NoSuchMethodError when testing with AccessibilityChecks enabled (#376)
- Fix the error message when Espresso is busy due to processing messages rather than idling resources
- ViewMatchers.isDisplayingAtLeast() works for views with negative scale.
- Enhance error messaging for WithIdMatcher
- Remove spurious wait in waitForAtLeastOneActivityToBeResumed.
- Set correct meta state for ACTION_UP
- Fix missing missing androidx_test_espresso_contrib_drawer_layout_tag field \[#671\]
- Improve class path scanning error handling in AndroidJUnitRunner: Ignore all no class found and linkage errors (Fixes #439)
- Initialize InstrumentationRegistry before creating RunListeners from RunnerArgs

**Dependency Changes**

- Truth: Update to com.google.truth:truth:1.0 and com.google.guava:guava:27.0.1-android

### Version 1.3.0-rc03

August 5, 2020

This is the third release candidate of AndroidX Test 1.3.0.
It contains updates to the following libraries:

- Core 1.3.0-rc03
- Espresso 3.3.0-rc03
  - Remove some not-yet-ready-for-release APIs that were mistakenly included in previous rc+beta builds
- Intents 3.3.0-rc03
  - Remove some not-yet-ready-for-release APIs that were mistakenly included in previous rc+beta builds
- JUnit 1.1.2-rc03
- Monitor 1.3.0-rc03
- Orchestrator 1.3.0-rc03
- Runner 1.3.0-rc03
- Rules 1.3.0-rc03
- Truth 1.3.0-rc03
- Test Services 1.3.0-rc03

### Version 1.3.0-rc02

July 28, 2020

This is the second release candidate of AndroidX Test 1.3.0.
It contains updates to the following libraries:

- Core 1.3.0-rc02
  - Make kotlin package names unique, fixing log spam when building with AGP 4.1 \[#680\]
- Espresso 3.3.0-rc02
  - Fix missing missing androidx_test_espresso_contrib_drawer_layout_tag field \[#671\]
- Intents 3.3.0-rc02
- JUnit 1.1.2-rc02
- Monitor 1.3.0-rc02
- Orchestrator 1.3.0-rc02
- Runner 1.3.0-rc02
- Rules 1.3.0-rc02
  - Add conversion tips for ActivityTestRule-\>ActivityScenario
- Truth 1.3.0-rc02
- Test Services 1.3.0-rc02

### Version 1.3.0-rc01

May 28, 2020

This is a release candidate of AndroidX Test 1.3.0.
It contains updates to the following libraries:

- Core 1.3.0-rc01
- Espresso 3.3.0-rc01
  - Make package names unique, fixing log spam when building with AGP 4.1 \[#573\]
- Intents 3.3.0-rc01
- JUnit 1.1.2-rc01
- Monitor 1.3.0-rc01
  - Make package names unique, fixing log spam when building with AGP 4.1 \[#573\]
- Orchestrator 1.3.0-rc01
- Runner 1.3.0-beta01
  - Make package names unique, fixing log spam when building with AGP 4.1 \[#573\]
- Rules 1.3.0-rc01
  - Make package names unique, fixing log spam when building with AGP 4.1 \[#573\]
- Truth 1.3.0-rc01
- Test Services 1.3.0-rc01

### Version 1.3.0-beta02

May 20, 2020

This is a beta release of AndroidX Test 1.3.0. New APIs are unlikely to change.
It contains updates to the following libraries:

- Core 1.3.0-beta02
- Espresso 3.3.0-beta02
- Intents 3.3.0-beta02
- JUnit 1.1.2-beta02
- Monitor 1.3.0-beta02
- Orchestrator 1.3.0-beta02
- Runner 1.3.0-beta01
  - Fix running parameterized tests with Orchestrator \[#215, https://issuetracker.google.com/119838413\]
- Rules 1.3.0-beta02
- Truth 1.3.0-beta02
- Test Services 1.3.0-beta02
  - Fix 'runtime permission dialog appears' when running on API 29

### Version 1.3.0-beta01

April 20, 2020

This is a beta release of AndroidX Test 1.3.0. New APIs are unlikely to change.
It contains updates to the following libraries:

- Core 1.3.0-beta01
- Espresso 3.3.0-beta01
  - Add ViewMatchers.isFocused()
  - Enhance error messaging for WithIdMatcher
- Intents 3.3.0-beta01
  - Allow Intents.release without Intents.init
- JUnit 1.1.2-beta01
- Monitor 1.3.0-beta01
- Orchestrator 1.3.0-beta01
- Runner 1.3.0-beta01
  - Only delegate to RobolectricTestRunner if its on the classpath
  - Support filtering by prerelease SDKs via SdkSuppress#codeName
- Rules 1.3.0-beta01
  - Deprecate ActivityTestRule
- Truth 1.3.0-beta01
  - Make LocationSubject override isEqualTo
- Test Services 1.3.0-beta01

### Version 1.3.0-alpha05

March 17, 2020

This is an alpha release of AndroidX Test 1.3.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.0-alpha05
  - Skip starting and finish animations for the empty activity used in ActivityScenario. (Fixes #411)
  - Handle Activities launched via implicit intents. (Fixes #496)
- Espresso 3.3.0-alpha05
  - ViewMatchers.isDisplayingAtLeast() works for views with negative scale.
  - Remove spurious wait in waitForAtLeastOneActivityToBeResumed.
  - Set correct meta state for ACTION_UP
- Intents 3.3.0-alpha05
- JUnit 1.1.2-alpha05
- Monitor 1.3.0-alpha05
- Orchestrator 1.3.0-alpha05
- Runner 1.3.0-alpha05
  - Ignore all LinkageError exceptions when scanning classpath for tests. (Fixes #439)
  - Initialize InstrumentationRegistry before creating RunListeners from RunnerArgs
- Rules 1.3.0-alpha05
- Truth 1.3.0-alpha05
- Test Services 1.3.0-alpha05

### Version 1.3.0-alpha04

February 20, 2020

This is an alpha release of AndroidX Test 1.3.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.0-alpha04
- Espresso 3.3.0-alpha04
  - Fix the error message when Espresso is busy due to processing messages rather than idling resources
- Intents 3.3.0-alpha04
- JUnit 1.1.2-alpha04
- Monitor 1.3.0-alpha04
- Orchestrator 1.3.0-alpha04
- Runner 1.3.0-alpha04
  - Fix AndroidJUnitRunner to report a test as failure if a StrictMode violation occurs
  - Add additional info when JUnit4 test class is malformed for easier diagnostics
- Rules 1.3.0-alpha04
- Truth 1.3.0-alpha04
- Test Services 1.3.0-alpha04
  - Include the test storage service in the test services

Here's [a full list of commits contained in version 1.3.0-alpha04](https://github.com/android/android-test/compare/androidx-test-1.3.0-alpha03...androidx-test-1.3.0-alpha04).

### Version 1.3.0-alpha03

December 3, 2019

This is an alpha release of AndroidX Test 1.3.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.3.0-alpha03
  - Support ActivityOptions in ActivityScenario
- Espresso 3.3.0-alpha03
  - Fix NoSuchMethodError when testing with AccessibilityChecks enabled (#376)
- Intents 3.3.0-alpha03
- JUnit 1.1.2-alpha03
- Monitor 1.3.0-alpha03
- Orchestrator 1.3.0-alpha03
- Runner 1.3.0-alpha03
  - Ignore NoClassDefFoundErrors when performing classpath scanning for tests
  - Add better error handling on unhandled exceptions
  - Allowing opting out of 'waitForActivitiesToComplete' via a runner argument
- Rules 1.3.0-alpha03
- Truth 1.3.0-alpha03
  - Update Location extensions to behave better with nulls.
  - Add stringArrayList and parcelableArrayList methods to BundleSubject

## Version 1.2.1

### Version 1.2.1-alpha02

July 15, 2019

This is an alpha release of AndroidX Test 1.2.1. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.2.1-alpha02
  - Make activity lifecycle transition timeout configurable
- Espresso 3.3.0-alpha02
- Intents 3.3.0-alpha02
  - Add a BundleMatchers.isEmpty() and isEmptyOrNull() methods
- JUnit 1.1.2-alpha02
- Monitor 1.3.0-alpha02
- Orchestrator 1.3.0-alpha02
- Runner 1.3.0-alpha02
- Rules 1.3.0-alpha02
- Truth 1.3.0-alpha02
  - Update to com.google.truth:truth:1.0 and com.google.guava:guava:27.0.1-android

### Version 1.2.1-alpha01

June 17, 2019

This is an alpha release of AndroidX Test 1.2.1. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.2.1-alpha01
  - Includes toolchain fix for 'Invalid parameter counts in MethodParameter attributes' build warning
- Espresso 3.3.0-alpha01
  - contrib: Replace usages of RecyclerView.findViewHolderForPosition method with its replacement
- Intents 3.3.0-alpha01
- JUnit 1.1.2-alpha01
- Monitor 1.3.0-alpha01
- Orchestrator 1.3.0-alpha01
- Runner 1.3.0-alpha01
- Rules 1.3.0-alpha01
  - Allow subclasses of ServiceTestRule to customize timeout
- Truth 1.3.0-alpha01
  - Add truth extensions for Location

## Version 1.2.0

### Version 1.2.0

May 29, 2019

This is the stable release of AndroidX Test 1.2.0.
It contains updates to the following libraries:

- Core 1.2.0
- Espresso 3.2.0
- Intents 3.2.0
- JUnit 1.1.1
- Monitor 1.2.0
- Orchestrator 1.2.0
- Runner 1.2.0
- Rules 1.2.0
- Truth 1.2.0

### Version 1.2.0-beta01

May 6, 2019

This is an beta release of AndroidX Test 1.2.0.
It contains updates to the following libraries:

- Core 1.2.0-beta01
  - More gracefully handle situations where multiple ActivityScenarios are used in a test
- Espresso 3.2.0-beta01
- Intents 3.2.0-beta01
- JUnit 1.1.1-beta01
- Monitor 1.2.0-beta01
  - Instrumentation.runOnMainSync() propogates exceptions back to calling thread
- Orchestrator 1.2.0-beta01
- Runner 1.2.0-beta01
- Rules 1.2.0-beta01
- Truth 1.2.0-beta01

### Version 1.2.0-alpha05

April 30, 2019

This is an alpha release of AndroidX Test 1.2.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.2.0-alpha05
  - Make ActivityScenario#onActivity callable from the main thread
- Espresso 3.2.0-alpha05
  - More deflaking of openActionBarOverflowOrOptionsMenu
- Intents 3.2.0-alpha05
- JUnit 1.1.1-alpha05
- Monitor 1.2.0-alpha05
- Orchestrator 1.2.0-alpha05
- Runner 1.2.0-alpha05
- Rules 1.2.0-alpha05
- Truth 1.2.0-alpha05
  - update to upstream google Truth 0.44

### Version 1.2.0-alpha04

April 18, 2019

This is an alpha release of AndroidX Test 1.2.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.2.0-alpha04
- Espresso 3.2.0-alpha04
  - Deflake openActionBarOverflowOrOptionsMenu
  - Add hook in androidx.test to simulate a window focus changed for local test environments
- Intents 3.2.0-alpha04
- JUnit 1.1.1-alpha04
- Monitor 1.2.0-alpha04
- Orchestrator 1.2.0-alpha04
- Runner 1.2.0-alpha04
  - Make androidx.test work if legacy android.test classes are not present
- Rules 1.2.0-alpha04
- Truth 1.2.0-alpha04

### Version 1.2.0-alpha03

April 7, 2019

This is an alpha release of AndroidX Test 1.2.0. New APIs are subject to change.
It contains updates to the following libraries:

- Core 1.2.0-alpha03
  - Add getState() API to ActivityScenario
- Espresso 3.2.0-alpha03
  - Convert WithTagKeyMatcher to accept `Matcher<?>` instead of `Matcher<Obj>`
  - Update link to espresso setup docs
  - Fix debug logging when running in different locales
- Intents 3.2.0-alpha03
- JUnit 1.1.1-alpha03
- Monitor 1.2.0-alpha03
  - Another attempt at clearing exception handler to prevent memory leaks in Robolectric.
- Orchestrator 1.2.0-alpha03
- Runner 1.2.0-alpha03
  - Add a tests_regex AJUR option to run tests matching a given regular expression.
- Rules 1.2.0-alpha03
- Truth 1.2.0-alpha03
  - Expose the ParcelableSubject API
  - Add BundleSubject#longInt
  - Add IntentSubject#hasComponent

## Version 1.1.1

### Version 1.1.1-alpha02

March 7, 2019

This is an alpha release of AndroidX Test 1.1.1. New APIs are subject to change.
It contains updates to the following libraries:

- Espresso 3.2.0-alpha02
- Intents 3.2.0-alpha02
  - Add IntentMatchers#filterEquals
  - Fix activity lifecycle timing bug in Intents#intended(). It now idles main looper before checking activity state.
- Runner 1.1.2-alpha02
  - Allow specifying both package and class filters.
- Truth 1.2.0-alpha02
- JUnit 1.1.1-alpha02
- Core 1.1.1-alpha02
  - Throw a RuntimeException when Activity cannot be resolved.
- Monitor 1.1.2-alpha02
  - Clear reference to uncaught exception handler to prevent memory leaks in Robolectric.
- Rules 1.1.2-alpha02
- Orchestrator 1.1.2-alpha02

### Version 1.1.1-alpha01

January 30, 2019

This is an alpha release of AndroidX Test 1.1.1. New APIs are subject to change.
It contains updates to the following libraries:

- Espresso 3.1.2-alpha01
  - Added method AccessibilityChecks.disable().
- Intents 3.1.2-alpha01
  - Add IntentMatchers#hasDataString
  - Fix activity lifecycle timing bug in Intents#intended(). It now idles main looper before checking activity state.
- Runner 1.1.2-alpha01
  - AndroidJUnitRunner now accepts comma separated class list in -e annotation option, for running only tests with all of the given annotations
- Truth 1.1.1-alpha01
  - Add filtersEquallyTo() to IntentSubject for comparison of intents using Intent.filterEquals().
- JUnit 1.1.1-alpha01
- Core 1.1.1-alpha01
- Monitor 1.1.2-alpha01
- Rules 1.1.2-alpha01
- Orchestrator 1.1.2-alpha01

## Version 1.1.0

### Version 1.1.0

December 13, 2018

This is the stable release of AndroidX Test 1.1.0.
It contains updates to the following libraries:

- Espresso 3.1.1
- Runner 1.1.1
- Rules 1.1.1
- Monitor 1.1.
- AndroidTestOrchestrator 1.1.1
- Core 1.1.0
- Truth 1.1.0
- JUnit 1.1.0

- Core 1.1.0

  - Make ActivityScenario support activities which start another activity

### Version 1.1.0-beta01

December 6, 2018

This is the beta01 release of AndroidX Test 1.1.0.
It contains updates to the following libraries:

- Core 1.1.0-beta01
  - New core-ktx kotlin extension artifact! Includes a kotlin-friendly ActivityScenario.launchActivity API
  - New ActivityScenario API for launching activities with custom intents
  - New ActivityScenario API for receiving an Activity result
  - Make ActivityScenario closeable
- Espresso3.1.1-beta01
  - Modify withResourceNameMatcher and HumanReadables to be API 28 compatible.
  - Update ReplaceTextAction's description to include the stringToBeSet
  - Support Espresso in Robolectric paused looper mode.
- JUnit 1.1.0-beta01
  - New ActivityScenarioRule API, for auto-launching and closing an Activity on test setup and teardown
  - New junit-ktx kotlin extension artifact! Includes a kotlin-friendly ActivityScenarioRule API
- Runner 1.1.1-beta01
  - Make -e package and -e testFile consistent in behavior when receiving packages
- Truth 1.1.0-beta01
  - Add bool, parcelable, and parcelableAsType BundleSubject APIs
- Rules 1.1.1-beta01
- Monitor 1.1.1-beta01
- AndroidTestOrchestrator 1.1.1-beta01

## Version 1.0.0

### Version 1.0.0

October 24, 2018

- All libraries
  - Set minSdkVersion to 14 and targetSdkVersion to 28
- Espresso 3.1.0
  - Fix withContentDescription to work with non-string types
  - Add support for using Espresso on Robolectric
  - Issue [73044169](https://issuetracker.google.com/issues/73044169): Espresso ViewMatchers.withText doesn't work when textAllCaps is enabled
  - Add support for injecting a sequence of motion events
- Intents
  - Add beta API for retrieving list of intents. Intended for use with new truth assertions
- Runner 1.1.0
  - Add support for instant apps
  - Deprecate androidx.test.runner.AndroidJUnit4 and replace with androidx.test.ext.junit.runners.AndroidJUnit4
- Monitor 1.1.0
  - Deprecate androidx.test.InstrumentationRegistry and replace with androidx.test.platform.app.InstrumentationRegistry and androidx.test.core.app.ApplicationProvider
- AndroidTestOrchestrator 1.1.0
  - Only enable orchestrator coverage handling if both 'coverage' and 'coverageFilePath' arguments are passed.
  - Only wait for debugger when the -debug is set but not for listing ATO test cases. A new orchestratorDebug flag was added for debugging orchestrator itself
- Core 1.0.0
  - New artifact! Includes new APIs that support both local and on-device tests for:
    - Retrieving context: ApplicationProvider
    - Controlling activity lifecycles: ActivityScenario(beta)
    - Builders for MotionEvent, PackageInfo
    - Parceables utility class
- Truth 1.0.0
  - New artifact! Includes custom truth subjects for Notification, Intent, Bundle, Parcelable, and MotionEvent
- JUnit 1.0.0
  - New artifact! Includes JUnit runner class androidx.test.ext.junit.runners.AndroidJUnit4 that supports both local and on-device tests.