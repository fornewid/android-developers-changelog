---
title: https://developer.android.com/media/implement/editing-app
url: https://developer.android.com/media/implement/editing-app
source: md.txt
---

The Transformer APIs in Jetpack Media3 are designed to make media editing
performant and reliable. Transformer supports a number of operations,
including:

- Modifying a video with trimming, scaling, and rotating
- Adding effects like overlays and filters
- Processing special formats like HDR and slow-motion video
- Exporting a media item after applying edits

This page walks you through some of the key use cases covered by
Transformer. For more details you can head to our full guides on
[Media3 Transformer](https://developer.android.com/guide/topics/media/transformer).

## Get started

To get started, add a dependency on the Transformer, Effect, and Common modules
of Jetpack Media3:  

```groovy
implementation "androidx.media3:media3-transformer:1.9.2"
implementation "androidx.media3:media3-effect:1.9.2"
implementation "androidx.media3:media3-common:1.9.2"
```

Make sure to replace `1.9.2` with your preferred version of the
library. You can refer to the
[release notes](https://github.com/androidx/media/tree/release/RELEASENOTES.md)
to see the latest version.

### Important classes

| Class | Purpose |
|---|---|
| [Transformer](https://developer.android.com/reference/androidx/media3/transformer/Transformer) | Start and stop transformations and check for progress updates on a running transformation. |
| [EditedMediaItem](https://developer.android.com/reference/androidx/media3/transformer/EditedMediaItem) | Represents a media item to process and the edits to apply to it. |
| [Effects](https://developer.android.com/reference/androidx/media3/transformer/Effects) | A collection of audio and video effects. |

## Configure the output

With `Transformer.Builder`, you can now specify `videoMimeType` and
`audioMimetype` directory by setting the function without needing to create a
`TransformationRequest` object.

### Transcode between formats

The following code shows how to configure a `Transformer` object to
output H.265/AVC video and AAC audio:  

### Kotlin

```kotlin
val transformer = Transformer.Builder(context)
    .setVideoMimeType(MimeTypes.VIDEO_H265)
    .setAudioMimeType(MimeTypes.AUDIO_AAC)
    .build()
```

### Java

```java
Transformer transformer = new Transformer.Builder(context)
    .setVideoMimeType(MimeTypes.VIDEO_H265)
    .setAudioMimeType(MimeTypes.AUDIO_AAC)
    .build();
```

If the input media format already matches the transformation request for audio
or video, Transformer automatically switches to *transmuxing*, that is, copying
the compressed samples from the input container to the output container without
modification. This avoids the computational cost and potential quality loss of
decoding and re-encoding in the same format.

### Set HDR mode

If the input media file is in an HDR format, you can choose between a few
different modes for how Transformer processes the HDR information. You probably
want to use either `HDR_MODE_KEEP_HDR` or
`HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL`.

|   | `HDR_MODE_KEEP_HDR` | `HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL` |
|---|---|---|
| Description | Preserve the HDR data, meaning that the HDR output format is the same as the HDR input format. | Tonemap HDR input to SDR using an OpenGL tone-mapper, meaning that the output format will be in SDR. |
| Support | Supported on API levels 31+ for devices that include an encoder with the [`FEATURE_HdrEditing`](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities#FEATURE_HdrEditing) capability. | Supported on API levels 29+. |
| Errors | If not supported, attempts to use `HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL` instead. | If not supported, throws an [`ExportException`](https://developer.android.com/reference/androidx/media3/transformer/ExportException). |

On devices that support the required encoding capabilities and run Android 13
(API level 33) or higher, `Transformer` objects let you edit HDR videos.
`HDR_MODE_KEEP_HDR` is the default mode when building the `Composition` object,
as shown in the following code:  

### Kotlin

```kotlin
val composition = Composition.Builder(
    ImmutableList.of(videoSequence))
    .setHdrMode(HDR_MODE_KEEP_HDR)
    .build()
```

### Java

```java
Composition composition = new Composition.Builder(
    ImmutableList.of(videoSequence))
    .setHdrMode(Composition.HDR_MODE_KEEP_HDR)
    .build();
```

## Prepare a media item

A [`MediaItem`](https://developer.android.com/guide/topics/media/exoplayer/media-items) represents an audio
or video item in your app. An `EditedMediaItem` collects a `MediaItem` along
with the transformations to apply to it.

### Trim a video

To remove unwanted portions of a video, you can set custom start and end
positions by adding a `ClippingConfiguration` to the `MediaItem`.  

### Kotlin

```kotlin
val clippingConfiguration = MediaItem.ClippingConfiguration.Builder()
    .setStartPositionMs(10_000) // start at 10 seconds
    .setEndPositionMs(20_000) // end at 20 seconds
    .build()
val mediaItem = MediaItem.Builder()
    .setUri(videoUri)
    .setClippingConfiguration(clippingConfiguration)
    .build()
```

### Java

```java
ClippingConfiguration clippingConfiguration = new MediaItem.ClippingConfiguration.Builder()
    .setStartPositionMs(10_000) // start at 10 seconds
    .setEndPositionMs(20_000) // end at 20 seconds
    .build();
MediaItem mediaItem = new MediaItem.Builder()
    .setUri(videoUri)
    .setClippingConfiguration(clippingConfiguration)
    .build();
```

### Use built-in effects

Media3 includes a number of built-in video effects for common transformations,
for example:

| Class | Effect |
|---|---|
| [`Presentation`](https://developer.android.com/reference/androidx/media3/effect/Presentation) | Scale the media item by resolution or aspect ratio |
| [`ScaleAndRotateTransformation`](https://developer.android.com/reference/androidx/media3/effect/ScaleAndRotateTransformation) | Scale the media item by a multiplier and/or rotate the media item |
| [`Crop`](https://developer.android.com/reference/androidx/media3/effect/Crop) | Crop the media item to a smaller or larger frame |
| [`OverlayEffect`](https://developer.android.com/reference/androidx/media3/effect/OverlayEffect) | Add a [text](https://developer.android.com/reference/androidx/media3/effect/TextOverlay) or [image](https://developer.android.com/reference/androidx/media3/effect/DrawableOverlay) overlay on top of the media item |

For audio effects, you can add a sequence of
[`AudioProcessor`](https://developer.android.com/reference/androidx/media3/common/audio/AudioProcessor)
instances that will transform the raw (PCM) audio data. For example, you can use
a [`ChannelMixingAudioProcessor`](https://developer.android.com/reference/androidx/media3/common/audio/ChannelMixingAudioProcessor)
to mix and scale audio channels.

To use these effects, create an instance of the effect or audio processor, build
an instance of `Effects` with the audio and video effects you want to apply to
the media item, then add the `Effects` object to an `EditedMediaItem`.  

### Kotlin

```kotlin
val channelMixingProcessor = ChannelMixingAudioProcessor()
val rotateEffect = ScaleAndRotateTransformation.Builder().setRotationDegrees(60f).build()
val cropEffect = Crop(-0.5f, 0.5f, -0.5f, 0.5f)

val effects = Effects(listOf(channelMixingProcessor), listOf(rotateEffect, cropEffect))

val editedMediaItem = EditedMediaItem.Builder(mediaItem)
    .setEffects(effects)
    .build()
```

### Java

```java
ChannelMixingAudioProcessor channelMixingProcessor = new ChannelMixingAudioProcessor();
ScaleAndRotateTransformation rotateEffect = new ScaleAndRotateTransformation.Builder()
    .setRotationDegrees(60f)
    .build();
Crop cropEffect = new Crop(-0.5f, 0.5f, -0.5f, 0.5f);

Effects effects = new Effects(
    ImmutableList.of(channelMixingProcessor),
    ImmutableList.of(rotateEffect, cropEffect)
);

EditedMediaItem editedMediaItem = new EditedMediaItem.Builder(mediaItem)
    .setEffects(effects)
    .build();
```

### Create custom effects

By extending the effects included in Media3, you can create custom effects
specific to your use cases. In the following example, use subclass
`MatrixTransformation` to zoom the video into filling the frame over the first
second of playback:  

### Kotlin

```kotlin
val zoomEffect = MatrixTransformation { presentationTimeUs ->
    val transformationMatrix = Matrix()
    // Set the scaling factor based on the playback position
    val scale = min(1f, presentationTimeUs / 1_000f)
    transformationMatrix.postScale(/* x */ scale, /* y */ scale)
    transformationMatrix
}

val editedMediaItem = EditedMediaItem.Builder(inputMediaItem)
    .setEffects(Effects(listOf(), listOf(zoomEffect))
    .build()
```

### Java

```java
MatrixTransformation zoomEffect = presentationTimeUs -> {
    Matrix transformationMatrix = new Matrix();
    // Set the scaling factor based on the playback position
    float scale = min(1f, presentationTimeUs / 1_000f);
    transformationMatrix.postScale(/* x */ scale, /* y */ scale);
    return transformationMatrix;
};

EditedMediaItem editedMediaItem = new EditedMediaItem.Builder(inputMediaItem)
    .setEffects(new Effects(ImmutableList.of(), ImmutableList.of(zoomEffect)))
    .build();
```

To further customize the behavior of an effect, implement a
[`GlShaderProgram`](https://developer.android.com/reference/androidx/media3/effect/GlShaderProgram). The
`queueInputFrame()` method is used to process input frames. For example, to
leverage the machine learning capabilities of
[MediaPipe](https://developers.google.com/mediapipe), you can use a
MediaPipe [`FrameProcessor`](https://github.com/google/mediapipe/tree/master/mediapipe/java/com/google/mediapipe/components/FrameProcessor.java)
to send each frame through a MediaPipe graph. See an example of this in the
[Transformer demo app](https://github.com/androidx/media/tree/release/demos/transformer).

### Preview effects

With [ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer), you can preview the effects
added to a media item before starting the export process. Using the same
`Effects` object as for the `EditedMediaItem`, call `setVideoEffects()` on your
ExoPlayer instance.  

### Kotlin

```kotlin
val player = ExoPlayer.builder(context)
    .build()
    .also { exoPlayer ->
        exoPlayer.setMediaItem(inputMediaItem)
        exoPlayer.setVideoEffects(effects)
        exoPlayer.prepare()
    }
```

### Java

```java
ExoPlayer player = new ExoPlayer.builder(context).build();
player.setMediaItem(inputMediaItem);
player.setVideoEffects(effects);
exoPlayer.prepare();
```

You can also preview audio effects with ExoPlayer. When building your
`ExoPlayer` instance, pass in a custom `RenderersFactory` that configures the
player's audio renderers to output audio to an `AudioSink` that uses your
`AudioProcessor` sequence. In the example below, we do this by overriding the
`buildAudioSink()` method of a `DefaultRenderersFactory`.  

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context, object : DefaultRenderersFactory(context) {
    override fun buildAudioSink(
        context: Context,
        enableFloatOutput: Boolean,
        enableAudioTrackPlaybackParams: Boolean,
        enableOffload: Boolean
    ): AudioSink? {
        return DefaultAudioSink.Builder(context)
            .setEnableFloatOutput(enableFloatOutput)
            .setEnableAudioTrackPlaybackParams(enableAudioTrackPlaybackParams)
            .setOffloadMode(if (enableOffload) {
                     DefaultAudioSink.OFFLOAD_MODE_ENABLED_GAPLESS_REQUIRED
                } else {
                    DefaultAudioSink.OFFLOAD_MODE_DISABLED
                })
            .setAudioProcessors(arrayOf(channelMixingProcessor))
            .build()
        }
    }).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context, new DefaultRenderersFactory(context) {
        @Nullable
        @Override
        protected AudioSink buildAudioSink(
            Context context,
            boolean enableFloatOutput,
            boolean enableAudioTrackPlaybackParams,
            boolean enableOffload
        ) {
            return new DefaultAudioSink.Builder(context)
                .setEnableFloatOutput(enableFloatOutput)
                .setEnableAudioTrackPlaybackParams(enableAudioTrackPlaybackParams)
                .setOffloadMode(
                    enableOffload
                        ? DefaultAudioSink.OFFLOAD_MODE_ENABLED_GAPLESS_REQUIRED
                        : DefaultAudioSink.OFFLOAD_MODE_DISABLED)
                .setAudioProcessors(new AudioProcessor[]{channelMixingProcessor})
                .build();
        }
    }).build();
```

## Start a transformation

Lastly, create a `Transformer` to apply your edits and start exporting the
resulting media item.  

### Kotlin

```kotlin
val transformer = Transformer.Builder(context)
    .addListener(listener)
    .build()
transformer.start(editedMediaItem, outputPath)
```

### Java

```java
Transformer transformer = new Transformer.Builder(context)
    .addListener(listener)
    .build();
transformer.start(editedMediaItem, outputPath);
```

You can similarly cancel the export process if needed with
[`Transformer.cancel()`](https://developer.android.com/reference/androidx/media3/transformer/Transformer#cancel()).

### Check for progress updates

`Transformer.start` returns immediately and runs asynchronously. To query the
current progress of a transformation, call
[`Transformer.getProgress()`](https://developer.android.com/reference/androidx/media3/transformer/Transformer#getProgress(androidx.media3.transformer.ProgressHolder)).
This method takes a `ProgressHolder`, and if the progress state is available,
that is, if the method returns `PROGRESS_STATE_AVAILABLE`, then the provided
`ProgressHolder` will be updated with the current progress percentage.

You can also attach a
[listener](https://developer.android.com/reference/androidx/media3/transformer/Transformer.Listener)
to your `Transformer` to be notified about completion or error events.