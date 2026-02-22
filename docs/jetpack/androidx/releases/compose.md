---
title: https://developer.android.com/jetpack/androidx/releases/compose
url: https://developer.android.com/jetpack/androidx/releases/compose
source: md.txt
---

# Compose

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary)  
Define your UI programmatically with composable functions that describe its shape and data dependencies.

Compose is combination of 7 Maven Group Ids within `androidx`. Each Group
contains a targeted subset of functionality, each with its own set of release
notes.

This table explains the groups and links to each set of release notes.

| Group | Description |
|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | Build animations in their Jetpack Compose applications to enrich the user experience. |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | Transform @Composable functions and enable optimizations with a Kotlin compiler plugin. |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces. |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io. |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI. |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target. |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input. |

## Versions

This table lists the current versions of each group.

| Maven Group ID | Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.11.0-alpha05) |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | August 7, 2024 | [1.5.15](https://developer.android.com/jetpack/androidx/releases/compose-compiler#1.5.15) | - | - | - |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.11.0-alpha05) |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-material#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-material#1.11.0-alpha05) |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | February 11, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.4.0) | - | - | [1.5.0-alpha14](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.5.0-alpha14) |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.11.0-alpha05) |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.11.0-alpha05) |

## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:610764+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=610764&template=1424126)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## BOMs

For the latest BOM releases, visit [Compose BOM Mapping Page](https://developer.android.com/jetpack/compose/bom/bom-mapping).

## Announcements

| Date | Announcement |
|---|---|
| August 13, 2025 | The August 2025 Compose Bill of Materials (BOM) has been released, which includes the stable version of Jetpack Compose 1.9! This update for Android's modern UI toolkit introduces several new features, such as advanced shadows, 2D scrolling APIs, and better list performance. If you'd like to learn more about all the new features and improvements, check out the [full blog post!](https://android-developers.googleblog.com/2025/08/whats-new-in-jetpack-compose-august-25-release.html) |
| April 23, 2025 | The Compose 1.8 release is here! This release for Android's modern UI toolkit brings new features like autofill, several text improvements, and visibility tracking. You can also animate a composable's size and location in new ways. We've also stabilized many experimental APIs and fixed a number of bugs. To learn more about all the new features and improvements in this release, check out the full [blog post!](https://android-developers.googleblog.com/2025/04/whats-new-in-jetpack-compose-april-25.html) |
| September 4, 2024 | The 1.7 Jetpack Compose release includes many features to make Android development faster and easier, regardless of the form factor you're building for. [We also shared news](https://android-developers.googleblog.com/2024/05/whats-new-in-jetpack-compose-at-io-24.html) on expanded Compose support across the Android ecosystem. |
| January 24, 2024 | [Jetpack Compose 1.6](https://android-developers.googleblog.com/2024/01/whats-new-in-jetpack-compose-january-24-release.html) is now stable as part of the Compose January '24 Bill of Materials! This release largely focuses on performance improvements, as we continue to migrate modifiers and improve the efficiency of major parts of our API. |
| June 26, 2023 | Since Compose 1.5.0-beta01 release, Compose aar are located under \`\*-android\` artifacts. With 1.6.0-alpha01, Compose POM files have been updated to point to the \`-android\` artifact by default for dependency resolution in build systems that don't support Gradle Module Metadata. |