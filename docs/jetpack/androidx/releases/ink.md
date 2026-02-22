---
title: https://developer.android.com/jetpack/androidx/releases/ink
url: https://developer.android.com/jetpack/androidx/releases/ink
source: md.txt
---

# ink

API Reference  
[androidx.ink.authoring](https://developer.android.com/reference/kotlin/androidx/ink/authoring/package-summary)  
[androidx.ink.authoring.compose](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary)  
[androidx.ink.brush](https://developer.android.com/reference/kotlin/androidx/ink/brush/package-summary)  
[androidx.ink.brush.compose](https://developer.android.com/reference/kotlin/androidx/ink/brush/compose/package-summary)  
[androidx.ink.geometry](https://developer.android.com/reference/kotlin/androidx/ink/geometry/package-summary)  
[androidx.ink.geometry.compose](https://developer.android.com/reference/kotlin/androidx/ink/geometry/compose/package-summary)  
[androidx.ink.rendering.android.canvas](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/package-summary)  
[androidx.ink.rendering.android.view](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/view/package-summary)  
[androidx.ink.storage](https://developer.android.com/reference/kotlin/androidx/ink/storage/package-summary)  
[androidx.ink.strokes](https://developer.android.com/reference/kotlin/androidx/ink/strokes/package-summary)  
Inspire best-in-class pen apps. Lower the developer barrier to entry for high performance, beautiful inking experiences.  

|  Latest Update   | Stable Release |                                  Release Candidate                                   | Beta Release | Alpha Release |
|------------------|----------------|--------------------------------------------------------------------------------------|--------------|---------------|
| December 3, 2025 | -              | [1.0.0-rc01](https://developer.android.com/jetpack/androidx/releases/ink#1.0.0-rc01) | -            | -             |

## Declaring dependencies

To add a dependency on Ink, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
  
    implementation "androidx.ink:ink-authoring:1.0.0-rc01"
    implementation "androidx.ink:ink-authoring-compose:1.0.0-rc01"
    implementation "androidx.ink:ink-brush:1.0.0-rc01"
    implementation "androidx.ink:ink-brush-compose:1.0.0-rc01"
    implementation "androidx.ink:ink-geometry:1.0.0-rc01"
    implementation "androidx.ink:ink-geometry-compose:1.0.0-rc01"
    implementation "androidx.ink:ink-nativeloader:1.0.0-rc01"
    implementation "androidx.ink:ink-rendering:1.0.0-rc01"
    implementation "androidx.ink:ink-storage:1.0.0-rc01"
    implementation "androidx.ink:ink-strokes:1.0.0-rc01"
    
}
```

### Kotlin

```kotlin
dependencies {


    implementation("androidx.ink:ink-authoring:1.0.0-rc01")
    implementation("androidx.ink:ink-authoring-compose:1.0.0-rc01")
    implementation("androidx.ink:ink-brush:1.0.0-rc01")
    implementation("androidx.ink:ink-brush-compose:1.0.0-rc01")
    implementation("androidx.ink:ink-geometry:1.0.0-rc01")
    implementation("androidx.ink:ink-geometry-compose:1.0.0-rc01")
    implementation("androidx.ink:ink-nativeloader:1.0.0-rc01")
    implementation("androidx.ink:ink-rendering:1.0.0-rc01")
    implementation("androidx.ink:ink-storage:1.0.0-rc01")
    implementation("androidx.ink:ink-strokes:1.0.0-rc01")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1662443+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1662443&template=2055047)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-rc01

December 03, 2025

`androidx.ink:ink-*:1.0.0-rc01`is released. Version 1.0.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4d752a0684fb1bf991cd0d15ebd3649ee8684ca1..7a31b848f1d509fe53e220229333c573be219d10/ink).

**Bug Fixes**

- Update dependency version. ([Iecd04](https://android-review.googlesource.com/#/q/Iecd04ee1ecca5aa981c756e246e11535455a898c))

### Version 1.0.0-beta02

November 19, 2025

`androidx.ink:ink-*:1.0.0-beta02`is released. Version 1.0.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/ink).

**API Changes**

- Experimental custom low latency shape APIs, assorted bug fixes ([Ib8d2f](https://android-review.googlesource.com/#/q/Ib8d2fe54389b3a2a9f5d305343878dd766d02527))

**Bug Fixes**

- Improve floating point precision on`StrokeInputBatch`serialization, fixing a drift in the values from repeated encoding and decoding
- More robust system input sanitization.
- Fix brush texture support in`InProgressStrokes`composable

### Version 1.0.0-beta01

October 22, 2025

`androidx.ink:ink-*:1.0.0-beta01`is released. Version 1.0.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/ink).

**Bug Fixes**

- Bug fixes in preparation for beta01 release ([I9900e](https://android-review.googlesource.com/#/q/I9900e364054c1873f97e1e60193e92cf01d4c9ab))
- Reduce rendering artifacts in strokes due to too many modeled inputs too close to each other.
- Fix a rare crash in input modeling.

### Version 1.0.0-alpha07

October 08, 2025

`androidx.ink:ink-*:1.0.0-alpha07`is released. Version 1.0.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..4350deab5806bf95370a4d012d7eeaa70a10be44/ink).

**New Features**

- `SelfOverlap`parameter for`StockBrushes``highlighter`and`emojiHighlighter`, which replaces`InProgressStrokesView``rendererFactory`
- Improved implementation of stroke input smoothing, which eliminates device measurement noise but which more accurately reflects user input than the previous stroke input smoothing implementation
- Improved consistency with other Android/Jetpack APIs for angle units (degrees vs. radians), transforms (skew vs. shear), and more

**API Changes**

- Change angle-related API to use degrees and include unit in names, be clear about units in Angle conversion utilities and support both degrees and radians, change`StockBrushes`API to take stock brush version as a factory function parameter and expose self-overlap behavior control for highlighter brushes, rename`MutableAffineTransform.populateFromTranslate`to`populateFromTranslation`, remove`InProgressStrokesView.setRenderFactory/getRenderFactory`. ([Id9eab](https://android-review.googlesource.com/#/q/Id9eab6301d2ca1803452cd8a1eb2dcf0a3cd357d),[b/436656418](https://issuetracker.google.com/issues/436656418))
- Rename shear to skew, clarify some documentation, remove`CanvasStrokeRenderer.strokeModifiedRegionOutsetPx`, add`InProgressStroke.changesWithTime`([Ia5e70](https://android-review.googlesource.com/#/q/Ia5e70048d15787a54bf4c848b715484366e5c629),[b/436656418](https://issuetracker.google.com/issues/436656418))

**Bug Fixes**

- Improve input modeling to make strokes more accurately reflect input. ([I93097](https://android-review.googlesource.com/#/q/I9309760022de0c30a0bc5e960da4c2467f663e9f))

### Version 1.0.0-alpha06

August 13, 2025

`androidx.ink:ink-*:1.0.0-alpha06`is released. Version 1.0.0-alpha06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..c359e97fece91f3767a7d017e9def23c7caf1f53/ink).

**New Features**

- Emoji highlighter stock brush: Highlight parts of a document with any emoji you choose, to add a fun flair and help stay organized.
- More helper APIs for geometry module primitive shapes
- Improve device compatibility and performance

**API Changes**

- Simplified API for`InProgressStrokesView`, finish geometry APIs, emoji highlighter, remove factory functions from`MutableParallelogram`in favor of populate methods, support seed for randomized brush behaviors. ([I38280](https://android-review.googlesource.com/#/q/I38280146fca9a55b06d87a835670efdd012990e7))

**Bug Fixes**

- Fix a performance issue and a wet/dry color consistency issue. ([Ifcd1d](https://android-review.googlesource.com/#/q/Ifcd1da4081a01ba8165b4e8624219b1bd26bd248))

### Version 1.0.0-alpha05

June 18, 2025

`androidx.ink:ink-*:1.0.0-alpha05`is released. Version 1.0.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/ink).

**New Features**

- Compose interoperability modules for authoring, brush, and geometry modules

**API Changes**

- New Compose interoperability modules and APIs, API cleanup ([I0e464](https://android-review.googlesource.com/#/q/I0e4641822d568573fc8c7b3955a007a8ac9cd1c5))
- `InProgressStroke.enqueueInputs/updateShape`methods which returned`kotlin.Result`are removed, clients should use e.g.`enqueueInputsOrThrow`or`enqueueInputsOrIgnore`instead.`InProgressStroke.getNeedsUpdate`is renamed to`isUpdateNeeded`.`InProgressStroke.populateOutlinePosition`now returns its output parameter to allow call chaining, consistent with other methods in Ink. The`TextureBitmapStore`interface is moved from the rendering module to the brush module.`BoxAccumulator.populateFrom`is made to take a nullable immutable Box instead of a mutable`BoxAccumulator`, to make it clearer what is mutated, callers should change`boxAccumulator.add(other)`to`boxAccumulator.add(other.box)`.`BrushUtil.toBuilderWithAndroidColor/createBuilderWithAndroidColor`are removed, use the`setAndroidColor`of`Brush.Builder`after constructing instead. ([Ia7155](https://android-review.googlesource.com/#/q/Ia7155560602b8319183aa12671d7f1d925873448))
- Previously experimental property`InProgressStrokesView.textureBitmapStore`is now private. There are still public accessors for this property. ([I1d706](https://android-review.googlesource.com/#/q/I1d7064ff25c953066a4b43a6c30a4b3aa0b145d5))

**Bug Fixes**

- Improved performance for custom brushes containing many particles.

### Version 1.0.0-alpha04

April 9, 2025

`androidx.ink:ink-*:1.0.0-alpha04`is released. Version 1.0.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..4c37298a97c16270c139eb812ddadaba03e23a52/ink).

**New Features**

- Introduces new experimental APIs for custom`BrushFamily`objects, enabling new brushes like Pencil and Laser Pointer. The API allows for loading brushes defined by this proto. ([I8809a](https://android-review.googlesource.com/#/q/I8809a675a5527c1a7bc2f519e041a8af1ed693b3))

### Version 1.0.0-alpha03

February 12, 2025

`androidx.ink:ink-*:1.0.0-alpha03`is released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/ink).

**New Features**

- Disk and network size savings: Serialization of`StrokeInputBatch`, saving many lines of code, with the resulting objects a tiny fraction of the size of traditionally stored strokes. ([Ie898d](https://android-review.googlesource.com/#/q/Ie898d91e3c77eccbf26e9ee6d7f384a3a57b974f))
- Lasso selection: dashed line brush to draw a selection stroke, and a function to turn the selection stroke into a`PartitionedMesh`for geometry queries. ([Ia38a0](https://android-review.googlesource.com/#/q/Ia38a0e3e7a2da344d978bdfd5b8db8210a753e74))

### Version 1.0.0-alpha02

December 11, 2024

`androidx.ink:ink-*:1.0.0-alpha02`is released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..46295bc0b75a16f452e8e0090e8de41073d4dbb6/ink).

**API Changes**

- Assorted bug fixes. ([I05dd8](https://android-review.googlesource.com/#/q/I05dd84cb83c29b6f8af876164c426fee57f6f932))

**External Contribution**

- Deprecate`BuildCompat.isAtLeastV`. Callers should check SDK_INT against 35 directly instead. ([I294d1](https://android-review.googlesource.com/#/q/I294d117a8fea924e7f1b739d52268a9a54be6db7))

### Version 1.0.0-alpha01

October 2, 2024

`androidx.ink:ink-*:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/ink).

**New Features**

- A modular and configurable library to make it easy to create, render, and manipulate beautiful ink strokes authored in your application.

**API Changes**

New modules to help developers build rich inking experiences:

- Authoring: Use`InProgressStrokesView`for high-performance, low latency rendering of strokes in real time as inputs are received.
- Rendering: Use`CanvasStrokeRenderer`and`ViewStrokeRenderer`to draw the finished ink strokes as part of an app's user interface.
- Strokes: Core data types used for inking features.
- Brush: Configurable specification of how strokes will look and act in response to user input.
- Geometry: Geometric operations like intersection and coverage to power tools like selection and erasing.