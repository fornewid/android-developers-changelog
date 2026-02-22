---
title: https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive
url: https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive
source: md.txt
---

<br />

# Compose Material 3 Adaptive

API Reference  
[androidx.compose.material3.adaptive](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary)  
Use the Material 3 adaptive library to create adaptive UIs that will adapt themselves automatically according to the current window configurations like window size classes or device postures. The library provides both default scaffold implementations and necessary building block composables to create your own custom experiences.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.2.0) | - | - | [1.3.0-alpha08](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.3.0-alpha08) |

## Declaring dependencies

To add a dependency on compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.material3.adaptive:adaptive:1.3.0-alpha08"
    implementation "androidx.compose.material3.adaptive:adaptive-layout:1.3.0-alpha08"
    implementation "androidx.compose.material3.adaptive:adaptive-navigation:1.3.0-alpha08"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.material3.adaptive:adaptive:1.3.0-alpha08")
    implementation("androidx.compose.material3.adaptive:adaptive-layout:1.3.0-alpha08")
    implementation("androidx.compose.material3.adaptive:adaptive-navigation:1.3.0-alpha08")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1467081+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1467081&template=0)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

<br />

## Compose Material3 Adaptive Navigation3 Version 1.0

### Version 1.0.0-alpha03

September 24, 2025

`androidx.compose.material3.adaptive:adaptive-navigation3:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf0316e0a0fa7e872bbfc1f6ecf667c8622db2c7..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/compose/material3/adaptive/adaptive-navigation3).

**API Changes**

- Add KMP stubs so JetBrains can fork and fill these targets to enable CMP. ([I75714](https://android-review.googlesource.com/#/q/I757148e2b77c5ebfe8230daceaa1d16da29fb6c2))
- Move `adaptive-navigation3` to `commonMain` to enable multiplatform use. ([I58aa9](https://android-review.googlesource.com/#/q/I58aa9e9359477ec5963a88e98a754c0e76db806b))

### Version 1.0.0-alpha02

September 10, 2025

`androidx.compose.material3.adaptive:adaptive-navigation3:1.0.0-alpha02` and `androidx.compose.material3.adaptive:adaptive-navigation3-android:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/21ec49263b1dfef28abcfedd25d83950ca381c13..cf0316e0a0fa7e872bbfc1f6ecf667c8622db2c7/compose/material3/adaptive/adaptive-navigation3).

### Version 1.0.0-alpha01

August 27, 2025

`androidx.compose.material3.adaptive:adaptive-navigation3:1.0.0-alpha01` and `androidx.compose.material3.adaptive:adaptive-navigation3-android:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/21ec49263b1dfef28abcfedd25d83950ca381c13/compose/material3/adaptive/adaptive-navigation3).

**New Features**

We are excited to announce the first alpha release of the `adaptive-navigation3` library. This new library, part of the Material Adaptive and Navigation3 ecosystem, is designed to help you build adaptive Material UIs integrated with the Navigation3 library.

Use scene strategies to implement a canonical list-detail pane scaffold (`ListDetailSceneStrategy`, `rememberListDetailSceneStrategy`) or a supporting pane scaffold (`SupportingPaneSceneStrategy`, `rememberSupportingPaneSceneStrategy`). For more information about scenes, scene strategies, and other new concepts introduced in Navigation 3, refer to the [Navigation3 guide](https://developer.android.com/guide/navigation/navigation-3).

## Compose Material3 Adaptive Version 1.3

### Version 1.3.0-alpha08

February 11, 2026

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha08` is released. Version 1.3.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/compose/material3/adaptive).

**API Changes**

