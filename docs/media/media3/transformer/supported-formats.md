---
title: https://developer.android.com/media/media3/transformer/supported-formats
url: https://developer.android.com/media/media3/transformer/supported-formats
source: md.txt
---

See the [ExoPlayer supported formats
page](https://developer.android.com/guide/topics/media/exoplayer/media-items) for an introduction to
media formats in general. The same limitations on loading, extracting, and
decoding streams apply with Transformer, though Transformer does not support
ExoPlayer's bundled software decoder modules.

Transformer also relies on `MediaCodec` for encoding, which limits the output
formats supported. See [MediaCodec video codecs](https://developer.android.com/guide/topics/media/media-formats#video-codecs)
for more information about encoding limitations.

By default, `Transformer` outputs standard MP4 files using [`InAppMp4Muxer`](https://developer.android.com/reference/androidx/media3/transformer/InAppMp4Muxer).
If your app requires fragmented MP4, you can pass an
[`InAppFragmentedMp4Muxer.Factory`](https://developer.android.com/reference/androidx/media3/transformer/InAppFragmentedMp4Muxer.Factory)
when initializing your `Transformer` instance. Media3 also supports other
formats such as WebM, AAC, Ogg using dedicated muxers like [`WebmMuxer`](https://developer.android.com/reference/androidx/media3/muxer/WebmMuxer)
, [`AacMuxer`](https://developer.android.com/reference/androidx/media3/muxer/AacMuxer) and [`OggMuxer`](https://developer.android.com/reference/androidx/media3/muxer/OggMuxer). These must be wrapped in
a custom [`Muxer.Factory`](https://developer.android.com/reference/androidx/media3/muxer/Muxer.Factory) to be injected, but future releases
will include ready-to-use factory implementations to simplify this process.

## Image support

Transformer uses `BitmapFactory` to load and decode all image assets, so
Transformer supports all the formats BitmapFactory does. See
[Image support](https://developer.android.com/guide/topics/media/media-formats#image-formats)
for supported image types. For multi-picture formats (e.g. gifs), a single image
frame from the container is displayed if the `DefaultAssetLoaderFactory` is
used.

## Special formats

Transformer supports handling input in newer media formats that provide special
features compared to conventional formats.

### Handling HDR videos

More and more devices support [HDR video
capture](https://developer.android.com/training/camera2/hdr-video-capture), giving more vivid, accurate
colors and a greater brightness range.

Transformer supports editing HDR videos from Android 13 (API level 33) onwards
on devices with the required encoding support. When editing HDR videos, any GL
video effects need to handle 16-bit floating point color components and BT.2020
color space. `HDR_MODE_KEEP_HDR` is the default mode when building the
`Composition`. If HDR editing is not supported, the Transformer
falls back to using `HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL`.

Converting HDR to SDR, also known as *tone-mapping* , is supported from Android
10 (API level 29) onwards on devices with the required decoding and OpenGL
support. This is useful when sharing HDR media to other apps or services that
don't support ingestion of HDR content. To enable tone-mapping using OpenGL call
`setHdrMode(HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL)` when creating the
`Composition`. From Android 12 (API level 31) onwards, `MediaCodec`
also supports tone-mapping on some devices, including all devices running
Android 13 or higher that can capture HDR video. To enable tone-mapping using
`MediaCodec` call `setHdrMode(HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_MEDIACODEC)`.

### Handling slow motion media

Slow-motion videos include metadata indicating the speed at which each section
of the stream should be played. *Flattening* is the process of producing a new
video stream based on the slow-motion video but where the sections are sped up
or slowed down based on metadata, so that they play correctly even on players
that don't apply slow motion metadata.

To flatten slow-motion streams, use the `setFlattenForSlowMotion` builder
method on `EditedMediaItem`.


### Kotlin

```kotlin
val editedMediaItem =
  EditedMediaItem.Builder(inputMediaItem).setFlattenForSlowMotion(true).build()
val transformer = Transformer.Builder(context).addListener(transformerListener).build()
transformer.start(editedMediaItem, outputPath)
```

### Java

```java
EditedMediaItem editedMediaItem =
    new EditedMediaItem.Builder(inputMediaItem).setFlattenForSlowMotion(true).build();
Transformer transformer =
    new Transformer.Builder(context).addListener(transformerListener).build();
transformer.start(editedMediaItem, outputPath);
```

<br />

This lets you support slow-motion videos without having to worry about
handling these special formats. All you need to do is to store and play the
flattened version of the video instead of the original one.

> [!NOTE]
> **Note:** Only Samsung's slow motion format is supported.