---
title: https://developer.android.com/media/media3/transformer
url: https://developer.android.com/media/media3/transformer
source: md.txt
---

# Media3 Transformer

Transformer is an API for editing media, including converting between formats (transcoding), applying changes like trimming a clip from a longer video, cropping a portion of the video frame, applying custom effects, and other editing operations. It's part of[Jetpack Media3](https://developer.android.com/guide/topics/media/media3).

Transformer is compatible with Android 5.0 Lollipop (API level 21) and higher, and includes workarounds to get more consistent behavior across Android versions and different devices. The API is implemented on top of`MediaCodec`for hardware-accelerated video decoding and encoding, and OpenGL for graphical modifications. Transformer supports format conversions and several types of edits out of the box, but you can also customize or replace various components in the pipeline entirely if you need more control. For example, video encoding works with default settings, but you can also pass custom video encoder settings or replace the encoder factory to get complete control over how encoders are used.

Learn how to use Transformer in your app on the[getting started](https://developer.android.com/media/media3/transformer/getting-started)page, and try out the[demo app](https://developer.android.com/media/media3/transformer/demo-application).