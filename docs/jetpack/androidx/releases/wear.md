---
title: https://developer.android.com/jetpack/androidx/releases/wear
url: https://developer.android.com/jetpack/androidx/releases/wear
source: md.txt
---

# Wear

[User Guide](https://developer.android.com/training/wearables) [Code Sample](https://github.com/android/wear-os-samples) API Reference  
[androidx.wear.activity](https://developer.android.com/reference/kotlin/androidx/wear/activity/package-summary)  
[androidx.wear.ambient](https://developer.android.com/reference/kotlin/androidx/wear/ambient/package-summary)  
[androidx.wear.input](https://developer.android.com/reference/kotlin/androidx/wear/input/package-summary)  
[androidx.wear.utils](https://developer.android.com/reference/kotlin/androidx/wear/utils/package-summary)  
[androidx.wear.widget](https://developer.android.com/reference/kotlin/androidx/wear/widget/package-summary)  
[androidx.wear.widget.drawer](https://developer.android.com/reference/kotlin/androidx/wear/widget/drawer/package-summary)  
(*See the refdocs for all wear packages*) Create applications for Wear OS by Google smartwatches.


This table lists all the artifacts in the `androidx.wear` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| wear | [1.4.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-1.4.0) | - | - | - |
| wear-input | [1.2.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-input-1.2.0) | - | - | - |
| wear-input-testing | [1.2.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-input-testing-1.2.0) | - | - | - |
| wear-ongoing | [1.1.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-ongoing-1.1.0) | - | - | - |
| wear-phone-interactions | [1.1.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-phone-interactions-1.1.0) | - | - | - |
| wear-remote-interactions | [1.2.0](https://developer.android.com/jetpack/androidx/releases/wear#wear-remote-interactions-1.2.0) | - | - | - |

This library was last updated on: February 25, 2026

## Declaring dependencies

To add a dependency on Wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.wear:wear:1.4.0"

    // Add support for wearable specific inputs
    implementation "androidx.wear:wear-input:1.2.0"
    implementation "androidx.wear:wear-input-testing:1.2.0"

    // Use to implement wear ongoing activities
    implementation "androidx.wear:wear-ongoing:1.1.0"

    // Use to implement support for interactions from the Wearables to Phones
    implementation "androidx.wear:wear-phone-interactions:1.1.0"
    // Use to implement support for interactions between the Wearables and Phones
    implementation "androidx.wear:wear-remote-interactions:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.wear:wear:1.4.0")

    // Add support for wearable specific inputs
    implementation("androidx.wear:wear-input:1.2.0")
    implementation("androidx.wear:wear-input-testing:1.2.0")

    // Use to implement wear ongoing activities
    implementation("androidx.wear:wear-ongoing:1.1.0")

    // Use to implement support for interactions from the Wearables to Phones
    implementation("androidx.wear:wear-phone-interactions:1.1.0")
    // Use to implement support for interactions between the Wearables and Phones
    implementation("androidx.wear:wear-remote-interactions:1.2.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460965+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460965&template=1422653)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Wear Core Version 1.0

### Version 1.0.0

December 17, 2025

`androidx.wear:wear-core:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d100b900f3fe5699adfa2afaaf6d467cf7b836dd..ea52d659916d0fe20e20ad2ed5574bf39e7e69a4/wear/wear-core).

**Major features of 1.0.0:**

- Added `WearApiVersionHelper` to assist with runtime API compatibility checking on Wear. Clients can use this static helper class and the provided method `(#isApiVersionAtLeast(VERSION))` to check compatibility.

### Version 1.0.0-rc01

October 08, 2025

`androidx.wear:wear-core:1.0.0-rc01` is released with no changes. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9ac371e13def566b9138a983e5dd9327a6244ae..4ab8deefd0e1b7fcf485d66245ee144aea666fbc/wear/wear-core).

### Version 1.0.0-beta02

September 10, 2025

`androidx.wear:wear-core:1.0.0-beta02` is released. Version 1.0.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..f9ac371e13def566b9138a983e5dd9327a6244ae/wear/wear-core).

**Bug Fixes**

- Prevent `WearApiVersionHelper` from throwing on older devices when checking newer APIs.

### Version 1.0.0-beta01

July 30, 2025

`androidx.wear:wear-core:1.0.0-beta01` is released with no notable changes since the last alpha. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..5fa9d0954ece0376736164b0f7bc2ef33506ab70/wear/wear-core).

### Version 1.0.0-alpha02

July 16, 2025

`androidx.wear:wear-core:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/wear/wear-core).

**API Changes**

- Updates `WearApiVersionHelper` to include VIC/Baklava ([I4676d](https://android-review.googlesource.com/#/q/I4676d749e3b0df6e5965c12ae49a553e79b0280f))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: `-Xjspecify-annotations=strict`, `-Xtype-enhancement-improvements-strict-mode` ([Icbfb9](https://android-review.googlesource.com/#/q/Icbfb9996a30b4decc85ee8a9bc4211a25adfcfe3), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.0.0-alpha01

May 29, 2024

`androidx.wear:wear-core:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b/wear/wear-core).

**API Changes**

- Added a new class `WearApiVersionhelper` to assist with runtime API compatibility checking on Wear. Clients can use this static helper class and the provided method (`#isApiVersionAtLeast(VERSION)`) to check compatibility.

## Wear Tooling Preview Version 1.0

### Version 1.0.0

November 29, 2023

`androidx.wear:wear-tooling-preview:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/af0e5af4f5cecea65dc0553cde117ce199dacb30..5b26896e52ff3bce385a4211e47750dda343998c/wear/wear-tooling-preview)

**Features in 1.0.0**

- Add `WearDevices` to list valid wear devices that can be used for UI previews.

### Version 1.0.0-rc01

November 15, 2023

`androidx.wear:wear-tooling-preview:1.0.0-rc01` is released with no changes. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..af0e5af4f5cecea65dc0553cde117ce199dacb30/)

### Version 1.0.0-beta01

October 18, 2023

`androidx.wear:wear-tooling-preview:1.0.0-beta01` is released with no changes. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/wear/wear-tooling-preview)

### Version 1.0.0-alpha01

August 23, 2023

`androidx.wear:wear-tooling-preview:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5/wear/wear-tooling-preview)

**API Changes**

- Add `WearDevices` to list valid wear devices that can be used for UI previews ([Ib036e](https://android-review.googlesource.com/#/q/Ib036edb1823884c5f9e312d6733e7c3db22f9a0a))

## Wear Version 1.4

### Version 1.4.0

February 25, 2026

`androidx.wear:wear:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea52d659916d0fe20e20ad2ed5574bf39e7e69a4..03bb121e9d4df29b8df0088d71c9091a9b55d1f2/wear/wear).

**Important changes since 1.3.0:**

- Bugfix to vertically center `ConfirmationOverlay` icon when there's no message. [I496d8](https://android-review.googlesource.com/#/q/I496d8db2998206e45b88117665057d9c5e67e7bd)

### Version 1.4.0-rc01

January 28, 2026

`androidx.wear:wear:1.4.0-rc01` is released. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f005cd28feebaa370904e6437c9ca3d465f5ac4f..75a4eb8f88ca34fde313ecae1e46c343519a44e6/wear/wear).

- There are no new changes between the beta01 and rc01.

### Version 1.4.0-beta01

December 17, 2025

`androidx.wear:wear:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..f005cd28feebaa370904e6437c9ca3d465f5ac4f/wear/wear).

- There are no substantial new changes since the previous alpha release.

### Version 1.4.0-alpha02

July 16, 2025

`androidx.wear:wear:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/wear/wear).

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: `-Xjspecify-annotations=strict`, `-Xtype-enhancement-improvements-strict-mode` ([If4b1a](https://android-review.googlesource.com/#/q/If4b1a5d446c07b0400f92650aae1a0072cf90ab4), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.4.0-alpha01

November 15, 2023

`androidx.wear:wear:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a81fd7956fbfa71c7b124c58a36e4799d8a231a3..312eb9f1ddece3a18317f18515a877e0e745cb2c/wear/wear)

**Bug Fixes**

- Vertically center `ConfirmationOverlay` icon when there's no message. ([I496d8](https://android-review.googlesource.com/#/q/I496d8db2998206e45b88117665057d9c5e67e7bd))

## Wear Version 1.3

### Version 1.3.0

August 9, 2023

`androidx.wear:wear:1.3.0` is released with no changes since `1.3.0-rc01`. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7b02e08f28f0a0eeda84e40d638084bbc89c82f9..a81fd7956fbfa71c7b124c58a36e4799d8a231a3/wear/wear)

**Important changes since 1.2.0**

- Migrate `AmbientModeSupport` to use `LifecycleObserver`. Deprecate `AmbientModeSupport` in favor of the new lifecycle-aware classes.
- Update `ConfirmationOverlay` with new icons/layout, fonts and font metrics
- `SwipeDismissTransitionHelper` updated to use a background drawable instead of a 2nd `View` to correct errors when using the `FragmentContainerView`
- `SwipeDismissFrameLayout` animation updated to be consistent with the Wear platform and Wear Compose implementations.
- `SwipeDismissFrameLayout` bug fix to avoid accidental dismissing of fragments with a vertical fling
- `ArcLayout` now supports expansion weights which operate in a similar way to regular Layout weights.
- Support `layoutDirection` on `ArcLayout`

### Version 1.3.0-rc01

June 21, 2023

`androidx.wear:wear:1.3.0-rc01` is released with no changes since `1.3.0-beta01`. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..7b02e08f28f0a0eeda84e40d638084bbc89c82f9/wear/wear)

### Version 1.3.0-beta01

June 7, 2023

`androidx.wear:wear:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..73f902dee011bfe400d8a0330bfd8d4bb632065f/wear/wear)

**API Changes**

- Updated `AmbientLifecycleObserver` after feedback. `AmbientLifecycleObserverInterface` has been renamed to `AmbientLifecycleObserver`, and an instance can be obtained by calling `AmbientLifecycleObserver(...)`. `isAmbient` has been moved to be a field instead of a method. ([I84b4f](https://android-review.googlesource.com/#/q/I84b4f60620993efc0cf20f9cad35c2686e1322f3))

**Bug Fixes**

- Adding null checks to handle cases when the parent view is null while resetting alpha and translation in `SwipeToDismiss`. ([Ib0ec7](https://android-review.googlesource.com/#/q/Ib0ec71ea0ec5cbe243379ab07bcacc64cdf28651))

### Version 1.3.0-alpha05

April 19, 2023

`androidx.wear:wear:1.3.0-alpha05` is released. [Version 1.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/wear/wear)

**API Changes**

- Migrate `AmbientModeSupport` to use `LifecycleObserver`. Deprecate `AmbientModeSupport` in favour of the new lifecycle-aware classes. ([I1593b](https://android-review.googlesource.com/#/q/I1593b4a089004310d965c9b79f79d1a70caba3ed))

**Bug Fixes**

- Update `SwipeDismissTransitionHelper` background scrim approach to use drawables instead of adding view to fix errors while using `FragmentContainerView`. ([I851cd](https://android-review.googlesource.com/#/q/I851cdc2ef6c763e1d7a5bd59143fb4f7d2baf2fe))

### Version 1.3.0-alpha04

January 25, 2023

`androidx.wear:wear:1.3.0-alpha04` is released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/wear/wear)

**Bug Fixes**

- We have updated the animation in `SwipeDismissFrameLayout` to be consistent with the Wear platform and Wear Compose implementations. ([I7261b](https://android-review.googlesource.com/#/q/I7261b9e695a1165f96f07e865b01b929519b28ed))

### Version 1.3.0-alpha03

August 24, 2022

`androidx.wear:wear:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..dd1e45e8550560087f6447a34a9145048b5766f4/wear/wear)

**New Features**

- `ArcLayout` now supports expansion weights which operate in a similar way to regular Layout weights. This means you can specify the relative size of child elements without having to compute their angles directly. We've also added a best effort `MaxAngleDegrees` which is respected when expanding child elements with weights. E.g. you could clamp the arc with several children with weights to 90 degrees, this would also respect the space taken by any non-expanded elements..

**API Changes**

- We've added weight to `ArcLayout.LayoutParams` which allows a widget to expand to fill the available space, if there's more than one widget then their share of the available space is proportional to their weight. In addition we've added `ArcLayout.setMaxAngleDegrees` so you can for example cap the expansion at 90 degrees (NB this does not affect layout of any fixed sized child widgets). Finally `ArcLayout.Widget` now has `setSweepAngleDegrees` which allows the `ArcLayout` to inform a Widget with a non-zero weight of its size. ([I75f24](https://android-review.googlesource.com/#/q/I75f2449c6bed88e2f6f8a443dd8951b2ce275d76))
- Updated nullability of `setColorFilter`([I99ddf](https://android-review.googlesource.com/#/q/I99ddf2b20cb2b58eae3e4ca40b605201076a1ad4), [b/236498063](https://issuetracker.google.com/issues/236498063))

### Version 1.3.0-alpha02

February 23, 2022

`androidx.wear:wear:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/wear/wear)

**New Features**

- Support `layoutDirection` on `ArcLayout` ([I14d49](https://android-review.googlesource.com/#/q/I14d492b43d79035e573b0aa17e178f527ff7d9c3))
- Improved content description message for ConfirmationOverlay ([I0fdf8](https://android-review.googlesource.com/#/q/I0fdf8662c30574dbf0c23cbd4d9b197d04d316e3))
- Update `ConfirmationOverlay` with new icons/layout. ([If5b54](https://android-review.googlesource.com/#/q/If5b5408a096719610ea80c5d2129762488558f85))

**Bug Fixes**

- Added ProGuard rules to ensure that ambient-related code is kept ([Idaa10](https://android-review.googlesource.com/#/q/Idaa10fbf067be47a3971b3bbe083c2b5ae7e3fb1))
- Avoid accidentally dismissing of fragments in SwipeDismissFrameLayout with a vertical fling ([Idb6d8](https://android-review.googlesource.com/#/q/Idb6d8a39b1b2d5760d1f5e9ec9678dc75d15dde3))
- Fix ConfirmationOverlay when it has no message ([I63e6f](https://android-review.googlesource.com/#/q/I63e6f0d8b6a310a9f2f642d4fdc7ec4b09f147af))

**External Contribution**

- Dae Gyu LEE (Samsung) - Avoid accidentally dismissing of fragments in SwipeDismissFrameLayout with a vertical fling ([Idb6d8](https://android-review.googlesource.com/#/q/Idb6d8a39b1b2d5760d1f5e9ec9678dc75d15dde3))

### Version 1.3.0-alpha01

September 29, 2021

`androidx.wear:wear:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/21d8b657a9de9dc81f495c51813006a7408c469b..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/wear/wear)

**Bug Fixes**

- `ConfirmationOverlay` now pushes the icon up to accommodate longer messages, without the message entering the device's bezel (or off-screen). ([I54bff](https://android-review.googlesource.com/#/q/I54bff6521d0fc8b942056d02351ca48390d04101))

## Wear-Remote-Interactions Version 1.2.0

### Version 1.2.0

February 25, 2026

`androidx.wear:wear-remote-interactions:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea52d659916d0fe20e20ad2ed5574bf39e7e69a4..55bf42f5cd58f4b0527ed1fccdf579f7e86c9b9e/wear/wear-remote-interactions).

**Important changes since 1.1.0:**

- Updated `RemoteActivityHelper.startRemoteActivity` to use a new public Wear SDK API (`startRemoteActivity`) if it's available (from Wear 6 onwards). [Id1e77](https://android-review.googlesource.com/#/q/Id1e77f5fc838470748137a612176f9bee76f6c46)
- Updated dependency on Play Basement version which contained CVE-2022-2390 vulnerability.

### Version 1.2.0-rc01

January 28, 2026

`androidx.wear:wear-remote-interactions:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f005cd28feebaa370904e6437c9ca3d465f5ac4f..7b41731cd36163f3e218f3d341cf22b377fdf90c/wear/wear-remote-interactions).

**Bug Fixes**

- Updated dependency on Play Basement version which contained CVE-2022-2390 vulnerability.

### Version 1.2.0-beta01

December 17, 2025

`androidx.wear:wear-remote-interactions:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..f005cd28feebaa370904e6437c9ca3d465f5ac4f/wear/wear-remote-interactions).

- There are no substantial new changes since the previous alpha release.

### Version 1.2.0-alpha01

July 2, 2025

`androidx.wear:wear-remote-interactions:1.2.0-alpha01` is released. Version 1.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80589c1ddd2f27bbb6103e55cd3a8a1f18c5b16..1b437892629a2cdedb46d9b7232575987b2cc6b5/wear/wear-remote-interactions).

**New Features**

- Updated `RemoteActivityHelper.startRemoteActivity` to use a new public Wear SDK API (`startRemoteActivity`) if it's available (from Wear 6 onwards). ([Id1e77](https://android-review.googlesource.com/#/q/Id1e77f5fc838470748137a612176f9bee76f6c46))

## Wear Ongoing \& Interactions Version 1.1.0

### Version 1.1.0

February 26, 2025

`androidx.wear:wear-phone-interactions:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2a6e9213b8a20cd6b58f08550065b5aa6bc56150..69d58ba42a41c8a1d00cead8cefd57d9ccb81fc1/wear/wear-phone-interactions).

**Important changes since 1.0.0**

- This version contains crucial bug fix for Apps running on Wear OS 5 (API level 34) or higher and targeting API level 35 or higher.
- Apps should update to this version of the library before updating their `targetSdkVersion` to 35 or higher.
- Otherwise, runtime exception will be thrown.
- A new definition for paired device type - `none`, when the device is not paired with the phone, has been added.

### Version 1.1.0-rc01

February 12, 2025

