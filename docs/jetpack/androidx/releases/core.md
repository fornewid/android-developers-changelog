---
title: https://developer.android.com/jetpack/androidx/releases/core
url: https://developer.android.com/jetpack/androidx/releases/core
source: md.txt
---

# Core

[Code Sample](https://github.com/android/user-interface-samples/tree/main/Notifications) API Reference  
[androidx.core.animation](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary)  
[androidx.core.app](https://developer.android.com/reference/kotlin/androidx/core/app/package-summary)  
[androidx.core.content](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary)  
[androidx.core.role](https://developer.android.com/reference/kotlin/androidx/core/role/package-summary)  
[androidx.core.view](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary)  
(*See the refdocs for all core packages*) Target the latest platform features and APIs while also supporting older devices.


This table lists all the artifacts in the `androidx.core` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| core | [1.17.0](https://developer.android.com/jetpack/androidx/releases/core#1.17.0) | [1.18.0-rc01](https://developer.android.com/jetpack/androidx/releases/core#1.18.0-rc01) | - | - |
| core-animation | [1.0.0](https://developer.android.com/jetpack/androidx/releases/core#core-animation-1.0.0) | - | - | - |
| core-google-shortcuts | [1.1.0](https://developer.android.com/jetpack/androidx/releases/core#core-google-shortcuts-1.1.0) | - | - | [1.2.0-alpha01](https://developer.android.com/jetpack/androidx/releases/core#core-google-shortcuts-1.2.0-alpha01) |
| core-performance | [1.0.0](https://developer.android.com/jetpack/androidx/releases/core#1.0.0) | - | - | - |
| core-remoteviews | [1.1.0](https://developer.android.com/jetpack/androidx/releases/core#core-remoteviews-1.1.0) | - | - | - |
| core-role | [1.1.0](https://developer.android.com/jetpack/androidx/releases/core#core-role-1.1.0) | - | - | - |
| core-splashscreen | [1.2.0](https://developer.android.com/jetpack/androidx/releases/core#core-splashscreen-1.2.0) | - | - | - |

This library was last updated on: February 11, 2026

## Declaring dependencies

To add a dependency on Core, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    def core_version = "1.17.0"

    // Java language implementation
    implementation "androidx.core:core:$core_version"
    // Kotlin
    implementation "androidx.core:core-ktx:$core_version"

    // To use RoleManagerCompat
    implementation "androidx.core:core-role:1.1.0"

    // To use the Animator APIs
    implementation "androidx.core:core-animation:1.0.0"
    // To test the Animator APIs
    androidTestImplementation "androidx.core:core-animation-testing:1.0.0"

    // Optional - To enable APIs that query the performance characteristics of GMS devices.
    implementation "androidx.core:core-performance:1.0.0"

    // Optional - to use ShortcutManagerCompat to donate shortcuts to be used by Google
    implementation "androidx.core:core-google-shortcuts:1.1.0"

    // Optional - to support backwards compatibility of RemoteViews
    implementation "androidx.core:core-remoteviews:1.1.0"

    // Optional - APIs for SplashScreen, including compatibility helpers on devices prior Android 12
    implementation "androidx.core:core-splashscreen:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    val core_version = "1.17.0"

    // Java language implementation
    implementation("androidx.core:core:$core_version")
    // Kotlin
    implementation("androidx.core:core-ktx:$core_version")

    // To use RoleManagerCompat
    implementation("androidx.core:core-role:1.1.0")

    // To use the Animator APIs
    implementation("androidx.core:core-animation:1.0.0")
    // To test the Animator APIs
    androidTestImplementation("androidx.core:core-animation-testing:1.0.0")

    // Optional - To enable APIs that query the performance characteristics of GMS devices.
    implementation("androidx.core:core-performance:1.0.0")

    // Optional - to use ShortcutManagerCompat to donate shortcuts to be used by Google
    implementation("androidx.core:core-google-shortcuts:1.1.0")

    // Optional - to support backwards compatibility of RemoteViews
    implementation("androidx.core:core-remoteviews:1.1.0")

    // Optional - APIs for SplashScreen, including compatibility helpers on devices prior Android 12
    implementation("androidx.core:core-splashscreen:1.2.0")
}
```

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460834+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460834&template=1418393)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Core-Pip Version 1.0

### Version 1.0.0-alpha02

February 11, 2026

`androidx.core:core-pip:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c4e491baa54e95e632dbbac0df9b66a7e62ad17f..2e98d140740558dc55710bde96311d2e0e8d5cfd/core/core-pip).

**New Features**

- Added `BasicPictureInPicture` and `VideoPlaybackPictureInPicture` to streamline standard implementations. The new `VideoPlaybackPictureInPicture` class allows the library to handle view-bounds tracking automatically, ensuring smoother visual transitions.

**API Changes**

- Remove the `onViewBoundsChanged` API ([Ie56d0](https://android-review.googlesource.com/#/q/Ie56d0c9472eee965067a9f598a8225ea5df7aaef), [b/475328144](https://issuetracker.google.com/issues/475328144))
- Add `BasicPictureInPicture` and `VideoPlaybackPictureInPicture` classes for typical PiP usages ([I7f989](https://android-review.googlesource.com/#/q/I7f9895dd5a0c6a5853dda519faf0ac62a4f9d5c1), [b/475328144](https://issuetracker.google.com/issues/475328144))

**Bug Fixes**

- Add `ViewBoundsTracker` class to continuously track the view bounds for setting `sourceRectHint` in `PictureInPictureParamsCompat`. ([Id203a](https://android-review.googlesource.com/#/q/Id203aa25cb63addc6585c6eb721d99e5b195177b), [b/474454111](https://issuetracker.google.com/issues/474454111))

### Version 1.0.0-alpha01

January 14, 2026

`androidx.core:core-pip:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c4e491baa54e95e632dbbac0df9b66a7e62ad17f/core/core-pip).

**New Features**

The PiP Jetpack library is introduced to address several challenges in Android's Picture-in-Picture (PiP) mode:

- OS Fragmentation: The library handles differences in PiP API calls across Android versions, such as `enterPictureInPictureMode` before Android S and `isAutoEnterEnabled` after.
- Incorrect PiP Parameters: It provides a unified solution for setting correct PiP parameters, especially for playback, to ensure smooth animations (e.g., source rect hint).
- Fragmented PiP State Callbacks: The library consolidates `onPictureInPictureModeChanged` and `onPictureInPictureUiStateChanged` into a single, unified callback interface for simplified state management.

**API Changes**

- `PictureInPictureDelegate` class that helps setup PiP (Picture-in-Picture) functionalities on behalf of the given `PictureInPictureProvider` instance ([8cf9588](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3857454)).
- `PictureInPictureDelegate.onPictureInPictureEvent` interface that provides a unified callback for application to listen on Picture-in-Picture events ([8cf9588](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3857454)).

**Bug Fixes**

- Add `PictureInPictureParamsValidator` class to validate the app provided `PictureInPictureParamsCompat` ([I89b4d](https://android-review.googlesource.com/#/q/I89b4d813f42c42687eb10bb45005f6765c210990), [b/470149490](https://issuetracker.google.com/issues/470149490))
- A dedicated `:core:core-pip` library is introduced to help app developers implementing the Android PiP (Picture-in-Picture) feature ([I8ebc5](https://android-review.googlesource.com/#/q/I8ebc5081a0067d80f1ae9e01578e36370a71be1a), [b/462178249](https://issuetracker.google.com/issues/462178249))

## Core-Backported-Fixes Version 1.0

### Version 1.0.0

December 17, 2025

`androidx.core:core-backported-fixes:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/39e25369b3a6dd0b08038933f4c1b15af324b339..6d6d409113492a342806d502d7572e4dcf8c6ad1/core/core-backported-fixes).

### Version 1.0.0-rc01

December 03, 2025

`androidx.core:core-backported-fixes:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9b6dee951e595dec2015b7b31a9591a22f7ea265..41c6d4700dc6c688a8090d524343e85d4aa57ac3/core/core-backported-fixes).

**Bug Fixes**

- Fix the code links in documentation for KI_452390376 ([I9a554](https://android-review.googlesource.com/#/q/I9a554376ca3be01cc6a79cda3349d0d4fb23c070), [b/454020407](https://issuetracker.google.com/issues/454020407))

### Version 1.0.0-beta02

November 05, 2025

`androidx.core:core-backported-fixes:1.0.0-beta02` is released. Version 1.0.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..9b6dee951e595dec2015b7b31a9591a22f7ea265/core/core-backported-fixes).

**API Changes**

- Add known issue b/452390376 ([Auto Exposure Mode Low Light Boost (LLB)](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY)) cannot be enabled for stream use cases such as VIDEO_CALL on Pixel 10 devices. ([Iba480](https://android-review.googlesource.com/#/q/Iba4803d52c9c93b88694aceb7d218b4c7a0e77f0), [b/452390376](https://issuetracker.google.com/issues/452390376))

**Bug Fixes**

- Mark specific pixel builds as fixed. ([I4c751](https://android-review.googlesource.com/#/q/I4c7519189c6fd1a792333925e0a1bd3cbb37c712), [b/398591036](https://issuetracker.google.com/issues/398591036))
- Add support for specifying a list of manually tested build fingerprints for a KnownIssue. ([Iea9f9](https://android-review.googlesource.com/#/q/Iea9f9f14a4c81a66689552d59ecaf2b41f02c494), [b/453691379](https://issuetracker.google.com/issues/453691379))

### Version 1.0.0-beta01

September 24, 2025

`androidx.core:core-backported-fixes:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dc350c93c84573d65395b944c310a27620091120..3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a/core/core-backported-fixes).

### Version 1.0.0-alpha01

August 13, 2025

`androidx.core:core-backported-fixes:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dc350c93c84573d65395b944c310a27620091120/core/core-backported-fixes).

**New Features**

- The Core Backported Fixes library lets you check if a critical bug fix has been applied to a device. This is useful because it can take a long time for bug fixes to be rolled out to all devices, and this API provides a way for you to know when it is safe to use features that depend on a fix.

      val fixManager = BackportedFixManager()
          if (fixManager.isFixed(KnownIssues.KI_1234)) {
            Offer_experience_that_needs_fix()
          } else {
            Offer_experience_that_avoids_the_bug()
        }

This release includes

- [`KnownIssues.KI_398591036`](https://developer.android.com/reference/androidx/core/backported/fixes/KnownIssues#KI_398591036()): Abnormal color tone when capturing `JPEG-R` images on some Pixel devices. Fix by using `JPEG` outputs until this KI is resolved.

## Core-Viewtree Version 1.0

### Version 1.0.0

February 26, 2025

`androidx.core:core-viewtree:1.0.0` has been promoted to its first stable release with no changes since its previous RC version.

This library introduces the concept of a View being able to have a disjoint parent. A disjoint parent of a view is a separate `View` object that acts as the view's parent, but is not set via the `View.parent` property. Examples of Views with disjoint parents are `ViewOverlays`, popups, and dialogs, which all appear outside of the main view hierarchy. A View can only have a disjoint parent if it does not have a direct parent via the platform's `View.parent` property. Currently, androidx only sets the disjoint parent for `ViewOverlays` created by [Transition `1.6.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/transition#1.6.0-alpha01) and higher. You can also specify your own disjoint parents for views. See the documentation for more information.

### Version 1.0.0-rc01

February 12, 2025

`androidx.core:core-viewtree:1.0.0-rc01` is released with no changes since the beta.

### Version 1.0.0-beta01

January 29, 2025

`androidx.core:core-viewtree:1.0.0-beta01` is released with no changes since the alpha. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..d70c42c692a5ce230394b651ac975fc7d03519c8/core/core-viewtree).

### Version 1.0.0-alpha01

December 11, 2024

`androidx.core:core-viewtree:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6/core/core-viewtree).

**New Features**

- Initial release of `core-viewtree`, transitively exposed by androidx core.

- This initial release introduces the concept of a View being able to have a disjoint parent. A disjoint parent of a view is a separate `View` object that acts as the view's parent, but is not set via the `View.parent` property. Examples of Views with disjoint parents are `ViewOverlays`, popups, and dialogs, which all appear outside of the main view hierarchy. A View can only have a disjoint parent if it does not have a direct parent via the platform's `View.parent` property. Currently, androidx only sets the disjoint parent for `ViewOverlays` created by transition. You can also specify your own disjoint parents for views. See the documentation for more information.

**API Changes**

- Adds `ViewParent.getParentOrViewTreeDisjointParent()` and `ViewParent.setViewTreeDisjointParent(View, ViewParent?)` methods ([Ib2950](https://android-review.googlesource.com/#/q/Ib295041b91c759b403d01fd9cb46bb189549a104))

## Core-i18n Version 1.0

### Version 1.0.0

April 9, 2025

`androidx.core:core-i18n:1.0.0` is released.

The component makes it easier to create properly internationalized applications, focusing on two main areas:

- Date and time formatting functionality following the best current practices, honoring user custom settings, and providing a unifying API that works properly on old and new Android versions.
- A backport of [`android.icu.text.MessageFormat`](https://developer.android.com/reference/android/icu/text/MessageFormat) that works on older APIs. But still useful on new Android versions because it integrates the date / time formatting mentioned above. That honors the user settings, which `android.icu.text.MessageFormat` does not do.

The component will be the vehicle to backporting new i18n APIs, adding new i18n functionality or fixes, and in general making internationalization easier.

### Version 1.0.0-rc01

March 26, 2025

`androidx.core:core-i18n:1.0.0-rc01` is released with no notable changes since the last beta. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8870a8ee99ec618927a9edb4b6e74b8570381149..207ad46672dec4dc2d1e8c2442e936f5b89b9b0b/core/core-i18n).

### Version 1.0.0-beta01

March 12, 2025

`androidx.core:core-i18n:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..8870a8ee99ec618927a9edb4b6e74b8570381149/core/core-i18n).

**New Features**

- This is the first release of the `core-i18n` component. The component makes it easier to create properly internationalized applications, focusing on two main areas:
  - Date and time formatting functionality following the best current practices, honoring user custom settings, and providing a unifying API that works properly on old and new Android versions.
  - A backport of [`android.icu.text.MessageFormat`](https://developer.android.com/reference/android/icu/text/MessageFormat) that works on older APIs. But still useful on new Android versions because it integrates the date / time formatting mentioned above. That honors the user settings, which `android.icu.text.MessageFormat` does not do.
  - The component will be the vehicle to backporting new i18n APIs, adding new i18n functionality or fixes, and in general making internationalization easier.

### Version 1.0.0-alpha01

July 26, 2023

`androidx.core:core-i18n:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313/core/core-location-altitude)

## Core-location-altitude Version 1.0.

### Version 1.0.0-beta01

November 05, 2025

`androidx.core:core-location-altitude:1.0.0-beta01`, `androidx.core:core-location-altitude-external-protobuf:1.0.0-beta01`, and `androidx.core:core-location-altitude-proto:1.0.0-beta01` are released with no notable changes since the last alpha. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..b7446a78657b91b088b062544628faaf3c5a5582/core).

### Version 1.0.0-alpha03

October 16, 2024

`androidx.core:core-location-altitude:1.0.0-alpha03`, `androidx.core:core-location-altitude-external-protobuf:1.0.0-alpha03`, and `androidx.core:core-location-altitude-proto:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..b8a68b0896897fa158508d73a31998a26161d9a7/core).

**Security fix**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on `androidx.core:core-location-altitude-proto`and `androidx.core:core-location-altitude-external-protobuf` to 1.1.0-alpha03 to address the vulnerability risk.

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ieb9ae](https://android-review.googlesource.com/#/q/Ieb9aecd2af5587c5b82833146fee6e912693ab7b), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.0.0-alpha02

June 12, 2024

`androidx.core:core-location-altitude:1.0.0-alpha02`, `androidx.core:core-location-altitude-external-protobuf:1.0.0-alpha02`, and `androidx.core:core-location-altitude-proto:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b/core).

**Bug Fixes**

- Fixes proguard failure caused by the repackaging of proto libraries.

**External Contribution**

- Bug fix above provided by andrekir@pm.me

### Version 1.0.0-alpha01

July 26, 2023

`androidx.core:core-i18n:1.0.0-alpha01` and `androidx.core:core-location-altitude:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313/core/core-location-altitude)

**New Features**

- Added `AltitudeConverterCompat` class with a single static method `addMslAltitudeToLocation(Context, Location)` ([I11168](https://android.googlesource.com/platform/frameworks/support/+/340afce6e1887c3322e839fe311748580bdd517c)).

## Core-telecom Version 1.1

### Version 1.1.0-alpha03

February 11, 2026

`androidx.core:core-telecom:1.1.0-alpha03` is released. Version 1.1.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f5e69af57ade617fcc3ab8b81eaa75d72916276..d70b7e8d1b45adbfec4334c6db491905b0b6534e/core/core-telecom).

**New Features**

- **Opt-out of Premium Network Slicing:** Introduced a new capability, `CAPABILITY_OPT_OUT_OF_PREMIUM_NETWORK`, in `CallsManager`. This allows VoIP applications to signal that they wish to opt-out of the system's default behavior of requesting premium network slices for voice and video calls. By default, the system may automatically request a premium network slice to improve call quality. This capability can be passed during `registerAppWithTelecom`. ([I2dfdb](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3885722))
- **Control Microphone Mute Capability:** Added APIs to allow VoIP apps to inform remote surfaces (like Android Auto, wearables) whether the user should be able to control the microphone state. This is useful in scenarios where the user is restricted from changing their mute state, such as being in a moderated meeting, joining as a passive viewer, or using Companion Mode. ([I55acf](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3872444))

**API Changes**

- Added `CallsManager.CAPABILITY_OPT_OUT_OF_PREMIUM_NETWORK`: Use this flag with `registerAppWithTelecom(int)` to prevent the system from automatically requesting premium network capabilities. `kotlin
  val callsManager = CallsManager(context)
  // Register with Telecom, opting out of premium network requests callsManager.registerAppWithTelecom(CallsManager.CAPABILITY_OPT_OUT_OF_PREMIUM_NETWORK)`
- `onCanUserUpdateSilence` is now an optional ([Ibb0c2](https://android-review.googlesource.com/#/q/Ibb0c2f91ee510704d38f1fc7f8620e5475bac9bb))
- Add APIs to inform surfaces on whether the mic should be shown or not ([I55acf](https://android-review.googlesource.com/#/q/I55acff5d35fdfff83d4bba83fc7adcd97d826c05))

**Bug Fixes**

- Fixed a `NullPointerException` in `JetpackConnectionService` caused by a race condition when accessing pending connection requests. This was resolved by switching to a `CopyOnWriteArrayList` for thread-safe iterations. ([I24306](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3858239))
- Corrected an issue in the Meeting Summary extension where a literal string "null" was emitted instead of a true `null` value for the current speaker. ([Idae9a](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3890913))

### Version 1.1.0-alpha01

October 8th, 2025

`androidx.core:core-telecom:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://googleplex-android.googlesource.com/platform/frameworks/support/+/d14695b2d4f8520f39b9d2089f1de48d99ac1e27).

**New Features**

- Added the ability for applications to request that a specific call not be saved in the system call log, even if the app has generally opted into call logging. This feature is only effective on devices running `Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.BAKLAVA_1`.

**API Changes**

- Introduced the optional `isLogExcluded` Boolean property to the `CallAttributesCompat` data class. Setting this to true requests the system to exclude the call from the call log. On older platform versions, this property has no effect. Please note that VoIP calls are not logged to the system call log by default. Developers must first explicitly opt-in their application to participate in system call logging. This requires declaring an intent handler for `android.telecom.action.CALL_BACK` in the app's manifest. The new `isLogExcluded` property provides a per-call exclusion option for apps that have already enabled this integration. ([d14695](https://googleplex-android.googlesource.com/platform/frameworks/support/+/d14695b2d4f8520f39b9d2089f1de48d99ac1e27))

## Core-telecom Version 1.0.

### Version 1.0.1

August 27, 2025

`androidx.core:core-telecom:1.0.1` is released. Version 1.0.1 is a bug-fix release that includes the following improvements which can be found in the [these commits](https://android.googlesource.com/platform/frameworks/support/+log/74f25b8b4e5983806db47125f343cb9f08eaa2e9..40e5626dcdec536576fecb4158c54e929329f682/core/core-telecom).

**Bug Fixes**

- Audio Routing and Endpoint Handling
  - Resolved an issue where a user's selected pre-call audio endpoint (e.g., Earpiece) would be incorrectly switched to Speaker when a video call starts. The library now ensures the user's preferred audio route is maintained. ([8fa4ba7](https://android.googlesource.com/platform/frameworks/support/+/8fa4ba7643d7ed03002da528a965952da94e1a54), [71d7be8](https://android.googlesource.com/platform/frameworks/support/+/71d7be876fa581cf746522ad67b6025eb322e942))
  - Improved the audio switching logic to prevent calls from automatically switching from Bluetooth headset to Speaker, especially when the Bluetooth device takes a moment to connect. This check requires the BLUETOOTH_CONNECT permission to differentiate between device types.([de83f3e](https://android.googlesource.com/platform/frameworks/support/+/de83f3ea42b9ef590c16dcd4ffeff85f7bc90c1f))
  - Optimized the auto-speaker functionality for video calls for users without Bluetooth devices. The library now performs a less intrusive check for Bluetooth devices before requesting the BLUETOOTH_CONNECT permission, improving the experience for non-Bluetooth users. ([721f4e2](https://android.googlesource.com/platform/frameworks/support/+/721f4e2e03ae9f304be58cd835c8757d7068b947))
- Stability and Crash Fixes
  - Fixed `NullPointerException` crashes that could occur during audio endpoint processing. The library now correctly handles inconsistent state management in `PreCallEndpointsUpdater` and filters null elements from the system's `AudioDeviceInfo` array to improve stability. ([23dd075](https://android.googlesource.com/platform/frameworks/support/+/23dd0751f76d709cafb0110a75cd7c988d59011c), [03eb616](https://android.googlesource.com/platform/frameworks/support/+/03eb616249d1803fe7d1abf1249132c58d04c71a))

### Version 1.0.0

May 7, 2025

`androidx.core:core-telecom:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bb8fdda78902ccbcb2fa68a04d02e52ce8f424ba..74f25b8b4e5983806db47125f343cb9f08eaa2e9/core/core-telecom).

**Major features of 1.0.0**

- Initial stable release of core-telecom API, focusing on `CallsManager` API surface for integration of VoIP calls into the Android platform.

### Version 1.0.0-rc01

April 9, 2025

`androidx.core:core-telecom:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..bb8fdda78902ccbcb2fa68a04d02e52ce8f424ba/core/core-telecom).

**New Features**

New experimental API call extensions. The new experimental extensions added in this release are:

- Support for a Meeting Summary Remote Extension, allowing a remote surface to receive meeting summary information (current speaker and participant count) from the connected VoIP application. ([7cf095f](https://android.googlesource.com/platform/frameworks/support/+/7cf095f23e31d90c04dcc4738e53528a2b7a1833))
- Support for a Call Icon Extension that allows a VoIP app to send an Icon Uri to a remote `InCallService` (auto, watch face, etc.). The Icon can be updated throughout the call and can have the same URI value. ([8e1813e](https://android.googlesource.com/platform/frameworks/support/+/8e1813ebb18a7104fe85c0e8884f0c5ffd029ca4))

### Version 1.0.0-beta01

December 11, 2024

`androidx.core:core-telecom:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..46295bc0b75a16f452e8e0090e8de41073d4dbb6/core/core-telecom).

**New Features**

Beta release for the following new features:

- Fetching available audio endpoints before a call is added. App developers can now display all the available endpoints before initiating a call which allows users to seamlessly select their preferred audio endpoint and optimize their setup. This eliminates the need for in-call adjustments at the start of the call, providing a smoother experience.
- Experimental API support for VOIP application call extensions. Call extensions allow an application to provide more details about an ongoing call, such as the list of participants in a group call or meeting. Supported remote surfaces such as Android Auto can then show this information to the user and allow them to interact with the supported extensions. The new experimental extensions added in this release are:
  - Support for showing the participants in a group call or meeting and describing which participant is active. Support for the following optional actions on participants:
    - Raising and lowering the hands of participants.
    - Kicking participants.
  - Support for call silence, which allows remote surfaces to silence a VOIP call without also globally muting the mic.

**API Changes**

- Rename `addLocalSilenceExtension` to `addLocalCallsilenceExtension` ([If4a9c](https://android-review.googlesource.com/#/q/If4a9cd364e72e9280fabddfe35a09e4a3f38cc73))
- Change `preferredStartingCallEndpoint`from `var` to `val`. ([Iab6b7](https://android-review.googlesource.com/#/q/Iab6b75ce5c3c729a8582a27a112ab1c3119b5949))
- Add local call silence APIs ([I29dd0](https://android-review.googlesource.com/#/q/I29dd0df846a3e075d8469e1e066c93516264a028))
- Implement the `compareTo` function for the `CallEndpointCompat` class ([Ia06b7](https://android-review.googlesource.com/#/q/Ia06b71919ac067bd77d22d7751fb9992d54c1b8b))
- Adds experimental app actions API. ([Ifb796](https://android-review.googlesource.com/#/q/Ifb796f222bc58126867dc8486b26a51ddcf226f8))
- Add new `CallsManager` API `getAvailableStartingCallEndpoints` ([Ia8bcf](https://android-review.googlesource.com/#/q/Ia8bcf70d3a8e6c9f6a96d96bdd12204aabfff3df))
- Update `ExperimentalAppActions` annotation to ensure that it is accurately tracking all usages of the experimental feature. ([Id5ea5](https://android-review.googlesource.com/#/q/Id5ea546ca3d9bb2f2904882b712e423cea04e1db))

**Bug Fixes**

- Add global mute state receiver for Android API level 28 through 33. ([I75e66](https://android-review.googlesource.com/#/q/I75e6671a62e44825fbb1eea25e6756ec8125b7bb))
- Fixes an issue where only the latest connected `InCallService` would be able to send action events ([I39599](https://android-review.googlesource.com/#/q/I39599e2b65e54fd43bdee97254a2d43c1825b1cb))
- Implements ICS Extensions API for voip app actions. ([I1274c](https://android-review.googlesource.com/#/q/I1274ca5cc898b0bd20ad90a1b97ee0ae8c90861b))
- Rejecting a call before API level 34 will now correctly destroy the call in Telecom. ([I635b7](https://android-review.googlesource.com/#/q/I635b7b3667afe7d00ce9d68515f55833c4840a72))
- `addCall` now properly throws Exceptions through the API instead of the parent coroutine ([I83334](https://android-review.googlesource.com/#/q/I83334efe4aa28bd3f1e6e1a23056d84bd841929a))
- Add a placeholder value to extras bundle ([Iebf7f](https://android-review.googlesource.com/#/q/Iebf7fdfb5bab35ec429dabb093d351868ca3edcc))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ieb9ae](https://android-review.googlesource.com/#/q/Ieb9aecd2af5587c5b82833146fee6e912693ab7b), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Adds experimental support for extensions to `CallsManager#addCall`. ([I24d92](https://android-review.googlesource.com/#/q/I24d9281b2e837b5f7480901d35216d15cd23e4a5))
- Core-Telecom will now throw a `CallException` if the platform failed to add the call due to an exception, reaching max call count, etc. ([I41f27](https://android-review.googlesource.com/#/q/I41f27f24423e0c735f2ff2c4d203a07674877b9b))

### Version 1.0.0-alpha03

April 17, 2024

`androidx.core:core-telecom:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..67004410fdbff19f90caa4cc43965ab21dca1943/core/core-telecom).

**Bug Fixes**

- Refactor of `JetpackConnectionService` to correct an issue which occurs on SDK 33 and below when the address passed in is empty. The refactored `JetpackConnectionService` is also resilient to unexpected NULL values from Telecom platform APIs.
- Improvements to `addCall/CallControlScope` API documentation.
- Test reliability improvements.

### Version 1.0.0-alpha02

October 4, 2023

`androidx.core:core-telecom:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ab43e1b522d2e81d0bf105d62a8e22edadd70b61..1f7407d4293384a1b91bc142880e3525048b3443/core/core-telecom)

**API Changes**

- Revamped the API signatures for methods that returned boolean to indicate success/failure to instead return a result class that clearly indicates why an operation succeeded or failed.
- Moved the `CallControlCallback` methods as lambda args to `addCall` to remove the need to explicitly provide a callback in the call scope.

**Bug Fixes**

- Fixed a bug in the `ConnectionService` compatibility layer which would have resulted in no call audio when running against pre-U SDKs.
- Improve API documentation.

### Version 1.0.0-alpha01

May 10, 2023

`androidx.core:core-telecom:1.0.0-alpha01` is released. This version is developed in an internal branch and should be used with Android 14 Beta 2.

**New Features**

- Introduces the `CallsManager` API which VoIP apps can use for integrating with the Telecom framework on a device. Calls notified to the platform benefit from foreground execution priority, visibility on Bluetooth, wearable and automotive devices, and simplified audio routing.

  The `CallsManager` API wraps the legacy `ConnectionService` API for devices running older versions of Android.

## Core and Core-ktx Version 1.18

### Version 1.18.0-rc01

February 11, 2026

`androidx.core:core:1.18.0-rc01`, `androidx.core:core-ktx:1.18.0-rc01`, and `androidx.core:core-testing:1.18.0-rc01` are released. Version 1.18.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..c1ae034f11f1bbd8ddc06914b65e0440f1d1f0cc/core).

**API Changes**

- Remove the `onViewBoundsChanged` API ([Ie56d0](https://android-review.googlesource.com/#/q/Ie56d0c9472eee965067a9f598a8225ea5df7aaef), [b/475328144](https://issuetracker.google.com/issues/475328144))
- Add `BasicPictureInPicture` and `VideoPlaybackPictureInPicture` classes for typical PiP usages ([I7f989](https://android-review.googlesource.com/#/q/I7f9895dd5a0c6a5853dda519faf0ac62a4f9d5c1), [b/475328144](https://issuetracker.google.com/issues/475328144))

**Bug Fixes**

- Add `ViewBoundsTracker` class to continuously track the view bounds for setting `sourceRectHint` in `PictureInPictureParamsCompat` ([Id203a](https://android-review.googlesource.com/#/q/Id203aa25cb63addc6585c6eb721d99e5b195177b), [b/474454111](https://issuetracker.google.com/issues/474454111))

### Version 1.18.0-alpha01

January 14, 2026

`androidx.core:core:1.18.0-alpha01`, `androidx.core:core-ktx:1.18.0-alpha01`, and `androidx.core:core-testing:1.18.0-alpha01` are released. Version 1.18.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5b1ab05399538aabe876833906e112a6f2fe4a04..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/core).

**API Changes**

- Add support for `getBoundingRects` in `WindowInsetsCompat` ([I24f18](https://android-review.googlesource.com/#/q/I24f18de869d6873961b759b8810bf1eda453d6bd))
- `onCanUserUpdateSilence` is now an optional ([Ibb0c2](https://android-review.googlesource.com/#/q/Ibb0c2f91ee510704d38f1fc7f8620e5475bac9bb))
- Extend `PictureInPictureProvider` interface to include also `OnUserLeaveHintProvider` ([I3125b](https://android-review.googlesource.com/#/q/I3125bc52082135d8da6a0a4d1275a5e0f7099604), [b/462178249](https://issuetracker.google.com/issues/462178249))
- Deprecated `PermissionsDelegateCompat.onActivityResult` which is no longer called by `FragmentActivity`. ([I59197](https://android-review.googlesource.com/#/q/I59197adc49b7725ffd289c3cb891615db0a1b99c), [b/460267600](https://issuetracker.google.com/issues/460267600))
- Abstract the Picture-in-Picture functions from `ComponentActivity` into a dedicated `PictureInPictureProvider` interface ([I068a3](https://android-review.googlesource.com/#/q/I068a39994a10b6a46a86c39dbe822f014e2c1e58), [b/462178249](https://issuetracker.google.com/issues/462178249))
- Add APIs to inform surfaces on whether the mic should be shown or not ([I55acf](https://android-review.googlesource.com/#/q/I55acff5d35fdfff83d4bba83fc7adcd97d826c05), [b/445237449](https://issuetracker.google.com/issues/445237449))
- Add `DisplayShapeCompat` APIs ([I490d4](https://android-review.googlesource.com/#/q/I490d440e80996aaf6a38bfd3499f473104bf5cac), [b/410851992](https://issuetracker.google.com/issues/410851992))
- `PictureInPictureParamsCompat` is introduced to wrap the framework `android.app.PictureInPictureParams` class. ([I8af9e](https://android-review.googlesource.com/#/q/I8af9e031886985e3fc1d19f6a019d5eef5eb4230), [b/458803858](https://issuetracker.google.com/issues/458803858))
- Add support for `IntentSender` into androidx-main am: 127eef7acc am: b4b1111b77 ([I5b30b](https://android-review.googlesource.com/#/q/I5b30b2d64fc5a239d84bbda5c5dcc5c3d9f08fdd))
- Add support for `IntentSender` into androidx-main am: 127eef7acc ([I849b9](https://android-review.googlesource.com/#/q/I849b975224ab69b9daa49ce6be22dc553c17c7f1))
- Add support for `IntentSender` into androidx-main
- Add support for `IntentSender` ([Ia998d](https://android-review.googlesource.com/#/q/Ia998d8afc5e52523f190aaf0c092c67bb9440c31), [b/445163724](https://issuetracker.google.com/issues/445163724))
- Add new APIs to get and set selection ([I05ec4](https://android-review.googlesource.com/#/q/I05ec4efb82a22cfa2994d1470bfbe5ca5d5a22f1), [b/362784540](https://issuetracker.google.com/issues/362784540))
- Add known issue 452390376 [Auto Exposure Mode Low Light Boost (LLB)](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY) cannot be enabled for stream use cases such as VIDEO_CALL on Pixel 10 devices. ([Iba480](https://android-review.googlesource.com/#/q/Iba4803d52c9c93b88694aceb7d218b4c7a0e77f0), [b/452390376](https://issuetracker.google.com/issues/452390376))
- Add new APIs to get and set sort direction ([I658de](https://android-review.googlesource.com/#/q/I658defcf8e0489fe98821132cb373f013a465219), [b/394670064](https://issuetracker.google.com/issues/394670064))
- Added new APIs to `CallControlScope` for video call management: `getVideoState()` to observe audio/video state and `requestVideoState(int)` to request changes to the video state. ([I51065](https://android-review.googlesource.com/#/q/I510657e4ebad6bc72c920543ee0e560e3f0984f9), [b/333074774](https://issuetracker.google.com/issues/333074774))
- Add missing `AccessibilityNodeInfoCompat` checked state constants. ([I40b4c](https://android-review.googlesource.com/#/q/I40b4cecf074bdbf59aecf3cbeb2fc72222a69816))
- Fix bug for missing `AccessibilityNodeInfoCompat` expanded state intdef. ([I75106](https://android-review.googlesource.com/#/q/I751062808f426881529f90dc4f83d08fcbc9351d), [b/435252704](https://issuetracker.google.com/issues/435252704))
- `BuildCompat.isAtLeastB1`: remove `@RequiresApi` ([I42fe2](https://android-review.googlesource.com/#/q/I42fe25f4ff83de690822bbd43eb433aa57fc9139), [b/430210979](https://issuetracker.google.com/issues/430210979))
- Fix bug for missing `AccessibilityNodeInfoCompat` expanded state constants. ([I1b1cd](https://android-review.googlesource.com/#/q/I1b1cdf122b3cffd61b105779b61e03835cc9048d), [b/435252704](https://issuetracker.google.com/issues/435252704))
- `CallsManager.registerAppWithTelecom` now includes a new optional `backwardsCompatSdkLevel` parameter. This gives developers control over which underlying platform implementation (legacy `ConnectionService` vs. modern transactional APIs) is used. The value defaults to 33, ensuring modern APIs are used by default on SDK 34+, but can be set higher to force the legacy path on specific SDK ranges. ([Ib9571](https://android-review.googlesource.com/#/q/Ib9571c205b36308ddaa588bde066e1b7c2d4dd79), [b/444266242](https://issuetracker.google.com/issues/444266242))
- Added `CallAttributesCompat.isLogExcluded` to allow specifying whether a call should be excluded from the call log ([Ia2a3a](https://android-review.googlesource.com/#/q/Ia2a3a86b05f70c4a4313a84031607cbee356011d), [b/447166999](https://issuetracker.google.com/issues/447166999))
- Add missing content change types. ([I52a3c](https://android-review.googlesource.com/#/q/I52a3cf40ed6bd0778d323f9a40f6154aaf247798))
- Add `BuildCompat.isAtLeastB1` for checking if an API added in Baklava, minor release 1 (SDK 36.1) is available. ([I78513](https://android-review.googlesource.com/#/q/I785134e8332bbeea7896112920fa1cf412a34a89), [b/430210979](https://issuetracker.google.com/issues/430210979))
- Introducing new API `RangingResultFailure` to report ranging session failure and reason, Ranging Initiation failure will also use `RangingResultFailure` callback previously reported through `RangingResultPeerDisconnected`
- Introducing new API `RangingResultFailure` to report ranging session failure and reason, Ranging Initiation failure will also use `RangingResultFailure` callback previously reported through `RangingResultPeerDisconnected` ([If3715](https://android-review.googlesource.com/#/q/If3715e45a59635b8196b983b6e80e67591c6c5f9))
- Deprecated the `bundleOf(...)` extension function, which does not provide compile time type safety and may lead to crashes at run time. Instead, use `Bundle` methods directly. ([I48af2](https://android-review.googlesource.com/#/q/I48af27ae6420cb8ca244465cab485f8b88375d03), [b/434825212](https://issuetracker.google.com/issues/434825212))

**Bug Fixes**

- Add the Pixel Dec release to the list of fixed build fingerprints in KI_398591036 ([I65f51](https://android-review.googlesource.com/#/q/I65f51f92c528ca7483476bb5ab9d0f0e7f603ca1), [b/398591036](https://issuetracker.google.com/issues/398591036))
- Add the Pixel Nov release to the list of fixed build fingerprints in KI_398591036 ([I60c10](https://android-review.googlesource.com/#/q/I60c10c18a5cbe68a2a5aaa45aae6caf314de0179), [b/398591036](https://issuetracker.google.com/issues/398591036))
- Add the Pixel Oct release to the list of fixed build fingerprints in KI_398591036 ([I6438c](https://android-review.googlesource.com/#/q/I6438cbd8db15b8ad545eff1c3b492385a1002a5f), [b/398591036](https://issuetracker.google.com/issues/398591036))
- Removed references to `FingerprintManager` class from `FingerprintManagerCompat` and updated all methods to return false or no-op. ([I0360b](https://android-review.googlesource.com/#/q/I0360b3ef856865097df80d3d98953978d1e86de7), [b/330524057](https://issuetracker.google.com/issues/330524057))
- Fix the code links in documentation for KI_452390376 ([I9a554](https://android-review.googlesource.com/#/q/I9a554376ca3be01cc6a79cda3349d0d4fb23c070), [b/454020407](https://issuetracker.google.com/issues/454020407))
- Mark specific pixel builds as fixed. ([I4c751](https://android-review.googlesource.com/#/q/I4c7519189c6fd1a792333925e0a1bd3cbb37c712), [b/398591036](https://issuetracker.google.com/issues/398591036))
- Add support for specifying a list of manually tested build fingerprints for a `KnownIssue`. ([Iea9f9](https://android-review.googlesource.com/#/q/Iea9f9f14a4c81a66689552d59ecaf2b41f02c494), [b/453691379](https://issuetracker.google.com/issues/453691379))

## Core and Core-ktx Version 1.17

### Version 1.17.0

August 13, 2025

`androidx.core:core:1.17.0`, `androidx.core:core-ktx:1.17.0`, and `androidx.core:core-testing:1.17.0` are released. Version 1.17.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a974e3bf6f579209fd28bf9d49838ce4951bf7e2..5b1ab05399538aabe876833906e112a6f2fe4a04/core).

**Important changes since 1.16.0**

- Core library has been updated to target Kotlin 2.0 language level and requires use of Kotlin Gradle Plugin 2.0.0 or newer.

### Version 1.17.0-rc01

July 30, 2025

`androidx.core:core:1.17.0-rc01`, `androidx.core:core-ktx:1.17.0-rc01`, and `androidx.core:core-testing:1.17.0-rc01` are released. Version 1.17.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..a974e3bf6f579209fd28bf9d49838ce4951bf7e2/core) since the previous beta release.

### Version 1.17.0-beta01

July 2, 2025

`androidx.core:core:1.17.0-beta01`, `androidx.core:core-ktx:1.17.0-beta01`, and `androidx.core:core-testing:1.17.0-beta01` are released. Version 1.17.0-beta01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/47d093c4befba4a57515b333d4d423429253286f..1b437892629a2cdedb46d9b7232575987b2cc6b5/core) since the previous alpha version.

### Version 1.17.0-alpha01

June 18, 2025

`androidx.core:core:1.17.0-alpha01`, `androidx.core:core-ktx:1.17.0-alpha01`, and `androidx.core:core-testing:1.17.0-alpha01` are released. Version 1.17.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/096ee90dd35920496448ba4b5c14f3979bcfee47..47d093c4befba4a57515b333d4d423429253286f/core).

**New Features**

- Core library has been updated to target Kotlin 2.0 language level and requires use of Kotlin Gradle Plugin 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

**API Changes**

- Added `NotificationCompat.ProgressStyle` and `NotificationCompat.Builder.setRequestPromotedOngoing()`. See [Progress centric notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications) and [Live Updates](https://developer.android.com/develop/ui/views/notifications/live-update)
  for details.

- Added `Parcel.use` extension function for safe handling of `Parcel` resources. ([I436da](https://android-review.googlesource.com/#/q/I436da7bab59f43b3b0b8216612e769b52c0a3a99))

## Core and Core-ktx Version 1.16

### Version 1.16.0

April 9, 2025

`androidx.core:core:1.16.0`, `androidx.core:core-ktx:1.16.0`, and `androidx.core:core-testing:1.16.0` are released. Version 1.16.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bce9701663354e1ae98c908ef1b02571e36afb03..096ee90dd35920496448ba4b5c14f3979bcfee47/core).

**Important changes since 1.15.0**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf3e1](https://android-review.googlesource.com/#/q/Iaf3e1d955e754d15c6b69b9fb397aad4b54aaf96), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.16.0-rc01

March 26, 2025

`androidx.core:core:1.16.0-rc01`, `androidx.core:core-ktx:1.16.0-rc01`, and `androidx.core:core-testing:1.16.0-rc01` are released. Version 1.16.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..bce9701663354e1ae98c908ef1b02571e36afb03/core) from the previous beta release.

### Version 1.16.0-beta01

March 12, 2025

`androidx.core:core:1.16.0-beta01`, `androidx.core:core-ktx:1.16.0-beta01`, and `androidx.core:core-testing:1.16.0-beta01` are released. Version 1.16.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d70c42c692a5ce230394b651ac975fc7d03519c8..7a145e052ae61e272e91ffe285e9451b8ab71870/core).

**API Changes**

- Refine insets protection APIs ([I7050d](https://android-review.googlesource.com/#/q/I7050ddde9a472ddfe48805f269f31f3eb87545a0))
- Adds new key to get character bounds in unmagnified window coordinates. ([If7a06](https://android-review.googlesource.com/#/q/If7a06f564f9909739538a674ecc40a4f1cf7e84b))
- Add new boolean property to represent if an `AccesibilityNodeInfo` represents a required field. ([I4fd2d](https://android-review.googlesource.com/#/q/I4fd2df6e2c931299670a4bb97083537a59463600))
- Backport `View.transformMatrixToGlobal` to `ViewCompat` ([If17e2](https://android-review.googlesource.com/#/q/If17e2c1fdad140ba4d8bab4d9ac123b0e94f1eb4))

### Version 1.16.0-alpha02

January 29, 2025

`androidx.core:core:1.16.0-alpha02`, `androidx.core:core-ktx:1.16.0-alpha02`, and `androidx.core:core-testing:1.16.0-alpha02` are released. Version 1.16.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..d70c42c692a5ce230394b651ac975fc7d03519c8/core).

**API Changes**

- Add `BuildCompat.isAtLeastB` for checking if an API added in Baklava is available ([I0f89c](https://android-review.googlesource.com/#/q/I0f89cbe91f8d81345cc9b495232e0f01f81d1890))
- Add an experimental API to get a list of built-in displays. ([Idda4d](https://android-review.googlesource.com/#/q/Idda4df3fe041858760b6fc2933fdc7546b61e3fa))
- Add a set of APIs related to ensuring system bar contrast ([I9849c](https://android-review.googlesource.com/#/q/I9849c8cecab425d353375064e6a7e07cc8bb4b82))

**Bug Fixes**

- Fix issue where `getLaunchDisplayId()` returned an incorrect default value of 0 on SDK \< 26. ([Icd679](https://android-review.googlesource.com/#/q/Icd679df4d9df330cd75deafc5c1a5f81429c444c))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf3e1](https://android-review.googlesource.com/#/q/Iaf3e1d955e754d15c6b69b9fb397aad4b54aaf96), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.16.0-alpha01

December 11, 2024

`androidx.core:core:1.16.0-alpha01`, `androidx.core:core-ktx:1.16.0-alpha01`, and `androidx.core:core-testing:1.16.0-alpha01` are released. Version 1.16.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9cb5997d32284d4f93d768acd1c74775fd8683f..46295bc0b75a16f452e8e0090e8de41073d4dbb6/core).

**API Changes**

- Added `setLaunchDisplayId` to `ActivityOptionsCompat`. ([I39e77](https://android-review.googlesource.com/#/q/I39e773972f9f91b6f970c542740a61486197a3cc), [b/379669743](https://issuetracker.google.com/issues/379669743))
- Added compat API for `SYSTEM_OVERLAYS`. ([Ibd1fd](https://android-review.googlesource.com/#/q/Ibd1fd4a28dae7ccdc3193f1afcfac7b097265d71), [b/287470173](https://issuetracker.google.com/issues/287470173))
- Added `OutcomeReceiverCompat`, a version of Android's `OutcomeReceiver` available on all API levels. ([Ib8265](https://android-review.googlesource.com/#/q/Ib82652305f6dd0aab5e9598dbfc13a397ab0f367), [b/380060342](https://issuetracker.google.com/issues/380060342))
- Added compat class for `android.view.ScrollFeedbackProvider`. ([Icaa92](https://android-review.googlesource.com/#/q/Icaa92df0d4abf1c6997b910a59e552bf27006e09))
- Added `ViewCompat.addViewOverlay(View)` as an alternative to `View.getOverlay().add(View)`. The `ViewCompat` variant fixes an issue where owners like the `LifecycleOwner` and `ViewModelStoreOwner` could not be resolved between the view being overlaid and the overlay owner. ([I81413](https://android-review.googlesource.com/#/q/I81413883e41e56e5ea76372debbd5b012c345f20))
- Introduces the concept of a `View` being able to have a disjoint parent. A disjoint parent of a view is a different view that effectively parents the other view, but is not set via the `View.parent` property. See the documentation for more information. ([Ib2950](https://android-review.googlesource.com/#/q/Ib295041b91c759b403d01fd9cb46bb189549a104))
- Added a new API `ViewGroupCompat#installCompatInsetsDispatch` for developers to fix an insets dispatching issue present prior to API 30. ([I11159](https://android-review.googlesource.com/#/q/I111590881991b94e5cd5f2100bf88dd4468bc781))
- Added `FontsContractCompat.TypefaceStyle` IntDef for annotating `Typeface` styles in `FontsContractCompat`. ([Ib3e5b](https://android-review.googlesource.com/#/q/Ib3e5be8259ac48eac43b3a5618f32cd67e047afc))

**External Contribution**

- Deprecated `BuildCompat.isAtLeastV`. Callers should check `SDK_INT` against 35 directly instead. Thanks to Jake Wharton! ([I294d1](https://android-review.googlesource.com/#/q/I294d117a8fea924e7f1b739d52268a9a54be6db7))
- Added a mutability flag to `TaskStackBuilder`. Thanks to Kamal Faraj! ([Ife0ec](https://android-review.googlesource.com/#/q/Ife0ec30e6c08d6ed56781cdb58a722a6c1f6b6c1), [b/371534781](https://issuetracker.google.com/issues/371534781))

## Core and Core-ktx Version 1.15

### Version 1.15.0

October 30, 2024

`androidx.core:core:1.15.0`, `androidx.core:core-ktx:1.15.0`, and `androidx.core:core-testing:1.15.0` are released. Version 1.15.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6aea9073ec1dde97639f8e7e617b1a0abd3176ae..f9cb5997d32284d4f93d768acd1c74775fd8683f/core).

**Important changes since 1.14.0**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ieb9ae](https://android-review.googlesource.com/#/q/Ieb9aecd2af5587c5b82833146fee6e912693ab7b), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Various updates to compatibility classes for parity with Android 15 SDK.

### Version 1.15.0-rc01

October 16, 2024

`androidx.core:core:1.15.0-rc01`, `androidx.core:core-ktx:1.15.0-rc01`, and `androidx.core:core-testing:1.15.0-rc01` are released. Version 1.15.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/488540191ae5d26a91fb9d37f3c081c77f8dd4a7..6aea9073ec1dde97639f8e7e617b1a0abd3176ae/core) since the previous release.

### Version 1.15.0-beta01

October 2, 2024

`androidx.core:core:1.15.0-beta01`, `androidx.core:core-ktx:1.15.0-beta01`, and `androidx.core:core-testing:1.15.0-beta01` are released. Version 1.15.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b2638e1bfd54531dae1f04b33829101af8bf350..488540191ae5d26a91fb9d37f3c081c77f8dd4a7/core).

**API Changes**

- Added `itemCount` and `importantForAccessibilityItemCount` fields to `CollectionInfoCompat`. ([Ibaf34](https://android-review.googlesource.com/#/q/Ibaf349887f2c40ba63cd8b38033050953b96204b))

**Bug Fixes**

- Fix documentation issues in `androidx.core.os.Profiling` ([I2542f](https://android-review.googlesource.com/#/q/I2542f0d8c61c3475990e570b52810ee988b705da))

### Version 1.15.0-alpha02

August 21, 2024

`androidx.core:core:1.15.0-alpha02`, `androidx.core:core-ktx:1.15.0-alpha02`, and `androidx.core:core-testing:1.15.0-alpha02` are released. Version 1.15.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4b0206986a60b7647e83f56df70756f23e5760d6..6b2638e1bfd54531dae1f04b33829101af8bf350/core).

**Important changes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ieb9ae](https://android-review.googlesource.com/#/q/Ieb9aecd2af5587c5b82833146fee6e912693ab7b), [b/345472586](https://issuetracker.google.com/issues/345472586))

**API Changes**

- Added `fallbackQuery` XML attribute to downloadable font definitions, allowing character-level fallback with downloadable fonts. ([Idd544](https://android-review.googlesource.com/#/q/Idd5449c07ede206b5a27e6553b5340dc16588347))
- Adds helper APIs for using `ProfilingManager` ([If2292](https://android-review.googlesource.com/#/q/If22927ac53ca54bcb294240f90c44ccf7ed01f1d))
- Add compat method for `ActivityOptions.setPendingIntentBackgroundActivityStartMode` ([I3ba1f](https://android-review.googlesource.com/#/q/I3ba1f4174f3a098e64aa255db50567bd76e3fbe5), [b/349617674](https://issuetracker.google.com/issues/349617674))
- Added `DisplayCutoutCompat.getCutoutPath` ([I58778](https://android-review.googlesource.com/#/q/I58778bb5c23837304fb5130644f9f4412884cdc2), [b/279635904](https://issuetracker.google.com/issues/279635904))
- Reverts deprecation of `ParcelCompat.writeBoolean` and delegates to the platform API on API level 29 and above. ([I9d243](https://android-review.googlesource.com/#/q/I9d2436d90f3cbe3bf22e2a3c97171f39b53cf040), [b/313834577](https://issuetracker.google.com/issues/313834577))
- Create `FontsContractCompat.requestFonts` that takes executors ([I03016](https://android-review.googlesource.com/#/q/I0301600d9a3c2f5062631d59105e42ad51bb4754), [b/302377512](https://issuetracker.google.com/issues/302377512))
- Reverts deprecation of `LocationCompat.isMock` and delegates to the platform API on API level 31 and above. ([I55940](https://android-review.googlesource.com/#/q/I559407ae8f2cce149cd2802322485f1b80cb85c9), [b/313834577](https://issuetracker.google.com/issues/313834577))
- Notifications can now be tagged as voicemail. ([I068ab](https://android-review.googlesource.com/#/q/I068aba00fe41ff34ceef18ad0ff43f60b30f18c9))

### Version 1.15.0-alpha01

June 12, 2024

`androidx.core:core:1.15.0-alpha01`, `androidx.core:core-ktx:1.15.0-alpha01`, and `androidx.core:core-testing:1.15.0-alpha01` are released. This version is developed in an internal branch and is compatible with Android 15 Beta 3 (`android-35`).

**API Changes**

- Various updates to compatibility classes for parity with Android 15 SDK.

## Core and Core-ktx Version 1.14

### Version 1.14.0-alpha01

May 1, 2024

`androidx.core:core:1.14.0-alpha01`, `androidx.core:core-ktx:1.14.0-alpha01`, and `androidx.core:core-testing:1.14.0-alpha01` are released. Version 1.14.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342/core).

**New Features**

- Move to 21 as the default `minSdkVersion` of androidx libraries ([I6ec7f](https://android-review.googlesource.com/#/q/I6ec7f80aafbe04c64c8f2d8fef82d4cd5c68525e))

**API Changes**

- Deprecate additional obsolete compat methods. ([Ie4470](https://android-review.googlesource.com/#/q/Ie44708f1423037d74b64aadb7418182a6a1dc089), [b/313834577](https://issuetracker.google.com/issues/313834577))
- Deprecated obsolete compat methods. ([I01d90](https://android-review.googlesource.com/#/q/I01d9076d4ef7b12614b233f8b0b3e147e97b8221), [b/313834577](https://issuetracker.google.com/issues/313834577))
- Updated `isAtLeastV()` to return true for finalized V SDK. ([I6339a](https://android-review.googlesource.com/#/q/I6339a600b8d9d38354c5a14834ed1a0e4c8d5cf9))

## Core and Core-ktx Version 1.13

### Version 1.13.1

May 1, 2024

`androidx.core:core:1.13.1`, `androidx.core:core-ktx:1.13.1`, and `androidx.core:core-testing:1.13.1` are released. Version 1.13.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3736d67a292f282220cadaf57500a052fd47ab4f..3be294a272164cf1920219d3e09cbabfefeb1de6/core).

**Bug Fixes**

- Fix issue where when handwriting toolbar is shown, a finger tap can't switch to the regular keyboard ([I7f843](https://android-review.googlesource.com/#/q/I7f843fc051358a4a522ef367317198c68a94e14c), [b/332769437](https://issuetracker.google.com/issues/332769437))

### Version 1.13.0

April 17, 2024

`androidx.core:core:1.13.0`, `androidx.core:core-ktx:1.13.0`, and `androidx.core:core-testing:1.13.0` are released. Version 1.13.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d304505e537b27e0e5da6b0d923c80ce7d85496a..3736d67a292f282220cadaf57500a052fd47ab4f/core).

**Important changes since 1.12.0**

- The library's `minSdkVersion` has been raised to `19`. Many compatibility APIs have been marked deprecated since they were only needed prior to API level 19.
- Several classes have been rewritten in Kotlin to provide better interoperability with Kotlin consumers while preserving Java compatibility.
- Removed `FingerprintManagerCompat`, which is a no-op starting in Android V and should not be used on earlier platforms. Clients should migrate to `BiometricPrompt` immediately.
- Added `PathParser`, which can create a Path instance from SVG path strings.

### Version 1.13.0-rc01

April 3, 2024

`androidx.core:core:1.13.0-rc01`, `androidx.core:core-ktx:1.13.0-rc01`, and `androidx.core:core-testing:1.13.0-rc01` are released. Version 1.13.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..d304505e537b27e0e5da6b0d923c80ce7d85496a/core).

**Bug Fixes**

- Fix retrieving initial system bar appearance on API 30+ ([I18596](https://android-review.googlesource.com/#/q/I1859688c4d89fa7c365eb420fb1646af0b7cd7db), [b/219993701](https://issuetracker.google.com/issues/219993701))

### Version 1.13.0-beta01

March 20, 2024

`androidx.core:core:1.13.0-beta01`, `androidx.core:core-ktx:1.13.0-beta01`, and `androidx.core:core-testing:1.13.0-beta01` are released. Version 1.13.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..a57d7d17753695012b58c9ce7ad55a8d39157e62/core).

**API Changes**

- `PathParser` is now `final`, `interpolatePathDataNodes` now throws an exception for incompatible arguments instead of returning a `boolean`, and `nodesToPath` now belongs to `PathParser` rather than `PathParser.PathDataNode`. ([I20d62](https://android-review.googlesource.com/#/q/I20d624307bd376de9ba89d1c8b623cb56bcca580))
- `FingerprintManagerCompat` has been soft-removed prior to its removal from the Android V platform SDK. The implementation will be replaced with a no-op in the near future, and developers should migrate away from this class immediately. ([I7ca1b](https://android-review.googlesource.com/#/q/I7ca1bea5c91171a5534a40ebe0acc8bd46454b82))
- The `Pool` interface and its subclasses, `SimplePool` and `SynchronizedPool` are now written in Kotlin. The generic type of objects being stored in the Pool must now be non-null. ([I08afe](https://android-review.googlesource.com/#/q/I08afe319e60db7fa645665464b61d0ad069cbf0a))

**External Contribution**

- `GestureDetectorCompat` is now deprecated as `GestureDetector` is guaranteed to be available in the platform at the library's minimum SDK version. Thanks to Jake Wharton for the contribution. ([Icc4cd](https://android-review.googlesource.com/#/q/Icc4cd9df0b358863ac36d059dc6b997775321be6))
- `MarginLayoutParamsCompat` is now deprecated as `MarginLayoutParams` is guaranteed to be available in the platform as the library's minimum SDK version. Thanks to Jake Wharton for the contribution. ([I4e0c3](https://android-review.googlesource.com/#/q/I4e0c3644a1c0c8c8a820e3a3e90b1c6d05d717f3))

### Version 1.13.0-alpha05

February 7, 2024

`androidx.core:core:1.13.0-alpha05`, `androidx.core:core-ktx:1.13.0-alpha05`, and `androidx.core:core-testing:1.13.0-alpha05` are released. [Version 1.13.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..ca2a8cf8da3a3502fccc593974f8085653e38261/core)

**External Contribution**

- Thanks to Matthew Zavislak for updating the `ContextCompat.registerReceiver` documentation for correctness. ([8fd733](https://android.googlesource.com/platform/frameworks/support/+/8fd733189a41fcc1a494c7c3cffb2c253f56e157))

### Version 1.13.0-alpha04

January 24, 2024

`androidx.core:core:1.13.0-alpha04`, `androidx.core:core-ktx:1.13.0-alpha04`, and `androidx.core:core-testing:1.13.0-alpha04` are released. [Version 1.13.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/core)

**New Features**

- Added `AlarmManagerCompat.canScheduleExactAlarms` API ([I62e95](https://android-review.googlesource.com/#/q/I62e957be392889a944d0c575f26fff12abd590a6), [b/315440583](https://issuetracker.google.com/issues/315440583))

**Kotlin Conversions**

- The `androidx.core.util.Consumer` class has been rewritten in Kotlin and now enforce that the generic type `T` now matches the nullability of what the `accept()` method receives. ([Ie21e0](https://android-review.googlesource.com/#/q/Ie21e0fdf7843c799a5cbcbcccde31e0770e6b3c1))
- `androidx.core.util.Supplier` has been converted to Kotlin, ensuring that the nullability of the type returned by `get()` matches the nullability of the generic type. ([I21e9c](https://android-review.googlesource.com/#/q/I21e9c034265b53520c5a0cb02922ef4b4032cd04))
- `androidx.core.util.Function` has been rewritten in Kotlin, ensuring that the nullability of the input and outputs of the function match the generic types used. ([I09dd7](https://android-review.googlesource.com/#/q/I09dd7d5c40ec90dae252e7befa22e557263a14ec))

**External Contribution**

- Thanks to Kamal Faraj for adding the `AlarmManagerCompat.canScheduleExactAlarms` API ([I62e95](https://android-review.googlesource.com/#/q/I62e957be392889a944d0c575f26fff12abd590a6), [b/315440583](https://issuetracker.google.com/issues/315440583))

### Version 1.13.0-alpha03

January 10, 2024

`androidx.core:core:1.13.0-alpha03`, `androidx.core:core-ktx:1.13.0-alpha03`, and `androidx.core:core-testing:1.13.0-alpha03` are released. [Version 1.13.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/core)

**API Changes**

- Deprecated `ListViewCompat`, use `ListView` directly. ([Iacce6](https://android-review.googlesource.com/#/q/Iacce6ec53b838502cfbfea2fc1f08f6f8e37303f), [b/318353933](https://issuetracker.google.com/issues/318353933))
- Deprecated `ViewCompat.LAYOUT_DIRECTION_` APIs. ([I51710](https://android-review.googlesource.com/#/q/I5171051c40ebe77a9ac6690abfe18810d794d99d), [b/317055535](https://issuetracker.google.com/issues/317055535))
- Deprecated obsolete compat methods in `ViewCompat`. ([I0bfc2](https://android-review.googlesource.com/#/q/I0bfc2cd15dc681ba0c09f795d25622f2ade004d6), [b/313834577](https://issuetracker.google.com/issues/313834577))

### Version 1.13.0-alpha02

November 29, 2023

`androidx.core:core:1.13.0-alpha02`, `androidx.core:core-ktx:1.13.0-alpha02`, and `androidx.core:core-testing:1.13.0-alpha02` are released. [Version 1.13.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/core)

**New Features**

- Adds the `OnUserLeaveHintProvider` interface to allow any component to receive `onUserLeaveHint` events necessary for implementing picture-in-picture. This is implemented by `ComponentActivity` in [Activity `1.9.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/activity#1.9.0-alpha01). ([I54892](https://android-review.googlesource.com/#/q/I54892c9ab5a8a002164b9f98cd31e02d56d73da7))

**API Changes**

- Deprecated `androidx.core.os.CancellationSignal`. Usages should be replaced with the platform-provided `android.os.CancellationSignal`. ([Id45f6](https://android-review.googlesource.com/#/q/Id45f69a0b9cee7515d3f5b35dde3b3b037f8bd3a), [b/309499026](https://issuetracker.google.com/issues/309499026), [b/309054079](https://issuetracker.google.com/issues/309054079))
- The `OnMultiWindowModeChangedProvider`, `OnNewIntentProvider`, `OnPictureInPictureModeChangedProvider`, `OnConfigurationChangedProvider`, and `OnTrimMemoryProvider` interfaces have been converted to Kotlin to ensure that the generic parameters on the `Consumer` that their listener methods take have the correct nullability (they are all non-null). ([Ib6237](https://android-review.googlesource.com/#/q/Ib62377a0f6002806074a05126cf6a9ca8c78dcbf))
- The `MultiWindowModeChangedInfo` and `PictureInPictureModeChangedInfo` classes that are sent to the `Consumer` added to their respective Provider interfaces are now written in Kotlin. ([Ie08e2](https://android-review.googlesource.com/#/q/Ie08e292c77dc66634a0b474a63df0ac31f34f87e))

**Dependency Update**

- Core now depends on [Lifecycle `2.6.2`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.2). ([I2d94c](https://android-review.googlesource.com/#/q/I2d94c8b7fc3fb3bb59547d56a5d2f06584f1b5a4))

### Version 1.13.0-alpha01

October 18, 2023

`androidx.core:core:1.13.0-alpha01`, `androidx.core:core-ktx:1.13.0-alpha01`, and `androidx.core:core-testing:1.13.0-alpha01` are released. [Version 1.13.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29aee18f0412c0d5d5b54e795697e34f358fd70a..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/core)

**API Changes**

- Make `PathParser` public. The class can create a Path instance from SVG path strings. ([Ic7af2](https://android-review.googlesource.com/#/q/Ic7af2e7ea294ed43e8ebcf41852d2c1618816655), [b/302376846](https://issuetracker.google.com/issues/302376846))
- Added compat method for `Context.createAttributionContext`. ([I61dcf](https://android-review.googlesource.com/#/q/I61dcfdb554718d29517694ea0793fa9fd9c920dd), [Ibe187](https://android-review.googlesource.com/#/q/Ibe18777566ad760e5f790409d02d96614bd8e849))
- Marks `NotificationCompatSideChannelService` as deprecated. ([I18fd9](https://android-review.googlesource.com/#/q/I18fd939b593bd4b624d5c8e09358b8cb3893da55))
- New API for differential motion fling. ([I46b0d](https://android-review.googlesource.com/#/q/I46b0db177bf022c0de3838dc4707d9dcc33cfa32), [Ia9f68](https://android-review.googlesource.com/#/q/Ia9f688063958d6165583d735d1b92745a8d2790e))
- Additional compat APIs for `VelocityTracker` to track platform SDK. ([I32753](https://android-review.googlesource.com/#/q/I327530551bbae8e4594d1b081ce3277bc60efe57))

**Bug Fixes**

- Override `equals` and `hashCode` methods in `Person`. ([I610a5](https://android-review.googlesource.com/#/q/I610a5c9ea9bfc273bea3a1c474eaec29edff2bab))

## Core and Core-ktx Version 1.12

### Version 1.12.0

September 6, 2023

`androidx.core:core:1.12.0`, `androidx.core:core-ktx:1.12.0`, and `androidx.core:core-testing:1.12.0` are released. [Version 1.12.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2162b56c0a32e398c2d311a15f1615f89c50d81f..29aee18f0412c0d5d5b54e795697e34f358fd70a/core)

**Important changes since 1.11.0**

- Many compat methods added for SDK 34 parity with TextView, AccessibilityNodeInfo, etc.
- New `LocalePreferences` APIs to help developers to easily access locale data or user's locale preferences.
- Deprecated `app.BundleCompat` in favor of `os.BundleCompat`.
- Deprecated `BuildCompat.isAtLeastU()`. Use `SDK_INT >= 34` instead.

### Version 1.12.0-rc01

August 9, 2023

`androidx.core:core:1.12.0-rc01`, `androidx.core:core-ktx:1.12.0-rc01`, and `androidx.core:core-testing:1.12.0-rc01` are released with no major changes. [Version 1.12.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..2162b56c0a32e398c2d311a15f1615f89c50d81f/core)

### Version 1.12.0-beta01

July 26, 2023

`androidx.core:core:1.12.0-beta01`, `androidx.core:core-ktx:1.12.0-beta01`, and `androidx.core:core-testing:1.12.0-beta01` are released. [Version 1.12.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..4aed940027a19667e67d155563fc5fa8b7279313/core)

**API Changes**

- Added `setLineHeight(unit, lineHeight)` to `TextView`compat classes ([Ia9fa9](https://android-review.googlesource.com/#/q/Ia9fa96f6ab74ebb6fe73b080c21c8afe419215cc))
- Added `TypedValueCompat.getUnitFromComplexDimension()` from Android 14 ([I958e8](https://android-review.googlesource.com/#/q/I958e824eb9ea46ba2795e0f8ceeff88012d1f358))
- Added `setLineHeight(unit, lineHeight)` to `TextView` compat classes ([Ib2ee1](https://android-review.googlesource.com/#/q/Ib2ee1334bd0396a8d92a87b8c2268029a36b1148))
- Backport miscellaneous Accessibility APIs ([Ic65ba](https://android-review.googlesource.com/#/q/Ic65badbf9262a388ffdd182cb25dcdde0c5eefe9))
- Backport API 34 `AccessibilityNodeInfo` methods ([I44182](https://android-review.googlesource.com/#/q/I44182678818c00732cf60e7acbf41b05374a4880))
- Graduate stable SDK checks out of experimental ([Ia9b35](https://android-review.googlesource.com/#/q/Ia9b3529ede0960d75f5b7e0a805aba6903a5add2))
- Backport `AccessiiblityWindowInfo` 34 APIs ([I96a5d](https://android-review.googlesource.com/#/q/I96a5d67a1fd485bdae0a14ac4c05c8a857400e7d))
- Deprecated `BuildCompat.isAtLeastU()`. Use `SDK_INT >= 34` instead. ([I4f8e7](https://android-review.googlesource.com/#/q/I4f8e795cbfa8c965b5f21331645af55c6709e7ab), [b/289269026](https://issuetracker.google.com/issues/289269026))
- Removed usages of experimental `isAtLeastU()` API ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87), [b/289269026](https://issuetracker.google.com/issues/289269026))
- Migrated `BuildCompat` to Kotlin for enhanced Deprecated tag ([I56775](https://android-review.googlesource.com/#/q/I56775e11c79e893138b67add76f758489a4262de), [b/289269026](https://issuetracker.google.com/issues/289269026))
- Added `setLineHeight(unit, lineHeight)` to `TextView` compat classes ([I15716](https://android-review.googlesource.com/#/q/I1571669714d19c2e26d514b512f485d8dc5f6b97))
- New `accessibilityDataSensitive` compat property. ([I0c6e0](https://android-review.googlesource.com/#/q/I0c6e02ee085e88d7815c437d0605de2e9285666f))
- `PendingIntentCompat.getActivity` and `getService` may return null when `FLAG_NO_CREATE` is specified. ([Iffdf0](https://android-review.googlesource.com/#/q/Iffdf01bbd65c2cc18f3b21ac4d02881a75a0afee), [b/289696515](https://issuetracker.google.com/issues/289696515))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b), [b/287516207](https://issuetracker.google.com/issues/287516207))
- Added `PendingIntentCompat.send()` ([Iaf707](https://android-review.googlesource.com/#/q/Iaf7071bb597ebdba7366bf5477f5a488e9233f52))
- Adds compat versions of `Location.removeVerticalAccuracy()`, `Location.removeSpeedAccuracy()`, and `Location.removeBearingAccuracy()`. ([I5b640](https://android-review.googlesource.com/#/q/I5b640be514323abdf2458a9c4ced92d31f448691))

**Bug Fixes**

- Made a view important for accessibility if the view has an accessibility delegate. ([If2b54](https://android-review.googlesource.com/#/q/If2b54e94daf9612e84aab13f498f8028ee8d68d6))

### Version 1.12.0-alpha05

June 7, 2023

`androidx.core:core:1.12.0-alpha05`, `androidx.core:core-ktx:1.12.0-alpha05`, and `androidx.core:core-testing:1.12.0-alpha05` are released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher. It contains the same bug fixes as 1.11.0-beta02.

**Bug Fixes**

- Updated the documentation on the `ColorUtils` classes for generating a color from the Material 3 Hue, Chroma, and Tone (M3HCT) parameters. ([I32979](https://android-review.googlesource.com/#/q/I3297991f0782c108e548835049536edbb824cd16), [I21c8c](https://android-review.googlesource.com/#/q/I21c8c4014ef098dbb60f048fb5e622e0a649eee4))
- Fix deprecation replaceWith for `android.os.Trace` ([I730f9](https://android-review.googlesource.com/#/q/I730f9d50071ae3c8bf6ba6a4afddbdbf062931d5))

### Version 1.12.0-alpha04

May 10, 2023

`androidx.core:core:1.12.0-alpha04`, `androidx.core:core-ktx:1.12.0-alpha04`, and `androidx.core:core-testing:1.12.0-alpha04` are released. This was released from an internal branch.
| **Note:** This version will only compile against the Android 14 Beta 2 SDK.

### Version 1.12.0-alpha03

April 12, 2023

`androidx.core:core:1.12.0-alpha03`, `androidx.core:core-ktx:1.12.0-alpha03`, and `androidx.core:core-testing:1.12.0-alpha03` are released. This was released from an internal branch.
| **Note:** This version will only compile against the Android 14 Beta 1 SDK.

**API Changes**

- Unhides `NotificationCompat.TvExtender` (aosp/01c67677e9310b2cf4c536d7e951e117d6cce64a)
- Added public methods to access M3HCT parameters and turn M3HCT values into ARGB (aosp/06810598aa94bee731bbe0d277933b8b9614934e)
- Added `NotificationManager.getCurrentInterruptionFilter` (aosp/b0c6940639e35371d212a7ebd7dbf01c14fc7710)
- Added `getCurrentInterruptionFilter` to `NotifManagerCompat` (aosp/516143e05f824ff49bde3c0c97344a2924867d30)
- Deprecated `app.BundleCompat` in favor of `os.BundleCompat` (aosp/bf6169fe9ee1113065d0cf380bd2e09f31ce0a40)
- Added `TestConsumer` so developers can record values in a test. (aosp/f75a4913940e710842168c832a7f57c2dcae4fdf)
- Added `TestConsumer` so developers can record values in a test.(aosp/67ad4e2c6488772b7c9a061ee6ca01bba23649f7)

**Bug Fixes**

- Fixed a bug where `unregisterGnssMeasurementsCallback()` does not work properly below Android R. (aosp/c5a97c4ee956f87d229ec892f2b8849f392e956c)

### Version 1.12.0-alpha01

March 8, 2023

`androidx.core:core:1.12.0-alpha01` and `androidx.core:core-ktx:1.12.0-alpha01` are released. [Version 1.12.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/923a1348f2ba835723e91c25cb5d4cd7e1ff4bc9/core)

**New Features**

- Provides APIs to help developers to easily access user's preference or the locale data in ICU. The accessible locale data includes hour cycle, calendar type, temperature unit, and first day of week.

**API Changes**

- Added new APIs `LocalePreferences` to help developers to easily access locale data or user's locale preferences.

## Core and Core-ktx Version 1.11

### Version 1.11.0-beta02

June 7, 2023

`androidx.core:core:1.11.0-beta02`, `androidx.core:core-ktx:1.11.0-beta02`, and `androidx.core:core-testing:1.11.0-beta02` are released. [Version 1.11.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..73f902dee011bfe400d8a0330bfd8d4bb632065f/core)

**Bug Fixes**

- Updated the documentation on the `ColorUtils` classes for generating a color from the Material 3 Hue, Chroma, and Tone (M3HCT) parameters. ([I32979](https://android-review.googlesource.com/#/q/I3297991f0782c108e548835049536edbb824cd16), [I21c8c](https://android-review.googlesource.com/#/q/I21c8c4014ef098dbb60f048fb5e622e0a649eee4))
- Fix deprecation replaceWith for `android.os.Trace` ([I730f9](https://android-review.googlesource.com/#/q/I730f9d50071ae3c8bf6ba6a4afddbdbf062931d5))

### Version 1.11.0-beta01

May 24, 2023

`androidx.core:core:1.11.0-beta01`, `androidx.core:core-ktx:1.11.0-beta01`, and `androidx.core:core-testing:1.11.0-beta01` are released. [Version 1.11.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/core)

**API Changes**

- Add `ViewCompat` support to method `performHapticFeedback` ([Ib02c6](https://android-review.googlesource.com/#/q/Ib02c648e0fe6a9bad1d4b3c10811559edda98935))
- Change `getDisplay` to `#getDisplayOrDefault` ([I96ff9](https://android-review.googlesource.com/#/q/I96ff91170c33a767e737b425a38a04c108bd0814))
- Add `ContextCompat#getDisplay(Context)` ([I7011f](https://android-review.googlesource.com/#/q/I7011fb43e667b46f8f161c7c6e169c1a7faa8847), [b/178183326](https://issuetracker.google.com/issues/178183326))
- Add `ContextCompat#getContextForLanguage(Context)` for getting per-app locales in non-Activity context ([I58e75](https://android-review.googlesource.com/#/q/I58e753c9168b139f475e11a3217b7a421f8d4456), [b/243457462](https://issuetracker.google.com/issues/243457462))

**Bug Fixes**

- Clarify `CollectionInfoCompat` docs, especially `isHierarchical` ([I14f6c](https://android-review.googlesource.com/#/q/I14f6c496eed404a51c65f28e58e09981ac4a0b28))

### Version 1.11.0-alpha04

May 10, 2023

`androidx.core:core:1.11.0-alpha04`, `androidx.core:core-ktx:1.11.0-alpha04`, and `androidx.core:core-testing:1.11.0-alpha04` are released. [Version 1.11.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/core)

**API Changes**

- Added `LinkMovementMethodCompat` that fixes link touch handling ([Ia632c](https://android-review.googlesource.com/#/q/Ia632c50bc335cf42ab903a2521de8afd97737f83))
- `PendingIntent.getBroadcast()` is now correctly marked `@Nullable` ([Ifff96](https://android-review.googlesource.com/#/q/Ifff965b38abb4fccc4709a52a5a71d6372a388a5), [b/277630907](https://issuetracker.google.com/issues/277630907))

**Bug Fixes**

- Fixed Context leak in `DisplayManagerCompat` ([I3409b](https://android-review.googlesource.com/#/q/I3409b324301609dba940ef5894ff349b0f229d13), [b/279625765](https://issuetracker.google.com/issues/279625765))
- Added a `SoftwareKeyboardControllerCompat` to provide direct methods to show and hide the software keyboard given a View. This backports workarounds for known issues when using the `WindowInsetsController` APIs on some API levels, and is the extraction of the backing implementation for `WindowInsetsControllerCompat.show` and hide for the IME inset types. ([Idd0a3](https://android-review.googlesource.com/#/q/Idd0a3e57c759b05ead2c7843b0400fff3515dd62))

### Version 1.11.0-alpha03

April 19, 2023

`androidx.core:core:1.11.0-alpha03`, `androidx.core:core-ktx:1.11.0-alpha03`, and `androidx.core:core-testing:1.11.0-alpha03` are released. [Version 1.11.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/core)

**API Changes**

- Update `BuildCompat` in preparation for Android 14 Beta 2 ([Idc1b1](https://android-review.googlesource.com/#/q/Idc1b17e48cf5e181b7904cb998a11511a3b2d75e), [b/276491001](https://issuetracker.google.com/issues/276491001))
- Unhides `NotificationCompat.TvExtender` ([Ibe13a](https://android-review.googlesource.com/#/q/Ibe13aa2cad4d3386e9a57cc6c515eac7efc36ce8))
- Add public methods to access M3HCT parameters and turn M3HCT values into ARGB ([Id7e9d](https://android-review.googlesource.com/#/q/Id7e9dd1565007a1840f4402a7a9c76de0c654b2d))

### Version 1.11.0-alpha02

April 5, 2023

`androidx.core:core:1.11.0-alpha02`, `androidx.core:core-ktx:1.11.0-alpha02`, and `androidx.core:core-testing:1.11.0-alpha02` are released. [Version 1.11.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597/core)

**API Changes**

- Adds `getCurrentInterruptionFilter` to `NotifManagerCompat` ([I8ec95](https://android-review.googlesource.com/#/q/I8ec95cf70faa9b5920c019784f44947a08ec5893), [b/243183646](https://issuetracker.google.com/issues/243183646))
- Deprecate `app.BundleCompat` in favor of `os.BundleCompat` ([Idc3a2](https://android-review.googlesource.com/#/q/Idc3a212aff67f8193665a65ca8cc916f3327d3a4), [b/274577000](https://issuetracker.google.com/issues/274577000))
- Add `TestConsumer` so developers can record values in a test. ([I937c1](https://android-review.googlesource.com/#/q/I937c1d33c450284f751f583f37b4939213caefeb))

**Bug Fixes**

- Fix a bug where `unregisterGnssMeasurementsCallback()` does not work properly below Android R. ([Id1999](https://android-review.googlesource.com/#/q/Id199974ce7d0ade2cffdb33bba5c589a7bf430e5))

### Version 1.11.0-alpha01

March 22, 2023

`androidx.core:core:1.11.0-alpha01` and `androidx.core:core-ktx:1.11.0-alpha01` are released. [Version 1.11.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/299c338f307a5a82d82a011539aaecbfb3e72521..5e7d256f82fbafb6d059ab7b18fddd87c7531553/core)

**API Changes**

- In Android U, the `ContentProvider` API of `getType` requires that the caller hold the correct read permission. `FileProvider` now provides a default `getTypeAnonymous` implementation, which is the unrestricted version. ([I4773f](https://android-review.googlesource.com/#/q/I4773f02b887582f19d2833bd771f4f2340e1d130))
- Added compat classes for content capture APIs ([I09366](https://android-review.googlesource.com/#/q/I09366f3389305c4403dcd92e084940386f6e576a))
- Added `NotifCompat.Builder.setLargeIcon(Icon)` ([Ic0a5b](https://android-review.googlesource.com/#/q/Ic0a5bd849209bd92eba1fbed430369ff30149d08))
- Adds a batch notification API to `NotificationManagerCompat`. Users are encouraged to use this API when posting multiple notifications. ([I2cd7f](https://android-review.googlesource.com/#/q/I2cd7f8d9bcce811dedb91204766b0a9fdaafee4b))
- Added `registerGnssMeasurementsCallback()` with Executor support on pre-R platforms ([I579f8](https://android-review.googlesource.com/#/q/I579f8cc2f40e2c8b27fa9d33126a0bc004f9c3f7))

## Core and Core-ktx Version 1.10

### Version 1.10.1

May 10, 2023

`androidx.core:core:1.10.1` and `androidx.core:core-ktx:1.10.1` are released. [Version 1.10.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7674e65cb62a6c6d4ab319246bc0c4e5fae84f68..ca5beb5b294cad4dde980fcd4743d5f86433ad2c/core)

**External Contribution**

- Fix `BadParcelableException` being thrown for result being null [b/277434277](https://issuetracker.google.com/issue?id=277434277), [b/278118318](https://issuetracker.google.com/issue?id=278118318) contributed by Mygod Studio

### Version 1.10.0

April 5, 2023

`androidx.core:core:1.10.0` and `androidx.core:core-ktx:1.10.0` are released. [Version 1.10.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/94ae06db1eb182d6464a7a5dabf76e1bf15e2af9..7674e65cb62a6c6d4ab319246bc0c4e5fae84f68/core)

**Important changes since 1.9.0**

- Deprecated recycling of accessibility objects. We've found performance changes to be negligible for even the oldest supported OS versions. ([I0a961](https://android-review.googlesource.com/#/q/I0a961c85c260b1e8dd97826d0b32c0bdcb51fcfe))
- Added `BuildCompat` constants for SDK extension versions. ([I6084c](https://android-review.googlesource.com/#/q/I6084c957e7cf6f9303d7cf2af712c1e35dfb7591))
- See release notes for pre-release versions of 1.10.0 for new APIs and bug fixes.

### Version 1.10.0-rc01

March 8, 2023

`androidx.core:core:1.10.0-rc01` and `androidx.core:core-ktx:1.10.0-rc01` are released with no changes from the previous beta.

### Version 1.10.0-beta01

February 22, 2023

`androidx.core:core:1.10.0-beta01` and `androidx.core:core-ktx:1.10.0-beta01` are released. [Version 1.10.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..87533b4ff06971ed59028936cd9b6da988cd4522/core)

**API Changes**

- The `AccessibilityNodeInfoCompat` APIs of `set/getMinMillisBetweteenContentChanges` have been renamed to `set/getMinDurationBetweenContentChanges` and now take a `long` for their duration. ([f46689](https://android.googlesource.com/platform/frameworks/support/+/f4668956db729a5ca67c6106e3f1a3710e9591ce))
- Added `NotificationCompat.bigLargeIcon(Icon)` ([I60855](https://android-review.googlesource.com/#/q/I60855a520dead45cb52bd16a26f688289fa7a3cb))

**Bug Fixes**

- Fix docs regarding default value of `NotificationCompat.Builder.setShowWhen()` ([ba52a2](https://android.googlesource.com/platform/frameworks/support/+/ba52a2d8a82194648b8498bc539e0f9d155b7fec))
- Fix typo in `AccelerateInterpolator / DecelerateInterpolator` docs ([2173505](https://android.googlesource.com/platform/frameworks/support/+/21735057f6262bbe47031fb3e904ff1f7f590388))
- Fix typo in `ShortcutInfoCompat` docs ([44075f](https://android.googlesource.com/platform/frameworks/support/+/44075fccc041fd2e902f989a0e671fd7285f5058))
- Fix up, down, spacebar and key variation keyboard actions with `NestedScrollView` and `CoordinatorLayout` ([bdd72e](https://android.googlesource.com/platform/frameworks/support/+/bdd72e61dff5f256a8d072b93547185a152ef292))

### Version 1.10.0-alpha02

January 25, 2023

`androidx.core:core:1.10.0-alpha02` and `androidx.core:core-ktx:1.10.0-alpha02` are released. [Version 1.10.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/838b545fcc966e05db9607c5c500916173c43c15..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/core)

**API Changes**

- Added `BuildCompat` constant for `AD_SERVICES` extension version ([I51d98](https://android-review.googlesource.com/#/q/I51d98dabff9502c1dfb41891cb3f0197a4efc463))
- Add `BEHAVIOR_DEFAULT` to `WindowInsetsControllerCompat`. `BEHAVIOR_SHOW_BARS_BY_SWIPE` and `BEHAVIOR_SHOW_BARS_BY_TOUCH` are deprecated. ([I17b61](https://android-review.googlesource.com/#/q/I17b61c4b2993036905881124b54fec9ae873ffa7))

### Version 1.10.0-alpha01

January 11, 2023

`androidx.core:core:1.10.0-alpha01` and `androidx.core:core-ktx:1.10.0-alpha01` are released. [Version 1.10.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/94ae06db1eb182d6464a7a5dabf76e1bf15e2af9..adf1c279a86ab3886e1666c08e2c3efba783367b/core)

**API Changes**

- Adds `CallStyle` to `NotificationCompat` ([Id9a53](https://android-review.googlesource.com/#/q/Id9a5321ab9172a004215c85aa2e6d7165a01e074), [b/199294989](https://issuetracker.google.com/issues/199294989))
- Added `BuildCompat` constants for SDK extension versions ([I6084c](https://android-review.googlesource.com/#/q/I6084c957e7cf6f9303d7cf2af712c1e35dfb7591))
- Add APIs for setting initial focus on accessibility node. ([Id199a](https://android-review.googlesource.com/#/q/Id199a3d11031a52c0082395a9e565140cae2ec34))
- Add new APIs for content change rate limiting ([If4ea0](https://android-review.googlesource.com/#/q/If4ea0b5d445b1dff1cbc0d228668b63b615838ae))
- Adds compatibility methods for new APIs introduced in Android 13 for Parcels, Bundles, and Intents. Some `ParcelCompat` method signatures have been updated, and may require a source change on upgrade to confirm to the new signature. ([I57e94](https://android-review.googlesource.com/#/q/I57e94c6efcc674173d201205fb175cef495bcf82), [b/242048899](https://issuetracker.google.com/issues/242048899))
- Deprecating recycling of accessibility objects. We've found performance changes to be negligible in even the oldest supported versions. ([I0a961](https://android-review.googlesource.com/#/q/I0a961c85c260b1e8dd97826d0b32c0bdcb51fcfe))
- Updated return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Added times/div operator overloads for Point and PointF ([I8e557](https://android-review.googlesource.com/#/q/I8e5579574ad55a39714d3c9aea2840bc21ee31c5), [b/261574780](https://issuetracker.google.com/issues/261574780))

**Bug Fixes**

- Add to `AccessibilityEvent#TYPE_ANNOUNCEMENT` with suggestion to avoid using it. ([I818bf](https://android-review.googlesource.com/#/q/I818bfedca2e8dfada286632a8ee6806d0998267c))
- Specify lists should have 1 row or 1 column for accessibility ([Ia1223](https://android-review.googlesource.com/#/q/Ia1223b7a9a714021c0cd7ac21e6f33f313e3c415))

## Core and Core-ktx Version 1.9.0

### Version 1.9.0

September 7, 2022

`androidx.core:core:1.9.0` and `androidx.core:core-ktx:1.9.0` are released. [Version 1.9.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/429a42e7ba6bd6bf15ebd8b4e5d1e504fe650d4e..94ae06db1eb182d6464a7a5dabf76e1bf15e2af9/core)

**Important changes since 1.8.0**

- Updated to improve compatibility with Android 13, including nullability changes and parity with framework APIs
- Added `IntentSanitizer` to sanitize unsafe intents before launching them. ([Ib0be5](https://android-review.googlesource.com/#/q/Ib0be5ae604249dc660585ff0c4cb42ed9f64a183))
- Adds support for `BigPictureStyle` using `Icon` ([Ice26d](https://android-review.googlesource.com/#/q/Ice26d1400836cdf74af931f0f8ca59c25dd9c3c3))
- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631))
- Improved parity between Android 13 accessibility framework APIs and compat APIs ([I93c97](https://android-review.googlesource.com/#/q/I93c97f1f2cbd9694db61f149d7a0b979bef63a47), [I5a074](https://android-review.googlesource.com/#/q/I5a074c3a8b787b0a85dba8c68c6bff427551a577), [Iedf82](https://android-review.googlesource.com/#/q/Iedf8253f63e74115c55d6b5814761344e88b120a))

### Version 1.9.0-rc01

August 24, 2022

`androidx.core:core:1.9.0-rc01` and `androidx.core:core-ktx:1.9.0-rc01` are released. [Version 1.9.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..429a42e7ba6bd6bf15ebd8b4e5d1e504fe650d4e/core)

**Bug Fixes**

- `IntentSanitizer.sanitizeByFiltering` no longer writes to the log when filtering ([69b3b55](https://android.googlesource.com/platform/frameworks/support/+/69b3b553c0ca9d063a035ebfdb89bfbcbccad377))

### Version 1.9.0-beta01

August 10, 2022

`androidx.core:core:1.9.0-beta01` is released. [Version 1.9.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf7759d18327857b729c79132e67a91caa382827..bea814b246f89ff7244e3c6b0648f0b57e47897c/core/core)

**API Changes**

- Added compatibility for `ACTION_SHOW_TEXT_SUGGESTIONS` and `is/setTextSelectable` ([Iedf82](https://android-review.googlesource.com/#/q/Iedf8253f63e74115c55d6b5814761344e88b120a))
- Added `IntentSanitizer` to sanitize unsafe intents before launching them. ([Ib0be5](https://android-review.googlesource.com/#/q/Ib0be5ae604249dc660585ff0c4cb42ed9f64a183))
- Adds support for `BigPictureStyle` using Icon ([Ice26d](https://android-review.googlesource.com/#/q/Ice26d1400836cdf74af931f0f8ca59c25dd9c3c3), [b/215583339](https://issuetracker.google.com/issues/215583339))
- Updated nullability annotations ([I34cce](https://android-review.googlesource.com/#/q/I34cce3c167135c9020a015b08f70fb1cdba5f8ce), [b/236498052](https://issuetracker.google.com/issues/236498052), [b/236498029](https://issuetracker.google.com/issues/236498029), [b/236497996](https://issuetracker.google.com/issues/236497996), [b/236497942](https://issuetracker.google.com/issues/236497942), [b/236497884](https://issuetracker.google.com/issues/236497884), [b/236497726](https://issuetracker.google.com/issues/236497726))
- Added `LocationManagerCompat.registerGnssMeasurementsCallback` to work around Android R bugs. ([Ie0f6f](https://android-review.googlesource.com/#/q/Ie0f6f86c5bb02291d23a0dcd56e50095c5041ec7))

**Bug Fixes**

- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631), [b/238790278](https://issuetracker.google.com/issues/238790278))
- Adding support for API introduced in T." into androidx-platform-dev" ([](https://android-review.googlesource.com/#/q/))
- Adding support for API introduced in T. ([I358f1](https://android-review.googlesource.com/#/q/I358f10779ba4a1fb34eeed94c9c579c24107ac08))
- `TypefaceCompate.create(..., weight, italic)` will fallback to platform `Typeface.create` when compat impl cannot resolve on API 14-20 ([I1ee34](https://android-review.googlesource.com/#/q/I1ee34c7e38fc36174151d88d363adaee4371cb51), [b/145311058](https://issuetracker.google.com/issues/145311058))
- Added accessibility framework constants previously absent from androidx." into androidx-main am: d5747be010" ([I5a074](https://android-review.googlesource.com/#/q/I5a074c3a8b787b0a85dba8c68c6bff427551a577))
- Added accessibility framework constants previously absent from androidx. ([I93c97](https://android-review.googlesource.com/#/q/I93c97f1f2cbd9694db61f149d7a0b979bef63a47))

**External Contribution**

- Backported `Typeface#create(Typeface, int, boolean)` which allows creating typeface with specific weight from a font family ([I342dc](https://android-review.googlesource.com/#/q/I342dc928edd1e8e5dbc018ca5375cceb047425e5))

### Version 1.9.0-alpha05

June 15, 2022

`androidx.core:core:1.9.0-alpha05` and `androidx.core:core-ktx:1.9.0-alpha05` are released. Version 1.9.0-alpha05 was developed in a private pre-release branch and has no public commits.

**API Changes**

- Nullability updates to align with finalized API surface in Tiramisu Beta 3 SDK
- `minCompileSdk` is now 33 to align with Tiramisu Beta 3 SDK

### Version 1.9.0-alpha04

May 18, 2022

`androidx.core:core:1.9.0-alpha04` and `androidx.core:core-ktx:1.9.0-alpha04` are released. Version 1.9.0-alpha04 is built against a pre-release Android SDK and does not have a publicly-available commit history.

**Bug Fixes**

- Revert deprecation of `BuildCompat.isAtLeastT()` and accompanying `SDK_INT` checks

### Version 1.9.0-alpha03

April 27, 2022

`androidx.core:core:1.9.0-alpha03` and `androidx.core:core-ktx:1.9.0-alpha03` are released. Version 1.9.0-alpha04 contains all commits from [1.8.0-beta01](https://developer.android.com/jetpack/androidx/releases/core#1.8.0-beta01), but has been built against Android 13 Beta 1.

This version requires Android 13 Beta 1 to compile and is not guaranteed to be runtime-compatible with future developer previews.

### Version 1.9.0-alpha02

March 23, 2022

`androidx.core:core:1.9.0-alpha02` and `androidx.core:core-ktx:1.9.0-alpha02` are released. Version 1.9.0-alpha02 contains all commits from 1.8.0-alpha06, but has been built against Tiramisu DP2.

### Version 1.9.0-alpha01

February 23, 2022

`androidx.core:core:1.9.0-alpha01` and `androidx.core:core-ktx:1.9.0-alpha01` are released. Version 1.9.0-alpha01 was built from an internal branch and does not have publicly-visible commits.

This version requires Android Tiramisu DP1 to compile and is not guaranteed to be runtime-compatible with future developer previews.

**New Features**

- Compatible with Android Tiramisu DP1.

## Core and Core-ktx Version 1.8.0

### Version 1.8.0

June 1, 2022

`androidx.core:core:1.8.0` and `androidx.core:core-ktx:1.8.0` are released. [Version 1.8.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e43c8f66cf73f1d25b5759c0e8a65f93051ea618..1f3d3b4e655e9441bc9d9a2892e6973751a04b38/core)

**Important changes since 1.7.0**

- Significant clean-up of nullability annotations to improve Kotlin usability
- Platform parity improvements to `ShortcutInfoCompat`, `NotificationCompat`, and more
- New interfaces to allow components to receive picture-in-picture and multi-window mode change events, implemented by `ComponentActivity` in Activity library
- Improvements to `MenuProvider` callback methods, including `onPrepareMenu` and `onMenuClosed`
- Fixed issue where `FileProvider` would fail with `IllegalArgumentException` on certain devices
- Fixed issue where `TypefaceCompat` applied incorrect typeface weight on API 29+ ([b/194553426](https://issuetracker.google.com/194553426)) thanks to contribution from [RikkaW](https://github.com/RikkaW)

### Version 1.8.0-rc02

May 18, 2022

`androidx.core:core:1.8.0-rc02` and `androidx.core:core-ktx:1.8.0-rc02` are released. [Version 1.8.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df694c502b6ecdcfc15500f0dd4fbb1d07683ed0..e43c8f66cf73f1d25b5759c0e8a65f93051ea618/core)

**Bug Fixes**

- Cast `OnSharedElementsReadyListener` to fully-qualified platform class to prevent `ClassCastException` ([0029fed](https://android-review.googlesource.com/c/platform/frameworks/support/+/2086006))

### Version 1.8.0-rc01

May 11, 2022

`androidx.core:core:1.8.0-rc01` and `androidx.core:core-ktx:1.8.0-rc01` are released. [Version 1.8.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..df694c502b6ecdcfc15500f0dd4fbb1d07683ed0/core)

**API Changes**

- Added `BuildCompat` check for next pre-release cycle ([If5a8f](https://android-review.googlesource.com/#/q/If5a8fd682e75bc0d1d69c25c11081f2b6b689bd7), [b/229859122](https://issuetracker.google.com/issues/229859122))
- Updated `BuildCompat.isAtLeastT()` for finalized SDK_INT value. ([Iffae0](https://android-review.googlesource.com/#/q/Iffae0c327706432f5f126cd93a1b5196ae4a38ba))

### Version 1.8.0-beta01

April 20, 2022

`androidx.core:core:1.8.0-beta01` and `androidx.core:core-ktx:1.8.0-beta01` are released with no changes since 1.8.0-alpha07. [Version 1.8.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/core)

### Version 1.8.0-alpha07

April 6, 2022

`androidx.core:core:1.8.0-alpha07` and `androidx.core:core-ktx:1.8.0-alpha07` are released. [Version 1.8.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/core)

**Bug Fixes**

- `TypefaceCompat` will now respect both requested and loaded style information on API 29+. This is a behavior change when the loaded fonts are not `FontWeight.Normal` or `FontWeight.Bold`, as the actual loaded weight and style will be used. ([#212](https://github.com/androidx/androidx/pull/212), [b/194553426](https://issuetracker.google.com/issues/194553426))

**External Contribution**

- Thanks [RikkaW](https://github.com/RikkaW) for ensuring we correctly apply Typeface weight in TypefaceCompat on API 29+. [#212](https://github.com/androidx/androidx/pull/212)

### Version 1.8.0-alpha06

March 23, 2022

`androidx.core:core:1.8.0-alpha06` is released. [Version 1.8.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/core/core)

**API Changes**

- The `MenuProvider` interface now includes the `onPrepareMenu()` callback, which is called when a menu is dynamically modified and should be shown. ([Ie85f9](https://android-review.googlesource.com/#/q/Ie85f9b6c42fa8b76d960d167aa1943e1190bf4d2))
- The `MenuProvider` interface now includes the `onMenuClosed()` method to be used whenever a menu should be closed. ([If5a16](https://android-review.googlesource.com/#/q/If5a16197b81d38aa3d0dc9ab4f0c089709e478b4))
- Updated `IconCompat#getResId` to have the proper resource annotation type to match the corresponding method in the framework in `Icon#getResId` ([I49700](https://android-review.googlesource.com/#/q/I497001954360a30666dc69b257f02aa5c9d85ed9))
- Reverted previous change of relying solely on a View for `WindowInsetsControllerCompat`, and again require a Window which is required for managing some window flags. Deprecated `ViewCompat.getWindowInsetsController` in favor of `WindowCompat.getInsetsController` to ensure that the correct Window is used (such as if the View is in a dialog). ([I660ae](https://android-review.googlesource.com/#/q/I660aee32108b59516232b41e05b3f05ae2538554), [b/219572936](https://issuetracker.google.com/issues/219572936))
- Updated nullability in core and appcompat to match Tiramisu DP2 ([I0cbb7](https://android-review.googlesource.com/#/q/I0cbb7f22651e725a4bb36d20388a949a72cc5903))
- Adds a method to `BitmapCompat` for smoother downscaling of bitmaps. ([Ib706c](https://android-review.googlesource.com/#/q/Ib706ce8bd6045811fb87e32277b5239be8c8e772))
- Added nullability annotations to `ActivityCompat.requestDragAndDropPermissions` ([I0f2b0](https://android-review.googlesource.com/#/q/I0f2b080bdff589ed22e8bf75789ed2e268f9b3c1), [b/206113378](https://issuetracker.google.com/issues/206113378))
- Added a work-around to `FileProvider` for OEMs stripping meta-data from manifests. ([I82f63](https://android-review.googlesource.com/#/q/I82f63ccc3d95c4b82c5c42db8cad4d09cd152017))

**Bug Fixes**

- Consider parent visibility changes for a11y pane visibility status for \<P ([I8e04f](https://android-review.googlesource.com/#/q/I8e04f145be0cb440695d988408703f9a723f5b84))

### Version 1.8.0-alpha05

February 23, 2022

`androidx.core:core:1.8.0-alpha05` and `androidx.core:core-ktx:1.8.0-alpha05` are released. [Version 1.8.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/core)

**API Changes**

- Updated nullability for androidx.core.os classes ([If18cd](https://android-review.googlesource.com/#/q/If18cd2bcd8b5de33a5e47997339d32e9a13bc312), [b/206113622](https://issuetracker.google.com/issues/206113622))
- Updated nullability for androidx.core.app classes ([I657eb](https://android-review.googlesource.com/#/q/I657ebbacc2cea4de6d8d5ca266701f2827fe417b), [b/206113302](https://issuetracker.google.com/issues/206113302))
- Updated nullability for androidx.core.text classes ([I08329](https://android-review.googlesource.com/#/q/I08329441241bee3909728295156afa721431a242), [b/206113384](https://issuetracker.google.com/issues/206113384))
- Added `ExtraData` functions to `AccessibilityNodeInfoCompat` ([If2fc7](https://android-review.googlesource.com/#/q/If2fc79374de6d7ae3b06096dc8fee2c80734b0e4), [b/137789185](https://issuetracker.google.com/issues/137789185))
- Added zero-arg overload for `bundleOf()` to avoid an invisible array allocation when creating an empty bundle ([If7089](https://android-review.googlesource.com/#/q/If70891fcfdee3aa107a3064b903d00de185049bc))
- Added `Continuation<T>.asFoo()` adapters to create callbacks for writing suspend wrappers for Android APIs that accept common/generic callback types ([I6615e](https://android-review.googlesource.com/#/q/I6615ef9adfef1ecd518b0388ab13ba58e84ea20d))
- Added nullable `Drawable.toBitmapOrNull` method to avoid exceptions ([I2342a](https://android-review.googlesource.com/#/q/I2342a1c2b1a4d8a708d46bf9960501599fb48edf))

### Version 1.8.0-alpha04

February 9, 2022

`androidx.core:core:1.8.0-alpha04` and `androidx.core:core-ktx:1.8.0-alpha04` are released. [Version 1.8.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/core)

**API Changes**

- Adds the `OnPictureInPictureModeChangedProvider` interface to allow any component to receive picture-in-picture mode change events. This is implemented by `ComponentActivity` in [Activity `1.5.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.0-alpha02). ([I9f567](https://android-review.googlesource.com/#/q/I9f56767522d22873e0539a7f1a51257972619806))
- Adds the `OnMultiWindowModeChangedProvider` interface to allow any component to receive multi-window mode change events. This is implemented by `ComponentActivity` in [Activity `1.5.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.0-alpha02). ([I62d91](https://android-review.googlesource.com/#/q/I62d91abd50bc3e1e3d51b924f5dc144c893b4250))
- Cleaned up nullability for a subset of androidx.core APIs. ([Ia0e2f](https://android-review.googlesource.com/#/q/Ia0e2fef924851e9f96dc316bdaff55c61e60400f), [b/206113818](https://issuetracker.google.com/issues/206113818))

### Version 1.8.0-alpha03

January 26, 2022

`androidx.core:core:1.8.0-alpha03` and `androidx.core:core-ktx:1.8.0-alpha03` are released. [Version 1.8.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..9dceceb54300ed028a7e8fc7a3454f270337ffde/core)

**API Changes**

- Converted `WindowInsetsControllerCompat` to depend on a View instead of a Window or the platform `WindowInsetsController`. This improves behavior with Dialogs, showing the IME, and ensures the non-deprecated creation methods workaround ([b/180881870](https://issuetracker.google.com/issues/180881870)). ([I29264](https://android-review.googlesource.com/#/q/I292640cb4acc39e47a4d2ce0502293d42468ed67), [b/207401542](https://issuetracker.google.com/issues/207401542), [b/210121779](https://issuetracker.google.com/issues/210121779))
- Cleaned up nullability for a subset of androidx.core APIs. ([Ib2583](https://android-review.googlesource.com/#/q/Ib2583f0cb8d6bcf8b94141069ac6834e29dc7759), [b/206113818](https://issuetracker.google.com/issues/206113818))
- Fixed nullability of `performAccessibilityAction` params ([Ibbafe](https://android-review.googlesource.com/#/q/Ibbafe0184c2d87c5b89d159ed05bf7a768a493dd))
- Added method for working around `ColorStateList` issues resulting from Theme-keyed caching and Theme.applyStyle ([I9188b](https://android-review.googlesource.com/#/q/I9188bbf6b182111b3d6d302b81b9a000058687bd), [b/207739887](https://issuetracker.google.com/issues/207739887))
- Update shortcut visibility api for better readability ([Ia58df](https://android-review.googlesource.com/#/q/Ia58df45fef322a61d42e6f404b396c17321d7c91))
- Added zero-arg overload for `persistableBundleOf()` to avoid an unnecessary array allocation when creating an empty PersistableBundle ([Icd7a4](https://android-review.googlesource.com/#/q/Icd7a41c8211462f6c0f2b9554c30c1fcfe8a1c16))

### Version 1.8.0-alpha02

December 15, 2021

`androidx.core:core:1.8.0-alpha02` and `androidx.core:core-ktx:1.8.0-alpha02` are released. [Version 1.8.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..301586664b5aad60548f21866cad502d524dbf9f/core)

**API Changes**

- Adds experimental `BuildCompat` methods for future SDKs ([Iafd82](https://android-review.googlesource.com/#/q/Iafd82e20e0c6d54878d352baddb18e86095504a7), [b/207528937](https://issuetracker.google.com/issues/207528937))
- Add utility methods to convert document into shortcut and vice versa. ([Id512c](https://android-review.googlesource.com/#/q/Id512cb3b0378b971151b260c96e480e3d5255787))
- Update visibility api for shortcut for better readability ([I86dec](https://android-review.googlesource.com/#/q/I86deceddc729e23580e9f372d9c8fd9f1874ad9a))
- Adds the `OnNewIntentProvider`, `OnConfigurationChangedProvider`, and `onTrimMemoryProvider` interfaces that can be used to denote that your custom activity can dispatch these events to any component that adds a listener. ([If1f8b](https://android-review.googlesource.com/#/q/If1f8baabb64aa4aa776303bab33322969776b10d), [If623b](https://android-review.googlesource.com/#/q/If623b1764a9fda903ae308bae13de86d09d3cfd6), [Ia9295](https://android-review.googlesource.com/#/q/Ia9295c9a47293e6a768fb590fe00b6fe7a3092a5))

### Version 1.8.0-alpha01

December 1, 2021

`androidx.core:core:1.8.0-alpha01` and `androidx.core:core-ktx:1.8.0-alpha01` are released. [Version 1.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f01b06dda22df8afd990b500c0663bf83df78a52..75784ce6dbac6faa5320e5898e9472f02ab8710c/core)

**API Changes**

- Significant clean-up of nullability annotations
- Added a new API `ShortcutInfoCompat.Builder#setHiddenFromLauncher` to determine whether the shortcut should be hidden from the launcher. ([Ia2a71](https://android-review.googlesource.com/#/q/Ia2a7147fab366308c392eb3dcf0cc6122d7f6181))
- Add `NotificationCompat.Action#setAuthenticationRequired` ([Ieeafa](https://android-review.googlesource.com/#/q/Ieeafaea3a880bf04e81320a5b944272e65804d01), [b/202172887](https://issuetracker.google.com/issues/202172887))
- Add `NotificationCompat.BigPictureStyle.setContentDescription` ([I3b483](https://android-review.googlesource.com/#/q/I3b483c4ac9b282f3f20f22effe4579363b633fda))
- Added extension function `Map<String, Any?>.toPersistableBundle()` ([I82c86](https://android-review.googlesource.com/#/q/I82c867ee5f5c22332fd0db8bbf8b9ca5e67229aa))

**Bug Fixes**

- Adjusts the scroll distance for accessibility action ([If74ae](https://android-review.googlesource.com/#/q/If74ae6f6d204f2b238998a31154abf61f8167d11))
- Removed hardcoded language code in Javadocs ([Ie5d68](https://android-review.googlesource.com/#/q/Ie5d6865dfeb20562647aff50f1a4c0d33a642efa))

## Core and Core-ktx Version 1.7

### Version 1.7.0

October 27, 2021

`androidx.core:core:1.7.0` and `androidx.core:core-ktx:1.7.0` are released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7376f60e84b9c218cd791c4abfac43a605f6c078..f01b06dda22df8afd990b500c0663bf83df78a52/core)

**Important changes since 1.6.0**

- Adds support for interacting with SDK 30 and later's permission revocation and app hibernation features, with backporting down to SDK 23 on supported devices. See [IntentCompat.createManageUnusedAppRestrictionsIntent](https://developer.android.com/reference/androidx/core/content/IntentCompat#createManageUnusedAppRestrictionsIntent(android.content.Context,%20java.lang.String)) for more information.
- Adds support for composing menu support in components, see [MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider) for more information.

### Version 1.7.0-rc01

October 13, 2021

`androidx.core:core:1.7.0-rc01` and `androidx.core:core-ktx:1.7.0-rc01` are released. [Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..7376f60e84b9c218cd791c4abfac43a605f6c078/core)

### Version 1.7.0-beta02

September 29, 2021

`androidx.core:core:1.7.0-beta02` and `androidx.core:core-ktx:1.7.0-beta02` released. [Version 1.7.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/core/core)

**Bug Fixes**

- `MenuHostHelper` will now properly remove all LifecycleObservers when a `MenuProvider` is removed prior to the Lifecycle being `DESTROYED`. ([Ibe2e1](https://android-review.googlesource.com/#/q/Ibe2e1f4a29c8079549814aaaa9b2484c22a41b2e), [b/199788262](https://issuetracker.google.com/issues/199788262))
- Update the descriptions of the Unused App Restrictions Constants to be clearer for developers ([I2858e](https://android-review.googlesource.com/#/q/I2858ef1f550acb64952f4ffae5c6d38f41e9569c))

### Version 1.7.0-beta01

September 15, 2021

`androidx.core:core:1.7.0-beta01` and `androidx.core:core-ktx:1.7.0-beta01` are released. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/core)

**API Changes**

- `LocationRequestCompat.toProvider` can now return null ([Ib5a09](https://android-review.googlesource.com/#/q/Ib5a09418f0a795746c142fbd3677da4e40e7b421))

### Version 1.7.0-alpha02

September 1, 2021

`androidx.core:core:1.7.0-alpha02` and `androidx.core:core-ktx:1.7.0-alpha02` are released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..47e81d1c497b8a57534a460c277855db1b0257ae/core)

**New Features**

- Streamlining and unification of how lifecycle-aware menus are managed, see MenuProvider for more details.

**API Changes**

- Added `MenuHost` interface for components that manage `MenuProvider`s. ([I83f23](https://android-review.googlesource.com/#/q/I83f23a17b112d2bdc85d1732fa6efcf32eb67ddd))
- Added `MenuProvider` interface that can be used to indicate that a component is supplying menu items. ([If8a40](https://android-review.googlesource.com/#/q/If8a40bc3edd37897cfaa1eed78c1c288b80c13c3))
- Added `MenuHostHelper` to simplify implementing `MenuHost` in a component. ([I74f4a](https://android-review.googlesource.com/#/q/I74f4ae6ab5ef63c51b4f982b6a334bba5bb0dfc2))
- Added `LocationRequestCompat.toLocationRequest()` for converting to platform class. ([I71e75](https://android-review.googlesource.com/#/q/I71e7543c4d764487fe362df5d605097d3a295b33))
- Added `DocumentsContractCompat` class for parity with platform APIs. ([Ia9e91](https://android-review.googlesource.com/#/q/Ia9e913676b58653492ca6897473d1a74d1fb4e5e))
- Added `NotificationCompat.BigPictureStyle.showBigPictureWhenCollapsed(boolean)` for parity with platform APIs. ([I8cd88](https://android-review.googlesource.com/#/q/I8cd88f42564e08fbad3bf8ae0c194ef872e62cbd))
- Fixed an issue where `checkSelfPermission` from `PermissionChecker` would show mic/cam indicators. ([I572a9](https://android-review.googlesource.com/#/q/I572a9c6e2c86d435ba22b42db888c021abcd888f))
- Added explicit threading annotation for `setImportantForAccessibility`. ([I990fa](https://android-review.googlesource.com/#/q/I990faac25c6136591f97c8d4cdea0b3372f51af2))
- Updated `getUnusedAppRestrictionsStatus` to conform to API guidelines. ([I28a18](https://android-review.googlesource.com/#/q/I28a1880547ccc73f04d1bb255b5e15bc841cd239))
- Completed functionality for `getUnusedAppRestrictionsStatus`. ([I7c2d6](https://android-review.googlesource.com/#/q/I7c2d63bb73588c8db98fdde4b13be652df699b4a))
- Added support to `LocationCompat` for vertical accuracy, speed accuracy, and bearing accuracy. ([I1d3e9](https://android-review.googlesource.com/#/q/I1d3e9ee37addf2c51fad17afb13c35fc46c4402e))
- Added math compat functions to `MathUtils`. ([Idb590](https://android-review.googlesource.com/#/q/Idb590f4b897a3cdeadbc6e84b3386d0c6031bdf6))
- Integrated `OnReceiveContentListener`into compat APIs. ([Ic6914](https://android-review.googlesource.com/#/q/Ic6914c23688b4165c81ffa19a7dbce89d52bffcd), [b/173814913](https://issuetracker.google.com/issues/173814913))
- Added `ActivityCompat#isLaunchedFromBubble` for platform parity. ([I6961a](https://android-review.googlesource.com/#/q/I6961ad810fdaf5b656647198f3026dffeee84de5))
- Added `LocationRequest` and `LocationManager.hasProvider()` for platform parity. ([I4f3e4](https://android-review.googlesource.com/#/q/I4f3e488fa561d8182485a264829e55f088a0b02b))

**Bug Fixes**

- Removed the use of lambdas in `PackageManagerCompat` to avoid `LambdaDesugaring` bug. ([I36c87](https://android-review.googlesource.com/#/q/I36c875108090468d2e66cc4d8a54402eb0d905f9))

### Version 1.7.0-alpha01

June 30, 2021

`androidx.core:core:1.7.0-alpha01` and `androidx.core:core-ktx:1.7.0-alpha01` are released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/core)

**API Changes**

- Added an API to configure an InputConnection to use `View.performReceiveContent` to handle IME calls to `InputConnection.commitContent`. ([I3a2ad](https://android-review.googlesource.com/#/q/I3a2ad7604145a6aba74ee7a020075f0bd3ecc266))
- Combined two APIs' functionality into one ([I261df](https://android-review.googlesource.com/#/q/I261dfbd46527e614a529d9a0dbe66aaa3719c45a))
- Modified two APIs' functionality for use with unused app restriction features (e.g. permission revocation, app hibernation) ([Ic1616](https://android-review.googlesource.com/#/q/Ic1616627069c0c22facc3312c7dd321132a17c53))
- Added three APIs for use with unused app restriction features (e.g. permission revocation, app hibernation) ([I606d7](https://android-review.googlesource.com/#/q/I606d713316a76b9be2386b7b0b2d0ae774fb474d))
- Added nullability annotations to several Compat classes ([I2802a](https://android-review.googlesource.com/#/q/I2802ac396ea7eeea0f9d8bf53c5fe6dbc0818541), [b/188452327](https://issuetracker.google.com/issues/188452327), [b/189962089](https://issuetracker.google.com/issues/189962089))
- Added three APIs for use with unused app restriction features (e.g. permission revocation, app hibernation) ([Icafee](https://android-review.googlesource.com/#/q/Icafee958d632200b24b1051dc313181de90c2be4))
- Addressed missing nullability annotation issues in ViewCompat ([Ic346e](https://android-review.googlesource.com/#/q/Ic346e32a79f8de1c49fe957ae387b0b88855c2d7), [b/188453571](https://issuetracker.google.com/issues/188453571))

## Core Remote Views Version 1.1

### Version 1.1.0

June 12, 2024

`androidx.core:core-remoteviews:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16fcdbc19dd53423937bad83094a24f4e901e57e..c9ba94cdd70f8dc09ace9bb042e815e7a6f77703/core/core-remoteviews).

**Important changes since 1.0.0**

- Core `RemoteViews` moves to 1.1.0 stable.

### Version 1.1.0-rc01

May 14, 2024

`androidx.core:core-remoteviews:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..16fcdbc19dd53423937bad83094a24f4e901e57e/core/core-remoteviews).

**New Features**

- Move `RemoteViews` 1.1.0 to Release Candidate.

**Bug Fixes**

- Move to 21 as the default `minSdkVersion` of androidx libraries. ([I6ec7f](https://android-review.googlesource.com/#/q/I6ec7f80aafbe04c64c8f2d8fef82d4cd5c68525e))

### Version 1.1.0-beta02

April 17, 2024

`androidx.core:core-remoteviews:1.1.0-beta02` is released. No major changes since the last release.

### Version 1.1.0-beta01

April 3, 2024

`androidx.core:core-remoteviews:1.1.0-beta01` is released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..004c95266df8aecba9fe14005b1d2fc108c463cf/core/core-remoteviews).

### Version 1.1.0-alpha01

February 7, 2024

`androidx.core:core-remoteviews:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f72d6d1deb52aa48f013d24118a9b0469a2fb839..ca2a8cf8da3a3502fccc593974f8085653e38261/core/core-remoteviews)

**New Features**

- Version bump to match dependency versions.

## Core Remote Views Version 1.0

### Version 1.0.0

September 6, 2023

`androidx.core:core-remoteviews:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/acde076f20ad5d7d8e2d2894b29c6c1464d0665e..f72d6d1deb52aa48f013d24118a9b0469a2fb839/core/core-remoteviews)

**Major features of 1.0.0**

- Move core-remoteviews to stable version 1.0.0

### Version 1.0.0-beta04

May 10, 2023

`androidx.core:core-remoteviews:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..f8115b4c10e1f8af23cdef2e7bc36dae358c9808/core/core-remoteviews)

**Bug Fixes**

- Fixes `ArrayOutOfBoundsException` being thrown in corner cases in compat library.

### Version 1.0.0-beta03

October 5, 2022

`androidx.core:core-remoteviews:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/core/core-remoteviews)

**New Features**

- No new features were added.

### Version 1.0.0-beta02

August 10, 2022

`androidx.core:core-remoteviews:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..bea814b246f89ff7244e3c6b0648f0b57e47897c/core/core-remoteviews)

**Bug Fixes**

- Version fix

### Version 1.0.0-beta01

June 29, 2022

`androidx.core:core-remoteviews:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..8094b683499b4098092c01028b55a38b49e357f2/core/core-remoteviews)

**New Features**

- Moves `Core-RemoteViews` to beta.

### Version 1.0.0-alpha03

February 23, 2022

`androidx.core:core-remoteviews:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/core/core-remoteviews)

**Bug Fixes**

- Fix for infrastructure.

### Version 1.0.0-alpha02

January 26, 2022

`androidx.core:core-remoteviews:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..9dceceb54300ed028a7e8fc7a3454f270337ffde/core/core-remoteviews)

### Version 1.0.0-alpha01

December 15, 2021

`androidx.core:core-remoteviews:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f/core/core-remoteviews)

**New Features**

- Backport of the new `RemoteViews.setRemoteAdapter` API.
- Kotlin Extension functions to avoid reflection when calling `RemoteViews` methods.
- Library with helper functions for working with `App Widget` sizing APIs.

## Core Performance Version 1.0

### Version 1.0.0

January 10, 2024

`androidx.core:core-performance:1.0.0`, `androidx.core:core-performance-play-services:1.0.0`, and `androidx.core:core-performance-testing:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c6f4fc030b2419567fea6628122e1f39432d1a3..896cdb98fff309410bc1bab9f46188a70bb1af3b/core)

**Major features of 1.0.0**

- **Core Performance** - Provides a reliable mechanism for developers to identify the device's level of performance at runtime to help optimize an app's user experience accordingly.
- **Core Performance Play Services** - Google-specific implementation providing up-to-date media performance class information for tested devices and OS versions.
- **Core Performance Testing** - Test doubles for Core Performance.

**Bug Fixes**

- Fixed a crash when initializing `PlayServicesDevicePerformance` found in version `1.0.0-beta2`. ([b/318803680](https://issuetracker.google.com/318803680))

### Version 1.0.0-rc01

December 13, 2023

`androidx.core:core-performance:1.0.0-rc01`, `androidx.core:core-performance-play-services:1.0.0-rc01`, and `androidx.core:core-performance-testing:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..9c6f4fc030b2419567fea6628122e1f39432d1a3/core)

**New Features**

- Core Performance - Updated library implementation. (`DevicePerformance` generic implementation).
- Core Performance Play Services - Initial library implementation. (Google specific `DevicePerformance` implementation).
- Core Performance Testing - Initial library implementation. (contains test doubles for Core Performance).

**API Changes**

- Initial RC release of `DevicePerformance` specific API.

### Version 1.0.0-beta02

October 4, 2023

`androidx.core:core-performance:1.0.0-beta02`, `androidx.core:core-performance-play-services:1.0.0-beta02`, and `androidx.core:core-performance-testing:1.0.0-beta02` are released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a642731f2e12d8256c8eebb3298c92064e93e9d0..1f7407d4293384a1b91bc142880e3525048b3443/core)

**New Features**

- Test related refactoring.

**API Changes**

- Unchanged API usage pattern.

### Version 1.0.0-beta01

September 6, 2023

`androidx.core:core-performance:1.0.0-beta01`, `androidx.core:core-performance-play-services:1.0.0-beta01`, and `androidx.core:core-performance-testing:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a642731f2e12d8256c8eebb3298c92064e93e9d0/core)

**New Features**

- Core Performance - Updated library implementation. (`DevicePerformance` generic implementation).
- Core Performance Play Services - Initial library implementation. (Google specific `DevicePerformance` implementation).
- Core Performance Testing - Initial library implementation. (contains test doubles for Core Performance).

**API Changes**

- Initial beta release of `DevicePerformance` specific API.

### Version 1.0.0-alpha03

August 23, 2023

`androidx.core:core-performance:1.0.0-alpha03`, `androidx.core:core-performance-play-services:1.0.0-alpha03`, and `androidx.core:core-performance-testing:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5/core)

**New Features**

- Initial library implementation of `core-performance-testing`, containing test doubles for core-performance.
- Initial library implementation or `core-performance-play-services`. Google specific implementation provides up to date media performance class information.

**API Changes**

- Add optional module providing media performance class from Google Play Services.
- core-performance constructors changed to support optional implementation.

### Version 1.0.0-alpha02

March 23, 2022

`androidx.core:core-performance:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/06ef778a6fb9a726319016bd80d441a13c3e851c/core/core-performance)

**New Features**

- Provide an easy and reliable mechanism for developers to identify at runtime the device's level of performance in order to deliver an optimized app experience.
- This initial release uses a list of hand-tested devices that are granted performance class values higher than the level declared in Build.VERSION.MEDIA_PERFORMANCE_CLASS

### Version 1.0.0-alpha01

December 15, 2021

`androidx.core:core-performance:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f/core/core-performance)

## Core Splashscreen Version 1.2

### Version 1.2.0

November 05, 2025

`androidx.core:core-splashscreen:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/40e5626dcdec536576fecb4158c54e929329f682..39e25369b3a6dd0b08038933f4c1b15af324b339/core/core-splashscreen).

### Version 1.2.0-rc01

July 2, 2025

`androidx.core:core-splashscreen:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..207e91042ce50586697faf3838c2c0a808e99799/core/core-splashscreen).

### Version 1.2.0-beta02

April 23, 2025

`androidx.core:core-splashscreen:1.2.0-beta02` is released. Version 1.2.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/core/core-splashscreen).

### Version 1.2.0-beta01

February 26, 2025

`androidx.core:core-splashscreen:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..fd7408b73d9aac0f18431c22580d9ab612278b1e/core/core-splashscreen).

### Version 1.2.0-alpha02

September 4, 2024

`androidx.core:core-splashscreen:1.2.0-alpha02` is released. Version 1.2.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/core/core-splashscreen).

**Bug Fixes**

- Add `isLightTheme` attribute to themes of `SplashScreen` ([I01000](https://android-review.googlesource.com/#/q/I010005266ec4b1dae815937ab0fcf28bb7d05267), [b/238522114](https://issuetracker.google.com/issues/238522114))
- Get splashscreen icon by `AppCompatResources` ([Ib05e](https://android-review.googlesource.com/q/Ib05e2e7da40ee7c7db39ff8512cfa97861b7ee3e), [b/289242141](https://issuetracker.google.com/issues/289242141), [b/263972037](https://issuetracker.google.com/issues/263972037))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ieb9ae](https://android-review.googlesource.com/#/q/Ieb9aecd2af5587c5b82833146fee6e912693ab7b), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.2.0-alpha01

April 17, 2024

`androidx.core:core-splashscreen:1.2.0-alpha01` is released. Version 1.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7f975047c0a7af9fdb0221a6ceaa3eb76b447a44..67004410fdbff19f90caa4cc43965ab21dca1943/core/core-splashscreen).

**Bug Fixes**

- Change the cutout mode of `Base.Theme.SplashScreen` to always since v30.([Idfc3f](https://android.googlesource.com/platform/frameworks/support/+/135f0021da98da2c3538eecd70399bf17d974847))
- Reset `enforceNavigationBarContrast` to system default value from API 31, so the splash screen theme won't corrupt activity's theme. From API 31+, the splash screen isn't create as `PhoneWindow`, so it's unnecessary to inherit the value from API 29. Also remove the override action from `applyAppSystemUiTheme`, since `enforceNavigationBarContrast` could already changed from app side during launch, override it from attribute doesn't make sense.([Ic2cd9](https://android.googlesource.com/platform/frameworks/support/+/325cd02adee5c75aba49d9e81b42b43ac136aad3))
- Set default light navigation bar which respects day/night theme. So for API 33+ platform, the splash screen theme won't cause flicker while removing the splash screen. ([I8023a](https://android-review.googlesource.com/#/q/I8023a149e46dd09a91bc4961acef4ad5d24617a9))
- Do not overwrite activity theme after receiving the splash screen view from api 33.([I10587b](https://android.googlesource.com/platform/frameworks/support/+/68b6d8d5d892f99429f626f07a13c022a7f330a9))

## Core Splashscreen Version 1.1

### Version 1.1.0-rc01

April 3, 2024

`androidx.core:core-splashscreen:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..7f975047c0a7af9fdb0221a6ceaa3eb76b447a44/core/core-splashscreen).

**Bug Fixes**

- Provide default dimensions for wear device with 48x48dp icon ([Ib8de8](https://android-review.googlesource.com/#/q/Ib8de8f78ea1d1dbe67cbc2d8de0388f5cfeb6c7e), [b/256678037](https://issuetracker.google.com/issues/256678037))
- Fix `SplashScreenView#getIconView` cause NPE crash ([6abfd6](https://android.googlesource.com/platform/frameworks/support/+/6abfd6f3f06ff68ad690fa61667189416652b9c2), [b/243457485](https://issuetracker.google.com/issues/243457485))

### Version 1.1.0-alpha02

September 6, 2023

`androidx.core:core-splashscreen:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a0de71cb4a653fcaf8d0018ded4e4bdc18fdf59a..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/core/core-splashscreen)

**Bug Fixes**

- Provide default dimensions for wear device with 48x48dp icon ([Ib8de8](https://android-review.googlesource.com/#/q/Ib8de8f78ea1d1dbe67cbc2d8de0388f5cfeb6c7e), [b/256678037](https://issuetracker.google.com/issues/256678037))

**Dependency Update**

- Core-Splashscreen now compiles against API 34.

### Version 1.1.0-alpha01

February 22, 2023

`androidx.core:core-splashscreen:1.1.0-alpha01` is released. This was developed in an internal branch.
| **Note:** This compiles against Android UDC DP1 SDK

**Bug Fixes**

- Fixed a `NullPointerException` when `SplashScreenView#getIconView` returned null. ([e231ab](https://android.googlesource.com/platform/frameworks/support/+/e231abf4623dd97b75b35ded10e6016ca57e8668))

## Core Splashscreen Version 1.0

### Version 1.0.1

April 19, 2023

`androidx.core:core-splashscreen:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87e71786a0e17a298b20b58eb719153d4260978a..15d14fb25653b741f5631975fb315782f6b7e5db/core/core-splashscreen)

**Bug Fixes**

- Provide default dimensions for wear device with 48x48dp icon ([Ib8de8](https://android-review.googlesource.com/#/q/Ib8de8f78ea1d1dbe67cbc2d8de0388f5cfeb6c7e), [b/256678037](https://issuetracker.google.com/issues/256678037))

### Version 1.0.0

July 27, 2022

The core SplashScreen library brings the new Android 12 splash screen to all devices from API 23. Using the splash screen library, your application doesn't need any custom SplashScreen Activity and leverages the right APIs for a fast launch of your application. To use it, simply follow the steps outlined in our [guide](https://developer.android.com/guide/topics/ui/splash-screen/migrate#migrate_your_splash_screen_implementation). For more information about the Android 12 splash screen, visit the [official documentation](https://developer.android.com/guide/topics/ui/splash-screen).

`androidx.core:core-splashscreen:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b8f90710aba0a775d0bbabb0eed20f4573c0a48d..87e71786a0e17a298b20b58eb719153d4260978a/core/core-splashscreen)

### Version 1.0.0-rc01

May 18, 2022

`androidx.core:core-splashscreen:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..b8f90710aba0a775d0bbabb0eed20f4573c0a48d/core/core-splashscreen)

- No changes since the last beta release.

### Version 1.0.0-beta02

March 23, 2022

`androidx.core:core-splashscreen:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f026ea82f7a4e53be13bae47ad5e5985a688f8c4..5ef5671233460b844828e14a816255dbf7904868/core/core-splashscreen)

**Bug Fixes**

- Fixed `Lateinit property platformView has not been initialized` ([b/214835299](https://issuetracker.google.com/214835299))

**External Contribution**

- Fix rendering issue on MIUI with dark mode and Explicitly set `android:animateLayoutChanges` to false to avoid the fading animation when removing the splash screen in the `OnExitAnimationListener` ([#327](https://github.com/androidx/androidx/pull/327))

### Version 1.0.0-beta01

January 12, 2022

`androidx.core:core-splashscreen:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..f026ea82f7a4e53be13bae47ad5e5985a688f8c4/core/core-splashscreen)

**Bug Fixes**

- Better night mode handling ensures that night mode is handled when the default parameters are used on all APIs. [2d1d182](https://android.googlesource.com/platform/frameworks/support/+/2d1d1822fb2a48aa023ed0db5c8b6460b16760f6)

Fixes bugs introduced in the new splash screen on Android 12:

- Fix systemBar flickering on API 31: Ensure that the system bars do not flicker when customizing the exit animation. [5a75362](https://android.googlesource.com/platform/frameworks/support/+/5a75362dc96ccaebf9a431c8facd899e1bb5ae34)
- Fix insets handling when using OnExitAnimationListener: Ensures that the content does not jump when the OnExitAnimationListener is used. [4c8f264](https://android.googlesource.com/platform/frameworks/support/+/4c8f26482c4c4d136e75e327730914e6388c0373)

### Version 1.0.0-alpha02

September 29, 2021

`androidx.core:core-splashscreen:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5101d5e8e377589f71c5b9a6c48a7031978c0823..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/core/core-splashscreen)

**New Features**

- Better insets support: The splash screen now shows full screen on all APIs even when the `OnExitAnimationListener` is set.
- `postSplashScreenTheme` is optional: you can simply call `activity.setTheme()` before `onCreate()` to set your app theme after the splash screen is shown.
- Backward support of the `windowSplashScreenIconBackgroundColor` attribute: using `Theme.SplashScreen.IconBackground` and `windowSplashScreenIconBackgroundColor`, you can add a background to the splash screen icon.
- The sizing of the icon has been corrected to match the platform's specs.

**API Changes**

- Added backward compatibility for the windowSplashScreenIconBackgroundColor attribute
  - Downgraded the minSdkVersion to API 21 ([Idd050](https://androidAndroid-review.googlesource.com/#/q/Idd05037fbc481ca80217c50b6e9bf64a16d90cd4), [b/198161849](https://issuetracker.google.com/issues/198161849), [b/197759820](https://issuetracker.google.com/issues/197759820), [b/198165621](https://issuetracker.google.com/issues/198165621))

**Bug Fixes**

- Make `postSplashScreenTheme` optional ([I8c4bf](https://android-review.googlesource.com/#/q/I8c4bfbdae7937ba03d2a657810bc23c322d00547))

### Version 1.0.0-alpha01

June 30, 2021

`androidx.core:core-splashscreen:1.0.0-alpha01` is released.

**New Features**

- `core-splashscreen` provides backward compatibility for the new [Splash Screen APIs](https://developer.android.com/about/versions/12/features/splash-screen). This first alpha version contains all the new APIs backported down to API 23, with the exception of the icon background.
- See the KDocs in `androidx.core.splashscreen` for usage information.

## Core Google Shortcuts Version 1.2

### Version 1.2.0-alpha01

July 26, 2023

`androidx.core:core-google-shortcuts:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7bc6d4ae02658b1e9c7ae11e14cc36ad550e059..4aed940027a19667e67d155563fc5fa8b7279313/core/core-google-shortcuts)

**API Changes**

- Merged public and experimental API files for a,b,c-paths ([I8cfee](https://android-review.googlesource.com/#/q/I8cfeeb37f9952db225e8d1eea6f471a920ac1dda), [b/278769092](https://issuetracker.google.com/issues/278769092))
- Migrated `androidx.core` group to use merged public API files ([Ifdef4](https://android-review.googlesource.com/#/q/Ifdef4c6a6b2828cba776b82672f2fc0e02c3b3b8), [b/278769092](https://issuetracker.google.com/issues/278769092))

## Core Google Shortcuts Version 1.1.0

### Version 1.1.0

October 24, 2022

`androidx.core:core-google-shortcuts:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2885eebbc42a35263057c1f1d95eecb317051476..a7bc6d4ae02658b1e9c7ae11e14cc36ad550e059/core/core-google-shortcuts)

**Important changes since 1.0.0**

- Migrated from using `com.google.firebase:firebase-appindexing` to the new `com.google.android.gms:play-services-appindex` library. This version of the library is not compatible with `com.google.firebase:firebase-appindexing`. Developers should avoid using both libraries to avoid build errors.

### Version 1.1.0-rc01

October 5, 2022

`androidx.core:core-google-shortcuts:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..2885eebbc42a35263057c1f1d95eecb317051476/core/core-google-shortcuts)

**New Features**

- Migrated from using `com.google.firebase:firebase-appindexing` to the new `com.google.android.gms:play-services-appindex` library. Note that this version of the library is not compatible with `com.google.firebase:firebase-appindexing`. Developers should avoid using both libraries to avoid build errors.

### Version 1.1.0-beta01

September 21, 2022

`androidx.core:core-google-shortcuts:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/core/core-google-shortcuts)

**New Features**

- Removed unused dependency. No new features.

### Version 1.1.0-alpha03

September 7, 2022

`androidx.core:core-google-shortcuts:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..cce7b70f6a5ebf955cf748a73c18b63228b22c74/core/core-google-shortcuts)

**New Features**

- Removed unused dependency. No new features.

### Version 1.1.0-alpha02

August 24, 2022

`androidx.core:core-google-shortcuts:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..dd1e45e8550560087f6447a34a9145048b5766f4/core/core-google-shortcuts)

**New Features**

- Update dependency from `com.google.firebase:firebase-appindexing` to `com.google.android.gms:play-services-appindex`. Developers who use this new version should not externally depend on `com.google.firebase:firebase-appindexing`, as the two libraries are now incompatible.

### Version 1.1.0-alpha01

August 4, 2021

`androidx.core:core-google-shortcuts:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/720ae3dd8b52a9505c88d436616c421214a389c3..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/core/core-google-shortcuts)

**New Features**

- Indexing support for URI based icons in Donated shortcuts to be displayed by Google apps.

## Core and Core-ktx Version 1.6.0

### Version 1.6.0

June 30, 2021

`androidx.core:core:1.6.0` and `androidx.core:core-ktx:1.6.0` are released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1929191a5c85958db81053e26e57c676644f6327..0a69de9e5eb38cf444cfc8ccda27044205bf3f50/core)

**Important changes since 1.5.0**

- Add support for resolving theme attributes in nested `ColorStateList`s. ([I2e409](https://android-review.googlesource.com/q/I2e4098d45173a443dda97a23923c02755e83acfb) [b/155579892](https://issuetracker.google.com/issues/155579892))
- Backport tintable background and check mark for CheckedTextView ([I8575c](https://android-review.googlesource.com/#/q/I8575c5c23240a14153654ffafd0387fa89f2a3bc))

### Version 1.6.0-rc01

June 16, 2021

`androidx.core:core:1.6.0-rc01` and `androidx.core:core-ktx:1.6.0-rc01` are released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..1929191a5c85958db81053e26e57c676644f6327/core)

**API Changes**

- JobIntentService has been deprecated in favor of WorkManager ([Ic7749](https://android-review.googlesource.com/#/q/Ic7749b06bf8365cb949cfd0139d3d4fae1e129c3), [b/149049019](https://issuetracker.google.com/issues/149049019))

### Version 1.6.0-beta02

June 2, 2021

`androidx.core:core:1.6.0-beta02` and `androidx.core:core-ktx:1.6.0-beta02` are released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/core/core)

**Bug Fixes**

- Update `BuildCompat` to use current long press timeout on latest platforms ([b/185118174](https://issuetracker.google.com/issues/185118174))
- Remove use of `synchronized` from `ContextCompat`, `ContentLoadingProgress` methods.

### Version 1.6.0-beta01

May 18, 2021

`androidx.core:core:1.6.0-beta01` and `androidx.core:core-ktx:1.6.0-beta01` are released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/core)

**API Changes**

- Backport `Objects.requireNonNull()` ([I27db5](https://android-review.googlesource.com/#/q/I27db535da3a0171d221bd781337f20f2b4a61fbd), [b/179904366](https://issuetracker.google.com/issues/179904366))

### Version 1.6.0-alpha03

May 5, 2021

`androidx.core:core:1.6.0-alpha03` and `androidx.core:core-ktx:1.6.0-alpha03` are released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/902e5b7442704f108ee9ea59ebbde4282d710ca8..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/core)

**New Features**

- Add support for resolving theme attributes in nested `ColorStateList`s. ([I2e409](https://android-review.googlesource.com/q/I2e4098d45173a443dda97a23923c02755e83acfb) [b/155579892](https://issuetracker.google.com/issues/155579892))

**Bug Fixes**

- Prevent NPE when handling `null` custom selection action mode callbacks on AppCompat-backed views. ([I033c7](https://android-review.googlesource.com/#/q/I033c712ffa477853f122788f2335e7cab9a877fb), [b/173435375](https://issuetracker.google.com/issues/173435375))

- Add support for setSystemBarsBehavior on SDK \< 30. ([I062c8](https://android-review.googlesource.com/q/I062c841f0e4201fddfcf1489dbfaff605bebbdb6), [b/173203649](https://issuetracker.google.com/issues/173203649))

### Version 1.6.0-alpha02

April 15, 2021

`androidx.core:core:1.6.0-alpha02` and `androidx.core:core-ktx:1.6.0-alpha02` are released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..079dd60d7d581a10fe71f976c3194c150ef1dd58/core)

**API Changes**

- Add `TelephoneManagerCompat` and `SubscriptionManagerCompat` ([I5568d](https://android-review.googlesource.com/#/q/I5568d5ef665d140ec998adbbf7681870a1c84ee2))
- Remove deprecated `addCapabilityBinding` method from `ShortcutInfoCompat` ([Ie8f70](https://android-review.googlesource.com/#/q/Ie8f70595bd410b6db5d4473f78d9423f4d7ea10c))
- Add `addCapabilityBinding` with parameters and `addCapabilityBinding` without parameters setters to `ShortcutInfoCompat.Builder`, deprecated old `addCapabilityBinding` ([I90686](https://android-review.googlesource.com/#/q/I906865532502b3bc2246bc79d32e64d7a2173c8f))
- Add `LocationCompat` class and `LocationManagerCompat.getCurrentLocation()` ([I78d9a](https://android-review.googlesource.com/#/q/I78d9ad233c3381477612bb9b382ca0cb60ce01a6))
- Deprecated `ModeCompat.isNative` which is replaced by `DisplayCompat.getMode`. ([I9a6a2](https://android-review.googlesource.com/#/q/I9a6a2cc601ac0fb41501ef5ac9e0aaa105a9d11d))
- Added `ContextCompat.getAttributionTag()` and `UserHandleCompat.getUserHandleForUid()` ([Iea486](https://android-review.googlesource.com/#/q/Iea4861c037732310318f97c359206a704573777a))

**External Contribution**

- Backport tintable background and check mark for `CheckedTextView` ([I8575c](https://android-review.googlesource.com/#/q/I8575c5c23240a14153654ffafd0387fa89f2a3bc))

### Version 1.6.0-alpha01

March 24, 2021

`androidx.core:core:1.6.0-alpha01` and `androidx.core:core-ktx:1.6.0-alpha01` are released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d84c0393bf1b89f62643ffc60b5e2318ec30298e..5c42896eb6591b09e3952030fb7ea8d9b8c42713/core)

**API Changes**

- Adds `Handler.hasCallbacks()` method for parity with platform SDK ([Idce1c](https://android-review.googlesource.com/#/q/Idce1c9fbe0d93bd9ebcb26716a63834bb1c4c12d), [b/113855676](https://issuetracker.google.com/issues/113855676))
- Adds capability related setter methods to `ShortcutInfoCompat.Builder` ([I45af6](https://android-review.googlesource.com/#/q/I45af6c6b3ee63e9ca09574a607d06817167d7b60))

## Core Google Shortcuts Version 1.0

### Version 1.0.1

May 18, 2022

`androidx.core:core-google-shortcuts:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/720ae3dd8b52a9505c88d436616c421214a389c3..2651c095c4b4fc97349aac2631ae60879d0aa8a8/core/core-google-shortcuts)

**Bug Fixes**

- Fix proguard rule to prevent a method from being unintentionally removed

### Version 1.0.0

June 30, 2021

`androidx.core:core-google-shortcuts:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ef7e096b90aa07e9f382378bc871febb3c8a70fb..720ae3dd8b52a9505c88d436616c421214a389c3/core/core-google-shortcuts)

**Major features of 1.0.0**

Include this module to allow shortcuts saved using [ShortcutManagerCompat](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat) to also be donated to Google. This will unlock additional features with those shortcuts for users, such as displaying them as suggestions or allowing Google Assistant to fulfill them through voice query. There is no limit to the number of shortcuts that can be donated, and those that are donated this way are saved on-device. For more information, see the full documentation on [pushing dynamic shortcuts to Assistant](https://developers.google.com/assistant/app/dynamic-shortcuts).

### Version 1.0.0-rc01

June 16, 2021

`androidx.core:core-google-shortcuts:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..ef7e096b90aa07e9f382378bc871febb3c8a70fb/core/core-google-shortcuts)

### Version 1.0.0-beta01

May 18, 2021

`androidx.core:core-google-shortcuts:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..66681ad83c328d0dd821b943bb3d375f02c1db61/core/core-google-shortcuts)

**New Features**

- Shortcuts added via `core-google-shortcuts` library will be saved as a Shortcut object in firebase appindexing, instead of a generic schema.org/Thing object.

**Bug Fixes**

- Removed the minSdkVersion requirement from the library. The library will still only work for API version 21 and above, but apps will no longer be required to set their own app's minSdkVersion to 21.

### Version 1.0.0-alpha03

May 5, 2021

`androidx.core:core-google-shortcuts:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/902e5b7442704f108ee9ea59ebbde4282d710ca8..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/core/core-google-shortcuts)

**Bug Fixes**

- No longer automatically report shortcut usage when a shortcut is added / updated. Instead usage reporting will be moved to `ShortcutManagerCompat#pushDynamicShortcut`.

### Version 1.0.0-alpha02

April 15, 2021

`androidx.core:core-google-shortcuts:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/902e5b7442704f108ee9ea59ebbde4282d710ca8/core/core-google-shortcuts)

**New Features**

- By depending on `androidx.core:core-google-shortcuts` as an optional component along with `androidx.core`; you can start using `ShortcutManagerCompat` to donate shortcuts to be used by Google.
- A new TrampolineActivity will be merged with apps depending on this module. The TrampolineActivity is used to open shortcuts donated by this module.

**API Changes**

- Added `ShortcutInfoChangeListenerImpl`, to be used by `ShortcutManagerCompat` to donate shortcuts to Firebase App Index.

## Core and Core-ktx Version 1.5.0

| **Note:** This version will only compile against the Android 11 SDK.

### Version 1.5.0

May 18, 2021

`androidx.core:core:1.5.0` and `androidx.core:core-ktx:1.5.0` are released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d71649df1a2eceeb1c1b0aa28eddc59707515ffe..a2ec52055df87fce6602c6381d7b45ef27021f25/core)

**Important changes since 1.4.0**

- Support for new Insets Animation APIs
- Updates to `OnReceiveContentListener` to support rich content
- Backported `WindowInsetsController` and `WindowInsetsCompat` APIs to control system bar appearance
- Updated `ActivityCompat.recreate()` to be safely called from any lifecycle state on any API level
- Added APIs to supply and retrieve initial surrounding text via `EditorInfoCompat`, which allows IME apps to avoid additional IPC latency.
- Various updates to improve parity with platform SDK APIs

### Version 1.5.0-rc02

May 5, 2021

`androidx.core:core:1.5.0-rc02` and `androidx.core:core-ktx:1.5.0-rc02` are released. [Version 1.5.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4cb15fdc3d603b2628e4bfe9c57a72dea59b7e8..d71649df1a2eceeb1c1b0aa28eddc59707515ffe/core)

**Bug Fixes**

- Add support for setSystemBarsBehavior on SDK \< 30. ([I062c8](https://android-review.googlesource.com/q/I062c841f0e4201fddfcf1489dbfaff605bebbdb6), [b/173203649](https://issuetracker.google.com/issues/173203649))

### Version 1.5.0-rc01

March 24, 2021

`androidx.core:core:1.5.0-rc01` and `androidx.core:core-ktx:1.5.0-rc01` are released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d84c0393bf1b89f62643ffc60b5e2318ec30298e..d4cb15fdc3d603b2628e4bfe9c57a72dea59b7e8/core)

**Summary**

- No changes from previous beta03

### Version 1.5.0-beta03

March 10, 2021

`androidx.core:core:1.5.0-beta03` and `androidx.core:core-ktx:1.5.0-beta03` are released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..d84c0393bf1b89f62643ffc60b5e2318ec30298e/core)

**API Changes**

- Added ExecutorCompat, which creates an Executor from a Handler. ([Ib4ca3](https://android-review.googlesource.com/#/q/Ib4ca32d49f1324c54226ad38988dc21c77a73272), [b/181237835](https://issuetracker.google.com/issues/181237835))

### Version 1.5.0-beta02

February 24, 2021

`androidx.core:core:1.5.0-beta02` and `androidx.core:core-ktx:1.5.0-beta02` are released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..5c90131a69042a6a3e13952e1da9e7ffc571c31d/core)

**Bug Fixes**

- Deprecated `ModeCompat.isNative` which is replaced by `DisplayCompat.getMode`. ([Iefa71](https://android-review.googlesource.com/#/q/Iefa7170574f98c26114b143e7c01e25bda3880e8))
- `NotificationCompat.MessagingStyle.getText()` was incorrectly marked as `@NonNull`; it is now `@Nullable` ([I05cb7](https://android-review.googlesource.com/#/q/I05cb74c5dbf27ef7dc5133d0642fe2d99ffeb068))

### Version 1.5.0-beta01

January 13, 2021

`androidx.core:core:1.5.0-beta01` and `androidx.core:core-ktx:1.5.0-beta01` are released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..6207afb1646d302c5d29c2c67d332b48db87fb27/core)

**API Changes**

- Follow API guidelines for Bounds Compat/Platform interoperability ([I7da35](https://android-review.googlesource.com/#/q/I7da358c617b6de36b2fef7dfc1a7bee2a408ccaf))
- Integrated drag-and-drop (drop events) in AppCompatEditText with OnReceiveContentListener. ([Ib26c9](https://android-review.googlesource.com/#/q/Ib26c90d51e2087e7c134dfc9331371745bfaf3ab), [b/175343405](https://issuetracker.google.com/issues/175343405))
- Connection of the new Insets Animation API with the Platform implementation ([I078da](https://android-review.googlesource.com/#/q/I078da1189041c3f5e53c18dae36f339244f31987))
- Added the new Insets Animation APIs ([I8aebd](https://android-review.googlesource.com/#/q/I8aebd12dfbadd9af03411a475710f8ae83d6cf40))
- Updated OnReceiveContentListener and related APIs:
  - Updated OnReceiveContentListener so it can be set on any type of view via ViewCompat.
  - Removed `getSupportedMimeTypes()` from `OnReceiveContentListener`; now MIME types are passed as an additional arg on the `ViewCompat` method that sets the listener.
  - Wrapped arguments to `OnReceiveContentListener.onReceiveContent()` in an object.
  - Added linkUri as a param to `onReceiveContent()` to ensure backwards compatibility with the keyboard image API.
  - Added a Bundle param to `onReceiveContent()` to ensure backwards compatibility with the keyboard image API and to facilitate evolution of the API in the future.
  - Updated `onReceiveContent()` to return any content that was not consumed, as a means to delegate to the default handling.
  - Removed `TextViewOnReceiveContentListener` from the public API since the default behavior can now be triggered by returning any unconsumed content from the listener.
  - ([Ib4616](https://android-review.googlesource.com/#/q/Ib4616cb0d0cd9f8537b64de6fcc19b80442dc3fb), [b/173814913](https://issuetracker.google.com/issues/173814913))
- Deprecated `BuildCompat.isAtLeastR` ([Idb37e](https://android-review.googlesource.com/#/q/Idb37ed0673c5a8812b60d70de5636bfc3e191d85))
- Moved `widget.RichContentReceiverCompat` to `view.OnReceiveContentListener`. ([Ifdab7](https://android-review.googlesource.com/#/q/Ifdab76f135e840a15430634a22e720947be4eecd), [b/173814913](https://issuetracker.google.com/issues/173814913))
- Added `Preconditions.checkFlagsArgument`. ([I43952](https://android-review.googlesource.com/#/q/I4395206cabeae21a1ce031607f40b801aaebc270), [b/174181100](https://issuetracker.google.com/issues/174181100))
- Deprecate custom menu for outbound sharing. ([I7cd92](https://android-review.googlesource.com/#/q/I7cd927f45e509bf7fcf32ec85a93fdb03b3ea74f))
- Notifications can now be tagged as missed calls. ([I14d90](https://android-review.googlesource.com/#/q/I14d907fc34999af5623260e09dd29dcbdde64c8e))
- Added `PackageInfoCompat#getSignatures` for retrieving the certificate array for a package ([I8e9a3](https://android-review.googlesource.com/#/q/I8e9a3ece2d45416abbcbaaa0cf2a0485180997d3), [b/159831205](https://issuetracker.google.com/issues/159831205))

**Bug Fixes**

- Fix a bug where setting `BigPictureStyle.bigLargeIcon` would break the `BigPictureStyle` for that notification on newer OS versions. ([Ic623d](https://android-review.googlesource.com/#/q/Ic623db52b536e3ad6839be5073431e1afc1f7fd4))

**External Contribution**

- ShareCompat now uses constructors for creation and the old factory methods have been deprecated. You can now create both builders and readers from a Context and an Activity is no longer required. ([I315b6](https://android-review.googlesource.com/#/q/I315b68aff01ca931d38b934786e6d9b2174f720b), [b/173043501](https://issuetracker.google.com/issues/173043501))
- Set clip data and grant uri read permission when sharing streams using ShareCompat ([I4aa31](https://android-review.googlesource.com/#/q/I4aa318b146206e4e5cd028b7e3798c9d895d8324), [b/173137936](https://issuetracker.google.com/issues/173137936))

### Version 1.5.0-alpha05

November 11, 2020

`androidx.core:core:1.5.0-alpha05` and `androidx.core:core-ktx:1.5.0-alpha05` are released. [Version 1.5.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/core)

**API Changes**

- Added support for new GnssStatus APIs ([Id8e22](https://android-review.googlesource.com/#/q/Id8e2215e55409b7212111dc84e1c87401ddb9d33))
- Added overloads of `FileProvider#getUriForFile` to support custom filenames ([Ie870b](https://android-review.googlesource.com/#/q/Ie870bbb7781edfc4c841bcaeefd55b5e632b3eeb))
- Backported the `WindowInsetsController` APIs to control the system bar appearance. ([Ieb4ee](https://android-review.googlesource.com/#/q/Ieb4eeea90a2a1db22f005b819c4307f293aa50ca))
- Renamed `getFont` with boolean to `getCachedFont` ([Iea520](https://android-review.googlesource.com/#/q/Iea5200980f74d06c3c174fcba25e319a2c9daa0f))
- Backported the `#hide()` and `#show()` methods from WindowInsetsController APIs, added in API 30 ([I21573](https://android-review.googlesource.com/#/q/I21573b5671d7681ce77e04f2401a4e0b06184864))
- Added new API `ResourcesCompat#getFont` with cacheOnly option ([Ic38cf](https://android-review.googlesource.com/#/q/Ic38cf93a5c3155eb2bacfbbc093365c31720481a))
- Updated androidx notification bubbles APIs for Android 11 ([Ib9c70](https://android-review.googlesource.com/#/q/Ib9c70f8ace7965e9cf6c2d9ec170dea5c29a7b67))

### Version 1.5.0-alpha04

October 1, 2020

`androidx.core:core:1.5.0-alpha04` and `androidx.core:core-ktx:1.5.0-alpha04` are released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/core)

**API Changes**

- Fix incomplete Style recovery when using `NotificationCompat.Builder.<init>(Context,Notification)` ([Ib297a](https://android-review.googlesource.com/#/q/Ib297ade8f6bc75f7bc897137145f813c782f37bd))
- New notification categories types are now available ([I9521a](https://android-review.googlesource.com/#/q/I9521a5794b4cf6da3ab5d1eb474f40fca783ffa9))

**Bug Fixes**

- Allow `ActivityCompat.recreate()` to be safely called from any lifecycle state on any API level. ([I62dde](https://android-review.googlesource.com/#/q/I62dde2d9041eb5b7ba2344380841aa03848d42e0), [b/160122826](https://issuetracker.google.com/issues/160122826))

### Version 1.5.0-alpha03

September 16, 2020

`androidx.core:core:1.5.0-alpha03` and `androidx.core:core-ktx:1.5.0-alpha03` are released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..18a5639262f8504db530176550e338a5d0e2e044/core)

**API Changes**

- `ViewCompat` is a utility class and shouldn't be instantiated. ([If20fa](https://android-review.googlesource.com/#/q/If20fa9fb482b80d1afb181ee4afda9f3cd31948b))
- APIs to supply and retrieve initial surrounding text were backported to `EditorInfoCompat`. They allow IME apps to avoid additional IPC latency. ([Ie3809](https://android-review.googlesource.com/#/q/Ie380919ac99373ec59f2b7162a13ab0a48e9b6bc))
- Query notification channels and groups with compat objects. ([I11d18](https://android-review.googlesource.com/#/q/I11d18088f58d3a2b10e014bd96af6d6c4914ffd0))

**Bug Fixes**

- For pre-P, ensure panes are marked as important for accessibility and support `CONTENT_CHANGE_TYPE_PANE_DISAPPEARED` events. ([Iaeffc](https://android-review.googlesource.com/#/q/Iaeffc6991881face6569627c662fe77bfbf289eb))

**External Contribution**

- API lint check for the StaticFinalBuilder is enabled for androidx ([I2b11b](https://android-review.googlesource.com/#/q/I2b11be1bb370e178e3e0d1d1083d43af38eece23), [b/138602561](https://issuetracker.google.com/issues/138602561))

### Version 1.5.0-alpha02

August 19, 2020

`androidx.core:core:1.5.0-alpha02` and `androidx.core:core-ktx:1.5.0-alpha02` are released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c15c60181fb736eac5d7fe37b547e04764eace6..96eb302ee1740ba656c90c9fb27df3723a1a89c1/core)

**New Features**

- The [`WindowInsetsCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat) APIs have been updated to those in the platform in Android 11. This includes the new `ime()` inset type, which allows checking the visibility and size of the on-screen keyboard.

  - Some caveats about the `ime()`type, it works very reliably on API 23+ when your Activity is using the `adjustResize` [window soft input mode](https://developer.android.com/training/keyboard-input/visibility#Respond). If you're instead using the `adjustPan` mode, it should work reliably back to API 14.

**API Changes**

- Added `ObjectsCompat#toString(Object, String)`. This offers the behavior of `Objects#toString(Object, String)` but can be used pre-API 19. ([I26cdc](https://android-review.googlesource.com/#/q/I26cdca93fcc21d7172908691e013afc19f23e9de))
- Added `NotificationCompat.Builder.recoverBuilder(Notification)` ([I6f100](https://android-review.googlesource.com/#/q/I6f10001da2930b84eecaff7fa9cec7f25d8b02fe))
- Add `NotificationCompat.Builder.createContentView()` and peers ([I6fe13](https://android-review.googlesource.com/#/q/I6fe13b85c1cbda4b54cff34fcfd5ae4e28c7f046))
- Add extra data related APIs in AccessibilityNodeInfoCompat ([I19567](https://android-review.googlesource.com/#/q/I19567b78f3dd007eb30404b8cfdf2d9ccb44b3b3))
- Add `NotificationCompat.Builder.setSettingsText` and `NotificationCompat.MessagingStyle.addHistoricMessage` ([I62bb6](https://android-review.googlesource.com/#/q/I62bb68df92c93375364b0753506ecbe91824210a))
- Update Notification documentation ([I1293f](https://android-review.googlesource.com/#/q/I1293ff2c58fcaf841fc9e99a2bcbbac33b91987f))
- Fix nullability of NotificationCompat.Builder ([I932e3](https://android-review.googlesource.com/#/q/I932e3b5db964d6154f1426341f138651f895f275))
- Added `NotificationChannelCompat` and `NotificationChannelGroupCompat` ([Icc3b6](https://android-review.googlesource.com/#/q/Icc3b6aea1216a7ee2c64f5ea6922988a31970e63))
- Add `addExtraDataToAccessibilityNodeInfo` to `AccessibilityNodeProviderCompat` ([I26575](https://android-review.googlesource.com/#/q/I2657562adcf20b6b7379b5fc4f956d76f2d5d80c))
- Update WindowInsetsCompat to Android 11 APIs ([I3df9e](https://android-review.googlesource.com/#/q/I3df9e889650db916c48d5567a9bcf9c7a7b9aa85))

**External Contribution**

- Add `Uri` overloads for `MailTo` methods ([I6fa6b](https://android-review.googlesource.com/#/q/I6fa6bac337338753677130985112642e0967aa1f))
- Added `MailTo` API which provides consistent behavior and bug fixes for all API levels ([Ie9395](https://android-review.googlesource.com/#/q/Ie93956270775e1214d778a890711105dd4b1db19), [b/159827506](https://issuetracker.google.com/issues/159827506))

### Version 1.5.0-alpha01

June 10, 2020

`androidx.core:core:1.5.0-alpha01` and `androidx.core:core-ktx:1.5.0-alpha01` are released.

**New Features**

- Provides parity with Android R platform SDK APIs for `ShortcutManager`, `ShortcutInfo`, `AccessibilityNodeInfo`, `DisplayCutout`, `GnssStatus`, and `Notification` classes

**Bug Fixes**

- Make it clear that checking shouldShowPermissionRationale is recommended.
- Change AtomicFile to use rename-into-place.
- Adjust the Typeface display style with the style of given font. ([b/156853883](https://issuetracker.google.com/issues/156853883))
- Fix failing Notification Builder Tests
- Fix register/unregister bug `LocationManagerCompat`.

## Core and Core-ktx Version 1.4.0

### Version 1.4.0-alpha01

May 20, 2020

`androidx.core:core:1.4.0-alpha01` and `androidx.core:core-ktx:1.4.0-alpha01` are released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c19e5fbcdbbc72e70d2f52971009cc17be53abe..cea47c265abad60d93f1ca6605fe0fd21ba970c5/core)

**API Changes**

- Add common API for inserting rich content (e.g. pasting an image). The new callback provides a single API that apps can implement to support the different ways in which rich content may be inserted. For now the API is only added to `AppCompatEditText` and will be invoked for the following code paths:
  - paste from the clipboard
  - content insertion from the IME (`InputConnection.commitContent`) ([I22bf7](https://android-review.googlesource.com/#/q/I22bf76a22b795cb47c7ab12e4f5b529fff8fe5d7))
- Backported `android.os.Process.isApplicationUid(int)` to help apps determine whether code is executing in a isolated process ([I4c83a](https://android-review.googlesource.com/#/q/I4c83a3aad2bb791f066a85f9051134510aa4f159), [b/153014822](https://issuetracker.google.com/issues/153014822))
- Backported `LocusId` to help apps correlate state between different subsystems such as content capture, shortcuts, and notifications. ([Ia3129](https://android-review.googlesource.com/#/q/Ia3129ef8ee75b287c29a78c085cdfdca200875a6))
- Added ancestry sequences to ViewGroup ([I5f75c](https://android-review.googlesource.com/#/q/I5f75cd25b3c46c99b21634d1f136788bd71ad890), [b/117976097](https://issuetracker.google.com/issues/117976097))

**Bug Fixes**

- Added permissions validation for `ActivityCompat.requestPermissions()` ([I372cc](https://android-review.googlesource.com/#/q/I372cca80d7c0394f4478847ae122acbc29bbb697), [b/122163323](https://issuetracker.google.com/issues/122163323))
- Extracted v28+ calls into a separate static class, which fixes a `NoClassDefFoundError` error for `View#OnUnhandledKeyEventListener` when building an app bundle ([Id3419](https://android-review.googlesource.com/#/q/Id34194f77b9c7a2f0864e38d17ef6039733dee95), [b/153695093](https://issuetracker.google.com/issues/153695093))
- Fixed a `setChronometerCountDown` crash bug ([I47282](https://android-review.googlesource.com/#/q/I472824f0835988a38186318f2b3b49a00542da89), [b/145770610](https://issuetracker.google.com/issues/145770610))

## Core and Core-ktx Version 1.3.2

### Version 1.3.2

October 1, 2020

`androidx.core:core:1.3.2` and `androidx.core:core-ktx:1.3.2` are released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86d9b726630d0b200964ff4bad3cd03e8adc9975..c148aca8257ba074d445bd3edfa50a890aecfe75/core)

**Bug Fixes**

- Allow `ActivityCompat.recreate()` to be safely called from any lifecycle state on any API level. ([I62dde](https://android-review.googlesource.com/#/q/I62dde2d9041eb5b7ba2344380841aa03848d42e0), [b/160122826](https://issuetracker.google.com/issues/160122826))

## Core and Core-ktx Version 1.3.1

### Version 1.3.1

July 22, 2020

`androidx.core:core:1.3.1` and `androidx.core:core-ktx:1.3.1` are released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/861913d9574541c4e906435a5f5e3ba4711bfc3d..86d9b726630d0b200964ff4bad3cd03e8adc9975/core)

**Bug Fixes**

- Fixed an issue where the resolved font resource `Typeface` weight and style had the wrong values on API Level 29 ([b/156853883](https://issuetracker.google.com/156853883))

## Core and Core-ktx Version 1.3.0

### Version 1.3.0

May 27, 2020

`androidx.core:core:1.3.0` and `androidx.core:core-ktx:1.3.0` are released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c19e5fbcdbbc72e70d2f52971009cc17be53abe..861913d9574541c4e906435a5f5e3ba4711bfc3d/core)

**Major changes since 1.2.0**

- New APIs on `NestedScrollView` to run smooth scrolls with specified duration
- New APIs on `ViewCompat` to retrieve the original window insets that were dispatched to the view hierarchy

### Version 1.3.0-rc01

April 15, 2020

`androidx.core:core:1.3.0-rc01` and `androidx.core:core-ktx:1.3.0-rc01` are released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..9c19e5fbcdbbc72e70d2f52971009cc17be53abe/core)

**Bug Fixes**

- `WindowInsetsCompat` now properly implements `hashCode()` and `equals()` on all supported API levels.

### Version 1.3.0-beta01

April 1, 2020

`androidx.core:core:1.3.0-beta01` and `androidx.core:core-ktx:1.3.0-beta01` are released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/core/core)

### Version 1.3.0-alpha02

March 4, 2020

`androidx.core:core:1.3.0-alpha02` and `androidx.core:core-ktx:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/741f4aed00efbd392b4c48a59b4cb06a599e6366..666ae665acfcfa2a20eccc18e4494808169742f4/core)

**API Changes**

- New APIs on `NestedScrollView` to run smooth scrolls with specified duration
- A new `ViewCompat` API to retrieve the original window insets that were dispatched to the view hierarchy

### Version 1.3.0-alpha01

January 29, 2020

`androidx.core:core:1.3.0-alpha01` and `androidx.core:core-ktx:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2eeb7cf736688188564be5ff2be9cc7a4f3bb3e0..741f4aed00efbd392b4c48a59b4cb06a599e6366/core).

**New features**

- Added `ContentProviderCompat`
- Added `WindowInsetsCompat.Builder`

**API changes**

- Added a `NotificationCompat` API to silence a notification instance
- Added `ResourcesCompat.NULL_ID`
- Deprecated `CarExtender.UnreadConversation` in `NotificationCompat`
- Added a `DisplayCompat` API to get the physical size of the device

**Bug fixes**

- Improved the handling actions with no icons in `NotificationCompat`
- Fixed drawable tinting on TextView relative to compound drawables on API Level 23 ([aosp/1172194](https://android-review.googlesource.com/c/platform/frameworks/support/+/1172194))
- Ensured the base context is always a wrapper
- Fixed an issue where RecyclerView should not populate Collection\[Item\]Info by default

## Version 1.2.0

| **Note:** newer versions androidx libraries now correctly reflect `implementation` dependencies versus `api` dependencies. If your project relies on an implicit dependency exposed through an `implementation` dependency in version `1.2.0`, it will be necessary to explicitly depend on that dependency in your `build.gradle`.

### Version 1.2.0

February 5, 2020

`androidx.core:core:1.2.0` and `androidx.core:core-ktx:1.2.0` are released. [Version 1.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2eeb7cf736688188564be5ff2be9cc7a4f3bb3e0..42402e71d1e88fe3d2cec757175074fdf50b4c2b/core).

**Major changes since 1.1.0**

- Added new APIs and bug fixes in `NotificationCompat`
- Added new APIs to work with `BlendMode` introduced in AndroidQ in backwards-compatible way
- Added new APIs and bug fixes in accessibility compat
- Added new APIs to work with `ShortcutInfo`
- Added new APIs to work with `WindowInsets`
- Fixed backwards compatibility for bundle key strings between 28.0 (support library) and 1.1 (AndroidX) in `EditorInfoCompat`, `ShareCompat`, `WakefulBroadcastReceiver` and `InputConnectionCompat`

### Version 1.2.0-rc01

November 20, 2019

`androidx.core:core:1.2.0-rc01` and `androidx.core:core-ktx:1.2.0-rc01` are released with no changes since `1.2.0-beta02`. [Version 1.2.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0bf4cab5211a3f32314c415816c1fe93e53e52ea..2eeb7cf736688188564be5ff2be9cc7a4f3bb3e0/core).

### Version 1.2.0-beta02

November 7, 2019

`androidx.core:core:1.2.0-beta02` and `androidx.core:core:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/f14ad350142290622d1645e1d0e280cbe8ca4c2f..0bf4cab5211a3f32314c415816c1fe93e53e52ea/core).

**Bug fixes**

- Updated translations for en-rCA and en-rXC locales.

### Version 1.2.0-beta01

October 9, 2019

`androidx.core:core:1.2.0-beta01` and `androidx.core:core-ktx:1.2.0-beta01` released. [Version 1.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/fe2f150d9da36e98fc351f413bf670468b5ace60..f14ad350142290622d1645e1d0e280cbe8ca4c2f/core).

**API Changes**

- Added support for creating NotificationCompat Actions using IconCompat and deprecated a public field (and its getter) using resource IDs to represent icons for Actions. ([aosp/1119192](https://android-review.googlesource.com/c/1119192))
- Add `MathUtils.clamp` for longs ([aosp/1117300](https://android-review.googlesource.com/c/platform/frameworks/support/+/1117300))
- Added `setChronometerCountDown` to `NotificationCompat` ([b/138601213](https://issuetracker.google.com/issues/138601213))

**Bug Fixes**

- Fixed an issue with the handling of unicode digits in address detection. ([aosp/1129852](https://android-review.googlesource.com/c/platform/frameworks/support/+/1129852))

**External Contribution**

- Thank you Sergey Zakharov for enabling the API lint check for MissingBuild and ListenerLast in AndroidX! ([aosp/1119191](https://android-review.googlesource.com/c/1119191), [aosp/1126768](https://android-review.googlesource.com/c/1126768))

### Version 1.2.0-alpha04

September 5, 2019

`androidx.core:core:1.2.0-alpha04` and `androidx.core:core-ktx:1.2.0-alpha04` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/f398f692520b94aa05a12ac91884012cb19902fc..fe2f150d9da36e98fc351f413bf670468b5ace60/core).

**API changes**

- Deprecated `ShortcutInfoCompat.Builder#setLongLived()` and replaced it with a new API with the same name that accepts a boolean as a parameter, to match the similar API in `ShortcutInfo.Builder` in Android framework.
- Added `ShortcutInfoCompat.Builder#setRank()` and `ShortcutInfoCompat#getRank()` to match the `ShortcutInfo` in Android framework.

**Bug fixes**

- Nested pre scrolling is no longer performed before the gesture exceeds touch slop ([b/139530818](https://issuetracker.google.com/issues/139530818), [aosp/1105373](https://android-review.googlesource.com/1105373)). This benefits [ViewPager2](https://developer.android.com/jetpack/androidx/releases/viewpager2) and other libraries.

### Version 1.2.0-alpha03

August 7, 2019

`androidx.core:core:1.2.0-alpha03` and `androidx.core:core-ktx:1.2.0-alpha03` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/cd16b09b10c939184a8a47a3f85b758f16c08e85..ece690f1fdb4481b47c5128fd21d88da7d6850a6/core).
| **Note:** The Kotlin dependant libraries of this version (`core-ktx`) target Java 8 bytecode. Please see our [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) page on using Java 8 in your project.

**New features**

- Added `UriCompat.toSafeString(Uri)` to provide URI escaping that is updatable separately from the platform. ([b/130878326](https://issuetracker.google.com/issues/130878326))
- Added `Predicate<T>` interface to provide Java 8-style predicates without requiring Java 8 language features.

**API changes**

- Made `removeDynamicShortuct()` static ([b/134993204](https://issuetracker.google.com/issues/134993204))
- Created factory method for BlendMode Color Filter ([b/135943149](https://issuetracker.google.com/issues/135943149))
- Added `async`, `counter`, and `isEnabled` to `TraceCompat` ([aosp/987332](https://android-review.googlesource.com/987332))
- Unhid APIs in `WindowInsetsCompat` and `ViewDragHelper` ([aosp/979408](https://android-review.googlesource.com/979408))

**Bug fixes**

- Fixed bug with `NestedScrollView` scrolling in response to a11y scroll calls. ([aosp/971000](https://android-review.googlesource.com/971000))
- Switched to using `SimpleArrayMap` in `ViewCompat` implementation ([aosp/1012534](https://android-review.googlesource.com/1012534))
- Fixed bug where FingerprintManager incorrectly checked PackageManager on API Level 23 ([b/124066957](https://issuetracker.google.com/issues/124066957))

### Version 1.2.0-alpha02

June 13, 2019

`androidx.core:core:1.2.0-alpha02` and `androidx.core:core-ktx:1.2.0-alpha02` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/f6d94c8b8adaf0edaff495c1e88e8ddc96060317..cd16b09b10c939184a8a47a3f85b758f16c08e85/core).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**API changes**

- Added WindowInsetsCompat.wrap() and unwrap(), to be able to wrap and unwrap WindowInsets instances

### Version 1.2.0-alpha01

May 7, 2019
`androidx.core:core:1.2.0-alpha01` are `androidx.core:core-ktx:1.2.0-alpha01` are released.
| **Note:** This version will only compile against the Q Beta 3 SDK.

**New features**

- Add `ACTION_PAGE_UP/DOWN/NEXT/PREVIOUS` accessibility actions
- Add `CATEGORY_NOTIFICATION` to NotificationCompat
- Add support for contextual Notification Actions
- Add support for bubbles in NotificationCompat
- Added BlendModeCompat APIs to leverage the BlendMode APIs on Android 10 and falling back to `PorterDuff.Mode` equivalents wherever possible
- Add new getters to WindowInsetsCompat and ViewCompat
- Add support for tap-to-edit in notifications
- DrawerLayout system gesture exclusion rects
- Add NotificationCompat API for whether to allow system generated contextual actions
- Handle disabled `<activity-alias>` components in NavUtils
- Add `AccessibilityNodeInfoCompat.setEntryKey`

**Bug fixes**

- Fix exception when loading fonts in TypefaceCompat
- Various DayNight fixes
- Fix backwards compatibility for bundle key strings between 28.0 (support library) and 1.1 (AndroidX) in EditorInfoCompat, ShareCompat, `WakefulBroadcastReceiver` and `InputConnectionCompat`

## Version 1.1.0

### Version 1.1.0

September 5, 2019

`androidx.core:core:1.1.0` and `androidx.core:core-ktx:1.1.0` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/bedbf8f35b386aceeb6ab1aa6105597b4a25855b..8139a2b2a6e73b094652ce1ad9865cdb60df2843/core).

**Important Changes since 1.0.0**

- Updated accessibility APIs to match the Android 10 platform accessibility APIs
- Added improvements to Nested Scrolling; see [`NestedScrollingChild3`](https://developer.android.com/reference/androidx/core/view/NestedScrollingChild3) and [`NestedScrollingParent3`](https://developer.android.com/reference/androidx/core/view/NestedScrollingParent3).
- This library no longer exposes the `androidx.collection` dependency as part of its API. If you were depending on the `androidx.collection` types implicitly through a dependency on Core, you will need to add an explicit `androidx.collection` dependency to your library or app. This change is source-incompatible but retains binary compatibility. The Collection dependency is still a transitive dependency of Core but as an implementation detail instead of part of its API.
- Worked around an IPC compatibility issue caused by refactor to androidx ([aosp/948725](https://android-review.googlesource.com/948725), [aosp/938269](https://android-review.googlesource.com/938269))
- Added a variety of fixes for AppCompat DayNight ([aosp/942956](https://android-review.googlesource.com/942956))

### Version 1.1.0-rc03

August 7, 2019

`androidx.core:core:1.1.0-rc03` and `androidx.core:core-ktx:1.1.0-rc03` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/236c058a2ec13f5c20c151f37bad489910caa27f..bedbf8f35b386aceeb6ab1aa6105597b4a25855b/core).

**Bug fixes**

- Make the hidden `androidx.core.app.ComponentActivity` implement `LifecycleOwner` to maintain binary compatibility with `androidx.fragment:fragment:1.0.0` ([aosp/1094409](https://android-review.googlesource.com/1094409))

### Version 1.1.0-rc02

July 2, 2019

`androidx.core:core:1.1.0-rc02` and `androidx.core:core-ktx:1.1.0-rc02` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/f0674eb1d73638c1220aca545ca46fab14d8f764..236c058a2ec13f5c20c151f37bad489910caa27f/core).

**Bug fixes**

- `FingerprintManagerCompat#getFingerprintManagerOrNull` on API level 23 should not check `PackageManager` ([b/124066957](https://developer.android.com/jetpack/androidx/releases/124066957)) ([aosp/987433](https://android-review.googlesource.com/c/987433))
- Fix equality comparison in AccessibilityNodeInfoCompat ([aosp/985736](https://android-review.googlesource.com/c/985736))

### Version 1.1.0-rc01

June 5, 2019

`androidx.core:core:1.1.0-rc01` and `androidx.core:core-ktx:1.1.0-rc01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/2c7181c30858d401daba909d0a9400d5fc8d16d9..f0674eb1d73638c1220aca545ca46fab14d8f764/core).

**Bug fixes**

- Make image keyboard API backport compatible to all previous impls ([aosp/968220](https://android-review.googlesource.com/c/platform/frameworks/support/+/968220))
- Remove Guava ListenableFuture from androidx.core:core library dependencies ([b/133171974](https://issuetracker.google.com/issues/133171974), [aosp/965393](https://android-review.googlesource.com/c/platform/frameworks/support/+/965393))
- Fix incorrect velocity while flinging with nested scrolling. ([aosp/961642](https://android-review.googlesource.com/c/platform/frameworks/support/+/961642))
- Add test for mutating `TransitionDrawable` ([b/37033322](https://issuetracker.google.com/issues/37033322))

### Version 1.1.0-beta01

May 7, 2019

`androidx.core:core:1.1.0-beta01` and `androidx.core:core-ktx:1.1.0-beta01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/f6d94c8b8adaf0edaff495c1e88e8ddc96060317..2c7181c30858d401daba909d0a9400d5fc8d16d9/core).

The initial release of AndroidX broke backwards compatibility for Support Library
`compat` APIs that are used for inter-process communication, sending keyed data
in bundles. This release fixes this compatibility, restoring communication
between code built with Support Library 28.0 (or earlier) and AndroidX 1.1
(or later).

**API changes**

- Undeprecated capability setters ([aosp/937281](https://android-review.googlesource.com/c/937281/))
- `RemoteActionCompat` is now a 1VersionedParcelable\` ([aosp/928534](https://android-review.googlesource.com/c/928534/))

**Bug fixes**

- AppCompatTextView in core tests should be created with an appcompat theme ([aosp/951636](https://android-review.googlesource.com/c/951636/))
- Use pre-1.0 string values for InputConnectionCompat ([aosp/948725](https://android-review.googlesource.com/c/948725/))
- Use pre-AndroidX strings as fallback interop for bundle keys ([aosp/938269](https://android-review.googlesource.com/c/938269/))
- Fixed bug in DayNight updates when in background ([aosp/942956](https://android-review.googlesource.com/c/942956/))
- Implemented text entry key API for accessibility services in AOSP Keyboard ([aosp/943897](https://android-review.googlesource.com/c/943897/))
- Fixed exception when loading font on devices running API Level 20 and lower
- Handle disabled `<activity-alias>` components in NavUtils ([aosp/940788](https://android-review.googlesource.com/c/940788/))

### Version 1.1.0-alpha05

March 13, 2019

`androidx.core:core:1.1.0-alpha05` and `androidx.core:core-ktx:1.1.0-alpha05`
are released. The full list of commits included in this version can be found
[here](https://android.googlesource.com/platform/frameworks/support/+log/3d680f800229fd452fd94b27f377053964ab4ca3..f6d94c8b8adaf0edaff495c1e88e8ddc96060317/core).

**New features**

- New `ActivityCompat.recreate()` API for working around pre-28 platform bugs ([aosp/898940](https://android-review.googlesource.com/898940))
- New `LocationManagerCompat` class ([aosp/894736](https://android-review.googlesource.com/894736))

**API changes**

- This library no longer exposes the 'collection' dependency as part of its API. If you were depending on the 'collection' types implicitly through a dependency on 'core', you will need to add an explicit 'collection' dependency to your library or app. This change is source-incompatible but retains binary compatibility. The 'collection' dependency is still a transitive dependency of 'core' but as an implementation detail instead of part of its API.

**Bug fixes**

- Fixed bug with default tint mode for `ImageView` on devices running API level 21

### Version 1.1.0-alpha04

January 30, 2019

`androidx.core:core 1.1.0-alpha04` and `androidx.core:core-ktx 1.1.0-alpha04` are released.

**API changes**

- Change value of `EXTRA_SHORTCUT_ID` to be consistent with the platform ([aosp/877712](https://android-review.googlesource.com/877712/))
- Add `CATEGORY_NOTIFICATION` to `NotificationCompat` ([aosp/861067](https://android-review.googlesource.com/861067/))

**Bug fixes**

- Fix for fontFamily not working on devices running API level 24 and lower ([aosp/807054](https://android-review.googlesource.com/807054/))
- Fixed bug where replacing accessibility actions, and adding accessibility actions, didn't remove old accessibility actions ([aosp/848314](https://android-review.googlesource.com/848314/))

### Version 1.1.0-alpha03

December 17, 2018

`androidx.core 1.1.0-alpha03` and `androidx.core-ktx 1.1.0-alpha03` are released with the following changes. `androidx.core-ktx 1.1.0-alpha02` is released to provide a ktx match for `androidx.core 1.1.0-alpha02`.

**New features**

- Added Notification channels methods to `NotificationManagerCompat` so developers can use only `NotificationManagerCompat` when working with notifications. Special thanks to Zdeněk Kořán for this new feature!

**API changes**

- Added new APIs to `ShortcutManagerCompat` to publish and update dynamic shortcuts.

### Version 1.1.0-alpha01

November 5, 2018

`androidx.core 1.1.0-alpha01` is released with the following API changes and
bug fixes.

**New features and API changes**

- NestedScrollingChild3 and NestedScrollingParent3 add the 'consumed' parameter to the overloaded dispatchNestedScroll and \* onNestedScroll methods so that the view that drives nested scrolling can be better informed about how much scroll distance was \* consumed by parents in each nested scroll pass.
- NestedScrollView now implements NestedScrollingChild3 and NestedScrollingParent3, and therefore, the NestedScrollingChild2 and \* NestedScrollingParent2 implementations of dispatchNestedScroll and onNestedScroll are not guaranteed to be called. Developers \* counting on either being called should also override the new nested scrolling 3 version of dispatchNestedScroll and onNestedScroll.
- ShortcutInfoCompat has the following new fields: Persons, categories and isLongLived. Done to advertise it can accept various types \* of content.
- Renamed SupportActivity to ComponentActivity. See androidx.activity for more info.
- Added getMainExecutor() method, which returns an Executor link that will run enqueued tasks on the main thread associated with that \* context.
- Added compatibility implementation of Resources.getFloat.
- Added Results Source to compat RemoteInput. This allows apps to distinguish direct and smart replies for logging purposes.
- Added Kotlin extension functions for TextView TextWatcher actions.
- Deprecated AccessibilityNodeInfo capability and flag setters; use actions instead.
- Added AccessibilityPane to ViewCompat.
- Exposed ClickableSpans on pre-O devices through the addition of AccessibilityClickableSpanCompat.
- Deprecated `AccessibilityNodeInfoCompat.setFocusable()`, `setClickable()`, `setLongClickable()`, `setScrollable()`, and `setContextClickable()`. Added `AccessibilityAction`s instead.
- Added `ViewCompat.setAccessibilityPaneTitle()`, `getAccessibilityPaneTitle()`, `setScreenReaderFocusable()`, `isScreenReaderFocusable()`, `setAccessibilityHeading()`, and `isAccessibilityHeading()`, to backport this `View` accessibility functionality through API 19.
- Added `ViewCompat.enableAccessibleClickableSpanSupport()` to allow developers to make non-URL `ClickableSpan`s accessible back through API 19.

**Bug fixes**

- Fixed bug that caused `ResourcesCompat.getFont()` crash when the network fails, when using downloadable fonts.
- Fixed Null Pointer Exception in TypefaceCompatApi21 that occurred when `ContentResolver` returned null.
- Fixed type error in Array Utils where it expected ColorStateList but got raw colors.

## Core-Animation and Core-Animation-Testing 1.0.0

### Version 1.0.0

May 1, 2024

`androidx.core:core-animation:1.0.0` and `androidx.core:core-animation-testing:1.0.0` are released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8cdeb1f6b44f8f5687d5fee6bbda4e43aaa1a593..8210d3ea51cfef5d8d53bb9af34fa543338dc2ee/core).

**Major features of 1.0.0**

`androidx.core:core-animation` is a backport of the Animator API including all the features added to the platform since API Level 14. Some of the notable features are:

- `ValueAnimator#pause`, `ValueAnimator#resume` (API Level 19)
- `ObjectAnimator.ofMultiInt`, `ObjectAnimator.ofMultiFloat` (API Level 21)
- `ValueAnimator#setCurrentFraction` (API Level 22)
- `AnimatorSet#setCurrentPlayTime` (API Level 26)
- `androidx.core:core-animation-testing` allows developers to test animators in a deterministic manner. See [`AnimatorTestRule`](https://developer.android.com/reference/androidx/core/animation/AnimatorTestRule) for the details.

### Version 1.0.0-rc01

July 26, 2023

`androidx.core:core-animation:1.0.0-rc01`, `androidx.core:core-animation-testing:1.0.0-rc01`, and `androidx.core:core-remoteviews:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f8115b4c10e1f8af23cdef2e7bc36dae358c9808..acde076f20ad5d7d8e2d2894b29c6c1464d0665e/core)

**New Features**

- `RemoteViews` moves moved to rc01 after stabilizing in beta.

### Version 1.0.0-beta01

April 20, 2022

`androidx.core:core-animation:1.0.0-beta01` is released with no changes since 1.0.0-alpha02. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c0a89ec374961b3015097ab307ebb8196dbe3888/core/core-animation)

### Core-Animation Core-Animation-Testing Version 1.0.0-alpha02

August 19, 2020

`androidx.core:core-animation:1.0.0-alpha02` and `androidx.core:core-animation-testing:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..96eb302ee1740ba656c90c9fb27df3723a1a89c1/core)

**Bug Fixes**

- Fix AnimatorSet with multiple Animators for a single property. ([aosp/1351310](https://android-review.googlesource.com/c/platform/frameworks/support/+/1351310))

### Core-Animation Version 1.0.0-alpha01

April 15, 2020

`androidx.core:core-animation:1.0.0-alpha01` and `androidx.core:core-animation-testing:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045/core)

**New Features**

`androidx.core:core-animation` is a backport of the Animator API including all the features added to the platform since API Level 14. Some of the notable features are:

- `ValueAnimator#pause`, `ValueAnimator#resume` (API Level 19)
- `ObjectAnimator.ofMultiInt`, `ObjectAnimator.ofMultiFloat` (API Level 21)
- `ValueAnimator#setCurrentFraction` (API Level 22)
- `AnimatorSet#setCurrentPlayTime` (API Level 26)
- `androidx.core:core-animation-testing` allows developers to test animators in a deterministic manner. See [AnimatorTestRule](https://developer.android.com/reference/androidx/core/animation/AnimatorTestRule) for the details.

## Core-Role Version 1.1.0

### Version 1.1.0

March 12, 2025

`androidx.core:core-role:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d950727ec55346f048816bcb77c6962881527405..62be11e8b31def4aa2cfd77694c26ea6f23e2019/core/core-role).

### Version 1.1.0-rc01

December 15, 2021

`androidx.core:core-role:1.1.0-rc01` is released with no changes since `1.1.0-alpha01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..d950727ec55346f048816bcb77c6962881527405/core/core-role)

### Core-Role Version 1.1.0-alpha01

April 15, 2020

`androidx.core:core-role:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b3acda6aadff279fb002c49e9d0d4bd5b21f0566..24daa503442fcd3e44ada60cf1da41df2815c045/core/core-role)

**API Changes**

- Added role name for system gallery.

## Core-Role Version 1.0.0

### Version 1.0.0

February 10, 2021

`androidx.core:core-role:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d1e4253a0dc3148439148c0c687698b243475326..40d9b4f0be5d2806f3b91a7d391c75fae55ddb03/core/core-role)

**Major features of 1.0.0**

- Added `RoleManagerCompat` containing the name and documentation for roles that might be available in the system.

### Core-Role Version 1.0.0-rc01

April 15, 2020

`androidx.core:core-role:1.0.0-rc01` is released with no changes since `1.0.0-beta01`. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b3acda6aadff279fb002c49e9d0d4bd5b21f0566..d1e4253a0dc3148439148c0c687698b243475326/core/core-role)

### Core-Role Version 1.0.0-beta01

November 20, 2019

`androidx.core:core:1.0.0-beta01` is released with no changes since `1.0.0-alpha01`. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b57674a04707e1adc076536377f967f62d2b68b..b3acda6aadff279fb002c49e9d0d4bd5b21f0566/core/core-role).

### Core-Role Version 1.0.0-alpha01

July 2, 2019

`androidx.core:core-role:1.0.0-alpha01` is released. This is the first release of `androidx.core:core-role`. The commits included in this initial version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/1b57674a04707e1adc076536377f967f62d2b68b/core/core-role).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.
| **Note:** This version will only work with the Q Beta 4 SDK.

**New features**

- Added `RoleManagerCompat` containing the name and documentation for roles that might be available in the system.

## Version 1.0.2

### Version 1.0.2

May 7, 2019

`androidx.core:core:1.0.2`, and `androidx.core:core-ktx:1.0.2` are released. This release includes 2 commits.

The initial release of AndroidX broke backwards compatibility for Support Library
`compat` APIs that are used for inter-process communication, sending keyed data
in bundles. This release fixes this compatibility, restoring communication
between code built with Support Library 28.0 (or earlier) and AndroidX 1.1
(or later).

**Bug fixes**

- Use pre-1.0 string values for InputConnectionCompat ([aosp/948725](https://android-review.googlesource.com/c/948725/))
- Use pre-AndroidX strings as fallback interop for bundle keys ([aosp/938269](https://android-review.googlesource.com/c/938269/))

## Version 1.0.1

### Version 1.0.1

November 7, 2018

Bugfix release of `core-1.0.1` and `appcompat-1.0.2`.

**Bug fixes**

- Fixed bug where `PrecomputedTextCompat` would crash when used with RTL `AppCompatTextView`. [b/113070424](https://issuetracker.google.com/113070424)

## Core-Ktx Version 1.0.1

November 5, 2018

`androidx.core-ktx 1.0.1` is released with the following bug fixes:

- Fixed bug where implementation of union and intersection were swapped.