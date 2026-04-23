---
title: https://developer.android.com/about/versions/17/qpr1/release-notes
url: https://developer.android.com/about/versions/17/qpr1/release-notes
source: md.txt
---

### Beta 1

|---|---|
| **Release date** | April 22, 2026 |
| **Builds** | CP31.260403.005.A1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-04-05 |
| **Google Play services** | 26.11.36 |

### Android 17 QPR 1 Beta 1 (April 2026)

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

### Top Issues fixed in Beta 1

- *Fixed a crash in the Default Print Service occurring during low ink conditions that prevents users from completing print jobs. ([**Issue #487545419**](https://issuetracker.google.com/issues/487545419))*
- *The Terminal app triggers an Application Not Responding (ANR) error that results in the application and device becoming unresponsive. ([**Issue #497465940**](https://issuetracker.google.com/issues/497465940))*
- *Resolved an issue where uncontrollable hardware audio processing on the voice communication path caused distortion and phase cancellation in VoIP applications. ([**Issue #494843726**](https://issuetracker.google.com/issues/494843726))*
- *Direct audio output may fail to open on devices using the AIDL audio HAL when playing audio streams longer than five seconds. ([**Issue #372064012**](https://issuetracker.google.com/issues/372064012))*