---
title: https://developer.android.com/jetpack/androidx/releases/constraintlayout
url: https://developer.android.com/jetpack/androidx/releases/constraintlayout
source: md.txt
---

# Constraintlayout

[User Guide](https://developer.android.com/training/constraint-layout) [Code Sample](https://github.com/android/performance-samples/tree/main/ConstraintLayoutPerformance)  
API Reference  
[androidx.constraintlayout.widget](https://developer.android.com/reference/kotlin/androidx/constraintlayout/widget/package-summary)  
Position and size widgets in a flexible way with relative positioning.  


This table lists all the artifacts in the `androidx.constraintlayout` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| constraintlayout | [2.2.1](https://developer.android.com/jetpack/androidx/releases/constraintlayout#constraintlayout-2.2.1) | - | - | - |
| constraintlayout-compose | [1.1.1](https://developer.android.com/jetpack/androidx/releases/constraintlayout#constraintlayout-compose-1.1.1) | - | - | - |
| constraintlayout-core | [1.1.1](https://developer.android.com/jetpack/androidx/releases/constraintlayout#constraintlayout-core-1.1.1) | - | - | - |

## Declaring dependencies

To add a dependency on ConstraintLayout, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.constraintlayout:constraintlayout:2.2.1"
    // To use constraintlayout in compose
    implementation "androidx.constraintlayout:constraintlayout-compose:1.1.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.constraintlayout:constraintlayout:2.2.1")
    // To use constraintlayout in compose
    implementation("androidx.constraintlayout:constraintlayout-compose:1.1.1")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:323867+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=323867&template=1023345)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## ConstraintLayout-compose, and ConstraintLayout-Core 1.1

### Version 1.1.1

February 26, 2025

`androidx.constraintlayout:constraintlayout-compose:1.1.1`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.1`, and `androidx.constraintlayout:constraintlayout-core:1.1.1` are released. Version 1.1.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5d79680b3493cf7c2808dbf1b7353c0822fa249c..a31205d256dd1a1629467c503b3fca269f765ebe/constraintlayout).

**Bug Fixes**

- Fixes some layout issues that in some cases results in Layouts not being placed. Such as toggling Visibility. ([I34e68](https://android-review.googlesource.com/#/q/I34e68fd99eb7299447edd605311f6cd55642771a), [b/299134793](https://issuetracker.google.com/issues/299134793))

### Version 1.1.0

October 30, 2024

`androidx.constraintlayout:constraintlayout-compose:1.1.0`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0`, and `androidx.constraintlayout:constraintlayout-core:1.1.0` are released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f575d1a1a11916e17e3ac857781b577fdafb840d..5d79680b3493cf7c2808dbf1b7353c0822fa249c/constraintlayout).

**Important changes since 1.0.0**

- Fixes interaction with SharedTransitionLayout ([b/332898040](https://issuetracker.google.com/issues/332898040)).
- Fixes Layout issues related to measurement due to recomposition ([b/219091179](https://issuetracker.google.com/issues/219091179), [Ibfe8a](https://android-review.googlesource.com/q/Ibfe8a2aeffba85aa6374d763729887aa1f308b35)).

### Version 1.1.0-rc01

October 16, 2024

`androidx.constraintlayout:constraintlayout-compose:1.1.0-rc01`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-rc01`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-rc01` are released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..f575d1a1a11916e17e3ac857781b577fdafb840d/constraintlayout).

### Version 1.1.0-beta01

September 4, 2024

`androidx.constraintlayout:constraintlayout-compose:1.1.0-beta01`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-beta01`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-beta01` are released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/constraintlayout).

### Version 1.1.0-alpha14

August 7, 2024

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha14`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-alpha14`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha14` are released. Version 1.1.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..9130b719318a69f2f3eaf82c32b131232fd721cb/constraintlayout).

**API Changes**

- Flags are now provided individually through the companion object and may be combined with the `or` operator. ([I9df53](https://android-review.googlesource.com/#/q/I9df5318aefd42496f9dd15ba1ec1b3376cf958ec))
- Simplified `createRow` \& `createColumn` helpers. Improved `createGrid` parameter names and documentation for clarification. ([Iebc92](https://android-review.googlesource.com/#/q/Iebc92f65e5986d57d5c592dd82fad34aef7b3ee4))
- Simplified `animateChanges` API in `ConstraintLayout` to only need a non-null `AnimationSpec`. `onIncomingConstraints` in `InvalidationStrategy` is now a regular lambda. `fixedWidthRate` renamed to `shouldInvalidateOnFixedWith`, same for the Height variant. ([Ie59cd](https://android-review.googlesource.com/#/q/Ie59cd551b999788c0f11ce77feb62d00dc8b9de6), [b/332898040](https://issuetracker.google.com/issues/332898040), [b/336370035](https://issuetracker.google.com/issues/336370035))
- `NestedScroll` sources Drag and Fling are being replaced by `UserInput` and `SideEffect` to accommodate for the extended definition of these sources that now include animations (Side Effect) and Mouse Wheel and Keyboard (UserInput). ([I40579](https://android-review.googlesource.com/#/q/I40579c9b053d6bcf477191b212c7a72876a588b7))

### Version 1.1.0-alpha13

October 4, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha13`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-alpha13`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha13` are released with no changes. [Version 1.1.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..1f7407d4293384a1b91bc142880e3525048b3443/constraintlayout)

- This release allows `androidx.constraintlayout` libraries to be ABI compatible with the latest Compose releases.

### Version 1.1.0-alpha12

August 9, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha12`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-alpha12`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha12` are released. [Version 1.1.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/constraintlayout)

**API Changes**

- Added `LayoutScopeMarker` to Transition DSL. ([If54ce](https://android-review.googlesource.com/#/q/If54ce92c05c63a1b30f5713592f71e4477969b75))

### Version 1.1.0-alpha11

July 26, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha11`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-alpha11`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha11` are released. [Version 1.1.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..4aed940027a19667e67d155563fc5fa8b7279313/constraintlayout)

**New Features**

- You may now provide an `InvalidationStrategy` to optimize invalidations in `MotionLayout`. Which will typically be the source of reduced performance. ([Iada0c](https://android-review.googlesource.com/#/q/Iada0c39db7669619642115863066c14f9bb19cdf))
- You may now use `animateChanges = true` when using `ConstraintLayout` with the inline Modifier DSL (`Modifier.constrainAs`), whenever a change on the constraints DSL is done `ConstraintLayout` will automatically animate to that new state. ([I9abf1](https://android-review.googlesource.com/#/q/I9abf1451ef5123ba2a69b794f85ca07aedcbfb10))
- Enabled functionality for `limitBoundsTo` on OnSwipe. ([I56522](https://android-review.googlesource.com/#/q/I565225391ff2936c1592e6921880f13d745e8757))

**API Changes**

- Renamed `TransitionScope.staggered` to `TransitionScope.maxStaggerDelay`. ([I0fd2d](https://android-review.googlesource.com/#/q/I0fd2d33dd1a3024163843edb5f434d42d4ef13ae))

**Bug Fixes**

- Fixed `dragScale` parameter from `OnSwipe` not working. ([8bef26](https://android-review.googlesource.com/#/q/8bef26aebdc226984f9dd73af407a6505682f374))
- Fixed `customColor` in `MotionScene` not working properly with transparent colors. ([81b2ac](https://android-review.googlesource.com/#/q/81b2acf2cd2fd3395cfd7f1c621fb5545d4ab303))
- Fixed `OnSwipe` not announcing properly when it has stopped, also fixed initial velocity calculation for `touchUp`. ([Ia5f6f](https://android-review.googlesource.com/#/q/Ia5f6f0145ef1ef50119628b39382a2754496e2a8))
- Updated KDoc for `ConstraintLayout` Composable and `Constraintset`. ([3bfe63](https://android-review.googlesource.com/#/q/3bfe631945311b92e3909ce65375fabfe7f28a83))

### Version 1.1.0-alpha10

May 24, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha10`, `androidx.constraintlayout:constraintlayout-compose-android:1.1.0-alpha10`, and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha10` are released. [Version 1.1.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/constraintlayout)

**API Changes**

- `MotionLayout` Api is no longer experimental, this represents the initial set of stable Api for `MotionLayout`. ([I288f4](https://android-review.googlesource.com/#/q/I288f4812061c924daabfddbcd6163e8ed8096ef7))
- Removed `MotionLayoutState`. ([Id3ac1](https://android-review.googlesource.com/#/q/Id3ac17048b18a6ab6e1a391524bf3c56943e80e5))
- You may now use `DebugFlags` for visual debugging: `DebugFlags(showBounds = true)`. ([Ic714b](https://android-review.googlesource.com/#/q/Ic714b851d92355b8fb95d930d38294e6668adbc0))
- Changed extension variable `Dp.asDimension` to a method: `Dp.asDimension()`. ([I2d6ef](https://android-review.googlesource.com/#/q/I2d6eff07ee626eaa6b5b3f64af5a6fdf5808708c))
- Staggered now supported in the `MotionLayout` DSL, define the maximum delay with `TransitionScope.staggered`, you may also use `ConstrainScope.staggeredWeight` (within a `MotionSceneScope`) to get a custom staggered order. ([I70275](https://android-review.googlesource.com/#/q/I70275855b29cbb7bdcfe85f27d6c4f4f8178bbd1))
- Two changes made for the Grid helper: 1. `paddingLeft` and `paddingRight` to `paddingStart` and `paddingEnd`, respectively, and 2. update the format of `gridSpans` and `gridSkip` to an array of the Span and Skip objects to make it more structural. ([Idd1eb](https://android-review.googlesource.com/#/q/Idd1ebe78c874c6d40e6e39e4d93819061c80fe6b))

### Version 1.1.0-alpha09

March 22, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha09` and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha09` are released. [Version 1.1.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c37bd7a58b465e53962265e5a5991400817fc2e5..5e7d256f82fbafb6d059ab7b18fddd87c7531553/constraintlayout)

**API Changes**

- `Modifier.intermediateLayout` now doesn't require an explicit `LookaheadScope`. The measure block in `intermediateLayout` has `IntermediateMeasureScope` as receiver, which provides convenient `CoroutineScope`, `LookaheadScope` and `MeasureScope`.
- `LookaheadLayout` has been replaced by `LookaheadScope`, which is no longer a Layout. This allows child content in a `LookaheadScope` to be directly controlled by parent's `MeasurePolicy`. ([Ibe2e5](https://android-review.googlesource.com/#/q/Ibe2e5e20a833d3824213e86e5c1e155f65647ad7))
- `Easing.Cubic()` can now take overshoot parameters. ([I2d826](https://android-review.googlesource.com/#/q/I2d826dc9fb5dd65ee340ceaba87825c843b01df5))

### Version 1.1.0-alpha08

March 8, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha08` and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha08` are released. [Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..c37bd7a58b465e53962265e5a5991400817fc2e5/constraintlayout)

**New Features**

- Lint checks added to suggest the use of `Dimension.percent(1f)` and `LayoutReference.withChainParams()` in cases where the typical patterns may lead to unpredictable behavior. ([I62eb0](https://android-review.googlesource.com/#/q/I62eb07e51c36d762aaeff3bfa0031fcfbf6e3923), [I03060](https://android-review.googlesource.com/#/q/I030608fef51ad993841c3a5e78ac6b551dac7609))

**API Changes**

- Enable `ReverseSpanDirection` and `SpansOrderFirst` flags for Grid Helper in Compose.
  1. `ReverseSpanDirection`: reverse the width and height specification for spans/skips.
  2. `SpansOrderFirst`: spans would respect the order of the widgets. ([I6ad50](https://android-review.googlesource.com/#/q/I6ad503428cd269eb503de96d010c77b3521b33a1))
- Use `Modifier.onStartEndBoundsChanged(...)` to obtain local bounds of Composables in a `MotionLayout` that are not affected by animation. Useful for any ui interaction that requires layout information that may also trigger animations such as `DragAndDrop`. ([I6b5f9](https://android-review.googlesource.com/#/q/I6b5f9882acf81386dc62340b5f1ffb46ca91c750))
- Enable skips and spans of the Grid Helper in Compose ([I917b6](https://android-review.googlesource.com/#/q/I917b66a7127e0db39aaabf2c9b9036969b2ad1f0))

**Bug Fixes**

- Fixed translation properties not applying expected values. ([I961cd](https://android-review.googlesource.com/#/q/I961cdf6bc804ec56b455111119ed623e4229cd6d))

### Version 1.1.0-alpha07

February 8, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha07` and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha07` are released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/constraintlayout)

**New Features**

- Add new APIs to enable the Grid Helper in Compose using DSL ([I1143b](https://android-review.googlesource.com/#/q/I1143bba4118a6de829d4f7e55feee2b92a10a731))

**Bug Fixes**

- Fixed `Wrap.Chain` for Flow not laying out properly to the given `maxElement` parameter. ([e1f2ed3](https://android.googlesource.com/platform/frameworks/support/+/e1f2ed3aaebf841ca962e670a24c6c21a9d8a968))
- Fixed `start` `ConstraintSet` not updating when changing Transition through `MotionLayout(motionScene: MotionScene, progress: Float, transitionName: String)`. ([17ffff1](https://android.googlesource.com/platform/frameworks/support/+/17ffff1420fbf1288cbcdece5dc11f8e83d9dc1a))
- Fixed `ConstraintSet` not reflecting some changes when inheriting constraints through `ConstraintSet(extendConstraintSet: ConstraintSet, description: ConstraintSetScope.() -> Unit)`.([740804b](https://android.googlesource.com/platform/frameworks/support/+/740804be5ae00c5ca63321f00a67d04f2afd29ba))

### Version 1.1.0-alpha06

January 25, 2023

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha06` and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/constraintlayout)

**New Features**

- Add new Apis to enable the Grid Helper in Compose with JSON representation which allows composables to be placed in a 2D grid. ([I968ad](https://android-review.googlesource.com/#/q/I968ad630bd51473eef8658e4b0bf5209831a4c6b))

**API Changes**

- Add support for arc up and arc down modes `Arc.Above` and `Arc.Below` direction independent arc modes to `MotionLayout` ([I184a9](https://android-review.googlesource.com/#/q/I184a9003c18f576009ac9bc8daf9ccdb8ba47f02))
- It is now possible to constrain a baseline anchor to top/bottom anchors and vice versa. ([I54628](https://android-review.googlesource.com/#/q/I546283cc910dfad223c2e8c7330e0e8c5f2c5073))
- Renamed `MotionLayoutScope#motionProperties` (including derivatives) to `MotionLayoutScope#customProperties`. This is to be consistent as when setting custom properties. ([Ib34c9](https://android-review.googlesource.com/#/q/Ib34c9e063267a9c0dfd89ff5e8caaa53da9f745f))
- It's now possible to create multiple references in `ConstraintSet` and `MotionScene`: `val (box, text, button) = createRefsFor("box", "text","button")`. Apply constraints to multiple elements with `constrain(box, button, text)`. Within a `ConstrainScope`, you may now intuitively set a fixed dimension with `Dp.asDimension`: `width = 10.dp.asDimension`. ([I021ec](https://android-review.googlesource.com/#/q/I021ecb4cc93ba7e638225326e07b234c12de2611), [Ia0960](https://android-review.googlesource.com/#/q/Ia0960697ea260a26cba3323b43bdeeea549ba6cd))
- `MotionScene()` and `Transition()` methods are now non-Composable functions. The objects from these functions (including `ConstraintSet`) should now be properly comparable from each other. `animateChanges = true` in `ConstraintLayout` can now be used with only one `ConstraintSet` reference, as long as any of its properties changed on recomposition. ([I7d22e](https://android-review.googlesource.com/#/q/I7d22e599204c749b80244f8169ccbc5888741cd6))

**Bug Fixes**

- Fixed issue where `ConstraintLayout` always triggered an unnecessary extra recomposition when helpers were changed. ([Id83ad](https://android-review.googlesource.com/#/q/Id83ada3e963b20180c324f25b6db7c53f810463f), [b/222093277](https://issuetracker.google.com/issues/222093277))
- Fix behavior when using Intrinsics with `ConstraintLayout` \& `MotionLayout`. ([I487ae](https://android-review.googlesource.com/q/I487ae6fcc36342cee7fe38428971c27500be0b23), [b/220527863](https://issuetracker.google.com/issues/220527863))
- Fix not being able to remeasure when the content changes. ([Ibfe8a](https://android-review.googlesource.com/q/Ibfe8a2aeffba85aa6374d763729887aa1f308b35), [b/219091179](https://issuetracker.google.com/issues/219091179))

### Version 1.1.0-alpha05

December 7, 2022

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha05` and `androidx.constraintlayout:constraintlayout-core:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c6ed48ba603ed10b85c7debb34239c480a87bab..4a2f5e696614339c1ac21f706c1a17c0285780e7/constraintlayout)

**New Features**

- Support custom `KeyAttributes` in DSL ([b94e748](https://android-review.googlesource.com/#/q/b94e748cbb0c309713a6608f6c6aa7d4696caea4))
- Surface bias properties in `ConstrainScope` ([32625d0](https://android-review.googlesource.com/#/q/32625d06d6e2e72f385471a90ba830a7a73ea659))
- Support custom parameters in chains ([72a2e9e](https://android-review.googlesource.com/#/q/72a2e9e9c1c07fe94cf66ab105b6fe7656a0220e))
- Add Macrobenchmark tests for `MotionLayout` in Compose ([36f43bc](https://android-review.googlesource.com/#/q/36f43bc0a2a83dbbc165d3131ac9072e6b5a9591))
- For more information on changes in previous release in Compose, see [wiki page](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.1-(Compose))

**API Changes**

- Flip `addConstraintSet` and `addTransition` parameters ([152facc](https://android-review.googlesource.com/#/q/152facc7a897fd0ff51140850cba1a20df655882))

**Bug Fixes**

- Fix Horizontal Chains ([ed5f56e](https://android-review.googlesource.com/#/q/ed5f56ef5669d1206a12a9e2878e103f01e4de49))

### Version 1.1.0-alpha01

May 20, 2022

`androidx.constraintlayout:constraintlayout-compose:1.1.0-alpha01` is released.

Please note MotionLayout API is experimental and requires opt in.

For more information, see what's [New in Compose 1.1.0-alpha01](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.1-(Compose)#new-in-compose-110-alpha01) on GitHub.

## Version 2.2

### Version 2.2.1

February 26, 2025

`androidx.constraintlayout:constraintlayout:2.2.1` is released. Version 2.2.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5d79680b3493cf7c2808dbf1b7353c0822fa249c..a31205d256dd1a1629467c503b3fca269f765ebe/constraintlayout/constraintlayout).

**External Contribution**

- Fixes an issue with binary compatibility from the `constraintlayout-core` library. Thanks Carlo Marinangeli! ([I8952e](https://android-review.googlesource.com/#/q/I8952e19a697eb39ddafdce2e0925ceafe3d0e7c2), [b/376718273](https://issuetracker.google.com/issues/376718273))

### Version 2.2.0

October 30, 2024

`androidx.constraintlayout:constraintlayout:2.2.0` is released. Version 2.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f575d1a1a11916e17e3ac857781b577fdafb840d..5d79680b3493cf7c2808dbf1b7353c0822fa249c/constraintlayout/constraintlayout).

**Important changes since 2.1.0**

- Parity release with underlying constraintlayout-core library.

### Version 2.2.0-rc01

October 16, 2024

`androidx.constraintlayout:constraintlayout:2.2.0-rc01` is released. Version 2.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..f575d1a1a11916e17e3ac857781b577fdafb840d/constraintlayout/constraintlayout).

### Version 2.2.0-beta01

September 4, 2024

`androidx.constraintlayout:constraintlayout:2.2.0-beta01` is released. Version 2.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/constraintlayout/constraintlayout).

### Version 2.2.0-alpha14

August 7, 2024

`androidx.constraintlayout:constraintlayout:2.2.0-alpha14` is released. Version 2.2.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..9130b719318a69f2f3eaf82c32b131232fd721cb/constraintlayout/constraintlayout).

### Version 2.2.0-alpha13

October 4, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha13` is released with no changes. [Version 2.2.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..1f7407d4293384a1b91bc142880e3525048b3443/constraintlayout/constraintlayout)

### Version 2.2.0-alpha12

August 9, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha12` is released. [Version 2.2.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/constraintlayout/constraintlayout)

### Version 2.2.0-alpha11

July 26, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha11` is released. [Version 2.2.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..4aed940027a19667e67d155563fc5fa8b7279313/constraintlayout/constraintlayout)

**API Changes**

- Add a setter method to allow developers to programmatically set the value for `mInfiniteCarousel` ([I0a8ca](https://android-review.googlesource.com/#/q/I0a8ca5f437fe07de2e0c2f04eb306f3af4fb90fd))

### Version 2.2.0-alpha10

May 24, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha10` is released. [Version 2.2.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/constraintlayout/constraintlayout)

**Bug Fixes**

- Fix a broken link of the `MotionLayout` doc. ([51cbe88](https://android-review.googlesource.com/#/q/I69cb39e73e4046c72574de581d219ed9c3fe7a03))

### Version 2.2.0-alpha09

March 22, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha09` is released. [Version 2.2.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c37bd7a58b465e53962265e5a5991400817fc2e5..5e7d256f82fbafb6d059ab7b18fddd87c7531553/constraintlayout/constraintlayout)

### Version 2.2.0-alpha08

March 8, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha08` is released. [Version 2.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..c37bd7a58b465e53962265e5a5991400817fc2e5/constraintlayout/constraintlayout)

### Version 2.2.0-alpha07

February 8, 2023

`androidx.constraintlayout:constraintlayout:2.2.0-alpha07` is released. [Version 2.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/constraintlayout/constraintlayout)

**Bug Fixes**

- Fix the `ConstraintLayout` page content missing issue. ([I82e25](https://android-review.googlesource.com/#/q/I82e2501b0a2ecd3f24c880cf73781e3d03329ac2))

### Version 2.2.0-alpha05

December 7, 2022

`androidx.constraintlayout:constraintlayout:2.2.0-alpha05` is released. [Version 2.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c6ed48ba603ed10b85c7debb34239c480a87bab..4a2f5e696614339c1ac21f706c1a17c0285780e7/constraintlayout/constraintlayout)

- For more information on changes in previous release, see [Github wiki page](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.2)

**Bug Fixes**

- Fix leak in View Carousel ([eb67b82](https://android-review.googlesource.com/#/q/eb67b82abc233c0c900c8f0788a8669081fd0836))

### Version 2.2.0-alpha01

May 20, 2022

`androidx.constraintlayout:constraintlayout:2.2.0-alpha01` is released.

Includes a preview of the new `Grid` helper.

For more information, see what's [New in 2.2.0-alpha01](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.2#new-in-220-alpha01) on GitHub.

## ConstraintLayout-compose 1.0

ConstraintLayout-compose 1.0 provides ConstraintLayout functionalities in Jetpack Compose.

### Version 1.0.1

May 20, 2022

`androidx.constraintlayout:constraintlayout-compose:1.0.1` is released.

Please note MotionLayout API is experimental and requires opt in.

For more information, see what's [New in Compose 1.0.1](https://github.com/androidx/constraintlayout/wiki/What%27s-New-in-1.0-%28Compose%29#new-in-compose-101) on GitHub.

### Version 1.0.0

January 13, 2022

`androidx.constraintlayout:constraintlayout-compose:1.0.0` is released.

Please note MotionLayout api is now experimental and requires opt in.

For more information, see the GitHub article [What's New in 1.0 (Compose)](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.0-(Compose)).

### Version 1.0.0-rc02

November 16, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-rc02` is released.

For more information, see the GitHub article [What's New in 1.0 (Compose)](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.0-(Compose)).

### Version 1.0.0-rc01

September 27, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-rc01` is released.

This release is the second beta. It is considered as feature complete, providing
[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout) and [`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout) for Compose.

For more information, see the GitHub article [What's New in 1.0 (Compose)](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.0-(Compose)).

### Version 1.0.0-beta02

July 30, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-beta02` is released.

This release is the second beta. It is considered as feature complete, providing
[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout) and [`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout) for Compose.

For more information, see the GitHub article [What's New in 1.0 (Compose)](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.0-(Compose)).

### Version 1.0.0-beta01

July 22, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-beta01` is released.

This release is the first beta. It is considered as feature complete, providing
[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout) and [`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout) for Compose.

For more information, see the GitHub article [What's New in 1.0 (Compose)](https://github.com/androidx/constraintlayout/wiki/What's-New-in-1.0-(Compose)).

### Version 1.0.0-alpha07

May 18, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha07` is released.

- Updated to be compatible with Compose version `1.0.0-beta07`.

### Version 1.0.0-alpha06

May 4, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha06` is released.

- Compose optimisation: Constraintlayout inline composable (#193)
- Minimize remeasurements in Compose (#210)

### Version 1.0.0-alpha05

March 15, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha05` is released.

- includes a fix for the optimization engine ([b/182657720](https://issuetracker.google.com/issues/182657720))
- add a optimizationLevel parameter to the ConstraintLayout copmosable

### Version 1.0.0-alpha04

March 11, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha04` is released.

Update to use the latest constraintlayout-core engine

### Version 1.0.0-alpha03

February 24, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha03` is released.

Release update for Jetpack Compose beta01 release

### Version 1.0.0-alpha02

February 10, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha02` is released.

Release update for Jetpack Compose alpha12 release

### Version 1.0.0-alpha01

February 2, 2021

`androidx.constraintlayout:constraintlayout-compose:1.0.0-alpha01` is released.

First release of the library, providing inline and external DSLs to express constraints.

## Version 2.1

ConstraintLayout 2.1.0 provides richer features in MotionLayout and new helpers
(Carousel, etc.)

### Version 2.1.4

May 20, 2022

`androidx.constraintlayout:constraintlayout:2.1.4` is released.

For more information, see what's [New in 2.1.4](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1#new-in-214) on GitHub.

### Version 2.1.3

January 13, 2022

`androidx.constraintlayout:constraintlayout:2.1.3` is released.

For more information, see the GitHub article
[What's New in 2.1](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.2

November 16, 2021

`androidx.constraintlayout:constraintlayout:2.1.2` is released.

For more information, see the GitHub article
[What's New in 2.1](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.1

September 27, 2021

`androidx.constraintlayout:constraintlayout:2.1.1` is released.

This is the final release for 2.1.1.

For more information, see the GitHub article
[What's New in 2.1](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.0

July 30, 2021

`androidx.constraintlayout:constraintlayout:2.1.0` is released.

This is the final release for 2.1.0.

For more information, see the GitHub article
[What's New in 2.1](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.0-rc01

July 22, 2021

`androidx.constraintlayout:constraintlayout:2.1.0-rc01` is released.

This is the release candidate for 2.1.0, providing minor improvements and fixes from the last beta.
For more information, see the GitHub article
[What's New in 2.1](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.0-beta02

May 4, 2021

`androidx.constraintlayout:constraintlayout:2.1.0-beta02` is released.

A few new features in MotionLayout:

- OnSwipe enhancement including spring (stiffness, damping, mass etc) \& never complete
- jumpToState function
- ViewTransition downUp mode where on touch Down it plays to 100 and on up reverses to 0

Various fixes, notably:

- Fix problem in MotionLayout with vertical scroll (#173)
- Perf improvements on nested MotionLayout (#189)
- Fast transition with NestedScrollView in MotionLayout (#189)
- ConstraintSet gone in MotionLayout (#189)
- Support downUp ViewTransitions in MotionLayout (#190)
- Fix in ImageFilter when reusing drawables (#192)
- Add spring support in MotionLayout (#199)
- Performance improvement to CircularFlow (#200)
- Fixes in derived constraints / constraint override (#212)

### Version 2.1.0-beta01

March 11, 2021

`androidx.constraintlayout:constraintlayout:2.1.0-beta01` is released.

**ConstraintLayout**

android:layout_width and android:layout_height are back being non-optional due to compatibility issues.

**MotionLayout**

- Programmatic support for inserting and removing onSwipe and onClick on Transitions
- Experimental Support for Transitions through screen rotation
- support duration argument to transitions
- Better support for customAttributes that are boolean or References

**Helpers**

- added a way to animate or jump directly to a given item of a Carousel
- new CircularFlow helper

See additional information on this release
[here](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1)
and [bugs closed](https://androidstudio.googleblog.com/2021/03/constraintlayout-210-beta-1.html).

### Version 2.1.0-alpha2

December 17, 2020

`androidx.constraintlayout:constraintlayout:2.1.0-alpha2` is released.

This second alpha adds several new features:

**ConstraintLayout**

- android:layout_width and android:layout_height are now optional, with wrap_content as default behavior
- new layout_constraintWidth and layout_constraintHeight attributes for expressing dimension constraints
- supports negative margins for constraints
- supports baseline to top and baseline to bottom constraints
- supports baseline margin constraints
- SharedValues allow to inject external values into ConstraintLayout

**MotionLayout**

- Support for overshoot interpolators (anticipate, overshoot)
- Enhanced MotionHelper support
- Add animated update of ConstraintSet to MotionLayout updateStateAnimate(id,cset,duration);
- Shared value based ViewTransition
- scheduleTransitonTo allow you to que a transition to run at the completion of the current transition.

**Helpers**

- Carousel now supports an infinite (wrap-around) mode
- ReactiveGuide : A guideline that position itself automatically when a SharedValue changes
- MotionEffect : inject Keyframes to referenced views moving in a given direction
- MotionLabel - A View for animating single line text

See additional information on this release
[here](https://github.com/androidx/constraintlayout/wiki/What's-New-in-2.1).

### Version 2.1.0-alpha1

November 19, 2020

`androidx.constraintlayout:constraintlayout:2.1.0-alpha1` is released.

First alpha of the 2.1 release. Introduces support for:

- Carousel motion helper, to build custom carousel views
- MotionLayout scenes supports include and constraints override
- MotionLayout adds richer support for rotation (input and output)
- MotionLayout adds ViewTransitions, allowing single view transitions for mutation of constraintsets

See additional information on this release [here](https://androidstudio.googleblog.com/2020/11/constraintlayout-210-alpha-1.html).

## Version 2.0

ConstraintLayout 2.0 adds new features for layouts (virtual layouts, etc.) and
a new class for simplifying animation of views, MotionLayout.

### Version 2.0.4

October 29, 2020

`androidx.constraintlayout:constraintlayout:2.0.4` is released.

**Bug Fixes**

This releases fixes a potential NPE that may happen when removing a child view
at runtime. It is recommended to update to this version.

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/10/constraintlayout-204.html).

### Version 2.0.3

October 27, 2020

`androidx.constraintlayout:constraintlayout:2.0.3` is released.

**Bug Fixes**

This releases fixes a few issues. It is recommended to update to this version.

- Windows insets handling
- Handling of dimension ratio in some situations
- Crash with some RTL layouts

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/10/constraintlayout-203.html).

### Version 2.0.2

October 6, 2020

`androidx.constraintlayout:constraintlayout:2.0.2` is released.

**Bug Fixes**

This releases improves performances as well as fix a few issues. It is recommended to update to this version.

- Handling of view GONE visibility in ConstraintLayout was incorrect in some situations
- Handling of packed chains in ConstraintLayout was incorrect in some situations
- Fixed inflation exception on API 15 for the Flow virtual layout helper
- limitsBoundsTo was broken in MotionLayout
- jump to end was broken in MotionLayout in some situations (chaining transitions)

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/10/constraintlayout-202.html).

### Version 2.0.1

August 25, 2020

`androidx.constraintlayout:constraintlayout:2.0.1` is released.

This is a minor update enabling the use of the MotionEditor in Android Studio.

### Version 2.0.0

August 21, 2020

`androidx.constraintlayout:constraintlayout:2.0.0` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/08/constraintlayout-200.html).

Notable fixes are:

- MotionLayout Transition delays \& TransitionListener fixes
- ConstraintLayout flow \& barrier fixes

### Version 2.0.0-rc1

July 29, 2020

`androidx.constraintlayout:constraintlayout:2.0.0-rc1` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/07/constraintlayout-200-rc1.html).

Notable fixes are:

- Flow fixes
- RecyclerView fixes (we recommend to update to recyclerview 1.2.0 alpha 5 or later)
- MotionLayout TransitionListener fixes
- MotionLayout memory leak fix

### Version 2.0.0-beta8

July 7, 2020

`androidx.constraintlayout:constraintlayout:2.0.0-beta8` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/07/constraintlayout-200-beta-8.html).

Notable fixes are:

- Placeholder behavior
- Layer visibility
- Flow, Barrier fixes
- TransitionListener fixes

### Version 2.0.0-beta7

June 12, 2020

`androidx.constraintlayout:constraintlayout:2.0.0-beta7` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/06/constraintlayout-200-beta-7.html).

Notable fixes are:

- Nested scroll view issues in MotionLayout
- Transition listener issues with MotionLayout
- Memory leak in MotionLayout
- RecyclerView issues
- Group visibility
- Padding issues

### Version 2.0.0-beta6

May 13, 2020

`androidx.constraintlayout:constraintlayout:2.0.0-beta6` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/05/constraintlayout-200-beta-6.html). Notable fixes are group visibility handling and derived constraints issues in MotionLayout.

### Version 2.0.0-beta5

May 7, 2020

`androidx.constraintlayout:constraintlayout:2.0.0-beta5` is released.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2020/05/constraintlayout-200-beta-5.html)

### Version 2.0.0-beta4

December 16, 2019

`androidx.constraintlayout:constraintlayout:2.0.0-beta4` is released.

**New Features**

MotionLayout

New attributes in Transition:

- layoutDuringTransition : let you configure how MotionLayout should react to children's requestLayouts calls during a transition. Possible values are {ignoreRequest, honorRequest}
- pathMotionArc : the path taken by elements moving will use an arc. Possible values are {startVertical \| startHorizontal \| flip \| none }

A default transition is now possible to define, simply by omitting the start and end ConstraintSets. That default transition will be used if no other existing transition can be found to match the current start/end states.

**Bug Fixes**

See the list of closed issues [here](https://androidstudio.googleblog.com/2019/12/constraintlayout-200-beta-4.html)