---
title: https://developer.android.com/media/grow/media-projection
url: https://developer.android.com/media/grow/media-projection
source: md.txt
---

# Media projection

The[`android.media.projection`](https://developer.android.com/reference/kotlin/android/media/projection/package-summary)APIs introduced in Android 5 (API level 21) enable you to capture the contents of a device display as a media stream that you can play back, record, or cast to other devices, such as TVs.

Android 14 (API level 34) introduces app screen sharing, which enables users to share a single app window instead of the entire device screen regardless of windowing mode. App screen sharing excludes the status bar, navigation bar, notifications, and other system UI elements from the shared display---even when app screen sharing is used to capture an app in full screen. Only the contents of the selected app are shared.

App screen sharing ensures user privacy, increases user productivity, and enhances multitasking by enabling users to run multiple apps but restrict content sharing to just a single app.

## Three display representations

A media projection captures the contents of a device display or app window and then projects the captured image to a virtual display that renders the image on a[`Surface`](https://developer.android.com/reference/kotlin/android/view/Surface).
![Real device display projected onto virtual display. Contents of virtual display written to application-provided `Surface`.](https://developer.android.com/static/media/images/grow/media-projection.png)**Figure 1.** Real device screen or app window projected onto virtual display. Virtual display written to application-provided`Surface`.

The application provides the`Surface`by means of a[`MediaRecorder`](https://developer.android.com/reference/kotlin/android/media/MediaRecorder),[`SurfaceTexture`](https://developer.android.com/reference/kotlin/android/graphics/SurfaceTexture), or[`ImageReader`](https://developer.android.com/reference/kotlin/android/media/ImageReader), which consumes the contents of the captured display and enables you to manage images rendered on the`Surface`in real time. You can save the images as a recording or cast them to a TV or other device.

### Real display

Begin a media projection session by obtaining a token that grants your app the ability to capture the contents of the device display or app window. The token is represented by an instance of the[`MediaProjection`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection)class.

Use the[`getMediaProjection()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager#getmediaprojection)method of the[`MediaProjectionManager`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager)system service to create a`MediaProjection`instance when you start a new activity. Start the activity with an intent from the[`createScreenCaptureIntent()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager#createscreencaptureintent)method to specify a screen capture operation:  

### Kotlin

<br />

```kotlin
val mediaProjectionManager = getSystemService(MediaProjectionManager::class.java)
var mediaProjection : MediaProjection

val startMediaProjection = registerForActivityResult(
    StartActivityForResult()
) { result ->
    if (result.resultCode == RESULT_OK) {
        mediaProjection = mediaProjectionManager
            .getMediaProjection(result.resultCode, result.data!!)
    }
}

startMediaProjection.launch(mediaProjectionManager.createScreenCaptureIntent())
```

<br />

### Java

<br />

```java
final MediaProjectionManager mediaProjectionManager =
    getSystemService(MediaProjectionManager.class);
final MediaProjection[] mediaProjection = new MediaProjection[1];

ActivityResultLauncher startMediaProjection = registerForActivityResult(
    new StartActivityForResult(),
    result -> {
        if (result.getResultCode() == Activity.RESULT_OK) {
            mediaProjection[0] = mediaProjectionManager
                .getMediaProjection(result.getResultCode(), result.getData());
        }
    }
);

startMediaProjection.launch(mediaProjectionManager.createScreenCaptureIntent());
```

<br />

| **Note:** Apps that use the[`android.media.projection`](https://developer.android.com/reference/kotlin/android/media/projection/package-summary)APIs are capable of app screen sharing automatically through the call to`createScreenCaptureIntent()`.

### Virtual display

The centerpiece of a media projection is the virtual display, which you create by calling[`createVirtualDisplay()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection#createvirtualdisplay)on a`MediaProjection`instance:  

### Kotlin

<br />

```kotlin
virtualDisplay = mediaProjection.createVirtualDisplay(
                     "ScreenCapture",
                     width,
                     height,
                     screenDensity,
                     DisplayManager.VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR,
                     surface,
                     null, null)
```

<br />

### Java

<br />

```java
virtualDisplay = mediaProjection.createVirtualDisplay(
                     "ScreenCapture",
                     width,
                     height,
                     screenDensity,
                     DisplayManager.VIRTUAL_DISPLAY_FLAG_AUTO_MIRROR,
                     surface,
                     null, null);
```

<br />

The`width`and`height`parameters specify the dimensions of the virtual display. To obtain values for width and height, use the[`WindowMetrics`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics)APIs introduced in Android 11 (API level 30). (For details, see the[Media projection size](https://developer.android.com/media/grow/media-projection#media_projection_size)section.)
| **Note:** The screen density parameter of the`createVirtualDisplay()`method enables adjustment of the resolution of the captured display for sharing or casting to a lower resolution external display. Use[`Configuration#densityDpi`](https://developer.android.com/reference/kotlin/android/content/res/Configuration#densitydpi)rather than[`Display#getRealMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealmetrics)(which is deprecated) to obtain the value for the screen density argument.

### Surface

Size the media projection surface to produce output in the appropriate resolution. Make the surface large (low resolution) for screen casting to TVs or computer monitors and small (high resolution) for device display recording.

As of Android 12L (API level 32), when rendering captured content on the surface, the system scales the content uniformly, maintaining the aspect ratio, so that both dimensions of the content (width and height) are equal to or less than the corresponding dimensions of the surface. The captured content is then centered on the surface.

The Android 12L scaling approach improves screen casting to televisions and other large displays by maximizing the size of the surface image while ensuring the proper aspect ratio.

## Foreground service permission

If your app targets Android 14 or higher, the app manifest must include a permission declaration for the[`mediaProjection`](https://developer.android.com/about/versions/14/changes/fgs-types-required#media-projection)foreground service type:  

    <manifest ...>
        <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
        <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" />
        <application ...>
            <service
                android:name=".MyMediaProjectionService"
                android:foregroundServiceType="mediaProjection"
                android:exported="false">
            </service>
        </application>
    </manifest>

Start the media projection service with a call to[`startForeground()`](https://developer.android.com/reference/kotlin/androidx/core/app/ServiceCompat#startForeground(android.app.Service,int,android.app.Notification,int)).

If you don't specify the foreground service type in the call, the type defaults to a bitwise integer of the foreground service types defined in the manifest. If the manifest doesn't specify any service types, the system throws[`MissingForegroundServiceTypeException`](https://developer.android.com/reference/kotlin/android/app/MissingForegroundServiceTypeException).

## User consent

Your app must request user consent before each media projection session. A session is a single call to`createVirtualDisplay()`. A`MediaProjection`token must be used only once to make the call.

On Android 14 or higher, the`createVirtualDisplay()`method throws a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)if your app does either of the following:

- Passes an`Intent`instance returned from`createScreenCaptureIntent()`to`getMediaProjection()`more than once
- Calls`createVirtualDisplay()`more than once on the same`MediaProjection`instance

## Media projection size

A media projection can capture the entire device display or an app window regardless of windowing mode.

### Initial size

With full-screen media projection, your app must determine the size of the device screen. In app screen sharing, your app won't be able to determine the size of the captured display until the user has selected the capture region. So, the initial size of any media projection is the size of the device screen.

Use the platform`WindowManager`[`getMaximumWindowMetrics()`](https://developer.android.com/reference/kotlin/android/view/WindowManager#getmaximumwindowmetrics)method to return a[`WindowMetrics`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics)object for the device screen even if the media projection host app is in multi‑window mode, occupying only part of the display.

For compatibility down to API level 14, use the`WindowMetricsCalculator`[`computeMaximumWindowMetrics()`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetricsCalculator#computeMaximumWindowMetrics(android.app.Activity))method from the Jetpack`WindowManager`library.

Call the`WindowMetrics`[`getBounds()`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics#getbounds)method to get the width and height of the device display.

### Size changes

The size of the media projection can change when the device is rotated or the user selects an app window as the capture region in app screen sharing. The media projection might be letterboxed if the captured content is a different size than the maximum window metrics obtained when the media projection was set up.

To ensure the media projection precisely aligns with the size of the captured content for any captured region and across device rotations, use the`onCapturedContentResize()`callback to resize the capture. (For more information, see the[Customization](https://developer.android.com/media/grow/media-projection#customization)section, which follows).

## Customization

Your app can customize the media projection user experience with the following[`MediaProjection.Callback`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback)APIs:

- [`onCapturedContentVisibilityChanged()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#oncapturedcontentvisibilitychanged): Enables the host app (the app that started the media projection) to show or hide the shared content.

  Use this callback to customize your app's UI based on whether the captured region is visible to the user. For example, if your app is visible to the user and is displaying the captured content within the app's UI, and the captured app is also visible to the user (as indicated through this callback), the user sees the same content twice. Use the callback to update your app's UI to hide the captured content and free up layout space in your app for other content.
- [`onCapturedContentResize()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#oncapturedcontentresize): Enables the host app to change the size of the media projection on the virtual display and media projection`Surface`based on the size of the captured display region.

  Triggered whenever the captured content---a single app window or full device display---changes size (because of device rotation or the captured app entering a different windowing mode). Use this API to resize both the virtual display and surface to ensure the aspect ratio matches the captured content and the capture is not letterboxed.

## Resource recovery

Your app should register the`MediaProjection`[`onStop()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#onstop)callback to be informed when the media projection session is stopped and becomes invalid. When the session is stopped, your app should release the resources that it holds, such as the virtual display and projection surface. A stopped media projection session can no longer create a new virtual display, even if your app has not previously created a virtual display for that media projection.

The system invokes the callback when the media projection terminates. This termination can happen for several reasons, such as:

- the user stops the session using the app's UI or the system's[media projection status bar chip](https://developer.android.com/media/grow/media-projection#status_bar_chip_auto_stop)
- the screen is being locked
- another media projection session starts
- the app process is killed

If your app doesn't register the callback, any call to`createVirtualDisplay()`throws[`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException).

## Opt out

Android 14 or higher enables app screen sharing by default. Each media projection session gives users the option of sharing an app window or the entire display.

Your app can opt out of app screen sharing by calling the[`createScreenCaptureIntent(MediaProjectionConfig)`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager#createscreencaptureintent_1)method with a[`MediaProjectionConfig`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionConfig)argument returned from a call to[`createConfigForDefaultDisplay()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionConfig#createconfigfordefaultdisplay).

A call to`createScreenCaptureIntent(MediaProjectionConfig)`with a`MediaProjectionConfig`argument returned from a call to[`createConfigForUserChoice()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionConfig#createconfigforuserchoice)is the same as the default behavior, that is, a call to[`createScreenCaptureIntent()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager#createscreencaptureintent).
| **Warning:** Device manufacturers can override your app's opt out of app screen sharing if the app misuses the opt out to show private user data from an app window that shouldn't be shared. See[Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode#override_disable_media_projection_single_app_option).

## Resizable apps

Always make your media projection apps resizable ([`resizeableActivity="true"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity)). Resizable apps support device configuration changes and multi‑window mode (see[Multi-window support](https://developer.android.com/guide/topics/ui/multi-window)).

If your app is not resizable, it must query the display bounds from a window context and use`getMaximumWindowMetrics()`to retrieve the`WindowMetrics`of the maximum display area available to the app :  

### Kotlin

<br />

```kotlin
val windowContext = context.createWindowContext(context.display!!,
      WindowManager.LayoutParams.TYPE_APPLICATION, null)
val projectionMetrics = windowContext.getSystemService(WindowManager::class.java)
      .maximumWindowMetrics
```

<br />

### Java

<br />

```java
Context windowContext = context.createWindowContext(context.getDisplay(),
      WindowManager.LayoutParams.TYPE_APPLICATION, null);
WindowMetrics projectionMetrics = windowContext.getSystemService(WindowManager.class)
      .getMaximumWindowMetrics();
```

<br />

| **Caution:** [`Display#getRealSize()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealsize)and[`Display#getRealMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealmetrics)are deprecated as of API level 31. For non-resizable apps (`resizeableActivity="false"`), the methods return the bounds of the app window rather than the bounds of the device display.

## Status bar chip and auto stop

Screen projection exploits expose private user data such as financial information because users don't realize their device screen is being shared.

For apps running on devices with Android 15 QPR1 or higher, a status bar chip that is large and prominent alerts users to any in‑progress screen projection. Users can tap the chip to stop their screen from being shared, cast, or recorded. Also, screen projection automatically stops when the device screen is locked.
![](https://developer.android.com/static/media/images/grow/media_projection_status_bar_chip.png)**Figure 2.**Status bar chip for screen sharing, casting, and recording.

Test the availability of the media projection status bar chip by starting screen sharing, casting, or recording. The chip should appear in the status bar.

To ensure your app releases resources and updates its UI when screen projection is stopped by user interaction with the status bar chip or by lock screen activation, do the following:

- Create an instance of[`MediaProjection.Callback`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback).

- Implement the callback[`onStop()`](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjection.Callback#onstop)method. The method is called when screen projection stops. Release any resources your app is holding and update the app UI as needed.

To test the callback, tap the status bar chip or lock the device screen to stop screen projection. Verify that the`onStop()`method is called and your app responds as intended.

## Additional resources

For more information about media projection, see[Capture video and audio playback](https://developer.android.com/guide/topics/media/av-capture).