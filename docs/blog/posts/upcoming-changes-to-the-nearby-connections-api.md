---
title: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
url: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

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
- [![View Breana Tate's profile](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_1PpSPG.webp)](https://developer.android.com/blog/authors/breana-tate.md.txt) 17 Nov 2026 17 Nov 2026 ![](https://developer.android.com/static/blog/assets/1109_ABL_160_Ship_smarter_keep_rules_How_library_providers_can_unblock_app_level_DEX_code_optimization_1_44aba4f3cd_1kr2I.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Ship smarter keep rules: How library providers can unblock app-level DEX code optimization](https://developer.android.com/blog/posts/ship-smarter-keep-rules-unblock-dex-optimization.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/ship-smarter-keep-rules-unblock-dex-optimization.md.txt) As Android app and library developers, we all strive for the same goal: performant apps that provide a smooth user experience. A major part of that involves R8, Android's app optimizer. R8 improves app performance by removing unused code, and optimizing and obfuscating the rest.
  [Breana Tate](https://developer.android.com/blog/authors/breana-tate.md.txt) • 6 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Phalene Gowling's profile](https://developer.android.com/static/blog/assets/Phalene_Gowling_0adca8708d_Z1EF0vK.webp)](https://developer.android.com/blog/authors/phalene-gowling.md.txt)[![View Rejane França's profile](https://developer.android.com/static/blog/assets/unnamed_31_d80d832499_1LWl7t.webp)](https://developer.android.com/blog/authors/rejane-franca.md.txt) 16 Nov 2026 16 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_158_Beyond_the_App_A_bd07c85947_982bv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Beyond the app: Expanding buyer reach across new surfaces with Google Play](https://developer.android.com/blog/posts/beyond-the-app-google-play-buyer-reach.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/beyond-the-app-google-play-buyer-reach.md.txt) Discover how Google Play's channel expansion tools in Play Console expand buyer reach across store, web, and external surfaces while protecting margins.
  [Phalene Gowling](https://developer.android.com/blog/authors/phalene-gowling.md.txt), [Rejane França](https://developer.android.com/blog/authors/rejane-franca.md.txt) • 4 min read
  - [#Monetization](https://developer.android.com/blog/topics/monetization.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)