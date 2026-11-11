---
title: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
url: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
source: md.txt
---

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