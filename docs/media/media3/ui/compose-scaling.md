---
title: https://developer.android.com/media/media3/ui/compose-scaling
url: https://developer.android.com/media/media3/ui/compose-scaling
source: md.txt
---

> Documentation index: https://developer.android.com/media/media3/llms.txt

Android powers a diverse range of form factors beyond conventional portrait
smartphones, including foldables, tablets, desktop windowing environments, and
external displays. If you assume screen geometry is static, media content can
end up stretched, cropped, or unintentionally letterboxed. Your app must
dynamically adapt to varied source media aspect ratios (from classic 4:3 to
ultra-wide) across evolving display modes.

Most media layout failures in Jetpack Compose stem from three common
architectural pitfalls:

- Inconsistent window inset handling and edge-to-edge collisions.
- Inconsistent layout updates due to incorrect window size calculation.
- Misconfiguration of content scaling options.

This guide covers strategies and best practices for addressing each of these
areas using Media3 and Jetpack Compose.

## Handle window insets and edge-to-edge collisions

On devices running Android 15 (API level 35) and higher, apps that target API
level 35 or higher are [displayed edge-to-edge](https://developer.android.com/about/versions/15/behavior-changes-15.md.txt#edge-to-edge) by default. System bars
such as the status bar, navigation bar, and desktop caption bar draw over your
app's content, and display cutouts can obscure parts of it.

Without proper window inset management, two major layout conflicts occur:

- **System bar overlaps:** Video frames, subtitles, and playback controls are partially obscured by the status bar (clock, battery icons), the gesture or navigation bar, or display cutouts (camera notches). For general setup guidance, see [Set up edge-to-edge](https://developer.android.com/develop/ui/compose/system/setup-e2e.md.txt).
- **Desktop mode caption bar interference:** In desktop windowing mode, the system introduces a top caption bar for window management. Standard layouts that render custom headers or edge-to-edge media canvases without accounting for this caption bar end up with video frames and top playback controls obscured and unclickable. For more details on window states, see [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing.md.txt).

![System status bar overlapping the edge-to-edge media canvas and playback controls.](https://developer.android.com/static/media/media3/ui/images/scale_status_bar_overlap.png) ![Gesture navigation bar overlapping the edge-to-edge media canvas.](https://developer.android.com/static/media/media3/ui/images/scale_navigation_bar_overlap.png) ![Desktop caption bar overlapping the top video playback controls.](https://developer.android.com/static/media/media3/ui/images/scale_caption_bar_overlap.png) **Figure 1.** System status bar, gesture navigation bar, and desktop caption bar overlap the edge-to-edge media canvas and obscure video content and playback controls.

### Inset management strategies

Your app should dynamically adapt to system insets based on whether the player
is in a non-immersive or immersive mode.

#### Non-immersive configurations

In non-immersive playback, system bars remain visible to preserve device
context.

When the player extends to the window edges, apply
[`windowInsetsPadding`](https://developer.android.com/develop/ui/compose/system/insets-ui.md.txt) with
[`WindowInsets.safeDrawing`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/WindowInsets.Companion.md.txt#(androidx.compose.foundation.layout.WindowInsets.Companion).safeDrawing()) and [`only`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary.md.txt#(androidx.compose.foundation.layout.WindowInsets).only(androidx.compose.foundation.layout.WindowInsetsSides)) to each
[`PlayerDefaults`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/PlayerDefaults.md.txt) control bar on the edges where it meets the
system bars or display cutout (for example, `Top + Horizontal` on `TopControls`
and `Bottom + Horizontal` on `BottomControls`). This keeps the controls clear of
system bars while the video surface extends across the container.

> [!NOTE]
> **Note:** `windowInsetsPadding` applies the full inset unless an ancestor consumes it. If you embed an inline player inside a scrolling feed or below a top app bar, use [`Modifier.fitInside(WindowInsetsRulers.SafeDrawing.current)`](https://developer.android.com/develop/ui/compose/system/evaluate-rulers.md.txt) instead. `WindowInsetsRulers` positions controls against the actual on-screen inset bounds regardless of what ancestor layouts consume.


```kotlin
@Composable
fun NonImmersiveVideoPlayer(
  player: Player,
  showControls: Boolean,
  modifier: Modifier = Modifier,
) {
  Player(
    player = player,
    modifier = modifier,
    showControls = showControls,
    // Keep top controls clear of the status bar, caption bar, and display cutout
    topControls = {
      PlayerDefaults.TopControls(
        player = player,
        modifier =
          Modifier.fillMaxWidth()
            .windowInsetsPadding(
              WindowInsets.safeDrawing.only(WindowInsetsSides.Top + WindowInsetsSides.Horizontal)
            ),
      ) {
        MuteButton(player = player, modifier = Modifier.align(Alignment.TopEnd).padding(16.dp))
      }
    },
    // Keep bottom controls clear of the navigation bar and display cutout
    bottomControls = {
      PlayerDefaults.BottomControls(
        player = player,
        modifier =
          Modifier.fillMaxWidth()
            .windowInsetsPadding(
              WindowInsets.safeDrawing.only(
                WindowInsetsSides.Bottom + WindowInsetsSides.Horizontal
              )
            ),
      )
    },
  )
}
```

<br />

![In non-immersive mode, the app integrates window inset padding to dynamically shift content inward.](https://developer.android.com/static/media/media3/ui/images/scale_non_immersive_insets.png) **Figure 2.** In non-immersive mode, the app applies window inset padding to shift controls inward.

#### Immersive configurations (portrait and landscape)

In full-screen immersive mode, the goal is to maximize the canvas for a
cinematic experience while keeping playback controls accessible:

1. Apply [`windowInsetsPadding`](https://developer.android.com/develop/ui/compose/system/insets-ui.md.txt) to media control overlays (such as top and bottom controls) to prevent them from overlapping display cutouts or system gesture areas (for example, combining `WindowInsets.displayCutout` with `WindowInsets.systemGestures` on the bottom controls so the seek bar does not conflict with edge-swipe gestures).
2. Hide system bars using [`WindowInsetsControllerCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat.md.txt) inside a `DisposableEffect`, ensuring the system UI visibility is restored when leaving the composable.


```kotlin
@Composable
fun ImmersiveVideoPlayer(player: Player, showControls: Boolean, modifier: Modifier = Modifier) {
  val view = LocalView.current

  // Manages the system UI lifecycle to create an edge-to-edge cinematic experience
  DisposableEffect(view) {
    // Finds the hosting Activity, unwrapping any ContextWrapper around the view's context
    val activity =
      generateSequence(view.context) { (it as? ContextWrapper)?.baseContext }
        .filterIsInstance<Activity>()
        .firstOrNull()
    val window = activity?.window ?: return@DisposableEffect onDispose {}
    val controller = WindowCompat.getInsetsController(window, view)

    // Records the current system bar state so it can be restored on dispose
    val insets = ViewCompat.getRootWindowInsets(view)
    val wereSystemBarsVisible =
      insets == null ||
        insets.isVisible(WindowInsetsCompat.Type.statusBars()) ||
        insets.isVisible(WindowInsetsCompat.Type.navigationBars())
    val previousBehavior = controller.systemBarsBehavior

    // Hides status bars, navigation bars, and caption bars to maximize the video canvas
    controller.hide(WindowInsetsCompat.Type.systemBars())

    // Allows hidden system bars to temporarily reappear with a swipe gesture from the edge
    controller.systemBarsBehavior =
      WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE

    onDispose {
      // Restores the previous system bar state when leaving the composable
      controller.systemBarsBehavior = previousBehavior
      if (wereSystemBarsVisible) {
        controller.show(WindowInsetsCompat.Type.systemBars())
      }
    }
  }

  Player(
    player = player,
    modifier = modifier,
    showControls = showControls,
    // Keep top controls clear of the display cutout while the system bars are hidden
    topControls = {
      PlayerDefaults.TopControls(
        player = player,
        modifier =
          Modifier.fillMaxWidth()
            .windowInsetsPadding(
              WindowInsets.displayCutout.only(
                WindowInsetsSides.Top + WindowInsetsSides.Horizontal
              )
            ),
      ) {
        MuteButton(player = player, modifier = Modifier.align(Alignment.TopEnd).padding(16.dp))
      }
    },
    // Keep bottom controls clear of the display cutout and system gesture areas
    bottomControls = {
      PlayerDefaults.BottomControls(
        player = player,
        modifier =
          Modifier.fillMaxWidth()
            .windowInsetsPadding(
              WindowInsets.displayCutout
                .union(WindowInsets.systemGestures)
                .only(WindowInsetsSides.Bottom + WindowInsetsSides.Horizontal)
            ),
      )
    },
  )
}
```

<br />

![System bar automatically hides when the video player enters immersive mode, providing a full-screen cinematic experience.](https://developer.android.com/static/media/media3/ui/images/scale_immersive_insets.png) **Figure 3.** System bars hide when the video player enters immersive mode.

> [!NOTE]
> **Note:** The preceding code samples use the [`media3-ui-compose-material3`](https://developer.android.com/media/media3/ui/compose.md.txt#add-dependency) module. Because both the playback player instance and the Material 3 UI component share the name `Player`, ensure your file imports `androidx.media3.common.Player` for the player instance and `androidx.media3.ui.compose.material3.Player` for the UI composable.

## Calculate dynamic window sizing and layout updates

Calculating screen width or height only once at app startup causes layouts to
rely on stale values when the device configuration changes---such as when a
foldable device is unfolded, a multi-window session is resized, or the display
is rotated.

In these cases, even if a child component correctly uses
[`Modifier.fillMaxWidth()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier.md.txt#(androidx.compose.ui.Modifier).fillMaxWidth(kotlin.Float)), it will fail to adapt if its parent
container is constrained by stale dimensions, causing stretching, clipping, or
unresponsive layouts.

In the following example, the left frame illustrates correct rendering on a
standard viewport, while the right frame demonstrates the failure of stale
window dimensions to adapt when a device is unfolded, resulting in
non-responsive content layout.
![Correct rendering on standard viewport with dynamic aspect ratio adaptation.](https://developer.android.com/static/media/media3/ui/images/scale_window_size_dynamic.png) ![Failure of stale window dimensions to adapt when device is unfolded.](https://developer.android.com/static/media/media3/ui/images/scale_window_size_stale.png) **Figure 4.** Comparison of dynamic aspect ratio adaptation.

To avoid stale layout constraints, use the [Jetpack Media Query
API](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery). Because this API is experimental and disabled by default,
first [enable the `mediaQuery` function](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery.md.txt#enable-uimediaquery) by setting
`ComposeUiFlags.isMediaQueryIntegrationEnabled = true` (for example, before
calling `setContent`), and opt in with
`@OptIn(ExperimentalMediaQueryApi::class)`.

Use [`derivedMediaQuery`](https://developer.android.com/reference/kotlin/androidx/compose/ui/derivedMediaQuery.composable.md.txt#derivedMediaQuery(kotlin.Function1)) to evaluate conditions on the
current window size, such as `windowWidth`, so your layout updates when the
window changes without unnecessary recompositions. You can combine
`derivedMediaQuery` with [`WindowSizeClass`](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass.md.txt) breakpoints to
switch between single-pane and multi-pane player layouts as the window expands:


```kotlin
@OptIn(ExperimentalMediaQueryApi::class)
@Composable
fun AdaptiveVideoPlayerScreen(
  player: Player,
  modifier: Modifier = Modifier,
  relatedContent: @Composable () -> Unit,
) {
  val isWideWindow by derivedMediaQuery {
    windowWidth >= WindowSizeClass.WIDTH_DP_MEDIUM_LOWER_BOUND.dp
  }

  if (isWideWindow) {
    // Medium or expanded width: place the player alongside a details or playlist pane
    Row(modifier = modifier.fillMaxSize()) {
      Player(player = player, modifier = Modifier.weight(0.65f).fillMaxHeight())
      Box(modifier = Modifier.weight(0.35f).fillMaxHeight()) { relatedContent() }
    }
  } else {
    // Compact width: stack a 16:9 player above the details pane
    Column(modifier = modifier.fillMaxSize()) {
      Player(player = player, modifier = Modifier.fillMaxWidth().aspectRatio(16f / 9f))
      Box(modifier = Modifier.weight(1f).fillMaxWidth()) { relatedContent() }
    }
  }
}
```

<br />

## Configure content scaling and aspect ratios

Distinguish between managing the available container area and scaling the media
content itself. Use inset management, such as safe area padding, to set
container boundaries relative to system bars and display cutouts. Then apply
scaling strategies within those boundaries. For design guidance on structuring
containers and scaling visual content across aspect ratios, see
[Content composition and structure](https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure.md.txt#scaling).

In the following example, the left image shows how a cropping strategy can cut
off content when full visibility is required, while the right image shows how a
fitting strategy preserves the native aspect ratio for full-frame rendering.
![Cropping strategy causing significant content loss when full visibility is required.](https://developer.android.com/static/media/media3/ui/images/scale_cropping_strategy.png) ![Fitting strategy maintaining native aspect ratio for full-frame rendering.](https://developer.android.com/static/media/media3/ui/images/scale_fitting_strategy.png) **Figure 5.** Comparison of scaling behaviors.

Media3 components handle standard video aspect ratios automatically, but
explicit [`ContentScale`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt) configurations become critical when
working with custom Compose layouts or constrained containers (such as
scrollable social feeds). Selecting an improper content scale can lead to layout
issues---such as video distortion (stretching) or unintended letterboxing that
leaves empty space in the viewport. Managing video surfaces manually without
these options can also result in broken layouts during screen rotations or
[foldable](https://developer.android.com/develop/adaptive-apps/guides/foldables/learn-about-foldables.md.txt) device state changes.

Whether displaying a 16:9 video on a 4:3 screen or a 4:3 video on a 16:9
display, the [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/Player.composable.md.txt) composable defaults to
[`ContentScale.Fit`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt#Fit()). This keeps the full video visible
without clipping by applying letterboxing or pillarboxing.

Subsequent display mode changes (such as zooming or cropping) should be
user-driven. For example, switch to [`ContentScale.Crop`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt#Crop()) to
fill the container completely. An interactive scaling toggle balances layout
requirements with user choice.

### Sample implementations

You can enforce full frame visibility and handle aspect ratios using standard
Compose [`ContentScale`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt) properties.

#### Use the `Player` composable

The simplest and most direct approach is to use the [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/Player.composable.md.txt)
composable. Serving as a high-level wrapper that automatically handles scaling
boundaries, it pairs a [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/ContentFrame.composable.md.txt) for video rendering with
customizable control overlays (`topControls`, `centerControls`,
`bottomControls`) and a shutter layer:


```kotlin
@Composable
fun FitVideoPlayer(player: Player, modifier: Modifier = Modifier) {
  Player(
    player = player,
    modifier = modifier.fillMaxSize(), // Fill the available space
    contentScale = ContentScale.Fit, // Default; shown for clarity
  )
}
```

<br />

When building a custom video player layout or placing custom UI layers directly
over the video stream, you can use [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/ContentFrame.composable.md.txt) directly for
precise, lower-level layout control.

#### Dynamic user-controlled scaling toggle

To enhance the viewing experience of your app, you can add an optional toggle to
switch between different content scaling options. By detecting a double-tap
gesture, you can instantly toggle the player's state between `ContentScale.Fit`
and `ContentScale.Crop`. You can also extend this functionality to support
dynamic `ContentScale` adjustments using pinch-to-zoom or other multi-touch
gestures, similar to modern video streaming applications.
**Figure 6.** Switching between ContentScale.Fit and ContentScale.Crop.


```kotlin
@Composable
fun ZoomableVideoPlayer(player: Player, modifier: Modifier = Modifier) {
  var isCropped by rememberSaveable { mutableStateOf(false) }

  Player(
    player = player,
    modifier =
      modifier
        .fillMaxSize()
        // Handle double-tap to toggle between Fit and Crop scaling
        .pointerInput(Unit) { detectTapGestures(onDoubleTap = { isCropped = !isCropped }) },
    contentScale = if (isCropped) ContentScale.Crop else ContentScale.Fit,
  )
}
```

<br />

> [!IMPORTANT]
> **Key Point:** Avoid hand-written cropping or scaling math. Use [`ContentScale`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt) (through [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/Player.composable.md.txt) or [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/ContentFrame.composable.md.txt)), which keeps the video's aspect ratio accurate as the container size changes.

While there are several content scaling options, choose the scaling option based
on your use case: use [`ContentScale.Crop`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt#Crop()) for short-form
video or scrollable feeds where filling the screen is the primary goal, and
default to [`ContentScale.Fit`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/ContentScale.md.txt#Fit()) for media with vital margin
information, such as sports scores or subtitles, to safeguard essential visual
context.