---
title: Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Case Studies](/blog/categories/case-studies)

# Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks

###### 2-min read

![](/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp)

04

May
2026

[![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](/blog/authors/tracy-agyemang)

##### [Thomas Ezan](/blog/authors/thomas-ezan) & [Tracy Agyemang](/blog/authors/tracy-agyemang)

[Karrot](https://play.google.com/store/apps/details?id=com.towneers.www&pcampaignid=web_share) is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.

After launching in North America, engineers at Karrot observed that 30% of users in the region use a non-English device language, such as Spanish. To make the app more accessible, the team wanted to bring seamless translation functionality to Karrot quickly and at scale. The developers determined that the most efficient way to implement quality translations would be through integrating an AI service directly into the app, so they selected the Firebase AI Logic and its Android SDK to access Gemini Flash Lite, which led to higher purchasing conversion among non-English users.

![AndDev_KARROT_Inline.gif](/static/blog/assets/And_Dev_KARROT_Inline_29a75f8bf3_25D1By.webp)

**Integrating Gemini Firebase AI Logic**

The team initially tested two on-device options: the ML Kit Translation SDK and Gemini Nano. But the team found challenges with each: ML Kit Translation didn’t meet the team’s quality expectations, and Gemini Nano, if it isn’t already on the device, required the user to download the model data.

The team then tested Firebase AI Logic. By calling the Gemini API directly from the app, Firebase AI Logic delivered accuracy at speeds that mirrored a natural conversational cadence.

![AANDDM_KARROT_Quote_02.png](/static/blog/assets/AANDDM_KARROT_Quote_02_0c321aaa68_Z1cNYLW.webp)

Integrating Firebase AI Logic into the app was a “remarkably straightforward experience,” according to TaeGyu An, an Android Software Engineer on Karrot’s Mobile Platform team. TaeGyu and the team used the platform’s [documentation](https://firebase.google.com/docs/ai-logic/get-started) and code samples to build a proof of concept in under three hours.

This allowed the team to spend more time refining prompts and finding optimal configuration values. “Even without extensive experience writing prompts, the official documentation's [guides and tips](https://ai.google.dev/gemini-api/docs/prompting-strategies) made it easy to quickly identify the right direction for improving translation quality,” said WonJoong Lee, an Android Software Engineer on Karrot’s North America Product Team.

This low barrier to entry and rapid turnaround time enabled engineers to keep development costs low and go from proof of concept to production code in just two weeks—all without setting up a dedicated backend. That also freed up time to focus on UX and policy design, such as opt-in behavior and the conditions for the translation banner.

**Driving sales with enhanced AI features**

![AANDDM_KARROT_Quote_01.png](/static/blog/assets/AANDDM_KARROT_Quote_01_0a6e7dd58e_swee9.webp)

Since implementing translation using Gemini and Firebase AI Logic, the Karrot team observed higher purchasing conversion among non-English users, indicating that the translation feature is helping drive sales.

Of users who used a non-English device language, **one in three of them who were shown the translation banner actively used the feature**. The team has also observed that buyers offered translation functionality were **2.4X more likely to start a chat**with a seller than those who weren’t.

The flexibility and simplicity of deploying Firebase AI Logic has led the team to explore other features to simplify the workstreams of its engineers. “It’s rewarding to build features that scale across diverse Android devices while helping neighbors connect and interact within their local communities,” concluded TaeGyu.

Going forward, the team plans to implement [Server Prompt Templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started?api=dev) to adjust prompts after release without shipping a new version of the app. This, combined with [Remote Config](https://firebase.google.com/docs/remote-config), should help the team iterate faster and reduce operational overhead.

**Get started**

Learn how to build Gemini-enabled features like AI translations and in-app personalization and more with [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started?api=dev) to deliver better experiences to your users, faster.

* [#Android](/blog/topics/android)

###### Written by:

* ## [Thomas Ezan](/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/thomas-ezan)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)
* ## [Tracy Agyemang](/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read\_more
  View profile](/blog/authors/tracy-agyemang)

  ![](/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)

  ![](/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)

## Continue reading

* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)

  30

  Oct
  2025

  30

  Oct
  2025

  ![](/static/blog/assets/thomas_bc2cd0efa0_19rH0O.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [redBus uses Gemini Flash via Firebase AI Logic to boost the length of customer reviews by 57%](/blog/posts/red-bus-uses-gemini-flash-via-firebase-ai-logic-to-boost-the-length-of-customer-reviews-by-57)

  [arrow\_forward](/blog/posts/red-bus-uses-gemini-flash-via-firebase-ai-logic-to-boost-the-length-of-customer-reviews-by-57)

  As the world's largest online bus ticketing platform, redBus serves millions of travelers across India, Southeast Asia, and Latin America.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan) • 3 min read
* [![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

  30

  Mar
  2026

  30

  Mar
  2026

  ![](/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow\_forward](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](/blog/authors/ben-weiss) • 2 min read
* [![](/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](/blog/authors/ben-trengrove)[![](/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](/blog/authors/ajesh-pai)

  13

  Mar
  2026

  13

  Mar
  2026

  ![](/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  [arrow\_forward](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  TikTok is a global short-video platform known for its massive user base and innovative features.

  ###### [Ben Trengrove](/blog/authors/ben-trengrove), [Ajesh Pai](/blog/authors/ajesh-pai) • 2 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)