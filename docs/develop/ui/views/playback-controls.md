---
title: Add media playback controls to your app  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/playback-controls
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add media playback controls to your app Stay organized with collections Save and categorize content based on your preferences.




If your app plays back audio and video, you must add UI components for
displaying media and controlling playback.

AndroidX Media3 offers a
[`PlayerView`](/reference/androidx/media3/ui/PlayerView) that displays playback
controls, video, subtitles, and album art during playback. To make it work
properly, connect `PlayerView` to a
[`Player`](/reference/androidx/media3/common/Player) instance such as
[`ExoPlayer`](/reference/androidx/media3/exoplayer/ExoPlayer).

To learn more about media playback controls, see the following documentation:

* [Media developer center](/media): Review best practices and step-by-step guides
  for writing a media app.
* [Audio and Video guide](/guide/topics/media/media3): Learn about AndroidX Media3.
* [Media3 ExoPlayer guide](/guide/topics/media/exoplayer) Develop a player.
* [Media3 UI guide](/guide/topics/media/ui/playerview) Browse details about the `PlayerView` and
  customization options.