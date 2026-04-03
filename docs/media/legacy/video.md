---
title: Video app overview  |  Legacy media APIs  |  Android Developers
url: https://developer.android.com/media/legacy/video
source: html-scrape
---

These guides discuss the MediaCompat APIs, which are no longer updated. We strongly recommend using the [Jetpack Media3](/guide/topics/media/media3) library instead.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Video app overview Stay organized with collections Save and categorize content based on your preferences.




A typical video player always displays its controls and video content while it's
running; it can't operate in the background or without a UI. Therefore, it's
appropriate to build your app as a single activity containing the UI, a player,
a media session, and a media controller:

![video player activity](/static/guide/topics/media/images/video-player-activity.png "video player activity")

**[Building a videoplayer activity](/guide/topics/media-apps/video-app/building-a-video-player-activity)**
:   How to create an activity that contains a media session and a media controller.

**[Media session callbacks](/guide/topics/media-apps/video-app/mediasession-callbacks)**
:   Describes how the media session callback methods manage the media session and other app components like notifications and broadcast receivers.

**[Compatible media transcoding](/guide/topics/media-apps/video-app/compatible-media-transcoding)**
:   Set up transcoding behavior, such as whether to automatically convert
    videos to AVC (H.264) when they are opened by an app that doesn't support
    the initial encoding format.