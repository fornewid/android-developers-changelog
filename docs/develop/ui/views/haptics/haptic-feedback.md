---
title: https://developer.android.com/develop/ui/views/haptics/haptic-feedback
url: https://developer.android.com/develop/ui/views/haptics/haptic-feedback
source: md.txt
---

One of the most basic use cases for haptics is to provide feedback to user
interactions. Time pickers, the key press on a virtual keyboard, and text
selection are common examples of good use cases for haptic feedback. For more
information about when and how to apply haptics, read
[Haptics design principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles).

This page describes three ways to provide haptic feedback.

- [Use a `View`](https://developer.android.com/develop/ui/views/haptics/haptic-feedback#view) **(recommended)** . This approach is action-oriented, has the widest support, and doesn't require the `VIBRATE` permission.
- [Use a predefined `VibrationEffect`](https://developer.android.com/develop/ui/views/haptics/haptic-feedback#predefined_vibrationeffect). This approach has more flexibility, but with some trade-offs.
- [Use advanced compositions with primitives](https://developer.android.com/develop/ui/views/haptics/haptic-feedback#advanced_composition). This method is newer and even more flexible, but requires specific device support.

These methods use primitives defined at the device level to provide high quality
feedback tailored to the device in hand.

> [!CAUTION]
> **Caution:** We strongly discourage using older `Vibrator` methods employing `createOneshot` or `createWaveform`, even if they appear to be supported on the device. These modes are often too loud for regular haptic feedback; use them only as a fallback if you need to highlight an extremely important action.

All haptic feedback methods respect the user's touch feedback settings by
default.

## Use `View` components to generate haptic feedback

Use the [`View.performHapticFeedback`](https://developer.android.com/reference/android/view/View#performHapticFeedback(int)) method to generate haptic feedback. The
haptic constants defined by the [`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants) are focused on their
functionality in an application, not the type of haptic effect performed.

The underlying implementation might vary depending on the device and hardware
capabilities, but the app only needs to consider the type of feedback to provide
in a particular context. By focusing on the functionality, you can enable haptic
feedback for similar interactions. Users learn to associate different meanings
to different haptic sensations over time.

### Prerequisites: Enable haptic feedback

As long as the [`View`](https://developer.android.com/reference/android/view/View) is visible, haptic feedback can be used for its events.
Some events, such as long press, have default haptics that are triggered if a
listener on the view handles the event (returns `true`).

An Android `View` can disable haptic feedback by setting the
[`View.hapticFeedbackEnabled`](https://developer.android.com/reference/android/view/View#attr_android:hapticFeedbackEnabled) property to `false`. Disabling this property
results in default feedback.

The [`performHapticFeedback`](https://developer.android.com/reference/android/view/View#performHapticFeedback(int)) method also honors the system setting
[`HAPTIC_FEEDBACK_ENABLED`](https://developer.android.com/reference/android/provider/Settings.System#HAPTIC_FEEDBACK_ENABLED), which allows the user to potentially disable them
for the entire system.

Unlike other haptic APIs, using `HapticFeedbackConstants` with a `View`
doesn't require the `VIBRATE` permission.

### Choose a `HapticFeedbackConstant`

When using `View` components with `HapticFeedbackConstants`, there's no need
to evaluate specific device support, as these constants will have fallback
behavior if necessary. The only consideration is the SDK level of the desired
constant.

### Example 1: Keypress

This is an example of how to add a haptic feedback to a touch input in `View`
using touch listeners. The effects simulate the feeling of pressing down on a
button and then releasing it.

### Kotlin

```kotlin
class HapticTouchListener : View.OnTouchListener {
  override fun onTouch(View view, MotionEvent event) : Boolean {
    when (event.actionMasked) {
      MotionEvent.ACTION_DOWN ->
        view.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
      MotionEvent.ACTION_UP ->
        view.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY_RELEASE)
    }
    return true
  }
}
```

### Java

```java
class HapticTouchListener implements View.OnTouchListener {
  @Override
  public boolean onTouch(View view, MotionEvent event) {
    switch (event.getAction()) {
      case MotionEvent.ACTION_DOWN:
        view.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY);
        break;
      case MotionEvent.ACTION_UP:
        view.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY_RELEASE);
        break;
    }
    return true;
  }
}
```

### Example 2: Submit button

Haptic feedback use cases go beyond simulating a physical interaction with the
device. They might also be used to convey an abstract meaning. For example,
the general expectation for a
[`CONFIRM`](https://developer.android.com/reference/android/view/HapticFeedbackConstants#CONFIRM) effect is a
short and light vibration while a
[`REJECT`](https://developer.android.com/reference/android/view/HapticFeedbackConstants#REJECT) might be a
stronger feedback to signal failure. This is illustrated in the following
example for a submit button feedback.

### Kotlin

```kotlin
submitButton.setOnClickListener { view ->
  val successful = performSubmit()
  if (successful) {
    view.performHapticFeedback(HapticFeedbackConstants.CONFIRM)
  } else {
    view.performHapticFeedback(HapticFeedbackConstants.REJECT)
  }
}
```

### Java

```java
submitButton.setOnClickListener(view -> {
  boolean successful = performSubmit();
  if (successful) {
    view.performHapticFeedback(HapticFeedbackConstants.CONFIRM);
  } else {
    view.performHapticFeedback(HapticFeedbackConstants.REJECT);
  }
});
```

## Use a predefined `VibrationEffect` to generate haptic feedback

Using the [`View`-based](https://developer.android.com/develop/ui/views/haptics/haptic-feedback#view) approach focuses on the user interaction. It is
preferred for consistency across the system. However, specific predefined
[`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect) APIs can also be invoked for customized haptic feedback
effects.

Predefined effects are available as [`VibrationEffect`
constants](https://developer.android.com/reference/android/os/VibrationEffect#constants_1), and can be
checked for support and played with the [`Vibrator`](https://developer.android.com/reference/android/os/Vibrator) service as shown in the
following examples.

### Understand device support of `VibrationEffect` APIs

In basic usage, there should be no need to check for support of individual
`VibrationEffect` APIs. The APIs such as [`Vibrator.areEffectsSupported`](https://developer.android.com/reference/android/os/Vibrator#areEffectsSupported(int...))
and [`Vibrator.areAllEffectsSupported`](https://developer.android.com/reference/android/os/Vibrator#areAllEffectsSupported(int...)) are used to determine if the device has
a *customized* implementation of the constant. If a customized effect isn't
present, your app can still play the effects and use a platform-defined
fallback implementation.

For more details, see [Predefined
`VibrationEffect`](https://developer.android.com/develop/ui/views/haptics/haptics-apis#predefined_vibration_effect).

### Prerequisites: Load the Vibrator and the `VIBRATE` permission

Most vibrations can be played with the `Vibrator` service, which can be loaded
as follows:

### Kotlin

```kotlin
import android.os.Vibrator

val vibrator = context.getSystemService(Vibrator::class.java)
```

### Java

```java
import android.os.Vibrator;

Vibrator vibrator = context.getSystemService(Vibrator.class);
```

The app needs to have the
[`VIBRATE`](https://developer.android.com/reference/android/Manifest.permission#VIBRATE) permission in order
to vibrate the device using this service. The permission can be added to the
application manifest file:

    <uses-permission android:name="android.permission.VIBRATE"/>

### Play a predefined `VibrationEffect`

> [!CAUTION]
> **Caution:** Following the [guidelines](https://developer.android.com/develop/ui/views/haptics/haptics-principles#guidelines), effects should be *clear* and their strengths should correspond with *importance*. If an effect isn't available, consider falling back to nothing rather than a discordant alternative.

Predefined effects can be prepared using [`VibrationEffect.createPredefined`](https://developer.android.com/reference/android/os/VibrationEffect#createPredefined(int)),
then played using one of the `vibrate` methods on [`Vibrator`](https://developer.android.com/reference/android/os/Vibrator).

This example plays a Click effect.

### Kotlin

```kotlin
val vibrator = context.getSystemService(Vibrator::class.java)
...
// Requires VIBRATE permission
vibrator.vibrate(VibrationEffect.createPredefined(VibrationEffect.EFFECT_CLICK))
```

### Java

```java
Vibrator vibrator = context.getSystemService(Vibrator.class);
...
// Requires VIBRATE permission
vibrator.vibrate(VibrationEffect.createPredefined(VibrationEffect.EFFECT_CLICK));
```

## Use advanced compositions with primitives

The [`VibrationEffect.Composition`](https://developer.android.com/reference/android/os/VibrationEffect.Composition) API offers additional possibilities for
haptic feedback. However, unlike effects, these primitives don't have
system-level fallbacks, which means that careful attention needs to be paid to
the primitives and other capabilities supported by the device.

Using these APIs is discussed in more detail in
[*Creating Custom Haptic Effects*](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#vibration_compositions).