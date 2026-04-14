---
title: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
url: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Dynamic App Links: Elevating your Android deep linking

###### 2-min read

![](https://developer.android.com/static/blog/assets/Android_Dynamic_App_Links_Blog_42ba94ce09_GV68O.webp) 20 Oct 2025 [![](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp)](https://developer.android.com/blog/authors/ran-mor) [##### Ran Mor](https://developer.android.com/blog/authors/ran-mor)

###### Senior Product Manager

We're excited to announce the availability of [**Dynamic App Links**](https://developer.android.com/training/app-links/about#dynamic-app-links), a significant leap forward for Android App Links that brings them on par with, and in many ways surpasses, industry standards for deep linking. For too long, Android App Links have been limited in their functionality, but with this launch, we're introducing powerful new features that provide unparalleled control and flexibility for developers.

Since Android 6, App Links has been crucial for delivering a seamless web-to-app user experience. By directing users directly to relevant content within your app, rather than a web browser or mobile-web page, you enhance engagement, boost conversions, and foster greater customer loyalty. Now Dynamic App Links, available on Android 15 and later, makes achieving this even easier and more effective.

## What's New: Functionalities Enabled by Dynamic App Links

The core of these enhancements lies in the **Digital Asset Links JSON file**. Previously, this file was primarily used for basic verification. Now, it's a powerful configuration tool that allows you to specify paths, query parameters, fragments, and exclusions, providing a dynamic and robust deep linking solution.

Here what's new in Dynamic App Links:

### Exclusions support

You can now specify certain paths or sections of a URL that should *not* open your app, even if they would otherwise match your App Link configuration. This is incredibly useful for:

- **Unsupported Content:** Directing users to web content that isn't yet supported within your app.
- **Legacy Content:** Managing old URLs that you no longer want to route to your app.
- **Specific Campaigns:** Temporarily excluding certain links during promotions or tests.

This granular control ensures users always land in the most appropriate experience.

### Query parameters support

With the new **Query parameters** functionality you can define specific parameters that, if present in a URL, will prevent your app from opening. This opens up exciting possibilities for:

- **Dynamic Exclusions:** Quickly turning off app linking for specific scenarios without requiring an app update.
- **A/B Testing:** Directing users to different experiences (app vs. web) based on test parameters.
- **Controlled Rollouts:** Gradually enabling app linking for certain user segments.

### Dynamic updates

Make easier updates to your App Links configuration without needing to update your app. You can now specify the URL paths that your app will handle directly within the Digital Asset Links JSON file that is hosted on your server.

This means you can:

- **Respond quickly to changes:** Adapt your deep linking strategy in real-time without the overhead of a new app release.
- **Reduce development cycles:** Implement and test App Link changes much more efficiently.
- **Maintain agility:** Keep your app's deep linking configuration current with your evolving content and features.

## Why Dynamic App Links?

Android Dynamic App Links are the preferred way to link to content within your app because they offer:

- **Seamless User Experience:** Direct users instantly to the exact content they're looking for, bypassing browser redirects.
- **Improved Engagement:** Keep users within your app, leading to higher engagement and longer session times.
- **Increased Conversions:** Guide users effortlessly through your app's flows, improving the likelihood of desired actions.
- **Enhanced Customer Loyalty:** Deliver a polished and efficient experience that keeps users coming back.

With Dynamic App Links, you now have the tools to build even more powerful and flexible deep linking experiences, ensuring your users always find the content they need, right where they expect it.

We're excited to see what you'll build with Dynamic App Links. [Visit our documentation](https://developer.android.com/training/app-links/about#dynamic-app-links) to start exploring these new features today and elevate your app's deep linking strategy!

###### Written by:

-

  ## [Ran Mor](https://developer.android.com/blog/authors/ran-mor)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/ran-mor) ![](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp) ![](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) 13 Apr 2026 13 Apr 2026 ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Test Multi-Device Interactions with the Android Emulator](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator)

  [arrow_forward](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator) Testing multi-device interactions is now easier than ever with the Android Emulator.

  ###### [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)