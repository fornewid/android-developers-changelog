---
title: https://developer.android.com/media/media3/exoplayer/progressive
url: https://developer.android.com/media/media3/exoplayer/progressive
source: md.txt
---

Streams in the following container formats can be played directly by ExoPlayer.
The contained audio and video sample formats must also be supported (see the
[Sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats) section for details).
For image container and format support, see
[Images](https://developer.android.com/media/media3/exoplayer/images).

| Container format | Supported | Comments |
|---|---|---|
| MP4 | YES |   |
| M4A | YES |   |
| FMP4 | YES |   |
| WebM | YES |   |
| Matroska | YES |   |
| MP3 | YES | Some streams only seekable using constant bitrate seeking\*\* |
| Ogg | YES | Containing Vorbis, Opus and FLAC |
| WAV | YES |   |
| MPEG-TS | YES |   |
| MPEG-PS | YES |   |
| FLV | YES | Not seekable\* |
| ADTS (AAC) | YES | Only seekable using constant bitrate seeking\*\* |
| FLAC | YES | Using the [FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac) or the FLAC extractor in the [ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer)\*\*\* |
| AMR | YES | Only seekable using constant bitrate seeking\*\* |

\* Seeking is unsupported because the container does not provide metadata (for example,
a sample index) to allow a media player to perform a seek in an efficient way.
If seeking is required, we suggest using a more appropriate container format.

\*\* These extractors have `FLAG_ENABLE_CONSTANT_BITRATE_SEEKING` flags for
enabling approximate seeking using a constant bitrate assumption. This
functionality is not enabled by default. The simplest way to enable this
functionality for all extractors that support it is to use
`DefaultExtractorsFactory.setConstantBitrateSeekingEnabled`, as described
[here](https://developer.android.com/media/media3/exoplayer/customization#enabling-constant-bitrate-seeking).

\*\*\* The [FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac) extractor outputs raw audio, which can be handled
by the framework on all API levels. The [ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer) FLAC extractor outputs
FLAC audio frames and so relies on having a FLAC decoder (for example, a `MediaCodec`
decoder that handles FLAC (required from API level 27), or the
[FFmpeg library](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg) with FLAC enabled). The `DefaultExtractorsFactory` uses the
extension extractor if the application was built with the [FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac).
Otherwise, it uses the [ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer) extractor.

## Using MediaItem

To play a progressive stream, create a `MediaItem` with the media URI and pass
it to the player.

### Kotlin

```kotlin
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(progressiveUri))
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(progressiveUri));
// Prepare the player.
player.prepare();
```

## Using ProgressiveMediaSource

For more customization options, you can create a `ProgressiveMediaSource` and
pass it directly to the player instead of a `MediaItem`.

### Kotlin

```kotlin
// Create a data source factory.
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSource.Factory()
// Create a progressive media source pointing to a stream uri.
val mediaSource: MediaSource =
  ProgressiveMediaSource.Factory(dataSourceFactory)
    .createMediaSource(MediaItem.fromUri(progressiveUri))
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media source to be played.
player.setMediaSource(mediaSource)
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a data source factory.
DataSource.Factory dataSourceFactory = new DefaultHttpDataSource.Factory();
// Create a progressive media source pointing to a stream uri.
MediaSource mediaSource =
    new ProgressiveMediaSource.Factory(dataSourceFactory)
        .createMediaSource(MediaItem.fromUri(progressiveUri));
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media source to be played.
player.setMediaSource(mediaSource);
// Prepare the player.
player.prepare();
```

## Customizing playback

ExoPlayer provides multiple ways for you to tailor playback experience to your
app's needs. See the [Customization page](https://developer.android.com/guide/topics/media/exoplayer/customization) for examples.