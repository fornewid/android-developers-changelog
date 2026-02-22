---
title: https://developer.android.com/training/cars/media
url: https://developer.android.com/training/cars/media
source: md.txt
---

This guide assumes you have a media app that plays audio on a phone and that your media app conforms to Android media app architecture. You also learn what your app needs from`MediaBrowserService`and`MediaSession`to run on Android Auto or AAOS. When you complete the core media infrastructure, you can add support for Android Auto and AAOS to your media app.
| **Caution:** Google takes driver distraction seriously. Your app must meet specific design requirements before it can be listed on Google Play for Android Auto or AAOS. By adhering to these requirements, you can make it more straightforward to build and test your app. To learn more, see[Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=media).

## Contents

These pages detail how to work with the media apps:

- [Configure the manifest file](https://developer.android.com/training/cars/media/configure-manifest)
- [Enable playback controls](https://developer.android.com/training/cars/media/enable-playback)
- [Support voice actions](https://developer.android.com/training/cars/media/voice-actions)
- [Implement distraction safeguards](https://developer.android.com/training/cars/media/distraction-safeguards)
- [Handle errors](https://developer.android.com/training/cars/media/errors)

## Create audio media apps

If your app focuses on playing audio media, use the tools described here. You can create media apps for cars in one of two ways:

1. Use`MediaBrowserService`and a`MediaSession`to create an app that Android Auto and AAOS can connect to. This allows the infotainment screen interface to render media browsing and playback user interfaces optimized for in-car use.

   *or*
2. Use the[Cars App Library](https://developer.android.com/training/cars/apps)templates to build apps with a customized media browsing and playback experience, including custom actions. To learn more, see[Build a templated media app](https://developer.android.com/training/cars/apps/media).

   | **Note:** Templated media apps are supported only on Android Auto.

| **Caution:** Aside from[voice guidance audio for navigation apps](https://developer.android.com/training/cars/apps/navigation#voice-guidance)and the media apps described here, in-app media playback while driving is**not**permitted.

This guide assumes you have a media app that plays audio on a phone and that your media app conforms to Android[media app architecture](https://developer.android.com/guide/topics/media-apps/media-apps-overview). This guide describes the required components of a`MediaBrowserService`and`MediaSession`needed by your app to be compatible with Android Auto or AAOS. After you complete the core media infrastructure, you can[add support for Android Auto](https://developer.android.com/training/cars/media/auto)and[add support for AAOS](https://developer.android.com/training/cars/media/automotive-os)to your media app.

## Create video media apps

If the primary content provided by your app is video, see:

- [Build video apps for Android Automotive OS](https://developer.android.com/training/cars/parked/video)
- [Build parked apps for cars](https://developer.android.com/training/cars/parked)

## Before you start

Be sure to consult:

- [Android media API documentation](https://developer.android.com/guide/topics/media-apps/media-apps-overview)
- Design guidance:[Create media apps](https://developers.google.com/cars/design/create-apps/app-types/media)
- Terminology:[Key terms and concepts](https://developer.android.com/training/cars/media#terms-concepts)

## Learn key terms and concepts

These terms are used in relation to building media apps for cars:

Media browser
:   An API used by media apps to discover media browser services and to display their content. Android Auto and AAOS use a media browser to find your app's media browser service.

Media browser service
:   An Android service implemented by your media app that complies with the[`MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat)API. Your app uses this service to expose content. We also support[\`MediaLibrarySerice'](https://developer.android.com/training/cars/media/configure-manifest).

Media item

:   The media browser organizes content in a tree of[`MediaItem`](https://developer.android.com/training/cars/parked/video)objects. A media item can have either or both of these flags. A media item that can be browsed for**and**played operates like a playlist. You can select the item to play all of its descendants, or you can browse its descendants.

- `FLAG_PLAYABLE`indicates that the item is a leaf on the content tree. The item represents a single sound stream, such as a song on an album, a chapter in an audio book, or an episode of a podcast.

- `FLAG_BROWSABLE`indicates that the item is a node on the content tree and has descendants. For example, the item represents an album, and its descendants are the songs on the album.

## See additional resources

For additional information, see:

- [Universal Media Player sample](https://github.com/googlesamples/android-UniversalMusicPlayer)
- [Audio app overview](https://developer.android.com/training/managing-audio)
- [ExoPlayer overview](https://developer.android.com/guide/topics/media/exoplayer)