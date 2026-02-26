---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/worker
url: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/worker
source: md.txt
---

When you use a [`Worker`](https://developer.android.com/reference/androidx/work/Worker), WorkManager
automatically calls [`Worker.doWork()`](https://developer.android.com/reference/androidx/work/Worker#doWork())
on a background thread. The background thread comes from the `Executor`
specified in WorkManager's [`Configuration`](https://developer.android.com/reference/androidx/work/Configuration).
By default, WorkManager sets up an `Executor` for you---but you can also customize
your own. For example, you can share an existing background Executor in your
app, create a single-threaded `Executor` to make sure all your background work
executes sequentially, or even specify a custom `Executor`. To customize the
`Executor`, make sure you initialize WorkManager manually.

When configuring WorkManager manually, you can specify your `Executor` as
follows:

### Kotlin

```kotlin
WorkManager.initialize(
    context,
    Configuration.Builder()
         // Uses a fixed thread pool of size 8 threads.
        .setExecutor(Executors.newFixedThreadPool(8))
        .build())
```

### Java

```java
WorkManager.initialize(
    context,
    new Configuration.Builder()
        .setExecutor(Executors.newFixedThreadPool(8))
        .build());
```

Here is an example of a simple `Worker` that downloads the contents of a webpage
100 times:

### Kotlin

```kotlin
class DownloadWorker(context: Context, params: WorkerParameters) : Worker(context, params) {

    override fun doWork(): ListenableWorker.Result {
        repeat(100) {
            try {
                downloadSynchronously("https://www.google.com")
            } catch (e: IOException) {
                return ListenableWorker.Result.failure()
            }
        }

        return ListenableWorker.Result.success()
    }
}
```

### Java

```java
public class DownloadWorker extends Worker {

    public DownloadWorker(Context context, WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public Result doWork() {
        for (int i = 0; i < 100; i++) {
            try {
                downloadSynchronously("https://www.google.com");
            } catch (IOException e) {
                return Result.failure();
            }
        }

        return Result.success();
    }

}
```

Note that [`Worker.doWork()`](https://developer.android.com/reference/androidx/work/Worker#doWork()) is a
synchronous call---you are expected to do the entirety of your background work in
a blocking fashion and finish it by the time the method exits. If you call an
asynchronous API in `doWork()` and return a [`Result`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result), your callback may not
operate properly. If you find yourself in this situation, consider using a [`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker) (see [Threading in ListenableWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/listenableworker)).

When a currently running `Worker` is [stopped for any reason](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/managing-work#cancelling), it
receives a call to [`Worker.onStopped()`](https://developer.android.com/reference/androidx/work/ListenableWorker#onStopped()). Override this method or
call [`Worker.isStopped()`](https://developer.android.com/reference/androidx/work/ListenableWorker#isStopped())
to checkpoint your code and free up resources when necessary. When the `Worker`
in the example above is stopped, it may be in the middle of its loop of
downloading items and will continue doing so even though it has been stopped. To
optimize this behavior, you can do something like this:

### Kotlin

```kotlin
class DownloadWorker(context: Context, params: WorkerParameters) : Worker(context, params) {

    override fun doWork(): ListenableWorker.Result {
        repeat(100) {
            if (isStopped) {
                break
            }

            try {
                downloadSynchronously("https://www.google.com")
            } catch (e: IOException) {
                return ListenableWorker.Result.failure()
            }

        }

        return ListenableWorker.Result.success()
    }
}
```

### Java

```java
public class DownloadWorker extends Worker {

    public DownloadWorker(Context context, WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public Result doWork() {
        for (int i = 0; i < 100; ++i) {
            if (isStopped()) {
                break;
            }

            try {
                downloadSynchronously("https://www.google.com");
            } catch (IOException e) {
                return Result.failure();
            }
        }

        return Result.success();
    }
}
```

Once a `Worker` has been stopped, it doesn't matter what you return from
`Worker.doWork()`; the `Result` will be ignored.