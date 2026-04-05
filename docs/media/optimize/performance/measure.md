---
title: Measuring performance  |  Android media  |  Android Developers
url: https://developer.android.com/media/optimize/performance/measure
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Measuring performance Stay organized with collections Save and categorize content based on your preferences.




In Android 8.0 (API level 26) and later, the `getMetrics()` method is available
for some media classes. It returns a
`PersistableBundle`
object containing configuration
and performance information, expressed as a map of attributes and values.
The `getMetrics()` method is defined for these media classes:

* `MediaPlayer.getMetrics()`
* `MediaRecorder.getMetrics()`
* `MediaCodec.getMetrics()`
* `MediaExtractor.getMetrics()`

Metrics are collected separately for each instance and persist for the
lifetime of the instance. If no metrics are available the method returns
null. The actual metrics returned depend on the class.

## Analytics with ExoPlayer

ExoPlayer includes tools to help you collect and process playback data. Learn
more in the developer guide for
[analytics](/guide/topics/media/exoplayer/analytics).