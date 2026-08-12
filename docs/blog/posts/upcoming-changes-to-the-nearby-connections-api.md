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
- [![View Toni Heidenreich's profile](https://developer.android.com/static/blog/assets/profile_picture_6cdbf09ec9_1RLN0R.webp)](https://developer.android.com/blog/authors/toni-heidenreich) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/AFD_ABL_101_Media3_1_11_is_out_Strapi_bebd1c9efc_Z1LP4Os.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Media3 1.11 - What's new?](https://developer.android.com/blog/posts/media3-1-11-whats-new)

  [arrow_forward](https://developer.android.com/blog/posts/media3-1-11-whats-new) Media3 1.11 is out. Powering the vast majority of top Android media apps, this release brings new features, bug fixes, and improvements across playback, editing, and UI components.
  [Toni Heidenreich](https://developer.android.com/blog/authors/toni-heidenreich) • 3 min read
  - [#Media3](https://developer.android.com/blog/topics/media3)
  - [#Jetpack](https://developer.android.com/blog/topics/jetpack)
  - [#ExoPlayer](https://developer.android.com/blog/topics/exo-player)
  - +1 ↩
- [![View Jose Alcérreca's profile](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)](https://developer.android.com/blog/authors/jose-alcerreca) 06 Aug 2026 06 Aug 2026 ![](https://developer.android.com/static/blog/assets/Inside_Android_Skills_Built_for_deprecation_Strapi_V01_8f34b79673_MYo9i.webp) [Community](https://developer.android.com/blog/categories/community)

  ## [Inside Android Skills - Built for deprecation](https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation)

  [arrow_forward](https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation) We released the official Android Skills in April. This blog post covers the feedback we received and explains the philosophy and methodology behind the project.
  [Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca) • 4 min read
  - [#AI-assisted coding](https://developer.android.com/blog/topics/ai-assisted-coding)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 29 Jul 2026 29 Jul 2026 ![](https://developer.android.com/static/blog/assets/Google_Play_Age_Signals_API_Blog_Strapi_d532f6c0b8_Z298Ads.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Delivering safer, age-appropriate experiences on Google Play](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play) Providing a safe online experience and protecting users from harm is a top priority at Google Play.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 2 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)