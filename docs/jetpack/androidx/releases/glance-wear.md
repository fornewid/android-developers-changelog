---
title: https://developer.android.com/jetpack/androidx/releases/glance-wear
url: https://developer.android.com/jetpack/androidx/releases/glance-wear
source: md.txt
---

# Glance Wear

API Reference  
[androidx.glance.wear](https://developer.android.com/reference/kotlin/androidx/glance/wear/package-summary)  
Glance Wear is a library for building Widgets for Wear OS

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/glance-wear#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on glance-wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.glance.wear:wear:1.0.0-alpha03"

    implementation "androidx.glance.wear:wear-core:1.0.0-alpha03"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.glance.wear:wear:1.0.0-alpha03")

    implementation("androidx.glance.wear:wear-core:1.0.0-alpha03")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1112273+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1112273&template=1623657)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha03

February 11, 2026

`androidx.glance.wear:wear:1.0.0-alpha03` and `androidx.glance.wear:wear-core:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c56b41d38e8ee7017db4bb3446a0598f8d80e378..2e98d140740558dc55710bde96311d2e0e8d5cfd/glance/wear).

**API Changes**

- Add support for Interaction Events to `GlanceWearWidget`. ([Ia4e28](https://android-review.googlesource.com/#/q/Ia4e285fc6cab170b37cb647a2a2749c82d2d347e), [b/469808447](https://issuetracker.google.com/issues/469808447))

### Version 1.0.0-alpha02

January 28, 2026

`androidx.glance.wear:wear:1.0.0-alpha02` and `androidx.glance.wear:wear-core:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/glance/wear).

**New Features**

- Re-map FULLSCREEN to LARGE in Widget params ([ad78d95](https://android.googlesource.com/platform/frameworks/support/+/ad78d95768ffb0c857248b01e2b485cbf1da2282))

**Bug Fixes**

- Fixed usage of DataStore that would prevent multiple widget instances of being shown ([474f3e4](https://android.googlesource.com/platform/frameworks/support/+/474f3e45918122164889e5a04802b7dd000c530e))

### Version 1.0.0-alpha01

January 14, 2026

`androidx.glance.wear:wear:1.0.0-alpha01` and `androidx.glance.wear:wear-core:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/glance/wear).

- Glance Wear is a library for building Widgets for Wear OS using `RemoteCompose`.