---
title: https://developer.android.com/jetpack/androidx/releases/xr-runtime
url: https://developer.android.com/jetpack/androidx/releases/xr-runtime
source: md.txt
---

# XR Runtime

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore)

Start your custom AR or 3D session with our native runtime.


| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 15, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/xr-runtime#1.0.0-beta01) | - |


## Declaring dependencies


To add a dependency on XR runtime, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-beta01"

    // Use in environments that do not support OpenXR
    testImplementation "androidx.xr.runtime:runtime-testing:1.0.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-beta01")

    // Use in environments that do not support OpenXR
    testImplementation("androidx.xr.runtime:runtime-testing:1.0.0-beta01")
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

#### Version 1.0.0-beta01

July 15, 2026

`androidx.xr.runtime:runtime-*:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a3db25aa1e59086c8e0c4d2eb2f2e9186211080b..504b2b04fe6292c47f04ecf1bd55f84634e669b6/xr/runtime).

**API Changes**

- Added `SessionTestRule` to runtime-testing. This API ([I672bc](https://android-review.googlesource.com/#/q/I672bcc6df88df4552c7dc8c361dc3fe06a6a6964), [b/516876144](https://issuetracker.google.com/issues/516876144))
- Converted Session.create to a suspend function. ([I5d27f](https://android-review.googlesource.com/#/q/I5d27fd6399fc5fe35f28ddf9c0c488a12eb23115))
- Added support for the lifecycle to the `XrDeviceTestRule` ([I2319c](https://android-review.googlesource.com/#/q/I2319cc1221cfd829ff654bf8b56f89019b7f4b63), [b/512140272](https://issuetracker.google.com/issues/512140272))
- Removed unused `ExperimentalXrDeviceLifecycleApi` experimental opt-in annotation. ([I46d95](https://android-review.googlesource.com/#/q/I46d957c80e875d3491e1aac92946ceb3a88c121f))
- Add specialized overrides of `toString()` for a number of runtime types. These types are intended to provide additional information to developers for debugging purposes and are not intended to be used in production or shipped applications.

**Bug Fixes**

- Fixed Pose.`fromLookAt` forward direction alignment, corrected scale extraction in Matrix3, and prevented numerical `NaNs` in normalization, axis-angle conversion, and `angleBetween` calculations. ([I7a3b5](https://android-review.googlesource.com/#/q/I7a3b54467df0110d16f98b0cad6d2e6c9a6edb68), [b/367780918](https://issuetracker.google.com/issues/367780918))

#### Version 1.0.0-alpha15

June 17, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha15` is released. Version 1.0.0-alpha15 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2cf81ac79d4a2cf6fe7d512d38c94b6b01ee384..a3db25aa1e59086c8e0c4d2eb2f2e9186211080b/xr/runtime).

**API Changes**

