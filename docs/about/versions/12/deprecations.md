---
title: https://developer.android.com/about/versions/12/deprecations
url: https://developer.android.com/about/versions/12/deprecations
source: md.txt
---

With each release, specific Android APIs may become obsolete or need to be
refactored to provide a better developer experience or support new platform
capabilities. In these cases, Android will officially deprecate the obsolete
APIs and direct developers to new APIs to use instead.

Deprecation means that we've ended official support for the APIs, but they will
continue to remain available to developers. This page highlights some of the
deprecations in this release of Android. To see other deprecations, refer to the
[API diff report](https://developer.android.com/sdk/api_diff/31/changes).

## RenderScript

Starting with Android 12, the RenderScript APIs are deprecated. They will
continue to function, but we expect that device and component manufacturers will
stop providing hardware acceleration support over time. To take full advantage
of GPU acceleration, we recommend [migrating away from RenderScript](https://developer.android.com/guide/topics/renderscript/migrate).

## Android playlists

Android [playlists](https://developer.android.com/reference/android/provider/MediaStore.Audio.Playlists) are
deprecated. The API is no longer maintained but the current functionality
remains for compatibility.

We recommend reading and saving playlists as [m3u](https://en.wikipedia.org/wiki/M3U)
files.

## Display API deprecations

Android devices are becoming available in many different form factors, such as
large screens, tablets, and foldables. In order to render content appropriately
for each device, your app needs to determine the screen or display size. Over
time Android provided different APIs for retrieving this information. In
Android 11 we introduced the
[`WindowMetrics`](https://developer.android.com/reference/android/view/WindowMetrics) API and deprecated
these methods:

- [`Display.getSize()`](https://developer.android.com/reference/android/view/Display#getSize(android.graphics.Point))
- [`Display.getMetrics()`](https://developer.android.com/reference/android/view/Display#getMetrics(android.util.DisplayMetrics))

In Android 12 we continue to recommend using `WindowMetrics`
and are deprecating these methods:

- [`Display.getRealSize()`](https://developer.android.com/reference/android/view/Display#getRealSize(android.graphics.Point))
- [`Display.getRealMetrics()`](https://developer.android.com/reference/android/view/Display#getRealMetrics(android.util.DisplayMetrics))

Apps should use the `WindowMetrics` APIs to query the bounds of their window, or
[`Configuration.densityDpi`](https://developer.android.com/reference/android/content/res/Configuration#densityDpi)
to query the current density.

Note that the Jetpack [`WindowManager`](https://developer.android.com/jetpack/androidx/releases/window)
library includes a [`WindowMetrics`](https://developer.android.com/reference/androidx/window/layout/WindowMetrics)
class that supports Android 4.0.1 (API level 14) and higher.

#### Examples

Here are some examples how to use `WindowMetrics`.

First, be sure your app can make its activities
[fully resizable](https://developer.android.com/guide/topics/ui/multi-window).

An activity should rely upon `WindowMetrics` from an activity context for
any UI-related work, particularly
[`WindowManager.getCurrentWindowMetrics()`](https://developer.android.com/reference/android/view/WindowManager#getCurrentWindowMetrics()).

If your app creates a `MediaProjection`, the bounds must be correctly sized
since the projection captures the display. If the app is fully resizable, the
activity context returns the correct bounds.  

### Kotlin

```kotlin
val projectionMetrics = activityContext
        .getSystemService(WindowManager::class.java).maximumWindowMetrics
```

### Java

```java
WindowMetrics projectionMetrics = activityContext
        .getSystemService(WindowManager.class).getMaximumWindowMetrics();
```

If the app is not fully resizable, it must query the bounds from a
`WindowContext` instance, and retrieve the WindowMetrics of the maximum display
area available to the application using
[`WindowManager.getMaximumWindowMetrics()`](https://developer.android.com/reference/android/view/WindowManager#getMaximumWindowMetrics())  

### Kotlin

```kotlin
val windowContext = context.createWindowContext(mContext.display!!,
      WindowManager.LayoutParams.TYPE_APPLICATION, null)
val projectionMetrics = windowContext.getSystemService(WindowManager::class.java)
      .maximumWindowMetrics
```

### Java

```java
Context windowContext = mContext.createWindowContext(mContext.getDisplay(),
      WindowManager.LayoutParams.TYPE_APPLICATION, null;
WindowMetrics projectionMetrics = windowContext.getWindowManager()
      .getMaximumWindowMetrics();
```
| **Note:** Any library that uses `MediaProjection` should follow this advice as well and query the appropriate `WindowMetrics` for the app window.