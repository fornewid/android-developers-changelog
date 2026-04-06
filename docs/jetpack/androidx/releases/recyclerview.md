---
title: https://developer.android.com/jetpack/androidx/releases/recyclerview
url: https://developer.android.com/jetpack/androidx/releases/recyclerview
source: md.txt
---

# Recyclerview

[User Guide](https://developer.android.com/guide/topics/ui/layout/recyclerview) [Code Sample](https://github.com/android/views-widgets-samples/tree/main/RecyclerView)  
API Reference  
[androidx.recyclerview.selection](https://developer.android.com/reference/kotlin/androidx/recyclerview/selection/package-summary)  
[androidx.recyclerview.widget](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/package-summary)  
Display large sets of data in your UI while minimizing memory usage.  


This table lists all the artifacts in the `androidx.recyclerview` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| recyclerview | [1.4.0](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.4.0) | - | - | - |
| recyclerview-selection | [1.2.0](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-selection-1.2.0) | - | - | [1.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-selection-1.3.0-alpha01) |

This library was last updated on: December 17, 2025

## Declaring dependencies

To add a dependency on RecyclerView, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.recyclerview:recyclerview:1.4.0"
    // For control over item selection of both touch and mouse driven selection
    implementation "androidx.recyclerview:recyclerview-selection:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.recyclerview:recyclerview:1.4.0")
    // For control over item selection of both touch and mouse driven selection
    implementation("androidx.recyclerview:recyclerview-selection:1.2.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460887+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460887&template=1422600)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.4

### Version 1.4.0

January 15, 2025

`androidx.recyclerview:recyclerview:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dfd74da8dfb752e0d0981903430e71ecb70097e1..513dc1f3ad435066bf1a73aa6eb8d3528f607dca/recyclerview/recyclerview).

**Important changes since RecyclerView 1.3.2**

- `Adaptive` refresh rate support: `RecyclerView` now calls `setFrameContentVelocity` when it is scrolling via `OverScroller` (such as settling from a fling or smooth scroll). ([I8f8a4](https://android.googlesource.com/platform/frameworks/support/+/a1e9ab3e5fd52e885731bd762ff7dd4a64b25505))

### Version 1.4.0-rc01

September 18, 2024

`androidx.recyclerview:recyclerview:1.4.0-rc01` is released, with no changes since [1.4.0-alpha02](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.4.0-alpha02)/. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..dfd74da8dfb752e0d0981903430e71ecb70097e1/recyclerview/recyclerview).

### Changes since 1.3.2

**Compatibility note**: This version will only compile against the API 35 (Vanilla Ice Cream) SDK or higher. If you see AGP (Android Gradle Plugin) warnings when you upgrade, you can suppress them.

**New Features**

- `Adaptive` refresh rate support: `RecyclerView` now calls `setFrameContentVelocity` when it is scrolling via `OverScroller` (such as settling from a fling or smooth scroll). ([I8f8a4](https://android.googlesource.com/platform/frameworks/support/+/a1e9ab3e5fd52e885731bd762ff7dd4a64b25505))

**API Changes**

- Add `RecyclerView$LayoutManager#isLayoutReversed` API. ([I4970e](https://android-review.googlesource.com/#/q/I4970ed9322cf3786377e847be6e22400cbd5c2e2))

**Other changes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Add item view type to `RecyclerView` bind/create trace sections, and label RV prefetches as 'forced - needed next frame' if they are expected to be used by the next frame, and thus should start work as soon as possible. ([I8ec3e](https://android-review.googlesource.com/#/q/I8ec3edb569d892fcb100c86e401d95a32e844d29), [b/309523615](https://issuetracker.google.com/issues/309523615))
- Update `compileSdk` to 35 (see "Compatibility note" above for details). [5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f)

### Version 1.4.0-beta01

August 21, 2024

`androidx.recyclerview:recyclerview:1.4.0-beta01` is released, with no changes since [1.4.0-alpha02](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.4.0-alpha02). Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..8c4071562bd7e22b937284d71fb7aca9c4cd662c/recyclerview/recyclerview).

**Compatibility note**: This version will only compile against the API 35 (Vanilla Ice Cream) SDK or higher. If you see AGP (Android Gradle Plugin) warnings when you upgrade, you can suppress them.

### Version 1.4.0-alpha02

August 7, 2024

`androidx.recyclerview:recyclerview:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..9130b719318a69f2f3eaf82c32b131232fd721cb/recyclerview/recyclerview).

**Compatibility note**: This version will only compile against the API 35 (Vanilla Ice Cream) SDK or higher. If you see AGP (Android Gradle Plugin) warnings when you upgrade, you can suppress them.

**New Features**

- Variable refresh rate support: RecyclerView now calls `setFrameContentVelocity` when it is scrolling via OverScroller (such as settling from a fling or smooth scroll). ([I8f8a4](https://android.googlesource.com/platform/frameworks/support/+/a1e9ab3e5fd52e885731bd762ff7dd4a64b25505))

**API Changes**

- Deprecated `ViewCompat.LAYOUT_DIRECTION_` APIs ([I51710](https://android-review.googlesource.com/#/q/I5171051c40ebe77a9ac6690abfe18810d794d99d), [b/317055535](https://issuetracker.google.com/issues/317055535))
- Add `RecyclerView$LayoutManager#isLayoutReversed` API. ([I4970e](https://android-review.googlesource.com/#/q/I4970ed9322cf3786377e847be6e22400cbd5c2e2))

**Other changes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Add item view type to `RecyclerView` bind/create trace sections, and label RV prefetches as 'forced - needed next frame' if they are expected to be used by the next frame, and thus should start work as soon as possible. ([I8ec3e](https://android-review.googlesource.com/#/q/I8ec3edb569d892fcb100c86e401d95a32e844d29), [b/309523615](https://issuetracker.google.com/issues/309523615))
- Update `compileSdk` to 35 (see "Compatibility note" above for details). [5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f)

**External Contribution**

- `GestureDetectorCompat` is now deprecated as `GestureDetector` is available from the `minSdk`. ([Icc4cd](https://android-review.googlesource.com/#/q/Icc4cd9df0b358863ac36d059dc6b997775321be6))

### Version 1.4.0-alpha01

October 18, 2023

`androidx.recyclerview:recyclerview:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/68f4660cd40b87c9383c5c7d86ae26ebccbf93e8..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/recyclerview/recyclerview)

**API Changes**

- Add `RecyclerView$LayoutManager#isLayoutReversed` API. ([I4970e](https://android-review.googlesource.com/#/q/I4970ed9322cf3786377e847be6e22400cbd5c2e2))

**Bug Fixes**

- Fix a bug causing sporadic crashes during animations ([I42f22b](https://android-review.googlesource.com/c/platform/frameworks/support/+/2672255)) (also included in 1.3.2)

## Version 1.3.2

### Version 1.3.2

October 18, 2023

`androidx.recyclerview:recyclerview:1.3.2` is released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/68f4660cd40b87c9383c5c7d86ae26ebccbf93e8..053c71e9fde5883b9033ee934e438bddc9c5a4ba/recyclerview/recyclerview)

**Bug Fixes**

- Fix a bug causing sporadic crashes during animations. ([I42f22b](https://android-review.googlesource.com/c/platform/frameworks/support/+/2672255))

## Version 1.3.1

### Version 1.3.1

July 26, 2023

`androidx.recyclerview:recyclerview:1.3.1` is released, with no changes since 1.3.1-rc01. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cd515272c151a7851eea51323c2dfcfa238a91fc..68f4660cd40b87c9383c5c7d86ae26ebccbf93e8/recyclerview/recyclerview)

For release notes of previous release, refer to our [Release Notes page](https://developer.android.com/jetpack/androidx/releases/recyclerview)

### Version 1.3.1-rc01

May 24, 2023

`androidx.recyclerview:recyclerview:1.3.1-rc01` is released. [Version 1.3.1-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86bf1b167c3ff33791a75eb42b0c8f056eaeab3e..cd515272c151a7851eea51323c2dfcfa238a91fc/recyclerview/recyclerview)

**Users of ViewPager2 must update to at least 1.1.0-beta02** when updating to this version of `RecyclerView` to avoid crashes.

**API Changes**

- Add new `setDebugAssertionsEnabled` and `setVerboseLoggingEnabled` methods that can aid in debugging `RecyclerView`-related issues in apps. ([I514b9](https://android-review.googlesource.com/c/platform/frameworks/support/+/2414514))

**Bug Fixes**

- Fix crashes for users of `ViewTreeLifecycleOwner` (including `ComposeView`) by temporarily re-attaching temporarily detached views when calling `onBind`. ([I7244f2c](https://android-review.googlesource.com/c/platform/frameworks/support/+/2366713), [b/265347515](https://issuetracker.google.com/265347515), [b/283288295](https://issuetracker.google.com/283288295))

## Version 1.3.0

### Version 1.3.0

March 8, 2023

`androidx.recyclerview:recyclerview:1.3.0` is released, with no changes since 1.3.0-rc01. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/540407bb72d3a01a8c1a1ea74de7e878d6094c7d..86bf1b167c3ff33791a75eb42b0c8f056eaeab3e/recyclerview/recyclerview)

**Important changes since 1.2.0**

- This release contains performance improvements (previously included in [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.3.0-alpha02) and [1.3.0-beta01](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.3.0-beta01)) when used with Jetpack Compose. If you are using Compose `1.2.0-beta02` or higher and were using the `MyComposeAdapter` and `DisposeOnViewTreeLifecycleDestroyed` `ViewCompositionStrategy` described in the previous interoperability guidelines, **you should remove these**, as they are no longer an improvement over the default state.
- New `ConcatAdapter.getWrappedAdapterAndPosition` method added to allow for retrieving wrapped adapter information in situations where you don't have a `ViewHolder`, such as a `SpanSizeLookup` ([I2bd4c](https://android-review.googlesource.com/#/q/I2bd4c99ee4417f0b3ed74d471ed732af24a2d1b3), [b/191543920](https://issuetracker.google.com/issues/191543920))

### Version 1.3.0-rc01

September 21, 2022

`androidx.recyclerview:recyclerview:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..1f3431c35948f75144d7af7d5c509860703ad91b/recyclerview/recyclerview)

- No changes since last release

### Version 1.3.0-beta02

August 10, 2022

`androidx.recyclerview:recyclerview:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f4522bf56248429cc9c58204b6fc724f6d51687..bea814b246f89ff7244e3c6b0648f0b57e47897c/recyclerview/recyclerview)

**API Changes**

- Removed nullability annotations added in 1.3.0-beta01 due to the fact that they represented a significant source-incompatible change for Kotlin users ([I7a258](https://android-review.googlesource.com/#/q/I7a25874d17e40de21c6bd2f50192c79746d6b7e5),[I1557e6](https://android-review.googlesource.com/c/platform/frameworks/support/+/2171631),[I8db76](https://android-review.googlesource.com/#/q/I8db7687f652539c6ee5c0be8410dac45fb244f29))

### Version 1.3.0-beta01

June 29, 2022

`androidx.recyclerview:recyclerview:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..6f4522bf56248429cc9c58204b6fc724f6d51687/recyclerview/recyclerview)

**New Features**

- This beta release contains performance improvements (previously included in [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/recyclerview#recyclerview-1.3.0-alpha02) when used with Jetpack Compose. If you are using Compose `1.2.0-beta02` or higher and were using the `MyComposeAdapter` and `DisposeOnViewTreeLifecycleDestroyed` `ViewCompositionStrategy` described in the previous interoperability guidelines, **you should remove these**, as they are no longer an improvement over the default state.

**API Changes**

- Added nullability annotations for a number of methods and parameters to improve lint warnings for Java users and interoperability for Kotlin users. This may be a source-breaking change for some Kotlin users and result in additional lint warnings/errors for some Java users. ([I61829](https://android-review.googlesource.com/#/q/I618295d8762376c078dbff1e844d0d7958259e97), [b/236487044](https://issuetracker.google.com/issues/236487044); [Ia0b6f](https://android-review.googlesource.com/#/q/Ia0b6fc9740bcc96a9b2780c9c4b722981a7426ac); [I6f119](https://android-review.googlesource.com/#/q/I6f11942c06ace4fe2deba6010f1133014de01eca), [b/236487209](https://issuetracker.google.com/issues/236487209); [Ibe1de](https://android-review.googlesource.com/#/q/Ibe1deecd4feb1371c6d231cc1967c97b51ba2c1a), [b/236487210](https://issuetracker.google.com/issues/236487210))

**Bug Fixes**

- Ensure grids are treated as grids by a11y services by setting an a11y node info class name. ([I12812](https://android-review.googlesource.com/#/q/I128122352a3fc4898cc6ba76d7da8166519bd648))

### Version 1.3.0-alpha02

April 6, 2022

`androidx.recyclerview:recyclerview:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/recyclerview/recyclerview)

**API Changes**

- Adds experimental `BuildCompat` methods for future SDKs ([Iafd82](https://android-review.googlesource.com/#/q/Iafd82e20e0c6d54878d352baddb18e86095504a7), [b/207528937](https://issuetracker.google.com/issues/207528937))
- New `ConcatAdapter.getWrappedAdapterAndPosition` method added to allow for retrieving wrapped adapter information in situations where you don't have a ViewHolder, such as a `SpanSizeLookup` ([I2bd4c](https://android-review.googlesource.com/#/q/I2bd4c99ee4417f0b3ed74d471ed732af24a2d1b3), [b/191543920](https://issuetracker.google.com/issues/191543920))

**Bug Fixes**

- Integration with the new AndroidX PoolingContainer library ([Ib89d2](https://android-review.googlesource.com/#/q/Ib89d2ecf78a27bda3786734aabd0c23fdba9a7a8))
- Adjusts the scroll distance for accessibility action ([If74ae](https://android-review.googlesource.com/#/q/If74ae6f6d204f2b238998a31154abf61f8167d11))

### Version 1.3.0-alpha01

September 15, 2021

`androidx.recyclerview:recyclerview:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/540407bb72d3a01a8c1a1ea74de7e878d6094c7d..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/recyclerview/recyclerview)

**New Features**

- Added support for stretch overscroll RecyclerView. ([Iab877](https://android.googlesource.com/platform/frameworks/support/+/4a1e1cf8a231240732d8323bed277870bca33d53))

## RecyclerView-Selection Version 1.3.0

### Version 1.3.0-alpha01

December 17, 2025

`androidx.recyclerview:recyclerview-selection:1.3.0-alpha01` is released. Version 1.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a54c887072ebcf6798d5a7e7ef3efed99b04e77..ec985eed3cba8444e5aaa52a748333397a1298f3/recyclerview/recyclerview-selection).

**API Changes**

- Let in-selection-hotspot clear existing selection ([I0eae7](https://android-review.googlesource.com/#/q/I0eae7dca16cbddb795dd8b730105e643fa6fb796), [b/389814214](https://issuetracker.google.com/issues/389814214)) This gives developers greater control over, when tapping or clicking on a `RecyclerView` to select an item, whether any other already-selected items stay selected or are deselected.

## RecyclerView-Selection Version 1.2.0

### Version 1.2.0

May 20, 2025

`androidx.recyclerview:recyclerview-selection:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d771fbb0d3b9774c2513f1f7244f17b0c96735f..6a54c887072ebcf6798d5a7e7ef3efed99b04e77/recyclerview/recyclerview-selection).

**Important changes since 1.1.0**

- Fix small mouse moves turning clicks into drags.
- Fix an issue where key/position mapping in KeyProvider was lost while entry was not yet recycled.

### Version 1.2.0-rc01

May 7, 2025

`androidx.recyclerview:recyclerview-selection:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b22977a837281f01683d3fa7c8703e97de2518a4..2d771fbb0d3b9774c2513f1f7244f17b0c96735f/recyclerview/recyclerview-selection).

**Bug Fixes**

- Fix small mouse moves turning clicks into drags. ([Ie9106](https://android-review.googlesource.com/#/q/Ie91064a473e28247ebc23fe370791f74b146ccd4))

### Version 1.2.0-beta01

April 9, 2025

`androidx.recyclerview:recyclerview-selection:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..b22977a837281f01683d3fa7c8703e97de2518a4/recyclerview/recyclerview-selection).

**API Changes**

- Deprecated `ViewCompat.LAYOUT_DIRECTION_` APIs ([I51710](https://android-review.googlesource.com/#/q/I5171051c40ebe77a9ac6690abfe18810d794d99d), [b/317055535](https://issuetracker.google.com/issues/317055535))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I03b80](https://android-review.googlesource.com/#/q/I03b80dbabc45393ade3436280e82f17ee050b9b7), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.2.0-alpha01

May 5, 2021

`androidx.recyclerview:recyclerview-selection:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/563bff8d5f42c831ddfa3a732ad82d97d0c60d99..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/recyclerview/recyclerview-selection)

**Bug Fixes**

- Fix an issue where key/position mapping in KeyProvider was lost while entry was not yet recycled. ([b/145767095](https://issuetracker.google.com/issues/145767095))

## Version 1.2.1

### Version 1.2.1

June 2, 2021

`androidx.recyclerview:recyclerview:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b3d7374d6ecfb818209fece439350ab44d44db1a..540407bb72d3a01a8c1a1ea74de7e878d6094c7d/recyclerview/recyclerview)

**Bug Fixes**

- `ViewHolder`s inside a `ConcatAdapter` now return the correct adapter position when queried in `onViewRecycled` callback. ([b/187339376](https://issuetracker.google.com/issues/187339376))

## Version 1.2.0

### Version 1.2.0

April 7, 2021

`androidx.recyclerview:recyclerview:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/28a2b25e799c715db874d822a8c4197a249698cb..b3d7374d6ecfb818209fece439350ab44d44db1a/recyclerview/recyclerview)

**Major changes since 1.1.0**

**ConcatAdapter** : This new adapter allows you to easily concatenate multiple Adapters on the same RecyclerView. See the [blog post](https://medium.com/androiddevelopers/merge-adapters-sequentially-with-mergeadapter-294d2942127a) for more information.

- As part of this change, [`ViewHolder.getAdapterPosition`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder#getAdapterPosition()) is deprecated and replaced with two new methods:
  - [getBindingAdapterPosition](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder#getBindingAdapterPosition()) returns the position relative to the Adapter which bound that item.
  - [getAbsoluteAdapterPosition](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder#getAbsoluteAdapterPosition()) returns the position relative to the whole RecyclerView.

**Lazy State Restoration** : RecyclerView Adapter can now delay state restoration until its contents are loaded. See the [documentation](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter#setstaterestorationpolicy) for more details.

### Version 1.2.0-rc01

March 24, 2021

`androidx.recyclerview:recyclerview:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..28a2b25e799c715db874d822a8c4197a249698cb/recyclerview/recyclerview)

**Bug Fixes**

- `ConcatAdapter.Config.Builder` now has default values that match `Config.DEFAULT` ([b/157169835](https://issuetracker.google.com/issues/157169835))

### Version 1.2.0-beta02

February 24, 2021

`androidx.recyclerview:recyclerview:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..5c90131a69042a6a3e13952e1da9e7ffc571c31d/recyclerview/recyclerview)

**Bug Fixes**

- Fixed issue where top padding was causing the right overscroll glow to move upward into the padded area, instead of downward in order to respect the padding. ([I6b61d](https://android-review.googlesource.com/#/q/I6b61d12af161feb1b84a9906f015d9a3edf0ef93), [b/118399122](https://issuetracker.google.com/issues/118399122))

### Version 1.2.0-beta01

December 2, 2020

`androidx.recyclerview:recyclerview:1.2.0-beta01` is released with no change since `1.2.0-alpha06`. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d49666a20b830dcb9d6cc82517eac86daea88d7..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/recyclerview/recyclerview)

### Version 1.2.0-alpha06

October 1, 2020

`androidx.recyclerview:recyclerview:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..3d49666a20b830dcb9d6cc82517eac86daea88d7/recyclerview/recyclerview)

**New Features**

- Added support for adding multiple RecyclerListeners. ([I70ad8](https://android-review.googlesource.com/#/q/I70ad8f9bcf25c2c00fbf5f71d5a991287bef1606), [b/145767095](https://issuetracker.google.com/issues/145767095))

**API Changes**

- Deprecated RecyclerView.setRecyclerListener(RecyclerListener). ([I70ad8](https://android-review.googlesource.com/#/q/I70ad8f9bcf25c2c00fbf5f71d5a991287bef1606), [b/145767095](https://issuetracker.google.com/issues/145767095))

### Version 1.2.0-alpha05

July 22, 2020

`androidx.recyclerview:recyclerview:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/recyclerview/recyclerview)

**Bug Fixes**

- Fixed issue where if an RecyclerView only has one item and it is focused, focusing forward or backwards will not move focus. ([6f36b3](https://android.googlesource.com/platform/frameworks/support/+/6f36b39c9163e9404cfd5b5f7937ad81f2db345a))
- Fixed an `ArrayIndexOutOfBoundsException` in `StaggeredGridLayoutManager` ([49b601](https://android.googlesource.com/platform/frameworks/support/+/49b601979ebccb8fcc6b8d670b79ae1c5f818dbf), [b/122303625](https://issuetracker.google.com/issues/122303625), [b/74877618](https://issuetracker.google.com/issues/74877618), [b/160193663](https://issuetracker.google.com/issues/160193663), [b/37086625](https://issuetracker.google.com/issues/37086625))
- Fixed a measurement bug where under specific circumstances, RecyclerView would inappropriately end up not showing it's children. ([89040c](https://android.googlesource.com/platform/frameworks/support/+/89040cd6e69bac6bed840934adf5dab295e022ea), [b/138734786](https://issuetracker.google.com/issues/122303625))

**External Contributions**

- Thanks to Kolin Krewinkel on behalf of Facebook for the [contribution](https://android.googlesource.com/platform/frameworks/support/+/49b601979ebccb8fcc6b8d670b79ae1c5f818dbf)!

### Version 1.2.0-alpha04

June 24, 2020

`androidx.recyclerview:recyclerview:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/recyclerview/recyclerview)

**API Changes**

- `MergeAdapter` has been renamed to `ConcatAdapter` to avoid any confusion with different data merging behaviors ([c0540c](https://android.googlesource.com/platform/frameworks/support/+/c0540c10cc7ea5027d3fc3b22024de7e66c41a9d), [b/158019211](https://issuetracker.google.com/issues/158019211)).

**Bug Fixes**

- Improvements to automatic scrolling when all visible items are removed ([fe8670](https://android.googlesource.com/platform/frameworks/support/+/fe867028214a364167c893083065eddcd709e223), [b/154124815](https://issuetracker.google.com/issues/154124815))

### Version 1.2.0-alpha03

April 29, 2020

`androidx.recyclerview:recyclerview:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..b752a10305d7cd58a7f50ad094ed54af4d765f27/recyclerview/recyclerview)

**New Features**

- RecyclerView now has a `nestedScrollBy` method that allows programmatic scrolling that cooperates with nested scrolling: ([Ibaa58](https://android-review.googlesource.com/#/q/Ibaa58076fb521bc75b16f071b426038c1d2b59b5))

### Version 1.2.0-alpha02

April 1, 2020

`androidx.recyclerview:recyclerview:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/740cde70237dd276f8ad66dfe9528b1cdb5d54bb..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/recyclerview/recyclerview)

This and higher versions of RecyclerView are not compatible with lower versions of ViewPager2. If you are currently using `androidx.viewpager2:viewpager2:1.0.0` or lower, make sure to update to [`androidx.viewpager2:viewpager2:1.1.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/viewpager2#1.1.0-alpha01).

**New Features**

- **MergeAdapter**

  - [MergeAdapter](https://developer.android.com/reference/androidx/recyclerview/widget/MergeAdapter): A new RecyclerView Adapter that can combine multiple adapters linearly.

      MyAdapter adapter1 = ...;
      AnotherAdapter adapter2 = ...;
      MergeAdapter merged = new MergeAdapter(adapter1, adapter2);
      recyclerView.setAdapter(mergedAdapter);

  For the sample above, MergeAdapter will present items from `adapter1` followed by `adapter2`.
- **`RecyclerView.Adapter` lazy state restoration**:

  - Added a new API to the `RecyclerView.Adapter` class which allows Adapter to control when the layout state should be restored.

  - For example, you can call:

      myAdapter.setStateRestorationStrategy(StateRestorationStrategy.WHEN_NOT_EMPTY);

  to make RecyclerView wait until Adapter is not empty before restoring the scroll position.
- **CollectionInfo and CollectionItemInfo will no longer be populated by default.**

  - If you would like Accessibility Services (Talkback for example) to continue indicating count and item index to the user, you will need to populate CollectionInfo and CollectionItemInfo yourself.

  - These objects are no longer populated in the framework because the framework can't determine the count of items as perceived by the user (such as separators, headers, or RecyclerView items that represent multiple perceived items).

**Bug Fixes**

- RecyclerView now avoids anchoring on Views outside the viewport when the viewport size has changed
- Fixed a bug in DiffUtil where it might compute the diff wrong when an original item in the first list is duplicated multiple times in the second list. ([b/123376278](https://issuetracker.google.com/issues/123376278))

### Version 1.2.0-alpha01

December 18, 2019

`androidx.recyclerview:recyclerview:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/63bf356b1e1c722539dc8768f5cfe991a23c517a..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/recyclerview/recyclerview).

**Bug fixes**

- Fixed minor issues with FastScroller related to RTL drawing and touch accuracy ([b/143789932](https://issuetracker.google.com/issues/143789932), [aosp/1130438](https://android-review.googlesource.com/c/1130438))
- Fixed crash in ItemTouchHelper when removed from RecyclerView while ItemTouchHelper animations are running ([b/140447176](https://issuetracker.google.com/issues/140447176), [aosp/1167575](https://android-review.googlesource.com/c/1167575))

## Version 1.1.0

### Version 1.1.0

November 20, 2019

`androidx.recyclerview:recyclerview:1.1.0` is released. [Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b4450eea34b0f7f4c6a46b25e2ffb1cfcaef2966..63bf356b1e1c722539dc8768f5cfe991a23c517a/recyclerview/recyclerview).

**Important changes since 1.0.0**

- `PagerSnapHelper` and `LinearSnapHelper` now take padding of RecyclerView into account regardless of the value of `clipToPadding` ([b/139452422](https://issuetracker.google.com/139452422), [b/139012032](https://issuetracker.google.com/139012032), [aosp/1103182](https://android-review.googlesource.com/c/1103182), [aosp/1106715](https://android-review.googlesource.com/c/1106715), [aosp/1130728](https://android-review.googlesource.com/c/1130728))
- `RecyclerView.setLayoutTransition(LayoutTransition)` is formally deprecated and will throw an `IllegalArgumentException` when called with a non null value. Use `RecyclerView.setItemAnimator(ItemAnimator)` instead. ([aosp/839414](https://android-review.googlesource.com/c/839414))
- [aosp/723649](https://android-review.googlesource.com/c/723649): RecyclerView now implements `NestedScrollingChild3`, enabling it to be informed of when all its nested scrolling parents have stopped consuming nested scrolling distances. If developer code currently overrides `RecyclerView.onNestedScroll(View, int, int, int, int, int)`, it will likely no longer be called and `RecyclerView.onNestedScroll(View, int, int, int, int, int, int[])` should be overridden instead.
- RecyclerView now has a default style attribute: `recyclerViewStyle`, which allows setting of the default style in your theme
- ViewCompat accessibility actions API no longer breaks RecyclerView ItemDelegate.
- `LinearLayoutManager.calculateExtraLayoutSpace(RecyclerView.State, int[])` can be overridden to customize how much extra layout space should be added to either side of the associated RecyclerView. ([aosp/931259](https://android-review.googlesource.com/c/931259))
- Added a new overload of smoothScrollBy: `RecyclerView#smoothScrollBy(@Px int, @Px int, @Nullable Interpolator, int duration)`, that allows you to specify a duration in milliseconds for how long the animation should take. ([aosp/952807](https://android-review.googlesource.com/c/952807))

### Version 1.1.0-rc01

October 23, 2019

`androidx.recyclerview:recyclerview:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/7cf80b101a4e9ee0fa66337dd7528f7b5d670c78..b4450eea34b0f7f4c6a46b25e2ffb1cfcaef2966/recyclerview/recyclerview).

**Bug fixes**

- Fixed an "Application Not Responding" when overriding `RecyclerViewAccessibilityDelegate.ItemDelegate` ([aosp/1138057](https://android-review.googlesource.com/c/platform/frameworks/support/+/1138057/), [aosp/1133434](https://android-review.googlesource.com/c/platform/frameworks/support/+/1133434/))

### Version 1.1.0-beta05

October 9, 2019

`androidx.recyclerview:recyclerview:1.1.0-beta05` is released. [Version 1.1.0-beta05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/9c00f40057f472c088c53de0c23937c02c9b64fc..7cf80b101a4e9ee0fa66337dd7528f7b5d670c78/recyclerview/recyclerview).

**API changes**

- Following up on [aosp/1106715](https://android-review.googlesource.com/c/1106715) and [aosp/1103182](https://android-review.googlesource.com/c/1103182), now LinearSnapHelper and PagerSnapHelper will return the view that is in the center of the RecyclerView's bounds, minus padding, despite the value of clipToPadding. ([aosp/1130728](https://android-review.googlesource.com/c/1130728))

**Bug fixes**

- Fixed an issue where RecyclerView was generating duplicate accessibility nodes for children of RecyclerView. ([aosp/1130618](https://android-review.googlesource.com/c/1130618))
- Fixed an issue where Virtual Accessibility Hierarchies in RecyclerViews didn't work.
- Fixed an issue where custom ItemDelegates weren't used.

### Version 1.1.0-beta04

September 5, 2019

`androidx.recyclerview:recyclerview:1.1.0-beta04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/1bd267a0d9317f3a8698ecc2b739d48a8805ca87..9c00f40057f472c088c53de0c23937c02c9b64fc/recyclerview/recyclerview).

**Bug fixes**

- `PagerSnapHelper` and `LinearSnapHelper` now take padding of RecyclerView into account regardless of the value of `clipToPadding` ([b/139452422](https://issuetracker.google.com/139452422), [b/139012032](https://issuetracker.google.com/139012032), [aosp/1103182](https://android-review.googlesource.com/1103182), [aosp/1106715](https://android-review.googlesource.com/1106715))
- Fixed a bug where RecyclerView was not disallowing touch intercept when nested pre-scrolling caused a `NestedScrollingParent` to scroll ([b/138668210](https://issuetracker.google.com/138668210), [aosp/1105373](https://android-review.googlesource.com/1105373)). This benefits libraries such as [ViewPager2](https://developer.android.com/jetpack/androidx/releases/viewpager2).
- RecyclerView now consistently goes to `SCROLL_STATE_DRAGGING` before nested pre scrolls are dispatched ([aosp/1105373](https://android-review.googlesource.com/1105373))
- Nested pre-scrolling is no longer performed before the gesture exceeds touch slop ([b/139530818](https://issuetracker.google.com/139530818), [aosp/1105373](https://android-review.googlesource.com/1105373))
- `dx` and `dy` arguments dispatched to nested pre-scrolls are zeroed when RecyclerView can't scroll in that direction ([aosp/1105373](https://android-review.googlesource.com/1105373))

### Version 1.1.0-beta03

August 15, 2019

`androidx.recyclerview:recyclerview:1.1.0-beta03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d43bc74d94460f3571f2ebf6a9b327c9a83441d3..1bd267a0d9317f3a8698ecc2b739d48a8805ca87/recyclerview/recyclerview).

**API changes**

- RecyclerView now dispatches scroll distances via `View.onScrollChanged(int l, int t, int oldl, int oldt)` such that accessibility services are notified about scroll changes accurately. ([aosp/1007823](https://android-review.googlesource.com/c/platform/frameworks/support/+/1007823))

**Bug fixes**

- Fixed a major bug stack overflow bug related to RecyclerView and accessibility. ([aosp/1099577](https://android-review.googlesource.com/c/platform/frameworks/support/+/1099577))

### Version 1.1.0-beta02

August 7, 2019

`androidx.recyclerview:recyclerview:1.1.0-beta02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/ac1bdc42de0ec27ad22ee33f04deb8772fccacf6..ece690f1fdb4481b47c5128fd21d88da7d6850a6/recyclerview/recyclerview).

**New features**

- RecyclerView now has a default style attribute: `recyclerViewStyle`, which allows setting of the default style in your theme

**Bug fixes**

- Fixed a bug where RecyclerView was not disallowing touch intercept when scrolling it caused a NestedScrollingParent to scroll. ([b/131115697](https://issuetracker.google.com/issues/131115697), [aosp/1055911](https://android-review.googlesource.com/c/1055911/))

### Version 1.1.0-beta01

July 2, 2019

`androidx.recyclerview:recyclerview:1.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0c2a7091f663f8e853290ecb2a84c08fc7adac86..ac1bdc42de0ec27ad22ee33f04deb8772fccacf6/recyclerview).

**New features**

- `RecyclerView` now participates in nested scrolling when a scroll is initiated via accessibility events. ([aosp/973584](https://android-review.googlesource.com/973584))

### Version 1.1.0-alpha06

June 5, 2019

`androidx.recyclerview:recyclerview:1.1.0-alpha06` and `androidx.recyclerview:recyclerview-selection:1.1.0-alpha06` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a546ca859408ae97792539219c423031cca32392..0c2a7091f663f8e853290ecb2a84c08fc7adac86/recyclerview).

**New features**

- Added a new overload of smoothScrollBy: `RecyclerView#smoothScrollBy(@Px int, @Px int, @Nullable Interpolator, int duration)`, that allows you to specify a duration in milliseconds for how long the animation should take. ([aosp/952807](https://android-review.googlesource.com/c/platform/frameworks/support/+/952807/))

**API changes**

- `GridLayoutManager` and `StaggeredGridLayoutManager` no longer automatically label full span items as headers for accessibility purposes ([aosp/969703](https://android-review.googlesource.com/c/platform/frameworks/support/+/969703/))
- Preserve order of selection (by creation time) in `recyclerview-selection` ([aosp/937279](https://android-review.googlesource.com/c/platform/frameworks/support/+/937279/))

**Bug fixes**

- Fixed a bug where `RecyclerView` was flinging with incorrect velocities while in a nested scrolling situation. ([aosp/961642](https://android-review.googlesource.com/c/platform/frameworks/support/+/961642))
- Added stability improvements to `recyclerview-selection` ([aosp/960213](https://android-review.googlesource.com/c/platform/frameworks/support/+/960213), [aosp/926296](https://android-review.googlesource.com/c/platform/frameworks/support/+/926296))

### Version 1.1.0-alpha05

May 7, 2019

`androidx.recyclerview:recyclerview:1.1.0-alpha05` and `androidx.recyclerview:recyclerview-selection:1.1.0-alpha05` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/162c15eca5b62edc19734a7c502e5f94a936411c..a546ca859408ae97792539219c423031cca32392/recyclerview).

**New features**

- `LinearLayoutManager.calculateExtraLayoutSpace(RecyclerView.State, int[])` can be overridden to customize how much extra layout space should be added to either side of the associated RecyclerView. ([aosp/931259](https://android-review.googlesource.com/c/931259/))

**API changes**

- Add API to retrieve `DividerItemDecoration` drawable ([aosp/937282](https://android-review.googlesource.com/c/937282/))
- Deprecate `LinearLayout.getExtraLayoutSpace(RecyclerVew.State)` in favor of a new mechanism that allows to have custom extra layout space on both sides. The new method is `LinearLayout.calculateExtraLayoutSpace(RecyclerView.state, int[])` ([aosp/931259](https://android-review.googlesource.com/c/931259/))

**Bug fixes**

- Cleaned up Gesture selection ([aosp/940781](https://android-review.googlesource.com/c/940781/))
- Preserve order of selection (by creation time) ([b/128455535](https://issuetracker.google.com/issues/128455535))

### Version 1.1.0-alpha04

April 3rd, 2019

`androidx.recyclerview:recyclerview:1.1.0-alpha04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/333a979ce2f308bf7b78f80e684e1d787fb8c6dd..162c15eca5b62edc19734a7c502e5f94a936411c/recyclerview).

**Bug fixes**

- RV OnItemTouchListener's previously couldn't intercept on ACTION_UP, preventing OnItemTouchListener's from blocking other code from responding to ACTION_UP. This is now fixed: ([aosp/916137](https://android-review.googlesource.com/c/916137/))

### Version 1.1.0-alpha03

March 13th, 2019

`androidx.recyclerview:recyclerview:1.1.0-alpha03` is released. The full list of commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/871963fd9c70c32aa57a2587530654ac1c7595bb..333a979ce2f308bf7b78f80e684e1d787fb8c6dd/recyclerview).

**New features**

- `GridLayoutManager`: Opt in, higher resolution `GridLayoutManager` scroll bar dimension estimation ([aosp/838836](https://android-review.googlesource.com/c/838836/)):
  - Uses span information to estimate scroll bar dimensions for a `GridLayoutManager`.
  - To enable, call `GridLayoutManager#setUsingSpansToEstimateScrollbarDimensions(boolean)` passing in true.
  - See the documentation on `GridLayoutManager#setUsingSpansToEstimateScrollbarDimensions(boolean)` for more information.

**Bug fixes**

- Accessibility: There was a bug where once a ViewHolder was recycled and then rebound, the ItemDelegate associated with the RecyclerView's `RecyclerViewAccessibilityDelegate` was not being associated with the ViewHolder's itemView, breaking Accessibility. This is now fixed ([aosp/917740](https://android-review.googlesource.com/c/917740)).

### Version 1.1.0-alpha02

January 30, 2019

`androidx.recyclerview:recyclerview 1.1.0-alpha02` is released.

**API changes**

- `RecyclerView.setLayoutFrozen(boolean)` and `RecyclerView.isLayoutFrozen()` are deprecated in favor of `RecyclerView.suppressLayout(boolean)` and `RecyclerView.isLayoutSuppressed()`. ([aosp/839414](https://android-review.googlesource.com/839414))
- `RecyclerView.setLayoutTransition(LayoutTransition)` is formally deprecated and will throw an `IllegalArgumentException` when called with a non null value. ([aosp/839414](https://android-review.googlesource.com/839414))

**Bug fixes**

- Fix bug in RV where `SmoothScroller` is never stopped ([aosp/843741](https://android-review.googlesource.com/843741))
- Bug fixed where `SCROLL_STATE_IDLE` may not be called at the end of a scrolling animation. ([aosp/812576](https://android-review.googlesource.com/812576))

### Version 1.1.0-alpha01

December 3, 2018

`androidx.recyclerview 1.1.0-alpha01` and `androidx.recyclerview-selection 1.1.0-alpha01` are released.

### androidx.recyclerview 1.1.0-alpha01

**API changes**

- [aosp/723649](http://aosp/723649): RecyclerView now implements `NestedScrollingChild3`, enabling it to be informed of when all its nested scrolling parents have stopped consuming nested scrolling distances. If developer code currently overrides `RecyclerView.onNestedScroll(View, int, int, int, int, int)`, it will likely no longer be called and `RecyclerView.onNestedScroll(View, int, int, int, int, int, int[])` should be overridden instead.

**Bug fixes**

- Fixed crash when using `TransitionManager` to collapse/expand item in `RecyclerView` ([b/37129527](https://issuetracker.google.com/issues/37129527)).
- Fixed bug where `RecyclerView.OnItemTouchListener`'s behavior was inconsistent with the view system's `onInterceptTouchEvent` and `onTouchEvent` behavior ([aosp/721235](https://android-review.googlesource.com/c/platform/frameworks/support/+/721235))
- Fixed few edge case bugs related to smooth scrolling ([aosp/729718](https://android-review.googlesource.com/c/platform/frameworks/support/+/729718), [aosp/747168](https://android-review.googlesource.com/c/platform/frameworks/support/+/747168), [aosp/812576](https://android-review.googlesource.com/c/platform/frameworks/support/+/812576))
- Fixed snap strategy in `PagerSnapHelper` to deal with non-typical child views ([aosp/795752](https://android-review.googlesource.com/c/platform/frameworks/support/+/795752))

### androidx.recyclerview-selection 1.1.0-alpha01

**Bug fixes**

- Fixed `ConcurrentModificationException` when data set changed with removing selection.

## RecyclerView-Selection Version 1.1.0

### RecyclerView-Selection Version 1.1.0

January 27, 2021

`androidx.recyclerview:recyclerview-selection:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d8da646b7b9b3138e3793a946611f88085755d7..c46ef05c18c637a9559c52d5d794084f3f15c042/recyclerview/recyclerview-selection)

**Major changes since 1.0.0**

- Numerous stability improvements.
- Deprecated `withGestureTooltypes` and `withPointerTooltypes` methods on `SelectionTracker.Builder`. These methods will be removed in a future release.

### RecyclerView-Selection Version 1.1.0-rc03

October 1, 2020

`androidx.recyclerview:recyclerview-selection:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f0fecda96ee03daa19b966cf109497c2f4bf8d78..3d8da646b7b9b3138e3793a946611f88085755d7/recyclerview/recyclerview-selection)

**Bug Fixes**

Thanks to Stefan Kiesler for testing fixes and feedback.

- Fixed issue where child view OnClickListeners were called unexpectedly during active selection.
- Mouse handler (band-selection) \> Handle unexpected scrolls gracefully. ([b/167821507](https://issuetracker.google.com/issues/167821507))

### RecyclerView-Selection Version 1.1.0-rc02

September 2, 2020

`androidx.recyclerview:recyclerview-selection:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ee84b31b9af04cf0f0b3b2f3c481950781771d49..f0fecda96ee03daa19b966cf109497c2f4bf8d78/recyclerview)

**Highlights**

- Addressed several regressions from 1.0 in input handling.
- Updated library to honor `onRequestDisallowInterceptTouchEvent`, allowing it to play well with ItemTouchHelper (just swipe it away!).

**Bug Fixes**

- Fixed issue where the selection library misinterpreted `GestureDetector` events resulting in lost taps during active selection ([b/165030422](https://issuetracker.google.com/issues/165030422))
- Fixed issue where selection was not updated to reflect items removed from adapter. ([b/138932671](https://issuetracker.google.com/issues/138932671))
- Fixed issue where RecyclerView items would fire onClick events while SelectionTracker has active selection ([b/161162268](https://issuetracker.google.com/issues/161162268))
- Now handles `onRequestDisallowInterceptTouchEvent` correctly
- Fixed issue where `"Cannot call this method in a scroll callback"` seen during mouse scrolling on Q
- Updated docs (especially in `StableIdKeyProvider`) to clearly state requirements of RecyclerView instance

### Recyclerview-Selection Version 1.1.0-rc01

February 5, 2020

`androidx.recyclerview:recyclerview-selection:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce2902e01f920f17637879b6c918ffe987d2f35b..ee84b31b9af04cf0f0b3b2f3c481950781771d49/recyclerview/recyclerview-selection).

**Bug fixes**

- Fixed an issue where RecyclerView is hard to scroll with a gesture selection if it interacts with a scrollable AppBarLayout ([aosp/1193934](https://android-review.googlesource.com/c/1193934))

### RecyclerView-Selection Version 1.1.0-beta01

December 4, 2019

`androidx.recyclerview:recyclerview-selection:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0c2a7091f663f8e853290ecb2a84c08fc7adac86..ce2902e01f920f17637879b6c918ffe987d2f35b/recyclerview/recyclerview-selection).

General improvements in stability related to defensive checks and management of internal state.

**Bug fixes**

- Improved management of library state and interpretation of CANCEL events, resulting in stability improvements.
  - [b/128054552](https://issuetracker.google.com/128054552)
  - [b/130707991](https://issuetracker.google.com/130707991)
  - [b/137460699](https://issuetracker.google.com/137460699)

**API changes**

- Added selection key type parameter to classes and methods where missing.
- Deprecated methods:
  - [SelectionTracker.Builder#withPointerTooltype](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker.Builder#withPointerTooltypes(int...))
  - [SelectionTracker.Builder#withGestureTooltype](https://developer.android.com/reference/androidx/recyclerview/selection/SelectionTracker.Builder#withGestureTooltypes(int...))
  - These methods existed with the intent that developers might map pointer or gesture behaviors to tooltypes other than the defaults\*. The intent was good, but upon further use it became clear that user expectations around input behavior are *very* tooltype specific. Also, "passive" styli are FINGER tooltype as far as the Android input system is concerned.
  - Default tooltypes are [FINGER](https://developer.android.com/reference/android/view/MotionEvent#TOOL_TYPE_FINGER) for Gesture and [MOUSE](https://developer.android.com/reference/android/view/MotionEvent#TOOL_TYPE_MOUSE) for Pointer.