---
title: https://developer.android.com/jetpack/androidx/releases/compose-remote-foundation
url: https://developer.android.com/jetpack/androidx/releases/compose-remote-foundation
source: md.txt
---

# Compose Remote Foundation

TODO

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 07, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/compose_remote_foundation#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on compose remote foundation, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

\<!DOCTYPE html\>


compose remote foundation deps

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.remote.foundation:foundation:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.remote.foundation:foundation:1.0.0-alpha04")
}
```


For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component&template)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Foundation

### Version 1.0

#### Version 1.0.0-alpha04

October 07, 2026

`androidx.compose.remote.foundation:foundation:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2b5ae7b0fe1bb4eece7018878fe5f18c5967a2f..dfba882dc7bd28aa4e7febb9c51b9a62fdfb14d0/compose/remote/foundation/foundation).

#### Version 1.0.0-alpha03

September 23, 2026

`androidx.compose.remote.foundation:foundation:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e4bd62f853853bf3522ed15681c58ef28b09ed44..7b7434f12dfb811bb3828261e14cd5c87ce8fa66/compose/remote/foundation/foundation).

**API Changes**

- Added `ImageVector.toRemoteImageVector()` and `RemoteImageVector.vectorResource(@DrawableRes id: Int)` to convert Compose UI `ImageVector` and drawable vector resources to `RemoteImageVector`. ([Ia8383](https://android-review.googlesource.com/#/q/Ia8383096088ccfbf93f17af836cdff9fe34cc7e2))

#### Version 1.0.0-alpha02

September 09, 2026

`androidx.compose.remote.foundation:foundation:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3ed195f0c9ef9eafe437351d974c9ec49ecc2ea..e4bd62f853853bf3522ed15681c58ef28b09ed44/compose/remote/foundation/foundation).

**Bug Fixes**

- `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))

## Compose Remote Foundation

### Version 1.0

#### Version 1.0.0-alpha01

August 26, 2026

The initial release of the `androidx.compose.remote.foundation` library. The Remote Foundation library is designed to contain design system agnostic UI Components for Remote Compose.

`androidx.compose.remote.foundation:foundation:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5790527f572101733cfbe2134e864d98fc1a3377/compose/remote/foundation/foundation).

**API Changes**

- Migrated basic Remote Compose widgets (`RemoteBasicText`, `RemoteBasicImage`, `RemoteSpacer`, `RemoteBasicIcon`) to the new remote-foundation library. ([I259b2](https://android-review.googlesource.com/#/q/I259b24dae1931f3508fba0eb0e40d6068ab82b5c), [b/532028292](https://issuetracker.google.com/issues/532028292))