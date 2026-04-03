---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive
url: https://developer.android.com/develop/ui/compose/layouts/adaptive
source: md.txt
---

Android apps run on a wide variety of devices---from foldable flip phones to
wall‑mounted TVs. To provide a great user experience on all types of
devices, adapt your app's UI to different display sizes and configurations. The
best Android apps make the most of the screen space they occupy and handle
changes to that space at runtime, including orientation changes and window
resizing in split‑screen and desktop windowing modes.
| **Note:** For apps that target Android 16 (API level 36), the system ignores screen orientation, aspect ratio, and app resizablility restrictions to improve the layout of apps on form factors with smallest width \>= 600dp. See [App
| orientation, aspect ratio, and
| resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).

## Topics

The adaptive layouts documentation provides guidance on how to:

- Design and implement adaptive layouts
- Adjust your app's primary navigation based on window size
- Use window size classes to adapt your app's UI
- Simplify implementation of canonical layouts, such as list‑detail, using the Jetpack APIs

## Prerequisites

The adaptive layouts guidance assumes you understand the following concepts:

- [Jetpack Compose basics](https://developer.android.com/develop/ui/compose/mental-model), including recomposition