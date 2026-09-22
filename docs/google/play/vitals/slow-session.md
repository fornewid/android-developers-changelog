---
title: https://developer.android.com/google/play/vitals/slow-session
url: https://developer.android.com/google/play/vitals/slow-session
source: md.txt
---

In Android vitals, a slow session is a session in which more than 25% of the
frames are slow. A frame is slow if it is not presented less than 50ms after the
previous frame (equivalent to 20 FPS). Android vitals also reports a second Slow
Sessions metric with a target of 34ms (equivalent to 30 FPS). Using Slow
Sessions, you can understand the frame-rate performance of your game, which
impacts how smooth and fluid your game feels to users.

In due course, Play will start steering users away from games that cannot
achieve 20 FPS on their phones. Note that Android vitals only begins monitoring
frame rate after your game has been running for one minute.

Visit our [Help Center](https://support.google.com/googleplay/android-developer/answer/9844486#slow_frames&zippy=%2Cslow-session-rate-fps-or-fps-games-only%2Cexcessive-slow-frames-apps-only) for more details
about the metric.
![Pie chart-like graphics that show the number of slow frames and non-slow frames.](https://developer.android.com/static/google/play/vitals/images/slow-session.png) **Figure 1.** A slow session in Android vitals.

> [!NOTE]
> **Note:** The Slow Sessions metric is computed with data collected from [SurfaceFlinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager#surfaceflinger). More concretely, the frame rate of a session is estimated based on the time in between frames drawn on surfaces owned by the app. The estimated frame rate includes frames rendered by OpenGL, Vulkan, as well as Android UI toolkit. This metric is available only for games. If your apps use the `View`-based UI toolkit, where the user-visible portion of the app is drawn from [`Canvas`](https://developer.android.com/reference/android/graphics/Canvas) or the `View` hierarchy, refer to [Slow Rendering](https://developer.android.com/google/play/vitals/render).

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Slow Sessions (games only)](https://developer.android.com/topic/performance/issues/slow-session).