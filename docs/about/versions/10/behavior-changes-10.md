---
title: https://developer.android.com/about/versions/10/behavior-changes-10
url: https://developer.android.com/about/versions/10/behavior-changes-10
source: md.txt
---

Android 10 includes updated system behavior changes that may affect your app.
The changes listed on this page apply exclusively to apps that are targeting
API 29 or higher. If your app sets `targetSdkVersion` to "29" or
higher, you should modify your app to support these behaviors properly,
where applicable.

Make sure to also review the list of [behavior changes that affect all apps
running on Android 10](https://developer.android.com/about/versions/10/behavior-changes-all).
**Note:**In addition to the changes listed on this page, Android 10
introduces a large number of privacy-based changes and restrictions, including
the following:

- Scoped storage
- Access to USB device serial number
- Ability to enable, disable, and configure Wi-Fi
- Location permissions for connectivity APIs

These changes, which affect apps that target API level 29 or higher,
enhance user privacy. To learn more about how to support these changes, see
the [Privacy changes](https://developer.android.com/about/versions/10/privacy/changes) page.

## Updates to non-SDK interface restrictions

To help ensure app stability and compatibility, the platform started restricting
which [non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)
your app can use in Android 9 (API level 28). Android 10 includes updated lists
of restricted non-SDK interfaces based on collaboration with Android developers
and the latest internal testing. Our goal is to make sure that public
alternatives are available before we restrict non-SDK interfaces.

If you will not be targeting Android 10 (API level 29), some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can
[test your app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk) to
find out. If your app relies on non-SDK interfaces, you should begin planning a
migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should
[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more, see [Updates to non-SDK interface restrictions in Android 10](https://developer.android.com/about/versions/10/non-sdk-q)
and see [Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).

## Shared memory

Ashmem has changed the format of dalvik maps in /proc/\<pid\>/maps,
affecting apps that directly parse the maps file. Application developers should
test the /proc/\<pid\>/maps format on devices that run
Android 10 or higher and parse accordingly if the app depends on
dalvik map formats.

Apps targeting Android 10 cannot directly use ashmem
(/dev/ashmem) and must instead access shared memory via the NDK's
[`ASharedMemory` class](https://android.googlesource.com/platform/frameworks/base/+/master/native/android/sharedmem.cpp).
In addition, apps cannot make direct IOCTLs to existing ashmem file descriptors
and must instead use either the NDK's `ASharedMemory` class or the Android Java
APIs for creating shared memory regions. This change increases security and
robustness when working with shared memory, improving performance and security
of Android overall.

## Removed execute permission for app home directory

Execution of files from the writable app home directory is a
[W\^X violation](https://en.wikipedia.org/wiki/W%5EX).
Apps should load only the binary code that's embedded within an app's APK file.

Untrusted apps that target Android 10 cannot invoke `execve()`
directly on files within the app's home directory.

In addition, apps that target Android 10 cannot in-memory modify
executable code from files which have been opened with `dlopen()` and expect
those changes to be written through to disk, because the library cannot have
been mapped `PROT_EXEC` through a writable file descriptor. This includes any
shared object (`.so`) files with text relocations.

## Android runtime only accepts system-generated OAT files

The Android runtime (ART) no longer invokes `dex2oat` from the application
process. This change means that the ART will only accept OAT files that the
system has generated.

## Enforcing AOT correctness in ART

In the past, the ahead-of-time (AOT) compilation performed by the Android
Runtime (ART) could cause runtime crashes if the classpath environment was not
the same at compile time and runtime. Android 10 and higher
always require these environment contexts to be the same, resulting in the
following changes in behavior:

- Custom class loaders---that is, class loaders written by apps, unlike class loaders from the `dalvik.system` package---aren't AOT-compiled. This is because ART cannot know about customized class lookup implementation at runtime.
- Secondary dex files---that is, the dex files loaded manually by apps not in the primary APK---are AOT-compiled in the background. This is because first-use compilation might be too expensive, leading to unwanted latency before execution. Note that for apps, adopting splits and moving away from secondary dex files is recommended.
- Shared libraries in Android (the entries \<library\> and \<uses-library\> in an Android manifest) are implemented using a different class loader hierarchy than the one used in previous versions of the platform.

## Permissions changes for fullscreen intents

Apps that target Android 10 or higher and use notifications with
[fullscreen
intents](https://developer.android.com/training/notify-user/build-notification#urgent-message) must request
the
[`USE_FULL_SCREEN_INTENT`](https://developer.android.com/reference/android/Manifest.permission#USE_FULL_SCREEN_INTENT)
permission in their app's manifest file. This is a [normal
permission](https://developer.android.com/guide/topics/permissions/normal-permissions), so the system
automatically grants it to the requesting app.

If an app that targets Android 10 or higher attempts to create a
notification with a fullscreen intent without requesting the necessary
permission, the system ignores the fullscreen intent and outputs the following
log message:

```
Package your-package-name: Use of fullScreenIntent requires the USE_FULL_SCREEN_INTENT permission
```

## Support for foldables

Android 10 has changes that support foldables and large screen devices.

When an app runs on Android 10, the
[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) and
[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) methods work
differently. When multiple apps appear at the same time in multi-window or
multi-display mode, all the focusable top activities in visible stacks
are in the resumed state, but only one of them, the "topmost resumed" activity,
actually has focus. When running on versions earlier than Android 10, only a
single activity in the system can be resumed at a time, all other visible
activities are paused.

Do not confuse "focus" with the "topmost resumed" activity. The system assigns
priorities to activities based on z-order to give higher priority to
the activities that the user interacted with last. An activity can be
top-resumed, but not have focus (for example, if the notification shade is
expanded).

In Android 10 (API level 29) and later, you can subscribe to the
[`onTopResumedActivityChanged()`](https://developer.android.com/reference/android/app/Activity#onTopResumedActivityChanged(boolean)) callback
to be notified when your activity acquires or loses the topmost resumed
position. This is the equivalent of the resumed state before Android 10 and can be useful
as a hint if your app is using exclusive or singleton resources that might need
to be shared with other apps.

The behavior of the
[`resizeableActivity`](https://developer.android.com/guide/topics/ui/multi-window#resizeableActivity)
manifest attribute has also changed. If an app sets
`resizeableActivity=false` in Android 10 (API level 29) or later, it might be put in compatibility mode
when the available screen size changes, or if the app moves from one screen to
another.

Apps can use the
[`android:minAspectRatio`](https://developer.android.com/reference/android/R.attr#minAspectRatio)
attribute, introduced in Android 10, to indicate the [screen
ratios](https://developer.android.com/guide/topics/ui/foldables#new_screen_ratios) that your app supports.

Starting with version 3.5, Android Studio's emulator tool
includes 7.3" and 8" virtual devices for testing your code with larger screens.

For more information, see [Design your apps for foldables](https://developer.android.com/guide/topics/ui/foldables).