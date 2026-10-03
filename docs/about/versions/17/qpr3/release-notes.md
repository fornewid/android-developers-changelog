---
title: https://developer.android.com/about/versions/17/qpr3/release-notes
url: https://developer.android.com/about/versions/17/qpr3/release-notes
source: md.txt
---

### Beta 1

|---|---|
| **Release date** | October 2, 2026 |
| **Builds** | DP11.260918.005 DP11.260918.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.32.34 |

### Android 17 QPR 3 Beta 1 (October 2026)

Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

### Top Issues fixed in Beta 1 (October 2026)

Top issues fixed include:

- *Audio output device cannot be switched while playing audio from apps without active media controls. ([**Issue #259180936**](https://issuetracker.google.com/issues/259180936))*
- *Apps crash when attempting to start a foreground service from a Quick Settings tile. ([**Issue #299506164**](https://issuetracker.google.com/issues/299506164))*
- *Application icons in the app menu display with excessive spacing. ([**Issue #316288379**](https://issuetracker.google.com/issues/316288379), [**Issue #300758716**](https://issuetracker.google.com/issues/300758716))*
- *App previews fail to display in the recent apps screen. ([**Issue #515091621**](https://issuetracker.google.com/issues/515091621))*
- *NFC service crashes with DeadObjectException and stops detecting tags after the initial scan on Android 16. ([**Issue #456078994**](https://issuetracker.google.com/issues/456078994))*
- *Device freezes and becomes unresponsive when unlocking with the fingerprint sensor. ([**Issue #490719716**](https://issuetracker.google.com/issues/490719716), [**Issue #514867650**](https://issuetracker.google.com/issues/514867650), [**Issue #523022829**](https://issuetracker.google.com/issues/523022829))*
- *Device crashes when selecting the require eyes to be open option in Face Unlock settings. ([**Issue #466618368**](https://issuetracker.google.com/issues/466618368), [**Issue #522677686**](https://issuetracker.google.com/issues/522677686))*
- *MediaPlayer crashes when handling non-ASCII audio attribute tags. ([**Issue #552043106**](https://issuetracker.google.com/issues/552043106))*
- *Applications freeze and trigger an Application Not Responding (ANR) error when launched. ([**Issue #484969809**](https://issuetracker.google.com/issues/484969809), [**Issue #475406236**](https://issuetracker.google.com/issues/475406236))*
- *Camera feed is rotated 90 degrees when using video calling apps on an external display in desktop mode. ([**Issue #432390710**](https://issuetracker.google.com/issues/432390710))*
- *User interface issues when navigating back to the home screen from an app. ([**Issue #566639975**](https://issuetracker.google.com/issues/566639975))*
- *Unexpected dot displayed on the Mobile Data icon in Quick Settings. ([**Issue #551150806**](https://issuetracker.google.com/issues/551150806))*
- *Front camera fails to function while screen recording is active. ([**Issue #523313834**](https://issuetracker.google.com/issues/523313834))*
- *Calling apps crash with ForegroundServiceStartNotAllowedException when handling calls immediately after device reboot. ([**Issue #409069722**](https://issuetracker.google.com/issues/409069722))*
- *eSIM profile cannot be enabled and silently reverts to off in Settings. ([**Issue #541436675**](https://issuetracker.google.com/issues/541436675))*
- *Excessive battery drain during idle when Flip to Shh is enabled. ([**Issue #560036427**](https://issuetracker.google.com/issues/560036427))*
- *Settings app crashes when opening battery settings. ([**Issue #554603197**](https://issuetracker.google.com/issues/554603197))*
- *Audio playback stops on active LHDC v5 Bluetooth devices when a second connected device disconnects. ([**Issue #554992287**](https://issuetracker.google.com/issues/554992287))*
- *com.android.phone crash loop and complete loss of cellular service when the modem reports unexpected SIM slot indices. ([**Issue #554049220**](https://issuetracker.google.com/issues/554049220))*
- *Wi-Fi fails to automatically reconnect during background wakes when hardware PNO scans fail or are unsupported. ([**Issue #551970385**](https://issuetracker.google.com/issues/551970385))*