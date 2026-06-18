---
title: https://developer.android.com/jetpack/androidx/releases/core-locationbutton
url: https://developer.android.com/jetpack/androidx/releases/core-locationbutton
source: md.txt
---

# Core Locationbutton

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| June 17, 2026 | - | - | - | - |

## Declaring dependencies

To add a dependency on core locationbutton, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.core.locationbutton:locationbutton:"
    implementation "androidx.core.locationbutton:locationbutton-compose:"
    implementation "androidx.core.locationbutton:locationbutton-testing:"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core.locationbutton:locationbutton:")
    implementation("androidx.core.locationbutton:locationbutton-compose:")
    implementation("androidx.core.locationbutton:locationbutton-testing:")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2162367+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2162367&template=2342253)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha01

June 17, 2026

`androidx.core.locationbutton:locationbutton:1.0.0-alpha01`, `androidx.core.locationbutton:locationbutton-compose:1.0.0-alpha01`, and `androidx.core.locationbutton:locationbutton-testing:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/refs/heads/androidx-main/core/locationbutton).

**New Features**

The initial alpha release of AndroidX implementations of `LocationButton` that enable both view and compose based applications to easily request one-time precise location permission. For devices running Android 16 (API 36) or below, the library provides automatic backwards compatibility by defaulting to standard location permission prompts.

**API Changes**

- Added `LocationButton` View as an entry point for View based applications.
- Added `LocationButton` composable as an entrypoint for Compose based applications.
- Added `OnPermissionResultListener`, `OnErrorListener`, and `OnRequestPermissionsListener` for callback handling.
- Added `TestLocationButtonProvider` to allow apps to test flows relying on the secure `LocationButton`.