---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/firebase
url: https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/firebase
source: md.txt
---

# Migrating from Firebase JobDispatcher to WorkManager

WorkManager is a library for scheduling and executing deferrable background work in Android. It is the recommended replacement for Firebase JobDispatcher. The following guide will walk you through the process of migrating your Firebase JobDispatcher implementation to WorkManager.

## Gradle setup

To import the WorkManager library into your Android project, add the dependencies listed in[Getting started with WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/basics).

## From JobService to workers

[`FirebaseJobDispatcher`](https://github.com/googlearchive/firebase-jobdispatcher-android/blob/e609dabf6cbd0fcc2451b8515f095cfbc3d9450a/jobdispatcher/src/main/java/com/firebase/jobdispatcher/FirebaseJobDispatcher.java)uses a subclass of[`JobService`](https://github.com/firebase/firebase-jobdispatcher-android/blob/master/jobdispatcher/src/main/java/com/firebase/jobdispatcher/JobService.java)as an entry point for defining the work which needs to be done. You might be using`JobService`directly, or using[`SimpleJobService`](https://github.com/firebase/firebase-jobdispatcher-android/blob/master/jobdispatcher/src/main/java/com/firebase/jobdispatcher/SimpleJobService.java).

A`JobService`will look something like this:  

### Kotlin

```kotlin
import com.firebase.jobdispatcher.JobParameters
import com.firebase.jobdispatcher.JobService

class MyJobService : JobService() {
    override fun onStartJob(job: JobParameters): Boolean {
        // Do some work here
        return false // Answers the question: "Is there still work going on?"
    }
    override fun onStopJob(job: JobParameters): Boolean {
        return false // Answers the question: "Should this job be retried?"
    }
}
```

### Java

```java
import com.firebase.jobdispatcher.JobParameters;
import com.firebase.jobdispatcher.JobService;

public class MyJobService extends JobService {
    @Override
    public boolean onStartJob(JobParameters job) {
        // Do some work here

        return false; // Answers the question: "Is there still work going on?"
    }

    @Override
    public boolean onStopJob(JobParameters job) {
        return false; // Answers the question: "Should this job be retried?"
    }
}
```

If you are using`SimpleJobService`you will have overridden`onRunJob()`, which returns a`@JobResult int`type.

The key difference is when you are using`JobService`directly,`onStartJob()`is called on the main thread, and it is the app's responsibility to offload the work to a background thread. On the other hand, if you are using`SimpleJobService`, that service is responsible for executing your work on a background thread.

WorkManager has similar concepts. The fundamental unit of work in WorkManager is a[`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker). There are also other useful subtypes of workers like[`Worker`](https://developer.android.com/reference/androidx/work/Worker),[`RxWorker`](https://developer.android.com/reference/androidx/work/RxWorker), and`CoroutineWorker`(when using Kotlin coroutines).

### JobService maps to a ListenableWorker

If you are using`JobService`directly, then the worker it maps to is a`ListenableWorker`. If you are using`SimpleJobService`then you should use`Worker`instead.

Let's use the above example (`MyJobService`) and look at how we can convert it to a`ListenableWorker`.  

### Kotlin

```kotlin
import android.content.Context
import androidx.work.ListenableWorker
import androidx.work.ListenableWorker.Result
import androidx.work.WorkerParameters
import com.google.common.util.concurrent.ListenableFuture

class MyWorker(appContext: Context, params: WorkerParameters) :
    ListenableWorker(appContext, params) {

    override fun startWork(): ListenableFuture<ListenableWorker.Result> {
        // Do your work here.
        TODO("Return a ListenableFuture<Result>")
    }

    override fun onStopped() {
        // Cleanup because you are being stopped.
    }
}
```

### Java

```java
import android.content.Context;
import androidx.work.ListenableWorker;
import androidx.work.ListenableWorker.Result;
import androidx.work.WorkerParameters;
import com.google.common.util.concurrent.ListenableFuture;

class MyWorker extends ListenableWorker {

  public MyWorker(@NonNull Context appContext, @NonNull WorkerParameters params) {
    super(appContext, params);
  }

  @Override
  public ListenableFuture<ListenableWorker.Result> startWork() {
    // Do your work here.
    Data input = getInputData();

    // Return a ListenableFuture<>
  }

  @Override
  public void onStopped() {
    // Cleanup because you are being stopped.
  }
}
```

The basic unit of work in WorkManager is a`ListenableWorker`. Just like`JobService.onStartJob()`,`startWork()`is called on the main thread. Here`MyWorker`implements`ListenableWorker`and returns an instance of[`ListenableFuture`](https://google.github.io/guava/releases/21.0-rc1/api/docs/com/google/common/util/concurrent/ListenableFuture.html), which is used to signal work completion*asynchronously*. You should choose your own threading strategy here.

The`ListenableFuture`here eventually returns a`ListenableWorker.Result`type which can be one of`Result.success()`,`Result.success(Data outputData)`,`Result.retry()`,`Result.failure()`, or`Result.failure(Data outputData)`. For more information, see the reference page for[`ListenableWorker.Result`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result).

`onStopped()`is called to signal that the`ListenableWorker`needs to stop, either because the constraints are no longer being met (for example, because the network is no longer available), or because a`WorkManager.cancel...()`method was called.`onStopped()`may also be called if the OS decides to shut down your work for some reason.

### SimpleJobService maps to a Worker

When using`SimpleJobService`the above worker will look like:  

### Kotlin

```kotlin
import android.content.Context;
import androidx.work.Data;
import androidx.work.ListenableWorker.Result;
import androidx.work.Worker;
import androidx.work.WorkerParameters;


class MyWorker(context: Context, params: WorkerParameters) : Worker(context, params) {
    override fun doWork(): Result {
        TODO("Return a Result")
    }

    override fun onStopped() {
        super.onStopped()
        TODO("Cleanup, because you are being stopped")
    }
}
```

### Java

```java
import android.content.Context;
import androidx.work.Data;
import androidx.work.ListenableWorker.Result;
import androidx.work.Worker;
import androidx.work.WorkerParameters;

class MyWorker extends Worker {

  public MyWorker(@NonNull Context appContext, @NonNull WorkerParameters params) {
    super(appContext, params);
  }

  @Override
  public Result doWork() {
    // Do your work here.
    Data input = getInputData();

    // Return a ListenableWorker.Result
    Data outputData = new Data.Builder()
        .putString("Key", "value")
        .build();
    return Result.success(outputData);
  }

  @Override
  public void onStopped() {
    // Cleanup because you are being stopped.
  }
}
```

Here`doWork()`returns an instance of`ListenableWorker.Result`to signal work completion synchronously. This is similar to`SimpleJobService`, which schedules jobs on a background thread.

## JobBuilder maps to WorkRequest

FirebaseJobBuilder uses`Job.Builder`to represent`Job`metadata. WorkManager uses[`WorkRequest`](https://developer.android.com/reference/androidx/work/WorkRequest)to fill this role.

WorkManager has two types of`WorkRequest`s:[`OneTimeWorkRequest`](https://developer.android.com/reference/androidx/work/OneTimeWorkRequest)and[`PeriodicWorkRequest`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest).

If you are currently using`Job.Builder.setRecurring(true)`, then you should create a new`PeriodicWorkRequest`. Otherwise, you should use a`OneTimeWorkRequest`.

Let's look at what scheduling a complex`Job`with`FirebaseJobDispatcher`might look like:  

### Kotlin

```kotlin
val input: Bundle = Bundle().apply {
    putString("some_key", "some_value")
}

val job = dispatcher.newJobBuilder()
    // the JobService that will be called
    .setService(MyService::class.java)
    // uniquely identifies the job
    .setTag("my-unique-tag")
    // one-off job
    .setRecurring(false)
    // don't persist past a device reboot
    .setLifetime(Lifetime.UNTIL_NEXT_BOOT)
    // start between 0 and 60 seconds from now
    .setTrigger(Trigger.executionWindow(0, 60))
    // don't overwrite an existing job with the same tag
    .setReplaceCurrent(false)
    // retry with exponential backoff
    .setRetryStrategy(RetryStrategy.DEFAULT_EXPONENTIAL)

    .setConstraints(
        // only run on an unmetered network
        Constraint.ON_UNMETERED_NETWORK,
        // // only run when the device is charging
        Constraint.DEVICE_CHARGING
    )
    .setExtras(input)
    .build()

dispatcher.mustSchedule(job)
```

### Java

```java
Bundle input = new Bundle();
input.putString("some_key", "some_value");

Job myJob = dispatcher.newJobBuilder()
    // the JobService that will be called
    .setService(MyJobService.class)
    // uniquely identifies the job
    .setTag("my-unique-tag")
    // one-off job
    .setRecurring(false)
    // don't persist past a device reboot
    .setLifetime(Lifetime.UNTIL_NEXT_BOOT)
    // start between 0 and 60 seconds from now
    .setTrigger(Trigger.executionWindow(0, 60))
    // don't overwrite an existing job with the same tag
    .setReplaceCurrent(false)
    // retry with exponential backoff
    .setRetryStrategy(RetryStrategy.DEFAULT_EXPONENTIAL)
    // constraints that need to be satisfied for the job to run
    .setConstraints(
        // only run on an unmetered network
        Constraint.ON_UNMETERED_NETWORK,
        // only run when the device is charging
        Constraint.DEVICE_CHARGING
    )
    .setExtras(input)
    .build();

dispatcher.mustSchedule(myJob);
```

To achieve the same with WorkManager you will need to:

- Build input data which can be used as input for the`Worker`.
- Build a`WorkRequest`with the input data and constraints similar to the ones defined above for`FirebaseJobDispatcher`.
- Enqueue the`WorkRequest`.

### Setting up inputs for the Worker

`FirebaseJobDispatcher`uses a`Bundle`to send input data to the`JobService`. WorkManager uses[`Data`](https://developer.android.com/reference/androidx/work/Data.Builder)instead. So that becomes:  

### Kotlin

```kotlin
import androidx.work.workDataOf
val data = workDataOf("some_key" to "some_val")
```

### Java

```java
import androidx.work.Data;
Data input = new Data.Builder()
    .putString("some_key", "some_value")
    .build();
```

### Setting up Constraints for the Worker

`FirebaseJobDispatcher`uses[`Job.Builder.setConstaints(...)`](https://github.com/firebase/firebase-jobdispatcher-android/blob/master/jobdispatcher/src/main/java/com/firebase/jobdispatcher/Job.java#L287)to set up constraints on jobs. WorkManager uses[`Constraints`](https://developer.android.com/reference/androidx/work/Constraints)instead.  

### Kotlin

```kotlin
import androidx.work.*

val constraints: Constraints = Constraints.Builder().apply {
    setRequiredNetworkType(NetworkType.CONNECTED)
    setRequiresCharging(true)
}.build()
```

### Java

```java
import androidx.work.Constraints;
import androidx.work.Constraints.Builder;
import androidx.work.NetworkType;

Constraints constraints = new Constraints.Builder()
    // The Worker needs Network connectivity
    .setRequiredNetworkType(NetworkType.CONNECTED)
    // Needs the device to be charging
    .setRequiresCharging(true)
    .build();
```

### Creating the WorkRequest (OneTime or Periodic)

To create`OneTimeWorkRequest`s and`PeriodicWorkRequest`s you should use[`OneTimeWorkRequest.Builder`](https://developer.android.com/reference/androidx/work/OneTimeWorkRequest.Builder)and[`PeriodicWorkRequest.Builder`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest.Builder).

To create a`OneTimeWorkRequest`which is similar to the above`Job`you should do the following:  

### Kotlin

```kotlin
import androidx.work.*
import java.util.concurrent.TimeUnit

val constraints: Constraints = TODO("Define constraints as above")
val request: OneTimeWorkRequest =
     // Tell which work to execute
     OneTimeWorkRequestBuilder<MyWorker>()
         // Sets the input data for the ListenableWorker
        .setInputData(input)
        // If you want to delay the start of work by 60 seconds
        .setInitialDelay(60, TimeUnit.SECONDS)
        // Set a backoff criteria to be used when retry-ing
        .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30000, TimeUnit.MILLISECONDS)
        // Set additional constraints
        .setConstraints(constraints)
        .build()
```

### Java

```java
import androidx.work.BackoffCriteria;
import androidx.work.Constraints;
import androidx.work.Constraints.Builder;
import androidx.work.NetworkType;
import androidx.work.OneTimeWorkRequest;
import androidx.work.OneTimeWorkRequest.Builder;
import androidx.work.Data;

// Define constraints (as above)
Constraints constraints = ...
OneTimeWorkRequest request =
    // Tell which work to execute
    new OneTimeWorkRequest.Builder(MyWorker.class)
        // Sets the input data for the ListenableWorker
        .setInputData(inputData)
        // If you want to delay the start of work by 60 seconds
        .setInitialDelay(60, TimeUnit.SECONDS)
        // Set a backoff criteria to be used when retry-ing
        .setBackoffCriteria(BackoffCriteria.EXPONENTIAL, 30000, TimeUnit.MILLISECONDS)
        // Set additional constraints
        .setConstraints(constraints)
        .build();
```

The key difference here is that WorkManager's jobs are always persisted across device reboot automatically.

If you want to create a`PeriodicWorkRequest`then you would do something like:  

### Kotlin

```kotlin
val constraints: Constraints = TODO("Define constraints as above")
val request: PeriodicWorkRequest =
PeriodicWorkRequestBuilder<MyWorker>(15, TimeUnit.MINUTES)
    // Sets the input data for the ListenableWorker
    .setInputData(input)
    // Other setters
    .build()
```

### Java

```java
import androidx.work.BackoffCriteria;
import androidx.work.Constraints;
import androidx.work.Constraints.Builder;
import androidx.work.NetworkType;
import androidx.work.PeriodicWorkRequest;
import androidx.work.PeriodicWorkRequest.Builder;
import androidx.work.Data;

// Define constraints (as above)
Constraints constraints = ...

PeriodicWorkRequest request =
    // Executes MyWorker every 15 minutes
    new PeriodicWorkRequest.Builder(MyWorker.class, 15, TimeUnit.MINUTES)
        // Sets the input data for the ListenableWorker
        .setInputData(input)
        . // other setters (as above)
        .build();
```

## Scheduling work

Now that you have defined a`Worker`and a`WorkRequest`, you are ready to schedule work.

Every`Job`defined with`FirebaseJobDispatcher`had a`tag`which was used to*uniquely identify* a`Job`. It also provided a way for the application to tell the scheduler if this instance of a`Job`was to replace an existing copy of the`Job`by calling`setReplaceCurrent`.  

### Kotlin

```kotlin
val job = dispatcher.newJobBuilder()
    // the JobService that will be called
    .setService(MyService::class.java)
    // uniquely identifies the job
    .setTag("my-unique-tag")
    // don't overwrite an existing job with the same tag
    .setRecurring(false)
    // Other setters...
    .build()
```

### Java

```java
Job myJob = dispatcher.newJobBuilder()
    // the JobService that will be called
    .setService(MyJobService.class)
    // uniquely identifies the job
    .setTag("my-unique-tag")
    // don't overwrite an existing job with the same tag
    .setReplaceCurrent(false)
    // other setters
    // ...

dispatcher.mustSchedule(myJob);
```

When using WorkManager, you can achieve the same result by using`enqueueUniqueWork()`and`enqueueUniquePeriodicWork()`APIs (when using a`OneTimeWorkRequest`and a`PeriodicWorkRequest`, respectively). For more information, see the reference pages for[`WorkManager.enqueueUniqueWork()`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniqueWork(java.lang.String,%20androidx.work.ExistingWorkPolicy,%20androidx.work.OneTimeWorkRequest))and[`WorkManager.enqueueUniquePeriodicWork()`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniquePeriodicWork(java.lang.String,%20androidx.work.ExistingPeriodicWorkPolicy,%20androidx.work.PeriodicWorkRequest)).

This will look something like:  

### Kotlin

```kotlin
import androidx.work.*

val request: OneTimeWorkRequest = TODO("A WorkRequest")
WorkManager.getInstance(myContext)
    .enqueueUniqueWork("my-unique-name", ExistingWorkPolicy.KEEP, request)
```

### Java

```java
import androidx.work.ExistingWorkPolicy;
import androidx.work.OneTimeWorkRequest;
import androidx.work.WorkManager;

OneTimeWorkRequest workRequest = // a WorkRequest;
WorkManager.getInstance(myContext)
    // Use ExistingWorkPolicy.REPLACE to cancel and delete any existing pending
    // (uncompleted) work with the same unique name. Then, insert the newly-specified
    // work.
    .enqueueUniqueWork("my-unique-name", ExistingWorkPolicy.KEEP, workRequest);
```
| **Note:** `Job`tags in FirebaseJobDispatcher map to the`name`of the`WorkRequest`for WorkManager.

## Cancelling work

With`FirebaseJobDispatcher`you could cancel work using:  

### Kotlin

```kotlin
dispatcher.cancel("my-unique-tag")
```

### Java

```java
dispatcher.cancel("my-unique-tag");
```

When using WorkManager you can use:  

### Kotlin

```kotlin
import androidx.work.WorkManager
WorkManager.getInstance(myContext).cancelUniqueWork("my-unique-name")
```

### Java

```java
import androidx.work.WorkManager;
WorkManager.getInstance(myContext).cancelUniqueWork("my-unique-name");
```

## Initializing WorkManager

WorkManager typically initializes itself by using a`ContentProvider`. If you require more control over how WorkManager organizes and schedules work, you can[customize the WorkManager configuration and initialization](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration).