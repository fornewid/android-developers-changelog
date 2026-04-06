---
title: https://developer.android.com/jetpack/androidx/releases/profileinstaller
url: https://developer.android.com/jetpack/androidx/releases/profileinstaller
source: md.txt
---

# ProfileInstaller

# ProfileInstaller

API Reference  
[androidx.profileinstaller](https://developer.android.com/reference/kotlin/androidx/profileinstaller/package-summary)  
Enables libraries to prepopulate ahead of time compilation traces to be read by ART.  

|  Latest Update  |                                     Stable Release                                      | Release Candidate | Beta Release | Alpha Release |
|-----------------|-----------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| October 2, 2024 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.4.1) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on ProfileInstaller, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.profileinstaller:profileinstaller:1.4.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.profileinstaller:profileinstaller:1.4.1")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1071684+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1071684&template=1592279)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.4

### Version 1.4.1

October 2, 2024

`androidx.profileinstaller:profileinstaller:1.4.1`is released. Version 1.4.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3bc0fb3beaccef509bb170cd69ddaad907b493b8..7f64d624bc8d619b4f6915bfba4d15f824b44aa1/profileinstaller/profileinstaller).

**Bug Fixes**

- Fixed support for multi-process Baseline Profile recording by signaling multiple processes sequentially. This fix requires both updating to`androidx.benchmark:benchmark-macro:1.4.0-alpha02`in your macrobenchmark/baseline profile module and`androidx.profileinstaller:profileinstaller:1.4.1`in the app. ([I0f519](https://android-review.googlesource.com/#/q/I0f51962266d3771ef72fad1a8c368316d8650694),[b/366231469](https://issuetracker.google.com/issues/366231469))

### Version 1.4.0

September 18, 2024

`androidx.profileinstaller:profileinstaller:1.4.0`is released. Version 1.4.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/96686b86417177a6743d87bead947ab48e8a5b7a..3bc0fb3beaccef509bb170cd69ddaad907b493b8/profileinstaller/profileinstaller).

**Important changes since 1.3.0**

- `ProfileInstaller`now supports capturing/installing profiles on API 35+. Updates to`ProfileInstaller`should no longer be required for platform version updates. ([6f9f6fa](https://android.googlesource.com/platform/frameworks/support/+/6f9f6fafc5b8cc8b9911de3222e2b598b6a7a5d6))
- Fixes crash when dropping shaders on Android U (API 34), as well as on emulators. ([I031ca](https://android-review.googlesource.com/#/q/I031ca38e15b9412e84a33eee4eb709cbf3014066),[b/274314544](https://issuetracker.google.com/issues/274314544))
- Fix method flag transcoding in the`V_015S`profile format. ([aosp/2906631](https://android-review.googlesource.com/c/platform/frameworks/support/+/2906631),[aosp/2847740](https://android-review.googlesource.com/c/platform/frameworks/support/+/2847740))

### Version 1.4.0-rc01

September 4, 2024

`androidx.profileinstaller:profileinstaller:1.4.0-rc01`is released with no changes from the last beta release. Version 1.4.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..686e63f6ac7e7d4a7909f9a7d145af07d03be3d2/profileinstaller/profileinstaller).

### Version 1.4.0-beta01

August 21, 2024

`androidx.profileinstaller:profileinstaller:1.4.0-beta01`is released with no changes from the last alpha. Version 1.4.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..8c4071562bd7e22b937284d71fb7aca9c4cd662c/profileinstaller/profileinstaller).

### Version 1.4.0-alpha02

August 7, 2024

`androidx.profileinstaller:profileinstaller:1.4.0-alpha02`is released. Version 1.4.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/eaded741fef7b77f24b638b5c600987cc8789759..9130b719318a69f2f3eaf82c32b131232fd721cb/profileinstaller/profileinstaller).

**New Features**

- Added api 35 support to Profile Installer. ([6f9f6fa](https://android.googlesource.com/platform/frameworks/support/+/6f9f6fafc5b8cc8b9911de3222e2b598b6a7a5d6))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.4.0-alpha01

February 7, 2024

`androidx.profileinstaller:profileinstaller:1.4.0-alpha01`is released.[Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3305e24b86112613150e9999ff18ea462a5ab76b..eaded741fef7b77f24b638b5c600987cc8789759/profileinstaller/profileinstaller)

**Bug Fixes**

- Added error code for no profile embedded to profile verifier. ([Ifb109](https://android-review.googlesource.com/#/q/Ifb1091758533f1491be99e23cfc84b61f8b3027b),[b/313928520](https://issuetracker.google.com/issues/313928520))
- Fixes crash when dropping shaders on Android U (API 34), as well as on emulators. ([I031ca](https://android-review.googlesource.com/#/q/I031ca38e15b9412e84a33eee4eb709cbf3014066),[b/274314544](https://issuetracker.google.com/issues/274314544))
- Enabled support for Android U in profile installer. ([Iaf177](https://android-review.googlesource.com/#/q/Iaf1779eb2abdd0030804240e505c68b8c39506f9))
- Fixed profile installer on Android U failing due to current profile not created empty when process starts. ([Ie3899](https://android-review.googlesource.com/#/q/Ie3899ddf7fd38be4d91fb0281ea4ead9f9f8288e))
- Fix method bitmap transcoding in the`V_015S`profile format. ([aosp/2906631](https://android-review.googlesource.com/c/platform/frameworks/support/+/2906631)) and ([aosp/2847740](https://android-review.googlesource.com/c/platform/frameworks/support/+/2847740))

## Version 1.3

### Version 1.3.1

May 3, 2023

`androidx.profileinstaller:profileinstaller:1.3.1`is released.[Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96686b86417177a6743d87bead947ab48e8a5b7a..3305e24b86112613150e9999ff18ea462a5ab76b/profileinstaller/profileinstaller)

**Bug Fixes**

- Enabled support for Android U in profile installer ([Iaf177](https://android-review.googlesource.com/#/q/Iaf1779eb2abdd0030804240e505c68b8c39506f9))
- Fixed profile installer on Android U failing due to current profile not created empty when process starts. ([Ie3899](https://android-review.googlesource.com/#/q/Ie3899ddf7fd38be4d91fb0281ea4ead9f9f8288e))

### Version 1.3.0

March 22, 2023

`androidx.profileinstaller:profileinstaller:1.3.0`is released.[Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..96686b86417177a6743d87bead947ab48e8a5b7a/profileinstaller/profileinstaller)

**Important changes since 1.2.0**

- Fixed a`NullPointerException`in`ProfileInstallReceiver`. ([b/243851384](https://issuetracker.google.com/issues/243851384))
- Added[`ProfileVerifier`](https://developer.android.com/reference/androidx/profileinstaller/ProfileVerifier)api to check from within the app if a baseline profile has been compiled, scheduled, or is missing ([I263a4](https://android-review.googlesource.com/#/q/I263a45582743afce0c3d9aefe629c07dfde77a72),[b/246653809](https://issuetracker.google.com/issues/246653809))
- Adds a new shell broadcast that enables Macrobenchmark to fully flush in-memory profile data to disk, to be included in baseline profile generation. This is required to use the macrobenchmark library to capture baseline profiles with`BaselineProfileRule`, and evaluate profile performance using`CompilationMode.Partial(warmupIterations)`.
- Added[a diagnostic code](https://developer.android.com/reference/kotlin/androidx/profileinstaller/ProfileInstaller#DIAGNOSTIC_PROFILE_IS_COMPRESSED())to detect compressed baseline profiles. Compressed baseline profiles cannot be installed by Profileinstaller in Macrobenchmarks or in production due to CPU overhead, and should be avoided when building your app by updating either to Studio/AGP Electric Eel or`bundletool`version`1.13.1`([I86413](https://android-review.googlesource.com/#/q/I8641387ad6073dde588d0d764da4a3b24b1c8ee4),[b/261998144](https://issuetracker.google.com/issues/261998144))
- Added hooks for macrobenchmark to capture profiles and drop shader cache, which are required for generating Baseline Profiles or macrobenchmarking on unrooted devices ([Ie0a7d](https://android-review.googlesource.com/#/q/Ie0a7d13cbe34476113bad955e47ed771d84e65a4),[b/250083467](https://issuetracker.google.com/issues/250083467),[b/253094958](https://issuetracker.google.com/issues/253094958)) ([Ia5171](https://android-review.googlesource.com/#/q/Ia5171b0f40dd8ce6f64f5ccf0a33281a4d8b121e),[b/231455742](https://issuetracker.google.com/issues/231455742))

### Version 1.3.0-rc01

March 8, 2023

`androidx.profileinstaller:profileinstaller:1.3.0-rc01`is released with no changes since the last beta.[Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..34caf23f3d501a274af3f34a759ce1ded741c2ae/profileinstaller/profileinstaller)

### Version 1.3.0-beta01

February 8, 2023

`androidx.profileinstaller:profileinstaller:1.3.0-beta01`is released.[Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..7d3ac1ab1206c01fae3ebb500b5b942636070155/profileinstaller/profileinstaller)

**API Changes**

- Removes support for handling compressed profiles - opening and decompressing leads to a 10s of ms regression in CPU utilization during startup, so instead added a diagnostic to discover incorrectly compressed baseline profiles. ([I86413](https://android-review.googlesource.com/#/q/I8641387ad6073dde588d0d764da4a3b24b1c8ee4),[b/261998144](https://issuetracker.google.com/issues/261998144))

### Version 1.3.0-alpha03

January 11, 2023

`androidx.profileinstaller:profileinstaller:1.3.0-alpha03`is released.[Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..adf1c279a86ab3886e1666c08e2c3efba783367b/profileinstaller/profileinstaller)

**Bug Fixes**

- Enables handling of compressed or uncompressed baseline profiles ([Ic61a0](https://android-review.googlesource.com/#/q/Ic61a096d5741e2516deb28a969bbf424fb568e4c))
- Fix`MacrobenchmarkScope.dropShaderCache()`to no longer crash by fixing broadcast registry in profileinstaller manifest ([I5c728](https://android-review.googlesource.com/#/q/I5c728449d99419a7599451414fe09f82c5970d3d),[b/258619948](https://issuetracker.google.com/issues/258619948))

### Version 1.3.0-alpha02

November 9, 2022

`androidx.profileinstaller:profileinstaller:1.3.0-alpha02`is released.[Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eef30a7b922be5eef255b7fbba9a3b43b4de0a25..a1e318590b217ecfce1b2de17eed2f18b6a680bb/profileinstaller/profileinstaller)

**API Changes**

- Added a hook for benchmarks to drop the shader cache, to ensure consistent performance for cold startups, especially when compiling with profiles from warmup iterations. This update is required to measure cold startups using`benchmark-macro-junit4:1.2.0-alpha05`or later. For Benchmark library's API changes, please refer to[Benchmark 1.2.0-alpha07](https://developer.android.com/jetpack/androidx/releases/benchmark#1.2.0-alpha07)page. ([Ia5171](https://android-review.googlesource.com/#/q/Ia5171b0f40dd8ce6f64f5ccf0a33281a4d8b121e),[b/231455742](https://issuetracker.google.com/issues/231455742))

### Version 1.3.0-alpha01

October 24, 2022

`androidx.profileinstaller:profileinstaller:1.3.0-alpha01`is released.[Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..eef30a7b922be5eef255b7fbba9a3b43b4de0a25/profileinstaller/profileinstaller)

**API Changes**

- Added`ProfileVerifier`api to check from within the app if a baseline profile has been compiled, scheduled, or is missing ([I263a4](https://android-review.googlesource.com/#/q/I263a45582743afce0c3d9aefe629c07dfde77a72),[b/246653809](https://issuetracker.google.com/issues/246653809))
- Adds a new shell broadcast that enables Macrobenchmark to fully flush in-memory profile data to disk, to be included in baseline profile generation. This is required to use the macrobenchmark library to capture baseline profiles with`BaselineProfileRule`, and evaluate profile performance using`CompilationMode.Partial(warmupIterations)`. ([Ie0a7d](https://android-review.googlesource.com/#/q/Ie0a7d13cbe34476113bad955e47ed771d84e65a4),[b/250083467](https://issuetracker.google.com/issues/250083467),[b/253094958](https://issuetracker.google.com/issues/253094958))

## Version 1.2.2

### Version 1.2.2

January 11, 2023

`androidx.profileinstaller:profileinstaller:1.2.2`is released.[Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2e3a67116121fa4f71ff424d8b0dd7fae1c08b97..0de62e140776bd6fce92cadd3312f1607df2c232/profileinstaller/profileinstaller)

**Bug Fixes**

- Enables handling of compressed or uncompressed baseline profiles ([Ic61a0](https://android-review.googlesource.com/#/q/Ic61a096d5741e2516deb28a969bbf424fb568e4c))

## Version 1.2.1

### Version 1.2.1

December 7, 2022

`androidx.profileinstaller:profileinstaller:1.2.1`is released.[Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..2e3a67116121fa4f71ff424d8b0dd7fae1c08b97/profileinstaller/profileinstaller)

**New Features**

- Enable profileinstaller for S_V2 (API 32) and TIRAMISU (API 33) ([b/254900303](https://issuetracker.google.com/254900303)).

## Version 1.2.0

### Version 1.2.0

July 27, 2022

`androidx.profileinstaller:profileinstaller:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..1e0793130863c72dc4a2d02bc975128f3ef0158b/profileinstaller/profileinstaller)

**Important changes since 1.1.0**

- Added support for the ART profile format used on Android 12 and going forward.
- Add new APIs in`ProfileInstallReceiver`to get more consistent results with`Macrobenchmarks`when using baseline profiles.

### Version 1.2.0-rc01

June 15, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-rc01`is released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..34fb17f767bcd64ac3bdd1f7ba6dda530791a9fe/profileinstaller/profileinstaller)

- This version is identical to`androidx.profileinstaller:profileinstaller:1.2.0-beta03`.

### Version 1.2.0-beta03

June 1, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-beta03`is released.[Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/profileinstaller/profileinstaller)

### Version 1.2.0-beta02

May 18, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-beta02`is released.[Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/profileinstaller/profileinstaller)

- No changes, needed to support Compose 1.2.0-beta02 versions.

### Version 1.2.0-beta01

May 11, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf/profileinstaller/profileinstaller)

**API Changes**

- Add new APIs in`ProfileInstallReceiver`to get more consistent results with`Macrobenchmarks`when using baseline profiles. ([If2ae5](https://android-review.googlesource.com/#/q/If2ae503e5f599e164d93eed0e9b4e6be832e6a53),[b/215740637](https://issuetracker.google.com/issues/215740637))

**Bug Fixes**

- Profile Installer throws a helpful message when trying to use metadata`V_001`format on Android 12 and above. ([aosp/1978526](https://android-review.googlesource.com/c/platform/frameworks/support/+/1978526),[b/217502387](https://issuetracker.google.com/issues/217502387))
- Profile Installer now uses`androidx.startup`version`1.1.1`. ([aosp/2077099](https://android-review.googlesource.com/c/platform/frameworks/support/+/2077099),[b/229828376](https://issuetracker.google.com/issues/229828376))

### Version 1.2.0-alpha02

January 26, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/profileinstaller/profileinstaller)

This version is identical to`1.2.0-alpha01`.

### Version 1.2.0-alpha01

January 12, 2022

`androidx.profileinstaller:profileinstaller:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/profileinstaller/profileinstaller)

**New Features**

- Add support for the ART profile format used on Android 12 and going forward.

## Version 1.1.0

### Version 1.1.0

February 9, 2022

`androidx.profileinstaller:profileinstaller:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/profileinstaller/profileinstaller)

### Version 1.1.0-rc01

December 15, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-rc01`is released with no updates since 1.1.0-beta04.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/profileinstaller/profileinstaller)

### Version 1.1.0-beta04

December 1, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-beta04`is released.[Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..75784ce6dbac6faa5320e5898e9472f02ab8710c/profileinstaller/profileinstaller)

### Version 1.1.0-beta03

November 17, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-beta03`is released.[Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/profileinstaller/profileinstaller)

**Bug Fixes**

- Updated to support Compose 1.1.0-beta03

### Version 1.1.0-beta02

November 3, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-beta02`is released.[Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/profileinstaller/profileinstaller)

**Bug Fixes**

- Updated to support Compose 1.1.0-beta02

### Version 1.1.0-beta01

October 27, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/profileinstaller/profileinstaller)

- No changes since 1.1.0-alpha07.

### Version 1.1.0-alpha07

October 13, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha07`is released.[Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/profileinstaller/profileinstaller)

**New Features**

- Added support for profm on Android N

### Version 1.1.0-alpha06

September 29, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha06`is released.[Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/profileinstaller/profileinstaller)

**Bug Fixes**

- Fix profileinstaller transcoding issues on N, O, and O_MR1. ([I12d75](https://android-review.googlesource.com/#/q/I12d759c4dc1ee570b7321671e3c9502924ed549d))

### Version 1.1.0-alpha05

September 15, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha05`is released.[Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/profileinstaller/profileinstaller)

**Bug Fixes**

- Fixed Android Nougat and Android Oreo profile transcoding for multidex apks.

### Version 1.1.0-alpha04

September 1, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha04`is released.[Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..47e81d1c497b8a57534a460c277855db1b0257ae/profileinstaller/profileinstaller)

**Bug Fixes**

- Fix`ProfileInstaller`to make it easier for apps using baseline profiles to run MacroBenchmarks using`CompilationMode.BaselineProfile`. ([I42657](https://android-review.googlesource.com/#/q/I426579600594e238b5b46adc20a6d4b33da3bab5),[b/196074999](https://issuetracker.google.com/issues/196074999))

### Version 1.1.0-alpha03

August 18, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha03`is released.[Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/profileinstaller/profileinstaller)

**Bug Fixes**

- Change profileinstaller skip behavior to log the PackageInfo.lastUpdatedTime in a file in the app's files directory and compare it prior to installing the profile on the next run. ([Ib93d1](https://android-review.googlesource.com/#/q/Ib93d1917a8a6a56162bf9e84c58ecc585fe86bfb))
- Adjust profile format on P, Q, R devices to conform to ART requirements ([I84e89](https://android-review.googlesource.com/c/platform/frameworks/support/+/1786568))

### Version 1.1.0-alpha02

August 4, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/profileinstaller/profileinstaller)

Updated to be compatible with Compose 1.1.0-alpha01.

### Version 1.1.0-alpha01

July 21, 2021

`androidx.profileinstaller:profileinstaller:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/profileinstaller/profileinstaller)

**Bug Fixes**

- Fixed bug that would trigger strict mode in some circumstances.

## Version 1.0

### Version 1.0.4

October 13, 2021

`androidx.profileinstaller:profileinstaller:1.0.4`is released.[Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/profileinstaller/profileinstaller)

- Updated to support Compose 1.0.4

### Version 1.0.3

September 29, 2021

`androidx.profileinstaller:profileinstaller:1.0.3`is released.[Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/profileinstaller/profileinstaller)

- Updated to support Compose 1.0.3

### Version 1.0.2

September 1, 2021

`androidx.profileinstaller:profileinstaller:1.0.2`is released.[Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/profileinstaller/profileinstaller)

**Bug Fixes**

- Added profile transcoding for P, Q, R devices. This change means that these devices will transcode the profile, ensuring that the written profile is always usable by ART. Previously transcoding would be skipped on these platforms, which sometimes lead ART to be unable to process the source profile. No changes to developer APIs.

### Version 1.0.1

August 4, 2021

`androidx.profileinstaller:profileinstaller:1.0.1`is released.[Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/profileinstaller/profileinstaller)

Updated to be compatible with Compose 1.0.1.

### Version 1.0.0

July 28, 2021

`androidx.profileinstaller:profileinstaller:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/profileinstaller/profileinstaller)

**Major features of 1.0.0**

Profile installer is a new library that allows libraries and applications to define "Profile Rules" and bundle ART profile information with an APK, and this library will install those profiles after application launch. This can be utilized to improve application performance.

Please see the detailed release notes at[1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.0.0-beta01)for more information on what these profile rules are and how they work.

### Version 1.0.0-rc02

July 14, 2021

`androidx.profileinstaller:profileinstaller:1.0.0-rc02`is released.[Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/profileinstaller/profileinstaller)

### Version 1.0.0-rc01

July 1, 2021

`androidx.profileinstaller:profileinstaller:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/profileinstaller/profileinstaller)

This is a RC release with no changes from beta.

### Version 1.0.0-beta01

June 16, 2021

`androidx.profileinstaller:profileinstaller:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4/profileinstaller/profileinstaller)

**Library Purpose**

Profile installer is a new library that allows libraries and applications to define "Profile Rules" and bundle ART profile information with an APK, and this library will install those profiles after application launch. This can be utilized to improve application performance.

This profile installation is done with the androidx.startup library. If for any reason one would like to disable profile installation, they can modify the manifest to remove it:  


           <provider
               android:name="androidx.startup.InitializationProvider"
               android:authorities="${applicationId}.androidx-startup"
               android:exported="false"
               tools:node="merge">
               <meta-data android:name="androidx.profileinstaller.ProfileInstallerInitializer"
                         tools:node="remove" />
           </provider>

This is especially useful if your app has nontrivial startup requirements and you would like to trigger the profile installation manually using the`ProfileInstaller.writeProfile`API.

**What are profile rules?**

- Profile rules for a library are specified in a text file`baseline-prof.txt`located in the`src/main`or equivalent directory. The file specifies a rule per line, where a rule in this case is a pattern for matching to methods or classes in the library. The syntax for these rules is a superset of the human-readable ART profile format that is used when using`adb shell profman --dump-classes-and-methods ...`. These rules take one of two forms to target either methods or classes.

- A method rule will have the following pattern:

      <FLAGS><CLASS_DESCRIPTOR>-><METHOD_SIGNATURE>

- And a class rule will have the following pattern:

      <CLASS_DESCRIPTOR>

- Here`<FLAGS>`is one or more of the characters`H`,`S`, and`P`to indicate whether or not this method should be flagged as "Hot", "Startup", or "Post Startup".

- The`<CLASS_DESCRIPTOR>`is the descriptor for the class that the targeted method belongs to. For example, the class`androidx.compose.runtime.SlotTable`would have a descriptor of`Landroidx/compose/runtime/SlotTable;`.

- The`<METHOD_SIGNATURE>`is the signature of the method, and includes the name, parameter types, and return types of the method. For example, the method`fun isPlaced(): Boolean`on`LayoutNode`has the signature`isPlaced()Z`.

- These patterns can have wildcards (`**`,`*`, and`?`) in order to have a single rule encompass multiple methods or classes.

**What do the rules do?**

- A method that has the flag`H`indicates that this method is a "hot" method, and should be compiled ahead of time.

- A method that has the flag`S`indicates that it is a method which is called at startup, and should be compiled ahead of time to avoid the cost of compilation and interpreting the method at startup time.

- A method that has the flag`P`indicates that it is a method which is called after startup.

- A class that is present in this file indicates that it is used during startup and should be pre-allocated in the heap to avoid the cost of class loading.

**How does this work?**

- Libraries can define these rules which will be packaged in AAR artifacts. When an APK is then built which includes these artifacts, these rules are merged together and the merged rules are used to build a compact binary ART profile that is specific to the APK. ART can then leverage this profile when the APK is installed on devices in order to ahead-of-time compile a specific subset of the application to improve the performance of the application, especially the first run. Note that this will have no effect on debuggable applications.

- Rule files should be named`baseline-prof.txt`and placed in the root directory of your main source set (it should be a sibling file to your`AndroidManifset.xml`file)

- Currently these files will only be utilized if you are using Android Gradle Plugin 7.0+, and is currently only enabled with a flag in your`gradle.properties`:

      # Enable adding baseline-prof.txt files to AAR artifacts, and binary profiles to APKs
      android.experimental.enableArtProfiles=true

**Profiles require a balance**

- Properly crafted profiles which correctly prioritize methods and classes that will be in the startup path and performance critical will yield the best results, however including too many methods or classes in profiles can end up having a net negative effect in terms of memory consumption and disk usage, so it is recommended to start conservatively if defining your own profile rules.