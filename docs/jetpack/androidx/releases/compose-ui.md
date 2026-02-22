---
title: https://developer.android.com/jetpack/androidx/releases/compose-ui
url: https://developer.android.com/jetpack/androidx/releases/compose-ui
source: md.txt
---

# Compose UI

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.ui](https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary)  
[androidx.compose.ui.geometry](https://developer.android.com/reference/kotlin/androidx/compose/ui/geometry/package-summary)  
[androidx.compose.ui.graphics](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/package-summary)  
[androidx.compose.ui.platform](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary)  
[androidx.compose.ui.test](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary)  
(*See the API reference docs for all compose packages*) Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.11.0-alpha05) |

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
    implementation "androidx.compose.ui:ui:1.10.3"
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
    implementation("androidx.compose.ui:ui:1.10.3")
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

### Version 1.11.0-alpha05

February 11, 2026

`androidx.compose.ui:ui-*:1.11.0-alpha05` is released. Version 1.11.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/ui).

**API Changes**

- `AndroidComposeUiFlags.isSharedWindowInfoEnabled` moves the `WindowInfo` information to `ComposeViewContext`. Disabling the flag leaves `WindowInfo` controlled by `AndroidComposeView` ([I3b364](https://android-review.googlesource.com/#/q/I3b364aecc1ff6966a5e3d7f3dc88281e40d26b18))
- Common structures within `ComposeView` will be moved to the shared `ComposeViewContext`. This is the first change that moves the `CoroutineContext` to `ComposeViewContext`. When `AndroidComposeUiFlags.isSharedComposeViewContextEnabled` is true, values are automatically shared. When false, they are not shared. ([I9364d](https://android-review.googlesource.com/#/q/I9364d1ce727c0ebbdad7aa29ae454bed0ae418c5), [b/461566955](https://issuetracker.google.com/issues/461566955))
- Adds support for trackpad gestures and conversion from trackpad input events to mouse. With this change, trackpad pointer events that control a cursor like on tablets or laptops will generally be reported as mouse pointers, which improves behavior around pointer slop, scrolling, and hovering. Pan and scale gestures will also be reported with additional information available in the pointer event changes, with a new PointerEventType.Pan and PointerEventType.Scale indicating that these values will be set ([Id071a](https://android-review.googlesource.com/#/q/Id071af573d5710d7d3aca73bd1c8037bdb0ea701), [b/315527861](https://issuetracker.google.com/issues/315527861), [b/459831570](https://issuetracker.google.com/issues/459831570))

**Bug Fixes**

- Send `CONTENT_CHANGE_TYPE_CHECKED` for Toggleable property change. ([I6ac64](https://android-review.googlesource.com/#/q/I6ac64bd51c781e596678ed33546de8a4dd1ddb31), [b/476894689](https://issuetracker.google.com/issues/476894689), [b/474538004](https://issuetracker.google.com/issues/474538004), [b/475754416](https://issuetracker.google.com/issues/475754416))

**External Contribution**

- `androidx.compose.ui.graphics.NativePaint` typealias is deprecated, use `android.graphics.Paint` directly instead ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))
- Replace `Paint.asFrameworkPaint()` to `Paint.nativePaint` extension to avoid exposing platform type into `commonMain` sourceset via `typealias` ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))
- Add support for `NumPad` movement keys ([I1ff12](https://android-review.googlesource.com/#/q/I1ff128370417cc7b837ae09a4f47521473cca698))

### Version 1.11.0-alpha04

January 28, 2026

`androidx.compose.ui:ui-*:1.11.0-alpha04` is released. Version 1.11.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/ui).

**API Changes**

- Exposed the `TestCoroutineScheduler` to enable usage of `runCurrent()` and ensure access to the shared scheduler instance. ([Iea662](https://android-review.googlesource.com/#/q/Iea662686f25332bd583a4512827bb5eab0fc5ad9), [b/254115946](https://issuetracker.google.com/issues/254115946))
- Add support for walking up nested scrolling in response to `android.R.id.accessibilityActionShowOnScreen` from Accessibility. ([Ib2723](https://android-review.googlesource.com/#/q/Ib2723ce329635e565459c6021425ad0222cc02f0), [b/431148846](https://issuetracker.google.com/issues/431148846))

**Bug Fixes**

- Fixed conversion of custom Android RGB color space. Custom grayscale transforms were incorrectly converted between custom Compose and Android RGB color spaces.([ebd45](https://android-review.googlesource.com/#/q/a2b7e44c1117c3851ac500d1f4a196445d5ebd45),[b/377021410](https://issuetracker.google.com/issues/377021410))

### Version 1.11.0-alpha03

January 14, 2026

`androidx.compose.ui:ui-*:1.11.0-alpha03` is released. Version 1.11.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/ui).

**API Changes**

- Removed the `ComposeUiTestFlags.isStandardTestDispatcherSupportEnabled` flag. The v2 `run*ComposeUiTest` and `create*ComposeRule` APIs now use `StandardTestDispatcher` by default. To continue using `UnconfinedTestDispatcher`, you can use the deprecated API variants; however, we strongly recommend migrating to the v2 APIs for better control over coroutine execution. ([Iecc9c](https://android-review.googlesource.com/#/q/Iecc9cea0a3669832923e3a3603f06b6aae5cb83a), [b/455601592](https://issuetracker.google.com/issues/455601592))
- Introduced `androidx.compose.ui.test.junit4.v2.create*ComposeRule` APIs. These new APIs use a `StandardTestDispatcher` by default to better simulate production behavior where coroutines are queued rather than executed immediately. See the [migration guidance](https://developer.android.com/develop/ui/compose/testing/migrate-v2) for more information. ([I1870e](https://android-review.googlesource.com/#/q/I1870e29d6b5e79ce2e64d7fc4c3634557bb85947), [b/254115946](https://issuetracker.google.com/issues/254115946))
- Introduced `androidx.compose.ui.test.v2.run*ComposeUiTest` APIs. These new APIs use a `StandardTestDispatcher` by default to better simulate production behavior where coroutines are queued rather than executed immediately. See the [migration guidance](https://developer.android.com/develop/ui/compose/testing/migrate-v2) for more information. ([I4f782](https://android-review.googlesource.com/#/q/I4f782e6905a33e11258e1dcabf3970f0f8a77cb3), [b/254115946](https://issuetracker.google.com/issues/254115946))
- Common structures within `ComposeView` can now be shared. When `ComposeUiFlags.isSharedComposeViewContextEnabled` is true, values are automatically shared. When false, they are not shared. ([I0d1b4](https://android-review.googlesource.com/#/q/I0d1b40edd5a2f6cde3734a8af6e5a8114cafb8ce), [b/463540495](https://issuetracker.google.com/issues/463540495), [b/460468959](https://issuetracker.google.com/issues/460468959), [b/461503366](https://issuetracker.google.com/issues/461503366), [b/463641813](https://issuetracker.google.com/issues/463641813))

**Bug Fixes**

- Fixes bug where removing all content from the `ComposeView` doesn't remove the drawn content. ([I8b382](https://android-review.googlesource.com/#/q/I8b3820ded1d89a3b4968384e6965ca47075cedff), [b/299503084](https://issuetracker.google.com/issues/299503084))
- Fix a crash with pausable composition when animated with `LookaheadScope`. ([I7e649](https://android-review.googlesource.com/#/q/I7e64960ec594e7fbe8a8345b9061d40bf5b440ab), [b/469669851](https://issuetracker.google.com/469669851))
- Resolved an issue where transmitting excessively long strings to the Autofill service triggered a crash. To prevent this, text is now automatically truncated to a valid length prior to being sent.
- Fixes bug where a hover exit can cause a click under very specific conditions ([a3d5a0f](https://android.googlesource.com/platform/frameworks/support/+/a3d5a0fae6074ffd08ef2a61f063272877f1bcb9))
- Fixes stylus hover event dispatching for tests and preps mouse tests for new stylus tests. ([9ca9bc9](https://android.googlesource.com/platform/frameworks/support/+/9ca9bc91f311069bbaf6f591d65ad8fb5943b8b6))
- Adds support for unplacing/placing UI elements with pointer input. ([d0742b0](https://android.googlesource.com/platform/frameworks/support/+/d0742b05497028e54cb3ccddc5a666e976c82825), [b/BUD_ID](https://developer.android.com/jetpack/androidx/releases/TODO_ISSUE_TRACKER_LINK))
- Fixed a bug in Jetpack Compose `Popup` where absolute coordinates of the anchor bounds were being passed to the `PopupPositionProvider`, leading to incorrect popup placements. Popup positioning calculations now use the correct relative coordinates.([1f7edf](https://android-review.googlesource.com/#/q/1f7edfefb8598d91e225fa89440b70408de018c4),[b/469940907](https://issuetracker.google.com/469940907))

### Version 1.11.0-alpha02

December 17, 2025

`androidx.compose.ui:ui-*:1.11.0-alpha02` is released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/ui).

**API Changes**

- The `MultiModalInjectionScope` APIs are now stable. This includes `performKeyInput` and `performRotaryScrollInput`, and their underlying key and rotary APIs. The experimental annotation has been removed. ([Ie8bbc](https://android-review.googlesource.com/#/q/Ie8bbc60afddb304113b0e9c35d1a39f010c242df), [b/261561237](https://issuetracker.google.com/issues/261561237))
- Adds trackpad testing APIs. These are similar to the mouse testing APIs, and inject events that mimic the behavior of a tablet or laptop trackpad. The primary entry points are `SemanticsNodeInteraction.performTrackpadInput` and `MultiModalInjectionScope.trackpad` ([I2ce67](https://android-review.googlesource.com/#/q/I2ce67fba9c0571ddf3ca97d5994e17062967e61b)), [b/432326139](https://issuetracker.google.com/432326139).

**Bug Fixes**

- Fixes mouse wheel scroll input interoperability to only consume if consumed in Compose, not if they were dispatched in Compose. ([I5e0c4](https://android-review.googlesource.com/#/q/I5e0c4c048f3cc3888e43d5c8288d1f120e6d9c5a)),

### Version 1.11.0-alpha01

December 03, 2025

`androidx.compose.ui:ui-*:1.11.0-alpha01` is released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b48588febd37d5947dfa0f2827d2b5ca6af2ed90..deb96499dfe95073f5c1215c1287787683cb1e92/compose/ui).

**API Changes**

- Removes `isSemanticAutofillEnabled` UI flag as semantic autofill has been enabled by default. ([I849cf](https://android-review.googlesource.com/#/q/I849cfb0385e8677a2798c8212b262e1e6d60aef5), [b/455587954](https://issuetracker.google.com/issues/455587954))
- Changed how traversable method find `findNearestAncestor` discovers relevant nodes. Now delegates of the same type (NodeKind) will be visible during the traversal. The change is guarded by the flag `isTraversableDelegatesFixEnabled`. ([Ia3165](https://android-review.googlesource.com/#/q/Ia316505eae1fad10e5b4455ad6a219bf0894f8d5), [b/280804097](https://issuetracker.google.com/issues/280804097))
- Add `TextEntryKey` mapping for `ANI#isTextEntryKey` ([Ifde7b](https://android-review.googlesource.com/#/q/Ifde7be87fb32dca55b9b7c4ccc72bc729d76c59a), [b/399540654](https://issuetracker.google.com/issues/399540654))
- `Modifier.onFirstVisible()` is deprecated as its behavior is misleading and doesn't always follow the contract claimed by the name. For example, when it is added on an item of `LazyColumn`, this callback will be called everytime this item became visible after scrolling. It is not what the users of the modifier with this name might have expected. It is recommended to use `Modifier.onVisibilityChanged()` instead and manually track if the layout was visible already previously based on the requirement of the specific use case. ([Ia7095](https://android-review.googlesource.com/#/q/Ia709566717edbdfe5717bedfa74d1334a78f8964), [b/447601783](https://issuetracker.google.com/issues/447601783))
- Introduced `MeasuredSizeAwareModifierNode`, which is needed when you need `onRemeasured()` callback. Please use this interface directly instead of using more generic `LayoutAwareModifierNode` when you don't need other callbacks. ([If6fb0](https://android-review.googlesource.com/#/q/If6fb04b74840d08274d01a41d84bd14507d190b8))

## Version 1.10

### Version 1.10.3

February 11, 2026

`androidx.compose.ui:ui-*:1.10.3` is released. Version 1.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b..0d23f956849b578e041ea4245127d4007eae43be/compose/ui).

### Version 1.10.2

January 28, 2026

`androidx.compose.ui:ui-*:1.10.2` is released. Version 1.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c09ac6669b664a348ecf964a97968cd81479dcd4..fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b/compose/ui).

### Version 1.10.1

January 14, 2026

`androidx.compose.ui:ui-*:1.10.1` is released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2120e7975523001d1eac390a5d9c5e2e9597267f..c09ac6669b664a348ecf964a97968cd81479dcd4/compose/ui).

**Bug Fixes**

- Fix a crash with pausable composition when animated with `LookaheadScope` ([I7e649](https://android-review.googlesource.com/#/q/I7e64960ec594e7fbe8a8345b9061d40bf5b440ab), [b/469669851](https://issuetracker.google.com/469669851))
- Fixed a bug in Jetpack Compose `Popup` where absolute coordinates of the anchor bounds were being passed to the `PopupPositionProvider`, leading to incorrect popup placements. Popup positioning calculations now use the correct relative coordinates.([1f7edf](https://android-review.googlesource.com/#/q/1f7edfefb8598d91e225fa89440b70408de018c4),[b/469940907](https://issuetracker.google.com/469940907))

### Version 1.10.0

December 03, 2025

`androidx.compose.ui:ui-*:1.10.0` is released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26..a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9/compose/ui).

### Version 1.10.0-rc01

November 19, 2025

`androidx.compose.ui:ui-*:1.10.0-rc01` is released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1c84233fc2372352b838d165d256581ff37ada9..b48588febd37d5947dfa0f2827d2b5ca6af2ed90/compose/ui).

**Bug Fixes**

- Correctly send `visibilityChanged` callbacks with false when `minDurationMs` is not zero. ([2ac08b8](https://android-review.googlesource.com/#/q/2ac08b84ed4deab3b28c513e46bd3177b5579267), [b/456384555](https://issuetracker.google.com/issues/456384555))
- Do not call `onVisibilityChanged` callback when the node is initially not visible. ([3969e8d](https://android-review.googlesource.com/#/q/3969e8d29808265bcd5cc1730541f15e9b0cb3cf), [b/447364998](https://issuetracker.google.com/issues/447364998))

### Version 1.10.0-beta02

November 05, 2025

`androidx.compose.ui:ui-*:1.10.0-beta02` is released. Version 1.10.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/784e4a2de372f09d49c65fbc1ca64681a25a5f06..d1c84233fc2372352b838d165d256581ff37ada9/compose/ui).

### Version 1.10.0-beta01

October 22, 2025

`androidx.compose.ui:ui-*:1.10.0-beta01` is released. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..784e4a2de372f09d49c65fbc1ca64681a25a5f06/compose/ui).

**API Changes**

- Adds an optimization for focus change dispatching. This can be disabled with `isOptimizedFocusEventDispatchEnabled = false` ([I919fb](https://android-review.googlesource.com/#/q/I919fb47196d36a3d7425e082098b0ce0b3d3b0e6), [b/449228515](https://issuetracker.google.com/issues/449228515))
- Updates all indirect touch APIs to use the name indirect pointer APIs to match pointer input APIs. ([I238ce](https://android-review.googlesource.com/#/q/I238ced063c4f54959abf1c07a1b93bbf1c6efa78), [b/451607214](https://issuetracker.google.com/issues/451607214))
- `TextDirection`, `TextAlign`, `Hyphens`, `FontSynthesis` `valueOf` functions now throw `IllegalArgumentException` when they receive an unknown value. ([I07c67](https://android-review.googlesource.com/#/q/I07c671cbd0a9fe4fe0b10d615d0aab98ee04cd52))
- Update `CompositionDataTree.makeTree` to pass default values instead of wrapper function. ([Id64a6](https://android-review.googlesource.com/#/q/Id64a699b00fb73464cfa7b4f7e18e793f12f677c), [b/445229688](https://issuetracker.google.com/issues/445229688))
- The test rule APIs `createComposeRule`, `createAndroidComposeRule` and `createEmptyComposeRule` which accept the `effectContext` parameter are stable and the parameter defaults to `EmptyCoroutineContext`. ([If400c](https://android-review.googlesource.com/#/q/If400c15315dc5f1ed6e5bc3717dd4bbbb2e2f015), [b/450540702](https://issuetracker.google.com/issues/450540702))
- `UnplacedStateAwareModifierNode` was renamed to `UnplacedAwareModifierNode` ([I6a551](https://android-review.googlesource.com/#/q/I6a551ec37d6ad1d6d6647e6a215a9f49ff5c0ed1), [b/449719932](https://issuetracker.google.com/issues/449719932))
- Undo the Content Capture Optimization ([Ic000b](https://android-review.googlesource.com/#/q/Ic000b4d15811c5cdae44341f9bae72d91f03925e), [b/442364065](https://issuetracker.google.com/issues/442364065))
- Added `ComposeUiFlags.isRectManagerOffsetUsageFromLayoutCoordinatesEnabled` feature flag. It enabled performance optimization where coordinates requests like `LayoutCoordinates.positionInRoot()` are using the cached offsets we already have in `RectManager`, instead of traversing the whole tree on each call. ([Ieaadc](https://android-review.googlesource.com/#/q/Ieaadca92a3d320dbc81663b7a357c8867e5cc814))

**Bug Fixes**

- `PlaceholderSpan` now correctly uses non-linear font scaling for sizing ([Id2ead](https://android-review.googlesource.com/#/q/Id2ead31ea5f608657561eff3748b75abf21b73af), [b/324462728](https://issuetracker.google.com/issues/324462728))
- Use `ViewCompat` to perform haptic feedback constants supported at the platform level, relying on its fallback support for newer constants. ([Ib5a00](https://android-review.googlesource.com/#/q/Ib5a00de6fb838ff6501d5c6a0213aa9badf59cdf))

### Version 1.10.0-alpha05

October 08, 2025

`androidx.compose.ui:ui-*:1.10.0-alpha05` is released. Version 1.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef9c81cf7222a390e0a467d8c8b48d04362fd3d..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/ui).

**Bug Fixes**

- Fixed a bug where nested Popups were incorrectly positioned at the screen's top; they now correctly anchor to their parent Popup. ([Id4603](https://android-review.googlesource.com/q/Id46039870362618073d66e6cc88d50430e953aff), [b/191279752](https://issuetracker.google.com/issues/191279752))
- Fixed problem with focus wrapping with other Views in the hierarchy. ([I95223](https://android-review.googlesource.com/#/q/I952231962c99e9ba17246394fd212ebc4a363bac), [b/446028624](https://issuetracker.google.com/issues/446028624))
- Fixes fields with inline parameters missing from inspector in lambdas generated by Kotlin 2.2.20 ([I9855d](https://android-review.googlesource.com/#/q/I9855d6dfaccd8127eb658fb2871965a09502c2e9), [b/447110005](https://issuetracker.google.com/issues/447110005))
- Fixes name shadowing of autofill resources between UI and foundation modules ([I5da5a](https://android-review.googlesource.com/q/I5da5abcbbddd93ad87069d82f5f66f78755b901a))

**External Contribution**

- `UiModes` object is renamed to AndroidUiModes to reflect that its constants are lifted from Android API. ([Ia0a77](https://android-review.googlesource.com/#/q/Ia0a77c5e36cf9e7f62b42c2d01d69e750d00286d))

### Version 1.10.0-alpha04

September 24, 2025

`androidx.compose.ui:ui-*:1.10.0-alpha04` is released. Version 1.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..6ef9c81cf7222a390e0a467d8c8b48d04362fd3d/compose/ui).

**API Changes**

- The Compose test rule variant that accepts a `CoroutineContext` parameter has been promoted to stable. The experimental annotation has been removed, and developers no longer need to opt-in to use this API. ([I74e6e](https://android-review.googlesource.com/#/q/I74e6e9fe59d583cad1f1015a0032059a4b97db65))
- `ComposeUiFlags.isRectTrackingEnabled` was removed. This logic is not always enabled. ([Id78df](https://android-review.googlesource.com/#/q/Id78dfb5fb5b2dd2f786492cb455321240df5d704))
- Deprecated inline overload of `Updater#set` as they were boxing provided value too many times ([Id679e](https://android-review.googlesource.com/#/q/Id679eefb099cbf45c00ba01338af5c1cfa2f8782))
- Mark `onAutofillText` semantic property as deprecated. ([I6f81c](https://android-review.googlesource.com/#/q/I6f81cdef315162eca07fde512429620704fb6b4f))
- `UnplacedStateAwareModifierNode` was introduced. It provides a callback called when the previously placed layout is not placed anymore. ([I8fdd8](https://android-review.googlesource.com/#/q/I8fdd82ad7b8b750209b07ba4b54af4152910be8e), [b/309776096](https://issuetracker.google.com/issues/309776096))
- Corrected documentation of `RetainObserver.onRetained` and added `RetainObserver.onUnused`, which mirrors `RememberObserver.onAbandoned`. ([Ia6fc5](https://android-review.googlesource.com/#/q/Ia6fc517b08308e53e8742202c3cc5525d173e077))
- Added `onVisibilityChangedNode()`, which is producing a `Modifier.Node`, used by `Modifier.onVisibilityChanged()` via delegation, which allows to expand on top of this functionality in your custom `Modifier.Node`. ([I70d84](https://android-review.googlesource.com/#/q/I70d84b97ebdd52f1c7b547f4909e8c3b3a11543d), [b/443001320](https://issuetracker.google.com/issues/443001320))

**Bug Fixes**

- Fixed an issue where inline content failed to render when positioned on the final line of multi-line ellipsized text, despite the placeholder preceding the ellipsized region. ([I76aaf](https://android-review.googlesource.com/#/q/I76aaf69b402e3efd8e7c759fc4ba0e082882a85e), [b/441829208](https://issuetracker.google.com/issues/441829208))

### Version 1.10.0-alpha03

September 10, 2025

`androidx.compose.ui:ui-*:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/compose/ui).

**API Changes**

- Renames `DelegatableNode.invalidateLayoutForSubtree` to `DelegatableNode.invalidateMeasurementForSubtree`. ([I94257](https://android-review.googlesource.com/#/q/I94257d9dea1e140bf2c33aa685445b9766016564), [b/430106107](https://issuetracker.google.com/issues/430106107))
- Removes redundant `isInHiddenAccessibilitySubtree` matcher. ([I4476c](https://android-review.googlesource.com/#/q/I4476c0328a3f9584b49baa9c313052edb632962a), [b/443792965](https://issuetracker.google.com/issues/443792965))
- Introduces group key based Compose stack traces that are enabled by default for all minified apps. The proguard mapping for these traces will be generated by Compose compiler Gradle plugin starting from Kotlin 2.3.0. ([Ifbcb5](https://android-review.googlesource.com/#/q/Ifbcb5302344d20eca05d9762662bcad893d80a56))
- `Modifier.skipToLookaheadSize` now uses a default enabled lambda that only enables the size skipping when shared transition is active, same as `Modifier.skipToLookaheadPosition`. ([Ibe0f5](https://android-review.googlesource.com/#/q/Ibe0f56ebe107b33a6adae7e1e4eb676b366afb5d), [b/432485585](https://issuetracker.google.com/issues/432485585))
- `ComposeUiFlags.isOutOfFrameDeactivationEnabled` is removed and this functionality is now always enabled. ([I421ed](https://android-review.googlesource.com/#/q/I421ed7766cc90874bf844029afaacf88c5dfa29c))
- Move factory functions for creating `FillableData` instances to companion object. Instead of calling `FillableData(value)`, use the new factory methods: `FillableData.createFrom(value)`. ([I2e200](https://android-review.googlesource.com/#/q/I2e2000938dacc674805868e2030813575892b26d), [b/441719650](https://issuetracker.google.com/issues/441719650))
- Introduce `BeyondBoundsLayoutModifierNode` a new Modifier node to perform beyond bound layout for focus search. ([I39be1](https://android-review.googlesource.com/#/q/I39be1741cebd0b7df56c8e034cc3189b2135e664), [b/416133658](https://issuetracker.google.com/issues/416133658))
- `FocusTargetModifierNode.requestFocus()` sends focus to one of its children when it is not itself focusable. This is now consistent with `FocusRequester.requestFocus()` and `FocusRequesterModifierNode.requestFocus()`. If you do not need this behavior, set the `ComposeUiFlags.isRequestFocusOnNonFocusableFocusTargetEnabled` flag to false in your app. ([Icca5c](https://android-review.googlesource.com/#/q/Icca5ccb8c6c4e4960cbc42af724532d62cf5b84a), [b/436863604](https://issuetracker.google.com/issues/436863604))
- Provide DP-based window size in `WindowInfo` ([I9322b](https://android-review.googlesource.com/#/q/I9322b7d4b71476faec15f8f72713ba4797ebdc83), [b/424442112](https://issuetracker.google.com/issues/424442112))
- Removed flag `isNestedScrollDispatcherNodeFixEnabled`. ([If451a](https://android-review.googlesource.com/#/q/If451a900c18b6801ed15ba942db7905d5be129e0))
- Add support for date values in autofill in the `FillableData` API. `val dateMillisValue: Long` added to retrieve date information, and a corresponding `FillableData(dateMillisValue: Long)` constructor added to create date-based `FillableData` instances. ([Id072a](https://android-review.googlesource.com/#/q/Id072a9a276493e831d24fc016d8bb1b8d7fd5b5d))

**External Contribution**

- `UiModes` object is introduced to declare constants that are used for `UiMode` annotation ([I03cb8](https://android-review.googlesource.com/#/q/I03cb80842c893d7f62d9390e9cdb13eb2a376828))

### Version 1.10.0-alpha02

August 27, 2025

`androidx.compose.ui:ui-*:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/ui).

**API Changes**

- Update `FillableData` to support non-text components such as toggles and lists, including boolean and integer values inside `FillableData` and factory constructors to create boolean and list instances of `FillableData` that translate to the platform's `AutofillValue`. The relevant semantic property and action also are added. ([Ia8105](https://android-review.googlesource.com/#/q/Ia810576b70c559f828102e0280612aed79fb1c65), [Icc5cf](https://android-review.googlesource.com/#/q/Icc5cf69cdec326bf9f12fdcb541d79e362793dfc))
- In non-touch mode, the view system assigns initial/default focus to one of the focusable items on the screen. This feature is added to Compose and can be enabled by enabling `ComposeUiFlags.isInitialFocusOnFocusableAvailable`. ([Ib9178](https://android-review.googlesource.com/#/q/Ib9178bdb9380090a7fadbee553d8a6d6603938e9))
- Removed flag `isPointerInteropFilterDispatchingFixEnabled`. ([Iaa589](https://android-review.googlesource.com/#/q/Iaa58900d980303b9f51fc96f5fd5d9422780cda3))
- Removed flag `isNestedScrollInteropPostFlingFixEnabled`. ([I2a756](https://android-review.googlesource.com/#/q/I2a756541e431ebf6e9e3452547dc2b09f4baa0d0))
- Add in `isHiddenFromAccessibility()` and `isInHiddenAccessibilitySubtree()` semantics matchers. ([I9f5a1](https://android-review.googlesource.com/#/q/I9f5a1e1b68eead720c37a1eaed91777e00cd5a0c))
- Added `runCurrent()` to `MainTestClock` to run all due tasks on the underlying scheduler. This is to support running tests on a `StandardTestDispatcher`, where tasks are added to the scheduler rather than executed immediately when they have a delay of 0ms. A test can be setup to use a `StandardTestDispatcher` by [creating](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/package-summary#createComposeRule(kotlin.coroutines.CoroutineContext)) a `ComposeTestRule` and passing a `StandardTestDispatcher` to it. By default, tests are run on an `UnconfinedTestDispatcher`, in which case `runCurrent()` will never have to be called.
- Added support for running tests on a `StandardTestDispatcher`. Historically, the test framework was (and still is) set up using an `UnconfinedTestDispatcher`, which differs from a production environment in subtle ways. You can now change this setup by creating your own `StandardTestDispatcher` and adding it to the `effectContext` when [creating](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/package-summary#createComposeRule(kotlin.coroutines.CoroutineContext)) your `ComposeTestRule` (or when calling [runComposeUiTest](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#runComposeUiTest(kotlin.coroutines.CoroutineContext,kotlin.Function1)) ). ([I334d0](https://android-review.googlesource.com/#/q/I334d0d149d263eb65c327f3dbba4fad154e8a559), [b/254115946](https://issuetracker.google.com/issues/254115946))
- Update code for creating a tree of nodes from `SlotTree`. ([I997d3](https://android-review.googlesource.com/#/q/I997d32b63f7c4170dc02671537b18d5b3867a382))

**Bug Fixes**

- Compose UI now installs lifecycle-aware `RetainScopes` on Android. The default behavior will now persist `retain`-ed values across configuration changes. ([Id4a09](https://android-review.googlesource.com/#/q/Id4a09d6fafacf8cfcee149c4bce74ec335449ca8), [b/177562901](https://issuetracker.google.com/issues/177562901))

**External Contribution**

- Adds the ability for `VelocityTracker` to calculate the velocity of a pointer based on tracked pointer events using platform-specific behavior. ([I621e8](https://android-review.googlesource.com/#/q/I621e880bd3e77128aa546ec87e92fbff8c22f548))

### Version 1.10.0-alpha01

August 13, 2025

`androidx.compose.ui:ui-*:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c30d03ab9e19dcf35e8b79438f0d91ee74cae557..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/ui).

**API Changes**

- Pointer downs with a mouse or touchpad in a `ComposeView` will now clear focus automatically if the pointer down doesn't occur in the bounds of the focused node. This results in a "tap-to-clear focus" UX that is more expected than current behavior when using pointer input devices. This behavior can be opt-ed out of with a new `AbstractComposeView.isClearFocusOnPointerDownEnabled` API. ([I6322b](https://android-review.googlesource.com/#/q/I6322b0a63e80042f6a558104d0684443e5dc161f), [b/282963174](https://issuetracker.google.com/issues/282963174))
- Introduce `FillableData` interface to support various autofill component types, in addition to Text. ([If9bd2](https://android-review.googlesource.com/#/q/If9bd2e0df45654b5c33bc7d46a6535169197aeb1))
- New API to allow dynamically enable and disable shared elements that also allows accounting for whether there is already an ongoing shared element transition. New API to set up an alternative target bounds when the target shared element is disposed during the transition. New API to obtain the `LayoutCoordinates` of a `LookaheadScope`. ([I18dd4](https://android-review.googlesource.com/#/q/I18dd441208500dbd29276f834421db3134047390), [b/409819304](https://issuetracker.google.com/issues/409819304), [b/395670637](https://issuetracker.google.com/issues/395670637))
- Introduce flag `isNestedScrollInteropIntegerPropagationEnabled` to control the experiment of dispatching correct integers to nested scroll interop. ([If8316](https://android-review.googlesource.com/#/q/If83167b8ea1aff41f6dd6ff823a2d43c6bb86f65))
- Added `requestFocusForChildInRootBounds()` to `DelegatableNode` to move focus to a child that overlaps with the given rect. ([I001ef](https://android-review.googlesource.com/#/q/I001efed653d1b06a11257ae7f79f51e8e6d31ad2))
- Removed flags `isOnScrollChangedCallbackEnabled`, `isAdjustPointerInputChangeOffsetForVelocityTrackerEnabled`, `isFlingContinuationAtBoundsEnabled`, `isAutomaticNestedPrefetchEnabled`, `DragGesturePickUpEnabled`, `isPointerInteropFilterDispatchingFixEnabled`, `isNestedScrollInteropPostFlingFixEnabled`, `isNestedScrollDispatcherNodeFixEnabled` ([I36c18](https://android-review.googlesource.com/#/q/I36c18840c708660e9cbad345024299bfd80cde3c))
- Added `@CheckResult` annotation on the `SemanticsNode` finder and selector functions to enforce usage of returned values. ([I6f86e](https://android-review.googlesource.com/#/q/I6f86e14a50de6cc72d71b5872fad78bda7706072), [b/201652748](https://issuetracker.google.com/issues/201652748))
- Improve the performance of the content capture process ([I3c7c0](https://android-review.googlesource.com/#/q/I3c7c05f87eb2306ab39be829e838d5b10df2a7c3))
- Introduce `CompositionLocal` that can be used to modify the brush of Autofill's successful filling highlight. ([I52329](https://android-review.googlesource.com/#/q/I52329ea7905c1a0a2db56caa36f4b9d53f3dd0d9))
- Introduced new Interpolatable interface which allows for automatic interpolation between different types, assuming one type knows how to convert from the other. This interface is leveraged in several compose types like Brush and Shape, but can be utilized externally as well. ([I58eab](https://android-review.googlesource.com/#/q/I58eab524eadd08c41f1809a2815a6311ad179aee))
- Now Scrollable supports 2 dimensional mouse wheel scroll events better. A new test API landed to help test use cases in `MouseInjectionScope`. We also introduced a new overload for scroll methods in `MouseInjectionScope` and a flag to control the new behavior called `isMouseWheel1DAxisLockingEnabled` ([I136df](https://android-review.googlesource.com/#/q/I136dfe2d0887c1900fb1896599ec4b4aa1b31ac7))
- Add `DeviceConfigurationOverrides` for keyboard type \& state, navigation type and state, touchscreen state, and UI mode type ([I282f0](https://android-review.googlesource.com/#/q/I282f0e65200637c02636d6e385d8ca4fde97b974))
- Added a new `LineHeightStyle.Mode` called `Tight`. This mode helps enforce smaller line heights even when they may possibly cut taller glyphs. ([Id3849](https://android-review.googlesource.com/#/q/Id38495accc4fe059f6e2318eaafb648f36fe0f99))
- `BaselineShift` now has an Unspecified value to prevent boxing `BaselineShift`, `Hyphens`, `LineBreak`, `TextAlign`, and `TextDirection` now have `isSpecified` helper functions `Hyphens`, `TextAlign`, `TextDecoration`, and `TextDirection` now have `valueOf()` and value methods enabling efficient serialization/deserialization. ([I8d44c](https://android-review.googlesource.com/#/q/I8d44cb45591118b5f8b0074f347cbd1d23a94501))
- Added a new `getDisplayName` method interface to allow custom display names for preview parameter instances. ([I19bdf](https://android-review.googlesource.com/#/q/I19bdfbff9392179ebb9d033bcfb11d124c0f366e), [b/241699422](https://issuetracker.google.com/issues/241699422))
- When Dp values are compared with Unspecified using less-than or greater-than, it now always returns false. Using `Dp.compareTo(Unspecified)` always returns 0. Setting the flag `ComposeUiUnitFlags.isDpCompareToChanged` to false will return `Dp.compareTo()` to is former behavior, where comparing Unspecified with less-than and greater-than don't always return false, and `compareTo()` with Unspecified matches the behavior of `Float.compareTo()`. ([Ifa88b](https://android-review.googlesource.com/#/q/Ifa88bbc81f180694728ab8f4418a698c836330ba), [b/429221319](https://issuetracker.google.com/issues/429221319))

**Bug Fixes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Fixes an issue that prevented the creation of new `AndroidComposeViews` while a transition is ongoing. ([I2e23e](https://android-review.googlesource.com/#/q/I2e23e3f220761547b505655534d8fda37f9154b4), [b/340894487](https://issuetracker.google.com/issues/340894487), [b/287484338](https://issuetracker.google.com/issues/287484338))
- Fixes a color bug when using a vector drawable that uses one color and the `fillColor` is neither fully opaque nor fully transparent. ([I3b041](https://android-review.googlesource.com/#/q/I3b04195622a5c24dab6e7f4f201dc7c27092a3d5), [b/328677973](https://issuetracker.google.com/issues/328677973))
- Fixes an issue where icons loaded via `painterResource` with theme-specific colors didn't update on theme changes. ([I85ea0](https://android-review.googlesource.com/#/q/I85ea086649ec3fd9d9170dbdd3ae64630cc44651), [b/424416571](https://issuetracker.google.com/issues/424416571))
- Introduce `onFillData` and `fillableData` semantics ([I45d9e](https://android-review.googlesource.com/#/q/I45d9e14d93785392eaba5df39e1077d85e19a522))
- Platform-specific state encoding is now always enabled in `StateRestorationTester`. This aligns test behavior with real application state restoration, such as Parcelization on Android. ([I38211](https://android-review.googlesource.com/#/q/I38211a72d5d553fad43564c97aa2798296981f04), [b/408154192](https://issuetracker.google.com/issues/408154192), [b/382294247](https://issuetracker.google.com/issues/382294247))
- Fixes occasional crashes when requesting focus. ([57b31a11](https://android-review.googlesource.com/#/q/57b31a11cc34d3bc7624d89e30475326625cc66e), [b/431111149](https://issuetracker.google.com/issues/408154192))

## Version 1.9

### Version 1.9.5

November 19, 2025

`androidx.compose.ui:ui-*:1.9.5` is released. Version 1.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41..1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26/compose/ui).

### Version 1.9.4

October 22, 2025

`androidx.compose.ui:ui-*:1.9.4` is released. Version 1.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea7909f13c54ea29d87d55d27ecf449000f82a8a..b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41/compose/ui).

**Bug Fixes**

- Fixed an issue where inline text content was disappearing if it was on the last line of a multi-line ellipsized text even though the inline content wasn't in the ellipsized region. ([I76aaf](https://android-review.googlesource.com/#/q/I76aaf69b402e3efd8e7c759fc4ba0e082882a85e), [b/441829208](https://issuetracker.google.com/issues/441829208))
- Fixed an issue where `onLayoutRectChanged` modifier callbacks were not always being called when `debounceMillis` is not zero. ([72aba47](https://android-review.googlesource.com/#/q/I1c204b382c94d08f02df664398355c7b542ed643), [b/445324854](https://issuetracker.google.com/issues/441829208))

### Version 1.9.3

October 08, 2025

`androidx.compose.ui:ui-*:1.9.3` is released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6177e34a7667c42030e47ee8ecba82f09e2a5de..ea7909f13c54ea29d87d55d27ecf449000f82a8a/compose/ui).

**Bug Fixes**

- Fixed a bug where `onVisibilityChanged/onFirstVisible/onLayoutRectChanged` modifiers were not receiving callbacks if the layout being moved has over 170 descendants. ([4f2fdd](https://android-review.googlesource.com/q/Ie34e70a9bee738334f11085075d795e04d4f2fdd), [b/445356774](https://issuetracker.google.com/issues/445356774))

### Version 1.9.2

September 24, 2025

`androidx.compose.ui:ui-*:1.9.2` is released. Version 1.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/93a1ed2aac05dbfa192392b9d4ab27c40da53d69..b6177e34a7667c42030e47ee8ecba82f09e2a5de/compose/ui).

**Bug Fixes**

- `Modifier.onVisibilityChanged()` now correctly fires when a node is detached or reused. ([Ic5ce20](https://android-review.googlesource.com/#/q/Ic5ce20fc8f870019d15c4491214e585210742100))
- `Modifier.onVisibilityChanged()` and `onLayoutRectChanged()` now properly handles parent layouts using `placeWithLayer()` to place children. ([Ia05ac9](https://android-review.googlesource.com/#/q/Ia05ac9e65e6e5608f1433eb275e9706097db1b11))
- For `Modifier.onVisibilityChanged()` and `onLayoutRectChanged()`, properly notify in corner cases like removing a layer/layer modifier or updating layer properties. ([Ia05ac](https://android-review.googlesource.com/#/q/Ia05ac9e65e6e5608f1433eb275e9706097db1b11))

### Version 1.9.1

September 10, 2025

`androidx.compose.ui:ui-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44da9aeaf3fa617c6f81f887691b37fe901109aa..93a1ed2aac05dbfa192392b9d4ab27c40da53d69/compose/ui).

**Bug Fixes**

- Fixes a color bug when using a vector drawable that uses one color and the `fillColor` is neither fully opaque nor fully transparent. ([I3b041](https://android-review.googlesource.com/#/q/I3b04195622a5c24dab6e7f4f201dc7c27092a3d5), [b/328677973](https://issuetracker.google.com/issues/328677973))

### Version 1.9.0

August 13, 2025

`androidx.compose.ui:ui-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..44da9aeaf3fa617c6f81f887691b37fe901109aa/compose/ui).

**Important changes since 1.8.0**

- Important changes in version 1.9.0 are covered in this [blogpost](https://android-developers.googleblog.com/2025/08/whats-new-in-jetpack-compose-august-25-release.html)
- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.
- Breaking change: the `graphicsLayer` modifier nodes now implements `SemanticsModifierNode`. This can result in new `SemanticsNodes` added to the semantics tree and, therefore, lead to test failures in tests that make assumptions about the semantics tree structure. For example, tests that use `onChild`, `onParent`, `onSibling`, and other similar methods to make assertions can fail if a new node is added between the current and target nodes. The preferred way to fix these failures is to add a `testTag` to the target node directly. Another approach is to use a looser matcher, such as `onNode(hasAnyAncestor(hasText("ancestor")) and hasText("target"))`. ([I638b5](https://android-review.googlesource.com/#/q/I638b56cb3aa3f4f68a354dfa5a42201febee61bc))

### Version 1.9.0-rc01

July 30, 2025

`androidx.compose.ui:ui-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..c30d03ab9e19dcf35e8b79438f0d91ee74cae557/compose/ui).

**Bug Fixes**

- Fixes an issue where icons loaded via `painterResource` with theme-specific colors didn't update on system theme changes. ([I85ea0](https://android-review.googlesource.com/#/q/I85ea086649ec3fd9d9170dbdd3ae64630cc44651), [b/424416571](https://issuetracker.google.com/issues/424416571))
- Fixes errors on APIs 21(Lollipop) and 28(Pie) where important graphics methods were renamed while being optimized. ([Iebf99](https://android-review.googlesource.com/#/q/Iebf994ff416c5464c6b760e87b4bce0d0d7894ec), [b/425120571](https://issuetracker.google.com/issues/425120571), [b/420462749](https://issuetracker.google.com/issues/420462749))
- Ensure that newly inserted `onLayoutRectChanged` modifiers get called back initially. ([l9aa91](https://android-review.googlesource.com/#/q/I9aa91eab487bc633e06a2124c5dddc86e3d80833)), ([lb348a](https://android-review.googlesource.com/#/q/Ib348aa8bce0b36a7c128ac178b1dad6035df9602))
- Fix for an offset cache being incorrectly invalidated, causing `onLayoutRectChanged` modifiers to be called with wrong coordinates ([ibd4cd](https://android-review.googlesource.com/#/q/Ibd4cd9fb7c1f288e56b449af9239fb93824ff243)), ([lddc57](https://android-review.googlesource.com/#/q/Iddc57baedff8b114a8fc444eb92201e2d5ed56ee))
- Fix for rotated/skewed layouts receiving incorrect coordinates by `onLayoutRectChanged` modifiers ([lddc57](https://android-review.googlesource.com/#/q/Ic64e9841c227af8e32e06164b4c12d2a2a575bd9), [b/426750475](https://issuetracker.google.com/issues/426750475))

**External Contribution**

- Fixed an issue where `dragAndDropSource` items in `LazyList` disappear when scrolled. Thanks Victor Rendina! ([dc3bcd3](https://android-review.googlesource.com/#/q/dc3bcd33dbcbeb32ce9c2815a4ed3c1ade234b29), [b/425894792](https://issuetracker.google.com/issues/425894792))

### Version 1.9.0-beta03

July 16, 2025

`androidx.compose.ui:ui-*:1.9.0-beta03` is released. Version 1.9.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d578548e34459870db64b61d8788d83f2cf49f54..5735a11c1798c2f8b419dfdc02347578a6ebf870/compose/ui).

**Bug Fixes**

- Fixes an issue where uniformly blurred inner shadows were not moving correctly with an offset.

### Version 1.9.0-beta02

July 2, 2025

`androidx.compose.ui:ui-*:1.9.0-beta02` is released. Version 1.9.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..d578548e34459870db64b61d8788d83f2cf49f54/compose/ui).

**API Changes**

- Changes companion object to experimental to match class. ([I8452a](https://android-review.googlesource.com/#/q/I8452aa286a2aeb8f134bc5b6d776fef71b73e9d0))
- Removed `isTrackFocusEnabled` experimental flag ([I003fd](https://android-review.googlesource.com/#/q/I003fd13c5c0c5a6062ab86d6d23a050bd4ab907e))

**Bug Fixes**

- When no `WindowInsets` enchroach on the content of the `ComposeView`, `WindowInsetsRulers` values are not provided. ([I71221](https://android-review.googlesource.com/#/q/I7122141fa51344acc2351299962ccde82468113e))

### Version 1.9.0-beta01

June 18, 2025

`androidx.compose.ui:ui-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e1d81d156ec778ff4b8bc291aa661d780576ea4c/compose/ui).

**Breaking Changes**

- The `graphicsLayer` modifier nodes now implements `SemanticsModifierNode`. This can result in new `SemanticsNodes` added to the semantics tree and, therefore, lead to test failures in tests that make assumptions about the semantics tree structure. For example, tests that use `onChild`, `onParent`, `onSibling`, and other similar methods to make assertions can fail if a new node is added between the current and target nodes. The preferred way to fix these failures is to add a `testTag` to the target node directly. Another approach is to use a looser matcher, such as `onNode(hasAnyAncestor(hasText("ancestor")) and hasText("target"))`. ([I638b5](https://android-review.googlesource.com/#/q/I638b56cb3aa3f4f68a354dfa5a42201febee61bc))

**API Changes**

- Changed `ShadowContext` to be a sealed interface ([I3ce40](https://android-review.googlesource.com/#/q/I3ce40f0d8f261362250238462ae7a409e91b1ea4))
- Adds a cross module way to create an Indirect Touch Event (for testing) ([I22e4c](https://android-review.googlesource.com/#/q/I22e4caba5d68a869f5c63a715f517cae659e9e79))
- Makes`IndirectTouchEvent.nativeEvent` experimental. ([I6fda5](https://android-review.googlesource.com/#/q/I6fda5888d1edf6d30dc5c7f47b3a3e89b5faab17))
- Revises API surface based on API council feedback. ([Ibf378](https://android-review.googlesource.com/#/q/Ibf378bc0b6c6d1c83572c58ce921b58cec219b57))
- Remove `FrameRateCategory.NoPreference` constant. Rename `Modifier.requestedFrameRate` to `Modifier.preferredFrameRate`. ([I2f976](https://android-review.googlesource.com/#/q/I2f9763092dbcff5fe06bda1fb514d4a5df1b9d21))
- `WindowInsetsRulers`: changed `rulersIgnoringVisibility` to maximum. Changed `getDisplayCutoutBounds()` to be an extension function of `PlacementScope`. `WindowInsetsAnimationProperties` has been changed to `WindowInsetsAnimation` and the `getAnimationProperties()` has been changed to `getAnimation()`. ([I3816f](https://android-review.googlesource.com/#/q/I3816f062168c83c7bb9e320cfa59a6a4ce1637e8))
- Changed class `ShadowParams` to `Shadow` ([I11cca](https://android-review.googlesource.com/#/q/I11cca9bd6406196d010ab92d398426812919d6a3))
- Change the package for frame rate API from `androidx.compose.ui.ui` to `androidx.compose.ui` ([I8994e](https://android-review.googlesource.com/#/q/I8994e38b954940a3e5a7669b2828011e37d0e112))
- Changed `InsetsRulers` to be in common code with the name `WindowInsetsRulers`. Simplified the API so all insets are `WindowInsetsRulers`. Extracted non-rulers animation properties to an `AnimationProperties` class. `WindowInsetsRulers.innermostOf()` can be used to merge multiple `WindowInsetsRulers`. ([I2f0c6](https://android-review.googlesource.com/#/q/I2f0c6aebeca80fc181e843da78743bf2a5289501), [b/415012444](https://issuetracker.google.com/issues/415012444))
- Added a tooling API for parsing source information added by Compose compiler. ([Iceaf9](https://android-review.googlesource.com/#/q/Iceaf954bf1d09a8ada7b908ceb2909c7f4652819), [b/408492167](https://issuetracker.google.com/issues/408492167))

**Bug Fixes**

- Flag for `isGetFocusedRectReturnEmptyEnabled` has been removed now that the feature has been fully verified. ([Ife722](https://android-review.googlesource.com/#/q/Ife72212763d29d3f9792447a4c76a6edf66c21a6))
- Fixes a bug in `performScrollToNode`, which in some cases was not reaching the target node. With this fix, it should always reach the target node in those cases. A side effect of this change is that the exact scroll position at the end of the action may now be different, which affects screenshot tests and tests that make assumptions about the exact scroll position. ([I2c8a1](https://android-review.googlesource.com/#/q/I2c8a1ac37b4f14814f65697d397091749129caca))

### Version 1.9.0-alpha04

June 4, 2025

`androidx.compose.ui:ui-*:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fd8d5a2f883c1cdd7f712b200d5a4fedf342136..786176dc2284c87a0e620477608e0aca9adeff15/compose/ui).

**API Changes**

- Added modifier APIs for customizable shadows. ([I2058d](https://android-review.googlesource.com/#/q/I2058d6641d5d0747f1455034a4300776035985b2), [b/160665122](https://issuetracker.google.com/issues/160665122))
- Add a `SemanticsModifierNode.isImportantForBounds` property that determines whether the node should be taken into account when computing bounds. The property is true by default and can be set to false to indicate that the node should not be taken into account for bounds. ([I7ebec](https://android-review.googlesource.com/#/q/I7ebec06c2af89f7890743b4ff4c2388fc0ebbde7))
- Add a `SemanticsPropertyKey` factory function for declaring Android-specific semantics properties that are made available as accessibility extras exposed via `AccessibilityNodeInfo.getExtras`. ([I2ed51](https://android-review.googlesource.com/#/q/I2ed511dc37b144196a911e7e55b56ea35205a5a2))
- Removed usages of `ComposeUiFlags.isRemoveFocusedViewFixEnabled` and deprecated the flag. ([I50328](https://android-review.googlesource.com/#/q/I5032840c5419ce8802619df0cfc5226d9fdd62ea))
- Introduce new customizable shadow framework. This includes `DropShadowPainter` and `InnerShadowPainter` as well as the `DropShadow/InnerShadow` dependencies. Shadow infrastructure is shared such that the same generated shadows can be shared at multiple callsites without having to re-generate the shadows n-times. ([I24f7a](https://android-review.googlesource.com/#/q/I24f7a227d0bcb3886682ff05d6f77ca6d2a133bd), [b/160665122](https://issuetracker.google.com/issues/160665122))
- Introduce `CompositeShader` and `CompositeShaderBrush` which creates a composited result between two shaders. Also add `ShaderBrush#transform` to set a transformation matrix for the shader. ([I2621a](https://android-review.googlesource.com/#/q/I2621aeede742c15964faefa927631208a98ff1a2), [b/160665122](https://issuetracker.google.com/issues/160665122))

**Bug Fixes**

- Fixed a bug in `NestedScrollInteropConnection` where fling methods were being in the wrong order with respect to views. ([I56ad4](https://android-review.googlesource.com/#/q/I56ad4f04e5b29aceb7d7ceeb40976ad17aaf9ce0))
- Previously, dialogs that drew full screen were not drawing within the display cutout region. This bug is fixed so that dialogs with `decorFitsSystemWindows = false` and `usePlatformDefaultWidth = false` can take the display cutout region. ([I9e975](https://android-review.googlesource.com/#/q/I9e9758a01b07a7943030f33c20720fe24186e0d6))
- Fixed a bug where `TalkBack`'s green focus indicator was not drawn after being turned on while the Compose app is in the background. ([Ifd12a](https://android-review.googlesource.com/#/q/Ifd12a124dc56036a06136583a75fb142a76de3d3))

### Version 1.9.0-alpha03

May 20, 2025

`androidx.compose.ui:ui-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..5fd8d5a2f883c1cdd7f712b200d5a4fedf342136/compose/ui).

**API Changes**

- Flag `ComposeUiFlags.isGetFocusedRectReturnEmptyEnabled` makes it so that when nothing is focusable in a `ComposeView`, it sets the rect to an Empty value. This prevents a focus search from choosing the View to focus on. This is especially important for when an IME has a NEXT option where it might try to focus on the `ComposeView` and `requestFocus()` fails. ([Ibd0e2](https://android-review.googlesource.com/#/q/Ibd0e260624d662b36c846bd0b2fa6e7b0f5ad08e), [b/369256395](https://issuetracker.google.com/issues/369256395))
- Introduce flag `isNestedScrollDispatcherNodeFixEnabled`. ([I0d24a](https://android-review.googlesource.com/#/q/I0d24ad6c222a319c9a9fb0356309a3b99fa15418))
- Rename `DialogProperties`' `dialogContentTitle` to `windowTitle` ([Ibd27b](https://android-review.googlesource.com/#/q/Ibd27b029ffa636af03a26a1bd73e90aa96ae3574))
- `Modifier.onFirstVisible` and `Modifier.onVisibilityChanged` modifiers were introduced, which are high level modifiers built on top of `Modifier.onLayoutRectChanged`. These modifiers are built specifically to handle a lot of common application requirements such as logging impressions, auto playing videos, etc. These have been built with performance in mind so that they can be used in critical list-based scenarios without risk of sacrificing scroll performance. In addition to these modifier APIs, additional APIs to `RelativeLayoutBounds` have been added in order to support these use cases, as well as make it easier for developers to easily create similar custom modifiers that suit their use case exactly. ([I759b8](https://android-review.googlesource.com/#/q/I759b8256fd7797ad9a10a955368231b70470dd7c))
- Change `setDiagnosticStackTraceEnabled` to experimental to account for future development of this feature. ([I11db3](https://android-review.googlesource.com/#/q/I11db30dfc2e0922aa4da13bc9769ab33f3e94f65))
- Introduce `Modifier.scrollable2D`, `Scrollable2DState` and companion APIs for state creation. Also introduced common scroll extension functions. ([Ic61c8](https://android-review.googlesource.com/#/q/Ic61c8f14451090f441b009bf8f86e7566c27c782), [b/214410040](https://issuetracker.google.com/issues/214410040))
- Compose 64-bit color values are not directly comparable to Android `ColorLongs` because the color space IDs are out of order for some color spaces. To convert to and from Android color spaces, two new APIs are added: `toColorLong()` and `fromColorLong()`. ([I36899](https://android-review.googlesource.com/#/q/I368990c572cebb2895f87291e9b966ba96b73961))
- Introduced `ViewConfiguration.minimumFlingVelocity` to allow lower bound fling velocity control. ([I11aab](https://android-review.googlesource.com/#/q/I11aab07292b0c3545149da8b4ac88bdc24154ae1))

### Version 1.9.0-alpha02

May 7, 2025

`androidx.compose.ui:ui-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/ui).

**API Changes**

- Add in `dialogContentTitle` to `DialogProperties`, which sets the content window title. [bf9d670](https://android.googlesource.com/platform/frameworks/support/+/bf9d670d9f91ac850afc985f3ecce250d517884f)

**Bug Fixes**

- Window Insets Rulers have been disabled temporarily while internal tests are fixed. [8d1402](https://android.googlesource.com/platform/frameworks/support/+/ba709fb65635975c04fdc78ca9ecb09a0f8d1402)
- Fixed how pointer input changes are added to the `VelocityTracker` in `DragGestureNode`, this can be controlled with the new flag `isAdjustPointerInputChangeOffsetForVelocityTrackerEnabled`.[254ddb](https://android.googlesource.com/platform/frameworks/support/+/0d93eda9a0bb69ac0c19ce59e18db1eaf5254ddb)

### Version 1.9.0-alpha01

April 23, 2025

`androidx.compose.ui:ui-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/ui).

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

**API Changes**

- Removes Flag to enable trace statements for hit path tracker (debug). ([I1b2a1](https://android-review.googlesource.com/#/q/I1b2a1d14486d63395e6d8514a36aeea202fe23ce))
- Changed `InnerRectRulers` and `OuterRectRules` to be methods instead. Removed name parameter from `RectRulers` public API. `DerivedRulers` is now a constructor option for Vertical and Horizontal Rulers. `MergedHorizontalRulers` and `MergedVerticalRulers` have been replaced with `minOf` and `maxOf` methods to generate instances. ([Iee89f](https://android-review.googlesource.com/#/q/Iee89f432021f21e79ef111a039c9fa4b8b78edc7), [b/408192133](https://issuetracker.google.com/issues/408192133))
- Deprecate `androidx.compose.ui.LocalSavedStateRegistryOwner` in favor of `androidx.savedstate.compose.LocalSavedStateRegistryOwner`. ([I5439f](https://android-review.googlesource.com/#/q/I5439fa13b66fc524c423d63e3be635025af1e756), [b/377946781](https://issuetracker.google.com/issues/377946781))
- Add a `Modifier.keepScreenOn` to set the display to not sleep while present ([Ib5af4](https://android-review.googlesource.com/#/q/Ib5af42c0d16e7d6b2d7a17c5e213f377778c98c8), [b/408284174](https://issuetracker.google.com/issues/408284174))
- Add a new semantics property `Shape`, which may be set when the shape of the UI element is different from its bounding rectangle, e.g., rounded corner rectangle. ([I1376f](https://android-review.googlesource.com/#/q/I1376f00a3f739052d119bbbd8a5aab18ecb2131c))
- Fix issue with pointer event dispatching in `AndroidViews` and added flag `isPointerInteropFilterDispatchingFixEnabled` to protect changes. ([I0e272](https://android-review.googlesource.com/#/q/I0e272fc05c7931c0e888a357d0a85e354dd32578), [b/372055500](https://issuetracker.google.com/issues/372055500), [b/408002332](https://issuetracker.google.com/issues/408002332))
- `FocusRestorer` no longer pins the previously focused item. Users should use a key to ensure that the previously focused item has the same composition hash, so that focus is successfully restored. ([I4203b](https://android-review.googlesource.com/#/q/I4203b9aede7ed93d78a58fd330a807384142dc48), [b/330696779](https://issuetracker.google.com/issues/330696779))
- Allow Compose to trigger `ViewTreeObserver.OnScrollChanged`. This behavior is introduced under the flag `isOnScrollChangedCallbackEnabled`. We also introduced an extension function of `DelegatableNode dispatchOnScrollChanged`. ([I34b9d](https://android-review.googlesource.com/#/q/I34b9d923ff1fb4a4e27a53e583a7b082bc99b158), [b/238109286](https://issuetracker.google.com/issues/238109286))
- `currentCompositeKeyHash` is now deprecated. Use `currentCompositeKeyHashCode` instead. The replacement API encodes the same hash with more bits, which exponentially reduces the chance of two random unrelated groups in the composition hierarchy from having the same hash key. ([I4cb6a](https://android-review.googlesource.com/#/q/I4cb6a801d12447ac52bc92bb899ae84d69c4a6ed), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Added lint check support for `FocusRequester` to make sure it is remembered inside composition ([I6bf91](https://android-review.googlesource.com/#/q/I6bf911348f006b4f04fe2c5633aba0a060ec4fd1))
- Added the ability to set preferred frame rate or frame rate category on the Composable should be rendered at ([Ie5201](https://android-review.googlesource.com/#/q/Ie52017587fbf70a60364c3ffe5f0a8fe575c9fd2))
- Expose native `MotionEvent` on Android. ([I17286](https://android-review.googlesource.com/#/q/I172860862ead5734c24091e1f377fd182a64ed82))
- Add `getChecked() + setChecked(int)`, deprecate `isChecked + setChecked(boolean)` ([Iaac9d](https://android-review.googlesource.com/#/q/Iaac9dd3ee7b30896e282935a9599006450565f3e))
- The `graphicsLayer` modifier now accepts a `blendMode` and a `colorFilter` ([Iab0e6](https://android-review.googlesource.com/#/q/Iab0e65f3f26fd4cc81c69cbb9ecf4484e933b5d4))
- Added `LocalResources` composition local to query Resources. Calling `LocalResources.current` will recompose when the configuration changes, so calls to APIs such as `stringResource()` will return updated values. ([I50c13](https://android-review.googlesource.com/#/q/I50c13ee26bc440f3fe64c40271850e76e734a596), [b/274786917](https://issuetracker.google.com/issues/274786917))
- Expose experimental API for Composables to handle indirect touch events ([Icff57](https://android-review.googlesource.com/#/q/Icff57d89af4f857abd2d37f41af8229f2e582b97))
- This release improves the reporting of unhandled exceptions thrown during the layout and draw phases of your composable content. Previously, an uncaught exception here would crash the test runner and prematurely end the test suite. These exceptions can now be reported more gracefully without ending the test suite. ([I9928b](https://android-review.googlesource.com/#/q/I9928b954c197d7295faeea252cf87733d092ed17), [b/314128080](https://issuetracker.google.com/issues/314128080))
- Deprecated the experimental `GlobalAssertions` API. Its intended use was to run accessibility checks, see [`enableAccessibilityChecks()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest?hl=en#enableAccessibilityChecks()) for that purpose instead. ([I50aa5](https://android-review.googlesource.com/#/q/I50aa509889849f8772724f46d5849920cf4fd660))
- `SemanticsNodeInteraction.performTextInputSelection` is no longer experimental and now supports an additional `relativeToOriginal` parameter which allows you to apply the selection to either the original untransformed text or the transformed text. ([I3a905](https://android-review.googlesource.com/#/q/I3a905087b0cd779910d09ff619d0a7e2c9e2a8ba), [b/261561038](https://issuetracker.google.com/issues/261561038), [b/277018945](https://issuetracker.google.com/issues/277018945))
- Introduce API for creating custom bullet lists through `AnnotatedString` ([I1d066](https://android-review.googlesource.com/#/q/I1d066d3df73999bd3c771b72982fe8bbccc822ae), [b/383269496](https://issuetracker.google.com/issues/383269496), [b/139326648](https://issuetracker.google.com/issues/139326648))
- Deprecate `runWithTimingDisabled` in favor of `runWithMeasurementDisabled`, which more clearly describes the behavior - all metrics are paused. Additionally, expose the `MicrobenchmarkScope` superclass since redeclaring the `runWithMeasurementDisabled` function to open access isn't possible, since it's inline. ([I9e23b](https://android-review.googlesource.com/#/q/I9e23b0dfcff18f162ca0d2517734f3038870b59c), [b/389149423](https://issuetracker.google.com/issues/389149423), [b/149979716](https://issuetracker.google.com/issues/149979716))
- Updated ui-tooling Devices API to include newer devices. ([Ia2ac1](https://android-review.googlesource.com/#/q/Ia2ac13b06f15228d65067c01f51f64fc2b8082ec))
- Add Tablet Portrait in the collection of Preview Screen sizes to help the developer to consider bigger windows ([Ia1976](https://android-review.googlesource.com/#/q/Ia1976dfd73960d190004e59269e042ab5fbc457c))
- Introduce trace value API for marking/logging trace with values at a given point in time. Trace values show in Prefetto as a new lane that can be seen through the timeline of a trace. On Android they're implemented using `Trace.setCounter`. ([Idcf48](https://android-review.googlesource.com/#/q/Idcf48360d3bc608f6397a5ba7368ba7246c3712e))

**Bug Fixes**

- Fix dispatching of remember observers in pausable composition to avoid dispatching remembered/forgotten in the same apply ([I570b2](https://android-review.googlesource.com/#/q/I570b2436b95c7f8fb88a6f9824dbb9b8bccbc0fa), [b/404645679](https://issuetracker.google.com/issues/404645679), [b/407931790](https://issuetracker.google.com/issues/407931790))
- `android:dialogTheme` can now be set to control dialog properties when `decorFitsSystemWindows` is false ([I7922f](https://android-review.googlesource.com/#/q/I7922fcfff59df0d611d1c61bad3c309c75e8e635), [b/246909281](https://issuetracker.google.com/issues/246909281))
- Fixed bug where any motion event caught outside of a dialog could dismiss the dialog. ([Ia78fd](https://android-review.googlesource.com/#/q/Ia78fd1dc0284df3aefd5ef1dfa6b25d7942791e4))
- Compose lint checks now require a minimum AGP version of 8.8.2 from command line, and at least Android Studio Ladybug for IDE support. If you are using an older version of AGP, you can set `android.experimental.lint.version=8.8.2` in gradle.properties to upgrade the Lint version, without affecting AGP. ([I6f2a8](https://android-review.googlesource.com/#/q/I6f2a8816d93bc7d9d2a24658d69baa0900abf4c6))
- Added a new semantics property `InputText` that captures a `textfield`'s value before output transformation is applied. ([Iae46a](https://android-review.googlesource.com/#/q/Iae46a52e7fbb1a3558e897c5afebd125089befbb), [b/395911609](https://issuetracker.google.com/issues/395911609), [b/176949051](https://issuetracker.google.com/issues/176949051))
- Moved `enableAccessibilityChecks()` API that turns on the Accessibility Checks for Android to separate packages which are `compose:ui:ui-test-accessibility` if you're not using the `TestRule` and `compose:ui:ui-test-junit4-accessibility` when calling on `TestRule` ([I3c318](https://android-review.googlesource.com/#/q/I3c3183c7f06ced8c0ad4873b6262ea39e1ea1b16), [b/391560768](https://issuetracker.google.com/issues/391560768))
- Added support for compose stack traces in `LaunchedEffect` and `rememberCoroutineScope` ([I705c0](https://android-review.googlesource.com/#/q/I705c0898bc527741d87cc9ff838016b87b14fb54), [b/354163858](https://issuetracker.google.com/issues/354163858))

**External Contribution**

- Changing the experimental `runComposeUiTest` function to accept a suspend block. Also added a deprecated fun `runComposeUiTest` for binary compatibility ([I3b88c](https://android-review.googlesource.com/#/q/I3b88cb2d89d06cba472ab9056cfae822c1a7dd4b), [b/361577328](https://issuetracker.google.com/issues/361577328))

## Version 1.8

### Version 1.8.3

June 18, 2025

`androidx.compose.ui:ui-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/754896be0859599f16ed264d79a04ee337bac777..13362f65a9c0649415fe57052ea0e3932d2303d1/compose/ui).

**Bug Fixes**

- Flag for `isGetFocusedRectReturnEmptyEnabled` has been removed now that the feature has been fully verified. ([Ife722](https://android-review.googlesource.com/#/q/Ife72212763d29d3f9792447a4c76a6edf66c21a6))
- Flag `ComposeUiFlags.isGetFocusedRectReturnEmptyEnabled` makes it so that when nothing is focusable in a `ComposeView`, it sets the rect to an Empty value. This prevents a focus search from choosing the View to focus on. This is especially important for when an IME has a NEXT option where it might try to focus on the `ComposeView`and `requestFocus()` fails. ([Ibd0e2](https://android-review.googlesource.com/#/q/Ibd0e260624d662b36c846bd0b2fa6e7b0f5ad08e), [b/369256395](https://issuetracker.google.com/issues/369256395))

### Version 1.8.2

May 20, 2025

`androidx.compose.ui:ui-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/018e42f9db74b5e4fce8007734de4da6ae087407..754896be0859599f16ed264d79a04ee337bac777/compose/ui).

**Bug Fixes**

- Fixes NPE when dialog is being removed during active event stream on dialog ([6a7e7f](https://android.googlesource.com/platform/frameworks/support/+/6a7e7f941c93b2aa40eaa17094f1093e16b11287))
- Fix `onLayoutRectChange` not updating per throttled timeline when draw-only updates occur. ([03b82d](https://android-review.googlesource.com/#/q/Ic3cb778685ee819da28da68fffe7ac9b5f749297))

### Version 1.8.1

May 7, 2025

`androidx.compose.ui:ui-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..018e42f9db74b5e4fce8007734de4da6ae087407/compose/ui).

**Bug Fixes**

- Fix some issues with `onLayoutRectChanged` and `LazyLayout` [d791b11](https://android.googlesource.com/platform/frameworks/support/+/d791b11f073a062b587ba4cb9516fb42c9598441/)
- Skip remeasure requests for precomposed items. This bug affected the lazy layouts scrolling performance as the prefetch was not working efficiently in some cases, the measurement was happening within the frame. [742087a](https://android.googlesource.com/platform/frameworks/support/+/742087ac7ad6724fc0fae9f7209843aeea1b7ad2)

### Version 1.8.0

April 23, 2025

`androidx.compose.ui:ui-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b6bba717628c4c8c633c9509bfc4e4d9b89f428..d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9/compose/ui).

**Important changes since 1.7.0**

- Compose 1.8 contains newly added support for semantic autofill. Ensure that the versions of UI and Foundation that you use are version 1.8 or higher, as autofill for text components needs the latest versions of both modules. For API usage and examples, please refer to the autofill documentation for more details, [here](https://developer.android.com/develop/ui/compose/text/autofill).
- Compose 1.8 supports additional types of haptic feedback: `Confirm`, `ContextClick`, `GestureEnd`, `GestureThresholdActivate`, `Reject`, `SegmentFrequentTick`, `SegmentTick`, `ToggleOn`, `ToggleOff`, `VirtualKey`. This is accessible via `LocalHapticFeedback` and on Android, this is available by default when the [Vibrator API](https://developer.android.com/develop/ui/views/haptics/haptics-apis#vibration_effect_composition) indicates that haptics are supported.
- Multiple Focus APIs are now stable, including `Modifier.focusRestorer()` and `onEnter` and `onExit` `FocusProperties` ([I6e667](https://android-review.googlesource.com/#/q/I6e667ad84b51a525531f4902c1a0ac6ab8b4fba8)). You can now specify a `FocusDirection` when you call `requestFocus`. We have added a `requestFocus(FocusDirection)` API to both `focusRequester` and `FocusTargetModifierNode` to allow focusing with a specific direction. (I5d9ec\]\[https://android-review.googlesource.com/#/q/I5d9eca3a2cd283c1b84ad6b77d929ef9a49ce4cc\], [b/245755256](https://issuetracker.google.com/issues/245755256))

### Version 1.8.0-rc03

April 9, 2025

`androidx.compose.ui:ui-*:1.8.0-rc03` is released. Version 1.8.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0907800009c0cb37dd12c5586d620350c1975de..1b6bba717628c4c8c633c9509bfc4e4d9b89f428/compose/ui).

**Bug Fixes**

- Disables some focus interop fixes that caused a regression. ([b9d998](https://android.googlesource.com/platform/frameworks/support/+/b9d998943e74bb06a448d52f7c4d3378a8e7ccbd), [b/369256395](http://issuetracker.google.com/issues/369256395), [b/378570682](http://issuetracker.google.com/issues/378570682), [b/376142752](http://issuetracker.google.com/issues/376142752), [b388590015/](http://issuetracker.google.com/issues/388590015), [b/389994198](http://issuetracker.google.com/issues/389994198), [b/391378895](http://issuetracker.google.com/issues/391378895))

### Version 1.8.0-rc02

March 26, 2025

`androidx.compose.ui:ui-*:1.8.0-rc02` is released. Version 1.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/071f2b22541efa1d5d528479b28aa42960923a4f..c0907800009c0cb37dd12c5586d620350c1975de/compose/ui).

**Bug Fixes**

- Fixed an issue where focused views embedded in the Compose hierarchy would cause re-entrant composition when the focused view was removed from a lazylist. ([765562](https://android.googlesource.com/platform/frameworks/support/+/765562eaabc9b71e3bd67985cf3701907185e812))

### Version 1.8.0-rc01

March 12, 2025

`androidx.compose.ui:ui-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d195d8376d369f4bf74652abe60101aa658bbcc..071f2b22541efa1d5d528479b28aa42960923a4f/compose/ui).

**Bug Fixes**

- Fixes crash when a focused `AndroidView` is removed with the soft keyboard active. ([Ic725a](https://android-review.googlesource.com/#/q/Ic725a3c4b4a9b8af5854dd43ea834648bb52dafb))
- Fixes a few issues in the new focus state handling implementation. ([b/395895685](https://issuetracker.google.com/issues/395895685))
- Fixes an issue blocking Autofill when using `LaunchedEffect` to request focus on a text field. ([b/392539099](https://issuetracker.google.com/issues/392539099))

### Version 1.8.0-beta03

February 26, 2025

`androidx.compose.ui:ui-*:1.8.0-beta03` is released. Version 1.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/08954f0d500d220e8d6af07b4e6c51090911f779..2d195d8376d369f4bf74652abe60101aa658bbcc/compose/ui).

**API Changes**

- Moved `enableAccessibilityChecks()` API that turns on the Accessibility Checks for Android to separate packages which are `compose:ui:ui-test-accessibility` if you're not using the TestRule and `compose:ui:ui-test-junit4-accessibility` when calling on `TestRule` ([I547ef](https://android-review.googlesource.com/#/q/I547ef720bfe3d295161e86fe7356995b994357ad), [b/391560768](https://issuetracker.google.com/issues/391560768))
- Added a new semantics property `InputText` that captures a textfield's value before output transformation is applied. ([Iae46a](https://android-review.googlesource.com/#/q/Iae46a52e7fbb1a3558e897c5afebd125089befbb))

**Bug Fixes**

- Fixed an issue which caused autofill services to save the output transformed text instead of the input text. ([Iae46a](https://android-review.googlesource.com/#/q/Iae46a52e7fbb1a3558e897c5afebd125089befbb), [b/395911609](https://issuetracker.google.com/issues/395911609), [b/176949051](https://issuetracker.google.com/issues/176949051))

### Version 1.8.0-beta02

February 12, 2025

`androidx.compose.ui:ui-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5d82c9c8e72f3dd8c4ee71ff5ac9a1365d24de4..08954f0d500d220e8d6af07b4e6c51090911f779/compose/ui).

**New Features**

- Added a lint check to warn against calls to `Configuration#screenWidth`/`heightDp` - `LocalWindowInfo.current.containerSize` can be used instead to retrieve the current window size.

### Version 1.8.0-beta01

January 29, 2025

`androidx.compose.ui:ui-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8..80c9eca8dc00a6ae7188bf5f2beaf129b79de243/compose/ui).

**API Changes**

- `ContextualFlowRow` and `ContextualFlowColumn` have been marked as deprecated. This experimental component was introduced in 1.7 and had not yet been stabilized, and the implementation has been deemed undesirable. In the future, a component solving the use cases this component was meant to solve may be provided.
  - `FlowRow` and `FlowColumn` have experimental overloads that were introduced in 1.7 that include an `overflow` parameter. The use of this parameter has been deprecated, and the overloads without this parameter can be used instead. The default "overflow" behavior for these overloads will be "Clip", as it was since its introduction.
  - Many use cases for `ContextualFlowRow` can be accomplished using FlowRow, but we acknowledge that is not true in full generality. `ContextualFlowRow` is completely implementable in user-space, and one can attempt to copy its implementation and adapt if desired. In the future, we hope to solve these use cases in a different way. ([Ibafec](https://android-review.googlesource.com/#/q/Ibafec7f7926d2060f7551910264d5dd51637cafc))
- `SemanticsNodeInteraction.semanticsId()` has been removed. Use `SemanticsNodeInteraction.fetchSemanticsNode().id` instead. ([Ie397a](https://android-review.googlesource.com/#/q/Ie397a87c7e8bfd754474ebbb03c26f4a3215ba52))
- The old autofill APIs are deprecated. Use the new semantics based API instead. ([I943ff](https://android-review.googlesource.com/#/q/I943fffca639a172cf1db71a57c7a4aa7e74883cb))
- Rewrite `requestAutofill` API to exist outside of autofill manager. ([Id1929](https://android-review.googlesource.com/#/q/Id1929e5264d1a4a86b937236ee9357529f79fc71))

**Bug Fixes**

- Fixed focus issue where `requestFocus()` with a nonsensical `previouslyFocusedRect` parameter (related to the focus direction) would skip past a `ComposeView`. ([Ifdc2f](https://android-review.googlesource.com/#/q/Ifdc2f17b23620d1ae14848624f447f84cc1b0b5d), [b/388590015](https://issuetracker.google.com/issues/388590015))
- Fixed an occasional NPE when using `GraphicsLayer.record { this@ContentDrawScope.drawContent() }`. If you are recording `drawContent()` in this way, make sure to use the `GraphicsLayer#record` extension function inside `DrawScope`, and not the member function on `GraphicsLayer`. ([I75fc0](https://android-review.googlesource.com/#/q/I75fc026069666b61cdd7e5c377fa4da706f985d8), [b/389046242](https://issuetracker.google.com/issues/389046242))
- Fix text layout with ellipsis sometimes translating incorrectly during animations, see [b/389707025](https://issuetracker.google.com/issues/389707025) for more info ([Ie55b1](https://android-review.googlesource.com/#/q/Ie55b173dee87596cd270788794b3c0e5e20a0dc6), [b/389707025](https://issuetracker.google.com/issues/389707025))

### Version 1.8.0-alpha08

January 15, 2025

`androidx.compose.ui:ui-*:1.8.0-alpha08` is released. Version 1.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/ui).

**API Changes**

- Making `AutofillManager` an abstract class. ([I0a3b0](https://android-review.googlesource.com/#/q/I0a3b0c533ca7d05ed2125c5657f1936f971e0991))
- Fixed several focus-related issues, including crashes when IME tries to focus on `ComposeView` without focusable items, focus change within child `AndroidViews`, and focus request leaving an `AndroidView`. ([Ia03c3](https://android-review.googlesource.com/#/q/Ia03c3c04dc9fd9d55d8fcae6b15e15cb2384f467), [b/369256395](https://issuetracker.google.com/issues/369256395), [b/378570682](https://issuetracker.google.com/issues/378570682), [b/376142752](https://issuetracker.google.com/issues/376142752))
- Change `FocusEnterExitScope.cancelFocus()` to `cancelFocusChange()` ([I89959](https://android-review.googlesource.com/#/q/I89959589e5302fbda9782426938cade81a96f65e))
- You may now calculate Composable occlusions with `RectInfo.calculateOcclusions()`.
- Added extension function on `DelegatableNode` to register a listener for global layout changes. ([I68b59](https://android-review.googlesource.com/#/q/I68b59e47e171889766c809343a0126844c66d905))

**Bug Fixes**

- The activity that is used as the host for the composable under test when using `ComposeContentTestRule.setContent` now uses the theme `Theme.Material.Light.NoActionBar`, to avoid the `ActionBar` from overlapping with test content when targeting SDK 35. To opt out of this behavior, you can remove the dependency on `ui-test-manifest` and add an activity entry in your test app's AndroidManifest.xml for `ComponentActivity` with the theme of your choice. ([I7ae1b](https://android-review.googlesource.com/#/q/I7ae1bd28f5e341dafc07442b35ee4249793d257d), [b/383368165](https://issuetracker.google.com/issues/383368165))
- Resource fonts with the same variation settings will now avoid over-caching causing the incorrect variation settings to be applied. ([If3dff](https://android-review.googlesource.com/#/q/If3dff4ea44e33b1ed80bc7fb5057923a088f1678), [b/372044241](https://issuetracker.google.com/issues/372044241))
- `AnnotatedString.fromHtml` now supports `<ul>/<li>` tags. ([I7c2fe](https://android-review.googlesource.com/#/q/I7c2fe1717e72b66da4b2613efbeeb7b6f5ebb44e), [b/299662276](https://issuetracker.google.com/issues/299662276), [b/139326648](https://issuetracker.google.com/issues/139326648))

**External Contribution**

- Added a new Clipboard interface and a composition local for it. ([I80809](https://android-review.googlesource.com/#/q/I808099e232564d551aeeb8ed09e74ab62d9354ed))

### Version 1.8.0-alpha07

December 11, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha07` is released. Version 1.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/compose/ui).

**API Changes**

- Exposed owner from `LayoutNode` for tools. ([I26f7f](https://android-review.googlesource.com/#/q/I26f7fd089daaab84d3e605f0f5231b171d09afce))
- Has `LocalAutofillHighlightColor` composition local use a Color type. ([I0e05b](https://android-review.googlesource.com/#/q/I0e05bc47c50ff04a873169ab69dfc79f9ecc0579))
- Keep deprecated `UrlAnnotation` and its methods marked as experimental. ([Ic0021](https://android-review.googlesource.com/#/q/Ic00213e5ce4f28ffc2548a6e5a97944262c421cf))

**Bug Fixes**

- Fixed `IndexOutOfBoundsException` crash when using `LinkAnnotation` inside the `BasicText` or Text composable ([be7605](https://android-review.googlesource.com/#/q/be7605af63fcd036dd037a67a1b18f2166598f6e), [b/374115892](https://issuetracker.google.com/issues/374115892))
- Fixed issue where filled text fields with custom shape didn't clip the indicator line. ([I4f87f](https://android-review.googlesource.com/#/q/I4f87f4637da0f17e9e435fa5609061fd320b7f7b), [b/380704151](https://issuetracker.google.com/issues/380704151))
- Fixed missing backgrounds with long screenshots. ([I4d57a](https://android-review.googlesource.com/#/q/I4d57a4fedb020cc80a6df71054c768bd3c640bd0))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Idfef8](https://android-review.googlesource.com/#/q/Idfef8002dd13e94de525c5e53d018437e2cc050b), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Update Compose support for wide gamut and HDR colors when running on Android Q+. ([Icd8be](https://android-review.googlesource.com/#/q/Icd8bea0a02aeea8ac8a06cda9684eed39dc4b990), [b/379135036](https://issuetracker.google.com/issues/379135036))
- Resource fonts that fail to load will now silently fall back to the default font, instead of the prior behavior of throwing an exception in measure. ([Ib6a49](https://android-review.googlesource.com/#/q/Ib6a4941f8679d9c40bbcb3422d8d6a0a79633181))
- Fix focus lost when `AndroidView` is detached and attached. ([I53446](https://android-review.googlesource.com/#/q/I53446d6e0f234ce408ed8555a6300d90e874b5c1))
- Accept `requestFocus()` from beyond bound layout action. ([Ia8461](https://android-review.googlesource.com/#/q/Ia84613ee89e40cb62a7682defea43b0a62c1cdda))

**External Contribution**

- Add `BringIntoViewResponderModifierNode` to UI, which provides a new way to implement Bring Into View functionality as well as allows implementing in on a platform level. ([Ia6dd8](https://android-review.googlesource.com/#/q/Ia6dd89b79c7a4e04fea0d73410b2b76e779b793f))

### Version 1.8.0-alpha06

November 13, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha06` is released. Version 1.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/ui).

**API Changes**

- Adds `stylusHoverIcon` modifier. ([Iff20a](https://android-review.googlesource.com/#/q/Iff20af03b451228bc44c4356d4b4e89956cc3b45), [b/331289114](https://issuetracker.google.com/issues/331289114))
- Changes Autofill manager to be an interface. ([I84914](https://android-review.googlesource.com/#/q/I8491407de5699bf7273b9f88bda11cc438e2fd62), [b/376080755](https://issuetracker.google.com/issues/376080755))
- Adds `requestFocus(FocusDirection)` to both `focusRequester` and `FocusTargetModifierNode` to allow focusing with a specific direction. ([I5d9ec](https://android-review.googlesource.com/#/q/I5d9eca3a2cd283c1b84ad6b77d929ef9a49ce4cc), [b/245755256](https://issuetracker.google.com/issues/245755256))
- `FocusProperties.enter` and `FocusProperties.exit` have been replaced with `onEnter` and `onExit`, using a receiver scope instead of `FocusDirection` parameter. ([I6e667](https://android-review.googlesource.com/#/q/I6e667ad84b51a525531f4902c1a0ac6ab8b4fba8))
- Adding autofill support in text toolbar. ([Ie6a4c](https://android-review.googlesource.com/#/q/Ie6a4c0542737d76d603a925f85c389c81eb49747))
- API changes to `Modifier.focusRestorer()` ([I99c03](https://android-review.googlesource.com/#/q/I99c038bcc996de64b5fa3219192e37752e7243bc)):
  - parameter name changed to 'fallback'
  - parameter is now a `FocusRequester` and not a lambda
  - parameter is now non-NULL with Default as the default value
- Removing `@Experimental` annotation from autofill manager interface. The feature is still WIP targeting this release but we do not want to introduce @Expemiental API ([Id8398](https://android-review.googlesource.com/#/q/Id83983b6de73b1fe7a958d7fcc12914f8d896081))
- `LocalHapticFeedback` now provides a default `HapticFeedback` implementation when the Vibrator API indicates that haptics are supported. The following have been added to the `HapticFeedbackType` - `Confirm`, `ContextClick`, `GestureEnd`, `GestureThresholdActivate`, `Reject`, `SegmentFrequentTick`, `SegmentTick`, `ToggleOn`, `ToggleOff`, `VirtualKey`. Wear Compose long-clickable components such as `Button`, `IconButton`, `TextButton`, and `Card` now perform the `LONG_PRESS` haptic when a long-click handler has been supplied. ([I5083d](https://android-review.googlesource.com/#/q/I5083db2ce3619189c0a3793de9f535d996029c75))
- Removes `OverscrollConfiguration` and `LocalOverscrollConfiguration`, and adds `rememberPlatformOverscrollFactory` to create an instance of / customize parameters of the default overscroll implementation. To disable overscroll, instead of `LocalOverscrollConfiguration provides null`, use `LocalOverscrollFactory provides null`. To change the glow color / padding, instead of `LocalOverscrollConfiguration provides OverscrollConfiguration(myColor, myPadding)`, use `LocalOverscrollFactory provides rememberPlatformOverscrollFactory(myColor, myPadding)`. ([Ie71f9](https://android-review.googlesource.com/#/q/Ie71f9a016face13262f4fe16ac56c40a0d6f9712), [b/255554340](https://issuetracker.google.com/issues/255554340), [b/234451516](https://issuetracker.google.com/issues/234451516))
- Removed the experimental `GlobalAssertions` API. It's intended use was to run accessibility checks, see `enableAccessibilityChecks()` for that purpose instead. ([I59322](https://android-review.googlesource.com/#/q/I5932296f2aca4c3daa30a013dd00e876ecebb077))

### Version 1.8.0-alpha05

October 30, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha05` is released. Version 1.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/ui).

**New Features**

Autofill is exposed behind a feature flag in this release. We are working on improving performance, and are looking for early feedback on the APIs. The APIs are expected to evolve prior to stable based on feedback.

- To enable Autofill, set `ComposeUiFlags.isSemanticAutofillEnabled` to true in `onCreate` and use the latest Compose Snapshot.
- This version of Autofill supports saving credentials manually, through Suggest Strong Password, and through navigation. It also supports filling when an autofillable field receives focus or when Autofill is triggered via the text toolbar on text components. The component will become highlighted to indicate when autofill has completed.

**API Changes**

- Modify Autofill interface to follow `expect`/`actual` structure. ([I22dce](https://android-review.googlesource.com/#/q/I22dceea9de3ac5a716f059bb763e34e332ab4166))
- Introduce `CompositionLocal` that can be used to modify the hue of Autofill's successful filling highlight. ([I32092](https://android-review.googlesource.com/#/q/I320926246d1811c2c974a6793f48941907c33afe))
- Added `Modifier.onRectChanged` API which is an API that allows one to subscribe to the root/window/screen-relative position and size of a `LayoutNode`. The API solves many use cases that the existing `onGloballyPositioned` modifier does, however it does so with much less overhead and the API comes with facilities to debounce and throttle the callback per what one's use case demands. ([Id28c7](https://android-review.googlesource.com/#/q/Id28c7c6c52ce3b18c9ac8c83cde48111a312cfc9), [b/372765423](https://issuetracker.google.com/issues/372765423), [b/372757007](https://issuetracker.google.com/issues/372757007), [b/372994338](https://issuetracker.google.com/issues/372994338))
- Expands Autofill manager to include `commit()` and `cancel()` APIs that help users save newly entered credentials. ([I2da00](https://android-review.googlesource.com/#/q/I2da00b7050b12af7b978f2f52fe27dc74a6fd8f2))
- Introduces new `AutofillManager` interface that can be used to fine-tune users' Autofill journey and a `isSemanticAutofillEnabled` flag to turn on this new version of Autofill. ([I9d484](https://android-review.googlesource.com/#/q/I9d4842cc35b289158e889f89b7b65346f049e884))
- Added `Modifier.onRectChanged` API which is an API that allows one to subscribe to the root/window/screen-relative position and size of a `LayoutNode`. The API solves many use cases that the existing `onGloballyPositioned` modifier does, however it does so with much less overhead and the API comes with facilities to debounce and throttle the callback per what one's use case demands. ([I3c8fa](https://android-review.googlesource.com/#/q/I3c8fa250f561bbd846a9044118532ec439240efd))
- Add in semantic properties and data types for extended Autofill support. ([I52c7d](https://android-review.googlesource.com/#/q/I52c7dddff216239c3fd51abcaa41304b3219f301))
- All methods in `AnnotatedString` builder are non-experimental now ([Ia89c8](https://android-review.googlesource.com/#/q/Ia89c8c90e0047b9edf89774468d3e5bd00ffee9b), [b/261561823](https://issuetracker.google.com/issues/261561823))

**Bug Fixes**

- Views embedded in compose can now receive rotary events if they are focused ([I4d53a](https://android-review.googlesource.com/#/q/I4d53a569bdf935d66aa38ce2d7d1fb437b864a6b), [b/320510084](https://issuetracker.google.com/issues/320510084))
- Fixed an issue where various resource types wouldn't update on configuration changes ([Ia9b99](https://android-review.googlesource.com/#/q/Ia9b99f5bd6bdcdcbe2796b83bb2c25b139d0ceef), [b/352336694](https://issuetracker.google.com/issues/352336694))
- Addressed an issue that prevented `TextField` from functioning correctly when using the POBox Japanese Keyboard on certain older Sony devices. ([Ia9b99](https://android-review.googlesource.com/#/q/I94e0e598274fb88b255f977f9fbd50dfbbb1ecb1), [b/373743376](https://issuetracker.google.com/373743376))
- Fixed problem with dialogs showing at bottom of the screen instead of centering ([Ia2ec](https://android-review/googlesource.com/#/q/Ia2ec9f6edc2705cb8a13201d5e05a859a6bb9571), [b/373093006](https://issuetracker.google.com/373093006))
- Targeting API 35+ no longer forces dialogs to have `decorFitsSystemWindows` set to false. ([Ibc94](https://android-review/googlesource.com/#/q/Ibc94bd0bdfe6645e2e8b92dfbe39c93fece38a2f), [b/364492593](https://issuetracker.google.com/364492593))
- Fix crash when layers are moved between windows (e.g. dialog and main content) ([I675ba](https://android-review/googlesource.com/#/qI675ba974b5a89cd0dab974015ea27c2254c43e98), [b/330955281](https://issuetracker.google.com/330955281))

### Version 1.8.0-alpha04

October 16, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha04` is released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/ui).

**API Changes**

- Adds `DelegatableNode#onDensityChange` and `DelegatableNode#onLayoutDirectionChange` callbacks to allow updating node state when these change ([I04f3e](https://android-review.googlesource.com/#/q/I04f3e3afea5aabdc6225b1afb197df18133eb018), [b/340662451](https://issuetracker.google.com/issues/340662451))
- Adds `WindowInfo#containerSize` to provide the current window's content container size. This can be retrieved using `LocalWindowInfo`. ([Idc38c](https://android-review.googlesource.com/#/q/Idc38c705655c9181022161927275318fba86bed8), [b/369334429](https://issuetracker.google.com/issues/369334429), [b/360343819](https://issuetracker.google.com/issues/360343819))
- Introduce a fix for nested scrollables that are removed from the node tree during an ongoing fling. Now these nodes will cancel the fling and correctly send the `onPostFling` event with the remaining velocity. We're also introducing the flag `NewNestedScrollFlingDispatchingEnabled` to control the behavior in case of regressions. The flag will be removed before beta. ([I05c37](https://android-review.googlesource.com/#/q/I05c37b5d0ae42d8ed97c014383fe9df3282d61d6), [b/371168883](https://issuetracker.google.com/issues/371168883))
- Introduced `PointerInputModifierNode#touchBoundsExpansion`, which can be used to enlarge the touch bounds of a single pointer input modifier. ([Iccf02](https://android-review.googlesource.com/#/q/Iccf028b886639d3b24e7a257a023320362399389), [b/335339283](https://issuetracker.google.com/issues/335339283))
- Adds `WindowInfo#containerSize` to provide the current window's content container size. This can be retrieved using `LocalWindowInfo`. ([I27767](https://android-review.googlesource.com/#/q/I277673b5576f15f60bc82eeb9d9424c5144a3c25), [b/369334429](https://issuetracker.google.com/issues/369334429), [b/360343819](https://issuetracker.google.com/issues/360343819))
- Remove `readOnly` from `TextFields`' to pin to stable foundation version. ([I3aaba](https://android-review.googlesource.com/#/q/I3aaba4e10f1317459d6a57acf32ec3ad50cd30bd))
- `Paragraph` and `ParagraphIntrinsics` now takes a list of all annotations applied to the `AnnotatedString`, previously it only had a list of `SpanStyles` ([I12f80](https://android-review.googlesource.com/#/q/I12f8071e3bb8ed7871bb659e256569182680d49e))

**Bug Fixes**

- Updated how paragraphs are treated in `AnnotatedString`. Before you could only create non-overlapping paragraphs. Now the `AnnotatedString` allows fully-overlapping paragraphs which will be merged together, and nested paragraphs in which case the outer paragraph will be split on bounds of the inner one, and the inner paragraph's style will be merged with the outer paragraph's style ([Ic9554](https://android-review.googlesource.com/#/q/Ic9554c8201c430733543517dd697da3d5eace926))
- Fix crash in `AnnotatedString` with a zero-length `LinkAnnotation`. ([89aac6](https://android.googlesource.com/platform/frameworks/support/+/89aac60c7498f4bf0bb2719f0c0eb436c4e25afa))

### Version 1.8.0-alpha03

October 2, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha03` is released. Version 1.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/compose/ui).

**API Changes**

- Kotlin version update to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))
- Introduced a new Semantics Role called Carousel to emulate the list behavior in Pagers for a11y services. ([Id354b](https://android-review.googlesource.com/#/q/Id354b132da03348aaa68da0dd8459d4528438018), [b/354109776](https://issuetracker.google.com/issues/354109776), [b/239672673](https://issuetracker.google.com/issues/239672673))
- Rename `invisibleToUser()` to `hideFromAccessibility`. Its function remains the same. See documentation for more details. ([Ib43a3](https://android-review.googlesource.com/#/q/Ib43a30cc748b503b4e70551cdfe55c30118870b1))

**Bug Fixes**

- Updating docs for `SensitiveContent` modifier ([Ib0442](https://android-review.googlesource.com/#/q/Ib0442a40b4d009efe3eff6d3c26eede5093645e5))
- Fixed issue where certain generic outline clips would be ignored in combination with elevation shadows on some Android versions
- Fixed issue where empty clips would be applied when a generic outline clips was specified on certain Android versions.
- Fixed exception thrown when the IME is active on an external View and the Next action is used to enter focus on the `ComposeView`. The `clearFocus()` behavior aligns with View behavior on API \< 28, where `clearFocus()` can cause the default View to be focused.
- Fixed an issue where placement happened on detached nodes in `LazyList` by separating the management of subcomposition for different layout passes.
- Fixed a problem where the Software Keyboard flickers when focus switches from a `TextField` to an `EditText` or any other View based editor.
- Nested Scroll nodes will now dispatch `onPostFling` events correctly after they get detached.
- General performance improvements

### Version 1.8.0-alpha02

September 18, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988..0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/ui).

**API Changes**

- `TextOverflow.StartEllipsis` and `TextOverflow.MiddleEllipsis` are now available which allows to place ellipsis at the start or middle of the line of the single line text. ([I38913](https://android-review.googlesource.com/#/q/I389132c71774d5c13afce85a8719af697431cef9), [b/185418980](https://issuetracker.google.com/issues/185418980))

**Bug Fixes**

- Fix Dalog `dismissOnClickoutside` ([39a3d](https://android.googlesource.com/platform/frameworks/support/+/39a3db5b65c127043043cd67a773657c931c4188), [b/364508685](https://issuetracker.google.com/issues/364508685))
- Don't clip shadows of dialog content ([e8e2f](https://android.googlesource.com/platform/frameworks/support/+/e8e2f7ff6b2135b7e2299830fba63d9255bb68b9), [b/363027803](https://issuetracker.google.com/issues/363027803))
- Fix errant behavior when focus search moves between Compose and a View ([58377](https://android.googlesource.com/platform/frameworks/support/+/58377bb3416cc24d342dd4e5d32e4a27247734e4), [b/350534714](https://issuetracker.google.com/issues/350534714))

**External Contribution**

- The `AlignmentLines` `Map` now accepts `VerticalAlignmentLine` or `HorizontalAlignmentLine` concrete types. ([I02912](https://android-review.googlesource.com/#/q/I0291247955d66a3d95b7984f3bc931e3b3e55e21))
- New common `ByteArray.decodeToImageBitmap(): ImageBitmap` method. ([I83c21](https://android-review.googlesource.com/#/q/I83c21fee43d4df2d74831ea8c5e5cea4dd9d3520))

### Version 1.8.0-alpha01

September 4, 2024

`androidx.compose.ui:ui-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..71a0e55934198cacb4c897d9b20e26e2b7275988/compose/ui).

## Version 1.7

### Version 1.7.8

February 12, 2025

`androidx.compose.ui:ui-*:1.7.8` is released. Version 1.7.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/456f991655af86d9ae121f7e93f8699f958fc7ac..215cdfd8cb9c0762dd0347c383250644057c367f/compose/ui).

### Version 1.7.7

January 29, 2025

`androidx.compose.ui:ui-*:1.7.7` is released. Version 1.7.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5e65beadeb2e2c15f34d0fff72861847795cca4f..456f991655af86d9ae121f7e93f8699f958fc7ac/compose/ui).

**Bug Fixes**

- Fixed `IndexOutOfBoundsException` when passing an `AnnotatedString` with the `LinkAnnotation` to the Text composable. ([Ic96d2](https://android-review.googlesource.com/#/q/Ic96d2868e3edd1ca11d718670fd494a8d402e086))
- Fixed a timeout issue in tests in some rare cases when `LinkAnnotation` is used in the `AnnotatedString`. ([I04a03](https://android-review.googlesource.com/#/q/I04a03e58abf7be25bd9dabc92ef761e6d121154d))

### Version 1.7.6

December 11, 2024

`androidx.compose.ui:ui-*:1.7.6` is released. Version 1.7.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cbf03b378a865660d8209d0229c2bb1928c6e33..5e65beadeb2e2c15f34d0fff72861847795cca4f/compose/ui).

**Bug Fixes**

- We previously used to throw an error whenever we encountered a key event when we encountered a key event when the focus system had pending invalidations. We now log an error instead ([I7ea0](https://android-review.googlesource.com/c/platform/frameworks/support/+/3164436), [b/346370327](https://issuetracker.google.com/issues/346370327)).
- Removed experimental annotation from `SemanticsPropertyReceiver.invisibleToUser()`. This will be deprecated in 1.8 to be replaced with `SemanticsPropertyReceiver.hideFromAccessibility()`. ([I448f0](https://android-review.googlesource.com/#/q/I448f035d73f9c98b6fa89653602e0cf9241a8e06), [b/376479686](https://issuetracker.google.com/issues/376479686))
- Fixed an issue that prevented `TextField` from functioning correctly when using the POBox Japanese Keyboard on certain older Sony devices. ([I94e0e](https://android-review.googlesource.com/c/platform/frameworks/support/+/3317256), [b/373743376](https://issuetracker.google.com/issues/373743376))
- Fixed an accessibility issue where `BasicText`'s inlineContent was not announced by `TalkBack`. ([I67bcb](https://android-review.googlesource.com/c/platform/frameworks/support/+/3376831), [b/376479686](https://issuetracker.google.com/issues/376479686))

### Version 1.7.5

October 30, 2024

`androidx.compose.ui:ui-*:1.7.5` is released. Version 1.7.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b0ae0e41147a8a917cab35b4a6487af4fce6ead..4cbf03b378a865660d8209d0229c2bb1928c6e33/compose/ui).

**Bug Fixes**

- Fixed issues where elevation and clipping with custom outlines would not render properly.
- Fixes a text crash that happens with a zero-width `LinkAnnotation`. ([Ic1e2e](https://android-review.googlesource.com/#/q/Ic1e2ea95709415fa40222298d70918a1cf2ccf42))
- Fixes an announcement in `Talkback` of the button when it's built as a clickable Text composable. ([I1f588](https://android-review.googlesource.com/#/q/I1f588e2fcef0c4aa85ba2051c3df42f6a33ff300))

### Version 1.7.4

October 16, 2024

`androidx.compose.ui:ui-*:1.7.4` is released. Version 1.7.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/00e91ed140ce2c4677f56fc06692b182b8a07fcf..6b0ae0e41147a8a917cab35b4a6487af4fce6ead/compose/ui).

### Version 1.7.3

October 2, 2024

`androidx.compose.ui:ui-*:1.7.3` is released. Version 1.7.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9..00e91ed140ce2c4677f56fc06692b182b8a07fcf/compose/ui).

**Bug Fixes**

- Fixed issue where specifying a generic outline clip would lead to an empty clip boundary on certain Android versions.
- Fixed exception thrown when the IME is active on an external View and the Next action is used to enter focus on the `ComposeView`. The `clearFocus()` behavior aligns with View behavior on API \< 28, where `clearFocus()` can cause the default View to be focused.
- Fixed an issue where an incorrect `placeOrder` was used for lookahead invalidation, therefore fixing an edge case where lookahead placement was skipped.

### Version 1.7.2

September 18, 2024

`androidx.compose.ui:ui-*:1.7.2` is released. Version 1.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1efd0b233a17f707cd918993df1fa12e0bf9ae83..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/ui).

**Bug Fixes**

- Improved performance of accessibility node info and semantics events by removing verbose tracing. ([I89156](https://android-review.googlesource.com/#/q/I891564c39879b0863a1d9543b4b44d786ebea4ba), [b/362530618](https://issuetracker.google.com/issues/362530618))
- `ComposeView` will no longer crash when passed exceptionally large measurement size ([da5db](https://android.googlesource.com/platform/frameworks/support/+/da5db3a60da057fce9095ba925d90bd44f4cbb27), [b/347036173](https://issuetracker.google.com/issues/347036173))
- Fixed an accessibility screenreader issue where `LiveRegion` announcements on buttons were not made. ([f66fa7](https://android.googlesource.com/platform/frameworks/support/+/f66fa79d19e5874f0afaa6868363c69ecf851cf2), [b/348590026](https://issuetracker.google.com/issues/348590026))

### Version 1.7.1

September 10, 2024

- No changes to Android artifacts. `-desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts.

### Version 1.7.0

September 4, 2024

`androidx.compose.ui:ui-*:1.7.0` is released.

**Important changes since 1.6.0**

Important changes in version 1.7.0 are covered in [this blogpost](https://android-developers.googleblog.com/2024/05/whats-new-in-jetpack-compose-at-io-24.html).

### Version 1.7.0-rc01

August 21, 2024

`androidx.compose.ui:ui-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98bc1cf10201a973793b72d2ff1ae728070e47e4..d8995e2377dd4baad64b39becb6d480cadd05c86/compose/ui).

**Notable changes**

- ui:ui module now forces requirement of a minimum version of foundation:foundation to be at least 1.7.0-rc01 or newer. This is enforced to remedy a behaviour incompatibility between ui and foundation in regards to `NestedScrollSource` changes that happened early during 1.7.0-alpha01.

### Version 1.7.0-beta07

August 7, 2024

`androidx.compose.ui:ui-*:1.7.0-beta07` is released. Version 1.7.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16151cbc8a68e976da6f2b0f624c2e9883c55aa3..98bc1cf10201a973793b72d2ff1ae728070e47e4/compose/ui).

**Bug Fixes**

- Text input related `SemanticsNodeInteraction` functions `performTextReplacement`, `performTextInput`, and `performTextClearance` is now going to throw assertion errors when they are called on read only `TextFields`. ([I4ae8f](https://android-review.googlesource.com/#/q/I4ae8f255bd02f3b13af2a106340f49f5595a78a8))

### Version 1.7.0-beta06

July 24, 2024

`androidx.compose.ui:ui-*:1.7.0-beta06` is released. Version 1.7.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8346df8de9f86a546fc9c316113bd4a3cc82ede9..16151cbc8a68e976da6f2b0f624c2e9883c55aa3/compose/ui).

### Version 1.7.0-beta05

July 10, 2024

`androidx.compose.ui:ui-*:1.7.0-beta05` is released. Version 1.7.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/487d2b07dba29c903cfd87a8dc7f99483084ebb6..8346df8de9f86a546fc9c316113bd4a3cc82ede9/compose/ui).

**Bug Fixes**

- Fixed a bug where changing the software keyboard would cause `TextField` to not accept input from the new keyboard until the focus is lost and regained.
- Fixed an issue where attempts to persist layer contents would cause unintended side effects when rendering with `SurfaceView` content.

### Version 1.7.0-beta04

June 26, 2024

`androidx.compose.ui:ui-*:1.7.0-beta04` is released. Version 1.7.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c29f7383c14ede0af9cb64be9f3eee63714bc73c..487d2b07dba29c903cfd87a8dc7f99483084ebb6/compose/ui).

**Bug Fixes**

- Avoid crashes when measuring very large text lines (e.g. 10k characters) ([8157ab](https://android.googlesource.com/platform/frameworks/support/+/8157ab1cf5d805e9d626b17e710df49bd6e5d680))
- Disable software rendering support for the `GraphicsLayer` API. ([35ddd8](https://android.googlesource.com/platform/frameworks/support/+/35ddd8cb7873c11ccc56c73ad2e4ee4e96ae2b68))
- Fix for a crash in layer persistence logic. ([70b13e](https://android.googlesource.com/platform/frameworks/support/+/70b13e38e559c9516a79d6d8d39a6cacea4421a0))
- Reusing layer objects optimization was reverted, as it caused rendering issues. ([70b13e](https://android.googlesource.com/platform/frameworks/support/+/70b13e38e559c9516a79d6d8d39a6cacea4421a0))

### Version 1.7.0-beta03

June 12, 2024

`androidx.compose.ui:ui-*:1.7.0-beta03` is released. Version 1.7.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a123f646cfea1599f9efead6da546b0c26063fa..c29f7383c14ede0af9cb64be9f3eee63714bc73c/compose/ui).

### Version 1.7.0-beta02

May 29, 2024

`androidx.compose.ui:ui-*:1.7.0-beta02` is released. Version 1.7.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..1a123f646cfea1599f9efead6da546b0c26063fa/compose/ui).

**API Changes**

- Renamed `SemanticsProperties.Editable` to `IsEditable` and changes `SemanticsPropertyReceiver.editable` to a val `isEditable`. The property is now a boolean and always specified by text fields. ([I8acd8](https://android-review.googlesource.com/#/q/I8acd87bcdfc80b70de9665ba45708ca529ccdf69))
- Rename accessibility benchmark parameter. ([I3d440](https://android-review.googlesource.com/#/q/I3d4405c9fecc11b98eec71c82f763d7e78fa9d55))
- Updated API for styling the links: `TextLinkStyles` is now part of the `LinkAnnotation` constructor and the `AnnotatedString.fromHtml` method ([I90b2b](https://android-review.googlesource.com/#/q/I90b2b73e126d9c1106c223de823dda8babaf6708)). Also removed the `TextDefaults` from material ([I5477b](https://android-review.googlesource.com/#/q/I5477bdb498b6b4f33ab3bc998e2be59d8a4ff7e4))

**Bug Fixes**

- Renamed `LayoutCoordinates.introducesFrameOfReference` to `LayoutCoordinates.introducesMotionFrameOfReference` to better reflect its purpose. Renamed related function to calculate coordinates based on that flag. ([I3a330](https://android-review.googlesource.com/#/q/I3a3301164ea2c08728b09faed6cf72ae089ead72))

### Version 1.7.0-beta01

May 14, 2024

`androidx.compose.ui:ui-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/ui).

**API Changes**

- Renamed `performCustomAccessibilityActionLabelled` to `performCustomAccessibilityActionWithLabel` and `performCustomAccessibilityActionWhere` to `performCustomAccessibilityActionWithLabelMatching`. ([I5387f](https://android-review.googlesource.com/#/q/I5387fb9656bffdc8d6f08991ccf90d4b2d40a1e7))
- `AnnotatedString.hasEqualsAnnotations` is now `hasEqualAnnotations` ([I685c0](https://android-review.googlesource.com/#/q/I685c066bc518b511146443d67926462b341991b2))
- Updated the API for getting Material themed links in text. Specifically, removed the methods from the `TextDefaults` for constructing themed `LinkAnnotations` and parse HTML with themed links. Instead, added a `TextLinkStyles` class that allows to style the links as a parameter to the Text composable. ([I31b93](https://android-review.googlesource.com/#/q/I31b93f4460f4a0a50c7a86996a499d359ba455c8))

**Bug Fixes**

- Fixes additional use cases when dynamically adding pointer input modifiers during events [63e1504](https://android.googlesource.com/platform/frameworks/support/+/63e15049e0f6cecf43aec620d4bf5c4dbde1c2ab)

### Version 1.7.0-alpha08

May 1, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha08` is released. Version 1.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7/compose/ui).

**API Changes**

- Adds support for mutable shape implementations. `Shape#createOutline` is now observed inside graphics layers, so reading state values inside will cause invalidations when the state changes, allowing for more performant shape animations. ([Id1629](https://android-review.googlesource.com/#/q/Id1629c24f02d882ba0de5e3e82fbc1284accc3ea), [b/326070216](https://issuetracker.google.com/issues/326070216))
- Renamed `isPositionedByParentWithDirectManipulation` to `introducesFrameOfReference`. Note that it now has the reverse effect, meaning that by default, most `LayoutCoordinates` introduce a frame of reference, and, only when placed under direct manipulation the property will be false. To query position with only those that introduce a frame of reference, use `positionInLocalFrameOfReference(...)`. Or `positionInLocalLookaheadFrameOfReference` from a `LookaheadScope`. ([Ifc5f7](https://android-review.googlesource.com/#/q/Ifc5f78c683543035e13ff727edf14a79075b1a84))
- `LookaheadScope` APIs have been made stable ([I21507](https://android-review.googlesource.com/#/q/I21507b73d88acc221e5963b76b9f1a83539342db))
- Change action lambda for `getScrollViewportLength` as per API council feedback. ([Ibc74a](https://android-review.googlesource.com/#/q/Ibc74abf76a2d5d88f97b9c5853a3d3b2d58585b9))
- Updated `GraphicsLayer` outline APIs to consume float parameters instead of int. Removed `UnsetOffset/UnsetSize IntSize` sentinel values in favor of already existing Unspecified constants on float based Offset and Size inline classes ([I2fb03](https://android-review.googlesource.com/#/q/I2fb03296a009ad4957a59905b97b6f21355cb8ba), [b/333863462](https://issuetracker.google.com/issues/333863462))
- When injecting mouse input during tests, `MouseInjectionScope.click()`, `MouseInjectionScope.doubleClick()`, `MouseInjectionScope.tripleClick()`, `MouseInjectionScope.longClick()` now accept a `button: MouseButton` parameter to make them more universally applicable. The default value is `MouseButton.Primary` for all methods. ([I31a23](https://android-review.googlesource.com/#/q/I31a23e6819a82b5513db3731dce3bf8cd7587d69), [b/190493367](https://issuetracker.google.com/issues/190493367), [b/261439695](https://issuetracker.google.com/issues/261439695))
- Renamed `onClicked` to `onClick` inside `LinkInteractionListener`. ([Iaa35c](https://android-review.googlesource.com/#/q/Iaa35cd1c54bdea113071a2eaf1e7d700e0eb5f19))
- Rename `TextInclusionStrategy.isInside` to `isIncluded`. Make `Paragraph/MultiParagraph#getRangeForRect()` return type non nullable. ([I51f26](https://android-review.googlesource.com/#/q/I51f269566495a3781946c8a72e6b615af2da57b9))

**Bug Fixes**

- Fixed long screenshot capture for scrolling containers with `reverseScrolling=true`. ([I7c59c](https://android-review.googlesource.com/#/q/I7c59cd9f43ca6968f3eefadbcfc7582c1aec51c7))

**External Contribution**

- Added support for prefetching items in nested `LazyLists` (e.g. a `LazyColumn` that renders nested `LazyRows`). This change is expected to reduce frame drops during scrolling for these `LazyLists`. The implementation default is to prefetch the first 2 nested items, however this behavior can be controlled by the new `LazyLayoutPrefetchStrategy(nestedPrefetchItemCount)` and `LazyListPrefetchStrategy#onNestedPrefetch` APIs. ([I51952](https://android-review.googlesource.com/#/q/I519526a694d8e9a89a1a040cd179d0416fa2d6d9))

### Version 1.7.0-alpha07

April 17, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha07` is released. Version 1.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/ui).

**API Changes**

- `ClickableText` is marked as deprecated. To add links to the text, create an `AnnotatedString` with a `LinkAnnotation` corresponding to your link and pass this `AnnotatedString` to the Text composable. ([I34d4b](https://android-review.googlesource.com/#/q/I34d4bf29a9386820f8582765e62576a5fcfcd3c6), [b/323346994](https://issuetracker.google.com/issues/323346994))
- Introduce `ViewConfiguration.HandwritingGestureLineMargin` for handwriting gestures. Support `JoinOrSplit` gesture for `BasicTextField` ([Ie6e13](https://android-review.googlesource.com/#/q/Ie6e13b41cc82da1fd3c9ecc7ac34c3ff88dfa235), [b/325660505](https://issuetracker.google.com/issues/325660505))
- `FocusProperties.enter` and `FocusProperties.exit` are no longer experimental. `FocusDirection.Enter` and `FocusDirection.Exit` are no longer experimental. `FocusRequester.Cancel` is no longer experimental ([I461a1](https://android-review.googlesource.com/#/q/I461a1335e08f7ec1b944e145d18d5559377a95c8), [b/261564106](https://issuetracker.google.com/issues/261564106))
- When querying Layout coordinates, you may now use the `excludeDirectManipulationOffset` argument to exclude the offset set by parent Layouts that placed their children using `Placeable.PlacementScope.withDirectManipulationPlacement`. Likewise, a Layout that changes the position of its children frequently may now place them using `withDirectManipulationPlacement` (such as Scroll, implemented by default). This helps `approachLayout` based animations to be more intuitive, having now the opportunity to differentiate what offset to animate, and what to apply directly when deciding to animate their approach. ([I60ec7](https://android-review.googlesource.com/#/q/I60ec77cec9d448ffdfed8b661ba2e433f3adaa55))
- The feature flag for long screenshots has been removed. ([I28648](https://android-review.googlesource.com/#/q/I28648d10fcd1293913a289ea21e64611248693a6), [b/329128246](https://issuetracker.google.com/issues/329128246))
- `LazyColumn` will now render sticky headers correctly in long screenshots. ([I8d239](https://android-review.googlesource.com/#/q/I8d239dddc5301c16a76b348edfab482adcdd157d), [b/329296635](https://issuetracker.google.com/issues/329296635))
- `NestedScroll` sources Drag and Fling are being replaced by `UserInput` and `SideEffect` to accommodate for the extended definition of these sources that now include animations (Side Effect) and Mouse Wheel and Keyboard (`UserInput`). ([I40579](https://android-review.googlesource.com/#/q/I40579c9b053d6bcf477191b212c7a72876a588b7))
- `ApproachLayoutModifierNode` and `Modifier.approachLayout` are now stable, with new `isMeasurementApproachInProgress()` and `isPlacementApproachInProgress()` to replace the old `isMeasurementApproachComplete()` and `isPlacementApproachComplete()` respectively.
- Removed deprecated `intermediateLayout` modifier. ([I3e91c](https://android-review.googlesource.com/#/q/I3e91ca2cfabebde655491f063466d2e5642f055e))
- Rename `GraphicsLayer#buildLayer` to record to mirror the begin/endRecording methods of Displaylist backed APIs like `RenderNode` and Picture.
- Updated `rememberGraphicsLayer` to leverage `rememberObserver`. ([I312c1](https://android-review.googlesource.com/#/q/I312c1120358d04fccfe8a646001a883017fb0fb3), [b/288494724](https://issuetracker.google.com/issues/288494724), [b/330758155](https://issuetracker.google.com/issues/330758155))
- `UrlAnnotation` is deprecated, use `LinkAnnotation.Url` instead. If you're using Material theming, then use `TextDefaults` object to create the annotation with Material theming applied to it ([I8d180](https://android-review.googlesource.com/#/q/I8d18033220b74bb84f74380855ef5efb5e3e92bb), [b/323346545](https://issuetracker.google.com/issues/323346545))
- Text links got pressed state styling option in addition to normal styling, hovered and focused ([I5f864](https://android-review.googlesource.com/#/q/I5f864b3fd1b1af6ff39dee03e1aa65ede7e16d32), [b/139312671](https://issuetracker.google.com/issues/139312671))
- `String.parseAsHtml` renamed to `AnnotatedString.Companion.fromHtml`. ([I43dcd](https://android-review.googlesource.com/#/q/I43dcd5b6f6ddc634879f5747df4b911953f84632))
- Added styling arguments (`linkStyle`, `focusedLinkStyle`, `hoveredLinkStyle`) and a link interaction listener to the `parseAsHtml` method. When parsing the HTML-tagged string with `<a>` tags, the method will construct a `LinkAnnotation.Url` for each such tag and pass the styling objects and link interaction listener to each annotation. ([I7c977](https://android-review.googlesource.com/#/q/I7c9777a340e04ccf4dc10258c83d18e69831b3c6))
- `LinkAnnotation` now takes the state-based styling arguments and a `LinkInteractionListener`. Add this annotation to the `AnnotatedString` to get a hyperlink. By passing `focusedState` and/or `hoveredState` you can define the visual `configuration` for links when they are focused and/or hovered. ([I81ce4](https://android-review.googlesource.com/#/q/I81ce4350b8a1e37881000fd82f081b7afb8e0f42), [b/139312671](https://issuetracker.google.com/issues/139312671))
- `ImeOptions.hintLocales` is no longer nullable. If you want to pass an empty Locale list, please use `LocaleList.Empty`. ([Ic5bc4](https://android-review.googlesource.com/#/q/Ic5bc4e784d61b40ebc69778758515eb240c01e20))

**Bug Fixes**

- Gracefully handles bad/corrupt historical input event data (ignores bad offset data).
- Fixes unexpected pointer events when a pointer input modifier is added dynamically before another pointer input modifier during an active pointer input event stream (for example, between a hover enter and hover exit \[mouse/stylus\]).

### Version 1.7.0-alpha06

April 3, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha06` is released. Version 1.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/ui).

**New Features**

- Added `parseAsHtml` method for styled strings: it allows to convert a string marked with HTML tags into `AnnotatedString`. Note that not all tags are supported, for example you won't be able to display bullet lists yet. ([I84d3d](https://android-review.googlesource.com/#/q/I84d3d1881805e964cea940eb1c68a5bba16f6416), [I30626](https://android-review.googlesource.com/#/q/I306261acf030feb96e8b8198f88b25375ed9356b), [b/139326648](https://issuetracker.google.com/issues/139326648))
- Implemented experimental support for long screenshots in Compose scroll containers using the official Android API (`ScrollCaptureCallback`). This feature is experimental and may not currently handle all cases correctly. For that reason it is currently disabled by default. To opt-in, set the `ComposeFeatureFlag_LongScreenshotsEnabled` flag to true. ([I2b055](https://android-review.googlesource.com/#/q/I2b0552d34c530b127d64ac58f48a0fa399b3edde), [b/329296471](https://issuetracker.google.com/issues/329296471))

**API Changes**

- `fun ClipEntry.getMetadata()` is changed to `val ClipEntry.clipMetadata`. ([I50155](https://android-review.googlesource.com/#/q/I50155cef29574f74be45e850d210d0c405aa69f5))
- Removed `ClipboardManager.getClipMetadata` and `ClipboardManager.hasClip` functions. Please use `clipEntry.getMetadata()` to read the current clip entry's metadata. Also check `ClipboardManager.getClip`'s result if it's null or not to understand whether Clipboard has a current clip. ([I50498](https://android-review.googlesource.com/#/q/I504988d835b71009609c01919b387239a1e2bee0))
- Now you can pass `GraphicsLayer` objects into `placeable.placeWithLayer()` functions ([I1b22f](https://android-review.googlesource.com/#/q/I1b22f3bcddefb2124f32d63aa34780026eae2475))
- `ClipboardManager.setClip` now accepts null to be able to clear the Clipboard. ([I7d2e9](https://android-review.googlesource.com/#/q/I7d2e957005fb2efecc64b7273d8209161016b36a))
- Added resource ids for assist with hiding Views used as implementation details within build tooling ([I99531](https://android-review.googlesource.com/#/q/I99531f701d07e95a28aeafd720ec7e999e2254c2))
- Added `GraphicsLayer#toImageBitmap` suspend method to support rendering contents of a bitmap into a `GraphicsLayer`. This is a hardware accelerated rendering operation on API level 22+ (inclusive) which supports over 99% of all Android devices. On Android API level 21 this falls back onto software rendering. ([I9e114](https://android-review.googlesource.com/#/q/I9e1147c069aa609e96f80b92c41d076d097be962))
- Helper method to convert an Android `RectF` to `ComposeRect` ([I39925](https://android-review.googlesource.com/#/q/I399254fb5d0f0c250a1c55b7418613fa88f655d0), [b/325660505](https://issuetracker.google.com/issues/325660505))
- All `KeyboardOptions` parameters now have an unspecified value by default. Added `KeyboardOptions.merge` method.
- Renamed `KeyboardOptions.autoCorrect` to `autoCorrectEnabled` and made it nullable, where null indicates no value was specified. ([Ia8ba0](https://android-review.googlesource.com/#/q/Ia8ba0fb1235a7a1c6c42d140119ddcb40b65892d), [b/295951492](https://issuetracker.google.com/issues/295951492))
- `BasicTextField(state)` variant and `BasicSecureTextField` now use `KeyboardActionHandler` instead of `KeyboardActions` to process actions taken by the software keyboard. ([I58dda](https://android-review.googlesource.com/#/q/I58dda71cd89a62a1fa34df44a40f7bc0e7384991))

### Version 1.7.0-alpha05

March 20, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha05` is released. Version 1.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/ui).

**New Features**

- Introduce new `GraphicsLayer` API to record drawing commands in a display list as well as additional properties that affect the rendering of the display list. This provides an isolation boundary to divide a complex scene into smaller pieces that can be updated individually of one another without recreating the entire scene. Transformations made to a `GraphicsLayer` can be done without re-recording the display list. Unlike `Modifier.graphicsLayer`, `GraphicsLayer` allows for rendering of Composable content elsewhere and is useful in animated use cases where content is expected to be rendered in different scenes.

**API Changes**

- `GraphicsLayer.draw(Canvas)` is not a public api anymore. Please use the `DrawScope.drawLayer(GraphicsLayer)` extension function instead to draw the layer. ([I7a7c0](https://android-review.googlesource.com/#/q/I7a7c001e58c2f6d4b13562b75a5695bab27aec9d))
- Split `restrictedConstraints()` to two methods: `fitPrioritizingWidth()` and `fitPrioritizingHeight()` ([I6d7fd](https://android-review.googlesource.com/#/q/I6d7fd3811fffff13b3343c5365290e73cb151bcb))
- Introduced `HardwareCanvas` stub for Android L usage ([I1c3b5](https://android-review.googlesource.com/#/q/I1c3b5821c20f51b9c8ae96f81c822174583251b7), [b/288494724](https://issuetracker.google.com/issues/288494724))
- Update Compose framework to expose a `GraphicsContext` composition local alongside updating Owner, `DelegateableNode` and `drawWithCache` Modifier implementations to expose access to the `GraphicsContext` for scoped access that will automatically cleanup `GraphicsLayer` instances when Modifiers are torn down. ([I64a2f](https://android-review.googlesource.com/#/q/I64a2f6a2e156f9305fe32ac2a6f9be2b61f7f0ed), [b/288494724](https://issuetracker.google.com/issues/288494724))
- Introduced `InterceptPlatformTextInput` for helping write low-level IME-related tests and other low-level IME use cases. `PlatformTextInputTestOverride` has been deprecated. ([I862ed](https://android-review.googlesource.com/#/q/I862ed2e997d6a98e33a25da2ff536a2779ae173d), [b/322680547](https://issuetracker.google.com/issues/322680547))
- `GraphicsLayer.setOutline(Outline)` extension function was added. ([Ib81f4](https://android-review.googlesource.com/#/q/Ib81f4aeab09a394baf300623738555c9c9db9616))
- Introduce `GraphicsContext` function constructor to create a factory to create `GraphicsLayer` instances ([Ib98d6](https://android-review.googlesource.com/#/q/Ib98d6b140fab3d857f74faa4fa227927e1625bed), [b/288494724](https://issuetracker.google.com/issues/288494724))
- Exposed `GraphicsLayer` API to provide developer defined flexibility in capturing drawing commands that can be used to draw elsewhere and also apply different visual effects to the end result. ([I80245](https://android-review.googlesource.com/#/q/I802452c9375fc6949ed85fb65d77173456893907), [b/288494724](https://issuetracker.google.com/issues/288494724))
- Introduce the `Paragraph#getRangeForRect` which returns a range of text covered by a given rectangle area. ([Iee516](https://android-review.googlesource.com/#/q/Iee51691ed1fbc3c68bbedd000abf4ae19bc5f84e), [b/325660505](https://issuetracker.google.com/issues/325660505))
- Removed experimental override of `BasicText` with `onLinkClicked` argument. A replacement API for hyperlinks support will follow in the future. ([I107d5](https://android-review.googlesource.com/#/q/I107d5d08153db444fac816ad7c9c65057d931a81))

**Bug Fixes**

- Added `GraphicsLayer` expect/actual API definition to support capturing and replaying of drawing commands with optional compositing visual effects and transforms. Introduce `GraphicsContext` interface to contain graphics dependencies including creation and management of `GraphicsLayer` instances. ([I4a8d6](https://android-review.googlesource.com/#/q/I4a8d67d7b45798d5e8afa78402168d14512e4318), [b/288494724](https://issuetracker.google.com/issues/288494724))
- Fixed an interop issue with 1D focus search where focus would get stuck inside a `ComposeView` that was embedded among other views. ([I08fd4](https://android-review.googlesource.com/#/q/I08fd438a8b995c73d52d914786c640646e3f3d8e))

**External Contribution**

- `LocalLifecycleOwner` moved from Compose UI to `lifecycle-runtime-compose` so that its Compose-based helper APIs can be used outside of Compose UI. Thanks Jake Wharton for the contribution. ([I6c41b](https://android-review.googlesource.com/#/q/I6c41b92eb6aaab67e7d733dfe3fe0b429b46becf), [b/328263448](https://issuetracker.google.com/issues/328263448))
- Consistently expose bias float properties on all bias-based alignment subtypes. ([I69f0f](https://android-review.googlesource.com/#/q/I69f0fb6798bb99d81287d69f9a9618bc89d99ffd), [b/328088992](https://issuetracker.google.com/issues/328088992))

### Version 1.7.0-alpha04

March 6, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha04` is released. Version 1.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/ui).

**API Changes**

- Support stylus handwriting feature for BasicTextField2 on devices after Android U. ([I002e4](https://android-review.googlesource.com/#/q/I002e4f3218bb909833fcb92b8d1ff9b2153931d7))
- In this CL we are adding the `GetScrollViewportLength` semantic action so we can pipe up information about the components being scrolled in compose to the a11y system. This CL also applies the usage of said property in Foundation Scrollable Lists. ([Ic5fa2](https://android-review.googlesource.com/#/q/Ic5fa297df4613636529e12037a0b7d03bcacc534))
- `FocusRequester.createRefs` is now stable ([I4d92c](https://android-review.googlesource.com/#/q/I4d92c644c57436fcd4883bc73fe0120ffa0a6fb2), [b/261436820](https://issuetracker.google.com/issues/261436820))
- Introduced `DelegatableNode.requireView()` to allow modifier nodes to get the current Android `View` without reading a composition local. ([I40768](https://android-review.googlesource.com/#/q/I407682883cafa8315d1ede370288afdaf62d97a4))
- New API `Path.reverse()` to reverse a path's direction ([I36348](https://android-review.googlesource.com/#/q/I36348a9731a210b34cd4c177d19ef617a87d8832))
- Added `hintLocales` to `KeyboardOptions` to provide `TextFields` with the ability to hint IMEs with specific locales to preset a preferred language.
- Expose `platformLocale` property from `Locale` that returns the underlying platform object, e.g. `java.util.Locale`. ([I921c6](https://android-review.googlesource.com/#/q/I921c6c846078caddeed0cb05a027b5ae91b90c75))

### Version 1.7.0-alpha03

February 21, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/ui)

**API Changes**

- Introducing `ContextualFlowRow` and Enhanced `FlowRow`/`Column` with MaxLines and Overflow. We are excited to announce enhancements to the experimental `FlowRow` and `FlowColumn`, now featuring maxLines and overflow support, alongside the debut of `ContextualFlowRow` and `ContextualFlowColumn`. This update is designed to provide performance optimal components, where `ContextualFlow*` is perfect for a large number of items making use of a small `maxLines` config and dynamic +N see more buttons, and `FlowRow` and `FlowColumn` is perfect for a small number of items, less than 100 items. Important: To maintain existing behavior in `FlowRow` or `FlowColumn` where all items are composed regardless of if they fit the cross axis max, set `overflow` to `FlowRowOverflow.Visible` or `FlowColumnOverflow.Visible` during initialization. Explore `ContextualFlowRowSample` and `FlowRowSample` for examples of these new features in action. ([Ib9135](https://android-review.googlesource.com/#/q/Ib913509969a79ff002eafb0075e6722a7a118531), [b/293577082](https://issuetracker.google.com/issues/293577082))
- Add `maxTextLength` semantics property that should be set on text fields that filter the maximum allowed number of characters. ([I24d9f](https://android-review.googlesource.com/#/q/I24d9f6b2aa6f1e94b67847464314480dd80e8245), [b/170648072](https://issuetracker.google.com/issues/170648072))
- The `Modifier.inspectable` wrapper has been deprecated. This API will create more invalidations of your modifier than necessary, so its use is now discouraged. Developers are encouraged to implement the `inspectableProperties()` method on `ModifierNodeElement` if they would like to expose modifier properties to tooling. ([Ib3236](https://android-review.googlesource.com/#/q/Ib323690cdea8d9d4739496b95c6be7909dce7d2f))
- New constructor for `PopupProperties` which allows for full control over `WindowManager.LayoutParams` flags. ([Ibb33e](https://android-review.googlesource.com/#/q/Ibb33e49304ab4d69c15d61b3d018536a55c342aa), [b/312485503](https://issuetracker.google.com/issues/312485503))
- Introduced `DelegatableNode.requireLayoutCoordinates()` as a way to get a `Modifier.Node`'s current `LayoutCoordinates` without needing to override `onPlaced` and store the coordinates in a property yourself. ([Ia8657](https://android-review.googlesource.com/#/q/Ia86579f48f389b7bc8d8a8be25602edfded6160c))
- Introduced `DelegatableNode.currentLayoutCoordinates` as a way to get a `Modifier.Node`'s current `LayoutCoordinates` without needing to override `onPlaced` and store the coordinates in a property yourself. ([Iaebaa](https://android-review.googlesource.com/#/q/Iaebaa704ca29bb366bea5f85958fc4ddaae8be2f))
- `BasicTextField2` and related APIs under `androidx.compose.foundation.text2` package are moved to `androidx.compose.foundation.text`. ([I9f635](https://android-review.googlesource.com/#/q/I9f6355e98b573d8985af9ec5135634da58bcc597))
- Added a new `ApproachLayoutModifierNode` API to support creating custom approach logic in an explicit Modifier Node. Also added a new experimental `DeferredTargetAnimation` API for animations whose target is unknown at instantiation. ([I60745](https://android-review.googlesource.com/#/q/I60745501487754b36b0e1986bc2bc7ecbac267e8))
- New `Path` APIs to query the direction of a Path and to extract contours from a `Path`. ([I63d04](https://android-review.googlesource.com/#/q/I63d04394c6b8b395f144ea082fc2cf7810806513))
- Added `PathHitTest` and `Path.contains(Offset)` to check if a `Path` contains a specific point. ([I3b218](https://android-review.googlesource.com/#/q/I3b2186d2d3bacc037f56a1d6c2266083b78a6785))
- The `TextLayoutResult` now exposes the `getLineBaseline(lineIndex)` method. This allows to read the baseline of an arbitrary line of the text in addition to existing convenience properties `firstBaseline` and `lastBaseline`. ([Ide4e8](https://android-review.googlesource.com/#/q/Ide4e848470681364cdf7e141154d8fe5b7641eb9), [b/237428541](https://issuetracker.google.com/issues/237428541))
- Added method to compare only the annotations of two `AnnotatedStrings`. ([I32659](https://android-review.googlesource.com/#/q/I3265940a29ab587c50c96bfcbeb35590cad48100))

**Bug Fixes**

- Fixed a backwards compatibility issue with `SemanticsPropertyReceiver.performImeAction` and `SemanticsActions.PerformImeAction`. ([Id0528](https://android-review.googlesource.com/#/q/Id0528d5c5115ce4a6f703547be943a9740c22860), [b/322269946](https://issuetracker.google.com/issues/322269946))

### Version 1.7.0-alpha02

February 7, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/ui)

**API Changes**

- Fixed a binary compatibility issue with `SemanticsPropertyReceiver.performImeAction`. ([I65865](https://android-review.googlesource.com/#/q/I658657d6a697e6c5e09cb95500410bd73f237c1b), [b/322269946](https://issuetracker.google.com/issues/322269946))
- `PopupProperties` constructor that takes a `usePlatformDefaultWidth` parameter is no longer experimental. ([I8f8d2](https://android-review.googlesource.com/#/q/I8f8d20c49487798766daaa3c64b5be1d3d308c52))
- Added an overload of `ComposeTestRule.waitUntil` that takes a string description of the condition to include in the timeout message. ([I9413e](https://android-review.googlesource.com/#/q/I9413e3f91be4d9754c363d8a8a66ab0e6f72535d))
- New semantics API `unset()` to remove semantics properties that are added in the same modifier chain. New semantics property `isOpaque`. ([I8c583](https://android-review.googlesource.com/#/q/I8c583e571956d1501f4df7312a4c60edae0a1bc0), [b/317966058](https://issuetracker.google.com/issues/317966058), [b/246056649](https://issuetracker.google.com/issues/246056649))
- Removed `originalEventPosition` from copy method in public API of `PointerInputChange`. ([I7bead](https://android-review.googlesource.com/#/q/I7beadbea5ea4b5b0125b93f3ceba44006ea58f6b))

**Bug Fixes**

- Fixed an a11y bug allowing non-tabs and non-radiobuttons to be clickable when selected. ([I2181c](https://android-review.googlesource.com/#/q/I2181c38693bd70e755a7514d655ef9091eef0975))
- `VelocityTracker` will now have the fix for adding points on by default. The fix can still be turned off by setting `VelocityTrackerAddPointsFix` to false if there's any issues. ([Ib3877](https://android-review.googlesource.com/#/q/Ib3877b1f81f19899dd91e20542fa589bf6ed5399), [b/269487059](https://issuetracker.google.com/issues/269487059))
- Fixed backwards binary incompatibility in `TextStyle` and `ParagraphStyle`. ([I179f0](https://android-review.googlesource.com/#/q/I179f0ff77b3b85a05d98a28405ad936d2e9413cf), [b/320819734](https://issuetracker.google.com/issues/320819734))

**External Contribution**

- Added a new `DialogProperties` constructor without platform-specific parameters. ([I45829](https://android-review.googlesource.com/#/q/I45829f07645b4457e3f6cbdfe98b1a0d59bafdff))
- Added a new `PopupProperties` constructor without platform-specific parameters. ([I9a038](https://android-review.googlesource.com/#/q/I9a038d1fc11856fa00be98b15ae9907686e3f0e8))

### Version 1.7.0-alpha01

January 24, 2024

`androidx.compose.ui:ui-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f/compose/ui)

**API Changes**

- Expanded `ClipboardManager` by adding `ClipEntry` and `ClipMetadata` to support arbitrary content such as images.
- Adds `DeviceConfigurationOverride` API to `ui-test` to allow locally overriding the behavior of content under test, such as to specify an available size, locale, layout direction, font scale, or theme.

## Version 1.6

### Version 1.6.8

June 12, 2024

`androidx.compose.ui:ui-*:1.6.8` is released. Version 1.6.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a13a0e3b1197d66bfc19b9051576bc705f2c337..9dbbab668fd22cd643de4651197354a828aaa7b9/compose/ui).

**Bug Fixes**

- Fixed inconsistencies in font scaling when the font scale is less than the lowest defined table. In this case, we now interpolate between the linear 1x scale and the lowest defined table, so that the font size is monotonically increasing as scales increase. ([Icbae3](https://android-review.googlesource.com/#/q/Icbae34e19e771ec2f55e74badcca3b4c90d55d25))

### Version 1.6.7

May 1, 2024

`androidx.compose.ui:ui-*:1.6.7` is released. Version 1.6.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b..9a13a0e3b1197d66bfc19b9051576bc705f2c337/compose/ui).

### Version 1.6.6

April 17, 2024

`androidx.compose.ui:ui-*:1.6.6` is released. Version 1.6.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/917ada96acf0ac343128c3f4af9bd67a4b80b99c..a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b/compose/ui).

**Bug Fixes**

- Fixes a rare `BasicTextField` crash.

### Version 1.6.5

April 3, 2024

`androidx.compose.ui:ui-*:1.6.5` is released. Version 1.6.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3..917ada96acf0ac343128c3f4af9bd67a4b80b99c/compose/ui).

### Version 1.6.4

March 20, 2024

`androidx.compose.ui:ui-*:1.6.4` is released. Version 1.6.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/22b329dfa8888198eb3024650d236b3afe6c0907..1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3/compose/ui).

### Version 1.6.3

March 6, 2024

`androidx.compose.ui:ui-*:1.6.3` is released. Version 1.6.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af119e2e31de85654fb7b2e5a2c7e724231131fd..22b329dfa8888198eb3024650d236b3afe6c0907/compose/ui).

### Version 1.6.2

February 21, 2024

`androidx.compose.ui:ui-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f639ccf09a84fa5af4a9016fa239539aeed40b94..af119e2e31de85654fb7b2e5a2c7e724231131fd/compose/ui)

### Version 1.6.1

February 7, 2024
`androidx.compose.ui:ui-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..f639ccf09a84fa5af4a9016fa239539aeed40b94/compose/ui)

**Bug Fixes**

- Fixed a backwards compatibility issue with `SemanticsPropertyReceiver.performImeAction` and `SemanticsActions.PerformImeAction`. ([Ie0bb2](https://android-review.googlesource.com/#/q/Ie0bb2b112bb585f051db7348e6eaaac859d8660c), [b/322269946](https://issuetracker.google.com/issues/322269946))
- Layouts now issue an error while measuring when one returns an abnormally large size. This kind of error normally happens when the measurement uses maximum constraints directly without checking for `Constraints.Infinity`. The check will help developers find problems with the layout having the wrong size rather than in a layout that contains it. ([I339a9](https://android-review.googlesource.com/q/I339a906701f382f7e043be65de57af6b9838e695))

### Version 1.6.0

January 24, 2024

`androidx.compose.ui:ui-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/296c44d6ba03d2167bdea85d53e8387d7b1644f9..4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf/compose/ui)

### Version 1.6.0-rc01

January 10, 2024

`androidx.compose.ui:ui-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc038a4bc84de9ab20493d6efa8d26f4a70214ae..296c44d6ba03d2167bdea85d53e8387d7b1644f9/compose/ui)

**Bug Fixes**

- Optimized vector graphics implementation to improve performance by minimizing additional recompositions.

### Version 1.6.0-beta03

December 13, 2023

`androidx.compose.ui:ui-*:1.6.0-beta03` is released. [Version 1.6.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15c82aaef0f1fd0307d6c00061859e5b6c4384c6..b76585a287cbcfdae38c3e16e5acbc6e26e808e2/compose/ui)

**New Features**

- It is now possible for a `LayoutCoordinates` to be detached without the node being detached. Guard against that in the compose Layout Inspector ([If693](https://android.googlesource.com/platform/frameworks/support/+/d194e75af4fb7b01a66bd7bb2dac8ebfd5b80405))

**Bug Fixes**

- `PlatformImeOptions` is now a concrete class instead of an interface. ([If40a4](https://android-review.googlesource.com/#/q/If40a4c3e832e7852f214e18af469f5ce68e798b7))
- Fixed extra downstream recompositions caused by `LocalSoftwareKeyboardController` and `LocalTextInputService` being provided new values every time a root recomposed. ([I42190](https://android-review.googlesource.com/#/q/I421902984824a99a7d753bc3e515d8bbfd142032), [b/310510985](https://issuetracker.google.com/issues/310510985))

### Version 1.6.0-beta02

November 29, 2023

`androidx.compose.ui:ui-*:1.6.0-beta02` is released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..15c82aaef0f1fd0307d6c00061859e5b6c4384c6/compose/ui)

### Version 1.6.0-beta01

November 15, 2023

`androidx.compose.ui:ui-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose/ui)

**API Changes**

- The `DragAndDropTarget` modifier now takes in the receiving `DragAndDropTarget` explicitly and has a lambda to opt into a drag and drop session. There are now two factory functions for a `DragAndDropModifierNode`. One for receiving transfers and one for transferring data ([I69481](https://android-review.googlesource.com/#/q/I69481ca031bfa52b3f8ff910b159e3ee8f7ffaf9))
- Updated `maximumFlingVelocity` to be represented as Float. Updated documentation to be more clear about the `maximumFlingVelocity` unity. ([I8adc7](https://android-review.googlesource.com/#/q/I8adc73327ca3c0d43a9ea31d871ddae1da5e9496))
- `onDragAndDropStart` in the `DragAndDropModifierNode` factory has been renamed to `acceptDragAndDropTransfer`.`acceptsDragAndDropTransfer` has been added to the `dragAndDropTarget` Modifier to accept from a drag and drop session. This lambda returns a viable `DragAndDropTarget` if interested in a drag and drop session. Other lambdas for processing drag events have been replaced by this. a `DragAndDropTarget` factory function has been added to receive from drag and drop sessions ([Iebf3a](https://android-review.googlesource.com/#/q/Iebf3a243ad9e4515dfe43b1947ab98ade6804a99))
- Removed `DragAndDropInfo` as a type `DragAndDropModifierNode.drag` now takes parameters for the `transferData`, decoration size and drag decoration `DrawScope` lambda

  `DragAndDropTarget` has methods for particular drag and drop events instead of being a single abstract method

  `onDragAndDropEvent` in the factory function for a `DragAndDropModifierNode` has been renamed to `onDragAndDropStart` to better communicate that the `DragAndDropTarget` provided is valid for a given drag and drop session only

  The `DragAndDropEventType` has been removed ([I645b1](https://android-review.googlesource.com/#/q/I645b1531085bceef359daebf7f36aa9119f6017b))
- Renamed `PlatformTextInputModifierNode.runTextInputSession` to `establishTextInputSession`. ([I03cd0](https://android-review.googlesource.com/#/q/I03cd0d84be09a89ed7a763d1b5921cb4975b72a0))

- Improves traversable node api names to make them more understandable. ([Ia4474](https://android-review.googlesource.com/#/q/Ia4474e234f77a9e04cfeffd46e7ee6a0f05d006a))

- Replace `OriginalText` by `TextSubstitution`. ([Ifa5a8](https://android-review.googlesource.com/#/q/Ifa5a8d6a2efd776c384642d9148dbf40b23eb6e3))

- Renamed `PlatformTextInputModifierNode.textInputSession` to `runTextInputSession`. ([Ie9c6b](https://android-review.googlesource.com/#/q/Ie9c6b37420dc9c024d68bbfc94fdcbbef105a547))

- The children of `SubcomposeLayout` (and layouts like `LazyColumn` based on it) which are retained to be reused in future are considered deactivated. New `assertIsDeactivated()` test API was introduced to test such nodes. The rests of the test apis will filter out deactivated nodes by default. ([I2ef84](https://android-review.googlesource.com/#/q/I2ef84fb2ed578238bb20c07655c475df6fb8dbd0), [b/187188981](https://issuetracker.google.com/issues/187188981))

- Removed `FocusDirection.In` and `FocusDirection.Out` use `FocusDirection.Enter` and `FocusDirection.Exit` instead ([I2f660](https://android-review.googlesource.com/#/q/I2f660ded2b6e0d018eca7afa0156b9af0ff35316))

- Material `SwipeToReveal` APIs (for Cards and Chips) now rely on a slot based API (as recommended by Compose) instead of data class based instances to create those slots. This is a breaking change, please see the demo and sample code for examples on how to use the new API. ([Ia8943](https://android-review.googlesource.com/#/q/Ia89431e240b0602bfe08bceb660ff9ef1137d938))

- `FontStyle(int)` constructor is deprecated, use `FontStyle.Normal` or `FontStyle.Italic` instead. ([I66610](https://android-review.googlesource.com/#/q/I6661037ce4156041740effcc9c194eaa3c55a0c9))

- Renamed `FontScalable` interface to `FontScaling` ([Ie804a](https://android-review.googlesource.com/#/q/Ie804acee6d71ed8d8fddb6817eea74e5f40da2c6))

**Bug Fixes**

- `SoftwareKeyboardController.show()` will no longer show the software keyboard if no text editor is focused. ([I2165a](https://android-review.googlesource.com/#/q/I2165acf1b065cd56e5bfdaab31829e83292efc3c), [b/301477279](https://issuetracker.google.com/issues/301477279))
- Hardware key Up events for keys that haven't received a Down event in the same Compose View will now be ignored. ([Ib37b4](https://android-review.googlesource.com/#/q/Ib37b434b9275c1e828b980f5124956cc2ef45047), [b/305518328](https://issuetracker.google.com/issues/305518328))
- Add renderer support for Sweep Gradient in `ArcLine`. ([I4d5bb](https://android-review.googlesource.com/#/q/I4d5bb5948d2216dca2a29d2449fd97519b2b65bb))
- Implement equals and hashcode for `PageSize.Fixed`. ([Ie3ede](https://android-review.googlesource.com/#/q/Ie3edea3aafd75068cd57c04aafdd7055ead20ad7), [b/300134276](https://issuetracker.google.com/issues/300134276))
- Fix binary compatibility issue with Window Inset change ([Iee695](https://android-review.googlesource.com/#/q/Iee695f0f1b2bf24a820b5a1bccfe550d9c29a5fa))
- Remove material core layer for Material3 Chip/Button as the microbenchmarks show better performance without it. ([I55555](https://android-review.googlesource.com/#/q/I5555573520638dd3c7f0d202e048ae6fffde19e5))
- `TestDispatcher`s passed as the `effectContext` to Compose tests will now be used to create the test and frame clocks. ([Ia7178](https://android-review.googlesource.com/#/q/Ia71786a741b31b16fa092800732e8c6abcdfcaa5))

### Version 1.6.0-alpha08

October 18, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/ui)

**API Changes**

- `Modifier.dragAndDrawSource` has had the `onDrawDragShadow` lambda renamed to `drawDragDecoration` and `DragAndDropInfo` has had the size parameter renamed to `dragDecorationSize`. ([Id0e30](https://android-review.googlesource.com/#/q/Id0e3037697efad03dcf74c2c9393a733e6ab0489), [b/303904810](https://issuetracker.google.com/issues/303904810))
- Introduce `SemanticsNodeInteraction.isDisplayed()` and `SemanticsNodeInteraction.isNotDisplayed()` to check if a matched node is visible or not without also asserting on it. ([I2c196](https://android-review.googlesource.com/#/q/I2c1967befd4ae5dc2fbe324371c3039eecd5d89c), [b/302100809](https://issuetracker.google.com/issues/302100809))
- Introduced a special `Unspecified` value for `TextAlign`, `TextDirection`, `Hyphens` and `LineBreak` fields of the `ParagraphTextStyle` to replace `null`. Because these classes are inline classes, by replacing nullable with the Unspecified, we avoid primitive type boxing. Constructors, getters and other methods in `TextStyle` and Paragraph style were updated to accept the mentioned parameters as non-null types. ([I4197e](https://android-review.googlesource.com/#/q/I4197ea85db556846ecad27ca8f561955e2370951), [b/299490814](https://issuetracker.google.com/issues/299490814))
- Add `GoogleFont` overload for reading a `GoogleFont` from XML. ([If8f59](https://android-review.googlesource.com/#/q/If8f5911dde550e78bded1a8ea6a72b9e5977bac7))
- Made `LoremIpsum` `PreviewParameterProvider` an open class. ([I41bf5](https://android-review.googlesource.com/#/q/I41bf5f4e880867aea3603b3c4ea9a37c456e428d), [b/266918816](https://issuetracker.google.com/issues/266918816), [b/300116360](https://issuetracker.google.com/issues/300116360))

**Bug Fixes**

- `FontFamilyResolver` now uses `Dispatchers.Main` for cache management coroutines. ([Ie8dd9](https://android-review.googlesource.com/#/q/Ie8dd912e671a4ee49990c76f4d72adad16cc4f53))
- `AndroidViewBinding` now synchronously removes `Fragment` instances inflated by including a `FragmentContainerView` in your layout as part of its `onRelease` by using `commitNow` (instead of the `commit` it was using previously), thus fixing issues with Live Edit's method with replacing the composition upon changes. ([I58fbf](https://android-review.googlesource.com/#/q/I58fbffefb19ed896ffedc835185718a24a86949e))

### Version 1.6.0-alpha07

October 4, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..1f7407d4293384a1b91bc142880e3525048b3443/compose/ui)

**API Changes**

- Introduced `PlatformTextInputMethodTestOverride` for writing tests for custom text editors. ([Id159b](https://android-review.googlesource.com/#/q/Id159b5ddf642d02a2427950d6f5fbe71e34fdf60))
- Adds `dragAndDropSource` Modifier for starting drag and drop sessions, and `dragAndDropTarget` Modifier for receiving from drag and drop sessions. ([Ib7828](https://android-review.googlesource.com/#/q/Ib782848c37656fd704f0cb2ef42baa16a4dc4f81), [b/286038936](https://issuetracker.google.com/issues/286038936))
- Added `ColorList` and `ColorSet` collections that avoid allocations. ([I744bd](https://android-review.googlesource.com/#/q/I744bdc5040eb4153b8cb5030e66d910157b8e41c))
- Added `DisableNonLinearFontScalingInCompose` temporary flag to disable non-linear font scaling. Set `DisableNonLinearFontScalingInCompose = true` in your tests if you need time to clean them up. This flag will be removed in Compose 1.6.0-beta01. ([Ic9486](https://android-review.googlesource.com/#/q/Ic94869c0be14f0a131ebcee03cd08b9256f308ab))

**Bug Fixes**

- Optimized XML vector drawables parsing. ([Ibb015](https://android-review.googlesource.com/#/q/Ibb0150afd6730d0887d160f8486a203fedd43806))

### Version 1.6.0-alpha06

September 20, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/ui)

**API Changes**

- Additional optimizations to Material icons. ([I3e08d](https://android-review.googlesource.com/#/q/I3e08d47c8aac295f6ca660cf1d869cc7de01c9e8))
- Adds ability to traverse up/down modifier tree to find similar nodes. ([I2d234](https://android-review.googlesource.com/#/q/I2d2341d3cf02a921983b0b702f33b5bb7cf50675))
- Added `onRestoreFailed()` callback to the `focusRestorer()` modifier ([Ie1d43](https://android-review.googlesource.com/#/q/Ie1d438706b0f302ecba1c969f660359390d01450))
- Added androidx annotations to various graphics APIs to specify `ColorInt`, `FloatRange`, `IntRange`, `Size` and more. ([Id65c8](https://android-review.googlesource.com/#/q/Id65c82355bc1859fb2b3683e69606a38779654a5), [b/290950582](https://issuetracker.google.com/issues/290950582))
- Add `showSystemUi=true` to `PreviewScreenSizes` definition ([Ib61d3](https://android-review.googlesource.com/#/q/Ib61d344d83febde5be9fd2730cc79f2207ece084))

**Behavior Changes**

- Compose now uses non-linear font scaling for better readability and accessibility. When font scale \> 100% in system settings, small text will increase in size normally, but already-large text will only increase a little bit. Also, line heights defined in SP will automatically adjust to stay proportional to the 100% scale intended height. See the [Font Scaling Best Practices](https://goo.gle/font-scaling-best-practices) for more info. ([I11518](https://android-review.googlesource.com/#/q/I115181d1e91dff483c68aeb781e7cae4609e73d4))

### Version 1.6.0-alpha05

September 6, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/ui)

**API Changes**

- Enable content capture in `AndroidComposeViewAccessibilityDelegateCompat`. ([Ib2969](https://android-review.googlesource.com/#/q/Ib2969c7ca5390d6e96b0d80110b7a8895b8b02a4))
- Fling velocities in View components like `ScrollView` and `RecyclerView` are capped at `ViewConfiguration.ScaledMaximumFlingVelocity`. Compose now contains its own version of `maximumFlingVelocity` which now applies to `Draggable`. ([Ibf974](https://android-review.googlesource.com/#/q/Ibf974df663c88da673be5c549fbae31303c6ba14))
- Adds initial scaffolding to support platform drag and drop APIs. ([If84ce](https://android-review.googlesource.com/#/q/If84ce89a681b8c0b718ac4ac7ce5b55bea39f22d))
- Add `deviceId` into `RotaryScrollEvent` ([Iba3bf](https://android-review.googlesource.com/#/q/Iba3bfd50ce58c42665342519c96f3d1588770061))
- Updated `ui-tooling` Devices API to include newer devices ([Ib25b4](https://android-review.googlesource.com/#/q/Ib25b42a00369eb8f19392d0990ac51d96404c0f4))

### Version 1.6.0-alpha04

August 23, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c11630971f4f8eeb21a3691bb8a0d9fb4d31585b..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/ui)

**API Changes**

- Added a method to deactivate `ReusableComposition`, removing observations but keeping nodes in place. The deactivated composition can be activated again by calling `setContent`. ([Ib7f31](https://android-review.googlesource.com/#/q/Ib7f318c47b9e4cad19da5702ddd0ea69fc4fa827))
- Add `ReusableComposition` interface for managing lifecycle and reuse of subcompositions. ([I812d1](https://android-review.googlesource.com/#/q/I812d1fa36791857a04471882d5edabea1400c15e), [b/252846775](https://issuetracker.google.com/issues/252846775))
- `Modifier.focusGroup` has been promoted to stable APIs. ([I7ffa3](https://android-review.googlesource.com/#/q/I7ffa30d82e2e382865fcd57f5ee7640959c087e2))
- Added androidx annotations to various graphics APIs to specify `ColorInt`, `FloatRange`, `IntRange`, `Size` and more. ([I70487](https://android-review.googlesource.com/#/q/I70487409f64808e1f004e7ed05e8497fbf607a63), [b/290950582](https://issuetracker.google.com/issues/290950582))
- Updated `ColorFilter` API to have concrete subclass types for improved inspectability of parameters. ([I5fe29](https://android-review.googlesource.com/#/q/I5fe2980d3425708e8563851bbfc9a6d6d17ad261))
- Introduce wear-tooling-preview library to list valid wear devices that can be used for UI previews ([Ib036e](https://android-review.googlesource.com/#/q/Ib036edb1823884c5f9e312d6733e7c3db22f9a0a))
- Created the `FontScalable` interface to handle the font scaling part of the Density interface. ([I2cf3f](https://android-review.googlesource.com/#/q/I2cf3f4c2fd79f7ab7b12789a90c5e68b53fef56a))

### Version 1.6.0-alpha03

August 9, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/ui)

**API Changes**

- New type of enter/exit transition that scales the content based on the size of the animating container during enter \& exit animation. `LookaheadScope` Composable fun and interface are now stable. ([Ifb2ce](https://android-review.googlesource.com/#/q/Ifb2ce945db06e291aeb0980872b427bf0a580ede))
- Added support for configuring `privateImeOptions` ([Idb772](https://android-review.googlesource.com/#/q/Idb772f8091a3a415659ccb0fb58846917c8e229c))

**Bug Fixes**

- `PopupPositionProvider.calculatePosition` will now automatically update the popup's position when state read in the calculation is changed. ([I676a1](https://android-review.googlesource.com/#/q/I676a1545d580b30913ea70eae043a303bbbeba6c), [b/292257547](https://issuetracker.google.com/issues/292257547))
- Fixed text fields showing keyboard and being editable when `readOnly` is true. Also fixed the keyboard not showing when `readOnly` is changed from true to false while focused. ([I34a19](https://android-review.googlesource.com/#/q/I34a19a80d8f44b10f23db0ca0dd7b43b69311c7c), [b/246909589](https://issuetracker.google.com/issues/246909589))
- Expanded application of global assertions in UI testing. ([I1f90d](https://android-review.googlesource.com/#/q/I1f90dac386d83de184eab8fcc975ad8fcf64b4fe))

### Version 1.6.0-alpha02

July 26, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/ui)

**API Changes**

- Added a service locator interface that can be implemented by implementors of Composition that allows an implementation of Composition that delegates to another composition delegate service lookups to the original Composition. This should not be called directy and is used to enable creating experimental APIs in the runtime that can be found from wrapped versions of the composer such as the UI module does. ([I296b9](https://android-review.googlesource.com/#/q/I296b9deae0c30b70d5e37f7b5fa992d2583ef4f4))
- Completely redesigned `PlatformTextInput*` API. ([I6c93a](https://android-review.googlesource.com/#/q/I6c93a1111561b5cb55c6a34e2fc3738be3c8941d), [b/274661182](https://issuetracker.google.com/issues/274661182), [b/267235947](https://issuetracker.google.com/issues/267235947), [b/277380808](https://issuetracker.google.com/issues/277380808))
- `SoftwareKeyboardController` and `LocalSoftwareKeyboardController` are no longer experimental. `LocalSoftwareKeyboardController` is also now a proper `CompositionLocal`. ([I4c364](https://android-review.googlesource.com/#/q/I4c3647f331eacc78f15bd5aa6b19a31ff748b23d))
- `LookaheadLayout` and `LookaheadLayoutScope` have been deprecated for a few releases and are now removed. The replacement APIs are `LookaheadScope` that can work with any Layout. ([I12ac3](https://android-review.googlesource.com/#/q/I12ac3827e34339ada08c29713558950abc8db5b8))
- Added `SemanticsNodeInteraction.requestFocus` as a more convenient and discoverable way to request focus in tests. ([Ie8722](https://android-review.googlesource.com/#/q/Ie87224a465a60cd462ee0eaf7c2d3797f1d63347))
- Add experimental APIs for registering global assertions, for use by testing frameworks in the future. ([I12d77](https://android-review.googlesource.com/#/q/I12d77ee7f84cf2d6395077d6abef1eb4b634f3df))

**Bug Fixes**

- `AndroidView`'s `update` callback's first invocation will now be defered until the view is attached, instead of running when the composition that introduces the `AndroidView` is applied. This fixes a bug where the `update` callback wouldn't be invalidated if a state it read was changed immediately by an effect. ([Ie9438](https://android-review.googlesource.com/#/q/Ie94381c17c417b4161d1531c9731a3b077ad46fb), [b/291094055](https://issuetracker.google.com/issues/291094055))

### Version 1.6.0-alpha01

June 21, 2023

`androidx.compose.ui:ui-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..3b5b931546a48163444a9eddc533489fcddd7494/compose/ui)

**New Features**

- Support lookahead in `LazyList`. This allows `LazyList` in the lookahead pass to bypass any animation (e.g. item placement animation, `AnimatedVisibility`, etc) and to calculate the lookahead size and position for all children. After the lookahead pass, children of `LazyList` could animate independently to the reality as seen in the lookahead pass.

**Behavior Change: includeFontPadding is now false by default in Compose**

[`includeFontPadding`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/PlatformTextStyle#PlatformTextStyle(kotlin.Boolean)) is now false by default ([21d806](https://android-review.googlesource.com/#/q/21d806ccda067df1e0e90cb7a4ff489d7e11a71d)) in Compose.

`includeFontPadding` is a legacy attribute that controls whether or not to include extra padding on top of the first line and last line of the text to accommodate any characters that may extend above or below the text baselines.

Updating this Compose version will modify how all texts render in your UI by removing the extra padding on top of the first line and last line of every text you display.

Depending on your UI requirements and the font metrics you're using, the changes should be minimal. However you might encounter blockers such as:
- Broken screenshot tests. Fix the UI if required, and regenerate the golden images.
- Text is slightly misaligned. Remove any custom negative paddings or add padding if required.

You can opt-in to `includeFontPadding` by using `PlatformTextStyle` for each text:

    Text(
     text = myText,
     style = TextStyle(
       lineHeight = 2.5.em,
       platformStyle = PlatformTextStyle(
         includeFontPadding = true/false
       )
       /* ... */
      )
    )

You can opt-in to `includeFontPadding` for all your texts by configuring your Material styles. Note that parameter names will vary between M2 and M3.

    val Typography = Typography(
       body1 = TextStyle(
           fontFamily =    /* ... */,
           fontSize =    /* ... */,
           platformStyle = PlatformTextStyle(
               includeFontPadding = false
           )
       /* ... */
       )
    )

    MaterialTheme(
       typography = Typography,
       /* ... */
    )

You can find more about Compose `includeFontPadding` in [developer documentation](https://developer.android.com/jetpack/compose/text/style-paragraph#adjust-line-height) and [this blog post](https://medium.com/androiddevelopers/fixing-font-padding-in-compose-text-768cd232425b).

If you experience issues/bugs connected with this change, file a bug using the [issue tracker](https://issuetracker.google.com/issues/new?component=779818&template=1371638).

**API Changes**

- Support `InputConnection#requestCursorUpdates` ([I0c69b](https://android-review.googlesource.com/#/q/I0c69bf50846ad6a639fe3f3f5f77f89747035b26))
- Added `FocusRequester.saveFocusedChild` and `FocusRequester.restoreFocusedChild` ([Ic557e](https://android-review.googlesource.com/#/q/Ic557eaacc4b5c5fe9f908c5afcc86fc5e84f2bac), [b/272302679](https://issuetracker.google.com/issues/272302679), [b/275157318](https://issuetracker.google.com/issues/275157318))
- Add `ResourceResolutionException` type to wrap throwables thrown when attempting to load bitmap assets with a description of the asset path that failed to load. ([I19f44](https://android-review.googlesource.com/#/q/I19f445605ae8b171532b73b7ae4697cec0453767), [b/230166331](https://issuetracker.google.com/issues/230166331), [b/278424788](https://issuetracker.google.com/issues/278424788))
- Optimized accessibility for performance and memory allocations. ([Iede48](https://android-review.googlesource.com/#/q/Iede48198c2709b0736a39287ebc8f082d3869ae2))
- Added semantics properties and actions to support text translation. ([I4a6bc](https://android-review.googlesource.com/#/q/I4a6bc0e167389b8604135d05fbcae7b3cebab0d1))
- New property in `IntrinsincMeasureScope` and its implementations (e.g. `MeasureScope`) to indicate whether the current measure pass is a lookahead pass. ([I7a812](https://android-review.googlesource.com/#/q/I7a8122bf09752d7afb6ace1a0b397a2632708e95))
- Updated `DrawScope` api to introduce the ability to retarget rendering into a different canvas with alternative density/layoutdirection and size.
- Updated `DrawContext` to support configuration of density and layout direction as well as making the canvas configurable. ([Ie1f9b](https://android-review.googlesource.com/#/q/Ie1f9b83f0486bdaa9a159084625c79d312d7e013), [b/225408150](https://issuetracker.google.com/issues/225408150))
- Added `Paragraph#fillBoundingBoxes` to calculate character bounding boxes. ([If30ee](https://android-review.googlesource.com/#/q/If30eee7df01266200e8b41ee3a6efc141f0c781d))
- Added a set of common `MultiPreviews` ([Ia5a27](https://android-review.googlesource.com/#/q/Ia5a27a26c2282a484a91ec812a01a8d1bc1bff17))

**Bug Fixes**

- Added `FocusTargetModifierNode` interface that can be used to create a custom `FocusTarget`. ([I9790e](https://android-review.googlesource.com/#/q/I9790ef90091a66436fd7f03d0be787741b42935c))
- Renamed the `fallback*` parameters on the `TextMeasurer` constructor to `default*`. ([I940a5](https://android-review.googlesource.com/#/q/I940a5fa24ae24dd98ed854eb4b57737c9de857f5))
- Renamed `SemanticsPropertyReceiver.performImeAction` to `onImeAction` and `SemanticsActions.PerformImeAction` to `OnImeAction`. ([I8e841](https://android-review.googlesource.com/#/q/I8e841b9789b882fecf991ac2fdcfc4fcb0aaa5b7))
- Adds Wheel to differentiate a mouse scroll from a drag in nested scrolling (specifically, in `NestedScrollConnection`). ([Ie57e4](https://android-review.googlesource.com/#/q/Ie57e47dbfb69c312d49fb67297771df332a14dca))
- Added `asComposePaint` API to replace `toComposePaint` as the returned object wraps the original `android.graphics.Paint` ([I22b4c](https://android-review.googlesource.com/#/q/I22b4c3b279f05277536465f2d5d701030268420f))
- Deprecate `SemanticsProperties.imeAction` and replace with a new parameter to `SemanticsActions.performImeAction`. ([I4a587](https://android-review.googlesource.com/#/q/I4a5871554bc5614b494a0ce8a7f60e0357f629aa))
- Added support for selection by mouse. Touch based selection will expand by word, and shrink by character. ([Ic0c6c](https://android-review.googlesource.com/#/q/Ic0c6c247aefb9cf567525369468fe19fe77dc986), [b/180639271](https://issuetracker.google.com/issues/180639271))
- `Paragraph` methods that used to throw `AssertionError` for out of bounds offsets now throw `IllegalArgumentException` as `MultiParagraph` does. ([I549d3](https://android-review.googlesource.com/#/q/I549d3ec936afbd941361690d1f16fadc4998670a), [b/243338896](https://issuetracker.google.com/issues/243338896))

## Version 1.5

### Version 1.5.4

October 18, 2023

`androidx.compose.ui:ui-*:1.5.4` is released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ed495b997a532cc4cbe39abdbaa98b8fc6f3764..b6d5e6e62e40f6938bdbcfef1d6c8a79e25006f8/compose/ui)

### Version 1.5.3

October 4, 2023

`androidx.compose.ui:ui-*:1.5.3` is released. [Version 1.5.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2bc777611812ef8ef7329a332fbaf8348af05ec7..4ed495b997a532cc4cbe39abdbaa98b8fc6f3764/compose/ui)

**Bug Fixes**

- ([b/301209788](http://b/301209788)) `TextField` would sometimes incorrectly apply previous commands when focusing and inputting Korean input, leading to lost characters.

### Version 1.5.2

September 27, 2023

`androidx.compose.ui:ui-*:1.5.2` is released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a2cac855f7723e1e485c20ac68d34dc8bb68d1e..2bc777611812ef8ef7329a332fbaf8348af05ec7/compose/ui)

**Bug Fixes**

- Added workaround for crashes when accessibility scroll API was accessed from background thread.
- Fix unattached nodes being added to the semantics tree.

### Version 1.5.1

September 6, 2023

`androidx.compose.ui:ui-*:1.5.1` is released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/ui)

**Bug Fixes**

- Fixed text fields showing keyboard and being editable when `readOnly` is true. Also fixed the keyboard not showing when `readOnly` is changed from true to false while focused. ([I34a19](https://android-review.googlesource.com/#/q/I34a19a80d8f44b10f23db0ca0dd7b43b69311c7c), [b/246909589](https://issuetracker.google.com/issues/246909589))

### Version 1.5.0

August 9, 2023

`androidx.compose.ui:ui-*:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e423b92ad8e8707ff4031626131f05e33979eac8..65e3f15108d25a7e1c5c841c0855b21eca194070/compose/ui)

### Version 1.5.0-rc01

July 26, 2023

`androidx.compose.ui:ui-*:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81e6706c269471032b283755131d2aa4e8821a89..e423b92ad8e8707ff4031626131f05e33979eac8/compose/ui)

**Bug Fixes**

- Fixed crash happening when `SubcomposeLayout` is used inside `movableContentOf()`.

### Version 1.5.0-beta03

June 28, 2023

`androidx.compose.ui:ui-*:1.5.0-beta03` is released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..24dc7b0781cb908b2385ec207ca1b3a72cb90093/compose/ui)

**Bug Fixes**

- Added FocusTargetModifierNode interface that can be used to create a custom FocusTarget. ([Ifb1d6](https://android-review.googlesource.com/#/q/Ifb1d6a93af9292ec159b72513cb3f40b62c643e0))
- Fixed an issue with Dialog and Popup composables that could result in the child window not resizing as expected when `usePlatformDefaultWidth=true`. ([I112ee](https://android-review.googlesource.com/c/platform/frameworks/support/+/2616362))

### Version 1.5.0-beta02

June 7, 2023

`androidx.compose.ui:ui-*:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d26ca4055c940126ae1663ad0d54aafd23205ea4..df792c9ff86d87f538bab5d7f9dd9f56e2437b15/compose/ui)

**API Changes**

- Added `asComposePaint` API to enable consumption of an `android.graphics.Paint` instance to be used in Compose

**Bug Fixes**

- Added `asComposePaint` API to replace `toComposePaint` as the returned object wraps the original `android.graphics.Paint` ([I22b4c](https://android-review.googlesource.com/#/q/I22b4c3b279f05277536465f2d5d701030268420f))

### Version 1.5.0-beta01

May 24, 2023

`androidx.compose.ui:ui-*:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..d26ca4055c940126ae1663ad0d54aafd23205ea4/compose/ui)

**API Changes**

- Removed allocations in recomposition, color animations, and `AndroidComposeView` ([Ib2bfa](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223))
- Adds helper fun `CacheDrawModifierNode()` to allow delegation ([Icf8f9](https://android-review.googlesource.com/#/q/Icf8f9ff2800d38cd27b7bc894e8c0b26f32daf53))
- Introducing `isLookingAhead` property, accessible from `MeasureScope`, to observe lookahead results and influence main pass if desired. ([Ibf4c3](https://android-review.googlesource.com/#/q/Ibf4c31d6ecb2a7424c4d3aace7de6ea133d11e42))
- New semantics property `traversalIndex`, a float used to reorder nodes in `TalkBack` traversal (lower values come before). ([I9a81b](https://android-review.googlesource.com/#/q/I9a81b4acf33c355c1142e28e6fd94788f7937cec), [b/186443263](https://issuetracker.google.com/issues/186443263))
- Renaming the Semantics property `isContainer` to `isTraversalGroup` ([I121f6](https://android-review.googlesource.com/#/q/I121f64d7e7be332c41a1fbf10a70ef1ec14ce0dc))
- `ColorProducer` now has an `operator fun invoke` instead of `produce` ([I4a9a2](https://android-review.googlesource.com/#/q/I4a9a254d77fcb19dce8913e8a28ceb0fdf5d9f2a))
- Add `Path` transform API to apply translation/scale/rotation transformations to path objects. ([I23434](https://android-review.googlesource.com/#/q/I2343476dc71e36001febac2bcb7052fe3632dfbe), [b/233772232](https://issuetracker.google.com/issues/233772232))
- `ColorProducer`'s method is called `produce`. ([I78bde](https://android-review.googlesource.com/#/q/I78bdeea086159c81a7d8a13b6f1458b01b26624d))
- Rename `toFrameworkColorSpace` to `toAndroidColorSpace` ([I4f547](https://android-review.googlesource.com/#/q/I4f5470019d81c71afeb00a27249443efbb451aba))
- Rename `ColorLambda` to `ColorProducer`. ([I73b1a](https://android-review.googlesource.com/#/q/I73b1aa7f45542e90ff5bebe866b7d673455741ef))
- Introduce APIs to convert between Android and Compose colorspace types. ([Ie7db4](https://android-review.googlesource.com/#/q/Ie7db48f49a2233dfe4d53c65084ae068076ae648), [b/279979665](https://issuetracker.google.com/issues/279979665))
- Added a color parameter to `BasicText` to allow efficiently animating or setting text color. ([Iffd88](https://android-review.googlesource.com/#/q/Iffd88c4c2de7f6922add66b1fc46bdff8853c3f6), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Renamed `TextRange.constrain` to `TextRange.coerceIn`. ([I31be2](https://android-review.googlesource.com/#/q/I31be27760f5d7b51533c5b74d2c1c337f750f4e7))
- Added optimized `TextStyle.merge(...)` with full parameter list. ([Iad234](https://android-review.googlesource.com/#/q/Iad23419809af1c7405ba9a9d42569521e7647034), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Stabilized many Text APIs that include `Brush`, `DrawStyle`, `TextMotion`, `DrawScope.drawText`, `Paragraph.paint(Brush)`, `MultiParagraph.paint(Brush)`. ([I2f740](https://android-review.googlesource.com/#/q/I2f7409cb64ade53b1ebc3385293456b126314b14), [b/261581564](https://issuetracker.google.com/issues/261581564), [b/261581931](https://issuetracker.google.com/issues/261581931), [b/261561245](https://issuetracker.google.com/issues/261561245))
- `PlatformTextStyle.includeFontPadding` is undeprecated. Our original intent was to remove the field, however the feedback shows that developers need this configuration option. Therefore removing deprecation from the field ([I98e96](https://android-review.googlesource.com/#/q/I98e96222691d8e5d023cd22b899f0dfbae2a1e1d), [b/277703184](https://issuetracker.google.com/issues/277703184))
- Added public `TextRange.constrain` method. ([I97912](https://android-review.googlesource.com/#/q/I97912f1c1492f877bdeb9e0369e7be6f7f6a1420))
- `UrlAnnotation`s in `AnnotatedString`s can now be opened via accessibility services like `TalkBack`. ([If4d82](https://android-review.googlesource.com/#/q/If4d82999d8c62aa3718e1e681eeeaac12a9b0f55), [b/253292081](https://issuetracker.google.com/issues/253292081))
- Added the `InsertTextAtCursor` semantics action for text fields. ([I11ed5](https://android-review.googlesource.com/#/q/I11ed573be29737b234a114863c3c8f81e0fd65b1))
- `LineHeightStyle.Alignment(topRatio)` constructor is promoted to stable API. ([I79c32](https://android-review.googlesource.com/#/q/I79c3266507757bbb77c238567774ed91761c148d), [b/261565383](https://issuetracker.google.com/issues/261565383))
- `TextMeasurer` and related APIs are no longer experimental. ([I74647](https://android-review.googlesource.com/#/q/I74647908ae270be731ffa12d1599f6c9199fd904), [b/261581753](https://issuetracker.google.com/issues/261581753))
- Added the `PerformImeAction` semantics action to invoke the IME action on text editor nodes. ([Ic606f](https://android-review.googlesource.com/#/q/Ic606f69ba8860017a6d11f0f50dc0da063af0512), [b/269633506](https://issuetracker.google.com/issues/269633506))
- `PlatformTextInput` APIs are no longer experimental for Android. ([I668eb](https://android-review.googlesource.com/#/q/I668eba08bb7d2b384ab05f1ef26d490f00ae1bf8))
- value parameter name for `Enum.valueOf` changed ([Ia9b89](https://android-review.googlesource.com/#/q/Ia9b89b3c1bd0407c9beac825c49477cdfc9c1f2a))
- more thrown exceptions from enum valueOf ([I818fe](https://android-review.googlesource.com/#/q/I818fed80f3a1af1a97b5b0de7882fb2e1b99ae62))
- Introduced new low-level `PlatformTextInputAdapter` API for building custom text input implementations that talk directly to platform APIs. ([I58df4](https://android-review.googlesource.com/#/q/I58df46daa7a88f9761dcd711519c6eddf8524b6d))
- Added `BlendMode` parameter to `DrawScope.drawText`, `Paragraph.paint`, and `MultiParagraph.paint` methods to support different blending algorithms when drawing text on Canvas. ([I57508](https://android-review.googlesource.com/#/q/I57508ab06da481f63b4061ecb8ad72c3a733b0a7))
- Rename `Font.MaximumAsyncTimeout` to `Font.MaximumAsyncTimeoutMillis`. Rename only. ([I07af5](https://android-review.googlesource.com/#/q/I07af50c23dc2c2a640c6297b34b339be79e1a728))
- Updated DPI values of `@Preview` reference devices ([Id6151](https://android-review.googlesource.com/#/q/Id6151d0c71d471824fb86734e5f52f286fa72334), [b/254528382](https://issuetracker.google.com/issues/254528382))
- Add `brush`, `alpha` parameters to `BasicText` to allow efficiently animating or setting text brush.
- Define box-free lambda types for Float, Double, Long, Int, Short in :ui:ui-unit ([I6f18d](https://android-review.googlesource.com/#/q/I6f18d24248b890d7c1fd4d0a2fac1c49918b2f2b), [b/246961787](https://issuetracker.google.com/issues/246961787))

**Bug Fixes**

- Removed multiple allocations in pointer velocity tracking ([I26bae](https://android-review.googlesource.com/#/q/I26baee3d57a0ea73292c03d73479078b47f39a75))
- Reduced allocations in layout and pointer input management ([I5333a](https://android-review.googlesource.com/#/q/I5333ad0e39e5aa457e569d69672b0f3d4f2a5c40))
- Optimize Vector memory usage and first-frames rendering ([I2f3c6](https://android-review.googlesource.com/#/q/I2f3c67bf8ea1cd09c6d782f19a2dae5de73b3889))
- Removed allocations when drawing lines and points with Canvas ([I9f535](https://android-review.googlesource.com/#/q/I9f535e80238674f56bde04537c21d054b603a6b9))
- Add docs for `AndroidFont.fontVariationSettings` ([I7d9e2](https://android-review.googlesource.com/#/q/I7d9e2384d5840416d6d664d6a231bd0404619cea))

**External Contribution**

- Improved performance and reduce allocations in Vector APIs ([I906cb](https://android-review.googlesource.com/#/q/I906cb6e7d7a950b11c27f414385aa7f9c9f514aa))

### Version 1.5.0-alpha04

May 10, 2023

`androidx.compose.ui:ui-*:1.5.0-alpha04` is released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/ui)

**New Features**

- `Modifier.Node` Delegation Improvements Added an enhanced ability to delegate to other `Modifier.Node` instances from a `DelegatingNode`. This can be done with the `delegate` and `undelegate` APIs. Prior to this change, every API from the delegating node needed to be delegated explicitly to the delegated node. After this change, node interfaces will get delegated implicitly unless the `DelegatingNode` is explicitly overriding them. ([67352bc](https://android-review.googlesource.com/#/q/Icaf30a53c64b3edff6f47aae10add8378081e201))

**API Changes**

- Introduce `NestedScrollModifierNode`, a `NestedScroll Modifier.Node` that can be delegated to. ([I69513](https://android-review.googlesource.com/#/q/I69513ed2bbb1b79c24d7e965e609ed5d277a9a87))
- Added `onReset` and `onRelease` parameters to the `AndroidViewBinding` composable, mirroring the `AndroidView` composable and enabling support for View reuse with `ViewBinding`. ([I00b1e](https://android-review.googlesource.com/#/q/I00b1e2a22dde29b6e011d3d8bb1ea51391231856), [b/276802519](https://issuetracker.google.com/issues/276802519))
- Updated Compose Path API to support rewind operations to support usecases of frequent Path manipulation with faster re-use. ([I7b797](https://android-review.googlesource.com/#/q/I7b797204e20b747fb7510229a220ddf410ca1fd0))
- Added optimized `TextStyle.merge(...)` with full parameter list. ([Iad234](https://android-review.googlesource.com/#/q/Iad23419809af1c7405ba9a9d42569521e7647034), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Stabilized many Text APIs that include `Brush`, `DrawStyle`, `TextMotion`, `DrawScope.drawText`, `Paragraph.paint(Brush)`, `MultiParagraph.paint(Brush)`. ([I2f740](https://android-review.googlesource.com/#/q/I2f7409cb64ade53b1ebc3385293456b126314b14), [b/261581564](https://issuetracker.google.com/issues/261581564), [b/261581931](https://issuetracker.google.com/issues/261581931), [b/261561245](https://issuetracker.google.com/issues/261561245))
- `PlatformTextStyle.includeFontPadding` is undeprecated. Our original intent was to remove the field, however the feedback shows that developers need this configuration option. Therefore removing deprecation from the field ([I98e96](https://android-review.googlesource.com/#/q/I98e96222691d8e5d023cd22b899f0dfbae2a1e1d), [b/277703184](https://issuetracker.google.com/issues/277703184))

**Bug Fixes**

- Fixed regression where keyboard wasn't showing for text fields inside dialogs not created by the `Dialog` composable. ([I82551](https://android-review.googlesource.com/#/q/I825512cde7e41dadfc8b7491bd24190d21b14729), [b/262140644](https://issuetracker.google.com/issues/262140644))

### Version 1.5.0-alpha03

April 19, 2023

`androidx.compose.ui:ui-*:1.5.0-alpha03` is released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/compose/ui)

**New Features**

- New default behavior for `SubcomposeLayout` in `LookaheadScope`: `SubcomposeLayouts` that don't have conditional slots (e.g. `TabRow`, `Scaffold`, `BoxWithConstraints`, etc) now work nicely with lookahead animations.

**API Changes**

- New default `intermediateMeasurePolicy` that reuses measure policy from lookahead pass allows `SubcomposeLayout` subtypes without conditional slots such as `Scaffold`, `TabRow`, and `BoxWithConstraints` to work with lookahead by default. ([Id84c8](https://android-review.googlesource.com/#/q/Id84c8357e63905ea09b07acee91094489eb04402))
- The recomposer created for an Android window will now only block calls to `withFrameNanos` instead of all composition when it receives an `ON_STOP` notification. This means windows associated with stopped activites will continue to recompose for data changes but the animations, or any other caller of `withFrameNanos`, will block. ([Id9e7f](https://android-review.googlesource.com/#/q/Id9e7fe262710544a48c2e4fc5fcbf1d27bfaa1ba), [b/240975572](https://issuetracker.google.com/issues/240975572))
- Changes `motionEventSpy` to stable. ([Ic5ec4](https://android-review.googlesource.com/#/q/Ic5ec4ef446908ae7fca45c5d3c6c816b61a8029f), [b/261560988](https://issuetracker.google.com/issues/261560988))
- Added public `TextRange.constrain` method. ([I97912](https://android-review.googlesource.com/#/q/I97912f1c1492f877bdeb9e0369e7be6f7f6a1420))
- `PlatformTextStyle.includeFontPadding` is no longer deprecated to encourage developers to use this compatibility API to switch and test setting `includeFontPadding` false. ([I98e96](https://android-review.googlesource.com/#/q/I98e96222691d8e5d023cd22b899f0dfbae2a1e1d), [b/277703184](https://issuetracker.google.com/issues/277703184))

### Version 1.5.0-alpha02

April 5, 2023

`androidx.compose.ui:ui-*:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/ui)

**API Changes**

- New `SubcomposeLayout` API that takes an additional intermediate measure policy for handling measure/layout logic during lookahead-based animations. ([I017d3](https://android-review.googlesource.com/#/q/I017d37b9d3c2f890387229bc8cfc6515913c1a3a))
- PointerInput is now lazy and uses Modifier.Node for better performance ([read about the minor behavior change](https://medium.com/androiddevelopers/improvements-and-changes-to-composes-pointer-input-6026904ac972)). ([15dab9](https://android.googlesource.com/platform/frameworks/support/+/15dab9f17ec9b6b79e1a3d8324393a900019af7c))
- Changes experimental APIs to stable with Key events. ([I9c7d8](https://android-review.googlesource.com/#/q/I9c7d8b826cd7f92a06e76136441892346a495b8e), [b/261566839](https://issuetracker.google.com/issues/261566839), [b/261567368](https://issuetracker.google.com/issues/261567368))
- Changes experimental APIs to stable in `PointerInputChange`. ([I1b543](https://android-review.googlesource.com/#/q/I1b5430f6bece9ee985a2a45b820dd5e5334832ec), [b/261560988](https://issuetracker.google.com/issues/261560988), [b/261565762](https://issuetracker.google.com/issues/261565762), [b/261565749](https://issuetracker.google.com/issues/261565749))
- Adds a way to instantiate a `SuspendingPointerInputModifierNode` for more complex `Modifier.Node` implementations. ([Ic4933](https://android-review.googlesource.com/#/q/Ic493335d030a524eac7297ad620041bbc13e00d8))
- `UrlAnnotation`s in `AnnotatedString`s can now be opened via accessibility services like `TalkBack`. ([If4d82](https://android-review.googlesource.com/#/q/If4d82999d8c62aa3718e1e681eeeaac12a9b0f55), [b/253292081](https://issuetracker.google.com/issues/253292081))
- Added an API to intercept hardware keys before they are sent to the soft keyboard ([I4f4c6](https://android-review.googlesource.com/#/q/I4f4c62841c98d26c654ca34505379ac6a3aa3136), [b/186800395](https://issuetracker.google.com/issues/186800395))
- Added the `InsertTextAtCursor` semantics action for text fields. ([I11ed5](https://android-review.googlesource.com/#/q/I11ed573be29737b234a114863c3c8f81e0fd65b1))
- Text-related test actions (e.g. `performTextInput`) will now request focus directly, using the semantics action, instead of clicking on the field. ([I6ed05](https://android-review.googlesource.com/#/q/I6ed05394845155b1a7335e341ed3548a322f04f5))

**Bug Fixes**

- Text test actions now require text fields to be enabled. ([Iab328](https://android-review.googlesource.com/#/q/Iab328b75f5705a7b26778bc47998c13a0549c49c))

### Version 1.5.0-alpha01

March 22, 2023

`androidx.compose.ui:ui-*:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/ui)

**API Changes**

- Modifier.intermediateLayout now doesn't require an explicit LookaheadScope. The measure block in intermediateLayout has IntermediateMeasureScope as receiver, which provides convenient CoroutineScope, LookaheadScope and MeasureScope.([Ibe2e5](https://android-review.googlesource.com/#/q/Ibe2e5e20a833d3824213e86e5c1e155f65647ad7))
- LookaheadLayout has been replaced by LookaheadScope, which is no longer a Layout. This allows chid content in a LookaheadScope to be directly controlled by parent's MeasurePolicy. ([Ibe2e5](https://android-review.googlesource.com/#/q/Ibe2e5e20a833d3824213e86e5c1e155f65647ad7))
- Adds `Modifier.Node#coroutineScope` to allow Modifier.Nodes to launch coroutines. ([I76ef9](https://android-review.googlesource.com/#/q/I76ef9c67fb270c8d6ba4f7ccfd5379fdf7d2db69))
- Allow Modifier.Nodes to read CompositionLocals by implementing the CompositionLocalConsumerModifierNode interface. ([Ib44df](https://android-review.googlesource.com/#/q/Ib44df147ceaad520c9102c416440d20fadadc403))
- Propagation of @Deprecated class to property. ([I882d1](https://android-review.googlesource.com/#/q/I882d15d1d0d17f2227262e682d05d9dc7d082e8a))

## Version 1.4

### Version 1.4.3

May 3, 2023

`androidx.compose.ui:ui-*:1.4.3` is released. [Version 1.4.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eaef265d47319c6bebd094eb8cbfce92dd790277..d83e1a7d6afe597aed6e48be005010c7a26486dd/compose/ui)

**Bug Fixes**

- Fixed an issue where `AndroidView` may not be laid out correctly when used with certain Modifiers. ([I4dc77](https://android-review.googlesource.com/q/I4dc771beb990020ea91d6fbf83de71145a4b6382), [b/274797771](https://issuetracker.google.com/issues/274797771))
- Fixed a bug in 2D Focus Search that affected `DropDown` Menus ([b/276811828](https://issuetracker.google.com/issues/276811828))
- Fixed a bug in custom focus enter/exit properties that only ran the enter/exit block the first time the lambda was invoked ([b/277234245](https://issuetracker.google.com/issues/277234245))
- Fixed a regression in the focus system that caused a crash while reading `focusProperties`. ([b/271324781](https://issuetracker.google.com/issues/271324781), [b/274897776](https://issuetracker.google.com/issues/274897776))

### Version 1.4.2

April 19, 2023

`androidx.compose.ui:ui-*:1.4.2` is released. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5..0872f930da585f7fbf6e17c74b1dc42045e8b2c6/compose/ui)

**Bug Fixes**

- Fixed an issue where `AndroidView` would not reuse its modifiers correctly, potentially resulting in unexpected behavior and crashes. ([Ib67ee](https://android-review.googlesource.com/#/q/Ib67ee784e908b4aea5c1de061e448267b97d2349), [b/275919849](https://issuetracker.google.com/issues/275919849))
- Fixed regression where keyboard wasn't showing for text fields inside dialogs not created by the `Dialog` composable ([I82551](https://android.googlesource.com/platform/frameworks/support/+/1763fd0e7b7e11e0ac928762c2c6d16f0c049762), [b/262140644](https://issuetracker.google.com/issues/262140644))

### Version 1.4.1

April 5, 2023

`androidx.compose.ui:ui-*:1.4.1` is released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c13b30cf6683e0a43585416f30b55e07bf2b560e..5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5/compose/ui)

**Bug Fixes**

- Fixes an issue with `ParentDataModifier` not affecting `AndroidView` ([b/274797771](https://issuetracker.google.com/issues/274797771))

### Version 1.4.0

March 22, 2023

`androidx.compose.ui:ui-*:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..c5b142d6ab0494c996b2378d5008ac1cd6da75f3/compose/ui)

**Important changes since 1.3.0**

- Added a new `PinnableContainer` API that allows lazy list items to be pinned, so that they are not disposed when they are scrolled out of bounds. For example, `Modifier.focusable()` uses this mechanism to pin the currently focused item. ([Ib8881](https://android-review.googlesource.com/#/q/Ib8881191a529c9d9dc5e886570650b1987763207), [b/259274257](https://issuetracker.google.com/issues/259274257), [b/195049010](https://issuetracker.google.com/issues/195049010))
- The focus system is rewritten using the new experimental `Modifier.Node` APIs. ([I7f4d7](https://android-review.googlesource.com/#/q/I7f4d7a99aa42f7f3e4f49d034f8358a41ed42d0f), [b/247708726](https://issuetracker.google.com/issues/247708726), [b/255352203](https://issuetracker.google.com/issues/255352203), [b/253043481](https://issuetracker.google.com/issues/253043481), [b/247716483](https://issuetracker.google.com/issues/247716483), [b/254529934](https://issuetracker.google.com/issues/254529934), [b/251840112](https://issuetracker.google.com/issues/251840112), [b/251859987](https://issuetracker.google.com/issues/251859987), [b/257141589](https://issuetracker.google.com/issues/257141589))
- Added in `IsContainer` semantics property on Surfaces. This property will be used in a later change that determines traversal order based on the semantic meaning of elements such as surfaces. ([I63379](https://android-review.googlesource.com/#/q/I63379fde102abbee7d5464c50b1c86a59e01e768))
- Added a new accessibility role `DropdownList`. This can be used to replicate `TalkBack`'s behavior when focusing `android.widget.Spinner`. ([I177e5](https://android-review.googlesource.com/#/q/I177e52da7f2e3c1f9b3d6848bf08a42995b6fb6e), [b/236159001](https://issuetracker.google.com/issues/236159001))
- You can now use `PlatformTextStyle(emojiSupportMatch)` to optionally disable emoji support processing for a single Paragraph. ([Ia7100](https://android-review.googlesource.com/#/q/Ia710096395ecfe4bbd986326882331e0a7e6a74d), [b/139326806](https://issuetracker.google.com/issues/139326806))
- Android Compose UI tests will now run layout passes for each frame when executing frames to get to idle (e.g. via `waitForIdle`). This may affect tests that assert on individual frames of layout animations. ([I8ea08](https://android-review.googlesource.com/#/q/I8ea08728a395665f9ec7965579797e537b2c35e5), [b/222093277](https://issuetracker.google.com/issues/222093277))
- Added experimental `TextMotion` to `TextStyle` to define Text either to be `Static(default)` or Animated. Use `TextMotion.Animated` if Text is going to be scaled, translated, or rotated via animation. ([I24dd7](https://android-review.googlesource.com/#/q/I24dd75e606184220ed3eebc3c80f84d5c977c14c))

### Version 1.4.0-rc01

March 8, 2023

`androidx.compose.ui:ui-*:1.4.0-rc01` is released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..6022301db806601f282c53b8cbb5a981923a1589/compose/ui)

**API Changes**

- Added an overload of `AndroidView` composable function, which accepts the `onReset` param. It allows View instances to be reused when their node in the composition is discarded and reused in a compatible way. This is especially useful for `LazyRows` and `LazyColumns` of Views. ([I3f10d](https://android-review.googlesource.com/#/q/I3f10db5de1b7699964274e0d25f4aad324865dca), [b/230099236](https://issuetracker.google.com/issues/230099236))
- Introduced new low-level `PlatformTextInputAdapter` API for building custom text input implementations that talk directly to platform APIs. ([I58df4](https://android-review.googlesource.com/#/q/I58df46daa7a88f9761dcd711519c6eddf8524b6d))

**Bug Fixes**

- `BasicTextField`'s `SetText` semantics action will now update the text buffer using the same code path as IME updates and the testing functions (e.g. `performTextReplacement`).
- Text testing functions `performTextClearance`, `performTextReplacement`, and `performTextSelection` now use `SemanticsActions`. ([I0807d](https://android-review.googlesource.com/#/q/I0807d73975224ac5bf02fc232c1ab615f76c1c7d), [b/269633168](https://issuetracker.google.com/issues/269633168), [b/269624358](https://issuetracker.google.com/issues/269624358))

### Version 1.4.0-beta02

February 22, 2023

`androidx.compose.ui:ui-*:1.4.0-beta02` is released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/ui)

**API Changes**

- Removed the `modifierElementOf()` API. Please extend from `ModifierNodeElement` directly instead. ([I2256b](https://android-review.googlesource.com/#/q/I2256b1776e00cbe0b781dbd7fb483e6740cdb7bc))
- Added a new `Modifier.Node.onReset()` callback allowing you to reset some local state to properly handle the case when the `Layout` will be reused (for example as an item of `LazyColumn`). Fixed `FocusTargetModifierNode` to properly reset the focused state. ([I65495](https://android-review.googlesource.com/#/q/I65495712cdeafeb3fedc3e4272627c024f952ddb), [b/265201972](https://issuetracker.google.com/issues/265201972))
- Added `BlendMode` parameter to `DrawScope.drawText`, `Paragraph.paint`, and `MultiParagraph.paint` methods to support different blending algorithms when drawing text on Canvas. ([I57508](https://android-review.googlesource.com/#/q/I57508ab06da481f63b4061ecb8ad72c3a733b0a7))

**Bug Fixes**

- Accessibility focus order algorithm improved, for example top/bottom bars are more often read first/last respectively ([74e9c5](https://android.googlesource.com/platform/frameworks/support/+/74e9c5f21c148a8c68372c1fae290cd733dd0f46))

### Version 1.4.0-beta01

February 8, 2023

`androidx.compose.ui:ui-*:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/ui)

**API Changes**

- `PinnableContainer.PinnedHandle.unpin()` was renamed to `release()` ([I4667a](https://android-review.googlesource.com/#/q/I4667a137f47ffe29f66940c010a50b254ab9bdb2))
- Added `waitUntilNodeCount`, `waitUntilAtLeastOneExists`, `waitUntilExactlyOneExists` and `waitUntilDoesNotExist` as experimental API to `ComposeTestRule`, extending the `waitUntil` API to accept any matcher and any count of nodes. See `ComposeTestRule` for further documentation. ([Ifa1b9](https://android-review.googlesource.com/#/q/Ifa1b98cf869a78b79f082c4ed8df6c9abd302a87), [b/226934294](https://issuetracker.google.com/issues/226934294))
- Rename `Font.MaximumAsyncTimeout` to `Font.MaximumAsyncTimeoutMillis`. ([I07af5](https://android-review.googlesource.com/#/q/I07af50c23dc2c2a640c6297b34b339be79e1a728))
- Removed `GoogleFont.Provider.AllFontsListUri` and linked to it in ktdoc instead. ([I16f29](https://android-review.googlesource.com/#/q/I16f29b6aa467ee1d373f9013671e4aeff780dec8))

**Bug Fixes**

- Add docs for `AndroidFont.fontVariationSettings` ([I7d9e2](https://android-review.googlesource.com/#/q/I7d9e2384d5840416d6d664d6a231bd0404619cea))

### Version 1.4.0-alpha05

January 25, 2023

`androidx.compose.ui:ui-*:1.4.0-alpha05` is released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/ui)

**API Changes**

- Introduced new experimental overloads for the `runComposeUiTest` function and `create*ComposeRule` functions that accept `CoroutineContext` parameters. The context will be used for the test composition and any `LaunchedEffect` and `rememberCoroutineScope()` calls in the composition. ([I10614](https://android-review.googlesource.com/#/q/I10614adabdb137ad44fb51f65403866b5b184ac1), [b/265177763](https://issuetracker.google.com/issues/265177763))
- Add a new API to track 1 dimensional velocity ([If5a82](https://android-review.googlesource.com/#/q/If5a827e39ebd2dbd5cca1d62bc4af2d72ba7665c))
- `FocusRequester` is now marked as `@Stable`. ([I580ee](https://android-review.googlesource.com/#/q/I580eea627b8d899f75bfaf51d69e6a7e20c24b6a))
- Remove an experimental annotation from the `DialogProperties` constructor that takes a `usePlatformDefaultWidth` parameter. ([Ic4048](https://android-review.googlesource.com/#/q/Ic4048c78bc69694e7b33850f28a3bcb944c6df2c))
- Added function to calculation position and tangent at a distance on a path - with `PathMeasure.getPosition()` and `PathMeasure.getTangent()` ([I3b47c](https://android-review.googlesource.com/#/q/I3b47c1d016343e0a4b49051a4869f6f59a38cd5e))
- Removed accidentally exposed public setter on `PlatformParagraphStyle`. ([I07f47](https://android-review.googlesource.com/#/q/I07f477b8f105890770e0d6f4fbf272639a68aa0c))
- More type/nullability of inline/deprecated-hidden functions ([I24f91](https://android-review.googlesource.com/#/q/I24f91d55dabdd4f7ee05b8a679a4e928acc95d6d))
- Add `AnnotatedString.hasStringAnnotations` to query for annotations with zero-allocations. ([I94dfe](https://android-review.googlesource.com/#/q/I94dfec1e10e72e2fdc2eb482c74f8c058095b348), [b/246960758](https://issuetracker.google.com/issues/246960758))
- Added a new overload for `TextMeasurer.measure` function which takes in a `String` as text. ([I47b2d](https://android-review.googlesource.com/#/q/I47b2d079c61b4f63d7d985266869a76f1e8679a8), [b/242705342](https://issuetracker.google.com/issues/242705342))
- `LineBreak` and `Hyphens` APIs in TextStyle are graduated to stable. ([Ic1e1d](https://android-review.googlesource.com/#/q/Ic1e1d5f43e0601251aa3cac549cd45b7cbb70aee))

**External Contribution**

- `notifyFocusedRect` methods in `TextInputSession` and `TextInputService` are not deprecated again. ([I23a04](https://android-review.googlesource.com/#/q/I23a0425b573a644fcc114a2b60d7bbbdaf5b04ed), [b/262648050](https://issuetracker.google.com/issues/262648050))

### Version 1.4.0-alpha04

January 11, 2023

`androidx.compose.ui:ui-*:1.4.0-alpha04` is released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/ui)

**New Features**

- Added a new `PinnableContainer` API that allows lazy list items to be pinned, so that they are not disposed when they are scrolled out of bounds. For example, `Modifier.focusable()` uses this mechanism to pin the currently focused item. ([Ib8881](https://android-review.googlesource.com/#/q/Ib8881191a529c9d9dc5e886570650b1987763207), [b/259274257](https://issuetracker.google.com/issues/259274257), [b/195049010](https://issuetracker.google.com/issues/195049010))
- The focus system is rewritten using the new experimental `Modifier.Node` APIs. ([I7f4d7](https://android-review.googlesource.com/#/q/I7f4d7a99aa42f7f3e4f49d034f8358a41ed42d0f), [b/247708726](https://issuetracker.google.com/issues/247708726), [b/255352203](https://issuetracker.google.com/issues/255352203), [b/253043481](https://issuetracker.google.com/issues/253043481), [b/247716483](https://issuetracker.google.com/issues/247716483), [b/254529934](https://issuetracker.google.com/issues/254529934), [b/251840112](https://issuetracker.google.com/issues/251840112), [b/251859987](https://issuetracker.google.com/issues/251859987), [b/257141589](https://issuetracker.google.com/issues/257141589))
- Added in `IsContainer` semantics property on Surfaces. This property will be used in a later change that determines traversal order based on the semantic meaning of elements such as surfaces. ([I63379](https://android-review.googlesource.com/#/q/I63379fde102abbee7d5464c50b1c86a59e01e768))
- Added new accessibility role `DropdownList`. This can be used to replicate `TalkBack's` behavior when focusing `android.widget.Spinner`. ([I177e5](https://android-review.googlesource.com/#/q/I177e52da7f2e3c1f9b3d6848bf08a42995b6fb6e), [b/236159001](https://issuetracker.google.com/issues/236159001))
- You can now use `PlatformTextStyle(emojiSupportMatch)` to optionally disable emoji support processing for a single Paragraph. ([Ia7100](https://android-review.googlesource.com/#/q/Ia710096395ecfe4bbd986326882331e0a7e6a74d), [b/139326806](https://issuetracker.google.com/issues/139326806))
- Android Compose UI tests will now run layout passes for each frame when executing frames to get to idle (e.g. via `waitForIdle`). This may affect tests that assert on individual frames of layout animations. ([I8ea08](https://android-review.googlesource.com/#/q/I8ea08728a395665f9ec7965579797e537b2c35e5), [b/222093277](https://issuetracker.google.com/issues/222093277))
- Added experimental `TextMotion` to `TextStyle` to define Text either to be `Static(default)` or Animated. Use `TextMotion.Animated` if Text is going to be scaled, translated, or rotated via animation. ([I24dd7](https://android-review.googlesource.com/#/q/I24dd75e606184220ed3eebc3c80f84d5c977c14c))

**API Changes**

- Replaced `maxSize: IntSize` argument in `drawText` with `size: Size` to be inline with other `DrawScope` functions. `size` is set to `Size.Unspecified` by default which should not change the previous default behavior. ([Icd27d](https://android-review.googlesource.com/#/q/Icd27ddc109548e76c7bc4fba08fb9dfc174afa40))
- Removed deprecated experimental font constructor. ([I8a724](https://android-review.googlesource.com/#/q/I8a7245a0eb552b0df8c6bc9344451ccca0d2d2b1), [b/261435386](https://issuetracker.google.com/issues/261435386))
- The ui tooling data class `Group` now has a field, `isInline`, that indicates if the group is for a call to an inline composable function. If `isInline` is `true` then the call is to an inline composable function. However, the value might be false for calls to inline composable functions that are from modules that are compiled with a version of the compose compiler plugin that doesn't generate the inline function information. ([Idb846](https://android-review.googlesource.com/#/q/Idb84635d4b427de2c4636792307f7e60360a9f0a))
- Graduated a number of previously experimental APIs to stable
- Rotary Scroll Event API is now stable ([I42ad3](https://android-review.googlesource.com/#/q/I42ad3a466855a165c905dc9e965d140da7269636), [b/261561229](https://issuetracker.google.com/issues/261561229))
- `FontVariation` API is now stable ([I8779f](https://android-review.googlesource.com/#/q/I8779f6f3097b3e7f6a8596ba65d6f2b4b1d7f2ed), [b/241016309](https://issuetracker.google.com/issues/241016309))
- All `Font()` constructors are now stable API ([I5948b](https://android-review.googlesource.com/#/q/I5948b7d635d649e93a14e7b4f34ea0a05cd6c3b0), [b/261435386](https://issuetracker.google.com/issues/261435386))
- `DeviceFontFamilyName` is now stable ([I8b640](https://android-review.googlesource.com/#/q/I8b640d1d7880dcd7c581f53ff71baf2af0e80860), [b/261435386](https://issuetracker.google.com/issues/261435386))
- `AndroidFont` constructor with `variationSettings` is now a stable API, and can be used to create new types of font descriptors. ([I5adcc](https://android-review.googlesource.com/#/q/I5adcc8bd923050d20021d4725fcfe0b36f258ae1), [b/261565807](https://issuetracker.google.com/issues/261565807))
- `createFontFamilyResolver` API is now stable. This can be used to catch uncaught exceptions during async font loading. ([Ibb481](https://android-review.googlesource.com/#/q/Ibb481cae9c40a1e3ed26e7da911be24fab1788b6), [b/261435386](https://issuetracker.google.com/issues/261435386))
- `Font.loadingStrategy` API is now stable. ([I5937c](https://android-review.googlesource.com/#/q/I5937cfa2e03047eb3affd2c07fb4f75eb35faa97), [b/261435386](https://issuetracker.google.com/issues/261435386))
- `GoogleFont` API is now stable. ([Ic90b0](https://android-review.googlesource.com/#/q/Ic90b0bcd8fa3901cc56a9a58979bce25eeded283), [b/261435386](https://issuetracker.google.com/issues/261435386))
- `TextUnit(float, TextUnitType)` is now stable API. ([I90c84](https://android-review.googlesource.com/#/q/I90c84bd2043c9da0e2fcfa5b4f9fe6ee803d211f), [b/261561612](https://issuetracker.google.com/issues/261561612))
- `pluralStringResource` is now stable API. ([I09849](https://android-review.googlesource.com/#/q/I09849dc71f6203002ad466db12700c2691684e2e), [b/261439703](https://issuetracker.google.com/issues/261439703))

### Version 1.4.0-alpha03

December 7, 2022

`androidx.compose.ui:ui-*:1.4.0-alpha03` is released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/ui)

**API Changes**

- Removing `ExperimentalComposeUiApi` from `PointerIcon` ([I23af8](https://android-review.googlesource.com/#/q/I23af8c12762d9baac9864ba93e34d29709027f2a))
- Introduce Page accessibility actions: `PageUp`, `PageDown`, `PageLeft`, `PageRight`. Note that these are only available from API 29. ([Ida4ab](https://android-review.googlesource.com/#/q/Ida4ab069a2c7f8d2fc06bf20555c611f4a360728))
- Updated `rememberNestedScrollConnection` parameter view from root view to host view. ([Ia5200](https://android-review.googlesource.com/#/q/Ia520073cedb35bffefd54f05bbac186c48521802))
- Added an Modifier API to query ancestors scroll info. ([I2ba9d](https://android-review.googlesource.com/#/q/I2ba9d6d55f853e5d2775fe9a9f15e7a41d41e359), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Used in `Clickable` to correctly delay press interactions, when gestures could become scroll events.
- Fixed `Clickables` not correctly delaying ripples, when used inside an `Scrollable ViewGroup`.
- Updated Drawers and Sheets to correctly delay presses in case gestures can become scroll events.
- Renamed `CompositingStrategy.Always` to `Offscreen` to indicate that the `graphicsLayer` will always be rendered into an intermediate buffer ([I47dc1](https://android-review.googlesource.com/#/q/I47dc13a167f51d98e9a46ca9bc57209e43a5b18a))
- Layout overload with multiple content slots is now stable ([I10566](https://android-review.googlesource.com/#/q/I105661f5ff4127215110cfb53fa437e444088f79), [b/248294649](https://issuetracker.google.com/issues/248294649))
- Added experimental new APIs `PerfettoTrace.record {}` and `PerfettoTraceRule` to capture Perfetto traces (also known as System Traces) as part of a test, to inspect test behavior and performance. ([I3ba16](https://android-review.googlesource.com/#/q/I3ba165beded0d8aabde791e3ac1b786d415404ed))
- In UI tests using a Compose rule, continuations resumed during `withFrameNanos` callbacks will not be dispatched until after all frame callbacks have finished running. This matches the behavior of compose when running normally. However, tests that rely on the old behavior may fail. This should only affect code that calls `withFrameNanos` or `withFrameMillis` directly, and has logic outside of callback passed to those functions that may need to be moved inside the callbacks. See the animation test changes in this CL for examples.
- Added optional `onPerformTraversals: (Long) -> Unit` parameter to `TestMonotonicFrameClock` constructor and factory function to run code after `withFrameNanos` callbacks but before resuming callers' coroutines. ([Idb413](https://android-review.googlesource.com/#/q/Idb41309445a030c91e8e4ae05daa9642b450505c), [b/254115946](https://issuetracker.google.com/issues/254115946), [b/222093277](https://issuetracker.google.com/issues/222093277), [b/255802670](https://issuetracker.google.com/issues/255802670))
- Added EmojiCompat to Compose ([Ibf6f9](https://android-review.googlesource.com/#/q/Ibf6f9f9d37c6280fe1b051269b127f0dfb1d6b6a), [b/139326806](https://issuetracker.google.com/issues/139326806))
- Added new wallpaper parameter to `@Preview` for dynamic colour support ([I9f512](https://android-review.googlesource.com/#/q/I9f512178c957f6a70f92116ce3dd5394f74131dd))

**Bug Fixes**

- Snapshot apply notifications are now sent after the `Recomposer` finishes applying changes. ([Iad6c0](https://android-review.googlesource.com/#/q/Iad6c0dcd163a5a8f9c5aec426da3d4f701ca509f), [b/222093277](https://issuetracker.google.com/issues/222093277))
- Introduced changes in `captureToImage` to allow for capturing multi window screenshots. This is useful for screenshot tests that use compose PopUps. ([I169c5](https://android-review.googlesource.com/#/q/I169c594f68e20939c98e8ebe0961625140177754))

**Dependency Updates**

- Compose UI and Compose Material now depend on Lifecycle 2.5.1. ([I05ab0](https://android-review.googlesource.com/#/q/I05ab08e48f49eee1a1e573d172ba22efc47640a6), [b/258038814](https://issuetracker.google.com/issues/258038814))

### Version 1.4.0-alpha02

November 9, 2022

`androidx.compose.ui:ui-*:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/ui)

**API Changes**

- Updated `GraphicsLayerScope` to expose the current size of the `graphicsLayer`. This is useful for computing `graphicsLayer` transformations as a function of the Composable size. ([If8c43](https://android-review.googlesource.com/#/q/If8c43dad95441ba7cc7ddc845bfa502cce688c7b),[b/181387080](https://issuetracker.google.com/issues/181387080))
- Introduced `CompositingStrategy` to determine when to leverage an offscreen compositing layer for rendering of `graphicsLayer` content. Auto maintains the default behavior which internally leverages a layer if alpha is applied or a `RenderEffect/Overscroll`. Always will always introduce an offscreen buffer where `ModulateAlpha` will avoid leveraging an offscreen buffer and instead will modulate each of the recorded drawing instructions within the `graphicsLayer`. `ModulateAlpha` usage will still leverage an offscreen buffer for `RenderEffect/Overscroll` usages ([I25e82](https://android-review.googlesource.com/#/q/I25e82c7d302e2ffd9353373595a72b8b10627a37), [b/256382834](https://issuetracker.google.com/issues/256382834))
- `invalidateSubtree()` was added to `Modifier.Node` to allow invalidating entire hierarchies for layout and drawing. ([I4bd90](https://android-review.googlesource.com/#/q/I4bd90727827d98f95f4ae4db9032a79dbba2fa33))
- Promote `rememberNestedScrollInteropConnection` to stable. Introduced the ability to pass a root view to `rememberNestedScrollInteropConnection`. This can help the custom view better react to scrolling constraints, specially in non-standard views (e.g. `ModalBottomSheetDialog`). ([I9e107](https://android-review.googlesource.com/#/q/I9e10769a50354aad1decadaa80152a3814c4480e))
- Added `ObserverNode` interface that can be used by `Modifier.Node` implementations that need to be notified when a value that they had previously read has changed ([I5728b](https://android-review.googlesource.com/#/q/I5728be00aad7c3fb9e44240c257f4d45a081da6f), [b/247716483](https://issuetracker.google.com/issues/247716483))
- Added a new constructor to `Paint` that accepts a native `android.graphics.Paint`. Also added an extension function `toComposePaint()` that converts an existing native Paint object to Compose Paint. ([Ica91b](https://android-review.googlesource.com/#/q/Ica91bfd4d1e2215cb0778c173c02f06c3f23fd9d))
- Add new `FontFamily.Resolver.resolveAsTypeface` for use on Android. ([I8950b](https://android-review.googlesource.com/#/q/I8950b91fc2a4edd52c66626c708c413e6d799dfd))
- Add `ToolingState` to allow tooling to change internal states of Composable ([Ie6614](https://android-review.googlesource.com/#/q/Ie66147788cfde7ede84a94d9591b3a05c51209cb))
- Refactor tooling to have better support for new added animations ([I8677b](https://android-review.googlesource.com/#/q/I8677b632c114f596a49e2a8d86a16f150feccd6a))
- Added `minLines` parameter into material and material3 Text, `TextField` and `OutlinedTextField` which allows setting the minimum height of the component in terms of number of lines ([I4af1d](https://android-review.googlesource.com/#/q/I4af1df6521acaa97edbed5048079b5e81b647dd8))

### Version 1.4.0-alpha01

October 24, 2022

`androidx.compose.ui:ui-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..548c8ac2570ae6cf15798fea1380491f7d93796b/compose/ui)

**API Changes**

- A new method, `awaitEachGesture()`, for gesture detectors was added. It operates similar to `forEachGesture()`, but the loop over gestures operates entirely within the `AwaitPointerEventScope` so events can't be lost between iterations.
- `forEachGesture()` has been deprecated in favor of `awaitEachGesture()` because it allows events to be lost between gestures. ([Iffc3f](https://android-review.googlesource.com/#/q/Iffc3fb8cf53d0e5eb9b529c023b3e2d29003e86f), [b/251260206](https://issuetracker.google.com/issues/251260206))
- Deprecating recycling of acccessibility objects in androidx. We've found performance changes to be negligible in even the oldest supported versions. ([I0a961](https://android-review.googlesource.com/#/q/I0a961c85c260b1e8dd97826d0b32c0bdcb51fcfe))
- Added `DrawStyle` as an Experimental attribute to `TextStyle` and `SpanStyle` to enable drawing outlined text. ([If24b8](https://android-review.googlesource.com/#/q/If24b8510daa597283c9f4d39c590747ebd822d69), [b/155421273](https://issuetracker.google.com/issues/155421273))
- `AnnotatedString.Builder` now implements `kotlin.text.Appendable`. ([I1a061](https://android-review.googlesource.com/#/q/I1a061f42c46b21f00320b5b31fa717b8d57fd919), [b/231030444](https://issuetracker.google.com/issues/231030444))
- `AnnotatedString.Builder` now has an `append(AnnotatedString, start: Int, end: Int)` method to append a substring of an `AnnotatedString` and the intersecting styles.
- Added `DrawStyle` parameter to `Paragraph` and `MultiParagraph` paint functions that enables drawing outlined text. ([Ic8102](https://android-review.googlesource.com/#/q/Ic8102680bd95cd65f03bac4f3b866e3df637cacf), [b/155421273](https://issuetracker.google.com/issues/155421273))

**External Contribution**

- Thanks for `vighnesh` for adding TV Devices to Previews ([Ie15cd](https://android-review.googlesource.com/#/q/Ie15cdcac3aad5c3d191d0ef9a096784549d0460f))

## Version 1.3

### Version 1.3.3

January 11, 2023

`androidx.compose.ui:ui-*:1.3.3` is released. [Version 1.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8476d588d4975cb86be01bf4e356c5605ad89d48..59e93356f8f2bfb40b6f56dc086c8b821bbebda6/compose/ui)

**Bug Fixes**

- Fix for a crash sometimes happening on Android 9 when Activity is saving the state of the Compose View. ([I0b755](https://android-review.googlesource.com/q/I0b755a3d6a164b6c26aa592e13e206dc45cd5dd9), [b/260322832](https://issuetracker.google.com/260322832))

### Version 1.3.2

December 7, 2022

`androidx.compose.ui:ui-*:1.3.2` is released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d29f2a87e3c1d5cb6dfde828400d67b6f161be63..8476d588d4975cb86be01bf4e356c5605ad89d48/compose/ui)

**Bug Fixes**

- Updated to use Profobuf 3.21.8, which avoids a security alert in `protobuf-javalite:3.19.4` (CVE-2022-3171) ([b/255545055](https://issuetracker.google.com/255545055))

### Version 1.3.1

November 9, 2022

`androidx.compose.ui:ui-*:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/ui)

### Version 1.3.0

October 24, 2022

`androidx.compose.ui:ui-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/ui)

**Important changes since 1.2.0**

- New experimental API suite [`LookaheadLayout`](https://android-review.googlesource.com/c/platform/frameworks/support/+/1961800) (enabling previously impossible animation behaviors)
- New experimental API suite [`Modifier.Node`](https://developer.android.com/jetpack/androidx/releases/(/jetpack/androidx/releases/compose-ui#1.3.0-beta01)) (higher-performance alternative to `Modifier.composed`)
- Improved window insets support.
- Focus support for D-Pads and hardware keyboard in LazyLists.
- Maximum supported elevation in dialogs and popups has been reduced to 8dp (behavior breaking change for some customized design systems -- [rationale in beta01 release notes](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.3.0-beta01))
- Many [minor, nonbreaking API improvements](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.3.0-alpha03)
- Many bugfixes and performance improvements

### Version 1.3.0-rc01

October 5, 2022

`androidx.compose.ui:ui-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/ui)

**API Changes**

- Added new experimental API Hyphens to support automatic hyphenation in Text ([Iaa869](https://android-review.googlesource.com/#/q/Iaa869b15b0cf6d9b4f4ab87ddf687c2388b886e8))

**Bug Fixes**

- `DeviceFontFamilyName` fonts will not configure `wght` and `ital` variation settings by default, instead using platform setting for loaded `Typeface`. ([Ia7a6d](https://android-review.googlesource.com/#/q/Ia7a6db95a402e7528d977ec67b4ed3992bdb7a5d), [b/246989332](https://issuetracker.google.com/issues/246989332))
- Fixed `LazyColumn` memory leak - `onModifierLocalsUpdated` was not being called with the default value when modifiers were reused ([b/230168389](https://issuetracker.google.com/issues/230168389))

### Version 1.3.0-beta03

September 21, 2022

`androidx.compose.ui:ui-*:1.3.0-beta03` is released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/ui)

**API Changes**

- Add options to customize line breaking in Text. ([I86907](https://android-review.googlesource.com/#/q/I8690771e479fd832dcd991a234c49bfcca1beaa0))
- Changed `size:IntSize` argument with `constraints: Constraints` in `TextMeasurer.measure` method to support minimum width constraints. ([I37530](https://android-review.googlesource.com/#/q/I37530a2f80f5a2226c6e155985491b824f08a0c0), [b/242707525](https://issuetracker.google.com/issues/242707525))

**Bug Fixes**

- AndroidX Activity's `BackHandler` API now works within a `Dialog` composable. ([I35342](https://android-review.googlesource.com/#/q/I3534219bb887fdc6c46c659a1b1f1465d2c8aa7d))

### Version 1.3.0-beta02

September 7, 2022

`androidx.compose.ui:ui-*:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/ui)

**API Changes**

- Added an experimental overload for Layout which accepts a list of multiple composable content lambdas, which allows to threat measurables put into different content lambdas differently ([Ic1b4e](https://android-review.googlesource.com/#/q/Ic1b4e8987173aa7f0a18341014079fb41a664ff0))

**Changes to experimental Focus APIs:**

- `FocusDirection.In` and `FocusDirection.Out` are deprecated and replaced by `FocusDirection.Enter` and `FocusDirection.Exit`. ([Ia4262](https://android-review.googlesource.com/#/q/Ia4262d2f8edc3ec36d2edc9ed2858895971ba33c), [b/183746982](https://issuetracker.google.com/issues/183746982))
- Added two new focus properties enter and exit to specify a custom behavior for `FocusManager.moveFocus(Enter)` and `FocusManager.moveFocus(Exit)`. ([I5f3f9](https://android-review.googlesource.com/#/q/I5f3f9e1c20494f3ee0d6484854c3d50485422ba3), [b/183746982](https://issuetracker.google.com/issues/183746982))
- You can now use `FocusRequester.Cancel` to cancel a focus move. `FocusRequester.Cancel` can be used in any of the following focus properties: up, down, left, right, next, previous, start, end, enter and exit. ([Ib300f](https://android-review.googlesource.com/#/q/Ib300fdd5738f7868f541b0bbfe209421bf9e0889))

### Version 1.3.0-beta01

August 24, 2022

`androidx.compose.ui:ui-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/ui)

**Modifier Node Refactor**

The layer which handles `Modifier/Modifier.Element` instances and coordinates their behavior on `LayoutNodes` has been majorly refactored. As it stands this was a refactor which did not affect the public API of any of the many modifiers in Compose, and can be viewed as an implementation-only change. Despite that, this is an important change for various reasons. ([Ie4313](https://android-review.googlesource.com/#/q/Ie4313071d4d9ebc82b28b6fbb691d3736d7d738a))

***Change Summary***

The added experimental `Modifier.Node` APIs provide an abstraction that allows for state to be maintained on an instance that will be retained with the lifecycle of the layout node, and will be allocated per-layout-node and per-usage of the corresponding `Modifier.Element` that produced it.

Broadly speaking, this abstraction provides an alternative mechanism to produce stateful modifiers without relying on the mechanics of the `Modifier.composed` API.

***Risk***

This change is strictly binary compatible with prior releases, and is intended to be backwards compatible in terms of observable behavior as much as practical and reasonable. That said, there are few subsystems of compose this refactor did not touch, and *it is likely that behavior has changed in ways that were not covered by our tests and have not yet been found and fixed*.

Please upgrade to this release with caution. If you believe this has broken something for you, please let us know.

***Experimental APIs***

Various experimental APIs have been added, all relating to the new concept of a "Modifier Node". Modifier.Node's are created as a result of

- `fun modifierElementOf(...): Modifier`
- `abstract class ModifierNodeElement`
- `abstract class Modifier.Node`
- `abstract class DelegatingNode`
- `interface LayoutModifierNode`
- `interface DrawModifierNode`
- `interface SemanticsNode`
- `interface PointerInputNode`
- `interface ModifierLocalNode`
- `interface ParentDataModifierNode`
- `interface LayoutAwareModifierNode`
- `interface GlobalPositionAwareModifierNode`
- `interface IntermediateLayoutModifierNode`

**Behavior breaking change**

Maximum supported elevation in dialogs and popups has been reduced to 8dp.

The maximum supported elevation for Compose dialogs and popups has been reduced from 30dp to 8dp. This change affects both material and ui custom dialogs and popups. This change is made to mitigate an accessibility bug on Android versions below S, and to ensure that accessibility services within those windows are able to interact with the content inside the dialog or popup.

You will only be impacted by this change if you are creating a custom dialog or popup implementation with an elevation set to levels higher than 8dp. Consider lowering the elevation of your dialog or popup. If you need to opt-out from this new behavior, consider forking your own dialog or popup with the desired elevation set. This is not recommended, as accessibility might be negatively impacted and it is on the developer to ensure the bottom part of the dialog or popup is interactable and readable by accessibility services.

**API Changes**

- Fixed an issue where `painterResource` wouldn't update on configuration changes ([I58e73](https://android-review.googlesource.com/#/q/I58e732cd43766d41a7f8f732c6bf519548a695d7), [b/228862715](https://issuetracker.google.com/issues/228862715))
- `rememberTextMeasurer` no longer takes `FontFamily.Resolver`, `Density`, or `LayoutDirection` parameters. Please use the `TextMeasurer` constructor to provide custom values for these parameters. ([Ia1da3](https://android-review.googlesource.com/#/q/Ia1da39bdd839b3a26ccc848806c241c923604438))
- Added `DialogProperties.decorFitsSystemWindows` property to allow Dialogs to support `WindowInsets`. ([I57742](https://android-review.googlesource.com/#/q/I577429919e87610107d6fd476538d8904866b5ce), [b/229378542](https://issuetracker.google.com/issues/229378542))
- Moved font constructors back to original kotlin file to retain binary compatibility. No change from last stable release. ([Ieb2f3](https://android-review.googlesource.com/#/q/Ieb2f3f5b9bff8000520a6e6ecb44c187abfd727c))
- Removed unnecessary operator from several equals definitions - this has no effect. ([I6c309](https://android-review.googlesource.com/#/q/I6c309cccd358bc76c82e7cd9e88e8a8bdf705c95))
- `FontVariation.Setting` is a sealed interface, to allow future clamping APIs. ([I11021](https://android-review.googlesource.com/#/q/I110218032f9128790bf2b27ac19cfafb057e37ce), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Add `CompositionGroup.findParameters` to `SlotTree.kt`. This allows tools to retrieve parameters for a `CompositionGroup` without having to parse the entire slot table. ([I124fe](https://android-review.googlesource.com/#/q/I124fee0869556b869a1ed2ee2ce1d90014d1c58e))

### Version 1.3.0-alpha03

August 10, 2022

`androidx.compose.ui:ui-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/ui)

**API Changes**

- `LayoutCoordinates.findRootCoordinates()` is now public ([I7fa37](https://android-review.googlesource.com/#/q/I7fa371019044fef3c3451c4b628f81425dd01140), [b/204723384](https://issuetracker.google.com/issues/204723384))
- Added experimental API to get the `LayoutCoordinates` in the `PlacementScope`. This lets developers know where the current layout is to place children relative to its position. ([I5482b](https://android-review.googlesource.com/#/q/I5482bf4604e700d9f5a753142fe0db3f306939fd), [b/238632578](https://issuetracker.google.com/issues/238632578))
- Added `LayoutCoordinates.transformFrom` to get the Matrix transformation from one `LayoutCoordinates` to another. ([Ic5ab1](https://android-review.googlesource.com/#/q/Ic5ab114e2fb6453c062e1450982081e18d190f9d), [b/238632578](https://issuetracker.google.com/issues/238632578))
- Deprecated `SemanticsModifier.id` and moved the semantics id to `LayoutInfo.semanticsId` instead. ([Iac808](https://android-review.googlesource.com/#/q/Iac808fc0e3ff14f1c1a95ee3f1f24cd436245a0e), [b/203559524](https://issuetracker.google.com/issues/203559524))
- Resource Fonts now support setting font variation settings (API 26+). ([I900dd](https://android-review.googlesource.com/#/q/I900dde1f539e580a66db9c14d389ada691377c91), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Variable font support in `DeviceFontFamilyNameFont` ([Ic1279](https://android-review.googlesource.com/#/q/Ic1279b2dcb1c29e75b8037791179853a9f828c02), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Font constructors now accept a list of `FontVariation.Setting` for configuring variable fonts on O+ devices. ([I11a9d](https://android-review.googlesource.com/#/q/I11a9d69d73429e9a875fd7096a00981a0cbd8a47), [b/143703328](https://issuetracker.google.com/issues/143703328))
- Add `FontVariation` API for defining and using variable fonts. ([I3c40c](https://android-review.googlesource.com/#/q/I3c40c6c8b4cee02cacda9482955ec16587ae62a5), [b/143703328](https://issuetracker.google.com/issues/143703328))
- `LineHeightStyle.Alignment` constructor is now public (experimental) ([I4bbbe](https://android-review.googlesource.com/#/q/I4bbbe53b2088b9b211b86919c55bf6be88572baf), [b/235876330](https://issuetracker.google.com/issues/235876330))
- Paragraph is now expect\|actual and defined for Android and Desktop. ([Id387e](https://android-review.googlesource.com/#/q/Id387e52c4509ebcfd78e9b57b09a0ee8cd51b11f), [b/239962983](https://issuetracker.google.com/issues/239962983))
- Interface Paragraph is now sealed interface Paragarph. There is no use case for subclassing paragraph, and we recommend reaching out if this change impacts you. ([If5247](https://android-review.googlesource.com/#/q/If52470dbc601b83f41b49a7bd1e28c57b5e353d1), [b/239962983](https://issuetracker.google.com/issues/239962983))
- Removed experimental annotation from `PlatformTextStyle` and `LineHeightStyle`. ([I64bef](https://android-review.googlesource.com/#/q/I64bef65f524025ac386bf0cf0d362eb7ac9a7352))
- Deprecate `TextInputService.show|hideSoftwareKeyboard`. Please use `SoftwareKeyboardController` instead in app code and `TextInputSession` in IME-management code. ([I14e4c](https://android-review.googlesource.com/#/q/I14e4cb6e685dd9a0a172797d8d3f363446aeb89d), [b/183448615](https://issuetracker.google.com/issues/183448615))
- Add new API for existing animation types ([I26179](https://android-review.googlesource.com/#/q/I261797ae35be7a2199cf1d3412d832570b4618b5))

**Bug Fixes**

- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631), [b/238790278](https://issuetracker.google.com/issues/238790278))

### Version 1.3.0-alpha02

July 27, 2022

`androidx.compose.ui:ui-*:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/ui)

**API Changes**

- Added a new property `PointerInputChange#pressure` to retrieve the pressure. ([I45a5e](https://android-review.googlesource.com/#/q/I45a5e8a0097064b01bba449df9e1d455a82e696c), [b/205164819](https://issuetracker.google.com/issues/205164819))
- Added `rememberTextMeasurer` to easily create and remember `TextMeasurer` instances in composition. ([I8d66e](https://android-review.googlesource.com/#/q/I8d66e8064e6ee4779270ba81f06c501815a725f7))
- `Rect`, `RoundRect`, and `MutableRect` now support the Kotlin `in` syntax for calling the `contains` function. ([Ie42b0](https://android-review.googlesource.com/#/q/Ie42b063455800b15524996628a4d6c94d4596ce8), [b/238642990](https://issuetracker.google.com/issues/238642990))
- Remove unnecessary functions from `KeyInjectionScope`, as they can be easily implemented with simpler parts of the API. The functions that have been removed include `pressKeys`, `keysDown` and `keysUp`. ([I81d77](https://android-review.googlesource.com/#/q/I81d7787f740184789e1b6d886a424ffffbcf1f1b))
- Refactored constant and parameter names in `KeyInjectionScope` to include the suffix 'Millis' where the units of said constants and parameters are milliseconds. ([Iabef5](https://android-review.googlesource.com/#/q/Iabef5a81de7d38e2e1bb9de01e94fd69f933e7a1))
- Added `toStringForLog()` method to `EditCommand` to help troubleshoot text editing issues. ([I53354](https://android-review.googlesource.com/#/q/I53354b781acb7c000c57a293aaf8bc030ac0e484), [b/228862731](https://issuetracker.google.com/issues/228862731))
- Added `drawText` extension function on `DrawScope` to provide a way to draw multi-styled text on composables and modifiers that operate on a `DrawScope` like `Canvas` and `drawBehind`. ([I16a62](https://android-review.googlesource.com/#/q/I16a6226ae83d879f2c493fb811f1ecef77a1fc15), [b/190787898](https://issuetracker.google.com/issues/190787898))
- Introduce a new experimental API called `TextMeasurer` that enables arbitrary text layout computation that creates identical results to `BasicText`, independent from Compose runtime. ([I17101](https://android-review.googlesource.com/#/q/I1710117775b135a2e2a01361758aa96c2c5193cc))
- Add `mapTree` to `SlotTree.kt`. This allows tools to inspect the `SlotTree` without making an in memory copy first like asTree does. For the Layout Inspector this gives a performance improvement of about a factor 10. ([I5e113](https://android-review.googlesource.com/#/q/I5e1135269ea35b617616aa03e58296765b291deb))
- Changed Compose Preview to be stored in binary output files, in order to allow developers to write and reuse `MultiPreview` annotations from libraries. ([I85699](https://android-review.googlesource.com/#/q/I856993ed3f4568f62130cfbd92ebb451ec897c24), [b/233511976](https://issuetracker.google.com/issues/233511976))

**Bug Fixes**

- When adding `InputEventChange` events to `Velocity` Tracker we will consider now deltas instead of positions, this will guarantee the velocity is correctly calculated for all cases even if the target element moves ([Icea9d](https://android-review.googlesource.com/#/q/Icea9d76a43643a6b17da11f3c539d27cb8fa6f6e), [b/216582726](https://issuetracker.google.com/issues/216582726), [b/223440806](https://issuetracker.google.com/issues/223440806), [b/227709803](https://issuetracker.google.com/issues/227709803))
- Fix NPE caused by `AnnotatedString.toUpperCase` when annotations are present. ([I0aca2](https://android-review.googlesource.com/#/q/I0aca2865d1137bc375b2548eac039112294a62fb), [b/210899140](https://issuetracker.google.com/issues/210899140))

### Version 1.3.0-alpha01

June 29, 2022

`androidx.compose.ui:ui-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..8094b683499b4098092c01028b55a38b49e357f2/compose/ui)

**API Changes**

- New `LookaheadLayout` that supports a lookahead pass before the actual measure/layout. This allows a pre-calculation of the layout when it changes, while permitting the post-lookahead measure/layout to use the pre-calculated size/position to animate the size and positions towards the target. `SubcomposeLayouts` are not yet supported, but will be in an upcoming release. ([I477f5](https://android-review.googlesource.com/#/q/I477f57d1f9efeb0aafd9fb509a2cac0ad8edfaf8))
- Add optional alpha parameter to Brush flavor of `TextStyle` and `SpanStyle` to modify opacity of the whole `Text`. ([Ic2fac](https://android-review.googlesource.com/#/q/Ic2facdfe451f6e0ec3d2961fb623ef30e4742e31), [b/234117635](https://issuetracker.google.com/issues/234117635))
- Introduced the `UrlAnnotation` annotation type and associated methods to support `TalkBack` link support in `AnnotatedString`s. ([I1c754](https://android-review.googlesource.com/#/q/I1c754dfa0ce88a36989888b43816333dfc94b0aa), [b/231495122](https://issuetracker.google.com/issues/231495122))
- Moving utility functionality to runtime ([I4f729](https://android-review.googlesource.com/#/q/I4f729ac5919a71218d89e8892ab9d96b8c76aa96))

**Bug Fixes**

- `TextLayoutResult.getLineForOffset` does not throw. ([Idc5d6](https://android-review.googlesource.com/#/q/Idc5d6d0721a0241b9992db60d0ddcf3fcc52ed44), [b/235876324](https://issuetracker.google.com/issues/235876324))

**External Contribution**

- Added a new API `WindowInfo.keyboardModifiers` to observe its state within composable functions or via snapshotFlow ([Icdb8a](https://android-review.googlesource.com/#/q/Icdb8a0e53f5adb436662bc62c620543e77029f1a))

## Version 1.2

### Version 1.2.1

August 10, 2022

`androidx.compose.ui:ui-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255/compose/ui)

**Bug Fixes**

- Fixed nullpointer in the inspector ([b/237987764](https://issuetracker.google.com/237987764))
- Fixed class cast exception during remember in the inspector ([b/235526153](https://issuetracker.google.com/235526153))

### Version 1.2.0

July 27, 2022

`androidx.compose.ui:ui-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ff668d1061ec9e732d65ec3bfa9dc3db50fd87a..1e0793130863c72dc4a2d02bc975128f3ef0158b/compose/ui)

**Important changes since 1.1.0**

- Improvements in focus traversal:

  - Focus-driven-scrolling of Lazy lists now works, using the new `BeyondBoundsLayout` core API
  - New behavior customization APIs in `FocusOrder` and `FocusProperties`
  - Improved behavior with physical keyboard or TV remote
- New APIs for:

  - Window insets
  - Core primitives for gesture-driven, infinite and layout animations
  - `GraphicsLayer` capabilities, including `RenderEffect`
- Many bugfixes and performance improvements

### Version 1.2.0-rc03

June 29, 2022

`androidx.compose.ui:ui-*:1.2.0-rc03` is released. [Version 1.2.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..e8af23f4f30713a3f6073d57558e7cde0f3056e9/compose/ui)

- No changes since 1.2.0-rc02.

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.ui:ui-*:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/ui)

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.ui:ui-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/ui)

**API Changes**

- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))
- Added higher-order functions to `KeyInjectionScope` for injecting key presses while other keys are held down or toggled on. These functions include `withKeysDown`, `withKeysToggled` etc. Also added properties for checking if a particular meta key is down, for example, `isCtrlDown` to check if either control key is depressed. Refer to `KeyInjectionScope` for documentation on each function. ([I9f6cd](https://android-review.googlesource.com/#/q/I9f6cdab059c04f4af089a28f99dd267747c723de), [b/229831515](https://issuetracker.google.com/issues/229831515))
- An experimental `OverscrollEffect` has been introduced to allow for custom overscroll effects, alongside the `Modifier.scrollable` overloads that accept it.
- Experimental `LocalOverScrollConfiguration` has been moved from `foundation.gesture` to foundation package and renamed to `LocalOverscrollConfiguration` ([If19fb](https://android-review.googlesource.com/#/q/If19fb8063922eddf1ffcb020ec6a8fbe48471ccf), [b/204650733](https://issuetracker.google.com/issues/204650733))
- Rename `runComposeUiTestWithoutActivity {}` to `runEmptyComposeUiTest {}`, which aligns it with `createEmptyComposeRule()` ([I6fed7](https://android-review.googlesource.com/#/q/I6fed7b344350260084cb2776367e68b9112298c4))

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.ui:ui-*:1.2.0-beta03` is released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/ui)

**API Changes**

- Added `pressKeyTimes` as well as `isCapsLockOn` and friends to `KeyInjectionScope`. Additionally, the API now supports mouse and keyboard combined injection patterns such as clicking a mouse button with a meta key held down. ([I4c8da](https://android-review.googlesource.com/#/q/I4c8dae112eeb7526cbc32b9bce90d7e3bb5ce73a), [b/229831515](https://issuetracker.google.com/issues/229831515))
- Added experimental support for injecting key events. Use `performKeyInput` to send key events, or send them through the `key` property of `MultiModalInjectionScope` during a multi modal input gesture with `performMultiModalInput`. See `KeyInjectionScope` for documentation of the API. ([Ic5000](https://android-review.googlesource.com/#/q/Ic5000922484274309323ee4d13c9941e0d737673), [b/229831515](https://issuetracker.google.com/issues/229831515))
- Add new `GoogleFont.Provider.AllFontsListUri` for retrieving the canonical internet source of Google Fonts supported by Android.
- Improve error messages rethrown when GoogleFonts fail to load in compose. ([I0416c](https://android-review.googlesource.com/#/q/I0416cf8dc002cb2dd108cfc1a2cfddba4d5d3590))

**Bug Fixes**

- When adding `InputEventChange` events to Velocity Tracker we will consider now deltas instead of positions, this will guarantee the velocity is correctly calculated for all cases even if the target element moves ([I51ec3](https://android-review.googlesource.com/#/q/I51ec384a0424829b680b4666c7d3ce49227f45de), [b/216582726](https://issuetracker.google.com/issues/216582726), [b/223440806](https://issuetracker.google.com/issues/223440806), [b/227709803](https://issuetracker.google.com/issues/227709803))
- The `Show Layout Bounds` setting will now be applied for composables immediately after toggling it from the quick settings tile, without having to leave and re-enter the activity. ([I843d5](https://android-review.googlesource.com/#/q/I843d5a7dec3cd7b6b43c0c8af2f928bba51e1532), [b/225937688](https://issuetracker.google.com/issues/225937688))
- Accessibility string lookup does not trigger font loading. Previously, it would attempt to load fonts for `StyleSpans`, which lead to crashes if `FontFamily.Resolver` had been overwritten. ([I4609d](https://android-review.googlesource.com/#/q/I4609d0202654e929d5ec4a86432987c9fb92b494))
- Pressing the forward delete key when the cursor is at the end of a text field will no longer crash.
- `DeleteSurroundingTextCommand` and `DeleteSurroundingTextInCodePointsCommand` now require their constructor arguments to be non-negative. ([Ica8e6](https://android-review.googlesource.com/#/q/Ica8e66d221137a82ac8aaa59372decab096a6ef6), [b/199919707](https://issuetracker.google.com/issues/199919707))

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.ui:ui-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/ui)

**API Changes**

- Reusing functionality in other preview types ([I19f39](https://android-review.googlesource.com/#/q/I19f39a319fdf562c930d5b7a124da79677a36f77))

**Bug Fixes**

- `ViewCompositionStrategy.DisposeOnDetachedFromWindowIfNotInPoolingContainer` has been renamed to `DisposeOnDetachedFromWindowOrReleasedFromPool` to better reflect that when disposals do occur, rather than simply when they do not occur. ([If15ca](https://android-review.googlesource.com/#/q/If15ca41841dde8226ce850b8894e473a1ac9c9d4))

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.ui:ui-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/ui)

**New Features**

- This is the first beta release of 1.2!

**API Changes**

- Added experimental `BeyondBoundsInterval` that can be used by custom implementations of `LazyList` when they layout items beyond visible bounds ([Ifabfb](https://android-review.googlesource.com/#/q/Ifabfbd95ba53bad23ce73bdb74f816c7854222bf), [b/184670295](https://issuetracker.google.com/issues/184670295))
- Keyed versions of `Modifier.composed` are now stable API ([Ie65e4](https://android-review.googlesource.com/#/q/Ie65e40306ed029661d0137281de02b0e2ed5fea6), [b/229988420](https://issuetracker.google.com/issues/229988420))
- Simplified the `rememberNestedScrollConnection` API to use composition locals to acquire the current view information ([I67ca7](https://android-review.googlesource.com/#/q/I67ca70fdf69493105ec9487fd5f1f44996d9619e))
- The `@ComposableTarget` annotation and annotations marked by `@ComposableTargetMarker` can now be used at the file scope using the `@file` prefix. Using a target annotation at the file scope will cause the compiler to assume all composable functions in the file are intended to be target the associated applier. For example, using `@file:UiComposable` declares that all `@Composable` functions target the Compose UI applier. A function that needs to target another applier must explicitly supply the target marker annotation for the desired applier. ([I40804](https://android-review.googlesource.com/#/q/I40804e71dcc931b788c101a0be90ae1d6fc7eba1))
- Introduced new experimental, platform independent, test API:
  an `interface ComposeUiTest` and a `fun runComposeUiTest(block:
  ComposeUiTest.() -> Unit)`, that can be used to run Compose Ui tests
  without the need for a `TestRule`. To run a test without a
  `ComposeTestRule`, pass the test as a lambda to `runComposeUiTest`, and use
  the methods and members in the receiver scope `ComposeUiTest`, which are
  the same ones as in `ComposeContentTestRule`.

  The Android specific `interface AndroidComposeUiTest` and `fun
  runAndroidComposeUiTest(block: AndroidComposeUiTest.() -> Unit)` are
  added to provide access to the underlying Activity, similar to
  `AndroidComposeTestRule`. For even more control, you can instantiate a
  `class AndroidComposeUiTestEnvironment` yourself.

  The Desktop implementation is the `class DesktopComposeUiTest`, but no
  Desktop specific run functions are offered at the moment.

  Migrating a test from a `ComposeTestRule` to `ComposeUiTest` can be done
  like this (Android example). From:

      @RunWith(AndroidJUnit4::class)
      class MyTest {
          @get:Rule val rule = createComposeRule()
          @Test
          fun test() {
              rule.setContent {
                  Text("Hello Compose!")
              }
              rule.onNodeWithText("Hello Compose!").assertExists()
          }
      }

  To:

      @RunWith(AndroidJUnit4::class)
      class MyTest {
          @Test
          @OptIn(ExperimentalTestApi::class)
          fun test() = runComposeUiTest {
              setContent {
                  Text("Hello Compose!")
              }
              onNodeWithText("Hello Compose!").assertExists()
          }
      }

- For now, `ComposeContentTestRule` and `ComposeTestRule` don't extend from `ComposeUiTest`, which means extension functions on `ComposeUiTest` can't be called yet on the `TestRule` interface. When `ComposeUiTest` graduates to stable API, `ComposeContentTestRule` and `ComposeTestRule` will be changed to extend from `ComposeUiTest`. ([Ib4e90](https://android-review.googlesource.com/#/q/Ib4e909d5b4f83a9b3942278e8cb7c86854b6ecaa))

- `LineHeightBehavior` is renamed as `LineHeightStyle`

- `LineVerticalAlignment` is renamed as `LineHeightStyle.Alignment`

- Renames `LineHeightTrim` is renamed as `LineHeightStyle.Trim`

- Default constructor values from `LineHeightStyle` is removed ([I582bf](https://android-review.googlesource.com/#/q/I582bf09152d60b30362b3cce9bd60d57fc488fe7), [b/181155707](https://issuetracker.google.com/issues/181155707))

- Added `Brush` to `TextStyle` and `SpanStyle` to provide a way to draw text with gradient coloring. ([I53869](https://android-review.googlesource.com/#/q/I538698c22f5a03b57ed811ea733dd1194deaaa6a), [b/187839528](https://issuetracker.google.com/issues/187839528))

- `trimFirstLineTop`, `trimLastLineBottom` attributes of
  `LineHeightBehavior` changed into a single enum: `LineHeightTrim`.
  `LineHeightTrim` have values of 4 states defined by two booleans:
  `FirstLineTop`, `LastLineBottom`, Both and None ([Ifc6a5](https://android-review.googlesource.com/#/q/Ifc6a5912eab7a0e41ae6cd4045ea9cbdf3c0a146), [b/181155707](https://issuetracker.google.com/issues/181155707))

- Added `LineHeightBehavior` to the `TextStyle` and `ParagraphStyle`. `LineHeightBehavior` controls whether line height is applied to the top of the first line and to the bottom of the last line. It also defines the alignment of line in the space provided by `TextStyle(lineHeight)`.

  For example it is possible to get a behavior similar to what CSS
  defines via `LineHeightBehavior(alignment = LineVerticalAlignment.Center, trimFirstLineTop=false, trimLastLineBottom = false)`.
- `trimFirstLineTop`, `trimLastLineBottom` configurations works correctly only when `includeFontPadding` is false. ([I97332](https://android-review.googlesource.com/#/q/I973329a540ca9f5a6e225f1e5aaffeaa1ff9cc61), [b/181155707](https://issuetracker.google.com/issues/181155707))

- `PlatformParagraphStyle.lerp` and `PlatformSpanStyle.lerp` functions are changed to be top level
  functions ([I9a268](https://android-review.googlesource.com/#/q/I9a268d3012b3e215408b2715a73a153818facc20))

**Bug Fixes**

- `PointerInputChange::copy` documentation now correctly states that it is a shallow copy. ([I182f5](https://android-review.googlesource.com/#/q/I182f5bf7edfce52ac7502b2b77ab9e0fb08fcfe1))
- Support ellipsis when height is limited and doesn't fit all text lines ([Ie528c](https://android-review.googlesource.com/#/q/Ie528c603d4c76c31ea71524a8381000d43d1cf42), [b/168720622](https://issuetracker.google.com/issues/168720622))
- Turned on default `includeFontPadding`. It is possible to turn off the `includeFontPadding` using `TextStyle.platformTextStyle` attribute. In the near future we will change the default behavior however until that time this allows us to better integrate line height improvements (aosp/2058653) and solve `TextField` clipping issues. ([I01423](https://android-review.googlesource.com/#/q/I01423d9a0042a1f3e462236e1fdadb60a20678fc), [b/171394808](https://issuetracker.google.com/issues/171394808))

**External Contribution**

- `MouseInjectionScope.scroll(delta = someDelta)` is now inverted on Android if we scroll vertically (if someDelta is positive, it will scroll downward) ([Ifb697](https://android-review.googlesource.com/#/q/Ifb697a9ae8bc05a2d54d0a6cb4018713e156baf8), [b/224992993](https://issuetracker.google.com/issues/224992993))

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/ui)

**API Changes**

- The `pluralStringResource` functions were marked as experimental in order to allow evolution to support better internationalization in the future. ([If24e4](https://android-review.googlesource.com/#/q/If24e41254c027dac9f68b3271ce91c8788712a9b))
- Paragraph and MultiParagraph are now accepting Constraints parameter. Passing `Constraints.maxHeight` is a no-op at the moment but will allow to do some calculation in the future, like ellipsizing based on the height. ([I6afee](https://android-review.googlesource.com/#/q/I6afeecb15d34ade2e82cad0381018f0736a167c1), [b/168720622](https://issuetracker.google.com/issues/168720622))
- `SubcomposeSlotReusePolicy.getSlotsToRetain()` now accepts a custom MutableSet-like class which doesn't allow adding new items in it. ([Icd314](https://android-review.googlesource.com/#/q/Icd314177f35c2ba05d1042454ca47834cf196e10))
- PointerIcon is now a `@Stable` interface ([I9dafe](https://android-review.googlesource.com/#/q/I9dafec680d335898344ecf5be5cd2de9fcf92b06))
- Partial consumption (down OR position) has been deprecated in `PointerInputChange`. You can use `consume()` to consume the change completely. You can use `isConsumed` to determine whether or not someone else has previously consumed the change.
- `PointerInputChange::copy()` now always makes a shallow copy. It means that copies of `PointerInputChange` will be consumed once one of the copies is consumed. If you want to create an unbound `PointerInputChange`, use constructor instead. ([Ie6be4](https://android-review.googlesource.com/#/q/Ie6be471e6ed2a843e38712922c2231fdfd26213a), [b/225669674](https://issuetracker.google.com/issues/225669674))
- Enable Nested Scroll interop between Compose and View in the direction Compose \> View. This means that a compose parent will be able to receive nested scroll deltas from a nested scroll view. ([If7949](https://android-review.googlesource.com/#/q/If7949ccb50ba7897bc740b489fd3f4d615a5369b), [b/174348612](https://issuetracker.google.com/issues/174348612))
- New `SemanticsProperty testTagsAsResourceId`, which can be used to make Compose conform with UIAutomator tests designed for the View system. ([I39c20](https://android-review.googlesource.com/#/q/I39c207e20a892df47707e38708bc314a23fe18f7))
- Display all available weights for systems fonts on Android when using `FontFamily.SansSerif`. This will use fallback font names like sans-serif-medium internally on API 21-28. This is a behavior change as previously only weights 400 and 700 were supported on API 21-28. ([I380fe](https://android-review.googlesource.com/#/q/I380fecb5ba839eecbf0b08acbca6247082b605d7), [b/156048036](https://issuetracker.google.com/issues/156048036), [b/226441992](https://issuetracker.google.com/issues/226441992))
- Paragraph and Multiparagraph instructors reordered positional arguments to before optional arguments. ([Idafaa](https://android-review.googlesource.com/#/q/Idafaae32232ac4fd093530dac211f4de491c89b6))
- `AndroidFont` now takes typefaceLoader as a constructor parameter. ([I2c971](https://android-review.googlesource.com/#/q/I2c9718fa02b6f84813e5d5cdb499c89b355b0b4b))

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/ui)

**API Changes**

- New function `Snapshot.withoutReadObservation { ... }` was added. It allows users to run the passed lambda without subscribing to the changes of the state values read during this block. You could find it useful in use cases when you want to benefit from the snapshot based thread safe write/reads, but want to be able to read the value without causing unnecessary recomposition or remeasure. ([I9f365](https://android-review.googlesource.com/#/q/I9f365d653483310cfda02cfa2c582fdcce8cfe33), [b/214054486](https://issuetracker.google.com/issues/214054486))
- The `consumeWindowInsets` extension property of `ComposeView` allows developers to disable consumption of Android `WindowInsets`. This allows separate `ComposeViews` in the hierarchy to each apply `WindowInsets` without interfering with each other. ([I0ef08](https://android-review.googlesource.com/#/q/I0ef08ca81d808408edb932f9326125f99da25bd0), [b/220943142](https://issuetracker.google.com/issues/220943142))
- Added `KeyboardType.Decimal` as an alternative to `Keyboard.Number` for specifically including decimal separator in IME. ([Iec4c8](https://android-review.googlesource.com/#/q/Iec4c84be81e72f8eaf136f2df23f9d12567cc3dc), [b/209835363](https://issuetracker.google.com/issues/209835363))
- `PointerEventType.Scroll` and `PointerEvent.scrollDelta` are stable APIs now ([I574c5](https://android-review.googlesource.com/#/q/I574c579abec9e26dfc16ae00014faab8627bd688), [b/225669674](https://issuetracker.google.com/issues/225669674))
- Enable Nested Scroll interop between View and Compose for cooperating View classes. This means compose is now able to dispatch scroll deltas to a (cooperating) View parent. ([I5d1ac](https://android-review.googlesource.com/#/q/I5d1ac5fdeced612ac07f0c26ce14284a43369673), [b/174348612](https://issuetracker.google.com/issues/174348612))
- Updated `FontFamily.Resolver` to integrate System-wide bold text accessibility setting ([I6c1e7](https://android-review.googlesource.com/#/q/I6c1e77e9cc8d1ce353d129d8a233271db0139a07))
- `Font(AssetManager, String, ...)` is deprecated, replaced with `Font(String, AssetManager, ...)`. This is an experimental API. ([I1c7a4](https://android-review.googlesource.com/#/q/I1c7a4fd5df4c7413a74e594b43f6d6fe296a6c86))
- Add new font descriptor `Font(DeviceFontFamilyName)` to optionally lookup system-installed fonts during font fallback chains. ([I30468](https://android-review.googlesource.com/#/q/I30468e48564fb9891e17cbee8bdb4026df0daf89), [b/219754572](https://issuetracker.google.com/issues/219754572))
- Added temporary compatibility configuration for `includeFontPadding` in TextStyle/ParagraphStyle. `includeFontPadding` can be changed via `TextStyle(platformStyle = PlatformTextStyle(includeFontPadding = true/false))`. This is a temporary configuration option to enable migration and will be removed. ([If47be](https://android-review.googlesource.com/#/q/If47be074f53de9ccf12af114648b21e25722d166), [b/171394808](https://issuetracker.google.com/issues/171394808))
- Add `GoogleFont.Provider.isAvailableOnDevice` extension for debugging help. ([I64e31](https://android-review.googlesource.com/#/q/I64e31b3b279631ec9561c1039488e09e9780677d))
- Add `GoogleFont.Provider` constructor for use with `@ArrayRes` ([Ic5ee1](https://android-review.googlesource.com/#/q/Ic5ee1e3fec3b23447273ac85f378bb50ec9c92d9), [b/225984280](https://issuetracker.google.com/issues/225984280))
- `Compose GoogleFont` is now called `Font(GoogleFont)`, API remains stable otherwise. ([I125f2](https://android-review.googlesource.com/#/q/I125f2c7ce202fd6e524dbc750e63c7bedaaacdd6))

**Bug Fixes**

- Added lint check to material/Scaffold to ensure that the inner padding is being used ([Ifb111](https://android-review.googlesource.com/#/q/Ifb1119e54063ae06ee993e552dcfdcc48de3496b))

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/ui)

**API Changes**

- Added `RequestFocus` semantics action to request focus on the focusable target. ([I17b71](https://android-review.googlesource.com/#/q/I17b71a13ca810f3ead1b7b87245b31b8e5b28f91))
- Updated parsing of vector drawables to support auto mirroring to flip the content of a `VectorPainter` if the current layout direction is RTL. ([I79cd9](https://android-review.googlesource.com/#/q/I79cd946811e9b06ff4186180c4f8eaa0dcdbc879), [b/185760237](https://issuetracker.google.com/issues/185760237))
- Updated shadow/ambient colors to be trailing parameters of `Modifier.graphicsLayer` for API compatibility ([I3f864](https://android-review.googlesource.com/#/q/I3f8645838aa5b8dc9e5ef22dc112329abcc46b55), [b/160665122](https://issuetracker.google.com/issues/160665122))

- Added default implementations to shadow/ambient color on `GraphicsLayerScope` to ensure non-breaking API changes

- Added event time to RSB events ([Ief8ae](https://android-review.googlesource.com/#/q/Ief8ae79863483b63428fbfaa42eb752c4aca27eb))

- `FocusOrder` has now been merged into `FocusProperties` and `focusProperties()` now has all the capabilities of `focusOrder()`. `FocusOrder` and `focusOrder()` have been deprecated. `focusOrder()` that accepts a `focusRequester` should be replaced with a `focusRequester()` modifier in combination with `focusProperties()`. This allows the modifiers to have a stronger separation of concerns. ([I601b7](https://android-review.googlesource.com/#/q/I601b751755bcfefd849c8a0c0d019e3eaf5d459c))

- Upgrading both `RecyclerView` and `Compose` will now result in much better scrolling performance for RecyclerViews with Compose views as children.

- Add `ViewCompositionStrategy.Default` as a means of retrieving the built-in default strategy

- Add `ViewCompositionStrategy.DisposeOnDetachedFromWindowIfNotInPoolingContainer`, which is the new default strategy and properly handles pooling containers such as RecyclerView. ([If7282](https://android-review.googlesource.com/#/q/If7282769f8d816f8952d9ffaeef946c1314a4140))

- Added support for annotating annotations classes with @Preview as a first step for adding the Multipreview feature. Such annotations could be used to annotate Composable methods or other annotation classes, which could then be considered as indirectly annotated with the given @Preview. ([I12eff](https://android-review.googlesource.com/#/q/I12eff7461e168f73ac64973bb925758810d463a3))

- Reference devices added to the Devices list for @Preview ([I071c9](https://android-review.googlesource.com/#/q/I071c91bd1fd35586d1e2989fa8be79ebadd10e3f))

**Bug Fixes**

- Updated Vector graphics APIs to use the proper composable annotation @VectorComposable instead of @UiComposable ([I942bc](https://android-review.googlesource.com/#/q/I942bccda1a1795a7f85143524db80c1fc13bc0b9))
- Remove crossinline from `AnnotatedString.Builder.withStyle` ([If84d5](https://android-review.googlesource.com/#/q/If84d549181be7cbf802cd361dddaeaeaa835429e))

**External Contribution**

- compose-ui: Add `ambientShadowColor` and `spotShadowColor` properties to `GraphicsLayerScope` ([I1ba1a](https://android-review.googlesource.com/#/q/I1ba1a4da6942817ad8593fc9052060d7c48b3064), [b/160665122](https://issuetracker.google.com/issues/160665122))
- Plural resources are now supported via the `pluralStringResource` functions. ([Ib2f23](https://android-review.googlesource.com/#/q/Ib2f23431f0fc24a5c717a21b6309a928b2f78b91), [b/191375123](https://issuetracker.google.com/issues/191375123))

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/ui)

**API Changes**

- `TextToolbar` now takes lambda arguments instead of `ActionCallback`. ([Ib2eb9](https://android-review.googlesource.com/#/q/Ib2eb9d370cd6a22bbfbdec0d2cb536302ea43d6a), [b/197950089](https://issuetracker.google.com/issues/197950089))
- Updated nullability in core and appcompat to match Tiramisu DP2 ([I0cbb7](https://android-review.googlesource.com/#/q/I0cbb7f22651e725a4bb36d20388a949a72cc5903))
- Measured interface now exposes parentData property ([I3313f](https://android-review.googlesource.com/#/q/I3313f74c5eb4a75b91cb9d438c6691117b152a7d))
- `Modifier.onPlaced` and the `OnPlacedModifier` interface are now stable. ([Ib5482](https://android-review.googlesource.com/#/q/Ib5482e5fc018d24324a7cedc647d13599b37e42a))
- Hooray! Compose animation now supports 'Animator duration scale' setting from Developer Options. ([I5a4fc](https://android-review.googlesource.com/#/q/I5a4fc779a3fbfbcb2926ac1624cd679bb9b912ce), [b/161675988](https://issuetracker.google.com/issues/161675988))
- Added a `BeyondBoundsLayout` modifier local ([If8b51](https://android-review.googlesource.com/#/q/If8b51c6e08a375d1c733588e53c9b07474c0855c), [b/184670295](https://issuetracker.google.com/issues/184670295))
- Text: includeFontPadding is now turned off by default. The clipping issues as a result of `includeFontPadding=false` is handled and no clipping should occur for tall scripts. ([I31c84](https://android-review.googlesource.com/#/q/I31c84166ae5241fea3f49e8f293dd9d8a5d712cb), [b/171394808](https://issuetracker.google.com/issues/171394808))

**Bug Fixes**

- `ComposeContentTestRule.setContent` will now throw an `IllegalStateException` if you try to set content when there already is content. ([I888a5](https://android-review.googlesource.com/#/q/I888a5054c27d7884110415a812d0ac748be3f869), [b/199631334](https://issuetracker.google.com/issues/199631334))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Improve RSB scrolling samples. ([I6a596](https://android-review.googlesource.com/#/q/I6a59618ca5bd80f3198ddbaaccfdb09387d6039a))

**External Contribution**

- Updated to use Kotlinx coroutines 1.6.0 ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/ui)

**API Changes**

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
  `ComposableTarget` annotation for the function and any
  composable lambda parameter types. It is recommended, however,
  to create an annotation that is annotated with
  `ComposableTargetMarker` and then the marked annotation be used
  instead of `ComposableTarget` directly. A composable annotation
  marked with `ComposableTargetMarker` is equivalent to a
  `ComposbleTarget` with the fully qualified name of the attribute
  class as the applier parameter. For an example of using
  `ComposableTargetMarker` see `anroidx.compose.ui.UiComposable`. ([I38f11](https://android-review.googlesource.com/#/q/I38f11b789291db89fc0bb92fc14ac5b3fcba0283))
- `Font(resId, ...)` now takes loadingStrategy on stable API. ([Ief3d2](https://android-review.googlesource.com/#/q/Ief3d20586183c3fdc221fce4f6519685f906b0ce))

- `FontLoadingStrategy` is now stable API. ([I1ee35](https://android-review.googlesource.com/#/q/I1ee351ba27589b1c778e04425c860223ae5e5635), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Support async font loading in Text ([I77057](https://android-review.googlesource.com/#/q/I77057da6e45e78bea9622f480343c32d0bb25ce3), [b/214587005](https://issuetracker.google.com/issues/214587005))

- Add bridge API for converting custom `Font.ResourceLoader` into `FontFamily.Resolver`. ([Ia0060](https://android-review.googlesource.com/#/q/Ia0060ac94570dbdba5f0a6aaba72f250e6f8fc72))

**Bug Fixes**

- Provided `FontFamily.Resolver` are passed to subcompositions such as Popup.
- Provided `Font.ResourceLoader` are passed to subcompositions such as Popup. ([I48fa5](https://android-review.googlesource.com/#/q/I48fa5e2fe4562d72fe6efb10ecbb680a0b17d482))

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/ui)

**API Changes**

- `notifyFocusedRect` methods in `TextInputSession` and `TextInputService` are now deprecated and won't be called. Use `BringIntoViewRequester` instead. ([Ia4302](https://android-review.googlesource.com/#/q/Ia4302c5f6ee79eec30a9f42c149da8775e1ed57e), [b/192043120](https://issuetracker.google.com/issues/192043120), [b/216842427](https://issuetracker.google.com/issues/216842427), [b/178211874](https://issuetracker.google.com/issues/178211874))
- Introduced `destroyDisplayListData` method on `RenderNode` stub class ([I1e659](https://android-review.googlesource.com/#/q/I1e6593d802a1e3eb01ff4f0c6f530b016929cf18), [b/216660268](https://issuetracker.google.com/issues/216660268))
- Added a new api which allows to premeasure children of `SubcomposeLayout` you precomposed. ([I857ea](https://android-review.googlesource.com/#/q/I857eaaef22478013af2a80d05a273ef3e3bb01a9))
- Added `movableContentOf` which converts a composable
  lambda into a lambda that moves it state, and corresponding nodes,
  to any new location it is called. When the previous call leaves
  the composition the state is temporarily preserved and if a new call
  to the lambda enters the composition then the state, and associated
  nodes, are moved to the location of the new call. If no new call is
  added the state is removed permanently and remember observers are
  notified.

  If a `movableContentOf` lambda is called multiple times in the same
  composition, new state and nodes are created for each call and, as
  calls leave the composition and new calls enter, the state is moved
  from the first leaving calls to the entering calls in the order they
  are called. All state not claimed by new calls is removed
  permanently. ([Ib4850](https://android-review.googlesource.com/#/q/Ib4850095f241617a191ea7815fc947adaf867456))
- `FontFamilyResolver` is now available via `LocalFontFamilyResolver.current`

- Added `createFontFamilyResolver(context)` and `createFontFamilyResolver(context, coroutineScope)` to create new
  FontFamily resolvers outside of compose usage.

- Paragraph and MultiParagraph now take `FontFamily.Resolver`

- `TextLayoutResult.layoutInput.fontFamilyResolver` now contains
  the resolver used for this layout, deprecated
  `TextLayoutResult.layoutInput.resourceLoader` as it is no longer used. ([Id5a45](https://android-review.googlesource.com/#/q/Id5a45c72bb6f33910643ee3da7f81a78dc093d86), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Support for async and optional font loading, with fallback
  behavior. This path is used by Text and TextField, and exposed through
  FontFamilyResolver

- Support for preloading fonts via `FontFamilyResolver.preload`

- `FontFamilyResolver.setAsyncLoadContext` allows setting the
  global coroutine context used for loading async fonts. ([I87fe8](https://android-review.googlesource.com/#/q/I87fe8bfe5715c956843a7676fe7d783c3cd974d8), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Added `AndroidFont`, a new low-level API for providing new types
  of font resource descriptors on Android. For example, loading fonts from
  an app-specific backend, optionally locating pre-installed fonts
  on-device, or loading a font from a resource not provided by the current
  Font factories.

- Expanded `Font.ResourceLoaded` API to support optional and async
  font loading. It is not recommended that application developers use this
  API directly. To add new types of fonts see `AndroidFont`.

- `Font.AndroidResourceLoader` extension function allows
  construction of a `Font.ResourceLoader` when outside of composition.

- Added `loadingStrategy` parameter to resource-based fonts, to allow
  async loading when resource font references downloadable fonts XML. ([Ie5aea](https://android-review.googlesource.com/#/q/Ie5aeadd2feaf996d2c826d87dd310b8984e106c8), [b/174162090](https://issuetracker.google.com/issues/174162090))

- `Typeface(FontFamily)` constructor is deprecated. This was
  previously used to preload fonts, which may take up to 10 seconds for
  downloadable fonts. With downloadable fonts, this call may block for 10
  seconds. Instead use `FontFamilyResolver.preload`.

- `fontResource(FontFamily): Typeface` is deprecated. This was
  previously used to preload fonts, which may take up to 10 seconds for
  downloadable fonts. Instead use `FontFamilyResolver.preload` ([If8e7c](https://android-review.googlesource.com/#/q/If8e7c6ce7cd64be8094a576587cc1329e19d246f), [b/174162090](https://issuetracker.google.com/issues/174162090))

- `SubcomposeLayoutState` constructor accepting `maxSlotsToRetainForReuse` is now deprecated. Instead there is a new constructor accepting `SubcomposeSlotReusePolicy` - a new interface allowing more granular control on what slots should be retained for the future reuse. ([I52c4d](https://android-review.googlesource.com/#/q/I52c4d0360cd987ce03504807312beabdbe410ab0))

- Exposes HSV and HSL function in `Color` as non-experimental
  API. The Oklab color space is now public API. ([I08fb6](https://android-review.googlesource.com/#/q/I08fb6cd74b1970deba71db86a0afdef0a8c1e735), [b/180731008](https://issuetracker.google.com/issues/180731008))

- Deprecated `AndroidComposeTestRule.AndroidComposeStatement`,
  which was not meant to be in public API and didn't do anything for you
  anyway. ([Ibc46b](https://android-review.googlesource.com/#/q/Ibc46b2efcdb207a38296f470b284cfe8ac61e512))

- Internal generated kt class rename ([Ia0b9e](https://android-review.googlesource.com/#/q/Ia0b9e518f8eb18ac6d5d341c933085a32db012ff), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Removed `FontLoadingStrategy.values` ([I42a9d](https://android-review.googlesource.com/#/q/I42a9dbf74cb40af63ac504045b61e8cc1ceaaf9d), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Global font loader is now called `FontFamilyResolver`. ([I4f773](https://android-review.googlesource.com/#/q/I4f7736829412d6a553a8cffe4eba2b6cda1f3d19), [b/174162090](https://issuetracker.google.com/issues/174162090))

- Use new font loading system for desktop. ([I9ce5c](https://android-review.googlesource.com/#/q/I9ce5cf9d537d95cf983c0e9a2a2462b5f046c359), [b/174162090](https://issuetracker.google.com/issues/174162090))

- `FontFamily.Resolver.resolve` returns `State<Any>` ([I4406c](https://android-review.googlesource.com/#/q/I4406c9752595e349abb8c4d733b9cad459cebfe2), [b/174162090](https://issuetracker.google.com/issues/174162090))

**Bug Fixes**

- TextFields will now be kept above the keyboard when they are focused and the keyboard is shown, when the soft input mode is `ADJUST_PAN`. ([I8eaeb](https://android-review.googlesource.com/#/q/I8eaebb684b7828dcf92b0678a86d796b49b349c8), [b/190539358](https://issuetracker.google.com/issues/190539358), [b/192043120](https://issuetracker.google.com/issues/192043120))
- Desktop uses composition local for `FontFamily.Resolver`
- Desktop `FontLoader` is deprecated
- New `createFontFamilyResolver` factory on Desktop ([I6bbbb](https://android-review.googlesource.com/#/q/I6bbbb76ece4ca3844f07e2fc22c2e63478bfdd8c), [b/174162090](https://issuetracker.google.com/issues/174162090))
- The soft keyboard input type no longer flickers when changing focus between text fields. ([I1bf50](https://android-review.googlesource.com/#/q/I1bf50cacddd8e20f9bd3d5124f277e5fef467ac0), [b/187746439](https://issuetracker.google.com/issues/187746439))

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03c236077d11b7c7452123b550442c781468223e..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/ui)

**API Changes**

- Added `Modifier.onRotaryScrollEvent()` and `Modifier.onPreRotaryScrollEvent()` for wear devices with a rotating side button ([I18bf5](https://android-review.googlesource.com/#/q/I18bf59262881d9c4a2edea159751164340ac3ed5), [b/210748686](https://issuetracker.google.com/issues/210748686))
- Add experimental `View.createLifecycleAwareRecomposer` extension ([I0cde6](https://android-review.googlesource.com/#/q/I0cde64f930ac68bf3895c5a5e58b9ac8213e8b84))

**External Contribution**

- `PointerEvent.scrollDelta.y` is now inverted on Android (now it returns 1 instead of -1 if we tilt mouse wheel to the right) ([Ia9811](https://android-review.googlesource.com/#/q/Ia981193e0870111d3f595b5b6c14f6bdc98f9873))

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.ui:ui-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/ui)

**API Changes**

- Deprecated `FontFamily.canLoadSynchronously`. This property has no semantic meaning. ([Ica5ef](https://android-review.googlesource.com/#/q/Ica5ef39f37c96a75502a1f25dff2ced62f54c019))
- Added identity field to `CompositionData` for generating invariant ids in the Layout Inspector. ([Ic116e](https://android-review.googlesource.com/#/q/Ic116e6682233c31ccc4a81f8cf0cc96cac4a83ca))
- Added Wear OS device ids to Preview devices list ([I93232](https://android-review.googlesource.com/#/q/I93232e4ea62f20e20d3193ee8b79c800026c01f2))

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.ui:ui-*:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/ui)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.ui:ui-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/ui)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
  - Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of 48x48dp, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable Support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.ui:ui-*:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/ui)

**Bug Fixes**

- Updated to support Compose Material 1.1.0-rc03

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.ui:ui-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/ui)

**Bug Fixes**

- Fixed a bug that caused missing accessibility scroll actions ([I7cbfb](https://android-review.googlesource.com/#/q/I7cbfb524b5baf98f044ee043ed19b8ad68cc9f89))
- `SemanticsNodeInteraction.captureToImage()` will now also work if `HardwareRenderer.isDrawingEnabled()` is `false`, by enabling it for the duration of the call ([Idf3d0](https://android-review.googlesource.com/#/q/Idf3d09c3a63458914d30b66e86bdea17101f7791))

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.ui:ui-*:1.1.0-beta04` is released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/ui)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

**API Changes**

- Cleaned up nullability in `androidx.core.view` ([I7078a](https://android-review.googlesource.com/#/q/I7078a577cc3cab983bdf34fae57e962fa734ceb9), [b/204917439](https://issuetracker.google.com/issues/204917439))
- Experimental APIs were added that allow users to consume PointerInputchange as a whole or check whether it was consumed or not. ([I2e59d](https://android-review.googlesource.com/#/q/I2e59de430d24336bbdbe3d0a975948969e8d2e82))
- Adds support for mouse scroll wheel events in the UI layer. ([Ia14eb](https://android-review.googlesource.com/#/q/Ia14eb9c9827bff80b57ecc62ae9227fad74c2a7e), [b/198214718](https://issuetracker.google.com/issues/198214718))
- Add experimental `Modifier.composed` overloads that accept keys to compare for equality and qualify for skipping optimizations. ([Ice799](https://android-review.googlesource.com/#/q/Ice799fbdef230423eab1ad0247979091410b9065), [b/205851704](https://issuetracker.google.com/issues/205851704))
- `ComposeNotIdleException` now extends from `Exception` instead of directly from `Throwable`. Note that this means that catch clauses that were catching `Exception` might now catch `ComposeNotIdleException`s, where they wouldn't do that previously. ([I9c217](https://android-review.googlesource.com/#/q/I9c217e174dbdeb96ef97ebcf840ef300a4dd9276))

**Bug Fixes**

- Fix text handles not moving when IME visibility changes. ([I25f2e](https://android-review.googlesource.com/#/q/I25f2ec3b813f179836c6e69c78bbd8ff2a636179))

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.ui:ui-*:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/ui)

**API Changes**

- Added new modifier Modifier.onPlaced to allow placement change to be observed. Additional changes to child modifier's offset can therefore be made based on the observed placement change. ([I558fd](https://android-review.googlesource.com/#/q/I558fd6a0fc0788942efe09a6c3e33c6c62608904))
- Removed `InjectionScope.flush()` and `InjectionScope.dispose()`. Flushing of all events and disposing of the scope now happens at the end of the called perform\*Input() method like before. ([I2bed8](https://android-review.googlesource.com/#/q/I2bed810296ab70173753b06bbc049dabeec39daa))
- Removed `MultiModalInjectionScope.Touch` and `MultiModalInjectionScope.Mouse`. In order to inject touch and mouse events for multi-modal gestures, you can now use `MultiModalInjectionScope.touch()` and `MultiModalInjectionScope.mouse()`, both of which accept a lambda that has the receiver scope of that modality. ([Idde18](https://android-review.googlesource.com/#/q/Idde18dc95d6b71c8ac15772198ef5de8b612a5b6))

**Bug Fixes**

- The default value for `durationMillis` in `TouchInjectionScope.swipeWithVelocity` is now calculated such that the swipe is feasible. ([I19deb](https://android-review.googlesource.com/#/q/I19deb73532dd304fd8646b576f27feec6538f58f))

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.ui:ui-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/ui)

**API Changes**

- Added experimental BringIntoView API that lets you send a request to parents so that they scroll to bring an item into view ([Ib918d](https://android-review.googlesource.com/#/q/Ib918da5f0ee21833e6e1c12169dbd308ca33caf5), [b/195353459](https://issuetracker.google.com/issues/195353459))
- New animation APIs for supporting tooling. Specifically, they allow tooling to inspect the animations \& their configurations in a Transitions. ([I4116e](https://android-review.googlesource.com/#/q/I4116e0f930fdbbbf3c306e1c2aa32b71b257bd3d))

**External Contribution**

- Added Modifier.pointerHoverIcon ([I95f01](https://android-review.googlesource.com/#/q/I95f011f87824926ddc87398a5ad553ca003c6f08))

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.ui:ui-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/ui)

**API Changes**

- Added experimental `BringIntoView` API that lets you send a request to parents so that they scroll to bring an item into view ([Ib918d](https://android-review.googlesource.com/#/q/Ib918da5f0ee21833e6e1c12169dbd308ca33caf5), [b/195353459](https://issuetracker.google.com/issues/195353459))
- New animation APIs for supporting tooling. Specifically, they allow tooling to inspect the animations \& their configurations in a Transitions. ([I4116e](https://android-review.googlesource.com/#/q/I4116e0f930fdbbbf3c306e1c2aa32b71b257bd3d))

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/ui)

**API Changes**

- Remove `ExperimentalComposeUiApi` from `ViewRootForInspector` and `LayoutInfo.ownerViewId` ([I5c2e3](https://android-review.googlesource.com/#/q/I5c2e3ad58a1baacb7d329eea216dd56eea548efe))
- A child-less overload for Layout was added, with improved efficiency ([Ib0d9a](https://android-review.googlesource.com/#/q/Ib0d9a0f11936c0568d20e26a3c6eaa3f938e0ccd))
- Removed `InternalCompilerApi` from Composer methods that are required to be called cross-module ([I1aa0b](https://android-review.googlesource.com/#/q/I1aa0b78dbfb808d352e3a46de2388797548d34a9))
- `SemanticsNodeInteraction.performSemanticsAction` now returns the `SemanticsNodeInteraction` on which the function was called. ([I9e5db](https://android-review.googlesource.com/#/q/I9e5db630fbc3c254a4cc862c45bae71496e3c99f))
- Added LocalInputModeManager CompositionLocal to detect TouchMode/NonTouchMode. ([I6a83c](https://android-review.googlesource.com/#/q/I6a83c0c04f4da63ffdf287051a2277cb337d7104), [b/175899786](https://issuetracker.google.com/issues/175899786))
- Added `viewConfiguration: ViewConfiguration` to `LayoutInfo` to allow consumers get the correct value for things like long press timeout. ([I76ca6](https://android-review.googlesource.com/#/q/I76ca6fd7a1f9f3161e0ceaee75e4d3431da11251))
  - Added `viewConfiguration: ViewConfiguration` to `InjectionScope` to allow tests to adjust input injection based on things like long press timeout or touch slop.
  - Changed default duration of long press and double tap for both touch and mouse input to be based on the values in `InjectionScope.viewConfiguration`.
- Implementation of ExposedDropdownMenu based on ExposedDropdownMenuBox with TextField and DropdownMenu inside ([If60b2](https://android-review.googlesource.com/#/q/If60b2e6c7c139d4d4c134c714e2803f531a6c72a))
- dismissOnOutsideClick was added to PopupProperties, replacing dismissOnClickOutside which was deprecated. The new property receives the click position and the anchor bounds, providing finer control over whether onDismissRequest should be invoked or not. For example, this can be useful to prevent anchor dismissal for touches on the anchor.
  - updateAndroidWindowManagerFlags was added to PopupProperties, offering low-level control over the flags passed by the popup to the Android WindowManager. The parameter of the lambda will be the flags calculated from the PopupProperties values that result in WindowManager flags: e.g. focusable. The result of the lambda will be the final flags which will be passed to the Android WindowManager. By default, updateAndroidWindowManagerFlags will leave the flags calculated from parameters unchanged. This API should be used with caution, only in cases where the popup has very specific behavior requirements. ([I6e9f9](https://android-review.googlesource.com/#/q/I6e9f9d393dc12bd1ea7ae294af1761817f154735))
- `Recomposer.state` has been deprecated and replaced by `Recomposer.currentState` to change its type to a StateFlow ([Ic2ab3](https://android-review.googlesource.com/#/q/Ic2ab34c19176704fe2f6cd081607dfb92d86ea3c), [b/197773820](https://issuetracker.google.com/issues/197773820))
- Added `flush()` and `dispose()` to `InjectionScope`. Use them when you want to flush all queued up events immediately and when you want to dispose of the scope, respectively. ([Ifb73a](https://android-review.googlesource.com/#/q/Ifb73a2812da448c872ab86fc06be4f8c242960b3))
- Added `performScrollToNode(matcher: SemanticsMatcher)` that scrolls a scrollable container to the content that is matched by the given matcher. ([Ic1cb8](https://android-review.googlesource.com/#/q/Ic1cb855e351c7bb683962d618d68782628b70f62))
- `InjectionScope` now implements `Density`, allowing you to easily convert between px and dp in `performTouchInput` and friends. ([I8fe1f](https://android-review.googlesource.com/#/q/I8fe1f17d53f8a51f9cb8bcce5b6d40de093da66b))

**Bug Fixes**

- AndroidView now propagates LocalLifecycleOwner and LocalSavedStateRegistryOwner to its view via ViewTreeLifecycleOwner and ViewTreeSavedStateRegistryOwner. ([I38f96](https://android-review.googlesource.com/#/q/I38f966576085db66e35b0106f49275ef5bb31adc), [b/179708470](https://issuetracker.google.com/issues/179708470))
- Fix WearOS SwipeToDismissBox sometimes not handling swipes. ([I9387e](https://android-review.googlesource.com/#/q/I9387e6584e9d04d7ffda3a4319e3da2da13788b5))
- The default time between injected input events has been changed from 10ms to 16ms. This potentially changes the outcome of tests that perform input gestures, like a specific swipe. ([I829fd](https://android-review.googlesource.com/#/q/I829fd33dd4ba14313ac73daf7c2e770955c90df6))

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/ui)

**API Changes**

- Added support for inter-modifier communication ([Id5467](https://android-review.googlesource.com/#/q/Id5467fce8c0463ec19af5c6170f4692307d2fbe2), [b/198826874](https://issuetracker.google.com/issues/198826874))
- Added experimental historical pointers to PointerEventChange. ([Ic1fd8](https://android-review.googlesource.com/#/q/Ic1fd82fd3f2335a9289cc1fc96c35e89ec9b90ee), [b/197553056](https://issuetracker.google.com/issues/197553056), [b/199921305](https://issuetracker.google.com/issues/199921305))
- Added `density: Density` and `layoutDirection:
  LayoutDirection` to `LayoutInfo`. This allows consumers of `LayoutInfo` to interpret the dimensions and position exposed in `LayoutInfo` properly. ([I002f1](https://android-review.googlesource.com/#/q/I002f191f17be7fa867cecf9c974edfb694523786))
- Added experimental support for injecting mouse events. Use `performMouseInput` to start sending mouse events, or send mouse events through the `Mouse` property of `MultiModalInjectionScope` during a multi modal input gesture with `performMultiModalInput`. See `MouseInjectionScope` for documentation of the available API. ([Iaa4a8](https://android-review.googlesource.com/#/q/Iaa4a82131f35d2d6376d8edaa1fac4807b27045d), [b/190493367](https://issuetracker.google.com/issues/190493367))

**Bug Fixes**

- Fixed accessibility support for scrollables (both lazy and non-lazy) with respect to scrolling ([I6cdb0](https://android-review.googlesource.com/#/q/I6cdb0e5114faa448deacd4d662893cec43c2d9f0))
- Improved `TouchInjectionScope.swipeWithVelocity`. It now accepts a wider range of input variables and will suggest changes to the input if a swipe can't be created ([I40fbe](https://android-review.googlesource.com/#/q/I40fbe57b6f28689bc2597b2e64ae0ef28158e593), [b/182477143](https://issuetracker.google.com/issues/182477143))

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/ui)

**API Changes**

- `PointerEvent` now has a `PointerEventType` to support hover events. ([I091fa](https://android-review.googlesource.com/#/q/I091fa991d1680d69a2532e73a894913c2865663d))
- Allow children to accept pointer input outside of parent's pointer input bounds. Parents may intercept those calls with a property PointerInputScope.alwaysInterceptChildEvents ([I9eae3](https://android-review.googlesource.com/#/q/I9eae3ce577012e26c3532266ac63db8e84ce5c7f), [b/192479655](https://issuetracker.google.com/issues/192479655))
- Deprecated `performGesture` and `GestureScope`, which have been replaced by `performTouchInput` and `TouchInjectionScope`. ([Ia5f3f](https://android-review.googlesource.com/#/q/Ia5f3f740c51a1add60fa82189d583d8a5192dd31), [b/190493367](https://issuetracker.google.com/issues/190493367))
- Added `touchBoundsInRoot` to `SemanticsNode` that includes the minimum touch target size so that developers can ensure that touch targets meet accessibility minimums. ([I2e14b](https://android-review.googlesource.com/#/q/I2e14bf1bab7a745aa2421353f44c734540d2489c), [b/197751214](https://issuetracker.google.com/issues/197751214))
- Redo implementation of inspectable ([I927bc](https://android-review.googlesource.com/#/q/I927bc731712d81f47aefdf946f778047c7645b26), [b/191017532](https://issuetracker.google.com/issues/191017532))
- Changed parameter name of inspectable to match composed ([I3a482](https://android-review.googlesource.com/#/q/I3a482c9f64ef0f7cc5a5a59cecaec010ca001e3f), [b/191017532](https://issuetracker.google.com/issues/191017532))
- Introduced `performTouchInput` and `TouchInjectionScope` as a
  replacement for `performTouchInput` and `TouchInjectionScope`, paving
  the way for other modalities (like mouse).

  `TouchInjectionScope` has the same methods as `GestureScope`, with the
  exception of `movePointerTo` and `movePointerBy`, which have been
  renamed to `updatePointerTo` and `updatePointerBy`. All other methods
  are the same.

  The behavior of `TouchInjectionScope` is almost identical to
  `GestureScope`, with two small details:
  1. When sending a down event while pointers had been moved without sending a move event (in other words, `updatePointerTo()` has been used, but not `move()`, and then `down()` is called), the previous implementation would advance the event time and send a move event before sending the down event. The new implementation still sends the move event, but doesn't advance the event time in this specific scenario.
  2. When sending an up event while pointers had been moved without sending a move event (similar as above), the previous implementation would advance the event time and send a move event before sending the up event. The new implementation does neither: the new positions of the pointers will only be reflected through the up event.

  Finally, `TouchInjectionScope` introduces a new method
  `currentPosition(pointerId: Int)` to get the current position of the
  given pointer. ([If1191](https://android-review.googlesource.com/#/q/If11912d1d85da53b0f675f874be29ecde1b8c7cd), [b/190493367](https://issuetracker.google.com/issues/190493367))

**Bug Fixes**

- Allow clip to extend touch target bounds beyond the clip region for minimum touch target purposes. ([I43e10](https://android-review.googlesource.com/#/q/I43e10218f7a20b5a8190ea838cef8eb8440928d1), [b/171509422](https://issuetracker.google.com/issues/171509422))
- Support for stretch overscroll has been added on Android 12 devices. ([Iccf3c](https://android-review.googlesource.com/#/q/Iccf3c3830a01469940828e21bc32b569951c187e), [b/171682480](https://issuetracker.google.com/issues/171682480))

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/ui)

**New Features**

- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

**API Changes**

- Added `Modifier.inspectable` for wrapping other modifiers. ([I1909b](https://android-review.googlesource.com/#/q/I1909b068b72041b8363c04c7ec619fcf26702da4), [b/191017532](https://issuetracker.google.com/issues/191017532))
- Added `BlurredEdgeTreatment` API to simplify blur use cases into more commonly used combinations of clip flags and TileModes. Most use cases involve either letting blurred content render outside the original content bounds and blurring regions outside these bounds with transparent black, or clipping content to content bounds sampling the closest edge for blur kernels that extend beyond content bounds. ([I6b4b7](https://android-review.googlesource.com/#/q/I6b4b7966920855374275ae7ea950b310fa28efd0), [b/166927547](https://issuetracker.google.com/issues/166927547))
- Added support for RenderEffect in compose desktop. Introduced OffsetEffect as well as the blur modifier as a simple way to introduce blur visual effects to a portion of the composition hierarchy. ([I0f6aa](https://android-review.googlesource.com/#/q/I0f6aa293db2bf34f5ed2aa7499a97332dacf73fc), [b/166927547](https://issuetracker.google.com/issues/166927547))
- Introduced RenderEffect API that can be optionally configured on a `Modifier.graphicsLayer` to alter the contents of the layer itself. This can be used to blur contents of a composable and child composables within a composition hierarchy. ([I47c4d](https://android-review.googlesource.com/#/q/I47c4d5ecc801f35e632d2062e03c756f564a2db5), [b/166927547](https://issuetracker.google.com/issues/166927547))
- AwaitPointerEventScope now has withTimeout() and withTimeoutOrNull() ([I507f0](https://android-review.googlesource.com/#/q/I507f0e696311ac0504126681c376f73beaa021fb), [b/179239764](https://issuetracker.google.com/issues/179239764), [b/182397793](https://issuetracker.google.com/issues/182397793))
- Added minimum touch target size to ViewConfiguration for use in semantics and pointer input to ensure accessibility. ([Ie861c](https://android-review.googlesource.com/#/q/Ie861ca1fcdbfcc9455352fc3a459d5734d5d57cc))
- Add TileMode.Decal support which is useful in defining edge behavior for blur based RenderEffects. ([I7e8ed](https://android-review.googlesource.com/#/q/I7e8ed0c4eb2490ef3cd0032b5952d0962f489354), [b/166927547](https://issuetracker.google.com/issues/166927547))
- `performScrollToIndex`, `performScrollToKey`, `hasScrollToIndexAction` and `hasScrollToKeyAction` are now stable API ([I142ae](https://android-review.googlesource.com/#/q/I142aefdd8455195d30a6b029b76255f1f737939f), [b/178483889](https://issuetracker.google.com/issues/178483889))
- Added test method to get the clipped bounds. ([I6b28e](https://android-review.googlesource.com/#/q/I6b28e437d6893a63be65c8a451a84bcb21bce906))

**Bug Fixes**

- Removed isBounded method from BlurredEdgeTreatment in favor of explicitly checking if the shape parameter is null. ([I85d68](https://android-review.googlesource.com/#/q/I85d687c2591770875dbfcc0fb893a8a377efefc4))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/ui)

**API Changes**

- PointerEvent now has support for reading mouse button state and keyboard modifier state. ([I6310c](https://android-review.googlesource.com/#/q/I6310c8e6bd4d2e383389db7d4a33299aa1c52cd3), [b/180075467](https://issuetracker.google.com/issues/180075467))
- Injected gestures now use the MainTestClock's time as the source of truth for time. The current time for injected events in `performGesture` will be initialized to the current time of the MainTestClock. ([Ifb364](https://android-review.googlesource.com/#/q/Ifb364da90fcbecacfcf7614168969655777905cd), [b/192064452](https://issuetracker.google.com/issues/192064452))
- Added `DpRect(DpOffset, DpSize)` constructor ([I2cf16](https://android-review.googlesource.com/#/q/I2cf1636d05302a444587d6a6c43bd2e52c0a903f), [b/194219828](https://issuetracker.google.com/issues/194219828))
- Added DpSize class ([I7abb1](https://android-review.googlesource.com/#/q/I7abb129c8c18a3f77b68aec5c2060d2aad11a693), [b/194219828](https://issuetracker.google.com/issues/194219828))

**Bug Fixes**

- Updated Vector graphics xml parsing to support ColorStateLists as root color tint properties on VectorDrawables. ([I86915](https://android-review.googlesource.com/#/q/I86915d08bdf50f729e91ec85c9f8595ad16f9562), [b/195668138](https://issuetracker.google.com/issues/195668138))

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.ui:ui-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/ui)

**API Changes**

- `RelocationRequester.bringIntoView` now accepts a rectangle as a parameter which enables us to bring a part of a composable into view ([Ice2c5](https://android-review.googlesource.com/#/q/Ice2c55d582bbeb80757cf30e2334bb970a31f438), [b/194330245](https://issuetracker.google.com/issues/194330245))
- `AnimatedImageVector` and the related APIs are now in the new `androidx.compose.animation:animation-graphics` module. ([I60873](https://android-review.googlesource.com/#/q/I6087391a9869d2315a71422f24175f42ec085681))
- Added experimental modifier to handle relocation requests. ([I65a97](https://android-review.googlesource.com/#/q/I65a97bd7fca7271781efe31fcc9cb387e9857b51), [b/178211874](https://issuetracker.google.com/issues/178211874))
- Introduced BrushPainter API
  to support drawing of an arbitrary Brush
  within a Painter, similar to ColorPainter

  Updated Brush API to have an intrinsic size
  parameter that is queried within BrushPainter ([Ia2752](https://android-review.googlesource.com/#/q/Ia27529070e6f2acdac9d2c73f41e886b36452f34), [b/189466433](https://issuetracker.google.com/issues/189466433))
- Updated DrawScope#drawImage method that
  consumes source and destination rects
  to consume an optional FilterQuality
  parameter. This is useful for pixel
  art that is intended to be pixelated
  when scaled up for pixel based art.
  Updated BitmapPainter + Image composable
  to also consume an optional FilterQuality
  parameter ([Ie4fb0](https://android-review.googlesource.com/#/q/Ie4fb04013701add0fba1c5c6bb9da2812d6436e7), [b/180311607](https://issuetracker.google.com/issues/180311607))

- Added `GestureScope.advanceEventTime` method to give more
  control over the timing of events in a gesture ([Ibf3e2](https://android-review.googlesource.com/#/q/Ibf3e2d35b4462863aa0de010cb2d0fe0d10cd3d1))

**Bug Fixes**

- In order to better support chaining of draw modifiers, make sure the Modifier.paint implementation calls drawsContent. Previously Modifier.paint was expected to a leaf node in the chain of Modifiers, however, by doing so it prevents it from being configured on a composable container (ex. box) or adding additional decorations on top such as `Modifier.paint().border()`. By having Modifier.paint call drawContent after drawing the contents of the given painter, we have better behavior consistency in behavior with the modifier pattern. ([Ibb2a7](https://android-review.googlesource.com/#/q/Ibb2a7ae54a86643ba4fc1604ce39df7477ab66f0), [b/178201337](https://issuetracker.google.com/issues/178201337), [b/186213275](https://issuetracker.google.com/issues/186213275))
- Dialogs now follow the platform sizing behaviour. Set `usePlatformDefaultWidth` to false to override this behaviour. ([Iffaed](https://android-review.googlesource.com/#/q/Iffaedb8890f59627a58fb4f33d06044ac120fd7d), [b/192682388](https://issuetracker.google.com/issues/192682388))
- Moved `InfiniteAnimationPolicy` to :compose:ui ([I5eb09](https://android-review.googlesource.com/#/q/I5eb09c7aa24a85fd2e66cc9b84ea6c906dc5210a), [b/160602714](https://issuetracker.google.com/issues/160602714))
- Scrolling via semantics actions for lazy lists and regular scrolling components is now animated ([Id9066](https://android-review.googlesource.com/#/q/Id9066420fd80bbea3c0463813be0338fff017514), [b/190742024](https://issuetracker.google.com/issues/190742024))

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.ui:ui-*:1.0.5` is released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/ui)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.ui:ui-*:1.0.4` is released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/ui)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.ui:ui-*:1.0.3` is released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/ui)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.ui:ui-*:1.0.2` is released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/ui)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.ui:ui-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/ui)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.ui:ui-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/ui)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

**Known Issues**

- If you are using Android Studio Bumblebee Canary 4 or AGP `7.1.0-alpha04`/`7.1.0-alpha05`, you may hit the following crash:

        java.lang.AbstractMethodError: abstract method "void androidx.lifecycle.DefaultLifecycleObserver.onCreate(androidx.lifecycle.LifecycleOwner)"

  To fix, temporarily increase your minSdkVersion to 24+ in your `build.gradle` file. This issue will be fixed in the next version of Android Studio Bumblebee and AGP `7.1`. ([b/194289155](https://issuetracker.google.com/issues/194289155))

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.ui:ui-*:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/ui)

**Bug Fixes**

- Dialogs now follow the platform sizing behaviour. Set `usePlatformDefaultWidth` to false to override this behaviour. ([Iffaed](https://android-review.googlesource.com/#/q/Iffaedb8890f59627a58fb4f33d06044ac120fd7d), [b/192682388](https://issuetracker.google.com/issues/192682388))

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.ui:ui-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/ui)

**New Features**

- Split ui-tooling module into `ui-tooling` and `ui-tooling-preview` ([Iefa28](https://android-review.googlesource.com/#/q/Iefa283aba6e2b41459ea17b0c35a4d6fc7fb4c3f), [b/190649014](https://issuetracker.google.com/issues/190649014))

**API Changes**

- Removed deprecated experimental `FocusManager#moveFocusIn` and `FocusManager#moveFocusOut` ([I227d7](https://android-review.googlesource.com/#/q/I227d79e985d993d52d383d22439abaecbce9f593), [b/170154986](https://issuetracker.google.com/issues/170154986), [b/186567354](https://issuetracker.google.com/issues/186567354), [b/168510304](https://issuetracker.google.com/issues/168510304))
- Canvas now supports a contentDescription parameter for accessibility. ([Ib547c](https://android-review.googlesource.com/#/q/Ib547c8fdb4c76a64f5ddcfe8ef3d46a0792f40bc))
- `useDefaultMaxWidth` in `PopupProperties` was renamed to `usePlatformDefaultWidth`. ([I05710](https://android-review.googlesource.com/#/q/I0571008fba7541d07511b95f31e1854849f36124))
- Dialogs are now able to use the entire screen width. ([I83929](https://android-review.googlesource.com/#/q/I83929941b29e5afe443b7472ff36e46b1ccc8108), [b/190810877](https://issuetracker.google.com/issues/190810877))
- Added experimental support for HSV and HSL color representations. ([Id7cf8](https://android-review.googlesource.com/#/q/Id7cf8ae76f6fbeaebabcd5551d71964f50499b4a), [b/180731008](https://issuetracker.google.com/issues/180731008))

**Behavior Changes**

- Compose `@Preview` now provides a `LocalActivityResultRegistryOwner` that allows you to preview Composables that use APIs like `rememberLauncherForActivityResult()` that depend on that owner existing. ([Ib13d1](https://android-review.googlesource.com/#/q/Ib13d12f085065adb89cfb731179b9295029e06e9), [b/185693006](https://issuetracker.google.com/issues/185693006))
- Compose `@Preview` now provides a `LocalOnBackPressedDispatcherOwner` that allows you to preview Composables that use APIs like `BackHandler` that depend on that owner existing. ([Ia1c05](https://android-review.googlesource.com/#/q/Ia1c05ea3cadf2fb55cef9c4b8bae0898cfb35ba9), [b/185693006](https://issuetracker.google.com/issues/185693006))

**Bug Fixes**

- Moved `InfiniteAnimationPolicy` to `androidx.compose.ui:ui` ([I5eb09](https://android-review.googlesource.com/#/q/I5eb09c7aa24a85fd2e66cc9b84ea6c906dc5210a), [b/160602714](https://issuetracker.google.com/issues/160602714))
- AnimatedImageVector was temporarily removed in order to change the module structure. ([I41906](https://android-review.googlesource.com/#/q/I419062b1b225003ee594f4d8522b11bb024144d6), [b/160602714](https://issuetracker.google.com/issues/160602714))

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.ui:ui-*:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/ui)

**API Changes**

- Change enum Role and LiveRegionMode into inline classes with private constructor ([Id1890](https://android-review.googlesource.com/#/q/Id189080b0537dde66639fc87f08ec5f46a449a97))
- KeyboardCapitalization is converted into an inline class. ([Id5a1c](https://android-review.googlesource.com/#/q/Id5a1c8b2c89a65eb41aa44675b960a3bb0dc1020))
- Change HapticFeedbackType to inline class. ([I255ec](https://android-review.googlesource.com/#/q/I255ec46ff76414180599fc5328a5b6b57a6f0915))
- Modifier.pointerInteropFilter is @ExperimentalComposeUiApi. ([Iede6c](https://android-review.googlesource.com/#/q/Iede6c29413d359091df79d8178684c857305db75))
- TextAlign, FontSynthesis and TextDirection are now inline classes. ([I212fe](https://android-review.googlesource.com/#/q/I212fee8bac36263fb0eda9c3362015c860168a73))
- TextOverflow is changed to an inline class. ([I433af](https://android-review.googlesource.com/#/q/I433af65606ae4e79ea0cb281be7049c73b12fcf0))
- FontStyle is now an inline class. ([I9e48b](https://android-review.googlesource.com/#/q/I9e48bba8f3c4e4cc45468b86d7145b18389be21c))

**Bug Fixes**

- Key constants are @ExperimentalComposeUiApi for now. Consuming code can declare private constants prior to stabilization. ([Ia5d48](https://android-review.googlesource.com/#/q/Ia5d48d518c6e73f5e3458260203dc237bef5464d))
- Compose tests can now be run on Robolectric. The following limitations have so far been identified:
  - There is no native bitmap, so `ImageBitmap()` leads to a NullPointerException.
  - There is no drawing, so `captureToImage()` will indefinitely await the next draw pass (i.e. it deadlocks).
  - There is no font loaded, so any text will be measured incorrectly. All characters have a fixed height of around 20px and width of 1px.
  - `ComposeTestRule.waitUntil {}` does not run the main thread while it's waiting, making it effectively the same as `ComposeTestRule.mainClock.advanceTimeUntil {}` More limitations are expected to be identified in the future. ([I284fa](https://android-review.googlesource.com/#/q/I284face60a4e5f6942b3d92cac7d47056d8174f3))

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

`androidx.compose.ui:ui-*:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/ui)

**API Changes**

- `NestedScrollSource` enum is replaced by an inline class. ([Ie321b](https://android-review.googlesource.com/#/q/Ie321b5864dc617b2d6382ba5d632e8037dd5c1d5), [b/187055290](https://issuetracker.google.com/issues/187055290))
- `FocusManager.clearFocus(forcedClear = true)` is renamed to `FocusManager.clearFocus(force = true)` ([Ia0c41](https://android-review.googlesource.com/#/q/Ia0c4194d4a70037d6d288a6edd307e033198d98e))
- Refactored enum usages to inline classes to avoid issues with exhaustive when statements when new enum values are added. ([I2b5eb](https://android-review.googlesource.com/#/q/I2b5eb2f04d64d1eccf38557d80e3eef06869c310))
- Remove `@ExperimentalComposeUiApi` from `PopupProperties`. ([I01fa6](https://android-review.googlesource.com/#/q/I01fa6aaf14729bd4bc4d04cc627e2bae87b89a82))
- `PointerType` was changed from an enum to an inline class ([If5058](https://android-review.googlesource.com/#/q/If50588eb1ea4ed4bafbcbd00689e57c09b021232))
- ContentDescription and Text semantics properties are no longer single values but lists. This enables to merge them as they are instead of concatenations. Also provided better testing APIs to utilize these changes ([Ica6bf](https://android-review.googlesource.com/#/q/Ica6bf4236d05b97357c18fb306a6305877a349f7), [b/184825850](https://issuetracker.google.com/issues/184825850))
- `Modifier.focusModifier()` is deprecated and replaced by `Modifier.focusTarget()` ([I6c860](https://android-review.googlesource.com/#/q/I6c860991217cc0c4e7cb35be73207f94669ce607))
- `Modifier.onSizeChanged()` and `Modifier.onGloballyPositioned()` are not inlined functions anymore ([I727f6](https://android-review.googlesource.com/#/q/I727f6622174806efb68b63808b322e6bc86e1cf5), [b/186109675](https://issuetracker.google.com/issues/186109675))
- `KeyboardType` enum is replaced by an inline class. ([I73045](https://android-review.googlesource.com/#/q/I73045de306c082ca8f6b11d44d252d0a63a407d3), [b/187055290](https://issuetracker.google.com/issues/187055290))
- Replaced `FocusState` enum with a `FocusState` interface ([Iccc1a](https://android-review.googlesource.com/#/q/Iccc1a7306fe886969b3a5c74359f53250b3901d9), [b/187055290](https://issuetracker.google.com/issues/187055290))
- ImeAction enum is replaced by an inline class. ([I18be5](https://android-review.googlesource.com/#/q/I18be51ba64f20257859ae634720b367ae7510e33), [b/187055290](https://issuetracker.google.com/issues/187055290))
- `PlaceholderVerticalAlign` is converted into an inline class. ([If6290](https://android-review.googlesource.com/#/q/If6290471c9b2704b746dc5688a08d7492e929570))
- TextUnitType is an inline class now. ([I4cba9](https://android-review.googlesource.com/#/q/I4cba981dfafbd433f157e384ad4e9f3e818e2f87))
- `AnnotatedString.withAnnotation` functions are now ExperimentalTextApi instead of ExperimentalComposeApi. ([I0cd0a](https://android-review.googlesource.com/#/q/I0cd0a64f5e0bf4cd082d479711c014162f27c763))
  - TextUnit constructor with TextUnitType is now ExperimentalTextApi instead of ExperimentalComposeApi.

**Bug Fixes**

- Fixed the bug introduced in beta07 where LazyColumn/Row items were displayed partially after the scroll ([I8c9ac](https://android-review.googlesource.com/#/q/I8c9ac2df59f3183bf6067dd20092a127f16c9e80), [b/188566058](https://issuetracker.google.com/issues/188566058))
- Now `detectDragGesures`, `detectVerticalGestures`, and `detectHorizontalGestures` will consume the position change automatically, no need to call change.consumePositionChange in the onDrag callbacks ([I42fc4](https://android-review.googlesource.com/#/q/I42fc4a6529f73db228ae671097d10a0cda0d834b), [b/185096350](https://issuetracker.google.com/issues/185096350), [b/187320697](https://issuetracker.google.com/issues/187320697))
- LayoutModifiers providing alignment lines was fixed. A bug causing the parent not being remeasured when the alignment lines of the children were changing was fixed. ([I4401f](https://android-review.googlesource.com/#/q/I4401f5f8a86934c935564e88b7446940d8a42c23), [b/174315652](https://issuetracker.google.com/issues/174315652))
- `Modifier.onGloballyPositioned()` was changed to report the coordinates of this modifier in the modifier chain, not the layout coordinates after applying all the modifiers. This means that now the ordering of modifiers is affecting what coordinates would be reported. ([Ieb67d](https://android-review.googlesource.com/#/q/Ieb67da0c327c9dc323a4b0a8bf33dbb66f0611e3), [b/177926591](https://issuetracker.google.com/issues/177926591))

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.ui:ui-*:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/ui)
| **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
| `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

**API Changes**

- Added `ViewRootForInspector` interface for use in inspector ([Ib70df](https://android-review.googlesource.com/#/q/Ib70df2eb3dfe0f205daecfd139e56514d3a2cd28))
- `SubcomposeLayoutState` now supports setting count of reusable slots. The layout will keep up to this count slots active instead of disposing them in order to reuse the slot next time we need a new one ([Ieb981](https://android-review.googlesource.com/#/q/Ieb9817249f5fa77ca12d32fcec2747e79c12565e))
- KeyEventType enum is replaced by an inline class. ([Id670a](https://android-review.googlesource.com/#/q/Id670a0f006c4219bbedef9e4f1b01e703b89cb2d), [b/187055290](https://issuetracker.google.com/issues/187055290))
- `FocusDirection` enum is replaced by an inline class. ([Ib6d03](https://android-review.googlesource.com/#/q/Ib6d03c672268e89eb67b5f3de7c29763872f5686), [b/187055290](https://issuetracker.google.com/issues/187055290), [b/184086802](https://issuetracker.google.com/issues/184086802))
- Introduces ability to hoist the SubcomposeLayout state which allows you to precompose the content into a requires slotId which would make the next measure pass faster as once we try to subcompose with the given slotId next time there will be no composition needed. ([I42580](https://android-review.googlesource.com/#/q/I425806be5ec3e36337e04558e6621fbe515b7cd8), [b/184940225](https://issuetracker.google.com/issues/184940225))
- Added Clip Selection Handle ([Iff80d](https://android-review.googlesource.com/#/q/Iff80d27fbac0e4de5e3e99fac4352cd6ef2cd201), [b/183408447](https://issuetracker.google.com/issues/183408447))
- Removed unused APIs related to LayoutInspector support. ([I2ac78](https://android-review.googlesource.com/#/q/I2ac78567834a4f6f33066aa52c834da5c9b4e1ff))

**Bug Fixes**

- LazyColumn/Row will now keep up to 2 previously visible items active (not disposed) even when they are scrolled out already. This allows the component to reuse the active subcompositions when we will need to compose a new item which improves the scrolling performance. ([Ie5555](https://android-review.googlesource.com/#/q/Ie5555c9a7031dc9bd31f452a0ed9b28d8a337f5f))
- `TextGeomerticTransform` and `TextDecoration` on `AnnotatedString` will be applied as given. ([I61900](https://android-review.googlesource.com/#/q/I61900b749deafc1570dc329a64d1050fd52b20a2), [b/184760917](https://issuetracker.google.com/issues/184760917))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.ui:ui-*:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/ui)

**API Changes**

- Solve Conflict with Navigation Gesture ([I1145e](https://android-review.googlesource.com/#/q/I1145eacbec270abcbb70f8ccb3664609a699ee47))
- `@ComposeCompilerApi` no longer `@RequiresOptIn` ([Iab690](https://android-review.googlesource.com/#/q/Iab6901114e02706221c6f1f2050d372b366ee060))
- Added CollectionInfo and CollectionItemInfo accessibility APIs that allows to mark collection and its items for accessibility services ([Id54ef](https://android-review.googlesource.com/#/q/Id54ef37379e14e41ac52782b40e29de54f95eed0), [b/180479017](https://issuetracker.google.com/issues/180479017))
- Added `SemanticsActions.ScrollToIndex` to scroll a list with indexed items to the item with a certain index, and `SemanticsProperties.IndexForKey` to get the index of an item in a list with keyed items. Both actions are implemented by LazyList.
  - Added `SemanticsNodeInteraction.performScrollToIndex` that scrolls a list to the given index, and `SemanticsNodeInteraction.performScrollToKey` that scrolls a list to the item with the given key. ([I4fe63](https://android-review.googlesource.com/#/q/I4fe63399fb620794651e1973730658877bcfeff4), [b/178483889](https://issuetracker.google.com/issues/178483889), [b/161584524](https://issuetracker.google.com/issues/161584524))
- Added ownerViewId to GraphicLayerInfo ([I19f62](https://android-review.googlesource.com/#/q/I19f62ba250ad53284a6c3fb94c562bf7c86e96c4))
- Added Font() overloads to load fonts from assets, File and FileDescriptor ([I5d382](https://android-review.googlesource.com/#/q/I5d3825e6120f68e7fac8f88c6b69662018175650))
- Added accessibility API `error` that allows to mark a node that contains invalid input ([I12997](https://android-review.googlesource.com/#/q/I129977e3d3b5f03435de41de409fde9029c325b9), [b/180584804](https://issuetracker.google.com/issues/180584804), [b/182142737](https://issuetracker.google.com/issues/182142737))
- Added `Font()` overloads to load fonts from assets, File and FileDescriptor ([I43007](https://android-review.googlesource.com/#/q/I43007da51b8500b57b9d7bb5dec2d00e4f61e2e4))
- AnnotatedString save support to `TextFieldValue.Saver`. Added `addTtsAnnotation` and withAnnotation utility functions to `AnnotatedString.Builder` ([I8cbdc](https://android-review.googlesource.com/#/q/I8cbdcfcdbe167ff7c68c760aebdd8affe2d8434e), [b/178446304](https://issuetracker.google.com/issues/178446304))
- Added TextUnit constructor function `TextUnit(value: Float, type: TextUnitType)` ([I7ecce](https://android-review.googlesource.com/#/q/I7eccedda948c374d0cab1e883a56294aa9007b68), [b/178446304](https://issuetracker.google.com/issues/178446304))

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.ui:ui-*:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/compose/ui)

**API Changes**

- Added experimental `FocusManager.moveFocus(In)` and `FocusManager.moveFocus(Out)` ([Ic5534](https://android-review.googlesource.com/#/q/Ic553490bfde0df10250e0fa30b5fda83898cff61), [b/183746743](https://issuetracker.google.com/issues/183746743))
- Added experimental `performTextInputSelection` API ([I2dcbb](https://android-review.googlesource.com/#/q/I2dcbbbc0178b62c7a290a7e170e00b26b74d7237), [b/178510628](https://issuetracker.google.com/issues/178510628))
- `InputEventCallback` interface is deprecated. It was not possible to use the interface in any public API; and there was no usage of it in the code. ([I34a02](https://android-review.googlesource.com/#/q/I34a0208fac88f99da33ce9c700a803454dfb27c7), [b/184003208](https://issuetracker.google.com/issues/184003208))
- Deprecated `TextLayoutResult/createTextLayoutResult` function. It is an unused public function which was added for testing. The function does not do anything usable for Compose text APIs. The function is now deprecated and will be removed later. ([I80413](https://android-review.googlesource.com/#/q/I8041316a98dfd682ca0a8740fc62c8003a0850be))

**Bug Fixes**

- Fixed `ACTION_SCROLL_FORWARD`, `ACTION_SCROLL_BACKWARD`, `accessibilityActionScrollLeft`, `accessibilityActionScrollUp`, `accessibilityActionScrollRight` and `accessibilityActionScrollDown` accessibility scroll actions. Instead of scrolling to the end of the scrollable, it will now scroll by one screen in the given direction. ([Ieccb0](https://android-review.googlesource.com/#/q/Ieccb0a794d61dc5fe28a236b379755d776c023dc))
- The AndroidManifest files from ui-test-manifest and ui-tooling-data are now compatible with Android 12 ([I6f9de](https://android-review.googlesource.com/#/q/I6f9dec0515ad6eb7fd232eeb124ee0164f4e90cb), [b/184718994](https://issuetracker.google.com/issues/184718994))

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.ui:ui-*:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/ui)

**API Changes**

- Rename `hideSoftwareKeyboard` and `showSoftwareKeyboard` on `SoftwareKeyboardController` to `hide()` and `show()` respectively.
  - Provide the full CompositionLocal interface for LocalSoftwareKeyboardController, allowing it to be set (especially useful in tests) ([I579a6](https://android-review.googlesource.com/#/q/I579a6e311d1cc96e4ea398465cad3a402a633b8d))
- LiveRegion accessibility API is added. If node is marked as a live region, the accessibility services will automatically notify the user about its changes ([Idcf6f](https://android-review.googlesource.com/#/q/Idcf6f425b12b005e59ad77fe7430e466132ea87c), [b/172590946](https://issuetracker.google.com/issues/172590946))
- TextOverflow.Visible is introduced. ([Ic8f89](https://android-review.googlesource.com/#/q/Ic8f898df15fa7cfa3fadf5a47d5b0e34a68f52f6))

**Bug Fixes**

- Fixed the issue when items of `LazyColumn`/`LazyRow` located on the edges were incorrectly positioned after fast fling ([Ie4d13](https://android-review.googlesource.com/#/q/Ie4d13def7dc4b12d4f52b4c5edbb0abb5150f698), [b/183877420](https://issuetracker.google.com/issues/183877420))
- `AndroidViewBinding` now properly removes fragments inflated via `FragmentContainerView` when the `AndroidViewBinding` is removed from the compose hierarchy. ([Ib0248](https://android-review.googlesource.com/#/q/Ib02480f78570972b3190ebd45ab12f4d7291fa23), [b/179915946](https://issuetracker.google.com/issues/179915946))
- `AndroidViewBinding` now correctly nests fragments inflated via `FragmentContainerView` when your `ComposeView` is within a `Fragment`, fixing issues with saving and restoring the state of those fragments. ([I70eb0](https://android-review.googlesource.com/#/q/I70eb0831fb6b756e2968e713e181193969d49b9a), [b/179915946](https://issuetracker.google.com/issues/179915946))
- Compose ViewBinding now depends on [Fragment `1.3.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.2) and now consistently shows fragments inflated via `FragmentContainerView` after configuration changes. ([I0743d](https://android-review.googlesource.com/#/q/I0743d383564ee28429ad0074f58de79c0e98ada0), [b/179915946](https://issuetracker.google.com/issues/179915946))

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.ui:ui-*:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/ui)

**API Changes**

- Deferred check for ViewTree dependencies of ComposeView ([I8dbbf](https://android-review.googlesource.com/#/q/I8dbbf72f5646a6420c41995cc38732bce6b53d55), [b/182466548](https://issuetracker.google.com/issues/182466548))
- Added optional `startX`/`endX` and `startY`/`endY` parameters to `swipeUp`/`swipeDown`/`swipeLeft`/`swipeRight` functions in `GestureScope`. ([I49e2d](https://android-review.googlesource.com/#/q/I49e2d463a3cf71668a95ca9ebf9355905b6f352e), [b/182063305](https://issuetracker.google.com/issues/182063305))

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.ui:ui-*:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/ui)

**API Changes**

- Added new `LocalSoftwareKeyboardController` composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I5951e](https://android-review.googlesource.com/#/q/I5951e802fbec7c26862b976de64b78640accd1f7), [b/168778053](https://issuetracker.google.com/issues/168778053))
- Added new `LocalSoftwareKeyboardController` composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I84472](https://android-review.googlesource.com/#/q/I84472a517db4b15345302346c967e7c6b359109b), [b/168778053](https://issuetracker.google.com/issues/168778053))
- Removed the following `SemanticsMatcher`s:
  - `hasWidth(width, tolerance)`
  - `hasHeight(height, tolerance)`
  - `hasLeftPosition(left, tolerance)`
  - `hasTopPosition(top, tolerance)`
  - `hasRightPosition(right, tolerance)`
  - `hasBottomPosition(bottom, tolerance)` ([If16bd](https://android-review.googlesource.com/#/q/If16bd0ec44dd7d3462cad13578fa5f798ec3ab96))
- Marked the following `SemanticsMatchers` as @ExperimentalTestApi:
  - `hasWidth(width, tolerance)`
  - `hasHeight(height, tolerance)`
  - `hasLeftPosition(left, tolerance)`
  - `hasTopPosition(top, tolerance)`
  - `hasRightPosition(right, tolerance)`
  - `hasBottomPosition(bottom, tolerance)` ([Ia600c](https://android-review.googlesource.com/#/q/Ia600c2aed8a4570927306bcafa8ed98ce53ce26d))
- Added the following `SemanticsMatcher`s:
  - `hasWidth(width, tolerance)`
  - `hasHeight(height, tolerance)`
  - `hasLeftPosition(left, tolerance)`
  - `hasTopPosition(top, tolerance)`
  - `hasRightPosition(right, tolerance)`
  - `hasBottomPosition(bottom, tolerance)` ([I2f502](https://android-review.googlesource.com/#/q/I2f5021f77a1bb827435709354688d0f7be285a92))

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))
- `androidx.compose.ui:ui` no longer depends on AppCompat or Fragment. If you are using a ComposeView in your application, and you are using Fragment and/or AppCompat, make sure that you are using AppCompat 1.3+ / Fragment 1.3+ - these versions are needed to correctly set lifecycle and saved state owners required for ComposeView. ([I1d6fa](https://android-review.googlesource.com/#/q/I1d6fa61deebc7771082d19a8268bd37b5f99194d), [b/161814404](https://issuetracker.google.com/issues/161814404))
- Fix for broken `rememberSaveable { mutableStateOf(0) }` when used inside a destination of navigation-compose. ([I1312b](https://android-review.googlesource.com/#/q/I1312b5b210dde32250945d164a2f3a1b574cb0a8), [b/180042685](https://issuetracker.google.com/issues/180042685), [b/180701630](https://issuetracker.google.com/issues/180701630))
- Added new `LocalSoftwareKeyboardController` composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I658b6](https://android-review.googlesource.com/#/q/I658b6bfc5c917db486c631312e3456469a615831), [b/168778053](https://issuetracker.google.com/issues/168778053))
- Fixed rare NoSuchElementException in `ComposeRootRegistry`'s `tearDownRegistry()` ([Iddce1](https://android-review.googlesource.com/#/q/Iddce1d32c69427846cd114bcb15f63807ee575f9))

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.ui:ui-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/ui)

This is the first release of Compose 1.0.0 Beta.

**API Changes**

- onStart callback has been added to `detectDragGestures` ([I67269](https://android-review.googlesource.com/#/q/I6726950322c7a3390fc79c630919b002bf7059eb), [b/179995594](https://issuetracker.google.com/issues/179995594))
- Modifiers for sizing to intrinsics are no longer experimental. ([I15744](https://android-review.googlesource.com/#/q/I15744bc96d9c9a94747901e47100fdea25e28742))
- MeasureBlocks was renamed to MeasurePolicy which became a fun interface. Layout APIs were updated / simplified to use MeasurePolicy. ([Icab48](https://android-review.googlesource.com/#/q/Icab485f5b5965261ce9f9d696d4c225ec158f072), [b/167662468](https://issuetracker.google.com/issues/167662468), [b/156751158](https://issuetracker.google.com/issues/156751158))
- `InteractionState` has been replaced with `[Mutable]InteractionSource`
  - Interfaces are responsible for emitting / collecting Interaction events.
  - Instead of passing `interactionState = remember { InteractionState() }` to components such as `Button` and `Modifier.clickable()`, use `interactionSource = remember { MutableInteractionSource() }`.
  - Instead of: `Interaction.Pressed in interactionState` you should instead use the extension functions on InteractionSource, such as InteractionSource.collectIsPressedAsState().
  - For complex use cases you can use InteractionSource.interactions to observe the stream of Interactions. See the InteractionSource documentation and samples for more information.
  - ([I85965](https://android-review.googlesource.com/#/q/I85965d0dba39d1740c097915d1d1a367eea2a78c), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/171913923](https://issuetracker.google.com/issues/171913923), [b/171710801](https://issuetracker.google.com/issues/171710801), [b/174852378](https://issuetracker.google.com/issues/174852378))
- Add AccessibilityMananger interface and LocalAccessibilityMananger in CompositionLocals ([I53520](https://android-review.googlesource.com/#/q/I5352073036978c367161e5c2f7cb3402dd502a65))
- Removed deprecated LayoutCoordinates methods, use function instead of the property for positionInParent and boundsInParent ([I580ed](https://android-review.googlesource.com/#/q/I580edba74283600c3aafba6130a7af806df7d6c5), [b/169874631](https://issuetracker.google.com/issues/169874631), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Typealiases replaced by underlying types:
  - `ColorStop` is now `Pair<Float, Color>`
  - `SpanStyleRange` is now \`AnnotatedString.Range
  - `ParagraphStyleRange` is now `AnnotatedString.Range<ParagraphStyle>`
  - `StringAnnotation` is now `AnnotatedString.Range<String>`
  - ([I8dd1a](https://android-review.googlesource.com/#/q/I8dd1aac90dc4193ec46e29a256c9f7b5bde15073))
- Created new TextInputSession for input sessions from low level text components such as CoreTextField. ([I8817f](https://android-review.googlesource.com/#/q/I8817f81e7c1b0066795ecb4af3674e99413362d0), [b/177662148](https://issuetracker.google.com/issues/177662148))
- Placeable now exposes measuredSize, representing the size which the child layout actually measured to. This size might not respect the measurement constraints. ([Ib2729](https://android-review.googlesource.com/#/q/Ib2729a2323f67d5e50248dbfa234394fb3d7ee71), [b/172560206](https://issuetracker.google.com/issues/172560206), [b/172338608](https://issuetracker.google.com/issues/172338608))
- Add selectionGroup modifier that allows to mark collection of Tabs or RadioButtons for accessibility purposes ([Ie5c29](https://android-review.googlesource.com/#/q/Ie5c29bc1cc0630f4f3a68ff57ebd94464c89ffd7))
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
- Deprecated methods from ui modules were removed ([I646f6](https://android-review.googlesource.com/#/q/I646f625da9289a48364903e0de0b02a78d8769ea))

- Size modifiers were renamed. Modifier.width/height/size were renamed to requiredWidth/requiredHeight/requiredSize. Modifier.preferredWidth/preferredHeight/preferredSize were renamed to width/height/size. ([I5b414](https://android-review.googlesource.com/#/q/I5b4145953d360b1fb851c0056fc9a7875bb34088))

- `Modifier.tapGestureFilter` has been removed. Use `Modifier.pointerInput { detectTapGestures(...) }` instead. ([I266ed](https://android-review.googlesource.com/#/q/I266ed741ca484924409a4a3a7d5afbbfffbd66d3), [b/175294473](https://issuetracker.google.com/issues/175294473))

- partial consumption was removed from pointer input system. The recommended way of coordinating partial consumtion is Modifier.nestedScroll. ([Ie9c9b](https://android-review.googlesource.com/#/q/Ie9c9b7c6f5da9a47c803b06985f45eb7df5552f2))

- Orientation has been moved to foundation package. VelocirtTracker moved from ui.gesture to ui.input.pointer. ([Iff4a8](https://android-review.googlesource.com/#/q/Iff4a887648735c4850dca0d8d95fd99d782d04bb), [b/175294473](https://issuetracker.google.com/issues/175294473))

- imageResource and vectorResource are now extension functions
  on ImageBitmap and ImageVector companions respectively.
  `load{Image,Vector,Font}Resource` functions have been deleted. ([I89130](https://android-review.googlesource.com/#/q/I89130cd429dfcbe54995d667d3501e3363851bce))

- AnimationClockObservable and subclasses have been
  removed. AnimatedFloat has been removed. ([Icde52](https://android-review.googlesource.com/#/q/Icde5248072620b741bdf4d8cf59291e7b2994e6a), [b/177457083](https://issuetracker.google.com/issues/177457083))

- Providers has been renamed to CompositionLocalProvider

  - The Composition constructor no longer accepts a key parameter, and has been deprecated.
  - currentCompositeKeyHash has been turned into a composable top level property instead of a composable top level function.
  - CompositionData and CompositionGroup have been moved to the androidx.compose.runtime.tooling namespace
  - ComposableLambda has been made an interface instead of a concrete class, and no longer has type parameters.
  - ComposableLambdaN has been made an interface instead of a concrete class, and no longer has type parameters.
  - The snapshotFlow function has been moved to the androidx.compose.runtime namespace
  - the merge method of SnapshotMutationPolicy is no longer experimental
  - The @TestOnly top level clearRoots function has been removed. It is no longer necessary.
  - keySourceInfoOf and resetSourceInfo functions have been removed. They are no longer necessary.
  - Composer.collectKeySourceInformation has been removed. It is no longer necessary.
  - isJoinedKey, joinedKeyLeft, and joinedKeyRight methods have been removed. They are no longer necessary.
  - Various top level APIs have been moved and reorganized into different files. Due to Kotlin's file class semantics, this will break binary compatibility but not source compatibility, so should not be an issue for most users.
  - ([I99b7d](https://android-review.googlesource.com/#/q/I99b7de8ea0fb5d73a0ee4667a65e35d976383831), [b/177245490](https://issuetracker.google.com/issues/177245490))
- `ComponentActivity.setContent()` was removed from compose:ui. Use the one from `androidx.activity:activity-compose:1.3.0-alpha01`.
  `viewModel()` and `LocalViewModelStoreOwner` were removed from compose:ui. Use the ones from `androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha01` ([I6f36b](https://android-review.googlesource.com/#/q/I6f36bd5a462fd80344b819e1c94cd180dd42543f))

- Modifier.scrollable has been reworked. Now it uses Scrollable interface instead of ScrollableController class ([I4f5a5](https://android-review.googlesource.com/#/q/I4f5a5189b90cdff631ffb7166ce2e847b92db205), [b/174485541](https://issuetracker.google.com/issues/174485541), [b/175294473](https://issuetracker.google.com/issues/175294473))

- CustomEvens support from PointerInputModifier has been removed ([I02707](https://android-review.googlesource.com/#/q/I0270780d7b8e6fddaf76f49194713d8eb2b44452), [b/175294473](https://issuetracker.google.com/issues/175294473))

- SnapshotStateObserver is not Experimental anymore ([Id2e6a](https://android-review.googlesource.com/#/q/Id2e6a2eaac801b2eb9ef3fcacfdadb679ffbffab))

- Deleted some previously deprecated APIs ([Ice5da](https://android-review.googlesource.com/#/q/Ice5dae36591015a9d905b84b26cc02662385d831), [b/178633932](https://issuetracker.google.com/issues/178633932))

- longPressGestureFilter and doubleClickGestureFilter have been removed. use Modifier.pointerInput with helper functions e.g detectTapGestures ([I2fedf](https://android-review.googlesource.com/#/q/I2fedf3814840157c278cd91988da3c5ab493c9eb), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Removed String.format API
  refactored usages in various
  toString methods to not leverage
  String.format internally. ([Id1290](https://android-review.googlesource.com/#/q/Id129075536ea21528dab0cf4fc5816563f9b8d4b))

- Removed dp assertions ([I798d2](https://android-review.googlesource.com/#/q/I798d2f7dbd5e687d8e1fb059f153cdc8150d8d27))

- Removed androidx.compose.runtime:runtime-dispatch ([I55feb](https://android-review.googlesource.com/#/q/I55febbec89c3dfb6cd5a57d30a098580eac303e7))

- Text actions now check focus automatically ([I13777](https://android-review.googlesource.com/#/q/I13777ef805c71674b929577a3b794d655948da3f), [b/179648629](https://issuetracker.google.com/issues/179648629))

- Removed `runBlockingWithManualClock` ([I15cdc](https://android-review.googlesource.com/#/q/I15cdc97a742c764cae3b332ad52143c07f32b9bd), [b/179664814](https://issuetracker.google.com/issues/179664814))

- Scroll position in Modifier.verticalScroll()/horizontalScroll() is represented with Ints now ([I81298](https://android-review.googlesource.com/#/q/I81298a8767a421293ca7d5ab33ce8373e63f383c))

- FlingConfig has been renamed to FlingBehavior now allows for customization of suspend animation rather than predefined Decays. ([I02b86](https://android-review.googlesource.com/#/q/I02b8639c646d24fd19ef7ac504ef6660b8906d54), [b/175294473](https://issuetracker.google.com/issues/175294473))

- Added a helper function that is helpful to
  set the same action for all ImeAction callbacks ([I63447](https://android-review.googlesource.com/#/q/I63447afe1302a01b9c8a8480482d27920858bc4b), [b/179226323](https://issuetracker.google.com/issues/179226323))

- Removed SoftwareKeyboardController callback from all text
  fields to be replaced by a new API shortly. ([Iae869](https://android-review.googlesource.com/#/q/Iae869e91c48300f4ab926dac2578d2d759f5fd89), [b/168778053](https://issuetracker.google.com/issues/168778053))

- FontSpan and FontWeigthStyleSpan are no longer used and removed. ([Ie5b56](https://android-review.googlesource.com/#/q/Ie5b5611883bc6a44577ae47572754f3d988526ba), [b/177423444](https://issuetracker.google.com/issues/177423444))

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

**Bug Fixes**

- Added API to use AnimatedVectorDrawable resources in Compose. Use animatedVectorResource to load an `<animated-vector>` XML as an AnimatedImageVector and animate it with painterFor ([I8ea91](https://android-review.googlesource.com/#/q/I8ea919f97faf6a45183065e2948a169063f17c8a))
- Added new LocalSoftwareKeyboardController composition local API to replace previous SoftwareKeyboardController interface on TextField. ([I658b6](https://android-review.googlesource.com/#/q/I658b6bfc5c917db486c631312e3456469a615831), [b/168778053](https://issuetracker.google.com/issues/168778053))

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.ui:ui-*:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/ui)
| **Note:** An issue was found in Activity Compose that causes a `NoSuchMethodError: No static method setContent` exception to be thrown by default for Apps that depend on either `androidx.compose.ui:ui-tooling:1.0.0-alpha12` or `androidx.compose.ui:ui-test-junit4:1.0.0-alpha12`, or internally use `setContent` ([b/179911234](https://issuetracker.google.com/issues/179911234)). To fix, add a dependency on [`androidx.activity:activity-compose:1.3.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.3.0-alpha02).

**API Changes**

- Support for ViewGroups was removed from UiApplier. The Deprecated emitView composables were removed. ([Ifb214](https://android-review.googlesource.com/#/q/Ifb2141153189ac4b0fbd748a23c3de38ed155af7))
- Modifier.pointerInput now requires remember keys to indicate when the pointer input detection coroutine should restart for new dependencies. ([I849cd](https://android-review.googlesource.com/#/q/I849cd63912b2d4c86ebe0dd24a7d0e2eb7a4e6d1))
- CompositionReference renamed to CompositionContext ([I53fcb](https://android-review.googlesource.com/#/q/I53fcb2d87d57c95c293108bf80e54c7d17064f24))
- Bounds has been renamed to DpRect ([I4b32a](https://android-review.googlesource.com/#/q/I4b32a75caa8a5e8a1b5a0051f9041855411876e4))
- Testing update: hasText() will check for both input and label/hint/placeholder texts in the text field ([Iab803](https://android-review.googlesource.com/#/q/Iab8030e3c98f05bd6f0ffaf203b8c15acab513bb))
- viewModel() composable and LocalViewModelStoreOwner were moved to androidx.lifecycle.viewmodel.compose. You will now need to add a separate dependency androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha01 in order to use it. ([I7a374](https://android-review.googlesource.com/#/q/I7a374b76168a6387e585337c131a988bddcb912b))
- Allow nullable action in AccessibilityAction, change action label in AccessibilityAction and CustomAccessibilityAction from CharSequence to String ([I0dc82](https://android-review.googlesource.com/#/q/I0dc82f11f78ebe89be161727feed53e1c2390b72))
- In order to better match naming conventions with ImageBitmap and ImageVector, ImagePainter has been renamed to BitmapPainter to parallel VectorPainter. ([Iba381](https://android-review.googlesource.com/#/q/Iba3810ae5cfd6f57442154c93eec500f35ba4ad5), [b/174565889](https://issuetracker.google.com/issues/174565889))
- Better substring test APIs with substring now as an argument ([Icbe78](https://android-review.googlesource.com/#/q/Icbe78369fe75bc01bfcfa25b8e9ee2ad148fdb96))
- Added an `Modifier.focusOrder()` that accepts a FocusRequester without specifying a custom focus order a lambda. This is useful when we only need to specify a reference but not a custom focus order for a composable ([I4f52a](https://android-review.googlesource.com/#/q/I4f52aa4697d6c7d23b7aa4f49719e2eb55302920), [b/179180978](https://issuetracker.google.com/issues/179180978))
- ComponentActivity.setContent has moved to androidx.activity.compose.setContent in the androidx.activity:activity-compose module. ([Icf416](https://android-review.googlesource.com/#/q/Icf4168e6078b87ce746569a946b2a90274197c72))
- Destructuring and copy() methods have been removed from several classes where they were rarely used. ([I26702](https://android-review.googlesource.com/#/q/I267021d3a45314acc9a169f6bbdfbfb4295a448c), [b/178659281](https://issuetracker.google.com/issues/178659281))
- Moved Popup to be platform specific. AndroidPopupProperties has been renamed to PopupProperties, and `isFocusable` has been moved to a `focusable` parameter in `PopupProperties` ([Ieeea5](https://android-review.googlesource.com/#/q/Ieeea528d395b4bb37834345e4a06c36eed0ce231))
- Moved Dialog to be platform specific. Renamed AndroidDialogProperties to DialogProperties. ([I4ef69](https://android-review.googlesource.com/#/q/I4ef69bc957d579c7d5566bb749057cbde807d6a5), [b/179138130](https://issuetracker.google.com/issues/179138130))
- Made LayoutNode internal ([I8a7b1](https://android-review.googlesource.com/#/q/I8a7b11b17c33e94b707692b208d15026510f3031), [b/175103944](https://issuetracker.google.com/issues/175103944))
- Constraints.enforce was replaced with Constraints.constrain. ([I8b8ea](https://android-review.googlesource.com/#/q/I8b8ea7898b09ccaa411b9b6ef20a16523e8ba029))
- loadFontResource is deprecated. Use fontResource instead. imageResource, loadImageResource, vectorResource, and loadVectorResource are deprecated. Use painterResource instead. ([I6b809](https://android-review.googlesource.com/#/q/I6b8096508b2280ca49c70a432c5497f386dc570e))
- For performance reasons, ScrollAxisRange semantics now takes lambdas returning Floats instead of direct Float values. ([If4a35](https://android-review.googlesource.com/#/q/If4a353ef9ac511ce77cf334ccf9a589ecadcac56), [b/178657186](https://issuetracker.google.com/issues/178657186))
- Added EditableText semantics to mark editable input text of the text field for accessibility and corresponding test methods to check the semantics ([I8e07a](https://android-review.googlesource.com/#/q/I8e07ab8a8f29d5c2a31fb1c979e099303083a38f))
- Made OwnerLayer/OwnerScope/OwnerSnapshotObserver internal ([I4ffaf](https://android-review.googlesource.com/#/q/I4ffafd0d9eaa5204200941609944d540934403e1), [b/175103944](https://issuetracker.google.com/issues/175103944))
- toIntPx() was renamed to roundToPx(). ([I9b7e4](https://android-review.googlesource.com/#/q/I9b7e460fb4b6e72ba65cdd8f5d1165c306461773), [b/173502290](https://issuetracker.google.com/issues/173502290))
- IntBounds was renamed to IntRect and the API was improved. ([I1f6ff](https://android-review.googlesource.com/#/q/I1f6ff3831e502856f1550ede9c367bf05c5a51b1))
- Snapshot API was updated to be more consistent with API guideline as well as hiding internal implementation classes from the public API. ([Id9e32](https://android-review.googlesource.com/#/q/Id9e32c885473f09cd69354a4c87a2c57c5f86533))
- Added expand and collapse semantics actions. Added expand and halfExpand in ModalBottomSheetState ([Ib5064](https://android-review.googlesource.com/#/q/Ib50644cb5d591f9c3a58b4d35da064341ac7253c))
- Modifier.dragGestureFilter has been deprecated. Use `Modifier.pointerInput { detectDragGestures (...)}` instead. Alternatively, use Modifier.draggable for one axis drags ([I0ba93](https://android-review.googlesource.com/#/q/I0ba93559f565fc2a277f322e53dce9df9855ea46), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Renamed Ambients to match the Ambient -\> CompositionLocal rename. Ambients used to be named AmbientFoo, now CompositionLocals are named LocalFoo. ([I2d55d](https://android-review.googlesource.com/#/q/I2d55d1c5c38a08b04e72a569d3079db4feca1bf7))
- The deprecated BaseTextField is now removed. Use BasicTextField instead. ([I71368](https://android-review.googlesource.com/#/q/I71368dafbe218764095e841e314c75278794a389))
- Selection was moved to foundation. ([I7892b](https://android-review.googlesource.com/#/q/I7892b8be5d2f91849f8ecc2e1034e0a8277bb61c))
- Similarly to how we previously removed `state { 0 }` composable and now promote usage like `remember { mutableStateOf(0) }` we are going to remove `savedInstanceState { 0 }` composable. You should use `rememberSaveable { mutableStateOf(0) }` instead and it will save and restore automatically if the type used inside the MutableState can be stored in the Bundle. If previously you were passing a custom saver object now you need to use a new overload of rememberSaveable which has `stateSaver` parameter. The usage will look like this: `val holder = rememberSaveable(stateSaver = HolderSaver) { mutableStateOf(Holder(0)) }` ([Ib4c26](https://android-review.googlesource.com/#/q/Ib4c266902d166f119ea1770cccbc78ac25a54ff7), [b/177338004](https://issuetracker.google.com/issues/177338004))
- Added password semantics for accessibility ([I231ce](https://android-review.googlesource.com/#/q/I231ce1c1e9c781c8ec8fda5536d8a0588d68755d))
- Added ProgressBarRangeInfo.Indeterminate to mark indeterminate progress bars for accessibility ([I6fe05](https://android-review.googlesource.com/#/q/I6fe052ba60861d64f31963507ff11e95f3331d89))
- `emptyContent()` and `(@Composable () -> Unit).orEmpty()` utilities have been deprecated as they no longer have any positive performance impact or value ([I0484d](https://android-review.googlesource.com/#/q/I0484d3ef439993d05eea86e53f05997eced590ab))
- `snapshotFlow` and `withMutableSnapshot` are no longer experimental ([I6a45f](https://android-review.googlesource.com/#/q/I6a45fac62267a318481e9a3ba8a3acf3162219f6))
- Recomposers can now be closed. Closed recomposers will continue recomposition until composition child coroutines complete. Recomposer.shutDown renamed to cancel to contrast with close. ([Ib6d76](https://android-review.googlesource.com/#/q/Ib6d766b91381ee45af41a14b7951c48f794f0a90))
- UiSavedStateRegistry was renamed to SaveableStateRegistry, AmbientUiSavedStateRegistry was renamed to AmbientSaveableStateRegistry and both moved to androidx.compose.runtime.saveable package. ([I30224](https://android-review.googlesource.com/#/q/I30224b3f671d01d6a2ae30a80405a69067e76838))
- Artefact androidx:compose:runtime:runtime-saved-instance-state was renamed to androidx:compose:runtime:runtime-saveable ([I6dcac](https://android-review.googlesource.com/#/q/I6dcac2489cf4ec4f17b8ce73bba6eab955a54c6d))
- Many longstanding deprecated APIs in the ui package are deleted. ([I2f2dc](https://android-review.googlesource.com/#/q/I2f2dcaf64fe719c6f2387202f3d0a5699d892657))
- The compose:runtime-dispatch artifact is now deprecated. MonotonicFrameClock can now be found in compose:runtime and AndroidUiDispatcher can be found in compose:ui. ([Ib5c36](https://android-review.googlesource.com/#/q/Ib5c36a427306eceac4b9b16b52a091e864e5b936))
- Outline.\* classes are not data classes anymore ([I4879e](https://android-review.googlesource.com/#/q/I4879e118a767e2fbe2d3272abca4696a9b5b5cdd), [b/178001427](https://issuetracker.google.com/issues/178001427))
- Removed `view.captureToImage()` without any replacement. ([I7fcd2](https://android-review.googlesource.com/#/q/I7fcd2ef813209aa11ec459374fd9a671b1a9d63a))
- Introduced ColorMatrix API used to modify rgb values of source content Refactored ColorFilter API to be an interface and match the implementation of PathEffect. ([Ica1e8](https://android-review.googlesource.com/#/q/Ica1e88332eb005e185e3da2ec95aff33440aa51d))
- Add layoutDirection param to Shape's createOutline. This allows to create layout direction aware shapes. ([I57c20](https://android-review.googlesource.com/#/q/I57c20c45978b5468556159966bd9836653a2e40d), [b/152756983](https://issuetracker.google.com/issues/152756983))
- onImeActionPerformed is deprecated. use KeyboardActions instead ([If0bbd](https://android-review.googlesource.com/#/q/If0bbda1241018d4c19b5df3cd1811c38cce4a76d), [b/179071523](https://issuetracker.google.com/issues/179071523))
- Introduced an `InfiniteAnimationPolicy` coroutine context element that will be applied in infinite animations. By default no policy is installed, except when running tests with `ComposeTestRule`. ([I50ec4](https://android-review.googlesource.com/#/q/I50ec421d7db495459a61c9282dbc2bfbc1f1ad02), [b/151940543](https://issuetracker.google.com/issues/151940543))
- canDrag has been removed from the Modifier.scrollable. ([Id66e7](https://android-review.googlesource.com/#/q/Id66e70ac186ffbdd05e2a62af26c7a41e85f02e9), [b/175294473](https://issuetracker.google.com/issues/175294473))
- Renamed LayoutCoordinates.parentCoordinates to LayoutCoordinates.parentLayoutCoordinates to allow for a new parentCoordinates property. The parentCoordinates property now offers the parent modifier's LayoutCoordintes. This will make for more complete use cases for onSizeChanged() and onGloballyPositioned() ([Idfbfd](https://android-review.googlesource.com/#/q/Idfbfd3012d88b8661b097cb50e4554f2b73f3b64), [b/177926591](https://issuetracker.google.com/issues/177926591))
- tapGestureFilter, doubleTapGestureFilter, longPressGestureFilter and pressIndicaitonGestureFilter have been deprecated. Use Modifier.clickable or Modifier.pointerInput with detectTapGestures function instead. ([I6baf9](https://android-review.googlesource.com/#/q/I6baf95f881b6fa6890ca1d065d49fef3e27bce83), [b/175294473](https://issuetracker.google.com/issues/175294473))
- SaveableStateRegistry's unregisterProvider was removed. Instead registerProvider() now returns SaveableStateRegistry.Entry object which you can use to unregister ([Ic4274](https://android-review.googlesource.com/#/q/Ic42741cecc67ce93cc097f01f7196110e2fff09d), [b/178583739](https://issuetracker.google.com/issues/178583739))
- rememberSavedInstanceState() was renamed to rememberSaveable() and moved to androidx.compose.runtime.saveable package. ([I1366e](https://android-review.googlesource.com/#/q/I1366e7fef0a5a56a43d6eeb3770967a9bf683380), [b/177338004](https://issuetracker.google.com/issues/177338004))
- Removed CoreText and CoreTextField from public API
  - Removed deprecated SelectionContainer overload
  - ([I99c19](https://android-review.googlesource.com/#/q/I99c199c4f9055da1e668d9d799ef11c90239df5b))
- Tests in which Compose is used in hierarchies that are added/removed directly to the WindowManager are now more stable. ([Ie81ed](https://android-review.googlesource.com/#/q/Ie81ed2a14d183b3d5cab594302e86261c8db2379), [b/175765614](https://issuetracker.google.com/issues/175765614))
- Removed Recomposer.current(). \[Abstract\]ComposeView now default to lazily created, window-scoped Recomposers driven by the ViewTreeLifecycleOwner for the window. Recomposition and withFrameNanos-based animation ticks are paused while the host Lifecycle is stopped. ([I38e11](https://android-review.googlesource.com/#/q/I38e11565b2fc776966b6b6984aceafd8a1e6fed1))
- Recomposer.runningRecomposers now offers a global StateFlow of read-only RecomposerInfo for observing ongoing composition state in the process. Prefer this API to Recomposer.current(), which is now deprecated. ([If8ebe](https://android-review.googlesource.com/#/q/If8ebe3959cfe71682ad372382d3b720035ef1605))
- Saver, listSaver(), mapSaver(), autoSaver was moved from androidx.compose.runtime.savedinstancestate to androidx.compose.runtime.saveable ([I77fe6](https://android-review.googlesource.com/#/q/I77fe618aa5e124891b84973d8b8b12735f9f909e))
- EditCommands accept AnnotatedString. However this is an API only change and multi-style text editing is not implemented yet. ([I4c3ea](https://android-review.googlesource.com/#/q/I4c3eaf53926b558759da95d498a07bc636ba4336))
- Uptime and Duration have been removed. ([Ib9bf4](https://android-review.googlesource.com/#/q/Ib9bf443043fdcc8ed2b27666b301d52fb3064d65), [b/177420019](https://issuetracker.google.com/issues/177420019))
- CompositionData.asTree() and related APIs moved to separate ui-tooling-data module and marked as experimental ([Ic95b8](https://android-review.googlesource.com/#/q/Ic95b89456b04b25ef41b8157a72511d10aca09cc))
- Parameters on RounderCornerShape, CutCornerShape and CornerBasedShape were renamed from left/right to start/end in order to support the shape's auto mirroring in the rtl direction. AbsoluteRounderCornerShape and AbsoluteCutCornerShape were introduced for the cases when auto-mirroring is not desired. ([I61040](https://android-review.googlesource.com/#/q/I61040b7bba950191361af89ff4c736ef6cb56235), [b/152756983](https://issuetracker.google.com/issues/152756983))
- The API the Compose compiler plugin targets
  has been refactored to use an interface instead of a
  concrete class. The interface also no longer uses
  a type parameter.

  This is an internal change that should not effect source
  code compatibility but is a binary breaking change. ([I3b922](https://android-review.googlesource.com/#/q/I3b9229969aa70138bc57f5e8498602f5b2dba1e6), [b/169406779](https://issuetracker.google.com/issues/169406779))
- Remove unintentionally public StringBuilder.deleteAt function ([Id6ed9](https://android-review.googlesource.com/#/q/Id6ed95e2e42ca664c13c79032f3276f1037f7625))

**Bug Fixes**

- ComposeViews placed in view hierarchies that are children of another composition now host child compositions of their ancestors ([I92883](https://android-review.googlesource.com/#/q/I92883a1532c4166de8d3551fc342b0533325375d))
- Updated compose's imageFromResource API to reuse the resource drawable cache when loading ImageBitmap objects. ([If3627](https://android-review.googlesource.com/#/q/If3627edded04b55794aede912b7e698abbcad7e6), [b/178751994](https://issuetracker.google.com/issues/178751994))

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.ui:ui-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/ui)

**API Changes**

- WithConstraints was reworked as BoxWithConstraints and moved to foundation.layout. ([I9420b](https://android-review.googlesource.com/#/q/I9420b9e0fbea7ee048b23a6ef328165bbb11e8a8), [b/173387208](https://issuetracker.google.com/issues/173387208))
- Key.DPadUp is deprecated. Use Key.DirectionUp instead. ([Iab335](https://android-review.googlesource.com/#/q/Iab3358b1d0172731601009df117974ca02d2e5a6), [b/177954892](https://issuetracker.google.com/issues/177954892))
- Owner interface from now on internal. ([If8e35](https://android-review.googlesource.com/#/q/If8e354bd05ef6227abf5ac0765619332752ca8e1))
- Added FocusManager.moveFocus() API to move focus programmatically. ([I045cb](https://android-review.googlesource.com/#/q/I045cb347ad697c00cffbd97988df4fd8b6179527), [b/177681839](https://issuetracker.google.com/issues/177681839))
- Changes PopupPositionProvider to use window-relative coordinates, not global coordinates. Renames parentGlobalBounds to anchorBounds, and changes windowGlobalBounds to be windowSize: IntSize ([I2994a](https://android-review.googlesource.com/#/q/I2994a280d3d5c2eafa3a7027f7df5403acaa9cc9))
- Duration and Uptime will be replace with Long milliseconds, and this step removes the dependency of pointer input on those classes. ([Ia33b2](https://android-review.googlesource.com/#/q/Ia33b2d6835861501019481b388cb2c99441c346c), [b/175142755](https://issuetracker.google.com/issues/175142755), [b/177420019](https://issuetracker.google.com/issues/177420019))
- AmbientSavedStateRegistryOwner was added similarly to already existing AmbientLifecycleOwner and AmbientViewModelStoreOwner ([I9a3e8](https://android-review.googlesource.com/#/q/I9a3e829262e30c950ac07dfc4f89eeda632a729f), [b/176756365](https://issuetracker.google.com/issues/176756365))
- Updated vector graphics API to support parsing of tinting applied to the root of vector graphics. ([Id9d53](https://android-review.googlesource.com/#/q/Id9d53298227fdce798db2968f79d1d27c57c1312), [b/177210509](https://issuetracker.google.com/issues/177210509))
- Added toolType to PointerInputChange to differentiate devices ([Iac787](https://android-review.googlesource.com/#/q/Iac78769d346a4a29be581cec54ab380d4901452e), [b/175142755](https://issuetracker.google.com/issues/175142755))
- AmbientWindowManager is renamed to AmbientWindowInfo ([I2686a](https://android-review.googlesource.com/#/q/I2686a353413875efef5899b1122b75d12ee43af6), [b/177084714](https://issuetracker.google.com/issues/177084714), [b/177084983](https://issuetracker.google.com/issues/177084983))
- Deprecated global coordinates methods and made new window-based coordinates methods. ([Iee284](https://android-review.googlesource.com/#/q/Iee284dee7dbc4226493feb144d446a0289b7c83e))
- Added Modifier.toolingGraphicsLayer which adds a graphics layer modifier when inspection is turned on. ([I315df](https://android-review.googlesource.com/#/q/I315df592b0903a783dcd48deff73f31beb63b56c))
- FocusRequester.createRefs is now marked as experimental as it might change. ([I2d898](https://android-review.googlesource.com/#/q/I2d898d56ed0ac33f5a08253509cfd811ee0e8a5d), [b/177000821](https://issuetracker.google.com/issues/177000821))
- SemanticsPropertyReceiver.hidden was renamed to invisibleToUser and marked @ExperimentalComposeUiApi. AccessibilityRangeInfo was renamed to ProgressBarRangeInfo. stateDescriptionRange was renamed to progressBarRangeInfo. AccessibilityScrollState was renamed to ScrollAxisRange. horizontalAccessibilityScrollState was renamed to horizontalScrollAxisRange. verticalAccessibilityScrollState was renamed to verticalScrollAxisRange. ([Id3148](https://android-review.googlesource.com/#/q/Id31487aa7cbddf4d3d163999afae458cdab4dc8a))
- Removed PointerInputData and modified PointerInputChange to give it all of PointerInputData's fields. Made PointerInputEvent and PointerInputEventData internal because they aren't used in any public API. ([Ifff97](https://android-review.googlesource.com/#/q/Ifff970815031482a0ac1d5dab42a6156e10154b1), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Updated GraphicsLayerScope implement density to support conversions of dp into raw pixels. ([Ied528](https://android-review.googlesource.com/#/q/Ied528ab0f8c3cb058664ace248e93942ef374c74), [b/176819695](https://issuetracker.google.com/issues/176819695))
- Updated matrix API to follow row major ordering and provide index constants to assist with conversions between different matrix representations to match framework conversion logic between SkMatrix and Matrix4 internally. ([I432e6](https://android-review.googlesource.com/#/q/I432e61366431db5d7e00f8e9a2e1cdbf412dc6ce))
- Removed experimental monotonicFrameAnimationClockOf methods ([Ib753f](https://android-review.googlesource.com/#/q/Ib753f5d3cb77dabc7727f677a73bb7da8dae5fe2), [b/170708374](https://issuetracker.google.com/issues/170708374))
- Move String.fintPrecedingBreak and String.fingFollowingBreak to InternalTextApi. ([I657c4](https://android-review.googlesource.com/#/q/I657c4531059f27c8609d0f458dc6ddfab3488ad3))
- androidx.compose.ui.util.isSurrogatePair has been removed from public API. ([Ia9494](https://android-review.googlesource.com/#/q/Ia9494b64647137dcb10508878deb46f30685344e))
- Renamed TransformedText.transformedText to TransformedText.text
  - TransformedText is no longer a data class ([Ie672a](https://android-review.googlesource.com/#/q/Ie672ad03d475ce6a9bf21b8c74a431592b01040b))
- Removed `data class` from the following classes:
  - InlineTextContent
  - LocaleList ([I605c7](https://android-review.googlesource.com/#/q/I605c7a0e257f0a52db29f8d82ee449e4ed2c9d8e))
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
- Changed VisualTransformation to be a functional interface ([I3bba4](https://android-review.googlesource.com/#/q/I3bba482675b65f234f5d46676f1e70853b21c051))
- Added a function reference parameter type ([I5e1bd](https://android-review.googlesource.com/#/q/I5e1bdbe66deb2528a7e152113818a2d7ff5303e6))
- Add transformed bounds to InspectorNode ([Ice42f](https://android-review.googlesource.com/#/q/Ice42fc685090449cb94241b46711e904a994d427))

**Bug Fixes**

- onCommit, onDispose, and onActive have been deprecated in favor of SideEffect and DisposableEffect APIs ([If760e](https://android-review.googlesource.com/#/q/If760ec2a190c4121a35006695d953010ac22a43a))
- Changes to factory functions for Font/FontFamily/Typeface

  - Added factory functions that start with capital letter
  - Deprecated previous factory functions with lowercase first letters
  - New factory functions return the FontFamily instead of subclasses
  - Hid constructors of the subclasses, so that they can only be constructed via factory functions.
  - Renamed Font.asFontFamily to Font.toFontFamily ([I42aa7](https://android-review.googlesource.com/#/q/I42aa7f9fb7e11eb708bc9e9828f65c57c6c9320b))
- Introduced `ComposeContentTestRule`, which extends
  `ComposeTestRule` and defines `setContent`, which has been removed from
  `ComposeTestRule`. Added a factory method `createEmptyComposeRule()`
  that returns a `ComposeTestRule` and does not launch an Activity for
  you. Use this when you want to launch your Activity during your test,
  e.g. using `ActivityScenario.launch` ([I9d782](https://android-review.googlesource.com/#/q/I9d78283c27d87a3135071884e115bbd814492c47), [b/174472899](https://issuetracker.google.com/issues/174472899))

- animateAsState is now animateFooAsState, where Foo is the
  type of the variable being animated. e.g. Float, Dp, Offset, etc ([Ie7e25](https://android-review.googlesource.com/#/q/Ie7e25c8978996334b0dcc757b07df1434ff346aa))

- Content description parameter has been added to the Image and Icon. It is used to provide description to the accessibility services ([I2ac4c](https://android-review.googlesource.com/#/q/I2ac4c1058ed0bf1e5756cc6cdae546806974409e))

- Remove displaySize as it should be avoided. Typically it is
  better to use size of onRoot() or window size at least. ([I62db4](https://android-review.googlesource.com/#/q/I62db4535f36b09ab6f0b874c221ece0b352db962))

- OnSizeChanged was reporting the size of the layout's
  contents. It now reports the size at its position within the
  modifier chain. ([I36b78](https://android-review.googlesource.com/#/q/I36b78f445cf90b10f3df4ea6251bc19392bb7c11), [b/177562900](https://issuetracker.google.com/issues/177562900))

- The emit() API and all overloads have been deprecated and renamed to ComposeNode. The APIs are identical, just a different name in order to follow the naming conventions of Compose ([I4137b](https://android-review.googlesource.com/#/q/I4137beb6f23fb43350bf7badcbe790f59fa85e2c))

- TextFieldValue accepts AnnotatedString. However this is
  an API only change and multi-style text editing is not
  implemented yet.

  - Removed `initial` from EditingBuffer constructor parameters. ([I326d5](https://android-review.googlesource.com/#/q/I326d534a69911fdd39097cdb42e9341ee7987130))
- invalidate and compositionReference() are now deprecated in favor of currentRecomposeScope and rememberCompositionReference respectively. ([I583a8](https://android-review.googlesource.com/#/q/I583a8efa6e3d3bc303792b825b948b3722ada103))

- AnnotatedString is changed to extend from kotlin.CharSequence.
  Therefore length and subSequence are now instance functions,
  and extension functions are removed. ([Iaf429](https://android-review.googlesource.com/#/q/Iaf429c94da9f1867cc0815cb26933961a71cc629))

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
- Deprecated arithmetic operations between 2 or more TextUnits. Deprecated TextUnit.Sp and TextUnit.Em functions in preference to the extension functions such as Int.sp and Int.em. ([I48369](https://android-review.googlesource.com/#/q/I4836990929ce6414615d6c5ebca83b5708a9753b))

- Resources in libraries with no explicitly declared public resources
  (ex. via public.xml) are now private by default. ([Ia1dcc](https://android-review.googlesource.com/#/q/Ia1dcca1ad5c65c1ab90b97c22589e7392161fd62), [b/170882230](https://issuetracker.google.com/issues/170882230))

- ScrollableColumn/Row were deprecated. Using ScrollableColumn is less efficient compared to LazyColumn when you have a large scrolling content because with LazyColumn we can only compose/measure/draw visible elements. To prevent users from going the inefficient way we decided to deprecate ScrollableColumn and ScrollableRow and promote usages of LazyColumn and LazyRow instead. Users can still decide they don't need the lazy behaviour and use the modifiers directly like this: Column(Modifier.verticalScroll(rememberScrollState())) ([Ib976b](https://android-review.googlesource.com/#/q/Ib976b534e063a86a2c587762b786a23e32cc61b6), [b/170468083](https://issuetracker.google.com/issues/170468083))

- New `items(count: Int)` factory method for scope of LazyColumn/LazyRow/LazyVerticalGrid.
  `items(items: List)` and `itemsIndexed(items: List)` are now extension functions so you have to manually import them when used.
  New extension overloads for Arrays: `items(items: Array)` and `itemsIndexed(Array)` ([I803fc](https://android-review.googlesource.com/#/q/I803fc5f25fac55855c710ff5064f11525f7b6010), [b/175562574](https://issuetracker.google.com/issues/175562574))

- Please use ImeAction.None instead of ImeAction.NoAction

  - Please use ImeAction.Default instead of ImeAction.Unspecified ([Ie1bcc](https://android-review.googlesource.com/#/q/Ie1bcc7bc3828c757e497b85c4dd70d37764f616f))
- Leverage TestCoroutineDispatcher in testing ([I532b6](https://android-review.googlesource.com/#/q/I532b68e37ea6f72964fdcc267e397d285cffd9ad))

- Renamed TextInputService.onStateUpdated as updateState ([Id4853](https://android-review.googlesource.com/#/q/Id4853b777bb81a4645d1b41b5dff874322949022))

- TransitionDefinition-based Transition has been deprecated ([I0ac57](https://android-review.googlesource.com/#/q/I0ac57acd13386d028dfe0840e8ce509362cf107e))

- TextUnitType.Inherit is removed. Please use TextUnitType.Unspecified instead. ([I9ff64](https://android-review.googlesource.com/#/q/I9ff64d3a870fe3b14582de5c18f82b01ba6f91b4))

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.ui:ui-*:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/ui)

**Breaking Change**

- Restructuring of the internal compiler
  API allows batching changes to the nodes generated
  as a result of composition into the "apply changes"
  phase of composition, after all `@Composable` functions
  have completed.

  This is a behavioral breaking
  change that might affect application code as
  nodes are no longer available from internal and
  experimental APIs until after changes have been
  applied. This can usually be worked around by
  surrounding code with such dependencies in a
  `SideEffect` composable to defer execution of the
  code until after the nodes have been created and
  initialized. ([I018da](https://android-review.googlesource.com/#/q/I018dab05a0486e8db663aea39a7546aa73142c11))

**API Changes**

- Added Modifier.focusOrder() that can be used to specify a custom focus traversal order ([I90cf5](https://android-review.googlesource.com/#/q/I90cf58d6b1f19341d6cdbc7846fd95934938e9f4), [b/175899543](https://issuetracker.google.com/issues/175899543), [b/170155556](https://issuetracker.google.com/issues/170155556), [b/170155429](https://issuetracker.google.com/issues/170155429))
- Removed deprecated focusObserver use onFocusChanged or onFocusEvent instead ([I3ecb9](https://android-review.googlesource.com/#/q/I3ecb9449c5aa3e9b3a9d396808c63a8b2c199916), [b/175156387](https://issuetracker.google.com/issues/175156387))
- EditOperations API Changes
  - Renamed EditOperation as EditCommand
  - Added Command suffix for EditOperation concrete implementations
  - EditCommand's are no longer data classes
  - Renamed EditOperation.process function to applyTo
  - Renamed InputEventListener to InputEventCallback
  - ([I0a366](https://android-review.googlesource.com/#/q/I0a366ac29c7a373efc36eb544bb759eba7f79f3d))
- Removed unused PxSquared, PxCubed, PxInverse. Changed Size.center() to be a property. ([I973f7](https://android-review.googlesource.com/#/q/I973f7604b65d1228bd527022d12df785ed1e5d92))
- ui-test module will now be able to configure the creation of Recomposers for UIs under test ([Ibebd8](https://android-review.googlesource.com/#/q/Ibebd8b327a7227f6c1ee66c66002bf682a2847f6))
- Modified Velocity to have component parts and mathematical operations. ([Ib0447](https://android-review.googlesource.com/#/q/Ib0447d694d7c5dc82fcef7448faeb0cdda87fced))
- Renamed `@ExperimentalTesting` to `@ExperimentalTestApi` to be consistent with similar experimental api annotations ([Ia4502](https://android-review.googlesource.com/#/q/Ia4502a82d5b66328b6e3e3cd322614939816901e), [b/171464963](https://issuetracker.google.com/issues/171464963))
- Renamed Color.useOrElse() to Color.takeOrElse() ([Ifdcf5](https://android-review.googlesource.com/#/q/Ifdcf503101fa33b1eaf729a33ac14d0dc03f66ff))
- Removed unused DpInverse, DpSquared, and DpCubed classes. ([I4d62b](https://android-review.googlesource.com/#/q/I4d62b6fb859cdae0cc2d5579a5ccfb7ea5372781))
- Constraints#satisfiedBy was renamed to isSatisfiedBy. ([I9cf5c](https://android-review.googlesource.com/#/q/I9cf5c5c15c90adaf95d91eef3da4d695733268e9))
- Add a callback to notify Owner when layoutnode bounds change. ([I72fd1](https://android-review.googlesource.com/#/q/I72fd151db59ff5196d9b03f0735f40535a71b47d))
- Added isSpecified, isUnspecified, and useOrElse for inline classes with an Unspecified constant. ([I93f7b](https://android-review.googlesource.com/#/q/I93f7b4f1b6c3ef08a3fc6d89fa397a122ef41348), [b/174310811](https://issuetracker.google.com/issues/174310811))
- Expand \[Abstract\]ComposeView APIs to allow recycling
  Compose-based views, disposing their composition to recreate again
  later. Add APIs for installing and discovering window-scoped Recomposers
  and CompositionReferences for creating child compositions.

  Add ViewCompositionStrategy for configuring the composition disposal
  strategy of \[Abstract\]ComposeViews; default behavior is dispose on
  window detach. ([I860ab](https://android-review.googlesource.com/#/q/I860ab99a2950457157a4d904e0c514d5134fdfd7))
- Removed Any.identityHashCode() public api ([I025d7](https://android-review.googlesource.com/#/q/I025d720aec64ebd2182787b9200ca9b3827d5436))

- Removed toStringAsFixed
  API in favor of using String.format
  instead directly. ([Iaba6b](https://android-review.googlesource.com/#/q/Iaba6b2d83490bcd3d7fd1cd167b54569418164fb))

- Add Toggle to foundation Strings.kt ([I4a5b7](https://android-review.googlesource.com/#/q/I4a5b74e3ed9bc3b1acd09af221331ef6ab51b9fe), [b/172366489](https://issuetracker.google.com/issues/172366489))

- Moved nativeClass to
  ui module and made it internal.
  Updated usages of nativeClass in
  equals implementations to use
  'is MyClass' instead. ([I4f734](https://android-review.googlesource.com/#/q/I4f7340266d36552665f0a059ab34e9b886926f0b))

- Modifier.focus() and Modifier.focusRequester() are deprecated. Use Modifier.focusModifier() and Modifier.focusReference() instead. ([I75a48](https://android-review.googlesource.com/#/q/I75a483954b69de794c5d7be9efc236b6d6b8fcad), [b/175160751](https://issuetracker.google.com/issues/175160751), [b/175160532](https://issuetracker.google.com/issues/175160532), [b/175077829](https://issuetracker.google.com/issues/175077829))

- Introduced SelectionRegistrar.notifySelectableChange to notify Selectable updates to SelectionManager. ([I6ff30](https://android-review.googlesource.com/#/q/I6ff3055300ca7316ad644a4bcf7872d0d48878b8), [b/173215242](https://issuetracker.google.com/issues/173215242))

- Introduced Outline.bounds
  property to obtain the bounding rect
  for various outline implementations. ([I16e74](https://android-review.googlesource.com/#/q/I16e749ad4477cfaacfef8267e37ff5cfefb2fd02), [b/175093504](https://issuetracker.google.com/issues/175093504))

- Deprecated TestUiDispatcher. Use Dispatchers.Main instead ([Ic171f](https://android-review.googlesource.com/#/q/Ic171f9e9da0d7c8d3688754e0f5eed482a668560), [b/175385255](https://issuetracker.google.com/issues/175385255))

- ImeOptions and KeyboardOptions are no more a data class ([I3c898](https://android-review.googlesource.com/#/q/I3c898ecf1f83f64bc9886a088af4fa2a12adcff7), [b/168684531](https://issuetracker.google.com/issues/168684531))

- VisualTransformation API Changes

  - Renamed OffsetMap to OffsetMapping
  - Renamed OffsetMapping.identityOffsetMap to OffsetMapping.Identity
  - PasswordTransformation is no longer data-class
  - Moved OffsetMapping to its own file
  - ([I0bdf3](https://android-review.googlesource.com/#/q/I0bdf3e90ac4a1d8e6e2a3c5762f51016561f2da8))
- Renamed Position to DpOffset and removed getDistance() ([Ib2dfd](https://android-review.googlesource.com/#/q/Ib2dfde4ceb450e417ff759bdabbc74d2506a44c9))

- Changed fun Dp.isFinite() to a val Dp.isFinite ([I50e00](https://android-review.googlesource.com/#/q/I50e0035e772c40d61500f56453cd02bb0d9dee70))

**Bug Fixes**

- Recomposer now exposes a Flow of its current state, allowing monitoring its activity and the activity of associated effects. ([Ifb2b9](https://android-review.googlesource.com/#/q/Ifb2b901636db4ec2f3ad068d063f5b8f74be82f4))
- The native keyEvent can now be accessed through keyEvent.nativeKeyEvent ([I87c57](https://android-review.googlesource.com/#/q/I87c57d68b76441fe92d2b91f58385832fc40ec8d), [b/173086397](https://issuetracker.google.com/issues/173086397))
- `animate()` is now replaced with `animateAsState()`, which returns a `State<T>` instead of `T`. This allows better performance, as the invalidation scope can be narrowed down to where the State value is read. ([Ib179e](https://android-review.googlesource.com/#/q/Ib179e3f5f4bf3b72f7445fc22e73c46af7cf74de))
- Add Semantics role API and add Role as a parameter to clickable, selectable and toggleable SemanticsModifier. Changed Modifier.progressSemantics so that Slider can also use it. ([I216cd](https://android-review.googlesource.com/#/q/I216cd5b9118581e569c48a095f009c841ed4418b))
- New coroutine-based API `Animatable` that ensures mutual exclusiveness among its animations.
  - New DecayAnimationSpec to support multi-dimensional decay animation
  - ([I820f2](https://android-review.googlesource.com/#/q/I820f29e24eaa512515c776db971444290dea97e9), [b/168014930](https://issuetracker.google.com/issues/168014930))

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/ui)

**API Changes**

- Deprecated KeyEvent.Alt is now removed. Use KeyEvent.isAltPressed instead. ([Idd695](https://android-review.googlesource.com/#/q/Idd695fc17bdb5080f6af112cfe040494127975f0))
- Modifier.keyInputFilter and Modifier.previewKeyInputFilter are deprecated use Modifier.onKeyEvent and Modifier.onPreviewKeyEvent instead ([Idbf1b](https://android-review.googlesource.com/#/q/Idbf1b0b7da9d09f4312b7599b863dc41f667594c), [b/175156384](https://issuetracker.google.com/issues/175156384))
- Modifier.focusObserver is deprecated. Use Modifier.onFocusChanged or Modifier.onFocusEvent instead ([I30f17](https://android-review.googlesource.com/#/q/I30f17d06d60fa9b8c510ee0468464258894a467b), [b/168511863](https://issuetracker.google.com/issues/168511863), [b/168511484](https://issuetracker.google.com/issues/168511484))
- For suspending pointer input APIs, renamed HandlePointerInputScope to AwaitPointerEventScope and handlePointerInput() to awaitPointerEventScope(). ([Idf0a1](https://android-review.googlesource.com/#/q/Idf0a1b94f065e72b65361cdf616122ed7939c3e7), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Autofill API is now experimental API and requires opt-in ([I0a1ec](https://android-review.googlesource.com/#/q/I0a1ecfbf4ddeccaecc3cea8d2223b0a4afa60636))
- Adding destructuring declarations to create FocuSRequester instances ([I35d84](https://android-review.googlesource.com/#/q/I35d84e1320bec5b62bf1fb096aa95f90cfd96e9c), [b/174817008](https://issuetracker.google.com/issues/174817008))
- accessibilityLabel has been renamed to contentDescription. accessibilityValue has been renamed to stateDescription. ([I250f2](https://android-review.googlesource.com/#/q/I250f2d41e139d4838b0b3706f18b56fcc4f515bd))
- Custom events were removed from suspending pointer input API ([Ia54d5](https://android-review.googlesource.com/#/q/Ia54d5d081b80b21bf7c84eae4a97ed757c9d11a1), [b/175142755](https://issuetracker.google.com/issues/175142755))
- Introduced several new functions in SelectionRegistrar and also renamed onPositionChange to notifyPositionChange. ([Ifbaf7](https://android-review.googlesource.com/#/q/Ifbaf754c0ee3f485869115bba8dbcc1a8b7f5b88))
- More members of LayoutNode we marked as internal ([I443c6](https://android-review.googlesource.com/#/q/I443c65c9b4677e3947894b7836af6cb5824f7c73))
- LayoutInfo was introduced to be used by tooling and testing ([I9b190](https://android-review.googlesource.com/#/q/I9b190ff86e173fe25a044312990e8a12cb48a59c))
- AndroidOwner made internal ([Ibcad0](https://android-review.googlesource.com/#/q/Ibcad027dbc1794f5d202be52fe0783c73d249a25), [b/170296980](https://issuetracker.google.com/issues/170296980))
- Removed ExperimentalPointerInput annotation ([Ia7a24](https://android-review.googlesource.com/#/q/Ia7a2473869400fc92ce70c802f42df9af7129386))
- Nested scroll system added. Refer to Modifier.nestedScroll for more details ([I36e15](https://android-review.googlesource.com/#/q/I36e1594231bddd0ab8e90bb04fd03bf930a434c5), [b/162408885](https://issuetracker.google.com/issues/162408885))
- subcomposeInto(LayoutNode) was made internal ([Id724a](https://android-review.googlesource.com/#/q/Id724aebef104f6404884f1a45bee9958583b7229))
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
- Added dismissOnBackPress and dismissOnClickOutside properties to AndroidDialogProperties. These allow configuring when the dialog's onDismissRequest lambda will be invoked. ([If5e17](https://android-review.googlesource.com/#/q/If5e175fe1866cb5b73118cb178269152bc80eea4))

- Added painterResource API
  to handle opaquely loading Painter objects
  from either rasterized asset formats (like PNGs)
  or VectorDrawables. Consumers no longer have
  to determine the type of asset in advance
  and can call this method to get a Painter object
  to use in Image composables or painter modifiers. ([I2c703](https://android-review.googlesource.com/#/q/I2c703e31eedbbfcf073d28064496a6e324c2027a), [b/173818471](https://issuetracker.google.com/issues/173818471))

- Added Modifier.clearAndSetSemantics to clear descendants'
  semantics and set new ones. ([I277ca](https://android-review.googlesource.com/#/q/I277ca1b76fda44a34a2c01844b832244cb42ff7e))

- Moved ContentDrawScope to ui-graphics
  module to be with DrawScope. ([Iee043](https://android-review.googlesource.com/#/q/Iee0437fa587fbe12a3623955f5fe720d5aae551f), [b/173832789](https://issuetracker.google.com/issues/173832789))

- Introduced PathEffect graphics API
  to provide different patterns to stroked shapes.
  Deprecated usage of NativePathEffect in favor
  of expect/actual implementation of PathEffect. ([I5e976](https://android-review.googlesource.com/#/q/I5e97670b4534250497dc31edab4f0001ab57f2ec), [b/171072166](https://issuetracker.google.com/issues/171072166))

- Added IdlingResource interfaces to Compose, as a Compose
  supported variant of Espresso's idling resources. They can be registered
  and unregistered through the ComposeTestRule ([I433f3](https://android-review.googlesource.com/#/q/I433f395067a6de6d0a4afc994e5cdb813098b9c3))

- Removed global (un)registration of ComposeIdlingResource and
  global (un)registration of clocks into ComposeIdlingResource ([I32660](https://android-review.googlesource.com/#/q/I326602fc29bac371a42fbdc54023422f8db20eeb))

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
- Deprecate LazyColumnFor, LazyRowFor, LazyColumnForIndexed and LazyRowForIndexed. Use LazyColumn and LazyRow instead ([I5b48c](https://android-review.googlesource.com/#/q/I5b48c8a3b1fef2f603ab69ded1d19709aa9f87fb))

- Deprecated BuildCompat.isAtLeastR ([Idb37e](https://android-review.googlesource.com/#/q/Idb37ed0673c5a8812b60d70de5636bfc3e191d85))

- Added buildAnnotatedString factory function in order
  to build an AnnotatedString. Deprecated annotatedString
  builder function. ([Idfe0b](https://android-review.googlesource.com/#/q/Idfe0b133687e7b5f377e997b79bd4463161a6d0b))

- Removed extension methods
  on Float and Double to convert values
  to radians. Moved to be a private function
  within the implementation PathParser
  which was the only place where it was used ([I25f52](https://android-review.googlesource.com/#/q/I25f52465ebf2fb238db43eb048cf19823e3fc990))

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/ui)
| **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

**API Changes**

- Add semantics action Dismiss ([I2b706](https://android-review.googlesource.com/#/q/I2b70641450760f3056a53e283cf04b004ea1db2c))
- Moved DrawModifier APIs from the androidx.compose.ui package to the androidx.compose.ui.draw package. Created DrawModifierDeprecated.kt file to include typealiases/helper methods to assist with the migration from the deprecated to the current APIs. ([Id6044](https://android-review.googlesource.com/#/q/Id6044c7119aeaf40a3ff21006fe39b03f5f1b18a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- Renamed Modifier.drawLayer to Modifier.graphicsLayer Also updated related classes to GraphicsLayer as per API feedback. ([I0bd29](https://android-review.googlesource.com/#/q/I0bd297065427d19715e4e33480f7be87e51ff48a), [b/173834241](https://issuetracker.google.com/issues/173834241))
- New methods placeable.placeWithLayer() and placeable.placeRelativeWithLayer() were added which allows custom layouts and layout modifiers to place a child with introducing a graphics layer for their drawing. Having that we can first optimize redrawings, so when we need to move a child we don't have to redraw its content, second we can apply draw transformations for a child ([Ibd8f6](https://android-review.googlesource.com/#/q/Ibd8f6bb03f391c3f1bbf13f659d79e3b57019a46), [b/170296989](https://issuetracker.google.com/issues/170296989), [b/171493718](https://issuetracker.google.com/issues/171493718), [b/173030831](https://issuetracker.google.com/issues/173030831))
- `<T>` was removed from SubcomposeLayout declaration. You can use it without specifying a type now. ([Ib60c8](https://android-review.googlesource.com/#/q/Ib60c850964b308ebee32beca6db78d76af67fbf1))
- Added Modifier.scale/rotate APIs as conveniences for drawLayer.
  - Renamed `Modifier.drawOpacity` to `Modifier.alpha`
  - Renamed `Modifier.drawShadow` to `Modifier.shadow` ([I264ca](https://android-review.googlesource.com/#/q/I264ca72b36ea62fd615436849203895ed742fa1e), [b/173208140](https://issuetracker.google.com/issues/173208140))
- Made PointerInputData's uptime and position fields non-nullable. ([Id468a](https://android-review.googlesource.com/#/q/Id468a0ef7c00c30a89114ea8dc95fa019961e189))
- MaterialTheme now sets the correct colors for selection handles and selection background. Non-Material apps can manually use AmbientTextSelectionColors to customize the colors used for selection. ([I1e6f4](https://android-review.googlesource.com/#/q/I1e6f4b495bdc713e162759a08ecf0a7311b26e33), [b/139320372](https://issuetracker.google.com/issues/139320372), [b/139320907](https://issuetracker.google.com/issues/139320907))
- Added WindowManager.isWindowFocused to check if the host window is in focus, and a WindowFocusObserver that provides an onWindowFocusChanged callback. ([I53b2a](https://android-review.googlesource.com/#/q/I53b2a702b81215dc5a5536144a752e1c93ab056e), [b/170932874](https://issuetracker.google.com/issues/170932874))
- Updated TransformOrigin API to have destructuring syntax to return `pivotFractionX` and `pivotFractionY` as `component1` and `component2` ([If43c4](https://android-review.googlesource.com/#/q/If43c4a1019440dfe20a73db23048672c3006131c), [b/173586560](https://issuetracker.google.com/issues/173586560))
- Added lint check for composable lambda parameter naming and position, to check for consistency with Compose guidelines. Also migrated some APIs using `children` as the name for their trailing lambda to `content`, according to the lint check and guidance. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48e38a2896785b521814d95c9fb624d2807315))
- Added API to check if Alt, Ctrl, Meta or Shift modifier keys were pressed when a keyevent was dispatched. ([I50ed9](https://android-review.googlesource.com/#/q/I50ed9c356c69b61a68fffe2b4247fe87cc91e8c4))
- Added a new `Modifier.drawLayer()` overload. It takes a lambda block on a new GraphicsLayerScope where you define the layer parameters in a way which allows to skip recomposition and relayout when the state change happens. DrawLayerModifier is now internal in preparation to migrating its logic into placeable.placeWithLayer() method of LayoutModifier ([I15e9f](https://android-review.googlesource.com/#/q/I15e9f41e3c93245529bf798e4a9617ca49d5e509), [b/173030831](https://issuetracker.google.com/issues/173030831))
- Deprecated Ambients named with `Ambient` as their suffix, and replaced them with new properties prefixed with Ambient, following other Ambients and Compose API guidelines. ([I33440](https://android-review.googlesource.com/#/q/I334403cc490ea913b8980d29e2cbe08e98ad7945))
- Moved `androidx.compose.ui.text.Typeface` to `androidx.compose.ui.text.font.Typeface` ([Ic2b81](https://android-review.googlesource.com/#/q/Ic2b81ae67d3b53224f4771f5b37717a24fafc9d8))
- Semantics argument mergeAllDescendants was renamed to mergeDescendants. ([Ib6250](https://android-review.googlesource.com/#/q/Ib625016bd3bbe4349c2870ba68ad52d76a0d372a))
- New drag gesture detector suspending pointer input API, including orientation locking. ([Icef25](https://android-review.googlesource.com/#/q/Icef25dbc49fa8786c7631e8b97b0732b871afea6))
- Renamed VectorAsset to ImageVector Moved and renamed VectorAsset to Builder to be an inner class of ImageVector as per API guidelines. Added typealias of VectorAssetBuilder to link to ImageVector.Builder for compat. ([Icfdc8](https://android-review.googlesource.com/#/q/Icfdc85391feb2bd0edabebeba84f31bace10883a))
- Renamed ImageAsset and related methods to ImageBitmap. ([Ia2d99](https://android-review.googlesource.com/#/q/Ia2d9941a6e0b8c29867cb3fbafb629fa4db10684))
- Add zIndex param for the PlacementScope's place() so Modifier.zIndex() now works as a LayoutModifier and any custom layout can set zIndexes for their children right in the placement block ([I711f7](https://android-review.googlesource.com/#/q/I711f7165ad321434c57082f4277c6623219102b0), [b/171493718](https://issuetracker.google.com/issues/171493718))
- Moved foundation semantics properties to ui ([I6f05c](https://android-review.googlesource.com/#/q/I6f05cc7c0bdf1e5344440cd6e492fbc0545011e7))
- Deprecate place(Offset) and placeRelative(Offset). Use overloads with int offsets instead ([I4c5e7](https://android-review.googlesource.com/#/q/I4c5e75e6ba7382735acccd44324bb96a59d82490))
- Previously Deprecated APIs were removed: Modifier.onPositioned was removed, use Modifier.onGloballyPositioned. Modifier.onDraw was removed, use Modifier.onDrawBehind. Modifier.plus was removed, use Modifier.then. Color.Unset was removed, use Color.Unspecified. PxBounds class was removed, use Rect instead. ([Ie9d02](https://android-review.googlesource.com/#/q/Ie9d0239f96922f1db769c38f6f970532a8f54ff3), [b/172562222](https://issuetracker.google.com/issues/172562222))
- The Alignment interface was updated and made functional. ([I46a07](https://android-review.googlesource.com/#/q/I46a0791e261b6f305804797cdda7fdd2ef405305), [b/172311734](https://issuetracker.google.com/issues/172311734))
- Gesture detector for tap, double-tap, long press, and press indication were added using the new suspending pointer input. A few utilities were added as well, making it easier for developers to write their own gesture detectors. ([I00807](https://android-review.googlesource.com/#/q/I0080776a5672f63ceb8f4ae0a753d5f4debdc2e8))
- `id` was renamed to `layoutId` for `LayoutIdParentData`. `Measurable.id` was renamed to `Measurable.layoutId`. ([Iadbcb](https://android-review.googlesource.com/#/q/Iadbcb8b5588876e0d2a512e476968025b03ada6c), [b/172449643](https://issuetracker.google.com/issues/172449643))
- New multitouch gesture detector, including helpers for detecting rotation, zoom, and panning. ([Ic459d](https://android-review.googlesource.com/#/q/Ic459dc4c6b4e4a171dbb16a87ee8dfe780230d16))
- Introduced SweepGradientShader and SweepGradientBrush APIs. ([Ia22c1](https://android-review.googlesource.com/#/q/Ia22c1593bad5a63dbc66f4b012617087b30d2f77))
- Time control in tests (TestAnimationClock and its usages) is now experimental ([I6ef86](https://android-review.googlesource.com/#/q/I6ef86c5f530422c7c751bdb086a691cbc2e837f3), [b/171378521](https://issuetracker.google.com/issues/171378521))
- Add coroutine-based scrolling APIs:

  Adds LazyListState.snapToItem and LazyListState.smoothScrollBy, as well as lower-level
  APIs for scroll control. These APIs provide a suspend interface to control scrolling
  that waits until the scroll is finished before returning. ([Ie5642](https://android-review.googlesource.com/#/q/Ie56426c01b3c8ad51afb237cb972a8578d2fefd4))
- Modifier.focusable has need added in foundation. Use this to add focusable behavior to a component, with correct semantics and accessibility. ([I41eb9](https://android-review.googlesource.com/#/q/I41eb9d67669e19f8a7c20804c836a8c6dc0b5526), [b/152525426](https://issuetracker.google.com/issues/152525426), [b/162865824](https://issuetracker.google.com/issues/162865824))

- Provide default implementations of methods and properties in
  AnimationClockTestRule that can be delegated to its `clock` ([I7ea3d](https://android-review.googlesource.com/#/q/I7ea3dadf99f2ab6ccd54850d03a65a41160989a2), [b/173399709](https://issuetracker.google.com/issues/173399709))

- AndroidComposeTestRule can now accept custom activity
  launchers ([Ib8288](https://android-review.googlesource.com/#/q/Ib828876d918f3f091b622bbeb62dd1a31c75badb), [b/153623653](https://issuetracker.google.com/issues/153623653), [b/154135019](https://issuetracker.google.com/issues/154135019))

- TextLayoutResult.getLineVisibleEnd is deprecated. As a replacement TextLayoutResult.getLineEnd now has a new parameter visibleEnd. ([I73282](https://android-review.googlesource.com/#/q/I732828f8e4ffad3b36e116910e787628a0472c1f))

- Updated TextFieldValue API

  - made TextFieldValue.composition readonly
  - removed exception thrown for invalid selection range ([I4a675](https://android-review.googlesource.com/#/q/I4a67592c05ab384ad5614cccf50ad6e79be52b55), [b/172239032](https://issuetracker.google.com/issues/172239032))
- Support TtsAnnotation for text to speech engine. ([I54cc6](https://android-review.googlesource.com/#/q/I54cc61f8e412212c66079a3c97b5575e1336af57))

- New APIs for running animations in coroutines ([Ied662](https://android-review.googlesource.com/#/q/Ied662fbc4c4c373fba7877c1421ee76c49fd69b1))

**Bug Fixes**

- The alignment parameter of Box was renamed to contentAlignment. ([I2c957](https://android-review.googlesource.com/#/q/I2c95727d9ec49f056fffb3a73dce95a9d3be5b53))
- offsetPx modifiers were renamed to offset. They are now taking lambda parameters instead of State. ([Ic3021](https://android-review.googlesource.com/#/q/Ic302174ef9cffa7ef806d1668f81cb89159363f2), [b/173594846](https://issuetracker.google.com/issues/173594846))
- Added resetInput parameter to TextInputService#onStateUpdated ([I3e8f5](https://android-review.googlesource.com/#/q/I3e8f5404553921bd94ae424d2840ca5595b6f90b), [b/172239032](https://issuetracker.google.com/issues/172239032), [b/171860947](https://issuetracker.google.com/issues/171860947))
- Added lint check for Modifier parameters in Composable functions. This lint check checks the naming, return type, default value, and order of the parameter for consistency with Compose guidelines. ([If493b](https://android-review.googlesource.com/#/q/If493bd2e3c236cae95744e1fab138f87f5844daa))
- Temporarily added option to let the TestAnimationClock be driven by the MonotonicFrameClock ([I1403b](https://android-review.googlesource.com/#/q/I1403ba3d82adc530d885192aa696c4363456a4c1), [b/173402197](https://issuetracker.google.com/issues/173402197))
- Added Android Typeface wrapper. You can load an Android Typeface via `typeface` function i.e. `typeface(Typeface.DEFAULT)`. Also renamed `typefaceFromFontFamily()` to `typeface()` ([I52ab7](https://android-review.googlesource.com/#/q/I52ab713f851011796d0a0437e62693a7e762701a))
- Added lint check to check that Modifier factory functions are defined as extensions on Modifier, so they can be fluently chained together. ([I07981](https://android-review.googlesource.com/#/q/I07981617a0e09137b787adbc0219f48af5b86169))
- Remove old ui-test module and its stubs ([I3a7cb](https://android-review.googlesource.com/#/q/I3a7cbbe376d0542955983fb09afd2dc37be7647e))
- Recomposer no longer accepts an EmbeddingContext; required scheduling dependencies are obtained from the effectCoroutineContext. FrameManager is deprecated; platform integrations should initialize their own global snapshot handling. ([I02369](https://android-review.googlesource.com/#/q/I02369db94b92e6ace0a7273d9d74ad44cc8cebe5))
- Pass style information to accessibility node. ([If5e8d](https://android-review.googlesource.com/#/q/If5e8d28f3d26016115e895d852edd18dab8aed09))
- TextUnit.Inherit is renamed to TextUnit.Unspecified for consistency with other units. ([Ifce19](https://android-review.googlesource.com/#/q/Ifce190ac87b01144b2fb0e7f9a8659bceed87f4e))

### Compose UI Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/ui)

**API Changes**

- Introduced ScaleFactor inline class to represent scale factors for the horizontal and vertical axes independent of one another in order to support non-uniform scaling use cases.
  - Added computeScaleFactor method to ContentScale
  - Added ContentScale.FillBounds to perform non-uniform scaling to stretch the src bounds to fully occupy the destination.
  - Added operator methods to compute ScaleFactor parameters with Size parameters.
  - ([Ic96a6](https://android-review.googlesource.com/#/q/Ic96a6eb421cda5550c817ceca23ab50fde337778), [b/172291582](https://issuetracker.google.com/issues/172291582))
- The BiasAlignment and BiasAbsoluteAlignment factories for creating Alignments were added. ([Iac836](https://android-review.googlesource.com/#/q/Iac836deef25843cbec763400d54903fca496d50e), [b/169406772](https://issuetracker.google.com/issues/169406772))
- Allow a developer to forcefully clear focus. ([I90372](https://android-review.googlesource.com/#/q/I9037255fff69d59e9596632c9e63875fdbd9df89))
- A bug causing elevation not being drawn for Views inside Compose was fixed. ([If7782](https://android-review.googlesource.com/#/q/If778269cb837dbc236b4a340e650a44eef33aca4))
- Created onDrawBehind API within ContentDrawScope to match naming convention with Modifier.drawBehind. ([I4fc3a](https://android-review.googlesource.com/#/q/I4fc3ae880757f9956c522a03e2ac28ab205946e9), [b/171955269](https://issuetracker.google.com/issues/171955269))
- Add support for camera distance to complement 3d transformations rotationX/rotationY on layer APIs. ([I40213](https://android-review.googlesource.com/#/q/I402132be203b2d62b5c3026e3989877e2fa8f3e1), [b/171492100](https://issuetracker.google.com/issues/171492100))
- Added SelectionContainer without the callback ([Ibfadb](https://android-review.googlesource.com/#/q/Ibfadba5a9f66101c5746c5b842dadf840617e1a6))
- ExperimentalSubcomposeLayoutApi annotation was removed. SubcomposeLayout can now be used without adding @OptIn ([I708ad](https://android-review.googlesource.com/#/q/I708adafbc3c10cc6c23fe5a236f66e73146e4f56))
- FirstBaseline and LastBaseline were moved to androidx.compose.ui.layout package ([Ied2e7](https://android-review.googlesource.com/#/q/Ied2e7ff4c8d8a45072439d719ea5c75270c28c97))
- Removed opacity from drawShadow() modifier as it was confusing. ([I82c62](https://android-review.googlesource.com/#/q/I82c622c9eb42c528667fdaeef53271c502c16fb5), [b/171624638](https://issuetracker.google.com/issues/171624638))
- MeasureResult was moved out of MeasureScope. ([Ibf96d](https://android-review.googlesource.com/#/q/Ibf96ddadae8115015066dcda2026a57b87c2ead6), [b/171184002](https://issuetracker.google.com/issues/171184002))
- Several layout related symbols were moved from androidx.compose.ui to androidx.compose.layout.ui. ([I0fa98](https://android-review.googlesource.com/#/q/I0fa982d87929e5ca9e3a32762fe9cf1fa8b8cfef), [b/170475424](https://issuetracker.google.com/issues/170475424))
- Removed Deprecated FocusState2 ([I686cb](https://android-review.googlesource.com/#/q/I686cb828fe0b0182bb31bbe016360d84fc5cbbbb), [b/168686446](https://issuetracker.google.com/issues/168686446))
- ZIndexModifier is now internal ([I1808b](https://android-review.googlesource.com/#/q/I1808b23b35c21e8f814b39a87b37a8a2088da951), [b/171493718](https://issuetracker.google.com/issues/171493718))
- Updated return type of lerp method on Size parameters to return a non-null Size to avoid unnecessary boxing. ([Ib0044](https://android-review.googlesource.com/#/q/Ib00440e033c91e466939bfc9cc700032c00f1ed3))
- Added TestMonotonicFrameClock for testing code that relies on Compose's MonotonicFrameClock for awaiting composition frame events using kotlinx-coroutines-test's runBlockingTest ([I4402f](https://android-review.googlesource.com/#/q/I4402fbcf6da2a1541344158cde473141160994da))
- Removed GestureScope.localToGlobal ([I15299](https://android-review.googlesource.com/#/q/I15299ffe7f0119020089ca9f2256508f56424b8e), [b/171462785](https://issuetracker.google.com/issues/171462785))
- Added `onAllNodesWithSubstring` finder ([I81dd7](https://android-review.googlesource.com/#/q/I81dd70295d9fd893d5c3489d7a7d5ff71b7e95f3), [b/171462889](https://issuetracker.google.com/issues/171462889))
- androidx.ui.test module deprecated. Please migrate to androidx.compose.ui.test and androidx.compose.ui.test.junit4 ([I452e8](https://android-review.googlesource.com/#/q/I452e8ca63834f5948dc183ae633feffa5dffdc6e))

**Bug Fixes**

- captureToBitmap moved to captureToImage. ([I86385](https://android-review.googlesource.com/#/q/I86385454625b533b83c87e48d82e143dd1bcb88e))
- foundation.Text has been deprecated and replaced with material.Text. For a basic, unopinionated text API that does not consume values from a theme, see androidx.compose.foundation.BasicText. ([If64cb](https://android-review.googlesource.com/#/q/If64cbdd89497f171edfd1b4de907123f73279e8d))
- Update TextFields to accept KeyboardOptions ([Ida7f3](https://android-review.googlesource.com/#/q/Ida7f3c71647dc9fff8acdd50fc5604a15957ccec))
- Rename KeyboardOptions as ImeOptions ([I82f36](https://android-review.googlesource.com/#/q/I82f364ca1ede4bfea9430fcc9fd227d729b39fd9))
- Moved KeyboardType and ImeAction into KeyboardOptions ([I910ce](https://android-review.googlesource.com/#/q/I910cea6ec0ef3568b9a94f7b193e8cb7e8b776ed))
- provideDefault was added as an alternative for providing ambients, and it can be used to specify ambient values that will only be set when there is no ambient value already provided. ([Id6635](https://android-review.googlesource.com/#/q/Id663500276ad2ec3e5a5b1310a81efbf3acc0842), [b/171024925](https://issuetracker.google.com/issues/171024925))
- BaseTextField has been deprecated. Use BasicTextField instead. ([I896eb](https://android-review.googlesource.com/#/q/I896eb0eb21e73bda5f269e1ffae4357201acb219))
- Introduce ui-test-junit4 module ([Ib91f8](https://android-review.googlesource.com/#/q/Ib91f8a6792d8852427cc0dff99a40086c00b8ce4))
- `relativePaddingFrom` was renamed to `paddingFrom`. The `paddingFromBaseline` modifier was added, as convenience for specifying distances from layout bounds to text baselines. ([I0440a](https://android-review.googlesource.com/#/q/I0440af2aea41e020cb581b9030522b7586fe952e), [b/170633813](https://issuetracker.google.com/issues/170633813))
- LaunchedTask was renamed to LaunchedEffect for consistency with the SideEffect and DisposableEffect APIs. LaunchedEffect with no subject params is not permitted in order to encourage best practices. ([Ifd3d4](https://android-review.googlesource.com/#/q/Ifd3d4f3b529b3956915c99096eef3fb3108b2b61))
- Introduced resources composable that recomposes when the configuration updates. ([I6387c](https://android-review.googlesource.com/#/q/I6387c385363ff8231d5eb13b4a97d3ef375453c1), [b/167352819](https://issuetracker.google.com/issues/167352819))
- Recomposer now requires a CoroutineContext at construction ([Ic4610](https://android-review.googlesource.com/#/q/Ic4610c5531ceebafc3c8644a3501a8442d1479d6))
- Sum `zIndex` values when multiple `Modifier.zIndex()` applied. Previously the first one was winning. ([Ic514c](https://android-review.googlesource.com/#/q/Ic514c8e7640a09fa3f0e224b23bb06bc7868f848), [b/170623936](https://issuetracker.google.com/issues/170623936))
- Changes to the internal SlotTable implementation which should not affect the public API. ([If9828](https://android-review.googlesource.com/#/q/If98280439f4965fd05f21dd0362635314176eaf8))
- Added Keyboard auto correct IME Option ([I57b8d](https://android-review.googlesource.com/#/q/I57b8d4b3c65630763e198c31c7d116fcbe461c51))
- androidx.ui.test moved to androidx.compose.ui.test ([I9ffdb](https://android-review.googlesource.com/#/q/I9ffdb165d49e8d136b58cc4e32599a4a1d5b169e))
- Removed KeyboardOptions.toImeOptions from public API. ([Ic2e45](https://android-review.googlesource.com/#/q/Ic2e4500be7841ad3815bc576356ab67e616db534))

**External Contribution**

- Disabled publication of internal artifact androidx.compose.ui:ui-text-android ([Ib93fa](https://android-review.googlesource.com/#/q/Ib93fa3ecad55683c735cfb0bfeed193f24da2fe8))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/ui)

**API Changes**

- Recomposer is now a CompositionReference and a valid composition parent. Explicit Recomposer is now required in fewer places. ([I4036f](https://android-review.googlesource.com/#/q/I4036ff66dff4759bd40127a9af0ca59cbaa37041))
- Deprecate VectorPainter in favor of rememberVectorPainter to better indicate that the composable API internally leverages 'remember' to persist data across compositions. ([Ifda43](https://android-review.googlesource.com/#/q/Ifda43dfd1d5b581c3666f4f69b528c47dbaa0ff5))
- Updated Modifier.drawWithCache API to expose ContentDrawScope as a receiver scope instead of DrawScope in order to provide implementations the ability to re-order drawing commands. This is useful for blending/ tinting use cases in which content pixels must be rendered first in order for the corresponding blend mode algorithm to be applied properly. ([Ie7ec8](https://android-review.googlesource.com/#/q/Ie7ec854e6b3f065aba1b8fe43e2b213b6ddf6fe5))
- Move SimpleContainer into PopupTestUtils.kt ([I78c57](https://android-review.googlesource.com/#/q/I78c5741b466eac4301b265636c82487215ebb633))
- ConsumedData is no longer a data class. See https://android-review.googlesource.com/c/platform/frameworks/support/+/1455219 for details ([I1737f](https://android-review.googlesource.com/#/q/I1737f9928e7731402e896deedf7d8a97a598e725))
- Fix Rtl Handle Position. ([I6e1e0](https://android-review.googlesource.com/#/q/I6e1e07b76476d8e2f0be50ff022257c2379edcf7))
- Refactored DrawScope and ContentDrawScope to be interfaces instead of abstract classes
  - Created CanvasDrawScope implementation of DrawScope
  - Refactored implementations of DrawScope to use CanvasScope instead
  - Created DrawContext to wrap dependencies for DrawScope
  - Removed deprecated methods on DrawScope ([I56f5e](https://android-review.googlesource.com/#/q/I56f5e816116bea0d1337fbe0becc26b87694409b))
- Breaking change: removed the return value from `PointerInputFilter.onPointerEvent(...)` given that the only value that should be able to be changed in pointer events is consumption data. Instead of returning data from `PointerInputFilter.onPointerEvent(...)`, now you can just mutate the consumption data of the PointerEvents passed in. ([I6acd0](https://android-review.googlesource.com/#/q/I6acd06e56ab49c8ca932ff7c2d35a517a412e2d2))
- MeasureScope and IntrinsicMeasureScope were made interfaces. ([I1a087](https://android-review.googlesource.com/#/q/I1a087c70511d15a9976a7f1cfc6ded7e90f66215), [b/170461665](https://issuetracker.google.com/issues/170461665))
- The merge function for AlignmentLine was hidden. ([I9da1a](https://android-review.googlesource.com/#/q/I9da1ae8390aca7148051361bbe64954bd2a6b7c2), [b/170612900](https://issuetracker.google.com/issues/170612900), [b/170611568](https://issuetracker.google.com/issues/170611568))
- Add ability to specify inspector info in composed modifier ([Idee08](https://android-review.googlesource.com/#/q/Idee08841816fb7dfc8f0621eb5a32c3663131aa1), [b/163494569](https://issuetracker.google.com/issues/163494569))
- Added SelectAll option into selection menu ([Ief02b](https://android-review.googlesource.com/#/q/Ief02bb5bb39d11a02112c4ace1b971d6834ec5dd))
- Updated DrawTransform.rotate to take a default pivot parameter of center to match the documentation.
  - Updated DrawScope.rotateRad to consume an Offset for the pivot point to match other transformation methods.
  - Deprecated DrawScope.rotateRad overload that consumed floats for the x and y coordinate of the pivot.
  - ([Iffcbb](https://android-review.googlesource.com/#/q/Iffcbb650423db90194d17e028cd4518d61a3a33e), [b/170434992](https://issuetracker.google.com/issues/170434992))

**Bug Fixes**

- API lint check for MissingGetterMatchingBuilder is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9), [b/138602561](https://issuetracker.google.com/issues/138602561))
- Add test. ([I6b8ae](https://android-review.googlesource.com/#/q/I6b8ae3cf931bc18b948bf611e1056dfeba57d285))
- Enable transitions in ComposeTestRule; remove option to enable the blinking cursor from ComposeTestRule. ([If0de3](https://android-review.googlesource.com/#/q/If0de36db743b7f57b161b0fe6324565750436866))
- Added KeyboardCapitalization IME Option ([I8ac38](https://android-review.googlesource.com/#/q/I8ac3875c7c668bcd2868becd328bb3a253c667cd))
- Added single line keyboard option to CoreTextField ([I72e6d](https://android-review.googlesource.com/#/q/I72e6d9f84abbf4ff6a9ede5355de4c30d37c3d8c))
- Move SimpleContainer into PopupTestUtils.kt ([I65c3e](https://android-review.googlesource.com/#/q/I65c3ea4dfec4f69438495f8e60348b92e19abef3))
- Renamed Radius API to CornerRadius to better express how it is used throughout Compose. Updated documentation to indicate that negative corner radii are clamped to zero. ([I130c7](https://android-review.googlesource.com/#/q/I130c7e1baadaf1b2f8e6c32f1af0d3702e2cee50), [b/168762961](https://issuetracker.google.com/issues/168762961))
- Improved Android interop by continuing to send MotionEvents to child Android Views that return false for onTouchEvent for all actions except `ACTION_DOWN` ([I94c5a](https://android-review.googlesource.com/#/q/I94c5ae24d8fd33d8e2f3d0086ed53654a0a57fea), [b/170320973](https://issuetracker.google.com/issues/170320973))
- Box was made an inline function. ([Ibce0c](https://android-review.googlesource.com/#/q/Ibce0c1940173f06c030fd1115b9badb692ceb05a), [b/155056091](https://issuetracker.google.com/issues/155056091))

**External Contribution**

- Support different locales for `AnnotatedString.capitalize` and `AnnotatedString.decapitalize` ([I4aa7f](https://android-review.googlesource.com/#/q/I4aa7f34296538953954558e21598755a239ab79a))

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/ui)

**API Changes**

- Add a DSL for specifying inspector information ([Ic9a22](https://android-review.googlesource.com/#/q/Ic9a22ffea5cdc0bc34160512515aef2c576d9aae))
- Move LongPress into Text. ([Iff2bc](https://android-review.googlesource.com/#/q/Iff2bc6e44143bedf71442531f8ec2d37a40e4a19))
- Experimental Modifier.pointerInput suspending input modifier ([Ia77d2](https://android-review.googlesource.com/#/q/Ia77d26185ba835c33bf48015977667df31800dff))
- Added Copy/Paste/Cut accessibility actions ([I6db4f](https://android-review.googlesource.com/#/q/I6db4f570596e65c2e12fbc6f0821961c65671e98))
- Public constructor for AndroidOwner was removed ([Iacaef](https://android-review.googlesource.com/#/q/Iacaefaba493d99121144048bfaef04887374da35))
- Popups and dialogs now inherit FLAG_SECURE from parent Window. Also added option to configure this explicitly ([I64966](https://android-review.googlesource.com/#/q/I649663482e91757df751315b03fee9867b580e96), [b/143778148](https://issuetracker.google.com/issues/143778148), [b/143778149](https://issuetracker.google.com/issues/143778149))
- Consumption data is now mutable. Also
  calls to extension functions that do consumption
  now no longer return a new PointerInputChange, but
  instead mutate the provided PointerInputChange.

  This is the first step in a 2 step process to
  make PointerEvent data mutable such that other
  pointer data cannot be edited by user code. The
  second step will be to remove the
  `List<PointerInputChange>` return type from
  `PointerInputFilter.onPointerEvent(...)`. ([Id067e](https://android-review.googlesource.com/#/q/Id067e10b5022ca973842d50954a8829bd808ecb6))
- Disable Selection in Text, and a Demo. ([Ie7e97](https://android-review.googlesource.com/#/q/Ie7e97b1bf0efd89c08c2bb554a9e676bb2d21dff))

- Made onGloballyPositioned an inline function ([I15830](https://android-review.googlesource.com/#/q/I15830e3d1f990b9b29eb6b3a2ff460bb7f972e85))

- OnPositionedModifier is renamed to OnGloballyPositionedModifier
  and onPositioned() is renamed to onGloballyPositioned(). ([I587e8](https://android-review.googlesource.com/#/q/I587e8b151079d9d9506d86caa4283b7108958de4), [b/169083903](https://issuetracker.google.com/issues/169083903))

- The hasPendingMeasureOrLayout property was added to Owner, telling whether the Owner has any pending layout work. ([I3d9f8](https://android-review.googlesource.com/#/q/I3d9f82abd025055cbe3bfdb8cb834bf343b8134c), [b/169038599](https://issuetracker.google.com/issues/169038599))

- Added API to programmatically clear focus ([Ie1dc2](https://android-review.googlesource.com/#/q/Ie1dc27dd6d2d0260cdeb363f072bbb609ea10c19), [b/161487952](https://issuetracker.google.com/issues/161487952))

- Removed `PointerInputFilter.onPointerInput(...)`.
  `PointerInputFilter.onPointerEvent(...)` should be used in its place. ([I6f04a](https://android-review.googlesource.com/#/q/I6f04a771485232d62134c22588a0ae67c909bf81))

- Changes to Size

  - Removed Size.getFlipped
  - Removed Size.rem
  - Removed Size.truncDiv ([Ief44d](https://android-review.googlesource.com/#/q/Ief44db39b08553d0e1be5ba51cd590a4dedfcfee), [b/169790720](https://issuetracker.google.com/issues/169790720))
- As part of the standardization
  of sentinel values for inline classes,
  rename Color.Unset to Color.Unspecified
  for consistency with other inline classes ([I97611](https://android-review.googlesource.com/#/q/I9761102e79ade32812984466c020f2715065ac85), [b/169797763](https://issuetracker.google.com/issues/169797763))

- TextOverflow.None is introduced. When overflow is None, Text won't handle overflow anymore, and it will report its actual size to LayoutNode. ([I175c9](https://android-review.googlesource.com/#/q/I175c9163a70ed35e4390b10848f143ed30ed2bf3), [b/158830170](https://issuetracker.google.com/issues/158830170))

- The scope parameter within AnnotatedString.Builder.addStringAnnotation is renamed to tag for API consistency. ([I7c8cb](https://android-review.googlesource.com/#/q/I7c8cbce7ffa7ec32837b9e9e80c49e210b02d552))

**Bug Fixes**

- The scrolling performance of LazyColumn/Row is improved by doing less work in subcomposition on every scroll. The new hasInvalidations() method was added for Composition class. hasPendingChanges() method from Recomposer was renamed to hasInvalidations() ([Ib2f32](https://android-review.googlesource.com/#/q/Ib2f324dd6845fd83321e0d4f3fa6e502c346dbc3), [b/168293643](https://issuetracker.google.com/issues/168293643), [b/167972292](https://issuetracker.google.com/issues/167972292), [b/165028371](https://issuetracker.google.com/issues/165028371))
- Updated Size.Unspecified parameters to be Float.NaN instead of Float.POSITIVE_INFINITY. Updated Painter implementations to check against Size.Unspecified as well as non-finite Sizes. ([I95a7e](https://android-review.googlesource.com/#/q/I95a7e394ef1bc64d4deca510a681c9dbf959b1c1))
- The order of place() calls in custom Layouts now defines the drawing order for the children ([Ibc9f6](https://android-review.googlesource.com/#/q/Ibc9f6844b7309f45a8f3dadfdcda0a33b39425e6))
- Support AnnotatedString to SpannableString conversion for accessibility. ([Ief907](https://android-review.googlesource.com/#/q/Ief907a05b7928fa3c59784cda5c7a7739485607b))
- Added stubs for android classes that are on older platforms to avoid use of reflection when possible. ([Ia1790](https://android-review.googlesource.com/#/q/Ia179051916f28a9924ac9ad733f4b3a2ff6f9844))
- Fixed bug: If the software keyboard showing caused the app to translate, pointer input coordinates would become incorrect. ([Ic4cec](https://android-review.googlesource.com/#/q/Ic4cec6cf5134c024fe544f130676a4be2dfd00bd), [b/163077821](https://issuetracker.google.com/issues/163077821))

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/ui)
| **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

**API Changes**

- Added OwnerScope to allow collection of layout and drawing observation scopes once they are no longer valid. ([Ic4cf8](https://android-review.googlesource.com/#/q/Ic4cf8889e486e175e0f2405f1a0dc7a5a085ad99))
- Added OnRemeasuredModifier and onSizeChanged() to receive a callback when content layout has been remeasured and the size has changed, respectively. ([I657cf](https://android-review.googlesource.com/#/q/I657cf033de811e9279a2b2079933ca0bd89e5e60), [b/154108792](https://issuetracker.google.com/issues/154108792))
- Add long click semantics action ([I6281b](https://android-review.googlesource.com/#/q/I6281b383328d549b30b3ef915e717abbbb28ddaa), [b/156468846](https://issuetracker.google.com/issues/156468846))
- Made FocusManager private. ([I7872f](https://android-review.googlesource.com/#/q/I7872fd59410800f15727c3220796af1d270d5a7e))
- Updated implementation to create
  a dedicated DrawCacheModifier implementation
  instead of adding optional properties on DrawModifier.

  Updated documentation for various methods ([Ibd166](https://android-review.googlesource.com/#/q/Ibd16690b8519362fc74659e2c85c6decfb0dd431))
- Make TextRange inline to avoid object creation. ([Id034b](https://android-review.googlesource.com/#/q/Id034bee391b277905590a94dbb7198739ad1e848))

- PlacementScope#parentWidth and PlacementScope#parentLayoutDirection can no longer be read from the placement block of a custom layout. ([Icc1ae](https://android-review.googlesource.com/#/q/Icc1ae00d774147c5fa7006c4bb408c99c7731690), [b/168295623](https://issuetracker.google.com/issues/168295623))

- add AccessibilityScrollState to semantics properties. ([Ifeda9](https://android-review.googlesource.com/#/q/Ifeda983f0f6b8a2a92dea82c1a594fa5607f7cc3))

- Introduced Modifier.drawWithCache
  to support creating a drawing object
  that conditionally recreates dependencies
  that depend on size/state information ([I376dc](https://android-review.googlesource.com/#/q/I376dc757683caac4f330d2d525cf3d5ce2e531fc))

- ParagraphConstraints is removed. Width is directly passed to Paragraph now. ([Ica712](https://android-review.googlesource.com/#/q/Ica712c3f10be8ab7e684c108b2339119f50eafb7))

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
- Annotated rootAnimationClockFactory, transitionsEnabled, blinkingCursorEnabled and textInputServiceFactory with @VisibleForTesting, make them internal API and hide their kdoc ([I554eb](https://android-review.googlesource.com/#/q/I554ebefac18b216d51e387e5fd1c3a735fde9500), [b/168308412](https://issuetracker.google.com/issues/168308412))
- Remove SelectionContainer from the Top to disable default selection and avoid unexpected behavior. One can specifically use a SelectionContainer to wrap the content that needs to be selectable instead. ([I8dfe0](https://android-review.googlesource.com/#/q/I8dfe067d1a56ddb95c8fdd7fa2678e8ac43bba6b), [b/158459594](https://issuetracker.google.com/issues/158459594))

### Version 1.0.0-alpha03

September 16, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..18a5639262f8504db530176550e338a5d0e2e044/compose/ui)

**API Changes**

- Remove scroll forward/backward semantics actions. Added steps in AccessibilityRangeInfo. ([Ia47b0](https://android-review.googlesource.com/#/q/Ia47b0be6d058f36b07d2141ec33aca634e63b544))
- Removed `onInvalidate()` from `Owner` -- `OwnedLayer` handles invalidation. ([Ica72b](https://android-review.googlesource.com/#/q/Ica72b49b10b5f2bd25845cb6c9fc45f085b679e7), [b/162061312](https://issuetracker.google.com/issues/162061312))
- Removed operator methods on Size
  API that consume Offset parameters. The
  result of these operations is unclear
  and the type of result is unexpected
  for these. Ex. should size - offset return
  an offset or a size result with the difference?

  Also removed deprecated methods on Size class. ([Iec902](https://android-review.googlesource.com/#/q/Iec902c3664d8669534b8d7eca2b572e6a8d2838a), [b/166514214](https://issuetracker.google.com/issues/166514214))

**Bug Fixes**

- Fix for items of LazyColumn being incorrectly drawn sometimes, this was also causing crashes in some conditions. ([Ibcf17](https://android-review.googlesource.com/#/q/Ibcf1745e40606f6a38d9eb90f915443935d34403), [b/163066980](https://issuetracker.google.com/issues/163066980), [b/165921895](https://issuetracker.google.com/issues/165921895))
- DpConstraints and APIs using it were deprecated. ([I90cdb](https://android-review.googlesource.com/#/q/I90cdbe407ae8dd69badd26cd02bbb784ba10ba6a), [b/167389835](https://issuetracker.google.com/issues/167389835))
- Moved `createAndroidComposeRule` and `AndroidInputDispatcher` from `androidx.ui.test.android` to `androidx.ui.test` ([Idef08](https://android-review.googlesource.com/#/q/Idef08e5b796ba14140eafd054c8aa898a3d38feb), [b/164060572](https://issuetracker.google.com/issues/164060572))
- Usages of gravity were consistently renamed to align or alignment in layout APIs. ([I2421a](https://android-review.googlesource.com/#/q/I2421a4d640a7086079739cd0e569aef70bb48577), [b/164077038](https://issuetracker.google.com/issues/164077038))
- Added onNode and other global methods on ComposeTestRule as the current global ones are going to be deprecated. ([Ieae36](https://android-review.googlesource.com/#/q/Ieae36a4b67a3190759e7284a638f8b755c06c1ec))

### Version 1.0.0-alpha02

September 2, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/compose/ui)

**API Changes**

- remove callback to notify Owner when layoutnode bounds change. ([If654e](https://android-review.googlesource.com/#/q/If654ebfbf711c9a7f6bcddb28673e4b6f786d05b), [b/166106882](https://issuetracker.google.com/issues/166106882))
- Added support for filltype parameters on vector graphics paths to support cutouts of shapes according to evenOdd or NonZero path fill rules. ([I43dd2](https://android-review.googlesource.com/#/q/I43dd21d2d08f44979107b46d4f644ac5aef19f69))
- Uptime and Velocity are now inline classes ([I48f4a](https://android-review.googlesource.com/#/q/I48f4ad4311b0e05694a0ad0f008820e9e6102098))
- Duration is now an inline class ([I565eb](https://android-review.googlesource.com/#/q/I565eb86145c866c18ceb35fc6b4065aba0ceb25f))
- Add a callback to notify Owner when layoutnode bounds change. ([Ic40b3](https://android-review.googlesource.com/#/q/Ic40b3c0c68a4ae5eb06ec2b9bd207037dff2c505))
- Fixed issue where Rect function constructor
  with Offset and radius would create the Rect in the
  order of left, right, top, bottom instead of
  left, top, right, bottom.

  Removed deprecated companion methods on Rect in
  favor of function constructors.

  Added tests to verify methods in Rect.kt ([I08460](https://android-review.googlesource.com/#/q/I0846006bd0ec7f1a0effd90490c93002b42e132b), [b/165822356](https://issuetracker.google.com/issues/165822356))

**Bug Fixes**

- Added MutableRect, a rectangle that can be modified. ([I71bd2](https://android-review.googlesource.com/#/q/I71bd20996a79aa72f33a1287e57e18d94c2cc504), [b/160140398](https://issuetracker.google.com/issues/160140398))
- Matrix4 was replaced with Matrix. All other parts of vectormath package have been removed. ([Ibd665](https://android-review.googlesource.com/#/q/Ibd66522490b861d85a7539176a4f105e20c31a66), [b/160140398](https://issuetracker.google.com/issues/160140398))
- The calling convention for composable functions has
  changed. This is a binary breaking change. All libraries must be
  recompiled to work with this version of the compose compiler plugin.

  This change does not create a source level breaking change as the
  only APIs that have changed are compiler APIs that have an explicit
  opt in. ([I7afd2](https://android-review.googlesource.com/#/q/I7afd2d7b19652ec92b8d6d1d1e92f0745968aa66), [b/158123185](https://issuetracker.google.com/issues/158123185))
- Fixed crash that could occur when
  dispatch to a PointerInputFilter could cause
  the PointerInputFilter to be synchronously removed. ([I58f25](https://android-review.googlesource.com/#/q/I58f253629761b39591e5fdf5b8553d352287d11c))

### Version 1.0.0-alpha01

August 26, 2020

`androidx.compose.ui:ui-*:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c93ac38a59f31e5db0eab67687532a4ba61913d5/ui)

## Version 0.1.0-dev

### Version 0.1.0-dev17

August 19, 2020

`androidx.compose.ui:ui-*:0.1.0-dev17` is released. [Version 0.1.0-dev17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/ui)

**API Changes**

- `emitView` was deprecated. Use `AndroidView` instead if possible for emitting Views inside Compose. Note that composing Views and ViewGroups directly will not be supported in the future unless these are leaves in the composition tree, case when this can be achieved using AndroidView. ([I29b1e](https://android-review.googlesource.com/#/q/I29b1e5405077f45e101eacfb26a1ebed85120444), [b/163871221](https://issuetracker.google.com/issues/163871221))
- `FocusState2` is deprecated and replaced by `FocusState` ([Ia8b79](https://android-review.googlesource.com/#/q/Ia8b79200f0353a823290a1fb7c2c909f99fd009f), [b/160822876](https://issuetracker.google.com/issues/160822876), [b/160923332](https://issuetracker.google.com/issues/160923332))
- The deprecated AndroidView overloads were removed. ([I946b9](https://android-review.googlesource.com/#/q/I946b92952ecfcd9f2211fa713e75f3fbcef2ea71), [b/163802393](https://issuetracker.google.com/issues/163802393))
- Custom emits can now declare that one or more of its setters can be skipped and recomposed independently of the emit. ([Ibbd13](https://android-review.googlesource.com/#/q/Ibbd13068440252724db405b26d1f6be179e80411))
- Changed Vector classes to no longer
  be data classes as the same object instance is
  used for composition.

  Added mutableStateOf flag for VectorPainter
  to conditionally re-draw if contents of the
  vector change.

  Refactored VectorComponent instance to be
  part of VectorPainter as it is re-used
  across compositions.

  Updated GroupComponent and PathComponent
  to have their name fields be mutable ([Ieae45](https://android-review.googlesource.com/#/q/Ieae454490e274d51a03433b6506319f692f7d981), [b/151378808](https://issuetracker.google.com/issues/151378808))
- Removed `onChildPositioned` and `OnChildPositionedModifier`.
  Developers should use `onPositioned` and `OnPositionedModifier`
  on the child layout instead. ([I4522e](https://android-review.googlesource.com/#/q/I4522e2cd4a0edb08fd36212eacf19d2895ae87f7), [b/162109766](https://issuetracker.google.com/issues/162109766))

- Offset has become an inline class ([Iaec70](https://android-review.googlesource.com/#/q/Iaec70bb466cae8964f03e7484c1e86857c924f82))

- Added a modifier param to SelectionContainer ([I4aada](https://android-review.googlesource.com/#/q/I4aadafd87d5705b96f73cd49af84728a463c1cc5), [b/161487952](https://issuetracker.google.com/issues/161487952))

- Removed deprecated FocusModifier ([I0b4ba](https://android-review.googlesource.com/#/q/I0b4ba5c6f28b683787848042af76ac9ec20c7caf), [b/160922116](https://issuetracker.google.com/issues/160922116), [b/160821157](https://issuetracker.google.com/issues/160821157), [b/162441435](https://issuetracker.google.com/issues/162441435), [b/160822875](https://issuetracker.google.com/issues/160822875), [b/160921940](https://issuetracker.google.com/issues/160921940))

- Added `mergePolicy` lambda to `SemanticsPropertyKey`. This can be
  used to define a custom policy for mergeAllDescendants semantics
  merging. The default policy is to use the parent value if already
  present, otherwise the child value. ([Iaf6c4](https://android-review.googlesource.com/#/q/Iaf6c4cc327017ee492f4d8334c8df5167d33df58), [b/161979921](https://issuetracker.google.com/issues/161979921))

- Constraints is now an inline class ([I88736](https://android-review.googlesource.com/#/q/I88736be04376359506a2e8b4d599975c4f13aa01))

- Added FocusManager that moves common focus logic out of AndroidComposeView ([I528ef](https://android-review.googlesource.com/#/q/I528ef86e1599baed36b70054b966a47dc016260d), [b/161487952](https://issuetracker.google.com/issues/161487952), [b/162206799](https://issuetracker.google.com/issues/162206799))

- Updated PointerEventPass names for Alpha release. ([Ifda6f](https://android-review.googlesource.com/#/q/Ifda6fd7d3b77f1fa4c2bb8781783728d6d15a1e0))

- IntOffset is now an inline class ([Iac0bf](https://android-review.googlesource.com/#/q/Iac0bf89bb95642bf3a77073aead2cbce4c0e2e37))

- IntSize is now an inline class ([I2bf42](https://android-review.googlesource.com/#/q/I2bf426245b41f4189dead45114e3791bbceb9d13))

- `PlacementScope.placeAbsolute()` was renamed to `PlacementScope.place()`, and the previous `PlacementScope.place()` was renamed to `PlacementScope.placeRelative()`. As a result, the `PlacementScope.place()` method will not automatically mirror the position in right-to-left contexts anymore. If this is desired, use `PlacementScope.placeRelative()` instead. ([I873ac](https://android-review.googlesource.com/#/q/I873ac827e6c4d4bf6c85a80b7128174c61602945), [b/162916675](https://issuetracker.google.com/issues/162916675))

- AlertDialog now uses FlowRow for buttons ([I00ec1](https://android-review.googlesource.com/#/q/I00ec1052c1e452380cda3a95bdb3ae5b74c5511e), [b/161809319](https://issuetracker.google.com/issues/161809319), [b/143682374](https://issuetracker.google.com/issues/143682374))

- Made some test utilities non
  public because they are not where they
  belong. Will be made public in the future. ([I32ab1](https://android-review.googlesource.com/#/q/I32ab1fdeff164695b29f95adb0292c3fae1195c4))

- Refactored organization of pointer input
  code. ([Ie3f45](https://android-review.googlesource.com/#/q/Ie3f45d957c67adefc00c5150e9c4575acb9bf9c8))

- Deprecated PxBounds in
  favor of Rect. Updated all usages
  of PxBounds with rect and added
  proper deprecate/replace with
  annotations to assist with the
  migration. ([I37038](https://android-review.googlesource.com/#/q/I370384202fff3e5b147d42086f4350ab7fa830de), [b/162627058](https://issuetracker.google.com/issues/162627058))

- Removed Deprecated KeyEvent2. Use KeyEvent instead. ([Ied2d0](https://android-review.googlesource.com/#/q/Ied2d05dcdca3b213d248ff1979fcc1a5e8d895b9), [b/162097587](https://issuetracker.google.com/issues/162097587))

- KeyEvent has a unicode property that can be used to get the unicode character generated by the specified key and meta key state combination ([If3afc](https://android-review.googlesource.com/#/q/If3afc9df182bf7269a61f9ca4ccffceac5836c38))

- Made the DelayUp custom event
  and related classes an opt in API as it
  is very likely going to be changed. ([I56d6f](https://android-review.googlesource.com/#/q/I56d6f7f6f3cb37a3b530d2256c657530d8b2e976))

- Removed 2 PointerEventPasses that are no longer
  needed. ([I3dd9d](https://android-review.googlesource.com/#/q/I3dd9d7871ec6e82b548a4c029d10257e4974bbbc))

- Add parameter color, shadow and TextDecoration to Paragraph.paint This function is useful to avoid unnecessary Paragraph recreation. ([I81689](https://android-review.googlesource.com/#/q/I81689d5d928ab10ba6cb567c12a115a0dd9449a5))

**Bug Fixes**

- Removed onFocusChanged callbacks from TextField. Use Modifier.focusObserver instead. ([I51089](https://android-review.googlesource.com/#/q/I51089bfbc858ea302770f92b13886818cf48ba9c), [b/161297615](https://issuetracker.google.com/issues/161297615))
- Modifier.drawBorder has been deprecated. Use Modifier.border instead. Border data class has been replaced by BorderStroke ([I4257d](https://android-review.googlesource.com/#/q/I4257d62b222e27c9ad67e1b2581b162cc9392c9e), [b/158160576](https://issuetracker.google.com/issues/158160576))
- Removed deprecated FrameManager calls.

  Internal compose APIs have been changed to reduce the amount of
  overhead to track state objects such as `mutableStateof()` ([I80ba6](https://android-review.googlesource.com/#/q/I80ba67ebf59f9399e673b6218edfca4249158f82))
- VerticalScroller and HorizontalScroller have been removed. Use ScrollableColumn/Row instead. Modifier.drawBackground has been removed. Use Modifier.background ([I73b0d](https://android-review.googlesource.com/#/q/I73b0d940455a0a8e8dd18b5a483b12707f599304), [b/163019183](https://issuetracker.google.com/issues/163019183))

- Crash when something which saves the state was used inside the for loop is fixed. Now having the same key in savedInstanceState() is allowed, api of UiSavedStateRegistry is now adjusted to this new requirement ([I4ab76](https://android-review.googlesource.com/#/q/I4ab7630120ffce145d1bf09d52a475d197030150), [b/160042650](https://issuetracker.google.com/issues/160042650), [b/156853976](https://issuetracker.google.com/issues/156853976), [b/159026663](https://issuetracker.google.com/issues/159026663), [b/154920561](https://issuetracker.google.com/issues/154920561))

- The `state { ... }` composable is now deprecated in favor of
  explicit calls to `remember { mutableStateOf(...) }` for clarity.
  This reduces the overall API surface and number of concepts for state
  management, and matches the `by mutableStateOf()` pattern for class
  property delegation. ([Ia5727](https://android-review.googlesource.com/#/q/Ia57278556d4f35ecf2cf5e6e30888b0d1f1f8012))

- Renamed RRect to RoundRect
  to better fit compose naming patterns
  Created similar function constructors
  to RRect and deprecated RRect function
  constructors ([I5d325](https://android-review.googlesource.com/#/q/I5d32529a133bc2f69ea1de94c2912b2748a0d678))

### Version 0.1.0-dev16

August 5, 2020

`androidx.compose.ui:ui-*:0.1.0-dev16` is released. [Version 0.1.0-dev16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d/ui)

**API Changes**

- OnChildPositioned has been deprecated. Use OnPositioned on the child instead. ([I87f95](https://android-review.googlesource.com/#/q/I87f95da597607cbc534647def3b1a39527dcdeaa), [b/162109766](https://issuetracker.google.com/issues/162109766))
- setViewContent was deprecated. setContent should be used instead. ([I7e497](https://android-review.googlesource.com/#/q/I7e49740d26f42e9326cb5582a4522d74957b90fe), [b/160335130](https://issuetracker.google.com/issues/160335130))
- Added the AndroidViewBinding API for inflating and composing layout resources, based on ViewBinding. ([I081c6](https://android-review.googlesource.com/#/q/I081c698b4961d5ef2cfeedd49ff33a2a4b7f7886))
- KeyEvent2 is replaced by KeyEvent ([I2d770](https://android-review.googlesource.com/#/q/I2d77004dc241ade2042effd1ff8e93762fc72dda), [b/162097585](https://issuetracker.google.com/issues/162097585))
- Added support for Alt hardware key ([I9036b](https://android-review.googlesource.com/#/q/I9036b3e3941f14c0623ee48efa50cc209c0e9e8b))
- FocusManager is Deprecated. Use Modifier.focus(), Modifier.focusObserver() and Modifier.focusRequester() instead. ([I74ae4](https://android-review.googlesource.com/#/q/I74ae41f8a0ad2fa1c5f614f57dcb67b969d9e5d3), [b/162211322](https://issuetracker.google.com/issues/162211322))
- loadVectorResource supports trimPath attributes ([I808fe](https://android-review.googlesource.com/#/q/I808feb22bb1a04e78441097726a2de0f373fecc7))
- Move dialog to ui ([I47fa6](https://android-review.googlesource.com/#/q/I47fa618a788e598182b782eab755defccaf45ebb))
- Removed 2 PointerEventPasses that are no longer needed. ([I33ca7](https://android-review.googlesource.com/#/q/I33ca77cee9c0c030d8495b2113e798e449bacbfd))
- Implemented PointerInteropModifier which provides the ability to receive MotionEvents and interact with Compose as if you are an implementation of an Android View. ([Ieb08c](https://android-review.googlesource.com/#/q/Ieb08cb00b2a70e3b4263640200cb2219b1fa728c))
- Removed the deprecated tag modifier. Please use layoutId instead. ([Idaa05](https://android-review.googlesource.com/#/q/Idaa051ac5c7f60703e8499c8d229a2b2f750a7a9), [b/162023919](https://issuetracker.google.com/issues/162023919))
- The APIs for right-to-left support has been updated. LayoutDirectionAmbient has been added, which can be used to read and change the layout direction. Modifier.rtl and Modifier.ltr have been removed. ([I080b3](https://android-review.googlesource.com/#/q/I080b3cb674dc32af5fbe7e696228ac21f0720d72))
- Support path trimming in vector graphics ([Ie16c9](https://android-review.googlesource.com/#/q/Ie16c93cdb5dc389a818418e7729d58b7999b68af), [b/158188351](https://issuetracker.google.com/issues/158188351))
- Added Modifier.layout() that allows to create a custom layout modifier conveniently ([I73b69](https://android-review.googlesource.com/#/q/I73b699f2434a2c8ca0400fca1c331997c09a44e9), [b/161355194](https://issuetracker.google.com/issues/161355194))
- Added a new AndroidView API and deprecated the existing ones. ([I5bcfd](https://android-review.googlesource.com/#/q/I5bcfd9c9945fecb3e55fe95d6528d8391ac7b961))
- Modifier.plus has been deprecated, use Modifier.then instead. 'Then' has a stronger signal of ordering, while also prohibits to type `Modifier.padding().background() + anotherModifier`, which breaks the chain and harder to read ([Iedd58](https://android-review.googlesource.com/#/q/Iedd587edbed0ba964ef203a66b98be7297147bd7), [b/161529964](https://issuetracker.google.com/issues/161529964))
- Add \[Abstract\]ComposeView View subclasses for hosting Compose content in a View hierarchy. ([I46357](https://android-review.googlesource.com/#/q/I4635790610de55ca7ffd6de72485e243196112a8))
- `Row` and `Column` are now inline function significantly reducing the overhead of using them. ([I75c10](https://android-review.googlesource.com/#/q/I75c10e663b74ffc250a3293df7583fcd86ea891a))
- SubcomposeLayout is added. It is a low level primitive which allows to compose the children during the measuring if we want to use some values available only later during the measure for the subtree composition. For example WithConstraints is not implemented using SubcomposeLayout. ([I25cc8](https://android-review.googlesource.com/#/q/I25cc8cfe8382db1ef61e93866ba08f4668cbc734))
- Added `SemanticsNode.positionInRoot` to get the position of a SemanticsNode relative to the root of the Compose hierarchy ([Icdf26](https://android-review.googlesource.com/#/q/Icdf262558341d6441ae91dfb8807d19f88f5b3fb), [b/161336532](https://issuetracker.google.com/issues/161336532))
- MotionEvents passed all the way through from Android, into Compose, and back into Android. ([I14be8](https://android-review.googlesource.com/#/q/I14be8bd67609696bf3e8950feb0bb54367786b81), [b/158034713](https://issuetracker.google.com/issues/158034713))
- Removed dropdownPopup. ([I00430](https://android-review.googlesource.com/#/q/I00430bd9ee70cba47019034392bf6263497d85e8))
- Fixed popup position on cut-out displays. ([Idd7dd](https://android-review.googlesource.com/#/q/Idd7ddf5f88728a96fc8ff725a39979fe962e8889))
- Add accessibility action to get TextLayoutResult ([I9d6e6](https://android-review.googlesource.com/#/q/I9d6e6313528500524f04638ccb5742fcfbb41392))
- RemeasurementModifier added. it allows to synchronously remeasure the layout. In general you never need it as remeasure/relayout is happening automatically, but we use it inside LazyColumnItems during the scroll. ([I5f331](https://android-review.googlesource.com/#/q/I5f33173ba1f76153139fa086fef4e2a86d010282), [b/160791058](https://issuetracker.google.com/issues/160791058))
- Remove getLineEllipsisOffset/getLineEllipsisCount. Use getLineVisibleEnd/getLineEnd/isLineEllipsized instead. ([I85aa2](https://android-review.googlesource.com/#/q/I85aa258d57056cbdae2816b14ce1af313023020c))
- Add some Marks/Annotations for best practice reason. ([I66b20](https://android-review.googlesource.com/#/q/I66b206ffe0fe1a5ceb88bf0b0a2b0d84f2c3f6bd))
- expose more line APIs in TextLayoutResult. ([I79bd2](https://android-review.googlesource.com/#/q/I79bd278c138c53477f3cbaf811d4bdcfe03b3dc3))
- Built-in vector converters to convert built-in units are now accessible via Foo.VectorConverter. e.g. Dp.VectorConverter, Color.VectorConverter, Float.VectorConverter, etc ([I3e273](https://android-review.googlesource.com/#/q/I3e2734f9712d94cc664184d35d495edab50bda53))

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
- Updated compose BlendMode API consumption to properly map between Android framework BlendModes and PorterDuff modes depending on API level. Introduced BlendMode#isSupported API to act as a capability query to determine if the BlendMode is supported on the device before it is used. ([I0ef42](https://android-review.googlesource.com/#/q/I0ef42dfc77e9813c277454c97f8f6ce4f6b9e9de))
- LazyItemScope was added for itemContent param of Lazy lists. It provides modifiers to fill the parent max size which solves the use case when the item should fill the viewport and the regular Modifier.fillMaxSize() doesn't work as the item is measured with infinity constraints. ([Ibd3b2](https://android-review.googlesource.com/#/q/Ibd3b21685641c22f7deaab1bb71785d8d6135058), [b/162248854](https://issuetracker.google.com/issues/162248854))
- Removed `SemanticsNodeInteraction.performPartialGesture`. Use `SemanticsNodeInteraction.performGesture` instead. ([Id9b62](https://android-review.googlesource.com/#/q/Id9b628ebe475c8a067118320b26a7b2461e98129))
- `LazyColumnItems` was renamed to `LazyColumnFor`. `LazyRowItems` was renamed to `LazyRowFor` ([I84f84](https://android-review.googlesource.com/#/q/I84f843793994276f1ccb9f21464c4b74629aaf12))
- `foundation.shape.corner` package was flattened to `foundation.share` ([I46491](https://android-review.googlesource.com/#/q/I464919cb74f8941c2a02f14dea0aa417febf3691), [b/161887429](https://issuetracker.google.com/issues/161887429))
- Renamed `AndroidComposeTestRule` to `createAndroidComposeRule`. ([I70aaf](https://android-review.googlesource.com/#/q/I70aaf550e1bff2871b9732cc5abf58e9af1479fe))
- Added more APIs to `TextLayoutResult`. ([Id7e04](https://android-review.googlesource.com/#/q/Id7e043fd17351ba68b80f51a376925916b541963))
- Material `FilledTextField` was renamed to `TextField` and foundational `TextField` was renamed to `BaseTextField` to make simplest desired API easy to discover and use ([Ia6242](https://android-review.googlesource.com/#/q/Ia62420a7a2231c02b6874a9a2867bf786a397ed3), [b/155482676](https://issuetracker.google.com/issues/155482676))
- Modifier.drawBackground has been renamed to Modifier.background ([I13677](https://android-review.googlesource.com/#/q/I1367723fce0e07418ed4ab391fe20c69aa092f53))

### Version 0.1.0-dev15

July 22, 2020

`androidx.compose.ui:ui-*:0.1.0-dev15` is released. [Version 0.1.0-dev15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/ui)

#### Dependencies Update

- To use the `0.1.0-dev15` version of Compose, you will need to update your dependencies according to the new code snippets shown above in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose-ui#declaring_dependencies).

**API Changes**

- FocusModifier is deprecated in favor of Modifier.focus, Modifier.focusRequester, Modifier.focusObserver. FocusState and FocusDetailedState are deprecated in favor of FocusState2 ([I46919](https://android-review.googlesource.com/#/q/I469196b76ebe08130fa4df9ed297f111abddd8b1), [b/160822875](https://issuetracker.google.com/issues/160822875), [b/160922136](https://issuetracker.google.com/issues/160922136))
- Added a modifier to observe focus state change. ([I05866](https://android-review.googlesource.com/#/q/I05866104c323317f41f43ce1c286236b7e344d4b), [b/160924455](https://issuetracker.google.com/issues/160924455), [b/160923326](https://issuetracker.google.com/issues/160923326))
- Added a modifier to request focus changes ([I8dd73](https://android-review.googlesource.com/#/q/I8dd73cf3ce77e112a9f97f203b8ec7a0f07bc706), [b/161182057](https://issuetracker.google.com/issues/161182057), [b/160924778](https://issuetracker.google.com/issues/160924778))
- Ajdust the Toolbar Menu to show copy, cut, paste properly. ([Id3955](https://android-review.googlesource.com/#/q/Id3955ab3845cc6ad1807b95bc39e73facf0fd358))
- Single-value semantics properties now use a calling style. For example, 'semantics { hidden = true }' is now written as: `semantics { hidden() }`. ([Ic1afd](https://android-review.googlesource.com/#/q/Ic1afd12ea22c926babc9662f1804d80b33aa0cfc), [b/145951226](https://issuetracker.google.com/issues/145951226), [b/145955412](https://issuetracker.google.com/issues/145955412))
- Added Modifier.focus which replaces FocusModifier. ([Ib852a](https://android-review.googlesource.com/#/q/Ib852a056a0f3c76757f0fdef07e75e82bf178b8d), [b/160924778](https://issuetracker.google.com/issues/160924778))
- Add FloatingToolbar for TextField Selection. ([Ie8b07](https://android-review.googlesource.com/#/q/Ie8b07e4405940f9d4b4147c34406c80a557b4d45))
- Added an experimental api annotation for key input related API ([I53c0a](https://android-review.googlesource.com/#/q/I53c0a52af14dd832170f774cbb638c253abd639d))
- Added an experimental api annotation for all Focus-related API ([I53b24](https://android-review.googlesource.com/#/q/I53b247a7feb23bd99b5f15f2cf0cfaddb104a888), [b/160903352](https://issuetracker.google.com/issues/160903352))
- Added FocusState2 which will replace FocusDetailedState ([I0a3ba](https://android-review.googlesource.com/#/q/I0a3ba4e87508dd29e0c355114c4caccb3252ac84), [b/160822595](https://issuetracker.google.com/issues/160822595))
- Added ExperimentalFocus which is an @OptIn annotation for Focus API. ([I1544b](https://android-review.googlesource.com/#/q/I1544bc717d24434ccc2295244ddb6bf7b2dde3c8), [b/160820961](https://issuetracker.google.com/issues/160820961))
- An IntBounds unit class has been added, representing integer pixel bounds from layout. The API of PopupPositionProvider has been updated to use it. ([I0d8d0](https://android-review.googlesource.com/#/q/I0d8d03c5535c80c6808d8f9ca7a210408890e6e7), [b/159596546](https://issuetracker.google.com/issues/159596546))
- Applier now requires a clear() method for disposing compositions ([Ibe697](https://android-review.googlesource.com/#/q/Ibe697b06ea885852731d029ef56da657b5f290dc))
- KeyEvent is deprecated and replaced by KeyEvent2 ([I68730](https://android-review.googlesource.com/#/q/I687305a80a4caff2645d87bfac108205028f9f44))
- A new optional flag useUnmergedTree was added to test finders. ([I2ce48](https://android-review.googlesource.com/#/q/I2ce48556aa3b0a0c73f4a56a0d9eed63eda49160))
- Made LayoutNode experimental API ([I4f2e9](https://android-review.googlesource.com/#/q/I4f2e93737020b0993f8ba5671e2a0a87f5de3ce2))
- Added copy methods to various
  inline class types including:

  - Offset
  - Size
  - Radius
  - Motion
  - TransformOrigin

  - Deprecated Size.copy companion object method
    favor of instance copy method ([Ife290](https://android-review.googlesource.com/#/q/Ife2903a0277e051188884cb5d5feefcae8875dd1), [b/159905651](https://issuetracker.google.com/issues/159905651))

- Popups, Dialogs and Menus are now inheriting the contextual MaterialTheme ([Ia3665](https://android-review.googlesource.com/#/q/Ia3665905218b4d12d7a9bd121a69a51569d82694), [b/156527485](https://issuetracker.google.com/issues/156527485))

- TextDirection is renamed as ResolvedTextDirection ([I3ff38](https://android-review.googlesource.com/#/q/I3ff38ad5993a0b844dced711e38c729d2b0c8697))

- Removed layout direction parameter from the measure block of the Layout() function. Layout direction is however available inside the callback through the measure scope object ([Ic7d9d](https://android-review.googlesource.com/#/q/Ic7d9d797938e6e2a91916836e5e9688794115c22))

- Refactor SelectionHandles for reusing. ([I420e0](https://android-review.googlesource.com/#/q/I420e0c6a5c00684ac9b4e2afb5ad1fec97668e38))

- Clickable was removed. Use Modifier.clickable ([I84bdf](https://android-review.googlesource.com/#/q/I84bdf2bc75e8ccda44afbe9db49d4c879703309b))

- TestTag and Semantics have been deleted.
  Use Modifier.testTag and Modifier.semantics instead ([I15ff0](https://android-review.googlesource.com/#/q/I15ff0bece5791ff8adae20c3c1bcaf48cea7f1b0), [b/158841414](https://issuetracker.google.com/issues/158841414))

- Prior to this change, the compose compiler plugin would non-trivially intercept calls to constructors inside of a @Composable function if there was an ([I5205a](https://android-review.googlesource.com/#/q/I5205af707238a70d600c105843cd99e88a5381e0), [b/158123804](https://issuetracker.google.com/issues/158123804))

- Modifier.tag was renamed to Modifier.layoutId, to avoid confusion with Modifier.testTag. ([I995f0](https://android-review.googlesource.com/#/q/I995f09d0722964ad8a5708c7299e4c6f52bec1c5))

- Alignment line Int positions returned from Placeable#get(AlignmentLine) are now non-null. If the queried alignment line is missing, AlignmentLine.Unspecified will be returned. ([I896c5](https://android-review.googlesource.com/#/q/I896c5ef8a18919aa84413669341e716bf676e32e), [b/158134875](https://issuetracker.google.com/issues/158134875))

- The AndroidView composable was added a modifier parameter. ([I48a88](https://android-review.googlesource.com/#/q/I48a88f9f907dd8bcf8153ce0f7d3f93cff961d9d), [b/158746303](https://issuetracker.google.com/issues/158746303))

- Semantics() is deprecated. Use Modifier.semantics() instead. ([I72407](https://android-review.googlesource.com/#/q/I72407fe09b5fe663baaa1e3a788107f0675eb10c), [b/158841414](https://issuetracker.google.com/issues/158841414))

- Add viewModel() composable which allows to create or get already created ViewModel similarly to how it works in Activity or Fragment ([I5fdd1](https://android-review.googlesource.com/#/q/I5fdd19bccbb57252e928b0f65097678022f860ef))

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

- TestTag is now deprecated. Use Modifier.testTag instead. ([If5110](https://android-review.googlesource.com/#/q/If5110df5865f5933d10d54a8aacba58f8cd1c712), [b/157173105](https://issuetracker.google.com/issues/157173105))

- The default, no-op, implementation of ParentDataModifier#modifyParentData has been removed - it was equivalent to not implementing the interface in the first place. ([I0deaa](https://android-review.googlesource.com/#/q/I0deaa7c824bb5a127f6358894ff2131296c0cecb))

- Previously deprecated ScaleFit as
  removed. Use ContentScale instead. ([Ifbc5b](https://android-review.googlesource.com/#/q/Ifbc5b150883fd4c62e31a1988371f569bed0340c))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I19d02](https://android-review.googlesource.com/#/q/I19d02beca10c30e9b6b444be0c2dd21227e30e9c))

- Added the DropdownMenu component in ui-material, a Material Design menu implementation. ([I9bb3d](https://android-review.googlesource.com/#/q/I9bb3d43fc1bb60cd0fed933c76b9d58cc5211514))

- Removed deprecated LayoutTag(), please use Modifier.tag() instead.
  Removed deprecated Modifier.matchParent(), please use Modifier.matchParentSize() instead. ([If8044](https://android-review.googlesource.com/#/q/If8044397663695ed258a1c8f8c01caa70ff2064f))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([I57bff](https://android-review.googlesource.com/#/q/I57bff9fbed3da9c71e8f5b24bbe75296d7275769))

- Modifier.semantics has been undeprecated to allow usages for high level components. ([I4cfdc](https://android-review.googlesource.com/#/q/I4cfdc837d5ac2d240af5a5ac6b755aebf800af15))

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

- DoubleTapGestureFilter now
  disambiguates SingleTapGestureFilter
  across the tree. ([If92b1](https://android-review.googlesource.com/#/q/If92b1647f11c296103c26b5f7e9e031add94323e))

- Updated Alignment API and added support for absolute alignment (which does not auto-mirror in Rtl context) ([I38cd3](https://android-review.googlesource.com/#/q/I38cd32c487c9dd72486476943c28afbed96aaf4e))

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

- WithConstraints trailing lambda API has been changed. Now instead of two params it has a receiver scope which in addition to constraints and layoutDirection provides minWidth, maxWidth, minHeight and maxHeight properties in Dp ([I91b9a](https://android-review.googlesource.com/#/q/I91b9af740cd2613ddd4fe6d63cd539a46b52fc52), [b/149979702](https://issuetracker.google.com/issues/149979702))

- Renamed LayoutModifier2 to LayoutModifier. ([Id29f3](https://android-review.googlesource.com/#/q/Id29f36d6b19674d189abb198a7656562b3b310b5))

- Removed deprecated LayoutModifier interface. ([I2a9d6](https://android-review.googlesource.com/#/q/I2a9d6a9840072d5cb92e68155be2d07de8411d04))

- Intrinsic measurements functions in Layout and LayoutModifier2 have an IntrinsicMeasureScope receiver now which provides intrinsics query API with implicitly propagated layout direction. ([Id9945](https://android-review.googlesource.com/#/q/Id9945cb41842df9f99132679b5b68a0f0edda53d))

- Layout and LayoutModifier children can be measured with a different layout direction. ([Ibd731](https://android-review.googlesource.com/#/q/Ibd7319b7caa93b2bc7fb38df3678e2bb8298652e))

- New Modifier.zIndex() is added to control the drawing order of the children within the same parent layout. elevation property on DrawLayerModifier is renamed to shadowElevation and doesn't control the drawing order anymore. The params order fo DrawShadow is changed: elevation is now the first one and the shape is the second one with a RectangleShape default. ([I20150](https://android-review.googlesource.com/#/q/I201506a33a55a4c48a4dbb6fe4e580824410588f), [b/152417501](https://issuetracker.google.com/issues/152417501))

- Removed onSizeChange and onPositionChange in Owner. ([I5c718](https://android-review.googlesource.com/#/q/I5c718529e3d46b765d00e307092228dde761ca4d))

- Added Constraints2, a copy of Constraints that does
  only supports Int connstraints values rather than IntPx. IntPx
  will be removed and all integer constraints will be assumed to
  be pixels like Android.

  - Added IntSize as well, which will eventually replace IntPxSize. ([I4b43a](https://android-review.googlesource.com/#/q/I4b43a8b15e346138d3bd40427791d89472782e38))
- Made Alignment instantiable with arbitrary values. Added 1D Alignments. ([Ia0c05](https://android-review.googlesource.com/#/q/Ia0c05cfa122108b48ac22de310ee98e0460f7f3f))

- alignToSiblings now accepts a Measured instead of Placeable. ([I5788d](https://android-review.googlesource.com/#/q/I5788dd1dab4d18c475e51a1e9a0440aba2bbc794))

- ([I45f09](https://android-review.googlesource.com/#/q/I45f09c681afda9c83483b20405ec21292593b41a), [b/152842521](https://issuetracker.google.com/issues/152842521))

  - Renamed ScaleFit to ContentScale
  - Moved ContentScale from ui-graphics to ui-core module to live in the same module as the Alignment API.
  - Renamed FillMaxDimension to Crop
  - Renamed FillMinDimension to Fit
  - Renamed Fit to Inside to better match
  - ImageView.ScaleType equivalents
  - Added documentation indicating that the combination of Crop and Alignment.Center achieves the same result as ImageView.ScaleType.CENTER_CROP and Fit used with Alignment.Center achieves the same result as ImageView.ScaleType.FIT_CENTER Inside used with Alignment.Center achieves the same result as ImageView.ScaleType.CENTER_INSIDE
- Rtl support for draw modifiers. ([I0aaf9](https://android-review.googlesource.com/#/q/I0aaf9072582e51e967d403cfec1d39f89680fc71))

- Released API for inflating Android Views from XML. See ViewInCompose demo for more details. ([I42916](https://android-review.googlesource.com/#/q/I42916dddd66770e866437232e3d1e118197de297))

- Improve DrawModifier API:

  - Made the receiver scope for draw() ContentDrawScope
  - Removed all parameters on draw()
  - DrawScope has same interface as former CanvasScope
  - ContentDrawScope has drawContent() method ([Ibaced](https://android-review.googlesource.com/#/q/Ibaced5feb8778510b8fe78e96f4fd3da1a6fda50), [b/152919067](https://issuetracker.google.com/issues/152919067))
- Added positionInParent and boundsInParent for LayoutCoordinates. ([Icacdd](https://android-review.googlesource.com/#/q/Icacdd0909bc434cd5fd935c46e0a07b965c6a38d), [b/152735784](https://issuetracker.google.com/issues/152735784))

- DrawLayerModifier and drawLayer() now default clipToBounds
  and clipToOutline to false. ([I0eb8b](https://android-review.googlesource.com/#/q/I0eb8b08323e0031cae87194d407351e6bdf5e189), [b/152810850](https://issuetracker.google.com/issues/152810850))

- Renamed LayoutResult to MeasureResult. ([Id8c68](https://android-review.googlesource.com/#/q/Id8c686b5f08d58e8e48d015ed42570e306687882))

- Added LayoutModifier2, a new API for defining layout modifiers; deprecated LayoutModifier ([If32ac](https://android-review.googlesource.com/#/q/If32acbfac08c677b80f9e4d5f624fe15c95ac60d))

- Replaced Modifier plus operator with factory extension functions ([I225e4](https://android-review.googlesource.com/#/q/I225e444f50956d84e15ca4f1378b7f805d54e0ca))

- Added translationX/Y properties to support
  offseting the display list of drawing commands for
  a given Layer. This is useful to move content
  in response to animations or touch events. ([I8641c](https://android-review.googlesource.com/#/q/I8641cc7d236296a4abf56be037746f5304488cf0))

- Added pivotX, pivotY parameters
  to Layer APIs to support rotation and scaling
  around a particular point on a layer ([Icf7c3](https://android-review.googlesource.com/#/q/Icf7c37ff805b4e86aed528f28d83c7d9634639fa))

- Add OnPositionedModifier and OnChildPositionedModifier
  to replace OnPositioned and OnChildPositioned composable
  functions. ([I2ec8f](https://android-review.googlesource.com/#/q/I2ec8fb4687b0b85e18174178562149745c03c7fd))

- Added LayerModifier, a modifier that allows
  adding a RenderNode for a Layout. It allows setting
  clipping, opacity, rotation, scaling, and shadows.
  This will replace RepaintBoundary. ([I7100d](https://android-review.googlesource.com/#/q/I7100dfe7a795567a48c2d5b3094e3dbd47e0f9c7), [b/150774014](https://issuetracker.google.com/issues/150774014))

- Made the layout direction be propagated from parent layout node to children. Added layout direction modifier. ([I3d955](https://android-review.googlesource.com/#/q/I3d9559ddec464850d22466793975b41757e0224e))

- Stack component supports right-to-left directionality ([Ic9e00](https://android-review.googlesource.com/#/q/Ic9e00dfc5b8c16ff305c14bc38de38cdf72d4cf5))

- Initial support for Rtl in Compose layout ([Ia5519](https://android-review.googlesource.com/#/q/Ia5519f42c6ded656242321a92c8c8069c2f42ab7))

- Density and DensityScope were merged into one interface. Instead of ambientDensity() you can now use DensityAmbient.current. Instead of withDensity(density) just with(density) ([I11cb1](https://android-review.googlesource.com/#/q/I11cb1f069a95f32f4ecab631f49d38dc1c071a42))

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

- Created CanvasScope API that wraps a
  Canvas object to expose a stateless, declarative
  drawing API surface. Transformations are contained
  within their own receiver scope and sizing information
  is also scoped to corresponding inset bounds.
  It does not require a consumer to maintain its own Paint state
  object for configuring drawing operations.

  - Added CanvasScopeSample as well as updated the demo app to include a declarative graphics demo ([Ifd86d](https://android-review.googlesource.com/#/q/Ifd86d39ef5807d34cc06d06854d24330e5e00164))
- Removed unused MaskFilter API
  as it has limited usage and is not optimized
  for hardware acceleration in most use cases ([I54f76](https://android-review.googlesource.com/#/q/I54f76d8af47b4e015d84a52d36a336f68f31d84b))

- RectangleShape moved from androidx.ui.foundation.shape.\* to androidx.ui.graphics.\* ([Ia74d5](https://android-review.googlesource.com/#/q/Ia74d5a3bbe2ee3a28bbddb57a2aef2607679d4ac), [b/154507984](https://issuetracker.google.com/issues/154507984))

- Replaced all nullable Color uses in API with
  non-nullable and use Color.Unset instead of null ([Iabaa7](https://android-review.googlesource.com/#/q/Iabaa7c6334857833cdb0d5958f062e2e576bd240))

- Introduce additional optional rect
  parameter to ImagePainter to support
  drawing a subsection of underlying ImageAsset ([I0ea9e](https://android-review.googlesource.com/#/q/I0ea9ec2f991b30b0e68fa702ebdf44cbb0848901))

- Added Unset Color to represent an unset value without
  boxing Colors. ([If901a](https://android-review.googlesource.com/#/q/If901abf1400233a97a63de2f01de3a7f75b9c55a))

- Added Canvas.rotate and
  Canvas.scale extension methods to
  consume optional pivot coordinates for
  transformations. These default
  to the top left corner of the
  current canvas translation.

  Also moved Canvas.rotateRad to be
  an extension method for consistency ([Ibaca6](https://android-review.googlesource.com/#/q/Ibaca68af0082251b89fe8bbe0b8e73f2a86e4918))
- Created PixelMap API to support
  querying pixel information from an ImageAsset. ([I69ad6](https://android-review.googlesource.com/#/q/I69ad6c9a12ceed74ef6e4cf10786da309baa5580))

- Renamed toFrameworkRect/toFrameworkRectF to
  toAndroidRect/toAndroidRectF to match naming convention
  for object conversions between compose and the Android
  framework APIs they are built on top of. Also updated
  docs on these APIs ([I86337](https://android-review.googlesource.com/#/q/I86337019ca9440bde7202943bb6493a5b22ce7ca))

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
- Renamed Image to ImageAsset to better differentiate the difference between the Image data and the upcoming Image composable used to participate in layout and draw content.
  _Body:Created extension method on android.graphics.Bitmap,
  Bitmap.asImageAsset(), to create an instance of an
  ImageAsset useful for combining traditional Android
  application development with the compose framework ([Id5bbd](https://android-review.googlesource.com/#/q/Id5bbdf3fe1cf68750a76bb955b20e06d1f81a71e))

- Added TextDirection.Content ([I48f36](https://android-review.googlesource.com/#/q/I48f3683066739b4d88b2e998f9b216a5cd874f8d))

- Added TextDecoration.plus operator ([I0ad1a](https://android-review.googlesource.com/#/q/I0ad1a94cb5f5b296831a6b7283c525ab6af8ee35))

- `Force` is removed from TextDirectionAlgorithm enum values ([Icc944](https://android-review.googlesource.com/#/q/Icc944e7ca5f706fa8fd23f32fca7c4dbc1a0821f))

- TextDirectionAlgorithm is renamed as TextDirection ([I75ce8](https://android-review.googlesource.com/#/q/I75ce894540855ae60201b05141ad40c400bda00a))

- Implements LongPressAndDrag for TextField Selection. ([I17919](https://android-review.googlesource.com/#/q/I17919b9c1514c8fa7d2b54062e4acc47e7685c8e))

- Added AnnotatedString.getStringAnnotations that returns all annotations within the range. ([I1fa00](https://android-review.googlesource.com/#/q/I1fa00deebf7db5182d3607a33d958999aefe476b))

- Changed the package name for Locale and LocaleList from
  androidx.ui.text to androidx.ui.intl ([I8132c](https://android-review.googlesource.com/#/q/I8132c50e8be9b7ac27e858573056abe9250426ca))

- TextField's cursor has a blinking animation ([Id10a7](https://android-review.googlesource.com/#/q/Id10a71f42f66fae532cca35ec132bcc35a4bc660))

- API change: AnnotatedString(builder: Builder) is renamed to annotatedString(builder: Builder). ([Ia6377](https://android-review.googlesource.com/#/q/Ia63777788348827d4362e0bd6a4ab6cd64680062))

- API change: AnnotatedString.Item is renamed to AnnotatedString.Range. ([I2d44d](https://android-review.googlesource.com/#/q/I2d44dd9e4f565d5f90eeba93dc61a052109da32e))

- Rename AnnotatedString.Builder.addAnnotationString to addStringAnnotation. ([I5059e](https://android-review.googlesource.com/#/q/I5059e6b6526a8fb64ab6ace7ad7e4637c718a19f))

- Now it is possible to hide/show software keyboard by using
  SoftwareKeyboardController which is delivered by onTextInputStarted
  callback ([I8dc44](https://android-review.googlesource.com/#/q/I8dc44f64d4f457339364b9624c0b3e946cdf01b3), [b/151860051](https://issuetracker.google.com/issues/151860051))

- Added plus operator for (Text/Paragraph/Span)Style which
  delegates to merge() function. ([Ia1add](https://android-review.googlesource.com/#/q/Ia1add7b4d6a2b05c2ca2e3a3a1e40d5056471065))

- FontWeight.lerp does not snap anymore. It is still a data class. ([I521c2](https://android-review.googlesource.com/#/q/I521c21831d2cd979be98d133668fa5229ba61b08))

- FontWeight constructor is now public, it is not data class anymore. ([Id6b1f](https://android-review.googlesource.com/#/q/Id6b1fb0dbda69497b113344ecb1f3b384d060bf9))

- Add getLineStart, getLineEnd, getEllipsisOffset and getEllipsisCount to TextLayoutResult ([Ibc801](https://android-review.googlesource.com/#/q/Ibc801167d7f849e94a7f7ebfbdadc7f00f6dde2d))

- ui-text module is renamed as ui-text-core ([I57dec](https://android-review.googlesource.com/#/q/I57dec72ca50e7288e37c9272ef6ce8bcc485a83e))

- Removed unused Size class
  as there is a duplicate Size class
  in the ui-geometry module that is
  being consumed. ([I1b602](https://android-review.googlesource.com/#/q/I1b602068d4c269ba9221eb2bf668026c495f4cee))

- Added AdapterList, a scrolling list component that only
  composes and lays out the visible items. Currently known issues
  include that it is vertical-only and does not fully handle all
  cases of changes to its children. ([Ib351b](https://android-review.googlesource.com/#/q/Ib351be89aabb59dac29806a935e377e90a2da9c2))

- Add paddings, border, shape and background param to Box ([I05027](https://android-review.googlesource.com/#/q/I05027a87956b6e4233a6b8992d321633e9fdcdc9), [b/148147281](https://issuetracker.google.com/issues/148147281))

**Bug Fixes**

- onFocusChange callback in text fields renamed to onFocusChanged ([Ida4a1](https://android-review.googlesource.com/#/q/Ida4a1a55e5a9119c3a740d28ad2e0d9126d40853))
- VerticalScroller and HoriziontalScroller have been deprecated. Use ScrollableColumn and ScrollableRow for build-in experience with Column/Row behaviour and parameters, or Modifier.verticalScroll and Modifier.horizontalScroll on your own element. Similarly, ScrollerPosition has been deprecated in favor of ScrollState' ([I400ce](https://android-review.googlesource.com/#/q/I400ce0e6c0e33aa865e0e49defef1eb92ac40a93), [b/157225838](https://issuetracker.google.com/issues/157225838), [b/149460415](https://issuetracker.google.com/issues/149460415), [b/154105299](https://issuetracker.google.com/issues/154105299))
- `runOnIdleCompose` renamed to `runOnIdle` ([I83607](https://android-review.googlesource.com/#/q/I836071f1c3c63d21417a531f336f8a93ca13f9ed))
- Several testing APIs were renamed to be more intuitive. All findXYZ APIs were renamed to onNodeXYZ. All doXYZ APIs were renamed to performXYZ. ([I7f164](https://android-review.googlesource.com/#/q/I7f164b42b04196f023c4a2153d66825487998de4))
- Compose UI can now be composed inside ViewGroups without requiring a new composition. See ViewInteropDemo for an example. ([I9ab0b](https://android-review.googlesource.com/#/q/I9ab0b3ff5febce27c34e81dd55e3dce6ea1aa742), [b/160455080](https://issuetracker.google.com/issues/160455080))
- Added sortWith and removeRange to MutableVector ([Icccf7](https://android-review.googlesource.com/#/q/Icccf73d3dd073dab0c7e67edf06afe77ec19bc67))
- Implement Drag Selection Handles to change selection for TextField. ([I27032](https://android-review.googlesource.com/#/q/I27032ee670131726d579612591dafcf3d60680b6))
- Removed Shader inline class that wrapped the NativeShader expect class Renamed NativeShader to Shader. The wrapped Shader inline class did not add anything valuable to the API surface and was an inline class, so use the NativeShader class directly. ([I25e4d](https://android-review.googlesource.com/#/q/I25e4db3d4f59899b6a7c59613e49ed093e76da2f))
- Refactored PainterModifier
  to no longer provide scaling based on
  the given constraints and ContentScale
  parameter. Implementations of Painter
  are to scale their drawing content
  themselves based on the given size of
  the DrawScope they are drawing into.

  Fixed issue where VectorPainter's cache
  bitmap was sized to its default size
  instead of the given size to draw into.

  Updated ImagePainter to scale its
  content instead of relying on PainterModifier
  to do so on its behalf. ([I6ba90](https://android-review.googlesource.com/#/q/I6ba901d9622d5070c64ee641044d9bfddd409222))
- add top-level withFrameNanos function for animation timing ([Ie34c5](https://android-review.googlesource.com/#/q/Ie34c53e2e105353acc5ad56df0e15e1bc2a2da08))

- @Untracked annotation has been deprecated. Replace with @ComposableContract(tracked=false) ([Id211e](https://android-review.googlesource.com/#/q/Id211e1c7c168c5171bbf3c844792890ee87d4fc2))

- androidx.ui.foundation.TextFieldValue and
  androidx.ui.input.EditorValue is deprecated. TextField,
  FilledTextField and CoreTextField composables that uses
  that type is also deprecated. Please use
  androidx.ui.input.TextFieldValue instead ([I4066d](https://android-review.googlesource.com/#/q/I4066d1f4d2e3e3514753aa3495680292dc55f89d), [b/155211005](https://issuetracker.google.com/issues/155211005))

- Fixed issue where pointer input
  dispatch would cause a crash if
  PointerInputFilters were removed via
  subcomposition during disptach. This is now fixed. ([I1f48b](https://android-review.googlesource.com/#/q/I1f48bdee2fcb59eb0984c31ef4ce95d75417dcf4), [b/157998762](https://issuetracker.google.com/issues/157998762))

- Fixed issue where pointer input dispatch would
  cause a crash if PointerInputFilters were removed via
  subcomposition during disptach. This is now fixed. ([Iab398](https://android-review.googlesource.com/#/q/Iab398032792a8dde761ce5440650c774b4d56022), [b/157998762](https://issuetracker.google.com/issues/157998762))

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
- The Recompose composable is no longer a useful abstraction. Most recomposition should happen as a result of MutableState assignments. For anything beyond that, it is recommended that you use the `invalidate` function to trigger a recomposition of the current scope. ([Ifc992](https://android-review.googlesource.com/#/q/Ifc9926013c51c1db1e27e702a707bc1050f82fa6))

- Replaced usage of Px class in various
  compose classes as part of the large
  refactoring effort to only rely on Dp
  and primitive types for pixel parameters ([Iede0b](https://android-review.googlesource.com/#/q/Iede0b310a8a8f4a39ba6ae4a99c753f7f590d8ed))

- Changes the code generation strategy of Compose's compiler. Prior to the change, the compose compiler would transform calls to composable functions. With this change, we now transform the body of a composable function and leave the callsite unaltered (mostly).

  This means that most of the logic communicating with the compose runtime happens at the start of the function body, instead of at the callsite.

  This should be a source-compatible change for all usage of compose. Most users of compose should not have to update any code as a result of this change.

  In order to support this work, the JVM signature of all composable functions has changed. A Composable function accepting a single parameter is transformed into a function accepting 3 parameters, the additional parameters are the Composer, a 'key' integer. a bitmask integer used to propagate metadata through calls.

  Compose now also transforms default arguments to a composable function. It does this without introducing an additional synthetic default overload of the function itself, so this change will result in fewer functions being defined.

  Known intentional behavioral changes resulting from this:
  1. Some calls will skip where they wouldn't have previously
  2. Composable expressions in default argument expressions are now correctly subscribed to and handled

  This work included some optimizations:
  1. The result of comparisons of parameters are propagated through the call graph to other composable functions. This will result in fewer comparisons at runtime, reduces the slot table size, as well as more skipping of composable functions that were previously not skipped
  2. Paremeters which are determined to be "static" at compile time are no longer compared or stored in the runtime. This reduces the number of comparisons and reduces slot table size.
  3. Control flow structure of the body of functions is used to minimize the number of groups that are generated. This reduces slot table size and results in less work for the runtime
  4. Unused dispatch and receiver parameters to functions are not included in determining skippability of the function if they are not used inside of the body of the function.

  Most breaking changes were for APIs that the compiler targets directly, and typical use of compose will not be affected:
  1. Composer::startExpr was removed
  2. Composer::endExpr was removed
  3. Composer::call was deprecated
  4. The non-varargs overloads of `key` have been removed. Use the `vararg` version going forward.
  5. The Pivotal annotation was deprecated. Use `key` as a replacement.
  6. ScopeUpdateScope::updateScope was changed to expect a Function3 instead of Function1
  7. restartableFunction and restartableFunctionN were updated to include additional compile time parameters
  ([I60756](https://android-review.googlesource.com/#/q/I607560574d83b4b6c1e68ff72cc4124c5f8c2602), [b/143464846](https://issuetracker.google.com/issues/143464846))
- Removed deprecated LayoutAlign modifiers. ([I10877](https://android-review.googlesource.com/#/q/I108771c0374a5c6f88a610549ddae220eab30a4f))

- Removed RepaintBoundary in favor of DrawLayerModifier ([I00aa4](https://android-review.googlesource.com/#/q/I00aa4667ebe6248500b677b07d08744d5f79ae7f))

- Button, FloatingActionButton and Clickable now have a separate `enabled` param. Some of the params on Button were renamed or reordered. ([I54b5a](https://android-review.googlesource.com/#/q/I54b5ac613632c1cd804b756d3ad2ccb7a475a149))

- Replaced ButtonStyle with distinct functions and removed text (string) overload. See updated samples for usage information. ([If63ab](https://android-review.googlesource.com/#/q/If63ab32bd3f12050a2d2f4b8c0cb044bc7144a6b), [b/146478620](https://issuetracker.google.com/issues/146478620), [b/146482131](https://issuetracker.google.com/issues/146482131))

- Breaking changes to the ambients API. See log and `Ambient<T>` documentation for details ([I4c7ee](https://android-review.googlesource.com/#/q/I4c7eea45f2b7bf41f8a8ba75fd667c06010469a9), [b/143769776](https://issuetracker.google.com/issues/143769776))

- Changed the behavior of default TextDirection to be determined
  by LayoutDirection. i.e. If LayoutDirection is RTL, default
  TextDirection will be RTL. Previously it was
  TextDirection.ContentOrLtr/Rtl ([I4e803](https://android-review.googlesource.com/#/q/I4e80360f28d5e95daa86f3e1f280f3ec8855abf4))

- Bug fix: When font weight and font style are nested on an AnnotatedString, text is not rendered correctly. ([I77a9d](https://android-review.googlesource.com/#/q/I77a9d8f3b69e9ee8246bdcb60ef82c42805bf879))

- Adds commonly used parameters to Text(). If you are currently creating a local text style to pass a small number of these parameters, such as Text(style = TextStyle(textAlign = TextAlign.Center)), you can now just provide the parameters directly: Text(textAlign = TextAlign.Center) ([I82768](https://android-review.googlesource.com/#/q/I8276873965f3588ed2cbc560f70a9ddd2405027b))

- ui-android-text module is renamed as ui-text-android ([I68cbe](https://android-review.googlesource.com/#/q/I68cbee56aab731acc66445f6578d41b7723a3c3f))