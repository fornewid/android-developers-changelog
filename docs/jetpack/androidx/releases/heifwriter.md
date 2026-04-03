---
title: https://developer.android.com/jetpack/androidx/releases/heifwriter
url: https://developer.android.com/jetpack/androidx/releases/heifwriter
source: md.txt
---

# Heifwriter

# Heifwriter

API Reference  
[androidx.heifwriter](https://developer.android.com/reference/kotlin/androidx/heifwriter/package-summary)  
Encode an image or image collection in HEIF format using the available codecs on the Android device.  

|  Latest Update   |                                  Stable Release                                   | Release Candidate | Beta Release |                                           Alpha Release                                           |
|------------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------------------------------------------------------------------------------------------|
| October 22, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/heifwriter#1.1.0) | -                 | -            | [1.2.0-alpha01](https://developer.android.com/jetpack/androidx/releases/heifwriter#1.2.0-alpha01) |

## Declaring dependencies

To add a dependency on HeifWriter, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.heifwriter:heifwriter:1.2.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.heifwriter:heifwriter:1.2.0-alpha01")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460473+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460473&template=1422625)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.0-alpha01

October 22, 2025

`androidx.heifwriter:heifwriter:1.2.0-alpha01`is released. Version 1.2.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/db5d2549d20116296d94d445a129a8b5dab5380b..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/heifwriter/heifwriter).

**New Features**

- A new`EncoderPreference`class has been implemented. This enhancement enables`HeifWriter`to consider encoder preferences, such as hardware or software encoding and enforcement of Constant Quantization (CQ), during the encoder selection process. If a suitable encoder cannot be found based on the specified preferences, an exception will be raised.

**API Changes**

- Added`EncoderPreference`class.[I81efd](https://android.googlesource.com/platform/frameworks/support/+/1cd0fc33beddf6a2b0d8d0a34b0d5d9c9f39f50d%5E%21/)

## Version 1.1

### Version 1.1.0

October 08, 2025

`androidx.heifwriter:heifwriter:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/730163fb904c374ddffe12740acf2d0b5e685dca..db5d2549d20116296d94d445a129a8b5dab5380b/heifwriter/heifwriter).

### Version 1.1.0-rc02

September 24, 2025

`androidx.heifwriter:heifwriter:1.1.0-rc02`is released. Version 1.1.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a5000d666331c3e5dc3064b0b5d2aafc8822b2b6..730163fb904c374ddffe12740acf2d0b5e685dca/heifwriter/heifwriter).

### Version 1.1.0-rc01

August 27, 2025

`androidx.heifwriter:heifwriter:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..a5000d666331c3e5dc3064b0b5d2aafc8822b2b6/heifwriter/heifwriter).

### Version 1.1.0-beta01

April 9, 2025

`androidx.heifwriter:heifwriter:1.1.0-beta01`is released with no notable changes. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..4c37298a97c16270c139eb812ddadaba03e23a52/heifwriter/heifwriter).

### Version 1.1.0-alpha05

February 12, 2025

`androidx.heifwriter:heifwriter:1.1.0-alpha05`is released with no notable changes since the last alpha. Version 1.1.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/85de16d348e19418f1602b34c72bcf243514a962..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/heifwriter/heifwriter).

### Version 1.1.0-alpha04

January 15, 2025

`androidx.heifwriter:heifwriter:1.1.0-alpha04`is released. Version 1.1.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..85de16d348e19418f1602b34c72bcf243514a962/heifwriter/heifwriter).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Icdd6c](https://android-review.googlesource.com/#/q/Icdd6c7401ac3b05b2842859da3dfe0bc9a78365e),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Fixed[b/372391363](https://issuetracker.google.com/issues/372391363)releasing buffer queues in the correct order to fix CTS failure.

### Version 1.1.0-alpha03

October 2, 2024

`androidx.heifwriter:heifwriter:1.1.0-alpha03`is released. Version 1.1.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c07f19942f7b20c74b9e72a0a706a0dc89adddfc..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/heifwriter/heifwriter).

**Bug Fixes**

- Fixes in documentation

### Version 1.1.0-alpha02

July 26, 2023

`androidx.heifwriter:heifwriter:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..c07f19942f7b20c74b9e72a0a706a0dc89adddfc/heifwriter/heifwriter)

**New Features**

- 10-bit encoding support
- AVIF encoding support

**Bug Fixes**

- Include experimental APIs in current.txt ([I1a07e](https://android-review.googlesource.com/#/q/I1a07e82e0e35b5fe361bfe02a3c42a2b2b85e2cb),[b/278769092](https://issuetracker.google.com/issues/278769092))
- N/A, API file changes are just reordering methods ([I5fa95](https://android-review.googlesource.com/#/q/I5fa95ca42073461bed8e5020c91b4c0894b70753))
- API lint check for`MissingGetterMatchingBuilder`is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9),[b/138602561](https://issuetracker.google.com/issues/138602561))

### Version 1.1.0-alpha01

January 22, 2020

`androidx.heifwriter:heifwriter:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..0a3d894e8fe0217f1312fb163a89ad51bf15794e/heifwriter).

**Bug fixes**

- Fined tune logic to pick HEVC/HEIC encoder
- Improved the exception handling during the shutdown sequence
- Bug fixes for quality control mode