`androidx.wear:wear-phone-interactions:1.1.0-rc01` is released with no notable changes since the last beta. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..2a6e9213b8a20cd6b58f08550065b5aa6bc56150/wear/wear-phone-interactions).

### Version 1.1.0-beta01

January 29, 2025

`androidx.wear:wear-phone-interactions:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..4c47131cd5b50c3091fc0874eb606aaac5b168fa/wear/wear-phone-interactions).

**New Features**

The 1.1.0-beta01 release of Wear Phone Interactions indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear Phone Interactions 1.1 includes the following new functionalities and APIs:

- Added property `redirectUrl` to `OAuthRequest`.
- Documentation fixes
- Additional type in `PhoneTypeHelper` to specify when device is not paired with phone, instead of using existing unknown type.

**API Changes**

- Added new definition for paired device type - none, when device is not paired with the phone. ([I06cb8](https://android-review.googlesource.com/#/q/I06cb8e824cce485132954503cd3957a4c35fa923))

### Version 1.1.0-alpha05

December 11, 2024

`androidx.wear:wear-phone-interactions:1.1.0-alpha05` is released. Version 1.1.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..46295bc0b75a16f452e8e0090e8de41073d4dbb6/wear/wear-phone-interactions).

**Bug Fixes**

- Fix a crash bug when running on Wear OS 5 (API level 34) or higher while targeting API level 35 or higher. Apps should update to this version of the library before updating their `targetSdkVersion` to 35 or higher.

### Version 1.1.0

December 11, 2024

`androidx.wear:wear-remote-interactions:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6d28cab96afc79c552e0a536271069ae563da2ab..c80589c1ddd2f27bbb6103e55cd3a8a1f18c5b16/wear/wear-remote-interactions).

**Important changes since 1.0.0**

- We have added `RemoteActivityHelper.isRemoteActivityHelperAvailable` which helps check whether the functionality of launching a remote activity is available. ([I107a9](https://android-review.googlesource.com/#/q/I107a967fbc8fdf445013d32427036aa9756f229b))

### Version 1.1.0-rc01

October 16, 2024

`androidx.wear:wear-remote-interactions:1.1.0-rc01` is released with no changes since `1.1.0-beta01`. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8b5ab34869fa8731b13a77763ea92989ce4ef70d..6d28cab96afc79c552e0a536271069ae563da2ab/wear/wear-remote-interactions).

### Version 1.1.0-beta01

July 24, 2024

`androidx.wear:wear-remote-interactions:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..8b5ab34869fa8731b13a77763ea92989ce4ef70d/wear/wear-remote-interactions). The 1.3.0-beta01 release of Wear Remote Interactions indicates that this release of the library is feature complete and the API is locked (except where marked as experimental).

### Version 1.1.0-alpha04

January 10, 2024

`androidx.wear:wear-phone-interactions:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/wear/wear-phone-interactions)

**API Changes**

