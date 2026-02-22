---
title: https://developer.android.com/media/media3/ui/compose-customization
url: https://developer.android.com/media/media3/ui/compose-customization
source: md.txt
---

The `media3-ui-compose` library provides the foundational components for
building a media UI in Jetpack Compose. It's designed for developers who need
more customization than what's offered by the `media3-ui-compose-material3`
library. This page explains how to use the core components and state holders to
create a custom media player UI.

## Mixing Material3 and custom Compose components

The `media3-ui-compose-material3` library is designed to be flexible. You can
use the prebuilt components for most of your UI, but swap out a single component
for a custom implementation when you need more control. This is when
`media3-ui-compose` library comes into play.

For example, imagine you want to use the standard
[`PreviousButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PreviousButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) and [`NextButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#NextButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) from the
Material3 library, but you need a completely custom `PlayPauseButton`. You can
achieve this by using [`PlayPauseButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,kotlin.Function1)) from the core `media3-ui-compose`
library and place it alongside the prebuilt components.

```kotlin
Row {
  // Use prebuilt component from the Media3 UI Compose Material3 library
  PreviousButton(player)
  // Use the scaffold component from Media3 UI Compose library
  PlayPauseButton(player) {
    // `this` is PlayPauseButtonState
    FilledTonalButton(
      onClick = {
        Log.d("PlayPauseButton", "Clicking on play-pause button")
        this.onClick()
      },
      enabled = this.isEnabled,
    ) {
      Icon(
        imageVector = if (showPlay) Icons.Default.PlayArrow else Icons.Default.Pause,
        contentDescription = if (showPlay) "Play" else "Pause",
      )
    }
  }
  // Use prebuilt component from the Media3 UI Compose Material3 library
  NextButton(player)
}
```

### Available components

The `media3-ui-compose` library provides a set of prebuilt composables for
common player controls. Here are some of the components you can use directly in
your app:

| Component | Description |
|---|---|
| [`PlayPauseButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that toggles between play and pause. |
| [`SeekBackButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#SeekBackButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that seeks backward by a defined increment. |
| [`SeekForwardButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#SeekForwardButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that seeks forward by a defined increment. |
| [`NextButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#NextButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that seeks to the next media item. |
| [`PreviousButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#PreviousButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that seeks to the previous media item. |
| [`RepeatButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#RepeatButton(androidx.media3.common.Player,kotlin.collections.List,kotlin.Function1)) | A state container for a button that cycles through repeat modes. |
| [`ShuffleButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#ShuffleButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that toggles shuffle mode. |
| [`MuteButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/buttons/package-summary#MuteButton(androidx.media3.common.Player,kotlin.Function1)) | A state container for a button that mutes and unmutes the player. |
| [`TimeText`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/indicators/package-summary#TimeText(androidx.media3.common.Player,kotlin.Int,kotlinx.coroutines.CoroutineScope,kotlin.Function1)) | A state container for a composable that displays the player progress. |
| [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0)) | A surface for displaying media content that handles aspect ratio management, resizing, and a shutter |
| [`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) | Raw surface which wraps `SurfaceView` and `TextureView` in `AndroidView`. |

## UI state holders

If none of the scaffolding components meet your needs, you can also use the
state objects directly. It's generally advisable to use the corresponding
`remember` methods to preserve your UI look between recompositions.

To better understand how you can use the flexibility of UI state holders versus
Composables, read about how Compose [manages State](https://developer.android.com/develop/ui/compose/state).

### Button state holders

For some UI states, the library makes the assumption that they will most likely
be consumed by button-like Composables.

| State | remember\*State | Type |
|---|---|---|
| [`PlayPauseButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/PlayPauseButtonState#PlayPauseButtonState(androidx.media3.common.Player)) | [`rememberPlayPauseButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberPlayPauseButtonState(androidx.media3.common.Player)) | 2-Toggle |
| [`PreviousButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/PreviousButtonState) | [`rememberPreviousButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberPreviousButtonState(androidx.media3.common.Player)) | Constant |
| [`NextButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/NextButtonState) | [`rememberNextButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberNextButtonState(androidx.media3.common.Player)) | Constant |
| [`RepeatButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/RepeatButtonState) | [`rememberRepeatButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberRepeatButtonState(androidx.media3.common.Player,kotlin.collections.List)) | 3-Toggle |
| [`ShuffleButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/ShuffleButtonState) | [`rememberShuffleButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberShuffleButtonState(androidx.media3.common.Player)) | 2-Toggle |
| [`PlaybackSpeedState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/PlaybackSpeedState) | [`rememberPlaybackSpeedState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/package-summary#rememberPlaybackSpeedState(androidx.media3.common.Player)) | Menu or N-Toggle |

Example usage of `PlayPauseButtonState`:

```kotlin
val state = rememberPlayPauseButtonState(player)

IconButton(onClick = state::onClick, modifier = modifier, enabled = state.isEnabled) {
  Icon(
    imageVector = if (state.showPlay) Icons.Default.PlayArrow else Icons.Default.Pause,
    contentDescription =
      if (state.showPlay)
        stringResource(androidx.media3.ui.compose.material3.R.string.playpause_button_play)
      else stringResource(androidx.media3.ui.compose.material3.R.string.playpause_button_pause),
  )
}
```

### Visual output state holders

[`PresentationState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/PresentationState) holds to information for when the video output in a
[`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) can be shown or should be covered by a placeholder UI element.
[`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0)) Composable combines the aspect ratio handling with taking care
of showing the shutter over a surface that is not ready yet.

```kotlin
@Composable
fun ContentFrame(
  player: Player?,
  modifier: Modifier = Modifier,
  surfaceType: @SurfaceType Int = SURFACE_TYPE_SURFACE_VIEW,
  contentScale: ContentScale = ContentScale.Fit,
  keepContentOnReset: Boolean = false,
  shutter: @Composable () -> Unit = { Box(Modifier.fillMaxSize().background(Color.Black)) },
) {
  val presentationState = rememberPresentationState(player, keepContentOnReset)
  val scaledModifier =
    modifier.resizeWithContentScale(contentScale, presentationState.videoSizeDp)

  // Always leave PlayerSurface to be part of the Compose tree because it will be initialised in
  // the process. If this composable is guarded by some condition, it might never become visible
  // because the Player won't emit the relevant event, e.g. the first frame being ready.
  PlayerSurface(player, scaledModifier, surfaceType)

  if (presentationState.coverSurface) {
    // Cover the surface that is being prepared with a shutter
    shutter()
  }
}
```

Here, we can use both `presentationState.videoSizeDp` to scale the Surface to
the chosen aspect ratio (see [ContentScale docs](https://developer.android.com/develop/ui/compose/graphics/images/customize#content-scale) for more types) and
`presentationState.coverSurface` to know when the timing is not right to be
showing the Surface. In this case, you can position an opaque shutter on top of
the surface, which will disappear when the surface becomes ready. `ContentFrame`
lets you customize the shutter as a trailing lambda, but by default it will be a
black `@Composable Box` filling the size of the parent container.

## Where are Flows?

Many Android developers are familiar with using Kotlin `Flow` objects to collect
ever-changing UI data. For example, you might be on the lookout for
`Player.isPlaying` flow that you can `collect` in a lifecycle-aware manner. Or
something like `Player.eventsFlow` to provide you with a `Flow<Player.Events>`
that you can `filter` the way you want.

However, using flows for `Player` UI state has some drawbacks. One of the main
concerns is the asynchronous nature of data transfer. We want to achieve as
little latency as possible between a `Player.Event` and its consumption on the
UI side, avoiding showing UI elements that are out-of-sync with the `Player`.

Other points include:

- A flow with all the `Player.Events` wouldn't adhere to a single responsibility principle, each consumer would have to filter out the relevant events.
- Creating a flow for each `Player.Event` will require you to combine them (with [`combine`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/combine.html)) for each UI element. There is a many-to-many mapping between a Player.Event and a UI element change. Having to use `combine` could lead the UI to potentially illegal states.

## Create custom UI states

You can add custom UI states if the existing ones don't fulfill your needs.
Check out the source code of the existing state to copy the pattern. A typical
UI state holder class does the following:

1. Takes in a [`Player`](https://developer.android.com/reference/androidx/media3/common/Player).
2. Subscribes to the `Player` using coroutines. See [`Player.listen`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#(androidx.media3.common.Player).listen(kotlin.Function2)) for more details.
3. Responds to particular [`Player.Events`](https://developer.android.com/reference/androidx/media3/common/Player.Events) by updating its internal state.
4. Accepts business-logic commands that will be transformed into an appropriate `Player` update.
5. Can be created in multiple places across the UI tree and will always maintain a consistent view of Player's state.
6. Exposes Compose `State` fields that can be consumed by a Composable to dynamically respond to changes.
7. Comes with a `remember*State` function for remembering the instance between compositions.

What happens behind the scenes:

    class SomeButtonState(private val player: Player) {
      var isEnabled by mutableStateOf(player.isCommandAvailable(Player.COMMAND_ACTION_A))
        private set

      var someField by mutableStateOf(someFieldDefault)
        private set

      fun onClick() {
        player.actionA()
      }

      suspend fun observe() =
        player.listen { events ->
          if (
            events.containsAny(
              Player.EVENT_B_CHANGED,
              Player.EVENT_C_CHANGED,
              Player.EVENT_AVAILABLE_COMMANDS_CHANGED,
            )
          ) {
            someField = this.someField
            isEnabled = this.isCommandAvailable(Player.COMMAND_ACTION_A)
          }
        }
    }

To react to your own `Player.Events`, you can catch them using [`Player.listen`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#(androidx.media3.common.Player).listen(kotlin.Function2))
which is a `suspend fun` that lets you enter the coroutine world and
indefinitely listen to `Player.Events`. Media3 implementation of various UI
states helps the end developer not to concern themselves with learning about
`Player.Events`.

> [!NOTE]
> **Note:** `Player` acts as a single source of truth. We shouldn't change `someField` externally because it will cause a divergence between the UI view of the world and that of the `Player`. Acting upon the button (for example, with a click) is an event that comes in. We react to it by sending the appropriate action to the `Player` without updating any fields locally. We receive the update from the `Player` in the form of a `Player.Event` and that updates the UI state. The UI element, like a button, that created the UI state locally, is able to extract the relevant information to display the correct UI element (icon, shape, content description, animation, etc.). Read more about [Compose State and unidirectional
> data flow](https://developer.android.com/develop/ui/compose/state).