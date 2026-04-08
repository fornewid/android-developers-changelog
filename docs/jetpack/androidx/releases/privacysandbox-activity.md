---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity
source: md.txt
---

# privacysandbox activity

# privacysandbox activity

API Reference  
[androidx.privacysandbox.activity](https://developer.android.com/reference/kotlin/androidx/privacysandbox/activity/package-summary)  
TODO  

| Latest Update  | Stable Release | Release Candidate | Beta Release |                                                 Alpha Release                                                  |
|----------------|----------------|-------------------|--------------|----------------------------------------------------------------------------------------------------------------|
| March 26, 2025 | -              | -                 | -            | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on privacysandbox-activity, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement privacysandbox activitys
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity:1.0.0-alpha02"

    // Use to implement privacysandbox activity complications
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-data-source:1.0.0-alpha02"
    // (Kotlin-specific extensions)
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-data-source-ktx:1.0.0-alpha02"

    // Use to implement a activity style and complication editor
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-editor:1.0.0-alpha02"

    // Can use to render complications.
    // TODO: Confirm these dependencies
    // This library is optional and activitys may have custom implementation for rendering
    // complications.
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-rendering:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement privacysandbox activitys
    // TODO: Confirm these dependencies
    implementation("androidx.privacysandbox.activity:activity:1.0.0-alpha02")

    // Use to implement privacysandbox activity complications
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-data-source:1.0.0-alpha02"
    // (Kotlin-specific extensions)
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-data-source-ktx:1.0.0-alpha02"

    // Use to implement a activity style and complication editor
    // TODO: Confirm these dependencies
    implementation("androidx.privacysandbox.activity:activity-editor:1.0.0-alpha02")

    // Can use to render complications.
    // TODO: Confirm these dependencies
    // This library is optional and activitys may have custom implementation for rendering
    // complications.
    // TODO: Confirm these dependencies
    implementation "androidx.privacysandbox.activity:activity-complications-rendering:1.0.0-alpha02"
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1116743+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1116743&template=1629474)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha02

March 26, 2025

`androidx.privacysandbox.activity:activity-client:1.0.0-alpha02`,`androidx.privacysandbox.activity:activity-core:1.0.0-alpha02`, and`androidx.privacysandbox.activity:activity-provider:1.0.0-alpha02`are released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..78132378b67c86698d1ade3dc368c9f15d738a71/privacysandbox/activity).

**New Features**

- SDK activity launchers can now be created for lifecycle-unaware activities, i.e. activities that don't implement the`LifecycleOwner`interface. These launchers need to be manually disposed of by the caller.

**API Changes**

- Added`LocalUnmanagedSdkActivityLauncher`and`createUnmanagedSdkActivityLauncher`, a launcher class for lifecycle-unaware activities and a method to create such launchers.
- Renamed`LocalSdkActivityLauncher`to`LocalManagedSdkActivityLauncher`to highlight the distinction between this and lifecycle-unaware type of launchers.

### Version 1.0.0-alpha01

November 15, 2023

`androidx.privacysandbox.activity:activity-client:1.0.0-alpha01`,`androidx.privacysandbox.activity:activity-core:1.0.0-alpha01`, and`androidx.privacysandbox.activity:activity-provider:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c/privacysandbox/activity)

**New Features**

- Introducing a dedicated Privacy Sandbox Activity library.
- It contains interfaces for launching activities from the SDK Runtime. The interfaces were previously defined in the Privacy Sandbox UI library.