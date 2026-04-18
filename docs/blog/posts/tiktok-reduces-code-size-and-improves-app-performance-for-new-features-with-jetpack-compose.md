---
title: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
url: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose

###### 2-min read

![](https://developer.android.com/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp) 13 Mar 2026 [![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](https://developer.android.com/blog/authors/ben-trengrove)[![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](https://developer.android.com/blog/authors/ajesh-pai)

##### [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove)
\&
[Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai)

[TikTok](https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically) is a global short-video platform known for its massive user base and innovative features. The team is constantly releasing updates, experiments, and new features for their users. Faced with the challenge of maintaining velocity while managing technical debt, the TikTok Android team turned to [Jetpack Compose](https://developer.android.com/compose).

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

###### Written by:

-

  ## [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-trengrove) ![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp) ![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)
-

  ## [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ajesh-pai) ![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp) ![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow_forward](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager) In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.

  ###### [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp)](https://developer.android.com/blog/authors/breana-tate) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/whoop2_fcb73fdc54_bqwCk.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How WHOOP decreased excessive partial wake lock sessions by over 90%](https://developer.android.com/blog/posts/how-whoop-decreased-excessive-partial-wake-lock-sessions)

  [arrow_forward](https://developer.android.com/blog/posts/how-whoop-decreased-excessive-partial-wake-lock-sessions) Building an Android app for a wearable means the real work starts when the screen turns off.

  ###### [Breana Tate](https://developer.android.com/blog/authors/breana-tate) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)