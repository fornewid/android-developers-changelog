---
title: https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio
url: https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# Ultrahuman launches features 15% faster with Gemini in Android Studio

2-min read ![](https://developer.android.com/static/blog/assets/Ultrahumanx_Gi_AS_Banner_1612731319_Z23acG3.webp) 08 Jan 2026 [![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev) \& [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) [Ultrahuman](https://play.google.com/store/apps/details?id=com.ultrahuman.android) is a consumer health-tech startup that provides daily well-being insights to users based on biometric data from the company's wearables, like the [RING Air](https://www.ultrahuman.com/ring/buy/us/) and the [M1 Live](https://www.ultrahuman.com/m1/) Continuous Glucose Monitor (CGM). The Ultrahuman team leaned on [Gemini in Android Studio's](https://developer.android.com/gemini-in-android) contextually aware tools to streamline and accelerate their development process.

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
Written by:

-

  ## [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev)

  ###### Staff Developer Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/amrit-sanjeev) ![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp) ![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)
-

  ## [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

  ###### Staff Developer Programs Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/trevor-johns) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
Continue reading
- [![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp)](https://developer.android.com/blog/authors/ash-nohe) 08 May 2026 08 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_2000x1000_7d5a00e6c2_Z2vwfIA.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gratitude saw 25% higher retention for widget users](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users)

  [arrow_forward](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users) The mindfulness app Gratitude encourages consistency through micro daily journaling, affirmations, and vision boards. The app has over 6 million downloads, 150 thousand 5 star ratings, and 100 million journal entries logged.
  [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev), [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe) • 3 min read
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


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)