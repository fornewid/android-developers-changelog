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

- [![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp)](https://developer.android.com/blog/authors/nataraj-k-r) 14 May 2026 14 May 2026 ![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_Z2wOXhv.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha)

  [arrow_forward](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha) Building on this foundation, Jetpack Telecom v1.1.0 brings native-level visibility and convenience to third-party VoIP apps.

  ###### [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 12 May 2026 12 May 2026 ![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_Z2pmmBN.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building for the Intelligence System on Android](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android) Announced today during The Android Show, Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  4 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/Vijaya_Kaza_38a0089092_1sYB49.webp)](https://developer.android.com/blog/authors/vijaya-kaza) 07 May 2026 07 May 2026 ![](https://developer.android.com/static/blog/assets/260429_A_look_ahead_to_2026_Banner_Strapi_2000_x_1000_px_b302a5104a_1L2cA4.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A look ahead: Making it easier and faster to publish safer apps](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps)

  [arrow_forward](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps) The mobile ecosystem is always evolving, bringing both new opportunities and new threats. Through these changes, Android and Google Play remain committed to ensuring that billions of users can continue to enjoy their apps with confidence and developer innovation can thrive.

  ###### [Vijaya Kaza](https://developer.android.com/blog/authors/vijaya-kaza) •
  3 min read

  - [#Android](https://developer.android.com/blog/topics/android)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)