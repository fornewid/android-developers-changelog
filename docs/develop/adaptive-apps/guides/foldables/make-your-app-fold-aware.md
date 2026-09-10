---
title: https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware
url: https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware
source: md.txt
---

Large unfolded displays and unique folded states enable new user experiences on
foldable devices. To make your app fold aware in Jetpack Compose, use the
[Compose Material 3 Adaptive library](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive), which provides APIs for foldable
device window features such as folds, hinges, and device postures. When your app
is fold aware, it can adapt its layout to avoid placing important content in the
area of folds or hinges and use folds and hinges as natural separators.

Understanding whether a device supports configurations such as tabletop or book
posture can guide decisions about supporting different layouts or providing
specific features.

## Window information

In Jetpack Compose, use the [`collectFoldingFeaturesAsState()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/collectFoldingFeaturesAsState.composable) composable
function to observe window folding information.
`collectFoldingFeaturesAsState()` collects the current window folding features
from [`WindowInfoTracker`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowInfoTracker) into a Compose [`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State) containing a list of
[`FoldingFeature`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature) objects.

Because `collectFoldingFeaturesAsState()` returns a Compose `State`, your
composables automatically recompose whenever the device fold state or posture
changes, without requiring manual lifecycle management or flow collection:

    @Composable
    fun FoldAwareScreen() {
        val foldingFeatures by collectFoldingFeaturesAsState()

        // Access folding features for the current window.
        val foldFeature = foldingFeatures.firstOrNull()
        if (foldFeature != null) {
            // Adapt layout based on the fold feature.
        }
    }

## Features of foldable displays

The list of [`FoldingFeature`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature) elements returned by
[`collectFoldingFeaturesAsState()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/collectFoldingFeaturesAsState.composable) (a subtype of [`DisplayFeature`](https://developer.android.com/reference/kotlin/androidx/window/layout/DisplayFeature))
provides information about foldable displays, including the following
properties:

- `state`: The folded state of the device, [`FLAT`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#FLAT()) or [`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED())