- Added test API for `isProjectedServiceAvailable()` ([I44ba1](https://android-review.googlesource.com/#/q/I44ba170691c5102f8bbe9d7a46d1b61ddc790056))
- Exposed `DeviceTrackingMode.INERTIAL` as a public experimental API under the new `@ExperimentalInertialTrackingApi` annotation. ([Ic3df3](https://android-review.googlesource.com/#/q/Ic3df319bd6944fe290e373d8581d9c397f3f689f))
- Added `Config.Builder`. Apps can create custom configurations by calling setter functions on the builder object and then calling `Builder.build`. ([I13142](https://android-review.googlesource.com/#/q/I13142e0a11c7a5f1d9db365d97c01f9b7f1b69b7))
- `androidx.xr.runtime.FieldOfView` has been removed. Apps should use `androidx.xr.runtime.math.FieldOfView` instead. ([I621ef](https://android-review.googlesource.com/#/q/I621ef48eb638845dfb6a36193722efcf27357e48))
- `Session.create` is now required to be ran on a `@WorkerThread`. ([I2169e](https://android-review.googlesource.com/#/q/I2169e3575fed27264c837e3fc2256fca090ec515))
- Added `isProjectedServiceAvailable()` to the `XrDevice` ([I507e9](https://android-review.googlesource.com/#/q/I507e9d75d9f33b4e53c6b07cc91ecf7a8662dd01))
- Renaming `DeviceTrackingMode.SPATIAL_LAST_KNOWN` to `DeviceTrackingMode.SPATIAL` and `DeviceTrackingMode.INERTIAL_LAST_KNOWN` to `DeviceTrackingMode.INERTIAL` ([I96f8b](https://android-review.googlesource.com/#/q/I96f8bd1ce16f796985e53385804cef8d443d6e9f))
- `Vector3.angleBetween` and `Vector4.angleBetween` now return degrees rather than radians. ([Ica8bc](https://android-review.googlesource.com/#/q/Ica8bce542cce3ff43c77ee428e7ac846e096aa8c))
- Added `QrCode` API ([Ia0bbe](https://android-review.googlesource.com/#/q/Ia0bbe0444195922efdf6ebd76ee91b44a600e3ee))

### Version 1.0.0-alpha14

May 19, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha14` is released. Version 1.0.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f0d77f65175480acff2718b61a7c34c502a1802e..e2cf81ac79d4a2cf6fe7d512d38c94b6b01ee384/xr/runtime).

**API Changes**

- Deprecating `GeospatialMode.VPS_AND_GPS` in favor of `GeospatialMode.SPATIAL` and introducing a new lower-power tracking mode, `GeospatialMode.INERTIAL`, which uses only IMU and GPS. ([I1e6cd](https://android-review.googlesource.com/#/q/I1e6cde5e98a05f7e52c6c107d596a004d8158022))
- Removes deprecation tag on `androidx.xr.runtime.FieldOfView`. Makes `androidx.xr.runtime.math.FieldOfView` a type aliaas of `androidx.xr.runtime.FieldOfView` in preparation for the latter's removal in the next release. Clients must migrate to the `androidx.xr.runtime.math` version wherever they are using the `androidx.xr.runtime` version. ([I6ce15](https://android-review.googlesource.com/#/q/I6ce156340a5b990016ed60d330e0e673d799246e))
- Added the `PreviewProjectedApi` annotation ([Ic49f6](https://android-review.googlesource.com/#/q/Ic49f60a65d71050f38b5c4df4eaafc4b6dd010c6))
- Removed `AugmentedObjectCategory.allSupported` ([I08656](https://android-review.googlesource.com/#/q/I0865696cf9a8f07b6a4557ed6642006af685cb4e))
- Adding APIs in `XrDevice` for determining device support for hand tracking, eye tracking, depth estimation, geospatial, and rendering. ([I00696](https://android-review.googlesource.com/#/q/I006964e70e8301fffa08cd470a6f4460995b5bec))
- `Session.getNativeData` has been replaced with `XrDevice.getNativeInstanceData` and `Session.getNativeSessionData`. ([Ieb077](https://android-review.googlesource.com/#/q/Ieb07742f2bb95f097afc598f22d273e8f464f74b))
- Annotated `DeviceTrackingMode.INERTIAL_LAST_KNOWN` with `@PreviewSpatialApi`. ([I99868](https://android-review.googlesource.com/#/q/I99868a9f3894e87040b453f109d3a8efb90b4a41))
- Added `XrDeviceTestRule` for its use in unit tests. ([I87584](https://android-review.googlesource.com/#/q/I87584e28a51edfc2b5832e0ed4e533a8ca73f55d))
- Adding `CATEGORY_XR_PROJECTED_LAUNCHER`, this constant is used in the Manifest file to indicate the activity should be discovered as a launcher by the system. ([Ia3069](https://android-review.googlesource.com/#/q/Ia306924431e6681173d177f95c63195e8510a8f6))

**External Contribution**

- Add `AugmentedImageMode` to the `Config` API ([I0cf09](https://android-review.googlesource.com/#/q/I0cf0953c17e691b1501e08182b3d027efa891753))

### Version 1.0.0-alpha13

May 06, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha13` is released. Version 1.0.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7913eae74f4112f4fbb22ea1a5037cd8b0e73f0..f0d77f65175480acff2718b61a7c34c502a1802e/xr/runtime).

**API Changes**

- `TrackingState` and `VpsAvailabilityResult` have moved to the `androidx.xr.arcore package`, and the types in `androidx.xr.runtime` are now deprecated. ([Ic7930](https://android-review.googlesource.com/#/q/Ic79303427f1301f722efb7f624033f9f11b49544), [b/480462213](https://issuetracker.google.com/issues/480462213))
- `Session.getNativeData()` is now defined the `xr:runtime:runtime` module and provides \[`nativeFunctionTablePointer`\] for OpenXR-backed runtimes. ([Ifa862](https://android-review.googlesource.com/#/q/Ifa8620c5df2e78985bb4c6ea36461e2c5ae7c20f))
- Moved `NativeData` API to `xr:runtime:runtime` library. ([I87954](https://android-review.googlesource.com/#/q/I87954b9811c11c019f9a256dacd11c352b79cc56), [b/494251500](https://issuetracker.google.com/issues/494251500))
- `Session.create` and `Session.configure` are now non-exhaustive and require else clauses in when statements. ([I9885e](https://android-review.googlesource.com/#/q/I9885e2b6bdb6da77988d04402f0df73380f6807a), [b/495805998](https://issuetracker.google.com/issues/495805998), [b/495805998](https://issuetracker.google.com/issues/495805998))
- `androidx.xr.runtime.FieldOfView` has been deprecated. Use `androidx.xr.runtime.math.FieldOfView` instead. ([Ia01a0](https://android-review.googlesource.com/#/q/Ia01a0ac228dc4a93c1bb2979b26d4f400be4fe99), [b/480233045](https://issuetracker.google.com/issues/480233045))
- `Matrix4.pose` has been renamed to `Matrix4.toPose()`. The pose property is now deprecated. ([I329b4](https://android-review.googlesource.com/#/q/I329b4d05fc0757359864a2762f76422d2154c37e), [b/493383490](https://issuetracker.google.com/issues/493383490))
- Added the `XrServiceAvailability` API ([If379e](https://android-review.googlesource.com/#/q/If379eefa6e058cd4c90c7efc5e27787e79350ecc), [b/493558010](https://issuetracker.google.com/issues/493558010))
- Added the `ExperimentalXrServiceAvailabilityApi` annotation ([Icab49](https://android-review.googlesource.com/#/q/Icab49610d9967f0c3c1e34b3ef25872bdceb42ea), [b/491069725](https://issuetracker.google.com/issues/491069725))
- Remove the suffix for `@PreviewSpatialApi` ([If5242](https://android-review.googlesource.com/#/q/If5242d7000a9514c7d0952e39f9eb170d534ccfd), [b/491939311](https://issuetracker.google.com/issues/491939311))
- Renamed `DeviceTrackingMode.LAST_KNOWN` to `SPATIAL_LAST_KNOWN` (with a deprecated fallback), added `INERTIAL_LAST_KNOWN` for 3DoF tracking, and added `TRACKING_DEGRADED` to `TrackingState`. ([Ie661c](https://android-review.googlesource.com/#/q/Ie661cfd441521987dcebd7e1fd1e7cfc3ef5ab9d), [b/445466590](https://issuetracker.google.com/issues/445466590))
- Added `XrLog` API. Set `XrLog.isEnabled` to `true` to enable logging in JetpackXR, and use \[`XrLog.Level`\] to set the log level. ([I76a1f](https://android-review.googlesource.com/#/q/I76a1f066b96ab6f07016d57c7e8e83518cb67de6), [b/463460895](https://issuetracker.google.com/issues/463460895), [b/487378441](https://issuetracker.google.com/issues/487378441))
- Adding `DISPLAY_CATEGORY_XR_PROJECTED`, this constant is used in the Manifest file to indicate the activity is meant for a XR projected display ([I26d8b](https://android-review.googlesource.com/#/q/I26d8b14946a4f523044486b1ad56f860d0423363))

### Version 1.0.0-alpha12

March 25, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6671838a2686d9e8b03e38681b78ebb63031c549..e7913eae74f4112f4fbb22ea1a5037cd8b0e73f0/xr/runtime).

**API Changes**

- Changed `Config.augmentedObjectCategories` from a List to a Set, ([I25a64](https://android-review.googlesource.com/#/q/I25a64eb05fa641c80185dbff62b7d140a2d4cac0), [b/487376359](https://issuetracker.google.com/issues/487376359))
- Removed `unscaledGravityAlignedActivitySpace` flag from `Session.create`. `ActivitySpace` is always unscaled and gravity-aligned now. ([If6f11](https://android-review.googlesource.com/#/q/If6f11877880f649ecf7a4844db3e809064cc10fb), [b/458173423](https://issuetracker.google.com/issues/458173423))
- Added `Session.create` overload to allow passing an Android Context for resource-scoping. ([I7d3fe](https://android-review.googlesource.com/#/q/I7d3fec251fb7d1a415a812286d71adbf23a910b2), [b/415805990](https://issuetracker.google.com/issues/415805990), [b/477386334](https://issuetracker.google.com/issues/477386334))
- Added `JvmOverloads` to `FloatSize2d.to3d`, `Matrix3.copy`, and `Matrix4.copy` ([I69586](https://android-review.googlesource.com/#/q/I695860cf9d75d118905cd01123a8b977b806fa61), [b/481371562](https://issuetracker.google.com/issues/481371562))
- Added ability to set categories for `AugmentedObject` tracking in the Config ([I1f6e4](https://android-review.googlesource.com/#/q/I1f6e4e634a511ab591802327ce3d45da6a3a0510), [b/480220930](https://issuetracker.google.com/issues/480220930))
- Added `xr:runtime:runtime-interfaces` module. ([I52ac6](https://android-review.googlesource.com/#/q/I52ac614c450be6b8a36e75611face78945f14667), [b/461561664](https://issuetracker.google.com/issues/461561664))

### Version 1.0.0-alpha11

February 25, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6d802bc724002ae38712673fb300c314f88fdd9e..6671838a2686d9e8b03e38681b78ebb63031c549/xr/runtime).

**API Changes**

- Restricted `ConfigMode` interface to internal use ([Ibfb87](https://android-review.googlesource.com/#/q/Ibfb8747c911fd6166d0310ad2f3b17378d20a145))
- Moved `androidx.xr.runtime.Config.GeospatialMode` to package level ([Ibe682](https://android-review.googlesource.com/#/q/Ibe68273f6c15f39a84ecac823b11e163da8eb8fe))
- Moved `androidx.xr.runtime.Config.FaceTrackingMode` to package level ([Iac501](https://android-review.googlesource.com/#/q/Iac5018bff5fc2c1467b0d9371c3d3b85fc7ca825))
- Moved `androidx.xr.runtime.Config.AnchorPersistenceMode` to package level ([I0360f](https://android-review.googlesource.com/#/q/I0360f5c8efe16dd8acf0b3a065bda0b366bba079))
- Moved `androidx.xr.runtime.Config.DepthEstimationMode` to package level ([I7e3e9](https://android-review.googlesource.com/#/q/I7e3e9e44d4d7e3a662108eab0b1afa977363e983))
- Moved `androidx.xr.runtime.Config.DeviceTrackingMode` to package level ([I3aacd](https://android-review.googlesource.com/#/q/I3aacdbeb3cc159286471c970557920aab9e0277a))
- Moved `androidx.xr.runtime.Config.HandTrackingMode` to package level ([I658f3](https://android-review.googlesource.com/#/q/I658f3ac7f134fee3faa9279b2a29542f2bc42078))
- Moved `androidx.xr.runtime.Config.PlaneTrackingMode` to package level ([Ia251b](https://android-review.googlesource.com/#/q/Ia251b2c84696209bf4558ad9d3a8a07aef234288))
- Moved `androidx.xr.runtime.XrDevice.DisplayBlendMode` to package level ([I6f333](https://android-review.googlesource.com/#/q/I6f333283c6e1d92a86e3616567d78f0a391193dc))
- Added a factory method to create an `XrDevice` using a Context, Session and a `CoroutineContext`. ([I139c5](https://android-review.googlesource.com/#/q/I139c5f1ec5f3ecd64f1a6fe3ffb51e9139c1c1b8))
- Added `SpatialApiVersionHelper` to help query the runtime version of Android XR available on the platform. ([I7c53c](https://android-review.googlesource.com/#/q/I7c53cc27a8c3e014ecf9144d2688830a7013b3cc))
- Added `xr:runtime:runtime-openxr` module ([Ib42ea](https://android-review.googlesource.com/#/q/Ib42eae999da3aaf37b8e45f0594d43d0ff0bc0b3))

### Version 1.0.0-alpha10

January 28, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5dd54df7c7f82386d2da53e696750df346d47550..6d802bc724002ae38712673fb300c314f88fdd9e/xr/runtime).

**API Changes**

- `ConfigMode.HeadTrackingMode` is replaced with `ConfigMode.DeviceTrackingMode`. ([le273e](https://android-review.googlesource.com/#/q/Ie273ef58cbd8187d33e91b344d37107187002990), [b/467150206](https://issuetracker.google.com/issues/467150206))
- Removed Quaternion's `toNormalized`, `times(float)`, `div(float)` methods. These methods are redundant given that all Quaternions are normalized at construction time and given that the class is immutable. ([l558fc](https://android-review.googlesource.com/#/q/I558fcff3211fc4a9122262b548936b2b877735e4), [b/460210457](https://issuetracker.google.com/issues/460210457))

**Bug Fixes**

- Added documentation to `Session.create` that illustrates how to avoid creating a session on the application's main thread. ([le5554](https://android-review.googlesource.com/#/q/Ie5554bace05cf2c51ee824d381fdff8f676500fa), [b/463687170](https://issuetracker.google.com/issues/463687170))
- Prevented applications from creating a `BoundingBox` with a `NaN` value. ([l58c14](https://android-review.googlesource.com/#/q/I58c146fae497ce72857f7547df157eaeff9d7081), [b/464025895](https://issuetracker.google.com/issues/464025895))

### Version 1.0.0-alpha09

December 03, 2025

`androidx.xr.runtime:runtime-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/df9651766b0beb5e3f80083d32772a6f0efec450..5dd54df7c7f82386d2da53e696750df346d47550/xr/runtime).

### Version 1.0.0-alpha08

November 19, 2025

`androidx.xr.runtime:runtime-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f4b7c51c02aefb416a700a23672d7285703a2cb6..df9651766b0beb5e3f80083d32772a6f0efec450/xr/runtime).

**New Features**

- `XrDevice` added to provide information about device capabilities. ([Ic9d1f](https://android-review.googlesource.com/#/q/Ic9d1f77990e0e36c9288e3511b4b3bfd9a6c06d9))
- Added new `ConfigMode.isSupported` API for querying session capabilities. ([Iff7af](https://android-review.googlesource.com/#/q/Iff7af12f5cb9eed86fa10882bb08ee90a8b516fb))
- Added `XrDisplay.BlendMode` API. ([I484e4](https://android-review.googlesource.com/#/q/I484e4ac1190a4b8c57d6d6ef22a799fc75fdd1f2))

**API Changes**

- Renamed \[XrDevice.getPreferredBlendMode\] to \[XrDevice.getPreferredDisplayBlendMode\]. ([I7e48f](https://android-review.googlesource.com/#/q/I7e48f09e7e2a4a6c961bbc53f12746c9e9c6e0a0))

### Version 1.0.0-alpha07

October 22, 2025

`androidx.xr.runtime:runtime-*:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cce22de903e4193a54e2143da843b8d98e84b59a..f4b7c51c02aefb416a700a23672d7285703a2cb6/xr/runtime).

**API Changes**

- Remove `SessionConfigureConfigureNotSupported` and replace it with `UnsupportedOperationException`. ([I7680f](https://android-review.googlesource.com/#/q/I7680f3a976845b2ab442d692b3d5db56e00a98cc))

### Version 1.0.0-alpha06

September 24, 2025

`androidx.xr.runtime:runtime-*:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8fe87e902b8acd3de17bd55d6ec0ef4b5188212e..cce22de903e4193a54e2143da843b8d98e84b59a/xr/runtime).

**API Changes**

- `HandJointType` has been moved to `xr:arcore:arcore` from `xr:runtime:runtime`. ([Iadb9c](https://android-review.googlesource.com/#/q/Iadb9cd5da1d2a6025980c07999da7f24830f8623), [b/409058039](https://issuetracker.google.com/issues/409058039))
- Changing the times operator for `componentWiseMultiplication` for `Vector2`, `Vector3`, `Vector4` to scale and removing the operator symbol for consistency with other math libraries. Also removing `componentWiseDivision` from the Vector classes in lieu of using `Vector.scale(otherVector.inverse())`. ([I8e1f6](https://android-review.googlesource.com/#/q/I8e1f688576ca45f7666908f79db8d24ee6d916f0), [b/399146447](https://issuetracker.google.com/issues/399146447))
- Adding \[unscaled\] to return a Matrix with a scale of one. ([I6381d](https://android-review.googlesource.com/#/q/I6381d310a9950a7a4e46cf2cd99cfbdc27db6ce6), [b/434928658](https://issuetracker.google.com/issues/434928658))
- `:xr:runtime:runtime-guava` will be removed as `Coroutines.kt` has been replaced with `SuspendtoFutureAdapter`. ([I0cd3c](https://android-review.googlesource.com/#/q/I0cd3c5f7659d3f2667f3b0f9e0717191977d5391), [b/406597902](https://issuetracker.google.com/issues/406597902))

### Version 1.0.0-alpha05

July 30, 2025

`androidx.xr.runtime:runtime-*:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..8fe87e902b8acd3de17bd55d6ec0ef4b5188212e/xr/runtime).

**New Features**

- Add `HandJointType` and `TrackingState`. ([I55880](https://android-review.googlesource.com/#/q/I558802d9a78449829990c0792e5a1d1bf97ca69b), [b/334645808](https://issuetracker.google.com/issues/334645808))
- Make Config implementation public. ([I95860](https://android-review.googlesource.com/#/q/I9586042b11a9340a80deffa2f92e391bf59f6a58), [b/334645808](https://issuetracker.google.com/issues/334645808))
- Introduced new `SessionCreateResult` and `SessionConfigureResult` types. ([Icb8cb](https://android-review.googlesource.com/#/q/Icb8cba8fcd89822929ff845d6d2e0408cef632af), [b/334645808](https://issuetracker.google.com/issues/334645808))
- Add a new `BoundingBox` class that represents an axis-aligned bounding box in 3D space, defined by its minimum and maximum corner points. ([Ic68c5](https://android-review.googlesource.com/#/q/Ic68c5e60f6443e12d4142cf8c69ecfc3d7d99844), [b/423073468](https://issuetracker.google.com/issues/423073468))

**API Changes**

- Renamed and moved `androidx.xr.scenecore.PixelDimensions` to `androidx.xr.runtime.math.IntSize2d`. Renamed and moved `androidx.xr.scenecore.Dimensions` to `androidx.xr.runtime.math.FloatSize3d`. Renamed `androidx.xr.scenecore.PlaneType` to `androidx.xr.scenecore.PlaneOrientation`. Renamed `androidx.xr.scenecore.PlaneSemantic` to `androidx.xr.scenecore.PlaneSemanticType`. ([Ifd405](https://android-review.googlesource.com/#/q/Ifd40559bd3ffaccfc1782c81af39be1c5e7922a1), [b/416456228](https://issuetracker.google.com/issues/416456228))
- Removed `androidx.xr.runtime.FoV` class. Use `androidx.xr.runtime.FieldOfView` instead. ([I9ae27](https://android-review.googlesource.com/#/q/I9ae27bc07ce8b2fad5371be283b7dad3f70296e6))
- Added an additional overload for `Session.create` which can provide a `LifecycleOwner` for the Session to attach to. Note that an Activity will still need to be provided for resource ownership and the `LifecycleOwner` must be scoped within the Activity. ([I1690b](https://android-review.googlesource.com/#/q/I1690b7d8b5935492fde2940615e87e0ed592ca82))
- Renamed `FakeRuntimeAnchor.anchorsCreated` to `anchorsCreatedCount` ([I96df9](https://android-review.googlesource.com/#/q/I96df9bd731f3e859d473d3dd95ce08e06554c89f), [b/424441218](https://issuetracker.google.com/issues/424441218))
- Config `*Mode` vals have been renamed to reflect their behavior. ([I6d247](https://android-review.googlesource.com/#/q/I6d24772f4456d4a2409adbaf6162fabb4f5756ef), [b/414648065](https://issuetracker.google.com/issues/414648065))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4), [b/344563182](https://issuetracker.google.com/issues/344563182))
- APIs related to manifest strings have been moved from `:xr:runtime:runtime` to `:xr:runtime:runtime-manifest`. The package name has changed from `androidx.xr.runtime` to `androidx.xr.runtime.manifest`. ([I610ad](https://android-review.googlesource.com/#/q/I610ad63853c8223ee0352b719eb5991047f71e84), [b/418800249](https://issuetracker.google.com/issues/418800249))
- `Session.resume()`, `Session.pause()`, and `Session.destroy()` have been removed from the API surface. Session is no longer a `LifecycleOwner`. The Session's lifecycle will now be attached to the lifecycle of the Activity passed in `Session.create()`. ([I28a03](https://android-review.googlesource.com/#/q/I28a0392c9e1a5bb1a02cc12b392442125f1d8cac))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler) ([Ia8420](https://android-review.googlesource.com/#/q/Ia84200c477b50c79761005fffb0d44c001009cca), [b/326456246](https://issuetracker.google.com/issues/326456246))
- The main Runtime artifact (`:xr:runtime:runtime`) will only contain Kolin-style async APIs. Java developers can depend on `:xr:runtime:runtime-guava` to access compatible APIs. ([I05d4a](https://android-review.googlesource.com/#/q/I05d4a527394b5666eb2da7e52968354fd605c393), [b/426639315](https://issuetracker.google.com/issues/426639315))
- The main Runtime artifact (`:xr:runtime:runtime`) will only contain Kotlin-style async APIs. Java developers can depend on the `xr:runtime:runtime-rxjava3` library to access compatible APIs. ([I64122](https://android-review.googlesource.com/#/q/I64122394dba159947b344aefebe741df3129e9c0), [b/426639775](https://issuetracker.google.com/issues/426639775))
- Move Coroutines to `:xr:runtime:runtime-guava` and Flows to `:xr:runtime:runtime-rxjava3`. ([I60ae9](https://android-review.googlesource.com/#/q/I60ae9d8bbe1de2ae5b08a2227028c80cb4fd3772))
- `Session.create` and `Session.configure` now throw `SecurityException` when sufficient permissions have not been granted instead of returning `SessionCreatePermissionsNotGranted` or `SessionConfigurePermissionsNotGranted`. ([I7c488](https://android-review.googlesource.com/#/q/I7c48826f858c9934949093ed8b52446153967761), [b/430651879](https://issuetracker.google.com/issues/430651879))

### Version 1.0.0-alpha04

May 7, 2025

`androidx.xr.runtime:runtime:1.0.0-alpha04`, `androidx.xr.runtime:runtime-openxr:1.0.0-alpha04`, and `androidx.xr.runtime:runtime-testing:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/043342a8810f3356110a0afce48c662e841c428f..b6c541571b9fb5471f965fc52612cb280713e5e4/xr/runtime).

> [!NOTE]
> **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

**New Features**

- Session now implements `androidx.lifecycle.LifecycleOwner` for more interoperability with existing Android lifecycle paradigms.
- Manifest strings for Android XR are specified and documented here.
- Spatial Visibility Callback extension methods added to monitor when the scene content moves inside or outside the user's field of view.
- Added a stub version of the `JxrPlatformAdapter` (and all its related classes).
- Session will be used in both `SceneCore` and Runtime instead of the Session in `SceneCore`.
- `ActivityPose.hitTest` was added, enabling a `hitTest` against virtual content.
- Specifying multiple Runtime implementations at compile time is now supported. Only one will be loaded at execution time based on the current device's feature set.
- Added new Component type `SpatialPointerComponent`, allowing clients to specify the icon rendered for the pointer, or to disable the icon. This Component can currently be attached to `PanelEntity` instances only.

**API Changes**

- Make Config implementation public. ([I95860](https://android-review.googlesource.com/#/q/I9586042b11a9340a80deffa2f92e391bf59f6a58))
- Add `HandJointType` and `TrackingState`. ([I55880](https://android-review.googlesource.com/#/q/I558802d9a78449829990c0792e5a1d1bf97ca69b))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `Hand.isActive (boolean)` has been changed to `Hand.trackingState`. The `OpenXR` implementation has been modified accordingly.
- `android.permission.SCENE_UNDERSTANDING` permission requirement in `Session.configure` has been changed to `android.permission.SCENE_UNDERSTANDING_COARSE`.
- `LifecycleManager.configure` is implemented and now passes in a `Config` object which contains a property for each configurable runtime feature.
- `Session.configure` can now be called with a `Config` in order to configure the available runtime features.
- `Session.create` now supports passing a `CoroutineContext` instead of a `CoroutineDispatcher`.
- `Session.create` supports loading `ARCore` for Jetpack XR and/or `SceneCore`. At least one must be provided (testing versions are available).
- `FakePerceptionManager` throws an `AnchorInvalidUuidException` when an invalid UUID is passed to `Anchor.load` and `Anchor.unpersist`.
- `CoreState` is no longer a data class.

**Bug Fixes**

- Fixed Runtime proguard configurations.

### Version 1.0.0-alpha03

February 26, 2025

`androidx.xr.runtime:runtime:1.0.0-alpha03`, `androidx.xr.runtime:runtime-openxr:1.0.0-alpha03`, and `androidx.xr.runtime:runtime-testing:1.0.0-alpha03` are released with no notable changes since the last alpha. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a96c4899cab90642c7b1d722dc1f3b45f56e7b82..043342a8810f3356110a0afce48c662e841c428f/xr/runtime).

### Version 1.0.0-alpha02

February 12, 2025

`androidx.xr.runtime:runtime:1.0.0-alpha02`, `androidx.xr.runtime:runtime-openxr:1.0.0-alpha02`, and `androidx.xr.runtime:runtime-testing:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2e2729abc59df52d40af80a8bbfe010c02455c6..a96c4899cab90642c7b1d722dc1f3b45f56e7b82/xr/runtime).

**Breaking \& behavioral changes**

- `OpenXR` runtime functions that return an Anchor now throw `AnchorResourcesExhaustedException` if they encounter an error code notifying that the `OpenXR` resource limit has been reached.
- Permission `android.permission.HAND_TRACKING` is now required for `Session.create` and `Session.resume`.

**New features**

- Added hand tracking support.

**Bug fixes**

- Creating anchors is more stable when running on an emulator

### Version 1.0.0-alpha01

December 12, 2024

`androidx.xr.runtime:runtime-* 1.0.0-alpha01` is released.

**Features of Initial Release**

Initial release of Jetpack XR Runtime. This library contains fundamental pieces of functionality for the Jetpack XR suite of libraries. This includes capability discovery, lifecycle management, configuration, and more. The Runtime library provides different variations (e.g. `runtime-openxr` or `runtime-testing`) depending on the execution platform. Additionally, this library offers fundamental math abstractions such as [`Vector3`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Vector3) and [`Matrix4`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Matrix4) that are used across the entire Jetpack XR API surface.

- [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session): Provides you with fine-grained controls over the XR system, including deciding when processing is and is not being executed and the overall configuration. It is also the handle that you will use across all other APIs to unlock the underlying system capabilities.

- [`Pose`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Pose): A location in an arbitrary coordinate system that has a position and orientation associated with it. You will use this class to communicate the location of objects with ARCore for Jetpack XR and Jetpack SceneCore.

**Known Issues**

- [`configure`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#configure()) is currently a no-op. Future releases will add new settings that you can use to control the behavior of the [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session).