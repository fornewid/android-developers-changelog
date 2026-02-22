---
title: https://developer.android.com/jetpack/androidx/releases/camera-viewfinder
url: https://developer.android.com/jetpack/androidx/releases/camera-viewfinder
source: md.txt
---

# camera viewfinder

API Reference  
[androidx.camera.viewfinder](https://developer.android.com/reference/kotlin/androidx/camera/viewfinder/package-summary)  
Standalone Composable and View based Viewfinder for Camera"


This table lists all the artifacts in the `androidx.camera-viewfinder` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| viewfinder-compose | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.5.3) | - | [1.6.0-beta02](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.6.0-beta02) | - |
| viewfinder-core | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.5.3) | - | [1.6.0-beta02](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.6.0-beta02) | - |
| viewfinder-view | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.5.3) | - | [1.6.0-beta02](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.6.0-beta02) | - |

This library was last updated on: February 11, 2026

## Declaring dependencies

To add a dependency on camera-viewfinder, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement camera viewfinders
    
    implementation "androidx.camera.viewfinder:viewfinder-view:1.6.0-beta02"
    implementation "androidx.camera.viewfinder:viewfinder-compose:1.6.0-beta02"
    implementation "androidx.camera.viewfinder:viewfinder-core:1.6.0-beta02"

}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement camera viewfinders
    implementation("androidx.camera.viewfinder:viewfinder-view:1.6.0-beta02")
    implementation("androidx.camera.viewfinder:viewfinder-core:1.6.0-beta02")
    implementation("androidx.camera.viewfinder:viewfinder-compose:1.6.0-beta02")


}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:618491+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=618491&template=1257717)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.6

### Version 1.6.0-beta02

February 11, 2026

`androidx.camera.viewfinder:viewfinder-compose:1.6.0-beta02`, `androidx.camera.viewfinder:viewfinder-core:1.6.0-beta02`, and `androidx.camera.viewfinder:viewfinder-view:1.6.0-beta02` are released. Version 1.6.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/48e95c38588deabd109b960f6d6ba5f47461c192..82004373076cf552e53b43166e1b4ddfbcfec21e/camera/viewfinder).

### Version 1.6.0-beta01

January 28, 2026

`androidx.camera.viewfinder:viewfinder-compose:1.6.0-beta01`, `androidx.camera.viewfinder:viewfinder-core:1.6.0-beta01`, and `androidx.camera.viewfinder:viewfinder-view:1.6.0-beta01` are released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/84753047f87d847904220ad53b1c78d1a98189c4..5fc4e0225a10d812728a4bece5a2f6e82737df85/camera/viewfinder).

### Version 1.6.0-alpha02

December 17, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.6.0-alpha02`, `androidx.camera.viewfinder:viewfinder-core:1.6.0-alpha02`, and `androidx.camera.viewfinder:viewfinder-view:1.6.0-alpha02` are released. Version 1.6.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dacd36e7413e15947cdd89e21c189fead769bfab..84753047f87d847904220ad53b1c78d1a98189c4/camera/viewfinder).

### Version 1.6.0-alpha01

October 22, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.6.0-alpha01`, `androidx.camera.viewfinder:viewfinder-core:1.6.0-alpha01`, and `androidx.camera.viewfinder:viewfinder-view:1.6.0-alpha01` are released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..dacd36e7413e15947cdd89e21c189fead769bfab/camera/viewfinder).

**API Changes**

