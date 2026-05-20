---
title: https://developer.android.com/jetpack/androidx/releases/test-ext
url: https://developer.android.com/jetpack/androidx/releases/test-ext
source: md.txt
---

# test ext

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| May 19, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/test-ext#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on test-ext, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement test exts
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext:1.0.0-alpha03"

    // Use to implement test ext complications
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-data-source:1.0.0-alpha03"
    // (Kotlin-specific extensions)
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-data-source-ktx:1.0.0-alpha03"

    // Use to implement a ext style and complication editor
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-editor:1.0.0-alpha03"

    // Can use to render complications.
    //TODO: Confirm these dependencies
    // This library is optional and exts may have custom implementation for rendering
    // complications.
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-rendering:1.0.0-alpha03"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement test exts
    //TODO: Confirm these dependencies
    implementation("androidx.test.ext:ext:1.0.0-alpha03")

    // Use to implement test ext complications
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-data-source:1.0.0-alpha03"
    // (Kotlin-specific extensions)
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-data-source-ktx:1.0.0-alpha03"

    // Use to implement a ext style and complication editor
    //TODO: Confirm these dependencies
    implementation("androidx.test.ext:ext-editor:1.0.0-alpha03")

    // Can use to render complications.
    //TODO: Confirm these dependencies
    // This library is optional and exts may have custom implementation for rendering
    // complications.
    //TODO: Confirm these dependencies
    implementation "androidx.test.ext:ext-complications-rendering:1.0.0-alpha03"
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1667556+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1667556&template=https://b.corp.google.com/issues/new?component%3D1667556&template=2058336)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha03

May 19, 2026

`androidx.test.ext:junit-gtest:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/01aefa1ec2d8ae54b9a4dd42cedfa13352d71cae..466b8fd7dc877ebc2e961649f1c65a6c3627275f/test/ext/junit-gtest).

**API Changes**

- Deprecate all APIs in junit-gtest. ([I355df](https://android-review.googlesource.com/#/q/I355dfb907ec590913e843a37bb6077441171e5b0), [b/500007449](https://issuetracker.google.com/issues/500007449))

**Bug Fixes**

- Change `minSdkVersion` to 21 to allow for NDK upgrade ([Ic748f](https://android-review.googlesource.com/#/q/Ic748f8570b1fb31702be340d0403a37c65401cbc))