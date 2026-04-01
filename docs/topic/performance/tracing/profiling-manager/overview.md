---
title: Overview  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/tracing/profiling-manager/overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Overview Stay organized with collections Save and categorize content based on your preferences.



The [`ProfilingManager`](/reference/android/os/ProfilingManager) Android API lets you collect real user performance
profiles, such as [system traces](/topic/performance/tracing), programmatically. The `ProfilingManager` API
supports two types of trace collections: traces that you explicitly start and
event-based traces.

This section focuses on traces that you explicitly start and covers the following
topics:

* How to collect traces with `ProfilingManager`.
* How to retrieve those traces.
* How to visualize traces in Perfetto UI.
* Important details about how `ProfilingManager` works.

**Key Point:** This guide is for developers who want to set up a way to collect
end-user performance profiles.