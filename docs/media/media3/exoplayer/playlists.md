---
title: https://developer.android.com/media/media3/exoplayer/playlists
url: https://developer.android.com/media/media3/exoplayer/playlists
source: md.txt
---

The playlist API is defined by the `Player` interface, which is implemented by
all `ExoPlayer` implementations. Playlists enable sequential playback of
multiple media items. The following example shows how to start playback of a
playlist
containing two videos:

### Kotlin

```kotlin
// Build the media items.
val firstItem = MediaItem.fromUri(firstVideoUri)
val secondItem = MediaItem.fromUri(secondVideoUri)
// Add the media items to be played.
player.addMediaItem(firstItem)
player.addMediaItem(secondItem)
// Prepare the player.
player.prepare()
// Start the playback.
player.play()
```

### Java

```java
// Build the media items.
MediaItem firstItem = MediaItem.fromUri(firstVideoUri);
MediaItem secondItem = MediaItem.fromUri(secondVideoUri);
// Add the media items to be played.
player.addMediaItem(firstItem);
player.addMediaItem(secondItem);
// Prepare the player.
player.prepare();
// Start the playback.
player.play();
```

Transitions between items in a playlist are seamless. There's no requirement
that they're of the same format (for example, it's fine for a playlist to contain both
H264 and VP9 videos). They may even be of different types (that is, it's fine for a
playlist to contain videos, images and audio only streams). You can use the
same `MediaItem` multiple times within a playlist.

## Modifying the playlist

You can dynamically modify a playlist by adding, moving, removing or replacing
media items. This can be done both before and during playback by calling the
corresponding playlist API methods:

### Kotlin

```kotlin
// Adds a media item at position 1 in the playlist.
player.addMediaItem(/* index= */ 1, MediaItem.fromUri(thirdUri))
// Moves the third media item from position 2 to the start of the playlist.
player.moveMediaItem(/* currentIndex= */ 2, /* newIndex= */ 0)
// Removes the first item from the playlist.
player.removeMediaItem(/* index= */ 0)
// Replace the second item in the playlist.
player.replaceMediaItem(/* index= */ 1, MediaItem.fromUri(newUri))
```

### Java

```java
// Adds a media item at position 1 in the playlist.
player.addMediaItem(/* index= */ 1, MediaItem.fromUri(thirdUri));
// Moves the third media item from position 2 to the start of the playlist.
player.moveMediaItem(/* currentIndex= */ 2, /* newIndex= */ 0);
// Removes the first item from the playlist.
player.removeMediaItem(/* index= */ 0);
// Replace the second item in the playlist.
player.replaceMediaItem(/* index= */ 1, MediaItem.fromUri(newUri));
```

Replacing and clearing the entire playlist are also supported:

### Kotlin

```kotlin
// Replaces the playlist with a new one.
val newItems: List<MediaItem> =
  listOf(MediaItem.fromUri(fourthUri), MediaItem.fromUri(fifthUri))
player.setMediaItems(newItems, /* resetPosition= */ true)
// Clears the playlist. If prepared, the player transitions to the ended state.
player.clearMediaItems()
```

### Java

```java
// Replaces the playlist with a new one.
ImmutableList<MediaItem> newItems =
    ImmutableList.of(MediaItem.fromUri(fourthUri), MediaItem.fromUri(fifthUri));
player.setMediaItems(newItems, /* resetPosition= */ true);
// Clears the playlist. If prepared, the player transitions to the ended state.
player.clearMediaItems();
```

The player automatically handles modifications during playback in the correct
way:

- If the currently playing `MediaItem` is moved, playback is not interrupted and its new successor will be played upon completion.
- If the currently playing `MediaItem` is removed, the player will automatically play the first remaining successor, or transition to the ended state if no such successor exists.
- If the currently playing `MediaItem` is replaced, playback is not interrupted if none of the properties in the `MediaItem` relevant for the playback changed. For example, it's possible to update the `MediaItem.MediaMetadata` fields in most cases without affecting playback.

## Querying the playlist

The playlist can be queried using `Player.getMediaItemCount` and
`Player.getMediaItemAt`. The currently playing media item can be queried
by calling `Player.getCurrentMediaItem`. There are also other convenience
methods like `Player.hasNextMediaItem` or `Player.getNextMediaItemIndex` to
simplify navigation in the playlist.

## Repeat modes

The player supports 3 repeat modes that can be set at any time with
`Player.setRepeatMode`:

- `Player.REPEAT_MODE_OFF`: The playlist isn't repeated and the player will transition to `Player.STATE_ENDED` once the last item in the playlist has been played.
- `Player.REPEAT_MODE_ONE`: The current item is repeated in an endless loop. Methods like `Player.seekToNextMediaItem` will ignore this and seek to the next item in the list, which will then be repeated in an endless loop.
- `Player.REPEAT_MODE_ALL`: The entire playlist is repeated in an endless loop.

## Shuffle mode

Shuffle mode can be enabled or disabled at any time with
`Player.setShuffleModeEnabled`. When in shuffle mode, the player will play the
playlist in a precomputed, randomized order. All items will be played once and
the shuffle mode can also be combined with `Player.REPEAT_MODE_ALL` to repeat
the same randomized order in an endless loop. When shuffle mode is turned off,
playback continues from the current item at its original position in the
playlist.

