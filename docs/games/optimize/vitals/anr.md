---
title: https://developer.android.com/games/optimize/vitals/anr
url: https://developer.android.com/games/optimize/vitals/anr
source: md.txt
---

When the UI thread of an Android app is blocked for too long, an "Application
Not Responding" (ANR) error is triggered. If the app is in the foreground, the
system displays a dialog to the user, as shown in figure 1. The ANR dialog gives
the user the opportunity to force quit the app.

![Figure 1. ANR dialog displayed to the user](https://developer.android.com/static/topic/performance/images/anr-example-framed.png)

**Figure 1.** ANR dialog displayed to the user

ANRs are a problem because the app's main thread, which is responsible for
updating the UI, can't process user input events or draw, causing frustration to
the user. For more information on the app's main thread, see [Processes and
threads](https://developer.android.com/guide/components/processes-and-threads).

An ANR is triggered for your app when one of the following conditions occur:

- **Input dispatching timed out:** If your app has not responded to an input event (such as key press or screen touch) within 5 seconds.
- **Executing service:** If a service declared by your app cannot finish executing `Service.onCreate()` and `Service.onStartCommand()`/`Service.onBind()` within a few seconds.
- **Service.startForeground() not called:** If your app uses `Context.startForegroundService()` to start a new service in the foreground, but the service then does not call `startForeground()` within 5 seconds.
- **Broadcast of intent:** If a [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) hasn't finished executing within a set amount of time. If the app has any activity in the foreground, this timeout is 5 seconds.
- **JobScheduler interactions:** If a [`JobService`](https://developer.android.com/reference/android/app/job/JobService) does not return from `JobService.onStartJob()` or `JobService.onStopJob()` within a few seconds, or if a [user-initiated job](https://developer.android.com/reference/android/app/job/JobParameters#isUserInitiatedJob()) starts and your app doesn't call `JobService.setNotification()` within a few seconds after `JobService.onStartJob()` was called. For apps targeting Android 13 and below, the ANRs are silent and not reported to the app. For apps targeting Android 14 and above, the ANRs are explicit and are reported to the app.

If your app is experiencing ANRs, you can use the guidance in this article to
diagnose and fix the problem.

## Detect the problem

If you have already published your app, you can use
Android vitals to see information on ANRs for your app. You can use other
tools to detect ANRs in the field but note that 3P tools cannot report ANRs on
older versions of Android (Android 10 and below), unlike Android vitals.

### Android vitals

Android vitals can help you monitor and improve your app's ANR rate.
Android vitals measures several ANR rates:

- **ANR rate:** The percentage of your daily active users who experienced any type of ANR.
- **User-perceived ANR rate:** The percentage of your daily active users who experienced at least one *user-perceived ANR* . Currently only ANRs of type `Input dispatching timed out` are considered user-perceived.
- **Multiple ANR rate:** The percentage of your daily active users who experienced at least two ANRs.

A *daily active user* is a unique user who uses your app
on a single day on a single device, potentially over multiple sessions.
If a user uses your app on more than one device in a single day,
each device will contribute to the number of active users for that day.
If multiple users use the same device in a single day,
this is counted as one active user.

User-perceived ANR rate is a *core vital* meaning that it affects the
discoverability of your app on Google Play. It is important because the ANRs it
counts always occur when the user is engaged with the app, causing the most
disruption.

Play has defined two **bad behavior thresholds** on this metric:

- **Overall bad behavior threshold:** At least 0.47% of daily active users experience a user-perceived ANR, across all device models.
- **Per-device bad behavior threshold:** At least 8% of daily users experience a user-perceived ANR, **for a single device model**.

If your app exceeds the overall bad behavior threshold, it is likely to be
less discoverable on all devices. If your app exceeds the per-device bad
behavior threshold on some devices, it is likely to be less discoverable on
those devices, and a warning may be shown on your store listing.

Android vitals can alert you, via the
[Play Console](https://play.google.com/console/),
when your app is exhibiting excessive ANRs.

For information on how Google Play collects Android vitals data, see the
[Play Console](https://support.google.com/googleplay/android-developer/answer/7385505)
documentation.

## Diagnose ANRs

There are some common patterns to look for when diagnosing ANRs:

- The app is doing slow operations involving I/O on the main thread.
- The app is doing a long calculation on the main thread.
- The main thread is doing a synchronous binder call to another process, and that other process is taking a long time to return.
- The main thread is blocked waiting for a synchronized block for a long operation that is happening on another thread.
- The main thread is in a deadlock with another thread, either in your process or via a binder call. The main thread is not just waiting for a long operation to finish, but is in a deadlock situation. For more information, see [Deadlock](https://en.wikipedia.org/wiki/Deadlock) on Wikipedia.

The following techniques can help you determine the cause of your ANRs.

#### HealthStats

[`HealthStats`](https://developer.android.com/reference/android/os/health/HealthStats) provides metrics about
the health of an application by capturing total user and system time, CPU time,
network, radio stats, screen on/off time, and wake up alarms. This can
help in measuring overall CPU usage and battery drainage.

#### Debug

[`Debug`](https://developer.android.com/reference/android/os/Debug) helps to inspect Android applications
during development, including tracing and allocation counts to identify jank
and lag in the apps. You can also use `Debug` to get runtime and native memory
counters, and memory metrics that can help in identifying the memory footprint
of a particular process.

#### ApplicationExitInfo

[`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo) is available
on Android 11 (API level 30) or higher, and provides information about the
reason for application exit. This includes ANRs, low memory, app crashes,
excessive CPU usage, user interruptions, system interruptions or runtime
permission changes.

#### Strict mode

Using [`StrictMode`](https://developer.android.com/reference/android/os/StrictMode) helps you find
accidental I/O operations on the main thread while you're developing your app.
You can use [`StrictMode`](https://developer.android.com/reference/android/os/StrictMode)
at the application or activity level.

### Enable background ANR dialogs

Android shows ANR dialogs for apps that take too long to process the broadcast
message only if **Show all ANRs** is enabled in the device's **Developer
options**. For this reason, background ANR dialogs are not always displayed to
the user, but the app could still be experiencing performance issues.

### Traceview

You can use Traceview to get a trace of your running app while going through the
use cases and identify the places where the main thread is busy. For information
about how to use Traceview, see [Profiling with Traceview and
dmtracedump](https://developer.android.com/studio/profile/traceview).

### Pull a traces file

Android stores trace information when it experiences an ANR. On older OS
releases, there's a single `/data/anr/traces.txt` file on the device.
On newer OS releases, there are multiple `/data/anr/anr_*` files.
You can access ANR traces from a device or emulator by using
[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb) as root:

    adb root
    adb shell ls /data/anr
    adb pull /data/anr/<filename>

You can capture a bug report from a physical device by using either the Take bug
report developer option on the device, or the adb bugreport command on your
development machine. For more information, see [Capture and read bug
reports](https://developer.android.com/studio/debug/bug-report).

## Fix the problems

After you have identified the problem, you can use the tips in this section to
fix commonly found problems.

### Slow code on the main thread

Identify the places in your code where the app's main thread is busy for more
than 5 seconds. Look for the suspicious use cases in your app and try to
reproduce the ANR.

For example, figure 2 shows a Traceview timeline where the main thread is busy
for more than 5 seconds.

![Figure 2. Traceview timeline showing a busy main
thread](https://developer.android.com/static/topic/performance/images/trace-work-on-main.png)

**Figure 2.** Traceview timeline showing a busy main thread

Figure 2 shows that most of the offending code happens in the
[`onClick(View)`](https://developer.android.com/reference/android/view/View.OnClickListener#onClick(android.view.View))
handler, as shown in the following code example:

### Kotlin

```kotlin
override fun onClick(v: View) {
    // This task runs on the main thread.
    BubbleSort.sort(data)
}
```

### Java

```java
@Override
public void onClick(View view) {
    // This task runs on the main thread.
    BubbleSort.sort(data);
}
```

In this case, you should move the work that runs in the main thread to a worker
thread. The Android Framework includes classes that can help to move the task
to a worker thread. See [Worker
threads](https://developer.android.com/guide/components/processes-and-threads#WorkerThreads) for more
information.

### IO on the main thread

Executing IO operations on the main thread is a common cause of slow operations
on the main thread, which can cause ANRs. It's recommended to move all IO
operations to a worker thread, as shown in the previous section.

Some examples of IO operations are network and storage operations. For more
information, see [Performing network
operations](https://developer.android.com/training/basics/network-ops) and [Saving
data](https://developer.android.com/training/basics/data-storage).

### Lock contention

In some scenarios, the work that causes the ANR is not directly executed on the
app's main thread. If a worker thread holds a lock on a resource that the main
thread requires to complete its work, then an ANR might happen.

For example, figure 3 shows a Traceview timeline where most of the work is
performed on a worker thread.

![Figure 3. Traceview timeline that shows the work being executed on a worker
thread](https://developer.android.com/static/topic/performance/images/trace-locked-thread.png)

**Figure 3.** Traceview timeline that shows the work being executed on a worker
thread

But if your users are still experiencing ANRs, you should look at the status of
the main thread in Android Device Monitor. Usually, the main thread is in the
[`RUNNABLE`](https://developer.android.com/reference/java/lang/Thread.State#RUNNABLE)
state if it's ready to update the UI and is generally responsive.

But if the main thread can't resume execution, then it's in the
[`BLOCKED`](https://developer.android.com/reference/java/lang/Thread.State#BLOCKED) state
and can't respond to events. The state shows on Android Device Monitor as
*Monitor* or *Wait*, as shown in figure 5.

![Figure 4. Main thread in the Monitor
status](https://developer.android.com/static/topic/performance/images/trace-monitor-thread.png)

**Figure 4.** Main thread in the Monitor status

The following trace shows an app's main thread that is blocked waiting for a
resource:

    ...
    AsyncTask #2" prio=5 tid=18 Runnable
      | group="main" sCount=0 dsCount=0 obj=0x12c333a0 self=0x94c87100
      | sysTid=25287 nice=10 cgrp=default sched=0/0 handle=0x94b80920
      | state=R schedstat=( 0 0 0 ) utm=757 stm=0 core=3 HZ=100
      | stack=0x94a7e000-0x94a80000 stackSize=1038KB
      | held mutexes= "mutator lock"(shared held)
      at com.android.developer.anrsample.BubbleSort.sort(BubbleSort.java:8)
      at com.android.developer.anrsample.MainActivity$LockTask.doInBackground(MainActivity.java:147)
      - locked <0x083105ee> (a java.lang.Boolean)
      at com.android.developer.anrsample.MainActivity$LockTask.doInBackground(MainActivity.java:135)
      at android.os.AsyncTask$2.call(AsyncTask.java:305)
      at java.util.concurrent.FutureTask.run(FutureTask.java:237)
      at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:243)
      at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1133)
      at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:607)
      at java.lang.Thread.run(Thread.java:761)
    ...

Reviewing the trace can help you locate the code that blocks the main thread.
The following code is responsible for holding the lock that blocks the main
thread in the previous trace:

### Kotlin

```kotlin
override fun onClick(v: View) {
    // The worker thread holds a lock on lockedResource
    LockTask().execute(data)

    synchronized(lockedResource) {
        // The main thread requires lockedResource here
        // but it has to wait until LockTask finishes using it.
    }
}

class LockTask : AsyncTask<Array<Int>, Int, Long>() {
    override fun doInBackground(vararg params: Array<Int>): Long? =
            synchronized(lockedResource) {
                // This is a long-running operation, which makes
                // the lock last for a long time
                BubbleSort.sort(params[0])
            }
}
```

### Java

```java
@Override
public void onClick(View v) {
    // The worker thread holds a lock on lockedResource
   new LockTask().execute(data);

   synchronized (lockedResource) {
       // The main thread requires lockedResource here
       // but it has to wait until LockTask finishes using it.
   }
}

public class LockTask extends AsyncTask<Integer[], Integer, Long> {
   @Override
   protected Long doInBackground(Integer[]... params) {
       synchronized (lockedResource) {
           // This is a long-running operation, which makes
           // the lock last for a long time
           BubbleSort.sort(params[0]);
       }
   }
}
```

Another example is an app's main thread that is waiting for a result from a
worker thread, as shown in the following code. Note that using `wait()` and
`notify()` is not a recommended pattern in Kotlin, which has its own mechanisms
for handling concurrency. When using Kotlin, you should use Kotlin-specific
mechanisms if possible.

### Kotlin

```kotlin
fun onClick(v: View) {
    val lock = java.lang.Object()
    val waitTask = WaitTask(lock)
    synchronized(lock) {
        try {
            waitTask.execute(data)
            // Wait for this worker thread's notification
            lock.wait()
        } catch (e: InterruptedException) {
        }
    }
}

internal class WaitTask(private val lock: java.lang.Object) : AsyncTask<Array<Int>, Int, Long>() {
    override fun doInBackground(vararg params: Array<Int>): Long? {
        synchronized(lock) {
            BubbleSort.sort(params[0])
            // Finished, notify the main thread
            lock.notify()
        }
    }
}
```

### Java

```java
public void onClick(View v) {
   WaitTask waitTask = new WaitTask();
   synchronized (waitTask) {
       try {
           waitTask.execute(data);
           // Wait for this worker thread's notification
           waitTask.wait();
       } catch (InterruptedException e) {}
   }
}

class WaitTask extends AsyncTask<Integer[], Integer, Long> {
   @Override
   protected Long doInBackground(Integer[]... params) {
       synchronized (this) {
           BubbleSort.sort(params[0]);
           // Finished, notify the main thread
           notify();
       }
   }
}
```

There are some other situations that can block the main thread, including
threads that use [`Lock`](https://developer.android.com/reference/java/util/concurrent/locks/Lock),
[`Semaphore`](https://developer.android.com/reference/java/util/concurrent/Semaphore),
as well as a resource pool (such as a pool of database connections)
or other mutual exclusion (mutex) mechanisms.

You should evaluate the locks that your app holds on resources in general, but
if you want to avoid ANRs, then you should look at the locks held for resources
required by the main thread.

Make sure that the locks are held for the least amount of time, or even better,
evaluate whether the app needs the hold in the first place. If you are using the
lock to determine when to update UI based on the processing of a worker thread,
use mechanisms such as
[`onProgressUpdate()`](https://developer.android.com/reference/android/os/AsyncTask#onProgressUpdate(Progress...))
and
[`onPostExecute()`](https://developer.android.com/reference/android/os/AsyncTask#onPostExecute(Result))
to communicate between the worker and main threads.

### Deadlocks

A deadlock occurs when a thread enters a waiting state because a required
resource is held by another thread, which is also waiting for a resource held by
the first thread. If the app's main thread is in this situation, ANRs are likely
to happen.

Deadlocks are a well-studied phenomenon in computer science, and there are
deadlock prevention algorithms that you can use to avoid deadlocks.

For more information, see [Deadlock](https://en.wikipedia.org/wiki/Deadlock) and
[Deadlock prevention
algorithms](https://en.wikipedia.org/wiki/Deadlock_prevention_algorithms) on
Wikipedia.

### Slow broadcast receivers

Apps can respond to broadcast messages, such as enabling or disabling airplane
mode or a change in connectivity status, by means of broadcast receivers. An ANR
occurs when an app takes too long to process the broadcast message.

An ANR occurs in the following cases:

- A broadcast receiver hasn't finished executing its [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent)) method within a considerable amount of time.
- A broadcast receiver calls [`goAsync()`](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync()) and fails to call [`finish()`](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult#finish()) on the [`PendingResult`](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult) object.

Your app should only perform short operations in the
[`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
method of a
[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver).
However, if your app requires more complex
processing as a result of a broadcast message you should defer the task to an
[`IntentService`](https://developer.android.com/reference/android/app/IntentService).

You can use tools like Traceview to identify if your broadcast receiver executes
long-running operations on the app's main thread. For example, figure 6 shows
the timeline of a broadcast receiver that processes a message on the main thread
for approximately 100 seconds.

![Figure 5. Traceview timeline showing the `BroadcastReceiver` work on the main
thread](https://developer.android.com/static/topic/performance/images/trace-work-on-broadcast.png)

**Figure 5.** Traceview timeline showing the `BroadcastReceiver` work on the
main thread

This behavior can be caused by executing long-running operations on the
[`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
method of the
[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver),
as shown in the following example:

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    // This is a long-running operation
    BubbleSort.sort(data)
}
```

### Java

```java
@Override
public void onReceive(Context context, Intent intent) {
    // This is a long-running operation
    BubbleSort.sort(data);
}
```

In situations like these, it's recommended to move the long-running operation to
an [`IntentService`](https://developer.android.com/reference/android/app/IntentService) because it uses
a worker thread to execute its work. The following code shows how to use an
[`IntentService`](https://developer.android.com/reference/android/app/IntentService) to process a
long-running operation:

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    Intent(context, MyIntentService::class.java).also { intentService ->
        // The task now runs on a worker thread.
        context.startService(intentService)
    }
}

class MyIntentService : IntentService("MyIntentService") {
    override fun onHandleIntent(intent: Intent?) {
        BubbleSort.sort(data)
    }
}
```

### Java

```java
@Override
public void onReceive(Context context, Intent intent) {
    // The task now runs on a worker thread.
    Intent intentService = new Intent(context, MyIntentService.class);
    context.startService(intentService);
}

public class MyIntentService extends IntentService {
   @Override
   protected void onHandleIntent(@Nullable Intent intent) {
       BubbleSort.sort(data);
   }
}
```

As a result of using the
[`IntentService`](https://developer.android.com/reference/android/app/IntentService), the long-running
operation is executed on a worker thread instead of the main thread. Figure 7
shows the work deferred to the worker thread in the Traceview timeline.

![Figure 6. Traceview timeline showing the broadcast message processed on a
worker thread](https://developer.android.com/static/topic/performance/images/trace-work-on-intent-service.png)

**Figure 6.** Traceview timeline showing the broadcast message processed on a
worker thread

Your broadcast receiver can use
[`goAsync()`](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync())
to signal the system that it needs more time to process the message. However,
you should call
[`finish()`](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult#finish())
on the
[`PendingResult`](https://developer.android.com/reference/android/content/BroadcastReceiver.PendingResult)
object. The following example shows how to call finish() to let the system
recycle the broadcast receiver and avoid an ANR:

### Kotlin

```kotlin
val pendingResult = goAsync()

object : AsyncTask<Array<Int>, Int, Long>() {
    override fun doInBackground(vararg params: Array<Int>): Long? {
        // This is a long-running operation
        BubbleSort.sort(params[0])
        pendingResult.finish()
        return 0L
    }
}.execute(data)
```

### Java

```java
final PendingResult pendingResult = goAsync();
new AsyncTask<Integer[], Integer, Long>() {
   @Override
   protected Long doInBackground(Integer[]... params) {
       // This is a long-running operation
       BubbleSort.sort(params[0]);
       pendingResult.finish();
   }
}.execute(data);
```

However, moving the code from a slow broadcast receiver to another thread and
using [`goAsync()`](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync())
won't fix the ANR if the broadcast is in the background.
The ANR timeout still applies.

### GameActivity

The [`GameActivity`](https://developer.android.com/games/agdk/game-activity) library has reduced ANRs in
[case studies](https://developer.android.com/stories/games/cat-daddy-agdk) of games and apps that are written
in C or C++. If you replace your existing native activity with `GameActivity`,
you can reduce UI thread blocking and prevent some ANRs from happening.

For more information about ANRs, see
[Keeping your app responsive](https://developer.android.com/training/articles/perf-anr). For more
information about threads, see
[Threading performance](https://developer.android.com/topic/performance/threads).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Excessive wakeups](https://developer.android.com/topic/performance/vitals/wakeup)