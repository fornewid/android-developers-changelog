---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/adaptive-dos-and-donts
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/adaptive-dos-and-donts
source: md.txt
---

| **Note:** For apps that target Android 16 (API level 36), the system ignores screen orientation, aspect ratio, and app resizablility restrictions to improve the layout of apps on form factors with smallest width \>= 600dp. See [App
| orientation, aspect ratio, and
| resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).

Adaptive apps support displays of all sizes: the entire device screen, resizable
windows in multi‑window mode, portrait and landscape orientations, folded
and unfolded displays of foldable devices.

A short list of configuration settings and APIs enable you to build adaptive
apps. But some outdated settings and APIs are incompatible with adaptive apps
and must be avoided.

## Resizability

Adaptive apps support app resizability and multi‑window mode.

The [`resizeableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity) attribute of the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) and
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) manifest elements enables or disables multi‑window
mode on Android 11 (API level 30) and lower. On Android 12 (API level 31) and
higher, large screens support multi‑window mode regardless of the
attribute. For more information, see [Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode).
✓ Do

Enable your app to participant in multi‑window, multitasking scenarios for
increased user productivity and satisfaction.

Set `resizeableActivity="true"` if your app targets API levels lower than 24;
otherwise, forget about it---it's `true` by default on Android 7.0 (API
level 24) and higher.
✗ Don't

Don't set `resizeableActivity="false"` for any API level. Don't exclude your app
from use cases that involve multi‑window mode.

## Orientation

Adaptive apps support portrait and landscape orientation regardless of display
size or windowing mode.

The [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen) manifest setting restricts activity orientation.
✓ Do

Eliminate the `screenOrientation` setting from your app manifest.

Locking the orientation of apps doesn't prevent window size changes. Apps are
resized when they enter multi-window mode, when a device is folded or unfolded,
or when a desktop‑type window is resized. Your app has to support changes
in window size regardless of the `screenOrientation` attribute setting.
✗ Don't

Don't restrict activity orientation. Apps that lock orientation are letterboxed
on large screen devices and incompatible window sizes.

Letterboxed apps are subject to decreased discoverability on Google Play for
tablets, foldables, and ChromeOS devices.

## Aspect ratio

As screen and window sizes vary, so do their aspect ratios---from tall and
narrow, to square, to short and wide.

The [`minAspectRatio`](https://developer.android.com/reference/android/R.attr#minAspectRatio) and [`maxAspectRatio`](https://developer.android.com/reference/android/R.attr#maxAspectRatio) manifest settings restrict
your app's aspect ratio to hard‑coded values.
| **Note:** Only apps with `resizeableActivity="false"` can set `minAspectRatio` and `maxAspectRatio`.
✓ Do

Adapt your app to fit the display regardless of relative dimensions.

Eliminate the `minAspectRatio` and `maxAspectRatio` settings from your app
manifest. Or ensure your app is resizable, and aspect ratio takes care of itself
(see the [Resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/adaptive-dos-and-donts#resizability) section).
✗ Don't

Don't try to control the relative dimensions of your app. If your app runs on a
screen or in a window that has an aspect ratio that's incompatible with the
aspect ratio of the app, your app is letterboxed.

On Android 14 (API level 34) and higher, users can override the app aspect ratio
to expand letterboxed apps to fill the available display area. See [Device
compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode#user_per-app_overrides).

## Window size

Optimizing layouts for different display sizes is the central premise of
adaptive design. Adaptive apps focus on app window size rather than device
screen size. When the app is full screen, the app window is the device screen.

[Window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes) provide a systematic way of determining and categorizing
the size of the app window. Adapt your app by changing layouts as the window
size class of your app changes.
✓ Do

Evaluate your app window size based on window size classes.

To determine the window size class, use the [`currentWindowAdaptiveInfo()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowAdaptiveInfo())
top‑level function of the Compose Material 3 Adaptive library. For more
information, see [Build adaptive apps](https://developer.android.com/develop/ui/compose/build-adaptive-apps).
✗ Don't

Don't disregard the utility of the window size class definitions and the
built‑in APIs. Don't use deprecated APIs to calculate window size.

## Deprecated APIs

Older platform APIs don't correctly measure the app window; some measure the
device screen, some exclude system decor.
✓ Do

Use [`WindowManager#getCurrentWindowMetrics()`](https://developer.android.com/reference/kotlin/android/view/WindowManager#getcurrentwindowmetrics) and
[`WindowMetrics#getBounds()`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics#getbounds) to get the size of the app window. Use
[`WindowMetrics#getDensity()`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics#getdensity) to get the display density.
✗ Don't

Don't use the following deprecated [`Display`](https://developer.android.com/reference/kotlin/android/view/Display) APIs to determine window size:

- [`getSize()`](https://developer.android.com/reference/kotlin/android/view/Display#getsize): Deprecated in Android 11 (API level 30)
- [`getMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getmetrics): Deprecated in Android 11 (API level 30)
- [`getRealSize()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealsize): Deprecated in Android 12 (API level 31)
- [`getRealMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealmetrics): Deprecated in Android 12 (API level 31)

## Compose

Jetpack Compose is designed for adaptive UI development. No XML, no layout
files, no resource qualifiers. Just Kotlin‑based, stateless composables
like [`Column`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)), [`Row`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)), and [`Box`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Box(androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)) that describe your UI, and modifiers
like [`offset`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).offset(kotlin.Function1)), [`padding`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).padding(androidx.compose.ui.unit.Dp)), and [`size`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).size(androidx.compose.ui.unit.Dp)) that add behavior to UI
elements.
✓ Do

Build with Compose. Stay up to date with the latest features and releases.
✗ Don't

Don't rely on outdated technology. Don't let your app become obsolete.

## Compose Material 3 Adaptive library

The [Compose Material 3 Adaptive library](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary) provides components and APIs that
facilitate the development of adaptive apps.
✓ Do

Use the following APIs to make your app adaptive:

- [`NavigationSuiteScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)): Switches between navigation bar and navigation rail depending on app window size class.
- [`ListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)): Implements the list-detail canonical layout. Adapts the layout to the app window size.
- [`SupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#SupportingPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)): Implements the supporting pane canonical layout.

✗ Don't

Don't reinvent the wheel. Don't miss out on the developer productivity gains
provided by all the Jetpack Compose libraries.

## Layouts

Users expect apps to make the most of available display space with supplemental
content or enhanced controls.

Adaptive apps optimize layouts based on changes in the display, in particular,
changes in the size of the app window or changes in device posture.
✓ Do

Change UI components as the window size changes to take advantage of available
display space. For example, swap the bottom navigation bar used on compact
window sizes for a vertical navigation rail on medium and expanded windows.
Reposition dialogs to be reachable on all displays.

Organize content into panes to enable multi‑pane layouts like
list‑detail and supporting pane for dynamic content displays.
Your browser doesn't support the video tag. ✓ Do: List and detail activities organized in a dual-pane layout. ✗ Don't

If you're not using content panes, don't just stretch UI elements to fill
available display space. Long lines of text are difficult to read. Stretched
buttons look poorly designed. If you use [`Modifier.fillMaxWidth`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).fillMaxWidth(kotlin.Float)), don't
assume that's the right behavior for all display sizes.
Your browser doesn't support the video tag. ✗ Don't: Layout stretched to fill expanding window.

## Input devices

Users don't just use touch screens to interact with apps.

Adaptive apps support external keyboards, mice, and styluses to provide an
enhanced user experience and help users be more productive on form factors of
all kinds.
✓ Do

Take advantage of the built‑in functionality of the Android framework for
keyboard tab navigation and mouse or trackpad click, select, and scroll. Publish
your app's keyboard shortcuts in [Keyboard Shortcuts Helper](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper).

Use the Jetpack [Material 3 library](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) to enable users to write into any
[`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) component using a stylus.
✗ Don't

Don't make alternative input methods impossible. Don't introduce accessibility
issues.

## Summary

- Build your app with Compose and the Material 3 Adaptive library
- Base layouts on window size classes
- Create multi-pane layouts
- Make your app resizable
- Never lock activity orientation
- Don't restrict aspect ratio
- Support input other than touch
- Avoid deprecated APIs

✓ Do what your users expect:
optimize your app for the diversity of devices people rely on every day.

✗ Don't wait. Get started today!