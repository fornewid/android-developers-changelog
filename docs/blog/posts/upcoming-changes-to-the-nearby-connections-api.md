---
title: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
url: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
source: md.txt
---

[Documentation](https://developer.android.com/blog/categories/documentation.md.txt)

# Upcoming Changes to the Nearby Connections API

1 min read ![](https://developer.android.com/static/blog/assets/Upcoming_Changes_to_the_Nearby_Connections_API_Strapi_11b1de50e2_ZGVCnW.webp) 20 Jul 2026 [![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)](https://developer.android.com/blog/authors/wei-wang.md.txt) [Wei Wang](https://developer.android.com/blog/authors/wei-wang.md.txt) Engineering Manager, Android BeTo User privacy and transparency are core to the Android experience. To better align with these principles, we are updating the default behavior of the Nearby Connections API regarding how it interacts with device radios.

### **What is changing?**

Previously, the Nearby Connections API could automatically toggle Wi-Fi and Bluetooth radios ON to facilitate connections without explicit user intervention. Moving forward, the API will no longer automatically enable these radios for 1P and 3P applications.

### **What this means for developers**

If your app relies on Nearby Connections, you will need to update your implementation to account for these changes:

- **Manual Radio Management:**You must ensure that the necessary radios (Wi-Fi or Bluetooth) are enabled before initiating Nearby Connections tasks.
- **User Notification:**If the required radios are disabled, your app must now inform the user and request that they enable them manually. The API will no longer programmatically turn them on for you.

### **Timing**

These changes are scheduled to take effect in late 2026. We recommend reviewing your connection workflows now to ensure a seamless transition for your users.
Written by:

-

  ## [Wei Wang](https://developer.android.com/blog/authors/wei-wang.md.txt)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/wei-wang) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)
Continue reading
- [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp)](https://developer.android.com/blog/authors/rob-orgiu.md.txt) 31 Aug 2026 31 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_123_Streamline_adaptive_testing_with_emulator_commands_Strapi_0d1336f9a2_1recRz.webp) [Documentation](https://developer.android.com/blog/categories/documentation.md.txt)

  ## [Emulator control for adaptive app development](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development.md.txt) Adaptive app development is fundamental on Android, but making sure everything looks good and every feature works the way it should require multiple tests on multiple devices. Or does it?
  [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu.md.txt) • 2 min read
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)