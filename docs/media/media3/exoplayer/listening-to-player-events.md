---
title: https://developer.android.com/media/media3/exoplayer/listening-to-player-events
url: https://developer.android.com/media/media3/exoplayer/listening-to-player-events
source: md.txt
---

## Listening to playback events

Events, such as changes in state and playback errors, are reported to registered
[`Player.Listener`](https://developer.android.com/reference/androidx/media3/common/Player.Listener) instances. To register a listener to receive such events:

### Kotlin

```kotlin
// Add a listener to receive events from the player.
player.addListener(listener)
```

### Java

```java
// Add a listener to receive events from the player.
player.addListener(listener);
```

`Player.Listener` has empty default methods, so you only need to implement the
methods you're interested in. See the [Javadoc](https://developer.android.com/reference/androidx/media3/common/Player.Listener) for a full description of the
methods and when they're called. Some of the most important methods are
described in more detail below.

Listeners have the choice between implementing individual event callbacks or a
generic `onEvents` callback that's called after one or more events occur
together. See [`Individual callbacks vs onEvents`](https://developer.android.com/media/media3/exoplayer/listening-to-player-events#individual-callbacks) for an explanation of which
should be preferred for different use cases.

### Playback state changes

Changes in player state can be received by implementing
`onPlaybackStateChanged(@State int state)` in a registered `Player.Listener`.
The player can be in one of four playback states:

- `Player.STATE_IDLE`: This is the initial state, the state when the player is stopped, and when playback failed. The player will hold only limited resources in this state.
- `Player.STATE_BUFFERING`: The player is not able to immediately play from its current position. This mostly happens because more data needs to be loaded.
- `Player.STATE_READY`: The player is able to immediately play from its current position.
- `Player.STATE_ENDED`: The player finished playing all media.

In addition to these states, the player has a `playWhenReady` flag to indicate
the user intention to play. Changes in this flag can be received by implementing
`onPlayWhenReadyChanged(playWhenReady, @PlayWhenReadyChangeReason int reason)`.

A player is playing (that is, its position is advancing and media is being
presented to the user) when all three of the following conditions are met:

- The player is in the `Player.STATE_READY` state
- `playWhenReady` is `true`
- Playback is not suppressed for a reason returned by `Player.getPlaybackSuppressionReason`

Rather than having to check these properties individually, `Player.isPlaying`
can be called. Changes to this state can be received by implementing
`onIsPlayingChanged(boolean isPlaying)`:

### Kotlin

```kotlin
player.addListener(
  object : Player.Listener {
    override fun onIsPlayingChanged(isPlaying: Boolean) {
      if (isPlaying) {
        // Active playback.
      } else {
        // Not playing because playback is paused, ended, suppressed, or the player
        // is buffering, stopped or failed. Check player.playWhenReady,
        // player.playbackState, player.playbackSuppressionReason and
        // player.playerError for details.
      }
    }
  }
)
```

### Java

```java
player.addListener(
    new Player.Listener() {
      @Override
      public void onIsPlayingChanged(boolean isPlaying) {
        if (isPlaying) {
          // Active playback.
        } else {
          // Not playing because playback is paused, ended, suppressed, or the player
          // is buffering, stopped or failed. Check player.getPlayWhenReady,
          // player.getPlaybackState, player.getPlaybackSuppressionReason and
          // player.getPlaybackError for details.
        }
      }
    });
```

### Playback errors

Errors that cause playback to fail can be received by implementing
`onPlayerError(PlaybackException error)` in a registered `Player.Listener`. When
a failure occurs, this method will be called immediately before the playback
state transitions to `Player.STATE_IDLE`. Failed or stopped playbacks can be
retried by calling `ExoPlayer.prepare`.

Note that some [`Player`](https://developer.android.com/reference/androidx/media3/common/Player) implementations pass instances of subclasses of
`PlaybackException` to provide additional information about the failure. For
example, [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) passes [`ExoPlaybackException`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlaybackException), which has `type`,
`rendererIndex`, and other ExoPlayer-specific fields.

The following example shows how to detect when a playback has failed due to an
HTTP networking issue:

### Kotlin

```kotlin
player.addListener(
  object : Player.Listener {
    override fun onPlayerError(error: PlaybackException) {
      val cause = error.cause
      if (cause is HttpDataSourceException) {
        // An HTTP error occurred.
        val httpError = cause
        // It's possible to find out more about the error both by casting and by querying
        // the cause.
        if (httpError is InvalidResponseCodeException) {
          // Cast to InvalidResponseCodeException and retrieve the response code, message
          // and headers.
        } else {
          // Try calling httpError.getCause() to retrieve the underlying cause, although
          // note that it may be null.
        }
      }
    }
  }
)
```

### Java

```java
player.addListener(
    new Player.Listener() {
      @Override
      public void onPlayerError(PlaybackException error) {
        @Nullable Throwable cause = error.getCause();
        if (cause instanceof HttpDataSourceException) {
          // An HTTP error occurred.
          HttpDataSourceException httpError = (HttpDataSourceException) cause;
          // It's possible to find out more about the error both by casting and by querying
          // the cause.
          if (httpError instanceof HttpDataSource.InvalidResponseCodeException) {
            // Cast to InvalidResponseCodeException and retrieve the response code, message
            // and headers.
          } else {
            // Try calling httpError.getCause() to retrieve the underlying cause, although
            // note that it may be null.
          }
        }
      }
    });
```

### Playlist transitions

Whenever the player changes to a new media item in the playlist
`onMediaItemTransition(MediaItem mediaItem, @MediaItemTransitionReason int
reason)` is called on registered `Player.Listener` objects. The reason indicates
whether this was an automatic transition, a seek (for example after calling
`player.next()`), a repetition of the same item, or caused by a playlist change
(for example, if the currently playing item is removed).

### Metadata

Metadata returned from `player.getCurrentMediaMetadata()` can change due to many
reasons: playlist transitions, in-stream metadata updates or updating the
current `MediaItem` mid-playback.

If you are interested in metadata changes, for example to update a UI that shows
the current title, you can listen to `onMediaMetadataChanged`.

### Seeking

Calling `Player.seekTo` methods results in a series of callbacks to registered
`Player.Listener` instances:

1. `onPositionDiscontinuity` with `reason=DISCONTINUITY_REASON_SEEK`. This is the direct result of calling `Player.seekTo`. The callback has `PositionInfo` fields for the position before and after the seek.
2. `onPlaybackStateChanged` with any immediate state change related to the seek. Note that there might not be such a change.

### Individual callbacks versus `onEvents`

Listeners can choose between implementing individual callbacks like
`onIsPlayingChanged(boolean isPlaying)`, and the generic `onEvents(Player
player, Events events)` callback. The generic callback provides access to the
`Player` object and specifies the set of `events` that occurred together. This
callback is always called after the callbacks that correspond to the individual
events.

### Kotlin

```kotlin
override fun onEvents(player: Player, events: Player.Events) {
  if (
    events.contains(Player.EVENT_PLAYBACK_STATE_CHANGED) ||
      events.contains(Player.EVENT_PLAY_WHEN_READY_CHANGED)
  ) {
    uiModule.updateUi(player)
  }
}
```

### Java

```java
@Override
public void onEvents(Player player, Events events) {
  if (events.contains(Player.EVENT_PLAYBACK_STATE_CHANGED)
      || events.contains(Player.EVENT_PLAY_WHEN_READY_CHANGED)) {
    uiModule.updateUi(player);
  }
}
```

Individual events should be preferred in the following cases:

- The listener is interested in the reasons for changes. For example, the reasons provided for `onPlayWhenReadyChanged` or `onMediaItemTransition`.
- The listener only acts on the new values provided through callback parameters or triggers something else that doesn't depend on the callback parameters.
- The listener implementation prefers a clear readable indication of what triggered the event in the method name.
- The listener reports to an analytics system that needs to know about all individual events and state changes.

The generic `onEvents(Player player, Events events)` should be preferred in the
following cases:

- The listener wants to trigger the same logic for multiple events. For example, updating a UI for both `onPlaybackStateChanged` and `onPlayWhenReadyChanged`.
- The listener needs access the `Player` object to trigger further events, for example seeking after a media item transition.
- The listener intends to use multiple state values that are reported through separate callbacks together, or in combination with `Player` getter methods. For example, using `Player.getCurrentWindowIndex()` with the `Timeline` provided in `onTimelineChanged` is only safe from within the `onEvents` callback.
- The listener is interested in whether events logically occurred together. For example, `onPlaybackStateChanged` to `STATE_BUFFERING` because of a media item transition.

In some cases, listeners may need to combine the individual callbacks with the
generic `onEvents` callback, for example to record media item change reasons
with `onMediaItemTransition`, but only act once all state changes can be used
together in `onEvents`.

## Using `AnalyticsListener`

When using `ExoPlayer`, an `AnalyticsListener` can be registered with the player
by calling `addAnalyticsListener`. `AnalyticsListener` implementations are able
to listen to detailed events that may be useful for analytics and logging
purposes. Please refer to the [analytics page](https://developer.android.com/guide/topics/media/exoplayer/analytics) for more details.

### Using `EventLogger`

`EventLogger` is an `AnalyticsListener` provided directly by the library for
logging purposes. Add `EventLogger` to an `ExoPlayer` to enable useful
additional logging with a single line:

### Kotlin

```kotlin
player.addAnalyticsListener(EventLogger())
```

### Java

```java
player.addAnalyticsListener(new EventLogger());
```

See the [debug logging page](https://developer.android.com/guide/topics/media/exoplayer/debug-logging) for more details.

## Firing events at specified playback positions

Some use cases require firing events at specified playback positions. This is
supported using `PlayerMessage`. A `PlayerMessage` can be created using
`ExoPlayer.createMessage`. The playback position at which it should be executed
can be set using `PlayerMessage.setPosition`. Messages are executed on the
playback thread by default, but this can be customized using
`PlayerMessage.setLooper`. `PlayerMessage.setDeleteAfterDelivery` can be used to
control whether the message will be executed every time the specified playback
position is encountered (this may happen multiple times due to seeking and
repeat modes), or just the first time. Once the `PlayerMessage` is configured,
it can be scheduled using `PlayerMessage.send`.

### Kotlin

```kotlin
player
  .createMessage { messageType: Int, payload: Any? -> }
  .setLooper(Looper.getMainLooper())
  .setPosition(/* mediaItemIndex= */ 0, /* positionMs= */ 120000)
  .setPayload(customPayloadData)
  .setDeleteAfterDelivery(false)
  .send()
```

### Java

```java
player
    .createMessage(
        (messageType, payload) -> {
          // Do something at the specified playback position.
        })
    .setLooper(Looper.getMainLooper())
    .setPosition(/* mediaItemIndex= */ 0, /* positionMs= */ 120_000)
    .setPayload(customPayloadData)
    .setDeleteAfterDelivery(false)
    .send();
```