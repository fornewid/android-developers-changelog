---
title: Get your app on the fast track with Android Performance Spotlight Week!  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/get-your-app-on-the-fast-track-with-android-performance-spotlight-week
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [How-tos](/blog/categories/how-tos)

# Get your app on the fast track with Android Performance Spotlight Week!

###### 3-min read

![](/static/blog/assets/performance_Week9_2c643934fa_p8Pb2.webp)

17

Nov
2025

[![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

[##### Ben Weiss](/blog/authors/ben-weiss)

###### Developer Relations Engineer

When working on new features, app performance often takes a back seat. However, while it's not always top of mind for developers, users can see exactly where your app's performance lags behind. When that new feature takes a long time to load or is slow to render, your users can become frustrated. And unhappy users are more likely to abandon the feature you spent so much time on.

**App performance is a core part of user experience and app quality, and recent studies and research shows that it's highly correlated with increased user satisfaction, higher retention, and better review scores.**

And we're here to help… Welcome to **Android Performance Spotlight Week**! All week long, we're providing you with low-effort, high-impact tools and guidance to get your app on the fast track to better performance. We help you lay the foundation and then dive deeper into helping your app become a better version of itself.

The R8 optimizer and Profile Guided Optimizations are foundational tools to improve overall app performance. And that's why we just released significant improvements to Android Studio tooling for performance and with the [Android Gradle Plugin 9.0](/build/releases/agp-preview) we're introducing new APIs to make it easier for you to do the right thing when configuring the R8 Android app optimizer. Jetpack Compose version 1.10, which is now in [beta](/jetpack/androidx/releases/compose-animation#1.10.0-beta02), ships with several features that improve app rendering performance. In addition to these updates, we're bringing you a refresher on improving app health and performance monitoring. Some of our partners are going to tell their performance improvement stories as well.

**Stay tuned to the blog all week as we'll be updating this post with a digest of all the content released.** We're excited to share these updates and help you improve your app's performance.

Here's a closer look at what we'll be covering:

## Monday: Deliberate performance optimization with R8

*November 17, 2025*

We're kicking off with a deep dive into the R8 optimizer. It's not just about shrinking your app's size, it's about gaining a fundamental understanding of how the R8 optimizer can improve performance in your app and why you should use it right away. We just published the largest overhaul of [new technical guidance](http://d.android.com/r8) to date. The guides cover how to enable, configure and troubleshoot the R8 optimizer. On Monday you'll also see case studies from top partners showing the real-world gains they achieved.

**Read the** [**blog post**](https://android-developers.googleblog.com/2025/11/use-r8-to-shrink-optimize-and-fast.html) **and** [**developer guide**](http://d.android.com/r8)**.**

## Tuesday: Debugging and troubleshooting R8

*November 18, 2025*

We tackle the "Why does my app crash after enabling R8?" question head-on. We know advanced optimization can sometimes reveal edge cases, so we're focusing on [debugging and troubleshooting R8 related issues](/topic/performance/app-optimization/test-and-troubleshoot-the-optimization). We'll show you how to use new features in Android Studio to de-obfuscate stack traces, identify common configuration problems, and implement best practices to get the most out of R8. We want you to feel confident, not just hopeful, when you flip the switch.

**Read the** [**blog post**](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html) **and developer guide on** [**testing**](/topic/performance/app-optimization/test-the-optimization) **and** [**troubleshooting**](/topic/performance/app-optimization/troubleshoot-the-optimization) **R8.**

## Wednesday: Deeper performance considerations

*November 19, 2025*

Mid-week, we explore high-impact performance offerings *beyond* the R8 optimizer. We'll show you how to supercharge your app's startup and interactions using Profile Guided Optimization with [Baseline Profiles](/topic/performance/baselineprofiles/overview) and [Startup Profiles](/topic/performance/baselineprofiles/dex-layout-optimizations).They are ready and proven to deliver another massive boost. We also have exciting news on [Jetpack Compose](/develop/ui/compose/performance) rendering performance improvements. Plus, we'll share how to optimize your app's health by [managing background work effectively](/develop/background-work/background-tasks).

**Read the**[**blog post**](https://android-developers.googleblog.com/2025/11/deeper-performance-considerations.html)**.**

## Thursday: Measure and improve

*November 20, 2025*

It's not an improvement if you can't prove it. Thursday is dedicated to performance measurement. We'll share our complete guide, starting from local measurement and debugging with tools like [Jetpack Macrobenchmark](/topic/performance/benchmarking/macrobenchmark-overview) and the new [UiAutomator API](/training/testing/other-components/ui-automator) to capture jank and startup times, all the way to monitoring your app in the wild. You'll learn about [Play Vitals](https://play.google.com/intl/de/console/about/vitals/) andother new APIsto understand your *real user* performance and quantify your success.

**Read the**[**blog post**](https://android-developers.googleblog.com/2025/11/leveling-guide-for-your-performance.html)**.**

## Friday: Ask Android Live

*November 21, 2025*

We cap off the week with an in-depth, live conversation. This is your chance to talk directly with the engineers and Developer Relations team who build and use these tools every day. We'll have a panel of experts from the **R8 and other performance teams** ready to answer your toughest questions live. Get your questions ready!

**Read the** [**blog post**](https://android-developers.googleblog.com/2025/11/fully-optimized-wrapping-up-performance.html) **and watch the recording of our Ask Android Session.**

---

### 📣 Take the Performance Challenge!

We're not just sharing guidance. We're challenging you to put it into action!

Here's our challenge for you this week: **Enable R8 full mode for your app.**

1. Follow our developer guides to get started: [**Enable app optimization**](/topic/performance/app-optimization/enable-app-optimization).
2. Then, **measure the impact**. Don't just *feel* the difference, *verify* it. Measure your performance gains by using or adapting the code from our [**Macrobenchmark sample app on GitHub**](https://github.com/android/performance-samples/blob/main/MacrobenchmarkSample/macrobenchmark/src/main/kotlin/com/example/macrobenchmark/benchmark/startup/FullyDrawnStartupBenchmark.kt) to measure your startup times before and after.

We're confident you'll see a meaningful improvement in your app's performance.

While you're at it, use the social tags #AskAndroid to bring your questions. Throughout the week our experts are monitoring and answering your questions.

* [#Performance](/blog/topics/performance)
* [#R8](/blog/topics/r8)

###### Written by:

* ## [Ben Weiss](/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/ben-weiss)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)

## Continue reading

* 3
  Authors

  19

  Nov
  2025

  19

  Nov
  2025

  ![](/static/blog/assets/performance_Week11_efe6dd10be_Z1PApe6.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Deeper Performance Considerations](/blog/posts/deeper-performance-considerations)

  [arrow\_forward](/blog/posts/deeper-performance-considerations)

  We're covering Profile Guided Optimization, Jetpack Compose performance improvements and considerations on working behind the scenes.

  ###### [Ben Weiss](/blog/authors/ben-weiss), [Breana Tate](/blog/authors/breana-tate), [Jossi Wolf](/blog/authors/jossi-wolf) • 8 min read
* [![](/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](/blog/authors/adarsh-fernando)[![](/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](/blog/authors/esteban-de-la-canal)

  16

  Apr
  2026

  16

  Apr
  2026

  ![](/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Android CLI: Build Android apps 3x faster using any agent](/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow\_forward](/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](/blog/authors/adarsh-fernando), [Esteban de la Canal](/blog/authors/esteban-de-la-canal) • 4 min read
* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  04

  Mar
  2026

  04

  Mar
  2026

  ![](/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow\_forward](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 8 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)