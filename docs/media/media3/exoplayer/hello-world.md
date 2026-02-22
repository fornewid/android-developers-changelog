---
title: https://developer.android.com/media/media3/exoplayer/hello-world
url: https://developer.android.com/media/media3/exoplayer/hello-world
source: md.txt
---

> [!TIP]
> **Tip:** Another way to get started is to work through [the ExoPlayer codelab](https://codelabs.developers.google.com/codelabs/exoplayer-intro/).

For simple use cases, getting started with `ExoPlayer` consists of implementing
the following steps:

1. Add ExoPlayer as a dependency to your project.
2. Create an `ExoPlayer` instance.
3. Attach the player to a view (for video output and user input).
4. Prepare the player with a `MediaItem` to play.
5. Release the player when done.

These steps are described in more detail below. For a complete example, refer to
`PlayerActivity` in the [main demo app](https://github.com/androidx/media/tree/release/demos/main/).

## Add ExoPlayer as a dependency

### Add ExoPlayer modules

The easiest way to get started using AndroidX Media3 is to add gradle
dependencies on the libraries you need in the `build.gradle` file of your app
module.

For example, to depend on ExoPlayer with DASH playback support and UI components
you can add dependencies on the modules like this:

### Kotlin

```kotlin
implementation("androidx.media3:media3-exoplayer:1.9.2")
implementation("androidx.media3:media3-exoplayer-dash:1.9.2")
implementation("androidx.media3:media3-ui:1.9.2")
implementation("androidx.media3:media3-ui-compose:1.9.2")
```

### Groovy

```groovy
implementation "androidx.media3:media3-exoplayer:1.9.2"
implementation "androidx.media3:media3-exoplayer-dash:1.9.2"
implementation "androidx.media3:media3-ui:1.9.2"
implementation("androidx.media3:media3-ui-compose:1.9.2")
```

where 1.9.2 is your preferred version (the latest version can be found by
consulting the [release notes](https://github.com/androidx/media/tree/release/RELEASENOTES.md)). All modules must be of the same version.

AndroidX Media3 has library modules that depend on
external libraries to provide additional functionality. Some are
available from the Maven repository, whereas others must be built manually.
Browse the [libraries directory](https://github.com/androidx/media/tree/main/libraries) and see individual READMEs for details.

More information on the library modules that are available can be found on the
[Google Maven AndroidX Media page](https://maven.google.com/web/index.html#androidx.media3).

### Turn on Java 8 support

If not enabled already, you need to turn on at least Java 8 support in all
`build.gradle` files that depend on ExoPlayer, by adding the following to the
`android` section:

    compileOptions {
      targetCompatibility JavaVersion.VERSION_1_8
    }

## Create the player

You can create an `ExoPlayer` instance using `ExoPlayer.Builder`, which provides
a range of customization options. The following code is the simplest example of
creating an instance.

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context).build();
```

### A note on threading

ExoPlayer instances must be accessed from a single application thread. For the
vast majority of cases, this should be the application's main thread. Using the
application's main thread is a requirement when using ExoPlayer's UI components
or the IMA extension.

The thread on which an ExoPlayer instance must be accessed can be explicitly
specified by passing a `Looper` when creating the player. If no `Looper` is
specified, then the `Looper` of the thread that the player is created on is
used, or if that thread does not have a `Looper`, the `Looper` of the
application's main thread is used. In all cases, the `Looper` of the thread from
which the player must be accessed can be queried using
`Player.getApplicationLooper`.

> [!NOTE]
> **Note:** If you see `IllegalStateException` being thrown with the message "Player is accessed on the wrong thread", then some code in your app is accessing an `ExoPlayer` instance on the wrong thread (the exception's stack trace shows you where).

For more information about ExoPlayer's threading model, see the
["Threading model" section of the ExoPlayer Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer).

## Attach the player to a view

The ExoPlayer library provides a range of pre-built UI components for media
playback. These include `PlayerView`, which encapsulates a
`PlayerControlView`, a `SubtitleView`, and a `Surface` onto which video is
rendered. A `PlayerView` can be included in your application's layout xml.
For example, to bind the player to the view:

### Kotlin

```kotlin
// Bind the player to the view.
playerView.player = playerhttps://github.com/androidx/media/blob/74cdcf82895199e073861ed3b3dbccafba281aaf/docsamples/src/main/java/androidx/media3/docsamples/exoplayer/HelloWorld.kt#L37-L38
```

### Java

```java
// Bind the player to the view.
playerView.setPlayer(player);
```

Use of ExoPlayer's pre-built UI components is optional. For video apps that
implement their own UI, the target `SurfaceView`, `TextureView`, `SurfaceHolder`
or `Surface` can be set using ExoPlayer's `setVideoSurfaceView`,
`setVideoTextureView`, `setVideoSurfaceHolder`, and `setVideoSurface` methods
respectively. The `Listener.onCues` callback can be used to receive captions
that should be rendered during playback and `setImageOutput` can be used to
receive decoded images.

For a more comfortable user experience, consider adding the `keepScreenOn`
attribute. You can investigate other actions that keep the device awake in the
[background work pages](https://developer.android.com/develop/background-work/background-tasks/awake).

    android:keepScreenOn="true"

Read more about using Media3 UI components and their customisation on the [UI
page](https://developer.android.com/guide/topics/media/ui/overview).

## Populate the playlist and preparing the player

In ExoPlayer, every piece of media is represented by a `MediaItem`. To play a
piece of media, you need to build a corresponding `MediaItem`, add it to the
player, prepare the player, and call `play` to start the playback:

### Kotlin

```kotlin
// Build the media item.
val mediaItem = MediaItem.fromUri(videoUri)
// Set the media item to be played.
player.setMediaItem(mediaItem)
// Prepare the player.
player.prepare()
// Start the playback.
player.play()
```

### Java

```java
// Build the media item.
MediaItem mediaItem = MediaItem.fromUri(videoUri);
// Set the media item to be played.
player.setMediaItem(mediaItem);
// Prepare the player.
player.prepare();
// Start the playback.
player.play();
```

ExoPlayer supports playlists directly, so it's possible to prepare the player
with multiple media items to be played one after the other:

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

The playlist can be updated during playback without the need to prepare the
player again. Read more about populating and manipulating the playlist on the
[Playlists page](https://developer.android.com/guide/topics/media/exoplayer/playlists). Read more about the different options available when
building media items, such as clipping and attaching subtitle files, on the
[Media items page](https://developer.android.com/guide/topics/media/exoplayer/media-items).

> [!NOTE]
> **Note:** Media3 ExoPlayer converts media items to `MediaSource` instances that it needs internally. Read more about this process and how it can be customized on the [Media sources page](https://developer.android.com/guide/topics/media/exoplayer/media-sources). You can provide a `MediaSource` directly to the player using `ExoPlayer.setMediaSource(s)` and `ExoPlayer.addMediaSource(s)`.

## Control the player

Once the player has been prepared, playback can be controlled by calling methods
on the player. Here are some of the most commonly used methods:

- `play` and `pause` start and pause playback.
- `seekTo` allows seeking within the media.
- `hasPrevious`, `hasNext`, `previous` and `next` allow navigating through the playlist.
- `setRepeatMode` controls if and how media is looped.
- `setShuffleModeEnabled` controls playlist shuffling.
- `setPlaybackParameters` adjusts playback speed and audio pitch.

If the player is bound to a `PlayerView` or `PlayerControlView`,
then user interaction with these components will cause corresponding methods on
the player to be invoked.

## Release the player

It's important to release the player when it's no longer needed, so as to free
up limited resources such as video decoders for use by other applications. This
can be done by calling `ExoPlayer.release`.