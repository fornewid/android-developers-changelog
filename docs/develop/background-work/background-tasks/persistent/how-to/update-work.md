---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/update-work
url: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/update-work
source: md.txt
---

WorkManager allows you to update a [`WorkRequest`](https://developer.android.com/reference/androidx/work/WorkRequest) after you have already
enenqueued it. This is often necessary in larger apps that frequently change
constraints or need to update their workers on the fly. As of WorkManager
version 2.8.0, the [`updateWork()`](https://developer.android.com/reference/androidx/work/WorkManager#updateWork(androidx.work.WorkRequest)) API is the means of doing this.

The `updateWork()` method allows you to change certain aspects of a
`WorkRequest` on the fly, without having to go through the process of manually
canceling and enqueuing a new one. This greatly simplifies the development
process.

## Avoid canceling work

You should generally avoid canceling an existing WorkRequest and enqueuing a new
one. Doing so can result in the app repeating certain tasks, and can require you
to write a significant amount of additional code.

Consider the following examples of where canceling a WorkRequest can cause
difficulties:

- **Back-end request:** If you cancel a [`Worker`](https://developer.android.com/reference/androidx/work/Worker) while it is computing a payload to send to the server, the new `Worker` needs to start over and recompute the potentially expensive payload.
- **Scheduling:** If you cancel a [`PeriodicWorkRequest`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest) and you would like the new `PeriodicWorkRequest` to execute on the same schedule, you need to calculate a time offset to ensure that the new execution time is aligned with the previous work request.

The `updateWork()` API allows you to update a work request's constraints and
other parameters without the trouble of canceling and enqueuing a new request.

### When to cancel work

There are cases where you should directly cancel a `WorkRequest` rather than
call `updateWork()`. This is what you should do when you wish to change the
fundamental nature of the work that you have enqueued.

> [!CAUTION]
> **Caution:** It is not possible to use `updateWork()` to change the type of `Worker` in a `WorkRequest`. For example, if you have enqueued a `OneTimeWorkRequest` and you would like for it to run periodically, you must cancel the request and schedule a new `PeriodicWorkRequest`.

### When to update work

Imagine a photo app that does a daily backup of the user's photos. It has
enqueued a `PeriodicWorkRequest` to do so. The `WorkRequest` has constraints
that require the device to be charging and connected to WiFi.

However, the user only charges their device for 20 minutes a day using a fast
charger. In this case, the app may want to update the `WorkRequest` to relax the
charging constraint, so that it can still upload the photos even if the device
isn't fully charged.

In this situation, you can use the `updateWork()` method to update the work
request's constraints.

## How to update work

The `updateWork()` method provides a simple means of updating an existing
`WorkRequest`, without having to cancel and enqueue a new one.

To use update enqueued work follow these steps:

1. **Get the existing ID for enqueued work** : Get the ID of the WorkRequest you would like to update. You can retrieve this ID with any of the [`getWorkInfo`](https://developer.android.com/reference/androidx/work/WorkManager#getWorkInfosByTag(java.lang.String)) APIs, or by manually persisting the ID from the initial WorkRequest for later retrieval with the public property [`WorkRequest.id`](https://developer.android.com/reference/androidx/work/WorkRequest#id()), before enqueuing it.
2. **Create new WorkRequest** : Create a new `WorkRequest` and use `WorkRequest.Builder.setID()` to set its ID to match that of the existing `WorkRequest`.
3. **Set constraints** : Use `WorkRequest.Builder.setConstraints()` to pass the WorkManager new constraints.
4. **Call updateWork** : Pass the new WorkRequest to `updateWork()`.

### Update work example

Here is an example code snippet in Kotlin that demonstrates how to use the
`updateWork()` method to change the battery constraints of a `WorkRequest` used
to upload photos:

    suspend fun updatePhotoUploadWork() {
        // Get instance of WorkManager.
        val workManager = WorkManager.getInstance(context)

        // Retrieve the work request ID. In this example, the work being updated is unique
        // work so we can retrieve the ID using the unique work name.
        val photoUploadWorkInfoList = workManager.getWorkInfosForUniqueWork(
            PHOTO_UPLOAD_WORK_NAME
        ).await()

        val existingWorkRequestId = photoUploadWorkInfoList.firstOrNull()?.id ?: return

        // Update the constraints of the WorkRequest to not require a charging device.
        val newConstraints = Constraints.Builder()
            // Add other constraints as required here.
            .setRequiresCharging(false)
            .build()

        // Create new WorkRequest from existing Worker, new constraints, and the id of the old WorkRequest.
        val updatedWorkRequest: WorkRequest =
            OneTimeWorkRequestBuilder<MyWorker>()
                .setConstraints(newConstraints)
                .setId(existingWorkRequestId)
                .build()

        // Pass the new WorkRequest to updateWork().
        workManager.updateWork(updatedWorkRequest)
    }

### Handle the result

`updateWork()` returns a `ListenableFuture<UpdateResult>`. The given
`UpdateResult` can have one of the several values that outline whether or not
WorkManager was able to apply your changes. It also indicates when it was able
to apply the change.

For more information, see the [`updateWork()`](https://developer.android.com/reference/androidx/work/WorkManager.UpdateResult) [and](https://developer.android.com/reference/androidx/work/WorkManager.UpdateResult) [`UpdateResult`](https://developer.android.com/reference/androidx/work/WorkManager.UpdateResult)
[reference](https://developer.android.com/reference/androidx/work/WorkManager.UpdateResult).

## Track work with generations

Each time you update a `WorkRequest`, its *generation* increments by one. This
lets you track exactly which `WorkRequest` is currently enqueued.
Generations provide you more control when observing, tracing, and testing work
requests.

To get the generation of a `WorkRequest`, follow these steps:

1. **WorkInfo** : Call `WorkManager.getWorkInfoById()` to retrieve an instance of [`WorkInfo`](https://developer.android.com/reference/androidx/work/WorkInfo) corresponding to your `WorkRequest`.
   - You can call one of several methods that return a `WorkInfo`. For more information, see the [WorkManager reference](https://developer.android.com/reference/androidx/work/WorkManager#getWorkInfoById(java.util.UUID)).
2. **getGeneration** : Call [`getGeneration()`](https://developer.android.com/reference/androidx/work/WorkInfo#getGeneration()) on the instance of `WorkInfo`. The `Int` returned corresponds to the generation of the `WorkRequest`.
   - Note that there isn't a generation field or property, only the `WorkInfo.getGeneration()` method.

### Track generation example

The following is an example implementation of the workflow described above for
retrieving the generation of a `WorkRequest`.

    // Get instance of WorkManager.
    val workManager = WorkManager.getInstance(context)

    // Retrieve WorkInfo instance.
    val workInfo = workManager.getWorkInfoById(oldWorkRequestId)

    // Call getGeneration to retrieve the generation.
    val generation = workInfo.getGeneration()

> [!NOTE]
> **Note:** The `UpdateResult` that `updateWork()` returns does not include the generation of the `WorkRequest`.

## Policies for updating work

Previously, the recommended solution to updating periodic work was to enqueue a
`PeriodicWorkRequest` with the policy [`ExistingPeriodicWorkPolicy.REPLACE`](https://developer.android.com/reference/androidx/work/ExistingPeriodicWorkPolicy#REPLACE).
If there was a pending `PeriodicWorkRequest` with the same unique `id`, the new
work request would cancel and delete it. This policy is now *deprecated* in
favor of the workflow using the [`ExistingPeriodicWorkPolicy.UPDATE`](https://developer.android.com/reference/androidx/work/ExistingPeriodicWorkPolicy#UPDATE).

For example, when using [`enqueueUniquePeriodicWork`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniquePeriodicWork(java.lang.String,androidx.work.ExistingPeriodicWorkPolicy,androidx.work.PeriodicWorkRequest)) with a
`PeriodicWorkRequest`, you can initialize the new `PeriodicWorkRequest` with the
`ExistingPeriodicWorkPolicy.UPDATE` policy. If there is a pending
`PeriodicWorkRequest` with the same unique name, WorkManager updates it to the
new specification. Following this workflow, it is not necessary to use
`updateWork()`.

> [!NOTE]
> **Note:** A similar update policy doesn't exist for `OneTimeWorkRequest`. This is because you can use the [`enqueueUniqueWork`](https://developer.android.com/reference/androidx/work/WorkManager#enqueueUniqueWork(java.lang.String,androidx.work.ExistingWorkPolicy,androidx.work.OneTimeWorkRequest)) method with the [`APPEND`](https://developer.android.com/reference/androidx/work/ExistingWorkPolicy#APPEND) or [`APPEND_OR_REPLACE`](https://developer.android.com/reference/androidx/work/ExistingWorkPolicy#APPEND_OR_REPLACE) policies. Doing so creates a chain of workers with the same name. As such, WorkManager can't effectively support an `UPDATE` policy for them, as it isn't possible to decide which workers in the chain it should update.