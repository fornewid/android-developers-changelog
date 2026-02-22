---
title: https://developer.android.com/jetpack/androidx/releases/text-vertical
url: https://developer.android.com/jetpack/androidx/releases/text-vertical
source: md.txt
---

# text-vertical

# text-vertical

API Reference  
[androidx.text](https://developer.android.com/reference/kotlin/androidx/text/package-summary)  
TODO  

|  Latest Update  | Stable Release | Release Candidate | Beta Release |                                        Alpha Release                                        |
|-----------------|----------------|-------------------|--------------|---------------------------------------------------------------------------------------------|
| October 8, 2025 | -              | -                 | -            | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/text#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on Text, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.text:text-vertical:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.text:text-vertical:1.0.0-alpha02")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1909646+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1909646&template=2203168)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Text Vertical Version 1.0

### Version 1.0.0-alpha02

October 08, 2025

`androidx.text:text-vertical:1.0.0-alpha02`is released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..4350deab5806bf95370a4d012d7eeaa70a10be44/text/text-vertical).

**New Features**

- Added`VerticalTextLayout#isVerticalTextLayoutSupported()`method to check capability of vertical text ([Ie2802](https://android-review.googlesource.com/#/q/Ie2802d542557658d06c3d90b5dc10d0f8677aad7),[b/442608654](https://issuetracker.google.com/issues/442608654))

**API Changes**

- Introduced a graceful fallback in API \< 36.([I8a67a](https://android-review.googlesource.com/#/q/I8a67aa87031b6e322fb9fd1671090f873ba5d760),[b/442608654](https://issuetracker.google.com/issues/442608654))
- Downgrade`minSDK`to 23 to be used in other AndroidX libraries ([I2d6b5](https://android-review.googlesource.com/#/q/I2d6b55e7148e919f16d810712893a567a36ce9d7),[b/442608654](https://issuetracker.google.com/issues/442608654))

### Version 1.0.0-alpha01

August 27, 2025

`androidx.text:text-vertical:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681/text/text-vertical).

**New Features**

- A new vertical text library to support vertical text layout mainly for Japanese, by leveraging the new[VERTICAL_TEXT_FLAG](https://developer.android.com/reference/android/graphics/Paint#VERTICAL_TEXT_FLAG)flag added in Android 16.
- Added`VerticalTextLayout`that displayed vertical text with proper line breaks, mixed orientation (e.g., horizontal Latin characters within a vertical line), and ruby text. ([8b3a10](https://android.googlesource.com/platform/frameworks/support/+/8b3a10cb8bc1ad17da5da6bb1386499453a4899e))
- Added`FontShearSpan`for italic-like style in vertical text. ([1ffd78](https://android.googlesource.com/platform/frameworks/support/+/1ffd782e24d6143a899c18c1599a95cab0d6cf64))
- Added`EmphasisRun`for emphasis marks. ([fe12d9](https://android.googlesource.com/platform/frameworks/support/+/fe12d9efff8394cfed4717324fe5dc648dc1e927))