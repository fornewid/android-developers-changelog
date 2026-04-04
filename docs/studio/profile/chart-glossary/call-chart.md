---
title: Call chart  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/profile/chart-glossary/call-chart
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Call chart Stay organized with collections Save and categorize content based on your preferences.




The **call chart** provides a graphical representation of a method trace or
function trace, where the period and timing of a call is represented on the
horizontal axis, and its callees are shown along the vertical axis. Calls to
system APIs are shown in orange, calls to your app's own methods are shown in
green, and calls to third-party APIs (including Java language APIs) are shown in
blue. Figure 1 shows an example call chart and illustrates the concept of self
time, children time, and total time for a given method or function. You can
learn more about these concepts in
[Top-down and bottom-up charts](/studio/profile/chart-glossary/top-bottom-charts).

![](/static/studio/images/profile/call_chart_1-2X.png)

**Figure 1.** An example call chart that illustrates
self, children, and total time for method D.