- `orientation`: The orientation of the fold or hinge, [`HORIZONTAL`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.Orientation#HORIZONTAL()) or
  [`VERTICAL`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.Orientation#VERTICAL())

- `occlusionType`: Whether the fold or hinge conceals part of the display,
  [`NONE`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.OcclusionType#NONE()) or [`FULL`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.OcclusionType#FULL())

- `isSeparating`: Whether the fold or hinge creates two logical display areas,
  true or false

> [!NOTE]
> **Note:** Although the hinge on foldable devices allows the device to fold to various angles, `FoldingFeature` does not expose the angle as part of the API. Different devices have different reporting ranges, and sensor accuracy can vary from device to device; so, animations or logic based on the precise hinge angle must be tuned to the device.

A foldable device that is `HALF_OPENED` always reports `isSeparating` as true
because the screen is separated into two display areas. Also, `isSeparating` is
always true on a dual‑screen device when the application spans both
screens.

The `FoldingFeature` [`bounds`](https://developer.android.com/reference/kotlin/androidx/window/layout/DisplayFeature#bounds()) property (inherited from `DisplayFeature`)
represents the bounding rectangle of a folding feature such as a fold or hinge.
The bounds can be used to position elements on screen relative to the feature:

    @Composable
    fun FoldFeatureDemo() {
        val foldingFeatures by collectFoldingFeaturesAsState()
        val foldFeature = foldingFeatures.firstOrNull()

        if (foldFeature != null) {
            val isSeparating = foldFeature.isSeparating
            val occlusionType = foldFeature.occlusionType
            val bounds = foldFeature.bounds
            // Use bounds and properties to position content.
        }
    }

### Tabletop posture

Using the information included in the `FoldingFeature` object, your app can
support postures like tabletop, where the phone sits on a surface, the hinge is
in a horizontal position, and the foldable screen is half opened.

Tabletop posture offers users the convenience of operating their phones without
holding the phone in their hands. Tabletop posture is great for watching media,
taking photos, and making video calls.
![A video player app in tabletop posture with video playback on the
upright vertical portion of the screen and playback controls on the
lower horizontal portion.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/foldables/tabletop.png) **Figure 1.** A video player app in tabletop posture---video on vertical portion of screen; playback controls on horizontal portion.

Use [`FoldingFeature.State`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State) and [`FoldingFeature.Orientation`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.Orientation) from
`collectFoldingFeaturesAsState()` to determine whether the device is in tabletop
posture:

    @Composable
    fun TabletopContent() {
        val foldingFeatures by collectFoldingFeaturesAsState()
        val foldFeature = foldingFeatures.firstOrNull()

        val isTableTopPosture = foldFeature != null &&
            foldFeature.state == FoldingFeature.State.HALF_OPENED &&
            foldFeature.orientation == FoldingFeature.Orientation.HORIZONTAL

        if (isTableTopPosture) {
            // Tabletop layout: separate content and controls across the fold.
        } else {
            // Standard layout.
        }
    }

Alternatively, you can determine whether the window is in tabletop posture by
checking the [`Posture`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/Posture) property returned by
[`currentWindowAdaptiveInfoV2()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/currentWindowAdaptiveInfoV2.composable):

    val adaptiveInfo = currentWindowAdaptiveInfoV2()
    val isTabletop = adaptiveInfo.windowPosture.isTabletop

Once you know the device is in tabletop posture, update your app layout
accordingly. For media apps, that typically means placing the playback above the
fold and positioning controls and supplementary content just following for a
hands‑free viewing or listening experience.

#### Examples

- [`MediaPlayerActivity`](https://github.com/android/platform-samples/blob/main/samples/user-interface/windowmanager/src/main/java/com/example/platform/ui/windowmanager/MediaPlayerActivity.kt) app: See how to use [Media3
  Exoplayer](https://developer.android.com/guide/topics/media/exoplayer) and [WindowManager](https://developer.android.com/jetpack/androidx/releases/window) to create a fold‑aware video
  player.

- [Optimize your camera app on foldable devices with Jetpack WindowManager](https://developer.android.com/codelabs/android-camera-foldables#5)
  codelab: Learn how to implement tabletop posture for photography apps. Show
  the viewfinder on the top half of the screen (above the fold) and the
  controls on the bottom half.

### Book posture

Another unique foldable feature is book posture, where the device is half opened
and the hinge is vertical. Book posture is great for reading e‑books. With
a two‑page layout on a large screen foldable open like a bound book, book
posture captures the experience of reading a real book.

It can also be used for photography if you want to capture a different aspect
ratio while taking pictures hands‑free.

Implement book posture with the same techniques used for tabletop posture. Check
that the folding feature orientation is vertical instead of horizontal:

    @Composable
    fun BookContent() {
        val foldingFeatures by collectFoldingFeaturesAsState()
        val foldFeature = foldingFeatures.firstOrNull()

        val isBookPosture = foldFeature != null &&
            foldFeature.state == FoldingFeature.State.HALF_OPENED &&
            foldFeature.orientation == FoldingFeature.Orientation.VERTICAL

        if (isBookPosture) {
            // Book posture layout: two-page layout across the vertical fold.
        } else {
            // Standard single-page layout.
        }
    }

> [!NOTE]
> **Note:** On foldable devices that have two screens separated by a hinge, use layouts designed for tabletop and book postures even if the `FoldingFeature.State` is `FLAT`. Don't place UI controls too close to a fold or hinge when `isSeparating` is true because the controls can be difficult to reach. Use `occlusionType` to decide whether to place content within the folding feature `bounds`.

## Window size changes

An app's display area can change as a result of a device configuration change,
for example, when the device is folded or unfolded, rotated, or resized in
multi‑window mode.

To retrieve the current window size class and adapt to size changes in Jetpack
Compose, use the [`currentWindowAdaptiveInfoV2()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/currentWindowAdaptiveInfoV2.composable) composable function from
the [Compose Material 3 Adaptive library](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive). `currentWindowAdaptiveInfoV2()`
returns a [`WindowAdaptiveInfo`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/WindowAdaptiveInfo) instance that provides the
[`WindowSizeClass`](https://developer.android.com/reference/kotlin/androidx/window/core/layout/WindowSizeClass) of the current window (with support for large and
extra-large breakpoints by default), as well as the device's
[`windowPosture`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/WindowAdaptiveInfo#windowPosture()):

    @Composable
    fun AdaptiveApp() {
        val adaptiveInfo = currentWindowAdaptiveInfoV2()
        val windowSizeClass = adaptiveInfo.windowSizeClass

        when {
            windowSizeClass.isWidthAtLeastBreakpoint(
                WIDTH_DP_EXPANDED_LOWER_BOUND
            ) -> {
                // Expanded layout
            }
            windowSizeClass.isWidthAtLeastBreakpoint(
                WIDTH_DP_MEDIUM_LOWER_BOUND
            ) -> {
                // Medium layout
            }
            else -> {
                // Compact layout
            }
        }
    }

See [Use window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes).

## Additional resources

To explore more about fold-aware layouts and foldable devices, see the following
resources:

### Samples

- Jetpack [WindowManager sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/windowmanager): Example of how to use the Jetpack WindowManager library
- [Jetcaster](https://github.com/android/compose-samples/tree/main/Jetcaster) : Tabletop posture implementation with Compose

### Codelabs

- [Support foldable and dual-screen devices with Jetpack WindowManager](https://developer.android.com/codelabs/android-window-manager-dual-screen-foldables#0)
- [Optimize your camera app on foldable devices with Jetpack WindowManager](https://developer.android.com/codelabs/android-camera-foldables#0)