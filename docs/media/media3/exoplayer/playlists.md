---
title: Playlists  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/playlists
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Playlists Stay organized with collections Save and categorize content based on your preferences.



The playlist API is defined by the `Player` interface, which is implemented by
all `ExoPlayer` implementations. Playlists enable sequential playback of
multiple media items. The following example shows how to start playback of a
playlist
containing two videos:

### Kotlin

```
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

Playlists.kt
```

### Java

```
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

Playlists.java
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

```
// Adds a media item at position 1 in the playlist.
player.addMediaItem(/* index= */ 1, MediaItem.fromUri(thirdUri))
// Moves the third media item from position 2 to the start of the playlist.
player.moveMediaItem(/* currentIndex= */ 2, /* newIndex= */ 0)
// Removes the first item from the playlist.
player.removeMediaItem(/* index= */ 0)
// Replace the second item in the playlist.
player.replaceMediaItem(/* index= */ 1, MediaItem.fromUri(newUri))

Playlists.kt
```

### Java

```
// Adds a media item at position 1 in the playlist.
player.addMediaItem(/* index= */ 1, MediaItem.fromUri(thirdUri));
// Moves the third media item from position 2 to the start of the playlist.
player.moveMediaItem(/* currentIndex= */ 2, /* newIndex= */ 0);
// Removes the first item from the playlist.
player.removeMediaItem(/* index= */ 0);
// Replace the second item in the playlist.
player.replaceMediaItem(/* index= */ 1, MediaItem.fromUri(newUri));

Playlists.java
```

Replacing and clearing the entire playlist are also supported:

### Kotlin

```
// Replaces the playlist with a new one.
val newItems: List<MediaItem> =
  listOf(MediaItem.fromUri(fourthUri), MediaItem.fromUri(fifthUri))
player.setMediaItems(newItems, /* resetPosition= */ true)
// Clears the playlist. If prepared, the player transitions to the ended state.
player.clearMediaItems()

Playlists.kt
```

### Java

```
// Replaces the playlist with a new one.
ImmutableList<MediaItem> newItems =
    ImmutableList.of(MediaItem.fromUri(fourthUri), MediaItem.fromUri(fifthUri));
player.setMediaItems(newItems, /* resetPosition= */ true);
// Clears the playlist. If prepared, the player transitions to the ended state.
player.clearMediaItems();

Playlists.java
```

The player automatically handles modifications during playback in the correct
way:

* If the currently playing `MediaItem` is moved, playback is not interrupted and
  its new successor will be played upon completion.
* If the currently playing `MediaItem` is removed, the player will automatically
  play the first remaining successor, or transition to the ended state if no
  such successor exists.
* If the currently playing `MediaItem` is replaced, playback is not interrupted
  if none of the properties in the `MediaItem` relevant for the playback
  changed. For example, it's possible to update the `MediaItem.MediaMetadata`
  fields in most cases without affecting playback.

## Querying the playlist

The playlist can be queried using `Player.getMediaItemCount` and
`Player.getMediaItemAt`. The currently playing media item can be queried
by calling `Player.getCurrentMediaItem`. There are also other convenience
methods like `Player.hasNextMediaItem` or `Player.getNextMediaItemIndex` to
simplify navigation in the playlist.

## Repeat modes

The player supports 3 repeat modes that can be set at any time with
`Player.setRepeatMode`:

* `Player.REPEAT_MODE_OFF`: The playlist isn't repeated and the player will
  transition to `Player.STATE_ENDED` once the last item in the playlist has
  been played.
* `Player.REPEAT_MODE_ONE`: The current item is repeated in an endless loop.
  Methods like `Player.seekToNextMediaItem` will ignore this and seek to the
  next item in the list, which will then be repeated in an endless loop.
* `Player.REPEAT_MODE_ALL`: The entire playlist is repeated in an endless loop.

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

```
// Set a custom shuffle order for the 5 items currently in the playlist:
exoPlayer.setShuffleOrder(DefaultShuffleOrder(intArrayOf(3, 1, 0, 4, 2), randomSeed))
// Enable shuffle mode.
exoPlayer.shuffleModeEnabled = true

Playlists

.kt
```