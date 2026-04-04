---
title: Multi-asset editing  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/transformer/multi-asset
source: html-scrape
---

Media3 Transformer is actively under development and we are looking to hear from you! We welcome your feedback, feature requests and bug reports in the [issue tracker](https://github.com/androidx/media/issues). Follow the [ExoPlayer blog](https://medium.com/google-exoplayer) for the latest updates.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Multi-asset editing Stay organized with collections Save and categorize content based on your preferences.



Using Transformer, you can combine multiple media assets, such as videos,
images, and audio files to create a `Composition`.

## Exporting a Composition

To apply [transformations](/media/media3/transformer/transformations)
(such as effects or trimming edits) to a `MediaItem`, you should create an
[`EditedMediaItem`](/reference/androidx/media3/transformer/EditedMediaItem)
to represent the asset that has the transformations applied to it.

`EditedMediaItem` objects can then be concatenated together to create an
[`EditedMediaItemSequence`](/reference/androidx/media3/transformer/EditedMediaItemSequence).
For example, you can create an `EditedMediaItemSequence` with two edited
videos. Items inside an `EditedMediaItemSequence` are ordered sequentially and
don't overlap in time.

A `Composition` is the combination of one or more `EditedMediaItemSequence`
objects. All `EditedMediaItemSequence` objects in the `Composition` are mixed
together, allowing you to combine video and audio assets.

`Composition` objects can be exported using Transformer.

Here is an example of creating and exporting a video asset that consists of two
edited video clips, overlaid with an audio track:

### Kotlin

```
val video1 = EditedMediaItem.Builder(MediaItem.fromUri(video1Uri)).build()

val video2 = EditedMediaItem.Builder(MediaItem.fromUri(video2Uri)).build()

val videoSequence =
  EditedMediaItemSequence.Builder(setOf(C.TRACK_TYPE_AUDIO, C.TRACK_TYPE_VIDEO))
    .addItems(video1, video2)
    .build()

val backgroundAudio = EditedMediaItem.Builder(MediaItem.fromUri(audioUri)).build()

val backgroundAudioSequence =
  EditedMediaItemSequence.Builder(setOf(C.TRACK_TYPE_AUDIO))
    .addItem(backgroundAudio)
    .setIsLooping(true) // Loop audio track through duration of videoSequence
    .build()

val composition = Composition.Builder(videoSequence, backgroundAudioSequence).build()

transformer.start(composition, filePath)

MultiAsset.kt
```

### Java

```
EditedMediaItem video1 = new EditedMediaItem.Builder(MediaItem.fromUri(video1Uri)).build();

EditedMediaItem video2 = new EditedMediaItem.Builder(MediaItem.fromUri(video2Uri)).build();

EditedMediaItemSequence videoSequence =
    new EditedMediaItemSequence.Builder(ImmutableSet.of(C.TRACK_TYPE_AUDIO, C.TRACK_TYPE_VIDEO))
        .addItems(video1, video2)
        .build();

EditedMediaItem backgroundAudio =
    new EditedMediaItem.Builder(MediaItem.fromUri(audioUri)).build();

EditedMediaItemSequence backgroundAudioSequence =
    new EditedMediaItemSequence.Builder(ImmutableSet.of(C.TRACK_TYPE_AUDIO))
        .addItem(backgroundAudio)
        .setIsLooping(true) // Loop audio track through duration of videoSequence
        .build();

Composition composition =
    new Composition.Builder(videoSequence, backgroundAudioSequence).build();

transformer.start(composition, filePath);

MultiAsset.java
```

## Examples of supported use cases

This is a non-exhaustive list of use cases that the Transformer API
supports with Compositions:

* Sequentially combining audio, image, and video assets.
* Adding background audio to a video asset.
* Adding effects to a Composition.
* Tone mapping HDR input to SDR to generate better visual quality SDR output.

## Current limitations

Sequences within a Composition must meet the conditions outlined in
[`Transformer.start()`](/reference/androidx/media3/transformer/Transformer#start(androidx.media3.transformer.Composition,java.lang.String)).
Furthermore, the following operations are not yet supported when working with
Compositions:

* Crossfading video or audio tracks

## Feature requests

If you have any feature requests for the Transformer API, file an issue on the
[Media3 GitHub repository](https://github.com/androidx/media/issues).