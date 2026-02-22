---
title: https://developer.android.com/develop/ui/compose/system/insets-views-compose
url: https://developer.android.com/develop/ui/compose/system/insets-views-compose
source: md.txt
---

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
[`AbstractComposeView.consumeWindowInsets`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/AbstractComposeView#(androidx.compose.ui.platform.AbstractComposeView).consumeWindowInsets())
to `false`.

## Backward compatible inset dispatching for views

If your app contains Views code, you may need to confirm that insets are dispatched
to sibling views on devices that run Android 10 (API level 29) or lower. See the
[edge-to-edge Views guide](https://developer.android.com/develop/ui/views/layout/edge-to-edge#backward-compatible-dispatching)
for more information.

## System bar icons

Calling `enableEdgeToEdge` ensures system bar icon colors update when the device
theme changes.

While going edge-to-edge, you might need to manually update the system bar icon
colors so they contrast with your app's background. For example, to create light
status bar icons:  

### Kotlin

```kotlin
WindowCompat.getInsetsController(window, window.decorView)
    .isAppearanceLightStatusBars = false
```

### Java

```java
WindowCompat.getInsetsController(window, window.getDecorView())
    .setAppearanceLightStatusBars(false);
```