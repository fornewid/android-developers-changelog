---
title: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
url: https://developer.android.com/blog/posts/dynamic-app-links-elevating-your-android-deep-linking
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Dynamic App Links: Elevating your Android deep linking

2 min read ![](https://developer.android.com/static/blog/assets/Android_Dynamic_App_Links_Blog_42ba94ce09_GV68O.webp) 20 Oct 2025 [![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp)](https://developer.android.com/blog/authors/ran-mor) [Ran Mor](https://developer.android.com/blog/authors/ran-mor) Senior Product Manager We're excited to announce the availability of [**Dynamic App Links**](https://developer.android.com/training/app-links/about#dynamic-app-links), a significant leap forward for Android App Links that brings them on par with, and in many ways surpasses, industry standards for deep linking. For too long, Android App Links have been limited in their functionality, but with this launch, we're introducing powerful new features that provide unparalleled control and flexibility for developers.

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
  View profile](https://developer.android.com/blog/authors/ran-mor) ![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp) ![View Ran Mor's profile](https://developer.android.com/static/blog/assets/Ran_Profile_Picture_4af70ee745_20lqjv.webp)
Continue reading
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 29 Jul 2026 29 Jul 2026 ![](https://developer.android.com/static/blog/assets/Google_Play_Age_Signals_API_Blog_Strapi_d532f6c0b8_Z298Ads.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Delivering safer, age-appropriate experiences on Google Play](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play) Providing a safe online experience and protecting users from harm is a top priority at Google Play.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 2 min read
- 3 Authors 28 Jul 2026 28 Jul 2026 ![](https://developer.android.com/static/blog/assets/Jetpack_compose_Strapi_123481f79e_Z1F9b9M.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Celebrating 5 years of Jetpack Compose](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose) Today, we officially celebrate five years since the release of Jetpack Compose 1.0. From version 1.0, announced on July 28th, 2021, to our latest 1.11 release, we've seen the APIs evolve significantly over the years, and we're taking a moment to celebrate.
  [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks), [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/MM_Adaptive_and_device_Meta_18e67bafd8_Z1BKgnT.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Optimize your apps for the next generation of Samsung Galaxy devices](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices)

  [arrow_forward](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices) Today at Galaxy Unpacked, Samsung unveiled its latest lineup of foldable and wearable devices. For developers, this means that the variety of form factors, screen sizes, and device postures your app needs to support is expanding once again.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) • 3 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)