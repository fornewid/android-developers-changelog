---
title: https://developer.android.com/jetpack/androidx/releases/wear-tiles
url: https://developer.android.com/jetpack/androidx/releases/wear-tiles
source: md.txt
---

# Wear Tiles

[User Guide](https://developer.android.com/training/wearables) [Code Sample](https://github.com/android/wear-os-samples) API Reference  
[androidx.wear.tiles](https://developer.android.com/reference/kotlin/androidx/wear/tiles/package-summary)  
Create applications for Wear OS by Google smartwatches.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.5.0) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.6.0-rc01) | - | - |

## Declaring dependencies

To add a dependency on Wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement support for wear tiles
    implementation "androidx.wear.tiles:tiles:1.5.0"

    // Use to utilize standard components and layouts in your tiles
    implementation "androidx.wear.protolayout:protolayout:1.3.0"

    // Use to utilize components and layouts with Material Design in your tiles
    implementation "androidx.wear.protolayout:protolayout-material:1.3.0"

    // Use to include dynamic expressions in your tiles
    implementation "androidx.wear.protolayout:protolayout-expression:1.3.0"

    // Use to preview wear tiles in your own app
    debugImplementation "androidx.wear.tiles:tiles-renderer:1.5.0"

    // Use to fetch tiles from a tile provider in your tests
    testImplementation "androidx.wear.tiles:tiles-testing:1.5.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement support for wear tiles
    implementation("androidx.wear.tiles:tiles:1.5.0")

    // Use to utilize standard components and layouts in your tiles
    implementation("androidx.wear.protolayout:protolayout:1.3.0")

    // Use to utilize components and layouts with Material Design in your tiles
    implementation("androidx.wear.protolayout:protolayout-material:1.3.0")

    // Use to include dynamic expressions in your tiles
    implementation("androidx.wear.protolayout:protolayout-expression:1.3.0")

    // Use to preview wear tiles in your own app
    debugImplementation("androidx.wear.tiles:tiles-renderer:1.5.0")

    // Use to fetch tiles from a tile provider in your tests
    testImplementation("androidx.wear.tiles:tiles-testing:1.5.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1112273+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1112273&template=1623657)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.6

### Version 1.6.0-rc01

February 25, 2026

`androidx.wear.tiles:tiles-*:1.6.0-rc01`is released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..ab5b6a7b57eb87f47a018419129d770797386e00/wear/tiles).

**Bug Fixes**

- Clean up saved resources on Tile remove event.

### Version 1.6.0-beta01

February 11, 2026

`androidx.wear.tiles:tiles-*:1.6.0-beta01` is released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/wear/tiles).

**New Features**

The 1.6.0-beta01 release of Wear Tiles indicates that this release of the library is feature-complete and the API is locked (except where marked as experimental). Wear Tiles 1.6 includes the following new functionalities and APIs:

- **Inlined Resource Handling and performance improvements:** Tiles now support automatic resource collection through `ProtoLayoutScope`.
  - This significantly improves Tiles loading time by removing the need for two binder calls as only the `onTileResourcesRequest` method can be implemented.
  - When using image resources directly in the layout, there is no longer a need to manually override `onTileResourcesRequest` or specify resources in `TilePreviewData`.
- **Material3TileService:** Introduced a new, Kotlin-friendly service for creating tiles. It simplifies development by providing a single `suspend` function to return both tile layout and resources. It automatically manages the `MaterialScope` and `ProtoLayoutScope` for better resource handling and performance improvements on faster Tiles loading.

  - Simplified code snippet:

      class MyTileService : Material3TileService() {
          override suspend fun **MaterialScope.tileResponse**(
              requestParams: RequestBuilders.TileRequest
          ): TileBuilders.Tile = tile(
      timeline = timeline(timelineEntry(
      primaryLayout(
          // layout setup here
      iconContent = { **icon**(
      **imageResource**(
      **androidImageResource**(R.drawable.myIcon)))})
      //...
      )))
      }

- **Tile Previews Update:** Tooling for Tile Previews has been updated to support the new `ProtoLayoutScope` automatic resource handling, ensuring previews reflect inlined resources correctly without extra configuration.

- **Many Kotlin DSL Improvements:** Added specialized Kotlin helpers for `Tile` and all other APIs needed to build a tile (such as `Timeline`) to improve the developer experience for Kotlin users.

- **Dynamic Service Switching:** Introduced `METADATA_GROUP_KEY`, allowing developers to group multiple `TileService` instances in the manifest. This enables dynamic switching between different services that represent the same tile on new OS versions.

- **Tile ID in Updates:** Developers can now specify a particular `tileId` in update requests, allowing for more granular control over which tile instances are refreshed.

**API Changes**

- **Increased Compile SDK:** To support the new `Material3TileService` and advanced resource handling, the `compileSdk` version requirement has been increased to **35**.
- **Minimum SDK Update:** The default `minSdk` for the library has been moved from API 21 to **API 23**.
- **Optional Resource Overrides:** Overriding `onTileResourcesRequest` is now optional when using the new `ProtoLayoutScope` APIs.
- **Schema Metadata:** Added metadata keys for major/minor Tiles Renderer schema versions as XML tags for better platform compatibility tracking.

**Bug Fixes**

- **ANR Prevention:** Moved the unbinding logic during Tile update requests to a background thread to prevent "Application Not Responding" (ANR) errors.
- **Version Awareness:** The internal `ProtoLayoutScope` includes the `ProtoLayout Renderer`'s `VersionInfo`, allowing for better backward compatibility checks.

### Version 1.6.0-alpha05

January 28, 2026

`androidx.wear.tiles:tiles-*:1.6.0-alpha05` is released. Version 1.6.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/wear/tiles).

**API Changes**

