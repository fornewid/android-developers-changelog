---
title: https://developer.android.com/media/media3/inspector/extract-frames
url: https://developer.android.com/media/media3/inspector/extract-frames
source: md.txt
---

The[`FrameExtractor`](https://developer.android.com/reference/androidx/media3/inspector/FrameExtractor)class provides an efficient way to extract decoded frames from a[`MediaItem`](https://developer.android.com/reference/androidx/media3/common/MediaItem).

Common use cases include:

- **Generating thumbnails**: Creating high-quality thumbnails for a video gallery or seek bar.
- **Video editing previews**: Displaying precise frame previews in an editor timeline, allowing users to seek through the content and visualize frames accurately.
- **Applying transformations**like scaling, cropping, or rotation directly during extraction, avoiding a separate post-processing step.
- **Content analysis**: Extracting frames at intervals to send to an analysis pipeline for tasks like scene detection, object recognition, or quality control.

## Overview

Using`FrameExtractor`is a two-step process:

1. **Build the extractor** : Create an instance using`FrameExtractor.Builder`. Pass a`Context`and the`MediaItem`that you want to inspect to the builder. You can also chain[configuration methods](https://developer.android.com/reference/androidx/media3/inspector/FrameExtractor.Builder)on the`Builder`for advanced settings.
2. **Extract frames** : Call[`getFrame()`](https://developer.android.com/reference/androidx/media3/inspector/FrameExtractor#getFrame(long))to extract a frame at a specific timestamp or[`getThumbnail()`](https://developer.android.com/reference/androidx/media3/inspector/FrameExtractor#getThumbnail())to request a representative thumbnail. These methods are**asynchronous** and return a`ListenableFuture`. Hence, the complex decoding work doesn't block the main thread.

**Important:** `FrameExtractor`instances must be accessed from a single application thread.  

### Kotlin

    suspend fun extractFrame(context: Context, mediaItem: MediaItem) {
        try {
            // 1. Build the frame extractor.
            // `FrameExtractor` implements `AutoCloseable`, so wrap it in
            // a Kotlin `.use` block, which calls `close()` automatically.
            FrameExtractor.Builder(context, mediaItem).build().use { extractor ->
                // 2. Extract frames asynchronously.
                val frame = extractor.getFrame(5000L).await()
                val thumbnail = extractor.thumbnail.await()
                handleFrame(frame, thumbnail)
            }
        } catch (e: Exception) {
            Log.e(TAG, "Exception: $e")
        }
    }

### Java

    public void extractFrame(Context context, MediaItem mediaItem) {
        // 1. Build the frame extractor.
        // `FrameExtractor` implements `AutoCloseable`, so use try-with-resources
        // so that the resources are automatically released.
        try (FrameExtractor frameExtractor = new FrameExtractor.Builder(context, mediaItem).build()) {
            // 2. Extract frames asynchronously.
            ListenableFuture<FrameExtractor.Frame> frameFuture = frameExtractor.getFrame(5000L);
            ListenableFuture<FrameExtractor.Frame> thumbnailFuture = frameExtractor.getThumbnail();

            ListenableFuture<List<Object>> allFutures = Futures.allAsList(frameFuture, thumbnailFuture);
            Futures.addCallback(allFutures, new FutureCallback<>() {
                @Override
                public void onSuccess(List<Object> result) {
                    handleFrame(Futures.getUnchecked(frameFuture), Futures.getUnchecked(thumbnailFuture));
                }

                @Override
                public void onFailure(@NonNull Throwable t) {
                    handleFailure(t);
                }
            }, MoreExecutors.directExecutor());
        }
    }