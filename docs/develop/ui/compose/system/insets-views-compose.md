---
title: Use insets in Views and Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/insets-views-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Use insets in Views and Compose Stay organized with collections Save and categorize content based on your preferences.



If your app contains both Compose and View code, you may need to be explicit
about which system insets each one should consume and ensure that insets are
dispatched to sibling views.

## Overriding default insets

You may need to override default insets when your screen has both Views and
Compose code in the same hierarchy. In this case, you need to be explicit in
which one should consume the insets, and which one should ignore them.

For example, if your outermost layout is an Android View layout, you should
consume the insets in the View system and ignore them for Compose.
Alternatively, if your outermost layout is a composable, you should consume the
insets in Compose, and pad the `AndroidView` composables accordingly.

By default, each `ComposeView` consumes all insets at the
`WindowInsetsCompat` level of consumption. To change this default behavior, set
[`AbstractComposeView.consumeWindowInsets`](/reference/kotlin/androidx/compose/ui/platform/AbstractComposeView#(androidx.compose.ui.platform.AbstractComposeView).consumeWindowInsets())
to `false`.

## Backward compatible inset dispatching for views

If your app contains Views code, you may need to confirm that insets are dispatched
to sibling views on devices that run Android 10 (API level 29) or lower. See the
[edge-to-edge Views guide](/develop/ui/views/layout/edge-to-edge#backward-compatible-dispatching)
for more information.

## System bar icons

Calling `enableEdgeToEdge` ensures system bar icon colors update when the device
theme changes.

While going edge-to-edge, you might need to manually update the system bar icon
colors so they contrast with your app's background. For example, to create light
status bar icons:

### Kotlin

```
WindowCompat.getInsetsController(window, window.decorView)
    .isAppearanceLightStatusBars = false
```

### Java

```
WindowCompat.getInsetsController(window, window.getDecorView())
    .setAppearanceLightStatusBars(false);
```

[Previous

arrow\_back

Use Material 3 insets](/develop/ui/compose/system/material-insets)

[Next

About system bar protection

arrow\_forward](/develop/ui/compose/system/system-bars)