---
title: https://developer.android.com/media/media3/ui/compose
url: https://developer.android.com/media/media3/ui/compose
source: md.txt
---

## Add the dependency

The Media3 library includes two Jetpack Compose-based UI modules. You don't have
to add both of them because the Material3 one depends on the core one.  

### Kotlin

    // Include only one of the following dependencies
    implementation("androidx.media3:media3-ui-compose:1.9.2")
    implementation("androidx.media3:media3-ui-compose-material3:1.9.2")

### Groovy

    // Include only one of the following dependencies
    implementation "androidx.media3:media3-ui-compose:1.9.2"
    implementation "androidx.media3:media3-ui-compose-material3:1.9.2"

We highly encourage you to develop your app in a Compose-first fashion or
[migrate from using Views](https://developer.android.com/develop/ui/compose/migrate).

## Fully Compose demo app

While the `media3-ui-compose` library does not include out-of-the-box
Composables (such as buttons, indicators, images or dialogs), you can find a
[demo app written fully in Compose](https://github.com/androidx/media/tree/release/demos/compose) that avoids any interoperability
solutions like wrapping [`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView) in [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)). The demo app
utilises the UI state holder classes from `media3-ui-compose` module and makes
use of the [Compose Material3](https://developer.android.com/develop/ui/compose/designsystems/material3) library.

## Which library do I need?

Depending on the level of customization you require, you can choose between two
Media3 Compose libraries. To understand the difference, it helps to think about
the [UI state production pipeline](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state-production-pipeline): `Business logic → UI logic → UI`.

**Use `media3-ui-compose` for full control over your UI components.**

This library provides the `Business logic → UI logic` connection. It contains
foundational components like [`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) and [`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0)), along with
state holder classes (e.g., [`PlayPauseButtonState`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/state/PlayPauseButtonState#PlayPauseButtonState(androidx.media3.common.Player))) that convert `Player`
state into UI state.

This library does **not** provide ready-to-use Material Design components. You
are responsible for building your own UI components and styling them. It gives
you maximum control over the look and feel, making it ideal if you have a highly
custom design system.

**Use `media3-ui-compose-material3` for faster integration with Material
Design.**

This library provides the final `UI` part of the pipeline. It depends on
`media3-ui-compose` and includes prebuilt Composable functions that are styled
with [Material3 components](https://m3.material.io/components). It eliminates the need for you to build your own
buttons and other UI elements from scratch. You can still customize the theme,
colors, and icons of these components, but the core implementation is provided
for you.

## At a glance

| Feature | `media3-ui-compose` | `media3-ui-compose-material3` |
|---|---|---|
| **UI Components** | Foundational elements like `PlayerSurface` and `ContentFrame`, but **no** pre-styled buttons or controls. | Provides a full set of prebuilt, Material3-styled `Composables` like `PlayPauseButton`, `SeekBackButton`, `PositionAndDurationText`, etc. |
| **State Management** | Provides `remember...State` holders to manage the logic. | Manages state internally, but you can still access the state holders if you need to. |
| **Dependencies** | `androidx.compose.foundation` | `media3-ui-compose`, `androidx.compose.material3`, `com.google.android.material` |
| **Primary Use Case** | Building a player UI with a custom design system. Full control over the look and feel. | Quickly building a player UI that follows Material Design 3 guidelines. |