---
title: https://developer.android.com/jetpack/androidx/releases/camera
url: https://developer.android.com/jetpack/androidx/releases/camera
source: md.txt
---

# CameraX

[User Guide](https://developer.android.com/training/camerax) [Code Sample](https://github.com/android/camera-samples) API Reference  
[androidx.camera.camera2](https://developer.android.com/reference/kotlin/androidx/camera/camera2/package-summary)  
[androidx.camera.core](https://developer.android.com/reference/kotlin/androidx/camera/core/package-summary)  
[androidx.camera.extensions](https://developer.android.com/reference/kotlin/androidx/camera/extensions/package-summary)  
[androidx.camera.lifecycle](https://developer.android.com/reference/kotlin/androidx/camera/lifecycle/package-summary)  
[androidx.camera.view](https://developer.android.com/reference/kotlin/androidx/camera/view/package-summary)  
[androidx.camera.video](https://developer.android.com/reference/kotlin/androidx/camera/video/package-summary)  
[androidx.camera.mlkit.vision](https://developer.android.com/reference/kotlin/androidx/camera/mlkit/vision/package-summary)  
[androidx.camera.viewfinder](https://developer.android.com/reference/kotlin/androidx/camera/viewfinder/package-summary)  
[androidx.camera.effects](https://developer.android.com/reference/kotlin/androidx/camera/effects/package-summary)  
CameraX is an addition to Jetpack that makes it easier to add camera capabilities to your app. The library provides a number of compatibility fixes and workarounds to help make the developer experience consistent across many devices.


This table lists all the artifacts in the `androidx.camera` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| camera-camera2 | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-core | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-compose | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-effects | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-extensions | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-feature-combination-query | - | - | - | [1.5.0-alpha06](https://developer.android.com/jetpack/androidx/releases/camera#1.5.0-alpha06) |
| camera-feature-combination-query-play-services | - | - | - | [1.5.0-alpha06](https://developer.android.com/jetpack/androidx/releases/camera#1.5.0-alpha06) |
| camera-lifecycle | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-mlkit-vision | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-view | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |
| camera-viewfinder | - | - | [1.3.0-beta02](https://developer.android.com/jetpack/androidx/releases/camera#1.3.0-beta02) | [1.4.0-alpha07](https://developer.android.com/jetpack/androidx/releases/camera#1.4.0-alpha07) |
| camera-video | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera#1.6.0-rc01) | - | - |

This library was last updated on: February 25, 2026

## Device testing

CameraX is tested on many devices in our lab. To see a list of the devices
currently in the lab, see [CameraX lab-tested
devices](https://developer.android.com/training/camerax/devices).

## Declaring dependencies

To add a dependency on CameraX, you must add the Google Maven repository to
your project. Read
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more
information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
  // CameraX core library using the camera2 implementation
  def camerax_version = "1.6.0-rc01"
  // The following line is optional, as the core library is included indirectly by camera-camera2
  implementation "androidx.camera:camera-core:${camerax_version}"
  implementation "androidx.camera:camera-camera2:${camerax_version}"
  // If you want to additionally use the CameraX Lifecycle library
  implementation "androidx.camera:camera-lifecycle:${camerax_version}"
  // If you want to additionally use the CameraX VideoCapture library
  implementation "androidx.camera:camera-video:${camerax_version}"
  // If you want to additionally use the CameraX View class
  implementation "androidx.camera:camera-view:${camerax_version}"
  // If you want to additionally add CameraX ML Kit Vision Integration
  implementation "androidx.camera:camera-mlkit-vision:${camerax_version}"
  // If you want to additionally use the CameraX Extensions library
  implementation "androidx.camera:camera-extensions:${camerax_version}"
}
```

### Kotlin

```kotlin
dependencies {
    // CameraX core library using the camera2 implementation
    val camerax_version = "1.6.0-rc01"
    // The following line is optional, as the core library is included indirectly by camera-camera2
    implementation("androidx.camera:camera-core:${camerax_version}")
    implementation("androidx.camera:camera-camera2:${camerax_version}")
    // If you want to additionally use the CameraX Lifecycle library
    implementation("androidx.camera:camera-lifecycle:${camerax_version}")
    // If you want to additionally use the CameraX VideoCapture library
    implementation("androidx.camera:camera-video:${camerax_version}")
    // If you want to additionally use the CameraX View class
    implementation("androidx.camera:camera-view:${camerax_version}")
    // If you want to additionally add CameraX ML Kit Vision Integration
    implementation("androidx.camera:camera-mlkit-vision:${camerax_version}")
    // If you want to additionally use the CameraX Extensions library
    implementation("androidx.camera:camera-extensions:${camerax_version}")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:618491+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=618491&template=1257717)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Camera Viewfinder Compose Version 1.0

### Version 1.0.0-alpha02

June 12, 2024

`androidx.camera:camera-viewfinder-compose:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7d2a9b0f7f27c85a187b05044b5fb8f1281a191..97ce0972adadb34722870dfe4d0a6bb0540d13e7/camera/camera-viewfinder-compose).

### Version 1.0.0-alpha01

May 14, 2024

`androidx.camera:camera-viewfinder-compose:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7d2a9b0f7f27c85a187b05044b5fb8f1281a191/camera/camera-viewfinder-compose).

**New Features**

- New library. This library introduces a Compose native Viewfinder composable, that can be used with CameraX and Camera2. The composable Viewfinder supports different aspect ratios, and handling of touch events.

## Camera Viewfinder Version 1.4

### Version 1.4.0-alpha07

June 12, 2024

`androidx.camera:camera-viewfinder:1.4.0-alpha07` and `androidx.camera:camera-viewfinder-core:1.4.0-alpha07` are released. Version 1.4.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7d2a9b0f7f27c85a187b05044b5fb8f1281a191..97ce0972adadb34722870dfe4d0a6bb0540d13e7/camera).

### Version 1.4.0-alpha06

May 14, 2024

`androidx.camera:camera-viewfinder:1.4.0-alpha06` and `androidx.camera:camera-viewfinder-core:1.4.0-alpha06` are released. Version 1.4.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7f20a95e69d42bdab1dbae806dd5dee41b86143d..c7d2a9b0f7f27c85a187b05044b5fb8f1281a191/camera).

**API Changes**

- Rename `Viewfinder`'s `ImplementationMode` Enums to better reflect underlying implementations, and add fixed constants for `TransformationInfo.sourceRotation`. ([Ic6149](https://android-review.googlesource.com/#/q/Ic61497ab594cf68858566e7ea21cbdb35376a58a))
- Added `ZoomGestureDetector.ZoomEvent` to encapsulates the states of a zoom gesture. ([I84cdf](https://android-review.googlesource.com/#/q/I84cdfd505443171f9910fb0b3fd40fdaf307796b))

## Camera Version 1.6

### Version 1.6.0-rc01

February 25, 2026

`androidx.camera:camera-*:1.6.0-rc01` is released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82004373076cf552e53b43166e1b4ddfbcfec21e..0dc6fa695e63a0bbc17f07b7368ba2567fb47d01/camera).

### Version 1.6.0-beta02

February 11, 2026

`androidx.camera:camera-*:1.6.0-beta02` is released. Version 1.6.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/48e95c38588deabd109b960f6d6ba5f47461c192..82004373076cf552e53b43166e1b4ddfbcfec21e/camera).

**Bug Fixes**

- Fixed `ImageCapture` OUTPUT_FORMAT_RAW_JPEG in-memory capture `IllegalArgumentException` issue. ([Id4eec](https://android-review.googlesource.com/#/q/Id4eece80253b2f5fbebf4471637cc3939ac890a6), [b/479990902](https://issuetracker.google.com/issues/479990902))
- Migrated to AndroidX Media3 muxer. This fixed 1: video corruption during unexpected interruptions or app termination and 2: crashes when saving videos to proxy file descriptors. ([I23b63](https://android-review.googlesource.com/#/q/I23b63968780daf56e726fa1ab0897fa98aba3291), [b/433649708](https://issuetracker.google.com/issues/433649708), [b/264812009](https://issuetracker.google.com/issues/264812009), [b/475750115](https://issuetracker.google.com/issues/475750115))

### Version 1.6.0-beta01

January 28, 2026

`androidx.camera:camera-*:1.6.0-beta01` is released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/84753047f87d847904220ad53b1c78d1a98189c4..5fc4e0225a10d812728a4bece5a2f6e82737df85/camera).

**Bug Fixes**

- Fixed `CameraExtensionsInfo` current type issue in CameraX 1.6.0-alpha that the LiveData object can't receive the updated type data. ([I2c7a5](https://android-review.googlesource.com/#/q/I2c7a5eb65d820bbf99fec7b4bec0175455e11063))
- Updated the [ExifInterface](https://developer.android.com/reference/android/media/ExifInterface) dependency to include a fix for parsing JPEGs with 0xFF padding, which resolves image capture failures on devices where the JPEG encoder adds fill bytes before markers. ([I0eb49](https://android-review.googlesource.com/#/q/I0eb49797f167c36511bc5a2ea5c31a920f598b6d))

### Version 1.6.0-alpha02

December 17, 2025

`androidx.camera:camera-*:1.6.0-alpha02` is released. Version 1.6.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dacd36e7413e15947cdd89e21c189fead769bfab..84753047f87d847904220ad53b1c78d1a98189c4/camera).

**New Features**

- Added a groupable feature to denote the video stabilization feature in a session config. Developers can now request video stabilization as a required or preferred feature, aligning it with other groupable features like UHD_RECORDING, PREVIEW_STABILIZATION. ([Ic6757](https://android-review.googlesource.com/#/q/Ic6757a2a1de6c66a1471ee0a32743cc041eaa3b5), [b/419766630](https://issuetracker.google.com/issues/419766630))
- Added groupable features to denote the video recording quality in a session config. Developers can now request a specific quality (e.g., UHD, FHD) as a required or preferred feature, aligning it with other groupable features like HDR and 60 FPS. ([Ib5cd3](https://android-review.googlesource.com/#/q/Ib5cd349f4995661d9aa753c8dacfcbc85e8d9144), [b/437820285](https://issuetracker.google.com/issues/437820285))
- Added support for using both the `CameraEffect` and the feature groups API in `SessionConfig`. ([I17f18](https://android-review.googlesource.com/#/q/I17f18f71e99f46d8c63d95da364cc3f8e7d4ce7c), [b/406370934](https://issuetracker.google.com/issues/406370934))
- Added support for using both the `ImageAnalysis` and the feature groups API in `SessionConfig`. ([I87833](https://android-review.googlesource.com/#/q/I87833dab66b27899d9c8740caa85c5427a45bcc1), [b/406371720](https://issuetracker.google.com/issues/406371720))

**API Changes**

- Added `addUseCase` setter function for `ExtensionSessionConfig.Builder` and added the lacking getters for `ExtensionSessionConfig`. ([I71e07](https://android-review.googlesource.com/#/q/I71e077c85a32b7dd9a2279747fb509e8c8d0220b), [b/453988621](https://issuetracker.google.com/issues/453988621))
- Added `ExtensionsManager.getInstance` API which is a suspending version of `ExtensionsManager.getInstanceAsync` ([I3a0a9](https://android-review.googlesource.com/#/q/I3a0a9d3f7790740cb9dc55beb61368f217ea19eb), [b/452208792](https://issuetracker.google.com/issues/452208792))
- Renamed `isFeatureGroupSupported` to `isSessionConfigSupported`, and make it support any types of `SessionConfig`. ([I21616](https://android-review.googlesource.com/#/q/I2161610a0e067756efd906284bfe4c69a3029c1a), [b/448781299](https://issuetracker.google.com/issues/448781299))
- Converted `ExtensionsManager` into Kotlin implementation. ([I73091](https://android-review.googlesource.com/#/q/I730915ebb9015743aa298874211c79dd3abcfe5b), [b/452208792](https://issuetracker.google.com/issues/452208792))
- Added `CameraProvider#getCameraInfo(CameraSelector, SessionConfig)` to retrieve `CameraInfo` when the `SessionConfig` can affect camera selection. For example, when using an `ExtensionSessionConfig`. ([Ic548c](https://android-review.googlesource.com/#/q/Ic548c97cbe916f8085c04f5642982608c294b6d1), [b/451891648](https://issuetracker.google.com/issues/451891648))
- Exposed `ExtensionSessionConfig` API. Apps can create an `ExtensionSessionConfig` and use it to create an extensions session now. ([I6354c](https://android-review.googlesource.com/#/q/I6354c9e14343bd62e19554044c537d25de90adb5), [b/448524373](https://issuetracker.google.com/issues/448524373))
- The `androidx.camera.video.HighSpeedVideoSessionConfig` API is no longer experimental and is now a fully stable public API. ([I492d4](https://android-review.googlesource.com/#/q/I492d493fa9b8e372b7251de3790d2f974782f5f8), [b/447558239](https://issuetracker.google.com/issues/447558239))
- The `androidx.camera.core.SessionConfig` API is no longer experimental and is now a fully stable public API. ([Idc87a](https://android-review.googlesource.com/#/q/Idc87ad64f1c2914bdca85d4b6d5ae60f6bfbd966), [b/447558437](https://issuetracker.google.com/issues/447558437))

**Bug Fixes**

- Fixed a crash due to an `IllegalArgumentException: Dynamic range profile cannot be converted to a DynamicRange object:` on Android 17 or higher. ([Ibd7b5](https://android-review.googlesource.com/#/q/Ibd7b5f532f7af0f43415aaef09cc9ce5f26763f6), [b/463465353](https://issuetracker.google.com/issues/463465353))
- Excluded problematic YUV format output sizes from Samsung Z Fold 4 device. The received images have distortion issue when using those output sizes. ([I776bf](https://android-review.googlesource.com/#/q/I776bf1f9447fba5b6354b597fb8067d25419756a), [b/460322307](https://issuetracker.google.com/issues/460322307))
- Fixed `CaptureRequest.FLASH_MODE` not being applied when set through the `Camera2Interop` API. ([I0004c](https://android-review.googlesource.com/#/q/I0004c7346db74b7e42a44bcd40d68e16320ce724), [b/459608684](https://issuetracker.google.com/issues/459608684))
- Fixed a device-specific issue on Samsung A53 where image capture with torch enabled would fail sometimes if `VideoCapture` use case is bound. ([I0f183](https://android-review.googlesource.com/#/q/I0f183808184febdcb203e8f5658e7663d8dc44b9), [b/458197367](https://issuetracker.google.com/issues/458197367))
- Fixes an issue on some devices where using the flash with the ultra-wide camera may result in underexposed images. ([Ib7530](https://android-review.googlesource.com/#/q/Ib75308343ede2999677ffce021affa013d175668), [b/444590340](https://issuetracker.google.com/issues/444590340))

### Version 1.6.0-alpha01

October 22, 2025

`androidx.camera:camera-*:1.6.0-alpha01` is released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..dacd36e7413e15947cdd89e21c189fead769bfab/camera).

**New Features**

- CameraX has migrated to a unified, high-performance camera stack, which is also used by the Pixel camera app. Known as `CameraPipe`, this new stack is a collaboration between the CameraX and Pixel Camera teams. It ensures that all improvements are shared, benefiting both CameraX users and the Pixel camera app.

**API Changes**

- Added new APIs for dynamic camera add/removal detection. See the `CameraPresenceListener` API for more details. ([I41ead](https://android-review.googlesource.com/#/q/I41ead2e9c432bc8507951e598f04369aad8a9f54), [b/427182232](https://issuetracker.google.com/issues/427182232), [b/419441394](https://issuetracker.google.com/issues/419441394))

**Bug Fixes**

- The feature group API now provides consistent results when `PREVIEW_STABILIZATION` is used with `VideoCapture`. This corrects a bug that caused inconsistent results when a `Preview` use case was not also active. ([Ifed82](https://android-review.googlesource.com/#/q/Ifed82d0d9ce2cfdb407523535d9e4c8c4a51f46d), [b/449913903](https://issuetracker.google.com/issues/449913903))
- Fixed an issue where unsupported preferred features were incorrectly made available. Features are now correctly filtered when their required use cases are not met. ([I38db8](https://android-review.googlesource.com/#/q/I38db88ca0ae9c2cd87b49ceffddd7980b3178576), [b/449532342](https://issuetracker.google.com/issues/449532342))
- Fixed glitchy video result on Samsung Galaxy S6. ([I612d9](https://android-review.git.corp.google.com/#/q/I612d902c2aa36dfd5b77a53a59a5646cadf96272), [b/235127608](https://issuetracker.google.com/issues/235127608))
- Fixed an issue where `CameraInfo#isFeatureGroupSupported` could incorrectly return true for `PREVIEW_STABILIZATION` if the `SessionConfig` in the query was already configured with other features. ([I2c355c](https://android-review.googlesource.com/#/q/I2c355c533f737d1797a7427d37661781cd1480b2), [b/437816469](https://issuetracker.google.com/issues/437816469))

## Camera Version 1.5

### Version 1.5.3

January 28, 2026

`androidx.camera:camera-*:1.5.3` is released. Version 1.5.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0975f1cec9e7c5b1192d3ceb925b3178cd234957..2afad3835627a7fdd11578788696f14b7aff6017/camera).

**Bug Fixes**

- Updated the [ExifInterface](https://developer.android.com/reference/android/media/ExifInterface) dependency to 1.4.2. This fixes an image capture failure that occurs on devices producing JPEGs with additional (and permitted) 0xFF bytes before a marker. ([I16df4](https://android-review.googlesource.com/#/q/I16df449e55031529e48c806d48a0658c9b41c711))

### Version 1.5.2

December 4, 2025

`androidx.camera:camera-*:1.5.2` is released. Version 1.5.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..0975f1cec9e7c5b1192d3ceb925b3178cd234957/camera).

**Bug Fixes**

- Fixed a crash due to an `IllegalArgumentException: Dynamic range profile cannot be converted to a DynamicRange object:` on Android 17 or higher. ([Ic9184](https://android-review.googlesource.com/#/q/Ic91844818c0072e2585c61067e500c514832f155))
- Fixed a bug leading to inconsistent feature group API results when `PREVIEW_STABILIZATION` feature was added with `VideoCapture` use case, but without `Preview` use case. ([Ifed82](https://android-review.googlesource.com/#/q/Ifed82d0d9ce2cfdb407523535d9e4c8c4a51f46d))
- Fixed preferred features not being filtered out despite lacking the required use cases for the features to be supported. ([I38db8](https://android-review.googlesource.com/#/q/I38db88ca0ae9c2cd87b49ceffddd7980b3178576))

### Version 1.5.1

October 08, 2025

`androidx.camera:camera-*:1.5.1` is released. Version 1.5.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bf14d325dfcbc73bf18b092f0435beaaf465e126..e7bb7786b42348603fed2825d18815e6dfa9bd4b/camera).

**Bug Fixes**

- Support `CameraEffect` in concurrent camera composition mode. The effect will be applied on the composition output. Please note that `mirrorMode` in `VideoCapture` will be ignored when effect is set in concurrent camera composition mode. ([If3d00](https://android-review.googlesource.com/#/q/If3d00d1463fe07a983f28d4355f822c0679db9bb), [b/425565129](https://issuetracker.google.com/issues/425565129))
- Fixed the issue where `mirrorMode` is not applied correctly to the secondary camera in concurrent camera composition mode. ([I686cd](https://android-review.googlesource.com/#/q/I686cde569e4cd5f4081b7a9d82ff6992fd3bf595), [b/446430827](https://issuetracker.google.com/issues/446430827))
- Support binding `Preview`, `ImageCapture` and `VideoCapture` together in concurrent camera non-composition mode. ([Ib410a](https://android-review.googlesource.com/#/q/Ib410aea04d264e6dc07ddc73a69bfa36a34f386e), [b/443009871](https://issuetracker.google.com/issues/443009871))
- Fixed an issue where UseCases such as `ImageCapture` and `VideoCapture` would lose their target rotation information if they were recreated. This could cause images or videos to have an incorrect orientation if a setting like `imageCaptureMode` was changed after the device had been rotated. ([I477c8](https://android-review.googlesource.com/#/q/I477c811394b7e9cc9849903683dc6d8dd6560643), [b/444734537](https://issuetracker.google.com/issues/444734537))
- Fixed an issue that prevented Preview from selecting 16:9 resolutions and `VideoCapture` from recording at QUALITY_1080P. This problem occurred when using a default Preview resolution configuration while the internal `StreamSharing` feature was active (e.g., when four UseCases are bound simultaneously). ([I493cb](https://android-review.googlesource.com/#/q/I493cb6d91d717ad47bdfd5db99c23dd9399c8672), [b/440364875](https://issuetracker.google.com/issues/440364875))
- Fixed the crash when effect is being activated after `SurfaceProcessor` is shut down ([I2c450](https://android-review.googlesource.com/#/q/I2c450c1a94806acea25038dcc3ab1ea8348e166c), [b/414150174](https://issuetracker.google.com/issues/414150174))
- Fixed a bug in `CameraController` that caused an `IllegalStateException` when an initial UseCase selected the maximum resolution, which subsequently prevented other UseCases from being bound. ([Ifb758](https://android-review.googlesource.com/#/q/Ifb758bef1582b20717a64b67657a9358e5600034), [b/440374234](https://issuetracker.google.com/issues/440374234))
- Excludes problematic YUV_420_888 output sizes for Nokia 7 Plus that will cause the silent fail problem without any error messages reported. ([I3af47](https://android-review.googlesource.com/#/q/I3af47fafb152e0b4227731740cd1434578abca96), [b/436524501](https://issuetracker.google.com/issues/436524501))
- Fixed an issue where `CameraInfo#isFeatureGroupSupported` could incorrectly return true for the `PREVIEW_STABILIZATION` feature. This could sometimes occur when querying with a `SessionConfig` that was already configured with other features. ([I2c355](https://android-review.googlesource.com/#/q/I2c355c533f737d1797a7427d37661781cd1480b2), [b/437816469](https://issuetracker.google.com/issues/437816469))
- Improved `CameraXViewfinder` stability on older API levels and devices with `SurfaceView` issues by defaulting to `TextureView` in such scenarios. This fallback mechanism is the new default but can be programmatically overridden. ([Ieb476](https://android-review.googlesource.com/#/q/Ieb4763c1e6102059a553900fea0557e1a443f6bb), [b/437496463](https://issuetracker.google.com/issues/437496463))
- Fixed a memory leak in `PreviewView` where it could prevent its Activity from being garbage collected. This happens if a new `SurfaceRequest` arrives before the previous one is handled. ([I4aa0b](https://android-review.git.corp.google.com/q/I4aa0b3b2d742268394c7bfeb66be3ab448a278b5),[b/443112512](https://issuetracker.google.com/issues/443112512))
- Fixed high-speed/slow-motion recording failed on Huawei P smart, Infinix Hot 40i and Realme C53. ([40a668e](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3756548), [b/442984200](https://issuetracker.google.com/issues/442984200))

### Version 1.5.0

September 10, 2025

`androidx.camera:camera-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3496263efa2133a8c8cd25f4ae6509b9d28a788f..bf14d325dfcbc73bf18b092f0435beaaf465e126/camera).

**Important changes since 1.4.0:**

- High-speed and Slow-motion Recording: Easily integrate high-speed (120/240 fps) and slow-motion video recording with minimal code. Refer to `Recorder#getHighSpeedVideoCapabilities(CameraInfo)` and `HighSpeedVideoSessionConfig` for details.
- `SessionConfig` and `FeatureGroup` API: The new `SessionConfig` API allows you to configure the camera session and enable multiple features together safely, including HLG (HDR), UltraHDR, 60 FPS, and Preview stabilization. You can also set a preferable feature group with priority, letting CameraX determine the optimal supported combination. See `SessionConfig.Builder#setPreferredFeatureGroup`, `SessionConfig.Builder#setRequiredFeatureGroup`, and `CameraInfo#isFeatureGroupSupported(SessionConfig)` for more information.
- Deterministic Frame Rate API: Address previous limitations with `setTargetFrameRate` by using `CameraInfo.getSupportedFrameRateRanges(sessionConfig)` to query and `SessionConfig.setExpectedFrameRateRange` to set precise and supported frame rates.
- Camera Extensions: UltraHDR format is now supported with Extensions. Check `ImageCapture.getImageCaptureCapabilities(cameraInfo).getSupportedOutputFormats()` and enable it in `ImageCapture.Builder.setOutputFormat`. Zoom ratio and preview stabilization capabilities are now reflected when Extensions are enabled.
- Torch Strength: Adjust torch strength using `CameraControl.setTorchStrengthLevel`.
- Low Light Boost Mode: You can enable the low light boost mode(`CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY`) by the following APIs: Refer to `CameraInfo#isLowLightBoostSupported`, `CameraInfo#getLowLightBoostState`, and `CameraControl#enableLowLightBoostAsync`.
- Video Capture: `VideoRecordEvent.Finalize.ERROR_INSUFFICIENT_STORAGE` is now triggered for insufficient storage during recording. `PendingRecording.withAudioEnabled(boolean initialMuted)` allows controlling the initial mute state for audio recording.
- Image Capture: Support for DNG (RAW) and JPEG + DNG (RAW) formats in `ImageCapture`. Check `ImageCaptureCapabilities(CameraInfo).getSupportedOutputFormats()` for RAW support. Use overloaded `takePicture` APIs with multiple `OutputFileOptions` for RAW+DNG capture.
- Image Analysis: Support for NV21 format in `ImageAnalysis`. Enable it with `ImageAnalysis.Builder.setOutputImageFormat(OUTPUT_IMAGE_FORMAT_NV21)`.

### Version 1.5.0-rc01

August 13, 2025

`androidx.camera:camera-*:1.5.0-rc01` is released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f22a8ba695b5a3d975f57d279262d9d39444d990..3496263efa2133a8c8cd25f4ae6509b9d28a788f/camera).

**Bug Fixes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Removed the 10-bit output restriction for the low-light boost auto-exposure mode. Applications can now simultaneously enable both features on supported devices. ([I5a638](https://android-review.googlesource.com/#/q/I5a638d6de82aab011d9533acda0bbfc37c200562))
- Resolved an issue that caused devices with `UniSoc` chipsets to hang when capturing an image. The problem occurred when `VideoCapture`, `Preview`, and `ImageCapture` were used simultaneously with all streams set to a 1280x720 resolution. ([Ia00c4](https://android-review.googlesource.com/#/q/Ia00c4df593e44451ecc67726addbc4cf294c295d), [b/380802479](https://issuetracker.google.com/issues/380802479))
- Fixed preview black screen when no high-speed frame rate is set for high-speed/slow-motion recording. ([cdf0ff2e9](https://android-review.git.corp.google.com/q/cdf0ff2e98fdebd426e35278658d67918af00c48))
- Improve error handling and logging in `getViewportAspectRatioInt` ([82fca18](https://android-review.googlesource.com/#/q/82fca18eb145bd4043963e47c4c3c00a194972d4))

### Version 1.5.0-beta02

July 16, 2025

`androidx.camera:camera-*:1.5.0-beta02` is released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314..f22a8ba695b5a3d975f57d279262d9d39444d990/camera).

**API Changes**

- Added new APIs to set or query groups of high-quality features more intuitively and accurately as these features may not be supported as a combination across all devices. `SessionConfig` now contains new APIs to denote a group of features as either required or preferred. The `CameraInfo.isFeatureGroupSupported` API allows to know if a feature group is supported before binding a `SessionConfig`. `SessionConfig` also allows setting a listener to know which features are finally selected when a session config is bound. ([Ie4d60](https://android-review.googlesource.com/#/q/Ie4d60e3ef392ae7e5016cc9c102e5c72bb6a10fd))
- Added new API `SessoinConfig.Builder.setFrameRateRange(Range<Integer>)` and `CameraInfo.getSupportedFrameRateRanges(SessionConfig)`, enabling developers to query guaranteed supported frame rates constrained by a specific `SessionConfig` and then apply the frame rate on `SessionConfig`. ([Ieacf7](https://android-review.googlesource.com/#/q/Ieacf7814313cb735ef17d34cc5bbf23c6a3fe917))
- Introduced the new `SessionConfig` API, which includes a better abstraction for configuring use cases, session parameters, `CameraEffect`, `ViewPort` and etc. Binding a `SessionConfig` to a LifecycleOwner opens the camera session, configures it using the specified use cases and session parameters, and applies the designated `CameraEffect` and `ViewPort`. When updating a new `SessionConfig` to the same `LifecycleOwner`, you can just bind a new `Sessionconfig` without the need of invoking unbind or `unbindAll` first. ([Iedfc3](https://android-review.googlesource.com/#/q/Iedfc38a69cd6d67e2791381700545ebd2d4ba4ca))
- Added new APIs to record high-speed/slow-motion video. See `HighSpeedVideoSessionConfig` API for more details. ([Ia16f3](https://android-review.googlesource.com/#/q/Ia16f391118003b964e26c47b7c4e1a291010538c))

**Bug Fixes**

- Fixed `ImageCaptureCapabilities#getSupportedOutputFormats()` API reporting RAW formats as supported in some devices which doesn't actually have RAW capability. ([Ibcadb](https://android-review.googlesource.com/#/q/Ibcadbc1b08383e58842f6c860f3b663a1ba649ff))
- Fixed the memory leak that happens when `PreviewView` is used, `CameraEffect` is enabled or binding 4 use cases(StreamSharing) ([I87468](https://android-review.googlesource.com/#/q/I874686eceab882ea96c5096b38c7e65c681c1830))
- Fixed a video recording crash by `AssertionError`: Invalid internal audio state: IDLING. ([I38d4b](https://android-review.googlesource.com/#/q/I38d4ba14fc11793d7f4ec2bf7d58ae9645a0fed3), [b/414259796](https://issuetracker.google.com/issues/414259796))
- Fixed the issue when the app runs in an external display and the device is landscape, the preview in `PreviewView` becomes stretched or sideway ([Ia917a](https://android-review.googlesource.com/#/q/Ia917ae4c5b33df7c0f9626e2cbd202a938747059))
- Fixed the issue that Preview Stabilization settings are not correctly applied when the camera stream is sharing between Preview and VideoCapture.([I5430e](https://android-review.googlesource.com/#/q/I5430e4053e4e53357c5959377147a495daf439f7))
- `CameraXViewfinder` now properly handles surface replacement in the underlying `Viewfinder`. This covers scenarios such as when an `EXTERNAL` viewfinder on API level 28 or lower moves off screen or if a `CameraXViewfinder` (with any `ImplementationMode`) is part of `moveableContentOf()`. In cases where the underlying `ViewfinderSurfaceSession` cannot be kept alive, the `CameraXViewfinder` will invalidate the current CameraX `SurfaceRequest`, allowing CameraX to use the new `Surface`. ([I79432](https://android-review.googlesource.com/#/q/I79432d3ad761fce4db134297c6057f357d9a7cf0))
- Fixes an issue on Android 10/11 where the `EXTERNAL` `CameraXViewfinder` could appear stretched or incorrect due to transformation operations (like scale or translate) being applied too early. The system now waits for the Surface to be created before applying these transformations in the layout phase, ensuring correct output. ([Icc77c](https://android-review.googlesource.com/#/q/Icc77c83b338df1828014f8fe27703d90e62cdea5))
- Composable `CameraXViewfinder` now works correctly with Compose's `Pager`. This change ensures that the Composable can be successfully reset by implementing the `onReset` callback of `AndroidView`, supporting both `EMBEDDED` and `EXTERNAL` implementations. ([I0d9be](https://android-review.googlesource.com/#/q/I0d9be911aea9fed574dde8ba988af7882dfc2dc9))
- Fixed a lifecycle owner leak that happens when unbinding use cases from a lifecycle owner without shutting down the camera provider.

### Version 1.5.0-beta01

May 7, 2025

`androidx.camera:camera-*:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/824a6d81bccbc4bf5286a94e6476d35825adf198..a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314/camera).

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `ContentScale` and Alignment can now be used in the viewfinder to scale and place the displayed surface within its container, similar to how `androidx.compose.foundation.Image` behaves. ([Ibcea3](https://android-review.googlesource.com/#/q/Ibcea3e4d1ea1badc0134df3f328a1710dcb4c20e))
- `TransformationInfo` now has default values for all args. This will allow Viewfinders to be created without any `TransformationInfo`, which will default to a source rotation of 0, no source mirroring, and no crop rect. ([I2b1b2](https://android-review.googlesource.com/#/q/I2b1b26e8f966363809a235424e0c19f2a6bd97b8))
- Added `LifecycleCameraProvider`, which is a camera provider that can be instantiated with different configurations for features such as accessing the camera of a virtual device by configuring with a customized context. ([Ia2992](https://android-review.googlesource.com/#/q/Ia29928816ac5750f2875473fe600b62d99185047))

**Bug Fixes**

- Fixed preview freeze issue when using `ImageAnalysis` with another stream that uses `TEMPLATE_RECORD` on Samsung SM-E556B device. ([Ic0e62](https://android-review.googlesource.com/#/q/Ic0e62cdec6dae778f7fab85e13a1b8790446de2f), [b/409478042](https://issuetracker.google.com/issues/409478042))
- Fixed preview freeze issue when using `ImageAnalysis` with another stream that uses `TEMPLATE_RECORD` on Samsung SM-M556B device. ([Ic1a6a](https://android-review.googlesource.com/#/q/Ic1a6a019c1525f30d7b863f732d421e36e5c978c), [b/395822788](https://issuetracker.google.com/issues/395822788))
- Fixed Extensions NIGHT mode `AssertError` issue on Android 15 Pixel devices when doing zoom related operations. ([I27a5d](https://android-review.googlesource.com/#/q/I27a5d514948d205a3dee80e7412c755261fb2bd0), [b/401460276](https://issuetracker.google.com/issues/401460276))
- Fix ML Kit Analyzer incorrect bounding box coordinates issue when using `CameraController`. ([Iae91b](https://android-review.googlesource.com/#/q/Iae91b2322e0c70ccd932060eddafacd06e29ee7f), [b/409808510](https://issuetracker.google.com/issues/409808510))

### Version 1.5.0-alpha06

February 26, 2025

`androidx.camera:camera-*:1.5.0-alpha06` is released. Version 1.5.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/74cbb818c9b3bfa4d09302a96cfde2c21c98d693..824a6d81bccbc4bf5286a94e6476d35825adf198/camera).

**API Changes**

- Added `CameraInfo.getTorchStrengthLevel`, `CameraInfo.getMaxTorchStrengthLevel` and `CameraControl.setTorchStrengthLevel` to allow customizing the torch brightness ([I00878](https://android-review.googlesource.com/#/q/I0087884e137e5a09dc7833980b052a8eae8b85e0))
- A new API `CameraController#setTapToFocusAutoCancelDuration` has been added so that users can control the auto-cancellation behavior for `PreviewView` tap-to-focus events. By default, CameraX cancels the focus events after 5 seconds (i.e. camera focus is reset) and this API allows to modify that duration or disable auto-cancellation altogether. ([Icf59a](https://android-review.googlesource.com/#/q/Icf59ac81f40cd7dd73ff431f9211d6bf0fbbaf82))
- `FLASH_STATE_READY` has been renamed to `NOT_FIRED` and the other `FlashState` constant names are simplified for better readability. ([I8771d](https://android-review.googlesource.com/#/q/I8771d1f6be4f7144de7605e3c07261011e1d4864))
- Exposed Low Light Boost API. Devices running Android 15 or higher can provide support for low-light boost. This feature can automatically adjust the brightness of the preview, video or image analysis streams in low-light conditions. Applications can use the new API to: 1. Use `CameraInfo#isLowLightBoostSupported` to check the feature availability. 2. Use `CameraControl#enableLowLightBoostAsync` to enable the mode when the devices can support it. 3. Use `CameraInfo#getLowLightBoostState` to monitor the low-light boost state. ([I937ed](https://android-review.googlesource.com/#/q/I937edfd0f715525acc2811c68314deeb40663f22))
- Add compat classes to allow faster non-camera2 querying in camera-feature-combination-query. ([Ie97ee](https://android-review.googlesource.com/#/q/Ie97eeb6c1d5ec3b0369025d45c222c2f3a6fae6c))
- For `CameraController` tap-to-focus events, a new API `getTapToFocusInfoState()` now exposes the corresponding tap position too by returning a `LiveData` of `TapToFocusInfo` class while the previous `LiveData<Integer>` returning `getTapToFocusState()` API is deprecated in favor of the new API. ([I238d2](https://android-review.googlesource.com/#/q/I238d26e82c2723c67e2b3add7a7110a5e5a4974f))

**Bug Fixes**

- Fixed the issue that preview stabilization is not applied when preview stabilization is enabled with Extensions. ([I24ad7](https://android-review.googlesource.com/#/q/I24ad778f67fa1f30a3b45eef2682b80d89f3fbde))
- Fixed `CameraController` focus state event not resetting back to `TAP_TO_FOCUS_NOT_STARTED` when CameraX auto-cancels a focus event which happens after 5 seconds by default. ([I31954](https://android-review.googlesource.com/#/q/I31954d6bc1d6a136157dc2294d6b08b6f6224db7))
- Fixed preview freeze when using Zero Shutter Lag (ZSL) after multiple captures due to unreleased image resources. ([Ic3c2a](https://android-review.googlesource.com/q/Ic3c2a0c5c413ddace554bccbea22072bf82c501c))
- Fixed issues that on some devices UHD videos are red tint when pipeline involves `OpenGL`. ([Idcedc](https://android-review.googlesource.com/q/Idcedcb4dde38dc37f83006105a1f92b55979c60e))

### Version 1.5.0-alpha05

January 15, 2025

`androidx.camera:camera-*:1.5.0-alpha05` is released. Version 1.5.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/619c6de87fe3f2c27da0045968f503c1bbd40ef6..74cbb818c9b3bfa4d09302a96cfde2c21c98d693/camera).

**API Changes**

- Add `VideoCapture.getSelectedQuality()` to know the selected Quality based on the `QualitySelector`. ([I70508](https://android-review.googlesource.com/#/q/I7050868dea1f1654386c991d441c25af2e3f1fe4), [b/204288986](https://issuetracker.google.com/issues/204288986))
- When an image capture is invoked with the `ImageCapture.OnImageCapturedCallback` API, the ImageInfo at the returned `ImageProxy` can now be used to know whether flash was fired through the new `ImageInfo.getFlashState()` API. ([Id2c61](https://android-review.googlesource.com/#/q/Id2c61f898acee6e75acded80fc41872cd0edf764), [b/380527406](https://issuetracker.google.com/issues/380527406))
- Added `OUTPUT_IMAGE_FORMAT_NV21` output format support for `ImageAnalysis`. ([I484ab](https://android-review.googlesource.com/#/q/I484ab2358aae7522e8f62115e636cb2d5036e64e))
- Remove the experimental annotation of the `featurecombinationquery` artifact ([I4427f](https://android-review.googlesource.com/#/q/I4427f3d99be11e8f1823c7be81096590d363d595))
- Adjust the zoom ratio range allowed for `CameraControl` by Extensions-specific characteristics when an extensions mode is enabled. ([I85af1](https://android-review.googlesource.com/#/q/I85af16007a5bcbe7eef66b581a135bc4c8eb193c))

**Bug Fixes**

- Upgraded `compileSdk` as 35 for using Android 15 related API. Apps using CameraX libraries will also need to upgrade their `compileSdk` config setting. ([Ic80cd](https://android-review.googlesource.com/#/q/Ic80cd9e0eea7adc72419a22c1ab5035e7fc5fb61))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Idc6c6](https://android-review.googlesource.com/#/q/Idc6c6616bb5cd6f37b6640eb03e99c215f67fc1b), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.5.0-alpha04

December 11, 2024

`androidx.camera:camera-*:1.5.0-alpha04` is released. Version 1.5.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd1d1e576a596e4748da989ef803d52d4e2e772b..619c6de87fe3f2c27da0045968f503c1bbd40ef6/camera).

**API Changes**

- Exposed `ImageCapture.Builder#setOutputFormat` and `ImageCaptureCapabilities#getSupportedOutputFormats` as stable APIs ([Ieb04a](https://android-review.googlesource.com/#/q/Ieb04ae19a2d9289dbb5c4a0218d2dc47c9bd561a))
- Add `VideoCapture.getResolutionInfo()` to get the resolution information when a `VideoCapture` is bound to a Lifecycle. ([Icb478](https://android-review.googlesource.com/#/q/Icb4782146409acbf28a19918759faeb42239149a))
- Exposed `PreviewView.getScreenFlash` and `PreviewView.setScreenFlashOverlayColor` as stable APIs. ([I74fee](https://android-review.googlesource.com/#/q/I74fee2c58f24ebd6b95c7581ac57092904b51ff0))

**Bug Fixes**

- Fixed capture failure issue on Vivo 1610 device while taking picture with flash in the dark. ([I366f4](https://android-review.googlesource.com/#/q/I366f436b016993c9db549b44b0900583be5aa0b0))
- Fixed torch unexpectedly turning off after image capture in Redmi Note 6 Pro. ([I2e0e8](https://android-review.googlesource.com/#/q/I2e0e86fd6e91f276254c77b811b2fa17edf2f18f), [b/377144569](https://issuetracker.google.com/issues/377144569))
- Fixed an issue on Pixel Android 15 devices where NIGHT mode in Extensions failed to capture still images until the camera focused on a nearby object. ([I228d4](https://android-review.googlesource.com/#/q/I228d453abe88bebcefc7bc159443f301956669c6))
- Fixed the still image capture malfunction issue when extensions are enabled and `VideoCapture` is bound together. ([I5c745](https://android-review.googlesource.com/#/q/I5c745f6934f4dfb2e918e5ce03c721bb461a5a2a))
- Enabled `UltraHDR` still image capture support for Extensions if the device can support it. ([I48300](https://android-review.googlesource.com/#/q/I48300ce4590ec5302dde81aed8f80b629cd9b4c9))
- Fixed flash timing issue for flash capture with `CameraEffect` targeting image captures on TCL devices. ([I7698c](https://android-review.googlesource.com/#/q/I7698ca79e03a4cf6540ea28e2c3c3f86e317e710))

### Version 1.5.0-alpha03

October 30, 2024

`androidx.camera:camera-*:1.5.0-alpha03` is released. Version 1.5.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c5333e2c7d785dd314479d930f3927d8ea9b7bcf..fd1d1e576a596e4748da989ef803d52d4e2e772b/camera).

**API Changes**

- Add output format APIs for RAW and RAW + JPEG `ImageCapture`, the device capability check is exposed in `ImageCaptureCapabilities#getSupportedOutputFormats`. The `OUTPUT_FORMAT_RAW` is to capture RAW image, which is Adobe DNG format and `OUTPUT_FORMAT_RAW_JPEG` is to simultaneously capture RAW and JPEG images. The new `ImageCapture#takePicture` API is used for simultaneous image capture, it needs to provide two `OutputFileOptions`, the first one is for RAW image and the second one is for JPEG image. ([Ib0f3d](https://android-review.googlesource.com/#/q/Ib0f3d6195b59efd878bf6d4b4c8f14d92bb94e6e))

**Bug Fixes**

- Fixed preview and video under-exposure issue on TCL devices when `VideoCapture` is enabled. ([Id7a64](https://android-review.googlesource.com/#/q/Id7a64a83ed74ff2f189cd315ede03c090ff818a0))
- Fixed the issue where invoking `startFocusMetering` with `PreviewView.getMeteringPointFactory` doesn't get the correct sensor coordinates when an effect is enabled or when 4 use cases are bound (stream-sharing). ([I916c5](https://android-review.googlesource.com/#/q/I916c55d371a2c2e7de798b21080318591f099561), [b/345993685](https://issuetracker.google.com/issues/345993685))
- Fixed the `VideoRecordEvent.Finalize.ERROR_INSUFFICIENT_STORAGE` event is not triggered when recording a video and there is insufficient storage space available. ([I35779](https://android-review.googlesource.com/#/q/I35779fd7edbbeaff77cdf917eea1b377dc3e2151), [b/356399842](https://issuetracker.google.com/issues/356399842))

### Version 1.5.0-alpha02

October 2, 2024

`androidx.camera:camera-*:1.5.0-alpha02` is released. Version 1.5.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/445fd4cb2234969b1622d272e143642886cf13eb..c5333e2c7d785dd314479d930f3927d8ea9b7bcf/camera).

**New Features**

- New APIs for querying camera features supported by the device. For example, checking if HDR and 60FPS can be enabled at the same time. It includes 2 artifacts: camera-feature-combination-query and camera-feature-combination-query-play-services. This is a compatible version of camera2's `CameraManager#getCameraDeviceSetup#isSessionConfigurationSupported` API with additional data provided by Google Play Service.

**Bug Fixes**

- Fixed `Preview/VideoCapture` target frame rate issue on LEGACY level devices. The target frame rate set via the `setTargetFrameRate` or `Camera2Interop` API was always overwritten to the value provided by the `AeFpsRangeLegacyQuirk`. With this fix, CameraX library will respect the value set via the `setTargetFrameRate` or `Camera2Interop` API. ([Ie2d32](https://android-review.googlesource.com/#/q/Ie2d328b78f6b7af70b804758fc79742752e84338))
- Added flash/torch/3A functionalities for image captures with `CameraEffect`. The image captures with `CameraEffect` should now have the same pre-capture and post-capture processings (e.g. flash trigger, 3A convergence etc. when applicable) as image capture without any `CameraEffect`. ([I5ff30](https://android-review.googlesource.com/#/q/I5ff30cdc38094de0a97889a9564372652a4b8922))
- Excluded problematic output sizes for `ImageAnalysis` on Samsung SM-A057G device. When `ImageAnalysis` uses a resolution larger or equal to 1920x1440, it will cause black preview issue. Applied `ExcludedSupportedSizesQuirk` to the SM-A057G device to avoid the issue. ([I63dfe](https://android-review.googlesource.com/#/q/I63dfe9a224f74e6960c8b5bfeace1372cff8b22c), [b/365877975](https://issuetracker.google.com/issues/365877975))
- Fixed `Preview/VideoCapture` target frame rate issue when stream sharing mechanism is enabled internally to share a stream to `Preview` and `VideoCapture`. ([I4fdac](https://android-review.googlesource.com/#/q/I4fdaccbc5601d67d62ce24737b814c717574c047))
- Enabled the workaround to fix the incorrect JPEG image metadata issue on Samsung S10e and S10+ devices. With the fix, CameraX can successfully save the JPEG image, or correct Bitmap objects can be returned when calling the `ImageProxy.toBitmap()` function on these devices if the incorrect JPEG image metadata issue happens. ([Iae493](https://android-review.googlesource.com/#/q/Iae493350efac5696dd9c210522015c1d3799a6eb), [b/356428987](https://issuetracker.google.com/issues/356428987))
- Disabled extensions for Samsung A52s' back camera whose id is 0, because native crashes might happen when capturing HDR images and configuring capture sessions might fail for the BOKEH or FACE_RETOUCH modes. ([I03ec9](https://android-review.googlesource.com/#/q/I03ec9ce16ff100c38eb9286cb391c4e32ee5c728), [b/364152642](https://issuetracker.google.com/issues/364152642))
- Fixed the `VideoRecordEvent.Finalize.ERROR_INSUFFICIENT_STORAGE` event is not triggered when recording a video and there is insufficient storage space available. ([Ia5b4f](https://android-review.googlesource.com/#/q/Ia5b4f435e387b690fa4e7bb13e747d636a2d72b0), [b/356399842](https://issuetracker.google.com/issues/356399842))
- Fixed issue where second video recording attempt fails on Oppo A5 (CPH1931). ([I181d6](https://android-review.googlesource.com/#/q/I181d6208ffafabfadd014ebe8b65c256c698bdd8))

### Version 1.5.0-alpha01

September 4, 2024

`androidx.camera:camera-*:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/95c324b1e196c9c30883678f411faafdf32f2a63..445fd4cb2234969b1622d272e143642886cf13eb/camera).

**New Features**

- A new artifact, `camera-compose` is released for the CameraX Viewfinder Compose Adapter which displays a Preview stream from a CameraX `SurfaceRequest` from `camera-core`. ([I8666e](https://android-review.googlesource.com/#/q/I8666ee2a6f6d2a411aa1f3018fa359b238d549dc))
- Added a new composable, `CameraXViewfinder`, which acts as an idiomatic composable that adapts CameraX `SurfaceRequest`s for the composable `Viewfinder`. ([I4770f](https://android-review.googlesource.com/#/q/I4770ff29c3e8081a2a9c6eac6ab90be252f8ac80))

**API Changes**

- Provide API to set composition settings for dual concurrent camera video capture. The settings include alpha value for blending, offset in x, y coordinates, scale of the width and height of camera frame display window. The offset, width and height are specified in normalized device coordinates. ([Ia2b8a](https://android-review.googlesource.com/#/q/Ia2b8a80a6d27e52a616c1918a2be1aadbf399daf))
- Exposed `CameraProvider.getCameraInfo` to be a formal API. ([I901cd](https://android-review.googlesource.com/#/q/I901cdfb5995ae3aee21404592137c29688209f78))
- Added API `PendingRecording.withAudioEnabled(boolean initialMuted)` to control the initial mute state. ([I635c3](https://android-review.googlesource.com/#/q/I635c37a3a703425c58932acbc08051f994484709), [b/354829267](https://issuetracker.google.com/issues/354829267))

**Bug Fixes**

- Fixed the crash when `bindToLifecycle` is invoked with a destroyed `LifecycleOwner`. ([I6e6d8](https://android-review.googlesource.com/#/q/I6e6d8f0c545730987587c318bae92998c06f6947))
- Fixed Preview is black screen in front camera while binding with `VideoCapture` on Motorola Edge 20 Fusion. ([I1fe88](https://android-review.googlesource.com/#/q/I1fe882c14201aeb293081b23dcaa27b64602c608))
- Optimized the configuration for detecting zoom gestures in `PreviewView` to improve smoothness. ([I04ffc](https://android-review.googlesource.com/#/q/I04ffc20b7ab0771919ad1703457b751c2b120e9c))

## Camera Version 1.4

### Version 1.4.2

March 26, 2025

`androidx.camera:camera-*:1.4.2` is released. Version 1.4.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c9954e6e2f9aa65ca4ad551687ef31543e13282b..3e0a72e3dcd61a1dee78ce48b9092c6b3267b331/camera).

**Bug Fixes**

- Fixed preview freeze issue when using `ImageAnalysis` with another stream that uses `TEMPLATE_RECORD` on Samsung Galaxy M55. ([Ic1a6a](https://android-review.googlesource.com/#/q/Ic1a6a019c1525f30d7b863f732d421e36e5c978c), [b/395822788](https://issuetracker.google.com/issues/395822788))

### Version 1.4.1

December 11, 2024

`androidx.camera:camera-*:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1d117856fc5cbc071d379fe5ec64846d40bf584b..c9954e6e2f9aa65ca4ad551687ef31543e13282b/camera).

**Bug Fixes**

- Fixed an issue on Pixel Android 15 devices where NIGHT mode in Extensions failed to capture still images until the camera focused on a nearby object. ([I228d4](https://android-review.googlesource.com/#/q/I228d453abe88bebcefc7bc159443f301956669c6))
- Fixed the `ImageCapture#takePicture` malfunction issue when extensions are enabled and `VideoCapture` is bound together. ([I5c745](https://android-review.googlesource.com/#/q/I5c745f6934f4dfb2e918e5ce03c721bb461a5a2a))

### Version 1.4.0

October 30, 2024

`androidx.camera:camera-*:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2318e19e0b920cc26f3af34e3a5cd5ad500ee0d0..1d117856fc5cbc071d379fe5ec64846d40bf584b/camera).

**Important changes since 1.3.0**

CameraX 1.4.0 is packed with exciting updates! Here's a summary:

Headline Feature: 10-bit HDR:

- Capture stunning HDR photos and videos with ease.
- Supports HLG and 10-bit HEVC encoding.
- Enjoy 10-bit HDR preview and query device capabilities.
- Works with `UltraHDR` images and HDR video on a growing range of devices.

Other Cool Features:

- Kotlin Extensions: Added `takePicture` and `awaitInstance` suspend functions.
- Real-time Effects: Apply effects like watermarks and object highlighting.
- CameraController API: New controls for video capture configuration.
- Preview Stabilization: Query device capability and enable stabilization.
- VideoCapture Enhancements: Finer control over quality and access to higher resolutions.
- CameraX Extensions Integration: Seamless integration with `VideoCapture` and new `ImageCapture` features.
- Shutter Sound API: Easily check regional shutter sound requirements.
- Screen Flash: Improved low-light photos for front-facing cameras.
- Camera Extensions Metadata APIs: Supporting APIs for adjusting extensions strength and get notification of current Extensions mode in `ExtensionMode#AUTO`. You can find more bug fixes in our [Beta](https://groups.google.com/a/android.com/g/camerax-developers/c/FpZXLanBuXk/m/ydvBgIVKBAAJ) and [RC](https://groups.google.com/a/android.com/g/camerax-developers/c/z_gu1riqZkg/m/hz2uifBABAAJ) announcements.

### Version 1.4.0-rc04

October 16, 2024

`androidx.camera:camera-*:1.4.0-rc04` is released. Version 1.4.0-rc04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4fcfa6081d83cbb9dbe5c35952e0e1ac775241f8..2318e19e0b920cc26f3af34e3a5cd5ad500ee0d0/camera).

**Bug Fixes**

- Fixed the issue where invoking `startFocusMetering` with `PreviewView.getMeteringPointFactory` doesn't get the correct sensor coordinates when an effect is enabled or when 4 use cases are bound (stream-sharing). ([I916c5](https://android-review.googlesource.com/#/q/I916c55d371a2c2e7de798b21080318591f099561), [b/345993685](https://issuetracker.google.com/issues/345993685))

### Version 1.4.0-rc03

October 2, 2024

`androidx.camera:camera-*:1.4.0-rc03` is released. Version 1.4.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c07d74a301cf15e34cb31fa985d045e0ef630f0b..4fcfa6081d83cbb9dbe5c35952e0e1ac775241f8/camera).

**Bug Fixes**

- Added flash/torch/3A functionalities for image captures with `CameraEffect`. The image captures with `CameraEffect` should now have the same pre-capture and post-capture processings (e.g. flash trigger, 3A convergence etc. when applicable) as image capture without any `CameraEffect`. ([I5ff30](https://android-review.googlesource.com/#/q/I5ff30cdc38094de0a97889a9564372652a4b8922))
- Optimized the pinch-to-zoom smoothness in `PreviewView` ([I04ffc](https://android-review.googlesource.com/#/q/I04ffc20b7ab0771919ad1703457b751c2b120e9c))
- Decouple Ultra HDR from 10-bit output capability, as Ultra HDR support no longer requires devices to have 10-bit output capability. ([I96ff2](https://android-review.googlesource.com/#/q/I96ff225f84b642ad2ea688960793c1f9407d016b), [I0c3b3](https://android-review.googlesource.com/#/q/I0c3b3f80671bd919b5cc60b9e29a3afb0eb19785))

### Version 1.4.0-rc02

September 18, 2024

`androidx.camera:camera-*:1.4.0-rc02` is released. Version 1.4.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/95c324b1e196c9c30883678f411faafdf32f2a63..c07d74a301cf15e34cb31fa985d045e0ef630f0b/camera).

**Bug Fixes**

- Fixed the crash when `bindToLifecycle` is invoked with a destroyed `LifecycleOwner`. ([I6e6d8](https://android-review.googlesource.com/#/q/I6e6d8f0c545730987587c318bae92998c06f6947))
- Added visibility animation in `ScreenFlashView` for `ScreenFlash#apply` which also fixes bugs due to brightness change completing asynchronously after some time. ([I37cdb](https://android-review.googlesource.com/#/q/I37cdb7231ad80dd670124692571cb2d2cb0fb5e9))
- Improved zooming smoothness by overriding zoom settings in the framework on supported devices.

### Version 1.4.0-rc01

August 7, 2024

`androidx.camera:camera-*:1.4.0-rc01` is released. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/97ce0972adadb34722870dfe4d0a6bb0540d13e7..95c324b1e196c9c30883678f411faafdf32f2a63/camera).

**New Features**

- Added experimental `CameraInfo.getCameraInfo` to provide specific camera information without the need of binding use cases to the camera. ([I550d1](https://android-review.googlesource.com/#/q/I550d1855dc32a47deaad7e26284987eccf81be71))

**API Changes**

- Added `PreviewView.getScreenFlash` and `PreviewView.setScreenFlashOverlayColor` APIs for cases where `ScreenFlashView` is not explicitly added. ([I43945](https://android-review.googlesource.com/#/q/I439457f23bde793514933f0d250d288a95fd82a1))

**Bug Fixes**

- Fixed exposure and color tint issues when image captured with flash enabled under low light with VideoCapture use case bound. ([Ic9814](https://android-review.googlesource.com/#/q/Ic9814d1e52fd1d7384fb663b793a7010c34ee41c))
- Fix the issue that interrupting a `takePicture` request with Extensions enabled could fail to get result and the next `takePicture` request might no longer work. ([Iae78f](https://android-review.googlesource.com/#/q/Iae78f85a429b5e72354debb9201daa130784a1ab))
- Fixed a memory leakage issue that happens when Extensions are enabled. ([Iab276](https://android-review.googlesource.com/#/q/Iab2762d4abf3f4779a3065e78deb3856de7de81b))
- Resolved a CameraX extensions malfunction on devices like Pixel 7/8 and Samsung Galaxy S24 series. The issue, stemming from a `Camera2OutputConfigImpl` conversion problem in release mode, surfaced after upgrading AGP to 8.5.1 and enabling minification. ([I99598](https://android-review.googlesource.com/#/q/I9959873ee37f47e07aa617b92859d2a5cadc7830), [b/354824993](https://issuetracker.google.com/issues/354824993))

### Version 1.4.0-beta02

June 12, 2024

`androidx.camera:camera-*:1.4.0-beta02` is released. Version 1.4.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7d2a9b0f7f27c85a187b05044b5fb8f1281a191..97ce0972adadb34722870dfe4d0a6bb0540d13e7/camera).

**API Changes**

- Similar to `VideoCapture`, add `setMirrorMode` for Preview use case. It will support mirror mode ON and OFF for Preview stream via `OutputConfiguration.setMirrorMode` from API 33 and above, for older APIs, it will be no-op. ([I821f4](https://android-review.googlesource.com/#/q/I821f466c4d5851468d02748483a68268e13023e6))

**Bug Fixes**

- Fixed the issue that apps can't take pictures successfully on Samsung Tab A8 when `ImageCapture` selects 1920x1080 under `Preview` + `VideoCapture` + `ImageCapture` `UseCase` combination. ([I5a463](https://android-review.googlesource.com/#/q/I5a463a7d42f5adda71c5ce34e934b93fa9969764), [b/336925549](https://issuetracker.google.com/issues/336925549))
- Fixed persistent recording may fail to continue recording after switching camera. ([Icb0a1](https://android-review.googlesource.com/#/q/Icb0a12559d0f7e6b144ea3f2f498de95ca2d95eb))

### Version 1.4.0-beta01

May 14, 2024

`androidx.camera:camera-*:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7f20a95e69d42bdab1dbae806dd5dee41b86143d..c7d2a9b0f7f27c85a187b05044b5fb8f1281a191/camera).

**API Changes**

- Added `ZoomGestureDetector.ZoomEvent` to encapsulates the states of a zoom gesture. ([I84cdf](https://android-review.googlesource.com/#/q/I84cdfd505443171f9910fb0b3fd40fdaf307796b))

**Bug Fixes**

- Fixed a bug that still capture and tap-to-focus do not use the repeating request FPS/stabilization mode values which may recreate capture session and cause latency issues or Preview freeze in some devices. ([I7dc0b](https://android-review.googlesource.com/#/q/I7dc0b1de12c35acbf08a078973a42512ef1f2b45))
- Fixed a bug where High Resolutions can not be selected when `CameraEffect` is enabled on some devices. (e.g. 4000x3000 on Samsung A32 5G). ([Ie3ed3](https://android-review.googlesource.com/#/q/Ie3ed3a802305628e471d73b4741add0d46ac12ad), [b/337336152](https://issuetracker.google.com/issues/337336152))
- Fixed a crash when taking picture with Preview, `ImageCapture` and `VideoCapture(UHD)` are bound on Pixel 4XL API29. ([I5b288](https://android-review.googlesource.com/#/q/I5b2889572295b1a22d5bc8a98182b7eaf40461d8))
- Support virtual devices: Context passed into `ProcessCameraProvider` will preserve the device ID to ensure the functionality in a virtual device environment. ([I5ba48](https://android-review.googlesource.com/#/q/I5ba48e8b569c11525711a38e5e54906a531e5cae))

### Version 1.4.0-alpha05

April 17, 2024

`androidx.camera:camera-*:1.4.0-alpha05` is released. Version 1.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cc8546da2e453883b157aa38bbd034b8ae5bbac8..7f20a95e69d42bdab1dbae806dd5dee41b86143d/camera).

**New Features**

- Converted `ProcessCameraProvider` into Kotlin implementation. ([I46d4f](https://android-review.googlesource.com/#/q/I46d4fb4e2a7eb8908f952afd5ffb8565d27f8a47))
- Added `ImageCapture.takePicture` suspend functions to allow it to be called in a Kotlin-idiomatic way. ([I920be](https://android-review.googlesource.com/#/q/I920bed9dc547a4e1b78af37f1ba4239793741bb5))

**API Changes**

- Add output format APIs to `ImageCapture`, and add `getSupportedOutputFormats` method to `ImageCaptureCapabilities` for querying device capability. The default output format value is `OUTPUT_FORMAT_JPEG`, which captures SDR images in JPEG format. When the device supports Ultra HDR and the output format is set to `OUTPUT_FORMAT_JPEG_ULTRA_HDR`, CameraX will capture Ultra HDR compressed images using the JPEG/R image format. The format is backwards compatible with SDR JPEG format and supports HDR rendering of content. This means that on older apps or devices, images appear seamlessly as regular JPEG; on apps and devices that have been updated to fully support the format, images appear as HDR. ([I5de50](https://android-review.googlesource.com/#/q/I5de5085906d23a4319d8f795a1d34bfe435d011c))
- Add `PhysicalCameraInfo` in `CameraInfo` to query physical camera information and add physical camera id setter/getter in `CameraSelector` ([Ic5b90](https://android-review.googlesource.com/#/q/Ic5b9021a03fed697df2eec33ef418869015ca0b1))
- Replace `CameraController#COORDINATE_SYSTEM_VIEW_REFERENCED` with `ImageAnalysis#COORDINATE_SYSTEM_VIEW_REFERENCED`. The value of the constant remains the same. This is for consolidating all the constants into one place. ([I890bb](https://android-review.googlesource.com/#/q/I890bb13e2c045393bd7b6e438c0f35a03eefe240))
- New `RetryPolicy` API empowers developers to customize retry behavior for CameraX initialization. ([I36dd2](https://android-review.googlesource.com/#/q/I36dd233d93bced1931cc765a79409a3384035931))
- Enable creation of `ImageCaptureLatencyEstimate` object to assist with testability ([Iaba99](https://android-review.googlesource.com/#/q/Iaba99723592047b8d3a244cd69391e75ef702ef7))
- Add a `ImageAnalysis#COORDINATE_SYSTEM_SENSOR`. When this is used, the `MlKitAnalyzer` returns coordinates in the camera sensor coordinate system. ([I3ec61](https://android-review.googlesource.com/#/q/I3ec61b28688aafb8398b7ddf7aa5f9325fc73a2d))
- Exposed extensions metadata API. New `CameraExtensionsInfo` and `CameraExtensionsControl` interfaces allow applications to monitor and adjust extension strength settings. Applications can obtain the `CameraExtensionsInfo` or `CameraExtensionsControl` instance via the newly added `ExtensionsManager#getCameraExtensionsInfo()` or `ExtensionsManager#getCameraExtensionsControl()` methods. ([I28e1a](https://android-review.googlesource.com/#/q/I28e1ad1ffa814e5c7c21408f6bf3ea121c2e2d2a))
- Added `ProcessCameraProvider.awaitInstance` which is a suspending version of `ProcessCameraProvider.getInstance` ([Ib22b9](https://android-review.googlesource.com/#/q/Ib22b908216f928c9b1be6bc5a61f7cf2592cdabd))
- Add a `PreviewView#getSensorToViewTransform()` API. The Matrix represents the transformation from camera sensor coordinates to the `PreviewView`'s coordinates. This can be used to transform coordinates from one `UseCase` to another. For example, transforming the coordinates of detected objects in `ImageAnalysis` to `PreviewView` overlay. ([I947ab](https://android-review.googlesource.com/#/q/I947ab623ddb63915a3f4dd77222b3aeba8c5b82e))
- Make `camera-viewfinder-core` API more generic so it can be used by `camera-viewfinder` and `camera-viewfinder-compose`. ([I1e295](https://android-review.googlesource.com/#/q/I1e295d7e809802ad710a4c466b2a4720a067760f))
- Add `getSurface` function to `ViewfinderSurfaceRequest`. ([I781a0](https://android-review.googlesource.com/#/q/I781a031ae184bf9a4e1a4d818533358db4ea8687))
- Use `camera-viewfinder-core` in `camera-viewfinder` and deprecate `ViewfinderSurfaceRequest` and `CameraViewfinder`. ([I6198c](https://android-review.googlesource.com/#/q/I6198c02781be9016805daca034386467092ff308))
- Added `ZoomGestureDetector` that interprets scaling gestures specifically configured for pinch-to-zoom activity. ([Ifafbf](https://android-review.googlesource.com/#/q/Ifafbfc2e24759013c3ed856fddba1ed372280c5a))

**Bug Fixes**

- Fixed `ImageAnalysis`' resolution selection issue related to the analyzer default target resolution setting: target resolution was incorrectly kept as 640x480 even if applications has set a different analyzer default resolution setting. If applications encounter this issue (1.3.0 \~ 1.3.2) and can't upgrade to use the newer version releases which contain the solution, directly setting a `ResolutionSelector` with the preferred resolution and a matching `AspectRatioStrategy` to the `ImageAnalysis` `UseCase` can workaround this issue. ([I81f72](https://android-review.googlesource.com/#/q/I81f72a850dcedb664e5b661247991ee4851bdfc6), [b/330091012](https://issuetracker.google.com/issues/330091012))
- Fixed an issue that queued `takePicture` request might fail to run if the current request is failed. ([Ie0801](https://android-review.googlesource.com/#/q/Ie080131d791aeaf6b7459cda3003480a0dc5692a))
- Make the invalid JPEG data check applied to Vivo X60 and X60 Pro devices. This can fix abnormally large image issue on these devices. ([I82247](https://android-review.googlesource.com/#/q/I8224707d5976d8e9a2cb96c54399544fb14699de), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Fixed the incorrect JPEG image metadata issue on Samsung A24 devices. With the fix, CameraX can successfully save the JPEG image, or correct Bitmap objects can be returned when calling the `ImageProxy.toBitmap()` function on Samsung A24 devices. ([I8d6eb](https://android-review.googlesource.com/#/q/I8d6eb3b4cc6f68237248cda566f0b9742f98862d), [b/309005680](https://issuetracker.google.com/issues/309005680))
- Make the invalid JPEG data check applied to all Samsung devices if the captured image is larger than 10 MB. This can fix abnormally large iamge issue on Samsung devices. ([Ic2a65](https://android-review.googlesource.com/#/q/Ic2a65ccdc3eeb75bdf4c70e5c2b96004328422d1), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Removed `ImageAnalysis` support on CameraX Extensions as many OEMs' Extensions implementations don't work with `ImageAnalysis` well and might cause inconsistent issues. ([I2d926](https://android-review.googlesource.com/#/q/I2d9262b3cc2078e351328f315b811a26720f077c))

### Version 1.4.0-alpha04

January 24, 2024

`androidx.camera:camera-*:1.4.0-alpha04` is released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/354ebb67b2265fff0e9169750bcf7341d723a159..cc8546da2e453883b157aa38bbd034b8ae5bbac8/camera)

**New Features**

- New artifact: camera-effects: A library for applying real time effects to CameraX output, including `Preview`, `VideoCapture` and/or `ImageCapture`. This artifact contains OpenGL implementations of the `CameraEffect` API that manipulates the camera output efficiently.
- `OverlayEffect`: for drawing overlays with Android's Canvas API. This allows the app to apply a watermark or highlight detected objects on camera outputs.
- `DynamicRange` APIs for the Preview Use Case: The dynamic range can now be set on the Preview Use Case, independently of the Video Use Case. This allows HDR dynamic ranges such as HLG10 for Preview alone. New APIs are also available in `CameraInfo` to query which dynamic ranges each camera supports.

**API Changes**

- Renamed `ScreenFlashUiCompleter` to `ScreenFlashListener` and moved `ScreenFlashUiCompleter#getExpirationTimeMillis` to `expirationTimeMillis` parameter of `ScreenFlash#apply`. ([I13944](https://android-review.googlesource.com/#/q/I139446df586160ff4c900bd4dd9dc1ec69efaf19))
- New APIs added to allow dynamic range to be set on Preview use case, and to query dynamic ranges supported by each camera. This allows HDR dynamic ranges, such as HLG10, to be used with the Preview use case alone, no longer requiring a `VideoCapture` to be bound at the same time. ([If25e3](https://android-review.googlesource.com/#/q/If25e3f803ef0bb993ce9270bcc36c5647c42af06))
- Renamed `getMirroring()` to `isMirroring()` ([I47063](https://android-review.googlesource.com/#/q/I470630ef430beebcae93ccb32818494358aff337))
- Added Realtime still capture latency estimate support in CameraX. Camera extensions enable applications to use an API that provides an estimate of how long a capture will take. The estimate takes into account the current environment conditions, the camera state and includes the time spent processing multi-frame capture requests along with any additional time for encoding processed buffers if necessary. ([I05c3a](https://android-review.googlesource.com/#/q/I05c3a12013008ada3461542c82da43e045f061c2))
- Renamed `ScreenFlashUiControl` to `ScreenFlash`, `ScreenFlashUiControl#applyScreenFlashUi` to `ScreenFlash#apply`, `ScreenFlashUiControl#clearScreenFlashUi` to `ScreenFlash#clear`, and added `getScreenFlashUiApplyTimeoutSeconds` method instead of exposing `SCREEN_FLASH_UI_APPLY_TIMEOUT_SECONDS` directly. ([Iccdd0](https://android-review.googlesource.com/#/q/Iccdd0f93601b77522ebfa58d05fb399ee61448b3))

**Bug Fixes**

- Fixed a memory leakage that results in activities or fragments not being released when Extensions are enabled ([I14215](https://android-review.googlesource.com/#/q/I142155b2b481007d5a45303e93992459b075d230))
- Fixed the issue where `getZoomRatio` incorrectly returned a decreased value when applying an increasing zoom ratio. ([I4aa0d](https://android-review.googlesource.com/#/q/I4aa0df75c6b6382e1e3f4b7905459acdbc6b4d3c), [b/317543616](https://issuetracker.google.com/issues/317543616))
- `ImageCapture#ScreenFlash#clear` event is invoked immediately when `ImageCapture` is unbound or camera is closed, also fixes some bugs where it is never invoked due to captures in these scenarios not completing properly. ([If99f9](https://android-review.googlesource.com/#/q/If99f98b14712268ec54f1f1f1f9b11d23c68b89f))
- Fixed the crash that happens when lifecycle is stopped before `takePicture` request is completed ([Idf017](https://android-review.googlesource.com/#/q/Idf017ef3ec1400955066433dd8446f94728b8a1a), [b/306202751](https://issuetracker.google.com/issues/306202751))
- Fixed the issue where camera preview becomes black when Extensions are enabled on some devices ([I1ffd0](https://android-review.googlesource.com/#/q/I1ffd01c1f45052caa5bb2a9f8f3d85d07f182e71))
- Fixed incorrect duration of video recording on devices using the Snapdragon 778G SoC. ([If6aa7](https://android-review.googlesource.com/#/q/If6aa766b7438145e957cae1e7b12f800eb84ce87), [b/316057919](https://issuetracker.google.com/issues/316057919))

### Version 1.4.0-alpha03

December 13, 2023

`androidx.camera:camera-*:1.4.0-alpha03` is released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/354ebb67b2265fff0e9169750bcf7341d723a159/camera)

**New Features**

- Added `CameraInfo.mustPlayShutterSound` to provide the information of whether a shutter sound must be played in accordance to regional restrictions. ([Ifda84](https://android-review.googlesource.com/#/q/Ifda84b6930fd5ab0193140d6f60571f92188d4f1))
- Added `OnImageCapturedCallback.onCaptureStarted` and `OnImageSavedCallback.onCaptureStarted` for notifying when the camera has started exposing a frame. It's recommended to play the shutter sound or the shutter animation at this point. ([Ic49b3](https://android-review.googlesource.com/#/q/Ic49b3caf6ef91649a48059e0657e017bbe98edaa))
- Added Screen Flash feature support in CameraX for front camera image capture. CameraX will take care of the framework-side API handling and sync the timing with application's UI changes as required (e.g. AE precapture trigger after app screen color/brightness change). Apps will only need to add their UI side implementations in the `ScreenFlashUiControl` interface provided to CameraX. ([I8ae84](https://android-review.googlesource.com/#/q/I8ae843fc126c173cb9e2658d72c7a04457264183))
- Added Screen Flash feature UI-side implementation support in CameraX. Apps will be able to get a basic `ImageCapture.ScreenFlashUiControl` implementation from `PreviewView` or the newly added `ScreenFlashView` which will add a mono-color overlay view and maximize screen brightness during screen flash photo capture. ([I1810e](https://android-review.googlesource.com/#/q/I1810efc37d35478082e995b2bf4a87b31e56b3fa))

**API Changes**

- Supports new Extensions features(postview and capture process progress): Added `ImageCapture#getImageCaptureCapabilities()` APIs for apps to query the capabilities of the postview and capture process progress callback. Apps can enable the postview using the `ImageCapture.Builder#setPostviewEnabled()`. The postview size can be selected using `ImageCapture.Builder#setPostviewResolutionSelector()`. When invoking `takePicture()`, `onPostviewBitmapAvailable` and `onCaptureProcessProgressed` can be implemented in `OnImageSavedCallback` or `OnImageCapturedCallback` to get the postview and process progress notification if supported. ([I5cd88](https://android-review.googlesource.com/#/q/I5cd88131d689950ee0d50fa63f9b3e2d2e7b06cb))
- APIs for calculate coordinates transformation from sensor to the current buffer, with a flag indicating whether the Surface contains the camera orientation info. ([I59096](https://android-review.googlesource.com/#/q/I59096cca934ee680dc2d57ac52fe2a1a252a29d1))
- Expose the API to query `PreviewCapabitlity` in Preview `UseCase`. ([Ie5b6c](https://android-review.googlesource.com/#/q/Ie5b6c6c5c194fd12e0e6ce1a7eff2f80ad8f1c49))
- Added APIs to support more qualities for `VideoCapture`. `Recorder.Builder#setVideoCapabilitiesSource(int)` can be used with `VIDEO_CAPABILITIES_SOURCE_CODEC_CAPABILITIES` to create a `Recorder` instance which supports more qualities than `VIDEO_CAPABILITIES_SOURCE_CAMCORDER_PROFILE`. A common use case is when the application strives to record UHD video whenever feasible, but the device's `CamcorderProfile` does not include a UHD settings, even though the codec is capable of recording UHD video. ([Iedbe2](https://android-review.googlesource.com/#/q/Iedbe2ae048c09a978b345b23d37ab989c000fd7a), [b/263961771](https://issuetracker.google.com/issues/263961771))
- Add `ImageAnalysis` output format getter/setter to `CameraController`. ([I9a96c](https://android-review.googlesource.com/#/q/I9a96ce6cba5835d6c08fa93b95579853714a6d55), [b/308240643](https://issuetracker.google.com/issues/308240643))

**Bug Fixes**

- From [Camera `1.3.1`](https://developer.android.com/jetpack/androidx/releases/camera#1.3.1): Improved the `ProcessCameraProvider#bindToLifecycle()` performance. The major change is to optimize the process of identifying the most suitable size combinations for `UseCases`. The optimal results vary based on the specific `UseCase` combinations and the number of supported output sizes for the target devices. ([I454f2](https://android-review.googlesource.com/#/q/I454f2ca19be1d77ed737a651676834f6e431e0b7))
- Allow the use of `VideoCapture` when Extensions are enabled. ([I91f32](https://android-review.googlesource.com/#/q/I91f32ebab5ba3d39b851d2c151e823775bdf18b5))
- Fixed large captured JPEG image issue on Samsung A71 and M51 series devices. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have extreme file size. Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I01afc](https://android-review.googlesource.com/#/q/I01afc7e5001f42788a66388f5a66e0858e4dcfd5), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Disable `ImageAnalysis` support on Pixels to avoid the bug on Pixel that returns the non-empty `ImageAnalysis` supported sizes accidentally. ([I7ec31](https://android-review.googlesource.com/#/q/I7ec313868a7d71a50faad6ca5297850a3cc291e6))
- Fixed performance issue where CPU loading and power consumption increased when Extensions are enabled. ([Ibdccb](https://android-review.googlesource.com/#/q/Ibdccbeeba9351f1cd7ae5cb525dc4d56708b11a0))
- Added Snapdragon 480 to the `CameraUseInconsistentTimebaseQuirk`. This fixes an issue on Android 12 for devices using this chipset where the audio in recordings is offset by the amount of time the device is in a suspended state. ([I58010](https://android-review.googlesource.com/#/q/I580100cfa2cd3111e687b8d0515f8f02c50205d7))

### Version 1.4.0-alpha02

October 18, 2023

`androidx.camera:camera-*:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c46c913e821a8f47c1376abbe688af1a9e8558cd..fca6737d0d4b9dda7d8ea4168cf8c85771227653/camera)

**API Changes**

- Rename the API to `setCameraOpenRetryMaxTimeoutInMillisWhileResuming` and rename the argument. ([I72370](https://android-review.googlesource.com/#/q/I7237035a800667b39433164b7b833788686c0b03))
- Adding APIs to query the device capability and enable video/preview stabilization. ([I87544](https://android-review.googlesource.com/#/q/I87544680620842990ce95ac226160126368547a2))
- Provide API to customize the camera open retrying max timeout time. ([I0c642](https://android-review.googlesource.com/#/q/I0c6424622a239c65a1e5687e1843b619b4824b64))
- Released `ProcessCameraProvider.shutdownAsync` as a public testing API to allow process camera provider to be used in test suites which may need to initialize CameraX in different ways in between tests. ([I9eca7](https://android-review.googlesource.com/#/q/I9eca7edd77a7dcb74f28786c830f5c3f5b5bcf22))
- Add APIs for configuring video capture dynamic range, frame rate and mirror mode. ([Ifb8f7](https://android-review.googlesource.com/#/q/Ifb8f76e2f0bbb3235c8735134fe2dcd44f85188c))
- Deprecate `OutputSize` and replace it with `ResolutionSelector`. `ResolutionSelector` is a more comprehensive way to select resolutions, and it's consistent with the camera-core API. ([I93abd](https://android-review.googlesource.com/#/q/I93abdb2472d82de5af890fccdd253d629f9111e7), [b/286801438](https://issuetracker.google.com/issues/286801438))

**Bug Fixes**

- Fixed the black preview issue on Samsung Galaxy S23 Ultra 5G when Extensions Bokeh or Face-Retouch is enabled with `ImageAnalysis` on the rear camera. ([I2e8b1](https://android-review.googlesource.com/#/q/I2e8b1c5bc42da2443299a0d89343bed82249da71))
- Fixed Preview and `VideoCapture` stretched issues on Moto E5 Play. ([73dce2](https://android-review.googlesource.com/#/q/73dce2dd644138870bda6cf61227b8dfd69c02bc))

### Version 1.4.0-alpha01

September 20, 2023

`androidx.camera:camera-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a5d48fc5725f8aac203c2ae3bd24e0e53dafbd4d..c46c913e821a8f47c1376abbe688af1a9e8558cd/camera)

**API Changes**

- Add new API to access audio amplitude information while recording. ([Id4925](https://android-review.googlesource.com/#/q/Id492575f356184b9dbe77b4bc24861be1d64e654))

**Bug Fixes**

- Improve Extensions stability by ensuring that the initialization and deinitialization events are triggered in correct order. ([Ib3b8e](https://android-review.googlesource.com/#/q/Ib3b8e50d7818e659a264a4dc5aa5505486414617))
- Fixed capture session configuration failure for exceeding supported surface combination due to adding extra repeating surface internally. ([Id718c](https://android-review.googlesource.com/#/q/Id718ca7a481564e229e54c7431317f7125877392))
- Fixed large captured JPEG image issue on Vivo S16 device. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have large file size. Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I79505](https://android-review.googlesource.com/#/q/I79505f36e448374847f82eba0696c31b0839ab26), [b/299069235](https://issuetracker.google.com/issues/299069235))
- Fixed the issue that `ImageAnalysis` can't be bound together with `ImageCapture` and Preview when some extension modes are enabled on some devices. The fix will return correct value when apps query the `ImageAnalysis` availability via `ExtensionsManager#isImageAnalysisSupported()`. ([I7d538](https://android-review.googlesource.com/#/q/I7d53885cebd4ea1c9b1aaead0a9c234fbc63f922))
- Update JavaDoc to match behavior. Instead of completes immediately, the `#setZoomRatio`, `#setLinearZoom` and `#enableTorch` wait until camera is ready. Also added information about how to get the maximum FOV with the `#takePicture` API. ([I23588](https://android-review.googlesource.com/#/q/I235883105dce096f094308423c68b3bbf5126868))

## Version 1.3

### Version 1.3.4

June 12, 2024

`androidx.camera:camera-*:1.3.4` is released. Version 1.3.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1fb89fe455e3527cadfdca47bfb353829dba6be4..fc680027273b2ecace66751e7a2f4f97b0ef2430/camera).

**Bug Fixes**

- Fixed the issue where `getZoomRatio` incorrectly returned a decreased value when applying an increasing zoom ratio. ([I4aa0d](https://android-review.googlesource.com/#/q/I4aa0df75c6b6382e1e3f4b7905459acdbc6b4d3c), [b/317543616](https://issuetracker.google.com/issues/317543616))
- Fixed still capture/tap-to-focus not using the repeating request FPS/stabilization mode values which may re-create capture session and cause latency issues or Preview freeze in some devices. ([I7dc0b](https://android-review.googlesource.com/#/q/I7dc0b1de12c35acbf08a078973a42512ef1f2b45))
- Fixed the issue that the frame rate is set to a lower value when calling `setTargetFrameRate` with `FRAME_RATE_RANGE_UNSPECIFIED`. ([I78c61](https://android-review.googlesource.com/#/q/I78c617b40e383d48b117e6ea7d8849847ce906d9))

### Version 1.3.3

April 17, 2024

`androidx.camera:camera-*:1.3.3` is released. Version 1.3.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4b6de18d0b6be6088de2618d7efdd3780003b005..1fb89fe455e3527cadfdca47bfb353829dba6be4/camera).

**Bug Fixes**

- Fixed `ImageAnalysis`' resolution selection issue related to the analyzer default target resolution setting: target resolution was incorrectly kept as 640x480 even if applications has set a different analyzer default resolution setting. If applications encounter this issue (1.3.0 \~ 1.3.2) and can't upgrade to use the newer version releases which contain the solution, directly setting a `ResolutionSelector` with the preferred resolution and a matching `AspectRatioStrategy` to the `ImageAnalysis` UseCase can workaround this issue. ([I81f72](https://android-review.googlesource.com/#/q/I81f72a850dcedb664e5b661247991ee4851bdfc6), [b/330091012](https://issuetracker.google.com/issues/330091012))

### Version 1.3.2

March 6, 2024

`androidx.camera:camera-*:1.3.2` is released. Version 1.3.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/716b8b7a0fb8fd062fd609f8af4f317b46f6f8dc..4b6de18d0b6be6088de2618d7efdd3780003b005/camera).

**Bug Fixes**

- Fixed a JPEG metadata issue on Samsung A24 devices. CameraX now saves images accurately, and the `ImageProxy.toBitmap()` function returns correct Bitmap objects. ([I8d6eb](https://android-review.googlesource.com/#/q/I8d6eb3b4cc6f68237248cda566f0b9742f98862d), [b/309005680](https://issuetracker.google.com/issues/309005680))
- Removed the 9280x6944 resolution option on Redmi Note 9 Pro devices due to issues. ([Ia23da](https://android-review.googlesource.com/#/q/Ia23daa62e7956b687ed86a8334db5e0541e91952))

### Version 1.3.1

December 13, 2023

`androidx.camera:camera-*:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ef36c63f9e8f6ac59ad44c45496c271d6cb2a3cc..ee5fe2aa34dba21365bb402477c32c593ccbecda/camera)

**Bug Fixes**

Improved the `ProcessCameraProvider#bindToLifecycle()` performance. The major change is to optimize the process of identifying the most suitable size combinations for `UseCases`. The optimal results vary based on the specific `UseCase` combinations and the number of supported output sizes for the target devices. ([I454f2](https://android-review.googlesource.com/#/q/I454f2ca19be1d77ed737a651676834f6e431e0b7))

Here are some reference results for various scenarios:

- Four `UseCases`: `Preview` + `ImageCapture` + `ImageAnalysis` + `VideoCapture`

  - Google Pixel 7: Approximately 430 ms to 60 ms
  - Samsung Galaxy S23 Ultra: Approximately 540 ms to 45 ms
  - Samsung A53 5G: Approximately 115 ms to 70 ms
- Three `UseCases`: `Preview` + `ImageCapture` + `ImageAnalysis`

  - Google Pixel 7: Approximately 9 ms to 7 ms
  - Samsung Galaxy S23 Ultra: Approximately 6 ms to 5 ms
  - Samsung A53 5G: Approximately 32 ms to 12 ms
- Added Snapdragon 480 to the `CameraUseInconsistentTimebaseQuirk`. This fixes an issue on Android 12 for devices using this chipset where the audio in recordings is offset by the amount of time the device is in a suspended state. ([I58010](https://android-review.googlesource.com/#/q/I580100cfa2cd3111e687b8d0515f8f02c50205d7))

### Version 1.3.0

October 18, 2023

`androidx.camera:camera-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85bee35bbcfa3c5f457a3ae3da014e0c8eea0a02..ef36c63f9e8f6ac59ad44c45496c271d6cb2a3cc/camera)

**Important changes since 1.2.0**

- Video features including [10-bit HDR](https://developer.android.com/reference/androidx/camera/video/VideoCapture.Builder#setDynamicRange%28androidx.camera.core.DynamicRange%29), [cropping](https://developer.android.com/reference/androidx/camera/core/ViewPort.Builder#Builder%28android.util.Rational,int%29), [mirror/non-mirror](https://developer.android.com/reference/androidx/camera/video/VideoCapture.Builder#setMirrorMode%28int%29), [mute/unmute](https://developer.android.com/reference/androidx/camera/video/Recording#mute%28boolean%29), [set framerate](https://developer.android.com/reference/androidx/camera/video/VideoCapture.Builder#setTargetFrameRate%28android.util.Range%3Cjava.lang.Integer%3E%29), and more.
- [Dual Concurrent Camera](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#getAvailableConcurrentCameraInfos%28%29)
- [Effect library](https://developer.android.com/reference/androidx/camera/core/CameraEffect)
- [Resolution Selector](https://developer.android.com/reference/androidx/camera/core/resolutionselector/ResolutionSelector)
- [Ultra-Wide \& Telescopic camera selection](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getIntrinsicZoomRatio%28%29)
- [Camera switching during video recording](https://developer.android.com/reference/androidx/camera/video/PendingRecording#asPersistentRecording%28%29) (experimental feature)

### Version 1.3.0-rc02

September 20, 2023

`androidx.camera:camera-*:1.3.0-rc02` is released. [Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e2a76338ab0e3f3c8be9b898fbc326c5b0e16711..85bee35bbcfa3c5f457a3ae3da014e0c8eea0a02/camera)

**Bug Fixes**

- Improve Extensions stability by ensuring that the initialization and deinitialization events are triggered in correct order. This fixed some black preview issues when switching Extensions modes or switching cameras. ([Iddaac](https://android-review.googlesource.com/#/q/Iddaac35470273442eff829680dc7bccde87e8519))
- Fixed the issue that `ImageAnalysis` can't be bound together with `ImageCapture` and Preview when some extension modes are enabled on some devices. The fix will return correct value when apps query the `ImageAnalysis` availability via `ExtensionsManager#isImageAnalysisSupported()`. ([I7d538](https://android-review.googlesource.com/#/q/I7d53885cebd4ea1c9b1aaead0a9c234fbc63f922))
- Fixed the issue where the recorded video audio and video were out of sync when mirroring mode was enabled on Xiaomi Poco X3 NFC. ([I20b4c](https://android-review.googlesource.com/q/I20b4cbc879cabf0d33bc449267e30d1aa02fbe0e))

### Version 1.3.0-rc01

August 23, 2023

`androidx.camera:camera-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a5d48fc5725f8aac203c2ae3bd24e0e53dafbd4d..e2a76338ab0e3f3c8be9b898fbc326c5b0e16711/camera)

**API Changes**

- Added `PendingRecording.asPersistentRecording` to allow a recording to continuously record while the `VideoCapture` it's Recorder is attached to is rebound. ([I517c6](https://android-review.googlesource.com/#/q/I517c6ce300cef6c38afcaa4e97792d9694bbffca))

**Bug Fixes**

- Fixed a crash when a stream is shared with both `VideoCapture` and Preview. Also fixed a black screen on LEGACY devices when stream sharing is enabled.
- Fixed large captured JPEG image issue on Samsung S7 (SM-G930T, SM-G930V) series devices. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have large file size. Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I407b0](https://android-review.googlesource.com/#/q/I407b0731d23a749a3cab21d8ed8cb5d52fe0ab0e), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Fixed large captured JPEG image issue on Samsung S22 (SM-S901B, SM-S901B/DS) and S22+ (SM-S906B) series devices. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have large file size about 13MB on S22 SM-S901B/DS device. Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I73be9](https://android-review.googlesource.com/#/q/I73be940494d3d600e6e2cdc99eb1f3814fb8bed2), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Fixed large captured JPEG image issue on Samsung A5, A52, A70 and A72 series devices. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have extreme file size (ex about 32MB or even 96 MB). Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I97c4d](https://android-review.googlesource.com/#/q/I97c4d7745cfbff789e8890a9a04ee735eb84e5ed), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Fixed the native crash when taking pictures with Extensions enabled ([I698f5](https://android-review.googlesource.com/#/q/I698f5739cd3d42243721184c1162f0ba86523e0d))

### Version 1.3.0-beta02

July 26, 2023

`androidx.camera:camera-*:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bef05e5a3f6d09babb620159f75c659bcc7df495..a5d48fc5725f8aac203c2ae3bd24e0e53dafbd4d/camera)

**Bug Fixes**

- Use torch as flash for Pixel 4 and 5 variants to improve capture quality in low light ([I56ff5](https://android-review.googlesource.com/#/q/I56ff5a3af37a4480f734db94c8e763f34dd9cc3b), [b/280221967](https://issuetracker.google.com/issues/280221967))
- Fixed large captured JPEG image issue on Samsung A5 (2017) series devices. The captured JPEG images contain redundant 0's padding data in the JFIF compressed data segment. It causes the captured images to have about 32 MB file size. Those redundant 0's padding data will be removed to make the captured images have normal image file sizes. ([I29837](https://android-review.googlesource.com/#/q/I298373a190ff42cee685a51290ff5e08945e326a), [b/288828159](https://issuetracker.google.com/issues/288828159))
- Fixed retry not triggering properly in case of capture failure in problematic devices mentioned in `CaptureFailedRetryQuirk`. ([I7b589](https://android-review.googlesource.com/#/q/I7b589a19bf5ee8f316c009e6c69dd21b7cf6a0c3))

### Version 1.3.0-beta01

June 21, 2023

`androidx.camera:camera-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/938a593fa34a9c8caac51e9aafa1945da629893b..bef05e5a3f6d09babb620159f75c659bcc7df495/camera)

**API Changes**

- Renamed the `ResolutionSelector.Builder#setHighResolutionEnabledFlag(int)` function name to `setAllowedResolutionMode` and renamed the `ResolutionSelector#HIGH_RESOLUTION_FLAG_OFF`/`ON` constants to `PREFER_CAPTURE_RATE_OVER_HIGHER_RESOLUTION`/`PREFER_HIGHER_RESOLUTION_OVER_CAPTURE_RATE`. ([If84e8](https://android-review.googlesource.com/#/q/If84e83d81be81de313ecd6064151d48408860018))
- Removed deprecated API `ImageAnalysis.setTargetRotationDegrees(int)`, `ImageCapture.setTargetRotationDegrees(int)` and `VideoCapture.setTargetRotationDegrees(int)`. ([Id8e77](https://android-review.googlesource.com/#/q/Id8e7741d6baf94e87919a0f3e8352bc723cfd113))
- The `DynamicRange` class respresent the dynamic range of images. This can be used to select High Dynamic Range formats as the output of `VideoCapture` through `VideoCapture.Builder#setDynamicRange()`. ([Ib0377](https://android-review.googlesource.com/#/q/Ib03770371433647f98a3e47d4a9c9a8083e348a8))
- Added an `isImageAnalysisSupported` API to the `ExtensionsManager` which apps can determine if an `ImageAnalysis` use case can be bound along with Preview and `ImageCapture` when Extensions are enabled. ([I1bc63](https://android-review.googlesource.com/#/q/I1bc6361c6fcb32f4ece0b616ebac1059b1ecfe76))
- The new `VideoCapabilities` class obtained from the `Recorder` can be used to query supported dynamic ranges and qualities for video recording on the device. `QualitySelector`'s `getSupportedQualities()` and `isQualitySupported()` methods are being deprecated. Please use `VideoCapabilities`'s `getSupportedQualities()` and `isQualitySupported()` methods instead. ([I04014](https://android-review.googlesource.com/#/q/I04014e9d4fbeae8007e72d41effb40f5b7b9ad38))
- `CameraController#setVideoCaptureTargetQuality()` is renamed to `setVideoCaptureQualitySelector` and takes argument `QualitySelector`, which provides more flexibility for video quality setup. `CameraController#getVideoCaptureTargetQuality()` is changed to `getVideoCaptureQualitySelector` accordingly. ([I520ed](https://android-review.googlesource.com/#/q/I520ed903bcb66e0bafa889b1a3038cde2dbd3412))
- Removed the experimental annotation for video features. The video features are now stable. ([I1a113](https://android-review.googlesource.com/#/q/I1a113f55d90924ca4728f9d1fbb5600d94a8e2e9))

**Bug Fixes**

- Use torch as flash on Samsung SM-A320 models to improve the speed and the captured image quality in low light. ([I6a022](https://android-review.googlesource.com/#/q/I6a022547c5a39c1783b9c1b8d9938a7d6494f482), [b/286190938](https://issuetracker.google.com/issues/286190938))
- Add `ImageFormat.JPEG` format support for `ImageProxy.toBitmap()`. If the JPEG byte array cannot be decoded, an `UnsupportedOperationException` will be thrown. ([I81958](https://android-review.googlesource.com/#/q/I819581bc0cb6591133b1861d89e8ee67a8e7fd86), [b/282057603](https://issuetracker.google.com/issues/282057603))

### Version 1.3.0-alpha07

May 24, 2023

`androidx.camera:camera-*:1.3.0-alpha07` is released. [Version 1.3.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e9eaaebb4ca9643ffda665848653708aa7d97ba4..938a593fa34a9c8caac51e9aafa1945da629893b/camera)

**New Features**

- The new `VideoCapture.Builder# setTargetFrameRate(Range)` API allows video recordings to be captured at other frame rates besides the device default. The available frame rates for recordings can be queried through the new `CameraInfo#getSupportedFrameRates()` API.

**API Changes**

- Renamed `ResolutionSelector#HIGH_RESOLUTION_FLAG_OFF`/`ON` constants to `ALLOWED_RESOLUTIONS_NORMAL`/`SLOW` and renamed the builder `setHighResolutionEnabledFlag` function name to `setAllowedResolutionMode`. ([Iae817](https://android-review.googlesource.com/#/q/Iae8175364782aecb55e04936bbba4e27a3834124))
- `CameraInfo#getSupportedFrameRateRanges()` now returns a `Set` rather than a `List` to better represent that the ranges are unordered. ([I02f43](https://android-review.googlesource.com/#/q/I02f43e7bc0e67bf0d9e6b028ae4a3167e2e0c3e6))
- Add an error listener to `CameraEffect` to handle unrecoverable errors ([Ice471](https://android-review.googlesource.com/#/q/Ice47156c364e628483ab6df46bdeceedd3c27be9))
- Add public constructor in `ResolutionInfo` for better testability ([If6d1c](https://android-review.googlesource.com/#/q/If6d1cedbe4ba6050a12d1425b362971027e797aa))
- Provided an API `UseCase.snapToSurfaceRotation(int)` to replace usage of `setTargetRotationDegrees` and deprecate API `ImageAnalysis.setTargetRotationDegrees(int)`, `ImageCapture.setTargetRotationDegrees(int)` and `VideoCapture.setTargetRotationDegrees(int)`. ([Ia9010](https://android-review.googlesource.com/#/q/Ia9010e1289e66fb23edb8981a70b1537d9e56666))
- Added new API `Preview#getTargetFrameRate` and `Preview.Builder#setTargetFrameRate` to be able to set and retrieve target frame rate for Preview use case ([If4f22](https://android-review.googlesource.com/#/q/If4f2263848b8dec0e689d002af9b65bca6ebd380))
- `VideoRecordEvent.Finalize` will now complete with error code `ERROR_RECORDING_GARBAGE_COLLECTED` when the `Recording` object is stopped due to garbage collection. ([Iba974](https://android-review.googlesource.com/#/q/Iba974398be221d6588f542efdb049fc04b6e5259))

**Bug Fixes**

- Fixed `NullPointerException` when the cached output sizes in `StreamConfigurationMapCompat` are null. ([Idf124](https://android-review.googlesource.com/#/q/Idf124b2054ca12fa58d66b53e4206ceb49493782), [b/282025204](https://issuetracker.google.com/issues/282025204))
- Fixed the issue that `Preview.setSurfaceProvider(null)` doesn't pause the preview in Extensions ([Ia903e](https://android-review.googlesource.com/#/q/Ia903e412176f12fdf38ab7d20c7e29c75d884dbd))
- Fixed an issue where `ConcurrentModificationException` is thrown during camera opening when `VideoCapture` is bound. ([Ic8ac4](https://android-review.googlesource.com/#/q/Ic8ac4a339a45f9f09d0ae0cb20fd4bef19d27cbf))

### Version 1.3.0-alpha06

April 19, 2023

`androidx.camera:camera-*:1.3.0-alpha06` is released. [Version 1.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..e9eaaebb4ca9643ffda665848653708aa7d97ba4/camera)

**New Features**

- Concurrent camera is a new feature introduced from Android 11, which supports simultaneous streaming of camera devices, for example, it allows a device to have both the front and back cameras operating at the same time. CameraX currently only supports dual concurrent cameras, which allows two cameras operating at the same time, with at most two {@link UseCase}s bound for each. The max resolution is 720p or 1440p, more details in the following link, see [CameraManager#getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds())
- Introducing the new `ResolutionSelector` API which covers the following features:
  - Applications can specify aspect ratio and resolution strategies to select the best resolution for their needs.
  - All sizes and aspect ratio parameters are expressed in the coordinates of the camera device sensor.
  - Applications can implement a custom resolution filter to arrange the supported sizes in the desired order.
  - Applications can also enable high resolution capture to obtain higher resolution images. However, please note that using a high resolution may result in slower capture times.
  - Added `VideoCapture` mirroring APIs. Videos recorded by `VideoCapture` are not mirrored by default. However, the camera preview is mirrored on the front camera by default. `VideoCapture` mirroring APIs make it possible to align to the camera preview when using the front camera. There are three `MirrorMode`, `OFF`, `ON` and `ON_FRONT_ONLY`. To align to the camera preview, it is recommended to use `ON_FRONT_ONLY` which means that mirroring is not enabled for the rear camera but is enabled for the front camera.

**API Changes**

- Exposed new `ResolutionSelector` API. Applications can specify aspect ratio and resolution strategies with fallback rules or a custom resolution filter to get the desired results. Applications can specify a flag to enable high resolution capture. This will allow CameraX to select higher resolutions when taking photos or videos. However, please note that using a high resolution may result in slower capture times. ([Ibed95](https://android-review.googlesource.com/#/q/Ibed95cf9fce530954803d5ab3115fac6711199ab))
- The FPS ranges supported by the AE algorithm can now be queried via `CameraInfo#getSupportedFrameRateRanges()`. ([Iaa67f](https://android-review.googlesource.com/#/q/Iaa67fb277cc50aa8fef25fc807208a294f20c095))
- Consolidate the names of all frame rate methods into using 'FrameRate'. Correct the javadoc mistake in `VideoCapture#getTargetFrameRate()` ([I83304](https://android-review.googlesource.com/#/q/I8330476ec33c05ba85ef10fb127e4fc592bb716d))
- Deprecated the legacy `setTargetAspectRatio` and `setTargetResolution` API. Please use the new `ResolutionSelector` API instead. ([I542c3](https://android-review.googlesource.com/#/q/I542c387ecdfdd96e9c4a2a7610b7d1a2af691b73))
- Added public APIs for concurrent dual camera, including
  1. `List<List<CameraInfo>> getAvailableConcurrentCameraInfos()`
  2. `ConcurrentCamera bindToLifecycle(@NonNull ConcurrentCameraConfig concurrentCameraConfig)`
  3. `boolean isConcurrentCameraModeOn()` and `ConcurrentCameraConfig`, `SingleCameraConfig` and `ConcurrentCamera` ([Iab1c1](https://android-review.googlesource.com/#/q/Iab1c1e3fa5225f4234c007fb70fbe351407f2bcb))
- Make `ImageProcessor.Response#getOutputImage` NonNull ([Ib9c60](https://android-review.googlesource.com/#/q/Ib9c600dff44dec65b80e7688313d3bd5f98c74d8))
- Added `VideoCapture` mirroring APIs, including `VideoCapture.Builder.setMirrorMode(int)` and `VideoCapture.getMirrorMode()`. The APIs are useful for applications require the video recording to be consistent with common camera preview behavior, i.e. the rear camera preview is not mirrored but the front camera preview is mirrored. ([I713b6](https://android-review.googlesource.com/#/q/I713b6afc589947296d5f415694b7022c66ad0d66), [b/194634656](https://issuetracker.google.com/issues/194634656))
- Add `setTargetFrameRate()` API in the `VideoCapture.Builder` and `getTargetFramerate()` API in `VideoCapture` ([I109d4](https://android-review.googlesource.com/#/q/I109d43a5c4ee38abb3c5fe03366166025aef9048))
- Make `SurfaceOutput` extending Closable and hide S`urfaceOutput.Event`'s public constructor. ([I60ea8](https://android-review.googlesource.com/#/q/I60ea838610a55f3d142677654f99c4130623811d))
- Added `Recording.mute` to dynamically mute or unmute an in-processing recording. `RecordingStats` will contain `AudioStats.AUDIO_STATE_MUTED` when the in-processing recording is muted explicitly. ([Ie17fc](https://android-review.googlesource.com/#/q/Ie17fce8d0054cb3f33845b0a26f3ea1c2858bc11))
- Made `#setEffects()` parameter non-null. Add a `#clearEffects()` API for clearing effects. The app should call `#clearEffects()` to remove effects. ([I4b4d9](https://android-review.googlesource.com/#/q/I4b4d9d3b6db48dbc9ad65d464ffe460d2fc5dbf0))
- Add a second constructor for `ViewfinderSurfaceRequest.Builder` to take a builder for copy constructor ([I621a7](https://android-review.googlesource.com/#/q/I621a7551adc879473d4774cf6c2179f373b6987d))

**Bug Fixes**

- Fixed the issue where apps invoking Extensions API could crash when closing the camera ([Ib27e5](https://android-review.googlesource.com/#/q/Ib27e5420c0e313f69259960fbe116dd5fb722623))
- Fixed an issue where `VideoCapture` could not work with the front camera on some devices. For example, on Samsung Galaxy S23 and Xiaomi 2107113SG. ([Ibec7e](https://android-review.googlesource.com/#/q/Ibec7ea9696314f3f7ba303a2d0053c58762f72a1), [b/270656244](https://issuetracker.google.com/issues/270656244))
- Fixed the issue where taking pictures using File in the external storage public folder will always fail in Android 10 or above. Please note that in Android 10, taking pictures using File in the external storage public folder also requires setting `requestLegacyExternalStorage` to true in application tag. ([I11b2c](https://android-review.googlesource.com/#/q/I11b2ce0e3038d7b20a69fc06bdb3f446bc9ad73b))
- Fixed a `RejectedExecutionException` crash in `DefaultSurfaceProcessor`. The crash could happen when `VideoCapture` is bound and the activity is paused. ([Idb46a](https://android-review.googlesource.com/#/q/Idb46a3791eafb3ca009a04333064d3501de1b2f5), [b/273713906](https://issuetracker.google.com/issues/273713906))

### Version 1.3.0-alpha05

March 22, 2023

`androidx.camera:camera-*:1.3.0-alpha05` is released. [Version 1.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e29b9d5011a682544cb10226575971c514437eae..5e7d256f82fbafb6d059ab7b18fddd87c7531553/camera)

**API Changes**

- Added `VideoCapture` rotation APIs, including `VideoCapture.Builder.setTargetRotation(int)`, `VideoCapture.setTargetRotation(int)`, `VideoCapture.setTargetRotationDegrees(int)` and `VideoCapture.getTargetRotation()`. The APIs are useful for applications that lock the device orientation. `ImageCapture.setTargetRotationDegrees(int)` and `ImageAnalysis.setTargetRotationDegrees(int)` are also added. ([Id3ffe](https://android-review.googlesource.com/#/q/Id3ffe7d8e640523b35b7777bbd39ad4fe214ea02), [b/205242781](https://issuetracker.google.com/issues/205242781))
- Allow `VIDEO_CAPTURE` and `PREVIEW|VIDEO_CAPTURE` as effects target. Effects that targets `VIDEO_CAPTURE` will be applied to the `VideoCapture` UseCase; Effects that targets `PREVIEW|VIDEO_CAPTURE` will be applied to a shared stream before copying to Preview and `VideoCapture` stream. ([Iee6f3](https://android-review.googlesource.com/#/q/Iee6f318490525a0d0d18c8a5228a315041960abf))

**Bug Fixes**

- From [Camera `1.2.2`](https://developer.android.com/jetpack/androidx/releases/camera#1.2.2): Fixed the issue where CameraX Extensions don't work properly when proguard is enabled on some devices such as Pixel ([I90aa2](https://android-review.googlesource.com/#/q/I90aa210540cc985c49816d8ae74bda526cccbbbe))
- Fixed a `PreviewView` bug that if the app handles screen orientation itself. the preview might become distorted upon rotation. This only happens on certain devices. It can be reproduced on Pixel a4, Pixel 5, and Pixel 6a. ([I14340](https://android-review.googlesource.com/#/q/I14340cc9790f22c70717217f8f1d9fdfe338dfeb), [b/223488673](https://issuetracker.google.com/issues/223488673))

### Version 1.3.0-alpha04

February 22, 2023

`androidx.camera:camera-*:1.3.0-alpha04` is released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ff35d3c81caf7392850e60f0410a04265fd95b80..e29b9d5011a682544cb10226575971c514437eae/camera)

**New Features**

A new feature to support previously unsupported Surface combinations by sharing one stream to multiple UseCases.

- Previously, when binding "Preview, VideoCapture, ImageAnalysis" on camera hardware level FULL and below, or binding "Preview, VideoCapture, ImageCapture" on hardware level LEGACY, CameraX throws `IllegalArgumentException`.
- The new behavior is that the bindings will work without throwing exceptions. Instead, CameraX uses OpenGL to copy a shared stream to both Preview and VideoCapture.
- As the cost of the buffer copy, the app may see an increase in latency and power consumption.

**API Changes**

- Add API to convert `ImageProxy` to `Bitmap`. The supported `ImageProxy` format is `ImageFormat.YUV_420_888` and `PixelFormat.RGBA_8888`. If the format is invalid, `IllegalArgumentException` will be thrown. ([Ic7110](https://android-review.googlesource.com/#/q/Ic7110b128b568320fc27408d7f00c8031d339729))
- Add `CoroutineCameraViewfinder` to support configuring viewfinder using suspending functions in Kotlin. ([I657bc](https://android-review.googlesource.com/#/q/I657bc25a2908414c44a700829f1706988c0c89ea))
- Add new public constructor for `ViewfinderSurfaceRequest`. It provides the flexibility when user cannot provide `CameraCharacteristics`. ([Ie6549](https://android-review.googlesource.com/#/q/Ie65492a882efe2a17d5fcb70cee9e1b1d4cc9e31))

**Bug Fixes**

- Fixed the Extensions crash that happens on some Samsung devices when pausing/resuming the app too quickly ([Iaca26](https://android-review.googlesource.com/#/q/Iaca262a499d7e8e72c5072ea7063943dd291b4f2))

### Version 1.3.0-alpha03

January 25, 2023

`androidx.camera:camera-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2c96666b2344cae1cd643af2eba5371be4b576d6..ff35d3c81caf7392850e60f0410a04265fd95b80/camera)

**API Changes**

- Added `CameraInfo.getIntrinsicZoomRatio` to provide angle of view information relative to the default camera. ([Ib300c](https://android-review.googlesource.com/#/q/Ib300cedf8ee42577230f84cb21173b280212b025))
- Added `CameraInfo.getLensFacing` to provide lens facing information. Added `CameraSelector#LENS_FACING_EXTERNAL` as an experimental feature for selecting external cameras. ([Icaf3e](https://android-review.googlesource.com/#/q/Icaf3eb12e2c9a003295fd6ca8bbb10d2e20c7858))
- Add `#setEffect()` to `CameraController` that allows adding effects to camera output. ([I1d21f](https://android-review.googlesource.com/#/q/I1d21f39630a5c334e2605c0b1b4866eaec35a011))
- Add `invalidate()` method to `SurfaceRequest`. The Surface provider can notify that the previously provided surface is no longer valid. ([Idc649](https://android-review.googlesource.com/#/q/Idc649eabf476d7f667d5aa613f6be03f1815d2e8))
- Add a `ImageProcessor` API. This interface is for inject post-processing effects into the `ImageCapture` pipeline. ([I575c6](https://android-review.googlesource.com/#/q/I575c62c264ff447ba6ffa9988bd0e81014ed45a4))
- Added API `Recorder.Builder.setAspectRatio()` which can be combined with `QualitySelector` to support more video resolutions. ([I8a082](https://android-review.googlesource.com/#/q/I8a082872c3404068a0cadc8d27692a9f27e35ef6))
- Added `Recorder.Builder#setTargetVideoEncodingBitRate` to set Target Video Encoding `BitRate` and `Recorder#getTargetVideoEncodingBitRate` to get Target Video Encoding BitRate. ([I5984d](https://android-review.googlesource.com/#/q/I5984de8c85b7ee08ad7422564669ce35fb96cfa7))

**Bug Fixes**

- Fixed `ImageCapture` failed when there is no flash unit and flash mode is on. ([I9e8b4](https://android-review.googlesource.com/#/q/I9e8b433c6a2696a363c06d109877a4df2f90ca6a), [b/263391112](https://issuetracker.google.com/issues/263391112))
- Fixed JPEG image corruption issue if writing Exif location data on some Samsung Android 12 devices. ([Ib7086](https://android-review.googlesource.com/#/q/Ib70862aa6e654f06b9358e3f92bbb98c86cb9caf), [b/263747161](https://issuetracker.google.com/issues/263747161), [b/263289024](https://issuetracker.google.com/issues/263289024))
- when setting torch/zoom prior before camera initialization compelets, e.g. calling `CameraController#enableTorch`, the pending action is cached and submitted once the initialization compeltes. ([I11e92](https://android-review.googlesource.com/#/q/I11e926246983a760b0e65652abe89c67f6434cff), [b/264157663](https://issuetracker.google.com/issues/264157663))

### Version 1.3.0-alpha02

December 7, 2022

`androidx.camera:camera-*:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3296a1dd8beca331583a4f3c2550d7aed2d306a4..2c96666b2344cae1cd643af2eba5371be4b576d6/camera)

**API Changes**

- add a new API for applying post-processing effect to Preview output. ([Ic17d5](https://android-review.googlesource.com/#/q/Ic17d53c89e7f03d9fc051334cba789209eb4d4ee))
- Renamed `OutputOptions.getDurationLimit` to `OutputOptions.getDurationLimitMillis` and `OutputOptions.setDurationLimit` to `OutputOptions.setDurationLimitMillis`. ([I91f0c](https://android-review.googlesource.com/#/q/I91f0c94066e5605cd031718f9cd547c1b427d775))
- Add `AudioConfig` class to handle the audio related setting while recording video. The `@RequiresPermission` annotation is moved from `startRecording` functions to `AudioConfig` to avoid unnecessary permission requests for the cases that audio is not needed. ([I28755](https://android-review.googlesource.com/#/q/I28755ca547aa91ee5d4de3440ab9e691c9a856a7))
- Remove Metadata, `OnVideoSavedCallback`, `OutputFileOptions` and `OutputFileResults` classes that are no longer used after applying the new video capture API. ([I38cd8](https://android-review.googlesource.com/#/q/I38cd8bfb206ef7383a366dd6ac81d3e6c533baf4))
- Apply the new video capture API. The `getVideoCaptureTargetSize` and `setVideoCaptureTargetSize` methods are replaced with the `getVideoCaptureTargetQuality` and the `setVideoCaptureTargetQuality` methods accordingly, as `setTargetResolution` is no longer supported. ([I2a1d5](https://android-review.googlesource.com/#/q/I2a1d597eb4d42346803da392d27a99235d258723))

**Bug Fixes**

- Remove deprecated `core.VideoCapture` API. ([I531e0](https://android-review.googlesource.com/#/q/I531e05b46e93020a825c1e2092b46585cf2a87be))
- Fixed the issue that the `onError` callback is not called when taking pictures without the storage permission.([I936db](https://android-review.googlesource.com/#/q/I936db35eede424d889f08ad8fb64fe779ee524ea), [b/244807669](https://issuetracker.google.com/issues/244807669))
- Improve camera extensions quality and reliability. Camera extensions are disabled on Motorola devices using Camera Extensions v1.1.0 and older due to issues with Bokeh support, image capture, and preview not resuming. ([Id3ce3](https://android-review.googlesource.com/#/q/Id3ce3d3652d09ea81cc678d0eb143d43d416bd45))
- Fixed native crash when video cropping via `ViewPort` is enabled on legacy devices. ([I16b8a](https://android-review.googlesource.com/#/q/I16b8aca645a9d336cf222ed7916c45e20130334a), [b/251357665](https://issuetracker.google.com/issues/251357665))

### Version 1.3.0-alpha01

November 9, 2022

`androidx.camera:camera-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3296a1dd8beca331583a4f3c2550d7aed2d306a4/camera)

**New Features**

- `Camera-viewfinder` has been published officially. `Camera-viewfinder` provides a base viewfinder widget that can display the camera feed for Camera2. Please check the [sample code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:camera/integration-tests/viewfindertestapp/src/main/java/androidx/camera/integration/viewfinder/CameraViewfinderFoldableFragment.kt;l=97?q=CameraViewfinder) for an example.

**API Changes**

- Added `OutputOptions.setDurationLimit` to allow setting of video duration limit. The recording will be automatically finalized when exceeding the specified duration limit. ([I902a0](https://android-review.googlesource.com/#/q/I902a049293775b7cda22c794163c1e4465863375))
- Add video recording audio error state `AudioStats.AUDIO_STATE_SOURCE_ERROR`. Sent when audio source setup fails or some error occurs. ([I37410](https://android-review.googlesource.com/#/q/I37410c5834d9b0084cf8410f2456502860013307))

**Bug Fixes**

- Add quirk to allow some problematic devices to retry capture once when encountering capture failures. ([Id4795](https://android-review.googlesource.com/#/q/Id4795aa8c42f475b10257716adf267636809ee57))
- Fix `PreviewView` `SurfaceView` implementation black screen issue on `ViewPager2`. As part of the fix, `PreviewView` will reuse its `SurfaceView` if the requested resolution is not changed. ([Ib3f27](https://android-review.googlesource.com/#/q/Ib3f27c45c8ad1f9fc837454961a27087fe2f38ff))
- Support video cropping (WYSIWYG feature) when `ViewPort` or `CameraController` API is used. ([Ifbba8](https://android-review.googlesource.com/#/q/Ifbba8358a6cdf8562621e67eb96360cc1b567e3f), [b/201085351](https://issuetracker.google.com/issues/201085351))
- Fixed video captured with front camera fails to record on Huawei P40 lite. ([I87c57](https://android-review.googlesource.com/#/q/I87c578a04e7a0318046da9a3a44bab5792007c88), [b/250807400](https://issuetracker.google.com/issues/250807400))

## Version 1.2

### Version 1.2.3

May 24, 2023

`androidx.camera:camera-*:1.2.3` is released. [Version 1.2.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e57dde4dad04cd1bcbf83e50fe7e2bcfdc13651e..59c948b1519dcf5a7fdb970909d4cdf1126d9067/camera)

**Bug Fixes**

- Fixed an issue where `VideoCapture` could not work with the front camera on some devices. For example, on Samsung Galaxy S23 and Xiaomi 2107113SG. ([Ibec7e](https://android-review.googlesource.com/#/q/Ibec7ea9696314f3f7ba303a2d0053c58762f72a1), [b/270656244](https://issuetracker.google.com/issues/270656244))

### Version 1.2.2

March 22, 2023

`androidx.camera:camera-*:1.2.2` is released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4a3edaf2c76267e85b5f30b707eb7851c5b1257..e57dde4dad04cd1bcbf83e50fe7e2bcfdc13651e/camera)

**Bug Fixes**

- Fixed the issue where CameraX Extensions don't work properly when proguard is enabled on some devices such as Pixel ([I90aa2](https://android-review.googlesource.com/#/q/I90aa210540cc985c49816d8ae74bda526cccbbbe))

### Version 1.2.1

January 25, 2023

`androidx.camera:camera-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/05a044e1a19ef44742449bb296cc7520dd109e35..d4a3edaf2c76267e85b5f30b707eb7851c5b1257/camera)

**Bug Fixes**

- Fix JPEG image corruption issue if writing Exif location data on some Samsung Android 12 devices. ([b/263289024](https://developer.android.com/issuetracker.google.com/issues/263289024))

### Version 1.2.0

December 7, 2022

`androidx.camera:camera-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4492a75904152396b00e333181677981b0e28fd0..05a044e1a19ef44742449bb296cc7520dd109e35/camera)

**Important changes since 1.1.0**

- New library camera-mlkit-vision. Easily integrate CameraX with many MLKit features, including barcode scanning, face detection, text detection, etc. Added `MLKitAnalyzer` as new APIs.
- New experimental Zero-Shutter Lag API. Optimizes capture pipeline to have better latency while keeping good image quality. When the capture mode is set to `CAPTURE_MODE_ZERO_SHUTTER_LAG`, the latency between the shutter button is clicked and the picture is taken is expected to be minimized, compared with other capture modes. On devices that don't support `ZERO_SHUTTER_LAG`, it'll fallback to `CAPTURE_MODE_MINIMIZE_LATENCY`.
- Deprecate `android.camera.core.VideoCapture`.
- Added `setStreamUseCase()` as a public `Camera2Interop` API.
- Added API level requirement for `setOutputImageRotationEnabled`.
- Renamed `ImageAnalysis.Analyzer#getTargetResolutionOverride()` to `ImageAnalysis.Analyzer#getDefaultTargetResolution()`.
- Added API for setting location metadata to the saved video.
- Fixed low framerate when using `VideoCapture` and Preview use cases with 16:9 aspect ratio
- Fixed the black preview issue that happens when BOKEH extension is enabled on some Samsung devices and the user switches the cameras.
- Fixed Samsung J7 Prime (SM-G610M) and J7 (SM-J710MN) `Preview/VideoCapture` stretched issue on API level 27 devices.
- Disabled the workaround to flip the AF region horizontally of front cameras on Samsung Android T since the issue was fixed

### Version 1.2.0-rc01

October 24, 2022

`androidx.camera:camera-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52096c49378ea748c1b11b54c04c19c8d1e571c6..4492a75904152396b00e333181677981b0e28fd0/camera)

**API Changes**

- Add `setStreamUseCase` API for `OutputConfiguration`. User can specify the Stream Use Case for the stream session, overrding CameraX's internal logics to choose Stream Use Case in order to optimize according to their need. ([Ib1a95](https://android-review.googlesource.com/#/q/Ib1a95b50619e5e710370d2d3fde4fe8a7761fb68))

**Bug Fixes**

- Fixed Samsung J7 Prime (SM-G610M) and J7 (SM-J710MN) `Preview/VideoCapture` stretched issue on API level 27 devices. Resolution 1920x1080 causes the `Preview/VideoCapture` images to be stretched. Added workaround to not select the 1920x1080 resolution for Preview or `VideoCapture` to avoid the image stretched problem. ([I0e04e](https://android-review.googlesource.com/#/q/I0e04ea85b3aea9962f6befa25b8fd5297e764b1f))
- Fixed low framerate when using `VideoCapture` and Preview use cases with 16:9 aspect ratio on some Huawei devices. ([If8c88](https://android-review.googlesource.com/#/q/If8c8824d923cefd368d24bf27cedc58b0ecccebb), [b/223643510](https://issuetracker.google.com/issues/223643510))
- Fixed camera open failure when Preview's `SurfaceProvider` is not set. As part of the fix, Preview with no `SurfaceProvider` set will now not be configured into the camera capture session. ([I99681](https://android-review.googlesource.com/#/q/I9968195c104b6de86a51a11288bf891b299f9aea))

### Version 1.2.0-beta02

September 21, 2022

`androidx.camera:camera-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7646e249f2982cf69f134e6b007af38eb7214158..52096c49378ea748c1b11b54c04c19c8d1e571c6/camera)

**API Changes**

- Add API level requirement for `setOutputImageRotationEnabled` ([I26e3e](https://android-review.googlesource.com/#/q/I26e3e939c0d4662573840d378b802e68141b8283), [b/240993561](https://issuetracker.google.com/issues/240993561))

**Bug Fixes**

- Disabled the workaround to flip the AF region horizontally of front cameras on Samsung Android T since the issue was fixed. ([I05f69](https://android-review.googlesource.com/#/q/I05f69db031ab59765976733a070677f197d0c21c))
- Fixed the black preview issue that happens when `BOKEH` extension is enabled on some Samsung devices and user switches the cameras. ([If6168](https://android-review.googlesource.com/#/q/If616822527f8b5274a285c341fdee6b5b8e80242))

### Version 1.2.0-beta01

August 24, 2022

`androidx.camera:camera-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe372724601dcfca420a9ce428d4fbae39a07264..7646e249f2982cf69f134e6b007af38eb7214158/camera)

**New Features**

- New library `camera-mlkit-vision`. Easily integrate CameraX with many MLKit features, including barcode scanning, face detection, text detection, etc. Please find the sample code [here](https://github.com/androidx/androidx/blob/androidx-main/camera/integration-tests/viewtestapp/src/main/java/androidx/camera/integration/view/MlKitFragment.kt).
- New experimental [Zero-Shutter Lag API](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_ZERO_SHUTTER_LAG). Optimizes capture pipeline to have better latency while keeping good image quality. When the capture mode is set to CAPTURE_MODE_ZERO_SHUTTER_LAG, the latency between the shutter button is clicked and the picture is taken is expected to be minimized, compared with other capture modes. On devices that don't support ZERO_SHUTTER_LAG, it'll fallback to CAPTURE_MODE_MINIMIZE_LATENCY.
- Made `ImageAnalysis.Analyzer` and `MLKitAnalyzer` as official APIs.
- Exposed API for setting location metadata to the saved video.
- Rename `ImageAnalysis.Analyzer#getTargetResolutionOverride()` to `ImageAnalysis.Analyzer#getDefaultTargetResolution()`.

**Bug Fixes**

- Fixed Alps k61v1_basic_ref image capture issue. The captured JPEG images from HAL have incorrect Exif metadata. The Exif metadata doesn't have the 0xffd9 or 0xffda tag to make `ExifInterface` correctly parse the attributes. Capturing the images in YUV format and then compressing them to JPEG output images to workaround this issue. ([I45abb](https://android-review.googlesource.com/#/q/I45abb731dc2408db0bb5df7f466e946f7325fc6f))

### Version 1.2.0-alpha04

July 27, 2022

`androidx.camera:camera-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b4d156f56a79b410967a0d3c33aa4f6de430f770..fe372724601dcfca420a9ce428d4fbae39a07264/camera)

**API Changes**

- Rename `ImageAnalysis.Analyzer#getTargetResolutionOverride()` to `ImageAnalysis.Analyzer#getDefaultTargetResolution()`. The behavior is also changed so that the value returned by this method can be overridden by the value of `ImageAnalysis#setTargetResolution()`. ([If1d36](https://android-review.googlesource.com/#/q/If1d36af8df968d06c0192ca985c8764c9fb25231))
- Exposed API for setting location metadata to the saved video. An `android.location.Location` object can be set via new API `androidx.camera.video.OutputOptions.Builder.setLocation(Location)`. ([I313a0](https://android-review.googlesource.com/#/q/I313a013445776ed730d6f98f57113e4998306e86), [b/204197544](https://issuetracker.google.com/issues/204197544))

**Bug Fixes**

- Fix the issue to take picture with unbind preview ([Ie70b6](https://android-review.googlesource.com/#/q/Ie70b6c269a1142e664eab5166acbb0f1788271c1), [b/235119898](https://issuetracker.google.com/issues/235119898))
- Fixed crash in `Recorder` when attempting to record while audio source is unavailable. ([I9f652](https://android-review.googlesource.com/#/q/I9f65246918979299458759a45e290a3dc44904fe))

### Version 1.2.0-alpha03

June 29, 2022

`androidx.camera:camera-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cf759a67ed7e4305c6e6cecac2070a5759bcf0cc..b4d156f56a79b410967a0d3c33aa4f6de430f770/camera)

**API Changes**

- Removed the experimental annotation for `ImageAnalysis.Analyzer` and `MLKitAnalyzer`. ([I0ff22](https://android-review.googlesource.com/#/q/I0ff22e15401255677fc9f53ca6a9f1eea4ed378a))

**Bug Fixes**

- Added auto focus default timeout 5000ms that will complete the AF part with `isFocusSuccessful` false if the `FocusMeteringAction` is not cancelled and the AF part is not converged in the duration. ([Ibc2e3](https://android-review.googlesource.com/#/q/Ibc2e3839383f483e929a2ba8a0310df3c5e82d60))
- Fix the issue to take picture with unbind preview ([I1d3a2](https://android-review.googlesource.com/#/q/I1d3a2ac7a96e6692c7e3a939cac6e313311f3fc4), [b/235119898](https://issuetracker.google.com/issues/235119898))
- Enabled advanced extender implementation and update the CameraX support extensions-interface version to 1.2 ([I92256](https://android-review.googlesource.com/#/q/I92256bc6a260654f8f984ddd8fa5ebf50935ef77))

### Version 1.2.0-alpha02

June 1, 2022

`androidx.camera:camera-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7529bbe53a1c354c3787cfd67a666e1c8c341be0..cf759a67ed7e4305c6e6cecac2070a5759bcf0cc/camera)

**New Features**

- Expose CameraX Zero-Shutter Lag API as experimental.

**API Changes**

- Add new capture mode `CAPTURE_MODE_ZERO_SHUTTER_LAG` in `ImageCapture` and add `isZslSupported` in `CameraInfo` to query the device capability. `CAPTURE_MODE_ZERO_SHUTTER_LAG` mode is aiming to provide the minimum latency for instant capture. It is implemented based on a ring buffer, which caches intermediate capture results for later reprocessing when the user presses buttons to take pictures. If {@link VideoCapture} is bound or flash mode is not OFF or OEM Extension is ON, this mode will be disabled automatically. ([I9ae74](https://android-review.googlesource.com/#/q/I9ae74de91ce38e607af4d6b7b65bc4f7e88217c9))
- Add `ImageAnalysis.getBackgroundExecutor()` method ([Icc945](https://android-review.googlesource.com/#/q/Icc94540065c82f97bbc2cd9699b543b01a8e0f06))

**Bug Fixes**

- Fixed `ImageCapture` takePicture method turns torch off on the reported devices. ([Ib5eb5](https://android-review.googlesource.com/#/q/Ib5eb52dd4d54dc193013f0296ae62121f5480fcd), [b/228272227](https://issuetracker.google.com/issues/228272227))
- Fixed a bug where `AssertionError` not being handled when getting the `CONTROL_ZOOM_RATIO_RANGE` characteristic.([/Ia248a](https://android-review.googlesource.com/#/q/Ia248ae5580b9d4a0949f4448ccbafcedd1ba7b9b), [b/231701345](https://issuetracker.google.com/231701345))

### Version 1.2.0-alpha01

May 18, 2022

`androidx.camera:camera-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6946e183ec360b11e53fb5a43ea1880dbb9e1b0a..7529bbe53a1c354c3787cfd67a666e1c8c341be0/camera)

**New Features**

- New library camera-mlkit-vision is launched

**Bug Fixes**

- Fixed `QualitySelector` fails to record a UHD video when a fallback strategy is enabled. The issue happens when `VideoCapture` is bound with `ImageCapture` and Preview on a FULL or higher hardware level camera device. A fallback strategy of `QualitySelector` causes `VideoCapture` incorrectly to get a FHD resolution. UHD resolution is actually supported for this use case combination and should be adopted. ([I0e788](https://android-review.googlesource.com/#/q/I0e788060512feef5fa934d7f35374da218ffe8e8), [b/230651237](https://issuetracker.google.com/issues/230651237))
- Fixed `NullPointerException` on `ImageCapture.takePicture()`. ([I92366](https://android-review.googlesource.com/#/q/I92366821320e183ca9ba4c6468325a686e6f9720), [b/230454568](https://issuetracker.google.com/issues/230454568), [b/229766155](https://issuetracker.google.com/issues/229766155))
- Fix async pause behavior of `androidx.camera.video.Recorder` ([Ia8ce8](https://android-review.googlesource.com/#/q/Ia8ce8c70381988220194b4bed439a88a45c9156a))

## Camera-Camera2, Camera-Core, Camera-Lifecycle, \& Camera-Video Version 1.1.0

### Version 1.1.0

June 29, 2022

`androidx.camera:camera-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/23746944e4ade5ba70e6d8e5f2bf4b543c99ea94..f066cfcb8ff63f32d0300623bf25da6baa10031e/camera)

**Important changes since 1.0.0**

- Landed View, Extension and Video Capture libraries as their first RC version. From 1.1.0-beta01, all CameraX libraries will align the same version number. This will help developers track versions much easier and reduce the complexity of large version compatibility matrices.
- Introduced new public APIs and features which including:
- Add the official camera-video library to support video capture use cases.
- YUV to RGB conversion and rotation capability (`ImageAnalysis.Builder.setOutputImageRotationEnabled` and `setOutputImageFormat`)
- Support multi-window mode by allowing CameraX applications to resume the camera when the camera is interrupted by another app and focus is back.
- Ensures CameraX works well in foldable devices by fixing some preview issues.
- Added a `CameraState` API that will be exposed through CameraInfo.
- Added an API `ProcessCameraProvider.getAvailableCameraInfos()` to directly retrieve information about the available cameras
- Output JPEG format for `ImageCapture#OnImageCapturedCallback` when Extensions are enabled.
- Added a API `isFocusMeteringSupported` in `CameraInfo` which allows applications to check if the given `FocusMeteringAction` is supported on current camera or not.
- Exposed `getResolutionInfo` API to provide the resolution information for Preview, `ImageCapture` and `ImageAnalysis`.
- Added a new API `ImageCapture.Builder#setJpegQuality` to allow changing the output JPEG image compression quality when taking pictures.
- Added `CameraSelector#filter` to the public API to filter a list of `CameraInfos` based on a `CameraSelector`.
- Added `Camera2CameraControl.clearCaptureRequestOptions` for clearing the existing capture request options.
- Added an experimental API for using `CameraController` with external image processing libraries. e.g. MLKit
- Added experimental API `CameraInfo#getCameraSelector()` which returns a `CameraSelector` unique to its camera
- Promoted several experimental APIs to formal public APIs
- Replaced annotation `@Experimental` with `@RequiresOptIn` to experimental APIs. For calling experimental APIs, use androidx.annotation.OptIn instead of deprecated androidx.annotation.experimental.UseExperimental.
- Promoted the following experimental APIs to official APIs: `CameraXConfig.Builder#setAvailableCamerasLimiter()`, `CameraXConfig.Builder#setMinimumLoggingLevel()`, `CameraXconfig.Builder#setSchedulerHandler()`, `CameraXConfig#getAvailableCamerasLimiter()`, `CameraXConfig#getMinimumLoggingLevel()`, `CameraXConfig#getCameraExecutor()`, `CameraXConfig#getSchedulerHandler()`,
- `@ExperimentalCameraFilter` APIs
- experimental exposure compensation APIs.
- Promoted the experimental `UseCaseGroup` API for camera-core, camera-lifecycle and camera-video. Added `ViewPort#getLayoutDirection`, `ViewPort.Builder#setLayoutDirection` and `ViewPort.Builder#setScaleType` for customizing viewport.
- Promoted the `ExperimentalUseCaseGroupLifecycle` to formal public APIs.
- Changes to the existing APIs
- `Renamed MediaStoreOutputOptions.getCollection` to `MediaStoreOutputOptions.getCollectionUri`.
- `ActiveRecording` has been renamed to "Recording" to reduce verbosity.
- Changed `QualitySelector` creator API to a list-based API

**Bug Fixes**

- Fixed `YuvToJpegProcessor` `EOFException` issue when extension mode is enabled and `ImageCapture#CAPTURE_MODE_MAX_QUALITY` mode is set.
- Fixed codec configuration failed due to video recording is closing
- Fixed stretched preview/video aspect ratio when recording at FHD
- Fixed audio/video out of sync after pause and resume on some devices
- Fixed the issue where flash is triggered during tap-to-focus (`startFocusAndMetering`) when flash mode is auto or always_on in low-light environment.

### Version 1.1.0-rc02

June 1, 2022

`androidx.camera:camera-*:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6946e183ec360b11e53fb5a43ea1880dbb9e1b0a..23746944e4ade5ba70e6d8e5f2bf4b543c99ea94/camera)

**Bug Fixes**

- Fixed `NullPointerException` on `ImageCapture.takePicture()`. ([I92366](https://android-review.googlesource.com/#/q/I92366821320e183ca9ba4c6468325a686e6f9720), [b/230454568](https://issuetracker.google.com/issues/230454568), [b/229766155](https://issuetracker.google.com/issues/229766155))
- Fixed a bug where `AssertionError` not being handled when getting the `CONTROL_ZOOM_RATIO_RANGE` characteristic. ([Ia248a](https://android-review.googlesource.com/#/q/Ia248ae5580b9d4a0949f4448ccbafcedd1ba7b9b), [b/231701345](https://issuetracker.google.com/231701345))

### Version 1.1.0-rc01

May 11, 2022

`androidx.camera:camera-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86c9b1e60c382a866990a04dd1250d436372891f..6946e183ec360b11e53fb5a43ea1880dbb9e1b0a/camera)

**New Features**

- Release the first RC version for camera-video, camera-view, and camera-extension

**Bug Fixes**

- Fixed an issue where the video codec wasn't released when `VideoCapture<Recorder>` was unbound, causing subsequent uses of `VideoCapture<Recorder>` to fail on recording with `MediaCodec.CodecException`, especially on API 21-22 devices. ([Ie7f68](https://android-review.googlesource.com/#/q/Ie7f684425cc8ea826b8ebbaf426a6c852cc413d1))
- Fix captured images of `CameraExtensionsActivity` do not be deleted in `ImageCaptureTest`

### Version 1.1.0-beta03

April 6, 2022

`androidx.camera:camera-*:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/43a214c72ffc3093ee9c3d7c340ad3a57ed4289b..86c9b1e60c382a866990a04dd1250d436372891f/camera)

**API Changes**

- Made `CaptureRequestOptions` constructor restricted. ([I261b6](https://android-review.googlesource.com/#/q/I261b65a7851ad2c73ad59bd5028e28cf6b8f008d))
- Added an experimental API for using `CameraController` with external image processing libraries. e.g. MLKit ([I4ea71](https://android-review.googlesource.com/#/q/I4ea71fb8112a13c16dbc79873267b7714e94c6ec))

**Bug Fixes**

- Fixed the issue that preview becomes sideway in `PreviewView` when activity is not restarted after rotating devices in multi-window. ([I1ea36](https://android-review.googlesource.com/#/q/I1ea3633cceb751cc101ab45dace4973f41dcd593), [b/223488673](https://issuetracker.google.com/issues/223488673))
- Fix a multi-window issue that when focus changes back to the app it fails to resume the camera when (1) other high priority app opens a different camera (2) the device is Samsung Android 12 devices. ([I7e9f2](https://android-review.googlesource.com/#/q/I7e9f2e0d306c43a9693f281b1d44ab80d4be8622))
- Workaround included for devices that crash when checking availability of flash. These devices will not have torch available. ([If26a3](https://android-review.googlesource.com/#/q/If26a3e436ce12dc82451f07ce49969ea237017c0), [b/216667482](https://issuetracker.google.com/issues/216667482))
- Fix `AbstractMethodError` issue happened when apps use extensions and enable proguard. ([I7cbaf](https://android-review.googlesource.com/#/q/I7cbaf1aae571a2b4c12859171bcd46c529e33d57), [b/222726805](https://issuetracker.google.com/issues/222726805))
- Force disable bokeh extension mode on Motorola razr 5G device which will cause black preview screen issue. ([I35d49](https://android-review.googlesource.com/#/q/I35d499e78e40b60f5f3193072543aabddf0b9850))
- Fixed audio/video out of sync after pause and resume on some Samsung devices pre-API 29. ([I64622](https://android-review.googlesource.com/#/q/I646221b9f94ae688592d4be96245f17f74806f0b), [b/202798609](https://issuetracker.google.com/issues/202798609), [b/202798572](https://issuetracker.google.com/issues/202798572))
- Fixed audio/video out of sync after pause and resume on Sony G3125. ([I2a1a5](https://android-review.googlesource.com/#/q/I2a1a5c3cdb4f5908819fb93af19e237426c673fb), [b/202799148](https://issuetracker.google.com/issues/202799148))
- Fixed a crash when the Recorder encountered an `InvalidConfigException`. However, this fix only prevents app from crashing, but doesn't resolve the cause of the `InvalidConfigException`. If the `Recorder` still cannot be configured, applications will receive error callback when it starts recording. ([I89c29](https://android-review.googlesource.com/#/q/I89c295716c6228c47f8bdadefef8336c9c058bd3), [b/213617227](https://issuetracker.google.com/issues/213617227))

**External Contribution**

- updated :compose:ui:ui-test api (updateApi) due to test-coroutines-lib migration ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

### Version 1.1.0-beta02

February 23, 2022

`androidx.camera:camera-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d133838a0a0efc58107ebeca386c34d70789865b..43a214c72ffc3093ee9c3d7c340ad3a57ed4289b/camera)

**API Changes**

- Add the ability to specify physical camera ID through Camera2Interop. ([I5aed8](https://android-review.googlesource.com/#/q/I5aed884146c751f31970b8be3adca4b2ee2110fb))

**Bug Fixes**

- Fixed the stretched preview issue on Oppo Find N ([I7d004](https://android-review.googlesource.com/#/q/I7d004bb90e7800338f83b8b7cb5c614529110e8e))
- Fixed a Galaxy J7 Prime issue that the preview is distorted. ([I4c500](https://android-review.googlesource.com/#/q/I4c500e2e310f686bcf1f974996e6e1284122d422))
- Use compatible bitrate to find video encoder. ([d969052](https://android-review.googlesource.com/#/q/d9690520eb8e306ba9c7febe9c8ac5e9c0e0dcc3))

### Version 1.1.0-beta01

January 26, 2022

`androidx.camera:camera-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f06551837636599d191fd581d56b68225440ed82..d133838a0a0efc58107ebeca386c34d70789865b/camera)

**New Features**

- From 1.1.0-beta01, all CameraX libraries will align the same version number. This will help developers track versions much easier and reduce the complexity of large version compatibility matrix.

**API Changes**

- Added `Camera2CameraControl.clearCaptureRequestOptions` for clearing the existing capture request options. ([Ifa07d](https://android-review.googlesource.com/#/q/Ifa07da1e4417c4bf9a4f6c64ab3d954be33ccfc9))

**Bug Fixes**

- Fixed the crash when recording the video on some pre-Android O(API 26) devices. ([I88fdf](https://android-review.googlesource.com/#/q/I88fdff4a6c3bf756378c66f08564e820110f74a5), [b/212328261](https://issuetracker.google.com/issues/212328261))
- Fixed the incorrect AF region issue when using `cameraControl#startFocusAndMetering()` on front lens-facing camera in Samsung devices ([Ifbf59](https://android-review.googlesource.com/#/q/Ifbf590152fa5740a2ca4ef5eee32ba424bc70f3e), [b/210548792](https://issuetracker.google.com/issues/210548792))
- Use torch as flash on Pixel 3a/Pixel 3a XL to improve the speed and the captured image quality in dark ([Ib12b6](https://android-review.googlesource.com/#/q/Ib12b6f948e545a1b33862e14db8bb4d989032fa6), [b/211474332](https://issuetracker.google.com/issues/211474332))
- Enabled applications to resume the camera when camera is interrupted by other higher priority application in the multi-window mode and the focus changes back to the application. Please note that there could be some latency(1 second to 10 seconds or more) between focus changes and camera reopened due to some framework issue. ([I4d092](https://android-review.googlesource.com/#/q/I4d0929f80b644387b8ba1ec3ec8b8c792a8a2481))

### Version 1.1.0-alpha12

December 15, 2021

`androidx.camera:camera-*:1.1.0-alpha12` is released. [Version 1.1.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85f6fde74bd9e34dee843bce6a5acfba9b82c38e..f06551837636599d191fd581d56b68225440ed82/camera)

**API Changes**

- Removed unnecessary `@RequiresApi(21)` annotations from the inner classes/interfaces. ([I8e286](https://android-review.googlesource.com/#/q/I8e28678667e2f8a5e982d64674abe4c19b5e9155), [b/204917951](https://issuetracker.google.com/issues/204917951))
- The quality constants and fallback strategy constants of `QualitySelector` have been changed to be represented by class objects. For example, `QualitySelector.QUALITY_HD` is changed to `Quality.HD`, and `QualitySelector.FALLBACK_STRATEGY_LOWER` is changed to the instance returned by `FallbackStrategy.lowerQualityOrHigherThan(Quality)`. The API used to create `QualitySelector` has been changed to a list-based API. The new API `QualitySelector.fromOrderedList(List<Quality>)` will refer to the order of the input quality list instead of the order created by `QualitySelector.Procedure`. `QualitySelector.Procedure` class has been removed. ([I43343](https://android-review.googlesource.com/#/q/I4334316b03343c325c458cb37bc0db20267d87a9))
- `PendingRecording.withEventListener()` was removed and the event listener must now be passed to `PendingRecording.start()`. This event listener requirement is meant to encourage handling of asynchronous errors that are reported in the `VideoRecordEvent.Finalize` event. ([I1e71d](https://android-review.googlesource.com/#/q/I1e71d3fdc43a27a63434467ec40f5fe2a9b7a284))
- `ActiveRecording` has been renamed to `Recording` to reduce verbosity. ([I77ceb](https://android-review.googlesource.com/#/q/I77ceb5c25a268e8b7687f6a3578102e162fd8661))

**Bug Fixes**

- Fixed the issue that captured photos in `FLASH_AUTO` mode is underexposed in dark conditions on Pixel 3a and Pixel 3a XL ([I13f19](https://android-review.googlesource.com/#/q/I13f19d787a770b4757ce6f80783aadf586d5c5b7), [b/205373142](https://issuetracker.google.com/issues/205373142))
- Always use latest display size to determine the preview `Resolution`. ([I4a694](https://android-review.googlesource.com/#/q/I4a694498d55c220f501756d97c01634f340bc3c4))
- Filtered out cameras which do not have `REQUEST_AVAILABLE_CAPABILITIES_BACKWARD_COMPATIBLE`. Cameras with `REQUEST_AVAILABLE_CAPABILITIES_BACKWARD_COMPATIBLE` have the minimal set of capabilities that every camera device supports. Camera without `REQUEST_AVAILABLE_CAPABILITIES_BACKWARD_COMPATIBLE` might be a camera to support special functionality and does not support standard color output. `CameraX` can't support the `Preview`, `ImageCapture`, `ImageAnalysis` or `VideoCapture` use cases for those cameras. Therefore, those cameras should be filtered out to prevent incorrect usage. ([Ib8cda](https://android-review.googlesource.com/#/q/Ib8cda657a8903e1cc0d0fc7ed4419984482835a2))
- `CameraSelector#filter` no longer throws an `IllegalArgumentException` when the result set is empty. ([I27804](https://android-review.googlesource.com/#/q/I27804168a78b11d74051d7b407762ed46c9f0f50))
- Smarter heuristics are now used to select encoder settings based on OEM specified profiles. ([Iaeef0](https://android-review.googlesource.com/#/q/Iaeef0bdf8252b5830c9a370718141b5c50316223))
- Fixed Preview will have interlaced color lines after start UHD video recording on Pixel1. ([I833c6](https://android-review.googlesource.com/#/q/I833c65d48e5a050742b4d1b4f2c4a851563c87c4), [b/205340278](https://issuetracker.google.com/issues/205340278))

### Version 1.1.0-alpha11

November 17, 2021

`androidx.camera:camera-*:1.1.0-alpha11` is released. [Version 1.1.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d51a5b31d004ef5b808e917260eb704d9e1c6bb2..ab8e6d320bb31b74ef87c504c9c5ac2b61d5ab98/camera)

**API Changes**

- Added CameraSelector#filter to the public API to filter a list of CameraInfos based on a CameraSelector. ([I105d0](https://android-review.googlesource.com/#/q/I105d07cb5a391b45045cbf06a429ab77e04fe040))
- Add setOutputImageRotationEnabled API for ImageAnalysis config. User can enable rotation for YUV/RGB image buffer. The rotation degree is a relative rotation calculated based on sensor rotation and target rotation to keep image upfront.

- Add setOutputImageRotationEnabled API for ImageAnalysis config. User can enable rotation for YUV/RGB image buffer. The rotation degree is a relative rotation calculated based on sensor rotation and target rotation to keep image upfront.

  Add `getSensorToBufferTransformMatrix` API in ImageInfo. The returned matrix is a mapping from sensor coordinates to buffer coordinates, which is, from the value of `CameraCharacteristics.SENSOR_INFO_ACTIVE_ARRAY_SIZE` to `(0, 0,
  image.getWidth, image.getHeight)`. The matrix can be used to map the coordinates from one {UseCase} to another. For example, mapping coordinates of the face detected with ImageAnalysis to Preview. ([I9ff1e](https://android-review.googlesource.com/#/q/I9ff1ee7581fff9febe7ccdc952f0bd1d8314dbb6))
- Added a new API ImageCapture.Builder#setJpegQuality to allow changing the output JPEG image compression quality when taking picture. ([I8dcf4](https://android-review.googlesource.com/#/q/I8dcf4c2b1652e2fec383073c2b86dd52abd0273c))

- Renamed MediaStoreOutputOptions.getCollection to
  MediaStoreOutputOptions.getCollectionUri. ([I16639](https://android-review.googlesource.com/#/q/I1663979876eb6fa27e3adfc56fbb6be0245a54ee))

**Bug Fixes**

- Fixed the issue where flash being triggered during tap-to-focus (startFocusAndMetering) when flash mode is auto or always_on in low-light environment. ([Id4c11](https://android-review.googlesource.com/#/q/Id4c1101c8b9b10bc8c64abb2102a2a712951fe41))
- Disabled HDR+ on Pixel 2 XL / Pixel 3 XL in MINIMIZE_LATENCY mode to reduce latency. ([Ib6270](https://android-review.googlesource.com/#/q/Ib6270375fdae288d34dd182b2d48294bc90d1e49), [b/203505523](https://issuetracker.google.com/issues/203505523))

**External Contribution**

### Version 1.1.0-alpha10

October 13, 2021

`androidx.camera:camera-*:1.1.0-alpha10` is released. [Version 1.1.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d51a5b31d004ef5b808e917260eb704d9e1c6bb2/camera)

**New Features**

- Released `androidx.camera:camera-video:1.1.0-alpha10` as the first alpha version for Video officially. There are [several known issues](https://issuetracker.google.com/issues?q=hotlistid:3493084+status:open) to be fixed in the later releases.

**API Changes**

- Added `@RequiresApi(21)` annotation to all CameraX classes and dropped minSdkVersion from AndroidManifest.xml. This will allow camera-core to be easily integrated into applications that have a minSdkVersion less than 21, but want to conditionally use code paths that rely on API 21 and higher. For any application with minSdkVersion 21 or higher, this change requires no action. ([Ie7f2e](https://android-review.googlesource.com/#/q/Ie7f2e23fa25ea401df4cddbe4d99651397cc0263), [b/200599470](https://issuetracker.google.com/issues/200599470))

**Bug Fixes**

- Throw an InitializationException to make the app be able to gracefully handle the AssertionError happened when creating CameraCharacteristics. ([Ibec79](https://android-review.googlesource.com/#/q/Ibec79fc0034482c47c25c41fa6d76a6a0c10d02c))

### Version 1.1.0-alpha09

September 29, 2021

`androidx.camera:camera-camera2:1.1.0-alpha09`, `androidx.camera:camera-core:1.1.0-alpha09`, and `androidx.camera:camera-lifecycle:1.1.0-alpha09` are released. [Version 1.1.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9e98cbf6f7926e3ccb8a11600bd631b238ed64c9..0329df5c3c75f45da38e69e594283dddfe1e82c7/camera)

**API Changes**

- ExperimentalUseCaseGroup annotation is removed now that the APIs are no longer experimental. ([I01ef5](https://android-review.googlesource.com/#/q/I01ef54912cd4ef540fe0389f785aa0bec5fc0783))

**Bug Fixes**

- Fix the issue where the captured photos are blurred in `MAXIMIZE_QUALITY` mode. ([I173a9](https://android-review.googlesource.com/#/q/I173a99c55ee46bc78033ef0582b24acf4e432403), [b/193823892](https://issuetracker.google.com/issues/193823892))
- Fixed a Samsung Galaxy J5 issue that camera gets stuck after taking pictures with flash on/auto in dark environment ([I3aab9](https://android-review.googlesource.com/#/q/I3aab98fe328680bae3f3e98430bf1040123d0481))
- When cropping is needed for ImageCapture, compressing the output cropped image with the specified JPEG quality level according to the set capture mode. If the capture mode is `CAPTURE_MODE_MINIMIZE_LATENCY`, the JPEG compression quality will be 95. If the capture mode is `CAPTURE_MODE_MAXIMIZE_QUALITY`, the JPEG compression quality will be 100. ([Ieb37c](https://android-review.googlesource.com/#/q/Ieb37cfede4173d165bd481b86a04545887b0d487), [b/142856426](https://issuetracker.google.com/issues/142856426))

### Version 1.1.0-alpha08

August 18, 2021

`androidx.camera:camera-camera2:1.1.0-alpha08`, `androidx.camera:camera-core:1.1.0-alpha08`, and `androidx.camera:camera-lifecycle:1.1.0-alpha08` are released. [Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86548c494687f4a4aadf3ebb2f724e410b378fcb..9e98cbf6f7926e3ccb8a11600bd631b238ed64c9/camera)

**New Features**

- Add setOutputImageFormat API for image analysis config. User can select ImageAnalysis.OUTPUT_IMAGE_FORMAT_YUV_420_888 or ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888. By default, ImageAnalysis.OUTPUT_IMAGE_FORMAT_YUV_420_888 will be selected. ([I7902d](https://android-review.googlesource.com/#/q/I7902dfe9a05e40e928319ab6e2fae25cf1084623))

**API Changes**

- ExperimentalUseCaseGroupLifecycle annotation is removed now that the APIs are no longer experimental. ([I17b85](https://android-review.googlesource.com/#/q/I17b85c8bb3cd33f85bff02bcd3abaeeca1a39b15))

**Bug Fixes**

- Fixed Preview screen is too bright on the Huawei P20 Lite. This problem only occurs when certain special Preview resolutions are used together with a large zoom in value. ([Idefce](https://android-review.googlesource.com/#/q/Idefce5b35d6a2c275b08da127bb7a7f278216e23), [b/192129158](https://issuetracker.google.com/issues/192129158))
- Fixed an issue that flash is not working on some devices when setting flash mode to FLASH_MODE_ON shortly followed by taking pictures. ([Ieb49b](https://android-review.googlesource.com/#/q/Ieb49b78a6b5bc9ea30b0edee91af76359454d9ac))
- Fixed the issue where Preview will halt for a while when taking pictures if VideoCapture, ImageCapture and Preview are bound. ([I56197](https://android-review.googlesource.com/#/q/I5619740857a7d5b62d64d4811e84fbd5ab959579), [b/193864120](https://issuetracker.google.com/issues/193864120))
- Allows ImageAnalysis to select a resolution larger than 1080p. A LIMITED-level above device can support a RECORD size resolution for ImageAnalysis when it is bound together with Preview and ImageCapture. The trade-off is the selected resolution for the ImageCapture will also need to be a RECORD size resolution. To successfully select a RECORD size resolution for ImageAnalysis, a RECORD size target resolution should be set on both ImageCapture and ImageAnalysis. This indicates that the application clearly understands the trade-off and prefers the ImageAnalysis to have a larger resolution rather than the ImageCapture to have a MAXIMUM resolution. For the definitions of RECORD, MAXIMUM sizes and more details see https://developer.android.com/reference/android/hardware/camera2/CameraDevice#regular-capture. The RECORD size refers to the camera device's maximum supported recording resolution, as determined by CamcorderProfile. The MAXIMUM size refers to the camera device's maximum output resolution for that format or target from StreamConfigurationMap.getOutputSizes(int). ([I1ee97](https://android-review.googlesource.com/#/q/I1ee973a50f9605324f06f406ca2230a464ed2363), [b/192911449](https://issuetracker.google.com/issues/192911449))
- Add the Exif info to the captured image. ([I01ff0](https://android-review.googlesource.com/#/q/I01ff0014f5124fc265ead5816789f41047e43cac), [b/193342619](https://issuetracker.google.com/issues/193342619))
- In ImageCapture, return the URI of the saved image if the saving location is File. ([Ib5b49](https://android-review.googlesource.com/#/q/Ib5b49b6b3555503b12f7461f6eca8f4407cab636), [b/149241379](https://issuetracker.google.com/issues/149241379))
- Fixed an issue that captured images with flash is dark on many devices. ([I4e510](https://android-review.googlesource.com/#/q/I4e51038d54b47955a57c7e80200c506759cf9562))

### Version 1.1.0-alpha07

July 21, 2021

`androidx.camera:camera-camera2:1.1.0-alpha07`, `androidx.camera:camera-core:1.1.0-alpha07`, and `androidx.camera:camera-lifecycle:1.1.0-alpha07` are released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d042a98877f160baa61a8f88718b6a49b7a15d61..86548c494687f4a4aadf3ebb2f724e410b378fcb/camera)

**Bug Fixes**

- Fixed a Samsung Galaxy Note 5 issue that camera gets stuck after taking pictures with flash on/auto in dark environment ([If6871](https://android-review.googlesource.com/#/q/If6871a66f0f9681603ecb7ab92a3a6ede9ec6753))
- Fixed `YuvToJpegProcessor` EOFException issue when extension mode is enabled and `ImageCapture#CAPTURE_MODE_MAX_QUALITY` mode is set. ([I538bd](https://android-review.googlesource.com/#/q/I538bdbc1e460cb5ad3d98cf87017127d7e68f131), [b/192017012](https://issuetracker.google.com/issues/192017012))

### Version 1.1.0-alpha06

June 30, 2021

`androidx.camera:camera-camera2:1.1.0-alpha06`, `androidx.camera:camera-core:1.1.0-alpha06`, and `androidx.camera:camera-lifecycle:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5065c9982754d7b54b8577d64c4ff830375a4b0e..d042a98877f160baa61a8f88718b6a49b7a15d61/camera)

**API Changes**

- Promote the experimental exposure compensation APIs for camera-core ([I08ee8](https://android-review.googlesource.com/#/q/I08ee8d04e3ed4078dd548ca900d887bebd37e18c))
- Added a API isFocusMeteringSupported in CameraInfo which allows applications to check if the given FocusMeteringAction is supported on current camera or not. ([Ib45ae](https://android-review.googlesource.com/#/q/Ib45aec3f7da1d614e3e319ba5f239837be382914), [b/188606490](https://issuetracker.google.com/issues/188606490))
- Exposed getResolutionInfo API to provide the resolution information for Preview, ImageCapture and ImageAnalysis. ([I2b613](https://android-review.googlesource.com/#/q/I2b61350f38bafa40862c923077d9da2675f16905), [b/188600718](https://issuetracker.google.com/issues/188600718))
- Promoted the following experimental APIs to official APIs: CameraXConfig.Builder#setAvailableCamerasLimiter(), CameraXConfig.Builder#setMinimumLoggingLevel(), CameraXconfig.Builder#setSchedulerHandler(), CameraXConfig#getAvailableCamerasLimiter(), CameraXConfig#getMinimumLoggingLevel(), CameraXConfig#getCameraExecutor(), CameraXConfig#getSchedulerHandler(). ([I2ade2](https://android-review.googlesource.com/#/q/I2ade23f6a8d5f0de66828ca3ca963cafc055fd4a))
- Exposed the CameraProvider interface to provide access to a set of cameras. ([I1a7b1](https://android-review.googlesource.com/#/q/I1a7b1fc1c026b6c8ce91aabad3bdfa9052bd8b82))
- Promote the experimental UseCaseGroup API for camera-core, camera-lifecycle and camera-video. Added `ViewPort#getLayoutDirection`, `ViewPort.Builder#setLayoutDirection` and `ViewPort.Builder#setScaleType` for customizing viewport. ([I7cee8](https://android-review.googlesource.com/#/q/I7cee86237511def4bbcd0aab8e32a9592ec78dc3))

### Version 1.1.0-alpha05

June 2, 2021

`androidx.camera:camera-camera2:1.1.0-alpha05`, `androidx.camera:camera-core:1.1.0-alpha05`, and `androidx.camera:camera-lifecycle:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/623bf2f080d4f35417d1af18aebdb72d29620275..5065c9982754d7b54b8577d64c4ff830375a4b0e/camera)

**API Changes**

- Removed `Camera2CameraFilter` class. Suggest to select camera by CameraFilter and retrieve CameraCharacteristics or other Camera2 related information through Camera2CameraInfo if needed. ([Ib887c](https://android-review.googlesource.com/#/q/Ib887c896d909690accc4923ee2af2bed46ac3c93))
- `ExperimentalCameraFilter` APIs are now out of experimental stage and become formal APIs. They can be used without annotated OptIn. ([I4bc94](https://android-review.googlesource.com/#/q/I4bc946c2ee431ea8ec67982a68a1181ebc2e335f))
- Added camera state API that's exposed through `CameraInfo#getCameraState()`. ([Ia86b4](https://android-review.googlesource.com/#/q/Ia86b4332f352e0fd41fe0e40f4a05f4026f46ca7))
- Added experimental API `CameraInfo#getCameraSelector()` which returns a CameraSelector unique to its camera ([I77f9f](https://android-review.googlesource.com/#/q/I77f9f0396ae8c4703d6bfb90055ba6119e773d00))

**Bug Fixes**

- Fixed the issue that ListenableFuture returned in setZoomRatio and setLinearZoom cannot complete on some android 11 devices ([I716d7](https://android-review.googlesource.com/#/q/I716d7273111769d3da23de346ebfec8f017d3b98))
- Speed up Camera switching and reduce the error happen rate of the camera device ([I34c99](https://android-review.googlesource.com/#/q/I34c99dd6bf6dcf95ee174f28bacc8bbc9c0caa59))
- Replaced ExperimentalUseCaseGroupLifecycle with ExperimentalUseCaseGroup. ([I3b2ef](https://android-review.googlesource.com/#/q/I3b2ef21251f3831245722d9cf46edc52d406ddcf), [b/159033688](https://issuetracker.google.com/issues/159033688))

### Version 1.1.0-alpha04

April 21, 2021

`androidx.camera:camera-camera2:1.1.0-alpha04`, `androidx.camera:camera-core:1.1.0-alpha04`, and `androidx.camera:camera-lifecycle:1.1.0-alpha04` are released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe710f46552d00a05886b5490e9fc247aaf91529..623bf2f080d4f35417d1af18aebdb72d29620275/camera)

**Bug Fixes**

- Fixed a memory leak caused by multiple threads concurrently accessing the same collection. The memory leak may cause the Activity or Fragment to be retained by a Preview instance. ([I7b4b8](https://android-review.googlesource.com/#/q/I7b4b832be4117cd37f21659555b0ea99e9e56e09))
- Replaced annotation `@Experimental` with `@RequiresOptIn` to experimental APIs. For calling experimental APIs, use `androidx.annotation.OptIn` instead of deprecated `androidx.annotation.experimental.UseExperimental`. ([Iff226](https://android-review.googlesource.com/#/q/Iff2262a11208aa8c9292d650ba8d9ae0ed500b78))
- Fixed ImageCapture with flash On/Auto takes washed out images on Samsung Galaxy S7. ([I30001](https://android-review.googlesource.com/#/q/I30001bdfb0fc773e9705d63a2f60a8402c55187c))
- Added a CameraState API that will be exposed through CameraInfo. ([I75392](https://android-review.googlesource.com/#/q/I753924a1130123cb25ee92f2f576c5b37dbfd60d))

### Version 1.1.0-alpha03

March 24, 2021

`androidx.camera:camera-camera2:1.1.0-alpha03`, `androidx.camera:camera-core:1.1.0-alpha03`, and `androidx.camera:camera-lifecycle:1.1.0-alpha03` are released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..fe710f46552d00a05886b5490e9fc247aaf91529/camera)

**Bug Fixes**

- Output JPEG format for `ImageCapture#OnImageCapturedCallback` when Extensions modes is enabled. ([I0d7b1](https://android-review.googlesource.com/#/q/I0d7b1a770ddb506f3fc1977aa8bd34c5b43a1c69))
- Fixed initialization failure on UMIDIGI BISON devices ([I57d9e](https://android-review.googlesource.com/#/q/I57d9e1c1e2ba1e4d585c3fcbba18820a65ab5562), [b/180818665](https://issuetracker.google.com/issues/180818665))
- Fixed Samsung A3 stretched preview in PreviewView. ([Iacb30](https://android-review.googlesource.com/#/q/Iacb30b0ff035d5a24ac221470a6815d96eca1725), [b/180121821](https://issuetracker.google.com/issues/180121821))

### Version 1.1.0-alpha02

February 24, 2021

`androidx.camera:camera-camera2:1.1.0-alpha02`, `androidx.camera:camera-core:1.1.0-alpha02`, and `androidx.camera:camera-lifecycle:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ae5a49a113d2ec1fd217074bf0df7393533a620..5c90131a69042a6a3e13952e1da9e7ffc571c31d/camera)

**API Changes**

- Added an API `ProcessCameraProvider.getAvailableCameraInfos()` to directly retrieve information about the available cameras, which are either all of the device's cameras, or those selected by the `CameraSelector` provided in `CameraXConfig.Builder.setAvailableCamerasLimiter(CameraSelector)`. ([Ieac08](https://android-review.googlesource.com/#/q/Ieac084685b307ee16a52b938d50e7baf5c8d8fd7))

**Bug Fixes**

- CameraX now tries to force open a camera on the initial attempt, this may result in CameraX stealing the camera away from other camera clients when its app has a higher priority. ([Iab069](https://android-review.googlesource.com/#/q/Iab0692e958c0a39d9da61a43fdd534e01d32be79), [b/175820568](https://issuetracker.google.com/issues/175820568))
- Fixed the Robolectric test failure when setAvailableCamerasLimiter is used in CameraXConfig. ([Ice307](https://android-review.googlesource.com/#/q/Ice307fb4af419d423f83545d26f279b2ee01f797))
- This change catches the exception when the image queue is maxed out in ImageAnalysis. So instead of crashing, you may notice other use cases being frozen or sluggish. e.g. frozen/sluggish preview. ([Ic12da](https://android-review.googlesource.com/#/q/Ic12dafa0b0feed875a07ea1d8c23c52977b15afa), [b/175851631](https://issuetracker.google.com/issues/175851631))
- Fixed ExtensionsErrorListener to report errors when only Preview or ImageCapture is bound. ([I5ae39](https://android-review.googlesource.com/#/q/I5ae397bd5d04c635828e1604ac7d36dc2643add7))
- Fixed ImageCapture performance regression by removing the validation of image saved location before taking a picture. After making this change, if the save destination is invalid, it will take longer to get the failure response because it will try to save the image after the photo is taken. ([I1fd4e](https://android-review.googlesource.com/#/q/I1fd4ed93d0984668c634c832010901d604cb0dc6), [b/177061560](https://issuetracker.google.com/issues/177061560))
- Fixed ImageCapture performance regression with "File" type OutputFileOptions. ([I5164a](https://android-review.googlesource.com/#/q/I5164a91c586df0a8dd90f30eda0ce43c1cbe5cd7), [b/177061560](https://issuetracker.google.com/issues/177061560))
- Documentation updated to recommend against using `ProcessCameraProvider.configureInstance(...)` from library code. ([Ib8a9f](https://android-review.googlesource.com/#/q/Ib8a9f475f705e0125f001755b19813ab0f133cc8))

### Version 1.1.0-alpha01

January 27, 2021

`androidx.camera:camera-camera2:1.1.0-alpha01`, `androidx.camera:camera-core:1.1.0-alpha01`, and `androidx.camera:camera-lifecycle:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6aa34a2b3faad8227b3311a8e372e4ccf7eaf462..5ae5a49a113d2ec1fd217074bf0df7393533a620/camera)

**Bug Fixes**

- Workaround included for intermittent corrupt image data in JPEGs on SM-G930T back-facing camera. ([I52001](https://android-review.googlesource.com/#/q/I52001b98b8124fc9a3ee6b8c343225bb21881d12), [b/159831206](https://issuetracker.google.com/issues/159831206))
- Fixed `IllegalArgumentException` issue that happened when all preview supported sizes are smaller than 640x480 and display size is larger than 640x480. ([I2a63c](https://android-review.googlesource.com/#/q/I2a63ce8e2ad42a9cc060c8635ac3603bf440b1ec), [b/150506192](https://issuetracker.google.com/issues/150506192))
- Resources in libraries with no explicitly declared public resources (ex. via public.xml) are now private by default. ([Ia1dcc](https://android-review.googlesource.com/#/q/Ia1dcca1ad5c65c1ab90b97c22589e7392161fd62), [b/170882230](https://issuetracker.google.com/issues/170882230))

## Camera-Camera2, Camera-Core, \& Camera-Lifecycle Version 1.0.2

### Version 1.0.2

September 29, 2021

`androidx.camera:camera-camera2:1.0.2`, `androidx.camera:camera-core:1.0.2`, and `androidx.camera:camera-lifecycle:1.0.2` are released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a955b74b0c426a59775ffe00c594d41a71e88686..32c3806c0ebe680d8812676282dee392586bf6cf/camera)

**Bug Fixes**

- Fix the issue where the captured photos are blurred in `MAXIMIZE_QUALITY` mode. ([I173a9](https://android-review.googlesource.com/#/q/I173a99c55ee46bc78033ef0582b24acf4e432403), [b/193823892](https://issuetracker.google.com/issues/193823892))
- Fixed a issue that captured image with flash is dark on many devices. ([I4e510](https://android-review.googlesource.com/#/q/I4e51038d54b47955a57c7e80200c506759cf9562))

## Camera-Camera2, Camera-Core, \& Camera-Lifecycle Version 1.0.1

### Version 1.0.1

July 21, 2021

`androidx.camera:camera-camera2:1.0.1`, `androidx.camera:camera-core:1.0.1`, and `androidx.camera:camera-lifecycle:1.0.1` are released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/de3cb1599436fa5736337b468448853d1981fadc..a955b74b0c426a59775ffe00c594d41a71e88686/camera)

**Bug Fixes**

- Fixed the issue that the `ListenableFuture` returned in
  `setZoomRatio` and `setLinearZoom` cannot complete on some android
  11 devices ([I716d7](https://android-review.googlesource.com/#/q/I716d7273111769d3da23de346ebfec8f017d3b98))

- Fixed the issue that the camera gets stuck at closing camera state on some devices and causes black preview. ([I34c99](https://android-review.googlesource.com/q/I34c99dd6bf6dcf95ee174f28bacc8bbc9c0caa59))

## Camera-Camera2, Camera-Core, \& Camera-Lifecycle Version 1.0.0

> [!NOTE]
> **Note:** Newer versions of AndroidX libraries now correctly reflect `implementation` dependencies versus `api` dependencies. If your project relies on an implicit dependency exposed through an `implementation` dependency in version `1.0.0`, you must explicitly depend on that dependency in your `build.gradle`.

### Version 1.0.0

May 5, 2021

`androidx.camera:camera-camera2:1.0.0`, `androidx.camera:camera-core:1.0.0`, and `androidx.camera:camera-lifecycle:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/00406dba96e608d4f56964a2d73e234cfb5ed019..de3cb1599436fa5736337b468448853d1981fadc/camera)

**Major features of 1.0.0**

- CameraX supports [Preview](https://developer.android.com/training/camerax/preview), [ImageCapture](https://developer.android.com/training/camerax/take-photo), and [Analysis](https://developer.android.com/training/camerax/analyze)
- CameraX manages the camera [lifecycle](https://developer.android.com/training/camerax/architecture#lifecycles) within an easy to use API
- CameraX aims to provide a compatibility layer that fixes many issues in the Android Camera Ecosystem

**Known Issues**

- See [Known Issue list](https://issuetracker.google.com/hotlists/1551123)

### Version 1.0.0-rc05

April 21, 2021

`androidx.camera:camera-camera2:1.0.0-rc05`, `androidx.camera:camera-core:1.0.0-rc05`, and `androidx.camera:camera-lifecycle:1.0.0-rc05` are released. [Version 1.0.0-rc05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c790ba79eb9b47d7edda547565fafbbf09f55f10..00406dba96e608d4f56964a2d73e234cfb5ed019/camera)

**Bug Fixes**

- Fixed ImageCapture with flash On/Auto takes washed out images on Samsung Galaxy S7. ([I30001](https://android-review.googlesource.com/#/q/I30001bdfb0fc773e9705d63a2f60a8402c55187c))

### Version 1.0.0-rc04

March 24, 2021

`androidx.camera:camera-camera2:1.0.0-rc04`, `androidx.camera:camera-core:1.0.0-rc04`, and `androidx.camera:camera-lifecycle:1.0.0-rc04` are released. [Version 1.0.0-rc04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cbbcaf606229323f6a80e9627683e68773ea249b..c790ba79eb9b47d7edda547565fafbbf09f55f10/camera)

**Bug Fixes**

- Fixed initialization failure on UMIDIGI BISON devices ([I57d9e](https://android-review.googlesource.com/#/q/I57d9e1c1e2ba1e4d585c3fcbba18820a65ab5562), [b/180818665](https://issuetracker.google.com/issues/180818665))

### Version 1.0.0-rc03

February 24, 2021

`androidx.camera:camera-camera2:1.0.0-rc03`, `androidx.camera:camera-core:1.0.0-rc03`, and `androidx.camera:camera-lifecycle:1.0.0-rc03` are released. [Version 1.0.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/061e502eeee77b497212dbe85a2a826a9a2c91e8..cbbcaf606229323f6a80e9627683e68773ea249b/camera)

**Bug Fixes**

- Fix format error in the document of `ProcessCameraProvider#getInstance`
- Fixed the Robolectric test failure when setAvailableCamerasLimiter is used in CameraXConfig.
- Fixed ImageCapture performance regression by removing the validation of image saved location before taking a picture. After making this change, if the save destination is invalid, it will take longer to get the failure response because it will try to save the image after the photo is taken
- This change catches the exception when the image queue is maxed out in ImageAnalysis. So instead of crash, you may notice other use cases being frozen or sluggish. e.g. frozen/sluggish preview.
- Workaround included for intermittent corrupt image data in JPEGs on SM-G930T back-facing camera. ([I52001](https://android-review.googlesource.com/#/q/I52001b98b8124fc9a3ee6b8c343225bb21881d12), [b/159831206](https://issuetracker.google.com/issues/159831206))
- This change catches the exception when the image queue is maxed out in ImageAnalysis. So instead of crashing, you may notice other use cases being frozen or sluggish. e.g. frozen/sluggish preview. ([Ic12da](https://android-review.googlesource.com/#/q/Ic12dafa0b0feed875a07ea1d8c23c52977b15afa), [b/175851631](https://issuetracker.google.com/issues/175851631))
- Fixed the Robolectric test failure when setAvailableCamerasLimiter is used in CameraXConfig. ([Ice307](https://android-review.googlesource.com/#/q/Ice307fb4af419d423f83545d26f279b2ee01f797))
- Fixed ImageCapture performance regression by removing the validation of image saved location before taking a picture. After making this change, if the save destination is invalid, it will take longer to get the failure response because it will try to save the image after the photo is taken. ([I1fd4e](https://android-review.googlesource.com/#/q/I1fd4ed93d0984668c634c832010901d604cb0dc6), [b/177061560](https://issuetracker.google.com/issues/177061560))
- Fixed ImageCapture performance regression with "File" type OutputFileOptions. ([I5164a](https://android-review.googlesource.com/#/q/I5164a91c586df0a8dd90f30eda0ce43c1cbe5cd7), [b/177061560](https://issuetracker.google.com/issues/177061560))

### Version 1.0.0-rc02

January 27, 2021

`androidx.camera:camera-camera2:1.0.0-rc02`, `androidx.camera:camera-core:1.0.0-rc02`, and `androidx.camera:camera-lifecycle:1.0.0-rc02` are released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6aa34a2b3faad8227b3311a8e372e4ccf7eaf462..061e502eeee77b497212dbe85a2a826a9a2c91e8/camera)

**Bug Fixes**

- Fixed IllegalArgumentException issue happened when all preview supported sizes are smaller than 640x480 and display size is larger than 640x480. ([b/150506192](http://issuetracker.google.com/150506192))
- Limit number of camera reopen attempts. While attempting to recover from certains issues when opening the camera, CameraX will no longer attempt to reopen the camera indefinitely, instead it will stop after retrying for 10 seconds.[I435d2](https://android-review.googlesource.com/c/platform/frameworks/support/+/1516019/)

- Fixed `IllegalArgumentException` issue that happened when all preview supported sizes are smaller than 640x480 and display size is larger than 640x480. ([I2a63c](https://android-review.googlesource.com/#/q/I2a63ce8e2ad42a9cc060c8635ac3603bf440b1ec), [b/150506192](https://issuetracker.google.com/issues/150506192))

### Version 1.0.0-rc01

December 16, 2020

`androidx.camera:camera-camera2:1.0.0-rc01`, `androidx.camera:camera-core:1.0.0-rc01`, and `androidx.camera:camera-lifecycle:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/369d39c56a955f4ee612581e26de38eb44ee02a8..6aa34a2b3faad8227b3311a8e372e4ccf7eaf462/camera)

**API Changes**

- Changed CameraFilter and Camera2Filter to take in CameraInfo. ([I6883d](https://android-review.googlesource.com/#/q/I6883d80f188ed3be14865a1409274a5c261b3cec))
- Added experimental class Camera2CameraControl to allow interoperating with Camera2 APIs dynamically. ([I45cf3](https://android-review.googlesource.com/#/q/I45cf3d1ff4415b078bfa8efcde39bbe722750897))
- Renamed Camera2CameraInfo#fromCameraInfo to #from. ([Ia2bd6](https://android-review.googlesource.com/#/q/Ia2bd6c212d6820b838d17f29a32bda98920018d0))
- Added an experimental setAvailableCamerasLimiter API to CameraXConfig to allow apps to optimize the initialization latency by avoiding initializing unused cameras. ([I6cf88](https://android-review.googlesource.com/#/q/I6cf887bab434dc6c6e0524e8a44d43d0f25de552))
- Added experimental method `CameraXConfig.Builder#setMinimumLoggingLevel()` to allow setting a minimum logging level for CameraX logs. When not set, it defaults to `Log#DEBUG`. ([Ic3245](https://android-review.googlesource.com/#/q/Ic32451f2640f1003a4e8dfcc3ffab36a6de58c63))

**Bug Fixes**

- Workaround included for intermittent corrupt image data in JPEGs on SM-G930V back-facing camera. ([I5aca5](https://android-review.googlesource.com/#/q/I5aca54ce3ce8a5a50bc7b84175b2f0dbb7e706e2), [b/159831206](https://issuetracker.google.com/issues/159831206))
- Fixed the issue that taking pictures doesn't receive results when flash is always/on and the environment is dark on Samsung SM-A716 devices. ([If98b2](https://android-review.googlesource.com/#/q/If98b2b45cbf1a7fb7228d4db1885846621644341), [b/172036589](https://issuetracker.google.com/issues/172036589))
- Fixed the issue that the Preview cannot be stopped by calling `Preview.setSurfaceProvider(null)`. ([I3ac18](https://android-review.googlesource.com/#/q/I3ac188840c60de20e0e891bb168922aa6fb37c1b))
- Fixed orientation issue when capturing 4:3 images on some devices. ([I0e3fb](https://android-review.googlesource.com/#/q/I0e3fb7705daeb5b8caa98e80215a545f8a3ca484), [b/171492111](https://issuetracker.google.com/issues/171492111))

### Camera Camera2, Core, \& Lifecycle Version 1.0.0-beta12

November 11, 2020

`androidx.camera:camera-camera2:1.0.0-beta12`, `androidx.camera:camera-core:1.0.0-beta12`, and `androidx.camera:camera-lifecycle:1.0.0-beta12` are released. [Version 1.0.0-beta12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9a238add5b2df90db87d93473595ccd6911e297e..369d39c56a955f4ee612581e26de38eb44ee02a8/camera)

**Bug Fixes**

- Disabled auto flash on Samsung A3 devices to fix the crash when taking a photo with auto flash AE mode on Samsung A3 devices. ([Ia5fe3](https://android-review.googlesource.com/#/q/Ia5fe30075e4ec65abe4030e4589a35e3c30a607f), [b/157535165](https://issuetracker.google.com/issues/157535165))
- Fixed an issue where the preview was stretched on Nexus 4 devices running Android L (API levels 21 and 22). ([I4d407](https://android-review.googlesource.com/#/q/I4d407ee366c978de4e518995e97d5946fc19e29a), [b/158749159](https://issuetracker.google.com/issues/158749159))
- `OnImageCapturedCallback#onCaptureSuccess` base class implementation no longer closes the image. This is for preventing unexpected behavior to developers. Developers should not rely on super.onCaptureSuccess to close the image. ([Ifbf9c](https://android-review.googlesource.com/#/q/Ifbf9c98da68fcbba0c177a1a0579d2d65c120346))
- The androidx variant of the Experimental annotation has been deprecated to provide parity with Kotlin. It has been replaced by the RequiresOptIn annotation, and the Java-facing linter has been updated to support both the new Kotlin annotation and the new androidx variant. ([I52495](https://android-review.googlesource.com/#/q/I52495721777cf9d2243a825fc491e59c031d2e96), [b/151331381](https://issuetracker.google.com/issues/151331381))

### Camera-Camera2 Version 1.0.0-beta11

October 14, 2020

`androidx.camera:camera-camera2:1.0.0-beta11` is released. [Version 1.0.0-beta11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/691e3a429902a0a3e087f28877e7cd5f668114fe..9a238add5b2df90db87d93473595ccd6911e297e/camera/camera-camera2)

**New Features**

- Supports android 11 `CONTROL_ZOOM_RATIO` API for zoom on android 11 or later devices which contains valid `CONTROL_ZOOM_RATIO_RANGE`. ([I62cc6](https://android-review.googlesource.com/#/q/I62cc6c3aaffd47de3416bca11e5beb8414e73631))

**Bug Fixes**

- Fixed the NumberFormatException issue happened when the camera Id is a non-integer camera Id. ([Ib2228](https://android-review.googlesource.com/#/q/Ib222860b07f73e02c25c5a7cf1f5deaa16b01fd3))
- Improved the latency of CameraX initialization and bindToLifecycle ([I61dc5](https://android-review.googlesource.com/#/q/I61dc581555c6f665162b435bd13f0fd86c965993))
- Creation of UseCases do not require initialization of CameraX to complete. All implementation specific configurations are set on UseCase once it is attached to a Camera instance which for the public API is `ProcessCameraProvider.bindToLifecycle()`. ([Ia5411](https://android-review.googlesource.com/#/q/Ia5411289c68c202dae2316b8a9987d6d28a3d749))
- `<UseCase>.getTargetRotation()` will return `Surface.ROTATION_0` if called before being attached to a Camera instance unless a targetRotation has been set on the Builder or UseCase. ([I80fcd](https://android-review.googlesource.com/#/q/I80fcd8b33ce27e31fd3fc38b4f9b6e0a62b06bc5))

### Camera-Core Version 1.0.0-beta11

October 14, 2020

`androidx.camera:camera-core:1.0.0-beta11` is released. [Version 1.0.0-beta11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/691e3a429902a0a3e087f28877e7cd5f668114fe..9a238add5b2df90db87d93473595ccd6911e297e/camera/camera-core)

**New Features**
- Supports android 11 `CONTROL_ZOOM_RATIO` API for zoom on
android 11 or later devices which contains valid
`CONTROL_ZOOM_RATIO_RANGE`. ([I62cc6](https://android-review.googlesource.com/#/q/I62cc6c3aaffd47de3416bca11e5beb8414e73631))

**Bug Fixes**

- Fixed the NumberFormatException issue happened when the camera Id is a non-integer camera Id. ([Ib2228](https://android-review.googlesource.com/#/q/Ib222860b07f73e02c25c5a7cf1f5deaa16b01fd3))
- Creation of UseCases do not require initialization of CameraX to complete. All implementation specific configurations are set on UseCase once it is attached to a Camera instance which for the public API is `ProcessCameraProvider.bindToLifecycle()`. ([Ia5411](https://android-review.googlesource.com/#/q/Ia5411289c68c202dae2316b8a9987d6d28a3d749))
- `<UseCase>.getTargetRotation()` will return `Surface.ROTATION_0` if called before being attached to a Camera instance unless a targetRotation has been set on the Builder or UseCase. ([I80fcd](https://android-review.googlesource.com/#/q/I80fcd8b33ce27e31fd3fc38b4f9b6e0a62b06bc5))

### Camera-Core Version 1.0.0-beta10

September 23, 2020

`androidx.camera:camera-core:1.0.0-beta10` is released. [Version 1.0.0-beta10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ebe09b1cb65d62b65b01054fd9ecd055d653a22..691e3a429902a0a3e087f28877e7cd5f668114fe/camera/camera-core)

> [!CAUTION]
> **Caution:** Please do not use **Camera-Core Version 1.0.0-beta09** as there is a Known Issue \[See Bug Fixes Below\] around image capture. Please do not use this version in your applications. Instead use **Camera-Core Version 1.0.0-beta10** and above.

**Bug Fixes**

- Fix bug in validating file save destination for image capture ([I8c565](https://android-review.googlesource.com/#/q/ee9fa116b553b77b17badd7cac58374c99651753), [b/167697553](https://issuetracker.google.com/167697553))

### Camera-Camera2 Version 1.0.0-beta10

September 23, 2020

`androidx.camera:camera-camera2:1.0.0-beta10` is released. [Version 1.0.0-beta10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ebe09b1cb65d62b65b01054fd9ecd055d653a22..691e3a429902a0a3e087f28877e7cd5f668114fe/camera/camera-camera2)

**Bug Fixes**

- Release to support [Camera-Core 1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/camera#camera-core-1.0.0-beta10)

### Camera-Camera2 Version 1.0.0-beta09

September 16, 2020

`androidx.camera:camera-camera2:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..9ebe09b1cb65d62b65b01054fd9ecd055d653a22/camera/camera-camera2)

> [!CAUTION]
> **Caution:** Please do not use **Camera-Core Version 1.0.0-beta09** as there is a Known Issue around image capture. Please do not use this version in your applications. Instead use [`Camera-Core Version 1.0.0-beta10`](https://developer.android.com/jetpack/androidx/releases/camera#camera-core-1.0.0-beta10) and above.

**API Changes**

- Instead of providing static methods, Camera2CameraInfo takes in a CameraInfo instance when created to retrieve Camera2 related information from. ([I5b844](https://android-review.googlesource.com/#/q/I5b84490f751e0464837270ada2b84e26bdf4d3e1))

**Bug Fixes**

- Fixed target aspect ratio issue on tablet devices. A 16:9 size should be selected when the target aspect ratio is set as `AspectRatio.RATIO_16_9`. ([Ib7fcf](https://android-review.googlesource.com/#/q/Ib7fcfae000fb16010c2246f22a7e6f6efb8021aa), [b/151969438](https://issuetracker.google.com/issues/151969438))
- Throw an `InitializationException` to make the app be able to gracefully handle the AssertionError happened when creating CameraCharacteristics. ([I89c8c](https://android-review.googlesource.com/#/q/I89c8c2b05f77b1cc00c070f4815e12ed775d1181), [b/160524721](https://issuetracker.google.com/issues/160524721))
- Added experimental interfaces for ExposureCompensation ([If96c7](https://android-review.googlesource.com/#/q/If96c7276cb8d20ac59ea5167245225c6327d23e0))

### Camera-Core Version 1.0.0-beta09

September 16, 2020

`androidx.camera:camera-core:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..9ebe09b1cb65d62b65b01054fd9ecd055d653a22/camera/camera-core)

**API Changes**

- fixed the bug where viewport is marked as non-null on UseCaseGroup. Developers should be able to create a viewport without setting a viewport. ([Ie3d2e](https://android-review.googlesource.com/#/q/Ie3d2ecb4559916680bfeee64a480cc52b1c6d627))
- Added experimental interfaces for `ExposureCompensation` ([If96c7](https://android-review.googlesource.com/#/q/If96c7276cb8d20ac59ea5167245225c6327d23e0))
- Allow arbitrary target rotation for Preview. The transformation info is calculated and returned to user on-the-fly via a new `TranformationInfoListener` callback. ([I21470](https://android-review.googlesource.com/#/q/I214703dfb077891738666bfbfbe1b7187fe02461))

**Bug Fixes**

- Fixed the issue that flash on some devices would not turn off. It happens when the flash mode is set to `FLASH_MODE_ON` to take a picture, and is changed to `FLASH_MODE_OFF` when the flash is fired. The symptom is like torch mode enabled. ([Ib4451](https://android-review.googlesource.com/#/q/Ib44514dbad0b8103de615e21717b11d45fb65640), [b/162568128](https://issuetracker.google.com/issues/162568128))
- Forced PreviewView to use TextureView if extension effect is enabled and the vendor library implementation needs to do a special process on the output surface. ([I0c3cc](https://android-review.googlesource.com/#/q/I0c3cc867847ec0f350119a8d05ace41c631d04de))
- Fixed the activity/fragment leak when an activity/fragment context is passed to `ProcessCameraProvider.getInstance(Context)`.

**Known Issues**

- When ViewPort is set, the crop rect of ImageCapture might be incorrect on devices who rotate the image buffer in HAL. This will be fixed in the next release.

### Camera-Camera2 Version 1.0.0-beta08

August 19, 2020

`androidx.camera:camera-camera2:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/camera/camera-camera2)

**Bug Fixes**

- Optimized bindToLifecycle to run quickly on the main thread. ([I1d57e](https://android-review.googlesource.com/#/q/I1d57e67ff68c4f453bcb9f510761605057e69514))
- DisplayOrientedMeteringPointFactory takes in a CameraInfo instance instead of a CameraSelector so there is a direct mapping to which Camera the factory will be generating points for. All classes which use DisplayOrientedMeteringPointFactory also take in a CameraInfo instance instead of CameraSelector. ([I400c1](https://android-review.googlesource.com/#/q/I400c16899037e29fd37d6cf6faaa87ed70188de1))
- Fixed auto-resolution aspect ratio size grouping issue that a 16:9 mod16 size (864x480) is selected when the target resolution setting is 2016x1080 and there is another 1920x1080 16:9 size supported. ([I53167](https://android-review.googlesource.com/#/q/I531671972a05bf01e2dea1f96da5bc3d6655c391), [b/159363774](https://issuetracker.google.com/issues/159363774))
- Fix the CameraControl issue where it's unable to work by a race condition ([I2279f](https://android-review.googlesource.com/#/q/I2279f7bda1a9edf90af0c46b2db749d59821e0cc), [b/152333890](https://issuetracker.google.com/issues/152333890), [b/160714166](https://issuetracker.google.com/issues/160714166))

### Camera-Core Version 1.0.0-beta08

August 19, 2020

`androidx.camera:camera-core:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/camera/camera-core)

**API Changes**

- `DisplayOrientedMeteringPointFactory` takes in a `CameraInfo` instance instead of a `CameraSelector` so there is a direct mapping to which Camera the factory will be generating points for. All classes which use `DisplayOrientedMeteringPointFactory` also take in a `CameraInfo` instance instead of `CameraSelector`. ([I400c1](https://android-review.googlesource.com/#/q/I400c16899037e29fd37d6cf6faaa87ed70188de1))

**Bug Fixes**

- For image capture, overwrite the flip horizontal flag in metadata based on camera direction. ([I28499](https://android-review.googlesource.com/#/q/I28499bd3a46b0760d31fe100f40175552e6b6221))
- Initialization should no longer crash when using a Context that does not return an Application object from `Context.getApplicationContext()`. ([I3d3c9](https://android-review.googlesource.com/#/q/I3d3c9880c24264e2b78f367777d675002f2126d3), [b/160817073](https://issuetracker.google.com/issues/160817073))

### Camera-Camera2 Version 1.0.0-beta07

July 22, 2020

`androidx.camera:camera-camera2:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/camera/camera-camera2)

**Bug Fixes**

- Fixed the issue that the preview is stretched on android 5.0 legacy device. ([I0c03a](https://android-review.googlesource.com/#/q/I0c03abc989e61b74de933424395e229d5263b52a))
- Excluded some JPEG supported sizes that will cause WYSIWYG issue on some devices. ([Ib5128](https://android-review.googlesource.com/#/q/Ib512864103b6e4d21db7c82ace403b555f7701df))

### Camera-Core Version 1.0.0-beta07

July 22, 2020

`androidx.camera:camera-core:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/camera/camera-core)

**API Changes**

- Merge `FIT_CENTER`, `FIT_START`, and `FIT_END` fit style with `FIT`. `FIT`means that the returned crop rect will be the max possible sensor rect. ([Ia73c3](https://android-review.googlesource.com/#/q/Ia73c3ee780dc386ba255d4c3193e67bc244472c3))
- Preview's crop rect is configured by viewport. Only the area covered by the crop rect should be visible to end users. ([I142a4](https://android-review.googlesource.com/#/q/I142a4bfb1f859721da12e10074b5cbe5e299e68d))

**Bug Fixes**

- Fixed the issue that the preview is stretched on android 5.0 legacy device. ([I0c03a](https://android-review.googlesource.com/#/q/I0c03abc989e61b74de933424395e229d5263b52a))
- Fixed the `ConcurrentModificationException` exception issue when unbinding use cases. ([I371c0](https://android-review.googlesource.com/#/q/I371c052c5edd6aeed2a127a44cc422758417ea57))

### Camera-Camera2 Version 1.0.0-beta06

June 24, 2020

`androidx.camera:camera-camera2:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/camera/camera-camera2)

**API Changes**

- Added experimental interfaces for filtering cameras by camera ID and CameraCharacteristics. ([I28f61](https://android-review.googlesource.com/#/q/I28f6110779ead8d6ed3177b86bd21ae5c27528c2))

**Bug Fixes**

- Fixed the issue where startFocusAndMetering fails to focus successfully on Samsung Galaxy S7. ([If3be7](https://android-review.googlesource.com/#/q/If3be7c3359687a47a61fbd0f9c7f018d5d8fd323), [b/159039233](https://issuetracker.google.com/issues/159039233))
- Fix the camera can't be closed after quit the app. ([I7a7b3](https://android-review.googlesource.com/#/q/I7a7b3a7ab9006b513bf0a4fee4e9747150fb9479))
- Fix repeated camera switching breaks preview when using SurfaceView implementation of PreviewView ([I920ce](https://android-review.googlesource.com/#/q/I920ceac24f0ed65d33badfd4b8263eb71d741da0))
- `CameraControl#startFocusAndMetering` will fail if none of the specified MeteringPoint can generate valid metering rectangles. ([Id53ce](https://android-review.googlesource.com/#/q/Id53ce08eb463ae641765eb91bacb5b466ba6a008))

### Camera-Core Version 1.0.0-beta06

June 24, 2020

`androidx.camera:camera-core:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/camera/camera-core)

**API Changes**

- Added experimental interfaces for filtering cameras by camera ID and CameraCharacteristics. ([I28f61](https://android-review.googlesource.com/#/q/I28f6110779ead8d6ed3177b86bd21ae5c27528c2))

**Bug Fixes**

- CameraX can now be configured with `ProcessCameraProvider#configureInstance()` before calling `ProcessCameraProvider#getInstance()`. This allows for customization of the `CameraXConfig` without requiring implementing `CameraXConfig.Provider` in the app's Application class. ([Ia1a8d](https://android-review.googlesource.com/#/q/Ia1a8d0b979e033d42ac06d1498395af07942d08f))
- `CameraControl#startFocusAndMetering` will fail if none of the specified MeteringPoint can generate valid metering rectangles. ([Id53ce](https://android-review.googlesource.com/#/q/Id53ce08eb463ae641765eb91bacb5b466ba6a008))

### Camera-Camera2 Version 1.0.0-beta05

June 10, 2020

`androidx.camera:camera-camera2:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-camera2)

**Bug Fixes**

- Fix the crash on app startup when initialising CameraX while phone is in Do Not Disturb mode. An `InitializationException` contains a `CameraUnavailableException` that will be set to the `ListenableFuture` of the intialization result instead of crashing the application. ([I9909a](https://android-review.googlesource.com/#/q/I9909af08a8305fcf8e603d709d98b4488f1af69f), [b/149413835](https://issuetracker.google.com/issues/149413835))
- Fixed the crash when calling `startFocusAndMetering` on devices that `CONTROL_AF_STATE` is null. ([Ife55e](https://android-review.googlesource.com/#/q/Ife55e091685081b37f87d61d429c7243a494e946), [b/157084254](https://issuetracker.google.com/issues/157084254))

### Camera-Core Version 1.0.0-beta05

June 10, 2020

`androidx.camera:camera-core:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-core)

**API Changes**

- Fix the crash on app startup when initialising CameraX while phone is in Do Not Disturb mode. An `InitializationException` contains a `CameraUnavailableException` will be set to the `ListenableFuture` of the intialization result instead of crashing the application. ([I9909a](https://android-review.googlesource.com/#/q/I9909af08a8305fcf8e603d709d98b4488f1af69f), [b/149413835](https://issuetracker.google.com/issues/149413835))

**Bug Fixes**

- Updated javadocs of `setTargetResolution` and `setTargetRotation`. ([Iae16f](https://android-review.googlesource.com/#/q/Iae16f3a1fc2f4419fbb5e53c97c88b56313acad7))

### Camera-Camera2 Version 1.0.0-beta04

May 27, 2020

`androidx.camera:camera-camera2:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4319ecd6ebdd8a9f8600cc5b3d1aada1f716abac..c4d097f4335fe6b0268ee9a6d53df43615da0d90/camera/camera-camera2)

**Bug Fixes**

- Allowed applications to set any camera2 capture request parameters via `Camera2Interop` without causing a crash. Please note that if there are issues that arise as a result of overriding parameters. Stability and behaviour are not guaranteed when overriding parameters using Camera2Interop. ([Ibe5a1](https://android-review.googlesource.com/#/q/Ibe5a101775aac7a7d257e4dfcb287ba66dd6df1d), [b/149103700](https://issuetracker.google.com/issues/149103700))
- Auto-initialization is fixed when using an app on a device that is using a pseudo-locale. ([I3bef3](https://android-review.googlesource.com/#/q/I3bef307a065f90b1fa1778d353b417ad597aca78), [b/154767663](https://issuetracker.google.com/issues/154767663))
- Converted error log related to detached use case to a debug log on Camera2CameraImpl. ([I1a565](https://android-review.googlesource.com/#/q/I1a565e55af6e63792287221f8cbd9e7747fd6875), [b/154422490](https://issuetracker.google.com/issues/154422490))
- Fixed issue where image taken is too dark sometimes even though flash is fired. ([I5d9fa](https://android-review.googlesource.com/#/q/I5d9fa6b387861189dbf666350b7f0ac94793ac06), [b/149729613](https://issuetracker.google.com/issues/149729613))
- Fix bug where buffer in `ImageProxy` from `ImageCapture` was not rewound ([I0c455](https://android-review.googlesource.com/#/q/I0c45524cdf5cc44e2b0441e82c4cc467d1e611e3), [b/153249512](https://issuetracker.google.com/issues/153249512))
- Fixed the issues where binding ImageCapture only: (1) Failed to take photos with MAX_QUALITY; (2) Generated bad Image quality because auto exposure does not work. ([I17782](https://android-review.googlesource.com/q/I177820832ae13c8f5b0120c5eb02311302f0104b), [b/145326998](https://issuetracker.google.com/issues/145326998))
- Improved reliability of re-opening camera when CameraX is disconnected by another process or codepath stealing the camera ([I1fbc3](https://android-review.googlesource.com/q/I1fbc374743468bb81ba549b3421e69a92d967022), [b/153714651](https://issuetracker.google.com/issues/153714651))

### Camera-Core Version 1.0.0-beta04

May 27, 2020

`androidx.camera:camera-core:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4319ecd6ebdd8a9f8600cc5b3d1aada1f716abac..c4d097f4335fe6b0268ee9a6d53df43615da0d90/camera/camera-core)

**API Changes**

- Adds an experimental API, `CameraXConfig.Builder#setSchedulerHandler()` for setting the handler used internally by the CameraX camera stack. This new API along with `CameraXConfig.Builder#setCameraExecutor()` should allow full control over the threads being used by the CameraX camera stack. ([I7bf32](https://android-review.googlesource.com/#/q/I7bf321368947cb1176d89eb311bc3c5586c58bb5), [b/121160431](https://issuetracker.google.com/issues/121160431))

**Bug Fixes**

- Fixes crash in `ImageAnalysis` where the `ImageProxy` is accessed after the `ImageReaderProxy` has been closed. This also makes it so that all `ImageProxy` received by the `Analyzer` must be closed before the `ImageReaderProxy` will be closed. ([I4b299](https://android-review.googlesource.com/#/q/I4b29996bcaf7549df6ababf080ea367326ba0dd3), [b/145956416](https://issuetracker.google.com/issues/145956416), [b/154155377](https://issuetracker.google.com/issues/154155377), [b/156357269](https://issuetracker.google.com/issues/156357269))
- Removed the `CameraInfo` parameter from `PreviewView#createSurfaceProvider()`, `PreviewView` now internally retrieves it from the `SurfaceRequest`. ([If18f0](https://android-review.googlesource.com/#/q/If18f04ff541eb77ec58b216d201e04802ab14785), [b/154652477](https://issuetracker.google.com/issues/154652477))
- Auto-initialization is fixed when using an app on a device that is using a pseudo-locale. ([I3bef3](https://android-review.googlesource.com/#/q/I3bef307a065f90b1fa1778d353b417ad597aca78), [b/154767663](https://issuetracker.google.com/issues/154767663))
- Fixed issue where image taken is too dark sometimes even though flash is fired. ([I5d9fa](https://android-review.googlesource.com/#/q/I5d9fa6b387861189dbf666350b7f0ac94793ac06), [b/149729613](https://issuetracker.google.com/issues/149729613))
- Fix issue with `ImageAnalysis` where multiple calls to setAnalyzer/clearAnalyzer resulted in the analyzer not receiving images to analyze. ([I6169f](https://android-review.googlesource.com/#/q/I6169f72de35f48e916b081498137d8f195d82c88), [b/151605317](https://issuetracker.google.com/issues/151605317), [b/153514544](https://issuetracker.google.com/issues/153514544))
- Fix bug where buffer in `ImageProxy` from `ImageCapture` was not rewound ([I0c455](https://android-review.googlesource.com/#/q/I0c45524cdf5cc44e2b0441e82c4cc467d1e611e3), [b/153249512](https://issuetracker.google.com/issues/153249512))
- Fixed the issue that the first camera in the supported list from `CameraManager` is not always selected to use. ([I4c624](https://android-review.googlesource.com/#/q/I4c624a4506c7fa1b01ad5b79864dcb51e9416984), [b/153418028](https://issuetracker.google.com/issues/153418028))
- Fixed intermittent crash caused by setting `Preview.SurfaceProvider` not releasing the previously requested surface. `"java.lang.IllegalStateException: Camera surface session should only fail with request cancellation"` ([I8e4e7](https://android-review.googlesource.com/q/I8e4e7b107cddfb6e47fb58805a100b3af261f95d), [b/155936225](https://issuetracker.google.com/155936225))

### Camera-Camera2 Version 1.0.0-beta03

April 15, 2020

`androidx.camera:camera-camera2:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..0e54727f73afedc58cfdda00fb123d6b50d3459d/camera/camera-camera2)

**Bug Fixes**

- Fixes to support the release of `camera-core`

### Camera-Core Version 1.0.0-beta03

April 15, 2020

`androidx.camera:camera-core:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..0e54727f73afedc58cfdda00fb123d6b50d3459d/camera/camera-core)

**Bug Fixes**

- Fixed regression from beta03 where calling `bindToLifecycle()` with zero `UseCase`s would cause a thrown exception. This prevented retrieval of a `Camera` without binding a `UseCase`.

### Camera-Camera2 Version 1.0.0-beta02

April 1, 2020

`androidx.camera:camera-camera2:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/camera/camera-camera2)

**Bug Fixes**

- Fixed the `ImageInfo.getRotationDegrees()` from the `ImageProxy` produced by `ImageCapture` so that it matches the EXIF orientation rotational value. ([Id4281](https://android-review.googlesource.com/#/q/Id4281f3a168b710eafef120ea9d12800a6d8d98d), [b/150802561](https://issuetracker.google.com/issues/150802561))
- Explicit ordering of CameraX dependencies within `build.gradle` is no longer required to use the default CameraX/Camera2 implementation. For cases where declaring strict dependencies is required, all CameraX dependencies can now be included in the build file. ([I46e88](https://android-review.googlesource.com/#/q/I46e888ee4450689ed5950b4f153b1592ff5c7fff))
- Fixed the `IllegalArgumentException` issue happening on the devices where the display size is smaller than 640x480. ([Ife3f2](https://android-review.googlesource.com/#/q/Ife3f24876122fc0897ee8c2985a4309a55556479), [b/150506192](https://issuetracker.google.com/issues/150506192))
- Fixed `bindToLifecycle` so that it only modifies the UseCase if it successfully binds. Previously when calling `bindToLifecycle` in order to do resolution calculations the UseCase is updated. Now it no longer needs to update the UseCase to do the calculations ([I78d9e](https://android-review.googlesource.com/#/q/I78d9ec96d30e2a2487ff43119f8b2067c8b92a03))

### Camera-Core Version 1.0.0-beta02

April 1, 2020

`androidx.camera:camera-core:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/camera/camera-core)

**Bug Fixes**

- Fixed the `ImageInfo.getRotationDegrees()` from the `ImageProxy` produced by `ImageCapture` so that it matches the EXIF orientation rotational value. ([Id4281](https://android-review.googlesource.com/#/q/Id4281f3a168b710eafef120ea9d12800a6d8d98d), [b/150802561](https://issuetracker.google.com/issues/150802561))
- Fixed `bindToLifecycle` so that it only modifies the UseCase if it successfully binds. Previously when calling `bindToLifecycle` in order to do resolution calculations the UseCase is updated. Now it no longer needs to update the UseCase to do the calculations ([I78d9e](https://android-review.googlesource.com/#/q/I78d9ec96d30e2a2487ff43119f8b2067c8b92a03))
- Fixed an issue where the `Preview` use case's capture session wasn't being updated when the preview surface changed after calling `Preview.setSurfaceProvider()` more than once.

### Camera-Camera2 Version 1.0.0-beta01

February 26, 2020

`androidx.camera:camera-camera2:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c76d34916ab81f6fea02ba6e2d717243562bb24..401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e/camera/camera-camera2)

**Bug Fixes**

- Renamed `SurfaceRequest.setSurface(Surface)` to `SurfaceRequest.provideSurface(Surface)`, and `SurfaceRequest.setWillNotComplete()` to `SurfaceRequest.willNotProvideSurface()`. ([I224fe](https://android-review.googlesource.com/#/q/I224fe088094eed4fb9e8a8ff83b7fa2417c6f36d))
- Fixed an issue with the aspect ratio of a saved image not being correct after changing the target rotation value using `ImageCapture.setTargetRotation()`. ([I474ea](https://android-review.googlesource.com/#/q/I474ea093775c723930b94cdfbdf2d4f0d93b3612), [b/148763432](https://issuetracker.google.com/issues/148763432))
- Fixed initialization of app variants with ProGuard enabled by preserving the flag that sets the default `CameraXConfig` provider. ([I2d6c1](https://android-review.googlesource.com/#/q/I2d6c1134e10e9d9add5e61d32efb14b06f2ae7ac))

### Camera-Core Version 1.0.0-beta01

February 26, 2020

`androidx.camera:camera-core:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c76d34916ab81f6fea02ba6e2d717243562bb24..401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e/camera/camera-core)

**API Changes**

- Replaced the `ListenableFuture` on `SurfaceRequest.provideSurface()` with an `Executor` and `Callback`. This simplifies the API by no longer requiring handling of exceptions on `provideSurface()` and enforces that the `provideSurface()` callback cannot be cancelled. This is to prevent crashes on older devices caused by prematurely releasing surfaces. The `SurfaceRequest.Result` object is now used for tracking how a `SurfaceRequest` uses the provided `Surface`. ([I7854b](https://android-review.googlesource.com/#/q/I7854b0a3c01c2e11030d18bf99eb4539207267e3))
- Renamed `SurfaceRequest.setSurface(Surface)` to `SurfaceRequest.provideSurface(Surface)` and `SurfaceRequest.setWillNotComplete()` to `SurfaceRequest.willNotProvideSurface()`. ([I224fe](https://android-review.googlesource.com/#/q/I224fe088094eed4fb9e8a8ff83b7fa2417c6f36d))

**Bug Fixes**

- Fixed an issue with the aspect ratio of a saved image not being correct after changing the target rotation value using `ImageCapture.setTargetRotation()`. ([I474ea](https://android-review.googlesource.com/#/q/I474ea093775c723930b94cdfbdf2d4f0d93b3612), [b/148763432](https://issuetracker.google.com/issues/148763432))
- Fixed initialization of app variants with ProGuard enabled by preserving the flag that sets the default `CameraXConfig` provider. ([I2d6c1](https://android-review.googlesource.com/#/q/I2d6c1134e10e9d9add5e61d32efb14b06f2ae7ac))
- Updated documentation for flash mode APIs to include possible values. ([I4a3ec](https://android-review.googlesource.com/#/q/I4a3ec543d2ed7e316fc1bba6f041412afd5c7315))

### Camera-Camera2 Version 1.0.0-alpha10

February 10, 2020

`androidx.camera:camera-camera2:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..1c76d34916ab81f6fea02ba6e2d717243562bb24/camera/camera-camera2).

**Bug Fixes**

- Improved stability on `INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY` devices by ensuring `Surface`s are only retained for duration of use by Camera2. ([I9dac2](https://android-review.googlesource.com/#/q/I9dac24649dae962541af18b30c7c1841baa53f17))
- Fixed underexposed preview issue on LEGACY devices by adjusting `CONTROL_AE_TARGET_FPS_RANGE` properly. ([1224638](https://android-review.googlesource.com/c/platform/frameworks/support/+/1224638))

### Camera-Core Version 1.0.0-alpha10

February 10, 2020

`androidx.camera:camera-core:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..1c76d34916ab81f6fea02ba6e2d717243562bb24/camera/camera-core).

**API Changes**

- Updated `ImageCapture` to allow saving images to `Uri` and `OutputStream`. Combined overloaded `takePicture` methods into one. Updated test app to use `Uri` as the canonical example. ([Ia3bec](https://android-review.googlesource.com/#/q/Ia3becf13029c367e7525d1b110f89bd4a06833a9))
- `Preview.PreviewSurfaceProvider` has been renamed to `Preview.SurfaceProvider`. `SurfaceProvider`s no longer require developers to create their own `ListenableFuture`, and providing a `Surface` is now done through a new `SurfaceRequest` object. The `Preview.getPreviewSurfaceProvider()` method has been removed due to its potential for misuse when `Preview` is paired with other classes such as `PreviewView`. ([I20105](https://android-review.googlesource.com/#/q/I2010570526c2336250d873c681a5c00d8420938e))
- Added `getTargetRotation()` and `getTargetName()` to `Preview`. ([Iceee7](https://android-review.googlesource.com/#/q/Iceee7422e0603c5e0201f3d3ec4f6326c2408538))
- Added `getTargetRotation()`, `getBackpressureStrategy()`, and `getImageQueueDepth()` in `ImageAnalysis`. ([I9d6d9](https://android-review.googlesource.com/#/q/I9d6d97bbacafc7c4b5183c717567611d691c6a71))
- Added `getTargetRotation()` and `getCaptureMode()` in `ImageCapture()` ([I5bc17](https://android-review.googlesource.com/#/q/I5bc17bfcebea4852e69cbd5e69665e7fef5ca3c4))
- The arguments that were previously passed in `ImageCapture.OnImageSavedCallback.onError()` and `ImageCapture.OnImageCapturedCallback.onError()` have now been replaced by a single argument `ImageCaptureException`, which still contains all the information that was previously passed.
- The file argument previously passed in `ImageCapture.OnImageSavedCallback.onImageSaved()` has been removed. ([I750d2](https://android-review.googlesource.com/#/q/I750d258b4d532ac99d7a49c1c7800dc2edea3c43))
- `Preview` and `ImageCapture` classes are now marked final. ([I2500b](https://android-review.googlesource.com/#/q/I2500b65bfbbaf1f4159816017adf69d06de961a8))
- API updated, with `getZoomRatio()`, `getMaxZoomRatio()`, `getMinZoomRatio()`, and `getLinearZoom()` methods of `CameraInfo` merging into `getZoomState()` which returns a `ZoomState` instance. ([Ib19fe](https://android-review.googlesource.com/#/q/Ib19feb7377aac17623e8d3edbde1dd39b25b31b9))
- Removed API fields `OPTION_TARGET_CLASS` and `OPTION_TARGET_NAME` from `CameraXConfig` as they are intended for internal library use only. Removed constructor for `CameraXConfig.Builder`. ([I96912](https://android-review.googlesource.com/#/q/I96912fa5a8bd9a11ef25d53f789ad190cbd69231))
- Removed requirement that app must extend `Application` in order to initialize CameraX. CameraX will now be initialized with a default Camera2 configuration as long as the `camera-camera2` artifact is included in the application's `build.gradle`. ([I58ff5](https://android-review.googlesource.com/#/q/I58ff5c4440f9fec0afb3d9790f652dd91c2c84bd)) ([b/146923574](https://issuetracker.google.com/issues/146923574))

### Camera-Camera2 Version 1.0.0-alpha09

January 22, 2020

`androidx.camera:camera-camera2:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/94383d99a6ed372cd569bd5ab7d9aab5e0b056ba..0a3d894e8fe0217f1312fb163a89ad51bf15794e/camera/camera-camera2).

**API changes**

- Add camera2 interop path for extracting a Camera2 camera ID. You can extract
  the camera ID from `CameraInfo` using `Camera2CameraInfo.extractCameraId()`.
  The following code sample shows how to use this:

      Camera camera = provider.bindToLifecycle(...);
      String cameraId =
          Camera2CameraInfo.extractCameraId(camera.getCameraInfo());

  The `Camera2CameraInfo` class requires the `ExperimentalCamera2Interop`
  markerClass.

### Camera-Core Version 1.0.0-alpha09

January 22, 2020

`androidx.camera:camera-core:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/94383d99a6ed372cd569bd5ab7d9aab5e0b056ba..0a3d894e8fe0217f1312fb163a89ad51bf15794e/camera/camera-core).

**API changes**

- The `SurfaceOrientedMeteringPointFactory` parameter `useCaseForSurface` was renamed to `useCaseForAspectRatio` and the reference documentation was expanded.
- `FocusMeteringAction.Builder.from()` methods are replaced by the constructors `FocusMeteringAction.Builder()`.
- Removed `DisplayOrientedMeteringPointFactory(android.content.Context, androidx.camera.core.CameraSelector, float, float)`. Applications should use the constructor that takes a `Display` parameter and pass in the current display.
- Javadoc improvements for focus and metering APIs regarding `MeteringMode` and 3A Flags, and usage of `Display` parameter.
- Expanded the reference documentation for `setZoomRatio` and `setLinearZoom`.

**Bug fixes**

- Fixed issues when closing then opening cameras resulting in "Precondition" check failure.
- Fixed a `ConcurrentModificationException` that could occur when using torch and zoom APIs.
- Fixed issue to now select resolutions closer to requested resolution when a mod16 dimensions size is available.
- `startFocusMetering` and `cancelFocusMetering` APIs now behave as documented, with correct timing and potentially returning errors when they occur.
- Fixed issue when a specific target resolution was requested with a crop aspect ratio on a device that doesn't support such sizes. Now, a non-cropped size of sufficient resolution to bound the original request will be selected when available.

### Camera-Camera2 Version 1.0.0-alpha08

December 18, 2019

`androidx.camera:camera-camera2:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/camera/camera-camera2).

**Known Issues**

- Not all Camera2 capture request options work when using the Camera2 interop. If the requested option is not supported, the session fails to start and an error like this may occur: `09-09 14:04:13.643 10117 26020 26036 E AndroidRuntime: java.lang.IllegalArgumentException: Unsupported session configuration combination`

**Bug Fixes**

- Fixed an issue in which a preview black screen occurred after rotating or switching the camera for API Levels 21 and 22.

**API Changes**

- *Experimental*: Added a camera2 interop path for extracting the Camera ID.

### Camera-Core Version 1.0.0-alpha08

December 18, 2019

`androidx.camera:camera-core:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/camera/camera-core).

**Known Issues**

- Apps using the `PreviewView` or `CameraView` may have the wrong aspect ratio preview. This happens after pause or resume on some FULL devices, such as the Pixel2.

**Bug Fixes**

- Updated the documentation for `FocusMeteringAction` and `CameraControl`.
- Implemented `TorchControl` for `enableTorch()` and `getTorchState()`.

**API Changes**

- Hid IntDefs and moved IntDef constants outside of the IntDef definition.
- Moved `rotationDegrees` from class `OnImageCaptureCallback` to `ImageInfo`.
- Moved `rotationDegrees` from class `Analyzer` to `ImageInfo`.

### Camera-Camera2 Version 1.0.0-alpha07

December 4, 2019

`androidx.camera:camera-camera2:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 of camera-camera2 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b46de96e17b1ea1b0f2a729c86cd5a8413d19c5c..4cb7a5cbd2e20d3bf45cae63fea8436818576256/camera/camera-camera2)

- `Camera2Config` is now available for use with initializing and configuring a Camera2-based implementation for CameraX. More details on how to use this in initialization are in the [camera-core section](https://developer.android.com/jetpack/androidx/releases/camera#camera2-core-1.0.0-alpha07) of the release notes.
- The camera2 interop functionally is now marked as experimental and moved to a separate package, `androidx.camera.camera2.interop.`

### Camera-Core Version 1.0.0-alpha07

December 4, 2019

`androidx.camera:camera-core:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 of camera-core contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/22d0f5f2091012403b8be4ffd93314d3ca43b06d..4cb7a5cbd2e20d3bf45cae63fea8436818576256/camera/camera-core)

**Note that there are some substantial changes in this Alpha release as we prepare for Beta.** We recommend you review the changes and share any feedback you may have on the [CameraX Google group](http://g.co/camerax/developers). For those developers using CameraX in apps that are on the Play store, we recommend waiting for the formal Beta release before upgrading the library within your applications.

**API changes**

- ***Important*** : CameraX initialization has changed. Applications should implement `CameraXConfig.Provider`, and use the default `Camera2Config` provided by `androidx.camera.camera2`. A typical usage is:

      import androidx.camera.camera2.Camera2Config
      import androidx.camera.core.CameraXConfig

      public class MyCameraXApplication : Application(),  CameraXConfig.Provider {
          override fun getCameraXConfig(): CameraXConfig {
                  return Camera2Config.defaultConfig(this)
          }
      }

- The CameraX class has been removed. The `bindToLifecycle()`, `unbind()`, `unbindAll()`, `isBound()`, and `hasCamera()` previously provided by the CameraX class call are now available via the `ProcessCameraProvider`.

- A per-process instance of `ProcessCameraProvider` is obtained asynchronously using the static method `ProcessCameraProvider.getInstance()`, which returns a listenable future, which provides the `ProcessCameraProvider` on completion.
  Here it is shown in `onCreate()` for a typical usage. You can place calls to `getInstance()` later in the activity's lifecycle to defer initialization latency to a later time (such as when a user action opens a camera UI).

      import androidx.camera.lifecycle.ProcessCameraProvider
      import com.google.common.util.concurrent.ListenableFuture

      class MainActivity : AppCompatActivity() {
         private lateinit var cameraProviderFuture : ListenableFuture<ProcessCameraProvider>
         override fun onCreate(savedInstanceState: Bundle?) {
             cameraProviderFuture = ProcessCameraProvider.getInstance(this);
        }

- A listener can be added to the `ListenableFuture` returned by `getInstance()`. This ensures the camera provider can be retrieved from the `Future` without blocking on `Future.get()`

      cameraProviderFuture.addListener(Runnable {
        val cameraProvider = cameraProviderFuture.get()
        cameraProvider.bindToLifecycle(...)
      }, ContextCompat.getMainExecutor(this))

- Camera selection is now done by a camera selector, instead of per-use case

      val cameraSelector = CameraSelector.Builder().requireLensFacing(LensFacing.BACK).build()

- `CameraProvider.bindToLifecycle` is given the lifecycle owner, the camera selector, and use cases, which are then bound to the given lifecycle owner and run for the selected camera.

      cameraProvider.bindToLifecycle(this as LifecycleOwner,
             cameraSelector, preview, imageAnalysis)

- Use case "Config" classes are removed. Instead, build use cases directly, setting options on each use case builder. For example:

      preview = Preview.Builder().setTargetAspectRatio(AspectRatio.RATIO_16_9).build()

- The Preview use case has been updated to accept a surface created and managed by the application to ensure Android best practices. It is highly recommended to use the `PreviewView` view class provided in the camera-view package.

      preview.setPreviewSurfaceProvider(previewView.previewSurfaceProvider)

- See documentation for attaching an app-managed surface. In these cases the app manages the lifecycle of the surface.

- ***Important*** : **The `ImageAnalysis` Analyzer method implementation must call `image.close()` on received images when finished using them. Otherwise, new images may not be received or the camera may stall, depending on back pressure setting. Refer to the [reference docs](https://developer.android.com/reference/kotlin/androidx/camera/core/ImageAnalysis) for details.**

- `ImageAnalysis ImageReaderMode` is now changed to a backpressure strategy `intdef`.

- `ImageProxy.getImage()` is marked as experimental. Applications should annotate usage for example via `@androidx.camera.core.ExperimentalGetImage`

- The `UIThread` annotation requirement for the `Analyzer` has been removed.

- The `ImageAnalysis.clearAnalyzer()` function is added for removing an analyzer.

- Listeners with more than 1 method have been renamed to Callback:

  - `ImageCapture.OnImageCapturedListener` is now `ImageCapture.OnImageCapturedCallback`
  - `ImageCapture.OnImageSavedListener` is now `ImageCapture.OnImageSavedCallback`
  - `VideoCapture.OnVideoSavedListener` is now `VideoCapture.OnVideoSavedCallback`
- Enums have changed to IntDef

- Zoom controls have been added:

  - `CameraControl.setLinearZoom()`
  - `CameraControl.setZoomRatio()`
  - `CameraInfo.getLinearZoom()`
  - `CameraInfo.getMaxZoomRatio()`
  - `CameraInfo.getZoomRatio()`
- `CameraInfo.hasFlashUnit()` is added to determine if flash/torch hardware is present.

- `CameraInfo.isFlashAvailable()` has been removed. Torch overrides flash functionality. More detail is included in the [reference documentation](https://developer.android.com/reference/androidx/camera/core/Preview#public-methods_1).

- `ImageCapture.Metadata` fields are replaced by get/set/is accessors.

- `startFocusMetering` and `cancelFocusMetering` now return `ListenableFutures` which represent the asynchronous operation of the call.

- `MeteringPoints` are now functioning as handles to metering actions, and are produced by factories. Apps should use the existing factories rather than custom factories.

**Fixed issues**

- Fixed issue when taking a picture on resuming (after a previous pause had take pictures pending completion).
- Known Issue: `CameraControl.enableTorch()` is functional but the returned `ListenableFuture<Void>` is always an immediate `complete(success)` future, even if there is no flash unit. Future versions will fix this to the final behavior: When there is no flash unit, `enableTorch(true)` fails immediately (won't send request to `CaptureSession`), and `TorchState` remain Off.
- Known Issue: `startFocusAndMetering` and `cancelFocusAndMetering` start and cancel focus metering, but return an immediately `completed (success)` future not representing the documented behavior. The `FocusMeteringResult` from `ListenableFuture<FocusMeteringResult> CameraControl.startFocusAndMetering()` is a fake result which `isFocusSuccessful()` and is always "false," differing from intended, documented behavior.
- Known Issue: A metering point factory for use with `PreviewView` touch events is being developed. For now, apps connecting custom managed surfaces can use the existing metering point factories, and otherwise no touch focus functionality is available for `PreviewView`.

### Camera-Camera2 and Camera-Core Version 1.0.0-alpha06

October 9, 2019

`androidx.camera:camera-camera2:1.0.0-alpha06` and `androidx.camera:camera-core:1.0.0-alpha06` are released. These are the [commits included in `camera-camera2:1.0.0-alpha06`](https://android.googlesource.com/platform/frameworks/support/+log/90f3b785f74ef777d901295e947aa9c6d024afca..b46de96e17b1ea1b0f2a729c86cd5a8413d19c5c/camera/camera-camera2) and these are the [commits included in `camera-core:1.0.0-alpha06`](https://android.googlesource.com/platform/frameworks/support/+log/90f3b785f74ef777d901295e947aa9c6d024afca..22d0f5f2091012403b8be4ffd93314d3ca43b06d/camera/camera-core).

**New features**

Changes to setting aspect ratios:

- `setTargetAspectRatioMode()` was added and accepts an enum argument. This sets the Aspect Ratio Mode with options `RATIO_4_3` or `RATIO_16_9` instead of an arbitrary aspect ratio. This closer reflects the fact that only certain aspect ratios are provided from the camera, rather than any arbitrary ratio.
  - Currently, the only available ratios are 16:9 and 4:3. In the case of 1:1, only certain devices have this available from the camera, and then only at limited resolutions. Applications designing a 1:1 interface or processing should use the more flexible 16:9 or 4:3 choices and crop the display or process a subregion.
  - These aspect ratios are oriented to use the maximum sensor area.
- `getTargetAspectRatio()` was added to use case config APIs, returning the aspect ratio the use case output is targeted for.
- The method `setTargetAspectRatio(Rational aspectRatio)` has been changed for ImageCapture to `setTargetAspectRatioCustom(Rational aspectRatio)`. When set, the ImageCapture output crops accordingly.

Executor APIs

- The following functions accept an executor parameter, which allows the app to control which executor the function runs on.
  - `Preview.setOnPreviewOutputUpdateListener()` API. If the executor is not present for that function, it executes on the main thread.
  - `Preview.setOnPreviewOutputUpdateListener`
  - `FocusMeteringAction.Builder.setAutoFocusCallback`
  - `ImageAnalysis.setAnalyzer`
  - `ImageCapture.takePicture`
  - `CameraView.takePicture`
  - `CameraView.startRecording`
  - `VideoCapture.startRecording`

CameraInfo added with check Flash Available and Sensor Rotation APIs

- Added `CameraInfo` and a `getCameraInfo` method, which allows apps to check if a lens facing CameraInfo is available and if a flash is available on that camera. For example:

      try {
          CameraInfo cameraInfo = CameraX.getCameraInfo(currentCameraLensFacing);
          LiveData<Boolean> isFlashAvailable = cameraInfo.isFlashAvailable();
          flashToggle.setVisibility(isFlashAvailable.getValue() ? View.VISIBLE : View.INVISIBLE);
      } catch (CameraInfoUnavailableException e) {
          Log.w(TAG, "Cannot get flash available information", e);
          flashToggle.setVisibility(View.VISIBLE);
      }

- `CameraInfo.getSensorRotationDegrees()` was added. It provides the camera sensor orientation relative to the device's natural orientation, or for convenience, relative to an orientation described by a Surface rotation (which describes an orientation relative to natural orientation).

**API changes and bug fixes**

- Aspect Ratios: For each use case, applications should call only one of `setTargetResolution()` or `setTargetAspectRatio()`. Calling both on the same builder returns an error.
  - In general it's recommended to use `setTargetAspectRatio()` based on the application's UI design. Specific resolutions are based on the use case. For example, preview is near screen resolutions and image capture provides high resolution stills. See the [automatic resolutions table](https://developer.android.com/training/camerax/configuration#automatic-resolution) for more information.
  - Use `setTargetResolution()` for more specific cases, such as when minimum (to save computation) or maximum resolutions (for processing details) are required.
- Executor API: Removed the `setCallbackHandler()` call from use case configuration APIs. Instead, applications can set the executor as a parameter in various other APIs that set a callback.
- Updated null annotations for various functions.
- Fixed an issue that caused `java.lang.IllegalStateException at Camera$StateCallback.onError` to be thrown when opening the camera.
- Fixed issue where resolutions would be selected that were too small (less than 640x480) when app is requesting larger or default resolutions resulting in a blocky or blurry preview image. Applications that specifically need smaller resolutions can explicitly request them.
- Fixed an issue where the camera would show black screen (failed to start the camera) after returning from an intent that launched another camera application.
- Fixed a bug that threw the following error when apps are repeatedly started or stopped; `java.lang.IllegalArgumentException: CaptureRequest contains unconfigured Input/Output Surface!`
- Fixed the following error that occurs when disabling ImageAnalysis: `java.lang.IllegalStateException: maxImages (4) has already been acquired, call #close before acquiring more.`
- Added additional tests for camera disconnect flow.
- Improved test system robustness when running back-to-back camera tests.

### Camera-Camera2 and Camera-Core Version 1.0.0-alpha05

September 5, 2019

`androidx.camera:camera-camera2:1.0.0-alpha05` and `androidx.camera:camera-core:1.0.0-alpha05` are released. These are the [commits included in camera-camera2:1.0.0-alpha05](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..90f3b785f74ef777d901295e947aa9c6d024afca/camera/camera-camera2) and these are the [commits included camera-core:1.0.0-alpha05](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..90f3b785f74ef777d901295e947aa9c6d024afca/camera/camera-core).

- API Change: Renamed use case error variables:

  - `ImageCapture.UseCaseError` is renamed `ImageCapture.ImageCaptureError`
  - `VideoCapture.UseCaseError` is renamed `VideoCapture.VideoCaptureError`
- Added `CameraControl` API w/Tap-to-Focus APIs

  - Added API to get a `CameraControl` from CameraX for a camera, selected by lens facing:

    `CameraX.getCameraControl(LensFacing lensFacing)`
  - Added `MeteringPointFactory`, `MeteringPoint`, `MeteringMode`, and `FocusMeteringAction` to run Tap-to-Focus:

        MeteringPointFactory factory = new SensorOrientedMeteringPointFactory(width, height);
        MeteringPoint point = factory.createPoint(x, y);
        FocusMeteringAction action = FocusMeteringAction.Builder.from(point,
                                         MeteringMode.AF_ONLY)
            .addPoint(point2, MeteringMode.AE_ONLY) // could have many
            .setAutoFocusCallback(new OnAutoFocusListener(){
                public void onFocusCompleted(boolean isSuccess) {
                }
            })
            // auto calling cancelFocusAndMetering in 5 sec.
            .setAutoCancelDuration(5, TimeUnit.Second)
            .build();

  - Added API for `CameraControl` to start and cancel focus metering:

    `getCameraControl(lensFacing).startFocusAndMetering(action);`
    `getCameraControl(lensFacing).cancelFocusAndMetering();`
  - Added APIs for Metering Point Factories that assist translating tap coordinates to sensor coordinates, based on view classes:

    `MeteringPointFactory factory = new TextureViewMeteringPointFactory(textureView);`
    `MeteringPointFactory factory = new DisplayOrientedMeteringPointFactory(context, lensFacing, viewWidth, viewHeight);`
- Enforce calling the following methods on the Main (UI) thread, throwing an
  `IllegalStateException` when they are not. Future versions will allow usage on
  other threads and ensure serialization.

  - `CameraX.bindToLifecycle()`
  - `CameraX.unbind()`
  - `CameraX.unbindAll()`
  - `ImageAnalysis.setAnalyzer()`
  - `ImageAnalysis.getAnalyzer()`
  - `ImageAnalysis.removeAnalyzer()`
  - `Preview.removePreviewOutputListener()`
  - `Preview.getOnPreviewOutputUpdateListener()`
  - `Preview.setOnPreviewOutputUpdateListener()`
- Various config settings now accept null parameters and corresponding getters may return null.

- Fixed issue when testing on emulators that do not support AF/AE/AWB settings.

- Fixed crash bug on rotation while analyzing image.

- Fixed bug where preview appears black on start (no camera data), after rotation or switching between front and back cameras.

- Removed testing for multiple concurrent image analysis use cases. To ensure compatibility, applications should only attach a single image analysis use case.

- Added initial robolectric tests for fake camera in camera-testing suite (WIP).

- Camera2Inititalizer test removed, as its coverage was unclear/misleading.

### Camera-Camera2 and Camera-Core Version 1.0.0-alpha04

August 7, 2019

`androidx.camera:camera-camera2:1.0.0-alpha04` and `androidx.camera:camera-core:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/da18b8e358a305e4ae90edc548eb48927f037696..6bc5fc2e82861585a6f28128dee9abbbe2e18591/camera).

> [!NOTE]
> **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New Features**

*Changes to Aspect Ratio and Resolution selection*

CameraX's goal is to successfully initialize a camera session. This means CameraX compromises on resolution/aspect ratios based on device capability, in order to start a capture session as its first goal, and so exact requests may not be honored. This may be due to:

- Devices not supporting the requested resolution
- Compatibility issues such as on LEGACY devices where certain resolutions must be used to operate correctly
- On some devices, certain formats are only available at certain aspect ratios
- A preference for a "nearest mod16" for JPEG or video encoding. See [`CameraCharacteristics#SCALER_STREAM_CONFIGURATION_MAP`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SCALER_STREAM_CONFIGURATION_MAP)

Although CameraX creates and manages the session, you should always check
the returned image sizes on the use case output in your code and adjust
accordingly.

Some changes have been made for setting resolutions and aspect ratios, intended to make the API more clear:

- Preview use case is now considered to have a default 4:3 aspect ratio when none is set.
- When CameraX internally considers changes to requested resolutions and aspect ratios based on device capability, it first tries to maintain the same aspect ratio (as determined by any of `setTargetAspectRatio` or `setTargetResolution` calls)
- A "Nearest mod16" version of the resolution is considered as the same aspect ratio.

*ImageAnalysis Non-Blocking Mode*

- The behaviour of `ImageReaderMode.ACQUIRE_LATEST_IMAGE` is now non-blocking. It acquires the latest image in the queue, but discards unused images continuously to allow the camera pipeline to avoid blocking.
- The analyzer can hold a single image indefinitely without stalling the pipeline.
- If the application provides an executor which then blocks, the ImageAnalysis use case blocks.
- The default executor set internally behaves as a non-blocking executor.

**Bug Fixes**

- Fixed timeout issues waiting for 3A convergence when capturing images on devices with no auto-focus, auto exposure, and auto-whitebalance
- Fixed issue when rapidly taking pictures with ImageCapture. Fixes error: `java.lang.IllegalStateException: maxImages (2) has already been acquired`
- Fixed issue when `setLensFacing` was not called for a use case, resulting in `java.lang.IllegalArgumentException: Unable to get camera ID for use case`.
- Fixed issue where LEGACY device required specific aspect ratio as maximum JPEG resolution
- Fixed issue when backgrounding the app while camera is opening
- Fixed issue on API \< 25, removing error `checkAndUpdateEglState: invalid current EGLDisplay`
- Fixed issue when unbinding preview after enabling and starting extensions
- Build artifacts for camera-view and camera-extensions are now published as alpha versions

### Camera-Camera2 and Camera-Core Version 1.0.0-alpha03

July 2, 2019

`androidx.camera:camera-core:1.0.0-alpha03` and `androidx.camera:camera-camera2:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/57ec1f21171cea40e93847ce2776a6604ea47872..da18b8e358a305e4ae90edc548eb48927f037696/camera).

> [!NOTE]
> **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**API Changes**

- Added javadoc clarification for "target" in setTarget configuration calls

**Camera-Core**

- Fixed unconfigured Input/Output Surface crash on rapid open/close or bind/unbind
- Move to new Futures implementations
- Test fixes for more robust testing
- Core integration test now shows capture time for photos
- Developed internal compat class for Executors
- Timing test app capture images waits for previous to complete \& improved stability

**Extensions**

- Added versioning checks
- Additional test coverage - extension event callbacks
- Improvements for internally corresponding image and meta-data
- Fixes to mode switching in test app

### Camera-Camera2 and Camera-Core Version 1.0.0-alpha02

June 5, 2019

`androidx.camera:camera-core:1.0.0-alpha02` and `androidx.camera:camera-camera2:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/6851a37ae1cfd9a1b07eedfa073399c7ec02a054..57ec1f21171cea40e93847ce2776a6604ea47872/camera).

**Bug fixes**

- Fixed div by zero issue when using emulator
- Fixed NullPointerException/Surface Abandoned error occurring on some devices when quickly taking photos while unbinding and rebinding use cases rapidly.
- Fixed internal issue to ensure capture request updates affect all surfaces consistently
- Stability improvements when restarting use cases in new app instances
- Internal architecture changes to prepare for supporting executors in the API
- Additional Javadoc clarifications on CameraX class and lifecycle management
- Added instrumented testing for Antelope performance test app
- Remove need for '-keepattributes Signature' in app Proguard config

### Camera-Camera2 and Camera-Core 1.0.0-alpha01

May 7, 2019

`androidx.camera:camera-core:1.0.0-alpha01` and
`androidx.camera:camera-camera2:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/9b9b6c0ba6fd5a8f3726395a5ff9a03505240fd9/camera).

### Camera-Lifecycle Version 1.0.0-beta11

October 14, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta11` is released. [Version 1.0.0-beta11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/691e3a429902a0a3e087f28877e7cd5f668114fe..9a238add5b2df90db87d93473595ccd6911e297e/camera/camera-lifecycle)

**Bug Fixes**

- `<UseCase>.getTargetRotation()` will return `Surface.ROTATION_0` if called before being attached to a Camera instance unless a targetRotation has been set on the Builder or UseCase. ([I80fcd](https://android-review.googlesource.com/#/q/I80fcd8b33ce27e31fd3fc38b4f9b6e0a62b06bc5))

### Camera-Lifecycle Version 1.0.0-beta10

September 23, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta10` is released. [Version 1.0.0-beta10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ebe09b1cb65d62b65b01054fd9ecd055d653a22..691e3a429902a0a3e087f28877e7cd5f668114fe/camera/camera-lifecycle)

**Bug Fixes**

- Release to support [Camera-Core 1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/camera#camera-core-1.0.0-beta10)

### Camera-Lifecycle Version 1.0.0-beta09

September 16, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..9ebe09b1cb65d62b65b01054fd9ecd055d653a22/camera/camera-lifecycle)

### Camera-Lifecycle Version 1.0.0-beta08

August 19, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/camera/camera-lifecycle)

**Bug Fixes**

- Initialization should no longer crash when using a Context that does not return an Application object from `Context.getApplicationContext()`. ([I3d3c9](https://android-review.googlesource.com/#/q/I3d3c9880c24264e2b78f367777d675002f2126d3), [b/160817073](https://issuetracker.google.com/issues/160817073))

### Camera-Lifecycle Version 1.0.0-beta07

July 22, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/camera/camera-lifecycle)

### Camera-Lifecycle Version 1.0.0-beta06

June 24, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/camera/camera-lifecycle)

**API Changes**

- CameraX can now be configured with ProcessCameraProvider#configureInstance() before calling ProcessCameraProvider#getInstance(). This allows for customization of the CameraXConfig without requiring implementing CameraXConfig.Provider in the app's Application class. ([Ia1a8d](https://android-review.googlesource.com/#/q/Ia1a8d0b979e033d42ac06d1498395af07942d08f))

### Camera-Lifecycle Version 1.0.0-beta05

June 10, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-lifecycle)

**Bug Fixes**

- Fix the crash on app startup when initialising CameraX while phone is in Do Not Disturb mode. An `InitializationException` contains a `CameraUnavailableException` will be set to the `ListenableFuture` of the intialization result instead of crashing the application. ([I9909a](https://android-review.googlesource.com/#/q/I9909af08a8305fcf8e603d709d98b4488f1af69f), [b/149413835](https://issuetracker.google.com/issues/149413835))

### Camera-Lifecycle Version 1.0.0-beta04

May 27, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4319ecd6ebdd8a9f8600cc5b3d1aada1f716abac..c4d097f4335fe6b0268ee9a6d53df43615da0d90/camera/camera-lifecycle)

### Camera-Lifecycle Version 1.0.0-beta03

April 15, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..0e54727f73afedc58cfdda00fb123d6b50d3459d/camera/camera-lifecycle)

**Bug Fixes**

- Fixed regression from beta03 where calling `bindToLifecycle()` with zero `UseCase`s would cause a thrown exception. This prevented retrieval of a `Camera` without binding a `UseCase`.
- Fixes to support the release of `camera-core`

### Camera-Lifecycle Version 1.0.0-beta01

February 26, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c76d34916ab81f6fea02ba6e2d717243562bb24..401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e/camera/camera-lifecycle)

**Bug Fixes**

- Fixed documentation to note that when obtaining a `ProcessCameraProvider` during initialization, a default configuration is used and that extending `Application` is optional. ([I5e395](https://android-review.googlesource.com/#/q/I5e395330f4a5764d27025993251d45b262550491))

### Camera-Lifecycle Version 1.0.0-beta02

April 1, 2020

`androidx.camera:camera-lifecycle:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/camera/camera-lifecycle)

**Bug Fixes**

- Updated to support the bug fixes in the `camera-camera2:1.0.0-beta02` and `camera-core:1.0.0-beta02` artifacts.

### Camera-Lifecycle Version 1.0.0-alpha10

February 10, 2020

`androidx.camera:camera-lifecycle:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..1c76d34916ab81f6fea02ba6e2d717243562bb24/camera/camera-lifecycle).

**API Changes**

- Added `@MainThread` annotation to BindToLifecycle, unbind and unbindAll methods. ([I990d2](https://android-review.googlesource.com/#/q/I990d2d532492d177e392a4b45e9893a9b5d7b7fd))

### Camera-Lifecycle Version 1.0.0-alpha03

January 22, 2020

`androidx.camera:camera-lifecycle:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/94383d99a6ed372cd569bd5ab7d9aab5e0b056ba..0a3d894e8fe0217f1312fb163a89ad51bf15794e/camera/camera-lifecycle).

**Updates**

- Various fixes and updates to support Camera Core \& Camera2 changes.

### Camera-Lifecycle Version 1.0.0-alpha02

December 18, 2019

`androidx.camera:camera-lifecycle:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/camera/camera-lifecycle).

**Dependency changes**

- Updated to use `androidx.camera:camera-core:1.0.0-alpha08`.

### Camera-Lifecycle Version 1.0.0-alpha01

December 4, 2019

`androidx.camera:camera-lifecycle:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 of camera-lifecycle contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256/camera/camera-lifecycle)

**API notes**

- The camera-lifecycle artifact is added, providing `LifeCycleCameraProvider` interface, and an implementation called `ProcessCameraProvider` which provides many of the functions of the previous CameraX class in core and is obtained via a `getInstance()` method.
- Apps should include the camera-lifecycle library to use CameraX.
- See notes in the [camera-core](https://developer.android.com/jetpack/androidx/releases/camera#camera2-core-1.0.0-alpha07) section for how to perform initialization of CameraX using a `ProcessCameraProvider`.

## Camera-Extensions and Camera-View Version 1.0.0

### Version 1.0.0-alpha32

December 15, 2021

`androidx.camera:camera-extensions:1.0.0-alpha32` and `androidx.camera:camera-view:1.0.0-alpha32` are released. [Version 1.0.0-alpha32 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85f6fde74bd9e34dee843bce6a5acfba9b82c38e..f06551837636599d191fd581d56b68225440ed82/camera)

**API Changes**

- Removed unnecessary `@RequiresApi(21)` annotations from the inner classes/interfaces. ([I8e286](https://android-review.googlesource.com/#/q/I8e28678667e2f8a5e982d64674abe4c19b5e9155), [b/204917951](https://issuetracker.google.com/issues/204917951))
- Update api files for camera-extensions artifact. ([If683a](https://android-review.googlesource.com/#/q/If683a4952044f06bded3e87d6fa47d7aff2ad0e9), [b/161377155](https://issuetracker.google.com/issues/161377155))

**Bug Fixes**

- Disallow the app to enable extension modes when binding `VideoCapture`. CameraX Extensions only support `ImageCapture` and `Preview`. The `VideoCapture` can't be supported yet. If the app binds `VideoCapture` and enables any extension mode, an `IllegalArgumentException` will be thrown. ([I0d87b](https://android-review.googlesource.com/#/q/I0d87b67c82786d18e947bf031df71842be5fc8f5))
- `CameraSelector#filter` no longer throws an `IllegalArgumentException` when the result set is empty. ([I27804](https://android-review.googlesource.com/#/q/I27804168a78b11d74051d7b407762ed46c9f0f50))
- Renamed `ExtensionsManager#getInstance` API as `getInstanceAsync` because it returns `ListenableFuture`. The Async suffix of the function name can clearly present that it is an async function. ([I279d2](https://android-review.googlesource.com/#/q/I279d2908ecff343f5abbe9ef4f11c6a10cfcdf57))
- Remove resolution parameter from the `ExtensionsManager#getEstimatedCaptureLatencyRange` API since users can't know which sizes are supported for the `ImageCapture` use case and can't distinguish whether the returned latency information is for the maximum capture output size or the input resolution parameter. ([I74bb2](https://android-review.googlesource.com/#/q/I74bb23e0bcb340772f19a1d620282f4f3607576f))
- Move `CameraProvider` parameter of `ExtensionsManager` functions to the `getInstance()` API. So that the users don't need to input the `CameraProvider` parameter each time when calling the `ExtensionsManager` functions. ([Ic7e48](https://android-review.googlesource.com/#/q/Ic7e48c7404a14d0e8810f8c5da6e48067248f9d9))

### Version 1.0.0-alpha31

November 17, 2021

`androidx.camera:camera-extensions:1.0.0-alpha31` and `androidx.camera:camera-view:1.0.0-alpha31` are released. [Version 1.0.0-alpha31 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d51a5b31d004ef5b808e917260eb704d9e1c6bb2..ab8e6d320bb31b74ef87c504c9c5ac2b61d5ab98/camera)

**API Changes**

- Added CameraSelector#filter to the public API to filter a list of CameraInfos based on a CameraSelector. ([I105d0](https://android-review.googlesource.com/#/q/I105d07cb5a391b45045cbf06a429ab77e04fe040))

**Bug Fixes**

- Fixed a crash when switching extensions mode quickly on certain devices. ([Iebbef](https://android-review.googlesource.com/#/q/Iebbefe9bc76d4ef6769317264b3367771d4472ac))

### Version 1.0.0-alpha30

October 13, 2021

`androidx.camera:camera-extensions:1.0.0-alpha30` and `androidx.camera:camera-view:1.0.0-alpha30` are released. [Version 1.0.0-alpha30 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0329df5c3c75f45da38e69e594283dddfe1e82c7..d51a5b31d004ef5b808e917260eb704d9e1c6bb2/camera)

**API Changes**

- Added @RequiresApi(21) annotation to all CameraX classes and dropped minSdkVersion from AndroidManifest.xml. This will allow camera-core to be easily integrated into applications that have a minSdkVersion less than 21, but want to conditionally use code paths that rely on API 21 and higher. For any application with minSdkVersion 21 or higher, this change requires no action. ([Ie7f2e](https://android-review.googlesource.com/#/q/Ie7f2e23fa25ea401df4cddbe4d99651397cc0263), [b/200599470](https://issuetracker.google.com/issues/200599470))

**Bug Fixes**

- Fixed the AbstractMethodError issue which happens when proguard is enabled. ([Iae468](https://android-review.googlesource.com/#/q/Iae4688ef953751255c49eff8dfd205a6df226cbc), [b/201177844](https://issuetracker.google.com/issues/201177844))

### Version 1.0.0-alpha29

September 29, 2021

`androidx.camera:camera-extensions:1.0.0-alpha29` and `androidx.camera:camera-view:1.0.0-alpha29` are released. [Version 1.0.0-alpha29 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9e98cbf6f7926e3ccb8a11600bd631b238ed64c9..0329df5c3c75f45da38e69e594283dddfe1e82c7/camera)

**API Changes**

- ExperimentalUseCaseGroup annotation is removed now that the APIs are no longer experimental. ([I01ef5](https://android-review.googlesource.com/#/q/I01ef54912cd4ef540fe0389f785aa0bec5fc0783))
- remove `RotationProvider#removeAllListeners()`. Please use `RotationProvider#removeListener(...)` instead. ([Id9d4a](https://android-review.googlesource.com/#/q/Id9d4a5dabaa567eb8d660e6109eae049f1cbddb4))
- Updated the RotationReceiver class: changed set/clear Listener to add/remove/removeAll, remove the setListener variation that uses the main thread by default and added annotation of methods. ([Ib1669](https://android-review.googlesource.com/#/q/Ib16691ae0f4e13721cb3bebc127c404fdbe3e72b))

**Bug Fixes**

- Renamed ExtensionMode#BEAUTY to FACE_RETOUCH to correctly present what is done by the extension mode. ([I61f54](https://android-review.googlesource.com/#/q/I61f544ce058d1ee39722825fd95e7bb1e1ac6349), [b/198515274](https://issuetracker.google.com/issues/198515274))
- Fixed the issue that camera is closed unexpectedly when multiple CameraController and PreviewView are used in one Activity. ([Ibfd18](https://android-review.googlesource.com/#/q/Ibfd1842890b683ae3db639bf0cc4a2202110fe9f), [b/197539358](https://issuetracker.google.com/issues/197539358))

### Version 1.0.0-alpha28

August 18, 2021

`androidx.camera:camera-extensions:1.0.0-alpha28` and `androidx.camera:camera-view:1.0.0-alpha28` are released. [Version 1.0.0-alpha28 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86548c494687f4a4aadf3ebb2f724e410b378fcb..9e98cbf6f7926e3ccb8a11600bd631b238ed64c9/camera)

**API Changes**

- ExperimentalUseCaseGroupLifecycle annotation is removed now that the APIs are no longer experimental. ([I17b85](https://android-review.googlesource.com/#/q/I17b85c8bb3cd33f85bff02bcd3abaeeca1a39b15))
- refactored RotationListener and renamed it to RotationProvider. It continues to provide the same feature with slightly different API. ([Idffc5](https://android-review.googlesource.com/#/q/Idffc534a5f631e664003f51c4a401cad2c8905a0))
- rename TAP_TO_FOCUS_UNSUCCESSFUL to TAP_TO_FOCUS_NOT_FOCUSED and TAP_TO_FOCUS_SUCCESSFUL to TAP_TO_FOCUS_FOCUSED. Made OutputSize final ([I099fa](https://android-review.googlesource.com/#/q/I099fa41340ec664013a9e1658912d34e40799cc9))

**Bug Fixes**

- Removed deprecated `<EffectName><UseCase>Extender` classes, ExtensionsErrorListener and related ExtensionsManager APIs. ([I3b8c3](https://android-review.googlesource.com/#/q/I3b8c3a872fcf0b157a5fc86770ab2f7a118c2279))

### Version 1.0.0-alpha27

July 21, 2021

`androidx.camera:camera-extensions:1.0.0-alpha27` and `androidx.camera:camera-view:1.0.0-alpha27` are released. [Version 1.0.0-alpha27 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d042a98877f160baa61a8f88718b6a49b7a15d61..86548c494687f4a4aadf3ebb2f724e410b378fcb/camera)

**API Changes**

- Promoted the viewport API out of experimental. Remove the experimental annotation of the API. ([I717ea](https://android-review.googlesource.com/#/q/I717ea8239870d3a34816a7a8deec129a410b451e))
- Renamed `CoordinateTransform#getTransform` to `CoordinateTransform#transform` and update JavaDoc ([I864ae](https://android-review.googlesource.com/#/q/I864aefbb93188c78a44a67eac7cc533c81a6ce9a))

**Bug Fixes**

- Fixed `PreviewView PERFORMANCE` mode stretch issue when using it together with Compose UI. ([Ie1137](https://android-review.googlesource.com/#/q/Ie11371e57cb196552cef786c5567ddb60187fdca), [b/183864890](https://issuetracker.google.com/issues/183864890))

### Version 1.0.0-alpha26

June 30, 2021

`androidx.camera:camera-extensions:1.0.0-alpha26` and `androidx.camera:camera-view:1.0.0-alpha26` are released. [Version 1.0.0-alpha26 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5065c9982754d7b54b8577d64c4ff830375a4b0e..d042a98877f160baa61a8f88718b6a49b7a15d61/camera)

**API Changes**

- add a new method `CameraController#getTapToFocusState()` that exposes the latest tap-to-focus result. ([Iaccb0](https://android-review.googlesource.com/#/q/Iaccb06143b282c78d78b89c0801f76bc469ed54f))
- adding more camera-core features to CameraController: getters/setters for target aspect ratio, target resolution, capture mode, CameraControl and custom executors. ([Iea8f2](https://android-review.googlesource.com/#/q/Iea8f2b507fa9783e6b63d42ee5f47ec867c5151a))
- add a RotationReceiver class that receives Surface rotation changes. This can be used to set the target rotation when the device is in fixed portrait/landscape mode. ([Ib278f](https://android-review.googlesource.com/#/q/Ib278f5f6050370e6de8a492a22dd39c861155688))
- Exposed new getEstimatedCaptureLatencyRange public APIs in ExtensionsManager class. ([I6a8ec](https://android-review.googlesource.com/#/q/I6a8eccf43124afbec8d12c504b95afb6a60d2009))
- Deprecated ExtensionsErrorListener. Currently, this interface is only used to monitor whether a Preview or ImageCapture is lacking when enabling extension modes. CameraX will automatically add an extra Preview or ImageCapture to make the extension functions work well. After that, no error will be reported via this interface. ([I47d9e](https://android-review.googlesource.com/#/q/I47d9ecf70d107273ddfd3fb6b73dc7c64d4b2de9))
- Exposed new ExtensionsManager getInstance, isExtensionAvailable and getExtensionEnabledCameraSelector public APIs and deprecated old `<EffectName><UseCase>Extender` classes and related APIs. ([I329e6](https://android-review.googlesource.com/#/q/I329e64b47382cfe973c35f8a2b098932b5755732))

### Version 1.0.0-alpha25

June 2, 2021

`androidx.camera:camera-extensions:1.0.0-alpha25` and `androidx.camera:camera-view:1.0.0-alpha25` are released. [Version 1.0.0-alpha25 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/623bf2f080d4f35417d1af18aebdb72d29620275..5065c9982754d7b54b8577d64c4ff830375a4b0e/camera)

**API Changes**

- ExperimentalCameraFilter APIs are now out of experimental stage and become formal APIs. They can be used without annotated OptIn. ([I4bc94](https://android-review.googlesource.com/#/q/I4bc946c2ee431ea8ec67982a68a1181ebc2e335f))
- Add a utility that transforms coordinates between use cases. Example usage: transforming the coordinates detected in ImageAnalysis use case and highlight the detected object in preview. ([I63ab1](https://android-review.googlesource.com/#/q/I63ab10c16350de0e22d2722902987242943018c0), [b/137515129](https://issuetracker.google.com/issues/137515129))
- Removed `CameraView`. `CameraView` has been replaced by `CameraController`. Please see the [migration guide](https://medium.com/androiddevelopers/camerax-learn-how-to-use-cameracontroller-e3ed10fffecf) for how to migrate.: ([Id5005](https://android-review.googlesource.com/#/q/Id500507b3dd834da2207946a9982033f7f01feab))

**Bug Fixes**

- Replaced `ExperimentalUseCaseGroupLifecycle` with `ExperimentalUseCaseGroup`. ([I3b2ef](https://android-review.googlesource.com/#/q/I3b2ef21251f3831245722d9cf46edc52d406ddcf), [b/159033688](https://issuetracker.google.com/issues/159033688))

### Version 1.0.0-alpha24

April 21, 2021

`androidx.camera:camera-extensions:1.0.0-alpha24` and `androidx.camera:camera-view:1.0.0-alpha24` are released. [Version 1.0.0-alpha24 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe710f46552d00a05886b5490e9fc247aaf91529..623bf2f080d4f35417d1af18aebdb72d29620275/camera)

**Bug Fixes**

- Replaced annotation `@Experimental` with `@RequiresOptIn` to experimental APIs. For calling experimental APIs, use `androidx.annotation.OptIn` instead of deprecated `androidx.annotation.experimental.UseExperimental`. ([Iff226](https://android-review.googlesource.com/#/q/Iff2262a11208aa8c9292d650ba8d9ae0ed500b78))
- Fixed the PreviewView stretched issue on Samsung J5 Prime ([Ib10b6](https://android-review.googlesource.com/#/q/Ib10b69b60a289d76c065b8f559e9c820b6148fd3))

### Camera Extensions \& View Version 1.0.0-alpha23

March 24, 2021

`androidx.camera:camera-extensions:1.0.0-alpha23` and `androidx.camera:camera-view:1.0.0-alpha23` are released. [Version 1.0.0-alpha23 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..fe710f46552d00a05886b5490e9fc247aaf91529/camera)

**API Changes**

- CameraView is being deprecated. Please use `LifecycleCameraController` instead. See [the migration guide](https://medium.com/androiddevelopers/camerax-learn-how-to-use-cameracontroller-e3ed10fffecf) ([Idac2c](https://android-review.googlesource.com/#/q/Idac2c38fa3a2fcd57814ca9f5f4b48345337a629))
- Added FloatRange annotation to setLinearZoom() ([I69971](https://android-review.googlesource.com/#/q/I699718001b1c9f453d3bf4068717a7aeee4ea35e))

**Bug Fixes**

- Pinned camera-view dependencies to rely on 1.0.0 artifacts. Depending on camera-view will not longer cause gradle's dependency resolution to automatically upgrade camera-core, camera-camera2 and camera-lifecycle to the latest 1.1.0 artifacts, though camera-view is still compatible with those artifacts if they are explicitly set to use 1.1.0. ([Ic8fa1](https://android-review.googlesource.com/#/q/Ic8fa123684e2ab739b4a4b271f004c4d3f631bf5), [b/181599852](https://issuetracker.google.com/issues/181599852))
- Fixed Samsung A3 stretched preview in PreviewView. ([Iacb30](https://android-review.googlesource.com/#/q/Iacb30b0ff035d5a24ac221470a6815d96eca1725), [b/180121821](https://issuetracker.google.com/issues/180121821))
- Fixed the issue where if camera selector cannot be set before camera is initialized. ([Ic8bd0](https://android-review.googlesource.com/#/q/Ic8bd0b78548cd4ee6f77eb0fc82f7459c19a5b1e))

### Camera Extensions \& View Version 1.0.0-alpha22

February 24, 2021

`androidx.camera:camera-extensions:1.0.0-alpha22` and `androidx.camera:camera-view:1.0.0-alpha22` are released. [Version 1.0.0-alpha22 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ae5a49a113d2ec1fd217074bf0df7393533a620..5c90131a69042a6a3e13952e1da9e7ffc571c31d/camera)

**API Changes**

- add a CameraInfo getter to CameraController. ([Ib8138](https://android-review.googlesource.com/#/q/Ib8138c44ebc17164d3bf91d4dbc684a0fe7a2728), [b/178251727](https://issuetracker.google.com/issues/178251727))

**Bug Fixes**

- Fixed ExtensionsErrorListener to report errors when only Preview or ImageCapture is bound. ([I5ae39](https://android-review.googlesource.com/#/q/I5ae397bd5d04c635828e1604ac7d36dc2643add7))

### Camera Extensions \& View Version 1.0.0-alpha21

January 27, 2021

`androidx.camera:camera-extensions:1.0.0-alpha21` and `androidx.camera:camera-view:1.0.0-alpha21` are released. [Version 1.0.0-alpha21 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6aa34a2b3faad8227b3311a8e372e4ccf7eaf462..5ae5a49a113d2ec1fd217074bf0df7393533a620/camera)

Releasing to support other camera library artifacts.

### Camera Extensions \& View Version 1.0.0-alpha20

December 16, 2020

`androidx.camera:camera-extensions:1.0.0-alpha20` and `androidx.camera:camera-view:1.0.0-alpha20` are released. [Version 1.0.0-alpha20 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/369d39c56a955f4ee612581e26de38eb44ee02a8..6aa34a2b3faad8227b3311a8e372e4ccf7eaf462/camera)

Releasing to support other camera library artifacts.

### Camera-Extensions \& Camera-View Version 1.0.0-alpha19

November 11, 2020

`androidx.camera:camera-extensions:1.0.0-alpha19` and `androidx.camera:camera-view:1.0.0-alpha19` are released. [Version 1.0.0-alpha19 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9a238add5b2df90db87d93473595ccd6911e297e..369d39c56a955f4ee612581e26de38eb44ee02a8/camera)

**Bug Fixes**

- `@ExperimentalVideo` annotation was introduced to camera-view. This annotation marks APIs which expose experimental video functionality which is subject to change as the features are fully developed. Any method using these APIs should use the `@UseExperimental` annotation with `ExperimentalVideo` as the `markerClass`. ([I6d729](https://android-review.googlesource.com/#/q/I6d72945efd3d1a6c4d9724e905ec38c0aa1c9205))

### Camera-Extensions Version 1.0.0-alpha18

October 14, 2020

`androidx.camera:camera-extensions:1.0.0-alpha18` is released. [Version 1.0.0-alpha18 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/691e3a429902a0a3e087f28877e7cd5f668114fe..9a238add5b2df90db87d93473595ccd6911e297e/camera/camera-extensions)

**Bug Fixes**

- Improved the latency of CameraX initialization and bindToLifecycle ([I61dc5](https://android-review.googlesource.com/#/q/I61dc581555c6f665162b435bd13f0fd86c965993))
- `<UseCase>.getTargetRotation()` will return `Surface.ROTATION_0` if called before being attached to a Camera instance unless a targetRotation has been set on the Builder or UseCase. ([I80fcd](https://android-review.googlesource.com/#/q/I80fcd8b33ce27e31fd3fc38b4f9b6e0a62b06bc5))

### Camera-View Version 1.0.0-alpha18

October 14, 2020

`androidx.camera:camera-view:1.0.0-alpha18` is released. [Version 1.0.0-alpha18 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/691e3a429902a0a3e087f28877e7cd5f668114fe..9a238add5b2df90db87d93473595ccd6911e297e/camera/camera-view)

Releasing to support other camera library artifacts.

### Camera-Extensions Version 1.0.0-alpha17

September 23, 2020

`androidx.camera:camera-extensions:1.0.0-alpha17` is released. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ebe09b1cb65d62b65b01054fd9ecd055d653a22..691e3a429902a0a3e087f28877e7cd5f668114fe/camera/camera-extensions)

**Bug Fixes**

- Release to support [Camera-Core 1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/camera#camera-core-1.0.0-beta10)

### Camera-View Version 1.0.0-alpha17

September 23, 2020

`androidx.camera:camera-view:1.0.0-alpha17` is released. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ebe09b1cb65d62b65b01054fd9ecd055d653a22..691e3a429902a0a3e087f28877e7cd5f668114fe/camera/camera-view)

**Bug Fixes**

- Release to support [Camera-Core 1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/camera#camera-core-1.0.0-beta10)

### Camera-Extensions Version 1.0.0-alpha16

September 16, 2020

`androidx.camera:camera-extensions:1.0.0-alpha16` is released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..9ebe09b1cb65d62b65b01054fd9ecd055d653a22/camera/camera-extensions)

**Bug Fixes**

- Added method in `ExtensionsManager` to get an `Extensions` object which is used to enable and query extensions on Camera instances ([I4fb7e](https://android-review.googlesource.com/#/q/I4fb7e4e00d82939b25da09b2815c2a5458eea170))

### Camera-View Version 1.0.0-alpha16

September 16, 2020

`androidx.camera:camera-view:1.0.0-alpha16` is released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..9ebe09b1cb65d62b65b01054fd9ecd055d653a22/camera/camera-view)

**API Changes**

- Removed `PreviewView#setDeviceRotationForRemoteDisplayMode()` and `PreviewView#getDeviceRotationForRemoteDisplayMode()`. The two methods are for customizing preview rotation, when desired rotation is not display rotation, e.g. remote display. To handle the non-display preview rotation now, set the desired rotation with `Preview#setTargetRotation()` and the newly added `PreviewView#getViewPort(targetRotation)`. ([Ib62cc](https://android-review.googlesource.com/#/q/Ib62ccd85d93197642cc25b97c80f2d33815df10e))
- Renamed `createSurfaceProvider()` to `getSurfaceProvider()`. The method will always return the same instance of Preview.SurfaceProvider. ([Iff83c](https://android-review.googlesource.com/#/q/Iff83cd9c45539a84f465f080e1975432c3561ac4))

**Bug Fixes**

- Forced PreviewView to use TextureView if extension effect is enabled and the vendor library implementation needs to do a special process on the output surface. ([I0c3cc](https://android-review.googlesource.com/#/q/I0c3cc867847ec0f350119a8d05ace41c631d04de))
- Allow arbitrary target rotation for Preview. The transformation info is calculated and returned to user on-the-fly via a new `TranformationInfoListener` callback. ([I21470](https://android-review.googlesource.com/#/q/I214703dfb077891738666bfbfbe1b7187fe02461))

**Known Issues**

- In PreviewView, `OnClickListener#onClick()` is not invoked when the end user clicks PreviewView. The touch event is mistakenly consumed by PreviewView#onTouchEvent(). The issue will be fixed in the next release.
- The MeteringPoint obtained from `PreviewView#getMeteringPointFactory()` may be wrong if ViewPort is used with PreviewView.

### Camera-Extensions Version 1.0.0-alpha15

August 19, 2020

`androidx.camera:camera-extensions:1.0.0-alpha15` is released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/camera/camera-extensions)

**Bug Fixes**

- The `ExtensionsManager.init()` method now takes in a Context as a parameter instead of having 0 args. ([Ife754](https://android-review.googlesource.com/#/q/Ife7540101282319caff9bbe5e31165efe4205b64))
- Initialization should no longer crash when using a Context
  that does not return an Application object from `Context.getApplicationContext()`. ([I3d3c9](https://android-review.googlesource.com/#/q/I3d3c9880c24264e2b78f367777d675002f2126d3), [b/160817073](https://issuetracker.google.com/issues/160817073))

  ### Camera-View Version 1.0.0-alpha15

  August 19, 2020

`androidx.camera:camera-view:1.0.0-alpha15` is released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/camera/camera-view)

**Bug Fixes**

- `DisplayOrientedMeteringPointFactory` takes in a `CameraInfo` instance instead of a `CameraSelector` so there is a direct mapping to which Camera the factory will be generating points for. All classes which use `DisplayOrientedMeteringPointFactory` also take in a `CameraInfo` instance instead of `CameraSelector`. ([I400c1](https://android-review.googlesource.com/#/q/I400c16899037e29fd37d6cf6faaa87ed70188de1))
- Removed `TextureViewMeteringPointFactory`. `PreviewView` provides a public API (`createMeteringPointFactory()`) to create a metering point factory regardless of whether it's using a `TextureView` or `SurfaceView`. ([Ide693](https://android-review.googlesource.com/#/q/Ide693f9a3790f4a3ebe42541ffd0c129772280ff))
- rename PreviewView's `SURFACE_VIEW`/`TEXTURE_VIEW` implementation modes to `PERFORMANCE`/`COMPATIBLE`. `PERFORMANCE` is the old `SURFACE_VIEW` mode, and `COMPATIBLE` is the old `TEXTURE_VIEW` mode. ([I0edc2](https://android-review.googlesource.com/#/q/I0edc2675b5499722d62032559cc8d098a4e4428b))
- For image capture, overwrite the flip horizontal flag in metadata based on camera direction. ([I28499](https://android-review.googlesource.com/#/q/I28499bd3a46b0760d31fe100f40175552e6b6221))

### Camera-Extensions Version 1.0.0-alpha14

July 22, 2020

`androidx.camera:camera-extensions:1.0.0-alpha14` is released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/camera/camera-extensions)

### Camera-View Version 1.0.0-alpha14

July 22, 2020

`androidx.camera:camera-view:1.0.0-alpha14` is released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/camera/camera-view)

### Camera-Extensions Version 1.0.0-alpha13

June 24, 2020

`androidx.camera:camera-extensions:1.0.0-alpha13` is released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/camera/camera-extensions)

**Bug Fixes**

- Added experimental interfaces for filtering cameras by camera ID and CameraCharacteristics. ([I28f61](https://android-review.googlesource.com/#/q/I28f6110779ead8d6ed3177b86bd21ae5c27528c2))

### Camera-View Version 1.0.0-alpha13

June 24, 2020

`androidx.camera:camera-view:1.0.0-alpha13` is released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/camera/camera-view)

**Bug Fixes**

- CameraView no longer crashes with an IllegalArgumentException when binding to a LifecycleOwner whose Lifecycle transitions to a DESTROYED state shortly after being bound. Binding Lifecycles in a DESTROYED state will not attempt to open the camera. ([I7c2b8](https://android-review.googlesource.com/#/q/I7c2b8699881ff7d1abce7547b11d2ef107e5cce8))
- PreviewView StreamState is now available through CameraView.getPreviewStreamState() ([I21a2b](https://android-review.googlesource.com/#/q/I21a2be6dd610f0bb5720fa09b8c63396dfd5e374))

### Camera-Extensions Version 1.0.0-alpha12

June 10, 2020

`androidx.camera:camera-extensions:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-extensions)

**Bug Fixes**

- Fix the crash on app startup when initialising CameraX while phone is in Do Not Disturb mode. An `InitializationException` contains a `CameraUnavailableException` will be set to the `ListenableFuture` of the intialization result instead of crashing the application. ([I9909a](https://android-review.googlesource.com/#/q/I9909af08a8305fcf8e603d709d98b4488f1af69f), [b/149413835](https://issuetracker.google.com/issues/149413835))

### Camera-View Version 1.0.0-alpha12

June 10, 2020

`androidx.camera:camera-view:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-view)

**Bug Fixes**

- Add `PreviewView#getBitmap()` API which returns a Bitmap representation of the content displayed on the preview surface. ([I9b500](https://android-review.googlesource.com/#/q/I9b500504cc6a7ec7b067706b91117118b4d4f7ab), [b/157659818](https://issuetracker.google.com/issues/157659818))

### Camera-Extensions Version 1.0.0-alpha11

May 27, 2020

`androidx.camera:camera-extensions:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4319ecd6ebdd8a9f8600cc5b3d1aada1f716abac..c4d097f4335fe6b0268ee9a6d53df43615da0d90/camera/camera-extensions)

### Camera-View Version 1.0.0-alpha12

June 10, 2020

`androidx.camera:camera-view:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4d097f4335fe6b0268ee9a6d53df43615da0d90..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/camera/camera-view)

**New Features**

**API Changes**

**Bug Fixes**

- Add `PreviewView#getBitmap()` API which returns a Bitmap representation of the content displayed on the preview surface. ([I9b500](https://android-review.googlesource.com/#/q/I9b500504cc6a7ec7b067706b91117118b4d4f7ab), [b/157659818](https://issuetracker.google.com/issues/157659818))

### Camera-View Version 1.0.0-alpha11

May 27, 2020

`androidx.camera:camera-view:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4319ecd6ebdd8a9f8600cc5b3d1aada1f716abac..c4d097f4335fe6b0268ee9a6d53df43615da0d90/camera/camera-view)

**API Changes**

- Add `PreviewView#getPreviewStreamState` API which allows apps to observe if preview is streaming or not. When the PreviewView is in TEXTURE_VIEW mode, the STREAMING state also guarantees the preview image is visible. ([Ic0906](https://android-review.googlesource.com/#/q/Ic0906d25aa89b3b1a9abb02ca42e15f676b1c72f), [b/154652477](https://issuetracker.google.com/issues/154652477))
- Added `PreviewView#setDeviceRotationForRemoteDisplayMode()` API to provide device rotation for transform calculations if the application is running in remote display mode. ([I59b95](https://android-review.googlesource.com/#/q/I59b95cf5c484d110c1a4f4dd925da43d8d79da2b), [b/153514525](https://issuetracker.google.com/issues/153514525))

**Bug Fixes**

- Fixed the preview distortion issue on `FULL/LIMITED/LEVEL_3` cameras running android 7.0 and below. Forced use `ImplementationMode#TEXTURE_VIEW` mode when the android version is 7.0 or below. ([I83e30](https://android-review.googlesource.com/#/q/I83e303c1beb899d94a21f04b15008671f45b77ae), [b/155085307](https://issuetracker.google.com/issues/155085307))
- Removed the `CameraInfo` parameter from `PreviewView#createSurfaceProvider()`, `PreviewView` now internally retrieves it from the `SurfaceRequest`. ([If18f0](https://android-review.googlesource.com/#/q/If18f04ff541eb77ec58b216d201e04802ab14785), [b/154652477](https://issuetracker.google.com/issues/154652477))
- Fixed the VideoCapture's default aspect ratio to be 16:9 in CameraView. ([Ie6a7b](https://android-review.googlesource.com/#/q/Ie6a7bf344e6e08b25e47109557288b07187b3f7a), [b/153237864](https://issuetracker.google.com/issues/153237864))
- Fix `PreviewView` black screen issues when swiped out `Preview` fragment and then swiped back in ViewPager2. Also fixed the issue when `removeView(previewview)` and then `addView(previewView)`. ([Iab555](https://android-review.googlesource.com/#/q/Iab5555fa4bbcca4020ba0dc55135c15009d24908), [b/149877652](https://issuetracker.google.com/issues/149877652), [b/147354615](https://issuetracker.google.com/issues/147354615))
- Update the `CameraView#takePicture()` API to allow saving images to `Uri` and `OutputStream`. Update the test app to use `Uri` as the canonical example. ([Ia2459](https://android-review.googlesource.com/#/q/Ia2459465f2e960ab46409fceda367e5bc2678963), [b/153607583](https://issuetracker.google.com/issues/153607583))
- You can set PreviewView's scale type from a XML layout by setting the `ScaleType` attribute. ([I08565](https://android-review.googlesource.com/#/q/I085654addf7436f1da84a4d1851f1d72ab403a86), [b/153015659](https://issuetracker.google.com/issues/153015659))
- `CameraView.ScaleType` has been removed. Instead, use `PreviewView.ScaleType` to set/get a scale type with CameraView. ([Ia8974](https://android-review.googlesource.com/#/q/Ia8974a3c8c271ec1dfd2736c2e02d42b27f531c9), [b/153014831](https://issuetracker.google.com/issues/153014831))
- Give `PreviewView` a background color by default if it doesn't already have one. This prevents content behind it from being visible before the preview stream starts. ([I09fad](https://android-review.googlesource.com/#/q/I09fadd5ca9e187ff24c8195a6cfc7493ea74aabb))

### Camera-Extensions Version 1.0.0-alpha10

April 15, 2020

`androidx.camera:camera-extensions:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..0e54727f73afedc58cfdda00fb123d6b50d3459d/camera/camera-extensions)

**Bug Fixes**

- Fixes to support the release of Camera-Core

### Camera-View Version 1.0.0-alpha10

April 15, 2020

`androidx.camera:camera-view:1.0.0-alpha010` is released. [Version 1.0.0-alpha010 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..0e54727f73afedc58cfdda00fb123d6b50d3459d/camera/camera-view)

**Bug Fixes**

- Fixes a previous known issue where `PreviewView`'s surfaceView implementation wasn't working well on certain devices, and would cause the app to crash after resuming preview. ([I5ed6b](https://android-review.googlesource.com/#/q/I5ed6b7d6ee6a4d9aeb6643e06440597f9674191c))

### Camera-Extensions Version 1.0.0-alpha09

April 1, 2020

`androidx.camera:camera-extensions:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/camera/camera-extensions)

**Bug Fixes**

- Updated to support the bug fixes in the `camera-camera2:1.0.0-beta02`, `camera-core:1.0.0-beta02`, and `camera-lifecycle:1.0.0-beta02` artifacts

### Camera-View Version 1.0.0-alpha09

April 1, 2020
`androidx.camera:camera-view:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/camera/camera-view)

**Known Issues**

- Using `ImplementationMode.SURFACE_VIEW` with `PreviewView` may not work well on certain devices, this is because the `SurfaceView` used for preview invalidates its surface when the lifecycle of the window it's in is stopped, when it restarts, the camera is reopened and may attempt to resume preview before the `SurfaceView`'s surface is valid again. For now, you should use `ImplementationMode.TEXTURE_VIEW`.

**API Changes**

- Renamed `PreviewView.setImplementationMode()` to `PreviewView.setPreferredImplementationMode()`.
- Renamed `PreviewView.getImplementationMode()` to `PreviewView.getPreferredImplementationMode()`.
- Replaced `PreviewView.getSurfaceProvider()` by `PreviewView.createSurfaceProvider(CameraInfo)`, which takes a nullable `CameraInfo` instance used to optimize preview by using `ImplementationMode.SURFACE_VIEW` whenever possible. If a null instance is passed, or if you set the preferred implementation mode to `ImplementationMode.TEXTURE_VIEW`, `ImplementationMode.TEXTURE_VIEW` is used internally.
- The following code sample shows how a preview use case used to previously be used with PreviewView.

      preview.setSurfaceProvider(previewView.previewSurfaceProvider)
      cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)

  Right now, you can write the following:

      val camera = cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)
      previewView.preferredImplementationMode = ImplementationMode.TEXTURE_VIEW
      preview.setSurfaceProvider(previewView.createSurfaceProvider(camera.cameraInfo))

- The `@UiThread` annotation has been added to `PreviewView.getSurfaceProvider()`, meaning it must be called from the main thread. ([I192f3](https://android-review.googlesource.com/#/q/I192f3e4f57c2ddf64c2d56302b19dd3b8c9aa34d))

- Added `PreviewView.setScaleType()` which allows to set the scale type of the preview. It accepts one of the values in `PreviewView.ScaleType`, and defaults to `PreviewView.ScaleType.FILL_CENTER`.

- Added `PreviewView.getScaleType()`.

- Removed support for setting the implementation mode for `PreviewView` in a XML layout using the `implementationMode` attribute.

- Add `createMeteringPointFactory()` API to PreviewView to support converting (x, y) in `PreviewView` to `MeteringPoint`. ([Ib36d7](https://android-review.googlesource.com/#/q/Ib36d78607ffcea891b5ec24b20f66e5e0eb42fc0))

**Bug Fixes**

- Fixed cases where an incorrect preview is displayed after `PreviewView`'s size changes. ([I71101](https://android-review.googlesource.com/#/q/I711010b55949fb8cedb28458375954aff87f6149))

### Camera-Extensions Version 1.0.0-alpha08

February 26, 2020

`androidx.camera:camera-extensions:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c76d34916ab81f6fea02ba6e2d717243562bb24..401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e/camera/camera-extensions)

### Camera-View Version 1.0.0-alpha08

February 26, 2020

`androidx.camera:camera-view:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1c76d34916ab81f6fea02ba6e2d717243562bb24..401dc9727e2eb1b5b89c0fbc4b7e1df77b2df75e/camera/camera-view)

**Bug Fixes**

- Replaced the `ListenableFuture` on `SurfaceRequest.provideSurface()` with an `Executor` and `Callback`. This simplifies the API by no longer requiring handling of exceptions on `provideSurface()` and enforces that the `provideSurface()` callback cannot be cancelled. This is to prevent crashes on older devices caused by prematurely releasing surfaces. The `SurfaceRequest.Result` object is now used for tracking how a `SurfaceRequest` uses the provided `Surface`. ([I7854b](https://android-review.googlesource.com/#/q/I7854b0a3c01c2e11030d18bf99eb4539207267e3))
- Renamed `SurfaceRequest.setSurface(Surface)` to `SurfaceRequest.provideSurface(Surface)` and `SurfaceRequest.setWillNotComplete()` to `SurfaceRequest.willNotProvideSurface()`. ([I224fe](https://android-review.googlesource.com/#/q/I224fe088094eed4fb9e8a8ff83b7fa2417c6f36d))
- Fixed initialization of app variants with ProGuard enabled by preserving the flag that sets the default `CameraXConfig` provider. ([I2d6c1](https://android-review.googlesource.com/#/q/I2d6c1134e10e9d9add5e61d32efb14b06f2ae7ac))

### Camera-Extensions Version 1.0.0-alpha07

February 10, 2020

`androidx.camera:camera-extensions:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..1c76d34916ab81f6fea02ba6e2d717243562bb24/camera/camera-extensions).

**Bug Fixes**

- The arguments that were previously passed in `ImageCapture.OnImageSavedCallback.onError()` and `ImageCapture.OnImageCapturedCallback.onError()` have now been replaced by a single argument `ImageCaptureException`, which still contains all the information that was previously passed.
- The file argument previously passed in `ImageCapture.OnImageSavedCallback.onImageSaved()` has been removed. ([I750d2](https://android-review.googlesource.com/#/q/I750d258b4d532ac99d7a49c1c7800dc2edea3c43))

### Camera-View Version 1.0.0-alpha07

February 10, 2020

`androidx.camera:camera-view:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..1c76d34916ab81f6fea02ba6e2d717243562bb24/camera/camera-view).

**API Changes**

- `PreviewView`'s `TextureView` implementation now sets the `TextureView`'s size to the camera sensor output size before scaling it to fill its parent `PreviewView`. If you want the camera preview to fill an entire part of the UI (the whole screen for instance), you should not set the `PreviewView`'s size to a fixed value, or have it wrap its content (by using the attribute "`wrap_content`" for example), this may result in the camera preview only filling part of the `PreviewView` (if the camera sensor output size is smaller). Instead, you should set the `PreviewView` as big as its parent (by using the attribute "`match_parent`" for example). ([1204869](https://android-review.googlesource.com/c/platform/frameworks/support/+/1204869/))

**Bug Fixes**

- Updated `ImageCapture` to allow saving images to `Uri` and `OutputStream`. Combined overloaded `takePicture` methods into one. Updated test app to use `Uri` as the canonical example. ([Ia3bec](https://android-review.googlesource.com/#/q/Ia3becf13029c367e7525d1b110f89bd4a06833a9))
- `Preview.PreviewSurfaceProvider` has been renamed to `Preview.SurfaceProvider`. `SurfaceProvider`s no longer require developers to create their own `ListenableFuture`, and providing a `Surface` is now done through a new `SurfaceRequest` object. The `Preview.getPreviewSurfaceProvider()` method has been removed due to its potential for misuse when `Preview` is paired with other classes such as `PreviewView`. ([I20105](https://android-review.googlesource.com/#/q/I2010570526c2336250d873c681a5c00d8420938e))
- The arguments that were previously passed in `ImageCapture.OnImageSavedCallback.onError()` and `ImageCapture.OnImageCapturedCallback.onError()` have now been replaced by a single argument `ImageCaptureException`, which still contains all the information that was previously passed.
- The file argument previously passed in `ImageCapture.OnImageSavedCallback.onImageSaved()` has been removed. ([I750d2](https://android-review.googlesource.com/#/q/I750d258b4d532ac99d7a49c1c7800dc2edea3c43))
- API updated, with `getZoomRatio()`, `getMaxZoomRatio()`, `getMinZoomRatio()`, and `getLinearZoom()` methods of `CameraInfo` merging into `getZoomState()` which returns a `ZoomState` instance. ([Ib19fe](https://android-review.googlesource.com/#/q/Ib19feb7377aac17623e8d3edbde1dd39b25b31b9))

### Camera-Extensions Version 1.0.0-alpha06

January 22, 2020

`androidx.camera:camera-extensions:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/94383d99a6ed372cd569bd5ab7d9aab5e0b056ba..0a3d894e8fe0217f1312fb163a89ad51bf15794e/camera/camera-extensions).

**Updates**

- Various fixes and updates to support Camera Core \& Camera2 changes.

### Camera-View Version 1.0.0-alpha06

January 22, 2020

`androidx.camera:camera-view:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/94383d99a6ed372cd569bd5ab7d9aab5e0b056ba..0a3d894e8fe0217f1312fb163a89ad51bf15794e/camera/camera-view).

**Updates**

- Various fixes and updates to support Camera Core \& Camera2 changes.

### Camera-Extensions Version 1.0.0-alpha05

December 18, 2019

`androidx.camera:camera-extensions:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/camera/camera-extensions).

**Bug Fixes**

- Updated to match the internal Camera Core APIs.

### Camera-View Version 1.0.0-alpha05

December 18, 2019

`androidx.camera:camera-view:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb7a5cbd2e20d3bf45cae63fea8436818576256..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/camera/camera-view).

**Known Issues**

- The aspect ratio may be incorrect when using PreviewView ([b/146215202](https://issuetracker.google.com/146215202)).

**New Features**

- Implemented a new class called `PreviewView.TextureViewImplementation` that syncs the SurfaceTexture's lifecycle with the camera's usage of the TextureView's surface.

### Camera-Extensions Version 1.0.0-alpha04

December 4, 2019

`androidx.camera:camera-extensions:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 of camera-extensions contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c92e554b976570c612bad53b16f5aa7591713593..4cb7a5cbd2e20d3bf45cae63fea8436818576256/camera/camera-extensions)

**API changes**

- Checking for the availability and enabling of an extension now takes in a `CameraSelector` as an input parameter. This needs to be the same `CameraSelector` that is used for binding the use case.

      val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
      val builder = ImageCapture.Builder()
      val bokehImageCaptureExtender = BokehImageCaptureExtender.create(builder)
      if (bokehImageCaptureExtender.isExtensionAvailable(cameraSelector)) {
          bokehImageCaptureExtender.enableExtension(cameraSelector)
      }
      val imageCapture = builder.build()
      mCameraProvider?.bindToLifecycle(this, cameraSelector, imageCapture)

- You must initialize extensions before using the extension library.

      val availability = ExtensionsManager.init()
      Futures.addCallback<ExtensionsManager.ExtensionsAvailability>(
         availability,
         object : FutureCallback<ExtensionsManager.ExtensionsAvailability> {
             override fun onSuccess(availability: ExtensionsManager.ExtensionsAvailability?) {
                 // Ready to make extensions calls
             }
             override fun onFailure(throwable: Throwable) {
                 // Extensions could not be initialized
             }
         },
         Executors.newSingleThreadExecutor()
      )

### Camera-View Version 1.0.0-alpha04

December 4, 2019

`androidx.camera:camera-view:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 of camera-view contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4606c6c990d6924534ff6c5c525648bd0877d551..4cb7a5cbd2e20d3bf45cae63fea8436818576256/camera/camera-view)

**API changes**

- A `PreviewView` class is provided for easily displaying the output from the Preview use case in an application.
- `PreviewView` can be included in the layout:

      <androidx.camera.view.PreviewView
        android:id="@+id/preview_view"
        ... />

- `PreviewView` provides a `PreviewSurfaceProvider` to easily connect a Preview use case

      preview.setPreviewSurfaceProvider(previewView.previewSurfaceProvider)

- "`ZoomLevel`" is now "`ZoomRatio`" in API-naming

- Some method parameters have changed nullability

### Camera-Extensions and Camera-View Version 1.0.0-alpha03

October 9, 2019

`androidx.camera:camera-extensions:1.0.0-alpha03` and `androidx.camera:camera-view:1.0.0-alpha03` are released. These are the [commits included in `camera-extensions:1.0.0-alpha03`](https://android.googlesource.com/platform/frameworks/support/+log/90f3b785f74ef777d901295e947aa9c6d024afca..c92e554b976570c612bad53b16f5aa7591713593/camera/camera-extensions) and these are the [commits included in `camera-view:1.0.0-alpha03`](https://android.googlesource.com/platform/frameworks/support/+log/90f3b785f74ef777d901295e947aa9c6d024afca..4606c6c990d6924534ff6c5c525648bd0877d551/camera/camera-view).

**New Features**

- Added Context initializer for extensions. Extensions version incremented to 1.1.0

### Camera-Extensions and Camera-View Version 1.0.0-alpha02

September 5, 2019

`androidx.camera:camera-extensions:1.0.0-alpha02` and
`androidx.camera:camera-view:1.0.0-alpha02` are released. These are the
[commits included in camera-extensions:1.0.0-alpha02](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..90f3b785f74ef777d901295e947aa9c6d024afca/camera/camera-extensions)
and these are the [commits included
camera-view:1.0.0-alpha02](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..90f3b785f74ef777d901295e947aa9c6d024afca/camera/camera-view).

- Added tests to verify `PreviewImageProcessorImpl` has correctly implemented timestamps.
- Fix `ExtensionTest` test failure on Nexus 5 (API level 21) and ensure preview is available.

### Camera-Extensions and Camera-View Version 1.0.0-alpha01

August 7, 2019

`androidx.camera:camera-extensions:1.0.0-alpha01` and
`androidx.camera:camera-view:1.0.0-alpha01` are released.
These are the
[commits included in camera-extensions:1.0.0-alpha01](https://android.googlesource.com/platform/frameworks/support/+log/da18b8e358a305e4ae90edc548eb48927f037696..6bc5fc2e82861585a6f28128dee9abbbe2e18591/camera)
and these are the [commits included
camera-view:1.0.0-alpha01](https://android.googlesource.com/platform/frameworks/support/+log/da18b8e358a305e4ae90edc548eb48927f037696..6bc5fc2e82861585a6f28128dee9abbbe2e18591/camera)

- New library for future Camera Extensions for accessing effects on supported devices. This library is a work in progress.
- New Camera View class. This library is a work in progress.