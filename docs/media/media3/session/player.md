---
title: https://developer.android.com/media/media3/session/player
url: https://developer.android.com/media/media3/session/player
source: md.txt
---

A player is the component of your app that facilitates playback of media items.
The Media3 [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player) interface
sets up an outline for functionality generally handled by a player. This
includes:

- Affecting playback controls, such as playing, pausing, and seeking
- Querying properties of the currently playing media, such as the playback position
- Managing a playlist/queue of media items
- Configuring playback properties, such as shuffling, repeating, speed, and volume
- Rendering video to the screen

Media3 also provides an implementation of the `Player` interface, called
[`ExoPlayer`](https://developer.android.com/guide/topics/media/exoplayer).
| **Tip:** If you're looking to implement a media player app using ExoPlayer, check out the [Create a basic media player app using Media3 ExoPlayer](https://developer.android.com/media/implement/playback-app) guide.

## A common interface between components

Several components in Media3 implement the Player interface, for example:

| Component | Description \& behavior notes |
|---|---|
| [`ExoPlayer`](https://developer.android.com/reference/kotlin/androidx/media3/exoplayer/ExoPlayer) | A media player API, and the default implementation of the `Player` interface. |
| [`MediaController`](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaController) | Interacts with a `MediaSession` to send playback commands. If your `Player` and `MediaSession` are in a `Service` separate from the `Activity` or `Fragment` where your player's UI lives, you can assign your `MediaController` as the player for your `PlayerView` UI. Playback and playlist method calls are sent to your `Player` through your `MediaSession`. |
| [`MediaBrowser`](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaBrowser) | In addition to the functionality offered by a `MediaController`, interacts with a `MediaLibrarySession` to browse available media content. |
| [`SimpleBasePlayer`](https://developer.android.com/reference/androidx/media3/common/SimpleBasePlayer) | A `Player` implementation that reduces the number of methods to implement to a minimum. Helpful when using a custom player that you want to connect to a `MediaSession`. |
| [`ForwardingSimpleBasePlayer`](https://developer.android.com/reference/androidx/media3/common/ForwardingSimpleBasePlayer) | A `SimpleBasePlayer` subclass designed to forward playback operations to another `Player` while allowing the same consistent behavior customizations as `SimpleBasePlayer`. Use this class to suppress or modify specific playback operations. |
| [`CastPlayer`](https://developer.android.com/reference/kotlin/androidx/media3/cast/CastPlayer) | A `Player` implementation that communicates with a Cast receiver app. Behavior depends on the underlying Cast session. |

Although a `MediaSession` doesn't implement the `Player` interface, it requires
a `Player` when creating one. Its purpose is to provide access to the `Player`
from other processes or threads.

### Media3 playback architecture

If you have access to a `Player`, you should call its methods directly to issue
playback commands. You can advertise your playback and grant external sources
playback control by implementing a `MediaSession`. These external sources
implement a `MediaController`, which facilitates connecting to a media session
and issuing playback command requests.

When playing media in the background, you need to house your media session and
player within a `MediaSessionService` or `MediaLibraryService` that runs as a
foreground service. If you do so, you can separate your player from the Activity
in your app that contains the UI for playback control. This may necessitate that
you use a media controller.
![A diagram showing how Media3 playback components fit into a media app architecture.](https://developer.android.com/static/guide/topics/media/images/backgroundplayback.png) **Figure 1** : The `Player` interface plays a key role in the architecture of Media3.

## Player state

The state of a media player implementing the `Player` interface consists
primarily of 4 categories of information:

1. Playback state
   - Retrieve with [`getPlaybackState()`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlaybackState()).
   - The state value defined by the interface are [`STATE_IDLE`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#STATE_IDLE()), [`STATE_BUFFERING`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#STATE_BUFFERING()), [`STATE_READY`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#STATE_READY()), and [`STATE_ENDED`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#STATE_ENDED()).
2. Playlist of media items
   - A sequence of `MediaItem` instances for playback.
   - Retrieve with [`getCurrentTimeline()`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentTimeline())
   - `Player` instances can provide playlist operation methods like [adding](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#addMediaItem(androidx.media3.common.MediaItem)) or [removing](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#removeMediaItem(int)) a `MediaItem` and convenience methods like [`getCurrentMediaItem()`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentMediaItem()).
3. Play/pause properties, such as:
   - [`playWhenReady`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlayWhenReady()): An indication of whether the user wants media to play when possible or remain paused
   - [Playback suppression reason](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlaybackSuppressionReason()): An indication of why playback is suppressed, if applicable, even if `playWhenReady` is `true`
   - [`isPlaying`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#isPlaying()): An indication of whether the player is currently playing, which will only be `true` if the playback state is `STATE_READY`, `playWhenReady` is `true`, and playback is not suppressed
4. Playback position, including:
   - [Current media item index](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentMediaItemIndex()): The index of the current `MediaItem` in the playlist.
   - [`isPlayingAd`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#isPlayingAd()): An indication of whether an inserted ad is playing.
   - [Current playback position](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentPosition()): The current playback position within the current `MediaItem` or inserted ad.

In addition, the `Player` interface allows access to the
[available tracks](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentTracks()),
[media metadata](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getMediaMetadata()),
[playback speed](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlaybackParameters()),
[volume](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getVolume()) and other
auxiliary properties of the playback.
| **Note:** `Player` instances don't have to support all features of the interface. You can check the [available commands](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#isCommandAvailable(int)) to see which feature is supported and which method is allowed to be called.

### Listen for changes

Use a [`Player.Listener`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player.Listener)
to listen for changes in a `Player`. See the ExoPlayer documentation on
[Player events](https://developer.android.com/guide/topics/media/exoplayer/listening-to-player-events) for
details on how to create and use a listener.

Note that the listener interface doesn't include any callbacks to track normal
playback progression. To continuously monitor playback progress, such as to set
up a progress bar UI, you should query the current position at proper intervals.  

### Kotlin

```kotlin
val handler = Handler(Looper.getMainLooper())
fun checkPlaybackPosition(delayMs: Long): Boolean =
  handler.postDelayed(
    {
      val currentPosition = player.currentPosition
      // Update UI based on currentPosition
      checkPlaybackPosition(delayMs)
    },
    delayMs)
```

### Java

```java
Handler handler = new Handler(Looper.getMainLooper());
boolean checkPlaybackPosition(long delayMs) {
    return handler.postDelayed(() -> {
        long currentPosition = player.getCurrentPosition();
        // Update UI based on currentPosition
        checkPlaybackPosition(delayMs);
    }, delayMs);
}
```

<br />

## Control playback

The `Player` interface offers many ways to manipulate the state and control
playback:

- [Basic playback controls](https://developer.android.com/guide/topics/media/exoplayer/hello-world#populate-playlist) like `play()`, `pause()`, `prepare()` and `stop()`.
- [Playlist operations](https://developer.android.com/guide/topics/media/exoplayer/playlists) like `addMediaItem()` or `removeMediaItem()`.
- [Seeking](https://developer.android.com/reference/androidx/media3/common/Player#seekTo(long)) to change the current item or position.
- Set [repeat modes](https://developer.android.com/guide/topics/media/exoplayer/playlists#repeat-modes) and the [shuffle mode](https://developer.android.com/guide/topics/media/exoplayer/playlists#shuffle-mode).
- Update [track selection preferences](https://developer.android.com/guide/topics/media/exoplayer/track-selection#modifying-track).
- Set the [playback speed](https://developer.android.com/reference/androidx/media3/common/Player#setPlaybackSpeed(float)).

| **Note:** `Player` instances don't have to support all features of the interface. You can check the [available commands](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#isCommandAvailable(int)) to see which feature is supported and which method is allowed to be called.

## Custom `Player` implementations

To create a custom player, you can extend the
[`SimpleBasePlayer`](https://developer.android.com/reference/androidx/media3/common/SimpleBasePlayer)
included in Media3. This class provides a base implementation of the `Player`
interface to reduce the number of methods you need to implement to a minimum.

Start by overriding the `getState()` method. This method should populate the
current player state when called, including:

- The set of available commands
- Playback properties, such as whether the player should start playing when the playback state is `STATE_READY`, the index of the currently playing media item, and the playback position within the current item

### Kotlin

```kotlin
class CustomPlayer : SimpleBasePlayer(looper) {
  override fun getState(): State {
    return State.Builder()
      .setAvailableCommands(...) // Set which playback commands the player can handle
      // Configure additional playback properties
      .setPlayWhenReady(true, PLAY_WHEN_READY_CHANGE_REASON_USER_REQUEST)
      .setCurrentMediaItemIndex(0)
      .setContentPositionMs(0)
      .build()
  }
}
```

### Java

```java
public class CustomPlayer extends SimpleBasePlayer {
  public CustomPlayer(Looper looper) {
    super(looper);
  }

  @Override
  protected State getState() {
    return new State.Builder()
      .setAvailableCommands(...) // Set which playback commands the player can handle
      // Configure additional playback properties
      .setPlayWhenReady(true, PLAY_WHEN_READY_CHANGE_REASON_USER_REQUEST)
      .setCurrentMediaItemIndex(0)
      .setContentPositionMs(0)
      .build();
  }
}
```

<br />

`SimpleBasePlayer` will enforce that the `State` is created with a valid
combination of state values. It will also handle listeners and informing
listeners of state changes. If you need to manually trigger a state update,
call [`invalidateState()`](https://developer.android.com/reference/androidx/media3/common/SimpleBasePlayer#invalidateState()).

Beyond the `getState()` method, you only need to implement methods that are used
for commands your player declares to be available. Find the overridable handler
method that corresponds to the functionality you want to implement. For example,
override the [`handleSeek()`](https://developer.android.com/reference/androidx/media3/common/SimpleBasePlayer#handleSeek(int,long,int))
method to support operations like [`COMMAND_SEEK_IN_CURRENT_MEDIA_ITEM`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_IN_CURRENT_MEDIA_ITEM())
and [`COMMAND_SEEK_TO_NEXT_MEDIA_ITEM`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_TO_NEXT_MEDIA_ITEM()).

### Modify `Player` implementations

Instead of creating a completely custom `Player`, you can use
`ForwardingSimpleBasePlayer` to modify the state and behavior of an existing
`Player`. See the guide on the [Customization page](https://developer.android.com/media/media3/exoplayer/customization#player-operations) for
more details.