---
title: https://developer.android.com/blog/posts/raising-the-bar-on-battery-performance-excessive-partial-wake-locks-metric-is-now-out-of-beta
url: https://developer.android.com/blog/posts/raising-the-bar-on-battery-performance-excessive-partial-wake-locks-metric-is-now-out-of-beta
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Raising the bar on battery performance: excessive partial wake locks metric is now out of beta

###### 3-min read

![](https://developer.android.com/static/blog/assets/raising_The_Bar_1e7745ca31_Z29xq01.webp) 10 Nov 2025 3 Authors

##### [Karan Jhavar,](https://developer.android.com/blog/authors/karan-jhavar)
[Dan Brown,](https://developer.android.com/blog/authors/dan-brown)
[Eric Brenner](https://developer.android.com/blog/authors/eric-brenner)

A great user experience is built on a foundation of strong technical performance. We are committed to helping you create stable, responsive, and efficient apps that users love. Excessive battery drain is top of mind for your users, and together, we are taking significant steps to help you build more power-efficient apps.

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
![breakdowns.png](https://developer.android.com/static/blog/assets/breakdowns_54677b84db_ZgUbO5.webp)

*Android vitals will alert you to excessive wake lock issues and provide a table of wake lock tags to P90/ P99 duration to help you identify the source by wake lock name.*

To help you understand your app's partial wake lock usage, we are enhancing the excessive partial wake locks page in Android vitals with a new**wake lock names table.**This table breaks down wake lock sessions by their specific tag names and durations, allowing you to easily identify long wake locks in your local development environment, like Android Studio, for easier debugging. You should investigate any wake locks with P90 or P99 durations above 60 minutes.
![image2-android-vitals-warning.png](https://developer.android.com/static/blog/assets/image2_android_vitals_warning_8d9d20e440_1ja1QH.webp)

2. Excessive wake locks and their impact on Google Play visibility

**If your title exceeds the bad behavior threshold for excessive wake locks, it may be ineligible for some discovery surfaces where users find new apps and games.**

In some cases, we may also show a warning on your store listing to inform users that your app may cause their device's battery to drain faster.
![image3_new.png](https://developer.android.com/static/blog/assets/image3_new_7d3382d9a8_1VXk4r.webp)

*Users may see a warning on your store listing if your app exceeds the bad behavior threshold. Note: The exact text and design are subject to change.*

We know making technical changes to your app's code and how it works can be time consuming, so we are making the metric available for you to diagnose and fix potential issues now, with time before the Store visibility changes begin, **starting from March 1, 2026.**

### 3. What to do next

We encourage you to take the following steps to ensure your app delivers a great experience for users:

1. **Visit** [**Android vitals**](https://play.google.com/console/developers/app/vitals/metrics/overview)**:** Review your app's performance on the new excessive partial wake locks metric. The metric is now visible to all developers whose apps have wake lock sessions.
2. **Discover** [**excessive partial wake locks**](https://play.google.com/console/developers/app/vitals/metrics/details?metric=EXCESSIVE_BACKGROUND_WAKELOCKS&days=28)**:** Use the new wake lock names table to identify excessive partial wake locks.
3. **Consult the documentation:** For detailed guidance on best practices and fixing common issues, please check out our[**technical blog post**](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html), [**technical video**](https://www.youtube.com/watch?v=-6mEvkLOln) and updated [**developer documentation on wake locks**](https://developer.android.com/topic/performance/vitals/excessive-wakelock).

Thank you for your continued partnership in building high-quality, performant experiences that users can rely on every day.

###### Written by:

-

  ## [Karan Jhavar](https://developer.android.com/blog/authors/karan-jhavar)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/karan-jhavar) ![](https://developer.android.com/static/blog/assets/Karan_Jhavar_9fe15fcdd8_ZqeKk7.webp) ![](https://developer.android.com/static/blog/assets/Karan_Jhavar_9fe15fcdd8_ZqeKk7.webp)
-

  ## [Dan Brown](https://developer.android.com/blog/authors/dan-brown)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/dan-brown) ![](https://developer.android.com/static/blog/assets/Dan_Brown_94dcf29eb9_2nDlrF.webp) ![](https://developer.android.com/static/blog/assets/Dan_Brown_94dcf29eb9_2nDlrF.webp)
-

  ## [Eric Brenner](https://developer.android.com/blog/authors/eric-brenner)

  ###### PM Rotator \& Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/eric-brenner) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)