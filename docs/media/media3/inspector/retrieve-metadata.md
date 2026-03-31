---
title: Retrieve metadata  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/inspector/retrieve-metadata
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Retrieve metadata Stay organized with collections Save and categorize content based on your preferences.



The [`MetadataRetriever`](/reference/androidx/media3/inspector/MetadataRetriever) retrieves information (such as duration, video
resolution, codecs, available tracks, and sampling rates) from a [`MediaItem`](/reference/androidx/media3/common/MediaItem)
without playback.

**Note:** `MetadataRetriever` is intended for extracting metadata from media formats
supported by Media3 players, such as ExoPlayer, for playback. It is not designed
to be a general-purpose metadata extractor for non-playback formats, such as
standalone images. To extract properties like height, width, and rotation from
images, use [`ExifInterface`](/reference/androidx/exifinterface/media/ExifInterface).

Common use cases include:

* **[Retrieving motion photo metadata](/media/media3/exoplayer/retrieving-metadata#motion-photos)**: including the offsets and lengths of
  the image and video parts of the file.
* **Building a media library**: Populating a [`MediaLibraryService`](/reference/androidx/media3/session/MediaLibraryService) with rich
  [`MediaItem`](/reference/androidx/media3/common/MediaItem) details (like duration and title) to serve a full media
  catalog to clients like Android Auto.
* **Prefetching UI details**: Fetching information like video resolution or
  duration to prepare the UI before playback begins.
* **Validating media files**: Checking if a file contains the required audio
  or video tracks or specific metadata before processing it.

## Overview

Using `MetadataRetriever` is a two-step process:

1. **Build the retriever**: Create an instance using
   `MetadataRetriever.Builder`. Pass a `Context` and the `MediaItem` that you
   want to inspect to the builder. For advanced use cases, such as custom
   networking or caching, you can also supply a custom [`MediaSource.Factory`](/reference/androidx/media3/exoplayer/source/MediaSource.Factory).
2. **Retrieve metadata**: Call methods like [`retrieveDurationUs()`](/reference/androidx/media3/inspector/MetadataRetriever#retrieveDurationUs()),
   [`retrieveTimeline()`](/reference/androidx/media3/inspector/MetadataRetriever#retrieveTimeline()), or [`retrieveTrackGroups()`](/reference/androidx/media3/inspector/MetadataRetriever#retrieveTrackGroups()) to fetch the required
   information. These methods are **asynchronous**, returning a
   `ListenableFuture` so that network or I/O operations don't block the main
   thread.

### Kotlin

```
suspend fun retrieveMetadata(context: Context, mediaItem: MediaItem) {
  try {
    // 1. Build the retriever.
    // `MetadataRetriever` implements `AutoCloseable`, so wrap it in
    // a Kotlin `.use` block, which calls `close()` automatically.
    MetadataRetriever.Builder(context, mediaItem).build().use { retriever ->
      // 2. Retrieve metadata asynchronously.
      val trackGroups = retriever.retrieveTrackGroups().await()
      val timeline = retriever.retrieveTimeline().await()
      val durationUs = retriever.retrieveDurationUs().await()
      handleMetadata(trackGroups, timeline, durationUs)
    }
  } catch (e: Exception) {
    handleFailure(e)
  }
}

RetrieveMetadata.kt
```

### Java

```
public void retrieveMetadata(Context context, MediaItem mediaItem) {
  // 1. Build the retriever.
  // `MetadataRetriever` implements `AutoCloseable`, so use try-with-resources
  // so that the resources are automatically released.
  try (MetadataRetriever retriever = new MetadataRetriever.Builder(context, mediaItem).build()) {
    // 2. Retrieve metadata asynchronously.
    ListenableFuture<TrackGroupArray> trackGroupsFuture = retriever.retrieveTrackGroups();
    ListenableFuture<Timeline> timelineFuture = retriever.retrieveTimeline();
    ListenableFuture<Long> durationUsFuture = retriever.retrieveDurationUs();

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
        directExecutor());
  }
}

RetrieveMetadata.java
```