- We have added `RemoteAuthClient.isRemoteAuthAvailable` which checks whether remote auth is available. ([Ibc10c](https://android-review.googlesource.com/#/q/Ibc10c7fb8af563a4538f0f689a87fb667d571afb))

### Version 1.1.0-alpha02

January 10, 2024

`androidx.wear:wear-remote-interactions:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/wear/wear-remote-interactions)

**API Changes**

- We have added `RemoteActivityHelper.isRemoteActivityHelperAvailable` which helps check whether the functionality of launching a remote activity is available. ([I107a9](https://android-review.googlesource.com/#/q/I107a967fbc8fdf445013d32427036aa9756f229b))
- We have updated `RemoteActivityHelper`'s constructor to have optional parameter compatible in Java. ([I75554](https://android-review.googlesource.com/#/q/I755543588602ebab6f506780e9808b7978da377a))

### Version 1.1.0-alpha01

June 21, 2023

`androidx.wear:wear-remote-interactions:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15e31e87f719904535e26aadb16fc5085490c3c6..3b5b931546a48163444a9eddc533489fcddd7494/wear/wear-remote-interactions)

**Bug Fixes**

- Improved how completion and error handling is done in `RemoteActivityHelper`. ([I60d60](https://android-review.googlesource.com/#/q/I60d608db5d3b7fdbc64d9a7046a0b0891e09b698))

**External Contribution**

- Remove Guava dependency from `wear-remote-interactions` and use smaller alternatives.

### Wear-Phone-Interactions Version 1.1.0-alpha03

March 9, 2022

`androidx.wear:wear-phone-interactions:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..33cb12e8aba043a05b40470a5ef3be1b35114fd5/wear/wear-phone-interactions)

**Bug Fixes**

- `redirectUrl` from `OAuthRequest` now returns an empty String if there the redirect URL is not set in the given request URL. ([I44242](https://android-review.googlesource.com/#/q/I44242b23fa434fbd845ec4aa2b1ef74ddc92f1e5))

### Wear-Phone-Interactions Version 1.1.0-alpha02

December 15, 2021

`androidx.wear:wear-phone-interactions:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..301586664b5aad60548f21866cad502d524dbf9f/wear/wear-phone-interactions)

**Bug Fixes**

- Fix the errors in `RemoteAuthClient` documentation, including error in code sample snippet and the dead link to `ErrorCode` ([I260e8](https://android-review.googlesource.com/#/q/I260e8e56bd7e85269e4eaa1aaede197154ebae5d))

### Wear-Phone-Interactions Version 1.1.0-alpha01

September 15, 2021

`androidx.wear:wear-phone-interactions:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da0944806932662865db1602128f5be25f81a5fa..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/wear/wear-phone-interactions)

**API Changes**

- Added property `redirectUrl` to OAuthRequest. ([I98840](https://android-review.googlesource.com/#/q/I98840d8e19f5534c3ebf15937506a2984beaf0d5), [Ie684d](https://android-review.googlesource.com/#/q/Ie684d55c71bf5a2800956b9ddd11106fe69d2df8))

## Wear Ongoing \& Interactions Version 1.0.0

### Wear-Phone-Interactions Version 1.0.1

December 15, 2021

`androidx.wear:wear-phone-interactions:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6ba6a1a24174802f1adfbd10672775c9a04737bc..07b07869f5e9674d63db1ce4b4d76b24b40f5ad2/wear/wear-phone-interactions)

**Bug Fixes**

- Fixed exception was thrown from the `BridgingManager` when trying to disable bridging notifications without `excludedTags`.

### Wear-Phone-Interactions Wear-Remote-Interactions Version 1.0.0

September 15, 2021

`androidx.wear:wear-phone-interactions:1.0.0` and `androidx.wear:wear-remote-interactions:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a8713100cbbd40b35331f0fc0f08af03640800a4..15e31e87f719904535e26aadb16fc5085490c3c6/wear)

**Major features of 1.0.0**

The Phone Interaction Library contains APIs for interactions from the Wearables to Phones. It contains the following:

- `PhoneDeviceType`, providing helper methods for determining the type of phone the current watch is paired to, for use on Wearable devices only.
- `BridgingManager`, `BridgingManagerService` and `BridgingConfig` APIs to enable/disable notifications at runtime and optionally set tags for notifications that are exempt from the bridging mode.
- `RemoteAuthClient`, providing support for remote authentication on Wearables together with support for adding OAuth PKCE extension. Additional handlers and helper classes for communication are provided.

The Remote Interaction Library contains APIs for interactions between the Wearables and Phones. It contains the following:

- `WatchFaceConfigIntentHelper`, providing helper functions to specify the ID and component name in the watch face configuration activities for the companion on the phone.
- `RemoteActivityHelper` class which can be used for opening intents on other devices (i.e. from watch to phone).

### Wear-Phone-Interactions Wear-Remote-Interactions Version 1.0.0-rc01

September 1, 2021

`androidx.wear:wear-phone-interactions:1.0.0-rc01` and `androidx.wear:wear-remote-interactions:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..a8713100cbbd40b35331f0fc0f08af03640800a4/wear)

**Bug Fixes**

- Fix bug preventing errors raised within Google Play Services from being propagated to the caller when using RemoteActivityHelper ([I60d60](https://android-review.googlesource.com/#/q/I60d608db5d3b7fdbc64d9a7046a0b0891e09b698))
- Fix bug where RemoteActivityHelper would never fulfill its Future if there were no connected nodes, or if the requested nodeId was not found ([I60d60](https://android-review.googlesource.com/#/q/I60d608db5d3b7fdbc64d9a7046a0b0891e09b698))

## Wear-Ongoing Version 1.1

### Version 1.1.0

September 10, 2025

`androidx.wear:wear-ongoing:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bb2d7cbe99a56fe59407bf1b598687ce8265ea22..b5910dbad26bb976618a85ecba477cbcf797c451/wear/wear-ongoing).

**Important changes since 1.0.0:**

- Added a content description field to Ongoing Activities, which is used by accessibility services.
- Added `RequiresPermission` annotations to APIs that require `POST_NOTIFICATIONS` permission on SDK 33 and above.

### Version 1.1.0-rc01

August 27, 2025

`androidx.wear:wear-ongoing:1.1.0-rc01` is released with no changes since the last beta. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..bb2d7cbe99a56fe59407bf1b598687ce8265ea22/wear/wear-ongoing).

### Version 1.1.0-beta01

July 30, 2025

`androidx.wear:wear-ongoing:1.1.0-beta01` is released with no notable changes since the last alpha. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..5fa9d0954ece0376736164b0f7bc2ef33506ab70/wear/wear-ongoing).

### Version 1.1.0-alpha01

August 23, 2023

`androidx.wear:wear-ongoing:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e29ee7ab92601af2140abdabaabf4960517e49f2..3315f1ef094c312203fe26841287902916fbedf5/wear/wear-ongoing)

**API Changes**

- Add a content description field to Ongoing Activity. This will be used by accessibility services to describe the Ongoing Activity. ([I79fc6](https://android-review.googlesource.com/#/q/I79fc6eaebca0dbb4cd5e7998e29b77152c1547c9))

**Bug Fixes**

- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631), [b/238790278](https://issuetracker.google.com/issues/238790278))

### Wear-Ongoing Version 1.0.0

September 1, 2021

`androidx.wear:wear-ongoing:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0cdc4fd8c6d04f740cd6224042b7b173e0d38721..e29ee7ab92601af2140abdabaabf4960517e49f2/wear/wear-ongoing)

**Major features of 1.0.0**

- The Wear Ongoing Activities API is an API for developers, including third party developers, used to mark their activity as an "Ongoing Activity", and provide the needed information.
- Ongoing Activities refer to activities that could be running in the background of the watch (e.g. workouts, calls and media). On Wear 3, an activity declared as ongoing will be made more prominent through a dedicated overlay icon on the watchface and a different rendering in the app launcher.
- For more information, see the [Wear Ongoing Activity Guide](https://developer.android.com/training/wearables/ongoing-activity)

### Wear-Phone-Interactions Wear-Remote-Interactions Version 1.0.0-beta01

August 18, 2021

`androidx.wear:wear-phone-interactions:1.0.0-beta01` and `androidx.wear:wear-remote-interactions:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/wear)

**API Changes**

- Renamed class `RemoteIntentHelper` to `RemoteActivityHelper`. Renamed functions `RemoteIntentHelper#getRemoteIntentExtraIntent` and `RemoteIntentHelper#getRemoteIntentNodeId` to `RemoteActivityHelper#getTargetIntent` and `RemoteActivityHelper#getTargetNodeId`, respectively. ([Id2042](https://android-review.googlesource.com/#/q/Id2042393d23e7e7520e631e01f84bd40bff45ce3))

### Wear-Ongoing Version 1.0.0-rc01

August 18, 2021

`androidx.wear:wear-ongoing:1.0.0-rc01` is released with no changes since `1.0.0-beta01`. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..0cdc4fd8c6d04f740cd6224042b7b173e0d38721/wear/wear-ongoing)

### Wear-Ongoing Version 1.0.0-beta01

August 4, 2021

`androidx.wear:wear-ongoing:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/wear/wear-ongoing)

**API Changes**

- Some setters on OngoingActivity.Builder now accept a null argument in order to give symmetry and consistency to the setters and getters ([I17ee5](https://android-review.googlesource.com/#/q/I17ee5238d2e515be2796fa12ecb6adc97e44fcd9))

### Wear-Phone-Interactions Version 1.0.0-alpha07

August 4, 2021

`androidx.wear:wear-phone-interactions:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/wear/wear-phone-interactions)

**API Changes**

- Renamed `WearTypeHelper.isChinaDevice` to`WearTypeHelper.isChinaBuild`. ([I47302](https://android-review.googlesource.com/#/q/I4730259bc10061164e989fba882331496b457316))
- We have updated RemoteAuthClient library to automatically pick redirect_uri based on device type (RoW/China). ([I38866](https://android-review.googlesource.com/#/q/I38866d48ffdeaa961edd5e67360b509d7ccffd6c))
- Fixed bug that caused converting BridgingConfig to/from Bundle to fail with ClassCastException. Added unit tests for BridgingManagerService class. ([I68ecb](https://android-review.googlesource.com/#/q/I68ecb506624219155adb5c3aa2fc67621fefb73e))

### Wear-Remote-Interactions Version 1.0.0-alpha06

August 4, 2021

`androidx.wear:wear-remote-interactions:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/wear/wear-remote-interactions)

### Wear-Phone-Interactions Version 1.0.0-alpha06

July 21, 2021

`androidx.wear:wear-phone-interactions:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear/wear-phone-interactions)

**API Changes**

- `BridgingManagerSeviceBinder` class is now a subclass of Service and is renamed to BridgingManagerSevice. ([I9fca2](https://android-review.googlesource.com/#/q/I9fca232a5d402c03b2d879187de92b14ab3c2444))
- Method `RemoteAuthClient.Callback.onAuthorizationError` is changed to include OAuthRequest parameter. Methods requiring callback now also require an executor for the callback to be run on. ([I35e11](https://android-review.googlesource.com/#/q/I35e119436556aeae193fb146369af9e97b8c71c4))

**Bug Fixes**

- We have made the authentication API clearer with more documented parameters and by using properties where possible. ([I12287](https://android-review.googlesource.com/#/q/I1228725db7defda787b49d322bfed4ab307f2b9b))

### Wear-Phone-Interactions Version 1.0.0-alpha05

June 30, 2021

`androidx.wear:wear-phone-interactions:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25..19ae3a88ff0824d615355b492cb56049e16991f2/wear/wear-phone-interactions)

**Bug Fixes**

- Documented parameters that should be passed in constructor for `BridgingConfig.Builder`.

### Wear-Ongoing Version 1.0.0-alpha06

June 2, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/wear/wear-ongoing)

**API Changes**

- Add Title field to Ongoing Activity. ([I7a405](https://android-review.googlesource.com/#/q/I7a4050af6db1845a1859a8df92dbc36610002901))

**Bug Fixes**

- `SerializationHelper.copy()` now does a defensive copy of the information ([I8b276](https://android-review.googlesource.com/#/q/I8b27619e49feb1c8d6b1e782060ea62eee298c6a))
- Improved setCategory documentation ([Iff01f](https://android-review.googlesource.com/#/q/Iff01f5843e3239180d9a18a3fec1c7279f1ea818))

### Wear-Ongoing Version 1.0.0-alpha05

May 18, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/wear/wear-ongoing)

**API Changes**

- `OngoingActivity` now has getters to retrieve all values directly set via the Builder (or the defaults taken from the associated Notification). ([Id8ac8](https://android-review.googlesource.com/#/q/Id8ac8b7aa2e363f6dfc8ea484782a8d7d198939a))

  - The new class `Status` is now used to create the status of the the `OngoingActivity`
  - `OngoingActivityData` and `OngoingActivityStatus` are no longer part of the public API.
- The classes `TextStatusPart` and `TimerStatusPart` are no longer part of the public API. ([I57fb6](https://android-review.googlesource.com/#/q/I57fb687933fcbc259c1c93094a2e5fbc88ddd979))

  - To create a `Part` with a static text, use `Status.TextPart`.
  - To create a `Part` with a stopwatch (counting up), use `Status.Stopwatch`
  - To create a `Part` with a timer (counting down), use `Status.Timer`

### Wear-Ongoing Version 1.0.0-alpha04

May 5, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/wear/wear-ongoing)

**API Changes**

- On OngoingActivity, the methods fromExistingOngoingActivity are now called recoverOngoingActivity.
- OngoingActivity now has a full set of getters, the same previously only available at OngoingActivityData. ([I0ee4d](https://android-review.googlesource.com/#/q/I0ee4deaba18f5da836d5dc31607df3d93a808edd))

### Wear-Remote-Interactions Version 1.0.0-alpha05

July 21, 2021

`androidx.wear:wear-remote-interactions:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear/wear-remote-interactions)

**API Changes**

- We have added the `RemoteIntentHelper` class (previously RemoteIntent in the Wearable Support Library) which can be used for opening intents on other devices (i.e. from watch to phone). ([I1d7e0](https://android-review.googlesource.com/#/q/I1d7e07052da1e0f942e61b044de08f97b8c51279))

- The PlayStoreAvailability class has been removed from the AndroidX library.
  To detect whether the Play Store is available on a connected phone, use the [`androidx.phone.interactions.PhoneTypeHelper.getPhoneDeviceType`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper.Companion#getPhoneDeviceType(android.content.Context)) method to determine if the connected phone is an Android phone. Then use the `androidx.wear.utils.WearTypeHelper.isChinaDevice` method to determine if the connected phone is a Chinese device. If the phone is an Android phone and if it is not a Chinese device then the Play Store will be available.
  ([Ie7dec](https://android-review.googlesource.com/#/q/Ie7dec297fc1b01c4e308bd001a3666fd87e509a0))

### Wear-Phone-Interactions Version 1.0.0-alpha04

April 7, 2021

`androidx.wear:wear-phone-interactions:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..24330de8135d689b34a31a701181b20549e8db25/wear/wear-phone-interactions)

**API Changes**

- Updated `ErrorCode` constants to make the new library backwards compatible with the implementation in Wearable Support Library.

**Bug Fixes**

- Fixed exception caused by new OAuth API when starting an OAuth session.

### Wear-Remote-Interactions Version 1.0.0-alpha03

April 7, 2021

`androidx.wear:wear-remote-interactions:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..24330de8135d689b34a31a701181b20549e8db25/wear/wear-remote-interactions)

**API Changes**

- Changed `PlayStoreAvailability` to be a class that contains companion object with static methods. Usage stays the same.

**Bug Fixes**

- Fixed summary doc for `WatchFaceConfigIntentHelper` to correctly show sample code with actual HTML characters.

### Wear-Ongoing Wear-Phone-Interactions Version 1.0.0-alpha03

March 10, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha03` and `androidx.wear:wear-phone-interactions:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/wear)

**New Features**

- Migrate OAuthClient from Wearable Support Library to AndroidX. This migrated class is renamed to RemoteAuthClient and it gives support for remote authentication on Wearables together with support for adding OAuth PKCE extension. Additional handlers and helper classes for communication are provided.
- Ongoing activities can now be associated with a Notification that has a tag, using the new OngoingActivity.Builder constructor.

**API Changes**

- Added support for notification tags on the Ongoing Activities Library ([I653b4](https://android-review.googlesource.com/#/q/I653b41b716ff5b3d590a5be03e417be8dc01236c))
- Migrate OAuthClient from Wear Support Library to AndroidX, and add support for OAuth PKCE extension ([I3eaaa](https://android-review.googlesource.com/#/q/I3eaaa7dd09af837a0221400b3bea639ebb8dd215))

### Wear-Remote-Interactions Version 1.0.0-alpha02

March 10, 2021

`androidx.wear:wear-remote-interactions:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/wear/wear-remote-interactions)

**New Features**

- Migrating PlayStoreAvailability class from Wearable Support Library to AndroidX which provides an API for checking whether the Play Store is available on the Phone.

**Bug Fixes**

- Migrating PlayStoreAvailability class from Wearable Support Library to AndroidX. ([I69bfe](https://android-review.googlesource.com/#/q/I69bfe4354149947c8c3631e9e55d994597895e9e))

### Version 1.0.0-alpha02

February 10, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha02` and `androidx.wear:wear-phone-interactions:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/wear)

**API Changes**

- Added support for more complex status. They are composed of a template (or several) and a series of Parts that will be used to fill the template's placeholders. OngoingActivityStatus now has a static method to create simple statuses with only one part (a Text or a Timer), and a Builder to create more complex statuses. ([I1fe81](https://android-review.googlesource.com/#/q/I1fe818ee09171f618699cce0b5046bec0bc79e91))
- Move BridgingManager and BridgingConfig classes from Wear Support Library to AndroidX which provides APIs to enable/disable notifications at runtime and optionally set tags for notifications that are exempt from the bridging mode. ([I3a17e](https://android-review.googlesource.com/#/q/I3a17e9cf1db86b731b96f0ee0cd45b238aa3fcea))

### Version 1.0.0-alpha01

January 27, 2021

`androidx.wear:wear-ongoing:1.0.0-alpha01`, `androidx.wear:wear-phone-interactions:1.0.0-alpha01`, and `androidx.wear:wear-remote-interactions:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6/wear)

**API Changes**

- Migrate the Ongoing Activities library to a new sub-library: wear-ongoing. Classes now live in the androidx.wear.ongoing package (previously was androidx.wear.ongoingactivities) ([I7c029](https://android-review.googlesource.com/#/q/I7c02947659bbf33c9b66757001eccfa225f4168f))

- Create a new support library to contain classes that support interactions from the Wearables to Phones. It is initially populated with classes migrated from Wearable Support Library. ([Id5180](https://android-review.googlesource.com/#/q/Id5180d4583a60b92f66e06d4f208d8920b97dc28))

- Migrate PhoneDeviceType class from Wearable Support Library to AndroidX. The migrated class is renamed as PhoneTypeHelper which provides helper methods for determining the type of phone the current watch is paired to, for use on Wearable devices only. ([Ibd947](https://android-review.googlesource.com/#/q/Ibd9474f69e958c2efd31949609df6aeb7c7dc648))

- Create a new support library to contain classes that support interactions between the Wearables and Phones. It is initially populated with classes migrated from Wearable Support Library. ([I9deb4](https://android-review.googlesource.com/#/q/I9deb4cc773b550141b0f05aae44b3f7705fec532))

- Migrate WatchFaceCompanion class from Wearable Support Library to AndroidX. The migrated class is renamed as WatchFaceConfigIntentHelper which provides helper functions to specify the ID and component name in the watch face configuration activities in companion on the phone, it can also be used locally to configure the watch face on the wearable device. ([Ia455f](https://android-review.googlesource.com/#/q/Ia455f4dc525b7fba3425608ae5a12b05399c476e))

## Wear Complications and Watchface 1.0.0

> [!NOTE]
> **Note:** As of `1.0.0-alpha23`, the `watchface` and `complications` libraries have been moved to a unified `androidx.wear.watchface` group. Please see the [Wear Watchface](https://developer.android.com/jetpack/androidx/releases/wear-watchface) release note page for more details.

### Version 1.0.0-alpha22

September 15, 2021

`androidx.wear:wear-*:1.0.0-alpha22` is released. [Version 1.0.0-alpha22 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/wear)

**New Features**

- The EditorSession now subscribes to lifecycle observers so you no longer have to explicitly close it when your activity goes away.

**API Changes**

- EditorSession and ListenableEditorSession now use kotlin StateFlows for complicationSlotsState, ComplicationsPreviewData and ComplicationsDataSourceInfo. ([I761d9](https://android-review.googlesource.com/#/q/I761d9a3c1990281e9235bcea79dc80f6fa5b7d0c))
- EditorSession#userStyle is now a `MutableStateFlow<UserStyle>` ([I32ca9](https://android-review.googlesource.com/#/q/I32ca96636efc1e79152d456dd263dd6c1cd00f5f))
- EditorSession.createOnWatchEditorSession now uses a lifecycle observer and it automatically closes when it observes onDestroy. In addition `createOnWatchEditorSession` now only requires the activity to be passed in. Identical changes have also been applied to ListenableEditorSession. ([Ic6b7f](https://android-review.googlesource.com/#/q/Ic6b7f48691a97bd8ef9a417dc692febf3e318eb1))
- CustomValueUserStyleSetting's constructor has been reinstated as part of the public API. ([I2e69a](https://android-review.googlesource.com/#/q/I2e69a3f307a969435296ee9e649b13b174054dcc))
- `UserStyle` now inherits from `Map<UserStyleSetting, UserStyleSetting.Option>` and `MutableUserStyleSetting#put` throws IllegalArgumentException if the setting is not in the schema or if the option doesn't match the setting. ([Iba40f](https://android-review.googlesource.com/#/q/Iba40fe5b1906a0ae1b6f36f37939f5e498ea8e71))

### Version 1.0.0-alpha21

September 1, 2021

`androidx.wear:wear-*:1.0.0-alpha21` is released. [Version 1.0.0-alpha21 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..47e81d1c497b8a57534a460c277855db1b0257ae/wear)

**API Changes**

- All public watch face, client, editor and complication APIs now use java.time.Instant for times rather than a Long, as a consequence the minimum API level has increased to 26. ([I3cd48](https://android-review.googlesource.com/#/q/I3cd482ea3c80e6b88d28f9e33368b8f0e8e651c8))
- The watchface and complication APIs now use the immutable ZonedDateTime instead of Calendar. ([I25cf8](https://android-review.googlesource.com/#/q/I25cf828b22577fe838a8baf8eab591febb90c284))
- ComplicationSlots are now initialized with NoDataComplicationData, ComplicationSlot.complicationData now always has a value and CanvasComplicationDrawable.complicationData is no longer nullable. ([I4dfd6](https://android-review.googlesource.com/#/q/I4dfd6e996b84f3d6d664fce98bc8e6601d9298cd)) This reduces (but doesn't eliminate) complication flickering when switching between watch faces.

### Version 1.0.0-alpha20

August 18, 2021

`androidx.wear:wear-*:1.0.0-alpha20` is released. [Version 1.0.0-alpha20 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/wear)

**API Changes**

- We have added createFallbackPreviewData to ComplicationDataSourceInfo which can be used when ComplicationDataSourceInfoRetriever.retrievePreviewComplicationData returns null. ([I38c4d](https://android-review.googlesource.com/#/q/I38c4dc237d114b51234a4b8df6528280513e4843))
- ComplicationDataSourceUpdateRequester has been turned into an interface to allow mocking in unit tests. You can construct a concrete ComplicationDataSourceUpdateRequester with ComplicationDataSourceUpdateRequester.create(). ([I7da22](https://android-review.googlesource.com/#/q/I7da226172823e58d1d0c6140f96e39f9e8e7ece9))
- RenderParameters.pressedComplicationSlotIds has been replaced by RenderParameters.lastComplicationTapDownEvents which exposes the new TapEvent class which contains a triple of x, y coordinates of the tap in pixels and a time stamp. `WatchFace.TapListener.onTap` has been replaced by `onTapEvent(@TapType tapType: Int, tapEvent: TapEvent)`. In addition, `InteractiveWatchFaceClient.displayPressedAnimation` has been removed. ([Id87d2](https://android-review.googlesource.com/#/q/Id87d2f42f4e051d400bff931595309fb20dbf489))
- Added explicit threading annotation for setImportantForAccessibility ([I990fa](https://android-review.googlesource.com/#/q/I990faac25c6136591f97c8d4cdea0b3372f51af2))
- ComplicationSlotBoundsType has been moved to androidx-wear-watchface.ComplicationSlotBoundsType in wear/wear-watchface. ([I09420](https://android-review.googlesource.com/#/q/I09420017bd5d811cc59f428add4c6f3a1fd9353a))
- We have added support for passing string resource ids into UserStyleSetting and Options. This is now the recommended way to construct those objects. ([I03d5f](https://android-review.googlesource.com/#/q/I03d5f65e8ad15cfd361778242786f7b9b8830693))
- Limits have been imposed upon the maximum wire size of a UserStyle Schema. Also Icons in the schema must not be bigger than 400x400 pixels. ([I3b65b](https://android-review.googlesource.com/#/q/I3b65b34f5018b0f28ca86552b91fceefa136f659))
- We added a MutableUserStyle class to support changes to UserStyle instances ([I95a40](https://android-review.googlesource.com/#/q/I95a4097e1765c987b87f281c431ef64b2449cff7))
- We have renamed `ListenableWatchFaceMetadataClient.Companion#listenableCreateWatchFaceMetadataClient` to `ListenableWatchFaceMetadataClient.Companion#createListenableWatchFaceMetadataClient`. ([I64ce2](https://android-review.googlesource.com/#/q/I64ce21f528ffcbb1717749b14d27035202987309))
- We've modified EditorState.previewComplicationsData to only contain data for enabled complications, and we've added `EditorSession.DEFAULT_PREVIEW_TIME_MILLIS` which if passed to`renderWatchFaceToBitmap` or `PreviewScreenshotParams` requests rendering with the watch face's default preview time. ([If7b3c](https://android-review.googlesource.com/#/q/If7b3c08c2fc0bb70a3fb9ab5b2df8c6a86ff30d7))
- We have removed UserStyleSetting constructors taking CharSequence from the public API. It's recommended to use the constructors that require StringResource IDs instead. ([I8537b](https://android-review.googlesource.com/#/q/I8537b7c6842e2cdcda0ed9e5c562d35a527bdbc6))
- `CurrentUserStyleRepository.UserStyleChangeListener` now supports SAM conversion. ([I85989](https://android-review.googlesource.com/#/q/I8598927b8384af5b03b9b9e189c307d0901a3282))

### Version 1.0.0-alpha19

August 4, 2021

`androidx.wear:wear-*:1.0.0-alpha19` is released. [Version 1.0.0-alpha19 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/wear)

**API Changes**

- We've added `ListenableWatchFaceMetadataClient.listenableCreateWatchFaceMetadataClient` which provides a `ListenableFuture` wrapper for `WatchFaceMetadataClient.createWatchFaceMetadataClient`. ([I5fa37](https://android-review.googlesource.com/#/q/I5fa37e1f8b22279c5900b837a93b2e20f388a1fa))
- `UserStyleOption.getOptionForId` now accepts `UserStyleOption.Id` instead of a byte array. ([I469be](https://android-review.googlesource.com/#/q/I469bed315164f9b8f3c9dc847d426f3798389468))
- Provide constants `BooleanOption.TRUE` and `BooleanOption.FALSE` and disallow instance creation ([I46e09](https://android-review.googlesource.com/#/q/I46e096d6cc1d80a53e01f814ba337d57de8ba41b))
- Methods in wear-watchface-client that can throw RemoteException have now been annotated accordingly. ([Ib8438](https://android-review.googlesource.com/#/q/Ib8438ef3e1bb63051f3ce7a8bff0da5bb58839fe))
- For consistency we've renamed `EditorSession.createOnWatchEditingSession` to `createOnWatchEditorSession`, similarly `createHeadlessEditingSession` is now `createHeadlessEditorSession`. Their guava wrappers have also been renamed. ([I1526b](https://android-review.googlesource.com/#/q/I1526b764a598937eb0bc16dab2b32e35ce279cfc))
- `EditorSession` is now an interface and `ListenableEditorSession.commitChangesOnClose` is now properly delegated. ([I7dc3e](https://android-review.googlesource.com/#/q/I7dc3ef8eea4ae8f5f11ccef7086d2909763ad411))
- We now reject any user style schema that has settings or options with conflicting IDs ([Ic2715](https://android-review.googlesource.com/#/q/Ic27153688978dca2bd801b4d69af6296a2eb3b2c))
- We have added an overloaded `UserStyle.get` which accepts `UserStyleSetting.Id`. ([I2aa0f](https://android-review.googlesource.com/#/q/I2aa0ff7c6075a91436fe9b5a87f935a1356862e2))

### Version 1.0.0-alpha18

July 21, 2021

`androidx.wear:wear-*:1.0.0-alpha18` is released. [Version 1.0.0-alpha18 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear)

**API Changes**

- We moved `ComplicationHelperActivity` to `androidx.wear:wear-watchface` library. ([I39e76](https://android-review.googlesource.com/#/q/I39e76d0e26e7f56cba741a5a654176e0813ea424))
- For consistency and clarity, `ComplicationProvider` has been renamed to `ComplicationDataSource` and all classes with Provider in their name have been similarly renamed. ([Iaef0b](https://android-review.googlesource.com/#/q/Iaef0bf0ebfad43990f4cde8ff89048102a1c97bb))
- `CanvasComplication.isHighlighted` has been moved into `RenderParameters.pressedComplicationSlotIds` this is a step towards making `CanvasComplication` stateless. To support this change `CanvasComplication.render` now also takes the `slotId` as a parameter and we now pass the `ComplicationSlot` into `GlesTextureComplication`. ([I50e6e](https://android-review.googlesource.com/#/q/I50e6e600d10f512689b680404eda737595b7a5e8))
- We have added `headlessDeviceConfig` to `EditorRequest`, if non null this parameter is used to construct a headless instance to back the EditorSession rather than acting on the interactive instance. This allows the editor to be invoked for a watch face that isn't the current one. ([I0a820](https://android-review.googlesource.com/#/q/I0a8204d7ddd6fa8dac0e082877fc5c741ce1c26a))
- We've added an experimental `WatchFaceMetadataClient` which allows efficient retrieval of static watch face metadata such as the `UserStyleSchema` and fixed details about `ComplicationSlots`. ([I6bfdf](https://android-review.googlesource.com/#/q/I6bfdf94361b3b84eb5ac7313b44f748b186a3aae))
- We have renamed `CanvasRenderer.uiThreadInit` to init. ([I6fff9](https://android-review.googlesource.com/#/q/I6fff94f222fda71b99927fcfa7c8657682ba2868))
- We've added PreviewScreenshotParams an optional new parameter for EditorRequest which instructs EditorSession to take a preview screenshot on commit with these parameter. The preview image is exposed on `EditorState.previewImage`. ([Ic2c16](https://android-review.googlesource.com/#/q/Ic2c1668f05a5d7fb9c73ea75a44f7499c4a5999c))

**Bug Fixes**

- Developers no longer need to add ComplicationHelperActivity to their own manifest. ([I6f0c2](https://android-review.googlesource.com/#/q/I6f0c2af08d927095e6bacbad49724fc2c33a282d))

### Version 1.0.0-alpha17

June 30, 2021

`androidx.wear:wear-*:1.0.0-alpha17` is released. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..19ae3a88ff0824d615355b492cb56049e16991f2/wear)

**New Features**

- In `GlesRenderer`, `makeUiThreadContextCurrent` and `makeBackgroundThreadContextCurrent` have been replaced by `runUiThreadGlCommands` and `runBackgroundThreadGlCommands` which both accept a `Runnable`. The library ensures that only one GL command runnable is executing at any given time.

- To make UiThread initialziaion easier we've added `CanvasRenderer.uiThreadInit` which is called once on the UiThread before any calls to render. We've also added `onRendererCreated` to `CanvasComplication` which makes it easier for `Renderer` and `CanvasComplication` to share state.

- For clarity we have renamed `Complication` to `ComplicationSlot` and `complicationId` to either `complicationSlotId` or `complicationInstanceId` depending on usage

**API Changes**

- For clarity we have renamed `Complication` to `ComplicationSlot` and `complicationId` to either `complicationSlotId` or `complicationInstanceId` depending on usage. Classes using Complication have similarly been renamed e.g. ComplicationsManager is now called ComplicationSlotsManager. ([I4da44](https://android-review.googlesource.com/#/q/I4da44b7a9bf2d720ad241770f2b677a025d7a70e))
- In GlesRenderer `makeUiThreadContextCurrent` and `makeBackgroundThreadContextCurrent` have been replaced by `runUiThreadGlCommands` and `runBackgroundThreadGlCommands` which both accept a `Runnable`. These functions are only needed if you need to make GL calls outside of render, `runBackgroundThreadGlCommands` and `onUiThreadGlSurfaceCreated`. This is required because there can be multiple GlesRenderers each with their own contexts in the same process, potentially from different watch faces. In addition access to the shared current GL context is now synchronized. ([I04d59](https://android-review.googlesource.com/#/q/I04d5982e80126be3e3dc26423cdf0a5006a79cd2))
- We have added `CanvasRenderer.uiThreadInit` which is called once on the UiThread before any calls to render. Also for clarity in GlesRenderer we have renamed `onGlContextCreated` to `onBackgroundThreadGlContextCreated`, and `onGlSurfaceCreated` to `onUiThreadGlSurfaceCreated`. ([If86d0](https://android-review.googlesource.com/#/q/If86d04e0a7faadb7f177716d3b18a8b8c640642f))
- `HeadlessWatchFaceClient` \& `InteractiveWatchFaceClient` `getComplicationsSlotState` has been renamed to `getComplicationSlotsState`. In `ComplicationSlot`: `createRoundRectComplicationBuilder`, `createBackgroundComplicationBuilder`, and `createEdgeComplicationBuilder` have been renamed to `createRoundRectComplicationSlotBuilder`, `createBackgroundComplicationSlotBuilder`, and `createEdgeComplicationSlotBuilder` respectively. ([Ib9adc](https://android-review.googlesource.com/#/q/Ib9adca0b03b4f27684eb55cd4e8328e98350bd66))
- We have added onRendererCreated to CanvasComplication which makes it easier for Renderer and CanvasComplication to share state. ([I5e1ac](https://android-review.googlesource.com/#/q/I5e1ac34833d9fab1eb54caa8f8f51f49c4d856e3))

### Version 1.0.0-alpha16

June 16, 2021

`androidx.wear:wear-*:1.0.0-alpha16` is released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..ccf79f53033e665475116a4e78ff124df2a52c4b/wear)

**New Features**

- We've fixed a number of bugs related to the recent threading model changes as well as addressing other issues with the on watch face editor.

**Bug Fixes**

- Prevent NPE in `onComplicationProviderChooserResult` ([b/189594557](https://issuetracker.google.com/issues/189594557))
- Fix issues with stale surfaces and drawBlack ([b/189452267](https://issuetracker.google.com/issues/189452267))
- Fix race in accessing `complicationsManager.watchState` ([b/189457893](https://issuetracker.google.com/issues/189457893))
- Fix background thread lifetime bug ([b/189445428](https://issuetracker.google.com/issues/189445428))
- Fix Pre-R Watch face Editor issues ([b/189126313](https://issuetracker.google.com/issues/189126313))
- Don't update direct boot params for editor style changes ([b/187177307](https://issuetracker.google.com/issues/187177307))

### Version 1.0.0-alpha15

June 2, 2021

`androidx.wear:wear-*:1.0.0-alpha15` is released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/wear)

**New Features**

The majority of watch face initialization is now done on a background thread, however after loading all watch face rendering etc is done on the UiThread. There is a memory barrier between loading and rendering so most user watch faces don't need to do anything special. Watch faces using GLES may be an exception since the context is thread specific and we create two linked contexts so it's possible to upload GL resources (e.g. textures and shaders) on the background thread and use them on the UiThread.

We have split the construction of watchfaces into three functions: createUserStyleSchema, createComplicationsManager and createWatchFace. We assume that createUserStyleSchema and createComplicationsManager are fast and createWatchFace may take some time to load assets. Taking advantage of this we have introduced `WatchFaceControlClient.getDefaultProviderPoliciesAndType` which returns a map of Complication Ids to DefaultComplicationProviderPolicies and the default ComplicationType. This is faster than creating a headless instance since it doesn't need to fully initialize the watch face to perform the query.

Finally complications are now constructed with a CanvasComplicationFactory which allows for lazy construction of the CanvasComplication renderers.

**API Changes**

- Replaced `@TargetApi` with `@RequiresApi`. ([I0184a](https://android-review.googlesource.com/#/q/I0184a41bcc214a5033f431f969f36ab5b9c174ae), [b/187447093](https://issuetracker.google.com/issues/187447093), [b/187447094](https://issuetracker.google.com/issues/187447094))
- We have introduced `WatchFaceControlClient.getDefaultProviderPoliciesAndType` which returns a map of Complication Ids to DefaultComplicationProviderPolicies and the default ComplicationType. Where possible a fast path is used that avoids fully constructing a watch face. To facilitate this the WatchFaceService API has had to change with two new methods being: createUserStyleSchema and createComplicationsManager the results of which are passed into createWatchFace. In addition Complications are now constructed with a CanvasComplicationFactory which allows for lazy construction of the CanvasComplication renderers. ([Iad6c1](https://android-review.googlesource.com/#/q/Iad6c1414c4ff1792abaf2c60334fed74bd5b5686))
- We have removed MOST_RECENT_APP from SystemProviders. ([I3df00](https://android-review.googlesource.com/#/q/I3df00a615950bd4ee3e32bdfc8cb277e48c48b8c))
- ObservableWatchData is now a sealed class. ([Ic940d](https://android-review.googlesource.com/#/q/Ic940ddaaca3f411fdbcf83e701694e4dbf381064))
- CanvasComplicationFactory.create (which is typically io bound) is now called on a background thread for each complication before ui thread rendering commences. There is a memory barrier between construction and rendering so no special threading primitives are required. ([Ia18f2](https://android-review.googlesource.com/#/q/Ia18f25841808e4d6880b0f5187dd1cae85324861))
- Watchface construction is now done on a background thread although all rendering is done on the ui thread, GlesRenderer supports two linked contexts to support this. WatchFaceControlClient.createHeadlessWatchFaceClient and WatchFaceControlClient.getOrCreateInteractiveWatchFaceClient may resolve before WatchFaceService.createWatchFace has completed. Subsequent API calls will block until watchFace initialization has completed. ([Id9f41](https://android-review.googlesource.com/#/q/Id9f416e2dc57612386f7361778d47d496dd4a4e2))
- EXPANSION_DP and STROKE_WIDTH_DP are no longer visible in api.txt. ([I54801](https://android-review.googlesource.com/#/q/I54801fdcc7b0c5657568c9cc3508b5da96cb39d9))
- We have made EditorSession.createOnWatchEditingSession throw TimeoutCancellationException if there's an error instead of sending a null session. Additionally, the return value of EditorRequest.createFromIntent and EditorSession.createOnWatchEditingSession is now NonNull. ([I41eb4](https://android-review.googlesource.com/#/q/I41eb47cbe25cdc5e945752f20cba0a56f3bbce05))

### Version 1.0.0-alpha14

May 18, 2021

`androidx.wear:wear-*:1.0.0-alpha14` is released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/wear)

**New Features**

- `EditorSession.openComplicationProviderChooser` now returns ChosenComplicationProvider which contains the complication id, `ComplicationProviderInfo` and a Bundle containing any additional extras returned by the provider chooser.
- In addition we have been steadily migrating code to Kotlin and the majority of the watch face API is now defined in Kotlin.

**API Changes**

- GlesRenderer properties `eglContext` and `eglDisplay` are now non-nullable. Any GL errors are now reported via `GlesRenderer.GlesException` rather than via RuntimeExceptions. ([Ib1005](https://android-review.googlesource.com/#/q/Ib100510722daafabdb37b3d32aefc79824917c57))
- We have migrated `androidx.wear.watchface.complications.rendering.ComplicationDrawable` from Java to Kotlin ([Ibc3eb](https://android-review.googlesource.com/#/q/Ibc3eb9084e8bf9b6261fc54a227898c587c200c6))
- We have migrated `androidx.wear.watchface.complications.rendering.ComplicationStyle` from Java to Kotlin ([I3375e](https://android-review.googlesource.com/#/q/I3375e0cda465c9fb52a993465f7e717e1fd2cf0a))
- We added information about the complication provider for each complication within EditorSession. ([I37f14](https://android-review.googlesource.com/#/q/I37f14f4867c495bfd9b67d9e32318e5a78eb33c7))
- We extended the result of `EditorSession.openComplicationProviderChooser` to include information returned by the chosen. ([Iead6d](https://android-review.googlesource.com/#/q/Iead6d1a7a7c64aeb4dd3d8d6f49a54b26c8f9c6a))

### Wear Complications \& Watchface Version 1.0.0-alpha13

May 5, 2021

`androidx.wear:wear-*:1.0.0-alpha13` is released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ddfc1583c09aaa878d34437fbfee1b995b60d3a..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/wear)

**New Features**

- Watch faces can have important visual elements beyond showing the time and complications. To provide screen reader support for this, watchface can now specify accessibility ContentDescriptionLabels via the Renderer's additionalContentDescriptionLabels property. In addition, to control the ordering of ContentDescriptionLabels accessibilityTraversalIndex has been added to complications. This can be modified by a ComplicationsUserStyleSetting.

- To encourage developers to carefully consider screen readers we have made `ShortTextComplicationData.Builder`'s, `LongTextComplicationData.Builder`'s and `RangedValueComplicationData.Builder`'s `contentDescription` field mandatory to be passed into their constructors. If `ComplicationText.EMPTY` is passed in for the `contentDescription`, a `contentDescription` will be automatically generated from the text and title.

- `WatchFaceControlClient.getOrCreateInteractiveWatchFaceClient` now throws `ServiceStartFailureException` if the watchface throws an exception during init, this makes it much easier to diagnose issues during watch face startup.

**API Changes**

- We added support for having a null component name in ComplicationProviderInfo, which is needed to support older versions of Wear OS. ([I744d2](https://android-review.googlesource.com/#/q/I744d23cebf1d658c0066d63f4b989a078dc828f9))
- We have migrated `androidx.wear.complications.SystemProviders` from Java to Kotlin. ([Ia1f8b](https://android-review.googlesource.com/#/q/Ia1f8bd1a6ed1e129b0fcc469781aa06a7f03dc90))
- We have hidden all classes from public API that are in android.support.wearable.complications and created corresponding wrappers in AndroidX where needed. ([I7bd50](https://android-review.googlesource.com/#/q/I7bd50e3bd368ae14883ad2c4802404a1c424ab3f))
- We have renamed method in `TimeDifferenceComplicationText.Builder` from `setMinimumUnit` to `setMinimalTimeUnit`. ([I20c64](https://android-review.googlesource.com/#/q/I20c64730819afd73e0bc0531315565d31ea21ada))
- We have made `ShortTextComplicationData.Builder`'s, `LongTextComplicationData.Builder`'s and `RangedValueComplicationData.Builder`'s `contentDescription` field mandatory to be passed in constructor. ([I8cb69](https://android-review.googlesource.com/#/q/I8cb69eb4bf900fb76eae8d2bb39af1297d490b6f))
- We have renamed ComplicationProviderService.onComplicationUpdate to onComplicationRequest and encapsulated id and type parameter of this method into data ComplicationRequest. Corresponding listener has been renamed to ComplicationRequestListener and its method ComplicationRequestListener.onComplicationData. ([Iaf146](https://android-review.googlesource.com/#/q/Iaf146c9495ce65ec8a3a13908979bc79277da6d8))
- We have removed method `isActiveAt` from `ComplicationData` and exposed field `validTimeRange` instead of it. This method call can be replaced with `validTimeRange.contains`. ([I65936](https://android-review.googlesource.com/#/q/I65936f9b3b4d6c2acf3f64be2773e92600e55d9c))
- We have changed description of the method ComplicationProviderService.onComplicationActivated to receive a ComplicationType instead of an int. ([Idb5ff](https://android-review.googlesource.com/#/q/Idb5ffd58898956aba178505c0791c434fcea9239))
- Migrated ProviderUpdateRequester from Java to Koltin. ([Ibce13](https://android-review.googlesource.com/#/q/Ibce13d8a9e244164640ade18afccf3e80af31250))
- GlesRender.makeContextCurrent is now public. Watch face code may need to make gl calls outside of render and onGlContextCreated and because there may be both an interactive and a headless context its necessary to call this. ([I8a43c](https://android-review.googlesource.com/#/q/I8a43ce92884892b6131c0b1fe2e08019c9f38fa1))
- WatchFaceControlClient.getOrCreateInteractiveWatchFaceClient now throws ServiceStartFailureException if the watchface throws during init. In addition WatchFaceService now throws an exception if createWatchFace takes longer than 6 seconds. ([I59b2f](https://android-review.googlesource.com/#/q/I59b2f354e62a71eea1b4b4d5da9309e3968b3b2e))
- We have removed the unused id property of `GlesTextureComplication`. ([I28958](https://android-review.googlesource.com/#/q/I28958350f962380a962b520425ae6e5d3acc5536))
- The watchface can now specify accessibility ContentDescriptionLabels via the `Renderer`'s additionalContentDescriptionLabels property. In addition to controlling the ordering of ContentDescriptionLabels accessibilityTraversalIndex has been added to complications. This can be modified by a ComplicationsUserStyleSetting. ([Ib7362](https://android-review.googlesource.com/#/q/Ib7362def16d52e924f7db5fdcfedb000683e7103))
- Expand documentation about touch event handling in the watch face. ([Iaf31e](https://android-review.googlesource.com/#/q/Iaf31ef431003a29c90228fc1866ef85e2651be55))

**Bug Fixes**

- `EditorSession.getComplicationsPreviewData()` now returns a map for every rather only non-empty complications. An instance of EmptyComplicationData is used for empty complications. ([I1ef7e](https://android-review.googlesource.com/#/q/I1ef7e9c1c9919a3103e83fdfb4f3c005962287db))

### Wear Complications \& Watchface Version 1.0.0-alpha12

April 21, 2021

`androidx.wear:wear-*:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25..4ddfc1583c09aaa878d34437fbfee1b995b60d3a/wear)

**New Features**

Watch face editors need to highlight parts of the watch face to help convery which aspect of a watch is being configured. We've extended RenderParameters to allow styles as well as complications to be highlighted. There's a new optional HighlightLayer which is intended to be matted on top of the watch face with alpha transparency (the screenshot apis can do this matting for you, or provide the HighlightLayer on its own for maximum flexibility). E.g. suppose you had a style that lets you configure the appearance of the watch hands, your renderer in its renderHighlightLayer can draw an outline around them.

To encourage Complication Provider support for accessibility we have made PhotoImageComplicationData.Builder's, MonochromaticImageComplicationData.Builder's and
SmallImageComplicationData.Builder's contentDescription field to be a mandatory constructor argument.
ComplicationTapFilter and Complication.createEdgeComplicationBuilder have been added to support edge complications (drawn around the edge of the screen). Rendering and hit testing of edge complications is left up to the watch face. Edge hit testing isn't supported from the companion editor.

**API Changes**

- Added `PROVIDER_` prefix to constants in SystemProviders. ([I1e773](https://android-review.googlesource.com/#/q/I1e77397a99f7d2051dc0a0467c37eeb4ecb38428))
- We have made `PhotoImageComplicationData.Builder`'s, `MonochromaticImageComplicationData.Builder`'s and `SmallImageComplicationData.Builder`'s `contentDescription` field mandatory to be passed in constructor. ([I9643a](https://android-review.googlesource.com/#/q/I9643a7aa0ce3033716e2221462f8cfbe590ceaf5))
- `ProviderInfoRetriever.requestPreviewComplicationData` has been renamed to `retrievePreviewComplicationData`. ([I911ee](https://android-review.googlesource.com/#/q/I911ee7c3209007628d9ad0536be5b2f3ffc08abb))
- Migrated `ComplicationProviderService` from Java to Koltin. ([I849f2](https://android-review.googlesource.com/#/q/I849f2d505096682acb71c10d8e28bb991b3d9c0c))
- Method `ComplicationProviderService.onBind` is now final ([I39af5](https://android-review.googlesource.com/#/q/I39af51b7ab16c4d75314899c72bb805e475131cb))
- We've reinstated interface `CanvasComplication` and moved `CanvasComplicaitonDrawable`, `GlesTextureComplication` and `ComplicationHighlightRenderer` to `wear-watchface-complications-rendering`. ([I84670](https://android-review.googlesource.com/#/q/I8467022e6958f6d1d6aadb6e8edf0cdd948bb1ae))
- `RenderParameters` has been refactored to support extended highlight rendering. It's now possible to request rendering of highlights for styles as well as all or a single complication. In addition CanvasRenderer and GlesRenderer how have a new abstract renderHighlightLayer method for rendering any highlighting requested by the editor. Layer has been renamed to WatchFaceLayer. ([Ic2444](https://android-review.googlesource.com/#/q/Ic24444dc23aa6e0ed9075d88ae92f167102a1791))
- `ComplicationTapFilter` and `Complication.createEdgeComplicationBuilder` have been added to support edge complications. Rendering and hit testing of edge complications is left up to the watch face. Hit testing isn't supported from within editors. ([Ia6604](https://android-review.googlesource.com/#/q/Ia6604405b67d1004314b143c7a767a0624a1ff3b))
- For `DoubleRangeUserStyleSetting` \& `LongRangeUserStyleSetting`: `defaultValue`, `maximumValue` and `minimumValue` are now kotlin properties. In addition, `UserStyleSetting.Option` functions like toBooleanOption, toCoplicationOptions, toListOption and similar have been removed. ([I52899](https://android-review.googlesource.com/#/q/I52899a374e0f5c4bf164c3b3a0ccc3d5d69b96e1))
- Add chin size to the properties of the device available to the watch face. ([I76e1e](https://android-review.googlesource.com/#/q/I76e1e578f0f32372ba8e540ac0b158b88ff92ba0))
- `ComplicationHighlightRenderer`'s constructor now accepts `outlineExpansion` and `outlineStrokeWidth` parameters. ([I87009](https://android-review.googlesource.com/#/q/I87009b21512d77fd861999420674f428987df36e))
- `ComplicationDrawable.getNoDataText` is now part of the public API. ([I00598](https://android-review.googlesource.com/#/q/I00598f90e553549698c67ea4b699b7fb54d6f70f))

### Version 1.0.0-alpha11

April 7, 2021

`androidx.wear:wear-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..24330de8135d689b34a31a701181b20549e8db25/wear)

**New Features**

- More polish has been applied to the watch face APIs. Most of the changes are simple renamings but `InteractiveWatchFaceWcsClient` and `InteractiveWatchFaceSysUiClient` have been merged into `InteractiveWatchFaceClient`.

**API Changes**

- ContentDescriptionLabel.text is now a ComplicationText rather than the old wearable support library TimeDependentText. ([I80c03](https://android-review.googlesource.com/#/q/I80c03a2ce3092e7c571df230515c8ed8121fe4e1))
- `SystemProviders.GOOGLE_PAY` is not guaranteed to be present on all Android R devices so it has been removed from the list. It's still possible to use this provider via `DefaultComplicationProviderPolicy` ([If01b5](https://android-review.googlesource.com/#/q/If01b508bf26e1537da0f6a47f535a38a9d0c85be))
- We've renamed ComplicationUpdateCallback to ComplicationUpdateListener for consistency. ([I61ec7](https://android-review.googlesource.com/#/q/I61ec7b97abae1fbb590453dcfd1e6d323c4e3dcb))
- The UserStyle wire format map has been changed to `Map<String, byte[]>` and for convenience a `UserStyleData` class has been added to the public API and is now used by wear-watchface-client and wear-watchface-editor. In addition CustomValueUserStyleSetting.CustomValueOption.value is now `byte[]` instead of `String`. ([Iaa103](https://android-review.googlesource.com/#/q/Iaa103736ab143ef4f6303db2529d416b4a28b1ca))
- `UserStyleSetting` and `UserStyleSetting.Option` now use `UserStyleSetting.Id` and `UserStyleSetting.Option.Id` respectively to store their ids rather than a String. ([I63f72](https://android-review.googlesource.com/#/q/I63f722e8ae9814892bb238007c498f22f5fcfbb4))
- `InteractiveWatchFaceClient.SystemState` has been renamed to `WatchUiState`. ([I6a4e0](https://android-review.googlesource.com/#/q/I6a4e0f8fd3811cdd22bd0b58f0e97accee3b3e0d))
- `InteractiveWatchFaceWcsClient` and `InteractiveWatchFaceSysUiClient` have been merged because it was hard to explain the division of responsibility ([Iff3fa](https://android-review.googlesource.com/#/q/Iff3fa02c0a40a9ae8ac2696a1ba76cd06273d311))
- Layer enum values have been renamed for clarity. `Layer#TOP_LAYER` is now `Layer#COMPLICATIONS_OVERLAY` and `Layer#BASE_LAYER` is now `Layer#BASE` ([Ia144e](https://android-review.googlesource.com/#/q/Ia144eca1c93fb57841e47e396cc442b86f5b2b0a))
- `UserStyleListener` has been renamed to `UserStyleChangeListener` ([I18524](https://android-review.googlesource.com/#/q/I185243bbd2723439457e75f78b3e145f1f1854a0))
- `UserStyleRepository` has been renamed to `CurrentUserStyleRepository` ([I6ea53](https://android-review.googlesource.com/#/q/I6ea531f4e0c9cdce6125ecf661c8548c4cb870e8))
- `InteractiveWatchFaceWcsClient.updateInstance` has been renamed to `updateWatchfaceInstance`. ([I321dc](https://android-review.googlesource.com/#/q/I321dc89e3b46d523245c76080b9491657834bcca))
- WatchFace TapType events have been renamed to align with MotionEvents / Compose. ([I0dfd0](https://android-review.googlesource.com/#/q/I0dfd0d1f55f13d583c2383aaee5775aa5446a8ff))
- takeWatchfaceScreenshot has been renamed to renderWatchFaceToBitmap, and takeComplicationScreenshot has been renamed to renderComplicationToBitmap ([Ie0697](https://android-review.googlesource.com/#/q/Ie0697af81b3b9aca215b8916c64e7bfd3c24b2e3))
- The CanvasComplication interface has been removed in favor of the open class CanvasComplicationDrawable. ([I1f81f](https://android-review.googlesource.com/#/q/I1f81f33d4bf34b69d9014676e9b467c4dae6cd18))
- `WatcfaceControlServiceFactory` has been removed from the public api. ([I1f8d3](https://android-review.googlesource.com/#/q/I1f8d3c6c8be716b9b5316f7197ce032b7b7b3ad9))
- We've renamed `CanvasComplication.setData` to `CanvasComplication.loadData`. ([If1239](https://android-review.googlesource.com/#/q/If1239a257d3cfad2abcba02a246461993ac69426))
- `ComplicationsManager.bringAttentionToComplication` has been renamed to `displayPressedAnimation`. ([Ic4297](https://android-review.googlesource.com/#/q/Ic4297c90db7536b0fc07f61588b217bfe4beae25))
- `WatchFaceService.createWatchFace` now has an `@UiThread` annotation. ([Ib54c2](https://android-review.googlesource.com/#/q/Ib54c292a1a50031544b934644039bd1de0966575))
- Changed the name of a CanvasComplicationDrawable parameter to fix a bug. ([I50dac](https://android-review.googlesource.com/#/q/I50dac9dd98c1461e44427134813d1866f1476f94))
- We've added `HeadlessWatchFaceClient.toBundle()` and `HeadlessWatchFaceClient.createFromBundle` to support sending `HeadlessWatchFaceClient` over AIDL. ([I07c35](https://android-review.googlesource.com/#/q/I07c35ca36d0ecae0c8e0b8cd926b38c602b2d9d8))
- HeadlessWatchFaceClient and InteractiveWatchFaceClient now have ClientDisconnectListener and isConnectionAlive() to allow you to observe if the connection is broken for some reason (e.g. the watchface being killed). ([Ie446d](https://android-review.googlesource.com/#/q/Ie446d8b50110c9d2992378ff8d8642707db7d2d1))
- `WatchFaceControlClient#getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClientAsync` is now a suspend function and has been renamed to `getOrCreateInteractiveWatchFaceClient`. ([Ib745d](https://android-review.googlesource.com/#/q/Ib745d13d911ffbb90d3cf9a961e469143fe8aaef))
- `EditorState.commitChanges` and `hasCommitChanges()` has been renamed to `shouldCommitChanges()`. ([I06e04](https://android-review.googlesource.com/#/q/I06e0407f2473e7884145ed418b9438b93017ecfd))
- `previewComplicationData` has been renamed to `previewComplicationsData` to indicate theres (usually) more than one complication in the map. ([I56c06](https://android-review.googlesource.com/#/q/I56c062bffef9d922a95abf8f2015cf716b105211))
- `InteractiveWatchFaceWcsClient.bringAttentionToComplication` has been renamed to `displayPressedAnimation` for consistency with `ComplicationsManager.displayPressedAnimation`. ([Ic9999](https://android-review.googlesource.com/#/q/Ic9999c10a88f44faf88e186bc4437056575e6605))
- All instances of watchface instance id have been encapsulated in a new WatchFaceId class ([I45fdf](https://android-review.googlesource.com/#/q/I45fdf4b8e7a0b1ac7262856191bcb021fb2dd911))
- `complicationState` property has been renamed to `complicationsState` to indicate plurality. ([Ided07](https://android-review.googlesource.com/#/q/Ided07073723d9115dedd9b37f2327e4c36893e0c))
- We've removed the various wear-watchface-client Binder conversions, they should be necessary. ([Icc4c0](https://android-review.googlesource.com/#/q/Icc4c02ef623b142b7d5d2a7fed86b2bb4930d7a4))
- For consistency `EditorServiceClient` has been refactored to use listeners instead of observers. ([Iec3a4](https://android-review.googlesource.com/#/q/Iec3a437e9583fbd7ca0835a2068cc306d6fa49f1))
- We've added a couple of missing `@Px` annotations to `InteractiveWatchFaceSysUiClient` and `WatchFaceControlClient`. ([I3277a](https://android-review.googlesource.com/#/q/I3277a824046ea85c10439e02df89dbb6b842d7a5))
- Renamed EditorObserverCallback to EditorObserverListener for consistency. ([Ie572d](https://android-review.googlesource.com/#/q/Ie572d57d0075f83219f721f76fc93b8860439f17))
- EditorState.watchFaceInstanceId is restricted to Android R API level and above and is no longer nullable. ([Id52bb](https://android-review.googlesource.com/#/q/Id52bb6d9ebc1d92cbff2deeda788f54e58e75113))
- `EditorSession.launchComplicationProviderChooser` has been renamed to `openComplicationProviderChooser`. ([I9d441](https://android-review.googlesource.com/#/q/I9d441b6cc55549a73832f38194180d9c6c6ddd14))
- `EditorSession.createOnWatchEditingSessionAsync` has been renamed to `createOnWatchEditingSession` and is now a suspend function. ([Id257b](https://android-review.googlesource.com/#/q/Id257baf80bca3fa8f97aa106684444e41f35fd5d))
- Added several missing `@UiThread` annotations on `EditorSession`. ([I6935c](https://android-review.googlesource.com/#/q/I6935ce9865b194764437c77b305d20f875b66806))
- `UserStyleSetting.affectsLayers` has been renamed to `affectedLayers`. ([I6e22b](https://android-review.googlesource.com/#/q/I6e22bf8a630776c9ca8f30c5214e9f4224999b0d))

### Version 1.0.0-alpha10

March 24, 2021

`androidx.wear:wear-*:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/wear)

**New Features**

- It's now possible to create open gl objects (e.g. textures) during WatchFaceService.createWatchFace because GlesRenderer now requires an explicit call to initOpenGLContext which can be done inside createWatchFace.

**API Changes**

- `IdAndComplicationData` was a bit awkward and has been removed from the public API. Classes \& interfaces that used it have been refactored. ([I4c928](https://android-review.googlesource.com/#/q/I4c92843bda1adcaeab5b1db692ae71b9ebc1353f))
- We've replaced `ReferenceTime` with `CountUpTimeReference` and `CountDownTimeReference` which are more self explanatory. ([Ib66c6](https://android-review.googlesource.com/#/q/Ib66c634425f70816b3762ab1f64a993cfe633581))
- Added some missing `@Px` and `@ColorInt` annotations. ([I9bbc3](https://android-review.googlesource.com/#/q/I9bbc3031af93f9bb09ffd5aad4751bb5d487aa3e))
- `Complication.complicationConfigExtras` is now non-nullable and defaults to `Bundle.EMPTY`. ([Iad04f](https://android-review.googlesource.com/#/q/Iad04f911e5e612373bda6ab10f2c7874800e92d4))
- `GlesRenderer` now requires you to call `initOpenGLContext` after construction. This function was an internal detail but is now on the public API to allow GL calls earlier inside createWatchFace. ([I726c2](https://android-review.googlesource.com/#/q/I726c279f6e7ae6185b1a446c0e314c4286673d1f))
- We've removed `Complication.setRenderer` as it should not be needed. ([Ie992f](https://android-review.googlesource.com/#/q/Ie992fabad06e17527b17a3b9a258615d6404849e))
- `Complicaiton.setComplicationBounds` is no longer part of the public API. If you need to adjust the position of a complication, this can be done via `ComplicationsUserStyleSetting`. ([Ibd9e5](https://android-review.googlesource.com/#/q/Ibd9e5f1f8d44f5ab4c8842e5117fa5aebb2fef7e))
- `ComplicationsManager.TapCallback.onComplicationSingleTapped` has been renamed to `onComplicationTapped`. ([I3a55c](https://android-review.googlesource.com/#/q/I3a55cf884e7c4f7899774975ff02811a8fd1c967))
- `ComplicationOutlineRenderer.drawComplicationSelectOutline` has been renamed to `drawComplicationOutline`. ([I14b88](https://android-review.googlesource.com/#/q/I14b8857a5903560b22379f2e383368b0b00d0830))

### Version 1.0.0-alpha09

March 10, 2021

`androidx.wear:wear-complications-*:1.0.0-alpha09` and `androidx.wear:wear-watchface-*:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/wear)

**New Features**

- The interface between WCS/SysUI host and the on watch face has evolved. It's now possible for an editor to determine if a style change will enable or disable a complication (enabled = initiallyEnabled plus any override from ComplicationsUserStyleSetting). Also `EditorService.closeEditor`allows SysUI to remotely close an on watch face editor if needed.
- In addition `InteractiveWatchFaceWcsClient.setUserStyle` with a more powerful command `updateInstance` which: changes the instance ID, sets the style, and clears complications all in one go.

**API Changes**

- TraceEvents have been added to the watchface libraries. ([I1a141](https://android-review.googlesource.com/#/q/I1a1417e576e9c871cab63c4eb6a0fc60e82842a6))
- `ComplicationState` now has a new property `initiallyEnabled` which is useful for predicting the consequences of switching styles. ([I8c905](https://android-review.googlesource.com/#/q/I8c9052560ad5b68d88d3e2b05255017ea7087a2f))
- We've replaced `InteractiveWatchFaceWcsClient.setUserStyle` with a more powerful command `updateInstance` which: changes the instance ID, sets the style, and clears complications. ([Ife6f6](https://android-review.googlesource.com/#/q/Ife6f658e8d86d85f986d66d52e00d84d1884cd19))
- WatchFaceClient screenshot APIs no longer compress the screenshots because that was slow, instead we leave any post processing up to the caller. ([Id35af](https://android-review.googlesource.com/#/q/Id35af41e21a27ce412542f8bbb40a66991695d26))
- It's now possible to remotely close an on watchface editor via `EditorService.closeEditor`. ([Ic5aa4](https://android-review.googlesource.com/#/q/Ic5aa4a1ac99cff2303a2116007b68dae18a4c579))
- Added nullability annotations ([Ic16ed](https://android-review.googlesource.com/#/q/Ic16ed43e46dfd51803d40e6332b0cf34467aaf7c))

### Version 1.0.0-alpha08

February 24, 2021

`androidx.wear:wear-*:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..5c90131a69042a6a3e13952e1da9e7ffc571c31d/wear)

**New Features**

- Some watch faces are designed around one or more specific complications, to support this we've added Complication.Builder#setFixedComplicationProvider which if set to true prevents the user from changing the complication in that slot.
- The watchface libraries are Kotlin first and use coroutines (e.g. suspend functions). For Java users we've provided ListenableFuture wrappers to improve interoperability in the following libraries: wear/wear-watchface-guava, wear/wear-watchface-client-guava \& wear/wear-watchface-editor-guava.

**API Changes**

- We've removed support for double taps on complications launching the provider chooser, this feature wasn't common in watchfaces and complicated the implementation of SysUI. ([I3ef24](https://android-review.googlesource.com/#/q/I3ef24322bbbb76a6a441954b7c31342966567ed2))
- ProviderInfoRetriever methods may throw ServiceDisconnectedException if the binder closes unexpectedly. ([Ib2cc4](https://android-review.googlesource.com/#/q/Ib2cc462394e39b42e28d6e1d0af911d67923563b))
- From Android 11 onwards, there are restrictions on when the ProviderChooser can be run, in addition we'd like editors to be built with the new `wear-watchface-editor` so ComplicationHelperActivity is being removed from the public API. ([Ib19c1](https://android-review.googlesource.com/#/q/Ib19c1b175b8927432b834465c0689641d371d6f9))
- Remove ComplicationText static methods in favor of builders. ([Ibe399](https://android-review.googlesource.com/#/q/Ibe3992ba05ac2abbc7be71a7c473eec173996d9f))
- We have introduced guava ListenableFuture wrappers for the various watch face library suspended methods. ([I16b2c](https://android-review.googlesource.com/#/q/I16b2c5ed3c54db97661dd2e94288e0e18e21a443))
- For API clarity we've added a secondary constructor to RenderParameters which doesn't require a tint, for use with LayerModes other than `LayerMode.DRAW_OUTLINED`. ([I497ea](https://android-review.googlesource.com/#/q/I497ea29cb4671fd2082eaca66d18ff36068f639c))
- Previously ListUserStyleSetting was different from the other because it had a default argument. Now all the StyleSetting subclass constructors take the default value last. ([I9dbfd](https://android-review.googlesource.com/#/q/I9dbfdb05d8dd7fe96c43f870d92843020370c3dd))
- CanvasComplication has been refactored to use have a hidden method, which makes it easier to implement a subclass ([I5b321](https://android-review.googlesource.com/#/q/I5b32176f98042a1b6affda73e492bdd25fa7d774))
- We have refactored away EditorResult in favor of a new EditorService and `EditorSession.broadcastState()` to stream updates to an observer (typically SysUI). ([Ic4370](https://android-review.googlesource.com/#/q/Ic4370d0f48b622a5ecf4c9424ec1fe9f988dcd39))
- Some watchfaces are built around a particular complication as an integral part of the watch face where the provider is not user configurable. To support this we've added `Complication.Builder#setFixedComplicationProvider`. ([I4509e](https://android-review.googlesource.com/#/q/I4509e9a0fbfe08d6614c9b684c216200fc0d772e))
- EditorRequest now specifies package name rather than ComponentName because it was inconvenient for SysUI to look up the class name of the editor, and we only really need the package name. ([Ib6814](https://android-review.googlesource.com/#/q/Ib68146df783dca74b2944d60fa5e5a762a2348d9))

### Version 1.0.0-alpha07

February 10, 2021

`androidx.wear:wear-*:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/wear)

**New Features**

- WatchFaceService.createWatchFace is now a suspend function which means the watchface no longer has to block the ui thread while waiting for IO. Similarly wear-watchface-editor and wear-complications-data

**API Changes**

- Remove PhotoImage class and use Icon directly. ([I8a70b](https://android-review.googlesource.com/#/q/I8a70b11af7fbee3a535e32a083749423d2f221da))
- Expose the validTimeRange of ComplicationData. ([I91366](https://android-review.googlesource.com/#/q/I91366d280466c1139b02cae4ed53b32a53ca5446))
- Make image-like attributes more explicit. ([I81700](https://android-review.googlesource.com/#/q/I81700dba61c3823861d1cca65fa2de69c6b475fd))
- wear-watchface-editor and wear-complications-data have been refactored to use suspend functions instead of coroutines. Rx java \& Future compat wrappers to follow. ([If3c5f](https://android-review.googlesource.com/#/q/If3c5ffa64e04406c4ebeadbffa8f5bc2a42aaaf2))
- ProviderInfoRetriever now now throws PreviewNotAvailableException if requestPreviewComplicationData can't return preview data due to connection issues or lack of API support. ([I4964d](https://android-review.googlesource.com/#/q/I4964df460dce91563e075241cb09843297219463))
- WatchFaceControlService::createWatchFaceControlClient is now a suspended fuction and getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClient is now called getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClientAsync returning `Deferred<InteractiveWatchFaceWcsClient>`. RX java and Future compat wrappers to follow. ([I5d461](https://android-review.googlesource.com/#/q/I5d4613786239ad2a15b16eed86fdee56029a0da6))
- Rename `CATEGORY_PROVIDER_CONFIG_ACTION` to `CATEGORY_PROVIDER_CONFIG`. ([I7c068](https://android-review.googlesource.com/#/q/I7c0689956ef6533ed3ac16edcc0487038cc96a55))
- Please note createOnWatchEditingSession is now a suspended function because the watchface sometimes isn't available until shortly after the editor activity has started. ([Ida9aa](https://android-review.googlesource.com/#/q/Ida9aa6ee3801b9ff79f64966340fdf485f1af389))
- WatchFaceService.createWatchFace is now a suspend function which allows for async initialization, previously you would have had to block the main thread. ([If076a](https://android-review.googlesource.com/#/q/If076aca5c94aaf20d8feae835c2833954368c27c))
- UserStyle now has an array operator and we've added casting helpers to UserStyle.Option. ([I35036](https://android-review.googlesource.com/#/q/I35036a0d62b14cda9e7c12fb55a256ed279af432))
- We've fixed a marshalling bug with UserStyle wireformats changing some of the unstable hidden API. ([I8be09](https://android-review.googlesource.com/#/q/I8be0900af78624868d3d7fbaeac0e7752d5beda1))
- We've added CustomValueUserStyleSetting which lets you store a single application specific string within a UserStyle. The default watch face editors will ignore this value. ([Ic04d2](https://android-review.googlesource.com/#/q/Ic04d2d56b0337d87e53926ad58065ca68aaa174f))
- InstanceID is not passed in the intent extras for R and older versions of Android WearOS which we can't upgrade. To support this we now allow InstancID to be null. ([Id8b78](https://android-review.googlesource.com/#/q/Id8b787fcdbbef1c26d79c4ea772786fd40eb073e))
- EditorRequest now includes the editor ComponentName which is set as the component in WatchFaceEditorContract.createIntent ([I3cd06](https://android-review.googlesource.com/#/q/I3cd0643327544771cc3b4278cc153736d4e2fb83))
- The watchface EditorResult now includes preview ComplicationData to allow the caller to take a screenshot of the watchface after editing. ([I2c561](https://android-review.googlesource.com/#/q/I2c561066ca91aa08c3450beaf88f18c5e9580fc6))

**Bug Fixes**

- Added toString() overrides to UserStyle, UserStyleSetting and UserStyleSchema which makes working with these classes a bit nicer. ([I9f5ec](https://android-review.googlesource.com/#/q/I9f5ec3339dbf6793c2c9c67f96467cc6cc227a04))

### Version 1.0.0-alpha06

January 27, 2021

`androidx.wear:wear-*:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..aee18b103203a91ee89df91f0af5df2ecff356d6/wear)

**New Features**

- We've introduced a new library wear/wear-watchface-editor which allows watch face developers and potentially OEMs to build a style and complication editor. SysUI will send an Intent to the watch face which will use the new EditorSession class to access WatchFace details and record the result via Activity.setWatchRequestResult. To support this we've added ProviderInfoRetriever.requestPreviewComplicationData which allows watch face editors to request preview ComplicationData. The advantage of preview ComplicationData is unlike live data you don't have to worry about showing permission dialogs when rendering your editor (note if a user selects a provider with a permission they will still be prompted to grant the permission).

**API Changes**

- ComplicationProviderInfo now has a field for the provider's ComponentName, support for this field will be added to WearOS at a later date and in the meantime, it will be null. ([Id8fc4](https://android-review.googlesource.com/#/q/Id8fc4130844dab52c7398354398a5267d6dbfea2))
- We've added ProviderInfoRetriever.requestPreviewComplicationData which allows watch face editors to request preview ComplicationData. This is useful because live complications may require permissions and you can now display preview data for complications that are not active. ([I2e1df](https://android-review.googlesource.com/#/q/I2e1df39373278a35db757823ddf1533ccb3623e2))
- ComplicationManager is now an optional parameter of WatchFace constructor and the arguments have been reordered to allow this. ([I66c76](https://android-review.googlesource.com/#/q/I66c76f8cd44b5766e6ad980746ed9ab9401e6982))
- We've added an optional Bundle to Complications which if set gets merged in with the intent sent to launch the provider chooser activity. ([Ifd4ad](https://android-review.googlesource.com/#/q/Ifd4adf79afbdaed2f505e7fcdd07d1d443752bfe))
- We've added a new `wear-watchface-editor` library to support on watch face and SysUi hosted editors. SysUI will launch these editors by sending an intent. The watch face activity service can use the new EditorSession class to access WatchFace details and record the result via Activity.setWatchRequestResult. ([I2110d](https://android-review.googlesource.com/#/q/I2110d1b0e714c563c0f076c7814b838511c2e3bc))
- LayerMode.DRAW_HIGHLIGHTED is now called LayerMode.DRAW_OUTLINED and RenderParameters.highlightComplicationId is now called RenderParameters.selectedComplicationId which draws a highlight on the specified complication in addition to an outline. ([I90a40](https://android-review.googlesource.com/#/q/I90a405d73c4d3a647c8ed21729655609050e2246))
- WatchFaceControlClient.getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClient's future can now resolve with a ServiceStartFailureException if the service dies while waiting for the watchface to be created. ([I0f509](https://android-review.googlesource.com/#/q/I0f509426f8e43822c6bdd0721857b385eb753848))
- EditorSession.complicationPreviewData is now a ListenableFuture because fetching this data is an asynchronous process. ([Iead9d](https://android-review.googlesource.com/#/q/Iead9d686587392e6be2db31b3010fe257a73eb8c))

**Bug Fixes**

- We're removing unused fields from ComplicationOverlay leaving enabled and complicationBounds. ([I17b71](https://android-review.googlesource.com/#/q/I17b71448a1875e66e3a209a4133dc079b4f223ea))

### Version 1.0.0-alpha05

January 13, 2021

`androidx.wear:wear-*:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd3c8e9c2424b78e44f55db599251891fd1cadb4..6207afb1646d302c5d29c2c67d332b48db87fb27/wear)

**New Features**

Watchfaces often support a number of complication configurations with varying numbers of complications shown. To make this easier to set up we now support initially disabled complications by calling setEnabled(false) on the builder. These can be enabled later via ComplicationsUserStyleSetting.

**API Changes**

- ComplicationHelperActivity now accepts `Collection<ComplicationType>` rather than an int array making it easier to use. ([I1f13d](https://android-review.googlesource.com/#/q/I1f13d4546c5f8fc8661a0664a333110f9ea0d148))
- `ProviderInfoRetriever.retrieveProviderInfo` now correctly returns `ListenableFuture<ProviderInfo[]>`. ([If2710](https://android-review.googlesource.com/#/q/If2710223e25ba11247bf952a714696f88ac6ccbf))
- You can now create an initially disabled complication by calling setEnabled(false) on the builder. ([Idaa53](https://android-review.googlesource.com/#/q/Idaa53a3fcaeeb0ec6ea8dedaddbfbafe5e3f613f))
- WatchFaceState now has an isHeadless property which is only true for headless instances. ([Ifa900](https://android-review.googlesource.com/#/q/Ifa900c849a27a2883bef7b6b1be735d82e3e2f5c))
- ComplicationDrawable now optionally supports synchronous loading of drawables. This is used by the screenshot APIs. ([I34d4a](https://android-review.googlesource.com/#/q/I34d4aa37eb0dbd995f93819e18232de5037cd613))

### Version 1.0.0-alpha04

December 16, 2020

`androidx.wear:wear-*:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..dd3c8e9c2424b78e44f55db599251891fd1cadb4/wear)

**New Features**

- The wear watch face library now supports setting bounds per type. E.g. you can switch to a wide bounding box for ComplicationType.LONG_TEXT whilst using a smaller bounding box for other types.

**API Changes**

- Complications now use ComplicationBounds which wraps a `Map<ComplicationType, RectF>` to support per complication type sizes. ([I1ebe7](https://android-review.googlesource.com/#/q/I1ebe78c6c7368ef3327c3dba39f6498b18089a4e))
- RenderParameters now lets you specify the highlight tint for use in screen shots. ([Iff42b](https://android-review.googlesource.com/#/q/Iff42b0df61de46be1e03566f8a9b79b67de8727e))
- With the exception of bounds you now have to use ComplicationsUserStyleSetting to modify complications, this is to ensure the OS is kept in sync. ([I8dc5d](https://android-review.googlesource.com/#/q/I8dc5db6f349e7ad4995f9ea7a3e12fe31b560c7e))
- Renderer is now a sealed class. This means CanvasRenderer and GlesRenderer are now inner classes of Renderer. ([Iab5d4](https://android-review.googlesource.com/#/q/Iab5d4cf05f02a2ed3a47729c32fac6b6e6cf23dc), [b/173803230](https://issuetracker.google.com/issues/173803230))
- CanvasComplicationDrawable.drawHighlight renamed to drawOutline. ObservableWatchData now has a few missing UiThread annotations. ScreenState has now been fully removed from WatchState. ([If1393](https://android-review.googlesource.com/#/q/If1393142f3a0d7902a35a7622329c1bf6e7e3449))
- The minimum API level for wear-watchface is now 25. Note hardware canvas support requires API level 26 or above. ([Ic9bbd](https://android-review.googlesource.com/#/q/Ic9bbdf1858ef4435bb6561cb02bba7b709d54d00))
- InteractiveWatchFaceWcsClient now has a getComplicationIdAt helper. ([I05811](https://android-review.googlesource.com/#/q/I05811891b9ea4ebb4f4c3fa393d3b7510dee8e0b))
- The API level for wear-watchface-client has been reduced to 25, however the screen shot APIs require API level 27. ([Id31c2](https://android-review.googlesource.com/#/q/Id31c21c4b650cc8cb21523f4b0cf861bd1b107e0))

**Bug Fixes**

- We now expose the complication's current ComplicationData's ComplicationType in ComplicationState. ([I9b390](https://android-review.googlesource.com/#/q/I9b39013cc5486d68bd285c9624fedc5f0ba835d2))
- InteractiveWatchFaceWcs now has a method \`bringAttentionToComplication to briefly highlight the specified complication. ([I6d31c](https://android-review.googlesource.com/#/q/I6d31cb1a177fe9eb98c0859ce400391c8cecb668))
- `InteractiveWatchFaceWcsClient#setUserStyle` now has an overload accepting Map which can potentially avoid an extra IPC round trip necessary to construct UserStyle. ([I24eec](https://android-review.googlesource.com/#/q/I24eec01f8eed113931fa7ec61cc8af4baf38049d))

### Version 1.0.0-alpha03

December 2, 2020

`androidx.wear:wear-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/wear)

**New Features**

The Complication class now has a compicationData property letting watch faces observe ComplicationData changes. This makes it possible to change the complication's dimensions based on the type of the complication.

Variable frame rates are now supported by assigning to Renderer.interactiveDrawModeUpdateDelayMillis. For watch faces which run short animations every second this can lead to good power savings by going to sleep when not animating.

**API Changes**

- `BACKGROUND_IMAGE` has been renamed to `PHOTO_IMAGE` along with related classes. This type of complication is not exclusively used for backgrounds hence the name change. ([I995c6](https://android-review.googlesource.com/#/q/I995c61974db868d89184b8fa49d677e6fc16befa))
- DefaultComplicationProviderPolicy properly annotated with IntDefs. ([I3b431](https://android-review.googlesource.com/#/q/I3b4312734532d2cec94d74ed70647fb33ecf21e3))
- The hidden TimeDependentText class is no longer exposed via ContentDescriptionLabel, instead we add an accessor to get the text at a specified time. ([Ica692](https://android-review.googlesource.com/#/q/Ica69255606c011c1b4c733db31d3c4afdad16887))
- ObservableWatchData's constructor is now internal. ([I30121](https://android-review.googlesource.com/#/q/I301215475e08c10a8cb97095638b235d664bcfcb), [b/173802666](https://issuetracker.google.com/issues/173802666))
- Complication now has compicationData letting watch faces observe ComplicationData changes. Complication also has a new isActiveAt call which can be used to tell if anything should be rendered at the provided datetime. ([Ic0e2a](https://android-review.googlesource.com/#/q/Ic0e2a53c2c8973e133304a55197ec27c708404e7))
- The empty `SharedMemoryImage` is no longer in the public API. ([I7ee17](https://android-review.googlesource.com/#/q/I7ee17b402375ff3231a4fb8b6cd32cacaefdab8a))
- `WatchFace.overridePreviewReferenceTimeMillis` now has an IntRange annotation and the getter and setter have consistent names. ([Ia5f78](https://android-review.googlesource.com/#/q/Ia5f7811eece551191ad1ec0ec9420369886058d2))
- `Complication.Builder` is now created via `Complication.createRoundRectComplicationBuilder` or `Complication.createBackgroundComplicationBuilder` for clarity ([I54063](https://android-review.googlesource.com/#/q/I54063447e6c0fac6f53448ec50a3f50d3a1c759b))
- Added WatchFace.TapListener which allows taps not consumed by complications to be observed by the WatchFace. ([Ic2fe1](https://android-review.googlesource.com/#/q/Ic2fe1b967acc321e459f560a298ad98206a431ab), [b/172721168](https://issuetracker.google.com/issues/172721168))
- WatchFace now supports variable frame rates by assigning to `Renderer.interactiveDrawModeUpdateDelayMillis`. This can help preserve battery life by sleeping when not animating. ([I707c9](https://android-review.googlesource.com/#/q/I707c9c6487b902c8f4f339ac292ca3a4dce49ef9))
- WatchFace.Builder is no longer needed and invalidate() and interactiveUpdateRateMillis have been moved to Renderer. ([I329ea](https://android-review.googlesource.com/#/q/I329ea7916fe2ad0c37cf45d8ab9de6da326ee82d))
- For better java interoperability renamed getters for boolean properties in WatchState ([I6d2f1](https://android-review.googlesource.com/#/q/I6d2f154452b3f6b17617bd7412539380ce0ea84c))
- Renamed TapListener to TapCallback and InvalidateCallback to InvalidateListener for consistency. ([I9414e](https://android-review.googlesource.com/#/q/I9414ef54a9ebbdbda6c625ef9f139882a0ee0af6))
- Wear 2.0 watchface style options have been moved to their own class for clarity. WatchFace.Builder setters now have symmetrical WatchFace class getters. ([Iefdfc](https://android-review.googlesource.com/#/q/Iefdfc95bbab3eec314d95b3cd7f6b4666fa28ba2))
- Added InteractiveWatchFaceWcsClient and `WatchFaceControlClient.getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClient` which either gets an existing instance or creates it once the wallaper service has connected and made the engine. ([Id666e](https://android-review.googlesource.com/#/q/Id666e8c785c8cd803ff445dda4e45f40db65cee9))
- WatchFaceControlClient is now an interface to allow tests to mock it. ([I875d9](https://android-review.googlesource.com/#/q/I875d9b0bf214db40781958e04e7cc751cdde709d))
- HeadlessWatchFaceClient, InteractiveWatchFaceSysUiClientImpl, InteractiveWatchFaceWcsClient are now interfaces to better facilitate testing. ([I7cdc3](https://android-review.googlesource.com/#/q/I7cdc3a7b9e49cb26a9a55d43243ae305e8cf9701))
- Added annotations to methods in `wear-watchface-complications-rendering` ([I0d65c](https://android-review.googlesource.com/#/q/I0d65c78e9c6717748a5891fc539fc258812851c5))

**Bug Fixes**

- Remove screen shape from DeviceConfig, which was duplicating `android.content.res.Configuration#isScreenRound()` ([Ifadf4](https://android-review.googlesource.com/#/q/Ifadf459ef1f67f24262e97279f859b413a2dd045))
- Changed `WatchFaceControlClient.getOrCreateWallpaperServiceBackedInteractiveWatchFaceWcsClient` to accept a `Map<String, String>` instead of `UserStyle` because it's hard to create a `UserStyle` without knowing the schema which you can only get after the client has been created. ([Iea02a](https://android-review.googlesource.com/#/q/Iea02ada7595d6e0272a94644c470330ed17378c1))
- Fix `InteractiveWatchFaceWcsClient` to use `ComplicationState` instead of the wire format. ([Icb8a4](https://android-review.googlesource.com/#/q/Icb8a49513e834ead46c7bcca78504f905b8766ba))
- `UserStyleSettings` is now a sealed class because the watch face editors only understand the built in classes. ([I2d797](https://android-review.googlesource.com/#/q/I2d797029198ecd2b6a3aac3e16b691be05171f83))

### Version 1.0.0-alpha02

November 11, 2020

`androidx.wear:wear-*:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/wear)

**API Changes**

- `ComplicationDetails` is now called `ComplicationState` and is properly wrapped and usages of wearable support `@ComplicationData.ComplicationType` have been migrated to androidx `ComplicationType`. ([I4dd36](https://android-review.googlesource.com/#/q/I4dd368751f3ffe3bd5728f485ef0f8afeee287ea))
- Add an optional `highlightedComplicationId` parameter to RenderParameters which allows you to request highlighting of a single complication in screenshots. ([I66ce9](https://android-review.googlesource.com/#/q/I66ce937929c863627c45291901b945945a21d89f))
- `ComplicationProviderService` to use new style complication api for consistency ([Id5aea](https://android-review.googlesource.com/#/q/Id5aea26299cefb845006e630d956e0ca08c20f99))
- `getPreviewReferenceTimeMillis` now gets reference times from `DeviceConfig`. ([I779fe](https://android-review.googlesource.com/#/q/I779fefb5b7bb8ea737b98fedbabe0d97844fd198))
- Simplifying Renderer API surface, can use `SurfaceHolder.Callback` to observe changes instead. ([I210db](https://android-review.googlesource.com/#/q/I210dbb26483698cfbea0e434182891ddd3958424))
- `CanvasComplicationRenderer` doesn't extend from `Renderer`, renaming it for clarity. ([Ibe880](https://android-review.googlesource.com/#/q/Ibe8809f15ec4d2145b8011c26e00fd2804aac466))

**Bug Fixes**

- First version of `androidx.wear:wear-watchface-client` ([I1e35e](https://android-review.googlesource.com/#/q/I1e35eb467fff1ed8d4a440bec74c6b6e94109d34))
- Changed the name of `GlesTextureComplication#renderer` for clarity ([Ib78f7](https://android-review.googlesource.com/#/q/Ib78f7d3b571033f35401858aeaf71f62fe1effa2))
- Rename `StyleCategory` to `StyleSetting` for clarity ([I488c7](https://android-review.googlesource.com/#/q/I488c740576f28a670b2a354b602030c1bff93d3c))
- Adding `UserStyleSchema` for a cleaner API ([If36f8](https://android-review.googlesource.com/#/q/If36f8841fe2d1c17b14afa8b35da72641ac8ffbc))

### Version 1.0.0-alpha01

October 28, 2020

`androidx.wear:wear-complications-*:1.0.0-alpha01` and `androidx.wear:wear-watchface-*:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b/wear)

**API Changes**

- Removed some things we didn't intend to expose in public api. ([I41669](https://android-review.googlesource.com/#/q/I4166938e428ef6147e39aaa8994e7e21003067b0))
- Create `androidx.wear:wear-complications-provider` library. ([I77f1f](https://android-review.googlesource.com/#/q/I77f1fe61bd5dfd122845b459901484e2c9ee4b77))
- ComplicationsUserStyleCategory the new recommended category for configuring complications ([I96909](https://android-review.googlesource.com/#/q/I96909e26ed00f6fb9f27f9fac2b81d7c0d92b690))
- Add wear-complication-data API. ([I7c268](https://android-review.googlesource.com/#/q/I7c268561f08f0a637ecc4bc4fbf59c32236d50bf))
- Functions with boolean return values to be prefixed with "is" rather than "get" ([If36ff](https://android-review.googlesource.com/#/q/If36ff36bc29d7090ae7f358d8b03123e43b53c7d))
- API advice is to avoid using protected so this class has been refactored to take parameters in via the constructor. ([I61644](https://android-review.googlesource.com/#/q/I6164450bf16baa6bde98380c2e113f49774f0916))
- Rename setBackgroundComplication for clarity. ([I96fe3](https://android-review.googlesource.com/#/q/I96fe3baa25837620d01ab51d16c4aef87a71a6b2))
- Use Kotlin properties for ComplicationDrawable isHighlighted \& data ([I4dcc8](https://android-review.googlesource.com/#/q/I4dcc8d2f323efd18fb1cadbbe9b01aac7111565a))
- Instead of ComplicationRenderer.InvalidateCallback we add Complication#invalidate() ([I4f4c6](https://android-review.googlesource.com/#/q/I4f4c6e25b0483dd5df47f24ddcb368baa93a11c0))
- These APIs are being deprecated in WearableSupport and are removed here. ([Ib425c](https://android-review.googlesource.com/#/q/Ib425caef57c20664c5840cb5e3ac5df15b8aab5e))
- Renamed some WatchFace builder methods to emphasize their wear 2.0 legacy nature. ([Idb775](https://android-review.googlesource.com/#/q/Idb7758597bc716af40d1739ac4703b15199e65d7))
- First beta API candidate for wear/wear-watchface ([Id3981](https://android-review.googlesource.com/#/q/Id39817fd9b1ee6d40f8be57580e73cdeb124cd92))
- First tracked version of the API. ([Ie9fe6](https://android-review.googlesource.com/#/q/Ie9fe6d120d948cfc33b7ca7caf6cd5a520c6229b))
- Properly hiding ComplicationDrawable.BorderStyle IntDef and move to ComplicationStyle for consistency. ([I27f7a](https://android-review.googlesource.com/#/q/I27f7ac3ea8b10cb8809fc3f9e6d52f03e1daf70d))
- Adding missing annotations for ComplicationStyle methods ([I838fd](https://android-review.googlesource.com/#/q/I838fd9dcb92d104f03cb5a0b2f31d524d95f3305))
- This library has no public API surface ([I88e2b](https://android-review.googlesource.com/#/q/I88e2b4b4a72bcd8ccf8237118f584278b2b6f069))
- All style category Option classes are now properly final. ([Ib8323](https://android-review.googlesource.com/#/q/Ib83234ce0dc8b6f0a5403add5372fb0c753eb052))
- First tracked version of the API. ([I27c85](https://android-review.googlesource.com/#/q/I27c852daff7b7ce6432af34cd08bbe95cdc77783))

**Bug Fixes**

- Changed ComplicationProviderService to have an explicit getComplicationPreviewData method. ([I4905f](https://android-review.googlesource.com/#/q/I4905f2efcc57bf4a7227c6aea60f164f70f27009))
- API lint check for MissingGetterMatchingBuilder is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9), [b/138602561](https://issuetracker.google.com/issues/138602561))
- Rename wear-complications-rendering. ([Ifea02](https://android-review.googlesource.com/#/q/Ifea0298d58e56d7ca03ffbd960d840aa086281a7))
- Style category display names are now CharSequences ([I28990](https://android-review.googlesource.com/#/q/I2899093bb0ccdefffddc08fedf5c14a9051dae26))
- Replacing Override with Overlay to match current themes \& styles naming conventions. ([I4fde9](https://android-review.googlesource.com/#/q/I4fde9ea29573156daa953916d3b92a1e929882c3))
- Renamed UserStyle#getOptions for clarity. ([I695b6](https://android-review.googlesource.com/#/q/I695b622d27a59c1effbbdcd9cee37c1f54c4c5da))

## Version 1.2.0

### Version 1.2.0

September 15, 2021

`androidx.wear:wear:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da0944806932662865db1602128f5be25f81a5fa..21d8b657a9de9dc81f495c51813006a7408c469b/wear/wear)

**Important changes since 1.1.0**

- Added CurvedText component for easily writing curved text following the curvature of the largest circle that can be inscribed in the view. An usage example:

      <androidx.wear.widget.CurvedText
              android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:text="example curved text"
              app:anchorAngleDegrees="180"
              app:anchorPosition="center"
              app:clockwise="false"
              style="@android:style/TextAppearance.Large"
      />

  ![An example of curved text in Android Wear](https://developer.android.com/static/images/jetpack/release-notes/wear-example-curved-text.png)
- Added ArcLayout container for laying out its child elements one by one on an arc in either the clockwise or counterclockwise direction. Its children can be both standard android widget or "curved" widgets which implement the `ArcLayout.Widget` interface. ([I536da](https://android-review.googlesource.com/q/I536da16ff800021b8d37c09cc00a25159997d4f3)) An usage example:

      <androidx.wear.widget.ArcLayout
              android:layout_width="match_parent"
              android:layout_height="match_parent"
              app:anchorPosition="center">
            <ImageView
                    android:layout_width="20dp"
                    android:layout_height="20dp"
                    android:src="@drawable/ic_launcher"
            />
            <androidx.wear.widget.CurvedText
                    android:layout_width="match_parent"
                    android:layout_height="match_parent"
                    android:text="Curved Text"
                    style="@android:style/TextAppearance.Small"
                    android:padding="2dp"
             />
        </androidx.wear.widget.WearArcLayout>

  ![An example of arch text in Android Wear](https://developer.android.com/static/images/jetpack/release-notes/wear-example-arch-text.png)
- Added a new layout container, DismissibleFrameLayout, which handles back-button-dismiss and/or swipe-to-dismiss, intended for use within an activity. At least one listener must be added to act on a dismissal action. A listener will typically remove a containing view or a fragment from the current activity. setSwipeDismissible(boolean) \& setBackButtonDismissible(boolean) are provided for direct control over the features. This new layout is meant to replace the existing SwipeDismissFrameLayout.

- Added support for indicating that an Activity can be "auto-resumed" when the device leaves ambient mode in the AmbientModeSupport class. This functionality was previously available in the deprecated WearableActivity class from WearableSupportLibrary. ([I336ab](https://android-review.googlesource.com/#/q/I336abf5db96568ea75f421990301cfa383f54285))

- Migrated WearableCalendarContract class from Wearable Support Library. This API provides a subset of the data available through [CalendarContract](http://developer.android.com/reference/android/provider/CalendarContract.html), but is automatically synced to wearable devices. ([I6f2d7](https://android-review.googlesource.com/#/q/I6f2d777b4c869eaa09a92ef56577fd06be829e2f))

- Added a new API `WearTypeHelper` in `androidx.wear.utils` for determining whether the given wear device is for China. ([Ib01a9](https://android-review.googlesource.com/#/q/Ib01a930f280286abf7824604a93cae0fece23cb5))

- Added accessibility features to `androidx.wear.widget.ConfirmationOverlay` that will read out messages if set followed by animation description. ([I524dd](https://android-review.googlesource.com/#/q/I524ddf3007652a024191197e46e1e6641d239c73))

- Fixed bug that caused ConfirmationActivity to crash if no message
  was provided. ([Ie6055](https://android-review.googlesource.com/#/q/Ie6055a81b7d1c696d4b4f7eb81ff03862f35f665))

- Fixed bug where horizontally scrolling RecyclerViews caused
  `WearableDrawerLayout` to peek on all interactions. ([I24c7f](https://android-review.googlesource.com/#/q/I24c7f3a4afecdad53b2952df11e6dfdab82050d3))

### Version 1.2.0-rc01

September 1, 2021

`androidx.wear:wear:1.2.0-rc01` is released with no changes since the last beta. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..da0944806932662865db1602128f5be25f81a5fa/wear/wear)

### Version 1.2.0-beta01

August 18, 2021

`androidx.wear:wear:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/wear/wear)

**Bug Fixes**

- Fix bug that caused ConfirmationActivity to crash if no message was provided. ([Ie6055](https://android-review.googlesource.com/#/q/Ie6055a81b7d1c696d4b4f7eb81ff03862f35f665))

### Version 1.2.0-alpha13

August 4, 2021

`androidx.wear:wear:1.2.0-alpha13` is released. [Version 1.2.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/wear/wear)

**API Changes**

- Renamed `WearTypeHelper.isChinaDevice` to`WearTypeHelper.isChinaBuild`. ([I47302](https://android-review.googlesource.com/#/q/I4730259bc10061164e989fba882331496b457316))

**Bug Fixes**

- We have added accessibility features to `androidx.wear.widget.ConfirmationOverlay` that will read out messages if set followed by animation description. ([I524dd](https://android-review.googlesource.com/#/q/I524ddf3007652a024191197e46e1e6641d239c73))

### Version 1.2.0-alpha12

July 21, 2021

`androidx.wear:wear:1.2.0-alpha12` is released. [Version 1.2.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear/wear)

**API Changes**

- We have added a new API `WearTypeHelper` in `androidx.wear.utils` for determining whether the given wear device is for China. ([Ib01a9](https://android-review.googlesource.com/#/q/Ib01a930f280286abf7824604a93cae0fece23cb5))

### Version 1.2.0-alpha11

June 30, 2021

`androidx.wear:wear:1.2.0-alpha11` is released. [Version 1.2.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/wear/wear)

**Bug Fixes**

- Fixed bug where horizontally scrolling RecyclerViews caused `WearableDrawerLayout` to peek on all interactions. ([I24c7f](https://android-review.googlesource.com/#/q/I24c7f3a4afecdad53b2952df11e6dfdab82050d3))

### Version 1.2.0-alpha10

June 2, 2021

`androidx.wear:wear:1.2.0-alpha10` is released. [Version 1.2.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/wear/wear)

**New Features**

- Alpha10 improves accessibility support in Curved Text and ArcLayouts. It also add some minor renaming of in the DismissibleFrameLayout to help clarify the API.

**API Changes**

- We have renamed following methods in `DismissibleFrameLayout` ([Ib195e](https://android-review.googlesource.com/#/q/Ib195e4be2d73db6a39a56ecf5d23ffa076905c4f)):
  - `Callback#onDismissed` -\> `Callback#onDismissedFinished`
  - `isSwipeDismissible` -\> `isDismissableBySwipe`
  - `isBackButtonDismissible` -\> `isDismissableByBackButton`
- We have made following methods final ([Ib195e](https://android-review.googlesource.com/#/q/Ib195e4be2d73db6a39a56ecf5d23ffa076905c4f)):
  - `setBackButtonDismissible`
  - `setSwipeDismissible`
  - `registerCallback`
  - `unregisterCallback`

**Bug Fixes**

- Use the content of the CurvedTextView on Talkback. ([I05798](https://android-review.googlesource.com/#/q/I057981fd1e744eae03d0874f38d6c392bd3e88b8))
- Better accessibility for normal views in an ArcLayout. ([I4418d](https://android-review.googlesource.com/#/q/I4418d87ba7b4ad3b3332b78dff14c3aeb32617a3))

### Version 1.2.0-alpha09

May 18, 2021

`androidx.wear:wear:1.2.0-alpha09` is released. [Version 1.2.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/wear/wear)

**API Changes**

- Added a new function `CurvedTextView.setTypeface()` (similar to `TextView`'s), to set the text typeface and bold/italics style. ([I4653c](https://android-review.googlesource.com/#/q/I4653c3219b8eaab1873f05a59518ce0934321298))
- Renamed `WearArcLayout` to `ArcLayout`, `WearCurvedText` to `CurvedText` and `WearArcLayout.ArcLayoutWidget` to `ArcLayout.Widget`. ([I6e5ce](https://android-review.googlesource.com/#/q/I6e5ce21e532e24b02a2ee0e03636d478425ef5e1))
  - On `ArcLayout.Widget`, renamed `getThicknessPx` into `getThickness`.
  - Vertical alignment constants on `ArcLayout.LayoutParams` are now named starting with `VERTICAL_ALIGN_` (instead of the previous `VALIGN_`)
- On `CurvedTextView`, the methods `setMinSweepDegrees` and `setMaxSweepDegrees` were replaced by `setSweepRangeDegrees` ([I7a9d9](https://android-review.googlesource.com/#/q/I7a9d97897e7d29186071e296ac4fd4ca0f101ac4))

### Version 1.2.0-alpha08

May 5, 2021

`androidx.wear:wear:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/wear/wear)

**API Changes**

- To improve code clarity, we added `@FloatRange` annotations to some angle parameters and return types. ([I430dd](https://android-review.googlesource.com/#/q/I430dd3cd37ce660234b5e5bb1937f477ae947cc8))
- In the interface `WearArcLayout.ArcLayoutWidget`, the method `insideClickArea` is now called isPointInsideClickArea. ([Ia7307](https://android-review.googlesource.com/#/q/Ia73073b0e9d664d41865d5df63afc2db637d036d))

### Version 1.2.0-alpha07

March 24, 2021

`androidx.wear:wear:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..5c42896eb6591b09e3952030fb7ea8d9b8c42713/wear/wear)

**Bug Fixes**

- Fixing errors with non-curved children inside of WearArcLayout caused by using screen size with height bigger than width. These non-curved children are now correctly placed inside of an arc on all screen types.

### Version 1.2.0-alpha06

January 27, 2021

`androidx.wear:wear:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..aee18b103203a91ee89df91f0af5df2ecff356d6/wear/wear)

**API Changes**

- Migrate the Ongoing Activities library to a new sub-library: wear-ongoing. Classes now live in the androidx.wear.ongoing package (previously was androidx.wear.ongoingactivities) ([I7c029](https://android-review.googlesource.com/#/q/I7c02947659bbf33c9b66757001eccfa225f4168f))
- Migrate WearableCalendarContract class from Wearable Support Library to AndroidX. This API provides a subset of the data available through [CalendarContract](http://developer.android.com/reference/android/provider/CalendarContract.html), but is automatically synced to wearable devices. ([I6f2d7](https://android-review.googlesource.com/#/q/I6f2d777b4c869eaa09a92ef56577fd06be829e2f))

**Bug Fixes**

- Disable the back button dismiss feature by default in Dismissible FrameLayout since swipe-to-dismiss remains as the main way to navigate back a full screen on Wearable devices ([Ic24e3](https://android-review.googlesource.com/#/q/Ic24e390d281c6a2e1b79ff3361c01788fc1eff5e))
- Fixed some issues handling children visibility on WearArcLayout ([Icf912](https://android-review.googlesource.com/#/q/Icf91280ddcea0e73008b55801bcb9d4e5ca169cf))

### Version 1.2.0-alpha05

January 13, 2021

`androidx.wear:wear:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd3c8e9c2424b78e44f55db599251891fd1cadb4..6207afb1646d302c5d29c2c67d332b48db87fb27/wear/wear)

**Bug Fixes**

- Update the javadoc of AmbientModeSupport class to provide sample snippets to better demonstrate the general use of this class.

### Version 1.2.0-alpha04

December 16, 2020

`androidx.wear:wear:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..dd3c8e9c2424b78e44f55db599251891fd1cadb4/wear/wear)

**API Changes**

- Added support for indicating that an Activity can be "auto-resumed" when the device leaves ambient mode in the AmbientModeSupport class. This functionality was previously available in the deprecated WearableActivity class from WearableSupportLibrary. ([I336ab](https://android-review.googlesource.com/#/q/I336abf5db96568ea75f421990301cfa383f54285))
- OngoingActivity
  - Category can now be set when creating an OngoingActivity, e.g. `OngoingActivitiy.Builder.getCategory(String)`
  - OngoingActivityData now has a timestamp of when the OngoingActivity was built - `OngoingActivityData.getTimestamp()`
  - ([I91cb4](https://android-review.googlesource.com/#/q/I91cb49fc7325b2deae05b58ab9b29468992d150e))
- Added support for setting margins on children of WearArcLayout by changing the layout params to extend MarginLayoutParams, i.e. WearArcLayout.LayoutParams extends android.view.ViewGroup.MarginLayoutParams. ([I2cd88](https://android-review.googlesource.com/#/q/I2cd88c276ab6b548a7fe068aecc74133b5300e3f))
- Change WearCurvedTextView's anchor type default to `WearArcLayout.ANCHOR_CENTER` (was `WearArcLayout.ANCHOR_START`). This simplifies the contract between the arc layout and the curved text as the curved text by default draws itself x-centered at the top, and the parent arc layout can rotate it to where it needs to be. ([I105ff](https://android-review.googlesource.com/#/q/I105ff40f39488f960582a7cba799e47b6b7086ee))

### Version 1.2.0-alpha03

December 2, 2020

`androidx.wear:wear:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/wear/wear)

**New Features**

A new layout container DismissibleFrameLayout, which handles back-button-dismiss and/or swipe-to-dismiss, intended for use within an activity. At least one listener must be added to act on a dismissal action. A listener will typically remove a containing view or a fragment from the current activity. setSwipeDismissible(boolean) \& setBackButtonDismissible(boolean) are provided for direct control over the features. This new layout is meant to replace the existing SwipeDismissFrameLayout.

Curved widgets now handle touch events. Normal widgets inside an WearArcLayout will receive all touch events, mapped to their coordinate space. WearCurvedTextView (inside an WearArcLayout or not) can set onClick and onLongClick handlers.

Ongoing activities classes are now VersionedParcelables instead of using custom serialization/deserialization. The static icon and touch intent are now required.

**API Changes**

- The attribute "sweepDegrees" for WearCurvedTextView is separated into minSweepDegrees and maxSweepDegrees to give a more flexible layout of this widget.

### Version 1.2.0-alpha02

November 11, 2020

`androidx.wear:wear:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/wear/wear)

This release adds a new "Ongoing Activities API" for the first time. This API can be used by developers to signal that a long running activity, such as a fitness exercise or a media playback session is on-going. It allows developers to provide periodic status updates such as "distance and time run" or "current track playing" for display on the watch face or in the app launcher. This functionality is targeted at future devices with the on-going activity functionality enabled.

**API Changes**

- New API for Ongoing Activities, this is a no-op on "unsupported devices.". ([I69a31](https://android-review.googlesource.com/#/q/I69a31a74749eeb6d290d7943892019a5a1cdfd62))

### Version 1.2.0-alpha01

October 28, 2020

`androidx.wear:wear:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/792501d04a4ca4858f27d36ec77bf3b35c3211af..234e23e470a5e7f81291f6acd12d538146dc010b/wear/wear)

**New Features**

- Added WearCurvedTextView component for easily writing curved text following the curvature of the largest circle that can be inscribed in the view. An usage example:

    <androidx.wear.widget.WearCurvedTextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="example curved text"
            app:anchorAngleDegrees="180"
            app:anchorPosition="center"
            app:clockwise="false"
            style="@android:style/TextAppearance.Large"
    />

![An example of curved text in Android Wear](https://developer.android.com/static/images/jetpack/release-notes/wear-example-curved-text.png)

- Added WearArcLayout container for laying out its child elements one by one on an arc in either the clockwise or counterclockwise direction. Its children can be both standard android widget or "curved" widgets which implement its ArcLayoutWidget interface. An usage example:

    <androidx.wear.widget.WearArcLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:anchorPosition="center">
          <ImageView
                  android:layout_width="20dp"
                  android:layout_height="20dp"
                  android:src="@drawable/ic_launcher"
          />
          <androidx.wear.widget.WearCurvedTextView
                  android:layout_width="match_parent"
                  android:layout_height="match_parent"
                  android:text="Curved Text"
                  style="@android:style/TextAppearance.Small"
                  android:padding="2dp"
           />
      </androidx.wear.widget.WearArcLayout>

![An example of arch text in Android Wear](https://developer.android.com/static/images/jetpack/release-notes/wear-example-arch-text.png)

([I536da](https://android-review.googlesource.com/q/I536da16ff800021b8d37c09cc00a25159997d4f3))

## Wear-Input 1.2

### Version 1.2.0

September 10, 2025

`androidx.wear:wear-input:1.2.0` and `androidx.wear:wear-input-testing:1.2.0` are released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c703f9ae405f8bd6f6c2b5ea25e78cc385af90ab..d100b900f3fe5699adfa2afaaf6d467cf7b836dd/wear).

**Important changes since 1.1.0:**

- Exposed physical button location constants.
- Added `WearableRemoteInputExtender` for setting Wear-specific extras on `android.app.RemoteInput` (for example, enabling Emoji input)

### Version 1.2.0-rc01

August 27, 2025

`androidx.wear:wear-input:1.2.0-rc01` and `androidx.wear:wear-input-testing:1.2.0-rc01` are released with no changes since the last beta. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..c703f9ae405f8bd6f6c2b5ea25e78cc385af90ab/wear).

### Version 1.2.0-beta01

July 30, 2025

`androidx.wear:wear-input:1.2.0-beta01` and `androidx.wear:wear-input-testing:1.2.0-beta01` are released with no notable changes since the last alphas. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..5fa9d0954ece0376736164b0f7bc2ef33506ab70/wear/wear-input).

### Version 1.2.0-alpha04

July 16, 2025

`androidx.wear:wear-input:1.2.0-alpha04` and `androidx.wear:wear-input-testing:1.2.0-alpha04` are released. Version 1.2.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/wear).

**New Features**

- Account for screen rotation when calculating the location of physical buttons relative to the screen. ([87a57e](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3396375))

**API Changes**

- Rename LOC*\* to LOCATION* \* in wear-input. ([I5e879](https://android-review.googlesource.com/#/q/I5e87996a7783a7fdf4abf9c4ea1357ac7bcc4590))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: `-Xjspecify-annotations=strict`, `-Xtype-enhancement-improvements-strict-mode` ([Icbfb9](https://android-review.googlesource.com/#/q/Icbfb9996a30b4decc85ee8a9bc4211a25adfcfe3), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.2.0-alpha02

September 29, 2021

`androidx.wear:wear-input:1.2.0-alpha02` and `androidx.wear:wear-input-testing:1.2.0-alpha02` are released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/wear)

**API Changes**

- Renamed `disallowEmoji` to `setEmojisAllowed` in `WearableRemoteInputExtender` to use to set whether the option to draw emojis will be shown. ([I28393](https://android-review.googlesource.com/#/q/I28393933d8c178c6f39bcc6ec0c571edf0ade471))

### Version 1.2.0-alpha01

September 15, 2021

`androidx.wear:wear-input:1.2.0-alpha01` and `androidx.wear:wear-input-testing:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf82de2481a345e3246890808ee52363d69194fc..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/wear)

**API Changes**

- Exposed all button location constants from `WearableButtons`. ([Ibb12c](https://android-review.googlesource.com/#/q/Ibb12c35ad548b8a67baeef405cb19739bbfa47bd))
- Added `WearableRemoteInputExtender` class that can be used for adding Wear-specific extras to the android.app.RemoteInput. ([I01903](https://android-review.googlesource.com/#/q/I0190310bcd43c98793bda31a7ef055e1abad815e))

## Wear-Input 1.1.0

### Version 1.1.0

August 18, 2021

`androidx.wear:wear-input:1.1.0` and `androidx.wear:wear-input-testing:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1d48419d620e931d6c410d4dedb2788d95a8fc98..bf82de2481a345e3246890808ee52363d69194fc/wear)

**Important changes since 1.0.0**

- Added `RemoteInputIntentHelper`.
  - This class can be used to build a RemoteInput Intent. This can then be used to request input from your users in a customisable activity.

### Version 1.1.0-rc01

August 4, 2021

`androidx.wear:wear-input:1.1.0-rc01` and `androidx.wear:wear-input-testing:1.1.0-rc01` are released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..1d48419d620e931d6c410d4dedb2788d95a8fc98/wear)

No API Changes since `androidx.wear:wear-input:1.1.0-beta01` and `androidx.wear:wear-input-testing:1.1.0-beta01`

### Version 1.1.0-beta01

July 21, 2021

`androidx.wear:wear-input:1.1.0-beta01` and `androidx.wear:wear-input-testing:1.1.0-beta01` are released with no changes since `1.1.0-alpha03`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear/wear-input)

### Version 1.1.0-alpha03

June 30, 2021

`androidx.wear:wear-input:1.1.0-alpha03` and `androidx.wear:wear-input-testing:1.1.0-alpha03` are released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..19ae3a88ff0824d615355b492cb56049e16991f2/wear)

**Bug Fixes**

- Fixed bug which caused RemoteInput intents, which had `RemoteInput`s added to them via `RemoteInputHelper.putRemoteInputsExtra`, to be rejected.

### Version 1.1.0-alpha02

May 18, 2021

`androidx.wear:wear-input:1.1.0-alpha02` and `androidx.wear:wear-input-testing:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..66681ad83c328d0dd821b943bb3d375f02c1db61/wear)

**API Changes**

- `RemoteInputIntentHelper`'s methods that are used for getting or putting extras that represent title, cancel, confirm, and in progress labels are now using `CharSequence` instead of `String` for these labels. ([I0e71f](https://android-review.googlesource.com/#/q/I0e71f888c3da299cf863bcd3a5af18174d705313))

### Version 1.1.0-alpha01

January 27, 2021

`androidx.wear:wear-input:1.1.0-alpha01` and `androidx.wear:wear-input-testing:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64308b96cf7c7c5e039a3f95cd3dae1bb9d9d915..aee18b103203a91ee89df91f0af5df2ecff356d6/wear)

**API Changes**

- Migrate RemoteInputIntent class from Wearable Support Library to AndroidX. The migrated class is renamed as RemoteInputIntentHelper which provides helper functions for supporting remote inputs through starting an intent. ([I47cee](https://android-review.googlesource.com/#/q/I47ceeb522f3d0d4ef9ab6078cee228b32b29c416))

## Wear-Input 1.0.0

### Version 1.0.0

December 2, 2020

`androidx.wear:wear-input:1.0.0` and `androidx.wear:wear-input-testing:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ecf1b5888d9d003cacb3edb9c2fff198d3437d70..64308b96cf7c7c5e039a3f95cd3dae1bb9d9d915/wear)

This release is identical to `1.0.0-rc01`.

**Major features of 1.0.0**

- Migration of [WearableButtons](https://developer.android.com/reference/android/support/wearable/input/WearableButtons) functionality from Wearable Support Library to Jetpack.

- Added `androidx.wear.input.test.TestWearableButtonsProvider` which implements `androidx.wear.input.WearableButtonsProvider` to aid testing applications developed with `androidx.wear:wear-input` library.

### Version 1.0.0-rc01

November 11, 2020

`androidx.wear:wear-input:1.0.0-rc01` and `androidx.wear:wear-input-testing:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..ecf1b5888d9d003cacb3edb9c2fff198d3437d70/NULL)

This release is identical to `1.0.0-beta01`.

### Version 1.0.0-beta01

October 28, 2020

`androidx.wear:wear-input:1.0.0-beta01` and `androidx.wear:wear-input-testing:1.0.0-beta01` are released with no changes since `1.1.0-alpha01`. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..234e23e470a5e7f81291f6acd12d538146dc010b/wear)

### Wear-Input-Testing Version 1.0.0-alpha01

October 14, 2020

`androidx.wear:wear-input-testing:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6/wear/wear-input-testing)

**API Changes**

- Added `androidx.wear.input.test.TestWearableButtonsProvider` which implements `androidx.wear.input.WearableButtonsProvider` to aid testing applications developed with `androidx.wear:wear-input` library. ([I0ed0c](https://android-review.googlesource.com/#/q/I0ed0ce2a891e982afea3517e3309153751ae4ac4))

### Wear-Input Version 1.0.0-alpha01

September 2, 2020

`androidx.wear:wear-input:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d/wear/wear-input)

**New Features**

Migration of [WearableButtons](https://developer.android.com/reference/android/support/wearable/input/WearableButtons) functionality from Wearable Support Library to Jetpack. Additional testing support will be provided in `androidx.wear:wear-input-testing` library in the next Jetpack release.

## Version 1.1.0

### Version 1.1.0

October 14, 2020

`androidx.wear:wear:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/792501d04a4ca4858f27d36ec77bf3b35c3211af..ad54b370b5a26a3ecac49960af95bbcff8c66d59/wear/wear)

**Major changes since 1.0.0**

- Added a `layout_` prefix to boxedEdges attribute (now `layout_BoxedEdges`) for `BoxInsetLayout` in order to comply with android naming convention. This will remove the linter error in Android Studio for these attributes. ([I4272f](https://android-review.googlesource.com/q/I4272f09a6d6d44cda5eb22c2b6117280c7b04ad3))
- Added optional `EXTRA_ANIMATION_DURATION_MILLIS` to `ConfirmationActivity` to allow for the duration that the confirmation dialog is displayed. ([adb83ce](https://android.googlesource.com/platform/frameworks/support/+/adb83ce3ab9c842b802587107e138253e28ce4f6), [b/143356547](https://issuetracker.google.com/143356547))
- Updated `WearableActionDrawView`to delay action drawer inflation until the drawer is opened for the first time. ([I01026](https://android-review.googlesource.com/q/I01026235e0282201b19bf63277ec78344bcdb070), [b/163870541](https://issuetracker.google.com/issues/163870541))

### Version 1.1.0-rc03

September 2, 2020

`androidx.wear:wear:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/07056667a38fffbc916fa2def4a5f0ce23d1933a..792501d04a4ca4858f27d36ec77bf3b35c3211af/wear/wear)

**Bug Fixes**

- Fixed issue with Action Drawer not showing content when it is opened. ([I01026](https://android-review.googlesource.com/q/I01026235e0282201b19bf63277ec78344bcdb070), [b/163870541](https://issuetracker.google.com/issues/163870541))

### Version 1.1.0-rc02

June 24, 2020

`androidx.wear:wear:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7128ce821b832b2f02be65d5cfc4a31b3d3aa04e..07056667a38fffbc916fa2def4a5f0ce23d1933a/wear/wear)

**Bug Fixes**

- Added a `layout_` prefix to boxedEdges attribute (now `layout_boxedEdges`) for `BoxInsetLayout` in order to comply with android naming convention. This will remove the linter error in Android Studio for these attributes.

### Version 1.1.0-rc01

May 14, 2020

`androidx.wear:wear:1.1.0-rc01` is released with no changes since `.1.0-beta01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..7128ce821b832b2f02be65d5cfc4a31b3d3aa04e/wear/wear)

### Version 1.1.0-beta01

April 29, 2020

`androidx.wear:wear:1.1.0-beta01` is released with no changes since `androidx.wear:wear:1.1.0-alpha01`. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..b752a10305d7cd58a7f50ad094ed54af4d765f27/webkit/webkit)

### Version 1.1.0-alpha01

April 15, 2020

`androidx.wear:wear:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..24daa503442fcd3e44ada60cf1da41df2815c045/wear/wear)

**API Changes**

- Added optional `EXTRA_ANIMATION_DURATION_MILLIS` to `ConfirmationActivity` to allow for the duration that the confirmation dialog is displayed. ([adb83ce](https://android.googlesource.com/platform/frameworks/support/+/adb83ce3ab9c842b802587107e138253e28ce4f6), [134523c](https://android.googlesource.com/platform/frameworks/support/+/134523c449b103383fc030ac033cd9a6282b287e), [b/143356547](https://issuetracker.google.com/143356547))

**Bug Fixes**

- Updated `WearableActionDrawView`to delay action drawer inflation until the drawer is opened for the first time. ([5cd32f7](https://android.googlesource.com/platform/frameworks/support/+/5cd32f7c870ad9b01428b9e51224992599e9e5fb))