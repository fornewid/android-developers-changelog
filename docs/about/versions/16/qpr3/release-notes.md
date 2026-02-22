---
title: https://developer.android.com/about/versions/16/qpr3/release-notes
url: https://developer.android.com/about/versions/16/qpr3/release-notes
source: md.txt
---

### Beta 2.1

|---|---|
| **Release date** | February 10, 2026 |
| **Builds** | CP11.251209.009.A1 CP11.251209.009 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | TBA |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

### Beta 2

|---|---|
| **Release date** | January 14, 2026 |
| **Builds** | CP11.251209.007.A1 CP11.251209.007 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | TBA |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

### Beta 1.1

|---|---|
| **Release date** | December 23, 2025 |
| **Builds** | CP11.251114.007 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-12-05 |
| **Google Play services** | 25.41.31 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

### Beta 1

|---|---|
| **Release date** | December 15, 2025 |
| **Builds** | CP11.251114.006 |
| **Emulator support** | TBA |
| **Security patch level** | 2025-12-05 |
| **Google Play services** | 25.41.31 |
| **API diff** | - [QPR2 Beta 2 → API 36.1](https://developer.android.com/sdk/api_diff/36.1-incr/changes) - [API 36 → API 36.1](https://developer.android.com/sdk/api_diff/36.1/changes) |

## About Android 16 QPR3 Beta 2 (January 2026)


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


Beta 2 addresses a wide range of stability, performance, and usability issues. Key fixes include resolving critical system crashes/device freezes, and correcting battery management issues where devices ignored charging limits or drained excessively. Significant improvements were made to connectivity, specifically addressing slow Wi-Fi speeds and missed calls. The update also resolves UI glitches in the notification shade and app drawer, ensuring smoother navigation and interaction.


It includes fixes for:

<br />

- An issue where the app drawer could become unresponsive when scrolling, which required updates to how UI elements were rendered. ([**Issue #432694128**](https://issuetracker.google.com/issues/432694128), [**Issue #432611971**](https://issuetracker.google.com/issues/432611971), [**Issue #441788998**](https://issuetracker.google.com/issues/441788998), [**Issue #447789653**](https://issuetracker.google.com/issues/447789653), [**Issue #447125065**](https://issuetracker.google.com/issues/447125065), [**Issue #446491462**](https://issuetracker.google.com/issues/446491462), [**Issue #445832419**](https://issuetracker.google.com/issues/445832419), [**Issue #442990958**](https://issuetracker.google.com/issues/442990958), [**Issue #440405179**](https://issuetracker.google.com/issues/440405179), [**Issue #439268737**](https://issuetracker.google.com/issues/439268737), [**Issue #439083159**](https://issuetracker.google.com/issues/439083159), [**Issue #454385069**](https://issuetracker.google.com/issues/454385069), [**Issue #451983469**](https://issuetracker.google.com/issues/451983469), [**Issue #458223724**](https://issuetracker.google.com/issues/458223724), [**Issue #469499984**](https://issuetracker.google.com/issues/469499984))
- Android Auto incorrectly logs extensive screen time, impacting battery life. ([**Issue #441280883**](https://issuetracker.google.com/issues/441280883), [**Issue #447843531**](https://issuetracker.google.com/issues/447843531), [**Issue #447296214**](https://issuetracker.google.com/issues/447296214), [**Issue #449371463**](https://issuetracker.google.com/issues/449371463), [**Issue #452024570**](https://issuetracker.google.com/issues/452024570), [**Issue #454619159**](https://issuetracker.google.com/issues/454619159), [**Issue #451565863**](https://issuetracker.google.com/issues/451565863), [**Issue #457515225**](https://issuetracker.google.com/issues/457515225), [**Issue #454055323**](https://issuetracker.google.com/issues/454055323))
- Graphical glitches and performance degradation when interacting with the notification shade in full-screen or PiP modes by improving display rendering. ([**Issue #462950086**](https://issuetracker.google.com/issues/462950086), [**Issue #459169119**](https://issuetracker.google.com/issues/459169119), [**Issue #459073123**](https://issuetracker.google.com/issues/459073123), [**Issue #457522321**](https://issuetracker.google.com/issues/457522321), [**Issue #456371707**](https://issuetracker.google.com/issues/456371707), [**Issue #470324651**](https://issuetracker.google.com/issues/470324651))
- An excessive battery drain issue occurring overnight by optimizing background process power consumption. ([**Issue #442456513**](https://issuetracker.google.com/issues/442456513), [**Issue #440873210**](https://issuetracker.google.com/issues/440873210), [**Issue #429398132**](https://issuetracker.google.com/issues/429398132), [**Issue #428357521**](https://issuetracker.google.com/issues/428357521), [**Issue #443002505**](https://issuetracker.google.com/issues/443002505), [**Issue #433564015**](https://issuetracker.google.com/issues/433564015), [**Issue #432594266**](https://issuetracker.google.com/issues/432594266), [**Issue #454776512**](https://issuetracker.google.com/issues/454776512), [**Issue #419460613**](https://issuetracker.google.com/issues/419460613))
- An issue where the battery charging limit was not being respected causing devices to charge to 100% instead of the set limit. ([**Issue #451095909**](https://issuetracker.google.com/issues/451095909), [**Issue #448046776**](https://issuetracker.google.com/issues/448046776), [**Issue #448021060**](https://issuetracker.google.com/issues/448021060), [**Issue #456718803**](https://issuetracker.google.com/issues/456718803), [**Issue #454560474**](https://issuetracker.google.com/issues/454560474), [**Issue #432877207**](https://issuetracker.google.com/issues/432877207), [**Issue #429727643**](https://issuetracker.google.com/issues/429727643), [**Issue #466851728**](https://issuetracker.google.com/issues/466851728))
- An issue where users experienced slow internet speeds on Wi-Fi due to a Wi-Fi connection bug. ([**Issue #454437480**](https://issuetracker.google.com/issues/454437480), [**Issue #456981967**](https://issuetracker.google.com/issues/456981967), [**Issue #456958280**](https://issuetracker.google.com/issues/456958280), [**Issue #455498451**](https://issuetracker.google.com/issues/455498451), [**Issue #458441788**](https://issuetracker.google.com/issues/458441788), [**Issue #458304750**](https://issuetracker.google.com/issues/458304750), [**Issue #457361044**](https://issuetracker.google.com/issues/457361044), [**Issue #453997420**](https://issuetracker.google.com/issues/453997420), [**Issue #453365426**](https://issuetracker.google.com/issues/453365426), [**Issue #461005533**](https://issuetracker.google.com/issues/461005533), [**Issue #452712962**](https://issuetracker.google.com/issues/452712962), [**Issue #463807838**](https://issuetracker.google.com/issues/463807838), [**Issue #469473410**](https://issuetracker.google.com/issues/469473410), [**Issue #469356290**](https://issuetracker.google.com/issues/469356290), [**Issue #470068419**](https://issuetracker.google.com/issues/470068419), [**Issue #472337394**](https://issuetracker.google.com/issues/472337394), [**Issue #470030535**](https://issuetracker.google.com/issues/470030535), [**Issue #471294203**](https://issuetracker.google.com/issues/471294203), [**Issue #473365864**](https://issuetracker.google.com/issues/473365864), [**Issue #471432420**](https://issuetracker.google.com/issues/471432420))
- A crash when accessing radio information settings. ([**Issue #470740072**](https://issuetracker.google.com/issues/470740072), [**Issue #470575371**](https://issuetracker.google.com/issues/470575371), [**Issue #471076634**](https://issuetracker.google.com/issues/471076634))
- Users experienced a noticeable delay and lack of feedback when switching audio outputs to speakerphone during calls; this was resolved by improving audio routing logic. ([**Issue #442358468**](https://issuetracker.google.com/issues/442358468), [**Issue #446414653**](https://issuetracker.google.com/issues/446414653), [**Issue #452604183**](https://issuetracker.google.com/issues/452604183), [**Issue #441823037**](https://issuetracker.google.com/issues/441823037), [**Issue #470810688**](https://issuetracker.google.com/issues/470810688))
- A display issue causing screen flickering when waking the device from Always-On Display by updating system webview. ([**Issue #455170051**](https://issuetracker.google.com/issues/455170051), [**Issue #447868121**](https://issuetracker.google.com/issues/447868121), [**Issue #472471563**](https://issuetracker.google.com/issues/472471563))
- An issue where certain apps, including Microsoft applications managed by Intune, were crashing on startup due to a compatibility problem with the Android system that has now been resolved. ([**Issue #470144317**](https://issuetracker.google.com/issues/470144317), [**Issue #470214834**](https://issuetracker.google.com/issues/470214834))
- An issue causing inconsistent or failed wireless charging and slow wired charging by improving the power management system. ([**Issue #440727445**](https://issuetracker.google.com/issues/440727445), [**Issue #440698378**](https://issuetracker.google.com/issues/440698378), [**Issue #441025579**](https://issuetracker.google.com/issues/441025579), [**Issue #440985884**](https://issuetracker.google.com/issues/440985884), [**Issue #440918295**](https://issuetracker.google.com/issues/440918295), [**Issue #440593328**](https://issuetracker.google.com/issues/440593328), [**Issue #441450848**](https://issuetracker.google.com/issues/441450848), [**Issue #441402306**](https://issuetracker.google.com/issues/441402306), [**Issue #441649075**](https://issuetracker.google.com/issues/441649075), [**Issue #443625841**](https://issuetracker.google.com/issues/443625841), [**Issue #444875773**](https://issuetracker.google.com/issues/444875773), [**Issue #445317095**](https://issuetracker.google.com/issues/445317095))
- System crashes that occurred when folding a foldable device with an app open by fixing an issue with activity lifecycle management during device state changes. ([**Issue #471377352**](https://issuetracker.google.com/issues/471377352), [**Issue #471113032**](https://issuetracker.google.com/issues/471113032), [**Issue #470681115**](https://issuetracker.google.com/issues/470681115))

**Android 16 QPR3 Beta 1.1 (December 2025)**


It includes a fix for:

- A change that caused some apps to crash on startup. ([Issue #470144317](https://issuetracker.google.com/issues/470144317), [Issue #470214834](https://issuetracker.google.com/issues/470214834))

All eligible devices enrolled in the
[Android Beta for Pixel program](https://g.co/androidbeta)
will be offered an over-the-air (OTA) update to Beta 1.1.

## About Android 16 QPR3 Beta 1 (December 2025)

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