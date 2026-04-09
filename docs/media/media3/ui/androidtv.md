---
title: Android TV  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/ui/androidtv
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Android TV Stay organized with collections Save and categorize content based on your preferences.




## D-pad navigation on Android TV

The remote control of Android TV has a D-pad control that sends commands that
arrive as key events at `dispatchKeyEvent(KeyEvent)` of your `Activity`. These
need to be delegated to the [`PlayerView`](/reference/androidx/media3/ui/PlayerView):

### Kotlin

```
override fun dispatchKeyEvent(event: KeyEvent?): Boolean {
  return playerView.dispatchKeyEvent(event!!) || super.dispatchKeyEvent(event)
}

AndroidTv.kt
```

### Java

```
@Override
public boolean dispatchKeyEvent(KeyEvent event) {
  return playerView.dispatchKeyEvent(event) || super.dispatchKeyEvent(event);
}

AndroidTv.java
```

Requesting focus for the `PlayerView` is important for navigating playback
controls and skipping ads. Consider requesting the focus in `onCreate` of the
`Activity`:

### Kotlin

```
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  // ...
  playerView.requestFocus()
  // ...
}

AndroidTv.kt
```

### Java

```
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  // ...
  playerView.requestFocus();
  // ...
}

AndroidTv.java
```

If you are using Compose on Android TV, you need to make the [`AndroidView`](/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView.composable#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1))
focusable and delegate the event by passing the modifier parameter into the
`AndroidView` accordingly:

```
AndroidView(
  modifier = modifier.focusable().onKeyEvent { playerView.dispatchKeyEvent(it.nativeKeyEvent) },
  factory = { playerView },
)

AndroidTv.kt
```