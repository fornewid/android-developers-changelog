---
title: https://developer.android.com/about/versions/14/behavior-changes-14
url: https://developer.android.com/about/versions/14/behavior-changes-14
source: md.txt
---

Like previous releases, Android 14 includes behavior changes that might affect
your app. The following behavior changes apply exclusively to apps that are
targeting Android 14 (API level 34) or higher. If your app is targeting Android
14 or higher, you should modify your app to support these behaviors properly,
where applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 14](https://developer.android.com/about/versions/14/behavior-changes-all) regardless of
the app's [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target).

## Core functionality

### Foreground service types are required

If your app targets Android 14 (API level 34) or higher, it must [specify at
least one foreground service type](https://developer.android.com/about/versions/14/changes/fgs-types-required) for each [foreground service](https://developer.android.com/guide/components/foreground-services) within
your app. You should choose a foreground service type that represents your app's
use case. The system expects foreground services that have a particular type to
satisfy a particular use case.
| **Note:** Android 14 introduces foreground service types for [health](https://developer.android.com/about/versions/14/changes/fgs-types-required#health) and [remote
| messaging](https://developer.android.com/about/versions/14/changes/fgs-types-required#remote-messaging) use cases. The system also reserves new types for [short
| services](https://developer.android.com/about/versions/14/changes/fgs-types-required#short-service), [special use cases](https://developer.android.com/about/versions/14/changes/fgs-types-required#special-use), and [system exemptions](https://developer.android.com/about/versions/14/changes/fgs-types-required#system-exempted).

If a use case in your app isn't associated with any of these types, it's
strongly recommended that you migrate your logic to use [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) or
[user-initiated data transfer jobs](https://developer.android.com/develop/background-work/background-tasks/uidt).

### Enforcement of BLUETOOTH_CONNECT permission in BluetoothAdapter

Android 14 enforces the [`BLUETOOTH_CONNECT`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT) permission when calling the
`BluetoothAdapter` [`getProfileConnectionState()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getProfileConnectionState(int)) method for apps targeting
Android 14 (API level 34) or higher.

This method already required the `BLUETOOTH_CONNECT` permission, but it was not
enforced. Make sure your app declares `BLUETOOTH_CONNECT` in your app's
`AndroidManifest.xml` file as shown in the following snippet and [check that
a user has granted the permission](https://developer.android.com/training/permissions/requesting#already-granted) before calling
`getProfileConnectionState`.  

    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />

### OpenJDK 17 updates

Android 14 continues the work of refreshing Android's core libraries to align
with the features in the latest OpenJDK LTS releases, including both library
updates and Java 17 language support for app and platform developers.

A few of these changes can affect app compatibility:

- **Changes to regular expressions** : Invalid group references are now disallowed to more closely follow the semantics of OpenJDK. You might see new cases where an `IllegalArgumentException` is thrown by the [`java.util.regex.Matcher`](https://developer.android.com/reference/java/util/regex/Matcher) class, so make sure to test your app for areas that use regular expressions. To enable or disable this change while testing, toggle the `DISALLOW_INVALID_GROUP_REFERENCE` flag using the [compatibility framework tools](https://developer.android.com/guide/app-compatibility/test-debug#toggle-dev-options).
- **UUID handling** : The [`java.util.UUID.fromString()`](https://developer.android.com/reference/java/util/UUID#fromString(java.lang.String)) method now does more strict checks when validating the input argument, so you might see an `IllegalArgumentException` during deserialization. To enable or disable this change while testing, toggle the `ENABLE_STRICT_VALIDATION` flag using the [compatibility framework tools](https://developer.android.com/guide/app-compatibility/test-debug#toggle-dev-options).
- **ProGuard issues** : In some cases, the addition of the [`java.lang.ClassValue`](https://developer.android.com/reference/java/lang/ClassValue) class causes an issue if you try to shrink, obfuscate, and optimize your app using ProGuard. The problem originates with a Kotlin library that changes runtime behaviour based on whether `Class.forName("java.lang.ClassValue")` returns a class or not. If your app was developed against an older version of the runtime without the `java.lang.ClassValue` class available, then these optimizations might remove the `computeValue` method from classes derived from `java.lang.ClassValue`.

### JobScheduler reinforces callback and network behavior

Since its introduction, JobScheduler expects your app to return from
[`onStartJob`](https://developer.android.com/reference/android/app/job/JobService#onStartJob(android.app.job.JobParameters)) or [`onStopJob`](https://developer.android.com/reference/android/app/job/JobService#onStopJob(android.app.job.JobParameters)) within a few seconds. Prior to Android 14,
if a job runs too long, the job is stopped and fails silently.
If your app targets Android 14 (API level 34) or higher and
exceeds the granted time on the main thread, the app triggers an ANR
with the error message "No response to `onStartJob`" or
"No response to `onStopJob`".

This ANR may be a result of 2 scenarios:
1. There is work blocking the main thread, preventing the callbacks `onStartJob`
or `onStopJob` from executing and completing within the expected time limit.
2. The developer is running blocking work within the JobScheduler
callback `onStartJob` or `onStopJob`, preventing the callback from
completing within the expected time limit.

To address #1, you will need to further debug what is blocking the main thread
when the ANR occurs, you can do this using
[`ApplicationExitInfo#getTraceInputStream()`](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo#getTraceInputStream()) to get the tombstone
trace when the ANR occurs. If you're able to manually reproduce the ANR,
you can record a [system trace](https://developer.android.com/studio/profile/cpu-profiler) and inspect the trace using either
[Android Studio](https://developer.android.com/studio/profile/inspect-traces) or [Perfetto](https://developer.android.com/tools/perfetto) to better understand what is running on
the main thread when the ANR occurs.
Note that this can happen when using JobScheduler API directly
or using the androidx library WorkManager.

To address #2, consider migrating to [WorkManager](https://developer.android.com/guide/background/persistent/threading), which provides
support for wrapping any processing in `onStartJob` or `onStopJob`
in an asynchronous thread.

`JobScheduler` also introduces a requirement to declare the
[`ACCESS_NETWORK_STATE`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE) permission if using [`setRequiredNetworkType`](https://developer.android.com/android/app/job/JobInfo.Builder#setRequiredNetworkType(int)) or
[`setRequiredNetwork`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setRequiredNetwork(android.net.NetworkRequest)) constraint. If your app does not declare the
`ACCESS_NETWORK_STATE` permission when scheduling the job and is targeting
Android 14 or higher, it will result in a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

### Tiles launch API

For apps targeting 14 and higher,
[`TileService#startActivityAndCollapse(Intent)`](https://developer.android.com/reference/android/service/quicksettings/TileService#startActivityAndCollapse(android.content.Intent)) is deprecated and now throws
an exception when called. If your app launches activities from tiles, use
[`TileService#startActivityAndCollapse(PendingIntent)`](https://developer.android.com/reference/android/service/quicksettings/TileService#startActivityAndCollapse(android.app.PendingIntent)) instead.

## Privacy

## Partial access to photos and videos

Android 14 introduces Selected Photos Access, which allows users to grant apps
access to specific images and videos in their library, rather than granting
access to all media of a given type.

This change is only enabled if your app targets Android 14 (API level 34) or
higher. If you don't use the photo picker yet, we recommend [implementing it in
your app](https://developer.android.com/training/data-storage/shared/photopicker) to provide a consistent experience for selecting images and videos
that also enhances user privacy without having to request any storage
permissions.

If you maintain your own gallery picker using storage permissions and need to
maintain full control over your implementation, [adapt your implementation](https://developer.android.com/about/versions/14/changes/partial-photo-video-access#app-gallery-picker)
to use the new [`READ_MEDIA_VISUAL_USER_SELECTED`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VISUAL_USER_SELECTED) permission. If your app
doesn't use the new permission, the system runs your app in a [compatibility
mode](https://developer.android.com/about/versions/14/changes/partial-photo-video-access#compatibility-mode).

## User experience

### Secure full-screen Intent notifications

With Android 11 (API level 30), it was possible for any app to use
[`Notification.Builder.setFullScreenIntent`](https://developer.android.com/reference/android/app/Notification.Builder#setFullScreenIntent(android.app.PendingIntent,%20boolean)) to send full-screen
intents while the phone is locked. You could auto-grant this on app install by
declaring [`USE_FULL_SCREEN_INTENT`](https://developer.android.com/reference/android/Manifest.permission#USE_FULL_SCREEN_INTENT) permission in the
AndroidManifest.

Full-screen intent notifications are designed for extremely high-priority
notifications demanding the user's immediate attention, such as an incoming
phone call or alarm clock settings configured by the user. For apps targeting
Android 14 (API level 34) or higher, apps that are allowed to use this
permission are limited to those that provide calling and alarms only. The Google
Play Store revokes default `USE_FULL_SCREEN_INTENT` permissions for any apps
that don't fit this profile. The deadline for these policy changes is [May 31,
2024](https://support.google.com/googleplay/android-developer/table/12921780?ref_topic=9877065).

This permission remains enabled for apps installed on the phone before the user
updates to Android 14. Users can turn this permission on and off.

You can use the new API
[`NotificationManager.canUseFullScreenIntent`](https://developer.android.com/reference/android/app/NotificationManager#canUseFullScreenIntent()) to check if your app
has the permission; if not, your app can use the new intent
[`ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT`](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT) to launch the settings
page where users can grant the permission.

## Security

### Restrictions to implicit and pending intents

For apps targeting Android 14 (API level 34) or higher, Android restricts apps
from sending implicit intents to internal app components in the following ways:

- Implicit intents are only delivered to exported components. Apps must either use an explicit intent to deliver to unexported components, or mark the component as exported.
- If an app creates a mutable pending intent with an intent that doesn't specify a component or package, the system throws an exception.

These changes prevent malicious apps from intercepting implicit intents that are
intended for use by an app's internal components.

For example, here is an [intent filter](https://developer.android.com/guide/components/intents-filters#Receiving) that could be
declared in your app's manifest file:  

    <activity
        android:name=".AppActivity"
        android:exported="false">
        <intent-filter>
            <action android:name="com.example.action.<var translate="no">APP_ACTION</var>" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
    </activity>

If your app tried to launch this activity using an implicit intent, an
[`ActivityNotFoundException`](https://developer.android.com/reference/android/content/ActivityNotFoundException) exception would be thrown:  

### Kotlin

```kotlin
// Throws an https://developer.android.com/reference/android/content/ActivityNotFoundException exception when targeting Android 14.
context.startActivity(Intent("com.example.action.<var translate="no">APP_ACTION</var>"))
```

### Java

```java
// Throws an https://developer.android.com/reference/android/content/ActivityNotFoundException exception when targeting Android 14.
context.startActivity(new Intent("com.example.action.<var translate="no">APP_ACTION</var>"));
```

To launch the non-exported activity, your app should use an explicit intent
instead:  

### Kotlin

```kotlin
// This makes the intent explicit.
val explicitIntent =
        Intent("com.example.action.<var translate="no">APP_ACTION</var>")
explicitIntent.apply {
    package = context.packageName
}
context.startActivity(explicitIntent)
```

### Java

```java
// This makes the intent explicit.
Intent explicitIntent =
        new Intent("com.example.action.<var translate="no">APP_ACTION</var>")
explicitIntent.setPackage(context.getPackageName());
context.startActivity(explicitIntent);
```

### Runtime-registered broadcasts receivers must specify export behavior

Apps and services that target Android 14 (API level 34) or higher and use
[context-registered receivers](https://developer.android.com/guide/components/broadcasts#context-registered-receivers) are required to specify a flag
to indicate whether or not the receiver should be exported to all other apps on
the device: either `RECEIVER_EXPORTED` or `RECEIVER_NOT_EXPORTED`, respectively.
This requirement helps protect apps from security vulnerabilities by leveraging
the [features for these receivers introduced in Android 13](https://developer.android.com/about/versions/13/features#runtime-receivers).

#### Exception for receivers that receive only system broadcasts

If your app is registering a receiver only for
[system broadcasts](https://developer.android.com/guide/components/broadcasts#system-broadcasts) through `Context#registerReceiver`
methods, such as [`Context#registerReceiver()`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter)), then it
shouldn't specify a flag when registering the receiver.

### Safer dynamic code loading

If your app targets Android 14 (API level 34) or higher and uses Dynamic Code
Loading (DCL), all dynamically-loaded files must be marked as read-only.
Otherwise, the system throws an exception. We recommend that apps [avoid
dynamically loading code](https://developer.android.com/privacy-and-security/security-tips#DynamicCode)
whenever possible, as doing so greatly increases the risk that an app can be
compromised by code injection or code tampering.

If you must dynamically load code, use the following approach to set the
dynamically-loaded file (such as a DEX, JAR, or APK file) as read-only as soon
as the file is opened and before any content is written:  

### Kotlin

```kotlin
val jar = File("<var translate="no">DYNAMICALLY_LOADED_FILE</var>.jar")
val os = FileOutputStream(jar)
os.use {
    // Set the file to read-only first to prevent race conditions
    jar.setReadOnly()
    // Then write the actual file content
}
val cl = PathClassLoader(jar, parentClassLoader)
```

### Java

```java
File jar = new File("<var translate="no">DYNAMICALLY_LOADED_FILE</var>.jar");
try (FileOutputStream os = new FileOutputStream(jar)) {
    // Set the file to read-only first to prevent race conditions
    jar.setReadOnly();
    // Then write the actual file content
} catch (IOException e) { ... }
PathClassLoader cl = new PathClassLoader(jar, parentClassLoader);
```

#### Handle dynamically-loaded files that already exist

To prevent exceptions from being thrown for existing dynamically-loaded files,
we recommend deleting and recreating the files before you try to dynamically
load them again in your app. As you recreate the files, follow the preceding
guidance for marking the files read-only at write time. Alternatively, you can
re-label the existing files as read-only, but in this case, we strongly
recommend that you verify the integrity of the files first (for example, by
checking the file's signature against a trusted value), to help protect your app
from malicious actions.

### Additional restrictions on starting activities from the background

For apps targeting Android 14 (API level 34) or higher, the system further
restricts when apps are allowed to start activities from the background:

- When an app sends a `PendingIntent` using [`PendingIntent#send()`](https://developer.android.com/reference/android/app/PendingIntent#send(android.content.Context,%20int,%20android.content.Intent,%20android.app.PendingIntent.OnFinished,%20android.os.Handler,%20java.lang.String,%20android.os.Bundle)) or similar methods, the app must opt in if it wants to grant its own background activity launch privileges to start the pending intent. To opt in, the app should pass an `ActivityOptions` bundle with [`setPendingIntentBackgroundActivityStartMode(MODE_BACKGROUND_ACTIVITY_START_ALLOWED)`](https://developer.android.com/reference/android/app/ActivityOptions#setPendingIntentBackgroundActivityStartMode(int)).
- When a visible app binds a service of another app that's in the background using the [`bindService()`](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent,%20android.content.Context.BindServiceFlags,%20java.util.concurrent.Executor,%20android.content.ServiceConnection)) method, the visible app must now opt in if it wants to grant its own background activity launch privileges to the bound service. To opt in, the app should include the [`BIND_ALLOW_ACTIVITY_STARTS`](https://developer.android.com/reference/android/content/Context#BIND_ALLOW_ACTIVITY_STARTS) flag when calling the `bindService()` method.

These changes expand the [existing set of restrictions](https://developer.android.com/guide/components/activities/background-starts) to protect
users by preventing malicious apps from abusing APIs to start disruptive
activities from the background.

### Zip path traversal

For apps targeting Android 14 (API level 34) or higher, Android prevents the Zip
Path Traversal Vulnerability in the following way:
[`ZipFile(String)`](https://developer.android.com/reference/java/util/zip/ZipFile#public-constructors) and
[`ZipInputStream.getNextEntry()`](https://developer.android.com/reference/java/util/zip/ZipInputStream#getNextEntry()) throws a
[`ZipException`](https://developer.android.com/reference/java/util/zip/ZipException) if zip file entry names contain ".." or start
with "/".

Apps can opt-out from this validation by calling
[`dalvik.system.ZipPathValidator.clearCallback()`](https://developer.android.com/reference/dalvik/system/ZipPathValidator#clearCallback()).

### User consent required for each MediaProjection capture session

For apps targeting Android 14 (API level 34) or higher, a `SecurityException` is
thrown by [`MediaProjection#createVirtualDisplay`](https://developer.android.com/reference/android/media/projection/MediaProjection#createVirtualDisplay(java.lang.String,%20int,%20int,%20int,%20int,%20android.view.Surface,%20android.hardware.display.VirtualDisplay.Callback,%20android.os.Handler)) in either of the following
scenarios:

- Your app caches the [`Intent`](https://developer.android.com/reference/android/content/Intent) that is returned from [`MediaProjectionManager#createScreenCaptureIntent`](https://developer.android.com/reference/android/media/projection/MediaProjectionManager#createScreenCaptureIntent()), and passes it multiple times to [`MediaProjectionManager#getMediaProjection`](https://developer.android.com/reference/android/media/projection/MediaProjectionManager#getMediaProjection(int,%20android.content.Intent)).
- Your app invokes `MediaProjection#createVirtualDisplay` multiple times on the same `MediaProjection` instance.

Your app must ask the user to give consent before each capture session. A single
capture session is a single invocation on
`MediaProjection#createVirtualDisplay`, and each `MediaProjection` instance must
be used only once.

#### Handle configuration changes

If your app needs to invoke `MediaProjection#createVirtualDisplay` to handle
configuration changes (such as the screen orientation or screen size changing),
you can follow these steps to update the `VirtualDisplay` for the existing
`MediaProjection` instance:

1. Invoke [`VirtualDisplay#resize`](https://developer.android.com/reference/kotlin/android/hardware/display/VirtualDisplay#resize) with the new width and height.
2. Provide a new [`Surface`](https://developer.android.com/reference/kotlin/android/view/Surface) with the new width and height to [`VirtualDisplay#setSurface`](https://developer.android.com/reference/kotlin/android/hardware/display/VirtualDisplay#setsurface).

#### Register a callback

Your app should register a callback to handle cases where the user doesn't grant
consent to continue a capture session. To do this, implement
[`Callback#onStop`](https://developer.android.com/reference/android/media/projection/MediaProjection.Callback#onStop()) and have your app release any related resources (such as
the `VirtualDisplay` and `Surface`).

If your app doesn't register this callback,
`MediaProjection#createVirtualDisplay` throws an [`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException)
when your app invokes it.

## Updated non-SDK restrictions

Android 14 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 14, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API
level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see
[Updates to non-SDK interface restrictions in Android 14](https://developer.android.com/about/versions/14/changes/non-sdk-14).
To learn more about non-SDK interfaces generally, see
[Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).