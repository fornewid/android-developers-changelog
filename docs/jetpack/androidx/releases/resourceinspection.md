---
title: https://developer.android.com/jetpack/androidx/releases/resourceinspection
url: https://developer.android.com/jetpack/androidx/releases/resourceinspection
source: md.txt
---

# Resource Inspection

# ResourceInspection

API Reference  
[androidx.resourceinspection.annotation](https://developer.android.com/reference/kotlin/androidx/resourceinspection/annotation/package-summary)  
Surface the attributes of custom views in Android Studio's Live Layout Inspector.  

|  Latest Update   |                                      Stable Release                                       | Release Candidate | Beta Release | Alpha Release |
|------------------|-------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| January 26, 2022 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/resourceinspection#1.0.1) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on ResourceInspection, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.resourceinspection:resourceinspection-annotation:1.0.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.resourceinspection:resourceinspection-annotation:1.0.1")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1033483+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1033483&template=1565569)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.1

January 26, 2022

`androidx.resourceinspection:resourceinspection-annotation:1.0.1`and`androidx.resourceinspection:resourceinspection-processor:1.0.1`are released.[Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/255d9759ff9495ea552d71b415bf638a02046780..8ae940536431022e180d2b13f8981184dc60fa74/resourceinspection)

**Bug Fixes**

- Added package documentation

### Version 1.0.0

November 3, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0`and`androidx.resourceinspection:resourceinspection-processor:1.0.0`are released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c38bf8cba2f6d60f9cceb03adcb56ff57f793b27..255d9759ff9495ea552d71b415bf638a02046780/resourceinspection)

**Major features of 1.0.0**

- The ResourceInspection library provides an annotation processor for library developers to surface the attributes of custom views in Android Studio's[Live Layout Inspector](https://developer.android.com/studio/debug/layout-inspector#4-0-0-live-layout-inspector).

### Version 1.0.0-rc01

October 27, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0-rc01`and`androidx.resourceinspection:resourceinspection-processor:1.0.0-rc01`are released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..c38bf8cba2f6d60f9cceb03adcb56ff57f793b27/resourceinspection)

- No changes since 1.0.0-beta01

### Version 1.0.0-beta01

September 15, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0-beta01`and`androidx.resourceinspection:resourceinspection-processor:1.0.0-beta01`are released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/resourceinspection)

**Bug Fixes**

- Fixed crash on non-existent attributes ([I87df0](https://android-review.googlesource.com/#/q/I87df0c0c68f04b32274eaedd65b5a7ab3c56b562))
- Fixed crash when compiling against an older SDK ([Ie8a1e](https://android-review.googlesource.com/#/q/Ie8a1eafcae62aa98330fc7af89474a32c61faafc))
- Added validation for int enums and flags ([Ic7ecf](https://android-review.googlesource.com/#/q/Ic7ecf3386c04d133f74b858953d747cacfecfc5a))

### Version 1.0.0-alpha03

June 30, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0-alpha03`and`androidx.resourceinspection:resourceinspection-processor:1.0.0-alpha03`are released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/resourceinspection)

**Bug Fixes**

- Fix a bug in generated code that prevented the Layout Inspector from reading view attributes. ([Ic7507](https://android-review.googlesource.com/#/q/Ic75075f21dafdf5cd12b714eff3a42e0fab17bbc))

### Version 1.0.0-alpha02

June 2, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0-alpha02`and`androidx.resourceinspection:resourceinspection-processor:1.0.0-alpha02`are released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..86ff5b4bb956431ec884586ce0aea0127e189ec4/resourceinspection)

**API Changes**

- Improved AppCompat support ([I2d738](https://android-review.googlesource.com/#/q/I2d7387a017585bcea14a8d8a857b9b60930bc1c5),[b/188446121](https://issuetracker.google.com/issues/188446121))

### Version 1.0.0-alpha01

March 24, 2021

`androidx.resourceinspection:resourceinspection-annotation:1.0.0-alpha01`and`androidx.resourceinspection:resourceinspection-processor:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713/resourceinspection)

**New Features**

The Resource Inspection library provides a convenient way for library developers to surface the attributes of custom views in Android Studio's[Live Layout Inspector](https://developer.android.com/studio/debug/layout-inspector#4-0-0-live-layout-inspector). This initial release is`1.0.0-alpha01`.