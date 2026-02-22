---
title: https://developer.android.com/topic/performance/app-optimization/test-the-optimization
url: https://developer.android.com/topic/performance/app-optimization/test-the-optimization
source: md.txt
---

After enabling app optimization, validate that your app is working as intended.

To test the optimization locally:

- **Measure performance gains using benchmarks** : To test performance locally,[benchmark your app](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview)before and after enabling app optimization.
- **Test your app's critical user journeys (CUJs)** : Make sure that all CUJs work as expected, for example, test whether users can sign in and do other important tasks. To test your release app build, use[UI Automator](https://developer.android.com/training/testing/other-components/ui-automator).

To test your app in production:

- **Track app performance metrics** : Use[Android vitals](https://developer.android.com/topic/performance/vitals)on the Play Console, and through the Google Play Developer Reporting API.
- **Release app updates with staged rollouts** : If your keep rules apply to rarely used code, it can be difficult to test them locally. Use[staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149)to test your changes with a set of early users. Pay attention to the crash regressions that might be due to issues with keep rules. For more information on how to identify crashes caused by R8, see[Troubleshoot the optimization](https://developer.android.com/topic/performance/app-optimization/troubleshoot-the-optimization).