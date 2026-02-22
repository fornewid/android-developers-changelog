---
title: https://developer.android.com/jetpack/androidx/releases/compose-remote
url: https://developer.android.com/jetpack/androidx/releases/compose-remote
source: md.txt
---

# remote compose

API Reference  
[androidx.compose.remote](https://developer.android.com/reference/kotlin/androidx/compose/remote/package-summary)  
Remote Compose is a framework to create UI for remote surfaces

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/compose-remote#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on compose-remote, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.remote:remote-core:1.0.0-alpha04"

    // Use to create Remote Compose documents
    implementation "androidx.compose.remote:remote-creation:1.0.0-alpha04"
    implementation "androidx.compose.remote:remote-creation-core:1.0.0-alpha04"
    implementation "androidx.compose.remote:remote-creation-android:1.0.0-alpha04"
    implementation "androidx.compose.remote:remote-creation-jvm:1.0.0-alpha04"
    implementation "androidx.compose.remote:remote-creation-compose:1.0.0-alpha04"

    // Use to render a Remote Compose document
    implementation "androidx.compose.remote:remote-player-core:1.0.0-alpha04"
    implementation "androidx.compose.remote:remote-player-view:1.0.0-alpha04"

    implementation "androidx.compose.remote:remote-tooling-preview:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.remote:remote-core:1.0.0-alpha04")

    // Use to create Remote Compose documents
    implementation("androidx.compose.remote:remote-creation:1.0.0-alpha04")
    implementation("androidx.compose.remote:remote-creation-core:1.0.0-alpha04")
    implementation("androidx.compose.remote:remote-creation-android:1.0.0-alpha04")
    implementation("androidx.compose.remote:remote-creation-jvm:1.0.0-alpha04")
    implementation("androidx.compose.remote:remote-creation-compose:1.0.0-alpha04")

    // Use to render a Remote Compose document
    implementation("androidx.compose.remote:remote-player-core:1.0.0-alpha04")
    implementation("androidx.compose.remote:remote-player-view:1.0.0-alpha04")

    implementation("androidx.compose.remote:remote-tooling-preview:1.0.0-alpha04")
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

### Version 1.0.0-alpha04

February 11, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/remote).

**New Features**

- Enable using the `RemoteApplier` by default, which prevents using non-Remote Composable functions when creating a Remote UI. This can be disabled by changing `isRemoteApplierEnabled` in `RemoteComposeCreationComposeFlags`. ([67a405f](https://android-review.googlesource.com/#/q/I10b57b6fee4d9f3cba75be4cab6976123a8c347e))
- Add Glyph spacing for bitmap fonts ([0852657](https://android-review.googlesource.com/#/q/I96311972f59b562c44845860e67c39c8346a826d))
- Rotate with pivot in `RemoteCanvas` ([9a292b3](https://android-review.googlesource.com/#/q/I96311972f59b562c44845860e67c39c8346a826d))
- Add `RemoteSpacer` ([12beb72](https://android-review.googlesource.com/#/q/I603e0995d933a68220fd72b595a42c98329db31a))
- Avoid `java.time` dependency, allowing the `minSdk` of the creation libraries to be lowered to 23 ([59e30d0](https://android-review.googlesource.com/#/q/I7edfc82475f2472673844d9eb5ca0a5214518e2f))
- `FlowLayout` ([7efef02](https://android-review.googlesource.com/#/q/I176532d6d4bddfcf360787f83dcef4b3f0833ef8))

**Bug Fixes**

- Fix evaluation for non global `ColorExpression` and computed String. ([c08d0bd](https://android-review.googlesource.com/#/q/I2085fcf66281fe05f2c37140786c614902ca03d5))

**External Contribution**

- `androidx.compose.ui.graphics.NativePaint` typealias is deprecated, use `android.graphics.Paint` directly instead ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))
- Replace `Paint.asFrameworkPaint()` to `Paint.nativePaint` extension to avoid exposing platform type into `commonMain` sourceset via `typealias` ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))

### Version 1.0.0-alpha03

January 28, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8ae214f288619313e8689cd4ab8286c7705c1000..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/remote).

**New Features**

- Support for different shapes \& `RemoteColors` in `BorderModifier` [0afd343](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3914200)
- Add `CombinedAction` to support multiple actions on click events [10e16a2](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3908363)

**API Changes**

- Migrated the APIs of `RemoteColor` and `RemoteBitmap` to use Compose types, rather than exposing Android types directly [a9bfbb8](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3917393)
- Introduce a `RemoteDensity` type, to allow determining whether to evaluate Density on the Player (when producing a document for a remote device), or to inline the expressions (to optimize document size when on the same device) [54352bb](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3914002)
- `RemoteState constantValueOrNull` rename ([I6ad5c](https://android-review.googlesource.com/#/q/I6ad5caf6e8af50642e3a7696ae7ceeefce89f11f), [b/467050397](https://issuetracker.google.com/issues/467050397))

### Version 1.0.0-alpha02

January 14, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..8ae214f288619313e8689cd4ab8286c7705c1000/compose/remote).

**New Features**

- Add min/max font size for CoreText. [I7bd3c](https://android-review.git.corp.google.com/#/q/I7bd3cbacdfcb70b62feada52cc74ff4853360775)

**API Changes**

- Expose minimal public API for Glance Wear infra. ([I7b4b9](https://android-review.googlesource.com/#/q/I7b4b99bb71b0b874acfbb77cbec7e7ec2eb85403), [b/467532762](https://issuetracker.google.com/issues/467532762))
- Return `CapturedDocument` from `captureSingleRemoteDocument` ([I5a283](https://android-review.googlesource.com/#/q/I5a2832bcd1eb4b54e82a413452d1146565925b81), [b/467532762](https://issuetracker.google.com/issues/467532762))

**Bug Fixes**

- Fix scrolling position after relayout + add support for edge effects ([6d4551](https://android-review.git.corp.google.com/#/q/I5c2d35e07c193d7b147753387eb1d47cc0765be9))

### Version 1.0.0-alpha01

December 17, 2025

`androidx.compose.remote:remote-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3/compose/remote).

- Remote Compose is a framework to create UI for remote surfaces.