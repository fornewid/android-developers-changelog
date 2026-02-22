---
title: https://developer.android.com/jetpack/androidx/releases/graphics
url: https://developer.android.com/jetpack/androidx/releases/graphics
source: md.txt
---

# graphics

API Reference  
[androidx.graphics](https://developer.android.com/reference/kotlin/androidx/graphics/package-summary)  
Leverage graphics facilities across multiple Android platform releases  


This table lists all the artifacts in the `androidx.graphics` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| graphics-core | [1.0.4](https://developer.android.com/jetpack/androidx/releases/graphics#graphics-core-1.0.4) | - | - | - |
| graphics-path | [1.0.1](https://developer.android.com/jetpack/androidx/releases/graphics#graphics-path-1.0.1) | - | [1.1.0-beta01](https://developer.android.com/jetpack/androidx/releases/graphics#graphics-path-1.1.0-beta01) | - |
| graphics-shapes | [1.1.0](https://developer.android.com/jetpack/androidx/releases/graphics#graphics-shapes-1.1.0) | - | - | - |

This library was last updated on: December 17, 2025

## Declaring dependencies

To add a dependency on Graphics, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.graphics:graphics-core:1.0.4"
    implementation "androidx.graphics:graphics-path:1.1.0-beta01"
    implementation "androidx.graphics:graphics-shapes:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.graphics:graphics-core:1.0.4")
    implementation("androidx.graphics:graphics-path:1.1.0-beta01")
    implementation("androidx.graphics:graphics-shapes:1.1.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1262687+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1262687&template=1745326)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Graphics Version 1.1

### Version 1.1.0

October 22, 2025

`androidx.graphics:graphics-*:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e4b672d6ee0029b3ab664d3c70b7f97b01376f8b..cb163bee53214245ad7a23367396a21b7f85ae82/graphics/graphics-shapes).

### Version 1.1.0-rc01

September 10, 2025

`androidx.graphics:graphics-*:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/def3e53c2013cff4f8a9ddd8e8be7b016a9d2c42..a1575365889263a8ae455c8127adea239f056f80/graphics/graphics-shapes).

### Version 1.1.0-beta01

July 30, 2025

`androidx.graphics:graphics-*:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..def3e53c2013cff4f8a9ddd8e8be7b016a9d2c42/graphics/graphics-shapes).

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Add `mingwX64`, js and wasm compilation targets. ([I2c46a](https://android-review.googlesource.com/#/q/I2c46afdeff9feb294cd7957103b992ef458d6c6f))

### Version 1.1.0-alpha01

December 11, 2024

`androidx.graphics:graphics-*:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/17aea5b083ca354fcad646462e8d3d0c211f1eae..46295bc0b75a16f452e8e0090e8de41073d4dbb6/graphics/graphics-shapes).

**New Features**

- Reworked the main demo into a generic Shape Editor. This allows you to import shapes from a svg path, manually edit the detected features in case of misses in the automatic process, and export the result into code that can be used in production code. ([I1ac13](https://android-review.googlesource.com/#/q/I1ac13e43844a89d4fd9c3f59d8ce93fd3c8c45d2))
- Replace angle measurements for shape outline progress with curve length measurements, this allows more complex shapes to be used for morphing. ([I75478](https://android-review.googlesource.com/#/q/I75478ac712c29895c073aa7b5c29f1799192a9fd)) , [I390dd](https://android-review.googlesource.com/#/q/I390ddc7a26b83c10a60d8f75ea8a1d4b640e0e07)
- Improved the feature mapping algorithm, so more morphs should look more natural. ([I83287](https://android-review.googlesource.com/#/q/I83287a0bd2a470f8a38b67c77bd19a957c054046))

**API Changes**

- Add SVG path import and feature serializer. The usual flow is:
  - Use the new `SvgPathParser.parseFeatures()` to convert a svg path (the value of the `d` attribute on the `path` element of a svg) into a `List<Feature>`.
  - That can be modified, then serialized into a string with `FeatureSerializer.serialize()`.
  - The resulted string can be used in production code, importing it with `FeatureSerializer.parse()`
  - Note that the steps 1 \& 2 are done once, and can be done with the new app. Production code should only need to do step 3. ([I9bd00](https://android-review.googlesource.com/#/q/I9bd005781c68a241ce3af2eca4655cf6bb166613), [b/371196190](https://issuetracker.google.com/issues/371196190)), ([Ic3842](https://android-review.googlesource.com/#/q/Ic3842e71c464d42e8bd4295e16eff8c8f26c78ca)), ([If68ed](https://android-review.googlesource.com/#/q/If68edad7e838351be9e8e8be9e5977adb4f4f7e3)), ([I10251](https://android-review.googlesource.com/#/q/I1025182593d5a82dab88ddda067a55bf82b281fa))
- Expose polygon features and feature types. More generic `RoundedPolygons` can now be created with the base constructor that takes a `List<Features>`. Features are mainly a list of Cubic bezier curves, but they are tagged to help the Morph algorithm match between the start and end shapes (convex corners are mapped to convex corners and concave corners are mapped to concave corners). ([I61e76](https://android-review.googlesource.com/#/q/I61e769ebad7b07c35b4ce28221364d022ab34978)), ([I1fc5c](https://android-review.googlesource.com/#/q/I1fc5c5d42d41f1be5eb46b7d49fc3631a02144cf))
- Adds support for `watchosDeviceArm64` KMP target and target kotlin 1.9. ([Icf15d](https://android-review.googlesource.com/#/q/Icf15d056ce2380ca3c733fb1a93fd502f60b40e4), [b/364652024](https://issuetracker.google.com/issues/364652024))

**Bug Fixes**

- Fixed edge case when the last feature was empty. ([I390dd](https://android-review.googlesource.com/#/q/I390ddc7a26b83c10a60d8f75ea8a1d4))
- Make `RoundedPolygon` creation more robust. ([Ib862c](https://android-review.googlesource.com/#/q/Ib862c9c59537f28a2cd3ac469ce883734add1269), [b/360888486](https://issuetracker.google.com/issues/360888486))
- Fix a bug on `RoundedPolygon` initialization. ([I83ddb](https://android-review.googlesource.com/#/q/I83ddb2f481dc6cdbbe77f03f7b9ecd4be9462026))
- Fix an error in the algorithm to estimate the center of the polygon. ([Ida147](https://android-review.googlesource.com/#/q/Ida1477637391618c3437521f53809dd140e10c36))

## Graphics Shapes Version 1.0

### Version 1.0.1

September 4, 2024

`androidx.graphics:graphics-shapes:1.0.1`, `androidx.graphics:graphics-shapes-android:1.0.1`, and `androidx.graphics:graphics-shapes-desktop:1.0.1` are released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/217941670a79c16dcfa827977fc9ace001bbfe3a..594e7b6ae3c328df6be79b67ea06fd32ae2af648/graphics/graphics-shapes).

### Version 1.0.0

August 21, 2024

`androidx.graphics:graphics-shapes:1.0.0`, `androidx.graphics:graphics-shapes-android:1.0.0`, and `androidx.graphics:graphics-shapes-desktop:1.0.0` are released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/217941670a79c16dcfa827977fc9ace001bbfe3a..594e7b6ae3c328df6be79b67ea06fd32ae2af648/graphics/graphics-shapes).

### Version 1.0.0-rc01

July 24, 2024

`androidx.graphics:graphics-shapes:1.0.0-rc01`, `androidx.graphics:graphics-shapes-android:1.0.0-rc01`, and `androidx.graphics:graphics-shapes-desktop:1.0.0-rc01` are released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..217941670a79c16dcfa827977fc9ace001bbfe3a/graphics/graphics-shapes).

### Version 1.0.0-beta01

May 1, 2024

`androidx.graphics:graphics-shapes:1.0.0-beta01`, `androidx.graphics:graphics-shapes-android:1.0.0-beta01`, and `androidx.graphics:graphics-shapes-desktop:1.0.0-beta01` are released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..fbd1ac175922f44c69a13545d194066ee428b342/graphics/graphics-shapes).

**API Changes**

- Allow shapes to be pre-rotated to start at a different point. This change allows `pillStar` shapes to start their curves from a non-default point on the perimeter. This can be useful when animating the stroking of the shape's path, to start drawing from a specific location on the shape's outline. ([Ifbb4d](https://android-review.googlesource.com/#/q/Ifbb4dd34cfa414430829533613fda13b8916535e), [b/324303807](https://issuetracker.google.com/issues/324303807))
- Added `calculateBounds()` functions to Morph, which parallel the same functions on `RoundedPolygon`. ([I8a3b6](https://android-review.googlesource.com/#/q/I8a3b6c37807effcc3919d73266fc83a721fb2866), [b/325463575](https://issuetracker.google.com/issues/325463575))

### Version 1.0.0-alpha05

February 7, 2024

`androidx.graphics:graphics-shapes:1.0.0-alpha05`, `androidx.graphics:graphics-shapes-android:1.0.0-alpha05`, and `androidx.graphics:graphics-shapes-desktop:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..ca2a8cf8da3a3502fccc593974f8085653e38261/graphics/graphics-shapes)

**New Features**

- The library now offers new `pill()` and `pillStar()` functions for easy creation of these rounded/starred shapes. There are also new APIs for calculating the exact bounds required for a shape (the previous bounds were just an estimate based on the underlying Bezier curve anchor and control points), as well as the max possible bounds, which can be helpful to determine the size of the container holding it if it will be rotated within that container. ([I71827](https://android-review.googlesource.com/#/q/I71827916f76e5e2d10a0cce1def7440a2e2b8eca))

**API Changes**

- Now more options for retrieving exact and max bounds. ([I6d49f](https://android-review.googlesource.com/#/q/I6d49f468a28c1f360000e8370f02a50841f744e4), [b/317286450](https://issuetracker.google.com/issues/317286450))

**Bug Fixes**

- There were occasional rendering artifacts when drawing these shapes as stroked paths, due to a low-level rendering issue related to zero-length curves. This bug was fixed by eliminating all zero-length curves (which the shapes do not need, thus also saving on the overhead of the paths produced by the shapes).

### Version 1.0.0-alpha04

December 13, 2023

`androidx.graphics:graphics-shapes:1.0.0-alpha04`, `androidx.graphics:graphics-shapes-android:1.0.0-alpha04`, and `androidx.graphics:graphics-shapes-desktop:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a/graphics/graphics-shapes)

**New Features**

- This release contains several API changes, as well as bug fixes.
- Many of the API changes make the Shapes library KMP-friendly. This makes it easier to call from non-Android code (such as Android-agnostic Compose code). For example, there are no Android types in the API, such as the previous PointF, Matrix, and Path types.
- There were also several changes made to APIs and implementation for performance reasons, specifically to minimize object allocation (and collection). For example, the move from PointF to separate Float parameters avoids allocating many temporary PointF structures to hold those vertices.

**API Changes**

- Replaced `Morph.asMutableCubics` with a function to iterate over the `MutableCubics`. Changed `PointTransformer` functional interface, now it takes x and y coordinates of a `Point` and returns a `TransformedResult` (which is constructed with the transformed x \& y coordinates) ([I6719e](https://android-review.googlesource.com/#/q/I6719eabfd9b8a56befee35ac810747fda38bd7fd))
- Removed the public `Cubic` constructor and made it a factory function. ([I409ce](https://android-review.googlesource.com/#/q/I409ce4d6154b21e511d96b288a057b61e30d62e0))
- Adding Android-specific transform and drawing APIs ([I079f6](https://android-review.googlesource.com/#/q/I079f6f0cbfef6d4496bff858fb659be206d78988), [b/292289543](https://issuetracker.google.com/issues/292289543))
- Eliminate android dependencies ([Iadc1c](https://android-review.googlesource.com/#/q/Iadc1c32dfc40a3e88e4c8516c59b21e71366e019), [b/292289543](https://issuetracker.google.com/issues/292289543))
- Anchor and control property names are more sensible now ([If13bd](https://android-review.googlesource.com/#/q/If13bd96434d8d6871c7cd82f99558ab863ebf754), [b/294562941](https://issuetracker.google.com/issues/294562941))
- `PointF` parameters changed to `Float` pairs ([Id4705](https://android-review.googlesource.com/#/q/Id4705d27c7be31b26ade8186b99fffe2e2f8450e), [b/276466399](https://issuetracker.google.com/issues/276466399), [b/290254314](https://issuetracker.google.com/issues/290254314))
- `progress` is now passed to `Morph` drawing commands directly ([Icdca2](https://android-review.googlesource.com/#/q/Icdca2f2ced00bd7957fc5dc318298fd083a74586))

**Bug Fixes**

- Fixed bug when creating big shapes. ([I4fd66](https://android-review.googlesource.com/#/q/I4fd6696643cc3725425cf7b55536a1242fa896c6), [b/313497325](https://issuetracker.google.com/issues/313497325))

### Version 1.0.0-alpha03

June 7, 2023

`androidx.graphics:graphics-shapes:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..73f902dee011bfe400d8a0330bfd8d4bb632065f/graphics/graphics-shapes)

**API Changes**

- Added new `RoundedPolygon.rectangle()` function ([I78e7e](https://android-review.googlesource.com/#/q/I78e7ee609295c20680c5e6f1a3383421420674ff), [b/280322189](https://issuetracker.google.com/issues/280322189))
- Star and Circle functions are now decapitalized and called via `RoundedPolygon`'s companion object: e.g., `RoundedPolygon.star(...)`([I14735](https://android-review.googlesource.com/#/q/I14735f28dbb7092674bd621b2606183969fbf1e4))

**Bug Fixes**

- Fixed bug on smoothing ([Ibf894](https://android-review.googlesource.com/#/q/Ibf894671e193a041390a13069389649e53eff846))
- Fixed a bug that occured when start and end shape were the same. Better distribute available space on side for cuts, first using available space for rounding, then for smoothing if there is space left. ([Ibd320](https://android-review.googlesource.com/#/q/Ibd32074f9a01c17501f77e330e70346677ba1b41), [b/277936300](https://issuetracker.google.com/issues/277936300))

### Version 1.0.0-alpha02

April 19, 2023

`androidx.graphics:graphics-shapes:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/graphics/graphics-shapes)

**API Changes**

- The Polygon superclass was merged in with its subclass, `RoundedPolygon`; all polygons are now \[optionally\] rounded polygons.
- The Star function (which still returns a `RoundedPolygon`, as before) now takes an `innerRadius` value, instead of the previous `innerRadiusRatio` parameter. This is in the same units as the existing radius parameter, making things simpler and more consistent. Also, the `numOuterVertices` parameter was renamed to `numVerticesPerRadius` to clarify that the same number is applied to both inner and outer radii.
- `CornerRounding.radius` was previously documented to be relative to the size of the polygon, but it was (and should be) an absolute, not relative, value. The docs were updated and the annotation limiting it to a max value of 1.0 was fixed.

### Version 1.0.0-alpha01

April 5, 2023

Graphics-Shapes is a new library which allows easy creation and rendering of rounded polygonal shapes, as well as simple and automatic morphing (animation) between different shapes.

`androidx.graphics:graphics-shapes:1.0.0-alpha01` is released. This version was released from an internal branch.

**New Features**

- Use the Polygon API to create regular and star polygons with the desired number of vertices.
- Use optional `CornerRounding` parameters to specify the rounding radius and smoothing parameters for the corners, resulting in polygonal shapes with rounded corners.
- Use the new `Morph(Polygon, Polygon)` API to automatically calculate a "morph" shape whose progress can be set from 0 to 1 to animate between the starting and ending shapes. Animate that progress over time, drawing the result on every frame, to create a smooth animation between these new rounded shapes.

## Graphics Path Version 1.1

### Version 1.1.0-beta01

December 17, 2025

`androidx.graphics:graphics-path:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..7978b337b99d48895d0f93c8058c5ef4d46adacc/graphics/graphics-path).

## Graphics Path Version 1.0

### Version 1.1.0-alpha01

August 13, 2025

`androidx.graphics:graphics-path:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8a05a22af450d589ef911d772a001a49dcb05b71..c359e97fece91f3767a7d017e9def23c7caf1f53/graphics/graphics-path).

**Bug Fixes**

- Add implementation for conversion from conic to quadratic and use it on host platforms. [f059b1](https://android.googlesource.com/platform/frameworks/support/+/f059b1080eb84c623ac43156c5361b53020156de)

### Version 1.0.1

May 1, 2024

`androidx.graphics:graphics-path:1.0.1` is released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4fcd99eacd92d7c73fb1d3580fd423ed7704a98a..8a05a22af450d589ef911d772a001a49dcb05b71/graphics/graphics-path).

**Bug Fixes**

- Improvements to compiler flags.

### Version 1.0.0

March 6, 2024

`androidx.graphics:graphics-path:1.0.0` is released.

### Version 1.0.0-rc01

February 21, 2024

`androidx.graphics:graphics-path:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..56a7bc0fd3521a28152fb509a3a745ff5a67daab/graphics/graphics-path)

**Bug Fixes**

- Improve performance of PathIterator on API \< 34 ([Id4629](https://android-review.googlesource.com/#/q/Id46291003fc89095abaff8eb38f672cd26b8c6a4))

### Version 1.0.0-beta02

January 10, 2024

The changes in this release were all about reducing the size of the library, which was larger than necessary due to assumptions made by native code.

`androidx.graphics:graphics-path:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/graphics/graphics-path)

**Bug Fixes**

- Reduced the size of `libandroidx.graphics.path.so` by 96%. ([I71397](https://android-review.googlesource.com/#/q/I7139702def79ecfcf3d4dfe7d36f833230cf754b))
- Reduce the size of `libandroidx.graphics.path.so` by 5%. ([I2da7c](https://android-review.googlesource.com/#/q/I2da7ccea714765b87bba26a408a1056c9bd5f556))
- Shrunk the native components of `androidx.graphics:graphics-path` by 43%. ([I8e40d](https://android-review.googlesource.com/#/q/I8e40d0eefc449b5fed7eaebbdfeb05252947735d))

### Version 1.0.0-beta01

November 29, 2023

`androidx.graphics:graphics-path:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/graphics/graphics-path)

**API Changes**

- Removed usages of experimental `isAtLeastU()` API ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87), [b/289269026](https://issuetracker.google.com/issues/289269026))

**Bug Fixes**

- Various fixes and performance improvements, including how the library deals with conics.

### Version 1.0.0-alpha02

June 7, 2023

`androidx.graphics:graphics-path:1.0.0-alpha02` is released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- Fixed problem with internal platform version check which caused problems when running on Android 14 previews (the version check would fail, but the mechanism for doing things on previous releases doesn't work correctly on Android 14 in particular).

### Version 1.0.0-alpha01

March 22, 2023

`androidx.graphics:graphics-path:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6496ad7d8317d3707164ed29f268c7cddb565315/graphics/graphics-path)

**New Features**

- This new library allows querying of Path data via the new `PathIterator` API. Using this API, callers can iterate through all segments of a Path object to determine the operation and data for those segments.
- The library uses similar APIs introduced in Android 14 preview, but this AndroidX version of the API also works on versions back to API 21.

## Graphics Core Version 1.0

### Version 1.0.4

December 03, 2025

`androidx.graphics:graphics-core:1.0.4` is released. Version 1.0.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cb163bee53214245ad7a23367396a21b7f85ae82..7620069dd1c615be201490afe981639f04cec40f/graphics/graphics-core).

**Bug Fixes**

- Improve compatibility and performance for particular devices.

### Version 1.0.3

March 26, 2025

`androidx.graphics:graphics-core:1.0.3` is released. Version 1.0.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2be6c2f793ca8a526dc525e98e4afb9db3ab9c05..e4b672d6ee0029b3ab664d3c70b7f97b01376f8b/graphics/graphics-core).

**Bug Fixes**

- Fix for full-screen flickers while drawing on certain devices with API\<33.

### Version 1.0.2

October 16, 2024

`androidx.graphics:graphics-core:1.0.2` is released. Version 1.0.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad866fa50e6d6a7a6ee907b38ebec8b8cb3c476f..2be6c2f793ca8a526dc525e98e4afb9db3ab9c05/graphics/graphics-core).

**Bug Fixes**

- Fixed issue where `SurfaceControl` instances would still be managed by the system compositor even after they were released.
- Fixed issue where the currently presented `HardwareBuffer` instance would not be released after low latency dependencies were disposed
- Fixed flickering issue on certain Android 14+ devices that did not support the front buffer usage flag

### Version 1.0.1

September 4, 2024

`androidx.graphics:graphics-core:1.0.1` is released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/df2afa3c4e8c0c1cf2095ea9057dd59df17de4ca..ad866fa50e6d6a7a6ee907b38ebec8b8cb3c476f/graphics/graphics-core).

**Bug Fixes**

- Fixed issue where memory resources would occasionally not be released.

### Version 1.0.0

May 29, 2024

`androidx.graphics:graphics-core:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc8da84ada72223ae5bca7d13fccc8c9c9242f19..df2afa3c4e8c0c1cf2095ea9057dd59df17de4ca/graphics/graphics-core).

**Major features of 1.0.0**

- Official stable release of the graphics-core library. Includes minor bug fixes and performance improvements from 1.0.0-rc01

### Version 1.0.0-rc01

April 17, 2024

`androidx.graphics:graphics-core:1.0.0-rc01` is released. This version is developed in an internal branch.

**Bug Fixes**

- Fixed issue leading to potential double closure of file descriptors with the `CanvasBufferedRendererAPI` with certain Android devices running Android 14.
- Fixed issue where `FrameBuffer` would not properly delete framebuffer instances.

### Version 1.0.0-beta01

December 13, 2023

`androidx.graphics:graphics-core:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/graphics/graphics-core)

**New Features**

- Introduced a new `LowLatencyCanvasView` API to support low latency rendering with Android's 2d graphics APIs (Canvas + Paint) within the View hierarchy.
- Introduced `CanvasBufferedRenderer` API to support hardware accelerated Canvas rendering to a `HardwareBuffer`. This can be used to draw a portion of a user interface into a buffer that can be converted to a Bitmap using the `Bitmap.wrapHardwareBuffer` API.

**API Changes**

- Updated `CanvasBufferRenderer#releaseBuffer` API to have an optional fence parameter. Updated documentation to describe when `RenderResult#fence` is returned. ([If1ea7](https://android-review.googlesource.com/#/q/If1ea7aea45c9770725ba8d33c24f1bf30e4a2cc8))
- Add `draw` method to `RenderRequest` to support leveraging coroutines to schedule draw requests. Renamed the previous draw method that consumed an executor to `drawAsync`. Refactored `isClosed()` method to a property. ([I5bff6](https://android-review.googlesource.com/#/q/I5bff6e5cfb2591600258d9dcd2cee49c7a5d114b))
- Exposed buffer format parameter to `CanvasFrontBufferRenderer` to map directly to `CanvasBufferedRenderer.Builder#setBufferFormat` ([I0f272](https://android-review.googlesource.com/#/q/I0f2729fcf92515273855b261dc81ee1fdfde08ef))
- Created `CanvasBufferedRenderer` API to handle hardware accelerated canvas rendering into a `HardwareBuffer`. This provides a backported implementation to Android Q alongside configuration of a swapchain depth of `HardwareBuffers`. `ColorSpace` configuration is still limited to Android U+ however the compat implementation provides no-op behavior on the developers' behalf. ([I9b1d8](https://android-review.googlesource.com/#/q/I9b1d889595b72e32418344e298a0017394fdc6e6))
- Add `setFrameRate`/`clearFrameRate` APIs to `SurfaceControlCompat.Transaction` in order to control the frame rate alongside the change strategy for seamless or default transitions. ([I6045c](https://android-review.googlesource.com/#/q/I6045cfe9bba4247fe93f7eb6cdc67e61d65dbf29))
- Lowered required API level for `setDataSpace` to Android Q from Android T. ([I59c34](https://android-review.googlesource.com/#/q/I59c347a7a669819b1df48ed2758ad0d0e9248979))
- Added `onBufferReleased` callback to `GLFrameBufferRenderer` API to give consumers the opportunity to clean up state when a buffer is no longer being presented ([I8a4e2](https://android-review.googlesource.com/#/q/I8a4e238a07ec32e39e2d67fb7f7093dcdb9752f4))
- Create `LowLatencyCanvasView` to support a simple use case of rendering content with low latency that gets synchronized with the View hierarchy rendering. This mitigates the complexities associated with `SurfaceView` management by internally managing the `SurfaceView` instance that gets translated off/on screen for synchronized and low latency rendering respectively. ([I9253b](https://android-review.googlesource.com/#/q/I9253bd3e42cfd24e5396a9d1117868cfd91d1909))
- Added colorspace configuration support to `CanvasFrontBufferedRenderer` API. Updated multibuffered callbacks to also include the back buffered `SurfaceControl` ([I24bd9](https://android-review.googlesource.com/#/q/I24bd949fd100317663346bf12c866a358011f38c))

### Version 1.0.0-alpha05

September 6, 2023

`androidx.graphics:graphics-core:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/graphics/graphics-core)

**New Features**

- Introduced `GLFrameBufferRenderer` API. This provides a combination of OpenGL dependencies, swap chain configuration, pixel formats and `SurfaceControl` configuration. ([Ic775b](https://android-review.googlesource.com/#/q/Ic775b67c56fde503a03db18f42b5d80cdf7e05c7))

**API Changes**

- Added width + height parameters to various callback APIs to pipe dimensions from `SurfaceHolder#Callbacks`. ([I7f9fc](https://android-review.googlesource.com/#/q/I7f9fca1eb4948ed5a077d95a567138d8ad568e93))
- Added clear API to clear both front and multi buffered layers. ([Ic1f95](https://android-review.googlesource.com/#/q/Ic1f9501ce59095c9071f7cc842319cd970d52ab3))
- Added support to configure the underlying buffer type of swapchains used within `GLFrontBufferedRenderer`. ([I07a13](https://android-review.googlesource.com/#/q/I07a134963fe1b6b8b43a80ed3e118716ae2f3efc))
- Added kotlin properties for getters on `GLFrameBufferRenderer`, `IntRange` annotation for max buffer entries, and `HardwareBufferFormart` and `HardwareBufferUsage` annotations for `setFormat`/`setUsage` respectively. ([Ief89e](https://android-review.googlesource.com/#/q/Ief89ede0678fcd7732ccfd726743c348bc3c4195))
- Updated `setBuffer` API on `SurfaceControl` transactions to provide a release fence. ([Ice1bb](https://android-review.googlesource.com/#/q/Ice1bb2399bf9801d7790382e180b2ea12a00a95f))
- Added `SurfaceControlCompat.Transaction` APIs to configure the data space as well as set the extended brightness range. ([Ic378d](https://android-review.googlesource.com/#/q/Ic378dc22438a7a7d63a8b11c716a0012ebca7232))

### Version 1.0.0-alpha04

June 7, 2023

`androidx.graphics:graphics-core:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..73f902dee011bfe400d8a0330bfd8d4bb632065f/graphics/graphics-core)

**New Features**

- Introduced `CanvasFrontBufferedRenderer` to support low latency graphics leveraging the `android.graphics.Canvas` API alongside the existing OpenGL implementation

**API Changes**

- Updated `SurfaceControlCompat.Transaction#setBuffer` API to allow for nullable `HardwareBuffer` instances to mirror the corresponding platform API ([I173d7](https://android-review.googlesource.com/#/q/I173d7f95eeafa68e5d5166f92314ca40b4e06b4b))
- Rename methods referring to Double Buffered rendering to Multi Buffered instead as the backing swapchain may contain more than 2 buffers. ([I830d7](https://android-review.googlesource.com/#/q/I830d7148fd1a85c9ba375a93d3efc1edbc926ee1))
- Create `CanvasFrontBufferedRenderer` API to enable 3ps to leverage a front buffered rendering system using the Canvas API. ([Ibfc29](https://android-review.googlesource.com/#/q/Ibfc29911acb314b12611687012983031c9dd7165))

**Bug Fixes**

- Fixed issue where `GLFrontBufferedRenderer` would not render content after resuming the corresponding Activity.
- Fixed issue where front buffered content would be cleared prematurely.
- Fixed issue where `SurfaceHolder.Callbacks` would not be removed after low latency graphics APIs were released.

### Version 1.0.0-alpha03

March 22, 2023

`androidx.graphics:graphics-core:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3ab6276ada43455a1f1cd3e8d0b3c77123b42150..5e7d256f82fbafb6d059ab7b18fddd87c7531553/graphics/graphics-core)

**API Changes**

- Updated `GLFrontBufferedRenderer` callback implementation to provide `BufferInfo` object that contains buffer width/height along with a frame buffer identifier that can be used to re-target the original destination after rendering to an intermediate scratch buffer. ([I7fe20](https://android-review.googlesource.com/#/q/I7fe20bf29d5321ef00e5bb7fce6a60cab09b7633))
- Consolidated `SyncFence` creation to static factory method on `SyncFenceCompat`.
- Removed public compatibility method for `eglDupNativeFenceFDANDROID` in favor of `SyncFenceCompat` factory method for SyncFence creation. This is to ensure all API surfaces receive the correct `SyncFence` implementation regardless of API level. ([I849bb](https://android-review.googlesource.com/#/q/I849bb702ab07ff3e3f154d80ca950e198a362981))
- Added documentation for `FrameBufferRenderer` and `SyncStrategy`.
  - Moved `FrameBufferRenderer` + `FrameBuffer` + `FrameBufferPool` to `androidx.graphics.opengl` package
  - Moved `SyncStrategy` to `androidx.graphics.opengl` package
  - Updated `RenderCallback#onDraw` docs
  - Updated documentation of `RenderCallback#obtainFrameBuffer` that implementor of API is responsible for calling `FrameBuffer.close`
  - Updated `onDrawComplete` to indicate consumers are responsible for dispatching contents to display
  - Moved `SyncFence` compatibility interfaces/classes to `androidx.hardware` package to mirror the framework
  - Renamed `SyncFence` API to `SyncFenceV19` and made private to consolidate usages to `SyncFenceCompat` which leverages the framework's `SyncFence` API wherever possible. ([I5149c](https://android-review.googlesource.com/#/q/I5149cdaed6c12822c898dde02ca3d1f12cb64d45))
- Added `GLFrontBufferedRenderer#cancel` and `GLFrontBufferedRenderer#execute` methods. The former is useful in palm rejection scenarios where rendering to the front buffer should be cancelled and hide the front buffer. The latter is useful in scenarios to manipulate objects on the GL thread without having to schedule a render. ([If0b7f](https://android-review.googlesource.com/#/q/If0b7f1674765f18ed0af9474a35567b16232858c))
- Add API to render directly to the double buffered layer. This assists with re-rendering a scene after resume as well as giving an opportunity to consumers to selectively determine when to leverage front buffered rendering dynamically based on the desired scene to render. ([Ied56c](https://android-review.googlesource.com/#/q/Ied56c2e057ef00b756d05a8b5f588a2341cd59f1))
- Added new API to `SurfaceControlCompat.Builder` to support configuring the parent `SurfaceControl` from another `SurfaceControl` instance in addition to the existing mechanism from a `SurfaceView`. ([I1d1b6](https://android-review.googlesource.com/#/q/I1d1b654352d2dd6964da3e75007cd6f346092ab5))
- More return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Added `EGL_ANDROID_get_native_client_buffer` extension constant to query whether the Android device supports importing of `HardwareBuffer` instances into `EGLClientBuffer` objects that can be consumed as an `EGLImage` instance. ([Iad767](https://android-review.googlesource.com/#/q/Iad767d0af10b10b2ce6b9d3c4bcced4345d0d5be))
- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.0.0-alpha02

November 9, 2022

`androidx.graphics:graphics-core:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..3ab6276ada43455a1f1cd3e8d0b3c77123b42150/graphics/graphics-core)

**API Changes**

- Fixed missing `RequiresApi` annotation for `addTransactionCommitListener` which was introduced in Android S ([I0a035](https://android-review.googlesource.com/#/q/I0a0358dd907c313ba0aa5d284fb360df5fa40d31))
- Updated `onDraw<Front/Double>` Buffer callbacks to provide a transform matrix that consumers can pass to their vertex shaders in addition to the current buffer width/height. Consumers are responsible for using these parameters to properly pre-rotate their OpenGL rendering code. ([I82f9e](https://android-review.googlesource.com/#/q/I82f9e11601c4626696cef9c10fd65a18657b76a5))

**Bug Fixes**

- Improved graphics latency by pre-rotating buffers before issuing `SurfaceControl` transactions.
- Fixed issue where error logs would show error 300d (EGL_BAD_SURFACE).
- Fixed issue where `GLFrontBufferedRenderer` would be invalid after the corresponding Activity it was used within was resumed.
- Increased support for emulators and ChromeOS devices.
- Fixed issue where the front buffered layer maybe hidden prematurely.

### Version 1.0.0-alpha01

October 24, 2022

`androidx.graphics:graphics-core:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b/graphics/graphics-core)

**New Features**

- Initial release of the graphics core AndroidX library. This includes APIs to support low latency use cases such as stylus input. This also introduces some helper APIs for OpenGL usage.

**API Changes**

- Introduces `GLFrontBufferedRenderer` to assist in front and multi-buffered rendering to achieve both low latency and high quality rendering output.
- Introduces `GLRenderer` API to assist in OpenGL rendering for various Surface providers such as `SurfaceView`, `TextureView` and others.