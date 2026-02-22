---
title: https://developer.android.com/media/media3/exoplayer/media-sources
url: https://developer.android.com/media/media3/exoplayer/media-sources
source: md.txt
---

In ExoPlayer, every piece of media is represented by a `MediaItem`. However
internally, the player needs `MediaSource` instances to play the content. The
player creates these from media items using a `MediaSource.Factory`.

By default the player uses a `DefaultMediaSourceFactory`, which can create
instances of the following content `MediaSource` implementations:

- `DashMediaSource` for [DASH](https://developer.android.com/guide/topics/media/exoplayer/dash).
- `SsMediaSource` for [SmoothStreaming](https://developer.android.com/guide/topics/media/exoplayer/smoothstreaming).
- `HlsMediaSource` for [HLS](https://developer.android.com/guide/topics/media/exoplayer/hls).
- `ProgressiveMediaSource` for [regular media files](https://developer.android.com/guide/topics/media/exoplayer/progressive).
- `RtspMediaSource` for [RTSP](https://developer.android.com/guide/topics/media/exoplayer/rtsp).

`DefaultMediaSourceFactory` can also create more complex media sources depending
on the properties of the corresponding media items. This is described in more
detail on the
[Media items page](https://developer.android.com/guide/topics/media/exoplayer/media-items).

For apps that need media source setups that are not supported by the
default configuration of the player, there are several options for
customization.

## Customizing media source creation

When building the player, a `MediaSource.Factory` can be injected. For example,
if an app wants to insert ads and use a `CacheDataSource.Factory` to support
caching, an instance of `DefaultMediaSourceFactory` can be configured to match
these requirements and injected during player construction:

### Kotlin

```kotlin
val mediaSourceFactory: MediaSource.Factory =
  DefaultMediaSourceFactory(context)
    .setDataSourceFactory(cacheDataSourceFactory)
    .setLocalAdInsertionComponents(adsLoaderProvider, playerView)
val player = ExoPlayer.Builder(context).setMediaSourceFactory(mediaSourceFactory).build()
```

### Java

```java
MediaSource.Factory mediaSourceFactory =
    new DefaultMediaSourceFactory(context)
        .setDataSourceFactory(cacheDataSourceFactory)
        .setLocalAdInsertionComponents(adsLoaderProvider, /* adViewProvider= */ playerView);
ExoPlayer player =
    new ExoPlayer.Builder(context).setMediaSourceFactory(mediaSourceFactory).build();
```

The
[`DefaultMediaSourceFactory` JavaDoc](https://developer.android.com/reference/androidx/media3/exoplayer/source/DefaultMediaSourceFactory)
describes the available options in more detail.

It's also possible to inject a custom `MediaSource.Factory` implementation, for
example to support creation of a custom media source type. The factory's
`createMediaSource(MediaItem)` will be called to create a media source for each
media item that is
[added to the playlist](https://developer.android.com/guide/topics/media/exoplayer/playlists).

## Media source based playlist API

The [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) interface defines additional playlist methods that accept
media sources rather than media items. This makes it possible to bypass the
player's internal `MediaSource.Factory` and pass media source instances to the
player directly:

### Kotlin

```kotlin
// Set a list of media sources as initial playlist.
exoPlayer.setMediaSources(listOfMediaSources)
// Add a single media source.
exoPlayer.addMediaSource(anotherMediaSource)

// Can be combined with the media item API.
exoPlayer.addMediaItem(/* index= */ 3, MediaItem.fromUri(videoUri))

exoPlayer.prepare()
exoPlayer.play()
```

### Java

```java
// Set a list of media sources as initial playlist.
exoPlayer.setMediaSources(listOfMediaSources);
// Add a single media source.
exoPlayer.addMediaSource(anotherMediaSource);

// Can be combined with the media item API.
exoPlayer.addMediaItem(/* index= */ 3, MediaItem.fromUri(videoUri));

exoPlayer.prepare();
exoPlayer.play();
```

## Advanced media source composition

ExoPlayer provides multiple `MediaSource` implementations to modify and compose
other `MediaSource` instances. These are most useful in cases where multiple
customizations have to be combined and none of the simpler setup paths are
sufficient.

- `ClippingMediaSource`: Allows to clip media to a specified timestamp range. If this is the only modification, it's preferable to use [`MediaItem.ClippingConfiguration`](https://developer.android.com/guide/topics/media/exoplayer/media-items#clipping-media) instead.
- `FilteringMediaSource`: Filters available tracks to the specified types, for example, just exposing the video track from a file that contains both audio and video. If this is the only modification, it's preferable to use [track selection parameters](https://developer.android.com/guide/topics/media/exoplayer/track-selection#disabling-track) instead.
- `MergingMediaSource`: Merges multiple media sources to play in parallel. In almost all cases, it's advisable to call the constructor with `adjustPeriodTimeOffsets` and `clipDurations` set to true to ensure all sources start and end at the same time. If this modification is done to add side-loaded subtitles, it's preferable to use [`MediaItem.SubtitleConfiguration`](https://developer.android.com/guide/topics/media/exoplayer/media-items#sideloading-subtitle) instead.
- `ConcatenatingMediaSource2`: Merges multiple media source to play consecutively. The user-visible media structure exposes a single `Timeline.Window`, meaning that it looks like a single item. If this modification is done to play multiple items that are not supposed to look like a single one, it's preferable to use the [playlist API](https://developer.android.com/guide/topics/media/exoplayer/playlists) methods like `Player.addMediaItem` instead.
- `SilenceMediaSource`: Generates silence for a specified duration that is useful to fill gaps.
- `AdsMediaSource`: Extends a media source with client-side ad insertion capabilities. Refer to the [ad insertion guide](https://developer.android.com/guide/topics/media/exoplayer/ad-insertion) for details.
- `ServerSideAdInsertionMediaSource`: Extends a media source with server-side ad insertion capabilities. Refer to the [ad insertion guide](https://developer.android.com/guide/topics/media/exoplayer/ad-insertion) for details.