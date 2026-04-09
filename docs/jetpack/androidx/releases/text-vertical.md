---
title: text-vertical  |  Jetpack  |  Android Developers
url: https://developer.android.com/jetpack/androidx/releases/text-vertical
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Get started](https://developer.android.com/get-started/overview)
* [Jetpack](https://developer.android.com/jetpack)
* [Libraries](https://developer.android.com/jetpack/androidx/explorer)

Stay organized with collections

Save and categorize content based on your preferences.



# text-vertical

API Reference  
[androidx.text-vertical](/reference/kotlin/androidx/text/package-summary)

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
| --- | --- | --- | --- | --- |
| April 08, 2026 | - | - | - | [1.0.0-alpha04](/jetpack/androidx/releases/text-vertical#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on Text, you must add the Google Maven repository to your
project. Read [Google's Maven repository](/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```
dependencies {
    implementation "androidx.text:text-vertical:1.0.0-alpha04"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.text:text-vertical:1.0.0-alpha04")
}
```

For more information about dependencies, see [Add build dependencies](/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1909646%20status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1909646&template=2203168)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Text Vertical Version 1.0

### Version 1.0.0-alpha04

April 08, 2026

`androidx.text:text-vertical:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f1927c2c3b66d0c3a6b9118974d818d2dc5a06a..966cd4961ea7030c43c4afe234f0c8a4472f8160/text/text-vertical).

**New Features**

* Refactored all public classes to provide more convenient, idiomatic Kotlin APIs for general usage, while maintaining strong Java interoperability.

**API Changes**

* Added a default zero-argument constructor to `FontShearSpan` for Java compatibility ([I73065](https://android-review.googlesource.com/#/q/I730658f1c6d29b291b6a9493e3ccc40f0ada4764), [b/493692287](https://issuetracker.google.com/issues/493692287)).
* Removed the `Parcelable` implementation in `RubySpan` and `EmphasisSpan` ([I49884](https://android-review.googlesource.com/#/q/I49884b2585ece811bb85a86d7b100c68d10f116d), [b/493693386](https://issuetracker.google.com/issues/493693386)).
* Refactored `EmphasisSpan` for better compatibility ([I34c40](https://android-review.googlesource.com/#/q/I34c40e89606a520b3a6a8d3d3f5c4cc531da6fc5), [b/493693310](https://issuetracker.google.com/issues/493693310)).
* Refactored `AnnotationPosition` to improve API surface ([I10dce](https://android-review.googlesource.com/#/q/I10dce948b769873d68c64077b4d96997cc2fa37e), [b/493693386](https://issuetracker.google.com/issues/493693386)).
* Converted `TextOrientation` to an enum class, refactored `AnnotationPosition` to a sealed class, and removed `RubySpan.Builder` ([Ib4a77](https://android-review.googlesource.com/#/q/Ib4a77651cdd2f3c7aa320ba6ef6d51c7965b7283), [b/493693386](https://issuetracker.google.com/issues/493693386)).
* Added the `AnnotationPosition` enum and refactored the `RubySpan` class ([Ibfcff](https://android-review.googlesource.com/#/q/Ibfcff6f417bbb5bdf79998fa7876e5cec79bb93a), [b/493692426](https://issuetracker.google.com/issues/493692426)).
* Refactored `TextOrientation` for general usage and improved internal text scaling extensions ([I82152](https://android-review.googlesource.com/#/q/I821529f1e8457a5541a66e55907ea04aa88104c9), [b/493692428](https://issuetracker.google.com/issues/493692428)).

### Version 1.0.0-alpha03

March 25, 2026

`androidx.text:text-vertical:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..1abcb4178d48853948b9b566cabff9222d90ab69/text/text-vertical).

**New Features**

* `VerticalTextLayout` now supports the horizontal layout, to display special spans in Japanese such as Ruby and Emphasis (Boten).

**API Changes**

* `RubySpan` and `EmphasisSpan` now inherit ReplacementSpan for supporting them for horizontal text ([I38db6](https://android-review.googlesource.com/#/q/I38db6f5fd0676dc0fdf0433dd81e53fe3c7fc981), [b/447239659](https://issuetracker.google.com/issues/447239659), [b/447224892](https://issuetracker.google.com/issues/447224892))

### Version 1.0.0-alpha02

October 08, 2025

`androidx.text:text-vertical:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..4350deab5806bf95370a4d012d7eeaa70a10be44/text/text-vertical).

**New Features**

* Added `VerticalTextLayout#isVerticalTextLayoutSupported()` method to check capability of vertical text ([Ie2802](https://android-review.googlesource.com/#/q/Ie2802d542557658d06c3d90b5dc10d0f8677aad7), [b/442608654](https://issuetracker.google.com/issues/442608654))

**API Changes**

* Introduced a graceful fallback in API < 36.([I8a67a](https://android-review.googlesource.com/#/q/I8a67aa87031b6e322fb9fd1671090f873ba5d760), [b/442608654](https://issuetracker.google.com/issues/442608654))
* Downgrade `minSDK` to 23 to be used in other AndroidX libraries ([I2d6b5](https://android-review.googlesource.com/#/q/I2d6b55e7148e919f16d810712893a567a36ce9d7), [b/442608654](https://issuetracker.google.com/issues/442608654))

### Version 1.0.0-alpha01

August 27, 2025

`androidx.text:text-vertical:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681/text/text-vertical).

**New Features**

* A new vertical text library to support vertical text layout mainly for Japanese, by leveraging the new [VERTICAL\_TEXT\_FLAG](https://developer.android.com/reference/android/graphics/Paint#VERTICAL_TEXT_FLAG) flag added in Android 16.
* Added `VerticalTextLayout` that displayed vertical text with proper line breaks, mixed orientation (e.g., horizontal Latin characters within a vertical line), and ruby text. ([8b3a10](https://android.googlesource.com/platform/frameworks/support/+/8b3a10cb8bc1ad17da5da6bb1386499453a4899e))
* Added `FontShearSpan` for italic-like style in vertical text. ([1ffd78](https://android.googlesource.com/platform/frameworks/support/+/1ffd782e24d6143a899c18c1599a95cab0d6cf64))
* Added `EmphasisRun` for emphasis marks. ([fe12d9](https://android.googlesource.com/platform/frameworks/support/+/fe12d9efff8394cfed4717324fe5dc648dc1e927))