---
title: Material3 Compose  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/ui/compose-material3
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Material3 Compose Stay organized with collections Save and categorize content based on your preferences.



The `media3-ui-compose-material3` library handles both the state management and
the Material3 styling internally. For more information on which library to use,
see the [Media3 Compose overview](/media/media3/ui/compose).

```
// The library provides styled UI components
Row {
  SeekBackButton(player)
  PlayPauseButton(player)
  SeekForwardButton(player)
}

ComposeMaterial3.kt
```

```
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

ComposeMaterial3.kt
```

### Customize the Material3 Components

While `media3-ui-compose-material3` provides components that follow Material3
Design, you still have full control over theming. You can customize colors,
typography, and shapes by wrapping your player UI in a `MaterialTheme`.

For example, to change the color of the [`PlayPauseButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)), you can provide a
custom `colorScheme`:

```
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

ComposeMaterial3.kt
```

### Available Material3 Components

The `media3-ui-compose-material3` library provides a set of prebuilt composables
for common player controls. Here are some of the components you can use directly
in your app:

| Component | Description |
| --- | --- |
| [`PlayPauseButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PlayPauseButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button that toggles between play and pause. |
| [`SeekBackButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#SeekBackButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek backward by a defined increment. |
| [`SeekForwardButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#SeekForwardButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek forward by a defined increment. |
| [`NextButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#NextButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek to the next media item. |
| [`PreviousButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#PreviousButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to seek to the previous media item. |
| [`RepeatButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#RepeatButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.collections.List,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to cycle through repeat modes. |
| [`ShuffleButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#ShuffleButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to toggle shuffle mode. |
| [`MuteButton`](/reference/kotlin/androidx/media3/ui/compose/material3/buttons/package-summary#MuteButton(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,androidx.compose.ui.graphics.Color,kotlin.Function1)) | A button to mute and unmute the player. |
| [`PositionAndDurationText`](/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#PositionAndDurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.String,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the current position and total duration. |
| [`PositionText`](/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#PositionText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the current position. |
| [`DurationText`](/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#DurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the total duration. |
| [`RemainingDurationText`](/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#RemainingDurationText(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Boolean,kotlinx.coroutines.CoroutineScope)) | A text composable that displays the remaining duration. |
| [`ProgressSlider`](/reference/kotlin/androidx/media3/ui/compose/material3/indicator/package-summary#ProgressSlider(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function0,kotlinx.coroutines.CoroutineScope)) | A slider that shows playback progress and allows the user to seek. |

*This is not an exhaustive list. Refer to the library's API reference for all
available components.*

Two other prebuilt Composables you are likely to need are related to the surface
management and they live in the `media3-ui-compose` module because they don't
possess Material theming.

| Component | Description |
| --- | --- |
| [`ContentFrame`](/reference/kotlin/androidx/media3/ui/compose/ContentFrame.composable#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0)) | A surface for displaying media content that handles aspect ratio management, resizing, and a shutter |
| [`PlayerSurface`](/reference/kotlin/androidx/media3/ui/compose/PlayerSurface.composable#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) | Raw surface which wraps `SurfaceView` and `TextureView` in `AndroidView` |