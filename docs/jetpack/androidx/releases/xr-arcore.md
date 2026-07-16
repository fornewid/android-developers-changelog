---
title: https://developer.android.com/jetpack/androidx/releases/xr-arcore
url: https://developer.android.com/jetpack/androidx/releases/xr-arcore
source: md.txt
---

# ARCore for Jetpack XR

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore)

Bring digital content into the real world with perception capabilities.


| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 15, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/xr-arcore#1.0.0-beta01) | - |


## Declaring dependencies


To add a dependency on ARCore for Jetpack XR, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.arcore:arcore:1.0.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.arcore:arcore:1.0.0-beta01")
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

### Version 1.0.0-beta01

July 15, 2026

`androidx.xr.arcore:arcore-*:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1790799be76c86764f97a92871414dfdd08154a2..ad7cd7099fdef1e27d4e7c957a7cbf7b8690d425/xr/arcore).

**API Changes**

- Updated resizable modifier to use a `ResizePolicy` instead of two modifiers ([I7fb0f](https://android-review.googlesource.com/#/q/I7fb0fff7c7abe5ab3cffe2a118fec42cf61f4684), [b/496257436](https://issuetracker.google.com/issues/496257436), [b/519672992](https://issuetracker.google.com/issues/519672992))
- Added movable overload with `movePolicy` param and deprecate `transformingMovable` and `movable` ([Ic88c1](https://android-review.googlesource.com/#/q/Ic88c1d6acf919b741f6f50bca3f61da958caab70), [b/481781189](https://issuetracker.google.com/issues/481781189))
- Removed `TrackingState`.TRACKING_DEGRADED from public API surface and map runtime degraded states to PAUSED instead. Update `TrackingState` to use enums instead of int values for string conversion and runtime conversion. ([I3eb5b](https://android-review.googlesource.com/#/q/I3eb5b4b57f9d9bd029f0b08a9841d54b4ebf128e), [b/524326338](https://issuetracker.google.com/issues/524326338))
- Converted Session.create to a suspend function. ([I5d27f](https://android-review.googlesource.com/#/q/I5d27fd6399fc5fe35f28ddf9c0c488a12eb23115))
- Deprecated the `ProjectedPermissionsResultContract` ([I141d5](https://android-review.googlesource.com/#/q/I141d5713b3a0c26606f85815111fa7af88f63269), [b/515699436](https://issuetracker.google.com/issues/515699436))
- Updated `AnchorEntity` to be called `AnchorSpace` ([Ifa95e](https://android-review.googlesource.com/#/q/Ifa95ebf5c1da2b4413723835db4c0e5f9a2e52fb), [b/513619219](https://issuetracker.google.com/issues/513619219))

### Version 1.0.0-alpha15

June 17, 2026

`androidx.xr.arcore:arcore-*:1.0.0-alpha15` is released. Version 1.0.0-alpha15 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9ddf57f5b4ce98e7df261a3de947540f143fe26c..1790799be76c86764f97a92871414dfdd08154a2/xr/arcore).

**API Changes**

- `HitResult.createAnchor` was removed. Developers can create an anchor representing the `HitResult` if the trackable of the result is an `Anchorable` by supplying the hit position to the `createAnchor` function of the `Anchorable`. ([Ia851e](https://android-review.googlesource.com/#/q/Ia851e1865dc7080f960d616965a845aafa56e8e9))
- `AnchorUnsupportedObject` was removed. It is no longer thrown by a JXR ARCore runtime. ([Ia851e](https://android-review.googlesource.com/#/q/Ia851e1865dc7080f960d616965a845aafa56e8e9))
- `androidx.xr.arcore.Anchor` and `androidx.xr.arcore.ArDevice` now implement `androidx.xr.arcore.Trackable`. ([I57b65](https://android-review.googlesource.com/#/q/I57b6519a710bf277345c332201a01d96aa9b9606))
- `Depth.left`, `Depth.right`, and `Depth.mono` are now non-nullable ([I1fc5e](https://android-review.googlesource.com/#/q/I1fc5e42404477122af26dd2a541483934aa327ad))
- `Face.getUserFace` is now non-nullable ([I0eac1](https://android-review.googlesource.com/#/q/I0eac1729355d684f7565c0e06a8f75f44c4603a0))
- `RenderViewpoint.left`, `RenderViewpoint.right`, `RenderViewpoint.mono` are now non-nullable ([Icf7fa](https://android-review.googlesource.com/#/q/Icf7faa4690d6d36ef43efb4544071b7f58face12))
- `Hand.left` and `Hand.right` are non non-nullable ([Icef37](https://android-review.googlesource.com/#/q/Icef37cb8599c6a1ca83ef2f4cb45f1e8ed0331dc))
- Added `QrCode` API ([Ia0bbe](https://android-review.googlesource.com/#/q/Ia0bbe0444195922efdf6ebd76ee91b44a600e3ee))

### Version 1.0.0-alpha14

May 19, 2026

`androidx.xr.arcore:arcore-*:1.0.0-alpha14` is released. Version 1.0.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0671e372f2168396421338583e76edca824d7d22..9ddf57f5b4ce98e7df261a3de947540f143fe26c/xr/arcore).

**API Changes**

- Deprecating `GeospatialMode.VPS_AND_GPS` in favor of `GeospatialMode.SPATIAL` and introducing a new lower-power tracking mode, `GeospatialMode.INERTIAL`, which uses only IMU and GPS. ([I1e6cd](https://android-review.googlesource.com/#/q/I1e6cde5e98a05f7e52c6c107d596a004d8158022))
- Custom anchor exception classes: `AnchorInvalidUuidException`, `AnchorNotAuthorizedException`, `AnchorUnsupportedLocationException`, `AnchorRuntimeFailureException`, and `AnchorUnsupportedObjectException` are now `RuntimeException` instances, not intended to be checked. ([I9356e](https://android-review.googlesource.com/#/q/I9356e4ac3a9d0e612e1c21fd319d7c18460f6c30))
- Added `ArCoreTestRule` API, including `TestArDevice`, `TestAugmentableObject`, `TestDepthMap`, `TestEye`, `TestFace`, `TestGeospatial`, `TestHand`, `TestPlane`, `TestRenderViewpoint`, \& `TestTrackable` ([I0ad3c](https://android-review.googlesource.com/#/q/I0ad3c7a75510b0078696558fa2e275785c0f3cc5))
- Removes `AnchorLoadInvalidUuid`, `AnchorCreateUnsupportedObject`, `AnchorCreateUnsupportedLocation`, and `AnchorCreateNotAuthorized`. All of these errors are now exceptions in the runtime. Removes `AnchorCreateIllegalState`. This has been replaced with `AnchorCreateTrackingUnavailable` in most cases. Adds `AnchorException` and derived classes `AnchorInvalidUuidException`, `AnchorNotAuthorizedException`, `AnchorUnsupportedLocationException`, `AnchorRuntimeFailureException`, and `AnchorUnsupportedObjectException`. ([I4c4dd](https://android-review.googlesource.com/#/q/I4c4dd34e8154e9a793160c3c081122b178694108))

**External Contribution**

- Added `AugmentedImage` API for custom marker tracking ([I0cf09](https://android-review.googlesource.com/#/q/I0cf0953c17e691b1501e08182b3d027efa891753))

### Version 1.0.0-alpha13

May 06, 2026

`androidx.xr.arcore:arcore-*:1.0.0-alpha13` is released. Version 1.0.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bc435de8f136679d268375c04ab31ecc94fa99f9..0671e372f2168396421338583e76edca824d7d22/xr/arcore).

**API Changes**

- `TrackingState` and `VpsAvailabilityResult` have moved to the `androidx.xr.arcore package`, and the types in `androidx.xr.runtime` are now deprecated. ([Ic7930](https://android-review.googlesource.com/#/q/Ic79303427f1301f722efb7f624033f9f11b49544), [b/480462213](https://issuetracker.google.com/issues/480462213))
- Renamed `Plane.Type` to `PlaneType`. ([I8c90c](https://android-review.googlesource.com/#/q/I8c90cccb087dd6bf0d5342d39db5e6eca210e572), [b/482675376](https://issuetracker.google.com/issues/482675376))
- Renamed `Hand.HandSide` to `HandSide`. ([Ica562](https://android-review.googlesource.com/#/q/Ica562ae66c9d59f927f5201b3315c82317840793), [b/482675376](https://issuetracker.google.com/issues/482675376))
- Renamed `Plane.Label` to `PlaneLabel`. ([Ic6b67](https://android-review.googlesource.com/#/q/Ic6b67074e9a22f44cd2ec30dad0c5f17fc9631af), [b/482675376](https://issuetracker.google.com/issues/482675376))
- Renamed `Geospatial.Surface` to `GeospatialSurface`. ([I1a8be](https://android-review.googlesource.com/#/q/I1a8be619cb27cd3915a2098bb85e167fcea595b7), [b/482675376](https://issuetracker.google.com/issues/482675376))
- Renamed `Geospatial.State`to `GeospatialState`. ([I203fa](https://android-review.googlesource.com/#/q/I203fa5118d103987272b5667bb67dc656efbaffb), [b/482675376](https://issuetracker.google.com/issues/482675376))
- Moved `NativeData` API to `xr:runtime:runtime` library. ([I87954](https://android-review.googlesource.com/#/q/I87954b9811c11c019f9a256dacd11c352b79cc56), [b/494251500](https://issuetracker.google.com/issues/494251500))
- `Session.create` and `Session.configure` are now non-exhaustive and require else clauses in when statements. ([I9885e](https://android-review.googlesource.com/#/q/I9885e2b6bdb6da77988d04402f0df73380f6807a), [b/495805998](https://issuetracker.google.com/issues/495805998), [b/495805998](https://issuetracker.google.com/issues/495805998))
- `androidx.xr.runtime.FieldOfView` has been deprecated. Use `androidx.xr.runtime.math.FieldOfView` instead. ([Ia01a0](https://android-review.googlesource.com/#/q/Ia01a0ac228dc4a93c1bb2979b26d4f400be4fe99), [b/480233045](https://issuetracker.google.com/issues/480233045))
- Changed Orbiter to use either an `OrbiterAnchorPoint + VolumeOffset` or an `OrbiterPoseProvider` instead of position, offset, offsetType, alignment, and elevation. Also removed the `shouldRenderInNonSpatial` parameter. If the developer does not want the orbiter to render in non-spatial they should wrap the orbiter in an if statement and check the `SpatialCapabilities`. ([I9fbb3](https://android-review.googlesource.com/#/q/I9fbb3826fb7e709f86fee3e033585cdd97bc0b79), [b/462428503](https://issuetracker.google.com/issues/462428503))
- Added movable modifiers. These modifiers work well, right now, for `SpatialPanels` and `SpatialExternalSurface`. Very soon they will also be supported for `SpatialGltfModels`. However, the intention is to have these supported well for all `SubspaceComposables`. ([I9a3cd](https://android-review.googlesource.com/#/q/I9a3cd5a7989887a09282207629cd4a6dd39dfae7), [b/479530787](https://issuetracker.google.com/issues/479530787), [b/478935063](https://issuetracker.google.com/issues/478935063), [b/478935063](https://issuetracker.google.com/issues/478935063))
- Developers are expected to observe the `ArDevice.state` Flow to monitor `State.trackingState` and adjust their application's rendering or warnings accordingly based on the tracking fidelity. ([Ic00f0](https://android-review.googlesource.com/#/q/Ic00f0e941ad4491ea15efdc42045eee256f50191), [b/445466590](https://issuetracker.google.com/issues/445466590))
- Renamed `HandJointType` enum values. ([Ifbc83](https://android-review.googlesource.com/#/q/Ifbc83b1141960fc83d32a08e6b8a65c7091ce612), [b/482670596](https://issuetracker.google.com/issues/482670596))
- Renamed `FaceConfidenceRegion` constants. ([Ia62d5](https://android-review.googlesource.com/#/q/Ia62d5d829ba0cf819d18bc96121045421acd7e60), [b/482670596](https://issuetracker.google.com/issues/482670596))
- Renamed `FaceBlendShapeType` constants. ([I33b8b](https://android-review.googlesource.com/#/q/I33b8b8460697dfd1d71d8d9d39a3d673d8abfad7), [b/482670596](https://issuetracker.google.com/issues/482670596))
- Added `CreatePoseFromGeospatialPoseErrorInternal` and `CreateGeospatialPoseFromPoseErrorInternal`. ([I4bcf1](https://android-review.googlesource.com/#/q/I4bcf1942bf859413b3f99a4618c48eb0ef63fd81), [b/482666615](https://issuetracker.google.com/issues/482666615))
- Renamed `DeviceTrackingMode.LAST_KNOWN` to `SPATIAL_LAST_KNOWN` (with a deprecated fallback), added `INERTIAL_LAST_KNOWN` for 3DoF tracking, and added `TRACKING_DEGRADED` to `TrackingState`. ([Ie661c](https://android-review.googlesource.com/#/q/Ie661cfd441521987dcebd7e1fd1e7cfc3ef5ab9d), [b/445466590](https://issuetracker.google.com/issues/445466590))
- Deprecated `GroupEntity`. To have an Entity with only the base Entity functionality, call `Entity.create` which will return and Entity interface. ([I4c450](https://android-review.googlesource.com/#/q/I4c45068d0b8f9a15a2b2ce29bc3523cf93463446), [b/473867483](https://issuetracker.google.com/issues/473867483))
- Added `XrLog` API. Set `XrLog.isEnabled`to `true` to enable logging in JetpackXR, and use `XrLog.Level` to set the log level. ([I76a1f](https://android-review.googlesource.com/#/q/I76a1f066b96ab6f07016d57c7e8e83518cb67de6), [b/463460895](https://issuetracker.google.com/issues/463460895), [b/487378441](https://issuetracker.google.com/issues/487378441))

**Bug Fixes**

- Add the device tracking state support to the openxr devices. ([I91485](https://android-review.googlesource.com/#/q/I914850cda132645b7c8d40e12e204e7528ac056a), [b/445466590](https://issuetracker.google.com/issues/445466590))

### Version 1.0.0-alpha12

March 25, 2026

`androidx.xr.arcore:arcore-*:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c6ef8fa5ea41c72f3cc3e7c77e7981305dfecf33..bc435de8f136679d268375c04ab31ecc94fa99f9/xr/arcore).

