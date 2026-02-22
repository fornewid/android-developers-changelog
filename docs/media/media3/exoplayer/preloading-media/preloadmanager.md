---
title: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager
url: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager
source: md.txt
---

The Media3 library provides a preload manager to help you show media faster to
users in your app. The preload manager loads content from media before the user
starts playing it. That way, when the user changes to a different piece of
content, it can start playing faster--the preloaded content can start playing
while the rest of the content is loaded for playback.

Media3 provides an abstract class, [`BasePreloadManager`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager), which can be
customized to implement whatever strategy you might have for prioritizing
content. This document set explains how to use an implementation of
`BasePreloadManager` that's also provided in the Media3 library:
[`DefaultPreloadManager`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager), which assumes media is in a one-dimensional list
(like a playlist or carousel), and prioritizes media items based on how close
they are to the media that's currently playing.

The documentation covers the following topics:

- [Preload manager concepts](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/concepts)
- [Create a preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create)
- [Manage and play content](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play)