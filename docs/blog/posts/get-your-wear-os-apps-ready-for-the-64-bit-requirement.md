---
title: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
url: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Get your Wear OS apps ready for the 64-bit requirement

###### 2-min read

![](https://developer.android.com/static/blog/assets/wear_os_64_1de6378905_ZOTQoW.webp) 01 Apr 2026 [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/michael-stillwell)[![](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Lifx.webp)](https://developer.android.com/blog/authors/dimitris-kosmidis)

##### [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell)
\&
[Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis)

64-bit architectures provide performance improvements and a foundation for future innovation, delivering faster and richer experiences for your users. We've supported 64-bit CPUs since Android 5. This aligns Wear OS with recent updates for [Google TV and other form factors](https://android-developers.googleblog.com/2025/08/64-bit-app-compatibility-for-google-tv-android-tv.html), building on the 64-bit requirement first introduced for [mobile](https://android-developers.googleblog.com/2019/01/get-your-apps-ready-for-64-bit.html) in 2019.

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

- **Inspect your APK or app bundle** for native code using the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) in Android Studio.
- **Look for .so files** within the lib folder. For ARM devices, 32-bit libraries are located in lib/armeabi-v7a, while the 64-bit equivalent is lib/arm64-v8a.
- **Ensure parity:** The goal is to ensure that your app runs correctly in a 64-bit-only environment. While specific configurations may vary, for most apps this means that for each native 32-bit architecture you support, you should include the corresponding 64-bit architecture by providing the relevant .so files for both [ABIs](https://developer.android.com/ndk/guides/abis).
- **Upgrade SDKs:** If you only have 32-bit versions of a third-party library or SDK, reach out to the provider for a 64-bit compliant version.

### How to test 64-bit compatibility

The 64-bit version of your app should offer the same quality and feature set as the 32-bit version. The [Wear OS Android Emulator](https://developer.android.com/training/wearables/get-started/emulator) can be used to verify that your app behaves and performs as expected in a 64-bit environment.

**Note:** Since Wear OS apps are [required to target Wear OS 4](https://support.google.com/googleplay/android-developer/answer/11926878) or higher to be submitted to Google Play, you are likely already testing on these newer, 64-bit only images.

When testing, pay attention to [native code loaders](https://support.google.com/googleplay/android-developer/answer/11926878) such as [SoLoader](https://github.com/facebook/SoLoader) or older versions of [OpenSSL](https://developer.android.com/google/play/requirements/64-bit#openssl), which may require updates to function correctly on 64-bit only hardware.

### Next steps

We are announcing this requirement now to give developers a six-month window to bring their apps into compliance before enforcement begins in September 2026. For more detailed guidance on the transition, please refer to our in-depth [documentation on supporting 64-bit architectures](https://developer.android.com/google/play/requirements/64-bit).

This transition marks an exciting step for the future of Wear OS and the benefits that 64-bit compatibility will bring to the ecosystem.

###### Written by:

-

  ## [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/michael-stillwell) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
-

  ## [Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dimitris-kosmidis) ![](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Lifx.webp) ![](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Lifx.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Ataul_Munim_cf0796f68c_r1HY2.webp)](https://developer.android.com/blog/authors/ataul-munim) 02 Jun 2026 02 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Differentiated_Experiences_Strapi_bbe8e7618b_19k3ww.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building Premium Android Experiences at Google I/O '26](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26) At Google I/O '26, we showcased how the latest advancements in the Android ecosystem can help you elevate your app's quality while maximizing development efficiency.

  ###### [Ataul Munim](https://developer.android.com/blog/authors/ataul-munim) •
  3 min read

  - [#Performance](https://developer.android.com/blog/topics/performance)
  - [#Memory](https://developer.android.com/blog/topics/memory)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#Automotive OS](https://developer.android.com/blog/topics/automotive-os)
  - +3 ↩
- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)