**API Changes**

- Changed `Config.augmentedObjectCategories` from a List to a Set. ([I25a64](https://android-review.googlesource.com/#/q/I25a64eb05fa641c80185dbff62b7d140a2d4cac0), [b/487376359](https://issuetracker.google.com/issues/487376359))
- The types `androidx.xr.arcore.Eye` and `androidx.xr.arcore.Hand`. ([I42438](https://android-review.googlesource.com/#/q/I42438bade68de856a267bdd7280ee89b81f7eb5b), [b/449032900](https://issuetracker.google.com/issues/449032900))
- Added `Session.create` overload to allow passing an Android Context for resource-scoping. ([I7d3fe](https://android-review.googlesource.com/#/q/I7d3fec251fb7d1a415a812286d71adbf23a910b2), [b/415805990](https://issuetracker.google.com/issues/415805990), [b/477386334](https://issuetracker.google.com/issues/477386334))
- Changes `FakeRuntimeAnchor.ANCHOR_RESOURCE_LIMIT` to `FakeRuntimeAnchor.anchorResourceLimit`. ([I90841](https://android-review.googlesource.com/#/q/I9084135267eeede19b5d4125432a409f33aa4ee8), [b/431992235](https://issuetracker.google.com/issues/431992235))
- Making `TiltGesture` API experimental as it may be changed or removed in the future. To use this api, opt in to `@ExperimentalGesturesApi` ([Ic9858](https://android-review.googlesource.com/#/q/Ic98584011ddc6c6ba6c44a6d979ce56ca04860c4))
- Added ability to set categories for `AugmentedObject` tracking in the Config ([I1f6e4](https://android-review.googlesource.com/#/q/I1f6e4e634a511ab591802327ce3d45da6a3a0510), [b/480220930](https://issuetracker.google.com/issues/480220930))

**Bug Fixes**

- Fixed Chrome's build by updating META-INF/services/ file with actual location of `PerceptionRuntimeFactory`. ([I7a801](https://android-review.googlesource.com/#/q/I7a80111b2144ed2406cb2bd0113100faac9057b0), [b/481288291](https://issuetracker.google.com/issues/481288291))

### Version 1.0.0-alpha11

February 25, 2026

`androidx.xr.arcore:arcore-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dee6404678a4a9ffe984428550062cb96908292e..c6ef8fa5ea41c72f3cc3e7c77e7981305dfecf33/xr/arcore).

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

> [!NOTE]
> **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

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