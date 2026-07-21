---
title: https://developer.android.com/about/versions/17/qpr2/release-notes
url: https://developer.android.com/about/versions/17/qpr2/release-notes
source: md.txt
---

### Beta 1

|---|---|
| **Release date** | July 20, 2026 |
| **Builds** | CP41.260701.005 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-07-05 |
| **Google Play services** | 26.23.34 |

### Android 17 QPR 2 Beta 1 (July 2026)

Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Android 17 QPR2 includes a minor SDK release. This incremental update has no
planned behavior changes, minimizing the need for compatibility testing.
You can the current SDK changes in the
[API diff report](https://developer.android.com/sdk/api_diff/37.1/changes).

### Top Issues fixed in Beta 1 (July 2026)

- *Bluetooth re-pairing fails silently following a remote bond loss. ([**Issue #412524057**](https://issuetracker.google.com/issues/412524057))*
- *Media player controls briefly flashed on the lock screen upon waking the device despite the app's notifications being disabled. ([**Issue #484607701**](https://issuetracker.google.com/issues/484607701))*
- *A system crash causing Pixel devices to unexpectedly reboot when invoking Gemini. ([**Issue #505750489**](https://issuetracker.google.com/issues/505750489))*
- *Initiating a drag-and-drop gesture with multiple fingers caused the source application to stop receiving subsequent touch events. ([**Issue #516836306**](https://issuetracker.google.com/issues/516836306))*
- *Notifications randomly became invisible in the notification shade until a system restart. ([**Issue #526139207**](https://issuetracker.google.com/issues/526139207), [**Issue #522657034**](https://issuetracker.google.com/issues/522657034))*
- *ML-DSA key generation fails with an exception when using the "NONE" string digest instead of the class constant. ([**Issue #525612735**](https://issuetracker.google.com/issues/525612735))*
- *An issue in AccessibilityNodeInfo.toString() where window bounds were incorrectly logged using screen bounds, which caused misleading accessibility debugging data. ([**Issue #520428442**](https://issuetracker.google.com/issues/520428442))*
- *Window-level UI blur effects failed to render and the "Allow window-level blurs" developer toggle reset after rebooting. ([**Issue #527376569**](https://issuetracker.google.com/issues/527376569))*