---
title: https://developer.android.com/jetpack/androidx/releases/customview
url: https://developer.android.com/jetpack/androidx/releases/customview
source: md.txt
---

# Customview

API Reference  
[androidx.customview.poolingcontainer](https://developer.android.com/reference/kotlin/androidx/customview/poolingcontainer/package-summary)  
[androidx.customview.view](https://developer.android.com/reference/kotlin/androidx/customview/view/package-summary)  
[androidx.customview.widget](https://developer.android.com/reference/kotlin/androidx/customview/widget/package-summary)  
Implement custom views.  


This table lists all the artifacts in the `androidx.customview` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| customview | [1.2.0](https://developer.android.com/jetpack/androidx/releases/customview#customview-1.2.0) | - | - | - |
| customview-poolingcontainer | [1.1.0](https://developer.android.com/jetpack/androidx/releases/customview#customview-poolingcontainer-1.1.0) | - | - | - |

This library was last updated on: April 23, 2025

## Declaring dependencies

To add a dependency on CustomView, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.customview:customview:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.customview:customview:1.2.0")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460211+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460211&template=1422676)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Customview Poolingcontainer Version 1.0

### Version 1.1.0

April 23, 2025

`androidx.customview:customview-poolingcontainer:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e51950bd8170b033fd13ec8fd564c7a75b7c80c..d073ee0e2cf88cf636c1783942cee10ed2c479e3/customview/customview-poolingcontainer).

### Version 1.1.0-rc01

April 9, 2025

`androidx.customview:customview-poolingcontainer:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a1d6f16bd381db2059144d27701f7d079f417ef2..7e51950bd8170b033fd13ec8fd564c7a75b7c80c/customview/customview-poolingcontainer).

### Version 1.1.0-beta01

March 26, 2025

`androidx.customview:customview-poolingcontainer:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..a1d6f16bd381db2059144d27701f7d079f417ef2/customview/customview-poolingcontainer).

### Version 1.0.0

July 27, 2022

`androidx.customview:customview-poolingcontainer:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..1e0793130863c72dc4a2d02bc975128f3ef0158b/customview/customview-poolingcontainer)

**Major features of 1.0.0**

- Upgrading `RecyclerView` to `1.3.0-alpha02` or newer and Compose UI to `1.2.0-beta02` or newer will enable more performant reuse of `RecyclerView` children containing Compose views. See [this blog post](https://medium.com/androiddevelopers/jetpack-compose-interop-using-compose-in-a-recyclerview-569c7ec7a583) for more information.

- For most users, there is no need to use this library directly, unless you are developing a RecyclerView-like `ViewGroup` or a View that requires additional resources to be explicitly disposed when it is removed (like Compose).

### Version 1.0.0-rc01

June 15, 2022

`androidx.customview:customview-poolingcontainer:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..34fb17f767bcd64ac3bdd1f7ba6dda530791a9fe/)

- This version is identical to `androidx.customview:customview-poolingcontainer:1.0.0-beta02`.

### Version 1.0.0-beta02

May 18, 2022

`androidx.customview:customview-poolingcontainer:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/customview/customview-poolingcontainer)

- No changes, needed to support Compose 1.2.0-beta02 versions.

### Version 1.0.0-beta01

May 11, 2022

`androidx.customview:customview-poolingcontainer:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf/customview/customview-poolingcontainer)

**New Features**

- Improved documentation!

### Version 1.0.0-alpha01

March 23, 2022

`androidx.customview:customview-poolingcontainer:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868/customview/customview-poolingcontainer)

**Features in first release**

- The CustomView Poolingcontainer library contains utilities for listening to the lifecycle of containers that manage their child Views' lifecycle, such as RecyclerView.

## Version 1.2.0

### Version 1.2.0

April 23, 2025

`androidx.customview:customview:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e51950bd8170b033fd13ec8fd564c7a75b7c80c..d073ee0e2cf88cf636c1783942cee10ed2c479e3/customview/customview).

- There are no major commits just moving to stable version

### Version 1.2.0-rc01

April 9, 2025

`androidx.customview:customview:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a1d6f16bd381db2059144d27701f7d079f417ef2..7e51950bd8170b033fd13ec8fd564c7a75b7c80c/customview/customview).

### Version 1.2.0-beta01

March 26, 2025

`androidx.customview:customview:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..a1d6f16bd381db2059144d27701f7d079f417ef2/customview/customview).

**API Changes**

- An overload for `ViewDragHelper#smoothSlideViewTo` has been introduced, which accepts duration and interpolator parameters for animation speed control.

### Version 1.2.0-alpha02

September 21, 2022

`androidx.customview:customview:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/customview/customview)

**API Changes**

- Added `@NonNull` annotations to the `create()` methods of `ViewDragHelper`. ([I93a01](https://android-review.googlesource.com/#/q/I93a01188b3de024225e5e3bfd38094b420bfe46c), [b/236474222](https://issuetracker.google.com/issues/236474222))

### Version 1.2.0-alpha01

February 23, 2022

`androidx.customview:customview:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df8e8a74e8f656eb0ab5e4747da96f60bfe0fc89..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/customview/customview)

