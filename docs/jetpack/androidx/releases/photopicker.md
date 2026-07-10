---
title: https://developer.android.com/jetpack/androidx/releases/photopicker
url: https://developer.android.com/jetpack/androidx/releases/photopicker
source: md.txt
---

# photopicker

This library provides an integration for Compose and Android Views for the embedded photo picker.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 01, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/photopicker#1.0.0-alpha02) |

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
    implementation "androidx.photopicker:photopicker-compose:1.0.0-alpha02"
    // For apps using Android views
    implementation "androidx.photopicker:photopicker:1.0.0-alpha02"
}
    
```

### Kotlin

```kotlin
dependencies {
    // For apps using Compose
    implementation("androidx.photopicker:photopicker-compose:1.0.0-alpha02")
    // For apps using Android views
    implementation("androidx.photopicker:photopicker:1.0.0-alpha02")
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