---
title: https://developer.android.com/about/versions/16/release-notes-qpr
url: https://developer.android.com/about/versions/16/release-notes-qpr
source: md.txt
---

### Beta 3.1

|---|---|
| **Release date** | August 14, 2025 |
| **Builds** | BP31.250610.009 BP31.250610.009.A1 (Pixel Tablet) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | July 2025 |
| **Google Play services** | 25.20.39 |

### Beta 3

|---|---|
| **Release date** | July 17, 2025 |
| **Builds** | BP31.250610.004 BP31.250610.004.A1 (Pixel 6, 6 Pro) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | July 2025 |
| **Google Play services** | 25.20.39 |

### Beta 2.1

|---|---|
| **Release date** | June 25, 2025 |
| **Build** | BP31.250523.010 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | June 2025 |
| **Google Play services** | 25.18.34 |

### Beta 2

|---|---|
| **Release date** | June 10, 2025 |
| **Build** | BP31.250523.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | May 2025 |
| **Google Play services** | 25.18.34 |

### Beta 1.1

|---|---|
| **Release date** | June 4, 2025 |
| **Build** | BP31.250502.008.A1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | May 2025 |
| **Google Play services** | 25.13.33 |

### Beta 1

|---|---|
| **Release date** | May 20, 2025 |
| **Build** | BP31.250502.008 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | May 2025 |
| **Google Play services** | 25.13.33 |

**Android 16 QPR1 Beta 3.1 (August 2025)**


It includes fixes for:

