---
title: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/concepts
url: https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/concepts
source: md.txt
---

The preload manager helps you give users a better experience by serving content
to them faster, with less waiting when they switch from one item to another. It
also lets you customize the duration and ranking of preloading per item.

A common situation in social media is, an app shows a list or carousel of media
choices to the user. For example, an app might show a carousel of short videos.
When one video finishes, the app switches to the next one. And if the user
doesn't like the video they're watching, they might swipe away to the next
video, or the previous one.

If you don't preload video content, this can result in a frustrating user
experience. The user finishes with some media and then has to wait for the next
media to load.

On the other hand, if you preload the content too aggressively,
that wastes power and network bandwidth loading content that the user may never
actually play.

[`DefaultPreloadManager`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager) helps your app balance these concerns. The preload
manager works with your app to decide how important each media item is, and
loads the appropriate amount in advance.

### Division of labor

If you use `DefaultPreloadManager`, some work is done by your code, and some by
the preload manager.

Your app has to do the following:

- Create the app's `ExoPlayer` objects by using the same `DefaultPreloadManager.Builder` object you use to create the preload manager. Call `DefaultPreloadManager.Builder.buildExoPlayer()` to create an `ExoPlayer`.
- [Tell the preload manager about each media item it should be tracking](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items). This might not be all the content in the carousel; instead, you can just tell it about the first few items to be played. As the user navigates through the carousel, you can add [and remove](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#remove) media items from the preload manager's pool.
- [Invalidate the priorities in the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate) when the content in the carousel changes, or the user changes which item they're playing. This tells the preload manager to redetermine the priority of each media item, and load content if necessary. You'll invalidate the preload manager after you first add media items, and also when the user moves from one item to another, or when you add or remove items to the carousel.
- [Respond to queries from the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create#create-tpsc), telling the manager *how
  much* content to preload for each item.
- [Fetch media from the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#fetch-play) when the user starts playing an
  item. The preload manager gives your app a `MediaSource` for that content.

  | **Important:** The `MediaSource` returned by the preload manager must be played on an `ExoPlayer` created by that preload manager's builder.
- [Release the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#release) when you're done with it, freeing its
  resources.

The preload manager does the following:

- It keeps track of all the media items your app has added to it.
- Each time its priorities are invalidated, it queries your app by calling a [`TargetPreloadStatusControl`](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/TargetPreloadStatusControl) implemented by your app. It calls this to find out *how much* of each media item to load.
- After it queries the app, it preloads the appropriate amount of each media item. The preload manager decides what order to load the item. It prioritizes items that are closest to the item the user's playing.
- When the app requests content, the preload manager provides a `MediaSource` with whatever content has already been loaded.

| **Note:** Your app decides *how much* of each media item should be preloaded, and tells the preload manager where each media item is in the carousel, as well as which item is currently playing. The preload manager decides what order to load the items, based on how close each item is to the item that's currently playing.

### Preload manager workflow

This section describes a typical workflow for an app that uses the preload
manager. In this example, we assume the app displays a carousel of short videos.
The selected video plays automatically, but the user can scroll the carousel in
either direction, which stops the video that was playing and starts the video
they scroll to.

All these steps are discussed in detail in the following pages.

1. [The app creates a](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create#create-tpsc) [*target preload status control*](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create#create-tpsc). The preload manager queries this control to find out how much of each media item to load.
2. The app creates a `DefaultPreloadManager.Builder`, and passes the target preload status control. The app then [uses the builder to create the preload
   manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/create#create-dpm).
3. The app [adds media items to the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#add-items). The app provides an *index* for each item, specifying the item's position in the carousel.
4. After all the media is added, [the app calls](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate) [`invalidate()`](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#invalidate) to tell the preload manager to set the priorities for each item then preload them.
5. For each media item, the preload manager calls the target preload control to query how much of the item should be loaded. The target preload control might say to load a certain duration of content, just fetch the item's metadata, or not fetch any of that item at this time. After the preload manager has gotten this information, it starts loading the media content.
6. When the user starts playing content, [the app calls the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#fetch-play) to request a `MediaSource` for that media item. The app also calls `setCurrentPlayingIndex()` to tell the preload manager which media item is being played.
7. If the user moves to a different media item, the app requests that item from the preload manager, and also updates the current playing index. It then calls `invalidate()` again to tell the preload manager to update its priorities based on what's now being played.
8. If the app adds or removes media items to the carousel, it also adds or removes those items to the preload manager, and calls `invalidate()` when it's done doing that.
9. Whenever the preload manager's priorities are invalidated, it calls the target preload control once again to find out how much of each item to load.
10. When the app closes the carousel, it [releases the preload manager](https://developer.android.com/media/media3/exoplayer/preloading-media/preloadmanager/manage-play#release) to free its resources.