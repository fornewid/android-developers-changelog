---
title: https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater
url: https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater
source: md.txt
---

# Asynclayoutinflater

# Asynclayoutinflater

API Reference  
[androidx.asynclayoutinflater.view](https://developer.android.com/reference/kotlin/androidx/asynclayoutinflater/view/package-summary)  
Inflate layouts asynchronously to avoid jank in the UI.  

| Latest Update |                                       Stable Release                                       | Release Candidate | Beta Release | Alpha Release |
|---------------|--------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on AsyncLayoutInflater, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.asynclayoutinflater:asynclayoutinflater:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.asynclayoutinflater:asynclayoutinflater:1.1.0")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460550+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460550&template=1422675)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.1.0

### Version 1.1.0

April 9, 2025

`androidx.asynclayoutinflater:asynclayoutinflater:1.1.0`and`androidx.asynclayoutinflater:asynclayoutinflater-appcompat:1.1.0`are released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f85ba4f521f334ee3e92ab0ff3359be2d281c2b9..7dd3136de5363becb496bfdb2c98bf89d4eb7305/asynclayoutinflater).

**Important changes since 1.0.0**

- Allows configuring a`AsyncLayoutFactory`when initializing`AsyncLayoutInflater`. For AppCompat context, this can be provided through`AsyncAppCompatFactory`which initializes AppCompat views correctly.
- The`inflate`API accepts an executor on which`OnInflateFinishedListener`callback can be triggered.

### Version 1.1.0-rc01

March 26, 2025

`androidx.asynclayoutinflater:asynclayoutinflater:1.1.0-rc01`and`androidx.asynclayoutinflater:asynclayoutinflater-appcompat:1.1.0-rc01`are released with no notable changes since the last beta. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8870a8ee99ec618927a9edb4b6e74b8570381149..f85ba4f521f334ee3e92ab0ff3359be2d281c2b9/).

### Version 1.1.0-beta01

March 12, 2025

`androidx.asynclayoutinflater:asynclayoutinflater:1.1.0-beta01`and`androidx.asynclayoutinflater:asynclayoutinflater-appcompat:1.1.0-beta01`are released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..8870a8ee99ec618927a9edb4b6e74b8570381149/asynclayoutinflater).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I32dda](https://android-review.googlesource.com/#/q/I32ddafb7e7412d5570a803f82d3e1f45b2febd4c),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.1.0-alpha01

October 5, 2022

`androidx.asynclayoutinflater:asynclayoutinflater:1.1.0-alpha01`and`androidx.asynclayoutinflater:asynclayoutinflater-appcompat:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/asynclayoutinflater)

**New Features**

- Allows configuring a`AsyncLayoutFactory`when initialzing`AsyncLayoutInflater`. For AppCompat context, this can be provided through`AsyncAppCompatFactory`which initializes AppCompat views correctly.
- The inflate API accepts an executor on which`OnInflateFinishedListener`callback can be triggered.