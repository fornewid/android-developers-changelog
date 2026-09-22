---
title: https://developer.android.com/google/play/vitals/render
url: https://developer.android.com/google/play/vitals/render
source: md.txt
---

UI rendering is the act of generating a frame from your app and displaying it on
the screen. To help ensure that a user's interaction with your app is smooth,
your app must render frames in under 16ms to achieve 60 frames per second (fps).
If your app suffers from slow UI rendering, then the system is forced to skip
frames and the user perceives stuttering in your app. This is called *jank*.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Slow rendering](https://developer.android.com/topic/performance/issues/render).

## Android vitals metrics

To help improve app quality, Android automatically monitors your app for jank
and frozen frames and displays the information in the Android vitals dashboard.
For information about how the data is collected, see [Monitor your app's
technical quality with Android
vitals](https://support.google.com/googleplay/android-developer/answer/7385505).

- **Slow frames:** UI frames that take longer than 16ms to render.
- **Frozen frames:** UI frames that take longer than 700ms to render. This is a problem because your app appears to be stuck and is unresponsive to user input for almost a full second while the frame is rendering. During app startup or while transitioning to a different screen, it's normal for the initial frame to take longer than 16ms to draw because your app must inflate views, lay out the screen, and perform the initial draw all from scratch. That's why Android tracks frozen frames separately from slow rendering. No frames in your app should ever take longer than 700ms to render.

> [!NOTE]
> **Note:** The Android vitals dashboard and Android system keep track of render time and frozen frame statistics for apps that use the `View`-based UI toolkit, where the user-visible portion of the app is drawn from [`Canvas`](https://developer.android.com/reference/android/graphics/Canvas) or the [`View`](https://developer.android.com/reference/android/view/View) hierarchy. If your app doesn't use the `View`-based UI toolkit, as is the case for apps that are built with [Vulkan](https://developer.android.com/ndk/guides/graphics), [Unity](https://unity3d.com/), [Unreal](https://www.unrealengine.com), or [OpenGL](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl), then render time and frozen frame statistics aren't available in the Android vitals dashboard. To determine if your device is logging render time metrics for your app, run `adb shell dumpsys gfxinfo <package name>`.