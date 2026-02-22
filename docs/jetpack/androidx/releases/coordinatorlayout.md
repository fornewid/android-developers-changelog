---
title: https://developer.android.com/jetpack/androidx/releases/coordinatorlayout
url: https://developer.android.com/jetpack/androidx/releases/coordinatorlayout
source: md.txt
---

# Coordinatorlayout

# Coordinatorlayout

API Reference  
[androidx.coordinatorlayout.widget](https://developer.android.com/reference/kotlin/androidx/coordinatorlayout/widget/package-summary)  
Position top-level application widgets, such as AppBarLayout and FloatingActionButton.  

|   Latest Update   |                                      Stable Release                                      | Release Candidate | Beta Release | Alpha Release |
|-------------------|------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| February 26, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout#1.3.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on CoordinatorLayout, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.coordinatorlayout:coordinatorlayout:1.3.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.coordinatorlayout:coordinatorlayout:1.3.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460296+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460296&template=1422727)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.3

### Version 1.3.0

February 26, 2025

`androidx.coordinatorlayout:coordinatorlayout:1.3.0`is released. Version 1.3.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b2fbfbc866f70691b8defd31a392175324793f8..c75bdbab8bebc2c00788ed8427172c46b9463345/coordinatorlayout/coordinatorlayout).

**Important changes since 1.2.0**

**New Features**

