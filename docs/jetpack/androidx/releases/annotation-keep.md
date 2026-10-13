---
title: https://developer.android.com/jetpack/androidx/releases/annotation-keep
url: https://developer.android.com/jetpack/androidx/releases/annotation-keep
source: md.txt
---

# Annotation Keep

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 12, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/annotation-keep#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on annotation keep, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.annotation.keep:keep:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-android:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-gradle-plugin:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-iosarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-iossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-jvm:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-linuxarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-linuxx64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-macosarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-mingwx64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-tvosarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-tvossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-watchosarm32:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-watchosarm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-watchosdevicearm64:1.0.0-alpha01"
    implementation "androidx.annotation.keep:keep-watchossimulatorarm64:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.annotation.keep:keep:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-android:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-gradle-plugin:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-iosarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-iossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-jvm:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-linuxarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-linuxx64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-macosarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-mingwx64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-tvosarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-tvossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-watchosarm32:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-watchosarm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-watchosdevicearm64:1.0.0-alpha01")
    implementation("androidx.annotation.keep:keep-watchossimulatorarm64:1.0.0-alpha01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2295349+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2295349&template=2425184)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha01

October 12, 2026

`androidx.annotation.keep:keep-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c01b149d4ed9ed3ed6932dc1fab475895b942d1f/annotation/keep).

**API Changes**