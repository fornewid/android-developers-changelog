---
title: https://developer.android.com/media/media3/inspector
url: https://developer.android.com/media/media3/inspector
source: md.txt
---

The `androidx.media3.inspector` module lets you *inspect* media files by
extracting information from them. You don't need to instantiate a full player,
which makes the module ideal for *non-playback* scenarios.

This module includes the following APIs:

- [`MetadataRetriever`](https://developer.android.com/reference/androidx/media3/inspector/MetadataRetriever): Retrieves high-level [**metadata**](https://developer.android.com/media/media3/inspector/retrieve-metadata).
- [`FrameExtractor`](https://developer.android.com/reference/androidx/media3/inspector/frame/FrameExtractor): Extracts individual [**decoded video frames and
  thumbnails**](https://developer.android.com/media/media3/inspector/extract-frames).
- [`MediaExtractorCompat`](https://developer.android.com/reference/androidx/media3/inspector/MediaExtractorCompat): Extracts raw, [**encoded media samples**](https://developer.android.com/media/media3/inspector/extract-samples).

## Getting started

Add the dependencies for the required modules:

### Kotlin

    implementation("androidx.media3:media3-inspector:1.9.2")
    implementation("androidx.media3:media3-inspector-frame:1.9.2")

### Groovy

    implementation "androidx.media3:media3-inspector:1.9.2"
    implementation "androidx.media3:media3-inspector-frame:1.9.2"

If you are migrating your app from platform APIs, these features provide
equivalent functionality:

| **Functionality** | **Platform API** | **Media3 API** |
|---|---|---|
| Metadata retrieval | [`MediaMetadataRetriever`](https://developer.android.com/reference/android/media/MediaMetadataRetriever) | [`MetadataRetriever`](https://developer.android.com/reference/androidx/media3/inspector/MetadataRetriever) |
| Frame extraction | [`MediaMetadataRetriever`](https://developer.android.com/reference/android/media/MediaMetadataRetriever) | [`FrameExtractor`](https://developer.android.com/reference/androidx/media3/inspector/frame/FrameExtractor) |
| Sample extraction | [`MediaExtractor`](https://developer.android.com/reference/android/media/MediaExtractor) | [`MediaExtractorCompat`](https://developer.android.com/reference/androidx/media3/inspector/MediaExtractorCompat) |