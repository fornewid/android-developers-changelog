---
title: https://developer.android.com/topic/performance/anrs/find-unresponsive-thread
url: https://developer.android.com/topic/performance/anrs/find-unresponsive-thread
source: md.txt
---

# Find the unresponsive thread

This document shows how to identify the unresponsive thread in an ANR stack dump. The unresponsive thread varies by type of ANR, as shown in the following table.

|                                                                                                                              ANR type                                                                                                                              |                                                                                                                                                                                                                                      Unresponsive thread                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input dispatch                                                                                                                                                                                                                                                     | Main thread                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Input dispatch no focused window                                                                                                                                                                                                                                   | Main thread. This type of ANR isn't usually caused by a blocked thread.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Broadcast receiver (synchronous)                                                                                                                                                                                                                                   | Thread running[onReceive()](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent)). This is the main thread unless a custom handler on a non-main thread is specified using[Context.registerReceiver](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20java.lang.String,%20android.os.Handler,%20int)). |
| Broadcast receiver (asynchronous)                                                                                                                                                                                                                                  | Check the code to see which thread or thread pool is responsible for doing the work to process the broadcast after[goAsync](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync())is called.                                                                                                                                                                                                                                                                    |
| Executing service timeout                                                                                                                                                                                                                                          | Main thread                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Foreground service start                                                                                                                                                                                                                                           | Main thread                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Content provider not responding                                                                                                                                                                                                                                    | Either: - Binder thread if ANR is caused by a slow content provider query. - Main thread if ANR is caused by a long app startup.                                                                                                                                                                                                                                                                                                                                                              |
| No response to[onStartJob](https://developer.android.com/reference/android/app/job/JobService#onStartJob(android.app.job.JobParameters))or[onStopJob](https://developer.android.com/reference/android/app/job/JobService#onStopJob(android.app.job.JobParameters)) | Main thread                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

Sometimes the thread is unresponsive due to a root cause in a different thread or process. The thread can be unresponsive due to waiting on the following:

- A lock held by a different thread.
- A slow binder call to a different process.

## Common causes of unresponsive threads

The following are common causes of unresponsive threads.

### Slow binder call

Although most binder calls are quick, the long tail can be very slow. This is more likely to happen if the device is loaded or the binder reply thread is slow, such as from lock contention, many incoming binder calls, or[hardware abstraction layer (HAL)](https://developer.android.com/guide/platform#hal)timeout.

You can solve this by moving synchronous binder calls to background threads wherever possible. If the call must happen on the main thread, find out why the call is slow. The best way to do this is from Perfetto traces.

Look for`BinderProxy.transactNative`or`Binderproxy.transact`in the stacks. This means a binder call is taking place. Following these two lines, you can see the binder API that is called. In the following example, the call is to`IAccessibilityManager.addClient`.  

    main tid=123

    ...
    android.os.BinderProxy.transactNative (Native method)
    android.os.BinderProxy.transact (BinderProxy.java:568)
    android.view.accessibility.IAccessibilityManager$Stub$Proxy.addClient (IAccessibilityManager.java:599)
    ...

### Many consecutive binder calls

Performing many consecutive binder calls in a tight loop can block a thread for a long period.

### A blocking I/O

Never perform blocking I/O on the main thread. This is an antipattern.

### Lock contention

If a thread is blocked when acquiring a lock, it can result in an ANR.

The following example shows the main thread is blocked when trying to acquire a lock:  

    main (tid=1) Blocked

    Waiting for com.example.android.apps.foo.BarCache (0x07d657b7) held by
    ptz-rcs-28-EDITOR_REMOTE_VIDEO_DOWNLOAD
    [...]
    at android.app.ActivityThread.handleStopActivity(ActivityThread.java:5412)
    [...]

The blocking thread is making a HTTP request to download a video:  

    ptz-rcs-28-EDITOR_REMOTE_VIDEO_DOWNLOAD (tid=110) Waiting

    at jdk.internal.misc.Unsafe.park(Native method:0)
    at java.util.concurrent.locks.LockSupport.park(LockSupport.java:211)
    at java.util.concurrent.locks.AbstractQueuedSynchronizer.acquire(AbstractQueuedSynchronizer.java:715)
    at java.util.concurrent.locks.AbstractQueuedSynchronizer.acquireSharedInterruptibly(AbstractQueuedSynchronizer.java:1047)
    at java.util.concurrent.CountDownLatch.await(CountDownLatch.java:230)
    at com.example.android.apps.foo.HttpRequest.execute(HttpRequest:136)
    at com.example.android.apps.foo$Task$VideoLoadTask.downloadVideoToFile(RequestExecutor:711)
    [...]

### Expensive frame

Rendering too many things in a single frame can cause the main thread to be unresponsive for the duration of the frame, such as the following:

- Rendering many unnecessary off-screen items.
- Using an inefficient algorithm, such as`O(n^2)`, when rendering many UI elements.

### Blocked by other component

If another component, such as a broadcast receiver, blocks the main thread for more than five seconds, it can cause input dispatch ANRs and serious jank.

Avoid doing any heavy work on the main thread in app components. Run broadcast receivers on a different thread wherever possible.