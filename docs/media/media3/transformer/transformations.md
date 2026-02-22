---
title: https://developer.android.com/media/media3/transformer/transformations
url: https://developer.android.com/media/media3/transformer/transformations
source: md.txt
---

clips, apply video effects, and optimize exports.
keywords_public: Media3, Transformer, transcode, video editing, trimming, audio
processing, Android media


## Transcode between formats

You can specify the output audio and video formats you want to produce when
building Transformer. For example, the following code shows how
to configure Transformer to output H.264/AVC video and AAC audio:

### Kotlin

```kotlin
Transformer.Builder(context)
    .setVideoMimeType(MimeTypes.VIDEO_H264)
    .setAudioMimeType(MimeTypes.AUDIO_AAC)
    .build()
```

### Java

```java
new Transformer.Builder(context)
    .setVideoMimeType(MimeTypes.VIDEO_H264)
    .setAudioMimeType(MimeTypes.AUDIO_AAC)
    .build();
```

<br />

If the input media format already matches the configurations for audio
or video, Transformer automatically switches to *transmuxing*, that is, copying
the compressed samples from the input container to the output container without
modification. This avoids the computational cost and potential quality loss of
decoding and re-encoding in the same format.

## Remove audio or video

Remove audio or video using `EditedMediaItem.Builder`, for example:

### Kotlin

```kotlin
EditedMediaItem.Builder(inputMediaItem).setRemoveAudio(true).build()
```

### Java

```java
new EditedMediaItem.Builder(inputMediaItem).setRemoveAudio(true).build();
```

<br />

## Trim a clip

You can remove any media outside specified start and end timestamps by setting
the clipping configuration on the input media item. For example, to produce a
clip containing only the media between 10 seconds and 20 seconds:

### Kotlin

```kotlin
val inputMediaItem = MediaItem.Builder()
    .setUri(uri)
    .setClippingConfiguration(
        MediaItem.ClippingConfiguration.Builder()
            .setStartPositionMs(10_000)
            .setEndPositionMs(20_000)
            .build())
    .build()
```

### Java

```java
MediaItem inputMediaItem =
    new MediaItem.Builder()
        .setUri(uri)
        .setClippingConfiguration(
            new MediaItem.ClippingConfiguration.Builder()
                .setStartPositionMs(10_000)
                .setEndPositionMs(20_000)
                .build())
        .build();
```

<br />

## MP4 edit lists

For faster trimming, Transformer supports MP4 edit lists, allowing for more
efficient "trim-only" edits without full video re-transcoding. This method
utilizes existing encoded samples and a "pre-roll" within the edit list, which
instructs the player to begin playback at a specific point, effectively skipping
the undesired initial segment.

To make trim-only edits significantly faster, call
`experimentalSetMp4EditListTrimEnabled(true)`.

### Kotlin

```kotlin
Transformer.Builder(context)
    .experimentalSetMp4EditListTrimEnabled(true)
    .build()
```

### Java

```java
new Transformer.Builder(context)
    .experimentalSetMp4EditListTrimEnabled(true)
    .build();
```


It is important to note that not all media players support a "pre-roll" position.
This means that when such a player is used, the file will start playback from the
absolute beginning of the encoded sample, regardless of any edit list
information that might specify a different starting point.
| **Caution:** Trimming video often implies permanent removal of unwanted sections. However, using edit lists creates a privacy risk: users might unknowingly share sensitive, "deleted" information "hidden" by the "pre-roll" position.

## Optimizing trims

To reduce the latency of trimming the beginning of a video, enable trim
optimization.

### Kotlin

```kotlin
Transformer.Builder(context)
    .experimentalSetTrimOptimizationEnabled(true)
    .build()
```

### Java

```java
new Transformer.Builder(context)
    .experimentalSetTrimOptimizationEnabled(true)
    .build();
```

<br />

This speeds up the export by decoding and re-encoding as little of the video as
possible, then stitching the re-encoded data with the rest of the original
video. The optimization relies on being able to stitch part of the input file
with newly-encoded output, which means that the encoder's output format and the
input format must be compatible. So, for example, if the file was originally
produced on a device with a different encoder implementation then it's likely
that it won't be possible to apply the optimization.
For the optimization to succeed, the encoder provided to Transformer via the
`EncoderFactory` must have a level and profile compatible with the input format.

