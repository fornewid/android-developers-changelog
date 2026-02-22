---
title: https://developer.android.com/media/grow/good-better-best
url: https://developer.android.com/media/grow/good-better-best
source: md.txt
---

# Take your app from good to better to best

This article charts the optimal progression of a media app from a likely starting place to best-in-class. It's designed to help you think about scaling your app over time, and what features to implement when. While every media app is different, consider these recommendations to achieve a best-in-class app.

## Basic media app

A basic media app provides users with a foundational experience, which may include:

- Offering in-app content browsing and discovery
- Offering an in-app media player with playback controls
- Using[formats](https://developer.android.com/guide/topics/media/media-formats)that are supported across the Android ecosystem
- Implementing best practices, such as using the latest version of the[Jetpack Media3](https://developer.android.com/guide/topics/media/media3)library
- Investing in[accessibility](https://developer.android.com/guide/topics/ui/accessibility)

## Better media app

A better media app starts to grow its reach to meet users where they are and increase engagement. You may also start to consider more holistic improvements in your app, which may include:

- Using[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)for advanced and customized playback features, such as using native platform[digital rights management](https://developer.android.com/guide/topics/media/exoplayer/drm)capabilities to protect content
- Implementing a[`MediaSession`](https://developer.android.com/guide/topics/media/media3/getting-started/mediasession)to enable playback integration with external Android clients
- Adding support for form factors such as[system media controls](https://developer.android.com/media/implement/surfaces/mobile)on mobile and large screen devices,[Wear OS](https://developer.android.com/training/wearables/apps/audio),[Android TV](https://developer.android.com/training/tv/playback), and[Android Auto](https://developer.android.com/training/cars/media)
- Integrating with media resumption features, such as[Watch Next](https://developer.android.com/training/tv/discovery/watch-next-add-programs)on Android TV and[media controls](https://developer.android.com/media/implement/surfaces/mobile)on mobile and large screen devices
- Enabling[picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)so users can multi-task
- Improving[accessibility](https://developer.android.com/guide/topics/ui/accessibility)for all, such as by adding[subtitles](https://developer.android.com/guide/topics/media/exoplayer/media-items#sideloading_subtitle_tracks)
- Supporting playback to[Cast](https://developers.google.com/cast/docs/developers)devices
- Using[Google Play Billing](https://developer.android.com/google/play/billing)to handle subscriptions

## Best-in-class media app

A best-in-class media app builds on the previous recommendations to create a seamless multidevice experience for users, which may include:

- Leveraging premium device capabilities by streaming[HDR](https://developer.android.com/media/grow/hdr-playback)and[spatial audio](https://developer.android.com/media/grow/spatial-audio)content when possible, and gracefully falling-back as necessary
- Enabling[media downloading](https://developer.android.com/guide/topics/media/exoplayer/downloading-media)and offline playback
- Optimizing for foldables by supporting the[`HALF_OPENED`state](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables#foldable_postures)
- Testing and refining voice assistant integrations, such as with[Google Assistant](https://developer.android.com/media/implement/assistant)
- Investing in performance on lower-powered devices, for example by leveraging[performance class](https://developer.android.com/topic/performance/performance-class)
- Supporting[Better Together](https://www.android.com/better-together)use cases, such as[Nearby Connections](https://developers.google.com/nearby/connections/overview)
- Ensuring[design](https://developer.android.com/design/ui)consistency with the platform
- Investing in seamless identity across surfaces such as[One Tap](https://developers.google.com/identity/one-tap/android/overview)and[account linking](https://developers.google.com/identity/account-linking)
- Offering[frictionless subscriptions](https://www.youtube.com/watch?v=ARuf97ncE4w)
- Implementing[Cast Connect](https://developers.google.com/cast/docs/android_tv_receiver)so users can cast to your native Android TV app