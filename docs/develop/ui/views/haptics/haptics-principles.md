---
title: https://developer.android.com/develop/ui/views/haptics/haptics-principles
url: https://developer.android.com/develop/ui/views/haptics/haptics-principles
source: md.txt
---

When it comes to haptic feedback on mobile devices, less is more. Too much
vibration can be annoying and even numbing to the hands, as the device is
usually in-hand with the user's full attention. It can also be distracting from
the user's intended task, which may lead the user to quickly turn off all
haptics. However, well crafted haptics provide valuable sensory feedback that
provide users with a richer engagement with their device.

This page explains use cases for using haptics, introduces
[classifications](https://developer.android.com/develop/ui/views/haptics/haptics-principles#haptics_classifications) for haptic effects, and also covers
basic [guidelines](https://developer.android.com/develop/ui/views/haptics/haptics-principles#haptics_design_guidelines) for apps.

## Use cases for adding haptics to your app

Here are some reasons for incorporating haptics into your app.

- **To notify the user of an event that needs their attention.** Examples
  include an incoming phone call or text message, or an upcoming meeting on
  the calendar.

- **To confirm a state change in the device following a user action.**
  Examples include click feedback for a button press, unlocking a phone,
  fingerprint acceptance or rejection, or activating the camera.

- **To delight the user with effects.** Such effects could enhance an ongoing
  user action or emulate physical interaction. Examples include scroll
  feedback, a slider snapping into place, or haptic effects in sync with
  animations, sounds, videos, and games.

## Haptics classifications

The haptic principles presented here are designed around *clear haptics* ,
*rich haptics* , and *buzzy haptics*.

### Clear haptics

Clear haptics refers to crisp and clean sensations associated with a discrete
event, such as button presses. These effects often aim to imitate a
corresponding real-world mechanical action, like those felt when pressing on a
physical button.

Android has predefined clear haptic effects in [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect). However,
in general apps should use action-oriented constants from
[`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants) to ensure consistency of effect and action across
the device.

The other advantage of action-oriented constants is that the platform can
provide fallback behavior if a more complex effect isn't supported by the
user's device.

As you expand the use cases of haptic feedback, the available clear haptics can
sometimes feel plain and monotone. In that case, aim for rich haptics
that are more expressive.

### Rich haptics

Rich haptics generally require haptic actuators that have a wider frequency
bandwidth, enabling greater expressiveness and range. Rich haptics can also be
produced by sequencing clear haptics [primitives](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#primitives) in varied amplitudes and
intervals.

Examples of rich haptic effects are:

- A "fluttery" sensation, similar to a butterfly flapping its wings on your fingertip
- The texture of a surface felt by a finger dragging or swiping across it
- The sensations of wobbliness and instability, or heaviness and reverberation

> [!CAUTION]
> **Caution:** Rich haptics are supported by fewer devices, so it's important to have a fallback strategy.

### Buzzy haptics

Buzzy haptics can be characterized by noisy, sharp and penetrating vibrations
that leave an after effect such as a tingling sensation even after the vibration
is over. It also tends to have a ringing effect that feels like a reverberation
before the vibration stops completely.

Examples of buzzy haptic sensations are:

- Operating a jackhammer
- Riding a motorcycle
- In mobile devices, a long-winded, ringing vibration after a key press

Dating back to pagers and feature phones, low-end mobile phones with
low-performance haptic actuators or drivers tended to produce buzzy long
vibrations for notification purposes.

> [!IMPORTANT]
> **Important:** Given the choice of buzzy haptics or no haptics for touch feedback, choose no haptics. Some situations where an event is always intended to grab the users attention, such as an incoming notification or call, may be appropriate for applying a buzzy fallback.

## Haptics design guidelines

At a high level, the design guidelines can be summarized as:

- Favor rich and clear haptics over buzzy haptics.
- Be consistent, both with the system and the app design.
- Be mindful of frequency of use, and importance.

### Prioritize predefined haptic constants and effects

If your action is covered by a predefined action present in
[`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants), use that constant. This ensures a consistent
user interaction experience, which is particularly valuable as an accessibility
consideration.

If you're creating your own effect, consider using the [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect)
predefined effects and the [`VibrationEffect.Composition`](https://developer.android.com/reference/android/os/VibrationEffect.Composition) primitives. They
are more likely to give a consistent quality experience across devices that
support them.

### Correlate event importance and frequency with strength

Haptic effects shouldn't overwhelm the user or feel gratuitous.

- Haptic effects applied to very frequent events, like scrolling or moving a
  text handle, should be very subtle to provide a pleasant overall experience.

- More important events, like refreshing a page or submitting a form, should
  be stronger than changing a toggle or scrolling on a list, for example.

- Combine both concepts to create effects that become stronger as the
  interaction reaches a target, for example gradually increasing the amplitude
  of a sequence of ticks with dragging, dropping or snapping actions.

### Be consistent

Be consistent within your app with the application of haptics. If a particular
interaction, like form submission or in-app navigation, has haptic feedback,
make sure the same effect is applied to all similar interactions. This helps
users to associate a meaning to a particular haptic feedback.

Also be consistent with the Android system by using the same
[`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants) for well defined interactions, like time pickers or
virtual keyboards.

### Design visual and audio experience together with haptics

Consider haptics as part of the total user experience.

We strongly recommend co-design of visual, audio, and haptic effects. Make it
harmonious or congruent with visual animations and sound patterns. Visual and
auditory inputs can enhance the haptics perceived, and a well-designed haptic
effect can provide a sense of *physicality* to visual and audio effects.

Conversely, a haptic feedback that is played out of sync or that feels
inconsistent with visual and audio effects can be a bit unsettling to the user.
In some cases, the user may perceive the haptic actuator to be broken.

### Avoid legacy one-shot vibrations for haptic feedback

Avoid using the legacy [one-shot
vibrations](https://developer.android.com/develop/ui/views/haptics/haptics-apis#on_off_vibrations), like the
ones defined by [`VibrationEffect.createOneShot`](https://developer.android.com/reference/android/os/VibrationEffect#createOneShot(long,%20int)) or performed with the APIs
[`Vibrator.vibrate(long)`](https://developer.android.com/reference/android/os/Vibrator#vibrate(long)) and [`Vibrator.vibrate(long[], int)`](https://developer.android.com/reference/android/os/Vibrator#vibrate(long%5B%5D,%20int)).

These vibrations might feel buzzy when they last for a long period after the
input waveform has ended, especially on devices with a low-performance haptic
actuator or driver.

A good keyclick haptic feedback signal should last between 10 to 20
milliseconds. However, the actuator may continue to ring for another 20 to 50
milliseconds after a 20-millisecond input to the actuator has ended. Therefore,
it's best to avoid single-shot vibrations for this type of feedback.