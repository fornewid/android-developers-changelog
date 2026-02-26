---
title: https://developer.android.com/develop/ui/views/haptics
url: https://developer.android.com/develop/ui/views/haptics
source: md.txt
---

Haptics is everything you feel through the sense of touch. Modern Android
devices often incorporate a vibration actuator to allow devices to stimulate the
user's sense of touch. These motors have advanced significantly from the
original loud buzzy vibration produced by early devices, and Android apps can
now take advantage of capabilities to give users a richer experience with
subtlety and depth.

The following pages cover everything about vibration, from basic haptic feedback
to increasingly more complex vibration waveforms and effect compositions.

[Haptics design principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles)
:   The page describes the classifications supported by Android haptics and
    guidelines for designing them.

[Add haptic feedback to events](https://developer.android.com/develop/ui/views/haptics/haptic-feedback)
:   The page presents code examples for different ways of providing haptic
    feedback to user interactions.

[Vibration actuators primer](https://developer.android.com/develop/ui/views/haptics/actuators)
:   The page provides an overview of how vibration actuators work, which is
    important prerequisite knowledge for creating custom haptics.

[Create custom haptic effects](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects)
:   This page provides several examples of using different haptics APIs to
    create custom effects in an Android application.

[Add haptics APIs](https://developer.android.com/develop/ui/views/haptics/haptics-apis)
:   The page is a reference for various haptics APIs available on Android, and
    also covers when and how to check for any device support necessary to ensure
    your Haptic effects play as intended.

Also, be sure to read the
[best practices for accessibility](https://developer.android.com/guide/topics/ui/accessibility).

## Samples

The following samples are available in the [Haptic Sampler app](https://github.com/android/platform-samples/tree/main/samples/user-interface/haptics) on
GitHub. You can also find documentation for each here.

- [Resist (with low ticks)](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#resist)
- [Expand (with rise and fall)](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#expand)
- [Wobble (with spins)](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#wobble)
- [Bounce (with thuds)](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#bounce)

This documentation also includes code examples for the following custom vibration patterns:

- [Ramp-up pattern](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#ramp_up_pattern)
- [Repeating pattern](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#repeating_pattern)
- [Pattern with fallback](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#pattern_with_fallback)

## Video