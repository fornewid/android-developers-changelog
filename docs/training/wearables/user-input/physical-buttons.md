---
title: Physical buttons  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/user-input/physical-buttons
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Physical buttons Stay organized with collections Save and categorize content based on your preferences.



A wearable device typically contains multiple physical buttons, also known as
*stems*. Wear OS devices always have, at minimum, one button: the power button.
Beyond that, zero or more multifunction buttons might be present.
Some devices also provide a [physical rotating side button](/training/wearables/compose/rotary-input).

In your app, you can assign multifunction buttons to actions for when your app
is in foreground. For example, a fitness app might start or pause a workout
using multifunction buttons:

![A watch with multiple side buttons. The system designates one of the buttons as the multi-function button.](/static/wear/images/multi_function_buttons.png)


Figure 1. Wear OS fitness app showing multifunction buttons.

For suitable use cases and design considerations, see the
[Wear OS design principles](/training/wearables/design).

This document describes how to retrieve information about available
multifunction
buttons on a device and how to process button presses.

## Button metadata

To get extra information about the buttons on a device, use the API defined in
the [Wear Input](/reference/androidx/wear/input/package-summary) AndroidX
library. Add the following dependency in your app module's `build.gradle` file:

```
dependencies {
implementation "androidx.wear:wear-input:1.2.0"
}
```

### Number of buttons

Determine how many buttons are available on the device, use the
[`WearableButtons.getButtonCount()`](/reference/androidx/wear/input/WearableButtons#getButtonCount(android.content.Context))
method. This method includes the power button, so if the method returns a value
greater than one, then there are multifunction buttons available for use. To get
an accurate count of assignable multifunction buttons, subtract one from the
count, since the first button is always the power button.

### Keycodes for button presses

Each button is mapped to an `int` constant from the
[`KeyEvent`](/reference/android/view/KeyEvent)
class, as shown in the following table:

| Button | KeyEvent |
| --- | --- |
| Multifunction button 1 | `KEYCODE_STEM_1` |
| Multifunction button 2 | `KEYCODE_STEM_2` |
| Multifunction button 3 | `KEYCODE_STEM_3` |

The following example code shows how to get the available button count:

```
val count = WearableButtons.getButtonCount(context)

if (count > 1) {
    Log.d(TAG, "More than one button available")
}

val buttonInfo = WearableButtons.getButtonInfo(
    activity,
    KeyEvent.KEYCODE_STEM_1
)

if (buttonInfo == null) {
    // KEYCODE_STEM_1 is unavailable
    Log.d(TAG, "KEYCODE_STEM_1 not available")
} else {
    // KEYCODE_STEM_1 is present on the device
    Log.d(TAG, "KEYCODE_STEM_1 is present on the device")
}

HardwareButtonsActivity.kt
```

## Handle button presses

There are a number of possible button keycodes that your app can handle:

* `KEYCODE_STEM_1`.
* `KEYCODE_STEM_2`.

Your app can receive these key codes and convert them to specific in-app
actions.

To handle a button press, implement the
[`onKeyDown()`](/reference/android/app/Activity#onKeyDown(int,%20android.view.KeyEvent))
method.

For example, this implementation responds to button presses to control actions
in an app:

```
override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
    return if (event?.repeatCount == 0) {
        when (keyCode) {
            KeyEvent.KEYCODE_STEM_1 -> {
                Log.d(TAG, "KEYCODE_STEM_1 pressed")
                true
            }
            KeyEvent.KEYCODE_STEM_2 -> {
                Log.d(TAG, "KEYCODE_STEM_2 pressed")
                true
            }
            else -> {
                super.onKeyDown(keyCode, event)
            }
        }
    } else {
        super.onKeyDown(keyCode, event)
    }
}

HardwareButtonsActivity.kt
```

## Determine the button positions

The AndroidX Library provides two methods that describe the location of a
button:

* [`WearableButtons.getButtonLabel()`](/reference/androidx/wear/input/WearableButtons#getButtonLabel(android.content.Context,int))
  returns a localized string describing the general placement of the button on
  the device.
* [`WearableButtons.getButtonIcon()`](/reference/androidx/wear/input/WearableButtons#getButtonIcon(android.content.Context,int))
  returns an icon representing the general placement of the button on the
  device.

If these APIs don't suit your app's needs, you can also use the
`WearableButtons.getButtonInfo()` API to get the location of the button on the
screen and handle it in a more customized way. For more information on the APIs,
see the [Wear API reference](/reference/kotlin/androidx/wear/input/package-summary).