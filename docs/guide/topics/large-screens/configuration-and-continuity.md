---
title: Configuration and continuity  |  Large screens  |  Android Developers
url: https://developer.android.com/guide/topics/large-screens/configuration-and-continuity
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Large screens](https://developer.android.com/guide/topics/large-screens)
* [Guides](https://developer.android.com/guide/topics/large-screens/tier-3-overview)

# Configuration and continuity Stay organized with collections Save and categorize content based on your preferences.




![Tier 3 adaptive ready icon](/static/images/docs/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 — Adaptive ready

**Objective:** Make your app [adaptive ready](/docs/quality-guidelines/adaptive-app-quality/tier-3) by meeting the
[Config\_Changes](/docs/quality-guidelines/adaptive-app-quality/tier-3#Config_Changes) and [Config\_Combinations](/docs/quality-guidelines/adaptive-app-quality/tier-3#Config_Combinations) configuration and continuity
requirements of the [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality).

Configuration is a combination of device state and system state. Device state
includes screen orientation, display size, folded or unfolded state of a
foldable device, external keyboard availability, attached displays. System state
includes display modes, such as multi-window and multi-display, and user-defined
settings, such as font size and locale.

Configuration changes are device or system state changes—a rotated device,
resized app window, unfolded device, connected peripheral, or updated user
setting.

Large screen devices undergo all the same configuration changes as small screen
phones, but large screens also have unique configuration changes such as:

* Device folding and unfolding
* Resizing of free-form, desktop-type windows in multi-window mode

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
[`android:configChanges`](/guide/topics/manifest/activity-element#config) attribute of the [`<activity>`](/guide/topics/manifest/activity-element) element in your
app manifest.

For example, enable your app to handle multi-window configuration changes:

```
<activity
  android:name=".MyActivity"
  android:configChanges="orientation|screenSize|smallestScreenSize|screenLayout" />
```

**Note:** Android handles any configuration changes you don't specify in
`configChanges`; that is, the system destroys and recreates your app's
activities.

## State management

Whether Android handles a configuration change for you or you do it yourself,
your app must maintain context and state. After a configuration change, users
should be able to resume interaction with your app without a disruption in
continuity and without losing data, for example, when a configuration change
happens during media playback or data entry, respectively.

## Next steps

For more information about how to handle configuration changes and maintain app
continuity, see the following developer guides:

* [Handle configuration changes](/guide/topics/resources/runtime-changes)
* [Save UI states](/topic/libraries/architecture/saving-states)