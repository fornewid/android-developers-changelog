---
title: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
url: https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api
source: md.txt
---

[Documentation](https://developer.android.com/blog/categories/documentation)

# Upcoming Changes to the Nearby Connections API

1 min read ![](https://developer.android.com/static/blog/assets/Upcoming_Changes_to_the_Nearby_Connections_API_Strapi_11b1de50e2_K0lSy.webp) 20 Jul 2026 [![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_Z1kCd5W.webp)](https://developer.android.com/blog/authors/wei-wang) [Wei Wang](https://developer.android.com/blog/authors/wei-wang) Engineering Manager, Android BeTo User privacy and transparency are core to the Android experience. To better align with these principles, we are updating the default behavior of the Nearby Connections API regarding how it interacts with device radios.

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
  View profile](https://developer.android.com/blog/authors/wei-wang) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_Z1kCd5W.webp) ![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_Z1kCd5W.webp)
Continue reading
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
- [![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)](https://developer.android.com/blog/authors/chiara-chiappini) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Bring_one_handed_gestures_Strapi_defff06599_Z1FDx9g.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring one-handed gestures to your Wear OS app](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app)

  [arrow_forward](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app) First introduced on Pixel Watch with Wear OS 6.1, one-handed gestures made quick interactions effortless, such as starting and stopping a timer, accepting calls, and controlling media.
  [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#pixel watch](https://developer.android.com/blog/topics/pixel-watch)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)