---
title: https://developer.android.com/jetpack/androidx/releases/compose-remote-foundation
url: https://developer.android.com/jetpack/androidx/releases/compose-remote-foundation
source: md.txt
---

# Compose Remote Foundation

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| August 26, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/compose_remote_foundation#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on compose remote foundation, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

\<!DOCTYPE html\>


Compose Remote Foundation dependencies

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.remote.foundation:foundation:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.remote.foundation:foundation:1.0.0-alpha01")
}
```


For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2237693+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2237693&template=2382803)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Compose Remote Foundation

### Version 1.0

#### Version 1.0.0-alpha01

August 26, 2026

The initial release of the `androidx.compose.remote.foundation` library. The Remote Foundation library is designed to contain design system agnostic UI Components for Remote Compose.

`androidx.compose.remote.foundation:foundation:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5790527f572101733cfbe2134e864d98fc1a3377/compose/remote/foundation/foundation).

**API Changes**

- Migrated basic Remote Compose widgets (`RemoteBasicText`, `RemoteBasicImage`, `RemoteSpacer`, `RemoteBasicIcon`) to the new remote-foundation library. ([I259b2](https://android-review.googlesource.com/#/q/I259b24dae1931f3508fba0eb0e40d6068ab82b5c), [b/532028292](https://issuetracker.google.com/issues/532028292))