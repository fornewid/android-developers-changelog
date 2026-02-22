---
title: https://developer.android.com/jetpack/androidx/releases/xr-runtime
url: https://developer.android.com/jetpack/androidx/releases/xr-runtime
source: md.txt
---

# XR Runtime

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore)  
API Reference  
[androidx.xr.runtime](https://developer.android.com/reference/androidx/xr/runtime/package-summary)  

[androidx.xr.runtime.java](https://developer.android.com/reference/androidx/xr/runtime/java/package-summary)  

[androidx.xr.runtime.math](https://developer.android.com/reference/androidx/xr/runtime/math/package-summary)  


Start your custom AR or 3D session with our native runtime.


| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | - | - | - | [1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/xr-runtime#1.0.0-alpha10) |


## Declaring dependencies


To add a dependency on XR runtime, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha10"

    // Optional dependencies for asynchronous conversions
    implementation "androidx.xr.runtime:runtime-guava:1.0.0-alpha10"
    implementation "androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha10"

    // Use in environments that do not support OpenXR
    testImplementation "androidx.xr.runtime:runtime-testing:1.0.0-alpha10"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha10")

    // Optional dependencies for asynchronous conversions
    implementation("androidx.xr.runtime:runtime-guava:1.0.0-alpha10")
    implementation("androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha10")

    // Use in environments that do not support OpenXR
    testImplementation("androidx.xr.runtime:runtime-testing:1.0.0-alpha10")
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

### Version 1.0.0-alpha10

January 28, 2026

`androidx.xr.runtime:runtime-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5dd54df7c7f82386d2da53e696750df346d47550..6d802bc724002ae38712673fb300c314f88fdd9e/xr/runtime).

**API Changes**

- `ConfigMode.HeadTrackingMode` is replaced with `ConfigMode.HeadTrackingMode`. ([le273e](https://android-review.googlesource.com/#/q/Ie273ef58cbd8187d33e91b344d37107187002990), [b/467150206](https://issuetracker.google.com/issues/467150206))
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
| **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

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