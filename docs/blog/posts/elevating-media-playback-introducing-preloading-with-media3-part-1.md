---
title: https://developer.android.com/blog/posts/elevating-media-playback-introducing-preloading-with-media3-part-1
url: https://developer.android.com/blog/posts/elevating-media-playback-introducing-preloading-with-media3-part-1
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Elevating media playback: Introducing preloading with Media3 - Part 1

###### 8-min read

![](https://developer.android.com/static/blog/assets/elevating_Media_Playback_16bfc9b0d6_25Uc6u.webp) 05 Sep 2025 [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) [##### Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya)

###### Developer Relations Engineer

In today's media-centric apps, delivering a smooth, uninterrupted playback experience is key to a delightful user experience. Users expect their videos to start instantly and play seamlessly without pauses.

The core challenge is latency. Traditionally, a video player only starts its work---connecting, downloading, parsing, buffering---after the user has chosen an item for playback. This reactive approach is slow for today's short form video context. The solution is to be proactive. We need to anticipate what the user will watch next and get the content ready ahead of time. This is the essence of preloading.

The key benefits of preloading include:

- **🚀 Faster Playback Start:** Videos are already ready to go, leading to quicker transitions between items and a more immediate start.
- **📉 Reduced Buffering:** By proactively loading data, playback is far less likely to stall, for example due to network hiccups.
- **✨ Resulting smoother User Experience:** The combination of faster starts and less buffering creates a more fluid, seamless interaction for users to enjoy.

In this three-part series, we'll introduce and deep dive into Media3's powerful utilities for (pre)loading components.

- In Part 1, we'll cover the foundations: understanding the different preloading strategies available in Media3, enabling PreloadConfiguration and setting up the DefaultPreloadManager, enabling your app to preload items. By the end of this blog, you should be able to preload and play media items with your configured ranking and duration.
- In [Part 2](https://android-developers.googleblog.com/2025/09/a-deep-dive-into-media3-preloadmanager.html), we'll get into more advanced topics of DefaultPreloadManager: using listeners for analytics, exploring production-ready best practices like the sliding window pattern and custom shared components of DefaultPreloadManager and ExoPlayer.
- In Part 3, we'll dive deep into disk caching with DefaultPreloadManager.

## Preloading to the rescue! 🦸‍♀️

The core idea behind preloading is simple: load media content before you need it. By the time a user swipes to the next video, the first segments of the video are already downloaded and available, ready for immediate playback.

Think of it like a restaurant. A busy kitchen doesn't wait for an order to start chopping onions. 🧅 They do their prep work in advance. Preloading is the prep work for your video player.

When enabled, preloading can help minimize join latency when a user skips to the next item before the playback buffer reaches the next item. The first period of the next window is prepared and video, audio and text samples are buffered. The preloaded period is later queued into the player with buffered samples immediately available and ready to be fed to the codec for rendering.

In Media3 there are two primary APIs for preloading, each suited for different use cases. Choosing the right API is the first step.

### 1. Preloading playlist items with PreloadConfiguration

This is the simple approach, useful for linear, sequential media like playlists where the playback order is predictable (like a series of episodes). You give the player the full list of media items using ExoPlayer's [playlist](https://developer.android.com/media/media3/exoplayer/playlists) APIs and set the [PreloadConfiguration](https://developers.google.com/admob/android/reference/com/google/android/gms/ads/preload/PreloadConfiguration) for the player, then it automatically preloads the next items in the sequence as configured. This API attempts to optimize the join latency when a user skips to the next item before the playback buffer already overlaps into the next item.

Preloading is only started when no media is being loaded for the ongoing playback, which prevents it from competing for bandwidth with the primary playback.

If you're still not sure whether you need preloading, this API is a great low-lift option to try it out!

```
player.preloadConfiguration =
    PreloadConfiguration(/* targetPreloadDurationUs= */ 5_000_000L)
```

With the [PreloadConfiguration](https://developer.android.com/reference/kotlin/androidx/media3/exoplayer/ExoPlayer.PreloadConfiguration) above, the player tries to preload five seconds of media for the next item in the playlist.

Once opted-in, playlist preloading can be turned off again by using `PreloadConfiguration.DEFAULT` to disable playlist preloading:

```
player.preloadConfiguration = PreloadConfiguration.DEFAULT
```

### 2. Preloading dynamic lists with PreloadManager

For dynamic UIs like vertical feeds or carousels, where the "next" item is determined by user interaction, the PreloadManager API is appropriate. This is a new powerful, standalone component within the Media3 ExoPlayer library specifically designed to proactively preload. It manages a collection of potential MediaSources, prioritizing them based on proximity to the user's current position and offers **granular** control over what to preload, suitable for complex scenarios like dynamic feeds of short form videos.

#### Setting Up Your PreloadManager

The [DefaultPreloadManager](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager) is the canonical implementation for PreloadManager.

The builder of `DefaultPreloadManager` can build both the DefaultPreloadManager and any [ExoPlayer](https://developer.android.com/media/media3/exoplayer) instances that will play its preloaded content. To create a DefaultPreloadManager, you will need to pass a TargetPreloadStatusControl, which the preload manager can query to find out how much to load for an item. We will explain and define an example of TargetPreloadStatusControl in the section below.

```
val preloadManagerBuilder =
DefaultPreloadManager.Builder(context, targetPreloadStatusControl)
val preloadManager = val preloadManagerBuilder.build()

// Build ExoPlayer with DefaultPreloadManager.Builder
val player = preloadManagerBuilder.buildExoPlayer()
```

Using the same [builder](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder#build()) for both the ExoPlayer and `DefaultPreloadManager` is necessary, which ensures that the components under the hood of them are correctly shared.

And that's it! You now have a manager ready to receive instructions.

#### Configuring Duration and Ranking with [TargetPreloadStatusControl](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/TargetPreloadStatusControl)

What if you want to preload, say, 10 seconds of video ? You can provide the position of your media items in the carousel, and the DefaultPreloadManager prioritizes loading the items based on how close it is to the item the user is currently playing.

If you want to control how much duration of the item to preload, you can tell that with DefaultPreloadManager.PreloadStatus you return.

For example,

- Item 'A' is the highest priority, load 5 seconds of video.
- Item 'B' is medium priority but when you get to it, load 3 seconds of video.
- Item 'C' is less priority, load only tracks.
- Item 'D' is even less of a priority, just prepare.
- Any other items are far away, Don't preload anything.

This granular control can help you optimize your resource utilization which is recommended for a seamless playback.

```
import androidx.media3.exoplayer.DefaultPreloadManager.PreloadStatus


class MyTargetPreloadStatusControl(
    currentPlayingIndex: Int = C.INDEX_UNSET
) : TargetPreloadStatusControl<Int,PreloadStatus> {


    // The app is responsible for updating this based on UI state
    override fun getTargetPreloadStatus(index: Int): PreloadStatus? {

        val distance = index - currentPlayingIndex

        // Adjacent items (Next): preload 5 seconds
        if (distance == 1) { 
        // Return a PreloadStatus that is labelled by STAGE_SPECIFIED_RANGE_LOADED and suggest loading // 5000ms from the default start position
                    return PreloadStatus.specifiedRangeLoaded(5000L)
                } 

        // Adjacent items (Previous): preload 3 seconds
        else if (distance == -1) { 
        // Return a PreloadStatus that is labelled by STAGE_SPECIFIED_RANGE_LOADED //and suggest loading 3000ms from the default start position
                    return PreloadStatus.specifiedRangeLoaded(3000L)
                } 

        // Items two positions away: just select tracks
        else if (distance) == 2) {
        // Return a PreloadStatus that is labelled by STAGE_TRACKS_SELECTED
                    return PreloadStatus.TRACKS_SELECTED
                } 

        // Items four positions away: just select prepare
        else if (abs(distance) <= 4) {
        // Return a PreloadStatus that is labelled by STAGE_SOURCE_PREPARED
                    return PreloadStatus.SOURCE_PREPARED
                }

             // All other items are too far away
             return null
            }
}
```

*Tip: PreloadManager can keep both the previous and next items preloaded, whereas the PreloadConfiguration will only look ahead to the next items.*

#### Managing Preloading Items

With your manager created, you can start telling it what to work on. As your user scrolls through a feed, you'll identify the upcoming videos and add them to the manager. The interaction with the PreloadManager is a state-driven conversation between your UI and the preloading engine.

**1. Add Media Items**

As you populate your feed, you must inform the [manager](https://developer.android.com/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager) of the media it needs to track. If you are starting, you could add the entire list you want to preload. Subsequently you can keep adding a single item to the list as and when required. You have full control over what items are in the preloading list which means you also have to manage what is added and removed from the manager.

```
val initialMediaItems = pullMediaItemsFromService(/* count= */ 20)
for (index in 0 until initialMediaItems.size) {
    preloadManager.add(
        initialMediaItems.get(index),index)
    )
}
```

The manager will now start fetching data for this `MediaItem` in the background.

After adding, tell the manager to re-evaluate its new list (hinting that something has changed like adding/ removing an item, or the user switches to play a new item.)

```
preloadManager.invalidate()
```

**2. Retrieve and Play an Item**

Here comes the main playback logic. When the user decides to play that video, you don't need to create a new `MediaSource`. Instead, you ask the `PreloadManager` for the one it has already prepared. You can retrieve the MediaSource from the Preload Manager using the MediaItem.

If the retrieved item from the PreloadManager is null, that means the mediaItem is not preloaded yet or added to the PreloadMamager, so you choose to set the mediaItem directly.

```
// When a media item is about to displ​​ay on the screen
val mediaSource = preloadManager.getMediaSource(mediaItem)
if (mediaSource!= null) {
  player.setMediaSource(mediaSource)
} else {
  // If mediaSource is null, that mediaItem hasn't been added yet.
  // So, send it directly to the player.
  player.setMediaItem(mediaItem)
}
player.prepare()
// When the media item is displaying at the center of the screen
player.play()
```

By preparing the MediaSource retrieved from the PreloadManager, you seamlessly transition from preloading to playback, using the data that's already in memory. This is what makes the start time faster.

**3. Keep the current index in sync with the UI**

Since our feed / list could be dynamic, it's important to notify the PreloadManager of your current playing index so that it can always prioritize items nearest to your current index for preloading.

```
preloadManager.setCurrentPlayingIndex(currentIndex)
// Need to call invalidate() to update the priorities
preloadManager.invalidate()
```

**4. Remove an Item**

To keep the manager efficient, you should remove items it no longer needs to track, such as items that are far away from the user's current position.

```
// When an item is too far from the current playing index
preloadManager.remove(mediaItem)
```

If you need to clear all items at once, you can call `preloadManager.reset()`.

**5. Release the Manager**

When you no longer need the PreloadManager (e.g., when your UI is destroyed), you must release it to free up its resources. A good place to do this is where you're already releasing your Player's resources. It's recommended to release the manager before the player as the player can continue to play if you don't need any more preloading.

```
// In your Activity's onDestroy() or Composable's onDispose
preloadManager.release()
```

### Demo time

#### Check it live in action 👍

In the demo below , we see the impact of PreloadManager on the right side which has faster load times, whereas the left side shows the existing experience. You can also view the code [sample](https://github.com/android/socialite/tree/ui_polishes_short_videos) for the demo. (Bonus: It also displays startup latency for every video)
![Demo-PreloadManager_2.webp](https://developer.android.com/static/blog/assets/Demo_Preload_Manager_2_cbbd20233c_Z2qBPHI.webp)

## What's Next?

And that's a wrap for Part 1! You now have the tools to build a dynamic preloading system. You can either use `PreloadConfiguration` to preload the next item of a playlist in ExoPlayer or set up a `DefaultPreloadManager`, add and remove items on the fly, configure the target preload status, and correctly retrieve the preloaded content for playback.

In [**Part 2**](https://android-developers.googleblog.com/2025/09/a-deep-dive-into-media3-preloadmanager.html), we'll go deeper on the `DefaultPreloadManager`. We'll explore how to listen for preloading events, discuss best practices like using a sliding window to avoid memory issues, and peek under the hood at custom shared components of ExoPlayer and DefaultPreloadManager.

Do you have any feedback to [share](https://github.com/androidx/media/issues)? We are eager to hear from you.

Stay tuned, and go make your app faster! 🚀

###### Written by:

-

  ## [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/mayuri-khabya) ![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp) ![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) 22 Sep 2025 22 Sep 2025 ![](https://developer.android.com/static/blog/assets/elevating_Media2_20563cb635_1XxrMX.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating media playback: A deep dive into Media3's PreloadManager - Part 2](https://developer.android.com/blog/posts/elevating-media-playback-a-deep-dive-into-media3-s-preload-manager-part-2)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-media-playback-a-deep-dive-into-media3-s-preload-manager-part-2) Welcome to the second installment of our three-part series on media preloading with Media3. This series is designed to guide you through the process of building highly responsive, low-latency media experiences in your Android apps.

  ###### [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya) •
  9 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)