---
title: https://developer.android.com/media/media3/ui/androidtv
url: https://developer.android.com/media/media3/ui/androidtv
source: md.txt
---

## D-pad navigation on Android TV

The remote control of Android TV has a D-pad control that sends commands that
arrive as key events at `dispatchKeyEvent(KeyEvent)` of your `Activity`. These
need to be delegated to the [`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView):


### Kotlin

```kotlin
override fun dispatchKeyEvent(event: KeyEvent?): Boolean {
  return playerView.dispatchKeyEvent(event!!) || super.dispatchKeyEvent(event)
}
```

### Java

```java
@Override
public boolean dispatchKeyEvent(KeyEvent event) {
  return playerView.dispatchKeyEvent(event) || super.dispatchKeyEvent(event);
}
```

<br />

Requesting focus for the `PlayerView` is important for navigating playback
controls and skipping ads. Consider requesting the focus in `onCreate` of the
`Activity`:


### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  // ...
  playerView.requestFocus()
  // ...
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  // ...
  playerView.requestFocus();
  // ...
}
```

<br />

If you are using Compose on Android TV, you need to make the [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView.composable#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1))
focusable and delegate the event by passing the modifier parameter into the
`AndroidView` accordingly:


```kotlin
AndroidView(
  modifier = modifier.focusable().onKeyEvent { playerView.dispatchKeyEvent(it.nativeKeyEvent) },
  factory = { playerView },
)
```

<br />

### Use the `Player` composable

If you use the [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/Player.composable) composable from the `media3-ui-compose-material3`
library, D-pad navigation is supported by default. The `Player` and
[`PlayerDefaults`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/PlayerDefaults) components have an automatic [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester) instance that
traverses the components with the D-pad, so you don't need additional code or
[`Modifier.focusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)) to handle focus and key events:

The [`PlayerDefaults`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/material3/PlayerDefaults) are arranged in top, center, and bottom slots so the
D-pad navigation feels intuitive. For any customizations and overrides to those
slots, ensure you provide a well-navigable component. Note that most Compose
components, such as `Slider` or `Row` containing buttons, manage focus
out-of-the-box.