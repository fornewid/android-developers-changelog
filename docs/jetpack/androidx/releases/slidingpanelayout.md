---
title: https://developer.android.com/jetpack/androidx/releases/slidingpanelayout
url: https://developer.android.com/jetpack/androidx/releases/slidingpanelayout
source: md.txt
---

# Slidingpanelayout

API Reference  
[androidx.slidingpanelayout.widget](https://developer.android.com/reference/kotlin/androidx/slidingpanelayout/widget/package-summary)  
Implement a sliding pane UI pattern.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 26, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout#1.2.0) | - | - | - |

## Declaring dependencies

To add a dependency on SlidingPaneLayout, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.slidingpanelayout:slidingpanelayout:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.slidingpanelayout:slidingpanelayout:1.2.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460835+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460835&template=1422627)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.2.0

### Version 1.2.0

January 26, 2022

`androidx.slidingpanelayout:slidingpanelayout:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/45c977739a46f49c3eab1fe134b54676db023544..16c3853a6d1da7f15bb226b272ce1db44beaf501/slidingpanelayout/slidingpanelayout)

**Important changes since 1.1.0**

- `SlidingPaneLayout` is now **fold-aware** . On a foldable device, `SlidingPaneLayout` will automatically adjust the size of the two panes so that the panes are on either side of the fold, hinge, etc.
- When handling your own configuration changes, - `SlidingPaneLayout` now animates between the single pane and two pane modes when the amount of space provided changes (i.e., when unfolding a foldable device).
- `SlidingPaneLayout` now has a new UI styling when the two panes overlap. Each pane will now extend from edge to edge, with the detail or secondary pane fully covering the list or primary pane when the `SlidingPaneLayout` is open. APIs specific to the old UI styling, such as the fade color, have been deprecated.
- `SlidingPaneLayout` now defaults to 'closed' - i.e., showing the list or primary pane. Calling `open()` or `openPane()` will now show the detail or secondary pane.
- Improved compatibility with additional measure specs to ensure that `SlidingPaneLayout` can be used in any type of layout without throwing an `IllegalStateException`.
- SlidingPaneLayout now allows registering multiple PanelSlideListeners.
- Developers can now control whether users can swipe between the list and detail panes by setting a lock mode.

### Version 1.2.0-rc01

December 15, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..45c977739a46f49c3eab1fe134b54676db023544/slidingpanelayout/slidingpanelayout)

**Dependency updates**

- `SlidingPaneLayout` now depends on [Window `1.0.0-rc01`](https://developer.android.com/jetpack/androidx/releases/window#1.0.0-rc01), fixing incompatibilities with previous beta versions of AndroidX Window.

### Version 1.2.0-beta01

September 1, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-beta01` is released with no notable changes. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7da80dd5f7c0c44d669ccb882c1aa6f81569254d..47e81d1c497b8a57534a460c277855db1b0257ae/slidingpanelayout/slidingpanelayout)

### Version 1.2.0-alpha04

August 18, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..7da80dd5f7c0c44d669ccb882c1aa6f81569254d/slidingpanelayout/slidingpanelayout)

**New Features**

