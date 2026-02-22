---
title: https://developer.android.com/jetpack/androidx/releases/xr-arcore
url: https://developer.android.com/jetpack/androidx/releases/xr-arcore
source: md.txt
---

# ARCore for Jetpack XR

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore)  
API Reference  
[androidx.xr.arcore](https://developer.android.com/reference/androidx/xr/arcore)  


Bring digital content into the real world with perception capabilities.


| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | - | - | - | [1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/xr-arcore#1.0.0-alpha10) |


## Declaring dependencies


To add a dependency on ARCore for Jetpack XR, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha10"

    // Optional dependencies for asynchronous conversions
    implementation "androidx.xr.arcore:arcore-guava:1.0.0-alpha10"
    implementation "androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha10"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha10")

    // Optional dependencies for asynchronous conversions
    implementation("androidx.xr.arcore:arcore-guava:1.0.0-alpha10")
    implementation("androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha10")
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

`androidx.xr.arcore:arcore-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/66babaed0f95f7d1aa432812f146f6f7ef81eb7b..dee6404678a4a9ffe984428550062cb96908292e/xr/arcore).

**New Features**

- Introduces `TiltGesture` API, providing a reactive `Flow` for stable detection of device tilt (UP/DOWN) state with transition progress. ([Ic269f](https://android-review.googlesource.com/#/q/Ic269f4bc5ffebcb1b51bde774529e2ea3a05c9a4), [b/448152779](https://issuetracker.google.com/issues/448152779))
- ARCore for Jetpack XR now uses the XR Runtime Logging mechanism. See `androidx.xr.runtime.Log` for more information. ([l52735](https://android-review.googlesource.com/#/q/I52735a844218c098129bcf05f9bdedeafc7b16c7), [b/448697662](https://issuetracker.google.com/issues/448697662))

**API Changes**

- `Geospatial.createPoseFromGeospatialPose` now works on OpenXR-enabled devices. ([l362c6](https://android-review.googlesource.com/#/q/I362c64c97acceeae44113defe10533a59a803f13))

### Version 1.0.0-alpha09

December 03, 2025

`androidx.xr.arcore:arcore-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/27075f6aa995822e9eed284abcef9deda5515d58..66babaed0f95f7d1aa432812f146f6f7ef81eb7b/xr/arcore).

### Version 1.0.0-alpha08

November 19, 2025

`androidx.xr.arcore:arcore-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2b064a168d829249efe96ad64737eb84d6c23d4e..27075f6aa995822e9eed284abcef9deda5515d58/xr/arcore).

**New Features**

- `ARCore` for Jetpack XR now supports devices where Google Play Services for AR is available.
- Added Geospatial APIs for VPS Availability and pose conversion ([I144dc](https://android-review.googlesource.com/#/q/I144dc1fc302ff6fc99046fb318e01762e3344ac0))

### Version 1.0.0-alpha07

October 22, 2025

`androidx.xr.arcore:arcore-*:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cec8da8c78713829dd8776bd16d274c4656de90d..2b064a168d829249efe96ad64737eb84d6c23d4e/xr/arcore).

**Bug Fixes**

