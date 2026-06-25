---
title: https://developer.android.com/distribute/aep/aep-req-media-3
url: https://developer.android.com/distribute/aep/aep-req-media-3
source: md.txt
---

Integrate the Jetpack Media3 library as the standard for media playback,
sessions, editing, metadata, and frame extraction to ensure apps utilize
recommended APIs for handling complex media tasks across Android form factors.
Modernizing media architecture by migrating from legacy framework APIs (such as
MediaPlayer, MediaMuxer, and MediaExtractor) to the robust Jetpack Media3
library provides a unified, feature-rich toolkit that ensures consistent media
experiences.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Shouldn't use legacy Android framework APIs, including MediaPlayer, MediaExtractor, MediaMuxer, and MediaMetadataRetriever.
- If playback is a core user journey, the app must integrate media sessions for OS awareness and cross-device integration.
- If the app has an audio content library, it must expose content through MediaLibraryService and implement support for media resumption.

## Guideline applicability

This guideline applies to:

- Apps that support media (video or audio) playback or video editing.
- To all form factors on which the app is available.

## Exemptions

Apps can use an equivalent alternative framework that provides similar quality,
user capabilities, stability and compatibility across the ecosystem.
[Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration. To
qualify, the alternative implementation must meet the following benchmarks:

- On a fast network, the first video frame must be displayed within 500 ms of user initiation.
- Playback must remain smooth, with no visible frame drops or audible audio underruns during a 30-second window.
- The app must properly manage [audio focus](https://developer.android.com/media/optimize/audio-focus).
- The app must respond to hardware media keys, even when running in the background.
- If background playback is supported, the app must post a media-style notification and use a foreground service.
- If the app supports resuming playback, it must implement [media
  resumption](https://developer.android.com/media/media3/session/background-playback#resumption).
- Headphone disconnections must be handled gracefully. For example, pausing playback instead of switching to the speaker.
- Playback must continue without dropped frames when switching between device orientations.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Media3** feature. These resources are for your reference only and don't
contain additional program requirements.

- [Jetpack Media3](https://developer.android.com/media/media3)
- [Media3 ExoPlayer](https://developer.android.com/media/media3/exoplayer)
- [Control and advertise playback using a MediaSession](https://developer.android.com/media/media3/session/control-playback)
- [MediaExtractorCompat API](https://developer.android.com/reference/androidx/media3/inspector/MediaExtractorCompat)
- [MediaMuxerCompat API](https://developer.android.com/reference/androidx/media3/muxer/MediaMuxerCompat)
- [MetadataRetriever API](https://developer.android.com/reference/androidx/media3/inspector/MetadataRetriever)
- [FrameExtractor API](https://developer.android.com/reference/androidx/media3/inspector/frame/FrameExtractor)