- Material scene strategies support custom pane animations. ([I65e80](https://android-review.googlesource.com/#/q/I65e80b10c01f67b90daedd54a7231fdd78eba9d0))
- Material scene strategies support metadata for setting the preferred width and height of a pane when displayed in an adaptive scaffold. ([If0c2a](https://android-review.googlesource.com/#/q/If0c2a93db24bb63a41791725d71da488d4e2ede0))
- Material scene strategies have new parameters to support pane expansion. ([Iea29b](https://android-review.googlesource.com/#/q/Iea29bdd4ea4b14c0518eb79bc18e678a8a24671a), [b/437981137](https://issuetracker.google.com/issues/437981137))

### Version 1.3.0-alpha07

January 28, 2026

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha07` is released. Version 1.3.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..c26c6f088b95903b7b9cd5e6f2092988f1e64dc3/compose/material3/adaptive).

**API Changes**

- Added a composition local to query Material adaptive scene scope. ([I2e0d9](https://android-review.googlesource.com/#/q/I2e0d96f8b3f5c1de0aa2eb929340ed276bf86285), [b/457721741](https://issuetracker.google.com/issues/457721741))
- Add a boolean flag to `PaneScaffoldDirective` to opt out the behavior that automatically moves the focus to the current destination pane. ([I929f5](https://android-review.googlesource.com/#/q/I929f5960c59f10a82b53d701eaf757da9e20f9e2), [b/445720462](https://issuetracker.google.com/issues/445720462))
- `ListDetailSceneStrategy` and `SupportingPaneSceneStrategy` can now opt in to handle scenes with only a single pane. ([I79384](https://android-review.googlesource.com/#/q/I79384dd90efe25321d431e6c96ddce827b93cf64), [b/417475283](https://issuetracker.google.com/issues/417475283))

### Version 1.3.0-alpha06

January 14, 2026

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha06` is released. Version 1.3.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/material3/adaptive).

**Bug Fixes**

- Support RTL with pane expansion anchors ([I0770b](https://android-review.googlesource.com/#/q/I0770bf84ce74eb1ba0534712a47689bebc7f8765), [b/467775639](https://issuetracker.google.com/issues/467775639))
- Fix the issue that shadows of levitated panes are not clipped ([375cf1](https://android-review.googlesource.com/#/q/375cf1d11bde78925fd99ddf6e6204c865f5b13a), [b/470517507](https://issuetracker.google.com/issues/470517507))

### Version 1.3.0-alpha05

December 03, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4d752a0684fb1bf991cd0d15ebd3649ee8684ca1..deb96499dfe95073f5c1215c1287787683cb1e92/compose/material3/adaptive).

### Version 1.3.0-alpha04

November 19, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/de4156d8a5b07409092dc83ff4008ace1c8363e4..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/compose/material3/adaptive).

**Bug Fixes**

- Fixes `ThreePaneScaffold` crashes when margins are set. ([2df348](https://android-review.googlesource.com/#/q/2df348fdb7fbade31bad8be4ae0cc995912a992f))

### Version 1.3.0-alpha03

November 05, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..de4156d8a5b07409092dc83ff4008ace1c8363e4/compose/material3/adaptive).

### Version 1.3.0-alpha02

October 22, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7b8a27d59a3cd5d0aa8259755193aadbd5c119da..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/compose/material3/adaptive).

**API Changes**

- Material adaptive scene strategies now allow passing custom pane adapt strategies ([Iae61d](https://android-review.googlesource.com/#/q/Iae61dc191380579284ba4b6327f9a39676099a1c), [b/437981298](https://issuetracker.google.com/issues/437981298))
- Graduate pane scaffold horizontal order APIs to stable ([I23ab3](https://android-review.googlesource.com/#/q/I23ab3ab5c4ba53729d3c5dc5b3c37a808e2798ce))
- Introduce `DragToResizeState` to Levitate strategy ([I717bd](https://android-review.googlesource.com/#/q/I717bdec3fb84cd15ebe1523684e154fa0a244ce8))
- Deprecate window size APIs ([I6749e](https://android-review.googlesource.com/#/q/I6749ed17a170ca93e516941cc799960f2cad3c50), [b/424442112](https://issuetracker.google.com/issues/424442112))

### Version 1.3.0-alpha01

October 08, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.3.0-alpha01` is released. Version 1.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/60b6e7b051ae202b72ab15ab3c8943e1d3934169..7b8a27d59a3cd5d0aa8259755193aadbd5c119da/compose/material3/adaptive).

**New Features**

- `ListDetailPaneScaffold` and `SupportingPaneScaffold` are now supporting margins and edge-to-edge.
- The `adaptive-navigation3` integration library is being released as 1.3.0-alpha01 since this version (previously 1.0.0-alpha03).

**API Changes**

- Introduce pane margin and edge-to-edge support to `ThreePaneScaffold`. ([If0794](https://android-review.googlesource.com/#/q/If079479d8e3129f1d98ffdd7c69dd14af4b7d3cc), [b/333539848](https://issuetracker.google.com/issues/333539848))

## Compose Material3 Adaptive Version 1.2

### Version 1.2.0

October 22, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5551c4584e9e6e93a700313cdc7b4712aca7a1f9..bda0327f6fc5c110aeed6f8802d8e5210cdefc38/compose/material3/adaptive).

**Important changes since 1.1.0:**

- Introduce `PaneScaffoldScope.preferredHeight` modifier for devs to provide pane preferred heights that will be applied with new adapt strategies we are going to introduce. ([I957dd](https://android-review.googlesource.com/#/q/I957dd252b2bd154e3b0be048c092147fb6d1b2b8))
- Add saveable state holder to `PaneScaffoldScope` ([Id9299](https://android-review.googlesource.com/#/q/Id92990026d6122593dbbaad1700c401a5aeb91f3))
- Introduce reflow strategy for adaptation ([I75c6a](https://android-review.googlesource.com/#/q/I75c6a7bf00556fc6d6d696a4c948ab31385096c1))
- Introduce levitate strategy for adaptation ([I1ba7c](https://android-review.googlesource.com/#/q/I1ba7c36b1ce7b420b56eb7ba7029c9c067ec5338))
- Make `currentWindowAdaptiveInfo()` function support large and extra-large window width size classes ([I92e97](https://android-review.googlesource.com/#/q/I92e9741c67389194f88885b026edfbb0f034fd8a))
- Support custom dragging behavior with pane expansion state ([If5c61](https://android-review.googlesource.com/#/q/If5c613d37bbd1d53aeef19ca7744af37555343b2))

### Version 1.2.0-rc01

October 08, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd..60b6e7b051ae202b72ab15ab3c8943e1d3934169/compose/material3/adaptive).

**Bug Fixes**

- Set default a11y pane title to `AnimatedPanes` ([012113](https://android-review.googlesource.com/#/q/012113aa2e60166324be399fd5064148dc8cf9d8), [b/323387770](https://issuetracker.google.com/issues/323387770))
- Fix incorrect re-anchoring during settling ([ca45f9](https://android-review.googlesource.com/#/q/ca45f974a40de05a6a1443ba151bf66e3a3a3fe3), [b/442911758](https://issuetracker.google.com/issues/442911758))

### Version 1.2.0-beta03

September 24, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-beta03` is released. Version 1.2.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf0316e0a0fa7e872bbfc1f6ecf667c8622db2c7..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/compose/material3/adaptive).

**Bug Fixes**

- Fix incorrect re-anchoring during dragging. ([6453cb6](https://android-review.googlesource.com/#/q/6453cb632bdb9e470367ac04dffe61eb04829ec9))

### Version 1.2.0-beta02

September 10, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-beta02` is released. Version 1.2.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/21ec49263b1dfef28abcfedd25d83950ca381c13..cf0316e0a0fa7e872bbfc1f6ecf667c8622db2c7/compose/material3/adaptive).

**API Changes**

- Remove the drag-to-resize feature from the public API surface ([Ic85ba](https://android-review.googlesource.com/#/q/Ic85ba48ddc8f358abe1996c0d4c8a5c2b938f380), [b/437953743](https://issuetracker.google.com/issues/437953743), [b/442636084](https://issuetracker.google.com/issues/442636084))
- Rename `Scrim()` to `LevitatedPaneScrim()` and hide properties of Levitated and Reflowed classes. ([I090e1](https://android-review.googlesource.com/#/q/I090e1d157101c385c0fefab8d9c48b0d59599053), [b/427953101](https://issuetracker.google.com/issues/427953101))
- Hide `calculatePosture()` API as internal ([Ie7227](https://android-review.googlesource.com/#/q/Ie72276123a57e9565e2e170571cf3c3af2919672), [b/424442112](https://issuetracker.google.com/issues/424442112))

**Bug Fixes**

- Use new initial anchor when pane expansion anchor list changes ([I91cd1](https://android-review.googlesource.com/#/q/I91cd1ecdcc587722214757e05c8b33a6ef70a43b), [b/438829477](https://issuetracker.google.com/issues/438829477))

### Version 1.2.0-beta01

August 27, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..21ec49263b1dfef28abcfedd25d83950ca381c13/compose/material3/adaptive).

**New Features**

- Support alternative input methods for the drag-to-resize feature ([Id7796](https://android-review.googlesource.com/#/q/Id779691a1535717c178538f2e206e3bba0aa40a6))

**API Changes**

- Support custom dragging behavior with pane expansion state ([If5c61](https://android-review.googlesource.com/#/q/If5c613d37bbd1d53aeef19ca7744af37555343b2))
- Adds an indicator in the pane scope interface to denote if a pane should be interactable or not. Also uses this indicator to disable accessibility access for underlying panes when a levitated pane is shown with a scrim. ([If36f3](https://android-review.googlesource.com/#/q/If36f3851addfe8ba48386440641c2462ee866a52))
- Replace Scrim definition with composable lambdas ([I7d811](https://android-review.googlesource.com/#/q/I7d811504d4e0e22844387aefa94de4e1b4168f80))
- Mark window size and posture related APIs as experimental ([I4ee96](https://android-review.googlesource.com/#/q/I4ee962a4c17597fc77f378a158cd35f841378982))
- Expose `PaneScaffoldHorizontalOrder` as a sealed public API ([Ia4ebe](https://android-review.googlesource.com/#/q/Ia4ebe8bda3df76c0470774401235559878af580d))

**Bug Fixes**

- Workaround the crash caused by unnecessary approaching measure ([I0a65a](https://android-review.googlesource.com/#/q/I0a65accd2dd2031b5855f68a591f604fb0bca5c4), [b/418932957](https://issuetracker.google.com/issues/418932957))

### Version 1.2.0-alpha11

August 13, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha11` is released. Version 1.2.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/material3/adaptive).

**API Changes**

- Introduce a generic `PaneScaffoldRole` interface to improve API readability ([I1b757](https://android-review.googlesource.com/#/q/I1b75744323c860800a379cb0da57d71e23355204))
- Remove `AdaptStrategy.Levitated.Strategy` class ([I6f798](https://android-review.googlesource.com/#/q/I6f7988e068342eac76488c121ea1bcb19ec2d68c))
- Changes `Modifier.preferredWidth/Height`'s proportion parameter from Int percentage values to Float ranges from 0 to 1. ([Ib2de2](https://android-review.googlesource.com/#/q/Ib2de2d23bb8918e62d9f4a6efe3332fe308dba43))

**Bug Fixes**

- Fix the issue that initial anchors are not respected ([I32f5d](https://android-review.googlesource.com/#/q/I32f5dac072a4870f669edab7cce6aafc7ce9467c), [b/418296559](https://issuetracker.google.com/issues/418296559))

### Version 1.2.0-alpha10

July 30, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha10` is released. Version 1.2.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..5fa9d0954ece0376736164b0f7bc2ef33506ab70/compose/material3/adaptive).

**API Changes**

- Support preferred width/height represented in proportions. ([I63dda](https://android-review.googlesource.com/#/q/I63dda4cdb0c654ab5d0004eedca5fc0a0b73ae01))
- Hides Reflow and Levitate strategies' constructor parameters; also renames `targetPane` to `reflowUnder`. ([Ifa81b](https://android-review.googlesource.com/#/q/Ifa81b09b51e0edd1a71e14c348083ae30344feac))

**Bug Fixes**

- Fix performance regression caused by snapshoting the scaffold state transition progress ([I3d555](https://android-review.googlesource.com/#/q/I3d5553b6942a2061d8e3fc44e441ffbcf0011cb2), [b/417329258](https://issuetracker.google.com/issues/417329258))

### Version 1.2.0-alpha09

July 16, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha09` is released. Version 1.2.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/compose/material3/adaptive).

### Version 1.2.0-alpha08

July 2, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha08` is released. Version 1.2.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..1b437892629a2cdedb46d9b7232575987b2cc6b5/compose/material3/adaptive).

### Version 1.2.0-alpha07

June 18, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha07` is released. Version 1.2.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/compose/material3/adaptive).

**API Changes**

- Make `currentWindowAdaptiveInfo()` function support large and extra-large window width size classes and promote `calculatePosture()` and `currentWindowDpSize()` functions to stable. ([I92e97](https://android-review.googlesource.com/#/q/I92e9741c67389194f88885b026edfbb0f034fd8a))

### Version 1.2.0-alpha06

May 20, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha06` is released. Version 1.2.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/compose/material3/adaptive).

**New Features**

- The default pane scaffold directive calculation functions is now supporting L and XL window width size classes.

**API Changes**

- Make `Modifier.paneExpansionDraggable` provide default accessibility semantics and promote relevant APIs to stable. ([Idb818](https://android-review.googlesource.com/#/q/Idb818e363173d620577582c45ba6fa2bec052e8c))
- Support drag-to-resize with levitated panes ([Idadd3](https://android-review.googlesource.com/#/q/Idadd3ea068465614857b0ff626d2aee9df4cfec3))
- Support scrims for levitated panes ([I9b091](https://android-review.googlesource.com/#/q/I9b091f202e0dbb597b8588b82aeccfc38aec012f))

### Version 1.2.0-alpha05

May 7, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha05` is released. Version 1.2.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/material3/adaptive).

**New Features**

- Material3 adaptive layouts are now supporting Levitated adapt strategies that can turn a pane into a floating popup.

**API Changes**

- Make current window size functions support multi-platform ([Ie4172](https://android-review.googlesource.com/#/q/Ie41728eeac80411a53a39c74394dc7d0bded3ce4))
- Introduce pane motions for levitated panes ([Ic9dc3](https://android-review.googlesource.com/#/q/Ic9dc31c7b3edfecbca477bf3e9f0be864f672307))
- Introduce levitate strategy for adaptation ([I1ba7c](https://android-review.googlesource.com/#/q/I1ba7c36b1ce7b420b56eb7ba7029c9c067ec5338))

**Bug Fixes**

- Fix the usage of coroutine scope in adaptive samples ([7631016](https://android-review.googlesource.com/#/q/7631016ea5e0f05a01fc5fe912b5d85fd703fe14))

### Version 1.2.0-alpha04

April 23, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha04` is released. Version 1.2.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/material3/adaptive).

**New Features**

- Reflow strategies are now available with `ListDetailPaneScaffold` and `SupportingPaneScaffold`, which reflows the associated pane under a single-pane layout setting.

**API Changes**

- Add saveable state holder to `PaneScaffoldScope` ([Id9299](https://android-review.googlesource.com/#/q/Id92990026d6122593dbbaad1700c401a5aeb91f3))
- Introduce reflow strategy for adaptation ([I75c6a](https://android-review.googlesource.com/#/q/I75c6a7bf00556fc6d6d696a4c948ab31385096c1))

**Bug Fixes**

- Fix the bug that panes not animate in the first transition. ([Ib0415](https://android-review.googlesource.com/#/q/Ib0415e8f04345177d87efaa3d44e0b567ae486e3))
- Fix preferred heights not working. ([I1913b](https://android-review.googlesource.com/#/q/I1913b4463ef1ee604244ce57699bac763a9a104b))
- Fix the bug that scaffold directive is not correctly updated. ([0403ab](https://android-review.googlesource.com/#/q/0403ab325595d1563ffe5748759f0439c98fdc7d))

### Version 1.2.0-alpha03

April 9, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha03` is released. Version 1.2.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52/compose/material3/adaptive).

**Bug Fixes**

- Fix drag handle incorrectly showing on single pane layout. ([806e443](https://android-review.googlesource.com/#/q/806e4434a4c7e5daf6bb1bb62f9a17ca232274b1))

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.2.0-alpha02

March 26, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha02` is released. Version 1.2.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/compose/material3/adaptive).

### Version 1.2.0-alpha01

March 12, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.2.0-alpha01` is released. Version 1.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ebeae502fb9637851a88554d75ff2c9280422de2..7a145e052ae61e272e91ffe285e9451b8ab71870/compose/material3/adaptive).

**API Changes**

- Introduce `PaneScaffoldScope.preferredHeight` modifier for devs to provide pane preferred heights that will be applied with new adapt strategies we are going to introduce. ([I957dd](https://android-review.googlesource.com/#/q/I957dd252b2bd154e3b0be048c092147fb6d1b2b8), [b/220960090](https://issuetracker.google.com/issues/220960090))
- Rename `ComponentOverride` types to `Override`, and `ComponentOverrideContext` types to `OverrideScope`. ([Id973c](https://android-review.googlesource.com/#/q/Id973c0d2fd806e8d5f53375690e0e487afb7fd91))
- Rename some component override methods. ([I222b3](https://android-review.googlesource.com/#/q/I222b3cbee858e60464f5f6a527c3f7d7fadc602c))

## Compose Material3 Adaptive Version 1.1

### Version 1.1.0

March 12, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ebeae502fb9637851a88554d75ff2c9280422de2..5551c4584e9e6e93a700313cdc7b4712aca7a1f9/compose/material3/adaptive).

**Important changes since 1.0.0**

- [`ListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) and [`SupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#SupportingPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) is now supporting the pane expansion feature - users can drag to change the default pane split of a dual pane layout, developers can also change the pane split at runtime via altering the newly introduced [`PaneExpansionState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/PaneExpansionState).
- Default predictive back support is now available with [`NavigableListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#NavigableListDetailPaneScaffold(androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldNavigator,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.material3.adaptive.navigation.BackNavigationBehavior,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) and [`NavigableSupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#NavigableSupportingPaneScaffold(androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldNavigator,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.material3.adaptive.navigation.BackNavigationBehavior,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)). You can also use [`ThreePaneScaffoldPredictiveBackHandler`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#ThreePaneScaffoldPredictiveBackHandler(androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldNavigator,androidx.compose.material3.adaptive.navigation.BackNavigationBehavior)) to provide predictive back support with your own three pane scaffold implementations.
- You can now customize your pane motions during pane switching by providing different `EnterTransition` and `ExitTransition` to [`AnimatedPane`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#(androidx.compose.material3.adaptive.layout.ExtendedPaneScaffoldPaneScope).AnimatedPane(androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)).

### Version 1.1.0-rc01

February 26, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/12f38ed3744a6cb1592cbc6d053dc2adb328f142..ebeae502fb9637851a88554d75ff2c9280422de2/compose/material3/adaptive).

**Bug Fixes**

- Disable three pane scaffold predictive back scale ([ab6fd0b](https://android-review.googlesource.com/#/q/ab6fd0b93dff5532042e8ab3e17cfaa9e8b95d68))

### Version 1.1.0-beta02

February 12, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-beta02` is released. Version 1.1.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82aef93384cbb5515cac6b2380d567d813e47308..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/compose/material3/adaptive).

**API Changes**

- Changed how `isPredictiveBackInProgress` is set in `MutableThreePaneScaffoldState` animation functions to preserve state consistency. ([Idc97f](https://android-review.googlesource.com/#/q/Idc97f297e74a4c2cafa3153fe9ff37153a559365))

**Bug Fixes**

- The default back behavior of `NavigableListDetailPaneScaffold` and `NavigableSupportingPaneScaffold` has been changed to `PopUntilScaffoldValueChange` for consistency with the rest of the library. ([I873f0](https://android-review.googlesource.com/#/q/I873f0ac64ba0d47470de2db01cd132d2f6f9e622))
- Set the correct accessibility traversing order of pane scaffolds. ([67d030](https://android-review.googlesource.com/#/q/67d030b5da1661462fe291466a13117635b97852))
- Fix the issue that pane content states are not saved. ([88b0ff](https://android-review.googlesource.com/#/q/88b0ffebf9a6edae34632d514d4b6c72d22b3d9e))
- Support alternative accessibility actions in place of dragging. ([28266d](https://android-review.googlesource.com/#/q/28266d19df8e36ea27cc881452fec600561853e2))
- Announce the current pane split after it's changed. ([0c3a80](https://android-review.googlesource.com/#/q/0c3a80ad3ac424ff767e02c6b5ad6f5dca41c5de))

### Version 1.1.0-beta01

January 29, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..82aef93384cbb5515cac6b2380d567d813e47308/compose/material3/adaptive).

**API Changes**

- Introduce factory functions to create pane expansion anchors of the offset type from the start and the end, respectively. ([I2eb21](https://android-review.googlesource.com/#/q/I2eb21917bbc9b63fb047eaf42f57784b4a54da06))
- Seal `PaneMotion` interface and remove its default transition methods. ([Ifc4c7](https://android-review.googlesource.com/#/q/Ifc4c783ba071091ee5025a57943f6ae4dc82d72d))
- Introduce APIs to get the current anchor and animate to an anchor. ([Icf95d](https://android-review.googlesource.com/#/q/Icf95d7dd22db992ddac0ec021b9d2da931590202))
- Introduce accessibility APIs for pane expansion ([Icc669](https://android-review.googlesource.com/#/q/Icc669563fd675dcee715d9711351bc51d887e1c6))
- Change `PaneScaffoldParentData.preferredWidth`'s type to DP. ([Id98ee](https://android-review.googlesource.com/#/q/Id98ee199b6f7b02004554625d23704fc40436fc7))

### Version 1.1.0-alpha09

January 15, 2025

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha09` is released. Version 1.1.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce211eef13c32d283bb64f2db117d93783070672..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/material3/adaptive).

**API Changes**

- Add and use new experimental annotation `ExperimentalMaterial3AdaptiveComponentOverrideApi`. ([Id45aa](https://android-review.googlesource.com/#/q/Id45aaaf8a1b85be49a1f40ebd7e054e57fa5813f))
- Hide `ThreePaneScaffoldHorizontalOrder.toLtrOrder`. ([I6f8d2](https://android-review.googlesource.com/#/q/I6f8d2fd927164bf4653068c489c5f77536e79abc))
- `ThreePaneScaffoldPredictiveBackHandler` has been made public. ([I1a995](https://android-review.googlesource.com/#/q/I1a9957b3f9d8bbd85025066e53c93ec87d6cd5e7), [b/370543873](https://issuetracker.google.com/issues/370543873))
- Added `isPredictiveBackInProgress` property to `ThreePaneScaffoldState`. ([I1a995](https://android-review.googlesource.com/#/q/I1a9957b3f9d8bbd85025066e53c93ec87d6cd5e7), [b/370543873](https://issuetracker.google.com/issues/370543873))
- Create overriding mechanism for `AnimatedPane` to support sideloading implementations for different form factors. ([Id7622](https://android-review.googlesource.com/#/q/Id76229fe4b3002551eeb134b9ec7a5917eafb8b2))

**Bug Fixes**

- Fix the issue when the settling direction has no anchors. ([df8257d](https://android-review.googlesource.com/#/q/df8257d2a6da42b18eafc14cbbb7db0471362b46))

### Version 1.1.0-alpha08

December 12, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha08` is released. Version 1.1.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..105dbfc6218aa1777d726fcdc715d59fa2e1a1ff/compose/material3/adaptive).

**API Changes**

- Introduce `currentWindowDpSize` function. ([I99125](https://android-review.googlesource.com/#/q/I991255c27fc9fa7aee15a52e99d6fb91ee27b77d), [b/296300441](https://issuetracker.google.com/issues/296300441))
- Expose `PaneScaffoldParentData` and `ThreePaneScaffoldHorizontalOrder.toLtrOrder()` ([I2d6b7](https://android-review.googlesource.com/#/q/I2d6b73dbbf56d0a6602346129e8979e98f579d42))
- Remove `PaneScaffoldMotionScope` and turn it into a field under `PaneScaffoldTransitionScope`. Also rename it to `PaneScaffoldMotionDataProvider` and remove the access to the underlying data structure of PaneMotionData - instead, provide getter and looping methods for accessing the data. ([Id8884](https://android-review.googlesource.com/#/q/Id8884de1cf9f74f006bc2cc3b8a515666e431976))
- Create overriding mechanism for `ThreePaneScaffold` to support sideloading implementations for different form factors. ([I5280f](https://android-review.googlesource.com/#/q/I5280fdbe1a2f5ed7f63be6c032fc1b85f47e02ea))
- Makes pane expansion state null by default ([Ia65f8](https://android-review.googlesource.com/#/q/Ia65f8919ba9aaaa4c611ecb40514ee41d1e8d56f), [b/376394520](https://issuetracker.google.com/issues/376394520))

### Version 1.1.0-alpha07

November 13, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha07` is released. Version 1.1.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/material3/adaptive).

**API Changes**

- Remove drag handle implementation in the adaptive library and encourage people to use the M3 version of it. And at the same time introduce a modifier to provide pane expansion dragging ability to a provided drag handle composable. Also hide `DraggableState` as an implementation detail so we can change it later if needed. ([Ib50cd](https://android-review.googlesource.com/#/q/Ib50cda6b33334d62f9722e87611901b5a42ad770))
- Moves the entry point of pane motion customization from the scaffold functions to `AnimatedPane` according to UXR feedback. ([I10f72](https://android-review.googlesource.com/#/q/I10f72e8f75e952ce6e19181ca6a322d31d2a8feb))
- Introduce fling support and custom animation spec for pane expansion. ([Ie207d](https://android-review.googlesource.com/#/q/Ie207deb40f036d3b21334ec8ee6dea63cedcc84e), [b/362584341](https://issuetracker.google.com/issues/362584341))

**Bug Fixes**

- Fix predictive back issues on cancellation. ([36a3e0a](https://android-review.googlesource.com/#/q/36a3e0acbfe7e1961374e9f5c9af2d29faa2f8a0)), ([b/369899645](https://issuetracker.google.com/issues/369899645))

### Version 1.1.0-alpha06

October 30, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha06` is released. Version 1.1.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/955f3c40a6dc8e5772c53a0edaa2f36f94d43bb0..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/material3/adaptive).

**API Changes**

- Add `FloatRange` to `PaneScaffoldTransitionScope.motionProgress`. ([Iac0dd](https://android-review.googlesource.com/#/q/Iac0dd5a7cb56a1779a8f04560e71aa2ac0916989))
- Change navigator params' type to generic types in navigable scaffolds. ([I1da6e](https://android-review.googlesource.com/#/q/I1da6e29ea212a2e6f15ed04326624ef115196c24))

### Version 1.1.0-alpha05

October 16, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha05` is released. Version 1.1.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/material3/adaptive).

**API Changes**

- Introduce animation specs class to ensure more consistent motion behavior and future expandability. ([I2d3cc](https://android-review.googlesource.com/#/q/I2d3cc0a049e9f749f7fce05571d846b43ac94895))
- Provide motion type and rename currentXXXXX in `PaneMotionData` to originXXXX. ([I7c61a](https://android-review.googlesource.com/#/q/I7c61a34b29febee3c9a4992db51e0ee8102b40f3))

### Version 1.1.0-alpha04

October 2, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha04` is released. Version 1.1.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/compose/material3/adaptive).

**New Features**

- Added predictive back support to `NavigableListDetailPaneScaffold` and `NavigableSupportingPaneScaffold`. ([I4dc21](https://android-review.googlesource.com/#/q/I4dc211a1f2760063543e67ec1d55295edc688419), [b/359616816](https://issuetracker.google.com/issues/359616816))

**API Changes**

- Added `ThreePaneScaffoldState` to `ThreePaneScaffoldNavigator`. Navigation methods have been made `suspend` to support navigation with animation. Added `seekBack` to support partial navigation states (e.g. predictive back). ([I5a651](https://android-review.googlesource.com/#/q/I5a6514097b98571304fb974315546d006ff10a69), [b/359616816](https://issuetracker.google.com/issues/359616816))
- Added `MutableThreePaneScaffoldState` to control the transition between scaffold values. The existing `ThreePaneScaffoldState` has been made read-only. ([Idb3c6](https://android-review.googlesource.com/#/q/Idb3c6807dab6134c24ac061cab883ac9acbed2ec))
- Expose default pane motion implementations ([I95a7b](https://android-review.googlesource.com/#/q/I95a7b96360c9b01d3b72a01fa0ccb13bf38f6b52))
- Enable setting initial anchor of pane expansion state ([Ie41b3](https://android-review.googlesource.com/#/q/Ie41b3423ec8f6ed7c1e23b074dac5f38980ccca2), [b/362350560](https://issuetracker.google.com/issues/362350560))

**Bug Fixes**

- Enforce 48x48dp min touch target size of drag handle ([7ce6635](https://android-review.googlesource.com/#/q/7ce66358501efb390647790c98cdd43899594f0f), [b/366018217](https://issuetracker.google.com/issues/366018217))
- Restore anchored position after configuration changes ([3c9fc6b](https://android-review.googlesource.com/#/q/3c9fc6bc93bd00073d1f094af24a088aad3445d8), [b/362353672](https://issuetracker.google.com/issues/362353672))

### Version 1.1.0-alpha03

September 18, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha03` is released. Version 1.1.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/material3/adaptive).

### Version 1.1.0-alpha02

September 4, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha02` is released. Version 1.1.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/compose/material3/adaptive).

**New Features**

- Motion customization ([I0bf9c](https://android-review.googlesource.com/#/q/I0bf9c6dc7e824c01bee31647e6d284085ce86268)), ([I80e66](https://android-review.googlesource.com/#/q/I80e66cde5edc45a8476faab8251ec7cc5ea3c26c)) is supported for makers to change the default motions during adaptive scaffold state changes. Makers can choose from a set of default entering and exiting transitions, or implement pure custom transitions with the info provided through new motion scopes.
- Implement fading animation of pane expansion drag handles ([46e3c69](https://android-review.googlesource.com/#/q/46e3c693fe4527c31b79731007b18537b1f888a5))
- Make remembered `PaneExpansionState` Saveable ([61ff76f](https://android-review.googlesource.com/#/q/61ff76f1052daeea6fd81ff6612176fd911e1e67))

**API Changes**

- Add missing pane expansion APis to scaffolds ([Ic5bc0](https://android-review.googlesource.com/#/q/Ic5bc051d20659e99ffcdd9ff226923fda934ff05))
- `ThreePaneScaffoldDestinationItem.content` renamed to `contentKey`. `rememberListDetailPaneScaffoldNavigator` and `rememberSupportingPaneScaffoldNavigator` default type argument changed from `Nothing` to `Any`. ([I58749](https://android-review.googlesource.com/#/q/I587499f38bdf440aab2e0bdfec2ec893fe0bc6a7))
- Mark `ThreePaneScaffoldState` as stable ([I64aec](https://android-review.googlesource.com/#/q/I64aec38dc00427a127d072fa73e71a7a10f5925d))
- Make drag handle parameters be scoped ([Ic0aa2](https://android-review.googlesource.com/#/q/Ic0aa2cc867aeaa243df2c35e6d5f7aa10fd2dbe3))

### Version 1.1.0-alpha01

August 21, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c/compose/material3/adaptive).

**New Features**

- Introduce pane expansion support of adaptive scaffolds.

**API Changes**

- Introduce pane expansion APIs to public ([I301d6](https://android-review.googlesource.com/#/q/I301d6a9efc34f352707aaabe45dca05ed40a9f97))
- Introduced `ThreePaneScaffoldState` to control pane value transitions. Added overloads of `ListDetailPaneScaffold` and `SupportingPaneScaffold` which accept this state. ([I5db3b](https://android-review.googlesource.com/#/q/I5db3b9c26ff5a6d0911473015229895a13c09fb5))
- Introduce pane expansion key and key provider interface ([Id621f](https://android-review.googlesource.com/#/q/Id621f67b8e0504e4d0e9f8084fb809b38ea1d081))

**Bug Fixes**

- Fix wrong partition calculation when excluded hinge presents. ([9dfd483](https://android-review.googlesource.com/#/q/9dfd483fadc0fdf3d27731c7567889650b0da10f))

## Compose Material3 Adaptive Version 1.0

### Version 1.0.0

September 4, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dd9a31e5a50f13aac48ebad38d86405cca057a46..cad2089d1b7edd842b0132ba03a6d2fa4ee7d1a1/compose/material3/adaptive).

**Major features of 1.0.0**

- One-liner Composable functions [`currentWindowSize()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowSize()), [`collectFoldingFeaturesAsState()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#collectFoldingFeaturesAsState()), and [`currentWindowAdaptiveInfo()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowAdaptiveInfo()) to get required window info to adapt apps, like window sizes and folding features.
- [`ListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) and [`SupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#SupportingPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) to provide two Material3 canonical layouts that will adapt themselves automatically according to different window configurations. Those two scaffolds are also fully customizable to suit makers' different needs.
- [`ThreePaneScaffoldNavigator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/ThreePaneScaffoldNavigator) and its relevant remember functions, [`rememberListDetailPaneScaffoldNavigator()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#rememberListDetailPaneScaffoldNavigator(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldAdaptStrategies,kotlin.Boolean,kotlin.collections.List)) and [`rememberSupportingPaneScaffoldNavigator()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#rememberSupportingPaneScaffoldNavigator(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldAdaptStrategies,kotlin.Boolean,kotlin.collections.List)) to provide navigation solutions within an adaptive scaffold, which can show multiple navigation destinations at the same time, comparing to the common one-destination-at-a-time setup in the non-adaptive world.
- Default, built-in Material3 animations when changing adaptive scaffold states.

### Version 1.0.0-rc01

August 21, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/967bd940b24778daf0ac5f9661bc881f4d0487c1..dd9a31e5a50f13aac48ebad38d86405cca057a46/compose/material3/adaptive).

**Bug Fixes**

- Fix wrong partition calculation when excluded hinge presents. ([9dfd483](https://android-review.googlesource.com/#/q/9dfd483fadc0fdf3d27731c7567889650b0da10f))

### Version 1.0.0-beta04

June 26, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-beta04` is released. Version 1.0.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..967bd940b24778daf0ac5f9661bc881f4d0487c1/compose/material3/adaptive).

**Bug Fixes**

- Fixes the issue that when hinge bounds get updated, the layout is not updated accordingly. ([71e9cf1](https://android.googlesource.com/platform/frameworks/support/+/71e9cf129cea74cd1f99b2a08bc9c7f05e0f01e1))

### Version 1.0.0-beta03

June 12, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-beta03` is released. Version 1.0.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..f5541f29d045c6ba9734689ec67891f8d667412b/compose/material3/adaptive).

**Bug Fixes**

- Fixes crashes caused by incorrect dependency resolution in beta02.

### Version 1.0.0-beta02

May 29, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-beta02` is released. Version 1.0.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/compose/material3/adaptive).

### Version 1.0.0-beta01

May 14, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/material3/adaptive).

### Version 1.0.0-alpha12

May 1, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..fbd1ac175922f44c69a13545d194066ee428b342/compose/material3/adaptive).

**API Changes**

- Add `isFlat` info to `HingeInfo` ([Ie0516](https://android-review.googlesource.com/#/q/Ie0516b1327e334b39a4409c1cfa8c3ef354e1d45), [b/333784198](https://issuetracker.google.com/issues/333784198))
- Make adaptive APIs non-experimental ([I1d038](https://android-review.googlesource.com/#/q/I1d0386470d06287365782befa85688c43bfab796))
- Make adaptive layout APIs non-experimental ([Id23df](https://android-review.googlesource.com/#/q/Id23df7a2b0c2978b43f423a85b1b2b26196b2ee6))
- Changed `BackNavigationBehavior` from an enum to a value class ([Id8757](https://android-review.googlesource.com/#/q/Id875736f68f20b0977c91d6b8b04f535436e031a))

**Bug Fixes**

- Change transition fraction to a lambda ([I6f5a9](https://android-review.googlesource.com/#/q/I6f5a97dde7d2d9a515c77e22ece89ca2c58870c2))
- Fix the initial state issue of `SizeTracker` ([18326a9](https://android-review.googlesource.com/#/q/18326a9a37f7618b589d28940aaee4f385868c8b))
- Include hinge list in `Posture` equality check ([6687137](https://android-review.googlesource.com/#/q/66871370eadb0ee44880e64f03c49d6ff8f2f910))

### Version 1.0.0-alpha11

April 17, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/material3/adaptive).

**API Changes**

- Make scope interfaces sealed. ([Iefa57](https://android-review.googlesource.com/#/q/Iefa575ae140202e21852e31a5ba0e87fa993b3d9))
- Introduce `AnimatedPaneScope`. ([I62d73](https://android-review.googlesource.com/#/q/I62d73a2322ad61b1734bfdb9782e5644741887f4), [b/332750742](https://issuetracker.google.com/issues/332750742))
- Make `AdaptStrategy` sealed and stable. ([Ia28b2](https://android-review.googlesource.com/#/q/Ia28b2d2f72bc47e57afd6663171c7c9d93ee3fe5))
- Introduce a copy method of `PaneScaffoldDirective`. ([I9291f](https://android-review.googlesource.com/#/q/I9291f4b5f096e9f6266ed13081a6c9dab2427259))
- Mark `ThreePaneScaffoldScope` as experimental. ([I9d527](https://android-review.googlesource.com/#/q/I9d527052dd8983fd87998fdc269152ac93f67d3b))
- Provide easy-to-use scaffold APIs that supports navigation. ([I263f0](https://android-review.googlesource.com/#/q/I263f0b41823e6220cd65994185e7aa783a52461d), [b/321010778](https://issuetracker.google.com/issues/321010778))

### Version 1.0.0-alpha10

April 3, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/material3/adaptive).

**API Changes**

- Make default preferred width adaptive and customizable. ([Ic3abc](https://android-review.googlesource.com/#/q/Ic3abc99f731e2f5fdbd5e6c44a20b09f7df385e5))
- Rename scaffold directive calculation functions. ([I10855](https://android-review.googlesource.com/#/q/I10855d06919ffbcf67b121b24fdaff92dd6f5ebd))
- Remove paddings and insets from scaffold APIs. ([I786f8](https://android-review.googlesource.com/#/q/I786f86697df87c3ed96cdf3cb3065c030057db43))
- Add navigator remember methods without generic types. ([I607c3](https://android-review.googlesource.com/#/q/I607c33b7b6b848d3617d8b90bfb3ae217589bd29))

### Version 1.0.0-alpha09

March 20, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/material3/adaptive).

**API Changes**

- Add state transition fields to `ThreePaneScaffoldScope`. ([I3d917](https://android-review.googlesource.com/#/q/I3d917e0f7a57a8f7504897fc559bfe380e7537dd))
- Reorder scaffold parameters. ([I4dff5](https://android-review.googlesource.com/#/q/I4dff5e539bf4b05f6b006d94ea9f6eb790aa42f7))
- Provide default value of `AnimatedPane` modifier parameter. ([I77dd7](https://android-review.googlesource.com/#/q/I77dd7b4481fa5d247f91535677581ae4f38e92dd))

**Bug Fixes**

- Include spacer size into pane motions. ([a3174ca](https://android-review.googlesource.com/#/q/a3174cad15c8db6b9008ee2c4d1157b453ab4624))

### Version 1.0.0-alpha08

March 6, 2024

`androidx.compose.material3.adaptive:adaptive-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/88dfe1dd1c2dab49147d5ee69f6dbd1c7d1fe1a5..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/material3/adaptive).

**New Features**

- Implement delayed sliding in when switching panes. ([I1a38e](https://android-review.googlesource.com/#/q/I1a38e35fdec953696478b42dcd8eb0170289214d))

**API Changes**

- Removed the `ThreePaneScaffoldState` interface. ([I63f23](https://android-review.googlesource.com/#/q/I63f23c0b31bcf5ea7d5a94927081824dbda4025b))

### Version 1.0.0-alpha07

February 21, 2024
| **Note:** This page contains the Jetpack Compose Material3 Adaptive libraries starting from alpha07.