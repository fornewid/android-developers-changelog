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

- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/Paul_Lammertsma_2f7e1baf32_Z28iSTy.webp)](https://developer.android.com/blog/authors/paul-lammertsma) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increasing app discovery and engagement on Google TV](https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv)

  [arrow_forward](https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv) We're excited to share Google TV features and developer tools designed to increase the discoverability of your content and prepare your app for future TV experiences.

  ###### [Paul Lammertsma](https://developer.android.com/blog/authors/paul-lammertsma) •
  4 min read

  - [#Gemini features](https://developer.android.com/blog/topics/gemini-features)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Engage SDK](https://developer.android.com/blog/topics/engage-sdk)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)