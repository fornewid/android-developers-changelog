---
title: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
url: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose

2 min read ![](https://developer.android.com/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp) 13 Mar 2026 [![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](https://developer.android.com/blog/authors/ben-trengrove)[![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](https://developer.android.com/blog/authors/ajesh-pai) [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove) \& [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai) [TikTok](https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically) is a global short-video platform known for its massive user base and innovative features. The team is constantly releasing updates, experiments, and new features for their users. Faced with the challenge of maintaining velocity while managing technical debt, the TikTok Android team turned to [Jetpack Compose](https://developer.android.com/compose).

The team wanted to enable faster, higher-quality iteration of product requirements. By leveraging Compose, the team sought to improve engineering efficiency by writing less code and reducing cognitive load, while also achieving better performance and stability.

### **Streamlining complex UI to accelerate developer productivity**

TikTok pages are often more complex than they appear, containing numerous layered conditional requirements. This complexity often resulted in difficult-to-maintain, sub-optimally structured View hierarchies and excessive View nesting, which caused performance degradation due to an increased number of measure passes.

Compose offered a direct solution to this structural problem.

Furthermore, Compose's [measurement strategy](https://developer.android.com/develop/ui/compose/performance/phases) helps reduce [*double taxation*](https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies#double), making measure performance easier to optimize.

To improve developer productivity, TikTok's central Design System team provides a component library for teams working on different app features. The team observed that Development in Compose is simple; leveraging small composables is highly effective, while incorporating large UI blocks with conditional logic is both straightforward and has minimal overhead.
![junShenTikTok.png](https://developer.android.com/static/blog/assets/jun_Shen_Tik_Tok_efde1f1625_Z2tAtL0.webp)

### **Building a path forward through strategic migration**

By strategically adopting Jetpack Compose, TikTok was able to stay on top of technical debt, while also continuing to focus on creating great experiences for their users. The ability of Compose to handle conditional logic cleanly and streamline composition allowed the team to **achieve up to a 78% reduction in page loading time on new or fully rewritten pages.** This improvement was 20--30% in smaller cases, and 70--80% for full rewrites and new features. They also were able to **reduce their code size by 58%** ,when compared to the same feature built in Views. The team has further shared a couple of learnings:

TikTok team's overall strategy was to incrementally migrate specific user journeys. This gave them an opportunity to migrate, confirm measurable benefits, then scale to more screens. They started with using Compose to simplify the overall structure in the QR code feature and saw the improvements. The team later expanded the migration to the Login and Sign-up experiences.

The team shared some additional learnings:

While checking performance during migration, the TikTok team found that using many small [ComposeViews](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView) to replace elements inside a single [ViewHolder](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder), caused composition overhead. They achieved better results by expanding the migration to use one single ComposeView for the entire ViewHolder.

When migrating a Fragment inside ViewPager, which has custom height logic and conditional logic to hide and show ui based on experiments, the performance wasn't impacted. In this case, migrating the ViewPager to Composable performed better than migrating the Fragment.

Jun Shen really likes that Compose "reduces the amount of code required for feature development, improves testability, and accelerates delivery". The team plans to steadily increase Compose adoption, making it their preferred framework in the long term. Jetpack Compose proved to be a powerful solution for improving both their developer experience and production metrics at scale.

### **Get Started with Jetpack Compose**

Learn more about how [Jetpack Compose](https://developer.android.com/compose)can help your team.
Written by:

-

  ## [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove)

  ###### Developer Relations Engineer

  [read_more View profile](https://developer.android.com/blog/authors/ben-trengrove) ![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp) ![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)
-

  ## [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai)

  ###### Developer Relations Engineer

  [read_more View profile](https://developer.android.com/blog/authors/ajesh-pai) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)
Continue reading
- [![View Jonathan Starup's profile](https://developer.android.com/static/blog/assets/unnamed_10_16ef5ad5c7_Z1s2HD7.webp)](https://developer.android.com/blog/authors/jonathan-starup)[![View Andrei Shikov's profile](https://developer.android.com/static/blog/assets/unnamed_9_1eaaffc6a9_EPI3Y.webp)](https://developer.android.com/blog/authors/andrei-shikov) 27 Jul 2026 27 Jul 2026 ![](https://developer.android.com/static/blog/assets/0707_Faster_Kotlin_coroutines_on_Android_with_R8_Strapi_5b162a2623_ZM78f7.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How R8 made Kotlin Coroutines on Android 2x faster](https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster)

  [arrow_forward](https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster) With the majority of Android apps adopting Kotlin as their main language of choice, kotlinx.coroutines has become a de-facto standard for asynchronous programming. The library offers a well-designed and structured way of managing concurrent flows that is native to Kotlin.
  [Jonathan Starup](https://developer.android.com/blog/authors/jonathan-starup), [Andrei Shikov](https://developer.android.com/blog/authors/andrei-shikov) • 7 min read
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#coroutines](https://developer.android.com/blog/topics/coroutines)
  - +1 ↩
- 3 Authors 08 Jun 2026 08 Jun 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_TITLE_Strapi_b83ae0beee_i9nEs.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Datadog delivers millions of in-depth performance insights with ProfilingManager](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager)

  [arrow_forward](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager) Performance regressions are notoriously hard to reproduce, making regressions a massive bottleneck for mobile developers.
  [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan), [Arti Arutiunov](https://developer.android.com/blog/authors/arti-arutiunov), [Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov) • 4 min read
  - [#Profiling Manager](https://developer.android.com/blog/topics/profiling-manager)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +1 ↩
- [![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) 15 May 2026 15 May 2026 ![](https://developer.android.com/static/blog/assets/cross_device_discovery_to_score_record_Wear_OS_adoption_Strapi_2f9244f1db_Z23QTbE.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How FotMob leveraged cross-device discovery to score record Wear OS adoption](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption)

  [arrow_forward](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption) FotMob recently experienced its largest single-day increase on Wear OS among its installed audience in 5 years, at 2-3x the daily average. The secret? A simple cross-device installation flow that helps users discover their Wear OS app directly from their phone.
  [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)