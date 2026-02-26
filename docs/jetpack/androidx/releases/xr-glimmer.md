---
title: https://developer.android.com/jetpack/androidx/releases/xr-glimmer
url: https://developer.android.com/jetpack/androidx/releases/xr-glimmer
source: md.txt
---

# Jetpack Compose Glimmer

API Reference  
[androidx.xr.glimmer](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary)  
Design language and UI toolkit for building augmented Android XR experiences

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | - | - | - | [1.0.0-alpha07](https://developer.android.com/jetpack/androidx/releases/xr-glimmer#1.0.0-alpha07) |

## Declaring dependencies

To add a dependency on Jetpack Compose Glimmer, you must add the Google Maven  

repository to your project. Read
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.glimmer:glimmer:1.0.0-alpha07"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.glimmer:glimmer:1.0.0-alpha07")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1935653+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1935653&template=2209255)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha07

February 25, 2026

`androidx.xr.glimmer:glimmer:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..6e23fc0c137022098ae2d043778ffdc56402ba5e/xr/glimmer/glimmer).

### Version 1.0.0-alpha06

February 11, 2026

`androidx.xr.glimmer:glimmer:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/xr/glimmer/glimmer).

**API Changes**

- Add an overloaded version of `VerticalList` API with the slot for a title. ([Ic3d44](https://android-review.googlesource.com/#/q/Ic3d4452fb59503fae78426f82c20b874eedee614))
- Updated Glimmer Text `autoSize` parameter ordering for consistency with material3. ([Ic24bd](https://android-review.googlesource.com/#/q/Ic24bdfb39ca374baf64d988e977dac56c0ea5ebf), [b/477669012](https://issuetracker.google.com/issues/477669012))

### Version 1.0.0-alpha05

January 28, 2026

`androidx.xr.glimmer:glimmer:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..b0ea337f3538c22dae2295d6a9265ab0c753e301/xr/glimmer/glimmer).

### Version 1.0.0-alpha04

January 14, 2026

`androidx.xr.glimmer:glimmer:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/xr/glimmer/glimmer).

**New Features**

- Added support for multiple item decorations per item for `VerticalStack` ([22daab3](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3895807)) and support for generic decoration shapes ([033e015](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3899124)).

**API Changes**

- Added `VerticalListDefaults` to provide recommended values for the `VerticalList` composable. ([I07b1a](https://android-review.googlesource.com/#/q/I07b1aee8bf6730458b9f251d51689d1cddf8cac8), [b/448364605](https://issuetracker.google.com/issues/448364605))

**Bug Fixes**

- Added initial focus handling to `VerticalStack` to make sure the top item gets focus when focus enters the stack. This fixes an issue where initial focus gets assigned to the next item resulting in an immediate scroll to that item. ([bd69841](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3880202))
- Fixed a bug in `VerticalStack`'s `ItemDecorationNode`, where the decorations were not updated in the item scope when the modifier node is reused. ([7ec2c94](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3899284))

### Version 1.0.0-alpha03

December 17, 2025

`androidx.xr.glimmer:glimmer:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/xr/glimmer/glimmer).

**Bug Fixes**

- Behavior updates and bug fixes for Stacks

### Version 1.0.0-alpha02

December 03, 2025

`androidx.xr.glimmer:glimmer:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c907d5394acb1b40d6145046653734db55e55b8b..deb96499dfe95073f5c1215c1287787683cb1e92/xr/glimmer/glimmer).

**API Changes**

- New `items(items: List<T>)` and `itemsIndexed(items: List<T>)` extension methods on the `ListScope`. ([Ic2afe](https://android-review.googlesource.com/#/q/Ic2afeb0a723367174de1b5ebd5205533cf1c0db8))
- Provide `FlingBehavior` API for `VerticaList`. ([I16de7](https://android-review.googlesource.com/#/q/I16de7549a51f0c047eafa505756b5e131ef214cd))
- Provide a factory for `VerticalList` focus aware snapping behavior. ([I4a528](https://android-review.googlesource.com/#/q/I4a528a9724944ab72fc80023da266e999edec6d6))

### Version 1.0.0-alpha01

November 05, 2025

`androidx.xr.glimmer:glimmer:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c907d5394acb1b40d6145046653734db55e55b8b/xr/glimmer/glimmer).

**New Features**

- Initial developer release of Jetpack Compose Glimmer, design language and UI components for building augmented Android XR experiences. Designed for clarity, legibility, and minimal distraction with simplified styling, differentiated focus, and optimized elevation.
- Get started with our initial set of Jetpack Compose Glimmer components:
  - Text
  - Icons
  - Title Chips
  - Cards
  - Lists
  - Buttons
  - Stacks (Under development)