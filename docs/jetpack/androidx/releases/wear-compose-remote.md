---
title: https://developer.android.com/jetpack/androidx/releases/wear-compose-remote
url: https://developer.android.com/jetpack/androidx/releases/wear-compose-remote
source: md.txt
---

# Wear Remote Compose Material 3

Write Widgets and other Remote UI for Wear OS using the Material 3 Expressive design system.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| April 08, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/wear-compose-remote#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on wear compose remote, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.wear.compose.remote:remote-material3:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.wear.compose.remote:remote-material3:1.0.0-alpha02")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1984647+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1984647&template=2233909)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha02

April 08, 2026

`androidx.wear.compose.remote:remote-material3:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f1927c2c3b66d0c3a6b9118974d818d2dc5a06a..951845221205b7a428a9d779107760fc929863ee/wear/compose/remote/remote-material3).

**API Changes**

- Expose `RemoteCircularProgressIndicator`, `RemoteProgressIndicatorDefaults`, and `RemoteProgressIndicatorColors` ([I64481](https://android-review.googlesource.com/#/q/I64481ef9b9246f0ef82b863f66f459e4bb8ccee7), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteTitleCard`([Ic65ff](https://android-review.googlesource.com/#/q/Ic65ff71f28387406a153889d8eee162430be5546), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteMaterialTheme` ([I07329](https://android-review.googlesource.com/#/q/I07329a0ac7c5ca82b251023cc9fe53abcd5c002f), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteAppCard` ([Ib6fbc](https://android-review.googlesource.com/#/q/Ib6fbcb4c2b022d89dd48017eabdd6e67edfea423), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteCard`, `RemoteOutlinedCard`, `RemoteCardDefaults`, and `RemoteCardColors` ([I2bcfd](https://android-review.googlesource.com/#/q/I2bcfd467f039e4a81e8221eff34ec851e262f2d8), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteColorScheme` ([Id0e88](https://android-review.googlesource.com/#/q/Id0e8817db6118b89c7728b6f853dbf57f3e8b05a), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteTypography` ([Ib6f88](https://android-review.googlesource.com/#/q/Ib6f880bb885f8fe2723d8176f996af0ad32f8aeb), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteShapes` ([I6c356](https://android-review.googlesource.com/#/q/I6c356b5485ae33a838a2a28e63ba9559d32812ac), [b/492476015](https://issuetracker.google.com/issues/492476015))

**Other Changes**

- Updated Compose `compileSdk` to API 37. This means that a minimum AGP version of 9.2.0 is required when using Compose. ([Id45cd](https://android-review.googlesource.com/#/q/Id45cdca34ef948e06259b2dd9adc901b7c930492), [b/413674743](https://issuetracker.google.com/issues/413674743))

### Version 1.0.0-alpha01

March 25, 2026

`androidx.wear.compose.remote:remote-material3:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1abcb4178d48853948b9b566cabff9222d90ab69/wear/compose/remote/remote-material3).

**API Changes**

- Expose `RemoteTextButton` public APIs. ([I169e3](https://android-review.googlesource.com/#/q/I169e3b2e0c336da4727d00da6d3f0a571061da88), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteIconButton` public APIs. ([Id7c71](https://android-review.googlesource.com/#/q/Id7c71e213914b4c524c465e8277bdd9dfaa923a7), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteButtonGroup` public APIs. ([Ibfc22](https://android-review.googlesource.com/#/q/Ibfc22f7315183805aa0cac158af8e8967d68ec87), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteButton`, `RemoteCompactButton`, `RemoteButtonDefaults` and `RemoteButtonColors` as public APIs ([I3bcdd](https://android-review.googlesource.com/#/q/I3bcdd4d2ed1b43f523eddaba953e8a95aefd2e71), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteIcon` as a public API ([I0cc79](https://android-review.googlesource.com/#/q/I0cc799082b3e90cbe5b218d13d83aaba976330f9), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteText` as public APIs ([I8a11a](https://android-review.googlesource.com/#/q/I8a11a50a46b90acb222ac99cf8bb9e41140fc5b5), [b/492476015](https://issuetracker.google.com/issues/492476015))
- Expose `RemoteFloat.asRemoteDp()` ([I28b36](https://android-review.googlesource.com/#/q/I28b361187b51f6b0b15a5223cd7af98f50270da0), [b/446824085](https://issuetracker.google.com/issues/446824085))