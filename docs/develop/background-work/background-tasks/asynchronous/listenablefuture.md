---
title: https://developer.android.com/develop/background-work/background-tasks/asynchronous/listenablefuture
url: https://developer.android.com/develop/background-work/background-tasks/asynchronous/listenablefuture
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/background-tasks/asynchronous/llms.txt

A `ListenableFuture` represents the result of an asynchronous computation: a
computation that may or may not have finished producing a result yet. It's a
type of `Future`
that allows you to register callbacks to be executed once the computation is
complete, or if the computation is already complete, immediately.

`ListenableFuture` is not part of the Android framework and is instead provided
by [Guava](https://github.com/google/guava). For more information about the
implementation of this class, see [ListenableFuture explained](https://github.com/google/guava/wiki/ListenableFutureExplained).

Many existing Jetpack libraries such as [CameraX](https://developer.android.com/jetpack/androidx/releases/camera.md.txt)
or [Health Services](https://developer.android.com/training/wearables/health-services) have asynchronous methods
where the return type is a `ListenableFuture` which represents the status of
the execution. In some cases you may need to implement a method that returns a
`ListenableFuture`, such as to satisfy the requirements of [`TileService`](https://developer.android.com/reference/androidx/wear/tiles/TileService.md.txt).

> [!NOTE]
> **Tip:** Check if the Jetpack library you're using has a `-ktx` artifact, as these often contain built-in wrappers for `ListenableFuture`-based methods. For example, `androidx.work:work-runtime-ktx` provides wrappers for WorkManager APIs as suspend functions.

## Required libraries

### Groovy

```groovy
dependencies {
    implementation "com.google.guava:guava:31.0.1-android"

    // To use CallbackToFutureAdapter
    implementation "androidx.concurrent:concurrent-futures:1.3.0"

    // Kotlin
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-guava:1.6.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("com.google.guava:guava:31.0.1-android")

    // To use CallbackToFutureAdapter
    implementation("androidx.concurrent:concurrent-futures:1.3.0")

    // Kotlin
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-guava:1.6.0")
}
```

## Getting the result of a `ListenableFuture`

### Adding a callback

Use the [`Futures.addCallback(...)`](https://guava.dev/releases/snapshot/api/docs/com/google/common/util/concurrent/Futures.html#addCallback(com.google.common.util.concurrent.ListenableFuture,com.google.common.util.concurrent.FutureCallback,java.util.concurrent.Executor))
helper method to attach success and failure callbacks onto a `ListenableFuture`.


```kotlin
val future: ListenableFuture<QueryResult> = ...
Futures.addCallback(
    future,
    object : FutureCallback<QueryResult> {
        override fun onSuccess(result: QueryResult) {
            // handle success.
        }

        override fun onFailure(t: Throwable) {
            // handle failure.
        }
    },
    // causes the callbacks to be executed on the main (UI) thread.
    context.mainExecutor
)
```

<br />

### Suspending in Kotlin

When using Kotlin, the easiest way to wait for the result of a ListenableFuture
is to use [`await()`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-guava/kotlinx.coroutines.guava/await.html).


```kotlin
// import kotlinx.coroutines.guava.await

// ...

val future: ListenableFuture<QueryResult> = ...
val queryResult = future.await() // suspends awaiting success.
```

<br />

### Interop with RxJava

An RxJava [`Single`](https://reactivex.io/documentation/single.html)
can be created from a `ListenableFuture` by registering callbacks inside a
[`SingleEmitter`](https://reactivex.io/RxJava/javadoc/io/reactivex/SingleEmitter.html).

```kotlin
val future: ListenableFuture<QueryResult> = ...
val single = Single.create<QueryResult> {
    Futures.addCallback(future, object : FutureCallback<QueryResult> {
        override fun onSuccess(result: QueryResult) {
            it.onSuccess(result)
        }

        override fun onFailure(t: Throwable) {
            it.onError(t)
        }
    }, executor)
}
```

## Creating a `ListenableFuture`

### Creating an immediate future

If your API is not asynchronous, but you need to wrap the result of a completed
operation into a `ListenableFuture`, you can create an `ImmediateFuture`. This
can be done using the [`Futures.immediateFuture(...)`](https://guava.dev/releases/snapshot/api/docs/com/google/common/util/concurrent/Futures.html#immediateFuture(V))
factory method.

> [!WARNING]
> **Warning:** This sample code is only recommended when the result is available *immediately* . `ImmediateFuture` shouldn't be used in synchronous APIs, such as when `getQueryResult()` is a long-running blocking call.


```kotlin
fun getResult(): ListenableFuture<QueryResult> {
    try {
        val queryResult = getQueryResult()
        return Futures.immediateFuture(queryResult)
    } catch (e: Exception) {
        return Futures.immediateFailedFuture(e)
    }
}
```

<br />

### Using a coroutine

In Kotlin, a [`future{ ... }`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-guava/kotlinx.coroutines.guava/future.html)
can be used to convert the result of a suspend function into a `ListenableFuture`.


```kotlin
// import kotlinx.coroutines.guava.future

suspend fun getResultAsync(): QueryResult = /* ... */

fun getResultFuture(): ListenableFuture<QueryResult> {
    return coroutineScope.future {
        getResultAsync()
    }
}
```

<br />

### Converting a callback

To convert a callback-based API into one that uses `ListenableFuture`, use
[`CallbackToFutureAdapter`](https://developer.android.com/reference/androidx/concurrent/futures/CallbackToFutureAdapter.md.txt).
This API is provided by the `androidx.concurrent:concurrent-futures` artifact.

See [androidx.concurrent](https://developer.android.com/jetpack/androidx/releases/concurrent.md.txt) for more information.

### Converting from RxJava `Single`

When using RxJava, a [`Single`](https://reactivex.io/documentation/single.html)
can be converted into a [`SettableFuture`](https://guava.dev/releases/snapshot/api/docs/com/google/common/util/concurrent/SettableFuture.html),
which implements `ListenableFuture`.

```kotlin
fun getResult(): ListenableFuture<QueryResult> {
    val single: Single<QueryResult> = ...

    val future = SettableFuture.create<QueryResult>()
    single.subscribe(future::set, future::setException)
    return future
}
```