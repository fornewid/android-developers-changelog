---
title: https://developer.android.com/about/versions/12/behavior-changes-all
url: https://developer.android.com/about/versions/12/behavior-changes-all
source: md.txt
---

The Android 12 platform includes behavior changes that may
affect your app. The following behavior changes apply to *all apps* when they
run on Android 12, regardless of `targetSdkVersion`. You should
test your app and then modify it as needed to support these properly, where
applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 12](https://developer.android.com/about/versions/12/behavior-changes-12).

## User experience

### Stretch overscroll effect

On devices running Android 12 and higher, the visual behavior for [overscroll
events](https://developer.android.com/training/gestures/scroll#term) changes.

On Android 11 and lower, an overscroll event causes the visual elements to have
a glow; on Android 12 and higher, the visual elements stretch and bounce back on
a drag event and they fling and bounce back on a fling event.

For more information, see the guide to [animating scroll
gestures](https://developer.android.com/training/gestures/scroll).

### App splash screens

If you have previously implemented a custom splash screen in Android 11 or
lower, you'll need to migrate your app to the `SplashScreen` API to ensure that
it displays correctly starting in Android 12. Not migrating your app will result
in a degraded or unintended app launch experience.

For instructions, see [Migrate your existing splash screen
implementation to Android 12](https://developer.android.com/guide/topics/ui/splash-screen/migrate).

Additionally, starting in Android 12, the system always applies the new [Android
system default splash screen](https://developer.android.com/about/versions/12/features/splash-screen) on
[cold](https://developer.android.com/topic/performance/vitals/launch-time#cold) and
[warm starts](https://developer.android.com/topic/performance/vitals/launch-time#warm) for all apps.
By default, this system default splash screen is constructed using your app's
launcher icon element and the
[`windowBackground`](https://developer.android.com/topic/performance/vitals/launch-time#solutions-3) of your
theme (if it's a single color).

For more details, see the [splash screens developer guide](https://developer.android.com/guide/topics/ui/splash-screen).

### Web intent resolution

Starting in Android 12 (API level 31), a generic web intent resolves to an
activity in your app only if your app is approved for the specific domain
contained in that web intent. If your app isn't approved for the domain, the
web intent resolves to the user's default browser app instead.

Apps can get this approval by doing one of the following:

- Verify the domain using [Android App
  Links](https://developer.android.com/training/app-links/verify-android-applinks).

  On apps that target Android 12 or higher, the system
  changes how it [automatically
  verifies](https://developer.android.com/training/app-links/verify-android-applinks#auto-verification)
  your app's Android App Links. In your app's [intent
  filters](https://developer.android.com/training/app-links/verify-android-applinks#add-intent-filters),
  check that you include the `BROWSABLE` category and support the `https`
  scheme.

  On Android 12 or higher, you
  can [manually
  verify](https://developer.android.com/training/app-links/verify-android-applinks#manual-verification)
  your app's Android App Links, to test how this updated logic affects your
  app.
- [Request the user to associate your app with the
  domain](https://developer.android.com/training/app-links/verify-android-applinks#request-user-associate-app-with-domain)
  in system settings.

If your app invokes web intents, consider adding a prompt or dialog that asks
the user to confirm the action.

### Immersive mode improvements for gesture navigation

Android 12 consolidates existing behavior to make it easier for users to
[perform gesture navigation commands while in immersive
mode](https://developer.android.com/training/system-ui/immersive#immersive-consolidated-behavior). In
addition, Android 12 provides [backward compatibility behavior for sticky
immersive
mode](https://developer.android.com/training/system-ui/immersive#sticky-immersive-compat-android11-lower).

### Display#getRealSize and getRealMetrics: deprecation and constraints

Android devices are available in many different form factors, such as large
screens, tablets, and foldables. To render content appropriately for each
device, your app needs to determine the screen or display size. Over time,
Android has provided different APIs for retrieving this information. In Android
11, we introduced the [`WindowMetrics`](https://developer.android.com/reference/android/view/WindowMetrics)
API and deprecated these methods:

- [`Display.getSize()`](https://developer.android.com/reference/android/view/Display#getSize(android.graphics.Point))
- [`Display.getMetrics()`](https://developer.android.com/reference/android/view/Display#getMetrics(android.util.DisplayMetrics))

In Android 12 we're continuing to recommend using `WindowMetrics`, and are
deprecating these methods:

- [`Display.getRealSize()`](https://developer.android.com/reference/android/view/Display#getRealSize(android.graphics.Point))
- [`Display.getRealMetrics()`](https://developer.android.com/reference/android/view/Display#getRealMetrics(android.util.DisplayMetrics))

To mitigate the behavior of applications using Display APIs to retrieve the
application's bounds, Android 12 constrains the values returned by the APIs
for apps that are not fully resizable. This could have an impact on
apps that are using this information with `MediaProjection`.

Apps should use the `WindowMetrics` APIs to query the bounds of
their window, and [`Configuration.densityDpi`](https://developer.android.com/reference/android/content/res/Configuration#densityDpi)
to query the current density.

For broader compatibility with older versions of Android, you can use the
Jetpack [`WindowManager`](https://developer.android.com/jetpack/androidx/releases/window) library, which
includes a [`WindowMetrics`](https://developer.android.com/reference/androidx/window/layout/WindowMetrics) class
that supports Android 4.0 (API level 14) and higher.

#### Examples of how to use WindowMetrics

First, be sure your app's activities are [fully resizable](https://developer.android.com/guide/topics/ui/multi-window).

An activity should rely upon `WindowMetrics` from an activity context for any
UI-related work, particularly
[`WindowManager.getCurrentWindowMetrics()`](https://developer.android.com/reference/android/view/WindowManager#getCurrentWindowMetrics())
or Jetpack's
[`WindowMetricsCalculator.computeCurrentWindowMetrics()`](https://developer.android.com/reference/androidx/window/layout/WindowMetricsCalculator#computeCurrentWindowMetrics(android.app.Activity)).

If your app creates a `MediaProjection`, the bounds must be correctly sized
since the projection captures the display partition in which the projector app
is running.

If the app is fully resizable, the activity context returns the correct bounds
like so:  

### Kotlin

```kotlin
val projectionMetrics: WindowMetrics = activityContext
      .getSystemService(WindowManager::class.java).maximumWindowMetrics
```

### Java

```java
WindowMetrics projectionMetrics = activityContext
      .getSystemService(WindowManager.class).getMaximumWindowMetrics();
```

If the app is not fully resizable, it must query from a `WindowContext`
instance and retrieve the `WindowMetrics` of the activity bounds using
[`WindowManager.getMaximumWindowMetrics()`](https://developer.android.com/reference/android/view/WindowManager#getMaximumWindowMetrics())
or the Jetpack method
[`WindowMetricsCalculator.computeMaximumWindowMetrics()`](https://developer.android.com/reference/androidx/window/layout/WindowMetricsCalculator#computeMaximumWindowMetrics(android.app.Activity)).  

### Kotlin

```kotlin
val windowContext = context.createWindowContext(mContext.display!!,
      WindowManager.LayoutParams.TYPE_APPLICATION, null)
val projectionMetrics = windowContext.getSystemService(WindowManager::class.java)
      .maximumWindowMetrics
```

### Java

```java
Context windowContext = context.createWindowContext(mContext.getDisplay(),
      WindowManager.LayoutParams.TYPE_APPLICATION, null);
WindowMetrics projectionMetrics = windowContext.getSystemService(WindowManager.class)
      .getMaximumWindowMetrics();
```
| **Note:** Any library that uses `MediaProjection` should also follow this advice and query the appropriate `WindowMetrics`.

### All apps in multi-window mode

Android 12 makes multi-window mode standard behavior.

On large screens (sw \>= 600dp), the platform supports all apps in multi-window
mode regardless of app configuration. If
[`resizeableActivity="false"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity),
the app is put into compatibility mode when necessary to accommodate display
dimensions.

On small screens (sw \< 600dp), the system checks an activity's
[`minWidth`](https://developer.android.com/reference/android/content/pm/ActivityInfo.WindowLayout#attr_android:minWidth)
and
[`minHeight`](https://developer.android.com/reference/android/content/pm/ActivityInfo.WindowLayout#attr_android:minHeight)
to determine whether the activity can run in multi-window mode. If
[`resizeableActivity="false"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity),
the app is prevented from running in multi‑window mode regardless of minimum
width and height.

For more information, see [Multi-window support](https://developer.android.com/guide/topics/ui/multi-window).

### Camera preview on large screens

Camera apps generally assume a fixed relationship between the orientation of
the device and the aspect ratio of the camera preview. But large screen form
factors, such as foldable devices, and display modes such as multi-window and
multi-display, challenge that assumption.

On Android 12, camera apps that request a specific screen
orientation and are not resizable (`resizeableActivity="false"`) automatically
enter inset portrait mode, which ensures the proper orientation and aspect
ratio of the camera preview. On foldables and other devices that have a camera
hardware abstraction layer ([HAL](https://source.android.com/devices/camera)),
additional rotation is applied to the camera output to compensate for camera
sensor orientation, and the camera output is cropped to match the aspect ratio
of the app's camera preview. The cropping and extra rotation ensure proper
presentation of the camera preview regardless of device orientation and folded
or unfolded state of the device.

### UX delay for foreground service notifications

To provide a streamlined experience for short-running [foreground
services](https://developer.android.com/guide/components/foreground-services), devices that run
Android 12 or higher can delay the display of foreground service
notifications by 10 seconds, with [a few
exceptions](https://developer.android.com/guide/components/foreground-services#notification-immediate). This
change gives short-lived tasks a chance to complete before their notifications
appear.

## Performance

### Restricted App Standby Bucket

Android 11 (API level 30) introduced the [restricted
bucket](https://developer.android.com/topic/performance/appstandby#restricted-bucket) as an App Standby
Bucket. Starting in Android 12, this bucket is active by default.
The restricted bucket has the lowest priority (and the highest restrictions) of
all the buckets. The buckets in order of priority from high to low are:

1. Active: App is currently being used or was very recently used.
2. Working set: App is in regular use.
3. Frequent: App is often used, but not every day.
4. Rare: App is not frequently used.
5. Restricted: App consumes a great deal of system resources, or may exhibit undesirable behavior.

The system considers your app's behavior, in addition to usage patterns, to
decide whether to place your app in the restricted bucket.

Your app is less likely to be placed in the restricted bucket if your app uses
system resources more responsibly. Also, the system places your app in a less
restrictive bucket if the user interacts directly with your app.

#### Check whether your app is in the restricted bucket

To check whether the system has placed your app in the restricted bucket, call
[`getAppStandbyBucket()`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#getAppStandbyBucket()).
If the return value of this method is `STANDBY_BUCKET_RESTRICTED`, then your app
is in the restricted bucket.

#### Test the restricted bucket behavior

To test how your app behaves when the system places your app into the restricted
bucket, you can manually move your app to that bucket. To do so, run the
following command in a terminal window:  

```
adb shell am set-standby-bucket PACKAGE_NAME restricted
```

### Foreground location and Battery Saver

Starting with Android 12, foreground location (including from a
foreground service) can continue to be delivered while Battery Saver is
active, even while the screen is off.

Previously, Battery Saver mode stopped location updates when the screen was off.
This change enables better battery life for users, and means that developers can
refrain from asking users to disable Battery Saver in order to ensure
location deliveries.

Apps that request location through a foreground service should take
the following steps:

1. Call [`getLocationPowerSaverMode()`](https://developer.android.com/reference/android/os/PowerManager#getLocationPowerSaveMode()) to check how the device's location features behave when Battery Saver is active.
2. If this returns [`LOCATION_MODE_FOREGROUND_ONLY`](https://developer.android.com/reference/android/os/PowerManager#LOCATION_MODE_FOREGROUND_ONLY), your app will continue to receive location updates while in the foreground or running a foreground service while Battery Saver is on and the screen is off.

## Security and privacy

### Approximate location

![The dialog has two sets of options, one above the
other](https://developer.android.com/static/images/about/versions/12/approximate-location-full-prompt.svg) **Figure 1.** System permissions dialog that allows the user to grant approximate location information.

On devices that run Android 12 or higher, [users can
request](https://developer.android.com/training/location/permissions#approximate-request) that your app have
access to only [approximate location](https://developer.android.com/training/location/permissions#accuracy)
information.
| **Note:** If your app requests `ACCESS_COARSE_LOCATION` but not `ACCESS_FINE_LOCATION`, then this change doesn't affect your app.

If your app requests the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
runtime permission, you should also request the
[`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)
permission to handle the case where the user grants approximate location access
to your app. You should include both permissions in a single [runtime
request](https://developer.android.com/training/permissions/requesting#allow-system-manage-request-code).
| **Caution:** On some releases of Android 12, this change only affects apps that target Android 12 or higher. In those releases, if your app requests `ACCESS_FINE_LOCATION`, it must also request `ACCESS_COARSE_LOCATION` to show the system permissions dialog.

The system permissions dialog includes the following options for the user,
as shown in figure 1:

- **Precise**: Provides access to precise location information.
- **Approximate**: Provides access only to approximate location information.

### Microphone and camera toggles

Supported devices that run Android 12 or higher allow users to
enable and disable camera and microphone access for all apps on the device, by
pressing a single toggle option. Users can access the toggleable options from
[Quick Settings](https://support.google.com/android/answer/9083864), as shown in
figure 1, or from the Privacy screen in system settings.

Learn more about these
[toggles](https://developer.android.com/training/permissions/explaining-access#toggles), and how to check
that your app follows best practices regarding the
[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) and
[`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO)
permissions.

### Microphone and camera indicators

On devices that run Android 12 or higher, when an app accesses
the microphone or camera, an icon appears in the status bar.

Learn more about these
[indicators](https://developer.android.com/training/permissions/explaining-access#indicators) and how to
check that your app follows best practices regarding the
[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) and
[`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO)
permissions.  
![Quick settings tiles are labeled 'Camera access' and
'Mic access'](https://developer.android.com/static/images/about/versions/12/mic-camera-toggles.svg) **Figure 2.** Microphone and camera toggles in Quick Settings.  
![A rounded rectangle in the upper-right corner, which
includes a camera icon and a microphone icon](https://developer.android.com/static/images/about/versions/12/mic-camera-indicators.svg) **Figure 3.** Microphone and camera indicators, which show recent data access.

<br />

### Permission package visibility

On devices that run Android 12 or higher, apps that target
Android 11 (API level 30) or higher and that call one of following methods
receive a filtered set of results, based on the app's [package
visibility](https://developer.android.com/training/package-visibility) into other apps:

- [`getAllPermissionGroups()`](https://developer.android.com/reference/android/content/pm/PackageManager#getAllPermissionGroups(int))
- [`getPermissionGroupInfo()`](https://developer.android.com/reference/android/content/pm/PackageManager#getPermissionGroupInfo(java.lang.String,%20int))
- [`getPermissionInfo()`](https://developer.android.com/reference/android/content/pm/PackageManager#getPermissionInfo(java.lang.String,%20int))
- [`queryPermissionsByGroup()`](https://developer.android.com/reference/android/content/pm/PackageManager#queryPermissionsByGroup(java.lang.String,%20int))

### BouncyCastle implementation removed

Android 12 removes many
[BouncyCastle](https://www.bouncycastle.org/) implementations of
cryptographic algorithms that were previously deprecated, including all AES
algorithms. The system instead uses the
[Conscrypt](https://github.com/google/conscrypt) implementations of
these algorithms.

This change affects your app if any of the following are true:

- **Your app uses 512-bit key sizes.** Conscrypt doesn't support this key size. If necessary, update your app's cryptography logic to use different key sizes.
- **Your app uses invalid key sizes with `KeyGenerator`.**
  Conscrypt's implementation of
  [`KeyGenerator`](https://developer.android.com/reference/javax/crypto/KeyGenerator) performs additional
  validation on key parameters, compared to BouncyCastle. For example, Conscrypt
  doesn't allow your app to generate a 64-bit AES key because AES only supports
  128-, 192-, and 256-bit keys.

  BouncyCastle allows keys of invalid sizes to be generated, but later fails
  if these keys are used with a [`Cipher`](https://developer.android.com/reference/javax/crypto/Cipher).
  Conscrypt fails earlier.
- **You initialize your Galois/Counter Mode (GCM) ciphers using a size other
  than 12 bytes.** Conscrypt's implementation of
  [`GcmParameterSpec`](https://developer.android.com/reference/javax/crypto/spec/GCMParameterSpec) requires an
  initialization of 12 bytes, which NIST recommends.

### Clipboard access notifications

On Android 12 and higher, when an app calls
[`getPrimaryClip()`](https://developer.android.com/reference/android/content/ClipboardManager#getPrimaryClip())
to [access clip data from a different
app](https://developer.android.com/guide/topics/text/copy-paste#Pasting) for the first time, a toast message
notifies the user of this clipboard access.

The text inside the toast message contains the following format:
<var translate="no">APP</var>` pasted from your clipboard.`
| **Note:** Your app might call [`getPrimaryClipDescription()`](https://developer.android.com/reference/android/content/ClipboardManager#getPrimaryClipDescription()) to receive information about the [current data that's on the
| clipboard](https://developer.android.com/guide/topics/text/copy-paste#ClipClasses). When your app calls this method, the system doesn't show a toast message.

#### Information about text in clip description

On Android 12 and higher, `getPrimaryClipDescription()` can
detect the following details:

- Stylized text, using [`isStyledText()`](https://developer.android.com/reference/android/content/ClipDescription#isStyledText()).
- Different classifications of text, such as URLs, using [`getConfidenceScore()`](https://developer.android.com/reference/android/content/ClipDescription#getConfidenceScore(java.lang.String)).

### Apps can't close system dialogs

To improve user control when interacting with apps and the system, the
[`ACTION_CLOSE_SYSTEM_DIALOGS`](https://developer.android.com/reference/android/content/Intent#ACTION_CLOSE_SYSTEM_DIALOGS)
intent action is deprecated as of Android 12. Except for [a few
special cases](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs-exceptions), when your app tries to [invoke
an intent](https://developer.android.com/guide/components/intents-filters) that contains this action, the
system does one of the following based on your app's target SDK version:

- If your app targets Android 12 or higher, a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException) occurs.
- If your app targets Android 11 (API level 30) or lower, the intent doesn't
  execute, and the following message appears in
  [Logcat](https://developer.android.com/studio/command-line/logcat):

  ```
  E ActivityTaskManager Permission Denial: \
  android.intent.action.CLOSE_SYSTEM_DIALOGS broadcast from \
  com.package.name requires android.permission.BROADCAST_CLOSE_SYSTEM_DIALOGS, \
  dropping broadcast.
  ```

#### Exceptions

In the following cases, an app can still close system dialogs on
Android 12 or higher:

- Your app is running an [instrumentation
  test](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests).
- Your app targets Android 11 or lower and is showing a window
  that is on top of the [notification
  drawer](https://material.io/design/platform-guidance/android-notifications#behavior).

  | **Note:** If your app targets Android 12, you don't need to use `ACTION_CLOSE_SYSTEM_DIALOGS` in this situation. That's because, if your app calls [`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) while a window is on top of the notification drawer, the system closes the notification drawer automatically.
- Your app targets Android 11 or lower. In addition, the user has
  interacted with a notification, possibly using the notification's [action
  buttons](https://developer.android.com/training/notify-user/build-notification#Actions), and your app is
  processing a [service](https://developer.android.com/guide/components/services) or [broadcast
  receiver](https://developer.android.com/guide/components/broadcasts) in response to that user action.

- Your app targets Android 11 or lower and has an active
  [accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service). If your app
  targets Android 12 and wants to close the notification bar, use
  the
  [`GLOBAL_ACTION_DISMISS_NOTIFICATION_SHADE`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#GLOBAL_ACTION_DISMISS_NOTIFICATION_SHADE)
  accessibility action instead.

### Untrusted touch events are blocked

To preserve system security and a good user experience,
Android 12 prevents apps from consuming [touch
events](https://developer.android.com/training/gestures) where an overlay obscures the app in an unsafe way.
In other words, the system blocks touches that pass through certain windows,
with [a few exceptions](https://developer.android.com/about/versions/12/behavior-changes-all#untrusted-touch-events-exceptions).

#### Affected apps

This change affects apps that choose to let touches pass through their windows,
for example by using the
[`FLAG_NOT_TOUCHABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_TOUCHABLE)
flag. Several examples include, but aren't limited to, the following:

- Overlays that require the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) permission, such as windows that use [`TYPE_APPLICATION_OVERLAY`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY), and use the `FLAG_NOT_TOUCHABLE` flag.
- Activity windows that use the `FLAG_NOT_TOUCHABLE` flag.

#### Exceptions

In the following cases, "pass-through" touches are allowed:

- **Interactions within your app.** Your app shows the overlay, and the overlay appears only when the user is interacting with your app.
- **Trusted windows.** These windows include (but aren't limited to) the
  following:

  - [Accessibility windows](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_ACCESSIBILITY_OVERLAY)
  - [Input method editor (IME) windows](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_INPUT_METHOD)
  - [Assistant windows](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_TOUCHABLE)

  | **Note:** Windows of type [`TYPE_APPLICATION_OVERLAY`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY) **aren't** trusted.
- **Invisible windows.** The window's root view is
  [`GONE`](https://developer.android.com/reference/android/view/View#GONE) or
  [`INVISIBLE`](https://developer.android.com/reference/android/view/View#INVISIBLE).

- **Completely transparent windows.** The
  [`alpha`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#alpha) property
  is 0.0 for the window.

- **Sufficiently translucent system alert windows.** The system considers a set
  of system alert windows to be sufficiently translucent when the combined opacity
  is less than or equal to the system's maximum obscuring opacity for touches.
  In Android 12, this maximum opacity is 0.8 by default.

#### Detect when an untrusted touch is blocked

If a touch action is blocked by the system,
[Logcat](https://developer.android.com/studio/command-line/logcat) logs the following message:  

    Untrusted touch due to occlusion by PACKAGE_NAME

#### Test the change

Untrusted touches are blocked by default on devices that run
Android 12 or higher. To allow untrusted touches, run
the following [ADB command](https://developer.android.com/studio/command-line/adb) in a terminal window:  

```bash
# A specific app
adb shell am compat disable BLOCK_UNTRUSTED_TOUCHES com.example.app

# All apps
# If you'd still like to see a Logcat message warning when a touch would be
# blocked, use 1 instead of 0.
adb shell settings put global block_untrusted_touches 0
```

To revert the behavior to the default (untrusted touches are blocked), run the
following command:  

```bash
# A specific app
adb shell am compat reset BLOCK_UNTRUSTED_TOUCHES com.example.app

# All apps
adb shell settings put global block_untrusted_touches 2
```

## Activity lifecycle

### Root launcher activities are no longer finished on Back press

Android 12 changes the default handling of the system Back press on launcher
activities that are at the root of their tasks. In previous versions, the system
would finish these activities on Back press. In Android 12, the system now moves
the activity and its task to the background instead of finishing the activity.
The new behavior matches the current behavior when navigating out of an app
using the Home button or gesture.
| **Note:** The system applies the new behavior only to launcher activities that are the root of their tasks---that is, to activities that declare an [Intent
| filter](https://developer.android.com/reference/android/content/IntentFilter) with both [`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) and [`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER). For other activities, the system handles Back press as it did before, by finishing the activity.

For most apps, this change means that users who use Back to navigate out of your
app are able to more quickly resume your app from a [warm state](https://developer.android.com/topic/performance/vitals/launch-time#warm),
instead of having to completely restart the app from a
[cold state](https://developer.android.com/topic/performance/vitals/launch-time#cold).

We recommend testing your apps with this change. If your app currently overrides
[`onBackPressed()`](https://developer.android.com/reference/android/app/Activity#onBackPressed()) to handle
Back navigation and finish the `Activity`, update your implementation to call
through to `super.onBackPressed()` instead of finishing. Calling
`super.onBackPressed()` moves the activity and its task to the background when
appropriate and provides a more consistent navigation experience for users
across apps.

Also note that, in general, we recommend using the AndroidX Activity APIs for
[providing custom back navigation](https://developer.android.com/guide/navigation/navigation-custom-back),
rather than overriding `onBackPressed()`. The AndroidX Activity APIs
automatically defer to the appropriate system behavior if there are no
components intercepting the system Back press.

## Graphics and images

### Improved refresh rate switching

In Android 12, refresh rate changes using
[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int,%20boolean))
can happen regardless of whether the display supports a seamless transition to
the new refresh rate; a seamless transition is one that doesn't have any visual
interruptions, such as a black screen for a second or two. Previously, if the
display did not support a seamless transition, it would typically continue using
the same refresh rate after `setFrameRate()` is called. You can determine in
advance whether the transition to the new refresh will likely be seamless by
calling [`getAlternativeRefreshRates()`](https://developer.android.com/reference/android/view/Display.Mode#getAlternativeRefreshRates()).
Generally, the callback [`onDisplayChanged()`](https://developer.android.com/reference/android/hardware/display/DisplayManager.DisplayListener#onDisplayChanged(int))
is called after the refresh rate switch completes, but for some
externally-connected displays, it is called during a non-seamless transition.

Here's an example of how you might implement this:  

### Kotlin

```kotlin
// Determine whether the transition will be seamless.
// Non-seamless transitions may cause a 1-2 second black screen.
val refreshRates = this.display?.mode?.alternativeRefreshRates
val willBeSeamless = Arrays.asList<FloatArray>(refreshRates).contains(newRefreshRate)

// Set the frame rate even if the transition will not be seamless.
surface.setFrameRate(newRefreshRate, FRAME_RATE_COMPATIBILITY_FIXED_SOURCE, CHANGE_FRAME_RATE_ALWAYS)
```

### Java

```java
// Determine whether the transition will be seamless.
// Non-seamless transitions may cause a 1-2 second black screen.
Display display = context.getDisplay(); // API 30+
Display.Mode mode = display.getMode();
float[] refreshRates = mode.getAlternativeRefreshRates();
boolean willBeSeamless = Arrays.asList(refreshRates).contains(newRefreshRate);

// Set the frame rate even if the transition will not be seamless.
surface.setFrameRate(newRefreshRate, FRAME_RATE_COMPATIBILITY_FIXED_SOURCE, CHANGE_FRAME_RATE_ALWAYS);
```

## Connectivity

### Passpoint updates

The following APIs are added in Android 12:

- [`isPasspointTermsAndConditionsSupported()`](https://developer.android.com/reference/android/net/wifi/WifiManager#isPasspointTermsAndConditionsSupported()): *Terms and conditions* is a [Passpoint](https://developer.android.com/guide/topics/connectivity/passpoint) feature that allows network deployments to replace insecure captive portals, which use open networks, with a secure Passpoint network. A notification is displayed to the user when terms and conditions are required to be accepted. Apps that suggest Passpoint networks that are gated by terms and conditions must call this API first to make sure that the device supports the capability. If the device does not support the capability, it won't be able to connect to this network, and an alternative or legacy network must be suggested.
- [`isDecoratedIdentitySupported()`](https://developer.android.com/reference/android/net/wifi/WifiManager#isDecoratedIdentitySupported()):
  When authenticating to networks with a prefix decoration, the decorated
  identity prefix allows network operators to update the Network Access
  Identifier (NAI) to perform explicit routing through multiple proxies inside
  of an AAA network (see
  [RFC 7542](https://datatracker.ietf.org/doc/html/rfc7542) for
  more on this).

  Android 12 implements this feature to conform with the [WBA specification for
  PPS-MO
  extensions](https://wballiance.com/wp-content/uploads/2021/03/WBA-PPS-MO-Extensions-v1.0.0.pdf).
  Apps that suggest Passpoint networks that require a decorated identity must
  call this API first to make sure that the device supports the capability. If
  the device does not support the capability, the identity won't be decorated
  and the authentication to the network might fail.

To create a Passpoint suggestion, apps must use the
[`PasspointConfiguration`](https://developer.android.com/reference/android/net/wifi/hotspot2/PasspointConfiguration),
[`Credential`](https://developer.android.com/reference/android/net/wifi/hotspot2/pps/Credential), and
[`HomeSp`](https://developer.android.com/reference/android/net/wifi/hotspot2/pps/HomeSp) classes. These
classes describe the Passpoint profile, which is defined in the [Wi-Fi Alliance
Passpoint
specification](https://www.wi-fi.org/downloads-registered-guest/Passpoint_Specification_Package_v3.2.zip/35974).

For more information, see [Wi-Fi suggestion API for internet connectivity](https://developer.android.com/guide/topics/connectivity/wifi-suggest).

## Updated non-SDK interface restrictions

Android 12 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 12, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see [Updates to
non-SDK interface restrictions in Android 12](https://developer.android.com/about/versions/12/non-sdk-12). To learn more
about non-SDK interfaces generally, see [Restrictions on non-SDK
interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).