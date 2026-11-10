---
title: https://developer.android.com/media/media3/exoplayer/scrubbing
url: https://developer.android.com/media/media3/exoplayer/scrubbing
source: md.txt
---

When a user drags a seek bar thumb across a timeline to preview frames and find
a playback position, the UI dispatches frequent `Player.seekTo` calls in short
succession. Standard seeking with `Player.seekTo` and
[`ExoPlayer.setSeekParameters`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.md.txt#setSeekParameters(androidx.media3.exoplayer.SeekParameters)) is designed for isolated
jumps, where each new seek aborts any in-flight seek and resets the decoder.
During a continuous drag gesture, that behavior can prevent preview frames from
rendering until the user stops moving.

[`ExoPlayer.setScrubbingModeEnabled`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.md.txt#setScrubbingModeEnabled(boolean)) configures the
player for interactive scrubbing so video preview frames render responsively as
the user drags.

> [!NOTE]
> **Note:** Scrubbing mode APIs are annotated with [`@UnstableApi`](https://developer.android.com/reference/androidx/media3/common/util/UnstableApi.md.txt) and require [opting in to unstable APIs](https://developer.android.com/media/media3/exoplayer/troubleshooting.md.txt#unstable-api-lint-errors).

## Use prebuilt UI components

Media3's prebuilt UI modules include built-in scrubbing mode support when
connected directly to an `ExoPlayer` instance (not wrapped in a
[`ForwardingPlayer`](https://developer.android.com/reference/androidx/media3/common/ForwardingPlayer.md.txt) or accessed through a
[`MediaController`](https://developer.android.com/reference/androidx/media3/session/MediaController.md.txt)):

- **Jetpack Compose (`media3-ui-compose-material3`)** : Both the [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/Player.composable.md.txt) composable and standalone [`ProgressSlider`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/indicator/ProgressSlider.composable.md.txt) use scrubbing mode **by default** . When a user drags the slider thumb, `ProgressSlider` calls `setScrubbingModeEnabled(true)` at the start of the drag, dispatches `seekTo` updates during the drag, and calls `setScrubbingModeEnabled(false)` when the drag ends or the composable leaves composition. For more information, see [Material3 Compose](https://developer.android.com/media/media3/ui/compose-material3.md.txt).
- **Views (`media3-ui`)** : [`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView.md.txt) and [`PlayerControlView`](https://developer.android.com/reference/androidx/media3/ui/PlayerControlView.md.txt) include scrubbing mode integration that is **disabled by default** , seeking only once when the user releases the time bar. Enable continuous scrubbing in XML by setting `app:time_bar_scrubbing_enabled="true"` on `PlayerView`, or in code by calling [`setTimeBarScrubbingEnabled(true)`](https://developer.android.com/reference/androidx/media3/ui/PlayerView.md.txt#setTimeBarScrubbingEnabled(boolean)).

Even when you use `ProgressSlider` or `PlayerView`, you can customize
[`ScrubbingModeParameters`](https://developer.android.com/reference/androidx/media3/exoplayer/ScrubbingModeParameters.md.txt) on the `ExoPlayer`
instance, such as [setting a fractional seek tolerance from the scrubber
width](https://developer.android.com/media/media3/exoplayer/scrubbing#fractional-seek-tolerance).

## When to turn scrubbing mode on and off

If you implement a custom seek bar or scrubber control, turn scrubbing mode on
only for the duration of an interactive user scrubbing gesture:

- **Turn scrubbing mode on (`setScrubbingModeEnabled(true)`)** when the user starts dragging the scrubber thumb, and call `seekTo` as the drag position changes.
- **Turn scrubbing mode off (`setScrubbingModeEnabled(false)`)** as soon as the user finishes or cancels the gesture. For example, turn it off on pointer release, on gesture cancellation, or if your UI component is detached or disposed mid-drag.
- **Keep scrubbing mode off during normal playback and single seeks**, such as pressing fast-forward or rewind buttons, tapping a seek bar without dragging, or seeking programmatically.

Leaving scrubbing mode active outside a drag gesture has unintended side
effects:

- **Playback is suppressed** : While scrubbing mode is enabled, ExoPlayer sets the playback suppression reason to [`Player.PLAYBACK_SUPPRESSION_REASON_SCRUBBING`](https://developer.android.com/reference/androidx/media3/common/Player.md.txt#PLAYBACK_SUPPRESSION_REASON_SCRUBBING()), so `Player.isPlaying` returns `false`. When you call `setScrubbingModeEnabled(false)`, normal playback resumes automatically if `playWhenReady` is `true`.
- **Non-visual tracks are disabled**: Audio and metadata tracks are disabled by default while scrubbing.
- **Power and decoder usage increase**: Scrubbing mode boosts video codec operating rates, which consumes additional hardware and battery resources if left enabled.

The following example connects custom scrubber gesture callbacks to `ExoPlayer`:


### Kotlin

```kotlin
fun onScrubStart(exoPlayer: ExoPlayer, positionMs: Long) {
  exoPlayer.setScrubbingModeEnabled(true)
  exoPlayer.seekTo(positionMs)
}

fun onScrubMove(exoPlayer: ExoPlayer, positionMs: Long) {
  exoPlayer.seekTo(positionMs)
}

fun onScrubStop(exoPlayer: ExoPlayer, positionMs: Long, canceled: Boolean) {
  if (!canceled) {
    exoPlayer.seekTo(positionMs)
  }
  exoPlayer.setScrubbingModeEnabled(false)
}
```

### Java

```java
public static void onScrubStart(ExoPlayer exoPlayer, long positionMs) {
  exoPlayer.setScrubbingModeEnabled(true);
  exoPlayer.seekTo(positionMs);
}

public static void onScrubMove(ExoPlayer exoPlayer, long positionMs) {
  exoPlayer.seekTo(positionMs);
}

public static void onScrubStop(ExoPlayer exoPlayer, long positionMs, boolean canceled) {
  if (!canceled) {
    exoPlayer.seekTo(positionMs);
  }
  exoPlayer.setScrubbingModeEnabled(false);
}
```

<br />

## How scrubbing mode optimizes seeking

With [`ScrubbingModeParameters.DEFAULT`](https://developer.android.com/reference/androidx/media3/exoplayer/ScrubbingModeParameters.md.txt#DEFAULT()), ExoPlayer applies
several optimizations while scrubbing mode is active:

- **Coalesces rapid seeks** : Rather than preempting an active seek on every pointer move, ExoPlayer finishes decoding and rendering the current target frame while holding only the most recent seek position queued. Superseded intermediate seeks are dropped and reported to [`AnalyticsListener.onDroppedSeeksWhileScrubbing`](https://developer.android.com/reference/androidx/media3/exoplayer/analytics/AnalyticsListener.md.txt#onDroppedSeeksWhileScrubbing(androidx.media3.exoplayer.analytics.AnalyticsListener.EventTime,int)).
- **Disables audio and metadata tracks** : Temporarily disables `C.TRACK_TYPE_AUDIO` and `C.TRACK_TYPE_METADATA` tracks to avoid audio pops and unnecessary renderer resets.
- **Increases codec throughput** : Increases the video `MediaCodec` operating rate and ensures dynamic scheduling is enabled so decoded output buffers are processed faster.
- **Reduces decoder resets** : Avoids unnecessary `MediaCodec` flushes when seeking to a keyframe in compatible streams, skips resetting back to the keyframe when seeking forward within the same group of pictures (GOP), and uses `MediaCodec.BUFFER_FLAG_DECODE_ONLY` on Android 14 (API level 34) and higher so the decoder skips producing output buffers for intermediate frames between a keyframe and the target frame.

## Customize scrubbing parameters

Use [`ScrubbingModeParameters.Builder`](https://developer.android.com/reference/androidx/media3/exoplayer/ScrubbingModeParameters.Builder.md.txt) to adjust scrubbing
behavior, such as which track types are disabled or whether codec operating
rates are boosted. Apply the configuration with
`ExoPlayer.setScrubbingModeParameters` or
`ExoPlayer.Builder.setScrubbingModeParameters`. Build from
`exoPlayer.scrubbingModeParameters.buildUpon()` (or
`ScrubbingModeParameters.DEFAULT.buildUpon()`) so default optimizations remain
enabled.

### Set a fractional seek tolerance from the scrubber width

By default, `ScrubbingModeParameters` leaves fractional seek tolerances unset
(`null`), so seeks during scrubbing use the player's
[`SeekParameters`](https://developer.android.com/reference/androidx/media3/exoplayer/SeekParameters.md.txt) (`SeekParameters.EXACT` by default). An
exact seek must decode every frame from the preceding keyframe up to the target
timestamp. When there are many frames since the previous keyframe, such as in
streams with wide keyframe intervals or high frame rates, this decoding work
can add noticeable latency while dragging.

On touch screens, a user's finger can't reliably distinguish `1dp` or `2dp` of
movement along a scrubber bar. For a scrubber of width `widthDp`, a small touch
tolerance such as `2dp` in either direction (`4dp` total) corresponds to a
fraction of `2.0 / widthDp` of the media duration. How much media time that
fraction spans depends on the length of the video. We recommend passing a
`dp`-based tolerance divided by your UI scrubber's width to
[`setFractionalSeekTolerance`](https://developer.android.com/reference/androidx/media3/exoplayer/ScrubbingModeParameters.Builder.md.txt#setFractionalSeekTolerance(java.lang.Double,java.lang.Double)) (for example, `2dp`,
or tuned between `1dp` and `4dp` to balance speed and precision):

- On **long content** (for example, a 1-hour video on a `400dp` scrubber, where `2dp` spans 18 seconds), ExoPlayer can snap directly to a nearby keyframe within that touch tolerance instead of decoding intermediate frames.
- On **short clips** (for example, a 10-second clip on the same `400dp` scrubber, where `2dp` spans 50 milliseconds), the same fraction automatically keeps seeks close to the target frame.

Convert your target `dp` tolerance to pixels using the display density so it
matches the scrubber's measured pixel width, and update the tolerance whenever
the scrubber's width or display density changes, such as on initial layout or
screen rotation.

In Jetpack Compose, convert the `dp` tolerance to pixels with `LocalDensity`,
measure your custom slider with `Modifier.onSizeChanged`, and update
`scrubbingModeParameters` when the player, width, or density changes. If the
`ExoPlayer` instance outlives the composable, clear the tolerance on disposal:


```kotlin
private val SCRUBBING_TOLERANCE = 2.dp

@Composable
fun CustomScrubbingSlider(exoPlayer: ExoPlayer?, modifier: Modifier = Modifier) {
  var sliderWidthPx by remember { mutableIntStateOf(0) }
  val tolerancePx = with(LocalDensity.current) { SCRUBBING_TOLERANCE.toPx() }
  LaunchedEffect(exoPlayer, sliderWidthPx, tolerancePx) {
    if (exoPlayer != null && sliderWidthPx > 0) {
      val tolerance = (tolerancePx.toDouble() / sliderWidthPx).coerceIn(0.0, 1.0)
      exoPlayer.setFractionalSeekTolerance(tolerance)
    }
  }
  DisposableEffect(exoPlayer) { onDispose { exoPlayer?.setFractionalSeekTolerance(null) } }
  CustomSlider(
    player = exoPlayer,
    modifier = modifier.onSizeChanged { size -> sliderWidthPx = size.width },
  )
}

private fun ExoPlayer.setFractionalSeekTolerance(tolerance: Double?) {
  scrubbingModeParameters =
    scrubbingModeParameters
      .buildUpon()
      .setFractionalSeekTolerance(
        /* toleranceBefore= */ tolerance,
        /* toleranceAfter= */ tolerance,
      )
      .build()
}
```

<br />

In a View-based UI, convert the `dp` tolerance to pixels using
`DisplayMetrics.density`, apply the current width if your scrubber view or
`PlayerView` is already laid out, and use `View.addOnLayoutChangeListener` to
update `scrubbingModeParameters` when its width changes. Remove the listener
when detaching the UI, and clear the tolerance if the `ExoPlayer` instance
outlives the view:


### Kotlin

```kotlin
private const val SCRUBBING_TOLERANCE_DP = 2.0

fun configureViewFractionalSeekTolerance(
  exoPlayer: ExoPlayer,
  scrubberView: View,
): View.OnLayoutChangeListener {
  updateFractionalSeekTolerance(exoPlayer, scrubberView, scrubberView.width)
  val listener = View.OnLayoutChangeListener { v, left, _, right, _, oldLeft, _, oldRight, _ ->
    val widthPx = right - left
    if (widthPx != oldRight - oldLeft) {
      updateFractionalSeekTolerance(exoPlayer, v, widthPx)
    }
  }
  scrubberView.addOnLayoutChangeListener(listener)
  return listener
}

fun clearViewFractionalSeekTolerance(
  exoPlayer: ExoPlayer,
  scrubberView: View,
  listener: View.OnLayoutChangeListener,
) {
  scrubberView.removeOnLayoutChangeListener(listener)
  setFractionalSeekTolerance(exoPlayer, tolerance = null)
}

private fun updateFractionalSeekTolerance(
  exoPlayer: ExoPlayer,
  scrubberView: View,
  widthPx: Int,
) {
  val density = scrubberView.resources.displayMetrics.density
  if (widthPx > 0 && density > 0f) {
    val tolerancePx = SCRUBBING_TOLERANCE_DP * density
    setFractionalSeekTolerance(exoPlayer, (tolerancePx / widthPx).coerceIn(0.0, 1.0))
  }
}

private fun setFractionalSeekTolerance(exoPlayer: ExoPlayer, tolerance: Double?) {
  exoPlayer.scrubbingModeParameters =
    exoPlayer.scrubbingModeParameters
      .buildUpon()
      .setFractionalSeekTolerance(
        /* toleranceBefore= */ tolerance,
        /* toleranceAfter= */ tolerance,
      )
      .build()
}
```

### Java

```java
private static final double SCRUBBING_TOLERANCE_DP = 2.0;

public static View.OnLayoutChangeListener configureViewFractionalSeekTolerance(
    ExoPlayer exoPlayer, View scrubberView) {
  updateFractionalSeekTolerance(exoPlayer, scrubberView, scrubberView.getWidth());
  View.OnLayoutChangeListener listener =
      (v, left, top, right, bottom, oldLeft, oldTop, oldRight, oldBottom) -> {
        int widthPx = right - left;
        if (widthPx != oldRight - oldLeft) {
          updateFractionalSeekTolerance(exoPlayer, v, widthPx);
        }
      };
  scrubberView.addOnLayoutChangeListener(listener);
  return listener;
}

public static void clearViewFractionalSeekTolerance(
    ExoPlayer exoPlayer, View scrubberView, View.OnLayoutChangeListener listener) {
  scrubberView.removeOnLayoutChangeListener(listener);
  setFractionalSeekTolerance(exoPlayer, /* tolerance= */ null);
}

private static void updateFractionalSeekTolerance(
    ExoPlayer exoPlayer, View scrubberView, int widthPx) {
  float density = scrubberView.getResources().getDisplayMetrics().density;
  if (widthPx > 0 && density > 0f) {
    double tolerancePx = SCRUBBING_TOLERANCE_DP * density;
    setFractionalSeekTolerance(exoPlayer, Math.min(1.0, tolerancePx / widthPx));
  }
}

private static void setFractionalSeekTolerance(ExoPlayer exoPlayer, @Nullable Double tolerance) {
  exoPlayer.setScrubbingModeParameters(
      exoPlayer
          .getScrubbingModeParameters()
          .buildUpon()
          .setFractionalSeekTolerance(
              /* toleranceBefore= */ tolerance, /* toleranceAfter= */ tolerance)
          .build());
}
```

<br />

When you use a `dp`-based tolerance, keeping scrubbing mode enabled through the
final `seekTo` call in `onScrubStop` avoids a visual frame jump when the user
lifts their finger. If your app instead requires the final release position to
land on an exact timestamp, call `setScrubbingModeEnabled(false)` *before* your
final `seekTo` call so the final seek uses the player's standard
`SeekParameters`.

## Media and network considerations

Scrubbing mode optimizes local seek scheduling and hardware decoding, so it is
most effective with local files, [downloaded media](https://developer.android.com/media/media3/exoplayer/downloading-media.md.txt),
[cached streams](https://developer.android.com/media/media3/exoplayer/network-stacks.md.txt#caching), or buffered adaptive streams encoded with frequent
keyframes (short GOPs). Over uncached, high-latency network connections,
frequent seeks to unbuffered positions remain bound by network round-trip times.