**New Features**

- Add a new `PoolingContainer` library that allows for listening to dispose events of a container that manages its children outside the View hierarchy. This will later be added as a dependency of `Compose` and `RecyclerView` ([I0e3f6](https://android-review.googlesource.com/#/q/I0e3f61f2a38f28a3fa9e5cbd50dbfb10c0871984), [b/196371929](https://issuetracker.google.com/issues/196371929))

**API Changes**

- Improved support for `AccessibilityNodeInfoCompat#setBoundsInScreen` in `ExploreByTouchHelper` and added `setBoundsInScreenFromBoundsInParent`, which can be used to translate parent bounds to screen bounds. ([Ie5529](https://android-review.googlesource.com/#/q/Ie5529b1b8ace40fab2040911553cbf8d98d13f90))

### Version 1.1.0

### Version 1.1.0

June 24, 2020

`androidx.customview:customview:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75f3faf4ff897611ef2e732ed0be0187917d797e..df8e8a74e8f656eb0ab5e4747da96f60bfe0fc89/customview/customview)

**Major changes since 1.0.0**

- Added a new [`Openable`](https://developer.android.com/reference/androidx/customview/widget/Openable) interface for layouts that can transition between an 'open' and 'closed' state.

### Version 1.1.0-rc01

May 20, 2020

`androidx.customview:customview:1.1.0-rc01` is released with no changes since `1.1.0-beta01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..75f3faf4ff897611ef2e732ed0be0187917d797e/customview/customview)

### Version 1.1.0-beta01

April 1, 2020

`androidx.customview:customview:1.1.0-beta01` is released with no changes since `1.1.0-alpha02`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/customview/customview)

### Version 1.1.0-alpha02

March 4, 2020

`androidx.customview:customview:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f464859d02d59b7975f89c519a9da51d9b8a41d9..666ae665acfcfa2a20eccc18e4494808169742f4/customview/customview)

**New Features**

- Added a new `Openable` interface for layouts that can transition between an 'open' and 'closed' state. `DrawerLayout` now implements this interface in [DrawerLayout `1.1.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.1.0-alpha04). ([b/129979320](https://issuetracker.google.com/issues/129979320))

### Version 1.1.0-alpha01

June 13, 2019

`androidx.customview:customview:1.1.0-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..f464859d02d59b7975f89c519a9da51d9b8a41d9/customview).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**API changes**

- Added new APIs to [ViewDragHelper](https://developer.android.com/reference/androidx/customview/widget/ViewDragHelper) to support changing its [edge size](https://developer.android.com/reference/androidx/customview/widget/ViewDragHelper#getEdgeSize())

**Bug fixes**

- Fixed some small bugs in `ExploreByTouchHelper` (([aosp/957741](https://android-review.googlesource.com/c/957741))