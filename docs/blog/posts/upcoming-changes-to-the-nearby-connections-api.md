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
- [![View Phalene Gowling's profile](https://developer.android.com/static/blog/assets/Phalene_Gowling_0adca8708d_Z1EF0vK.webp)](https://developer.android.com/blog/authors/phalene-gowling.md.txt)[![View Rejane França's profile](https://developer.android.com/static/blog/assets/unnamed_31_d80d832499_1LWl7t.webp)](https://developer.android.com/blog/authors/rejane-franca.md.txt) 16 Nov 2026 16 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_158_Beyond_the_App_A_bd07c85947_982bv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Beyond the app: Expanding buyer reach across new surfaces with Google Play](https://developer.android.com/blog/posts/beyond-the-app-google-play-buyer-reach.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/beyond-the-app-google-play-buyer-reach.md.txt) Discover how Google Play's channel expansion tools in Play Console expand buyer reach across store, web, and external surfaces while protecting margins.
  [Phalene Gowling](https://developer.android.com/blog/authors/phalene-gowling.md.txt), [Rejane França](https://developer.android.com/blog/authors/rejane-franca.md.txt) • 4 min read
  - [#Monetization](https://developer.android.com/blog/topics/monetization.md.txt)
- [![View Donovan McMurray's profile](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_1V0INl.webp)](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) 11 Nov 2026 11 Nov 2026 ![](https://developer.android.com/static/blog/assets/1007_ABL_134_How_Smile_ID_Scaled_Identity_Verification_with_Camera_X_Strapi_788bf73f23_1N5Hb5.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [How SmileID Scaled Identity Verification to 18,000+ Android Device Types with CameraX](https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification.md.txt) Identity verification apps for banking and SIM registration require clear, high-resolution face captures to detect spoofing and deepfakes. Capturing frames sharp enough for liveness and anti-spoofing checks, without crashing low-memory devices, is a common challenge for Android camera develope
  [Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) • 4 min read
  - [#Camera X](https://developer.android.com/blog/topics/camera-x.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)