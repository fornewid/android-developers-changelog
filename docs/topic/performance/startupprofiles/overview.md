---
title: Overview of Startup Profiles  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/startupprofiles/overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Overview of Startup Profiles Stay organized with collections Save and categorize content based on your preferences.



Startup Profiles are similar to Baseline Profiles, but they are used at compile
time to optimize DEX layout for faster startup times, rather than for on-device
optimization. To learn more about how startup profiles differ from Baseline
Profiles, see [Compare Baseline Profiles and Startup Profiles](/topic/performance/baselineprofiles/overview#compare-baseline-startup).
For more on DEX layout optimization, see [DEX layout optimizations and startup
profiles](/topic/performance/baselineprofiles/dex-layout-optimizations).

Startup Profiles impact your app's APK size, and the performance impact they
provide might be large or small depending on how your app is structured. We
recommend running an A/B test to assess the effect of Startup Profiles on your
app.

We recommend using both Baseline Profiles and Startup Profiles to fully optimize
app startup.

![](/static/topic/performance/images/dex-layout-optimizations.png)


**Figure 1.** Code locality improvement from DEX layout
optimization.

[Next

Create Startup Profiles

arrow\_forward](/topic/performance/startupprofiles/dex-layout-optimizations)