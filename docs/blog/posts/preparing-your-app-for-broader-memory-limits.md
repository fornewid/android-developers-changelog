---
title: https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits
url: https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Preparing your app for broader memory limits

2 min read ![](https://developer.android.com/static/blog/assets/ABL_116_Preparing_your_app_for_expanded_memory_limits_strapi_0aac62fa12_1hkk5a.webp) 19 Aug 2026 [![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)](https://developer.android.com/blog/authors/blair-harmon) [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon) Director of Product Management, Android Platform A great user experience is central to Android's mission, and delivering on that promise requires keeping devices fast, responsive, and reliable. This is why memory optimization is more critical than ever. Across the ecosystem, new devices are maintaining or even decreasing their physical memory capacity in response to memory price increases, yet users continue to expect the same seamless, high-performance app experience.

In Android 17, we [introduced per-app memory limits](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits), starting with Pixel devices, to help protect the overall user experience from applications using excess memory and causing system-wide slowdowns. Over the coming year, an increasing number of manufacturers will leverage the Android per-app memory limits across their portfolio of device RAM configurations from 4GB to 16GB+ devices.**If your app exceeds these limits, it will be slowed down and may be terminated.** Optimizing your app's memory footprint is essential to preventing OS throttling and maintaining a seamless user experience.

In this post, we'll explore how these limits work under the hood, how to measure your memory footprint using new Android vitals metrics, and actionable steps to optimize your app or game.

## Understanding Memory Limits

When your app exceeds its memory budget, Android takes progressive action to protect device responsiveness:

1. **zRAM Swapping** : If your app reaches its allocated limit, the system forces your app's pages into **zRAM** (compressed RAM). While zRAM prevents immediate eviction, compressing and decompressing pages adds CPU overhead, which can result in noticeable UI jank and experience slowdowns.
2. **Process Termination** : If your app continues to increase its memory usage beyond the zRAM threshold, **it will be terminated by the system** . To determine if your app session was impacted by these constraints in the field, you can call [`getDescription()`](https://developer.android.com/reference/android/app/ApplicationExitInfo#getDescription%28%29) within [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo). If the system applied a limit, the exit reason is reported as [`REASON_OTHER`](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_OTHER) and the description string will contain "MemoryLimiter:AnonSwap". You can also leverage [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) using [`TRIGGER_TYPE_ANOMALY`](https://developer.android.com/about/versions/17/features#anomaly-profiling-trigger) to automatically capture heap dumps when the memory limit is reached.

To learn more about per-app memory limits and system enforcement, review the [Android 17 App Memory Limits documentation](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits). To test your application on different device configurations use the [Memory Limiter adb commands](https://developer.android.com/about/versions/17/behavior-changes-all#mem-limit-test).

## Monitoring and Diagnosing Memory Issues

You can't optimize what you can't measure. Identifying memory leaks, excessive heap allocations, and Out-Of-Memory (OOM) crashes across the Android ecosystem requires leveraging complementary monitoring tools:

- **Macro-level health with Android vitals:** For broad, population-level visibility without additional overhead, Google Play Console's Android vitals provides essential metrics like [Memory Usage (Anonymous RSS + swap)](https://developer.android.com/topic/performance/vitals/memory-usage)and [Bitmap Memory Usage](https://developer.android.com/topic/performance/vitals/bitmap-memory-usage). This gives you a clear snapshot of memory distribution across different process states (foreground, background, user-perceived services, and cached) and RAM class ranges, helping you spot memory outliers.
- **Memory Limiter exits \& OOM tracking with Firebase Crashlytics:** To stay informed about severe memory degradation before it impacts your key metrics, [Crashlytics version 20.1.0](https://firebase.google.com/support/release-notes/android#crashlytics_v20-1-0) introduces additional debug data to help you catch, prioritize, and fix Out-Of-Memory exceptions and memory limiter kills. Tracking these events alongside custom logs and key-value metadata gives you immediate context into process status when a memory failure occurs.
- **In-field traces with ProfilingManager:** For teams able to maintain a performance observability framework, the `ProfilingManager` API introduced in Android 15 (API level 35) allows your app to programmatically request and collect detailed memory debug artifacts such as Java heap dumps and heap profiles directly from production devices. You can also trigger heap dump captures based on specific system signals, such as `TRIGGER_TYPE_OOM` and `TRIGGER_TYPE_ANOMALY`.

Read our [documentation](https://developer.android.com/topic/performance/memory#monitor) to learn more about other memory monitoring techniques.

## Summary \& What's Next

With Android broadening per-app memory limits across all RAM classes, now is the time to audit your memory footprint:

1. **Prioritize memory optimizations** : Prevent your app from being impacted by app memory limits by using [best practices](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html).
2. **Monitor memory use** : [Monitor your app's memory behavior](https://developer.android.com/topic/performance/memory#monitor) to detect and resolve anomalous behavior.
3. **Optimize your game** : Follow the [latest guidance for games](https://developer.android.com/games/optimize/memory-overview) and complex multimedia apps to maximize memory savings across process states.

### Helpful Resources \& References

- **Android 17 Behavior Changes** : [App Memory Limits](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits)
- **Android Vitals** : [Memory Usage (RSS + swap metric)](https://developer.android.com/topic/performance/vitals/memory-usage) and [Bitmap Memory Usage](https://developer.android.com/topic/performance/vitals/bitmap-memory-usage)
- **Android Developers Blog** : [Prioritizing memory efficiency steps for Android 17](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html)
- **Developer Guide** : [Manage your app's memory](https://developer.android.com/topic/performance/memory)
- [#App Memory Limits](https://developer.android.com/blog/topics/app-memory-limits)
- [#Android Vitals](https://developer.android.com/blog/topics/android-vitals)
- [#Multi-Process Architecture](https://developer.android.com/blog/topics/multi-process-architecture)
- [#Android 17](https://developer.android.com/blog/topics/android-17)
- [#Performance](https://developer.android.com/blog/topics/performance)
Written by:

-

  ## [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon)

  ###### Director of Product Management

  [read_more
  View profile](https://developer.android.com/blog/authors/blair-harmon) ![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp) ![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)
Continue reading
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 16 Jun 2026 16 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_Hero_White_e4dbee04d8_Z1qQbv3.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android 17 is Here](https://developer.android.com/blog/posts/android-17-is-here)

  [arrow_forward](https://developer.android.com/blog/posts/android-17-is-here) Today we're releasing Android 17 and making it available on most supported Pixel devices. Look for new devices running Android 17 in the coming months.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 13 min read
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
- [![View Ataul Munim's profile](https://developer.android.com/static/blog/assets/Ataul_Munim_cf0796f68c_r1HY2.webp)](https://developer.android.com/blog/authors/ataul-munim) 02 Jun 2026 02 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Differentiated_Experiences_Strapi_bbe8e7618b_19k3ww.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building Premium Android Experiences at Google I/O '26](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26) At Google I/O '26, we showcased how the latest advancements in the Android ecosystem can help you elevate your app's quality while maximizing development efficiency.
  [Ataul Munim](https://developer.android.com/blog/authors/ataul-munim) • 3 min read
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - [#Memory](https://developer.android.com/blog/topics/memory)
  - [#Widgets](https://developer.android.com/blog/topics/widgets)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#Automotive OS](https://developer.android.com/blog/topics/automotive-os)
  - +4 ↩
- [![View Robert Clifford's profile](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)](https://developer.android.com/blog/authors/robert-clifford) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/Redefining_Location_5e4a362604_Z1wl0mf.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Redefining Location Privacy: New Tools and Improvements for Android 17](https://developer.android.com/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17) A pillar of the Android ecosystem is our shared commitment to user trust. As the mobile landscape has evolved, so does our approach to protecting sensitive information.
  [Robert Clifford](https://developer.android.com/blog/authors/robert-clifford) • 3 min read
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)