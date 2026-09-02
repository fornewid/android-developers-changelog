---
title: https://developer.android.com/jetpack/androidx/releases/mediarouter
url: https://developer.android.com/jetpack/androidx/releases/mediarouter
source: md.txt
---

# Mediarouter

[User Guide](https://developer.android.com/guide/topics/media/mediarouter) [Code Sample](https://github.com/android/media-samples) API Reference  
[androidx.mediarouter.app](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/package-summary)  
[androidx.mediarouter.media](https://developer.android.com/reference/kotlin/androidx/mediarouter/media/package-summary)  
Enable media display and playback on remote receiver devices using a common user interface.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.8.1](https://developer.android.com/jetpack/androidx/releases/mediarouter#1.8.1) | - | - | [1.9.0-alpha01](https://developer.android.com/jetpack/androidx/releases/mediarouter#1.9.0-alpha01) |

## Declaring dependencies

To add a dependency on MediaRouter, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.mediarouter:mediarouter:1.8.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.mediarouter:mediarouter:1.8.1")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:461042+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=461042&template=1238510)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.9

### Version 1.9.0-alpha01

February 11, 2026

`androidx.mediarouter:mediarouter:1.9.0-alpha01` and `androidx.mediarouter:mediarouter-testing:1.9.0-alpha01` are released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0cab07c4babbff31087ac2ab8da21290b7923a35..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/mediarouter).

**API Changes**

- Add `MediaRouter` APIs to support device suggestions ([I34cf1](https://android-review.googlesource.com/#/q/I34cf120ff37d5772267637ff79ee5079cb50c948), [b/438200509](https://issuetracker.google.com/issues/438200509))
- Add methods for permission-based route visibility ([I8f814](https://android-review.googlesource.com/#/q/I8f8144fc4e6c1e3c942dab1040c1aab1074ce77c), [b/395174487](https://issuetracker.google.com/issues/395174487))
- Added a new constructor for `MediaRouteDiscoveryRequest` which accepts a new parameter along with the existing params to indicate whether the scanning should happen even with screen off. ([I987c8](https://android-review.googlesource.com/#/q/I987c8b11a291477924f728ae693d80b2d0538670), [b/451842800](https://issuetracker.google.com/issues/451842800))

**Bug Fixes**

- Change the default `minSdk` from API 21 to API 23. ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

**External Contribution**

- Replace most PNG assets with vector drawables.

## Version 1.8

### Version 1.8.1

July 2, 2025

`androidx.mediarouter:mediarouter:1.8.1` and `androidx.mediarouter:mediarouter-testing:1.8.1` are released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f7fb264c3718c3816f1cfd173f61c34e261aa51a..0cab07c4babbff31087ac2ab8da21290b7923a35/mediarouter).

**Bug Fixes**

- Make the selection of a selected route a no-op ([a2953f](https://android.googlesource.com/platform/frameworks/support/+/a2953fdeee205cfa6bddb34c9742941d0ac55471)).

### Version 1.8.0

June 4, 2025

`androidx.mediarouter:mediarouter:1.8.0` and `androidx.mediarouter:mediarouter-testing:1.8.0` are released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/068e09c26f719be79a26e04bcec353e197730b41..f7fb264c3718c3816f1cfd173f61c34e261aa51a/mediarouter).

**Important changes since MediaRouter 1.7.0**

- Add new API to support connecting (and disconnecting) to routes without affecting the route selection.
- Add new API that allows providers to take parameters when creating a controller.
- Add new API for listening for changes in the list of bound `MediaRouteProviderService` clients.
- New API to support stream expansion with route connection.
- Update `onRouteDisconnected` callback with both disconnected and requested routes.

### Version 1.8.0-rc01

May 20, 2025

`androidx.mediarouter:mediarouter:1.8.0-rc01` and `androidx.mediarouter:mediarouter-testing:1.8.0-rc01` are released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..068e09c26f719be79a26e04bcec353e197730b41/mediarouter).

### Version 1.8.0-beta01

May 7, 2025

`androidx.mediarouter:mediarouter:1.8.0-beta01` and `androidx.mediarouter:mediarouter-testing:1.8.0-beta01` are released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/mediarouter).

**API Changes**

- Include client package name in `RouteControllerOptions` ([Ieac03](https://android-review.googlesource.com/#/q/Ieac0331da2ff9e3d0b5681a8c23ccd8423ad627a))

**Bug Fixes**

- Fix `NullPointerException` when attempting to detach a non-existent controller from a connection ([8e61574](https://android-review.googlesource.com/c/platform/frameworks/support/+/3605991)).

### Version 1.8.0-alpha04

April 23, 2025

`androidx.mediarouter:mediarouter:1.8.0-alpha04` and `androidx.mediarouter:mediarouter-testing:1.8.0-alpha04` are released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/mediarouter).

**Bug Fixes**

- Fix `NullPointerException` that occurs as a result of returning a null route controller in specific scenarios ([Ib7efe](https://android.googlesource.com/platform/frameworks/support/+/a3adedeb3322dc362533d0aa2620cd57f7949de1)).

### Version 1.8.0-alpha03

February 12, 2025

`androidx.mediarouter:mediarouter:1.8.0-alpha03` and `androidx.mediarouter:mediarouter-testing:1.8.0-alpha03` are released. Version 1.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/mediarouter).

**API Changes**

- Remove an alpha API `GroupRouteInfo#updateRoutes`. ([Ib3d70](https://android-review.googlesource.com/#/q/Ib3d7044dcdf038a676fce030303654f6f76b8bc4))
- Update the javadoc of route selection and route connection APIs ([I85bc5](https://android-review.googlesource.com/#/q/I85bc5068b6478f0ef0be8ce24cc1fc03a470f13a))

### Version 1.8.0-alpha02

January 15, 2025

`androidx.mediarouter:mediarouter:1.8.0-alpha02` and `androidx.mediarouter:mediarouter-testing:1.8.0-alpha02` are released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/mediarouter).

**API Changes**

- New API to support stream expansion with route connection. ([I87373](https://android-review.googlesource.com/#/q/I87373d357290b535ededae9d092a30e5077193c6))
- Update `onRouteDisconnected` callback with both disconnected and requested routes. ([Iae5f3](https://android-review.googlesource.com/#/q/Iae5f363eeb9452b8dd55dd3afa06e02815dbee25))

### Version 1.8.0-alpha01

December 11, 2024

`androidx.mediarouter:mediarouter:1.8.0-alpha01` and `androidx.mediarouter:mediarouter-testing:1.8.0-alpha01` are released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/10bd7b9c1fd5169f3dfc50e744fa70aa87c65182..46295bc0b75a16f452e8e0090e8de41073d4dbb6/mediarouter).

**API Changes**

- Add new API to support connecting (and disconnecting) to routes without affecting the route selection. ([I64a8e](https://android-review.googlesource.com/#/q/I64a8e45a1b3270d4749291fb7d6d62be5b57bb85)).
- Add new API that allows providers to take parameters when creating a controller. ([I703b9](https://android-review.googlesource.com/#/q/I703b9011c8ab76fd9849362f8805340dc4cc4c11)).
- Add new API for listening for changes in the list of bound `MediaRouteProviderService` clients. ([I69996](https://android-review.googlesource.com/#/q/I6999664611a2f23401dd8237c437ecf04a7dffad))

**Bug Fixes**

- Mitigate issue causing playback to be incorrectly routed to the built-in speakers while a Bluetooth device is connected.
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Fix Output Switcher invocation in certain `WearOs` scenarios ([Iab44a](https://android-review.googlesource.com/#/q/Iab44ae49e1288a95e2c79334bfcd5e147ffdb75f)).
- Fix some translations for the `MediaRouteChooserDialog`. ([26da14](https://android.googlesource.com/platform/frameworks/support/+/26da14b8a0d61b65cb7f063c0ddb9d2e349b694c)).

## Version 1.7

### Version 1.7.0

March 20, 2024

`androidx.mediarouter:mediarouter:1.7.0` and `androidx.mediarouter:mediarouter-testing:1.7.0` are released. Version 1.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b0e4a78094191074b46ef428e2c04350e604f605..10bd7b9c1fd5169f3dfc50e744fa70aa87c65182/mediarouter).

**API Changes**

- Add `isSystemRoute()` to `MediaRouteDescriptor` and `RouteInfo` which returns true if the corresponding route is a system-managed route, which means that the system is the route provider and the app is in charge of feeding media samples to the system for their rendering ([I949e4](https://android-review.googlesource.com/#/q/I949e41347ede2fec98700f45de532cf89e75d9f8)). Bluetooth headsets, wired headsets and built-in speakers are examples of system routes.
- Deprecate `MediaRouter.removeRemoteControlClient`. You should call `setMediaSessionCompat(MediaSessionCompat)` instead of `addRemoteControlClient(Object)` so that there is no need to call `removeRemoteControlClient(Object)`. ([I8fc5e](https://android-review.googlesource.com/#/q/I8fc5e2ec38776d1f965541437c35dfda95eb276b)).
- Make `MediaRouteButton` extend `AppCompatImageView`. ([Ib455e](https://android-review.googlesource.com/#/q/Ib455eabd662effe6bde57a54f80a56ef009afde0)).
- Add `DEVICE_TYPE_SMARTPHONE`, which indicates that a media route is a smartphone. ([I39837](https://android-review.googlesource.com/#/q/I39837f2ed6a28c8126b7c3e9eff00e92cdb83639)).
- Improve device type mappings from `MediaRouter2` to AndroidX `MediaRouter` to describe system routes (for example: Bluetooth, HDMI, wired). ([Iccffa](https://android-review.googlesource.com/#/q/Iccffa930a861f091135db10b7109bab6c0aa4a94))

**Bug Fixes**

- Add missing icon resolutions for the route button that was possibly causing some isolated crashes. ([cddba9](https://android.googlesource.com/platform/frameworks/support/+/cddba9334fdcdc5e5e7ac6df9753df7095545814), [b/261878418](https://issuetracker.google.com/261878418)).
- Fix bug causing `isSystemRoute` to return true for user routes added via `android.media.MediaRouter#addUserRoute()` ([a27f6b](https://android.googlesource.com/platform/frameworks/support/+/a27f6bfd287635fac0803acfc37e42dd42229baa)).

**New Features**

- Bump the minSdk to 19. ([e8c4463](https://android.googlesource.com/platform/prebuilts/sdk/+/e8c4463c1643214ebc5bdbcf1a98869d80afec58))

### Version 1.7.0-rc01

March 6, 2024

`androidx.mediarouter:mediarouter:1.7.0-rc01` and `androidx.mediarouter:mediarouter-testing:1.7.0-rc01` are released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..816f86b18b935dea381f6abe363221eb1c538283/mediarouter).

### Version 1.7.0-beta01

February 21, 2024

`androidx.mediarouter:mediarouter:1.7.0-beta01` and `androidx.mediarouter:mediarouter-testing:1.7.0-beta01` are released. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/mediarouter)

### Version 1.7.0-alpha02

February 7, 2024

`androidx.mediarouter:mediarouter:1.7.0-alpha02` and `androidx.mediarouter:mediarouter-testing:1.7.0-alpha02` are released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..ca2a8cf8da3a3502fccc593974f8085653e38261/mediarouter)

**New Features**

- Bump the minSdk to 19. ([e8c4463](https://android.googlesource.com/platform/prebuilts/sdk/+/e8c4463c1643214ebc5bdbcf1a98869d80afec58))

**API Changes**

- Improve device type mappings from `MediaRouter2` to AndroidX `MediaRouter` to describe system routes (for example: Bluetooth, HDMI, wired). ([Iccffa](https://android-review.googlesource.com/#/q/Iccffa930a861f091135db10b7109bab6c0aa4a94))

**Bug Fixes**

- Fix bug causing `isSystemRoute` to return true for user routes added via `android.media.MediaRouter#addUserRoute()` ([a27f6b](https://android.googlesource.com/platform/frameworks/support/+/a27f6bfd287635fac0803acfc37e42dd42229baa)).

### Version 1.7.0-alpha01

November 15, 2023

`androidx.mediarouter:mediarouter:1.7.0-alpha01` and `androidx.mediarouter:mediarouter-testing:1.7.0-alpha01` are released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b0e4a78094191074b46ef428e2c04350e604f605..312eb9f1ddece3a18317f18515a877e0e745cb2c/mediarouter)

**API Changes**

- Add `isSystemRoute()` to `MediaRouteDescriptor` and `RouteInfo` which returns true if the corresponding route is a system-managed route, which means that the system is the route provider and the app is in charge of feeding media samples to the system for their rendering ([I949e4](https://android-review.googlesource.com/#/q/I949e41347ede2fec98700f45de532cf89e75d9f8)). Bluetooth headsets, wired headsets and built-in speakers are examples of system routes.
- Deprecate `MediaRouter.removeRemoteControlClient`. You should call `setMediaSessionCompat(MediaSessionCompat)` instead of `addRemoteControlClient(Object)` so that there is no need to call `removeRemoteControlClient(Object)`. ([I8fc5e](https://android-review.googlesource.com/#/q/I8fc5e2ec38776d1f965541437c35dfda95eb276b)).
- Make `MediaRouteButton` extend `AppCompatImageView`. ([Ib455e](https://android-review.googlesource.com/#/q/Ib455eabd662effe6bde57a54f80a56ef009afde0)).
- Add `DEVICE_TYPE_SMARTPHONE`, which indicates that a media route is a smartphone. ([I39837](https://android-review.googlesource.com/#/q/I39837f2ed6a28c8126b7c3e9eff00e92cdb83639)).

**Bug Fixes**

- Add missing icon resolutions for the route button that was possibly causing some isolated crashes. ([cddba9](https://android.googlesource.com/platform/frameworks/support/+/cddba9334fdcdc5e5e7ac6df9753df7095545814), [b/261878418](https://issuetracker.google.com/261878418)).

## Version 1.6

### Version 1.6.0

September 20, 2023

`androidx.mediarouter:mediarouter:1.6.0` and `androidx.mediarouter:mediarouter-testing:1.6.0` are released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0bdaed7dcede1e26861f5e60c08633ca79fa42cf..b0e4a78094191074b46ef428e2c04350e604f605/mediarouter)

**Major features since 1.4.0**

- Route Listing preferences for output switcher
- Add route listing preference support to AndroidX MediaRouter.
- Add visibility support for MediaRouteDescriptor.
- Revamp the MediaRouteButton to provide a better user experience ((I9dbcb)\[https://android-review.googlesource.com/#/q/I9dbcb8d9e5ee4902d48f1bfb4133e04781c6ae35)). Including:
  - Add a hint to the user to check the searched device is on the same wifi.
  - Add an end state with an error message to be shown at the end of a predefined period of time.
- Added automatic dismissal of the MediaRouter dialog when screen is turned off.

### Version 1.6.0-rc01

August 23, 2023

`androidx.mediarouter:mediarouter:1.6.0-rc01` and `androidx.mediarouter:mediarouter-testing:1.6.0-rc01` are released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..2c0f492a1ad8bfa69506ab50b77cbc51e3e2a66c/mediarouter)

**New Features**

- Added automatic dismissal of the `MediaRouter` dialog when screen is turned off. ([Ib25ee](https://android.googlesource.com/platform/frameworks/support/+/b96f8039105d4991a435f734c63218d28ebe208a)).

**Bug Fixes**

- Changed the `MediaRouter` logging tag to `AxMediaRouter` to disambiguate from the platform `MediaRouter`. ([Ib619f](https://android.googlesource.com/platform/frameworks/support/+/1d6347e40e3f856453abf16078c1786b54532634)).

### Version 1.6.0-beta01

August 9, 2023

`androidx.mediarouter:mediarouter:1.6.0-beta01` and `androidx.mediarouter:mediarouter-testing:1.6.0-beta01` are released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dfe594066da9582870e83c75e366b9b9a05208c0..4aed940027a19667e67d155563fc5fa8b7279313/mediarouter)

**API Changes**

- Fix support for Android U platform APIs. ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87), [b/289269026](https://issuetracker.google.com/issues/289269026))

**Bug Fixes**

- Fix translations in `MediaRouteChooserDialog`. ([d39a7f](https://android.googlesource.com/platform/frameworks/support/+/d39a7face66cb42898b3c4aa97f7857c420e827d%5E%21/#F2))

### Version 1.6.0-alpha05

June 21, 2023

`androidx.mediarouter:mediarouter:1.6.0-alpha05` and `androidx.mediarouter:mediarouter-testing:1.6.0-alpha05` are released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..dfe594066da9582870e83c75e366b9b9a05208c0/mediarouter)

**New Features**

- Improve the `MediaRouteChooserDialog` UI to handle the lack of discovered devices by providing written guidance to the user ([I0cad9](https://android.googlesource.com/platform/frameworks/support/+/4615d44114048f5224b025361a16d00082458a8c), [I3d445](https://android.googlesource.com/platform/frameworks/support/+/5cc91aa86051956af0138c05570b9d1e7e72889e)).

### Version 1.6.0-alpha04

June 7, 2023

`androidx.mediarouter:mediarouter:1.6.0-alpha04` and `androidx.mediarouter:mediarouter-testing:1.6.0-alpha04` are released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- Revamp the `MediaRouteButton` to provide a better user experience ([I9dbcb](https://googleplex-android.googlesource.com/platform/frameworks/support/+/72e83d6e55f7682406261bfcd78e0d7f81f3db92)). Including:
  - Add a hint to the user to check the searched device is on the same wifi.
  - Add an end state with an error message to be shown at the end of a predefined period of time.

**API Changes**

- Bring in new `MediaRouteDescriptor` device types from the platform. ([I75ba6](https://googleplex-android.googlesource.com/platform/frameworks/support/+/fe62f4d9d605deeb3a1e61d7feb5aa5c08aadb6a)).

**Bug Fixes**

- Fixed volume adjustment on non-dynamic route controllers ([I730ec](https://googleplex-android.googlesource.com/platform/frameworks/support/+/93f409c56507fdc271a1bc41b8aa3130811ed4f5)).
- Make `MediaRouteButton` always enabled ([I1e9ff](https://googleplex-android.googlesource.com/platform/frameworks/support/+/4dad8d968cf3801581ba2b3a8281ca13a9d0ba27%5E%21/#F0)).
- Fix some android version runtime checks preventing Android U features from being accessible using the AndroidX media router library ([I97cab](https://googleplex-android.googlesource.com/platform/frameworks/support/+/cb5e531e3a814749cc308c767714c0a641d2b5cc)).

### Version 1.6.0-alpha03

April 12, 2023

`androidx.mediarouter:mediarouter:1.6.0-alpha03` and `androidx.mediarouter:mediarouter-testing:1.6.0-alpha03` are released. This was released from an internal branch.
| **Note:** This version will only compile against the Android 14 Beta 1 SDK.

- Make some changes around `MediaRouteDescriptor`'s visibility API.
- Deprecate `MediaRouteActionProvider.setAlwaysVisible` and `MediaRouteButton.setAlwaysVisible`, making the media route button always visible, regardless of the network connectivity, or the availability of media routes.
- Fix volume adjustment for non-dynamic route controllers. This addresses a bug where trying to adjust the volume of a route in the output switcher would cause volume to go back to its original value ([93f409](https://android.googlesource.com/platform/frameworks/support/+/93f409c56507fdc271a1bc41b8aa3130811ed4f5)).

### Version 1.6.0-alpha02

March 8, 2023

`androidx.mediarouter:mediarouter:1.6.0-alpha02` and `androidx.mediarouter:mediarouter-testing:1.6.0-alpha02` are released. Developed on internal branch.

**New Features**

- Add route listing preference support to AndroidX `MediaRouter`.
- Add visibility support for `MediaRouteDescriptor`.

**Bug Fixes**

- Improve SystemUI output switcher invocation on Android U+.

### Version 1.6.0-alpha01

February 10, 2023

`androidx.mediarouter:mediarouter:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6baf17024ccdfc27531f3b18b534341162885d1a..6d22a07c33e6f53eafa5be1ef0b4aa27b1c7080a/)

**New Features**

- Route Listing preferences for output switcher

**API Changes**

- Mechanism for the app to configure the output switcher.

## Version 1.4

### Version 1.4.0

May 3, 2023

`androidx.mediarouter:mediarouter:1.4.0` and `androidx.mediarouter:mediarouter-testing:1.4.0` are released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b4796d8003385f8c36719805a80f658abd99c2f..0bdaed7dcede1e26861f5e60c08633ca79fa42cf/mediarouter)

**Important changes since 1.3.1**

- Add `SystemOutputSwitcherDialogController#showDialog` to show the system's output switcher dialog, or the Bluetooth Settings Fragment on Wear devices where the system output switcher is not available. ([Ic3d78](https://android-review.googlesource.com/#/q/Ic3d7874263d6bb1fbdbc01ff265642f984711e98))
- Fix regression causing application crashes due `IllegalArgumentException` in `MediaRouterProvider.notifyDynamicRoutesChanged` ([7d17ea](https://android.googlesource.com/platform/frameworks/support/+/7d17ea43394f687d40c5d64830eb4544ef9e2590)).
- Add `MediaRouteDescriptor.Builder.clearControlFilters` ([I3a4e1](https://android-review.googlesource.com/#/q/I3a4e1dde46dced116d574991abe9be5e7134db3f))
- Add missing `MainThread` annotations in `MediaRouter`. ([I3ef6e](https://android-review.googlesource.com/#/q/I3ef6ea1113fcd88b33900f790e0f1979901d4cd7))
- Add broadcast receiver export flags on API 33+ ([b2a663](https://android.googlesource.com/platform/frameworks/support/+/b2a66336c9a9e18f70cde28d2b91cafd18d00837%5E%21/#F7)).

### Version 1.4.0-rc01

April 5, 2023

`androidx.mediarouter:mediarouter:1.4.0-rc01` and `androidx.mediarouter:mediarouter-testing:1.4.0-rc01` are released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7da190979ae2a30f5d29a8fe68b447516d992082..118447f9f3eb2cd8c79c8e0be47e6b8114202524/mediarouter)

- Remove null lists in MediaRouteProviderDescriptor.

### Version 1.4.0-beta02

February 22, 2023

`androidx.mediarouter:mediarouter:1.4.0-beta02` is released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6baf17024ccdfc27531f3b18b534341162885d1a..7da190979ae2a30f5d29a8fe68b447516d992082/mediarouter/mediarouter)

**Bug Fixes**

- Fix regression causing application crashes due `IllegalArgumentException` in `MediaRouterProvider.notifyDynamicRoutesChanged` ([7d17ea](https://android.googlesource.com/platform/frameworks/support/+/7d17ea43394f687d40c5d64830eb4544ef9e2590)).

### Version 1.4.0-beta01

January 25, 2023

`androidx.mediarouter:mediarouter:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..6baf17024ccdfc27531f3b18b534341162885d1a/mediarouter/mediarouter)

**API Changes**

`DynamicGroupRouteController.notifyDynamicRoutesChanged()` now throws `IllegalArgumentException` when no route passed is SELECTED or SELECTING. ([8f6b3e](https://android.googlesource.com/platform/frameworks/support/+/8f6b3ef4b734a0db0725ab209c8942723a4c3cfe))

**Bug Fixes**

- Fix crash caused by an api-compliant provider service implementation returning a null route provider. ([63f16d](https://android.googlesource.com/platform/frameworks/support/+/63f16d2ca12c51796925ab197eefb73ea54bbbde))
- Make protected broadcast receivers work on apps targeting API 33+ by marking them as non-exported. ([784f8b](https://android.googlesource.com/platform/frameworks/support/+/784f8bb1f510946a448561cfdb353c0301f2db5f))
- Fix some spurious nullability annotations in `OverlayListView`. ([472e3f](https://android.googlesource.com/platform/frameworks/support/+/472e3f03f81f4eb0069be0138c9deec8c0d568e9))
- Fix bug where `EXTRA_CLOSE_ON_CONNECT` in `SystemOutputSwitcherDialogController.showDialog` would cause the bluetooth settings fragment to close suddenly on wear devices. ([28c9d8](https://android.googlesource.com/platform/frameworks/support/+/28c9d8f1a4d8fc6c3b3f72b863010ada9bdce916))
- Changed to Javadoc of Output Switcher's public methods. ([f0ae94](https://android.googlesource.com/platform/frameworks/support/+/f0ae9461df462a340cb45e26e18b1ff14b163e61), [44d2c9](https://android.googlesource.com/platform/frameworks/support/+/44d2c94c5d525287139c1feaa5ad79551d728e64))

### Version 1.4.0-alpha01

November 9, 2022

`androidx.mediarouter:mediarouter:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b4796d8003385f8c36719805a80f658abd99c2f..a1e318590b217ecfce1b2de17eed2f18b6a680bb/mediarouter/mediarouter)

**New Features**

- Add `SystemOutputSwitcherDialogController#showDialog` to show the system's output switcher dialog, or the Bluetooth Settings Fragment on Wear devices where the system output switcher is not available. ([Ic3d78](https://android-review.googlesource.com/#/q/Ic3d7874263d6bb1fbdbc01ff265642f984711e98))

**API Changes**

- Add `MediaRouteDescriptor.Builder.clearControlFilters` ([I3a4e1](https://android-review.googlesource.com/#/q/I3a4e1dde46dced116d574991abe9be5e7134db3f))
- Add missing `MainThread` annotations in `MediaRouter`. ([I3ef6e](https://android-review.googlesource.com/#/q/I3ef6ea1113fcd88b33900f790e0f1979901d4cd7))

**Bug Fixes**

- Fix device-specific crash caused by calling `MediaRouter.removeUserRoute` ([b/202931542](https://issuetracker.google.com/issues/202931542)).
- Fix group descriptors not receiving volume handling updates consistently ([461303](https://android.googlesource.com/platform/frameworks/support/+/461303cd4b2c3e6bbf88eb0f4458b7b67bee34a0%5E%21/#F0)).
- Add broadcast receiver export flags on API 33+ ([b2a663](https://android.googlesource.com/platform/frameworks/support/+/b2a66336c9a9e18f70cde28d2b91cafd18d00837%5E%21/#F7)).
- Fix crash caused by receiving invalid route descriptors from the platform ([dd5c09](https://android.googlesource.com/platform/frameworks/support/+/dd5c09bfd80d0f5c77036d7c5fd5622ac9ec9934)).

## Version 1.3

### Version 1.3.1

July 27, 2022

`androidx.mediarouter:mediarouter:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d15c54ec9034549e7b7ce6b631f032d8c322dfd0..3b4796d8003385f8c36719805a80f658abd99c2f/mediarouter/mediarouter)

**Bug Fixes**

- Work around a device-specific issue where `MediaRouter.removeUserRoute()` would throw an unexpected `IllegalArgumentException` ([b/202931542](https://issuetracker.google.com/issues/202931542)).

### Version 1.3.0

April 20, 2022

`androidx.mediarouter:mediarouter:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38c02ea495b416f7db83faaefb8674d94f0c2dfc..d15c54ec9034549e7b7ce6b631f032d8c322dfd0/mediarouter/mediarouter)

**Important changes since 1.2.0**

- Add a flag into `MediaRouterParams` that can be used to disable seamless transfer at runtime.
- Added a testing artifact which can reset the `MediaRouter`.
- Add a router param for UX tweak in `MediaRouterControllerDialog`.
- Annotated nullness for public methods.
- API lint check for `MissingGetterMatchingBuilder` is enabled for androidx.
- Update dependency on core for mediarouter to 1.6.0.

### Version 1.3.0-rc01

March 23, 2022

`androidx.mediarouter:mediarouter:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..38c02ea495b416f7db83faaefb8674d94f0c2dfc/mediarouter/mediarouter)

- No changes since the last beta release.

### Version 1.3.0-beta01

March 9, 2022

`androidx.mediarouter:mediarouter:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7b3f681a0464178e603cba3dce271b86b5de1234..33cb12e8aba043a05b40470a5ef3be1b35114fd5/mediarouter/mediarouter)

- No changes since the last alpha release.

### Version 1.3.0-alpha01

December 15, 2021

`androidx.mediarouter:mediarouter:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/94e8a6b7a1769388b24b77e3920b06019071cc2d..7b3f681a0464178e603cba3dce271b86b5de1234/mediarouter/mediarouter)

**API Changes**

- Add a flag into `MediaRouterParams` that can be used to disable seamless transfer at runtime ([I53d68](https://android-review.googlesource.com/#/q/I53d687a07bceb307530241851bb453d425f20ba1))
- Added a testing artifact which can reset the `MediaRouter`. ([Id167c](https://android-review.googlesource.com/#/q/Id167c77cf72ffe322056eb36d52a58c1a0169bb9))
- Add a router param for UX tweak in `MediaRouterControllerDialog` ([I7e574](https://android-review.googlesource.com/#/q/I7e574f16dd509b499badb50c9f7dc2c105117e95))
- Annotated nullness for public methods ([Ifc901](https://android-review.googlesource.com/#/q/Ifc901081f52334709858b5f8efda05e1c97295d6))

**Bug Fixes**

- API lint check for `MissingGetterMatchingBuilder` is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9), [b/138602561](https://issuetracker.google.com/issues/138602561))

## Version 1.2

### Version 1.2.6

January 26, 2022

`androidx.mediarouter:mediarouter:1.2.6` is released. [Version 1.2.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/94e8a6b7a1769388b24b77e3920b06019071cc2d..66099ad80f574c8eb6361eff3ee7e7472ee90843/mediarouter/mediarouter)

**Bug Fixes**

- Fix `RemotePlaybackClient` constructor crash on Android 12 [b/210684559](https://issuetracker.google.com/210684559)

### Version 1.2.5

September 1, 2021

`androidx.mediarouter:mediarouter:1.2.5` is released. [Version 1.2.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/638ef4da0b4dd777b42374e6e17e4d64ee787d4d..94e8a6b7a1769388b24b77e3920b06019071cc2d/mediarouter/mediarouter)

**Bug Fixes**

- Hide the media route button in the Output switcher when there is no routes to transfer.
- Fix issues of controlling the volume of group member routes.

### Version 1.2.4

June 16, 2021

`androidx.mediarouter:mediarouter:1.2.4` is released. [Version 1.2.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ab0e0fa1d05c014d6bbec0091425363dbd629259..638ef4da0b4dd777b42374e6e17e4d64ee787d4d/mediarouter/mediarouter)

**Bug Fixes**

- Fixed an issue where MediaRouteButton replays connecting animation.
- Fixed the vertical alignment of routes in `MediaRouteChooserDialog`.

### Version 1.2.3

May 5, 2021

`androidx.mediarouter:mediarouter:1.2.3` is released. [Version 1.2.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/773ee0f10f4aefa072b6c62f93eaf5c2862e8044..ab0e0fa1d05c014d6bbec0091425363dbd629259/mediarouter/mediarouter)

**Bug Fixes**

- Fixed the NullPointerException for customized chooser dialog.
- Fixed issue where the MediaRouteButton shows a disconnected state even when it's connected, if it is temporarily disabled.

### Version 1.2.2

February 10, 2021

`androidx.mediarouter:mediarouter:1.2.2` is released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b7d013387af59eee31d948bb9e3da6601a40d914..773ee0f10f4aefa072b6c62f93eaf5c2862e8044/mediarouter/mediarouter)

**Bug Fixes**

- Do not try to reselect the selected route when `OnDynamicRouteChangedListener.onRouteChanged` is called.

### Version 1.2.1

January 13, 2021

`androidx.mediarouter:mediarouter:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ae3985dad56118fe76563ade00e2f24a987d1a0d..b7d013387af59eee31d948bb9e3da6601a40d914/mediarouter/mediarouter)

**Bug Fixes**

- Fix selecting phone speaker when `unselect()` is called while BT is available
- Fix MediaRouter.Callback timing. `Callback#onRouteSelected` and `Callback#onRouteUnselected` will be called after `OnPrepareTransferListener#onPrepareTransfer` is completed.

### Version 1.2.0

October 14, 2020

`androidx.mediarouter:mediarouter:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64dec1870d3b3af9f23965460c10c8390f484a33..ae3985dad56118fe76563ade00e2f24a987d1a0d/mediarouter/mediarouter)

**Major Features Since 1.1.0**

- Support seamless media transfer that enables media transfer via System UI: See the [What's new in Media video](https://youtu.be/fhii2K9o6ts) for more details
- Changed the guidance on registering callback. See the example code in the Javadoc of `MediaRouter.addCallback()`
- Add a new listener `MediaRouter#OnPrepareTransferListener` for receiving events when the selected route is about to be changed
- Add `MediaRouterParams` to denote routing functionality and UI types.
- Prevent tentative usages of internal use only methods with `@RestrictTo(LIBRARY)`

### Version 1.2.0-rc02

October 1, 2020

`androidx.mediarouter:mediarouter:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/69619173445c0eaf71ef0074b02b44269c2e983a..64dec1870d3b3af9f23965460c10c8390f484a33/mediarouter/mediarouter)

**Bug Fixes**

- Fixed an issue that `RouteController#onUnselect` may not be called when the user stopped casting via System UI.

### Version 1.2.0-rc01

September 16, 2020

`androidx.mediarouter:mediarouter:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..69619173445c0eaf71ef0074b02b44269c2e983a/mediarouter/mediarouter)

**Bug Fixes**

- Fixed the disconnection of the current casting when Bluetooth audio device is connected.
- Fixed throwing `IllegalArgumentException` in `MediaRouteProvider#notifyDynamicRoutesChanged()`.
- Make stop casting from the output switcher work

### Version 1.2.0-beta01

September 2, 2020

`androidx.mediarouter:mediarouter:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..31022a2dda22705843be1199c786552a6f9f875d/mediarouter/mediarouter)

**New Features**

- Support seamless media transfer that enables media transfer via System UI: See the [What's new in Media video](https://youtu.be/fhii2K9o6ts) for more details

**API Changes**

- Make `MediaRouter.OnPrepareTransferListener` use ListenableFuture

**Bug Fixes**

- Fix volume controls of group routes.
- When a group route is created, creates a group route first and member routes later.
- Make "Stop" in Output switcher work.
- Fix callbacks that are not called expected
  - `RouteController#onSelect` when a routing session is created.
  - `MediaRouter.Callback#onRouteSelected` when transferring to phone from cast.
  - `MediaRouter.Callback#onRouteSelected` with the correct group route info.
- Make the callbacks be removed

### Version 1.2.0-alpha02

July 22, 2020

`androidx.mediarouter:mediarouter:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..9f60cc700129e30cee9df020005c317fb39d32ec/mediarouter/mediarouter)

**API Changes**

- Add a new `MediaRouter.Callback#onRouteSelected` to get notified when the selected route are different from the requested route ([Ieee16](https://android-review.googlesource.com/#/q/Ieee163d3487d28be5088311316b881885c5d6f08))
- Add a new listener `MediaRouter#OnPrepareTransferListener` for receiving events when the selected route is about to be changed ([I6ace1](https://android-review.googlesource.com/#/q/I6ace162aec4d12c70d8da094041ae13126e6d61f))
- Add MediaRouterParam ([I33150](https://android-review.googlesource.com/#/q/I33150fa6864bad35385a9a6ca8dd36c89b506857))
- Changed the guidance on registering callback. See the example code in the Javadoc of `MediaRouter.addCallback()` ([I58112](https://android-review.googlesource.com/#/q/I58112e7d2ab50efef5141527e073f4b090800fb3))

### Version 1.2.0-alpha01

April 15, 2020

`androidx.mediarouter:mediarouter:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/acf26b9b01f4429d77435f3c20d46e01cc03ca9a..24daa503442fcd3e44ada60cf1da41df2815c045/mediarouter/mediarouter)

**API Changes**

- Prevent tentative usages of internal use only methods with `@RestrictTo(LIBRARY)`

**Bug Fixes**

- Resolved talkback on cast dialog issue
- Guard DynamicGroupRouterController's listener with a Lock

## Version 1.1

### Version 1.1.0

September 5, 2019

`androidx.mediarouter:mediarouter:1.1.0` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/de87d1aef00e890a6117a03ca8af2168b2227bc5..acf26b9b01f4429d77435f3c20d46e01cc03ca9a/mediarouter).

**Import changes since 1.0.0**

- Dynamic group support
  - Allows users to add or remove route devices dynamically.
  - To enable a dynamic group, call `MediaRouteButton.enableDynamicGroup()`; the app shows a new dialog for the dynamic group
  - The installed `MediaRouteProvider` should also support dynamic group to actually enable the functionality.

### Version 1.1.0-rc01

June 13, 2019

`androidx.mediarouter:mediarouter:1.1.0-rc01` is released with no changes from `1.1.0-beta02`. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/75e93a025020288fd9cd22580aabbcd7b11b4fd9..de87d1aef00e890a6117a03ca8af2168b2227bc5/mediarouter).

### Version 1.1.0-beta02

June 5, 2019

`androidx.mediarouter:mediarouter:1.1.0-beta02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/2c7181c30858d401daba909d0a9400d5fc8d16d9..75e93a025020288fd9cd22580aabbcd7b11b4fd9/mediarouter).

**New features**

- Support RTL languages in MediaRouter dialogues

**Bug fixes**

- Fix the bottom padding of MediaRoute dialogues

### Version 1.1.0-beta01

May 7, 2019

`androidx.mediarouter:mediarouter:1.1.0-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/4b8b1a18bf33c6daf7400de92c09fde21da06f6f..2c7181c30858d401daba909d0a9400d5fc8d16d9/mediarouter).

**New features**

- Changed `IllegalPointerException` to `NullPointerException` for the null arguments which marked as `@NonNull`.

**API changes**

- Callback logic for `DynamicRouteDescriptor` was changed. Now `MediaRouteProvider` will call `MediaRouterProvider.DynamicGroupController.notifyDynamicRoutesChanged` instead of directly calling the callback method.

### Version 1.1.0-alpha03

April 3, 2019

`androidx.mediarouter:mediarouter:1.1.0-alpha03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/b76873b4b2d548744a08dc5180c4b94b924b9886..4b8b1a18bf33c6daf7400de92c09fde21da06f6f/mediarouter).

**Bug fixes**

- Fixed crashes on MediaRouteVolumeSlider and RegisteredMediaRouteProvider.

### Version 1.1.0-alpha02

March 13, 2019

`androidx.mediarouter:mediarouter:1.1.0-alpha02` is released. The full list of commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/b9925c3695ce7da0625a2fd3ded0149b7153826c..b76873b4b2d548744a08dc5180c4b94b924b9886/mediarouter).

**New features**

- Support MediaRouteButton in Android Studio layout preview

**API changes**

- Added `enableDynamicGroup()` method in `MediaRouteActionProvider` and `MediaRouteButton` to enable dynamic group feature
- Added `setAlwaysVisible(boolean)` method in `MediaRouteActionProvider` and `MediaRouteButton` to allow `MediaRouteButton` visible always

**Bug fixes**

- Made `MediaRouteCastDialog` rows easy to click
- Removed unnecessary calls of `onRouteChanged` callback

### Version 1.1.0-alpha01

December 3, 2018

**New features**

- Added support dynamic group routes
  - Added APIs to support dynamic group routes by `MediaRouteProviders`
  - Added new UX for route chooser and controller dialogues for dynamic group routes