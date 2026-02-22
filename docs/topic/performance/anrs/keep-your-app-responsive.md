---
title: https://developer.android.com/topic/performance/anrs/keep-your-app-responsive
url: https://developer.android.com/topic/performance/anrs/keep-your-app-responsive
source: md.txt
---

# Keep your app responsive

![](https://developer.android.com/static/images/anr.png)

**Figure 1.**An ANR dialog displayed to the user.

This document describes how the Android system determines whether an app isn't responding and shows how to keep your app responsive.

No matter how well-written your code is, it's possible for your app to still feel sluggish, hang, freeze for significant periods, or take too long to process input. If your app is in the foreground and is unresponsive, the user gets an Application Not Responding (ANR) dialog, as shown in figure 1. The ANR dialog lets the user force quit the app. If the app isn't in the foreground, then it's silently stopped. It's critical to design responsiveness into your app to minimize ANR dialogs.

## ANR triggers

Generally, the system displays an ANR if an app can't respond to user input on the main thread---also known as the UI thread---preventing the system from processing incoming user input events.

For example, an ANR can occur if an app performs a blocking I/O operation, such as network access, on the UI thread. Another example is when an app spends too much time building an elaborate in-memory structure or computing the next move in a game on the UI thread.

In Android, app responsiveness is monitored by the[`ActivityManager`](https://developer.android.com/reference/android/app/ActivityManager)and[`WindowManager`](https://developer.android.com/reference/android/view/WindowManager)system services. Android displays the ANR dialog for an app when it detects one of the following conditions:

- No response to an input event---such as key press or screen tap events---within 5 seconds.
- A[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver)doesn't finish executing within 10 to 20 seconds, for foreground intents. For more information, see[Broadcast receiver timeout](https://developer.android.com/topic/performance/anrs/diagnose-and-fix-anrs#broadcast-receiver-anr).

## Avoid ANRs

The following are general tips to avoid ANRs. For more details about diagnosing and debugging different types of ANRs, see the other pages in this section.

- Keep the main thread unblocked at all times, and use threads strategically.

  - Don't perform blocking or long-running operations on the app's main thread. Instead, create a worker thread and do most of the work there.

  - Try to minimize any lock contention between the main thread and other threads.

  - Minimize any non-UI related work on the main thread, such as when handling broadcasts or running services. Any method that runs in the UI thread must do as little work as possible on that thread. In particular, activities must do as little as possible to set up in key lifecycle methods, such as`onCreate()`and`onResume()`. See[Background work overview](https://developer.android.com/guide/background)for more information about available solutions for scheduling work on a background thread and communicating back with the UI.

  - Be careful when sharing thread pools between components. Don't use the same threads for potentially long-blocking operations and time-sensitive tasks such as broadcast receiving.

  | **Note:** Because such threading usually is accomplished at the class level, you can think of responsiveness as a class problem. Compare this with basic code performance, which is a method-level concern.
- Keep app startup fast. Minimize slow or blocking operations in the app's startup code, such as methods run during dagger initialization.

- If you're using`BroadcastReceiver`, consider running broadcast receivers in a non-main thread using[`Context.registerReceiver`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20java.lang.String,%20android.os.Handler,%20int)). For more information, see[ANRs in BroadcastReceiver](https://developer.android.com/topic/performance/anrs/keep-your-app-responsive#anrs-in-broadcast-receiver).

  - If you use[`goAsync()`](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync()), make sure[`PendingResult.finish`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.PendingResult#finish)is called quickly before the ANR timeout.

## ANRs in BroadcastReceiver

`BroadcastReceiver`execution time is constrained because broadcast receivers are meant to do small, discrete amounts of work in the background, such as saving a setting or registering a[`Notification`](https://developer.android.com/reference/android/app/Notification). So, as with other methods called in the UI thread, apps must avoid potentially long-running operations or calculations in a broadcast receiver. Instead of performing long-running tasks via the UI thread, perform them in the background for later execution. See[Background work overview](https://developer.android.com/guide/background)for more information about possible solutions.

Another common issue with`BroadcastReceiver`objects occurs when they execute too frequently. Frequent background execution can reduce the amount of memory available to other apps. For more information about how to enable and disable`BroadcastReceiver`objects efficiently, see[Broadcasts overview](https://developer.android.com/guide/components/broadcasts).
| **Tip:** You can use[`StrictMode`](https://developer.android.com/reference/android/os/StrictMode)to help find potentially lengthy operations such as network or database operations that you might accidentally be doing on your main thread.

## Reinforce responsiveness

Generally, 100 to 200ms is the threshold beyond which users perceive slowness in an app. Here are additional tips for making your app seem responsive to users:

- If your app is doing work in the background in response to user input, show that progress is being made, such as with a[`ProgressBar`](https://developer.android.com/reference/android/widget/ProgressBar)in your UI.

- For games specifically, do calculations for moves in a worker thread.

- If your app has a time-consuming initial setup phase, consider showing a[splash screen](https://developer.android.com/develop/ui/views/launch/splash-screen)or rendering the main view as quickly as possible. Indicate that loading is in progress and fill the information asynchronously. In either case, we recommend indicating somehow that progress is being made, so that the user doesn't perceive that the app is frozen.

- Use performance tools such as[Perfetto](https://developer.android.com/topic/performance/tracing)and[CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler)to determine bottlenecks in your app's responsiveness.