---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/input
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/input
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Users interact with audio glasses and display glasses in different ways, such as
the following:

- Asking a question using their voice.
- Gesturing on the touchpad (for example, tapping or swiping back, forward, up, and down)
- Pressing a button on the side of their device.

Android XR has built-in support for some of these use cases, while others
require you to customize or extend the system's default behavior or implement
certain APIs.

Regardless of whether a user has audio glasses or display glasses, their voice
is their primary way to interact with their device.

This guide covers the following ways of handling input:

- How to [handle physical input](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/physical-input).
- How to [handle audio input using automatic speech recognition](https://developer.android.com/develop/xr/jetpack-xr-sdk/asr).

This guide assumes you're familiar with the following concepts:

- [Requesting hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions)
- [Android activities](https://developer.android.com/guide/components/activities/intro-activities)
- [The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)
- [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)