---
title: https://developer.android.com/about/versions/16/qpr2/release-notes
url: https://developer.android.com/about/versions/16/qpr2/release-notes
source: md.txt
---

### Beta 3

|---|---|
| **Release date** | November 10, 2025 |
| **Builds** | BP41.250916.015.A1 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-10-05 |
| **Google Play services** | 25.34.34 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

### Beta 2

|---|---|
| **Release date** | September 17, 2025 |
| **Builds** | BP41.250822.010 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-09-05 |
| **Google Play services** | 25.29.32 |
| **API diff** | - [QPR2 Beta 1 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

### Beta 1

|---|---|
| **Release date** | August 20, 2025 |
| **Builds** | BP41.250725.006 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-08-05 |
| **Google Play services** | 25.25.33 |
| **API diff** | - [API 36 → QPR2 Beta 1](https://developer.android.com/sdk/api_diff/b-1-beta1/changes) |

## About Android 16 QPR2 Beta 3

QPR2 Beta 3 is now available. This is our second platform stability
release, and it includes many fixes, including to the following issues:

- Google Play System Updates were failing to install for some users. ([Issue #420748298](https://issuetracker.google.com/issues/420748298), [Issue #438257102](https://issuetracker.google.com/issues/438257102))
- Home screen shortcuts appeared as blank gray circles. ([Issue #440302367](https://issuetracker.google.com/issues/440302367))
- The Wallet icon on your lockscreen could sometimes appear with incorrect coloring. ([Issue #419061603](https://issuetracker.google.com/issues/419061603), [Issue #434489536](https://issuetracker.google.com/issues/434489536))
- Battery charged to 100% when adaptive charging is turned on ([Issue #445583926](https://issuetracker.google.com/issues/445583926))
- The swipe-up gesture from the bottom occasionally stopped working. ([Issue #436632152](https://issuetracker.google.com/issues/436632152), [Issue #445023211](https://issuetracker.google.com/issues/445023211))
- Your selected theme might not apply on the first attempt. ([Issue #440830741](https://issuetracker.google.com/issues/440830741))
- 50MP images captured with the ultrawide or telephoto lens displayed rainbow artifacts. ([Issue #422058430](https://issuetracker.google.com/issues/422058430), [Issue #443250512](https://issuetracker.google.com/issues/443250512))
- Poor battery life due to excessive CPU usage by the launcher, particularly on foldable devices. ([Issue #441741448](https://issuetracker.google.com/issues/441741448))
- Calls could incorrectly route Bluetooth audio. ([Issue #448580013](https://issuetracker.google.com/issues/448580013), [Issue #448580779](https://issuetracker.google.com/issues/448580779))
- Users in New Zealand could not access all 6GHz Wi-Fi networks. ([Issue #444050891](https://issuetracker.google.com/issues/444050891))
- The Terminal app would crash if you changed your device's UI font size while it was open. ([Issue #412082408](https://issuetracker.google.com/issues/412082408))
- Users couldn't type special characters like `\*`, `@`, or `#` in the GUI terminal. ([Issue #444130818](https://issuetracker.google.com/issues/444130818))
- Simultaneously swiping lockscreen widgets and the notification shade caused buggy animations and a laggy, unresponsive UI. ([Issue #446133358](https://issuetracker.google.com/issues/446133358))
- The screen sometimes became unresponsive or froze when unlocking the device.
- Display freezes and screen noise
- Unexpected device crashes

## About Android 16 QPR2 Beta 2

[QPR2 Beta 2 is now available](https://android-developers.googleblog.com/2025/09/android-16-qpr2-beta-2-is-here.html) and has released Platform Stability. That
means that the API surface is locked, and the app-facing behaviors are final, so
you can incorporate them into your apps and take advantage of our latest
platform innovations. Android 16 QPR2 is still in active development, so the
Android system and apps running on it might not always work as expected.

## What's new in QPR2 Beta 2

This late stage in the development cycle focuses largely on readying the
platform for release, but there are still a few new things to cover.

### Testing developer verification

[Android developer verification](https://developer.android.com/developer-verification)
is a
[new requirement](https://android-developers.googleblog.com/2025/08/elevating-android-security.html)
designed to link real-world entities (individuals and organizations) with their
Android applications to make
it harder for bad actors to spread harm.

Starting in September 2026 and in specific regions, Android will require apps to
be registered by verified developers to be installed on
[certified Android devices](https://www.android.com/certified/partners/),
with an exception made for installs made through the Android Debug
Bridge (ADB).

As a developer, you are free to install apps without verification with ADB. This
is designed to support your need to develop and test apps that are not intended
or not yet ready to distribute to the wider consumer population.

For apps that
[enable user-initiated installation of app packages](https://support.google.com/googleplay/android-developer/answer/12085295),
Android 16 QPR2 Beta 2 contains new APIs that support developer verification
during installation, along with a new adb command to let you force a
verification outcome for testing purposes.

### SMS OTP Protection

The delivery of messages containing an
[SMS retriever hash](https://developers.google.com/identity/sms-retriever/verify)
will be delayed for most apps for three hours to help prevent OTP hijacking.
Apps can continue to use the
[SMS retriever API](https://developers.google.com/identity/sms-retriever/overview)
to access messages intended for them in a timely manner.

### Custom app icon shapes

Android 16 QPR2 allows users to select from a list of icon shapes that apply to
all app icons and folder previews.

### More efficient garbage collection

The Android Runtime (ART) now includes a Generational Concurrent Mark-Compact
(CMC) Garbage Collector in Android 16 QPR2 that focuses collection efforts on
newly allocated objects, which are more likely to be garbage. You can expect
reduced CPU usage from garbage collection, a smoother user experience with less
jank, and improved battery efficiency.

### Automatic step tracking and expanded exercise data in Health Connect

Health Connect now automatically tracks steps using the device's sensors, and
the `ExerciseSegment` and `ExerciseSession` data types have been updated.

## About Android 16 QPR2 Beta 1

[QPR2 Beta 1 is now available](https://android-developers.googleblog.com/2025/08/android-16-qpr2-beta-1-is-here.html)
with the latest features and changes to try with
your apps. This release is suitable for development, testing, and general use.
However, Android 16 QPR2 is still in active development, so the Android system
and apps running on it might not always work as expected.

Unlike the major platform release in Q2 that included behavior changes that
impact app compatibility, the changes in this release are largely additive
and designed to minimize the need for additional app testing.

## What's new in QPR2 Beta 1

QPR2 Beta 1 includes new features and changes to try out with your apps:

### UI, System Experience, and Accessibility

- Expanded Dark Theme
- Auto-Themed App Icons
- Interactive Chooser Sessions
- Smoother Android Migrations
- PDF Document Annotation and Editing
- Display Topology API
- Device-aware View Configuration
- Granular Haptic Feedback Control
- Quick Settings Tile Categories

### Media \& Audio

- IAMF Decoding Support
- Personal Audio Sharing in Output Switcher
- New AAudio APIs
- HDR/SDR Brightness Slider

### Connectivity

- Companion Device Management Enhancements
- MediaRouter Network Privacy Improvements

### Privacy \& Security

- Secure Lock Device
- Phone Theft Protection Toggle

### Developer Productivity

- Widget Engagement Metrics
- Early Warnings for 16KB Page Size Compatibility
- Enhanced Profiling
- More Robust Multi-Display Testing

## How to get Beta 1

You can install this release on any of the following Google Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 6a
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold
- Pixel 9a

See [Get Android 16 QPR2](https://developer.android.com/about/versions/16/qpr2/get) for details on how to get
started.

Remember to update your SDK and the Android Emulator as well before you try out
the latest features and changes. The best way to do this is using the SDK
Manager in the [latest preview version of Android Studio](https://developer.android.com/studio/preview).

Depending on your development and testing needs, you can also get Android 16 in
the following ways:

- Get Android 16 QPR2 [on the Android Emulator](https://developer.android.com/about/versions/16/qpr2/get#on_emulator)
- Get a [Generic System Image](https://developer.android.com/about/versions/16/qpr2/gsi-release-notes) (GSI)

### General advisories

While a key goal of this release is maintaining app compatibility:

- This release might have various stability, battery, or performance issues.
- For users with accessibility needs, this release might not be appropriate for daily use.
- Some apps might not function as expected when running on this release. This limitation includes Google's apps as well as other apps.
- Android 16 Beta builds aren't [Compatibility Test Suite
  (CTS)-approved](https://source.android.com/compatibility/cts/), but they have passed preliminary testing and provide a stable set of pre-release APIs for developers. Apps that depend on CTS-approved builds or use [Play Integrity API](https://developer.android.com/google/play/integrity) might not work normally on Android 16 Beta builds.

### Get support

Two primary support channels are available to you when developing and testing
with Android Beta. The channel you should use to get support depends on where
you are encountering your issue.

- **Support for device-specific issues, system issues, and issues with Google
  apps** : Use the Issue Tracker to create new issues and to view and track issues that you and other developers have submitted. Before creating your own issue, check the known issues listed on this page and search the lists of [top
  open issues](https://developer.android.com/about/versions/16/qpr2/top-issues) and [recently created issues](https://developer.android.com/about/versions/16/qpr2/recent-issues) to see if someone else has already reported it. You can subscribe and vote for an issue by clicking **star this issue** . See [Where to report issues](https://developer.android.com/about/versions/16/qpr2/feedback#templates) to find an issue template that best matches the type of issue that you are encountering.
- **Support for issues with other apps**: Contact the app developer directly.

To discuss issues or ideas with other developers and users working with the
Android 16 QPR2 Beta, join the
[android_beta community on Reddit](https://developer.android.com/about/versions/16/qpr2/dev-community).