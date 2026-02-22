---
title: https://developer.android.com/guide/topics/large-screens/configuration-and-continuity
url: https://developer.android.com/guide/topics/large-screens/configuration-and-continuity
source: md.txt
---

![Tier 3 adaptive ready icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 --- Adaptive ready
| **Objective:** Make your app [adaptive ready](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_ready) by meeting the [Config:Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Changes) and [Config:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Combinations) configuration and continuity requirements of the [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) guidelines.

Configuration is a combination of device state and system state. Device state
includes screen orientation, display size, folded or unfolded state of a
foldable device, external keyboard availability, attached displays. System state
includes display modes, such as multi-window and multi-display, and user-defined
settings, such as font size and locale.

Configuration changes are device or system state changes---a rotated device,
resized app window, unfolded device, connected peripheral, or updated user
setting.

Large screen devices undergo all the same configuration changes as small screen
phones, but large screens also have unique configuration changes such as:

- Device folding and unfolding
- Resizing of free-form, desktop-type windows in multi-window mode

## Activity recreation

Android handles configuration changes for apps by destroying and recreating the
activity that's running when the configuration change occurs. Android recreates
the activity with settings and resources that accommodate the new configuration.

Design your app with responsive/adaptive layouts that support a wide variety of
screen and app window sizes and aspect ratios, and the Android framework's
configuration handling will provide the optimal presentation of your app on
large *and* small screens.

## Do-it-yourself configuration management

For special cases, such as app-specific optimizations, enable your app to handle
configuration changes rather than letting Android destroy and recreate your
app's activities.

Specify the configuration changes your app handles by setting the
[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config) attribute of the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) element in your
app manifest.

For example, enable your app to handle multi-window configuration changes:  

    <activity
      android:name=".MyActivity"
      android:configChanges="orientation|screenSize|smallestScreenSize|screenLayout" />

| **Note:** Android handles any configuration changes you don't specify in `configChanges`; that is, the system destroys and recreates your app's activities.

## State management

Whether Android handles a configuration change for you or you do it yourself,
your app must maintain context and state. After a configuration change, users
should be able to resume interaction with your app without a disruption in
continuity and without losing data, for example, when a configuration change
happens during media playback or data entry, respectively.

## Next steps

For more information about how to handle configuration changes and maintain app
continuity, see the following developer guides:

- [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)