---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins
source: md.txt
---

# privacysandbox plugins

API Reference  
[androidx.privacysandbox.plugins](https://developer.android.com/reference/kotlin/androidx/privacysandbox/plugins/package-summary)  
Android Privacy Sandbox Sdk Library Gradle Plugin  

| Latest Update  | Stable Release | Release Candidate | Beta Release |                                                 Alpha Release                                                 |
|----------------|----------------|-------------------|--------------|---------------------------------------------------------------------------------------------------------------|
| August 9, 2023 | -              | -                 | -            | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on privacysandbox plugins, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement privacysandbox plugins
    implementation "androidx.privacysandbox.plugins:plugins-privacysandbox-library:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement privacysandbox plugins
    implementation("androidx.privacysandbox.plugins:plugins-privacysandbox-library:1.0.0-alpha02")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1344534+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1344534&template=1808652)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha02

August 9, 2023

`androidx.privacysandbox.plugins:plugins-privacysandbox-library:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..5d7dd999525725bd038a00ca4e89e0fef624a6da/privacysandbox/plugins/plugins-privacysandbox-library)

**New Features**

Updates applied privacy sandbox libraries versions:

- privacysandbox tools libraries 1.0.0-alpha04
- privacysandbox sdkruntime libraries 1.0.0-alpha06
- coroutine libraries 1.6.4

**Bug Fixes**

- Update Privacy Sandbox tool versions to alpha-04. ([I5b9fa](https://android-review.googlesource.com/#/q/I5b9fac55f5cce253b8a76be6f05aee3fcfea76cd))

### Version 1.0.0-alpha01

April 5, 2023

`androidx.privacysandbox.plugins:plugins-privacysandbox-library:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597/privacysandbox/plugins/plugins-privacysandbox-library)

**New Features**

- New Androidx Gradle Plugin that provides assistance for Android libraries consumed by privacy sandbox sdk modules. The plugin configures the tools-apipackager as a KSP symbol processor and adds necessary dependencies.