---
title: SmoothStreaming  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/smoothstreaming
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# SmoothStreaming Stay organized with collections Save and categorize content based on your preferences.




ExoPlayer supports SmoothStreaming with the FMP4 container format. Media streams
must be demuxed, meaning that video, audio, and text must be defined in distinct
StreamIndex elements in the SmoothStreaming manifest. The contained audio and
video sample formats must also be supported (see the
[sample formats](/media/media3/exoplayer/supported-formats#sample-formats) section for details).

| Feature | Supported | Comments |
| --- | --- | --- |
| **Containers** |  |  |
| FMP4 | YES | Demuxed streams only |
| **Closed captions/subtitles** |  |  |
| TTML | YES | Embedded in FMP4 |
| **Content protection** |  |  |
| PlayReady SL2000 | YES | Android TV only |
| **Live playback** |  |  |
| Regular live playback | YES |  |
| **Common Media Client Data (CMCD)** | YES | [Integration Guide](/guide/topics/media/exoplayer/cmcd) |

## Using MediaItem

To play a SmoothStreaming stream, you need to depend on the SmoothStreaming
module.

### Kotlin

```
implementation("androidx.media3:media3-exoplayer-smoothstreaming:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-exoplayer-smoothstreaming:1.10.0"
```

You can then create a `MediaItem` for a SmoothStreaming manifest URI and pass it
to the player.

### Kotlin

```
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(ssUri))
// Prepare the player.
player.prepare()

SmoothStreaming.kt
```

### Java

```
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(ssUri));
// Prepare the player.
player.prepare();

SmoothStreaming.java
```

If your URI doesn't end with `.ism/Manifest`, you can pass
`MimeTypes.APPLICATION_SS` to `setMimeType` of `MediaItem.Builder` to explicitly
indicate the type of the content.

ExoPlayer will automatically adapt between representations defined in the
manifest, taking into account both available bandwidth and device capabilities.

## Using SsMediaSource

For more customization options, you can create a `SsMediaSource` and pass it
directly to the player instead of a `MediaItem`.

### Kotlin

```
// Create a data source factory.
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSource.Factory()
// Create a SmoothStreaming media source pointing to a manifest uri.
val mediaSource: MediaSource =
  SsMediaSource.Factory(dataSourceFactory).createMediaSource(MediaItem.fromUri(ssUri))
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media source to be played.
player.setMediaSource(mediaSource)
// Prepare the player.
player.prepare()

SmoothStreaming.kt
```

### Java

```
// Create a data source factory.
DataSource.Factory dataSourceFactory = new DefaultHttpDataSource.Factory();
// Create a SmoothStreaming media source pointing to a manifest uri.
MediaSource mediaSource =
    new SsMediaSource.Factory(dataSourceFactory).createMediaSource(MediaItem.fromUri(ssUri));
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media source to be played.
player.setMediaSource(mediaSource);
// Prepare the player.
player.prepare();

SmoothStreaming.java
```

## Accessing the manifest

You can retrieve the current manifest by calling `Player.getCurrentManifest`.
For SmoothStreaming, you should cast the returned object to `SsManifest`. The
`onTimelineChanged` callback of `Player.Listener` is also called whenever
the manifest is loaded. This will happen once for on-demand content and
possibly many times for live content. The following code snippet shows how an app
can do something whenever the manifest is loaded.

### Kotlin

```
player.addListener(
  object : Player.Listener {
    override fun onTimelineChanged(timeline: Timeline, @TimelineChangeReason reason: Int) {
      val manifest = player.currentManifest
      if (manifest is SsManifest) {
        // Do something with the manifest.
      }
    }
  }
)

SmoothStreaming.kt
```

### Java

```
player.addListener(
    new Player.Listener() {
      @Override
      public void onTimelineChanged(
          Timeline timeline, @Player.TimelineChangeReason int reason) {
        Object manifest = player.getCurrentManifest();
        if (manifest != null) {
          SsManifest ssManifest = (SsManifest) manifest;
          // Do something with the manifest.
        }
      }
    });

SmoothStreaming.java
```

## Customizing playback

ExoPlayer provides multiple ways for you to tailor playback experience to your
app's needs. See the [Customization page](/guide/topics/media/exoplayer/customization) for examples.