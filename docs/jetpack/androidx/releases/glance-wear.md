---
title: https://developer.android.com/jetpack/androidx/releases/glance-wear
url: https://developer.android.com/jetpack/androidx/releases/glance-wear
source: md.txt
---

# Glance Wear

Glance Wear is a library for building Widgets for Wear OS

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 01, 2026 | - | - | - | [1.0.0-alpha13](https://developer.android.com/jetpack/androidx/releases/glance-wear#1.0.0-alpha13) |

## Declaring dependencies

To add a dependency on glance-wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.glance.wear:wear:1.0.0-alpha13"

    implementation "androidx.glance.wear:wear-core:1.0.0-alpha13"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.glance.wear:wear:1.0.0-alpha13")

    implementation("androidx.glance.wear:wear-core:1.0.0-alpha13")
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

## Glance Wear Version 1.0

### Version 1.0.0-alpha13

July 01, 2026

`androidx.glance.wear:wear:1.0.0-alpha13`, `androidx.glance.wear:wear-core:1.0.0-alpha13`, and `androidx.glance.wear:wear-tooling-preview:1.0.0-alpha13` are released. Version 1.0.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/14c2f2ed81d0f61a3227641684cd875e95dd6529..ba3014c143b9c9782fe30bc766c5dced55e13453/glance/wear).

**API Changes**

