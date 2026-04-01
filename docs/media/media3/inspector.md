---
title: Media3 Inspector  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/inspector
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media3 Inspector Stay organized with collections Save and categorize content based on your preferences.



The `androidx.media3.inspector` module lets you *inspect* media files by
extracting information from them. You don't need to instantiate a full player,
which makes the module ideal for *non-playback* scenarios.

This module includes the following APIs:

* [`MetadataRetriever`](/reference/androidx/media3/inspector/MetadataRetriever): Retrieves high-level
  [**metadata**](/media/media3/inspector/retrieve-metadata).
* [`FrameExtractor`](/reference/androidx/media3/inspector/frame/FrameExtractor): Extracts individual [**decoded video frames and
  thumbnails**](/media/media3/inspector/extract-frames).
* [`MediaExtractorCompat`](/reference/androidx/media3/inspector/MediaExtractorCompat): Extracts raw,
  [**encoded media samples**](/media/media3/inspector/extract-samples).

## Getting started

Add the dependencies for the required modules:

### Kotlin

```
implementation("androidx.media3:media3-inspector:1.10.0")
implementation("androidx.media3:media3-inspector-frame:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-inspector:1.10.0"
implementation "androidx.media3:media3-inspector-frame:1.10.0"
```

If you are migrating your app from platform APIs, these features provide
equivalent functionality:

| **Functionality** | **Platform API** | **Media3 API** |
| --- | --- | --- |
| Metadata retrieval | [`MediaMetadataRetriever`](/reference/android/media/MediaMetadataRetriever) | [`MetadataRetriever`](/reference/androidx/media3/inspector/MetadataRetriever) |
| Frame extraction | [`MediaMetadataRetriever`](/reference/android/media/MediaMetadataRetriever) | [`FrameExtractor`](/reference/androidx/media3/inspector/frame/FrameExtractor) |
| Sample extraction | [`MediaExtractor`](/reference/android/media/MediaExtractor) | [`MediaExtractorCompat`](/reference/androidx/media3/inspector/MediaExtractorCompat) |