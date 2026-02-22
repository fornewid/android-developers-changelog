---
title: https://developer.android.com/jetpack/androidx/releases/compose-foundation
url: https://developer.android.com/jetpack/androidx/releases/compose-foundation
source: md.txt
---

# Compose Foundation

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.foundation](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary)  
[androidx.compose.foundation.layout](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary)  
[androidx.compose.foundation.gestures](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary)  
[androidx.compose.foundation.selection](https://developer.android.com/reference/kotlin/androidx/compose/foundation/selection/package-summary)  
[androidx.compose.foundation.lazy](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary)  
[androidx.compose.foundation.interaction](https://developer.android.com/reference/kotlin/androidx/compose/foundation/interaction/package-summary)  
[androidx.compose.foundation.text](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary)  
(*See the API reference docs for all compose packages*) Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.11.0-alpha05) |

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
    implementation "androidx.compose.foundation:foundation:1.10.3"
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
    implementation("androidx.compose.foundation:foundation:1.10.3")
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
[existing issues](https://issuetracker.google.com/issues?q=componentid:856989+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=856989&template=1425922)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.11

### Version 1.11.0-alpha05

February 11, 2026

`androidx.compose.foundation:foundation-*:1.11.0-alpha05` is released. Version 1.11.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/foundation).

**API Changes**

- Introduced `isNestedDraggablesTouchConflictFixEnabled` to resolve nested draggable conflicts. We will favor vertical drags over horizontal drags more because UX-wise there's more freedom and uncertainty when a user performs a vertical gesture vs. a horizontal gesture. ([I273c7](https://android-review.googlesource.com/#/q/I273c7a603dcbbd0fe302c7e4589343bbdae26bb9), [b/252334353](https://issuetracker.google.com/issues/252334353), [b/269627294](https://issuetracker.google.com/issues/269627294), [b/363198504](https://issuetracker.google.com/issues/363198504), [b/442390269](https://issuetracker.google.com/issues/442390269), [b/419580124](https://issuetracker.google.com/issues/419580124))
- Adds support for trackpad gestures and conversion from trackpad input events to mouse. With this change, trackpad pointer events that control a cursor like on tablets or laptops will generally be reported as mouse pointers. Pan and scale gestures will also be reported with additional information available in the pointer event changes, with a new `PointerEventType.Pan` and `PointerEventType.Scale` indicating that these values will be set ([Id071a](https://android-review.googlesource.com/#/q/Id071af573d5710d7d3aca73bd1c8037bdb0ea701), [b/315527861](https://issuetracker.google.com/issues/315527861), [b/459831570](https://issuetracker.google.com/issues/459831570))
- Introduce `isDelayPressesUsingGestureConsumptionEnabled`. When this flag is enabled, containers with drag gesture will delay press. This includes a behavior change for containers based off `Modifier.draggable` which didn't delay press previously. ([I53f24](https://android-review.googlesource.com/#/q/I53f242a2161ea4c540e44c615a20581075ac61a6), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Removed the flag `isDetectTapGesturesImmediateCoroutineDispatchEnabled` and deprecated flag `DetectTapGesturesEnableNewDispatchingBehavior` ([I9bba3](https://android-review.googlesource.com/#/q/I9bba3ed7a354147cb6f1cad4f1275a5ec6c1157d))

**Bug Fixes**

- Fixed an `IndexOutOfBoundsException` in `BasicTextField` when using \`\`OutputTransformation and deleting text. ([I20ee1](https://android-review.googlesource.com/#/q/I20ee17de095ffb2c598267bd7b1450651d2ce1f1))
- Changed `GridTrackSize.Auto` behavior. It now sizes tracks from `min-content` up to `max-content`. ([Ifa22e](https://android-review.googlesource.com/#/q/Ifa22e11e512ad779f99228b1ba9d0749369e34ac), [b/477748472](https://issuetracker.google.com/issues/477748472))

**External Contribution**

- Add support for `NumPad` movement keys ([I1ff12](https://android-review.googlesource.com/#/q/I1ff128370417cc7b837ae09a4f47521473cca698))

### Version 1.11.0-alpha04

January 28, 2026

`androidx.compose.foundation:foundation-*:1.11.0-alpha04` is released. Version 1.11.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/foundation).

**API Changes**

- Fixed a bug where `AnchoredDraggableState`'s `targetValue` was incorrect in some scenarios with multiple anchors at the same offset. When settled at an anchor that had the same offset as another anchor, `targetValue` incorrectly returned the last of the anchors at this offset. It now returns the `currentValue` when settled at the `currentValue`'s offset. ([I66a7a](https://android-review.googlesource.com/#/q/I66a7a227dbb1df035eb81d30f9e7b54d502e2d90), [b/476365336](https://issuetracker.google.com/issues/476365336))
- Introduced `FlexBox`, a configurable layout system that is a superset of `Row`, `Column`, `FlowRow`, and `FlowColumn`. It supports features like flex-grow, flex-shrink, custom wrapping, direction change and detailed alignment control via `FlexBoxConfig` and `Modifier.flex`. ([I44780](https://android-review.googlesource.com/#/q/I44780b3c90e0a36f4095ed83e73c9b0984ecd6f6))
- Introduced `Grid`, a new non-lazy 2D layout composable inspired by CSS Grid. This initial version allows defining explicit grid structures with various track sizes including `Fixed`, `Percentage`, `Flex`, and content-based options via the `config` block. The core layout logic supports explicit item placement within the grid using `Modifier.gridItem()`. All Grid related APIs are currently experimental and require opt-in with `@OptIn(ExperimentalGridApi::class)`. We are actively seeking feedback on this new layout! ([I04907](https://android-review.googlesource.com/#/q/I04907884457dbffb9653b09807c03b96506517c0), [b/462550392](https://issuetracker.google.com/issues/462550392))

### Version 1.11.0-alpha03

January 14, 2026

`androidx.compose.foundation:foundation-*:1.11.0-alpha03` is released. Version 1.11.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/foundation).

**Bug Fixes**

- Fix a memory leak in `LazyStaggeredGrid` when used inside `LookaheadScope` [I286ad](https://android-review.googlesource.com/#/q/I286ad4ef513caa2303e06ae5f47c18ab77dc72e9)

### Version 1.11.0-alpha02

December 17, 2025

`androidx.compose.foundation:foundation-*:1.11.0-alpha02` is released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/foundation).

**API Changes**

- The `MultiModalInjectionScope` APIs are now stable. This includes `performKeyInput` and `performRotaryScrollInput`, and their underlying key and rotary APIs. The experimental annotation has been removed. ([Ie8bbc](https://android-review.googlesource.com/#/q/Ie8bbc60afddb304113b0e9c35d1a39f010c242df), [b/261561237](https://issuetracker.google.com/issues/261561237))
- Removed the `isNonSuspendingPointerInputInClickableEnabled` flag. ([I6a168](https://android-review.googlesource.com/#/q/I6a1681823e831b71d61543e2a8790f67bf04c578), [b/455591971](https://issuetracker.google.com/issues/455591971))

### Version 1.11.0-alpha01

December 03, 2025

`androidx.compose.foundation:foundation-*:1.11.0-alpha01` is released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b48588febd37d5947dfa0f2827d2b5ca6af2ed90..deb96499dfe95073f5c1215c1287787683cb1e92/compose/foundation).

**API Changes**

- Introduced `Modifier.scrollIndicator` to allow adding custom scroll indicators to scrollable containers. The `ScrollIndicatorFactory` interface enables creating scroll indicators by defining their appearance and behavior. ([I89322](https://android-review.googlesource.com/#/q/I893224c108519428fe4579fa8d20133462b95d58))
- Removed `ComposeFoundationFlags.isTextFieldDpadNavigationEnabled`. The new behavior is now enabled at all times. ([I3f034](https://android-review.googlesource.com/#/q/I3f0347185d3590f9b7442a5fd44b06016f4c381e))
- Introduce `isCacheWindowRefillFixEnabled` to control the roll out of the cache window refill fix. ([I4e52b](https://android-review.googlesource.com/#/q/I4e52baefd57b178834444a60cf43a016ec193e52), [b/454439658](https://issuetracker.google.com/issues/454439658))
- Removed `ComposeFoundationFlags.isKeepInViewFocusObservationChangeEnabled`. The new behavior is now enabled at all times. ([I7cbd4](https://android-review.googlesource.com/#/q/I7cbd45779b72807426875ab6efd05e391ed1f111))
- `Modifier.onFirstVisible()` is deprecated as its behavior is misleading and doesn't always follow the contract claimed by the name. For example, when it is added on an item of `LazyColumn`, this callback will be called everytime this item became visible after scrolling. It is not what the users of the modifier with this name might have expected. It is recommended to use `Modifier.onVisibilityChanged()` instead and manually track if the layout was visible already previously based on the requirement of the specific use case. ([Ia7095](https://android-review.googlesource.com/#/q/Ia709566717edbdfe5717bedfa74d1334a78f8964), [b/447601783](https://issuetracker.google.com/issues/447601783))
- Introduced `MeasuredSizeAwareModifierNode`, which is needed when you need `onRemeasured()` callback. Please use this interface directly instead of using more generic `LayoutAwareModifierNode` when you don't need other callbacks. ([If6fb0](https://android-review.googlesource.com/#/q/If6fb04b74840d08274d01a41d84bd14507d190b8))
- Introduces a `visible` Modifier which can be used to skip drawing the content of a Composable without affecting the space it occupies. ([Ia6871](https://android-review.googlesource.com/#/q/Ia687178fc4299c10a19bd5fad63394c45f81b170), [b/158837937](https://issuetracker.google.com/issues/158837937))

## Version 1.10

### Version 1.10.3

February 11, 2026

`androidx.compose.foundation:foundation-*:1.10.3` is released. Version 1.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b..0d23f956849b578e041ea4245127d4007eae43be/compose/foundation).

### Version 1.10.2

January 28, 2026

`androidx.compose.foundation:foundation-*:1.10.2` is released. Version 1.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c09ac6669b664a348ecf964a97968cd81479dcd4..fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b/compose/foundation).

**Bug Fixes**

- Fixed a crash when navigating back from a screen with an active text selection. ([I9f540](https://android-review.googlesource.com/#/q/I9f5408fbfc56be0de9632d979b4c3e89a9c59139), [b/444482508](https://issuetracker.google.com/issues/444482508))

### Version 1.10.1

January 14, 2026

`androidx.compose.foundation:foundation-*:1.10.1` is released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2120e7975523001d1eac390a5d9c5e2e9597267f..c09ac6669b664a348ecf964a97968cd81479dcd4/compose/foundation).

**Bug Fixes**

- Fix a crash when text selection extends from one Text instance to another that are aligned horizontally. [I351311](https://android-review.googlesource.com/#/q/I351311a9ac698d410cc849762e28e1e3f977b1da), [b/439758956](https://issuetracker.google.com/439758956)

### Version 1.10.0

December 03, 2025

`androidx.compose.foundation:foundation-*:1.10.0` is released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26..a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9/compose/foundation).

### Version 1.10.0-rc01

November 19, 2025

`androidx.compose.foundation:foundation-*:1.10.0-rc01` is released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1c84233fc2372352b838d165d256581ff37ada9..b48588febd37d5947dfa0f2827d2b5ca6af2ed90/compose/foundation).

**Bug Fixes**

- Disabled `isCacheWindowForPagerEnabled` flag. ([Iffdec](https://android-review.googlesource.com/#/q/Iffdec7dd9d2c7f8f967f0e8d415a1dd9bade7341), [b/458193632](https://issuetracker.google.com/issues/458193632))

### Version 1.10.0-beta02

November 05, 2025

`androidx.compose.foundation:foundation-*:1.10.0-beta02` is released. Version 1.10.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/784e4a2de372f09d49c65fbc1ca64681a25a5f06..d1c84233fc2372352b838d165d256581ff37ada9/compose/foundation).

### Version 1.10.0-beta01

October 22, 2025

`androidx.compose.foundation:foundation-*:1.10.0-beta01` is released. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..784e4a2de372f09d49c65fbc1ca64681a25a5f06/compose/foundation).

**API Changes**

- Updates all indirect touch APIs to use the name indirect pointer APIs to match pointer input APIs. ([I238ce](https://android-review.googlesource.com/#/q/I238ced063c4f54959abf1c07a1b93bbf1c6efa78), [b/451607214](https://issuetracker.google.com/issues/451607214))
- Annotated `PagerState.currentPageOffsetFraction` with `@FrequentlyChangingValue`. ([Idfaab](https://android-review.googlesource.com/#/q/Idfaab09686eb5a65093de8375363912e93115515))

**Bug Fixes**

- Fixes marquee behavior for RTL layout directions. ([Ib8be3](https://android-review.googlesource.com/#/q/Ib8be3ad95cba2d7b0199e0c21c371ef0e14f4f46))

### Version 1.10.0-alpha05

October 08, 2025

`androidx.compose.foundation:foundation-*:1.10.0-alpha05` is released. Version 1.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef9c81cf7222a390e0a467d8c8b48d04362fd3d..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/foundation).

**API Changes**

- `PaddingValues` now support addition and subtraction to simplify common padding calculations. ([I327e1](https://android-review.googlesource.com/#/q/I327e1036702074612ff4614490ea7c095a30708c), [b/244468479](https://issuetracker.google.com/issues/244468479))

**Bug Fixes**

- `ComposeFoundationFlags.isPausableCompositionInPrefetchEnabled` is enabled by default. It is a performance optimization, which allows us to distribute work we need to do during the prefetch better, for example we can only perform the composition for parts of the `LazyColumn`'s next item during one ui frame, and then continue composing the rest of it in the next frames. ([I4c7fe](https://android-review.googlesource.com/#/q/I4c7feb6cff8b812e75cbf0a1d4e512b3c42ee412))

### Version 1.10.0-alpha04

September 24, 2025

`androidx.compose.foundation:foundation-*:1.10.0-alpha04` is released. Version 1.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..6ef9c81cf7222a390e0a467d8c8b48d04362fd3d/compose/foundation).

**API Changes**

- `ScrollIndicatorState` implementation added for `PagerState`. ([I113b7](https://android-review.googlesource.com/#/q/I113b7797decc869e5c0e02e8d58ae384bf79c128))
- `ScrollIndicatorState` implementation added for `LazyStaggeredGridState`. ([I1028e](https://android-review.googlesource.com/#/q/I1028e40848a2e95c11b9f43bd3b8177bda726221))
- `ScrollIndicatorState` implementation added for `LazyGridState`. ([I9e50c](https://android-review.googlesource.com/#/q/I9e50c4ba28b3e8d32e528eee9b40dbf30bc48623))
- `ScrollIndicatorState` implementation added for `LazyListState`. ([I5ee29](https://android-review.googlesource.com/#/q/I5ee290fd937bdcd4f8916263f1c848abd9d0313e))
- `ScrollIndicatorState` implementation added for `ScrollState`. ([I27f66](https://android-review.googlesource.com/#/q/I27f667c1749bf373425873806d9d127b19ff0243))
- Introduce `scrollIndicatorState` property in `ScrollableState` interface ([Idca93](https://android-review.googlesource.com/#/q/Idca9393841cf71bde346d7dcc0488c42253be643))
- Flag `isWindowInsetsModifierLocalNodeImplementationEnabled` was removed ([I15e8f](https://android-review.googlesource.com/#/q/I15e8fe65062ce9f03947acb8a131856f922d3cde), [b/440964232](https://issuetracker.google.com/issues/440964232))
- Expose `scrollableArea()` modifier that can be used to make the component scrollable with the behaviors of clipping content to its bounds and automatically handling content scroll direction based on Orientation, RTL and the `reverseScrolling` flag. ([I9471b](https://android-review.googlesource.com/#/q/I9471b1bcf0d738626e8f9a9e2d60ef5d2c9c395a), [b/316559454](https://issuetracker.google.com/issues/316559454))

### Version 1.10.0-alpha03

September 10, 2025

`androidx.compose.foundation:foundation-*:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/compose/foundation).

**API Changes**

- Removes `ComposeFoundationFlags.isNonComposedClickableEnabled` ([I0dfc0](https://android-review.googlesource.com/#/q/I0dfc069e0c53be41a043df36c111bacdd09fbcd8), [b/406228525](https://issuetracker.google.com/issues/406228525))
- Move factory functions for creating `FillableData` instances to companion object. Instead of calling `FillableData(value)`, use the new factory methods: `FillableData.createFrom(value)`. ([I2e200](https://android-review.googlesource.com/#/q/I2e2000938dacc674805868e2030813575892b26d), [b/441719650](https://issuetracker.google.com/issues/441719650))
- Introduce `BeyondBoundsLayoutModifierNode` a new Modifier node to perform beyond bound layout for focus search. ([I39be1](https://android-review.googlesource.com/#/q/I39be1741cebd0b7df56c8e034cc3189b2135e664), [b/416133658](https://issuetracker.google.com/issues/416133658))
- Marked `ScrollState.value` as `@FrequentlyChangingValue` property. ([I4723d](https://android-review.googlesource.com/#/q/I4723d9d1e5c39731f5a3110e1d76948e8f606e7a))
- Introduced `LazyLayoutKeyIndexMap` and a factory for a default implementation. ([I4fd0c](https://android-review.googlesource.com/#/q/I4fd0c2861acc2d0eb69d3be619a5fa9c3464d539), [b/415038029](https://issuetracker.google.com/issues/415038029))

**Bug Fixes**

- Column and Row now correctly pass the item's actual size to `Modifier.align`, resolving an issue where custom `Modifier.align` implementation received an incorrect 0 value. ([I8194f](https://android-review.googlesource.com/#/q/I8194f5e3538ec16cf750d4f109f4d9a071ba2a33), [b/439716351](https://issuetracker.google.com/issues/439716351))

### Version 1.10.0-alpha02

August 27, 2025

`androidx.compose.foundation:foundation-*:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/foundation).

**API Changes**

- Removed flag `isFlingContinuationAtBoundsEnabled`. ([I6b84f](https://android-review.googlesource.com/#/q/I6b84f1c0fe0cba45c52545ee52e1b7a3a2a01891))
- Removed flag `isAdjustPointerInputChangeOffsetForVelocityTrackerEnabled`. ([I62380](https://android-review.googlesource.com/#/q/I62380042ed112396d975d298dad3a8667a5e4950))
- Removed flag `isOnScrollChangedCallbackEnabled`. ([I667dc](https://android-review.googlesource.com/#/q/I667dcf93b25605666a106ed840e8f3f8c296f8e6))
- Removed flag `isAutomaticNestedPrefetchEnabled`. ([I4f416](https://android-review.googlesource.com/#/q/I4f416c30fd4321f4b9ce8c70029a326c3a73757d))
- Removed flag `DragGesturePickUpEnabled`. ([Ib8500](https://android-review.googlesource.com/#/q/Ib8500127bd7a17d5b9741d5efcc99f8c8b4831d8))
- Introduce `ScrollIndicatorState` API for representing scrollbar state ([I5e229](https://android-review.googlesource.com/#/q/I5e22972f8fec5f563bfb6fbd71c9a82b4f607023))

**Bug Fixes**

- Fixed a bug where using `Modifier.anchoredDraggable` was not invoking `confirmValueChange`. ([Iff7cc](https://android-review.googlesource.com/#/q/Iff7cc0e6a7da0b37b69e59d3578928f9c2c654ab))

### Version 1.10.0-alpha01

August 13, 2025

`androidx.compose.foundation:foundation-*:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c30d03ab9e19dcf35e8b79438f0d91ee74cae557..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/foundation).

**API Changes**

- Update Pager's prefetch strategy to use Cache Window instead of the default 1 item in the direction of the scroll. Now initial prefetching is enabled by default in Pager and prefetching will be based on the size of the window worth 1 viewport, that is, we will try to fill 1 whole view port with prefetched items. Items will be kept around longer as well. ([I4d45e](https://android-review.googlesource.com/#/q/I4d45ece5bab78dc241618d29d3701e5463789aa6), [b/292136289](https://issuetracker.google.com/issues/292136289))
- `ComposeFoundationLayoutFlags.isWindowInsetsOptimizationEnabled` flag has been added to allow disabling a `WindowInsets` performance optimization should the new implementation cause a behavioral change. ([I8e912](https://android-review.googlesource.com/#/q/I8e9129e7cdafc6bc4da61c0b3c0883dbf5376ef5))
- `SnapFlingBehavior` now allows snap animation specs to overshoot during snapping. This allows enables e.g. a bouncy spring spec as the `snapAnimationSpec` to produce a bouncy snap animation. Overshooting values continue to be ignored when performing an approach with the snap spec. ([I373c2](https://android-review.googlesource.com/#/q/I373c2f58fe859a25014c707913041eeb5975f63d))
- Pointer downs with a mouse or touchpad in a `ComposeView` will now clear focus automatically if the pointer down doesn't occur in the bounds of the focused node. This results in a "tap-to-clear focus" UX that is more expected than current behavior when using pointer input devices. This behavior can be opt-ed out of with a new `AbstractComposeView.isClearFocusOnPointerDownEnabled` API. ([I6322b](https://android-review.googlesource.com/#/q/I6322b0a63e80042f6a558104d0684443e5dc161f), [b/282963174](https://issuetracker.google.com/issues/282963174))
- Now Scrollable supports 2 dimensional mouse wheel scroll events better. A new test API landed to help test use cases in `MouseInjectionScope`. We also introduced a new overload for scroll methods in `MouseInjectionScope` and a flag to control the new behavior called `isMouseWheel1DAxisLockingEnabled` ([I136df](https://android-review.googlesource.com/#/q/I136dfe2d0887c1900fb1896599ec4b4aa1b31ac7))
- Updated `DragGestureNode` to use raw pointer input instead of suspending pointer input for optimization. The changes are added behind the flag `isNonSuspendingPointerInputInDraggableEnabled` ([I0fa4b](https://android-review.googlesource.com/#/q/I0fa4b8cedc216b227542f67984796cd02ffc008f))
- Annotated some `AnchoredDraggable` APIs with `@FrequentlyChangingValue`. `offset`, `requireOffset` and `progress` change often and should not be read in composition. Please access these values from the layout and draw phases, effects or otherwise outside of composition instead. ([I05539](https://android-review.googlesource.com/#/q/I0553910e71876e3354ee4f94080d5fecfd8cb032))
- Removed flags `isOnScrollChangedCallbackEnabled`, `isAdjustPointerInputChangeOffsetForVelocityTrackerEnabled`, `isFlingContinuationAtBoundsEnabled`, `isAutomaticNestedPrefetchEnabled`, `DragGesturePickUpEnabled`, `isPointerInteropFilterDispatchingFixEnabled`, `isNestedScrollInteropPostFlingFixEnabled`, `isNestedScrollDispatcherNodeFixEnabled` ([I36c18](https://android-review.googlesource.com/#/q/I36c18840c708660e9cbad345024299bfd80cde3c))
- Introduce `CompositionLocal` that can be used to modify the brush of Autofill's successful filling highlight. ([I52329](https://android-review.googlesource.com/#/q/I52329ea7905c1a0a2db56caa36f4b9d53f3dd0d9))
- Added customizable focus rect to `FocusProperties`. You can now define a custom focus area instead of defaulting the bounding box of the focusable. This information is used by the focus traversal system and the keep in view logic of scrollable containers. ([Id6555](https://android-review.googlesource.com/#/q/Id6555453fe54b4a11db6a6ff90ebaa486b02f395), [b/368378073](https://issuetracker.google.com/issues/368378073))
- Added a new `LineHeightStyle.Mode` called `Tight`. This mode helps enforce smaller line heights even when they may possibly cut taller glyphs. ([Id3849](https://android-review.googlesource.com/#/q/Id38495accc4fe059f6e2318eaafb648f36fe0f99))
- Introduced new Interpolatable interface which allows for automatic interpolation between different types, assuming one type knows how to convert from the other. This interface is leveraged in several compose types like Brush and Shape, but can be utilized externally as well. ([I58eab](https://android-review.googlesource.com/#/q/I58eab524eadd08c41f1809a2815a6311ad179aee))
- Adds indirect input events and a way to specify coordinate axis to use for scrolling. ([I58e7c](https://android-review.googlesource.com/#/q/I58e7c4acc58c38d1690d5267f7f26b7d5cb83d13))
- Adds new `WindowInsets.cutoutPath` API to get the path for the display cutout ([Ib90b1](https://android-review.googlesource.com/#/q/Ib90b14ad65463a23805a44c7531ae2bdbb49f8df), [b/279636456](https://issuetracker.google.com/issues/279636456))
- The `isWindowInsetsDefaultPassThroughEnabled` flag has been removed, defaulting WindowInsets to not consuming so that child Views can receive `WindowInsets` by default. ([I888e0](https://android-review.googlesource.com/#/q/I888e0e284b5f089d19b340258fbe6f2d1f34c7c5), [b/412469666](https://issuetracker.google.com/issues/412469666))

**Bug Fixes**

- `isNonSuspendingPointerInputInDraggableEnabled` should be disabled for now. ([Ia41c4](https://android-review.googlesource.com/#/q/Ia41c43344d70a63105a5a10e1d83d86551194e97))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Updated `DraggableAnchors`' `minPosition/maxPosition` documentation to indicate these APIs should return Float.NaN in line with other `DraggableAnchors` APIs. ([I0460a](https://android-review.googlesource.com/#/q/I0460ae646ea59d3fae68fd2f8c27266b1ed7f779))
- Fixed a bug where `DraggableAnchors#closestAnchor` would crash if the anchors were empty ([I4e646](https://android-review.googlesource.com/#/q/I4e646c562b0d2b3538230ec0474c02f296763a72))
- Performance improvements for `DraggableAnchors` ([If4065](https://android-review.googlesource.com/#/q/If40650e0a3b70b8402eaf606f159342c5232c68f), [I0460a](https://android-review.googlesource.com/#/q/I0460ae646ea59d3fae68fd2f8c27266b1ed7f779))
- `TextFieldState.edit { }` no longer clears the undo history. Instead it creates a standalone undo entry. If the desired behavior is to clear the undo stack after an `edit` call, please use `TextFieldState.undoState.clearHistory()`. ([I12c14](https://android-review.googlesource.com/#/q/I12c14696947b577ffb42d33094b89dedb76dc34b))
- Added support for double-tap to select word in `SelectionContainer` and `BasicTextField(value, onValueChange)` overload. ([Ibb06a](https://android-review.googlesource.com/#/q/Ibb06abaa0342a3ccd7483b831f35a2db1b7c27a2))
- Minor bug fix to make `AutoboxingStateValuePropertyDetector` compatible for both K1 and K2 ([Ie81c1](https://android-review.googlesource.com/#/q/Ie81c19fdfb3d88da4b56ae251a3a462dbe927923))
- `requestRectangleOnScreen` requests made by AndroidViews now properly propagates to Compose. This helps views like `EditText` to stay on screen when interacted with. ([Ibbf4c](https://android-review.googlesource.com/#/q/Ibbf4c7255eff71357780058986ded41dbff03c48))
- Column and Row now correctly pass the item's actual size to `Alignment.Vertical.align` and `Alignment.Horizontal.align`, resolving an issue where custom alignment implementations received an incorrect 0 value. ([I3e460](https://android-review.googlesource.com/#/q/I3e460b688b02cce7b1d90ac0949aa185a96a88a3), [b/349722072](https://issuetracker.google.com/issues/349722072))

## Version 1.9

### Version 1.9.5

November 19, 2025

`androidx.compose.foundation:foundation-*:1.9.5` is released. Version 1.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41..1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26/compose/foundation).

### Version 1.9.4

October 22, 2025

`androidx.compose.foundation:foundation-*:1.9.4` is released. Version 1.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea7909f13c54ea29d87d55d27ecf449000f82a8a..b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41/compose/foundation).

### Version 1.9.3

October 08, 2025

`androidx.compose.foundation:foundation-*:1.9.3` is released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6177e34a7667c42030e47ee8ecba82f09e2a5de..ea7909f13c54ea29d87d55d27ecf449000f82a8a/compose/foundation).

### Version 1.9.2

September 24, 2025

`androidx.compose.foundation:foundation-*:1.9.2` is released. Version 1.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/93a1ed2aac05dbfa192392b9d4ab27c40da53d69..b6177e34a7667c42030e47ee8ecba82f09e2a5de/compose/foundation).

### Version 1.9.1

September 10, 2025

`androidx.compose.foundation:foundation-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44da9aeaf3fa617c6f81f887691b37fe901109aa..93a1ed2aac05dbfa192392b9d4ab27c40da53d69/compose/foundation).

**Bug Fixes**

- Fixes crash happening when using `LazyLayoutCacheWindow` in `LazyLists` ([c39f5f3](https://android-review.googlesource.com/#/q/c39f5f3af766384c4517d9e4f684840239b1d5ab))

### Version 1.9.0

August 13, 2025

`androidx.compose.foundation:foundation-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..44da9aeaf3fa617c6f81f887691b37fe901109aa/compose/foundation)

**Important changes since 1.8.0**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.
- Breaking change: `clickable`, `combinedClickable`,`selectable`, `toggleable`, and `triStateToggleable` overloads without an Indication parameter now only support `IndicationNodeFactory` instances provided using `LocalIndication`. This change will apply when you recompile your usages of these modifiers using this version of Compose. Binary / transitive dependencies are not affected. If you are providing a deprecated Indication implementation to `LocalIndication`, and using these APIs, this will introduce a crash at runtime. This behavior change is needed to enable improved performance, and allow Composable functions using these modifiers to skip during recomposition. You can use `ComposeFoundationFlags.isNonComposedClickableEnabled=false` to temporarily opt-out of this behavior change, to enable upgrading Compose without being blocked on this migration. This flag will be removed after one stable release. To resolve, migrate any deprecated Indication implementations to use `IndicationNodeFactory` instead. You can also use the overloads with an explicit Indication parameter - these overloads will continue to support non-`IndicationNodeFactory` instances of Indication, although this is not recommended for performance reasons. ([I6bcdc](https://android-review.googlesource.com/#/q/I6bcdc6ff82dd6ff5ea1a97688d5a1426b719df20), [b/316914333](https://issuetracker.google.com/issues/316914333))
- Introduced `isFlingCancellationWithNestedScrollFixEnabled` to fix an issue with fling propagation in nested scrolling. In this CL we are restoring the fling continuation behavior removed in [I9326a](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3260391). We will still cancel the fling animation in case the child is removed from composition. ([I467f4](https://android-review.googlesource.com/#/q/I467f4a8974a752d63bd3d6ab62e6eb751f5e2ccc), [b/405910180](https://issuetracker.google.com/issues/405910180), [b/419049142](https://issuetracker.google.com/issues/419049142), [b/416784125](https://issuetracker.google.com/issues/416784125))
- Re-add usage of `scrollAnimationSpec` in `ContentInViewNode`. The behavior was removed during the `scrollAnimationSpec` deprecation which caused use cases to be broken. ([I1436a](https://android-review.googlesource.com/#/q/I1436a3212c8f637935259243253f70db1163e584), [b/403301605](https://issuetracker.google.com/issues/403301605))
- Stabilized `LazyLayout`. ([If5db4](https://android-review.googlesource.com/#/q/If5db4170daec197e39612bcfb5f8b5d4cdd8db52)), `LazyLayoutPrefetchState` and it's scheduling method `schedulePrecomposition` and `schedulePrecompositionAndPremeasure`. ([I4362f](https://android-review.googlesource.com/#/q/I4362f3417ebe652d967463a474e4ba799967930d), [b/252853717](https://issuetracker.google.com/issues/252853717)) and `LazyLayoutItemProvider` ([Icce09](https://android-review.googlesource.com/#/q/Icce09a01e2668ea0a93678ec84d189aa4769e26c),[b/261565751](https://issuetracker.google.com/issues/261565751))
- Allow Compose to trigger `ViewTreeObserver.OnScrollChanged`. This behavior is introduced under the flag `isOnScrollChangedCallbackEnabled`. We also introduced an extension function of `DelegatableNode dispatchOnScrollChanged`. ([I34b9d](https://android-review.googlesource.com/#/q/I34b9d923ff1fb4a4e27a53e583a7b082bc99b158), [b/238109286](https://issuetracker.google.com/issues/238109286))
- Introduce `Modifier.scrollable2D`, `Scrollable2DState` and companion APIs for state creation. Also introduced common scroll extension functions. ([Ic61c8](https://android-review.googlesource.com/#/q/Ic61c8f14451090f441b009bf8f86e7566c27c782), [b/214410040](https://issuetracker.google.com/issues/214410040))
- `PrefetchScheduler` and customisation have been deprecated in favor of the internal implementation that does all the work automatically. ([I3a9a6](https://android-review.googlesource.com/#/q/I3a9a678918c7ce33174b9c330142a650cc9e3b2a), [b/420551535](https://issuetracker.google.com/issues/420551535))
- `TextFieldState.edit { }` no longer clears the undo history. Instead it creates a standalone undo entry. If the desired behavior is to clear the undo stack after an edit call, please use `TextFieldState.undoState.clearHistory()`. ([I12c14](https://android-review.googlesource.com/#/q/I12c14696947b577ffb42d33094b89dedb76dc34b))
- Context Menu and Selection toolbar now both support Smart Items (Smart Selection)
- Added styled text `OutputTransformation` to allow styling the output of `TextField` using the `state` overload.
- `TextField`: Support context menu (right click menu).
- Text copied from multiple Text composables in a `SelectionContainer` now will have a line separator \\n added between text coming from the separate Text composables. ([I25332](https://android-review.googlesource.com/#/q/I25332168924ca35574bb8c5e7094ad8010ab5927), [b/285036739](https://issuetracker.google.com/issues/285036739))
- Introduce API for creating custom bullet lists through `AnnotatedString` ([I1d066](https://android-review.googlesource.com/#/q/I1d066d3df73999bd3c771b72982fe8bbccc822ae), [b/383269496](https://issuetracker.google.com/issues/383269496), [b/139326648](https://issuetracker.google.com/issues/139326648))
- The `state` overload of `BasicTextField` will keep the cursor scrolled into view when its size changes. ([I0eb41](https://android-review.googlesource.com/#/q/I0eb41276b627d49889d3aedb11b58ba4d2ec0b74), [b/406187741](https://issuetracker.google.com/issues/406187741))
- Breaking change: the `background` and `border` modifier nodes now implement `SemanticsModifierNode`. This can result in new `SemanticsNodes` added to the semantics tree and, therefore, lead to test failures in tests that make assumptions about the semantics tree structure. For example, tests that use `onChild`, `onParent`, `onSibling`, and other similar methods to make assertions can fail if a new node is added between the current and target nodes. The preferred way to fix these failures is to add a `testTag` to the target node directly. Another approach is to use a looser matcher, such as `onNode(hasAnyAncestor(hasText("ancestor")) and hasText("target"))`. ([I638b5](https://android-review.googlesource.com/#/q/I638b56cb3aa3f4f68a354dfa5a42201febee61bc))

### Version 1.9.0-rc01

July 30, 2025

`androidx.compose.foundation:foundation-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..c30d03ab9e19dcf35e8b79438f0d91ee74cae557/compose/foundation).

**Bug Fixes**

- `TextFieldState.edit { }` no longer clears the undo history. Instead it creates a standalone undo entry. If the desired behavior is to clear the undo stack after an `edit` call, please use `TextFieldState.undoState.clearHistory()`. ([I12c14](https://android-review.googlesource.com/#/q/I12c14696947b577ffb42d33094b89dedb76dc34b))

### Version 1.9.0-beta03

July 16, 2025

`androidx.compose.foundation:foundation-*:1.9.0-beta03` is released. Version 1.9.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d578548e34459870db64b61d8788d83f2cf49f54..5735a11c1798c2f8b419dfdc02347578a6ebf870/compose/foundation).

**Bug Fixes**

- Fixed a regression bug breaking sticky headers behavior in lazy grids when empty header content is provided. ([e3e3400](https://android-review.googlesource.com/#/q/e3e3400084c77a22c8adc0ba313610f97b6763e8))

### Version 1.9.0-beta02

July 2, 2025

`androidx.compose.foundation:foundation-*:1.9.0-beta02` is released. Version 1.9.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..d578548e34459870db64b61d8788d83f2cf49f54/compose/foundation).

**New Features**

- Support smart items in context menu and selection toolbar.

**API Changes**

- Fixed a bug where certain hardware keyboards or TV remotes fail to move cursor in new `TextFields` using the directional keys, and instead switch focus to another composable. Added `ComposeFoundationFlag.isTextFieldDpadNavigationFixEnabled` to be able to disable this fix for the time being if it causes an undesired behavior in an irrecoverable way. ([Ie1922](https://android-review.googlesource.com/#/q/Ie1922b03e8ec24a0b0d35995e407a3bcd09400a0))

**Bug Fixes**

- Fix issue where sticky headers were not sticking if a pinned item was present. ([I9198d](https://android-review.googlesource.com/#/q/I9198dc5afb50bb8704113f8ba3aa89b3a652a6ac), [b/385006133](https://issuetracker.google.com/issues/385006133))
- `TextObfuscationMode.RevealLastTyped` now follows the system setting "TEXT_SHOW_PASSWORD". ([I41c0c](https://android-review.googlesource.com/#/q/I41c0c91d93a8e4f5d3ae33fb6652997c50eb700c))
- Fixed a bug where `BasicTextField` wrongly shows a "Clipboard pasted" warning when the text toolbar opens for the first time. ([I5fda2](https://android-review.googlesource.com/#/q/I5fda2582663a8ce74f4f6b0d03452994f9695e7c))

### Version 1.9.0-beta01

June 18, 2025

`androidx.compose.foundation:foundation-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e1d81d156ec778ff4b8bc291aa661d780576ea4c/compose/foundation).

**Breaking Changes**

- The `background` and `border` modifier nodes now implement `SemanticsModifierNode`. This can result in new `SemanticsNodes` added to the semantics tree and, therefore, lead to test failures in tests that make assumptions about the semantics tree structure. For example, tests that use `onChild`, `onParent`, `onSibling`, and other similar methods to make assertions can fail if a new node is added between the current and target nodes. The preferred way to fix these failures is to add a `testTag` to the target node directly. Another approach is to use a looser matcher, such as `onNode(hasAnyAncestor(hasText("ancestor")) and hasText("target"))`. ([I638b5](https://android-review.googlesource.com/#/q/I638b56cb3aa3f4f68a354dfa5a42201febee61bc))

**API Changes**

- Rename `Modifier.addTextContextMenuComponents` to `appendTextContextMenuComponents`. ([I4c43f](https://android-review.googlesource.com/#/q/I4c43fe5bda562755f85823ae6a53cd1030237319))
- Removed `AnnotatedOutputTransformation` and carried `addStyle` functions to `TextFieldBuffer`. `addStyle` can still only be called from `OutputTransformation`. ([I9930a](https://android-review.googlesource.com/#/q/I9930a56b2444939e5ab2cce66b4c8a442c6f30ec), [b/417991824](https://issuetracker.google.com/issues/417991824))
- Clickable is rewritten to not use suspend pointer input as an optimization. This feature is enabled by a flag - you can disable if you encounter a bug in the new implementation - `ComposeFoundationFlags.isNonSuspendingPointerInputInClickableEnabled`. ([I85b65](https://android-review.googlesource.com/#/q/I85b65452be174df2c548a2c4cf7d96b702596c23))
- Introduced `isFlingCancellationWithNestedScrollFixEnabled` to fix an issue with fling propagation in nested scrolling. In this CL we are restoring the fling continuation behavior removed in [aosp/3260391](https://android-review.googlesource.com/c/platform/frameworks/support/+/3260391). We will still cancel the fling animation in case the child is removed from composition. ([I467f4](https://android-review.googlesource.com/#/q/I467f4a8974a752d63bd3d6ab62e6eb751f5e2ccc), [b/405910180](https://issuetracker.google.com/issues/405910180), [b/419049142](https://issuetracker.google.com/issues/419049142), [b/416784125](https://issuetracker.google.com/issues/416784125))
- `WindowInsetsRulers`: changed `rulersIgnoringVisibility` to maximum. Changed `getDisplayCutoutBounds()` to be an extension function of `PlacementScope`. `WindowInsetsAnimationProperties` has been changed to `WindowInsetsAnimation` and the `getAnimationProperties()` has been changed to `getAnimation()`. ([I3816f](https://android-review.googlesource.com/#/q/I3816f062168c83c7bb9e320cfa59a6a4ce1637e8))
- Changed `InsetsRulers` to be in common code with the name `WindowInsetsRulers`. Simplified the API so all insets are `WindowInsetsRulers`. Extracted non-rulers animation properties to an `AnimationProperties` class. `WindowInsetsRulers.innermostOf()` can be used to merge multiple `WindowInsetsRulers`. ([I2f0c6](https://android-review.googlesource.com/#/q/I2f0c6aebeca80fc181e843da78743bf2a5289501), [b/415012444](https://issuetracker.google.com/issues/415012444))

**Bug Fixes**

- Re-add usage of `scrollAnimationSpec` in `ContentInViewNode`. The behavior was removed during the `scrollAnimationSpec` deprecation which caused use cases to be broken. ([I1436a](https://android-review.googlesource.com/#/q/I1436a3212c8f637935259243253f70db1163e584), [b/403301605](https://issuetracker.google.com/issues/403301605))

### Version 1.9.0-alpha04

June 4, 2025

`androidx.compose.foundation:foundation-*:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fd8d5a2f883c1cdd7f712b200d5a4fedf342136..786176dc2284c87a0e620477608e0aca9adeff15/compose/foundation).

**API Changes**

- `PrefetchScheduler` and customisation have been deprecated in favor of the internal implementation that does all the work automatically. ([I3a9a6](https://android-review.googlesource.com/#/q/I3a9a678918c7ce33174b9c330142a650cc9e3b2a), [b/420551535](https://issuetracker.google.com/issues/420551535))
- Updated `Scrollable2DState` to use an offset in the `canScroll` method instead of an angle. ([I28694](https://android-review.googlesource.com/#/q/I28694cebf0b29b236eea1eaa6e072c7cf7dad623), [b/417268474](https://issuetracker.google.com/issues/417268474))
- Replaced `addAnnotation` in `AnnotatedOutputTransformation` with `addStyle`. ([I91c6f](https://android-review.googlesource.com/#/q/I91c6f52917074ecfecdeadcb96a5da4f14592f8e), [b/417991824](https://issuetracker.google.com/issues/417991824))
- Stabilized `LazyLayout`. ([If5db4](https://android-review.googlesource.com/#/q/If5db4170daec197e39612bcfb5f8b5d4cdd8db52))
- Stabilized an empty constructor for `LazyLayoutPrefetchState` and it's scheduling method `schedulePrecomposition` and `schedulePrecompositionAndPremeasure`. ([I4362f](https://android-review.googlesource.com/#/q/I4362f3417ebe652d967463a474e4ba799967930d), [b/252853717](https://issuetracker.google.com/issues/252853717))
- Introduced `ProcessTextKey` on Android used for context menu items that's added for `PROCESS_TEXT` intent actions. ([If0ac4](https://android-review.googlesource.com/#/q/If0ac40e1a2c4e385de4ebeb0e41afc5f09b00187))
- Make context menu APIs public. Exposed `Modifier.addTextContextMenuComponents` and `Modifier.filterTextContextMenuComponents` to add and remove items in context menu. And also made the following elementary APIs public so that one can build a customized context menu:
  - `TextContextMenuProvider`
  - `TextContextMenuDataProvider`
  - `TextContextMenuData`
  - `TextContextMenuComponent`
  - `LocalTextContextMenuDropdownProvider`
  - `LocalTextContextMenuToolbarProvider` ([I1b7b0](https://android-review.googlesource.com/#/q/I1b7b0fd6744fbae808a3e142cca4ad53bd3731f1))
- Make `LazyLayoutItemProvider` stable ([Icce09](https://android-review.googlesource.com/#/q/Icce09a01e2668ea0a93678ec84d189aa4769e26c), [b/261565751](https://issuetracker.google.com/issues/261565751))
- Introduced android smart selection features that can be enable/disabled via `ComposeFoundationFlags.isSmartSelectionEnabled`. It also exposed a static `compositionLocal` `LocalTextClassifierCoroutineContext` that can be used to specify the `CoroutineContext` in which the `TextClassification` job is launched. ([I1dbaa](https://android-review.googlesource.com/#/q/I1dbaa65e254cc11c1217d2c8ff551c92f7f642f6), [b/139321320](https://issuetracker.google.com/issues/139321320))

### Version 1.9.0-alpha03

May 20, 2025

`androidx.compose.foundation:foundation-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..5fd8d5a2f883c1cdd7f712b200d5a4fedf342136/compose/foundation).

**API Changes**

- Added `AnnotatedOutputTransformation` that provides a way to add annotations to `TextField` before rendering. ([Ibc6f0](https://android-review.googlesource.com/#/q/Ibc6f08a54bf25e0c6352839df7c2acc6607db482), [b/389978748](https://issuetracker.google.com/issues/389978748))
- Introduce `LazyLayoutMeasurePolicy` and make `LazyLayoutMeasureScope` stable. ([I8c5df](https://android-review.googlesource.com/#/q/I8c5dfa6083fb7d5faf58229556f6b2231386b276), [b/252853717](https://issuetracker.google.com/issues/252853717))
- `BasicSecureTextField` now hoists ScrollState of its internal `BasicTextField`. ([I6e576](https://android-review.googlesource.com/#/q/I6e576357e0fefca548697f83bef17f5e3c3b9648))
- `Modifier.onFirstVisible` and `Modifier.onVisibilityChanged` modifiers were introduced, which are high level modifiers built on top of `Modifier.onLayoutRectChanged`. These modifiers are built specifically to handle a lot of common application requirements such as logging impressions, auto playing videos, etc. These have been built with performance in mind so that they can be used in critical list-based scenarios without risk of sacrificing scroll performance. In addition to these modifier APIs, additional APIs to `RelativeLayoutBounds` have been added in order to support these use cases, as well as make it easier for developers to easily create similar custom modifiers that suit their use case exactly. ([I759b8](https://android-review.googlesource.com/#/q/I759b8256fd7797ad9a10a955368231b70470dd7c))
- Introduced a `detectDragGestures` overload that has touch slop and orientation lock control. ([Iadb0d](https://android-review.googlesource.com/#/q/Iadb0d52c5faf9d37a294f5ea6b529615a0ec8c0e))
- Introduce `Modifier.scrollable2D`, `Scrollable2DState` and companion APIs for state creation. Also introduced common scroll extension functions. ([Ic61c8](https://android-review.googlesource.com/#/q/Ic61c8f14451090f441b009bf8f86e7566c27c782), [b/214410040](https://issuetracker.google.com/issues/214410040))
- Compose 64-bit color values are not directly comparable to Android `ColorLongs` because the color space IDs are out of order for some color spaces. To convert to and from Android color spaces, two new APIs are added: `toColorLong()` and `fromColorLong()`. ([I36899](https://android-review.googlesource.com/#/q/I368990c572cebb2895f87291e9b966ba96b73961))

**Bug Fixes**

- Text copied from multiple Text composables in a `SelectionContainer` now will have a line separator `\n` added between text coming from the separate Text composables. ([I25332](https://android-review.googlesource.com/#/q/I25332168924ca35574bb8c5e7094ad8010ab5927), [b/285036739](https://issuetracker.google.com/issues/285036739))

### Version 1.9.0-alpha02

May 7, 2025

`androidx.compose.foundation:foundation-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/foundation).

**API Changes**

- Fixed how pointer input changes are added to the `VelocityTracker` in `DragGestureNode`, this can be controlled with the new flag `isOffsetPositionBeforeAddingToVelocityTrackerEnabled`. ([Ic7992](https://android-review.googlesource.com/#/q/Ic7992d09a4d1bab4e1a4e988afae681d654cf61f), [b/292556787](https://issuetracker.google.com/issues/292556787), [b/236451818](https://issuetracker.google.com/issues/236451818))
- Make `await[Vertical/Horizontal]PointerSlopOrCancellation` public ([I6968b](https://android-review.googlesource.com/#/q/I6968be9620a13a21deb2cd4c3201bc3ca0f72353), [b/298903681](https://issuetracker.google.com/issues/298903681))
- `AbstractComposeView.consumeWindowInsets` now defaults to false. `WindowInsets` will automatically be adjusted for child size and position when set to false, so there is no need to default it to true any longer. This fixes the issue where child Views were not receiving `WindowInsets` updates by default. Developers can opt out of the update either by changing the experimental `ComposeFoundationLayout.isWindowInsetsDefaultPassThroughEnabled` to true or, preferably, by setting `AbstractComposeView.consumeWindowInsets` to true on all Compose view instances. ([I6fa0a](https://android-review.googlesource.com/#/q/I6fa0a74f9b1a25107bebc586f2058bbb598b5eff), [b/411868840](https://issuetracker.google.com/issues/411868840))

**External Contribution**

- Fixed Pager crash with extremely large beyondViewportPageCount values ([Idb2db](https://android-review.googlesource.com/#/q/Idb2dbbe5e8d24bb032664c02a3b3fffd6a8d3845))

### Version 1.9.0-alpha01

April 23, 2025

`androidx.compose.foundation:foundation-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/foundation).

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

- Breaking change: `clickable`, `combinedClickable`, `selectable`, `toggleable`, and `triStateToggleable` overloads without an Indication parameter now only support `IndicationNodeFactory` instances provided using `LocalIndication`. This change will apply when you recompile your usages of these modifiers using this version of Compose. Binary / transitive dependencies are not affected. If you are providing a deprecated Indication implementation to `LocalIndication`, and using these APIs, this will introduce a crash at runtime. This behavior change is needed to enable improved performance, and allow Composable functions using these modifiers to skip during recomposition. You can use `ComposeFoundationFlags.isNonComposedClickableEnabled=false` to temporarily opt-out of this behavior change, to enable upgrading Compose without being blocked on this migration. This flag will be removed after one stable release. To resolve, migrate any deprecated Indication implementations to use `IndicationNodeFactory` instead. You can also use the overloads with an explicit Indication parameter - these overloads will continue to support non-`IndicationNodeFactory` instances of Indication, although this is not recommended for performance reasons. ([I6bcdc](https://android-review.googlesource.com/#/q/I6bcdc6ff82dd6ff5ea1a97688d5a1426b719df20), [b/316914333](https://issuetracker.google.com/issues/316914333))

**API Changes**

- Introduce API for creating custom bullet lists through `AnnotatedString` ([I1d066](https://android-review.googlesource.com/#/q/I1d066d3df73999bd3c771b72982fe8bbccc822ae), [b/383269496](https://issuetracker.google.com/issues/383269496), [b/139326648](https://issuetracker.google.com/issues/139326648))
- Allow Compose to trigger `ViewTreeObserver.OnScrollChanged`. This behavior is introduced under the flag `isOnScrollChangedCallbackEnabled`. We also introduced an extension function of `DelegatableNode dispatchOnScrollChanged`. ([I34b9d](https://android-review.googlesource.com/#/q/I34b9d923ff1fb4a4e27a53e583a7b082bc99b158), [b/238109286](https://issuetracker.google.com/issues/238109286))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Added lint check support for `TextFieldState` to make sure it is remembered inside composition. Consider using `rememberTextFieldState` instead. ([I53d74](https://android-review.googlesource.com/#/q/I53d749ff2b2cad5e02c8f87940a36656d6437467))
- Added lint check support for `FocusRequester` to make sure it is remembered inside composition ([I6bf91](https://android-review.googlesource.com/#/q/I6bf911348f006b4f04fe2c5633aba0a060ec4fd1))
- Added lint check support for `BringIntoViewRequester` to make sure it is remembered inside composition. ([Ibfba6](https://android-review.googlesource.com/#/q/Ibfba6998dc6916bf409d8f4d6b142d715f89c29f))
- Introduced scopes for `schedulePrefetch` calls in grids and lists strategies to align with the `LazyListPrefetchState` capabilities of providing size and index info. ([Iad80c](https://android-review.googlesource.com/#/q/Iad80ca8c87d1d2823f87cb40fc81579c4f6f484c))
- Breaking change: `clickable`, `combinedClickable`, `selectable`, `toggleable`, and `triStateToggleable` overloads without an Indication parameter now only support `IndicationNodeFactory` instances provided using `LocalIndication`. This change will apply when you recompile your usages of these modifiers using this version of Compose. Binary / transitive dependencies are not affected. If you are providing a deprecated Indication implementation to `LocalIndication`, and using these APIs, this will introduce a crash at runtime. This behavior change is needed to enable improved performance, and allow Composable functions using these modifiers to skip during recomposition. You can use `ComposeFoundationFlags.isNonComposedClickableEnabled=false` to temporarily opt-out of this behavior change, to enable upgrading Compose without being blocked on this migration. This flag will be removed after one stable release. To resolve, migrate any deprecated Indication implementations to use `IndicationNodeFactory` instead. You can also use the overloads with an explicit Indication parameter - these overloads will continue to support non-`IndicationNodeFactory` instances of Indication, although this is not recommended for performance reasons. ([I6bcdc](https://android-review.googlesource.com/#/q/I6bcdc6ff82dd6ff5ea1a97688d5a1426b719df20), [b/316914333](https://issuetracker.google.com/issues/316914333))
- Introduce a flag for controlling the automatic nested prefetch behavior: `isAutomaticNestedPrefetchEnabled` ([I8d448](https://android-review.googlesource.com/#/q/I8d448db663c7733d7df9b5c24326371221aaaec6))
- Introduce an overload for `LazyGridState` and `rememberLazyGridState` that takes a `LazyLayoutCacheWindow`. ([I51151](https://android-review.googlesource.com/#/q/I511510d5db20c6c810b1ff4872db6ff3af8738e5))
- Adds Rulers for Window Insets. Adds `DerivedRuler` to allow a Ruler to be calculated from another Ruler. Modifies `PlacmentScope` to implement Density. ([I658bc](https://android-review.googlesource.com/#/q/I658bc9f5e707d2b74b51790ff7541c10448e4c9b), [b/359260964](https://issuetracker.google.com/issues/359260964))
- Added a zero arg `WindowInsets()` factory function to easily create empty `WindowInsets`. ([I65f62](https://android-review.googlesource.com/#/q/I65f6296e8d870ac93dd38d086c41a7e9c04ba59d), [b/395311689](https://issuetracker.google.com/issues/395311689))
- Added `PaddingValues.Zero` for an empty `PaddingValues`. ([If193e](https://android-review.googlesource.com/#/q/If193e919401ab4350577e4f0d03be5e7eaa0f743), [b/386255688](https://issuetracker.google.com/issues/386255688))

**Bug Fixes**

- The `state` overload of `BasicTextField` will keep the cursor scrolled into view when its size changes. ([I0eb41](https://android-review.googlesource.com/#/q/I0eb41276b627d49889d3aedb11b58ba4d2ec0b74), [b/406187741](https://issuetracker.google.com/issues/406187741))
- Updated `onVisibleItemsUpdated` APIs in `LazyListPrefetchStrategy` and `LazyGridPrefetchStrategy` to inform about initial state. ([If2cfa](https://android-review.googlesource.com/#/q/If2cfa51541b20f0646131241beb215e6e8c1f671))

## Version 1.8

### Version 1.8.3

June 18, 2025

`androidx.compose.foundation:foundation-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/754896be0859599f16ed264d79a04ee337bac777..13362f65a9c0649415fe57052ea0e3932d2303d1/compose/foundation).

### Version 1.8.2

May 20, 2025

`androidx.compose.foundation:foundation-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/018e42f9db74b5e4fce8007734de4da6ae087407..754896be0859599f16ed264d79a04ee337bac777/compose/foundation).

**Bug Fixes**

- Introduced a fix that prevents calculation of number of items to load for focus search to cause a division by zero. Applied the check to all layouts that use `LazyLayoutBeyondBoundsState`. ([8e6dc8](https://android-review.googlesource.com/#/q/I09bae509c111236b9db1426a80a46f0af6f0344a))

### Version 1.8.1

May 7, 2025

`androidx.compose.foundation:foundation-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..018e42f9db74b5e4fce8007734de4da6ae087407/compose/foundation).

**Bug Fixes**

- Fixed a bug in `BasicText` and `TextAutoSize` where using `TextOverflow.Ellipsize` would result in smaller-than-optimal text. ([I1e1d8](https://android-review.googlesource.com/#/q/I1e1d8710f8719edb229d4826da746d195875590b), [b/396582066](https://issuetracker.google.com/issues/396582066))
- Fixed a bug in `BasicTextField` that caused miscellaneous crashes when `TextFieldDecorator` skips calling `innerTextField`. ([I2638c](https://android-review.googlesource.com/#/q/I2638c2cffea1ac5f4bd8ce105cdfc79a2503f0ab)), [b/308398612](https://issuetracker.google.com/issues/308398612)
- Fixed a bug in `TextField` that caused the text toolbar and selection handles to completely disappear when the `TextFieldState` instance was changed. ([I8068a](https://android-review.googlesource.com/#/q/I8068a9f18f9834421f7e3aca4bba47df333384a2)), [b/390477786](https://issuetracker.google.com/issues/390477786)
- Fixed a bug in `BasicText` where changing the min width constraint did not update the text's placement when `textAlign` was set to a non-default value. ([I77a96](https://android-review.googlesource.com/#/q/I77a9635afe19b45cbf286924f9b5e1c79258a7f1)), [b/406305552](https://issuetracker.google.com/issues/406305552)

### Version 1.8.0

April 23, 2025

`androidx.compose.foundation:foundation-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b6bba717628c4c8c633c9509bfc4e4d9b89f428..d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9/compose/foundation).

### Version 1.8.0-rc03

April 9, 2025

`androidx.compose.foundation:foundation-*:1.8.0-rc03` is released. Version 1.8.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0907800009c0cb37dd12c5586d620350c1975de..1b6bba717628c4c8c633c9509bfc4e4d9b89f428/compose/foundation).

### Version 1.8.0-rc02

March 26, 2025

`androidx.compose.foundation:foundation-*:1.8.0-rc02` is released. Version 1.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/071f2b22541efa1d5d528479b28aa42960923a4f..c0907800009c0cb37dd12c5586d620350c1975de/compose/foundation).

### Version 1.8.0-rc01

March 12, 2025

`androidx.compose.foundation:foundation-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d195d8376d369f4bf74652abe60101aa658bbcc..071f2b22541efa1d5d528479b28aa42960923a4f/compose/foundation).

### Version 1.8.0-beta03

February 26, 2025

`androidx.compose.foundation:foundation-*:1.8.0-beta03` is released. Version 1.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/08954f0d500d220e8d6af07b4e6c51090911f779..2d195d8376d369f4bf74652abe60101aa658bbcc/compose/foundation).

**Bug Fixes**

- Added a new semantics property `InputText` that captures a textfield's value before output transformation is applied. ([Iae46a](https://android-review.googlesource.com/#/q/Iae46a52e7fbb1a3558e897c5afebd125089befbb), [b/395911609](https://issuetracker.google.com/issues/395911609), [b/176949051](https://issuetracker.google.com/issues/176949051))
- Removed deprecated `AutoSize` overloads. Please use the `TextAutoSize` APIs serving the same function. ([I2c90f](https://android-review.googlesource.com/#/q/I2c90f11c8cdfdd3b1f92cf1f401df6a911017693))
- Fixed a caching issue with `TextAutoSize` where a second layout pass with the same constraints could result in using the second-biggest fitting font size instead of the biggest. ([Id367f](https://android-review.googlesource.com/#/q/Id367f4f18e4e0a1bd7c8076a0f956af773dc986b))

### Version 1.8.0-beta02

February 12, 2025

`androidx.compose.foundation:foundation-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5d82c9c8e72f3dd8c4ee71ff5ac9a1365d24de4..08954f0d500d220e8d6af07b4e6c51090911f779/compose/foundation).

**Bug Fixes**

- Fixed an issue where overscroll implementations using `LayoutModifierNode` would not work correctly inside scrolling containers.

### Version 1.8.0-beta01

January 29, 2025

`androidx.compose.foundation:foundation-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8..80c9eca8dc00a6ae7188bf5f2beaf129b79de243/compose/foundation).

**API Changes**

- `SemanticsNodeInteraction.semanticsId()` has been removed. Use `SemanticsNodeInteraction.fetchSemanticsNode().id` instead. ([Ie397a](https://android-review.googlesource.com/#/q/Ie397a87c7e8bfd754474ebbb03c26f4a3215ba52))
- Rewrite `requestAutofill` API to exist outside of autofill manager. ([Id1929](https://android-review.googlesource.com/#/q/Id1929e5264d1a4a86b937236ee9357529f79fc71))
- `ContextualFlowRow` and `ContextualFlowColumn` have been marked as deprecated. This experimental component was introduced in 1.7 and had not yet been stabilized, and the implementation has been deemed undesirable. In the future, a component solving the use cases this component was meant to solve may be provided.
  - `FlowRow` and `FlowColumn` have experimental overloads that were introduced in 1.7 that include an `overflow` parameter. The use of this parameter has been deprecated, and the overloads without this parameter can be used instead. The default "overflow" behavior for these overloads will be "Clip", as it was since its introduction.
  - Many use cases for `ContextualFlowRow` can be accomplished using `FlowRow`, but we acknowledge that is not true in full generality. `ContextualFlowRow` is completely implementable in user-space, and one can attempt to copy its implementation and adapt if desired. In the future, we hope to solve these use cases in a different way. ([Ibafec](https://android-review.googlesource.com/#/q/Ibafec7f7926d2060f7551910264d5dd51637cafc))

**Bug Fixes**

- Fix text layout with ellipsis sometimes translating incorrectly during animations, see [b/389707025](https://issuetracker.google.com/issues/389707025) for more info ([Ie55b1](https://android-review.googlesource.com/#/q/Ie55b173dee87596cd270788794b3c0e5e20a0dc6), [b/389707025](https://issuetracker.google.com/issues/389707025))
- Fixed a bug in `BasicText` with `TextAutoSize` and `maxLines` set to 1. ([Ic0450](https://android-review.googlesource.com/#/q/Ic0450c763c5d764492995b44ee1fe570246a9689), [b/376834366](https://issuetracker.google.com/issues/376834366))
- Text's minimum intrinsics height now takes `minLines` parameter into account. It means that minimum intrinsics height reported won't be smaller than the height required to satisfy the `minLines` parameter ([I225f9](https://android-review.googlesource.com/#/q/I225f910dcbff2292d045ffac0750544d4601eeba), [b/388299762](https://issuetracker.google.com/issues/388299762))

### Version 1.8.0-alpha08

January 15, 2025

`androidx.compose.foundation:foundation-*:1.8.0-alpha08` is released. Version 1.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/foundation).

**API Changes**

- AutoSize: Renamed `AutoSize` to `TextAutoSize` and published APIs that enable creating custom `TextAutoSize` implementations. See `TextAutoSizeSample` for an example of a custom text auto size implementation. ([I85756](https://android-review.googlesource.com/#/q/I85756591bf459504a338a1e42c18b2d175c4561a))
- Moved the `DetectTapGesturesEnableNewDispatchingBehavior` feature flag to `ComposeFoundationFlags` and renamed it to `isDetectTapGesturesImmediateCoroutineDispatchEnabled`. The old flag is deprecated and will now delegate to `ComposeFoundationFlags.isDetectTapGesturesImmediateCoroutineDispatchEnabled` instead. ([I62932](https://android-review.googlesource.com/#/q/I629321d209cfc727992fbb57db6f82d58e09771a))

**Bug Fixes**

- Enabled `DetectTapGesturesEnableNewDispatchingBehavior` by default. `TapGestureDetector` APIs now use the new dispatching behavior (immediate dispatch) by default. ([I9f2bc](https://android-review.googlesource.com/#/q/I9f2bc726cffd87500d10962c067541d8add69b63), [b/369648479](https://issuetracker.google.com/issues/369648479))
- Fixed the `requiredWidth/Height/Size` modifiers to properly handle intrinsic sizes. ([Ie3d7d](https://android-review.googlesource.com/#/q/Ie3d7dbd737fa3162a58feca8a596134a4baf201d), [b/368113212](https://issuetracker.google.com/issues/368113212))

**External Contribution**

- Commonized `BasicTooltip` in foundation and `BasicTooltip/Tooltip` in material3. ([Ifc2e6](https://android-review.googlesource.com/#/q/Ifc2e61bf8dac507072ec7e52a803f40422367c68))
- Added a new Clipboard interface and a composition local for it. ([I80809](https://android-review.googlesource.com/#/q/I808099e232564d551aeeb8ed09e74ab62d9354ed))

### Version 1.8.0-alpha07

December 11, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha07` is released. Version 1.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/compose/foundation).

**API Changes**

- Deleted `ComposeFoundationFlags.RemoveBasicTextGraphicsLayerEnabled` flag that helped revert the removal of internal `graphicsLayer` from `BasicText`. If you were using this flag please let us know of the reasons by filing a bug. Also you can just pass in `Modifier.graphicsLayer()` to your `BasicText` calls to achieve the same behavior as before. ([Id9f90](https://android-review.googlesource.com/#/q/Id9f90910d19dd7bb9e3a43aede83d5bd9188c450))
- Added default implementation for new `stickyHeader` DSL. ([I68986](https://android-review.googlesource.com/#/q/I6898663e2599264a98e6ce2537ef9f0e065db571))
- Has `LocalAutofillHighlightColor` composition local use a Color type. ([I0e05b](https://android-review.googlesource.com/#/q/I0e05bc47c50ff04a873169ab69dfc79f9ecc0579))
- Renamed `OverscrollEffect#withoutDrawing` to `OverscrollEffect#withoutVisualEffect`. ([I1a154](https://android-review.googlesource.com/#/q/I1a154f66a48cea170b6f1de3b98aaf451fb1f111))

**Bug Fixes**

- Follow-up fix for an issue in `AnchoredDraggable`'s target calculation where it could settle at the wrong anchor for specific swipes. ([I23b87](https://android-review.googlesource.com/#/q/I23b8773d3a694aa3c8de6a8f34b9d7fb54cfe560), [b/367660226](https://issuetracker.google.com/issues/367660226))

**External Contribution**

- Add `BringIntoViewResponderModifierNode` to UI, which provides a new way to implement Bring Into View functionality as well as allows implementing in on a platform level ([Ia6dd8](https://android-review.googlesource.com/#/q/Ia6dd89b79c7a4e04fea0d73410b2b76e779b793f))
- We are ever slightly changing the way the cursor is drawn. You can use `LocalCursorBlinkEnabled` to disable the cursor drawing in tests. ([I4c697](https://android-review.googlesource.com/#/q/I4c6979903bec329287ec25093f55b83668d674ea))

### Version 1.8.0-alpha06

November 13, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha06` is released. Version 1.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/foundation).

**API Changes**

- Adds `stylusHoverIcon` modifier. ([Iff20a](https://android-review.googlesource.com/#/q/Iff20af03b451228bc44c4356d4b4e89956cc3b45), [b/331289114](https://issuetracker.google.com/issues/331289114))
- Deprecated `AnchoredDraggableState`'s `confirmValueChange`. Instead of vetoing state changes, disallowed anchors should not be in the active anchor set, and an `OverscrollEffect` should be used to indicate the unavailability of the requested action. ([Ia717f](https://android-review.googlesource.com/#/q/Ia717fb7dba3db65609a933a55b164d2186e25806))
- Changes Autofill manager to be an interface. ([I84914](https://android-review.googlesource.com/#/q/I8491407de5699bf7273b9f88bda11cc438e2fd62), [b/376080755](https://issuetracker.google.com/issues/376080755))
- Adds `OverscrollEffect#withoutDrawing` and `OverscrollEffect#withoutEventHandling` APIs - these APIs create a wrapped instance of the provided overscroll effect that doesn't draw / handle events respectively, which allows for rendering overscroll in a separate component from the component that is dispatching events. For example, disabling drawing the overscroll inside a lazy list, and then drawing the overscroll separately on top / elsewhere. ([Idbb3d](https://android-review.googlesource.com/#/q/Idbb3d91546b49c1987a041f959bce4b2b09a9f61), [b/266550551](https://issuetracker.google.com/issues/266550551), [b/204650733](https://issuetracker.google.com/issues/204650733), [b/255554340](https://issuetracker.google.com/issues/255554340), [b/229537244](https://issuetracker.google.com/issues/229537244))
- Adding autofill support in text toolbar. ([Ie6a4c](https://android-review.googlesource.com/#/q/Ie6a4c0542737d76d603a925f85c389c81eb49747))
- Deprecates `OverscrollConfiguration` and `LocalOverscrollConfiguration`, and adds `rememberPlatformOverscrollFactory` to create an instance of / customize parameters of the default overscroll implementation. To disable overscroll, instead of `LocalOverscrollConfiguration provides null`, use `LocalOverscrollFactory provides null`. To change the glow color / padding, instead of `LocalOverscrollConfiguration provides OverscrollConfiguration(myColor, myPadding)`, use `LocalOverscrollFactory provides rememberPlatformOverscrollFactory(myColor, myPadding)`. ([Ie71f9](https://android-review.googlesource.com/#/q/Ie71f9a016face13262f4fe16ac56c40a0d6f9712), [b/255554340](https://issuetracker.google.com/issues/255554340), [b/234451516](https://issuetracker.google.com/issues/234451516))
- Changed the `effectModifier` property on `OverscrollEffect` to be `node: DelegatableNode`, consistent with other APIs. ([Ic0b46](https://android-review.googlesource.com/#/q/Ic0b46a80aa7d9426ced0731531b3492093e1654e), [b/255554340](https://issuetracker.google.com/issues/255554340))
- Removed the experimental `GlobalAssertions` API. It's intended use was to run accessibility checks, see `enableAccessibilityChecks()` for that purpose instead. ([I59322](https://android-review.googlesource.com/#/q/I5932296f2aca4c3daa30a013dd00e876ecebb077))

### Version 1.8.0-alpha05

October 30, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha05` is released. Version 1.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/foundation).

**New Features**

- Support for auto-sizing text. Pass an `AutoSize` instance (e.g. `AutoSize.StepBased`) to your favorite text composable (like `BasicText`) and see your text size adapt to the available space! ([Ice7e0](https://android-review.googlesource.com/#/q/Ice7e09b9cac7be10ab5e681ec57d994d50102583), [b/139320827](https://issuetracker.google.com/issues/139320827))
- Adds `OverscrollFactory` and `LocalOverscrollFactory` APIs to allow configuring overscroll within a hierarchy. The value provided through `LocalOverscrollFactory` will be used by default to create an `OverscrollEffect`. To create and remember an effect from the current provided factory, use `rememberOverscrollEffect()`. ([I51ca4](https://android-review.googlesource.com/#/q/I51ca476f3efcf0249640873f74cf7d40beebb788), [b/255554340](https://issuetracker.google.com/issues/255554340))

**API Changes**

- Introduce `CompositionLocal` that can be used to modify the hue of Autofill's successful filling highlight. ([I32092](https://android-review.googlesource.com/#/q/I320926246d1811c2c974a6793f48941907c33afe))
- Removed `ScrollableDefaults.overscrollEffect` - instead you should use `rememberOverscrollEffect`. This will create an instance of the current overscroll implementation provided with `LocalOverscrollFactory`. ([I1651a](https://android-review.googlesource.com/#/q/I1651acbab8ddb4b35399af103e3db76b37361303), [b/255554340](https://issuetracker.google.com/issues/255554340)),([b/234451516](https://issuetracker.google.com/issues/234451516))
- Introduces new `AutofillManager` interface that can be used to fine-tune users' Autofill journey and a `isSemanticAutofillEnabled` flag to turn on this new version of Autofill. ([I9d484](https://android-review.googlesource.com/#/q/I9d4842cc35b289158e889f89b7b65346f049e884))
- Removes `CombinedClickableNode`. This experimental API was temporarily exposed to unblock performance work, but is no longer needed. Instead you should directly use `Modifier.combinedClickable` as with other modifier APIs. ([I4b658](https://android-review.googlesource.com/#/q/I4b658dabfefb13eb5bff42029502486ab89b7a6f))
- Adds overloads to `horizontalScroll`, `verticalScroll`, `LazyColumn`, `LazyRow`, `LazyHorizontalGrid`, `LazyVerticalGrid`, `LazyHorizontalStaggeredGrid`, `LazyVerticalStaggeredGrid`, `HorizontalPager`, and `VerticalPager` with support for specifying a custom `OverscrollEffect`. The provided `OverscrollEffect` will receive events, and be rendered within the bounds of these components. Note that drawing the same `OverscrollEffect` twice is unsupported - so you cannot draw the same `OverscrollEffect` provided to one of these components separately with `Modifier.overscroll`. The use case of drawing the overscroll outside of the bounds of these components will be addressed separately in the future. ([I2dc42](https://android-review.googlesource.com/#/q/I2dc42851c824a63e495312246eb5389c33121af8), [b/266550551](https://issuetracker.google.com/issues/266550551), [b/234274772](https://issuetracker.google.com/issues/234274772), [b/224572538](https://issuetracker.google.com/issues/224572538), [b/353805117](https://issuetracker.google.com/issues/353805117))

### Version 1.8.0-alpha04

October 16, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha04` is released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/foundation).

**API Changes**

- Adds `DelegatableNode#onDensityChange` and `DelegatableNode#onLayoutDirectionChange` callbacks to allow updating node state when these change. ([I04f3e](https://android-review.googlesource.com/#/q/I04f3e3afea5aabdc6225b1afb197df18133eb018), [b/340662451](https://issuetracker.google.com/issues/340662451))
- Paragraph and `ParagraphIntrinsics` now takes a list of all annotations applied to the `AnnotatedString`, previously it only had a list of `SpanStyles`. ([I12f80](https://android-review.googlesource.com/#/q/I12f8071e3bb8ed7871bb659e256569182680d49e))
- Introduced `PointerInputModifierNode#touchBoundsExpansion`, which can be used to enlarge the touch bounds of a single pointer input modifier. ([Iccf02](https://android-review.googlesource.com/#/q/Iccf028b886639d3b24e7a257a023320362399389), [b/335339283](https://issuetracker.google.com/issues/335339283))

**Bug Fixes**

- Fixed a bug where positional thresholds passed to `AnchoredDraggableDefaults.flingBehavior` were not considered correctly in some scenarios. ([Ifdf0d](https://android-review.googlesource.com/#/q/Ifdf0dfcf3d7ff8288affee56e7092bbed473d6ab), [b/367660226](https://issuetracker.google.com/issues/367660226))
- Introduce a fix for nested scrollables that are removed from the node tree during an ongoing fling. Now these nodes will cancel the fling and correctly send the `onPostFling` event with the remaining velocity. We're also introducing the flag `NewNestedScrollFlingDispatchingEnabled` to control the behavior in case of regressions. The flag will be removed before beta. ([I05c37](https://android-review.googlesource.com/#/q/I05c37b5d0ae42d8ed97c014383fe9df3282d61d6), [b/371168883](https://issuetracker.google.com/issues/371168883))
- Fixed a bug where `OverscrollEffects` passed to `Modifier.anchoredDraggable` would receive 2D deltas instead of 1D. ([Ie52c0](https://android-review.googlesource.com/#/q/Ie52c0db5e85eef359cf82b2f88713a31cf6802f4))

### Version 1.8.0-alpha03

October 2, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha03` is released. Version 1.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/compose/foundation).

**API Changes**

- Kotlin version update to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))
- Introduced flag `DraggableAddDownEventFixEnabled` ([I848d5](https://android-review.googlesource.com/#/q/I848d5633a27bdf6c115df486e1cc9d881d4547b7))
- Introduced a new Semantics Role called Carousel to emulate the list behavior in Pagers for a11y services. ([Id354b](https://android-review.googlesource.com/#/q/Id354b132da03348aaa68da0dd8459d4528438018), [b/354109776](https://issuetracker.google.com/issues/354109776), [b/239672673](https://issuetracker.google.com/issues/239672673))
- Removed the implicit `graphicsLayer` modifier from `BasicText` composable. Added experimental `ComposeFoundationFlags.RemoveBasicTextGraphicsLayerEnabled` flag to be able to revert to the old behavior. ([Ie478d](https://android-review.googlesource.com/#/q/Ie478db03fec7f5a7ee48b46e03a63c4b718fe69c))
- Added `Modifier.recalculateWindowInsets()` to allow children in the hierarchy to use `insetsPadding` even when parents aligned them without `consumeWindowInsets()`. ([I7f9e4](https://android-review.googlesource.com/#/q/I7f9e42ad23eb6a8706ab9c04dc60460b3e91695d))

**Bug Fixes**

- Implement gesture pick-up in `detectDragGestures`, draggables and scrollables. Now if a child draggable gives up on a gesture, the parent has the opportunity to pick it up. This allows for a more continuous and integrated gesture handling. ([Ic88fe](https://android-review.googlesource.com/#/q/Ic88fe7a8d34eb49ae279b922ef570a3464924727))
- Update fling cancellation behavior in scrollables. Now if a scrollable flings and hits the bounds it will correctly pass on the fling velocity to the next scrollable in the chain instead of continue to drive the fling. ([I9326a](https://android-review.googlesource.com/#/q/I9326ad40271d77d6b2f8038c6fb9eb313873d8b6))

### Version 1.8.0-alpha02

September 18, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988..0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/foundation).

**API Changes**

- `TextOverflow.StartEllipsis` and `TextOverflow.MiddleEllipsis` are now available which allows to place ellipsis at the start or middle of the line of the single line text ([I38913](https://android-review.googlesource.com/#/q/I389132c71774d5c13afce85a8719af697431cef9), [b/185418980](https://issuetracker.google.com/issues/185418980))

### Version 1.8.0-alpha01

September 4, 2024

`androidx.compose.foundation:foundation-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/compose/foundation).

## Version 1.7

### Version 1.7.8

February 12, 2025

`androidx.compose.foundation:foundation-*:1.7.8` is released. Version 1.7.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/456f991655af86d9ae121f7e93f8699f958fc7ac..215cdfd8cb9c0762dd0347c383250644057c367f/compose/foundation).

**Bug Fixes**

- Fix crash in `BasicTextField` with input transformation when replacing part of the pasted text. ([I73702](https://android-review.googlesource.com/#/q/I73702a6ff3274bec6ea66cd7729aacd1437bb19a))

### Version 1.7.7

January 29, 2025

`androidx.compose.foundation:foundation-*:1.7.7` is released. Version 1.7.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5e65beadeb2e2c15f34d0fff72861847795cca4f..456f991655af86d9ae121f7e93f8699f958fc7ac/compose/foundation).

**Bug Fixes**

- Fixed `IndexOutOfBound` crash with link annotation. ([Ic96d2](https://android-review.googlesource.com/#/q/6b1682b753b1496ba7e65e91dfefbb6f13172143))
- Fixed infinite recomposition in some edge cases with links. ([I04a03](https://android-review.googlesource.com/#/q/c0a6a8c46d1a6dfcdbde84e68a3f75a96418eabe))

**Known Bugs**

- A bug was identified that can cause text to wrap unexpectedly in rare scenarios on Android API level 35. It cannot be fixed in 1.7, so it will be fixed in 1.8. ([b/391378120](https://issuetracker.google.com/391378120))

### Version 1.7.6

December 11, 2024

`androidx.compose.foundation:foundation-*:1.7.6` is released. Version 1.7.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cbf03b378a865660d8209d0229c2bb1928c6e33..5e65beadeb2e2c15f34d0fff72861847795cca4f/compose/foundation).

**Bug Fixes**

- Fixed text inline content not being visible to accessibility services.
- Fixed an issue where `AndroidEmbeddedExternalSurface` would not reset properly and be stuck when reusing in a lazy list.

### Version 1.7.5

October 30, 2024

`androidx.compose.foundation:foundation-*:1.7.5` is released. Version 1.7.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b0ae0e41147a8a917cab35b4a6487af4fce6ead..4cbf03b378a865660d8209d0229c2bb1928c6e33/compose/foundation).

**Bug Fixes**

- Ensure that pinned items are not subcomposed twice in the content padding area. ([Ic6224](https://android-review.googlesource.com/#/q/Ic62242563f2ed9790dd34d7efd15f0e3cb1a4b3b))

### Version 1.7.4

October 16, 2024

`androidx.compose.foundation:foundation-*:1.7.4` is released. Version 1.7.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/00e91ed140ce2c4677f56fc06692b182b8a07fcf..6b0ae0e41147a8a917cab35b4a6487af4fce6ead/compose/foundation).

**Bug Fixes**

- Fixed a bug causing a rare crash in text fields. ([I475c6](https://android-review.googlesource.com/#/q/I475c69d27d3a15ba36c13b47695086a4ec5841f2), [b/313010266](https://issuetracker.google.com/issues/313010266))
- Removed `ReusableContentHost` at the root of Lazy layout items. This was a potential root cause for "measure called on a deactivated node" crashes. ([Id6e60](https://android-review.googlesource.com/#/q/Id6e6087b1ac571d991de535d85c465936a3e4c1c))

### Version 1.7.3

October 2, 2024

`androidx.compose.foundation:foundation-*:1.7.3` is released. Version 1.7.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9..00e91ed140ce2c4677f56fc06692b182b8a07fcf/compose/foundation).

**Bug Fixes**

- Fixed a memory leak with `BasicText` when minLines is set to a non-default value.

### Version 1.7.2

September 18, 2024

`androidx.compose.foundation:foundation-*:1.7.2` is released. Version 1.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1efd0b233a17f707cd918993df1fa12e0bf9ae83..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/foundation).

**Bug Fixes**

- Fix issue with draggable that was missing down events which caused flings to look slower than normal.

### Version 1.7.1

September 10, 2024

- No changes to Android artifacts. `-desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts.

### Version 1.7.0

September 4, 2024

`androidx.compose.foundation:foundation-*:1.7.0` is released. Version 1.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d8995e2377dd4baad64b39becb6d480cadd05c86..38ffb9c315c3f894412184bda180c1b58b2a8556/compose/foundation).

**Important changes since 1.6.0**

- Performance of `Modifier.clickable`, `Modifier.focusable`, `Modifier.indication`, `Modifier.scrollable` and `Modifier.draggable` has been significantly improved. As a part of this effort, the following API changes were made in addition to internal changes
  - Added a new Indication API, `IndicationNodeFactory`. This leads to more performant Indication implementations compared to the previous (now deprecated) `rememberUpdatedInstance` API. For migration information, see [developer.android.com](http://developer.android.com/).
  - `clickable` / `combinedClickable` / `selectable` / `toggleable` now accepts a nullable `MutableInteractionSource` parameter. If null, and the provided Indication is an `IndicationNodeFactory`, the Indication can be lazily created only when needed, which improves performance. If you are not hoisting and using the `MutableInteractionSource`, it is recommended to pass null instead of passing `remember { MutableInteractionSource() }`.
  - `Indication#rememberUpdatedInstance` has been deprecated. It has a high unavoidable performance penalty, and prevents other optimizations. Instead, you should use the new `IndicationNodeFactory` API.
- `BasicTextField` using a [`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState) is now stable and we advise all call-sites to begin migration from `BasicTextField(value, onValueChange)` to `BasicTextField(TextFieldState)`.
- The `ClickableText` has been deprecated. To add clickable links to your text, use `BasicText` with the new [`LinkAnnotation`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/LinkAnnotation) annotation in your `AnnotatedString`. `LinkAnnotation` allows for custom styling based on link state (e.g. focused, hovered).
- Introducing `ContextualFlowRow` and `Enhanced FlowRow/Column` with `MaxLines` and `Overflow`. We are excited to announce enhancements to the experimental `FlowRow` and `FlowColumn`, now featuring `maxLines` and overflow support, alongside the debut of `ContextualFlowRow` and `ContextualFlowColumn`. This update is designed to provide performance optimal components, where `ContextualFlow*` is perfect for a large number of items making use of a small maxLines config and dynamic +N see more buttons, and `FlowRow` and `FlowColumn` is perfect for a small number of items, less than 100 items. Important: To maintain existing behavior in `FlowRow` or `FlowColumn` where all items are composed regardless of if they fit the cross axis max, set overflow to `FlowRowOverflow.Visible` or `FlowColumnOverflow.Visible` during initialization. Explore `ContextualFlowRowSample` and `FlowRowSample` for examples of these new features in action. ([Ib9135](https://android-review.googlesource.com/#/q/Ib913509969a79ff002eafb0075e6722a7a118531), [b/293577082](https://issuetracker.google.com/issues/293577082))
- Item appearance and disappearance animation support was added into `LazyColumn` and `LazyRow`. Previously it was possible to add `Modifier.animateItemPlacement()` modifier in order to support placement (reordering) animations. We deprecated this modifier and introduced a new non-experimental modifier called `Modifier.animateItem()` which allows you to support all three animation types: appearance (fade in), disappearance (fade out) and reordering. ([I2d7f7](https://android-review.googlesource.com/#/q/I2d7f7a376cea26c0a36a59a4586d2705ab04cab7), [b/150812265](https://issuetracker.google.com/issues/150812265))
- Implemented experimental support for long screenshots in Compose scroll containers using the official Android API (`ScrollCaptureCallback`).
- `NestedScroll` sources Drag and Fling are being replaced by `UserInput` and `SideEffect` to accommodate for the extended definition of these sources that now include animations (Side Effect) and Mouse Wheel and Keyboard (`UserInput`).
- `LazyLayout` prefetch requests can be marked as urgent now, meaning that we expect this item to be needed in the next frame and want to ignore frame budget to make sure to do more work in advance ([Id513f](https://android-review.googlesource.com/#/q/Id513f17517aa1b240e91afb3468837b12ed54da8))
- Support stylus handwriting feature on devices after Android U. ([I002e4](https://android-review.googlesource.com/#/q/I002e4f3218bb909833fcb92b8d1ff9b2153931d7))
- Various APIs have been promoted to stable
  - Pagers, snapping, window insets

### Version 1.7.0-rc01

August 21, 2024

`androidx.compose.foundation:foundation-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98bc1cf10201a973793b72d2ff1ae728070e47e4..d8995e2377dd4baad64b39becb6d480cadd05c86/compose/foundation).

**Bug Fixes**

- Fixed a regression where the crash occurred when any element is focused inside a parent that is focusable (or clickable) and disabled. ([b/317561689](https://issuetracker.google.com/issues/317561689))

### Version 1.7.0-beta07

August 7, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta07` is released. Version 1.7.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16151cbc8a68e976da6f2b0f624c2e9883c55aa3..98bc1cf10201a973793b72d2ff1ae728070e47e4/compose/foundation).

**Bug Fixes**

- Text input related `SemanticsNodeInteraction` functions `performTextReplacement`, `performTextInput`, and `performTextClearance` is now going to throw assertion errors when they are called on read only `TextFields`. ([I4ae8f](https://android-review.googlesource.com/#/q/I4ae8f255bd02f3b13af2a106340f49f5595a78a8))
- Fixed a visual glitch in hyperlinks. ([I23311](https://android-review.googlesource.com/#/q/I233110029159eb93c49cd24562387c3f868d9d89))
- Fixed `contentReceiver` modifier not working with some IMEs.
- Velocity generation: Prevent propagation of NaN values in Compose UI and Foundation.

### Version 1.7.0-beta06

July 24, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta06` is released. Version 1.7.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8346df8de9f86a546fc9c316113bd4a3cc82ede9..16151cbc8a68e976da6f2b0f624c2e9883c55aa3/compose/foundation).

### Version 1.7.0-beta05

July 10, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta05` is released. Version 1.7.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/487d2b07dba29c903cfd87a8dc7f99483084ebb6..8346df8de9f86a546fc9c316113bd4a3cc82ede9/compose/foundation).

**Bug Fixes**

- Fix for treatment of Nan values in `SnapFlingBehavior` and Pager.

### Version 1.7.0-beta04

June 26, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta04` is released. Version 1.7.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c29f7383c14ede0af9cb64be9f3eee63714bc73c..487d2b07dba29c903cfd87a8dc7f99483084ebb6/compose/foundation).

**Bug Fixes**

- Avoid crashes when measuring very large text lines (e.g. 10k characters) ([8157ab](https://android.googlesource.com/platform/frameworks/support/+/8157ab1cf5d805e9d626b17e710df49bd6e5d680))
- Fixes measurement of very large text causing crash in the new `BasicTextField` ([6b7575](https://android.googlesource.com/platform/frameworks/support/+/6b75757fbd5bd38f144b3126a4a1af49c0328430))
- Reverts a behavior change in Row/Column measurement that breaks Text usage in certain scenarios ([69e8ba](https://android.googlesource.com/platform/frameworks/support/+/69e8ba04943fb0ba364f1220f8c762163d001c00))

### Version 1.7.0-beta03

June 12, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta03` is released. Version 1.7.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a123f646cfea1599f9efead6da546b0c26063fa..c29f7383c14ede0af9cb64be9f3eee63714bc73c/compose/foundation).

### Version 1.7.0-beta02

May 29, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta02` is released. Version 1.7.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..1a123f646cfea1599f9efead6da546b0c26063fa/compose/foundation).

**API Changes**

- Adds an experimental API for configuring prefetch behavior of `LazyGrids` similar to the existing experimental API for `LazyLists`. This includes support for prefetching items in nested `LazyGrids`. Similiar to `LazyListPrefetchStrategy`, the implementation default is to prefetch the first 2 nested items of each grid, but this can be configured by the new `LazyGridPrefetchStrategy(nestedPrefetchItemCount)` and `LazyListPrefetchStrategy#onNestedPrefetch` APIs. ([I591c4](https://android-review.googlesource.com/#/q/I591c4e8959ba225b9e1817765c6e6bc10b7fac1a))
- Renamed `SemanticsProperties.Editable` to `IsEditable` and changes `SemanticsPropertyReceiver.editable` to a val `isEditable`. The property is now a boolean and always specified by text fields. ([I8acd8](https://android-review.googlesource.com/#/q/I8acd87bcdfc80b70de9665ba45708ca529ccdf69))
- Moved `basicMarquee` default values into `MarqueeDefaults` object. ([I12ff6](https://android-review.googlesource.com/#/q/I12ff617e3c8bddc43c3cc44d8be14926ac20378b))
- Renamed `basicMarquee` `delayMillis` parameter to `repeatDelayMillis`. ([I12ff6](https://android-review.googlesource.com/#/q/I12ff617e3c8bddc43c3cc44d8be14926ac20378b))
- Update API for styling the links: moved the `TextLinkStyles` to the `TextStyle` and removed the `TextDefaults` from material ([I5477b](https://android-review.googlesource.com/#/q/I5477bdb498b6b4f33ab3bc998e2be59d8a4ff7e4))

**Bug Fixes**

- Renamed `LayoutCoordinates.introducesFrameOfReference` to `LayoutCoordinates.introducesMotionFrameOfReference` to better reflect its purpose. Renamed related function to calculate coordinates based on that flag. ([I3a330](https://android-review.googlesource.com/#/q/I3a3301164ea2c08728b09faed6cf72ae089ead72))
- Removed 'Default' from the `MarqueeDefaults` properties. ([I1d8a0](https://android-review.googlesource.com/#/q/I1d8a0a53a7b74aa116a5595013a815a201f16c01))
- Removed 'Marquee' from `MarqueeDefaults` properties. ([Iad4f4](https://android-review.googlesource.com/#/q/Iad4f44b7803faf57f5a3a1445bfdbe94e4693d80))
- Removed `TextLinkStyles` from the `TextStyle` class. Instead, `TextLinkStyles` is part of the `LinkAnntation` constructor and the `AnnotatedString.fromHtml` method ([I90b2b](https://android-review.googlesource.com/#/q/I90b2b73e126d9c1106c223de823dda8babaf6708))
- Fixed a bug where Pager would snap when flinging towards a bound while already settled at the bound. ([I9f373](https://android-review.googlesource.com/#/q/I9f3730a6c168c19e077fd4d29325f444f54c1070), [b/339171222](https://issuetracker.google.com/issues/339171222))
- BTF2 now has correct mouse selection gestures. ([Ibe8c6](https://android-review.googlesource.com/#/q/Ibe8c678df325fd1cd55962ab023d8d3b40ab4aa3))

**External Contribution**

- Resubmit 'Make compose/measure time calculation content-type based in prefetch to improve accuracy' ([Iea622](https://android-review.googlesource.com/#/q/Iea6227ee19a6ef6ed4d6a09f8c28f3d012c5594c))
- Make compose/measure time calculation content-type based in prefetch to improve accuracy ([Ibccb1](https://android-review.googlesource.com/#/q/Ibccb1d3bfcc5c5409eea4ab47904f9f10e1f7fc5))
- Make `WindowInsetsPadding` modifiers available from common source set ([I070b2](https://android-review.googlesource.com/#/q/I070b2fbfc6dcae41be4bc9bf313d5847065d4053))

### Version 1.7.0-beta01

May 14, 2024

`androidx.compose.foundation:foundation-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/foundation).

**API Changes**

- Added `KeyboardOptions.shouldShowKeyboardOnFocus` property back as deprecated hidden for binary compatibility. ([I15cfe](https://android-review.googlesource.com/#/q/I15cfef582c07970eb66b28fdc1dd046692ee69aa))
- `Modifier.anchoredDraggable` now reverses drag deltas by default for components with a Horizontal orientation when used in an RTL layout. ([I3c6d9](https://android-review.googlesource.com/#/q/I3c6d950cedc30b1790e09e140d3d83d19a5d312b))
- `AnnotatedString.hasEqualsAnnotations` is now `hasEqualAnnotations`. ([I685c0](https://android-review.googlesource.com/#/q/I685c066bc518b511146443d67926462b341991b2))
- Updated the API for getting Material themed links in text. Specifically, removed the methods from the `TextDefaults` for constructing themed `LinkAnnotations` and parse HTML with themed links. Instead, added a `TextLinkStyles` class that allows to style the links as a parameter to the Text composable. ([I31b93](https://android-review.googlesource.com/#/q/I31b93f4460f4a0a50c7a86996a499d359ba455c8))
- Replaced `onDragStarted` and `onDragStopped` with non-suspend callbacks. ([I59de8](https://android-review.googlesource.com/#/q/I59de8c2b7adb0353420da1e7c8f3c9aa9d46f7e7))

**Bug Fixes**

- Fixed a bug where Pager would crash when the `contentPadding` was bigger than the incoming constraints. Pager now coerces negative values returned from `PageSize` to 0. ([Iba5d8](https://android-review.googlesource.com/#/q/Iba5d8eccddaf1a49bb09dc4f93d8a4f38276d60b), [b/314008560](https://issuetracker.google.com/issues/314008560))

### Version 1.7.0-alpha08

May 1, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha08` is released. Version 1.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7/compose/foundation).

**New Features**

- Added right-click context menu to `BasicTextField` and `SelectionContainer` with items for cut, copy, paste, and select-all actions. ([If8c93](https://android-review.googlesource.com/#/q/If8c9399d197d8c3c436ccca436e3ddfed3bc959e), [Ia2b49](https://android-review.googlesource.com/#/q/Ia2b4973e4535ff4c083a7ab39258bfcf9c6ae81e), [I6f268](https://android-review.googlesource.com/#/q/I6f268a534acee4fa8732b1058bc636a9ce6b1108))

**API Changes**

- `LazyLayout` prefetch requests can be marked as urgent now, meaning that we expect this item to be needed in the next frame and want to ignore frame budget to make sure to do more work in advance ([Id513f](https://android-review.googlesource.com/#/q/Id513f17517aa1b240e91afb3468837b12ed54da8))
- Renamed `isPositionedByParentWithDirectManipulation` to `introducesFrameOfReference`. Note that it now has the reverse effect, meaning that by default, most `LayoutCoordinates` introduce a frame of reference, and, only when placed under direct manipulation the property will be false. To query position with only those that introduce a frame of reference, use `positionInLocalFrameOfReference(...)`. Or `positionInLocalLookaheadFrameOfReference` from a `LookaheadScope`. ([Ifc5f7](https://android-review.googlesource.com/#/q/Ifc5f78c683543035e13ff727edf14a79075b1a84))
- Renamed `onClicked` to `onClick` inside `LinkInteractionListener` ([Iaa35c](https://android-review.googlesource.com/#/q/Iaa35cd1c54bdea113071a2eaf1e7d700e0eb5f19))
- Change action lambda for `getScrollViewportLength` as per API council feedback. ([Ibc74a](https://android-review.googlesource.com/#/q/Ibc74abf76a2d5d88f97b9c5853a3d3b2d58585b9))
- Renamed stylus handwriting delegation APIs. ([Ica45f](https://android-review.googlesource.com/#/q/Ica45f13c23a7bc0472bf10c99195e924ba3a32d7), [b/327271923](https://issuetracker.google.com/issues/327271923))
- Rename `TextInclusionStrategy.isInside` to `isIncluded`. Make `Paragraph/MultiParagraph#getRangeForRect()` return type non nullable. ([I51f26](https://android-review.googlesource.com/#/q/I51f269566495a3781946c8a72e6b615af2da57b9))

**Bug Fixes**

- Added "Select all" to all text contextual menus in `SelectionContainer`. ([Ib750e](https://android-review.googlesource.com/#/q/Ib750e9580a290c68356c02cc83bab4cc048e4cc8), [b/240143283](https://issuetracker.google.com/issues/240143283))
- Fixed long screenshot capture for scrolling containers with `reverseScrolling=true`. ([I7c59c](https://android-review.googlesource.com/#/q/I7c59cd9f43ca6968f3eefadbcfc7582c1aec51c7))
- Fixed an issue where `AnchoredDraggableState`'s `currentValue` would change when approaching the state's bounds. ([Iea30b](https://android-review.googlesource.com/#/q/Iea30b4ea0764f2cd817f4406011ab7b18b5e575a), [b/333846848](https://issuetracker.google.com/issues/333846848))

**External Contribution**

- Renamed `PrefetchExecutor` -\> `PrefetchScheduler` to better reflect its responsibilities. ([Ib9154](https://android-review.googlesource.com/#/q/Ib915439b1f029adfcfff0ee716b1ad5759f4a35d))
- Added support for prefetching items in nested `LazyLists` (e.g. a `LazyColumn` that renders nested `LazyRows`). This change is expected to reduce frame drops during scrolling for these `LazyLists`. The implementation default is to prefetch the first 2 nested items, however this behavior can be controlled by the new `LazyLayoutPrefetchStrategy(nestedPrefetchItemCount)` and `LazyListPrefetchStrategy#onNestedPrefetch` APIs. ([I51952](https://android-review.googlesource.com/#/q/I519526a694d8e9a89a1a040cd179d0416fa2d6d9))

### Version 1.7.0-alpha07

April 17, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha07` is released. Version 1.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/foundation).

**New Features**

- Added a `TextDefaults` object that contains methods to construct a `LinkAnnotation` and parse HTML-tagged string which apply `MaterialTheme` to the links. ([I98532](https://android-review.googlesource.com/#/q/I98532f3512d1930416f66dd195746eeeba884497), [b/139312671](https://issuetracker.google.com/issues/139312671))
- Item appearance and disappearance animation support was added into`LazyVerticalGrid` and `LazyHorizontalGrid`. Previously it was possible to add `Modifier.animateItemPlacement()` modifier in order to support placement (reordering) animations. We deprecated this modifier and introduced a new non-experimental modifier called `Modifier.animateItem()` which allows you to support all three animation types: appearance (fade in), disappearance (fade out) and reordering. ([Ib7d12](https://android-review.googlesource.com/#/q/Ib7d120e5dfec53dae00dc662e982dafeab1a6b0f), [b/330510929](https://issuetracker.google.com/issues/330510929))
- Item appearance and disappearance animation support was added into `LazyVerticalStaggeredGrid` and `LazyHorizontalStaggeredGrid`. Previously it was possible to add `Modifier.animateItemPlacement()` modifier in order to support placement (reordering) animations. We deprecated this modifier and introduced a new non-experimental modifier called `Modifier.animateItem()` which allows you to support all three animation types: appearance (fade in), disappearance (fade out) and reordering. ([I69bc9](https://android-review.googlesource.com/#/q/I69bc9cc1999c8b166e3ff6bb749bbb73a768bffe), [b/330511290](https://issuetracker.google.com/issues/330511290))

**API Changes**

- Adds `ContextMenuColors` and the associated `LocalContextMenuTheme` `ProvidableCompositionLocal`. The colors of the context menu on text fields and selectable text can be modified by providing the composition local. ([Ifa154](https://android-review.googlesource.com/#/q/Ifa154a761c372822bca1182023b70cb82b2a14b9))
- Text links got pressed state styling option in addition to normal styling, hovered and focused. ([I5f864](https://android-review.googlesource.com/#/q/I5f864b3fd1b1af6ff39dee03e1aa65ede7e16d32), [b/139312671](https://issuetracker.google.com/issues/139312671))
- Introduce `ViewConfiguration.HandwritingGestureLineMargin` for handwriting gestures. Support handwriting gesture for `BasicTextField`. ([Ie6e13](https://android-review.googlesource.com/#/q/Ie6e13b41cc82da1fd3c9ecc7ac34c3ff88dfa235), [b/325660505](https://issuetracker.google.com/issues/325660505))
- Removed `DelegatableNode.scrollIntoView` for the 1.7 release since we didn't have time to finish stabilizing the rest of the related API surface. This function will be re-introduced in 1.8 ([I6cf61](https://android-review.googlesource.com/#/q/I6cf6120f4cb0b4fbb4fbaff7bf57793b854da202), [b/333421581](https://issuetracker.google.com/issues/333421581), [b/332900232](https://issuetracker.google.com/issues/332900232))
- When querying Layout coordinates, you may now use the `excludeDirectManipulationOffset` argument to exclude the offset set by parent Layouts that placed their children using `Placeable.PlacementScope.withDirectManipulationPlacement`. Likewise, a Layout that changes the position of its children frequently may now place them using `withDirectManipulationPlacement` (such as Scroll, implemented by default). This helps `approachLayout` based animations to be more intuitive, having now the opportunity to differentiate what offset to animate, and what to apply directly when deciding to animate their approach. ([I60ec7](https://android-review.googlesource.com/#/q/I60ec77cec9d448ffdfed8b661ba2e433f3adaa55))
- Introduce `requestScrollToItem` for `LazyStaggeredGrid`. For each measure-pass, the client may now opt-out of maintaining index based on the key by calling `requestScrollToItem`. This does not change existing behavior in any way unless `requestScrollToItem` is called. ([I63983](https://android-review.googlesource.com/#/q/I63983a31730ea445dc4a1839f8a0afa9d2f8ee80))
- Introduce `requestScrollToPage` in Pager. For each measure-pass, the client may now opt-out of maintaining index based on the key by calling `requestScrollToPage`. This does not change existing behavior in any way unless `requestScrollToPage` is called. ([Ic4213](https://android-review.googlesource.com/#/q/Ic4213b831da197ac47c01ce26260cc147d797787))
- Introduced `requestScrollToItem` for `LazyGrids`. For each measure-pass, the client may now opt-out of maintaining index based on the key by calling `requestScrollToItem`. This does not change existing behavior in any way unless `requestScrollToItem` is called. ([I0a7a0](https://android-review.googlesource.com/#/q/I0a7a06d25850d4ff11b782568bc42e6724b3c862))
- `ClickableText` is marked as deprecated. To add links to the text, create an `AnnotatedString` with a `LinkAnnotation` corresponding to your link and pass this `AnnotatedString` to the `Text` composable ([I34d4b](https://android-review.googlesource.com/#/q/I34d4bf29a9386820f8582765e62576a5fcfcd3c6), [b/323346994](https://issuetracker.google.com/issues/323346994))
- `UrlAnnotation` is deprecated, use `LinkAnnotation.Url` instead. If you're using Material theming, then use `TextDefaults` object to create the annotation with Material theming applied to it ([I8d180](https://android-review.googlesource.com/#/q/I8d18033220b74bb84f74380855ef5efb5e3e92bb), [b/323346545](https://issuetracker.google.com/issues/323346545))
- `String.parseAsHtml` renamed to `AnnotatedString.Companion.fromHtml` ([I43dcd](https://android-review.googlesource.com/#/q/I43dcd5b6f6ddc634879f5747df4b911953f84632))
- Added styling arguments (`linkStyle`, `focusedLinkStyle`, `hoveredLinkStyle`) and a link interaction listener to the `parseAsHtml` method. When parsing the HTML-tagged string with `<a>` tags, the method will construct a `LinkAnnotation.Url` for each such tag and pass the styling objects and link interaction listener to each annotation. ([I7c977](https://android-review.googlesource.com/#/q/I7c9777a340e04ccf4dc10258c83d18e69831b3c6))
- `LinkAnnotation` now takes the state-based styling arguments and a `LinkInteractionListener`. Add this annotation to the `AnnotatedString` to get a hyperlink. By passing `focusedState` and/or `hoveredState` you can define the visual configuration for links when they are focused and/or hovered. ([I81ce4](https://android-review.googlesource.com/#/q/I81ce4350b8a1e37881000fd82f081b7afb8e0f42), [b/139312671](https://issuetracker.google.com/issues/139312671))
- The feature flag for long screenshots has been removed. ([I28648](https://android-review.googlesource.com/#/q/I28648d10fcd1293913a289ea21e64611248693a6), [b/329128246](https://issuetracker.google.com/issues/329128246))
- `LazyColumn` will now render sticky headers correctly in long screenshots. ([I8d239](https://android-review.googlesource.com/#/q/I8d239dddc5301c16a76b348edfab482adcdd157d), [b/329296635](https://issuetracker.google.com/issues/329296635))
- Stabilized majority of the remaining experimental APIs that were introduced with the new `BasicTextField`. ([I714e2](https://android-review.googlesource.com/#/q/I714e2dec19b189e9b74411fefbd636a8cc8e60d1))
- Added `textObfuscationCharacter` parameter to `BasicSecureTextField` that controls which character to use while obfuscating the contents. ([I0588b](https://android-review.googlesource.com/#/q/I0588b5b978e74feb4a473b24bab3792281998114))
- `NestedScroll` sources Drag and Fling are being replaced by `UserInput` and `SideEffect` to accommodate for the extended definition of these sources that now include animations (Side Effect) and Mouse Wheel and Keyboard (`UserInput`). ([I40579](https://android-review.googlesource.com/#/q/I40579c9b053d6bcf477191b212c7a72876a588b7))
- Introduce `LocalBringIntoViewSpec`, a platform dependent focus scrolling behavior that is applied at the Scrollable modifier layer. ([I27aa5](https://android-review.googlesource.com/#/q/I27aa527cf8088eb3295f97da7501c76e4c4456f4), [b/317453911](https://issuetracker.google.com/issues/317453911))
- Removed `TextFieldCharSequence`. `TextFieldBuffer.originalValues` is replaced with `TextFieldBuffer.originalText` and `TextFieldBuffer.originalSelection`. ([I2c7d6](https://android-review.googlesource.com/#/q/I2c7d6d00ddd9a6412ed97f4ec893f97b0e2342c9))
- `ImeOptions.hintLocales` is no longer nullable. If you want to pass an empty Locale list, please use `LocaleList.Empty`. ([Ic5bc4](https://android-review.googlesource.com/#/q/Ic5bc4e784d61b40ebc69778758515eb240c01e20))
- Renamed `getOffsetFractionForPage` to `getOffsetDistanceInPages`. ([Ia05e2](https://android-review.googlesource.com/#/q/Ia05e2e47d2d1372e099766bbe337d64e9c374b58))

**Bug Fixes**

- When `InputTransformations` are joined with `next`, their `KeyboardOptions` are now properly merged by individual options using the new `KeyboardOptions.merge` method. ([Ie5304](https://android-review.googlesource.com/#/q/Ie530405a5d45080f3907d65345f988108515adb4), [b/295951492](https://issuetracker.google.com/issues/295951492))
- `AnchoredDraggableState`'s `targetValue` now does *not* consider positional thresholds anymore. It now has an implicit threshold of 50%, meaning that the `targetValue` changes at the midpoint between two anchors. ([I82c2c](https://android-review.googlesource.com/#/q/I82c2c160f078ebdee15c74e0b0016ed60446cc94))

**External Contribution**

- Renamed 2 scroll APIs ([I56a75](https://android-review.googlesource.com/#/q/I56a75db3b76a9b31b58f66872b5b49ae1d907e69))

### Version 1.7.0-alpha06

April 3, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha06` is released. Version 1.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/foundation).

**New Features**

- Item appearance and disappearance animation support was added into `LazyColumn` and `LazyRow`. Previously it was possible to add `Modifier.animateItemPlacement()` modifier in order to support placement (reordering) animations. We deprecated this modifier and introduced a new non-experimental modifier called `Modifier.animateItem()` which allows you to support all three animation types: appearance (fade in), disappearance (fade out) and reordering. ([I2d7f7](https://android-review.googlesource.com/#/q/I2d7f7a376cea26c0a36a59a4586d2705ab04cab7), [b/150812265](https://issuetracker.google.com/issues/150812265))
- Clients of `LazyColumn/LazyRow`may now opt-out of maintaining an index based on the key for the upcoming measure-pass by calling a non-suspend `LazyListState.requestToScroll`. ([I98036](https://android-review.googlesource.com/#/q/I98036297fdf1bdf73125c6713fe746d71d6d94a8), [b/209652366](https://issuetracker.google.com/issues/209652366))
- Added `parseAsHtml` method for styled strings: it allows to convert a string marked with HTML tags into `AnnotatedString`. Note that not all tags are supported, for example you won't be able to display bullet lists yet. ([I84d3d](https://android-review.googlesource.com/#/q/I84d3d1881805e964cea940eb1c68a5bba16f6416))
- Implemented experimental support for long screenshots in Compose scroll containers using the official Android API (`ScrollCaptureCallback`). This feature is experimental and may not currently handle all cases correctly. For that reason it is currently disabled by default. To opt-in, set the `ComposeFeatureFlag_LongScreenshotsEnabled` flag to true. This flag will be removed before 1.7 beta. ([I2b055](https://android-review.googlesource.com/#/q/I2b0552d34c530b127d64ac58f48a0fa399b3edde), [b/329296471](https://issuetracker.google.com/issues/329296471))
- Introduce new `GraphicsLayer` API to provide more flexibility in placement and rendering of `GraphicsLayer` instances and support intrinsic rendering features without needing to coordinate with Composable implementations to specify `GraphicsLayer` modifier instances.

**API Changes**

- All `KeyboardOptions` parameters now have an unspecified value by default. Added `KeyboardOptions.merge` method.
- Renamed `KeyboardOptions.autoCorrect` to `autoCorrectEnabled` and made it nullable, where null indicates no value was specified. ([Ia8ba0](https://android-review.googlesource.com/#/q/Ia8ba0fb1235a7a1c6c42d140119ddcb40b65892d), [b/295951492](https://issuetracker.google.com/issues/295951492))
- Renamed `outOfBoundsPageCount` to `beyondViewportPageCount`. ([I129c6](https://android-review.googlesource.com/#/q/I129c68df1d82f992e102b4141427c0b425b38799))
- `fun ClipEntry.getMetadata()` is changed to `val ClipEntry.clipMetadata`. ([I50155](https://android-review.googlesource.com/#/q/I50155cef29574f74be45e850d210d0c405aa69f5))
- Removed `TextFieldState.valueAsFlow()`. Prefer using `snapshotFlow { state.text }`, or `snapshotFlow { TextFieldCharSequence(state.text, state.selection) }` ([I7d629](https://android-review.googlesource.com/#/q/I7d629547848fe91ac6127b83c2836fe4c358c1ef))
- Reorganized `InputTransformation.transformInput` parameters. Removed `originalValue: TextFieldCharSequence`. Instead `TextFieldBuffer` now carries this value with the same name. Also removed the `valueWithChanges: TextFieldBuffer` parameter. `TextFieldBuffer` now is the receiver scope on the function. ([I919cc](https://android-review.googlesource.com/#/q/I919cc112d32cc821ee5beb7d90888020a060e024))
- `BasicTextField(state)` variant and `BasicSecureTextField` now use `KeyboardActionHandler` instead of `KeyboardActions` to process actions taken by the software keyboard. ([I58dda](https://android-review.googlesource.com/#/q/I58dda71cd89a62a1fa34df44a40f7bc0e7384991))
- Stylus handwriting delegation APIs to support stylus handwriting on "fake" text input fields. ([I9c09c](https://android-review.googlesource.com/#/q/I9c09c7c66896625e812674f262eceeb00938d983), [b/327271923](https://issuetracker.google.com/issues/327271923))
- Renamed `KeyboardOptions.shouldShowKeyboardOnFocus` to `showKeyboardOnFocus`. ([Ib4b7a](https://android-review.googlesource.com/#/q/Ib4b7af571c6bdfb06c3b0e160482cbb62c5277fa), [b/295951492](https://issuetracker.google.com/issues/295951492))
- Removed `hintMediaTypes` parameter from `Modifier.contentReceiver`. Developers were already encouraged to check the received `TransferableContent`'s media type since it could be incompatible with the configured `hintMediaTypes`. ([I82f99](https://android-review.googlesource.com/#/q/I82f995187934e7d62ff2c6312869964ba7ca3b6a))
- Reordered the parameters of `BasicSecureTextField`. Removed `keyboardType` and `imeAction` parameters in favor of full `KeyboardOptions` class while keeping the same defaults appropriate for `BasicSecureTextField`. Also removed the `scrollState` parameter. ([Ibbfa9](https://android-review.googlesource.com/#/q/Ibbfa90ce45ab4e5ef7e4e38aed293d8f831af674))
- `TextFieldState.text`'s type is changed from `TextFieldCharSequence` to just `CharSequence`. Therefore, added `TextFieldState.selection: TextRange` and `TextFieldState.composition: TextRange?` to read the current selection and composition values directly from the state object.
- Removed `TextFieldState.forEachTextValue`. ([Idb2a2](https://android-review.googlesource.com/#/q/Idb2a216a1866957e336c12ad6ee0c1338f0f530d))
- Removed `ClipboardManager.getClipMetadata` and `ClipboardManager.hasClip` functions. Please use `clipEntry.getMetadata()` to read the current clip entry's metadata. Also check `ClipboardManager.getClip`'s result if it's null or not to understand whether Clipboard has a current clip. ([I50498](https://android-review.googlesource.com/#/q/I504988d835b71009609c01919b387239a1e2bee0))
- `ClipboardManager.setClip` now accepts null to be able to clear the Clipboard. ([I7d2e9](https://android-review.googlesource.com/#/q/I7d2e957005fb2efecc64b7273d8209161016b36a))
- `ReceiveContentListener` is converted to a function interface. Also `Modifier.receiveContent` overload that takes in a lambda is removed since `ReceiveContentListener` is a function interface now.
- `Modifier.receiveContent` is renamed to `Modifier.contentReceiver`. ([I1e6af](https://android-review.googlesource.com/#/q/I1e6affb8908f738c0a27f57f67479bf7ee091a7e))
- Renamed `TransferableContent.consumeEach` to `TransferableContent.consume`. ([I1e462](https://android-review.googlesource.com/#/q/I1e462742e827d84c9dec6e8184a9a2f9acb84540))
- `rememberTextFieldState` has graduated to a Stable API. ([I37999](https://android-review.googlesource.com/#/q/I3799979f1211c2182f32e45af82be5d13e181f3d))

**Bug Fixes**

- Fixed a bug where `BasicTextField(state)` variant did not work with CJK(composition based) keyboards. ([I54425](https://android-review.googlesource.com/#/q/I544255c03179f59e86974710d59308cfea48b036))
- Fixed a bug where `Modifier.dragAndDropTarget()` could reference stale data in certain scenarios with `Modifier.Node` re-use. ([I05bb1](https://android-review.googlesource.com/#/q/I05bb1a7dea19acf4234f88fe988f51e3c2822f4b))
- Reverted a recent contract change where `AnchoredDraggableState#anchoredDrag` calls would snap at the end of an `anchoredDrag` operation. ([I95715](https://android-review.googlesource.com/#/q/I9571542e53b0bd026e6bcb8ca6abead58ca4a4ae))

### Version 1.7.0-alpha05

March 20, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha05` is released. Version 1.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/foundation).

**API Changes**

- Removed experimental `LocalTextLinkStyle` composition local for styling hyperlinks. ([Iebfa7](https://android-review.googlesource.com/#/q/Iebfa7af5ec45e276de9b57191400e37638e2997f))
- Removed experimental override of `BasicText` with `onLinkClicked` argument. A replacement API for hyperlinks support will follow in the future. ([I107d5](https://android-review.googlesource.com/#/q/I107d5d08153db444fac816ad7c9c65057d931a81))
- Removed Codepoints related methods and properties under `TextFieldState` and `TextFieldBuffer`. Also removed the `inChars` suffixes from the remaining selection and composition related APIs. ([Ief7ce](https://android-review.googlesource.com/#/q/Ief7ce54a84a9276d79b1e5bed50801b7d9b9b524))
- `AnchoredDraggable`'s `currentValue` will now update when passing through an anchor point. Use `settledValue` to receive the previous `currentValue` semantics, only updating when settling at an anchor. The progress is now exposed as a function (requiring a starting and end point) instead of a property. ([Ibe6e8](https://android-review.googlesource.com/#/q/Ibe6e88f172b099e8f1f841722946471e4641f999), [b/318707189](https://issuetracker.google.com/issues/318707189), [b/298271489](https://issuetracker.google.com/issues/298271489), [b/294991954](https://issuetracker.google.com/issues/294991954))
- `BasicTextField(state)`, `TextFieldState`, `InputTransformation`, `OutputTransformation`, `TextFieldLineLimits`, `TextFieldDecorator` are graduated to stable. ([I9582b](https://android-review.googlesource.com/#/q/I9582b7fab87b79a08f617122ed7bd1d2c5b61b9a))
- Introduced `InterceptPlatformTextInput` for helping write low-level IME-related tests and other low-level IME use cases. `PlatformTextInputTestOverride` has been deprecated. ([I862ed](https://android-review.googlesource.com/#/q/I862ed2e997d6a98e33a25da2ff536a2779ae173d), [b/322680547](https://issuetracker.google.com/issues/322680547))
- Split `restrictedConstraints()` to two methods: `fitPrioritizingWidth()` and `fitPrioritizingHeight()` ([I6d7fd](https://android-review.googlesource.com/#/q/I6d7fd3811fffff13b3343c5365290e73cb151bcb))

**External Contribution**

- Added 2 new API `isLastScrollForward`/`isLastScrollBackward` to check scroll direction for latest scroll action, return false if no scroll action yet. ([I63a0e](https://android-review.googlesource.com/#/q/I63a0e2181d19fdbb945ff1f71781b44559923537))

### Version 1.7.0-alpha04

March 6, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha04` is released. Version 1.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/foundation).

**API Changes**

- Support stylus handwriting feature on devices after Android U. ([I002e4](https://android-review.googlesource.com/#/q/I002e4f3218bb909833fcb92b8d1ff9b2153931d7))
- Added `hintLocales` to `KeyboardOptions` to provide `TextFields` with the ability to hint IMEs with specific locales to preset a preferred language. ([Id18c2](https://android-review.googlesource.com/#/q/Id18c27ef6047856a416e98c899674e2b5295e939))
- Removed the Experimental `BasicTextField2` and `BasicSecureTextField` overloads that took `value: String` and `onValueChange: () -> String` parameters. ([I568b4](https://android-review.googlesource.com/#/q/I568b4fc59c404938cf38f45e0f8ba1f2b35e8fc1))
- Add an optional `applySemantics` function to `InputTransformation` to influence the semantics of the `BasicTextField2` that it's applied to. ([I74a2f](https://android-review.googlesource.com/#/q/I74a2f4db178fe2660862749f10367bac57761ae9), [b/170648072](https://issuetracker.google.com/issues/170648072))
- In this CL we are adding the `GetScrollViewportLength` semantic action so we can pipe up information about the components being scrolled in compose to the a11y system. This CL also applies the usage of said property in Foundation Scrollable Lists. ([Ic5fa2](https://android-review.googlesource.com/#/q/Ic5fa297df4613636529e12037a0b7d03bcacc534))
- `BasicTextField2` is renamed to `BasicTextField`. ([Ie5713](https://android-review.googlesource.com/#/q/Ie5713a5542fa0980aefc5a15b41c9ba8f777b277))
- `FocusRequester.createRefs` is now stable ([I4d92c](https://android-review.googlesource.com/#/q/I4d92c644c57436fcd4883bc73fe0120ffa0a6fb2), [b/261436820](https://issuetracker.google.com/issues/261436820))
- Introduced `DelegatableNode.scrollIntoView()` to allow modifier nodes to make `scrollIntoView` requests directly. ([I2b3b7](https://android-review.googlesource.com/#/q/I2b3b7b59a4906f213ae161c531d5af667b4049c7), [b/299939840](https://issuetracker.google.com/issues/299939840))
- Introduced `DelegatableNode.requireView()` to allow modifier nodes to get the current Android `View` without reading a composition local. ([I40768](https://android-review.googlesource.com/#/q/I407682883cafa8315d1ede370288afdaf62d97a4))
- Introducing contextual layout information within Contextual Flow Row Scope and Contextual Flow Column Scope, featuring line index, position, and constraints on maximum width and height to stay in specified position. Items exceeding maximum width/height may flow to the next line or be omitted based on overflow settings. ([Id13f8](https://android-review.googlesource.com/#/q/Id13f86913c1c7a2c87c2980d451374db187e83ae), [b/292114798](https://issuetracker.google.com/issues/292114798))

**Bug Fixes**

- Fixed a bug where in certain conditions toggling `enabled` or `readOnly` attributes of `TextField` would cause a crash. ([Iae17b](https://android-review.googlesource.com/#/q/Iae17bf3ac4f0da228413f4f3efbed729e0621a6d))

### Version 1.7.0-alpha03

February 21, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/foundation)

**API Changes**

- Introduced `DelegatableNode.requireLayoutCoordinates()` as a way to get a `Modifier.Node`'s current `LayoutCoordinates` without needing to override `onPlaced` and store the coordinates in a property yourself. ([Ia8657](https://android-review.googlesource.com/#/q/Ia86579f48f389b7bc8d8a8be25602edfded6160c))
- Introduced `DelegatableNode.currentLayoutCoordinates` as a way to get a `Modifier.Node`'s current `LayoutCoordinates` without needing to override `onPlaced` and store the coordinates in a property yourself. ([Iaebaa](https://android-review.googlesource.com/#/q/Iaebaa704ca29bb366bea5f85958fc4ddaae8be2f))
- Performance optimizations in `DraggableAnchors` used by `AnchoredDraggable`. ([I89cff](https://android-review.googlesource.com/#/q/I89cffe9b91f9559d0295b064e7237d68393023a2))
- `BasicTextField2` and related APIs under `androidx.compose.foundation.text2` package are moved to `androidx.compose.foundation.text`. ([I9f635](https://android-review.googlesource.com/#/q/I9f6355e98b573d8985af9ec5135634da58bcc597))
- `BasicTextField2` no longer accepts a `CodepointTransformation` parameter. Use `BasicSecureTextField` or `OutputTransformation`. ([Id34ff](https://android-review.googlesource.com/#/q/Id34ffdd13deb8079fcc678cc519511fe9d1c97a5))
- Added method to compare only the annotations of two `AnnotatedStrings`. ([I32659](https://android-review.googlesource.com/#/q/I3265940a29ab587c50c96bfcbeb35590cad48100))
- Introducing `ContextualFlowRow` and Enhanced `FlowRow`/`Column` with `MaxLines` and `Overflow`. We are excited to announce enhancements to the experimental `FlowRow` and `FlowColumn`, now featuring `maxLines` and overflow support, alongside the debut of `ContextualFlowRow` and `ContextualFlowColumn`. This update is designed to provide performance optimal components, where `ContextualFlow*` is perfect for a large number of items making use of a small `maxLines` config and dynamic +N see more buttons, and `FlowRow` and `FlowColumn` is perfect for a small number of items, less than 100 items. Important: To maintain existing behavior in `FlowRow` or `FlowColumn` where all items are composed regardless of if they fit the cross axis max, set `overflow` to `FlowRowOverflow.Visible` or `FlowColumnOverflow.Visible` during initialization. Explore `ContextualFlowRowSample` and `FlowRowSample` for examples of these new features in action. ([Ib9135](https://android-review.googlesource.com/#/q/Ib913509969a79ff002eafb0075e6722a7a118531), [b/293577082](https://issuetracker.google.com/issues/293577082))

**Bug Fixes**

- Cursor animation no longer requests frames between on and off states. ([Ia2253](https://android-review.googlesource.com/#/q/Ia22537827b1735a0c2f6f5c732bebf79aaa3b773))
- `KeyboardOptions`' deprecated copy constructors will now correctly copy all properties. ([If12de](https://android-review.googlesource.com/#/q/If12deae291313795562ab37f59afe4255012960e))

### Version 1.7.0-alpha02

February 7, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/foundation)

**API Changes**

- `HorizontalPager`, `VerticalPager` and `PagerState` are promoted to stable. ([I67660](https://android-review.googlesource.com/#/q/I67660aa3cc1d44ae3dae5b002bae4459a1b25ae3), [b/316966909](https://issuetracker.google.com/issues/316966909))
- Added `LocalTextLinkStyle` composition local that allows to change the style of the links in Text across the app. If you're using your own theme in the app, you should be setting this composition local according to your theming. When using Material theme the color of the link by default will be set to Material's primary color. ([I7eb10](https://android-review.googlesource.com/#/q/I7eb10b55fcec1b268c60744de700058eb11a385a))
- Introduced `receiveContent` modifier that provides developers with a way to [receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content) in Jetpack Compose.
- `receiveContent` integrates with `BasicTextField2` to accept rich content provided by the software keyboard, or via Clipboard paste action. ([I81b72](https://android-review.googlesource.com/#/q/I81b72a6f0e851618fdd7346d9b1b7a8cf4e3ec3e))
- In this change we're replacing `SnapFlingBehavior` with `TargetedFlingBehavior` in pager to unlock other use cases and provide greater flexibility. ([I762ea](https://android-review.googlesource.com/#/q/I762eac32d9f1f1545efa8d8eb79ceb97833a77ed))
- In this change we're making Snapping APIs Stable. We're also cleaning up some of the testing code and adding more samples to Snapping. ([Id8da9](https://android-review.googlesource.com/#/q/Id8da9bf3d268eae6a5a7372170c6122d7adaea1e))
- Introduce `TargetedFlingBehavior`, a `FlingBehavior` that allows propagating information about the state of the ongoing animation and it's target scroll offset. ([I6a207](https://android-review.googlesource.com/#/q/I6a2070d346b92d9cfa6e9bb5d2315c4a521dbb79))

**Bug Fixes**

- `BasicTextField2` now keeps the cursor in view while typing when it has been scrolled out of view or would move out of view due to input. ([Ieb856](https://android-review.googlesource.com/#/q/Ieb85691dd1a7cf98ab5fc188721d4e4475aec762), [b/237190748](https://issuetracker.google.com/issues/237190748))

**External Contribution**

- Adds an experimental API for configuring prefetch behavior of LazyLists. ([I022a4](https://android-review.googlesource.com/#/q/I022a469c6d89d8742511cf10715afeced732d27e))

### Version 1.7.0-alpha01

January 24, 2024

`androidx.compose.foundation:foundation-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f/compose/foundation)

**New Features**

- Added a new `Indication API`, `IndicationNodeFactory`. This leads to more performant `Indication` implementations compared to the previous (now deprecated) `rememberUpdatedInstance` API. For migration information, see [developer.android.com](http://developer.android.com).
- `clickable / combinedClickable / selectable / toggleable` now accepts a nullable `MutableInteractionSource` parameter. If null, and the provided `Indication` is an `IndicationNodeFactory`, the `Indication` can be lazily created only when needed, which improves performance. If you are not hoisting and using the `MutableInteractionSource`, it is recommended to pass null.

**API Changes**

- Introduce `DecayAnimation` in `AnchoredDraggable`, this change adds a `decayAnimationSpec` parameter to `AnchoredDraggable` allowing to use decay animation when settling to one of the anchors. The change also includes renaming the existing `animationSpec` to `snapAnimationSpec` to help understanding the use case of each spec.
- `BasicTextField2` is available for experimental use. It should be roughly at feature parity with `BasicTextField`, and behavior should be production-ready. However, the API remains experimental for now. Before stabilizing, it will be renamed to `BasicTextField` and moved into the same package.
- Introduced the first draft of the `OutputTransformation` API for `BasicTextField2`. This API replaces most of the use cases of `VisualTransformation` in the old `BasicTextField`. However it is not complete yet, and some things won't work correctly, but we'd appreciate any feedback on the API usability for your use cases. ([aosp/2708848](https://r.android.com/2708848))
- Introduced `LinkAnnotation` that allows to add links and clickables into text. Links feature is not complete yet and more API changes are coming.
- Introduced `receiveContent` modifier that provides developers with a way to [receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content) in Jetpack Compose.
- `receiveContent` integrates with `BasicTextField2` to accept rich content provided by the software keyboard, or via paste from Clipboard.
- `KeyboardOptions.shouldShowKeyboardOnFocus` allows you to disable the default behavior of `BasicTextField` of requesting a software keyboard on focus.
- `TextInputService` and `LocalTextInputService` are now deprecated. Use `PlatformTextInputModifierNode` to integrate directly with platform IME APIs instead. ([aosp/2862698](https://r.android.com/2862698))
- `Indication#rememberUpdatedInstance` has been deprecated. It has a high unavoidable performance penalty, and prevents other optimizations. Instead, you should use the new `IndicationNodeFactory` API.

**Bug Fixes**

- `BasicTextField` will now pre-validate a small selection of offset mappings when `VisualTransformation` is passed. This helps catch common coding errors that lead to unrecoverable exceptions in later measure or draw passes. By throwing during composition, it is more likely developers will see these errors during development helping avoid production crashes. ([I0fd42](https://android.googlesource.com/c/platform/frameworks/support/+/290461))
- `VisualTransformation` will not throw if you return an invalid index for an invalid index ([b/316401857](http://b/316401857))

## Version 1.6

### Version 1.6.8

June 12, 2024

`androidx.compose.foundation:foundation-*:1.6.8` is released. Version 1.6.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a13a0e3b1197d66bfc19b9051576bc705f2c337..9dbbab668fd22cd643de4651197354a828aaa7b9/compose/foundation).

### Version 1.6.7

May 1, 2024

`androidx.compose.foundation:foundation-*:1.6.7` is released. Version 1.6.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b..9a13a0e3b1197d66bfc19b9051576bc705f2c337/compose/foundation).

### Version 1.6.6

April 17, 2024

`androidx.compose.foundation:foundation-*:1.6.6` is released. Version 1.6.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/917ada96acf0ac343128c3f4af9bd67a4b80b99c..a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b/compose/foundation).

**Bug Fixes**

- Fixed a bug where in certain conditions toggling `enabled` or `readOnly` attributes of `TextField` would cause a crash. ([Iae17b](https://android-review.googlesource.com/#/q/Iae17bf3ac4f0da228413f4f3efbed729e0621a6d))

### Version 1.6.5

April 3, 2024

`androidx.compose.foundation:foundation-*:1.6.5` is released. Version 1.6.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3..917ada96acf0ac343128c3f4af9bd67a4b80b99c/compose/foundation).

**Bug Fixes**

- Adds debugging logs to hard-to-reproduce bugs in Row/Column: ([b/300280216](https://issuetracker.google.com/issues/300280216) and [b/297974033](https://issuetracker.google.com/issues/297974033))

### Version 1.6.4

March 20, 2024

`androidx.compose.foundation:foundation-*:1.6.4` is released. Version 1.6.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/22b329dfa8888198eb3024650d236b3afe6c0907..1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3/compose/foundation).

**Bug Fixes**

- A long-press-then-drag selection gesture which moves out of the text's layout bounds in the first frame of the drag no longer crashes. ([Icdf90](https://android-review.googlesource.com/#/q/Icdf907784adf27d418cd140864c1778dd73a9ec5), [b/325307463](https://issuetracker.google.com/issues/325307463))

### Version 1.6.3

March 6, 2024

`androidx.compose.foundation:foundation-*:1.6.3` is released. Version 1.6.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af119e2e31de85654fb7b2e5a2c7e724231131fd..22b329dfa8888198eb3024650d236b3afe6c0907/compose/foundation).

### Version 1.6.2

February 21, 2024

`androidx.compose.foundation:foundation-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f639ccf09a84fa5af4a9016fa239539aeed40b94..af119e2e31de85654fb7b2e5a2c7e724231131fd/compose/foundation)

**Bug Fixes**

- Fix `AnimateContentSize` not resetting properly. ([I07051](https://android-review.googlesource.com/c/platform/frameworks/support/+/2933952))
- Fix issue where `intrinsicHeight` of text would be over-cached in some circumstances. ([3cd398](https://android.googlesource.com/platform/frameworks/support/+/3cd398c1ce0d79dab4738f00a6998f05d039801b), [b/217910352](https://issuetracker.google.com/issues/217910352))

### Version 1.6.1

February 7, 2024

`androidx.compose.foundation:foundation-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..f639ccf09a84fa5af4a9016fa239539aeed40b94/compose/foundation)

**Bug Fixes**

- Fix staggered grid measure when scrolled over limit. ([bffc39](https://android.googlesource.com/platform/frameworks/support/+/bffc39c4b6a48e9763d9176a513db9667f5185eb))
- Add check for layout with large dimensions. ([e74af5](https://android.googlesource.com/platform/frameworks/support/+/e74af5db9d9f23e962b70a70b702c7b8ab60dcc1))
- Fix placement of 0-sized items at the start of the staggered grid. ([785f94](https://android.googlesource.com/platform/frameworks/support/+/785f94541e8d67ec374eb0554c8baca2c067fb1b))
- Call onRelease callback in the same order as onForgotten. ([31ce3b](https://android.googlesource.com/platform/frameworks/support/+/31ce3be612d118cbe53543f5af8965a665e5f7d9))

### Version 1.6.0

January 24, 2024

`androidx.compose.foundation:foundation-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/296c44d6ba03d2167bdea85d53e8387d7b1644f9..4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf/compose/foundation)

**Important changes since 1.5.0**

- New Modifier `Modifier.anchoredDraggable` that unlocks the ability to drag and animate between predefined set of anchors. This modifier is intended to be a replacement for `Modifier.swipeable`. Learn how to use it and migrate from `Modifier.swipeable` in the [migration guide](https://developer.android.com/jetpack/compose/touch-input/pointer-input/migrate-swipeable).
- Drag and drop functionality between apps and components has been added. Refer to [`DragAndDropTarget`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draganddrop/DragAndDropTarget), [`Modifier.dragAndDropSource`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/package-summary#(androidx.compose.ui.Modifier).dragAndDropSource(kotlin.coroutines.SuspendFunction1)) and other APIs to get started
- `Modifier.draggable2D` is the new modifier that allows for easy 2d dragging support. See [Sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/samples/src/main/java/androidx/compose/foundation/samples/Draggable2DSamples.kt).
- [`AndroidExternalSurface`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#AndroidExternalSurface(androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.unit.IntSize,androidx.compose.foundation.AndroidExternalSurfaceZOrder,kotlin.Boolean,kotlin.Function1)) and [`AndroidEmbeddedExternalSurface`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#AndroidEmbeddedExternalSurface(androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.unit.IntSize,androidx.compose.ui.graphics.Matrix,kotlin.Function1)) have been added to make it easier to add surface-driven components in compose
- Various API changes and improvements in `Pager` and `snapFlingBehaviour`
- Various focus, text and insets APIs have been promoted to stable APIs

### Version 1.6.0-rc01

January 10, 2024

`androidx.compose.foundation:foundation-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc038a4bc84de9ab20493d6efa8d26f4a70214ae..296c44d6ba03d2167bdea85d53e8387d7b1644f9/compose/foundation)

**API Changes**

- The `DragAndDropTarget()` extension constructor has been removed. Create a new instance using `object: DragAndDropTarget {}`. ([I32318](https://android-review.googlesource.com/#/q/I323182a88276948803412494d5d24aefd23db32d))

### Version 1.6.0-beta03

December 13, 2023

`androidx.compose.foundation:foundation-*:1.6.0-beta03` is released. [Version 1.6.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15c82aaef0f1fd0307d6c00061859e5b6c4384c6..b76585a287cbcfdae38c3e16e5acbc6e26e808e2/compose/foundation)

**Bug Fixes**

- Fix crash that impacted very large text measured with infinite constraints. ([I1a7df](https://android-review.googlesource.com/#/q/I1a7df0f35e5506b4ca05c4e2091142012a07908f), [b/312294386](https://issuetracker.google.com/issues/312294386))
- `PlatformImeOptions` is now a concrete class instead of an interface. ([If40a4](https://android-review.googlesource.com/#/q/If40a4c3e832e7852f214e18af469f5ce68e798b7))

### Version 1.6.0-beta02

November 29, 2023

`androidx.compose.foundation:foundation-*:1.6.0-beta02` is released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..15c82aaef0f1fd0307d6c00061859e5b6c4384c6/compose/foundation)

**Bug Fixes**

- Fix for `canScroll` not being updated after relayout-only scroll. ([I60a86](https://android.googlesource.com/platform/frameworks/support/+/2d15876146ccf201f7e15cacc78bfca762060624))
- Fix for `Modifier.animateItemPlacement()` and `LookaheadScope` after small scrolls. ([I3a2b7](https://android.googlesource.com/platform/frameworks/support/+/14a894f3270c310a12a68f7ae1d0eda2ffe1c81e))

### Version 1.6.0-beta01

November 15, 2023

`androidx.compose.foundation:foundation-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose)

**API Changes**

- The `DragAndDropTarget` modifier now takes in the receiving `DragAndDropTarget` explicitly and has a lambda to opt into a drag and drop session. There are now two factory functions for a `DragAndDropModifierNode`. One for receiving transfers and one for transferring data ([I69481](https://android-review.googlesource.com/#/q/I69481ca031bfa52b3f8ff910b159e3ee8f7ffaf9))
- Updated `maximumFlingVelocity` to be represented as Float. Updated documentation to be more clear about the `maximumFlingVelocity` unity. ([I8adc7](https://android-review.googlesource.com/#/q/I8adc73327ca3c0d43a9ea31d871ddae1da5e9496))
- `onDragAndDropStart` in the `DragAndDropModifierNode`
  factory has been renamed to `acceptDragAndDropTransfer`.

  `acceptsDragAndDropTransfer` has been added to the `dragAndDropTarget` `Modifier` to accept from a drag and drop session.
  This lambda returns a viable
  `DragAndDropTarget` if interested in a drag and drop session.
  Other lambdas for processing drag events have been replaced by this.

  a `DragAndDropTarget` factory function has been added to receive from drag and drop sessions ([Iebf3a](https://android-review.googlesource.com/#/q/Iebf3a243ad9e4515dfe43b1947ab98ade6804a99))
- Exposing `startDragImmediately` in `AnchoredDraggable` gives control for detecting dragging gestures when using it. It is useful to set it when the widget is animating to a target anchor. See [Sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/samples/src/main/java/androidx/compose/foundation/samples/AnchoredDraggableSample.kt?q=java/androidx/compose/foundation/samples/AnchoredDraggableSample.kt#:%7E:text=AnchoredDraggableCatchAnimatingWidgetSample). ([Ie6d13](https://android-review.googlesource.com/#/q/Ie6d134277bb4f25bbab7ff1929d59bba00ede235), [b/285139987](https://issuetracker.google.com/issues/285139987))

- Foundation Tooltip APIs are now `@ExperimentalFoundationApi` ([I30b0b](https://android-review.googlesource.com/#/q/I30b0b47c0d7d048369779600071fde5f2452e71d))

- Removed `DragAndDropInfo` as a type `DragAndDropModifierNode.drag` now takes parameters for the `transferData`, decoration size and drag decoration `DrawScope` lambda

  `DragAndDropTarget` has methods for particular drag and drop events instead of being a single abstract method

  `onDragAndDropEvent` in the factory function for a `DragAndDropModifierNode` has been renamed to `onDragAndDropStart` to better communicate that the `DragAndDropTarget` provided is valid for a given drag and drop session only

  The `DragAndDropEventType` has been removed ([I645b1](https://android-review.googlesource.com/#/q/I645b1531085bceef359daebf7f36aa9119f6017b))
- Renamed `PlatformTextInputModifierNode.runTextInputSession` to `establishTextInputSession`. ([I03cd0](https://android-review.googlesource.com/#/q/I03cd0d84be09a89ed7a763d1b5921cb4975b72a0))

- Replace `OriginalText` by `TextSubstitution`. ([Ifa5a8](https://android-review.googlesource.com/#/q/Ifa5a8d6a2efd776c384642d9148dbf40b23eb6e3))

- Renamed `PlatformTextInputModifierNode.textInputSession` to `runTextInputSession`. ([Ie9c6b](https://android-review.googlesource.com/#/q/Ie9c6b37420dc9c024d68bbfc94fdcbbef105a547))

- The children of `SubcomposeLayout` (and layouts like `LazyColumn` based on it) which are retained to be reused in future are considered deactivated. New `assertIsDeactivated()` test API was introduced to test such nodes. The rest of the test apis will filter out deactivated nodes by default. ([I2ef84](https://android-review.googlesource.com/#/q/I2ef84fb2ed578238bb20c07655c475df6fb8dbd0), [b/187188981](https://issuetracker.google.com/issues/187188981))

- `clippingEnabled` parameter of `Modifier.magnifier` is renamed to `clip`.

- `magnifierCenter` parameter of `Modifier.magnifier` is made nullable preserving the same default behavior. ([I6aa66](https://android-review.googlesource.com/#/q/I6aa66e52283bd467372b6a04132341642549f20d))

- Material `SwipeToReveal` APIs (for Cards and Chips) now rely on a slot based API (as recommended by Compose) instead of data class based instances to create those slots. This is a breaking change, please see the demo and sample code for examples on how to use the new API. ([Ia8943](https://android-review.googlesource.com/#/q/Ia89431e240b0602bfe08bceb660ff9ef1137d938))

**Bug Fixes**

- Implement equals and hashcode for `PageSize.Fixed`. ([Ie3ede](https://android-review.googlesource.com/#/q/Ie3edea3aafd75068cd57c04aafdd7055ead20ad7), [b/300134276](https://issuetracker.google.com/issues/300134276))
- Fixed a bug that would cause `BasicText` layout to not shrink when `minWidth` changed and `minWidth` less than initial measure constraints `maxWidth` ([Idb19c](https://android-review.googlesource.com/#/q/Idb19ce3a2975761c189962887575eab3066a04b7))
- Add renderer support for Sweep Gradient in `ArcLine`. ([I4d5bb](https://android-review.googlesource.com/#/q/I4d5bb5948d2216dca2a29d2449fd97519b2b65bb))
- Fix binary compatibility issue with Window Inset change ([Iee695](https://android-review.googlesource.com/#/q/Iee695f0f1b2bf24a820b5a1bccfe550d9c29a5fa))
- Remove material core layer for Material3 Chip/Button as the microbenchmarks show better performance without it. ([I55555](https://android-review.googlesource.com/#/q/I5555573520638dd3c7f0d202e048ae6fffde19e5))

### Version 1.6.0-alpha08

October 18, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/foundation)

**New Features**

- `Modifier.draggable2D` is the new modifier that allows for easy 2d dragging support. See [Sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/samples/src/main/java/androidx/compose/foundation/samples/Draggable2DSamples.kt) ([Id95f5](https://android-review.googlesource.com/#/q/Id95f5706cb31e2c0d4bbd17bb127f527a313df6f), [b/214412658](https://issuetracker.google.com/issues/214412658))

**API Changes**

- `Modifier.dragAndDrawSource` has had the `onDrawDragShadow` lambda renamed to `drawDragDecoration` and `DragAndDropInfo` has had the size parameter renamed to `dragDecorationSize`. ([Id0e30](https://android-review.googlesource.com/#/q/Id0e3037697efad03dcf74c2c9393a733e6ab0489), [b/303904810](https://issuetracker.google.com/issues/303904810))
- `BasicTextField2`'s `decorationBox` parameter is renamed to `decorator`. Its type is also changed to an equivalent fun interface `TextFieldDecorator`. ([I23c1c](https://android-review.googlesource.com/#/q/I23c1cbb759aa823d100689bba3375166686573b4))

**Bug Fixes**

- Improved documentation on `BasicTextField` regarding `onValueChange` requirements. ([I90fc9](https://android-review.googlesource.com/#/q/I90fc9dea845dafbf35fd439fe7813b2a752d9189), [b/160257648](https://issuetracker.google.com/issues/160257648))

### Version 1.6.0-alpha07

October 4, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443/compose/foundation)

**API Changes**

- Introduced `PlatformTextInputMethodTestOverride` for writing tests for custom text editors. ([Id159b](https://android-review.googlesource.com/#/q/Id159b5ddf642d02a2427950d6f5fbe71e34fdf60))
- Renamed `GraphicsSurface` to `AndroidExternalSurface` ([I11680](https://android-review.googlesource.com/#/q/I1168074a32ebd7b8586ba80cc78c343b7e489097))
- Added `DisableNonLinearFontScalingInCompose` temporary flag to disable non-linear font scaling. Set `DisableNonLinearFontScalingInCompose = true` in your tests if you need time to clean them up. This flag will be removed in Compose 1.6.0-beta01. ([Ic9486](https://android-review.googlesource.com/#/q/Ic94869c0be14f0a131ebcee03cd08b9256f308ab))
- Added `ColorList` and `ColorSet` collections that avoid allocations. ([I744bd](https://android-review.googlesource.com/#/q/I744bdc5040eb4153b8cb5030e66d910157b8e41c))
- This change removes `shortSnapVelocityThreshold` which has been turned into an implementation detail of the implementations of `SnapLayoutInfoProvider`. ([I65f6d](https://android-review.googlesource.com/#/q/I65f6d577ecfb9ffbad9b2921f1cf1dcc813d24a6))
- Adds `dragAndDropSource` Modifier for starting drag and drop sessions, and `dragAndDropTarget` Modifier for receiving from drag and drop sessions ([Ib7828](https://android-review.googlesource.com/#/q/Ib782848c37656fd704f0cb2ef42baa16a4dc4f81), [b/286038936](https://issuetracker.google.com/issues/286038936))
- Update `SnapPositionInLayout` documentation and position method. Introduce content paddings to the position method in `SnapPositionInLayout`. ([Id7938](https://android-review.googlesource.com/#/q/Id79383a2bc99bc7db54f716fdfd7b0aa6708cfac), [b/300116110](https://issuetracker.google.com/issues/300116110))
- Added `UndoState` to `TextFieldState` that provides the ability to undo/redo the changes made by the user. ([Icc024](https://android-review.googlesource.com/#/q/Icc024ae43fe9046d7f20ddfe52de3a7810e8d0ce))

**Bug Fixes**

- Fixed `basicMarquee` not animating after velocity change. ([Id2e77](https://android-review.googlesource.com/#/q/Id2e77b47a3fd5cc046e59594cc1d5f01c99f34a0), [b/297974036](https://issuetracker.google.com/issues/297974036))

### Version 1.6.0-alpha06

September 20, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/foundation)

**New Features**

- New Composable wrappers for `SurfaceView` and `TextureView: GraphicsSurface()` and `EmbeddedGraphicsSurface()`. It is an experimental API and is subject to changes and modifications. ([I9ddb2](https://android-review.googlesource.com/#/q/I9ddb2355e01aacb20b9e595c7d58c7e972f63630))
- `Modifier.magnifier()` is now a stable API. This includes the removal of `MagnifierStyle` in favor of inline parameters in the modifier itself. ([I83bec](https://android-review.googlesource.com/#/q/I83bec09bc5ec419cb007d6f1e1340fba99f122d6), [b/298381260](https://issuetracker.google.com/issues/298381260), [b/262367109](https://issuetracker.google.com/issues/262367109), [b/261438887](https://issuetracker.google.com/issues/261438887))

**API Changes**

- Introduced `updateCurrentPage` and `updateTargetPage` in `ScrollScope`, these are the last pieces necessary to allowing customization of animated scroll through `PagerState.scroll`. ([I9cad5](https://android-review.googlesource.com/#/q/I9cad5789ef0d48da46b0e38fbc04bd9ac740861e), [b/267744105](https://issuetracker.google.com/issues/267744105), [b/243786897](https://issuetracker.google.com/issues/243786897))
- Remove density from `SnapFlingBehavior`. All implementations of `SnapLayoutInfoProvider` already have a way of accessing the density, the receiver scope could be removed which will lead to a less complex implementation of both `SnapFlingBehavior` and `SnapLayoutInfoProviders`. ([I153c3](https://android-review.googlesource.com/#/q/I153c358968d8f4bfec027f0568f29c887aa06d53))
- More modifiers marked as stable. ([I56af1](https://android-review.googlesource.com/#/q/I56af1d5a1f7e93a0e228a57e6631957ff94f82a3), [b/298046462](https://issuetracker.google.com/issues/298046462))
- Removed `SnapStepSize` from `SnapLayoutInfoProvider`. The calculation should be done using the Layout information and provided through the approach or snapping offsets. ([If320c](https://android-review.googlesource.com/#/q/If320cd680d318151d7c83f1f1df1878385c56078))

**Behavior Changes**

- Compose now uses non-linear font scaling for better readability and accessibility. When font scale \> 100% in system settings, small text will increase in size normally, but already-large text will only increase a little bit. Also, line heights defined in SP will automatically adjust to stay proportional to the 100% scale intended height. See the [Font Scaling Best Practices](https://goo.gle/font-scaling-best-practices) for more info. ([I11518](https://android-review.googlesource.com/#/q/I115181d1e91dff483c68aeb781e7cae4609e73d4))

**Bug Fixes**

- Remove the use of `rememberSaveable` for tooltips. ([Icc131](https://android-review.googlesource.com/#/q/Icc131c852cc3b3c722954aecb0a002711e13ca96), [b/299500338](https://issuetracker.google.com/issues/299500338))

### Version 1.6.0-alpha05

September 6, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/foundation)

**API Changes**

- Add overloads for `BasicSecureTextField` that accept an immutable value and a callback to change that value, just like the current `BasicTextField` API. ([Ia4882](https://android-review.googlesource.com/#/q/Ia4882ce8689f486cd7d7cf5bf5b51e0cf7b1d374))
- Add `Modifier.preferKeepClear()` to mark as composable as preferring to keep clear of floating windows on API 33 and above. ([Ib51d5](https://android-review.googlesource.com/#/q/Ib51d57d785da1e0503f26604819ba7d29940e052), [b/297260115](https://issuetracker.google.com/issues/297260115))
- Fling velocities in View components like `ScrollView` and `RecyclerView` are capped at `ViewConfiguration.ScaledMaximumFlingVelocity`. Compose now contains its own version of `maximumFlingVelocity` which now applies to `Draggable`. ([Ibf974](https://android-review.googlesource.com/#/q/Ibf974df663c88da673be5c549fbae31303c6ba14))
- Removed deprecated `Pager` and `PagerState` overloads. ([Iea07e](https://android-review.googlesource.com/#/q/Iea07e3c441146d90f2a53d6d0706445ce4ad7dea))
- Added `BasicTooltipBox` to `compose.foundation` and updated `PlainTooltipBox` and `RichTooltipBox` to use `TooltipBox` with new `PlainTooltip` and `RichTooltip` composables. ([I79e1d](https://android-review.googlesource.com/#/q/I79e1df0ac02fdccc3399dcf8d24a515d6461fde9))

### Version 1.6.0-alpha04

August 23, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/foundation)

**API Changes**

- Add `ReusableComposition` interface for managing lifecycle and reuse of subcompositions. ([I812d1](https://android-review.googlesource.com/#/q/I812d1fa36791857a04471882d5edabea1400c15e), [b/252846775](https://issuetracker.google.com/issues/252846775))
- `Modifier.focusGroup` has been promoted to stable APIs. ([I7ffa3](https://android-review.googlesource.com/#/q/I7ffa30d82e2e382865fcd57f5ee7640959c087e2))
- Add overloads for `BasicTextField2` that accept an immutable value and a callback to change that value, just like the current `BasicTextField` API. ([I3f2b8](https://android-review.googlesource.com/#/q/I3f2b851e744fe2cd6f9c0c79e9f2ecbf35d2fdca))
- `GridItemSpan::currentLineSpan` is now a stable API. ([Icc29c](https://android-review.googlesource.com/#/q/Icc29c5af036d72c218cc4c630e166c4088209049))
- Canvas that accepts `contentDescription` is now a stable API. ([Ib3d29](https://android-review.googlesource.com/#/q/Ib3d2916e9521268daf351ad17dce8d6a35d57aa5))
- Introduced `viewportSize` in `ScrollState`, a way of knowing the `viewPort` size of the component that uses `ScrollState` after measuring happens. ([I8b85a](https://android-review.googlesource.com/#/q/I8b85a0058db96f4b0eb5a6afa32e5293adaaeda5), [b/283102682](https://issuetracker.google.com/issues/283102682))
- Fixed an issue where the prefetching in Pager did not match the behavior in Views. ([I93352](https://android-review.googlesource.com/#/q/I93352e6de29fa8bc23b3af7516872d3e2da7ce0e), [b/289088847](https://issuetracker.google.com/issues/289088847))
- `Modifier.consumeWindowInsets(PaddingValues)` is now stable.
  - `Deprecated Modifier.consumedWindowInsets` API is now removed. Use `Modifier.consumeWindowInsets` instead. ([Id72bb](https://android-review.googlesource.com/#/q/Id72bbe3b02da9e9c34295a963b9efd1ceed96e41))

### Version 1.6.0-alpha03

August 9, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/foundation)

**API Changes**

- Overload of `LazyLayout` added, it accepts a lambda of `LazyLayoutItemProvider`, not a plain object as it was before. The previous overload is deprecated. ([I42a5a](https://android-review.googlesource.com/#/q/I42a5a3d5933deaccac5b5fc6df15c47194cf8b05))
- Added support for configuring `privateImeOptions` ([Idb772](https://android-review.googlesource.com/#/q/Idb772f8091a3a415659ccb0fb58846917c8e229c))

**Bug Fixes**

- Fixed text fields showing keyboard and being editable when `readOnly` is true. Also fixed the keyboard not showing when `readOnly` is changed from true to false while focused. ([I34a19](https://android-review.googlesource.com/#/q/I34a19a80d8f44b10f23db0ca0dd7b43b69311c7c), [b/246909589](https://issuetracker.google.com/issues/246909589))

### Version 1.6.0-alpha02

July 26, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/foundation)

**API Changes**

- Introduced `PagerLayoutInfo` with information collected after a measure pass in `Pager`. Also introduced `PageInfo`, the information about a single measured Page in `Pager`. ([Iad003](https://android-review.googlesource.com/#/q/Iad003bd71d5d26a6b0507f0c6c06751b3969d95c), [b/283098900](https://issuetracker.google.com/issues/283098900))
- Additional annotations to specify allowed inputs to composables ([I51109](https://android-review.googlesource.com/#/q/I51109ce34ab8bb50a8104572d79d2a94b67f3b17))
- Added `SemanticsNodeInteraction.requestFocus` as a more convenient and discoverable way to request focus in tests. ([Ie8722](https://android-review.googlesource.com/#/q/Ie87224a465a60cd462ee0eaf7c2d3797f1d63347))
- Completely redesigned `PlatformTextInput*` API. ([I6c93a](https://android-review.googlesource.com/#/q/I6c93a1111561b5cb55c6a34e2fc3738be3c8941d), [b/274661182](https://issuetracker.google.com/issues/274661182), [b/267235947](https://issuetracker.google.com/issues/267235947), [b/277380808](https://issuetracker.google.com/issues/277380808))
- `SoftwareKeyboardController` and `LocalSoftwareKeyboardController` are no longer experimental. `LocalSoftwareKeyboardController` is also now a proper `CompositionLocal`. ([I4c364](https://android-review.googlesource.com/#/q/I4c3647f331eacc78f15bd5aa6b19a31ff748b23d))
- `Modifier.transformable` now provides pan delta in `canPan` parameter to help determine the direction of the pan to allow or disallow it. ([I692aa](https://android-review.googlesource.com/#/q/I692aa5bf43084658ca6a20175869d9d593986f2b), [b/266829800](https://issuetracker.google.com/issues/266829800))
- Updates the modifier `consumeWindowInsets` to extend the superclass `AbstractComposeView` ([Iacd74](https://android-review.googlesource.com/#/q/Iacd74d1928c018276c3d923d55c959c644273b22), [b/269479941](https://issuetracker.google.com/issues/269479941))

### Version 1.6.0-alpha01

June 21, 2023

`androidx.compose.foundation:foundation-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..3b5b931546a48163444a9eddc533489fcddd7494/compose/foundation)

**New Features**

- Introduced a new `AnchoredDraggable` API in Foundation. It can be used to build components that can be dragged between discrete states, like modal bottom sheets. This API replaces Material's `Swipeable` API. ([I4a2ed](https://android-review.googlesource.com/#/q/I4a2ed763cbe73ee71f49311cf27f38105cdbd6e6))

**API Changes**

- Support `InputConnection#requestCursorUpdates` ([I0c69b](https://android-review.googlesource.com/#/q/I0c69bf50846ad6a639fe3f3f5f77f89747035b26))
- Introduced `scrollAnimationSpec` to allow custom animation specs. Updated `BringIntoViewCalculator` to `BringIntoViewScroller`. ([Idb741](https://android-review.googlesource.com/#/q/Idb741a8f55df781cc93448159dace9f339aec7b4))
- Add `ResourceResolutionException` type to wrap throwables thrown when attempting to load bitmap assets with a description of the asset path that failed to load. ([I19f44](https://android-review.googlesource.com/#/q/I19f445605ae8b171532b73b7ae4697cec0453767), [b/230166331](https://issuetracker.google.com/issues/230166331), [b/278424788](https://issuetracker.google.com/issues/278424788))
- Added semantics properties and actions to support text translation. ([I4a6bc](https://android-review.googlesource.com/#/q/I4a6bc0e167389b8604135d05fbcae7b3cebab0d1))
- Introduced a `BringIntoViewCalculator` API that can be used to customize how components like `Scrollable` respond to `bringIntoView` requests. Changed the overload of scrollable to optionally accept an instance of `BringIntoViewCalculator`. ([Iaf5af](https://android-review.googlesource.com/#/q/Iaf5af8c24b8545a3e5cb2af379111faea16015c8))

**Bug Fixes**

- Added a lint check to warn if you are creating a `MutableInteractionSource` in composition without remembering it, similar to the lint checks for creating mutable state / `Animatable`. ([I5daae](https://android-review.googlesource.com/#/q/I5daae036829f03ab257564e80edda0849aa21e63))
- Added support for selection by mouse. Touch based selection will expand by word, and shrink by character. ([Ic0c6c](https://android-review.googlesource.com/#/q/Ic0c6c247aefb9cf567525369468fe19fe77dc986), [b/180639271](https://issuetracker.google.com/issues/180639271))
- Added `FocusTargetModifierNode` interface that can be used to create a custom `FocusTarget`. ([I9790e](https://android-review.googlesource.com/#/q/I9790ef90091a66436fd7f03d0be787741b42935c))

## Version 1.5

### Version 1.5.4

October 18, 2023

`androidx.compose.foundation:foundation-*:1.5.4` is released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ed495b997a532cc4cbe39abdbaa98b8fc6f3764..b6d5e6e62e40f6938bdbcfef1d6c8a79e25006f8/compose/foundation)

### Version 1.5.3

October 4, 2023

`androidx.compose.foundation:foundation-*:1.5.3` is released. This version has no changes.

### Version 1.5.2

September 27, 2023

`androidx.compose.foundation:foundation-*:1.5.2` is released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a2cac855f7723e1e485c20ac68d34dc8bb68d1e..2bc777611812ef8ef7329a332fbaf8348af05ec7/compose/foundation)

**Bug Fixes**

- Fixed a bug in text that led to crashes in certain circumstances when semantics were invalidated.

### Version 1.5.1

September 6, 2023

`androidx.compose.foundation:foundation-*:1.5.1` is released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/foundation)

**Bug Fixes**

- Fixed text fields showing keyboard and being editable when `readOnly` is true. Also fixed the keyboard not showing when `readOnly` is changed from true to false while focused. ([I34a19](https://android-review.googlesource.com/#/q/I34a19a80d8f44b10f23db0ca0dd7b43b69311c7c), [b/246909589](https://issuetracker.google.com/issues/246909589))

### Version 1.5.0

August 9, 2023

`androidx.compose.foundation:foundation-*:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e423b92ad8e8707ff4031626131f05e33979eac8..65e3f15108d25a7e1c5c841c0855b21eca194070/compose/foundation)

**Important changes since 1.4.0**

- Many foundational modifiers, including `Modifier.clickable`,`Modifier.draggable`, `Modifier.scrollable`, layout modifier and more have been migrated to `Modifier.Node` API, reducing the overhead on the initial composition.
- Improvements in Pagers stability. Many bugs have been addressed.
- `pageCount` parameters now lives in `PagerState` instead of the Pager itself

### Version 1.5.0-rc01

July 26, 2023

`androidx.compose.foundation:foundation-*:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81e6706c269471032b283755131d2aa4e8821a89..e423b92ad8e8707ff4031626131f05e33979eac8/compose)

**Bug Fixes**

- An optional inspection to recommend migrating `mutableStateOf()` calls to their corresponding specialized types for primitives is available. Its lint ID is `AutoboxingStateCreation`. Previously, this inspection was enabled by default for all projects. To see this warning in Android Studio's editor and your project's lint outputs, change its severity from informational to warning (or higher) by declaring `warning "AutoboxingStateCreation"` inside your module's `build.gradle` or `build.gradle.kts` configuration as shown ([I34f7e](https://android-review.googlesource.com/#/q/I34f7ea540f782ae95630f7f94cab93d842dfdd0f)):

          android {
              lint {
                  warning "AutoboxingStateCreation"
              }
              ...
          }

### Version 1.5.0-beta03

June 28, 2023

`androidx.compose.foundation:foundation-*:1.5.0-beta03` is released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..24dc7b0781cb908b2385ec207ca1b3a72cb90093/compose/foundation)

### Version 1.5.0-beta02

June 7, 2023

`androidx.compose.foundation:foundation-*:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d26ca4055c940126ae1663ad0d54aafd23205ea4..9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e/compose/foundation)

### Version 1.5.0-beta01

May 24, 2023

`androidx.compose.foundation:foundation-*:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..d26ca4055c940126ae1663ad0d54aafd23205ea4/compose/foundation)

**API Changes**

- Implement `PlatformDataProvider` to provide heart rate and daily steps. `SensorGateway` interface is removed from the public API. ([I55b84](https://android-review.googlesource.com/#/q/I55b84b6b9bffc5f0a6b812307f1bd4ad61750d65))

**Bug Fixes**

- Reduce allocations during lazy list/grids/etc. measurements ([Iaf9e2](https://android-review.googlesource.com/#/q/Iaf9e27f481ce2cf0f03395fca03fb3d0b2eee7f1))
- Reduced allocations when applying snapshots ([I65c09](https://android-review.googlesource.com/#/q/I65c09492518269d6605a4731effd164d93be023a))
- Removed allocations from spring animations ([Ie9431](https://android-review.googlesource.com/#/q/Ie94317f7206752e917cd5e74eb19e6abede8e656))
- Removed allocation from `TextLayout` ([I0fd11](https://android-review.googlesource.com/#/q/I0fd1110a5b5b5e4c3f101209efe93dc54140a201))
- Removed multiple allocations in pointer velocity tracking ([I26bae](https://android-review.googlesource.com/#/q/I26baee3d57a0ea73292c03d73479078b47f39a75))

### Version 1.5.0-alpha04

May 10, 2023

`androidx.compose.foundation:foundation:1.5.0-alpha04` and `androidx.compose.foundation:foundation-layout:1.5.0-alpha04` are released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/foundation)

**API Changes**

- Added optimized `TextStyle.merge(...)` with full parameter list. ([Iad234](https://android-review.googlesource.com/#/q/Iad23419809af1c7405ba9a9d42569521e7647034), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Introduce a `SnapLayoutInfoProvider` that can be used with `LazyGridState`. ([I92134](https://android-review.googlesource.com/#/q/I92134d4e64e639774e0239814a2705d44467bbcf), [b/269237141](https://issuetracker.google.com/issues/269237141), [b/260914964](https://issuetracker.google.com/issues/260914964))
- Experimental `Modifier.animateItemPlacement()` was added for the lazy staggered grids item scope. You can apply it on the items in order to achieve the automation position change/reordering animations. ([I4b62d](https://android-review.googlesource.com/#/q/I4b62dc65bf21e9376678c2e86f368bd3b8ee7ae0), [b/257034719](https://issuetracker.google.com/issues/257034719))
- Promote `GridCells.FixedSize` to stable. `FixedSize` defines a `LazyGrid` where each cell takes exact size on cross axis, with the remaining space distributed by cross axis arrangement. ([I8542f](https://android-review.googlesource.com/#/q/I8542f31f185efcdb71169f2eba0f389c2222f2fc))
- Introduced receiver scope `PagerScope` for Pager and an utility function for calculation a given page offset. ([If2577](https://android-review.googlesource.com/#/q/If25778c9ed12b11732fe98a3ca751542ebd69cc5))
- Introduce the `snapPositionalThreshold` when creating a snap fling behavior. Use this parameter to specify a positional threshold to short snapping in Pager. ([If8f7f](https://android-review.googlesource.com/#/q/If8f7f5c5c95cca74c7e810969c6bf14cb064683b))
- Replaced `SnapLayoutInfoProvider.calculateSnappingOffsetBounds` with `calculateSnappingOffset`. In this new method we simply request the next offset to snap to. The calculation of the bounds should be performed at the implementation level as this may differ depending on how one needs snapping to happen. ([I923a4](https://android-review.googlesource.com/#/q/I923a4f8fbfa08db31446a52fd9bb869e33daf9fd))
- `LazyStaggeredGrid` APIs have been promoted to stable. ([I633a5](https://android-review.googlesource.com/#/q/I633a5534c0eaeee8e6cff80ed872a60bf42fdb20))
- Remove `pageCount` from `Horizontal/VerticalPager`. This should be provided at the state creation. Updated `PagerState` and `rememberPagerState` to accept the `pageCount`. ([Ieb52d](https://android-review.googlesource.com/#/q/Ieb52d10f08c4a45beaa4ce0a72734a44afb60ce7), [b/266965072](https://issuetracker.google.com/issues/266965072))
- Remove `pageCount` from `Horizontal/VerticalPager`. This should be provided at the state creation. Updated `PagerState` and `rememberPagerState` to accept the `pageCount`. ([Ifa3cb](https://android-review.googlesource.com/#/q/Ifa3cb3f0444ed1493efbeb3e6268f50684dec44a), [b/266965072](https://issuetracker.google.com/issues/266965072))
- Introduce `shortSnapVelocityThreshold` in Pager's `SnapFlingBehavior`. ([I7379e](https://android-review.googlesource.com/#/q/I7379e457b8b7321aba6605a81cccd2245122a80e), [b/275579012](https://issuetracker.google.com/issues/275579012))
- Adds a `FlowRowScope` and `FlowColumnScope`. ([I54fe2](https://android-review.googlesource.com/#/q/I54fe2b0945ebcd8a2bf99cf58ce4a06c12e0553d))

**Bug Fixes**

- Calls to get semantics on Text when constraints have `minWidth` and `minHeight` no longer crash. ([Ibd072](https://android-review.googlesource.com/#/q/Ibd0723171145265198eee10bf4666fdaa6efd06d))
- Fixed regression where keyboard wasn't showing for text fields inside dialogs not created by the `Dialog` composable. ([I82551](https://android-review.googlesource.com/#/q/I825512cde7e41dadfc8b7491bd24190d21b14729), [b/262140644](https://issuetracker.google.com/issues/262140644))

### Version 1.5.0-alpha03

April 19, 2023

`androidx.compose.foundation:foundation:1.5.0-alpha03` and `androidx.compose.foundation:foundation-layout:1.5.0-alpha03` are released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/compose/foundation)

This release enables the new text rendering stack for Compose. The new stack is performance optimized, and you should see no visible changes.

If you do see changes in rendered text, you can debug by setting `NewTextRendering1_5 = false` to confirm the behavior difference. Setting this will force recomposition. Please file any behavior differences as bugs.

The debug flag will be removed before the 1.5 beta01 release.([Iada23](https://android-review.googlesource.com/#/q/Iada234d046dffb92e45c1a910f6976aa1dd339cf), [b/246960758](https://issuetracker.google.com/issues/246960758))

**API Changes**

- Make `FlowColumn/FlowRow` inline. ([Idab37](https://android-review.googlesource.com/#/q/Idab37f7d83de66cf713ee29ba4c2f1f0243d4172))

### Version 1.5.0-alpha02

April 5, 2023

`androidx.compose.foundation:foundation:1.5.0-alpha02` and `androidx.compose.foundation:foundation-layout:1.5.0-alpha02` are released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/foundation)

**API Changes**

- Added support for fixed size cells in `LazyGrid` and arranging them with cross axis arrangement. ([I83ed9](https://android-review.googlesource.com/#/q/I83ed9c6fa41d500ab049726b85373fade65a7ccc), [b/235121277](https://issuetracker.google.com/issues/235121277), [b/267942510](https://issuetracker.google.com/issues/267942510))
- Added support for fixed size lanes in `LazyStaggeredGrid` and arranging them with cross axis arrangement. ([I7d519](https://android-review.googlesource.com/#/q/I7d51967becb63f581d15c8e2d40b5d00e25ceb1f))
- `UrlAnnotation`s in `AnnotatedString`s can now be opened via accessibility services like `TalkBack`. ([If4d82](https://android-review.googlesource.com/#/q/If4d82999d8c62aa3718e1e681eeeaac12a9b0f55), [b/253292081](https://issuetracker.google.com/issues/253292081))
- Added the `InsertTextAtCursor` semantics action for text fields. ([I11ed5](https://android-review.googlesource.com/#/q/I11ed573be29737b234a114863c3c8f81e0fd65b1))
- Text-related test actions (e.g. `performTextInput`) will now request focus directly, using the semantics action, instead of clicking on the field. ([I6ed05](https://android-review.googlesource.com/#/q/I6ed05394845155b1a7335e341ed3548a322f04f5))
- Adds support for cross axis spacing/arrangement using the `verticalArrangement` in `FlowRow` and `horizontalArrangement` in `FlowColumn`. We also remove the top-level `verticalAlignment` and `horizontalAlignment` in `FlowRow/FlowColumn`. Developers can use `Modifier.align` instead. This reduces confusion between the naming conventions of `verticalAlignment` and `verticalArrangement`. ([I87b60](https://android-review.googlesource.com/#/q/I87b60b6bb09586d9126b9494e998be0710df3b62), [b/268365538](https://issuetracker.google.com/issues/268365538))

### Version 1.5.0-alpha01

March 22, 2023

`androidx.compose.foundation:foundation:1.5.0-alpha01` and `androidx.compose.foundation:foundation-layout:1.5.0-alpha01` are released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce5f1f96b304c7952d07c5bb472112c4b0ee2312..5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/foundation)

**API Changes**

- Text and `BasicText` is refactored to use the new modifier system. This leads to substantial performance improvements in many cases. No changes should be visible. ([If1d17](https://android-review.googlesource.com/#/q/If1d17135e10b5eb6678842331421cb810e0d967e), [b/246961435](https://issuetracker.google.com/issues/246961435))
- Added the `PerformImeAction` semantics action to invoke the IME action on text editor nodes. ([Ic606f](https://android-review.googlesource.com/#/q/Ic606f69ba8860017a6d11f0f50dc0da063af0512), [b/269633506](https://issuetracker.google.com/issues/269633506))

**Bug Fixes**

- Updated internals of `Modifier.hoverable`. The `hoverable` modifier will only be shown in the inspector if it is enabled. ([I82103](https://android-review.googlesource.com/#/q/I82103dc33bad80b014b9c9546effaa76f1915ce2))

## Version 1.4

### Version 1.4.3

May 3, 2023

`androidx.compose.foundation:foundation:1.4.3` and `androidx.compose.foundation:foundation-layout:1.4.3` are released with no changes (only a version bump).

### Version 1.4.2

April 19, 2023

`androidx.compose.foundation:foundation:1.4.2` and `androidx.compose.foundation:foundation-layout:1.4.2` are released. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5..0872f930da585f7fbf6e17c74b1dc42045e8b2c6/compose/foundation)

### Version 1.4.1

April 5, 2023

`androidx.compose.foundation:foundation:1.4.1` and `androidx.compose.foundation:foundation-layout:1.4.1` are released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c13b30cf6683e0a43585416f30b55e07bf2b560e..5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5/compose/foundation)

### Version 1.4.0

March 22, 2023

`androidx.compose.foundation:foundation:1.4.0` and `androidx.compose.foundation:foundation-layout:1.4.0` are released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..c5b142d6ab0494c996b2378d5008ac1cd6da75f3/compose/foundation)

**Important changes since 1.3.0**

- Added Emoji compat integration to `Text` and `TextField`, as well as the lower level Paragraph. It is enabled by default when emojicompat is configured.
- `EmojiCompat` can be configured on a specific Text using `PlatformParagraphStyle`.
- Added full line span support to `LazyStaggeredGrid`[(I28252)](https://android-review.googlesource.com/#/q/I28252ba175f719bb6f731341cfad476c98e9c5e8)
- Adding experimental `onHover` to `ClickableText`[(I6938f)](https://android-review.googlesource.com/#/q/I6938fee052331eb671c07839e30e71e338adf897)
- Introduced new experimental overloads for the `runComposeUiTest` function and `create*ComposeRule` functions that accept `CoroutineContext` parameters. The context will be used for the test composition and any `LaunchedEffect` and `rememberCoroutineScope()` calls in the composition. ([I10614](https://android-review.googlesource.com/#/q/I10614adabdb137ad44fb51f65403866b5b184ac1), [b/265177763](https://issuetracker.google.com/issues/265177763))
- `FlowRow` and `FlowColumn` are now available as `@ExperimentalFoundationApi` that allow for a more flexible row and column based layout of components that will break to a new line if there is not enough space on the main axis. ([I3a7b2](https://android-review.googlesource.com/#/q/I3a7b26bff88ec172df7ab4acf62c2eefd5edb16d))
- `Modifier.basicMarquee()` is available as experimental for displaying content with a scrolling marquee effect. ([I2df44](https://android-review.googlesource.com/#/q/I2df44c3343afa8400b0da768a642b77da94c103d), [b/139321650](https://issuetracker.google.com/issues/139321650))

### Version 1.4.0-rc01

March 8, 2023

`androidx.compose.foundation:foundation:1.4.0-rc01` and `androidx.compose.foundation:foundation-layout:1.4.0-rc01` are released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..6022301db806601f282c53b8cbb5a981923a1589/compose/foundation)

**API Changes**

- Introduced new low-level `PlatformTextInputAdapter` API for building custom text input implementations that talk directly to platform APIs. ([I58df4](https://android-review.googlesource.com/#/q/I58df46daa7a88f9761dcd711519c6eddf8524b6d))
- Add support for reverse layout to `LazyStaggeredGrid`. ([I3ef4a](https://android-review.googlesource.com/#/q/I3ef4ac9464b116d22515411acd6c7fd303894025))

**Bug Fixes**

- `BasicTextField`'s `SetText` semantics action will now update the text buffer using the same code path as IME updates and the testing functions (e.g. `performTextReplacement`).
- Text testing functions `performTextClearance`, `performTextReplacement`, and `performTextSelection` now use `SemanticsActions`. ([I0807d](https://android-review.googlesource.com/#/q/I0807d73975224ac5bf02fc232c1ab615f76c1c7d), [b/269633168](https://issuetracker.google.com/issues/269633168), [b/269624358](https://issuetracker.google.com/issues/269624358))

### Version 1.4.0-beta02

February 22, 2023

`androidx.compose.foundation:foundation:1.4.0-beta02` and `androidx.compose.foundation:foundation-layout:1.4.0-beta02` are released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/foundation)

**API Changes**

- Added a new `Modifier.Node.onReset()` callback allowing you to reset some local state to properly handle the case when the `Layout` will be reused (for example as an item of `LazyColumn`). Fixed `FocusTargetModifierNode` to properly reset the focused state. ([I65495](https://android-review.googlesource.com/#/q/I65495712cdeafeb3fedc3e4272627c024f952ddb), [b/265201972](https://issuetracker.google.com/issues/265201972))
- Added `BlendMode` parameter to `DrawScope.drawText`, `Paragraph.paint`, and `MultiParagraph.paint` methods to support different blending algorithms when drawing text on Canvas. ([I57508](https://android-review.googlesource.com/#/q/I57508ab06da481f63b4061ecb8ad72c3a733b0a7))
- Removed the `modifierElementOf()` API. Please extend from `ModifierNodeElement` directly instead. ([Ie6d21](https://android-review.googlesource.com/#/q/Ie6d218280e3f9cdcd130f6abce2c5e549b12b765))

**Bug Fixes**

- Adjusting selection handles can no longer select a partial character. ([Idedd1](https://android-review.googlesource.com/#/q/Idedd1679a5d1a2f2a8c93405b8d2f0450e793feb))
- Fix crash when ctrl+backspace on empty `TextField` ([I0427f](https://android-review.googlesource.com/#/q/I0427f936ddc519955d4b8092a86e10e0825c8696), [b/244185537](https://issuetracker.google.com/issues/244185537))

### Version 1.4.0-beta01

February 8, 2023

`androidx.compose.foundation:foundation:1.4.0-beta01` and `androidx.compose.foundation:foundation-layout:1.4.0-beta01` are released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/foundation)

**New Features**

- Since 1.3, added Emoji compat integration to `Text` and `TextField`, as well as the lower level Paragraph. It is enabled by default when emojicompat is configured.
- `EmojiCompat` can be configured on a specific Text using `PlatformParagraphStyle`.

**API Changes**

- Added common implementation of `PinnableContainer` API used in all `LazyLayouts` to retain items that exit composition, but still need to be active. ([If45a4](https://android-review.googlesource.com/#/q/If45a40f06ea4c71a05c014d837dbb9bc5bfe8387))
- `PinnableContainer.PinnedHandle.unpin()` was renamed to `release()` ([I4667a](https://android-review.googlesource.com/#/q/I4667a137f47ffe29f66940c010a50b254ab9bdb2))

**External Contribution**

- Added `mainAxisItemSpacing` property to `LazyListLayoutInfo`, `LazyGridLayoutInfo` and `LazyStaggeredGridItemInfo` ([I52fad](https://android-review.googlesource.com/#/q/I52fad30754e5fdda03fb47ac4d08c0c0b4cde2dc))

### Version 1.4.0-alpha05

January 25, 2023

`androidx.compose.foundation:foundation:1.4.0-alpha05` and `androidx.compose.foundation:foundation-layout:1.4.0-alpha05` are released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/foundation)

**New Features**

- Added full line span support to `LazyStaggeredGrid` ([I28252](https://android-review.googlesource.com/#/q/I28252ba175f719bb6f731341cfad476c98e9c5e8))
- Adding experimental `onHover` to `ClickableText` ([I6938f](https://android-review.googlesource.com/#/q/I6938fee052331eb671c07839e30e71e338adf897))
- Introduced new experimental overloads for the `runComposeUiTest` function and `create*ComposeRule` functions that accept `CoroutineContext` parameters. The context will be used for the test composition and any `LaunchedEffect` and `rememberCoroutineScope()` calls in the composition. ([I10614](https://android-review.googlesource.com/#/q/I10614adabdb137ad44fb51f65403866b5b184ac1), [b/265177763](https://issuetracker.google.com/issues/265177763))

**API Changes**

- Merges the pre/post APIs of `OverscrollEffect` into combined 'decorator' `applyToScroll` and `applyToFling` functions. See the updated samples in the documentation for examples of how to implement an overscroll effect with the new API shape. ([I8a9c4](https://android-review.googlesource.com/#/q/I8a9c487a2d4a5438925d4664ac45c17f4a1b7e53), [b/255554340](https://issuetracker.google.com/issues/255554340))
- More type/nullability of inline/deprecated-hidden functions ([I24f91](https://android-review.googlesource.com/#/q/I24f91d55dabdd4f7ee05b8a679a4e928acc95d6d))
- `LineBreak` and `Hyphens` APIs in `TextStyle` are graduated to stable. ([Ic1e1d](https://android-review.googlesource.com/#/q/Ic1e1d5f43e0601251aa3cac549cd45b7cbb70aee))

**Bug Fixes**

- The cursor in text fields will now continue to blink even when animations are disabled. ([I95e70](https://android-review.googlesource.com/#/q/I95e700ee40223cbc3970160b5c267a427d614f39), [b/265177763](https://issuetracker.google.com/issues/265177763))
- `Modifier.basicMarquee` now animates even when animations are disabled in the system settings. ([I23389](https://android-review.googlesource.com/#/q/I23389686f06f2bf749a5f0326d0a33e6da23a1ec), [b/262298306](https://issuetracker.google.com/issues/262298306), [b/265177763](https://issuetracker.google.com/issues/265177763))

**External Contribution**

- `notifyFocusedRect` methods in `TextInputSession` and `TextInputService` are not deprecated again. ([I23a04](https://android-review.googlesource.com/#/q/I23a0425b573a644fcc114a2b60d7bbbdaf5b04ed), [b/262648050](https://issuetracker.google.com/issues/262648050))

### Version 1.4.0-alpha04

January 11, 2023

`androidx.compose.foundation:foundation:1.4.0-alpha04` and `androidx.compose.foundation:foundation-layout:1.4.0-alpha04` are released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/foundation)

**New Features**

- `FlowRow` and `FlowColumn` are now available as `@ExperimentalFoundationApi` that allow for a more flexible row and column based layout of components that will break to a new line if there is not enough space on the main axis. ([I3a7b2](https://android-review.googlesource.com/#/q/I3a7b26bff88ec172df7ab4acf62c2eefd5edb16d))
- `Modifier.basicMarquee()`is available as experimental for displaying content with a scrolling marquee effect. ([I2df44](https://android-review.googlesource.com/#/q/I2df44c3343afa8400b0da768a642b77da94c103d), [b/139321650](https://issuetracker.google.com/issues/139321650))

**API Changes**

- `FocusRequesterModifier` is deprecated in favor of `FocusRequesterNode` ([I7f4d7](https://android-review.googlesource.com/#/q/I7f4d7a99aa42f7f3e4f49d034f8358a41ed42d0f), [b/247708726](https://issuetracker.google.com/issues/247708726), [b/255352203](https://issuetracker.google.com/issues/255352203), [b/253043481](https://issuetracker.google.com/issues/253043481), [b/247716483](https://issuetracker.google.com/issues/247716483), [b/254529934](https://issuetracker.google.com/issues/254529934), [b/251840112](https://issuetracker.google.com/issues/251840112), [b/251859987](https://issuetracker.google.com/issues/251859987), [b/257141589](https://issuetracker.google.com/issues/257141589))
- `AndroidFont` constructor with `variationSettings` is now a stable API, and can be used to create new types of font descriptors. ([I5adcc](https://android-review.googlesource.com/#/q/I5adcc8bd923050d20021d4725fcfe0b36f258ae1), [b/261565807](https://issuetracker.google.com/issues/261565807))
- Introduced `PinnableContainer` api propagated by lazy lists via a composition local which allows to pin current item. This means such item will not be disposed when it is scrolled away from the view. For example, `Modifier.focusable()` will pin the current focused item via this mechanism. ([Ib8881](https://android-review.googlesource.com/#/q/Ib8881191a529c9d9dc5e886570650b1987763207), [b/259274257](https://issuetracker.google.com/issues/259274257), [b/195049010](https://issuetracker.google.com/issues/195049010))
- Rewrote the way scrollables respond to `bringIntoViewRequesters` and focusables to better model the complexity of those operations and handle more edge cases. ([I2e5fe](https://android-review.googlesource.com/#/q/I2e5fec8c8582a8fe1f191e37fd0f4f9165678664), [b/241591211](https://issuetracker.google.com/issues/241591211), [b/192043120](https://issuetracker.google.com/issues/192043120), [b/237190748](https://issuetracker.google.com/issues/237190748), [b/230756508](https://issuetracker.google.com/issues/230756508), [b/239451114](https://issuetracker.google.com/issues/239451114))
- More return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Added experimental `TextMotion` to `TextStyle` to define Text either to be `Static(default)` or Animated. Use `TextMotion.Animated` if Text is going to be scaled, translated, or rotated via animation. ([I24dd7](https://android-review.googlesource.com/#/q/I24dd75e606184220ed3eebc3c80f84d5c977c14c))
- Add `TextFieldFocusModifier` to fix focus navigation behaviour for android platform ([I00303](https://android-review.googlesource.com/#/q/I0030377131b9328f30ad62d8cb7f1a98f188b330))
- Replaced `maxSize: IntSize` argument in `drawText` with `size: Size` to be inline with other `DrawScope` functions. `size` is set to `Size.Unspecified` by default which should not change the previous default behavior. ([Icd27d](https://android-review.googlesource.com/#/q/Icd27ddc109548e76c7bc4fba08fb9dfc174afa40))

**Bug Fixes**

- Adjustments in the snapping physics in `SnapFlingBehaviour` for a more natural feel.

**Known Issue**

- When updating from `androidx.compose.foundation:1.4.0-alpha03` to `androidx.compose.foundation:1.4.0-alpha04`, you might experience a `java.lang.NoSuchFieldError` error. [Here](https://issuetracker.google.com/issues/265172081) is where the issue was orginially reported. A fix has been submitted, and will be available on the next Compose update. As a work around, update your `androidx.compose.material` and `androidx.compose.material3` libraries to the latest version(1.1.0-alpha04) or downgrade your `androidx.compose.foundation` to 1.4.0-alpha03.

### Version 1.4.0-alpha03

December 7, 2022

`androidx.compose.foundation:foundation:1.4.0-alpha03` and `androidx.compose.foundation:foundation-layout:1.4.0-alpha03` are released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/foundation)

**API Changes**

- In UI tests using a Compose rule, continuations resumed during `withFrameNanos` callbacks will not be dispatched until after all frame callbacks have finished running. This matches the behavior of compose when running normally. However, tests that rely on the old behavior may fail. This should only affect code that calls `withFrameNanos` or `withFrameMillis` directly, and has logic outside of callback passed to those functions that may need to be moved inside the callbacks. See the animation test changes in [this CL for examples](https://android-review.googlesource.com/#/q/Idb41309445a030c91e8e4ae05daa9642b450505c).
- Added optional `onPerformTraversals: (Long) -> Unit` parameter to `TestMonotonicFrameClock` constructor and factory function to run code after `withFrameNanos` callbacks but before resuming callers' coroutines. ([Idb413](https://android-review.googlesource.com/#/q/Idb41309445a030c91e8e4ae05daa9642b450505c), [b/254115946](https://issuetracker.google.com/issues/254115946), [b/222093277](https://issuetracker.google.com/issues/222093277), [b/255802670](https://issuetracker.google.com/issues/255802670))
- Introduce Page accessibility actions: `PageUp`, `PageDown`, `PageLeft`, `PageRight`. Note that these are only available from API 29. ([Ida4ab](https://android-review.googlesource.com/#/q/Ida4ab069a2c7f8d2fc06bf20555c611f4a360728))
- Introduce `HorizontalPager` and `VerticalPager`, a way of showing composables in a Pager manner. Introduced `PagerState` to control the Pagers as well as query information about the Pager's current state. Introduced `PageSize`, a way of controlling the size of a Pager's page, this can be used to create a carousel like Pagers. Introduced `PagerSnapDistance`, a way to control how snapping will work in Pager's fling behavior. ([I01120](https://android-review.googlesource.com/#/q/I01120224eaccd9ee255890eb409e87a7ef7ffd5f))
- Introduced an overload in `SnapFlingBehavior.performFling` to help to understand where the fling will settle. ([I569f6](https://android-review.googlesource.com/#/q/I569f6480401d4250f7a4e8a73f02d29d9c8c3b95))
- Removed `OverscrollEffect#isEnabled`. Instead of needing to remember and set this flag, just don't dispatch events to the overscroll effect in cases where you do not want overscroll to show (for example if `ScrollableState#canScrollForward/backward` both return false). ([I1a4b0](https://android-review.googlesource.com/#/q/I1a4b07627dca47f13d7adb7481fd25097b6eb6a9), [b/255554340](https://issuetracker.google.com/issues/255554340), [b/255557085](https://issuetracker.google.com/issues/255557085))
- Added `ScrollableState#canScrollForward` and `ScrollableState#canScrollBackward` to query whether a `ScrollableState` has room to scroll in either direction (whether it is at the minimum / maximum of its range). This defaults to true for backwards compatibility with existing implementations of `ScrollableState`. Consumers can use this to show indication to the user that there is still room to scroll, and this could also be used to avoid dispatching delta to `ScrollableStates` that have no room to scroll in a given direction, to reduce unnecessary work. ([Idf1a0](https://android-review.googlesource.com/#/q/Idf1a066bdd86d2205d4bd5bab121c73059ada054), [b/255557085](https://issuetracker.google.com/issues/255557085))
- Added an Modifier API to query ancestors scroll info. ([I2ba9d](https://android-review.googlesource.com/#/q/I2ba9d6d55f853e5d2775fe9a9f15e7a41d41e359), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Used in `Clickable` to correctly delay press interactions, when gestures could become scroll events.
- Fixed `Clickables` not correctly delaying ripples, when used inside an `Scrollable ViewGroup`.
- Updated Drawers and Sheets to correctly delay presses in case gestures can become scroll events.
- Update `snapStepSize` naming to be consistent with other methods in `SnapLayoutInfoProvider`. ([Ife67c](https://android-review.googlesource.com/#/q/Ife67c7ed561e4e8169f3e6234dab33819998234c))
- Added `EmojiCompat` to `Compose` ([Ibf6f9](https://android-review.googlesource.com/#/q/Ibf6f9f9d37c6280fe1b051269b127f0dfb1d6b6a), [b/139326806](https://issuetracker.google.com/issues/139326806))
- Renamed `consumedWindowInsets()` to `consumeWindowInsets()` and `withConsumedWindowInsets()` to `onConsumedWindowInsetsChanged()` and made the Modifiers public. ([Ie44e1](https://android-review.googlesource.com/#/q/Ie44e1304babf2007f6dc5894716ca92c2ef6d067))

**Bug Fixes**

- The crash with `Modifier.animateItemPlacement()` and Lazy grids was fixed. It was happening in some conditions when the new items count is smaller then the previous one. ([I0bcac](https://android-review.googlesource.com/#/q/I0bcac889f7916ab032be277ba11fcfb723e56516), [b/253195989](https://issuetracker.google.com/issues/253195989))

### Version 1.4.0-alpha02

November 9, 2022

`androidx.compose.foundation:foundation:1.4.0-alpha02` and `androidx.compose.foundation:foundation-layout:1.4.0-alpha02` are released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/foundation)

**API Changes**

- `awaitFirstDown` and `waitForUpOrCancellation` now accept a `PointerEventPass` for greater flexibility. ([I7579a](https://android-review.googlesource.com/#/q/I7579a2dbb44c748a3fd3e515d2e7ab086aaff443), [b/212091796](https://issuetracker.google.com/issues/212091796))
- Revert `beyondBoundCount` API from Lazy\* APIs ([I12197](https://android-review.googlesource.com/#/q/I121974911a3cca2210f27df5c88683dcdc77b545))
- Introduced parameter in Lazy APIs to compose and place out of viewport items ([I69e89](https://android-review.googlesource.com/#/q/I69e8973974b1e7fa0e1bd075b63ef42cbb4709cb), [b/172029355](https://issuetracker.google.com/issues/172029355))
- Added `minLines` parameter to the `BasicText` and `BasicTextField`. It allows to set the minimum height of these composables in terms of number of lines ([I24294](https://android-review.googlesource.com/#/q/I2429479960eef317f467fa054b979c12fd73689d), [b/122476634](https://issuetracker.google.com/issues/122476634))

### Version 1.4.0-alpha01

October 24, 2022

`androidx.compose.foundation:foundation:1.4.0-alpha01` and `androidx.compose.foundation:foundation-layout:1.4.0-alpha01` are released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..548c8ac2570ae6cf15798fea1380491f7d93796b/compose/foundation)

**API Changes**

- A new method, `awaitEachGesture()`, for gesture detectors was added. It operates similar to `forEachGesture()`, but the loop over gestures operates entirely within the `AwaitPointerEventScope` so events can't be lost between iterations.
- `forEachGesture()` has been deprecated in favor of `awaitEachGesture()` because it allows events to be lost between gestures. ([Iffc3f](https://android-review.googlesource.com/#/q/Iffc3fb8cf53d0e5eb9b529c023b3e2d29003e86f), [b/251260206](https://issuetracker.google.com/issues/251260206))
- Added `WindowInsets.imeAnimationSourc`e and `WindowInsets.imeAnimationTarget` to determine the animation progress and know where the IME will be after animation completes. ([I356f1](https://android-review.googlesource.com/#/q/I356f1bac4ac4ff311573eb8df7227098b9186c20), [b/217770337](https://issuetracker.google.com/issues/217770337))

## Version 1.3

### Version 1.3.1

November 9, 2022

`androidx.compose.foundation:foundation:1.3.1` and `androidx.compose.foundation:foundation-layout:1.3.1` are released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/foundation)

**Bug Fixes**

- Fix performance issue in `BeyondBoundsLayout` ([aosp/2255266](https://android-review.googlesource.com/c/platform/frameworks/support/+/2255266))
- `ContentInViewModifier` will not read layout coordinates unless attached ([aosp/2241316](https://android-review.googlesource.com/c/platform/frameworks/support/+/2241316))

### Version 1.3.0

October 24, 2022

`androidx.compose.foundation:foundation:1.3.0` and `androidx.compose.foundation:foundation-layout:1.3.0` are released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/foundation)

**Important changes since 1.2.0**

- Experimental versions of `LazyVerticalStaggeredGrid` and `LazyHorizontalStaggeredGrid` were introduced.
- `SnapFlingBehavior`, `rememberSnapFlingBehavior` and other corresponding APIs were added as experimental.
- `Modifier.clickable`, `Modifier.toggleable`, and `Modifier.selectable` now show ripples if clicked with the keyboard or d-pad on a remote control.

### Version 1.3.0-rc01

October 5, 2022

`androidx.compose.foundation:foundation:1.3.0-rc01` and `androidx.compose.foundation:foundation-layout:1.3.0-rc01` are released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/foundation)

**API Changes**

- Introduced `lowVelocityAnimationSpec` used by the approach step when there's not enough fling velocity to decay. ([Iaeb27](https://android-review.googlesource.com/#/q/Iaeb272de77d42e142c01cc3f514a85331e9ef856))
- Added new experimental API Hyphens to support automatic hyphenation in Text ([Iaa869](https://android-review.googlesource.com/#/q/Iaa869b15b0cf6d9b4f4ab87ddf687c2388b886e8))

### Version 1.3.0-beta03

September 21, 2022

`androidx.compose.foundation:foundation:1.3.0-beta03` and `androidx.compose.foundation:foundation-layout:1.3.0-beta03` are released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/foundation)

**API Changes**

- Add options to customize line breaking in Text. ([I86907](https://android-review.googlesource.com/#/q/I8690771e479fd832dcd991a234c49bfcca1beaa0))
- `BringIntoViewResponder`s are now able to get the most up-to-date bounds of a request while processing it. ([If86a5](https://android-review.googlesource.com/#/q/If86a581463c14db3fa5638720aabca9830720630), [b/241591211](https://issuetracker.google.com/issues/241591211))
- Introduce support for spacings between items to experimental `Staggered Grid` ([I10b82](https://android-review.googlesource.com/#/q/I10b82056a2da0df7b19889c14bf92d307adbec52))
- Introduce content padding to experimental `Staggered Grid` ([I342ea](https://android-review.googlesource.com/#/q/I342ea10af989e837517299ed85ad587606c14a02))
- Changed `size:IntSize` argument with `constraints: Constraints` in `TextMeasurer.measure` method to support minimum width constraints. ([I37530](https://android-review.googlesource.com/#/q/I37530a2f80f5a2226c6e155985491b824f08a0c0), [b/242707525](https://issuetracker.google.com/issues/242707525))
- Added `Modifier.withConsumedWindowInsets()` to get consumed `WindowInsets` for use outside `windowInsetsPadding`.
- Added `MutableWindowInsets` to allow easily changing `WindowInsets` without recomposition. ([I7fd28](https://android-review.googlesource.com/#/q/I7fd28c29953ca10b4182d07996f16b66263548b1), [b/237019262](https://issuetracker.google.com/issues/237019262), [b/243119659](https://issuetracker.google.com/issues/243119659))

### Version 1.3.0-beta02

September 7, 2022

`androidx.compose.foundation:foundation:1.3.0-beta02` and `androidx.compose.foundation:foundation-layout:1.3.0-beta02` are released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/foundation)

**API Changes**

- Initial version of experimental `StaggeredGrid` ([Ia48be](https://android-review.googlesource.com/#/q/Ia48bee0578661d2c1ecb3fdcab207e615097835f))
- Renamed `FocusDirection.In` and `FocusDirection.Out` to `FocusDirection.Enter` and `FocusDirection.Exit` ([Ia4262](https://android-review.googlesource.com/#/q/Ia4262d2f8edc3ec36d2edc9ed2858895971ba33c), [b/183746982](https://issuetracker.google.com/issues/183746982))
- Introduced a `rememberSnapFlingBehavior` overload that provides a quick way of enabling snapping in `LazyLists`. ([Ifb48a](https://android-review.googlesource.com/#/q/Ifb48aa88914ef278b32c0f0f5861c6bbc5ff7f6c))
- Replaced the `snapFlingBehavior` factory with a concrete `SnapFlingBehavior` class. Scoped `SnapLayoutInfoProvider` methods to Density to make Dp\<-\>Px conversions easier for the API users. ([I54a11](https://android-review.googlesource.com/#/q/I54a1185e1402e2f5b0a7f05655155bdfe6cb953e))
- Update `LazyLayoutMeasureScope.measure` to return list of placeables, highlighting desired immutability of the returned value. ([I48b7c](https://android-review.googlesource.com/#/q/I48b7ced0d579cc40287c3307a967b27439eb5c94))
- Introduced `SnapLayoutInfoProvider` which takes a `LazyListState` to create an instance of `SnapLayoutInfoProvider` that can be used to enable a snap `FlingBehavior` for `LazyLists`. ([I2dd10](https://android-review.googlesource.com/#/q/I2dd101bbbff6a75c05d89962f240fd0e4e278c38))

**Bug Fixes**

- Refactors `AwaitPointerEventScope#awaitLongPressOrCancellation` to match other await functions ([I646e6](https://android-review.googlesource.com/#/q/I646e6fb3477573b98183c10830c0f9dd4cfa715f))

### Version 1.3.0-beta01

August 24, 2022

`androidx.compose.foundation:foundation:1.3.0-beta01` and `androidx.compose.foundation:foundation-layout:1.3.0-beta01` are released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/foundation)

**API Changes**

- Removed `pointerPosition` from `OverscrollEffect` - effects that care about pointer position can use `Modifier.pointerInput { }` in the `effectModifier` to get the current pointer position instead. ([I9f606](https://android-review.googlesource.com/#/q/I9f606c640cc23d7483b32ed98b7caf790c9d2e36), [b/241239306](https://issuetracker.google.com/issues/241239306))
- Exposed `AwaitPointerEventScope#awaitLongPressOrCancellation` as additional building block for more complex gesture detection ([I04374](https://android-review.googlesource.com/#/q/I646e6fb3477573b98183c10830c0f9dd4cfa715f), [b/181577176](https://issuetracker.google.com/issues/181577176))
- Introduced `lazyListSnapLayoutInfoProvider` to enable snapping in Lazy Lists. ([I3ecdf](https://android-review.googlesource.com/#/q/I3ecdfe2b0584be65057eb9a4dab29fcbc401dbca))
- Introduced `SnapFlingBehavior`, a fling behavior that enables list snapping. Provide an instance of `SnapLayoutInfoProvider` with information about your snapping layout. ([Ie754c](https://android-review.googlesource.com/#/q/Ie754cce97819d2f81c6bd72a68ff79e1af31c51e))

### Version 1.3.0-alpha03

August 10, 2022

`androidx.compose.foundation:foundation:1.3.0-alpha03` and `androidx.compose.foundation:foundation-layout:1.3.0-alpha03` are released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/foundation)

**API Changes**

- Resource Fonts now support setting font variation settings (API 26+). ([I900dd](https://android-review.googlesource.com/#/q/I900dde1f539e580a66db9c14d389ada691377c91), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Variable font support in `DeviceFontFamilyNameFont` ([Ic1279](https://android-review.googlesource.com/#/q/Ic1279b2dcb1c29e75b8037791179853a9f828c02), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Removed experimental annotation from `PlatformTextStyle` and `LineHeightStyle`. ([I64bef](https://android-review.googlesource.com/#/q/I64bef65f524025ac386bf0cf0d362eb7ac9a7352))
- Text fields will now throw more detailed exceptions when the `OffsetMapping` provided by a `VisualTransformation` returns invalid indices. ([Ie73f9](https://android-review.googlesource.com/#/q/Ie73f9a652c29dde66d073a868a2e1c181feaa98d), [b/229378536](https://issuetracker.google.com/issues/229378536))
- Introduce experimental APIs to share item provider logic between Lazy layouts. ([Ic891c](https://android-review.googlesource.com/#/q/Ic891c22570c755e56ca35f65e8f8408048ce8d20))
- `ScrollableDefaults.reverseDirection()` is not experimental anymore. ([Iba646](https://android-review.googlesource.com/#/q/Iba64650ce62b9073b3554a6acf3385806711c4a5))
- Deprecated `SemanticsModifier.id` and moved the semantics id to `LayoutInfo.semanticsId` instead. ([Iac808](https://android-review.googlesource.com/#/q/Iac808fc0e3ff14f1c1a95ee3f1f24cd436245a0e), [b/203559524](https://issuetracker.google.com/issues/203559524))
- `checkScrollableContainerConstraints()` is not experimental anymore. ([I2c290](https://android-review.googlesource.com/#/q/I2c290705f35f9b8f15ff14d3fa1fc8d8fcf395de))
- `Modifier.clipScrollableContainer()` is not experimental anymore. ([Ia2b44](https://android-review.googlesource.com/#/q/Ia2b44e094e37bab71992d5fb366e866cf9dd3c31))
- Deprecate `TextInputService.show|hideSoftwareKeyboard`. Please use `SoftwareKeyboardController` instead in app code and `TextInputSession` in IME-management code. ([I14e4c](https://android-review.googlesource.com/#/q/I14e4cb6e685dd9a0a172797d8d3f363446aeb89d), [b/183448615](https://issuetracker.google.com/issues/183448615))

### Version 1.3.0-alpha02

July 27, 2022

`androidx.compose.foundation:foundation:1.3.0-alpha02` and `androidx.compose.foundation:foundation-layout:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/foundation)

**API Changes**

- Added `drawText` extension function on `DrawScope` to provide a way to draw multi-styled text on composables and modifiers that operate on a `DrawScope` like `Canvas` and `drawBehind`. ([I16a62](https://android-review.googlesource.com/#/q/I16a6226ae83d879f2c493fb811f1ecef77a1fc15), [b/190787898](https://issuetracker.google.com/issues/190787898))

**Bug Fixes**

- Soft keyboard will now be hidden when a text field is disabled while focused. ([I6e3e4](https://android-review.googlesource.com/#/q/I6e3e4c264a0927710ee2413740154ddb6ac392bf), [b/237308379](https://issuetracker.google.com/issues/237308379))
- When adding `InputEventChange` events to Velocity Tracker we will consider now deltas instead of positions, this will guarantee the velocity is correctly calculated for all cases even if the target element moves ([Icea9d](https://android-review.googlesource.com/#/q/Icea9d76a43643a6b17da11f3c539d27cb8fa6f6e), [b/216582726](https://issuetracker.google.com/issues/216582726), [b/223440806](https://issuetracker.google.com/issues/223440806), [b/227709803](https://issuetracker.google.com/issues/227709803))
- When a scrollable has a focused child, it will now correctly scroll to keep the focused child in view when its size is decreased, even when the size is animated. ([I80867](https://android-review.googlesource.com/#/q/I8086717b14174e566b299f2643f1dd6c0b250773), [b/230756508](https://issuetracker.google.com/issues/230756508), [b/220119990](https://issuetracker.google.com/issues/220119990))
- Fixed a crash where `TextField` is cleared and refilled while selection is active. ([I1235b](https://android-review.googlesource.com/#/q/I1235b669921e67dcbec9e55a6d1a95ff609fe4b6), [b/208655565](https://issuetracker.google.com/issues/208655565), [b/214253689](https://issuetracker.google.com/issues/214253689))

### Version 1.3.0-alpha01

June 29, 2022

`androidx.compose.foundation:foundation:1.3.0-alpha01` and `androidx.compose.foundation:foundation-layout:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..8094b683499b4098092c01028b55a38b49e357f2/compose/foundation)

**API Changes**

- Introduced the `UrlAnnotation` annotation type and associated methods to support `TalkBack` link support in `AnnotatedString`s. ([I1c754](https://android-review.googlesource.com/#/q/I1c754dfa0ce88a36989888b43816333dfc94b0aa), [b/231495122](https://issuetracker.google.com/issues/231495122))

**Bug Fixes**

- `BasicTextField` `cursorBrush` may now be animated without restarting the cursor timer. ([I812e6](https://android-review.googlesource.com/#/q/I812e6d2fd1db29b16401e121a2132aa37f6d7b51), [b/236383522](https://issuetracker.google.com/issues/236383522))

## Version 1.2

### Version 1.2.1

August 10, 2022

`androidx.compose.foundation:foundation:1.2.1` and `androidx.compose.foundation:foundation-layout:1.2.1` are released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255/compose/foundation)

### Version 1.2.0

July 27, 2022

`androidx.compose.foundation:foundation:1.2.0` and `androidx.compose.foundation:foundation-layout:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ff668d1061ec9e732d65ec3bfa9dc3db50fd87a..1e0793130863c72dc4a2d02bc975128f3ef0158b/compose/foundation)

**Important changes since 1.1.0**

- `LazyVerticalGrid` and `LazyHorizontalGrid` are stable now.
- You can now specify a content type for items in Lazy lists and grids. This will allow the components to reuse elements more efficiently.
- Lazy lists and grids now have `userScrollEnabled` param which allows to disable scrolling via the user gestures.
- A new experimental API called `LazyLayout` was added. It It is the API we use internally to power Lazy lists and grids.
- `OverscrollEffect` API has been introduced as experimental. You can define custom overscroll effects as well as adding a standard platform one to custom scrollable containers.
- [Nested scrolling interoperability APIs](https://developer.android.com/jetpack/compose/gestures#nested-scrolling-interop) have been introduced to allow for interoperability between views and compose scrolling actors.
- Mouse and trackpad scrolling has been added to all scrolling containers.

### Version 1.2.0-rc03

June 29, 2022

`androidx.compose.foundation:foundation:1.2.0-rc03` and `androidx.compose.foundation:foundation-layout:1.2.0-rc03` are released. [Version 1.2.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..e8af23f4f30713a3f6073d57558e7cde0f3056e9/compose/foundation)

- No changes since 1.2.0-rc02.

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.foundation:foundation:1.2.0-rc02` and `androidx.compose.foundation:foundation-layout:1.2.0-rc02` are released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/foundation)

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.foundation:foundation:1.2.0-rc01` and `androidx.compose.foundation:foundation-layout:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/foundation)

**API Changes**

- An experimental `OverscrollEffect` has been introduced to allow for custom overscroll effects, alongside the `Modifier.scrollable` overloads that accept it.
- Experimental `LocalOverScrollConfiguration` has been moved from `foundation.gesture` to foundation package and renamed to `LocalOverscrollConfiguration` ([If19fb](https://android-review.googlesource.com/#/q/If19fb8063922eddf1ffcb020ec6a8fbe48471ccf), [b/204650733](https://issuetracker.google.com/issues/204650733))
- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))
- Introduced an experimental api `checkScrollableContainerConstraints()` which allows to check that we do not nest scrollable containers. You can use it when create your own scrollable lazy layouts via `LazyLayout`. ([Id6fab](https://android-review.googlesource.com/#/q/Id6fabde2877f20155be3d9642c2e74e0e7d4dab0), [b/233352497](https://issuetracker.google.com/issues/233352497))
- Removed deprecated `LazyVerticalGrid` from `androidx.compose.foundation.lazy` package. The new stable api is located in `androidx.compose.foundation.lazy.grid` ([I73c76](https://android-review.googlesource.com/#/q/I73c76e02e0b95692dbceeae372b1e15f33aa57d7), [b/225192009](https://issuetracker.google.com/issues/225192009))

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.foundation:foundation:1.2.0-beta03` and `androidx.compose.foundation:foundation-layout:1.2.0-beta03` are released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/foundation)

**API Changes**

- Added new experimental `IntervalList` and `MutableIntervalList`. It allows to represent some list of values via multiple intervals. It will be useful when you want to define your own dsl similar to the one used by `LazyColumn` where list items can be defined via multiple item/items calls. ([I2d05e](https://android-review.googlesource.com/#/q/I2d05e91646068eab522514024b483d88d77be309), [b/228580728](https://issuetracker.google.com/issues/228580728))

**Bug Fixes**

- Clarified the documentation for `WindowInsets.ime` to state that `ime` insets are reported as far back as API 23, but only *animated* on 30+. ([Ia7fc0](https://android-review.googlesource.com/#/q/Ia7fc002bde64074be7a176121483bff3017f24a8), [b/230756508](https://issuetracker.google.com/issues/230756508))
- Pressing the forward delete key when the cursor is at the end of a text field will no longer crash.
- `DeleteSurroundingTextCommand` and `DeleteSurroundingTextInCodePointsCommand` now require their constructor arguments to be non-negative. ([Ica8e6](https://android-review.googlesource.com/#/q/Ica8e66d221137a82ac8aaa59372decab096a6ef6), [b/199919707](https://issuetracker.google.com/issues/199919707))

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.foundation:foundation:1.2.0-beta02` and `androidx.compose.foundation:foundation-layout:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/foundation)

- Downloadable font resolution that does not change the layout size of Text or `TextField` previously would not redraw, leading to stale font display. This bugfix ensures that text layout always triggers redraw (b/229727404). ([I1d49e](https://android-review.googlesource.com/#/q/I1d49e9b977c234c9bc0317def7918d7821b321eb), [b/229727404](https://issuetracker.google.com/issues/229727404))

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.foundation:foundation:1.2.0-beta01` and `androidx.compose.foundation:foundation-layout:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/foundation)

**New Features**

- This is the first beta release of 1.2!

**API Changes**

- Added experimental `BeyondBoundsInterval` that can be used by custom implementations of `LazyList` when they layout items beyond visible bounds ([Ifabfb](https://android-review.googlesource.com/#/q/Ifabfbd95ba53bad23ce73bdb74f816c7854222bf), [b/184670295](https://issuetracker.google.com/issues/184670295))
- `LineHeightBehavior` is renamed as `LineHeightStyle`
- `LineVerticalAlignment` is renamed as `LineHeightStyle.Alignment`
- Renames `LineHeightTrim` is renamed as `LineHeightStyle.Trim`
- Default constructor values from `LineHeightStyle` is removed ([I582bf](https://android-review.googlesource.com/#/q/I582bf09152d60b30362b3cce9bd60d57fc488fe7), [b/181155707](https://issuetracker.google.com/issues/181155707))
- Added default values for the optional members of `LazyLayoutItemProvider` interface. ([Iba8a0](https://android-review.googlesource.com/#/q/Iba8a0196e68efce0afe0610a8b6e79fe3f02ee83))
- In the `LazyLayoutItemProvider` api instead of a factory returning the composable lambda by index we now have a simpler composable function Item accepting the index. ([Id2196](https://android-review.googlesource.com/#/q/Id21962ddb1fd14b8946d89c948d4f1779dc8fc8c))
- LazyLayoutItemsProvider is renamed to LazyLayoutItemProvider ([I0638c](https://android-review.googlesource.com/#/q/I0638c931ced98a63b63bf7e2122f1a14dbe37cf0))
- `LazyLayoutItemsProvider.itemsCount` is renamed to `itemCount` ([Id409c](https://android-review.googlesource.com/#/q/Id409c7afef79f35cc3e2ef019b9842c2ad507f58))
- Added Brush to `TextStyle` and `SpanStyle` to provide a way to draw text with gradient coloring. ([I53869](https://android-review.googlesource.com/#/q/I538698c22f5a03b57ed811ea733dd1194deaaa6a), [b/187839528](https://issuetracker.google.com/issues/187839528))
- `trimFirstLineTop`, `trimLastLineBottom` attributes of `LineHeightBehavior` changed into a single enum: `LineHeightTrim`. `LineHeightTrim` have values of 4 states defined by two booleans: `FirstLineTop`, `LastLineBottom`, Both and None ([Ifc6a5](https://android-review.googlesource.com/#/q/Ifc6a5912eab7a0e41ae6cd4045ea9cbdf3c0a146), [b/181155707](https://issuetracker.google.com/issues/181155707))
- Added `LineHeightBehavior` to the `TextStyle` and `ParagraphStyle. LineHeightBehavior` controls whether line height is applied to the top of the first line and to the bottom of the last line. It also defines the alignment of line in the space provided by `TextStyle`(`lineHeight`).

  For example it is possible to get a behavior similar to what CSS
  defines via `LineHeightBehavior(alignment = LineVerticalAlignment.Center, trimFirstLineTop=false, trimLastLineBottom = false)`.
- `trimFirstLineTop`, `trimLastLineBottom` configurations works correctly
  only when `includeFontPadding` is false. ([I97332](https://android-review.googlesource.com/#/q/I973329a540ca9f5a6e225f1e5aaffeaa1ff9cc61), [b/181155707](https://issuetracker.google.com/issues/181155707))

- Added experimental `imeNestedScroll()` modifier so that developers can control the IME through scrolling. ([I60759](https://android-review.googlesource.com/#/q/I6075942f67d2fbbdde97e5ce58f6fc871e51b7bc))

**Bug Fixes**

- Fixed regression where text fields would not hide the keyboard when removed from the composition while focused. ([I7a410](https://android-review.googlesource.com/#/q/I7a41031f5fb257200cf9958fe0d2a64af2519c9a), [b/230536793](https://issuetracker.google.com/issues/230536793), [b/225541817](https://issuetracker.google.com/issues/225541817))
- Support ellipsis when height is limited and doesn't fit all text lines ([Ie528c](https://android-review.googlesource.com/#/q/Ie528c603d4c76c31ea71524a8381000d43d1cf42), [b/168720622](https://issuetracker.google.com/issues/168720622))
- `BringIntoViewRequester.bringIntoView` will now always suspend until the request is either completed or was interrupted by a newer, non-overlapping request. Overlapping requests will be queued. ([I43e7f](https://android-review.googlesource.com/#/q/I43e7f73af86615f08e2d2d05bfd05ac96d0c65e4), [b/216790855](https://issuetracker.google.com/issues/216790855))
- Concurrent `BringIntoViewRequester.bringIntoView` calls for rectangles that are completely overlapping will now only honor the larger rectangle's request. ([I34be7](https://android-review.googlesource.com/#/q/I34be70f23527e4fea694fd5266bbc127cc1d1b0b), [b/216790855](https://issuetracker.google.com/issues/216790855), [b/184760918](https://issuetracker.google.com/issues/184760918))
- Turned on default `includeFontPadding`. It is possible to turn off the `includeFontPadding` using `TextStyle.platformTextStyle` attribute. In the near future we will change the default behavior however until that time this allows us to better integrate line height improvements (aosp/2058653) and solve `TextField` clipping issues. ([I01423](https://android-review.googlesource.com/#/q/I01423d9a0042a1f3e462236e1fdadb60a20678fc), [b/171394808](https://issuetracker.google.com/issues/171394808))
- `Modifier.bringIntoViewRequester` no longer uses `onGloballyPositioned`. ([I630f5](https://android-review.googlesource.com/#/q/I630f552bc59f31e91852aeaf3345216bb1f8c403))

**External Contribution**

- `MouseInjectionScope.scroll(delta = someDelta)` is now inverted on Android if we scroll vertically (if someDelta is positive, it will scroll downward) ([Ifb697](https://android-review.googlesource.com/#/q/Ifb697a9ae8bc05a2d54d0a6cb4018713e156baf8), [b/224992993](https://issuetracker.google.com/issues/224992993))

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha08` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha08` are released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/foundation)

**API Changes**

- Display all available weights for systems fonts on Android when using `FontFamily.SansSerif`. This will use fallback font names like sans-serif-medium internally on API 21-28. This is a behavior change as previously only weights 400 and 700 were supported on API 21-28. ([I380fe](https://android-review.googlesource.com/#/q/I380fecb5ba839eecbf0b08acbca6247082b605d7), [b/156048036](https://issuetracker.google.com/issues/156048036), [b/226441992](https://issuetracker.google.com/issues/226441992))
- Paragraph and MultiParagraph are now accepting Constraints parameter. Passing `Constraints.maxHeight` is a no-op at the moment but will allow to do some calculation in the future, like ellipsizing based on the height. ([I6afee](https://android-review.googlesource.com/#/q/I6afeecb15d34ade2e82cad0381018f0736a167c1), [b/168720622](https://issuetracker.google.com/issues/168720622))
- `SubcomposeSlotReusePolicy.getSlotsToRetain()` now accepts a custom MutableSet-like class which doesn't allow adding new items in it. ([Icd314](https://android-review.googlesource.com/#/q/Icd314177f35c2ba05d1042454ca47834cf196e10))
- Partial consumption (down OR position) has been deprecated in `PointerInputChange`. You can use `consume()` to consume the change completely. You can use `isConsumed` to determine whether or not someone else has previously consumed the change.
- `PointerInputChange::copy()` now always makes a shallow copy. It means that copies of `PointerInputChange` will be consumed once one of the copies is consumed. If you want to create an unbound `PointerInputChange`, use constructor instead. ([Ie6be4](https://android-review.googlesource.com/#/q/Ie6be471e6ed2a843e38712922c2231fdfd26213a), [b/225669674](https://issuetracker.google.com/issues/225669674))
- New experimental `LazyLayout` API is introduced. This allows you to build your own components like `LazyColumn` of `LazyVerticalGrid`. Note that the API is in its early stages and can be changed in the future releases. ([Iba2bc](https://android-review.googlesource.com/#/q/Iba2bcf7e48fb1693c61e9e0b93e0a9e97f9ecf8c), [b/166591700](https://issuetracker.google.com/issues/166591700))
- `AndroidFont` now takes `typefaceLoader` as a constructor parameter. ([I2c971](https://android-review.googlesource.com/#/q/I2c9718fa02b6f84813e5d5cdb499c89b355b0b4b))
- `WindowInsets` companion now exposes the visibility (whether they are on the screen, regardless of whether they intersect with the window) and the size they could be if they are available on the device, but not currently active. ([I65182](https://android-review.googlesource.com/#/q/I65182e3c8cdc868b9f6de3aef403c9f4d5074711), [b/217770337](https://issuetracker.google.com/issues/217770337))

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha07` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha07` are released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/foundation)

**API Changes**

- Added a `PinnableParent` API that allows children of lazy layouts to prevent the currently composed items from being disposed ([Ibbdd0](https://android-review.googlesource.com/#/q/Ibbdd02b0d25db2e0de343d5d2278287ab1991831), [b/184670295](https://issuetracker.google.com/issues/184670295))
- `LazyListLayoutInfo` and `LazyGridLayoutInfo` now have `beforeContentPadding` and `afterContentPadding` fields ([I3b628](https://android-review.googlesource.com/#/q/I3b628e4f4fdfc27b7629c3ac1cd2b47375ff31f2), [b/200920410](https://issuetracker.google.com/issues/200920410))
- Added `KeyboardType.Decimal` as an alternative to `Keyboard.Number` for specifically including decimal separator in IME. ([Iec4c8](https://android-review.googlesource.com/#/q/Iec4c84be81e72f8eaf136f2df23f9d12567cc3dc), [b/209835363](https://issuetracker.google.com/issues/209835363))
- Add new font descriptor Font(DeviceFontFamilyName) to optionally lookup system-installed fonts during font fallback chains. ([I30468](https://android-review.googlesource.com/#/q/I30468e48564fb9891e17cbee8bdb4026df0daf89), [b/219754572](https://issuetracker.google.com/issues/219754572))
- `PointerEventType.Scroll` and `PointerEvent.scrollDelta` are stable APIs now ([I574c5](https://android-review.googlesource.com/#/q/I574c579abec9e26dfc16ae00014faab8627bd688), [b/225669674](https://issuetracker.google.com/issues/225669674))
- Added temporary compatibility configuration for `includeFontPadding` in `TextStyle/ParagraphStyle. includeFontPadding` can be changed via `TextStyle(platformStyle = PlatformTextStyle(includeFontPadding = true/false))`. This is a temporary configuration option to enable migration and will be removed. ([If47be](https://android-review.googlesource.com/#/q/If47be074f53de9ccf12af114648b21e25722d166), [b/171394808](https://issuetracker.google.com/issues/171394808))
- Updated `FontFamily.Resolver` to integrate System-wide bold text accessibility setting ([I6c1e7](https://android-review.googlesource.com/#/q/I6c1e77e9cc8d1ce353d129d8a233271db0139a07))
- The `consumeWindowInsets` extension property of `ComposeView` allows developers to disable consumption of Android WindowInsets. This allows separate `ComposeViews` in the hierarchy to each apply `WindowInsets` without interfering with each other. ([I0ef08](https://android-review.googlesource.com/#/q/I0ef08ca81d808408edb932f9326125f99da25bd0), [b/220943142](https://issuetracker.google.com/issues/220943142))

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha06` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha06` are released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/foundation)

**API Changes**

- Added `RequestFocus` semantics action to request focus on the focusable target. ([I17b71](https://android-review.googlesource.com/#/q/I17b71a13ca810f3ead1b7b87245b31b8e5b28f91))
- `FocusOrder` has now been merged into `FocusProperties` and `focusProperties()` now has all the capabilities of `focusOrder()`. `FocusOrder` and `focusOrder()` have been deprecated. `focusOrder()` that accepts a `focusRequester` should be replaced with a `focusRequester()` modifier in combination with `focusProperties()`. This allows the modifiers to have a stronger separation of concerns. ([I601b7](https://android-review.googlesource.com/#/q/I601b751755bcfefd849c8a0c0d019e3eaf5d459c))
- `WindowInsets.asPaddingValues(Density)` was added to allow developers to do the conversion without needing to be in composition. ([I94c35](https://android-review.googlesource.com/#/q/I94c353356d8550e56ca297be5c44a26b3a99b34a))
- Updated parsing of vector drawables to support auto mirroring to flip the content of a `VectorPainter` if the current layout direction is RTL. ([I79cd9](https://android-review.googlesource.com/#/q/I79cd946811e9b06ff4186180c4f8eaa0dcdbc879), [b/185760237](https://issuetracker.google.com/issues/185760237))

**Bug Fixes**

- Scroll modifiers (`Modifier.verticalScroll()`,`Modifier.horizontalScroll()`, and `Modifier.scrollable()`) will now scroll to keep the focused composable visible if the scroll area is resized and the focused composable was previously visible.
- TextFields will now be kept above the keyboard when they are focused and the keyboard is shown, when inside a non-lazy scrollable and the soft input mode is `ADJUST_RESIZE`. ([I4a485](https://android-review.googlesource.com/#/q/I4a485a1c80aa2d500dcd55e916006903ff45da95), [b/190539358](https://issuetracker.google.com/issues/190539358), [b/192043120](https://issuetracker.google.com/issues/192043120), [b/216842427](https://issuetracker.google.com/issues/216842427))

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha05` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha05` are released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/foundation)

**API Changes**

- `LazyVerticalGrid` and `LazyHorizontalGrid` are now stable. ([I307c0](https://android-review.googlesource.com/#/q/I307c0ce412c7bc762e334e429013c0442bd22fde))
- `LazyGridItemInfo.Unknown` was replaced with separate `LazyGridItemInfo.UnknownRow` and `LazyGridItemInfo.UnknownColumn` ([I56d51](https://android-review.googlesource.com/#/q/I56d512212459f408a00cff1601d010f72184102d))
- `LazyVerticalGrid`/`LazyHorizontalGrid` and all related apis were moved into `.grid` subpackage. Please update your imports from `androidx.compose.foundation.lazy` to `androidx.compose.foundation.lazy.grid`. ([I2d446](https://android-review.googlesource.com/#/q/I2d446e0bed6f27f0394b7dcab1152301e3404b0f), [b/219942574](https://issuetracker.google.com/issues/219942574))
- Text: `includeFontPadding` is now turned off by default. The clipping issues as a result of `includeFontPadding=false` is handled and no clipping should occur for tall scripts. ([I31c84](https://android-review.googlesource.com/#/q/I31c84166ae5241fea3f49e8f293dd9d8a5d712cb), [b/171394808](https://issuetracker.google.com/issues/171394808))
- Measured interface now exposes parentData property ([I3313f](https://android-review.googlesource.com/#/q/I3313f74c5eb4a75b91cb9d438c6691117b152a7d))
- Introduced experimental `Modifier.onFocusedBoundsChanged` to allow observing the bounds of child focusables. ([I14283](https://android-review.googlesource.com/#/q/I14283393b5273527ab65f4aa1a2d4383321b0d95), [b/220030968](https://issuetracker.google.com/issues/220030968), [b/190539358](https://issuetracker.google.com/issues/190539358), [b/192043120](https://issuetracker.google.com/issues/192043120), [b/216842427](https://issuetracker.google.com/issues/216842427))
- LazyHorizontalGrid was added. ([I61ae7](https://android-review.googlesource.com/#/q/I61ae7abe269fdb3776c301dd5c233762f9766f4d), [b/191238807](https://issuetracker.google.com/issues/191238807))
- Added a new `LazyVerticalGrid` API to define cross axis sizes ([I17723](https://android-review.googlesource.com/#/q/I17723fdc6302a345dd643fb637e1644168a2a321))
- Added FocusGroup modifier ([I64bc0](https://android-review.googlesource.com/#/q/I64bc0b945bf172ad37b64d011d7055f4a99bfeca), [b/213508274](https://issuetracker.google.com/issues/213508274), [b/184670295](https://issuetracker.google.com/issues/184670295))

**Bug Fixes**

- `WindowInsets.toString()` will now show the correct values. ([I1585d](https://android-review.googlesource.com/#/q/I1585d12df9b15b616ede0bda7db39a2cc4ead3d3))

**External Contribution**

- Updated to use Kotlinx coroutines 1.6.0 ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha04` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha04` are released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/foundation)

**API Changes**

- `BringIntoViewResponders` are no longer required to manually pass requests up to parent responders, and are instead required to immediately return the rectangle they want their parent to bring into view. ([I8e66a](https://android-review.googlesource.com/#/q/I8e66acfde483dd1a3b67dbf37cc815967eae746a))
- Support async font loading in Text ([I77057](https://android-review.googlesource.com/#/q/I77057da6e45e78bea9622f480343c32d0bb25ce3), [b/214587005](https://issuetracker.google.com/issues/214587005))
- `LazyVerticalGrid` now supports `line breaking` before items with span not fitting inside the current line. ([I05c40](https://android-review.googlesource.com/#/q/I05c405c9ccf81fb1682a8f84eb36481d3b13ceea), [b/207462103](https://issuetracker.google.com/issues/207462103))
- Renamed `excludeFromSystemGestures` to `systemGesturesExclusion` ([I19526](https://android-review.googlesource.com/#/q/I19526f6c1f89946c5ec433f477c65ff41ec3b10d))
- `LazyVerticalGrid` now supports reverseLayout. ([I6d7d7](https://android-review.googlesource.com/#/q/I6d7d7057318b873fc22b78a212480e1205ccb8c0), [b/215572963](https://issuetracker.google.com/issues/215572963), [b/211753558](https://issuetracker.google.com/issues/211753558))
- Add `WindowInsets.only()` method to allow developers to include only dimensions from the WindowInsets. ([I14c94](https://android-review.googlesource.com/#/q/I14c94c017d0b7a31f5fc3248f478d5331332d18f), [b/217768486](https://issuetracker.google.com/issues/217768486))
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

**Bug Fixes**

- Now it is allowed to pass negative scroll offsets into `LazyGridState.scrollToItem()` and `LazyGridState.animateScrollToItem()`. ([I025c6](https://android-review.googlesource.com/#/q/I025c608ce2eef36f90ad657bba78229b62bcd725), [b/211753558](https://issuetracker.google.com/issues/211753558))
- Support async font loading for TextField. ([Icc4bf](https://android-review.googlesource.com/#/q/Icc4bf288dde6406b470c700dc760a9d99bdc0971), [b/214587005](https://issuetracker.google.com/issues/214587005))

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha03` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha03` are released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/foundation)

**API Changes**

- `notifyFocusedRect` methods in `TextInputSession` and `TextInputService` are now deprecated and won't be called. Use `BringIntoViewRequester` instead. ([Ia4302](https://android-review.googlesource.com/#/q/Ia4302c5f6ee79eec30a9f42c149da8775e1ed57e), [b/192043120](https://issuetracker.google.com/issues/192043120), [b/216842427](https://issuetracker.google.com/issues/216842427), [b/178211874](https://issuetracker.google.com/issues/178211874))
- Animations were enabled for items of lazy grids with Modifier.animateItemPlacement(). ([Ib6621](https://android-review.googlesource.com/#/q/Ib66210f8959214b5f94fd1fcc49100294cd0e2d6), [b/211753218](https://issuetracker.google.com/issues/211753218))
- `BringIntoViewRequester` now propagates requests to the hosting Android View. ([Ia7a51](https://android-review.googlesource.com/#/q/Ia7a5163a1eeb3e9d2f1623fa280f33cb98d4fb6d))
- `FontFamilyResolver` is now available via `LocalFontFamilyResolver.current`
  - Added `createFontFamilyResolver(context)` and `createFontFamilyResolver(context, coroutineScope)` to create new FontFamily resolvers outside of compose usage.
  - Paragraph and MultiParagraph now take `FontFamily.Resolver`
  - `TextLayoutResult.layoutInput.fontFamilyResolver` now contains the resolver used for this layout, deprecated `TextLayoutResult.layoutInput.resourceLoader` as it is no longer used. ([Id5a45](https://android-review.googlesource.com/#/q/Id5a45c72bb6f33910643ee3da7f81a78dc093d86), [b/174162090](https://issuetracker.google.com/issues/174162090))
- Added `AndroidFont`, a new low-level API for providing new types of font resource descriptors on Android. For example, loading fonts from an app-specific backend, optionally locating pre-installed fonts on-device, or loading a font from a resource not provided by the current Font factories.
  - Expanded `Font.ResourceLoaded` API to support optional and async font loading. It is not recommended that application developers use this API directly. To add new types of fonts see AndroidFont.
  - `Font.AndroidResourceLoader` extension function allows construction of a `Font.ResourceLoader` when outside of composition.
  - Added `loadingStrategy` parameter to resource-based fonts, to allow async loading when resource font references downloadable fonts XML. ([Ie5aea](https://android-review.googlesource.com/#/q/Ie5aeadd2feaf996d2c826d87dd310b8984e106c8), [b/174162090](https://issuetracker.google.com/issues/174162090))
- `Typeface(FontFamily)` constructor is deprecated. This was previously used to preload fonts, which may take up to 10 seconds for downloadable fonts. With downloadable fonts, this call may block for 10 seconds. Instead use `FontFamilyResolver.preload`
  - `fontResource(FontFamily): Typeface` is deprecated. This was previously used to preload fonts, which may take up to 10 seconds for downloadable fonts. Instead use `FontFamilyResolver.preload` ([If8e7c](https://android-review.googlesource.com/#/q/If8e7c6ce7cd64be8094a576587cc1329e19d246f), [b/174162090](https://issuetracker.google.com/issues/174162090))
- You can now specify the content type for the items of `LazyVerticalGrid` - item/items functions on `LazyGridScope` now accept such parameter. Providing such information helps item composition reusing logic to make it more efficiently and only reuse the content between the items of similar type. ([I7b355](https://android-review.googlesource.com/#/q/I7b3550cf626b6ef6f65029b1e55465266bfacb18), [b/215372836](https://issuetracker.google.com/issues/215372836))
- `LazyListLayoutInfo` and `LazyGridLayoutInfo` now have new properties: `viewportSize`, `orientation`, `reverseLayout` ([Ifc8ed](https://android-review.googlesource.com/#/q/Ifc8ed6a22fa14fecb3f6910ef86caa5345e6d5e4), [b/200920410](https://issuetracker.google.com/issues/200920410))
- You can now specify the content type for the items of LazyColumn/LazyRow - item/items functions on LazyListScope now accept such parameter. Providing such information helps item composition reusing logic to make it more efficiently and only reuse the content between the items of similar type. ([I26506](https://android-review.googlesource.com/#/q/I26506a2b3d0049be6ff4decf295e183c5d2b8fc3))
- `SubcomposeLayoutState` constructor accepting `maxSlotsToRetainForReuse` is now deprecated. Instead there is a new constructor accepting `SubcomposeSlotReusePolicy` - a new interface allowing more granular control on what slots should be retained for the future reuse. ([I52c4d](https://android-review.googlesource.com/#/q/I52c4d0360cd987ce03504807312beabdbe410ab0))
- Adds Modifiers for WindowInsets, both for padding and sizing. This allows some content to extend into the inset area, and still have primary content stay out of the inset area. For example, windowInsetsPadding can be used to pad the content area to avoid areas that may be fully or partially covered. ([Id0395](https://android-review.googlesource.com/#/q/Id0395142409b981e92f94fb46ebf1c2ec2540048), [b/213942085](https://issuetracker.google.com/issues/213942085))

**Bug Fixes**

- TextFields will now be kept above the keyboard when they are focused and the keyboard is shown, when the soft input mode is `ADJUST_PAN`. ([I8eaeb](https://android-review.googlesource.com/#/q/I8eaebb684b7828dcf92b0678a86d796b49b349c8), [b/190539358](https://issuetracker.google.com/issues/190539358), [b/192043120](https://issuetracker.google.com/issues/192043120))
- Desktop uses composition local for `FontFamily.Resolver`
  - Desktop `FontLoader` is deprecated
  - New `createFontFamilyResolver` factory on Desktop ([I6bbbb](https://android-review.googlesource.com/#/q/I6bbbb76ece4ca3844f07e2fc22c2e63478bfdd8c), [b/174162090](https://issuetracker.google.com/issues/174162090))
- The soft keyboard input type no longer flickers when changing focus between text fields. ([I1bf50](https://android-review.googlesource.com/#/q/I1bf50cacddd8e20f9bd3d5124f277e5fef467ac0), [b/187746439](https://issuetracker.google.com/issues/187746439))
- Text fields no longer require an extra back press when the cursor handle is showing. ([Ideb4b](https://android-review.googlesource.com/#/q/Ideb4bafc9e7ada3faf16310d96ae4abf0caca734), [b/205726883](https://issuetracker.google.com/issues/205726883))
- Text selection magnifier behavior has been polished to match the platform magnifier. ([Idd918](https://android-review.googlesource.com/#/q/Idd918c3b321e8d7626e47a027e0b19640085a2fa), [b/206833278](https://issuetracker.google.com/issues/206833278))

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha02` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha02` are released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/foundation)

**API Changes**

- Added `NonRestartableComposable` to methods that are overloads of existing methods without complex logic. This reduces compiler generated memoization checks (equals) for all parameters which are repeated in the inner function that is called. ([I90490](https://android-review.googlesource.com/#/q/I90490b1a28bada20840ab59e47245c00c6253d11))
- Added `excludeFromSystemGesture` Modifiers for easy access to Android's `setSystemGestureExclusionRects` ([I46f07](https://android-review.googlesource.com/#/q/I46f0768d06c645f23bba4d056448686976e74fca))

**Bug Fixes**

- Text selection magnifier behavior has been polished to match the platform magnifier. ([Idd918](https://android-review.googlesource.com/#/q/Idd918c3b321e8d7626e47a027e0b19640085a2fa), [b/206833278](https://issuetracker.google.com/issues/206833278))
- `LazyColumn`, `LazyRow`, `Modifier.verticalScroll` and other containers that use `Modifier.scrollable` now support mouse wheel scrolling. ([I2b5e1](https://android-review.googlesource.com/#/q/I2b5e15f480a26878e8dc8727e34d6e7ec660e564), [b/198214718](https://issuetracker.google.com/issues/198214718))

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.foundation:foundation:1.2.0-alpha01` and `androidx.compose.foundation:foundation-layout:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/foundation)

**API Changes**

- New parameter `userScrollEnabled` was added to `LazyColumn`, `LazyRow`, and `LazyVerticalGrid` in order to allow users to temporarily or permanently disable the user initiated scroll via touch gestures or accessibility actions. Scrolling programmatically via the methods on the state will still be allowed. ([I7eae9](https://android-review.googlesource.com/#/q/I7eae94b090ffc56269faea51ce84fe36b0ba9ae5), [b/201150093](https://issuetracker.google.com/issues/201150093))
- Add `onSizeChanged` callback to magnifier modifier. ([I6879f](https://android-review.googlesource.com/#/q/I6879fe3b66f9bfa66abf8401159dc31753f40e9a))
- The magnifier widget now shows when dragging selection handles in a `SelectionContainer`. ([I30b38](https://android-review.googlesource.com/#/q/I30b386701480c51bf711c5d9936e7a5e6b7b5a71), [b/139320979](https://issuetracker.google.com/issues/139320979))

**Bug Fixes**

- Fixes `TextField` cursor handle not hiding when scrolled out of view. ([I14552](https://android-review.googlesource.com/#/q/I145524fd69aa0b27ba572a1b6239d268a6fa5654), [b/208883748](https://issuetracker.google.com/issues/208883748))

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.foundation:foundation:1.1.1` and `androidx.compose.foundation:foundation-layout:1.1.1` are released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/foundation)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.foundation:foundation:1.1.0` and `androidx.compose.foundation:foundation-layout:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/foundation)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
- Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of 48x48dp, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.foundation:foundation:1.1.0-rc03` and `androidx.compose.foundation:foundation-layout:1.1.0-rc03` are released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/foundation)

**Bug Fixes**

- Updated to support Compose Material 1.1.0-rc03

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.foundation:foundation:1.1.0-rc01` and `androidx.compose.foundation:foundation-layout:1.1.0-rc01` are released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/foundation)

**Bug Fixes**

- Now it is allowed to pass negative scroll offsets into `LazyListState.scrollToItem()` and `LazyListState.animateScrollToItem()`. ([Iceb90](https://android-review.googlesource.com/#/q/Iceb907f268a19db3e9315154ebd136764ad975a3), [b/184252837](https://issuetracker.google.com/issues/184252837))
- Fixed a bug that caused missing accessibility scroll actions ([I7cbfb](https://android-review.googlesource.com/#/q/I7cbfb524b5baf98f044ee043ed19b8ad68cc9f89))

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.foundation:foundation:1.1.0-beta04` and `androidx.compose.foundation:foundation-layout:1.1.0-beta04` are released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/foundation)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

**API Changes**

- Cleaned up nullability in `androidx.core.view`([I7078a](https://android-review.googlesource.com/#/q/I7078a577cc3cab983bdf34fae57e962fa734ceb9), [b/204917439](https://issuetracker.google.com/issues/204917439))
- Experimental APIs were added that allow to consume PointerInputchange as a whole or check whether it was consumed or not. ([I2e59d](https://android-review.googlesource.com/#/q/I2e59de430d24336bbdbe3d0a975948969e8d2e82))
- Show a magnifier widget when dragging the cursor or selection handles inside text fields. ([I5391e](https://android-review.googlesource.com/#/q/I5391e3fab709172189dada65e8dba6a130526c15), [b/203781358](https://issuetracker.google.com/issues/203781358))

**Bug Fixes**

- Fix text handles not moving when IME visibility changes. ([I25f2e](https://android-review.googlesource.com/#/q/I25f2ec3b813f179836c6e69c78bbd8ff2a636179))

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.foundation:foundation:1.1.0-beta03` and `androidx.compose.foundation:foundation-layout:1.1.0-beta03` are released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/foundation)

**API Changes**

- Support for horizontal spans was added to LazyVerticalGrid. ([I7e2fa](https://android-review.googlesource.com/#/q/I7e2fa4e915b28aa96980a53c4b9ad79bdb7aeeb2), [b/176758183](https://issuetracker.google.com/issues/176758183))
- Experimental ability to animate Lazy lists item positions was added.
  There is a new modifier available within LazyItemScope called `Modifier.animateItemPlacement()`.
  Usage example:

        var list by remember { mutableStateOf(listOf("A", "B", "C")) }
        LazyColumn {
            item {
                Button(onClick = { list = list.shuffled() }) {
                    Text("Shuffle")
                }
            }
            items(list, key = { it }) {
                Text("Item $it", Modifier.animateItemPlacement())
            }
        }

  - When you provide a key via `LazyListScope.item` or `LazyListScope.items` this modifier will enable item reordering animations. Aside from item reordering all other position changes caused by events like arrangement or alignment changes will also be animated. ([I59e7b](https://android-review.googlesource.com/#/q/I59e7b8fd3a4a9eb19a15a4704da150bd187a6f24), [b/150812265](https://issuetracker.google.com/issues/150812265))

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.foundation:foundation:1.1.0-beta02` and `androidx.compose.foundation:foundation-layout:1.1.0-beta02` are released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/foundation)

**Bug Fixes**

- Ripples and other indications will now only be delayed if they are inside a `Modifier.scrollable()` container, instead of always being delayed for a down event. ([Ibefe0](https://android-review.googlesource.com/#/q/Ibefe01bcdef89e01b6e9f7edf9fe13622450f487), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Added experimental BringIntoView API that lets you send a request to parents so that they scroll to bring an item into view ([Ib918d](https://android-review.googlesource.com/#/q/Ib918da5f0ee21833e6e1c12169dbd308ca33caf5), [b/195353459](https://issuetracker.google.com/issues/195353459))

**External Contribution**

- Added `Modifier.pointerHoverIcon` ([I95f01](https://android-review.googlesource.com/#/q/I95f011f87824926ddc87398a5ad553ca003c6f08))

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.foundation:foundation:1.1.0-beta01` and `androidx.compose.foundation:foundation-layout:1.1.0-beta01` are released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/foundation)

**Bug Fixes**

- Added experimental BringIntoView API that lets you send a request to parents so that they scroll to bring an item into view ([Ib918d](https://android-review.googlesource.com/#/q/Ib918da5f0ee21833e6e1c12169dbd308ca33caf5), [b/195353459](https://issuetracker.google.com/issues/195353459))

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha06` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/foundation)

**API Changes**

- A child-less overload for Layout was added, with improved efficiency ([Ib0d9a](https://android-review.googlesource.com/#/q/Ib0d9a0f11936c0568d20e26a3c6eaa3f938e0ccd))
- `SemanticsNodeInteraction.performSemanticsAction` now returns the `SemanticsNodeInteraction` on which the function was called. ([I9e5db](https://android-review.googlesource.com/#/q/I9e5db630fbc3c254a4cc862c45bae71496e3c99f))
- Added `performScrollToNode(matcher: SemanticsMatcher)` that scrolls a scrollable container to the content that is matched by the given matcher. ([Ic1cb8](https://android-review.googlesource.com/#/q/Ic1cb855e351c7bb683962d618d68782628b70f62))

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha05` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/foundation)

**API Changes**

- Added experimental historical pointers to PointerEventChange. ([Ic1fd8](https://android-review.googlesource.com/#/q/Ic1fd82fd3f2335a9289cc1fc96c35e89ec9b90ee), [b/197553056](https://issuetracker.google.com/issues/197553056), [b/199921305](https://issuetracker.google.com/issues/199921305))

**Bug Fixes**

- Fixed accessibility support for scrollables (both lazy and non-lazy) with respect to scrolling ([I6cdb0](https://android-review.googlesource.com/#/q/I6cdb0e5114faa448deacd4d662893cec43c2d9f0))

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha04` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha04` are released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/foundation)

**API Changes**

- Deprecated `performGesture` and `GestureScope`, which have been replaced by `performTouchInput` and `TouchInjectionScope`. ([Ia5f3f](https://android-review.googlesource.com/#/q/Ia5f3f740c51a1add60fa82189d583d8a5192dd31), [b/190493367](https://issuetracker.google.com/issues/190493367))
- Added `touchBoundsInRoot` to `SemanticsNode` that includes the minimum touch target size so that developers can ensure that touch targets meet accessibility minimums. ([I2e14b](https://android-review.googlesource.com/#/q/I2e14bf1bab7a745aa2421353f44c734540d2489c), [b/197751214](https://issuetracker.google.com/issues/197751214))

**Bug Fixes**

- Support for stretch overscroll has been added on Android 12 devices. ([Iccf3c](https://android-review.googlesource.com/#/q/Iccf3c3830a01469940828e21bc32b569951c187e), [b/171682480](https://issuetracker.google.com/issues/171682480))

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha03` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha03` are released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/foundation)

**New Features**

- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

**API Changes**

- Glow effect for scroll has been added. New experimental OverScrollConfiguration API has been added to allow for configuration of the overscroll visual effect. Provide null to turn off the overscroll effect. ([I0c304](https://android-review.googlesource.com/#/q/I0c3042f89365408e92f657330ed3164e6f3e12f8), [b/171682480](https://issuetracker.google.com/issues/171682480))
- AwaitPointerEventScope now has withTimeout() and withTimeoutOrNull() ([I507f0](https://android-review.googlesource.com/#/q/I507f0e696311ac0504126681c376f73beaa021fb), [b/179239764](https://issuetracker.google.com/issues/179239764), [b/182397793](https://issuetracker.google.com/issues/182397793))
- Added test method to get the clipped bounds. ([I6b28e](https://android-review.googlesource.com/#/q/I6b28e437d6893a63be65c8a451a84bcb21bce906))
- Added minimum touch target size to ViewConfiguration for use in semantics and pointer input to ensure accessibility. ([Ie861c](https://android-review.googlesource.com/#/q/Ie861ca1fcdbfcc9455352fc3a459d5734d5d57cc))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha02` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/foundation)

**API Changes**

- Added DpSize versions for `Modifier.size` and `requiredSize` ([I3fc7e](https://android-review.googlesource.com/#/q/I3fc7e0a9bd9989a8217ccc2ecf9aaea047693e1d), [b/194219828](https://issuetracker.google.com/issues/194219828))

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.foundation:foundation:1.1.0-alpha01` and `androidx.compose.foundation:foundation-layout:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/foundation)

**API Changes**

- Updated `DrawScope#drawImage` method that consumes source and destination rects to consume an optional FilterQuality parameter. This is useful for pixel art that is intended to be pixelated when scaled up for pixel based art. Updated BitmapPainter + Image composable to also consume an optional FilterQuality parameter ([Ie4fb0](https://android-review.googlesource.com/#/q/Ie4fb04013701add0fba1c5c6bb9da2812d6436e7), [b/180311607](https://issuetracker.google.com/issues/180311607))
- TextField now clears selection when back button is pressed, which matches Android EditText behavior. ([I3ca16](https://android-review.googlesource.com/#/q/I3ca164d09ee6d82f292aacfd2df0af05643cb1aa), [b/174173645](https://issuetracker.google.com/issues/174173645))
- Add Cursor Handle. ([I07a82](https://android-review.googlesource.com/#/q/I07a8217c8ecbcd1c84c1a8df20c6e8b07d409148), [b/173016579](https://issuetracker.google.com/issues/173016579))

**Bug Fixes**

- Scrolling via semantics actions for lazy lists and regular scrolling components is now animated ([Id9066](https://android-review.googlesource.com/#/q/Id9066420fd80bbea3c0463813be0338fff017514), [b/190742024](https://issuetracker.google.com/issues/190742024))

**External Contribution**

- `LazyVerticalGrid` now accepts both horizontal and vertical arrangement parameters. ([If9c92](https://android-review.googlesource.com/#/q/If9c929e4d44f1c5e55184e426b62ab4b41c76ff6))

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.foundation:foundation:1.0.5` and `androidx.compose.foundation:foundation-layout:1.0.5` are released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/foundation)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.foundation:foundation:1.0.4` and `androidx.compose.foundation:foundation-layout:1.0.4` are released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/foundation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.foundation:foundation:1.0.3` and `androidx.compose.foundation:foundation-layout:1.0.3` are released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/foundation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.foundation:foundation:1.0.2` and `androidx.compose.foundation:foundation-layout:1.0.2` are released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/foundation)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.foundation:foundation:1.0.1` and `androidx.compose.foundation:foundation-layout:1.0.1` are released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/foundation)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.foundation:foundation:1.0.0` and `androidx.compose.foundation:foundation-layout:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/foundation)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

**Known Issues**

- If you are using Android Studio Bumblebee Canary 4 or AGP `7.1.0-alpha04`/`7.1.0-alpha05`, you may hit the following crash:

        java.lang.AbstractMethodError: abstract method "void androidx.lifecycle.DefaultLifecycleObserver.onCreate(androidx.lifecycle.LifecycleOwner)"

  To fix, temporarily increase your minSdkVersion to 24+ in your `build.gradle` file. This issue will be fixed in the next version of Android Studio Bumblebee and AGP `7.1`. ([b/194289155](https://issuetracker.google.com/issues/194289155))

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.foundation:foundation:1.0.0-rc02` and `androidx.compose.foundation:foundation-layout:1.0.0-rc02` are released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/foundation)

- Updated border rendering for generic shapes to address issues with paths defined with fixed dimensions. ([aosp/1748871](https://android-review.googlesource.com/c/platform/frameworks/support/+/1748871), [b/191817116](https://issuetracker.google.com/issues/191817116))

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.foundation:foundation:1.0.0-rc01` and `androidx.compose.foundation:foundation-layout:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/foundation)

**API Changes**

- Canvas now supports a contentDescription parameter for accessibility. ([Ib547c](https://android-review.googlesource.com/#/q/Ib547c8fdb4c76a64f5ddcfe8ef3d46a0792f40bc))

**Bug Fixes**

- Disabled Button, Card, Checkboxes and overall `Modifier.clickable(enabled=false)` will block clicks from going up to the parent. ([Ic2c3b](https://android-review.googlesource.com/#/q/Ic2c3b17121c3ab4676a995c4a83d15bac6c16aaa), [b/183908811](https://issuetracker.google.com/issues/183908811))

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.foundation:foundation:1.0.0-beta09` and `androidx.compose.foundation:foundation-layout:1.0.0-beta09` are released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/foundation)

**API Changes**

- Removed `ManualFrameClock`. If you need to control animations, use `composeTestRule.mainClock` instead. ([I3c3e8](https://android-review.googlesource.com/#/q/I3c3e8d0387c37ab3f3a29b648429056ac0eb6b26), [b/189951065](https://issuetracker.google.com/issues/189951065))
- change enum Role and LiveRegionMode to inline classes with private constructor ([Id1890](https://android-review.googlesource.com/#/q/Id189080b0537dde66639fc87f08ec5f46a449a97))
- KeyboardCapitalization is converted into inline class. ([Id5a1c](https://android-review.googlesource.com/#/q/Id5a1c8b2c89a65eb41aa44675b960a3bb0dc1020))
- TextOverflow is changed to an inline class. ([I433af](https://android-review.googlesource.com/#/q/I433af65606ae4e79ea0cb281be7049c73b12fcf0))

**Bug Fixes**

- Now when you specify the unique keys for LazyColumn/Row items the scroll position will be maintained based on the key, which means if you add/remove items before the current visible item the item with the given key will be kept as the first visible one. ([Id263f](https://android-review.googlesource.com/#/q/Id263f45e44fbcd5a6112ef88848da3303705c460), [b/184257857](https://issuetracker.google.com/issues/184257857))
- Key constants are @ExperimentalComposeUiApi for now. Consuming code can declare private constants prior to stabilization. ([Ia5d48](https://android-review.googlesource.com/#/q/Ia5d48d518c6e73f5e3458260203dc237bef5464d))
- Added IdlingStrategy to AndroidComposeTestRule that can be used by testing frameworks to install an alternative mechanism to await or achieve quiescence. Use `AndroidComposeTestRule.setIdlingStrategyFactory()` before your test starts to install your own strategy. ([I608fa](https://android-review.googlesource.com/#/q/I608fa541ffd0bfff6b847e873843df0701425529))

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

`androidx.compose.foundation:foundation:1.0.0-beta08` and `androidx.compose.foundation:foundation-layout:1.0.0-beta08` are released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/foundation)

**API Changes**

- NestedScrollSource enum is replaced by an inline class. ([Ie321b](https://android-review.googlesource.com/#/q/Ie321b5864dc617b2d6382ba5d632e8037dd5c1d5), [b/187055290](https://issuetracker.google.com/issues/187055290))
- Refactored enum usages to inline classes to avoid issues with exhaustive when statements when new enum values are added. ([I2b5eb](https://android-review.googlesource.com/#/q/I2b5eb2f04d64d1eccf38557d80e3eef06869c310))
- Adds a tap timeout to clickable / toggleable to prevent showing a ripple during a scroll / drag ([Ia2704](https://android-review.googlesource.com/#/q/Ia27044999597dd9411344119a7b77180943d9a25), [b/168524931](https://issuetracker.google.com/issues/168524931))
- ContentDescription and Text semantics properties are no longer single values but lists. This enables to merge them as they are instead of concatenations. Also provided better testing APIs to utilize these changes ([Ica6bf](https://android-review.googlesource.com/#/q/Ica6bf4236d05b97357c18fb306a6305877a349f7), [b/184825850](https://issuetracker.google.com/issues/184825850))
- `Modifier.focusModifier()` is deprecated and replaced by `Modifier.focusTarget()` ([I6c860](https://android-review.googlesource.com/#/q/I6c860991217cc0c4e7cb35be73207f94669ce607))
- KeyboardType enum is replaced by an inline class. ([I73045](https://android-review.googlesource.com/#/q/I73045de306c082ca8f6b11d44d252d0a63a407d3), [b/187055290](https://issuetracker.google.com/issues/187055290))
- Replaced `FocusState` enum with a `FocusState` interface ([Iccc1a](https://android-review.googlesource.com/#/q/Iccc1a7306fe886969b3a5c74359f53250b3901d9), [b/187055290](https://issuetracker.google.com/issues/187055290))
- ImeAction enum is replaced by an inline class. ([I18be5](https://android-review.googlesource.com/#/q/I18be51ba64f20257859ae634720b367ae7510e33), [b/187055290](https://issuetracker.google.com/issues/187055290))
- `AnnotatedString.withAnnotation` functions are now ExperimentalTextApi instead of ExperimentalComposeApi. ([I0cd0a](https://android-review.googlesource.com/#/q/I0cd0a64f5e0bf4cd082d479711c014162f27c763))
  - TextUnit constructor with TextUnitType is now ExperimentalTextApi instead of ExperimentalComposeApi.
- PaddingValues is now `@Stable` rather than `@Immutable` ([I88c50](https://android-review.googlesource.com/#/q/I88c506cf737fdb19d99fc495ab343395c3b23e01))

**Bug Fixes**

- Fix crashes of long press the blank area in non-empty text. ([I33ab5](https://android-review.googlesource.com/#/q/I33ab5d732fc3564ec4fe99b16234a980f51684a8), [b/187437299](https://issuetracker.google.com/issues/187437299))
- Show Toolbar after SelectAll ([I495d9](https://android-review.googlesource.com/#/q/I495d9fdb7c7e01cfd6085748cb5116e106906bb8), [b/185919613](https://issuetracker.google.com/issues/185919613))
- Fix for scrollable containers clipping its children on the cross axis. It was easily reproducible if you have a LazyRow with Card items. now the shadow will not be clipped. ([Icb635](https://android-review.googlesource.com/#/q/Icb6356d8dac24720981caa6afe8785546a2e7847), [b/186318448](https://issuetracker.google.com/issues/186318448))
- Fixed an issue where ripples / other indication would sometimes get stuck on a long click when using Modifier.combinedClickable ([I2298c](https://android-review.googlesource.com/#/q/I2298ce564e3940875c3f3525255424da25dc9414), [b/186223077](https://issuetracker.google.com/issues/186223077))
- Now `detectDragGesures`, `detectVerticalGestures`, and `detectHorizontalGestures` will consume the position change automatically, no need to call change.consumePositionChange in the onDrag callbacks ([I42fc4](https://android-review.googlesource.com/#/q/I42fc4a6529f73db228ae671097d10a0cda0d834b), [b/185096350](https://issuetracker.google.com/issues/185096350), [b/187320697](https://issuetracker.google.com/issues/187320697))
- `Modifier.onGloballyPositioned()` was changed to report the coordinates of this modifier in the modifier chain, not the layout coordinates after applying all the modifiers. This means that now the ordering of modifiers is affecting what coordinates would be reported. ([Ieb67d](https://android-review.googlesource.com/#/q/Ieb67da0c327c9dc323a4b0a8bf33dbb66f0611e3), [b/177926591](https://issuetracker.google.com/issues/177926591))

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.foundation:foundation:1.0.0-beta07` and `androidx.compose.foundation:foundation-layout:1.0.0-beta07` are released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/compiler/compiler)
| **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
| `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

**API Changes**

- The next visible item prefetching logic is introduced for LazyColumn/Row ([I8a4bc](https://android-review.googlesource.com/#/q/I8a4bc52322a5444e3782274822fa6d07f7c1d402), [b/184940225](https://issuetracker.google.com/issues/184940225))
- Added Clip Selection Handle ([Iff80d](https://android-review.googlesource.com/#/q/Iff80d27fbac0e4de5e3e99fac4352cd6ef2cd201), [b/183408447](https://issuetracker.google.com/issues/183408447))

**Bug Fixes**

- LazyColumn/Row will now keep up to 2 previously visible items active (not disposed) even when they are scrolled out already. This allows the component to reuse the active subcompositions when we will need to compose a new item which improves the scrolling performance. ([Ie5555](https://android-review.googlesource.com/#/q/Ie5555c9a7031dc9bd31f452a0ed9b28d8a337f5f))
- Remove paintBackground. ([I38660](https://android-review.googlesource.com/#/q/I3866020fa1fe7331604d144dcffc1ed3a0e56f50))
- Draw Selection Background using DrawScope. ([I73c61](https://android-review.googlesource.com/#/q/I73c61bfd553fca38c412d9372e3eaa6336dcd74f), [b/186674472](https://issuetracker.google.com/issues/186674472))
- A beta06 regression affecting Row/Column using spacedBy arrangements to layout weighted children was fixed. ([Ifaf8c](https://android-review.googlesource.com/#/q/Ifaf8c6180000d06e1aaa89553ff60e82638e9465), [b/187326588](https://issuetracker.google.com/issues/187326588))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.foundation:foundation:1.0.0-beta06` and `androidx.compose.foundation:foundation-layout:1.0.0-beta06` are released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/foundation)

**API Changes**

- Solve Conflict with Navigation Gesture ([I1145e](https://android-review.googlesource.com/#/q/I1145eacbec270abcbb70f8ccb3664609a699ee47))
- Added CollectionInfo and CollectionItemInfo accessibility APIs that allows to mark collection and its items for accessibility services ([Id54ef](https://android-review.googlesource.com/#/q/Id54ef37379e14e41ac52782b40e29de54f95eed0), [b/180479017](https://issuetracker.google.com/issues/180479017))
- Added `SemanticsActions.ScrollToIndex` to scroll a list with indexed items to the item with a certain index, and `SemanticsProperties.IndexForKey` to get the index of an item in a list with keyed items. Both actions are implemented by LazyList.
  - Added `SemanticsNodeInteraction.performScrollToIndex` that scrolls a list to the given index, and `SemanticsNodeInteraction.performScrollToKey` that scrolls a list to the item with the given key. ([I4fe63](https://android-review.googlesource.com/#/q/I4fe63399fb620794651e1973730658877bcfeff4), [b/178483889](https://issuetracker.google.com/issues/178483889), [b/161584524](https://issuetracker.google.com/issues/161584524))
- AnnotatedString save support to TextFieldValue.Saver. Added addTtsAnnotation and withAnnotation utility functions to AnnotatedString.Builder ([I8cbdc](https://android-review.googlesource.com/#/q/I8cbdcfcdbe167ff7c68c760aebdd8affe2d8434e), [b/178446304](https://issuetracker.google.com/issues/178446304))
- Default `0.dp` parameter values were added to `PaddingValues(horizontal, vertical)` ([I05571](https://android-review.googlesource.com/#/q/I0557182c68da793da30caeb6325949829101e0cf), [b/181336792](https://issuetracker.google.com/issues/181336792))

**Bug Fixes**

- Row \& Column children with `weight(fill = false)` are no longer making the parent fill the entire available main axis space. ([Ied94d](https://android-review.googlesource.com/#/q/Ied94da682f4cf6ead5b91e06ba08904c1a349b9f), [b/186012444](https://issuetracker.google.com/issues/186012444), [b/184355105](https://issuetracker.google.com/issues/184355105))

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.foundation:foundation:1.0.0-beta05` and `androidx.compose.foundation:foundation-layout:1.0.0-beta05` are released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/compose/foundation)

**API Changes**

- FlingBehavior interface is now marked as @Stable. All implementations should comply with the `@Stable` contract. ([I93354](https://android-review.googlesource.com/#/q/I93354d661af9074ad27fc37ff623f83b03e4f36c), [b/184830577](https://issuetracker.google.com/issues/184830577))

**Bug Fixes**

- Fixed `ACTION_SCROLL_FORWARD`, `ACTION_SCROLL_BACKWARD`, `accessibilityActionScrollLeft`, `accessibilityActionScrollUp`, `accessibilityActionScrollRight` and `accessibilityActionScrollDown` accessibility scroll actions. Instead of scrolling to the end of the scrollable, it will now scroll by one screen in the given direction. ([Ieccb0](https://android-review.googlesource.com/#/q/Ieccb0a794d61dc5fe28a236b379755d776c023dc))
- The AndroidManifest files from ui-test-manifest and ui-tooling-data are now compatible with Android 12 ([I6f9de](https://android-review.googlesource.com/#/q/I6f9dec0515ad6eb7fd232eeb124ee0164f4e90cb), [b/184718994](https://issuetracker.google.com/issues/184718994))

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.foundation:foundation:1.0.0-beta04` and `androidx.compose.foundation:foundation-layout:1.0.0-beta04` are released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/foundation)

**API Changes**

- Rename hideSoftwareKeyboard and showSoftwareKeyboard on SoftwareKeyboardController to `hide()` and `show()` respectively.
  - Provide the full CompositionLocal interface for LocalSoftwareKeyboardController, allowing it to be set (especially useful in tests) ([I579a6](https://android-review.googlesource.com/#/q/I579a6e311d1cc96e4ea398465cad3a402a633b8d))
- `TextOverflow.Visible` is introduced. ([Ic8f89](https://android-review.googlesource.com/#/q/Ic8f898df15fa7cfa3fadf5a47d5b0e34a68f52f6))
- Public instances of `RowScope`, `ColumnScope`, `BoxScope`, `BoxWithConstraintsScope` were removed. ([I4e83e](https://android-review.googlesource.com/#/q/I4e83e38b3bb85be593288720e6b9cdbe0032bceb), [b/181869067](https://issuetracker.google.com/issues/181869067))

**Bug Fixes**

- Fixed the issue when items of `LazyColumn`/`LazyRow` located on the edges were incorrectly positioned after fast fling ([Ie4d13](https://android-review.googlesource.com/#/q/Ie4d13def7dc4b12d4f52b4c5edbb0abb5150f698), [b/183877420](https://issuetracker.google.com/issues/183877420))
- Prior to this change, local composable functions were skippable based on their parameters. After this change, no local composable functions will skip. This change is done because it is common and expected for local functions to capture parameters from the parent and them skipping is a common source of bugs.

  To summarize, consider the example:

      @Composable fun Counter(count: Int, onCountChange: (Int) -> Unit) {
        @Composable fun ShowCount() { Text("Count: $count") }
        ShowCount()
        Button(onClick={ onCountChange(count + 1) }) {
          Text("Increment")
        }
      }

  Prior to this change, the `ShowCount` composable function would always skip, even after the `count` parameter was updated. This is no longer the case. ([I5648a](https://android-review.googlesource.com/#/q/I5648a5f11c89e71c6b8c748f111c47bcafee9178))

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.foundation:foundation:1.0.0-beta03` and `androidx.compose.foundation:foundation-layout:1.0.0-beta03` are released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/foundation)

**API Changes**

- `DefaultMonotonicFrameClock` is deprecated. Calling `withFrameNanos` or `Recomposer.runRecomposeAndApplyChanges` with no `MonotonicFrameClock` will now throw `IllegalStateException`. ([I4eb0d](https://android-review.googlesource.com/#/q/I4eb0d7a8ebae7497735d25bc35e9f94c66ce2232))

**Bug Fixes**

- `FlingBehavior.performFling()` is now called even when velocity is 0 ([I0b6e5](https://android-review.googlesource.com/#/q/I0b6e5934c646494c1b96340c0f9822d28b9cd2c2), [b/181237123](https://issuetracker.google.com/issues/181237123))

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.foundation:foundation:1.0.0-beta02` and `androidx.compose.foundation:foundation-layout:1.0.0-beta02` are released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/foundation)

**API Changes**

- Multiple small optimizations in LazyColumn measuring logic were added ([Ic6889](https://android-review.googlesource.com/#/q/Ic6889648c8192f400dabce375d87bdfad50a6f96))
- Added new `LocalSoftwareKeyboardController` composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I5951e](https://android-review.googlesource.com/#/q/I5951e802fbec7c26862b976de64b78640accd1f7), [b/168778053](https://issuetracker.google.com/issues/168778053))
- Added new `LocalSoftwareKeyboardController` composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I84472](https://android-review.googlesource.com/#/q/I84472a517db4b15345302346c967e7c6b359109b), [b/168778053](https://issuetracker.google.com/issues/168778053))

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.foundation:foundation:1.0.0-beta01` and `androidx.compose.foundation:foundation-layout:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/foundation)

This is the first release of Compose 1.0.0 Beta.

**API Changes**

- onStart callback has been added to `detectDragGestures` ([I67269](https://android-review.googlesource.com/#/q/I6726950322c7a3390fc79c630919b002bf7059eb), [b/179995594](https://issuetracker.google.com/issues/179995594))
- Modifiers for sizing to intrinsics are no longer experimental. ([I15744](https://android-review.googlesource.com/#/q/I15744bc96d9c9a94747901e47100fdea25e28742))
- Removed dp assertions ([I798d2](https://android-review.googlesource.com/#/q/I798d2f7dbd5e687d8e1fb059f153cdc8150d8d27))
- Removed SoftwareKeyboardController callback from all text fields to be replaced by a new API shortly. ([Iae869](https://android-review.googlesource.com/#/q/Iae869e91c48300f4ab926dac2578d2d759f5fd89), [b/168778053](https://issuetracker.google.com/issues/168778053))
- MeasureBlocks was renamed to MeasurePolicy which became a fun interface. Layout APIs were updated / simplified to use MeasurePolicy. ([Icab48](https://android-review.googlesource.com/#/q/Icab485f5b5965261ce9f9d696d4c225ec158f072), [b/167662468](https://issuetracker.google.com/issues/167662468), [b/156751158](https://issuetracker.google.com/issues/156751158))
- `InteractionState` has been replaced with `[Mutable]InteractionSource`
  - Interfaces are responsible for emitting / collecting Interaction events.
  - Instead of passing `interactionState = remember { InteractionState() }` to components such as `Button` and `Modifier.clickable()`, use `interactionSource = remember { MutableInteractionSource() }`.
  - Instead of: `Interaction.Pressed in interactionState` you should instead use the extension functions on InteractionSource, such as InteractionSource.collectIsPressedAsState().
  - For complex use cases you can use InteractionSource.interactions to observe the stream of Interactions. See the InteractionSource documentation and samples for more information.
  - ([I85965](https://android-review.googlesource.com/#/q/I85965d0dba39d1740c097915d1d1a367eea2a78c), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/171913923](https://issuetracker.google.com/issues/171913923), [b/171710801](https://issuetracker.google.com/issues/171710801), [b/174852378](https://issuetracker.google.com/issues/174852378))
- Removed deprecated LayoutCoordinates methods, use function instead of the property for positionInParent and boundsInParent ([I580ed](https://android-review.googlesource.com/#/q/I580edba74283600c3aafba6130a7af806df7d6c5), [b/169874631](https://issuetracker.google.com/issues/169874631), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Created new TextInputSession for input sessions from low level text components such as CoreTextField. ([I8817f](https://android-review.googlesource.com/#/q/I8817f81e7c1b0066795ecb4af3674e99413362d0), [b/177662148](https://issuetracker.google.com/issues/177662148))
- Placeable now exposes measuredSize, representing the size which the child layout actually measured to. This size might not respect the measurement constraints. ([Ib2729](https://android-review.googlesource.com/#/q/Ib2729a2323f67d5e50248dbfa234394fb3d7ee71), [b/172560206](https://issuetracker.google.com/issues/172560206), [b/172338608](https://issuetracker.google.com/issues/172338608))
- Add selectionGroup modifier that allows to mark collection of Tabs or RadioButtons for accessibility purposes ([Ie5c29](https://android-review.googlesource.com/#/q/Ie5c29bc1cc0630f4f3a68ff57ebd94464c89ffd7))
- Add LazyListState.animateScrollToItem

  This method smooth scrolls to a specific item in the list. ([I4bfd7](https://android-review.googlesource.com/#/q/I4bfd722f76c600483b41d27164eae10e24cc1454))
- ScrollableState.smoothScrollBy() was renamed to animateScrollBy()
  LazyListState.snapToItemIndex() was renamed to scrollToItem()
  ScrollState.smoothScrollTo() was renamed to animateScrollTo() ([I35ded](https://android-review.googlesource.com/#/q/I35deda2585dafb47c8b4d68fc0063d289f5c78d6))

- Modifier.zoomable has been replaced my Modifier.transformable. smoothPanBy, smoothRotationBy have been added as a functionality. ([Ifc32b](https://android-review.googlesource.com/#/q/Ifc32b264ce6a99e17f38ac339bde498fe5b2337a), [b/175294473](https://issuetracker.google.com/issues/175294473))

- The `defaultFactory` for `compositionLocalOf` and
  `staticCompositionLocalOf` is now required instead of
  optional.

  This changes removes a potential type error for non-nullable
  types where no default factory was provided. Previously this
  would provide a null reference for a non-nullable type.

  For nullable types consider supplying `{ null }` as the default
  factory.

  We do not recommend using locals with non-nullable types unless
  a sensible default can be provided. If no sensible default exists,
  the `defaultFactory` lambda should throw an exception. However
  throwing an exception means that consumers of the local will have
  an implicit dependency on it being provided that is not enforced
  by the type system. ([Ifbd2a](https://android-review.googlesource.com/#/q/Ifbd2a8abd2f1fc4578da4b782b570ed9de088beb))
- Changed `Indication#createIndication()` to `Indication#rememberUpdatedIndication(InteractionState)` and removes `InteractionState` parameter from I`ndicationInstance#drawIndication()`. IndicationInstance should only be responsible for drawing visual effects, and not launching animations / writing state in response to InteractionState changes. These animations and state writes should happen within `rememberUpdatedIndication()` instead. The `indication` parameter in `Modifier.indication` was also changed to be a required parameter. ([Ic1764](https://android-review.googlesource.com/#/q/Ic1764c0417b25cd0a0dbb96ed3e1b0974618c4ca), [b/152525426](https://issuetracker.google.com/issues/152525426))

- Text actions now check focus automatically ([I13777](https://android-review.googlesource.com/#/q/I13777ef805c71674b929577a3b794d655948da3f), [b/179648629](https://issuetracker.google.com/issues/179648629))

- Removed `runBlockingWithManualClock` ([I15cdc](https://android-review.googlesource.com/#/q/I15cdc97a742c764cae3b332ad52143c07f32b9bd), [b/179664814](https://issuetracker.google.com/issues/179664814))

- Scroll position in Modifier.verticalScroll()/horizontalScroll() is represented with Ints now ([I81298](https://android-review.googlesource.com/#/q/I81298a8767a421293ca7d5ab33ce8373e63f383c))

- smoothScrollBy and scrollBy methods' packages changed to `androidx.compose.foundation.gestures.*` ([I3f7c1](https://android-review.googlesource.com/#/q/I3f7c18be72b1b4e8d7958194b10d63d749f7d948), [b/175294473](https://issuetracker.google.com/issues/175294473))

- FlingConfig has been renamed to FlingBehavior now allows for customization of suspend animation rather than predefined Decays. ([I02b86](https://android-review.googlesource.com/#/q/I02b8639c646d24fd19ef7ac504ef6660b8906d54), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Size modifiers were renamed. Modifier.width/height/size were renamed to requiredWidth/requiredHeight/requiredSize. Modifier.preferredWidth/preferredHeight/preferredSize were renamed to width/height/size. ([I5b414](https://android-review.googlesource.com/#/q/I5b4145953d360b1fb851c0056fc9a7875bb34088))

- defaultMinSizeConstraints was renamed to defaultMinSize. ([I4eaae](https://android-review.googlesource.com/#/q/I4eaaec7cb1fffdb530744c7b7e42f23a26e96493))

- Modifier.tapGestureFilter has been removed. Use `Modifier.pointerInput { detectTapGestures(...) }` instead. ([I266ed](https://android-review.googlesource.com/#/q/I266ed741ca484924409a4a3a7d5afbbfffbd66d3), [b/175294473](https://issuetracker.google.com/issues/175294473))

- partial consumption was removed from pointer input system. The recommended way of coordinating partial consumtion is Modifier.nestedScroll. ([Ie9c9b](https://android-review.googlesource.com/#/q/Ie9c9b7c6f5da9a47c803b06985f45eb7df5552f2))

- Orientation has been moved to foundation package. VelocirtTracker moved from ui.gesture to ui.input.pointer. ([Iff4a8](https://android-review.googlesource.com/#/q/Iff4a887648735c4850dca0d8d95fd99d782d04bb), [b/175294473](https://issuetracker.google.com/issues/175294473))

- AnimationClockObservable and subclasses have been
  removed. AnimatedFloat has been removed. ([Icde52](https://android-review.googlesource.com/#/q/Icde5248072620b741bdf4d8cf59291e7b2994e6a), [b/177457083](https://issuetracker.google.com/issues/177457083))

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

- requiredWidth(IntrinsicSize) and requiredHeight(IntrinsicSize) modifiers were added for required sizing to intrinsic sizes. ([I0a6b4](https://android-review.googlesource.com/#/q/I0a6b4fc2f6e18c9ff160c94f67fcc6059cd4e2de))

- Deprecated `emptyContent()` is removed. Use `{}` instead. ([Idb33f](https://android-review.googlesource.com/#/q/Idb33f22d9a1002f86b42606dd93478ee37924445), [b/179432510](https://issuetracker.google.com/issues/179432510))

- Deleted some previously deprecated APIs ([Ice5da](https://android-review.googlesource.com/#/q/Ice5dae36591015a9d905b84b26cc02662385d831), [b/178633932](https://issuetracker.google.com/issues/178633932))

**Bug Fixes**

- Added new LocalSoftwareKeyboardController composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I658b6](https://android-review.googlesource.com/#/q/I658b6bfc5c917db486c631312e3456469a615831), [b/168778053](https://issuetracker.google.com/issues/168778053))

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.foundation:foundation:1.0.0-alpha12` and `androidx.compose.foundation:foundation-layout:1.0.0-alpha12` are released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/foundation)

**API Changes**

- Modifier.pointerInput now requires remember keys to indicate when the pointer input detection coroutine should restart for new dependencies. ([I849cd](https://android-review.googlesource.com/#/q/I849cd63912b2d4c86ebe0dd24a7d0e2eb7a4e6d1))
- Testing update: hasText() will check for both input and label/hint/placeholder texts in the text field ([Iab803](https://android-review.googlesource.com/#/q/Iab8030e3c98f05bd6f0ffaf203b8c15acab513bb))
- PaddingValues.Absolute was added and can be used in APIs accepting PaddingValues. ([Ia5f30](https://android-review.googlesource.com/#/q/Ia5f30058d0e5e9549132cdad9b1611a20c975359))
- onImeActionPerformed is deprecated. use KeyboardActions instead ([If0bbd](https://android-review.googlesource.com/#/q/If0bbda1241018d4c19b5df3cd1811c38cce4a76d), [b/179071523](https://issuetracker.google.com/issues/179071523))
- In order to better match naming conventions with ImageBitmap and ImageVector, ImagePainter has been renamed to BitmapPainter to parallel VectorPainter. ([Iba381](https://android-review.googlesource.com/#/q/Iba3810ae5cfd6f57442154c93eec500f35ba4ad5), [b/174565889](https://issuetracker.google.com/issues/174565889))
- Better substring test APIs with substring now as an argument ([Icbe78](https://android-review.googlesource.com/#/q/Icbe78369fe75bc01bfcfa25b8e9ee2ad148fdb96))
- Introduced an `InfiniteAnimationPolicy` coroutine context element that will be applied in infinite animations. By default no policy is installed, except when running tests with `ComposeTestRule`. ([I50ec4](https://android-review.googlesource.com/#/q/I50ec421d7db495459a61c9282dbc2bfbc1f1ad02), [b/151940543](https://issuetracker.google.com/issues/151940543))
- Animatable.snapTo and Animatable.stop are now suspend functions ([If4288](https://android-review.googlesource.com/#/q/If42887504caa0a07a0d89477805b68ca51c9b3b4))
- ComponentActivity.setContent has moved to androidx.activity.compose.setContent in the androidx.activity:activity-compose module. ([Icf416](https://android-review.googlesource.com/#/q/Icf4168e6078b87ce746569a946b2a90274197c72))
- Destructuring and copy() methods have been removed from several classes where they were rarely used. ([I26702](https://android-review.googlesource.com/#/q/I267021d3a45314acc9a169f6bbdfbfb4295a448c), [b/178659281](https://issuetracker.google.com/issues/178659281))
- Custom keys support for LazyColumn/LazyRow was added. This allows us to smarter handle items reordering. So the state you stored in remember {} blocks will move together with the item when you reorder elements or removed the item from the middle.

      LazyColumn {
          items(users, key = { user -> user.id }) { ... }
      }

  - ([Ia50ef](https://android-review.googlesource.com/#/q/Ia50ef7cd8f47ab87d76edc4e0691199ce426729d), [b/164901852](https://issuetracker.google.com/issues/164901852))
- Changed Indication#createInstance to be @Composable, and changed LocalIndication to contain an Indication, not () -\> Indication. ([I5eeea](https://android-review.googlesource.com/#/q/I5eeea2424e4deda6116f0b48b690b628f8d545eb), [b/157150564](https://issuetracker.google.com/issues/157150564))

- `Constraints.enforce` was replaced with `Constraints.constrain`. ([I8b8ea](https://android-review.googlesource.com/#/q/I8b8ea7898b09ccaa411b9b6ef20a16523e8ba029))

- loadFontResource is deprecated. Use fontResource instead.
  imageResource, loadImageResource, vectorResource, and loadVectorResource
  are deprecated. Use painterResource instead. ([I6b809](https://android-review.googlesource.com/#/q/I6b8096508b2280ca49c70a432c5497f386dc570e))

- For performance reasons, ScrollAxisRange semantics now takes
  lambdas returning Floats instead of direct Float values. ([If4a35](https://android-review.googlesource.com/#/q/If4a353ef9ac511ce77cf334ccf9a589ecadcac56), [b/178657186](https://issuetracker.google.com/issues/178657186))

- Added EditableText semantics to mark editable input text of the text field for accessibility and corresponding test methods to check the semantics ([I8e07a](https://android-review.googlesource.com/#/q/I8e07ab8a8f29d5c2a31fb1c979e099303083a38f))

- Modifier.clickable now doesn't have double and long click support. Use Modifier.combinedClickable to achieve this functionality. ([Iafad1](https://android-review.googlesource.com/#/q/Iafad17bbdb5029ce413bce94cd47f7c5233cb67b))

- toIntPx() was renamed to roundToPx(). ([I9b7e4](https://android-review.googlesource.com/#/q/I9b7e460fb4b6e72ba65cdd8f5d1165c306461773), [b/173502290](https://issuetracker.google.com/issues/173502290))

- IntBounds was renamed to IntRect and the API was improved. ([I1f6ff](https://android-review.googlesource.com/#/q/I1f6ff3831e502856f1550ede9c367bf05c5a51b1))

- Modifier.dragGestureFilter has been deprecated. Use `Modifier.pointerInput { detectDragGestures (...)}` instead. Alternatively, use Modifier.draggable for one axis drags ([I0ba93](https://android-review.googlesource.com/#/q/I0ba93559f565fc2a277f322e53dce9df9855ea46), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Renamed Ambients to match the Ambient -\> CompositionLocal rename. Ambients used to be named AmbientFoo, now CompositionLocals are named LocalFoo. ([I2d55d](https://android-review.googlesource.com/#/q/I2d55d1c5c38a08b04e72a569d3079db4feca1bf7))

- Selection was moved to foundation. ([I7892b](https://android-review.googlesource.com/#/q/I7892b8be5d2f91849f8ecc2e1034e0a8277bb61c))

- Similarly to how we previously removed `state { 0 }` composable and now promote usage like `remember { mutableStateOf(0) }` we are going to remove `savedInstanceState { 0 }` composable. You should use `rememberSaveable { mutableStateOf(0) }` instead and it will save and restore automatically if the type used inside the MutableState can be stored in the Bundle. If previously you were passing a custom saver object now you need to use a new overload of rememberSaveable which has the `stateSaver` parameter. The usage will look like this: `val holder = rememberSaveable(stateSaver = HolderSaver) { mutableStateOf(Holder(0)) }` ([Ib4c26](https://android-review.googlesource.com/#/q/Ib4c266902d166f119ea1770cccbc78ac25a54ff7), [b/177338004](https://issuetracker.google.com/issues/177338004))

- Added password semantics for accessibility ([I231ce](https://android-review.googlesource.com/#/q/I231ce1c1e9c781c8ec8fda5536d8a0588d68755d))

- Added ProgressBarRangeInfo.Indeterminate to mark indeterminate progress bars for accessibility ([I6fe05](https://android-review.googlesource.com/#/q/I6fe052ba60861d64f31963507ff11e95f3331d89))

- Playtime in animation is now unfiied to nanoseconds ([If776a](https://android-review.googlesource.com/#/q/If776ab3406909ddf6d841dc2e71fc0889db77047))

- @ComposableContract has been deprecated in favor of three more specific annotations.

  `@ComposableContract(restartable = false)` has become `@NonRestartableComposable`
  `@ComposableContract(readonly = true)` has become `@ReadOnlyComposable`
  `@ComposableContract(preventCapture = true)` has become `@DisallowComposableCalls`
  `@ComposableContract(tracked = true)` has been removed. ([I60a9d](https://android-review.googlesource.com/#/q/I60a9db0287dc0e03b38e6cf31a7d435026a2ce0f))
- `emptyContent()` and `(@Composable () -> Unit).orEmpty()` utilities have been deprecated as they no longer have any positive performance impact or value ([I0484d](https://android-review.googlesource.com/#/q/I0484d3ef439993d05eea86e53f05997eced590ab))

- Recomposers can now be closed. Closed recomposers will
  continue recomposition until composition child coroutines complete.
  Recomposer.shutDown renamed to cancel to contrast with close. ([Ib6d76](https://android-review.googlesource.com/#/q/Ib6d766b91381ee45af41a14b7951c48f794f0a90))

- APIs related to LazyVerticalGrid are marked as experimental ([Ia53e3](https://android-review.googlesource.com/#/q/Ia53e3b055e4278f67d52df379f3f65c2a10adcc4), [b/178519862](https://issuetracker.google.com/issues/178519862))

- rememberSavedInstanceState() was renamed to rememberSaveable() and moved to androidx.compose.runtime.saveable package. ([I1366e](https://android-review.googlesource.com/#/q/I1366e7fef0a5a56a43d6eeb3770967a9bf683380), [b/177338004](https://issuetracker.google.com/issues/177338004))

- RestorableStateHolder was renamed to SaveableStateHolder and moved to androidx.compose.runtime.saveable package. Inner method RestorableStateProvider was renamed to SaveableStateProvider. Generic type was removed so you can just pass Any as a key. Experimental annotation is not needed anymore. ([I0902e](https://android-review.googlesource.com/#/q/I0902eb1618d36d08ade37be7b6a9453d85b1af62), [b/174598702](https://issuetracker.google.com/issues/174598702))

- Saver, listSaver(), mapSaver(), autoSaver was moved from androidx.compose.runtime.savedinstancestate to androidx.compose.runtime.saveable ([I77fe6](https://android-review.googlesource.com/#/q/I77fe618aa5e124891b84973d8b8b12735f9f909e))

- Artefact androidx:compose:runtime:runtime-saved-instance-state was renamed to androidx:compose:runtime:runtime-saveable ([I6dcac](https://android-review.googlesource.com/#/q/I6dcac2489cf4ec4f17b8ce73bba6eab955a54c6d))

- Many longstanding deprecated APIs in the ui package are deleted. ([I2f2dc](https://android-review.googlesource.com/#/q/I2f2dcaf64fe719c6f2387202f3d0a5699d892657))

- The compose:runtime-dispatch artifact is now deprecated.
  MonotonicFrameClock can now be found in compose:runtime and
  AndroidUiDispatcher can be found in compose:ui. ([Ib5c36](https://android-review.googlesource.com/#/q/Ib5c36a427306eceac4b9b16b52a091e864e5b936))

- Parameters on RounderCornerShape, CutCornerShape and CornerBasedShape were renamed from left/right to start/end in order to support the shape's auto mirroring in the rtl direction. AbsoluteRounderCornerShape and AbsoluteCutCornerShape were introduced for the cases when auto-mirroring is not desired. ([I61040](https://android-review.googlesource.com/#/q/I61040b7bba950191361af89ff4c736ef6cb56235), [b/152756983](https://issuetracker.google.com/issues/152756983))

- canDrag has been removed from the Modifier.scrollable. ([Id66e7](https://android-review.googlesource.com/#/q/Id66e70ac186ffbdd05e2a62af26c7a41e85f02e9), [b/175294473](https://issuetracker.google.com/issues/175294473))

- The API the Compose compiler plugin targets
  has been refactored to use an interface instead of a
  concrete class. The interface also no longer uses
  a type parameter.

  This is an internal change that should not effect source
  code compatibility but is a binary breaking change. ([I3b922](https://android-review.googlesource.com/#/q/I3b9229969aa70138bc57f5e8498602f5b2dba1e6), [b/169406779](https://issuetracker.google.com/issues/169406779))
- Modifier.scaleGestureFilter has been removed. Use Modifier.zoomable instead. Alternatively, use `Modifier.pointerInput { detectMultitouchGestures { ... }}` ([Id5da1](https://android-review.googlesource.com/#/q/Id5da14604597ffe92bf1dd32837a34b462eaa80d), [b/175294473](https://issuetracker.google.com/issues/175294473))

- AnimatedValue/Float is now deprecated. Please use
  Animatable instead. ([I71345](https://android-review.googlesource.com/#/q/I713457f88b04e50fbc5deb70a5bb7bbcf777e630), [b/177457083](https://issuetracker.google.com/issues/177457083))

-
  - Removed CoreText and CoreTextField from public API

  <!-- -->

  - Removed deprecated SelectionContainer overload ([I99c19](https://android-review.googlesource.com/#/q/I99c199c4f9055da1e668d9d799ef11c90239df5b))
- Remove deprecated non-suspend scrolling functions
  Continuing with the changes from last release, the non-suspend scrolling
  functions are now removed entirely. Please convert to the suspend
  functions with the same names. A coroutine scope can be obtained via
  rememberCoroutineScope(). ([I3d39c](https://android-review.googlesource.com/#/q/I3d39c25a1d6790ee5c378f298ffe7af62047810f), [b/178169563](https://issuetracker.google.com/issues/178169563))

- androidx.compose.foundation.layout.ConstraintLayout was deprecated in favor of androidx.constraintlayout.compose.ConstraintLayout. You will need to add a dependency on `androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha01`. ([I87adc](https://android-review.googlesource.com/#/q/I87adc8984e1bb9cb8f76b5779f7c90eab48d2e36))

- tapGestureFilter, doubleTapGestureFilter, longPressGestureFilter and pressIndicaitonGestureFilter have been deprecated. Use Modifier.clickable or Modifier.pointerInput with detectTapGestures function instead. ([I6baf9](https://android-review.googlesource.com/#/q/I6baf95f881b6fa6890ca1d065d49fef3e27bce83), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Removed `Recomposer.current()`. \[Abstract\]ComposeView now
  default to lazily created, window-scoped Recomposers driven by the
  ViewTreeLifecycleOwner for the window. Recomposition and
  withFrameNanos-based animation ticks are paused while the host Lifecycle
  is stopped. ([I38e11](https://android-review.googlesource.com/#/q/I38e11565b2fc776966b6b6984aceafd8a1e6fed1))

- Recomposer.runningRecomposers now offers a global StateFlow
  of read-only RecomposerInfo for observing ongoing composition state in
  the process. Prefer this API to Recomposer.current(), which is now
  deprecated. ([If8ebe](https://android-review.googlesource.com/#/q/If8ebe3959cfe71682ad372382d3b720035ef1605))

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.foundation:foundation:1.0.0-alpha11` and `androidx.compose.foundation:foundation-layout:1.0.0-alpha11` are released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/foundation)

**API Changes**

- Deprecate non-suspend scrollBy, remove non-suspend scrollTo

  We now recommend using suspend functions to control scrolling and wait
  for the scroll to finish. We are deprecating and/or removing the
  non-suspend versions of these functions as part of this transition. ([Ie9ced](https://android-review.googlesource.com/#/q/Ie9cedf8bc71b54353a175699901edd92f850d02c))
- Deprecate non-suspend smoothScrollBy
  We now recommend using suspend functions to control scrolling and wait
  for the scroll to finish. We are deprecating the non-suspend versions
  of these functions as part of this transition. ([I12880](https://android-review.googlesource.com/#/q/I128806c8aea7f17758d1a5d953bbe40e3bcc1b18))

- Content description parameter has been added to the Image and Icon. It is used to provide description to the accessibility services ([I2ac4c](https://android-review.googlesource.com/#/q/I2ac4c1058ed0bf1e5756cc6cdae546806974409e))

- BasicTextField received a new parameter called 'decorationBox'. It allows to add the decorations like icons, placeholder, label and similar to the text field and increase the hit target area of it. ([I16996](https://android-review.googlesource.com/#/q/I169960830df82b0406ac4b6868ea544c9f848403))

- canDrag parameter has been removed from the Modifier.draggable ([Ic4bec](https://android-review.googlesource.com/#/q/Ic4bec74b6fb3a9306abe4fdee7c6961ad3a62d77), [b/175294473](https://issuetracker.google.com/issues/175294473))

- AnimatedFloat.fling that accepts FlingConfig has been removed. Please use suspend
  Animatable.animateDecay instead. ([I4659b](https://android-review.googlesource.com/#/q/I4659b606834e8325473fd672d824114b8ec20173), [b/177457083](https://issuetracker.google.com/issues/177457083))

- Removed `data class` from the following classes:

  - InlineTextContent
  - LocaleList
  - ([I605c7](https://android-review.googlesource.com/#/q/I605c7a0e257f0a52db29f8d82ee449e4ed2c9d8e))
- clickable, toggleable and selectable can be created outside of composition now ([I0a130](https://android-review.googlesource.com/#/q/I0a130bfa57713c96cc8b52c67becd32145526685), [b/172938345](https://issuetracker.google.com/issues/172938345), [b/175294473](https://issuetracker.google.com/issues/175294473))

- ScrollableColumn/Row were deprecated. Using ScrollableColumn is less efficient comparing to LazyColumn when you have a large scrolling content because with LazyColumn we can only compose/measure/draw visible elements. To prevent users from going inefficient way we decided to deprecate ScrollableColumn and ScrollableRow and promote usages of LazyColumn and LazyRow instead. Users can still decide they don't need the lazy behaviour and use the modifiers directly like this: Column(Modifier.verticalScroll(rememberScrollState())) ([Ib976b](https://android-review.googlesource.com/#/q/Ib976b534e063a86a2c587762b786a23e32cc61b6), [b/170468083](https://issuetracker.google.com/issues/170468083))

- New `items(count: Int)` factory method for scope of LazyColumn/LazyRow/LazyVerticalGrid.
  `items(items: List)` and `itemsIndexed(items: List)` are now extension functions so you have to manually import them when used.
  New extension overloads for Arrays: items(items: Array) and itemsIndexed(Array) ([I803fc](https://android-review.googlesource.com/#/q/I803fc5f25fac55855c710ff5064f11525f7b6010), [b/175562574](https://issuetracker.google.com/issues/175562574))

- The deprecated AbsoluteArrangement was removed. ([Iffa96](https://android-review.googlesource.com/#/q/Iffa9670e9c19bc92c48eadbb28783935034e835e), [b/177641870](https://issuetracker.google.com/issues/177641870))

- The propagateMinConstraints parameter was added to Box, for specifying whether the incoming min constraints should be passed to the content of the Box or not. Default is false. ([I0125b](https://android-review.googlesource.com/#/q/I0125bbce017b1ea8587501ace9dea02f7971c01a), [b/152613457](https://issuetracker.google.com/issues/152613457))

**Bug Fixes**

- onCommit, onDispose, and onActive have been deprecated in favor of SideEffect and DisposableEffect APIs ([If760e](https://android-review.googlesource.com/#/q/If760ec2a190c4121a35006695d953010ac22a43a))
- WithConstraints was reworked as BoxWithConstraints and moved to foundation.layout. ([I9420b](https://android-review.googlesource.com/#/q/I9420b9e0fbea7ee048b23a6ef328165bbb11e8a8), [b/173387208](https://issuetracker.google.com/issues/173387208))
- Changes to factory functions for Font/FontFamily/Typeface

  - Added factory functions that start with capital letter
  - Deprecated previous factory functions with lowercase first letters
  - New factory functions return the FontFamily instead of subclasses
  - Hid constructors of the subclasses, so that they can only be constructed via factory functions.
  - Renamed Font.asFontFamily to Font.toFontFamily
  - ([I42aa7](https://android-review.googlesource.com/#/q/I42aa7f9fb7e11eb708bc9e9828f65c57c6c9320b))
- Introduced `ComposeContentTestRule`, which extends
  `ComposeTestRule` and defines `setContent`, which has been removed from
  `ComposeTestRule`. Added a factory method `createEmptyComposeRule()`
  that returns a `ComposeTestRule` and does not launch an Activity for
  you. Use this when you want to launch your Activity during your test,
  e.g. using `ActivityScenario.launch` ([I9d782](https://android-review.googlesource.com/#/q/I9d78283c27d87a3135071884e115bbd814492c47), [b/174472899](https://issuetracker.google.com/issues/174472899))

- animateAsState is now animateFooAsState, where Foo is the
  type of the variable being animated. e.g. Float, Dp, Offset, etc ([Ie7e25](https://android-review.googlesource.com/#/q/Ie7e25c8978996334b0dcc757b07df1434ff346aa))

- Density is now receiver scope for Arrangement interfaces. ([I18aad](https://android-review.googlesource.com/#/q/I18aadb928b615b64ddd6ac41fb630e2ece470f08))

- TextFieldValue accepts AnnotatedString. However this is
  an API only change and multi-style text editing is not
  implemented yet.

  - Removed `initial` from EditingBuffer constructor parameters. ([I326d5](https://android-review.googlesource.com/#/q/I326d534a69911fdd39097cdb42e9341ee7987130))
- invalidate and compositionReference() are now deprecated in favor of currentRecomposeScope and rememberCompositionReference respectively. ([I583a8](https://android-review.googlesource.com/#/q/I583a8efa6e3d3bc303792b825b948b3722ada103))

- AnnotatedString is changed to extend from kotlin.CharSequence.
  Therefore length and subSequence are now instance functions,
  and extension functions are removed. ([Iaf429](https://android-review.googlesource.com/#/q/Iaf429c94da9f1867cc0815cb26933961a71cc629))

- Duration and Uptime will be replace with Long milliseconds,
  and this step removes the dependency of pointer input on those
  classes. ([Ia33b2](https://android-review.googlesource.com/#/q/Ia33b2d6835861501019481b388cb2c99441c346c), [b/175142755](https://issuetracker.google.com/issues/175142755), [b/177420019](https://issuetracker.google.com/issues/177420019))

- RememberObserver replaces CompositionLifecycleObserver
  and CompositionLifecycleObserver is now deprecated.

  `RememberObserver` is a replacement for
  `CompositionLifecycleObserver` with modified semantics and
  renamed methods. Changing to the new API can be done mechanically
  for objects that are only remembered once which is, and continues to
  be, the recommended practice. However, if a reference was
  remembered more than once in a composition `onRemembered` is called
  for each reference where `onEnter` is only called once. `onEnter`
  was called multiple time if the object was used in subcompositions,
  such as `WithConstraints` and `Scaffold` making the single
  `onEnter` call guarantee unreliable and it was removed for
  `RememberObserver`.

  `RememberObserver` adds `onAbandoned` which is called if the
  `RememberObserver` instance is returned from the callback passed
  to `remember` but was not remembered in the composition state
  and, therefore, will never have `onRemembered` called. This can
  occur if an exception terminates composition before completing or
  the composition is discarded because the state is was producing
  a composition for is no longer current or otherwise is no longer
  needed. If the instance of `RememberObserver` following the single
  reference recommendation above is tracking an external resource
  both `onForgotten` and `onAbandoned` each indicate that the
  resource is no longer needed. If the object is tracking work
  started or resources allocated in `onRemembered`, `onAbandoned`
  can be ignored as it will not be called if `onRemembered` is
  called. ([I02c36](https://android-review.googlesource.com/#/q/I02c364f517507abd6a5c071fb527192ad1d77239))
- Renamed TransformedText.transformedText to TransformedText.text

  - TransformedText is no longer a data class ([Ie672a](https://android-review.googlesource.com/#/q/Ie672ad03d475ce6a9bf21b8c74a431592b01040b))
- The following classes are not data classes anymore:

  - AnnotatedString
  - ParagraphStyle
  - SpanStyle
  - TextStyle
  - FontWeight
  - TextDecoration
  - TextGeometricTransform
  - TextIndex
  - TextLayoutResult
  - TextLayoutInput ([Iaff99](https://android-review.googlesource.com/#/q/Iaff995cc24f578b5ffd397aa12a6c98b75182e80))
- Removed experimental monotonicFrameAnimationClockOf methods ([Ib753f](https://android-review.googlesource.com/#/q/Ib753f5d3cb77dabc7727f677a73bb7da8dae5fe2), [b/170708374](https://issuetracker.google.com/issues/170708374))

- Deprecated global coordinates methods and made
  new window-based coordinates methods. ([Iee284](https://android-review.googlesource.com/#/q/Iee284dee7dbc4226493feb144d446a0289b7c83e))

- Please use ImeAction.None instead of ImeAction.NoAction

  - Please use ImeAction.Default instead of ImeAction.Unspecified ([Ie1bcc](https://android-review.googlesource.com/#/q/Ie1bcc7bc3828c757e497b85c4dd70d37764f616f))
- FocusRequester.createRefs is now marked as experimental as it might change. ([I2d898](https://android-review.googlesource.com/#/q/I2d898d56ed0ac33f5a08253509cfd811ee0e8a5d), [b/177000821](https://issuetracker.google.com/issues/177000821))

- SemanticsPropertyReceiver.hidden was renamed to invisibleToUser and marked @ExperimentalComposeUiApi.
  AccessibilityRangeInfo was renamed to ProgressBarRangeInfo.
  stateDescriptionRange was renamed to progressBarRangeInfo.
  AccessibilityScrollState was renamed to ScrollAxisRange.
  horizontalAccessibilityScrollState was renamed to horizontalScrollAxisRange.
  verticalAccessibilityScrollState was renamed to verticalScrollAxisRange. ([Id3148](https://android-review.googlesource.com/#/q/Id31487aa7cbddf4d3d163999afae458cdab4dc8a))

- Changed VisualTransformation to be a functional interface ([I3bba4](https://android-review.googlesource.com/#/q/I3bba482675b65f234f5d46676f1e70853b21c051))

- Leverage TestCoroutineDispatcher in testing ([I532b6](https://android-review.googlesource.com/#/q/I532b68e37ea6f72964fdcc267e397d285cffd9ad))

- Removed PointerInputData and modified PointerInputChange
  to give it all of PointerInputData's fields. Made PointerInputEvent
  and PointerInputEventData internal because they aren't used in
  any public API. ([Ifff97](https://android-review.googlesource.com/#/q/Ifff970815031482a0ac1d5dab42a6156e10154b1), [b/175142755](https://issuetracker.google.com/issues/175142755))

- Renamed TextInputService.onStateUpdated as updateState ([Id4853](https://android-review.googlesource.com/#/q/Id4853b777bb81a4645d1b41b5dff874322949022))

- Remove displaySize as it should be avoided. Typically it is
  better to use size of onRoot() or window size at least. ([I62db4](https://android-review.googlesource.com/#/q/I62db4535f36b09ab6f0b874c221ece0b352db962))

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.foundation:foundation:1.0.0-alpha10` and `androidx.compose.foundation:foundation-layout:1.0.0-alpha10` are released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/foundation)

**API Changes**

- ImeOptions and KeyboardOptions are no more a data class ([I3c898](https://android-review.googlesource.com/#/q/I3c898ecf1f83f64bc9886a088af4fa2a12adcff7), [b/168684531](https://issuetracker.google.com/issues/168684531))
- VisualTransformation API Changes
  - Renamed OffsetMap to OffsetMapping
  - Renamed OffsetMapping.identityOffsetMap to OffsetMapping.Identity
  - PasswordTransformation is no longer data-class
  - Moved OffsetMapping to its own file
  - ([I0bdf3](https://android-review.googlesource.com/#/q/I0bdf3e90ac4a1d8e6e2a3c5762f51016561f2da8))
- EditOperations API Changes
  - Renamed EditOperation as EditCommand
  - Added Command suffix for EditOperation concrete implementations
  - EditCommand's are no longer data classes
  - Renamed EditOperation.process function to applyTo
  - Renamed InputEventListener to InputEventCallback
  - ([I0a366](https://android-review.googlesource.com/#/q/I0a366ac29c7a373efc36eb544bb759eba7f79f3d))
- Modified Velocity to have component parts and mathematical operations. ([Ib0447](https://android-review.googlesource.com/#/q/Ib0447d694d7c5dc82fcef7448faeb0cdda87fced))
- Renamed @ExperimentalTesting to @ExperimentalTestApi to be consistent with similar experimental api annotations ([Ia4502](https://android-review.googlesource.com/#/q/Ia4502a82d5b66328b6e3e3cd322614939816901e), [b/171464963](https://issuetracker.google.com/issues/171464963))
- Added experimental stickyHeader method for LazyColumn/LazyRow ([I0a81d](https://android-review.googlesource.com/#/q/I0a81d453bc0d66501a183813af58aef34cfecaf3))
- Ranamed Color.useOrElse() to Color.takeOrElse() ([Ifdcf5](https://android-review.googlesource.com/#/q/Ifdcf503101fa33b1eaf729a33ac14d0dc03f66ff))
- Deprecated TestUiDispatcher. Use Dispatchers.Main instead ([Ic171f](https://android-review.googlesource.com/#/q/Ic171f9e9da0d7c8d3688754e0f5eed482a668560), [b/175385255](https://issuetracker.google.com/issues/175385255))
- Add Toggle to foundation Strings.kt ([I4a5b7](https://android-review.googlesource.com/#/q/I4a5b74e3ed9bc3b1acd09af221331ef6ab51b9fe), [b/172366489](https://issuetracker.google.com/issues/172366489))
- Moved nativeClass to ui module and made it internal. Updated usages of nativeClass in equals implementations to use 'is MyClass' instead. ([I4f734](https://android-review.googlesource.com/#/q/I4f7340266d36552665f0a059ab34e9b886926f0b))
- FlowRow and FlowColumn were deprecated. Please use a custom layout instead. ([I09027](https://android-review.googlesource.com/#/q/I0902712b97eed1baecddf605bbac0246938c812d))
- Modifier.focus() and Modifier.focusRequester() are deprecated. Use Modifier.focusModifier() and Modifier.focusReference() instead. ([I75a48](https://android-review.googlesource.com/#/q/I75a483954b69de794c5d7be9efc236b6d6b8fcad), [b/175160751](https://issuetracker.google.com/issues/175160751), [b/175160532](https://issuetracker.google.com/issues/175160532), [b/175077829](https://issuetracker.google.com/issues/175077829))
- Introduced SelectionRegistrar.notifySelectableChange to notify Selectable updates to SelectionManager. ([I6ff30](https://android-review.googlesource.com/#/q/I6ff3055300ca7316ad644a4bcf7872d0d48878b8), [b/173215242](https://issuetracker.google.com/issues/173215242))
- Changed `fun Dp.isFinite()` to a `val Dp.isFinite` ([I50e00](https://android-review.googlesource.com/#/q/I50e0035e772c40d61500f56453cd02bb0d9dee70))
- Constraints#satisfiedBy was renamed to isSatisfiedBy. ([I9cf5c](https://android-review.googlesource.com/#/q/I9cf5c5c15c90adaf95d91eef3da4d695733268e9))
- Added isSpecified, isUnspecified, and useOrElse for inline classes with an Unspecified constant. ([I93f7b](https://android-review.googlesource.com/#/q/I93f7b4f1b6c3ef08a3fc6d89fa397a122ef41348), [b/174310811](https://issuetracker.google.com/issues/174310811))

**Bug Fixes**

- New coroutine-based API `Animatable` that ensures mutual exclusiveness among its animations. New DecayAnimationSpec to support multi-dimensional decay animation ([I820f2](https://android-review.googlesource.com/#/q/I820f29e24eaa512515c776db971444290dea97e9), [b/168014930](https://issuetracker.google.com/issues/168014930))
- Added support for disabled and read-only text fields ([I35279](https://android-review.googlesource.com/#/q/I352791811a7b75189013e1ed73c9834cfa5ce961), [b/171040474](https://issuetracker.google.com/issues/171040474), [b/166478534](https://issuetracker.google.com/issues/166478534))
- `animate()` is now replaced with `animateAsState()`, which returns a `State<T>` instead of `T`. This allows better performance, as the invalidation scope can be narrowed down to where the State value is read. ([Ib179e](https://android-review.googlesource.com/#/q/Ib179e3f5f4bf3b72f7445fc22e73c46af7cf74de))
- Add Semantics role API and add Role as a parameter to clickable, selectable and toggleable SemanticsModifier. Changed Modifier.progressSemantics so that Slider can also use it. ([I216cd](https://android-review.googlesource.com/#/q/I216cd5b9118581e569c48a095f009c841ed4418b))
- The native keyEvent can now be accessed through keyEvent.nativeKeyEvent ([I87c57](https://android-review.googlesource.com/#/q/I87c57d68b76441fe92d2b91f58385832fc40ec8d), [b/173086397](https://issuetracker.google.com/issues/173086397))

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha09` and `androidx.compose.foundation:foundation-layout:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/foundation)

**API Changes**

- Add Scrollable interface

  This allows ScrollState and LazyListState to be treated as a common
  type, allowing custom scrolling to be implemented across both types.

  This also moves smoothScrollBy to an extension function on Scrollable,
  taking advantage of this functionality. ([I2153b](https://android-review.googlesource.com/#/q/I2153bebb540136618210dc0e3980eae788c01392))
- LazyVerticalGrid is added. ([I17267](https://android-review.googlesource.com/#/q/I172670e5a6648278604e9ad024d3db17c9c6974b), [b/162213211](https://issuetracker.google.com/issues/162213211))

- Deprecate LazyColumnFor, LazyRowFor, LazyColumnForIndexed and LazyRowForIndexed. Use LazyColumn and LazyRow instead ([I5b48c](https://android-review.googlesource.com/#/q/I5b48c8a3b1fef2f603ab69ded1d19709aa9f87fb))

- For suspending pointer input APIs, renamed
  HandlePointerInputScope to AwaitPointerEventScope and
  handlePointerInput() to awaitPointerEventScope(). ([Idf0a1](https://android-review.googlesource.com/#/q/Idf0a1b94f065e72b65361cdf616122ed7939c3e7), [b/175142755](https://issuetracker.google.com/issues/175142755))

- LazyListState.layoutInfo was added which exposes the list of sizes and offsets of the currently visible items ([If8678](https://android-review.googlesource.com/#/q/If86783ac8b127269d4bf8bbc5dd4eba52b3fbb77), [b/170472532](https://issuetracker.google.com/issues/170472532))

- Removed ExperimentalPointerInput annotation ([Ia7a24](https://android-review.googlesource.com/#/q/Ia7a2473869400fc92ce70c802f42df9af7129386))

- InteractionState support for TextFields has been added. ([I61d91](https://android-review.googlesource.com/#/q/I61d91b15858fc3914ab9f15409857f0bccf67f34))

- Add reverseLayout param for LazyColumn/Row. when `true` items will be composed from the bottom to the top and `LazyListState.firstVisibleItemIndex == 0` will mean the first item is located at the bottom. ([I552ae](https://android-review.googlesource.com/#/q/I552ae9123cfc426cda2bf2e72784bf07c3c15cbf), [b/166589935](https://issuetracker.google.com/issues/166589935))

- verticalArrangement param was added for LazyColumn. horizontalArrangement param was added for LazyRow. Arrangement allows us to add a spacing between items and specify the arrangement of the items when we do not have enough of them to fill the whole minimum size. ([Icf79a](https://android-review.googlesource.com/#/q/Icf79a56204f07903c5f3bd4dd5700568fb6d1343), [b/170394300](https://issuetracker.google.com/issues/170394300))

- detectMultitouchGestures now uses one callback with combined
  centroid, pan, zoom and rotate parameters. ([Ie6e1c](https://android-review.googlesource.com/#/q/Ie6e1c2d7496ed0aabc6a5256f859c91cc39a08dc))

- Moved ContentDrawScope to ui-graphics
  module to be with DrawScope. ([Iee043](https://android-review.googlesource.com/#/q/Iee0437fa587fbe12a3623955f5fe720d5aae551f), [b/173832789](https://issuetracker.google.com/issues/173832789))

**Bug Fixes**

- Lambdas in offset modifiers now return IntOffset rather than Float. ([Ic9ee5](https://android-review.googlesource.com/#/q/Ic9ee5c05df4c89993ee19f19ddd327a986f21bc1), [b/174137212](https://issuetracker.google.com/issues/174137212), [b/174146755](https://issuetracker.google.com/issues/174146755))
- Removed SlotTable, SlotReader and
  SlotWriter from the public API. These were marked as
  InternalComposeAPI previously. Now they are internal
  to the compose module.

  CompositionData and CompositionGroup were added as a
  replacement for the ui-tooling API to use to extract
  composition information. These are public but are not
  intended for use outside the ui-tooling API as they provide
  the raw information the ui-tooling API interprets ([I31a9c](https://android-review.googlesource.com/#/q/I31a9ca6a7e5bbf162c984394dffd7a25b059315a))
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

- Autofill API is now experimental API and requires opt-in ([I0a1ec](https://android-review.googlesource.com/#/q/I0a1ecfbf4ddeccaecc3cea8d2223b0a4afa60636))

- Adding destructuring declarations to create FocusRequester instances ([I35d84](https://android-review.googlesource.com/#/q/I35d84e1320bec5b62bf1fb096aa95f90cfd96e9c), [b/174817008](https://issuetracker.google.com/issues/174817008))

- accessibilityLabel has been renamed to contentDescription.
  accessibilityValue has been renamed to stateDescription. ([I250f2](https://android-review.googlesource.com/#/q/I250f2d41e139d4838b0b3706f18b56fcc4f515bd))

- Introduced several new functions in SelectionRegistrar and also renamed onPositionChange to notifyPositionChange. ([Ifbaf7](https://android-review.googlesource.com/#/q/Ifbaf754c0ee3f485869115bba8dbcc1a8b7f5b88))

- AndroidOwner made internal ([Ibcad0](https://android-review.googlesource.com/#/q/Ibcad027dbc1794f5d202be52fe0783c73d249a25), [b/170296980](https://issuetracker.google.com/issues/170296980))

- New infiniteRepeatable function for creating an InfiniteRepeatableSpec ([I668e5](https://android-review.googlesource.com/#/q/I668e501c0c9061aa94b258ec9646617e0f77faf1))

- The `Applier` interface has changed to simplify
  building trees bottom-up instead of top-down.

  The `insert()` method has been renamed to `insertTopDown()`.

  A new method, `insertBottomUp()`, was added.

  An applier either inserts nodes into the tree it is editing
  using `insertTopDown()` or `insertBottomUp()` depending on
  which performs better.

  Some trees, such as `LayoutNode` and `View`, are much more
  efficient to build bottom-up than top-down. Prior to this change,
  a stack of inserts was required to implement bottom-up which
  needed to be copied to every applier which needed bottom-up
  construction for performance. With this change an `Applier`
  overrides `insertBottomUp()` to build a tree bottom-up and
  `insertTopDown()` to build the tree top-down. ([Icbdc2](https://android-review.googlesource.com/#/q/Icbdc2929ab8fc8fce231d633b062fc80be5c10c9))
- Added painterResource API
  to handle opaquely loading Painter objects
  from either rasterized asset formats (like PNGs)
  or VectorDrawables. Consumers no longer have
  to determine the type of asset in advance
  and can call this method to get a Painter object
  to use in Image composables or painter modifiers. ([I2c703](https://android-review.googlesource.com/#/q/I2c703e31eedbbfcf073d28064496a6e324c2027a), [b/173818471](https://issuetracker.google.com/issues/173818471))

- Added buildAnnotatedString factory function in order
  to build an AnnotatedString. Deprecated annotatedString
  builder function. ([Idfe0b](https://android-review.googlesource.com/#/q/Idfe0b133687e7b5f377e997b79bd4463161a6d0b))

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha08` and `androidx.compose.foundation:foundation-layout:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/foundation)
| **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

**API Changes**

- Removed `maxLines` parameter from the `CoreTextField`. If you'd like to constraint the height of the text field by the number of lines, use `BasicTextField` instead. ([Iec002](https://android-review.googlesource.com/#/q/Iec0026dfe939c60e110304db6cda0fdaa57a034f))
- Changed the `await*TouchSlop()` methods to not detect the pointer down and renamed them to `*OrCancellation`. Also removed the need for `orientationLock` parameter. ([Ie96e1](https://android-review.googlesource.com/#/q/Ie96e10e900244ab02936b143727db5faad1597e5))
- Added lint check for composable lambda parameter naming and position, to check for consistency with Compose guidelines. Also migrated some APIs using `children` as the name for their trailing lambda to `content`, according to the lint check and guidance. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48e38a2896785b521814d95c9fb624d2807315))
- `foundation:foundation-text` apis moved to `foundation:foundation`. The package structure remained the same ([Id3eb2](https://android-review.googlesource.com/#/q/Id3eb24adc68111232087cdb2a1d01132ddd49a64))
- New multitouch gesture detector, including helpers for detecting rotation, zoom, and panning. ([Ic459d](https://android-review.googlesource.com/#/q/Ic459dc4c6b4e4a171dbb16a87ee8dfe780230d16))
- New drag gesture detector suspending pointer input API, including orientation locking. ([Icef25](https://android-review.googlesource.com/#/q/Icef25dbc49fa8786c7631e8b97b0732b871afea6))
- Renamed VectorAsset to ImageVector Moved and renamed VectorAsset to Builder to be an inner class of ImageVector as per API council guidelines. Added typealias of VectorAssetBuilder to link to ImageVector.Builder for compat. ([Icfdc8](https://android-review.googlesource.com/#/q/Icfdc85391feb2bd0edabebeba84f31bace10883a))
- Renamed ImageAsset and related methods to ImageBitmap. ([Ia2d99](https://android-review.googlesource.com/#/q/Ia2d9941a6e0b8c29867cb3fbafb629fa4db10684))
- Moved foundation semantics properties to ui ([I6f05c](https://android-review.googlesource.com/#/q/I6f05cc7c0bdf1e5344440cd6e492fbc0545011e7))
- Add coroutine-based scrolling APIs:

  Adds LazyListState.snapToItem and LazyListState.smoothScrollBy, as well as lower-level
  APIs for scroll control. These APIs provide a suspend interface to control scrolling
  that waits until the scroll is finished before returning. ([Ie5642](https://android-review.googlesource.com/#/q/Ie56426c01b3c8ad51afb237cb972a8578d2fefd4))
- Added a singeLine parameter into BasicTextField, TextField and OutlinedTextField. Set this parameter to true to make the text field a single horizontally scrollable line. ([I57004](https://android-review.googlesource.com/#/q/I57004dff8b341f08f6673235e28e958c9fbf63c6), [b/168187755](https://issuetracker.google.com/issues/168187755))

- Gesture detector for tap, double-tap, long press,
  and press indication were added using the new suspending pointer
  input. A few utilities were added as well, making it easier
  for developers to write their own gesture detectors. ([I00807](https://android-review.googlesource.com/#/q/I0080776a5672f63ceb8f4ae0a753d5f4debdc2e8))

- Modifier.focusable has need added in foundation. Use this to add focusable behavior to a component, with correct semantics and accessibility. ([I41eb9](https://android-review.googlesource.com/#/q/I41eb9d67669e19f8a7c20804c836a8c6dc0b5526), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/162865824](https://issuetracker.google.com/issues/162865824))

- Previously deprecated APIs have been removed: Border was removed, use BorderStroke instead. Modifier.drawBorder was removed, use Modifier.border instead. Modifier.gravity was removed, use Modifier.align instead. Stack was removed, use Box instead ([I32c2b](https://android-review.googlesource.com/#/q/I32c2b7c59a199f206b8ad854e07b66f32f0ef1f9), [b/172470874](https://issuetracker.google.com/issues/172470874))

- AbsoluteArrangement was renamed to Arrangement.Absolute. ([If26f2](https://android-review.googlesource.com/#/q/If26f210b1352608678ab175677fb8b54a631d0c9))

**Bug Fixes**

- Moved DrawModifier APIs from the androidx.compose.ui package to the androidx.compose.ui.draw package. Created DrawModifierDeprecated.kt file to include typealiases/helper methods to assist with the migration from the deprecated to the current APIs. ([Id6044](https://android-review.googlesource.com/#/q/Id6044c7119aeaf40a3ff21006fe39b03f5f1b18a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- Renamed Modifier.drawLayer to Modifier.graphicsLayer Also updated related classes to GraphicsLayer as per API council feedback. ([I0bd29](https://android-review.googlesource.com/#/q/I0bd297065427d19715e4e33480f7be87e51ff48a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- `<T>` was removed from SubcomposeLayout declaration. You can use it without specifying a type now. ([Ib60c8](https://android-review.googlesource.com/#/q/Ib60c850964b308ebee32beca6db78d76af67fbf1))
- Made PointerInputData's uptime and position fields non-nullable. ([Id468a](https://android-review.googlesource.com/#/q/Id468a0ef7c00c30a89114ea8dc95fa019961e189))
- MaterialTheme now sets the correct colors for selection handles and selection background. Non-Material apps can manually use AmbientTextSelectionColors to customize the colors used for selection. ([I1e6f4](https://android-review.googlesource.com/#/q/I1e6f4b495bdc713e162759a08ecf0a7311b26e33), [b/139320372](https://issuetracker.google.com/issues/139320372), [b/139320907](https://issuetracker.google.com/issues/139320907))
- The alignment parameter of Box was renamed to contentAlignment. ([I2c957](https://android-review.googlesource.com/#/q/I2c95727d9ec49f056fffb3a73dce95a9d3be5b53))
- offsetPx modifiers were renamed to offset. They are now taking lambda parameters instead of State. ([Ic3021](https://android-review.googlesource.com/#/q/Ic302174ef9cffa7ef806d1668f81cb89159363f2), [b/173594846](https://issuetracker.google.com/issues/173594846))
- Added WindowManager.isWindowFocused to check if the host window is in focus, and a WindowFocusObserver that provides an onWindowFocusChanged callback. ([I53b2a](https://android-review.googlesource.com/#/q/I53b2a702b81215dc5a5536144a752e1c93ab056e), [b/170932874](https://issuetracker.google.com/issues/170932874))
- Added resetInput parameter to TextInputService#onStateUpdated ([I3e8f5](https://android-review.googlesource.com/#/q/I3e8f5404553921bd94ae424d2840ca5595b6f90b), [b/172239032](https://issuetracker.google.com/issues/172239032), [b/171860947](https://issuetracker.google.com/issues/171860947))
- Updated TextFieldValue API
  - made TextFieldValue.composition readonly
  - removed exception thrown for invalid selection range ([I4a675](https://android-review.googlesource.com/#/q/I4a67592c05ab384ad5614cccf50ad6e79be52b55), [b/172239032](https://issuetracker.google.com/issues/172239032))
- Deprecated Ambients named with `Ambient` as their suffix, and replaced them with new properties prefixed with Ambient, following other Ambients and Compose API guidelines. ([I33440](https://android-review.googlesource.com/#/q/I334403cc490ea913b8980d29e2cbe08e98ad7945))
- Added Android Typeface wrapper. You can load an Android Typeface via `typeface` function i.e. `typeface(Typeface.DEFAULT)`. Also renamed `typefaceFromFontFamily()` to `typeface()` ([I52ab7](https://android-review.googlesource.com/#/q/I52ab713f851011796d0a0437e62693a7e762701a))
- Added lint check to check that Modifier factories use `androidx.compose.ui.composed {}` internally, instead of being marked as `@Composable`. ([I3c4bc](https://android-review.googlesource.com/#/q/I3c4bcedafbd0bc9846a9c0ba75685a35cb4de371))
- Added lint check to check that Modifier factory functions are defined as extensions on Modifier, so they can be fluently chained together. ([I07981](https://android-review.googlesource.com/#/q/I07981617a0e09137b787adbc0219f48af5b86169))
- Semantics argument mergeAllDescendants was renamed to mergeDescendants. ([Ib6250](https://android-review.googlesource.com/#/q/Ib625016bd3bbe4349c2870ba68ad52d76a0d372a))
- Time control in tests (TestAnimationClock and its usages) is now experimental ([I6ef86](https://android-review.googlesource.com/#/q/I6ef86c5f530422c7c751bdb086a691cbc2e837f3), [b/171378521](https://issuetracker.google.com/issues/171378521))
- Remove old ui-test module and its stubs ([I3a7cb](https://android-review.googlesource.com/#/q/I3a7cbbe376d0542955983fb09afd2dc37be7647e))
- TextUnit.Inherit is renamed to TextUnit.Unspecified in consistent with other units. ([Ifce19](https://android-review.googlesource.com/#/q/Ifce190ac87b01144b2fb0e7f9a8659bceed87f4e))
- The Alignment interface was updated and made functional. ([I46a07](https://android-review.googlesource.com/#/q/I46a0791e261b6f305804797cdda7fdd2ef405305), [b/172311734](https://issuetracker.google.com/issues/172311734))
- `foundation:foundation-text` module has been merged into `foundation:foundation` ([Idac0f](https://android-review.googlesource.com/#/q/Idac0f648e575be6627d940b6af7f9b25e73188ce))
- Deprecate place(Offset) and placeRelative(Offset). Use overloads with int offsets instead ([I4c5e7](https://android-review.googlesource.com/#/q/I4c5e75e6ba7382735acccd44324bb96a59d82490))
- `id` was renamed to `layoutId` for `LayoutIdParentData`. `Measurable.id` was renamed to `Measurable.layoutId`. ([Iadbcb](https://android-review.googlesource.com/#/q/Iadbcb8b5588876e0d2a512e476968025b03ada6c), [b/172449643](https://issuetracker.google.com/issues/172449643))

### Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha07`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha07`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/foundation)

**API Changes**

- Similarly to `Modifier.fillMaxSize[Width|Height]` we now support fractions in `Modifier.fillParentMaxSize[Width|Height]` inside the scope of `LazyColumn/Row` ([I797e2](https://android-review.googlesource.com/#/q/I797e279db98215aa6f7c3e705f90442b5bf31f99), [b/166586426](https://issuetracker.google.com/issues/166586426))
- Removed `KeyboardOptions.toImeOptions` from public API. ([Ic2e45](https://android-review.googlesource.com/#/q/Ic2e4500be7841ad3815bc576356ab67e616db534))
- The foundation AmbientTextStyle, ProvideTextStyle, and AmbientContentColor have been deprecated. Instead use the new versions available in the Material library. For non-Material applications, you should instead create your own design system specific theming ambients that can be consumed in your own components. ([I74acc](https://android-review.googlesource.com/#/q/I74accf7166eaca28e9e2d14402ed08d80f8625ab), [b/172067770](https://issuetracker.google.com/issues/172067770))
- foundation.Text has been deprecated and replaced with material.Text. For a basic, unopinionated text API that does not consume values from a theme, see androidx.compose.foundation.BasicText. ([If64cb](https://android-review.googlesource.com/#/q/If64cbdd89497f171edfd1b4de907123f73279e8d))
- Added maxLines to TextFields ([Ib2a5b](https://android-review.googlesource.com/#/q/Ib2a5bb1c0ec8782b6a05fc48033fd4b05622820e))
- Update TextFields to accept KeyboardOptions ([Ida7f3](https://android-review.googlesource.com/#/q/Ida7f3c71647dc9fff8acdd50fc5604a15957ccec))
- Added KeyboardOptions for use in TextFields ([I9ca32](https://android-review.googlesource.com/#/q/I9ca329336d80be07e6a0c1e6d7a2f84902774898))
- Adds BasicText as a design-unopinionated API for text, parallel to BasicTextField. ([I28268](https://android-review.googlesource.com/#/q/I28268e2eff13261410ea88ced1dd1b3dca509a20))
- ExperimentalLazyDsl annotation was removed. LazyColumn/LazyRow can now be used without adding @OptIn ([Idab7a](https://android-review.googlesource.com/#/q/Idab7ad1ce0d14659e5e7f54076d4c207b9449215), [b/166584730](https://issuetracker.google.com/issues/166584730))
- BaseTextField has been deprecated. Use BasicTextField instead. ([I896eb](https://android-review.googlesource.com/#/q/I896eb0eb21e73bda5f269e1ffae4357201acb219))
- BasicTextField has been added as a replacement for both CoreTextField and BaseTextField ([Id4cea](https://android-review.googlesource.com/#/q/Id4cea88b13c50145a6ffd8a52318bc8e2f83edb8))
- Remove deprecated LazyColumnItems/LazyRowItems ([I1d8a8](https://android-review.googlesource.com/#/q/I1d8a809dfb424b9f066dc030d148c3b0572c4345))
- The deprecated composables for sizing to intrinsic measurements were removed. ([I18537](https://android-review.googlesource.com/#/q/I18537b5628f76eecb30f9a163d2fde3cd5984609), [b/171811496](https://issuetracker.google.com/issues/171811496))
- relativePaddingFrom was renamed to paddingFrom. The paddingFromBaseline modifier was added, as convenience for specifying distances from layout bounds to text baselines. ([I0440a](https://android-review.googlesource.com/#/q/I0440af2aea41e020cb581b9030522b7586fe952e), [b/170633813](https://issuetracker.google.com/issues/170633813))
- The matchHeightConstraintsFirst parameter was added to the aspectRatio modifier, which can be used to specify the modifier to size to height constraints before trying the width correspondents. ([Ie7c43](https://android-review.googlesource.com/#/q/Ie7c433d0f51d33c1df45a4b63d110e34ae0bd360), [b/155290593](https://issuetracker.google.com/issues/155290593))
- The deprecated DpConstraints was removed. ([I87884](https://android-review.googlesource.com/#/q/I87884131131503fe08e78f67898cf233b2818832), [b/171702471](https://issuetracker.google.com/issues/171702471))

**Bug Fixes**

- Introduced ScaleFactor inline class to represent scale factors for the horizontal and vertical axes independent of one another in order to support non-uniform scaling use cases.
  - Added computeScaleFactor method to ContentScale
  - Added ContentScale.FillBounds to perform non-uniform scaling to stretch the src bounds to fully occupy the destination.
  - Added operator methods to compute ScaleFactor parameters with Size parameters.
  - ([Ic96a6](https://android-review.googlesource.com/#/q/Ic96a6eb421cda5550c817ceca23ab50fde337778), [b/172291582](https://issuetracker.google.com/issues/172291582))
- captureToBitmap moved to captureToImage. ([I86385](https://android-review.googlesource.com/#/q/I86385454625b533b83c87e48d82e143dd1bcb88e))
- Marks CoreText as @InternalTextApi. Use BasicText instead. ([I6aaeb](https://android-review.googlesource.com/#/q/I6aaeb3c571bc716f920409a255e07d0d03cf78d8))
- Rename KeyboardOptions as ImeOptions ([I82f36](https://android-review.googlesource.com/#/q/I82f364ca1ede4bfea9430fcc9fd227d729b39fd9))
- Moved KeyboardType and ImeAction into KeyboardOptions ([I910ce](https://android-review.googlesource.com/#/q/I910cea6ec0ef3568b9a94f7b193e8cb7e8b776ed))
- CoreTextField has been marked as @InternalTextApi. Use BasicTextField instead ([Ie2469](https://android-review.googlesource.com/#/q/Ie2469cf4af3a476e8015999f45e439ea619dab23))
- ExperimentalSubcomposeLayoutApi annotation was removed. SubcomposeLayout can now be used without adding @OptIn ([I708ad](https://android-review.googlesource.com/#/q/I708adafbc3c10cc6c23fe5a236f66e73146e4f56))
- Introduce ui-test-junit4 module ([Ib91f8](https://android-review.googlesource.com/#/q/Ib91f8a6792d8852427cc0dff99a40086c00b8ce4))
- Updated Icon API to take in Color.Unspecified as a possible tint color which will draw the provided asset or painter without a ColorFilter. Previously attempts to ignore tinting with Color.Unspecified would tint with a transparent color ending up with nothing rendered at all. ([I049e2](https://android-review.googlesource.com/#/q/I049e2b7464204f1fd8965d31d6dfba811b30a2bb), [b/171624632](https://issuetracker.google.com/issues/171624632))
- MeasureResult was moved out of MeasureScope. ([Ibf96d](https://android-review.googlesource.com/#/q/Ibf96ddadae8115015066dcda2026a57b87c2ead6), [b/171184002](https://issuetracker.google.com/issues/171184002))
- Several layout related symbols were moved from androidx.compose.ui to androidx.compose.layout.ui. ([I0fa98](https://android-review.googlesource.com/#/q/I0fa982d87929e5ca9e3a32762fe9cf1fa8b8cfef), [b/170475424](https://issuetracker.google.com/issues/170475424))
- androidx.ui.test moved to androidx.compose.ui.test ([I9ffdb](https://android-review.googlesource.com/#/q/I9ffdb165d49e8d136b58cc4e32599a4a1d5b169e))
- FirstBaseline and LastBaseline were moved to androidx.compose.ui.layout package ([Ied2e7](https://android-review.googlesource.com/#/q/Ied2e7ff4c8d8a45072439d719ea5c75270c28c97))
- Added SelectionContainer without the callback ([Ibfadb](https://android-review.googlesource.com/#/q/Ibfadba5a9f66101c5746c5b842dadf840617e1a6))
- Add Tests for SelectionHandles' Positions in SelectionContainer. ([Ie93db](https://android-review.googlesource.com/#/q/Ie93dbdbebcdc55d63bc8185fdf2faa0262778c15))
- Added Keyboard auto correct IME Option ([I57b8d](https://android-review.googlesource.com/#/q/I57b8d4b3c65630763e198c31c7d116fcbe461c51))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha06`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha06`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/foundation)

**API Changes**

- androidx.compose.foundation.Icon has been moved to androidx.compose.material.Icon. You can also use the Image component / Modifier.paint() with a Painter if you do not want to use the Material library. ([I9f622](https://android-review.googlesource.com/#/q/I9f6222326427cebacde10562cde99b9ebff2490f))
- Added interactionState to Modifier.scrollable, ScrollableColumn and LazyColumnFor ([I81566](https://android-review.googlesource.com/#/q/I815666e1b4544dcd5da9f253ec1b539fdd777529), [b/169509805](https://issuetracker.google.com/issues/169509805))
- alignByBaseline was added to RowScope and alignWithSiblings was renamed to alignBy ([I06503](https://android-review.googlesource.com/#/q/I06503f2d4c9b7717c6bdee3bdb466e30f8a56d52), [b/170628732](https://issuetracker.google.com/issues/170628732))
- Box was made an inline function. ([Ibce0c](https://android-review.googlesource.com/#/q/Ibce0c1940173f06c030fd1115b9badb692ceb05a), [b/155056091](https://issuetracker.google.com/issues/155056091))
- Added maxLines to CoreTextField ([Ibee58](https://android-review.googlesource.com/#/q/Ibee58be1331d36bfce70a0b14e83ffb5c0cfa3a2), [b/143687793](https://issuetracker.google.com/issues/143687793))
- Added softwrap to CoreTextField. ([I21a4b](https://android-review.googlesource.com/#/q/I21a4bb066176e69accc0b2b45b13faa11afd4ec5))

**Bug Fixes**

- Deprecate VectorPainter in favor of rememberVectorPainter to better indicate that the composable API internally leverages 'remember' to persist data across compositions. ([Ifda43](https://android-review.googlesource.com/#/q/Ifda43dfd1d5b581c3666f4f69b528c47dbaa0ff5))
- Enable transitions in ComposeTestRule; remove option to enable the blinking cursor from ComposeTestRule. ([If0de3](https://android-review.googlesource.com/#/q/If0de36db743b7f57b161b0fe6324565750436866))
- Added single line keyboard option to CoreTextField ([I72e6d](https://android-review.googlesource.com/#/q/I72e6d9f84abbf4ff6a9ede5355de4c30d37c3d8c))
- Renamed Radius API to CornerRadius to better express how it is used throughout Compose. Updated documentation to indicate that negative corner radii are clamped to zero. ([I130c7](https://android-review.googlesource.com/#/q/I130c7e1baadaf1b2f8e6c32f1af0d3702e2cee50), [b/168762961](https://issuetracker.google.com/issues/168762961))
- Add ability to specify inspector info in composed modifier ([Idee08](https://android-review.googlesource.com/#/q/Idee08841816fb7dfc8f0621eb5a32c3663131aa1), [b/163494569](https://issuetracker.google.com/issues/163494569))
- Added KeyboardCapitalization IME Option ([I8ac38](https://android-review.googlesource.com/#/q/I8ac3875c7c668bcd2868becd328bb3a253c667cd))
- Fix Rtl Handle Position. ([I6e1e0](https://android-review.googlesource.com/#/q/I6e1e07b76476d8e2f0be50ff022257c2379edcf7))
- Breaking change: removed the return value from PointerInputFilter.onPointerEvent(...) given that the only value that should be able to be changed in pointer events is consumption data. Instead of returning data from PointerInputFilter.onPointerEvent(...), now you can just mutate the consumption data of the PointerEvents passed in. ([I6acd0](https://android-review.googlesource.com/#/q/I6acd06e56ab49c8ca932ff7c2d35a517a412e2d2))
- Added SelectAll option into selection menu ([Ief02b](https://android-review.googlesource.com/#/q/Ief02bb5bb39d11a02112c4ace1b971d6834ec5dd))

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha05`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha05`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/foundation)

**API Changes**

- CoreTextField now supports cursor functionality ([Id23aa](https://android-review.googlesource.com/#/q/Id23aa3de7c74074fb9c0d37a42490b6c49f691f3))
- Deprecates contentColor() and currentTextStyle() APIs, and replaces them with AmbientContentColor and AmbientTextStyle ambients respectively. You can access the current value by using `.current` on the ambient property, as with any other ambient. This was change was made for consistency and to avoid having multiple ways to accomplish the same thing. Additionally renames some ambient properties to better describe their purpose as follows:

  - ContentColorAmbient -\> AmbientContentColor
  - TextStyleAmbient -\> AmbientTextStyle
  - IndicationAmbient -\> AmbientIndication
  - EmphasisAmbient -\> AmbientEmphasisLevels
  - RippleThemeAmbient -\> AmbientRippleTheme ([I37b6d](https://android-review.googlesource.com/#/q/I37b6dccb9751f2a9eb550f42da32bf4b1bff4296))

**Bug Fixes**

- As part of the standardization of sentinel values for inline classes, rename Color.Unset to Color.Unspecified for consistency with other inline classes ([I97611](https://android-review.googlesource.com/#/q/I9761102e79ade32812984466c020f2715065ac85), [b/169797763](https://issuetracker.google.com/issues/169797763))
- Added Copy/Paste/Cut accessibility actions ([I6db4f](https://android-review.googlesource.com/#/q/I6db4f570596e65c2e12fbc6f0821961c65671e98))
- TextOverflow.None is introduced. When overflow is None, Text won't handle overflow anymore, and it will report its actual size to LayoutNode. ([I175c9](https://android-review.googlesource.com/#/q/I175c9163a70ed35e4390b10848f143ed30ed2bf3), [b/158830170](https://issuetracker.google.com/issues/158830170))
- Updated Size.Unspecified parameters to be Float.NaN instead of Float.POSITIVE_INFINITY. Updated Painter implementations to check against Size.Unspecified as well as non-finite Sizes. ([I95a7e](https://android-review.googlesource.com/#/q/I95a7e394ef1bc64d4deca510a681c9dbf959b1c1))
- Added Paging Compose module and paging integration ([Ib85da](https://android-review.googlesource.com/#/q/Ib85da91de0128619d792484a31c1db4d31603141))
- Modify LazyListScope to receive nullable values ([I1765b](https://android-review.googlesource.com/#/q/I1765bf0567a0c8dd1f75cf9c9a1ee7ac7195354b))
- OnPositionedModifier is renamed to OnGloballyPositionedModifier and onPositioned() is renamed to onGloballyPositioned(). ([I587e8](https://android-review.googlesource.com/#/q/I587e8b151079d9d9506d86caa4283b7108958de4), [b/169083903](https://issuetracker.google.com/issues/169083903))
- Added samples for LazyColumn/Row ([Idc16d](https://android-review.googlesource.com/#/q/Idc16d2e2ced995bae92d045eb60cda97be8cb7e6))
- Fix for the items and itemsIndexed methods to allow emptyList ([I06647](https://android-review.googlesource.com/#/q/I066470185765d918c5f29e96b5ac6dfefe46cb2c))
- Add a DSL for specifying inspector information ([Ic9a22](https://android-review.googlesource.com/#/q/Ic9a22ffea5cdc0bc34160512515aef2c576d9aae))
- Move LongPress into Text. ([Iff2bc](https://android-review.googlesource.com/#/q/Iff2bc6e44143bedf71442531f8ec2d37a40e4a19))
- Disable Selection in Text, and a Demo. ([Ie7e97](https://android-review.googlesource.com/#/q/Ie7e97b1bf0efd89c08c2bb554a9e676bb2d21dff))
- Support AnnotatedString to SpannableString conversion for accessibility. ([Ief907](https://android-review.googlesource.com/#/q/Ief907a05b7928fa3c59784cda5c7a7739485607b))
- Removed `PointerInputFilter.onPointerInput(...)`. `PointerInputFilter.onPointerEvent(...)` should be used in its place. ([I6f04a](https://android-review.googlesource.com/#/q/I6f04a771485232d62134c22588a0ae67c909bf81))

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha04`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha04`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/foundation)
| **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

**API Changes**

- Stack was renamed to Box. The previously existing foundation.Box will be deprecated in favor of the new Box in compose.foundation.layout. The behavior of the new Box is to stack children one on top of another when it has multiple children - this is different from the previous Box, which was behaving similar to a Column. ([I94893](https://android-review.googlesource.com/#/q/I94893bca003d7826c6a5b3c05ac3878d2f6bf953), [b/167680279](https://issuetracker.google.com/issues/167680279))
- Box decoration parameters have been deprecated. If you want to have decorations/padding on your box, use Modifiers instead (Modifier.background, Modifier.border, Modifier.padding) ([Ibae92](https://android-review.googlesource.com/#/q/Ibae92e99d0dd8984e666ece6cd6ec6f26f6ef672), [b/167680279](https://issuetracker.google.com/issues/167680279))
- Add a new LazyListState class. This allows for observation and control of the scroll position of LazyRow and LazyColumn components. Instances can be created using rememberLazyListState() and passed into the state parameter of the component. Currently, the first visible item and offsets can be observed in this initial version. ([Ic7cb7](https://android-review.googlesource.com/#/q/Ic7cb72444d41ccb6add635ba0873bb0e9222cf15), [b/159307669](https://issuetracker.google.com/issues/159307669))
- Lazy list position and scroll offset are now saved and restored across Activity recreation ([Ie045f](https://android-review.googlesource.com/#/q/Ie045f8264ad032fd46934306d4cf603db81b23a2), [b/166589058](https://issuetracker.google.com/issues/166589058))
- Add long click semantics action ([I6281b](https://android-review.googlesource.com/#/q/I6281b383328d549b30b3ef915e717abbbb28ddaa), [b/156468846](https://issuetracker.google.com/issues/156468846))
- MutatorMutex utility added for keeping a single mutator of shared state over time and cancelling conflicting mutators by priority ([I3f975](https://android-review.googlesource.com/#/q/I3f9751b239aba5b9769aa821be08e88909aca90e))
- Annotated rootAnimationClockFactory, transitionsEnabled, blinkingCursorEnabled and textInputServiceFactory with @VisibleForTesting, make them internal API and hide their kdoc ([I554eb](https://android-review.googlesource.com/#/q/I554ebefac18b216d51e387e5fd1c3a735fde9500), [b/168308412](https://issuetracker.google.com/issues/168308412))
- Removed inlineContent parameter from Text with String input. It won't be used because inlineContent must work with AnnotatedString. ([Ief403](https://android-review.googlesource.com/#/q/Ief40369f380fe1d5e970b42358e5bb002eeb8ef4))
- The deprecated custom Arrangement APIs were removed. ([Ic576d](https://android-review.googlesource.com/#/q/Ic576d1053ebfe238d0805b4e8f0ec6a741e04645), [b/168297922](https://issuetracker.google.com/issues/168297922), [b/168297923](https://issuetracker.google.com/issues/168297923))
- The `unbounded` parameter was added to wrapContentSize modifiers, which enables measuring the layout element with infinite max constraints. ([I77951](https://android-review.googlesource.com/#/q/I7795170623538cd5dd2372ce0fd52bc6d0368cbd), [b/158559319](https://issuetracker.google.com/issues/158559319))
- We prevented static imports of contents of layout scopes (e.g. alignWithSiblings in RowScope). The explicit scope alternative should be used instead: `with(RowScope) { Modifier.alignWithSiblings(FirstBaseline) }`. ([I216be](https://android-review.googlesource.com/#/q/I216be6984d82e0a41432ac5b89f7d6240eef1b9d), [b/166760797](https://issuetracker.google.com/issues/166760797))

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
- Performance optimizations for LazyColumnFor/LazyRowFor scrolling by not doing unnecessary recompositions during every scroll ([I64f65](https://android-review.googlesource.com/#/q/I64f6568fd1193a6d28e3e2e2205b977f4a5f116b), [b/168293643](https://issuetracker.google.com/issues/168293643), [b/167972292](https://issuetracker.google.com/issues/167972292), [b/165028371](https://issuetracker.google.com/issues/165028371))
- Fixed crash in LazyColumnFor/LazyRowFor after scrolling and then changing items and implemented auto scrolling up when the previously visible item was removed so we don't display empty gaps in the end anymore ([I220ab](https://android-review.googlesource.com/#/q/I220abfb686295685653eb28019318ea671eb6755), [b/161480164](https://issuetracker.google.com/issues/161480164), [b/167855468](https://issuetracker.google.com/issues/167855468))
- Nesting scrollable in the same direction containers like ScrollableContainer and LazyColumnFor is not allowed anymore. It was never supported and was breaking the fling and all the laziness of composing the items of LazyColumnFor ([I6e101](https://android-review.googlesource.com/#/q/I6e1011b2fce2b5ecebda26987a28c6feb1ef6cf7))
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
- add AccessibilityScrollState to semantics properties. ([Ifeda9](https://android-review.googlesource.com/#/q/Ifeda983f0f6b8a2a92dea82c1a594fa5607f7cc3))
- Make TextRange inline to avoid object creation. ([Id034b](https://android-review.googlesource.com/#/q/Id034bee391b277905590a94dbb7198739ad1e848))
- ParagraphConstraints is removed. Width is directly passed to Paragraph now. ([Ica712](https://android-review.googlesource.com/#/q/Ica712c3f10be8ab7e684c108b2339119f50eafb7))

### Version 1.0.0-alpha03

September 16, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha03`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha03`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..18a5639262f8504db530176550e338a5d0e2e044/compose/foundation)

**API Changes**

- InnerPadding was renamed to PaddingValues. ([I195f1](https://android-review.googlesource.com/#/q/I195f122095b02ee49bf2ee0bc7f15f0339ca027f), [b/167389171](https://issuetracker.google.com/issues/167389171))
- Usages of gravity were consistently renamed to align or alignment in layout APIs. ([I2421a](https://android-review.googlesource.com/#/q/I2421a4d640a7086079739cd0e569aef70bb48577), [b/164077038](https://issuetracker.google.com/issues/164077038))
- An alignment parameter was added to Stack, which allows specifying the default alignment for all the Stack children. ([Ie80ca](https://android-review.googlesource.com/#/q/Ie80cabdc20860227e12992b65948ba870c70f147), [b/164085265](https://issuetracker.google.com/issues/164085265))

**Bug Fixes**

- DpConstraints and APIs using it were deprecated. ([I90cdb](https://android-review.googlesource.com/#/q/I90cdbe407ae8dd69badd26cd02bbb784ba10ba6a), [b/167389835](https://issuetracker.google.com/issues/167389835))
- The parameters `minWidth` and `maxWidth` of `widthIn` were renamed to `min` and `max`. Similarly for `preferredWidthIn`, `heightIn`, `preferredHeightIn`. ([I0e5e1](https://android-review.googlesource.com/#/q/I0e5e1405083224e747c54afcf7c5db5ec7472773), [b/167389544](https://issuetracker.google.com/issues/167389544))
- Added onNode and other global methods on ComposeTestRule as the current global ones are going to be deprecated. ([Ieae36](https://android-review.googlesource.com/#/q/Ieae36a4b67a3190759e7284a638f8b755c06c1ec))
- Fixed size and position calculations in GestureScope, which caused amongst others generation of invalid swipe gestures ([Iaf358](https://android-review.googlesource.com/#/q/Iaf358bea0470bd6f0e907c6bdd901bb95bea0447), [b/166589947](https://issuetracker.google.com/issues/166589947))
- Moved `createAndroidComposeRule` and `AndroidInputDispatcher` from `androidx.ui.test.android` to `androidx.ui.test` ([Idef08](https://android-review.googlesource.com/#/q/Idef08e5b796ba14140eafd054c8aa898a3d38feb), [b/164060572](https://issuetracker.google.com/issues/164060572))

### Version 1.0.0-alpha02

September 2, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha02`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha02`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/compose/foundation)

**Bug Fixes**

- TestUiDispatcher is marked experimental ([Iae99d](https://android-review.googlesource.com/#/q/Iae99dc8853f69819d969d6c1908615e69e28fb18), [b/161247083](https://issuetracker.google.com/issues/161247083))
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

### Version 1.0.0-alpha01

August 26, 2020

`androidx.compose.foundation:foundation:1.0.0-alpha01`, `androidx.compose.foundation:foundation-layout:1.0.0-alpha01`, and `androidx.compose.foundation:foundation-text:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c93ac38a59f31e5db0eab67687532a4ba61913d5/ui)

## Version 0.1.0-dev

### Version 0.1.0-dev17

August 19, 2020

`androidx.compose.foundation:foundation:0.1.0-dev17`, `androidx.compose.foundation:foundation-layout:0.1.0-dev17`, and `androidx.compose.foundation:foundation-text:0.1.0-dev17` are released. [Version 0.1.0-dev17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/ui)

**API Changes**

- The spacedBy Arrangement was added for Row and Column, to enable positioning layout children with a fixed spacing. The aligned Arrangment was also added, to enable positioning layout children one next to the other and aligned in the Row/Column according to an Alignment. The previous Arrangement.Vertical#arrange and Arrangement.Horizontal#arrange methods were deprecated, and writing custom Arrangements will not be supported in the future. ([I6733d](https://android-review.googlesource.com/#/q/I6733d4a76e4abd5713bfacf95da696bdd6153932), [b/161985975](https://issuetracker.google.com/issues/161985975))
- Offset has become an inline class ([Iaec70](https://android-review.googlesource.com/#/q/Iaec70bb466cae8964f03e7484c1e86857c924f82))
- Removed onFocusChanged callbacks from TextField. Use Modifier.focusObserver instead. ([I51089](https://android-review.googlesource.com/#/q/I51089bfbc858ea302770f92b13886818cf48ba9c), [b/161297615](https://issuetracker.google.com/issues/161297615))
- Modifier.drawBorder has been deprecated. Use Modifier.border instead. Border data class has been replaced by BorderStroke ([I4257d](https://android-review.googlesource.com/#/q/I4257d62b222e27c9ad67e1b2581b162cc9392c9e), [b/158160576](https://issuetracker.google.com/issues/158160576))
- VerticalScroller and HorizontalScroller have been removed. Use ScrollableColumn/Row instead. Modifier.drawBackground has been removed. Use Modifier.background ([I73b0d](https://android-review.googlesource.com/#/q/I73b0d940455a0a8e8dd18b5a483b12707f599304), [b/163019183](https://issuetracker.google.com/issues/163019183))
- Remove marked as deprecated fillMax\* modifiers from LazyItemScope as they are making it harder to add such modifiers correctly for items which are not direct children of LazyColumnFor ([Ifa78d](https://android-review.googlesource.com/#/q/Ifa78d7d5956e7f1d903c03aac4fa34b8bef5c425))
- added LazyColumn/LazyRow implementation as DSL ([I93cc6](https://android-review.googlesource.com/#/q/I93cc6fbf6ba4b46561677bda17a0b16108b2bd63))
- Constraints is now an inline class ([I88736](https://android-review.googlesource.com/#/q/I88736be04376359506a2e8b4d599975c4f13aa01))
- Added the ability to size a layout to a fraction of the available space, using the fillMaxWidth, fillMaxHeight and fillMaxSize modifiers. ([I945bb](https://android-review.googlesource.com/#/q/I945bbae02b59241d993fc93c31aa81b6e3fee3c8), [b/161562591](https://issuetracker.google.com/issues/161562591))

**Bug Fixes**

- Added a modifier param to SelectionContainer ([I4aada](https://android-review.googlesource.com/#/q/I4aadafd87d5705b96f73cd49af84728a463c1cc5), [b/161487952](https://issuetracker.google.com/issues/161487952))
- Added mergePolicy lambda to SemanticsPropertyKey. This can be used to define a custom policy for mergeAllDescendants semantics merging. The default policy is to use the parent value if already present, otherwise the child value. ([Iaf6c4](https://android-review.googlesource.com/#/q/Iaf6c4cc327017ee492f4d8334c8df5167d33df58), [b/161979921](https://issuetracker.google.com/issues/161979921))
- `PlacementScope.placeAbsolute()` was renamed to `PlacementScope.place()`, and the previous `PlacementScope.place()` was renamed to `PlacementScope.placeRelative()`. As a result, the `PlacementScope.place()` method will not automatically mirror the position in right-to-left contexts anymore. If this is desired, use `PlacementScope.placeRelative()` instead. ([I873ac](https://android-review.googlesource.com/#/q/I873ac827e6c4d4bf6c85a80b7128174c61602945), [b/162916675](https://issuetracker.google.com/issues/162916675))
- Removed deprecated FilledTextField component. Please use TextField instead to get the Material Design implementation of the Filled text field. ([I5e889](https://android-review.googlesource.com/#/q/I5e88900375ee81067f24d39f82f4022bf85b3d9c))
- Added backgroundColor parameter to LinearProgressIndicator and removed internal padding from CircularProgressIndicator. Added new ProgressIndicatorConstants.DefaultProgressAnimationSpec which can be used as the default AnimationSpec when animating progress between values ([If38b5](https://android-review.googlesource.com/#/q/If38b5dd58d052b75c1974031e0974f22808d9776), [b/161809914](https://issuetracker.google.com/issues/161809914), [b/161804677](https://issuetracker.google.com/issues/161804677))
- The `state { ... }` composable is now deprecated in favor of explicit calls to `remember { mutableStateOf(...) }` for clarity. This reduces the overall API surface and number of concepts for state management, and matches the `by mutableStateOf()` pattern for class property delegation. ([Ia5727](https://android-review.googlesource.com/#/q/Ia57278556d4f35ecf2cf5e6e30888b0d1f1f8012))
- Renamed RRect to RoundRect to better fit compose naming patterns Created similar function constructors to RRect and deprecated RRect function constructors ([I5d325](https://android-review.googlesource.com/#/q/I5d32529a133bc2f69ea1de94c2912b2748a0d678))
- Removed onChildPositioned and OnChildPositionedModifier. Developers should use onPositioned and OnPositionedModifier on the child layout instead. ([I4522e](https://android-review.googlesource.com/#/q/I4522e2cd4a0edb08fd36212eacf19d2895ae87f7), [b/162109766](https://issuetracker.google.com/issues/162109766))
- IntSize is now an inline class ([I2bf42](https://android-review.googlesource.com/#/q/I2bf426245b41f4189dead45114e3791bbceb9d13))
- LongPress the Blank Area to Edit. ([Ib1e5b](https://android-review.googlesource.com/#/q/Ib1e5b6da49a1b25f4539af29c505f173c7bb6e6e))
- Hide FloatingToolbar After Tapping on the Text. ([If4525](https://android-review.googlesource.com/#/q/If452579ab2b744624c517332919dda25b1e32bd6))
- Hide FloatingToolbar When Updating the Selection. ([I8444c](https://android-review.googlesource.com/#/q/I8444c88f72e19554625cfe3fdbddc693df73c647))
- Deselect When Blur. ([I781a2](https://android-review.googlesource.com/#/q/I781a2627786bb5938f13dcd7b5e48373f5a655d0))

### Version 0.1.0-dev16

August 5, 2020

`androidx.compose.foundation:foundation:0.1.0-dev16`, `androidx.compose.foundation:foundation-layout:0.1.0-dev16`, and `androidx.compose.foundation:foundation-text:0.1.0-dev16` are released. [Version 0.1.0-dev16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c74ed7b07d1c18da576f179d55e568ca12973df..316f882e649c600372170f013a18515f590f490d/ui)

**API Changes**

- LazyItemScope was added for itemContent param of Lazy lists. It provides modifiers to fill the parent max size which solves the use case when the item should fill the viewport and the regular Modifier.fillMaxSize() doesn't work as the item is measured with infinity constraints. ([Ibd3b2](https://android-review.googlesource.com/#/q/Ibd3b21685641c22f7deaab1bb71785d8d6135058), [b/162248854](https://issuetracker.google.com/issues/162248854))
- Move dialog to ui ([I47fa6](https://android-review.googlesource.com/#/q/I47fa618a788e598182b782eab755defccaf45ebb))
- Added LazyColumnForIndexed/LazyRowForIndexed - versions of LazyColumnFor/LazyRowFor which provides both index and item in the itemCallback. It is useful when in addition to a current item you need to know a current index. ([I65ff3](https://android-review.googlesource.com/#/q/I65ff336f568c18bd875157e67ece1f8da6985d4c))
- Modifier.deternimateProgress has been renamed to Modifier.progressSemantics ([I9c0b4](https://android-review.googlesource.com/#/q/I9c0b48e0b7969a842a114b50c86d8c37799ede1d))
- LazyColumnItems was renamed to LazyColumnFor. LazyRowItems was renamed to LazyRowFor ([I84f84](https://android-review.googlesource.com/#/q/I84f843793994276f1ccb9f21464c4b74629aaf12))
- Add some Marks/Annotations for best practice reason. ([I66b20](https://android-review.googlesource.com/#/q/I66b206ffe0fe1a5ceb88bf0b0a2b0d84f2c3f6bd))
- foundation.shape.corner package were flatten to foundation.share ([I46491](https://android-review.googlesource.com/#/q/I464919cb74f8941c2a02f14dea0aa417febf3691), [b/161887429](https://issuetracker.google.com/issues/161887429))
- Added сrossaxis gravity param for LazyRowItems/LazyColumnItems. LazyRowItems/LazyColumnItems now support wrap content behaviour. ([Ib39fc](https://android-review.googlesource.com/#/q/Ib39fc1d1ec28db109f05d191ad80570230e985cd))
- ZoomableState has been renamed to ZoomableController. Custom curve support has been added for smoothScale. `enabled` and `onZoomStarted` functionality has been added ([If8b8f](https://android-review.googlesource.com/#/q/If8b8fa81e13136f225a94b87f55d7f1c51fb6747))
- Material FilledTextField was renamed to TextField and foundational TextField was renamed to BaseTextField to make simplest desired API easy to discover and use ([Ia6242](https://android-review.googlesource.com/#/q/Ia62420a7a2231c02b6874a9a2867bf786a397ed3), [b/155482676](https://issuetracker.google.com/issues/155482676))
- Previously deprecated AdapterList has been removed. Use LazyColumnItems instead ([I12b9b](https://android-review.googlesource.com/#/q/I12b9b009a56b669f7024ae5e2e8fb9e5cb9f8d98))
- Modifier.drawBackground has been renamed to Modifier.background ([I13677](https://android-review.googlesource.com/#/q/I1367723fce0e07418ed4ab391fe20c69aa092f53))
- The old ConstraintLayout DSL was removed. ConstraintSet2 has been renamed to ConstraintSet. ([If58d1](https://android-review.googlesource.com/#/q/If58d10ec7933bb5b3cd71f6b0ec257839b0309dc), [b/162450908](https://issuetracker.google.com/issues/162450908))
- Added Modifier.absoluteOffset() and Modifier.absoluteOffsetPx(). Unlike offset modifiers, absolute offset modifiers will not auto-mirror in right-to-left context ([I3aa21](https://android-review.googlesource.com/#/q/I3aa2155766e3989cbf703e48f71daaf079a63f8e))
- `Row` and `Column` are now inline function significantly reducing the overhead of using them. ([I75c10](https://android-review.googlesource.com/#/q/I75c10e663b74ffc250a3293df7583fcd86ea891a))

**Bug Fixes**

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
- Added MonotonicFrameAnimationClock that enables you to use a
  MonotonicFrameClock as an AnimationClockObservable to bridge the gap
  between the new coroutines based clocks and APIs that still use the old
  callback based clocks.

  The MonotonicFrameClock equivalent of ManualAnimationClock is now
  ManualFrameClock. ([I111c7](https://android-review.googlesource.com/#/q/I111c7b7182a1495f95eab1bb808d3acd6af82447), [b/161247083](https://issuetracker.google.com/issues/161247083))
- Removed `SemanticsNodeInteraction.performPartialGesture`. Use
  `SemanticsNodeInteraction.performGesture` instead. ([Id9b62](https://android-review.googlesource.com/#/q/Id9b628ebe475c8a067118320b26a7b2461e98129))

- Renamed `SemanticsNodeInteraction.getBoundsInRoot()` to
  `SemanticsNodeInteraction.getUnclippedBoundsInRoot()` ([Icafdf](https://android-review.googlesource.com/#/q/Icafdf63b2e2f03f48d5b51371e733917dedcf422), [b/161336532](https://issuetracker.google.com/issues/161336532))

- The APIs for right-to-left support has been updated. LayoutDirectionAmbient has been added, which can be used to read and change the layout direction. Modifier.rtl and Modifier.ltr have been removed. ([I080b3](https://android-review.googlesource.com/#/q/I080b3cb674dc32af5fbe7e696228ac21f0720d72))

- Modifier.plus has been deprecated, use Modifier.then instead. 'Then' has a stronger signal of ordering, while also prohibits to type `Modifier.padding().background() + anotherModifier`, which breaks the chain and harder to read ([Iedd58](https://android-review.googlesource.com/#/q/Iedd587edbed0ba964ef203a66b98be7297147bd7), [b/161529964](https://issuetracker.google.com/issues/161529964))

- Added `isFocused()` and `isNotFocused()` SemanticsMatcher. ([I0b760](https://android-review.googlesource.com/#/q/I0b760d316a616ab385fa421b080edefee8e27681))

- RemeasurementModifier was added. It allows users to synchronously remeasure the layout. In general, you never need it as remeasure/relayout is happening automatically, but we use it inside LazyColumnItems during the scroll. ([I5f331](https://android-review.googlesource.com/#/q/I5f33173ba1f76153139fa086fef4e2a86d010282), [b/160791058](https://issuetracker.google.com/issues/160791058))

- isSystemInDarkTheme now always considers the system-wide dark theme setting, and ignores power saving status before Q, following latest guidance. ([I0c10c](https://android-review.googlesource.com/#/q/I0c10c14676fa25da477d9faff50e58a46eb4cee8))

- OnChildPositioned has been deprecated. Use OnPositioned
  on the child instead. ([I87f95](https://android-review.googlesource.com/#/q/I87f95da597607cbc534647def3b1a39527dcdeaa), [b/162109766](https://issuetracker.google.com/issues/162109766))

- Renamed AndroidComposeTestRule to createAndroidComposeRule. ([I70aaf](https://android-review.googlesource.com/#/q/I70aaf550e1bff2871b9732cc5abf58e9af1479fe))

- Add accessibility action to get TextLayoutResult ([I9d6e6](https://android-review.googlesource.com/#/q/I9d6e6313528500524f04638ccb5742fcfbb41392))

### Version 0.1.0-dev15

July 22, 2020

`androidx.compose.foundation:foundation:0.1.0-dev15`, `androidx.compose.foundation:foundation-layout:0.1.0-dev15`, and `androidx.compose.foundation:foundation-text:0.1.0-dev15` are released. [Version 0.1.0-dev15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/ui)

To use the `0.1.0-dev15` version of Compose, you will need to:

#### Dependencies Update

- To use the `0.1.0-dev15` version of Compose, you will need to update your dependencies according to the new code snippets shown above in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose-foundation#declaring_dependencies).

**API Changes**

- Similarly to the new param in ScrollableColumn/ScrollableRow LazyColumnItems/LazyRowItems now also have contentPadding param which allows to add a padding for the content after it has been clipped, which is not possible via just a modifier param. It also allows to add a spacing only before first item/after last item. ([Ibc24e](https://android-review.googlesource.com/#/q/Ibc24e9e194f9cd7cd4c24c2b843eb5be39266b35))
- onFocusChange callback in text fields renamed to onFocusChanged ([Ida4a1](https://android-review.googlesource.com/#/q/Ida4a1a55e5a9119c3a740d28ad2e0d9126d40853))
- VerticalScroller and HoriziontalScroller have been deprecated. Use ScrollableColumn and ScrollableRow for build-in experience with Column/Row behaviour and parameters, or Modifier.verticalScroll and Modifier.horizontalScroll on your own element. Similarly, ScrollerPosition has been deprecated in favor of ScrollState' ([I400ce](https://android-review.googlesource.com/#/q/I400ce0e6c0e33aa865e0e49defef1eb92ac40a93), [b/157225838](https://issuetracker.google.com/issues/157225838), [b/149460415](https://issuetracker.google.com/issues/149460415), [b/154105299](https://issuetracker.google.com/issues/154105299))
- Modifier.draggable and Modifier.scrollable APIs were reworked. DragDirection was removed in favor of Orientation. State required for scrollable has beed simplified. ScrollableState has been renamed to ScrollableController ([Iab63c](https://android-review.googlesource.com/#/q/Iab63cb65002471a5173f387f7bc6720aa929f9e6), [b/149460415](https://issuetracker.google.com/issues/149460415))
- Single-value semantics properties now use a calling style. For example, 'semantics { hidden = true }' is now written as: `semantics { hidden() }`. ([Ic1afd](https://android-review.googlesource.com/#/q/Ic1afd12ea22c926babc9662f1804d80b33aa0cfc), [b/145951226](https://issuetracker.google.com/issues/145951226), [b/145955412](https://issuetracker.google.com/issues/145955412))
- Corner sizes used by RoundedCornerShape and CutCornerShape can now be larger than 50% ([Id2340](https://android-review.googlesource.com/#/q/Id2340cc5b2c3e2c8a95c9318b1110b840864dd97), [b/160400213](https://issuetracker.google.com/issues/160400213))
- Changed the default ContentScale parameter for the Image composable from Inside to Fit. This was done in order to get behavior to scale up the underlying Painter if the layout size is larger than the intrinsic size of the painter while maintaining the aspect ratio. This behavior better matches expectations for providing fixed sizes to the Image while not affecting the default behavior if only the intrinsic size is used to compute the size of the composable. ([I40ae3](https://android-review.googlesource.com/#/q/I40ae3af9b6a2efc3d730ea0ba5f457a788eca1f7), [b/159838006](https://issuetracker.google.com/issues/159838006))
- Use AnimationSpec instead of AnimationBuilder in the top level APIs to clarify the concept of static animation specification -Improve the transition DSL by removing the lambda requirement for creating AnimationSpecs such as tween, spring. They instead take constructor params directly. -Improve the overall ease of use of AnimationSpec opening up constructors instead of relying on builders -Change the duration and delay for KeyFrames and Tween to Int. This eliminates unnecessary type casts and method overloading (for supporting both Long and Int). ([Ica0b4](https://android-review.googlesource.com/#/q/Ica0b4cb42996d3d30f9b6dacdbe149c75af77341))
- Clickable was removed. Use Modifier.clickable ([I84bdf](https://android-review.googlesource.com/#/q/I84bdf2bc75e8ccda44afbe9db49d4c879703309b))
- Added LazyRowItems - Horizontally scrolling analogue of LazyColumnItems ([Ibbcf7](https://android-review.googlesource.com/#/q/Ibbcf7fdd13264dbeda6b95d927b6bdc77cf27486))
- Introduced low level stateless animation APIs. These APIs ([I63bf7](https://android-review.googlesource.com/#/q/I63bf7d28d5ac5e5ca2caaa427ee7643828c848a5))
- androidx.ui.foundation.TextFieldValue and androidx.ui.input.EditorValue is deprecated. TextField, FilledTextField and CoreTextField composables that uses that type is also deprecated. Please use androidx.ui.input.TextFieldValue instead ([I4066d](https://android-review.googlesource.com/#/q/I4066d1f4d2e3e3514753aa3495680292dc55f89d), [b/155211005](https://issuetracker.google.com/issues/155211005))
- Replaced usage of IntPx with Int. Replaced IntPxPosition with IntOffset. Replaced IntPxSize with IntSize. ([Ib7b44](https://android-review.googlesource.com/#/q/Ib7b44d92ce3aff86c606753f0ac5c3122b71041d))
- androidx.ui.foundation.shape.RectangleShape removed; use androidx.ui.graphics.RectangleShape ([I94939](https://android-review.googlesource.com/#/q/I94939a33873c808440fa8256627e16a79e88472c), [b/154507984](https://issuetracker.google.com/issues/154507984))
- In order to consolidate the number of classes used to represent sizing information, standardize on usage of the Size class instead of PxSize. This provides the benefits of an inline class to leverage a long to pack 2 float values to represent width and height represented as floats. ([Ic0191](https://android-review.googlesource.com/#/q/Ic019171b52d2f24d262d9c47ac964728cdc1ee8b))
- In order to consolidate the number of classes used to represent positioning information, standardize on usage of the Offset class instead of PxPosition. This provides the benefits of an inline class to leverage a long to pack 2 float values to represent x and y offsets represented as floats. ([I3ad98](https://android-review.googlesource.com/#/q/I3ad983207bc37af20afac03e2cd09b4240777687))
- Added Modifier.zoomable for pinch-to-zoom functionality ([Id5d63](https://android-review.googlesource.com/#/q/Id5d63ff7d29f9dedd6d9d28df2ce74081a892cda))
- Toggleable component has been deprecated. Use Modifier.toggleable instead ([I35220](https://android-review.googlesource.com/#/q/I35220fca0d9d11198d1158cb905cfb2586965a34), [b/157642842](https://issuetracker.google.com/issues/157642842))
- MutuallyExclusiveSetItem has been deprecated. Use Modifier.selectable instead. ([I02b47](https://android-review.googlesource.com/#/q/I02b473710e5a654427b51565c0b950392f68fcff), [b/157642842](https://issuetracker.google.com/issues/157642842))
- TestTag is now deprecated. Use Modifier.testTag instead. ([If5110](https://android-review.googlesource.com/#/q/If5110df5865f5933d10d54a8aacba58f8cd1c712), [b/157173105](https://issuetracker.google.com/issues/157173105))
- Adds fontWeight parameter to Text, which was accidentally not added previously ([I56937](https://android-review.googlesource.com/#/q/I5693777e720aed4b890c10fcbcd3949c66b24a0e))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters ([I19d02](https://android-review.googlesource.com/#/q/I19d02beca10c30e9b6b444be0c2dd21227e30e9c))
- VerticalScroller now provides Column out of the box. HorizontalScroller now provides Row out of the box. ([Ieca5d](https://android-review.googlesource.com/#/q/Ieca5d185b9f6e950a7175b9daa7a9a511a439da2), [b/157020670](https://issuetracker.google.com/issues/157020670))
- Replaced usage of Px class in various compose classes as part of the large refactoring effort to only rely on Dp and primitive types for pixel parameters ([Iede0b](https://android-review.googlesource.com/#/q/Iede0b310a8a8f4a39ba6ae4a99c753f7f590d8ed))
- Modifier.indication has been added to foundation package. Use it to show press/drag/other indication on your custom interactable elements ([I8425f](https://android-review.googlesource.com/#/q/I8425fc70afc4d2815f937f8514352ce831e692ae), [b/155287131](https://issuetracker.google.com/issues/155287131))
- VerticalScroller and HorizontalScroller now support reversed scrolling is isReversed is set on ScrollerPosition ([I953bd](https://android-review.googlesource.com/#/q/I953bd0d7f4b036a030eeb29e4596d02c67dc35a1))
- Support adding composables into text layout. ([I1373c](https://android-review.googlesource.com/#/q/I1373cd3bcc4e9d6a70f822c520f0b4ee9ff1bc5b))
- Consolidated CanvasScope implementations so there is now just DrawScope and ContentDrawScope Renamed CanvasScope to DrawScope. Updated DrawScope to implement Density interface and provide LayoutDirection Deleted DrawScope subclass in ContentDrawScope Painter and PainterModifier have been updated to no longer maintain an RTL property themselves as DrawScope provides this already without manually providing it ([I1798e](https://android-review.googlesource.com/#/q/I1798e4b2b325297c3b5394aa99be3db935e369b7))
- Removed deprecated DrawBackground API in favor of drawBackground extension APIs on Modifier. Refactored color, brush and paint drawBackground implementations to reduce code paths as well as remove requirement for Modifier to be created as part of composition. ([I0343a](https://android-review.googlesource.com/#/q/I0343a0d32684e77f9bc72c9cf68ce55d92ec575d))
- Updated higher level compose APIs that expose a Canvas to expose CanvasScope instead. This removes the need for consumers to maintain their own Paint objects. For consumers that still require access to a Canvas they can use the drawCanvas extension method which provides a callback to issue drawing commands with the underlying Canvas. ([I80afd](https://android-review.googlesource.com/#/q/I80afdf4c0a648962aa6ef1efc05b1d3b65757094))
- HorizontalScroller and VerticalScroller not restores their scroll position using saved instance state. ([Ia0fae](https://android-review.googlesource.com/#/q/Ia0fae1fe0df60d85302255acb8577cd8e769d297), [b/155075048](https://issuetracker.google.com/issues/155075048))
- FocusManagerAmbient is removed. Use FocusModifier.requestFocus to obtain focus. ([Ic4826](https://android-review.googlesource.com/#/q/Ic482662c18a1cb41f097a1e0bcc114d517b756b7))
- Table layout was removed temporarily until we will make it available again with a refreshed API. ([Id88a7](https://android-review.googlesource.com/#/q/Id88a7d9c0a4de2c1abd4f030c27f77f73fa21bb3))
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
- ColoredRect has been removed. User Box with drawBackground modifier instead ([I983c7](https://android-review.googlesource.com/#/q/I983c7fe9b61d873421278caf1c46ff9461307642), [b/152753731](https://issuetracker.google.com/issues/152753731))

- Add cursor color customisation to the TextField ([I6e33f](https://android-review.googlesource.com/#/q/I6e33fa47950cddb5d3631528cd954c48a3f255d2))

- Now it is possible to hide/show software keyboard by using
  SoftwareKeyboardController which is delivered by onTextInputStarted
  callback ([I8dc44](https://android-review.googlesource.com/#/q/I8dc44f64d4f457339364b9624c0b3e946cdf01b3), [b/151860051](https://issuetracker.google.com/issues/151860051))

- TextFieldValue used with TextField can now be survive activity recreation when used like this: `var text by savedInstanceState(saver = TextFieldValue.Saver) { TextFieldValue() }` ([I5c3ce](https://android-review.googlesource.com/#/q/I5c3cee62fa592dd00c1595efc6ea950b8aeda676), [b/155075724](https://issuetracker.google.com/issues/155075724))

- Adds commonly used parameters to Text(). If you are currently creating a local text style to pass a small number of these parameters, such as `Text(style = TextStyle(textAlign = TextAlign.Center))`, you can now just provide the parameters directly: `Text(textAlign = TextAlign.Center)` ([I82768](https://android-review.googlesource.com/#/q/I8276873965f3588ed2cbc560f70a9ddd2405027b))

- Replaced CoreTextField/TextField focusIdentifier
  parameter with FocusNode in order to integrate with focus subsystem. ([I7ea48](https://android-review.googlesource.com/#/q/I7ea4842b2acff06658b0731c55c877301b524757))

- TextField update - in horizontal dimension it will occupy all available space granted to it ([Ib08df](https://android-review.googlesource.com/#/q/Ib08dfc0363c5a3521f68c750ba6dc490a25081d3), [b/154638552](https://issuetracker.google.com/issues/154638552))

- Added InteractionState and Interaction, making it easier to build components that react to UI state changes such as press, and drag ([Icfe25](https://android-review.googlesource.com/#/q/Icfe2590a97f5df73e999334b88dd69faa91651b7), [b/152525426](https://issuetracker.google.com/issues/152525426))

- RectangleShape moved from androidx.ui.foundation.shape.\* to androidx.ui.graphics.\* ([Ia74d5](https://android-review.googlesource.com/#/q/Ia74d5a3bbe2ee3a28bbddb57a2aef2607679d4ac), [b/154507984](https://issuetracker.google.com/issues/154507984))

- Replaced all nullable Color uses in API with
  non-nullable and use Color.Unset instead of null ([Iabaa7](https://android-review.googlesource.com/#/q/Iabaa7c6334857833cdb0d5958f062e2e576bd240))

- TextField API update - merged onFocus and onBlur callbacks into a single onFocusChange(Boolean) callback with parameter ([I66cd3](https://android-review.googlesource.com/#/q/I66cd3b14d1df6bfbaafc25e501995368d69138ec))

- Renamed ScaleFit to ContentScale
  Moved ContentScale from ui-graphics to ui-core
  module to live in the same module as the Alignment
  API.
  Renamed FillMaxDimension to Crop
  Renamed FillMinDimension to Fit
  Renamed Fit to Inside to better match
  ImageView.ScaleType equivalents
  Added documentation indicating that the combination
  of Crop and Alignment.Center achieves the same result
  as ImageView.ScaleType.CENTER_CROP and Fit
  used with Alignment.Center achieves the same result as
  ImageView.ScaleType.FIT_CENTER
  Inside used with Alignment.Center achieves the same
  result as ImageView.ScaleType.CENTER_INSIDE ([I45f09](https://android-review.googlesource.com/#/q/I45f09c681afda9c83483b20405ec21292593b41a), [b/152842521](https://issuetracker.google.com/issues/152842521))

- Removes ProvideContentColor, instead just use ContentColorAmbient directly with `Providers` ([Iee942](https://android-review.googlesource.com/#/q/Iee94234bfe6f820445b3d3d986895b293271753e))

- Adds color parameter to text, allowing overriding the color of the text style without needing to manually merge with the style provided in a theme. ([I41a66](https://android-review.googlesource.com/#/q/I41a6676070cdb4d2dac91bf3c6422007db7f7276))

- Improve DrawModifier API:

  - Made the receiver scope for draw() ContentDrawScope
  - Removed all parameters on draw()
  - DrawScope has same interface as former CanvasScope
  - ContentDrawScope has drawContent() method ([Ibaced](https://android-review.googlesource.com/#/q/Ibaced5feb8778510b8fe78e96f4fd3da1a6fda50), [b/152919067](https://issuetracker.google.com/issues/152919067))
- ColoredRect has been deprecated. Use `Box(Modifier.preferredSize(width, height).drawBackground(color))` instead. ([I499fa](https://android-review.googlesource.com/#/q/I499fa26b66b128943500fbdf9ba490d754adf561), [b/152753731](https://issuetracker.google.com/issues/152753731))

- Shape theming system is updated according to the Material design specification. Now you can provide small, medium and large shapes to be used by most of the components ([Ifb4d1](https://android-review.googlesource.com/#/q/Ifb4d152de62f71c6b1759c73702752673aa27c7d))

- Replaced Modifier plus operator with factory extension functions ([I225e4](https://android-review.googlesource.com/#/q/I225e444f50956d84e15ca4f1378b7f805d54e0ca))

- Draggable has been moved to modifier ([Id9b16](https://android-review.googlesource.com/#/q/Id9b16db6942de069e8d2221f192525b3bc71ab7d), [b/151959544](https://issuetracker.google.com/issues/151959544))

- Moved `Text` to androidx.ui.foundation package, from androidx.ui.core. ([I87ce5](https://android-review.googlesource.com/#/q/I87ce56618b325d7fcf221262fdd468840619dc7f))

- add `enabled` param to Checkbox, Switch and Toggleable ([I41c16](https://android-review.googlesource.com/#/q/I41c1634c860ab068308d33d7e1a0547ad79adbdb))

- Ripple is now a Modifier. While Clickable is not yet converted the recommended usage is `Clickable(onClick = { ... }, modifier = ripple())` ([Ie5200](https://android-review.googlesource.com/#/q/Ie52007f6948838a64fb25dba4dfbb7853d0e442f), [b/151331852](https://issuetracker.google.com/issues/151331852), [b/150060763](https://issuetracker.google.com/issues/150060763))

- Added VectorPainter API to
  replace existing subcomposition API for
  vector graphics. Result of subcomposition
  is a VectorPainter object instead of a
  DrawModifier. Deprecated previous DrawVector
  composables in favor of VectorPainter.

  Renamed `Image(Painter)` API to `PaintBox(Painter)`
  Created Vector composable that behaves like the
  Image composable except with a VectorAsset instead
  of an ImageAsset ([I9af9a](https://android-review.googlesource.com/#/q/I9af9a365eb744e0cdb343cf424f4df5160d6c2b4), [b/149030271](https://issuetracker.google.com/issues/149030271))
- Created Image composable to handle
  sizing/layout in addition to drawing a given
  ImageAsset to the screen. This composable
  also supports drawing any arbitrary Painter
  instance respecting its intrinsic size
  as well as supporting a given fixed
  size or minimum size ([Ibcc8f](https://android-review.googlesource.com/#/q/Ibcc8f4d61cf0a0fbe697055ee2b6bfe8568755ed))

- Button, FloatingActionButton and Clickable now have a separate `enabled` param. Some of the params on Button were renamed or reordered. ([I54b5a](https://android-review.googlesource.com/#/q/I54b5ac613632c1cd804b756d3ad2ccb7a475a149))

- Renamed Image to ImageAsset to better differentiate
  the difference between the Image data and the upcoming
  Image composable used to participate in layout and draw
  content.

  Created extension method on android.graphics.Bitmap,
  `Bitmap.asImageAsset()`, to create an instance of an
  ImageAsset useful for combining traditional Android
  application development with the compose framework. ([Id5bbd](https://android-review.googlesource.com/#/q/Id5bbdf3fe1cf68750a76bb955b20e06d1f81a71e))
- DrawImage composable was removed. Use ImagePainter to draw image on existing layout, or SimpleImage to introduce Image that takes space ([I595e1](https://android-review.googlesource.com/#/q/I595e1cac09eb1d275b3b1ded2c2ce05b3f4b41bb), [b/149827027](https://issuetracker.google.com/issues/149827027))

- Stack component supports right-to-left directionality ([Ic9e00](https://android-review.googlesource.com/#/q/Ic9e00dfc5b8c16ff305c14bc38de38cdf72d4cf5))

- Added Icon, IconButton and IconToggleButton, removing AppBarIcon.
  You can directly replace existing usages of AppBarIcon with IconButton,
  and they will now have the correct touch target. See the samples for
  usage information, and see Icons for the provided Material Icons
  you can use directly with these components. ([I96849](https://android-review.googlesource.com/#/q/I9684914dcde197df74d11f1173d827cd902e8832))

- DrawShape composable was removed. Use DrawBackground modifier instead. ([I7ceb2](https://android-review.googlesource.com/#/q/I7ceb270c8571b3cb1cdc8b0494d90c985f61b3d7))

- Added AdapterList, a scrolling list component that only
  composes and lays out the visible items. Currently known issues
  include that it is vertical-only and does not fully handle all
  cases of changes to its children. ([Ib351b](https://android-review.googlesource.com/#/q/Ib351be89aabb59dac29806a935e377e90a2da9c2))

- Scrollable component has been added, which allows creation of custom Scrollers/Lists ([I5fd37](https://android-review.googlesource.com/#/q/I5fd372b89269ffe08db8fe27238ec9dc0f9d84a1))

- Renamed background to DrawBackground and make it to be memorized by default ([Ia0bd3](https://android-review.googlesource.com/#/q/Ia0bd3f7657dc66ae6f492ccfcf88c44ba92bb7e0))

- Add paddings, border, shape and background param to Box ([I05027](https://android-review.googlesource.com/#/q/I05027a87956b6e4233a6b8992d321633e9fdcdc9), [b/148147281](https://issuetracker.google.com/issues/148147281))

- Added Canvas component. This composable takes up some size (provided by user) and allows you to draw using CanvasScope ([I0d622](https://android-review.googlesource.com/#/q/I0d62259da4f70e68e57ed1b20cdc9b9aa3d8b1be))

- rename `Border` modifier to `DrawBorder` ([I8ffcc](https://android-review.googlesource.com/#/q/I8ffccaa928e74efd71dcdcda550f250195f2e5d3))

- Added Box component for combining layout and drawing common functionality. ([I6e2a7](https://android-review.googlesource.com/#/q/I6e2a71af98e847124a5944b1cbe9fee82d886b3b))

- Scrollers now exhibit native Android fling motion behavior. ([I922af](https://android-review.googlesource.com/#/q/I922af68261f3f1e81538a98a7575603e531fc035), [b/147493715](https://issuetracker.google.com/issues/147493715))

- Replaced DrawBorder in favor of Border Modifier ([Id335a](https://android-review.googlesource.com/#/q/Id335a8c2526693f8eb9d440c8d25341029f5de89))

- Modifier.tag was renamed to Modifier.layoutId, to avoid confusion with Modifier.testTag. ([I995f0](https://android-review.googlesource.com/#/q/I995f09d0722964ad8a5708c7299e4c6f52bec1c5))

- The percent parameter when creating ConstraintLayout guidelines has been renamed to fraction. ([Ida2db](https://android-review.googlesource.com/#/q/Ida2db05016958daba8ebaf7cbb5cc5fbe5f0a4dc))

- Added support for margins of ConstraintLayout barriers. ([I47ffe](https://android-review.googlesource.com/#/q/I47ffedafd3cfd3a1164763224f8c6a61c0d1588e))

- Fixed RTL support in ConstraintLayout. Added RTL unaware APIs. ([I3b1c7](https://android-review.googlesource.com/#/q/I3b1c75b837ef54b48306fe7938ec1d0444488d0b))

- A new DSL for ConstraintLayout has been added. Please see the samples for more details. ([Icaa9a](https://android-review.googlesource.com/#/q/Icaa9abed35747c227aa53f9365e7ec1100e81759))

- Added the @ExperimentalLayout annotation. ConstraintLayout, FlowRow and FlowColumn are now tagged with it to mark that their APIs are going to change. ([I412a8](https://android-review.googlesource.com/#/q/I412a82b5d6389a7cc99fb2da01aef6cae01aca0c))

- `Modifier.padding(InnerPadding)` has been added ([I94985](https://android-review.googlesource.com/#/q/I94985666c03d8bf2748dfb9524ebc3df5d09b1ae), [b/157133803](https://issuetracker.google.com/issues/157133803))

- Removed deprecated RowAlign, ColumnAlign in Row and Column. ([If60d4](https://android-review.googlesource.com/#/q/If60d4b94486fdd3fa7c768905827c3b6594bffda), [b/155858731](https://issuetracker.google.com/issues/155858731))

- Removed deprecated LayoutTag(), please use Modifier.tag() instead.
  Removed deprecated Modifier.matchParent(), please use Modifier.matchParentSize() instead. ([If8044](https://android-review.googlesource.com/#/q/If8044397663695ed258a1c8f8c01caa70ff2064f))

- Added the offsetPx layout modifier, which can be used to define (dynamic) offsets in px. ([I5af57](https://android-review.googlesource.com/#/q/I5af57f262d283f5220779c7dbca3aa9b2b1f9c06))

- AlignmentLineOffset composable is deprecated, please use relativePaddingFrom() modifier instead. CenterAlignmentLine composable is removed. ([I60107](https://android-review.googlesource.com/#/q/I601076f5ba044b176e07115a1916cdee71083163))

- Added defaultMinSizeConstraints layout modifier, which sets size constraints to the wrapped layout only when the incoming corresponding constraints are unspecified (0 for min constraints and infinity for max constraints). ([I311ea](https://android-review.googlesource.com/#/q/I311eaf525d05eea9f657f583da7fdf845ad8d64f), [b/150460257](https://issuetracker.google.com/issues/150460257))

- Container has been removed. Use Box instead ([Ibbc2b](https://android-review.googlesource.com/#/q/Ibbc2b13b68d04a708211e6477a7e4fbd13f34ac6), [b/151407926](https://issuetracker.google.com/issues/151407926))

- Removed deprecated LayoutWidth/Height/Size modifiers. ([Ib0bc1](https://android-review.googlesource.com/#/q/Ib0bc1a7d59645ce2f4f8cea071535d89aeb80018))

- Added default parameter values for the offset modifier. ([I37f06](https://android-review.googlesource.com/#/q/I37f06c0dc49f89601e6688c5fa0eadaf8ff3d822))

- Added symmetric padding modifier. ([I39840](https://android-review.googlesource.com/#/q/I39840a44ea3ff9cbf17dc1c073b1d142d59b02ec))

- Removed deprecated LayoutAspectRatio modifier. ([I65a74](https://android-review.googlesource.com/#/q/I65a74e1b962cfe5de21ca2b8adbbb610ddac456f))

- Removed deprecated LayoutAlign modifiers. ([I10877](https://android-review.googlesource.com/#/q/I108771c0374a5c6f88a610549ddae220eab30a4f))

- Fixed a bug in the width and height modifiers that was causing the wrapped layout to be measured with no opposite axis constraints. ([I210b8](https://android-review.googlesource.com/#/q/I210b84ad765c3ab33e593f027245ab135dd036f4), [b/154797971](https://issuetracker.google.com/issues/154797971))

- Added verticalGravity and horizontalGravity parameters to Row and Column, respectively. ([I7dc5a](https://android-review.googlesource.com/#/q/I7dc5a4e757370075657be68e6eda68e7498228fa))

- Updated wrapContentWidth and wrapContentHeight to expect vertical or horizontal Alignment rather than any Alignment. The gravity modifier was updated to accept vertical or horizontal Alignment. Row, Column and Stack were updated to support custom continuous Alignments. ([Ib0728](https://android-review.googlesource.com/#/q/Ib07281752fa9806a13e61823e00accb26f99c1f6))

- Made Alignment instantiable with arbitrary values. Added 1D Alignments. ([Ia0c05](https://android-review.googlesource.com/#/q/Ia0c05cfa122108b48ac22de310ee98e0460f7f3f))

- Renamed EdgeInsets to InnerPadding. Renamed innerPadding parameter of Material Buttons to paddding. ([I66165](https://android-review.googlesource.com/#/q/I66165851232da7635a34b6bb3af7ef8dc38e3e3d))

- alignToSiblings now accepts a Measured instead of Placeable. ([I5788d](https://android-review.googlesource.com/#/q/I5788dd1dab4d18c475e51a1e9a0440aba2bbc794))

- Added modifiers for sizing to intrinsic measurements and deprecated the components serving this purpose. ([I8295d](https://android-review.googlesource.com/#/q/I8295d57e17ba8ca83ea170713fc57ea7baea52fb))

- Added support for customizing dimensions of children of ConstraintLayout ([Idb1a5](https://android-review.googlesource.com/#/q/Idb1a50e90b4c1199ee693b9261a55458dd6642e1))

- Removed deprecated Wrap and Center composables. ([I29e23](https://android-review.googlesource.com/#/q/I29e238298bd43cc9c13d3b3a8315992ce02fb60c))

- Added LayoutModifier2, a new API for defining layout modifiers; deprecated LayoutModifier ([If32ac](https://android-review.googlesource.com/#/q/If32acbfac08c677b80f9e4d5f624fe15c95ac60d))

- RowScope and ColumnScope members are now accessible outside Row and Column. ([I3a641](https://android-review.googlesource.com/#/q/I3a6415334c145f6a3f610d7852c4d2478371e6e6))

- Container has been deprecated. Use Box instead. ([I675ce](https://android-review.googlesource.com/#/q/I675ced9614fad98dfb90c0ad37583648766cb089), [b/151407926](https://issuetracker.google.com/issues/151407926))

- Added the LayoutOffset modifier for offsetting layout position ([I0b8a3](https://android-review.googlesource.com/#/q/I0b8a37b9b7d11cf48b7bbe37a95cc262720dadf4))

- Initial support for Rtl in Compose layout ([Ia5519](https://android-review.googlesource.com/#/q/Ia5519f42c6ded656242321a92c8c8069c2f42ab7))

- Updated LayoutAlign to not fill the available space anymore ([I2b14f](https://android-review.googlesource.com/#/q/I2b14f4378d92a69c32c3b4f1b8de8a31e15ec400))

- Removed AspectRatio composable in favor of modifier. Deleted
  obsolete FlexColumn, FlexRow composables and Spacing modifier ([Iec8a7](https://android-review.googlesource.com/#/q/Iec8a7b87c9130310a9d80ab82cd166738c99a3df))

- Removed the LayoutInflexible modifier for Row and Column ([I0d820](https://android-review.googlesource.com/#/q/I0d820be3157459fdabd9550a57ee7407b3c3ae69))

- Implement Drag Selection Handles to change selection for TextField. ([I27032](https://android-review.googlesource.com/#/q/I27032ee670131726d579612591dafcf3d60680b6))

- Implements LongPressAndDrag for TextField Selection. ([I17919](https://android-review.googlesource.com/#/q/I17919b9c1514c8fa7d2b54062e4acc47e7685c8e))

**Bug Fixes**

- FocusModifier is deprecated in favor of Modifier.focus, Modifier.focusRequester, Modifier.focusObserver. FocusState and FocusDetailedState are deprecated in favor of FocusState2 ([I46919](https://android-review.googlesource.com/#/q/I469196b76ebe08130fa4df9ed297f111abddd8b1), [b/160822875](https://issuetracker.google.com/issues/160822875), [b/160922136](https://issuetracker.google.com/issues/160922136))
- `runOnIdleCompose` renamed to `runOnIdle` ([I83607](https://android-review.googlesource.com/#/q/I836071f1c3c63d21417a531f336f8a93ca13f9ed))
- Several testing APIs were renamed to be more intuitive. All findXYZ APIs were renamed to onNodeXYZ. All doXYZ APIs were renamed to performXYZ. ([I7f164](https://android-review.googlesource.com/#/q/I7f164b42b04196f023c4a2153d66825487998de4))
- Removes previously deprecated Modifier.ripple. Clickable now uses ripple as the default indication (if you have a MaterialTheme {} set in your application) so in most cases you can just use clickable and get ripple indication for free. If you need to customize the color / size / bounded parameter for the ripple, you can manually create a RippleIndication and pass it to clickable as the indication parameter. ([I663b2](https://android-review.googlesource.com/#/q/I663b2fcbdc3079343b54dcf713f5d467e39b87a5), [b/155375067](https://issuetracker.google.com/issues/155375067))
- Removed obsolete size testing APIs. ([Iba0a0](https://android-review.googlesource.com/#/q/Iba0a086e8c88cf44684cba56766792614201ba30))
- Made LayoutNode experimental API ([I4f2e9](https://android-review.googlesource.com/#/q/I4f2e93737020b0993f8ba5671e2a0a87f5de3ce2))
- Version 1 of scroll orientation locking is implemented across Compose. ([I1ce7a](https://android-review.googlesource.com/#/q/I1ce7ae095c2af931e040411458a47cbc73d29eae), [b/150289741](https://issuetracker.google.com/issues/150289741))
- Popups, Dialogs and Menus are now inheriting the contextual MaterialTheme ([Ia3665](https://android-review.googlesource.com/#/q/Ia3665905218b4d12d7a9bd121a69a51569d82694), [b/156527485](https://issuetracker.google.com/issues/156527485))
- Removed layout direction parameter from the measure block of the Layout() function. Layout direction is however available inside the callback through the measure scope object ([Ic7d9d](https://android-review.googlesource.com/#/q/Ic7d9d797938e6e2a91916836e5e9688794115c22))
- Add AbsoluteArrangement - allows for arrangement of the children inside the Row without automatic mirroring in RTL ([I3a1df](https://android-review.googlesource.com/#/q/I3a1df99368838ce603137c77974763704c33ca57))
- @Untracked annotation has been deprecated. Replace with @ComposableContract(tracked=false) ([Id211e](https://android-review.googlesource.com/#/q/Id211e1c7c168c5171bbf3c844792890ee87d4fc2))
- Prior to this change, the compose compiler plugin would non-trivially intercept calls to constructors inside of a @Composable function if there was an ([I5205a](https://android-review.googlesource.com/#/q/I5205af707238a70d600c105843cd99e88a5381e0), [b/158123804](https://issuetracker.google.com/issues/158123804))
- Add `viewModel()` composable which allows to create or get already created ViewModel similarly to how it works in Activity or Fragment ([I5fdd1](https://android-review.googlesource.com/#/q/I5fdd19bccbb57252e928b0f65097678022f860ef))
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
- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters.
  Deleted Px class in its entirety ([I3ff33](https://android-review.googlesource.com/#/q/I3ff339371abd6fb622172d060a70d12dda4822e0))

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

- TextField's cursor has a blinking animation ([Id10a7](https://android-review.googlesource.com/#/q/Id10a71f42f66fae532cca35ec132bcc35a4bc660))

- Partial gestures no longer require passing around of a
  GestureToken ([Id7ae5](https://android-review.googlesource.com/#/q/Id7ae5d8c63606f85fe7264f6d23240a75cd6a017))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I57bff](https://android-review.googlesource.com/#/q/I57bff9fbed3da9c71e8f5b24bbe75296d7275769))

- Modifier.semantics has been undeprecated to allow usages for high level components. ([I4cfdc](https://android-review.googlesource.com/#/q/I4cfdc837d5ac2d240af5a5ac6b755aebf800af15))

- Rename AnnotatedString.Builder.addAnnotationString to addStringAnnotation. ([I5059e](https://android-review.googlesource.com/#/q/I5059e6b6526a8fb64ab6ace7ad7e4637c718a19f))

- Updated Alignment API and added support for absolute alignment (which does not auto-mirror in Rtl context) ([I38cd3](https://android-review.googlesource.com/#/q/I38cd32c487c9dd72486476943c28afbed96aaf4e))

- Layout and LayoutModifier children can be measured with a different layout direction. ([Ibd731](https://android-review.googlesource.com/#/q/Ibd7319b7caa93b2bc7fb38df3678e2bb8298652e))

- Introduce additional optional rect
  parameter to ImagePainter to support
  drawing a subsection of underlying ImageAsset ([I0ea9e](https://android-review.googlesource.com/#/q/I0ea9ec2f991b30b0e68fa702ebdf44cbb0848901))

- Fixed a crash in AdapterList when removing items ([Ic64b0](https://android-review.googlesource.com/#/q/Ic64b0221db177462d76c355363c2843734f43007), [b/153195921](https://issuetracker.google.com/issues/153195921))

- We changed how we measure the first layout you put inside activity.setContent { } block. Previously it was forced to fill the whole activity screen, and now it behaves as if you put your layout inside a Stack: it can be smaller than a screen and will be positioned in the top left screen. If you want the old behaviour you can apply Modifier.fillMaxSize() for your layout. ([Ie88a7](https://android-review.googlesource.com/#/q/Ie88a713401b8d1db32acf421f2612121bd1d23f6), [b/153453714](https://issuetracker.google.com/issues/153453714))

- ui-text-compose module is renamed as ui-text. ui-text
  now contains CoreText and CoreTextField composables ([Ib7d47](https://android-review.googlesource.com/#/q/Ib7d4743369dbffbac262251b25d3c4351387fb36))

- ui-text module is renamed as ui-text-core ([I57dec](https://android-review.googlesource.com/#/q/I57dec72ca50e7288e37c9272ef6ce8bcc485a83e))

- Moved ui-framework/CoreText, CoreTextField composables under
  ui-text-compose. You might want to include ui-text-compose in your
  project. ([I32042](https://android-review.googlesource.com/#/q/I32042a9c701b1ea3ec4f92c02811c248af6ddb84))

- `runOnIdleCompose` and `runOnUiThread` are now global functions
  instead of methods on ComposeTestRule. ([Icbe8f](https://android-review.googlesource.com/#/q/Icbe8fd71d52144e855ccb4ce06a4677337be731a))

- \[Mutable\]State property delegate operators moved to extensions
  to support Kotlin 1.4 property delegate optimizations. Callers must add
  imports to continue using `by state { ... }` or `by mutableStateOf(...)`. ([I5312c](https://android-review.googlesource.com/#/q/I5312cf7bdfa072cadc1be2de5d5f45ec53200f41))

- DrawLayerModifier and drawLayer() now default clipToBounds
  and clipToOutline to false. ([I0eb8b](https://android-review.googlesource.com/#/q/I0eb8b08323e0031cae87194d407351e6bdf5e189), [b/152810850](https://issuetracker.google.com/issues/152810850))

- Renamed LayoutResult to MeasureResult. ([Id8c68](https://android-review.googlesource.com/#/q/Id8c686b5f08d58e8e48d015ed42570e306687882))

- Deprecated Center composable. It should be replaced either with the LayoutSize.Fill + LayoutAlign.Center modifier, or with one of the Box or Stack composables with suitable modifiers applied ([Idf5e0](https://android-review.googlesource.com/#/q/Idf5e0d25a2a8764489d738f6fcf242eeb667e124))

- Renamed LayoutFlexible to LayoutWeight. Renamed tight parameter to fill. ([If4738](https://android-review.googlesource.com/#/q/If4738c70c381e149ded400d657b5efd888ae5891))

- DrawVector has been changed from a regular
  composable function to returning a Modifier drawVector() that
  will draw the vector as a background to a layout. ([I7b8e0](https://android-review.googlesource.com/#/q/I7b8e04d9eae7619211748b92658b31bc09e9b2a0))

- Replace composable function Clip with modifier
  drawClip(). DrawClipToBounds is a convenient modifier
  to use when you only need to clip to the layer bounds
  with a rectangle shape. ([If28eb](https://android-review.googlesource.com/#/q/If28eb34fe98927dcb8d87f8961657cb8317371ae))

- Replaced DrawShadow composable function with drawShadow()
  modifier. Shadows are now drawn as part of LayerModifier. ([I0317a](https://android-review.googlesource.com/#/q/I0317ac63ddafcf16bd2e24662d489aacb4bb6a7e))

- androidx.compose.ViewComposer has been moved to androidx.ui.node.UiComposer
  androidx.compose.Emittable has been removed. It was redundant with ComponentNode.
  androidx.compose.ViewAdapters has been removed. They are no longer a supported use case.
  Compose.composeInto has been deprecated. Use `setContent` or `setViewContent` instead.
  Compose.disposeComposition has been deprecated. Use the `dispose` method on the `Composition` returned by `setContent` instead.
  androidx.compose.Compose.subcomposeInto has moved to androidx.ui.core.subcomposeInto
  ComponentNode#emitInsertAt has been renamed to ComponentNode#insertAt
  ComponentNode#emitRemoveAt has been renamed to ComponentNode#removeAt
  ComponentNode#emitMode has been renamed to ComponentNode#move ([Idef00](https://android-review.googlesource.com/#/q/Idef00fba3a2e67d7034e31d580d69192e9018b5f))

- Deprecated Wrap composable. It can be replaced either with the LayoutAlign modifier or with the Stack composable ([Ib237f](https://android-review.googlesource.com/#/q/Ib237f0f8f8cedd87c35683e5cc1b69abfd13d111))

- Made the layout direction be propagated from parent layout node to children. Added layout direction modifier. ([I3d955](https://android-review.googlesource.com/#/q/I3d9559ddec464850d22466793975b41757e0224e))

- Rename Painter.toModifier to Painter.asModifier as the newly created Modifier has a reference to the original Painter that can be shared across multiple Modifier instances ([I7195b](https://android-review.googlesource.com/#/q/I7195b03410cc351a2f62d89e7c01653221594571))

-
  | **Deprecated:** Draw composable is a common source of bugs as it's ([I78392](https://android-review.googlesource.com/#/q/I78392f01c2d37c2419812478d96417a1b8a1293d), [b/149827027](https://issuetracker.google.com/issues/149827027))
- Support right-to-left direction in LayoutPadding modifier ([I9e8da](https://android-review.googlesource.com/#/q/I9e8da0bfbb135ff7f34b0dc49b905f634ad7d18c))

- Density and DensityScope were merged into one interface. Instead of ambientDensity() you can now use DensityAmbient.current. Instead of withDensity(density) just with(density) ([I11cb1](https://android-review.googlesource.com/#/q/I11cb1f069a95f32f4ecab631f49d38dc1c071a42))

- Removed ValueHolder class. Restructured AnimatedValue, AnimatedFloat classes to
  make the animation value field abstract so that subclasses can watch the value update.

  - Added model classes for AnimatedValue, AnimatedFloat, etc.
  - Added a new set of light-weight @Composable API for animating between values.
  - ([I79530](https://android-review.googlesource.com/#/q/I79530e117cfa893a52542f85a55528eaa0f11b93))
- Breaking changes to the ambients API. See log and `Ambient<T>` documentation for details ([I4c7ee](https://android-review.googlesource.com/#/q/I4c7eea45f2b7bf41f8a8ba75fd667c06010469a9), [b/143769776](https://issuetracker.google.com/issues/143769776))

- Alignment line Int positions returned from Placeable#get(AlignmentLine) are now non-null. If the queried alignment line is missing, AlignmentLine.Unspecified will be returned. ([I896c5](https://android-review.googlesource.com/#/q/I896c5ef8a18919aa84413669341e716bf676e32e), [b/158134875](https://issuetracker.google.com/issues/158134875))

- Fixed a ConstraintLayout bug causing a crash on recompositions. ([Ibee5a](https://android-review.googlesource.com/#/q/Ibee5afd640816add9bd0c1545eee2ef747e9c2d2), [b/158164341](https://issuetracker.google.com/issues/158164341))

- WithConstraints trailing lambda API has been changed. Now instead of two params it has a receiver scope which in addition to constraints and layoutDirection provides minWidth, maxWidth, minHeight and maxHeight properties in Dp ([I91b9a](https://android-review.googlesource.com/#/q/I91b9af740cd2613ddd4fe6d63cd539a46b52fc52), [b/149979702](https://issuetracker.google.com/issues/149979702))

- Renamed LayoutModifier2 to LayoutModifier. ([Id29f3](https://android-review.googlesource.com/#/q/Id29f36d6b19674d189abb198a7656562b3b310b5))

- Intrinsic measurements functions in Layout and LayoutModifier2 have an IntrinsicMeasureScope receiver now which provides intrinsics query API with implicitly propagated layout direction. ([Id9945](https://android-review.googlesource.com/#/q/Id9945cb41842df9f99132679b5b68a0f0edda53d))

- LayoutDirectionAmbient is deprecated. To read the layout direction defined by the locale, use localeLayoutDirection on ConfigurationAmbient ([I851b1](https://android-review.googlesource.com/#/q/I851b137413c620a10bef4ef0a83d5c47d7a9fa6c))

- Added positionInParent and boundsInParent for LayoutCoordinates. ([Icacdd](https://android-review.googlesource.com/#/q/Icacdd0909bc434cd5fd935c46e0a07b965c6a38d), [b/152735784](https://issuetracker.google.com/issues/152735784))

- ParentData composable is deprecated. You should either create a modifier which implements ParentDataModifier interface, or use LayoutTag modifier if you simply need to tag layout children to recognize them inside the measure block. ([I51368](https://android-review.googlesource.com/#/q/I51368a2cb132318f5466949297e5fa247c04d68a), [b/150953183](https://issuetracker.google.com/issues/150953183))

- Add OnPositionedModifier and OnChildPositionedModifier
  to replace OnPositioned and OnChildPositioned composable
  functions. ([I2ec8f](https://android-review.googlesource.com/#/q/I2ec8fb4687b0b85e18174178562149745c03c7fd))

- Disallow negative padding in LayoutPadding. LayoutOffset should be used instead for negative position offsets. ([Ifb5b1](https://android-review.googlesource.com/#/q/Ifb5b19b62ad11d5f2c0efd993acc19de39a65635))

- WithConstraints got LayoutDirection parameter ([I6d6f7](https://android-review.googlesource.com/#/q/I6d6f7d5fd9a4a0428e3ee188a9a3790e1cdaf083))

- Updated the `ComposeFlags.COMPOSER_PARAM` flag to be `true`, which will change the code generation strategy for the compose plugin. At a high level, this causes @Composable functions to be generated with an additional synthetic parameter, which is passed through to subsequent @Composable calls in order for the runtime to properly manage execution. This is a significant binary breaking change, however, should preserve source-level compatibility in all sanctioned usage of compose. ([I7971c](https://android-review.googlesource.com/#/q/I7971ca1b6525440c38643953645fa388131e31f0))

- Changed LayoutCoordinates to make providedAlignmentLines
  a Set instead of a Map and have LayoutCoordinates implement the
  get() operator instead for retrieving a value. This makes it easier
  for modifiers to modify one or more value of the set without
  creating a new collection for each modifier. ([I0245a](https://android-review.googlesource.com/#/q/I0245a750ed12e822d61fa7d87c52bd708996f55d))

- LayoutCoordinates no longer has a position property. The
  position property does not make sense when considering LayoutModifiers,
  rotation, or scaling. Instead, developers should use parentCoordinates
  and childToLocal() to calculate the transform from one
  LayoutCoordinate to another.

  LayoutCoordinates uses IntPxSize for the size property instead of
  PxSize. Layouts use integer pixel sizes for layouts, so all layout sizes
  should use integers and not floating point values. ([I9367b](https://android-review.googlesource.com/#/q/I9367be21c2c202c8b6ad889b50a29454773f41af))
- Improvements to the API surface of Constraints ([I0fd15](https://android-review.googlesource.com/#/q/I0fd1505ae9a68c067a82eff6ab02b43080fe153c))

- Added TextDirection.Content ([I48f36](https://android-review.googlesource.com/#/q/I48f3683066739b4d88b2e998f9b216a5cd874f8d))

- Ajdust the Toolbar Menu to show copy, cut, paste properly. ([Id3955](https://android-review.googlesource.com/#/q/Id3955ab3845cc6ad1807b95bc39e73facf0fd358))

- Add FloatingToolbar for TextField Selection. ([Ie8b07](https://android-review.googlesource.com/#/q/Ie8b07e4405940f9d4b4147c34406c80a557b4d45))

- TextDirectionAlgorithm is renamed as TextDirection ([I75ce8](https://android-review.googlesource.com/#/q/I75ce894540855ae60201b05141ad40c400bda00a))

- TextDirection is renamed as ResolvedTextDirection ([I3ff38](https://android-review.googlesource.com/#/q/I3ff38ad5993a0b844dced711e38c729d2b0c8697))

- Add HapticFeedback to TextField Selection. ([I58050](https://android-review.googlesource.com/#/q/I58050bcae9699346c2ee7727c7b0f9efaee0e9cd))

- Add Copy, Cut, and Paste methods to TextField Selection. ([Idb70b](https://android-review.googlesource.com/#/q/Idb70bb33b718d5ba725630e3b90abd156d8160af))

- TestTag and Semantics have been deleted.
  Use Modifier.testTag and Modifier.semantics instead ([I15ff0](https://android-review.googlesource.com/#/q/I15ff0bece5791ff8adae20c3c1bcaf48cea7f1b0), [b/158841414](https://issuetracker.google.com/issues/158841414))

- Changed the package name for Locale and LocaleList from
  androidx.ui.text to androidx.ui.intl ([I8132c](https://android-review.googlesource.com/#/q/I8132c50e8be9b7ac27e858573056abe9250426ca))

- API change: `AnnotatedString(builder: Builder)` is renamed to `annotatedString(builder: Builder)`. ([Ia6377](https://android-review.googlesource.com/#/q/Ia63777788348827d4362e0bd6a4ab6cd64680062))

- API change: `AnnotatedString.Item` is renamed to `AnnotatedString.Range`. ([I2d44d](https://android-review.googlesource.com/#/q/I2d44dd9e4f565d5f90eeba93dc61a052109da32e))

- Add Toolbar for text related operations. ([I49d53](https://android-review.googlesource.com/#/q/I49d533345151058eac9026d1456196331ed0bf45))

- New LifecycleOwnerAmbient is now available. Now an Activity you are using with Compose UI should extend androidx.activity.ComponentActivity (or AppCompatActivity). setContent on android.app.Activity is now deprecated ([Idb25a](https://android-review.googlesource.com/#/q/Idb25a736332b17aebbfb96e919b932c2cc284d56), [b/153141084](https://issuetracker.google.com/issues/153141084))

- ui-android-text package name (androidx.text) replaced with
  androidx.ui.text.platform in order to align with androidx policy. ([I42711](https://android-review.googlesource.com/#/q/I42711800349ba35a5d1e45747a441f150e0a15fd))