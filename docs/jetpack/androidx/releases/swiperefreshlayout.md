---
title: https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout
url: https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout
source: md.txt
---

# Swiperefreshlayout

# Swiperefreshlayout

[Code Sample](https://github.com/android/views-widgets-samples)  
API Reference  
[androidx.swiperefreshlayout.widget](https://developer.android.com/reference/kotlin/androidx/swiperefreshlayout/widget/package-summary)  
Implement the swipe-to-refresh UI pattern.  

|   Latest Update   |                                      Stable Release                                       |                                          Release Candidate                                          | Beta Release | Alpha Release |
|-------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------|---------------|
| November 19, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout#1.1.0) | [1.2.0-rc01](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout#1.2.0-rc01) | -            | -             |

## Declaring dependencies

To add a dependency on SwipeRefreshLayout, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.swiperefreshlayout:swiperefreshlayout:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460836+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460836&template=1422576)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2.0

### Version 1.2.0-rc01

November 19, 2025

`androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-rc01`is released. Version 1.2.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7344269b2d862d014a647efafcd7735f0d53f1da..bc967b3b2ff6a5f5047d4e14f4aedbbe49939161/swiperefreshlayout/swiperefreshlayout).

### Version 1.2.0-beta01

February 12, 2025

`androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-beta01`is released. Version 1.2.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..7344269b2d862d014a647efafcd7735f0d53f1da/swiperefreshlayout/swiperefreshlayout).

**API Changes**

- Specified nullability of`SwipeRefreshLayout`method parameters and return types ([I006d1](https://android-review.googlesource.com/#/q/I006d15100662ca77db65dd0cf4735c65cee84dfd),[b/236497776](https://issuetracker.google.com/issues/236497776))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf490](https://android-review.googlesource.com/#/q/Iaf49080833b450a7dbba982367bfd863a2ead6ad),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.2.0-alpha01

July 22, 2020

`androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6b97b146b743340c9d9b6fa54e735404374f2a5f..9f60cc700129e30cee9df020005c317fb39d32ec/swiperefreshlayout/swiperefreshlayout)

**Bug Fixes**

- `requestDisallowInterceptTouchEvent(boolean)`now honors the request like any other ViewGroup. While strongly discouraged, new behavior can be disabled with`setLegacyRequestDisallowInterceptTouchEventEnabled`. ([I968da](https://android-review.googlesource.com/#/q/I968da769d8400caf6f52c8a12595ee19fb4c0773),[b/141855018](https://issuetracker.google.com/issues/141855018))

## Version 1.1.0

### Version 1.1.0

June 24, 2020

`androidx.swiperefreshlayout:swiperefreshlayout:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6563b7854e79a3f7182efe27ee726867a091b603..6b97b146b743340c9d9b6fa54e735404374f2a5f/swiperefreshlayout/swiperefreshlayout)

**Major changes since 1.0.0**

- `SwipeRefreshLayout`now implements`NestedScrollingChild3`and`NestedScrollingParent3`.

### Version 1.1.0-rc01

April 15, 2020

`androidx.swiperefreshlayout:swiperefreshlayout:1.1.0-rc01`is released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..6563b7854e79a3f7182efe27ee726867a091b603/swiperefreshlayout/swiperefreshlayout)

### Version 1.1.0-beta01

March 4, 2020

`androidx.swiperefreshlayout:swiperefreshlayout:1.1.0-beta01`is released with no changes since`1.1.0-alpha03`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f14ad350142290622d1645e1d0e280cbe8ca4c2f..666ae665acfcfa2a20eccc18e4494808169742f4/swiperefreshlayout/swiperefreshlayout)

### Version 1.1.0-alpha03

October 9, 2019

`androidx.swiperefreshlayout:swiperefreshlayout:1.1.0-alpha03`is released.[Version 1.1.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a7b3cb32a2c7adac9b7af4bc2f996f1eb79fc12..f14ad350142290622d1645e1d0e280cbe8ca4c2f/swiperefreshlayout).

**New features**

- We have a new style attribute`R.styleable.SwipeRefreshLayout_swipeRefreshLayoutProgressSpinnerBackgroundColor`to set the background color of the progress indicator. ([aosp/931124](https://android-review.googlesource.com/931124))

**API changes**

- `requestDisallowInterceptTouchEvent(boolean)`now always propagates up to its parents. While strongly discouraged, new behavior can be disabled with`setLegacyRequestDisallowInterceptTouchEventEnabled`. ([aosp/1108540](https://android-review.googlesource.com/1108540))

**Bug fixes**

- Fixed issue with nested scrolling where SwipeRefreshLayout has a scrollable parent (e.g.[ViewPager2](https://developer.android.com/jetpack/androidx/releases/viewpager2)) and a scrollable child. ([b/138314213](https://issuetracker.google.com/issues/138314213))

### Version 1.1.0-alpha02

July 2, 2019

`androidx.swiperefreshlayout:swiperefreshlayout:1.1.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/d9ca300b3f70db75744a6d743f85e3784287434a..9a7b3cb32a2c7adac9b7af4bc2f996f1eb79fc12/swiperefreshlayout).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

**Bug fixes**

- Implemented saving and restoring of the refreshing state of SwipeRefreshLayout
- Fixed usability bug when SwipeRefreshLayout is embedded in a RecyclerView

### Version 1.1.0-alpha01

December 3, 2018

**API changes**

- [aosp/737631]():`SwipeRefreshLayout`now implements`NestedScrollingChild3`and`NestedScrollingParent3`, enabling nested scrolling 3 parents and children to pass consumed nested scrolling distance information through`SwipeRefreshLayout`. If developer code currently overrides`SwipeRefreshLayout.onNestedScroll(View, int, int, int, int, int)`, it will likely no longer be called and`SwipeRefreshLayout.onNestedScroll(View, int, int, int, int, int, int[])`should be overridden instead. Likewise,`SwipeRefreshLayout.dispatchNestedScroll(int, int, int, int, int[], int)`will likely no longer be called and`SwipeRefreshLayout.dispatchNestedScroll(int, int, int, int, int[], int, int[])`should be overridden instead.