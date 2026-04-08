---
title: https://developer.android.com/jetpack/androidx/releases/print
url: https://developer.android.com/jetpack/androidx/releases/print
source: md.txt
---

# Print

# Print

API Reference  
[androidx.print](https://developer.android.com/reference/kotlin/androidx/print/package-summary)  
Print photos, docs, and other graphics and images from your app.  

| Latest Update  |                                Stable Release                                | Release Candidate | Beta Release | Alpha Release |
|----------------|------------------------------------------------------------------------------|-------------------|--------------|---------------|
| April 23, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/print#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Print, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.print:print:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.print:print:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:461068+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=461068&template=1422780)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

April 23, 2025

`androidx.print:print:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ebf16b28ce2d18fb383e00c130ce68ec1ffa1143..5a8037cca8d7b2046dac7578308937af87044f44/print/print).

### Version 1.1.0-rc01

April 9, 2025

`androidx.print:print:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..ebf16b28ce2d18fb383e00c130ce68ec1ffa1143/print/print).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([If585e](https://android-review.googlesource.com/#/q/If585e20f8e06ac265ebe3238e697e2b9c108fc75),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.1.0-beta01

October 28, 2020

`androidx.print:print:1.1.0-beta01`is released with no changes since`1.1.0-alpha01`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..234e23e470a5e7f81291f6acd12d538146dc010b/print/print)

### Version 1.1.0-alpha01

July 22, 2020

`androidx.print:print:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/print/print)

**Bug Fixes**

- Use RGB when delivering images to printers for better compatibility