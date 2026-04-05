---
title: Create and configure a DefaultPreloadManager  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Create and configure a DefaultPreloadManager Stay organized with collections Save and categorize content based on your preferences.




This page describes how to create a [`DefaultPreloadManager`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager), which preloads
media content for your app based on the strategy you choose.

Preload managers based on the [`BasePreloadManager`](/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager) abstract class let you
rank content by the criteria you choose. This document explains how to use the
derived class `DefaultPreloadManager`, in which each media item is ranked with
an integer representing its location in a list (for example, its position in a
video carousel). The preload manager prioritizes loading the items based on how
close it is to the item the user is currently playing. That way, if a user moves
to another item, the new item can start playing right away.

There are three steps to creating an instance of `DefaultPreloadManager`:

* [Define a `TargetPreloadStatusControl`](#create-tpsc) which the preload manager can
  query to find out if the media item is ready to be loaded and how much to
  load.
* [Create the builder](#create-dpm) which you'll use to create the preload manager, and
  to create your app's `ExoPlayer` objects.
* Use the builder to create the preload manager by calling the builder's
  [`build()`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder#build()) method.

## Create a target preload status control

When you create the [`DefaultPreloadManager.Builder`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder), you'll pass it a
*target preload status control* object that you define. This object implements
the [`TargetPreloadStatusControl`](/reference/androidx/media3/exoplayer/source/preload/TargetPreloadStatusControl) interface. When the preload manager is
getting ready to preload media, it calls your status control's
[`getTargetPreloadStatus()`](/reference/androidx/media3/exoplayer/source/preload/TargetPreloadStatusControl#getTargetPreloadStatus(T)) method to find out how much content to load. The
status control can reply with one of these status codes:

* [`STAGE_SPECIFIED_RANGE_LOADED`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.PreloadStatus#STAGE_SPECIFIED_RANGE_LOADED()): The preload manager should load the
  content from the specified start position and for the specified duration
  (given in milliseconds).
* [`STAGE_TRACKS_SELECTED`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.PreloadStatus#STAGE_TRACKS_SELECTED()): The preload manager should load and process the
  content track's information, and select the tracks. The preload manager
  shouldn't start loading the content yet.
* [`STAGE_SOURCE_PREPARED`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.PreloadStatus#STAGE_SOURCE_PREPARED()): The preload manager should prepare the content
  source. For example, if the content's metadata is in a separate manifest
  file, the preload manager might fetch and parse that manifest.
* `null`: The preload manager shouldn't load any content or metadata for that
  media item.

You'll need to have a strategy for deciding how much content to load for each
media item. In this example, more content is loaded for items closest to the
item that's currently playing. If the user is playing content with index **n**,
the controller returns the following codes:

* Index **n+1** (the next media item): Load 3000 ms (3 seconds) from the
  default start position
* Index **n-1** (the previous media item): Load 1000 ms (1 second) from the
  default start position
* Other media items in the range **n-2** to **n+2**: Return
  `PreloadStatus.TRACKS_SELECTED`
* Other media items in the range **n-4** to **n+4**: Return
  `PreloadStatus.SOURCE_PREPARED`
* For all other media items, return `null`

```
class MyTargetPreloadStatusControl(var currentPlayingIndex: Int = 0) :
  TargetPreloadStatusControl<Int, DefaultPreloadManager.PreloadStatus> {

  override fun getTargetPreloadStatus(index: Int): DefaultPreloadManager.PreloadStatus {
    if (index - currentPlayingIndex == 1) { // next track
      // return a PreloadStatus that is labelled by STAGE_SPECIFIED_RANGE_LOADED and
      // suggest loading 3000ms from the default start position
      return DefaultPreloadManager.PreloadStatus.specifiedRangeLoaded(3000L)
    } else if (index - currentPlayingIndex == -1) { // previous track
      // return a PreloadStatus that is labelled by STAGE_SPECIFIED_RANGE_LOADED and
      // suggest loading 3000ms from the default start position
      return DefaultPreloadManager.PreloadStatus.specifiedRangeLoaded(3000L)
    } else if (abs(index - currentPlayingIndex) == 2) {
      // return a PreloadStatus that is labelled by STAGE_TRACKS_SELECTED
      return DefaultPreloadManager.PreloadStatus.PRELOAD_STATUS_TRACKS_SELECTED
    } else if (abs(index - currentPlayingIndex) <= 4) {
      // return a PreloadStatus that is labelled by STAGE_SOURCE_PREPARED
      return DefaultPreloadManager.PreloadStatus.PRELOAD_STATUS_SOURCE_PREPARED
    }
    return DefaultPreloadManager.PreloadStatus.PRELOAD_STATUS_NOT_PRELOADED
  }
}

PreloadManagerCreate.kt
```

#### Key points about the code

* You'll pass an instance of `MyTargetPreloadStatusControl` to the preload
  manager builder when you create it.
* `currentPlayingIndex` holds the index of whatever media item is currently
  playing. It's the app's job to keep that value up to date.
* When the preload manager is ready to load content, it calls
  `getTargetPreloadStatus` and passes the ranking information you specified
  for that corresponding media item. In the case of `DefaultPreloadManager`,
  that ranking information is an integer, specifying the item's position in a
  carousel. The method chooses what code to return by comparing that index
  with the index of the item that's currently selected.

## Create the preload manager

To create your preload manager, you need a [`DefaultPreloadManager.Builder`](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder).
That builder is configured with the current context and the app's target preload
status control. The builder also provides setter methods which you can use to
set the preload manager's custom components.

Besides using the builder to create the preload manager, you'll also use it to
create the [`ExoPlayer`](/media/media3/exoplayer) objects your app uses to play the content.

**Note:** You can only use a `DefaultPreloadManager.Builder` to create a single
`DefaultPreloadManager`. If you try to create a second preload manager with the
same builder, it throws an exception, even if you've [released the first preload
manager](/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#release).

```
val targetPreloadStatusControl = MyTargetPreloadStatusControl()
val preloadManagerBuilder = DefaultPreloadManager.Builder(context, targetPreloadStatusControl)
val preloadManager = preloadManagerBuilder.build()

PreloadManagerCreate.kt
```

#### Key points about the code

* `MyTargetPreloadStatusControl` is the class you defined in [Create a target
  preload status control](#create-tpsc).
* You'll use the same `DefaultPreloadManager.Builder` to create the
  `ExoPlayer` objects that will play content managed by that preload manager.