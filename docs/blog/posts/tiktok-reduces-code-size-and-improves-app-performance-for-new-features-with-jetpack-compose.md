---
title: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
url: https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

# TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose

2 min read ![](https://developer.android.com/static/blog/assets/tiktok_Case_Study_ae91bba156_Z1VlEKj.webp) 13 Mar 2026 [![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_Z1TO68U.webp)](https://developer.android.com/blog/authors/ben-trengrove.md.txt)[![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_1XcV4X.webp)](https://developer.android.com/blog/authors/ajesh-pai.md.txt) [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove.md.txt) \& [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai.md.txt) [TikTok](https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically) is a global short-video platform known for its massive user base and innovative features. The team is constantly releasing updates, experiments, and new features for their users. Faced with the challenge of maintaining velocity while managing technical debt, the TikTok Android team turned to [Jetpack Compose](https://developer.android.com/compose).

The team wanted to enable faster, higher-quality iteration of product requirements. By leveraging Compose, the team sought to improve engineering efficiency by writing less code and reducing cognitive load, while also achieving better performance and stability.

### **Streamlining complex UI to accelerate developer productivity**

TikTok pages are often more complex than they appear, containing numerous layered conditional requirements. This complexity often resulted in difficult-to-maintain, sub-optimally structured View hierarchies and excessive View nesting, which caused performance degradation due to an increased number of measure passes.

Compose offered a direct solution to this structural problem.

Furthermore, Compose's [measurement strategy](https://developer.android.com/develop/ui/compose/performance/phases.md.txt) helps reduce [*double taxation*](https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies.md.txt#double), making measure performance easier to optimize.

To improve developer productivity, TikTok's central Design System team provides a component library for teams working on different app features. The team observed that Development in Compose is simple; leveraging small composables is highly effective, while incorporating large UI blocks with conditional logic is both straightforward and has minimal overhead.
![junShenTikTok.png](https://developer.android.com/static/blog/assets/jun_Shen_Tik_Tok_efde1f1625_HLUTh.webp)

### **Building a path forward through strategic migration**

By strategically adopting Jetpack Compose, TikTok was able to stay on top of technical debt, while also continuing to focus on creating great experiences for their users. The ability of Compose to handle conditional logic cleanly and streamline composition allowed the team to **achieve up to a 78% reduction in page loading time on new or fully rewritten pages.** This improvement was 20--30% in smaller cases, and 70--80% for full rewrites and new features. They also were able to **reduce their code size by 58%** ,when compared to the same feature built in Views. The team has further shared a couple of learnings:

TikTok team's overall strategy was to incrementally migrate specific user journeys. This gave them an opportunity to migrate, confirm measurable benefits, then scale to more screens. They started with using Compose to simplify the overall structure in the QR code feature and saw the improvements. The team later expanded the migration to the Login and Sign-up experiences.

The team shared some additional learnings:

While checking performance during migration, the TikTok team found that using many small [ComposeViews](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView.md.txt) to replace elements inside a single [ViewHolder](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder.md.txt), caused composition overhead. They achieved better results by expanding the migration to use one single ComposeView for the entire ViewHolder.

When migrating a Fragment inside ViewPager, which has custom height logic and conditional logic to hide and show ui based on experiments, the performance wasn't impacted. In this case, migrating the ViewPager to Composable performed better than migrating the Fragment.

Jun Shen really likes that Compose "reduces the amount of code required for feature development, improves testability, and accelerates delivery". The team plans to steadily increase Compose adoption, making it their preferred framework in the long term. Jetpack Compose proved to be a powerful solution for improving both their developer experience and production metrics at scale.

### **Get Started with Jetpack Compose**

Learn more about how [Jetpack Compose](https://developer.android.com/compose)can help your team.
Written by:

-

  ## [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-trengrove) ![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_Z1TO68U.webp) ![View Ben Trengrove's profile](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_Z1TO68U.webp)
-

  ## [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ajesh-pai) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_1XcV4X.webp) ![View Ajesh Pai's profile](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_1XcV4X.webp)
Continue reading
- 3 Authors 19 Oct 2026 19 Oct 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Grab_Strapi_2000x1000_STATIC_1_dbb884ce74_22df0m.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [Grab Reduces ANRs by 32% and improves startup time by 35% with R8 and Profile guided optimization](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/grab-r8-profile-guided-optimization-anr-startup-time.md.txt) Grab is Southeast Asia's leading superapp, offering deliveries, mobility, and financial services to millions of users across eight countries through a single app.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai.md.txt), [Nguyen Van Minh](https://developer.android.com/blog/authors/nguyen-van-minh.md.txt), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt) • 5 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Copy_of_ANDDM_TINDER_Strapi_d8536aec8a_1WnFNT.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [Tinder cuts app cold starts by 47% with new R8 Configuration Analyzer](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer.md.txt) Tinder is on a mission to power and inspire real connections by making meeting easy and fun for every new generation of singles.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai.md.txt), [Ulises Uriel Verduzco Díaz](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz.md.txt), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt) • 4 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Donovan McMurray's profile](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_1V0INl.webp)](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) 11 Nov 2026 11 Nov 2026 ![](https://developer.android.com/static/blog/assets/1007_ABL_134_How_Smile_ID_Scaled_Identity_Verification_with_Camera_X_Strapi_788bf73f23_1N5Hb5.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies.md.txt)

  ## [How SmileID Scaled Identity Verification to 18,000+ Android Device Types with CameraX](https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/smileid-camerax-android-identity-verification.md.txt) Identity verification apps for banking and SIM registration require clear, high-resolution face captures to detect spoofing and deepfakes. Capturing frames sharp enough for liveness and anti-spoofing checks, without crashing low-memory devices, is a common challenge for Android camera develope
  [Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray.md.txt) • 4 min read
  - [#Camera X](https://developer.android.com/blog/topics/camera-x.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)