- We have added metadata keys for the major/minor Tiles schema version as an XML tag. ([I2cf66](https://android-review.googlesource.com/#/q/I2cf66dea93dbc5015f911e882fd554ffc7e13959))

**Bug Fixes**

- We have fixed the issue with better resource handling by removing stateful `ProtoLayoutScope` from `TileService` and fixed the issue about keys for holding the resources data. ([I5dc0a](https://android-review.googlesource.com/#/q/I5dc0abfbb5aa41721dd75f14765ccde449229611), [b/474614772](https://issuetracker.google.com/issues/474614772))
- Code for unbinding service when update is requested is run on the main thread for testing environments. ([8fd7348](https://android.googlesource.com/platform/frameworks/support/+/8fd73481386146814ffa434121bf60df419ba86e))

### Version 1.6.0-alpha04

January 14, 2026

`androidx.wear.tiles:tiles-*:1.6.0-alpha04` is released. Version 1.6.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/wear/tiles).

**API Changes**

- A new service for creating tiles called `Material3TileService` has been added to the Tiles library.
- This provides better experience in creating `TileService`, as it automatically creates `MaterialScope` needed for Material3 components and layout, which includes `ProtoLayoutScope` for **better resources handling** and **performance improvements**.
- It is more Kotlin friendly, with 1 suspend function to provide both tile layout and resources inlined within the layout components.
- In order to support new service for Tiles with better resources handling, the compile SDK version is increased to 35. ([I1ff29](https://android-review.googlesource.com/#/q/I1ff2955c528db8e5133393f52b997e9353272a0f), [b/470048768](https://issuetracker.google.com/issues/470048768))

### Version 1.6.0-alpha03

December 17, 2025

`androidx.wear.tiles:tiles-*:1.6.0-alpha03` is released. Version 1.6.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..ec985eed3cba8444e5aaa52a748333397a1298f3/wear/tiles).

**API Changes**

- We introduced `METADATA_GROUP_KEY` to allow specifying an optional group name in the service's manifest to which the corresponding `TileService` belongs. This can be used to dynamically switch between different services that correspond to the same tile. ([Ic9e71](https://android-review.googlesource.com/#/q/Ic9e71b555948035e77cb96ae87d3be0359cda0d5), [b/451988130](https://issuetracker.google.com/issues/451988130))

**Bug Fixes**

- Unbinding from service when requesting an update for the Tile is now moved to the background thread to avoid potential ANRs. ([Ifc9f9](https://android-review.googlesource.com/#/q/Ifc9f9b12c418122b594af8157117f4aa5552c1c2), [b/460017465](https://issuetracker.google.com/issues/460017465))

### Version 1.6.0-alpha02

October 22, 2025

`androidx.wear.tiles:tiles-*:1.6.0-alpha02` is released. Version 1.6.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/wear/tiles).

**New Features**

- Tile Previews is now updated to support automatic resource handling via `ProtoLayoutScope`. If using image resources directly in the layout via `materialScopeWithScope` or `ProtoLayoutScope` directly, there is no longer need to specify `onTileResourcesRequest` and resources specifically in the `TilePreviewData`, they will be collected automatically. ([I58516](https://android-review.googlesource.com/#/q/I5851622ac108dbe37b6be4e03d93f0529a9f8e05))

**Bug Fixes**

- `ProtoLayoutScope` created internally by the `TileService` now includes the ProtoLayout Renderer's `VersionInfo`. ([I6eee2](https://android-review.googlesource.com/#/q/I6eee26a6f710e00ee264e6ab4842766ff87c17fe), [b/450259727](https://issuetracker.google.com/issues/450259727))

### Version 1.6.0-alpha01

September 24, 2025

`androidx.wear.tiles:tiles-*:1.6.0-alpha01` is released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/90062705131fa122cdd8d9bed30380b183dc48bd..0c132271cd448b355c7c853ce868820bbb8acbbd/wear/tiles).

**New Features**

- Add provider APIs for accepting `PendingIntent` as click action ([I01978](https://android-review.googlesource.com/#/q/I019786be77ba4a959d43da286dc05e52531238e0), [b/433802488](https://issuetracker.google.com/issues/433802488))
- Allow tile id to be specified in update request. ([Ia05c3](https://android-review.googlesource.com/#/q/Ia05c348c81d798e4fcb78d891deb28436aec941e), [b/421346031](https://issuetracker.google.com/issues/421346031))
- Add method in `TileRequest` to get the `ProtoLayoutScope` object for the corresponding tile instance. ([I5b8de](https://android-review.googlesource.com/#/q/I5b8de14652a927fd5883051eae3cb5bd224845fd), [b/428692428](https://issuetracker.google.com/issues/428692428))

**API Changes**

- Allow not overridding `onTileResourcesRequest` when `ProtoLayoutScope` APIs are used. ([I1773d](https://android-review.googlesource.com/#/q/I1773d50b31dca50cf1a837df25863f39f2a377b8))

**Bug Fixes**

- Add implementation for supporting `PendingIntent` in `ProtoTiles`. ([I38167](https://android-review.googlesource.com/#/q/I38167189ae91141338112412e5f7e90edb7f7e46), [b/430610429](https://issuetracker.google.com/issues/430610429))
- Save resources used from `ProtoLayoutScope` to be correctly sent in `onTileResourcesRequest` for older renderers that don't bundle it within Tile response. ([I063a8](https://android-review.googlesource.com/#/q/I063a804ab158869a03d5596ab7da5fc0b32da920), [b/428692502](https://issuetracker.google.com/issues/428692502))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

## Version 1.5

### Version 1.5.0

June 4, 2025

`androidx.wear.tiles:tiles-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7938d4e7647114b0f950c73aa11b9ebde3e446b..90062705131fa122cdd8d9bed30380b183dc48bd/wear/tiles).

**Important changes since 1.4.0**

- Added new API `TileService.onRecentInteractionEvents()` for processing interaction tile events (Enter / Leave) in batches.
  - The existing APIs in `TileService` for `onEnterEvent` and `onLeaveEvent` are deprecated and won't work from SDK 36+ for Apps targeting API 36 or more
- Critical bug fix for any clients targeting SDK higher than 34 and requesting a tile update on API 34 that would cause a `SecurityException`.
- Starting from Wear 6 (SDK level 36+), all Tiles will be displayed in a system font that is defined by each device.

### Version 1.5.0-rc01

May 20, 2025

`androidx.wear.tiles:tiles-*:1.5.0-rc01`is released with no changes from the previous release. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..c7938d4e7647114b0f950c73aa11b9ebde3e446b/wear/tiles).

### Version 1.5.0-beta02

May 7, 2025

`androidx.wear.tiles:tiles-*:1.5.0-beta02` is released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..b6c541571b9fb5471f965fc52612cb280713e5e4/wear/tiles).

### Version 1.5.0-beta01

April 9, 2025

`androidx.wear.tiles:tiles-*:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..4c37298a97c16270c139eb812ddadaba03e23a52/wear/tiles).

**New Features**

The 1.5.0-beta01 release of Wear Tiles indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear Tiles 1.5 includes the following new functionalities and APIs:

- Added new API `TileService.onRecentInteractionEvents()` for processing interaction tile events (Enter / Leave) in batches.
  - The existing APIs in `TileService` for `onEnterEvent` and `onLeaveEvent` are deprecated and won't work from SDK 36+ for Apps targeting API 36 or more
- Critical bug fix for any clients targeting SDK higher than 34 and requesting a tile update on API 34 that would cause a `SecurityException`.
- Starting from Wear 6 (SDK level 36+), all Tiles will be displayed in a system font that is defined by each device.

### Version 1.5.0-alpha10

March 12, 2025

`androidx.wear.tiles:tiles-*:1.5.0-alpha10` is released. Version 1.5.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/wear/tiles).

### Version 1.5.0-alpha09

February 26, 2025

`androidx.wear.tiles:tiles-*:1.5.0-alpha09` is released. Version 1.5.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..fd7408b73d9aac0f18431c22580d9ab612278b1e/wear/tiles).

### Version 1.5.0-alpha08

February 12, 2025

`androidx.wear.tiles:tiles-*:1.5.0-alpha08` is released. Version 1.5.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/wear/tiles).

**API Changes**

- `TileService.onRecentInteractionEvents()` to return `ListenableFuture<Void>` to allow for long running tasks. ([Iaa6c5](https://android-review.googlesource.com/#/q/Iaa6c52e8506ea0454e91bceea8562300eac915ff))

### Version 1.5.0-alpha07

January 29, 2025

`androidx.wear.tiles:tiles-*:1.5.0-alpha07` is released. Version 1.5.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..4c47131cd5b50c3091fc0874eb606aaac5b168fa/wear/tiles).

### Version 1.5.0-alpha06

January 15, 2025

`androidx.wear.tiles:tiles-*:1.5.0-alpha06` is released. Version 1.5.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/wear/tiles).

**API Changes**

- Renamed `processRecentInteractionEvents` to `onRecentInteractionEvents` method. ([Iec3d5](https://android-review.googlesource.com/#/q/Iec3d5949726fa70c2ab9899105fd944bc325401d))

### Version 1.5.0-alpha05

December 11, 2024

`androidx.wear.tiles:tiles-*:1.5.0-alpha05` is released. Version 1.5.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/wear/tiles).

**New Features**

- Add api for `TileService` to process interaction events in batches. ([I04d1b](https://android-review.googlesource.com/#/q/I04d1bcf5dcf17d71cfd0dcf4e8ec8fff7f969e59))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I390e9](https://android-review.googlesource.com/#/q/I390e9fc6d6e16227f3c7f1d114aa15c4c4626b65), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Fixed the bug where requesting tile updates on API 34 when the app `targetSdk` is higher than 34 would cause a `SecurityException` ([If62a1](https://android-review.googlesource.com/#/q/If62a1453a44f7c3e2cf73c8d1715c8e993d32b06))
- Fixed a dependency to `WearSdk` in Robolectric tests. ([I37796](https://android-review.googlesource.com/#/q/I377965cc4bc3493b27536b6bc6d8eeeeda0feee6))

### Version 1.5.0-alpha04

November 13, 2024

`androidx.wear.tiles:tiles-*:1.5.0-alpha04` is released. Version 1.5.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/wear/tiles).

### Version 1.5.0-alpha03

October 30, 2024

`androidx.wear.tiles:tiles-*:1.5.0-alpha03` is released. Version 1.5.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/wear/tiles).

### Version 1.5.0-alpha02

October 16, 2024

`androidx.wear.tiles:tiles-*:1.5.0-alpha02` is released. Version 1.5.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/wear/tiles).

**Security Fixes**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on version 1.5.0-alpha01 of `androidx.wear.tiles:tiles-proto` to 1.5.0-alpha02 to address the vulnerability risk.

### Version 1.5.0-alpha01

October 2, 2024

`androidx.wear.tiles:tiles-*:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6cfd01b64fd559c7ae948030d262d8bb49e8d19..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/wear/tiles).

## Version 1.4

### Version 1.4.1

October 16, 2024

`androidx.wear.tiles:tiles-*:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6cfd01b64fd559c7ae948030d262d8bb49e8d19..c082c8e53e6ef0e5f04f181b92dc4b9bc99aae3c/wear/tiles).

**Security Fixes**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on version 1.4.0 of `androidx.wear.tiles:tiles-proto` to 1.4.1 to address the vulnerability risk.

### Version 1.4.0

August 7, 2024

`androidx.wear.tiles:tiles-*:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a90014340290143c500c38a4029aea80a9a45c05..d6cfd01b64fd559c7ae948030d262d8bb49e8d19/wear/tiles).

**Important changes since 1.3.0**

- Tooling support for specifying custom platform data for Tiles previews in Android Studio.

### Version 1.4.0-rc01

July 24, 2024

`androidx.wear.tiles:tiles-*:1.4.0-rc01` is released with no changes from the previous release. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..a90014340290143c500c38a4029aea80a9a45c05/wear/tiles).

### Version 1.4.0-beta01

July 10, 2024

`androidx.wear.tiles:tiles-*:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..56579bc30499ce39f0d7a6713a065b00c6194206/wear/tiles).

**New Features**

The 1.4.0-beta01 release of Wear Tiles indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear Tiles 1.4 includes the following new functionalities and APIs:

- Tooling support for specifying custom platform data for Tiles previews in Android Studio.

### Version 1.4.0-alpha05

June 26, 2024

`androidx.wear.tiles:tiles-*:1.4.0-alpha05` is released. Version 1.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..948119be341fa4affc055418e695d8c4c7e5e2e4/wear/tiles).

### Version 1.4.0-alpha04

May 29, 2024

`androidx.wear.tiles:tiles-*:1.4.0-alpha04` is released. Version 1.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/wear/tiles).

### Version 1.4.0-alpha03

May 14, 2024

`androidx.wear.tiles:tiles-*:1.4.0-alpha03` is released. Version 1.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/wear/tiles).

**Bug Fixes**

- `TileService#getActiveTilesAsync` now uses `WearSdk` API (when available) to provide a more accurate result. ([I57bd8](https://android-review.googlesource.com/#/q/I57bd82ee65bfc83ab033fb98aeabd734c1e2c9ff))

### Version 1.4.0-alpha02

May 1, 2024

`androidx.wear.tiles:tiles-*:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..fbd1ac175922f44c69a13545d194066ee428b342/wear/tiles).

**API Changes**

- Move `tileId` to Builder constructor param as a mandatory field and document default timestamp value in the getter. ([I98c2b](https://android-review.googlesource.com/#/q/I98c2b4643f384ea0a5f6e0528d742bdadc5f7349))
- Add `TileInteractionEvent`, `TileEnter`, and `TileLeave` proto messages and Java Wrappers needed for batching tile enter/leave events. ([I112b0](https://android-review.googlesource.com/#/q/I112b03ed1efa2d3042e2796943834068be7358de))
- Refactor `TileRenderer` to use a Builder instead of a `TileRenderer.Config` object. ([Ib66f9](https://android-review.googlesource.com/#/q/Ib66f91213411ff5fd73be2f3ab8b4bc37aa37da4))
- Add a `platformDataProviders` attribute to `TileRenderer.Config`. ([I6030d](https://android-review.googlesource.com/#/q/I6030dd90442d574adfff0e366bd6b698685aec85))
- Add a new constructor to `TileRenderer` that supports a new `TileRenderer.Config` class. Other constructors are deprecated. ([Iae7ff](https://android-review.googlesource.com/#/q/Iae7ff371c15610156f4757e76db818274cfed335))
- Add a `platformDataValues` field to `TilePreviewData` to allow overriding platform data values. ([If437a](https://android-review.googlesource.com/#/q/If437a11bbd2e92407aea6315d0fb1204c199faa1))

**Bug Fixes**

- Document that the default value for `TileRenderer.Config.Builder#setTilesTheme` is zero. ([Iced18](https://android-review.googlesource.com/#/q/Iced18d8f3dee7b441ba3f089c36bd8a60aacb770))

### Version 1.4.0-alpha01

March 6, 2024

`androidx.wear.tiles:tiles-*:1.4.0-alpha01` is released. Version 1.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8a15acd27e433b62c26328806e1b2983aa146db1..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/wear/tiles).

## Version 1.3

### Version 1.3.0

February 7, 2024

`androidx.wear.tiles:tiles-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38756a2fd525d921dd921f38b03e0d9a23150db7..8a15acd27e433b62c26328806e1b2983aa146db1/wear/tiles)

**Important changes since 1.2.0**

- Updated tooling for tile preview support.
- Support for querying active tiles belonging to the app.

**Additional changes**

- For a more complete set of the changes introduced in version 1.3.0, see the [beta01 release notes](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.3.0-beta01).

### Version 1.3.0-rc01

January 24, 2024

`androidx.wear.tiles:tiles-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..38756a2fd525d921dd921f38b03e0d9a23150db7/wear)

**API Changes**

- Renamed `TileService#getActiveTilesSnapshotAsync` to `getActiveTilesAsync`. ([If6b87](https://android-review.googlesource.com/#/q/If6b872cec2888a3a49eaf068e00f62e05fb1c18f))

### Version 1.3.0-beta01

January 10, 2024

`androidx.wear.tiles:tiles-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/wear/tiles)

The 1.3.0-beta01 release of Wear Tiles indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear Tiles 1.3 includes the following new functionalities and APIs:

- Module for wear tiles tooling is updated for tile preview support and is set for being published.
- Support for querying which tiles belonging to the app are active with `TileService.getActiveTilesSnapshotAsync`.

### Version 1.3.0-alpha04

December 13, 2023

`androidx.wear.tiles:tiles-*:1.3.0-alpha04` is released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/wear/tiles)

### Version 1.3.0-alpha03

November 29, 2023

`androidx.wear.tiles:tiles-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/wear/tiles)

**New Features**

- Added a new API `TileService#getActiveTilesSnapshotAsync` for querying which tiles belonging to the app are active. ([I6850e](https://android-review.googlesource.com/#/q/I6850e783d964154711fefd6b1f1a5f2f5f49a59a))

**API Changes**

- Rename `@TilePreview` to `@Preview` ([Ifc08a](https://android-review.googlesource.com/#/q/Ifc08a144da2b9fb09c88321d3c71103e2d17edb3))

### Version 1.3.0-alpha02

November 15, 2023

`androidx.wear.tiles:tiles-*:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..312eb9f1ddece3a18317f18515a877e0e745cb2c/wear/tiles)

**New Features**

- We have added an experimental API to automatically scale the text size based on the space it has inside of the parent. ([Ibbe63](https://android-review.googlesource.com/#/q/Ibbe632447dcf28a9948a0877f193b4912acb23d1))

### Version 1.3.0-alpha01

October 18, 2023

`androidx.wear.tiles:tiles-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/wear/tiles)

**New Features**

- Provide the context as a preview method parameter instead of `TilePreviewData` callback parameters. ([I5e97d](https://android-review.googlesource.com/#/q/I5e97d259efc03dd36bb6855288ebfc75bc21d0d7))
- Module for wear tiles tooling is updated for tile preview support and is set for being published. ([I63d0f](https://android-review.googlesource.com/#/q/I63d0f04780f4f28e67d40951057bcdc814f5f6d8))

## Version 1.2

### Version 1.2.0

August 9, 2023

`androidx.wear.tiles:tiles-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/07457ca20d6ae00c8e2ca5fb141efd40de8ac6ee..b9b10aa25e1bd67bdb78cc13bac036cb58657587/wear/tiles)

**Important changes since 1.1.0**

- Stable release of Wear Tiles 1.2.0 ([read more](https://android-developers.googleblog.com/2023/08/compose-for-wear-os-and-tiles-1-2-libraries-now-stable-new-features.html))
- Tiles 1.2 adds support for binding layout elements to platform data (for faster updates) and animation. For migration instructions see the release notes for ([1.2.0-rc01](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.2.0-rc01))

### Version 1.2.0-rc01

July 26, 2023

`androidx.wear.tiles:tiles-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..07457ca20d6ae00c8e2ca5fb141efd40de8ac6ee/wear/tiles)

- With the v1.2 release, Tiles library has been refactored and the majority of the features and APIs are moved into new [ProtoLayout library](https://developer.android.com/jetpack/androidx/releases/wear-protolayout) (package `androidx.wear.protolayout`) with a small subset remaining in Tiles (`androidx.wear.tiles`):

  - All classes names have stayed the same, there are only additions to the v1.1
  - The majority of the APIs have stayed the same and the only change is package name.
  - Some of the methods in `TileService/TileBuilder` have been deprecated and now have renamed versions that accept new `ProtoLayout` types instead of deprecated Tiles one.
- To make this migration easier, we have put together a small instructions and script that does this renaming, see [here](https://gist.github.com/NedaTop/68c6e708f5584061a3daf8a9e7321cfd).

**API Changes**

- We have limited the maximum depth that a layout can have to 30 nested elements in tile. If that depth is exceeded, the tile renderer will show a previously inflated layout. ([I8a74b](https://android-review.googlesource.com/#/q/I8a74b20b153652f324aa31ef9595edfaa72266c4))

### Version 1.2.0-beta01

June 21, 2023

`androidx.wear.tiles:tiles-*:1.2.0-beta01` is released with no changes. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..3b5b931546a48163444a9eddc533489fcddd7494/wear/tiles)

### Version 1.2.0-alpha07

June 7, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..d2eebe3624c889d079f3a8ba5659c91328fb56b6/wear/tiles)

**New Features**

- `TileRenderer.setState` allows setting the state for the rendering session. This state will apply to the current layout and any future one (until a new state is set) ([Iaaf35](https://android-review.googlesource.com/#/q/Iaaf35980302cd3d690f463f0649241e0122ae564))
- protolayout types are now fully supported across all tile-renderer APIS. ([I428b0](https://android-review.googlesource.com/#/q/I428b0c469c5638045802f7f014a0fb5d6185da34))

**Bug Fixes**

- Setting a custom theme is now possible in the `ProtoLayoutViewInstance`. ([Iae8c0](https://android-review.googlesource.com/#/q/Iae8c03fb195382e945867781cab4cb3c19512987))

### Version 1.2.0-alpha06

May 24, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/wear/tiles)

**API Changes**

- Rename `StateEntryValue` to `DynamicDataValue`, and update the state APIs to use the `DynamicDataKey` ([If1c01](https://android-review.googlesource.com/#/q/If1c01335804c5dd98dd2c326ec560e1816ec4c77))
- We are limiting the number of entries that are allowed in the `StateStore` in order to ensure that memory usage and state update time are well contained and controlled for each instance of the `StateStore`. As a result, the developer needs to ensure that they do not have more than `MAX_STATE_ENTRY_COUNT` entries in the map otherwise they will get an `IllegalStateException` when creating or updating the `StateStore`. ([Ibadb3](https://android-review.googlesource.com/#/q/Ibadb3c422ade12c5d77cfedac1a806e8d7b0c756))

### Version 1.2.0-alpha05

May 10, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/wear/tiles)

**New Features**

- We've added tile id to the tile events and requests. This id can be used to associate some data with a tile instance in the carousel. ([Ic4f83](https://android-review.googlesource.com/#/q/Ic4f83ae80090a3d68ddded038add627dd1f1fd9c))

**API Changes**

- `TileRenderer.inflateAsync` now returns a `ListenableFuture`. ([I2f2b9](https://android-review.googlesource.com/#/q/I2f2b9b0229dbf684445e4afad7a115de5892d869))
- Tile builders which have a replacement in the `protolayout` library are now marked as deprecated. ([Ie2029](https://android-review.googlesource.com/#/q/Ie2029716e8613f765a59adb31fcdd10431c68449))

**Bug Fixes**

- The javadoc for `TileService.onTileResourcesRequest` now clarifies when the method might be called by the system. ([Iee037](https://android-review.googlesource.com/#/q/Iee037f4aa2f60c7212003551c4fa6bcdda42058a))

### Version 1.2.0-alpha04

April 19, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/wear/tiles)

**Bug Fixes**

- The gradle dependencies are now correctly set to `api` instead of `implementation` when required. ([I40503](https://android-review.googlesource.com/#/q/I40503c70b2ea9e9d37047b4d52f4dd1c4905f5fd))

### Version 1.2.0-alpha03

April 5, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/wear/tiles)

**API Changes**

- We've added support for `androidx.wear.protolayout` types to `TileRenderer` ([I4ac7f](https://android-review.googlesource.com/#/q/I4ac7f21c084b6706b02927b5609d51ac1d1b71bc))
- `ObservableStateStore` has been renamed to `StateStore`. ([Ieb0e2](https://android-review.googlesource.com/#/q/Ieb0e23bb8e5a09ad260eac5ebe2579407b4f8c14))
- Add overloads for protolayout types to `TileRenderer` ([I4ac7f](https://android-review.googlesource.com/#/q/I4ac7f21c084b6706b02927b5609d51ac1d1b71bc))
- Enable animations in `TileRenderer` ([I07dcf](https://android-review.googlesource.com/#/q/I07dcf2050e0ddc177d3a767d8b056af7b446edc5))

### Version 1.2.0-alpha02

March 22, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553/wear)

**API Changes**

- Tiles Material library has been deprecated. Please use the new `ProtoLayout Material` library with the same functionalities. ([If242b](https://android-review.googlesource.com/#/q/If242bed2b097591a45ca90d0f2a5e9e63ad58bee))

**Bug Fixes**

- `TileRenderer` has been updated to use new features from protolayout library. ([I832f9](https://android-review.googlesource.com/#/q/I832f90d38dafd854f16ec511a617553cd1170f3d))

### Version 1.2.0-alpha01

March 8, 2023

`androidx.wear.tiles:tiles-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/302bfa3a8f2613c71f61c1133d26167dd568ff3e..ad9ba647b7548818fc9d4796a03a3b5510166fb3/wear/tiles)

**New Features**

- We've added `onTileResourceRequest` to `TileService`, for providing resources from the `protolayout` library. ([983d9c5](https://android-review.googlesource.com/#/q/I749bc23a53a5d425c74f0f2ea53204ab740711e9))
- We've updated `ResourcesRequest`and `TileRequest` to support `State` and `DeviceParameters` types from the `protolayout` library. ([88fa01d](https://android-review.googlesource.com/#/q/I0025ef0ab9b60d928f6683eb87772135220d8ff1))
- We've updated `TileBuilders.Tile` to support `State` and `Timeline` types from the `protolayout` library. ([168619c](https://android-review.googlesource.com/#/q/I5c801094fcf06af815b2b1fb0b933b59444ef20e))

**Bug Fixes**

- Improvements to Javadocs. ([I3ed73](https://android-review.googlesource.com/#/q/I3ed739a208bc700f65c73b3904185ec67ef9e7c0))
- Default colors for `onPrimary` and surface has changed. ([I0b039](https://android-review.googlesource.com/#/q/I0b0395259cc5df0430d30f4259e5e6d88d769b5a))

## Version 1.1

### Version 1.1.0

August 24, 2022

`androidx.wear.tiles:tiles-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b3d5f40aa010fdf22f7d664ad0ff77a88ac28ee..302bfa3a8f2613c71f61c1133d26167dd568ff3e/wear/tiles)

**Important changes since 1.0.0**

- This is the first stable release that contains the Tiles Material library (read more on our [blog](https://android-developers.googleblog.com/)).
- This library contains components and layouts that are in-line with Material guidelines and easy to use. The included components are `Button`, `Chip`, `CompactChip`, `TitleChip`, `CircularProgressIndicator`, `Text`.All these components have their own colors object that can be built with the main Colors class to easily apply the same theme over all components. In addition to colors, there is a Typography class to easily get FontStyle objects using the typography name.
- Besides components, there are recommended tile layouts - `PrimaryLayout`, `EdgeContentLayout`, `MultiButtonLayout`, `MultiSlotLayout`. All layouts have recommended padding and styles applied that are within Material guidelines.
- For a list of the components and layouts in Tiles Material library see the release notes for [Tiles](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.1.0-beta01).

### Version 1.1.0-rc01

August 10, 2022

`androidx.wear.tiles:tiles-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..9b3d5f40aa010fdf22f7d664ad0ff77a88ac28ee/wear/tiles)

- There were no new changes between the Beta and RC release.

### Version 1.1.0-beta01

July 27, 2022

`androidx.wear.tiles:tiles-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/wear/tiles)

The 1.0.0-beta01 release of Tiles Material library contains components and layouts that are in-line with Material guidelines and easy to build.

The included components are:

- `Button` - clickable, circular-shaped object, with either icon, text or image with 3 predefined sizes.
- `Chip` - clickable, stadium-shaped object that can contain an icon, primary and secondary labels, and has fixed height and customizable width.
- `CompactChip` \& `TitleChip` - two variations of the standard Chip that have smaller and larger heights, respectively, and can contain one line of text.
- `CircularProgressIndicator` - colored arc around the edge of the screen with the given start and end angles, which can describe a full or partial circle with the full progress arc behind it.
- `Text` - styled text which uses the recommended Wear Material typography styles

All these components have their own colors object that can be built with the main `Colors` class to easily apply the same theme over all components. In addition to colors, there is a `Typography` class to easily get `FontStyle` objects using the typography name.

In addition to components, there are recommended tiles layouts:

- `PrimaryLayout` - A layout which can be customized by adding primary or secondary labels, content in the middle, and a primary chip at the bottom. The main content within this layout could be added as a `MultiSlotLayout` or `MultiButtonLayout` object.
- `EdgeContentLayout` - A layout for hosting `CircularProgressIndicator` around the edge with main content inside and primary or secondary label around it.
- `MultiButtonLayout` - A layout that can contain 1 - 7 buttons, arranged in line with the Material guidelines depending on their number.
- `MultiSlotLayout` - A row-like style layout with horizontally aligned and spaced slots (for icons or other small content).

All layouts have recommended padding and styles applied that are within Material guidelines.

**API Changes**

- Major refactor to the Chip components that includes separating setters in Builder so that each part of the content is passed in separately with renaming to match guidelines (primary label, secondary label, image resource id). Additionally, content description will be auto generated if not set. ([I57622](https://android-review.googlesource.com/#/q/I57622f5db7b3af9494d37094fef8b4fdd83ab9ec))
- `ProgressIndicatorLayout` has been renamed to `EdgeContentLayout`. ([Ic1aa6](https://android-review.googlesource.com/#/q/Ic1aa681ded084b53febdb3337a65809da9931734))
- Button size contents have been renamed to names `without _BUTTON` suffix in it with additional Javadocs clarification across `Button`. ([I1dfe2](https://android-review.googlesource.com/#/q/I1dfe2b3f43e3d9e873b10ce238a79351ff02dd38))

**Bug Fixes**

- Margins, padding and overall arrangement in Material Layouts has been updated to accommodate all types of recommended layouts and screen sizes and shapes.
- Improvements to Material Layouts. In `MultiSlotLayout` slots are now flexible in width where they'll wrap content instead of being fixed size.([I52919](https://android-review.googlesource.com/#/q/I52919d51f3be4f47bbcc8fbb54792fb5fc2763b0)),([If18b4](https://android-review.googlesource.com/#/q/If18b40e810cb5b6f7e1b6fa4a1cb970c5c269dce))
- Area that can be tapped on `CompactChip` has been increased to follow accessibility guidelines. ([Ie8264](https://android-review.googlesource.com/#/q/Ie8264d424026e16f999b2c69a53c68b1d41b8345))

### Version 1.1.0-alpha09

June 29, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha09` is released. [Version 1.1.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..8094b683499b4098092c01028b55a38b49e357f2/wear/tiles)

**New Features**

- We have added support for adding optional labels in `ProgressIndicatorLayout`. ([I30788](https://android-review.googlesource.com/#/q/I30788aff8001fb8c2477dee8b115f51d88781af1))

**API Changes**

- Helper methods for `ElementMetadata` now accept `ElementMetadata` instead of Modifiers. ([I5a70f](https://android-review.googlesource.com/#/q/I5a70f5b81462fc8bd1a48c96149bfef5abbdb509))

**Bug Fixes**

- The limitation of 9 characters on `CompactChip` was removed. If text is too big to fit into the screen in `PrimaryLayout`, it will be ellipsized. ([Id56ec](https://android-review.googlesource.com/#/q/Id56eca1d31999330657ce8a4ad3d260ab039c16b))
- Getters in `Chip` now have *Content* suffix. ([Iba437](https://android-review.googlesource.com/#/q/Iba43761adfdb2fe1a6694a87cf5ccc402b9d5d54))
- Javadoc clarification across Tiles Material classes. ([I56e41](https://android-review.googlesource.com/#/q/I56e41ee4f0eb9c096f2def7e4daad9a36b740bcf)), ([I80f31](https://android-review.googlesource.com/#/q/I80f31a7efe8b45dfc8be733d82217c8ab23f8ba0)), ([Iba437](https://android-review.googlesource.com/#/q/Iba43761adfdb2fe1a6694a87cf5ccc402b9d5d54))

### Version 1.1.0-alpha08

June 1, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha08` is released. [Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/wear/tiles)

**New Features**

- Metadata tag has been added to Modifiers to be used to track component's metadata with helper methods added to the `Helper` class. ([I70db2](https://android-review.googlesource.com/#/q/I70db2829eddd24c4d05fa8dfc1163457ee475fce)),([I30c3d](https://android-review.googlesource.com/#/q/I30c3d7c0816a50ba8fb13e6241d5405f71cc0d5b))
- Static method `fromLayoutElement` has been added to all components and layouts inside of Tiles Material. It should be used for testing, to cast a LayoutElement obtained from accessing the contents of a container to its original type. ([Ia572a](https://android-review.googlesource.com/#/q/Ia572a1d084c94d4c9266cef2722dd7580457d331)),([Idbd8a](https://android-review.googlesource.com/#/q/Idbd8adc8587482e3bee927edf8c247e5c10bfe43)),([I3ae13](https://android-review.googlesource.com/#/q/I3ae130d66bd5bc06cf4a175f8c69e97200adb08d)),([I292fe](https://android-review.googlesource.com/#/q/I292fee874cbe76195a9ce0bec6911bbc110e932b)),([I8b20f](https://android-review.googlesource.com/#/q/I8b20f5fb74be8247ea3bf18dee4dca77a697f6f3)),([I3cacb](https://android-review.googlesource.com/#/q/I3cacb1fd116f12b9e990cef834dc244ceb785ca5)),([I84b24](https://android-review.googlesource.com/#/q/I84b243f77d67652970e8be4e0a8a9ae0041da521))

### Version 1.1.0-alpha07

May 18, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha07` is released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b18424ac8b7d47a65751381a4f8ad4777f537107..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/wear/tiles)

**API Changes**

- Getters related to different setters for content have now been added to the `ProgressIndicatorLayout` and `PrimaryLayout`. Now all setters in these classes have matching getters.([Iddbe5](https://android-review.googlesource.com/#/q/Iddbe588fbb562c7348a5cb2bfc56af7fe053b403)) ([Iabe4e](https://android-review.googlesource.com/#/q/Iabe4e6d4fc4df8a4e95a148edae14540710f21ba))
- Getter for content description in Material Components can return null since its setter is not mandatory.
- Attempting to create a Button with no content passed in will result in `IllegalArgumentException`. ([I7fc0c](https://android-review.googlesource.com/#/q/I7fc0cc24e5ccac3d1de92781e3d117bbc8030656))
- Icon color related fields in `ChipColors` have been renamed from `iconTintColor` to `iconColor`. ([Ic053b](https://android-review.googlesource.com/#/q/Ic053baaf614a88b2a7fe44806c9abc85c0bc953c))

**Bug Fixes**

- Added `androidTests` for Layouts in Tiles Material. ([I96404](https://android-review.googlesource.com/#/q/I96404dbf9d30295e89f5fdb09e44a6aa830ca7a2))

### Version 1.1.0-alpha06

May 11, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..b18424ac8b7d47a65751381a4f8ad4777f537107/wear/tiles)

**New Features**

- The new layout has been added to the Material Layouts sub library - `MultiButtonLayout`. It represents a layout that can contain between 1 and 7 buttons arranged in line with the Material guidelines. In most cases, this layout should be passed in as a content to the [PrimaryLayout](https://developer.android.com/reference/kotlin/androidx/wear/tiles/material/layouts/PrimaryLayout). ([Ib727f](https://android-review.googlesource.com/#/q/Ib727ff696b28f3f8baaad3320fbad30dff251eea))

**API Changes**

- `MultiSlotLayout` has been refactored to have only slots in it. This layout should be passed as a content to the main `PrimaryLayout`. ([I1870f](https://android-review.googlesource.com/#/q/I1870fa7dfb35e2b8188b1cd0dbe915d4d8078295))
- Updated defined default colors for `CircularProgressIndicator` to be one value instead of primary and secondary. ([I64a51](https://android-review.googlesource.com/#/q/I64a517b85324f98495551ee1d28292de2bfd43d1))
- Added getter for horizontal spacer in `MultiSlotLayout`. ([I11e1e](https://android-review.googlesource.com/#/q/I11e1e1c3ed6b7cc4159244d29a888b9bb7663e0f))

**Bug Fixes**

- Android tests for Components have been added to Tiles Material. ([I20041](https://android-review.googlesource.com/#/q/I2004154691e47c49fecc3ffd58fe5257b8e6eb98))

### Version 1.1.0-alpha05

April 6, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/wear/tiles)

**New Features**

- Added helper methods to convert `LayoutElement` to Layout, Timeline, TimelineEntry into these classes for easier Tiles building. ([I2f6d1](https://android-review.googlesource.com/#/q/I2f6d1b81d2aa2228d2b01a424cc432ecb4b352ed))
- `Colors` object was added to the Material library to be passed in across components' colors as a theme. ([I0792c](https://android-review.googlesource.com/#/q/I0792c826dc2a131d99d2b5ff56855bd6960e2c25))

**API Changes**

- Material Text component requires text passed in into constructor. This component can now be customized by setting weight. ([I25dbd](https://android-review.googlesource.com/#/q/I25dbd37e1455154f023ea5248f0b186030aee954))
- Removed constants from `ChipDefaults` that are not used in the public setters. ([I7baed](https://android-review.googlesource.com/#/q/I7baedaa3acf716594ab83de2b5b15cf793054f83))
- Removed getters from `CompactChip` \& `TitleChip` that don't have matching setters. ([I99e85](https://android-review.googlesource.com/#/q/I99e853d9986a71c86d0aa88844ab65442bc74e3a))
- Removed `DEFAULT_PADDING` from `ProgressIndicatorDefaults`. ([Idabcd](https://android-review.googlesource.com/#/q/Idabcda9d0ea686444124d29c897eaa405f9e1c96))
- Material components now accept `CharSequence` for content description instead of String. ([I5b21a](https://android-review.googlesource.com/#/q/I5b21a9ef30ddf28c63fed0fa47f9137971f2287f))

**Bug Fixes**

- Refactored setters implementation of optional parameters in Button. ([Ib7135](https://android-review.googlesource.com/#/q/Ib7135e86bf8583e3784cf50e47e63dc99eaa61af))
- Font style variant has been added to the fonts in Typography. ([I8dbc6](https://android-review.googlesource.com/#/q/I8dbc6fadd0d26428eb3a600b6f1f468e195612e9))

### Version 1.1.0-alpha04

March 23, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/wear/tiles)

**New Features**

- Optional primary or secondary label can be added to `PrimaryLayout`. ([Ib9916](https://android-review.googlesource.com/#/q/Ib9916cd8daddfbb553c29e01ec57f0f7633ded81))
- Text component can be customized by setting overflow, italic, underline, etc. ([I703f7](https://android-review.googlesource.com/#/q/I703f77ad39c8061d39f1c1ee1f00fa12057dfff2))

**API Changes**

- Default color constants have been removed from the Tiles Material API. ([I0ab55](https://android-review.googlesource.com/#/q/I0ab55d028f8828e8a61e4f8eb8d764a7f78ed1bd))
- All clickable components in Tiles Material require `Clickable` object in their Builder's constructor instead of an Action. ([I2f101](https://android-review.googlesource.com/#/q/I2f10198361549d1acf263dd80abeae8251087474))

**Bug Fixes**

- Text will now draw an ellipsis on overflow in Chip and Text component. ([I8a2f8](https://android-review.googlesource.com/#/q/I8a2f81dc91e1c7c968861be27f0f77a6d816071a))
- Improved components look when the user font scale is set to large. ([Ib63b1](https://android-review.googlesource.com/#/q/Ib63b11f27c4a75d1037555c0ea012204a25c1878))
- Clarify Javadocs of `setPrimaryChipContent` in PrimaryLayout. ([Ie6296](https://android-review.googlesource.com/#/q/Ie6296ee0ab0e1c226d543c70ce346e29d67029a5))

### Version 1.1.0-alpha03

February 23, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/wear/tiles)

**API Changes**

- `Text` component with the recommended typography styles has been added to the TIles Material. ([Iec0ae](https://android-review.googlesource.com/#/q/Iec0ae0375a7d46d9ed847bd2b84797c5bd4fc8da))

### Version 1.1.0-alpha02

February 9, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/wear/tiles)

**New Features**

- A new sub-library `layouts` in Tiles Material has been added. It contains opinionated Tiles layouts with recommended padding and margin applied to make Tile development faster and easier implementation. Initial layouts are:
  - `PrimaryLayout` ([I7ba91](https://android-review.googlesource.com/#/q/I7ba9171dfd9f2869c4f23e36dc77474054a9d1e2)) that represents the layout with a primary chip at the bottom and content in the center.
  - `MultiSlotLayout` ([I32104](https://android-review.googlesource.com/#/q/I32104317f92268cca458bf08c1bc82a4215f8051)) that represents a layout with labels on rows 1 and 3, horizontally aligned and spaced slots on row 2 and all followed by a 4th row that contains a primary chip.
  - `ProgressIndicatorLayout` ([I9fec6](https://android-review.googlesource.com/#/q/I9fec616fd8ed5d5da2f0ece8c29d8e71ba12df6a)) that represents a layout with the circular progress indicator around the edge of the screen and the given content inside.
- `CircularProgressIndicator` ([Ic4b88](https://android-review.googlesource.com/#/q/Ic4b88bf0cfbf78596b49f6a4b0251b729047b856)) has been added to the Tiles Material components.

**API Changes**

- Renamed remaining constants used by `TitleChip` to include title in the name. ([I14f4c](https://android-review.googlesource.com/#/q/I14f4c754286cc4c424dfa533506bdc7913d34324))
- `setHorizontalAlignment` method has been added to the `Chip`. ([Ie6e0b](https://android-review.googlesource.com/#/q/Ie6e0b72503a0cdbc823f4b6d3411b34c53b425b0))

### Version 1.1.0-alpha01

January 26, 2022

`androidx.wear.tiles:tiles-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e632337e786a8f1ca1f8830e988656e02548a89e..9dceceb54300ed028a7e8fc7a3454f270337ffde/wear/tiles)

**New Features**

- The new library Tiles Material has been added. It contains components to build Tiles layouts faster and easier with Material design. Initial components are:
  - `Button`
  - `Chip`
  - `CompactChip`
  - `TitleChip`

**Bug Fixes**

- Fix bug in `TileUiClient` which led to cached resources being discarded. ([I60e0b](https://androidreview.googlesource.com/q/I60e0b805cce3a72c7b33cb4c8e9e60dfb44ed1a5))

## Version 1.0

### Version 1.0.1

January 26, 2022

`androidx.wear.tiles:tiles-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e632337e786a8f1ca1f8830e988656e02548a89e..6b618f7306add6aed50820b805172424cb35d6ce/wear/tiles)

**Bug Fixes**

- Fix bug in `TileUiClient` which led to cached resources being discarded. ([I60e0b](https://android-review.googlesource.com#/q/I60e0b805cce3a72c7b33cb4c8e9e60dfb44ed1a5))

### Version 1.0.0

November 3, 2021

`androidx.wear.tiles:tiles-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8651d9ea0f2523efe566785034a57a30f2a53e53..e632337e786a8f1ca1f8830e988656e02548a89e/wear/tiles)

**Major features of 1.0.0**

- The Wear Tiles library provides functionality to build custom Tiles for Wear OS devices, along with the classes that allow the system to fetch your Tile and display it right next to your watch face.
- tiles-renderer allows you to show a Tile as part of an Android Activity, facilitating quick testing of your tile layouts.

### Version 1.0.0-rc01

October 27, 2021

`androidx.wear.tiles:tiles-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..8651d9ea0f2523efe566785034a57a30f2a53e53/wear/tiles)

### Version 1.0.0-beta01

October 13, 2021

`androidx.wear.tiles:tiles-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/wear/tiles)

**Bug Fixes**

- Fixed `NullPointerException` in `TileUiClient` when an empty resource version was provided. ([I0586e](https://android-review.googlesource.com/#/q/I0586ea13311ffe1e8fba6b0304c508f344b1c25a))

### Version 1.0.0-alpha12

September 29, 2021

`androidx.wear.tiles:tiles-*:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/wear/tiles)

**Bug Fixes**

- UpdateScheduler no longer uses a weak
  reference, fixing issues where TileUiClient would not update([I1120d](https://android-review.googlesource.com/#/q/I1120ddab0752d5f2104cf65bd4235783b6b818c2), [b/199061124](https://issuetracker.google.com/issues/199061124))

- Declare that SysUiTileUpdateRequester queries PacakgeManager, fixing a
  bug where tile updates would not work on R+ devices. ([I1120d](https://android-review.googlesource.com/#/q/I1120ddab0752d5f2104cf65bd4235783b6b818c2))

### Version 1.0.0-alpha11

September 1, 2021

`androidx.wear.tiles:tiles-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae/wear/tiles)

**New Features**

- Added and released a testing library, androidx.wear.tiles:tiles-testing library to enable developers to test their tiles more easily. ([Iedb6b](https://android-review.googlesource.com/#/q/Iedb6b68e14e7bf0a7e68379f5baf5e9bdcbdfa3b))

**API Changes**

- Renamed TileProviderService to TileService. ([I1ad2c](https://android-review.googlesource.com/#/q/I1ad2c33119a4e098a458c4791d27409b3f5fc1a9))
- Tiles builders updated; static `.builder()` methods have been deprecated in favour of calling `new Foo.Builder()`, and setter overloads which accepted a `Builder` instance have been removed. ([Ia9606](https://android-review.googlesource.com/#/q/Ia9606d0f656fde599851bc2b8a0140a0256cccaa))
- TileRenderer should now use a UI context, instead of the application context. ([I84b61](https://android-review.googlesource.com/#/q/I84b6186474f9bc4c02fe3621a7956e345aacd364))

**Bug Fixes**

- Fix bug causing multiple underlines to be applied in certain situations. ([Ib6712](https://android-review.googlesource.com/#/q/Ib6712e68987be272f471e8c229840f57cd6f3845))

### Version 1.0.0-alpha10

August 18, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha10`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha10`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha10` are released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/wear/tiles)

**API Changes**

- Removed layout checkers from public API. These will always be enabled, although will only raise a warning if a check fails. ([Ie9f29](https://android-review.googlesource.com/#/q/Ie9f2944b028e8a0ad00f36a7748eb31c828499cf))
- TileRenderer now accepts a UI context, instead of the Application Context.

**Bug Fixes**

- Fixed bug which prevented clickable elements in a Spannable from being clicked.

### Version 1.0.0-alpha09

July 21, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha09`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha09`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/wear/tiles)

**New Features**

- Added layout checkers to Wear Tiles' renderer. ([I3a869](https://android-review.googlesource.com/#/q/I3a8692e72398b01fdb29a19b7f64d6d9452032de))
  - These are used to validate best practises in your tile. To begin with, these will raise a warning if your tile does not contain any elements with a `Semantics` modifier.
- Added documentation for `DefaultTileProviderClient` and `TestingTileProviderClient constructors`. ([I9f4b9](https://android-review.googlesource.com/#/q/I9f4b9b06673a425efb9b4f12dd35248052982b7b))

**API Changes**

- Renaming in TileProviderClient ([I0ec36](https://android-review.googlesource.com/#/q/I0ec368d77860a55f6cac36de01e8d718a6c92587)):
  - `getApiVersion` -\> `requestApiVersion`
  - `tile/resourcesRequest` -\> `requestTile/Resources`
  - `onTileFooEvent` -\> `sendOnTileFooEvent`
- Added layout checkers to Wear Tiles' renderer. ([I3a869](https://android-review.googlesource.com/#/q/I3a8692e72398b01fdb29a19b7f64d6d9452032de))

**Bug Fixes**

- Ensure that a LaunchAction target does not have special permissions. ([I39136](https://android-review.googlesource.com/#/q/I391366818173f1f313806c45da729c539a70a7da))

### Version 1.0.0-alpha08

June 30, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha08`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha08`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..19ae3a88ff0824d615355b492cb56049e16991f2/wear/tiles)

**New Features**

- Spannables now support line_height instead of line_spacing.

**API Changes**

- Add support for line_height in Spannables, remove line_spacing. ([Ibeb54](https://android-review.googlesource.com/#/q/Ibeb54523224d4514ba5c94d83a0a34d7d4abfb21))
  - Code using line_spacing should be ported to use line_height instead.

**Bug Fixes**

- Fix bug when using proportional dimensions. ([I37ace](https://android-review.googlesource.com/#/q/I37ace9ae4619027467b4593aa798f2ce54611907))
- Fix bug preventing Text elements having content descriptions. ([Id2c7d](https://android-review.googlesource.com/#/q/Id2c7dcc2cf9fcddb26ed88518b9192ebc1e1a97f))

### Version 1.0.0-alpha07

June 16, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha07`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha07`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..ccf79f53033e665475116a4e78ff124df2a52c4b/wear/tiles)

**API Changes**

- Add `TileProviderClient` interface, and expose `DefaultTileProviderClient`, allowing implementations to bind to a `TileProviderService` interface. ([I69165](https://android-review.googlesource.com/#/q/I691659d10e9cc011cb612fc2df0f7f2a8d509a73))

### Version 1.0.0-alpha06

June 2, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha06`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha06`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/wear/tiles)

**API Changes**

- All Builder classes now contain getters for all properties. Note that these are intended for testing purposes only ([I9d155](https://android-review.googlesource.com/#/q/I9d1554305b55d2e3c2676084fe8a6f0ef5e51aeb))
- Package change: Classes in `androidx.wear.tiles.builders` have been moved to `androidx.wear.tiles`.
- Add experimental tint support to Tiles. ([I38929](https://android-review.googlesource.com/#/q/I389299a4fb863f72052f96ecb7b75b719196ec1a))
- Renamed `LayoutElementBuilders.HALIGN_*` to `LayoutElementBuilders.HORIZONTAL_ALIGN_*` ([I67e58](https://android-review.googlesource.com/#/q/I67e58029203dcceed3444f7c86a4b04a4dd2a325))
- Renamed `LayoutElementBuilders.VALIGN_*` to `LayoutElementBuilders.VERTICAL_ALIGN_*` ([I67e58](https://android-review.googlesource.com/#/q/I67e58029203dcceed3444f7c86a4b04a4dd2a325))
- Renamed `LayoutElementBuilders.SPAN_VALIGN_*` to `LayoutElementBuilders.SPAN_VERTICAL_ALIGN_*` ([I67e58](https://android-review.googlesource.com/#/q/I67e58029203dcceed3444f7c86a4b04a4dd2a325))
- Added builder classes for Requests and Events. ([Ib5cf4](https://android-review.googlesource.com/#/q/Ib5cf4cf39e98656ac8650207953faaf756a8c1c7))
- Migrated `TileProviderService` to use request and event classes from `RequestBuilders` and `EventBuilders`, rather than `RequestReaders`/`EventReaders` (e.g. `onTileRequest` now provides you with a `RequestBuilders.TileRequest`, rather than `RequestReaders.TileRequest`). ([I46ea1](https://android-review.googlesource.com/#/q/I46ea19332f3544c936f3e46343d7532ff0513aad))

**Bug Fixes**

- Fix bug in async image loading for Tiles renderer. ([Iad9b0](https://android-review.googlesource.com/#/q/Iad9b03e39a1a288b0f90cb3a9d471b4041acde4a))
- Fixed layout bug when placing an image with width or height set to `expand()` in a `Box` with width or height set to `wrap()`. ([I33770](https://android-review.googlesource.com/#/q/I33770e987e419a0d03ae95e7ddceb42904ace9f7))

### Version 1.0.0-alpha05

May 18, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha05`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha05`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/wear/tiles)

**API Changes**

- Removed getTileId from incoming tile events (`TileAddEvent`, `TileRemoveEvent`, `TileEnterEvent`, `TileLeaveEvent`, `TileRequest`). ([Ifbba2](https://android-review.googlesource.com/#/q/Ifbba2ecaf6caddb899de91a2d2d7ee79b1d6c9ff))
- Renamed `ImageResource#setAndroidResourceByResid` to `setAndroidResourceByResId` ([I4ba6e](https://android-review.googlesource.com/#/q/I4ba6e3f4a956f715cc98b323b628fc69b4076f79))
- Renamed `TimelineManager#deInit` to close, and implemented `AutoCloseable`. ([I5dff2](https://android-review.googlesource.com/#/q/I5dff2b1b9bf64c0af39c8af91c481b4e76682ced))

### Version 1.0.0-alpha04

May 5, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha04`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha04`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ddfc1583c09aaa878d34437fbfee1b995b60d3a..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/wear/tiles)

**API Changes**

- Hidden concrete TileProviderService classes.
  - Made TileUpdateRequester take a `Class<? extends TileProviderService>`. ([Ib7cca](https://android-review.googlesource.com/#/q/Ib7ccab689da6c43f8d210109cbfeef1e1c1b8c54))
- Added ability to add extras to AndroidActivity. ([I748f4](https://android-review.googlesource.com/#/q/I748f4516245ee82f86d12a7e6b076bd7cf4a4ded))

### Tiles Version 1.0.0-alpha03

April 21, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha03`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha03`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25..4ddfc1583c09aaa878d34437fbfee1b995b60d3a/wear/tiles)

**API Changes**

- Rename `TileManager` -\> `TileClient`
  - Rename `TileManager#create` -\> `TileClient#connect` ([I91839](https://android-review.googlesource.com/#/q/I9183961e3578a74f0614dbd48c87d48e591df397))

**Bug Fixes**

- Added Proguard rules to ensure `tiles` and `tiles-renderer` work properly with Proguard enabled ([Ie3d85](https://android-review.googlesource.com/#/q/Ie3d85bc41303dfc45aeba14e1897d47408b6cdaa))

### Version 1.0.0-alpha02

April 7, 2021

`androidx.wear.tiles:tiles:1.0.0-alpha02`, `androidx.wear.tiles:tiles-proto:1.0.0-alpha02`, and `androidx.wear.tiles:tiles-renderer:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25/wear/tiles)

**API Changes**

- `androidx.wear:wear-tiles` has moved groups, and should now be referred to as `androidx.wear.tiles:tiles`
- `androidx.wear:wear-tiles-renderer` has moved groups, and should now be referred to as `androidx.wear.tiles:tiles-renderer`
- `TileRenderer.LoadActionListener` now consumes an instance of `androidx.wear.tiles.builders.StateBuilders.State` rather than `androidx.wear.tiles.proto.StateProto.State`.
- `TileRenderer` now accepts Tile resources from `androidx.wear.tiles.builders.ResourceBuilders.Resources`, rather than an instance of `androidx.wear.tiles.renderer.ResourceAccessors`.

**Bug Fixes**

- Fixed inability to use `LoadActionListener`, as it exposed an internal class.

### Version 1.0.0-alpha01

March 10, 2021

`androidx.wear:wear-tiles:1.0.0-alpha01`, `androidx.wear:wear-tiles-proto:1.0.0-alpha01`, and `androidx.wear:wear-tiles-renderer:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51/wear)

**New Features**

- The Wear Tiles Renderer library provides functionality to build custom Tiles for Wear OS devices, along with the classes that allow the system to fetch your Tile and display it right next to your watch face.

> [!NOTE]
> **Note:** While you can build and test Tiles with the alpha version of this library, these Tiles aren't currently displayed to Wear OS users.