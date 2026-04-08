---
title: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/integration-testing
url: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/integration-testing
source: md.txt
---

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
[WorkManager release notes](https://developer.android.com/jetpack/androidx/releases/work#declaring_dependencies).

> [!NOTE]
> **Note:** Beginning with 2.1.0, WorkManager provides the [`TestWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestWorkerBuilder) and [`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder) classes, which let you test the business logic in your workers without having to initialize `WorkManager` with `WorkManagerTestInitHelper`. [Testing Worker implementation](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/testing-worker-impl) covers these classes. The material in this page is still useful for when you need to perform integration tests.

> [!NOTE]
> **Note:** It is highly recommended to use [`TestListenableWorkerBuilder`](https://developer.android.com/reference/androidx/work/testing/TestListenableWorkerBuilder) to test [`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker) implementations, as the `work-testing` artifact uses [Dispatchers.Default](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-default.html) rather than your worker implementation's [CoroutineDispatcher](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/). More information about this API can be found at [Testing Worker implementation](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/testing-worker-impl#testing_listenableworker_and_its_variants).

## Concepts

`work-testing` provides a special implementation of WorkManager for test mode,
which is initialized using
[`WorkManagerTestInitHelper`](https://developer.android.com/reference/androidx/work/testing/WorkManagerTestInitHelper).

The `work-testing` artifact also provides a
[`SynchronousExecutor`](https://developer.android.com/reference/androidx/work/testing/SynchronousExecutor)
which makes it easier to write tests in a synchronous manner, without having to
deal with multiple threads, locks, or latches.

Here is an example on how to use all these classes together.

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
class BasicInstrumentationTest {
    @Before
    fun setup() {
        val context = InstrumentationRegistry.getTargetContext()
        val config = Configuration.Builder()
            .setMinimumLoggingLevel(Log.DEBUG)
            .setExecutor(SynchronousExecutor())
            .build()

        // Initialize WorkManager for instrumentation tests.
        WorkManagerTestInitHelper.initializeTestWorkManager(context, config)
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
public class BasicInstrumentationTest {
    @Before
    public void setup() {
        Context context = InstrumentationRegistry.getTargetContext();
        Configuration config = new Configuration.Builder()
                .setMinimumLoggingLevel(Log.DEBUG)
                .setExecutor(new SynchronousExecutor())
                .build();

        // Initialize WorkManager for instrumentation tests.
        WorkManagerTestInitHelper.initializeTestWorkManager(
            context, config);
    }
}
```

## Structuring Tests

Now that WorkManager has been initialized in test mode, you are ready to test
your workers.

Let's say you have an `EchoWorker` which expects some `inputData`, and simply
copies (echoes) its input to `outputData`.

### Kotlin

```kotlin
class EchoWorker(context: Context, parameters: WorkerParameters)
   : Worker(context, parameters) {
   override fun doWork(): Result {
       return when(inputData.size()) {
           0 -> Result.failure()
           else -> Result.success(inputData)
       }
   }
}
```

### Java

```java
public class EchoWorker extends Worker {
  public EchoWorker(Context context, WorkerParameters parameters) {
      super(context, parameters);
  }

  @NonNull
  @Override
  public Result doWork() {
      Data input = getInputData();
      if (input.size() == 0) {
          return Result.failure();
      } else {
          return Result.success(input);
      }
  }
}
```

### Basic Tests

Below is an Android Instrumentation test that tests `EchoWorker`. The main
takeaway here is that testing `EchoWorker` in test mode is very similar to how
you would use `EchoWorker` in a real application.

### Kotlin

```kotlin
@Test
@Throws(Exception::class)
fun testSimpleEchoWorker() {
    // Define input data
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .build()

    val workManager = WorkManager.getInstance(applicationContext)
    // Enqueue and wait for result. This also runs the Worker synchronously
    // because we are using a SynchronousExecutor.
    workManager.enqueue(request).result.get()
    // Get WorkInfo and outputData
    val workInfo = workManager.getWorkInfoById(request.id).get()
    val outputData = workInfo.outputData

    // Assert
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

### Java

```java
@Test
public void testSimpleEchoWorker() throws Exception {
   // Define input data
   Data input = new Data.Builder()
           .put(KEY_1, 1)
           .put(KEY_2, 2)
           .build();

   // Create request
   OneTimeWorkRequest request =
       new OneTimeWorkRequest.Builder(EchoWorker.class)
           .setInputData(input)
           .build();

   WorkManager workManager = WorkManager.getInstance(getApplicationContext());
   // Enqueue and wait for result. This also runs the Worker synchronously
   // because we are using a SynchronousExecutor.
   workManager.enqueue(request).getResult().get();
   // Get WorkInfo and outputData
   WorkInfo workInfo = workManager.getWorkInfoById(request.getId()).get();
   Data outputData = workInfo.getOutputData();

   // Assert
   assertThat(workInfo.getState(), is(WorkInfo.State.SUCCEEDED));
   assertThat(outputData, is(input));
}
```

Let's write another test which makes sure that when `EchoWorker` gets no input
data, the expected `Result` is a `Result.failure()`.

### Kotlin

```kotlin
@Test
@Throws(Exception::class)
fun testEchoWorkerNoInput() {
   // Create request
   val request = OneTimeWorkRequestBuilder<EchoWorker>()
       .build()

   val workManager = WorkManager.getInstance(applicationContext)
   // Enqueue and wait for result. This also runs the Worker synchronously
   // because we are using a SynchronousExecutor.
   workManager.enqueue(request).result.get()
   // Get WorkInfo
   val workInfo = workManager.getWorkInfoById(request.id).get()

   // Assert
   assertThat(workInfo.state, `is`(WorkInfo.State.FAILED))
}
```

### Java

```java
@Test
public void testEchoWorkerNoInput() throws Exception {
  // Create request
  OneTimeWorkRequest request =
      new OneTimeWorkRequest.Builder(EchoWorker.class)
         .build();

  WorkManager workManager = WorkManager.getInstance(getApplicationContext());
  // Enqueue and wait for result. This also runs the Worker synchronously
  // because we are using a SynchronousExecutor.
  workManager.enqueue(request).getResult().get();
  // Get WorkInfo
  WorkInfo workInfo = workManager.getWorkInfoById(request.getId()).get();

  // Assert
  assertThat(workInfo.getState(), is(WorkInfo.State.FAILED));
}
```

## Simulate constraints, delays, and periodic work

`WorkManagerTestInitHelper` provides you with an instance of
[`TestDriver`](https://developer.android.com/reference/androidx/work/testing/TestDriver) which can be used
to simulate initial delay, conditions where constraints are met for
`ListenableWorker` instances, and, intervals for `PeriodicWorkRequest`
instances.

### Test Initial Delays

Workers can have initial delays. To test `EchoWorker` with an `initialDelay`,
rather than having to wait for the `initialDelay` in your test, you can use
the `TestDriver` to mark the work request's initial delay as met using
`setInitialDelayMet`.

### Kotlin

```kotlin
@Test
@Throws(Exception::class)
fun testWithInitialDelay() {
    // Define input data
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .setInitialDelay(10, TimeUnit.SECONDS)
        .build()

    val workManager = WorkManager.getInstance(getApplicationContext())
    // Get the TestDriver
    val testDriver = WorkManagerTestInitHelper.getTestDriver()
    // Enqueue
    workManager.enqueue(request).result.get()
    // Tells the WorkManager test framework that initial delays are now met.
    testDriver.setInitialDelayMet(request.id)
    // Get WorkInfo and outputData
    val workInfo = workManager.getWorkInfoById(request.id).get()
    val outputData = workInfo.outputData

    // Assert
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

### Java

```java
@Test
public void testWithInitialDelay() throws Exception {
  // Define input data
  Data input = new Data.Builder()
          .put(KEY_1, 1)
          .put(KEY_2, 2)
          .build();

  // Create request
  OneTimeWorkRequest request = new OneTimeWorkRequest.Builder(EchoWorker.class)
          .setInputData(input)
          .setInitialDelay(10, TimeUnit.SECONDS)
          .build();

  WorkManager workManager = WorkManager.getInstance(myContext);
  // Get the TestDriver
  TestDriver testDriver = WorkManagerTestInitHelper.getTestDriver();
  // Enqueue
  workManager.enqueue(request).getResult().get();
  // Tells the WorkManager test framework that initial delays are now met.
  testDriver.setInitialDelayMet(request.getId());
  // Get WorkInfo and outputData
  WorkInfo workInfo = workManager.getWorkInfoById(request.getId()).get();
  Data outputData = workInfo.getOutputData();

  // Assert
  assertThat(workInfo.getState(), is(WorkInfo.State.SUCCEEDED));
  assertThat(outputData, is(input));
}
```

### Testing Constraints

`TestDriver` can also be used to mark constraints as met using
`setAllConstraintsMet`. Here is an example on how you can test a `Worker`
with constraints.

### Kotlin

```kotlin
@Test
@Throws(Exception::class)
fun testWithConstraints() {
    // Define input data
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    val constraints = Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .build()

    // Create request
    val request = OneTimeWorkRequestBuilder<EchoWorker>()
        .setInputData(input)
        .setConstraints(constraints)
        .build()

    val workManager = WorkManager.getInstance(myContext)
    val testDriver = WorkManagerTestInitHelper.getTestDriver()
    // Enqueue
    workManager.enqueue(request).result.get()
    // Tells the testing framework that all constraints are met.
    testDriver.setAllConstraintsMet(request.id)
    // Get WorkInfo and outputData
    val workInfo = workManager.getWorkInfoById(request.id).get()
    val outputData = workInfo.outputData

    // Assert
    assertThat(workInfo.state, `is`(WorkInfo.State.SUCCEEDED))
    assertThat(outputData, `is`(input))
}
```

### Java

```java
@Test
public void testWithConstraints() throws Exception {
    // Define input data
    Data input = new Data.Builder()
            .put(KEY_1, 1)
            .put(KEY_2, 2)
            .build();

    // Define constraints
    Constraints constraints = new Constraints.Builder()
            .setRequiresDeviceIdle(true)
            .build();

    // Create request
    OneTimeWorkRequest request = new OneTimeWorkRequest.Builder(EchoWorker.class)
            .setInputData(input)
            .setConstraints(constraints)
            .build();

    WorkManager workManager = WorkManager.getInstance(myContext);
    TestDriver testDriver = WorkManagerTestInitHelper.getTestDriver();
    // Enqueue
    workManager.enqueue(request).getResult().get();
    // Tells the testing framework that all constraints are met.
    testDriver.setAllConstraintsMet(request.getId());
    // Get WorkInfo and outputData
    WorkInfo workInfo = workManager.getWorkInfoById(request.getId()).get();
    Data outputData = workInfo.getOutputData();

    // Assert
    assertThat(workInfo.getState(), is(WorkInfo.State.SUCCEEDED));
    assertThat(outputData, is(input));
}
```

### Testing Periodic Work

The `TestDriver` also exposes a `setPeriodDelayMet` which can be used to
indicate that an interval is complete. Here is an example of
`setPeriodDelayMet` being used.

### Kotlin

```kotlin
@Test
@Throws(Exception::class)
fun testPeriodicWork() {
    // Define input data
    val input = workDataOf(KEY_1 to 1, KEY_2 to 2)

    // Create request
    val request = PeriodicWorkRequestBuilder<EchoWorker>(15, MINUTES)
        .setInputData(input)
        .build()

    val workManager = WorkManager.getInstance(myContext)
    val testDriver = WorkManagerTestInitHelper.getTestDriver()
    // Enqueue and wait for result.
    workManager.enqueue(request).result.get()
    // Tells the testing framework the period delay is met
    testDriver.setPeriodDelayMet(request.id)
    // Get WorkInfo and outputData
    val workInfo = workManager.getWorkInfoById(request.id).get()

    // Assert
    assertThat(workInfo.state, `is`(WorkInfo.State.ENQUEUED))
}
```

### Java

```java
@Test
public void testPeriodicWork() throws Exception {
    // Define input data
    Data input = new Data.Builder()
            .put(KEY_1, 1)
            .put(KEY_2, 2)
            .build();

    // Create request
    PeriodicWorkRequest request =
            new PeriodicWorkRequest.Builder(EchoWorker.class, 15, MINUTES)
            .setInputData(input)
            .build();

    WorkManager workManager = WorkManager.getInstance(myContext);
    TestDriver testDriver = WorkManagerTestInitHelper.getTestDriver();
    // Enqueue and wait for result.
    workManager.enqueue(request).getResult().get();
    // Tells the testing framework the period delay is met
    testDriver.setPeriodDelayMet(request.getId());
    // Get WorkInfo and outputData
    WorkInfo workInfo = workManager.getWorkInfoById(request.getId()).get();

    // Assert
    assertThat(workInfo.getState(), is(WorkInfo.State.ENQUEUED));
}
```