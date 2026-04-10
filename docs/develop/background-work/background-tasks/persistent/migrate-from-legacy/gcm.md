---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/gcm
url: https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/gcm
source: md.txt
---

This document explains how to migrate apps to use the WorkManager client library
to perform background operations instead of the GCMNetworkManager library. The
preferred way for an app to schedule background jobs is to use WorkManager. By
also including the WorkManager GCM library, you can enable WorkManager to use
GCM to schedule the tasks when running on Android devices running API level 22
or lower.

## Migrate to WorkManager

If your app currently uses GCMNetworkManager to perform background operations,
follow these steps to migrate to WorkManager.

For the following steps, we assume you're starting with the following
GCMNetworkManager code, which defines and schedules your task:

### Kotlin

```kotlin
val myTask = OneoffTask.Builder()
    // setService() says what class does the work
    .setService(MyUploadService::class.java)
    // Don't run the task unless device is charging
    .setRequiresCharging(true)
    // Run the task between 5 & 15 minutes from now
    .setExecutionWindow(5 * DateUtil.MINUTE_IN_SECONDS,
            15 * DateUtil.MINUTE_IN_SECONDS)
    // Define a unique tag for the task
    .setTag("test-upload")
    // ...finally, build the task and assign its value to myTask
    .build()
GcmNetworkManager.getInstance(this).schedule(myTask)
```

### Java

```java
// In GcmNetworkManager, this call defines the task and its
// runtime constraints:
OneoffTask myTask = new OneoffTask.Builder()
    // setService() says what class does the work
    .setService(MyUploadService.class)
    // Don't run the task unless device is charging
    .setRequiresCharging(true)
    // Run the task between 5 & 15 minutes from now
    .setExecutionWindow(
        5 * DateUtil.MINUTE_IN_SECONDS,
        15 * DateUtil.MINUTE_IN_SECONDS)
    // Define a unique tag for the task
    .setTag("test-upload")
    // ...finally, build the task and assign its value to myTask
    .build();
GcmNetworkManager.getInstance(this).schedule(myTask);
```

In this example, we assume `MyUploadService` defines the actual upload operation:

### Kotlin

```kotlin
class MyUploadService : GcmTaskService() {
    fun onRunTask(params: TaskParams): Int {
        // Do some upload work
        return GcmNetworkManager.RESULT_SUCCESS
    }
}
```

### Java

```java
class MyUploadService extends GcmTaskService {
    @Override
    public int onRunTask(TaskParams params) {
        // Do some upload work
        return GcmNetworkManager.RESULT_SUCCESS;
    }
}
```

### Include the WorkManager libraries

To use the WorkManager classes, you need to add the WorkManager library to your
build dependencies. You also need to add the WorkManager GCM library, which
enables WorkManager to use GCM for job scheduling when your app is running on
devices that don't support JobScheduler (that is, devices running API level 22
or lower). For full details on adding the libraries, see [Getting started with
WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/basics).

### Modify your manifest

When you implemented GCMNetworkManager, you added an instance of
`GcmTaskService` to your app manifest, as described in the `GcmNetworkManager`
[reference documentation](https://developers.google.com/android/reference/com/google/android/gms/gcm/GcmNetworkManager).
`GcmTaskService` looks at the incoming task and delegates it to the task
handler. WorkManager manages task delegation to your Worker, so you no longer
need a class that does this; simply remove your `GcmTaskService` from the
manifest.

> [!NOTE]
> **Note:** You might have added logic to your `GcmTaskService` to do some work before dispatching the task to the handler. In that case, you need to refactor and move that logic into the [`Worker`](https://developer.android.com/reference/androidx/work/Worker) class you define in the next section.

### Define the Worker

Your GCMNetworkManager implementation defines a `OneoffTask` or `RecurringTask`,
which specifies just what work needs to be done. You need to rewrite that as a
`Worker`, as documented in [Defining your work
requests](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work).

> [!NOTE]
> **Note:** In GCMNetworkManager, the task defines both what work you want to do, and when the task should run. With the `WorkManager` library, you use two different classes to define these elements. The [`Worker`](https://developer.android.com/reference/androidx/work/Worker) defines the task you want to perform; when you create the [`WorkRequest`](https://developer.android.com/reference/androidx/work/WorkRequest), you specify any constraints on when the job should run.

The [sample GCMNetworkManager
code](https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/gcm#gcm-before)
defines a `myTask` task. The WorkManager equivalent looks like this:

### Kotlin

```kotlin
class UploadWorker(context: Context, params: WorkerParameters)
                        : Worker(context, params) {
    override fun doWork() : Result {
        // Do the upload operation ...
        myUploadOperation()

        // Indicate whether the task finished successfully with the Result
        return Result.success()
    }
}
```

### Java

```java
public class UploadWorker extends Worker {

    public UploadWorker(
        @NonNull Context context,
        @NonNull WorkerParameters params) {
        super(context, params);
    }

    @Override
    public Result doWork() {
      // Do the upload operation ...

      myUploadOperation()

      // Indicate whether the task finished successfully with the Result
      return Result.success()
    }
}
```

There are a few differences between the GCM task and the `Worker`:

- GCM uses a `TaskParams` object to pass parameters to the task. The `WorkManager` uses input data, which you can specify on the `WorkRequest`, as described in the `WorkManager` documentation for [Defining input/output for
  your task](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#input_output). In both cases, you can pass key/value pairs specifying any persistable parameters needed by the task.
- The `GcmTaskService` signals success or failure by returning flags like `GcmNetworkManager.RESULT_SUCCESS`. A WorkManager `Worker` signals its results by using a [`ListenableWorker.Result`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result) method, like [`ListenableWorker.Result.success()`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result#success()), and returning that method's return value.
- As we mentioned, you do not set the constraints or tags when you define the `Worker`; instead, you do this in the next step, when you create the `WorkRequest`.

### Schedule the work request

Defining a `Worker` specifies *what* you need done. To specify when the work
should be done, you need to define the
[`WorkRequest`](https://developer.android.com/reference/androidx/work/WorkRequest):

1. Create a [`OneTimeWorkRequest`](https://developer.android.com/reference/androidx/work/OneTimeWorkRequest) or [`PeriodicWorkRequest`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest), and set any desired constraints specifying when the task should run, as well as any tags to identify your work.
2. Pass the request to [`WorkManager.enqueue()`](https://developer.android.com/reference/androidx/work/WorkManager#enqueue(androidx.work.WorkRequest)) to have the task queued for execution.

For example, the [previous section](https://developer.android.com/develop/background-work/background-tasks/persistent/migrate-from-legacy/gcm#define-worker) showed how to convert a
`OneoffTask` to an equivalent `Worker`. However, that `Worker` did not include
the `OneoffTask` object's execution constraints and tag. Instead, we set the
constraints and task ID when we create the `WorkRequest`. We'll also specify
that the task must not run unless there's a network connection. You don't need
to explicitly request a network connection with GCMNetworkManager, since
GCMNetworkManager requires a network connection by default, but WorkManager does
not require a network connection unless you specifically add that constraint.
Once we've defined the `WorkRequest`, we enqueue it with WorkManager.

### Kotlin

```kotlin
val uploadConstraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresCharging(true).build()

val uploadTask = OneTimeWorkRequestBuilder&lt;UploadWorker>()
    .setConstraints(uploadConstraints)
    .build()
WorkManager.getInstance().enqueue(uploadTask)
```

### Java

```java
Constraints uploadConstraints = new Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresCharging(true)
    .build();

OneTimeWorkRequest uploadTask =
        new OneTimeWorkRequest.Builder(UploadWorker.class)
  .setConstraints(uploadConstraints)
  .build();
WorkManager.getInstance().enqueue(uploadTask);
```

> [!NOTE]
> **Note:** With GCMNetworkManager, every task must have a unique tag. The analogous WorkManager construct is the `WorkRequest` ID. This ID is automatically set by WorkManager when the request is created; you get the ID by calling [`WorkRequest.getId()`](https://developer.android.com/reference/androidx/work/WorkRequest#getId). WorkManager also allows you to define tags for your jobs, but these are different from GCMNetworkManager tags because they need not be unique; you might have several similar WorkManager tasks all enqueued at once, and all using the same tag.

> [!NOTE]
> **Note:** GCMNetworkManager requires you to define an execution window, but WorkManager does not require this. Instead, WorkManager runs the job as soon as possible after the constraints are met. In this example, we assume you don't actually need to set a specific time for the job to run.

## API mappings

This section describes how some GCMNetworkManager features and constraints map
onto WorkManager equivalents.

### Constraint mappings

GCMNetworkManager lets you set a number of constraints on when your task should
run. In most cases, there's a clear equivalent WorkManager constraint. This
section lists those equivalents.

Set constraints on GCMNetworkManager tasks by calling the appropriate method in
the task's Builder object; for example, you can set a network requirement by
calling [`Task.Builder.setRequiredNetwork()`](https://developer.google.com/android/reference/com/google/android/gms/gcm/Task.Builder.html#setRequiredNetwork(int)).

In WorkManager, you create a
[`Constraints.Builder`](https://developer.android.com/reference/androidx/work/Constraints.Builder) object and
call that object's methods to set constraints (for example,
[`Constraints.Builder.setRequiredNetworkType())`](https://developer.android.com/reference/androidx/work/Constraints.Builder#setRequiredNetworkType(androidx.work.NetworkType)),
then use the Builder to create a Constraints object which you can attach to the
work request. For more information, see [Defining your work
requests](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#constraints).

> [!NOTE]
> **Note:** GCMNetworkManager allows you to specify a specific execution window for your task. There is no equivalent functionality in WorkManager. If you need to do work at a precise time, we recommend using other options, like [`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager).

| GCMNetworkManager constraint | WorkManager equivalent | Notes |
|---|---|---|
| [`setPersisted()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder#setPersisted(boolean)) | *(not required)* | All WorkManager jobs are persisted across device reboots |
| [`setRequiredNetwork()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder#public-abstract-task.builder-setrequirednetwork-int-requirednetworkstate) | [`setRequiredNetworkType()`](https://developer.android.com/reference/androidx/work/Constraints.Builder#setRequiredNetworkType(androidx.work.NetworkType)) | By default GCMNetworkManager requires network access. WorkManager does not require network access by default. If your job requires network access, you must use `setRequiredNetworkType(CONNECTED)`, or set some more specific network type. |
| [`setRequiresCharging()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder#public-abstract-task.builder-setrequirescharging-boolean-requirescharging) |   |   |

### Other mappings

Besides constraints, there are other settings you can apply to GCMNetworkManager
tasks. This section lists the corresponding way to apply those settings to a
WorkManager job.

#### Tags

All GCMNetworkManager tasks must have a tag string, which you set by calling the
Builder's [`setTag()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder#setTag(java.lang.String))
method. WorkManager jobs are uniquely identified by an ID, which is
automatically generated by WorkManager; you can get that ID by calling
[`WorkRequest.getId()`](https://developer.android.com/reference/androidx/work/WorkRequest#getId()). In
addition, work requests can *optionally* have one or more tags. To set a tag for
your WorkManager job, call the
[`WorkRequest.Builder.addTag()`](https://developer.android.com/reference/androidx/work/WorkRequest.Builder#addTag(java.lang.String))
method, before you use that Builder to create the `WorkRequest`.

In GCMNetworkManager, you can call
[`setUpdateCurrent()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder.html#setUpdateCurrent(boolean))
to specify whether the task should replace any existing task with the same tag.
The equivalent WorkManager approach is to enqueue the task by calling
[`enqueueUniqueWork()`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniqueWork(java.lang.String,%2520androidx.work.ExistingWorkPolicy,%2520java.util.List%3Candroidx.work.OneTimeWorkRequest%3E))
or [`enqueueUniquePeriodicWork()`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniquePeriodicWork(java.lang.String,%2520androidx.work.ExistingPeriodicWorkPolicy,%2520androidx.work.PeriodicWorkRequest));
if you use these methods, you give the job a unique name, and also specify how
WorkManager should handle the request if there's already a pending job with that
name. For more information, see [Handling unique
work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/managing-work#unique-work).

#### Task parameters

You can pass parameters to a GCMNetworkManager job by calling
[`Task.Builder.setExtras()`](https://developers.google.com/android/reference/com/google/android/gms/gcm/Task.Builder#setExtras(android.os.Bundle))
and passing a `Bundle` containing the parameters. WorkManager allows you to pass
a `Data` object to the WorkManager job, containing the parameters as key/value
pairs. For details, see
[Assign input data](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#assign_input_data).