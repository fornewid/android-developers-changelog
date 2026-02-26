---
title: https://developer.android.com/jetpack/androidx/releases/compose-animation
url: https://developer.android.com/jetpack/androidx/releases/compose-animation
source: md.txt
---

# Compose Animation

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.animation](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary)  
[androidx.compose.animation.core](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary)  
[androidx.compose.animation.graphics](https://developer.android.com/reference/kotlin/androidx/compose/animation/graphics/res/package-summary)  
(*See the API reference docs for all compose packages*) Build animations in their Jetpack Compose applications to enrich the user experience.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.10.4](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.10.4) | - | - | [1.11.0-alpha06](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.11.0-alpha06) |

## Structure

Compose is a combination of 7 Maven group IDs within `androidx`. Each group
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
    implementation "androidx.compose.animation:animation:1.10.4"
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
    implementation("androidx.compose.animation:animation:1.10.4")
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
[existing issues](https://issuetracker.google.com/issues?q=componentid:610478+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=610478&template=1265071)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.11

### Version 1.11.0-alpha06

February 25, 2026

`androidx.compose.animation:animation-*:1.11.0-alpha06` is released. Version 1.11.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..6e23fc0c137022098ae2d043778ffdc56402ba5e/compose/animation).

**Bug Fixes**

- Improve performance of `sharedElements` map access. ([93f57d](https://android-review.googlesource.com/#/q/Ib98ee4709dee9ece4e07830a0baa449593a6716f))

### Version 1.11.0-alpha05

February 11, 2026

`androidx.compose.animation:animation-*:1.11.0-alpha05` is released. Version 1.11.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/animation).

### Version 1.11.0-alpha04

January 28, 2026

`androidx.compose.animation:animation-*:1.11.0-alpha04` is released. Version 1.11.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/animation).

### Version 1.11.0-alpha03

January 14, 2026

`androidx.compose.animation:animation-*:1.11.0-alpha03` is released. Version 1.11.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/animation).

**New Features**

- Introduced a new set of visual debugging capabilities that allows visualizations of information related to shared elements and `Modifier.animatedBounds`. Such information includes: target bounds, the trajectory of the bounds animation, number of matches found, whether the transition is active, etc.

**API Changes**

