---
title: https://developer.android.com/games/engines/unity/unity-anrs-list
url: https://developer.android.com/games/engines/unity/unity-anrs-list
source: md.txt
---

Unity ANRs happen for a variety of reasons. Most common ANRs are caused by misuse of Android and Unity components and their miscommunication.

## WebView

[`WebView`](https://developer.android.com/reference/android/webkit/WebView)is an Android class that displays web pages. Third-party[SDKs](https://en.wikipedia.org/wiki/Software_development_kit)(such as ads) use`WebView`to display dynamic web content in activities other than the`UnityPlayerActivity`. ANRs occur when third-party SDKs misuse`WebView`.

### Stack trace

The stack trace is your first recourse for understanding the cause of the ANR.  

    /data/app/~~p-0ksfCD6bF6Sdq6kpVePg==/com.google.android.webview-5YQZOqKbbqp-uoLY6WYnTw==/base.apk!libmonochrome.so
      at J.N.Mhc_M_H$ (Native method)
      at org.chromium.components.viz.service.frame_sinks.ExternalBeginFrameSourceAndroid.doFrame (chromium-TrichromeWebViewGoogle.aab-stable-579013831:60)
      at android.view.Choreographer$CallbackRecord.run (Choreographer.java:1054)
      at android.view.Choreographer.doCallbacks (Choreographer.java:878)
      at android.view.Choreographer.doFrame (Choreographer.java:807)
      at android.view.Choreographer$FrameDisplayEventReceiver.run (Choreographer.java:1041)
      at android.os.Handler.handleCallback (Handler.java:938)
      at android.os.Handler.dispatchMessage (Handler.java:99)
      at android.os.Looper.loop (Looper.java:223)
      at android.app.ActivityThread.main (ActivityThread.java:7721)
      at java.lang.reflect.Method.invoke (Native method)
      at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run (RuntimeInit.java:592)
      at com.android.internal.os.ZygoteInit.main (ZygoteInit.java:952)

**Figure 1.** ANR stack trace caused by a*futex*wait.

### Cause

So far, the root cause of this issue is unclear. Some potential causes may include:

- Bad ad implementation.
- An outdated version of`WebView`since the user may have opted not to update the app automatically.
- High usage of system resources (CPU, GPU, etc.), which may require a lot of profiling.
- [Shader compilation](https://docs.unity3d.com/Manual/shader-compilation.html)crashes, which could indicate that the content has an incompatible shader or that the user has an old`WebView`version installed.

### Solution

- To narrow down which type of content is causing the`WebView`to block the main thread, add logs to your game whenever a web page is loaded, displayed, or closed.
  - You can use[Backtrace](https://backtrace.io/)or[Crashlytics](https://firebase.google.com/products/crashlytics)reporting services.
  - Then, after analyzing the data and finding the issue, try disabling the offending ad providers.
  - Include memory logs to ensure the issue is not memory related.
- Alert the user to[update the`WebView`from Google Play](https://developer.android.com/about/versions/lollipop#WebView). From Android 5.0 (API level 21) and higher,`WebView`has moved to an APK. Therefore, it can be updated separately from the Android platform. To see what version of`WebView`is in use on a device, go to**Settings \> Apps \> Android System WebView**and look at the version at the bottom of the page.

![App info screen showing the WebView versions.](https://developer.android.com/static/images/games/engines/unity/unity-anrs-list-webview-version.png)**Figure 1.** Check the`WebView`version.

## Unity pause

When`UnityPlayerActivity`receives an`onPause()`call, the following chain of operations starts:

1. `UnityPlayerActivity`notifies the Unity runtime engine that the activity has paused.
2. Unity calls every[`MonoBehaviour`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html)that implements the[`OnApplicationPause`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnApplicationPause.html)event.
3. Unity stops its components and modules, such as sound playback, rendering, game loop, and animation.
4. To make sure both[`Unity Android Player`](https://docs.unity3d.com/Manual/class-PlayerSettings.html)(UAP) and engine are synchronized, the UAP waits 4 seconds for the engine to stop.
5. If that operation takes over 5 seconds, the system triggers an ANR.

### Stack trace

    "main" tid=1 Timed Waiting
    jdk.internal.misc.Unsafe.park (Native method)
    java.util.concurrent.locks.LockSupport.parkNanos (LockSupport.java:234)
    java.util.concurrent.locks.AbstractQueuedSynchronizer.doAcquireSharedNanos (AbstractQueuedSynchronizer.java:1079)
    java.util.concurrent.locks.AbstractQueuedSynchronizer.tryAcquireSharedNanos (AbstractQueuedSynchronizer.java:1369)
    java.util.concurrent.Semaphore.tryAcquire (Semaphore.java:415)
    com.unity3d.player.UnityPlayer.pauseUnity (UnityPlayer.java:833)
    com.unity3d.player.UnityPlayer.pause (UnityPlayer.java:796)
    com.unity3d.player.UnityPlayerActivity.onPause (UnityPlayerActivity.java:117)
    android.app.Activity.performPause (Activity.java:8517)
    android.app.Instrumentation.callActivityOnPause (Instrumentation.java:1618)
    android.app.ActivityThread.performPauseActivityIfNeeded (ActivityThread.java:5061)
    android.app.ActivityThread.performPauseActivity (ActivityThread.java:5022)
    android.app.ActivityThread.handlePauseActivity (ActivityThread.java:4974)
    android.app.servertransaction.PauseActivityItem.execute (PauseActivityItem.java:48)
    android.app.servertransaction.ActivityTransactionItem.execute (ActivityTransactionItem.java:45)
    android.app.servertransaction.TransactionExecutor.executeLifecycleState (TransactionExecutor.java:179)
    android.app.servertransaction.TransactionExecutor.execute (TransactionExecutor.java:97)
    android.app.ActivityThread$H.handleMessage (ActivityThread.java:2303)
    android.os.Handler.dispatchMessage (Handler.java:106)
    android.os.Looper.loopOnce (Looper.java:201)
    android.os.Looper.loop (Looper.java:288)
    android.app.ActivityThread.main (ActivityThread.java:7884)
    java.lang.reflect.Method.invoke (Native method)
    com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run (RuntimeInit.java:548)
    com.android.internal.os.ZygoteInit.main (ZygoteInit.java:936)

**Figure 3.**ANR caused by a semaphore that's never released.

### Solution

Ensure that your C# game code doesn't take too long to finish execution during a pause or resume event.

- Profile your game and check whether the`OnApplicationPause`is an expensive operation. You can use a[`Stopwatch`](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.stopwatch).
- Avoid I/O operations or synchronous network requests.
- Move the operations to another[`Thread`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread)using the[`Task`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task). Unity 2023.1 supports a simplified[asynchronous programming model](https://docs.unity3d.com/2023.2/Documentation/Manual/AwaitSupport.html)using C#`async`and`await`keywords.

## UnitySendMessage blocked

Java Unity plugins and SDKs send data to the C# game layer using[JNI](https://developer.android.com/ndk/guides). However, this communication might block the main thread due to a native synchronization routine such as a mutex, causing an ANR due to lock contention.

### Stack trace

The ANR in figure 4 was caused by a long operation in the C# code called by a Java plugin. The Unity engine uses a[Non-Priority Inheritance mutex](https://android.googlesource.com/platform/bionic/+/master/libc/bionic/pthread_mutex.cpp#711)to ensure correct execution.  

    libc.so NonPI::MutexLockWithTimeout(pthread_mutex_internal_t*, bool, timespec const*) + 604
    com.unity3d.player.UnityPlayer.nativeUnitySendMessage (Native method)
    com.unity3d.player.UnityPlayer.UnitySendMessage (UnityPlayer.java:665)

**Figure 4.**ANR caused by a lock contention.

**Cause**

The problem is that several messages are being dispatched when the application is resumed. The messages are queued because they cannot be sent while the game is in the background. The messages are all dispatched simultaneously when the app resumes.

During a pause period, you generally store your game's information on the server; for example, you record a player's position in the game so the player can return to the same place when the game resumes.

This workload, combined with other third-party code creating its own workload, can overload the device's resources, particularly the main thread. The main thread runs an app's user interface and is often the main location of ANRs. So, any added workload on the main thread increases the potential for an ANR.

### Solution

During an application pause, make sure all your code actions are necessary, or try saving the user's state in your local device memory. And, of course, see whether you can also complete these actions outside of the pause period.

**A few approaches**:

- Move the C# operation that handles a[message](https://docs.unity3d.com/560/Documentation/Manual/MessagingSystem.html)to a thread other than the main thread.
  - If your code does not depend on Unity's main thread context, use`Task`for communication instead of message.
- Don't send multiple messages from your plugin when the game is paused.
  - The engine cannot send messages while the game is in the background.
  - Only send the last data state to your game if that does not impact your game functionality.

## Install Referrer

[Play Install Referrer](https://developer.android.com/google/play/installreferrer/library)is a unique string sent to the Play Store whenever a user clicks on an ad. It is an Android-specific ad tracking identifier. Once installed, the app sends the install referrer to the attribution partner, which matches the source with the install (attributing the conversion).

### Stack trace

Figure 5 shows an ANR stack trace from a game that uses the Facebook SDK to retrieve the install attribution.
![](https://developer.android.com/static/images/games/engines/unity/unity-anrs-list-binder.png)**Figure 5.**Android Vitals report containing a Binder call.

### Cause

The ANR was caused by a slow binder call. However, the root cause can't be determined without access to the SDK source code.

### Solution

Solving this type of problem involves communication with the SDK developer or a lot of online searching for a potential solution, checking whether a newer version of the SDK solves the ANR for others, or even experimenting with a small rollout strategy.

Google provides an[SDK Index page](https://play.google.com/sdks)that combines usage data from Google Play apps with information gathered through code detection to provide attributes and signals designed to help you decide whether to adopt, keep, or remove an SDK from your app.

## Additional resources

To learn more about ANRs, consult the following resources:

- [Debug ANRs](https://developer.android.com/games/engines/unity/unity-anrs)--- Android game development
- [ANRs](https://developer.android.com/topic/performance/vitals/anr)--- App quality