---
title: https://developer.android.com/jetpack/androidx/releases/text-vertical
url: https://developer.android.com/jetpack/androidx/releases/text-vertical
source: md.txt
---

# text-vertical

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 29, 2026 | - | - | - | [1.0.0-alpha06](https://developer.android.com/jetpack/androidx/releases/text-vertical#1.0.0-alpha06) |

## Declaring dependencies

To add a dependency on Text, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.text:text-vertical:1.0.0-alpha06"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.text:text-vertical:1.0.0-alpha06")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1909646+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1909646&template=2203168)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Text-Vertical

### Version 1.0

#### Version 1.0.0-alpha06

July 29, 2026

`androidx.text:text-vertical:1.0.0-alpha06` and `androidx.text:text-vertical-compose:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/df4b49eda6f6834b6bc4c8aa30a581fa577a511e..61ee8cd421d0c0252d8db0253b739de537999371/text).

**Important Changes**

- This release marks the final planned alpha version of the library.
- Finalized and refined the parameters in the `VerticalText` composable

**API Changes**

- Introduced `VerticalTextStyle` for vertical text layout. ([I647a8](https://android-review.googlesource.com/#/q/I647a8f1f681b019f2a306575f9a83a73fd4602e3), [b/512424512](https://issuetracker.google.com/issues/512424512))
- Introduced a new public DSL (`VerticalTextScope` and `buildVerticalText`) in the `text-vertical-compose` library ([I6faa7](https://android-review.googlesource.com/#/q/I6faa75247b091a6bbc6e7f209e0c467e7a39b073), [b/502088091](https://issuetracker.google.com/issues/502088091))
- Introduce `VerticalText` composable ([I96509](https://android-review.googlesource.com/#/q/I96509c991366dfbd411b8125ba550753abda83fe), [b/502088091](https://issuetracker.google.com/issues/502088091))

**Bug Fixes**

- Clarified documentation for `VerticalTextLayout` fallback behavior on older API levels. ([Ia7ccc](https://android-review.googlesource.com/#/q/Ia7ccc156c5c1d1a8b69c106b331b8f1f7a89a304), [b/449184326](https://issuetracker.google.com/issues/449184326))

There are no release notes for this artifact.

## Text Vertical Version 1.0

### Version 1.0.0-alpha05

April 22, 2026

`androidx.text:text-vertical:1.0.0-alpha05` and `androidx.text:text-vertical-compose:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/951845221205b7a428a9d779107760fc929863ee..df4b49eda6f6834b6bc4c8aa30a581fa577a511e/text).

**New Features**

- Added Composable functions to support vertical text layout, aligning with Google's Compose-first initiative.

**API Changes**

