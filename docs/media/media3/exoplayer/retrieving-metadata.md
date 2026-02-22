---
title: https://developer.android.com/media/media3/exoplayer/retrieving-metadata
url: https://developer.android.com/media/media3/exoplayer/retrieving-metadata
source: md.txt
---

## During playback

The metadata of the media can be retrieved during playback in multiple ways. The
most straightforward is to listen for the
`Player.Listener#onMediaMetadataChanged` event; this will provide a
[`MediaMetadata`](https://developer.android.com/reference/androidx/media3/common/MediaMetadata) object for use, which has fields such as `title` and
`albumArtist`. Alternatively, calling `Player#getMediaMetadata` returns the same
object.

### Kotlin

```kotlin
override fun onMediaMetadataChanged(mediaMetadata: MediaMetadata) {
  mediaMetadata.title?.let(::handleTitle)
}
```

### Java

```java
@Override
public void onMediaMetadataChanged(MediaMetadata mediaMetadata) {
  if (mediaMetadata.title != null) {
    handleTitle(mediaMetadata.title);
  }
}
```

If your app needs access to specific [`Metadata.Entry`](https://developer.android.com/reference/androidx/media3/common/Metadata.Entry) objects, then it
should listen to `Player.Listener#onMetadata` (for dynamic metadata delivered
during playback). Alternatively, if there is a need to look at static metadata,
this can be accessed through the `TrackSelections#getFormat`.
`Player#getMediaMetadata` is populated from both of these sources.

## Without playback

If playback is not needed, it is more efficient to use the
[`MetadataRetriever`](https://developer.android.com/reference/androidx/media3/inspector/MetadataRetriever) to extract the metadata because it avoids having to
create and prepare a player.

### Kotlin

```kotlin
try {
  MetadataRetriever.Builder(context, mediaItem).build().use { metadataRetriever ->
    val trackGroups = metadataRetriever.retrieveTrackGroups().await()
    val timeline = metadataRetriever.retrieveTimeline().await()
    val durationUs = metadataRetriever.retrieveDurationUs().await()
    handleMetadata(trackGroups, timeline, durationUs)
  }
} catch (e: IOException) {
  handleFailure(e)
}
```

### Java

```java
try (MetadataRetriever metadataRetriever =
    new MetadataRetriever.Builder(context, mediaItem).build()) {
  ListenableFuture<TrackGroupArray> trackGroupsFuture = metadataRetriever.retrieveTrackGroups();
  ListenableFuture<Timeline> timelineFuture = metadataRetriever.retrieveTimeline();
  ListenableFuture<Long> durationUsFuture = metadataRetriever.retrieveDurationUs();
  ListenableFuture<List<Object>> allFutures =
      Futures.allAsList(trackGroupsFuture, timelineFuture, durationUsFuture);
  Futures.addCallback(
      allFutures,
      new FutureCallback<List<Object>>() {
        @Override
        public void onSuccess(List<Object> result) {
          handleMetadata(
              Futures.getUnchecked(trackGroupsFuture),
              Futures.getUnchecked(timelineFuture),
              Futures.getUnchecked(durationUsFuture));
        }

        @Override
        public void onFailure(Throwable t) {
          handleFailure(t);
        }
      },
      executor);
}
```

## Motion photos

> [!NOTE]
> **Note:** For motion photo **playback** , see [Media Items](https://developer.android.com/media/media3/exoplayer/images#motion-photos) and for motion photo **format support** , see [Supported formats](https://developer.android.com/media/media3/exoplayer/supported-formats#images).

It is also possible to extract motion photo metadata, including the offsets and
lengths of the image and video parts of the file.

For motion photos, the `TrackGroupArray` obtained with the `MetadataRetriever`
contains a `TrackGroup` with a single `Format` enclosing a
[`MotionPhotoMetadata`](https://developer.android.com/reference/androidx/media3/extractor/metadata/MotionPhotoMetadata) metadata entry.

### Kotlin

```kotlin
0.until(trackGroups.length)
  .asSequence()
  .mapNotNull { trackGroups[it].getFormat(0).metadata }
  .filter { metadata -> metadata.length() == 1 }
  .map { metadata -> metadata[0] }
  .filterIsInstance<MotionPhotoMetadata>()
  .forEach(::handleMotionPhotoMetadata)
```

### Java

```java
for (int i = 0; i < trackGroups.length; i++) {
  TrackGroup trackGroup = trackGroups.get(i);
  Metadata metadata = trackGroup.getFormat(0).metadata;
  if (metadata != null && metadata.length() == 1) {
    Metadata.Entry metadataEntry = metadata.get(0);
    if (metadataEntry instanceof MotionPhotoMetadata) {
      MotionPhotoMetadata motionPhotoMetadata = (MotionPhotoMetadata) metadataEntry;
      handleMotionPhotoMetadata(motionPhotoMetadata);
    }
  }
}
```