- Exposed the default viewfinder `ImplementationMode` via the new `ViewfinderDefaults.implementationMode` public API. This is now used as the default for both `ViewfinderView` and the `Viewfinder` composable. ([Ic3f52](https://android-review.googlesource.com/#/q/Ic3f52afe6a4e188b3487f124b4fa873d5e2f2b06))

## Version 1.5

### Version 1.5.3

January 28, 2026

`androidx.camera.viewfinder:viewfinder-compose:1.5.3`, `androidx.camera.viewfinder:viewfinder-core:1.5.3`, and `androidx.camera.viewfinder:viewfinder-view:1.5.3` are released. Version 1.5.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0975f1cec9e7c5b1192d3ceb925b3178cd234957..2afad3835627a7fdd11578788696f14b7aff6017/camera/viewfinder).

### Version 1.5.2

December 4, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.2`, `androidx.camera.viewfinder:viewfinder-core:1.5.2`, and `androidx.camera.viewfinder:viewfinder-view:1.5.2` are released. Version 1.5.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..0975f1cec9e7c5b1192d3ceb925b3178cd234957/camera/viewfinder).

### Version 1.5.1

October 08, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.1`, `androidx.camera.viewfinder:viewfinder-core:1.5.1`, and `androidx.camera.viewfinder:viewfinder-view:1.5.1` are released. Version 1.5.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bf14d325dfcbc73bf18b092f0435beaaf465e126..e7bb7786b42348603fed2825d18815e6dfa9bd4b/camera/viewfinder).

### Version 1.5.0

September 10, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.0`, `androidx.camera.viewfinder:viewfinder-core:1.5.0`, and `androidx.camera.viewfinder:viewfinder-view:1.5.0` are released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3496263efa2133a8c8cd25f4ae6509b9d28a788f..bf14d325dfcbc73bf18b092f0435beaaf465e126/camera/viewfinder).

**Important changes since 1.4.0:**

This is the first stable release of the Camera Viewfinder library, providing robust, lifecycle-aware, and easy-to-use View and Compose-based APIs. These components are designed to serve as a camera viewfinder and can be integrated directly with Camera2.

This release also establishes the foundation for the new `androidx.camera:camera-compose` artifact, which introduces `CameraXViewfinder`, a Compose-idiomatic viewfinder that integrates seamlessly with CameraX `SurfaceRequest`s, similar to how `PreviewView` works for View-based layouts. Some of the most important changes include:

- **Artifact Relocation:** To improve modularity, the Viewfinder artifacts have been moved to their own library group. Developers previously using `androidx.camera:camera-viewfinder*` dependencies should migrate to `androidx.camera.viewfinder:viewfinder-*`.
- **API Stabilization and Refinements:** The API surface has been polished for this stable release. This includes renaming `CameraViewfinder` to `ViewfinderView` to better reflect its versatility, reorganizing packages for clarity, and making `ViewfinderSurfaceRequest` an immutable data type for more predictable state management.
- **Compose API Updates:** The Compose `Viewfinder` API now supports `ContentScale` and `Alignment` for fine-grained control over how the camera stream is displayed within its container, mirroring the behavior of the standard `androidx.compose.foundation.Image` composable.
- **Surface Lifecycle Management:** `ViewfinderSurfaceSession` is now kept alive across configuration changes and lifecycle events on API 29+. This change is designed to reduce dropped frames and provide a smoother user experience.
- **Implementation Mode Defaults:** The `Viewfinder` now defaults to an intelligent `ImplementationMode` that automatically selects the best underlying implementation. It prioritizes the high-performance `SurfaceView` (`EXTERNAL` mode) and gracefully falls back to the more compatible `TextureView` (`EMBEDDED` mode) on older API levels or devices with known compatibility issues. This behavior can still be overridden for full developer control.

**Bug Fixes**

- The composable `Viewfinder` now works correctly within Compose's `Pager` and with `movableContentOf()`, ensuring the surface is properly reset and managed in complex UI scenarios. ([I0d9be](https://android-review.googlesource.com/#/q/I0d9be911aea9fed574dde8ba988af7882dfc2dc9),[I79432](https://android-review.googlesource.com/#/q/I79432d3ad761fce4db134297c6057f357d9a7cf0))
- Fixed an issue on Android 10 and 11 where the `SurfaceView`-based `Viewfinder` could appear stretched when transformations were applied. ([Icc77c](https://android-review.googlesource.com/#/q/Icc77c83b338df1828014f8fe27703d90e62cdea5))

### Version 1.5.0-rc01

August 13, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.0-rc01`, `androidx.camera.viewfinder:viewfinder-core:1.5.0-rc01`, and `androidx.camera.viewfinder:viewfinder-view:1.5.0-rc01` are released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f22a8ba695b5a3d975f57d279262d9d39444d990..3496263efa2133a8c8cd25f4ae6509b9d28a788f/camera/viewfinder).

