---
title: https://developer.android.com/media/media3/ui/playerview
url: https://developer.android.com/media/media3/ui/playerview
source: md.txt
---

## Add the dependency

### Kotlin

    implementation("androidx.media3:media3-ui:1.9.2")

### Groovy

    implementation "androidx.media3:media3-ui:1.9.2"

## PlayerView

The most important component is [`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView), a view for media playback.
`PlayerView` displays video, images, subtitles, and album art during playback,
as well as playback controls.

`PlayerView` has a [`setPlayer()`](https://developer.android.com/reference/androidx/media3/ui/PlayerView#setPlayer(androidx.media3.common.Player)) method for attaching and detaching (by
passing `null`) [`Player`](https://developer.android.com/reference/androidx/media3/common/Player) instances.

`PlayerView` can be used for both video, image and audio playbacks. It renders
video and subtitles in the case of video playback, bitmaps for image playback
and can display artwork included as metadata in audio files. You can include it
in your layout files like any other UI component. For example, a `PlayerView`
can be included with the following XML:  

    <androidx.media3.ui.PlayerView
        android:id="@+id/player_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:show_buffering="when_playing"
        app:show_shuffle_button="true"/>

The snippet above illustrates that `PlayerView` provides several attributes.
These attributes can be used to customize the view's behavior, as well as its
look and feel. Most of these attributes have corresponding setter methods, which
can be used to customize the view at runtime. The `PlayerView` documentation
lists these attributes and setter methods in more detail.

For a more comfortable user experience, consider adding the `keepScreenOn`
Android attribute or [setting a wake lock](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer#setWakeMode(int)), if you are using ExoPlayer. You
can investigate other actions that keep the device awake in the [background work
pages](https://developer.android.com/develop/background-work/background-tasks/awake).  

    android:keepScreenOn="true"

Once the view is declared in the layout file, it can be looked up in the
`onCreate` method of the activity:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  // ...
  playerView = findViewById(R.id.player_view)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  // ...
  playerView = findViewById(R.id.player_view);
}
```

<br />

When a player has been initialized, it can be attached to the view by calling
`setPlayer`:  

### Kotlin

```kotlin
// Instantiate the player.
val player = ExoPlayer.Builder(context).build()
// Attach player to the view.
playerView.player = player
// Set the media item to be played.
player.setMediaItem(mediaItem)
// Prepare the player.
player.prepare()
```

### Java

```java
// Instantiate the player.
player = new ExoPlayer.Builder(context).build();
// Attach player to the view.
playerView.setPlayer(player);
// Set the media item to be played.
player.setMediaItem(mediaItem);
// Prepare the player.
player.prepare();
```

<br />

### PlayerControlView

[`PlayerControlView`](https://developer.android.com/reference/androidx/media3/ui/PlayerControlView) is one of `PlayerView` sub-Views that contains the
progress bar and buttons to control playback. Note that `PlayerControlView` is
not intended to be used a standalone component outside of `PlayerView`. It can
be customized by setting attributes on `PlayerView` (which will be passed onto
`PlayerControlView`) or providing a custom controller with
`android:id="@id/exo_controller`.

### Choose a surface type

The `surface_type` attribute of `PlayerView` lets you set the type of surface
used for video playback. The allowed values are `surface_view`, `texture_view`,
`spherical_gl_surface_view` (which is a special value for spherical video
playback), `video_decoder_gl_surface_view` (which is for video rendering using
extension renderers) and `none` (for audio playback only). More information on
which surface type to pick can be found [on the Surface page](https://developer.android.com/media/media3/ui/surface).