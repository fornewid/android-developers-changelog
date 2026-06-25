---
title: https://developer.android.com/distribute/aep/aep-req-preload-caching
url: https://developer.android.com/distribute/aep/aep-req-preload-caching
source: md.txt
---

Implement predictive media caching to minimize playback start latency and
eliminate buffering pauses when switching between media items. This ensures
seamless, high-performance playback in scrollable media feeds, delivering a
premium user experience. Implementation through Jetpack Media3 is recommended.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Asset transitions must occur in less than 50 ms.

## Guideline applicability

This guideline applies to:

- Apps that include continuous or sequential video playback where the next video is predictable. For example, short-form video (SFV), linear playlists, or auto-playing lists.
- All form factors on which the app is available.

## Exemptions

The following exemptions apply for this guideline:

- Apps where the user must actively navigate to and select their next video from a distinct UI (such as a grid, list, or recommendation menu) after the current video completes.
- Apps where the core use case is live, peer-to-peer, or server-mediated streaming (such as chat apps and live-streaming apps). These videos are real-time and hence cannot be cached.
- Apps can use an equivalent alternative framework that provides similar quality, user capabilities, stability and compatibility across the ecosystem. [Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Preload Caching** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Introducing preloading with Media3](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html)
- [A deep dive into Media3's PreloadManager](https://android-developers.googleblog.com/2025/09/a-deep-dive-into-media3-preloadmanager.html)
- [Instagram and Facebook deliver instant playback with Media3](https://android-developers.googleblog.com/2026/03/instagram-and-facebook-deliver-instant.html)