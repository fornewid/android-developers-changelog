---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/listenableworker
url: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/listenableworker
source: md.txt
---

In certain situations, you may need to provide a custom threading strategy. For
example, you may need to handle a callback-based asynchronous operation.
WorkManager supports this use case with
[`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker).
`ListenableWorker` is the most basic worker API;
[`Worker`](https://developer.android.com/reference/androidx/work/Worker),
[`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker), and
[`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker) all derive from this class. A
`ListenableWorker` only signals when the work should start and stop and leaves
the threading entirely up to you. The start work signal is invoked on the main
thread, so it is very important that you go to a background thread of your
choice manually.

The abstract method
[`ListenableWorker.startWork()`](https://developer.android.com/reference/androidx/work/ListenableWorker#startWork())
returns a `ListenableFuture` of the
[`Result`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result). A
`ListenableFuture` is a lightweight interface: it is a `Future` that provides
functionality for attaching listeners and propagating exceptions. In the
`startWork` method, you are expected to return a `ListenableFuture`, which you
will set with the `Result` of the operation once it's completed. You can create
`ListenableFuture` instances in one of two ways:

1. If you use Guava, use `ListeningExecutorService`.
2. Otherwise, include [`councurrent-futures`](https://developer.android.com/jetpack/androidx/releases/concurrent#declaring_dependencies) in your gradle file and use [`CallbackToFutureAdapter`](https://developer.android.com/reference/androidx/concurrent/futures/CallbackToFutureAdapter).

If you wanted to execute some work based on an asynchronous callback, you would
do something like this:  

### Kotlin

```kotlin
class CallbackWorker(
        context: Context,
        params: WorkerParameters
) : ListenableWorker(context, params) {
    override fun startWork(): ListenableFuture<Result> {
        return CallbackToFutureAdapter.getFuture { completer ->
            val callback = object : Callback {
                var successes = 0

                override fun onFailure(call: Call, e: IOException) {
                    completer.setException(e)
                }

                override fun onResponse(call: Call, response: Response) {
                    successes++
                    if (successes == 100) {
                        completer.set(Result.success())
                    }
                }
            }

            repeat(100) {
                downloadAsynchronously("https://example.com", callback)
            }

            callback
        }
    }
}
```

### Java

```java
public class CallbackWorker extends ListenableWorker {

    public CallbackWorker(Context context, WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public ListenableFuture<Result> startWork() {
        return CallbackToFutureAdapter.getFuture(completer -> {
            Callback callback = new Callback() {
                int successes = 0;

                @Override
                public void onFailure(Call call, IOException e) {
                    completer.setException(e);
                }

                @Override
                public void onResponse(Call call, Response response) {
                    successes++;
                    if (successes == 100) {
                        completer.set(Result.success());
                    }
                }
            };

            for (int i = 0; i < 100; i++) {
                downloadAsynchronously("https://www.example.com", callback);
            }
            return callback;
        });
    }
}
```

What happens if your work is
[stopped](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/managing-work#cancelling)?
A `ListenableWorker`'s `ListenableFuture` is always cancelled when the work is
expected to stop. Using a `CallbackToFutureAdapter`, you simply have to add a
cancellation listener, as follows:  

### Kotlin

```kotlin
class CallbackWorker(
        context: Context,
        params: WorkerParameters
) : ListenableWorker(context, params) {
    override fun startWork(): ListenableFuture<Result> {
        return CallbackToFutureAdapter.getFuture { completer ->
            val callback = object : Callback {
                var successes = 0

                override fun onFailure(call: Call, e: IOException) {
                    completer.setException(e)
                }

                override fun onResponse(call: Call, response: Response) {
                    ++successes
                    if (successes == 100) {
                        completer.set(Result.success())
                    }
                }
            }

 completer.addCancellationListener(cancelDownloadsRunnable, executor)

            repeat(100) {
                downloadAsynchronously("https://example.com", callback)
            }

            callback
        }
    }
}
```

### Java

```java
public class CallbackWorker extends ListenableWorker {

    public CallbackWorker(Context context, WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public ListenableFuture<Result> startWork() {
        return CallbackToFutureAdapter.getFuture(completer -> {
            Callback callback = new Callback() {
                int successes = 0;

                @Override
                public void onFailure(Call call, IOException e) {
                    completer.setException(e);
                }

                @Override
                public void onResponse(Call call, Response response) {
                    ++successes;
                    if (successes == 100) {
                        completer.set(Result.success());
                    }
                }
            };

            completer.addCancellationListener(cancelDownloadsRunnable, executor);

            for (int i = 0; i < 100; ++i) {
                downloadAsynchronously("https://www.example.com", callback);
            }
            return callback;
        });
    }
}
```

## Running a ListenableWorker in a different process

You can also bind a worker to a specific process by using
[`RemoteListenableWorker`](https://developer.android.com/reference/kotlin/androidx/work/multiprocess/RemoteListenableWorker),
an implementation of `ListenableWorker`.

`RemoteListenableWorker` binds to a specific process with two extra arguments
that you provide as part of the input data when building the work request:
`ARGUMENT_CLASS_NAME` and `ARGUMENT_PACKAGE_NAME`.

The following example demonstrates building a work request that is bound to a
specific process:  

### Kotlin

```kotlin
val PACKAGE_NAME = "com.example.background.multiprocess"

val serviceName = RemoteWorkerService::class.java.name
val componentName = ComponentName(PACKAGE_NAME, serviceName)

val data: Data = Data.Builder()
   .putString(ARGUMENT_PACKAGE_NAME, componentName.packageName)
   .putString(ARGUMENT_CLASS_NAME, componentName.className)
   .build()

return OneTimeWorkRequest.Builder(ExampleRemoteListenableWorker::class.java)
   .setInputData(data)
   .build()
```

### Java

```java
String PACKAGE_NAME = "com.example.background.multiprocess";

String serviceName = RemoteWorkerService.class.getName();
ComponentName componentName = new ComponentName(PACKAGE_NAME, serviceName);

Data data = new Data.Builder()
        .putString(ARGUMENT_PACKAGE_NAME, componentName.getPackageName())
        .putString(ARGUMENT_CLASS_NAME, componentName.getClassName())
        .build();

return new OneTimeWorkRequest.Builder(ExampleRemoteListenableWorker.class)
        .setInputData(data)
        .build();
```

For each `RemoteWorkerService`, you also need to add a service definition in
your `AndroidManifest.xml` file:  

```xml
<manifest ... >
    <service
            android:name="androidx.work.multiprocess.RemoteWorkerService"
            android:exported="false"
            android:process=":worker1" />

        <service
            android:name=".RemoteWorkerService2"
            android:exported="false"
            android:process=":worker2" />
    ...
</manifest>
```

## Samples

- [WorkManagerMultiProcessSample](https://github.com/android/architecture-components-samples/tree/main/WorkManagerMultiprocessSample)