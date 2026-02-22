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
override fun dispatchKeyEvent(event: KeyEvent?): Boolean{
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

If you are using Compose on Android TV, you need to make the [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1))
focusable and delegate the event by passing the modifier parameter into the
`AndroidView` accordingly:  

    AndroidView(
      modifier = modifier
        .focusable()
        .onKeyEvent { playerView.dispatchKeyEvent(it.nativeKeyEvent) },
      factory = { playerView }
    )

<br />