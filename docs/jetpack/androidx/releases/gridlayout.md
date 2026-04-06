---
title: https://developer.android.com/jetpack/androidx/releases/gridlayout
url: https://developer.android.com/jetpack/androidx/releases/gridlayout
source: md.txt
---

# GridLayout

# GridLayout

[Code Sample](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/CycleEditor/src/com/google/androidstudio/motionlayoutcycles/MainPanel.java)  
API Reference  
[androidx.gridlayout.widget](https://developer.android.com/reference/kotlin/androidx/gridlayout/widget/package-summary)  
Implement a grid layout.  

| Latest Update |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/gridlayout#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on GridLayout, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.gridlayout:gridlayout:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.gridlayout:gridlayout:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460990+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460990&template=1422598)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.1

### Version 1.1.0

April 9, 2025

`androidx.gridlayout:gridlayout:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/d97f11014f7445681568d955387d895e87f584b2..1ae17d5f1e991c672971ab50949feecb75d1e557/gridlayout/gridlayout).

**Important changes since 1.0.0**

- Removed dependency on`androidx.legacy`library and dropped support for legacy`Space`class in GridLayout. Developers should be using the platform version of`Space`(`android.widget.Space`) class instead of the`androidx.legacy`version.

### Version 1.1.0-rc01

March 26, 2025

`androidx.gridlayout:gridlayout:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..d97f11014f7445681568d955387d895e87f584b2/).

### Version 1.1.0-beta01

May 24, 2023

`androidx.gridlayout:gridlayout:1.1.0-beta01`is released with no changes.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/gridlayout/gridlayout)

### Version 1.1.0-alpha01

March 22, 2023

`androidx.gridlayout:gridlayout:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553/gridlayout/gridlayout)

**New Features**

- Remove dependency on`androidx.legacy`library and drop support for legacy`Space`class in GridLayout. Developers should be using the platform version of Space class instead of the`androidx.legacy`version.