This optimization only works with single-asset MP4 input with no effects except
no op video effects and rotations divisible by 90 degrees. If the optimization
fails, Transformer automatically falls back to normal export, and reports the
outcome of the optimization in `ExportResult.OptimizationResult`.

We are validating this functionality and expect it to become non-experimental
in a later release.

## Video edits

`EditedMediaItems` have lists of audio processors and video effects to apply in
order. The library includes video effect implementations for common use cases,
or you can write custom effects and pass them in when building edited media
items.

You can rescale media, which can be useful to save on processing resources or
bandwidth when dealing with very high resolution input, such as 4k or 8k video.
For example, to scale proportionally to 480 pixels high:

### Kotlin

```kotlin
EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(Effects(
        /* audioProcessors= */ listOf(),
        /* videoEffects= */ listOf(Presentation.createForHeight(480))
    )).build()
```

### Java

```java
new EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(new Effects(
        /* audioProcessors= */ ImmutableList.of(),
        /* videoEffects= */ ImmutableList.of(Presentation.createForHeight(480))))
    .build();
```

<br />

Alternatively, you can scale by a given factor, for example, to halve the size:

### Kotlin

```kotlin
val editedMediaItem = EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(Effects(
        /* audioProcessors= */ listOf(),
        /* videoEffects= */ listOf(
            ScaleAndRotateTransformation.Builder().setScale(.5f, .5f).build())
    )).build()
```

### Java

```java
new EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(new Effects(
        /* audioProcessors= */ ImmutableList.of(),
        /* videoEffects= */ ImmutableList.of(
            new ScaleAndRotateTransformation.Builder().setScale(.5f, .5f).build())))
    .build();
```

<br />

You can configure rotation in the same way:

### Kotlin

```kotlin
EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(Effects(
        /* audioProcessors= */ listOf(),
        /* videoEffects= */ listOf(
            ScaleAndRotateTransformation.Builder()
                .setRotationDegrees(90f)
                .build())
    )).build()
```

### Java

```java
new EditedMediaItem.Builder(MediaItem.fromUri(uri))
    .setEffects(new Effects(
        /* audioProcessors= */ ImmutableList.of(),
        /* videoEffects= */ ImmutableList.of(
            new ScaleAndRotateTransformation.Builder().setRotationDegrees(90f).build())))
    .build();
```

<br />

### Custom video effects

The `Effects` constructor accepts a list of audio and video effects to apply.
Internally, Transformer's effects framework converts the list of video effects
into a sequence of GL shader programs that are applied in order. In some cases,
the effects framework is able to apply multiple effects with one shader program.
For example, one shader program can apply multiple consecutive matrix
transformations, which improves efficiency and quality.

Video effects are also supported for preview in ExoPlayer, using
`ExoPlayer.setVideoEffects`. For an example of how to use this API, check out
the [effect demo app](https://github.com/androidx/media/tree/release/demos/effect).

The [demo app](https://developer.android.com/media/media3/transformer/demo-application) includes examples of custom video effects.

## Image input

Transformer supports image inputs by treating them as static video clips. To
configure an image as an input source, follow these steps:

- Create a `MediaItem` using `MediaItem.Builder`. Specify the display
  duration of the image in the output video by calling `setImageDurationMs`.

- Construct an `EditedMediaItem` wrapping the `MediaItem`. Specify the target
  frame rate for the generated video stream using
  `EditedMediaItem.Builder#setFrameRate`.

The following example demonstrates how to configure an image input to generate a
5-second video at 30 frames per second:

### Kotlin

```kotlin
val imageMediaItem = MediaItem.Builder()
    .setUri(imageUri)
    .setImageDurationMs(5000) // 5 seconds
    .build()

val editedImageItem = EditedMediaItem.Builder(imageMediaItem)
    .setFrameRate(30) // 30 frames per second
    .build()
```

### Java

```java
MediaItem imageMediaItem = new MediaItem.Builder()
    .setUri(imageUri)
    .setImageDurationMs(5000) // 5 seconds
    .build();

EditedMediaItem editedImageItem = new EditedMediaItem.Builder(imageMediaItem)
    .setFrameRate(30) // 30 frames per second
    .build();
```

<br />

## Audio edits

Audio effects are implemented by applying a sequence of `AudioProcessor`
instances to raw (PCM) audio. ExoPlayer supports passing audio processors to the
`DefaultAudioSink.Builder`, which allows previewing audio edits.