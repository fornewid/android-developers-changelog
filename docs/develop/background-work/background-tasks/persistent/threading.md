---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/threading
url: https://developer.android.com/develop/background-work/background-tasks/persistent/threading
source: md.txt
---

# Threading in WorkManager

In[Getting started with WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/basics), we mentioned that WorkManager performs background work asynchronously on your behalf. The basic implementation addresses the demands of most apps. For more advanced use cases, such as correctly handling work being stopped, you should learn about threading and concurrency in WorkManager.

There are four different types of work primitives provided by WorkManager:

- [`Worker`](https://developer.android.com/reference/androidx/work/Worker)is the simplest implementation, and the one you have seen in previous sections. WorkManager automatically runs it on a background thread (that you can override). Read more about threading in`Worker`instances in[Threading in Worker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/worker).
- [`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker)is the recommended implementation for Kotlin users.`CoroutineWorker`instances expose a suspending function for background work. By default, they run a default`Dispatcher`, which you can customize. Read more about threading in`CoroutineWorker`instances in[Threading in CoroutineWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/coroutineworker).
- [`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker)is the recommended implementation for RxJava users. RxWorkers should be used if a lot of your existing asynchronous code is modelled in RxJava. As with all RxJava concepts, you are free to choose the threading strategy of your choice. Read more about threading in`RxWorker`instances in[Threading in RxWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/rxworker).
- [`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker)is the base class for`Worker`,`CoroutineWorker`, and`RxWorker`. It is intended for Java developers who have to interact with callback-based asynchronous APIs such as`FusedLocationProviderClient`and are not using RxJava. Read more about threading in`ListenableWorker`instances in[Threading in ListenableWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/listenableworker).