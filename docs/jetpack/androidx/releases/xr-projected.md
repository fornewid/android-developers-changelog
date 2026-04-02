---
title: https://developer.android.com/jetpack/androidx/releases/xr-projected
url: https://developer.android.com/jetpack/androidx/releases/xr-projected
source: md.txt
---

# XR Projected

API Reference  
[androidx.xr.projected](https://developer.android.com/reference/kotlin/androidx/xr/projected/package-summary)  
Build experiences that leverage the unique capabilities of connected XR devices.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/xr-projected#1.0.0-alpha05) |

## Declaring dependencies

To add a dependency on xr projected, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement xr projecteds
    implementation "androidx.xr.projected:projected:1.0.0-alpha05"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement xr projecteds
    implementation("androidx.xr.projected:projected:1.0.0-alpha05")

    // Use to implement xr projected complications
    implementation "androidx.xr.projected:projected-complications-data-source:1.0.0-alpha05"
    // (Kotlin-specific extensions)
    implementation "androidx.xr.projected:projected-complications-data-source-ktx:1.0.0-alpha05"

    // Use to implement a projected style and complication editor
    implementation("androidx.xr.projected:projected-editor:1.0.0-alpha05")

    // Can use to render complications.
    // This library is optional and projecteds may have custom implementation for rendering
    // complications.
    implementation "androidx.xr.projected:projected-complications-rendering:1.0.0-alpha05"
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1689664+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1689664&template=2070825)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha05

February 25, 2026

`androidx.xr.projected:projected:1.0.0-alpha05`, `androidx.xr.projected:projected-binding:1.0.0-alpha05`, and `androidx.xr.projected:projected-testing:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5dd0fe5f4702e29b6874a10d29459dc59f0d8502..855e9d89b825c1acd405c8aeb81dab7792e61dbc/xr/projected).

### Version 1.0.0-alpha04

January 28, 2026

`androidx.xr.projected:projected:1.0.0-alpha04` and `androidx.xr.projected:projected-binding:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9750bafc0c1ba237e91ada68cd21a7de0a4b4676..5dd0fe5f4702e29b6874a10d29459dc59f0d8502/xr/projected/projected).

### Version 1.0.0-alpha03

December 03, 2025

`androidx.xr.projected:projected:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/64e40d162445a8c6c0f233dfc6f8890c439b5d6e..9750bafc0c1ba237e91ada68cd21a7de0a4b4676/xr/projected/projected).

**API Changes**

- Added the experimental API for getting the `PresentationMode` ([I2dc0b](https://android-review.googlesource.com/#/q/I2dc0b6ae70e60d2768c03c7ba70920a146609760))
- Added the experimental API for collecting `ProjectedInputEvent`s ([I78ef8](https://android-review.googlesource.com/#/q/I78ef8007c242f6d78844a75f424de437a37d4486))
- Added `ProjectedDeviceController` and capabilities API ([If7d2d](https://android-review.googlesource.com/#/q/If7d2ddff2404eb4ef28e19c5358aaa8f7cf1e690))

### Version 1.0.0-alpha02

November 19, 2025

`androidx.xr.projected:projected:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/03fefa290d190d39c7e47025f76847d7b8baaf1c..64e40d162445a8c6c0f233dfc6f8890c439b5d6e/xr/projected/projected).

**New Features**

- Initial alpha release of the Projected library.

### Version 1.0.0-alpha01

October 22, 2025

`androidx.xr.projected:projected:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/03fefa290d190d39c7e47025f76847d7b8baaf1c/xr/projected/projected).

**New Features**

- Adds Projected XR library ([Ieedea7](https://android-review.googlesource.com/#/q/Ieedea759434c0dd59976d5e56f1d3e47f597d402))