**Bug Fixes**

- Moving the default `minSdk` from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.5.0-beta03

July 16, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.0-beta03`, `androidx.camera.viewfinder:viewfinder-core:1.5.0-beta03`, and `androidx.camera.viewfinder:viewfinder-view:1.5.0-beta03` are released. Version 1.5.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7442ed2cb3111f2187694f18723b4fbd1c9efa69..f22a8ba695b5a3d975f57d279262d9d39444d990/camera/viewfinder).

**Bug Fixes**

- The default `ImplementationMode` for `Viewfinder` (both Compose and View-based) now intelligently selects between `EXTERNAL` (for performance) and `EMBEDDED` (for compatibility on older APIs/quirky devices). This behavior can still be overridden by explicit settings in `ViewfinderSurfaceRequest` or XML attributes (on the View-based API). ([Iecd3a](https://android-review.googlesource.com/#/q/Iecd3a80941ccbd4ace9b246fc7dcf713c4714259))
- Improved Surface session management by allowing the `ViewfinderSurfaceSession` to be kept alive across surface create/destroy lifecycles when using TextureView or SurfaceView on API 29+. ([I112d9](https://android-review.googlesource.com/#/q/I112d96bf0d5cc70aa9f9694f8158a098f9d63b74))
- The `Viewfinder` now ensures Surfaces are released at the proper time, only when no longer in use by the session, rather than always releasing when the Composable is disposed. For `EXTERNAL` (`SurfaceView`) this behavior is currently only available on API 29+. For `EMBEDDED` (`TextureView`), this behavior is present on all API levels. ([I9a03f](https://android-review.googlesource.com/#/q/I9a03fee7a06b7fa8f6b7748c0e71dc7ee522de28))
- The `Viewfinder` now properly handles surface replacement in scenarios such as when an `EXTERNAL` viewfinder on API level 28 or lower moves off screen or if a `Viewfinder` (with any `ImplementationMode`) is part of `moveableContentOf()`. ([I79432](https://android-review.googlesource.com/#/q/I79432d3ad761fce4db134297c6057f357d9a7cf0))
- Composable `Viewfinder` now works correctly with Compose's `Pager`. This change ensures that the Composable can be successfully reset by implementing the `onReset` callback of `AndroidView`, supporting both `EMBEDDED` and `EXTERNAL` implementations. ([I0d9be](https://android-review.googlesource.com/#/q/I0d9be911aea9fed574dde8ba988af7882dfc2dc9))
- Fixes an issue on Android 10/11 where the `EXTERNAL` `Viewfinder` could appear stretched or incorrect due to transformation operations (like scale or translate) being applied too early. The system now waits for the Surface to be created before applying these transformations in the layout phase, ensuring correct output. ([Icc77c](https://android-review.googlesource.com/#/q/Icc77c83b338df1828014f8fe27703d90e62cdea5))

### Version 1.5.0-beta02

June 4, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.0-beta02`, `androidx.camera.viewfinder:viewfinder-core:1.5.0-beta02`, and `androidx.camera.viewfinder:viewfinder-view:1.5.0-beta02` are released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314..7442ed2cb3111f2187694f18723b4fbd1c9efa69/camera/viewfinder).

### Version 1.5.0-beta01

