---
title: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
url: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
source: md.txt
---

[Documentation](https://developer.android.com/blog/categories/documentation)

# Upcoming Changes to the Nearby Connections API

1 min read ![](https://developer.android.com/static/blog/assets/Upcoming_Changes_to_the_Nearby_Connections_API_Strapi_11b1de50e2_ZGVCnW.webp) 20 Jul 2026 [![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)](https://developer.android.com/blog/authors/wei-wang) [Wei Wang](https://developer.android.com/blog/authors/wei-wang) Engineering Manager, Android BeTo User privacy and transparency are core to the Android experience. To better align with these principles, we are updating the default behavior of the Nearby Connections API regarding how it interacts with device radios.

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

  ## [Wei Wang](https://developer.android.com/blog/authors/wei-wang)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/wei-wang) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_ZCJJeG.webp)
Continue reading
- [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp)](https://developer.android.com/blog/authors/rob-orgiu) 31 Aug 2026 31 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_123_Streamline_adaptive_testing_with_emulator_commands_Strapi_0d1336f9a2_1recRz.webp) [Documentation](https://developer.android.com/blog/categories/documentation)

  ## [Emulator control for adaptive app development](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development)

  [arrow_forward](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development) Adaptive app development is fundamental on Android, but making sure everything looks good and every feature works the way it should require multiple tests on multiple devices. Or does it?
  [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) • 2 min read
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi) 05 Nov 2026 05 Nov 2026 ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [From in-app agents to the Android intelligence system: What's new in intelligent apps at the Android Developer Summit](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads)

  [arrow_forward](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads) In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) • 4 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- [![View Rebecca Gutteridge's profile](https://developer.android.com/static/blog/assets/unnamed_28_42b5e825ea_1MlfGM.webp)](https://developer.android.com/blog/authors/rebecca-gutteridge) 04 Nov 2026 04 Nov 2026 ![](https://developer.android.com/static/blog/assets/ADS_Compose_blog_1_9a0f711253_Z2jewd5.webp) [Events \& Programs](https://developer.android.com/blog/categories/events-and-programs)

  ## [Build for every screen with the latest Jetpack Compose updates from Android Developer Summit](https://developer.android.com/blog/posts/build-for-every-screen-jetpack-compose-updates)

  [arrow_forward](https://developer.android.com/blog/posts/build-for-every-screen-jetpack-compose-updates) The Android ecosystem is a multi-device reality that spans phones, foldables, tablets, wearables, in-car displays, XR, and Googlebook. In this landscape, adaptive development is foundational to reaching users wherever they are.
  [Rebecca Gutteridge](https://developer.android.com/blog/authors/rebecca-gutteridge) • 3 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)