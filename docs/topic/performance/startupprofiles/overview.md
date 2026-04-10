---
title: https://developer.android.com/topic/performance/startupprofiles/overview
url: https://developer.android.com/topic/performance/startupprofiles/overview
source: md.txt
---

Startup Profiles are similar to Baseline Profiles, but they are used at compile
time to optimize DEX layout for faster startup times, rather than for on-device
optimization. To learn more about how startup profiles differ from Baseline
Profiles, see [Compare Baseline Profiles and Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview#compare-baseline-startup).
For more on DEX layout optimization, see [DEX layout optimizations and startup
profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations).

Startup Profiles impact your app's APK size, and the performance impact they
provide might be large or small depending on how your app is structured. We
recommend running an A/B test to assess the effect of Startup Profiles on your
app.

We recommend using both Baseline Profiles and Startup Profiles to fully optimize
app startup.
![](https://developer.android.com/static/topic/performance/images/dex-layout-optimizations.png) **Figure 1.** Code locality improvement from DEX layout optimization.