---
title: https://developer.android.com/develop/ui/compose/system/insets
url: https://developer.android.com/develop/ui/compose/system/insets
source: md.txt
---

[Video](https://www.youtube.com/watch?v=mlL6H-s0nF0)

The Android platform is responsible for drawing the system UI, such as the
status bar and navigation bar. This system UI is displayed regardless of which
app the user is using.

[`WindowInsets`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/WindowInsets) provides information about the system
UI to ensure that your app draws in the correct area and your UI isn't obscured
by the system UI.
![Going edge-to-edge to draw behind the system bars](https://developer.android.com/static/develop/ui/compose/images/layouts/insets/e2e-intro.gif) **Figure 1.** Going edge-to-edge to draw behind the system bars.

On Android 14 (API level 34) and lower, your app's UI does not draw underneath
the system bars and display cutouts by default.

On Android 15 (API level 35) and higher, your app draws underneath the system
bars and display cutouts once your app targets SDK 35. This results in a more
seamless user experience and allows your app to take full advantage of the
window space available to it.

Displaying content behind the system UI is called *going edge-to-edge*. On this
page, you learn about the different types of insets, how to go edge-to-edge,
and how to use the inset APIs to animate your UI and ensure your app's content
isn't obscured by system UI elements.

> [!IMPORTANT]
> **Important:** [Edge-to-edge is enforced](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge) on Android 15 and higher once your app targets SDK 35. If your app is not already edge-to-edge, portions of your app may be hidden and you must handle insets. Depending on the app, this work may or may not be significant. The Material 3 [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) component can reduce the work required to be compatible with the Android 15 edge-to-edge enforcement. See [Create a scaffold component to hold the UI together](https://developer.android.com/quick-guides/content/create-scaffold).

## Inset fundamentals

[Video](https://www.youtube.com/watch?v=QRzepC9gHj4)

When an app goes edge-to-edge, you need to ensure that important content and
interactions are not obscured by the system UI. For example, if a button is
placed behind the navigation bar, the user may not be able to click it.

The size of the system UI and information about where it is placed is specified
via *insets*.

Each portion of the system UI has a corresponding type of inset that describes
its size and where it is placed. For example, status bar insets provide the size
and position of the status bar, whereas the navigation bar insets provide the
size and position of the navigation bar. Each type of inset consists of four
pixel dimensions: top, left, right, and bottom. These dimensions specify how far
the system UI extends from the corresponding sides of the app's window. To avoid
overlapping with that type of system UI, therefore, app UI must be inset by that
amount.

These built-in Android inset types are available through [`WindowInsets`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/WindowInsets):

|---|---|
| [`WindowInsets.statusBars`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).statusBars()) | The insets describing the status bars. These are the top system UI bars containing notification icons and other indicators. |
| [`WindowInsets.statusBarsIgnoringVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).statusBarsIgnoringVisibility()) | The status bar insets for when they are visible. If the status bars are currently hidden (due to entering immersive full screen mode), then the main status bar insets will be empty, but these insets will be non-empty. |
| [`WindowInsets.navigationBars`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).navigationBars()) | The insets describing the navigation bars. These are the system UI bars on the left, right, or bottom side of the device, describing the taskbar or navigation icons. These can change at runtime based on the user's preferred navigation method and interacting with the taskbar. |
| [`WindowInsets.navigationBarsIgnoringVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).navigationBarsIgnoringVisibility()) | The navigation bar insets for when they are visible. If the navigation bars are currently hidden (due to entering immersive full screen mode), then the main navigation bar insets will be empty, but these insets will be non-empty. |
| [`WindowInsets.captionBar`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).captionBar()) | The inset describing the system UI window decoration if in a freeform window, like top title bar. |
| [`WindowInsets.captionBarIgnoringVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).captionBarIgnoringVisibility()) | The caption bar insets for when they are visible. If the caption bars are currently hidden, then the main caption bar insets will be empty, but these insets will be non-empty. |
| [`WindowInsets.systemBars`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).systemBars()) | The union of the system bar insets, which include the status bars, navigation bars, and caption bar. |
| [`WindowInsets.systemBarsIgnoringVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).systemBarsIgnoringVisibility()) | The system bar insets for when they are visible. If the system bars are currently hidden (due to entering immersive full screen mode), then the main system bar insets will be empty, but these insets will be non-empty. |
| [`WindowInsets.ime`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).ime()) | The insets describing the amount of space on the bottom that the software keyboard occupies. |
| [`WindowInsets.imeAnimationSource`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).imeAnimationSource()) | The insets describing the amount of space that the software keyboard occupied *before* the current keyboard animation. |
| [`WindowInsets.imeAnimationTarget`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).imeAnimationTarget()) | The insets describing the amount of space that the software keyboard will occupy *after* the current keyboard animation. |
| [`WindowInsets.tappableElement`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).tappableElement()) | A type of insets describing more detailed information about the navigation UI, giving the amount of space where "taps" will be handled by the system, and not the app. For transparent navigation bars with gesture navigation, some app elements can be tappable through the system navigation UI. |
| [`WindowInsets.tappableElementIgnoringVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).tappableElementIgnoringVisibility()) | The tappable element insets for when they are visible. If the tappable elements are currently hidden (due to entering immersive full screen mode), then the main tappable element insets will be empty, but these insets will be non-empty. |
| [`WindowInsets.systemGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).systemGestures()) | The insets representing the amount of insets where the system will intercept gestures for navigation. Apps can manually specify handling a limited amount of these gestures via [`Modifier.systemGestureExclusion`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).systemGestureExclusion()). |
| [`WindowInsets.mandatorySystemGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).mandatorySystemGestures()) | A subset of the system gestures that will always be handled by the system, and which can't be opted out via [`Modifier.systemGestureExclusion`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).systemGestureExclusion()). |
| [`WindowInsets.displayCutout`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).displayCutout()) | The insets representing the amount of spacing needed to avoid overlapping with a display cutout (notch or pinhole). |
| [`WindowInsets.waterfall`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).waterfall()) | The insets representing the curved areas of a waterfall display. A waterfall display has curved areas along the edges of the screen where the screen begins to wrap along the sides of the device. |

These types are summarized by three "safe" inset types that ensure content isn't
obscured:

- [`WindowInsets.safeDrawing`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeDrawing())
- [`WindowInsets.safeGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeGestures())
- [`WindowInsets.safeContent`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeContent())

These "safe" inset types protect content in different ways, based on the
underlying platform insets:

- Use [`WindowInsets.safeDrawing`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeDrawing()) to protect content that shouldn't be drawn underneath any system UI. This is the most common usage of insets: to prevent drawing content that is obscured by the system UI (either partially or completely).
- Use [`WindowInsets.safeGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeGestures()) to protect content with gestures. This avoids system gestures clashing with app gestures (such as those for bottom sheets, carousels, or in games).
- Use [`WindowInsets.safeContent`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeContent()) as a combination of [`WindowInsets.safeDrawing`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeDrawing()) and [`WindowInsets.safeGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).safeGestures()) to ensure content has no visual overlap and no gesture overlap.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Material Components and layouts](https://developer.android.com/develop/ui/compose/layouts/material)
- [Migrate `CoordinatorLayout` to Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/coordinator-layout)
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)