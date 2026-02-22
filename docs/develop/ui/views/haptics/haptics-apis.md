---
title: https://developer.android.com/develop/ui/views/haptics/haptics-apis
url: https://developer.android.com/develop/ui/views/haptics/haptics-apis
source: md.txt
---

This section gives an introduction to the various haptics APIs
available in Android. It also covers when and how to check for any device
support necessary to ensure your haptic effects play as you intend.

There are several different ways to create haptic effects, and it's important to
consider Android haptics [design principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles) when choosing among
them. The following table summarizes these high level attributes of each
approach:

- *Availability* is particularly important when planning behavior fallback, and needs to be combined with checking individual device support.
- [Clear haptics](https://developer.android.com/develop/ui/views/haptics/haptics-principles#clear_haptics) are crisp and clean sensations that are less jarring for users.
- [Rich haptics](https://developer.android.com/develop/ui/views/haptics/haptics-principles#rich_haptics) have greater expressiveness and often require more feature-rich hardware.

| API surface | Availability | Clear haptics | Rich haptics |
|---|---|---|---|
| [HapticFeedbackConstants](https://developer.android.com/develop/ui/views/haptics/haptics-apis#haptic_feedback_constants) | Android 1.5+ (per constant) |   |   |
| [Predefined VibrationEffect](https://developer.android.com/develop/ui/views/haptics/haptics-apis#predefined_vibration_effect) | Android 10+ |   |   |
| [VibrationEffect Composition](https://developer.android.com/develop/ui/views/haptics/haptics-apis#vibration_effect_composition) | Android 11+ (per constant) |   |   |
| [On/off, one-shot and waveform vibrations](https://developer.android.com/develop/ui/views/haptics/haptics-apis#on_off_vibrations) | Android 1 |   |   |

Additionally, [notification APIs](https://developer.android.com/develop/ui/views/haptics/haptics-apis#notification_apis), described on this page,
allows you to customize the haptic effects that play for incoming notifications.

Also described on this page are additional concepts that span the API surfaces:

- [Does the device have a vibrator?](https://developer.android.com/develop/ui/views/haptics/haptics-apis#has_vibrator)
- [Amplitude control](https://developer.android.com/develop/ui/views/haptics/haptics-apis#amplitude_control) allows smoother, richer haptic effects, but is not supported by all devices.
- [`VibrationAttributes()`](https://developer.android.com/develop/ui/views/haptics/haptics-apis#vibration_attributes) helps you classify vibration based on its usage, ensuring the appropriate user settings will be applied to it and thus avoiding surprises to the user.

## `HapticFeedbackConstants`

The [`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants) class provides action-based constants to allow
apps to add haptic feedback that's consistent across the device experience,
rather than each app having different effects for common actions.

### Compatibility and requirements

Using the [`View.performHapticFeedback`](https://developer.android.com/reference/android/view/View#performHapticFeedback(int)) method with these constants does not
require any special permissions for the app. It is subject to the
[`View.hapticFeedbackEnabled`](https://developer.android.com/reference/android/view/View#attr_android:hapticFeedbackEnabled) property, which if set to `false` will disable
all haptic feedback calls on the view, including default ones.The primary
related setting the [`View.hapticFeedbackEnabled`](https://developer.android.com/reference/android/view/View#attr_android:hapticFeedbackEnabled) property, which if set to
`false` will disable all haptic feedback calls on the view, including default
ones. The method also honours the user's system setting for enabling touch
feedback.

The only compatibility consideration is the SDK-level of the specific constant
for the action.

There is no need to provide fallback behavior when using
[`HapticFeedbackConstants`](https://developer.android.com/reference/android/view/HapticFeedbackConstants).

### Usage of `HapticsFeedbackConstants`

For details on using `HapticFeedbackConstants`, see [Add haptic feedback to
events](https://developer.android.com/develop/ui/views/haptics/haptic-feedback).

## Predefined `VibrationEffect`

The [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect#constants) class
provides several predefined constants such as `CLICK`, `TICK` and
`DOUBLE_CLICK`. These effects may be optimized for the device.

### Compatibility and requirements

Playing any `VibrationEffect` requires the `VIBRATE` permission in the app
manifest.

There is no need to provide fallback behavior when using predefined
`VibrationEffect`, as constants that don't have a device-optimized
implementation revert to a standard platform fallback.

The [`Vibrator.areEffectsSupported`](https://developer.android.com/reference/android/os/Vibrator#areEffectsSupported(int...)) and [`Vibrator.areAllEffectsSupported`](https://developer.android.com/reference/android/os/Vibrator#areAllEffectsSupported(int...))
APIs are for determining if there is a *device-optimized implementation* .
Predefined effects can still be used without an optimized implementation, and
uses the standard platform fallback. Consequently, these
`areEffectsSupported` APIs are only needed if an application wants to take into
consideration whether the effect is optimized for the device or not.

The effect-checking methods can return one of three values:

- [`VIBRATION_EFFECT_SUPPORT_YES`](https://developer.android.com/reference/android/os/Vibrator#VIBRATION_EFFECT_SUPPORT_YES) indicates that the device has optimized support for this effect.
- [`VIBRATION_EFFECT_SUPPORT_NO`](https://developer.android.com/reference/android/os/Vibrator#VIBRATION_EFFECT_SUPPORT_NO) indicates that the device does not have optimized support, but still uses the platform fallback.
- [`VIBRATION_EFFECT_SUPPORT_UNKNOWN`](https://developer.android.com/reference/android/os/Vibrator#VIBRATION_EFFECT_SUPPORT_UNKNOWN) indicates the system doesn't know if the implementation is optimized or not.

As the `UNKNOWN` value indicates the checking API is unavailable, it's typically
returned for all effects or none of them. These devices fall back dynamically.

### Usage of predefined `VibrationEffect`

For details on using a predefined `VibrationEffect`, see [Use a predefined `VibrationEffect` to generate haptic feedback](https://developer.android.com/develop/ui/views/haptics/haptic-feedback#using_a_predefined_vibrationeffect).

## Envelope VibrationEffect

Envelope based vibrations allow for precise control of the vibration's amplitude
and frequency over time by defining a sequence of control points. This enables
developers to craft richer and more nuanced haptic feedback experiences. These
vibrations can be created using the [`BasicEnvelopeBuilder`](https://developer.android.com/reference/android/os/VibrationEffect.BasicEnvelopeBuilder) and
[`WaveformEnvelopeBuilder`](https://developer.android.com/reference/android/os/VibrationEffect.WaveformEnvelopeBuilder) classes.

### Compatibility and requirements

To play any vibration effects, your app must declare the `VIBRATE` permission in
the app manifest.

To check for envelope effects support, call
[`Vibrator.areEnvelopeEffectsSupported()`](https://developer.android.com/reference/android/os/Vibrator#areEnvelopeEffectsSupported()).

### Basic Envelope Builder

To create a smooth and seamless haptic experience, envelope effects must start
and end with an intensity of \\( 0.0 \\). The API enforces this by fixing the
start intensity at zero and throws an exception if the end intensity is not
zero. This constraint prevents undesirable dynamic effects in the vibrations due
to discontinuities in the amplitude that can negatively impact the user's haptic
perception.

To provide consistent envelope effect rendering across devices, the framework
requires that devices supporting this feature can handle a minimum duration of
20 ms between control points and at least 16 points for envelope effects.

### Waveform Envelope Builder

The framework doesn't modify the requested frequency and amplitude values
provided by the developer. However, the API also fixes the start amplitude at
zero to create smooth transitions.
| **Caution:** Check that the frequency specified in their envelope effects fall within the device's supported range, as defined by the device's [frequency-to-output-acceleration mapping (FOAM)](https://developer.android.com/develop/ui/views/haptics/actuators#vibrator-output-acceleration). If values exceed these limits, the device doesn't play any vibration.

To help you optimize your app's waveform envelope effects and provide
compatibility across devices, Android provides APIs for querying important
device capabilities. These methods provide information about the device's
limitations, such as the maximum and minimum transition duration between control
points and maximum number of control points supported for a single effect:

[`getMaxSize()`](https://developer.android.com/reference/android/os/vibrator/VibratorEnvelopeEffectInfo#getMaxSize())
:   Retrieves the maximum number of control points supported for an envelope
    effect.

[`getMinControlPointDurationMillis()`](https://developer.android.com/reference/android/os/vibrator/VibratorEnvelopeEffectInfo#getMinControlPointDurationMillis())
:   Retrieves the minimum duration supported, in milliseconds, between two
    control points within an envelope effect.

[`getMaxControlPointDurationMillis()`](https://developer.android.com/reference/android/os/vibrator/VibratorEnvelopeEffectInfo#getMaxControlPointDurationMillis())
:   Retrieves the maximum duration supported, in milliseconds, between two
    control points within an envelope effect.

[`getMaxDurationMillis()`](https://developer.android.com/reference/android/os/vibrator/VibratorEnvelopeEffectInfo#getMaxDurationMillis())
:   Retrieves the maximum duration supported for an envelope effect, in
    milliseconds.

If an effect exceeds the device's limitations---such as allowing too many control
points or a duration exceeding the maximum---the framework automatically adjusts
the effect to fit within the allowed boundaries. This adjustment process tries
to preserve the original intent and feel of the design as much as possible.

### Usage of Envelope VibrationEffects

For details on creating envelope waveform effects, see
[create vibration waveform with envelopes](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#vibration-waveform-with-envelopes).

## `VibrationEffect` composition

A [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect) composition is a vibration effect created using the
[`VibrationEffect.startComposition`](https://developer.android.com/reference/android/os/VibrationEffect#startComposition()) API. This API allows expressive
[rich haptics](https://developer.android.com/develop/ui/views/haptics/haptics-principles#rich_haptics) by creating a sequence of primitives with
customized delays and intensities. However, take special care to ensure that the
device supports the features being combined to avoid an inconsistent overall
experience.

### Compatibility and requirements

Playing any `VibrationEffect` requires the `VIBRATE` permission in the app
manifest.

Not all devices support all features of the composition API, and it is important
to ensure that the *primitives* are available.

#### Check for vibration primitive support

| **Caution:** If a composition contains primitives that aren't supported by the device, the entire `VibrationEffect.Composition` won't play any vibration. Therefore, to ensure a predictable experience, the set of primitives used in your app should be checked for support when considering which haptic experiences to enable.

Per-primitive support can be retrieved using the
[`Vibrator.arePrimitivesSupported`](https://developer.android.com/reference/android/os/Vibrator#arePrimitivesSupported(int...)) method. Alternatively, a set of primitives
may be checked together by using the [`Vibrator.areAllPrimitivesSupported`](https://developer.android.com/reference/android/os/Vibrator#areAllPrimitivesSupported(int...))
method - this is equivalent to `AND`-ing the per-primitive support.
| **Note:** The support for checking individual primitives is fully available starting in Android 12 (SDK 31). In Android 11, the check relies only in the ability to compose primitives, returning `TRUE` for all requested primitive IDs.

### Usage of `VibrationEffect` Compositions

For details on using `VibrationEffect` compositions, see [Create vibration compositions](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#vibration_compositions).

## On-off, one-shot, and waveform vibrations

The oldest form of vibration supported on Android is simple vibrator on-off
patterns with configurable durations. These APIs are typically not well aligned
with [Haptics design principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles) because they can generate
[buzzy haptics](https://developer.android.com/develop/ui/views/haptics/haptics-principles#buzzy_haptics); avoid them except as a last resort.

The most common use case for on-off vibrations is notifications, where, no
matter what, some vibration is desired. *Waveform vibrations* also uniquely
allow a pattern to repeat indefinitely, as you might imagine for a ringtone.

A *one-shot pattern* refers to vibrating once for N milliseconds.

There are two types of *waveform* patterns:

- **Timings-only.** This type of waveform is a description of alternating durations spent off, and durations spent on. The timings start with the duration spent off. Consequently, waveform patterns often start with a zero value to indicate to immediately start vibrating.
- **Timings and amplitudes.** This type of waveform has an additional array of amplitudes to match with each timing figure, rather than the implicit on-off of the first form. However, it's important to check that the device supports amplitude control to ensure that the intended scaling can be achieved.

### Compatibility and requirements

As on-off vibrations are the oldest form of vibrations, these are supported on
virtually all devices [with a vibrator](https://developer.android.com/develop/ui/views/haptics/haptics-apis#has_vibrator), as described later on
this page.

Playing any `VibrationEffect` or the older style `vibrate` calls, requires the
`VIBRATE` permission in the app manifest.

When using different amplitude values in a waveform, we strongly recommend that
you that the device supports *amplitude control*.

#### Check for amplitude control support

Non-zero amplitude values are rounded up to 100% on devices without amplitude
control, so it is important to check if the support is present using
[`Vibrator.hasAmplitudeControl`](https://developer.android.com/reference/android/os/Vibrator#hasAmplitudeControl()). See the [amplitude control](https://developer.android.com/develop/ui/views/haptics/haptics-apis#amplitude_control)
for more details.

You should carefully consider whether your effect has sufficient quality without
amplitude control. Falling back to an explicitly designed on-off vibration may
be better.

### Usage of on-off vibrations

In newer SDK levels, all vibration modes were consolidated into a single
expressive [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect) class, where these simple vibrations are created
using [`VibrationEffect.createOneshot`](https://developer.android.com/reference/android/os/VibrationEffect#createOneShot(long,%20int)) or [`VibrationEffect.createWaveform`](https://developer.android.com/reference/android/os/VibrationEffect#createWaveform(long%5B%5D,%20int)).

## Notification APIs

When customizing your app notifications, you can use one of the following APIs
to associate a pattern with each notification channel:

- AndroidX
  - [`NotificationChannelCompat.Builder.setVibrationPattern`](https://developer.android.com/reference/androidx/core/app/NotificationChannelCompat.Builder#setVibrationPattern(long%5B%5D))
  - [`NotificationCompat.setVibrate`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setVibrate(long%5B%5D))
- Android
  - [`NotificationChannel.setVibrationPattern`](https://developer.android.com/reference/android/app/NotificationChannel#setVibrationPattern(long%5B%5D))
  - (deprecated) [`NotificationBuilder.setVibrate`](https://developer.android.com/reference/android/app/Notification.Builder#setVibrate(long%5B%5D))

All of these forms take a basic [on-off waveform pattern](https://developer.android.com/develop/ui/views/haptics/haptics-apis#on_off_vibrations),
as described earlier, where the first entry is the delay before turning the
vibrator on.

## General concepts

Several concepts apply across the API surfaces detailed above.

### Does the device have a vibrator?

You can obtain a non-null [`Vibrator`](https://developer.android.com/reference/android/os/Vibrator) class from
`context.getSystemService(Vibrator.class)`. If the device doesn't have a
vibrator, calls to the vibration APIs don't have any effect, so apps don't need
to gate all of their haptics on a condition. However, if needed, an application
can call [`hasVibrator()`](https://developer.android.com/reference/android/os/Vibrator#hasVibrator()) to
determine if this is a real vibrator (`true`) or a stub (`false`).

### Has the user disabled touch haptics?

Some custom implementations may require manually checking whether the user has
entirely disabled Android's [**Touch feedback**](https://support.google.com/accessibility/android/answer/9078946)
setting, in which case touch feedback effects should be suppressed. This setting
can be queried using the [`HAPTIC_FEEDBACK_ENABLED`](https://developer.android.com/reference/android/provider/Settings.System#HAPTIC_FEEDBACK_ENABLED) key, where a value of zero
means disabled.

### Vibration attributes

Vibration attributes (currently in the form of [`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes)) can be
provided to help inform the system of the purpose of the vibration. This is
required when initiating a vibration when your app is in the background,
as only attentional haptics are supported for background usage.

The creation of `AudioAttributes` is covered in its class documentation, and
should be thought of as *vibration* rather than *sound*.

As a guide, in most cases, the content type is `CONTENT_TYPE_SONIFICATION`,
and the usage might be values such as `USAGE_ASSISTANCE_SONIFICATION` for
touch feedback in the foreground, or `USAGE_ALARM` for an alarm in the
background. Audio flags have no effect on vibrations.

### Amplitude control

If a vibrator has amplitude control, then it can play vibrations with varying
intensities. This is an important capability for producing
[rich haptics](https://developer.android.com/develop/ui/views/haptics/haptics-principles#rich_haptics), as well as potentially allowing user control of
default haptic intensities.

Amplitude control support can be checked by calling
[`Vibrator.hasAmplitudeControl`](https://developer.android.com/reference/android/os/Vibrator#hasAmplitudeControl()). If a vibrator does not have amplitude support,
*all amplitude values will map to off/on based on whether they are
zero/non-zero*. Consequently, applications using rich haptics with varying
amplitudes should consider disabling them if the device lacks amplitude control.

### Envelope effects support

Vibrators with envelope effects support and enable the creation of more dynamic
and nuanced vibrations, offering more precise control over intensity and
sharpness for richer haptic experiences. Use
[`Vibration.areEnvelopeEffectsSupported`](https://developer.android.com/reference/android/os/Vibrator#areEnvelopeEffectsSupported()) to determine if your device
supports this feature. If it doesn't, envelope based vibrations are ignored.