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

- [![](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 24 Jun 2026 24 Jun 2026 ![](https://developer.android.com/static/blog/assets/Apps_Experience_Play_Blog_Header_2000x1000_8c3a95404a_lYfpd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Expanded billing choice and lower fees on Google Play](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play) At Google Play, we are committed to delivering the best possible experience to users, while ensuring developers have the tools and adaptability to succeed.

  ###### [Paul Feng](https://developer.android.com/blog/authors/paul-feng) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 18 Jun 2026 18 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together) Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1R62M0.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  ###### [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) •
  3 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)