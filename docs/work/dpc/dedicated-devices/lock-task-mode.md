---
title: https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode
url: https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode
source: md.txt
---

# Lock task mode

This developer's guide explains how dedicated devices can be locked to a single
app or a set of apps. If you're an enterprise mobility management (EMM)
developer or solutions integrator read this guide to add lock task mode to your
solution.

## Overview

Android can run tasks in an immersive, kiosk-like fashion called *lock task
mode*. You might use lock task mode if you're developing a kiosk application or
a launcher to present a collection of apps. When the system runs in lock task
mode, device users typically can't see notifications, access non-allowlisted
apps, or return to the home screen (unless the home screen is allowlisted).
| **Key Term:** Lock task mode and screen pinning are sometimes used interchangeably. [Screen pinning](https://support.google.com/android/answer/9455138) appears similar (and provides an immersive experience) but the person using the device can exit the mode whenever they want.

Only apps that have been allowlisted by a device policy controller (DPC) can run
when the system is in lock task mode. Apps are allowlisted because the person
using the device can't always leave lock task mode.

How you combine the app allowlisted for lock task mode and the allowlisting DPC
will depend on the problem you want to solve. Here are some examples:

- A single app package that combines a kiosk (to present content) and a mini DPC (to allowlist itself for lock task mode).
- A DPC that's part of an enterprise mobility management solution, launching the customer's mobile apps in lock task mode.

## Availability

The system can run in lock task mode in Android 5.0 or later. Table 1 shows
which versions of Android support allowlisting apps by user.

|           Android version            |      DPC administers      |                                                                                    Notes                                                                                     |
|--------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Android 5.0 (API level 21) or higher | Fully managed device      |                                                                                                                                                                              |
| Android 8.0 (API level 26) or higher | Affiliated secondary user | The secondary user must be affiliated with the primary user. See [multiple user](https://developer.android.com/work/dpc/dedicated-devices/multiple-users#overview) overview. |
| Android 9.0 (API level 28) or higher | Secondary user            |                                                                                                                                                                              |
[**Table 1**. Android version support for DPC admin modes]

In Android 9.0 or later a DPC can start any app's activity into lock task mode.
In earlier versions, the app must already support starting its own activity in
lock task mode.

## Allowlist apps

A DPC must allowlist apps before they can be used in lock task mode. Call
[`DevicePolicyManager.setLockTaskPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskPackages(android.content.ComponentName,%20java.lang.String%5B%5D)) to
allowlist apps for lock task mode as shown in the following sample:  

### Kotlin

```kotlin
// Allowlist two apps.
private val KIOSK_PACKAGE = "com.example.kiosk"
private val PLAYER_PACKAGE = "com.example.player"
private val APP_PACKAGES = arrayOf(KIOSK_PACKAGE, PLAYER_PACKAGE)

// ...

val context = context
val dpm = context.getSystemService(Context.DEVICE_POLICY_SERVICE)
        as DevicePolicyManager
val adminName = getComponentName(context)
dpm.setLockTaskPackages(adminName, APP_PACKAGES)
```

### Java

```java
// Allowlist two apps.
private static final String KIOSK_PACKAGE = "com.example.kiosk";
private static final String PLAYER_PACKAGE = "com.example.player";
private static final String[] APP_PACKAGES = {KIOSK_PACKAGE, PLAYER_PACKAGE};

// ...

Context context = getContext();
DevicePolicyManager dpm =
    (DevicePolicyManager) context.getSystemService(Context.DEVICE_POLICY_SERVICE);
ComponentName adminName = getComponentName(context);
dpm.setLockTaskPackages(adminName, APP_PACKAGES);
```

To find out the apps previously allowlisted for lock task mode, a DPC can call
[`DevicePolicyManager.getLockTaskPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getLockTaskPackages(android.content.ComponentName)). Other
apps can call
[`DevicePolicyManager.isLockTaskPermitted()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isLockTaskPermitted(java.lang.String)) to confirm
that an app package supports lock task mode.

## Start lock task mode

In Android 9.0 (API level 28) or higher, you can start another app's activity in
lock task mode. If an activity is already running in the foreground or
background, you need to relaunch the activity. Call
[`ActivityOptions.setLockTaskEnabled()`](https://developer.android.com/reference/android/app/ActivityOptions#setLockTaskEnabled(boolean)) and supply these
options when starting the activity. The following snippet shows one way you can
do this:  

### Kotlin

```kotlin
// Set an option to turn on lock task mode when starting the activity.
val options = ActivityOptions.makeBasic()
options.setLockTaskEnabled(true)

// Start our kiosk app's main activity with our lock task mode option.
val packageManager = context.packageManager
val launchIntent = packageManager.getLaunchIntentForPackage(KIOSK_PACKAGE)
if (launchIntent != null) {
    context.startActivity(launchIntent, options.toBundle())
}
```

### Java

```java
// Set an option to turn on lock task mode when starting the activity.
ActivityOptions options = ActivityOptions.makeBasic();
options.setLockTaskEnabled(true);

// Start our kiosk app's main activity with our lock task mode option.
PackageManager packageManager = context.getPackageManager();
Intent launchIntent = packageManager.getLaunchIntentForPackage(KIOSK_PACKAGE);
if (launchIntent != null) {
  context.startActivity(launchIntent, options.toBundle());
}
```

In Android versions before 9.0, an app starts its own activities in lock task
mode by calling [`Activity.startLockTask()`](https://developer.android.com/reference/android/app/Activity#startLockTask()). To call this
method, the activity must be running in the foreground (see [Activity-lifecycle
concepts](https://developer.android.com/guide/components/activities/activity-lifecycle#alc)) so we suggest calling in the
[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) method of an [`Activity`](https://developer.android.com/reference/android/app/Activity) or
[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment). Here's how you can call `startLockTask()`:  

### Kotlin

```kotlin
// In our Fragment subclass.
override fun onResume() {
    super.onResume()
    // First, confirm that this package is allowlisted to run in lock task mode.
    if (dpm.isLockTaskPermitted(context.packageName)) {
        activity.startLockTask()
    } else {
        // Because the package isn't allowlisted, calling startLockTask() here
        // would put the activity into screen pinning mode.
    }
}
```

### Java

```java
// In our Fragment subclass.
@Override
public void onResume() {
  super.onResume();

  // First, confirm that this package is allowlisted to run in lock task mode.
  if (dpm.isLockTaskPermitted(context.getPackageName())) {
    getActivity().startLockTask();
  } else {
    // Because the package isn't allowlisted, calling startLockTask() here
    // would put the activity into screen pinning mode.
  }
}
```

Don't start lock task mode when the device is locked because the user might not
be able to unlock the device. You can call [`KeyguardManager`](https://developer.android.com/reference/android/app/KeyguardManager) methods to
find out if the device is locked and use an [`Activity`](https://developer.android.com/reference/android/app/Activity) lifecycle
callback (such as [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) that's called after unlocking) to
start lock task mode.

An app in lock task mode can start new activities as long as the activity
doesn't start a new task---except tasks that launch an allowlisted app. To
understand how tasks relate to activities, read the guide [Understand Tasks and
Back Stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack).

Alternatively, you can declare in your [app manifest
file](https://developer.android.com/guide/topics/manifest/manifest-intro) how an activity should behave when
the system is running in lock task mode. To have the system automatically run
your activity in lock task mode, set the
[`android:lockTaskMode`](https://developer.android.com/guide/topics/manifest/activity-element#ltmode) attribute to `if_whitelisted` as
shown in the following example:  

    <activity
        android:name=".MainActivity"
        android:lockTaskMode="if_whitelisted">
        <!-- ... -->
    </activity>

You can learn more about declaring options in the app manifest file, by reading
the [`lockTaskMode`](https://developer.android.com/reference/android/R.attr#lockTaskMode) reference.

## Stop lock task mode

A DPC can remotely stop lock task mode by removing the app package from the
allowlist. Call
[`DevicePolicyManager.setLockTaskPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskPackages(android.content.ComponentName,%20java.lang.String%5B%5D)), in
Android 6.0 (API level 23) or later, and omit the package name from the
allowlist array. When you update the allowlist, the app returns to the previous
task in the stack.
| **Note:** Removing the app from the allowlist in Android 5.0 and 5.1 doesn't stop lock task mode. If your solution needs to exit lock task mode on these versions, confirm that the app supports this itself. See the following `stopLockTask()` note.

If an activity previously called `startLockTask()`, then the activity can call
[`Activity.stopLockTask()`](https://developer.android.com/reference/android/app/Activity#stopLockTask()) to stop lock task mode. This method
only works for the activity that started lock task mode.

## Lifecycle callbacks

Your DPC might find it useful to know when an app (running in the same user)
enters and exits lock task mode. To receive callbacks, override the following
callback methods in your DPC's [`DeviceAdminReceiver`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver) subclass:

[`onLockTaskModeEntering()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onLockTaskModeEntering(android.content.Context,%20android.content.Intent,%20java.lang.String))
:   Called after an app enters lock task mode. You can get the package name of an
    app from the `pkg` argument.

[`onLockTaskModeExiting()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onLockTaskModeExiting(android.content.Context,%20android.content.Intent))
:   Called after an app exits lock task mode. This callback doesn't receive
    information about the app.

If you launch another app into lock task mode, you need to track the running
status in your own app. To check if the current app is running in lock task
mode, use the methods on [`ActivityManager`](https://developer.android.com/reference/android/app/ActivityManager) as shown in the following
example:  

### Kotlin

```kotlin
// Check if this app is in lock task mode. Screen pinning doesn't count.
var isLockTaskModeRunning = false

val activityManager = context
        .getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager

if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    isLockTaskModeRunning =
            activityManager.lockTaskModeState ==
            ActivityManager.LOCK_TASK_MODE_LOCKED
} else if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Deprecated in API level 23.
    isLockTaskModeRunning = activityManager.isInLockTaskMode
}

if (isLockTaskModeRunning) {
    // Show the exit button ...
}
```

### Java

```java
// Check if this app is in lock task mode. Screen pinning doesn't count.
boolean isLockTaskModeRunning = false;

ActivityManager activityManager = (ActivityManager)
    getContext().getSystemService(Context.ACTIVITY_SERVICE);

if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  isLockTaskModeRunning = activityManager.getLockTaskModeState()
      == ActivityManager.LOCK_TASK_MODE_LOCKED;
} else if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  // Deprecated in API level 23.
  isLockTaskModeRunning = activityManager.isInLockTaskMode();
}

if (isLockTaskModeRunning) {
  // Show the exit button ...
}
```

## Customize the UI

When an app runs in lock task mode, the system user interface (UI) changes in
the following ways:

- The status bar is blank with notifications and system information hidden.
- The Home and Overview buttons are hidden.
- Other apps can't launch new activities.
- The lock screen (if set) is disabled.

In Android 9.0 or higher when lock task mode is enabled, your DPC can enable
certain system UI features on the device---useful to developers creating a custom
launcher. Call
[`DevicePolicyManager.setLockTaskFeatures()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskFeatures(android.content.ComponentName,%20int)) as shown
in the following snippet:  

### Kotlin

```kotlin
// Enable the Home and Overview buttons so that our custom launcher can respond
// using our custom activities. Implicitly disables all other features.
dpm.setLockTaskFeatures(
        adminName,
        DevicePolicyManager.LOCK_TASK_FEATURE_HOME or
              DevicePolicyManager.LOCK_TASK_FEATURE_OVERVIEW)
```

### Java

```java
// Enable the Home and Overview buttons so that our custom launcher can respond
// using our custom activities. Implicitly disables all other features.
dpm.setLockTaskFeatures(adminName,
    DevicePolicyManager.LOCK_TASK_FEATURE_HOME |
          DevicePolicyManager.LOCK_TASK_FEATURE_OVERVIEW);
```

The system disables any features you don't include in the `flags` argument. The
enabled UI features persist between launches into lock task mode. If the device
is already in lock task mode, any changes you make to the lock task features
show immediately. Table 2 describes the UI features you can customize.

|                                                                  System UI feature                                                                   |                                                                                                                                                                                     Description                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`LOCK_TASK_FEATURE_HOME`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_HOME)                     | Shows the Home button. Enable for custom launchers---tapping an enabled Home button has no action unless you allowlist the default Android launcher.                                                                                                                                                                                                                                |
| [`LOCK_TASK_FEATURE_OVERVIEW`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_OVERVIEW)             | Shows the Overview button (tapping this button opens the [Recents](https://developer.android.com/guide/components/activities/recents) screen). If you enable this button, you must also enable the Home button.                                                                                                                                                                     |
| [`LOCK_TASK_FEATURE_GLOBAL_ACTIONS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_GLOBAL_ACTIONS) | Enables the global actions dialog that shows when long-pressing the power button. The only feature that's enabled when [setLockTaskFeatures()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskFeatures(android.content.ComponentName,%20int)) hasn't been called. A user typically can't power off the device if you disable this dialog. |
| [`LOCK_TASK_FEATURE_NOTIFICATIONS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_NOTIFICATIONS)   | Enables notifications for all apps. This shows notification icons in the status bar, heads-up notifications, and the expandable notification shade. If you enable this button, you must also enable the Home button. Tapping notification actions and buttons that open new panels, doesn't work in lock task mode.                                                                 |
| [`LOCK_TASK_FEATURE_SYSTEM_INFO`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_SYSTEM_INFO)       | Enables the status bar's system info area that contains indicators such as connectivity, battery, and sound and vibrate options.                                                                                                                                                                                                                                                    |
| [`LOCK_TASK_FEATURE_KEYGUARD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_KEYGUARD)             | Enables any lock screen that might be set on the device. Typically not suitable for devices with public users such as information kiosks or digital signage.                                                                                                                                                                                                                        |
| [`LOCK_TASK_FEATURE_NONE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_NONE)                     | Disables all the system UI features listed above.                                                                                                                                                                                                                                                                                                                                   |
[**Table 2**. Customizable system UI features in lock task mode]

A DPC can call
[`DevicePolicyManager.getLockTaskFeatures()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getLockTaskFeatures(android.content.ComponentName)) to get
the list of features available on a device when lock task mode is enabled. When
a device exits lock task mode, the user interface returns to the state mandated
by existing device policies.

## Block windows and overlays

When an app runs in lock task mode, other apps and background services can
create new windows that Android displays in front of the app in lock task mode.
Apps and services create these windows to show toasts, dialogs, and overlays to
the person using the device. Your DPC can prevent these by adding the
[`DISALLOW_CREATE_WINDOWS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CREATE_WINDOWS) user restriction.
The following example shows how you might do this in the
[`onLockTaskModeEntering()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onLockTaskModeEntering(android.content.Context,%20android.content.Intent,%20java.lang.String)) callback:  

### Kotlin

```kotlin
// Called just after entering lock task mode.
override fun onLockTaskModeEntering(context: Context, intent: Intent) {
    val dpm = getManager(context)
    val admin = getWho(context)

    dpm.addUserRestriction(admin, UserManager.DISALLOW_CREATE_WINDOWS)
}
```

### Java

```java
// Called just after entering lock task mode.
public void onLockTaskModeEntering(Context context, Intent intent) {
  DevicePolicyManager dpm = getManager(context);
  ComponentName admin = getWho(context);

  dpm.addUserRestriction(admin, UserManager.DISALLOW_CREATE_WINDOWS);
}
```

Your DPC can remove the user restriction when the device exits lock task mode.

## Additional resources

To learn more about dedicated devices, read the following documents:

- [Dedicated devices cookbook](https://developer.android.com/work/dpc/dedicated-devices/cookbook) with further examples to restrict the dedicated devices and enhance the user experience.
- [Dedicated devices overview](https://developer.android.com/work/dpc/dedicated-devices) is an overview of dedicated devices.
- [Manage multiple users](https://developer.android.com/work/dpc/dedicated-devices/multiple-users) explains how to share devices between users.