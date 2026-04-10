---
title: Fully Optimized: Wrapping up Performance Spotlight Week  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/fully-optimized-wrapping-up-performance-spotlight-week
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Events & Programs](/blog/categories/events-and-programs)

# Fully Optimized: Wrapping up Performance Spotlight Week

###### 3-min read

![](/static/blog/assets/performance_Week12_b8eed5b989_2b3WAh.webp)

21

Nov
2025

[![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/sara-hamilton)

##### [Ben Weiss](/blog/authors/ben-weiss) & [Sara Hamilton](/blog/authors/sara-hamilton)

We spent the past week diving deep into sharing best practices and guidance that helps to make Android apps faster, smaller, and more stable. From the foundational powers of the **R8 optimizer** and **Profile Guided Optimizations,** to performance improvements with Jetpack Compose, to a new guide on leveling up your app's performance, we've covered the *low effort, high impact* tools you need to build a performant app.

This post serves as your index and roadmap to revisit these resources whenever you need to optimize. Here are the five key takeaways from our journey together.

## **Use the R8 optimizer to speed up your app**

The single most impactful, low-effort change you can make is fully enabling the **R8 optimizer**. It doesn't just reduce app size; it performs deep, whole-program optimizations to fundamentally rewrite your code for efficiency. Revisit your Keep Rules and get R8 back into your engineering tasks.

Our newly [updated and expanded documentation](http://d.android.com/r8) on the R8 optimizer is here to help.

**Reddit** observed a **40% faster cold startup** and **30% fewer ANR errors** after enabling R8 full mode.

You can read the [full case study on our blog](https://android-developers.googleblog.com/2025/11/how-reddit-used-r8-optimizer-for-high.html).

![image.png](/static/blog/assets/image_6786830a66_ICScn.webp)

Engineers at **Disney+** invest in app performance and are optimizing the app's user experience. Sometimes even seemingly small changes can make a huge impact. While inspecting their R8 configuration, the team found that the `-dontoptimize` flag was being used. After enabling optimizations by removing this flag, the Disney+ team saw significant improvements in their app's performance.

![image.png](/static/blog/assets/image_50bd3a4d41_1kTMqB.webp)

So next time someone asks you what you could do to improve app performance, just link them to this post.

*Read more in our Day 1 blog:*[*Use R8 to shrink, optimize, and fast-track your app*](https://android-developers.googleblog.com/2025/11/use-r8-to-shrink-optimize-and-fast.html)

## **Guiding you to better performance**

[**Baseline Profiles**](/topic/performance/baselineprofiles/overview) effectively remove the need for Just in Time compilation, improving startup speed, scrolling, animation and overall rendering performance. [**Startup Profiles**](/topic/performance/baselineprofiles/dex-layout-optimizations) make app startup more even more lightweight by bringing an intelligent order to your app's classes.dex files.

And to learn more about just how important Baseline Profiles are for app performance, read [**Meta's engineering blog**](https://engineering.fb.com/2025/10/01/android/accelerating-our-android-apps-with-baseline-profiles) where they shared how Baseline Profiles improved various critical performance metrics by **up to 40%** across their apps.

We continue to make Jetpack Compose more performant for you in **Jetpack Compose 1.10.**Features like [pausable composition](/reference/kotlin/androidx/compose/runtime/PausableComposition) and the customizable cache window are crucial for maintaining zero scroll jank when dealing with complex list items.Take a look at the latest [episode](https://www.youtube.com/live/0vMDXa2PluY?si=An6wjXF2A9eVp_-J&t=2968) of #TheAndroidShow where we explain this in more detail.

*Read more in our Wednesday's blog:*[*Deeper Performance Considerations*](https://android-developers.googleblog.com/2025/11/deeper-performance-considerations.html)

## **Measuring performance can be easy as 1, 2, 3**

You can't manage what you don't measure. Our **Performance Leveling Guide** breaks down your measurement journey into five steps, starting with easily available data and building up to advanced local tooling.  
  
Starting at **level 1**, we’ll teach you how to use readily available data from [**Android Vitals**](/topic/performance/vitals), which provides you with field data on ANRs, crashes, and excessive battery usage.

We’ll also teach you how to level up. For example, we’ll demonstrate how to reach **level 3** with local performance testingusing [**Jetpack Macrobenchmark**](/topic/performance/benchmarking/macrobenchmark-overview) and the new [**UiAutomator 2.4 API**](/training/testing/other-components/ui-automator) to accurately measure and verify any change in your app's performance.

*Read more in our Thursday's blog:* **[Link to Thursday's Blog: Leveling Guide for your Performance Journey]**

## **Debugging performance just got an upgrade**

Advanced optimization shouldn't mean unreadable crash reports. New features are designed to help you confidently debug R8 and background work:

**Automatic Logcat Retrace**

Starting in Android Studio Narwhal, stack traces can automatically be de-obfuscated in the Logcat window. This way you can immediately see and debug any crashes in a production-ready build.

**Narrow Keep Rules**

On Tuesday we demystified the Keep Rules needed to fix runtime crashes, emphasizing writing specific, member-level rules over overly-broad wildcards. And because it's an important topic, we made you a video as well.

And with the new lint check for wide Keep Rules, the Android Studio Otter 3 Feature Drop has you covered here as well.

![image.png](/static/blog/assets/image_eff7d19348_1V9VpA.webp)

We also released new guidance on [testing](/topic/performance/app-optimization/test-the-optimization) and [troubleshooting](/topic/performance/app-optimization/troubleshoot-the-optimization) your R8 configuration to help you get the configuration right with confidence.

*Read more in our Tuesday's blog:* [Configure and troubleshoot R8 Keep Rules](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html)

**Background Work**

We shared guidance on debugging common scenarios you may encounter when scheduling tasks with WorkManager.

[Background Task Inspector](/studio/inspect/task) gives you a visual representation and graph view of WorkManager tasks, helping debug why scheduled work is delayed or failed. And our refreshed Background Work documentation [landing page](/develop/background-work) highlights task-specific APIs that are optimized for particular use cases, helping you achieve more reliable execution.

*Read more in our Wednesday's blog:* [Background work performance considerations](https://android-developers.googleblog.com/2025/11/deeper-performance-considerations.html#:~:text=Background%20work%20performance%20considerations)

## **Performance optimization is an ongoing journey**

If you successfully took our challenge to enable R8 full mode this week, your next step is to integrate performance into your product roadmap using the [**App Performance Score**](/topic/performance/app-score). This standardized framework helps you find the highest leverage action items for continuous improvement.

We capped off the week with the **#AskAndroid Live** Q&A session, where engineers answered your toughest questions on R8, Profile Guided Optimizations, and more. If you missed it, look for the replay!

*Thank you for joining us! Now, get building and keep that momentum going.*

###### Written by:

* ## [Ben Weiss](/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/ben-weiss)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)
* ## [Sara Hamilton](/blog/authors/sara-hamilton)

  ###### Product Manager

  [read\_more
  View profile](/blog/authors/sara-hamilton)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

* [![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

  17

  Nov
  2025

  17

  Nov
  2025

  ![](/static/blog/assets/performance_Week10_467f2693b4_2su32q.webp)

  #### [Events & Programs](/blog/categories/events-and-programs)

  ## [Use R8 to shrink, optimize, and fast-track your app](/blog/posts/use-r8-to-shrink-optimize-and-fast-track-your-app)

  [arrow\_forward](/blog/posts/use-r8-to-shrink-optimize-and-fast-track-your-app)

  We're kicking things off with the single most impactful, low-effort change you can make to improve your app's performance: enabling the R8 optimizer in full mode.

  ###### [Ben Weiss](/blog/authors/ben-weiss) • 5 min read
* [![](/static/blog/assets/maru_ahues_7598dede84_Zr7Omv.webp)](/blog/authors/maru-ahues-bouza)

  11

  Mar
  2026

  11

  Mar
  2026

  ![](/static/blog/assets/Google_Play_Level_Up_metadata_banner_2048x1323_33658d545a_ZDM8Sn.webp)

  #### [Events & Programs](/blog/categories/events-and-programs)

  ## [Level Up: Test Sidekick and prepare for upcoming program milestones](/blog/posts/level-up-test-sidekick-and-prepare-for-upcoming-program-milestones)

  [arrow\_forward](/blog/posts/level-up-test-sidekick-and-prepare-for-upcoming-program-milestones)

  Last September, we shared our vision for the future of Google Play Games grounded in a core belief: the best way to drive your game’s success is to deliver a world-class player experience.

  ###### [Maru Ahues Bouza](/blog/authors/maru-ahues-bouza) • 3 min read
* 17

  Feb
  2026

  17

  Feb
  2026

  ![](/static/blog/assets/O_SVD_DAC_Banner_1600x476_4x1_1_21e5678d22_Z2feGk6.webp)

  #### [Events & Programs](/blog/categories/events-and-programs)

  ## [Get ready for Google I/O May 19-20](/blog/posts/get-ready-for-google-io-may)

  [arrow\_forward](/blog/posts/get-ready-for-google-io-may)

  Google I/O is back! Join us online as we share our latest AI breakthroughs and updates in products across the company, from Gemini to Android, Chrome, Cloud, and more.

  ###### 1 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)