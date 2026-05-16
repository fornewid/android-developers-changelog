---
title: https://developer.android.com/media/media3/transformer/compositionplayer
url: https://developer.android.com/media/media3/transformer/compositionplayer
source: md.txt
---

The Jetpack Media3 library provides the [`CompositionPlayer`](https://developer.android.com/reference/kotlin/androidx/media3/transformer/CompositionPlayer) API, a
powerful [`Player`](https://developer.android.com/reference/androidx/media3/common/Player) implementation for previewing video edits in real time.
If your app lets users edit videos, such as applying effects, trimming, or
compositing multiple input media items, `CompositionPlayer` helps you show an
accurate preview of the output. This can be valuable in cases where you don't
need to save the applied edits, or to validate the edits are configured as
intended before committing them to the final video for export.

> [!NOTE]
> **Note:** `CompositionPlayer` is in an early preview stage. This means the API is subject to change, and we are actively working on its development for future enhancements. As such, it is annotated as an [`@ExperimentalApi`](https://developer.android.com/reference/kotlin/androidx/media3/common/util/ExperimentalApi) that you will need to [opt-in](https://developer.android.com/reference/androidx/annotation/OptIn) to use.

## What is `CompositionPlayer`?

`CompositionPlayer` is a specialized implementation of the
[Player interface](https://developer.android.com/media/media3/session/player), designed specifically to play [`Composition`](https://developer.android.com/reference/androidx/media3/transformer/Composition) objects.
A `Composition` defines
how input media assets, like video clips and audio tracks, are arranged and what
audio and video effects should be applied to them. To learn more about the
`Composition` API, see [Define a `Composition` of media items](https://developer.android.com/media/media3/transformer/composition).

The primary purpose of `CompositionPlayer` is to render this `Composition`,
complete with all specified edits, in real-time, allowing users to see exactly
how their edits will look before committing to the potentially time- and
resource-consuming export process. The same `Composition` object can then be
used with a [`Transformer`](https://developer.android.com/reference/androidx/media3/transformer/Transformer) instance for export, which you can learn more
about in [Exporting a `Composition`](https://developer.android.com/media/media3/transformer/composition#export).

### `CompositionPlayer` versus `ExoPlayer`

While both `CompositionPlayer` and [`ExoPlayer`](https://developer.android.com/media/media3/exoplayer) are `Player` implementations
within Media3, they are optimized for different use-cases:

|---|---|---|
| **Feature** | **CompositionPlayer** | **ExoPlayer** |
| Input media | Takes a single Composition object, which can consist of multiple [EditedMediaItem](https://developer.android.com/reference/kotlin/androidx/media3/transformer/EditedMediaItem) instances with per-item effects. | Takes a single [MediaItem](https://developer.android.com/reference/androidx/media3/common/MediaItem) or a [playlist](https://developer.android.com/media/media3/exoplayer/playlists) of MediaItem instances. |
| Timeline | The timeline and duration are based on the entire Composition. | The timeline and duration correspond to the actively playing MediaItem. |
| Effects | Effects are defined within the Composition and can be applied to an individual EditedMediaItem or to the entire Composition. | Effects are set on the ExoPlayer instance itself with [setVideoEffects()](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer#setVideoEffects(java.util.List%3Candroidx.media3.common.Effect%3E)), and each effect is applied individually to each item in the playlist. |

In essence, `CompositionPlayer` is most helpful when you need to render a
complex `Composition` of media and effects, typically in an editing context. Use
`ExoPlayer` for general-purpose playback of audio or video content, or to
preview single-asset edits with `setVideoEffects()`.

## `CompositionPlayer` for preview

Integrating `CompositionPlayer` into your app involves a few key steps. First,
use the Builder pattern to instantiate a `CompositionPlayer`, then set the
`Composition` to be played:


```kotlin
val compositionPlayer = CompositionPlayer.Builder(context).build()
compositionPlayer.setComposition(composition)
compositionPlayer.prepare()
compositionPlayer.play()
```

<br />

For guidance on how to create a `Composition`, see the
[Create a `Composition`](https://developer.android.com/media/media3/transformer/composition#create-composition) section.

Note that since `CompositionPlayer` implements the `Player` interface, you can
then [set the target output](https://developer.android.com/media/media3/exoplayer/hello-world#attach-player) and [control the player](https://developer.android.com/media/media3/exoplayer/hello-world#control-player) through standard
`Player` methods.

> [!IMPORTANT]
> **Important:** The `CompositionPlayer` must be accessed from a single application thread. By default, this is the `Looper` of the thread that creates the player, or the application's main thread if the creation thread doesn't have a `Looper`. See [A note on threading](https://developer.android.com/media/media3/exoplayer/hello-world#a-note-on-threading) for more details.

### Error handling

Attach a [`Player.Listener`](https://developer.android.com/reference/androidx/media3/common/Player.Listener) instance to your `CompositionPlayer` to react
to playback events and errors. The [`onPlayerError()`](https://developer.android.com/reference/androidx/media3/common/Player.Listener#onPlayerError(androidx.media3.common.PlaybackException)) callback will also
surface any issues coming from editing-specific components like the
`Composition` or [`VideoGraph.Factory`](https://developer.android.com/reference/kotlin/androidx/media3/common/VideoGraph.Factory). Read the [Player events](https://developer.android.com/media/media3/exoplayer/listening-to-player-events)
documentation for more details.

## Important Considerations

Some features and limitations to keep in mind as you use `CompositionPlayer`:

- Although `CompositionPlayer` is based on the `Player` interface, some of its behaviors differ from `ExoPlayer` since it depends on a `Composition` for playback. For example, `CompositionPlayer` only supports setting the repeat mode to [`REPEAT_MODE_OFF`](https://developer.android.com/reference/androidx/media3/common/Player#REPEAT_MODE_OFF()) or [`REPEAT_MODE_ALL`](https://developer.android.com/reference/androidx/media3/common/Player#REPEAT_MODE_ALL()).
- By default, `CompositionPlayer` uses a [`SingleInputVideoGraph.Factory`](https://developer.android.com/reference/kotlin/androidx/media3/effect/SingleInputVideoGraph.Factory), but if your Composition uses more than one sequence with image or video items, you should use [`setVideoGraphFactory()`](https://developer.android.com/reference/kotlin/androidx/media3/transformer/CompositionPlayer.Builder#setVideoGraphFactory(androidx.media3.common.VideoGraph.Factory)) when building your `CompositionPlayer` instance to instead use a [`MultipleInputVideoGraph.Factory`](https://developer.android.com/reference/kotlin/androidx/media3/effect/MultipleInputVideoGraph.Factory). A `SingleInputVideoGraph.Factory` is sufficient if only one sequence has image or video items, and the others are audio-only.
- All the media items in your Composition should have a duration explicitly set, either with [`MediaItem.Builder.setImageDurationMs()`](https://developer.android.com/reference/kotlin/androidx/media3/common/MediaItem.Builder#setImageDurationMs(long)) for images, or with [`EditedMediaItem.Builder.setDurationUs()`](https://developer.android.com/reference/androidx/media3/transformer/EditedMediaItem.Builder#setDurationUs(long)) for audio or videos.

The following use cases are supported:

- Single-asset preview.
- Single-sequence (that is, sequential media items) preview.
- Single video sequence + Single audio sequence (for example, background audio) preview.

The following use cases are in active development:

- Multi-asset preview, including layouts such as picture-in-picture, side-by-side, and grid, where multiple video sequences are involved.
- Customizing the editing pipeline with a different graphics engine.

## Feature requests

If you have any feature requests or feedback for `CompositionPlayer`, file an
issue on the [Media3 GitHub repository](https://github.com/androidx/media/issues).