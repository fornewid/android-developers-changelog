---
title: https://developer.android.com/jetpack/androidx/releases/performance
url: https://developer.android.com/jetpack/androidx/releases/performance
source: md.txt
---

# performance

API Reference  
[androidx.performance](https://developer.android.com/reference/kotlin/androidx/performance/package-summary)  
Provides source annotations for performance optimizations.  

|  Latest Update   | Stable Release | Release Candidate | Beta Release |                                           Alpha Release                                            |
|------------------|----------------|-------------------|--------------|----------------------------------------------------------------------------------------------------|
| January 15, 2025 | -              | -                 | -            | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/performance#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on performance, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    //TODO: Confirm these dependencies
    implementation "androidx.performance:performance:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    //TODO: Confirm these dependencies
    implementation("androidx.performance:performance:1.0.0-alpha01")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1709068+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1709068&template=2081980)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha01

January 15, 2025

`androidx.performance:performance-*:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5/performance).

- These libraries add a set of platform compatibility mechanisms intended for androidx internal use only. These libraries are used as implementation dependencies only.