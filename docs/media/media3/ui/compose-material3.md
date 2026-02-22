---
title: https://developer.android.com/media/media3/ui/compose-material3
url: https://developer.android.com/media/media3/ui/compose-material3
source: md.txt
---

The `media3-ui-compose-material3` library handles both the state management and
the Material3 styling internally. For more information on which library to use,
see the [Media3 Compose overview](https://developer.android.com/media/media3/ui/compose).

```kotlin
// The library provides styled UI components
Row {
  SeekBackButton(player)
  PlayPauseButton(player)
  SeekForwardButton(player)
}
```

```kotlin
// You can rearrange the composables into a layout that suits your needs
@Composable
fun PlayerProgressControlsLeftAligned(player: Player) {
  Row {
    PositionAndDurationText(player)
    ProgressSlider(player)
  }
}

@Composable
fun PlayerProgressControlsCenterAligned(player: Player) {
  Row {
    PositionText(player)
    ProgressSlider(player)
    DurationText(player)
  }
}
```

### Customize the Material3 Components

While `media3-ui-compose-material3` provides components that follow Material3
Design, you still have full control over theming. You can customize colors,
typography, and shapes by wrapping your player UI in a `MaterialTheme`.

For example, to change the color of the [`PlayPauseButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)), you can provide a
custom `colorScheme`:

```kotlin
MaterialTheme(
  colorScheme =
    lightColorScheme(
      primary = Color.Red, // Change the primary color for the button
      onPrimary = Color.White,
    )
) {
  // The PlayPauseButton will now use the custom colors
  PlayPauseButton(player)
}
```

### Available Material3 Components

The `media3-ui-compose-material3` library provides a set of prebuilt composables
for common player controls. Here are some of the components you can use directly
in your app:

| Component | Description |
|---|---|
| [`PlayPauseButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button that toggles between play and pause. |
| [`SeekBackButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#SeekBackButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek backward by a defined increment. |
| [`SeekForwardButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#SeekForwardButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek forward by a defined increment. |
| [`NextButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#NextButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek to the next media item. |
| [`PreviousButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PreviousButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek to the previous media item. |
| [`RepeatButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#RepeatButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.collections.List,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to cycle through repeat modes. |
| [`ShuffleButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#ShuffleButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to toggle shuffle mode. |
| [`MuteButton`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#MuteButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to mute and unmute the player. |
| [`PositionAndDurationText`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#PositionAndDurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.String,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the current position and total duration. |
| [`PositionText`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#PositionText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the current position. |
| [`DurationText`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#DurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the total duration. |
| [`RemainingDurationText`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#RemainingDurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Boolean,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the remaining duration. |
| [`ProgressSlider`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#ProgressSlider(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function0,kotlinx.coroutines.CoroutineScope)) | A slider that shows playback progress and allows the user to seek. |

*This is not an exhaustive list. Refer to the library's API reference for all
available components.*

Two other prebuilt Composables you are likely to need are related to the surface
management and they live in the `media3-ui-compose` module because they don't
possess Material theming.

| Component | Description |
|---|---|
| [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0)) | A surface for displaying media content that handles aspect ratio management, resizing, and a shutter |
| [`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) | Raw surface which wraps `SurfaceView` and `TextureView` in `AndroidView` |