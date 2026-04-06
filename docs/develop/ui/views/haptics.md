---
title: Implement haptics on Android  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/haptics
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Implement haptics on Android Stay organized with collections Save and categorize content based on your preferences.




Haptics is everything you feel through the sense of touch. Modern Android
devices often incorporate a vibration actuator to allow devices to stimulate the
user's sense of touch. These motors have advanced significantly from the
original loud buzzy vibration produced by early devices, and Android apps can
now take advantage of capabilities to give users a richer experience with
subtlety and depth.

The following pages cover everything about vibration, from basic haptic feedback
to increasingly more complex vibration waveforms and effect compositions.

[Haptics design principles](/develop/ui/views/haptics/haptics-principles)
:   The page describes the classifications supported by Android haptics and
    guidelines for designing them.

[Add haptic feedback to events](/develop/ui/views/haptics/haptic-feedback)
:   The page presents code examples for different ways of providing haptic
    feedback to user interactions.

[Vibration actuators primer](/develop/ui/views/haptics/actuators)
:   The page provides an overview of how vibration actuators work, which is
    important prerequisite knowledge for creating custom haptics.

[Create custom haptic effects](/develop/ui/views/haptics/custom-haptic-effects)
:   This page provides several examples of using different haptics APIs to
    create custom effects in an Android application.

[Add haptics APIs](/develop/ui/views/haptics/haptics-apis)
:   The page is a reference for various haptics APIs available on Android, and
    also covers when and how to check for any device support necessary to ensure
    your Haptic effects play as intended.

Also, be sure to read the
[best practices for accessibility](/guide/topics/ui/accessibility).

## Samples

The following samples are available in the [Haptic Sampler app](https://github.com/android/platform-samples/tree/main/samples/user-interface/haptics) on
GitHub. You can also find documentation for each here.

* [Resist (with low ticks)](/develop/ui/views/haptics/custom-haptic-effects#resist)
* [Expand (with rise and fall)](/develop/ui/views/haptics/custom-haptic-effects#expand)
* [Wobble (with spins)](/develop/ui/views/haptics/custom-haptic-effects#wobble)
* [Bounce (with thuds)](/develop/ui/views/haptics/custom-haptic-effects#bounce)

This documentation also includes code examples for the following custom vibration patterns:

* [Ramp-up pattern](/develop/ui/views/haptics/custom-haptic-effects#ramp_up_pattern)
* [Repeating pattern](/develop/ui/views/haptics/custom-haptic-effects#repeating_pattern)
* [Pattern with fallback](/develop/ui/views/haptics/custom-haptic-effects#pattern_with_fallback)

## Video