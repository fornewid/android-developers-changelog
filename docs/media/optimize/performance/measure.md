---
title: https://developer.android.com/media/optimize/performance/measure
url: https://developer.android.com/media/optimize/performance/measure
source: md.txt
---

# Measuring performance

In Android 8.0 (API level 26) and later, the`getMetrics()`method is available for some media classes. It returns a[PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle)object containing configuration and performance information, expressed as a map of attributes and values. The`getMetrics()`method is defined for these media classes:

- [MediaPlayer.getMetrics()](https://developer.android.com/reference/android/media/MediaPlayer#getMetrics())
- [MediaRecorder.getMetrics()](https://developer.android.com/reference/android/media/MediaRecorder#getMetrics())
- [MediaCodec.getMetrics()](https://developer.android.com/reference/android/media/MediaCodec#getMetrics())
- [MediaExtractor.getMetrics()](https://developer.android.com/reference/android/media/MediaExtractor#getMetrics())

Metrics are collected separately for each instance and persist for the lifetime of the instance. If no metrics are available the method returns null. The actual metrics returned depend on the class.

## Analytics with ExoPlayer

ExoPlayer includes tools to help you collect and process playback data. Learn more in the developer guide for[analytics](https://developer.android.com/guide/topics/media/exoplayer/analytics).