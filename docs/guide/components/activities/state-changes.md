---
title: https://developer.android.com/guide/components/activities/state-changes
url: https://developer.android.com/guide/components/activities/state-changes
source: md.txt
---

# Activity state changes

Different events, some user-triggered and some system-triggered, can cause an[`Activity`](https://developer.android.com/reference/android/app/Activity)to transition from one state to another. This document describes some common cases in which such transitions happen and how to handle those transitions.

For more information about activity states, see[The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle). To learn about how the[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)class can help you manage the activity lifecycle, see the[ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel).

## Configuration change occurs

There are a number of events that can trigger a configuration change. Perhaps the most prominent example is a change between portrait and landscape orientations. Other cases that can cause configuration changes include changes to language settings or input device.

When a configuration change occurs, the activity is destroyed and recreated. This triggers the following callbacks in the original activity instance:

1. [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause())
2. [`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop())
3. [`onDestroy()`](https://developer.android.com/reference/android/app/Activity#onDestroy())

A new instance of the activity is created, and the following callbacks are triggered:

1. [`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))
2. [`onStart()`](https://developer.android.com/reference/android/app/Activity#onStart())
3. [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume())

Use a combination of`ViewModel`instances, the`onSaveInstanceState()`method, or persistent local storage to preserve an activity's UI state across configuration changes. Deciding how to combine these options depends on the complexity of your UI data, use cases for your app, and consideration of the speed of retrieval versus memory usage. For more information about saving your activity UI state, see[Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).

### Handle multi-window cases

When an app enters multi-window mode, available in Android 7.0 (API level 24)and higher, the system notifies the running activity of a configuration change, thus going through the lifecycle transitions described previously.

This behavior also occurs if an app already in multi-window mode gets resized. Your activity can handle the configuration change itself, or it can allow the system to destroy the activity and recreate it with the new dimensions.

For more information about the multi-window lifecycle, see the explanation of the[multi-window lifecycle](https://developer.android.com/guide/topics/ui/multi-window#lifecycle)in the[Multi-window support](https://developer.android.com/guide/topics/ui/multi-window)page.

In multi-window mode, although there are two apps that are visible to the user, only the one the user is interacting with is in the foreground and has focus. That activity is in the Resumed state, while the app in the other window is in the Paused state.

When the user switches from app A to app B, the system calls[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause())on app A and[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume())on app B. It switches between these two methods each time the user toggles between apps.

For more details about multi-window mode, refer to[Multi-window support](https://developer.android.com/guide/topics/ui/multi-window).

## Activity or dialog appears in foreground

If a new activity or dialog appears in the foreground, taking focus and partially covering the activity in progress, the covered activity loses focus and enters the Paused state. Then, the system calls[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause())on it.

When the covered activity returns to the foreground and regains focus, the system calls[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()).

If a new activity or dialog appears in the foreground, taking focus and completely covering the activity in progress, the covered activity loses focus and enters the Stopped state. The system then, in rapid succession, calls`onPause()`and[`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()).

When the same instance of the covered activity returns to the foreground, the system calls[`onRestart()`](https://developer.android.com/reference/android/app/Activity#onRestart()),[`onStart()`](https://developer.android.com/reference/android/app/Activity#onStart()), and`onResume()`on the activity. If it is a new instance of the covered activity that comes to the background, the system does not call`onRestart()`, only`onStart()`and`onResume()`.
| **Note:** When the user taps the Overview or Home button, the system behaves as if the current activity has been completely covered.

## User taps or gestures Back

If an activity is in the foreground and the user taps or gestures Back, the activity transitions through the[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()),[`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()), and[`onDestroy()`](https://developer.android.com/reference/android/app/Activity#onDestroy())callbacks. The activity is destroyed and removed from the back stack.
| **Note:** If the activity is a root launcher activity, the system handles the event differently depending on the version of Android that the device is running. For more information, see[Back tap behavior for root launcher activities](https://developer.android.com/guide/components/activities/tasks-and-back-stack#back-press-behavior).

By default, the[`onSaveInstanceState()`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle))callback does not fire in this case. This behavior assumes the user taps Back with no expectation of returning to the same instance of the activity.

However, you can override the[`onBackPressed()`](https://developer.android.com/reference/android/app/Activity#onBackPressed())method to implement custom behavior, such as displaying a dialog that asks the user to confirm that they want to exit your app.

If you override the`onBackPressed()`method, we highly recommend that you still invoke`super.onBackPressed()`from your overridden method. Otherwise the system Back behavior might be jarring to the user.

## System kills app process

If an app is in the background and the system needs to free up memory for a foreground app, the system can kill the background app. When the system kills an app, there is no guarantee that`onDestroy()`is called in the app.

To learn more about how the system decides which processes to destroy, read[Activity state and ejection from memory](https://developer.android.com/guide/components/activities/activity-lifecycle#asem)and[Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle).

To learn how to save your activity UI state when the system kills your app process, see[Saving and restoring transient UI state](https://developer.android.com/guide/components/activities/activity-lifecycle#saras).