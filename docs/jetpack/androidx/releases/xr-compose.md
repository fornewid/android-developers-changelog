---
title: https://developer.android.com/jetpack/androidx/releases/xr-compose
url: https://developer.android.com/jetpack/androidx/releases/xr-compose
source: md.txt
---

# Jetpack Compose for XR

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) [Code Sample](https://github.com/android/xr-samples) [Codelab](https://github.com/android/xr-codelabs) API Reference  
[androidx.xr.compose.platform](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary)  
[androidx.xr.compose.spatial](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary)  
[androidx.xr.compose.subspace](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary)  
[androidx.xr.compose.subspace.layout](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/package-summary)  
[androidx.xr.compose.subspace.node](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/node/package-summary)  
[androidx.xr.compose.unit](https://developer.android.com/reference/kotlin/androidx/xr/compose/unit/package-summary)  
Declaratively build spatial UI layouts that take advantage of Android XR's spatial capabilities.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | - | - | - | [1.0.0-alpha11](https://developer.android.com/jetpack/androidx/releases/xr-compose#1.0.0-alpha11) |

## Declaring dependencies

To add a dependency on XR compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.compose:compose:1.0.0-alpha11"

    // Use to write unit tests
    testImplementation "androidx.xr.compose:compose-testing:1.0.0-alpha11"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.compose:compose:1.0.0-alpha11")

    // Use to write unit tests
    testImplementation("androidx.xr.compose:compose-testing:1.0.0-alpha11")
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

### Version 1.0.0-alpha11

February 25, 2026

`androidx.xr.compose:compose:1.0.0-alpha11` and `androidx.xr.compose:compose-testing:1.0.0-alpha11` are released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0da43ebb1f8dc8fba8df8f2cf05d8164688aa0ab..a34b6c25f6fbb862348d1696a3ac8806f66842c5/xr/compose).

**New Features**

- Adding `SuperSampling` parameter to `SpatialExternalSurfaces` ([Icd4d1](https://android-review.googlesource.com/#/q/Icd4d18c137960ab4c84f03ce97e3ada0c7dc4cb6))

**API Changes**

- Subspace modifier padding changes for layout direction awareness. ([I53e25](https://android-review.googlesource.com/#/q/I53e25bced4273331204eac3910dd285c16b9c394))
- `SpatialCapabilities` is now sealed and cannot be extended. ([I07aef](https://android-review.googlesource.com/#/q/I07aef87e644421fb5ac63464d88b76a094c5215f))
- The `SpatialRow` and `SpatialColumn` APIs that accept a generic `SpatialAlignment` parameter are deprecated; instead, use the APIs that accept either `verticalAlignment` or `horizontalAlignment` for `SpatialRow` and `SpatialColumn`, respectively. ([Iec390](https://android-review.googlesource.com/#/q/Iec390d2f302fe756f7c112ff30e877f74c36589b))
- Combining overloading `SubspaceLayout` function APIs ([Idd30a](https://android-review.googlesource.com/#/q/Idd30a865bf5ff5249be94abae6b5ba2da847450c))
- Renamed `SubspaceModifier.lookAtUser` to `rotateToLookAtUser` and the `up` parameter to `upDirection`. ([Icafb8](https://android-review.googlesource.com/#/q/Icafb85196f75e75e8530eb658981f26141abb6e3))
- Making `SpatialRow` an inline function ([Ia2f20](https://android-review.googlesource.com/#/q/Ia2f20b8af183cf5064676fb597ed587cba240266))
- Making `SpatialColumn` an inline function ([I681be](https://android-review.googlesource.com/#/q/I681be0b9b5263f0a2b54eac21d54c81c502b02ce))
- Removed billboard API ([Ib76cd](https://android-review.googlesource.com/#/q/Ib76cd43fe8338322d20b062ef937538a8c7fd04d))

### Version 1.0.0-alpha10

January 28, 2026

`androidx.xr.compose:compose:1.0.0-alpha10` and `androidx.xr.compose:compose-testing:1.0.0-alpha10` are released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e4042dc841f56cd0fc47060f4a1efbf76486ca2..0da43ebb1f8dc8fba8df8f2cf05d8164688aa0ab/xr/compose).

**API Changes**

- Removing deprecated API - `ApplicationSubspace` ([Ia6596](https://android-review.googlesource.com/#/q/Ia6596f3badd4d09cc25cfd4006ad9ccf946b28c2), [b/468345186](https://issuetracker.google.com/issues/468345186))
- Updated `SpatialShape` to a sealed interface ([I7e3f5](https://android-review.googlesource.com/#/q/I7e3f54b3057ab2ce8d59c0e6de42eb9fa6166aa1), [b/460426800](https://issuetracker.google.com/issues/460426800))
- Removing Deprecated APIs in `SpatialAlignment`. ([Ib0b61](https://android-review.googlesource.com/#/q/Ib0b61182a03595362e8275dbee9b8a85da966970), [b/468011887](https://issuetracker.google.com/issues/468011887))
- Deprecating `SpatialLayoutSpacer` and introducing `SpatialSpacer`. ([I2ebf3](https://android-review.googlesource.com/#/q/I2ebf3c6229719e75b9832090197eaed37c772e23), [b/466071383](https://issuetracker.google.com/issues/466071383))
- Updated `UserSubspace` API to replace "lazy locking" terminology with "soft locking". ([I9ded1](https://android-review.googlesource.com/#/q/I9ded16a27b9b634d1e9b8698722db43ffbc8e3a9), [b/464035984](https://issuetracker.google.com/issues/464035984))

### Version 1.0.0-alpha09

December 03, 2025

`androidx.xr.compose:compose:1.0.0-alpha09` and `androidx.xr.compose:compose-testing:1.0.0-alpha09` are released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/91b842c20be0cfd3185e2953615ea38c4707bf34..7e4042dc841f56cd0fc47060f4a1efbf76486ca2/xr/compose).

**API Changes**

- Adding `LookAtUser` and Billboard modifiers which allows content to always face the user. ([I49b99](https://android-review.googlesource.com/#/q/I49b995ac13d1a33c83da7b24bccc0e825da8e8bb))
- Adds the ability to set an `InteractionPolicy` to `SpatialExternalSurfaces` and `SpatialPanels`, allowing the detection of clicks and other 3D input events. ([Iae155](https://android-review.googlesource.com/#/q/Iae15522cfe9f52dece5adeb87696dc8fdffba6bb))
- Added size and `requiredSize` modifier overload with width, height, and depth as Dp values. ([I92f79](https://android-review.googlesource.com/#/q/I92f79139e762989340bbf53c7150d00466ea7d78))
- `ParentLayoutParamsModifier` interface now extends `DelegatableSubspaceNode`. ([I1a6d4](https://android-review.googlesource.com/#/q/I1a6d4ef5caa69dce5173b6d65a534bb333972ad4))
- `ApplicationSubspace` is deprecated in favor of the Subspace API.
  - Subspace API behavior is changed to only provide an application-wide subspace at the recommended pose and scale.
  - `PlanarEmbeddedSubspace` API is introduced to provide embedded subspaces in 2D contexts. ([Id3343](https://android-review.googlesource.com/#/q/Id3343f593b0d32c447d5f51d4c75044928621216))
- Added `shouldAutoInvalidate` flag to `SubspaceModifier.Node` API. ([I93902](https://android-review.googlesource.com/#/q/I9390208186737d34d042ec1c7ae7ce6b270a064c))
- Added `required(Size|Width|Depth|Height)`In APIs that allow developers to constrain a `@SubspaceComposable`'s size to a specific range, disregarding the parent's incoming measurement constraints. ([Ifaa78](https://android-review.googlesource.com/#/q/Ifaa78911b26c5bc2eecfbb31ab5e8b531da42270))
- Added `SubspaceModifier.onSizeChanged` that provides a simple, focused callback for developers to react when a `@SubspaceComposable`'s size changes. ([I994f9](https://android-review.googlesource.com/#/q/I994f926cd7189e37ab37aac2a38430052922ec07))
- Removed the Volume API. The `SceneCoreEntity` API should be used instead of the Volume API. ([I4162b](https://android-review.googlesource.com/#/q/I4162b33bd22244d38e9593a658127a6aa5f2047a))
- Split `SubspaceLayoutModifierNode.requestRelayout` into `invalidateMeasurement/invalidatePlacement`. ([I14805](https://android-review.googlesource.com/#/q/I14805caba6baa1f4055aacc8c1c47015f8b14d78))
- Added the `SpatialGltfModel` API that allows developers to render glTFs in compose. ([Icc91f](https://android-review.googlesource.com/#/q/Icc91f672f13622c9c136d41bad9f9b09b055b541))
- Introduced the `SpatialGltfModel` composable API for easily rendering glTFs ([Iade67](https://android-review.googlesource.com/#/q/Iade67a7e07440f85c62779b6a75ce9be07f5754c))

**Bug Fixes**

- Fixed a layout bug in `SceneCoreEntity`. It should now properly respect its constraints. ([I11bb8](https://android-review.googlesource.com/#/q/I11bb838de7fd357f09febfa63a743bf78aa78a2e))
- Lower jxr-compose modules to `Compile sdk = 34` ([I2d5db](https://android-review.googlesource.com/#/q/I2d5db3bfc2acd903fbd76d7fb677170aa3de84ee))

### Version 1.0.0-alpha08

October 22, 2025

`androidx.xr.compose:compose:1.0.0-alpha08` and `androidx.xr.compose:compose-testing:1.0.0-alpha08` are released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5e032601bca53b499bd4725e4cdb975643bc3c2a..91b842c20be0cfd3185e2953615ea38c4707bf34/xr/compose).

**API Changes**

- Changed `ResizePolicy` to accept `onResizeStart`, `onResizeUpdate`, and `onResizeEnd`. ([I7e21f](https://android-review.googlesource.com/#/q/I7e21f8ed412b2f46fd8d6f3ddd1f3a67cd8ea54a))

**Bug Fixes**

- Prevent crash when destroying an Activity with a Subspace. ([I595a1](https://android-review.googlesource.com/#/q/I595a1aee4a52f322c36c98625d689b38d8017e3f))

### Version 1.0.0-alpha07

September 24, 2025

`androidx.xr.compose:compose:1.0.0-alpha07` and `androidx.xr.compose:compose-testing:1.0.0-alpha07` are released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e21507177b82f0dd17c8323b7362ac89fede28ce..5e032601bca53b499bd4725e4cdb975643bc3c2a/xr/compose).

**API Changes**

- Improved KDocs for `SpatialMainPanel`. ([I27b70](https://android-review.googlesource.com/#/q/I27b70fac09898875d52441edfab06cf14137fcd7), [b/444467891](https://issuetracker.google.com/issues/444467891))
- Introduced `SpatialArrangement` for arranging children along the main axis in 3D layouts like `SpatialRow` and `SpatialColumn`. This new API provides familiar arrangement options from 2D Compose, including `Start`, `End`, `Center`, `SpaceBetween`, `SpaceAround`, and `SpaceEvenly`, with full support for both LTR and RTL layout directions. ([I7db38](https://android-review.googlesource.com/#/q/I7db38a094fa3fb7d5920e3a17d14e19f4d9eb38d), [b/436289959](https://issuetracker.google.com/issues/436289959))
- Added a base interface for `SubspaceModifier.Node` to improve type safety and usability of extension interfaces; such as
  - `CompositionLocalConsumerSubspaceModifierNode`
  - `LayoutCoordinatesAwareModifierNode`
  - `SubspaceLayoutModifierNode`
  - `CoreEntityNode` (internal) ([Iede00](https://android-review.googlesource.com/#/q/Iede00f60a7bdf6cfec12a6d60c806431a119de58), [b/440599394](https://issuetracker.google.com/issues/440599394), [b/440599394](https://issuetracker.google.com/issues/440599394))
- Unrestrict `SpatialExternalSurface` ([I33315](https://android-review.googlesource.com/#/q/I33315c3dd13629c3e3695423412b821ad2f22f9e), [b/439646773](https://issuetracker.google.com/issues/439646773))
- Introduce `SubspaceModifier` to Subspace composables and replace constraints parameter with `SubspaceModifier` with size-related `SubspaceModifiers`. If `allowUnboundedSubspace` is true, Subspaces can still have unbounded constraints. ([Ib06e6](https://android-review.googlesource.com/#/q/Ib06e6d268a161e8e132766668df5a48c9659bd6b), [b/433331675](https://issuetracker.google.com/issues/433331675))
- Deprecating movable and resizable `SubspaceModifiers` now that `DragPolicy()` and `ResizePolicy()` are a part of the `SpatialPanel` and `SpatialExternalSurface` API ([I397bf](https://android-review.googlesource.com/#/q/I397bfdf44df081865b27b7aeb67e278ea3d025ac), [b/437924639](https://issuetracker.google.com/issues/437924639))
- Added support for `LayoutDirection` in spatial layouts. Composable using `SpatialAlignment` will now correctly position elements in both LTR and RTL contexts. ([I964bb](https://android-review.googlesource.com/#/q/I964bb0096283b2ab16b69d3b5d51453eb9c6523d), [b/436300273](https://issuetracker.google.com/issues/436300273))
- Add Resizable and Movable parameters to the `Panel` APIs to ensure that these behaviors can only be applied to supported containers. ([Id491c](https://android-review.googlesource.com/#/q/Id491cf18ef769997914f493dcfa8ce8bcd146c03))
- Added `sizeIn`, `widthIn`, `heightIn`, `depthIn` `SubspaceModifiers` that let you set exact minimum and maximum constraints for width, height and depth. ([I1af09](https://android-review.googlesource.com/#/q/I1af0960b4a616d3144773df278c6db2c8de27b2e), [b/433330761](https://issuetracker.google.com/issues/433330761))

### Version 1.0.0-alpha06

August 13, 2025

`androidx.xr.compose:compose:1.0.0-alpha06` and `androidx.xr.compose:compose-testing:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/102c5e13657cf0731ff209d71be7248a2aec274d..e21507177b82f0dd17c8323b7362ac89fede28ce/xr/compose).

**Bug Fixes**

- Recreate the `ComposeXrOwnerLocals` when the lifecycle owner is destroyed. ([9123ce1](http://android.googlesource.com/platform/frameworks/support/+/9123ce11474ab7e5016dcbdaa094f1ae8f485607))

### Version 1.0.0-alpha05

July 30, 2025

`androidx.xr.compose:compose:1.0.0-alpha05` and `androidx.xr.compose:compose-testing:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..102c5e13657cf0731ff209d71be7248a2aec274d/xr/compose).

**New Features**

- Made `SubspaceComposable` annotation class public. ([Ic2a34](https://android-review.googlesource.com/#/q/Ic2a34011e1f648b62102ad117b673858d10c16fa), [b/399432430](https://issuetracker.google.com/issues/399432430))
- Two new `SpatialExternalSurface` Composables representing 180 and 360 degree spheres. ([I40ef2](https://android-review.googlesource.com/#/q/I40ef2b289ec1e956e2979e37ca17b7bdbf999f18), [b/391705799](https://issuetracker.google.com/issues/391705799))
- Added `SubspaceModifier.aspectRatio` ([Ide5ab](https://android-review.googlesource.com/#/q/Ide5abb4689db0ad03abe5de42f97357788f6c5a4), [b/399729509](https://issuetracker.google.com/issues/399729509), [b/414762147](https://issuetracker.google.com/issues/414762147))
- Added the `SceneCoreEntity` API to improve interoperability between `SceneCore` and Compose for XR. ([I50bb3](https://android-review.googlesource.com/#/q/I50bb3781c764042066f95c7c11f15be6456ad48b), [b/423020989](https://issuetracker.google.com/issues/423020989))
- Provided `GravityAlignedsubspace` API to support the unscaled And `GravityAligned` feature ([I07359](https://android-review.googlesource.com/#/q/I073595e109e3f3bbd88fef8872c4f7d0c654fe3c))

**API Changes**

- `SpatialDialog()` will follow `SpatialDialogProperties.dismissOnBack` press configuration. ([Ib453b](https://android-review.googlesource.com/#/q/Ib453b669d962f0d1287249b497dbf6a9e65f84ce), [b/416797132](https://issuetracker.google.com/issues/416797132))
- Update `minimumPanelDimension` to a new default Dimension size of `Dimensions(0.1f, 0.1f, 0.1f)` due its representation in Meters. ([Ib852a](https://android-review.googlesource.com/#/q/Ib852a9a946e2fdc0168cea12d8e1f9039bdc31cc))
- Subspaces and Orbiters will now retain their internal state in home space and when the app is in the background. In home space mode, Subspace will still set up its scene in preparation for the switch to full space mode. ([I40317](https://android-review.googlesource.com/#/q/I403176b040bbeb62ea0c4ab098992a6232da1c1d), [b/416037751](https://issuetracker.google.com/issues/416037751))
- `SpatialDialogs` will now retain their state when the app is in the background. ([I6aa56](https://android-review.googlesource.com/#/q/I6aa56cb52092904678ad6bfea68e2002a09fe5ce))
- `ApplicationSubspace` will now inherit its recommended scale and position from the system. ([I4565f](https://android-review.googlesource.com/#/q/I4565f833ebba43fd643af2c5c0ae18f80a62fe0d), [b/418834194](https://issuetracker.google.com/issues/418834194))
- Added a better error message and trigger the error earlier when a `SubspaceComposable` is used in a non-`SubspaceComposable` context. ([Iee2ae](https://android-review.googlesource.com/#/q/Iee2ae9bb02fca1f14e52238871663ce709fa9bc4), [b/416484684](https://issuetracker.google.com/issues/416484684))
- Updating `ExperimentalSubspaceVolumeApi` from Warning to Error because warnings are often overlooked when misusing composable APIs. ([I427aa](https://android-review.googlesource.com/#/q/I427aad29f283d9df21cd6f2582f78bd3024f90f6), [b/424864286](https://issuetracker.google.com/issues/424864286))
- Subspace and `ApplicationSubspace` are now constrained by `recommendedContentBoxInFullSpace`. Previously it was constrained by `SpatialUser`'s Field of View. ([I41015](https://android-review.googlesource.com/#/q/I410151b4d76b8485e9e1ec276e0f32b9a2cd9680), [b/423074142](https://issuetracker.google.com/issues/423074142))
- Update `SpatialElevation` to use min size to no longer use hard coded size ([I2dbe6](https://android-review.googlesource.com/#/q/I2dbe6650fa3a8f4e0e023e5d742140767903de11), [b/427785338](https://issuetracker.google.com/issues/427785338))
- Update how we scrim the `SpatialAcitivityPanel` to update when a key variable is modified. ([I0f64d](https://android-review.googlesource.com/#/q/I0f64d7b9885283db7a5a320785e586f1afd73405), [b/427999029](https://issuetracker.google.com/issues/427999029))
- Remove `VolumeConstraints.Unbounded` in favor of setting the default constraint values to the equivalent. ([Ie24ec](https://android-review.googlesource.com/#/q/Ie24ec47de60979cdf5375325fb13bb8b2db36294), [b/407938414](https://issuetracker.google.com/issues/407938414))
- `SpatialFeatheringSize` is no longer public ([I1c15b](https://android-review.googlesource.com/#/q/I1c15bd5ec258ad5f45490dd786ded7f80f00ac8a), [b/399432430](https://issuetracker.google.com/issues/399432430))
- Renamed the XR `Placeable` to `SubspacePlaceable` to distinguish it from Compose's `Placeable`. ([I74874](https://android-review.googlesource.com/#/q/I748741bebe814381cc90cdace5f2dfcb4234572e))
- Removing Orbiter settings and adding `shouldRenderInNonSpatial` as a new param. In addition, removing class `EdgeOffset` and adding `orbiterOffsetType` as a new param to consolidate `Orbiter()` Functions. As well as renaming `OrbiterEdge` to `ContentEdge`. ([Iebf3d](https://android-review.googlesource.com/#/q/Iebf3d87a149f8a8b691758ca86da2b51ebcb480b))
- Renamed `Measurable` to `SubspaceMeasurable` to differentiate the type from Compose's `Measurable` type. ([I9726c](https://android-review.googlesource.com/#/q/I9726cb6ab1f7fe925296e5f0a4be383ddd1c8d19))
- Rename `MeasureResult` to `SubspaceMeasureResult` ([I9f34d](https://android-review.googlesource.com/#/q/I9f34d7542efa8941c050933ddf64e905cf830f52))
- Removed the `setSubspaceContent` API in favor of using Compose's `setContent` with a `Subspace` composable. ([Ifff4c](https://android-review.googlesource.com/#/q/Ifff4ccd5e05510e9d7966a5b9a3d3ea98926ff09), [b/421427391](https://issuetracker.google.com/issues/421427391), [b/421427391](https://issuetracker.google.com/issues/421427391))
- `MeasurePolicy` is renamed to `SubspaceMeasurePolicy`. ([I37a9b](https://android-review.googlesource.com/#/q/I37a9b4e5ff3fbaca78888adbd1a3ca6b2f202c86), [b/422553904](https://issuetracker.google.com/issues/422553904))
- Turn `SubspaceSemanticsInfo` into a sealed interface because we won't be able to add members without the defaults. ([I372f9](https://android-review.googlesource.com/#/q/I372f989d2fa779aa304d354bcd2d53a39d3a267c), [b/423704068](https://issuetracker.google.com/issues/423704068))
- Updated `SpatialExternalSurface` documentation, renamed `ContentSecurityLevel` to `SurfaceProtection` ([I3c460](https://android-review.googlesource.com/#/q/I3c4602fe56b8a88c8c1398354517c7ee04287a95), [b/420982808](https://issuetracker.google.com/issues/420982808))
- Provided overloaded constructor for movable modifier which allows anchoring. ([Ic0c70](https://android-review.googlesource.com/#/q/Ic0c70e86c0be734b7f8bdda14f5501a4a57cd5e4))
- Add more position provider for tooltips so now developers can control if the tooltip is placed above, below, left, or right of the anchor. Add an API that takes in a Shape for carets, so more custom shapes can be provided. ([Ie513c](https://android-review.googlesource.com/#/q/Ie513c947d881a2afc8dea1f09929dc58bacf29d5), [b/374766087](https://issuetracker.google.com/issues/374766087), [b/418854637](https://issuetracker.google.com/issues/418854637))
- Removed `CoreEntity` as a `PublishedApi` ([Ifee05](https://android-review.googlesource.com/#/q/Ifee0510597f39cad2b21f781c1965aa8f138b15a))

**Bug Fixes**

- Fixed issue where `SpatialDialog` would flash when being rendered. ([Ife73c](https://android-review.googlesource.com/#/q/Ife73c018a39141e0d1d524709d4577b1372c09e3), [b/401619909](https://issuetracker.google.com/issues/401619909))
- Fixes issue where `SpatialDialog` could not scrim the Activity Panel. ([I8ca6c](https://android-review.googlesource.com/#/q/I8ca6cdec18e09dad6b93dcdc4c730e722c789594),[b/367442109](https://issuetracker.google.com/issues/367442109))
- Fix XR dialog not showing some content ([I17cd5](https://android-review.googlesource.com/#/q/I17cd55c3a6d6dd5b36efb7b3f893b684701cd262), [b/418062437](https://issuetracker.google.com/issues/418062437))
- Fixed issue where `SpatialPopup` was being dismissed when clicked inside of the content. ([If262c](https://android-review.googlesource.com/#/q/If262c68747574f6cc986f23189ee2f67ad779af2), [b/417245722](https://issuetracker.google.com/issues/417245722))
- Fixed the issue where when chaining `resizable().movable()` the SpatialPanel failed to resize correctly to the new size. ([I02ee3](https://android-review.googlesource.com/#/q/I02ee3379dbc0632c22635f2511e6416593c66e8c), [b/422264230](https://issuetracker.google.com/issues/422264230))
- Fixed `topBar` overlapping with menu in `SpatialComposeVideoPlayer` ([Id33bc](https://android-review.googlesource.com/#/q/Id33bca8c50ddf46a49030de88b8367dd82c5e8a6), [b/427168167](https://issuetracker.google.com/issues/427168167))
- Fixed corner radius not rendering ([I975fe](https://android-review.googlesource.com/#/q/I975fe535847f49784982cc0483720df778f185dd), [b/428261830](https://issuetracker.google.com/issues/428261830))

### Version 1.0.0-alpha04

May 7, 2025

`androidx.xr.compose:compose:1.0.0-alpha04` and `androidx.xr.compose:compose-testing:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/043342a8810f3356110a0afce48c662e841c428f..b6c541571b9fb5471f965fc52612cb280713e5e4/xr/compose).

> [!NOTE]
> **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

**New Features**

- Added `CompositionLocalConsumerSubspaceModifierNode` interface to allow custom `SubspaceModifier` types to access composition local values.
- Added a new `SpatialPanel` API that follows the compose `AndroidView` implementation style and deprecates the previous `ViewBased SpatialPanel`.
- Added `VolumeConstraints.Unbounded` companion object which represents unbounded constraints.
- Added `SubspaceModifier.onPointSourceParams` to allow a spatialized audio source.
- A public `ApplicationSubspace` has been added, offering optional `VolumeConstraints` to define a 3D area where the app can render spatial content. By default, if no constraints are specified, the Subspace will be bounded by the `SpatialUser`'s current field of view in width and height. Users can provide constraints to be used if the field of view cannot be determined. Otherwise, the default field of view width and height values are used.
- Added `SpatialExternalSurface`, which can be used to render stereoscopic content. `SpatialExternalSurface` is customizable with modifiers (except alpha), and an edge feathering effect.
- Added a new `pointerHoverIcon` Subspace Modifier that allows users to set the icon for the spatial pointer.

**API Changes**

- Removed `RequiresApi(34)` restriction on all Jetpack XR packages. This restriction was redundant as Jetpack XR is currently only available on devices with API level 34+. ([Iae0f8](https://android-review.googlesource.com/#/q/Iae0f8f1c0de1d62609ed0dcad6cf2731756054dd))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Back handling will now work on spatial panels without embedded activities. For back handling to work you need to specify `android:enableOnBackInvokedCallback="true"` in the android manifest.
- Backhandling will now work on spatial dialogs. For backhandling to work you need to specify `android:enableOnBackInvokedCallback="true"` in the android manifest.
- Compose-based and View-based `SpatialPanel`s can now size themselves based on their contents.
- Developers may now set their own custom `SpatialElevationLevel` values and are not limited to the predefined levels.
- Orbiter elevation level may now be customized via the `elevation` parameter.
- Subspace can now be bounded by the `SpatialUser`'s field of view in width and height by default. If the field of view cannot be determined, the default field of view width and height values are used.
- Added new callbacks `onMoveStart` and `onMoveEnd` to the `Movable` modifier. The `onMoveStart` and `onMoveEnd` callbacks are called when the user starts and ends moving a subspace composable with the movable modifier.
- The `name` parameter has been removed from spatial APIs such as `SpatialRow` and `SpatialPanel`. For debugging spatial compose trees use `SubspaceModifier.testTag` instead.
- Removed an unsupported overload of `SpatialPopup` that only has `spatialElevationLevel` and `content`. Please use the interface that supports `onDimissRequest`.
- The `onPoseChange` callback from the Movable modifier has been removed. Use `onMove` instead.
- `SubspaceModifiers` will no longer apply their effects if they are detached or currently detaching.
- The existing `SpatialRow` API has been split into `SpatialRow` and `SpatialCurvedRow`. If previously using `SpatialRow`'s `curveRadius` parameter, use `SpatialCurvedRow` now instead which offers the same behavior.
- `MainPanel` and `ActivityPanel` no longer have title bars when run on a similarly recent system image.
- Alpha and scale modifiers are now stackable and will multiply their values for the final applied alpha or scale value.
- The `onPoseChange` callback from the Movable modifier has been optimized to perform smoother pose movement.
- The movable and resizable modifiers will now perform their callbacks on the main thread to ensure that state changes will trigger recomposition.
- Added state observation to the layout and measure phases to ensure that state changes in `SubspaceLayout` will trigger relayout.
- Optimized modifier chain updates to better reuse existing modifiers.

**Bug Fixes**

- Stopped scrimming when a `SpatialDialog` is shown. ([Ic4594](https://android-review.googlesource.com/#/q/Ic4594fc7a668877b4c32652f2929962c3512cc64))
- Relayout requests made while modifier nodes are detached will now be ignored.
- Removed relayout phases triggered by Movable and Resizable modifiers.
- Fixed a crash in `MainPanel()` composable that occurred when either dimension was set to zero, either directly or during a layout calculation, e.g., a `SpatialRow/SpatialColumn` calculation. The panel will now be hidden instead. Note that this fix specifically addresses crashes during the layout phase; resizing the panel to zero via user interaction will be handled separately. The hidden panel lacks UI affordances.
- Fixed issue with `maintainAspectRatio` from the resizable modifier. The aspect ratio should be kept now.
- Fixed an issue with nested Subspaces where they would be incorrectly positioned for a single frame.
- Fixed issue where rounded corners were sometimes not applied when they should be.
- `NestedSubspaces` will no longer appear for one frame in the wrong location.

### Version 1.0.0-alpha03

February 26, 2025

`androidx.xr.compose:compose:1.0.0-alpha03` and `androidx.xr.compose:compose-testing:1.0.0-alpha03` are released with no notable changes since the last alpha. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a96c4899cab90642c7b1d722dc1f3b45f56e7b82..043342a8810f3356110a0afce48c662e841c428f/xr/compose)

### Version 1.0.0-alpha02

February 12, 2025

`androidx.xr.compose:compose:1.0.0-alpha02` and `androidx.xr.compose:compose-testing:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2e2729abc59df52d40af80a8bbfe010c02455c6..a96c4899cab90642c7b1d722dc1f3b45f56e7b82/xr/compose).

**New Features**

- The Activity Panel can now scrim its content when a Spatial Dialog is activated.
- The `Orbiter` API is now usable in `SubspaceComposable` contexts and will attach Orbiters to their nearest `SubspaceLayout`-based composable parent.
- Introduced `LayoutCoordinatesAwareModifierNode` to allow custom positioning-based modifiers.
- Added attach/detach lifecycle methods to `SubspaceModifier.Node`.
- Added `scaleWithDistance` to the movable modifier. When `scaleWithDistance` is enabled, the subspace element moved will grow or shrink. It will also maintain any explicit scale that it had before movement.

**API Changes**

- Removed `SessionCallbackProvider` in favor of `SpatialCapabilities`.

**Other changes**

- Reduced `minSDK` to 24. All Jetpack XR APIs continue to require API 34 at runtime.
- `Orbiter` `EdgeOffset.inner`, `EdgeOffset.outer`, and `EdgeOffset.overlap` constructors are no longer `@Composable` methods, which allows them to be used in non-composable contexts.
- Update Spatial Elevation Levels to match the latest UX spec.
- Implement `SubspaceSemanticsInfo` interface into `MeasurableLayout`.
- Renamed `SubspaceModifierElement` to `SubspaceModifierNodeElement`.

**Bug fixes**

- Fixes to stabilize `SubspaceModifier` ordering. `SubspaceModifier` should behave more reliably. Offset, rotate, scale, movable, and resizable modifier should now be usable in any order.

### Version 1.0.0-alpha01

December 12, 2024

`androidx.xr.compose:compose-*1.0.0-alpha01` is released.

**Features of Initial Release**

- Initial developer release of Jetpack Compose for XR. Use familiar Compose concepts such as rows and columns to create spatial UI layouts in XR, whether you're porting an existing 2D app to XR or creating a new XR app from scratch. This library provides subspace and spatial composables: such as spatial panels and orbiters, which let you place your existing 2D Compose or Views-based UI in a spatial layout. It introduces the Volume subspace composable, which allows you to place SceneCore entities, such as 3D models, relative to your UI. Learn more in this [developer guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui):

  - [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Subspace(kotlin.Function1)): This composable can be placed anywhere within your app's UI hierarchy, allowing you to maintain layouts for 2D and spatial UI without losing context between files. This makes it easier to share things like existing app architecture between XR and other form factors without needing to hoist state through your whole UI tree or re-architect your app.

  - [SpatialPanel](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(android.content.Intent,androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.String,androidx.xr.compose.subspace.layout.SpatialShape)): A spatial panel is a subspace composable that lets you display app content--for example, you could display video playback, still images, or any other content in a spatial panel.

  - [Orbiter](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Orbiter(androidx.xr.compose.spatial.OrbiterEdge.Horizontal,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Horizontal,androidx.xr.compose.spatial.OrbiterSettings,androidx.xr.compose.subspace.layout.SpatialShape,kotlin.Function0)): An orbiter is a spatial UI component. It's designed to be attached to a corresponding spatial panel, and contains navigation and contextual action items related to that spatial panel. For example, if you've created a spatial panel to display video content, you could add video playback controls inside an orbiter.

  - [Volume](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#Volume(androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.String,kotlin.Function1)): Place SceneCore entities, such as 3D models, relative to your UI.

- Spatial Layout:
  You can create multiple spatial panels and place them within a Spatial Layout using [`SpatialRow`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialRow(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,androidx.compose.ui.unit.Dp,kotlin.String,kotlin.Function1)), [`SpatialColumn`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialColumn(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,kotlin.String,kotlin.Function1)), [`SpatialBox`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialBox(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,kotlin.Boolean,kotlin.String,kotlin.Function1)), and [`SpatialLayoutSpacer`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialLayoutSpacer(androidx.xr.compose.subspace.layout.SubspaceModifier)).
  Use `SubspaceModifier`s to customize your layout.

- Spatial UI components: These elements can be reused in your 2D UI, and their spatial attributes will only be visible when spatial capabilities are enabled.

  - [`SpatialDialog`](https://developer.android.com/kotlin/androidx/xr/compose/spatial/package-summary#SpatialDialog(kotlin.Function0,androidx.xr.compose.spatial.SpatialDialogProperties,kotlin.Function0)): Panel will push slightly back in z-depth to display an elevated dialog.
  - [`SpatialPopUp`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#SpatialPopup(androidx.xr.compose.spatial.SpatialElevationLevel,kotlin.Function1)): Panel will push slightly back in z-depth to display an elevated popup
  - [`SpatialElevation`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#SpatialElevation(androidx.xr.compose.spatial.SpatialElevationLevel,kotlin.Function0)): `SpatialElevationLevel` can be set to add elevation.
- SpatialCapabilities: Spatial capabilities can change as users interact with your app or the system, or can even be changed by your app itself---for example, moving into Home Space or Full Space. To avoid issues, your app needs to check for [`LocalSpatialCapabilities.current`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSpatialCapabilities()) to determine which APIs are supported in the current environment.
  [`isSpatialUiEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialUiEnabled()): [Spatial UI elements](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) (e.g. SpatialPanel)
  [`isContent3dEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isContent3dEnabled()): [3D objects](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models)
  [`isAppEnvironmentEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isAppEnvironmentEnabled()): The [environment](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments)
  [`isPassthroughControlEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isPassthroughControlEnabled()): Whether or not the application can control the passthrough state
  [`isSpatialAudioEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialAudioEnabled()): [Spatial audio](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio)

**Known Issues**

- Currently a minSDK of 30 is required to use Jetpack Compose for XR. As a workaround you may add the following manifest entry `<uses-sdk tools:overrideLibrary="androidx.xr.scenecore, androidx.xr.compose"/>` to be able to build and run with a minSDK of 23.
- Jetpack XR apps currently require requesting `android.permission.SCENE_UNDERSTANDING` permission in the AndroidManifest.
- When an app launches directly into Full Space using the `PROPERTY_XR_ACTIVITY_START_MODE` property in their manifest, Activities/Applications are initially opened in Home Space before transitioning into Full Space.
- glTFs in Volume Composables may initially flicker at the wrong location.
- Using a SpatialDialog in a panel that has been moved significantly will push the content in the wrong direction.