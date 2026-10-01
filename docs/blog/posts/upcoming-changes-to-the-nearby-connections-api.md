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
- [![View Pavlo Stavytskyi's profile](https://developer.android.com/static/blog/assets/pavlo_a4e2ec12e9_v4xs2.webp)](https://developer.android.com/blog/authors/pavlo-stavytskyi)[![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_Z1XnKqa.webp)](https://developer.android.com/blog/authors/rebecca-franks) 30 Sep 2026 30 Sep 2026 ![](https://developer.android.com/static/blog/assets/Compose_Carousel_Strapi_3_ca1ff69fce_Z1u412n.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How Instagram Direct engineers built AI-native UI architecture with Jetpack Compose and reduced token cost per agent session by 33%](https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct) The team built an AI-native UI codebase that is 50% smaller than the original implementation, while achieving a 35% reduction in AI agent execution time, 32% fewer engineer-agent exchanges, and a 33% reduction in token cost.
  [Pavlo Stavytskyi](https://developer.android.com/blog/authors/pavlo-stavytskyi), [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks) • 11 min read
  - [#Compose-first](https://developer.android.com/blog/topics/compose-first)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- [![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp)](https://developer.android.com/blog/authors/sheenam-mittal) 29 Sep 2026 29 Sep 2026 ![](https://developer.android.com/static/blog/assets/ABL_0137_Strapi_1331188d3a_Z17ea85.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Driving growth on Google Play: The next era of subscriptions](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions)

  [arrow_forward](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions) On Google Play, we are continuously expanding our subscription platform to help you drive growth, adapt to new business models, and meet your users exactly where they are.
  [Sheenam Mittal](https://developer.android.com/blog/authors/sheenam-mittal) • 4 min read
  - [#Google Play subscriptions](https://developer.android.com/blog/topics/google-play-subscriptions)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)