May 7, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.5.0-beta01`, `androidx.camera.viewfinder:viewfinder-core:1.5.0-beta01`, and `androidx.camera.viewfinder:viewfinder-view:1.5.0-beta01` are released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/824a6d81bccbc4bf5286a94e6476d35825adf198..a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314/camera/viewfinder).

- This is the first official beta release of the view-based and compose-based viewfinders that are flexible enough to be used with Camera2. If you're looking for a View or composable to use with CameraX, see [`PreviewView`](https://developer.android.com/reference/androidx/camera/view/PreviewView) and [`CameraXViewfinder`](https://developer.android.com/reference/kotlin/androidx/camera/compose/package-summary#CameraXViewfinder(androidx.camera.core.SurfaceRequest,androidx.camera.viewfinder.core.ImplementationMode,androidx.camera.viewfinder.core.TransformationInfo,androidx.compose.ui.Modifier,androidx.camera.viewfinder.compose.MutableCoordinateTransformer,androidx.compose.ui.Alignment,androidx.compose.ui.ContentScale)).

**New Features**

- `ContentScale` and `Alignment` can now be used in the compose-based viewfinder to scale and place the displayed surface within its container, similar to how `androidx.compose.foundation.Image` behaves. ([Ibcea3](https://android-review.googlesource.com/#/q/Ibcea3e4d1ea1badc0134df3f328a1710dcb4c20e))

**API Changes**

- `TransformationInfo` now has default values for all args. This will allow Viewfinders to be created without any `TransformationInfo`, which will default to a source rotation of 0, no source mirroring, and no crop rect. ([I2b1b2](https://android-review.googlesource.com/#/q/I2b1b26e8f966363809a235424e0c19f2a6bd97b8))
- Composable Viewfinder now takes a trailing lambda to receive a Surface session, similar to `AndroidExternalSurface`. The provided lambda uses `ViewfinderInitScope` as a receiver, which allows installing a callback to receive new Surface sessions. These surface sessions automatically release resources held by the Viewfinder when they go out of scope. ([Ib2b0d](https://android-review.googlesource.com/#/q/Ib2b0d565883bbc4817d2dc77c12df198878b5770))
- `ViewfinderSurfaceRequest.Builder.populateFromCharacteristics` has now been removed and is now replaced with an equivalent set of static APIs that can be used to generate `TransformationInfo` which will produce the same transformation as `populateFromCharacteristics`. These static methods are added to the `Camera2TransformationInfo` class. ([Idc6af](https://android-review.googlesource.com/#/q/Idc6af2f22621d9a050d02bf18ef1f7daf6bd1742))
- `ViewfinderSurfaceRequest` no longer includes async APIs for retrieving the surface. It is now an immutable data type. APIs for retrieving the Surface are now moved to the viewfinder. ([I30127](https://android-review.googlesource.com/#/q/I30127dff80267a5594c95b8d338cd96208035609))
- `CameraViewfinder` has been renamed to `ViewfinderView` so that the naming aligns with the naming of the Viewfinder composable and to indicate that it can be used with more than just camera sources. ([Id9e6b](https://android-review.googlesource.com/#/q/Id9e6bb2c7b8f9a14f19a24386e627c8c718fe02f))
- Classes from `viewfinder-view` have been moved to the `androidx.camera.viewfinder.view` subpackage from the `androidx.camera.viewfinder` package. ([I6cb44](https://android-review.googlesource.com/#/q/I6cb440cb6cb801564a097d06e773374bbd4b7506))
- New APIs are added to view-based Viewfinder that allow setting the source rotation, mirroring, and crop rectangle. This `TransformationInfo` class is the same class used by the compose-based Viewfinder. ([I907c3](https://android-review.googlesource.com/#/q/I907c307a2275447a370e6946c8aa030e268dad91))
- The view-based Viewfinder now uses new `ViewfinderSurfaceRequest` APIs which no longer internally handle the Surface response. Instead of returning `ListenableFuture<Surface>`, the `requestSurfaceSession()` APIs now return `ListenableFuture<ViewfinderSurfaceSession>` which returns an `AutoCloseable` class that when closed behaves the same way as calling the old API of `ViewfinderSurfaceRequest.markSurfaceSafeToRelease()`. This provides a clearer separation of responsibilities between the surface request and surface response. ([I19041](https://android-review.googlesource.com/#/q/I19041b515efec4e3f82b125f066b25a08703902b))

## Version 1.4

### Version 1.4.0-alpha13

February 26, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha13`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha13`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha13` are released. Version 1.4.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/74cbb818c9b3bfa4d09302a96cfde2c21c98d693..824a6d81bccbc4bf5286a94e6476d35825adf198/camera/viewfinder).

