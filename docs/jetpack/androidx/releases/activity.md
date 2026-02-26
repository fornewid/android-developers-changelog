---
title: https://developer.android.com/jetpack/androidx/releases/activity
url: https://developer.android.com/jetpack/androidx/releases/activity
source: md.txt
---

# Activity

[User Guide](https://developer.android.com/guide/components/activities/intro-activities) API Reference  
[androidx.activity](https://developer.android.com/reference/androidx/activity/package-summary)  
Access composable APIs built on top of Activity.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.12.4](https://developer.android.com/jetpack/androidx/releases/activity#1.12.4) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/activity#1.13.0-rc01) | - | - |

## Declaring dependencies

To add a dependency on Activity, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    def activity_version = "1.12.4"

    // Java language implementation
    implementation "androidx.activity:activity:$activity_version"
    // Kotlin
    implementation "androidx.activity:activity-ktx:$activity_version"
}
```

### Kotlin

```kotlin
dependencies {
    val activity_version = "1.12.4"

    // Java language implementation
    implementation("androidx.activity:activity:$activity_version")
    // Kotlin
    implementation("androidx.activity:activity-ktx:$activity_version")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:527362+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=527362&template=1189829)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.13

### Version 1.13.0-rc01

February 25, 2026

`androidx.activity:activity:1.13.0-rc01`, `androidx.activity:activity-compose:1.13.0-rc01`, and `androidx.activity:activity-ktx:1.13.0-rc01` are released. Version 1.13.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..6360e6fe078d931d2fcdd7076c6952c41b455f5d/activity).

**Bug Fixes**

- From [Activity 1.12.4](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/activity#1.12.4): The Photo and Video `ActivityResultContracts` now will correctly launch when being used on devices with the latest URI security fixes. ([I61201](https://android-review.googlesource.com/#/q/I612010ef247badc4cd926afa2130ef553ecd2f3e), [b/433708587](https://issuetracker.google.com/issues/433708587))

### Version 1.13.0-alpha01

January 14, 2026

`androidx.activity:activity:1.13.0-alpha01`, `androidx.activity:activity-compose:1.13.0-alpha01`, and `androidx.activity:activity-ktx:1.13.0-alpha01` are released. Version 1.13.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7ef667d42385c5b9200e987ab65005d1c3af7429..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/activity).

**New Features**

