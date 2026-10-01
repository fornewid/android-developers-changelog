---
title: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
url: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Dynamic App Links: Elevating your Android deep linking

2 min read ![](https://developer.android.com/static/blog/assets/Android_Dynamic_App_Links_Blog_42ba94ce09_FP0fF.webp) 20 Oct 2025 [![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_7ya3A.webp)](https://developer.android.com/blog/authors/ran-mor) [Ran Mor](https://developer.android.com/blog/authors/ran-mor) Senior Product Manager We're excited to announce the availability of [**Dynamic App Links**](https://developer.android.com/training/app-links/about#dynamic-app-links), a significant leap forward for Android App Links that brings them on par with, and in many ways surpasses, industry standards for deep linking. For too long, Android App Links have been limited in their functionality, but with this launch, we're introducing powerful new features that provide unparalleled control and flexibility for developers.

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
Written by:

-

  ## [Ran Mor](https://developer.android.com/blog/authors/ran-mor)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/ran-mor) ![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_7ya3A.webp) ![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_7ya3A.webp)
Continue reading
- [![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp)](https://developer.android.com/blog/authors/sheenam-mittal) 29 Sep 2026 29 Sep 2026 ![](https://developer.android.com/static/blog/assets/ABL_0137_Strapi_1331188d3a_Z17ea85.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Driving growth on Google Play: The next era of subscriptions](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions)

  [arrow_forward](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions) On Google Play, we are continuously expanding our subscription platform to help you drive growth, adapt to new business models, and meet your users exactly where they are.
  [Sheenam Mittal](https://developer.android.com/blog/authors/sheenam-mittal) • 4 min read
  - [#Google Play subscriptions](https://developer.android.com/blog/topics/google-play-subscriptions)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 24 Sep 2026 24 Sep 2026 ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build your way: Use any AI agent of your choice in Android Studio](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio) Last year, Android Studio opened up to any AI model. Today, we're taking the next step by introducing support for your choice of coding agents.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)