- Adds support for page up, page down, move home, and move end key events .([14719d3](https://android.googlesource.com/platform/frameworks/support/+/14719d3c62be24e8568c91cba862d06a39f02e7a))
- Adds demos of`RecyclerView`in a`CoordinatorLayout`with a collapsing app bar and`PreferenceScreen`in a`CoordinatorLayout`with a collapsing app bar. ([fca56e0](https://android.googlesource.com/platform/frameworks/support/+/fca56e0b9864f3327bb4fe8be6ebcfdcc960b886),[I4c679](https://android.googlesource.com/platform/frameworks/support/+/30612996cfc8f2ce286b19134c46a605ba326fc4))

**Bug Fixes**

- Fixes up, down, spacebar and key variation keyboard actions with`NestedScrollView`in a`CoordinatorLayout`. ([I216f4](https://android.googlesource.com/platform/frameworks/support/+/bdd72e61dff5f256a8d072b93547185a152ef292))
- Fixes keyboard down properly collapsing App Bar when a recyclerview is used within a`CoordinatorLayout`. ([I7eac4](https://android.googlesource.com/platform/frameworks/support/+/9532b81b22b1f5529c1163ef0206f3d8ef0253a1))

### Version 1.3.0-rc01

February 12, 2025

`androidx.coordinatorlayout:coordinatorlayout:1.3.0-rc01`is released. Version 1.3.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..1b2fbfbc866f70691b8defd31a392175324793f8/coordinatorlayout/coordinatorlayout).

### Version 1.3.0-beta01

January 29, 2025

`androidx.coordinatorlayout:coordinatorlayout:1.3.0-beta01`is released. Version 1.3.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..4c47131cd5b50c3091fc0874eb606aaac5b168fa/coordinatorlayout/coordinatorlayout).

### Version 1.3.0-alpha03

January 15, 2025

`androidx.coordinatorlayout:coordinatorlayout:1.3.0-alpha03`is released. Version 1.3.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..ad66672b42ec1e9359219e82b7f8189d03df40f5/coordinatorlayout/coordinatorlayout).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I9ab25](https://android-review.googlesource.com/#/q/I9ab25c15f127dbbf2912405f24961e822f554509),[b/326456246](https://issuetracker.google.com/issues/326456246))
- App Bar now properly collapses with Keyboard down when using a`recyclerview`inside a`CoordinatorLayout`.

### Version 1.3.0-alpha02

October 4, 2023

`androidx.coordinatorlayout:coordinatorlayout:1.3.0-alpha02`is released.[Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..1f7407d4293384a1b91bc142880e3525048b3443/coordinatorlayout/coordinatorlayout)

- A version bump release, no change from`1.3.0-alpha01`.

### Version 1.3.0-alpha01

September 20, 2023

`androidx.coordinatorlayout:coordinatorlayout:1.3.0-alpha01`is released.[Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8c8104dca8b315701cba6b4ea6e8089a0fc9857c..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/coordinatorlayout/coordinatorlayout)

**New Features**

- Adds support for page up, page down, move home, and move end key events. ([14719d3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2503895))

**API Changes**

- Added Nullability annotations in`CoordinatorLayout.java`. ([Ieb647](https://android-review.googlesource.com/#/q/Ieb64783622f7931cc7b43bed3a4088c5595e02c1),[b/236474453](https://issuetracker.google.com/issues/236474453))

**Bug Fixes**

- Fixes up, down, spacebar and key variation keyboard actions with`NestedScrollView`and`CoordinatorLayout`. ([bdd72e6](https://android-review.googlesource.com/q/I216f42029674cc8210907eb6591dc9584b000c75))

## Version 1.2

### Version 1.2.0

January 12, 2022

`androidx.coordinatorlayout:coordinatorlayout:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6b13a7c217ae1e01ed4b4d6db213e6e2763cec2..8c8104dca8b315701cba6b4ea6e8089a0fc9857c/coordinatorlayout/coordinatorlayout)

**Important changes since 1.1.0**

- Only retain runtime visible annotations in CoordinatorLayout rules ([9ec7cb](https://android.googlesource.com/platform/frameworks/support/+/9ec7cbd4c185c80999d9d3d8b08dcde305ef52aa))

### Version 1.2.0-rc01

December 15, 2021

`androidx.coordinatorlayout:coordinatorlayout:1.2.0-rc01`is released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85f6fde74bd9e34dee843bce6a5acfba9b82c38e..b6b13a7c217ae1e01ed4b4d6db213e6e2763cec2/coordinatorlayout/coordinatorlayout)

### Version 1.2.0-beta01

November 17, 2021

`androidx.coordinatorlayout:coordinatorlayout:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..6c03583017fc21a40e26a60a9f560b106dd08cec/coordinatorlayout/coordinatorlayout)

**API Changes**

- APIs have been finalized for beta.

### Version 1.2.0-alpha01

November 3, 2021

`androidx.coordinatorlayout:coordinatorlayout:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7f141e51dccf55d6c8d368dac9afaf06c11a8108..f07d12061370a603549747200c79b60239706330/coordinatorlayout/coordinatorlayout)

**Bug Fixes**

- Only retain runtime visible annotations in CoordinatorLayout rules ([9ec7cb](https://android.googlesource.com/platform/frameworks/support/+/9ec7cbd4c185c80999d9d3d8b08dcde305ef52aa))

## Version 1.1.0

### Version 1.1.0

December 4, 2019

`androidx.coordinatorlayout:coordinatorlayout:1.1.0`is released.[Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b98f40c889e3083050d4270e953874921fde8e52..7f141e51dccf55d6c8d368dac9afaf06c11a8108/coordinatorlayout).

**Important changes since 1.0.0**

- [aosp/737190](https://android-review.googlesource.com/c/737190): CoordinatorLayout now implements`NestedScrollingParent3`and`CoordinatorLayout.Behavior`implements a new overload of`onNestedScroll`to enable`Behaviors`to be able to report how much scroll distance they consume to nested scrolling children (during the`dispatchNestedScroll()`/`onNestedScroll()`pass). The previously existing`onNestedScroll(CoordinatorLayout, V, View, int, int, int, int, int)`has been deprecated in favor of the new`onNestedScroll(CoordinatorLayout, V, View, int, int, int, int, int, int[])`and`Behavior`implementations should be updated accordingly. If developer code currently overrides`CoordinatorLayout#onNestedScroll(View, int, int, int, int, int)`, it will likely no longer be called and`CoordinatorLayout#onNestedScroll(View, int, int, int, int, int, int[])`should be overridden instead.
- Exposed CoordinatorLayout to accessibility services ([aosp/1056175](https://android-review.googlesource.com/c/1056175))
- The`CoordinatorLayout.DefaultBehavior`annotation is deprecated. Use the`CoordinatorLayout.AttachedBehavior`interface instead.

### Version 1.1.0-rc01

October 23, 2019

`androidx.coordinatorlayout:coordinatorlayout:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c8501f258905089258e1d19e04fd610bb923c364..b98f40c889e3083050d4270e953874921fde8e52/coordinatorlayout).
| **Note:** The next release of CoordinatorLayout will remove the deprecated`DefaultBehavior`annotation. Switch all usages of that annotation to the`AttachedBehavior`interface instead.

**New features**

- Exposed CoordinatorLayout to accessibility services ([aosp/1056175](https://android-review.googlesource.com/c/platform/frameworks/support/+/1056175))

### Version 1.1.0-beta01

June 5, 2019

`androidx.coordinatorlayout:coordinatorlayout:1.1.0-beta01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/225ba21ffaa37f0f1fc0da373afd960907e8092f..c8501f258905089258e1d19e04fd610bb923c364/coordinatorlayout).

**Bug fixes**

- Migrate away from deprecated test classes ([aosp/853955](https://android-review.googlesource.com/c/platform/frameworks/support/+/853955))

### Version 1.1.0-alpha01

December 3, 2018

**API changes**

- [aosp/737190](https://android-review.googlesource.com/c/platform/frameworks/support/+/737190): CoordinatorLayout now implements`NestedScrollingParent3`and`CoordinatorLayout.Behavior`implements a new overload of`onNestedScroll`to enable`Behaviors`to be able to report how much scroll distance they consume to nested scrolling children (during the`dispatchNestedScroll()`/`onNestedScroll()`pass). The previously existing`onNestedScroll(CoordinatorLayout, V, View, int, int, int, int, int)`has been deprecated in favor of the new`onNestedScroll(CoordinatorLayout, V, View, int, int, int, int, int, int[])`and`Behavior`implementations should be updated accordingly.

  If developer code currently overrides`CoordinatorLayout#onNestedScroll(View, int, int, int, int, int)`, it will likely no longer be called and`CoordinatorLayout#onNestedScroll(View, int, int, int, int, int, int[])`should be overridden instead.