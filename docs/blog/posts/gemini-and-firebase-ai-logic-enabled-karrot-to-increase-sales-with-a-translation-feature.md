---
title: https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature
url: https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks

###### 2-min read

![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp) 04 May 2026 [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang)

##### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)
\&
[Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

[Karrot](https://play.google.com/store/apps/details?id=com.towneers.www&pcampaignid=web_share) is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.

After launching in North America, engineers at Karrot observed that 30% of users in the region use a non-English device language, such as Spanish. To make the app more accessible, the team wanted to bring seamless translation functionality to Karrot quickly and at scale. The developers determined that the most efficient way to implement quality translations would be through integrating an AI service directly into the app, so they selected the Firebase AI Logic and its Android SDK to access Gemini Flash Lite, which led to higher purchasing conversion among non-English users.
![AndDev_KARROT_Inline.gif](https://developer.android.com/static/blog/assets/And_Dev_KARROT_Inline_29a75f8bf3_25D1By.webp)

**Integrating Gemini Firebase AI Logic**

The team initially tested two on-device options: the ML Kit Translation SDK and Gemini Nano. But the team found challenges with each: ML Kit Translation didn't meet the team's quality expectations, and Gemini Nano, if it isn't already on the device, required the user to download the model data.

The team then tested Firebase AI Logic. By calling the Gemini API directly from the app, Firebase AI Logic delivered accuracy at speeds that mirrored a natural conversational cadence.
![AANDDM_KARROT_Quote_02.png](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Quote_02_0c321aaa68_Z1cNYLW.webp)

Integrating Firebase AI Logic into the app was a "remarkably straightforward experience," according to TaeGyu An, an Android Software Engineer on Karrot's Mobile Platform team. TaeGyu and the team used the platform's [documentation](https://firebase.google.com/docs/ai-logic/get-started) and code samples to build a proof of concept in under three hours.

This allowed the team to spend more time refining prompts and finding optimal configuration values. "Even without extensive experience writing prompts, the official documentation's [guides and tips](https://ai.google.dev/gemini-api/docs/prompting-strategies) made it easy to quickly identify the right direction for improving translation quality," said WonJoong Lee, an Android Software Engineer on Karrot's North America Product Team.

This low barrier to entry and rapid turnaround time enabled engineers to keep development costs low and go from proof of concept to production code in just two weeks---all without setting up a dedicated backend. That also freed up time to focus on UX and policy design, such as opt-in behavior and the conditions for the translation banner.

**Driving sales with enhanced AI features**
![AANDDM_KARROT_Quote_01.png](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Quote_01_0a6e7dd58e_swee9.webp)

Since implementing translation using Gemini and Firebase AI Logic, the Karrot team observed higher purchasing conversion among non-English users, indicating that the translation feature is helping drive sales.

Of users who used a non-English device language, **one in three of them who were shown the translation banner actively used the feature** . The team has also observed that buyers offered translation functionality were **2.4X more likely to start a chat**with a seller than those who weren't.

The flexibility and simplicity of deploying Firebase AI Logic has led the team to explore other features to simplify the workstreams of its engineers. "It's rewarding to build features that scale across diverse Android devices while helping neighbors connect and interact within their local communities," concluded TaeGyu.

Going forward, the team plans to implement [Server Prompt Templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started?api=dev) to adjust prompts after release without shipping a new version of the app. This, combined with [Remote Config](https://firebase.google.com/docs/remote-config), should help the team iterate faster and reduce operational overhead.

**Get started**

Learn how to build Gemini-enabled features like AI translations and in-app personalization and more with [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started?api=dev) to deliver better experiences to your users, faster.
- [#Android](https://developer.android.com/blog/topics/android)

###### Written by:

-

  ## [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/thomas-ezan) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp) ![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 30 Oct 2025 30 Oct 2025 ![](https://developer.android.com/static/blog/assets/thomas_bc2cd0efa0_19rH0O.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [redBus uses Gemini Flash via Firebase AI Logic to boost the length of customer reviews by 57%](https://developer.android.com/blog/posts/red-bus-uses-gemini-flash-via-firebase-ai-logic-to-boost-the-length-of-customer-reviews-by-57)

  [arrow_forward](https://developer.android.com/blog/posts/red-bus-uses-gemini-flash-via-firebase-ai-logic-to-boost-the-length-of-customer-reviews-by-57) As the world's largest online bus ticketing platform, redBus serves millions of travelers across India, Southeast Asia, and Latin America.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) •
  3 min read

- 3 Authors 08 Jun 2026 08 Jun 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_TITLE_Strapi_b83ae0beee_i9nEs.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Datadog delivers millions of in-depth performance insights with ProfilingManager](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager)

  [arrow_forward](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager) Performance regressions are notoriously hard to reproduce, making regressions a massive bottleneck for mobile developers.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan), [Arti Arutiunov](https://developer.android.com/blog/authors/arti-arutiunov), [Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov) •
  4 min read

  - [#Profiling Manager](https://developer.android.com/blog/topics/profiling-manager)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss)[![](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)