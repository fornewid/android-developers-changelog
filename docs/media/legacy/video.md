---
title: https://developer.android.com/media/legacy/video
url: https://developer.android.com/media/legacy/video
source: md.txt
---

# Video app overview

A typical video player always displays its controls and video content while it's running; it can't operate in the background or without a UI. Therefore, it's appropriate to build your app as a single activity containing the UI, a player, a media session, and a media controller:

![video player activity](https://developer.android.com/static/guide/topics/media/images/video-player-activity.png "video player activity")

**[Building a videoplayer activity](https://developer.android.com/guide/topics/media-apps/video-app/building-a-video-player-activity)**
:   How to create an activity that contains a media session and a media controller.

**[Media session callbacks](https://developer.android.com/guide/topics/media-apps/video-app/mediasession-callbacks)**
:   Describes how the media session callback methods manage the media session and other app components like notifications and broadcast receivers.

**[Compatible media transcoding](https://developer.android.com/guide/topics/media-apps/video-app/compatible-media-transcoding)**
:   Set up transcoding behavior, such as whether to automatically convert videos to AVC (H.264) when they are opened by an app that doesn't support the initial encoding format.