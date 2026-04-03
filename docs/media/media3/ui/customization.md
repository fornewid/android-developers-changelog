---
title: UI customizations  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/ui/customization
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# UI customizations Stay organized with collections Save and categorize content based on your preferences.




Media3 provides a default [`PlayerView`](/guide/topics/media/ui/playerview) that provides some customization
options.

## Override drawables

**Caution:** We don't guarantee that the customizations described in the following
section will continue to work in future versions of the library. The resource
IDs may change name, or some may be deleted entirely. This is indicated by the
[resource IDs being marked 'private'](/studio/projects/android-library#PrivateResources).

`PlayerView` uses `PlayerControlView` to display the playback controls and
progress bar. The drawables used by `PlayerControlView` can be overridden by
drawables with the same names defined in your application. See the
[`PlayerControlView`](/reference/androidx/media3/ui/PlayerControlView) documentation for a list of control drawables that can
be overridden.

For any further customization, app developers are expected to implement their
own UI components. However, here are some best practices that can help you get
started.

## Best practices

When implementing a media UI that connects to a Media3 `Player` (for example
`ExoPlayer`, `MediaController` or a custom `Player` implementation), apps are
advised to follow these best practices for the best UI experience.

### Play/Pause button

The play and pause button does not directly correspond to a single player state.
For example, a user should be able to restart playback after it ended or failed
even if the player isn't paused.

To simplify the implementation, Media3 provides util methods to decide which
button to show (`Util.shouldShowPlayButton`) and to handle button presses
(`Util.handlePlayPauseButtonAction`):

### Kotlin

```
val shouldShowPlayButton: Boolean = Util.shouldShowPlayButton(player)
playPauseButton.setImageDrawable(if (shouldShowPlayButton) playDrawable else pauseDrawable)
playPauseButton.setOnClickListener { Util.handlePlayPauseButtonAction(player) }

UiCustomization.kt
```

### Java

```
boolean shouldShowPlayButton = Util.shouldShowPlayButton(player);
playPauseButton.setImageDrawable(shouldShowPlayButton ? playDrawable : pauseDrawable);
playPauseButton.setOnClickListener(view -> Util.handlePlayPauseButtonAction(player));

UiCustomization.java
```

### Listen to state updates

The UI component needs to add a `Player.Listener` to be informed of state
changes that require a corresponding UI update. See [Listen to playback
events](/guide/topics/media/exoplayer/listening-to-player-events) for details.

Refreshing the UI can be costly and multiple player events often arrive
together. To avoid refreshing the UI too often in a short period of time, it's
generally better to listen to just `onEvents` and trigger UI updates from there:

### Kotlin

```
player.addListener(
  object : Player.Listener {
    override fun onEvents(player: Player, events: Player.Events) {
      if (
        events.containsAny(
          Player.EVENT_PLAY_WHEN_READY_CHANGED,
          Player.EVENT_PLAYBACK_STATE_CHANGED,
          Player.EVENT_PLAYBACK_SUPPRESSION_REASON_CHANGED,
        )
      ) {
        updatePlayPauseButton()
      }
      if (events.containsAny(Player.EVENT_REPEAT_MODE_CHANGED)) {
        updateRepeatModeButton()
      }
    }
  }
)

UiCustomization.kt
```

### Java

```
player.addListener(
    new Player.Listener() {
      @Override
      public void onEvents(Player player, Player.Events events) {
        if (events.containsAny(
            Player.EVENT_PLAY_WHEN_READY_CHANGED,
            Player.EVENT_PLAYBACK_STATE_CHANGED,
            Player.EVENT_PLAYBACK_SUPPRESSION_REASON_CHANGED)) {
          updatePlayPauseButton();
        }
        if (events.containsAny(Player.EVENT_REPEAT_MODE_CHANGED)) {
          updateRepeatModeButton();
        }
      }
    });

UiCustomization.java
```

### Handle available commands

A general purpose UI component that may need to work with different `Player`
implementations should check the available player commands to show or hide
buttons and to avoid calling unsupported methods:

### Kotlin

```
nextButton.isEnabled = player.isCommandAvailable(COMMAND_SEEK_TO_NEXT)

UiCustomization.kt
```

### Java

```
nextButton.setEnabled(player.isCommandAvailable(COMMAND_SEEK_TO_NEXT));

UiCustomization.java
```

### First frame shutter and image display

When a UI component displays video or images, it typically uses a placeholder
shutter view until the real first frame or image is available. In addition,
mixed video and image playback requires to hide and show the image view at
appropriate times.

A common pattern to handle these updates is to listen to
[`Player.Listener.onEvents()`](/reference/androidx/media3/exoplayer/Player.Listener#onEvents(androidx.media3.exoplayer.Player,%20androidx.media3.exoplayer.Player.Events)) for any change in selected tracks
(`EVENT_TRACKS_CHANGED`) and for when the first video frame has been rendered
(`EVENT_RENDERED_FIRST_FRAME`), as well as [`ImageOutput.onImageAvailable()`](/reference/androidx/media3/ui/ImageOutput#onImageAvailable(long,%20android.graphics.Bitmap))
for when a new image is available:

### Kotlin

```
override fun onEvents(player: Player, events: Player.Events) {
  if (events.contains(Player.EVENT_TRACKS_CHANGED)) {
    // If no video or image track: show shutter, hide image view.
    // Otherwise: do nothing to wait for first frame or image.
  }
  if (events.contains(Player.EVENT_RENDERED_FIRST_FRAME)) {
    // Hide shutter, hide image view.
  }
}

override fun onImageAvailable(presentationTimeUs: Long, bitmap: Bitmap) {
  // Show shutter, set image and show image view.
}

UiCustomization.kt
```

### Java

```
@Override
public void onEvents(Player player, Player.Events events) {
  if (events.contains(Player.EVENT_TRACKS_CHANGED)) {
    // If no video or image track: show shutter, hide image view.
    // Otherwise: do nothing to wait for first frame or image.
  }
  if (events.contains(Player.EVENT_RENDERED_FIRST_FRAME)) {
    // Hide shutter, hide image view.
  }
}

@Override
public void onImageAvailable(long presentationTimeUs, Bitmap bitmap) {
  // Show shutter, set image and show image view.
}

UiCustomization.java
```