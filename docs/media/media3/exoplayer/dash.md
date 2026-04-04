---
title: DASH  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/dash
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# DASH Stay organized with collections Save and categorize content based on your preferences.




ExoPlayer supports DASH with multiple container formats. Media streams must be
demuxed, meaning that video, audio, and text must be defined in distinct
`AdaptationSet` elements in the DASH manifest (CEA-608 is an exception as
described in the table below). The contained audio and video sample formats must
also be supported (see the
[sample formats](/media/media3/exoplayer/supported-formats#sample-formats) section for details).

| Feature | Supported | Comments |
| --- | --- | --- |
| **Containers** |  |  |
| FMP4 | YES | Demuxed streams only |
| WebM | YES | Demuxed streams only |
| Matroska | YES | Demuxed streams only |
| MPEG-TS | NO | No support planned |
| **Closed captions /** **subtitles** |  |  |
| TTML | YES | Raw, or embedded in FMP4 according to ISO/IEC 14496-30 |
| WebVTT | YES | Raw, or embedded in FMP4 according to ISO/IEC 14496-30 |
| CEA-608 | YES | Embedded in FMP4 when signalled using SCTE Accessibility descriptors |
| CEA-708 | YES | Embedded in FMP4 when signalled using SCTE Accessibility descriptors |
| **Metadata** |  |  |
| EMSG metadata | YES | Embedded in FMP4 |
| **Content protection** |  |  |
| Widevine | YES | "cenc" scheme: API 19+; "cbcs" scheme: API 25+ |
| PlayReady SL2000 | YES | Android TV, "cenc" scheme only |
| ClearKey | YES | API 21+, "cenc" scheme only |
| **Ad insertion** |  |  |
| Multi-period playback | YES |  |
| Server-guided ad insertion (xlinks) | NO |  |
| IMA server-side and client-side ads | YES | [Ad insertion guide](/media/media3/exoplayer/ad-insertion) |
| **Live playback** |  |  |
| Regular live playback | YES |  |
| Ultra low-latency CMAF live playback | YES |  |
| **Common Media Client Data** **(CMCD)** | YES | [CMCD integration guide](/media/media3/exoplayer/cmcd) |

## Using MediaItem

To play a DASH stream, you need to depend on the DASH module.

### Kotlin

```
implementation("androidx.media3:media3-exoplayer-dash:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-exoplayer-dash:1.10.0"
```

You can then create a `MediaItem` for a DASH MPD URI and pass it to the player.

### Kotlin

```
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(dashUri))
// Prepare the player.
player.prepare()

Dash.kt
```

### Java

```
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(dashUri));
// Prepare the player.
player.prepare();

Dash.java
```

If your URI doesn't end with `.mpd`, you can pass `MimeTypes.APPLICATION_MPD`
to `setMimeType` of `MediaItem.Builder` to explicitly indicate the type of the
content.

ExoPlayer will automatically adapt between representations defined in the
manifest, taking into account both available bandwidth and device capabilities.

## Using DashMediaSource

For more customization options, you can create a `DashMediaSource` and pass it
directly to the player instead of a `MediaItem`.

### Kotlin

```
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSource.Factory()
// Create a dash media source pointing to a dash manifest uri.
val mediaSource: MediaSource =
  DashMediaSource.Factory(dataSourceFactory).createMediaSource(MediaItem.fromUri(dashUri))
// Create a player instance which gets an adaptive track selector by default.
val player = ExoPlayer.Builder(context).build()
// Set the media source to be played.
player.setMediaSource(mediaSource)
// Prepare the player.
player.prepare()

Dash.kt
```

### Java

```
DataSource.Factory dataSourceFactory = new DefaultHttpDataSource.Factory();
// Create a dash media source pointing to a dash manifest uri.
MediaSource mediaSource =
    new DashMediaSource.Factory(dataSourceFactory)
        .createMediaSource(MediaItem.fromUri(dashUri));
// Create a player instance which gets an adaptive track selector by default.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media source to be played.
player.setMediaSource(mediaSource);
// Prepare the player.
player.prepare();

Dash.java
```

## Accessing the manifest

You can retrieve the current manifest by calling `Player.getCurrentManifest`.
For DASH you should cast the returned object to `DashManifest`. The
`onTimelineChanged` callback of `Player.Listener` is also called whenever
the manifest is loaded. This will happen once for a on-demand content, and
possibly many times for live content. The following code snippet shows how an app
can do something whenever the manifest is loaded.

### Kotlin

```
player.addListener(
  object : Player.Listener {
    override fun onTimelineChanged(
      timeline: Timeline,
      @Player.TimelineChangeReason reason: Int,
    ) {
      val manifest = player.currentManifest
      if (manifest is DashManifest) {
        // Do something with the manifest.
      }
    }
  }
)

Dash.kt
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
          DashManifest dashManifest = (DashManifest) manifest;
          // Do something with the manifest.
        }
      }
    });

Dash.java
```

## Customizing playback

ExoPlayer provides multiple ways for you to tailor playback experience to your
app's needs. See the [Customization page](/guide/topics/media/exoplayer/customization) for examples.