- Introduced `:text:text-vertical-compose` library artifact. ([I939e4](https://android-review.googlesource.com/#/q/I939e4862996f64c79975568aa3249016ccda19ab))
- Added `lineCount` property to `VerticalTextLayout` class. ([I93884](https://android-review.googlesource.com/#/q/I93884649fdcbc7be076446b5fe7d75e15f58b84d), [b/502088091](https://issuetracker.google.com/issues/502088091))

**Bug Fixes**

- Updated KDoc documentation for clarity and accuracy. ([I71c8f](https://android-review.googlesource.com/#/q/I71c8ffd6d4b2987bb7abc1a090133501d25a766c), [b/449184326](https://issuetracker.google.com/issues/449184326))

### Version 1.0.0-alpha04

April 08, 2026

`androidx.text:text-vertical:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f1927c2c3b66d0c3a6b9118974d818d2dc5a06a..966cd4961ea7030c43c4afe234f0c8a4472f8160/text/text-vertical).

**New Features**

- Refactored all public classes to provide more convenient, idiomatic Kotlin APIs for general usage, while maintaining strong Java interoperability.

**API Changes**

- Added a default zero-argument constructor to `FontShearSpan` for Java compatibility ([I73065](https://android-review.googlesource.com/#/q/I730658f1c6d29b291b6a9493e3ccc40f0ada4764), [b/493692287](https://issuetracker.google.com/issues/493692287)).
- Removed the `Parcelable` implementation in `RubySpan` and `EmphasisSpan` ([I49884](https://android-review.googlesource.com/#/q/I49884b2585ece811bb85a86d7b100c68d10f116d), [b/493693386](https://issuetracker.google.com/issues/493693386)).
- Refactored `EmphasisSpan` for better compatibility ([I34c40](https://android-review.googlesource.com/#/q/I34c40e89606a520b3a6a8d3d3f5c4cc531da6fc5), [b/493693310](https://issuetracker.google.com/issues/493693310)).
- Refactored `AnnotationPosition` to improve API surface ([I10dce](https://android-review.googlesource.com/#/q/I10dce948b769873d68c64077b4d96997cc2fa37e), [b/493693386](https://issuetracker.google.com/issues/493693386)).
- Converted `TextOrientation` to an enum class, refactored `AnnotationPosition` to a sealed class, and removed `RubySpan.Builder` ([Ib4a77](https://android-review.googlesource.com/#/q/Ib4a77651cdd2f3c7aa320ba6ef6d51c7965b7283), [b/493693386](https://issuetracker.google.com/issues/493693386)).
- Added the `AnnotationPosition` enum and refactored the `RubySpan` class ([Ibfcff](https://android-review.googlesource.com/#/q/Ibfcff6f417bbb5bdf79998fa7876e5cec79bb93a), [b/493692426](https://issuetracker.google.com/issues/493692426)).
- Refactored `TextOrientation` for general usage and improved internal text scaling extensions ([I82152](https://android-review.googlesource.com/#/q/I821529f1e8457a5541a66e55907ea04aa88104c9), [b/493692428](https://issuetracker.google.com/issues/493692428)).

### Version 1.0.0-alpha03

March 25, 2026

`androidx.text:text-vertical:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..1abcb4178d48853948b9b566cabff9222d90ab69/text/text-vertical).

**New Features**

- `VerticalTextLayout` now supports the horizontal layout, to display special spans in Japanese such as Ruby and Emphasis (Boten).

**API Changes**

- `RubySpan` and `EmphasisSpan` now inherit ReplacementSpan for supporting them for horizontal text ([I38db6](https://android-review.googlesource.com/#/q/I38db6f5fd0676dc0fdf0433dd81e53fe3c7fc981), [b/447239659](https://issuetracker.google.com/issues/447239659), [b/447224892](https://issuetracker.google.com/issues/447224892))

### Version 1.0.0-alpha02

October 08, 2025

`androidx.text:text-vertical:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..4350deab5806bf95370a4d012d7eeaa70a10be44/text/text-vertical).

**New Features**

- Added `VerticalTextLayout#isVerticalTextLayoutSupported()` method to check capability of vertical text ([Ie2802](https://android-review.googlesource.com/#/q/Ie2802d542557658d06c3d90b5dc10d0f8677aad7), [b/442608654](https://issuetracker.google.com/issues/442608654))

**API Changes**

- Introduced a graceful fallback in API \< 36.([I8a67a](https://android-review.googlesource.com/#/q/I8a67aa87031b6e322fb9fd1671090f873ba5d760), [b/442608654](https://issuetracker.google.com/issues/442608654))
- Downgrade `minSDK` to 23 to be used in other AndroidX libraries ([I2d6b5](https://android-review.googlesource.com/#/q/I2d6b55e7148e919f16d810712893a567a36ce9d7), [b/442608654](https://issuetracker.google.com/issues/442608654))

### Version 1.0.0-alpha01

August 27, 2025

`androidx.text:text-vertical:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681/text/text-vertical).

**New Features**

- A new vertical text library to support vertical text layout mainly for Japanese, by leveraging the new [VERTICAL_TEXT_FLAG](https://developer.android.com/reference/android/graphics/Paint#VERTICAL_TEXT_FLAG) flag added in Android 16.
- Added `VerticalTextLayout` that displayed vertical text with proper line breaks, mixed orientation (e.g., horizontal Latin characters within a vertical line), and ruby text. ([8b3a10](https://android.googlesource.com/platform/frameworks/support/+/8b3a10cb8bc1ad17da5da6bb1386499453a4899e))
- Added `FontShearSpan` for italic-like style in vertical text. ([1ffd78](https://android.googlesource.com/platform/frameworks/support/+/1ffd782e24d6143a899c18c1599a95cab0d6cf64))
- Added `EmphasisRun` for emphasis marks. ([fe12d9](https://android.googlesource.com/platform/frameworks/support/+/fe12d9efff8394cfed4717324fe5dc648dc1e927))