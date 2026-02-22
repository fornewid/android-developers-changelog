---
title: https://developer.android.com/social-and-messaging/guides/media-playback/basic-better-best
url: https://developer.android.com/social-and-messaging/guides/media-playback/basic-better-best
source: md.txt
---

# Take your media display and playback to the next level — basic, better, and best

This guide charts the optimal progression of a media playback-focused app from a likely starting place to best-in-class. It's designed to help you think about scaling your app over time, and what features to implement when. While every media consumption app is different, consider these recommendations to achieve a best-in-class experience.

## Basic media display and playback

A basic media display and playback app provides users with a foundational experience, which may include doing the following:

- Offer an in-app media player using with playback controls, using[formats](https://developer.android.com/guide/topics/media/media-formats)that are supported across the Android ecosystem, ideally using[Media3s](https://developer.android.com/guide/topics/media/media3)[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer).
- Use the latest version of the[Jetpack Media3](https://developer.android.com/guide/topics/media/media3)library.
- Use optimized server-generated thumbnails as well as[best practices for locally-generated ones](https://developer.android.com/social-and-messaging/guides/media-thumbnails), and cache them locally.
- Invest in[accessibility](https://developer.android.com/guide/topics/ui/accessibility/principles#media-content).

## Better media display and playback

A better media display and playback app leverages premium device hardware and updated platform features, to:

- Implement a[`MediaSession`](https://developer.android.com/guide/topics/media/media3/getting-started/mediasession)--- made easy with[Media3s](https://developer.android.com/guide/topics/media/media3)[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)--- to enable playback integration across different apps, system components, and devices.
- Use[best practices for sharing video](https://developer.android.com/media/optimize/sharing),[transcoding](https://developer.android.com/media/media3/transformer/transformations#transcode)if necessary.
- Support[sharing multiple pieces of content](https://developer.android.com/training/sharing/send#share-multiple-content)at the same time.
- Enable[picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)for video and audio playback so users can multitask.
- Enable support for[UltraHDR](https://developer.android.com/media/grow/ultra-hdr-display)images.
- Play[HDR](https://developer.android.com/media/grow/hdr-playback)video.
- Support playback to[Cast](https://developers.google.com/cast/docs/developers)devices.
- Add an[app widget](https://developer.android.com/develop/ui/views/appwidgets/overview)so users can get see what friends are up to and search from their home screen.

## Best media display and playback

A best-in-class media display and playback app gives users access to advanced features that really make the app stand out, such as:

- Check to see if images contain a[gain-map](https://developer.android.com/guide/topics/media/platform/hdr-image-format#gain_map-generation), and strategically use[`setColorMode()`](https://developer.android.com/reference/android/view/Window#setColorMode(int))to[`ActivityInfo.COLOR_MODE_HDR`](https://developer.android.com/reference/android/content/pm/ActivityInfo#COLOR_MODE_HDR)to optimize for content display and battery life.
- Optimize for foldables by supporting the[`HALF_OPENED`state](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables#foldable_postures)
- Ensure[design](https://developer.android.com/design/ui)consistency with the platform.
- Implement[Cast Connect](https://developers.google.com/cast/docs/android_tv_receiver)so users can cast to your[Android TV](https://developer.android.com/training/tv)app.
- Use[Performance Class](https://developer.android.com/topic/performance/performance-class)to adapt your user experience to match device capabilities.