Note that the indices as returned by methods like
`Player.getCurrentMediaItemIndex` always refer to the original, unshuffled
order. Similarly, `Player.seekToNextMediaItem` will not play the item at
`player.getCurrentMediaItemIndex() + 1`, but the next item according to the
shuffle order. Inserting new items in the playlist or removing items will keep
the existing shuffled order unchanged as far as possible.

### Setting a custom shuffle order

By default, the player supports shuffling by using the `DefaultShuffleOrder`.
This can be customized by providing a custom shuffle order implementation, or by
setting a custom order in the `DefaultShuffleOrder` constructor:

### Kotlin

```kotlin
// Set a custom shuffle order for the 5 items currently in the playlist:
exoPlayer.setShuffleOrder(DefaultShuffleOrder(intArrayOf(3, 1, 0, 4, 2), randomSeed))
// Enable shuffle mode.
exoPlayer.shuffleModeEnabled = truehttps://github.com/androidx/media/blob/42042a121d7c87975ee645747ef0b8323debb5c1/docsamples/src/main/java/androidx/media3/docsamples/exoplayer/Playlists.kt#L77-L80
```

### Java

```java
// Set a custom shuffle order for the 5 items currently in the playlist:
exoPlayer.setShuffleOrder(new DefaultShuffleOrder(new int[] {3, 1, 0, 4, 2}, randomSeed));
// Enable shuffle mode.
exoPlayer.setShuffleModeEnabled(/* shuffleModeEnabled= */ true);
```

## Identifying playlist items

To identify playlist items, `MediaItem.mediaId` can be set when building the
item:

### Kotlin

```kotlin
// Build a media item with a media ID.
val mediaItem = MediaItem.Builder().setUri(uri).setMediaId(mediaId).build()
```

### Java

```java
// Build a media item with a media ID.
MediaItem mediaItem = new MediaItem.Builder().setUri(uri).setMediaId(mediaId).build();
```

If an app does not explicitly define a media ID for a media item, the string
representation of the URI is used.

## Associating app data with playlist items

In addition to an ID, each media item can also be configured with a custom tag,
which can be any app provided object. One use of custom tags is to attach
metadata to each media item:

### Kotlin

```kotlin
// Build a media item with a custom tag.
val mediaItem = MediaItem.Builder().setUri(uri).setTag(metadata).build()
```

### Java

```java
// Build a media item with a custom tag.
MediaItem mediaItem = new MediaItem.Builder().setUri(uri).setTag(metadata).build();
```

## Detecting when playback transitions to another media item

When playback transitions to another media item, or starts repeating the same
media item, `Listener.onMediaItemTransition(MediaItem,
@MediaItemTransitionReason)` is called. This callback receives the new media
item, along with a `@MediaItemTransitionReason` indicating why the transition
occurred. A common use case for `onMediaItemTransition` is to update the
app's UI for the new media item:

### Kotlin

```kotlin
override fun onMediaItemTransition(
  mediaItem: MediaItem?,
  @MediaItemTransitionReason reason: Int,
) {
  updateUiForPlayingMediaItem(mediaItem)
}
```

### Java

```java
@Override
public void onMediaItemTransition(
    @Nullable MediaItem mediaItem, @MediaItemTransitionReason int reason) {
  updateUiForPlayingMediaItem(mediaItem);
}
```

If the metadata required to update the UI is attached to each media item using
custom tags, then an implementation might look like:

### Kotlin

```kotlin
override fun onMediaItemTransition(
  mediaItem: MediaItem?,
  @MediaItemTransitionReason reason: Int,
) {
  var metadata: CustomMetadata? = null
  mediaItem?.localConfiguration?.let { localConfiguration ->
    metadata = localConfiguration.tag as? CustomMetadata
  }
  updateUiForPlayingMediaItem(metadata)
}
```

### Java

```java
@Override
public void onMediaItemTransition(
    @Nullable MediaItem mediaItem, @MediaItemTransitionReason int reason) {
  @Nullable CustomMetadata metadata = null;
  if (mediaItem != null && mediaItem.localConfiguration != null) {
    metadata = (CustomMetadata) mediaItem.localConfiguration.tag;
  }
  updateUiForPlayingMediaItem(metadata);
}
```

## Detecting when the playlist changes

When a media item is added, removed or moved,
`Listener.onTimelineChanged(Timeline, @TimelineChangeReason)` is called
immediately with `TIMELINE_CHANGE_REASON_PLAYLIST_CHANGED`. This callback is
called even when the player has not yet been prepared.

### Kotlin

```kotlin
override fun onTimelineChanged(timeline: Timeline, @TimelineChangeReason reason: Int) {
  if (reason == Player.TIMELINE_CHANGE_REASON_PLAYLIST_CHANGED) {
    // Update the UI according to the modified playlist (add, move or remove).
    updateUiForPlaylist(timeline)
  }
}
```

### Java

```java
@Override
public void onTimelineChanged(Timeline timeline, @TimelineChangeReason int reason) {
  if (reason == TIMELINE_CHANGE_REASON_PLAYLIST_CHANGED) {
    // Update the UI according to the modified playlist (add, move or remove).
    updateUiForPlaylist(timeline);
  }
}
```

When information such as the duration of a media item in the playlist becomes
available, the `Timeline` will be updated and `onTimelineChanged` will be called
with `TIMELINE_CHANGE_REASON_SOURCE_UPDATE`. Other reasons that can cause a
timeline update include:

- A manifest becoming available after preparing an adaptive media item.
- A manifest being updated periodically during playback of a live stream.