---
title: https://developer.android.com/about/versions/14/features/screenshot-detection
url: https://developer.android.com/about/versions/14/features/screenshot-detection
source: md.txt
---

![Message reads 'Pay app detected this screenshot'](https://developer.android.com/static/about/versions/14/images/screenshot-detection.svg) **Figure 1.** An example of the system-provided toast message that appears when the user takes a screenshot of an app that supports the screenshot detection API.

To create a more-standardized experience for detecting screenshots,
Android 14 introduces a privacy-preserving screenshot detection
API. This API lets apps register callbacks on a per-activity basis. These
callbacks are invoked, and the user is notified, when the user takes a
screenshot while that activity is visible.

> [!NOTE]
> **Note:** The callback doesn't provide an image of the actual screenshot. It's up to your app to determine what appeared on the screen when the user took a screenshot.

## Supported use cases

In Android 14, the system API only detects a screenshot if the user performs a
specific combination of hardware button presses. The API doesn't detect
screenshots that are taken when running test commands related to screenshots,
including [ADB](https://developer.android.com/studio/command-line/adb), or within instrumentation tests that [capture the device's
current screen contents](https://developer.android.com/reference/androidx/test/core/app/DeviceCapture).

## Implementation steps

To add screenshot detection, declare the new [`DETECT_SCREEN_CAPTURE`](https://developer.android.com/reference/android/Manifest.permission#DETECT_SCREEN_CAPTURE)
install-time permission:

    <uses-permission android:name="android.permission.DETECT_SCREEN_CAPTURE" />

Then, complete these steps for each activity in your app where users might
capture screenshots:

1. Implement a callback by overriding the `onScreenCapture()` function. In this
   callback, your app can take action, such as warning another user that
   someone took a screenshot of a messaging conversation.

   ### Kotlin

   ```kotlin
   val screenCaptureCallback = Activity.ScreenCaptureCallback {
       // Add logic to take action in your app.
   }
   ```

   ### Java

   ```java
   final Activity.ScreenCaptureCallback screenCaptureCallback =
       new Activity.ScreenCaptureCallback() {
           @Override
           public void onScreenCaptured() {
               // Add logic to take action in your app.
           }
       };
   ```
2. In the activity's `onStart()` method, register the screenshot callback.

   > [!NOTE]
   > **Note:** Given that a notice is shown with every screenshot detection signal, developers should provide in-context notices to the user when they are starting an activity that uses screenshot detection APIs so the system notice does not come as a surprise to users.

   ### Kotlin

   ```kotlin
   override fun onStart() {
       super.onStart()
       // Pass in the callback created in the previous step 
       // and the intended callback executor (e.g. Activity's mainExecutor).
       registerScreenCaptureCallback(mainExecutor, screenCaptureCallback)
   }
   ```

   ### Java

   ```java
   @Override
   protected void onStart() {
       super.onStart();
       // Pass in the callback created in the previous step 
       // and the intended callback executor (e.g. Activity's mainExecutor).
       registerScreenCaptureCallback(executor, screenCaptureCallback);
   }
   ```
3. In the activity's `onStop()` method, unregister the screenshot callback:

   ### Kotlin

   ```kotlin
   override fun onStop() {
       super.onStop()
       unregisterScreenCaptureCallback(screenCaptureCallback)
   }
   ```

   ### Java

   ```java
   @Override
   protected void onStop() {
       super.onStop();
       unregisterScreenCaptureCallback(screenCaptureCallback);
   }
   ```

## Control ability to capture screenshots

If you don't want the contents of an app's activity to appear in screenshots, or
on non-secure displays, set the [`FLAG_SECURE`](https://developer.android.com/reference/android/view/Display#FLAG_SECURE) display flag.

> [!NOTE]
> **Note:** To provide transparency and user control, consider adding a setting in your app that allows users to toggle this flag.

### Kotlin

```kotlin
activity.getWindow().setFlags(LayoutParams.FLAG_SECURE, LayoutParams.FLAG_SECURE)
```

### Java

```java
activity.getWindow().setFlags(LayoutParams.FLAG_SECURE, LayoutParams.FLAG_SECURE);
```