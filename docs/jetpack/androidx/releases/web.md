---
title: https://developer.android.com/jetpack/androidx/releases/web
url: https://developer.android.com/jetpack/androidx/releases/web
source: md.txt
---

# Web

--

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| November 04, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/web#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on web, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.web:web:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.web:web:1.0.0-alpha01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2170315+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2170315&template=2433969)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Web

### Version 1.0

#### Version 1.0.0-alpha01

November 04, 2026

`androidx.web:web:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b4510a0ac49baf283afedaa15ee936afa8a25ff4/web/web).

**API Changes**

- `WebContent`: Introducing a new API to hold a persistent web engine session state that can safely outlive individual UI views or Activities. ([I41397](https://android-review.googlesource.com/#/q/I413973fcf8af9c93f650bf35c7c3c66bd6cf1a87))
- `WebContentView`: Introducing a new specialized `WebView` designed to integrate with `WebContent`. ([I41397](https://android-review.googlesource.com/#/q/I413973fcf8af9c93f650bf35c7c3c66bd6cf1a87))
- `DetachedWebContentView`: A specialized `WebContentView` that `WebContent` attaches to when not attached to an Activity. ([I41397](https://android-review.googlesource.com/#/q/I413973fcf8af9c93f650bf35c7c3c66bd6cf1a87))