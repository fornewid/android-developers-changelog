---
title: https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio
url: https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Ultrahuman launches features 15% faster with Gemini in Android Studio

###### 2-min read

![](https://developer.android.com/static/blog/assets/Ultrahumanx_Gi_AS_Banner_1612731319_Z23acG3.webp) 08 Jan 2026 [![](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns)

##### [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev)
\&
[Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

[Ultrahuman](https://play.google.com/store/apps/details?id=com.ultrahuman.android) is a consumer health-tech startup that provides daily well-being insights to users based on biometric data from the company's wearables, like the [RING Air](https://www.ultrahuman.com/ring/buy/us/) and the [M1 Live](https://www.ultrahuman.com/m1/) Continuous Glucose Monitor (CGM). The Ultrahuman team leaned on [Gemini in Android Studio's](https://developer.android.com/gemini-in-android) contextually aware tools to streamline and accelerate their development process.

Ultrahuman's app is maintained by a lean team of just eight developers. They prioritize building features that their users love, and have a backlog of bugs and needed performance improvements that take a lot of time. The team needed to scale up their output of feature improvements, and also needed to handle their performance improvements, without increasing headcount. One of their biggest opportunities was reducing the amount of time and effort for their backlog: every hour saved on maintenance could be reinvested into working on features for their users.
![UltrahumanxGiAS_Image_01.webp](https://developer.android.com/static/blog/assets/Ultrahumanx_Gi_AS_Image_01_645a0baed3_Z1krKy4.webp)

**Solving technical hurdles and boosting performance with Gemini**

The team integrated Gemini in Android Studio to see if the AI enhanced tools could improve their workflow by handling many Android tasks. First, the team turned to the [Gemini chat](https://developers.google.com/gemini-code-assist/docs/use-gemini-code-assist-chat) inside Android Studio. The goal was to prototype a [GATT Server](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt) implementation for their application's Bluetooth Low Energy (BLE) connectivity.
![arka.png](https://developer.android.com/static/blog/assets/arka_674b22b8fe_t79PE.webp)

As Ultrahuman's Android Development Lead, Arka, noted, "**Gemini helped us reach a working prototype in under an hour**---something that would have otherwise taken us several hours." The BLE implementation provided by Gemini worked perfectly for syncing large amounts of health sensor data while the app ran in the background, improving the data syncing process and saving battery life on both the user's Android phone and Ultrahuman's paired wearable device.

Beyond this core challenge, Gemini also proved invaluable for finding algorithmic optimizations in a custom open-source library, pointing to helpful documentation, assisting with code commenting, and analyzing crash logs. The Ultrahuman team also used [code completion](https://developer.android.com/studio/preview/gemini/ai-code-completion) to help them breeze through writing otherwise repetitive code, [Jetpack Compose Preview Generation](https://developer.android.com/studio/gemini/generate-compose-previews) to enable rapid iteration during UI design, and [Agent Mode](https://developer.android.com/studio/gemini/agent-mode) for managing complex, project-wide changes, such as rendering a new stacked bar graph that mapped to backend data models and UI models.
![arka2.png](https://developer.android.com/static/blog/assets/arka2_812923fa66_Z10WPE.webp)

<br />

**Transforming productivity and accelerating feature delivery**

These improvements have saved the team dozens of hours each week. This reclaimed time is being used to deliver new features to Ultrahuman's beta users 10-15% faster. For example, the team built a new in-app AI assistant for users, powered by [Gemini 2.5 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash). The UI design, architecture, and parts of the user experience for this new feature were initially suggested by Gemini in Android Studio---showcasing a full-circle AI-assisted development process.

**Accelerate your Android development with Gemini**

Gemini's expert Android advice, closely integrated throughout Android Studio, helps Android developers spend less time digging through documentation and writing boilerplate code---freeing up more time to innovate.

Learn how [Gemini in Android Studio](http://d.android.com/gemini-in-android) can help your team resolve complex issues, streamline workflows, and ship new features faster.

###### Written by:

-

  ## [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev)

  ###### Staff Developer Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/amrit-sanjeev) ![](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp) ![](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)
-

  ## [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

  ###### Staff Developer Programs Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/trevor-johns) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

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