- `:xr:arcore:arcore-openxr` added as an implementation dependency to `:xr:arcore:arcore` ([I47315](https://android-review.googlesource.com/#/q/I4731512dc13e5d4d819ae27cac98b3278086d7de), [b/446999229](https://issuetracker.google.com/issues/446999229))

### Version 1.0.0-alpha06

September 24, 2025

`androidx.xr.arcore:arcore-*:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1180fa76699d16f2ed6497faf92089ff851636ff..cec8da8c78713829dd8776bd16d274c4656de90d/xr/arcore).

**API Changes**

- Testing support for `ARCore` has migrated to the `xr:arcore:arcore-testing` module. ([I25469](https://android-review.googlesource.com/#/q/I25469a26fc79b7f9b6ee47ae83b882723dab196e))
- Adding `ArDevice` and `RenderViewpoint` to allow applications to retrieve the device's pose and display configuration for rendering purposes. ([Ib7e3f](https://android-review.googlesource.com/#/q/Ib7e3f2ff3ca432cb335877fecd6bec391496ed6b))
- Rename `HandJointType` enums with `HAND_JOINT_TYPE_` prefix. ([I3f7cd](https://android-review.googlesource.com/#/q/I3f7cd85345c7c61baa72a79b11857a9a28437d04))
- `HandJointType` has been moved to `xr:arcore:arcore` from `xr:runtime:runtime`. ([Iadb9c](https://android-review.googlesource.com/#/q/Iadb9cd5da1d2a6025980c07999da7f24830f8623), [b/409058039](https://issuetracker.google.com/issues/409058039))
- `Hand.State` now exposes a [`java.nio.FloatBuffer`](https://developer.android.com/reference/java/nio/FloatBuffer) with the joint poses in a format that allows easy access to performance-oriented applications. ([I55e27](https://android-review.googlesource.com/#/q/I55e27c38b75af734304f3de665d0faaca58f1e57))

### Version 1.0.0-alpha05

July 30, 2025

`androidx.xr.arcore:arcore:1.0.0-alpha05`, `androidx.xr.arcore:arcore-guava:1.0.0-alpha05`, and `androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1180fa76699d16f2ed6497faf92089ff851636ff/xr/arcore).

**New Features**

- Add `getPrimaryHandSide` so the developer could get the hand side info ([I270bd](https://android-review.googlesource.com/#/q/I270bd96a51c22a0b881b10dc3f63ab498a91027e))
- Add geospatial check VPS availability API ([I58573](https://android-review.googlesource.com/#/q/I585737ac31e4de16cd8f0c4bf39449e0e83043ec))
- Add ARCore API for `checkVpsAvailability` ([Idbded](https://android-review.googlesource.com/#/q/Idbded3e077a1c5cde660cc064c67ebdb4fd5cca9))
- `stateFlowable` extension functions added to `:xr:arcore:arcore-rxjava3` for usage by Java developers. ([I083aa](https://android-review.googlesource.com/#/q/I083aafc4e99d0ce2c8c815a05950b8f47af7ee8d), [b/427247794](https://issuetracker.google.com/issues/427247794))

**API Changes**

- Config `*Mode` vals have been renamed to reflect their behavior. ([I6d247](https://android-review.googlesource.com/#/q/I6d24772f4456d4a2409adbaf6162fabb4f5756ef), [b/414648065](https://issuetracker.google.com/issues/414648065))
- The main ARCore artifact (xr:arcore:arcore) will only contain Kotlin-style async APIs. Java developers can depend on the `xr:arcore:arcore-rxjava3` library to access compatible APIs. ([Ia525e](https://android-review.googlesource.com/#/q/Ia525e08c0a79a9b97af3983a0b582ad8d9e38077), [b/422794329](https://issuetracker.google.com/issues/422794329))
- The main ARCore artifact (`xr:scenecore:scenecore`) will only contain Kotlin-style async APIs. Java developers can depend on the `xr:arcore:arcore-guava` library to access compatible APIs. ([Iffcb4](https://android-review.googlesource.com/#/q/Iffcb48c1fe842ed1fe1342969a50fac6ba38eb6a), [b/422773524](https://issuetracker.google.com/issues/422773524))
- `Anchor.persistAsync()` added to `AnchorGuava` for usage by Java developers. ([I4af1c](https://android-review.googlesource.com/#/q/I4af1c265e2a60f804ed13042e2f1a9b31c6136fd), [b/425984631](https://issuetracker.google.com/issues/425984631))
- `Earth.createAnchorOnSurfaceAsync(Session, Double, Double, Double, Quaternion, Surface)` added to `EarthGuava` for usage by Java developers. ([I66357](https://android-review.googlesource.com/#/q/I6635792821a1c766bca4c838800b071c11fff9a6), [b/425992992](https://issuetracker.google.com/issues/425992992))
- Java developers will use the extension functions for `GltfModel.createAsync` in `GltfModel.kt`. Async functions in `GltfModel` will be deleted. ([I0af60](https://android-review.googlesource.com/#/q/I0af609e44a3aaa6122ebf8c8ca2783c121cce094))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler) ([Ia8420](https://android-review.googlesource.com/#/q/Ia84200c477b50c79761005fffb0d44c001009cca), [b/326456246](https://issuetracker.google.com/issues/326456246))
- `subscribeAsFlowable` extension functions added to `:xr:arcore:arcore-rxjava3` for usage by Java developers. ([Id3e49](https://android-review.googlesource.com/#/q/Id3e496e8cd4ef7c4757295d939de46f2b96898e4), [b/427277298](https://issuetracker.google.com/issues/427277298))

### Version 1.0.0-alpha04

May 7, 2025

`androidx.xr.arcore:arcore:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/043342a8810f3356110a0afce48c662e841c428f..b6c541571b9fb5471f965fc52612cb280713e5e4/xr/arcore/arcore).
| **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `TrackingState` and `HandJointType` have been moved from ARCore to Runtime.
- `Hand.State.isActive (boolean)` has been changed to `Hand.State.trackingState (androidx.xr.runtime.TrackingState)`.
- `Anchor.load` returns `Anchor.AnchorLoadInvalidUuid` if the UUID is invalid.

### Version 1.0.0-alpha03

February 26, 2025

`androidx.xr.arcore:arcore:1.0.0-alpha03` is released with no notable changes since the last alpha. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a96c4899cab90642c7b1d722dc1f3b45f56e7b82..043342a8810f3356110a0afce48c662e841c428f/xr/arcore/arcore).

### Version 1.0.0-alpha02

February 12, 2025

`androidx.xr.arcore:arcore:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2e2729abc59df52d40af80a8bbfe010c02455c6..a96c4899cab90642c7b1d722dc1f3b45f56e7b82/xr/arcore/arcore).

**New Features**

- Added hand tracking support. Use `Hand.left` and `Hand.right` to access the tracking information.
- APIs that generate an anchor (`Anchor.create`, `Anchor.load`, `Plane.createAnchor`) now all return `AnchorCreateResult` and properly implement `AnchorCreateResourcesExhausted`.

**Bug fixes**

- `Anchor.detach` no longer causes a fatal crash due to a race condition with the Session update thread.
- `Anchor.create` is more stable when running on an emulator

### Version 1.0.0-alpha01

December 12, 2024

`androidx.xr.arcore:arcore-* 1.0.0-alpha01` is released.

**Features of initial release**

Inspired by the existing ARCore library, the ARCore for Jetpack XR library provides capabilities for blending digital content with the real world. This library includes motion tracking, persistent anchors, hit testing, and plane identification with semantic labeling (for example, floor, walls, and tabletops). View the [developer guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore)
to learn more about working with ARCore for Jetpack XR.

- [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session): ARCore for Jetpack XR uses the Jetpack XR Runtime under-the-hood to power its functionality. You will use a Session to interact with most ARCore for Jetpack XR APIs, so please take a look at its documentation.

- [`Plane`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane): Use planes to understand the world around you. Each plane has a [`Label`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.Label) that describes it semantically. You can use [`subscribe`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane#subscribe(androidx.xr.runtime.Session)) to be notified about the latest detected planes or [`state`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane#state()) to be notified about the changes to a specific plane.

- [`Anchor`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor): A link between a virtual object and a real world location. Anchors can be attached to a specific location in space (using [`create`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#create(androidx.xr.runtime.Session,androidx.xr.runtime.math.Pose))) or a [`Trackable`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Trackable) (using [`createAnchor`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Trackable#createAnchor(androidx.xr.runtime.math.Pose))).

  - Anchors can be reused across sessions. You can use [`persist`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#persist()) to store them, [`getPersistedAnchorUuids`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#getPersistedAnchorUuids(androidx.xr.runtime.Session)) to enumerate them and [`load`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#load(androidx.xr.runtime.Session,java.util.UUID)) to retrieve them. Make sure that you [`unpersist`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#unpersist(androidx.xr.runtime.Session,java.util.UUID)) them once they are no longer in use.

  - Anchors are interoperable between ARCore for Jetpack XR and Jetpack SceneCore. You can create an [`AnchorEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AnchorEntity) using an anchor or, if you have an existing AnchorEntity, you can use [`getAnchor`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AnchorEntity#getAnchor(androidx.xr.runtime.Session)) to retrieve its backing anchor.

  - Offer natural user interactions using [`hitTest`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/package-summary#hitTest(androidx.xr.runtime.Session,androidx.xr.runtime.math.Ray)). A hitTest uses a [`Ray`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Ray) to determine which contents it intersects and to create an [`Anchor`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor) from that location. Consider conducting a hitTest from an [`InputEvent`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/InputEvent).

**Known Issues**

- There might be a delay between calling [`unpersist`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#unpersist(androidx.xr.runtime.Session,java.util.UUID)) and its UUID being removed from the results returned by [`getPersistedAnchorUuids`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#getPersistedAnchorUuids(androidx.xr.runtime.Session)).

- [`create`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#create(androidx.xr.runtime.Session,androidx.xr.runtime.math.Pose)) will not validate that the system has enough resources to return new anchors. Creating an excessive amount of anchors might lead to a crash.

- Persisting an Anchor that was previously persisted and unpersisted is not currently supported.

- Usage in the emulator is supported, but the behavior might not be as stable as when running on an actual device. Particularly, calls to [`create`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#create(androidx.xr.runtime.Session,androidx.xr.runtime.math.Pose)) might fail with a native code error and immediately terminate the activity.

- In certain circumstances, a `RuntimeException` might be erroneously thrown when calling [`persist`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#persist()) with the message "Anchor was not persisted". In those circumstances, the function would still succeed and the anchor will be persisted. We recommend wrapping the call to `persist` with a `try` block as a workaround.