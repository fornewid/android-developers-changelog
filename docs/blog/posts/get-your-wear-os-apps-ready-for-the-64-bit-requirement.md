---
title: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
url: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Get your Wear OS apps ready for the 64-bit requirement

2 min read ![](https://developer.android.com/static/blog/assets/wear_os_64_1de6378905_Z2fNN6j.webp) 01 Apr 2026 [![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)](https://developer.android.com/blog/authors/michael-stillwell.md.txt)[![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp)](https://developer.android.com/blog/authors/dimitris-kosmidis.md.txt) [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell.md.txt) \& [Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis.md.txt) 64-bit architectures provide performance improvements and a foundation for future innovation, delivering faster and richer experiences for your users. We've supported 64-bit CPUs since Android 5. This aligns Wear OS with recent updates for [Google TV and other form factors](https://android-developers.googleblog.com/2025/08/64-bit-app-compatibility-for-google-tv-android-tv.html), building on the 64-bit requirement first introduced for [mobile](https://android-developers.googleblog.com/2019/01/get-your-apps-ready-for-64-bit.html) in 2019.

Today, we are extending this 64-bit requirement to Wear OS. This blog provides guidance to help you prepare your apps to meet these new requirements.

### The 64-bit requirement: timeline for Wear OS developers

Starting September 15, 2026:

- All new apps and app updates that include native code will be required to provide 64-bit versions in addition to 32-bit versions when publishing to Google Play.
- Google Play will start blocking the upload of non-compliant apps to the Play Console.

We are not making changes to our policy on 32-bit support, and Google Play will continue to deliver apps to existing 32-bit devices.

The vast majority of Wear OS developers has already made this shift, with 64-bit compliant apps already available. For the remaining apps, we expect the effort to be small.

### Preparing for the 64-bit requirement

Many apps are written entirely in non-native code (i.e. Kotlin or Java) and do not need any code changes. However, it is important to note that even if you do not write native code yourself, a dependency or SDK could be introducing it into your app, so you still need to check whether your app includes native code.

## Assess your app

- **Inspect your APK or app bundle** for native code using the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer.md.txt) in Android Studio.
- **Look for .so files** within the lib folder. For ARM devices, 32-bit libraries are located in lib/armeabi-v7a, while the 64-bit equivalent is lib/arm64-v8a.
- **Ensure parity:** The goal is to ensure that your app runs correctly in a 64-bit-only environment. While specific configurations may vary, for most apps this means that for each native 32-bit architecture you support, you should include the corresponding 64-bit architecture by providing the relevant .so files for both [ABIs](https://developer.android.com/ndk/guides/abis.md.txt).
- **Upgrade SDKs:** If you only have 32-bit versions of a third-party library or SDK, reach out to the provider for a 64-bit compliant version.

### How to test 64-bit compatibility

The 64-bit version of your app should offer the same quality and feature set as the 32-bit version. The [Wear OS Android Emulator](https://developer.android.com/training/wearables/get-started/emulator.md.txt) can be used to verify that your app behaves and performs as expected in a 64-bit environment.

**Note:** Since Wear OS apps are [required to target Wear OS 4](https://support.google.com/googleplay/android-developer/answer/11926878) or higher to be submitted to Google Play, you are likely already testing on these newer, 64-bit only images.

When testing, pay attention to [native code loaders](https://support.google.com/googleplay/android-developer/answer/11926878) such as [SoLoader](https://github.com/facebook/SoLoader) or older versions of [OpenSSL](https://developer.android.com/google/play/requirements/64-bit.md.txt#openssl), which may require updates to function correctly on 64-bit only hardware.

### Next steps

We are announcing this requirement now to give developers a six-month window to bring their apps into compliance before enforcement begins in September 2026. For more detailed guidance on the transition, please refer to our in-depth [documentation on supporting 64-bit architectures](https://developer.android.com/google/play/requirements/64-bit.md.txt).

This transition marks an exciting step for the future of Wear OS and the benefits that 64-bit compatibility will bring to the ecosystem.
Written by:

-

  ## [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/michael-stillwell) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)
-

  ## [Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dimitris-kosmidis) ![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp) ![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp)
Continue reading
- [![View Matthew Forsythe's profile](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_1FlQLe.webp)](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) 19 Nov 2026 19 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_139_Android_developer_verification_Going_global_together_Strapi_01_png_12aa1e5aae_ZkNaef.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Expanding Android developer verification in 2027](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt) After over a year of joint preparation with industry leaders, regional partners, app distributors, and Android communities, our user protections successfully went live on September 30 for participating stores across Brazil, Indonesia, Singapore, and Thailand.
  [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
- [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating apps: New adaptive quality standards on Google Play](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) To give users the premium experience they expect and ensure your apps shine across every screen size, Google Play is introducing new adaptive app quality requirements that go into effect April 2027.
  [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) • 4 min read
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - +1 ↩
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)