- Removed the permission check from `heartRateAccuracy` ([I14269](https://android-review.googlesource.com/#/q/I14269c1e05223e2b3b851749b40cf24b61e6be15), [b/522444636](https://issuetracker.google.com/issues/522444636))

**Bug fixes**

- We have tweaked the Squircle shaped Wear widget params for preview per UX feedback

### Version 1.0.0-alpha12

June 17, 2026

`androidx.glance.wear:wear:1.0.0-alpha12`, `androidx.glance.wear:wear-core:1.0.0-alpha12`, and `androidx.glance.wear:wear-tooling-preview:1.0.0-alpha12` are released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3fad9a116191a476216752005ae5752c236e4faf..14c2f2ed81d0f61a3227641684cd875e95dd6529/glance/wear).

**New features**

- **Added `AssociateWithGlanceWearWidget` that *must* be used on the `GlanceWearWidgetService` to provide which implementation of `GlanceWearWidget` it is associated to.** ([Ifcabb](https://android-review.googlesource.com/#/q/Ifcabb316a0dc3fcd5fc0d5a5878fe8ad281ed8ad), [b/514679763](https://issuetracker.google.com/issues/514679763))

  - For example:

       @AssociateWithGlanceWearWidget(MyGlanceWearWidget::class)
       class MyGlanceWearWidgetService : GlanceWearWidgetService() {
         override val widget = MyGlanceWearWidget()
       }
       ```

- We have added `image` brush to `WearWidgetBrush` to support bitmap backgrounds in Wear Widgets. ([I9a228](https://android-review.googlesource.com/#/q/I9a22801ae1d5e5d5fe473a51b153f3e0e8e97312), [b/513481558](https://issuetracker.google.com/issues/513481558))

- We have introduced a `@Composable` helper function, `WearWidgetPreview`, to simplify the development of Glance Wear widgets by removing the boilerplate required for IDE previews.

**API Changes**

- Renamed `androidx.glance.wear.health.DataType` to `androidx.glance.wear.health.HealthData` ([I4cb0b](https://android-review.googlesource.com/#/q/I4cb0b961829680053b1611b153d0c5ce9f5dcb0c), [b/516746689](https://issuetracker.google.com/issues/516746689))
- `isHeartRateBpmAvailable` is exposed to determine if `heartRateBpm` is available on the host. ([I5999d](https://android-review.googlesource.com/#/q/I5999d40f4cd432e921a7b10ecdff67d566f0d06c), [b/514641567](https://issuetracker.google.com/issues/514641567))
- Exposed `RemoteInt` compare operators. ([I5fe3d](https://android-review.googlesource.com/#/q/I5fe3d4e06e25650003dcea04cdef1c252612bf06), [b/513228889](https://issuetracker.google.com/issues/513228889))
- Exposed `captureRemoteDocument` Flow API and a new `captureSingleRemoteDocument` overload (which takes `RemoteCreationDisplayInfo`) as public APIs. ([I87b0e](https://android-review.googlesource.com/#/q/I87b0ef46ca9cbaae9375053ab8d0618921aa1957), [b/513228889](https://issuetracker.google.com/issues/513228889))
- We have added `@CallSuper` to `GlanceWearWidgetService` lifecycle methods

### Version 1.0.0-alpha11

June 03, 2026

`androidx.glance.wear:wear:1.0.0-alpha11`, `androidx.glance.wear:wear-core:1.0.0-alpha11`, and `androidx.glance.wear:wear-tooling-preview:1.0.0-alpha11` are released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b5d2acb5ad0a36c9d2aba8feb4c7951165f30fbe..59d7db8fc3c97056707d1f7a4b415c80d9a8688a/glance/wear).

**API Changes**

- We have added `WearWidgetPreview` for previewing Wear Widgets in Android Studio. ([I36504](https://android-review.googlesource.com/#/q/I36504163576c4869ecd67732321dc7535edf3467), [b/485147770](https://issuetracker.google.com/issues/485147770))
- Expose `is*Available` (`isDailyStepsAvailable`, etc.) variables to verify if the related health data type is available and valid. ([Ib98a7](https://android-review.googlesource.com/#/q/Ib98a78eec469c425b2ab8f3b231e9fae562437e0), [b/498179656](https://issuetracker.google.com/issues/498179656))
- Added `triggerUpdateAll` API to `GlanceWearWidget` to trigger update on all widgets of the given app. ([I6ab20](https://android-review.googlesource.com/#/q/I6ab20fe37b23d531d38c622e31acdbe4e1b83f3c), [b/510896410](https://issuetracker.google.com/issues/510896410))

**Bug Fixes**

- Include Renderer version information in the `WearWidgetParams` as internal field to prevent breakage in the document generated with the alpha10 version. ([Idcf8e](https://android-review.googlesource.com/#/q/Idcf8e6e180db390b74d2b283920d1f81dfb797b2), [b/511263591](https://issuetracker.google.com/issues/511263591), [b/512830184](https://issuetracker.google.com/issues/512830184))
- Trigger force pull update flow in debug mode or emulator for Wear Widgets.

### Version 1.0.0-alpha10

May 19, 2026

`androidx.glance.wear:wear:1.0.0-alpha10`, `androidx.glance.wear:wear-core:1.0.0-alpha10`, and `androidx.glance.wear:wear-tooling-preview:1.0.0-alpha10` are released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e29a10982f4299b1fa812e229d76792092a62814..376d4304794a4ceb62b09f6b61dd88688bda018d/glance/wear).

**API Changes**

- Expose `glance.wear.health.DataType` APIs in Wear Widget. These APIs can be used by developers to access system health data.

**Bug Fixes**

- Fixed a crash loop happening in the *alpha09* version on Wear 7 emulator or devices running 1.6 renderer by not allowing empty font axis to be send to the Player for Glance Wear Widget.

### Version 1.0.0-alpha09

May 06, 2026

`androidx.glance.wear:wear:1.0.0-alpha09` and `androidx.glance.wear:wear-core:1.0.0-alpha09` are released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/df4b49eda6f6834b6bc4c8aa30a581fa577a511e..7115d2ecdb44b1d7d55e95cae78fa4736ee25d13/glance/wear).

**API Changes**

- We have added `ExperimentalGlanceWearApi` which will be used for experimental Glance Wear features. ([Id2f76](https://android-review.googlesource.com/#/q/Id2f764bcb6fc427eb0e013e76e7554b172bc9f43), [b/498179813](https://issuetracker.google.com/issues/498179813))

**Bug Fixes**

- Updated the parser for Wear Widget XML metadata to be aware of widgets during boot.

### Version 1.0.0-alpha08

April 22, 2026

`androidx.glance.wear:wear:1.0.0-alpha08` and `androidx.glance.wear:wear-core:1.0.0-alpha08` are released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/951845221205b7a428a9d779107760fc929863ee..df4b49eda6f6834b6bc4c8aa30a581fa577a511e/glance/wear).

**Bug Fixes**

- Added `<queries>` tag to the manifest of `glance:wear:wear` library to make sure the `PackageManager` queries the correct services for push updates. ([I192787](https://android-review.googlesource.com/#/q/I192787bae1d03dcd83c824e30a010e2ce7ea514c))

**Other**

- Reverted "Updates Compose compileSdk to 37" ([I6007](https://android-review.googlesource.com/#/q/I60078d5774b303651921c5c0a26ab0cf7ce09205)) which also applies to glance-wear, so the compileSdk requirement is no longer 37 in this release.

### Version 1.0.0-alpha07

April 08, 2026

`androidx.glance.wear:wear:1.0.0-alpha07` and `androidx.glance.wear:wear-core:1.0.0-alpha07` are released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f1927c2c3b66d0c3a6b9118974d818d2dc5a06a..4c9e6b44e0f35c9a0595abec3ba2fd139900c25d/glance/wear).

**New Features**

- Add default Wear Widget background when `WearWidgetBrush` is empty or not specified. ([I8300b](https://android-review.googlesource.com/#/q/I8300b8047772ed0bcafbc0d37cd0da8e0307ad88))
- Update `getActiveWidgets` API to return the Container Type of the Widget. ([2772eb1](https://android-review.googlesource.com/#/q/I9383b031feccedbc967e25bd54acc055d968555e))

**API Changes**

- Change Widget update API to take `WidgetInstanceId` and add helper for fetching IDs for a given widget. The new api throws `IllegalArgumentException` if the provided id is invalid or not owned by the caller. ([I6f3c5](https://android-review.googlesource.com/#/q/I6f3c5d0fe4d2e7fa94fecfa3333eb6fa7b424779), [b/446828899](https://issuetracker.google.com/issues/446828899))
- Add vertical and horizontal gradient in `WearWidgetBrush`. ([If70ae](https://android-review.googlesource.com/#/q/If70ae449194e0c30c43053cdbcd7ed8fed3d6fdb), [b/470080675](https://issuetracker.google.com/issues/470080675))

### Version 1.0.0-alpha06

March 25, 2026

`androidx.glance.wear:wear:1.0.0-alpha06` and `androidx.glance.wear:wear-core:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a508f033de883ba2853b9f9ae1853eec7010638..fe367de0a74244126fbc65fbf03d56061fb84f79/glance/wear).

**New Features**

- Define the operations for Wear Widgets profile inline.

**API Changes**

- We have renamed `CONTAINER_TYPE_FULLSCREEN` to `CONTAINER_TYPE_TILE_COMPAT` to better differentiate fullscreen compatibility widget. This includes reverting of mapping previously `FULLSCREEN` type to `LARGE` in Widget params.

### Version 1.0.0-alpha05

March 11, 2026

`androidx.glance.wear:wear:1.0.0-alpha05` and `androidx.glance.wear:wear-core:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6e23fc0c137022098ae2d043778ffdc56402ba5e..1a508f033de883ba2853b9f9ae1853eec7010638/glance/wear).

**API Changes**

- We have added `WearWidgetBrush`API with the `color` method to be used for the Wear Widget background. ([I66f54](https://android-review.googlesource.com/#/q/I66f54dde07793ac7a00c48d374ec04824b9b3858), [b/464273091](https://issuetracker.google.com/issues/464273091))
- `fetchActiveWidgetsForProvider` method has been removed as there is already `fetchActiveWidgets`. ([I85e4e](https://android-review.googlesource.com/#/q/I85e4e22abd2144a97e4b2765f285c204bbe0c2ab), [b/486197890](https://issuetracker.google.com/issues/486197890))

### Version 1.0.0-alpha04

February 25, 2026

`androidx.glance.wear:wear:1.0.0-alpha04` and `androidx.glance.wear:wear-core:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..6e23fc0c137022098ae2d043778ffdc56402ba5e/glance/wear).

**API Changes**

- Added `GlanceWearWidgetManager` API for allowing Apps to query their active widgets and tiles. ([I5be95](https://android-review.googlesource.com/#/q/I5be95954c759493c4bf978b812e5a5e53daf6394))
- We have moved APIs from the `glance:wear:wear-core` library into the `androidx.glance.wear.core` package. ([I429cf](https://android-review.googlesource.com/#/q/I429cf4c36d27bc8fc01115194b20806f10950dde))

**Bug Fixes**

- Expose common Remote Composable and Modifier types ([Id1d40](https://android-review.googlesource.com/#/q/Id1d40acae7af63f9acb99438adaa992035fd3c01))

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