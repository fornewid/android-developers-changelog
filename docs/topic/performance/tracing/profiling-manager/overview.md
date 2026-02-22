---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/overview
url: https://developer.android.com/topic/performance/tracing/profiling-manager/overview
source: md.txt
---

# Overview

The[`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager)Android API lets you collect real user performance profiles, such as[system traces](https://developer.android.com/topic/performance/tracing), programmatically. The`ProfilingManager`API supports two types of trace collections: traces that you explicitly start and event-based traces.

This section focuses on traces that you explicitly start and covers the following topics:

- How to collect traces with`ProfilingManager`.
- How to retrieve those traces.
- How to visualize traces in Perfetto UI.
- Important details about how`ProfilingManager`works.

| **Key Point:** This guide is for developers who want to set up a way to collect end-user performance profiles.