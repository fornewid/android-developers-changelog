---
title: https://developer.android.com/jetpack/androidx/releases/photopicker
url: https://developer.android.com/jetpack/androidx/releases/photopicker
source: md.txt
---

# photopicker

This library provides an integration for Compose and Android Views for the embedded photo picker.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 21, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/photopicker#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on PhotoPicker, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // For apps using Compose
    implementation "androidx.photopicker:photopicker-compose:1.0.0-alpha03"
    // For apps using Android views
    implementation "androidx.photopicker:photopicker:1.0.0-alpha03"
}
    
```

### Kotlin

```kotlin
dependencies {
    // For apps using Compose
    implementation("androidx.photopicker:photopicker-compose:1.0.0-alpha03")
    // For apps using Android views
    implementation("androidx.photopicker:photopicker:1.0.0-alpha03")
}
    
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1815792+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1815792&template=2142352)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha03

October 21, 2026

`androidx.photopicker:photopicker-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44ceb3b539fab42fa69f741b6eafc4f434fc4fad/photopicker).

**API Changes**

- Added EXTRA_SYSTEM_FALLBACK_PICK_IMAGES_REQUEST_LOCATION_METADATA_ACCESS to `PickVisualMedia` to allow requesting location metadata access in system fallback pickers. ([Ie5917](https://android-review.googlesource.com/#/q/Ie5917f0c8ba3bf941f2b34879328c3a9073fe61c))
- Renamed artifact `androidx.photopicker:photopicker` to `androidx.photopicker:photopicker-embedded` (package `androidx.photopicker.embedded`), `androidx.photopicker:photopicker-compose` to `androidx.photopicker:photopicker-embedded-compose` (package `androidx.photopicker.embedded.compose`), and `androidx.photopicker:photopicker-testing` to `androidx.photopicker:photopicker-embedded-testing` (package `androidx.photopicker.embedded.testing`). ([I48b9b](https://android-review.googlesource.com/#/q/I48b9b45c38b7c5c2e10b95f8a1cd358f6eee1a9d), [b/537430760](https://issuetracker.google.com/issues/537430760))
- Refactored `EmbeddedPhotoPickerState` to expose `surfacePackage` and `notifyVisibilityChanged` and added and `onError` callback. ([Ifa4b0](https://android-review.googlesource.com/#/q/Ifa4b0db08ce8c9b0e257786e27aa5a57bfe80d61))
- Added `setLocationMetadataAccessRequested` to `PickVisualMediaRequest` to allow requesting location metadata access in Photo Picker requests. ([Idde80](https://android-review.googlesource.com/#/q/Idde80c378009581dc25d44e2600f9a5ee74abf9f))
- Migrated `PickVisualMedia` and `PickMultipleVisualMedia` contracts, and `PickVisualMediaRequest` to the new `photopicker-activity` artifact. Copied tests. ([I2a201](https://android-review.googlesource.com/#/q/I2a201ac41fe675937d7d854d4306f26156fd9e29), [b/530216959](https://issuetracker.google.com/issues/530216959))
- Removed the `inputs` parameter from `rememberEmbeddedPhotoPickerState`. To reset the state when inputs change, wrap the call in a `key` block instead. ([I8a0c5](https://android-review.googlesource.com/#/q/I8a0c5b3f1c0cb989fc5a94fe1d90fe92343bad2d))
- Lowered the `minSdk` of the androidx.photopicker:photopicker and androidx.photopicker:photopicker-compose libraries to 23. ([I94e42](https://android-review.googlesource.com/#/q/I94e42624e79d97494629acedd891ad318e5733c7), [b/524083018](https://issuetracker.google.com/issues/524083018))
- `Revising Embedded PhotoPicker Compose APIs` ([Ie32c9](https://android-review.googlesource.com/#/q/Ie32c9a86b3c826863b727fdc90d909a4c5dfd84e))
- New libraries for Photopicker ([I0f52a](https://android-review.googlesource.com/#/q/I0f52a993080d9b71e027358e0a171491a0ba8862))
- New testing library for photopicker ([I7c1ec](https://android-review.googlesource.com/#/q/I7c1ec1d1136a7f965c7880494e920770f00e1216))

**Bug Fixes**

- `androidx.lifecycle:lifecycle-runtime` dependency was updated to 2.10.0. This version is required for bundled lifecycle runtime lint checks to run with AGP version 9.5.0-alpha04 or later. ([I99bfd](https://android-review.googlesource.com/#/q/I99bfdb355ffd7f1083dbdac4167b1f5577740116), [b/556807521](https://issuetracker.google.com/issues/556807521))
- `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))
- Updated Compose compileSdk to API 37. This means that a minimum AGP version of 9.2.0 is required when using Compose. ([Id45cd](https://android-review.googlesource.com/#/q/Id45cdca34ef948e06259b2dd9adc901b7c930492))

### Version 1.0.0-alpha02

July 01, 2026

`androidx.photopicker:photopicker:1.0.0-alpha02`, `androidx.photopicker:photopicker-compose:1.0.0-alpha02`, and `androidx.photopicker:photopicker-testing:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..f7668b81600bdf22bc975d3fc38e6fd22c94b585/photopicker).

**API Changes**

- Lowered the `minSdk` of the androidx.photopicker:photopicker and androidx.photopicker:photopicker-compose libraries to 23, while the APIs still require to be called starting from 34. ([I94e42](https://android-review.googlesource.com/#/q/I94e42624e79d97494629acedd891ad318e5733c7), [b/524083018](https://issuetracker.google.com/issues/524083018))
- Updating Embedded PhotoPicker Compose APIs (removing AbstractEmbeddedPhotoPickerState, renaming and change visibility of some fields from EmbeddedPhotoPickerState) ([Ie32c9](https://android-review.googlesource.com/#/q/Ie32c9a86b3c826863b727fdc90d909a4c5dfd84e), [b/449786033](https://issuetracker.google.com/issues/449786033))

**Bug Fixes**

- Updated Compose compileSdk to API 37. This means that a minimum AGP version of 9.2.0 is required when using Compose. ([Ic748a](https://android-review.googlesource.com/#/q/Ic748a207afaadaa5d1061603adae2028637bf85c), [b/413674743](https://issuetracker.google.com/issues/413674743))

### Version 1.0.0-alpha01

June 4, 2025

`androidx.photopicker:photopicker:1.0.0-alpha01`, `androidx.photopicker:photopicker-compose:1.0.0-alpha01`, and `androidx.photopicker:photopicker-testing:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15/photopicker).

**New Features**

- The initial alpha release of androidx implementations of the [Embedded PhotoPicker](https://developer.android.com/reference/android/widget/photopicker/package-summary) that enable both View based and Compose based applications to easily integrate with the Embedded Photopicker service.

**API Changes**

- Added `EmbeddedPhotopicker` composable for as an entrypoint for compose based applications.
  - `rememberEmbeddedPhotoPickerState` can be used (recommended) or applications can implement their own state management with the `EmbeddedPhotoPickerState` interface.
- Added `EmbeddedPhotopickerView` as an entrypoint for view based applications.
  - `EmbeddedPhotoPickerStateChangeListener` can be used to receive related callbacks to state inside the PhotoPicker.
- Added `TestEmbeddedPhotoPickerProvider` to allow apps to test flows that rely on the Embedded Photopicker.