---
title: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
url: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Trade-in mode on Android 16+

2 min read ![](https://developer.android.com/static/blog/assets/Android_Trade_IN_Mode_Blog_9dc083b903_1DwR2p.webp) 26 Jan 2026 *Trade-in mode: faster assessment of a factory-reset phone or tablet, bypassing setup wizard, a new feature on Android 16 and above.*

### Supporting device longevity

Android is committed to making devices last longer. With device longevity comes device circularity: phones and tablets traded-in and resold. [GSMA reported](https://www.gsma.com/solutions-and-impact/connectivity-for-good/external-affairs/climate-action/rethinking-mobile-phones/) that secondhand phones have around 80-90% lower carbon emissions than new phones. The secondhand device market has grown substantially both in volume and value, a trend projected to continue.

Android 16 and above offers an easy way to access device information on any factory reset phone or tablet via the new `tradeinmode` parameter, accessed via adb commands. This means you can view quality indicators of a phone or tablet, skipping each setup wizard step. Simply connect a phone or tablet with adb, and use `tradeinmode` [commands](https://source.android.com/docs/core/perf/trade-in-mode) to get information about the device.

#### **Trade-in mode: What took minutes, now takes seconds**

**Faster trade-in processing --**By bypassing setup wizard, trade-in mode improves device trade ins. The mode enables immediate access to understand the 'health' of a device, helping everyone along the secondhand value chain check the quality of devices that are wiped. We've already seen significant increases in processing secondhand Android devices!

**Secure evaluation --**To ensure the device information is only accessed in secure situations, the device must 1) be factory reset, 2) not have cellular service, 3) not have connectivity or a connected account, and 4) be running a non-debuggable build.

**Get device health information with one command --** You can view all the below device information with adb command from your workstation `adb shell tradeinmode getstatus`, skipping setup wizard:

- Device information
  - Device IMEI(s)
  - Device serial number
  - Brand
  - Model
  - Manufacturer
  - Device model, e.g., Pixel 9
  - Device brand, e.g., Google
  - Device manufacturer, e.g., Google
  - Device name, e.g., tokay
  - API level to ensure correct OS version, e.g., launch_level : 34
- Battery heath
  - Cycle count
  - Health
  - State, e.g., unknown, good, overheat, dead, over_voltage, unspecified_failure, cold, fair, not_available, inconsistent
  - Battery manufacturing date
  - Date first used
  - Serial number (to help provide indication of genuine parts, if OEM supported)
  - Part status, e.g., replaced, original, unsupported
- Storage
  - Useful lifetime remaining
  - Total capacity
- Screen Part status, e.g., replaced, original, unsupported
- Foldables (number of times devices has been folded and total fold lifespan)
- Moisture intrusion
- UICCS information i.e., Indication if there is an e-SIM or removable SIM and the microchip ID for the SIM slot
- Camera count and location, e.g., 3 cameras on front and 2 on back
- Lock detection for select device locks
- And the list keeps growing! Stay up to date [here](https://source.android.com/docs/core/perf/trade-in-mode).

**Run your own tests --** Trade-in mode enables you to run your own diagnostic commands or applications by entering the evaluation flow using `tradeinmode evaluate`. The device will automatically factory reset on reboot after evaluation mode to ensure nothing remains on the device.

**Ensure the device is running an approved build --** Further, when connected to the internet, with a single command `tradeinmode getstatus --challenge` `*CHALLENGE*` you can test the device's operating system (OS) authenticity, to be sure the device is running a trusted build. If the build passes the test, you can be sure the diagnostics results are coming from a trusted OS.

**There's more** -- You can use commands to factory reset, power off, reboot, reboot directly into trade-in mode, check if trade-in mode is active, revert to the previous mode, and pause tests until system services are ready.

**Want to try it?** Learn more about the [developer steps and commands](https://source.android.com/docs/core/perf/trade-in-mode).
Continue reading
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi.md.txt) 05 Nov 2026 05 Nov 2026 ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in intelligent apps at the Android Developer Summit](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt) In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt) • 4 min read
  - [#Android MCP](https://developer.android.com/blog/topics/android-mcp.md.txt)
  - [#Gemini Nano](https://developer.android.com/blog/topics/gemini-nano.md.txt)
  - [#ML Kit](https://developer.android.com/blog/topics/ml-kit.md.txt)
  - [#Connected Apps](https://developer.android.com/blog/topics/connected-apps.md.txt)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)