---
title: Media3 Cast overview  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/cast
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media3 Cast overview Stay organized with collections Save and categorize content based on your preferences.



The Media3 [`cast`](/reference/androidx/media3/cast/package-summary) module extends your media playback experience to
Cast devices. It lets your app cast content to [compatible devices](/media/media3/cast/create-castplayer#get-device),
such as TVs and speakers. The [sender](https://developers.google.com/cast/glossary#sender) app acts as a remote controller for media
playback on the [receiver](https://developers.google.com/cast/glossary#receiver) device. This module integrates with the [Jetpack
Media3](/guide/topics/media/media3) library, so you can use the same `Player` interface and UI
components for both local and remote playback.

## Media3 CastPlayer

The `CastPlayer` is a media player API included in Media3 that supports both
local and remote media playback. It implements the `Player` interface to manage
playback, simplifying the integration of casting into your media experience.

[Go to Media3 CastPlayer](/media/media3/cast/create-castplayer)

## Other Cast integrations

The Cast SDK overview explains how to integrate Cast with other platforms, such
as building a receiver app or integrating with the web sender SDK.

[Explore Cast SDK](https://developers.google.com/cast/docs/developers)