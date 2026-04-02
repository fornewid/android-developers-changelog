---
title: https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume
url: https://developer.android.com/guide/topics/large-screens/multi-window-mode-and-multi-resume
source: md.txt
---

![Tier 3 adaptive ready icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 --- Adaptive ready
| **Objective:** Make your app [adaptive ready](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_ready) by meeting the [Multi-Window:Functionality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Functionality) and [Multi-Window:Multi-Resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Multi-Resume) requirements of the [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) guidelines.

Multi-window mode enables your app to share the same screen simultaneously with
other apps for an enhanced, multitasking user experience. Apps share the screen
in split-screen mode, picture-in-picture mode, or free-form windowing mode.

Multi-resume maintains all activities in the [`RESUMED`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state when the device
is in multi-window mode, even when activities aren't focused. Multi-resume
enables activities to continue processes such as video playback while the user
interacts with other activities.

## Next steps

To learn how to enable your app to run in multi-window mode with multi-resume,
see the following developer guides:

- [Support multi-window mode: Compose](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)
- [Support multi-window mode: views](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode)