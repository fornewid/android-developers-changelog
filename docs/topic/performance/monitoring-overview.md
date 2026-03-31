---
title: Monitor performance  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/monitoring-overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Monitor performance Stay organized with collections Save and categorize content based on your preferences.



You can track and analyze performance of your app for valuable insight about a
user's overall experience. You can monitor performance to identify potential
issues and optimize for those paths before they impact more users.

## Android vitals

Android vitals helps you improve the stability and performance of Google Play
apps on Android-powered devices. For the best user experience, we recommend
monitoring and prioritizing your app vitals. For more information, see [Android
vitals](/topic/performance/vitals).

## Firebase Performance Monitoring

Firebase Performance Monitoring is a service that helps you gain insight into
the performance characteristics of your app. Use the Performance Monitoring SDK
to collect performance data from your app, then review and analyze that data in
the Firebase console. For more information, see [Firebase Performance
Monitoring](https://firebase.google.com/docs/perf-mon).

## JankStats library

Use the JankStats library to track and analyze slow rendering frames in your app
and generate reports on the jank statistics impacting your users. For more
information about integrating this to your app, see [JankStats
library](/topic/performance/jankstats).

## Continuous integration

Run benchmarks as part of your CI pipeline to track performance over time and
recognize performance regressions or improvements before you push the update to
your users. For more information, see [Benchmark in Continuous
Integration](/topic/performance/benchmarking/benchmarking-in-ci).