---
title: Elevating media playback: A deep dive into Media3’s PreloadManager - Part 2  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/elevating-media-playback-a-deep-dive-into-media3-s-preload-manager-part-2
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Elevating media playback: A deep dive into Media3’s PreloadManager - Part 2

###### 9-min read

![](/static/blog/assets/elevating_Media2_20563cb635_1XxrMX.webp)

22

Sep
2025

[![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](/blog/authors/mayuri-khabya)

[##### Mayuri Khinvasara Khabya](/blog/authors/mayuri-khabya)

###### Developer Relations Engineer

Welcome to the second installment of our three-part series on media preloading with Media3. This series is designed to guide you through the process of building highly responsive, low-latency media experiences in your Android apps.

* [Part 1: Introducing Preloading with Media3](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html) covered the fundamentals. We explored the distinction between [PreloadConfiguration](https://developers.google.com/admob/android/reference/com/google/android/gms/ads/preload/PreloadConfiguration) for simple playlists and the more powerful [DefaultPreloadManager](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager) for dynamic user interfaces. You learned how to implement the basic API lifecycle: adding media with add(), retrieving a prepared MediaSource with getMediaSource(), managing priorities with setCurrentPlayingIndex() and invalidate(), and releasing resources with remove() and release().
* Part 2 (This post): In this blog, we explore the advanced capabilities of the DefaultPreloadManager. We cover how to gain insights with [PreloadManagerListener](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadManagerListener), implement production-ready best practices like sharing core components with ExoPlayer, and master the sliding window pattern to effectively manage memory.
* Part 3: The final part of this series will dive into integrating PreloadManager with a persistent disk cache, enabling you to reduce data consumption with resource management and provide a seamless experience.

If you are new to preloading in Media3, we highly recommend reading [Part 1](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html) before proceeding. For those ready to move beyond the basics, let's explore how to elevate your media playback implementation.

## Listening in: Fetch analytics with PreloadManagerListener

When you want to launch a feature in production, as an app developer you also want to understand and capture the analytics behind it. How can you be certain that your **preloading strategy is effective in a real-world environment?** Answering this requires data on success rates, failures, and performance. The [PreloadManagerListener](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadManagerListener) interface is the primary mechanism for gathering this data.

The PreloadManagerListener provides two essential callbacks that offer critical insights into the preloading process and status.

* [*onCompleted*](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadManagerListener#onCompleted(androidx.media3.common.MediaItem))*(MediaItem mediaItem)*: This callback is invoked upon the successful completion of a preload request, as defined by your TargetPreloadStatusControl.
* [*onError*](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadManagerListener#onError(androidx.media3.exoplayer.source.preload.PreloadException))*(PreloadException error)*: This callback could be useful for debugging and monitoring. It is invoked when a preload fails, providing the associated exception.

You can register a listener with a single method call as shown in the following example code:

```
  val preloadManagerListener = object : PreloadManagerListener {
    override fun onCompleted(mediaItem: MediaItem) {
        // Log success for analytics. 
        Log.d("PreloadAnalytics", "Preload completed for $mediaItem")
    }

    override fun onError( preloadError: PreloadException) {
        // Log the specific error for debugging and monitoring.
        Log.e("PreloadAnalytics", "Preload error ", preloadError)
    }
}

preloadManager.addListener(preloadManagerListener)
```

### Extracting insights from the listener

These listener callbacks can be hooked to your analytics pipeline. By forwarding these events to your analytics engine, you can answer key questions like:

* *What is our preload success rate? (ratio of onCompleted events to total preload attempts)*
* *Which CDNs or video formats exhibit the highest error rates? (By parsing the exceptions from onError)*
* *What is our preload error rate? (ratio of onError events to total preload attempts)*

This data could give you quantitative feedback on your preloading strategy, enabling A/B testing and data-driven improvements to your user experience. This data can further help you to **intelligently finetune your preload** durations and number of videos you want to preload as well as the buffers you allocate.

### Beyond debugging: Using onError for graceful UI fallback

A failed preload is a strong indicator of an upcoming buffering event for the user. The onError callback allows you to respond reactively. Instead of merely logging the error, you can adapt the UI. For instance, if the upcoming video fails to preload, your application could disable autoplay for the next swipe, requiring a user tap to begin playback.

Additionally, by inspecting the [PreloadException](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadException) type you can define a more intelligent retry strategy. An app can choose to immediately remove a failing source from the manager based on the error message or HTTP status code. The item would need to be removed from the UI stream accordingly to not make loading issues leak into the user experience. You could also get more granular data from PreloadException like the [HttpDataSourceException](/reference/kotlin/androidx/media3/datasource/HttpDataSource.HttpDataSourceException) to probe further into the errors. Read more about [ExoPlayer troubleshooting](/media/media3/exoplayer/troubleshooting).

## The buddy system: Why is sharing components with ExoPlayer necessary?

The DefaultPreloadManager and ExoPlayer are designed to work together. To ensure stability and efficiency, they must share several core [components](/media/media3/exoplayer/customization). If they operate with separate, uncoordinated components, it could impact thread safety and usability of preloaded tracks on the player since we need to ensure that preloaded tracks should be played on the correct player. The separate components could also compete for limited resources like network bandwidth and memory, which could lead to performance degradation. An important part of the lifecycle is handling appropriate disposal, the recommended order of disposal is to release the PreloadManager first, followed by the ExoPlayer.

The DefaultPreloadManager.Builder is designed to facilitate this sharing and has APIs to [instantiate](/media/media3/exoplayer/preloading-media/preloadmanager/create#create-dpm) both your PreloadManager and a linked player instance. Let's see why components like BandwidthMeter, LoadControl, TrackSelector, Looper must be shared. Check the [visual representation](/reference/kotlin/androidx/media3/exoplayer/ExoPlayer#threading-model) of how these components interact with ExoPlayer Playback.

![preloadManager2.png](/static/blog/assets/preload_Manager2_66609d424a_1ELxyA.webp)

### Preventing bandwidth conflicts with a shared BandwidthMeter

The [BandwidthMeter](/reference/androidx/media3/exoplayer/upstream/BandwidthMeter) provides an estimate of available network bandwidth based on historical transfer rates. If the PreloadManager and the player use separate instances, they are unaware of each other's network activity, which can lead to failure scenarios. For example, consider the scenario where a user is watching a video, their network connection degrades, and the preloading MediaSource simultaneously initiates an aggressive download for a future video. The preloading MediaSource’s activity would consume bandwidth needed by the active player, causing the current video to stall. A stall during playback is a significant user experience failure.

By sharing a single BandwidthMeter, the TrackSelector is able to select tracks of highest quality given the current network conditions and the state of the buffer, during preloading or playback. It can then make intelligent decisions to protect the active playback session and ensure a smooth experience.

`preloadManagerBuilder.setBandwidthMeter(customBandwidthMeter)`

### Ensuring consistency with shared LoadControl, TrackSelector, Renderer components of ExoPlayer

* [LoadControl](/reference/androidx/media3/exoplayer/LoadControl): This component dictates buffering policy, such as how much data to buffer before starting playback and when to start or stop loading more data. Sharing LoadControl ensures that the memory consumption of player and PreloadManager is guided by a single, coordinated buffering strategy across both preloaded and actively playing media, preventing resource contention. You will have to smartly allocate buffer size coordinating with how many items you are preloading and with what duration, to ensure consistency. In times of contention, the player will prioritize playback of the current item displayed on the screen. With a shared LoadControl, the preload manager will continue preloading as long as the target buffer bytes allocated for preloading hasn't reached the upper limit, it doesn't wait until the loading for playback is done.

*Note: The sharing of LoadControl in the latest version of* [*Media3 (1.8)*](https://github.com/androidx/media/tree/1.8.0) *ensures that its Allocator can be shared correctly with PreloadManager and player. Using the LoadControl to effectively control the preloading is a feature that will be available in the upcoming Media3 1.9 release.*

`preloadManagerBuilder.setLoadControl(customLoadControl)`

* [TrackSelector](/reference/androidx/media3/exoplayer/trackselection/TrackSelector): This component is responsible for selecting which tracks (for example, video of a certain resolution, audio in a specific language) to load and play. Sharing ensures that the tracks selected during preloading are the same ones the player will use. This avoids a wasteful scenario where a 480p video track is preloaded, only for the player to immediately discard it and fetch a 720p track upon playback.< br /> The preload manager should NOT share the **same instance** of TrackSelector with the player. Instead, they should use the different TrackSelector **instance but of the same implementation**. That's why we set the TrackSelectorFactory rather than a TrackSelector in the DefaultPreloadManager.Builder.

`preloadManagerBuilder.setTrackSelectorFactory(customTrackSelectorFactory)`

* [Renderer](/reference/androidx/media3/exoplayer/Renderer): This component is responsible for understanding the player's capabilities without creating the full renderers. It checks this blueprint to see which video, audio, and text formats the final player will support. This allows it to intelligently select and download only the compatible media track and prevents wasting bandwidth on content the player can't actually play.

`preloadManagerBuilder.setRenderersFactory(customRenderersFactory)`

Read about more [Exoplayer components](/media/media3/exoplayer/customization).

### The golden rule: A common [Playback Looper](/media/media3/exoplayer/hello-world#a-note-on-threading) to rule them all

The thread on which an ExoPlayer instance can be accessed can be explicitly specified by passing a Looper when creating the player. The Looper of the thread from which the player must be accessed can be queried using [Player.getApplicationLooper](/reference/kotlin/androidx/media3/common/Player#getApplicationLooper()). By maintaining a shared Looper between the player and PreloadManager, it is guaranteed that all operations on these shared media objects are serialized onto a single thread's message queue. This can reduce the concurrency bugs.

All interactions between the PreloadManager and the player with media sources to be loaded or preloaded need to happen on the same playback thread. Sharing the [Looper](/reference/android/os/Looper) is a must for thread safety and hence we must share the PlaybackLooper between the PreloadManager and player.

The PreloadManager prepares a stateful MediaSource object in the background. When your UI code calls player.setMediaSource(mediaSource), you are performing a handoff of this complex, stateful object from the preloading MediaSource to the player. In this scenario, the entire PreloadMediaSource is moved from the manager to the player. All these interactions and handoffs should occur on the same PlaybackLooper.

If the PreloadManager and ExoPlayer were operating on different threads, a race condition could occur. The PreloadManager’s thread could be modifying the MediaSource's internal state (e.g, writing new data into a buffer) at the exact moment the player's thread is attempting to read from it. This leads to unpredictable behavior, IllegalStateException that is difficult to debug.

`preloadManagerBuilder.setPreloadLooper(playbackLooper)`

Lets see how you can share all the above components between ExoPlayer and DefaultPreloadManager in the setup itself.

```
  val preloadManagerBuilder =
DefaultPreloadManager.Builder(context, targetPreloadStatusControl)

// Optional - Share components between ExoPlayer and DefaultPreloadManager
preloadManagerBuilder
     .setBandwidthMeter(customBandwidthMeter)
     .setLoadControl(customLoadControl)
     .setMediaSourceFactory(customMediaSourceFactory)
     .setTrackSelectorFactory(customTrackSelectorFactory)
     .setRenderersFactory(customRenderersFactory)
     .setPreloadLooper(playbackLooper)

val preloadManager = val preloadManagerBuilder.build()
```

*Tip: If you use the Default components in ExoPlayer like the* [*DefaultLoadControl*](/reference/androidx/media3/exoplayer/DefaultLoadControl)*, etc, you don't need to explicitly share them with DefaultPreloadManager. When you build your ExoPlayer instance via the* [*buildExoPlayer*](/reference/androidx/media3/exoplayer/source/preload/DefaultPreloadManager.Builder#buildExoPlayer()) *of the DefaultPreloadManager.Builder these components are automatically referenced with each other, if you use the default implementations with default configurations. But if you use custom components or custom configurations, you should **explicitly** notify the DefaultPreloadManager about them via the above APIs.*

## Production-ready preloading: The sliding window pattern

In a dynamic feed, a user can scroll through a virtually infinite amount of content. If you continuously add videos to the DefaultPreloadManager without a corresponding removal strategy, you will inevitably cause an OutOfMemoryError. Each preloaded MediaSource holds onto a [**SampleQueue**](/reference/androidx/media3/exoplayer/source/SampleQueue), which allocates memory buffers. As these accumulate, they can exhaust the application's heap space. The solution is an algorithm you may already be familiar with, called the sliding window. The sliding window pattern maintains a small, manageable set of items in memory that are logically adjacent to the user's current position in the feed. As the user scrolls, this "window" of managed items slides with them, adding new items that come into view, and also removing items that are now distant.

![slidingwindow.png](/static/blog/assets/slidingwindow_a063aa1f77_Z2aUSm9.webp)

### Implementing the sliding window pattern

It is essential to understand that PreloadManager does not provide a built-in setWindowSize() method. The sliding window is a design pattern that you, the developer, are responsible for implementing using the primitive add() and remove() methods. Your application logic must connect UI events, such as a scroll or page change, to these API calls. If you want a code reference for this, we have this sliding window pattern implemented in [socialite](http://github.com/android/socialite) sample which also includes a [PreloadManagerWrapper](https://github.com/android/socialite/blob/main/app/src/main/java/com/google/android/samples/socialite/ui/player/preloadmanager/PreloadManagerWrapper.kt) which imitates a sliding window.

Don’t forget to add preloadManager.remove(mediaItem) in your implementation when the item is no longer likely to come up soon in the user’s viewing. Failing to remove items that are no longer proximate to the user is the primary cause of memory issues in preloading implementations. The remove() call ensures resources are released that help you keep your app's memory usage bound and stable.

## Fine-Tuning a categorized preloading strategy with TargetPreloadStatusControl

Now that we have defined what to preload (the items in our window), we can apply a well defined strategy for how much to preload for each item. We already saw how to achieve this granularity with the [TargetPreloadStatusControl](/reference/androidx/media3/exoplayer/source/preload/TargetPreloadStatusControl) setup in [Part 1](https://android-developers.googleblog.com/2025/09/introducing-preloading-with-media3.html).

To recall, an item at position +/- 1 could have a higher probability of being played than an item at position +/- 4. You could allocate more resources (network, CPU, memory) to items the user is most likely to view next. This creates a "preloading" strategy based on proximity, which is the key to **balancing** immediate playback with efficient resource usage.

You could use analytics data via [PreloadManagerListener](/reference/kotlin/androidx/media3/exoplayer/source/preload/PreloadManagerListener) as discussed in the earlier sections to decide your preload duration strategy.

## Conclusion and next steps

You are now equipped with the advanced knowledge to build fast, stable, and resource-efficient media feeds using Media3's DefaultPreloadManager.

**Let's recap the key takeaways:**

* Use PreloadManagerListener to gather analytics insights and implement robust error handling.
* Always use a single DefaultPreloadManager.Builder to create both your manager and player instances to ensure important components are shared.
* Implement the sliding window pattern by actively managing add() and remove() calls to prevent OutOfMemoryError.
* Use TargetPreloadStatusControl to create a smart, tiered preloading strategy that balances performance and resource consumption.

## What’s next in Part 3: Caching with preloaded media

Preloading data into memory provides an immediate performance benefit, but it can come with tradeoffs. Once the application is closed or the preloaded media is removed from the manager, the data is gone. To achieve a more persistent level of optimization, we can combine preloading with disk caching. This feature is in active development and will come soon in a few months.

Do you have any feedback to [share](https://github.com/androidx/media/issues)? We are eager to hear from you.

Stay tuned, and go make your video playback faster! 🚀

###### Written by:

* ## [Mayuri Khinvasara Khabya](/blog/authors/mayuri-khabya)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/mayuri-khabya)

  ![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)

  ![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)

## Continue reading

* [![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](/blog/authors/mayuri-khabya)

  05

  Sep
  2025

  05

  Sep
  2025

  ![](/static/blog/assets/elevating_Media_Playback_16bfc9b0d6_25Uc6u.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Elevating media playback: Introducing preloading with Media3 - Part 1](/blog/posts/elevating-media-playback-introducing-preloading-with-media3-part-1)

  [arrow\_forward](/blog/posts/elevating-media-playback-introducing-preloading-with-media3-part-1)

  In today's media-centric apps, delivering a smooth, uninterrupted playback experience is key to a delightful user experience. Users expect their videos to start instantly and play seamlessly without pauses.

  ###### [Mayuri Khinvasara Khabya](/blog/authors/mayuri-khabya) • 8 min read
* [![](/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](/blog/authors/matthew-warner)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow\_forward](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](/blog/authors/matthew-warner) • 2 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/matt-dyor)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow\_forward](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](/blog/authors/matt-dyor) • 3 min read

  + [#Android Studio](/blog/topics/android-studio)

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)