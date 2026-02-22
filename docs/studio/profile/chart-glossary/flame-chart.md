---
title: https://developer.android.com/studio/profile/chart-glossary/flame-chart
url: https://developer.android.com/studio/profile/chart-glossary/flame-chart
source: md.txt
---

# Flame chart

The**Flame Chart**tab provides an inverted call chart that aggregates identical call stacks. That is, identical methods or functions that share the same sequence of callers are collected and represented as one longer bar in a flame chart (rather than displaying them as multiple shorter bars, as shown in a call chart). This makes it easier to see which methods or functions consume the most time. However, this also means that the horizontal axis doesn't represent a timeline; instead, it indicates the relative amount of time each method or function takes to execute.

To help illustrate this concept, consider the call chart in Figure 1. Note that method D makes multiple calls to B (B~1~, B~2~, and B~3~), and some of those calls to B make a call to C (C~1~and C~3~).

![](https://developer.android.com/static/studio/images/profile/call_chart_2-2X.png)

**Figure 1.**A call chart with multiple method calls that share a common sequence of callers.

<br />

Because B~1~, B~2~, and B~3~share the same sequence of callers (A → D → B) they are aggregated, as shown in Figure 2. Similarly, C~1~and C~3~are aggregated because they share the same sequence of callers (A → D → B → C); note that C~2~is not included because it has a different sequence of callers (A → D → C).

![](https://developer.android.com/static/studio/images/profile/flame_chart_aggregation-2X.png)

**Figure 2.**Aggregating identical methods that share the same call stack.

<br />

The aggregated calls are used to create the flame chart, as shown in Figure 3. Note that, for any given call in a flame chart, the callees that consume the most CPU time appear first.

![](https://developer.android.com/static/studio/images/profile/flame_chart-2X.png)

**Figure 3.**A flame chart representation of the call chart shown in figure 5.

<br />