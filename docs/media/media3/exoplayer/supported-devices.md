---
title: https://developer.android.com/media/media3/exoplayer/supported-devices
url: https://developer.android.com/media/media3/exoplayer/supported-devices
source: md.txt
---

# Supported devices

The minimum Android versions required for core ExoPlayer use cases are:

|                  Use case                  | Android version | API level  |
|--------------------------------------------|-----------------|------------|
| Audio playback                             | 5.0             | 21         |
| Audio playback (using offload)             | 10              | 29         |
| Video playback                             | 5.0             | 21         |
| Video playback (with effects)              | 5.0             | 21         |
| Video playback (HDR)                       | 7.0             | 24         |
| DASH (no DRM)                              | 5.0             | 21         |
| DASH (Widevine CENC; "cenc" scheme)        | 5.0             | 21         |
| DASH (Widevine CENC; "cbcs" scheme)        | 7.1             | 25         |
| DASH (ClearKey; "cenc" scheme)             | 5.0             | 21         |
| SmoothStreaming (no DRM)                   | 4.4             | 19         |
| SmoothStreaming (PlayReady; "cenc" scheme) | Android TV      | Android TV |
| HLS (no DRM)                               | 5.0             | 21         |
| HLS (AES-128 encryption)                   | 5.0             | 21         |
| HLS (Widevine CENC; "cenc" scheme)         | 4.4             | 19         |
| HLS (Widevine CENC; "cbcs" scheme)         | 7.1             | 25         |

For a given use case, we aim to support ExoPlayer on all Android devices that satisfy the minimum version requirement. Known device-specific issues are listed on the[Media3 GitHub issue tracker](https://github.com/androidx/media/labels/bug%3A%20device%20specific)or the[legacy ExoPlayer GitHub issue tracker](https://github.com/google/ExoPlayer/labels/bug%3A%20device%20specific).

## Emulators

Some Android emulators don't properly implement components of Android's media stack, and as a result don't support ExoPlayer. This is an issue with the emulator, not with ExoPlayer. Android's official emulator ("Virtual Devices" in Android Studio) supports ExoPlayer provided the system image has an API level of at least 23. System images with earlier API levels don't support ExoPlayer. The level of support provided by third-party emulators varies. Issues running ExoPlayer on third-party emulators should be reported to the developer of the emulator rather than to the ExoPlayer team. Where possible, we recommend testing media apps on physical devices rather than emulators.