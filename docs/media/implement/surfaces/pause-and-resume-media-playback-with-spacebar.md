---
title: https://developer.android.com/media/implement/surfaces/pause-and-resume-media-playback-with-spacebar
url: https://developer.android.com/media/implement/surfaces/pause-and-resume-media-playback-with-spacebar
source: md.txt
---

# Pause and resume media playback with external keyboard Spacebar

Whenever your app plays a media file, users should be able to pause and resume playback by pressing the<kbd>Spacebar</kbd>on a physical keyboard.

## Respond to keypress events

Apps based on Jetpack Compose or views respond to keyboard key presses in similar ways: the app listens for keypress events, filters the events, and responds to keypresses such as a<kbd>Spacebar</kbd>keypress.

### 1. Listen for keyboard events

**Compose**

With Jetpack Compose, use either the[`onPreviewKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).onPreviewKeyEvent(kotlin.Function1))or the[`onKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).onKeyEvent(kotlin.Function1))modifier within the layout that manages the keystroke:  

    Column(modifier = Modifier.onPreviewKeyEvent { event ->
        if (event.type == KeyEventType.KeyUp) {
            ...
        }
        ...
    })

or  

    Column(modifier = Modifier.onKeyEvent { event ->
        if (event.type == KeyEventType.KeyUp) {
            ...
        }
        ...
    })

| **Note:** The main difference between the two modifiers is where the event is dispatched if the modifier does not consume it:  
|
| - `onPreviewKeyEvent`--- Dispatches the event to its first child
| - `onKeyEvent`--- Dispatches the event to the composable's parent

**Views**

In an activity in your app, override the[`onKeyUp()`](https://developer.android.com/reference/kotlin/android/app/Activity#onkeyup)method:  

### Kotlin

```kotlin
override fun onKeyUp(keyCode: Int, event: KeyEvent?): Boolean {
    ...
}
```

### Java

```java
@Override
public boolean onKeyUp(int keyCode, KeyEvent event) {
    ...
}
```

The method is invoked every time a pressed key is released, so it fires exactly once for every keystroke.
| **Caution:** Do not use the[`onKeyDown()`](https://developer.android.com/reference/kotlin/android/app/Activity#onkeydown)method, which fires repeatedly as long as the key is pressed.

### 2. Filter<kbd>Spacebar</kbd>presses

Inside the Compose`onPreviewKeyEvent`and`onKeyEvent`modifier methods or views`onKeyUp()`method, filter for[`KeyEvent.KEYCODE_SPACE`](https://developer.android.com/reference/kotlin/android/view/KeyEvent#keycode_space)to send the correct event to your media component:

**Compose**  

    Column(modifier = Modifier.onPreviewKeyEvent { event ->
        if (event.type == KeyEventType.KeyUp && event.key == Key.Spacebar) {
            ...
        }
        ...
    })

or  

    Column(modifier = Modifier.onKeyEvent { event ->
        if (event.type == KeyEventType.KeyUp && event.key == Key.Spacebar) {
            ...
        }
        ...
    })

**Views**  

### Kotlin

```kotlin
if (keyCode == KeyEvent.KEYCODE_SPACE) {
    togglePlayback()
    return true
}
return false
```

### Java

```java
if (keyCode == KeyEvent.KEYCODE_SPACE) {
    togglePlayback();
    return true;
}
return false;
```
| **Note:** Return`true`from the`onKeyUp()`method if your code manages the event and you don't want the event to propagate any further. Return`false`if you want to allow propagation of the event so that other components can manage the event.

## Key points

- [`KEYCODE_SPACE`](https://developer.android.com/reference/kotlin/android/view/KeyEvent#keycode_space): Key code constant for the<kbd>Spacebar</kbd>.

**Compose**

- [`onPreviewKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).onPreviewKeyEvent(kotlin.Function1)): Modifier that enables a component to intercept hardware key events when it (or one of its children) is focused.
- [`onKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).onKeyEvent(kotlin.Function1)): Similar to`onPreviewKeyEvent`, modifier that enables a component to intercept hardware key events when the component (or one of its children) is focused.

**Views**

- [`onKeyUp()`](https://developer.android.com/reference/kotlin/android/app/Activity#onkeyup): Event handler called when a key is released and not handled by a view (such as[`TextView`](https://developer.android.com/reference/kotlin/android/widget/TextView)) within an activity.

### Results

Your app can now respond to<kbd>Spacebar</kbd>key presses to pause and resume a video or other media.