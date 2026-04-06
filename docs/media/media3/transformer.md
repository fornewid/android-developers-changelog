---
title: Media3 Transformer  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/transformer
source: html-scrape
---

Media3 Transformer is actively under development and we are looking to hear from you! We welcome your feedback, feature requests and bug reports in the [issue tracker](https://github.com/androidx/media/issues). Follow the [ExoPlayer blog](https://medium.com/google-exoplayer) for the latest updates.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media3 Transformer Stay organized with collections Save and categorize content based on your preferences.




Transformer is an API for editing media, including converting between formats
(transcoding), applying changes like trimming a clip from a longer video,
cropping a portion of the video frame, applying custom effects, and other
editing operations. It's part of [Jetpack Media3](/guide/topics/media/media3).

Transformer is compatible with Android 5.0 Lollipop (API level 21) and higher,
and includes workarounds to get more consistent behavior across Android versions
and different devices. The API is implemented on top of `MediaCodec` for
hardware-accelerated video decoding and encoding, and OpenGL for graphical
modifications. Transformer supports format conversions and several types of
edits out of the box, but you can also customize or replace various components
in the pipeline entirely if you need more control. For example, video encoding
works with default settings, but you can also pass custom video encoder settings
or replace the encoder factory to get complete control over how encoders are
used.

Learn how to use Transformer in your app on the [getting
started](/media/media3/transformer/getting-started) page, and try out the [demo app](/media/media3/transformer/demo-application).