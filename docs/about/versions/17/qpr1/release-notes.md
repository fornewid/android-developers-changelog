---
title: https://developer.android.com/about/versions/17/qpr1/release-notes
url: https://developer.android.com/about/versions/17/qpr1/release-notes
source: md.txt
---

### Beta 4

|---|---|
| **Release date** | June 10, 2026 |
| **Builds** | CP31.260522.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-05-05 |
| **Google Play services** | 26.18.35 |

### Beta 3

|---|---|
| **Release date** | May 19, 2026 |
| **Builds** | CP31.260508.005 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-05-05 |
| **Google Play services** | 26.15.33 |

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

### Android 17 QPR 1 Beta 4 (June 2026)

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

### Top Issues fixed in Beta 4 (June 2026)

- *An issue where the mouse pointer becomes invisible on external displays when Work profile or FLAG_SECURE applications are active. ([**Issue #446715557**](https://issuetracker.google.com/issues/446715557))*
- *A Settings app crash occurring when launching credential provider settings from a Private Space. ([**Issue #499908921**](https://issuetracker.google.com/issues/499908921))*
- *An issue where screenshot sounds were coupled with the ringer volume, preventing silent captures while maintaining call alerts. ([**Issue #336098340**](https://issuetracker.google.com/issues/336098340))*
- *An issue where video recording at 5x zoom would exhibit frame jumps and jitter during panning. ([**Issue #447867142**](https://issuetracker.google.com/issues/447867142))*
- *An issue where Back Tap gestures failed to trigger on the interactive lock screen. ([**Issue #476775220**](https://issuetracker.google.com/issues/476775220))*
- *A graphics driver regression that caused severe 3D performance drops in OpenGL ES applications on newer hardware. ([**Issue #476585209**](https://issuetracker.google.com/issues/476585209))*
- *A regression where Wireless ADB and local network-dependent apps failed to connect. ([**Issue #506418219**](https://issuetracker.google.com/issues/506418219))*

### Top Issues fixed in Beta 3 (May 2026)

- *A recurring system error in ContextHubClientManager that caused excessive logcat noise when attempting to send messages to unregistered clients. ([**Issue #289721806**](https://issuetracker.google.com/issues/289721806))*
- *Clicking on the* date on at a glance prompts to open the terminal *([**Issue #506101970**](https://issuetracker.google.com/issues/506101970))*
- *Wi-Fi unexpectedly disconnects due to erroneous low-quality detection despite strong signal strength. ([**Issue #494670350**](https://issuetracker.google.com/issues/494670350))*
- *Users experienced frequent crackling or distorted audio during media playback from any source. ([**Issue #482749744**](https://issuetracker.google.com/issues/482749744), [**Issue #471865281**](https://issuetracker.google.com/issues/471865281), [**Issue #485701794**](https://issuetracker.google.com/issues/485701794), [**Issue #489062503**](https://issuetracker.google.com/issues/489062503), [**Issue #494050912**](https://issuetracker.google.com/issues/494050912), [**Issue #494901502**](https://issuetracker.google.com/issues/494901502), [**Issue #493915745**](https://issuetracker.google.com/issues/493915745), [**Issue #458363923**](https://issuetracker.google.com/issues/458363923))*
- *UI elements are partially cut off or positioned off-screen when apps are expanded to full-screen mode. ([**Issue #476830614**](https://issuetracker.google.com/issues/476830614), [**Issue #489452085**](https://issuetracker.google.com/issues/489452085))*
- *Home screen widgets would disappear or become unavailable in the widget picker after a device reboot. ([**Issue #488125748**](https://issuetracker.google.com/issues/488125748), [**Issue #505117543**](https://issuetracker.google.com/issues/505117543), [**Issue #505671079**](https://issuetracker.google.com/issues/505671079), [**Issue #497140330**](https://issuetracker.google.com/issues/497140330), [**Issue #506685943**](https://issuetracker.google.com/issues/506685943), [**Issue #510967059**](https://issuetracker.google.com/issues/510967059))*
- *The mobile data icon incorrectly remains active in the Quick Settings panel after Airplane Mode is enabled. ([**Issue #501368569**](https://issuetracker.google.com/issues/501368569), [**Issue #505757076**](https://issuetracker.google.com/issues/505757076))*

### Top Issues fixed in Beta 2 (May 2026)

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