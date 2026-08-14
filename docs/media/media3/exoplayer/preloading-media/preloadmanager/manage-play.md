---
title: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play
url: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play
source: md.txt
---

This page describes how to use a preload manager to manage video content. By
using a preload manager, you can give the user a better experience; when the
user switches from one media item to another, the playback starts faster because
the manager has already loaded some of the content.

This page covers the following topics:

- [Add media items to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items)
- [Fetch and play media](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#fetch-play)
- [Remove items from the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#remove)
- [Release the preload manager when you're done with it](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#release)

## Add media items to the preload manager

You have to tell the preload manager about each media item it will track.
For example, if your app has a carousel of videos, you'd add them to the
preload manager. Depending on your use case, you might add all the videos, or
just all the videos near the video that's currently playing. You can also add
new items to the preload manager later.

To do this, use a batch addition method like [`addMediaItems`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/or%20%5B%60addMediaSources%60%5D). Alternatively, you can call [`add`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#add(androidx.media3.common.MediaItem,T)) (or
`addMediaSource`) to add media items individually. However, adding media items
individually does not automatically trigger preloading. When using individual
methods, you must explicitly call [`invalidate`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#invalidate()) once you're done
adding items to tell the preload manager to update priorities and start
preloading.


```kotlin
val initialMediaItems = pullMediaItemsFromService(count = 20)
val rankingDataList = initialMediaItems.indices.toList()
preloadManager.addMediaItems(initialMediaItems, rankingDataList)
```

<br />

#### Key points about the code

- This snippet shows how to initially populate the preload manager in batch mode after you've created it. You can call [`addMediaItems`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#addMediaItems(java.util.List,java.util.List)) to add items to an existing, populated preload manager.
- In this snippet, `pullMediaItemsFromService()` is the app's logic to fetch the list of content to play. The code calls that method to fetch a list of up to 20 items.
- `preloadManager` is the `DefaultPreloadManager` created in [Create a
  `DefaultPreloadManager`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create).
- `rankingData` is a value the preload manager uses to determine the priority of each media item. For `DefaultPreloadManager`, `rankingData` is an integer representing the item's position in the carousel. The preload manager determines the priority by how far each item is from the item that's currently playing.

### Fetch and play media

When the user advances to a new media item, you need to get the media item from
the preload manager. If the preload manager has loaded any of the content, the
content plays faster than it would have if you hadn't used the preload manager.
If the preload manager hasn't loaded content from that item yet, the content
plays normally.

You also need to update the current playing index on the preload manager by
calling `setCurrentPlayingIndex`, which enables the preload manager to determine
the priorities of future preloading operations.


```kotlin
// When a media item is about to be displayed on the screen
val mediaSource = preloadManager.getMediaSource(mediaItem)
if (mediaSource != null) {
  player.setMediaSource(mediaSource)
} else {
  // If the mediaSource is null, its mediaItem hasn't been added to the preload
  // manager yet. Send it directly to the player when it's about to play.
  player.setMediaItem(mediaItem)
}
player.prepare()

// When the media item is being displayed at the center of the screen ("in focus")
player.play()
// Update the current playing index to let the preload manager know where the user
// is in the carousel/pagination/list.
preloadManager.setCurrentPlayingIndex(currentIndex)
```

<br />

#### Key points about the code

- `player` is the Media3 `ExoPlayer` the app is using to play the content. You must create that player by calling [`DefaultPreloadManager.Builder.buildExoPlayer()`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder#buildExoPlayer()) on the same builder you used to create the preload manager.
- When the user switches to a new media item, the app calls `getMediaSource()` to get the media source from the preload manager. This must be a `mediaItem` you have [already added to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items). It's okay if the preload manager hasn't already started loading the content; in that case, it returns a `MediaSource` that doesn't have preloaded data. For example, this might happen if the user suddenly jumps far ahead in the carousel.
- After the user plays the new media item, call `setCurrentPlayingIndex` to tell the preload manager where in the carousel the new item is. The preload manager needs that information to prioritize loading the next item.

### Remove items from the preload manager

To keep the preload manager efficient, you should remove items the preload
manager no longer needs to track. You might also remove items that are still in
the carousel, but are far away from the user's current position. For example,
you might decide that if an item is more than 15 items away from what the user
is watching, it doesn't need to be preloaded. In that case, you'd remove items
when they got that far away. If the user moves back towards those removed items,
you can always [add them back](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items).

If you have a list of media items to remove, you can use
[`removeMediaItems`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/or%20%5B%60removeMediaSources%60%5D). Alternatively, you can
call [`remove`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#remove(androidx.media3.common.MediaItem)) (or `removeMediaSource`) to remove media items
individually.


```kotlin
preloadManager.removeMediaItems(mediaItemsToRemove)
```

<br />

#### Key points about the code

- If you want to remove *all* the items from the preload manager, you can call [`reset()`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#reset()) instead of `remove()`. This approach is useful if you need to change all the items in your carousel. In that case, after you remove the items, you'll need to [add new items to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items).

### Release the preload manager when you're done with it

When you no longer need the preload manager, you must release it to free up its
resources. In particular, make sure to release it when your activity is
destroyed.


```kotlin
preloadManager.release()
```

<br />

#### Key points about the code

- You *must not* call any of the object's methods after you release it.
- If you need to create another preload manager, create a new `DefaultPreloadManager.Builder` and use it to create the `DefaultPreloadManager`. Don't try to reuse the old builder.