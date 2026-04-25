---
title: https://developer.android.com/blog/posts/media3-whats-new
url: https://developer.android.com/blog/posts/media3-whats-new
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Media3 1.9.0 - What's new

###### 6-min read

![](https://developer.android.com/static/blog/assets/Android_Evergreen_Hero_Banner_AI_Weband_App_Option_B_627622b909_10sGeD.webp) 19 Dec 2025 [![](https://developer.android.com/static/blog/assets/Kristina_Simakova_0a7a20024f_a9nfE.webp)](https://developer.android.com/blog/authors/kristina-simakova) [##### Kristina Simakova](https://developer.android.com/blog/authors/kristina-simakova)

###### Engineering Manager

Media3 1.9.0 is out! Besides the usual bug fixes and performance improvements, the latest release also contains **four** new or largely rewritten modules:

- `media3-inspector` - Extract metadata and frames outside of playback
- `media3-ui-compose-material3` - Build a basic Material3 Compose Media UI in just a few steps
- `media3-cast` - Automatically handle transitions between Cast and local playbacks
- `media3-decoder-av1` - Consistent AV1 playback with the rewritten extension decoder based on the dav1d library

We also added caching and memory management improvements to `PreloadManager`, and provided several new `ExoPlayer`, `Transformer` and `MediaSession` simplifications.

This release also gives you the first experimental access to `CompositionPlayer` to preview media edits.

<br />

Read on to find out more, and as always please check out the full [release notes](https://github.com/androidx/media/releases/tag/1.9.0) for a comprehensive overview of changes in this release.

## Extract metadata and frames outside of playback

There are many cases where you want to inspect media without starting a playback. For example, you might want to detect which formats it contains or what its duration is, or to retrieve thumbnails.

The new `media3-inspector` module combines all utilities to inspect media without playback in one place:

- `MetadataRetriever` to read duration, format and static metadata from a `MediaItem`.
- `FrameExtractor` to get frames or thumbnails from an item.
- `MediaExtractorCompat` as a direct replacement for the Android platform MediaExtractor class, to get detailed information about samples in the file.

`MetadataRetriever` and `FrameExtractor` follow a simple `AutoCloseable` pattern. Have a look at our [new guide pages](https://developer.android.com/media/media3/inspector) for more details.

```
suspend fun extractThumbnail(mediaItem: MediaItem) {

  FrameExtractor.Builder(context, mediaItem).build().use {

    val thumbnail = frameExtractor.getThumbnail().await()

  } 

}
```

## Build a basic Material3 Compose Media UI in just a few steps

In previous releases we started providing connector code between Compose UI elements and your Player instance. With Media3 1.9.0, we added a new module media3-ui-compose-material3 with fully-styled Material3 buttons and content elements. They allow you to build a media UI in just a few steps, while providing all the flexibility to customize style. If you prefer to build your own UI style, you can use the building blocks that take care of all the update and connection logic, so you only need to concentrate on designing the UI element. Please check out our [extended guide pages](https://developer.android.com/media/media3/ui/compose) for the Compose UI modules.

We are also still working on even more Compose components, like a prebuilt seek bar, a complete out-of-the-box replacement for `PlayerView`, as well as subtitle and ad integration.

```
@Composable
fun SimplePlayerUI(player: Player, modifier: Modifier = Modifier) {
  Column(modifier) {
    ContentFrame(player)  // Video surface and shutter logic
    Row (Modifier.align(Alignment.CenterHorizontally)) {                 
      SeekBackButton(player)   // Simple controls
      PlayPauseButton(player)
      SeekForwardButton(player)
    }
  }
}
```

![image.png](https://developer.android.com/static/blog/assets/image_c643ce55c4_miyY9.webp)

*Simple Compose player UI with out-of-the-box elements*

## Automatically handle transitions between Cast and local playbacks

The [CastPlayer](https://developer.android.com/media/media3/cast/create-castplayer) in the `media3-cast` module has been rewritten to automatically handle transitions between local playback (for example with `ExoPlayer`) and remote Cast playback.

When you set up your `MediaSession`, simply build a `CastPlayer` around your `ExoPlayer` and add a `MediaRouteButton` to your UI and you're done!

```
// MediaSession setup with CastPlayer 

val exoPlayer = ExoPlayer.Builder(context).build()

val castPlayer = CastPlayer.Builder(context).setLocalPlayer(exoPlayer).build()

val session = MediaSession.Builder(context, castPlayer).build()

// MediaRouteButton in UI 

@Composable fun UIWithMediaRouteButton() {

  MediaRouteButton()

}
```
![image.png](https://developer.android.com/static/blog/assets/image_da153aa491_14UjYy.webp)

*New CastPlayer integration in Media3 session demo app*

## Consistent AV1 playback with the rewritten extension based on dav1d

The 1.9.0 release contains a completely rewritten AV1 extension module based on the popular [dav1d](https://github.com/videolan/dav1d) library.

As with all extension decoder modules, please note that it requires [building from source](https://github.com/androidx/media/tree/release/libraries/decoder_av1#readme)to bundle the relevant native code correctly. Bundling a decoder provides consistency and format support across all devices, but because it runs the decoding in your process, it's best suited for content you can trust.

## Integrate caching and memory management into PreloadManager

We made our `PreloadManager` even better as well. It already enabled you to preload media into memory outside of playback and then seamlessly hand it over to a player when needed. Although pretty performant, you still had to be careful to not exceed memory limits by accidentally preloading too much. So with Media3 1.9.0, we added two features that makes this a lot easier and more stable:

1. **Caching support** -- When defining how far to preload, you can now choose `PreloadStatus.specifiedRangeCached(0, 5000)` as a target state for preloaded items. This will add the specified range to your cache on disk instead of loading the data to memory. With this, you can provide a much larger range of items for preloading as the ones further away from the current item no longer need to occupy memory. Note that this requires setting a `Cache` in `DefaultPreloadManager.Builder`.
2. **Automatic memory management** -- We also updated our `LoadControl` interface to better handle the preload case so you are now able to set an explicit upper memory limit for all preloaded items in memory. It's 144 MB by default, and you can configure the limit in `DefaultLoadControl.Builder`. The `DefaultPreloadManager` will automatically stop preloading once the limit is reached, and automatically releases memory of lower priority items if required.

## Rely on new simplified default behaviors in ExoPlayer

As always, we added lots of incremental improvements to ExoPlayer as well. To name just a few:

- **Mute and unmute** -- We already had a `setVolume` method, but have now added the convenience `mute` and `unmute` methods to easily restore the previous volume without keeping track of it yourself.
- **Stuck player detection** -- In some rare cases the player can get stuck in a buffering or playing state without making any progress, for example, due to codec issues or misconfigurations. Your users will be annoyed, but you never see these issues in your analytics! To make this more obvious, the player now reports a `StuckPlayerException` when it detects a stuck state.
- **Wakelock by default** -- The wake lock management was previously opt-in, resulting in hard to find edge cases where playback progress can be delayed a lot when running in the background. Now this feature is opt-out, so you don't have to worry about it and can also remove all manual wake lock handling around playback.
- **Simplified setting for CC button logic** -- Changing `TrackSelectionParameters` to say "turn subtitles on/off" was surprisingly hard to get right, so we added a simple boolean `selectTextByDefault` option for this use case.

## Simplify your media button preferences in MediaSession

Until now, defining your preferences for which buttons should show up in the media notification drawer on Android Auto or WearOS required defining custom commands and buttons, even if you simply wanted to trigger a standard player method.

Media3 1.9.0 has new functionality to make this a lot simpler -- you can now [define your media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) with a standard player command, requiring no custom command handling at all.

```
session.setMediaButtonPreferences(listOf(
    CommandButton.Builder(CommandButton.ICON_FAST_FORWARD) // choose an icon
      .setDisplayName(R.string.skip_forward)
      .setPlayerCommand(Player.COMMAND_SEEK_FORWARD) // choose an action 
      .build()
))
```
![image.png](https://developer.android.com/static/blog/assets/image_9f184d8c74_9UQMh.webp)

*Media button preferences with fast forward button*

## CompositionPlayer for real-time preview

The 1.9.0 release introduces CompositionPlayer under a new `@ExperimentalApi` annotation. The annotation indicates that it is available for experimentation, but is still under development.

`CompositionPlayer` is a new component in the Media3 editing APIs designed for real-time preview of media edits. Built upon the familiar Media3 `Player` interface, `CompositionPlayer` allows users to see their changes in action before committing to the export process. It uses the same `Composition` object that you would pass to `Transformer` for exporting, streamlining the editing workflow by unifying the data model for preview and export.

We encourage you to start using [CompositionPlayer](https://developer.android.com/reference/androidx/media3/transformer/CompositionPlayer) and share [your feedback](https://github.com/androidx/media/issues), and keep an eye out for forthcoming posts and updates to the documentation for more details.

## InAppMuxer as a default muxer in Transformer

Transformer now uses [`InAppMp4Muxer`](https://developer.android.com/reference/androidx/media3/transformer/InAppMp4Muxer) as the default muxer for writing media container files. Internally, `InAppMp4Muxer` depends on the Media3 [Muxer](https://developer.android.com/reference/androidx/media3/muxer/package-summary) module, providing consistent behaviour across all API versions.

Note that while Transformer no longer uses the Android platform's [MediaMuxer](https://developer.android.com/reference/android/media/MediaMuxer) by default, you can still provide `FrameworkMuxer.Factory` via [setMuxerFactory](https://developer.android.com/reference/androidx/media3/transformer/Transformer.Builder#setMuxerFactory(androidx.media3.muxer.Muxer.Factory)) if your use case requires it.

## New speed adjustment APIs

The 1.9.0 release simplifies speed adjustments APIs for media editing. We've introduced new methods directly on `EditedMediaItem.Builder` to control speed, making the API more intuitive. You can now change the speed of a clip by calling `setSpeed(SpeedProvider provider)` on the `EditedMediaItem.Builder`:

```
val speedProvider = object : SpeedProvider {
    override fun getSpeed(presentationTimeUs: Long): Float {
        return speed
    }

    override fun getNextSpeedChangeTimeUs(timeUs: Long): Long {
        return C.TIME_UNSET
    }
}

EditedMediaItem speedEffectItem = EditedMediaItem.Builder(mediaItem)
    .setSpeed(speedProvider)
    .build()
```

This new approach replaces the previous method of using `Effects#createExperimentalSpeedChangingEffects()`, which we've deprecated and will remove in a future release.

## Introducing track types for EditedMediaItemSequence

In the 1.9.0 release, `EditedMediaItemSequence` requires specifying desired output track types during sequence creation. This change ensures track handling is more explicit and robust across the entire Composition.

This is done via a new `EditedMediaItemSequence.Builder` constructor that accepts a set of track types (e.g., `C.TRACK_TYPE_AUDIO, C.TRACK_TYPE_VIDEO`).

To simplify creation, we've added new static convenience methods:

- EditedMediaItemSequence.withAudioFrom(List\<EditedMediaItem\>)
- EditedMediaItemSequence.withVideoFrom(List\<EditedMediaItem\>)
- EditedMediaItemSequence.withAudioAndVideoFrom(List\<EditedMediaItem\>)

We encourage you to migrate to the new constructor or the convenience methods for clearer and more reliable sequence definitions.

Example of creating a video-only sequence:

```
EditedMediaItemSequence videoOnlySequence =
    EditedMediaItemSequence.Builder(setOf(C.TRACK_TYPE_VIDEO))
        .addItem(editedMediaItem)
        .build()
```

Please get in touch via the [Media3 issue Tracker](https://github.com/androidx/media/issues) if you run into any bugs, or if you have questions or feature requests. We look forward to hearing from you!

###### Written by:

-

  ## [Kristina Simakova](https://developer.android.com/blog/authors/kristina-simakova)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/kristina-simakova) ![](https://developer.android.com/static/blog/assets/Kristina_Simakova_0a7a20024f_a9nfE.webp) ![](https://developer.android.com/static/blog/assets/Kristina_Simakova_0a7a20024f_a9nfE.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)