---
title: https://developer.android.com/media/media3/transformer/multi-asset
url: https://developer.android.com/media/media3/transformer/multi-asset
source: md.txt
---

Using Transformer, you can combine multiple media assets, such as videos, images, and audio files to create a`Composition`.

## Exporting a Composition

To apply[transformations](https://developer.android.com/media/media3/transformer/transformations)(such as effects or trimming edits) to a`MediaItem`, you should create an[`EditedMediaItem`](https://developer.android.com/reference/androidx/media3/transformer/EditedMediaItem)to represent the asset that has the transformations applied to it.

`EditedMediaItem`objects can then be concatenated together to create an[`EditedMediaItemSequence`](https://developer.android.com/reference/androidx/media3/transformer/EditedMediaItemSequence). For example, you can create an`EditedMediaItemSequence`with two edited videos. Items inside an`EditedMediaItemSequence`are ordered sequentially and don't overlap in time.

A`Composition`is the combination of one or more`EditedMediaItemSequence`objects. All`EditedMediaItemSequence`objects in the`Composition`are mixed together, allowing you to combine video and audio assets.

`Composition`objects can be exported using Transformer.

Here is an example of creating and exporting a video asset that consists of two edited video clips, overlaid with an audio track:  

### Kotlin

```kotlin
val transformer = ... // Set up Transformer instance

val video1 = EditedMediaItem.Builder(
  MediaItem.fromUri(video1Uri))
  .build()

val video2 = EditedMediaItem.Builder(
  MediaItem.fromUri(video2Uri))
  .build()

val videoSequence = EditedMediaItemSequence.Builder(
  setOf(C.TRACK_TYPE_AUDIO, C.TRACK_TYPE_VIDEO))
  .addItems(video1, video2)
  .build()

val backgroundAudio = EditedMediaItem.Builder(
  MediaItem.fromUri(audioUri))
  .build()

val backgroundAudioSequence = EditedMediaItemSequence.Builder(
  setOf(C.TRACK_TYPE_AUDIO))
  .addItem(backgroundAudio)
  .setIsLooping(true)  // Loop audio track through duration of videoSequence
  .build()

val composition = Composition.Builder(
  videoSequence,
  backgroundAudioSequence)
  .build()

val filePath = ... // Provide file path to save Composition

transformer.start(composition, filePath)
```

### Java

```java
Transformer transformer = ... // Set up Transformer instance

EditedMediaItem video1 = new EditedMediaItem.Builder(
  MediaItem.fromUri(video1Uri))
  .build();

EditedMediaItem video2 = new EditedMediaItem.Builder(
  MediaItem.fromUri(video2Uri))
  .build();

EditedMediaItemSequence videoSequence = new EditedMediaItemSequence.Builder(
  ImmutableSet.of(C.TRACK_TYPE_AUDIO, C.TRACK_TYPE_VIDEO))
  .addItems(video1, video2)
  .build();

EditedMediaItem backgroundAudio = new EditedMediaItem.Builder(
  MediaItem.fromUri(audioUri))
  .build();

EditedMediaItemSequence backgroundAudioSequence = new EditedMediaItemSequence.Builder(
  ImmutableSet.of(C.TRACK_TYPE_AUDIO))
  .addItem(backgroundAudio)
  .setIsLooping(true) // Loop audio track through duration of videoSequence
  .build();

String filePath = ... // Provide file path to save Composition

Composition composition = new Composition.Builder(
  videoSequence,
  backgroundAudioSequence)
  .build();

transformer.start(composition, filePath);
```

<br />

## Examples of supported use cases

This is a non-exhaustive list of use cases that the Transformer API supports with Compositions:

- Sequentially combining audio, image, and video assets.
- Adding background audio to a video asset.
- Adding effects to a Composition.
- Tone mapping HDR input to SDR to generate better visual quality SDR output.

## Current limitations

Sequences within a Composition must meet the conditions outlined in[`Transformer.start()`](https://developer.android.com/reference/androidx/media3/transformer/Transformer#start(androidx.media3.transformer.Composition,java.lang.String)). Furthermore, the following operations are not yet supported when working with Compositions:

- Crossfading video or audio tracks

## Feature requests

If you have any feature requests for the Transformer API, file an issue on the[Media3 GitHub repository](https://github.com/androidx/media/issues).