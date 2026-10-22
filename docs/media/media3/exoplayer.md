---
title: https://developer.android.com/media/media3/exoplayer
url: https://developer.android.com/media/media3/exoplayer
source: md.txt
---

A media player is an app-level component that allows playback of video and audio
files. Such files can be stored locally or streamed over the Internet. Jetpack
Media3 provides a `Player` interface that defines basic functionality such as
the ability to play, pause, seek, and display track information.

`ExoPlayer` is the default implementation of this interface in Media3. Compared
to Android's `MediaPlayer` API, it adds additional conveniences such as support
for multiple streaming protocols, default audio and video renderers, and
components that handle media buffering. ExoPlayer is designed to be customized
and extended and can be updated through Play Store application updates.

> [!TIP]
> **Tip:** If you are new to ExoPlayer, check out the [Getting started](https://developer.android.com/media/media3/exoplayer/hello-world) page for an introduction to using ExoPlayer. If you already use the standalone ExoPlayer library, see the [migration guide](https://developer.android.com/media/media3/exoplayer/migration-guide) for instructions on moving to Media3.