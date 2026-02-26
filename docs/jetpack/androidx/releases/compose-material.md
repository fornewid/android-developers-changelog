---
title: https://developer.android.com/jetpack/androidx/releases/compose-material
url: https://developer.android.com/jetpack/androidx/releases/compose-material
source: md.txt
---

# Compose Material

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.material](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary)  
[androidx.compose.material.icons](https://developer.android.com/reference/kotlin/androidx/compose/material/icons/package-summary)  
(*See the API reference docs for all compose packages*) Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.10.4](https://developer.android.com/jetpack/androidx/releases/compose-material#1.10.4) | - | - | [1.11.0-alpha06](https://developer.android.com/jetpack/androidx/releases/compose-material#1.11.0-alpha06) |

## Structure

Compose is combination of 7 Maven Group Ids within `androidx`. Each Group
contains a targeted subset of functionality, each with its own set of release
notes.

This table explains the groups and links to each set of release notes.

| Group | Description |
|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | Build animations in their Jetpack Compose applications to enrich the user experience. |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | Transform @Composable functions and enable optimizations with a Kotlin compiler plugin. |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces. |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io. |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI. |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target. |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input. |

## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.material:material:1.10.4"
}

android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.material:material:1.10.4")
}

android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:742043+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=742043&template=1346811)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.11

### Version 1.11.0-alpha06

February 25, 2026

`androidx.compose.material:material-*:1.11.0-alpha06` is released. Version 1.11.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..6e23fc0c137022098ae2d043778ffdc56402ba5e/compose/material).

### Version 1.11.0-alpha05

February 11, 2026

`androidx.compose.material:material-*:1.11.0-alpha05` is released. Version 1.11.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/material).

### Version 1.11.0-alpha04

January 28, 2026

`androidx.compose.material:material-*:1.11.0-alpha04` is released. Version 1.11.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/material).

### Version 1.11.0-alpha03

January 14, 2026

`androidx.compose.material:material-*:1.11.0-alpha03` is released. Version 1.11.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/material).

### Version 1.11.0-alpha02

December 17, 2025

`androidx.compose.material:material-*:1.11.0-alpha02` is released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/material).

### Version 1.11.0-alpha01

December 03, 2025

`androidx.compose.material:material-*:1.11.0-alpha01` is released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b48588febd37d5947dfa0f2827d2b5ca6af2ed90..deb96499dfe95073f5c1215c1287787683cb1e92/compose/material).

## Version 1.10

### Version 1.10.4

February 25, 2026

`androidx.compose.material:material-*:1.10.4` is released. Version 1.10.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0d23f956849b578e041ea4245127d4007eae43be..6b6d8d062bfb0daa907101a196d1ea43d60ecfe2/compose/material).

### Version 1.10.3

February 11, 2026

`androidx.compose.material:material-*:1.10.3` is released. Version 1.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b..0d23f956849b578e041ea4245127d4007eae43be/compose/material).

### Version 1.10.2

January 28, 2026

`androidx.compose.material:material-*:1.10.2` is released. Version 1.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c09ac6669b664a348ecf964a97968cd81479dcd4..fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b/compose/material).

### Version 1.10.1

January 14, 2026

`androidx.compose.material:material-*:1.10.1` is released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2120e7975523001d1eac390a5d9c5e2e9597267f..c09ac6669b664a348ecf964a97968cd81479dcd4/compose/material).

### Version 1.10.0

December 03, 2025

`androidx.compose.material:material-*:1.10.0` is released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26..a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9/compose/material).

### Version 1.10.0-rc01

November 19, 2025

`androidx.compose.material:material-*:1.10.0-rc01` is released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1c84233fc2372352b838d165d256581ff37ada9..b48588febd37d5947dfa0f2827d2b5ca6af2ed90/compose/material).

### Version 1.10.0-beta02

November 05, 2025

`androidx.compose.material:material-*:1.10.0-beta02` is released. Version 1.10.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/784e4a2de372f09d49c65fbc1ca64681a25a5f06..d1c84233fc2372352b838d165d256581ff37ada9/compose/material).

### Version 1.10.0-beta01

October 22, 2025

`androidx.compose.material:material-*:1.10.0-beta01` is released. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..784e4a2de372f09d49c65fbc1ca64681a25a5f06/compose/material).

### Version 1.10.0-alpha05

October 08, 2025

`androidx.compose.material:material-*:1.10.0-alpha05` is released. Version 1.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef9c81cf7222a390e0a467d8c8b48d04362fd3d..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/material).

### Version 1.10.0-alpha04

September 24, 2025

`androidx.compose.material:material-*:1.10.0-alpha04` is released. Version 1.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..6ef9c81cf7222a390e0a467d8c8b48d04362fd3d/compose/material).

### Version 1.10.0-alpha03

September 10, 2025

`androidx.compose.material:material-*:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/compose/material).

### Version 1.10.0-alpha02

August 27, 2025

`androidx.compose.material:material-*:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/material).

### Version 1.10.0-alpha01

August 13, 2025

`androidx.compose.material:material-*:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c30d03ab9e19dcf35e8b79438f0d91ee74cae557..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/material).

**Bug Fixes**

- Moving the default `minSdk` from API 21 to API 23. ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

## Version 1.9

### Version 1.9.5

November 19, 2025

`androidx.compose.material:material-*:1.9.5` is released. Version 1.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41..1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26/compose/material).

### Version 1.9.4

October 22, 2025

`androidx.compose.material:material-*:1.9.4` is released. Version 1.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea7909f13c54ea29d87d55d27ecf449000f82a8a..b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41/compose/material).

### Version 1.9.3

October 08, 2025

`androidx.compose.material:material-*:1.9.3` is released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6177e34a7667c42030e47ee8ecba82f09e2a5de..ea7909f13c54ea29d87d55d27ecf449000f82a8a/compose/material).

### Version 1.9.2

September 24, 2025

`androidx.compose.material:material-*:1.9.2` is released. Version 1.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/93a1ed2aac05dbfa192392b9d4ab27c40da53d69..b6177e34a7667c42030e47ee8ecba82f09e2a5de/compose/material).

### Version 1.9.1

September 10, 2025

`androidx.compose.material:material-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44da9aeaf3fa617c6f81f887691b37fe901109aa..93a1ed2aac05dbfa192392b9d4ab27c40da53d69/compose/material).

### Version 1.9.0

August 13, 2025

`androidx.compose.material:material-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..44da9aeaf3fa617c6f81f887691b37fe901109aa/compose/material).

**Important changes since 1.8.0**

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your gradle.properties. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Text field decoration box APIs are no longer experimental. ([I7480f](https://android-review.googlesource.com/#/q/I7480f45273b5d7617c256d32168eccf5f34aadf9))

**Bug Fixes**

- `ExposedDropdownMenu` is binary compat with older versions. ([I133f7](https://android-review.googlesource.com/#/q/I133f7ffd562aed04798ab77c38acc7e3f7f7b7d5))

### Version 1.9.0-rc01

July 30, 2025

`androidx.compose.material:material-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..c30d03ab9e19dcf35e8b79438f0d91ee74cae557/compose/material).

### Version 1.9.0-beta03

July 16, 2025

`androidx.compose.material:material-*:1.9.0-beta03` is released. Version 1.9.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d578548e34459870db64b61d8788d83f2cf49f54..5735a11c1798c2f8b419dfdc02347578a6ebf870/compose/material).

### Version 1.9.0-beta02

July 2, 2025

`androidx.compose.material:material-*:1.9.0-beta02` is released. Version 1.9.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..d578548e34459870db64b61d8788d83f2cf49f54/compose/material).

### Version 1.9.0-beta01

June 18, 2025

`androidx.compose.material:material-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e1d81d156ec778ff4b8bc291aa661d780576ea4c/compose/material).

**Bug Fixes**

- Hyperlinks in `Text(AnnotatedString)` now have Material styling by default. ([I0e8ed](https://android-review.googlesource.com/#/q/I0e8ed2883ccc1f74a823193c71b7c5d0374cd8cd), [b/339843816](https://issuetracker.google.com/issues/339843816))

### Version 1.9.0-alpha04

June 4, 2025

`androidx.compose.material:material-*:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fd8d5a2f883c1cdd7f712b200d5a4fedf342136..786176dc2284c87a0e620477608e0aca9adeff15/compose/material).

### Version 1.9.0-alpha03

May 20, 2025

`androidx.compose.material:material-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..5fd8d5a2f883c1cdd7f712b200d5a4fedf342136/compose/material).

### Version 1.9.0-alpha02

May 7, 2025

`androidx.compose.material:material-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/material).

### Version 1.9.0-alpha01

April 23, 2025

`androidx.compose.material:material-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/material).

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Text field decoration box APIs are no longer experimental ([I7480f](https://android-review.googlesource.com/#/q/I7480f45273b5d7617c256d32168eccf5f34aadf9), [b/269651160](https://issuetracker.google.com/issues/269651160))
- Deprecate `runWithTimingDisabled` in favor of `runWithMeasurementDisabled`, which more clearly describes the behavior - all metrics are paused. Additionally, expose the `MicrobenchmarkScope` superclass since redeclaring the `runWithMeasurementDisabled` function to open access isn't possible, since it's inline. ([I9e23b](https://android-review.googlesource.com/#/q/I9e23b0dfcff18f162ca0d2517734f3038870b59c), [b/389149423](https://issuetracker.google.com/issues/389149423), [b/149979716](https://issuetracker.google.com/issues/149979716))

**Bug Fixes**

- `ExposedDropdownMenu` is binary compat with older versions. ([I133f7](https://android-review.googlesource.com/#/q/I133f7ffd562aed04798ab77c38acc7e3f7f7b7d5))
- Fixed a crash at the progress and loading indicators in case a `Float.NaN` is passed in as a progress. ([I4fa96](https://android-review.googlesource.com/#/q/I4fa969a1d46358a6f1db8b28cb0a375a809102c2), [b/352364576](https://issuetracker.google.com/issues/352364576))

## Version 1.8

### Version 1.8.3

June 18, 2025

`androidx.compose.material:material-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/754896be0859599f16ed264d79a04ee337bac777..13362f65a9c0649415fe57052ea0e3932d2303d1/compose/material).

### Version 1.8.2

May 20, 2025

`androidx.compose.material:material-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/018e42f9db74b5e4fce8007734de4da6ae087407..754896be0859599f16ed264d79a04ee337bac777/compose/material).

### Version 1.8.1

May 7, 2025

`androidx.compose.material:material-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..018e42f9db74b5e4fce8007734de4da6ae087407/compose/material).

### Version 1.8.0

April 23, 2025

`androidx.compose.material:material-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b6bba717628c4c8c633c9509bfc4e4d9b89f428..d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9/compose/material).

### Version 1.8.0-rc03

April 9, 2025

`androidx.compose.material:material-*:1.8.0-rc03` is released. Version 1.8.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0907800009c0cb37dd12c5586d620350c1975de..1b6bba717628c4c8c633c9509bfc4e4d9b89f428/compose/material).

### Version 1.8.0-rc02

March 26, 2025

`androidx.compose.material:material-*:1.8.0-rc02` is released. Version 1.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/071f2b22541efa1d5d528479b28aa42960923a4f..c0907800009c0cb37dd12c5586d620350c1975de/compose/material).

### Version 1.8.0-rc01

March 12, 2025

`androidx.compose.material:material-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d195d8376d369f4bf74652abe60101aa658bbcc..071f2b22541efa1d5d528479b28aa42960923a4f/compose/material).

### Version 1.8.0-beta03

February 26, 2025

`androidx.compose.material:material-*:1.8.0-beta03` is released. Version 1.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/08954f0d500d220e8d6af07b4e6c51090911f779..2d195d8376d369f4bf74652abe60101aa658bbcc/compose/material).

### Version 1.8.0-beta02

February 12, 2025

`androidx.compose.material:material-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5d82c9c8e72f3dd8c4ee71ff5ac9a1365d24de4..08954f0d500d220e8d6af07b4e6c51090911f779/compose/material).

### Version 1.8.0-beta01

January 29, 2025

`androidx.compose.material:material-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8..80c9eca8dc00a6ae7188bf5f2beaf129b79de243/compose/material).

### Version 1.8.0-alpha08

January 15, 2025

`androidx.compose.material:material-*:1.8.0-alpha08` is released. Version 1.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8/compose/material).

**Bug Fixes**

- Adds `displayCutout` to the group of insets that Material components take into account by default, to avoid content overlapping with the display cutout.
  - This is a behavior change that will impact how inset-aware components behave around a display cutout. This includes the default value of the `WindowInsets` parameter for inset-aware Material 3 components, and the `WindowInsets` values provided in the component.
  - Defaults objects for both Material 2 and Material 3. If this change causes undesirable behavior, manually specify the `WindowInsets` parameter on a per-component basis. ([I43ee9](https://android-review.googlesource.com/#/q/I43ee9ad12db0450ebb9c65ce10d5c39d12628b6c), [b/362508045](https://issuetracker.google.com/issues/362508045))
- The activity that is used as the host for the composable under test when using `ComposeContentTestRule.setContent` now uses the theme `Theme.Material.Light.NoActionBar`, to avoid the `ActionBar` from overlapping with test content when targeting SDK 35. To opt out of this behavior, you can remove the dependency on `ui-test-manifest` and add an activity entry in your test app's `AndroidManifest.xml` for `ComponentActivity` with the theme of your choice. ([I7ae1b](https://android-review.googlesource.com/#/q/I7ae1bd28f5e341dafc07442b35ee4249793d257d), [b/383368165](https://issuetracker.google.com/issues/383368165))

**External Contribution**

- Expose `sheetGesturesEnabled` in `ModalBottomSheetLayout`. ([I3f032](https://android-review.googlesource.com/#/q/I3f032d9016b1730b1a90392209f7c07fa6617343), [b/329543529](https://issuetracker.google.com/issues/329543529))

### Version 1.8.0-alpha07

December 11, 2024

`androidx.compose.material:material-*:1.8.0-alpha07` is released. Version 1.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/compose/material).

**Bug Fixes**

- Fix text field size modifiers sometimes not being followed. ([I90d4c](https://android-review.googlesource.com/#/q/I90d4c690aabd1b4e35cb3934998a8c379671163f), [b/356905963](https://issuetracker.google.com/issues/356905963))

### Version 1.8.0-alpha06

November 13, 2024

`androidx.compose.material:material-*:1.8.0-alpha06` is released. Version 1.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/material).

### Version 1.8.0-alpha05

October 30, 2024

`androidx.compose.material:material-*:1.8.0-alpha05` is released. Version 1.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/material).

**Bug Fixes**

- Optimize Scaffold `contentPadding` behavior to avoid always recomposing the body content when the `contentPadding` changes. ([I8c8e2](https://android-review.googlesource.com/#/q/I8c8e226666d916662d5f5c22d4b02ca9ad0d6f97), [b/373904168](https://issuetracker.google.com/issues/373904168))
- Make the material Slider change its value when control keys are pressed. ([I1c442](https://android-review.googlesource.com/#/q/I1c442dee1c87e48a2d34c0277d36a9a5d3e14a5b))

### Version 1.8.0-alpha04

October 16, 2024

`androidx.compose.material:material-*:1.8.0-alpha04` is released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/material).

**API Changes**

- Remove `readOnly` from `TextFields`' to pin to stable foundation version. ([I3aaba](https://android-review.googlesource.com/#/q/I3aaba4e10f1317459d6a57acf32ec3ad50cd30bd))

**Bug Fixes**

- Adds support for ripples in expanding components on Android S+, such as a card that expands on click. Previously the ripple would not fill up the new size but now it will expand to the new bounds. ([If509a](https://android-review.googlesource.com/#/q/If509acac87caa3f13aa2cf969f7bfade7da3e7f6), [b/183019123](https://issuetracker.google.com/issues/183019123))

### Version 1.8.0-alpha02

September 18, 2024

`androidx.compose.material:material-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988..0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/material).

### Version 1.8.0-alpha01

September 4, 2024

`androidx.compose.material:material-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988/compose/material).

**API Changes**

- Added new `NavGraphBuilder.bottomSheet` builder to create a bottomSheet with safe args (([I28589](https://android-review.googlesource.com/#/q/I28589fd1d67de6a23167e6a7648f15d95ed4beb3), [I777db](https://android-review.googlesource.com/#/q/I777dbf640b83cd3428fd37c4ff5a8065f9ff856e), [b/351858980](https://issuetracker.google.com/issues/351858980)))
- Added new `TextField` and `OutlinedTextField` overloads that take a `TextFieldState` ([I3b74c](https://android-review.googlesource.com/#/q/I3b74c1d94f689ac738d32fc14263d76f8150e453))

## Version 1.7

### Version 1.7.8

February 12, 2025

`androidx.compose.material:material-*:1.7.8` is released. Version 1.7.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/456f991655af86d9ae121f7e93f8699f958fc7ac..215cdfd8cb9c0762dd0347c383250644057c367f/compose/material).

### Version 1.7.7

January 29, 2025

`androidx.compose.material:material-*:1.7.7` is released. No changes from 1.7.6.

### Version 1.7.6

December 11, 2024

`androidx.compose.material:material-*:1.7.6` is released. Version 1.7.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cbf03b378a865660d8209d0229c2bb1928c6e33..5e65beadeb2e2c15f34d0fff72861847795cca4f/compose/material).

### Version 1.7.5

October 30, 2024

`androidx.compose.material:material-*:1.7.5` is released. Version 1.7.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b0ae0e41147a8a917cab35b4a6487af4fce6ead..4cbf03b378a865660d8209d0229c2bb1928c6e33/compose/material).

### Version 1.7.4

October 16, 2024

`androidx.compose.material:material-*:1.7.4` is released. Version 1.7.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/00e91ed140ce2c4677f56fc06692b182b8a07fcf..6b0ae0e41147a8a917cab35b4a6487af4fce6ead/compose/material).

### Version 1.7.2

September 18, 2024

`androidx.compose.material:material-*:1.7.2` is released. Version 1.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1efd0b233a17f707cd918993df1fa12e0bf9ae83..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/material).

### Version 1.7.1

September 10, 2024

- No changes to Android artifacts. `-desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts.

### Version 1.7.0

September 4, 2024

`androidx.compose.material:material-*:1.7.0` is released. Version 1.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d8995e2377dd4baad64b39becb6d480cadd05c86..38ffb9c315c3f894412184bda180c1b58b2a8556/compose/material).

**Important changes since 1.6.0**

- Material components have been migrated to use the new ripple APIs, and no longer query `RippleTheme`.
- Material components that previously accepted a `MutableInteractionSource` and defaulted to `remember { MutableInteractionSource() }` now accept a nullable `MutableInteractionSource` and default to null instead. If you are not hoisting and using the `MutableInteractionSource`, you should pass null. This allows for some components to lazily create an instance only when needed, improving performance. It is also recommended that you make similar changes in your own components.
- `BottomDrawer`, `ModalBottomSheet`, `BackdropScaffold` and standard Bottomsheet have been promoted to stable API.

### Version 1.7.0-rc01

August 21, 2024

`androidx.compose.material:material-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98bc1cf10201a973793b72d2ff1ae728070e47e4..d8995e2377dd4baad64b39becb6d480cadd05c86/compose/material).

### Version 1.7.0-beta07

August 7, 2024

`androidx.compose.material:material-*:1.7.0-beta07` is released. Version 1.7.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16151cbc8a68e976da6f2b0f624c2e9883c55aa3..98bc1cf10201a973793b72d2ff1ae728070e47e4/compose/material).

### Version 1.7.0-beta06

July 24, 2024

`androidx.compose.material:material-*:1.7.0-beta06` is released. Version 1.7.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8346df8de9f86a546fc9c316113bd4a3cc82ede9..16151cbc8a68e976da6f2b0f624c2e9883c55aa3/compose/material).

### Version 1.7.0-beta05

July 10, 2024

`androidx.compose.material:material-*:1.7.0-beta05` is released. Version 1.7.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/487d2b07dba29c903cfd87a8dc7f99483084ebb6..8346df8de9f86a546fc9c316113bd4a3cc82ede9/compose/material).

### Version 1.7.0-beta04

June 26, 2024

`androidx.compose.material:material-*:1.7.0-beta04` is released. Version 1.7.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c29f7383c14ede0af9cb64be9f3eee63714bc73c..487d2b07dba29c903cfd87a8dc7f99483084ebb6/compose/material).

### Version 1.7.0-beta03

June 12, 2024

`androidx.compose.material:material-*:1.7.0-beta03` is released. Version 1.7.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a123f646cfea1599f9efead6da546b0c26063fa..3bb7e8ef41a5a1cec16efda4248c7865d2da51c4/compose/material).

### Version 1.7.0-beta02

May 29, 2024

`androidx.compose.material:material-*:1.7.0-beta02` is released. Version 1.7.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..1a123f646cfea1599f9efead6da546b0c26063fa/compose/material).

**API Changes**

