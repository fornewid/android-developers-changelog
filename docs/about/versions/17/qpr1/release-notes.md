---
title: https://developer.android.com/about/versions/17/qpr1/release-notes
url: https://developer.android.com/about/versions/17/qpr1/release-notes
source: md.txt
---

### Beta 2

|---|---|
| **Release date** | May 6, 2026 |
| **Builds** | CP31.260423.012.A1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-04-05 |
| **Google Play services** | 26.15.32 |

### Beta 1

|---|---|
| **Release date** | April 22, 2026 |
| **Builds** | CP31.260403.005.A1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-04-05 |
| **Google Play services** | 26.11.36 |

### Android 17 QPR 1 Beta 2 (May 2026)

Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to
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

### Top Issues fixed in Beta 2

- *Resolved an issue where the Terminal app fails to launch, resulting in an unresolvable error pop-up and infinite loading. ([**Issue #501751748**](https://issuetracker.google.com/issues/501751748))*
- *Fixed a display issue where date and weather information overlapped the fingerprint sensor area on the lock screen. ([**Issue #498106709**](https://issuetracker.google.com/issues/498106709))*
- *Terminating a third active call from the head unit incorrectly disconnects an existing conference call participant instead of the intended call. ([**Issue #481492536**](https://issuetracker.google.com/issues/481492536))*
- *Fixed an issue where mobile signal bars incorrectly display as empty or greyed out despite active connectivity, preventing users from accurately gauging their network signal strength. ([**Issue #488358813**](https://issuetracker.google.com/issues/488358813))*
- *Custom themed app icons incorrectly appear enlarged on the homescreen when returning from an application. ([**Issue #453458883**](https://issuetracker.google.com/issues/453458883), [**Issue #452939724**](https://issuetracker.google.com/issues/452939724), [**Issue #473509945**](https://issuetracker.google.com/issues/473509945))*
- *Resolves a bug in the F2FS file system that could result in data corruption or unexpected system instability. ([**Issue #498762380**](https://issuetracker.google.com/issues/498762380))*
- *Fixed a UI issue that caused visual instability or glitches when moving apps in the recent items screen. ([**Issue #485468312**](https://issuetracker.google.com/issues/485468312), [**Issue #496828676**](https://issuetracker.google.com/issues/496828676), [**Issue #498193454**](https://issuetracker.google.com/issues/498193454))*
- *Fixed an issue where navigation bar swipe gestures failed to switch between recent apps. ([**Issue #494847234**](https://issuetracker.google.com/issues/494847234))*
- *Resolved an issue where the Bluetooth tethering toggle would reset to off after device restarts or Bluetooth cycles, requiring users to manually re-enable internet sharing for connected devices. ([**Issue #371660785**](https://issuetracker.google.com/issues/371660785))*

### Top Issues fixed in Beta 1 (April 2026)

- *Fixed a crash in the Default Print Service occurring during low ink conditions that prevents users from completing print jobs. ([**Issue #487545419**](https://issuetracker.google.com/issues/487545419))*
- *The Terminal app triggers an Application Not Responding (ANR) error that results in the application and device becoming unresponsive. ([**Issue #497465940**](https://issuetracker.google.com/issues/497465940))*
- *Resolved an issue where uncontrollable hardware audio processing on the voice communication path caused distortion and phase cancellation in VoIP applications. ([**Issue #494843726**](https://issuetracker.google.com/issues/494843726))*
- *Direct audio output may fail to open on devices using the AIDL audio HAL when playing audio streams longer than five seconds. ([**Issue #372064012**](https://issuetracker.google.com/issues/372064012))*