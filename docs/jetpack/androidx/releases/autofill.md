---
title: https://developer.android.com/jetpack/androidx/releases/autofill
url: https://developer.android.com/jetpack/androidx/releases/autofill
source: md.txt
---

# Autofill

[User Guide](https://developer.android.com/guide/topics/text/autofill) [Code Sample](https://github.com/android/input-samples)  
API Reference  
[androidx.autofill](https://developer.android.com/reference/kotlin/androidx/autofill/package-summary)  
Improve autofill accuracy via extending hints.  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| June 4, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/autofill#1.3.0) | - | - | - |

## Declaring dependencies

To add a dependency on Autofill, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.autofill:autofill:1.3.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.autofill:autofill:1.3.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:670328+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=670328&template=1422416)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.3

### Version 1.3.0

June 4, 2025

`androidx.autofill:autofill:1.3.0` is released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/de7ff0d66c069bf65e3faae7d59e3ca579031e03..934a41ec2c6c5c7a033e600ca0635df2c79ccd13/autofill/autofill).

**Important changes since AutoFill 1.2.0**

- Adds autofill hint constants for wallet valuables types.

### Version 1.3.0-rc01

February 12, 2025

`androidx.autofill:autofill:1.3.0-rc01` is released. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..de7ff0d66c069bf65e3faae7d59e3ca579031e03/autofill/autofill).

- This release moves Autofill 1.3.0 into stabilization.

### Version 1.3.0-beta01

September 18, 2024

`androidx.autofill:autofill:1.3.0-beta01` is released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..0431b84980e97d6bafdfda7c9038bc4d9529564f/autofill/autofill).

### Version 1.3.0-alpha01

May 24, 2023

`androidx.autofill:autofill:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/autofill/autofill)

**API Changes**

- Adds autofill hint constants for wallet valuables types. ([Ie5d9d](https://android-review.googlesource.com/#/q/Ie5d9d377dd44590e2104731949734ff11f15a41c))

## Version 1.2.0

### Version 1.2.0-beta01

July 21, 2021

`androidx.autofill:autofill:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc/autofill/autofill)

**New Features**

- Added new extended hint constants for more requested field types:
  - WiFi Password
  - Email OTP
  - Authenticator app OTP
  - UPI address
  - Address unit
  - Address dependent locality
  - Promo codes

### Version 1.2.0-alpha02

June 2, 2021

`androidx.autofill:autofill:1.2.0-alpha02` is released.

**API Changes**

- `AUTOFILL_HINT_TFA_APP_OTP` renamed to `AUTOFILL_HINT_2FA_APP_OTP` to match the canonical representation of two-factor authentication.

### Version 1.2.0-alpha01

March 24, 2021

`androidx.autofill:autofill:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ef7019a95c1b606a0ccd2856b1ad7b332e3501b..5c42896eb6591b09e3952030fb7ea8d9b8c42713/autofill/autofill)

**New Features**

- Added new extended hint constants for more requested field types:
  - WiFi Password
  - Email OTP
  - Authenticator app OTP
  - UPI address
  - Address unit
  - Address dependent locality
  - Promo codes

**API Changes**

- Added new autofill hints for some requested types (Email OTP, Granular address fields, Promo codes, UPI ID). ([I89e2f](https://android-review.googlesource.com/#/q/I89e2f2b9631c8369c07248b32c239bde37f5aab8))

## Version 1.1.0

### Version 1.1.0

January 27, 2021

`androidx.autofill:autofill:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d97e99d4fa84f60b4c51eecff3ab994d5bcac1ef..7ef7019a95c1b606a0ccd2856b1ad7b332e3501b/autofill/autofill)

**Major changes since 1.0.0**

- Adds a set of APIs to support constructing Autofill inline suggestions, a new feature that was introduced in Android 11. See [the IME Autofill Guide](https://developer.android.com/guide/topics/text/ime-autofill) for more information.
- Specifically, v1 UI template [InlineSuggestionUi](https://developer.android.com/reference/androidx/autofill/inline/v1/InlineSuggestionUi) is introduced, with example code in the javadoc, to help IME developers to specify inline suggestion styles, and Autofill provider developers to construct inline suggestion contents.

### Version 1.1.0-rc01

November 11, 2020

`androidx.autofill:autofill:1.1.0-rc01` is released with no change since `1.1.0-beta01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..d97e99d4fa84f60b4c51eecff3ab994d5bcac1ef/autofill)

### Version 1.1.0-beta01

October 14, 2020

`androidx.autofill:autofill:1.1.0-beta01` is released with no changes since `1.1.0-alpha02`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..f413b8be76bfa0a4d109a3afb583188c580a2aa6/autofill/autofill)

### Version 1.1.0-alpha02

August 19, 2020

`androidx.autofill:autofill:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8744680798c115f612a99148c5a5c3ad4bd6fbf5..96eb302ee1740ba656c90c9fb27df3723a1a89c1/autofill/autofill)

**API Changes**

- Updated the required API version of the autofill inline suggestion library from Q to R ([I983a5](https://android-review.googlesource.com/#/q/I983a5904df5b2900f8b776e5d00a8132cc601f30))
- `InlineSuggestionUi` helper added to allow autofill services to generate inline presentations
- Renderer added to help IME providers to inflate inline presentations sent by autofill services
- Styling and theming support for IME providers added as part of v1 versioned style API

### Version 1.1.0-alpha01

March 18, 2020

`androidx.autofill:autofill:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/34328d238b2999f231e824d2a9149acdbe3d5c00..8744680798c115f612a99148c5a5c3ad4bd6fbf5/autofill/autofill)

**New Features**

- `InlinePresentationBuilder` added to help autofill providers to interface with the new keyboard based `InlineSuggestionRequest`
- `InlinePresentationRenderer` added to help keyboard providers to render Slices given by autofill providers
- `InlineSuggestionsHostView` added to allow keyboard providers to constrain where the slices are rendered

## Version 1.0.0

### Version 1.0.0

December 4, 2019

`androidx.autofill:autofill:1.0.0` is released. [Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce07ec29121b02ac196689766626af39a5fa8700..34328d238b2999f231e824d2a9149acdbe3d5c00/autofill).

**Major features of 1.0.0**

- First stable version of the autofill module.
- Adds a standard set of supported autofill hint constants which should be supported by all autofill services.

### Version 1.0.0-rc01

October 23, 2019

`androidx.autofill:autofill:1.0.0-rc01` is released with no changes since `1.0.0-beta01`. [Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/391dc4bc729d2973a6e6e57916d3008c58026e56..ce07ec29121b02ac196689766626af39a5fa8700/autofill).

### Version 1.0.0-beta01

September 18, 2019

`androidx.autofill:autofill:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/a290bf422772729760cd49aa80450826768d5a45..391dc4bc729d2973a6e6e57916d3008c58026e56/autofill).

**New features**

- Added support for annotating One Time Password (OTP) fields which can be filled by reading the code from an SMS.
- Generator function added to get hint constants for single character OTP fields.

### Version 1.0.0-alpha02

August 7, 2019

`androidx.autofill:autofill:1.0.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a6ddab53486a549190d183f626993551dfaeacf5..a290bf422772729760cd49aa80450826768d5a45/autofill).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- New hint constants added to support annotation of SMS One Time Password (OTP) codes.

### Version 1.0.0-alpha01

July 2, 2019

This is the first release of `androidx.autofill:autofill:1.0.0-alpha01`. The commits included in this initial version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a6ddab53486a549190d183f626993551dfaeacf5/autofill).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

This is the initial release of autofill AndroidX module. It provides new autofill hint constants added to allow more granular annotation of form fields.