- `EdgeToEdge` is now re-invoked on configuration changes to ensure that the system status bar color is properly updated. ([Id1381](https://android-review.googlesource.com/#/q/Id1381f2ead0370317baeff80efbf40c4e469ebfd), [b/364713509](https://issuetracker.google.com/issues/364713509))

**API Changes**

- `ComponentActivity` now implements the `OnPictureInPictureUiStateChangedProvider` interface which means it can now integrate with the new `core:core-pip` artifact that allows allow any component to receive picture-in-picture ui state change events. ([I4df5c](https://android-review.googlesource.com/#/q/I4df5cf539a9ba7a248b8ead58e6de5b7d8f9d366), [b/441310308](https://issuetracker.google.com/issues/441310308))

**Bug Fixes**

- From Activity 1.12.2: Fixed an issue where manually setting `isEnabled` on a lifecycle-aware `OnBackPressedCallback` would override the `Lifecycle` state, potentially causing crashes. ([I7d898](https://android-review.googlesource.com/#/q/I7d8981a1d02f5e2bc7fb24f1a0e7987e412934d2), [b/461999811](https://issuetracker.google.com/issues/461999811))

## Version 1.12

### Version 1.12.4

February 11, 2026

`androidx.activity:activity:1.12.4`, `androidx.activity:activity-compose:1.12.4`, and `androidx.activity:activity-ktx:1.12.4` are released. Version 1.12.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0b457d57265743f41fa76fdd0d2235c9518f4e8a..d1ba6dcc5e581e7f1d2cc18466e48d5044a58d4e/activity).

**Bug Fixes**

- The Photo and Video `ActivityResultContracts` now will correctly launch when being used on devices with the latest URI security fixes. ([I61201](https://android-review.googlesource.com/#/q/I612010ef247badc4cd926afa2130ef553ecd2f3e), [b/433708587](https://issuetracker.google.com/issues/433708587))

### Version 1.12.3

January 28, 2026

`androidx.activity:activity:1.12.3`, `androidx.activity:activity-compose:1.12.3`, and `androidx.activity:activity-ktx:1.12.3` are released. Version 1.12.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7ef667d42385c5b9200e987ab65005d1c3af7429..6aa8a5085abed345526a544f3a498c19bca795fe/activity).

### Version 1.12.2

December 17, 2025

`androidx.activity:activity:1.12.2`, `androidx.activity:activity-compose:1.12.2`, and `androidx.activity:activity-ktx:1.12.2` are released. Version 1.12.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1bbe37f1d3fc8ca58ec9358a39fe2ad8f4d714e0..7ef667d42385c5b9200e987ab65005d1c3af7429/activity).

**Bug Fixes**

- Fixed an issue where manually setting isEnabled on a lifecycle-aware `OnBackPressedCallback` would override the Lifecycle state, potentially causing crashes. ([I7d898](https://android-review.googlesource.com/#/q/I7d8981a1d02f5e2bc7fb24f1a0e7987e412934d2), [b/461999811](https://issuetracker.google.com/issues/461999811))

### Version 1.12.1

December 03, 2025

`androidx.activity:activity:1.12.1`, `androidx.activity:activity-compose:1.12.1`, and `androidx.activity:activity-ktx:1.12.1` are released. Version 1.12.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/693a1dc9ba291b1c951cb7f2930fe3009e85e49e..1bbe37f1d3fc8ca58ec9358a39fe2ad8f4d714e0/activity).

**Updated Dependency**

- Activity now depends on [Navigation Event 1.0.1](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/navigationevent#1.0.1)

### Version 1.12.0

November 19, 2025

`androidx.activity:activity:1.12.0`, `androidx.activity:activity-compose:1.12.0`, and `androidx.activity:activity-ktx:1.12.0` are released. Version 1.12.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cc0d43d81e035bfc91fee2dd339c049e4fef8cc9..693a1dc9ba291b1c951cb7f2930fe3009e85e49e/activity).

**Important changes since 1.11.0:**

- The `Androidx Activity` library is now dependent on the new `NavigationEvent` library. This includes support for the `NavigationEventDispatcher` in `ComponentActivity` and `ComponentDialog`. The `OnBackPressed` APIs have also been rewritten on top of the `NavigationEvent` APIs to ensure it is backward compatible with the previous library.

### Version 1.12.0-rc01

November 05, 2025

`androidx.activity:activity:1.12.0-rc01`, `androidx.activity:activity-compose:1.12.0-rc01`, and `androidx.activity:activity-ktx:1.12.0-rc01` are released. Version 1.12.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..bcc8bee1eb595dcb47e9d7acf0379692cc49061f/activity).

**Bug Fixes**

- Fix runtime failures for `BackHandler` and `PredictiveBackHandler` in apps using custom Activity classes. These composables now safely fall back to `LocalOnBackPressedDispatcherOwner` while preserving dispatch order in apps that support `NavigationEventDispatcherOwner`. ([I43873](https://android-review.googlesource.com/#/q/I43873459dbaa00b35fbf22f6fc5e9172f97198d2))

### Version 1.12.0-beta01

October 22, 2025

`androidx.activity:activity:1.12.0-beta01`, `androidx.activity:activity-compose:1.12.0-beta01`, and `androidx.activity:activity-ktx:1.12.0-beta01` are released. Version 1.12.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/activity).

**API Changes**

- Introduce the experimental `ActivityFlags` API for managing runtime behavior changes and migrations. The first flag enables stable ordering for `OnBackPressedCallback`, making back navigation more predictable across lifecycle changes. Developers can opt out by setting `ActivityFlags.isOnBackPressedLifecycleOrderMaintained = false`. ([I06bdf](https://android-review.googlesource.com/#/q/I06bdf646214ba5b3501adba53f9a35f1f267ce21), [Id08bb](https://android-review.googlesource.com/#/q/Id08bbadb07591edefd5454d16a61278412c7eb67), [I439aa](https://android-review.googlesource.com/#/q/I439aaeeb5e101766a94d1ce641eac35a18460b36), [b/422730945](https://issuetracker.google.com/issues/422730945), [b/450533622](https://issuetracker.google.com/issues/450533622))

**Dependency Update**

- Update lifecycle dependencies to 2.9.4 ([Ic9fb2](https://android-review.googlesource.com/#/q/Ic9fb28c689235a1bea62f9c98dde06aee1e8172e))

### Version 1.12.0-alpha09

September 24, 2025

`androidx.activity:activity:1.12.0-alpha09`, `androidx.activity:activity-compose:1.12.0-alpha09`, and `androidx.activity:activity-ktx:1.12.0-alpha09` are released. Version 1.12.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/activity).

**Dependency Changes**

- Activity now depends on [Navigation Event 1.0.0-alpha08](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha09).

### Version 1.12.0-alpha08

September 10, 2025

`androidx.activity:activity:1.12.0-alpha08`, `androidx.activity:activity-compose:1.12.0-alpha08`, and `androidx.activity:activity-ktx:1.12.0-alpha08` are released. Version 1.12.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/activity).

**Dependency Update**

- Activity now depends on [Navigation Event 1.0.0-alpha08](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha08).

### Version 1.12.0-alpha07

August 27, 2025

`androidx.activity:activity:1.12.0-alpha07`, `androidx.activity:activity-compose:1.12.0-alpha07`, and `androidx.activity:activity-ktx:1.12.0-alpha07` are released. Version 1.12.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/activity).

**Bug Fixes**

- Fixed an issue with `EdgeToEdge` on API 35 in which invisible views caused unexpected measurement insets. ([If49ff](https://android-review.googlesource.com/#/q/If49ff4fea1670dfc4c3bb98c5f37ea4123ae5c29))

**Dependency Update**

- Activity now depends on [Navigation Event `1.0.0-alpha07`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha07).

### Version 1.12.0-alpha06

August 13, 2025

`androidx.activity:activity:1.12.0-alpha06`, `androidx.activity:activity-compose:1.12.0-alpha06`, and `androidx.activity:activity-ktx:1.12.0-alpha06` are released. Version 1.12.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..c359e97fece91f3767a7d017e9def23c7caf1f53/activity).

**MinSdk Update**

- The default `minSdk` for the AndroidX has been moved from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

**Documentation Updates**

- Updated KDocs for `PredictiveBackHandler` to call out a known timing issue where it may process a gesture in the same frame it is disabled. ([I5be5c](https://android-review.googlesource.com/#/q/I5be5c49bc7b430b16c7a7c9a86b1b18820682be4), [b/431534103](https://issuetracker.google.com/issues/431534103))
- Updated KDocs for `BackHandler` and `PredictiveBackHandler` to explicitly state the 'last composed wins' behavior in addition to recommending unconditional composition with the `enabled` flag. ([I7ab94](https://android-review.googlesource.com/#/q/I7ab943c77b627402cb2cbfbca4fe790be35934cf))

**Dependency update**

- Activity now depends on [Navigation Event `1.0.0-alpha06`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha06).

### Version 1.12.0-alpha05

July 30, 2025

`androidx.activity:activity:1.12.0-alpha05`, `androidx.activity:activity-compose:1.12.0-alpha05`, and `androidx.activity:activity-ktx:1.12.0-alpha05` are released. Version 1.12.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..5fa9d0954ece0376736164b0f7bc2ef33506ab70/activity).

**Dependency Update**

- Activity now depends on [Navigation Event `1.0.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha05).

### Version 1.12.0-alpha04

July 2, 2025

`androidx.activity:activity:1.12.0-alpha04`, `androidx.activity:activity-compose:1.12.0-alpha04`, and `androidx.activity:activity-ktx:1.12.0-alpha04` are released. Version 1.12.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..1b437892629a2cdedb46d9b7232575987b2cc6b5/activity).

**Dependency Changes**

- Activity now depends on [NavigationEvent Alpha04](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha04)

### Version 1.12.0-alpha03

June 18, 2025

`androidx.activity:activity:1.12.0-alpha03`, `androidx.activity:activity-compose:1.12.0-alpha03`, and `androidx.activity:activity-ktx:1.12.0-alpha03` are released. Version 1.12.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/activity).

**Bug Fixes**

- `OnBackPressedDispatcher` and `NavigationEventDispatcher` are now both initialized lazily in `ComponentActivity`. ([I710e6](https://android-review.googlesource.com/#/q/I710e6cc0ef99009aff88c09a594e8c31bf204464))

- Fixed issues with `OnBackPressedDistpatcher` that caused the following:

  - Only the latest dispatcher an `OnBackPressedCallback` was added to being notified of its enabled state ([b/418715930](https://issuetracker.google.com/issues/418715930))
  - `OnBackPressedDispatcher` removes the wrong callback when using the `addCallback` function that takes a lifecycle. ([b/422714753](https://issuetracker.google.com/issues/422714753))
  - `OnBackPressedDispatcher.remove()` does not remove all instances of a registered `OnBackPressedCallback`. ([b/423024414](https://issuetracker.google.com/issues/423024414))

### Version 1.12.0-alpha02

June 4, 2025

`androidx.activity:activity:1.12.0-alpha02`, `androidx.activity:activity-compose:1.12.0-alpha02`, and `androidx.activity:activity-ktx:1.12.0-alpha02` are released. Version 1.12.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..786176dc2284c87a0e620477608e0aca9adeff15/activity).

**Bug Fixes**

- From [NavigationEvent `1.0.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha02): Fixed a `ConcurrentModificationException` that could occur when `NavigationEventCallback.remove()` was called due to simultaneously modifying the internal list of closeables. ([I63066](https://android-review.googlesource.com/#/q/I6306693f5fd98795f68917d7c6fac8b90a3c6a1c))

### Version 1.12.0-alpha01

May 20, 2025

`androidx.activity:activity:1.12.0-alpha01`, `androidx.activity:activity-compose:1.12.0-alpha01`, and `androidx.activity:activity-ktx:1.12.0-alpha01` are released. Version 1.12.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f6e1691e353bc6b305e5f0fdf597f075d05d68c4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/activity).

**New Features**

- `ComponentActivity` and `ComponentDialog` have been integrated with [NavigationEvent `1.0.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha01) via the `NavigationEventDispatcherOwner` API. You can now retrieve a `NavigationEventDispatcher` from your `ComponentActivity` via the `navigationEventDispatcher` field. Since the `OnBackPressedDispatcher` has been re-written on top of the new library all previous usages should continue to work correctly. You should use `NavigationEventDispatcher` and `NavigationEventCallback` going forward. ([Ib8eed](https://android-review.googlesource.com/#/q/Ib8eedae8ea39de8d4dc7352f11b98ac2ad8001ad), [I6cc44](https://android-review.googlesource.com/#/q/I6cc446a896f45ea57b3f76a15d4ff3e8f6ff168c), [Ib7724](https://android-review.googlesource.com/#/q/Ib7724f1a236de3d3ce44d9a3efc79164cb177f63), [I9a0f7](https://android-review.googlesource.com/#/q/I9a0f78646525cb1de4d7626fa1e7479f16b01f20),[b/412597031](https://issuetracker.google.com/issues/412597031), [b/415028038](https://issuetracker.google.com/issues/415028038), [b/412596729](https://issuetracker.google.com/issues/412596729), [b/412597140](https://issuetracker.google.com/issues/412597140), [b/412596012](https://issuetracker.google.com/issues/412596012))

## Version 1.11

### Version 1.11.0

September 10, 2025

`androidx.activity:activity:1.11.0`, `androidx.activity:activity-compose:1.11.0`, and `androidx.activity:activity-ktx:1.11.0` are released. Version 1.11.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f6e1691e353bc6b305e5f0fdf597f075d05d68c4..cc0d43d81e035bfc91fee2dd339c049e4fef8cc9/activity).

**Important changes since 1.10.0:**

- Added `MediaCapabilities` API to `PickVisualMediaRequest` to let applications specify its media capabilities, such as supported HDR Types.
- Activity is now compiled with API 36.

### Version 1.11.0-rc01

April 23, 2025

`androidx.activity:activity:1.11.0-rc01`, `androidx.activity:activity-compose:1.11.0-rc01`, and `androidx.activity:activity-ktx:1.11.0-rc01` are released. Version 1.11.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..f6e1691e353bc6b305e5f0fdf597f075d05d68c4/activity).

### Version 1.11.0-beta01

April 9, 2025

`androidx.activity:activity:1.11.0-beta01`, `androidx.activity:activity-compose:1.11.0-beta01`, and `androidx.activity:activity-ktx:1.11.0-beta01` are released. Version 1.11.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..4c37298a97c16270c139eb812ddadaba03e23a52/activity).

### Version 1.11.0-alpha02

March 26, 2025

`androidx.activity:activity:1.11.0-alpha02`, `androidx.activity:activity-compose:1.11.0-alpha02`, and `androidx.activity:activity-ktx:1.11.0-alpha02` are released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/activity).

**API Changes**

- Integrated the new `EDGE_NONE` and `frameTimeMillis` from Android 16 Beta03 into the `BackEventCompat` provided by `OnBackPressedCallback`'s `handleOnBackStarted` and `handleOnBackProgressed` functions.

**Dependency Updates**

- Activity is now compiled with API 36. ([I510e8](https://android-review.googlesource.com/#/q/I510e8f026436f72b000eae153f627b02b1f1e2a3), [b/301910674](https://issuetracker.google.com/issues/301910674))

### Version 1.11.0-alpha01

March 12, 2025

`androidx.activity:activity:1.11.0-alpha01`, `androidx.activity:activity-compose:1.11.0-alpha01`, and `androidx.activity:activity-ktx:1.11.0-alpha01` are released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/261165aaaecdddde7e136be4f706bb9f5e1b8b34..7a145e052ae61e272e91ffe285e9451b8ab71870/activity).

**New Features**

- Added `MediaCapabilities` API to `PickVisualMediaRequest` to let applications specify its media capabilities, such as supported HDR Types. ([Ic3ee7](https://android-review.googlesource.com/#/q/Ic3ee73985c6aacaf86b1c4a71b54e80b7ed7c3cc))

## Version 1.10

### Version 1.10.1

February 26, 2025

`androidx.activity:activity:1.10.1`, `androidx.activity:activity-compose:1.10.1`, and `androidx.activity:activity-ktx:1.10.1` are released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/54846baa440355b8e6183df33fdad02e17566c75..261165aaaecdddde7e136be4f706bb9f5e1b8b34/activity).

**Bug Fixes**

- `ViewTree` `OnBackPressedDispatcherOwners` and `FullyDrawnReporterOwners` can now be resolved through disjoint parents of a view, such as a `ViewOverlay`. See the release notes of core or the documentation in `ViewTree.setViewTreeDisjointParent` for more information on disjoint view parents. ([Ie7750](https://android-review.googlesource.com/#/q/Ie77506e9490d3bbc7e36c7d05510308ffc15a584))

### Version 1.10.0

January 15, 2025

`androidx.activity:activity:1.10.0`, `androidx.activity:activity-compose:1.10.0`, and `androidx.activity:activity-ktx:1.10.0` are released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6164e1df97417c3dbf36eaf7c79975f1543fab3b..54846baa440355b8e6183df33fdad02e17566c75/activity).

**Important changes since 1.9.0**

- `PhotoPicker` now allows picking images in order and choosing which tab (either albums or images) should be initially visible.
- The `PickVisualMedia` and `PickMultipleVisualMedia` Activity Result contracts that trigger the Photo Picker no longer directly delegates to Google Play services if the system Photo picker is not available, but uses the public `ACTION_SYSTEM_FALLBACK_PICK_IMAGES` action and related extras to provide a consistent Photo Picker experience to OEMs and system apps as a fallback.
- New `LocalActivity` composition local that provides the `Activity` for the current scope, removing the need for developers to get an `Activity` from the `LocalContext`.

### Version 1.10.0-rc01

December 11, 2024

`androidx.activity:activity:1.10.0-rc01`, `androidx.activity:activity-compose:1.10.0-rc01`, and `androidx.activity:activity-ktx:1.10.0-rc01` are released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..6164e1df97417c3dbf36eaf7c79975f1543fab3b/activity).

**Bug Fixes**

- Fixed an issue where changing the enabled state while the `PredictiveBackHandler` is currently active would short circuit the callback immediately. It will now finish the current callback regardless of the enabled status changes. ([Ib8719](https://android-review.googlesource.com/#/q/Ib871962b429baa044d1993817e9cd2dd231b506f))

### Version 1.10.0-beta01

November 13, 2024

`androidx.activity:activity:1.10.0-beta01`, `androidx.activity:activity-compose:1.10.0-beta01`, and `androidx.activity:activity-ktx:1.10.0-beta01` are released with no changes since the last alpha. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/activity).

### Version 1.10.0-alpha03

October 30, 2024

`androidx.activity:activity:1.10.0-alpha03`, `androidx.activity:activity-compose:1.10.0-alpha03`, and `androidx.activity:activity-ktx:1.10.0-alpha03` are released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/activity).

**API Changes**

- Added a new `LocalActivity` composition local that provides the `Activity` for the current scope, removing the need for developers to get an `Activity` from the `LocalContext`. It also comes with a new lint rule that checks when the `LocalContext` is incorrectly being cast to an `Activity`. ([I7746a](https://android-review.googlesource.com/#/q/I7746aaaeb779d7af79867b4d9143b9d5c5545543), [b/283009666](https://issuetracker.google.com/issues/283009666))

**Bug Fixes**

- From [Activity `1.9.3`](https://developer.android.com/jetpack/androidx/releases/activity#1.9.3): `PredictiveBackHandler` will no longer fire it's callback after the handler has been disabled. This will fix an issue where the `NavHost` from Navigation Compose would throw an `IndexOutOfBoundsException`. ([I3f75e](https://android-review.googlesource.com/#/q/I3f75eb2415f39b914f18cf4b87bf4ed57bb5a483), [b/365027664](https://issuetracker.google.com/issues/365027664), [b/340202286](https://issuetracker.google.com/issues/340202286))

**Dependency Update**

- Activity Compose now depends on Compose Runtime 1.7.0 ([I7746a](https://android-review.googlesource.com/#/q/I7746aaaeb779d7af79867b4d9143b9d5c5545543), [b/283009666](https://issuetracker.google.com/issues/283009666))

### Version 1.10.0-alpha02

September 4, 2024

`androidx.activity:activity:1.10.0-alpha02`, `androidx.activity:activity-compose:1.10.0-alpha02`, and `androidx.activity:activity-ktx:1.10.0-alpha02` are released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/189dc77df5357bfd41bebee4e837cb12f825d2e2..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/activity).

**Behavior Changes**

- The `PickVisualMedia` and `PickMultipleVisualMedia` Activity Result contracts that trigger the Photo Picker no longer directly delegates to Google Play services if the system Photo picker is not available, but uses the public `ACTION_SYSTEM_FALLBACK_PICK_IMAGES` action and related extras to provide a consistent Photo Picker experience to OEMs and system apps as a fallback. This should have no effect on the user experience for devices that have a recent version of Google Play services. ([I3513d](https://android-review.googlesource.com/#/q/I3513de5543be10405fa77cdaeb200ce94884e95c))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([I9496c](https://android-review.googlesource.com/#/q/I9496cfaeb50a5c484fbee6521b74a0605fb013dc), [b/345472586](https://issuetracker.google.com/issues/345472586))
- From [Activity `1.9.2`](https://developer.android.com/jetpack/androidx/releases/activity#1.9.2): Fixed an issue where the Activity Compose `PredictiveBackHandler` API would continue to handle the system back gesture on the frame it was disabled, which could result in libraries like Navigation Compose to handle back even with an empty back stack, resulting in it throwing an `IndexOutOfBoundsException`. ([Ie3301](https://android-review.googlesource.com/#/q/Ie3301e4a06593101bc48c447f3a9505a1de5d6a3), [b/340202286](https://issuetracker.google.com/issues/340202286))
- From [Activity `1.9.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.9.1): Fixed an issue with `PredictiveBackHandler` where after doing system back, attempting to do `onBackPressed` from the `OnBackPressedDispatcher` would fail. ([I5f1f8](https://android-review.googlesource.com/#/q/I5f1f8075fb3abac768761e0e8889254d4c31f81e))

### Version 1.10.0-alpha01

June 26, 2024

`androidx.activity:activity:1.10.0-alpha01`, `androidx.activity:activity-compose:1.10.0-alpha01`, and `androidx.activity:activity-ktx:1.10.0-alpha01` are released. This version is developed in an internal branch.

**New Features**

- Added support for new `PhotoPicker` features introduced in Android V including being able to pick images in order and choose which tab (either albums or images) should be initially visible.

## Version 1.9

### Version 1.9.3

October 16, 2024

`androidx.activity:activity:1.9.3`, `androidx.activity:activity-compose:1.9.3`, and `androidx.activity:activity-ktx:1.9.3` are released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7334f3f60ac9828792ba48a5ae0d16d5c704154b..ff392ed574e0279bee748d48276071b6b522277d/activity).

**Bug Fixes**

- `PredictiveBackHandler` will no longer fire it's callback after the handler has been disabled. This will fix an issue where the `NavHost` from Navigation Compose would throw an `IndexOutOfBoundsException`. ([I3f75e](https://android-review.googlesource.com/#/q/I3f75eb2415f39b914f18cf4b87bf4ed57bb5a483), [b/340202286](https://issuetracker.google.com/issues/340202286))

### Version 1.9.2

September 4, 2024

`androidx.activity:activity:1.9.2`, `androidx.activity:activity-compose:1.9.2`, and `androidx.activity:activity-ktx:1.9.2` are released. Version 1.9.2 contains [these lthcocommits](https://android.googlesource.com/platform/frameworks/support/+log/7e8da50b9a7dfb9e425f15a65d6d0a464361604b..7334f3f60ac9828792ba48a5ae0d16d5c704154b/activity).

**Bug Fixes**

- Fixed an issue where the Activity Compose `PredictiveBackHandler` API would continue to handle the system back gesture on the frame it was disabled, which could result in libraries like Navigation Compose to handle back even with an empty back stack, resulting in it throwing an `IndexOutOfBoundsException`. ([Ie3301](https://android-review.googlesource.com/#/q/Ie3301e4a06593101bc48c447f3a9505a1de5d6a3), [b/340202286](https://issuetracker.google.com/issues/340202286))

### Version 1.9.1

July 24, 2024

`androidx.activity:activity:1.9.1`, `androidx.activity:activity-compose:1.9.1`, and `androidx.activity:activity-ktx:1.9.1` are released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fdf742dd71a144f62554c9d810891993dcfb9fa8..7e8da50b9a7dfb9e425f15a65d6d0a464361604b/activity).

**Bug Fixes**

- Fixed an issue with `PredictiveBackHandler` where after doing system back, attempting to do `onBackPressed` from the `OnBackPressedDispatcher` would fail. ([I5f1f8](https://android-review.googlesource.com/#/q/I5f1f8075fb3abac768761e0e8889254d4c31f81e))

### Version 1.9.0

April 17, 2024

`androidx.activity:activity:1.9.0`, `androidx.activity:activity-compose:1.9.0`, and `androidx.activity:activity-ktx:1.9.0` are released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80bdf43686b9fa5e4c31299217168d73df5c9243..fdf742dd71a144f62554c9d810891993dcfb9fa8/activity).

**Important changes since 1.8.0**

- `ComponentActivity` now implements `OnUserLeaveHintProvider` to allow components to callbacks for `onUserLeaveHint` events.
- The `OnBackPressedCallback`, `BackHandler`, and `PredictiveBackHandler` APIs now warn when calling `onBackPressedDispatcher.onBackPressed()` when handling back as that will always break the [Predictive Back Animation](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture). See the [best practices guide](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#ui-logic) for more details.
- The remainder of the Activity APIs have been rewritten in Kotlin and all extensions previously available in `activity-ktx` have been moved to `activity`. `activity-ktx` is now completely empty.
  - As part of the conversion of `ActivityResultLauncher` to Kotlin, the `getContract` method is now an abstract Kotlin property. This is a binary compatible change, but source breaking if your implementation of `ActivityResultLauncher` is written in Kotlin.

### Version 1.9.0-rc01

April 3, 2024

`androidx.activity:activity:1.9.0-rc01`, `androidx.activity:activity-compose:1.9.0-rc01`, and `androidx.activity:activity-ktx:1.9.0-rc01` are released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..80bdf43686b9fa5e4c31299217168d73df5c9243/activity).

**Dependency update**

- Activity now depends on [Profile Installer 1.3.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.1).

### Version 1.9.0-beta01

March 20, 2024

`androidx.activity:activity:1.9.0-beta01`, `androidx.activity:activity-compose:1.9.0-beta01`, and `androidx.activity:activity-ktx:1.9.0-beta01` are released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..a57d7d17753695012b58c9ce7ad55a8d39157e62/activity).

**Bug Fixes**

- Fixed an Activity startup performance regression introduced in [Activity `1.9.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.9.0-alpha02) caused by calling the `OnBackPressedDispatcher` as part of the creation of the Activity. ([Ie75e3](https://android-review.googlesource.com/#/q/Ie75e392c506ea3f142df175ae62dde7fd8220821))

### Version 1.9.0-alpha03

February 7, 2024

`androidx.activity:activity:1.9.0-alpha03`, `androidx.activity:activity-compose:1.9.0-alpha03`, and `androidx.activity:activity-ktx:1.9.0-alpha03` are released. [Version 1.9.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..ca2a8cf8da3a3502fccc593974f8085653e38261/activity)

**Lint Warning**

- The `OnBackPressedCallback`, `BackHandler`, and `PredictiveBackHandler` APIs now warn when calling `onBackPressedDispatcher.onBackPressed()` when handling back as that will always break the [Predictive Back Animation](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture). See the [best practices guide](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#ui-logic) for more details. ([1e4222](https://android.googlesource.com/platform/frameworks/support/+/1e4222b878bd2a990871d75fa744995d09acedb9), [2c950d](https://android.googlesource.com/platform/frameworks/support/+/2c950d0cfc22551a989265c4ffde9f69d5c69235), [b/287505200](https://issuetracker.google.com/287505200))

**Bug Fixes**

- If a back event is sent from the system started during an already running Predictive Back Gesture, the currently running Predictive Back Gesture is canceled and the new back event takes over to begin a new Predictive Back Gesture. ([I3482e](https://android-review.googlesource.com/#/q/I3482edb367c56c3feba833c7ba8cedf3293467bb))
- Fixed a crash when accessing the `onBackPressedDispatcher` from a `ComponentActivity` for the first time from a background thread. It is now safe to access the `onBackPressedDispatcher` on any thread. ([I79955](https://android-review.googlesource.com/#/q/I7995575573270fec6f01c4b87e40a86cd713327b))

### Version 1.9.0-alpha02

January 24, 2024

`androidx.activity:activity:1.9.0-alpha02`, `androidx.activity:activity-compose:1.9.0-alpha02`, and `androidx.activity:activity-ktx:1.9.0-alpha02` are released. [Version 1.9.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/activity)

**Kotlin Conversions**

- `ActivityResultRegistry` has been rewritten in Kotlin. This ensures that the nullability of the generics on the contract passed to `register` will correctly be passed through to the `ActivityResultLauncher` returned to you. ([I121f0](https://android-review.googlesource.com/#/q/I121f0ca842066fb73ab0e51b89720029e991407a))
- `ActivityResult` has been rewritten in Kotlin. The `ActivityResult` Kotlin extensions that support destructuring into the `resultCode` and `data` fields have been moved from `activity-ktx` to `activity`. ([I0565a](https://android-review.googlesource.com/#/q/I0565a95aa4470a4cd23dcddf75df3f9dd8dca19e))
- The Kotlin extensions of `by viewModels()` for `ComponentActivity` and `trackPipAnimationHintView` have been moved from `activity-ktx` to `activity`. The `activity-ktx` artifact is now completely empty. ([I0a444](https://android-review.googlesource.com/#/q/I0a444140b10671bbfbb5aeab66f1a3a7e9d28061))

**Bug Fixes**

- The `enableEdgeToEdge` API now draws around any display cutouts. ([a3644b](https://android.googlesource.com/platform/frameworks/support/+/a3644b966f658b5b726eb8dc7c60d370194d250d), [b/311173461](https://issuetracker.google.com/311173461))
- From [Activity `1.8.2`](https://developer.android.com/jetpack/androidx/releases/activity#1.8.2): Fixed the extra passed to the Photo Picker Activity Contract's `ACTION_SYSTEM_FALLBACK_PICK_IMAGES` to correctly pass it the `EXTRA_SYSTEM_FALLBACK_PICK_IMAGES_MAX` key, rather than using the extra with the key `"com.google.android.gms.provider.extra.PICK_IMAGES_MAX"`. It is strongly recommended if you are an OEM who implements a system fallback Photo Picker to support both extras to ensure the widest compatibility. ([I96a00](https://android-review.googlesource.com/#/q/I96a00ed51416a3ea65705357157127091a24f189))

### Version 1.9.0-alpha01

November 29, 2023

`androidx.activity:activity:1.9.0-alpha01`, `androidx.activity:activity-compose:1.9.0-alpha01`, and `androidx.activity:activity-ktx:1.9.0-alpha01` are released. [Version 1.9.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b9ef80de74ee258455627f176f46da81e48ac3b2..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/activity)

**New Features**

- `ComponentActivity` now implements `OnUserLeaveHintProvider` to allow components to callbacks for `onUserLeaveHint` events. ([I54892](https://android-review.googlesource.com/#/q/I54892c9ab5a8a002164b9f98cd31e02d56d73da7))

**API Changes**

- `ComponentActivity` has been rewritten in Kotlin. ([I14f31](https://android-review.googlesource.com/#/q/I14f312d6879ce6c91496112fb6b171f81cdbddf2))
- `ActivityResultCaller` has been rewritten in Kotlin. ([Ib02e4](https://android-review.googlesource.com/#/q/Ib02e49c49dbed2ce0d25ac71c8caf0325ffb8142))
- `ActivityResultLauncher` has been rewritten in Kotlin. As part of that conversion, the `getContract` method is now an abstract Kotlin property. This is a binary compatible change, but source breaking if your implementation of `ActivityResultLauncher` is written in Kotlin. ([Id4615](https://android-review.googlesource.com/#/q/Id4615d19b383b2438be6a8f68da7584394d13515))
- `PickVisualMediaRequest` now has the same minimum API level of 19 as the `PickVisualMedia` Activity Result contract. ([Id6e21](https://android-review.googlesource.com/#/q/Id6e21cd21f91dd81bcb1c3b23286e5528ffa7cd6))

**Dependency Update**

- Activity now depends on [Core `1.13.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/core#1.13.0-alpha01). ([I14f31](https://android-review.googlesource.com/#/q/I14f312d6879ce6c91496112fb6b171f81cdbddf2))

## Version 1.8

### Version 1.8.2

December 13, 2023

`androidx.activity:activity:1.8.2`, `androidx.activity:activity-compose:1.8.2`, and `androidx.activity:activity-ktx:1.8.2` are released. [Version 1.8.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b9ef80de74ee258455627f176f46da81e48ac3b2..f9666ddb040689f37dc8a7955e26a0669f458da1/activity)

**Bug Fixes**

- Fixed the extra passed to the Photo Picker Activity Contract's `ACTION_SYSTEM_FALLBACK_PICK_IMAGES` to correctly pass it the `EXTRA_SYSTEM_FALLBACK_PICK_IMAGES_MAX` key, rather than using the extra with the key `"com.google.android.gms.provider.extra.PICK_IMAGES_MAX"`. It is strongly recommended if you are an OEM who implements a system fallback Photo Picker to support both extras to ensure the widest compatibility. ([I96a00](https://android-review.googlesource.com/#/q/I96a00ed51416a3ea65705357157127091a24f189))

### Version 1.8.1

November 15, 2023

`androidx.activity:activity:1.8.1`, `androidx.activity:activity-compose:1.8.1`, and `androidx.activity:activity-ktx:1.8.1` are released. [Version 1.8.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed4ce88fa7e2b68e312ef93f7a97744620a7d03..b9ef80de74ee258455627f176f46da81e48ac3b2/activity)

**Bug Fixes**

- `OnBackPressedDispatcher` now continues to dispatch to the correct `OnBackPressedCallback` even after a new `OnBackPressedCallback` is added while the back gesture is being handled. ([Id0ff6](https://android-review.googlesource.com/#/q/Id0ff6b50a2a7f721fc13bab5ca63f620f1e3e25e))

### Version 1.8.0

October 4, 2023

`androidx.activity:activity:1.8.0`, `androidx.activity:activity-compose:1.8.0`, and `androidx.activity:activity-ktx:1.8.0` are released. [Version 1.8.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d494531b988564d977d4d601c6df5ccf2ac6861a..9ed4ce88fa7e2b68e312ef93f7a97744620a7d03/activity)

**Important changes since 1.7.0**

- **Predictive Back** - The `OnBackPressedCallback` now offers new Predictive Back callbacks for handling the back gesture starting, progress throughout the gesture, and the back gesture being canceled in addition to the previous `handleOnBackPressed()` callback for when the back gesture is committed. This also comes with the `PredictiveBackHandler` Composable to handle predictive back gesture events in Activity Compose. It provides a Flow of BackEventCompat objects that must be collected in the suspending lamba you provide:

      PredictiveBackHandler { progress: Flow<BackEventCompat> ->
        // code for gesture back started
        try {
          progress.collect { backEvent ->
          // code for progress
        }
        // code for completion
        } catch (e: CancellationException) {
          // code for cancellation
        }
      }

`ComponentActivity.onBackPressed()` has now been deprecated in favor of the APIs for handling back. Developers should now utilize the `OnBackPressedDispatcher`, rather than overriding this method.

- **EdgeToEdge** - `ComponentActivity.enableEdgeToEdge()` has been added to easily set up the edge-to-edge display in a backward-compatible manner.

### Version 1.8.0-rc01

September 20, 2023

`androidx.activity:activity:1.8.0-rc01`, `androidx.activity:activity-compose:1.8.0-rc01`, and `androidx.activity:activity-ktx:1.8.0-rc01` are released. [Version 1.8.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..d494531b988564d977d4d601c6df5ccf2ac6861a/activity)

### Version 1.8.0-beta01

September 6, 2023

`androidx.activity:activity:1.8.0-beta01`, `androidx.activity:activity-compose:1.8.0-beta01`, and `androidx.activity:activity-ktx:1.8.0-beta01` are released. [Version 1.8.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/activity)

**Documentation Improvement**

- Improved the documentation of `BackEventCompat`. ([aosp/2722254](https://android-review.googlesource.com/c/platform/frameworks/support/+/2722254))

### Version 1.8.0-alpha07

August 23, 2023

`androidx.activity:activity:1.8.0-alpha07`, `androidx.activity:activity-compose:1.8.0-alpha07`, and `androidx.activity:activity-ktx:1.8.0-alpha07` are released. [Version 1.8.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a83d3b232cf53ff8483130686a9d19ae65b7919f..3315f1ef094c312203fe26841287902916fbedf5/activity)

**New Features**

- Activity Compose has added a new `PredictiveBackHandler` Composable to handle predictive back gesture events. It provides a `Flow` of `BackEventCompat` objects that must be collected in the suspending lamba you provide:

      PredictiveBackHandler { progress: Flow<BackEventCompat> ->
        // code for gesture back started
        try {
          progress.collect { backEvent ->
          // code for progress
        }
        // code for completion
        } catch (e: CancellationException) {
          // code for cancellation
        }
      }

  It also comes with a compile time warning via lint rule to ensure the `Flow` calls `collect()`. ([Id2773](https://android-review.googlesource.com/#/q/Id27732d3729a866399eea48c188995275c0f5255), [b/294884345](https://issuetracker.google.com/issues/294884345))
- The `onBackPressedDispatcher` in `ComponentActivity` is now initialized lazily so that it is only created when required. ([I0bf8e](https://android-review.googlesource.com/#/q/I0bf8e1b37c55bbd0dbc2b69ff7e224fb2409daa8))

**Bug Fixes**

- `ComponentActivity` will no longer show a NPE on Android 13 when it gets an `onBackPressed()` callback and the Activity has already been `DESTROYED`. ([Idb055](https://android-review.googlesource.com/#/q/Idb0555c76dd63173a1fa93e34b8bc622500b9176), [b/291869278](https://issuetracker.google.com/issues/291869278))
- Removed usages of experimental `isAtLeastU()` API ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87), [b/289269026](https://issuetracker.google.com/issues/289269026))

### Version 1.8.0-alpha06

June 21, 2023

`androidx.activity:activity:1.8.0-alpha06`, `androidx.activity:activity-compose:1.8.0-alpha06`, and `androidx.activity:activity-ktx:1.8.0-alpha06` are released. [Version 1.8.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..3b5b931546a48163444a9eddc533489fcddd7494/activity)

**New Features**

- The `OnBackPressedDispatcher` now correctly cancels any callbacks that are removed during a Predictive Back Gesture. ([I3f90f](https://android-review.googlesource.com/#/q/I3f90fd77d0b34477cb63232aa9cfecf5c39904fc))

**API Changes**

- When passing `SystemBarStyle.auto` to the `enableEdgeToEdge` API, you can now override the `detectDarkMode` lambda parameter to provide custom logic for detecting night mode. ([aosp/2546393](https://android-review.googlesource.com/2546393), [b/278263793](https://issuetracker.google.com/278263793))

### Version 1.8.0-alpha05

June 7, 2023

`androidx.activity:activity:1.8.0-alpha05`, `androidx.activity:activity-compose:1.8.0-alpha05`, and `androidx.activity:activity-ktx:1.8.0-alpha05` are released. This version is developed in an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**API Changes**

- Activity now provides a `BackEventCompat` class that serves as a backward compatible version of `BackEvent` that is decoupled from the framework `BackEvent` class.
- **Breaking change:** The `handleOnBackStarted` and `handleOnBackProgressed` methods of `OnBackPressedCallback` now receive an `androidx.activity.BackEventCompat` instance rather than a framework `android.window.BackEvent` class. The equivalent `@VisibleForTesting` APIs on `OnBackPressedDispatcher` have also been updated.
- The constructor for `OnBackPressedDispatcher` now takes an optional `Consumer<Boolean>` instance that allows the owners of the dispatcher to receive a callback whenever the number of enabled callbacks changes from zero to non-zero or vice versa.

**Bug Fixes**

- From [Activity `1.7.2`](https://developer.android.com/jetpack/androidx/releases/activity#1.7.2): Fix `ReportDrawn` crashing when navigating away from a screen before `report` is called. ([Ic46f1](https://android-review.googlesource.com/#/q/Ic46f17d4dfd9a0758398564dce72fbb5f637626e), [b/260506820](https://issuetracker.google.com/issues/260506820))

### Version 1.8.0-alpha04

May 10, 2023

`androidx.activity:activity:1.8.0-alpha04`, `androidx.activity:activity-compose:1.8.0-alpha04`, and `androidx.activity:activity-ktx:1.8.0-alpha04` are released. This was released from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the [Android 14 (Upside Down Cake) Beta 2 SDK](https://developer.android.com/about/versions/14#beta-2).

**Bug Fixes**

- From [Activity 1.7.1](https://developer.android.com/jetpack/androidx/releases/activity#1.7.1): - The `ReportFullyDrawExecuter` no longer leaks when using `ComponentActivity` with `ActivityScenario`. ([Id2ff2](https://android-review.googlesource.com/#/q/Id2ff2311e16d89fc7309a6e99f302cf3e8d9d595), [b/277434271](https://issuetracker.google.com/277434271))

### Version 1.8.0-alpha03

April 12, 2023

`androidx.activity:activity:1.8.0-alpha03`, `androidx.activity:activity-compose:1.8.0-alpha03`, and `androidx.activity:activity-ktx:1.8.0-alpha03` are released. This was released from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the [Android 14 (Upside Down Cake) Beta 1 SDK](https://developer.android.com/about/versions/14#beta-1).

**New Features**

- Added `ComponentActivity.setUpEdgeToEdge()` to easily set up the edge-to-edge display in a backward-compatible manner.

**API Changes**

- `ComponentActivity.onBackPressed()` has now been deprecated in favor of the APIs for handling back. Developers should now utilize the `OnBackPressedDispatcher`, rather than overriding this method. ([Ibce2f](https://android-review.googlesource.com/#/q/Ibce2f664a8d73cb1df06c20918752fb3dfb44e0c), [b/271596918](https://issuetracker.google.com/271596918))
- `ComponentDialog` and `ComponentActivity` now contain public API `initViewTreeOwners()` to be used to initialize all view tree owners before setting the content view. ([Ibdce0](https://android-review.googlesource.com/#/q/Ibdce0a994b0daddc090e4ff58583ccba71612870), [b/261314581](https://issuetracker.google.com/261314581))

**Bug Fixes**

- Fixed an issue where Fragments were incorrectly invalidating MenuHosts and causing other menus in the Activity to have unexpected behavior. ([I9404e](https://android-review.googlesource.com/#/q/I9404ee9fcc9ce6b80d70a93bea720fe4ccf583a0), [b/244336571](https://issuetracker.google.com/244336571))

**Other Changes**

- The `ActivityResultRegister` now uses Kotlin `Random` instead of Java. ([I4d98f](https://android-review.googlesource.com/#/q/I4d98f4bc5a36b35fea026f716db45efa74078af8), [b/272096025](https://issuetracker.google.com/272096025))

### Version 1.8.0-alpha02

March 8, 2023

`androidx.activity:activity:1.8.0-alpha02`, `androidx.activity:activity-compose:1.8.0-alpha02`, and `androidx.activity:activity-ktx:1.8.0-alpha02` are released. Developed from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the [Android 14 (Upside Down Cake) Developer Preview 2 SDK](https://developer.android.com/about/versions/14#developer-preview-2).

**Dependency update**

- From [Activity `1.7.0-rc01`](https://developer.android.com/jetpack/androidx/releases/activity#1.7.0-rc01): Activity now depends on [`Lifecycle 2.6.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.0).

### Version 1.8.0-alpha01

February 8, 2023

`androidx.activity:activity:1.8.0-alpha01`, `androidx.activity:activity-compose:1.8.0-alpha01`, and `androidx.activity:activity-ktx:1.8.0-alpha01` are released. This was built from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 (Upside Down Cake) Developer Preview 1 SDK.

**New Features**

- The `OnBackPressedCallback` class now contains new Predictive Back progress callbacks for handling the back gesture starting, progress throughout the gesture, and the back gesture being canceled in addition to the previous `handleOnBackPressed()` callback for when the back gesture is committed.

## Version 1.7

### Version 1.7.2

May 24, 2023

`androidx.activity:activity:1.7.2`, `androidx.activity:activity-compose:1.7.2`, and `androidx.activity:activity-ktx:1.7.2` are released. [Version 1.7.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db92507fc4c50d8975eba066ca034fc4a156b401..4121ca4f250861430dca57d0b727ad4d2d792741/activity)

**Bug Fixes**

- Fix `ReportDrawn` crashing when navigating away from a screen before `report` is called. ([Ic46f1](https://android-review.googlesource.com/#/q/Ic46f17d4dfd9a0758398564dce72fbb5f637626e), [b/260506820](https://issuetracker.google.com/issues/260506820))

### Version 1.7.1

April 19, 2023

`androidx.activity:activity:1.7.1`, `androidx.activity:activity-compose:1.7.1`, and `androidx.activity:activity-ktx:1.7.1` are released. [Version 1.7.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/83d3b196775ea26547854fb88000b4ef5c2649fd..db92507fc4c50d8975eba066ca034fc4a156b401/activity)

**Bug Fixes**

- The `ReportFullyDrawExecuter` no longer leaks when using `ComponentActivity` with `ActivityScenario`. ([Id2ff2](https://android-review.googlesource.com/#/q/Id2ff2311e16d89fc7309a6e99f302cf3e8d9d595), [b/277434271](https://issuetracker.google.com/277434271))

### Version 1.7.0

March 22, 2023

`androidx.activity:activity:1.7.0`, `androidx.activity:activity-compose:1.7.0`, and `androidx.activity:activity-ktx:1.7.0` are released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/78f788418108373b512284fd2b9e6fc91fdf50ca..83d3b196775ea26547854fb88000b4ef5c2649fd/activity)

**Important changes since 1.6.0**

- The Photo Picker activity contracts in `PickVisualMedia` and `PickMultipleVisualMedia` have been updated to contain an additional fallback for when `MediaStore.ACTION_PICK_IMAGES` is unavailable that allows OEMs and system apps, such as Google Play services, to provide a consistent Photo Picker experience on a wider range of Android devices and API levels by implementing the [fallback action](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia#ACTION_SYSTEM_FALLBACK_PICK_IMAGES()). The Photo Picker will use this fallback if it is available before falling back to using `Intent.ACTION_OPEN_DOCUMENT`, which remains to support all API 19 and higher devices.
- `ComponentDialog` now implements `SavedStateRegistryOwner` and has access to its own `SavedStateRegistry` and sets the `SavedStateRegistryOwner` for its `ViewTree`. It is now possible to use Jetpack Compose within a `ComponentDialog` as it meets both the `LifecycleOwner` and `SavedStateRegistryOwner` attached to the Window via the `ViewTree` APIs requirements.
- `IntentSenderRequest.Builder.setFlags()` now allows you to set multiple flags from `Intent`, rather than only a single flag.

**Kotlin Conversion**

A number of Activity classes have been converted to Kotlin. All converted classes still retain their binary compatibility with previous versions. The following classes have **source incompatible** changes for classes written in Kotlin: `ActivityResultRegistryOwner`, `OnBackPressedDispatcherOwner`.

The table below provides the source conversions for the new version of Activity:

| Activity 1.5 | Activity 1.6 |
|---|---|
| `override fun getActivityResultRegistry() = activityResultRegistry` | `override val activityResultRegistry = activityResultRegistry` |
| `override fun getOnBackPressedDispatcher() = onBackPressedDispatcher` | `override val onBackPressedDispatcher = onBackPressedDispatcher` |

These classes were also converted to Kotlin, but remain source compatible: `ContextAware`, `ContextAwareHelper`, `OnContextAvailableListener`, `IntentSenderRequest`, and `OnBackPressedDispatcher`

**FullyDrawnReporter APIs**

`ComponentActivity` now provides a `FullyDrawnReporter` instance that allows multiple components to report when they are ready for interaction. `ComponentActivity` will wait for all components to complete before calling `reportFullyDrawn()` on your behalf. These APIs take care of the timing requirements for you and do not need to be called as part of an `onDraw` call.

These APIs are encouraged to enable:

- Signaling the Android Runtime when startup completes, to ensure all of the code run during a multi-frame startup sequence is included and prioritized for background compilation.
- Signaling Macrobenchmark and Play Vitals when your application should be considered fully drawn for startup metrics, so you can track performance.

Three Activity Compose APIs have been added to make it more convenient to use the `FullyDrawnReporter` from individual composables:

- `ReportDrawn` indicates that your composable is immediately ready for interaction.
- `ReportDrawnWhen` takes a predicate (i.e., `list.count > 0`) to indicate when your composable is ready for interaction.
- `ReportDrawnAfter` takes a suspending method that, when it completes, indicates that you are ready for interaction.

**Dependency Updates**

- Activity now depends on [Lifecycle `2.6.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.1). ([8fc31d](https://android.googlesource.com/platform/frameworks/support/+/8fc31d13a3a01210139e014d127f9aa0aa3479ed))
- Activity now depends on [ProfileInstaller `1.3.0`](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0). ([83d3b1](https://android.googlesource.com/platform/frameworks/support/+/83d3b196775ea26547854fb88000b4ef5c2649fd))

### Version 1.7.0-rc01

March 8, 2023

`androidx.activity:activity:1.7.0-rc01`, `androidx.activity:activity-compose:1.7.0-rc01`, and `androidx.activity:activity-ktx:1.7.0-rc01` are released. [Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..78f788418108373b512284fd2b9e6fc91fdf50ca/activity)

**Dependency update**

- Activity now depends on [`Lifecycle 2.6.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.0).

### Version 1.7.0-beta02

February 22, 2023

`androidx.activity:activity:1.7.0-beta02`, `androidx.activity:activity-compose:1.7.0-beta02`, and `androidx.activity:activity-ktx:1.7.0-beta02` are released. [Version 1.7.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2ea70540638fa56f90e00b5a8b84781a400a49a1..87533b4ff06971ed59028936cd9b6da988cd4522/activity)

**API Changes**

- The action and extra used by the `PickVisualMedia` and `PickMultipleVisualMedia` contracts as a fallback for when `MediaStore.ACTION_PICK_IMAGES` is unavailable are now public constants that provide API stability to OEMs and system apps that want to provide a consistent Photo Picker experience. The implementation of this fallback is still limited to only system apps. ([Icd320](https://android-review.googlesource.com/#/q/Icd320c81c44c718144c55fcd7c5e39056b3bdc7f))

### Version 1.7.0-beta01

February 8, 2023

`androidx.activity:activity:1.7.0-beta01`, `androidx.activity:activity-compose:1.7.0-beta01`, and `androidx.activity:activity-ktx:1.7.0-beta01` are released. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..2ea70540638fa56f90e00b5a8b84781a400a49a1/activity)

**New Features**

- `IntentSenderRequest.Builder.setFlags()` now allows you to set multiple flags from `Intent`, rather than only a single flag. ([Iac04c](https://android-review.googlesource.com/#/q/Iac04cfbd35caadf10db7376505888f1c7cd8b216))

**Bug Fixes**

- The fallback for `PickVisualMedia` for when the framework Photo Picker is unavailable now correctly limits the handling to apps installed in the device's system image. ([If8ae6](https://android-review.googlesource.com/#/q/If8ae6760b36221fa0357cb6ee9f81acd76f7f3a2))

**Kotlin Conversions**

- `ActivityResultRegistryOwner` is now written in Kotlin. This is a **source incompatible change** for those classes written in Kotlin - you must now override the `activityResultRegistry` property rather than implementing the previous `getActivityResultRegistry()` function. ([I0b00e](https://android-review.googlesource.com/#/q/I0b00efc873c16e5b6d26e9ebad889f00a8ddb6b3))
- `OnBackPressedDispatcherOwner` is now written in Kotlin. This is a **source incompatible change** for those classes written in Kotlin - you must now override the `onBackPressedDispatcher` property rather than implementing the previous `getOnBackPressedDispatcher` function. ([Ia277d](https://android-review.googlesource.com/#/q/Ia277dc57731597b869c4e86d3f8c13896a6ce56f))
- `ContextAware`, `ContextAwareHelper`, `OnContextAvailableListener`, `IntentSenderRequest` and `OnBackPressedDispatcher` are now written in Kotlin. ([I1a73e](https://android-review.googlesource.com/#/q/I1a73e84b3742edf18db69c18722f61b8bc49548b), [Iada92](https://android-review.googlesource.com/#/q/Iada9260aa0d006aeea976d08713e171285848d7f), [aosp/2410754](https://android-review.googlesource.com/c/platform/frameworks/support/+/2410754), [I18ac7](https://android-review.googlesource.com/#/q/I18ac79d3cd20fc29159542b729935d3b8d2e4506), [b/257291701](https://issuetracker.google.com/257291701))

### Version 1.7.0-alpha04

January 25, 2023

`androidx.activity:activity:1.7.0-alpha04`, `androidx.activity:activity-compose:1.7.0-alpha04`, and `androidx.activity:activity-ktx:1.7.0-alpha04` are released. [Version 1.7.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/activity)

**New Features**

- The `PickVisualMedia` and `PickMultipleVisualMedia` Activity Result contracts will now use a Google Play services provided Photo Picker where available in cases where the Android system provided Photo Picker (e.g., `MediaStore.ACTION_PICK_IMAGES`) is not available. The `isPhotoPickerAvailable()` API that only detects the Android system provided Photo Picker has been deprecated. It is recommended to use the new `isPhotoPickerAvailable(Context)` API, which will return if either Photo Picker is available. ([I55be6](https://android-review.googlesource.com/#/q/I55be6cf7cf59657acf9b131b3257d25d21b77f7a))

### Version 1.7.0-alpha03

January 11, 2023

`androidx.activity:activity:1.7.0-alpha03`, `androidx.activity:activity-compose:1.7.0-alpha03`, and `androidx.activity:activity-ktx:1.7.0-alpha03` are released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..adf1c279a86ab3886e1666c08e2c3efba783367b/activity)

**New Features**

- `ComponentDialog` now implements `SavedStateRegistryOwner` and has access to its own `SavedStateRegistry` and sets the `SavedStateRegistryOwner` for its ViewTree. It is now possible to use Jetpack Compose within a `ComponentDialog` as it meets both the `LifecycleOwner` and `SavedStateRegistryOwner` attached to the Window via the ViewTree APIs requirements. ([Idca17](https://android-review.googlesource.com/#/q/Idca172600df720d8b724e8bc6971b0d933864253), [I73468](https://android-review.googlesource.com/#/q/I7346856b333933e03f5d3b0d380f5122b4856908) [b/261162296](https://issuetracker.google.com/issues/261162296))

**API Changes**

- Added a `ReportDrawn` composable that immediately marks the activity as ready to call `reportFullyDrawn`. ([Ic5b14](https://android-review.googlesource.com/#/q/Ic5b14e8599e7e7f571023e548ef3ed3fef4fa8d0), [b/259687964](https://issuetracker.google.com/issues/259687964))

**Kotlin Conversions**

- The `ActvitiyResultCallback` and `OnBackPressedCallback` classes have both been converted to Kotlin while maintaining source and binary compatibility. ([Ifc5e5](https://android-review.googlesource.com/#/q/Ifc5e5e1a9a7ed4e281007830fb8d4c74237c63ce), [Ide1b0](https://android-review.googlesource.com/#/q/Ide1b056e438b403c9b1888bc7dfedf283f1ff168), [b/257291701](https://issuetracker.google.com/issues/257291701))

### Version 1.7.0-alpha02

October 24, 2022

`androidx.activity:activity:1.7.0-alpha02`, `androidx.activity:activity-compose:1.7.0-alpha02`, and `androidx.activity:activity-ktx:1.7.0-alpha02` are released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..548c8ac2570ae6cf15798fea1380491f7d93796b/activity)

**Bug Fixes**

- From [Activity `1.6.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.6.1): Fixed an issue with the `PickMultipleVisualMedia` Activity Result contract not launching on Android R devices when using the default value for `maxItems`. ([Ie2776](https://android-review.googlesource.com/#/q/Ie277697928c3af81460f8620ebf6b37bbe0649d1), [b/249182130](https://issuetracker.google.com/issues/249182130))

### Version 1.7.0-alpha01

October 5, 2022

`androidx.activity:activity:1.7.0-alpha01`, `androidx.activity:activity-compose:1.7.0-alpha01`, and `androidx.activity:activity-ktx:1.7.0-alpha01` are released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7d70188d0ef7d7ad972567094fa04e25c88b421..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/activity)

**FullyDrawnReporter APIs**

`ComponentActivity` now provides a `FullyDrawnReporter` instance that allows multiple components to report when they are ready for interaction. `ComponentActivity` will wait for all components to complete before calling `reportFullyDrawn()` on your behalf. These APIs take care of the timing requirements for you and do not need to be called as part of an `onDraw` call.

These APIs are encouraged to enable:

- Signaling the Android Runtime when startup completes, to ensure all of the code run during a multi-frame startup sequence is included and prioritized for background compilation.
- Signaling Macrobenchmark and Play Vitals when your application should be considered fully drawn for startup metrics, so you can track performance.

Two Activity Compose APIs have been added to make it more convenient to use the `FullyDrawnReporter` from individual composables:

- `ReportDrawnWhen` takes a predicate (i.e., `list.count > 0`) to indicate when your composable is ready for interaction.
- `ReportDrawnAfter` takes a suspending method that, when it completes, indicates that you are ready for interaction.

## Version 1.6.1

### Version 1.6.1

October 24, 2022

`androidx.activity:activity:1.6.1`, `androidx.activity:activity-compose:1.6.1`, and `androidx.activity:activity-ktx:1.6.1` are released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7d70188d0ef7d7ad972567094fa04e25c88b421..3f892739d8519e5a9d4f4a47e2da485007715510/activity)

**Bug Fixes**

- Fixed an issue with the `PickMultipleVisualMedia` Activity Result contract not launching on Android R devices when using the default value for `maxItems`. ([Ie2776](https://android-review.googlesource.com/#/q/Ie277697928c3af81460f8620ebf6b37bbe0649d1), [b/249182130](https://issuetracker.google.com/issues/249182130))

## Version 1.6.0

### Version 1.6.0

September 21, 2022

`androidx.activity:activity:1.6.0`, `androidx.activity:activity-compose:1.6.0`, and `androidx.activity:activity-ktx:1.6.0` are released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4e758496ed4c0a1acd5da1fd0fbbde75da899183..a7d70188d0ef7d7ad972567094fa04e25c88b421/activity)

**Important changes since 1.5.0**

- Added `ActivityResultContracts.PickVisualMedia` and `ActivityResultContracts.PickMultipleVisualMedia` for providing a backward compatible contract that uses `MediaStore.ACTION_PICK_IMAGES` when the [Photo Picker](https://developer.android.com/training/data-storage/shared/photopicker) is available and `Intent.ACTION_OPEN_DOCUMENT` when it is not available.
- Integrated the `OnBackInvokedCallback` in Android 13 into the `OnBackPressedDispatchers` provided by `ComponentActivity` and `ComponentDialog`. This ensures that all APIs built on`OnBackPressedDispatcher` work when enabling a [predictive back gesture](https://developer.android.com/guide/navigation/predictive-back-gesture).

### Version 1.6.0-rc02

September 7, 2022

`androidx.activity:activity:1.6.0-rc02`, `androidx.activity:activity-compose:1.6.0-rc02`, and `androidx.activity:activity-ktx:1.6.0-rc02` are released. [Version 1.6.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/55e944757f7798ad52edde754a70cb854e2cdd23..4e758496ed4c0a1acd5da1fd0fbbde75da899183/activity)

**Bug Fixes**

- `OnBackPressedDispatcher` now registers the `OnBackInvokedCallback` with the `PRIORITY_DEFAULT` instead of `PRIORITY_OVERLAY`. ([I3901f](https://android-review.googlesource.com/#/q/I3901fa85f26fa5554da4e0b309447e9592766601))
- Classes that extend `ComponentActivity` will now always have both of their `onMultiWindowModeChanged()` callbacks dispatched. ([Ic4d85](https://android-review.googlesource.com/#/q/Ic4d85882270447666ed7b15019c39c04aa4d4602))
- The `ActivityResultRegistry` will no longer return a result to the `ActivityResultCallback` when the `launch` call throws any `Exception` and the callback was registered without a `LifecycleOwner`. ([Ia7ff7](https://android-review.googlesource.com/#/q/Ia7ff773da287b2d97490bcc553f90020ea9d6067), [b/238350794](https://issuetracker.google.com/issues/238350794))
- `ComponentActivity` will now properly dispatch menu calls without the need to call the super function in your activity. ([Ie33c5](https://android-review.googlesource.com/#/q/Ie33c57e900be51ab49abfdbe5c57407f61553167), [b/238057118](https://issuetracker.google.com/issues/238057118))

**Dependency Update**

- The `Activity` library now depends on [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1). ([If6697](https://android-review.googlesource.com/#/q/If6697c8a96ac9378c29d76a5a26fce8f6ff9d1b1))

### Version 1.6.0-rc01

August 24, 2022

`androidx.activity:activity:1.6.0-rc01`, `androidx.activity:activity-compose:1.6.0-rc01`, and `androidx.activity:activity-ktx:1.6.0-rc01` are released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..55e944757f7798ad52edde754a70cb854e2cdd23/activity)

**Bug Fixes**

- Initializing an `OnBackPressedDispatcher` will no longer cause `ClassVerificationError`s when using SDK versions prior to 33. ([Ic32e1](https://android-review.googlesource.com/#/q/Ic32e1fb18a4f17692d4b62ddf9d37bb5e67c2771))
- Classes that override `ComponentActivity`'s `onPictureInPictureModeChanged()` callback will now always have their callbacks dispatched. ([Ib7fdb](https://android-review.googlesource.com/#/q/Ib7fdbb7cbbfe12347df81b43e8e8f3fe841555fd))

### Version 1.6.0-beta01

August 10, 2022

`androidx.activity:activity:1.6.0-beta01`, `androidx.activity:activity-compose:1.6.0-beta01`, and `androidx.activity:activity-ktx:1.6.0-beta01` are released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8f2c5386181f36db1a3b90633150c993f8dd6192..bea814b246f89ff7244e3c6b0648f0b57e47897c/activity)

**API Changes**

- Marked the deprecated `startActivityForResult` and `startIntentSenderForResult` methods on `ComponentActivity` with `@NonNull` because passing `null` has always resulted in a crash. ([Id2a25](https://android-review.googlesource.com/#/q/Id2a257e4c6f0327c104d87d677543e589f483ab8), [b/231476082](https://issuetracker.google.com/issues/231476082))

**Bug Fixes**

- From [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1): The `ActivityResultRegistry` will no longer return a result to the `ActivityResultCallback` when the `launch` call throws any `Exception` and the callback was registered without a `LifecycleOwner`. ([Ia7ff7](https://android-review.googlesource.com/#/q/Ia7ff773da287b2d97490bcc553f90020ea9d6067), [b/238350794](https://issuetracker.google.com/issues/238350794))
- From [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1): `ComponentActivity` will now properly dispatch menu calls to `onPrepareOptionMenu()`, `onCreateOptionsMenu()` and `onOptionsItemSelected()` overrides without the need to call the super function. ([Ie33c5](https://android-review.googlesource.com/#/q/Ie33c57e900be51ab49abfdbe5c57407f61553167), [b/238057118](https://issuetracker.google.com/issues/238057118))

**Dependency Update**

- From [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1): The `Activity` library now depends on the `Lifecycle` version `2.5.1`. ([If6697](https://android-review.googlesource.com/#/q/If6697c8a96ac9378c29d76a5a26fce8f6ff9d1b1))

### Version 1.6.0-alpha05

June 15, 2022

`androidx.activity:activity:1.6.0-alpha05`, `androidx.activity:activity-compose:1.6.0-alpha05`, and `androidx.activity:activity-ktx:1.6.0-alpha05` are released. Version 1.6.0-alpha05 was developed in a private pre-release branch and has no public commits.

**API Changes**

- `minCompileSdk` is now 33 to align with Tiramisu Beta 3 SDK

**Bug Fixes**

- Fixed crash on older devices when doing SDK extension check for the `PickVisualMedia` `ActivityResultContract` so that it should now work with `ACTION_OPEN_DOCUMENT` on devices running Android 10 and lower.

### Version 1.6.0-alpha04

May 18, 2022

`androidx.activity:activity:1.6.0-alpha04` and `androidx.activity:activity-ktx:1.6.0-alpha04` are released.

**Bug Fixes**

- Fixed an error in `PickVisualMediaRequest` where attempting to create a request, either via the Builder or the top level Kotlin function, would result in a stack overflow.
- Integrated the `OnBackInvokedCallback` in Android 13 Dev Beta 2 into the `OnBackPressedDispatcher` provided by `ComponentDialog`. This ensures that all APIs built on `OnBackPressedDispatcher` work when [enabling a predictive back gesture](https://developer.android.com/about/versions/13/features/predictive-back-gesture).

### Version 1.6.0-alpha03

April 27, 2022

`androidx.activity:activity:1.6.0-alpha03`, `androidx.activity:activity-compose:1.6.0-alpha03`, and `androidx.activity:activity-ktx:1.6.0-alpha03` are released.

- Note: This version will only compile against the Android 13 Developer Beta 1 SDK.

**New Features**

- Added `ActivityResultContracts.PickVisualMedia` and `ActivityResultContracts.PickMultipleVisualMedia` for providing a backward compatible contract that uses `MediaStore.ACTION_PICK_IMAGES` when the [Photo Picker](https://developer.android.com/about/versions/13/features/photopicker) is available and `Intent.ACTION_OPEN_DOCUMENT` when it is not available.
- Integrated the `OnBackInvokedCallback` in Android 13 Dev Beta 1 into the `OnBackPressedDispatcher` provided by `ComponentActivity`. This ensures that all APIs built on `OnBackPressedDispatcher` work when [enabling a predictive back gesture](https://developer.android.com/about/versions/13/features/predictive-back-gesture).

### Version 1.6.0-alpha01

March 23, 2022

`androidx.activity:activity:1.6.0-alpha01`, `androidx.activity:activity-compose:1.6.0-alpha01`, and `androidx.activity:activity-ktx:1.6.0-alpha01` are released.

- Note: This version will only compile against the Android 13 Developer Preview 2 SDK.

**New Features**

- Integrated changes in Android 13 Dev Preview 2 into `ComponentActivity`.

## Version 1.5.1

### Version 1.5.1

July 27, 2022

`androidx.activity:activity:1.5.1`, `androidx.activity:activity-compose:1.5.1`, and `androidx.activity:activity-ktx:1.5.1` are released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e047538e9c1a9b12afec093910a556017720cb13..835baf76d995c6653478c7e00946a0558c678c45/activity)

**Bug Fixes**

- The `ActivityResultRegistry` will no longer return a result to
  the `ActivityResultCallback` when the `launch()` call throws any
  `Exception` and the callback was registered without a `LifecycleOwner`. ([Ia7ff7](https://android-review.googlesource.com/#/q/Ia7ff773da287b2d97490bcc553f90020ea9d6067), [b/238350794](https://issuetracker.google.com/issues/238350794))

- `ComponentActivity` will now properly dispatch menu calls to `onPrepareOptionMenu()`, `onCreateOptionsMenu()` and `onOptionsItemSelected()` overrides
  without the need to call the super function. ([Ie33c5](https://android-review.googlesource.com/#/q/Ie33c57e900be51ab49abfdbe5c57407f61553167), [b/238057118](https://issuetracker.google.com/issues/238057118))

**Dependency update**

- The `Activity` library now depends on the [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1). ([If6697](https://android-review.googlesource.com/#/q/If6697c8a96ac9378c29d76a5a26fce8f6ff9d1b1))

## Version 1.5.0

### Version 1.5.0

June 29, 2022

`androidx.activity:activity:1.5.0`, `androidx.activity:activity-compose:1.5.0`, and `androidx.activity:activity-ktx:1.5.0` are released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/49cd978b488ce31274b756058de8dc8b42ffbf4e..e047538e9c1a9b12afec093910a556017720cb13/activity)

**Important changes since 1.4.0**

- **ComponentDialog** - `ComponentDialog` is a subclass of `Dialog` that includes an `OnBackPressedDispatcher` that will be called when the system back button is pressed and the dialog is visible. Importantly, this subclass also sets the `ViewTreeOnBackPressedDispatcherOwner`, allowing views a generic way to retrieve the correct dispatcher whether it exists in a `ComponentActivity` or a `ComponentDialog`.
- **Callback Interfaces** - `ComponentActivity` now implements a set of modular callback interfaces that can be used instead of the `Activity` callbacks. These interfaces include the following: `OnNewIntentProvider`, `OnConfigurationChangedProvider`, `OnTrimMemoryProvider`, `OnPictureInPictureModeChangedProvider`, `OnMultiWindowModeChangedProvider`
- **CreationExtras Integration** - `ComponentActivity` now has the ability to provide a stateless `ViewModelProvider.Factory` via [Lifecycle `2.5.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0)'s `CreationExtras`.

**Other changes**

- The no parameter constructor for `ActivityResultContracts.CreateDocument` has been deprecated and replaced with a new constructor that takes a concrete mime type (e.g., "image/png") as is required by `Intent.ACTION_CREATE_DOCUMENT`.

### Version 1.5.0-rc01

May 11, 2022

`androidx.activity:activity:1.5.0-rc01`, `androidx.activity:activity-compose:1.5.0-rc01`, and `androidx.activity:activity-ktx:1.5.0-rc01` are released with no changes from 1.5.0-beta01. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..49cd978b488ce31274b756058de8dc8b42ffbf4e/activity)

### Version 1.5.0-beta01

April 20, 2022

`androidx.activity:activity:1.5.0-beta01`, `androidx.activity:activity-compose:1.5.0-beta01`, and `androidx.activity:activity-ktx:1.5.0-beta01` are released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/activity)

**Dependency updates**

- Activity now depends on [Lifecycle `2.4.0-beta01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-beta01).

### Version 1.5.0-alpha05

April 6, 2022

`androidx.activity:activity:1.5.0-alpha05`, `androidx.activity:activity-compose:1.5.0-alpha05`, and `androidx.activity:activity-ktx:1.5.0-alpha05` are released. [Version 1.5.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/activity)

**Bug Fixes**

- `ComponentActivity`'s `onPanelClosed()` now calls the super `onPanelClosed()` as well, fixing an issue where the `onContextMenuClosed` method would not be called. ([Ib6f77](https://android-review.googlesource.com/#/q/Ib6f775e8749a134f8096633d9e1f55b9c10aad5e))

### Version 1.5.0-alpha04

March 23, 2022

`androidx.activity:activity:1.5.0-alpha04`, `androidx.activity:activity-compose:1.5.0-alpha04`, and `androidx.activity:activity-ktx:1.5.0-alpha04` are released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/activity)

**Bug Fixes**

- `SavedStateViewFactory` now supports using `CreationExtras` even when it was initialized with a `SavedStateRegistryOwner`. If extras are provided, the initialized arguments are ignored. ([I6c43b](https://android-review.googlesource.com/#/q/I6c43bfd75888cb4b8bdd610cd07d4962aaba37ea), [b/224844583](https://issuetracker.google.com/issues/224844583))

### Version 1.5.0-alpha03

February 23, 2022

`androidx.activity:activity:1.5.0-alpha03`, `androidx.activity:activity-compose:1.5.0-alpha03`, and `androidx.activity:activity-ktx:1.5.0-alpha03` are released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/activity)

**API Changes**

- You can now pass `CreationExtras` to the activity `by viewModels()` function ([I6a3e6](https://android-review.googlesource.com/#/q/I6a3e64fb4ec1c18510ab5f45b3533de586f50d77), [b/217600303](https://issuetracker.google.com/issues/217600303))

### Version 1.5.0-alpha02

February 9, 2022

`androidx.activity:activity:1.5.0-alpha02`, `androidx.activity:activity-compose:1.5.0-alpha02`, and `androidx.activity:activity-ktx:1.5.0-alpha02` are released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/activity)

**New Features**

- `ComponentActivity` now implements the `OnPictureInPictureModeChangedProvider` interface to allow any component to receive picture-in-picture mode change events. ([I9f567](https://android-review.googlesource.com/#/q/I9f56767522d22873e0539a7f1a51257972619806))
- `ComponentActivity` now implements the `OnMultiWindowModeChangedProvider` interface to allow any component to receive multi-window mode change events. ([I62d91](https://android-review.googlesource.com/#/q/I62d91abd50bc3e1e3d51b924f5dc144c893b4250))

### Version 1.5.0-alpha01

January 26, 2022

`androidx.activity:activity:1.5.0-alpha01`, `androidx.activity:activity-compose:1.5.0-alpha01`, and `androidx.activity:activity-ktx:1.5.0-alpha01` are released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/12bdbc07b7e7e6ea8c70d50af20301310931d415..9dceceb54300ed028a7e8fc7a3454f270337ffde/activity)

**New Features**

- `ComponentActivity` now integrates with ViewModel CreationExtras, introduced as part of [Lifecycle `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-alpha01). ([Ie7e00](https://android-review.googlesource.com/#/q/Ie7e00cf560026d19de728920f8c233a128ec24f3), [b/207012584](https://issuetracker.google.com/issues/207012584))
- Added `ComponentDialog`, a subclass of `Dialog` that includes an `OnBackPressedDispatcher` that will be called when the system back button is pressed when the dialog is visible. Importantly, this subclass also sets the `ViewTreeOnBackPressedDispatcherOwner`, allowing views a generic way to retrieve the correct dispatcher whether it exists in a `ComponentActivity` or a `ComponentDialog`. ([I8a1bc](https://android-review.googlesource.com/#/q/I8a1bcd3c4e2b4544d4b4460e2e7fd7424af34452))
- `ComponentActivity` now implements the new `OnNewIntentProvider` interface to allow any component to receive these events. ([If1f8b](https://android-review.googlesource.com/#/q/If1f8baabb64aa4aa776303bab33322969776b10d))
- `ComponentActivity` now implements the new `OnConfigurationChangedProvider` interface to allow any component to receive these events. ([If623b](https://android-review.googlesource.com/#/q/If623b1764a9fda903ae308bae13de86d09d3cfd6))
- `ComponentActivity` now implements the new `OnTrimMemoryProvider` interface to allow any component to receive these events. ([Ia9295](https://android-review.googlesource.com/#/q/Ia9295c9a47293e6a768fb590fe00b6fe7a3092a5))

**API Changes**

- The no parameter constructor for `ActivityResultContracts.CreateDocument` has been deprecated and replaced with a new constructor that takes a concrete mime type (e.g., `"image/png"`) as is required by `Intent.ACTION_CREATE_DOCUMENT`. ([I2bec6](https://android-review.googlesource.com/#/q/I2bec6d0db33a7cacd468df5c4af3eedf1102f3f4))
- The `OnBackPressedDispatcherOwner` associated with a View can now be retrieved via the `ViewTreeOnBackPressedDispatcherOwner`, rather than relying on casting the `Context`. ([I74685](https://android-review.googlesource.com/#/q/I74685aabe026659f649eea1b803f499a4def979e))

**Bug Fixes**

- Fixed a crash when accessing a `ViewModel` for the very first time from a `registerForActivityResult()` callback or the callbacks to a `LifecycleObserver` added as part of `init` of a `ComponentActivity`. ([Ife83f](https://android-review.googlesource.com/#/q/Ife83f26bedddb2b843a2ce977d0e9526f070ac07))

## Version 1.4.0

### Version 1.4.0

October 27, 2021

`androidx.activity:activity:1.4.0`, `androidx.activity:activity-compose:1.4.0`, and `androidx.activity:activity-ktx:1.4.0` are released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e436c934fda58d94a88adef42dd8321f508b9812..12bdbc07b7e7e6ea8c70d50af20301310931d415/activity)

**Important changes since 1.3.0**

- AndroidX `ComponentActivity` now implements the `MenuHost` interface. This allows any component to add menu items to the `ActionBar` by adding a `MenuProvider` instance to the activity. Each `MenuProvider` can optionally be added with a `Lifecycle` that will automatically control the visibility of those menu items based on the `Lifecycle` state and handle the removal of the `MenuProvider` when the `Lifecycle` is destroyed.
- The `ActivityResultContract` class has been rewritten in Kotlin to ensure that developers writing custom contracts in Kotlin can define the correct nullability for their input and output classes.
- The `ActivityResultContracts` class and its contracts have been rewritten in Kotlin to ensure the proper nullability.

### Version 1.4.0-rc01

October 13, 2021

`androidx.activity:activity:1.4.0-rc01`, `androidx.activity:activity-compose:1.4.0-rc01`, and `androidx.activity:activity-ktx:1.4.0-rc01` are released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..e436c934fda58d94a88adef42dd8321f508b9812/activity)

**Bug Fixes**

- The `ActivityResultRegistry` will no longer return a result to the `ActivityResultCallback` when the `launch` call throws any `Exception`. ([If4f91](https://android-review.googlesource.com/#/q/If4f9159bce2edf7f3f0c76e7ff37ce21b05c13ee), [b/200845664](https://issuetracker.google.com/issues/200845664))

### Version 1.4.0-beta01

September 29, 2021

`androidx.activity:activity:1.4.0-beta01`, `androidx.activity:activity-compose:1.4.0-beta01`, and `androidx.activity:activity-ktx:1.4.0-beta01` are released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/activity)

**API Changes**

- Fixed the type for the `ActivityResultContracts.OpenMultipleDocuments` and `ActivityResultContracts.GetMultipleContents` that caused then to use an output type of `List<? extends Uri>` when using the code from the Java programming language. ([If71de](https://android-review.googlesource.com/#/q/If71de885c6f38bfba07760cd88e368e00ec3ad2d))
- Public constants within the `ActivityResultContracts.StartActivityForResult`, `ActivityResultContracts.StartIntentSenderForResult`, and `ActivityResultContracts.RequestMultiplePermissions` classes are now accessible when using Kotlin via their now public `Companion` objects. ([aosp/1832555](https://android-review.googlesource.com/c/platform/frameworks/support/+/1832555/))

**Documentation Updates**

- The deprecation message for APIs now handled by the [Activity Result APIs](https://developer.android.com/training/basics/intents/result), namely `startActivityForResult`, `startIntentSenderForResult`, `onActivityResult`, `requestPermissions`, and `onRequestPermissionsResult`, have all been expanded with more details. ([cce80f](https://android-review.googlesource.com/#/q/cce80f6e9e1ae0f5b3390b59c5cf1321443ab81f))

### Version 1.4.0-alpha02

September 15, 2021

`androidx.activity:activity:1.4.0-alpha02`, `androidx.activity:activity-compose:1.4.0-alpha02`, and `androidx.activity:activity-ktx:1.4.0-alpha02` are released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/activity)

**New Features**

- The `activity-compose` artifact now contains a `LaunchDuringComposition` lint error that prevents you from calling the `launch` method of `ActivityResultLauncher` as part of composition as composition should be side-effect free. Use the [APIs for handling side-effects](https://developer.android.com/jetpack/compose/side-effects). ([7c2bbe](https://android-review.googlesource.com/#/q/7c2bbe38807c834b21a3766cfcca141765bd19a9), [b/191347220](https://issuetracker.google.com/issues/191347220))

**API Changes**

- The `ActivityResultContract` class has been rewritten in Kotlin to ensure that developers writing custom contracts in Kotlin can define the correct nullability for their input and output classes. ([I8a8f5](https://android-review.googlesource.com/#/q/I8a8f5f38d3a8d0cb457d876300efc748c299e772))
- The `ActivityResultContracts` class and its contracts have been rewritten in Kotlin to ensure the proper nullability. ([I69802](https://android-review.googlesource.com/#/q/I698025e2f1051ca5b21d3fef7522ed449896ab95))

### Version 1.4.0-alpha01

September 1, 2021

`androidx.activity:activity:1.4.0-alpha01`, `androidx.activity:activity-compose:1.4.0-alpha01`, and `androidx.activity:activity-ktx:1.4.0-alpha01` are released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..47e81d1c497b8a57534a460c277855db1b0257ae/activity)

**New Features**

- AndroidX `ComponentActivity` now implements the `MenuHost` interface.. This allows any component to add menu items to the `ActionBar` by adding a `MenuProvider` instance to the activity. Each `MenuProvider` can optionally be added with a `Lifecycle` that will automatically control the visibility of those menu items based on the `Lifecycle` state and handle the removal of the `MenuProvider` when the `Lifecycle` is destroyed. ([I3b608](https://android-review.googlesource.com/#/q/I3b6081516403543ea61a8dc0dbcfd226f81fae6d)):

    /**
      * Using the addMenuProvider() API directly in your Activity
      **/
    class ExampleActivity : ComponentActivity(R.layout.activity_example) {

      override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Add menu items without overriding methods in the Activity
       addMenuProvider(object : MenuProvider {
          override fun onCreateMenu(menu: Menu, menuInflater: MenuInflater) {
            // Add menu items here
            menuInflater.inflate(R.menu.example_menu, menu)
          }

          override fun onMenuItemSelected(menuItem: MenuItem): Boolean {
            // Handle the menu selection
            return true
          }
        })
      }
    }

    /**
      * Using the addMenuProvider() API in a Fragment
      **/
    class ExampleFragment : Fragment(R.layout.fragment_example) {

      override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // The usage of an interface lets you inject your own implementation
        val menuHost: MenuHost = requireActivity()
      
        // Add menu items without using the Fragment Menu APIs
        // Note how we can tie the MenuProvider to the viewLifecycleOwner
        // and an optional Lifecycle.State (here, RESUMED) to indicate when
        // the menu should be visible
        menuHost.addMenuProvider(object : MenuProvider {
          override fun onCreateMenu(menu: Menu, menuInflater: MenuInflater) {
            // Add menu items here
            menuInflater.inflate(R.menu.example_menu, menu)
          }

          override fun onMenuItemSelected(menuItem: MenuItem): Boolean {
            // Handle the menu selection
            return true
          }
        }, viewLifecycleOwner, Lifecycle.State.RESUMED)
      }

**Behavior Changes**

- The `ActivityResultRegistry` will now throw an `IllegalStateException` when attempting to call `launch()` on an `ActivityResultLauncher` that has not be registered or that has been unregistered. ([Ida75d](https://android-review.googlesource.com/#/q/Ida75dca1c2947d74376c453f6e3b65c1adf1684d), [b/192567522](https://issuetracker.google.com/issues/192567522))

**External Contribution**

- Thanks [dmitrilc](https://github.com/dmitrilc) for fixing a typo in the `ActivityResult` documentation. ([#221](https://github.com/androidx/androidx/pull/221))

## Version 1.3.1

### Version 1.3.1

August 4, 2021

`androidx.activity:activity:1.3.1`, `androidx.activity:activity-compose:1.3.1`, and `androidx.activity:activity-ktx:1.3.1` are released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/activity)

**Dependency updates**

- Activity now depends on Kotlin `1.5.21`.
- Activity Compose now depends on Compose `1.0.1`.

## Version 1.3.0

### Version 1.3.0

July 28, 2021

`androidx.activity:activity:1.3.0`, `androidx.activity:activity-compose:1.3.0`, and `androidx.activity:activity-ktx:1.3.0` are released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/activity)

**Important changes since 1.2.0**

- **Activity Compose artifact** - The `activity-compose` artifact provides the `setContent` extension method for hosting your Jetpack Compose UI in an activity and Compose specific wrappers for interacting with the `ComponentActivity` APIs for handling the system back button and the Activity Result APIs. See [the documentation](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary) for more details.
- **CaptureVideo contract** - The `CaptureVideo` `ActivityResultContract` replaces the now deprecated `TakeVideo` contract and returns a boolean denoting success that works across many camera apps.
- **Picture-In-Picture Hint View Tracking** - Users of `activity-ktx` can now use the `trackPipAnimationHintView` extension method on `Activity` to automatically rebuild the `PictureInPictureParams` with the new position of the view as it changes position relative to the window.

### Version 1.3.0-rc02

July 14, 2021

`androidx.activity:activity:1.3.0-rc02`, `androidx.activity:activity-compose:1.3.0-rc02`, and `androidx.activity:activity-ktx:1.3.0-rc02` are released. [Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/activity)

**Bug Fixes**

- The `ActivityResultRegistry` callbacks are now properly saved and restored so callbacks are not duplicated in the savedState. ([I97816](https://android-review.googlesource.com/#/q/I9781617370ad24f768249df42d2ab148915097cb), [b/191893160](https://issuetracker.google.com/issues/191893160))

### Version 1.3.0-rc01

July 1, 2021

`androidx.activity:activity:1.3.0-rc01`, `androidx.activity:activity-compose:1.3.0-rc01`, and `androidx.activity:activity-ktx:1.3.0-rc01` are released with no changes from `1.3.0-beta02`. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/activity)

### Version 1.3.0-beta02

June 16, 2021

`androidx.activity:activity:1.3.0-beta02`, `androidx.activity:activity-compose:1.3.0-beta02`, and `androidx.activity:activity-ktx:1.3.0-beta02` are released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/activity)

Updated `activity-compose` to depend on Compose `1.0.0-beta09`. `androidx.compose.ui:ui-test-junit4` now has a compile time dependency on `activity-compose`.

### Version 1.3.0-beta01

June 2, 2021

`androidx.activity:activity:1.3.0-beta01`, `androidx.activity:activity-compose:1.3.0-beta01`, and `androidx.activity:activity-ktx:1.3.0-beta01` are released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/activity)

**API Changes**

- The previously deprecated `@Composable
  registerForActivityResult()` method has been removed. Please use `rememberLauncherForActivityResult()`. ([Ic39d3](https://android-review.googlesource.com/#/q/Ic39d369a500cd4efd834aecbfadc580ac1a983d9))

### Version 1.3.0-alpha08

May 18, 2021

`androidx.activity:activity:1.3.0-alpha08`, `androidx.activity:activity-compose:1.3.0-alpha08`, and `androidx.activity:activity-ktx:1.3.0-alpha08` are released. [Version 1.3.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/activity)

**New Features**

- The new `CaptureVideo` `ActivityResultContract` returns a boolean to your `ActivityResultCallback` indicating if your video was successfully saved to the given URI. This replaces the now deprecated `TakeVideo` contract as camera apps very rarely supported returning a thumbnail bitmap, making the result unhelpful. ([Ie21f2](https://android-review.googlesource.com/#/q/Ie21f23fd680c361242c7ec11aa0684b9a6cdbf1a), [b/185938070](https://issuetracker.google.com/issues/185938070))
- Added new API `Activity#setPipAnimationHintView` to update the PipParams' source rect hint whenever the view moves. ([I9063d](https://android-review.googlesource.com/#/q/I9063de7990e997607b60384ea3f37970b902c39a))

**API Changes**

- The `rememberLauncherForActivityResult` function now returns a launcher that deprecates the `unregister()` function - registration and unregistering the launcher is handled automatically by `rememberLauncherForActivityResult`. ([I2443e](https://android-review.googlesource.com/#/q/I2443e7e3682a015bbef3948400864cff891bf686))

**Compose Compatibility**

- `androidx.activity:activity-compose:1.3.0-alpha08` is only compatible with Compose version `1.0.0-beta07` and above.

### Version 1.3.0-alpha07

April 21, 2021

`androidx.activity:activity:1.3.0-alpha07`, `androidx.activity:activity-compose:1.3.0-alpha07`, and `androidx.activity:activity-ktx:1.3.0-alpha07` are released. [Version 1.3.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/activity)

**Bug Fixes**

- `rememberLauncherForActivityResult` now returns a stable reference to the same `ActivityResultLauncher` instance even if the contract changes due to recompositions. ([Id2d6d](https://android-review.googlesource.com/#/q/Id2d6d602149aee89a7c0b7b1f2c7b8226cb8ed48))
- Using unstable versions of Fragments above `1.3.0` will no longer throw a false positive lint error telling you to use `1.3.0`. ([aosp/1670206](https://android-review.googlesource.com/1670206), [b/184847092](https://issuetracker.google.com/issues/184847092))

### Version 1.3.0-alpha06

April 7, 2021

`androidx.activity:activity:1.3.0-alpha06`, `androidx.activity:activity-compose:1.3.0-alpha06`, and `androidx.activity:activity-ktx:1.3.0-alpha06` are released. [Version 1.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/activity)

**API Changes**

- The `registerForActivityResult()` API has been renamed to `rememberLauncherForActivityResult()` to better indicate that the returned `ActivityResultLauncher` is a managed object that is remembered on your behalf. Attempting to call `unregister` the returned `ActivityResultLauncher` will now throw an error. ([I2bb6d](https://android-review.googlesource.com/#/q/I2bb6db90e9e936cba23fd48ea318e80e618ca8d5))
- `LocalOnBackPressedDispatcherOwner.current` and `LocalActivityResultRegistryOwner.current` now return a nullable value to better determine whether it is available in the current composition. APIs that requires those APIs, such as `BackHandler` and `rememberLauncherForActivityResult()`, respectively, will now throw a more descriptive error if the underlying owner is not found. `NavHost` now works even when an `OnBackPressedDispatcherOwner` is not found, such is the case when previewing the `NavHost`. ([I7d8b4](https://android-review.googlesource.com/#/q/I7d8b4662b2d30515a4536e212bf6631357a5357f))

**Bug Fixes**

- The `BackHandler` will now properly intercept back presses in the event that the Activity is `STOPPED`, then `STARTED` again, and other callbacks were added with a LifecycleOwner. ([I71de6](https://android-review.googlesource.com/#/q/I71de6184ba73f56b34de9dcddaf138d98c46417f), [b/182284739](https://issuetracker.google.com/issues/182284739))
- Using the `launch()` method extension with a custom `ActivityResultContract` that has a `Unit` input will no longer cause a `NullPointerException` ([I76282](https://android-review.googlesource.com/#/q/I76282e17d47d25e3ff859f0b646e6063a381a510), [b/183837954](https://issuetracker.google.com/issues/183837954))

### Version 1.3.0-alpha05

March 24, 2021

`androidx.activity:activity:1.3.0-alpha05`, `androidx.activity:activity-compose:1.3.0-alpha05`, and `androidx.activity:activity-ktx:1.3.0-alpha05` are released. [Version 1.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/activity)

**Bug Fixes**

- From [Activity 1.2.2](https://developer.android.com/jetpack/androidx/releases/activity#1.2.2): Fixed an issue in the `InvalidFragmentVersionForActivityResult` lint check that led to a false positive when using Fragment 1.3.1 or higher. ([I54da1](https://android-review.googlesource.com/#/q/I54da158c0ca4bfa6246f51226fd4991dc485b0d2), [b/182388985](https://issuetracker.google.com/issues/182388985))
- From [Activity 1.2.2](https://developer.android.com/jetpack/androidx/releases/activity#1.2.2): `ComponentActivity` now avoids a `ClassNotFoundException` when launching an `Intent` from an `ActivityResultContract` that was previously held as an extra in another `Intent`. ([Ieff05](https://android-review.googlesource.com/#/q/Ieff0578bfd0875f22d42b19040ee24999bb23c89), [b/182906230](https://issuetracker.google.com/issues/182906230))

**Dependency Updates**

- From [Activity 1.2.2](https://developer.android.com/jetpack/androidx/releases/activity#1.2.2): Activity now depends on [Lifecycle `2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1).

### Version 1.3.0-alpha04

March 10, 2021

`androidx.activity:activity:1.3.0-alpha04`, `androidx.activity:activity-compose:1.3.0-alpha04`, and `androidx.activity:activity-ktx:1.3.0-alpha04` are released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b6cff92e45f1d4467086aa2c6aa0248b4883950..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/activity)

**Bug Fixes**

- From [Activity `1.2.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.1): `RequestMultiplePermissions` now always returns results for all requested permissions instead of only permissions that weren't previously granted. ([I50bc3](https://android-review.googlesource.com/#/q/I50bc3db9c59c7a3e3ca8afc7c3fe1b1318c26067), [b/180884668](https://issuetracker.google.com/issues/180884668))
- From [Activity `1.2.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.1): `ActivityResultRegistry` now ensures that in progress `launch()` requests will return their results even if you `unregister()`, then `register()` again with the same key. ([I9ef34](https://android-review.googlesource.com/#/q/I9ef34256a1e0f93fd1fd8983e867b9dd5e8e2441), [b/181267562](https://issuetracker.google.com/issues/181267562))
- Activity Compose no longer adds test dependencies to the runtime classpath. ([Ifd8b3](https://android-review.googlesource.com/#/q/Ifd8b37d57361e94de7e848f0f6ed91a9f0ee37c0))
- Fixed an issue with `BackHandler` where the previously set `onBack` lambda was still being used after recomposition. ([8eb5eb](https://android-review.googlesource.com/#/q/8eb5ebe7c4e0ab803af4c02b1922043c0037a9b4))

### Version 1.3.0-alpha03

February 24, 2021

`androidx.activity:activity:1.3.0-alpha03`, `androidx.activity:activity-compose:1.3.0-alpha03`, and `androidx.activity:activity-ktx:1.3.0-alpha03` are released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e8a50ec64c8057f75a68e371f5287d3f6da4ba6..4b6cff92e45f1d4467086aa2c6aa0248b4883950/activity)

**New Features**

- There is a now a Composable `registerForActivityResult` function for getting results from activities within composables. ([Ia7851](https://android-review.googlesource.com/#/q/Ia78515f6693ebf6f1997ee0109df87dcc388dda7), [b/172690553](https://issuetracker.google.com/issues/172690553))

**API Changes**

- `LocalOnBackPressedDispatcherOwner` now has a `provides` functions that can be used with `CompositionLocalProvider`, replacing the `asProvidableCompositionLocal()` API. ([I45d24](https://android-review.googlesource.com/#/q/I45d244bea668db72a536c1f9bbdb7b24073aba0c))

> [!NOTE]
> **Note:** Activity Compose 1.3.0-alpha03 is only compatible with Compose 1.0.0-beta01.

### Version 1.3.0-alpha02

February 10, 2021

`androidx.activity:activity:1.3.0-alpha02`, `androidx.activity:activity-compose:1.3.0-alpha02`, and `androidx.activity:activity-ktx:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c96bbfa4cd323a18c5db328a5234ec27377906c..1e8a50ec64c8057f75a68e371f5287d3f6da4ba6/activity)

**Bug Fixes**

- Fixed an issue in Activity Compose `1.3.0-alpha01` that causes a `NoSuchMethodError: No static method setContent` exception when using Compose `1.0.0-alpha12`. All Compose users should depend on `1.3.0-alpha02` and above. ([b/179911234](https://issuetracker.google.com/issues/179911234))

**API Changes**

- The `BackHandler` API can be used to allow a Composable to intercept the system back button. ([I58ed5](https://android-review.googlesource.com/#/q/I58ed5891125e093f3425a514c82266e25a684384), [b/172154006](https://issuetracker.google.com/issues/172154006))

> [!NOTE]
> **Note:** Activity Compose 1.3.0-alpha02 is only compatible with Compose 1.0.0-alpha12.

### Version 1.3.0-alpha01

February 10, 2021

`androidx.activity:activity:1.3.0-alpha01`, `androidx.activity:activity-compose:1.3.0-alpha01`, and `androidx.activity:activity-ktx:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0c05672ea464c9788ec7c07e723361f2a23b3439..3c96bbfa4cd323a18c5db328a5234ec27377906c/activity)

> [!CAUTION]
> **Caution:** Please use version `1.3.0-alpha02` instead. A critical issue was found in `1.3.0-alpha01` that causes Activity Compose and libraries that depend on it to crash with a `NoSuchMethodError: No static method setContent` exception. ([b/179911234](https://issuetracker.google.com/issues/179911234))

**New Features**

- The new `activity-compose` artifact provides Jetpack Compose specific helpers for `androidx.activity` specific APIs.
  - `ComponentActivity.setContent` has moved from `androidx.compose.ui.platform.setContent` to `androidx.activity.compose.setContent`. ([Icf416](https://android-review.googlesource.com/#/q/Icf4168e6078b87ce746569a946b2a90274197c72))

> [!NOTE]
> **Note:** Activity Compose 1.0.0-alpha01 is only compatible with Compose 1.0.0-alpha12.

**Known Issues**

- Using Activity Compose `1.3.0-alpha01` and libraries that depend on it, such as `androidx.compose.ui:ui-test-junit4:1.0.0-alpha12`, will result in a `NoSuchMethodError: No static method setContent` exception. ([b/179911234](https://issuetracker.google.com/issues/179911234))

## Version 1.2.4

### Version 1.2.4

July 21, 2021

`androidx.activity:activity:1.2.4` and `androidx.activity:activity-ktx:1.2.4` are released. [Version 1.2.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f4a57ed58db086df5059f059a09e014df9f46e4c..332dfe3d3ed401984ae01f42076cf5801ddfd81d/activity)

**Bug Fixes**

- From [Activity `1.3.0-rc02`](https://developer.android.com/jetpack/androidx/releases/activity#1.3.0-rc02): The ActivityResultRegistry callbacks are now properly saved and restored so callbacks are not duplicated in the savedState. ([I97816](https://android-review.googlesource.com/#/q/I9781617370ad24f768249df42d2ab148915097cb), [b/191893160](https://issuetracker.google.com/issues/191893160))

## Version 1.2.3

### Version 1.2.3

May 5, 2021

`androidx.activity:activity:1.2.3` and `androidx.activity:activity-ktx:1.2.3` are released. [Version 1.2.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2e83201d839574608d563976022ea651a4a4192c..f4a57ed58db086df5059f059a09e014df9f46e4c/activity)

**Bug Fixes**

- Using the `launch()` method extension with a custom `ActivityResultContract` that has a `Unit` input will no longer cause a `NullPointerException` ([I76282](https://android-review.googlesource.com/#/q/I76282e17d47d25e3ff859f0b646e6063a381a510), [b/183837954](https://issuetracker.google.com/issues/183837954))
- Fixed a false positive lint error telling you to use Fragment `1.3.0` when using an snapshot, alpha, beta, or RC build of a newer version of Fragments. ([f4a57e](https://android-review.googlesource.com/c/platform/frameworks/support/+/1684167), [b/184847092](https://issuetracker.google.com/issues/184847092))

## Version 1.2.2

### Version 1.2.2

March 24, 2021

`androidx.activity:activity:1.2.2` and `androidx.activity:activity-ktx:1.2.2` are released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/48102953c701f63f9237bdd6133a70d6eac30a78..2e83201d839574608d563976022ea651a4a4192c/activity)

**Bug Fixes**

- Fixed an issue in the `InvalidFragmentVersionForActivityResult` lint check that led to a false positive when using Fragment 1.3.1 or higher. ([I54da1](https://android-review.googlesource.com/#/q/I54da158c0ca4bfa6246f51226fd4991dc485b0d2), [b/182388985](https://issuetracker.google.com/issues/182388985))
- `ComponentActivity` now avoids a `ClassNotFoundException` when launching an `Intent` from an `ActivityResultContract` that was previously held as an extra in another `Intent`. ([Ieff05](https://android-review.googlesource.com/#/q/Ieff0578bfd0875f22d42b19040ee24999bb23c89), [b/182906230](https://issuetracker.google.com/issues/182906230))

**Dependency Updates**

- Activity now depends on [Lifecycle `2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1).

## Version 1.2.1

### Version 1.2.1

March 10, 2021

`androidx.activity:activity:1.2.1` and `androidx.activity:activity-ktx:1.2.1` are released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b9107d21669925e066ad87d9caa04b7dedf59d4..48102953c701f63f9237bdd6133a70d6eac30a78/activity)

**Bug Fixes**

- `RequestMultiplePermissions` now always returns results for all requested permissions instead of only permissions that weren't previously granted. ([I50bc3](https://android-review.googlesource.com/#/q/I50bc3db9c59c7a3e3ca8afc7c3fe1b1318c26067), [b/180884668](https://issuetracker.google.com/issues/180884668))
- `ActivityResultRegistry` now ensures that in progress `launch()` requests will return their results even if you `unregister()`, then `register()` again with the same key. ([I9ef34](https://android-review.googlesource.com/#/q/I9ef34256a1e0f93fd1fd8983e867b9dd5e8e2441), [b/181267562](https://issuetracker.google.com/issues/181267562))

## Version 1.2.0

> [!NOTE]
> **Note:** The Kotlin dependant libraries of this version (`activity-ktx`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.0

February 10, 2021

`androidx.activity:activity:1.2.0` and `androidx.activity:activity-ktx:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0c05672ea464c9788ec7c07e723361f2a23b3439..2b9107d21669925e066ad87d9caa04b7dedf59d4/activity)

**Major changes since 1.1.0**

- **Activity Result APIs** : `ComponentActivity` now provides an `ActivityResultRegistry` that lets you handle `startActivityForResult()`+`onActivityResult()` as well as `requestPermissions()`+`onRequestPermissionsResult()` flows without overriding methods in your Activity or Fragment, brings increased type safety via `ActivityResultContract`, and provides hooks for testing these flows. See the updated [Getting a Result from an Activity](https://developer.android.com/training/basics/intents/result).

> [!NOTE]
> **Note:** when upgrading to Activity `1.2.0`, you **must** upgrade to [Fragment `1.3.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0) to fix issues with invalid request codes and ensure that permission requests are delivered correctly. The `InvalidFragmentVersionForActivityResult` Lint check will warn you if you do not upgrade to an appropriate Fragment version.

- **`ContextAware`** : `ComponentActivity` now implements `ContextAware`, allowing you to add one or more `OnContextAvailableListener` instances which will receive a callback *before* the base `Activity.onCreate()`.

  - A suspending Kotlin extension `withContextAvailable()` allows you to run a non-suspending block when the Context becomes available and return a result.
  - This API is used by `FragmentActivity` in [Fragment 1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0) to restore the state of the `FragmentManager`. Any listeners added to subclasses of `FragmentActivity` will run after that listener.
  - This API is used by `AppCompatActivity` in [AppCompat 1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/appcompat#1.3.0-alpha02) or higher. Any listeners added to subclasses of `AppCompatActivity` will run after that listener.
- **`ViewTree` Support** : `ComponentActivity` now supports the `ViewTreeLifecycleOwner.get(View)`, `ViewTreeViewModelStoreOwner.get(View)`, and `ViewTreeSavedStateRegistryOwner` APIs added in [Lifecycle `2.3.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0) and [SavedState `1.1.0`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.1.0) such that it will return the Activity as the `LifecycleOwner`, `ViewModelStoreOwner`, and `SavedStateRegistryOwner` for any Views directly added to the `ComponentActivity`.

> [!NOTE]
> **Note:** When using `AppCompatActivity`, you must use [AppCompat `1.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.3.0-alpha01) or higher to gain `ViewTree` support.

- **reportFullyDrawn() backport** - The `Activity` method of `reportFullyDrawn()` has been backported in `ComponentActivity` to work on all API levels, fixing a crash on API 19 and adding tracing for this method for all API levels.

### Version 1.2.0-rc01

December 16, 2020

`androidx.activity:activity:1.2.0-rc01` and `androidx.activity:activity-ktx:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..0c05672ea464c9788ec7c07e723361f2a23b3439/activity)

**Bug Fixes**

- The `ActivityResultRegistry` now always restores the exact state that was saved. ([Idd56b](https://android-review.googlesource.com/#/q/Idd56b95f825aa457d623a9569ce229d42c7f746b))
- Add tracing to `ComponentActivity.reportFullyDrawn` ([Ic7632](https://android-review.googlesource.com/#/q/Ic7632bef49a1440843cba550b1da27736d5abe41))

**External Contribution**

- `ComponentActivity` now overrides `reportFullyDrawn()`, allowing it to be called on all API levels and fixing a crash when calling this method without the appropriate system permission on API 19 devices. Thanks Simon Schiller! ([b/163239764](https://issuetracker.google.com/163239764), [#103](https://github.com/androidx/androidx/pull/103))

### Version 1.2.0-beta02

December 2, 2020

`androidx.activity:activity:1.2.0-beta02` and `androidx.activity:activity-ktx:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/activity)

**Bug Fixes**

- Fixed an issue where the Activity Result API would not wait for the Lifecycle to be `STARTED` before delivering results when registered with a `Lifecycle`. ([I109ea](https://android-review.googlesource.com/#/q/I109ea1fc5712d5cfc1f223cd085993b5397d3a8f))

**External Contribution**

- Updated the documentation for `launch()` to explicitly call out that it can throw an `ActivityNotFoundException`. Thanks Michał Zieliński! ([aosp/1493580](https://android-review.googlesource.com/1493580))

### Version 1.2.0-beta01

October 1, 2020

`androidx.activity:activity:1.2.0-beta01` and `androidx.activity:activity-ktx:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/activity)

**Bug Fixes**

- The `ActivityResultRegistry` now randomly generates integers until it finds one that is unallocated to use as a request code `register()`, thus preventing the possible integer overflow caused by incrementing request codes. ([b/168779518](https://issuetracker.google.com/issues/168374000))

- `Lifecycle` observers are properly removed when calling `unregister()` on an `ActivityResultLauncher`. ([b/165608393](https://issuetracker.google.com/165608393))

**Behavior Changes**

- The `ActivityResultRegistry` now throws an `IllegalStateException` when attempting to call `register()` with a `LifecycleOwner` whose `Lifecycle` has already reached `STARTED`. ([b/165435866](https://issuetracker.google.com/165435866))

**Documentation Updated**

- `ContextAware` documentation links to `LifecycleOwner` to highlight `Lifecycle` callbacks as the appropriate place for creation and destruction events. ([aosp/1414152](https://android-review.googlesource.com/c/platform/frameworks/support/+/1414152))

### Version 1.2.0-alpha08

August 19, 2020

`androidx.activity:activity:1.2.0-alpha08` and `androidx.activity:activity-ktx:1.2.0-alpha08` are released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/activity)

**New Features**

- `ComponentActivity` now implements `ContextAware`, allowing you to add one or more `OnContextAvailableListener` instances which will receive a callback before the base `Activity.onCreate()`. ([b/161390636](https://issuetracker.google.com/161390636))
  - A suspending Kotlin extension `withContextAvailable()` allows you to run a non-suspending block when the Context becomes available and return a result. ([I8290c](https://android-review.googlesource.com/#/q/I8290cd9de8231913036d23a233c177ed45d2d370))
  - This API is used by `FragmentActivity` in [Fragment 1.3.0-alpha08](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha08) to restore the state of the `FragmentManager`. Any listeners added to subclasses of `FragmentActivity` will run after that listener. ([I513da](https://android-review.googlesource.com/#/q/I513da73bc0862b62af4166be35ba353fc7869a09))
  - This API is used by `AppCompatActivity` in [AppCompat 1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/appcompat#1.3.0-alpha02). Any listeners added to subclasses of `AppCompatActivity` will run after that listener. ([I513da](https://android-review.googlesource.com/#/q/I513da73bc0862b62af4166be35ba353fc7869a09))

**Bug Fixes**

- Fixed an issue with the `ActivityResultFragmentVersionDetector` Lint check that caused it to break when using Lint 27.1.0 or higher. ([b/162155191](https://issuetracker.google.com/162155191))

### Version 1.2.0-alpha07

July 22, 2020

`androidx.activity:activity:1.2.0-alpha07` and `androidx.activity:activity-ktx:1.2.0-alpha07` are released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..9f60cc700129e30cee9df020005c317fb39d32ec/activity)

**New Features**

- Added a new `InvalidFragmentVersionForActivityResult` lint check that verifies that you are using [Fragment `1.3.0-alpha07`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha07) when using the [Activity Result API](https://developer.android.com/training/basics/intents/result), avoiding runtime crashes due to "invalid request code" issues and non-functioning permission requests caused by using older versions of Fragments. ([b/152554847](https://issuetracker.google.com/152554847))

**External Contribution**

- Fixed an `ArrayIndexOutOfBoundsException` when parsing the results for the `RequestPermission` Activity Result contract. ([I8f9e3](https://android-review.googlesource.com/#/q/I8f9e3e3a5e9bdf35b391fea19dc1c3d985650d6a), [b/161057605](https://issuetracker.google.com/161057605))

### Version 1.2.0-alpha06

June 10, 2020

`androidx.activity:activity:1.2.0-alpha06` and `androidx.activity:activity-ktx:1.2.0-alpha06` are released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/activity)

**New Features**

- You can now destructure the `ActivityResult` class in kotlin to directly access the `requestCode` and `intent`. ([b/157212935](https://issuetracker.google.com/issues/157212935))
- `ActivityResultLauncher` now allows you to get the `ActivityResultContract` that was used to register the launcher. ([b/156875743](https://issuetracker.google.com/issues/156875743))

**API Changes**

- *Breaking change* : The `invoke()` method on `ActivityResultRegistry` has been renamed to `onLaunch()`. ([b/157496491](https://issuetracker.google.com/issues/157496491))
- The `OpenMultipleDocuments` contract now returns an empty list instead of `null` to the registered callback if no result is returned. ([b/157348014](https://issuetracker.google.com/issues/157348014))

### Version 1.2.0-alpha05

May 20, 2020

`androidx.activity:activity:1.2.0-alpha05` and `androidx.activity:activity-ktx:1.2.0-alpha05` are released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/942518f415d35ff9f2ff78f312c076c673468877..ccc6e95c574b66563952c33fbe26888b93a0e0cb/activity)

**New Features**

- Added support for `ViewTreeViewModelStoreOwner` from [Lifecycle `2.3.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha03), and `ViewTreeSavedStateRegistryOwner` from [SavedState `1.1.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.1.0-alpha01) when using a `View` within a `ComponentActivity`. ([aosp/1297993](https://android-review.googlesource.com/1300264), [aosp/1300264](https://android-review.googlesource.com/1298680))

**API Changes**

- The `TakePicture` contract now returns a `boolean` indicating success rather than a thumbnail `Bitmap` as this was very rarely supported by camera apps when writing the image to the provided `Uri`. ([b/154302879](https://issuetracker.google.com/issues/154302879))
- The `invoke()` extensions on `ActivityResultLauncher` have been removed in favor of explicitly using `launch()` to better indicate that these are asynchronous operations. Kotlin extensions for `launch` have been added to the `androidx.activity.result` package for `ActivityResultLauncher<Void>` and `ActivityResultLauncher<Unit>` that remove the need to pass in `null` or `Unit`, respectively, mirroring that behavior from the previously `invoke()` extensions. ([aosp/1304674](https://android-review.googlesource.com/1304674), [aosp/1304675](https://android-review.googlesource.com/1304675))
- The `IntentSenderRequest.Builder` methods for `setFlagsMask()` and `setFlagsValues()` has been combined into a single `setFlags()` method. ([aosp/1302111](https://android-review.googlesource.com/1302111/))

**Bug Fixes**

- When registering an `ActivityResultCallback` with a `LifecycleOwner`, fixed an issue where the callback would be triggered before the state reaches `STARTED`. ([aosp/1309744](https://android-review.googlesource.com/1309744/))

**Behavior Changes**

- The `ActivityResultRegistry` now generates request codes starting at `0xFFFF` rather than at `0`, preventing overlap when using `startActivityForResult()` or `requestPermissions()` in an activity. ([aosp/1302324](https://android-review.googlesource.com/1302324/))

### Version 1.2.0-alpha04

April 29, 2020

`androidx.activity:activity:1.2.0-alpha04` and `androidx.activity:activity-ktx:1.2.0-alpha04` are released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..942518f415d35ff9f2ff78f312c076c673468877/activity)

**New Features**

- Added a contract that can call startIntentSenderForResult to the ActivityResult APIs. ([b/153007517](https://issuetracker.google.com/issues/153007517))

**API Changes**

- The `prepareCall()` method has been renamed to `registerForActivityResult()`, both on `ComponentActivity` here and in [Fragment `1.3.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha04). ([aosp/1278717](https://android-review.googlesource.com/1278717))
- The `GetContents`, `OpenDocuments`, and `RequestPermissions` contracts have been renamed to `GetMultipleContents`, `OpenMultipleDocuments`, and `RequestMultiplePermissions`, respectively. ([aosp/1280161](https://android-review.googlesource.com/1280161))
- `ComponentActivity` now implements the `ActivityResultRegisteryOwner` interface. ([aosp/1290888](https://android-review.googlesource.com/1290888))
- - The `startActivityForResult()`/`onActivityResult()` and `onRequestPermissionsResult()` APIs on `ComponentActivity` have been deprecated. Please use the [Activity Result APIs](https://developer.android.com/training/basics/intents/result). ([b/154751887](https://issuetracker.google.com/issues/154751887))

**Bug Fixes**

- When using the `GetMultipleContents` and `OpenMultipleDocuments` contracts and selecting a single item, it is now correctly returned to your callback. ([b/152941153](https://issuetracker.google.com/issues/152941153))

### Version 1.2.0-alpha03

April 1, 2020

`androidx.activity:activity:1.2.0-alpha03` and `androidx.activity:activity-ktx:1.2.0-alpha03` are released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ba6efec9a86f20ddc75c8c2b132e009cfb6b1..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/activity)

**New Features**

- Added the `TakeVideo`, `PickContact`, `GetContent`, `GetContents`, `OpenDocument`, `OpenDocuments`, `OpenDocumentTree`, and `CreateDocument` contracts to the set of pre-built contracts provided by [`ActivityResultContracts`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts). ([aosp/1262482](https://android-review.googlesource.com/1262482), [aosp/1266916](https://android-review.googlesource.com/1266916), [aosp/1268960](https://android-review.googlesource.com/1268960))
- The Activity Result APIs now support launching an activity for result with an optional `ActivityOptionsCompat`. ([b/151860054](https://issuetracker.google.com/issues/151860054))

**API Changes**

- The `TakePicture` contract now takes a `Uri` input for where the image should be stored. The previous contract that does not take any input has been renamed to `TakePicturePreview`. ([aosp/1262482](https://android-review.googlesource.com/1262482))
- The `registerActivityResultCallback()` method on `ActivityResultRegistry` has been renamed to `register()`. ([aosp/1267621](https://android-review.googlesource.com/1267621))
- The `dispose()` method on `ActivityResultLauncher` has been renamed to `unregister()` and the `unregisterResultCallback()` on `ActivityResultRegistry` has been removed. ([aosp/1267621](https://android-review.googlesource.com/1267621))
- The `createIntent()` method of `ActivityResultContact` now takes a `Context` in addition to the input to make it possible to create explicit Intents. ([aosp/1238800](https://android-review.googlesource.com/1238800))
- An `ActivityResultContract` can now override `getSynchronousResult()` to deliver a result without calling `startActivityForResult`. This is used by the `RequestPermission` and `RequestPermissions` contracts to correctly deliver a 'granted' status if the requested permissions are already granted. ([b/151110799](https://issuetracker.google.com/issues/151110799))
- The previously available `Dial` contract has been removed as that `Intent` is not meant to be used with `startActivityForResult()`. ([aosp/1266916](https://android-review.googlesource.com/1266916))
- Many of the Activity Result APIs not meant to be extended are now `final`. This includes `getActivityResultRegistry()`, the `prepareCall()` methods, all methods of `ActivityResultRegistry` except `invoke()`, and a number of the default contracts that do not support optional extras. ([b/152439361](https://issuetracker.google.com/issues/152439361))

**Bug Fixes**

- Fixed a `NullPointerException` in `ActivityResultRegistry` when attempting to deliver results to a callback that has not yet been re-registered after a configuration change; `ActivityResultRegistry` now holds onto these pending results and delivers them when the callback is re-registered. ([b/152137004](https://issuetracker.google.com/issues/152137004))

> [!NOTE]
> **Note:** when upgrading to Activity `1.2.0-alpha03`, you **must** upgrade to [Fragment `1.3.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha03) if you were previously using Fragment `1.3.0-alpha02` or if you want to use the `RequestPermission` or `RequestPermissions` contracts.

### Version 1.2.0-alpha02

March 18, 2020

`androidx.activity:activity:1.2.0-alpha02` and `androidx.activity:activity-ktx:1.2.0-alpha02` are released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..1e0ba6efec9a86f20ddc75c8c2b132e009cfb6b1/activity)

**New Features**

- **ActivityResultRegistry** : `ComponentActivity` now provides an `ActivityResultRegistry` that lets you handle the `startActivityForResult()`+`onActivityResult()` as well as `requestPermissions()`+`onRequestPermissionsResult()` flows without overriding methods in your Activity or Fragment, brings increased type safety via `ActivityResultContract`, and provides hooks for testing these flows. See the updated [Getting a Result from an Activity](https://developer.android.com/training/basics/intents/result). ([b/125158199](https://developer.android.com/issuetracker.google.com/issues/125158199))

> [!NOTE]
> **Note:** when upgrading to Activity `1.2.0-alpha02`, you **must** upgrade to [Fragment `1.3.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha02) or higher to use the `RequestPermission` or `RequestPermissions` Activity Result contracts.

### Version 1.2.0-alpha01

March 4, 2020

`androidx.activity:activity:1.2.0-alpha01` and `androidx.activity:activity-ktx:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c8a1a3df9acb8af62c1ccd923b5be6b3defebcae..666ae665acfcfa2a20eccc18e4494808169742f4/activity)

**New Features**

- Added support for the `ViewTreeLifecycleOwner.get(View)` API added in [Lifecycle `2.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha01) such that it will return the Activity as the `LifecycleOwner` for any Views directly added to the Activity. ([aosp/1182955](https://android-review.googlesource.com/1182955))

**Bug Fixes**

- Fixed a regression introduced in Activity `1.1.0` when running on older versions of the platform where `onBackPressed()` would cause an `IllegalStateException` due to a bug in the `android.app.FragmentManager`. ([b/146290338](https://issuetracker.google.com/issues/146290338))

## Version 1.1.0

> [!NOTE]
> **Note:** The Kotlin dependant libraries of this version (`activity-ktx`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.1.0

January 22, 2020

`androidx.activity:activity:1.1.0` is released. [Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/19547d654a4c370cb59ce66319f585a674f5ddf3..c8a1a3df9acb8af62c1ccd923b5be6b3defebcae/activity).

**Important changes since 1.0.0**

- **Lifecycle ViewModel SavedState Integration** : `SavedStateViewModelFactory` is now the default factory used when using `by viewModels()`, the `ViewModelProvider` constructor, or `ViewModelProviders.of()` with a `ComponentActivity` or its subclasses.

### Version 1.1.0-rc03

December 4, 2019

`androidx.activity:activity:1.1.0-rc03` and `androidx.activity:activity-ktx:1.1.0-rc03` are released. [Version 1.1.0-rc03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/a010ca9118db203ee40cc5db0a023002d5a247bd..19547d654a4c370cb59ce66319f585a674f5ddf3/activity/activity).

**Dependency changes**

- Activity now depends on Lifecycle `2.2.0-rc03` and Lifecycle ViewModel SavedState `1.0.0-rc03`.

### Version 1.1.0-rc02

November 7, 2019

`androidx.activity:activity:1.1.0-rc02` and `androidx.activity:activity-ktx:1.1.0-rc02` are released. [Version 1.1.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c378b9a2eae63d2701c82b0144af36e33d15c26a..a010ca9118db203ee40cc5db0a023002d5a247bd/activity/activity).

**Dependency changes**

- Activity now depends on lifecycle `2.2.0-rc02`.

### Version 1.1.0-rc01

October 23, 2019

`androidx.activity:activity:1.1.0-rc01` and `androidx.activity:activity-ktx:1.1.0-rc01` are released with no changes from `1.1.0-beta01`. [Version 1.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f072e1c234477ad31b7dfe6dfc22b08cc7307f5..c378b9a2eae63d2701c82b0144af36e33d15c26a/activity/activity).

### Version 1.1.0-beta01

October 9, 2019

`androidx.activity:activity:1.1.0-beta01` and `androidx.activity:activity-ktx:1.1.0-beta01` are released. [Version 1.1.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/7abd0436770aa87911dffd1b405bbbf819da3335..6f072e1c234477ad31b7dfe6dfc22b08cc7307f5/activity).

**Dependency changes**

- Activity now depends on SavedState 1.0.0 stable.

### Version 1.1.0-alpha03

September 5, 2019

`androidx.activity:activity:1.1.0-alpha03` and `androidx.activity:activity-ktx:1.1.0-alpha03` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/b4eddfd7b427a4a334dceb6e0fb600de38ccdd4f..7abd0436770aa87911dffd1b405bbbf819da3335/activity).

**New features**

- Activity now depends on Core 1.1.0 stable.

**Bug fixes**

- Activity now depends on [Lifecycle `2.2.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.2.0-alpha04).

### Version 1.1.0-alpha02

August 7, 2019

`androidx.activity:activity:1.1.0-alpha02` and `androidx.activity:activity-ktx:1.1.0-alpha02` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/73a6643abc8d19bf3ae23376c260e6194f1bd7bd..ece690f1fdb4481b47c5128fd21d88da7d6850a6/activity).

**New features**

- `SavedStateViewModelFactory` is now the default factory used when using `by viewModels()`, the `ViewModelProvider` constructor, or `ViewModelProviders.of()` with a `ComponentActivity` ([b/135716331](https://issuetracker.google.com/issues/135716331))

### Version 1.1.0-alpha01

July 2, 2019

`androidx.activity:activity:1.1.0-alpha01` and `androidx.activity:activity-ktx:1.1.0-alpha01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7b91c9627d1e99d3ab66a4045fbb4ebf28427c02..73a6643abc8d19bf3ae23376c260e6194f1bd7bd/activity).

**New features**

- `activity` now depends on Lifecycle `2.2.0-alpha02`. ([aosp/1007817](https://android-review.googlesource.com/1007817))
- `activity-ktx` added a dependency on `lifecycle-runtime-ktx`; you no longer need to explicitly add it to your dependencies when using `activity-ktx` or libraries that depend on `activity-ktx` (such as `fragment-ktx`). ([aosp/987162](https://android-review.googlesource.com/987162))

## Version 1.0.0

### Version 1.0.0

September 5, 2019

`androidx.activity:activity:1.0.0` and `androidx.activity:activity-ktx:1.0.0` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/31e072b23ddd65615efc5f3fbece2276b6b5cae4..04474c7d7e242b12e34e49067cabadade0ee8a86/activity).

**Major Features of 1.0.0**

- **ComponentActivity** : `ComponentActivity` serves as the new base class for `FragmentActivity` in [Fragment `1.1.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0) and, by extension, `AppCompatActivity` in [AppCompat `1.1.0`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.1.0).
- **activity-ktx** : The `activity-ktx` module includes a `by viewModels` Kotlin property extension for accessing ViewModels. This module is automatically included when you include `fragment-ktx` from [Fragment `1.1.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0).
- **OnBackPressedDispatcher** : As a composable alternative to overriding `onBackPressed()`, you can now register a `OnBackPressedCallback` from any `LifecycleOwner` (such as a fragment) to intercept system back button events. A lambda with receiver version `addCallback` has been added to `activity-ktx`. See [Provide custom back navigation documentation](https://developer.android.com/guide/navigation/navigation-custom-back) for more details.
- **onRetainCustomNonConfigurationInstance deprecation** : the `onRetainCustomNonConfigurationInstance()` and the related `getLastCustomNonConfigurationInstance()` APIs have been deprecated. It is strongly recommended to use [ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel) to store non-configuration state as they offer a composable solution suitable for any `ViewModelStoreOwner` that makes the ownership of the retained objects clear and provides an `onCleared()` callback for cleaning up resources when the activity is finally destroyed.

### Version 1.0.0-rc01

July 2, 2019

`androidx.activity:activity:1.0.0-rc01` and `androidx.activity:activity-ktx:1.0.0-rc01` are released with no changes from `1.0.0-beta01`. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7b91c9627d1e99d3ab66a4045fbb4ebf28427c02..31e072b23ddd65615efc5f3fbece2276b6b5cae4/activity).

### Version 1.0.0-beta01

June 5, 2019

`androidx.activity::activity:1.0.0-beta01` and `androidx.activity:activity-ktx:1.0.0-beta01` are released with no changes from `1.0.0-alpha08`. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d0c85eb6e595cfd4383ef345e97e1b8d6acd0a44..7b91c9627d1e99d3ab66a4045fbb4ebf28427c02/activity).

### Version 1.0.0-alpha08

May 7, 2019

`androidx.activity:activity:1.0.0-alpha08` and `androidx.activity:activity-ktx:1.0.0-alpha08` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d0c85eb6e595cfd4383ef345e97e1b8d6acd0a44..baca2b5c73982f26b5630b87ff7dbf25622bbafc/activity).

**API changes**

- Breaking change: The previously deprecated `addOnBackPressedCallback` and `removeOnBackPressedCallback` methods on `ComponentActivity` have been removed. [aosp/953857](https://android-review.googlesource.com/953857)
- The `setEnabled()` and `isEnabled()` methods of `OnBackPressedCallback` are now final. [b/131416833](https://issuetracker.google.com/issues/131416833)
- The `remove()` method of `OnBackPressedCallback` is now final. [aosp/952720](https://android-review.googlesource.com/952720)
- `OnBackPressedDispatcher` now has public constructors, allowing you to construct your own instances for testing, etc. [aosp/953431](https://android-review.googlesource.com/953431)
- `onBackPressed()` for `ComponentActivity` is now explicitly marked as `@MainThread` [aosp/952721](https://android-review.googlesource.com/952721)

**Bug fixes**

- Fixed a `ConcurrentModificationException` when calling `remove()` from within the `handleOnBackPressed()` method of a `OnBackPressedCalback` that was added with a `LifecycleOwner`. [b/131765095](https://issuetracker.google.com/issues/131765095)

### Version 1.0.0-alpha07

April 25th, 2019

`androidx.activity:activity:1.0.0-alpha07` and `androidx.activity:activity-ktx:1.0.0-alpha07` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/00d1b79bfaa97c1a00793e5e80769f094316a6b0..1d1a928881b4a7a75a85ab5b723cc81c829f1c83/activity).

**API changes**

This release makes significant changes to the handling of the `onBackPressed()`. See the [updated custom back documentation](https://developer.android.com/guide/navigation/navigation-custom-back) for more details.

- The methods for `OnBackPressedCallback` and `OnBackPressedDispatcher` have been marked as `@MainThread`. ([aosp/943813](https://android-review.googlesource.com/943813))
- The `handleOnBackPressed()` method no longer returns a `boolean`. Instead, `OnBackPressedCallback` is now an abstract class that can be enabled or disabled - only when the new `isEnabled()` method returns true will `handleOnBackPressed()` be called, in which you **must** handle the back button. ([aosp/944518](https://android-review.googlesource.com/944518))
- The `addCallback` methods of `OnBackPressedDispatcher` no longer return a `Cancellable` instance. `OnBackPressedCallback` now contain a `remove()` method that fulfill this functionality, allowing you to call `remove()` during `handleOnBackPressed()`. ([aosp/944519](https://android-review.googlesource.com/944519)) ([aosp/946316](https://android-review.googlesource.com/946316))
- `activity-ktx` now contains a receiver scoped callback for `addCallback` that accepts a lamdba that implements `handleOnBackPressed()` and has access to `isEnabled` and `remove()` ([aosp/944520](https://android-review.googlesource.com/944520))

### Version 1.0.0-alpha06

April 3rd, 2019

`androidx.activity:activity:1.0.0-alpha06` and `androidx.activity:activity-ktx:1.0.0-alpha06` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/82ddb41c3e7be8ae7a4a3557e66edb5274c6d96c..00d1b79bfaa97c1a00793e5e80769f094316a6b0/activity).

**API changes**

- ComponentActivity now contain a second constructor that takes a `@LayoutRes int`, which replaces the previous behavior of annotating your AppCompatActivity class with `@ContentView`. This approach works in both app and library modules. ([b/128352521](https://issuetracker.google.com/issues/128352521))
- The `OnBackPressedCallback` related APIs on ComponentActivity have been deprecated in favor of the new `OnBackPressedDispatcher`, retrievable via `getOnBackPressedDispatcher()`. ([aosp/922523](https://android-review.googlesource.com/922523))
- Methods to add a new `OnBackPressedCallback` to the `OnBackPressedDispatcher` now return a `Cancellable` object, allowing removal of the callback without requiring an explicit reference to the `OnBackPressedDispatcher`. ([aosp/922523](https://android-review.googlesource.com/922523))
- Adding a `OnBackPressedCallback` with an associated `LifecycleOwner` now results in adding and removing the `OnBackPressedCallback` as the Lifecycle is started and stopped, respectively. ([aosp/922523](https://android-review.googlesource.com/922523))

### Version 1.0.0-alpha05

March 13th, 2019

`androidx.activity:activity:1.0.0-alpha05` and
`androidx.activity:activity-ktx:1.0.0-alpha05` are released. The full list of commits
included in this release can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/37f2d45370dc3d53ea3f327068edd21698c2e959..82ddb41c3e7be8ae7a4a3557e66edb5274c6d96c/activity).

**New features**

- `@ContentView` annotation lookups are now cached ([b/123709449](https://issuetracker.google.com/issues/123709449))

### Version 1.0.0-alpha04

January 30, 2019

`androidx.activity:activity 1.0.0-alpha04`and `androidx.activity:activity-ktx 1.0.0-alpha04` are released.

**New features**

- Added support for the `@ContentView` class annotation that allows you to indicate which layout XML file should be inflated as an alternative to using `setContentView()`. ([aosp/837619](https://android-review.googlesource.com/837619))

**API changes**

- Added a note that `getViewModelStore()` should not be overridden and will be made final in a future release. Please [file a feature request](https://issuetracker.google.com/issues/new?component=527362) if you are currently overriding this method. ([aosp/837619](https://android-review.googlesource.com/880712))

**Bug fixes**

- The `activity` module now depends on version 2.1.0-alpha02 of ViewModel to match the `activity-ktx` module's dependency.

### Version 1.0.0-alpha03

December 17, 2018

`androidx.activity 1.0.0-alpha03` is released.

**New features**

- ComponentActivity now implements `BundleSavedStateRegistryOwner` and depends on the newly released SavedState library \[[aosp/815133](https://android-review.googlesource.com/815133)\]
- ComponentActivity now works around an Android framework bug that would cause InputMethodManager to leak the last focused view \[[b/37122102](https://issuetracker.google.com/issues/37122102)\]

### Version 1.0.0-alpha02

December 3, 2018

**API changes**

- Added a note that `getLifecycle()` should not be overridden and will be made `final` in a future release. Please [file a feature
  request](https://issuetracker.google.com/issues/new?component=197448) if you are currently overriding this method. ([aosp/815834](https://android-review.googlesource.com/c/platform/frameworks/support/+/815834))

### Version 1.0.0-alpha01

November 5, 2018

`androidx.activity 1.0.0-alpha01` introduces
`ComponentActivity`, a new base class of the existing `FragmentActivity` and
`AppCompatActivity`.

**New features**

- You can now register an `OnBackPressedCallback` via `addOnBackPressedCallback` to receive `onBackPressed()` callbacks without needing to override the method in your activity.
- Added a new `by viewModels()` Kotlin property delegate for retrieving `ViewModel`s from a `ComponentActivity`.
- Pending input events (such as clicks) are now canceled in `onStop()`.

**API changes**

- The implementation of `LifecycleOwner` and `ViewModelStoreOwner` have been moved from `FragmentActivity` to `ComponentActivity`.
- `onRetainCustomNonConfigurationInstance` has been deprecated. Use a `ViewModel` for storing objects that need to survive configuration changes.