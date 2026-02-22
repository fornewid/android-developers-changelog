---
title: https://developer.android.com/jetpack/androidx/releases/input
url: https://developer.android.com/jetpack/androidx/releases/input
source: md.txt
---

# input

API Reference  
[androidx.input](https://developer.android.com/reference/kotlin/androidx/input/package-summary)  
Reduce the latency of input interactions by predicting future MotionEvents  

|   Latest Update   |                                Stable Release                                | Release Candidate | Beta Release | Alpha Release |
|-------------------|------------------------------------------------------------------------------|-------------------|--------------|---------------|
| November 19, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/input#1.0.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Input, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.input:input-motionprediction:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.input:input-motionprediction:1.0.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1263170+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1263170&template=1745246)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0

November 19, 2025

`androidx.input:input-motionprediction:1.0.0`is released. Version 1.0.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e3511bdaf82f43eeb8c415c3313a3f3904adc82b..b2bd14a028581cd8869c8ef9116871da68fd875e/input/input-motionprediction).

### Version 1.0.0-rc01

November 05, 2025

`androidx.input:input-motionprediction:1.0.0-rc01`is released. Version 1.0.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e53274587ab3eb7dde3a27872b6dfbfd7e55172f..31058ecdb7ebf3999769e9d79e2ecc2d2c7abd67/input/input-motionprediction).

**Bug Fixes**

- Moving the default`minSdk`from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.0.0-beta06

August 13, 2025

`androidx.input:input-motionprediction:1.0.0-beta06`is released. Version 1.0.0-beta06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1ddcc5c5a15362711a13f1d8a5b4278a4f7d5440..e53274587ab3eb7dde3a27872b6dfbfd7e55172f/input/input-motionprediction).

**New Features**

- The library will now use the system prediction API if available.

**API Changes**

- Removing obsolete`@RequiresApi(21)`annotations ([I9103b](https://android-review.googlesource.com/#/q/I9103beb2d5f73470f3abfdf034bc2b473be923e6))

### Version 1.0.0-beta05

October 2, 2024

`androidx.input:input-motionprediction:1.0.0-beta05`is released. Version 1.0.0-beta05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..1ddcc5c5a15362711a13f1d8a5b4278a4f7d5440/input/input-motionprediction).

**Bug Fixes**

- Prevent prediction from going beyond requested amount ([Ifbf49](https://android-review.googlesource.com/#/q/Ifbf492418e3a15ff4743526a394c2da7c3941268),[b/369330439](https://issuetracker.google.com/issues/369330439))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.0.0-beta04

May 1, 2024

`androidx.input:input-motionprediction:1.0.0-beta04`is released. Version 1.0.0-beta04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..fbd1ac175922f44c69a13545d194066ee428b342/input/input-motionprediction).

**New Features**

- Prediction will not stop suddenly
- Built-in prediction is now the default instead of the system one

**Bug Fixes**

- Move to 21 as the default`minSdkVersion`of androidx libraries ([I6ec7f](https://android-review.googlesource.com/#/q/I6ec7f80aafbe04c64c8f2d8fef82d4cd5c68525e))
- Fix down event time for the multi pointer events ([04824a](https://android-review.googlesource.com/#/q/04824a47b59e4708fe7964bcfb36631148430d1d)).
- Fix historical timestamp for the first pointer ([dee0b0](https://android-review.googlesource.com/#/q/dee0b0c4a6113a23fbf26021aa81cf05cd01cdc2)).
- Fix bad historical time when multiple pointers are present ([1189fa](https://android-review.googlesource.com/#/q/1189fa5f6841e2290dff8b86921ab63857cbd2c4)).

### Version 1.0.0-beta03

September 20, 2023

`androidx.input:input-motionprediction:1.0.0-beta03`is released.[Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/input/input-motionprediction)

**New Features**

- Increase prediction confidence when using accurate tools. ([57cb7c6](https://android.googlesource.com/platform/frameworks/support/+/57cb7c62c62fe4c95643d4777dbf3443f7ba7d1b))
- Optimized built-in prediction library memory allocation. ([0b7686e](https://android.googlesource.com/platform/frameworks/support/+/0b7686e0df49ea98b1b4e91979197ed3f6107574))

### Version 1.0.0-beta02

July 26, 2023

`androidx.input:input-motionprediction:1.0.0-beta02`is released.[Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..4aed940027a19667e67d155563fc5fa8b7279313/input/input-motionprediction)

**New Features**

- Add support for Android U system prediction API ([I7261f](https://android-review.googlesource.com/#/q/I7261fd0bdcfe0283ff9edbb4e19940bc4731c83e))

**API Changes**

- Merged public and experimental API files for h- thru m-paths ([Ic4630](https://android-review.googlesource.com/#/q/Ic46302e01e1352d8b4d37cb2468ef61474e79df3),[b/278769092](https://issuetracker.google.com/issues/278769092))

**Bug Fixes**

- Predicted motion events now report the correct down and event time ([I40059](https://android-review.googlesource.com/#/q/I400595643e50e8cdd5c2686df65ce4cd7965b598))

### Version 1.0.0-beta01

March 22, 2023

`androidx.input:input-motionprediction:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..5e7d256f82fbafb6d059ab7b18fddd87c7531553/input/input-motionprediction)

**New Features**

- Orientation and tilt are present in the predicted motion events
- Dynamically calculated prediction internals

**API Changes**

- Removed`close`method as it is no longer needed ([I84349](https://android-review.googlesource.com/#/q/I843491e06b583282a4a085737429c80bc6322d99))

### Version 1.0.0-alpha02

December 7, 2022

`androidx.input:input-motionprediction:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3511bdaf82f43eeb8c415c3313a3f3904adc82b..4a2f5e696614339c1ac21f706c1a17c0285780e7/input/input-motionprediction)

**API Changes**

- Renamed`recordMovement`to`record`, and`dispose`to`close`([I018c0](https://android-review.googlesource.com/#/q/I018c04a32c9129d6559ee85819d9a82773fd376f))

### Version 1.0.0-alpha01

October 24, 2022

`androidx.input:input-motionprediction:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b/input/input-motionprediction)

**New Features**

- Initial release of the input prediction AndroidX library. This includes an API to reduce the perceived latency of input interactions by predicting future motion events.

**API Changes**

- Introduces`MotionEventPredictor`, a utility that provides predicted motion events based on the previously received ones.