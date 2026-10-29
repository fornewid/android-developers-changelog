---
title: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
url: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

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
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Mesa_de_trabajo_1_copy_8_3f8cf8a935_Z1799P4.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Agentic and Flexible: A next era of Android development](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development)

  [arrow_forward](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development) Today, at the Android Dev Summit, we are announcing the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Rabbit2_Strapi_27563aeaf4_1BAzRM.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Your favorite agents are now integrated in Android Studio](https://developer.android.com/blog/posts/ai-agents-android-studio-integration)

  [arrow_forward](https://developer.android.com/blog/posts/ai-agents-android-studio-integration) Android Studio Rabbit 2 is now stable and ready for you to use in production. This release includes key features to improve your development such as Bring Your Own Agent, new XR Emulator features, a LeakCanary update, a new agent skills manager tool, AI code review, and more.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)](https://developer.android.com/blog/authors/roxanna-walker) 21 Oct 2026 21 Oct 2026 ![](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A more reliable way to add and edit contacts on Android](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)

  [arrow_forward](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android) Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission.
  [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) • 6 min read
  - [#Android](https://developer.android.com/blog/topics/android)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)