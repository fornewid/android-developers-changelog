---
title: https://developer.android.com/games/playgames/input-mouse
url: https://developer.android.com/games/playgames/input-mouse
source: md.txt
---

This topic covers how to implement mouse input for Google Play Games on PC for
games where input translation mode doesn't provide an ideal player experience.

PC players typically have a keyboard and mouse rather than a touchscreen, making
it important to consider whether your game accomodates mouse input. By default,
Google Play Games on PC converts any left-click mouse event into a single
virtual tap event. This is known as "input translation mode".

Although this mode makes your game functional with few changes, it does not
provide PC players with a native-feeling experience. For that, we recommend
that you implement the following:

- Hover states for context menus rather than press and hold actions
- Right-click for alternative actions that happen on long press or in a context menu
- Mouselook for first or third person action games rather than a press and drag event

In order to support UI patterns that are common on PCs, you must disable input
translation mode.

Input handling for Google Play Games on PC is identical to that of
[ChromeOS](https://developer.android.com/topic/arc/input-compatibility). The changes that support PCs also
improve your game for all Android players.

> [!NOTE]
> **Note:** If your game is using Unity, you could checkout this [input_capture_package plugin](https://github.com/android/games-samples/tree/main/googleplaygamesforpc/unity_projects/input_capture_package) to handle mouse capture for you.

## Disable input translation mode

In your [`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro) file,
declare the
`android.hardware.type.pc` [feature](https://developer.android.com/guide/topics/manifest/manifest-intro#uses-feature).
This indicates that your game uses PC hardware and disables input translation
mode. In addition, adding `required="false"` helps ensure that your game can
still be installed on phones and tablets without a mouse. For example:

    <manifest ...>
      <uses-feature
          android:name="android.hardware.type.pc"
          android:required="false" />
      ...
    </manifest>

The production version of Google Play Games on PC switches to the correct
mode when a game launches. When running in the developer emulator, you need to
right-click the task bar icon, select **Developer Options** , and then
**PC mode(KiwiMouse)** to receive raw mouse input.

![Screenshot of the "PC mode(KiwiMouse)" selected in the context menu](https://developer.android.com/static/images/games/playgames/input-mouse-kiwi-mouse.png)

After you do this, the mouse movement is reported by [View.onGenericMotionEvent](https://developer.android.com/reference/android/view/View#onGenericMotionEvent(android.view.MotionEvent)) with the source [`SOURCE_MOUSE`](https://developer.android.com/reference/android/view/InputDevice#SOURCE_MOUSE)
indicating that it's a mouse event.

### Kotlin

```kotlin
gameView.setOnGenericMotionListener { _, motionEvent ->
    var handled = false
    if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
        // handle the mouse event here
        handled = true
    }
    handled
}
```

### Java

```java
gameView.setOnGenericMotionListener((view, motionEvent) -> {
    if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
        // handle the mouse event here
        return true;
    }
    return false;
});
```

For details on handling mouse input, see the
[ChromeOS documentation](https://chromeos.dev/en/android/input-compatibility#mouse-and-touchpad-support).

## Handling mouse movement

To detect mouse movement, listen to the [`ACTION_HOVER_ENTER`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_HOVER_ENTER), [`ACTION_HOVER_EXIT`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_HOVER_EXIT), and
[`ACTION_HOVER_MOVE`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_HOVER_MOEV)
events.

This is best used to detect the user hovering over buttons or objects in a
game, giving you a chance to display a hint box or implement a mouseover state
to highlight what a player is about to select. For example:

### Kotlin

```kotlin
gameView.setOnGenericMotionListener { _, motionEvent ->
   var handled = false
   if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
       when(motionEvent.action) {
           MotionEvent.ACTION_HOVER_ENTER -> Log.d("MA", "Mouse entered at ${motionEvent.x}, ${motionEvent.y}")
           MotionEvent.ACTION_HOVER_EXIT -> Log.d("MA", "Mouse exited at ${motionEvent.x}, ${motionEvent.y}")
           MotionEvent.ACTION_HOVER_MOVE -> Log.d("MA", "Mouse hovered at ${motionEvent.x}, ${motionEvent.y}")
       }
       handled = true
   }

   handled
}
```

### Java

```java
gameView.setOnGenericMotionListener((view, motionEvent) -> {
    if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
        switch (motionEvent.getAction()) {
            case MotionEvent.ACTION_HOVER_ENTER:
                Log.d("MA", "Mouse entered at " + motionEvent.getX() + ", " + motionEvent.getY());
                break;
            case MotionEvent.ACTION_HOVER_EXIT:
                Log.d("MA", "Mouse exited at " + motionEvent.getX() + ", " + motionEvent.getY());
                break;
            case MotionEvent.ACTION_HOVER_MOVE:
                Log.d("MA", "Mouse hovered at " + motionEvent.getX() + ", " + motionEvent.getY());
                break;
        }
        return true;
    }
    return false;
});
```

## Handling mouse buttons

PCs have long had both left and right mouse buttons, giving interactive elements
both primary and secondary actions. In a game, tap actions like tapping on a
button are best mapped to left-click where touch \& hold actions feel most
natural with right-click. In real time strategy games you might also use
left-click to select and right-click to move. First person shooters might assign
primary and secondary fire-to-left and right-click. An infinite runner might
use left-click to jump and right-click to dash. We have not added support for
the middle-click event.

To handle button presses, use `ACTION_DOWN` and `ACTION_UP`. Then use
`getActionButton` to determine which button triggered the action or
`getButtonState` to get the state of all the buttons.

In this example, an enum is used to help display the result of
`getActionButton`:

### Kotlin

```kotlin
enum class MouseButton {
   LEFT,
   RIGHT,
   UNKNOWN;
   companion object {
       fun fromMotionEvent(motionEvent: MotionEvent): MouseButton {
           return when (motionEvent.actionButton) {
               MotionEvent.BUTTON_PRIMARY -> LEFT
               MotionEvent.BUTTON_SECONDARY -> RIGHT
               else -> UNKNOWN
           }
       }
   }
}
```

### Java

```java
enum MouseButton {
    LEFT,
    RIGHT,
    MIDDLE,
    UNKNOWN;
    static MouseButton fromMotionEvent(MotionEvent motionEvent) {
        switch (motionEvent.getActionButton()) {
            case MotionEvent.BUTTON_PRIMARY:
                return MouseButton.LEFT;
            case MotionEvent.BUTTON_SECONDARY:
                return MouseButton.RIGHT;
            default:
                return MouseButton.UNKNOWN;
        }
    }
}
```

In this example, the action is handled similar to the hover events:

### Kotlin

```kotlin
// Handle the generic motion event
gameView.setOnGenericMotionListener { _, motionEvent ->
   var handled = false
   if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
       when (motionEvent.action) {
           MotionEvent.ACTION_BUTTON_PRESS -> Log.d(
               "MA",
               "${MouseButton.fromMotionEvent(motionEvent)} pressed at ${motionEvent.x}, ${motionEvent.y}"
           )
           MotionEvent.ACTION_BUTTON_RELEASE -> Log.d(
               "MA",
               "${MouseButton.fromMotionEvent(motionEvent)} released at ${motionEvent.x}, ${motionEvent.y}"
           )
       }
       handled = true
   }

   handled
}
```

### Java

```java
gameView.setOnGenericMotionListener((view, motionEvent) -> {
    if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
        switch (motionEvent.getAction()) {
            case MotionEvent.ACTION_BUTTON_PRESS:
                Log.d("MA", MouseButton.fromMotionEvent(motionEvent) + " pressed at " + motionEvent.getX() + ", " + motionEvent.getY());
                break;
            case MotionEvent.ACTION_BUTTON_RELEASE:
                Log.d("MA", MouseButton.fromMotionEvent(motionEvent) + " released at " + motionEvent.getX() + ", " + motionEvent.getY());
                break;
        }
        return true;
    }
    return false;
});
```

## Handle mousewheel scrolling

We recommend that you use the mouse scroll wheel in place of pinch to zoom
gestures or touch and drag scroll areas in your game.

To read scroll wheel values, listen for the `ACTION_SCROLL` event. The *delta*
since the last frame can be retrieved using `getAxisValue` with `AXIS_VSCROLL`
for vertical offset and `AXIS_HSCROLL` for horizontal offset. For example:

### Kotlin

```kotlin
gameView.setOnGenericMotionListener { _, motionEvent ->
   var handled = false
   if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
       when (motionEvent.action) {
           MotionEvent.ACTION_SCROLL -> {
               val scrollX = motionEvent.getAxisValue(MotionEvent.AXIS_HSCROLL)
               val scrollY = motionEvent.getAxisValue(MotionEvent.AXIS_VSCROLL)
               Log.d("MA", "Mouse scrolled $scrollX, $scrollY")
           }
       }
       handled = true
   }
   handled
}
```

### Java

```java
gameView.setOnGenericMotionListener((view, motionEvent) -> {
    if (motionEvent.isFromSource(InputDevice.SOURCE_CLASS_POINTER)) {
        switch (motionEvent.getAction()) {
            case MotionEvent.ACTION_SCROLL:
                float scrollX = motionEvent.getAxisValue(MotionEvent.AXIS_HSCROLL);
                float scrollY = motionEvent.getAxisValue(MotionEvent.AXIS_VSCROLL);
                Log.d("MA", "Mouse scrolled " + scrollX + ", " + scrollY);
                break;
        }
        return true;
    }
    return false;
});
```

## Capture mouse input

Some games need to take full control of the mouse cursor such as first or third
person action games that map mouse movement to camera movement. To take
exclusive control of the mouse, invoke [`View.requestPointerCapture()`](https://developer.android.com/reference/android/view/View#requestPointerCapture()).

`requestPointerCapture()` only works when the view hierarchy containing your
view has focus. For this reason, you cannot acquire pointer capture in the
`onCreate` callback. You should either wait for player interaction to capture
the mouse pointer, such as when interacting with the main menu, or use the
[`onWindowFocusChanged`](https://developer.android.com/reference/android/app/Activity#onWindowFocusChanged(boolean))
callback. For example:

### Kotlin

```kotlin
override fun onWindowFocusChanged(hasFocus: Boolean) {
   super.onWindowFocusChanged(hasFocus)

   if (hasFocus) {
       gameView.requestPointerCapture()
   }
}
```

### Java

```java
@Override
public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus);

    if (hasFocus) {
        View gameView = findViewById(R.id.game_view);
        gameView.requestPointerCapture();
    }
}
```

Events captured by [`requestPointerCapture()`](https://developer.android.com/reference/android/view/View#requestPointerCapture())
are dispatched to the focusable view that registered
`OnCapturedPointerListener`. For example:

### Kotlin

```kotlin
gameView.focusable = View.FOCUSABLE
gameView.setOnCapturedPointerListener { _, motionEvent ->
    Log.d("MA", "${motionEvent.x}, ${motionEvent.y}, ${motionEvent.actionButton}")
    true
}
```

### Java

```java
gameView.setFocusable(true);
gameView.setOnCapturedPointerListener((view, motionEvent) -> {
    Log.d("MA", motionEvent.getX() + ", " + motionEvent.getY() + ", " + motionEvent.getActionButton());
    return true;
});
```

In order to release exclusive mouse capture, such as to allow players to
interact with a pause menu, invoke [`View.releasePointerCapture()`](https://developer.android.com/reference/android/view/View#releasePointerCapture()).