- `SlidingPaneLayout` now animates between the single pane and two pane modes when using a Foldable device. ([aosp/1702066](https://android-review.googlesource.com/c/platform/frameworks/support/+/1702066/), [b/186211031](https://issuetracker.google.com/186211031))
- Improved compatibility with additional measure specs to ensure that `SlidingPaneLayout` can be used in any type of layout without throwing an `IllegalStateException`. ([aosp/1774187](https://android-review.googlesource.com/1774187), [aosp/1773623](https://android-review.googlesource.com/1773623), [aosp/1773256](https://android-review.googlesource.com/1773256))

**Bug Fixes**

- Fixed an issue where tapping on an empty position of the detail pane would pass through clicks to the list pane when the panes overlap. ([aosp/1755141](https://android-review.googlesource.com/1755141))

**Dependency Updates**

- SlidingPaneLayout now depends on [Window 1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/window#1.0.0-alpha10).

### Version 1.2.0-alpha03

June 30, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..19ae3a88ff0824d615355b492cb56049e16991f2/slidingpanelayout/slidingpanelayout)

**Dependency changes**

- SlidingPaneLayout now depends on [Window `1.0.0-alpha09`](https://developer.android.com/jetpack/androidx/releases/window#1.0.0-alpha09).

### Version 1.2.0-alpha02

May 5, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/slidingpanelayout/slidingpanelayout)

**Bug Fixes**

- `SlidingPaneLayout` now takes into account folding features that have a non-zero width. ([847cc2](https://android-review.googlesource.com/c/platform/frameworks/support/+/1678094))
- `SlidingPaneLayout` now expands the drag edge size when gesture navigation is enabled, mirroring the behavior of `DrawerLayout`. ([2c6d24](https://android-review.googlesource.com/c/platform/frameworks/support/+/1664980))
- The open and closed state of `SlidingPaneLayout` is now preserved even if it is changed when the device is non-slidable (i.e., when both panes are shown side by side), thus ensuring that users will continue to see the detail screen when they rotate their device or otherwise switch to a smaller display. ([b15eda](https://android-review.googlesource.com/c/platform/frameworks/support/+/1681593))
- Fix lock mode behavior ([Ic01dc](https://android-review.googlesource.com/#/q/Ic01dcef161ec0800d79bd257c17226480d50108d))

**External Contributions**

- Thanks Cesar Valiente for fixing `SlidingPaneLayout` to now take into account folding features that have a non-zero width. ([847cc2](https://android-review.googlesource.com/c/platform/frameworks/support/+/1678094))

### Version 1.2.0-alpha01

March 24, 2021

`androidx.slidingpanelayout:slidingpanelayout:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f778df0ff4a2d74de91163d48b9a03fa278397e7..5c42896eb6591b09e3952030fb7ea8d9b8c42713/slidingpanelayout/slidingpanelayout)

**New Features**

- `SlidingPaneLayout` is now **fold-aware** . On a foldable device, `SlidingPaneLayout` will automatically adjust the size of the two panes so that the panes are on either side of the fold, hinge, etc.

**Behavior Changes**

- `SlidingPaneLayout` now has a new UI styling when the two panes overlap. Each pane will now extend from edge to edge, with the detail or secondary pane fully covering the list or primary pane when the `SlidingPaneLayout` is open. APIs specific to the old UI styling, such as the fade color, have been deprecated. ([Ia60ce](https://android-review.googlesource.com/#/q/Ia60cedb855a39d79489774a8b1961248a8026fb9))
- `SlidingPaneLayout` now defaults to 'closed' - i.e., showing the list or primary pane. Calling `open()` or `openPane()` will now show the detail or secondary pane. ([I5d26c](https://android-review.googlesource.com/#/q/I5d26cbab8f00c52910d2a283f57349780fc93d0d))

**API Changes**

- SlidingPaneLayout now allows registering multiple PanelSlideListeners. ([I50ce2](https://android-review.googlesource.com/#/q/I50ce2f92348cc3c9e6ee8a7e27ae64e62e88e88f))
- Developers can now control whether users can swipe between the list and detail panes by setting a lock mode. ([Idf2fd](https://android-review.googlesource.com/#/q/Idf2fdc56a37e4cfdcfa80b5bbc4c498cfda54ae2), [I5d26c](https://android-review.googlesource.com/#/q/I5d26cbab8f00c52910d2a283f57349780fc93d0d))

## Version 1.1.0

### Version 1.1.0

June 24, 2020

`androidx.slidingpanelayout:slidingpanelayout:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75f3faf4ff897611ef2e732ed0be0187917d797e..f778df0ff4a2d74de91163d48b9a03fa278397e7/slidingpanelayout/slidingpanelayout)

**Major changes since 1.0.0**

- `SlidingPaneLayout` now implements the [`Openable`](https://developer.android.com/reference/androidx/customview/widget/Openable) interface added in [CustomView `1.1.0`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0).

### Version 1.1.0-rc01

May 20, 2020

`androidx.slidingpanelayout:slidingpanelayout:1.1.0-rc01` is released with no changes since `1.1.0-beta01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..75f3faf4ff897611ef2e732ed0be0187917d797e/slidingpanelayout/slidingpanelayout)

### Version 1.1.0-beta01

April 1, 2020

`androidx.slidingpanelayout:slidingpanelayout:1.1.0-beta01` is released with no changes since `1.1.0-alpha01`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8744680798c115f612a99148c5a5c3ad4bd6fbf5..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/slidingpanelayout/slidingpanelayout)

### Version 1.1.0-alpha01

March 18, 2020

`androidx.slidingpanelayout:slidingpanelayout:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..8744680798c115f612a99148c5a5c3ad4bd6fbf5/slidingpanelayout/slidingpanelayout)

**API Changes**

- `SlidingPaneLayout` now implements the `Openable` interface added in [CustomView `1.1.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/customview#1.1.0-alpha02), mirroring the change in [DrawerLayout `1.1.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.0-alpha04). ([b/129979320](https://issuetracker.google.com/issues/129979320))