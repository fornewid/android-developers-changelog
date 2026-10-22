---
title: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/worker-impl
url: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/worker-impl
source: md.txt
---

WorkManager provides APIs for testing [`Worker`](https://developer.android.com/reference/kotlin/androidx/work/Worker),
[`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker), and the
`ListenableWorker` variants
([`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker)
and [`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker)).

## Testing Workers

Let's say we have a `Worker` which looks like this:


```kotlin
class SleepWorker(context: Context, parameters: WorkerParameters) :
    Worker(context, parameters) {

    override fun doWork(): Result {
        // Sleep on a background thread.
        Thread.sleep(1000)
        return Result.success()
    }
}
```

<br />

To test this `Worker`, you can use
[`TestWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestWorkerBuilder). This
builder helps build instances of `Worker` that can be used for the purpose of
testing business logic.


```kotlin
// Kotlin code uses the TestWorkerBuilder extension to build
// the Worker
@RunWith(AndroidJUnit4::class)
class SleepWorkerTest {
    private lateinit var context: Context
    private lateinit var executor: Executor

    @Before
    fun setUp() {
        context = ApplicationProvider.getApplicationContext()
        executor = Executors.newSingleThreadExecutor()
    }

    @Test
    fun testSleepWorker() {
        val worker = TestWorkerBuilder<SleepWorker>(
            context = context,
            executor = executor
        ).build()

        val result = worker.doWork()
        assertThat(result, `is`(Result.success()))
    }
}
```

<br />

`TestWorkerBuilder` can also be used to set tags, such as `inputData` or
`runAttemptCount`, so that you can verify worker state in isolation. Consider
an example in which `SleepWorker` takes in a sleep duration as input data
rather than it being a constant defined in the worker:


```kotlin
class SleepWorker(context: Context, parameters: WorkerParameters) :
    Worker(context, parameters) {

    override fun doWork(): Result {
        // Sleep on a background thread.
        val sleepDuration = inputData.getLong(SLEEP_DURATION, 1000)
        Thread.sleep(sleepDuration)
        return Result.success()
    }

    companion object {
        const val SLEEP_DURATION = "SLEEP_DURATION"
    }
}
```

<br />

In `SleepWorkerTest`, you can provide that input data to your
`TestWorkerBuilder` to satisfy the needs of `SleepWorker`.


```kotlin
// Kotlin code uses the TestWorkerBuilder extension to build
// the Worker
@RunWith(AndroidJUnit4::class)
class SleepWorkerTest {
    private lateinit var context: Context
    private lateinit var executor: Executor

    @Before
    fun setUp() {
        context = ApplicationProvider.getApplicationContext()
        executor = Executors.newSingleThreadExecutor()
    }

    @Test
    fun testSleepWorker() {
        val worker = TestWorkerBuilder<SleepWorker>(
            context = context,
            executor = executor,
            inputData = workDataOf("SLEEP_DURATION" to 1000L)
        ).build()

        val result = worker.doWork()
        assertThat(result, `is`(Result.success()))
    }
}
```

<br />

For more details on the `TestWorkerBuilder` API, see the reference page for
[`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder),
the superclass of `TestWorkerBuilder`.

## Testing ListenableWorker and its variants

To test a [`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker) or its
variants ([`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker)
and [`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker)), use
[`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder).
The main difference between `TestWorkerBuilder` and a
[`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder)
is that `TestWorkerBuilder` lets you specify the background `Executor` used to
run the `Worker`, whereas `TestListenableWorkerBuilder` relies on the
threading logic of the `ListenableWorker` implementation.

For example, suppose we need to test a `CoroutineWorker` which looks like this:


```kotlin
class SleepWorker(context: Context, parameters: WorkerParameters) :
    CoroutineWorker(context, parameters) {
    override suspend fun doWork(): Result {
        delay(1000L) // milliseconds
        return Result.success()
    }
}
```

<br />

To test `SleepWorker`, we first create an instance of the Worker using
`TestListenableWorkerBuilder` and then call its `doWork` function within a
coroutine.


```kotlin
@RunWith(AndroidJUnit4::class)
class SleepWorkerTest {
    private lateinit var context: Context

    @Before
    fun setUp() {
        context = ApplicationProvider.getApplicationContext()
    }

    @Test
    fun testSleepWorker() {
        val worker = TestListenableWorkerBuilder<SleepWorker>(context).build()
        runBlocking {
            val result = worker.doWork()
            assertThat(result, `is`(Result.success()))
        }
    }
}
```

<br />

`runBlocking` makes sense as a coroutine builder for your tests so that any code
that would execute asynchronously is instead run in parallel.

Testing an `RxWorker` implementation is similar to testing `CoroutineWorker`, as
`TestListenableWorkerBuilder` can handle any subclass of `ListenableWorker`.
Consider a version of `SleepWorker` that uses RxJava instead of coroutines.


```kotlin
class SleepWorker(
    context: Context,
    parameters: WorkerParameters
) : RxWorker(context, parameters) {
    override fun createWork(): Single<Result> {
        return Single.just(Result.success())
            .delay(1000L, TimeUnit.MILLISECONDS)
    }
}
```

<br />

A version of `SleepWorkerTest` that tests an `RxWorker` may look similar to the
version that tested a `CoroutineWorker`. You use the same
`TestListenableWorkerBuilder` but now call into `RxWorker`'s `createWork`
function. `createWork` returns a `Single` that you can use to verify the
behavior of your worker. `TestListenableWorkerBuilder` handles any threading
complexities and executes your worker code in parallel.


```kotlin
@RunWith(AndroidJUnit4::class)
class SleepWorkerTest {
    private lateinit var context: Context

    @Before
    fun setUp() {
        context = ApplicationProvider.getApplicationContext()
    }

    @Test
    fun testSleepWorker() {
        val worker = TestListenableWorkerBuilder<SleepWorker>(context).build()
        worker.createWork().subscribe { result ->
            assertThat(result, `is`(Result.success()))
        }
    }
}
```

<br />