---
title: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
url: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Trade-in mode on Android 16+

###### 2-min read

![](https://developer.android.com/static/blog/assets/Android_Trade_IN_Mode_Blog_9dc083b903_Z28Fz7W.webp) 26 Jan 2026 *Trade-in mode: faster assessment of a factory-reset phone or tablet, bypassing setup wizard, a new feature on Android 16 and above.*

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

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 18 Jun 2026 18 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together) Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_D_Android_XR_Strapi_39d27725e6_Zhwmdd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  ###### [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) •
  3 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)
- [![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp)](https://developer.android.com/blog/authors/simona-milanovic) 09 Jun 2026 09 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Dev_Productivity_Strapi_b7e79722e6_45umk.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top 3 updates for Android developer productivity](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity)

  [arrow_forward](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity) Every year, Google I/O brings new announcements and resources across ecosystems and products, including Android development. As development shifts toward AI and agent-assisted tooling, we've expanded our offerings to better support you, however you decide to build for Android.

  ###### [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)