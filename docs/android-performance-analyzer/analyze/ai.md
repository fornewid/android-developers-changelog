---
title: Use AI-powered analysis features  |  Android Performance Analyzer  |  Android Developers
url: https://developer.android.com/android-performance-analyzer/analyze/ai
source: html-scrape
---

Android Performance Analyzer is currently intended for profiling games and Vulkan-based graphics. For all other apps, use the [profilers in Android Studio](/studio/profile).

* [Home](https://developer.android.com/)
* [Android Performance Analyzer](https://developer.android.com/android-performance-analyzer)

# Use AI-powered analysis features Stay organized with collections Save and categorize content based on your preferences.





Android Performance Analyzer includes features to support AI-assisted analysis of system traces.
This guide explains how to use these features with your preferred AI agent to
streamline the analysis process.

## Explore a trace with your AI agent

With the sheer breadth of data available in an Android Performance Analyzer trace file, it can
be difficult to know where to start if you aren't already experienced with
profiling. The System Profiler supports a purpose-built analysis skill that
works with your preferred AI agent to suggest starting points in response to
high-level questions.

![](/static/android-performance-analyzer/images/ai-analysis.png)

To get started, use the Android profiler skill.

## Android skills

[View on GitHub
open\_in\_new](https://github.com/android/skills/tree/main/profilers/android-profiler)

### Android profiler

Use an [Android skill](/tools/agents/android-skills) to record and analyze Android performance data so that you can diagnose bottlenecks, jank, and memory leaks, and convert natural language into executable trace queries, such as PerfettoSQL queries.

To install this skill from the [Android CLI](/tools/agents/android-cli), run:

```
android skills add android-profiler
```

## Use AI to build custom queries

Android Performance Analyzer supports [custom SQL queries](/android-performance-analyzer/view#custom-queries) for deeper and more
flexible analysis of your recorded traces. You can always write your own
queries, but the System Profiler also supports letting your preferred AI agent
write a query for you.

![](/static/android-performance-analyzer/images/ai-sql.png)

To get started, use the [android-profiler skill](#ai-analysis).