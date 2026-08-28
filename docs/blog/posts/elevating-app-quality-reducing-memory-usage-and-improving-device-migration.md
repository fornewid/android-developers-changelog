---
title: https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration
url: https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Elevating app quality: Reducing memory usage and improving device migration

4 min read ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) 26 Aug 2026 [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) GM, Google Play Developer \& Monetization Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play. To help you deliver the premium experiences users expect, Google Play is introducing two new quality requirements: one focused on reducing app memory footprint, and another on providing a secure, seamless device migration experience.

First, to help developers navigate industry-wide hardware constraints and Android's broader memory limits, Google Play is establishing new performance thresholds.

Second, as part of our broader commitment to elevate app quality, we are introducing a new onboarding standard to simplify and secure login during device upgrades.

## Reducing app memory usage and optimizing code

The mobile industry is navigating significant hardware supply constraints that are altering device memory availability that over time can negatively impact the user experience. Android is addressing this challenge head-on with [broader memory limits](http://android-developers.googleblog.com/2026/08/app-broader-memory-limits.html) that aim to protect the overall user experience from apps using excess memory and causing system-wide slowdowns.

Building on this, today Google Play is establishing [performance thresholds](https://support.google.com/googleplay/android-developer/answer/17492799) to help developers ensure their apps continue to deliver the premium experience users expect. This includes new thresholds across dynamic memory usage, bitmap usage, and code optimization to prevent unexpected on-device performance throttling and app terminations.

- **Dynamic memory usage (anonymous RSS + swap):**This tracks the memory used for your app's private data storage, including both active and compressed memory. It excludes files stored on the device, such as code or assets. We will assess this usage across different app states (like when your app is in use or running in the background) and device performance categories.
- **Bitmap memory usage:** This evaluates the memory consumed by bitmaps. While bitmaps occupy memory when your app is in the foreground, they should not be held in memory for extended periods of time in non-visible app states such as background and cached.
- **Optimized DEX code:** A well-optimized Android App Bundle uses less memory, starts faster, reduces ANRs, and improves rendering and runtime performance. To ensure an optimized footprint, apps published on Google Play must be [optimized](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) with a minimum of 25% coverage across optimization, shrinking, and obfuscation using a tool such as R8 or any other shrinking tool.

[Review the thresholds and technical details](https://support.google.com/googleplay/android-developer/answer/17492799) to better understand applicability differences specific to apps and games, RAM buckets, and process states.

### **New tools to help you take action**

To enable you to proactively discover, investigate, and optimize your app or game to meet the new bad behavior thresholds, we've already begun rolling out new tools in Play Console to get you started.

- **Deep-dive into new dynamic memory metrics:** Monitor your overall dynamic memory usage (anonymous RSS + swap) and bitmap memory usage directly within [Android vitals](https://play.google.com/console/developers/app/vitals/metrics/overview). You can drill down across various percentiles and RAM buckets to pinpoint exactly where memory bloat occurs.

*New memory metrics in Android vitals to identify and resolve memory bloat*

- **Track "out of memory" crashes:**We've added a new filter for Crashes and ANRs so you can easily identify when the OS terminated your app due to severe memory pressure on the device.
- **Analyze DEX code optimization insights:** For every new [app bundle you upload to Play Console](https://play.google.com/console/developers/app/releases/overview), we now surface detailed optimization insights. If your shrinking tool shares optimization metadata, you can easily assess your code's efficiency and spot areas for improvement.

![image.png](https://developer.android.com/static/blog/assets/image_f034e6877f_PG9eT.webp) Review DEX code optimization insights in Play Console

- **Get proactive performance alerts:** When your app or game exceeds the new [bad behavior thresholds](https://support.google.com/googleplay/android-developer/answer/17492799), we'll provide a warning directly on the Android vitals overview page. You'll also be alerted if we detect unoptimized bitmaps, limited DEX optimization or limited split-bundle usage on [Android vitals](https://play.google.com/console/developers/app/vitals/metrics/overview), helping you squeeze more performance and memory savings.

Later this year, you can expect additional diagnostic tools, including metrics on how long your app spends in each state and deeper insights into the Android [Memory Limiter](http://source.android.com/docs/core/perf/memory-limiter), a feature that prevents individual apps from using too much device memory. Through our ongoing investment in these enhancements, our goal is to help you continuously optimize your footprint and elevate the experience you provide your users.

### **Enforcement timeline**

Starting in February 2027, apps and games must meet their respective [bad behavior thresholds](https://support.google.com/googleplay/android-developer/answer/17492799) for Memory usage (Anonymous RSS + Swap), Bitmap memory usage and [DEX code optimization](https://support.google.com/googleplay/android-developer/answer/17492799#dex_code_optimization). Similar to existing Android vitals metrics, exceeding thresholds is a strong indicator of degraded app experiences and on-device Android app terminations.

Apps and games that do not meet these thresholds may see reduced app visibility and publishing capabilities on Google Play. Additional details will be provided later this year.

Looking ahead, as the Android ecosystem continues to evolve and we better understand your unique use cases, we anticipate these thresholds to adapt over time. Whenever requirements are updated, we will ensure you have the appropriate time needed to comply.

## Providing a secure \& seamless device migration experience

When users switch to a new device, moving their apps over should be secure and effortless. To provide a better onboarding experience, we're introducing a requirement for app developers to make log-ins faster and safer during device transfers.

The [Zero-Tap Sign-In](https://support.google.com/googleplay/android-developer/answer/17492799#zero-tap_sign-in_restoration) standard will require any app supporting user sign-in, optional or mandatory, to automatically restore a user's sign-in state when they move from one Android device to another with the [Android Restore Credentials API](https://developer.android.com/identity/sign-in/restore-credentials). This API ensures that when a user opens your app on their new Android device for the very first time, they are instantly recognized and securely signed in without additional taps.

Starting in April 2027, Google Play will require apps to meet the Zero Tap Sign-In requirement to maintain full publishing capabilities and optimal visibility in the Play Store.

While games are currently exempt from the Zero-Tap Sign-In requirement, developers should expect dedicated guidance and tailored solutions for complex gaming authentication use cases coming in 2027. For games who support single-account sign-in, we strongly encourage usage of the Restore Credentials API to support zero-tap sign-in. Please visit our [help center](https://support.google.com/googleplay/android-developer/answer/17492799#zero-tap_sign-in_restoration) for more information.

## Plan your roadmap: Review Play's requirements

Start preparing for the upcoming enforcement deadlines by reviewing the details of each requirement:

- [Reducing app memory usage and optimizing code](https://support.google.com/googleplay/android-developer/answer/17492799)
- [Providing a secure \& seamless device migration experience](https://support.google.com/googleplay/android-developer/answer/17492799#zero-tap_sign-in_restoration)

Meeting these quality requirements on Google Play is a crucial step toward building a faster, more reliable experience for our users. We appreciate your partnership and everything you do to keep the Android community thriving.
Written by:

-

  ## [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty)

  ###### GM

  [read_more
  View profile](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) ![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp) ![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)
Continue reading
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
- 3 Authors 24 Aug 2026 24 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_1_Strapi_6f49d09922_ZVXnJg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [AAOS SDV - Secure by Design](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design)

  [arrow_forward](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design) At Google, we believe our products should be secure by design, which is why we built the Android Automotive Operating System for Software Defined Vehicle (AAOS SDV) on existing, market-proven platforms, leveraging virtualization technologies like Cuttlefish.
  [Markus Vill](https://developer.android.com/blog/authors/markus-vill), [Sean Keys](https://developer.android.com/blog/authors/sean-keys), [István Nádor](https://developer.android.com/blog/authors/istvan-nador) • 5 min read
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto)
  - [#Security](https://developer.android.com/blog/topics/security)
- [![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)](https://developer.android.com/blog/authors/blair-harmon) 19 Aug 2026 19 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_116_Preparing_your_app_for_expanded_memory_limits_strapi_0aac62fa12_1hkk5a.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Preparing your app for broader memory limits](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits)

  [arrow_forward](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits) A great user experience is central to Android's mission, and delivering on that promise requires keeping devices fast, responsive, and reliable.
  [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon) • 2 min read
  - [#App Memory Limits](https://developer.android.com/blog/topics/app-memory-limits)
  - [#Android Vitals](https://developer.android.com/blog/topics/android-vitals)
  - [#Multi-Process Architecture](https://developer.android.com/blog/topics/multi-process-architecture)
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +3 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)