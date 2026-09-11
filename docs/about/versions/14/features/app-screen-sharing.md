---
title: https://developer.android.com/about/versions/14/features/app-screen-sharing
url: https://developer.android.com/about/versions/14/features/app-screen-sharing
source: md.txt
---

Media projection on Android enables users to share their device display with other users. On Android 14 QPR2, users can share or record an app window rather than the entire device screen.

App screen sharing increases privacy, improves user productivity, and enhances multitasking by enabling users to run multiple apps but restrict content sharing to a single app.

With app screen sharing, the status bar, navigation bar, notifications, and other system UI elements are excluded from the shared display. Only the content of the selected app is shared.

Apps that use the [`MediaProjection`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection) APIs are capable of app screen sharing automatically. However, test your app to ensure app screen sharing works as intended.

### `MediaProjection` callbacks

Android 14 (API level 34) added the following media projection callback methods which enable you to customize app screen sharing:

- [**`MediaProjection.Callback#onCapturedContentResize()`**](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#oncapturedcontentresize)

  Enables resizing of the shared projection based on the size of the captured display area.
- [**`MediaProjection.Callback#onCapturedContentVisibilityChanged()`**](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#oncapturedcontentvisibilitychanged)

  Informs the shared projection host app of the visibility of the capture content. The host app can show or hide the captured content on the output surface based on whether the captured region is visible to the user. For example, in multi‑window mode, if another app completely covers the shared app, the host can hide the shared app on the output surface.

Use the new methods to enhance the app screen sharing user experience.