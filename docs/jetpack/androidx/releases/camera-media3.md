---
title: https://developer.android.com/jetpack/androidx/releases/camera-media3
url: https://developer.android.com/jetpack/androidx/releases/camera-media3
source: md.txt
---

# camera media3

# camera media3

API Reference  
[androidx.camera.media3](https://developer.android.com/reference/kotlin/androidx/camera/media3/package-summary)  
TODO  

|  Latest Update  | Stable Release | Release Candidate | Beta Release |                                            Alpha Release                                             |
|-----------------|----------------|-------------------|--------------|------------------------------------------------------------------------------------------------------|
| August 13, 2025 | -              | -                 | -            | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/camera-media3#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on camera-media3, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement camera media3s
    implementation "androidx.camera.media3:media3-effect:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement camera media3s
    implementation("androidx.camera.media3:media3-effect:1.0.0-alpha04")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:618491+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=618491&template=1257717)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha04

August 13, 2025

`androidx.camera.media3:media3-effect:1.0.0-alpha04`is released. Version 1.0.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314..feae6a5205c47556fc7e6ce3a9557418a860cbd9/camera/media3/media3-effect).

**Bug Fixes**

- Fixed the crash in`androidx.camera.media3.effect`with media3 1.7 or later ([I450a6](https://android-review.googlesource.com/#/q/I450a60d6f082085ded2d19e335e783e2f077807d))

### Version 1.0.0-alpha03

May 7, 2025

`androidx.camera.media3:media3-effect:1.0.0-alpha03`is released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a7636b45f90dfa9f1364d109f60358af270a143a..a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314/camera/media3/media3-effect).

**Bug Fixes**

- Fixed the cameraX media3-effect crash when using with media3 1.6 dependency ([Ic1ff1](https://android-review.googlesource.com/#/q/Ic1ff129dc4467fc7fa376de3497a941231415fda))

### Version 1.0.0-alpha01

December 11, 2024

`androidx.camera.media3:media3-effect:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/619c6de87fe3f2c27da0045968f503c1bbd40ef6/camera/media3/media3-effect).

**New Features**

- An adapter library for using Media3 effects with CameraX. It's for adding Media3 effects into the camera pipeline with CameraX's`CameraEffect/SurfaceProcessor`API.