- Update API for styling the links: moved the `TextLinkStyles` to the `TextStyle` and removed the `TextDefaults` from material ([I5477b](https://android-review.googlesource.com/#/q/I5477bdb498b6b4f33ab3bc998e2be59d8a4ff7e4))

### Version 1.7.0-beta01

May 14, 2024

`androidx.compose.material:material-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/material).

**API Changes**

- Updated the API for getting Material themed links in Text. Specifically, removed the methods from the `TextDefaults` for constructing themed `LinkAnnotations` and parse HTML with themed links. Instead, added a `TextLinkStyles` class that allows to style the links as a parameter to the Text composable. ([I31b93](https://android-review.googlesource.com/#/q/I31b93f4460f4a0a50c7a86996a499d359ba455c8))

### Version 1.7.0-alpha08

May 1, 2024

`androidx.compose.material:material-*:1.7.0-alpha08` is released. Version 1.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7/compose/material).

**API Changes**

- Fix `backgroundColor` not applying to `TextFieldDecorationBox` and `OutlinedTextFieldDecorationBox`. Decoration boxes now accept a `shape` parameter. ([I371c2](https://android-review.googlesource.com/#/q/I371c26718597cb36ac537e9412ce476532afb40d), [b/307694651](https://issuetracker.google.com/issues/307694651))
- `RippleConfiguration#isEnabled` has been removed, and `LocalRippleConfiguration` has been made nullable. To disable a ripple, instead of providing a `RippleConfiguration` with `isEnabled = false`, provide `null` to `LocalRippleConfiguration`. ([I22725](https://android-review.googlesource.com/#/q/I22725ce120f27f7dd0041bfabff5f3faff614ea9))
- Text links have a pressed state styling option in addition to normal styling, hovered and focused. `TextDefaults` methods each have a `pressedStyle` argument to support that. ([Ic473f](https://android-review.googlesource.com/#/q/Ic473f81fd32d95ad84d6bc452c8dcbf6de7ba4ba), [b/139312671](https://issuetracker.google.com/issues/139312671))

**Bug Fixes**

- `OutlinedTextField` top padding for label now accounts for system font size. ([Idc781](https://android-review.googlesource.com/#/q/Idc78176ca566364b041b5863aa477ada660d05a9))

### Version 1.7.0-alpha07

April 17, 2024

`androidx.compose.material:material-*:1.7.0-alpha07` is released. Version 1.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/material).

**API Changes**

- Text links got pressed state styling option in addition to normal styling, hovered and focused. ([I5f864](https://android-review.googlesource.com/#/q/I5f864b3fd1b1af6ff39dee03e1aa65ede7e16d32), [b/139312671](https://issuetracker.google.com/issues/139312671))
- Added a `TextDefaults` object that contains methods to construct a `LinkAnnotation` and parse HTML-tagged string which apply `MaterialTheme` to the links. ([I98532](https://android-review.googlesource.com/#/q/I98532f3512d1930416f66dd195746eeeba884497), [b/139312671](https://issuetracker.google.com/issues/139312671))

### Version 1.7.0-alpha06

April 3, 2024

`androidx.compose.material:material-*:1.7.0-alpha06` is released. Version 1.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/material).

**Announcement**

- `androidx.compose.material` no longer requires using the same version of every artifact is this maven group. Users can mix and match versions of Compose foundation libraries ([Ie5fba](https://android-review.googlesource.com/#/q/Ie5fba03cf3045df6ef6a4baaf3b8a0b3e88da552))

**API Changes**

- Moved more `ModalDrawer` and `BottomDrawer` defaults into `DrawerDefaults` object. ([Ib5b2e](https://android-review.googlesource.com/#/q/Ib5b2e175d2d59735376377301471dbf4f125591f))

### Version 1.7.0-alpha05

March 20, 2024

`androidx.compose.material:material-*:1.7.0-alpha05` is released. Version 1.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/material).

**API Changes**

- The `ScaffoldSubcomposeInMeasureFix` flag has been removed. ([I67363](https://android-review.googlesource.com/#/q/I67363b370f20618118553c43805cd565149e38d4))

### Version 1.7.0-alpha04

March 6, 2024

`androidx.compose.material:material-*:1.7.0-alpha04` is released. Version 1.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/material).

**New Features**

- Added a new `androidx.compose.material:material-navigation` artifact that adds support for bottom sheets as destinations when using [Navigation Compose](https://developer.android.com/jetpack/compose/navigation). This replaces the [Accompanist Navigation Material library](https://google.github.io/accompanist/navigation-material/). ([d65d57](https://android.googlesource.com/platform/frameworks/support/+/d65d5731e4f0dfe560b43eae886a4fabfa949b84), [b/180247978](https://issuetracker.google.com/180247978))

### Version 1.7.0-alpha03

February 21, 2024

`androidx.compose.material:material-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/material)

**API Changes**

- `BottomDrawer` has been promoted from experimental to stable. `BottomDrawerState` now exposes the progress as a function, allowing to query progress between specific targets. `BottomDrawerState` now allows customizing the animation spec, and `confirmStateChange` is not a trailing lambda anymore. ([I9c029](https://android-review.googlesource.com/#/q/I9c029340ea69a755ad0cd8f46b8fcdc76422c41c), [b/261423850](https://issuetracker.google.com/issues/261423850))
- `BackdropScaffold` has been promoted from experimental to stable. The animation spec is now a `tween` spec in accordance with guidelines. The `snackbarHost` parameter of `BackdropScaffold` is no longer the last parameter to avoid confusion with trailing lambdas. `BackdropScaffoldState` exposes a `progress(from, to)` API to query progress between anchors. ([I73f48](https://android-review.googlesource.com/#/q/I73f48dd7d1aab0a57d728f562f22bda5020ccd4b), [b/261423218](https://issuetracker.google.com/issues/261423218))
- Standard bottom sheets have been promoted from experimental to stable. Deprecated constructors have been removed. The animation spec is now a tween spec in accordance with guidelines. ([I3c1a8](https://android-review.googlesource.com/#/q/I3c1a892338d183db35ecf3c023255682b4e785bd), [b/278692145](https://issuetracker.google.com/issues/278692145), [b/261409034](https://issuetracker.google.com/issues/261409034))
- Modal bottom sheets have been promoted from experimental to stable. Deprecated constructors have been removed. The animation spec is now a `tween` spec in accordance with guidelines. ([Ic53f4](https://android-review.googlesource.com/#/q/Ic53f4fe7c7183569cb7322c8f56f571be5316be0), [b/278692145](https://issuetracker.google.com/issues/278692145), [b/266780235](https://issuetracker.google.com/issues/266780235), [b/261409034](https://issuetracker.google.com/issues/261409034))

**Bug Fixes**

- Fixed an issue where `BackdropScaffold` could crash in specific scenarios in combination with `LookaheadScope`. ([I51396](https://android-review.googlesource.com/#/q/I5139666a03c031ae50528e493aa415a9cf00c7d1))
- Removed subcomposition inside `BottomSheetScaffold` to improve performance. Fixed an issue where `BottomSheetScaffold` would crash in specific scenarios in combination with `LookaheadScope`. ([I2f90c](https://android-review.googlesource.com/#/q/I2f90cfec6dde3d7c9d351ab3e7d8917b13adb126))
- Removed subcomposition inside `ModalBottomSheetLayout`, improving performance. ([I7a025](https://android-review.googlesource.com/#/q/I7a0255c0ad99a0be553f95c13f9fa2eda38b2aeb))

### Version 1.7.0-alpha02

February 7, 2024

`androidx.compose.material:material-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3abba2d2e4a810f1cf9909ba77546cae2258919d..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/material)

### Version 1.7.0-alpha01

January 24, 2024

`androidx.compose.material:material-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..3abba2d2e4a810f1cf9909ba77546cae2258919d/compose/material)

**Behavior Changes**

- Material components have been migrated to use the new ripple APIs, and no longer query `RippleTheme`.

**API Changes**

- `rememberRipple` and `RippleTheme` have been deprecated from material-ripple, with new ripple and `RippleConfiguration` APIs added to material and other design system libraries.

- Material components that previously accepted a `MutableInteractionSource` and defaulted to remember `{ MutableInteractionSource() }` now accept a nullable `MutableInteractionSource` and default to null instead. If you are not hoisting and using the `MutableInteractionSource`, you should pass null. This allows for some components to lazily create an instance only when needed, improving performance. It is also recommended that you make similar changes in your own components.

## Version 1.6

### Version 1.6.8

June 12, 2024

`androidx.compose.material:material-*:1.6.8` is released. Version 1.6.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a13a0e3b1197d66bfc19b9051576bc705f2c337..9dbbab668fd22cd643de4651197354a828aaa7b9/compose/material).

### Version 1.6.7

May 1, 2024

`androidx.compose.material:material-*:1.6.7` is released. Version 1.6.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b..9a13a0e3b1197d66bfc19b9051576bc705f2c337/compose/material).

### Version 1.6.6

April 17, 2024

`androidx.compose.material:material-*:1.6.6` is released. No changes since the last release.

### Version 1.6.5

April 3, 2024

`androidx.compose.material:material-*:1.6.5` is released. Version 1.6.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3..917ada96acf0ac343128c3f4af9bd67a4b80b99c/compose/material).

### Version 1.6.4

March 20, 2024

`androidx.compose.material:material-*:1.6.4` is released. Version 1.6.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/22b329dfa8888198eb3024650d236b3afe6c0907..1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3/compose/material).

### Version 1.6.3

March 6, 2024

`androidx.compose.material:material-*:1.6.3` is released. Version 1.6.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af119e2e31de85654fb7b2e5a2c7e724231131fd..22b329dfa8888198eb3024650d236b3afe6c0907/compose/material).

**Bug Fixes**

- Fix regression in `ExposedDropdownMenu` to make it focusable again. ([c0e0ed](https://android-review.googlesource.com/#/q/b3e6ebe4229e10fa0711277b139316d3e6c0e0ed), [b/323694447](https://issuetracker.google.com/issues/322269951))

### Version 1.6.2

February 21, 2024

`androidx.compose.material:material-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f639ccf09a84fa5af4a9016fa239539aeed40b94..af119e2e31de85654fb7b2e5a2c7e724231131fd/compose/material)

### Version 1.6.1

February 7, 2024

`androidx.compose.material:material-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..f639ccf09a84fa5af4a9016fa239539aeed40b94/compose/material)

### Version 1.6.0

January 24, 2024

`androidx.compose.material:material-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/296c44d6ba03d2167bdea85d53e8387d7b1644f9..4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf/compose/material)

### Version 1.6.0-rc01

January 10, 2024

`androidx.compose.material:material-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc038a4bc84de9ab20493d6efa8d26f4a70214ae..6dc685be02316455881d22b69d0bb8adbe768c4f/compose/material)

### Version 1.6.0-beta03

December 13, 2023

`androidx.compose.material:material-*:1.6.0-beta03` is released. [Version 1.6.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15c82aaef0f1fd0307d6c00061859e5b6c4384c6..b76585a287cbcfdae38c3e16e5acbc6e26e808e2/compose/material)

### Version 1.6.0-beta02

November 29, 2023

`androidx.compose.material:material-*:1.6.0-beta02` is released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..15c82aaef0f1fd0307d6c00061859e5b6c4384c6/compose/material)

### Version 1.6.0-beta01

November 15, 2023

`androidx.compose.material:material-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose/material)

### Version 1.6.0-alpha08

October 18, 2023

`androidx.compose.material:material-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/material)

**API Changes**

- Deprecate a `materialIcon` function in favor of its overload that takes an `autoMirror` parameter. ([Ia338d](https://android-review.googlesource.com/#/q/Ia338d719d9bf0c053bf41cc4f8f4acb714240ff9))

**Bug Fixes**
- Auto-increase height of nav item for large content. ([0c4ecc](https://android-review.googlesource.com/c/platform/frameworks/support/+/2768305), [b/272336962](https://issuetracker.google.com/issues/272336962))

### Version 1.6.0-alpha07

October 4, 2023

`androidx.compose.material:material-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..1f7407d4293384a1b91bc142880e3525048b3443/compose/material)

- Dependency updates

### Version 1.6.0-alpha06

September 20, 2023

`androidx.compose.material:material-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/material)

**Behavior Breaking Change**

- Removed drawer-related functionality from `BottomSheetScaffold`. Wrap your `BottomSheetScaffold` in a Drawer composable to achieve the previous functionality. See `BottomSheetScaffoldWithDrawerSample` for an example. ([I1dcc8](https://android-review.googlesource.com/#/q/I1dcc8c426b3a956c0103c8637b22873c6237b0d9))

**API Changes**

- Introduced a temporary flag to control whether Scaffold should measure its children during measurement or during placement. By default, this will measure in measurement. If you are facing issues with the new behavior, please file an issue. ([If6e3b](https://android-review.googlesource.com/#/q/If6e3b68c0af4445e5c94f8a49cc64323d7f2ed32))

### Version 1.6.0-alpha05

September 6, 2023

`androidx.compose.material:material-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/material)

**New Features**

- Added support for auto-mirrored icons when rendered in right-to-left layouts. Icons in the material-icons-core and material-icons-extended modules are now providing additional icon sets for supporting auto-mirroring when the icon allows it. The new sets are prefixed with `Icons.AutoMirrored.Filled...` etc., and hold icons that will auto-mirror on RTL layouts. See the [list of Material icons](http://developers.google.com/fonts/docs/material_icons) for the list of icons that can (and should) be auto-mirrored.

**API Changes**

- Added support for auto-mirrored icons when rendered in right-to-left layouts. Icons in the material-icons-core and material-icons-extended modules are now providing additional icon sets for supporting auto-mirroring when the icon allows it. The new sets are prefixed with `Icons.AutoMirrored.Filled...` etc., and hold icons that will auto-mirror on RTL layouts. See the [list of Material icons](http://developers.google.com/fonts/docs/material_icons) for the list of icons that can (and should) be auto-mirrored. The previously provided icon properties for those icons are now marked as deprecated, and provides a replacement-block suggestion to help with the migration. In case you don't have any special handling for mirroring icons on RTL, we recommend migrating to the new set of icons. For example, `Icons.Filled.ArrowBack` should be refactored to `Icons.AutoMirrored.Filled.ArrowBack`. ([I4b511](https://android-review.googlesource.com/#/q/I4b5116207cb9c0dd1a8a72d2bd3f606f8fdd0129))

### Version 1.6.0-alpha04

August 23, 2023

`androidx.compose.material:material-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/material)

**Bug Fixes**

- Fixed an issue where some components using `Subcomposition` (e.g. `BottomSheetScaffold`) inside a Scaffold inside a `LookaheadScope` were attempting to read their size too early. ([If2c5d](https://android-review.googlesource.com/#/q/If2c5daa98914149d12be03e02ba650c24acf19b8))
- Fixed `DropdownMenu`'s `offset` calculation so x offsets depend solely on the local layout direction, and y offsets will no longer be reversed when the menu is near the bottom of the screen. ([Iccc74](https://android-review.googlesource.com/#/q/Iccc743f3306d9b259f0cc21d1089d9479df203fb), [b/294103942](https://issuetracker.google.com/issues/294103942))
- Optimized `BottomSheetScaffold`'s layout internals and fixed a potential issue with `BottomSheetScaffold` inside a `LookaheadLayout`. ([Ic0afa](https://android-review.googlesource.com/#/q/Ic0afaf770bc5062ddae0159698402a00cf29bd0c))

### Version 1.6.0-alpha03

August 9, 2023

`androidx.compose.material:material-*:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/material)

**API Changes**

- Material2 components now have a separate API to pass `windowInsets` to support edge-to-edge functionality in android. Unlike material3 components, material2 components do not support insets by default and the value should be passed manually. Refer to the corresponding samples for guidance. ([I655e8](https://android-review.googlesource.com/#/q/I655e87062da5c3b01c3923e6711ba12977e0b3d8))

### Version 1.6.0-alpha02

July 26, 2023

`androidx.compose.material:material-*:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/material)

**API Changes**

- We are moving the density dependency to the component level. This applies to the following components: `SwipeToDismiss` and Sheet based components. Please use the new overload provided where density is a parameter. ([I1846e](https://android-review.googlesource.com/#/q/I1846ea6aeb659f53eb8bff6895f7aea19af46fe8))
- Additional annotations to specify allowed inputs to composables ([I51109](https://android-review.googlesource.com/#/q/I51109ce34ab8bb50a8104572d79d2a94b67f3b17))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b), [b/287516207](https://issuetracker.google.com/issues/287516207))
- Added new Start alignment for `FabPosition` ([Ib7aea](https://android-review.googlesource.com/#/q/Ib7aea97d6ac5c6ee33fd10916c74c540ff5889de), [b/170592777](https://issuetracker.google.com/issues/170592777))
- `TextFieldColorsWithIcons` in Material 2 has been deprecated in favor of `TextFieldColors`. When overriding `leadingIconColor` or `trailingIconColor`, also override the overload with `interactionSource`. ([Id57ed](https://android-review.googlesource.com/#/q/Id57eda2be81aa23263a9c9a83e89789934acf169), [b/199377790](https://issuetracker.google.com/issues/199377790))

### Version 1.6.0-alpha01

June 21, 2023

`androidx.compose.material:material-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..3b5b931546a48163444a9eddc533489fcddd7494/compose/material)

**Behavior Changes**

- `includeFontPadding` is now `false` by default in Material 2 typography. The default line height style has also been changed to `Trim.None` and `Alignment.Center`, and explicit `lineHeight` (in sp) have been added to the `TextStyle`s of `Typography`. Consult [the API docs](https://developer.android.com/jetpack/compose/text/style-paragraph#adjust-line-height) if you want to customize these values, and see [the blog post](https://medium.com/androiddevelopers/fixing-font-padding-in-compose-text-768cd232425b) for an in-depth explainer of these changes. ([Icabc3](https://android-review.googlesource.com/#/q/Icabc31f64e23ba0b8b92c909a8df1fe5f72ce9ed), [I3f801](https://android-review.googlesource.com/#/q/I3f8014ab249694ce695fc7655b6c5d27ca872acd), [I04c03](https://android-review.googlesource.com/#/q/I04c0331d11740f21f37b5f480a312012b122d22b))

**API Changes**

- Material's `Swipeable` APIs have been deprecated. Please refer to Foundation's `AnchoredDraggable` APIs which are optimized for both simple and complex use cases. ([I732e0](https://android-review.googlesource.com/#/q/I732e03d07da57c1231ea2ebd84f793aaab1df2dd))

**Bug Fixes**

- `BottomSheetState`, `ModalBottomSheetState` and `BottomDrawerState` now expose a progress property indicating the progress between the current (settled) anchor and the closest anchor in the swipe direction. ([I1b317](https://android-review.googlesource.com/#/q/I1b31727b4f56df890e336bea9f4de526733aaacc), [b/271169225](https://issuetracker.google.com/issues/271169225), [b/276375124](https://issuetracker.google.com/issues/276375124), [b/276776071](https://issuetracker.google.com/issues/276776071), [b/270066861](https://issuetracker.google.com/issues/270066861))

## Version 1.5

### Version 1.5.4

October 18, 2023

`androidx.compose.material:material-*:1.5.4` is released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ed495b997a532cc4cbe39abdbaa98b8fc6f3764..b6d5e6e62e40f6938bdbcfef1d6c8a79e25006f8/compose/material)

### Version 1.5.3

October 4, 2023

`androidx.compose.material:material-*:1.5.3` is released. This version does not have any changes

### Version 1.5.2

September 27, 2023

`androidx.compose.material:material-*:1.5.2` is released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a2cac855f7723e1e485c20ac68d34dc8bb68d1e..2bc777611812ef8ef7329a332fbaf8348af05ec7/compose/material)

### Version 1.5.1

September 6, 2023

`androidx.compose.material:material-*:1.5.1` is released with no changes. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/material)

### Version 1.5.0

August 9, 2023

`androidx.compose.material:material-*:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d83e1a7d6afe597aed6e48be005010c7a26486dd..65e3f15108d25a7e1c5c841c0855b21eca194070/compose/material)

**Important changes since 1.4.0**

**API Changes**

- Incorporated changes in the Swipeable1 APIs in `BottomSheetScaffold`. `BottomSheetState`'s `confirmStateChange` param has been renamed to `confirmValueChange`. `progress` is now exposed as a float value. `animateTo` and `snapTo` are internal. Use `expand()` and `collapse()` instead. `direction` and `overflow` have been removed. `offset` has been replaced with `requireOffset()`. [I323b4](https://android-review.googlesource.com/#/q/I323b4ebe42e5a3817f27759749d72ad222ac084b)
- Mark the `snapTo` function in Drawer as non-experimental API. ([Ib9c18](https://android-review.googlesource.com/#/q/Ib9c18103d5485a48177a9b57ce40b29656bb4cf1), [b/261425368](https://issuetracker.google.com/issues/261425368))
- Added a track color parameter for circular progress indicators, and a stroke cap parameter for both circular and linear progress indicators. ([Ie668c](https://android-review.googlesource.com/#/q/Ie668cc47ce9ce3aa688ad3c3ed9e9e15fdbda5e9), [b/216325962](https://issuetracker.google.com/issues/216325962), [b/222964817](https://issuetracker.google.com/issues/222964817))
- Renamed `ModalBottomSheetState`, `ModalBottomSheetState.Saver` and `rememberModalBottomSheetState`'s `confirmStateChange` to `confirmValueChange`. ([Ib48d1](https://android-review.googlesource.com/#/q/Ib48d1cbe2671647f5feda1fcde5dee9754c8caa0))
- Add `Modifier.minimumInteractiveComponentSize`. It can be used to reserve at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. ([I33f58](https://android-review.googlesource.com/#/q/I33f58e4c11cf74668e97167b91dad26b64ac554b), [b/258495559](https://issuetracker.google.com/issues/258495559))
- Incorporated changes in the Swipeable APIs in `ModalBottomSheetLayout`. `ModalBottomSheetState`'s animateTo does not take an `animationSpec` parameter anymore and the offset exposed is now nullable. Use `requireOffset` to require the offset. ([Ia2e79](https://android-review.googlesource.com/#/q/Ia2e79162058b143cc40ab6c4b1082126e147a7a2))
- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))
- Incorporated changes in the Swipeable APIs in `ModalDrawer. DrawerState`'s `animateTo` has been replaced by the open and close methods and the offset is now nullable. Use `requireOffset` to require the offset. ([I3de9e](https://android-review.googlesource.com/#/q/I3de9e361fdd8be7ee83c7946b809b5729d4ef2c4))
- Updated Drawers and Sheets to correctly delay presses in case gestures can become scroll events.
- Added `minLines` parameter into material and material3 Text, `TextField` and `OutlinedTextField` which allows setting the minimum height of the component in terms of number of lines ([I4af1d](https://android-review.googlesource.com/#/q/I4af1df6521acaa97edbed5048079b5e81b647dd8))

**Bug Fixes**

- Fixes an issue where `pullRefresh` was not consuming velocity, causing overscroll to show. Also changed the API signature of the `onRelease` lambda in `Modifier.pullRefresh` to return a Float for consumed velocity ([I7db65](https://android-review.googlesource.com/#/q/I7db6562a865f6ea870a57102f81d04e3d8289c0e), [b/266874741](https://issuetracker.google.com/issues/266874741))
- `BottomSheetState`, `ModalBottomSheetState` and `BottomDrawerState` now expose a progress property indicating the progress between the current (settled) anchor and the closest anchor in the swipe direction. ([I1b317](https://android-review.googlesource.com/#/q/I1b31727b4f56df890e336bea9f4de526733aaacc), [b/271169225](https://issuetracker.google.com/issues/271169225), [b/276375124](https://issuetracker.google.com/issues/276375124), [b/276776071](https://issuetracker.google.com/issues/276776071), [b/270066861](https://issuetracker.google.com/issues/270066861))
- Fixed the `AlertDialog` dismiss action to appear below the confirm action when the actions stacked over each other to fit into the dialog's width. This fix aligns the implementation with the Material Design spec. ([I029de](https://android-review.googlesource.com/#/q/I029ded5c6dd79f38b1a060afb3d24dcfb9cf119a), [b/235454277](https://issuetracker.google.com/issues/235454277))
- `BottomSheetScaffold` will not participate in nested scroll anymore when `gesturesEnabled` is set to false. ([I634f3](https://android-review.googlesource.com/#/q/I634f33bf0d7e6b4dea5d2225c8e7561b74a42d40), [b/215403277](https://issuetracker.google.com/issues/215403277))
- Fixed a bug where `BottomSheetScaffold` would crash when provided with empty content for slots. ([Ib24a5](https://android-review.googlesource.com/#/q/Ib24a55cf43d4e887f7742691e522d7fc843ce89c), [b/235588730](https://issuetracker.google.com/issues/235588730))
- Fixes `PullRefreshIndicator` intercepting clicks/pointer events. ([2494256](https://android-review.googlesource.com/c/platform/frameworks/support/+/2494256), [b/271777421](https://issuetracker.google.com/issues/271777421))
- Fixed an issue where `ModalBottomSheetLayout` would crash in an edge case on orientation change. Layout animations (e.g. `Modifier.animateContentSize`) in/on the sheet content now work smoothly. ([I2f981](https://android-review.googlesource.com/#/q/I2f981d892f163254f0282d6874fb860aae5d0992), [b/266780234](https://issuetracker.google.com/issues/266780234))

### Version 1.5.0-rc01

July 26, 2023

`androidx.compose.material:material-*:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81e6706c269471032b283755131d2aa4e8821a89..e423b92ad8e8707ff4031626131f05e33979eac8/compose)

### Version 1.5.0-beta03

June 28, 2023

`androidx.compose.material:material-*:1.5.0-beta03` is released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..24dc7b0781cb908b2385ec207ca1b3a72cb90093/compose/material)

**Bug Fixes**

- `BottomSheetState`, `ModalBottomSheetState` and `BottomDrawerState` now expose a progress property indicating the progress between the current (settled) anchor and the closest anchor in the swipe direction. ([I1b317](https://android-review.googlesource.com/#/q/I1b31727b4f56df890e336bea9f4de526733aaacc), [b/271169225](https://issuetracker.google.com/issues/271169225), [b/276375124](https://issuetracker.google.com/issues/276375124), [b/276776071](https://issuetracker.google.com/issues/276776071), [b/270066861](https://issuetracker.google.com/issues/270066861))

### Version 1.5.0-beta02

June 7, 2023

`androidx.compose.material:material-*:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d26ca4055c940126ae1663ad0d54aafd23205ea4..df792c9ff86d87f538bab5d7f9dd9f56e2437b15/compose/material)

### Version 1.5.0-beta01

May 24, 2023

`androidx.compose.material:material-*:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..d26ca4055c940126ae1663ad0d54aafd23205ea4/compose/material)

**API Changes**

- `DrawerState`'s and `BottomDrawerState`'s offset are not nullable anymore. They instead return `Float.NaN` to indicate the absence of the offset. ([Ie9855](https://android-review.googlesource.com/#/q/Ie98555941822a1609a86926b57a156e671e16778))
- Added an option to pass in a `ScrollState` when constructing a `DropdownMenu` or an `ExposedDropdownMenu` for controlling the vertical scroll state of the displayed menu items. ([Idb009](https://android-review.googlesource.com/#/q/Idb0090cd1b9bb4853e448d82094156a8af39d65b), [b/185304441](https://issuetracker.google.com/issues/185304441))
- Add the support for enabling/disabling the gesture of `ModalBottomSheetLayout` so that user could configure this for more featured bottomsheet ([I40af0](https://android-review.googlesource.com/#/q/I40af0ce2206e5967b468c5545324c7a0e9c2e97c))
- Added a color parameter to `BasicText` to allow efficiently animating or setting text color. ([Iffd88](https://android-review.googlesource.com/#/q/Iffd88c4c2de7f6922add66b1fc46bdff8853c3f6), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Renaming the Semantics property `isContainer` to `isTraversalGroup` ([I121f6](https://android-review.googlesource.com/#/q/I121f64d7e7be332c41a1fbf10a70ef1ec14ce0dc))

**Bug Fixes**

- Fixed the `AlertDialog` dismiss action to appear below the confirm action when the actions stacked over each other to fit into the dialog's width. This fix align the implementation with the Material Design spec. ([I029de](https://android-review.googlesource.com/#/q/I029ded5c6dd79f38b1a060afb3d24dcfb9cf119a), [b/235454277](https://issuetracker.google.com/issues/235454277))

### Version 1.5.0-alpha04

May 10, 2023

`androidx.compose.material:material-*:1.5.0-alpha04` is released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/material)

**API Changes**

- We are moving the density dependency to the component level. This applies to the following components: `BottomDrawer`, `ModalBottomSheetLayout`, `BottomSheetScaffold`, `Switch`, `ModalDrawer`. Please use the new overload provided where density is a parameter. ([I8fbd8](https://android-review.googlesource.com/#/q/I8fbd8011386bbaa46e3a1492cbaa9766d8f24024))

### Version 1.5.0-alpha03

April 19, 2023

`androidx.compose.material:material-*:1.5.0-alpha03` is released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/compose/material)

**API Changes**

- Update `BottomDrawer` internals to use the new `SwipeableV2` APIs. Because of this `BottomDrawerState` will now only have APIS defined at the class level, it won't inherit methods/properties from `SwipeableState`. We're using composition with an internal `SwipeableV2State`. Offset is now a nullable floating point property, the current value and a swipe target value can still be accessed through currentValue and targetValue properties. The previous class level methods such as open/expand/close and properties such as `isOpen/isClosed` continue to be supported. ([Iad40c](https://android-review.googlesource.com/#/q/Iad40c08ca8f48afbc451191c788e80584e874b98), [b/178529942](https://issuetracker.google.com/issues/178529942), [b/220676296](https://issuetracker.google.com/issues/220676296))

**Bug Fixes**

- Updated internals of the Switch component. The switch will now preview the closest (target state) when dragging. ([Id90d4](https://android-review.googlesource.com/#/q/Id90d466b47eb7eb446ee96e234215f3b0d3e5706))
- Animated sheet content (e.g. `Modifier.animateContentSize` on sheet content) in `BottomSheetScaffold` has been optimized and now works smoothly. ([Ia913c](https://android-review.googlesource.com/#/q/Ia913cf9c75949c25a5cc1a6f6dc2b650c95793b9), [b/270518202](https://issuetracker.google.com/issues/270518202), [b/254446195](https://issuetracker.google.com/issues/254446195))
- `BottomSheetScaffold` will not participate in nested scroll anymore when `gesturesEnabled` is set to `false`. ([I634f3](https://android-review.googlesource.com/#/q/I634f33bf0d7e6b4dea5d2225c8e7561b74a42d40), [b/215403277](https://issuetracker.google.com/issues/215403277))

### Version 1.5.0-alpha02

April 5, 2023

`androidx.compose.material:material-*:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/material)

**Bug Fixes**

- Fixed a bug where `BottomSheetScaffold` would crash when provided with empty content for slots. ([Ib24a5](https://android-review.googlesource.com/#/q/Ib24a55cf43d4e887f7742691e522d7fc843ce89c), [b/235588730](https://issuetracker.google.com/issues/235588730))
- Fixes `PullRefreshIndicator` intercepting clicks / pointer events ([2494256](https://android-review.googlesource.com/c/platform/frameworks/support/+/2494256), [b/271777421](https://issuetracker.google.com/issues/271777421))

### Version 1.5.0-alpha01

March 22, 2023

`androidx.compose.material:material-*:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce5f1f96b304c7952d07c5bb472112c4b0ee2312..5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/material)

**Bug Fixes**

- Add a chipgroup reflow sample. Update the horizontal padding in between child chips in the single line chipgroup sample to match spec. ([I3b155](https://android-review.googlesource.com/#/q/I3b15551ade23831d2099ccdbcc0217cfc81c3eb4))
- Fixed an issue where `ModalBottomSheetLayout` would crash in an edge case on orientation change. Layout animations (e.g. `Modifier.animateContentSize`) in/on the sheet content now work smoothly. ([I2f981](https://android-review.googlesource.com/#/q/I2f981d892f163254f0282d6874fb860aae5d0992), [b/266780234](https://issuetracker.google.com/issues/266780234))

## Version 1.4

### Version 1.4.3

May 3, 2023

`androidx.compose.material:material-*:1.4.3` is released with no changes (only a version bump).

### Version 1.4.2

April 19, 2023

`androidx.compose.material:material-*:1.4.2` is released. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5..0872f930da585f7fbf6e17c74b1dc42045e8b2c6/compose/material)

### Version 1.4.1

April 5, 2023

`androidx.compose.material:material-*:1.4.1` is released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c13b30cf6683e0a43585416f30b55e07bf2b560e..5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5/compose/material)

### Version 1.4.0

March 22, 2023

`androidx.compose.material:material-*:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce5f1f96b304c7952d07c5bb472112c4b0ee2312..c5b142d6ab0494c996b2378d5008ac1cd6da75f3/compose/material)

**Important changes since 1.3.0**

**API Changes**

- Add `Modifier.minimumInteractiveComponentSize`. It can be used to reserve at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. ([I33f58](https://android-review.googlesource.com/#/q/I33f58e4c11cf74668e97167b91dad26b64ac554b), [b/258495559](https://issuetracker.google.com/issues/258495559))
- Incorporated changes in the Swipeable APIs in `ModalDrawer`. `DrawerState`'s `animateTo` has been replaced by the open and close methods and the offset is now nullable. Use `requireOffset` to require the offset. ([I3de9e](https://android-review.googlesource.com/#/q/I3de9e361fdd8be7ee83c7946b809b5729d4ef2c4))
- Added `minLines` parameter into material and material3 Text, `TextField` and `OutlinedTextField` which allows setting the minimum height of the component in terms of number of lines ([I4af1d](https://android-review.googlesource.com/#/q/I4af1df6521acaa97edbed5048079b5e81b647dd8))
- Added `minLines` parameter to the `BasicText` and `BasicTextField`. It allows to set the minimum height of these composables in terms of number of lines ([I24294](https://android-review.googlesource.com/#/q/I2429479960eef317f467fa054b979c12fd73689d), [b/122476634](https://issuetracker.google.com/issues/122476634))

### Version 1.4.0-rc01

March 8, 2023

`androidx.compose.material:material-*:1.4.0-rc01` is released with no changes. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..6022301db806601f282c53b8cbb5a981923a1589/compose/material)

### Version 1.4.0-beta02

February 22, 2023

`androidx.compose.material:material-*:1.4.0-beta02` is released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/material)

**API Changes**

- Incorporated changes in the Swipeable APIs in `BottomSheetScaffold`. `BottomSheetState`'s `confirmStateChange` param has been renamed to `confirmValueChange`. `progress` is now exposed as a float value. `animateTo` and `snapTo` are internal. Use `expand()` and `collapse()` instead. `direction` and `overflow` have been removed. `offset` has been replaced with `requireOffset()`. ([I323b4](https://android-review.googlesource.com/#/q/I323b4ebe42e5a3817f27759749d72ad222ac084b))

**Bug Fixes**

- Removed semantic roles from clickable and selectable surfaces, updated components that used them to set roles using modifier.semantics ([Ibb4ba](https://android-review.googlesource.com/#/q/Ibb4ba779b94c5bd69728d09b0318072eef8a6a99))
- Minor update to the extended Material icons that tweaks the filled `desktop_mac`, `directions`, and `kitchen` icons. ([I65f5e](https://android-review.googlesource.com/#/q/I65f5e9e1dd6efaa53ebbfc80ac6d8ec923ddb174))

### Version 1.4.0-beta01

February 8, 2023

`androidx.compose.material:material-*:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/material)

**API Changes**

- Fixes an issue where `pullRefresh` was not consuming velocity, causing overscroll to show. Also changed the API signature of the `onRelease` lambda in `Modifier.pullRefresh` to return a Float for consumed velocity ([I7db65](https://android-review.googlesource.com/#/q/I7db6562a865f6ea870a57102f81d04e3d8289c0e), [b/266874741](https://issuetracker.google.com/issues/266874741))
- Restored property getter `LocalMinimuTouchTargetEnforcement` and mark it as deprecated and redirect to `LocalMinimumInteractiveComponentEnforcement`. ([I60dd5](https://android-review.googlesource.com/#/q/I60dd5ceb7c5703c8ba68f1b7d4a4a883b3f961a8))

### Version 1.4.0-alpha05

January 25, 2023

`androidx.compose.material:material-*:1.4.0-alpha05` is released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d74a1c966cd7ab8285c91c7c566827dc9f6de840..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/material)

**Bug Fixes**

- Fixed an issue where `ModalBottomSheetLayout's HalfExpanded` state was calculated incorrectly and the sheet would appear to be floating. ([I8c615](https://android-review.googlesource.com/#/q/I8c6155884780f8480fe714ee886d17e28bd21427), [b/265610459](https://issuetracker.google.com/issues/265610459))
- Fixed a bug in `ModalBottomSheetLayout` where the sheet would crash when going from the hidden to a visible state in some circumstances. ([Ia9265](https://android-review.googlesource.com/#/q/Ia926514a65dc4d2c44781e132f8faae7e442cf68), [b/265444789](https://issuetracker.google.com/issues/265444789))

### Version 1.4.0-alpha04

January 11, 2023

`androidx.compose.material:material-*:1.4.0-alpha04` is released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/material)

**API Changes**

- Added in `IsContainer` semantics property on Surfaces. This property will be used in a later change that determines traversal order based on the semantic meaning of elements such as surfaces. ([I63379](https://android-review.googlesource.com/#/q/I63379fde102abbee7d5464c50b1c86a59e01e768))
- Mark the `snapTo` function in Drawer as non-experimental API. ([Ib9c18](https://android-review.googlesource.com/#/q/Ib9c18103d5485a48177a9b57ce40b29656bb4cf1), [b/261425368](https://issuetracker.google.com/issues/261425368))
- Added a track color parameter for circular progress indicators, and a stroke cap parameter for both circular and linear progress indicators. ([Ie668c](https://android-review.googlesource.com/#/q/Ie668cc47ce9ce3aa688ad3c3ed9e9e15fdbda5e9), [b/216325962](https://issuetracker.google.com/issues/216325962), [b/222964817](https://issuetracker.google.com/issues/222964817))
- Renamed `ModalBottomSheetState`, `ModalBottomSheetState.Saver` and `rememberModalBottomSheetState`'s `confirmStateChange` to `confirmValueChange`. ([Ib48d1](https://android-review.googlesource.com/#/q/Ib48d1cbe2671647f5feda1fcde5dee9754c8caa0))
- More return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Add `Modifier.minimumInteractiveComponentSize`. It can be used to reserve at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. ([I33f58](https://android-review.googlesource.com/#/q/I33f58e4c11cf74668e97167b91dad26b64ac554b), [b/258495559](https://issuetracker.google.com/issues/258495559))
- Incorporated changes in the Swipeable APIs in `ModalBottomSheetLayout`. `ModalBottomSheetState`'s `animateTo` does not take an `animationSpec` parameter anymore and the `offset` exposed is now nullable. Use `requireOffset` to require the `offset`. ([Ia2e79](https://android-review.googlesource.com/#/q/Ia2e79162058b143cc40ab6c4b1082126e147a7a2))

**Bug Fixes**

- A `ModalBottomSheetLayout`'s sheet now has a maximum width of 640 dp. ([I71a4f](https://android-review.googlesource.com/#/q/I71a4f015f303a2d20c0e8bf5b54ded56533c9701), [b/234927577](https://issuetracker.google.com/issues/234927577))
- Fixes an issue where `rememberPullRefreshState` was not updating `refreshThreshold` and `refreshingOffset` over time. ([Ifed10](https://android-review.googlesource.com/#/q/Ifed10d3305317f3a46e7e700ce7759746e1cea0e), [b/263159832](https://issuetracker.google.com/issues/263159832))
- Progress for progress indicators is now properly bounded to its expected range. ([I8a7eb](https://android-review.googlesource.com/#/q/I8a7eb76931af76bac20dbd2879674a60c2899672), [b/262262727](https://issuetracker.google.com/issues/262262727))
- When `ModalBottomSheetState` has not received any anchors yet, it will update the `currentValue` without an animation when `snapTo` or `animateTo` are called instead of throwing an exception. ([I2c91b](https://android-review.googlesource.com/#/q/I2c91b5c454882c7288425921e13b20ba3a375351))
- Fixed the enabled state at the Material 2 `FilterChip` implementation. ([Id326a](https://android-review.googlesource.com/#/q/Id326a2a1749936c585011497bf5bcb3d21a05f9e), [b/261329817](https://issuetracker.google.com/issues/261329817))
- Fixed a bug where `ModalBottomSheetLayout` would crash if it was `HalfExpanded` when rotating from portrait to landscape. Please ensure you are passing in the correct `initialValue`, for example by checking the configuration. ([Ie8df7](https://android-review.googlesource.com/#/q/Ie8df79fae22ea27329024e0ea3b3f6a240151b87), [b/182882364](https://issuetracker.google.com/issues/182882364))
- Fixed an issue where `ModalBottomSheetLayout` would crash if the sheet content was empty. `ModalBottomSheetLayout` now allows empty sheet content. If the sheet content is empty, it will only have a Hidden state. ([Ic2288](https://android-review.googlesource.com/#/q/Ic2288017e3c5a80a0951cf136064cca5e2fab7cb), [b/200980998](https://issuetracker.google.com/issues/200980998), [b/216693030](https://issuetracker.google.com/issues/216693030))

**Known Issue**

- When updating from `androidx.compose.foundation:1.4.0-alpha03` to `androidx.compose.foundation:1.4.0-alpha04`, you might experience a `java.lang.NoSuchFieldError` error. [Here](https://issuetracker.google.com/issues/265172081) is where the issue was orginially reported. A fix has been submitted, and will be available on the next Compose update. As a work around, update your `androidx.compose.material` and `androidx.compose.material3` libraries to the latest version(1.1.0-alpha04) or downgrade your `androidx.compose.foundation` to 1.4.0-alpha03.

### Version 1.4.0-alpha03

December 7, 2022

`androidx.compose.material:material-*:1.4.0-alpha03` is released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/material)

**API Changes**

- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))
- Incorporated changes in the `Swipeable` APIs in `ModalDrawer`. `DrawerState`'s `animateTo` has been replaced by the `open` and `close` methods and the offset is now nullable. Use `requireOffset` to require the offset. ([I3de9e](https://android-review.googlesource.com/#/q/I3de9e361fdd8be7ee83c7946b809b5729d4ef2c4))
- Added an Modifier API to query ancestors scroll info. ([I2ba9d](https://android-review.googlesource.com/#/q/I2ba9d6d55f853e5d2775fe9a9f15e7a41d41e359), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Used in `Clickable` to correctly delay press interactions, when gestures could become scroll events.
- Fixed `Clickables` not correctly delaying ripples, when used inside an `Scrollable ViewGroup`.
- Updated Drawers and Sheets to correctly delay presses in case gestures can become scroll events.

**Bug Fixes**

- Fixed an issue where `PullRefreshIndicator` could get stuck after `onRefresh` is called, if the refreshing state was not changed to true. ([Ie2416](https://android-review.googlesource.com/#/q/Ie24160bf51bd010d165d75675cfb2c51f28dde04), [b/248274004](https://issuetracker.google.com/issues/248274004))

**Dependency Updates**

- Compose UI and Compose Material now depend on Lifecycle 2.5.1. ([I05ab0](https://android-review.googlesource.com/#/q/I05ab08e48f49eee1a1e573d172ba22efc47640a6), [b/258038814](https://issuetracker.google.com/issues/258038814))

### Version 1.4.0-alpha02

November 9, 2022

`androidx.compose.material:material-*:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/material)

**API Changes**

- `awaitFirstDown` and `waitForUpOrCancellation` now accept a `PointerEventPass` for greater flexibility. ([I7579a](https://android-review.googlesource.com/#/q/I7579a2dbb44c748a3fd3e515d2e7ab086aaff443), [b/212091796](https://issuetracker.google.com/issues/212091796))
- Added `minLines` parameter into material and material3 Text, `TextField` and `OutlinedTextField` which allows setting the minimum height of the component in terms of number of lines ([I4af1d](https://android-review.googlesource.com/#/q/I4af1df6521acaa97edbed5048079b5e81b647dd8))
- Added `minLines` parameter to the `BasicTex`t and `BasicTextField`. It allows to set the minimum height of these composables in terms of number of lines ([I24294](https://android-review.googlesource.com/#/q/I2429479960eef317f467fa054b979c12fd73689d), [b/122476634](https://issuetracker.google.com/issues/122476634))

### Version 1.4.0-alpha01

October 24, 2022

`androidx.compose.material:material-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..548c8ac2570ae6cf15798fea1380491f7d93796b/compose/material)

**API Changes**

- A new method, `awaitEachGesture()`, for gesture detectors was added. It operates similar to `forEachGesture()`, but the loop over gestures operates entirely within the `AwaitPointerEventScope` so events can't be lost between iterations.
- `forEachGesture()` has been deprecated in favor of `awaitEachGesture()` because it allows events to be lost between gestures. ([Iffc3f](https://android-review.googlesource.com/#/q/Iffc3fb8cf53d0e5eb9b529c023b3e2d29003e86f), [b/251260206](https://issuetracker.google.com/issues/251260206))

## Version 1.3

### Version 1.3.1

November 9, 2022

`androidx.compose.material:material-*:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/material)

### Version 1.3.0

October 24, 2022

`androidx.compose.material:material-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/material)

**Important changes since 1.2.0**

**Behavior breaking change**

- Maximum supported elevation in dialogs and popups has been reduced to 8dp.

**API Changes**

- Add a Pull-To-Refresh component to Compose ([I29168](https://android-review.googlesource.com/q/I29168f745898a795c46744b9773ae434fdcf7e7b)).
- Change parameter name from values to value in RangeSlider ([I3b79a](https://android-review.googlesource.com/q/I3b79aaaebf9b3080e9d775e10d287355c7d03ca5)).

### Version 1.3.0-rc01

October 5, 2022

`androidx.compose.material:material-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/material)

### Version 1.3.0-beta03

September 21, 2022

`androidx.compose.material:material-*:1.3.0-beta03` is released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/material)

**API Changes**

- Add a Pull-To-Refresh component to Compose ([I29168](https://android-review.googlesource.com/#/q/I29168f745898a795c46744b9773ae434fdcf7e7b))

### Version 1.3.0-beta02

September 7, 2022

`androidx.compose.material:material-*:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/material)

No changes since 1.3.0-beta01

### Version 1.3.0-beta01

August 24, 2022

`androidx.compose.material:material-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/material)

**Behavior breaking change**

Maximum supported elevation in dialogs and popups has been reduced to 8dp.

The maximum supported elevation for Compose dialogs and popups has been reduced from 30dp to 8dp. This change affects both material and ui custom dialogs and popups. This change is made to mitigate an accessibility bug on Android versions below S, and to ensure that accessibility services within those windows are able to interact with the content inside the dialog or popup.

You will only be impacted by this change if you are creating a custom dialog or popup implementation with an elevation set to levels higher than 8dp. Consider lowering the elevation of your dialog or popup. If you need to opt-out from this new behavior, consider forking your own dialog or popup with the desired elevation set. This is not recommended, as accessibility might be negatively impacted and it is on the developer to ensure the bottom part of the dialog or popup is interactable and readable by accessibility services.

### Version 1.3.0-alpha03

August 10, 2022

`androidx.compose.material:material-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/material)

### Version 1.3.0-alpha02

July 27, 2022

`androidx.compose.material:material-*:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/material)

**External Contribution**

- Fix `AnimatedVisibility` issue with `FloatingActionButton` in Scaffold ([I3a0ae](https://android-review.googlesource.com/#/q/I3a0aec281af02a829375aeb2ca4474cbf1eb05a5), [b/224005027](https://issuetracker.google.com/issues/224005027))

### Version 1.3.0-alpha01

June 29, 2022

`androidx.compose.material:material-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..8094b683499b4098092c01028b55a38b49e357f2/compose/material)

**API Changes**

- Change parameter name from values to value in `RangeSlider` ([I3b79a](https://android-review.googlesource.com/#/q/I3b79aaaebf9b3080e9d775e10d287355c7d03ca5))

**Bug Fixes**

- Update badge sample to provide more meaningful content description. ([I10b9d](https://android-review.googlesource.com/#/q/I10b9d99db01ac3844fa8b84b70aae231512e9d99))

## Version 1.2

### Version 1.2.1

August 10, 2022

`androidx.compose.material:material-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255/compose/material)

### Version 1.2.0

July 27, 2022

`androidx.compose.material:material-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ff668d1061ec9e732d65ec3bfa9dc3db50fd87a..1e0793130863c72dc4a2d02bc975128f3ef0158b/compose/material)

### Version 1.2.0-rc03

June 29, 2022

`androidx.compose.material:material-*:1.2.0-rc03` is released. [Version 1.2.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..e8af23f4f30713a3f6073d57558e7cde0f3056e9/compose/material)

- No changes since 1.2.0-rc02.

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.material:material-*:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/material)

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.material:material-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/material)

**API Changes**

- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))

**Bug Fixes**

- Updates badge with leading icon tab to affix badge to the label instead of the icon. ([I90993](https://android-review.googlesource.com/#/q/I90993b49d4804875e9e3dfe95b5ff715825063a5))

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.material:material-*:1.2.0-beta03` is released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/material)

**Bug Fixes**

- Fixed a bug where `BottomSheetScaffold` was drawing over the top app bar's shadow. `BottomSheetScaffold` now also takes the sheet's state into account when placing Snackbars: in the collapsed state, Snackbars are placed above the sheet and FAB; in the expanded state, Snackbars are anchored to the sheet's bottom. ([Ia80b5](https://android-review.googlesource.com/#/q/Ia80b5d1ebcd4c86431eab22a985ab2b1fa824843), [b/187771422](https://issuetracker.google.com/issues/187771422))

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.material:material-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/material)

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.material:material-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/material)

**New Features**

- This is the first beta release of 1.2!

**API Changes**

- Renamed `TextFieldDefaults.BorderStroke` composable that draws a border stroke in `OutlinedTextField` to `TextFieldDefaults.BorderBox`. ([I5f295](https://android-review.googlesource.com/#/q/I5f295062ff2a3ebc72115df2412062558d226273))

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.material:material-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/material)

**API Changes**

- Partial consumption (down OR position) has been deprecated in `PointerInputChange`. You can use `consume()` to consume the change completely. You can use `isConsumed` to determine whether or not someone else has previously consumed the change.
- `PointerInputChange::copy()` now always makes a shallow copy. It means that copies of `PointerInputChange` will be consumed once one of the copies is consumed. If you want to create an unbound `PointerInputChange`, use constructor instead. ([Ie6be4](https://android-review.googlesource.com/#/q/Ie6be471e6ed2a843e38712922c2231fdfd26213a), [b/225669674](https://issuetracker.google.com/issues/225669674))

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.material:material-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/material)

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.material:material-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/material)

**API Changes**

- Updates to the clickable Card API to follow changes at the Surface API ([I56bcb](https://android-review.googlesource.com/#/q/I56bcbaee18240026a37dbcd409d2cfd7b68be9a9))
- Updates to Material 2 Surface API that adds additional overloaded functions for selectable and toggleable Surfaces. ([Ifcca5](https://android-review.googlesource.com/#/q/Ifcca5da006887180e238eddda2bc42eb70a914ae))

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.material:material-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/material)

**API Changes**

- `LazyVerticalGrid` and `LazyHorizontalGrid` are now stable. ([I307c0](https://android-review.googlesource.com/#/q/I307c0ce412c7bc762e334e429013c0442bd22fde))
- `LazyVerticalGrid/LazyHorizontalGrid` and all related apis were moved into .grid subpackage. Please update your imports from androidx.compose.foundation.lazy to androidx.compose.foundation.lazy.grid. ([I2d446](https://android-review.googlesource.com/#/q/I2d446e0bed6f27f0394b7dcab1152301e3404b0f), [b/219942574](https://issuetracker.google.com/issues/219942574))
- Reverted previous change of relying solely on a View for `WindowInsetsControllerCompat`, and again require a Window which is required for managing some window flags. Deprecated `ViewCompat.getWindowInsetsController` in favor of `WindowCompat.getInsetsController` to ensure that the correct Window is used (such as if the View is in a dialog). ([I660ae](https://android-review.googlesource.com/#/q/I660aee32108b59516232b41e05b3f05ae2538554), [b/219572936](https://issuetracker.google.com/issues/219572936))
- Text:`includeFontPadding` is now turned off by default. The clipping issues as a result of `includeFontPadding=false` is handled and no clipping should occur for tall scripts. ([I31c84](https://android-review.googlesource.com/#/q/I31c84166ae5241fea3f49e8f293dd9d8a5d712cb), [b/171394808](https://issuetracker.google.com/issues/171394808))
- Added a new `LazyVerticalGrid` API to define cross axis sizes ([I17723](https://android-review.googlesource.com/#/q/I17723fdc6302a345dd643fb637e1644168a2a321))

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.material:material-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/material)

**API Changes**

- `Add support for filter chips` ([I39a6e](https://android-review.googlesource.com/#/q/I39a6e25725a71191a2e78c2162419935d487ac59), [b/192585545](https://issuetracker.google.com/issues/192585545))
- Added `TextFieldDecorationBox` and `OutlinedTextFieldDecorationBox`. Using them together with `BasicTextField` will help you build custom text field based on Material Design text fields but with more options for customisation.
- Provided a way to adjust horizontal and vertical paddings in text fields. ([I8c9f1](https://android-review.googlesource.com/#/q/I8c9f168a687e337670c266e1eb3e985da6aebdc3), [b/203764564](https://issuetracker.google.com/issues/203764564), [b/191543915](https://issuetracker.google.com/issues/191543915), [b/189971673](https://issuetracker.google.com/issues/189971673), [b/183136600](https://issuetracker.google.com/issues/183136600), [b/179882597](https://issuetracker.google.com/issues/179882597), [b/168003617](https://issuetracker.google.com/issues/168003617))
- Added `ComposableTarget`, `ComposableTargetMarker` and
  `ComposableOpenTarget` that allows compile time reporting of when
  a composable function is called targeting an applier it was not
  designed to use.

  In most cases the annotations can be inferred by the compose
  compiler plugin so using these annotation directly should be
  rare . The cases that cannot be inferred include creating and
  using a custom applier, abstract composable functions (such as
  interface methods), fields or global variables that are
  composable lambdas (local variables and parameters are inferred),
  or when using `ComposeNode` or a related composable functions.

  For custom appliers the composable functions that calls
  `ComposeNode` or `ReusableComposeNode` need to add a
  `CompoableTarget` annotation for the function and any
  composable lambda parameter types. It is recommended, however,
  to create an annotation that is annotated with
  `ComposableTargetMarker` and then the marked annotation be used
  instead of `ComposableTarget` directly. A composable annotation
  marked with `ComposableTargetMarker` is equivalent to a
  `ComposbleTarget` with the fully qualified name of the attribute
  class as the applier parameter. For an example of using
  `ComposableTargetMarker` see `anroidx.compose.ui.UiComposable`. ([I38f11](https://android-review.googlesource.com/#/q/I38f11b789291db89fc0bb92fc14ac5b3fcba0283))

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.material:material-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/material)

**Bug Fixes**

- Addes chip group sample ([I97080](https://android-review.googlesource.com/#/q/I970808fe62083adaee55806e1707b4919d17ec3c), [b/192585545](https://issuetracker.google.com/issues/192585545))

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.material:material-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/material)

**API Changes**

- Added `NonRestartableComposable` to methods that are overloads of existing methods without complex logic. This reduces compiler generated memoization checks (equals) for all parameters which are repeated in the inner function that is called. ([I90490](https://android-review.googlesource.com/#/q/I90490b1a28bada20840ab59e47245c00c6253d11))
- Add support for action chip ([I07100](https://android-review.googlesource.com/#/q/I07100d433428017c69701aa0dd6a1490e4ea3522), [b/192585545](https://issuetracker.google.com/issues/192585545))

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.material:material-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/material)

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

**External Contribution**

- `ModalBottomSheetState` now has a `isSkipHalfExpanded` flag. It can be either set through the constructor or updated later on by setting `ModalBottomSheetState`'s `isSkipHalfExpanded` property to `true`. Updating `isSkipHalfExpanded`'s value causes a recomposition of the sheet. ([I18b86](https://android-review.googlesource.com/#/q/I18b866d1895f53d46c5965867f628b5eca455fa4), [b/186669820](https://issuetracker.google.com/issues/186669820))

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.material:material-*:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/material)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.material:material-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/material)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
- Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of 48x48dp, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable Support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.material:material-*:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/material)

**Behaviour Changes**

Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) [touch target](https://material.io/design/usability/accessibility.html#layout-and-typography) size. For instance, Button touch target will expand to a minimum size of 48x48dp, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.

**Bug Fixes**

- Added some better debug information for the layout inspector when inspecting minimum touch target modifiers. ([aosp/1955036](https://android-review.googlesource.com/c/platform/frameworks/support/+/1955036/))

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.material:material-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/material)

**Bug Fixes**

- Fix the corner radius that is applied for `Checkbox`es ([I38b03](https://android-review.googlesource.com/#/q/I38b03cda11bf28245a3af3d726ddd0bb9cbe8fa6), [b/175198975](https://issuetracker.google.com/issues/175198975), [b/202309440](https://issuetracker.google.com/issues/202309440))

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.material:material-*:1.1.0-beta04` is released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/material)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.material:material-*:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/material)

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.material:material-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/material)

**Bug Fixes**

- Ripples and other indications will now only be delayed if they are inside a Modifier.scrollable() container, instead of always being delayed for a down event. ([Ibefe0](https://android-review.googlesource.com/#/q/Ibefe01bcdef89e01b6e9f7edf9fe13622450f487), [b/203141462](https://issuetracker.google.com/issues/203141462))

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.material:material-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/material)

**New Features**

- Ripples now support hover and focus states, so hovering / focusing a component such as Button will now show the correct state overlay.

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.material:material-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/material)

**API Changes**

- A child-less overload for Layout was added, with improved efficiency ([Ib0d9a](https://android-review.googlesource.com/#/q/Ib0d9a0f11936c0568d20e26a3c6eaa3f938e0ccd))
- Implementation of `ExposedDropdownMenu` based on `ExposedDropdownMenuBox` with `TextField` and `DropdownMenu` inside ([If60b2](https://android-review.googlesource.com/#/q/If60b2e6c7c139d4d4c134c714e2803f531a6c72a))
- `dismissOnOutsideClick` was added to `PopupProperties`, replacing `dismissOnClickOutside` which was deprecated. The new property receives the click position and the anchor bounds, providing finer control over whether onDismissRequest should be invoked or not. For example, this can be useful to prevent anchor dismissal for touches on the anchor.
  - `updateAndroidWindowManagerFlags` was added to `PopupProperties`, offering low-level control over the flags passed by the popup to the Android WindowManager. The parameter of the lambda will be the flags calculated from the PopupProperties values that result in WindowManager flags: e.g. focusable. The result of the lambda will be the final flags which will be passed to the Android WindowManager. By default, updateAndroidWindowManagerFlags will leave the flags calculated from parameters unchanged. This API should be used with caution, only in cases where the popup has very specific behavior requirements. ([I6e9f9](https://android-review.googlesource.com/#/q/I6e9f9d393dc12bd1ea7ae294af1761817f154735))

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.material:material-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/material)

**API Changes**

- Adds minimum touch target sizing for Material components that do not have an accessible touch target. As this adds extra spacing around components to make sure they have a large enough touch target, this may change existing UIs that assume the size of these components is their visual size, and doesn't account for touch target size. You can use the experimental `LocalMinimumTouchTargetEnforcement` composition local to disable this behavior across a hierarchy, but this is intended only to be a temporary escape hatch while updating existing UIs to account for the new minimum size. ([I9b966](https://android-review.googlesource.com/#/q/I9b966a79a290538d8d450aa732b5092760cbece4), [b/149691127](https://issuetracker.google.com/issues/149691127), [b/171509422](https://issuetracker.google.com/issues/171509422))
- Added experimental TextFieldColorsWithIcons interface, extending TextFieldColors to provide InteractionSource to the leadingColor and trailingColor. This enables modifying the appearance of TextField according to the focus state. ([I66923](https://android-review.googlesource.com/#/q/I6692391098f7840a491bd175da2dfde116718bbc), [b/198402662](https://issuetracker.google.com/issues/198402662))

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.material:material-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/material)

**API Changes**

- Deprecated `performGesture` and `GestureScope`, which have been replaced by `performTouchInput` and `TouchInjectionScope`. ([Ia5f3f](https://android-review.googlesource.com/#/q/Ia5f3f740c51a1add60fa82189d583d8a5192dd31), [b/190493367](https://issuetracker.google.com/issues/190493367))
- Added `touchBoundsInRoot` to `SemanticsNode` that includes the minimum touch target size so that developers can ensure that touch targets meet accessibility minimums. ([I2e14b](https://android-review.googlesource.com/#/q/I2e14bf1bab7a745aa2421353f44c734540d2489c), [b/197751214](https://issuetracker.google.com/issues/197751214))

**Bug Fixes**

- Allow clip to extend touch target bounds beyond the clip region for minimum touch target purposes. ([I43e10](https://android-review.googlesource.com/#/q/I43e10218f7a20b5a8190ea838cef8eb8440928d1), [b/171509422](https://issuetracker.google.com/issues/171509422))
- Updated `Divider` composable to respect `Dp.Hairline` for the thickness parameter to support drawing single pixel dividers regardless of display density. ([I16ffb](https://android-review.googlesource.com/#/q/I16ffb642eda86c17b65f56249686ffe67082ffe5), [b/196840810](https://issuetracker.google.com/issues/196840810))

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.material:material-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/material)

**New Features**

- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

**API Changes**

- Added test method to get the clipped bounds. ([I6b28e](https://android-review.googlesource.com/#/q/I6b28e437d6893a63be65c8a451a84bcb21bce906))
- Added minimum touch target size to ViewConfiguration for use in semantics and pointer input to ensure accessibility. ([Ie861c](https://android-review.googlesource.com/#/q/Ie861ca1fcdbfcc9455352fc3a459d5734d5d57cc))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.material:material-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/material)

**External Contribution**

- Fix the behavior of SwipeableState in the case where the swipe offset is within a rounding error of an anchor. ([I03d39](https://android-review.googlesource.com/#/q/I03d39d25bc376314d7197484c2a707498296aa97), [b/191993377](https://issuetracker.google.com/issues/191993377))

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.material:material-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/material)

**API Changes**

- Updated `DrawScope#drawImage` method that consumes source and destination rects to consume an optional FilterQuality parameter. This is useful for pixel art that is intended to be pixelated when scaled up for pixel based art. Updated BitmapPainter + Image composable to also consume an optional FilterQuality parameter ([Ie4fb0](https://android-review.googlesource.com/#/q/Ie4fb04013701add0fba1c5c6bb9da2812d6436e7), [b/180311607](https://issuetracker.google.com/issues/180311607))
- Renamed BadgeBox to BadgedBox, changed parameters to accept Badge composable. Added Badge component that is the typical badge content for a BadgedBox. ([I639c6](https://android-review.googlesource.com/#/q/I639c692b5fe86e8aabfb01df2020114ea13b4912))
- Added NavigationRail component, see the docs and samples for usage information ([I8de77](https://android-review.googlesource.com/#/q/I8de77279455344ff38bd4d04ba3c30e3c0dda0fb))

**Bug Fixes**

- Added a bottom-aligned NavigationRail sample and Catalog app demo. ([I3cffc](https://android-review.googlesource.com/#/q/I3cffc68a7a8d6591f2d59bb407f23b1ebe43361b))
- Dialogs now follow the platform sizing behaviour. Set usePlatformDefaultWidth to false to override this behaviour. ([Iffaed](https://android-review.googlesource.com/#/q/Iffaedb8890f59627a58fb4f33d06044ac120fd7d), [b/192682388](https://issuetracker.google.com/issues/192682388))
- Added navigation-rail demo to the catalog app. ([I04960](https://android-review.googlesource.com/#/q/I0496024f7358b4accbb5e62e3198a6ead14c685e))
- Added badge demo to the catalog app. ([If285d](https://android-review.googlesource.com/#/q/If285dd945a8e32efeb6ba912eb6bc535554ca140))

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.material:material-*:1.0.5` is released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/material)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.material:material-*:1.0.4` is released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/material)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.material:material-*:1.0.3` is released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/material)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.material:material-*:1.0.2` is released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/material)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.material:material-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/material)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.material:material-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/material)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

**Known Issues**

- If you are using Android Studio Bumblebee Canary 4 or AGP `7.1.0-alpha04`/`7.1.0-alpha05`, you may hit the following crash:

        java.lang.AbstractMethodError: abstract method "void androidx.lifecycle.DefaultLifecycleObserver.onCreate(androidx.lifecycle.LifecycleOwner)"

  To fix, temporarily increase your minSdkVersion to 24+ in your `build.gradle` file. This issue will be fixed in the next version of Android Studio Bumblebee and AGP `7.1`. ([b/194289155](https://issuetracker.google.com/issues/194289155))

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.material:material-*:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/material)

**Bug Fixes**

- Dialogs now follow the platform sizing behaviour. Set `usePlatformDefaultWidth` to false to override this behaviour. ([Iffaed](https://android-review.googlesource.com/#/q/Iffaedb8890f59627a58fb4f33d06044ac120fd7d), [b/192682388](https://issuetracker.google.com/issues/192682388))

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.material:material-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/material)

**API Changes**

- Added `BadgeBox` component, see the docs and samples for usage information ([I5e284](https://android-review.googlesource.com/#/q/I5e284595a47007d7f6df22963db95843e961182c))
- `useDefaultMaxWidth` in `PopupProperties` was renamed to `usePlatformDefaultWidth`. ([I05710](https://android-review.googlesource.com/#/q/I0571008fba7541d07511b95f31e1854849f36124))
- Dialogs are now able to use the entire screen width. ([I83929](https://android-review.googlesource.com/#/q/I83929941b29e5afe443b7472ff36e46b1ccc8108), [b/190810877](https://issuetracker.google.com/issues/190810877))
- Added Experimental Range Slider implementation ([I2f4b3](https://android-review.googlesource.com/#/q/I2f4b3f3f00b2d65189a8a2523a2227bacd6ae6c0))

**Bug Fixes**

- To align with Material Design specs OutlinedTextField with invalid input stopped using error color for label when label is being used as a placeholder. The latter is true when there is no input text in the text field and the text field is not in focus. With that change the meaning of the `error:Boolean` parameter in `TextFieldColors.labelColor()` function also changed: it will now return `false` even when the input is invalid if the label is being used as a placeholder. ([I45f78](https://android-review.googlesource.com/#/q/I45f78ef50d31f11ef1776a5a0ed89eb1fac62f93))

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.material:material-*:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/material)

**API Changes**

- Added Shape parameter to OutlinedTextField to be able to customize the shape of the border ([I8f39e](https://android-review.googlesource.com/#/q/I8f39edee8f5c4860336d9b26772403f680b4afff), [b/181322957](https://issuetracker.google.com/issues/181322957))
- TextOverflow is changed to an inline class. ([I433af](https://android-review.googlesource.com/#/q/I433af65606ae4e79ea0cb281be7049c73b12fcf0))

**Bug Fixes**

- Scrim in BottomDrawer, BackdropScaffold and ModalBottomSheetLayout will disappear then the Color.Unspecified is passed ([I2d899](https://android-review.googlesource.com/#/q/I2d8999e16e2b4b3942e4fd9df424c5d6446e5a2b), [b/182063309](https://issuetracker.google.com/issues/182063309))

**Added Profile Rules**

This release adds profile rules to the following compose modules ([I14ed6](https://android-review.googlesource.com/#/q/I14ed64578d535320a40ed8d486f75715641b2762)):

- androidx.compose.animation
- androidx.compose.animation-core
- androidx.compose.foundation
- androidx.compose.foundation-layout
- androidx.compose.material
- androidx.compose.material-ripple
- androidx.compose.runtime
- androidx.compose.ui
- androidx.compose.ui.geometry
- androidx.compose.ui.graphics
- androidx.compose.ui.text
- androidx.compose.ui.text
- androidx.compose.ui.unit
- androidx.compose.ui.util

#### What are profile rules?

- Profile rules for a library are specified in a text file `baseline-prof.txt` located in the `src/main` or equivalent directory. The file specifies a rule per line, where a rule in this case is a pattern for matching to methods or classes in the library. The syntax for these rules is a superset of the human-readable ART profile format that is used when using `adb shell profman --dump-classes-and-methods ...`. These rules take one of two forms to target either methods or classes.

- A method rule will have the following pattern:

      <FLAGS><CLASS_DESCRIPTOR>-><METHOD_SIGNATURE>

- And a class rule will have the following pattern:

      <CLASS_DESCRIPTOR>

- Here `<FLAGS>` is one or more of the characters `H`, `S`, and `P` to indicate whether or not this method should be flagged as "Hot", "Startup", or "Post Startup".

- The `<CLASS_DESCRIPTOR>` is the descriptor for the class that the targeted method belongs to. For example, the class `androidx.compose.runtime.SlotTable` would have a descriptor of `Landroidx/compose/runtime/SlotTable;`.

- The `<METHOD_SIGNATURE>` is the signature of the method, and includes the name, parameter types, and return types of the method. For example, the method `fun isPlaced(): Boolean` on `LayoutNode` has the signature `isPlaced()Z`.

- These patterns can have wildcards (`**`, `*`, and `?`) in order to have a single rule encompass multiple methods or classes.

#### What do the rules do?

- A method that has the flag `H` indicates that this method is a "hot" method, and should be compiled ahead of time.

- A method that has the flag `S` indicates that it is a method which is called at startup, and should be compiled ahead of time to avoid the cost of compilation and interpreting the method at startup time.

- A method that has the flag `P` indicates that it is a method which is called after startup.

- A class that is present in this file indicates that it is used during startup and should be pre-allocated in the heap to avoid the cost of class loading.

#### How does this work?

- Libraries can define these rules which will be packaged in AAR artifacts. When an APK is then built which includes these artifacts, these rules are merged together and the merged rules are used to build a compact binary ART profile that is specific to the APK. ART can then leverage this profile when the APK is installed on devices in order to ahead-of-time compile a specific subset of the application to improve the performance of the application, especially the first run. Note that this will have no effect on debuggable applications.

### Version 1.0.0-beta08

June 2, 2021

`androidx.compose.material:material-*:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/material)

**New Features**

**Behavior Breaking API Change**

- BEHAVIOUR-BREAKING: Card now consumes clicks, making clicks added via `Card(Modifier.clickable)` to be a no-op. Please, use new experimental overload of a Card that accepts onClick. ([Ia8744](https://android-review.googlesource.com/#/q/Ia8744f372b7ecafd4e92d0fc58245ebc0972b18d), [b/183775620](https://issuetracker.google.com/issues/183775620))
  - Added a new Card overload that handles clicks as well as other clickable functionality: indication, interactionSource, enabled/disabled. It wasn't possible to use a regular non-clickable Card with the `Modifier.clickable` because the Card will not clip the ripple indication in those cases.
- BEHAVIOUR-BREAKING: Surface now consumes clicks, making clicks added via `Surface(Modifier.clickable)` to be a no-op. Please, use new experimental overload of Surface that accepts onClick. ([I73e6c](https://android-review.googlesource.com/#/q/I73e6c76ed6389040d824a5dcc82dc84dc4fea0c7), [b/183775620](https://issuetracker.google.com/issues/183775620))
  - Added a new Surface overload that handles clicks as well as other clickable functionality: indication, interactionSource, enabled/disabled. It wasn't possible to use a regular non-clickable Surface with the `Modifier.clickable` because the Surface will not clip the ripple indication in those cases.

**API Changes**

- `FabPosition` was converted to inline class from enum to support potential expansion in the future ([I030fb](https://android-review.googlesource.com/#/q/I030fbbd31d4406985cca383e355f6973eee2861b))
- Refactored enum usages to inline classes to avoid issues with exhaustive when statements when new enum values are added. ([I2b5eb](https://android-review.googlesource.com/#/q/I2b5eb2f04d64d1eccf38557d80e3eef06869c310))
- Adds a tap timeout to clickable / toggleable to prevent showing a ripple during a scroll / drag ([Ia2704](https://android-review.googlesource.com/#/q/Ia27044999597dd9411344119a7b77180943d9a25), [b/168524931](https://issuetracker.google.com/issues/168524931))
- ContentDescription and Text semantics properties are no longer single values but lists. This enables to merge them as they are instead of concatenations. Also provided better testing APIs to utilize these changes ([Ica6bf](https://android-review.googlesource.com/#/q/Ica6bf4236d05b97357c18fb306a6305877a349f7), [b/184825850](https://issuetracker.google.com/issues/184825850))
- `Modifier.focusModifier()` is deprecated and replaced by `Modifier.focusTarget()` ([I6c860](https://android-review.googlesource.com/#/q/I6c860991217cc0c4e7cb35be73207f94669ce607))
- Replaced `FocusState` enum with a `FocusState` interface ([Iccc1a](https://android-review.googlesource.com/#/q/Iccc1a7306fe886969b3a5c74359f53250b3901d9), [b/187055290](https://issuetracker.google.com/issues/187055290))
- Removed `LocalRippleNativeRendering` now that the View-backed ripple implementation is stable ([I7fab3](https://android-review.googlesource.com/#/q/I7fab3b12f34b82741c562ae8af3b2d08fbbb47c7), [b/188569367](https://issuetracker.google.com/issues/188569367))

**Bug Fixes**

- `Modifier.onGloballyPositioned()` was changed to report the coordinates of this modifier in the modifier chain, not the layout coordinates after applying all the modifiers. This means that now the ordering of modifiers is affecting what coordinates would be reported. ([Ieb67d](https://android-review.googlesource.com/#/q/Ieb67da0c327c9dc323a4b0a8bf33dbb66f0611e3), [b/177926591](https://issuetracker.google.com/issues/177926591))
- Added a README for the existing Compose Material catalog. ([If9191](https://android-review.googlesource.com/#/q/If9191a89b99bea722566a18e0d2878aa71b79ac6))

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.material:material-*:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/material)

> [!NOTE]
> **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
> `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

**API Changes**

- You no longer need to use extension methods for route support in Navigation Compose. ([I22beb](https://android-review.googlesource.com/#/q/I22beb923cccecdc76c555abc7921ab3d9efc860d), [b/172823546](https://issuetracker.google.com/issues/172823546))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.material:material-*:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/material)

**API Changes**

- Ripple has been migrated to use `RippleDrawable` internally on Android devices. This means that ripple animations will happen on the RenderThread, and so will be smooth even when the UI thread is under load, such as when navigating between screens. This does not change the API surface of ripple, but there may be behavior changes introduced as a result of this change. To aid the migration, `LocalRippleNativeRendering` has been added - provide a value of `false` to this CompositionLocal to fall back to the previous ripple implementation inside the CompositionLocalProvider. This API is temporary and will be removed in the future, so if you run into issues that cause you to use this API, please [file a bug](https://issuetracker.google.com/issues/new?component=612128). ([I902f8](https://android-review.googlesource.com/#/q/I902f8eecaa8e3f55eb4c1bebc86f4f50e2967d0c), [b/168777351](https://issuetracker.google.com/issues/168777351), [b/183019123](https://issuetracker.google.com/issues/183019123))
- Added CollectionInfo and CollectionItemInfo accessibility APIs that allows to mark collection and its items for accessibility services ([Id54ef](https://android-review.googlesource.com/#/q/Id54ef37379e14e41ac52782b40e29de54f95eed0), [b/180479017](https://issuetracker.google.com/issues/180479017))
- Added accessibility API `error` that allows to mark a node that contains invalid input ([I12997](https://android-review.googlesource.com/#/q/I129977e3d3b5f03435de41de409fde9029c325b9), [b/180584804](https://issuetracker.google.com/issues/180584804), [b/182142737](https://issuetracker.google.com/issues/182142737))

**Bug Fixes**

- Updated Compose Material catalog insets implementation from: https://github.com/google/accompanist/pull/365. ([I25dc3](https://android-review.googlesource.com/#/q/I25dc3d73bdf3245036a6299efe11f9c7a2de14df))
- Row \& Column children with weight(fill = false) are no longer making the parent fill the entire available main axis space. ([Ied94d](https://android-review.googlesource.com/#/q/Ied94da682f4cf6ead5b91e06ba08904c1a349b9f), [b/186012444](https://issuetracker.google.com/issues/186012444), [b/184355105](https://issuetracker.google.com/issues/184355105))

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.material:material-*:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/compose/material)

**Bug Fixes**

- Added component tile images, theme picker, and more specific menu URLs to existing Compose Material catalog. ([I9b58e](https://android-review.googlesource.com/#/q/I9b58e64b0bfeaa3a177131261e50e253b801586a))

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.material:material-*:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/material)

**API Changes**

- API CHANGE: `DrawerState` state is no longer extends experimental SwipeableState.
  - API CHANGE: `BottomDrawerState` is now marked as Experimental, to match already Experimental BottomDrawer component ([I81114](https://android-review.googlesource.com/#/q/I81114f9ba3762dfa162368be2b812b24d1d788e3), [b/181656094](https://issuetracker.google.com/issues/181656094))
- Rename `hideSoftwareKeyboard` and `showSoftwareKeyboard` on `SoftwareKeyboardController` to `hide()` and `show()` respectively.
  - Provide the full CompositionLocal interface for LocalSoftwareKeyboardController, allowing it to be set (especially useful in tests) ([I579a6](https://android-review.googlesource.com/#/q/I579a6e311d1cc96e4ea398465cad3a402a633b8d))
- LiveRegion accessibility API is added. If node is marked as a live region, the accessibility services will automatically notify the user about its changes ([Idcf6f](https://android-review.googlesource.com/#/q/Idcf6f425b12b005e59ad77fe7430e466132ea87c), [b/172590946](https://issuetracker.google.com/issues/172590946))

**Bug Fixes**

- Added implementation of Compose Material catalog to existing module. Currently missing: component tile images, theme picker (to be added in follow-up changes). ([Ie7a94](https://android-review.googlesource.com/#/q/Ie7a947b589a9b229b9a1f3e10ef91cee950029ac))

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.material:material-*:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/material)

**API Changes**

- `DefaultMonotonicFrameClock` is deprecated. Calling `withFrameNanos` or `Recomposer.runRecomposeAndApplyChanges` with no `MonotonicFrameClock` will now throw `IllegalStateException`. ([I4eb0d](https://android-review.googlesource.com/#/q/I4eb0d7a8ebae7497735d25bc35e9f94c66ce2232))
- Added a new API `LeadingIconTab` to support displaying an icon and inline text in a tab. ([I23267](https://android-review.googlesource.com/#/q/I2326771eb8d8f8716a8a13bdd8b6e6682912be35))

**External Contribution**

- \[by Jossi Wolf\] `BottomDrawer` now wraps the content of the drawer slot. `BottomDrawer` doesn't throw an `IllegalStateException` when the parent has infinite height. The bottom drawer will now open to an expanded state if it is smaller than 50% of its parent. Docs around `BottomDrawerState` and `ModalBottomSheetLayoutState` have been updated. `BottomDrawerState#isOpen` returns true now if it is in either open or expanded state. ([I87241](https://android-review.googlesource.com/#/q/I8724160d0a593e4f8611f33a7da231b9450debba))

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.material:material-*:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/material)

**API Changes**

- Added new `LocalSoftwareKeyboardController` composition local API to replace previous `SoftwareKeyboardController` interface on TextField. ([I5951e](https://android-review.googlesource.com/#/q/I5951e802fbec7c26862b976de64b78640accd1f7), [b/168778053](https://issuetracker.google.com/issues/168778053))

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))
- Changed the default horizontal alignment for TopAppBar and BottomAppBar to Start, consistent with Row ([Ib2dc7](https://android-review.googlesource.com/#/q/Ib2dc7beec6fbf4ef1a9762414ee4d50f0113b850))
- Added a new module and placeholder UI for a Compose Material catalog, currently nested in existing integration test demos. ([Idfcb3](https://android-review.googlesource.com/#/q/Idfcb3d3bd4b5934ae33855e83c61d150853c928b))
- `androidx.compose.ui:ui` no longer depends on AppCompat or Fragment. If you are using a ComposeView in your application, and you are using Fragment and/or AppCompat, make sure that you are using AppCompat 1.3+ / Fragment 1.3+ - these versions are needed to correctly set lifecycle and saved state owners required for ComposeView. ([I1d6fa](https://android-review.googlesource.com/#/q/I1d6fa61deebc7771082d19a8268bd37b5f99194d), [b/161814404](https://issuetracker.google.com/issues/161814404))

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.material:material-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/material)

This is the first release of Compose 1.0.0 Beta.

**API Changes**

- Size modifiers were renamed. Modifier.width/height/size were renamed to requiredWidth/requiredHeight/requiredSize. Modifier.preferredWidth/preferredHeight/preferredSize were renamed to width/height/size. ([I5b414](https://android-review.googlesource.com/#/q/I5b4145953d360b1fb851c0056fc9a7875bb34088))
- imageResource and vectorResource are now extension functions on ImageBitmap and ImageVector companions respectively. load{Image,Vector,Font}Resource functions have been deleted. ([I89130](https://android-review.googlesource.com/#/q/I89130cd429dfcbe54995d667d3501e3363851bce))
- Modifiers for sizing to intrinsics are no longer experimental. ([I15744](https://android-review.googlesource.com/#/q/I15744bc96d9c9a94747901e47100fdea25e28742))
- Removed dp assertions ([I798d2](https://android-review.googlesource.com/#/q/I798d2f7dbd5e687d8e1fb059f153cdc8150d8d27))
- Removed SoftwareKeyboardController callback from all text fields to be replaced by a new API shortly. ([Iae869](https://android-review.googlesource.com/#/q/Iae869e91c48300f4ab926dac2578d2d759f5fd89), [b/168778053](https://issuetracker.google.com/issues/168778053))
- Switch, Checkbox and RadioButton action lambdas are now nullable. Checkbox-in-clickable-row samples updated to use this feature. ([If601b](https://android-review.googlesource.com/#/q/If601b88cf4622111bca5f4927cbb86c7d300ebbf), [b/171819073](https://issuetracker.google.com/issues/171819073))
- `InteractionState` has been replaced with `[Mutable]InteractionSource`
  - Interfaces are responsible for emitting / collecting Interaction events.
  - Instead of passing `interactionState = remember { InteractionState() }` to components such as `Button` and `Modifier.clickable()`, use `interactionSource = remember { MutableInteractionSource() }`.
  - Instead of: `Interaction.Pressed in interactionState` you should instead use the extension functions on InteractionSource, such as InteractionSource.collectIsPressedAsState().
  - For complex use cases you can use InteractionSource.interactions to observe the stream of Interactions. See the InteractionSource documentation and samples for more information.
  - ([I85965](https://android-review.googlesource.com/#/q/I85965d0dba39d1740c097915d1d1a367eea2a78c), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/171913923](https://issuetracker.google.com/issues/171913923), [b/171710801](https://issuetracker.google.com/issues/171710801), [b/174852378](https://issuetracker.google.com/issues/174852378))
- Add AccessibilityMananger interface and LocalAccessibilityMananger in CompositionLocals ([I53520](https://android-review.googlesource.com/#/q/I5352073036978c367161e5c2f7cb3402dd502a65))
- Removed deprecated LayoutCoordinates methods, use function instead of the property for positionInParent and boundsInParent ([I580ed](https://android-review.googlesource.com/#/q/I580edba74283600c3aafba6130a7af806df7d6c5), [b/169874631](https://issuetracker.google.com/issues/169874631), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Slider now supports enabled/disabled state ([I6d56b](https://android-review.googlesource.com/#/q/I6d56b992042f54b63daf4936ef6f6c27319b0498), [b/179793072](https://issuetracker.google.com/issues/179793072))
- Created new TextInputSession for input sessions from low level text components such as CoreTextField. ([I8817f](https://android-review.googlesource.com/#/q/I8817f81e7c1b0066795ecb4af3674e99413362d0), [b/177662148](https://issuetracker.google.com/issues/177662148))
- AnimationEndReason.Interrupted is removed. CancellationException will be throws if animation is interrupted. ([I2cbbc](https://android-review.googlesource.com/#/q/I2cbbc6112cef6e750c10843846ee46cb9d077b03), [b/179695417](https://issuetracker.google.com/issues/179695417))
- Removed `@ExperimentalRippleApi` and changed `RippleAlpha` to be a class with properties instead of an interface. ([I6df7c](https://android-review.googlesource.com/#/q/I6df7c2fd5fdf528bb245c13d9eb4fcecdb438eed))
- Added TextFieldColors interface to represent different colors used in TextField and OutlinedTextField in different states. For defaut implementation see TextFieldDefaults.textFieldColors and TextFieldDefaults.outlinedTextFieldColors.
  - Renamed isErrorValue parameter inside TextField and OutlinedTextField into isError. ([I831f9](https://android-review.googlesource.com/#/q/I831f90c3be79452bcaa6dff41d1777298a23ca09), [b/171305338](https://issuetracker.google.com/issues/171305338), [b/168004067](https://issuetracker.google.com/issues/168004067))
- Add selectionGroup modifier that allows to mark collection of Tabs or RadioButtons for accessibility purposes ([Ie5c29](https://android-review.googlesource.com/#/q/Ie5c29bc1cc0630f4f3a68ff57ebd94464c89ffd7))
- Add LazyListState.animateScrollToItem

  This method smooth scrolls to a specific item in the list. ([I4bfd7](https://android-review.googlesource.com/#/q/I4bfd722f76c600483b41d27164eae10e24cc1454))
- `ScrollableState.smoothScrollBy()` was renamed to `animateScrollBy()`
  `LazyListState.snapToItemIndex()` was renamed to `scrollToItem()`
  `ScrollState.smoothScrollTo()` was renamed to `animateScrollTo()` ([I35ded](https://android-review.googlesource.com/#/q/I35deda2585dafb47c8b4d68fc0063d289f5c78d6))

- Any composables marked with `@ReadOnlyComposable` are now compile-time validated to ensure that they only make calls to other `@ReadOnlyComposables` ([I58961](https://android-review.googlesource.com/#/q/I58961d2946c80a6a2d9e8e0cca35fd61f41ee703))

- TargetAnimation API has been removed. ([If47d1](https://android-review.googlesource.com/#/q/If47d1f88096955c131af20c1660a5c450d5b7ed9), [b/177457083](https://issuetracker.google.com/issues/177457083))

- Scroll position in Modifier.verticalScroll()/horizontalScroll() is represented with Ints now ([I81298](https://android-review.googlesource.com/#/q/I81298a8767a421293ca7d5ab33ce8373e63f383c))

- smoothScrollBy and scrollBy methods' packages changed to `androidx.compose.foundation.gestures.*` ([I3f7c1](https://android-review.googlesource.com/#/q/I3f7c18be72b1b4e8d7958194b10d63d749f7d948), [b/175294473](https://issuetracker.google.com/issues/175294473))

- FlingConfig has been renamed to FlingBehavior now allows for customization of suspend animation rather than predefined Decays. ([I02b86](https://android-review.googlesource.com/#/q/I02b8639c646d24fd19ef7ac504ef6660b8906d54), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Size modifiers were renamed. Modifier.width/height/size were renamed to requiredWidth/requiredHeight/requiredSize. Modifier.preferredWidth/preferredHeight/preferredSize were renamed to width/height/size. ([I5b414](https://android-review.googlesource.com/#/q/I5b4145953d360b1fb851c0056fc9a7875bb34088))

- defaultMinSizeConstraints was renamed to defaultMinSize. ([I4eaae](https://android-review.googlesource.com/#/q/I4eaaec7cb1fffdb530744c7b7e42f23a26e96493))

- Orientation has been moved to foundation package. VelocirtTracker moved from ui.gesture to ui.input.pointer. ([Iff4a8](https://android-review.googlesource.com/#/q/Iff4a887648735c4850dca0d8d95fd99d782d04bb), [b/175294473](https://issuetracker.google.com/issues/175294473))

- drawerState.open() and drawerState.close() are now suspending functions. Use rememberCoroutineScope() to get the scope of the composition to call them ([I16f60](https://android-review.googlesource.com/#/q/I16f608d016fa82a59e3e68b96cb4931dcebb57a6), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Providers has been renamed to CompositionLocalProvider

  - The Composition constructor no longer accepts a key parameter, and has been deprecated.
  - currentCompositeKeyHash has been turned into a composable top level property instead of a composable top level function.
  - CompositionData and CompositionGroup have been moved to the androidx.compose.runtime.tooling namespace
  - ComposableLambda has been made an interface instead of a concrete class, and no longer has type parameters.
  - ComposableLambdaN has been made an interface instead of a concrete class, and no longer has type parameters.
  - The snapshotFlow function has been moved to the androidx.compose.runtime namespace
  - the merge method of SnapshotMutationPolicy is no longer experimental
  - The `@TestOnly` top level clearRoots function has been removed. It is no longer necessary.
  - keySourceInfoOf and resetSourceInfo functions have been removed. They are no longer necessary.
  - Composer.collectKeySourceInformation has been removed. It is no longer necessary.
  - isJoinedKey, joinedKeyLeft, and joinedKeyRight methods have been removed. They are no longer necessary.
  - Various top level APIs have been moved and reorganized into different files. Due to Kotlin's file class semantics, this will break binary compatibility but not source compatibility, so should not be an issue for most users.
  - ([I99b7d](https://android-review.googlesource.com/#/q/I99b7de8ea0fb5d73a0ee4667a65e35d976383831), [b/177245490](https://issuetracker.google.com/issues/177245490))
- Modifier.scrollable has been reworked. Now it uses Scrollable interface instead of ScrollableController class ([I4f5a5](https://android-review.googlesource.com/#/q/I4f5a5189b90cdff631ffb7166ce2e847b92db205), [b/174485541](https://issuetracker.google.com/issues/174485541), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Modifier.draggable now accepts DraggableState instead of a simple lambda. you can create state via `rememberDraggableState { delta -> }` to get the same behaviour as before ([Ica70f](https://android-review.googlesource.com/#/q/Ica70f33e73b6691375c9bdf07d008bae7546d48a), [b/175294473](https://issuetracker.google.com/issues/175294473))

- ZoomableController.smoothScaleBy and
  ZoomableController.stopAnimation are now suspend functions. ([I7f970](https://android-review.googlesource.com/#/q/I7f970ebd60086d3fbe4d805ac115de749bbd4240), [b/177457083](https://issuetracker.google.com/issues/177457083))

- Deleted some previously deprecated APIs ([Ice5da](https://android-review.googlesource.com/#/q/Ice5dae36591015a9d905b84b26cc02662385d831), [b/178633932](https://issuetracker.google.com/issues/178633932))

- Made the following Material API changes:

  - Added contentPadding parameter to Top/BottomAppBar to allow customizing the default padding.
  - Reordered parameters in BackdropScaffold to follow API guidelines for required parameters being before optional parameters.
  - Moved `icon` parameter in BottomNavigationItem to be after `selected` and `onClick`.
  - Renamed `alwaysShowLabels` parameter in BottomNavigationItem to `alwaysShowLabel`.
  - Renamed `bodyContent` parameters in a few components to just `content`.
  - Reordered parameters in `ButtonDefaults.buttonColors()`. Please note that because the type of the parameters have not changed, this will not cause an error in your code - please ensure you are either using named parameters or update the ordering manually, otherwise your code will not work the same as previously.
  - Added `secondaryVariant` parameter to `darkColors()`. This color is typically the same as `secondary` in dark theme, but adding for consistency and further customization.
  - Removed ElevationDefaults and animateElevation() from the public API surface since they were not commonly used / useful.
  - Renamed `onValueChangeEnd` in `Slider` to `onValueChangeFinished` and made it nullable.
  - Renamed `text` parameter in `Snackbar` to `content` for consistency.
  - Added `contentPadding` parameter to `DropdownMenuItem` to allow customizing the default padding and made `content` be an extension on `RowScope`.
  - Renamed `ModalDrawerLayout` to `ModalDrawer`.
  - Renamed `BottomDrawerLayout` to `BottomDrawer`.
  - ([I1cc66](https://android-review.googlesource.com/#/q/I1cc669dfec6194e13843879823bfdc97f98a7d20))
- BasicTextField now accepts Brush instead of Color for better customization ([I83a36](https://android-review.googlesource.com/#/q/I83a36a7e21f7a4fa796fc61904ca3324a44a4bdd))

- imageResource and vectorResource are now extension functions
  on ImageBitmap and ImageVector companions respectively.
  load{Image,Vector,Font}Resource functions have been deleted. ([I89130](https://android-review.googlesource.com/#/q/I89130cd429dfcbe54995d667d3501e3363851bce))

- Changed Indication#createIndication() to Indication#rememberUpdatedIndication(InteractionState) and removes InteractionState parameter from IndicationInstance#drawIndication(). IndicationInstance should only be responsible for drawing visual effects, and not launching animations / writing state in response to InteractionState changes. These animations and state writes should happen within `rememberUpdatedIndication()` instead. The `indication` parameter in `Modifier.indication` was also changed to be a required parameter. ([Ic1764](https://android-review.googlesource.com/#/q/Ic1764c0417b25cd0a0dbb96ed3e1b0974618c4ca), [b/152525426](https://issuetracker.google.com/issues/152525426))

**Bug Fixes**

- Added new LocalSoftwareKeyboardController composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I658b6](https://android-review.googlesource.com/#/q/I658b6bfc5c917db486c631312e3456469a615831), [b/168778053](https://issuetracker.google.com/issues/168778053))

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.material:material-*:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/material)

**API Changes**

- Modifier.pointerInput now requires remember keys to indicate when the pointer input detection coroutine should restart for new dependencies. ([I849cd](https://android-review.googlesource.com/#/q/I849cd63912b2d4c86ebe0dd24a7d0e2eb7a4e6d1))
- BottomDrawerLayout and ListItem have been marked as @ExperimentalMaterialApi ([Id766e](https://android-review.googlesource.com/#/q/Id766ec28dfebd958298f71f14d2ffc2f03cd162b))
- PaddingValues.Absolute was added and can be used in APIs accepting PaddingValues. ([Ia5f30](https://android-review.googlesource.com/#/q/Ia5f30058d0e5e9549132cdad9b1611a20c975359))
- onImeActionPerformed is deprecated. use KeyboardActions instead ([If0bbd](https://android-review.googlesource.com/#/q/If0bbda1241018d4c19b5df3cd1811c38cce4a76d), [b/179071523](https://issuetracker.google.com/issues/179071523))
- In order to better match naming conventions with ImageBitmap and ImageVector, ImagePainter has been renamed to BitmapPainter to parallel VectorPainter. ([Iba381](https://android-review.googlesource.com/#/q/Iba3810ae5cfd6f57442154c93eec500f35ba4ad5), [b/174565889](https://issuetracker.google.com/issues/174565889))
- Animatable.snapTo and Animatable.stop are now suspend functions ([If4288](https://android-review.googlesource.com/#/q/If42887504caa0a07a0d89477805b68ca51c9b3b4))
- ComponentActivity.setContent has moved to androidx.activity.compose.setContent in the androidx.activity:activity-compose module. ([Icf416](https://android-review.googlesource.com/#/q/Icf4168e6078b87ce746569a946b2a90274197c72))
- Destructuring and copy() methods have been removed from several classes where they were rarely used. ([I26702](https://android-review.googlesource.com/#/q/I267021d3a45314acc9a169f6bbdfbfb4295a448c), [b/178659281](https://issuetracker.google.com/issues/178659281))
- Make halfExpand() and expand() in ModalBottomSheetState internal ([Ic914e](https://android-review.googlesource.com/#/q/Ic914e14324ab13ead315f0d545bf675d1e0c71fa))
- Changed Indication#createInstance to be @Composable, and changed LocalIndication to contain an Indication, not () -\> Indication. ([I5eeea](https://android-review.googlesource.com/#/q/I5eeea2424e4deda6116f0b48b690b628f8d545eb), [b/157150564](https://issuetracker.google.com/issues/157150564))
- Moved AlertDialog and DropdownMenu to be Android only for now. Added PopupProperties parameter to DropdownMenu for further configuration of the underlying Popup. ([I9c443](https://android-review.googlesource.com/#/q/I9c4434bdfcc070bb7f3c6b9be7bd7ccb775660b5))
- loadFontResource is deprecated. Use fontResource instead. imageResource, loadImageResource, vectorResource, and loadVectorResource are deprecated. Use painterResource instead. ([I6b809](https://android-review.googlesource.com/#/q/I6b8096508b2280ca49c70a432c5497f386dc570e))
- Removed `toggle` and `toggleModifier` parameter from DropdownMenu, and renamed `dropdownModifier`, `dropdownOffset` and `dropdownContent` to `modifier`, `offset` and `content` respectively. DropdownMenu now behaves consistently to `Popup`, where the parent layout is used for the position of the menu. In most cases you can move `toggle` to be a sibling of `DropdownMenu` and wrap both in a `Box`. See the updated sample in the documentation for more information on usage of this API. ([I884fb](https://android-review.googlesource.com/#/q/I884fbf5ca080e3afea00146c5a7a869247b3613e))
- toIntPx() was renamed to roundToPx(). ([I9b7e4](https://android-review.googlesource.com/#/q/I9b7e460fb4b6e72ba65cdd8f5d1165c306461773), [b/173502290](https://issuetracker.google.com/issues/173502290))
- IntBounds was renamed to IntRect and the API was improved. ([I1f6ff](https://android-review.googlesource.com/#/q/I1f6ff3831e502856f1550ede9c367bf05c5a51b1))
- Added expand and collapse semantics actions. Added expand and halfExpand in ModalBottomSheetState ([Ib5064](https://android-review.googlesource.com/#/q/Ib50644cb5d591f9c3a58b4d35da064341ac7253c))
- Modifier.dragGestureFilter has been deprecated. Use `Modifier.pointerInput { detectDragGestures (...)}` instead. Alternatively, use Modifier.draggable for one axis drags ([I0ba93](https://android-review.googlesource.com/#/q/I0ba93559f565fc2a277f322e53dce9df9855ea46), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Renamed Ambients to match the Ambient -\> CompositionLocal rename. Ambients used to be named AmbientFoo, now CompositionLocals are named LocalFoo. ([I2d55d](https://android-review.googlesource.com/#/q/I2d55d1c5c38a08b04e72a569d3079db4feca1bf7))
- Selection was moved to foundation. ([I7892b](https://android-review.googlesource.com/#/q/I7892b8be5d2f91849f8ecc2e1034e0a8277bb61c))
- Similarly to how we previously removed `state { 0 }` composable and now promote usage like `remember { mutableStateOf(0) }` we are going to remove `savedInstanceState { 0 }` composable. You should use `rememberSaveable { mutableStateOf(0) }` instead and it will save and restore automatically if the type used inside the MutableState can be stored in the Bundle. If previously you were passing a custom saver object now you need to use a new overload of rememberSaveable which has `stateSaver` parameter. The usage will look like this: `val holder = rememberSaveable(stateSaver = HolderSaver) { mutableStateOf(Holder(0)) }` ([Ib4c26](https://android-review.googlesource.com/#/q/Ib4c266902d166f119ea1770cccbc78ac25a54ff7), [b/177338004](https://issuetracker.google.com/issues/177338004))
- Added ProgressBarRangeInfo.Indeterminate to mark indeterminate progress bars for accessibility ([I6fe05](https://android-review.googlesource.com/#/q/I6fe052ba60861d64f31963507ff11e95f3331d89))
- @ComposableContract has been deprecated in favor of three more specific annotations.

  - `@ComposableContract(restartable = false)` has become `@NonRestartableComposable`
  - `@ComposableContract(readonly = true)` has become `@ReadOnlyComposable`
  - `@ComposableContract(preventCapture = true)` has become `@DisallowComposableCalls`
  - `@ComposableContract(tracked = true)` has been removed.
  - ([I60a9d](https://android-review.googlesource.com/#/q/I60a9db0287dc0e03b38e6cf31a7d435026a2ce0f))
- `emptyContent()` and `(@Composable () -> Unit).orEmpty()` utilities have been deprecated as they no longer have any positive performance impact or value ([I0484d](https://android-review.googlesource.com/#/q/I0484d3ef439993d05eea86e53f05997eced590ab))

- rememberSavedInstanceState() was renamed to rememberSaveable() and moved to androidx.compose.runtime.saveable package. ([I1366e](https://android-review.googlesource.com/#/q/I1366e7fef0a5a56a43d6eeb3770967a9bf683380), [b/177338004](https://issuetracker.google.com/issues/177338004))

- Saver, listSaver(), mapSaver(), autoSaver was moved from androidx.compose.runtime.savedinstancestate to androidx.compose.runtime.saveable ([I77fe6](https://android-review.googlesource.com/#/q/I77fe618aa5e124891b84973d8b8b12735f9f909e))

- Parameters on RounderCornerShape, CutCornerShape and CornerBasedShape were renamed from left/right to start/end in order to support the shape's auto mirroring in the rtl direction. AbsoluteRounderCornerShape and AbsoluteCutCornerShape were introduced for the cases when auto-mirroring is not desired. ([I61040](https://android-review.googlesource.com/#/q/I61040b7bba950191361af89ff4c736ef6cb56235), [b/152756983](https://issuetracker.google.com/issues/152756983))

- Changed Tab's `text` and `icon` parameters, and BottomNavigationItem's `label` parameter to be nullable, to better convey the behavior of the component when these parameters are / are not provided, since it affects the size and layout of the component. If you are currently passing `emptyContent()` to represent no text / icon / label, you should use `null` instead. ([I57ed4](https://android-review.googlesource.com/#/q/I57ed4f72c434440068ab17edfa2b5ef791ddbf2f))

- Renamed contentColorFor color parameter to backgroundColor ([I5bb67](https://android-review.googlesource.com/#/q/I5bb67382d0d3d1c37c0ea741a902f4f875cdd1d8))

- Deprecated TabDefaults and replaced it with TabRowDefaults. ([I0f189](https://android-review.googlesource.com/#/q/I0f18943cbdff6ab88239d5ab3189ad1440011de0))

- Introduced ColorMatrix API used
  to modify rgb values of source content
  Refactored ColorFilter API to be an
  interface and match the implementation
  of PathEffect. ([Ica1e8](https://android-review.googlesource.com/#/q/Ica1e88332eb005e185e3da2ec95aff33440aa51d))

- AnimatedValue/Float is now deprecated. Please use
  Animatable instead. ([I71345](https://android-review.googlesource.com/#/q/I713457f88b04e50fbc5deb70a5bb7bbcf777e630), [b/177457083](https://issuetracker.google.com/issues/177457083))

- Add SemanticsProperties.PaneTitle API. ([I20d5a](https://android-review.googlesource.com/#/q/I20d5a27adec172993b792a4cfa7df37280aa0425))

- Added enabled parameters to Tab and BottomNavigationItem, to prevent them from being clickable. Changed BottomNavigationItem to be RowScope.BottomNavigationItem to better express its layout requirements in its API. ([Id683d](https://android-review.googlesource.com/#/q/Id683dc9a558c8d0704306a1c7f307985a9dbb12f))

- tapGestureFilter, doubleTapGestureFilter, longPressGestureFilter and pressIndicaitonGestureFilter have been deprecated. Use Modifier.clickable or Modifier.pointerInput with detectTapGestures function instead. ([I6baf9](https://android-review.googlesource.com/#/q/I6baf95f881b6fa6890ca1d065d49fef3e27bce83), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Add layoutDirection param to Shape's createOutline. This allows to create layout direction aware shapes. ([I57c20](https://android-review.googlesource.com/#/q/I57c20c45978b5468556159966bd9836653a2e40d), [b/152756983](https://issuetracker.google.com/issues/152756983))

- Removed `Recomposer.current()`. \[Abstract\]ComposeView now
  default to lazily created, window-scoped Recomposers driven by the
  ViewTreeLifecycleOwner for the window. Recomposition and
  withFrameNanos-based animation ticks are paused while the host Lifecycle
  is stopped. ([I38e11](https://android-review.googlesource.com/#/q/I38e11565b2fc776966b6b6984aceafd8a1e6fed1))

**Bug Fixes**

- Icon will now scale up to fit its size, respecting size modifiers applied to it. For example `Icon(.., modifier = Modifier.size(50.dp)` will now draw in a 50x50dp space. ([Ib2ba9](https://android-review.googlesource.com/#/q/Ib2ba987760dbd038d075e720cf705eef99456f15), [b/178796190](https://issuetracker.google.com/issues/178796190))

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.material:material-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/material)

**API Changes**

- Promotes some Material APIs to no longer be `@Experimental` ([I5d20e](https://android-review.googlesource.com/#/q/I5d20e2ae511aca075231e8ef32026e1ef76b5b6b))
- Content description parameter has been added to the Image and Icon. It is used to provide description to the accessibility services ([I2ac4c](https://android-review.googlesource.com/#/q/I2ac4c1058ed0bf1e5756cc6cdae546806974409e))
- Changes Material stateful parameter interfaces to have @Composable functions that return `State<T>`. Adds `Animatable.asState()` to make it easier to convert an Animatable to a State. Also changes animateElevation to be a suspend extension on Animatable. ([If613c](https://android-review.googlesource.com/#/q/If613cc7c751a11b77a03f8066b233b7e55cb67e0))
- Snackbar, SnackbarHost, SnackbarHostState are not `@ExperimentalMaterialAPI` anymore ([Id1fb5](https://android-review.googlesource.com/#/q/Id1fb55a91d53bd74adb131a318fee1cad0b485d8))
- Changes Typography, Shapes, and TabPosition to no longer be data classes. Adds copy function for Typography and Shapes to replace the generated ones. ([I40037](https://android-review.googlesource.com/#/q/I40037a96c8484c01d28a4dd1d8ab7a3105a34805))
- Deleted some previously deprecated Material APIs ([Ifaa25](https://android-review.googlesource.com/#/q/Ifaa25387db4af0195bdccb465d6ebb76a9a24297))

**Bug Fixes**

- onCommit, onDispose, and onActive have been deprecated in favor of SideEffect and DisposableEffect APIs ([If760e](https://android-review.googlesource.com/#/q/If760ec2a190c4121a35006695d953010ac22a43a))
- TransitionDefinition-based Transition has been deprecated ([I0ac57](https://android-review.googlesource.com/#/q/I0ac57acd13386d028dfe0840e8ce509362cf107e))
- Initial State in updateTransition is now supported ([Ifd51d](https://android-review.googlesource.com/#/q/Ifd51d5c737b86d52282c18e29b89e75e1c0bea35))
- WithConstraints was reworked as BoxWithConstraints and moved to foundation.layout. ([I9420b](https://android-review.googlesource.com/#/q/I9420b9e0fbea7ee048b23a6ef328165bbb11e8a8), [b/173387208](https://issuetracker.google.com/issues/173387208))
- Deprecate non-suspend scrollBy, remove non-suspend scrollTo

  We now recommend using suspend functions to control scrolling and wait
  for the scroll to finish. We are deprecating and/or removing the
  non-suspend versions of these functions as part of this transition. ([Ie9ced](https://android-review.googlesource.com/#/q/Ie9cedf8bc71b54353a175699901edd92f850d02c))
- Deprecate non-suspend smoothScrollBy
  We now recommend using suspend functions to control scrolling and wait
  for the scroll to finish. We are deprecating the non-suspend versions
  of these functions as part of this transition. ([I12880](https://android-review.googlesource.com/#/q/I128806c8aea7f17758d1a5d953bbe40e3bcc1b18))

- Introduced `ComposeContentTestRule`, which extends
  `ComposeTestRule` and defines `setContent`, which has been removed from
  `ComposeTestRule`. Added a factory method `createEmptyComposeRule()`
  that returns a `ComposeTestRule` and does not launch an Activity for
  you. Use this when you want to launch your Activity during your test,
  e.g. using `ActivityScenario.launch` ([I9d782](https://android-review.googlesource.com/#/q/I9d78283c27d87a3135071884e115bbd814492c47), [b/174472899](https://issuetracker.google.com/issues/174472899))

- The ripple used in Button and FloatingActionButton can no longer be customized by providing a new Indication through AmbientIndication - this was never intended to be a way to customize these components and this now makes these components consistent with other Material components. To customize ripples across an application, see RippleTheme. ([I546c5](https://android-review.googlesource.com/#/q/I546c59bf53904435e14590ed4b3ca9973704bff3))

- animateAsState is now animateFooAsState, where Foo is the
  type of the variable being animated. e.g. Float, Dp, Offset, etc ([Ie7e25](https://android-review.googlesource.com/#/q/Ie7e25c8978996334b0dcc757b07df1434ff346aa))

- BasicTextField received a new parameter called `decorationBox`. It allows to add the decorations like icons, placeholder, label and similar to the text field and increase the hit target area of it. ([I16996](https://android-review.googlesource.com/#/q/I169960830df82b0406ac4b6868ea544c9f848403))

- Fix for a bug which made it not possible to set the width of the material text field be less than 280.dp ([I78373](https://android-review.googlesource.com/#/q/I7837308a081e04d00ac4bf7e71b2f65698cebf00))

- canDrag parameter has been removed from the Modifier.draggable ([Ic4bec](https://android-review.googlesource.com/#/q/Ic4bec74b6fb3a9306abe4fdee7c6961ad3a62d77), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Remove displaySize as it should be avoided. Typically it is
  better to use size of onRoot() or window size at least. ([I62db4](https://android-review.googlesource.com/#/q/I62db4535f36b09ab6f0b874c221ece0b352db962))

- Surface can now have multiple layout children. ([I66a92](https://android-review.googlesource.com/#/q/I66a921f3963162ae62cdb498298e6aa4210cf602), [b/144488459](https://issuetracker.google.com/issues/144488459))

- invalidate and compositionReference() are now deprecated in favor of currentRecomposeScope and rememberCompositionReference respectively. ([I583a8](https://android-review.googlesource.com/#/q/I583a8efa6e3d3bc303792b825b948b3722ada103))

- Changes PopupPositionProvider to use window-relative coordinates, not global coordinates. Renames parentGlobalBounds to anchorBounds, and changes windowGlobalBounds to be `windowSize: IntSize` ([I2994a](https://android-review.googlesource.com/#/q/I2994a280d3d5c2eafa3a7027f7df5403acaa9cc9))

- Duration and Uptime will be replace with Long milliseconds,
  and this step removes the dependency of pointer input on those
  classes. ([Ia33b2](https://android-review.googlesource.com/#/q/Ia33b2d6835861501019481b388cb2c99441c346c), [b/175142755](https://issuetracker.google.com/issues/175142755), [b/177420019](https://issuetracker.google.com/issues/177420019))

- AnimatedFloat.fling that accepts FlingConfig has been removed. Please use suspend
  Animatable.animateDecay instead. ([I4659b](https://android-review.googlesource.com/#/q/I4659b606834e8325473fd672d824114b8ec20173), [b/177457083](https://issuetracker.google.com/issues/177457083))

- clickable, toggleable and selectable can be created outside of composition now ([I0a130](https://android-review.googlesource.com/#/q/I0a130bfa57713c96cc8b52c67becd32145526685), [b/172938345](https://issuetracker.google.com/issues/172938345), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Easing has been changed to a functional interface ([Ib14e5](https://android-review.googlesource.com/#/q/Ib14e513b2c4b839287535bda19ae93375a4baa73))

- ScrollableColumn/Row were deprecated. Using ScrollableColumn is less efficient comparing to LazyColumn when you have a large scrolling content because with LazyColumn we can only compose/measure/draw visible elements. To prevent users from going inefficient way we decided to deprecate ScrollableColumn and ScrollableRow and promote usages of LazyColumn and LazyRow instead. Users can still decide they don't need the lazy behaviour and use the modifiers directly like this: Column(Modifier.verticalScroll(rememberScrollState())) ([Ib976b](https://android-review.googlesource.com/#/q/Ib976b534e063a86a2c587762b786a23e32cc61b6), [b/170468083](https://issuetracker.google.com/issues/170468083))

- New `items(count: Int)` factory method for scope of LazyColumn/LazyRow/LazyVerticalGrid.
  `items(items: List)` and `itemsIndexed(items: List)` are now extension functions so you have to manually import them when used.
  New extension overloads for Arrays: `items(items: Array)` and `itemsIndexed(Array)` ([I803fc](https://android-review.googlesource.com/#/q/I803fc5f25fac55855c710ff5064f11525f7b6010), [b/175562574](https://issuetracker.google.com/issues/175562574))

- Removed experimental monotonicFrameAnimationClockOf methods ([Ib753f](https://android-review.googlesource.com/#/q/Ib753f5d3cb77dabc7727f677a73bb7da8dae5fe2), [b/170708374](https://issuetracker.google.com/issues/170708374))

- Deprecated global coordinates methods and made
  new window-based coordinates methods. ([Iee284](https://android-review.googlesource.com/#/q/Iee284dee7dbc4226493feb144d446a0289b7c83e))

- Added Modifier.toolingGraphicsLayer which adds a graphics layer modifier when inspection is turned on. ([I315df](https://android-review.googlesource.com/#/q/I315df592b0903a783dcd48deff73f31beb63b56c))

- FocusRequester.createRefs is now marked as experimental as it might change. ([I2d898](https://android-review.googlesource.com/#/q/I2d898d56ed0ac33f5a08253509cfd811ee0e8a5d), [b/177000821](https://issuetracker.google.com/issues/177000821))

- SemanticsPropertyReceiver.hidden was renamed to invisibleToUser and marked @ExperimentalComposeUiApi.
  AccessibilityRangeInfo was renamed to ProgressBarRangeInfo.
  stateDescriptionRange was renamed to progressBarRangeInfo.
  AccessibilityScrollState was renamed to ScrollAxisRange.
  horizontalAccessibilityScrollState was renamed to horizontalScrollAxisRange.
  verticalAccessibilityScrollState was renamed to verticalScrollAxisRange. ([Id3148](https://android-review.googlesource.com/#/q/Id31487aa7cbddf4d3d163999afae458cdab4dc8a))

- Leverage TestCoroutineDispatcher in testing ([I532b6](https://android-review.googlesource.com/#/q/I532b68e37ea6f72964fdcc267e397d285cffd9ad))

- Updated vector graphics
  API to support parsing of tinting
  applied to root of vector graphics. ([Id9d53](https://android-review.googlesource.com/#/q/Id9d53298227fdce798db2968f79d1d27c57c1312), [b/177210509](https://issuetracker.google.com/issues/177210509))

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.material:material-*:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/material)

**API Changes**

- Modified Velocity to have component parts and mathematical operations. ([Ib0447](https://android-review.googlesource.com/#/q/Ib0447d694d7c5dc82fcef7448faeb0cdda87fced))
- Renamed `@ExperimentalTesting` to `@ExperimentalTestApi` to be consistent with similar experimental api annotations ([Ia4502](https://android-review.googlesource.com/#/q/Ia4502a82d5b66328b6e3e3cd322614939816901e), [b/171464963](https://issuetracker.google.com/issues/171464963))
- Renamed Position to DpOffset and removed getDistance() ([Ib2dfd](https://android-review.googlesource.com/#/q/Ib2dfde4ceb450e417ff759bdabbc74d2506a44c9))
- Ranamed Color.useOrElse() to Color.takeOrElse() ([Ifdcf5](https://android-review.googlesource.com/#/q/Ifdcf503101fa33b1eaf729a33ac14d0dc03f66ff))
- Add Toggle to foundation Strings.kt ([I4a5b7](https://android-review.googlesource.com/#/q/I4a5b74e3ed9bc3b1acd09af221331ef6ab51b9fe), [b/172366489](https://issuetracker.google.com/issues/172366489))
- FlowRow and FlowColumn were deprecated. Please use a custom layout instead. ([I09027](https://android-review.googlesource.com/#/q/I0902712b97eed1baecddf605bbac0246938c812d))
- Modifier.focus() and Modifier.focusRequester() are deprecated. Use Modifier.focusModifier() and Modifier.focusReference() instead. ([I75a48](https://android-review.googlesource.com/#/q/I75a483954b69de794c5d7be9efc236b6d6b8fcad), [b/175160751](https://issuetracker.google.com/issues/175160751), [b/175160532](https://issuetracker.google.com/issues/175160532), [b/175077829](https://issuetracker.google.com/issues/175077829))
- Moved nativeClass to ui module and made it internal. Updated usages of nativeClass in equals implementations to use 'is MyClass' instead. ([I4f734](https://android-review.googlesource.com/#/q/I4f7340266d36552665f0a059ab34e9b886926f0b))

**Bug Fixes**

- Added support for disabled and read-only text fields ([I35279](https://android-review.googlesource.com/#/q/I352791811a7b75189013e1ed73c9834cfa5ce961), [b/171040474](https://issuetracker.google.com/issues/171040474), [b/166478534](https://issuetracker.google.com/issues/166478534))
- `animate()` is now replaced with `animateAsState()`, which returns a `State<T>` instead of `T`. This allows better performance, as the invalidation scope can be narrowed down to where the State value is read. ([Ib179e](https://android-review.googlesource.com/#/q/Ib179e3f5f4bf3b72f7445fc22e73c46af7cf74de))
- Add Semantics role API and add Role as a parameter to clickable, selectable and toggleable SemanticsModifier. Changed Modifier.progressSemantics so that Slider can also use it. ([I216cd](https://android-review.googlesource.com/#/q/I216cd5b9118581e569c48a095f009c841ed4418b))

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.material:material-*:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/material)

**API Changes**

- added API to manually trigger settle animation and drag in Modifier.swipeable ([Iaa17a](https://android-review.googlesource.com/#/q/Iaa17a40fec2949f6364a9339a5d269dc622570d6), [b/162408885](https://issuetracker.google.com/issues/162408885))
- Renamed \*Constants objects such as ButtonConstants to end with Defaults instead, such as ButtonDefaults. Also removes unnecessary `default` prefixes from properties in these new objects. ([Ibb915](https://android-review.googlesource.com/#/q/Ibb915f0fd06a9c99ae6791e85634d5aea49374f6), [b/159982740](https://issuetracker.google.com/issues/159982740))
- Compose supports property getters that can make composable invocations. Support for this is not going away, but the syntax for declaring a property getter as being @Composable is changing.

  The now-deprecated syntax for doing this was by annotating the property itself:

          @Composable val someProperty: Int get() = ...

  The now-correct syntax for doing this is by annotating the getter of the property:

         val someProperty: Int @Composable get() = ...

  Both syntaxes will work for some time, but the former deprecated syntax will eventually become a compile error. ([Id9197](https://android-review.googlesource.com/#/q/Id91977f2583b81d3e4e51bbf120cfaf943be25d5))
- Added `androidx.compose.material:material-ripple` library containing ripple APIs to allow building interactive components without needing the rest of the Material library. rememberRippleIndication has been deprecated and replaced with rememberRipple. ([Ibdf11](https://android-review.googlesource.com/#/q/Ibdf11f8fe8da5abc8abc4d57e06c8e53b8eb589c))

**Bug Fixes**

- Lambdas in offset modifiers now return IntOffset rather than Float. ([Ic9ee5](https://android-review.googlesource.com/#/q/Ic9ee5c05df4c89993ee19f19ddd327a986f21bc1), [b/174137212](https://issuetracker.google.com/issues/174137212), [b/174146755](https://issuetracker.google.com/issues/174146755))
- Refactored ShaderBrush to
  lazily create a shader instance when
  sizing information of the drawing
  environment is available.
  This is useful to define gradients that
  occupy the full drawing bounds of a composable
  at composition time, without having to
  implement custom DrawModifier implementations.

  Deprecated gradient function constructor APIs
  in favor of factory methods on a Gradient object. ([I511fc](https://android-review.googlesource.com/#/q/I511fc09bdeb4b41127de4a6b1e616688b10295f5), [b/173066799](https://issuetracker.google.com/issues/173066799))
- Modifier.focusObserver is deprecated. Use Modifier.onFocusChanged or Modifier.onFocusEvent instead ([I30f17](https://android-review.googlesource.com/#/q/I30f17d06d60fa9b8c510ee0468464258894a467b), [b/168511863](https://issuetracker.google.com/issues/168511863), [b/168511484](https://issuetracker.google.com/issues/168511484))

- Deprecate LazyColumnFor, LazyRowFor, LazyColumnForIndexed and LazyRowForIndexed. Use LazyColumn and LazyRow instead ([I5b48c](https://android-review.googlesource.com/#/q/I5b48c8a3b1fef2f603ab69ded1d19709aa9f87fb))

- Moved Dp.VectorConverter, Position.VectorConverter, etc to
  animation-core, and deprecated the old VectorConveters ([If0c4b](https://android-review.googlesource.com/#/q/If0c4bbdec55ec9d6436d74156db6f993904aae47))

- Autofill API is now experimental API and requires opt-in ([I0a1ec](https://android-review.googlesource.com/#/q/I0a1ecfbf4ddeccaecc3cea8d2223b0a4afa60636))

- Adding destructuring declarations to create FocusRequester instances ([I35d84](https://android-review.googlesource.com/#/q/I35d84e1320bec5b62bf1fb096aa95f90cfd96e9c), [b/174817008](https://issuetracker.google.com/issues/174817008))

- accessibilityLabel has been renamed to contentDescription.
  accessibilityValue has been renamed to stateDescription. ([I250f2](https://android-review.googlesource.com/#/q/I250f2d41e139d4838b0b3706f18b56fcc4f515bd))

- New infiniteRepeatable function for creating an InfiniteRepeatableSpec ([I668e5](https://android-review.googlesource.com/#/q/I668e501c0c9061aa94b258ec9646617e0f77faf1))

- The positioning behaviour of DropdownMenus was slightly changed according to the Material spec. ([I34c72](https://android-review.googlesource.com/#/q/I34c721d5c6a710161af31bf131c7751740fb966c), [b/168594123](https://issuetracker.google.com/issues/168594123))

- InteractionState support for TextFields has been added. ([I61d91](https://android-review.googlesource.com/#/q/I61d91b15858fc3914ab9f15409857f0bccf67f34))

- Added Modifier.clearAndSetSemantics to clear descendants'
  semantics and set new ones. ([I277ca](https://android-review.googlesource.com/#/q/I277ca1b76fda44a34a2c01844b832244cb42ff7e))

- Moved ContentDrawScope to ui-graphics
  module to be with DrawScope. ([Iee043](https://android-review.googlesource.com/#/q/Iee0437fa587fbe12a3623955f5fe720d5aae551f), [b/173832789](https://issuetracker.google.com/issues/173832789))

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.material:material:1.0.0-alpha08`, `androidx.compose.material:material-icons-core:1.0.0-alpha08`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/material)

> [!NOTE]
> **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

**API Changes**

- MaterialTheme now sets the correct colors for selection handles and selection background. Non-Material apps can manually use AmbientTextSelectionColors to customize the colors used for selection. ([I1e6f4](https://android-review.googlesource.com/#/q/I1e6f4b495bdc713e162759a08ecf0a7311b26e33), [b/139320372](https://issuetracker.google.com/issues/139320372), [b/139320907](https://issuetracker.google.com/issues/139320907))
- Added lint check for composable lambda parameter naming and position, to check for consistency with Compose guidelines. Also migrated some APIs using `children` as the name for their trailing lambda to `content`, according to the lint check and guidance. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48e38a2896785b521814d95c9fb624d2807315))
- Renamed VectorAsset to ImageVector Moved and renamed VectorAsset to Builder to be an inner class of ImageVector as per API council guidelines. Added typealias of VectorAssetBuilder to link to ImageVector.Builder for compat. ([Icfdc8](https://android-review.googlesource.com/#/q/Icfdc85391feb2bd0edabebeba84f31bace10883a))
- Renamed ImageAsset and related methods to ImageBitmap. ([Ia2d99](https://android-review.googlesource.com/#/q/Ia2d9941a6e0b8c29867cb3fbafb629fa4db10684))
- Moved foundation semantics properties to ui ([I6f05c](https://android-review.googlesource.com/#/q/I6f05cc7c0bdf1e5344440cd6e492fbc0545011e7))
- `fun RippleIndication()` has been deprecated and replaced with `rememberRippleIndication()` for consistency with other APIs. ([Id8e2c](https://android-review.googlesource.com/#/q/Id8e2c54e8a15091aa27a014e1cc06886578dbe89))
- Added a singeLine parameter into BasicTextField, TextField and OutlinedTextField. Set this parameter to true to make the text field a single horizontally scrollable line. ([I57004](https://android-review.googlesource.com/#/q/I57004dff8b341f08f6673235e28e958c9fbf63c6), [b/168187755](https://issuetracker.google.com/issues/168187755))

**Bug Fixes**

- Add semantics action Dismiss ([I2b706](https://android-review.googlesource.com/#/q/I2b70641450760f3056a53e283cf04b004ea1db2c))
- Moved DrawModifier APIs from the androidx.compose.ui package to the androidx.compose.ui.draw package. Created DrawModifierDeprecated.kt file to include typealiases/helper methods to assist with the migration from the deprecated to the current APIs. ([Id6044](https://android-review.googlesource.com/#/q/Id6044c7119aeaf40a3ff21006fe39b03f5f1b18a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- Renamed Modifier.drawLayer to Modifier.graphicsLayer Also updated related classes to GraphicsLayer as per API feedback. ([I0bd29](https://android-review.googlesource.com/#/q/I0bd297065427d19715e4e33480f7be87e51ff48a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- `<T>` was removed from SubcomposeLayout declaration. You can use it without specifying a type now. ([Ib60c8](https://android-review.googlesource.com/#/q/Ib60c850964b308ebee32beca6db78d76af67fbf1))
- Added Modifier.scale/rotate APIs as conveniences for drawLayer.
  - Renamed `Modifier.drawOpacity` to `Modifier.alpha`
  - Renamed `Modifier.drawShadow` to `Modifier.shadow` ([I264ca](https://android-review.googlesource.com/#/q/I264ca72b36ea62fd615436849203895ed742fa1e), [b/173208140](https://issuetracker.google.com/issues/173208140))
- The alignment parameter of Box was renamed to contentAlignment. ([I2c957](https://android-review.googlesource.com/#/q/I2c95727d9ec49f056fffb3a73dce95a9d3be5b53))
- offsetPx modifiers were renamed to offset. They are now taking lambda parameters instead of State. ([Ic3021](https://android-review.googlesource.com/#/q/Ic302174ef9cffa7ef806d1668f81cb89159363f2), [b/173594846](https://issuetracker.google.com/issues/173594846))
- Introduced SweepGradientShader and SweepGradientBrush APIs. ([Ia22c1](https://android-review.googlesource.com/#/q/Ia22c1593bad5a63dbc66f4b012617087b30d2f77))
- Added lint check for Modifier parameters in Composable functions. This lint check checks the naming, return type, default value, and order of the parameter for consistency with Compose guidelines. ([If493b](https://android-review.googlesource.com/#/q/If493bd2e3c236cae95744e1fab138f87f5844daa))
- Updated TextFieldValue API
  - made TextFieldValue.composition readonly
  - removed exception thrown for invalid selection range ([I4a675](https://android-review.googlesource.com/#/q/I4a67592c05ab384ad5614cccf50ad6e79be52b55), [b/172239032](https://issuetracker.google.com/issues/172239032))
- Added a new `Modifier.drawLayer()` overload. It takes a lambda block on a new GraphicsLayerScope where you define the layer parameters in a way which allows to skip recomposition and relayout when the state change happens. DrawLayerModifier is now internal in preparation to migrating its logic into `placeable.placeWithLayer()` method of LayoutModifier ([I15e9f](https://android-review.googlesource.com/#/q/I15e9f41e3c93245529bf798e4a9617ca49d5e509), [b/173030831](https://issuetracker.google.com/issues/173030831))
- Deprecated Ambients named with `Ambient` as their suffix, and replaced them with new properties prefixed with Ambient, following other Ambients and Compose API guidelines. ([I33440](https://android-review.googlesource.com/#/q/I334403cc490ea913b8980d29e2cbe08e98ad7945))
- Added lint check to check that Modifier factories use `androidx.compose.ui.composed {}` internally, instead of being marked as `@Composable`. ([I3c4bc](https://android-review.googlesource.com/#/q/I3c4bcedafbd0bc9846a9c0ba75685a35cb4de371))
- Semantics argument mergeAllDescendants was renamed to mergeDescendants. ([Ib6250](https://android-review.googlesource.com/#/q/Ib625016bd3bbe4349c2870ba68ad52d76a0d372a))
- Time control in tests (TestAnimationClock and its usages) is now experimental ([I6ef86](https://android-review.googlesource.com/#/q/I6ef86c5f530422c7c751bdb086a691cbc2e837f3), [b/171378521](https://issuetracker.google.com/issues/171378521))
- Remove old ui-test module and its stubs ([I3a7cb](https://android-review.googlesource.com/#/q/I3a7cbbe376d0542955983fb09afd2dc37be7647e))
- TextUnit.Inherit is renamed to TextUnit.Unspecified for consistency with other units. ([Ifce19](https://android-review.googlesource.com/#/q/Ifce190ac87b01144b2fb0e7f9a8659bceed87f4e))
- The Alignment interface was updated and made functional. ([I46a07](https://android-review.googlesource.com/#/q/I46a0791e261b6f305804797cdda7fdd2ef405305), [b/172311734](https://issuetracker.google.com/issues/172311734))
- id was renamed to layoutId for LayoutIdParentData. Measurable.id was renamed to Measurable.layoutId. ([Iadbcb](https://android-review.googlesource.com/#/q/Iadbcb8b5588876e0d2a512e476968025b03ada6c), [b/172449643](https://issuetracker.google.com/issues/172449643))

### Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.material:material:1.0.0-alpha07`, `androidx.compose.material:material-icons-core:1.0.0-alpha07`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/material)

**API Changes**

- Emphasis has been deprecated and replaced with AmbientContentAlpha. AmbientContentAlpha is a simpler abstraction that represents the preferred content alpha for part of the hierarchy, similar to how AmbientContentColor represents the preferred content color. Text and Icon now consume the current value from AmbientContentAlpha by default, and you can manually do: `color.copy(alpha = AmbientContentAlpha.current)` to have the same effect in your components. Instead of using ProvideEmphasis, you can just directly provide a value through AmbientContentAlpha, and use the new default levels in ContentAlpha to replace the old EmphasisLevels. ([Idf03e](https://android-review.googlesource.com/#/q/Idf03e63a3082842e183535b5fdbf04947e3a671c), [b/159017896](https://issuetracker.google.com/issues/159017896))
- Adds androidx.compose.material.AmbientContentColor to replace androidx.compose.foundation.AmbientContentColor ([I84f7b](https://android-review.googlesource.com/#/q/I84f7be83a15ed02b301c3d9d0e44481ebb01ddb0), [b/172067770](https://issuetracker.google.com/issues/172067770))
- Adds androidx.compose.material.Text to replace androidx.compose.foundation.Text as a high level, themeable Text component. For a basic text component that does not consume color / text style from the theme, use BasicText. ([Ie6ae0](https://android-review.googlesource.com/#/q/Ie6ae043baf890ec6c47555bce2b0ea35d270ec2b))
- Added maxLines to TextFields ([Ib2a5b](https://android-review.googlesource.com/#/q/Ib2a5bb1c0ec8782b6a05fc48033fd4b05622820e))
- Update TextFields to accept KeyboardOptions ([Ida7f3](https://android-review.googlesource.com/#/q/Ida7f3c71647dc9fff8acdd50fc5604a15957ccec))
- Surface now uses the absolute (total) elevation when calculating elevation overlays, so a Surface nested in another Surface will use the combined elevation to draw the overlay. ([I7bd2b](https://android-review.googlesource.com/#/q/I7bd2b08da276d5624baad6a2e59eb74bc021bc45), [b/171031040](https://issuetracker.google.com/issues/171031040))

**Bug Fixes**

- `captureToBitmap` moved to `captureToImage`. ([I86385](https://android-review.googlesource.com/#/q/I86385454625b533b83c87e48d82e143dd1bcb88e))
- The foundation AmbientTextStyle, ProvideTextStyle, and AmbientContentColor have been deprecated. Instead use the new versions available in the Material library. For non-Material applications, you should instead create your own design system specific theming ambients that can be consumed in your own components. ([I74acc](https://android-review.googlesource.com/#/q/I74accf7166eaca28e9e2d14402ed08d80f8625ab), [b/172067770](https://issuetracker.google.com/issues/172067770))
- foundation.Text has been deprecated and replaced with material.Text. For a basic, unopinionated text API that does not consume values from a theme, see androidx.compose.foundation.BasicText. ([If64cb](https://android-review.googlesource.com/#/q/If64cbdd89497f171edfd1b4de907123f73279e8d))
- Rename KeyboardOptions as ImeOptions ([I82f36](https://android-review.googlesource.com/#/q/I82f364ca1ede4bfea9430fcc9fd227d729b39fd9))
- Moved KeyboardType and ImeAction into KeyboardOptions ([I910ce](https://android-review.googlesource.com/#/q/I910cea6ec0ef3568b9a94f7b193e8cb7e8b776ed))
- BaseTextField has been deprecated. Use BasicTextField instead. ([I896eb](https://android-review.googlesource.com/#/q/I896eb0eb21e73bda5f269e1ffae4357201acb219))
- ExperimentalSubcomposeLayoutApi annotation was removed. SubcomposeLayout can now be used without adding @OptIn ([I708ad](https://android-review.googlesource.com/#/q/I708adafbc3c10cc6c23fe5a236f66e73146e4f56))
- FirstBaseline and LastBaseline were moved to androidx.compose.ui.layout package ([Ied2e7](https://android-review.googlesource.com/#/q/Ied2e7ff4c8d8a45072439d719ea5c75270c28c97))
- Updated Icon API to take in Color.Unspecified as a possible tint color which will draw the provided asset or painter without a ColorFilter. Previously attempts to ignore tinting with Color.Unspecified would tint with a transparent color ending up with nothing rendered at all. ([I049e2](https://android-review.googlesource.com/#/q/I049e2b7464204f1fd8965d31d6dfba811b30a2bb), [b/171624632](https://issuetracker.google.com/issues/171624632))
- relativePaddingFrom was renamed to paddingFrom. The paddingFromBaseline modifier was added, as convenience for specifying distances from layout bounds to text baselines. ([I0440a](https://android-review.googlesource.com/#/q/I0440af2aea41e020cb581b9030522b7586fe952e), [b/170633813](https://issuetracker.google.com/issues/170633813))
- LaunchedTask was renamed to LaunchedEffect for consistency with the SideEffect and DisposableEffect APIs. LaunchedEffect with no subject params is not permitted in order to encourage best practices. ([Ifd3d4](https://android-review.googlesource.com/#/q/Ifd3d4f3b529b3956915c99096eef3fb3108b2b61))
- MeasureResult was moved out of MeasureScope. ([Ibf96d](https://android-review.googlesource.com/#/q/Ibf96ddadae8115015066dcda2026a57b87c2ead6), [b/171184002](https://issuetracker.google.com/issues/171184002))
- Several layout related symbols were moved from androidx.compose.ui to androidx.compose.layout.ui. ([I0fa98](https://android-review.googlesource.com/#/q/I0fa982d87929e5ca9e3a32762fe9cf1fa8b8cfef), [b/170475424](https://issuetracker.google.com/issues/170475424))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.material:material:1.0.0-alpha06`, `androidx.compose.material:material-icons-core:1.0.0-alpha06`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/material)

**API Changes**

- androidx.compose.foundation.Icon has been moved to androidx.compose.material.Icon. You can also use the Image component / Modifier.paint() with a Painter if you do not want to use the Material library. ([I9f622](https://android-review.googlesource.com/#/q/I9f6222326427cebacde10562cde99b9ebff2490f))
- Adds FloatingActionButtonElevation to represent elevation used by FABs in different states. See FloatingActionButtonConstants.defaultElevation() for the default implementation ([I2d4f5](https://android-review.googlesource.com/#/q/I2d4f59c6baf6d080dbc6ff3f95365a270727ebc3))
- Adds SwitchColors interface to represent colors used by a Switch in different states. See SwitchConstants.defaultColors to customize these colors. ([I93805](https://android-review.googlesource.com/#/q/I938059ed6a6279f99b66e892e7b6c9957fc16d6c))
- Adds ButtonElevation and ButtonColors interfaces to represent elevation and colors used by buttons in different states. See the default functions in ButtonConstants to customize these parameters. ([Ic5b7b](https://android-review.googlesource.com/#/q/Ic5b7b2f2ebe67b77fe96e5981f9bdee31dcafd0f))
- Adds RadioButtonColors interface to represent colors used by a RadioButton in different states. See RadioButtonConstants.defaultColors() to customize the colors used in different states. ([I74130](https://android-review.googlesource.com/#/q/I74130e122ab6432251d845937ee64524c233dbac))
- Adds CheckboxColors interface to represent colors used by a checkbox in different states. See CheckboxConstants.defaultColors() to customize the colors used in different states. ([I7dbdb](https://android-review.googlesource.com/#/q/I7dbdb42469e76deeaf921f49f3a178cca7d2865c))

**Bug Fixes**

- Material components do not set the elevation as zIndex anymore. Which means that within the same parent the child with larger shadow size will not be drawn on top of the child with the smaller one automatically. If you still need such behavior please set Modifier.zIndex() manually where needed ([I70417](https://android-review.googlesource.com/#/q/I704173218a6e049c215b33d5a71234e0eaba1c44), [b/170623932](https://issuetracker.google.com/issues/170623932))
- Deprecate VectorPainter in favor of rememberVectorPainter to better indicate that the composable API internally leverages 'remember' to persist data across compositions. ([Ifda43](https://android-review.googlesource.com/#/q/Ifda43dfd1d5b581c3666f4f69b528c47dbaa0ff5))
- Enable transitions in ComposeTestRule; remove option to enable the blinking cursor from ComposeTestRule. ([If0de3](https://android-review.googlesource.com/#/q/If0de36db743b7f57b161b0fe6324565750436866))
- Added single line keyboard option to CoreTextField ([I72e6d](https://android-review.googlesource.com/#/q/I72e6d9f84abbf4ff6a9ede5355de4c30d37c3d8c))
- Renamed Radius API to CornerRadius to better express how it is used throughout Compose. Updated documentation to indicate that negative corner radii are clamped to zero. ([I130c7](https://android-review.googlesource.com/#/q/I130c7e1baadaf1b2f8e6c32f1af0d3702e2cee50), [b/168762961](https://issuetracker.google.com/issues/168762961))
- Refactored DrawScope and ContentDrawScope to be interfaces instead of abstract classes
  - Created CanvasDrawScope implementation of DrawScope
  - Refactored implementations of DrawScope to use CanvasScope instead
  - Created DrawContext to wrap dependencies for DrawScope
  - Removed deprecated methods on DrawScope ([I56f5e](https://android-review.googlesource.com/#/q/I56f5e816116bea0d1337fbe0becc26b87694409b))
- Box was made an inline function. ([Ibce0c](https://android-review.googlesource.com/#/q/Ibce0c1940173f06c030fd1115b9badb692ceb05a), [b/155056091](https://issuetracker.google.com/issues/155056091))

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.material:material:1.0.0-alpha05`, `androidx.compose.material:material-icons-core:1.0.0-alpha05`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/material)

**API Changes**

- Popups and dialogs now inherit FLAG_SECURE from parent Window. Also added option to configure this explicitly ([I64966](https://android-review.googlesource.com/#/q/I649663482e91757df751315b03fee9867b580e96), [b/143778148](https://issuetracker.google.com/issues/143778148), [b/143778149](https://issuetracker.google.com/issues/143778149))
- Modifier.swipeable has 56.dp thresholds for states by default now ([Iab825](https://android-review.googlesource.com/#/q/Iab825eb19a13d9600aae2041ecd308851f530450), [b/168610267](https://issuetracker.google.com/issues/168610267))
- all scaffold states marked as @Stable. drawerGesturesEnabled in ScaffoldState moved to Scaffold itself. ([I36645](https://android-review.googlesource.com/#/q/I36645f82bea09908d0045593447f9b684a605fae), [b/168297016](https://issuetracker.google.com/issues/168297016))
- Removes nullable type from Scaffold lambda parameters, you can use emptyContent() to represent no content for a given parameter. ([I2b318](https://android-review.googlesource.com/#/q/I2b3181de9314b8b0dd48c30e2f663cddc0d62448), [b/157633857](https://issuetracker.google.com/issues/157633857), [b/158551084](https://issuetracker.google.com/issues/158551084))
- Deprecates contentColor() and currentTextStyle() APIs, and replaces them with AmbientContentColor and AmbientTextStyle ambients respectively. You can access the current value by using `.current` on the ambient property, as with any other ambient. This was change was made for consistency and to avoid having multiple ways to accomplish the same thing. Additionally renames some ambient properties to better describe their purpose as follows:

  - ContentColorAmbient -\> AmbientContentColor
  - TextStyleAmbient -\> AmbientTextStyle
  - IndicationAmbient -\> AmbientIndication
  - EmphasisAmbient -\> AmbientEmphasisLevels
  - RippleThemeAmbient -\> AmbientRippleTheme ([I37b6d](https://android-review.googlesource.com/#/q/I37b6dccb9751f2a9eb550f42da32bf4b1bff4296))
- Adds AmbientElevationOverlay, allowing customizing / disabling the default elevation overlay applied to Surfaces in dark theme. ([I5b74d](https://android-review.googlesource.com/#/q/I5b74d816ca8d8699e6e38a39579cb05451570cde))

**Bug Fixes**

- As part of the standardization of sentinel values for inline classes, rename Color.Unset to Color.Unspecified for consistency with other inline classes ([I97611](https://android-review.googlesource.com/#/q/I9761102e79ade32812984466c020f2715065ac85), [b/169797763](https://issuetracker.google.com/issues/169797763))
- TextOverflow.None is introduced. When overflow is None, Text won't handle overflow anymore, and it will report its actual size to LayoutNode. ([I175c9](https://android-review.googlesource.com/#/q/I175c9163a70ed35e4390b10848f143ed30ed2bf3), [b/158830170](https://issuetracker.google.com/issues/158830170))
- launchInComposition renamed to LaunchedTask to match Compose API guidelines ([I99a8e](https://android-review.googlesource.com/#/q/I99a8ef39b1e1abd7b9cae898863a35ed71b62e48))
- OnPositionedModifier is renamed to OnGloballyPositionedModifier and onPositioned() is renamed to onGloballyPositioned(). ([I587e8](https://android-review.googlesource.com/#/q/I587e8b151079d9d9506d86caa4283b7108958de4), [b/169083903](https://issuetracker.google.com/issues/169083903))

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.material:material:1.0.0-alpha04`, `androidx.compose.material:material-icons-core:1.0.0-alpha04`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/material)

> [!NOTE]
> **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

**API Changes**

- Exposes InteractionState parameters in stateful Material components, to allow hoisting the state and reading / controlling the state. ([Iaca5f](https://android-review.googlesource.com/#/q/Iaca5f65f8132a6f2b45d461001fa740d08b6bacb), [b/168025711](https://issuetracker.google.com/issues/168025711), [b/167164434](https://issuetracker.google.com/issues/167164434))
- Changes the `*color` parameters on RadioButton and TriStateCheckbox to allow fully customizing the colors used in each state, as well as changing how the colors animate between states if desired. See the new animateDefault\* color functions in CheckboxConstants and RadioButtonConstants for more information. ([I1c532](https://android-review.googlesource.com/#/q/I1c5327270119a2934265a342fd4303a476811c65))
- Renamed rememberBackdropState to rememberBackdropScaffoldState and added an additional param for the animation clock. Renamed the param backdropScaffoldState of BackdropScaffold to just scaffoldState. Renamed BackdropConstants to BackdropScaffoldConstants. ([Ib644d](https://android-review.googlesource.com/#/q/Ib644d5364cf8890ef0c637cc2ab1e0479db1eacb))
- Added experimental BottomSheetScaffold component. ([Ie02f0](https://android-review.googlesource.com/#/q/Ie02f03288c910fbfa6702a77342eb00917050ba2), [b/148996320](https://issuetracker.google.com/issues/148996320))
- Added experimental ModalBottomSheetLayout component. ([Ic209e](https://android-review.googlesource.com/#/q/Ic209e7e68e14afd3022a11846842cfbaa52a0812), [b/148996320](https://issuetracker.google.com/issues/148996320))
- Renames ButtonConstants/FloatingActionButtonConstants.defaultAnimatedElevation to defaultElevation, and now returns a Dp value instead of an AnimatedValue. ([I5f3ed](https://android-review.googlesource.com/#/q/I5f3ed41681092eb98896533f2f99047e2716cf61))

**Bug Fixes**

- Updated many Graphics APIs
  - Updated scale and rotation transformation APIs to consume a single Offset parameter to represent the pivot coordinate instead of separate float parameters for the x/y coordinates in DrawScope and DrawTransform
  - Removed Rect.expandToInclude and Rect.join methods
  - Updated Radius documentation to say oval in addition to elliptical
  - Added documentation to indicate the public constructor for the inline Radius class is not to be called directly but instead Radius objects should be instantiated through their function constructors
  - Removed RoundRect APIs to query topRight, bottomRight, bottomCenter, etc.
  - Deprecated Rect.shift in favor of Rect.translate
  - Removed RoundRect.grow and Rect.shrink APIs
  - Renamed RoundRect.outerRect to Rect.boundingRect
  - Removed RoundRect.middleRect/tallMiddleRect/wideMiddleRect and Rect.isStadium methods
  - Renamed RoundRect.longestSide to RoundRect.maxDimension
  - Renamed RoundRect.shortestSide to RoundRect.minDimension
  - Changed RoundRect.center to be a property instead of a function
  - Updated RoundRect constructor to consume Radius properties instead of individual parameters for x/y radius values
  - Removed Size APIs that assumed it was a Rectangle with origin at 0,0
  - Added a destructing API to Radius
  - Migrated various RoundRect extension functions to be properties instead
  - ([I8f5c7](https://android-review.googlesource.com/#/q/I8f5c738d1629b2cabd1b6e9fc8e8241dd06cfe2c), [b/168762961](https://issuetracker.google.com/issues/168762961))
- foundation.Box was deprecated. Please use foundation.layout.Box instead. ([Ie5950](https://android-review.googlesource.com/#/q/Ie59501cfd404c6bce53afee2d14dd95f1520d02c), [b/167680279](https://issuetracker.google.com/issues/167680279))
- Stack was renamed to Box. The previously existing Box will be deprecated in favor of the new Box in compose.foundation.layout. The behavior of the new Box is to stack children one on top of another when it has multiple children - this is different from the previous Box, which was behaving similar to a Column. ([I94893](https://android-review.googlesource.com/#/q/I94893bca003d7826c6a5b3c05ac3878d2f6bf953), [b/167680279](https://issuetracker.google.com/issues/167680279))
- Box decoration parameters have been deprecated. If you want to have decorations/padding on your box, use Modifiers instead (Modifier.background, Modifier.border, Modifier.padding) ([Ibae92](https://android-review.googlesource.com/#/q/Ibae92e99d0dd8984e666ece6cd6ec6f26f6ef672), [b/167680279](https://issuetracker.google.com/issues/167680279))
- Updated many Graphics APIs
  - Updated DrawScope APIs with scoped transformation methods to indicate that the transformation is only applied within the callback and removed after the callback is invoked
  - Updated clipPath documentation to refer to Path instead of rounded rectangle
  - Fixed spacing in documentation for right parameter in clipPath
  - Renamed DrawScope.drawCanvas to drawIntoCanvas and removed size parameter
  - Renamed dx/dy parameters in inset method to horizontal and vertical
  - Added inset overload that provides the same inset value to all 4 bounds
  - Removed documentation on inset method indicating that inset would be applied to all 4 sides
  - Updated documentation for Rect class
  - Updated comments on Rect parameters to match kdoc style
  - Removed Rect.join and Rect.expandToInclude
  - Created overload for Rect.translate(offset) and deprecated Rect.shift
  - ([If086a](https://android-review.googlesource.com/#/q/If086a1610e1bff12482897852d45cba075dcb4a1), [b/167737376](https://issuetracker.google.com/issues/167737376))
- We prevented static imports of contents of layout scopes (e.g. alignWithSiblings in RowScope). The explicit scope alternative should be used instead: `with(RowScope) { Modifier.alignWithSiblings(FirstBaseline) }`. ([I216be](https://android-review.googlesource.com/#/q/I216be6984d82e0a41432ac5b89f7d6240eef1b9d), [b/166760797](https://issuetracker.google.com/issues/166760797))

### Version 1.0.0-alpha03

September 16, 2020

`androidx.compose.material:material:1.0.0-alpha03`, `androidx.compose.material:material-icons-core:1.0.0-alpha03`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..18a5639262f8504db530176550e338a5d0e2e044/compose/material)

**API Changes**

- Renames`BottomNavigationItem`'s `onSelect` parameter to `onClick` ([I91925](https://android-review.googlesource.com/#/q/I919251069ab307d1ed5c1c3fbf5a01bf77a85047), [b/161809324](https://issuetracker.google.com/issues/161809324))
- Adds InteractionState parameter to BottomNavigationItem and Tab, allowing hoisting this state and adjusting how the component appears in different states. ([Ia3e9e](https://android-review.googlesource.com/#/q/Ia3e9ee1699a7d6eda38f4e62ce5a11d4ef616652), [b/168025711](https://issuetracker.google.com/issues/168025711))
- Removes `disabledBackgroundColor` and `disabledContentColor` parameters from buttons. You should instead use the new default color functions inside ButtonConstants. If you are already setting contentColor / backgroundColor explicitly, you should instead use these default functions and customize some / all of the parameters to avoid overwriting the color for both enabled / disabled states. ([If9b52](https://android-review.googlesource.com/#/q/If9b521ce01fe83ffc833fb340815120692abdd37))
- Textfield's background color does not implicitly apply transparency alpha anymore. Instead, any color provided through the backgroundColor parameter will be applied directly. ([Iecee9](https://android-review.googlesource.com/#/q/Iecee9f535b699acf684948fa99ec64217ea3f249), [b/167951441](https://issuetracker.google.com/issues/167951441))
- InnerPadding was renamed to PaddingValues. ([I195f1](https://android-review.googlesource.com/#/q/I195f122095b02ee49bf2ee0bc7f15f0339ca027f), [b/167389171](https://issuetracker.google.com/issues/167389171))
- The params `resistanceFactorAtMin` and `resistanceFactorAtMax` in `Modifier.swipeable` were replaced with a single resistance param. A new `defaultResistanceConfig` method was added in `SwipeableConstants`. ([I54238](https://android-review.googlesource.com/#/q/I54238306c8356145c8d03507ff20d79cfdab5707))
- Adds animated stateful elevation support for Button and FloatingActionButton. The elevation now animates between default and pressed states. To customize the elevation between states, please use `ButtonConstants.defaultAnimatedElevation()` and `FloatingActionButtonConstants.defaultAnimatedElevation()` instead of setting a flat Dp value in all cases. ([I37925](https://android-review.googlesource.com/#/q/I37925f16f21bc8d9e35732e003b8c535f3d284b3))
- Label became an optional parameter inside TextField and OutlinedTextField ([I267f6](https://android-review.googlesource.com/#/q/I267f6ada96a3371aaa99bdaa4007229ab7efddab), [b/162234081](https://issuetracker.google.com/issues/162234081))

**Bug Fixes**

- Global testing functions such as `onNode` or `waitForIdle` are now deprecated, please migrate to their new counterparts that are defined on ComposeTestRule ([I7f45a](https://android-review.googlesource.com/#/q/I7f45a41128160a0e67ad07e32a1ad49774602a97))
- DpConstraints and APIs using it were deprecated. ([I90cdb](https://android-review.googlesource.com/#/q/I90cdbe407ae8dd69badd26cd02bbb784ba10ba6a), [b/167389835](https://issuetracker.google.com/issues/167389835))
- The parameters minWidth and maxWidth of widthIn were renamed to min and max. Similarly for preferredWidthIn, heightIn, preferredHeightIn. ([I0e5e1](https://android-review.googlesource.com/#/q/I0e5e1405083224e747c54afcf7c5db5ec7472773), [b/167389544](https://issuetracker.google.com/issues/167389544))
- Remove scroll forward/backward semantics actions. Added steps in AccessibilityRangeInfo. ([Ia47b0](https://android-review.googlesource.com/#/q/Ia47b0be6d058f36b07d2141ec33aca634e63b544))
- Usages of gravity were consistently renamed to align or alignment in layout APIs. ([I2421a](https://android-review.googlesource.com/#/q/I2421a4d640a7086079739cd0e569aef70bb48577), [b/164077038](https://issuetracker.google.com/issues/164077038))
- Added onNode and other global methods on ComposeTestRule as the current global ones are going to be deprecated. ([Ieae36](https://android-review.googlesource.com/#/q/Ieae36a4b67a3190759e7284a638f8b755c06c1ec))
- Moved `createAndroidComposeRule` and `AndroidInputDispatcher` from `androidx.ui.test.android` to `androidx.ui.test` ([Idef08](https://android-review.googlesource.com/#/q/Idef08e5b796ba14140eafd054c8aa898a3d38feb), [b/164060572](https://issuetracker.google.com/issues/164060572))

### Version 1.0.0-alpha02

September 2, 2020

`androidx.compose.material:material:1.0.0-alpha02`, `androidx.compose.material:material-icons-core:1.0.0-alpha02`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/compose/material)

**API Changes**

- Added an experimental BackdropScaffold component. ([Iad908](https://android-review.googlesource.com/#/q/Iad908db4a93687c6dee6cc163721febfe4c814fc))

**Bug Fixes**

- Matrix4 was replaced with Matrix. All other parts of vectormath package have been removed. ([Ibd665](https://android-review.googlesource.com/#/q/Ibd66522490b861d85a7539176a4f105e20c31a66), [b/160140398](https://issuetracker.google.com/issues/160140398))

### Version 1.0.0-alpha01

August 26, 2020

`androidx.compose.material:material:1.0.0-alpha01`, `androidx.compose.material:material-icons-core:1.0.0-alpha01`, and `androidx.compose.material:material-icons-extended:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c93ac38a59f31e5db0eab67687532a4ba61913d5/ui/ui-material)

**Known Issue**

= The first character in a material `TextField` cannot be removed using a backspace ([b/165956313](https://issuetracker.google.com/165956313))

## Version 0.1.0-dev

### Version 0.1.0-dev17

August 19, 2020

`androidx.compose.material:material:0.1.0-dev17`, `androidx.compose.material:material-icons-core:0.1.0-dev17`, and `androidx.compose.material:material-icons-extended:0.1.0-dev17` are released. [Version 0.1.0-dev17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/ui/ui-material)

**API Changes**

- Previously deprecated RadioGroup and RadioGroupItems have been removed. Use Row and RadioBotton instead ([I381b7](https://android-review.googlesource.com/#/q/I381b71bbaf0092608a14743cdd2976de5d574824), [b/163806637](https://issuetracker.google.com/issues/163806637))
- Removed onFocusChanged callbacks from TextField. Use Modifier.focusObserver instead. ([I51089](https://android-review.googlesource.com/#/q/I51089bfbc858ea302770f92b13886818cf48ba9c), [b/161297615](https://issuetracker.google.com/issues/161297615))
- Modifier.drawBorder has been deprecated. Use Modifier.border instead. Border data class has been replaced by BorderStroke ([I4257d](https://android-review.googlesource.com/#/q/I4257d62b222e27c9ad67e1b2581b162cc9392c9e), [b/158160576](https://issuetracker.google.com/issues/158160576))
- Renamed some properties in SwipeableState: swipeTarget -\> targetValue, swipeProgress -\> progress, swipeDirection -\> direction. Added a rememberSwipeableState function for creating SwipeableStates. ([I2fc9c](https://android-review.googlesource.com/#/q/I2fc9c3af465b579a18359ae0aa0853c2d2b02abe), [b/163129614](https://issuetracker.google.com/issues/163129614), [b/163132293](https://issuetracker.google.com/issues/163132293))
- Snackbar support with positioning and proper queueing has been added. Access it via `SnackbarHostState.showSnackbar` suspend function. Additionally:
  - SnackbarHost components has been added. It hosts Snackbars based on the state and is responsible for transition between snackbars.
  - SnackbarHostState has been added to allow for control over snackbars, snackbars hosts and to decouple it from the ScaffoldState. you can access this state via `scaffoldState.snackbarHostState` as well.
  - Snackbar overload has been added to support common interface between snackbarHostState and snackbars itself. ([I79aaa](https://android-review.googlesource.com/#/q/I79aaae1deb410d6b1019a691a12a0ab861f6b03f))
- Adds enabled parameter to IconButton, and reorders parameters in IconToggleButton ([I0a941](https://android-review.googlesource.com/#/q/I0a9419b1a631cadad451395302ad87b7f9214f96), [b/161809385](https://issuetracker.google.com/issues/161809385), [b/161807956](https://issuetracker.google.com/issues/161807956))
- ListItem version with String-based API has been removed. Use slot version instead. ([Ib8f57](https://android-review.googlesource.com/#/q/Ib8f5742805f11b458db53b98a893c7fcb35eba00), [b/161804681](https://issuetracker.google.com/issues/161804681))
- Removed deprecated FilledTextField component. Please use TextField instead to get the Material Design implementation of the Filled text field. ([I5e889](https://android-review.googlesource.com/#/q/I5e88900375ee81067f24d39f82f4022bf85b3d9c))
- AlertDialog now uses FlowRow for buttons ([I00ec1](https://android-review.googlesource.com/#/q/I00ec1052c1e452380cda3a95bdb3ae5b74c5511e), [b/161809319](https://issuetracker.google.com/issues/161809319), [b/143682374](https://issuetracker.google.com/issues/143682374))
- Added params in Modifier.swipeable for changing the amount of resistance when swiping past the bounds. Removed \[min/max\]Value params. ([I93d98](https://android-review.googlesource.com/#/q/I93d98d2674798d39844f88dcef356cbbdb34458a))
- Added backgroundColor parameter to LinearProgressIndicator and removed internal padding from CircularProgressIndicator. Added new ProgressIndicatorConstants.DefaultProgressAnimationSpec which can be used as the default AnimationSpec when animating progress between values ([If38b5](https://android-review.googlesource.com/#/q/If38b5dd58d052b75c1974031e0974f22808d9776), [b/161809914](https://issuetracker.google.com/issues/161809914), [b/161804677](https://issuetracker.google.com/issues/161804677))
- Optional param velocityThreshold added to Modifier.swipeable. ([I698ba](https://android-review.googlesource.com/#/q/I698ba84bbb83ba262b8a55d9f70da4bff907eba9))
- bottomBarSize, fabSize and others and not available anymore in ScaffoldState. Use Modifier.onPosition instead on the component you'd like to know the size of. contentColor and Modifier pamateres have been added to Scaffold ([Ic6f7b](https://android-review.googlesource.com/#/q/Ic6f7bdd21d469227675b5e59a6b32c592c1ff9e5), [b/161811485](https://issuetracker.google.com/issues/161811485), [b/157174382](https://issuetracker.google.com/issues/157174382))
- Renames and reorders some parameters in Tab for consistency with other APIs ([Ia2d12](https://android-review.googlesource.com/#/q/Ia2d12aa787a9c8b829371070cd4379ae30049c7c), [b/161807532](https://issuetracker.google.com/issues/161807532))
- Splits TabRow into TabRow and ScrollableTabRow, removing isScrollable from TabRow. Also exposes edgePadding in ScrollableTabRow, which allows controlling the free space before / after the tabs. ([I583e8](https://android-review.googlesource.com/#/q/I583e82f0424571b538adbf6f3e8f69721c37352b), [b/161809544](https://issuetracker.google.com/issues/161809544))
- The `TabRow` object has been removed, replacing it with TabConstants. TabRow.TabPosition has moved to be top level (TabPosition), and indicatorContainer has been renamed to `indicator`. See the samples and documentation for detailed information on how to use the updated API, and defaults. ([I54d45](https://android-review.googlesource.com/#/q/I54d452697a70b9653812e5366420563a3aa19209), [b/161809544](https://issuetracker.google.com/issues/161809544))
- The thresholds param in Modifier.swipeable was tweaked; it now takes a pair of states (of type T) and returns the threshold between them in the form of a ThresholdConfig. A param dismissThresholds was added to SwipeToDismiss, which is a lambda (DismissDirection) -\> ThresholdConfig. ([Ie1080](https://android-review.googlesource.com/#/q/Ie1080e5a6a23459abab5cff1d292b326542cb62d))
- Slider has more colors for granular customization ([I73e64](https://android-review.googlesource.com/#/q/I73e647095847ac0dae744fd1d6407d2cf29418d4), [b/161810475](https://issuetracker.google.com/issues/161810475))
- Card's color param was renamed to backgroundColor ([I01fc1](https://android-review.googlesource.com/#/q/I01fc1d0aceae82f80663f4428a02fe6a0acbccc0), [b/161809546](https://issuetracker.google.com/issues/161809546))
- Snackbar has customizable background and content colors now ([I238f2](https://android-review.googlesource.com/#/q/I238f223914322fd47ad6c9707219075c45706c08), [b/161804381](https://issuetracker.google.com/issues/161804381))
- modifier, backgroundColor, contentColor and scrimColor customization params has been added to Drawers ([I23655](https://android-review.googlesource.com/#/q/I236555ff68b57685c4709ba24a6464e7fba0c10a), [b/161804378](https://issuetracker.google.com/issues/161804378))
- The `state { ... }` composable is now deprecated in favor of explicit calls to `remember { mutableStateOf(...) }` for clarity. This reduces the overall API surface and number of concepts for state management, and matches the `by mutableStateOf()` pattern for class property delegation. ([Ia5727](https://android-review.googlesource.com/#/q/Ia57278556d4f35ecf2cf5e6e30888b0d1f1f8012))
- Button's padding param was renamed to contentPadding ([Id252e](https://android-review.googlesource.com/#/q/Id252e03bd7750acf9acea72672d41b4f409ad1d0), [b/161809394](https://issuetracker.google.com/issues/161809394))
- Add an experimental material component SwipeToDismiss. ([I129e5](https://android-review.googlesource.com/#/q/I129e5ce937cf6eca5e4e12e6564db810da0cc902))

**Bug Fixes**

- Removed `onChildPositioned` and `OnChildPositionedModifier`. Developers should use `onPositioned` and `OnPositionedModifier` on the child layout instead. ([I4522e](https://android-review.googlesource.com/#/q/I4522e2cd4a0edb08fd36212eacf19d2895ae87f7), [b/162109766](https://issuetracker.google.com/issues/162109766))
- Added mergePolicy lambda to SemanticsPropertyKey. This can be used to define a custom policy for mergeAllDescendants semantics merging. The default policy is to use the parent value if already present, otherwise the child value. ([Iaf6c4](https://android-review.googlesource.com/#/q/Iaf6c4cc327017ee492f4d8334c8df5167d33df58), [b/161979921](https://issuetracker.google.com/issues/161979921))
- IntSize is now an inline class ([I2bf42](https://android-review.googlesource.com/#/q/I2bf426245b41f4189dead45114e3791bbceb9d13))
- `PlacementScope.placeAbsolute()` was renamed to `PlacementScope.place()`, and the previous `PlacementScope.place()` was renamed to `PlacementScope.placeRelative()`. As a result, the `PlacementScope.place()` method will not automatically mirror the position in right-to-left contexts anymore. If this is desired, use `PlacementScope.placeRelative()` instead. ([I873ac](https://android-review.googlesource.com/#/q/I873ac827e6c4d4bf6c85a80b7128174c61602945), [b/162916675](https://issuetracker.google.com/issues/162916675))
- Deprecated PxBounds in favor of Rect. Updated all usages of PxBounds with rect and added proper deprecate/replace with annotations to assist with the migration. ([I37038](https://android-review.googlesource.com/#/q/I370384202fff3e5b147d42086f4350ab7fa830de), [b/162627058](https://issuetracker.google.com/issues/162627058))
- Renamed RRect to RoundRect to better fit compose naming patterns Created similar function constructors to RRect and deprecated RRect function constructors ([I5d325](https://android-review.googlesource.com/#/q/I5d32529a133bc2f69ea1de94c2912b2748a0d678))

### Version 0.1.0-dev16

August 5, 2020

`androidx.compose.material:material:0.1.0-dev16`, `androidx.compose.material:material-icons-core:0.1.0-dev16`, and `androidx.compose.material:material-icons-extended:0.1.0-dev16` are released. [Version 0.1.0-dev16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c74ed7b07d1c18da576f179d55e568ca12973df..316f882e649c600372170f013a18515f590f490d/ui/ui-material)

**API Changes**

- Colors is now a final class instead of an interface. Instead of extending and providing a custom implementation, you should create a new ambient for your custom theme object, and access the theme object through the new ambient in your components, similar to how MaterialTheme works internally. ([Ibae84](https://android-review.googlesource.com/#/q/Ibae84078f839b3193f75b2983d17b585ac0e4719))
- Renamed ColorPalette to Colors, to better map to the Material color system and remove confusion over ColorPalette being a 'generic' theming object, as opposed to being a specific implementation of the Material color system. Additionally renames lightColorPalette and darkColorPalette to lightColors and darkColors respectively. ([I9e976](https://android-review.googlesource.com/#/q/I9e97690f51cb9eb0e51ff1a57d08f1911f179232), [b/161812111](https://issuetracker.google.com/issues/161812111))
- Renames BottomNavigationItem's `text` parameter to `label`, `onSelected` to `onSelect`, `activeColor` to `selectedContentColor`, `inactiveColor` to `unselectedContentColor` and updates parameter ordering to match guidelines. ([Icb605](https://android-review.googlesource.com/#/q/Icb605dac9b76a0204a2a9d675530da8897f817d5), [b/161809324](https://issuetracker.google.com/issues/161809324))
- `Modifier.stateDraggable` was completely reworked and renamed to Modifier.swipeable. A new SwipeableState class was introduced, and DrawerState and BottomDrawerState were refactored to inherit from it. \[Modal/Bottom\]DrawerLayout no longer takes an onStateChange parameter. ([I72332](https://android-review.googlesource.com/#/q/I7233229dfc9c04a4615f4c1cc29e604b97edd1df), [b/148023068](https://issuetracker.google.com/issues/148023068))
- foundation.shape.corner package were flatten to foundation.share ([I46491](https://android-review.googlesource.com/#/q/I464919cb74f8941c2a02f14dea0aa417febf3691), [b/161887429](https://issuetracker.google.com/issues/161887429))
- Added ExperimentalMaterialApi annotation. RippleTheme marked as Experimental ([Ic5fa0](https://android-review.googlesource.com/#/q/Ic5fa0382a2f4453e46e0793034d865e9182ec6ba), [b/161784800](https://issuetracker.google.com/issues/161784800))
- Material FilledTextField was renamed to TextField and foundational TextField was renamed to BaseTextField to make simplest desired API easy to discover and use ([Ia6242](https://android-review.googlesource.com/#/q/Ia62420a7a2231c02b6874a9a2867bf786a397ed3), [b/155482676](https://issuetracker.google.com/issues/155482676))

**Bug Fixes**

- OnChildPositioned has been deprecated. Use OnPositioned on the child instead. ([I87f95](https://android-review.googlesource.com/#/q/I87f95da597607cbc534647def3b1a39527dcdeaa), [b/162109766](https://issuetracker.google.com/issues/162109766))
- Address broad API fixes ([I077bc](https://android-review.googlesource.com/#/q/I077bcdc5c027e5dbe865d56f49420ce4a70a4e44))
  1. Remove unused OffsetBase interface
  2. Align Offset and IntOffset classes to have a consistent API surface
  3. Rename IntOffset.Origin to IntOffset.Zero to be consistent with Offset API
  4. Moved nativeCanvas method off of Canvas interface to support consumers to create their own Canvas instances
  5. Created stub EmptyCanvas class to refactor DrawScope to be a non-null parameter instead of lateinit and ensure non-nullability of the field
  6. Renamed ClipOp enums to be Pascal Case
  7. Renamed FilterQuality enums to be Pascal Case
  8. Renamed StrokeJoin enums to be Pascal Case
  9. Renamed PointMode enums to be Pascal Case
  10. Renamed PaintingStyle enums to be Pascal Case
  11. Renamed PathFillType enums to be Pascal Case
  12. Renamed StrokeCap enums to be Pascal Case
  13. Updated DrawCache implementation to no longer use lateinit params
  14. Updated DrawScope to no longer use lazy delegation for fillPaint and strokePaint internal parameters
  15. Updated Image composable to avoid Box usage for less overhead
  16. Updated Outline class to have @Immutable annotations
  17. Updated PathNode to have @Immutable annotations for each path instruction
  18. Updated Vector subcomposition to remove redundant conditional checks for equality as compose already handles them
  19. Deprecated Rect companion constructor methods in favor of function constructors
  20. Updated Brush classes and function constructors with @Immutable and @Stable APIs
  21. Updated VertexMode enum to be PascalCase
  22. Updated DrawScope selectPaint method to conditionally overwrite stroke parameters on the paint if they have changed
  23. Updated Size to add destructuring API, rename UnspecifiedSize to Unspecified and removed unused methods
- Move dialog to ui ([I47fa6](https://android-review.googlesource.com/#/q/I47fa618a788e598182b782eab755defccaf45ebb))
- Removed `SemanticsNodeInteraction.performPartialGesture`. Use `SemanticsNodeInteraction.performGesture` instead. ([Id9b62](https://android-review.googlesource.com/#/q/Id9b628ebe475c8a067118320b26a7b2461e98129))
- Renamed `SemanticsNodeInteraction.getBoundsInRoot()` to `SemanticsNodeInteraction.getUnclippedBoundsInRoot()` ([Icafdf](https://android-review.googlesource.com/#/q/Icafdf63b2e2f03f48d5b51371e733917dedcf422), [b/161336532](https://issuetracker.google.com/issues/161336532))
- The APIs for right-to-left support has been updated. LayoutDirectionAmbient has been added, which can be used to read and change the layout direction. Modifier.rtl and Modifier.ltr have been removed. ([I080b3](https://android-review.googlesource.com/#/q/I080b3cb674dc32af5fbe7e696228ac21f0720d72))
- Modifier.deternimateProgress has been renamed to Modifier.progressSemantics ([I9c0b4](https://android-review.googlesource.com/#/q/I9c0b48e0b7969a842a114b50c86d8c37799ede1d))
- Updates material-icons-extended with the latest icons added to Material.io/icons ([I4b1d3](https://android-review.googlesource.com/#/q/I4b1d3e58c07aacdcd0c700621db51f45232e8031))
- Require type T to be explicitly specified for transitionDefinition. ([I1aded](https://android-review.googlesource.com/#/q/I1adedb34525ebb8c079a77a9af2636f1cb8339f7))
- Modifier.plus has been deprecated, use Modifier.then instead. 'Then' has a stronger signal of ordering, while also prohibits to type `Modifier.padding().background() + anotherModifier`, which breaks the chain and harder to read ([Iedd58](https://android-review.googlesource.com/#/q/Iedd587edbed0ba964ef203a66b98be7297147bd7), [b/161529964](https://issuetracker.google.com/issues/161529964))
- Renamed AndroidComposeTestRule to createAndroidComposeRule. ([I70aaf](https://android-review.googlesource.com/#/q/I70aaf550e1bff2871b9732cc5abf58e9af1479fe))
- Add isFocused() and isNotFocused() SemanticsMatcher. ([I0b760](https://android-review.googlesource.com/#/q/I0b760d316a616ab385fa421b080edefee8e27681))
- Removed `BaseGestureScope.globalBounds`, which shouldn't be used from tests. Use coordinates local to the node with which you're interacting instead. ([Ie9b08](https://android-review.googlesource.com/#/q/Ie9b089d62f41b7ffd1ad5a8f8e3f173d68069b7b))
- Fixed popup position on cut-out displays. ([Idd7dd](https://android-review.googlesource.com/#/q/Idd7ddf5f88728a96fc8ff725a39979fe962e8889))
- Modifier.drawBackground has been renamed to Modifier.background ([I13677](https://android-review.googlesource.com/#/q/I1367723fce0e07418ed4ab391fe20c69aa092f53))

### Version 0.1.0-dev15

July 22, 2020

`androidx.compose.material:material:0.1.0-dev15`, `androidx.compose.material:material-icons-core:0.1.0-dev15`, and `androidx.compose.material:material-icons-extended:0.1.0-dev15` are released. [Version 0.1.0-dev15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/ui/ui-material)

#### Dependencies Update

- To use the `0.1.0-dev15` version of Compose, you will need to update your dependencies according to the new code snippets shown above in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose-material#declaring_dependencies).

**API Changes**

- `@Model` annotation is now deprecated. Use state and mutableStateOf as alternatives. This deprecation decision was reached after much careful discussion.

  #### Justification

  Rationale includes but is not limited to:
  - Reduces API surface area and concepts we need to teach
  - More closely aligns with other comparable toolkits (Swift UI, React, Flutter)
  - Reversible decision. We can always bring `@Model` back later.
  - Removes corner-case usage and difficult to answer questions about configuring `@Model` as things we need to handle
  - `@Model` data classes, equals, hashcode, etc.
  - How do I have some properties "observed" and others not?
  - How do I specify structural vs. referential equality to be used in observation?
  - Reduces "magic" in the system. Would reduce the likelihood of someone assuming system was smarter than it is (ie, it knowing how to diff a list)
  - Makes the granularity of observation more intuitive.
  - Improves refactorability from variable -\> property on class
  - Potentially opens up possibilities to do hand-crafted State-specific optimizations
  - More closely aligns with the rest of the ecosystem and reduces ambiguity towards immutable or us "embracing mutable state"

  #### Migration Notes

  Almost all existing usages of `@Model` are fairly trivially transformed in one of two ways. The example below has a `@Model` class with two properties just for the sake of example, and has it being used in a composable.

      @Model class Position(
       var x: Int,
       var y: Int
      )

      @Composable fun Example() {
       var p = remember { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p.x = it }
         onYChange={ p.y = it }
       )
      }

  #### Alternative 1: Use `State<OriginalClass>` and create copies.

  This approach is made easier with Kotlin's data classes. Essentially, make all previously `var` properties into `val` properties of a data class, and then use `state` instead of `remember`, and assign the state value to cloned copies of the original using the data class `copy(...)` convenience method.

  It's important to note that this approach only works when the only mutations to that class were done in the same scope that the `State` instance is created. If the class is internally mutating itself outside of the scope of usage, and you are relying on the observation of that, then the next approach is the one you will want to use.

      data class Position(
       val x: Int,
       val y: Int
      )

      @Composable fun Example() {
       var p by state { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p = p.copy(x=it) }
         onYChange={ p = p.copy(y=it) }
       )
      }

  #### Alternative 2: Use mutableStateOf and property delegates

  This approach is made easier with Kotlin's property delegates and the `mutableStateOf` API which allows you to create MutableState instances outside of composition. Essentially, replace all `var` properties of the original class with `var` properties with `mutableStateOf` as their property delegate. This has the advantage that the usage of the class will not change at all, only the internal implementation of it. The behavior is not completely identical to the original example though, as each property is now observed/subscribed to individually, so the recompositions you see after this refactor could be more narrow (a good thing).

      class Position(x: Int, y: Int) {
       var x by mutableStateOf(x)
       var y by mutableStateOf(y)
      }

      // source of Example is identical to original
      @Composable fun Example() {
       var p = remember { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p.x = it }
         onYChange={ p.y = it }
       )
      }

  ([I409e8](https://android-review.googlesource.com/#/q/I409e8c158841eae1dd548b33f1ec80bb609cba31), [b/152050010](https://issuetracker.google.com/issues/152050010), [b/146362815](https://issuetracker.google.com/issues/146362815), [b/146342522](https://issuetracker.google.com/issues/146342522), [b/143413369](https://issuetracker.google.com/issues/143413369), [b/135715219](https://issuetracker.google.com/issues/135715219), [b/143263925](https://issuetracker.google.com/issues/143263925), [b/139653744](https://issuetracker.google.com/issues/139653744))
- onFocusChange callback in text fields renamed to onFocusChanged ([Ida4a1](https://android-review.googlesource.com/#/q/Ida4a1a55e5a9119c3a740d28ad2e0d9126d40853))

- Added thresholds param in stateDraggable to specify thresholds
  between anchors. This was used to set a 56dp threshold in bottom drawer.
  Also BottomDrawerLayout now uses a separate BottomDrawerState enum. ([I533fa](https://android-review.googlesource.com/#/q/I533fad3d3bf9b95f702156e321aa15a84e81819b))

- Removes previously deprecated Modifier.ripple. Clickable now uses ripple as the default indication (if you have a MaterialTheme {} set in your application) so in most cases you can just use clickable and get ripple indication for free. If you need to customize the color / size / bounded parameter for the ripple, you can manually create a RippleIndication and pass it to clickable as the indication parameter. ([I663b2](https://android-review.googlesource.com/#/q/I663b2fcbdc3079343b54dcf713f5d467e39b87a5), [b/155375067](https://issuetracker.google.com/issues/155375067))

- Removed deprecated override of FilledTextField composable ([I7f8f8](https://android-review.googlesource.com/#/q/I7f8f867bb10329f5b1dbadc0a512456c40f5eaef))

- Rename Button object (containing the defaults used by Button function) to ButtonConstants ([I7c5f7](https://android-review.googlesource.com/#/q/I7c5f7d864984502bc477c3d42896f052b25c1db3), [b/159687878](https://issuetracker.google.com/issues/159687878))

- Button's content slot now behaves as Row (useful when you need to have an icon with a text, see samples on Button how to write it) ([I0ff10](https://android-review.googlesource.com/#/q/I0ff10603b1a290a8f9b0c27988008572ecf0927a), [b/158677863](https://issuetracker.google.com/issues/158677863))

- RadioGroup and RadioGroupItem have been deprecated. Use Box with Modifier.selectable, Row and Column to make proper set of radioButton choices by your design ([I7f5cf](https://android-review.googlesource.com/#/q/I7f5cf83c411fe9ad21eecf211544b868bac17fb5), [b/149528535](https://issuetracker.google.com/issues/149528535))

- Added Material Outlined Textfield ([I1a518](https://android-review.googlesource.com/#/q/I1a518ccda1cb0873ceb1f0a850b2156a9709bf3a))

- androidx.ui.foundation.TextFieldValue and
  androidx.ui.input.EditorValue is deprecated. TextField,
  FilledTextField and CoreTextField composables that uses
  that type is also deprecated. Please use
  androidx.ui.input.TextFieldValue instead ([I4066d](https://android-review.googlesource.com/#/q/I4066d1f4d2e3e3514753aa3495680292dc55f89d), [b/155211005](https://issuetracker.google.com/issues/155211005))

- TabRow.TabPosition not contains position in Dp, not in IntPx ([I34a07](https://android-review.googlesource.com/#/q/I34a07faef2f00f46ea6a38903d635d939bf06879), [b/158577776](https://issuetracker.google.com/issues/158577776))

- Replaced usage of IntPx with Int. Replaced IntPxPosition
  with IntOffset. Replaced IntPxSize with IntSize. ([Ib7b44](https://android-review.googlesource.com/#/q/Ib7b44d92ce3aff86c606753f0ac5c3122b71041d))

- In order to consolidate the
  number of classes used to represent
  sizing information, standardize
  on usage of the Size class instead
  of PxSize. This provides the benefits
  of an inline class to leverage a long
  to pack 2 float values to represent
  width and height represented as floats. ([Ic0191](https://android-review.googlesource.com/#/q/Ic019171b52d2f24d262d9c47ac964728cdc1ee8b))

- Deprecates Modifier.ripple. Clickable now uses ripple as the default indication (if you have a MaterialTheme {} set in your application) so in most cases you can just use clickable and get ripple indication for free. If you need to customize the color / size / bounded parameter for the ripple, you can manually create a RippleIndication and pass it to clickable as the indication parameter. ([I101cd](https://android-review.googlesource.com/#/q/I101cd0adac4e1f466f84a35c1b3f2db1e7a69472), [b/155375067](https://issuetracker.google.com/issues/155375067))

- Scaffold API has been reworked: few parameters changed their name, added new parameters for better customization. Added getter to query sizes of Fab, TopBar and BottomBar ([I0e7ce](https://android-review.googlesource.com/#/q/I0e7ce733b83235d9b6970ea5f014026fe9fd1445))

- Added the DropdownMenu component in ui-material, a Material Design menu implementation. ([I9bb3d](https://android-review.googlesource.com/#/q/I9bb3d43fc1bb60cd0fed933c76b9d58cc5211514))

- Allow to show/hide software keyboard manually using SoftwareKeyboardController ([Ifb9d6](https://android-review.googlesource.com/#/q/Ifb9d6b63534b4e71121bbd983a56217da40d7978), [b/155427736](https://issuetracker.google.com/issues/155427736))

- Modifier.indication has been added to foundation package. Use it to show press/drag/other indication on your custom interactable elements ([I8425f](https://android-review.googlesource.com/#/q/I8425fc70afc4d2815f937f8514352ce831e692ae), [b/155287131](https://issuetracker.google.com/issues/155287131))

- Consolidated CanvasScope implementations
  so there is now just DrawScope and
  ContentDrawScope
  Renamed CanvasScope to DrawScope.
  Updated DrawScope to implement Density
  interface and provide LayoutDirection
  Deleted DrawScope subclass in ContentDrawScope
  Painter and PainterModifier have been updated
  to no longer maintain an RTL property
  themselves as DrawScope provides this already
  without manually providing it ([I1798e](https://android-review.googlesource.com/#/q/I1798e4b2b325297c3b5394aa99be3db935e369b7))

- Renames Emphasis.emphasize() to Emphasis.applyEmphasis() ([Iceebe](https://android-review.googlesource.com/#/q/Iceebe99ae74631527855c108ca06a13da366f762))

- Disabled buttons now visually follows the Material Design specification ([I47dcb](https://android-review.googlesource.com/#/q/I47dcb49c2306b497f2166b621a00d8a2896795e3), [b/155076924](https://issuetracker.google.com/issues/155076924))

- FilledTextField gets ime action, visual transformation and keyboard type support ([I1f9cf](https://android-review.googlesource.com/#/q/I1f9cf5c9eecaeb6530e01bf1fe900bb21ecb0256), [b/155075201](https://issuetracker.google.com/issues/155075201))

- Adds strokeWidth parameter to CircularProgressIndicator to customize the stroke size. To change the stroke size (height) of a LinearProgressIndicator, you can use Modifier.preferredHeight() or another size modifier. ([Icea16](https://android-review.googlesource.com/#/q/Icea1609a1dd22cd9becf2b0ed96830c1ea752eab), [b/154919081](https://issuetracker.google.com/issues/154919081))

- Adds strokeWidth parameter to CircularProgressIndicator to customize the stroke size. To change the stroke size (height) of a LinearProgressIndicator, you can use Modifier.preferredHeight() or another size modifier. ([Icea16](https://android-review.googlesource.com/#/q/Icea1609a1dd22cd9becf2b0ed96830c1ea752eab), [b/154919081](https://issuetracker.google.com/issues/154919081))

- Added slot API for trailing and leading icons in the FilledTextField and handling of the error state ([Ic12e0](https://android-review.googlesource.com/#/q/Ic12e06c1c3338255dca78d409401021d5a4f6f48))

- FAB's and Extended FAB's default color has been changed to MaterialTheme.colors.secondary. ([I3b9b9](https://android-review.googlesource.com/#/q/I3b9b9ddcc0a8aeaf8862cc79e648e48b75ea5956), [b/154118816](https://issuetracker.google.com/issues/154118816))

- Replaced all nullable Color uses in API with
  non-nullable and use Color.Unset instead of null ([Iabaa7](https://android-review.googlesource.com/#/q/Iabaa7c6334857833cdb0d5958f062e2e576bd240))

- Renamed EdgeInsets to InnerPadding. Renamed innerPadding parameter of Material Buttons to paddding. ([I66165](https://android-review.googlesource.com/#/q/I66165851232da7635a34b6bb3af7ef8dc38e3e3d))

- Slider is now stateless. Users will need to pass and update state by themselves, just like in any other control. ([Ia00aa](https://android-review.googlesource.com/#/q/Ia00aa9ced51252190589e47ea928a94bd3c5555a))

- StaticDrawer was removed. If you need it, use Box with material-spec'ed width instead ([I244a7](https://android-review.googlesource.com/#/q/I244a7e7878e8cf443c008464229fdeb9a3c24e0f))

- Added Material Design implementation of Filled Text Field ([Ic75cd](https://android-review.googlesource.com/#/q/Ic75cd8de3fab1dbc253d7dd63c20ca1dda358688))

- Added modifier param to ListItem and reordered params to
  promote trailing lambda body ([I66e21](https://android-review.googlesource.com/#/q/I66e21cd6fd955a11663e17d9fab863caaa67d053))

- Adds defaultFontFamily constructor parameter to Typography, allowing specifying the default font family that will be used for any provided TextStyles that do not have a family set. ([I89d07](https://android-review.googlesource.com/#/q/I89d07c0730ab21464824754d2f2d17770d6bbdb9))

- Temporarily removed Material Data Tables from the API surface. ([Iaea61](https://android-review.googlesource.com/#/q/Iaea6140fa9946b81da4d0cda10d172073a4edb1c))

- Renamed paramaters in Divider composable ([Ic4373](https://android-review.googlesource.com/#/q/Ic4373753b3d13cf17e434a645c47d0a8350610b8))

- children ([Ia6d19](https://android-review.googlesource.com/#/q/Ia6d19fb822f29f13d774ca84777713e3b45b0cbd))

- Removes MaterialTheme.emphasisLevels, instead use EmphasisAmbient.current to retrieve the emphasis levels ([Ib5e40](https://android-review.googlesource.com/#/q/Ib5e40c2d26737829a80ec16b390b125b570e5cbb))

- Shape theming system is updated according to the Material design specification. Now you can provide small, medium and large shapes to be used by most of the components ([Ifb4d1](https://android-review.googlesource.com/#/q/Ifb4d152de62f71c6b1759c73702752673aa27c7d))

- Changed MaterialTheme APIs such as MaterialTheme.colors(), MaterialTheme.typography() to be properties instead of functions. Remove parentheses from existing calls, no behavioral change is expected. ([I3565a](https://android-review.googlesource.com/#/q/I3565ae6a3a08d4d329a4fdcb68360fe1bbf8617c))

- Refactored FloatingActionButton APIs to accept composable
  lambdas instead of primitives. See updated samples for usage
  information. ([I00622](https://android-review.googlesource.com/#/q/I0062288bd79e894f542d53882ae125404dd29ae2))

- add `enabled` param to Checkbox, Switch and Toggleable ([I41c16](https://android-review.googlesource.com/#/q/I41c1634c860ab068308d33d7e1a0547ad79adbdb))

- Ripple is now a Modifier. While Clickable is not yet converted the recommended usage is `Clickable(onClick = { ... }, modifier = ripple())` ([Ie5200](https://android-review.googlesource.com/#/q/Ie52007f6948838a64fb25dba4dfbb7853d0e442f), [b/151331852](https://issuetracker.google.com/issues/151331852), [b/150060763](https://issuetracker.google.com/issues/150060763))

- Surface and Card were moved from androidx.ui.material.surface to androidx.ui.material ([I88a6d](https://android-review.googlesource.com/#/q/I88a6d868983cf34b5d1f79ceedf04f8f47c87c6a), [b/150863888](https://issuetracker.google.com/issues/150863888))

- Button, FloatingActionButton and Clickable now have a separate `enabled` param. Some of the params on Button were renamed or reordered. ([I54b5a](https://android-review.googlesource.com/#/q/I54b5ac613632c1cd804b756d3ad2ccb7a475a149))

- Renamed Image to ImageAsset to better differentiate the difference between the Image data and the upcoming Image composable used to participate in layout and draw content.
  _Body:Created extension method on android.graphics.Bitmap,
  Bitmap.asImageAsset(), to create an instance of an
  ImageAsset useful for combining traditional Android
  application development with the compose framework ([Id5bbd](https://android-review.googlesource.com/#/q/Id5bbdf3fe1cf68750a76bb955b20e06d1f81a71e))

- Removed Snackbar API with String parameters in favour of using
  the overload that accepts composable lambdas. See updated samples for
  usage information ([I55f80](https://android-review.googlesource.com/#/q/I55f800021b13a2611b8846b31bf4ca24f34830fa))

- Refactored Tab APIs to accept `text` and `icon` lambdas, ([Ia057e](https://android-review.googlesource.com/#/q/Ia057e449977c4115ae6d564fdad341562030351e))

- Added BottomNavigation component, see the docs and samples for
  usage information ([I731a0](https://android-review.googlesource.com/#/q/I731a0730a9e889192fc520cd3f511ec4661866dc))

- Added Icon, IconButton and IconToggleButton, removing AppBarIcon.
  You can directly replace existing usages of AppBarIcon with IconButton,
  and they will now have the correct touch target. See the samples for
  usage information, and see Icons for the provided Material Icons
  you can use directly with these components. ([I96849](https://android-review.googlesource.com/#/q/I9684914dcde197df74d11f1173d827cd902e8832))

- Replaced ButtonStyle with distinct functions and removed text (string) overload. See updated samples for usage information. ([If63ab](https://android-review.googlesource.com/#/q/If63ab32bd3f12050a2d2f4b8c0cb044bc7144a6b), [b/146478620](https://issuetracker.google.com/issues/146478620), [b/146482131](https://issuetracker.google.com/issues/146482131))

- rename `Border` modifier to `DrawBorder` ([I8ffcc](https://android-review.googlesource.com/#/q/I8ffccaa928e74efd71dcdcda550f250195f2e5d3))

- LayoutCoordinates no longer has a position property. The
  position property does not make sense when considering LayoutModifiers,
  rotation, or scaling. Instead, developers should use parentCoordinates
  and childToLocal() to calculate the transform from one
  LayoutCoordinate to another.

  LayoutCoordinates uses IntPxSize for the size property instead of
  PxSize. Layouts use integer pixel sizes for layouts, so all layout sizes
  should use integers and not floating point values. ([I9367b](https://android-review.googlesource.com/#/q/I9367be21c2c202c8b6ad889b50a29454773f41af))
- Breaking changes to the ambients API. See log and `Ambient<T>` documentation for details ([I4c7ee](https://android-review.googlesource.com/#/q/I4c7eea45f2b7bf41f8a8ba75fd667c06010469a9), [b/143769776](https://issuetracker.google.com/issues/143769776))

- Scaffold material component has been added. Scaffold implements ([I7731b](https://android-review.googlesource.com/#/q/I7731b4e0f0a5238176640d5a40431c5bf98185d2))

- Replaced DrawBorder in favor of Border Modifier ([Id335a](https://android-review.googlesource.com/#/q/Id335a8c2526693f8eb9d440c8d25341029f5de89))

**Bug Fixes**

- FocusModifier is deprecated in favor of Modifier.focus, Modifier.focusRequester, Modifier.focusObserver. FocusState and FocusDetailedState are deprecated in favor of FocusState2 ([I46919](https://android-review.googlesource.com/#/q/I469196b76ebe08130fa4df9ed297f111abddd8b1), [b/160822875](https://issuetracker.google.com/issues/160822875), [b/160922136](https://issuetracker.google.com/issues/160922136))
- VerticalScroller and HoriziontalScroller have been deprecated. Use ScrollableColumn and ScrollableRow for build-in experience with Column/Row behaviour and parameters, or Modifier.verticalScroll and Modifier.horizontalScroll on your own element. Similarly, ScrollerPosition has been deprecated in favor of ScrollState' ([I400ce](https://android-review.googlesource.com/#/q/I400ce0e6c0e33aa865e0e49defef1eb92ac40a93), [b/157225838](https://issuetracker.google.com/issues/157225838), [b/149460415](https://issuetracker.google.com/issues/149460415), [b/154105299](https://issuetracker.google.com/issues/154105299))
- Modifier.draggable and Modifier.scrollable APIs were reworked. DragDirection was removed in favor of Orientation. State required for scrollable has beed simplified. ScrollableState has been renamed to ScrollableController ([Iab63c](https://android-review.googlesource.com/#/q/Iab63cb65002471a5173f387f7bc6720aa929f9e6), [b/149460415](https://issuetracker.google.com/issues/149460415))
- `runOnIdleCompose` renamed to `runOnIdle` ([I83607](https://android-review.googlesource.com/#/q/I836071f1c3c63d21417a531f336f8a93ca13f9ed))
- Single-value semantics properties now use a calling style. For example, 'semantics { hidden = true }' is now written as: 'semantics { hidden() }'. ([Ic1afd](https://android-review.googlesource.com/#/q/Ic1afd12ea22c926babc9662f1804d80b33aa0cfc), [b/145951226](https://issuetracker.google.com/issues/145951226), [b/145955412](https://issuetracker.google.com/issues/145955412))
- Several testing APIs were renamed to be more intuitive. All findXYZ APIs were renamed to onNodeXYZ. All doXYZ APIs were renamed to performXYZ. ([I7f164](https://android-review.googlesource.com/#/q/I7f164b42b04196f023c4a2153d66825487998de4))
- Transition API has been changed to return a TransitionState instead of passing the TransitionState to children. This makes the API more consistent with animate() APIs. ([I24e38](https://android-review.googlesource.com/#/q/I24e38fea3bf299e47d87dc5d2b42991e03d6786c))
- An IntBounds unit class has been added, representing integer pixel bounds from layout. The API of PopupPositionProvider has been updated to use it. ([I0d8d0](https://android-review.googlesource.com/#/q/I0d8d03c5535c80c6808d8f9ca7a210408890e6e7), [b/159596546](https://issuetracker.google.com/issues/159596546))
- A new optional flag useUnmergedTree was added to test finders. ([I2ce48](https://android-review.googlesource.com/#/q/I2ce48556aa3b0a0c73f4a56a0d9eed63eda49160))
- Removed obsolete size testing APIs. ([Iba0a0](https://android-review.googlesource.com/#/q/Iba0a086e8c88cf44684cba56766792614201ba30))
- Removed Shader inline class that wrapped the NativeShader expect class Renamed NativeShader to Shader. The wrapped Shader inline class did not add anything valuable to the API surface and was an inline class, so use the NativeShader class directly. ([I25e4d](https://android-review.googlesource.com/#/q/I25e4db3d4f59899b6a7c59613e49ed093e76da2f))
- Popups, Dialogs and Menus are now inheriting the contextual MaterialTheme ([Ia3665](https://android-review.googlesource.com/#/q/Ia3665905218b4d12d7a9bd121a69a51569d82694), [b/156527485](https://issuetracker.google.com/issues/156527485))
- Material DropdownMenu are now scrollable. ([Ide699](https://android-review.googlesource.com/#/q/Ide6991aae11c05c5ebc6b193eede567c4fcae77e))
- Removed layout direction parameter from the measure block of the Layout() function. Layout direction is however available inside the callback through the measure scope object ([Ic7d9d](https://android-review.googlesource.com/#/q/Ic7d9d797938e6e2a91916836e5e9688794115c22))
- Use AnimationSpec instead of AnimationBuilder in the top level APIs to clarify the concept of static animation specification -Improve the transition DSL by removing the lambda requirement for creating AnimationSpecs such as tween, spring. They instead take constructor params directly. -Improve the overall ease of use of AnimationSpec opening up constructors instead of relying on builders -Change the duration and delay for KeyFrames and Tween to Int. This eliminates unnecessary type casts and method overloading (for supporting both Long and Int). ([Ica0b4](https://android-review.googlesource.com/#/q/Ica0b4cb42996d3d30f9b6dacdbe149c75af77341))
- Switch now appears in a disabled state when `enabled` is set to false ([If4624](https://android-review.googlesource.com/#/q/If46244d35274f24d3713422c8d28b5b870fb8c84), [b/155941869](https://issuetracker.google.com/issues/155941869), [b/159331694](https://issuetracker.google.com/issues/159331694))
- Modifier.tag was renamed to Modifier.layoutId, to avoid confusion with Modifier.testTag. ([I995f0](https://android-review.googlesource.com/#/q/I995f09d0722964ad8a5708c7299e4c6f52bec1c5))
- Alignment line Int positions returned from Placeable#get(AlignmentLine) are now non-null. If the queried alignment line is missing, AlignmentLine.Unspecified will be returned. ([I896c5](https://android-review.googlesource.com/#/q/I896c5ef8a18919aa84413669341e716bf676e32e), [b/158134875](https://issuetracker.google.com/issues/158134875))
- Refactored Radius class to be an
  inline class. Removed companion creation
  methods in favor of function constructor
  with default parameter to have the radius
  along the y-axis match that of the mandatory
  x-axis radius parameter.

  Updated DrawScope.drawRoundRect to consume
  a single Radius parameter instead of 2 separate
  float values for the radius along the x and y
  axis ([I46d1b](https://android-review.googlesource.com/#/q/I46d1b6c89a0f738304c915ce7ee52b621e10302f))
- In order to consolidate the
  number of classes used to represent
  positioning information, standardize
  on usage of the Offset class instead
  of PxPosition. This provides the benefits
  of an inline class to leverage a long
  to pack 2 float values to represent x
  and y offsets represented as floats. ([I3ad98](https://android-review.googlesource.com/#/q/I3ad983207bc37af20afac03e2cd09b4240777687))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters.
  Deleted Px class in its entirety ([I3ff33](https://android-review.googlesource.com/#/q/I3ff339371abd6fb622172d060a70d12dda4822e0))

- Toggleable component has been deprecated. Use Modifier.toggleable instead ([I35220](https://android-review.googlesource.com/#/q/I35220fca0d9d11198d1158cb905cfb2586965a34), [b/157642842](https://issuetracker.google.com/issues/157642842))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I086f4](https://android-review.googlesource.com/#/q/I086f4744d1eb51f0f31356e36991c2a8d4433059))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([Id3434](https://android-review.googlesource.com/#/q/Id343458210b56a9a4cdae4ef3d0f97ea79004942))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I97a5a](https://android-review.googlesource.com/#/q/I97a5af412d913a53e5ff575bbf685f007d25c0d6))

- Fixed onClick not being invoked for DropdonMenuItems. ([I3998b](https://android-review.googlesource.com/#/q/I3998b374f4ad047c5a24521b5d3ba928be2e3e69), [b/157673259](https://issuetracker.google.com/issues/157673259))

- MutuallyExclusiveSetItem has been deprecated. Use Modifier.selectable instead. ([I02b47](https://android-review.googlesource.com/#/q/I02b473710e5a654427b51565c0b950392f68fcff), [b/157642842](https://issuetracker.google.com/issues/157642842))

- TestTag is now deprecated. Use Modifier.testTag instead. ([If5110](https://android-review.googlesource.com/#/q/If5110df5865f5933d10d54a8aacba58f8cd1c712), [b/157173105](https://issuetracker.google.com/issues/157173105))

- TextField's cursor has a blinking animation ([Id10a7](https://android-review.googlesource.com/#/q/Id10a71f42f66fae532cca35ec132bcc35a4bc660))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I19d02](https://android-review.googlesource.com/#/q/I19d02beca10c30e9b6b444be0c2dd21227e30e9c))

- VerticalScroller now provides Column out of the box. HorizontalScroller now provides Row out of the box. ([Ieca5d](https://android-review.googlesource.com/#/q/Ieca5d185b9f6e950a7175b9daa7a9a511a439da2), [b/157020670](https://issuetracker.google.com/issues/157020670))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([Iede0b](https://android-review.googlesource.com/#/q/Iede0b310a8a8f4a39ba6ae4a99c753f7f590d8ed))

- Modifier.semantics has been undeprecated to allow usages for high level components. ([I4cfdc](https://android-review.googlesource.com/#/q/I4cfdc837d5ac2d240af5a5ac6b755aebf800af15))

- DrawLayer modifiers api has been changed: outlineShape renamed to shape and has the RectangleShape default value and now non-nullable; clipToOutline renamed to clip; clipToBounds removed as it is the same as clip == true with RectangleShape ([I7ef11](https://android-review.googlesource.com/#/q/I7ef1155f6a1d93c41a98411f9e4632c4e18956e1), [b/155075735](https://issuetracker.google.com/issues/155075735))

- Updated higher level
  compose APIs that expose a Canvas to
  expose CanvasScope instead. This removes
  the need for consumers to maintain their
  own Paint objects. For consumers that
  still require access to a Canvas
  they can use the drawCanvas extension
  method which provides a callback to issue
  drawing commands with the underlying
  Canvas. ([I80afd](https://android-review.googlesource.com/#/q/I80afdf4c0a648962aa6ef1efc05b1d3b65757094))

- AlignmentLineOffset composable is deprecated, please use relativePaddingFrom() modifier instead. CenterAlignmentLine composable is removed. ([I60107](https://android-review.googlesource.com/#/q/I601076f5ba044b176e07115a1916cdee71083163))

- WithConstraints trailing lambda API has been changed. Now instead of two params it has a receiver scope which in addition to constraints and layoutDirection provides minWidth, maxWidth, minHeight and maxHeight properties in Dp ([I91b9a](https://android-review.googlesource.com/#/q/I91b9af740cd2613ddd4fe6d63cd539a46b52fc52), [b/149979702](https://issuetracker.google.com/issues/149979702))

- Added defaultMinSizeConstraints layout modifier, which sets size constraints to the wrapped layout only when the incoming corresponding constraints are unspecified (0 for min constraints and infinity for max constraints). ([I311ea](https://android-review.googlesource.com/#/q/I311eaf525d05eea9f657f583da7fdf845ad8d64f), [b/150460257](https://issuetracker.google.com/issues/150460257))

- FocusManagerAmbient is removed. Use FocusModifier.requestFocus to obtain focus. ([Ic4826](https://android-review.googlesource.com/#/q/Ic482662c18a1cb41f097a1e0bcc114d517b756b7))

- Created CanvasScope API that wraps a
  Canvas object to expose a stateless, declarative
  drawing API surface. Transformations are contained
  within their own receiver scope and sizing information
  is also scoped to corresponding inset bounds.
  It does not require a consumer to maintain its own Paint state
  object for configuring drawing operations.

  Added CanvasScopeSample as well as
  updated the demo app to include a declarative graphics
  demo ([Ifd86d](https://android-review.googlesource.com/#/q/Ifd86d39ef5807d34cc06d06854d24330e5e00164))
- Add cursor color customisation to the TextField ([I6e33f](https://android-review.googlesource.com/#/q/I6e33fa47950cddb5d3631528cd954c48a3f255d2))

- TextFieldValue used with TextField can now be survive activity recreation when used like this: `var text by savedInstanceState(saver = TextFieldValue.Saver) { TextFieldValue() }` ([I5c3ce](https://android-review.googlesource.com/#/q/I5c3cee62fa592dd00c1595efc6ea950b8aeda676), [b/155075724](https://issuetracker.google.com/issues/155075724))

- Renamed LayoutModifier2 to LayoutModifier. ([Id29f3](https://android-review.googlesource.com/#/q/Id29f36d6b19674d189abb198a7656562b3b310b5))

- Removed deprecated LayoutModifier interface. ([I2a9d6](https://android-review.googlesource.com/#/q/I2a9d6a9840072d5cb92e68155be2d07de8411d04))

- Replaced CoreTextField/TextField focusIdentifier
  parameter with FocusNode in order to integrate with focus subsystem. ([I7ea48](https://android-review.googlesource.com/#/q/I7ea4842b2acff06658b0731c55c877301b524757))

- Intrinsic measurements functions in Layout and LayoutModifier2 have an IntrinsicMeasureScope receiver now which provides intrinsics query API with implicitly propagated layout direction. ([Id9945](https://android-review.googlesource.com/#/q/Id9945cb41842df9f99132679b5b68a0f0edda53d))

- New Modifier.zIndex() is added to control the drawing order of the children within the same parent layout. elevation property on DrawLayerModifier is renamed to shadowElevation and doesn't control the drawing order anymore. The params order fo DrawShadow is changed: elevation is now the first one and the shape is the second one with a RectangleShape default. ([I20150](https://android-review.googlesource.com/#/q/I201506a33a55a4c48a4dbb6fe4e580824410588f), [b/152417501](https://issuetracker.google.com/issues/152417501))

- RectangleShape moved from androidx.ui.foundation.shape.\* to androidx.ui.graphics.\* ([Ia74d5](https://android-review.googlesource.com/#/q/Ia74d5a3bbe2ee3a28bbddb57a2aef2607679d4ac), [b/154507984](https://issuetracker.google.com/issues/154507984))

- TextField API update - merged onFocus and onBlur callbacks into a single onFocusChange(Boolean) callback with parameter ([I66cd3](https://android-review.googlesource.com/#/q/I66cd3b14d1df6bfbaafc25e501995368d69138ec))

- Added verticalGravity and horizontalGravity parameters to Row and Column, respectively. ([I7dc5a](https://android-review.googlesource.com/#/q/I7dc5a4e757370075657be68e6eda68e7498228fa))

- Updated wrapContentWidth and wrapContentHeight to expect vertical or horizontal Alignment rather than any Alignment. The gravity modifier was updated to accept vertical or horizontal Alignment. Row, Column and Stack were updated to support custom continuous Alignments. ([Ib0728](https://android-review.googlesource.com/#/q/Ib07281752fa9806a13e61823e00accb26f99c1f6))

- Created PixelMap API to support
  querying pixel information from an ImageAsset. ([I69ad6](https://android-review.googlesource.com/#/q/I69ad6c9a12ceed74ef6e4cf10786da309baa5580))

- Removes ProvideContentColor, instead just use ContentColorAmbient directly with `Providers` ([Iee942](https://android-review.googlesource.com/#/q/Iee94234bfe6f820445b3d3d986895b293271753e))

- ui-text-compose module is renamed as ui-text. ui-text
  now contains CoreText and CoreTextField composables ([Ib7d47](https://android-review.googlesource.com/#/q/Ib7d4743369dbffbac262251b25d3c4351387fb36))

- ui-text module is renamed as ui-text-core ([I57dec](https://android-review.googlesource.com/#/q/I57dec72ca50e7288e37c9272ef6ce8bcc485a83e))

- Moved ui-framework/CoreText, CoreTextField composables under
  ui-text-compose. You might want to include ui-text-compose in your
  project. ([I32042](https://android-review.googlesource.com/#/q/I32042a9c701b1ea3ec4f92c02811c248af6ddb84))

- Improve DrawModifier API:

  - Made the receiver scope for draw() ContentDrawScope
  - Removed all parameters on draw()
  - DrawScope has same interface as former CanvasScope
  - ContentDrawScope has drawContent() method ([Ibaced](https://android-review.googlesource.com/#/q/Ibaced5feb8778510b8fe78e96f4fd3da1a6fda50), [b/152919067](https://issuetracker.google.com/issues/152919067))
- `runOnIdleCompose` and `runOnUiThread` are now global functions
  instead of methods on ComposeTestRule. ([Icbe8f](https://android-review.googlesource.com/#/q/Icbe8fd71d52144e855ccb4ce06a4677337be731a))

- \[Mutable\]State property delegate operators moved to extensions
  to support Kotlin 1.4 property delegate optimizations. Callers must add
  imports to continue using `by state { ... }` or `by mutableStateOf(...)`. ([I5312c](https://android-review.googlesource.com/#/q/I5312cf7bdfa072cadc1be2de5d5f45ec53200f41))

- Added positionInParent and boundsInParent for LayoutCoordinates. ([Icacdd](https://android-review.googlesource.com/#/q/Icacdd0909bc434cd5fd935c46e0a07b965c6a38d), [b/152735784](https://issuetracker.google.com/issues/152735784))

- ColoredRect has been deprecated. Use Box(Modifier.preferredSize(width, height).drawBackground(color)) instead. ([I499fa](https://android-review.googlesource.com/#/q/I499fa26b66b128943500fbdf9ba490d754adf561), [b/152753731](https://issuetracker.google.com/issues/152753731))

- Renamed LayoutResult to MeasureResult. ([Id8c68](https://android-review.googlesource.com/#/q/Id8c686b5f08d58e8e48d015ed42570e306687882))

- Added LayoutModifier2, a new API for defining layout modifiers; deprecated LayoutModifier ([If32ac](https://android-review.googlesource.com/#/q/If32acbfac08c677b80f9e4d5f624fe15c95ac60d))

- Replaced Modifier plus operator with factory extension functions ([I225e4](https://android-review.googlesource.com/#/q/I225e444f50956d84e15ca4f1378b7f805d54e0ca))

- Draggable has been moved to modifier ([Id9b16](https://android-review.googlesource.com/#/q/Id9b16db6942de069e8d2221f192525b3bc71ab7d), [b/151959544](https://issuetracker.google.com/issues/151959544))

- ParentData composable is deprecated. You should either create a modifier which implements ParentDataModifier interface, or use LayoutTag modifier if you simply need to tag layout children to recognize them inside the measure block. ([I51368](https://android-review.googlesource.com/#/q/I51368a2cb132318f5466949297e5fa247c04d68a), [b/150953183](https://issuetracker.google.com/issues/150953183))

- Deprecated Center composable. It should be replaced either with the LayoutSize.Fill + LayoutAlign.Center modifier, or with one of the Box or Stack composables with suitable modifiers applied ([Idf5e0](https://android-review.googlesource.com/#/q/Idf5e0d25a2a8764489d738f6fcf242eeb667e124))

- Added VectorPainter API to
  replace existing subcomposition API for
  vector graphics. Result of subcomposition
  is a VectorPainter object instead of a
  DrawModifier. Deprecated previous DrawVector
  composables in favor of VectorPainter.

  Renamed Image(Painter) API to PaintBox(Painter)
  Created Vector composable that behaves like the
  Image composable except with a VectorAsset instead
  of an ImageAsset ([I9af9a](https://android-review.googlesource.com/#/q/I9af9a365eb744e0cdb343cf424f4df5160d6c2b4), [b/149030271](https://issuetracker.google.com/issues/149030271))
- Renamed LayoutFlexible to LayoutWeight. Renamed tight parameter to fill. ([If4738](https://android-review.googlesource.com/#/q/If4738c70c381e149ded400d657b5efd888ae5891))

- Removed RepaintBoundary in favor of DrawLayerModifier ([I00aa4](https://android-review.googlesource.com/#/q/I00aa4667ebe6248500b677b07d08744d5f79ae7f))

- DrawVector has been changed from a regular
  composable function to returning a Modifier drawVector() that
  will draw the vector as a background to a layout. ([I7b8e0](https://android-review.googlesource.com/#/q/I7b8e04d9eae7619211748b92658b31bc09e9b2a0))

- The Opacity composable function has been replaced
  with the drawOpacity modifier. ([I5fb62](https://android-review.googlesource.com/#/q/I5fb62404e20e3f2a0fa94ad0fb121f35d05bbb1c))

- Replace composable function Clip with modifier
  drawClip(). DrawClipToBounds is a convenient modifier
  to use when you only need to clip to the layer bounds
  with a rectangle shape. ([If28eb](https://android-review.googlesource.com/#/q/If28eb34fe98927dcb8d87f8961657cb8317371ae))

- Replaced DrawShadow composable function with drawShadow()
  modifier. Shadows are now drawn as part of LayerModifier. ([I0317a](https://android-review.googlesource.com/#/q/I0317ac63ddafcf16bd2e24662d489aacb4bb6a7e))

- Added LayerModifier, a modifier that allows
  adding a RenderNode for a Layout. It allows setting
  clipping, opacity, rotation, scaling, and shadows.
  This will replace RepaintBoundary. ([I7100d](https://android-review.googlesource.com/#/q/I7100dfe7a795567a48c2d5b3094e3dbd47e0f9c7), [b/150774014](https://issuetracker.google.com/issues/150774014))

- androidx.compose.ViewComposer has been moved to androidx.ui.node.UiComposer
  androidx.compose.Emittable has been removed. It was redundant with ComponentNode.
  androidx.compose.ViewAdapters has been removed. They are no longer a supported use case.
  Compose.composeInto has been deprecated. Use `setContent` or `setViewContent` instead.
  Compose.disposeComposition has been deprecated. Use the `dispose` method on the `Composition` returned by `setContent` instead.
  androidx.compose.Compose.subcomposeInto has moved to androidx.ui.core.subcomposeInto
  ComponentNode#emitInsertAt has been renamed to ComponentNode#insertAt
  ComponentNode#emitRemoveAt has been renamed to ComponentNode#removeAt
  ComponentNode#emitMode has been renamed to ComponentNode#move ([Idef00](https://android-review.googlesource.com/#/q/Idef00fba3a2e67d7034e31d580d69192e9018b5f))

- Created Image composable to handle
  sizing/layout in addition to drawing a given
  ImageAsset to the screen. This composable
  also supports drawing any arbitrary Painter
  instance respecting its intrinsic size
  as well as supporting a given fixed
  size or minimum size ([Ibcc8f](https://android-review.googlesource.com/#/q/Ibcc8f4d61cf0a0fbe697055ee2b6bfe8568755ed))

- Deprecated Wrap composable. It can be replaced either with the LayoutAlign modifier or with the Stack composable ([Ib237f](https://android-review.googlesource.com/#/q/Ib237f0f8f8cedd87c35683e5cc1b69abfd13d111))

- WithConstraints got LayoutDirection parameter ([I6d6f7](https://android-review.googlesource.com/#/q/I6d6f7d5fd9a4a0428e3ee188a9a3790e1cdaf083))

- Made the layout direction be propagated from parent layout node to children. Added layout direction modifier. ([I3d955](https://android-review.googlesource.com/#/q/I3d9559ddec464850d22466793975b41757e0224e))

-

  > [!WARNING]
  > **Deprecated:** Draw composable is a common source of bugs as it's ([I78392](https://android-review.googlesource.com/#/q/I78392f01c2d37c2419812478d96417a1b8a1293d), [b/149827027](https://issuetracker.google.com/issues/149827027))

- Stack component supports right-to-left directionality ([Ic9e00](https://android-review.googlesource.com/#/q/Ic9e00dfc5b8c16ff305c14bc38de38cdf72d4cf5))

- DrawShape composable was removed. Use DrawBackground modifier instead. ([I7ceb2](https://android-review.googlesource.com/#/q/I7ceb270c8571b3cb1cdc8b0494d90c985f61b3d7))

- Support right-to-left direction in LayoutPadding modifier ([I9e8da](https://android-review.googlesource.com/#/q/I9e8da0bfbb135ff7f34b0dc49b905f634ad7d18c))

- Added AdapterList, a scrolling list component that only
  composes and lays out the visible items. Currently known issues
  include that it is vertical-only and does not fully handle all
  cases of changes to its children. ([Ib351b](https://android-review.googlesource.com/#/q/Ib351be89aabb59dac29806a935e377e90a2da9c2))

- Updated the `ComposeFlags.COMPOSER_PARAM` flag to be `true`, which will change the code generation strategy for the compose plugin. At a high level, this causes @Composable functions to be generated with an additional synthetic parameter, which is passed through to subsequent @Composable calls in order for the runtime to properly manage execution. This is a significant binary breaking change, however, should preserve source-level compatibility in all sanctioned usage of compose. ([I7971c](https://android-review.googlesource.com/#/q/I7971ca1b6525440c38643953645fa388131e31f0))

- Added Canvas component. This composable takes up some size (provided by user) and allows you to draw using CanvasScope ([I0d622](https://android-review.googlesource.com/#/q/I0d62259da4f70e68e57ed1b20cdc9b9aa3d8b1be))

- Density and DensityScope were merged into one interface. Instead of ambientDensity() you can now use DensityAmbient.current. Instead of withDensity(density) just with(density) ([I11cb1](https://android-review.googlesource.com/#/q/I11cb1f069a95f32f4ecab631f49d38dc1c071a42))

- Changed LayoutCoordinates to make providedAlignmentLines
  a Set instead of a Map and have LayoutCoordinates implement the
  get() operator instead for retrieving a value. This makes it easier
  for modifiers to modify one or more value of the set without
  creating a new collection for each modifier. ([I0245a](https://android-review.googlesource.com/#/q/I0245a750ed12e822d61fa7d87c52bd708996f55d))

- Scrollers now exhibit native Android fling motion behavior. ([I922af](https://android-review.googlesource.com/#/q/I922af68261f3f1e81538a98a7575603e531fc035), [b/147493715](https://issuetracker.google.com/issues/147493715))

- Improvements to the API surface of Constraints ([I0fd15](https://android-review.googlesource.com/#/q/I0fd1505ae9a68c067a82eff6ab02b43080fe153c))