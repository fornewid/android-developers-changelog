---
title: https://developer.android.com/about/versions/14/changes/schedule-exact-alarms
url: https://developer.android.com/about/versions/14/changes/schedule-exact-alarms
source: md.txt
---

# Schedule exact alarms are denied by default

Exact alarms are meant for user-intentioned notifications or actions that need to happen at a precise time.

[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM), the permission introduced in Android 12 for apps to schedule exact alarms, is**no longer being pre-granted to most newly installed apps targeting Android 13 and higher**(will be set to denied by default). If the user transfers app data to a device running Android 14 through a backup-and-restore operation, the permission will still be denied. If an existing app already has this permission, it'll be pre-granted when the device upgrades to Android 14.

The[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)permission is required to initiate exact alarms via the following APIs or a`SecurityException`will be thrown:

- [`setExact()`](https://developer.android.com/reference/android/app/AlarmManager#setExact(int,%20long,%20android.app.PendingIntent))
- [`setExactAndAllowWhileIdle()`](https://developer.android.com/reference/android/app/AlarmManager#setExactAndAllowWhileIdle(int,%20long,%20android.app.PendingIntent))
- [`setAlarmClock()`](https://developer.android.com/reference/android/app/AlarmManager#setAlarmClock(android.app.AlarmManager.AlarmClockInfo,%20android.app.PendingIntent))

| **Note:** If the exact alarm is set using an[`OnAlarmListener`](https://developer.android.com/reference/android/app/AlarmManager.OnAlarmListener)object, like in the[`setExact`](https://developer.android.com/reference/android/app/AlarmManager#setExact(int,%20long,%20java.lang.String,%20android.app.AlarmManager.OnAlarmListener,%20android.os.Handler))API, the`SCHEDULE_EXACT_ALARM`permission isn't required.

Existing best-practices for the[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)permission still apply, including the following:

- Check the permission with[`canScheduleExactAlarms()`](https://developer.android.com/reference/android/app/AlarmManager#canScheduleExactAlarms())before scheduling exact alarms.
- Set up your app to listen and properly react to the foreground broadcast[`AlarmManager.ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED`](https://developer.android.com/reference/android/app/AlarmManager#ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED), which the system sends when the user grants the permission.

## Affected apps

If a device is running Android 14 or higher, this change will affect a newly installed app that has the following characteristics:

- Targets Android 13 (API level 33) or higher.
- Declares the[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)permission in the manifest.
- Doesn't fall under an[exemption](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms#exemptions)or[pre-grant](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms#pre-grant)scenario.
- **Isn't**a calendar or alarm clock app.

## Calendar and alarm clock apps should declare USE_EXACT_ALARM

[Calendar or alarm clock apps](https://support.google.com/googleplay/android-developer/answer/12253906#exact_alarm_preview)need to send calendar reminders, wake-up alarms, or alerts when the app is no longer running. These apps can request the[`USE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)normal permission. The`USE_EXACT_ALARM`permission will be granted on install, and apps holding this permission will be able to schedule exact alarms just like apps with the[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)permission.
| **Note:** Apps will not be able to publish a version of their app with this permission in the manifest unless they qualify based on the[policy language](https://support.google.com/googleplay/android-developer/answer/12253906#exact_alarm_preview).

## Use cases that might not require exact alarms

Because the[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)permission is now denied by default and the permission grant process requires extra steps from users, developers are strongly encouraged to evaluate their use cases and determine if exact alarms still make sense for their use cases.

The following list shows common workflows that may not require an exact alarm:

Scheduling repeated work during the lifetime of your app
:   The[`set()`](https://developer.android.com/reference/android/app/AlarmManager#set(int,%20long,%20android.app.PendingIntent))method is useful if the task needs to keep real-time constraints in mind, such as going off at 2:00 PM tomorrow or in 30 minutes. Otherwise, it's recommended to use the[`postAtTime()`](https://developer.android.com/reference/android/os/Handler#postAtTime(java.lang.Runnable,%20long))or[`postDelayed()`](https://developer.android.com/reference/android/os/Handler#postDelayed(java.lang.Runnable,%20long))methods instead.

Scheduled background work, such as updating your app and uploading logs
:   `WorkManager`provides a way to[schedule timing-sensitive periodic work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#flexible_run_intervals). You can provide a repeat interval and flexInterval (15 minutes minimum) to define granular runtime for the work.

Need alarm to go off at an approximate time while system is in idle state
:   Use an inexact alarm. Specifically, call[`setAndAllowWhileIdle()`](https://developer.android.com/reference/android/app/AlarmManager#setAndAllowWhileIdle(int,%20long,%20android.app.PendingIntent)).

User-specified action that should happen after a specific time
:   Use an inexact alarm. Specifically, call[`set()`](https://developer.android.com/reference/android/app/AlarmManager#set(int,%20long,%20android.app.PendingIntent)).

User-specified action that can happen within a time window
:   Use an inexact alarm. Specifically, call[`setWindow()`](https://developer.android.com/reference/android/app/AlarmManager#setWindow(int,%20long,%20long,%20android.app.PendingIntent)). Note that the smallest allowed window length is 10 minutes.

## Migration steps to continue using exact alarms

At a minimum, apps must check to see if they have the permission before scheduling exact alarms. If apps don't have the permission, they must request it from the user by invoking an intent.

This is the same as the standard workflow for[requesting a special permission](https://developer.android.com/training/permissions/requesting-special):

1. Apps should call[`AlarmManager.canScheduleExactAlarms()`](https://developer.android.com/reference/android/app/AlarmManager#canScheduleExactAlarms())to confirm that it has the appropriate permission.
2. If the app doesn't have the permission, invoke an intent that includes the[`ACTION_REQUEST_SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_SCHEDULE_EXACT_ALARM), along with the app's package name, to ask users to grant the permission.

   [Check the user's decision](https://developer.android.com/reference/android/app/AlarmManager#set(int,%20long,%20android.app.PendingIntent))in the[`onResume()`](https://developer.android.com/guide/components/activities/activity-lifecycle#onresume)method of your app.
3. Listen for the[`AlarmManager.ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED`](https://developer.android.com/reference/android/app/AlarmManager#ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED)broadcasts that are sent if the user grants the permission.

4. If the user granted the permission to your app, your app can set exact alarms. If the user denied the permission instead,[gracefully degrade your app experience](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms#gracefully-degrade)so that it provides functionality to the user without the information that's protected by that permission.

The following code snippet demonstrates how to check for the`SCHEDULE_EXACT_ALARM`permission:  

    val alarmManager: AlarmManager = context.getSystemService<AlarmManager>()!!
    when {
       // If permission is granted, proceed with scheduling exact alarms.
       alarmManager.canScheduleExactAlarms() -> {
           alarmManager.setExact(...)
       }
       else -> {
           // Ask users to go to exact alarm page in system settings.
           startActivity(Intent(ACTION_REQUEST_SCHEDULE_EXACT_ALARM))
       }
    }

Sample code to check the permission and handle the user's decisions in`onResume()`:  

    override fun onResume() {
       ...  
       if (alarmManager.canScheduleExactAlarms()) {
           // Set exact alarms.
           alarmManager.setExact(...)
       }
       else {
           // Permission not yet approved. Display user notice and revert to a fallback  
           // approach.
           alarmManager.setWindow(...)
       }
    }

### Gracefully degrade on permission denial

Some users will refuse to grant the permission. In this scenario, we recommend apps to gracefully degrade the experience and still strive to provide the best possible fallback user experience by identifying their[use cases](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms#use-cases).

## Exemptions

The following types of apps are always allowed to call the[`setExact()`](https://developer.android.com/reference/android/app/AlarmManager#setExact(int,%20long,%20android.app.PendingIntent))or[`setExactAndAllowWhileIdle()`](https://developer.android.com/reference/android/app/AlarmManager#setExactAndAllowWhileIdle(int,%20long,%20android.app.PendingIntent))methods:

- Apps signed with the platform certificate.
- Privileged apps.
- Apps that are on the power allowlist (if your app fits the requirements, you can[request this](https://developer.android.com/training/monitoring-device-state/doze-standby#exemption-cases)using the`ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS`intent action).

## Pre-grants

- Role holders of`SYSTEM_WELLBEING`will be pre-granted[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM).

## Testing guidelines

To test this change, disable the**Alarms \& reminders** permission for your app from the**Special app access** page in system settings (**Settings \> Apps \> Special app access \> Alarms \& reminders**) and observe the behavior of your app.