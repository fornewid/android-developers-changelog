---
title: https://developer.android.com/jetpack/androidx/releases/glance-adaptive
url: https://developer.android.com/jetpack/androidx/releases/glance-adaptive
source: md.txt
---

# Glance Adaptive

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| September 09, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/glance_adaptive#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on glance adaptive, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

\<!DOCTYPE html\>


glance adaptive deps

### Groovy

```groovy
dependencies {
    implementation "androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha02"
    implementation "androidx.glance.adaptive:adaptive-core:1.0.0-alpha02"
    implementation "androidx.glance.adaptive:adaptive-wear:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha02")
    implementation("androidx.glance.adaptive:adaptive-core:1.0.0-alpha02")
    implementation("androidx.glance.adaptive:adaptive-wear:1.0.0-alpha02")
}
```


For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:TODO+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=TODO&template=TODO)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha02

September 09, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha02`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha02`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea..e4bd62f853853bf3522ed15681c58ef28b09ed44/glance/adaptive).

**Bug Fixes**

- `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))

#### Version 1.0.0-alpha01

August 26, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha01`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha01`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea/glance/adaptive).

This is the initial release of the Glance Adaptive library - the library for building template-first `RemoteCompose` Widgets for multiple form factors and surfaces across Android ecosystem.