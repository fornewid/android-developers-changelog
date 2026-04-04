---
title: Multi-window mode and multi-resume  |  Large screens  |  Android Developers
url: https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Large screens](https://developer.android.com/guide/topics/large-screens)
* [Guides](https://developer.android.com/guide/topics/large-screens/tier-3-overview)

# Multi-window mode and multi-resume Stay organized with collections Save and categorize content based on your preferences.



![Tier 3 adaptive ready icon](/static/images/docs/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 — Adaptive ready

**Objective:** Make your app [adaptive ready](/docs/quality-guidelines/adaptive-app-quality/tier-3) by meeting the
[Multi-Window\_Functionality](/docs/quality-guidelines/adaptive-app-quality/tier-3#Multi-Window_Functionality) and [Multi-Resume](/docs/quality-guidelines/adaptive-app-quality/tier-3#Multi-Resume) requirements of
the [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality).

Multi-window mode enables your app to share the same screen simultaneously with
other apps for an enhanced, multitasking user experience. Apps share the screen
in split-screen mode, picture-in-picture mode, or free-form windowing mode.

Multi-resume maintains all activities in the [`RESUMED`](/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state when the device
is in multi-window mode, even when activities aren't focused. Multi-resume
enables activities to continue processes such as video playback while the user
interacts with other activities.

## Next steps

To learn how to enable your app to run in multi-window mode with multi-resume,
see the following developer guides:

* [Support multi-window mode: Compose](/develop/ui/compose/layouts/adaptive/support-multi-window-mode)
* [Support multi-window mode: views](/develop/ui/views/layout/support-multi-window-mode)