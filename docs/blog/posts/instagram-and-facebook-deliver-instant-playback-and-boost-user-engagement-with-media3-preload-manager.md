---
title: https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager
url: https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager

###### 4-min read

![](https://developer.android.com/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp) 05 Mar 2026 [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) [##### Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya)

###### Developer Relations Engineer

In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally. For Meta, delivering videos seamlessly isn't just a feature, it's the core of their user experience. Short-form videos, particularly Facebook Newsfeed and Instagram Reels, have become a primary driver of engagement. They enable creative expression and rapid content consumption; connecting and entertaining people around the world.

This blog post takes you through the journey of how Meta transformed video playback for billions by delivering true instant playback.

### **The latency gap in short form videos**

Short-form videos lead to highly fast paced interactions as users quickly scroll through their feeds. Delivering a seamless transition between videos in an ever-changing feed introduces unique hurdles for instantaneous playback. Hence we need solutions that go beyond traditional disk caching and standard reactive playback strategies.

### **The path forward with Media3 PreloadManager**

To address the shifts in consumption habits from rise in short form content and the limitations of traditional long form playback architecture, Jetpack Media3 introduced [PreloadManager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create). This component allows developers to move beyond disk caching, offering granular control and customization to keep media ready in memory before the user hits play. Read this [blog series](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html) to understand technical details about media playback with PreloadManager.

## **How Meta achieved true instant playback**

### **Existing Complexities**

Previously, Meta used a combination of warmup (to get players ready) and prefetch (to cache content on disk) for video delivery. While these methods helped improve network efficiency, they introduced significant challenges. Warmup required instantiating multiple player instances sequentially, which consumed significant memory and limited preloading to only a few videos. This high resource demand meant that a more scalable robust solution could be applied to deliver the instant playback expected on modern, fast-scrolling social feeds.

### **Integrating Media3 PreloadManager**

To achieve truly instant playback, Meta's Media Foundation Client team integrated the Jetpack Media3 PreloadManager into Facebook and Instagram. They chose the DefaultPreloadManager to unify their preloading and playback systems. This integration required refactoring Meta's existing architecture to enable efficient resource sharing between the PreloadManager and ExoPlayer instances. This strategic shift provided a key architectural advantage: the ability to parallelize preloading tasks and manage many videos using a single player instance. This dramatically increased preloading capacity while eliminating the high memory complexities of their previous approach.
![colinKho.png](https://developer.android.com/static/blog/assets/colin_Kho_fc40711178_Y5Hbs.webp)

### **Optimization and Performance Tuning**

The team then performed extensive testing and iterations to optimize performance across Meta's diverse global device ecosystem. Initial aggressive preloading sometimes caused issues, including increased memory usage and scroll performance slowdowns. To solve this, they fine-tuned the implementation by using careful memory measurements, considering device fragmentation, and tailoring the system to specific UI patterns.

### **Fine tuning implementation to specific UI patterns**

Meta applied different preloading strategies and tailored the behavior to match the specific UI patterns of each app:

- **Facebook Newsfeed** : The UI prioritizes the video currently coming into view. The manager preloads only the current video to ensure it starts the moment the user pauses their scroll. This "**current-only**" focus minimizes data and memory footprints in an environment where users may see many static posts between videos. While the system is presently designed to preload just the video in view, it can be adjusted to also preload upcoming (future) videos.
- **Instagram Reels** : This is a pure video environment where users swipe vertically. For this UI, the team implemented an "**adjacent preload**" strategy. The PreloadManager keeps the videos immediately after the current Reel ready in memory. This bi-directional approach ensures that whether a user swipes up or down, the transition remains instant and smooth. The result was a dramatic improvement in the Quality of Experience (QoE) including improvements in Playback Start and Time to First Frame for the user.

### **Scaling for a diverse global device ecosystem**

Scaling a high-performance video stack across billions of devices requires more than just aggressive preloading; it requires intelligence. Meta faced initial challenges with memory pressure and scroll lag, particularly on mid-to-low-end hardware. To solve this, they built a *Device Stress Detection* system around the Media3 implementation. The apps now monitor I/O and CPU signals in real-time. If a device is under heavy load, preloading is paused to prioritize UI responsiveness.

This device-aware optimization ensures that the benefit of instant playback doesn't come at the cost of system stability, allowing even users on older hardware to experience a smoother, uninterrupted feed.
![mirabelHu.png](https://developer.android.com/static/blog/assets/mirabel_Hu_c2c154dbc2_Z2nSukS.webp)

### **Architectural wins and code health**

Beyond the user-facing metrics, the migration to Media3 `PreloadManager` offered long-term architectural benefits. While the integration and tuning process needed multiple iterations to balance performance, the resulting codebase is more maintainable. The team found that the `PreloadManager` API integrated cleanly with the existing Media3 ecosystem, allowing for better resource sharing. For Meta, the adoption of Media3 PreloadManager was a strategic investment in the future of video consumption.

By adopting preloading and adding device-intelligent gates, they successfully increased total watch time on their apps and improved the overall engagement of their global community.

## **Resulting impact on Instagram and Facebook**

The proactive architecture delivered immediate and measurable improvements across both platforms.

- Facebook experienced **faster playback starts, decreased playback stall rates and a reduction in bad sessions** (like rebuffering, delayed start time, lower quality,etc) which overall resulted in higher watch time.
- Instagram saw **faster playback starts and an increase in total watch time. Eliminating join latency** (the interval from the user's action to the first frame display) directly increased engagement metrics. The **fewer interruptions** due to reduced buffering meant users watched more content, which showed through engagement metrics.

![beforeAfterPreload.gif](https://developer.android.com/static/blog/assets/before_After_Preload_57acfe3175_k1TQ5.webp)

## **Key engineering learnings at scale**

As media consumption habits evolve, the demand for instant experiences will continue to grow. Implementing proactive memory management and optimizing for scale and device diversity ensures your application can meet these expectations efficiently.

- **Prioritize intelligent preloading**

Focus on delivering a reliable experience by minimizing stutters and loading times through preloading. Rather than simple disk caching, leveraging memory-level preloading ensures that content is ready the moment a user interacts with it.

- **Align your implementation with UI patterns**

Customize preloading behavior as per your apps's UI. For example, use a "current-only" focus for mixed feeds like Facebook to save memory, and an "adjacent preload" strategy for vertical environments like Instagram Reels.
![preloadingStrategy.png](https://developer.android.com/static/blog/assets/preloading_Strategy_381de8a469_Z1CnbTE.webp)

- **Leverage Media3 for long-term code health**

Integrating with Media3 APIs rather than a custom caching solution allows for better resource sharing between the player and the PreloadManager, enabling you to manage multiple videos with a single player instance. This results in a future-proof codebase that is easier for engineering teams to not only maintain and optimize over time but also benefit from the latest feature updates.

- **Implement device aware optimizations**

Broaden your market reach by testing on various devices, including mid-to-low-end models. Use real-time signals like CPU, memory, and I/O to adapt features and resource usage dynamically.

## **Learn More**

To get started and learn more, visit[](https://www.google.com/search?q=https://developer.android.com/guide/topics/media/media3/exoplayer/preload-manager)

- Explore the Media3 [PreloadManager documentation](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager).
- Read the[blog series](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html) for advanced technical and implementation details.
  - [Part 1: Introducing Preloading with Media3](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html)
  - [Part 2: A deep dive into Media3's PreloadManager](https://android-developers.googleblog.com/2025/09/a-deep-dive-into-media3-preloadmanager.html)
- Check out the [sample app](https://github.com/android/socialite) to see preloading in action.

Now you know the secrets for instant playback. Go try them out!

###### Written by:

-

  ## [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/mayuri-khabya) ![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp) ![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)

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