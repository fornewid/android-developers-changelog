---
title: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
url: https://developer.android.com/blog/posts/trade-in-mode-on-android-16
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Trade-in mode on Android 16+

2-min read ![](https://developer.android.com/static/blog/assets/Android_Trade_IN_Mode_Blog_9dc083b903_Z28Fz7W.webp) 26 Jan 2026 *Trade-in mode: faster assessment of a factory-reset phone or tablet, bypassing setup wizard, a new feature on Android 16 and above.*

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
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 16 Jul 2026 16 Jul 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_ZzldHB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent) Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 3 min read
  - [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
  - [# Quail 2](https://developer.android.com/blog/topics/quail-2)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- [![View Zoe Lopez-Latorre 's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1QyLll.webp)](https://developer.android.com/blog/authors/zoe-lopez-latorre) 08 Jul 2026 08 Jul 2026 ![](https://developer.android.com/static/blog/assets/Bench_July_releas_V01_Strapi_6ee24bdb6b_1NrCN7.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Evolving how LLMs are measured for Android: the next era of Android Bench](https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench)

  [arrow_forward](https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench) Back in March, we introduced Android Bench---our LLM leaderboard for real-world Android development tasks. Since then, we have enhanced the benchmark based on your feedback, including evaluating open-weight models and adding cost and efficiency dimensions to the leaderboard.
  [Zoe Lopez-Latorre](https://developer.android.com/blog/authors/zoe-lopez-latorre) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 24 Jun 2026 24 Jun 2026 ![](https://developer.android.com/static/blog/assets/Apps_Experience_Play_Blog_Header_2000x1000_8c3a95404a_lYfpd.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Expanded billing choice and lower fees on Google Play](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play) At Google Play, we are committed to delivering the best possible experience to users, while ensuring developers have the tools and adaptability to succeed.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 3 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)