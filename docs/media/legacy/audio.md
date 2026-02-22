---
title: https://developer.android.com/media/legacy/audio
url: https://developer.android.com/media/legacy/audio
source: md.txt
---

# Audio app overview

The preferred architecture for an audio app is a client/server design. The client is an Activity in your app that includes a`MediaBrowser`, media controller, and the UI. The server is a`MediaBrowserService`containing the player and a media session.

![Audio activity and BrowserService](https://developer.android.com/static/guide/topics/media/images/audio-activity-and-service.png "audio-app")

A`MediaBrowserService`provides two main features:

- When you use a`MediaBrowserService`, other components and applications with a`MediaBrowser`can discover your service, create their own media controller, connect to your media session, and control the player. This is how Wear OS and Android Auto Applications gain access to your media application.
- It also provides an optional*browsing API*. Applications don't have to use this feature. The browsing API lets clients query the service and build out a representation of its content hierarchy, which might represent playlists, a media library, or some other kind of collection.

| **Note:** As is the case with media session and media controller, the recommended implementation of media browser services and media browsers are the classes`MediaBrowserServiceCompat`and`MediaBrowserCompat`, which are defined in the[media-compat support library](https://developer.android.com/topic/libraries/support-library/features.html#v4-media-compat). They replace earlier versions of the classes`MediaBrowserService`and`MediaBrowser`that were introduced in API 21. For brevity, the terms "MediaBrowserService" and "MediaBrowser" refer to instances of`MediaBrowserServiceCompat`and`MediaBrowserCompat`respectively.

**[Building a media browser service](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice)**
:   How to create a media browser service that contains a media session, manage client connections, and become a foreground service while playing audio.

**[Building a media browser client](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowser-client)**
:   How to create a media browser client activity that contains a UI and media controller, and connect and communicate with a media browser service.

**[Media session callbacks](https://developer.android.com/guide/topics/media-apps/audio-app/mediasession-callbacks)**
:   Describes how the media session callback methods manage the media session, media browser service, and other app components like notifications and broadcast receivers.

**[Universal Android Music Player Sample](https://github.com/android/uamp)**
:   This GitHub sample shows how to implement a media app that allows background playback of audio, and provides a media library that is exposed to other apps.