- Device instability or reboots related to Wi-Fi by improving how the system processes network statistics. ([Issue #433037402](https://issuetracker.google.com/issues/433037402), [Issue #432867183](https://issuetracker.google.com/issues/432867183), [Issue #433418936](https://issuetracker.google.com/issues/433418936), [Issue #432795362](https://issuetracker.google.com/issues/432795362), [Issue #432770117](https://issuetracker.google.com/issues/432770117), [Issue #432699126](https://issuetracker.google.com/issues/432699126), [Issue #435489862](https://issuetracker.google.com/issues/435489862), [Issue #435011484](https://issuetracker.google.com/issues/435011484))
- The Context Hub, a low-power sensor component, would crash due to excessive use of main memory, causing device instability; resolved by optimizing memory allocation and preventing memory leaks. ( [Issue #420999948](https://issuetracker.google.com/issues/420999948), [Issue #426316038](https://issuetracker.google.com/issues/426316038))
- The home screen sometimes lost its bottom row of pinned apps and the search bar, making them inaccessible; this was fixed by adjusting how these elements reappear after screen transitions. ([Issue #428088033](https://issuetracker.google.com/issues/428088033), [Issue #428405658](https://issuetracker.google.com/issues/428405658), [Issue #429817851](https://issuetracker.google.com/issues/429817851))
- Notifications would overlap in the shade, hindering readability, by refining the notification display and dismissal animation logic. ([Issue #421792538](https://issuetracker.google.com/issues/421792538), [Issue #422749237](https://issuetracker.google.com/issues/422749237), [Issue #420418750](https://issuetracker.google.com/issues/420418750), [Issue #428896474](https://issuetracker.google.com/issues/428896474))
- An issue that caused unexpected device restarts. ([Issue #427676713](https://issuetracker.google.com/issues/427676713))
- The Quick Settings UI on unfolded foldable devices appeared clipped or misaligned due to incorrect padding caused by double-counting the camera cutout. ([Issue #419184923](https://issuetracker.google.com/issues/419184923), [Issue #421879049](https://issuetracker.google.com/issues/421879049), [Issue #421810067](https://issuetracker.google.com/issues/421810067), [Issue #423172198](https://issuetracker.google.com/issues/423172198), [Issue #422560004](https://issuetracker.google.com/issues/422560004), [Issue #424116279](https://issuetracker.google.com/issues/424116279))
- An issue that caused devices to unexpectedly reboot. ([Issue #408888279](https://issuetracker.google.com/issues/408888279), [Issue #409949346](https://issuetracker.google.com/issues/409949346), [Issue #409960197](https://issuetracker.google.com/issues/409960197), [Issue #410624610](https://issuetracker.google.com/issues/410624610), [Issue #407373090](https://issuetracker.google.com/issues/407373090), [Issue #430095518](https://issuetracker.google.com/issues/430095518))
- The status bar appearing in the Quick Settings shade was sometimes misaligned with the standard status bar, causing a visual inconsistency. ([Issue #419573315](https://issuetracker.google.com/issues/419573315), [Issue #419134909](https://issuetracker.google.com/issues/419134909), [Issue #432794874](https://issuetracker.google.com/issues/432794874))
- Addressed a system hang or crash, particularly during unlock, caused by the camera's Ambient Light Sensor (ALS) read getting stuck, by implementing a non-blocking method for sensor data retrieval. ([Issue #421870862](https://issuetracker.google.com/issues/421870862), [Issue #420725698](https://issuetracker.google.com/issues/420725698))
- The media player on the lock screen would sometimes disappear or become unresponsive. ([Issue #420517884](https://issuetracker.google.com/issues/420517884))
- An issue where the notification shade displayed a large, growing gap, obscuring notifications, by correcting how notification animations were clipped. ([Issue #421366916](https://issuetracker.google.com/issues/421366916))
- An issue where the media player notification could appear clipped or disappear during device rotation, by improving how its display area is sized and updated in UI transitions. ([Issue #433040374](https://issuetracker.google.com/issues/433040374))
- Video calls initiated from voice calls no longer experience muted audio; a system audio fix now correctly manages sound output during call type transitions. ([Issue #434139133](https://issuetracker.google.com/issues/434139133), [Issue #427060263](https://issuetracker.google.com/issues/427060263), [Issue #438414975](https://issuetracker.google.com/issues/438414975))
- An issue where black translucent bars appeared at the top and bottom of the home screen after exiting full-screen apps by correcting how transient system bar states were cleared. ([Issue #425407737](https://issuetracker.google.com/issues/425407737), [Issue #433929827](https://issuetracker.google.com/issues/433929827))
- An issue that caused the device to unexpectedly crash and restart during an OTA update.
- An issue causing occasional device restarts after system updates.
- Widgets on the home screen sometimes failed to load due to looking for outdated app files.
- Typing occasionally stopped working in apps because internal input system processes could race.
- Device crashes caused by the Context Hub running out of memory.
- Bluetooth crashes and instability caused by an "Unimplemented Packet Type" error have been resolved.
- An issue that could cause phone disconnections or system crashes during calls by resolving a memory corruption bug in audio data buffer handling related to audio playback speed changes.
- A brief screen flicker happened when launching apps from the notification shade.
- A system crash that could occur when using your device's media features, especially when connected to a computer for media transfer, by improving the internal handling of media connection resources.

All eligible devices enrolled in the
[Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to Beta 3.1.

> [!NOTE]
> **Note:** See [top open issues](https://developer.android.com/about/versions/16/top-issues-qpr) for the latest list of issues that have been reported by developers and users.

## About Android 16 QPR1 Beta 3 (July 2025)

Building on the [initial release of Android 16](https://developer.android.com/about/versions/16), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use.

### How to get QPR1 Beta 3

You can install Android 16 QPR1 Beta 3 on any of the following Google Pixel
devices:

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

See [Get Android 16 QPR beta builds](https://developer.android.com/about/versions/16/get-qpr) for details on how to get started.
Note: All eligible devices enrolled in the [Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to Beta 3.

### General advisories

Be aware of these general advisories about the release:

- This release might have various stability, battery, or performance issues.
- For users with accessibility needs, this release might not be appropriate for daily use.
- Some apps might not function as expected when running on this release. This limitation includes Google's apps as well as other apps.
- Android 16 QPR beta builds aren't [Compatibility Test Suite
  (CTS)](https://source.android.com/compatibility/cts/)-approved, but they have passed preliminary testing and provide a stable set of pre-release APIs for developers. Apps that depend on CTS-approved builds or use SafetyNet APIs might not work normally on Android 16 QPR beta builds.

### Get support

Two primary support channels are available to you when developing and testing
with Android 16 QPR1. The channel you should use to get support depends on where
you are encountering your issue.

- **Support for device-specific issues, system issues, and issues with Google
  apps** : Use the Issue Tracker to create new issues and to view and track issues that you and other developers have submitted. Before creating your own issue, check the known issues listed on this page and search the lists of [top open issues](https://developer.android.com/about/versions/16/top-issues-qpr) and [recently created issues](https://developer.android.com/about/versions/16/recent-issues-qpr) to see if someone else has already reported it. You can subscribe and vote for an issue by clicking **star this issue** ![](https://developer.android.com/static/images/shared/star-issue.svg) See [Where to report issues](https://developer.android.com/about/versions/16/feedback-qpr1#templates) to find an issue template that best matches the type of issue that you are encountering.
- **Support for issues with other apps** : Contact the app developer directly. To discuss issues or ideas with other developers working with the Android 16 QPR Beta, join the [android_beta community on Reddit](https://developer.android.com/about/versions/16/dev-community).

## Top resolved issues

Android 16 QPR1 Beta 3 resolves the top issues that are described in the
following list and includes fixes for some issues that are not noted here.

- *An issue around RTOS task list corruption that was causing restarts. ([Issue #420999948](https://issuetracker.google.com/issues/420999948), [Issue #426316038](https://issuetracker.google.com/issues/426316038))*
- *Launcher not completely displaying ([Issue #428088033](https://issuetracker.google.com/issues/428088033), [Issue #428405658](https://issuetracker.google.com/issues/428405658), [Issue #429817851](https://issuetracker.google.com/issues/429817851))*
- *Notification display issues ([Issue #421792538](https://issuetracker.google.com/issues/421792538), [Issue #422749237](https://issuetracker.google.com/issues/422749237), [Issue #420418750](https://issuetracker.google.com/issues/420418750), [Issue #428896474](https://issuetracker.google.com/issues/428896474))*
- *The media player in the notification pulldown fails to fully display and function. ([Issue #419184923](https://issuetracker.google.com/issues/419184923), [Issue #421879049](https://issuetracker.google.com/issues/421879049), [Issue #421810067](https://issuetracker.google.com/issues/421810067), [Issue #423172198](https://issuetracker.google.com/issues/423172198), [Issue #422560004](https://issuetracker.google.com/issues/422560004), [Issue #424116279](https://issuetracker.google.com/issues/424116279))*
- *Full phone restart due to class loader issues ([Issue #427676713](https://issuetracker.google.com/issues/427676713))*
- *Kernel issue causing restarts ([Issue #408888279](https://issuetracker.google.com/issues/408888279), [Issue #409949346](https://issuetracker.google.com/issues/409949346), [Issue #409960197](https://issuetracker.google.com/issues/409960197), [Issue #410624610](https://issuetracker.google.com/issues/410624610), [Issue #407373090](https://issuetracker.google.com/issues/407373090), [Issue #430095518](https://issuetracker.google.com/issues/430095518))*
- *Camera non-functional at startup with black screen ([Issue #421870862](https://issuetracker.google.com/issues/421870862), [Issue #420725698](https://issuetracker.google.com/issues/420725698))*
- *Status bar icons missing corner padding ([Issue #419573315](https://issuetracker.google.com/issues/419573315), [Issue #419134909](https://issuetracker.google.com/issues/419134909))*
- *Notification shade message folding breaks ([Issue #421366916](https://issuetracker.google.com/issues/421366916))*

## Previous beta releases

Information about previous preview builds is included in the following sections.
If you're encountering issues, check the lists of previously known issues and
make sure you're using the latest preview build.

## About Android 16 QPR1 Beta 2 (June 2025)

Building on the [initial release of Android 16](https://developer.android.com/about/versions/16), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use.

Android 16 QPR1 Beta 2 notably contains the developer preview of
[*enhanced desktop windowing on connected
displays*](https://android-developers.googleblog.com/2025/06/developer-preview-enhanced-android-desktop-experiences-connected-displays.html).

## Top resolved issues

Android 16 QPR1 Beta 2 resolves the top issues that are described in the
following list and includes fixes for some issues that are not noted here.

- *Auto dark theme is not working* ([*Issue #394471802*](https://issuetracker.google.com/issues/394471802), [*Issue #419213868*](https://issuetracker.google.com/issues/419213868))
- *Now playing is crashing when selecting a track* ([*Issue #421862329*](https://issuetracker.google.com/issues/421862329))
- *Camera frequently fails to launch* ([*Issue #421870862*](https://issuetracker.google.com/issues/421870862))
- *Shortcuts for newly-downloaded apps aren't automatically added* ([*Issue
  #419320526*](https://issuetracker.google.com/issues/419320526))
- *Home button not working on app list UI* ([*Issue #419256078*](https://issuetracker.google.com/issues/419256078))
- "*More wallpapers" button misaligned in wallpaper settings* ([*Issue
  #419295443*](https://issuetracker.google.com/issues/419295443))
- *Gemini fails to work on the lockscreen* ([*Issue #421276731*](https://issuetracker.google.com/issues/421276731))

**Android 16 QPR1 Beta 2.1 (June 2025)**


This minor update to Android 16 QPR1 Beta 2 includes the following fixes:

- The "Approve" button in the Device Admin settings is transparent and invisible ([Issue #419144521](https://issuetracker.google.com/issues/419144521))
- The lockscreen sound toggle shows as off, but sounds still play ([Issue #423985494](https://issuetracker.google.com/issues/423985494))
- The Android back button intermittently fails to function ([Issue #412691179](https://issuetracker.google.com/issues/412691179), [Issue #417434626](https://issuetracker.google.com/issues/4</li>17434626), [Issue #420283260](https://issuetracker.google.com/issues/420283260))
- Fix for a launcher crash when swiping up from the bottom

All eligible devices enrolled in the
[Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to QPR Beta 2.1.

> [!NOTE]
> **Note:** See [top open issues](https://developer.android.com/about/versions/16/top-issues) for the latest list of issues that have been reported by developers and users.

## About Android 16 QPR1 Beta 1 (May 2025)

Building on the [initial release of Android 16](https://developer.android.com/about/versions/16), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Unlike developer previews and betas for unreleased, major versions of Android,
these builds are suitable for general use.

Android 16 QPR1 includes some of the [Material 3 Expressive changes](https://blog.google/products/android/material-3-expressive-android-wearos-launch/), with
visual refreshes to notifications, quick settings, the lock screen, and the
launcher.
**Android 16 QPR1 Beta 1.1 (June 2025)**


This minor update to Android 16 QPR1 Beta 1 includes the following fixes:

- Fixed an issue where the navigation buttons would become unresponsive in the app drawer or task switcher ([Issue #418395419](https://issuetracker.google.com/issues/418395419))
- Fixed an issue where the progress bar in the media player on the lock screen doesn't reflect the place in media ([Issue #419142109](https://issuetracker.google.com/issues/419142109))
- Fixed a crash when trying to open effects in wallpaper ([Issue #419063857](https://issuetracker.google.com/issues/419063857))
- Fixed an issue where the settings app would crash after trying to open the battery menu ([Issue #419125330](https://issuetracker.google.com/issues/419125330))
- Fixed an issue where the lock screen date could get cut off when using a wide clock style ([Issue #419145518](https://issuetracker.google.com/issues/419145518))
- Fixed an issue where the search button has a different color when scrolling ([Issue #419130323](https://issuetracker.google.com/issues/419130323))
- Fixed an issue where the approve button in Device Admin settings is missing ([Issue #419144521](https://issuetracker.google.com/issues/419144521))
- Fixed an issue where dark album labels appeared in the photo picker when in dark mode, impacting readability ([Issue #419159231](https://issuetracker.google.com/issues/419159231))
- Fixed an issue where the date wasn't appearing on the homescreen
- Fixed a fingerprint authentication failure on a multi-user Android device in certain low-power conditions

All eligible devices enrolled in the
[Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to QPR Beta 1.1.

> [!NOTE]
> **Note:** See [top open issues](https://developer.android.com/about/versions/16/top-issues) for the latest list of issues that have been reported by developers and users.