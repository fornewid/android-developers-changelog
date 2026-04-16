---
title: https://developer.android.com/blog/posts/how-reddit-used-the-r8-optimizer-for-high-impact-performance-improvements
url: https://developer.android.com/blog/posts/how-reddit-used-the-r8-optimizer-for-high-impact-performance-improvements
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# How Reddit used the R8 optimizer for high impact performance improvements

###### 4-min read

![](https://developer.android.com/static/blog/assets/REDDIT_casestudy01_1_f3fc4706f3_ZQQjCi.webp) 17 Nov 2025 [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) [##### Ben Weiss](https://developer.android.com/blog/authors/ben-weiss)

###### Developer Relations Engineer

In today's world of mobile applications, a seamless user experience is not just a feature---it's a necessity. Slow load times, unresponsive interfaces, and instability can be significant barriers to user engagement and retention. During their work with the Android Developer Relations team, the engineering team at [Reddit](https://play.google.com/store/apps/details?id=com.reddit.frontpage) used the [App Performance Score](https://developer.android.com/topic/performance/app-score) to evaluate their app. After assessing their performance, they identified significant improvement potential and decided to take the steps to enable the full power of [R8, the Android app optimizer](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization). This focused initiative led to remarkable improvements in startup times, reductions in slow or frozen frames and ANRs, and an overall increase in Play Store ratings. This case study breaks down how Reddit achieved these impressive results.

## **How the R8 Optimizer helped Reddit**

The R8 Optimizer is a foundational tool for performance optimization on Android. It takes various steps to improve app performance.Let's take a quick look at the most impactful ones.

- **Tree shaking** is the most important step to reduce an app's size. Here, unused code from app dependencies and the app itself is removed.
- **Method inlining** replaces method calls with the actual code, making the app more performant.
- **Class merging**, and other strategies are applied to make the code more compact. At this point it's not about human readability of source code any more, but making compiled code work fast. So abstractions, such as interfaces or class hierarchies don't matter here and will be removed.
- **Identifier minification** changes the names of classes, fields, and methods to shorter, meaningless names. So instead of `MyDataModel` you might end up with a class called a.
- **Resource shrinking**removes unused resources such as xml files and drawables to further reduce app size.

![image.png](https://developer.android.com/static/blog/assets/image_b659849bba_ZGIfFG.webp)

*Main stages of R8 Optimization*

## **From hard data to user satisfaction: Identifying success in production**

Reddit saw improved performance results immediately after a new version of the app was rolled out to users. By using [**Android Vitals**](https://developer.android.com/topic/performance/vitals) and [**Crashlytics**](https://firebase.google.com/docs/crashlytics), Reddit was able to capture performance metrics on real devices with actual users, allowing them to compare the new release against previous versions.
![image.png](https://developer.android.com/static/blog/assets/image_87410c5b2a_2KU1w.webp)

*How R8 improved Reddit's app performance*

The team observed a **40% faster cold startup** , a **30% reduction in "Application Not Responding" (ANR) errors** , a **25% improvement in frame rendering** , and a **14% reduction in app size**.

These enhancements are crucial for user satisfaction. A faster startup means less waiting and quicker access to content. Fewer ANRs lead to a more stable and reliable app, reducing user frustration. Smoother frame rendering removes UI jank, making scrolling and animations feel fluid and responsive. This positive technical impact was also clearly visible in user sentiment.

User satisfaction indicators of the optimization's success were directly visible on the Google Play Store. Following the rollout of the R8-optimized version, the team saw a dramatic and positive shift in user sentiment and engagement.
![image.png](https://developer.android.com/static/blog/assets/image_e608c65b7f_1xXwkR.webp)

*Drew Heavner: "Enabling R8's full potential tool less than 2 weeks"*

Most impressively, this was accomplished with a focused effort. Drew Heavner, the Staff Software Engineer at Reddit who worked on this initiative, noted that implementing the changes to enable R8's full potential took **less than two weeks**.

## **Confirming the gains: A deep dive with macrobenchmarks**

After observing the significant real-world improvements, Reddit's engineering team and the Android Developer Relations team at Google conducted detailed benchmarks to scientifically confirm the gains and experiment with further optimizations. For this analysis, Reddit engineering provided two versions of their app: one without optimizations and another that applied [**R8**](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) and two more foundational performance optimization tools: [**Baseline Profiles**](https://developer.android.com/topic/performance/baselineprofiles/overview), and [**Startup Profiles**](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).

Baseline Profiles effectively move the Just in Time (JIT) compilation steps away from user devices and onto developer machines. The generated Ahead Of Time (AOT) compiled code has proven to reduce startup time and rendering issues alike.

When an app is packaged, the d8 dexer takes classes and methods and constructs your app's `classes.dex` files. When a user opens the app, these dex files are loaded, one after the other until the app can start. By providing a **Startup Profile** you let d8 know which classes and methods to pack in the first `classes.dex` files. This structure allows the app to load fewer files, which in turn improves startup speed.

[**Jetpack Macrobenchmark**](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) was the core tool for this phase, allowing for precise measurement of user interactions in a controlled environment. To simulate a typical user journey, they used the [**UIAutomator API**](https://developer.android.com/training/testing/other-components/ui-automator) to create a test that opened the app, scrolled down three times, and then scrolled back up.

In the end all that was needed to write the benchmark was this:

```
uiAutomator {

  startApp(REDDIT)

  repeat(3) {

    onView { isScrollable }.fling(Direction.DOWN) }

  repeat(3) {

    onView {isScrollable }.fling(Direction.UP)

  }

}
```

The benchmark data confirmed the field observations and provided deeper insights. The fully optimized app started **55% faster** and users could begin to browse **18% sooner** . The optimized app also showed a **two-thirds reduction in Just in Time (JIT) compilation occurrences** and a **one-third decrease in JIT compilation time** . Frame rendering improved, resulting in **19% more frames** being rendered over the benchmarked user journey. Finally, the app's size was reduced by over a third.
![image.png](https://developer.android.com/static/blog/assets/image_ef7fbd0f3a_TslQi.webp)

*Reddit's overall performance improvements*

You can measure the JIT compilation time with a custom Macrobenchmark trace section metric like this:

```
val jitCompilationMetric = TraceSectionMetric("JIT Compiling %", label = "JIT compilation")
```

## **Enabling the technology behind the transformation: R8**

To enable R8 in full mode, you configure your `app/build.gradle.kts` file by setting `minifyEnabled` and `shrinkResources` to `true` in the release build type.

```
android {

    ...

    buildTypes {

        release {

            isMinifyEnabled = true

            isShrinkResources = true

            proguardFiles(

                getDefaultProguardFile("proguard-android-optimize.txt"),

                "keep-rules.pro",

            )

        }

    }

}
```

This step has to be followed by holistic end to end testing, as performance optimizations can lead to unwanted behavior, which you better catch before your users do.

As shown earlier in this article, R8 performs extensive optimizations in order to maximize your performance benefits. R8 makes substantial modifications to the code including renaming, moving, and removing classes, fields and methods. If you observe that these modifications cause errors, you need to specify which parts of the code R8 shouldn't modify by declaring those in [keep rules](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview).

## **Follow Reddit's example in your app**

Reddit's success with R8 serves as a powerful case study for any development team looking to make a significant, low-effort impact on their app's performance. The direct correlation between the technical improvements and the subsequent rise in user satisfaction underscores the value of performance optimization.

By following the blueprint laid out in this case study---using tools like the [App Performance Score](https://developer.android.com/topic/performance/app-score) to identify opportunities, enabling R8's full optimization potential, monitoring real-world data, and using benchmarks to confirm and deepen understanding---other developers can achieve similar gains.

To get started with R8 in your own app, refer to the freshly updated [official documentation and guidance](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) on enabling, configuring and troubleshooting the R8 optimizer.

###### Written by:

-

  ## [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-weiss) ![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp) ![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](https://developer.android.com/blog/authors/ben-trengrove)[![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](https://developer.android.com/blog/authors/ajesh-pai) 13 Mar 2026 13 Mar 2026 ![](https://developer.android.com/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose](https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose) TikTok is a global short-video platform known for its massive user base and innovative features.

  ###### [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove), [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow_forward](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager) In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.

  ###### [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)