---
title: https://developer.android.com/jetpack/androidx/releases/photopicker
url: https://developer.android.com/jetpack/androidx/releases/photopicker
source: md.txt
---

# photopicker

# photopicker

API Reference  
[androidx.photopicker](https://developer.android.com/reference/kotlin/androidx/photopicker/package-summary)  
This library provides an integration for Compose and Android Views for the embedded photo picker.  

| Latest Update | Stable Release | Release Candidate | Beta Release |                                           Alpha Release                                            |
|---------------|----------------|-------------------|--------------|----------------------------------------------------------------------------------------------------|
| June 4, 2025  | -              | -                 | -            | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/photopicker#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on PhotoPicker, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // For apps using Compose
    implementation "androidx.photopicker:photopicker-compose:1.0.0-alpha01"
    // For apps using Android views
    implementation "androidx.photopicker:photopicker:1.0.0-alpha01"
}
    
```

### Kotlin

```kotlin
dependencies {
    // For apps using Compose
    implementation("androidx.photopicker:photopicker-compose:1.0.0-alpha01")
    // For apps using Android views
    implementation("androidx.photopicker:photopicker:1.0.0-alpha01")
}
    
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1815792+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1815792&template=2142352)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha01

June 4, 2025

`androidx.photopicker:photopicker:1.0.0-alpha01`,`androidx.photopicker:photopicker-compose:1.0.0-alpha01`, and`androidx.photopicker:photopicker-testing:1.0.0-alpha01`are released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15/photopicker).

**New Features**

- The initial alpha release of androidx implementations of the[Embedded PhotoPicker](https://developer.android.com/reference/android/widget/photopicker/package-summary)that enable both View based and Compose based applications to easily integrate with the Embedded Photopicker service.

**API Changes**

- Added`EmbeddedPhotopicker`composable for as an entrypoint for compose based applications.
  - `rememberEmbeddedPhotoPickerState`can be used (recommended) or applications can implement their own state management with the`EmbeddedPhotoPickerState`interface.
- Added`EmbeddedPhotopickerView`as an entrypoint for view based applications.
  - `EmbeddedPhotoPickerStateChangeListener`can be used to receive related callbacks to state inside the PhotoPicker.
- Added`TestEmbeddedPhotoPickerProvider`to allow apps to test flows that rely on the Embedded Photopicker.