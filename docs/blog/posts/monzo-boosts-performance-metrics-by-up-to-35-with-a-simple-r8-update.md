---
title: https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update
url: https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# Monzo boosts performance metrics by up to 35% with a simple R8 update

2 min read ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp) 30 Mar 2026 [![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) \& [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

By fully enabling R8 optimizations, Monzo achieved a massive 35% reduction in their Application Not Responding (ANR) rate. This simple change proved that impactful optimizations don't always require complex engineering efforts.

## Unlocking broad performance wins with R8 full mode

Monzo identified R8 full mode as an easy fix worth trying; and it worked, improving performance across the board:

- **Startup Reliability:** Cold starts improved by 30%, Warm starts by 24%, and Hot starts by 14%.
- **Launch Speed:** P50 launch times improved by 11% and P90 launch times by 12%.
- **Efficiency:** Overall app size was reduced by 9%.
- **Stability:** ANR reduction of 35%.

![AANDDM_Monzo_Quote-1.png](https://developer.android.com/static/blog/assets/AANDDM_Monzo_Quote_1_f28ffd5e7a_oMNg6.webp) ![large_AANDDM_Monzo_Quote-2.png](https://developer.android.com/static/blog/assets/large_AANDDM_Monzo_Quote_2_94f7583b7d_Z23rrlm.webp)

## Enabling optimizations with a single change

Many Android apps use an outdated default configuration file which disables most functionality of the R8 optimizer. The main change Monzo made to unlock these performance improvements was to replace the `proguard-android.txt` default file with `proguard-android-optimize.txt`. This change removes the `-dontoptimize` instruction and allows R8 to properly do its job.

```
buildTypes {
  release {
    isMinifyEnabled = true
    isShrinkResources = true
    proguardFiles(
      getDefaultProguardFile("proguard-android-optimize.txt"),
    )
  }
}
```

After making this change, it's worth looking at your Keep configuration files. These files tell R8 which parts of your code to leave alone (usually because they're called dynamically or by external libraries). Tidying up unnecessary Keep rules means R8 can do more.

## Improving scroll performance with Baseline Profiles

To further enhance the user experience, Monzo implemented [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview), specifically targeting scroll and rendering performance on their main feed. This strategy ensured that the most common user journeys---opening the app and scrolling the feed---were fully optimized. The impact on rendering was substantial: P90 scroll performance became 71% faster, and P95 scroll performance improved by 87%. Now scrolling the app is smoother than before.  

Monzo built this into their release process to maintain these improvements over time. "We trigger the baseline profile generation every week day (before running our nightly builds) and commit the latest changes once completed," Neumayer explains.

## Keeping up with modern Android development

Monzo's experience shows what's possible when you stay up to date with Android build-tooling recommendations. While legacy apps often struggle with complex reflection usage, Monzo found the transition straightforward by documenting their Keep Rules properly. "We always add a comment explaining why Keep Rules are in place, so we know when it's safe to remove the rules," Neumayer notes.  

Neumayer's advice for other teams? Regularly check your practices against current standards: "Take a look at the latest recommendations from Google around app performance and check if you're following all the latest advice."

To get started and learn more about R8, visit [https://d.android.com/r8](https://developer.android.com/r8)
Written by:

-

  ## [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-weiss) ![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp) ![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)
-

  ## [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tracy-agyemang) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp) ![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)
Continue reading
- 3 Authors 27 Aug 2026 27 Aug 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Passkeys_Strapi_2fc9df18a8_Z1oNucg.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys)

  [arrow_forward](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys) WhatsApp is the world's largest messaging platform, serving billions of users globally. It is the default communication tool for people across diverse regions, connecting users through private, reliable, and secure messaging.
  [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang), [Mayank Jain](https://developer.android.com/blog/authors/blog-author) • 8 min read
  - [#Passkeys](https://developer.android.com/blog/topics/passkeys)
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Copy_of_ANDDM_TINDER_Strapi_d8536aec8a_j79Hm.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Tinder cuts app cold starts by 47% with new R8 Configuration Analyzer](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer)

  [arrow_forward](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer) Tinder is on a mission to power and inspire real connections by making meeting easy and fun for every new generation of singles.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai), [Ulises Uriel Verduzco Díaz](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- [![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![View Tracy Agyemang's profile](https://developer.android.com/static/blog/assets/Tracy_Agyemang_Headshot_9a0c523435_1hBimO.webp)](https://developer.android.com/blog/authors/tracy-agyemang) 04 May 2026 04 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_KARROT_Strapi_eed79b0e1b_cCxXk.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gemini and Firebase AI Logic enabled Karrot to increase sales with a translation feature built in under 2 weeks](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature)

  [arrow_forward](https://developer.android.com/blog/posts/gemini-and-firebase-ai-logic-enabled-karrot-to-increase-sales-with-a-translation-feature) Karrot is a hyperlocal, community-driven peer-to-peer marketplace app that enables users to buy, sell, and trade items with other verified users. Since launching in South Korea in 2015, the platform has expanded into global markets, amassing over 43 million registered users.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)