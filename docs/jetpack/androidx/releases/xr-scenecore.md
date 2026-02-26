---
title: https://developer.android.com/jetpack/androidx/releases/xr-scenecore
url: https://developer.android.com/jetpack/androidx/releases/xr-scenecore
source: md.txt
---

# Jetpack SceneCore

[User Guide](https://developer.android.com/develop/devices/xr/jetpack-xr-sdk) [Code Sample](https://github.com/android/xr-samples) API Reference  
[androidx.xr.scenecore](https://developer.android.com/reference/androidx/xr/scenecore/package-summary)  
[androidx.xr.scenecore.testing](https://developer.android.com/reference/androidx/xr/scenecore/testing/package-summary)  
Build and manipulate the Android XR scene graph with 3D content.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | - | - | - | [1.0.0-alpha12](https://developer.android.com/jetpack/androidx/releases/xr-scenecore#1.0.0-alpha12) |

## Declaring dependencies

To add a dependency on XR SceneCore, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.scenecore:scenecore:1.0.0-alpha12"

    // Optional dependencies for asynchronous conversions
    implementation "androidx.xr.scenecore:scenecore-guava:1.0.0-alpha12"

    // Use to write unit tests
    testImplementation "androidx.xr.scenecore:scenecore-testing:1.0.0-alpha12"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.scenecore:scenecore:1.0.0-alpha12")

    // Optional dependencies for asynchronous conversions
    implementation("androidx.xr.scenecore:scenecore-guava:1.0.0-alpha12")

    // Use to write unit tests
    testImplementation("androidx.xr.scenecore:scenecore-testing:1.0.0-alpha12")
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

### Version 1.0.0-alpha12

February 25, 2026

`androidx.xr.scenecore:scenecore-*:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/858c4795b789900a14f261bc90ed7e375af2b9be..bf48d1095789789d9d62bfd42bb4f8c9a335ecea/xr/scenecore).

**Known Issues**

- Anchored entities may snap from their anchored position to the activity space origin after several seconds.

**API Changes**

- `ActivitySpace.addOnSpaceUpdatedListener` and `ActivitySpace.removeOnSpaceUpdatedListener` have been renamed to `addOnOriginChangedListener` and `removeOnOriginChangedListener`. `AnchorEntity.setOnSpaceUpdatedListener` has been renamed to `setOnOriginChangedListener`. ([I5d8fb](https://android-review.googlesource.com/#/q/I5d8fb8dc2994f2241c03c9adab17dfa56c11eb6f))
- Added public name property to `FakeEntity` and made view public on `FakePanelEntity`. ([Ifa1f9](https://android-review.googlesource.com/#/q/Ifa1f9ed8b3116c2baba71cec85659d944feb42e8))

**Bug Fixes**

- Fixed pixel density calculations on newer system images ([I57d04](https://android-review.googlesource.com/#/q/I57d043ac72367c8765502991141c42389bf9e9d9))

### Version 1.0.0-alpha11

January 28, 2026

`androidx.xr.scenecore:scenecore-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bac172b1818f60ee3cd443ab6ae6596338aa5215..858c4795b789900a14f261bc90ed7e375af2b9be/xr/scenecore).

**API Changes**

- Renames `PerceivedResolutionResult.InvalidCameraView` to `PerceivedResolutionResult.InvalidRenderViewpoint` as the `getPerceivedResolution` APIs now rely on ARCore's `RenderViewpoint` API instead of `CameraViewScenePose`. This name better reflects the new implementation. ([I8c967](https://android-review.googlesource.com/#/q/I8c967b7b3091f445716aae2d7ca552a0ae4bdb9b), [b/446989745](https://issuetracker.google.com/issues/446989745), [b/419311998](https://issuetracker.google.com/issues/419311998))
- The `PanelEntity`/`SurfaceEntity.getPerceivedResolution` methods now take a `RenderViewpoint` provided by the developer as an argument. Before, the runtime arbitrarily chose the `RenderViewpoint` used in the perceived resolution calculation. ([I8c967](https://android-review.googlesource.com/#/q/I8c967b7b3091f445716aae2d7ca552a0ae4bdb9b), [b/446989745](https://issuetracker.google.com/issues/446989745), [b/419311998](https://issuetracker.google.com/issues/419311998))
- Removed `SpatialUser`, `ScenePose.Head`, and `ScenePose.CameraView`. The functionality of these APIs is covered by the `ArDevice` and `RenderViewpoint` APIs within ARCore for Jetpack XR. To obtain a `ScenePose` corresponding to the user's head or left or right eye, developers can use `PerceptionSpace.getScenePoseFromPerceptionPose` with the appropriate pose obtained using ARCore APIs. ([I2f69c](https://android-review.googlesource.com/#/q/I2f69c3d74f123f64efe2c7c9d41826a2f0f1ae28), [b/446989745](https://issuetracker.google.com/issues/446989745))

### Version 1.0.0-alpha10

December 03, 2025

`androidx.xr.scenecore:scenecore-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2f33cda7973a5fca1f200764ce1adaf32540a7d5..bac172b1818f60ee3cd443ab6ae6596338aa5215/xr/scenecore).

**API Changes**

- Added `transformPixelCoordinatesToPose` and `transformNormalizedCoordinatesToPose` to `PanelEntity` ([I462b3](https://android-review.googlesource.com/#/q/I462b308e11becbc5718ed81c797dc92a795f6c27))
- Added a helper class, Utils, to `SceneCore` Runtime based on logic in `SceneCore` ([I570b9](https://android-review.googlesource.com/#/q/I570b92336e3f96438ffefe02c4780480761dece8))

**Bug Fixes**

- Fixed a potential crash that can occur when Session is destroyed and a `SpatialModeChangeEvent` is received ([If44e8](https://android-review.googlesource.com/#/q/If44e858108a5f29f69a10cd17bce551abfebbb02))
- Fixed a bug which could cause an `IllegalStateException` to be thrown when leaving or re-entering an Activity. ([Ibff1c](https://android-review.googlesource.com/#/q/Ibff1cf591f2917f3f20340f063b8fb69e9b35da2))

### Version 1.0.0-alpha09

November 19, 2025

`androidx.xr.scenecore:scenecore-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fcb8595c5d66b0a2d43ae985efed1ff14fa92da1..2f33cda7973a5fca1f200764ce1adaf32540a7d5/xr/scenecore).

**New Features**

- Adds an API for retrieving a `ScenePose` that represents the composition of the perception space origin pose and a pose with respect to the perception space origin. ([I5b50a](https://android-review.googlesource.com/#/q/I5b50a282fee4e643bbb07487317ea749d216c808))
- Added `getGravityAlignedPose` function. The gravity aligned pose ignores the Pitch and Roll of rotation. ([I5ae21](https://android-review.googlesource.com/#/q/I5ae218eabe7a2c946bddd297f483f5fa2fd07052))
- `AnchorEntity.State` constant types have been changed from Ints to State subtypes. ([Ib0c49](https://android-review.googlesource.com/#/q/Ib0c49642c322348f40ff7205f857d6032a8853bd))
- Added `getChildren()` to Entity interface. Updated `MainPanelEntity` lifecycle. ([Ia69d6](https://android-review.googlesource.com/#/q/Ia69d6c7e5cdb7b8fd269f4dddf72cdbc67b34ad5))

**API Changes**

- `PointerCaptureComponent.PointerCaptureState` constant types have been changed from Ints to `PointerCaptureState` subtypes. ([Ic888a](https://android-review.googlesource.com/#/q/Ic888a3cf67a7be6fa749b8acfb4156c2d34a49c2))
- `Scene.spatialCapabilities` is now of type `Set<SpatialCapability>` instead of an Int field. The `SpatialCapability` constants have been renamed. ([I9c109](https://android-review.googlesource.com/#/q/I9c1096e70b530c0d7564117d2cccc0c538d4c2cf))
- `SurfaceEntity` constant types have been renamed and changed from Ints to `SurfaceEntity` subtypes. ([I419ed](https://android-review.googlesource.com/#/q/I419edfac64e41f071e9b01a68b416ad0e06f2424))
- `SpatializerConstant` constant types have been renamed and changed from Ints to `SpatializerConstant` subtypes. ([Ia0e18](https://android-review.googlesource.com/#/q/Ia0e184fb23b78420e11fd9048e7ec7082c08c34c))
- `TextureSampler` constant types have been renamed and changed from Ints to `TextureSampler` subtypes. ([I44078](https://android-review.googlesource.com/#/q/I440787f30a0c7af2a1bf5bf6a3be8eba97a04a83))
- `SpatialVisibility` constant types have been changed from Ints to `SpatialVisibility` subtypes. ([I70739](https://android-review.googlesource.com/#/q/I70739cc1437f3840ee1321c25ebb1d73926fe781))
- `ResizeEvent.ResizeState` constant types have been renamed and changed from Ints to `ResizeState` subtypes. ([I384d5](https://android-review.googlesource.com/#/q/I384d5e31c6fb29725ec34fbfed8b36e0233708d1))
- `InputEvent` constant types have been renamed and changed from Ints to inherit from their respective enclosing type. ([I82817](https://android-review.googlesource.com/#/q/I828174001ffe242ca57c2e4ad857c6e7a7af2f32))
- `GltfModelEntity.AnimationState` constant types have been changed from Ints to `AnimationState` subtypes. ([I24f4e](https://android-review.googlesource.com/#/q/I24f4e5751e77c08b434d3063c385f37e82ad0997))
- `AlphaMode` constant types have been renamed and changed from Ints to `AlphaMode` subtypes. ([I27b56](https://android-review.googlesource.com/#/q/I27b56553658d06d40f00115b32cc60e44f88367c))
- `Space` constant types have been changed from Ints to Space subtypes. ([I9255b](https://android-review.googlesource.com/#/q/I9255bff50a69a154dd58b7304552daa70512b7fc))
- `ScenePose.hitTest` and related methods now return `null` if no intersection was found, instead of a `HitTestResult` with a null `hitPosition`. `HitTestResult.hitPosition` is no longer nullable. ([I1400a](https://android-review.googlesource.com/#/q/I1400a3daaac70ec50f99a11d5548038474f45de6))
- Changed references of `ActivityPose` to `ScenePose`. ([I7fe43](https://android-review.googlesource.com/#/q/I7fe43b72793a4597abd2bc5913d3a4bae368c451))

### Version 1.0.0-alpha08

October 22, 2025

`androidx.xr.scenecore:scenecore-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9dcef8caadcc3ef1c1eb670d1da2553621a5017b..fcb8595c5d66b0a2d43ae985efed1ff14fa92da1/xr/scenecore).

**API Changes**

- Renamed `ActivityPanelEntity.moveActivity` to `transferActivity` ([I273c5](https://android-review.googlesource.com/#/q/I273c5a971621a72949a04a6d64a0cc787bf73c29), [b/430332856](https://issuetracker.google.com/issues/430332856))

**Bug Fixes**

- `:xr:scenecore:scenecore-spatial-rendering` and `:xr:scenecore:scenecore-spatial-core` added as implementation dependency of `:xr:scenecore:scenecore` ([I6ab65](https://android-review.googlesource.com/#/q/I6ab6593c092fcfbd1e8f0f4cc4bb7398fd75ec6a), [b/447000520](https://issuetracker.google.com/issues/447000520))
- Exception is thrown if `session.scene` is accessed after session destruction. ([I77e6f](https://android-review.googlesource.com/#/q/I77e6fb4a6e96073baa481f34127741af0640bd06))

### Version 1.0.0-alpha07

September 24, 2025

`androidx.xr.scenecore:scenecore:1.0.0-alpha07`, `androidx.xr.scenecore:scenecore-guava:1.0.0-alpha07`, and `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha07` are released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a54f47329f5dd47722a43b92814d5c7278a434ce..9dcef8caadcc3ef1c1eb670d1da2553621a5017b/xr/scenecore).

**API Changes**

- Renamed `fixedAspectRatio` to `isFixedAspectRatioEnabled` and made it a boolean property ([I5c4e8](https://android-review.googlesource.com/#/q/I5c4e8c1026afdccc8f6b40eb2f595261febaf71c), [b/440588971](https://issuetracker.google.com/issues/440588971))
- `Scenecore` Fakes are now located in `xr:scenecore:scenecore-testing` module. ([Idd951](https://android-review.googlesource.com/#/q/Idd951597c65a2104ba1e02e1a388abfafec15664))
- Renamed `shouldAutoHideContent` to `isAutoHideContentWhileResizingEnabled` and `shouldAlwaysShowOverlay` to `isAlwaysShowOverlayEnabled` ([I97c36](https://android-review.googlesource.com/#/q/I97c36d70477b1606e5962c077e332d1ca9080396), [b/432335421](https://issuetracker.google.com/issues/432335421))
- Updated `SceneCore` `TextureSampler` constants for readability, for example `TextureSampler.MinFilter.LINEAR` is now `TextureSampler.MIN_FILTER_LINEAR` ([Ib159c](https://android-review.googlesource.com/#/q/Ib159cfad20d3da673016475afa4b9dc4ae3b2905))
- Scene's `setKeyEntity` setter has been merged into the `keyEntity` variable. Setting the `keyEntity` to an unmovable Entity such as `AnchorEntity` will throw an `IllegalArgumentException` instead of returning a boolean false. ([I62080](https://android-review.googlesource.com/#/q/I620806e7d64aad4c03a6727ea3a7d9b171572025), [b/428721695](https://issuetracker.google.com/issues/428721695), [b/422215745](https://issuetracker.google.com/issues/422215745))
- Scene's `SpatialModeChangeListener` variable was replaced with `setSpatialModeChangedListener`. It takes in a `Consumer<SpatialModeChangeEvent>` instead of a `SpatialModeChangedListener`. `setSpatialModeChangedListener` can now optionally take in an Executor. ([I62080](https://android-review.googlesource.com/#/q/I620806e7d64aad4c03a6727ea3a7d9b171572025), [b/428721695](https://issuetracker.google.com/issues/428721695), [b/422215745](https://issuetracker.google.com/issues/422215745))
- Removed the `bundle` parameter from `ActivityPanelEntity.startActivity` ([I64344](https://android-review.googlesource.com/#/q/I64344057bfa3097a232dc3b5d0ae005b436c17bf), [b/430332856](https://issuetracker.google.com/issues/430332856), [b/430333040](https://issuetracker.google.com/issues/430333040))
- Renamed `SpatializerConstants.SOURCE_TYPE_BYPASS` to `SpatializerConstants.SOURCE_TYPE_DEFAULT`. ([Ifc7fe](https://android-review.googlesource.com/#/q/Ifc7fed07b28f5177d711184711f524b42cd4c14e), [b/422215565](https://issuetracker.google.com/issues/422215565))
- Added `SpatialSoundPool.PLAY_FAILED` constant. ([Ifc7fe](https://android-review.googlesource.com/#/q/Ifc7fed07b28f5177d711184711f524b42cd4c14e), [b/422215565](https://issuetracker.google.com/issues/422215565))
- Added default arguments to `SpatialSoundPool.play` methods. ([Ifc7fe](https://android-review.googlesource.com/#/q/Ifc7fed07b28f5177d711184711f524b42cd4c14e), [b/422215565](https://issuetracker.google.com/issues/422215565))
- Removed return value of setters in `SpatialAudioTrackBuilder`. ([Ifc7fe](https://android-review.googlesource.com/#/q/Ifc7fed07b28f5177d711184711f524b42cd4c14e), [b/422215565](https://issuetracker.google.com/issues/422215565))
- SurfaceEntity changes
  - `SurfaceEntity.CanvasShape` renamed `Shape`
  - `SurfaceEntity.CanvasShape.Vr180Hemisphere` renamed `Hemisphere`
  - `SurfaceEntity.CanvasShape.Vr360Sphere` renamed `Sphere`
  - `SurfaceEntity.EdgeFeatheringParams.SmoothFeather` renamed `RectangleFeather`
  - `SurfaceEntity.EdgeFeathingParams.SolidEdge` renamed `NoFeathering`
  - `SurfaceEntity.ContentSecurityLevel` renamed `SurfaceProtection`
  - `SurfaceEntity.ContentSecurityLevel.{values}` added a `SURFACE_PROTECTION_` prefix.
  - `SurfaceEntity.SuperSampling.{$values}` added a `SUPER_SAMPLING_` prefix
  - `SurfaceEntity.StereoMode.{values}` added a `STEREO_MODE_` prefix
  - `SurfaceEntity.ContentColorMetadata.maxCLL` renamed `maxContentLightLevel` ([I7eb5f](https://android-review.googlesource.com/#/q/I7eb5fa6e22e7e8e9514293b66de30d4c6bc545b0), [b/422216050](https://issuetracker.google.com/issues/422216050), [b/427529950](https://issuetracker.google.com/issues/427529950))
- Renamed `launchActivity` to `startActivity` ([I7db90](https://android-review.googlesource.com/#/q/I7db907769a5e26f9cb5346ba63f63afb0a0ea31d), [b/430332856](https://issuetracker.google.com/issues/430332856))
- Removed `Scene.activitySpaceRoot`. Use `Scene.activitySpace` instead. ([I05ee8](https://android-review.googlesource.com/#/q/I05ee8971d2208203b660045aca43453e2bf8249b), [b/378706624](https://issuetracker.google.com/issues/378706624), [b/422215745](https://issuetracker.google.com/issues/422215745))
- `configureBundleForFullSpaceModeLaunch` and `configureBundleForFullSpaceModeLaunchWithEnvironmentInherited` renamed to `createBundleForFullSpaceModeLaunch` and `createBundleForFullSpaceModeLaunchWithEnvironmentInherited` respectively, and moved to LaunchUtils.kt file as top-level methods and take Session as first param ([I64a2c](https://android-review.googlesource.com/#/q/I64a2c9cf37fa14a1c46a99592e00fd9b25c1373b), [b/437186050](https://issuetracker.google.com/issues/437186050))
- `GroupEntity` factory now returns `GroupEntity` type instead of Entity. ([I66042](https://android-review.googlesource.com/#/q/I660420712026424ec806f39477ff0ddec284a6d3))

**Bug Fixes**

- Throw an `IllegalStateException` when an entity instance is used after dispose. ([I90990](https://android-review.googlesource.com/#/q/I90990152de00b78c2d9f36efafe347cac1f1dccc), [b/427314036](https://issuetracker.google.com/issues/427314036), [b/432063442](https://issuetracker.google.com/issues/432063442))

### Version 1.0.0-alpha06

August 13, 2025

`androidx.xr.scenecore:scenecore:1.0.0-alpha06`, `androidx.xr.scenecore:scenecore-guava:1.0.0-alpha06`, and `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eef55ce7cd8e6d0ab2f3574d87e36e97239347d2..a54f47329f5dd47722a43b92814d5c7278a434ce/xr/scenecore).

**API Changes**

- Unrestrict `SceneCore`'s `BaseEntity` and `BaseScenePose` APIs ([88c0ff6](https://android.googlesource.com/platform/frameworks/support/+/88c0ff656e00a7fd47f8b622e4d036eeb3bdc792))

### Version 1.0.0-alpha05

July 30, 2025

`androidx.xr.scenecore:scenecore-guava:1.0.0-alpha05`, `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha05`, and `androidx.xr.scenecore:scenecore:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..e2ada2fb2bdda489dea67a9220554f31e20a5e5f/xr/scenecore).

**New Features**

- Perceived Resolution API added to Panel Entities and `SurfaceEntities`. ([I118f6](https://android-review.googlesource.com/#/q/I118f66e03081de2547292744407b2d6783ebf5a9))
- `PerceivedResolution` Callback methods added to Scene.kt to monitor the perceived resolution of the main panel of the activity in HSM. ([I58084](https://android-review.googlesource.com/#/q/I58084ac28e6de85fa1fe7f44d2742bf6187c55f5))
- `SurfaceEntity` - Support added for Application to request super sampling at creation time. This allows applications to use super sampling filter for anti-aliasing. ([I06913](https://android-review.googlesource.com/#/q/I069135e2d6ec04d2fb20d777d0c919259a0758c7))
- Added `recommendedContentBoxInFullSpace` property to `ActivitySpace`. It returns a recommended box for content to be placed in when in Full Space Mode. ([I4cd6f](https://android-review.googlesource.com/#/q/I4cd6f2d54fdb4fd62866a971f528b878fa0a08b3))
- Provided overloaded constructor for movable modifier which allows anchoring. ([Ic0c70](https://android-review.googlesource.com/#/q/Ic0c70e86c0be734b7f8bdda14f5501a4a57cd5e4))

**API Changes**

Extensive API changes were made to `SceneCore` for this release. Several classes have been renamed and/or moved to different modules, and most getter/setter methods have been replaced with Kotlin properties. While we anticipate future breaking API changes until our first Beta release, they will not be as disruptive or numerous.

- Renamed and/or moved the following classes \& interfaces: `androidx.xr.scenecore.PixelDimensions` to `androidx.xr.runtime.math.IntSize2d`; `androidx.xr.scenecore.Dimensions` to `androidx.xr.runtime.math.FloatSize3d`; `androidx.xr.scenecore.ActivityPose` to `ScenePose`, `androidx.xr.scenecore.ContentlessEntity` to `GroupEntity`, `androidx.xr.scenecore.PlaneType` to `PlaneOrientation`; `androidx.xr.scenecore.PlaneSemantic` to `PlaneSemanticType`. ([Ifd405](https://android-review.googlesource.com/#/q/Ifd40559bd3ffaccfc1782c81af39be1c5e7922a1))([I3b622](https://android-review.googlesource.com/#/q/I3b6220239765cdaa502184d4598c8048fea6570d)) ([If534d](https://android-review.googlesource.com/#/q/If534da0c7d818a518c3559b6037e92fb01f6fac5))
- A number of setters for `Scene`'s properties have been made private; they were not intended to be mutated by `SceneCore` clients: `activitySpace`, `activitySpaceRoot`, `mainPanelEntity`, `perceptionSpace`, `spatialCapabilities`, `spatialEnvironment`, and `spatialUser`. ([I2f506](https://android-review.googlesource.com/#/q/I2f506c72a5c699547b8fa2b1096b5c63ac115d2b))
- In Entity: Changed the following to properties: `get/setParent()`, `setContentDescription`; Deprecated `Entity.is/setHidden()`, use `Entity.is/setEnabled` instead. ([Ibc4c6](https://android-review.googlesource.com/#/q/Ibc4c642ebd8b84e4fbe06f0d4afbbc62aaf77f10))
- Removed the `androidx.xr.scenecore.BasePanelEntity` class, use `PanelEntity` directly instead. Replaced getters and setters for `PanelEntity` with properties. Changed `PanelEntity.size` property from `Float3dSize` to `Float2dSize`. Remmoved the deprecated method `androidx.xr.scenecore.PanelEntity.getPixelDimensions`, use `getSizeInPixels` instead. ([Icc174](https://android-review.googlesource.com/#/q/Icc17414612735c9ca955b2aba63c96ff9ba382fc))
- Replaced `androidx.xr.scenecore.OnSpaceUpdatedListener` with `Runnable`. ([I19308](https://android-review.googlesource.com/#/q/I19308b238f4f4799416e0c155dde5cdabfecb3cf))
- Replaced `SpatialUser.getCameraViews()` with a property. ([Ib0cc5](https://android-review.googlesource.com/#/q/Ib0cc54a3f72b1057702d6c4819f526246d88eae2)) For `ExrImage` and `GltfModel:` Changed `create` methods to be suspend functions; modified create parameters to accept a `Uri` or `Path` instead of a `String`. ([Id8883](https://android-review.googlesource.com/#/q/Id888320395bf66f267293e54b0cc388ed83c1a50)) ([I0d247](https://android-review.googlesource.com/#/q/I0d247e3db918e0a95f067745e76bf755986b91c0)), ([I25706](https://android-review.googlesource.com/#/q/I25706f1b2e278e814c02a35bba606b8790801a08))
- Moved `SpatialEnvironment.requestFullSpaceMode` and `SpatialEnvironment.requestHomeSpaceMode` to Scene, for example use `session.scene.requestFullSpaceMode()` instead of `session.scene.spatialEnvironment.requestFullSpaceMode()`. `addOnPassthroughOpacityChangedListener` and `addOnSpatialEnvironmentChangedListener` now have overrides that accept optional Executors. ([I12fe0](https://android-review.googlesource.com/#/q/I12fe0c5472eb5971be7bf733988abc1013209309)) ([I6b21e](https://android-review.googlesource.com/#/q/I6b21e7098f0d7061c84704ed56977bbfac45ccfc))
- Removed the following deprecated `SpatialEnvironment` methods: `togglePassthrough`, `setPassthrough`, `setPassthroughOpacity`, `getPassthroughMode`, `getPassthroughOpacity`, `setSkybox`, and `setGeometry`. Also removed deprecated class `SpatialEnvironment.PassthroughMode` ([I927bd](https://android-review.googlesource.com/#/q/I927bd71a2926f233b89fceca8881641695015846)) ([I927bd](https://android-review.googlesource.com/#/q/I927bd71a2926f233b89fceca8881641695015846)) ([I927bd](https://android-review.googlesource.com/#/q/I927bd71a2926f233b89fceca8881641695015846))
- Replaced the following `SpatialEnvironment` getters and setters with Kotlin properties: `getCurrentPassthroughOpacity()`, `get/setPassthroughOpacityPreference()`, `get/setSpatialEnvironmentPreference()`, `isSpatialEnvironmentPreferenceActive()` ([I33a7b](https://android-review.googlesource.com/#/q/I33a7bd2ae3a900f14d862f265d298ab794b4afa2)) ([Ie06e2](https://android-review.googlesource.com/#/q/Ie06e2988ca2f2c4404cf99a38e07fe2e74048895)) ([Ie06e2](https://android-review.googlesource.com/#/q/Ie06e2988ca2f2c4404cf99a38e07fe2e74048895))
- `SpatialEnvironmentPreference.preferredPassthroughOpacity` type changed from `Float?` to `Float`. It no longer accepts null values. Instead, `SpatialEnvironment.NO_PASSTHROUGH_OPACITY_PREFERENCE` is used to signal that there's no opacity preference. ([I40107](https://android-review.googlesource.com/#/q/I40107611d1a838254580238feae914a1847afe73))
- Updated the `windowBoundsPx` parameter to `pixelDimensions` and its type from Rect to `IntSize2d` in the create method. ([I1926e](https://android-review.googlesource.com/#/q/I1926ef679cbb7f8e480f92f9ddd9c7d135a06a6b))
- `SpatialEnvironment` constructor is now internal ([I75a51](https://android-review.googlesource.com/#/q/I75a510c2032f7733db31593c580c37cacb13f3ad))
- Replaced class `SpatialPointerIconNone` and `SpatialPointerIconCircle` classes with companion objects `SpatialPointerIcon.NONE` and `SpatialPointerIcon.CIRCLE` ([I416d2](https://android-review.googlesource.com/#/q/I416d2cc4b60558a78774e06221c243e3d77cf70f))
- `SpatialPointerIcon` in `SpatialPointerComponent` is no longer nullable. Use `SpatialPointerIcon.DEFAULT` instead of null to indicate that the system default pointer icon should be used. ([I416d2](https://android-review.googlesource.com/#/q/I416d2cc4b60558a78774e06221c243e3d77cf70f))
- Replaced `androidx.xr.scenecore.AnchorEntity.getState()` with a read-only property. Renamed parameters on the `AnchorEntity.create()` method for clarity. In `AnchorEntity`'s methods for setting and adding listeners, the listener has been moved to the final argument to enabled trailing lambdas. Replaced `androidx.xr.scenecore.OnStateChangedListener` for `AnchorEntity` with `Consumer<AnchorEntity.State>`. ([I472e0](https://android-review.googlesource.com/#/q/I472e007c99b6c2601442eff8c8e2b268551809a4))
- `GltfModelEntity.getAnimationState()` is now a property. ([I10b29](https://android-review.googlesource.com/#/q/I10b2955f5b1d26a11792e097125d2a66b262db62))
- Replaced `ActivitySpace.getBounds()` with a property. Renamed `ActivitySpace.addBoundsChangedListener` to `ActivitySpace.addOnBoundsChangedListener`. Replaced `ActivitySpace.setOnSpaceUpdatedListener` with add/remove methods. ([I4c956](https://android-review.googlesource.com/#/q/I4c956982487c947284de1574e0880b08e9b78917))
- For `AnchorPlacement: planeTypeFilter` was renamed to `anchorablePlaneOrientations`, `planeSemanticFilter` was renamed to `anchorablePlaneSemanticTypes`. Add a `MovableComponent` to an `AnchorEntity` or `ActivitySpace` will return false, `MoveListener` was renamed to `EntityMoveListener shouldDisposeParentAnchor` was renamed to `disposeParentOnReAnchor systemMovable` was removed from the `create` function in favor of `creeateCustomMovable`, `createSystemMovable` and `createAnchorable` ([If11c4](https://android-review.googlesource.com/#/q/If11c49d4cec222d13d29caac0cf0bf25305738b2))
- Removed `SurfaceEntity.featherRadiusX/Y` and adds an `EdgeFeatheringParams` class concept. ([Ic78fc](https://android-review.googlesource.com/#/q/Ic78fcebcf3d8e27ebc3972dda56e6211563371e8))
- `PanelEntity.enablePanelDepthTest()` method replaced with `panelClippingConfig` property. Set `Scene.panelClippingConfig = PanelClippingConfig(isDepthTestEnabled = true)` to enable depth-testing or set it to `PanelClippingConfig(isDepthTestEnabled = false)` to disable it. ([I0cbe0](https://android-review.googlesource.com/#/q/I0cbe0d959f3efedd353f453049e55a3c21ffb0c6))
- `Scene.mainPanelEntity` is now of type `MainPanelEntity` instead of `PanelEntity` ([I7125a](https://android-review.googlesource.com/#/q/I7125a7d8ce44551062adf54a9d770ad894bf9c15))
- Renamed Scene's `setFullSpaceMode` method to `configureBundleForFullSpaceModeLaunch` and `setFullSpaceModeWithEnvironmentInherited` method to `configureBundleForFullSpaceModeLaunchWithEnvironmentInherited`. ([I0cbe0](https://android-review.googlesource.com/#/q/I0cbe0d959f3efedd353f453049e55a3c21ffb0c6)) ([I0cbe0](https://android-review.googlesource.com/#/q/I0cbe0d959f3efedd353f453049e55a3c21ffb0c6))
- Renamed `SpatialVisibility`'s UNKNOWN, OUTSIDE_FOV, PARTIALLY_WITHIN_FOV, and WITHIN_FOV values to SPATIAL_VISIBILITY_UNKNOWN, SPATIAL_VISIBILITY_OUTSIDE_FIELD_OF_VIEW, SPATIAL_VISIBILITY_PARTIALLY_WITHIN_FIELD_OF_VIEW, and SPATIAL_VISIBILITY_WITHIN_FIELD_OF_VIEW, respectively ([Ie7e8c](https://android-review.googlesource.com/#/q/Ie7e8c3ee87d976d51f6091eb981cb97ec771502f))
- `SpatialVisibility` class replaced with public object with const Int values. `setSpatialVisibilityChangedListener` now accepts a `Consumer<Int>` instead of `Consumer<SpatialVisibility>` ([Ie7e8c](https://android-review.googlesource.com/#/q/Ie7e8c3ee87d976d51f6091eb981cb97ec771502f))
- `PointerCaptureComponent` constants renamed and moved to `PointerCaptureComponent.PointerCaptureState` object ([I9c7ac](https://android-review.googlesource.com/#/q/I9c7ac29494cec93bbf9793dba863cd5c900b0611))
- Replaced `PointerCaptureComponents' StateListener` with `Consumer<Int>`. ([I9c7ac](https://android-review.googlesource.com/#/q/I9c7ac29494cec93bbf9793dba863cd5c900b0611))
- Replaced `InputEventListener` with `Consumer<InputEvent>` ([I9c7ac](https://android-review.googlesource.com/#/q/I9c7ac29494cec93bbf9793dba863cd5c900b0611))
- `setPreferredAspectRatio` moved from Scene class to `SpatialWindow` object and takes in Session as first parameter. ([I7b717](https://android-review.googlesource.com/#/q/I7b7176ad279ee1088112bcc07af189bf1ba2c3fe))
- `Entity.setHidden()` replaced by `Entity.setEnabled()` and `Entity.isHidden()` replaced by `Entity.isEnabled()`. `setHidden(false)` is equal to `setEnabled(true)` and `isHidden() == !isEnabled()`. ([Icf0de](https://android-review.googlesource.com/#/q/Icf0dee494643388021214c9567e2a98f04d0017a))
- `Entity.contentDescription` type changed from String to `CharSequence`. ([Ie59be](https://android-review.googlesource.com/#/q/Ie59be94d2f2c1c2f2d7277b22bf2d72c6029580d))
- `Session.create` and `Session.configure` now throw `SecurityException` when sufficient permissions have not been granted instead of returning `SessionCreatePermissionsNotGranted` or `SessionConfigurePermissionsNotGranted`. ([I7c488](https://android-review.googlesource.com/#/q/I7c48826f858c9934949093ed8b52446153967761))
- `ResizableComponent.create` now requires a `Consumer<ResizeEvent> ResizeEventListener` was replaced with `Consumer<ResizeEvent> ResizableComponent.size` was renamed to `ResizableComponent.affordanceSize ResizableComponent.minimumSize` was renamed to `ResizableComponent.minimumEntitySize ResizableComponent.maximumSize` was renamed to `ResizableComponent.maximumEntitySize`, `ResizableComponent.autoHideContent` was renamed to `ResizableComponent.shouldAutoHideContent` `ResizableComponent.forceShowResizeOverlay` was renamed to `ResizableComponent.shouldAlwaysShowOverlay` ([I97a2d](https://android-review.googlesource.com/#/q/I97a2d78f4b386e602120d967609a485ab9fede91))
- Reduced `minSDK` to 24 for `androidx.xr.scenecore` and `androidx.xr.compose`. XR packages still require API 34 at runtime. ([I17224](https://android-review.googlesource.com/#/q/I172248f53672e708d8486452ed5742e116aab538))
- Removed `RequiresApi(34)` restriction on all Jetpack XR packages. This restriction was redundant as Jetpack XR is currently only available on devices with API level 34+. ([Iae0f8](https://android-review.googlesource.com/#/q/Iae0f8f1c0de1d62609ed0dcad6cf2731756054dd))
- The main `SceneCore` artifact (`xr:scenecore:scenecore`) will only contain Kotlin-style async APIs. Java developers can depend on the `xr:scenecore:scenecore-guava` library to access compatible APIs. ([If221b](https://android-review.googlesource.com/#/q/If221be3c3d771aea9b8aa74682df6db753d3c593))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler) ([Ia8420](https://android-review.googlesource.com/#/q/Ia84200c477b50c79761005fffb0d44c001009cca))
- All async methods that return `ListenableFuture` have been replaced with Kotlin suspend functions. Java developers that wish to use `ListenableFuture`-based async methods instead Kotlin suspend functions must now use extension functions in `:xr:scenecore-scenecore-guava`. For example, `GuavaExrImage` contains the Guava-equivalent ExrImage async functions, `GuavaScenePose` contains the Guava-equivalent `ScenePose` async functions, `GuavaGltfModel` contains the `Guava-equivalent GltfModel` async functions, etc. ([If7283](https://android-review.googlesource.com/#/q/If7283b35cdeb52c067a31082302d32dddca2d35b)) ([I0af60](https://android-review.googlesource.com/#/q/I0af609e44a3aaa6122ebf8c8ca2783c121cce094)) ([If7283](https://android-review.googlesource.com/#/q/If7283b35cdeb52c067a31082302d32dddca2d35b)) ([Ia8515](https://android-review.googlesource.com/#/q/Ia851535bdb3259a8866f974c1af3dfbbda1bdfc7)) ([I4efdf](https://android-review.googlesource.com/#/q/I4efdf84b03d46e4be47811764833ea9903e1c8cb)) ([I54bbf](https://android-review.googlesource.com/#/q/I54bbf9c1d6bc5a8154ae418ef2b93c5a415b333e)) ([I3467a](https://android-review.googlesource.com/#/q/I3467ab8105a43de68af4697d86aa1d9c44829d7d)) ([I82a33](https://android-review.googlesource.com/#/q/I82a33360f97954726b29bcc94aff961c7860bfcf))

**Bug Fixes**

- Updated Jetpack XR Scenecore `ProGuard` rule to prevent `AbstractMethodError` for minified clients. ([I91a01](https://android-review.googlesource.com/#/q/I91a01dd6f1545db37c95c59ee8691f51ed665ce0))
- Additional fixes to support Proguard minification for Jetpack XR `SceneCore` ([I4f47e](https://android-review.googlesource.com/#/q/I4f47e46ecb26a1909d2e4622810a5f85b9b06958))
- Fixed a bug where an `InteractableComponent` may cause a crash if the `hitPosition` on the HitInfo of the `InputEvent` may crash if the `hitPosition` returned from the system was null ([I7a695](https://android-review.googlesource.com/#/q/I7a695367377503e87fa072dd3d6d6828bcce2fa0))
- Config \*Mode vals have been renamed to reflect their behavior. ([I6d247](https://android-review.googlesource.com/#/q/I6d24772f4456d4a2409adbaf6162fabb4f5756ef))
- Fixed issues with FOV and `HitTest` in `SceneCore` TestApp. ([I2c51e](https://android-review.googlesource.com/#/q/I2c51ed7b9b46f5759eb23e773d64a04c86f2f6f9))
- Fixed bug in `SpatialCapabilities.hasCapability()` where it would return true if any of the capabilities passed in with a bitwise OR was true instead of only returning true if they were all true. ([I2cd40](https://android-review.googlesource.com/#/q/I2cd40dfc08eb53874fd96fd19cf1bc6e19dbb253))
- `SurfaceEntity.StereoMode.TOP_BOTTOM` updated to have the top map to the left eye and the bottom map to the right eye. ([I4ae68](https://android-review.googlesource.com/#/q/I4ae685be894a6368c20a2bf624113040b8301af1))

### Version 1.0.0-alpha04

May 7, 2025

`androidx.xr.scenecore:scenecore:1.0.0-alpha04` and `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/043342a8810f3356110a0afce48c662e841c428f..b6c541571b9fb5471f965fc52612cb280713e5e4/xr/scenecore).

> [!NOTE]
> **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

**New Features**

- Backhandling will now work on panel entities without embedded activities. For backhandling to work you need to specify `android:enableOnBackInvokedCallback= "true"` in the android manifest.
- `StereoSurfaceEntity` now supports MV-HEVC playback through two new `StereoMode` values: MULTIVIEW_LEFT_PRIMARY and MULTIVIEW_RIGHT_PRIMARY.
- `PanelEntity.setSize` and `PanelEntity.getSize` now return sizes in parent space.
- `Entity.setPose`, `Entity.getPose`, `Entity.setScale`, `Entity.getScale`, `Entity.setAlpha` and `Entity.getAlpha` now take a new param `relativeTo`, which allows get/set values relative to different spaces. The supported values are Parent, Activity and Real World spaces, and the default value for this param is Parent.
- Spatial Visibility Callback extension methods added to `SessionExt.kt` to monitor when the scene content moves inside or outside the user's field of view.
- `setPointSourceParams` has been added to `SpatialAudioTrack`, allowing the params to be updated after the track has been built.
- Added a new class, Scene, with references to `Scenecore` APIs. Scene will be accessible as an extension property of Session. Functions inside of `SessionExt` have been moved to Scene so imports will be need to be adjusted; for example, `SessionExt.getScene(session)`.`addSpatialCapababilitiesChangedListener` versus `SessionExt.addSpatialCapabilitiesChangedListener`.
- `ActivityPose.hitTestAsync` was added, enabling a `hitTest` against virtual content.
- Added new Component type `SpatialPointerComponent`, allowing clients to specify the icon rendered for the pointer, or to disable the icon. This Component can currently be attached to `PanelEntity` instances only.
- Introducing new `PanelEntity` factory, which takes panel dimensions in either meters or pixels. Older `PanelEntity` factory taking two Dimension type params for panel removed.

**API Changes**

- Removed `RequiresApi(34)` restriction on all Jetpack XR packages. This restriction was redundant as Jetpack XR is currently only available on devices with API level 34+. ([Iae0f8](https://android-review.googlesource.com/#/q/Iae0f8f1c0de1d62609ed0dcad6cf2731756054dd))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `PermissionHelper` class has been removed.
- `PanelEntity.getPixelDensity` is deprecated.
- `PanelEntity.setPixelDimensions` and `PanelEntity.getPixelDimension` are removed, replaced by `setSizeInPixels` and `getSizeInPixels`.
- `Entity.getActivitySpaceAlpha` removed. Can be replaced with `Entity.getAlpha(Space.Activity)`.
- `Entity.getWorldSpaceScale` removed. Can be replaced with `Entity.getScale(Space.REAL\_WORLD)`.
- The Session class in `SceneCore` has been deleted in favor of the Session in XR Runtime.
- `StereoSurfaceEntity` has been renamed to `SurfaceEntity`.
- `Entity.setSize` and `Entity.getSize` are removed, and the same methods were added to `PanelEntity`.
- `PointSourceAttributes` has been renamed to `PointSourceParams`.
- `SpatializerConstants.SOURCE\_TYPE\_BYPASS` has been renamed to `SpatializerConstants.SOURCE\_TYPE\_DEFAULT`.
- `PointSourceParams` entity has been modified from public to internal access.
- `AnchorEntity.create` now requires `PlaneTrackingMode` to be configured in `Session.configure()`.
- `SpatialUser` APIs now require `HeadTrackingMode` to be configured in `Session.configure()`.
- When `ResizableComponent` is not attached, it will give INFO-level log instead of ERROR-level log.
- Fov class is now a regular Kotlin class.
- Split `Entity.kt` to place each concrete entity type into its own file.
- When creating a new `PanelEntity`, most Views will be reparented to a `FrameLayout`. This facilitates the use of `LayoutInspector` with Spatial Panels.
- The currently used `XrExtensions` instance is now registered with the platform, in a best effort way, to help with app debugging.

**Bug Fixes**

- A fix was added to prevent a crash that could occur when a `PanelEntity` with `MovableComponent` and `AnchorPlacement` was moved
- Fixed an issue where `ResizableComponent` was providing stale sizes in `onResizeStart` callback.
- Fixed crash when `JxrPlatformAdapterAxr`'s `dispose()` was called multiple times.

### Version 1.0.0-alpha03

February 26, 2025

`androidx.xr.scenecore:scenecore:1.0.0-alpha03` and `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a96c4899cab90642c7b1d722dc1f3b45f56e7b82..043342a8810f3356110a0afce48c662e841c428f/xr/scenecore).

**New Features**

- Proguard minification is now supported for Jetpack XR code

**Bug Fixes**

- Additional fixes to support Proguard minification for Jetpack XR SceneCore ([I4f47e](https://android-review.googlesource.com/#/q/I4f47e46ecb26a1909d2e4622810a5f85b9b06958))
- Updated Jetpack XR Scenecore `ProGuard` rule to prevent `AbstractMethodError` for minified clients. ([I91a01](https://android-review.googlesource.com/#/q/I91a01dd6f1545db37c95c59ee8691f51ed665ce0))

### Version 1.0.0-alpha02

February 12, 2025

`androidx.xr.scenecore:scenecore:1.0.0-alpha02` and `androidx.xr.scenecore:scenecore-testing:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2e2729abc59df52d40af80a8bbfe010c02455c6..a96c4899cab90642c7b1d722dc1f3b45f56e7b82/xr/scenecore).

**Upcoming breaking change affecting apps built before 1.0.0-alpha02**

- Factory methods have been moved from the `Session` class to a companion method on each respective type:
  - `Session.createActivityPanelEntity(Dimensions, String, Activity, Pose)` has been deleted and replaced with `ActivityPanelEntity.create(Session, Dimensions, String, Pose)`
  - `Session.createAnchorEntity(Anchor)` has been deleted and replaced with `AnchorEntity.create(Session, Anchor)`
  - `Session.createAnchorEntity(Dimensions, Int, Int, Duration)` has been deleted and replaced with `AnchorEntity.create(Session, Dimensions, Int, Int, Duration)`
  - `Session.createEntity(String, Pose)` has been deleted and replaced with `ContentlessEntity.create(Session, String, Pose)`
  - `Session.createExrImageResource(String)` has been deleted and replaced with `ExrImage.create(Session, String)`
  - `Session.createGltfEntity(GltfModel, Pose)` has been deleted and replaced with `GltfModelEntity.create(Session, GltfModel, Pose)`
  - `Session.createGltfModelResource(String)` has been deleted and replaced with `GltfModel.create(Session, String)`
  - `Session.createInteractableComponent(Executor, InputEventListener)` has been deleted and replaced with `InteractableComponent.create(Session, Executor, InputEventListener)`
  - `Session.createMovableComponent(Boolean, Boolean, Set<AnchorPlacement>, Boolean)` has been deleted and replaced with `MovableComponent.create(Session, Boolean, Boolean, Set<AnchorPlacement>, Boolean)`
  - `Session.createPanelEntity(View, Dimensions, Dimensions, String, Pose)` has been deleted and replaced with `PanelEntity.create(Session, View, Dimensions, Dimensions, String, Pose)`
  - `Session.createResizableComponent(Dimensions, Dimensions)` has been deleted and replaced with `ResizableComponent.create(Session, Dimensions, Dimensions)`
  - `Session.createStereoSurfaceEntity(Int, Dimensions, Pose)` has been deleted and replaced with `StereoSurface.create(Session, Int, Dimensions, Pose)`
- The following deprecated methods were removed:
  - `Session.canEmbedActivityPanel(Activity)` has been deleted. Use `getSpatialCapabilities.hasCapabilility(SPATIAL_CAPABILITY_EMBED_ACTIVITY)` instead.
  - `Session.hasSpatialCapability(Int)` has been deleted. It has been replaced in favor of using `getSpatialCapabilities().hasCapability()` as a more compartmentalized way to check for the presence of spatial capabilities since `getSpatialCapabilities()` returns a `SpatialCapabilities` object.
  - `Session.requestFullSpaceMode()` has been deleted and replaced with `SpatialEnvironment.requestFullSpaceMode()`
  - `Session.requestHomeSpaceMode()` has been deleted and replaced with `SpatialEnvironment.requestHomeSpaceMode()`
- `Session.setFullSpaceMode(Bundle)` and `Session.setFullSpaceModeWithEnvironmentInherited(Bundle)` have been moved to extension functions. Developer files will need to add the new imports for access:
  - `import androidx.xr.scenecore.setFullSpaceMode`
  - `import androidx.xr.scenecore.setFullSpaceModeWithEnvironmentInherited`
- `Session.setPreferredAspectRatio(Activity, Float)` has been moved to an extension function. Developer files will need to add the new import for access:
  - `import androidx.xr.scenecore.setPreferredAspectRatio`
- `Session.getEntitiesOfType(Class<out T>)` and `Session.getEntityForRtEntity(RtEntity)` have been moved to extension functions. Developer files will need to add the new imports for access:
  - `import androidx.xr.scenecore.getEntitiesOfType`
  - `import androidx.xr.scenecore.getEntityForRtEntity`
- `Session.unpersistAnchor(Anchor)` has been deleted
- `Session.createPersistedAnchorEntity(UUID)` has been deleted

**Known issues**

- `PanelEntity.setCornerRadius()` and `ActivityPanelEntity.setCornerRadius()` may not take effect until the panel is next moved, this can be mitigated by moving the panel to its current position
- When `BoundsChanged` is called on the `ActivitySpace`, some `ActivityPose`s may not have been correctly updated. It will be updated on the following `OnSpaceUpdated` call on the `ActivitySpace`

**Breaking \& behavioral changes**

- `PanelEntity` and `ActivityPanelEntity` will have a default corner radius of 32dp or smaller if the panel has a width or height smaller than 32dp

**New APIs and capabilities**

- Introduces `StereoSurface.CanvasShape`, which allows for the creation of `Spherical` and `Hemispherical` canvases for rendering immersive media.
- `StereoSurfaceEntity.create()` now accepts a `CanvasShape` parameter. (This parameter is currently ignored, but will be used in a future release)
- `StereoSurfaceEntity.create()` no longer takes a `Dimensions` parameter. Applications should control the size of the canvas through setting the `CanvasShape`
- `StereoSurfaceEntity` has a `CanvasShape` member which can be set dynamically.
- `StereoSurfaceEntity.dimensions` is now a read-only property; applications should set the `CanvasShape` to change dimensions.
- `StereoSurfaceEntity` now allows the `StereoMode` to be re-set after construction.

**Other changes**

- Reduced compile-time minSDK to 24. All Jetpack XR APIs continue to require API 34 at runtime.
- `SceneCore`'s Session factory (`Session.create`) no longer launches an intent to acquire the `SCENE_UNDERSTANDING` permission. Instead, the client application must explicitly request the permissions from the user, before attempting to create the anchors. Anchor creation will fail if the permission is not granted by the user.

**Bug fixes**

- `getActivitySpacePose()` has been fixed to account for the `ActivitySpace` scale by returning translation values in scaled meters rather than always returning non-scaled meters. `transformPoseTo` now also uses the right units to compute coordinate changes when the `ActivitySpace` is involved in the source or destination.
- The skybox will now be set to an all-black skybox whenever a null skybox preference is passed using `setSpatialEnvironmentPreference(new SpatialEnvironmentPreference(null, geom))`. To revert to the system default skybox and geometry, use `setSpatialEnvironmentPreference(null).`

### Version 1.0.0-alpha01

December 12, 2024

`androidx.xr.scenecore:scenecore-* 1.0.0-alpha01` is released.

**Features of Initial Release**
Initial developer release of Jetpack SceneCore, a 3D scene graph library for creating and manipulating immersive scenes and environments. This library allows you to place and arrange 3D models and content panels relative to each other and your virtual or real-world environments.

- [SpatialEnvironment](https://developer.android.com/design/ui/xr/guides/environments): Create fully immersive experiences with a skybox image and/or 3D model geometry as the backdrop for your XR scene of your environment. Or enable passthrough, so your virtual scene can integrate with the user's real-world environment.
- [PanelEntity](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity): Add 2D content to your 3D scenes by embedding standard Android layouts and Activities into spatialized panels that can float or be anchored to real-world surfaces.
- [GltfModelEntity](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity): Place, animate, and interact with 3D models in your scene. SceneCore supports the glTF file format for ease of integration with existing models.
- [SpatialAudio](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio): Add ambient and point audio sources into your 3D scene for fully immersive, spatialized sound.
- [StereoSurfaceEntity](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/StereoSurfaceEntity): SceneCore supports left/right eye routing of content rendered onto an Android Surface. This can be used to render stereoscopic content in a side-by-side or top-bottom format, such as stereo photos, 3D video, or other dynamically rendered UIs. Applications should use MediaPlayer or ExoPlayer for video decoding.
- Component System: SceneCore offers a robust and flexible component system for adding capabilities to your XR content, including affordances for users to move, resize, and interact with models and panels.
- [Anchor](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor): With passthrough enabled, you can attach panels and models to actual surfaces, giving users seamless integration of virtual content in their real-world environment.
- User Pose: Access the user's location in the virtual scene, to orient your content around the user's position.
- [SpatialCapabilities](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities): Build fully adaptive apps that take advantage of spatialized capabilities when available, such as 3D positioning of UI content. Not only that, but your app can monitor for changes to capabilities while the app is executing, to modify the experience based on how the user is using their Android XR device.

**Known Issues**

- Currently a minSDK of 30 is required to use Jetpack SceneCore. As a workaround add the following manifest entry `<uses-sdk tools:overrideLibrary="androidx.xr.scenecore, androidx.xr.compose"/>` to be able to build and run with a minSDK of 23.
- Session can become invalid in various situations that automatically recreate the Activity, including resizing a main panel, connecting peripherals, and changing between light and dark mode. If you encounter session invalidation issues, workarounds include making you main panel non-resizable, using a dynamic panel entity, [disabling activity recreation](https://developer.android.com/guide/topics/resources/runtime-changes#restrict-activity) for specific config changes or disabling light/dark mode theme changes.
- Movable and Resizable components are not supported on GltfEntity.
- Entity.getSize() is not supported on GltfEntity.
- Jetpack XR apps required to request `android.permission.SCENE_UNDERSTANDING` permission in AndroidManifest.
- Creating a session is only supported on an Android XR device. At this time, if you create a Session and try to use it on a non Android XR device, you'll get a RuntimeException.
- Setting the skybox to null via \`SpatialEnvironment.setSpatialEnvironmentPreference() does not result in a solid black skybox as documented. It may result in the system default skybox or no change to the current skybox.
- SceneCore clients should add `implementation("com.google.guava:listenablefuture-1.0")` to their Gradle configuration for their app's dependencies. In a future release, scenecore will include this library as an `api` dependency so clients will not need to explicitly declare it.
- SceneCore erroneously includes `com.google.guava:guava-31.1-android` and `com.google.protobuf:protobuf-javalite` as transitive dependencies. If this results in duplicate class errors in your build, these two dependencies can be safely excluded.
- If your app uses SceneCore and enables ProGuard, it will crash when you create a Session. As a workaround, disable ProGuard. See [this
  guide](https://developer.android.com/build/shrink-code) for more information on how to enable ProGuard.