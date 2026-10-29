---
title: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
url: https://developer.android.com/blog/posts/get-your-wear-os-apps-ready-for-the-64-bit-requirement
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Get your Wear OS apps ready for the 64-bit requirement

2 min read ![](https://developer.android.com/static/blog/assets/wear_os_64_1de6378905_Z2fNN6j.webp) 01 Apr 2026 [![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)](https://developer.android.com/blog/authors/michael-stillwell)[![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp)](https://developer.android.com/blog/authors/dimitris-kosmidis) [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell) \& [Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis) 64-bit architectures provide performance improvements and a foundation for future innovation, delivering faster and richer experiences for your users. We've supported 64-bit CPUs since Android 5. This aligns Wear OS with recent updates for [Google TV and other form factors](https://android-developers.googleblog.com/2025/08/64-bit-app-compatibility-for-google-tv-android-tv.html), building on the 64-bit requirement first introduced for [mobile](https://android-developers.googleblog.com/2019/01/get-your-apps-ready-for-64-bit.html) in 2019.

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
Written by:

-

  ## [Michael Stillwell](https://developer.android.com/blog/authors/michael-stillwell)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/michael-stillwell) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)
-

  ## [Dimitris Kosmidis](https://developer.android.com/blog/authors/dimitris-kosmidis)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dimitris-kosmidis) ![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp) ![View Dimitris Kosmidis's profile](https://developer.android.com/static/blog/assets/dimitris_kosmidis_08bb21b8a2_Z2oix8v.webp)
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