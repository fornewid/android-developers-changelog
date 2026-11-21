---
title: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/integration-testing
url: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/integration-testing
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/background-tasks/llms.txt

[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) provides a
`work-testing` artifact which helps with testing of your workers.

## Setup

To use the `work-testing` artifact, add it as an `androidTestImplementation`
dependency in `build.gradle`.

### Groovy

```groovy
dependencies {
    def work_version = "2.5.0"

    ...

    // optional - Test helpers
    androidTestImplementation "androidx.work:work-testing:$work_version"
}
```

### Kotlin

```kotlin
dependencies {
    val work_version = "2.4.0"

    ...

    // optional - Test helpers
    androidTestImplementation("androidx.work:work-testing:$work_version")
}
```

For more information on adding dependencies, look at the Declaring dependencies
section in the
[WorkManager release notes](https://developer.android.com/jetpack/androidx/releases/work.md.txt#declaring_dependencies).

> [!NOTE]
> **Note:** Beginning with 2.1.0, WorkManager provides the [`TestWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestWorkerBuilder.md.txt) and [`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder.md.txt) classes, which let you test the business logic in your workers without having to initialize `WorkManager` with `WorkManagerTestInitHelper`. [Testing Worker implementation](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/testing-worker-impl) covers these classes. The material in this page is still useful for when you need to perform integration tests.

> [!NOTE]
> **Note:** It is highly recommended to use [`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder.md.txt) to test [`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker.md.txt) implementations, as the `work-testing` artifact uses [Dispatchers.Default](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-default.html) rather than your worker implementation's [CoroutineDispatcher](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/). More information about this API can be found at [Testing Worker implementation](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/testing-worker-impl#testing_listenableworker_and_its_variants).

## Concepts

`work-testing` provides a special implementation of WorkManager for test mode,
which is initialized using
[`WorkManagerTestInitHelper`](https://developer.android.com/reference/androidx/work/testing/WorkManagerTestInitHelper.md.txt).

The `work-testing` artifact also provides a
[`SynchronousExecutor`](https://developer.android.com/reference/androidx/work/testing/SynchronousExecutor.md.txt)
which makes it easier to write tests in a synchronous manner, without having to
deal with multiple threads, locks, or latches.

Here is an example on how to use all these classes together.


```kotlin
@RunWith(AndroidJUnit4::class)
class BasicInstrumentationTest {
    @Before
    fun setup() {
        val context = InstrumentationRegistry.getInstrumentation().targetContext
        val config = Configuration.Builder()
            .setMinimumLoggingLevel(Log.DEBUG)
            .setExecutor(SynchronousExecutor())
            .build()

        // Initialize WorkManager for instrumentation tests.
        WorkManagerTestInitHelper.initializeTestWorkManager(context, config)
    }
}
```

<br />

## Structuring Tests

Now that WorkManager has been initialized in test mode, you are ready to test
your workers.

Let's say you have an `EchoWorker` which expects some `inputData`, and simply
copies (echoes) its input to `outputData`.


```kotlin
class EchoWorker(context: Context, parameters: WorkerParameters) :
    Worker(context, parameters) {
    override fun doWork(): Result {
        return when (inputData.size()) {
            0 -> Result.failure()
            else -> Result.success(inputData)
        }
    }
}
```

<br />

### Basic Tests

Below is an Android Instrumentation test that tests `EchoWorker`. The main
takeaway here is that testing `EchoWorker` in test mode is very similar to how
you would use `EchoWorker` in a real application.


```kotlin
@Test
@Throws(Exception::class)
fun testSimpleEchoWorker() {
    // Define input data.
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request.
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .build()

    val workManager = WorkManager.getInstance(applicationContext)
    // Enqueue and wait for result. This also runs the Worker synchronously
    // because we are using a SynchronousExecutor.
    workManager.enqueue(request).result.get()
    // Get WorkInfo and outputData.
    val workInfo = checkNotNull(workManager.getWorkInfoById(request.id).get())
    val outputData = workInfo.outputData

    // Assert.
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

<br />

Let's write another test which makes sure that when `EchoWorker` gets no input
data, the expected `Result` is a `Result.failure()`.


```kotlin
@Test
@Throws(Exception::class)
fun testEchoWorkerNoInput() {
    // Create request.
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .build()

    val workManager = WorkManager.getInstance(applicationContext)
    // Enqueue and wait for result. This also runs the Worker synchronously
    // because we are using a SynchronousExecutor.
    workManager.enqueue(request).result.get()
    // Get WorkInfo.
    val workInfo = checkNotNull(workManager.getWorkInfoById(request.id).get())

    // Assert.
    assertThat(workInfo.state, `is`(WorkInfo.State.FAILED))
}
```

<br />

## Simulate constraints, delays, and periodic work

`WorkManagerTestInitHelper` provides you with an instance of
[`TestDriver`](https://developer.android.com/reference/androidx/work/testing/TestDriver.md.txt) which can be used
to simulate initial delay, conditions where constraints are met for
`ListenableWorker` instances, and, intervals for `PeriodicWorkRequest`
instances.

### Test Initial Delays

Workers can have initial delays. To test `EchoWorker` with an `initialDelay`,
rather than having to wait for the `initialDelay` in your test, you can use
the `TestDriver` to mark the work request's initial delay as met using
`setInitialDelayMet`.


```kotlin
@Test
@Throws(Exception::class)
fun testWithInitialDelay() {
    // Define input data.
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request.
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .setInitialDelay(10, TimeUnit.SECONDS)
        .build()

    val workManager = WorkManager.getInstance(getApplicationContext())
    // Get the TestDriver.
    val testDriver = checkNotNull(WorkManagerTestInitHelper.getTestDriver(getApplicationContext()))
    // Enqueue.
    workManager.enqueue(request).result.get()
    // Tells the WorkManager test framework that initial delays are now met.
    testDriver.setInitialDelayMet(request.id)
    // Get WorkInfo and outputData.
    val workInfo = checkNotNull(workManager.getWorkInfoById(request.id).get())
    val outputData = workInfo.outputData

    // Assert.
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

<br />

### Testing Constraints

`TestDriver` can also be used to mark constraints as met using
`setAllConstraintsMet`. Here is an example on how you can test a `Worker`
with constraints.


```kotlin
@Test
@Throws(Exception::class)
fun testWithConstraints() {
    // Define input data.
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    val constraints = Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .build()

    // Create request.
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .setConstraints(constraints)
        .build()

    val workManager = WorkManager.getInstance(myContext)
    val testDriver = checkNotNull(WorkManagerTestInitHelper.getTestDriver(myContext))
    // Enqueue.
    workManager.enqueue(request).result.get()
    // Tells the testing framework that all constraints are met.
    testDriver.setAllConstraintsMet(request.id)
    // Get WorkInfo and outputData.
    val workInfo = checkNotNull(workManager.getWorkInfoById(request.id).get())
    val outputData = workInfo.outputData

    // Assert.
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

<br />

### Testing Periodic Work

The `TestDriver` also exposes a `setPeriodDelayMet` which can be used to
indicate that an interval is complete. Here is an example of
`setPeriodDelayMet` being used.


```kotlin
@Test
@Throws(Exception::class)
fun testPeriodicWork() {
    // Define input data.
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request.
    val request = PeriodicWorkRequestBuilder<EchoWorker>(15, MINUTES)
        .setInputData(input)
        .build()

    val workManager = WorkManager.getInstance(myContext)
    val testDriver = checkNotNull(WorkManagerTestInitHelper.getTestDriver(myContext))
    // Enqueue and wait for result.
    workManager.enqueue(request).result.get()
    // Tells the testing framework the period delay is met.
    testDriver.setPeriodDelayMet(request.id)
    // Get WorkInfo and outputData.
    val workInfo = checkNotNull(workManager.getWorkInfoById(request.id).get())

    // Assert.
    assertThat(workInfo.state, `is`(WorkInfo.State.ENQUEUED))
}
```

<br />