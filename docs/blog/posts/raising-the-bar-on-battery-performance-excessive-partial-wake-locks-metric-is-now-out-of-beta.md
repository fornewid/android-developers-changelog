---
title: https://developer.android.com/blog/posts/raising-the-bar-on-battery-performance-excessive-partial-wake-locks-metric-is-now-out-of-beta
url: https://developer.android.com/blog/posts/raising-the-bar-on-battery-performance-excessive-partial-wake-locks-metric-is-now-out-of-beta
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Raising the bar on battery performance: excessive partial wake locks metric is now out of beta

3 min read ![](https://developer.android.com/static/blog/assets/raising_The_Bar_1e7745ca31_1lkMos.webp) 10 Nov 2025 3 Authors [Karan Jhavar,](https://developer.android.com/blog/authors/karan-jhavar.md.txt) [Dan Brown,](https://developer.android.com/blog/authors/dan-brown.md.txt) [Eric Brenner](https://developer.android.com/blog/authors/eric-brenner.md.txt) A great user experience is built on a foundation of strong technical performance. We are committed to helping you create stable, responsive, and efficient apps that users love. Excessive battery drain is top of mind for your users, and together, we are taking significant steps to help you build more power-efficient apps.

Earlier this year, we [introduced a new beta metric](https://android-developers.googleblog.com/2025/04/boost-app-performance-and-battery-life-android-vitals-metrics.html) in Android vitals, **excessive partial wake locks** , to help you identify and address sources of battery drain. This initial beta metric was **co-developed in close collaboration with Samsung**, combining their deep, real-world insights into user experience with battery consumption with Android's platform data.

We want to thank you for providing invaluable feedback during the beta period. **Powered by your input and our continued collaboration with Samsung, we have further refined the algorithm** to be even more accurate and representative. We are excited to announce that this refined metric is now **generally available as a new** [**core vitals metric**](https://developer.android.com/topic/performance/vitals#core-vitals)**to all developers in Android vitals.**

We have defined a **bad behavior threshold** for excessive wake locks. Starting **March 1, 2026,** if your title does not meet this quality threshold, wemay exclude the title from prominent discovery surfaces such as recommendations. In some cases, we may display a warning on your store listing to indicate to users that your app may cause excessive battery drain.

| GOOGLE PLAY'S CORE TECHNICAL QUALITY METRICS To maximize visibility on Google Play, keep your app below the bad behavior thresholds for these metrics. ||
|---|---|
| User-perceived crash rate | The percentage of daily active users who experienced at least one crash that is likely to have been noticeable |
| User-perceived ANR rate | The percentage of daily active users who experienced at least one ANR that is likely to have been noticeable |
| Excessive battery usage | The percentage of watch face sessions where battery usage exceeds 4.44% per hour |
| **New: Excessive partial wake locks** | **The percentage of user sessions where cumulative, non-exempt wake lock usage exceeds 2 hours** |

*Excessive partial wake locks newly join the *[*technical quality bars*](https://developer.android.com/topic/performance/vitals#what_are_the_bad_behavior_thresholds)* that Play expects all titles to maintain for a great user experience*

This is the first in a series of new metrics designed to provide deeper insight into your app's resource utilization, enabling you to improve the experience for your users across the entire Android ecosystem.

### 1. Aligning our definition of excessive wake locks with user expectations

Apps can hold wake locks to prevent the user's device from entering sleep mode, letting the apps perform background work while the screen is off.

We consider a user session **excessive** if it holds more than 2 cumulative hours of non-exempt wake locks in a 24 hour period. These excessive sessions are a heavy contributor to battery drain. A wake lock is exempted if it is a system held wake lock that offers clear user benefits that cannot be further optimized, such as audio playback or user-initiated data transfer.

**The bad behaviour threshold** is crossed when 5% of an app's user sessions over the last 28 days are excessive. If your app exceeds this threshold, you will be alerted directly on your [Android vitals overview page](https://play.google.com/console/developers/app/vitals/metrics/overview). You can read more information about our definition on the [Android Developer pages](https://developer.android.com/topic/performance/vitals/excessive-wakelock).
![breakdowns.png](https://developer.android.com/static/blog/assets/breakdowns_54677b84db_Z1iKx61.webp)

*Android vitals will alert you to excessive wake lock issues and provide a table of wake lock tags to P90/ P99 duration to help you identify the source by wake lock name.*

To help you understand your app's partial wake lock usage, we are enhancing the excessive partial wake locks page in Android vitals with a new**wake lock names table.**This table breaks down wake lock sessions by their specific tag names and durations, allowing you to easily identify long wake locks in your local development environment, like Android Studio, for easier debugging. You should investigate any wake locks with P90 or P99 durations above 60 minutes.
![image2-android-vitals-warning.png](https://developer.android.com/static/blog/assets/image2_android_vitals_warning_8d9d20e440_Z1MYzd6.webp)

2. Excessive wake locks and their impact on Google Play visibility

**If your title exceeds the bad behavior threshold for excessive wake locks, it may be ineligible for some discovery surfaces where users find new apps and games.**

In some cases, we may also show a warning on your store listing to inform users that your app may cause their device's battery to drain faster.
![image3_new.png](https://developer.android.com/static/blog/assets/image3_new_7d3382d9a8_15THxe.webp)

*Users may see a warning on your store listing if your app exceeds the bad behavior threshold. Note: The exact text and design are subject to change.*

We know making technical changes to your app's code and how it works can be time consuming, so we are making the metric available for you to diagnose and fix potential issues now, with time before the Store visibility changes begin, **starting from March 1, 2026.**

### 3. What to do next

We encourage you to take the following steps to ensure your app delivers a great experience for users:

1. **Visit** [**Android vitals**](https://play.google.com/console/developers/app/vitals/metrics/overview)**:** Review your app's performance on the new excessive partial wake locks metric. The metric is now visible to all developers whose apps have wake lock sessions.
2. **Discover** [**excessive partial wake locks**](https://play.google.com/console/developers/app/vitals/metrics/details?metric=EXCESSIVE_BACKGROUND_WAKELOCKS&days=28)**:** Use the new wake lock names table to identify excessive partial wake locks.
3. **Consult the documentation:** For detailed guidance on best practices and fixing common issues, please check out our[**technical blog post**](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html), [**technical video**](https://www.youtube.com/watch?v=-6mEvkLOln) and updated [**developer documentation on wake locks**](https://developer.android.com/topic/performance/vitals/excessive-wakelock).

Thank you for your continued partnership in building high-quality, performant experiences that users can rely on every day.
Written by:

-

  ## [Karan Jhavar](https://developer.android.com/blog/authors/karan-jhavar.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/karan-jhavar) ![View Karan Jhavar's profile](https://developer.android.com/static/blog/assets/Karan_Jhavar_9fe15fcdd8_Z1xiMtl.webp) ![View Karan Jhavar's profile](https://developer.android.com/static/blog/assets/Karan_Jhavar_9fe15fcdd8_Z1xiMtl.webp)
-

  ## [Dan Brown](https://developer.android.com/blog/authors/dan-brown.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dan-brown) ![View Dan Brown's profile](https://developer.android.com/static/blog/assets/Dan_Brown_94dcf29eb9_Z1YFjv0.webp) ![View Dan Brown's profile](https://developer.android.com/static/blog/assets/Dan_Brown_94dcf29eb9_Z1YFjv0.webp)
-

  ## [Eric Brenner](https://developer.android.com/blog/authors/eric-brenner.md.txt)

  ###### PM Rotator \& Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/eric-brenner) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_Z1SMg9h.svg)
Continue reading
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi.md.txt) 05 Nov 2026 05 Nov 2026 ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in intelligent apps at the Android Developer Summit](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt) In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt) • 4 min read
  - [#Android MCP](https://developer.android.com/blog/topics/android-mcp.md.txt)
  - [#Gemini Nano](https://developer.android.com/blog/topics/gemini-nano.md.txt)
  - [#ML Kit](https://developer.android.com/blog/topics/ml-kit.md.txt)
  - [#Connected Apps](https://developer.android.com/blog/topics/connected-apps.md.txt)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)