---
title: https://developer.android.com/media/platform/mediaplayer
url: https://developer.android.com/media/platform/mediaplayer
source: md.txt
---

# About MediaPlayer

This document discusses the MediaPlayer APIs in the Android multimedia framework. However, the recommended approach for media is[Jetpack Media3](https://developer.android.com/media/media3), which includes[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer). To create a new app, use Jetpack Media3 instead of the MediaPlayer APIs.

The`MediaPlayer`APIs in the Android multimedia framework support playing a variety of common media types.
| **Note:** You can play back the audio data only to the standard output device. That is, the mobile device speaker or a Bluetooth headset. You cannot play sound files in the conversation audio during a call.

You can:

- Integrate audio, video, and images into your applications.
- Play audio or video from media files stored in your application's resources (raw resources).
- Play audio or video from standalone files in the file system.
- Play audio or video from a data stream arriving over a network connection.

| **Caution:** The recommended way to include media in your app is to use[Jetpack Media3](https://developer.android.com/media/media3), which includes[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer).

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app.[Read more](https://developer.android.com/media/media3)about it.

These pages cover topics relating to recording, storing, and playing back audio and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)