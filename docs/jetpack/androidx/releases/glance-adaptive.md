---
title: https://developer.android.com/jetpack/androidx/releases/glance-adaptive
url: https://developer.android.com/jetpack/androidx/releases/glance-adaptive
source: md.txt
---

# Glance Adaptive

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| November 04, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/glance_adaptive#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on glance adaptive, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha04"
    implementation "androidx.glance.adaptive:adaptive-core:1.0.0-alpha04"
    implementation "androidx.glance.adaptive:adaptive-wear:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha04")
    implementation("androidx.glance.adaptive:adaptive-core:1.0.0-alpha04")
    implementation("androidx.glance.adaptive:adaptive-wear:1.0.0-alpha04")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component&template)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha04

November 04, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha04`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha04`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2b5ae7b0fe1bb4eece7018878fe5f18c5967a2f..a021adf44194ae86e596ae25ca43d5e4e18f6926/glance/adaptive).

**API Changes**

- Added `GlanceAdaptiveWidgetReceiver` base `AppWidgetProvider` class as the main entry point for Glance Adaptive widgets. ([Iddecc](https://android-review.googlesource.com/#/q/Iddecc86920578ee4f5c6a66d96278ceae72758b7))
- Added `@integer/glance_adaptive_widget_category_all_known` resource for `<appwidget-provider>`'s `android:widgetCategory` declaration, to opt in into all supported Widget surfaces. ([I4582e](https://android-review.googlesource.com/#/q/I4582e2140f96b5911d674a6892d726f7e8cda4ff))

### Version 1.0.0-alpha03

September 23, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha03`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha03`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e4bd62f853853bf3522ed15681c58ef28b09ed44..b2b5ae7b0fe1bb4eece7018878fe5f18c5967a2f/glance/adaptive).

Internal development to enable building template-first `RemoteCompose` Widgets for multiple surfaces across Android ecosystem. Public APIs to come.

### Version 1.0.0-alpha02

September 09, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha02`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha02`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea..e4bd62f853853bf3522ed15681c58ef28b09ed44/glance/adaptive).

**Bug Fixes**

- `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))

#### Version 1.0.0-alpha01

August 26, 2026

`androidx.glance.adaptive:adaptive-appwidget:1.0.0-alpha01`, `androidx.glance.adaptive:adaptive-core:1.0.0-alpha01`, and `androidx.glance.adaptive:adaptive-wear:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea/glance/adaptive).

This is the initial release of the Glance Adaptive library - the library for building template-first `RemoteCompose` Widgets for multiple form factors and surfaces across Android ecosystem.