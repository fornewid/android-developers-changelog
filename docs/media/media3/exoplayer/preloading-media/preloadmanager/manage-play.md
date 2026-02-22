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
- [Invalidate the priorities in the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate)
- [Fetch and play media](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#fetch-play)
- [Remove items from the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#remove)
- [Release the preload manager when you're done with it](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#release)

## Add media items to the preload manager

You have to tell the preload manager about each media item it will be tracking.
For example, if your app has a carousel of videos, you'd add those videos to the
preload manager. Depending on your use case, you might add all the videos, or
just all the videos near the video that's currently playing. You can also add
new items to the preload manager later.

Adding the media items does not, by itself, cause the preload manager to start
loading the content. To trigger the preloading, you'll need to [invalidate the
priorities in the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate).  

```kotlin
val initialMediaItems = pullMediaItemsFromService(count = 20)
for (index in 0 until initialMediaItems.size) {
  preloadManager.add(initialMediaItems.get(index), /* rankingData= */ index)
}
// items aren't actually loaded yet! need to call invalidate() after this  
https://github.com/androidx/media/blob/630c1af455a16b8eb1ab36f49d82d9db799d7f5e/docsamples/src/main/java/androidx/media3/docsamples/PreloadManagerKotlinSnippets.kt#L78-L82
```

#### Key points about the code

- This snippet shows how to initially populate the preload manager after you've created it. You can also call `add()` to add items to an existing, populated preload manager.
- In this snippet, `pullMediaItemsFromService()` is the app's logic to fetch the list of content to play. The code calls that method to fetch a list of up to 20 items.
- `preloadManager` is the `DefaultPreloadManager` created in [Create a
  `DefaultPreloadManager`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create). The code calls that manager's `add()` method to add each item in the carousel.
- `rankingData` is a value the preload manager uses to determine the priority of each media item. For `DefaultPreloadManager`, `rankingData` is an integer representing the item's position in the carousel. The preload manager determines the priority by how far each item is from the item that's currently playing.

### Invalidate the priorities in the preload manager

To trigger the preload manager to start preloading content, you need to call
`invalidate()` to tell the preload manager that the priorities of items are out
of date. You should do this in the following situations:

- When you add new media items to the preload manager, or remove media items. If you're adding or removing several items, you should add all of them, *then* call `invalidate()`.
- When the user switches from one media item to another. In this case, you should make sure to update the current playing index *before* you call `invalidate()`, as described in [Fetch and play content](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#fetch-play).

When you invalidate the preload manager, it calls the
[`TargetPreloadStatusControl` you created](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create#create-tpsc) to find out how much content
it should load from each item. It then loads the content for each item in the
order of their priority from high to low.  

```kotlin
preloadManager.invalidate()
```

#### Key points about the code

- Calling `invalidate()` triggers the preload manager to re-evaluate the priority of each media item it knows about. For this reason, if you're making a lot of changes to the preload manager, you should finish making the changes before you call `invalidate()`.

### Fetch and play media

When the user advances to a new media item, you need to get the media item from
the preload manager. If the preload manager has loaded any of the content, the
content plays faster than it would have if you hadn't used the preload manager.
If the preload manager hasn't loaded content from that item yet, the content
plays normally.  

```kotlin
// When a media item is about to display on the screen
val mediaSource = preloadManager.getMediaSource(mediaItem)
if (mediaSource != null) {
  player.setMediaSource(mediaSource)
} else {
  // If mediaSource is null, that mediaItem hasn't been added to the preload manager
  // yet. So, send it directly to the player when it's about to play
  player.setMediaItem(mediaItem)
}
player.prepare()

// When the media item is displaying at the center of the screen
player.play()
preloadManager.setCurrentPlayingIndex(currentIndex)

// Need to call invalidate() to update the priorities
preloadManager.invalidate()
```

#### Key points about the code

- `player` is the Media3 `ExoPlayer` the app is using to play the content. You must create that player by calling [`DefaultPreloadManager.Builder.buildExoPlayer()`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder#buildExoPlayer()) on the same builder you used to create the preload manager.
- When the user switches to a new media item, the app calls `getMediaSource()` to get the media source from the preload manager. This must be a `mediaItem` you have [already added to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items). It's okay if the preload manager hasn't already started loading the content; in that case, it returns a `MediaSource` that doesn't have preloaded data. For example, this might happen if the user suddenly jumps far ahead in the carousel.
- After the user plays the new media item, call `setCurrentPlayingIndex` to tell the preload manager where in the carousel the new item is. The preload manager needs that information to prioritize loading the next item. After you update the current index, [call `invalidate()`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate) to make the preload manager redetermine the priority for each item.

### Remove items from the preload manager

To keep the preload manager efficient, you should remove items the preload
manager no longer needs to track. You might also remove items that are still in
the carousel, but are far away from the user's current position. For example,
you might decide that if an item is more than 15 items away from what the user
is watching, it doesn't need to be preloaded. In that case, you'd remove items
when they got that far away. If the user moves back towards those removed items,
you can always [add them back](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items).  

```kotlin
preloadManager.remove(mediaItem)
```

#### Key points about the code

- If you want to remove *all* the items from the preload manager, you can call [`reset()`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/BasePreloadManager#reset()) instead of `remove()`. This approach is useful if you need to change all the items in your carousel. In that case, after you remove the items, you'll need to [add new items to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items) then [invalidate the priorities in the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate).

### Release the preload manager when you're done with it

When you no longer need the preload manager, you must release it to free up its
resources. In particular, make sure to release it when your activity is
destroyed.  

```kotlin
preloadManager.release()
```

#### Key points about the code

- You *must not* call any of the object's methods after you release it.
- If you need to create another preload manager, create a new `DefaultPreloadManager.Builder` and use it to create the `DefaultPreloadManager`. Don't try to reuse the old builder.