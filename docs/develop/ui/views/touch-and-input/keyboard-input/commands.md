---
title: Handle keyboard actions  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/commands
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Handle keyboard actions Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to handle keyboard actions in Compose.

[Handle keyboard actions in Compose →](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands#key_events)

![](/static/images/android-compose-ui-logo.png)

When the user gives focus to an editable text view, such as an
`EditText`
element, and the user has a hardware keyboard attached, all
input is handled by the system. However, if you want to intercept
or directly handle the keyboard input yourself, you can do so by implementing callback methods
from the `KeyEvent.Callback`
interface, such as `onKeyDown()`
and `onKeyMultiple()`.

Both the `Activity`
and `View` classes implement the
`KeyEvent.Callback` interface, so you
generally override the callback methods in your extension of these classes, as
appropriate.

**Note:** When handling keyboard events with the
`KeyEvent` class and related APIs,
expect that the keyboard events are coming only from a hardware keyboard. Never rely on receiving key
events for any key on a soft input method (an on-screen keyboard).

## Handle single key events

To handle an individual key press, implement
`onKeyDown()`
or `onKeyUp()`,
as appropriate. Usually, you use
`onKeyUp()`
if you want to ensure that you receive only one event. If the user presses and holds a key,
then `onKeyDown()` is called multiple times.

For example, this implementation responds to some keyboard keys to control a game:

### Kotlin

```
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
    return when (keyCode) {
        KeyEvent.KEYCODE_D -> {
            moveShip(MOVE_LEFT)
            true
        }
        KeyEvent.KEYCODE_F -> {
            moveShip(MOVE_RIGHT)
            true
        }
        KeyEvent.KEYCODE_J -> {
            fireMachineGun()
            true
        }
        KeyEvent.KEYCODE_K -> {
            fireMissile()
            true
        }
        else -> super.onKeyUp(keyCode, event)
    }
}
```

### Java

```
@Override
public boolean onKeyUp(int keyCode, KeyEvent event) {
    switch (keyCode) {
        case KeyEvent.KEYCODE_D:
            moveShip(MOVE_LEFT);
            return true;
        case KeyEvent.KEYCODE_F:
            moveShip(MOVE_RIGHT);
            return true;
        case KeyEvent.KEYCODE_J:
            fireMachineGun();
            return true;
        case KeyEvent.KEYCODE_K:
            fireMissile();
            return true;
        default:
            return super.onKeyUp(keyCode, event);
    }
}
```

## Handle modifier keys

To respond to modifier key events, such as when a key is combined with `Shift`
or `Control`, you can
query the `KeyEvent`
that is passed to the callback method. Several methods
provide information about modifier keys, such as
`getModifiers()`
and `getMetaState()`.
However, the simplest solution is to check whether
the exact modifier key you care about is being pressed with methods such as
`isShiftPressed()`
and `isCtrlPressed()`.

For example, here's the `onKeyUp()` implementation
again, with extra handling for when the `Shift` key is held down with one of the keys:

### Kotlin

```
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
    return when (keyCode) {
        ...
        KeyEvent.KEYCODE_J -> {
            if (event.isShiftPressed) {
                fireLaser()
            } else {
                fireMachineGun()
            }
            true
        }
        KeyEvent.KEYCODE_K -> {
            if (event.isShiftPressed) {
                fireSeekingMissle()
            } else {
                fireMissile()
            }
            true
        }
        else -> super.onKeyUp(keyCode, event)
    }
}
```

### Java

```
@Override
public boolean onKeyUp(int keyCode, KeyEvent event) {
    switch (keyCode) {
        ...
        case KeyEvent.KEYCODE_J:
            if (event.isShiftPressed()) {
                fireLaser();
            } else {
                fireMachineGun();
            }
            return true;
        case KeyEvent.KEYCODE_K:
            if (event.isShiftPressed()) {
                fireSeekingMissle();
            } else {
                fireMissile();
            }
            return true;
        default:
            return super.onKeyUp(keyCode, event);
    }
}
```

## Additional resources

* [Keyboard Shortcuts Helper](/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper): System screen that enables users to search the keyboard shortcuts your app offers.