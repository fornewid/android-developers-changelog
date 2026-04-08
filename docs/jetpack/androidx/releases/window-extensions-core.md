---
title: https://developer.android.com/jetpack/androidx/releases/window-extensions-core
url: https://developer.android.com/jetpack/androidx/releases/window-extensions-core
source: md.txt
---

# window extensions core

# window extensions core

API Reference  
[androidx.window.extensions.core](https://developer.android.com/reference/kotlin/androidx/window/extensions/core/package-summary)  
The Core APIs for Window Manager Library Extensions  

| Latest Update |                                        Stable Release                                         | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| June 7, 2023  | [1.0.0](https://developer.android.com/jetpack/androidx/releases/window-extensions-core#1.0.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on window extensions core, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement window extensions core
    implementation "androidx.window.extensions.core:core:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement window extensions core
   implementation("androidx.window.extensions.core:core:1.0.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1324559+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1324559&template=1789973)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0

June 7, 2023

`androidx.window.extensions.core:core:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41e119676c75bba23ed13a5061871a9ff46d3036..d880ecd411d7ed0d3897644cd64d7e20eae98916/window/extensions/core/core)

**Major features of 1.0.0**

- Simple interfaces to work with`androidx.window.extensions`. Not meant for generic developer use. For generic use see`androidx.core`.

### Version 1.0.0-rc01

May 10, 2023

`androidx.window.extensions.core:core:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d4c9b3ab577ea883637e38bbd1fc3ca9b08f2fa..41e119676c75bba23ed13a5061871a9ff46d3036/window/extensions/core/core)

**New Features**

- Release some interfaces to improve function for`androidx.window`and specific devices. These interfaces are not for general use. Use the interfaces in`androidx.core`instead.

**Bug Fixes**

- Make core interfaces public so it can be used in extensions. ([I45052](https://android-review.googlesource.com/#/q/I450527ca1ed9cb8bcd27289d681f441b0074f012))

### Version 1.0.0-beta03

May 3, 2023

`androidx.window.extensions.core:core:1.0.0-beta03`is released.[Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..5d4c9b3ab577ea883637e38bbd1fc3ca9b08f2fa/window/extensions/core/core)

**New Features**

Reinstate`extensions.core`interfaces. These are an implementation detail used, please use the`androidx.core`APIs instead.

**Bug Fixes**

- Make core interfaces public so it can be used in extensions. ([I45052](https://android-review.googlesource.com/#/q/I450527ca1ed9cb8bcd27289d681f441b0074f012))

### Version 1.0.0-beta02

April 5, 2023

`androidx.window.extensions.core:core:1.0.0-beta02`is released.[Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/window/extensions/core/core)

**API Changes**

- Hide local interfaces that are not meant for public use. ([I3e88b](https://android-review.googlesource.com/#/q/I3e88b44d034b1a24347ac8606755ba04c9bd1558))

### Version 1.0.0-beta01

March 22, 2023`androidx.window.extensions.core:core:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..5e7d256f82fbafb6d059ab7b18fddd87c7531553/window/extensions/core/core)

- Added the window extensions core version of functional interface to reduce issues of lambda expressions desugaring.

### Version 1.0.0-alpha01

February 22, 2023

`androidx.window.extensions.core:core:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522/)

**New Features**

- Add some local interfaces that are not meant for general developer use. This is an implementation detail to support the androidx.window library. Please see the`androidx.window`library instead.