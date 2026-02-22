---
title: https://developer.android.com/media/media3/inspector/extract-samples
url: https://developer.android.com/media/media3/inspector/extract-samples
source: md.txt
---

The[`MediaExtractorCompat`](https://developer.android.com/reference/androidx/media3/inspector/MediaExtractorCompat)class is a drop-in replacement for the platform's[`MediaExtractor`](https://developer.android.com/reference/android/media/MediaExtractor)class and provides identical APIs and functionality. It facilitates extraction of demuxed, typically encoded, media data from a data source.

It separates a container file (like an MP4 or MKV) into its individual*tracks* , such as video, audio, and subtitles. The extractor then reads the raw,*encoded data* from these tracks as a sequence of*samples*(for example, a single compressed video frame or block of audio) before they are sent to a decoder.

Common use cases include:

- **Transcoding** or**Remuxing**: Reading encoded samples from a track to either change the codec (transcoding) or repackage the streams into a new container (remuxing), such as converting an MP4 file to MKV.
- **Selective content extraction**: Isolating and saving a single track, such as extracting an audio stream from a video file.
- **Low-level debugging**: Inspecting individual samples to debug file corruption, timestamp issues, or other problems.
- **Building custom players**: For niche use cases, building a custom player with full control over the media pipeline.

## Overview

The following code sample shows how to use`MediaExtractorCompat`:  

### Kotlin

    fun extractSamples(context: Context, mediaPath: String) {
        val extractor = MediaExtractorCompat(context)
        try {
            // 1. Setup the extractor
            extractor.setDataSource(mediaPath)

            // Find and select available tracks
            for (i in 0 until extractor.trackCount) {
                val format = extractor.getTrackFormat(i)
                extractor.selectTrack(i)
            }

            // 2. Process samples
            val buffer = ByteBuffer.allocate(10 * 1024 * 1024)
            while (true) {
                // Read an encoded sample into the buffer.
                val bytesRead = extractor.readSampleData(buffer, 0)
                if (bytesRead < 0) break

                // Access sample metadata
                val trackIndex = extractor.sampleTrackIndex
                val presentationTimeUs = extractor.sampleTime
                val sampleSize = extractor.sampleSize

                extractor.advance()
            }
        } catch (e: IOException) {
            throw RuntimeException(e)
        } finally {
            // 3. Release the extractor
            extractor.release()
        }
    }

### Java

    public void extractSamples(Context context, String mediaPath) {
        MediaExtractorCompat extractor = new MediaExtractorCompat(context);
        try {
            // 1. Setup the extractor
            extractor.setDataSource(mediaPath);

            // Find and select available tracks
            for (int i = 0; i < extractor.getTrackCount(); i++) {
                MediaFormat format = extractor.getTrackFormat(i);
                extractor.selectTrack(i);
            }

            // 2. Process samples
            ByteBuffer buffer = ByteBuffer.allocate(10 * 1024 * 1024);
            while (true) {
                // Read an encoded sample into the buffer.
                int bytesRead = extractor.readSampleData(buffer, 0);
                if (bytesRead < 0) break;

                // Access sample metadata
                int trackIndex = extractor.getSampleTrackIndex();
                long presentationTimeUs = extractor.getSampleTime();
                long sampleSize = extractor.getSampleSize();

                extractor.advance();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            // 3. Release the extractor
            extractor.release();
        }
    }