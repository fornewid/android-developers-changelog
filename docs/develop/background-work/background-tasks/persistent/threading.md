---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/threading
url: https://developer.android.com/develop/background-work/background-tasks/persistent/threading
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/llms.txt

[Getting started with WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/basics) explains that WorkManager performs
background work asynchronously on your behalf. The basic implementation
addresses the demands of most apps. For more advanced use cases, such as
correctly handling work being stopped, you should learn about threading and
concurrency in WorkManager.

There are four different types of work primitives provided by WorkManager:

- [`Worker`](https://developer.android.com/reference/androidx/work/Worker.md.txt) is the basic implementation, and the one you have seen in previous sections. WorkManager automatically runs it on a background thread, which you can override. For more information about threading in `Worker` instances, see [Threading in Worker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/worker).
- [`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker.md.txt) is the recommended implementation for Kotlin users. `CoroutineWorker` instances expose a suspending function for background work. By default, they run a default `Dispatcher`, which you can customize. For more information about threading in `CoroutineWorker` instances, see [Threading in
  CoroutineWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/coroutineworker).
- [`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker.md.txt) is the recommended implementation for RxJava users. Use `RxWorker` if a lot of your existing asynchronous code is modeled in RxJava. As with all RxJava concepts, you are free to choose the threading strategy. For more information about threading in `RxWorker` instances, see [Threading in RxWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/rxworker).
- [`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker.md.txt) is the base class for `Worker`, `CoroutineWorker`, and `RxWorker`. It is intended for Java developers who have to interact with callback-based asynchronous APIs such as `FusedLocationProviderClient` and are not using RxJava. For more information about threading in `ListenableWorker` instances, see [Threading in ListenableWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/listenableworker).