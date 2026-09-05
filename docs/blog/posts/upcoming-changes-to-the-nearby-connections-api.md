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
- [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)](https://developer.android.com/blog/authors/rob-orgiu) 31 Aug 2026 31 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_123_Streamline_adaptive_testing_with_emulator_commands_Strapi_0d1336f9a2_do9zK.webp) [Documentation](https://developer.android.com/blog/categories/documentation)

  ## [Emulator control for adaptive app development](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development)

  [arrow_forward](https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development) Adaptive app development is fundamental on Android, but making sure everything looks good and every feature works the way it should require multiple tests on multiple devices. Or does it?
  [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) • 2 min read
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- 3 Authors 27 Aug 2026 27 Aug 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Passkeys_Strapi_2fc9df18a8_Z1oNucg.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys)

  [arrow_forward](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys) WhatsApp is the world's largest messaging platform, serving billions of users globally. It is the default communication tool for people across diverse regions, connecting users through private, reliable, and secure messaging.
  [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang), [Mayank Jain](https://developer.android.com/blog/authors/blog-author) • 8 min read
  - [#Passkeys](https://developer.android.com/blog/topics/passkeys)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)