- Added a new api `LookaheadAnimationVisualDebugging`, `CustomizedLookaheadAnimationVisualDebugging`, and `LookaheadAnimationVisualDebugConfig` to help debug animated bounds and shared element animations. ([Id5575](https://android-review.googlesource.com/#/q/Id5575389fd198a82de8f3187c4ab2e16036e64d4), [b/390011686](https://issuetracker.google.com/issues/390011686), [b/466169919](https://issuetracker.google.com/issues/466169919))

**Bug Fixes**

- Require shared transition root to be placed before querying bounds. ([77d59c](https://android-review.googlesource.com/#/q/77d59cb))

### Version 1.11.0-alpha02

December 17, 2025

`androidx.compose.animation:animation-*:1.11.0-alpha02` is released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/animation).

### Version 1.11.0-alpha01

December 03, 2025

`androidx.compose.animation:animation-*:1.11.0-alpha01` is released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b48588febd37d5947dfa0f2827d2b5ca6af2ed90..deb96499dfe95073f5c1215c1287787683cb1e92/compose/animation).

**Bug Fixes**

- Only acquire position for `sharedElements` if `SharedTransitionLayout` is attached ([I2a035](https://android-review.googlesource.com/#/q/I2a03554b3528abf628787091d3a7bede6c01a292))

## Version 1.10

### Version 1.10.4

February 25, 2026

`androidx.compose.animation:animation-*:1.10.4` is released. Version 1.10.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0d23f956849b578e041ea4245127d4007eae43be..6b6d8d062bfb0daa907101a196d1ea43d60ecfe2/compose/animation).

### Version 1.10.3

February 11, 2026

`androidx.compose.animation:animation-*:1.10.3` is released. Version 1.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b..0d23f956849b578e041ea4245127d4007eae43be/compose/animation).

**Bug Fixes**

- Fixed the crash caused by a corner case where the shared content node is detached before the shared transition root was ever placed. ([121310](https://android-review.googlesource.com/#/q/121310e))

### Version 1.10.2

January 28, 2026

`androidx.compose.animation:animation-*:1.10.2` is released. Version 1.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c09ac6669b664a348ecf964a97968cd81479dcd4..fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b/compose/animation).

### Version 1.10.1

January 14, 2026

`androidx.compose.animation:animation-*:1.10.1` is released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2120e7975523001d1eac390a5d9c5e2e9597267f..c09ac6669b664a348ecf964a97968cd81479dcd4/compose/animation).

### Version 1.10.0

December 03, 2025

`androidx.compose.animation:animation-*:1.10.0` is released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26..a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9/compose/animation).
**Important changes since 1.9.0:**

- Shared transition APIs are stable in 1.10
- New `Modifier.skipToLookaheadPosition` API for layouts in `SharedTransitionScope` to skip to the target position instead of animating position changes ([9a88f4](https://android-review.googlesource.com/#/q/9a88f40))
- Support dynamically enabling/disabling shared elements ([07680e](https://android-review.googlesource.com/#/q/07680e0))
- New API to support initial velocity for initiating shared element transition with a fling ([b0afe2](https://android-review.googlesource.com/#/q/b0afe2d))
- New `EnterTransition` and `ExitTransition` for animating a veil layer for `AnimatedVisibility` and `AnimatedContent` ([0f6e7c](https://android-review.googlesource.com/#/q/0f6e7c7))

### Version 1.10.0-rc01

November 19, 2025

`androidx.compose.animation:animation-*:1.10.0-rc01` is released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1c84233fc2372352b838d165d256581ff37ada9..b48588febd37d5947dfa0f2827d2b5ca6af2ed90/compose/animation).

**API Changes**

- `unveilIn` and `veilOut` options are now available for `EnterExitTransitions`. This allows to animate an overlay layer in front of the entering or exiting content. ([If26fe](https://android-review.googlesource.com/#/q/If26fe2c15212de1b0ad2b91ad70bfd5d882610c2))

**Bug Fixes**

- Support bounds tracking through detaching \& reattaching of `sharedElement` ([be0e9e](https://android-review.googlesource.com/#/q/be0e9e763a9683077c0525f7c0b6cf3aab144d07))
- Make shared element map observable for transition activeness observation. ([1fc2ec](https://android-review.googlesource.com/#/q/1fc2ecd18345bebf0c2ad31382478a877e47ea3a))

### Version 1.10.0-beta02

November 05, 2025

`androidx.compose.animation:animation-*:1.10.0-beta02` is released. Version 1.10.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/784e4a2de372f09d49c65fbc1ca64681a25a5f06..d1c84233fc2372352b838d165d256581ff37ada9/compose/animation).

### Version 1.10.0-beta01

October 22, 2025

`androidx.compose.animation:animation-*:1.10.0-beta01` is released. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..784e4a2de372f09d49c65fbc1ca64681a25a5f06/compose/animation).

**API Changes**

- The `SharedContentConfig` factory method that takes a lambda indicating whether the shared element should be enabled has been removed. `lookheadScopeCoordinates` API has been updated with a `LookaheadScope` being the receiver scope, with source coordinates being the parameter. ([Id1fc2](https://android-review.googlesource.com/#/q/Id1fc2a33c193ea054ae2d6cc7801cf03d243f77b), [b/452416806](https://issuetracker.google.com/issues/452416806))
- `BoundsTransform` interface has been updated to be consistent with `SizeTransform`. ([Ia46f2](https://android-review.googlesource.com/#/q/Ia46f29ba82f8f8c32610792d7f8a4be4f29f754d), [b/343696350](https://issuetracker.google.com/issues/343696350))
- Deprecated `ScaleToBounds` API has been removed. Please use `scaleToBounds` instead. ([I17296](https://android-review.googlesource.com/#/q/I17296bda0d58f47d83eb972dc19abf7ad7b34669))

### Version 1.10.0-alpha05

October 08, 2025

`androidx.compose.animation:animation-*:1.10.0-alpha05` is released. Version 1.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef9c81cf7222a390e0a467d8c8b48d04362fd3d..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/animation).

**API Changes**

- Shared transition APIs are now stable. For more information, please see the [shared element guide](https://developer.android.com/develop/ui/compose/animation/shared-elements). ([I7167e](https://android-review.googlesource.com/#/q/I7167e00a544b1c9ef4a7c8d16803fc3439228d6d)).

### Version 1.10.0-alpha04

September 24, 2025

`androidx.compose.animation:animation-*:1.10.0-alpha04` is released. Version 1.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..6ef9c81cf7222a390e0a467d8c8b48d04362fd3d/compose/animation).

**API Changes**

- Updated the naming for `PlaceHolderSize` related APIs. ([I037d8](https://android-review.googlesource.com/#/q/I037d819a9edbf03b3bf788223afd4272a783f9ae), [b/343696350](https://issuetracker.google.com/issues/343696350))
- New shared element transition API to support an initial velocity to continue the gesture velocity in shared elements. ([I91be9](https://android-review.googlesource.com/#/q/I91be97f4324d1ab6595172988bb203f5fbc7382a))

### Version 1.10.0-alpha03

September 10, 2025

`androidx.compose.animation:animation-*:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/compose/animation).

**API Changes**

- `Modifier.skipToLookaheadSize` now uses a default enabled lambda that only enables the size skipping when shared transition is active, same as `Modifier.skipToLookaheadPosition`. ([Ibe0f5](https://android-review.googlesource.com/#/q/Ibe0f56ebe107b33a6adae7e1e4eb676b366afb5d), [b/432485585](https://issuetracker.google.com/issues/432485585))

### Version 1.10.0-alpha02

August 27, 2025

`androidx.compose.animation:animation-*:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/animation).

### Version 1.10.0-alpha01

August 13, 2025

`androidx.compose.animation:animation-*:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c30d03ab9e19dcf35e8b79438f0d91ee74cae557..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/animation).

**New Features**

- New API to allow dynamically enable and disable shared elements that also allows accounting for whether there is already an ongoing shared element transition.
- New API to set up an alternative target bounds when the target shared element is disposed during the transition.
- New API to obtain the `LayoutCoordinates` of a `LookaheadScope`. ([I18dd4](https://android-review.googlesource.com/#/q/I18dd441208500dbd29276f834421db3134047390), [b/409819304](https://issuetracker.google.com/issues/409819304), [b/395670637](https://issuetracker.google.com/issues/395670637))
- New modifier `Modifier.skipToLookaheadPosition` in `SharedTransitionScope` for anchoring a layout at the target position during a shared transition. ([I88734](https://android-review.googlesource.com/#/q/I887347cb86f334564d938300eb81d277a9c4be4b))

**API Changes**

- Simplified `renderInSharedTransitionOverlay` by removing the `clipInOverlayDuringTransition` lambda as this has been rarely used. Introduced new factory method for `SharedContentConfig`. ([Id01b2](https://android-review.googlesource.com/#/q/Id01b23ce2acd97cd5c2fdd41ed39c85f1d835192))
- Added a set of Defaults for shared element, shared bounds, `renderInSharedTransitionOverlay` configurations. These defaults are now accessible through public APIs. ([Id23cc](https://android-review.googlesource.com/#/q/Id23cc7f8e55f83d2128ff6e51de754e659923a15))
- `ScaleToBounds` ResizeMode has been renamed to `scaleToBounds` ([I5ac50](https://android-review.googlesource.com/#/q/I5ac508eed2c833f0c091584b5b929b50ce1f9825))

**Bug Fixes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

## Version 1.9

### Version 1.9.5

November 19, 2025

`androidx.compose.animation:animation-*:1.9.5` is released. Version 1.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41..1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26/compose/animation).

### Version 1.9.4

October 22, 2025

`androidx.compose.animation:animation-*:1.9.4` is released. Version 1.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea7909f13c54ea29d87d55d27ecf449000f82a8a..b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41/compose/animation).

### Version 1.9.3

October 08, 2025

`androidx.compose.animation:animation-*:1.9.3` is released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6177e34a7667c42030e47ee8ecba82f09e2a5de..ea7909f13c54ea29d87d55d27ecf449000f82a8a/compose/animation).

### Version 1.9.2

September 24, 2025

`androidx.compose.animation:animation-*:1.9.2` is released. Version 1.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/93a1ed2aac05dbfa192392b9d4ab27c40da53d69..b6177e34a7667c42030e47ee8ecba82f09e2a5de/compose/animation).

### Version 1.9.1

September 10, 2025

`androidx.compose.animation:animation-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44da9aeaf3fa617c6f81f887691b37fe901109aa..93a1ed2aac05dbfa192392b9d4ab27c40da53d69/compose/animation).

**Bug Fixes**

- Fix initializing animation for `sharedElementWithCallerManagedVisibility`. ([fa29de](https://android-review.googlesource.com/#/q/fa29de5))

### Version 1.9.0

August 13, 2025

`androidx.compose.animation:animation-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..44da9aeaf3fa617c6f81f887691b37fe901109aa/compose/animation).

### Version 1.9.0-rc01

July 30, 2025

`androidx.compose.animation:animation-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..c30d03ab9e19dcf35e8b79438f0d91ee74cae557/compose/animation).

### Version 1.9.0-beta03

July 16, 2025

`androidx.compose.animation:animation-*:1.9.0-beta03` is released. Version 1.9.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d578548e34459870db64b61d8788d83f2cf49f54..5735a11c1798c2f8b419dfdc02347578a6ebf870/compose/animation).

### Version 1.9.0-beta02

July 2, 2025

`androidx.compose.animation:animation-*:1.9.0-beta02` is released. Version 1.9.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..d578548e34459870db64b61d8788d83f2cf49f54/compose/animation).

### Version 1.9.0-beta01

June 18, 2025

`androidx.compose.animation:animation-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e1d81d156ec778ff4b8bc291aa661d780576ea4c/compose/animation).

### Version 1.9.0-alpha04

June 4, 2025

`androidx.compose.animation:animation-*:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fd8d5a2f883c1cdd7f712b200d5a4fedf342136..786176dc2284c87a0e620477608e0aca9adeff15/compose/animation).

### Version 1.9.0-alpha03

May 20, 2025

`androidx.compose.animation:animation-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..5fd8d5a2f883c1cdd7f712b200d5a4fedf342136/compose/animation).

### Version 1.9.0-alpha02

May 7, 2025

`androidx.compose.animation:animation-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/animation).

**New Features**

- Much improved support for scrolling or dragging in shared elements. More specifically, when a transitioning shared element is being scrolled, the scroll delta will be directly applied to the shared element rather than causing the shared elements to chase the new target. ([cacf7b](https://android-review.googlesource.com/#/q/cacf7b9))

### Version 1.9.0-alpha01

April 23, 2025

`androidx.compose.animation:animation-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/animation).

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

**New Features**

- Improved scrolling performance for shared elements ([ea4f1f](https://android-review.googlesource.com/#/q/ea4f1f2))

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `TabRow` and `ScrollableTabRow` are deprecated in favor of Primary and Secondary variants of each. Primary and Secondary tab rows are more performant and accurate to spec. ([I918e2](https://android-review.googlesource.com/#/q/I918e2c22e4ec59c9162a730c4c1223ef735d6da0))
- Added `LocalResources` composition local to query Resources. Calling `LocalResources.current` will recompose when the configuration changes, so calls to APIs such as `stringResource()` will return updated values ([I50c13](https://android-review.googlesource.com/#/q/I50c13ee26bc440f3fe64c40271850e76e734a596), [b/274786917](https://issuetracker.google.com/issues/274786917))

**Bug Fixes**

- Ensure shared elements are dropped from the overlay when the transition is finished ([35f359](https://android-review.googlesource.com/#/q/35f359d))
- Eliminate extra recomposition in Transition ([988923](https://android-review.googlesource.com/#/q/9889234))
- Fix child transition interruption handling ([8aed52](https://android-review.googlesource.com/#/q/8aed52d))
- Ensure transition is reset when a new `TransitionState` is provided ([57820a](https://android-review.googlesource.com/#/q/57820ab))

**External Contribution**

- From [Compose `1.8.1`](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.8.1): End animations in `SeekableTransitionState` if already past new duration by Steven Schoen. ([0c832c](https://android-review.googlesource.com/#/q/0c832c1))

## Version 1.8

### Version 1.8.3

June 18, 2025

`androidx.compose.animation:animation-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/754896be0859599f16ed264d79a04ee337bac777..13362f65a9c0649415fe57052ea0e3932d2303d1/compose/animation).

### Version 1.8.2

May 20, 2025

`androidx.compose.animation:animation-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/018e42f9db74b5e4fce8007734de4da6ae087407..754896be0859599f16ed264d79a04ee337bac777/compose/animation).

### Version 1.8.1

May 7, 2025

`androidx.compose.animation:animation-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..018e42f9db74b5e4fce8007734de4da6ae087407/compose/animation).

**External Contribution**

- End animations in `SeekableTransitionState` if already past new duration. Thanks Steven Schoen! ([fbcdf7](https://android-review.googlesource.com/#/q/fbcdf7b))

### Version 1.8.0

April 23, 2025

`androidx.compose.animation:animation-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b6bba717628c4c8c633c9509bfc4e4d9b89f428..d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9/compose/animation).

**Important changes since 1.7.0**

- Important changes in version 1.8.0 are covered in this[blogpost](https://android-developers.googleblog.com/2025/04/whats-new-in-jetpack-compose-april-25.html)
- New `Modifier.animateBounds` API for animating size and position changes within a lookahead scope. ([94b939](https://android-review.googlesource.com/#/q/94b9394))
- Finalized APIs for Keyframes with Arcs and Splines ([89e119](https://android-review.googlesource.com/#/q/89e1199))
- Supported Lookahead in `LazyGrid` and Pager. This includes differentiating lookahead pass versus approach pass in scrolling, item composition/disposal, and item animation, and uses lookahead pass for source of truth for scrolling, and item animation target.
- Updated `sharedElement` parameter naming from state to `sharedContentState` for consistency across shared element APIs. ([9e7df5](https://android-review.googlesource.com/#/q/9e7df51))
- `AnimatedImageVector` suite of APIs are now stable.([69d7e0](https://android-review.googlesource.com/#/q/69d7e04))

### Version 1.8.0-rc03

April 9, 2025

`androidx.compose.animation:animation-*:1.8.0-rc03` is released. Version 1.8.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0907800009c0cb37dd12c5586d620350c1975de..1b6bba717628c4c8c633c9509bfc4e4d9b89f428/compose/animation).

### Version 1.8.0-rc02

March 26, 2025

`androidx.compose.animation:animation-*:1.8.0-rc02` is released. Version 1.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/071f2b22541efa1d5d528479b28aa42960923a4f..c0907800009c0cb37dd12c5586d620350c1975de/compose/animation).

### Version 1.8.0-rc01

March 12, 2025

`androidx.compose.animation:animation-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d195d8376d369f4bf74652abe60101aa658bbcc..071f2b22541efa1d5d528479b28aa42960923a4f/compose/animation).

**Bug Fixes**

- Fixed child transition incorrectly being marked as interrupted. ([3fa2ce](https://android-review.googlesource.com/#/q/3fa2ce1b70708aceeb46456ff240b7024e8cbd59))

### Version 1.8.0-beta03

February 26, 2025

`androidx.compose.animation:animation-*:1.8.0-beta03` is released. Version 1.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/08954f0d500d220e8d6af07b4e6c51090911f779..2d195d8376d369f4bf74652abe60101aa658bbcc/compose/animation).

### Version 1.8.0-beta02

February 12, 2025

`androidx.compose.animation:animation-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5d82c9c8e72f3dd8c4ee71ff5ac9a1365d24de4..08954f0d500d220e8d6af07b4e6c51090911f779/compose/animation).

### Version 1.8.0-beta01

January 29, 2025

`androidx.compose.animation:animation-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8..80c9eca8dc00a6ae7188bf5f2beaf129b79de243/compose/animation).

### Version 1.8.0-alpha08

January 15, 2025

`androidx.compose.animation:animation-*:1.8.0-alpha08` is released. Version 1.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/animation).

**Bug Fixes**

- Fixed incorrect placement animation from `animateBounds` in `LazyGrid` due to `MotionFrameOfReferencePlacement` being reset. ([16193b](https://android-review.googlesource.com/#/q/16193b6f5334f219c6dc4a8aac96fd257a91767d))
- Fixed intrinsic query in `SharedTransitionLayout` by redirecting the intrinsic query to lookahead pass from a top-level lookahead root. ([a07d12](https://android-review.googlesource.com/#/q/a07d12c83d22ec5ba6f200dc25af9c60d61339b2))
- Added missing `@param` tags in docs. ([e5cf67](https://android-review.googlesource.com/#/q/e5cf676e339f2807cf29bf28fe7d8364931a48eb))

### Version 1.8.0-alpha07

December 11, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha07` is released. Version 1.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/compose/animation).

**New Features**

- Supports lookahead in Pager, by differentiating the lookahead pass from approach pass for retaining items and consuming scrolling. ([b/371802474](https://issuetracker.google.com/371802474))

**Bug Fixes**

- Fixes a rare crash where a shared element is composed but never measured/placed, by requiring the shared element to render in place at least once before rendering it in overlay. ([b/371802474](https://issuetracker.google.com/371802474))

### Version 1.8.0-alpha06

November 13, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha06` is released. Version 1.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/animation).

**API Changes**

- Updated `sharedElement` parameter naming from `state` to `sharedContentState` for consistency across shared element APIs. ([I5694c](https://android-review.googlesource.com/#/q/I5694cffa5df5527e1fcd12f9267d479fd175ee87), [b/375351468](https://issuetracker.google.com/issues/375351468))
- `AnimatedImageVector` suite of APIs are now stable. ([I7174b](https://android-review.googlesource.com/#/q/I7174b2b38481ddd55dc1550b0247b315dd7ce200), [b/261436267](https://issuetracker.google.com/issues/261436267))

### Version 1.8.0-alpha05

October 30, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha05` is released. Version 1.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/animation).

**New Features**

- Lookahead is now supported in `LazyGrid`. This includes differentiating lookahead pass versus approach pass in scrolling, item composition/disposal, and item animation, and uses lookahead pass for source of truth for scrolling, and item animation target.

**Bug Fixes**

- Update internal states for `AnimatedContent`'s size transform when transition is recreated. This ensures the target size information is always up to date. ([b/372512085](https://issuetracker.google.com/372512085))

### Version 1.8.0-alpha04

October 16, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha04` is released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/animation).

**Bug Fixes**

- Fixed a bug causing some easing curves to crash at certain time fractions.
- Fixed a bug causing improper alignment for `Modifier.animateContentSize` under RTL. ([Idae6b](https://android-review.googlesource.com/#/q/Idae6b6255bb15b0f366b2737e68131f2db733bcb), [b/372055503](https://issuetracker.google.com/issues/372055503))

### Version 1.8.0-alpha03

October 2, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha03` is released. Version 1.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/compose/animation).

**API Changes**

- Kotlin version update to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))

**Bug Fixes**

- Fixed an issue in `AnimatedContent` size animation by always tracking and starting animation from the current size to ensure continuity.

### Version 1.8.0-alpha02

September 18, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988..0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/animation).

### Version 1.8.0-alpha01

September 4, 2024

`androidx.compose.animation:animation-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988/compose/animation).

**New Features**

- New `Modifier.animateBounds` API for animating size and position changes within a lookahead scope. [94b9394](https://android.googlesource.com/platform/frameworks/support/+/94b9394bd96f2c5b261551679c8d3e33dbe2b65a)

**API Changes**

- Remove experimental flags on Keyframes with Arcs and Splines ([89e1199](https://android.googlesource.com/platform/frameworks/support/+/89e11992e83265305c3aeaf4d8000bb24320b737))

**Bug Fixes**

- Skip `placeHolderSize` logic when no match is found ([77c0160](https://android.googlesource.com/platform/frameworks/support/+/77c0160158470a9899b4d8050c535603ee79b581))
- Clamp play time in `AndroidFlingSpline` to prevent crashes due to non-monotonically increasing play time([9d47587](https://android.googlesource.com/platform/frameworks/support/+/9d4758702ca80899774fb03dbaaf2ff09d06f554))
- Fix `SharedTransitionScope` not drawing items in certain conditions ([b41077b6](https://android.googlesource.com/platform/frameworks/support/+/b41077b6316a2c9a15b32765aaff73e301299040))

**External Contribution**

- Prevent setting seekable transition `playTime` when no transition is running by Steven Schoen. ([c2e6e7e6](https://android.googlesource.com/platform/frameworks/support/+/c2e6e7e61424d6883b7fd280785521ed22f42eca))

## Version 1.7

### Version 1.7.8

February 12, 2025

`androidx.compose.animation:animation-*:1.7.8` is released. Version 1.7.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/456f991655af86d9ae121f7e93f8699f958fc7ac..215cdfd8cb9c0762dd0347c383250644057c367f/compose/animation).

### Version 1.7.7

January 29, 2025

`androidx.compose.animation:animation-*:1.7.7` is released. No changes from 1.7.6.
December 11, 2024

`androidx.compose.animation:animation-*:1.7.6` is released. Version 1.7.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cbf03b378a865660d8209d0229c2bb1928c6e33..5e65beadeb2e2c15f34d0fff72861847795cca4f/compose/animation).

### Version 1.7.5

October 30, 2024

`androidx.compose.animation:animation-*:1.7.5` is released. Version 1.7.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b0ae0e41147a8a917cab35b4a6487af4fce6ead..4cbf03b378a865660d8209d0229c2bb1928c6e33/compose/animation).

**Bug Fixes**

- Fixed a bug causing improper alignment for `Modifier.animateContentSize` under RTL. ([Idae6b](https://android-review.googlesource.com/#/q/Idae6b6255bb15b0f366b2737e68131f2db733bcb), [b/372055503](https://issuetracker.google.com/issues/372055503))

### Version 1.7.4

October 16, 2024

`androidx.compose.animation:animation-*:1.7.4` is released. Version 1.7.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/00e91ed140ce2c4677f56fc06692b182b8a07fcf..6b0ae0e41147a8a917cab35b4a6487af4fce6ead/compose/animation).

### Version 1.7.3

October 2, 2024

`androidx.compose.animation:animation-*:1.7.3` is released. Version 1.7.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9..00e91ed140ce2c4677f56fc06692b182b8a07fcf/compose/animation).

### Version 1.7.2

September 18, 2024

`androidx.compose.animation:animation-*:1.7.2` is released. Version 1.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1efd0b233a17f707cd918993df1fa12e0bf9ae83..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/animation).

**External Contribution**

- Prevent setting seekable transition `playTime` when no transition is running. Thanks Steven Schoen! ([c2e6e7e6](https://android.googlesource.com/platform/frameworks/support/+/c2e6e7e61424d6883b7fd280785521ed22f42eca))

### Version 1.7.1

September 10, 2024

- No changes to Android artifacts. `-desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts.

### Version 1.7.0

September 4, 2024

`androidx.compose.animation:animation-*:1.7.0` is released.

**Important changes since 1.6.0**

Important changes in version 1.7.0 are covered in [this blogpost](https://android-developers.googleblog.com/2024/05/whats-new-in-jetpack-compose-at-io-24.html).

New Shared Element Transition APIs

- New shared element transition APIs await your usage and feedback. These new experimental APIs enable tagging layouts as shared across layout tree using the provided modifiers, producing smoothly changing bounds when one set of shared content exits and the other set enters. ([Icb0b9](https://android-review.googlesource.com/#/q/Icb0b953f1eaff80a582b1edd3f21f9f8031cf8b0))
- New `scaleInSharedContentToBounds` and `scaleOutSharedContentToBounds` to scale content in `sharedBounds` ([I731c1](https://android-review.googlesource.com/#/q/I731c18d0bd9a533bbf53ebba62f4638bdc758cbe))
- Experimental `SharedTransitionScope` is now an interface rather than a class. ([Iaf856](https://android-review.googlesource.com/#/q/Iaf856b84ad2d91f94f8e294f015b6341808fcc74))
- New `resizeModes` (`ScaleToBounds` and `RemeasureToBounds`) for `sharedBounds` to choose between scaling and remeasure. The previous `scaleIn/OutSharedContentToBounds` APIs are now deprecated. ([I0d41a](https://android-review.googlesource.com/#/q/I0d41aa7395b84f0232c1c64281e95f693526faa9))

Improvements to existing APIs:

- New `Modifier.animateContentSize` that takes an additional parameter for custom content alignment. ([I5623a](https://android-review.googlesource.com/#/q/I5623af336f137bb4464cbf7993942452e86bcd88), [b/269803907](https://issuetracker.google.com/issues/269803907))
- New Experimental `DeferredTargetAnimation` for animating size, position, or any other target that is unknown during instantiation. ([I60745](https://android-review.googlesource.com/#/q/I60745501487754b36b0e1986bc2bc7ecbac267e8))
- `SeekableTransitionState` replaces `snapTo()` with `seekTo()`, and adds a `snapTo()` that immediately changes the state to a destination state without any kind of animation.
- You may now pass a `periodicBias` value (Float) to `keyframesWithSpline`, this will make it so that the initial and final velocity of the spline are equal. Useful for repeatable animations using splines. The bias indicates how much each velocity (initial and final) gets modified to achieve periodicity. ([Ic1e6c](https://android-review.googlesource.com/#/q/Ic1e6c4996f8c25055955331384639b57e9ad86db), [b/292114811](https://issuetracker.google.com/issues/292114811))

The following APIs have become stable or been removed:

- `AnimatedVisibilityScope.transition` is now a stable API. `Modifier.animateEnterExit(..)` has also been made stable. ([I6c1d1](https://android-review.googlesource.com/#/q/I6c1d1ea596664892cc8928c1379bbe8d9b207f1e))
- `ApproachLayoutModifierNode` and `Modifier.approachLayout` are now stable, with new `isMeasurementApproachInProgress()` and `isPlacementApproachInProgress()` to replace the old `isMeasurementApproachComplete()` and `isPlacementApproachComplete()` respectively.
- Removed deprecated `intermediateLayout` modifier. ([I3e91c](https://android-review.googlesource.com/#/q/I3e91ca2cfabebde655491f063466d2e5642f055e))
- `LookaheadScope` APIs have been made stable. ([I21507](https://android-review.googlesource.com/#/q/I21507b73d88acc221e5963b76b9f1a83539342db))

### Version 1.7.0-rc01

August 21, 2024

`androidx.compose.animation:animation-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98bc1cf10201a973793b72d2ff1ae728070e47e4..d8995e2377dd4baad64b39becb6d480cadd05c86/compose/animation).

### Version 1.7.0-beta07

August 7, 2024

`androidx.compose.animation:animation-*:1.7.0-beta07` is released. Version 1.7.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16151cbc8a68e976da6f2b0f624c2e9883c55aa3..98bc1cf10201a973793b72d2ff1ae728070e47e4/compose/animation).

**Bug Fixes**

- Fixed `SharedTransitionScope` not drawing overlay items during transition in certain conditions, which would typically include usage with Navigation. ([Id65ab](https://android-review.googlesource.com/#/q/Id65abf8cc50fc08e246c0a85581df32be1983ecc), [b/347520198](https://issuetracker.google.com/issues/347520198))

### Version 1.7.0-beta06

July 24, 2024

`androidx.compose.animation:animation-*:1.7.0-beta06` is released. Version 1.7.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8346df8de9f86a546fc9c316113bd4a3cc82ede9..16151cbc8a68e976da6f2b0f624c2e9883c55aa3/compose/animation).

**Bug Fixes**

- Fixed `SeekableTransition` leaking transition states by properly cleaning up observations from `SnapshotStateObserver` when the transition is disposed. ([b9c7182](https://android.googlesource.com/platform/frameworks/support/+/b9c7182a9426d47a64dc995fa99ba0a65afc2428))
- Fixed edge cases where child Transitions are not properly marked complete when the parent completes. ([dc42216](https://android.googlesource.com/platform/frameworks/support/+/dc42216d1b941eadc40e3851da60564a3d6882a4))

### Version 1.7.0-beta05

July 10, 2024

`androidx.compose.animation:animation-*:1.7.0-beta05` is released. Version 1.7.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/487d2b07dba29c903cfd87a8dc7f99483084ebb6..8346df8de9f86a546fc9c316113bd4a3cc82ede9/compose/animation).

**Bug Fixes**

- The Transition property `totalDurationNanos` now can be properly read within a `snapshotFlow`.

### Version 1.7.0-beta04

June 26, 2024

`androidx.compose.animation:animation-*:1.7.0-beta04` is released. Version 1.7.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c29f7383c14ede0af9cb64be9f3eee63714bc73c..487d2b07dba29c903cfd87a8dc7f99483084ebb6/compose/animation).

### Version 1.7.0-beta03

June 12, 2024

`androidx.compose.animation:animation-*:1.7.0-beta03` is released. Version 1.7.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a123f646cfea1599f9efead6da546b0c26063fa..c29f7383c14ede0af9cb64be9f3eee63714bc73c/compose/animation).

### Version 1.7.0-beta02

May 29, 2024

`androidx.compose.animation:animation-*:1.7.0-beta02` is released. Version 1.7.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..1a123f646cfea1599f9efead6da546b0c26063fa/compose/animation).

### Version 1.7.0-beta01

May 14, 2024

`androidx.compose.animation:animation-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/animation).

**API Changes**

- New `resizeModes` (`ScaleToBounds` and `RemeasureToBounds`) for `sharedBounds` to choose between scaling and remeasure. The previous `scaleIn/OutSharedContentToBounds` APIs are now deprecated. ([I0d41a](https://android-review.googlesource.com/#/q/I0d41aa7395b84f0232c1c64281e95f693526faa9))

**External Contribution**

- Experimental `SharedTransitionScope` is now an interface rather than a class by Steven Schoen. ([Iaf856](https://android-review.googlesource.com/#/q/Iaf856b84ad2d91f94f8e294f015b6341808fcc74), [b/338415048](https://issuetracker.google.com/issues/338415048), [b/338414702](https://issuetracker.google.com/issues/338414702))

### Version 1.7.0-alpha08

May 1, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha08` is released. Version 1.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7/compose/animation).

**API Changes**

- `LookaheadScope` APIs have been made stable. ([I21507](https://android-review.googlesource.com/#/q/I21507b73d88acc221e5963b76b9f1a83539342db))

**External Contribution**

- Clear start animation time after `SeekableTransitionState` animates/snaps by Steven Schoen ([1ca89529](https://android.googlesource.com/platform/frameworks/support/+/1ca895298f43862e40f0ac14c300d0432d42153d))

### Version 1.7.0-alpha07

April 17, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha07` is released. Version 1.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/animation).

**New Features**

- New shared element transition APIs await your usage and feedback. These new experimental APIs enable tagging layouts as shared across layout tree using the provided modifiers, producing smoothly changing bounds when one set of shared content exits and the other set enters. ([Icb0b9](https://android-review.googlesource.com/#/q/Icb0b953f1eaff80a582b1edd3f21f9f8031cf8b0))
- New `scaleInSharedContentToBounds` and `scaleOutSharedContentToBounds` to scale content in `sharedBounds` ([I731c1](https://android-review.googlesource.com/#/q/I731c18d0bd9a533bbf53ebba62f4638bdc758cbe))

**API Changes**

- `AnimatedVisibilityScope.transition` is now a stable API. `Modifier.animateEnterExit(..)` has also been made stable. ([I6c1d1](https://android-review.googlesource.com/#/q/I6c1d1ea596664892cc8928c1379bbe8d9b207f1e))
- `ApproachLayoutModifierNode` and `Modifier.approachLayout` are now stable, with new `isMeasurementApproachInProgress()` and `isPlacementApproachInProgress()` to replace the old `isMeasurementApproachComplete()` and `isPlacementApproachComplete()` respectively.
- Removed deprecated `intermediateLayout` modifier. ([I3e91c](https://android-review.googlesource.com/#/q/I3e91ca2cfabebde655491f063466d2e5642f055e))
- You may now pass a `periodicBias` value (Float) to `keyframesWithSpline`, this will make it so that the initial and final velocity of the spline are equal. Useful for repeatable animations using splines. The bias indicates how much each velocity (initial and final) gets modified to achieve periodicity. ([Ic1e6c](https://android-review.googlesource.com/#/q/Ic1e6c4996f8c25055955331384639b57e9ad86db), [b/292114811](https://issuetracker.google.com/issues/292114811))

**Bug Fixes**

- Fixed over-shooting and under-shooting easing curves that would previously be clamped to 0..1 ([I38747](https://android-review.googlesource.com/#/q/I38747d944b9fc437c77174ccba67beaa6fc7a8fc))

### Version 1.7.0-alpha06

April 3, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha06` is released. Version 1.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/animation).

**New Features**

- Item appearance and disappearance animation support was added into `LazyColumn` and `LazyRow`. Previously it was possible to add `Modifier.animateItemPlacement()` modifier in order to support placement (reordering) animations. We deprecated this modifier and introduced a new non-experimental modifier called `Modifier.animateItem()` which allows you to support all three animation types: appearance (fade in), disappearance (fade out) and reordering. ([I2d7f7](https://android-review.googlesource.com/#/q/I2d7f7a376cea26c0a36a59a4586d2705ab04cab7), [b/330152398](https://issuetracker.google.com/issues/330152398), [b/150812265](https://issuetracker.google.com/issues/150812265))

**Bug Fixes**

- Improved performance of `updateTransition` API.

### Version 1.7.0-alpha05

March 20, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha05` is released. Version 1.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/animation).

**API Changes**

- `SeekableTransitionState` replaces `snapTo()` with `seekTo()`, and adds a `snapTo()` that immediately changes the state to a destination state without any kind of animation.

### Version 1.7.0-alpha04

March 6, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha04` is released. Version 1.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/animation).

**API Changes**

- New API `Path.reverse()` to reverse a path's direction ([I36348](https://android-review.googlesource.com/#/q/I36348a9731a210b34cd4c177d19ef617a87d8832))

### Version 1.7.0-alpha03

February 21, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/animation)

**New Features**

- New `Modifier.animateContentSize` that takes an additional parameter for custom content alignment. ([I5623a](https://android-review.googlesource.com/#/q/I5623af336f137bb4464cbf7993942452e86bcd88), [b/269803907](https://issuetracker.google.com/issues/269803907))
- New Experimental `DeferredTargetAnimation` for animating size, position, or any other target that is unknown during instantiation. ([I60745](https://android-review.googlesource.com/#/q/I60745501487754b36b0e1986bc2bc7ecbac267e8))

### Version 1.7.0-alpha02

February 7, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/animation)

**Bug Fixes**

- Compatibility fix for `KeyframesSpec`. ([I2bdf3](https://android-review.googlesource.com/#/q/I2bdf33634d19c8077a35ee21020fb8991eb6d5a1), [b/322214617](https://issuetracker.google.com/issues/322214617))
- Fixed `Modifier.animateContentSize` not resetting properly when used in `LazyList`. ([I070512](https://android-review.googlesource.com/#/q/I070512423d2c358326c50fae32ed0696d6fe9193), [b/322525716](https://issuetracker.google.com/issues/322525716))
- Fixed `IllegalStateException` on `KeyframesSpec` when using out of range timestamps. ([I341b8](https://android-review.googlesource.com/#/q/I341b862ed2c5acb92ec596e5d4cb0445c5663ad6), [b/322839811](https://issuetracker.google.com/issues/322839811))

### Version 1.7.0-alpha01

January 24, 2024

`androidx.compose.animation:animation-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f/compose/animation)

## Version 1.6

### Version 1.6.8

June 12, 2024

`androidx.compose.animation:animation-*:1.6.8` is released. Version 1.6.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a13a0e3b1197d66bfc19b9051576bc705f2c337..9dbbab668fd22cd643de4651197354a828aaa7b9/compose/animation).

### Version 1.6.7

May 1, 2024

`androidx.compose.animation:animation-*:1.6.7` is released. Version 1.6.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b..9a13a0e3b1197d66bfc19b9051576bc705f2c337/compose/animation).

### Version 1.6.6

April 17, 2024

`androidx.compose.animation:animation-*:1.6.6` is released. No changes since the previous release

### Version 1.6.5

April 3, 2024

`androidx.compose.animation:animation-*:1.6.5` is released. Version 1.6.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3..917ada96acf0ac343128c3f4af9bd67a4b80b99c/compose/animation).

### Version 1.6.4

March 20, 2024

`androidx.compose.animation:animation-*:1.6.4` is released. Version 1.6.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/22b329dfa8888198eb3024650d236b3afe6c0907..1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3/compose/animation).

### Version 1.6.3

March 6, 2024

`androidx.compose.animation:animation-*:1.6.3` is released. Version 1.6.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af119e2e31de85654fb7b2e5a2c7e724231131fd..22b329dfa8888198eb3024650d236b3afe6c0907/compose/animation).

### Version 1.6.2

February 21, 2024

`androidx.compose.animation:animation-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f639ccf09a84fa5af4a9016fa239539aeed40b94..af119e2e31de85654fb7b2e5a2c7e724231131fd/compose/animation)

### Version 1.6.1

February 7, 2024

`androidx.compose.animation:animation-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..f639ccf09a84fa5af4a9016fa239539aeed40b94/compose/animation)

**Bug Fixes**

- Compatibility fix for `KeyframesSpec`. ([I2bdf3](https://android-review.googlesource.com/#/q/I2bdf33634d19c8077a35ee21020fb8991eb6d5a1), [b/322214617](https://issuetracker.google.com/issues/322214617))

### Version 1.6.0

January 24, 2024

`androidx.compose.animation:animation-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/296c44d6ba03d2167bdea85d53e8387d7b1644f9..4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf/compose/animation)

### Version 1.6.0-rc01

January 10, 2024

`androidx.compose.animation:animation-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc038a4bc84de9ab20493d6efa8d26f4a70214ae..6dc685be02316455881d22b69d0bb8adbe768c4f/compose/animation)

### Version 1.6.0-beta03

December 13, 2023

`androidx.compose.animation:animation-*:1.6.0-beta03` is released. [Version 1.6.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15c82aaef0f1fd0307d6c00061859e5b6c4384c6..b76585a287cbcfdae38c3e16e5acbc6e26e808e2/compose/animation)

**API Changes**

- Temporarily removed `scaleInToFitContainer` and `scaleOutToFitContainer` from `AnimatedContentTransitionScope` as they require lookahead. They will be available when lookahead is on by default or opted-in in future releases.

### Version 1.6.0-beta02

November 29, 2023

`androidx.compose.animation:animation-*:1.6.0-beta02` is released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..15c82aaef0f1fd0307d6c00061859e5b6c4384c6/compose/animation)

### Version 1.6.0-beta01

November 15, 2023

`androidx.compose.animation:animation-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose/animation)

**API Changes**

- `ExitTransition.Hold` has been renamed to `ExitTransition.KeepUntilTransitionsFinished` to be more explicit. ([I1c490](https://android-review.googlesource.com/#/q/I1c4906213f267c9dabae03f15e6d9d9f05622581))
- You may now use `keyframesWithSpline` to interpolate any N-dimensional value using monotonic splines. It's particularly useful to interpolate positional values such as `Offset`, `IntOffset`, `DpOffset`. Added as Experimental API.

**Bug Fixes**

- Add renderer support for Sweep Gradient in `ArcLine`. ([I4d5bb](https://android-review.googlesource.com/#/q/I4d5bb5948d2216dca2a29d2449fd97519b2b65bb))
- Implement equals and hashcode for `PageSize.Fixed`. ([Ie3ede](https://android-review.googlesource.com/#/q/Ie3edea3aafd75068cd57c04aafdd7055ead20ad7), [b/300134276](https://issuetracker.google.com/issues/300134276))
- Fix binary compatibility issue with Window Inset change. ([Iee695](https://android-review.googlesource.com/#/q/Iee695f0f1b2bf24a820b5a1bccfe550d9c29a5fa))
- Remove material core layer for Material3 Chip/Button as the microbenchmarks show better performance without it. ([I55555](https://android-review.googlesource.com/#/q/I5555573520638dd3c7f0d202e048ae6fffde19e5))

### Version 1.6.0-alpha08

October 18, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/animation)

**API Changes**

- Deprecated `KeyframesSpecConfig#with` in favor `KeyframesSpecConfig#using` which preserves the builder pattern. ([I1d769](https://android-review.googlesource.com/#/q/I1d76980eee35ded738ac185a96857fdb048f7b22))

### Version 1.6.0-alpha07

October 4, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..1f7407d4293384a1b91bc142880e3525048b3443/compose/animation)

**API Changes**

- Fixed and Scrollable Tabrows now have Primary and Secondary variants. These correctly map to the color and indicator behavior as defined in Material3.
- `PrimaryScrollableTabRow` and `SecondaryScrollableTabRow` now expose scroll state. ([Iec8f5](https://android-review.googlesource.com/#/q/Iec8f5a2876a15865842a6f0d4a584b539e16892a), [b/260572337](https://issuetracker.google.com/issues/260572337))

### Version 1.6.0-alpha06

September 20, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/animation)

### Version 1.6.0-alpha05

September 6, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/animation)

**API Changes**

- Added `PathEasing` to enable an arbitrary path to be supplied to an easing curve. ([Idb4b9](https://android-review.googlesource.com/#/q/Idb4b92266c7716e199e033e6734b3524c3c968a4))

### Version 1.6.0-alpha04

August 23, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/animation)

**API Changes**

- Add `SeekableTransitionState` to allow developers to control the progress of a transition. ([I8e69d](https://android-review.googlesource.com/#/q/I8e69df11beeb580c8ba4552fc5d7647367a44dcc))

### Version 1.6.0-alpha03

August 9, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/animation)

**API Changes**

- New type of enter/exit transition that scales the content based on the size of the animating container during enter \& exit animation. `LookaheadScope` Composable fun and interface are now stable. ([Ifb2ce](https://android-review.googlesource.com/#/q/Ifb2ce945db06e291aeb0980872b427bf0a580ede))

### Version 1.6.0-alpha02

July 26, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/animation)

**API Changes**

- New `ExitTransition.Hold` to display outgoing content in `AnimatedContent` until both enter \& exit transition are finished. ([I5984f](https://android-review.googlesource.com/#/q/I5984fde342fe99f422eaaf18ea639205926af2ee))
- Additional annotations to specify allowed inputs to composables ([I51109](https://android-review.googlesource.com/#/q/I51109ce34ab8bb50a8104572d79d2a94b67f3b17))

### Version 1.6.0-alpha01

June 21, 2023

`androidx.compose.animation:animation-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..3b5b931546a48163444a9eddc533489fcddd7494/compose/animation)

**New Features**

- Enable `Modifier.animateContentSize` and `AnimatedVisibility` to be fully integrated into the lookahead system by reporting the target size in the lookahead pass.

**API Changes**

- New property in `IntrinsincMeasureScope` and its implementations (e.g. `MeasureScope`) to indicate whether the current measure pass is a lookahead pass. ([I7a812](https://android-review.googlesource.com/#/q/I7a8122bf09752d7afb6ace1a0b397a2632708e95))

**Bug Fixes**

- Removed allocations from spring animations. ([Ie9431](https://android-review.googlesource.com/#/q/Ie94317f7206752e917cd5e74eb19e6abede8e656))
- value parameter name for Enum.valueOf changed ([Ia9b89](https://android-review.googlesource.com/#/q/Ia9b89b3c1bd0407c9beac825c49477cdfc9c1f2a))
- more thrown exceptions from enum valueOf ([I818fe](https://android-review.googlesource.com/#/q/I818fed80f3a1af1a97b5b0de7882fb2e1b99ae62))

## Version 1.5

### Version 1.5.4

October 18, 2023

`androidx.compose.animation:animation-*:1.5.4` is released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ed495b997a532cc4cbe39abdbaa98b8fc6f3764..b6d5e6e62e40f6938bdbcfef1d6c8a79e25006f8/compose/animation)

### Version 1.5.3

October 4, 2023

`androidx.compose.animation:animation-*:1.5.3` is released. This version has no changes

### Version 1.5.2

September 27, 2023

`androidx.compose.animation:animation-*:1.5.2` is released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a2cac855f7723e1e485c20ac68d34dc8bb68d1e..2bc777611812ef8ef7329a332fbaf8348af05ec7/compose/animation)

### Version 1.5.1

September 6, 2023

`androidx.compose.foundation:foundation-*:1.5.1` is released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/foundation)

**Bug Fixes**

- Fixed text fields showing keyboard and being editable when `readOnly` is true. Also fixed the keyboard not showing when `readOnly` is changed from true to false while focused. ([I34a19](https://android-review.googlesource.com/#/q/I34a19a80d8f44b10f23db0ca0dd7b43b69311c7c), [b/246909589](https://issuetracker.google.com/issues/246909589))

### Version 1.5.1

September 6, 2023

`androidx.compose.animation:animation-*:1.5.1` is released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/animation)

### Version 1.5.0

August 9, 2023

`androidx.compose.animation:animation-*:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e423b92ad8e8707ff4031626131f05e33979eac8..65e3f15108d25a7e1c5c841c0855b21eca194070/compose/animation)

### Version 1.5.0-rc01

July 26, 2023

`androidx.compose.animation:animation-*:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81e6706c269471032b283755131d2aa4e8821a89..e423b92ad8e8707ff4031626131f05e33979eac8/compose/animation)

**Bug Fixes**

- Fixed an issue where calling `.value` on a primitive state type (like `MutableIntState`) would report a lint warning with an invalid fix. The inspection will now recommend migrating to the correct property. ([Iba953](https://android-review.googlesource.com/#/q/Iba9536e23d6d94f1056cf7859454e4e2d6ee03cb), [b/287279257](https://issuetracker.google.com/issues/287279257))

- An optional inspection to recommend migrating `mutableStateOf()` calls to their corresponding specialized types for primitives is available. Its lint ID is `AutoboxingStateCreation`. Previously, this inspection was enabled by default for all projects. To see this warning in Android Studio's editor and your project's lint outputs, change its severity from informational to warning (or higher) by declaring `warning "AutoboxingStateCreation"` inside your module's `build.gradle` or `build.gradle.kts` configuration as shown ([I34f7e](https://android-review.googlesource.com/#/q/I34f7ea540f782ae95630f7f94cab93d842dfdd0f)):

          android {
              lint {
                  warning "AutoboxingStateCreation"
              }
              ...
          }

### Version 1.5.0-beta03

June 28, 2023

`androidx.compose.animation:animation-*:1.5.0-beta03` is released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..24dc7b0781cb908b2385ec207ca1b3a72cb90093/compose/animation)

### Version 1.5.0-beta02

June 7, 2023

`androidx.compose.animation:animation-*:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d26ca4055c940126ae1663ad0d54aafd23205ea4..df792c9ff86d87f538bab5d7f9dd9f56e2437b15/compose/animation)

### Version 1.5.0-beta01

May 24, 2023

`androidx.compose.animation:animation-*:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..d26ca4055c940126ae1663ad0d54aafd23205ea4/compose/animation)

**API Changes**

- Removed allocations in recomposition, color animations, and `AndroidComposeView` ([Ib2bfa](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223))

**Bug Fixes**

- Removed allocations from spring animations ([Ie9431](https://android-review.googlesource.com/#/q/Ie94317f7206752e917cd5e74eb19e6abede8e656))

### Version 1.5.0-alpha04

May 10, 2023

`androidx.compose.animation:animation-*:1.5.0-alpha04` is released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/animation)

**API Changes**

- `ContentKey` is now supported in `AnimatedContent` to allow more control for when transition should happen. ([Ic069b](https://android-review.googlesource.com/#/q/Ic069b01c0d2b302c7527ed850c32ba68bfc0101f))

### Version 1.5.0-alpha03

April 19, 2023

`androidx.compose.animation:animation-*:1.5.0-alpha03` is released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/compose/animation)

**New Features**

- New default behavior for `SubcomposeLayout` in `LookaheadScope`. It allows `SubcomposeLayouts` that don't have conditional slots (e.g. `TabRow`, `Scaffold`, `BoxWithConstraints`, etc) to work nicely with lookahead animations.

**API Changes**

- New default `intermediateMeasurePolicy` that reuses measure policy from lookahead pass allows `SubcomposeLayout` subtypes without conditional slots such as `Scaffold`, `TabRow`, and `BoxWithConstraints` to work with lookahead by default. ([Id84c8](https://android-review.googlesource.com/#/q/Id84c8357e63905ea09b07acee91094489eb04402))
- Rename infix fun with to `togetherWith` for combining enter and exit transitions. New `AnimatedContentScope` as receiver for the content lambda. ([Ic39ae](https://android-review.googlesource.com/#/q/Ic39aee09d77a905e538a101264dc352e1fecbfc0))

### Version 1.5.0-alpha02

April 5, 2023

`androidx.compose.animation:animation-*:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/animation)

**New Features**

- New experimental API to support lookahead in `SubcomposeLayout`. This will allow `SubcomposeLayout` to function properly in a `LookaheadScope`. More out-of-the-box support for specific subtypes of `SubcomposeLayout` will come soon.

**API Changes**

- New `SubcomposeLayout` API that takes an additional intermediate measure policy for handling measure/layout logic during lookahead-based animations. ([I017d3](https://android-review.googlesource.com/#/q/I017d37b9d3c2f890387229bc8cfc6515913c1a3a))

### Version 1.5.0-alpha01

March 22, 2023

`androidx.compose.animation:animation-*:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/animation)

**API Changes**

- `AnimatedContent` APIs are now stable `AnimatedContentScope` has been renamed to `AnimatedContentTransitionScope`. `scaleIn` and `scaleOut` are now stable APIs. ([Iaf54e](https://android-review.googlesource.com/#/q/Iaf54e341fb897868b6bfa90d4ef81faa75b17ed5))

## Version 1.4

### Version 1.4.3

May 3, 2023

`androidx.compose.animation:animation:1.4.3`, `androidx.compose.animation:animation-core:1.4.3`, and `androidx.compose.animation:animation-graphics:1.4.3` are released with no changes (only a version bump).

### Version 1.4.2

April 19, 2023

`androidx.compose.animation:animation:1.4.2`, `androidx.compose.animation:animation-core:1.4.2`, and `androidx.compose.animation:animation-graphics:1.4.2` are released with no changes. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5..0872f930da585f7fbf6e17c74b1dc42045e8b2c6/compose/animation)

### Version 1.4.1

April 5, 2023

`androidx.compose.animation:animation:1.4.1`, `androidx.compose.animation:animation-core:1.4.1`, and `androidx.compose.animation:animation-graphics:1.4.1` are released with no changes. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c13b30cf6683e0a43585416f30b55e07bf2b560e..5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5/compose/animation)

### Version 1.4.0

March 22, 2023

`androidx.compose.animation:animation:1.4.0`, `androidx.compose.animation:animation-core:1.4.0`, and `androidx.compose.animation:animation-graphics:1.4.0` are released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..c5b142d6ab0494c996b2378d5008ac1cd6da75f3/compose/animation)

**Important changes since 1.3.0**

- Tooling label is supported in r`ememberInfiniteTransition` and all the extension functions on `InfiniteTransition` and Transition (e.g. `InfiniteTransition#animateColor`) ([I56ef7](https://android-review.googlesource.com/#/q/I56ef7627431ba19c7462719e2be3af7245249573))

### Version 1.4.0-rc01

March 8, 2023

`androidx.compose.animation:animation:1.4.0-rc01`, `androidx.compose.animation:animation-core:1.4.0-rc01`, and `androidx.compose.animation:animation-graphics:1.4.0-rc01` are released with no changes. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..6022301db806601f282c53b8cbb5a981923a1589/compose/animation)

### Version 1.4.0-beta02

February 22, 2023

`androidx.compose.animation:animation:1.4.0-beta02`, `androidx.compose.animation:animation-core:1.4.0-beta02`, and `androidx.compose.animation:animation-graphics:1.4.0-beta02` are released with no changes. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/animation)

### Version 1.4.0-beta01

February 8, 2023

`androidx.compose.animation:animation:1.4.0-beta01`, `androidx.compose.animation:animation-core:1.4.0-beta01`, and `androidx.compose.animation:animation-graphics:1.4.0-beta01` are released with no changes. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/animation)

### Version 1.4.0-alpha05

January 25, 2023

`androidx.compose.animation:animation:1.4.0-alpha05`, `androidx.compose.animation:animation-core:1.4.0-alpha05`, and `androidx.compose.animation:animation-graphics:1.4.0-alpha05` are released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/animation)

**Changes**

- No changes in animation libraries since the last alpha, version bump only

### Version 1.4.0-alpha04

January 11, 2023

`androidx.compose.animation:animation:1.4.0-alpha04`, `androidx.compose.animation:animation-core:1.4.0-alpha04`, and `androidx.compose.animation:animation-graphics:1.4.0-alpha04` are released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/animation)

**New Features**

- Tooling label is supported in `rememberInfiniteTransition` and all the extension functions on `InfiniteTransition` and `Transition` (e.g. `InfiniteTransition#animateColor`) ([I56ef7](https://android-review.googlesource.com/#/q/I56ef7627431ba19c7462719e2be3af7245249573))

**API Changes**

- `InfiniteTransition#TransitionAnimationState` and `InfiniteTransition#animations` APIs are now public. ([I36682](https://android-review.googlesource.com/#/q/I366825fb1f87ae8b2816645e9852174cb6f31cdd))

### Version 1.4.0-alpha03

December 7, 2022

`androidx.compose.animation:animation:1.4.0-alpha03`, `androidx.compose.animation:animation-core:1.4.0-alpha03`, and `androidx.compose.animation:animation-graphics:1.4.0-alpha03` are released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/animation)

**API Changes**

- In UI tests using a Compose rule, continuations resumed during `withFrameNanos` callbacks will not be dispatched until after all frame callbacks have finished running. This matches the behavior of compose when running normally. However, tests that rely on the old behavior may fail. This should only affect code that calls `withFrameNanos` or `withFrameMillis` directly, and has logic outside of callback passed to those functions that may need to be moved inside the callbacks. See the animation test changes in [this CL for examples](https://android-review.googlesource.com/#/q/Idb41309445a030c91e8e4ae05daa9642b450505c).
- Added optional `onPerformTraversals: (Long) -> Unit` parameter to `TestMonotonicFrameClock` constructor and factory function to run code after `withFrameNanos` callbacks but before resuming callers' coroutines. ([Idb413](https://android-review.googlesource.com/#/q/Idb41309445a030c91e8e4ae05daa9642b450505c), [b/254115946](https://issuetracker.google.com/issues/254115946), [b/222093277](https://issuetracker.google.com/issues/222093277), [b/255802670](https://issuetracker.google.com/issues/255802670))
- New param in `AnimatedContent` for tooling label ([Iebe2d](https://android-review.googlesource.com/#/q/Iebe2d30122367bdd626063c15cbd17fcfb049023))

### Version 1.4.0-alpha02

November 9, 2022

`androidx.compose.animation:animation:1.4.0-alpha02`, `androidx.compose.animation:animation-core:1.4.0-alpha02`, and `androidx.compose.animation:animation-graphics:1.4.0-alpha02` are released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/animation)

**API Changes**

- Add `ToolingState` to allow tooling to change internal states of Composable ([Ie6614](https://android-review.googlesource.com/#/q/Ie66147788cfde7ede84a94d9591b3a05c51209cb))

### Version 1.4.0-alpha01

October 24, 2022

`androidx.compose.animation:animation:1.4.0-alpha01`, `androidx.compose.animation:animation-core:1.4.0-alpha01`, and `androidx.compose.animation:animation-graphics:1.4.0-alpha01` are released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255..548c8ac2570ae6cf15798fea1380491f7d93796b/compose/animation)

**Bug Fixes**

- Fix incorrect interruption animation in AnimatedContent ([b/238662479](https://issuetracker.google.com/238662479))

## Version 1.3

### Version 1.3.3

January 11, 2023

`androidx.compose.animation:animation:1.3.3`, `androidx.compose.animation:animation-core:1.3.3`, and `androidx.compose.animation:animation-graphics:1.3.3` are released. [Version 1.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8476d588d4975cb86be01bf4e356c5605ad89d48..59e93356f8f2bfb40b6f56dc086c8b821bbebda6/compose/animation)

- No changes since the 1.3.2.

### Version 1.3.2

December 7, 2022

`androidx.compose.animation:animation:1.3.2`, `androidx.compose.animation:animation-core:1.3.2`, and `androidx.compose.animation:animation-graphics:1.3.2` are released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d29f2a87e3c1d5cb6dfde828400d67b6f161be63..8476d588d4975cb86be01bf4e356c5605ad89d48/compose/animation)

**Bug Fixes**

- Updated to support androidx.compose.ui 1.3.2

### Version 1.3.1

November 9, 2022

`androidx.compose.animation:animation:1.3.1`, `androidx.compose.animation:animation-core:1.3.1`, and `androidx.compose.animation:animation-graphics:1.3.1` are released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/animation)

### Version 1.3.0

October 24, 2022

`androidx.compose.animation:animation:1.3.0`, `androidx.compose.animation:animation-core:1.3.0`, and `androidx.compose.animation:animation-graphics:1.3.0` are released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/animation)

**Important changes since 1.2.0**

- New set of easing functions are made stable

### Version 1.3.0-rc01

October 5, 2022

`androidx.compose.animation:animation:1.3.0-rc01`, `androidx.compose.animation:animation-core:1.3.0-rc01`, and `androidx.compose.animation:animation-graphics:1.3.0-rc01` are released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/animation)

### Version 1.3.0-beta03

September 21, 2022

`androidx.compose.animation:animation:1.3.0-beta03`, `androidx.compose.animation:animation-core:1.3.0-beta03`, and `androidx.compose.animation:animation-graphics:1.3.0-beta03` are released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/animation)

- No changes since 1.3.0-beta02.

### Version 1.3.0-beta02

September 7, 2022

`androidx.compose.animation:animation:1.3.0-beta02`, `androidx.compose.animation:animation-core:1.3.0-beta02`, and `androidx.compose.animation:animation-graphics:1.3.0-beta02` are released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/animation)

- Removed Kotlin.experimental from the compiler options since it is depricated

### Version 1.3.0-beta01

August 24, 2022

`androidx.compose.animation:animation:1.3.0-beta01`, `androidx.compose.animation:animation-core:1.3.0-beta01`, and `androidx.compose.animation:animation-graphics:1.3.0-beta01` are released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/animation)

### Version 1.3.0-alpha03

August 10, 2022

`androidx.compose.animation:animation:1.3.0-alpha03`, `androidx.compose.animation:animation-core:1.3.0-alpha03`, and `androidx.compose.animation:animation-graphics:1.3.0-alpha03` are released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/animation)

**API Changes**

- New param in `Crossfade`, `animateAsState` and `Animatable` for tooling label ([Iac08a](https://android-review.googlesource.com/#/q/Iac08a13e7e685108821e311abcbd808537bfcd7b))
- Added `atFraction` function for defining keyframes at a fraction instead of at a specific duration. ([I20c76](https://android-review.googlesource.com/#/q/I20c7687134349bcd9a07a18bd4523b24b7f121d6), [b/232059455](https://issuetracker.google.com/issues/232059455))

### Version 1.3.0-alpha02

July 27, 2022

`androidx.compose.animation:animation:1.3.0-alpha02`, `androidx.compose.animation:animation-core:1.3.0-alpha02`, and `androidx.compose.animation:animation-graphics:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/animation)

### Version 1.3.0-alpha01

June 29, 2022

`androidx.compose.animation:animation:1.3.0-alpha01`, `androidx.compose.animation:animation-core:1.3.0-alpha01`, and `androidx.compose.animation:animation-graphics:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..8094b683499b4098092c01028b55a38b49e357f2/compose/animation)

**API Changes**

- New `LookaheadLayout` that supports a lookahead pass before the actual measure/layout. This allows a pre-calculation of the layout when it changes, while permitting the post-lookahead measure/layout to use the pre-calculated size/position to animate the size and positions towards the target. `SubcomposeLayouts` are not yet supported, but will be in an upcoming release. ([I477f5](https://android-review.googlesource.com/#/q/I477f57d1f9efeb0aafd9fb509a2cac0ad8edfaf8))

## Version 1.2

### Version 1.2.1

August 10, 2022

`androidx.compose.animation:animation:1.2.1`, `androidx.compose.animation:animation-core:1.2.1`, and `androidx.compose.animation:animation-graphics:1.2.1` are released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255/compose/animation)

### Version 1.2.0

July 27, 2022

`androidx.compose.animation:animation:1.2.0`, `androidx.compose.animation:animation-core:1.2.0`, and `androidx.compose.animation:animation-graphics:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ff668d1061ec9e732d65ec3bfa9dc3db50fd87a..1e0793130863c72dc4a2d02bc975128f3ef0158b/compose/animation)

**Important changes since 1.1.0**

- Compose animation now supports 'Animator duration scale' setting from Developer Options.
- A large selection of new experimental easing curves.
- `AnimatedImageVector` now supports `repeatCount` and `repeatMode`

### Version 1.2.0-rc03

June 29, 2022

`androidx.compose.animation:animation:1.2.0-rc03`, `androidx.compose.animation:animation-core:1.2.0-rc03`, and `androidx.compose.animation:animation-graphics:1.2.0-rc03` are released. [Version 1.2.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..e8af23f4f30713a3f6073d57558e7cde0f3056e9/compose/animation)

- No changes since 1.2.0-rc02.

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.animation:animation:1.2.0-rc02`, `androidx.compose.animation:animation-core:1.2.0-rc02`, and `androidx.compose.animation:animation-graphics:1.2.0-rc02` are released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/animation)

**Bug Fixes**

- Removed `ExperimentalEasingApi` annotation on Easing functions ([Ied441](https://android-review.googlesource.com/#/q/Ied4417b953ec8b423e06ae0efeef909f0f150e98))

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.animation:animation:1.2.0-rc01`, `androidx.compose.animation:animation-core:1.2.0-rc01`, and `androidx.compose.animation:animation-graphics:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/animation)

**API Changes**

- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.animation:animation:1.2.0-beta03`, `androidx.compose.animation:animation-core:1.2.0-beta03`, and `androidx.compose.animation:animation-graphics:1.2.0-beta03` are released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/animation)

**API Changes**

- Added Experimental Easing Curves for Animations ([I64a38](https://android-review.googlesource.com/#/q/I64a38836fbc396088ce965ea7c123abb50ed40f6))

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.animation:animation:1.2.0-beta02`, `androidx.compose.animation:animation-core:1.2.0-beta02`, and `androidx.compose.animation:animation-graphics:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/animation)

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.animation:animation:1.2.0-beta01`, `androidx.compose.animation:animation-core:1.2.0-beta01`, and `androidx.compose.animation:animation-graphics:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/animation)

- This is the first beta release of 1.2! There are no changes since the last alpha.

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.animation:animation:1.2.0-alpha08`, `androidx.compose.animation:animation-core:1.2.0-alpha08`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha08` are released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/animation)

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.animation:animation:1.2.0-alpha07`, `androidx.compose.animation:animation-core:1.2.0-alpha07`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha07` are released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/animation)

**API Changes**

- `AnimatedImageVector` now supports `repeatCount` and `repeatMode` ([Ia3e75](https://android-review.googlesource.com/#/q/Ia3e75fe74f9552c2a1ce4a0995d781009b7a5257), [b/199304067](https://issuetracker.google.com/issues/199304067))

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.animation:animation:1.2.0-alpha06`, `androidx.compose.animation:animation-core:1.2.0-alpha06`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha06` are released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/animation)

**API Changes**

- Updated parsing of vector drawables to support auto mirroring to flip the content of a `VectorPainter` if the current layout direction is RTL. ([I79cd9](https://android-review.googlesource.com/#/q/I79cd946811e9b06ff4186180c4f8eaa0dcdbc879), [b/185760237](https://issuetracker.google.com/issues/185760237))

**Bug Fixes**

- Updated Vector graphics APIs to use the proper composable annotation `@VectorComposable` instead of `@UiComposable` ([I942bc](https://android-review.googlesource.com/#/q/I942bccda1a1795a7f85143524db80c1fc13bc0b9))

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.animation:animation:1.2.0-alpha05`, `androidx.compose.animation:animation-core:1.2.0-alpha05`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha05` are released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/animation)

**API Changes**

- Hooray! Compose animation now supports 'Animator duration scale' setting from Developer Options. ([I5a4fc](https://android-review.googlesource.com/#/q/I5a4fc779a3fbfbcb2926ac1624cd679bb9b912ce), [b/161675988](https://issuetracker.google.com/issues/161675988))

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.animation:animation:1.2.0-alpha04`, `androidx.compose.animation:animation-core:1.2.0-alpha04`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha04` are released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/animation)

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.animation:animation:1.2.0-alpha03`, `androidx.compose.animation:animation-core:1.2.0-alpha03`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha03` are released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/animation)

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.animation:animation:1.2.0-alpha02`, `androidx.compose.animation:animation-core:1.2.0-alpha02`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha02` are released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/animation)

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.animation:animation:1.2.0-alpha01`, `androidx.compose.animation:animation-core:1.2.0-alpha01`, and `androidx.compose.animation:animation-graphics:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/animation)

**API Changes**

- Use `AnimatedImageVector.animatedVectorResource` instead of `animatedVectorResource` to load an `<animated-vector>` resource file.
  - Use `rememberAnimatedVectorResource` instead of `AnimatedImageVector#painterFor` to render an `AnimatedImageVector`. ([I9c300](https://android-review.googlesource.com/#/q/I9c3000cdfcfc571394431e44f4642a0233542990))

**Bug Fixes**

- Add toString methods to Animatable and AnimationResult. ([Icd3a6](https://android-review.googlesource.com/#/q/Icd3a67ac43b4446d62ddd5fd207a2d5ece86df0a))

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.animation:animation:1.1.1`, `androidx.compose.animation:animation-core:1.1.1`, and `androidx.compose.animation:animation-graphics:1.1.1` are released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/animation)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.animation:animation:1.1.0`, `androidx.compose.animation:animation-core:1.1.0`, and `androidx.compose.animation:animation-graphics:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/animation)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
- Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of 48x48dp, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.animation:animation:1.1.0-rc03`, `androidx.compose.animation:animation-core:1.1.0-rc03`, and `androidx.compose.animation:animation-graphics:1.1.0-rc03` are released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/animation)

**Bug Fixes**

- Updated to support Compose Material 1.1.0-rc03

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.animation:animation:1.1.0-rc01` and `androidx.compose.animation:animation-core:1.1.0-rc01` are released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/animation)

**API Changes**

- Use `AnimatedImageVector.animatedVectorResource` instead of `animatedVectorResource` to load an `<animated-vector>` resource file.
  - Use `rememberAnimatedVectorResource` instead of `AnimatedImageVector#painterFor` to render an `AnimatedImageVector`. ([I9c300](https://android-review.googlesource.com/#/q/I9c3000cdfcfc571394431e44f4642a0233542990))

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.animation:animation:1.1.0-beta04`, `androidx.compose.animation:animation-core:1.1.0-beta04`, and `androidx.compose.animation:animation-graphics:1.1.0-beta04` are released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/animation)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.animation:animation:1.1.0-beta03`, `androidx.compose.animation:animation-core:1.1.0-beta03`, and `androidx.compose.animation:animation-graphics:1.1.0-beta03` are released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/animation)

**API Changes**

- Added new modifier Modifier.onPlaced to allow placement change to be observed. Additional changes to child modifier's offset can therefore be made based on the observed placement change. ([I558fd](https://android-review.googlesource.com/#/q/I558fd6a0fc0788942efe09a6c3e33c6c62608904))
- New support for contentKey in Crossfade.
  ContentKey will be used for equality check by animation system.
  Therefore custom diffing on states can be achieved via specifying
  appropriate contentKey for different states.

  ContentKey will also be used as the key for save \& restore content. ([I2e055](https://android-review.googlesource.com/#/q/I2e055c2b42736633b544b653e9815255578e7169), [b/197907070](https://issuetracker.google.com/issues/197907070))

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.animation:animation:1.1.0-beta02`, `androidx.compose.animation:animation-core:1.1.0-beta02`, and `androidx.compose.animation:animation-graphics:1.1.0-beta02` are released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/animation)

**Bug Fixes**

- New animation APIs for supporting tooling. Specifically, they allow tooling to inspect the animations \& their configurations in a Transitions. ([I4116e](https://android-review.googlesource.com/#/q/I4116e0f930fdbbbf3c306e1c2aa32b71b257bd3d))

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.animation:animation:1.1.0-beta01`, `androidx.compose.animation:animation-core:1.1.0-beta01`, and `androidx.compose.animation:animation-graphics:1.1.0-beta01` are released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/animation)

**API Changes**

- New animation APIs for supporting tooling. Specifically, they allow tooling to inspect the animations \& their configurations in a Transitions. ([I4116e](https://android-review.googlesource.com/#/q/I4116e0f930fdbbbf3c306e1c2aa32b71b257bd3d))

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.animation:animation:1.1.0-alpha06`, `androidx.compose.animation:animation-core:1.1.0-alpha06`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/animation)

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.animation:animation:1.1.0-alpha05`, `androidx.compose.animation:animation-core:1.1.0-alpha05`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/animation)

**API Changes**

- `EnterTransition`, `ExitTransition`, and some of the
  `AnimatedVisibility` APIs have been made stable.
  `MutableTransitionState.isIdle` is also no longer experimental. ([I5072d](https://android-review.googlesource.com/#/q/I5072db0fff64678b726a90670668d1dc274cadab))

- **Breaking change** : lambdas in Enter/ExitTransition factories
  have been moved to the last position in the param list. ([I5072d](https://android-review.googlesource.com/#/q/I5072db0fff64678b726a90670668d1dc274cadab))

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.animation:animation:1.1.0-alpha04`, `androidx.compose.animation:animation-core:1.1.0-alpha04`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha04` are released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/animation)

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.animation:animation:1.1.0-alpha03`, `androidx.compose.animation:animation-core:1.1.0-alpha03`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha03` are released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/animation)

**New Features**

- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.animation:animation:1.1.0-alpha02`, `androidx.compose.animation:animation-core:1.1.0-alpha02`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/animation)

**API Changes**

- StartOffset is now supported in repeatable and infiniteRepeatable, as a way to delay the start time or fast forward the animation before the animation starts. This start offset will not be repeated ([Ic679f](https://android-review.googlesource.com/#/q/Ic679f995fa5d118ae5bd50966bc9d775557e06df), [b/195079908](https://issuetracker.google.com/issues/195079908))
- New Enter/Exit transition for scale. It can be used in combination with other types of Enter/ExitTransitions. ([I372da](https://android-review.googlesource.com/#/q/I372dade56f09168b8d5450c897550b93dd819e53), [b/191325593](https://issuetracker.google.com/issues/191325593))

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.animation:animation:1.1.0-alpha01`, `androidx.compose.animation:animation-core:1.1.0-alpha01`, and `androidx.compose.animation:animation-graphics:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/animation)

**API Changes**

- `AnimatedImageVector` and the related APIs are now in the new `androidx.compose.animation:animation-graphics` module. ([I60873](https://android-review.googlesource.com/#/q/I6087391a9869d2315a71422f24175f42ec085681))

**Bug Fixes**

- Moved `InfiniteAnimationPolicy` to :compose:ui ([I5eb09](https://android-review.googlesource.com/#/q/I5eb09c7aa24a85fd2e66cc9b84ea6c906dc5210a), [b/160602714](https://issuetracker.google.com/issues/160602714))

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.animation:animation:1.0.5` and `androidx.compose.animation:animation-core:1.0.5` are released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/animation)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.animation:animation:1.0.4` and `androidx.compose.animation:animation-core:1.0.4` are released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/animation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.animation:animation:1.0.3` and `androidx.compose.animation:animation-core:1.0.3` are released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/animation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.animation:animation:1.0.2` and `androidx.compose.animation:animation-core:1.0.2` are released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/animation)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.animation:animation:1.0.1` and `androidx.compose.animation:animation-core:1.0.1` are released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/animation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.animation:animation:1.0.0` and `androidx.compose.animation:animation-core:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/animation)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

**Known Issues**

- If you are using Android Studio Bumblebee Canary 4 or AGP `7.1.0-alpha04`/`7.1.0-alpha05`, you may hit the following crash:

        java.lang.AbstractMethodError: abstract method "void androidx.lifecycle.DefaultLifecycleObserver.onCreate(androidx.lifecycle.LifecycleOwner)"

  To fix, temporarily increase your minSdkVersion to 24+ in your `build.gradle` file. This issue will be fixed in the next version of Android Studio Bumblebee and AGP `7.1`. ([b/194289155](https://issuetracker.google.com/issues/194289155))

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.animation:animation:1.0.0-rc02` and `androidx.compose.animation:animation-core:1.0.0-rc02` are released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/animation)

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.animation:animation:1.0.0-rc01` and `androidx.compose.animation:animation-core:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/animation)

**Bug Fixes**

- Moved `InfiniteAnimationPolicy` to `androidx.compose.ui:ui` ([I5eb09](https://android-review.googlesource.com/#/q/I5eb09c7aa24a85fd2e66cc9b84ea6c906dc5210a), [b/160602714](https://issuetracker.google.com/issues/160602714))

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.animation:animation:1.0.0-beta09` and `androidx.compose.animation:animation-core:1.0.0-beta09` are released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/animation)

**API Changes**

- New `AnimatedContent` Composable. It manages its content change using customizable `ContentTransform` as new target content enters and initial content leaves. Different combination of enter and exit transitions can be used to produce a customized look and feel. As a part of the content transform, `AnimatedContent` automatically animates its size to match the incoming content. ([I2c3df](https://android-review.googlesource.com/#/q/I2c3df9070957cc144b13b404848b7fe4717dd2b8))
- Removed `ManualFrameClock`. If you need to control animations, use `composeTestRule.mainClock` instead. ([I3c3e8](https://android-review.googlesource.com/#/q/I3c3e8d0387c37ab3f3a29b648429056ac0eb6b26), [b/189951065](https://issuetracker.google.com/issues/189951065))

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

- Libraries can define these rules which will be packaged in AAR artifacts. When an app is then built which includes these artifacts, these rules are merged together and the merged rules are used to build a compact binary ART profile that is specific to the app. ART can then leverage this profile when the app is installed on devices in order to ahead-of-time compile a specific subset of the application to improve the performance of the application, especially the first run. Note that this will have no effect on debuggable applications.

### Version 1.0.0-beta08

June 2, 2021

`androidx.compose.animation:animation:1.0.0-beta08` and `androidx.compose.animation:animation-core:1.0.0-beta08` are released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/animation)

**Bug Fixes**

- Now `detectDragGesures`, `detectVerticalGestures`, and `detectHorizontalGestures` will consume the position change automatically, no need to call change.consumePositionChange in the onDrag callbacks ([I42fc4](https://android-review.googlesource.com/#/q/I42fc4a6529f73db228ae671097d10a0cda0d834b), [b/185096350](https://issuetracker.google.com/issues/185096350), [b/187320697](https://issuetracker.google.com/issues/187320697))
- `Modifier.onGloballyPositioned()` was changed to report the coordinates of this modifier in the modifier chain, not the layout coordinates after applying all the modifiers. This means that now the ordering of modifiers is affecting what coordinates would be reported. ([Ieb67d](https://android-review.googlesource.com/#/q/Ieb67da0c327c9dc323a4b0a8bf33dbb66f0611e3), [b/177926591](https://issuetracker.google.com/issues/177926591))

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.animation:animation:1.0.0-beta07` and `androidx.compose.animation:animation-core:1.0.0-beta07` are released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/animation)

> [!NOTE]
> **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
> `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

**API Changes**

- New `AnimatedVisibility` API that support visibility to be specified in a `MutableTransitionState`. This also allows the animation states to be observed external to `AnimatedVisibility` via `currentState` and `isIdle`.
  - New child transition support in Transition
  - Support custom exit/enter transition animation in AnimatedVisibility using AnimationScope.transition
  - New animateEnterExit modifier accessible for all children of AnimatedVisibility
  - Deprecated the AnimatedVisibility APIs that take an `initiallyVisible` parameter ([I702f3](https://android-review.googlesource.com/#/q/I702f3a6d948938130701e6ab91b77f0b6fe000c2))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.animation:animation:1.0.0-beta06` and `androidx.compose.animation:animation-core:1.0.0-beta06` are released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/compose/animation)

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.animation:animation:1.0.0-beta05` and `androidx.compose.animation:animation-core:1.0.0-beta05` are released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/animation)

**Bug Fixes**

- The AndroidManifest files from ui-test-manifest and ui-tooling-data are now compatible with Android 12 ([I6f9de](https://android-review.googlesource.com/#/q/I6f9dec0515ad6eb7fd232eeb124ee0164f4e90cb), [b/184718994](https://issuetracker.google.com/issues/184718994))

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.animation:animation:1.0.0-beta04` and `androidx.compose.animation:animation-core:1.0.0-beta04` are released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/animation)

**API Changes**

- Public instances of `RowScope`, `ColumnScope`, `BoxScope`, `BoxWithConstraintsScope` were removed. ([I4e83e](https://android-review.googlesource.com/#/q/I4e83e38b3bb85be593288720e6b9cdbe0032bceb), [b/181869067](https://issuetracker.google.com/issues/181869067))

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.animation:animation:1.0.0-beta03` and `androidx.compose.animation:animation-core:1.0.0-beta03` are released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/animation)

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.animation:animation:1.0.0-beta02` and `androidx.compose.animation:animation-core:1.0.0-beta02` are released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/animation)

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.animation:animation:1.0.0-beta01` and `androidx.compose.animation:animation-core:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/animation)

This is the first release of Compose 1.0.0 Beta.

**API Changes**

- `InteractionState` has been replaced with `[Mutable]InteractionSource`
  - Interfaces are responsible for emitting / collecting Interaction events.
  - Instead of passing `interactionState = remember { InteractionState() }` to components such as `Button` and `Modifier.clickable()`, use `interactionSource = remember { MutableInteractionSource() }`.
  - Instead of: `Interaction.Pressed in interactionState` you should instead use the extension functions on InteractionSource, such as InteractionSource.collectIsPressedAsState().
  - For complex use cases you can use InteractionSource.interactions to observe the stream of Interactions. See the InteractionSource documentation and samples for more information.
  - ([I85965](https://android-review.googlesource.com/#/q/I85965d0dba39d1740c097915d1d1a367eea2a78c), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/171913923](https://issuetracker.google.com/issues/171913923), [b/171710801](https://issuetracker.google.com/issues/171710801), [b/174852378](https://issuetracker.google.com/issues/174852378))
- smoothScrollBy and scrollBy methods' packages changed to `androidx.compose.foundation.gestures.*` ([I3f7c1](https://android-review.googlesource.com/#/q/I3f7c18be72b1b4e8d7958194b10d63d749f7d948), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Size modifiers were renamed. Modifier.width/height/size were renamed to requiredWidth/requiredHeight/requiredSize. Modifier.preferredWidth/preferredHeight/preferredSize were renamed to width/height/size. ([I5b414](https://android-review.googlesource.com/#/q/I5b4145953d360b1fb851c0056fc9a7875bb34088))
- Orientation has been moved to foundation package. VelocirtTracker moved from ui.gesture to ui.input.pointer. ([Iff4a8](https://android-review.googlesource.com/#/q/Iff4a887648735c4850dca0d8d95fd99d782d04bb), [b/175294473](https://issuetracker.google.com/issues/175294473))
- AnimationClockObservable and subclasses have been removed. AnimatedFloat has been removed. ([Icde52](https://android-review.googlesource.com/#/q/Icde5248072620b741bdf4d8cf59291e7b2994e6a), [b/177457083](https://issuetracker.google.com/issues/177457083))
- Modifier.draggable now accepts DraggableState instead of a simple lambda. you can create state via `rememberDraggableState { delta -> }` to get the same behaviour as before ([Ica70f](https://android-review.googlesource.com/#/q/Ica70f33e73b6691375c9bdf07d008bae7546d48a), [b/175294473](https://issuetracker.google.com/issues/175294473))
- animate, animatedValue, AnimatedValue APIs have been removed ([If27bc](https://android-review.googlesource.com/#/q/If27bc4f86851a978239709a6f7ddab8ec94070ca), [b/177457083](https://issuetracker.google.com/issues/177457083))
- AnimationEndReason.Interrupted is removed. CancellationException will be throws if animation is interrupted. ([I2cbbc](https://android-review.googlesource.com/#/q/I2cbbc6112cef6e750c10843846ee46cb9d077b03), [b/179695417](https://issuetracker.google.com/issues/179695417))
- TargetAnimation API has been removed. ([If47d1](https://android-review.googlesource.com/#/q/If47d1f88096955c131af20c1660a5c450d5b7ed9), [b/177457083](https://issuetracker.google.com/issues/177457083))

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.animation:animation:1.0.0-alpha12` and `androidx.compose.animation:animation-core:1.0.0-alpha12` are released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/animation)

**API Changes**

- `Modifier.pointerInput` now requires remember keys to indicate when the pointer input detection coroutine should restart for new dependencies. ([I849cd](https://android-review.googlesource.com/#/q/I849cd63912b2d4c86ebe0dd24a7d0e2eb7a4e6d1))
- Bounds has been renamed to DpRect ([I4b32a](https://android-review.googlesource.com/#/q/I4b32a75caa8a5e8a1b5a0051f9041855411876e4))
- Unified the param name for AnimationSpec to animationSpec across the animation system. Also constrain the Enter/ExitTransition to accept FiniteAnimationSpec. ([Ie47c5](https://android-review.googlesource.com/#/q/Ie47c54ef91d1a4330e4d6f0f18ec3cde78d903ad), [b/177457083](https://issuetracker.google.com/issues/177457083))
- Animatable.snapTo and Animatable.stop are now suspend functions ([If4288](https://android-review.googlesource.com/#/q/If42887504caa0a07a0d89477805b68ca51c9b3b4))
- Similarly to how we previously removed `state { 0 }` composable and now promote usage like `remember { mutableStateOf(0) }` we are going to remove `savedInstanceState { 0 }` composable. You should use `rememberSaveable { mutableStateOf(0) }` instead and it will save and restore automatically if the type used inside the MutableState can be stored in the Bundle. If previously you were passing a custom saver object now you need to use a new overload of rememberSaveable which has `stateSaver` parameter. The usage will look like this: `val holder = rememberSaveable(stateSaver = HolderSaver) { mutableStateOf(Holder(0)) }` ([Ib4c26](https://android-review.googlesource.com/#/q/Ib4c266902d166f119ea1770cccbc78ac25a54ff7), [b/177338004](https://issuetracker.google.com/issues/177338004))
- Updated Crossfade's method signature to be more consistent with the rest of the animation system. ([Ib05ed](https://android-review.googlesource.com/#/q/Ib05ed5405bd4a781d2d78c84b7c06c0d153e8dc2), [b/177457083](https://issuetracker.google.com/issues/177457083))
- rememberSavedInstanceState() was renamed to rememberSaveable() and moved to androidx.compose.runtime.saveable package. ([I1366e](https://android-review.googlesource.com/#/q/I1366e7fef0a5a56a43d6eeb3770967a9bf683380), [b/177338004](https://issuetracker.google.com/issues/177338004))
- RestorableStateHolder was renamed to SaveableStateHolder and moved to androidx.compose.runtime.saveable package. Inner method RestorableStateProvider was renamed to SaveableStateProvider. Generic type was removed so you can just pass Any as a key. Experimental annotation is not needed anymore. ([I0902e](https://android-review.googlesource.com/#/q/I0902eb1618d36d08ade37be7b6a9453d85b1af62), [b/174598702](https://issuetracker.google.com/issues/174598702))
- Updated Modifier.animateContentSize API to be consistent with the rest of the animation system. ([I0bf75](https://android-review.googlesource.com/#/q/I0bf752ff98bd11094a834099cbd1b42c600ebcaf), [b/177457083](https://issuetracker.google.com/issues/177457083))
- AnimatedValue/Float is now deprecated. Please use Animatable instead. ([I71345](https://android-review.googlesource.com/#/q/I713457f88b04e50fbc5deb70a5bb7bbcf777e630), [b/177457083](https://issuetracker.google.com/issues/177457083))
- tapGestureFilter, doubleTapGestureFilter, longPressGestureFilter and pressIndicaitonGestureFilter have been deprecated. Use Modifier.clickable or Modifier.pointerInput with detectTapGestures function instead. ([I6baf9](https://android-review.googlesource.com/#/q/I6baf95f881b6fa6890ca1d065d49fef3e27bce83), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Introduced an `InfiniteAnimationPolicy` coroutine context element that will be applied in infinite animations. By default no policy is installed, except when running tests with `ComposeTestRule`. ([I50ec4](https://android-review.googlesource.com/#/q/I50ec421d7db495459a61c9282dbc2bfbc1f1ad02), [b/151940543](https://issuetracker.google.com/issues/151940543))
- Destructuring and copy() methods have been removed from several classes where they were rarely used. ([I26702](https://android-review.googlesource.com/#/q/I267021d3a45314acc9a169f6bbdfbfb4295a448c), [b/178659281](https://issuetracker.google.com/issues/178659281))
- Playtime in animation is now unfiied to nanoseconds ([If776a](https://android-review.googlesource.com/#/q/If776ab3406909ddf6d841dc2e71fc0889db77047))
- The compose:runtime-dispatch artifact is now deprecated. MonotonicFrameClock can now be found in compose:runtime and AndroidUiDispatcher can be found in compose:ui. ([Ib5c36](https://android-review.googlesource.com/#/q/Ib5c36a427306eceac4b9b16b52a091e864e5b936))
- Added `Animation.isInfinite` and `VectorizedAnimationSpec.isInfinite` that signal if an animation is infinite or not. This can be used in implementations of animations to have special handling of such animations. For example, a special "time remaining" message can be shown, or during tests the animation can be cancelled to prevent waiting for idleness indefinitely. ([Iebb05](https://android-review.googlesource.com/#/q/Iebb05e9d158b4fe81d037ab28e113da4926c50cd), [b/151940543](https://issuetracker.google.com/issues/151940543))
- Use Long instead of Uptime as animation time type ([Ie3aa7](https://android-review.googlesource.com/#/q/Ie3aa71cd8bf9ff66e74daa482b6ca5a6af9d15e2), [b/177420019](https://issuetracker.google.com/issues/177420019))

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.animation:animation:1.0.0-alpha11` and `androidx.compose.animation:animation-core:1.0.0-alpha11` are released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/animation)

**API Changes**

- TransitionDefinition-based Transition has been deprecated ([I0ac57](https://android-review.googlesource.com/#/q/I0ac57acd13386d028dfe0840e8ce509362cf107e))
- A label field is added for Transition and child animations to be displayed in tools ([I619fb](https://android-review.googlesource.com/#/q/I619fb982527ac50dc6d0bdac0227b2d830b81397))
- animateAsState is now animateFooAsState, where Foo is the type of the variable being animated. e.g. Float, Dp, Offset, etc ([Ie7e25](https://android-review.googlesource.com/#/q/Ie7e25c8978996334b0dcc757b07df1434ff346aa))
- New InfiniteTransition that runs any number of child animations. ([I1da81](https://android-review.googlesource.com/#/q/I1da81724c9f9d1c20f5c24b3170f7c9f899fcb23))
- Changes Material stateful parameter interfaces to have @Composable functions that return `State<T>`. Adds Animatable.asState() to make it easier to convert an Animatable to a State. Also changes animateElevation to be a suspend extension on Animatable. ([If613c](https://android-review.googlesource.com/#/q/If613cc7c751a11b77a03f8066b233b7e55cb67e0))

**Bug Fixes**

- onCommit, onDispose, and onActive have been deprecated in favor of SideEffect and DisposableEffect APIs ([If760e](https://android-review.googlesource.com/#/q/If760ec2a190c4121a35006695d953010ac22a43a))
- Initial State in updateTransition is now supported ([Ifd51d](https://android-review.googlesource.com/#/q/Ifd51d5c737b86d52282c18e29b89e75e1c0bea35))
- Content description parameter has been added to the Image and Icon. It is used to provide description to the accessibility services ([I2ac4c](https://android-review.googlesource.com/#/q/I2ac4c1058ed0bf1e5756cc6cdae546806974409e))
- invalidate and compositionReference() are now deprecated in favor of currentRecomposeScope and rememberCompositionReference respectively. ([I583a8](https://android-review.googlesource.com/#/q/I583a8efa6e3d3bc303792b825b948b3722ada103))
- Duration and Uptime will be replace with Long milliseconds, and this step removes the dependency of pointer input on those classes. ([Ia33b2](https://android-review.googlesource.com/#/q/Ia33b2d6835861501019481b388cb2c99441c346c), [b/175142755](https://issuetracker.google.com/issues/175142755), [b/177420019](https://issuetracker.google.com/issues/177420019))
- clickable, toggleable and selectable can be created outside of composition now ([I0a130](https://android-review.googlesource.com/#/q/I0a130bfa57713c96cc8b52c67becd32145526685), [b/172938345](https://issuetracker.google.com/issues/172938345), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Easing has been changed to a functional interface ([Ib14e5](https://android-review.googlesource.com/#/q/Ib14e513b2c4b839287535bda19ae93375a4baa73))
- New `items(count: Int)` factory method for scope of LazyColumn/LazyRow/LazyVerticalGrid. `items(items: List)` and `itemsIndexed(items: List)` are now extension functions so you have to manually import them when used. New extension overloads for Arrays: items(items: Array) and itemsIndexed(Array) ([I803fc](https://android-review.googlesource.com/#/q/I803fc5f25fac55855c710ff5064f11525f7b6010), [b/175562574](https://issuetracker.google.com/issues/175562574))
- Leverage TestCoroutineDispatcher in testing ([I532b6](https://android-review.googlesource.com/#/q/I532b68e37ea6f72964fdcc267e397d285cffd9ad))
- Removed PointerInputData and modified PointerInputChange to give it all of PointerInputData's fields. Made PointerInputEvent and PointerInputEventData internal because they aren't used in any public API. ([Ifff97](https://android-review.googlesource.com/#/q/Ifff970815031482a0ac1d5dab42a6156e10154b1), [b/175142755](https://issuetracker.google.com/issues/175142755))

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.animation:animation:1.0.0-alpha10` and `androidx.compose.animation:animation-core:1.0.0-alpha10` are released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/animation)

**API Changes**

- Modified Velocity to have component parts and mathematical operations. ([Ib0447](https://android-review.googlesource.com/#/q/Ib0447d694d7c5dc82fcef7448faeb0cdda87fced))
- Renamed `@ExperimentalTesting` to `@ExperimentalTestApi` to be consistent with similar experimental api annotations ([Ia4502](https://android-review.googlesource.com/#/q/Ia4502a82d5b66328b6e3e3cd322614939816901e), [b/171464963](https://issuetracker.google.com/issues/171464963))
- Renamed Position to DpOffset and removed getDistance() ([Ib2dfd](https://android-review.googlesource.com/#/q/Ib2dfde4ceb450e417ff759bdabbc74d2506a44c9))
- Removed Any.identityHashCode() public api ([I025d7](https://android-review.googlesource.com/#/q/I025d720aec64ebd2182787b9200ca9b3827d5436))

**Bug Fixes**

- New coroutine-based API `Animatable` that ensures mutual exclusiveness among its animations. New DecayAnimationSpec to support multi-dimensional decay animation ([I820f2](https://android-review.googlesource.com/#/q/I820f29e24eaa512515c776db971444290dea97e9), [b/168014930](https://issuetracker.google.com/issues/168014930))
- `animate()` is now replaced with `animateAsState()`, which returns a `State<T>` instead of `T`. This allows better performance, as the invalidation scope can be narrowed down to where the State value is read. ([Ib179e](https://android-review.googlesource.com/#/q/Ib179e3f5f4bf3b72f7445fc22e73c46af7cf74de))

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.animation:animation:1.0.0-alpha09` and `androidx.compose.animation:animation-core:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/animation)

**API Changes**

- Moved Dp.VectorConverter, Position.VectorConverter, etc to animation-core, and deprecated the old VectorConveters ([If0c4b](https://android-review.googlesource.com/#/q/If0c4bbdec55ec9d6436d74156db6f993904aae47))
- Introduced a whole new set of Transition APIs with improved ease of use, and support for dynamically added animations, and dynamically calculated animation targets. This APIs are marked experimental for easy differentiation from the TransitionDefinition-based API. ([Ia7fe3](https://android-review.googlesource.com/#/q/Ia7fe35961a5c50972f149562bb66c4b87b9302ac))

**Bug Fixes**

- Lambdas in offset modifiers now return IntOffset rather than Float. ([Ic9ee5](https://android-review.googlesource.com/#/q/Ic9ee5c05df4c89993ee19f19ddd327a986f21bc1), [b/174137212](https://issuetracker.google.com/issues/174137212), [b/174146755](https://issuetracker.google.com/issues/174146755))
- Deprecate LazyColumnFor, LazyRowFor, LazyColumnForIndexed and LazyRowForIndexed. Use LazyColumn and LazyRow instead ([I5b48c](https://android-review.googlesource.com/#/q/I5b48c8a3b1fef2f603ab69ded1d19709aa9f87fb))
- For suspending pointer input APIs, renamed HandlePointerInputScope to AwaitPointerEventScope and handlePointerInput() to awaitPointerEventScope(). ([Idf0a1](https://android-review.googlesource.com/#/q/Idf0a1b94f065e72b65361cdf616122ed7939c3e7), [b/175142755](https://issuetracker.google.com/issues/175142755))
- New infiniteRepeatable function for creating an InfiniteRepeatableSpec ([I668e5](https://android-review.googlesource.com/#/q/I668e501c0c9061aa94b258ec9646617e0f77faf1))
- Removed ExperimentalPointerInput annotation ([Ia7a24](https://android-review.googlesource.com/#/q/Ia7a2473869400fc92ce70c802f42df9af7129386))

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.animation:animation:1.0.0-alpha08` and `androidx.compose.animation:animation-core:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/animation)

> [!NOTE]
> **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

**API Changes**

- Added lint check for composable lambda parameter naming and position, to check for consistency with Compose guidelines. Also migrated some APIs using `children` as the name for their trailing lambda to `content`, according to the lint check and guidance. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48e38a2896785b521814d95c9fb624d2807315))
- Previously Deprecated APIs were removed:
  - `Modifier.onPositioned` was removed, use `Modifier.onGloballyPositioned`.
  - `Modifier.onDraw` was removed, use `Modifier.onDrawBehind`.
  - `Modifier.plus` was removed, use `Modifier.then`.
  - `Color.Unset` was removed, use `Color.Unspecified`.
  - `PxBounds` class was removed, use `Rect` instead.
  - ([Ie9d02](https://android-review.googlesource.com/#/q/Ie9d0239f96922f1db769c38f6f970532a8f54ff3), [b/172562222](https://issuetracker.google.com/issues/172562222))
- Temporarily added option to let the TestAnimationClock be driven by the MonotonicFrameClock ([I1403b](https://android-review.googlesource.com/#/q/I1403ba3d82adc530d885192aa696c4363456a4c1), [b/173402197](https://issuetracker.google.com/issues/173402197))

**Bug Fixes**

- Renamed Modifier.drawLayer to Modifier.graphicsLayer Also updated related classes to GraphicsLayer as per API council feedback. ([I0bd29](https://android-review.googlesource.com/#/q/I0bd297065427d19715e4e33480f7be87e51ff48a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- Added Modifier.scale/rotate APIs as conveniences for drawLayer.
  - Renamed Modifier.drawOpacity to Modifier.alpha
  - Renamed Modifier.drawShadow to Modifier.shadow ([I264ca](https://android-review.googlesource.com/#/q/I264ca72b36ea62fd615436849203895ed742fa1e), [b/173208140](https://issuetracker.google.com/issues/173208140))
- Made PointerInputData's uptime and position fields non-nullable. ([Id468a](https://android-review.googlesource.com/#/q/Id468a0ef7c00c30a89114ea8dc95fa019961e189))
- offsetPx modifiers were renamed to offset. They are now taking lambda parameters instead of State. ([Ic3021](https://android-review.googlesource.com/#/q/Ic302174ef9cffa7ef806d1668f81cb89159363f2), [b/173594846](https://issuetracker.google.com/issues/173594846))
- New APIs for running animations in coroutines ([Ied662](https://android-review.googlesource.com/#/q/Ied662fbc4c4c373fba7877c1421ee76c49fd69b1))
- Deprecated Ambients named with `Ambient` as their suffix, and replaced them with new properties prefixed with Ambient, following other Ambients and Compose API guidelines. ([I33440](https://android-review.googlesource.com/#/q/I334403cc490ea913b8980d29e2cbe08e98ad7945))
- Time control in tests (TestAnimationClock and its usages) is now experimental ([I6ef86](https://android-review.googlesource.com/#/q/I6ef86c5f530422c7c751bdb086a691cbc2e837f3), [b/171378521](https://issuetracker.google.com/issues/171378521))
- Remove old ui-test module and its stubs ([I3a7cb](https://android-review.googlesource.com/#/q/I3a7cbbe376d0542955983fb09afd2dc37be7647e))
- `RestorableStateHolder.withRestorableState` function was renamed to `RestorableStateProvider` ([I66640](https://android-review.googlesource.com/#/q/I66640dac2f299f5d85d270f2aa1c5d6fc8ab7128))
- The Alignment interface was updated and made functional. ([I46a07](https://android-review.googlesource.com/#/q/I46a0791e261b6f305804797cdda7fdd2ef405305), [b/172311734](https://issuetracker.google.com/issues/172311734))

### Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.animation:animation:1.0.0-alpha07` and `androidx.compose.animation:animation-core:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/animation)

**Bug Fixes**

- The foundation AmbientTextStyle, ProvideTextStyle, and AmbientContentColor have been deprecated. Instead use the new versions available in the Material library. For non-Material applications, you should instead create your own design system specific theming ambients that can be consumed in your own components. ([I74acc](https://android-review.googlesource.com/#/q/I74accf7166eaca28e9e2d14402ed08d80f8625ab), [b/172067770](https://issuetracker.google.com/issues/172067770))
- foundation.Text has been deprecated and replaced with material.Text. For a basic, unopinionated text API that does not consume values from a theme, see androidx.compose.foundation.BasicText. ([If64cb](https://android-review.googlesource.com/#/q/If64cbdd89497f171edfd1b4de907123f73279e8d))
- MeasureResult was moved out of MeasureScope. ([Ibf96d](https://android-review.googlesource.com/#/q/Ibf96ddadae8115015066dcda2026a57b87c2ead6), [b/171184002](https://issuetracker.google.com/issues/171184002))
- Several layout related symbols were moved from androidx.compose.ui to androidx.compose.layout.ui. ([I0fa98](https://android-review.googlesource.com/#/q/I0fa982d87929e5ca9e3a32762fe9cf1fa8b8cfef), [b/170475424](https://issuetracker.google.com/issues/170475424))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.animation:animation:1.0.0-alpha06` and `androidx.compose.animation:animation-core:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/animation)

**API Changes**

- Enable transitions in ComposeTestRule; remove option to enable the blinking cursor from ComposeTestRule. ([If0de3](https://android-review.googlesource.com/#/q/If0de36db743b7f57b161b0fe6324565750436866))

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.animation:animation:1.0.0-alpha05` and `androidx.compose.animation:animation-core:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/animation)

**API Changes**

- New Animation interface and subclasses: These classes store the start and end conditions for animations, and therefore allow value and velocity to be queried via only playtime ([Ie95bd](https://android-review.googlesource.com/#/q/Ie95bdaad0a1cf18dc18548fd511ef6f31faa1e59), [b/163329867](https://issuetracker.google.com/issues/163329867))

**Bug Fixes**

- OnPositionedModifier is renamed to OnGloballyPositionedModifier and onPositioned() is renamed to onGloballyPositioned(). ([I587e8](https://android-review.googlesource.com/#/q/I587e8b151079d9d9506d86caa4283b7108958de4), [b/169083903](https://issuetracker.google.com/issues/169083903))
- Deprecates contentColor() and currentTextStyle() APIs, and replaces them with AmbientContentColor and AmbientTextStyle ambients respectively. You can access the current value by using `.current` on the ambient property, as with any other ambient. This was change was made for consistency and to avoid having multiple ways to accomplish the same thing. Additionally renames some ambient properties to better describe their purpose as follows:

  - ContentColorAmbient -\> AmbientContentColor
  - TextStyleAmbient -\> AmbientTextStyle
  - IndicationAmbient -\> AmbientIndication
  - EmphasisAmbient -\> AmbientEmphasisLevels
  - RippleThemeAmbient -\> AmbientRippleTheme ([I37b6d](https://android-review.googlesource.com/#/q/I37b6dccb9751f2a9eb550f42da32bf4b1bff4296))

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.animation:animation:1.0.0-alpha04` and `androidx.compose.animation:animation-core:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/animation)

> [!NOTE]
> **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

**API Changes**

- Annotated rootAnimationClockFactory, transitionsEnabled, blinkingCursorEnabled and textInputServiceFactory with @VisibleForTesting, make them internal API and hide their kdoc ([I554eb](https://android-review.googlesource.com/#/q/I554ebefac18b216d51e387e5fd1c3a735fde9500), [b/168308412](https://issuetracker.google.com/issues/168308412))

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
- We prevented static imports of contents of layout scopes (e.g. alignWithSiblings in RowScope). The explicit scope alternative should be used instead: `with(RowScope) { Modifier.alignWithSiblings(FirstBaseline) }`. ([I216be](https://android-review.googlesource.com/#/q/I216be6984d82e0a41432ac5b89f7d6240eef1b9d), [b/166760797](https://issuetracker.google.com/issues/166760797))

### Version 1.0.0-alpha03

September 16, 2020

`androidx.compose.animation:animation:1.0.0-alpha03` and `androidx.compose.animation:animation-core:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..18a5639262f8504db530176550e338a5d0e2e044/compose/animation)

**Bug Fixes**

- Usages of gravity were consistently renamed to align or alignment in layout APIs. ([I2421a](https://android-review.googlesource.com/#/q/I2421a4d640a7086079739cd0e569aef70bb48577), [b/164077038](https://issuetracker.google.com/issues/164077038))

### Version 1.0.0-alpha02

September 2, 2020

`androidx.compose.animation:animation:1.0.0-alpha02` and `androidx.compose.animation:animation-core:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/compose/animation)

**API Changes**

- Added `ManualFrameClock.hasAwaiters` to see if anything is
  awaiting a frame from that clock; `runWithManualClock` as a replacement
  for `runBlocking` when running tests that need a ManualFrameClock;
  `TestUiDispatcher.Main` that gives easy access to the main UI dispatcher
  in your tests.

  For example:

      @Test
      fun myTest() = runWithManualClock { clock ->
          // set some compose content
          withContext(TestUiDispatcher.Main) {
              clock.advanceClock(1000L)
          }
          if (clock.hasAwaiters) {
              println("The clock has awaiters")
          } else {
              println("The clock has no more awaiters")
          }
      }

  ([I0a85b](https://android-review.googlesource.com/#/q/I0a85b019ae5f40f52f2c6b78c08958eb7b8e7485), [b/161247083](https://issuetracker.google.com/issues/161247083))

**Bug Fixes**

- onPreCommit is deprecated; onCommit now has onPreCommit's
  behavior.

  onCommit and onActive now run in the same choreographer frame that
  the composition changes committed in rather than at the beginning
  of the next choreographer frame. ([I70403](https://android-review.googlesource.com/#/q/I70403eea442a7a003f08e7b1d19e44e0134ea077))

### Version 1.0.0-alpha01

August 26, 2020

`androidx.compose.animation:animation:1.0.0-alpha01` and `androidx.compose.animation:animation-core:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c93ac38a59f31e5db0eab67687532a4ba61913d5/ui)

## Version 0.1.0-dev

### Version 0.1.0-dev17

August 19, 2020

`androidx.compose.animation:animation:0.1.0-dev17` and `androidx.compose.animation:animation-core:0.1.0-dev17` are released. [Version 0.1.0-dev17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/ui)

**New Features**

**API Changes**

- Offset has become an inline class ([Iaec70](https://android-review.googlesource.com/#/q/Iaec70bb466cae8964f03e7484c1e86857c924f82))
- IntOffset is now an inline class ([Iac0bf](https://android-review.googlesource.com/#/q/Iac0bf89bb95642bf3a77073aead2cbce4c0e2e37))
- IntSize is now an inline class ([I2bf42](https://android-review.googlesource.com/#/q/I2bf426245b41f4189dead45114e3791bbceb9d13))
- AnimatedVisibilty composable animates the appearance
  and disappearance of the child content.

  EnterTransition and ExitTransition are introduced to work with
  AnimatedVisibilty composable to provide 3 different typs of
  appearance and disappearance animation: fade, slide, and
  expand/shrink the content. The different types of animations
  can be combined to achieve more bespoke look and feel. ([Idda11](https://android-review.googlesource.com/#/q/Idda1162e0d7f777f64dfd91b3192c2548d1c2c29))
- Deprecated PxBounds in
  favor of Rect. Updated all usages
  of PxBounds with rect and added
  proper deprecate/replace with
  annotations to assist with the
  migration. ([I37038](https://android-review.googlesource.com/#/q/I370384202fff3e5b147d42086f4350ab7fa830de), [b/162627058](https://issuetracker.google.com/issues/162627058))

**Bug Fixes**

- `PlacementScope.placeAbsolute()` was renamed to `PlacementScope.place()`, and the previous `PlacementScope.place()` was renamed to `PlacementScope.placeRelative()`. As a result, the `PlacementScope.place()` method will not automatically mirror the position in right-to-left contexts anymore. If this is desired, use `PlacementScope.placeRelative()` instead. ([I873ac](https://android-review.googlesource.com/#/q/I873ac827e6c4d4bf6c85a80b7128174c61602945), [b/162916675](https://issuetracker.google.com/issues/162916675))
- The `state { ... }` composable is now deprecated in favor of explicit calls to `remember { mutableStateOf(...) }` for clarity. This reduces the overall API surface and number of concepts for state management, and matches the `by mutableStateOf()` pattern for class property delegation. ([Ia5727](https://android-review.googlesource.com/#/q/Ia57278556d4f35ecf2cf5e6e30888b0d1f1f8012))

### Version 0.1.0-dev16

August 5, 2020

`androidx.compose.animation:animation:0.1.0-dev16` and `androidx.compose.animation:animation-core:0.1.0-dev16` are released. [Version 0.1.0-dev16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c74ed7b07d1c18da576f179d55e568ca12973df..316f882e649c600372170f013a18515f590f490d/ui)

**API Changes**

- Built-in vector converters to convert built-in units are now accessible via `Foo.VectorConverter`. e.g. `Dp.VectorConverter`, `Color.VectorConverter`, `Float.VectorConverter`, etc ([I3e273](https://android-review.googlesource.com/#/q/I3e2734f9712d94cc664184d35d495edab50bda53))
- Support end listener in `Modifier.animateContentSize()` such that when size change animation finishes, the listener will be notified, along with start/end size of the animation. ([I277b2](https://android-review.googlesource.com/#/q/I277b2b90f1ab5c6473cfb1e2de56e0ae7e67245d))
- New animateContentSize modifier that animates the layout size change of its child modifier ([Ieffdc](https://android-review.googlesource.com/#/q/Ieffdccd0fd0545ed139ecc20ef7baaebcda6d9d2))
- Added `MonotonicFrameAnimationClock` that enables you to use a
  MonotonicFrameClock as an `AnimationClockObservable` to bridge the gap
  between the new coroutines based clocks and APIs that still use the old
  callback based clocks.

  The `MonotonicFrameClock`equivalent of `ManualAnimationClock` is now
  `ManualFrameClock`. ([I111c7](https://android-review.googlesource.com/#/q/I111c7b7182a1495f95eab1bb808d3acd6af82447), [b/161247083](https://issuetracker.google.com/issues/161247083))

**Bug Fixes**

- The APIs for right-to-left support has been updated. LayoutDirectionAmbient has been added, which can be used to read and change the layout direction. Modifier.rtl and Modifier.ltr have been removed. ([I080b3](https://android-review.googlesource.com/#/q/I080b3cb674dc32af5fbe7e696228ac21f0720d72))
- Require type T to be explicitly specified for transitionDefinition. ([I1aded](https://android-review.googlesource.com/#/q/I1adedb34525ebb8c079a77a9af2636f1cb8339f7))
- foundation.shape.corner package were flatten to foundation.share ([I46491](https://android-review.googlesource.com/#/q/I464919cb74f8941c2a02f14dea0aa417febf3691), [b/161887429](https://issuetracker.google.com/issues/161887429))
- Modifier.plus has been deprecated, use Modifier.then instead. 'Then' has a stronger signal of ordering, while also prohibits to type `Modifier.padding().background() + anotherModifier`, which breaks the chain and harder to read ([Iedd58](https://android-review.googlesource.com/#/q/Iedd587edbed0ba964ef203a66b98be7297147bd7), [b/161529964](https://issuetracker.google.com/issues/161529964))
- Modifier.drawBackground has been renamed to Modifier.background ([I13677](https://android-review.googlesource.com/#/q/I1367723fce0e07418ed4ab391fe20c69aa092f53))

### Version 0.1.0-dev15

July 22, 2020

`androidx.compose.animation:animation:0.1.0-dev15` and `androidx.compose.animation:animation-core:0.1.0-dev15` are released. [Version 0.1.0-dev15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/ui)

#### Dependencies Update

- To use the `0.1.0-dev15` version of Compose, you will need to update your dependencies according to the new code snippets shown above in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose-animation#declaring_dependencies).

**API Changes**

- Transition API has been changed to return a TransitionState instead of passing the TransitionState to children. This makes the API more consistent with animate() APIs. ([I24e38](https://android-review.googlesource.com/#/q/I24e38fea3bf299e47d87dc5d2b42991e03d6786c))
- Modifier parameter added for Crossfade ([I87cfe](https://android-review.googlesource.com/#/q/I87cfe587dd58ee662d8e589274978aef44bbdf99), [b/159706180](https://issuetracker.google.com/issues/159706180))
- Use AnimationSpec instead of AnimationBuilder in the top level APIs to clarify the concept of static animation specification
  - Improve the transition DSL by removing the lambda requirement for creating AnimationSpecs such as tween, spring. They instead take constructor params directly.
  - Improve the overall ease of use of AnimationSpec opening up constructors instead of relying on builders
  - Change the duration and delay for KeyFrames and Tween to Int. This eliminates unnecessary type casts and method overloading (for supporting both Long and Int). ([Ica0b4](https://android-review.googlesource.com/#/q/Ica0b4cb42996d3d30f9b6dacdbe149c75af77341))
- Replaced usage of IntPx with Int. Replaced IntPxPosition with IntOffset. Replaced IntPxSize with IntSize. ([Ib7b44](https://android-review.googlesource.com/#/q/Ib7b44d92ce3aff86c606753f0ac5c3122b71041d))
- In order to consolidate the number of classes used to represent sizing information, standardize on usage of the Size class instead of PxSize. This provides the benefits of an inline class to leverage a long to pack 2 float values to represent width and height represented as floats. ([Ic0191](https://android-review.googlesource.com/#/q/Ic019171b52d2f24d262d9c47ac964728cdc1ee8b))
- In order to consolidate the number of classes used to represent positioning information, standardize on usage of the Offset class instead of PxPosition. This provides the benefits of an inline class to leverage a long to pack 2 float values to represent x and y offsets represented as floats. ([I3ad98](https://android-review.googlesource.com/#/q/I3ad983207bc37af20afac03e2cd09b4240777687))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters ([I086f4](https://android-review.googlesource.com/#/q/I086f4744d1eb51f0f31356e36991c2a8d4433059))
- Added animate() support for Dp, Px, Size, Position, Bounds, PxPosition, PxSize, PxBounds, IntPx, IntPxSize, IntPxPosition, IntPxBounds, and AnimationVector ([Ib7518](https://android-review.googlesource.com/#/q/Ib75184a2dc31986f8eb3698a428cbd8483104f61))
- Crossfade now accepts optional AnimationBuilder param to allow configuring the animation ([I6d6e0](https://android-review.googlesource.com/#/q/I6d6e03ec54221b740d7c88bdb8a8c93a662280a4))
- Replaced all nullable Color uses in API with non-nullable and use Color.Unset instead of null ([Iabaa7](https://android-review.googlesource.com/#/q/Iabaa7c6334857833cdb0d5958f062e2e576bd240))
- Removed ValueHolder class. Restructured AnimatedValue, AnimatedFloat classes to make the animation value field abstract so that subclasses can watch the value update.
  - Added model classes for AnimatedValue, AnimatedFloat, etc.
  - Added a new set of light-weight @Composable API for animating between values. ([I79530](https://android-review.googlesource.com/#/q/I79530e117cfa893a52542f85a55528eaa0f11b93))
- Breaking changes to the ambients API. See log and `Ambient<T>` documentation for details ([I4c7ee](https://android-review.googlesource.com/#/q/I4c7eea45f2b7bf41f8a8ba75fd667c06010469a9), [b/143769776](https://issuetracker.google.com/issues/143769776))
- New repeat mode: Reverse. This mode reverses the previous iteration as the animation repeats in RepeatableSpec or VectorizedRepeatableSpec. ([Ibe0f5](https://android-review.googlesource.com/#/q/Ibe0f50b12223911f87f4541c683f55bc25ad0a3f))
- API additions to ManualAnimationClock: `hasObservers: Boolean` and constructor parameter `dispatchOnSubscribe: Boolean` ([Iaa134](https://android-review.googlesource.com/#/q/Iaa1346a80d6c0ff3b3a4a1ff01cccadbca3407bc))
- Added APIs for getting min/max bounds in AnimatedFloat ([Icd9cc](https://android-review.googlesource.com/#/q/Icd9ccde2e7d163b28d3a7a7d9193bcb4a0c05f9e))

**Bug Fixes**

- `runOnIdleCompose` renamed to `runOnIdle` ([I83607](https://android-review.googlesource.com/#/q/I836071f1c3c63d21417a531f336f8a93ca13f9ed))
- Several testing APIs were renamed to be more intuitive. All findXYZ APIs were renamed to onNodeXYZ. All doXYZ APIs were renamed to performXYZ. ([I7f164](https://android-review.googlesource.com/#/q/I7f164b42b04196f023c4a2153d66825487998de4))
- Introduced low level stateless animation APIs. These APIs ([I63bf7](https://android-review.googlesource.com/#/q/I63bf7d28d5ac5e5ca2caaa427ee7643828c848a5))
- The Recompose composable is no longer a useful abstraction. Most recomposition should happen as a result of MutableState assignments. For anything beyond that, it is recommended that you use the `invalidate` function to trigger a recomposition of the current scope. ([Ifc992](https://android-review.googlesource.com/#/q/Ifc9926013c51c1db1e27e702a707bc1050f82fa6))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters. Deleted Px class in its entirety ([I3ff33](https://android-review.googlesource.com/#/q/I3ff339371abd6fb622172d060a70d12dda4822e0))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters ([Id3434](https://android-review.googlesource.com/#/q/Id343458210b56a9a4cdae4ef3d0f97ea79004942))
- Crossfade can now work with null as initial value ([Iad6a4](https://android-review.googlesource.com/#/q/Iad6a45933469434110ffdf5a55dd2e8eda37035a), [b/155947711](https://issuetracker.google.com/issues/155947711))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters ([I19d02](https://android-review.googlesource.com/#/q/I19d02beca10c30e9b6b444be0c2dd21227e30e9c))
- Consolidated CanvasScope implementations so there is now just DrawScope and ContentDrawScope Renamed CanvasScope to DrawScope. Updated DrawScope to implement Density interface and provide LayoutDirection Deleted DrawScope subclass in ContentDrawScope Painter and PainterModifier have been updated to no longer maintain an RTL property themselves as DrawScope provides this already without manually providing it ([I1798e](https://android-review.googlesource.com/#/q/I1798e4b2b325297c3b5394aa99be3db935e369b7))
- Updated higher level compose APIs that expose a Canvas to expose CanvasScope instead. This removes the need for consumers to maintain their own Paint objects. For consumers that still require access to a Canvas they can use the drawCanvas extension method which provides a callback to issue drawing commands with the underlying Canvas. ([I80afd](https://android-review.googlesource.com/#/q/I80afdf4c0a648962aa6ef1efc05b1d3b65757094))
- Added verticalGravity and horizontalGravity parameters to Row and Column, respectively. ([I7dc5a](https://android-review.googlesource.com/#/q/I7dc5a4e757370075657be68e6eda68e7498228fa))
- ui-text module is renamed as ui-text-core ([I57dec](https://android-review.googlesource.com/#/q/I57dec72ca50e7288e37c9272ef6ce8bcc485a83e))
- Improve DrawModifier API:
  - Made the receiver scope for draw() ContentDrawScope
  - Removed all parameters on draw()
  - DrawScope has same interface as former CanvasScope
  - ContentDrawScope has drawContent() method ([Ibaced](https://android-review.googlesource.com/#/q/Ibaced5feb8778510b8fe78e96f4fd3da1a6fda50), [b/152919067](https://issuetracker.google.com/issues/152919067))
- `runOnIdleCompose` and `runOnUiThread` are now global functions instead of methods on ComposeTestRule. ([Icbe8f](https://android-review.googlesource.com/#/q/Icbe8fd71d52144e855ccb4ce06a4677337be731a))
- \[Mutable\]State property delegate operators moved to extensions to support Kotlin 1.4 property delegate optimizations. Callers must add imports to continue using `by state { ... }` or `by mutableStateOf(...)`. ([I5312c](https://android-review.googlesource.com/#/q/I5312cf7bdfa072cadc1be2de5d5f45ec53200f41))
- ColoredRect has been deprecated. Use `Box(Modifier.preferredSize(width, height).drawBackground(color))` instead. ([I499fa](https://android-review.googlesource.com/#/q/I499fa26b66b128943500fbdf9ba490d754adf561), [b/152753731](https://issuetracker.google.com/issues/152753731))
- Replaced Modifier plus operator with factory extension functions ([I225e4](https://android-review.googlesource.com/#/q/I225e444f50956d84e15ca4f1378b7f805d54e0ca))
- Deprecated Center composable. It should be replaced either with the LayoutSize.Fill + LayoutAlign.Center modifier, or with one of the Box or Stack composables with suitable modifiers applied ([Idf5e0](https://android-review.googlesource.com/#/q/Idf5e0d25a2a8764489d738f6fcf242eeb667e124))
- Renamed LayoutFlexible to LayoutWeight. Renamed tight parameter to fill. ([If4738](https://android-review.googlesource.com/#/q/If4738c70c381e149ded400d657b5efd888ae5891))
- The Opacity composable function has been replaced with the drawOpacity modifier. ([I5fb62](https://android-review.googlesource.com/#/q/I5fb62404e20e3f2a0fa94ad0fb121f35d05bbb1c))
- Tests using AndroidComposeTestRule now provide an animation clock at the root of the composition that allows it to be paused, resumed and advanced manually. ([Id54c5](https://android-review.googlesource.com/#/q/Id54c51482f554cdb512e4eb53c78930408778f94))
- Support right-to-left direction in LayoutPadding modifier ([I9e8da](https://android-review.googlesource.com/#/q/I9e8da0bfbb135ff7f34b0dc49b905f634ad7d18c))
- Density and DensityScope were merged into one interface. Instead of ambientDensity() you can now use DensityAmbient.current. Instead of withDensity(density) just with(density) ([I11cb1](https://android-review.googlesource.com/#/q/I11cb1f069a95f32f4ecab631f49d38dc1c071a42))
- Added copy methods to various inline class types including:
  - Offset
  - Size
  - Radius
  - Motion
  - TransformOrigin
  - Deprecated Size.copy companion object method favor of instance copy method ([Ife290](https://android-review.googlesource.com/#/q/Ife2903a0277e051188884cb5d5feefcae8875dd1), [b/159905651](https://issuetracker.google.com/issues/159905651))
- androidx.compose.ViewComposer has been moved to androidx.ui.node.UiComposer androidx.compose.Emittable has been removed. It was redundant with ComponentNode. androidx.compose.ViewAdapters has been removed. They are no longer a supported use case. Compose.composeInto has been deprecated. Use `setContent` or `setViewContent` instead. Compose.disposeComposition has been deprecated. Use the `dispose` method on the `Composition` returned by `setContent` instead. androidx.compose.Compose.subcomposeInto has moved to androidx.ui.core.subcomposeInto ComponentNode#emitInsertAt has been renamed to ComponentNode#insertAt ComponentNode#emitRemoveAt has been renamed to ComponentNode#removeAt ComponentNode#emitMode has been renamed to ComponentNode#move ([Idef00](https://android-review.googlesource.com/#/q/Idef00fba3a2e67d7034e31d580d69192e9018b5f))