### Version 1.4.0-alpha12

January 15, 2025

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha12`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha12`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha12` are released. Version 1.4.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/619c6de87fe3f2c27da0045968f503c1bbd40ef6..74cbb818c9b3bfa4d09302a96cfde2c21c98d693/camera/viewfinder).

**New Features**

- Upgraded `compileSdk` as 35 for using Android 15 related API. Apps using CameraX libraries will also need to upgrade their `compileSdk` config setting. ([Ic80cd](https://android-review.googlesource.com/#/q/Ic80cd9e0eea7adc72419a22c1ab5035e7fc5fb61))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I7bcd7](https://android-review.googlesource.com/#/q/I7bcd759969c194304f52523354c792d19e52903b), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.4.0-alpha11

December 11, 2024

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha11`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha11`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha11` are released. Version 1.4.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd1d1e576a596e4748da989ef803d52d4e2e772b..619c6de87fe3f2c27da0045968f503c1bbd40ef6/camera/viewfinder).

**API Changes**

- `viewfinder-core` classes have been moved into packages that are consistent with the library they belong to. ([I431c6](https://android-review.googlesource.com/#/q/I431c6032114664ab915e35f77251ce677017c639))
- `CameraViewfinder.ScaleType` has been moved to `viewfinder-core` so it can be reused with compose ([I87ef1](https://android-review.googlesource.com/#/q/I87ef1575ebb402c51fb9d5576f7ac7c931b68bbb))
- Deprecated `CameraViewfinder` classes are removed. Please use the new APIs which provide equivalent functionality. ([I6e59a](https://android-review.googlesource.com/#/q/I6e59a75c1b44fd371d4662246f537b706c8ae7fa))

### Version 1.4.0-alpha10

October 30, 2024

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha10`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha10`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha10` are released. Version 1.4.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c5333e2c7d785dd314479d930f3927d8ea9b7bcf..fd1d1e576a596e4748da989ef803d52d4e2e772b/camera/viewfinder).

### Version 1.4.0-alpha09

October 2, 2024

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha09`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha09`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha09` are released. Version 1.4.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/445fd4cb2234969b1622d272e143642886cf13eb..c5333e2c7d785dd314479d930f3927d8ea9b7bcf/camera/viewfinder).

### Version 1.4.0-alpha08

September 4, 2024

`androidx.camera.viewfinder:viewfinder-compose:1.4.0-alpha08`, `androidx.camera.viewfinder:viewfinder-core:1.4.0-alpha08`, and `androidx.camera.viewfinder:viewfinder-view:1.4.0-alpha08` are released. Version 1.4.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/445fd4cb2234969b1622d272e143642886cf13eb/camera/viewfinder).

**New Features**

With the update to 1.4.0-alpha08, the CameraX Viewfinder artifact has been moved to its own library group. This change is necessary to improve the modularity and maintainability of the CameraX library.

If you were previously depending on `androidx.camera:camera-viewfinder`, `androidx.camera:camera-viewfinder-compose` or `androidx.camera:camera-viewfinder-core`, you will need to transition your dependencies to the following:

- `androidx.camera:camera-viewfinder` -\> `androidx.camera.viewfinder:viewfinder-view`
- `androidx.camera:camera-viewfinder-compose` -\> `androidx.camera.viewfinder:viewfinder-compose`
- `androidx.camera:camera-viewfinder-core` -\> `androidx.camera.viewfinder:viewfinder-core`

No code changes should be needed to make this transition. The old Viewfinder maven coordinates will no longer receive updates.

Additionally, if you are using Compose with CameraX, a new Compose-first library is now available in alpha: `androidx.camera:camera-compose`. This provides the `CameraXViewfinder` composable, which is a compose-idiomatic Viewfinder that adapts CameraX's `SurfaceRequest` to Compose, similar to how `PreviewView` works for views.