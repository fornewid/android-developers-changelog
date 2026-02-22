---
title: https://developer.android.com/about/versions/15/release-notes
url: https://developer.android.com/about/versions/15/release-notes
source: md.txt
---

### Beta 3

|---|---|
| **Release date** | January 21, 2025 |
| **Build** | BP11.241210.004 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | January 2025 |
| **Google Play services** | 24.45.32 |

### Beta 2.1

|---|---|
| **Release date** | January 9, 2025 |
| **Build** | BP11.241121.013 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | December 2024 |
| **Google Play services** | 24.45.32 |

### Beta 2

|---|---|
| **Release date** | December 16, 2024 |
| **Build** | BP11.241121.010 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | December 2024 |
| **Google Play services** | 24.45.32 |

### Beta 1

|---|---|
| **Release date** | November 12, 2024 |
| **Build** | BP11.241025.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | November 2024 |
| **Google Play services** | 24.39.34 |

## About Android 15 QPR2 Beta 3

Building on the [initial release of Android 15](https://developer.android.com/about/versions/15), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use. However, review any known issues that
are listed on this page.

Android 15 QPR2 builds on the updates in the initial release of Android 15 and
Android 15 QPR1. This QPR release includes the next round of refinements such as
bug fixes and improvements to stability and performance.

### How to get QPR2 Beta 3

You can install Android 15 QPR2 Beta 3 on any of the following Google Pixel
devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

See [Get Android 15 QPR beta builds](https://developer.android.com/about/versions/15/get-qpr) for details on how to get started.
| **Note:** All eligible devices enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta) will be offered an over-the-air (OTA) update to Beta 3.

### General advisories

Be aware of these general advisories about the release:

- This release might have various stability, battery, or performance issues.
- For users with accessibility needs, this release might not be appropriate for daily use.
- Some apps might not function as expected when running on this release. This limitation includes Google's apps as well as other apps.
- Android 15 QPR beta builds aren't [Compatibility Test Suite
  (CTS)](https://source.android.com/compatibility/cts/)-approved, but they have passed preliminary testing and provide a stable set of pre-release APIs for developers. Apps that depend on CTS-approved builds or use the [Play Integrity API](https://developer.android.com/google/play/integrity) ([SafetyNet APIs are
  deprecated](https://developer.android.com/privacy-and-security/safetynet/deprecation-timeline)) might not work normally on Android 15 QPR beta builds.

### Get support

Two primary support channels are available to you when developing and testing
with Android 15 QPR2. The channel you should use to get support depends on where
you are encountering your issue.

- **Support for device-specific issues, system issues, and issues with Google
  apps**: Use the Issue Tracker to create new issues and to view and track
  issues that you and other developers have submitted.

  Before creating your own issue, check the known issues listed on this page
  and search the lists of [top open issues](https://developer.android.com/about/versions/15/qpr-top-issues) and
  [recently created issues](https://developer.android.com/about/versions/15/qpr-recent-issues) to see if someone else has already reported it.
  You can subscribe and vote for an issue by clicking **star this issue**
  ![](https://developer.android.com/static/images/shared/star-issue.svg)

  See [Where to report issues](https://developer.android.com/about/versions/15/feedback-qpr#templates) to find an issue template that best matches
  the type of issue that you are encountering.
- **Support for issues with other apps**: Contact the app developer directly.

To discuss issues or ideas with other developers working with the Android 15 QPR
Beta, join the [android_beta community on Reddit](https://developer.android.com/about/versions/15/dev-community).

## Features to test

In addition to other app testing that you do with Android 15 QPR2, we recommend
testing your app with the following features:

### Enable 16 KB mode on a device using developer options

![](https://developer.android.com/static/images/guide/practices/16-kb-dev-option.png)

Toggle the **Boot with 16KB page size** developer
option to boot a device in 16 KB mode.

In QPR versions of Android 15, you can
[use the developer option](https://source.android.com/docs/core/architecture/16kb-page-size/16kb-developer-option#use_16kb_toggle) that's available on certain
devices to boot the device in 16 KB mode and perform on-device testing.
Before using the developer option, go to **Settings \> System \> Software
updates** and apply any updates that are available.

This developer option is available on the following devices:

- Pixel 8 and 8 Pro (with Android 15 QPR1 or higher)

- Pixel 8a (with Android 15 QPR1 or higher)

- Pixel 9, 9 Pro, and 9 Pro XL (with Android 15 QPR2 or higher)

- Pixel 9a (with Android 16 or higher)

For more information about how to prepare your app to support 16 KB page
sizes, see our [Developer's Guide](https://developer.android.com/guide/practices/page-sizes).

### Enable the Linux development environment on device using developer options

Starting with Android 15 QPR1, you can try the experimental [Linux terminal
app](https://android.googlesource.com/platform/packages/modules/Virtualization/+/refs/heads/main/android/TerminalApp/) that's available on select devices. This app provides access
to a Linux terminal environment within a virtual machine (VM).

This developer option is available on the following devices where the
Android Virtualization Framework (AVF) is enabled:

- Pixel 7 and 7a (with Android 15 QPR1 or higher)
- Pixel 8, 8a and 8 Pro (with Android 15 QPR1 or higher)
- Pixel 9, 9 Pro, Pro Fold, and Pro XL (with Android 15 QPR1 or higher)

To launch the terminal app:

1. [Enable developer options](https://developer.android.com/studio/debug/dev-options#enable) on the device, then open the
   Settings app and navigate to **System** \> **Developer options** \> **Linux
   development environment** and toggle the option on.

   ![Developer option for the linux development
   environment](https://developer.android.com/static/images/about/versions/15/linux-dev-option.png)
2. Locate the Terminal app in your app drawer and launch it.

   Upon first launch, the app automatically downloads the necessary Linux
   image.

   ![The interface for the Terminal
   app](https://developer.android.com/static/images/about/versions/15/linux-terminal-app.png)

## Top resolved issues

Android 15 QPR2 Beta 3 resolves the top issues that are described in the
following list and includes fixes for some issues that are not noted here.

### Developer- and user-reported issues

- Fixed issues that could cause a device to restart when making a phone call. ([Issue #379051274](https://issuetracker.google.com/issues/379051274), [Issue #390594506](https://issuetracker.google.com/issues/390594506))
- Fixed an issue where trying to resume an app from the app overview would return to the home screen instead. ([Issue #385017194](https://issuetracker.google.com/issues/385017194))
- Fixed issues where the language picker menu (accessed by long-pressing the spacebar) changed the window, which caused the IME to hide in apps that had set their `softInputMode` to `STATE_ALWAYS_HIDDEN`. ([Issue #388201594](https://issuetracker.google.com/issues/388201594), [Issue #386972825](https://issuetracker.google.com/issues/386972825))
- Fixed an issue that sometimes caused a clicking sound in the background while recording video. ([Issue #385998260](https://issuetracker.google.com/issues/385998260))
- Fixed an issue that caused wireless charging to stop functioning in some cases. ([Issue #379301921](https://issuetracker.google.com/issues/379301921))

### Other resolved issues

- Fixed an issue that could cause devices to crash after starting an exercise on a connected Wear OS device.
- Fixed an issue with null pointer exceptions that sometimes caused the system UI to crash.
- Fixed an issue that caused the Android Beta Feedback app to crash sometimes when submitting a bug report.
- Fixed various other issues that were impacting system stability, connectivity, and interactivity.

## Top open issues

See [top open issues](https://developer.android.com/about/versions/15/qpr-top-issues) for the latest list of top open issues that have been
reported by developers.

## Other known issues

Based on our testing, you might encounter the following issues when using
Android 15 QPR2 Beta 3. These issues are already known, so you don't need to
file additional reports for similar issues.

### Android platform

- The touchscreen doesn't work on Pixel 8 or 8a devices after installing Android 15 QPR2 Beta 3 and booting the device in 16 KB mode. To work around this issue:
  - If you already have a device running Android 15 QPR2 with Beta 2.1 or lower, continue to use the previous builds until a fix is released.
  - If you don't already have a device running Android 15 QPR2 and you want to perform testing in 16 KB mode using Pixel 8 and 8a devices, use a [stable build of Android
    15 QPR1](https://developers.google.com/android/images) instead.

## Previous beta releases

Information about previous preview builds is included in the following sections.
If you're encountering issues, check the lists of previously known issues and
make sure you're using the latest preview build.

### Android 15 QPR2 Beta 2

### Beta 2.1

|---|---|
| **Release date** | January 9, 2025 |
| **Build** | BP11.241121.013 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | December 2024 |
| **Google Play services** | 24.45.32 |

### Beta 2

|---|---|
| **Release date** | December 16, 2024 |
| **Build** | BP11.241121.010 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | December 2024 |
| **Google Play services** | 24.45.32 |

Building on the [initial release of Android 15](https://developer.android.com/about/versions/15), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use. However, review any known issues that
are listed on this page.

Android 15 QPR2 builds on the updates in the initial release of Android 15 and
Android 15 QPR1. This QPR release includes the next round of refinements such as
bug fixes and improvements to stability and performance.

#### Minor updates

The following minor updates were released for Beta 2 before the Beta 3 release:  
**Android 15 QPR2 Beta 2.1 (January 2025)**


This minor update to Android 15 QPR2 Beta 2 includes the following fixes:

- Fixed several issues that sometimes caused a device to freeze, crash, or restart unexpectedly. ([Issue #380500068](https://issuetracker.google.com/issues/380500068), [Issue #381894854](https://issuetracker.google.com/issues/381894854), [Issue #378856187](https://issuetracker.google.com/issues/378856187), [Issue #384447026](https://issuetracker.google.com/issues/384447026), [Issue #384885640](https://issuetracker.google.com/issues/384885640), [Issue #385056337](https://issuetracker.google.com/issues/385056337), [Issue #385126181](https://issuetracker.google.com/issues/385126181))
- Fixed an issue where the Emoji Workshop options opened when selecting wallpapers from other categories in system settings. ([Issue #384629413](https://issuetracker.google.com/issues/384629413))
- Fixed various other issues that were impacting system stability and connectivity.

All eligible devices enrolled in the
[Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to Beta 2.1.
| **Note:** See [top open issues](https://developer.android.com/about/versions/15/top-issues) for the latest list of issues that have been reported by developers and users.

#### Top resolved issues

Android 15 QPR2 Beta 2 resolves the top issues that are described in the
following sections and includes fixes for some issues that are not noted here.

##### Developer- and user-reported issues

- Fixed an issue that prevented the "ANGLE preferences" option from being accessed in developer options. ([Issue #379196574](https://issuetracker.google.com/issues/379196574))
- Fixed an issue that prevented some glucose sensor devices from connecting. ([Issue #378816128](https://issuetracker.google.com/issues/378816128))
- Fixed issues that caused a long delay while selecting options to place a call. ([Issue #379266329](https://issuetracker.google.com/issues/379266329), [Issue #378854091](https://issuetracker.google.com/issues/378854091))
- Fixed an issue that prevented the "Limit to 80%" option in charging optimization settings from being enabled. ([Issue #378800194](https://issuetracker.google.com/issues/378800194))
- Fixed null pointer issues that could cause devices to unexpectedly crash or restart. ([Issue #378856187](https://issuetracker.google.com/issues/378856187), [Issue #381894854](https://issuetracker.google.com/issues/381894854))
- Fixed an issue that sometimes caused Pixel Fold devices to stop responding while unfolded. ([Issue #379387626](https://issuetracker.google.com/issues/379387626))

### Android 15 QPR2 Beta 1

### Beta 1

|---|---|
| **Release date** | November 12, 2024 |
| **Build** | BP11.241025.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | November 2024 |
| **Google Play services** | 24.39.34 |

Building on the [initial release of Android 15](https://developer.android.com/about/versions/15), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use. However, review any known issues that
are listed on this page.

Android 15 QPR2 builds on the updates in the initial release of Android 15 and
Android 15 QPR1. This QPR release includes the next round of refinements such as
bug fixes and improvements to stability and performance.