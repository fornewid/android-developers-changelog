---
title: https://developer.android.com/develop/background-work/services/fgs/handle-user-stopping
url: https://developer.android.com/develop/background-work/services/fgs/handle-user-stopping
source: md.txt
---

Starting in Android 13 (API level 33), users can complete a workflow from the
[notification drawer](https://developer.android.com/develop/ui/views/notifications#bar-and-drawer)
to stop an app that has an ongoing foreground services, regardless of that app's
target SDK version. This affordance, called the
*Task Manager*, shows a list of apps that are
currently running a foreground service.  
![At the bottom of the notification drawer is a button that indicates the
number of apps that are currently running in the background. When you press
this button, a dialog appears, which lists the names of different apps. The
Stop button is to the right of each app](https://developer.android.com/static/images/guide/components/fgs-manager.svg) **Figure 1.** Task Manager workflow on devices that run Android 13 or higher.

This list is labeled **Active apps** .
Next to each app is a **Stop** button. Figure 1 illustrates the
Task Manager workflow on a device that runs
Android 13.

When the user presses the **Stop** button next to your app in the
Task Manager, then the following actions occur:

- The system removes your app from memory. Therefore, your **entire app stops**, not just the running foreground service.
- The system removes your app's activity back stack.
- Any media playback stops.
- The notification associated with the foreground service is removed.
- Your app remains in history.
- Scheduled jobs execute at their scheduled time.
- Alarms go off at their scheduled time or time window.

| **Note:** The system doesn't send your app any callbacks when the user taps the **Stop** button. When your app starts back up, it's helpful to check for the [`REASON_USER_REQUESTED`](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_USER_REQUESTED) reason that's part of the `ApplicationExitInfo` API.

To test that your app behaves as expected while and after a user stops your
app, run the following ADB command in a terminal window:  

```bash
adb shell cmd activity stop-app PACKAGE_NAME
```