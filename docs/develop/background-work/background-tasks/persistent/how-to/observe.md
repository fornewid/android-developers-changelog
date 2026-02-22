---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/observe
url: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/observe
source: md.txt
---

# Observe intermediate worker progress

WorkManager has built-in support for setting and observing intermediate progress for workers. If the worker was running while the app was in the foreground, this information can also be shown to the user using APIs which return the[`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData)of[`WorkInfo`](https://developer.android.com/reference/androidx/work/WorkInfo).

[`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker)now supports the[`setProgressAsync()`](https://developer.android.com/reference/androidx/work/ListenableWorker#setProgressAsync(androidx.work.Data))API, which allows it to persist intermediate progress. These APIs allow developers to set intermediate progress that can be observed by the UI. Progress is represented by the[`Data`](https://developer.android.com/reference/androidx/work/Data)type, which is a serializable container of properties (similar to[`input`and`output`](https://developer.android.com/topic/libraries/architecture/workmanager/advanced#params), and subject to the same restrictions).

Progress information can only be observed and updated while the`ListenableWorker`is running. Attempts to set progress on a`ListenableWorker`after it has completed its execution are ignored.

You can also observe progress information by using the one of the[`getWorkInfoBy...()`or`getWorkInfoBy...LiveData()`](https://developer.android.com/reference/androidx/work/WorkManager#getWorkInfoById(java.util.UUID))methods. These methods return instances of[`WorkInfo`](https://developer.android.com/reference/androidx/work/WorkInfo), which has a new[`getProgress()`](https://developer.android.com/reference/androidx/work/WorkInfo#getProgress())method that returns`Data`.

## Update progress

For Java developers using a[`ListenableWorker`](https://developer.android.com/reference/androidx/work/ListenableWorker)or a[`Worker`](https://developer.android.com/reference/androidx/work/Worker), the[`setProgressAsync()`](https://developer.android.com/reference/androidx/work/ListenableWorker#setProgressAsync(androidx.work.Data))API returns a`ListenableFuture<Void>`; updating progress is asynchronous, given that the update process involves storing progress information in a database. In Kotlin, you can use the[`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker)object's[`setProgress()`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker#setprogress)extension function to update progress information.

This example shows a`ProgressWorker`. The`Worker`sets its progress to 0 when it starts, and upon completion updates the progress value to 100.  

### Kotlin

    import android.content.Context
    import androidx.work.CoroutineWorker
    import androidx.work.Data
    import androidx.work.WorkerParameters
    import kotlinx.coroutines.delay

    class ProgressWorker(context: Context, parameters: WorkerParameters) :
        CoroutineWorker(context, parameters) {

        companion object {
            const val Progress = "Progress"
            private const val delayDuration = 1L
        }

        override suspend fun doWork(): Result {
            val firstUpdate = workDataOf(Progress to 0)
            val lastUpdate = workDataOf(Progress to 100)
            setProgress(firstUpdate)
            delay(delayDuration)
            setProgress(lastUpdate)
            return Result.success()
        }
    }

### Java

    import android.content.Context;
    import androidx.annotation.NonNull;
    import androidx.work.Data;
    import androidx.work.Worker;
    import androidx.work.WorkerParameters;

    public class ProgressWorker extends Worker {

        private static final String PROGRESS = "PROGRESS";
        private static final long DELAY = 1000L;

        public ProgressWorker(
            @NonNull Context context,
            @NonNull WorkerParameters parameters) {
            super(context, parameters);
            // Set initial progress to 0
            setProgressAsync(new Data.Builder().putInt(PROGRESS, 0).build());
        }

        @NonNull
        @Override
        public Result doWork() {
            try {
                // Doing work.
                Thread.sleep(DELAY);
            } catch (InterruptedException exception) {
                // ... handle exception
            }
            // Set progress to 100 after you are done doing your work.
            setProgressAsync(new Data.Builder().putInt(PROGRESS, 100).build());
            return Result.success();
        }
    }

## Observe progress

To observe progress information, use the[`getWorkInfoById`](https://developer.android.com/reference/androidx/work/WorkManager#getWorkInfoById(java.util.UUID))methods, and get a reference to[`WorkInfo`](https://developer.android.com/reference/androidx/work/WorkInfo).

Here is an example which uses`getWorkInfoByIdFlow`for Kotlin and`getWorkInfoByIdLiveData`for Java.  

### Kotlin

    WorkManager.getInstance(applicationContext)
          // requestId is the WorkRequest id
          .getWorkInfoByIdFlow(requestId)
          .collect { workInfo: WorkInfo? ->
              if (workInfo != null) {
                  val progress = workInfo.progress
                  val value = progress.getInt("Progress", 0)
                  // Do something with progress information
              }
          }

### Java

    WorkManager.getInstance(getApplicationContext())
         // requestId is the WorkRequest id
         .getWorkInfoByIdLiveData(requestId)
         .observe(lifecycleOwner, new Observer<WorkInfo>() {
                 @Override
                 public void onChanged(@Nullable WorkInfo workInfo) {
                     if (workInfo != null) {
                         Data progress = workInfo.getProgress();
                         int value = progress.getInt(PROGRESS, 0)
                         // Do something with progress
                 }
          }
    });

## Observe stop reason state

To debug why a`Worker`was stopped, you can log the stop reason by calling[`WorkInfo.getStopReason()`](https://developer.android.com/reference/androidx/work/WorkInfo#getStopReason()):  

### Kotlin

    workManager.getWorkInfoByIdFlow(syncWorker.id)
      .collect { workInfo ->
          if (workInfo != null) {
            val stopReason = workInfo.stopReason
            logStopReason(syncWorker.id, stopReason)
          }
      }

### Java

      workManager.getWorkInfoByIdLiveData(syncWorker.id)
        .observe(getViewLifecycleOwner(), workInfo -> {
            if (workInfo != null) {
              int stopReason = workInfo.getStopReason();
              logStopReason(syncWorker.id, workInfo.getStopReason());
            }
      });

For more documentation the lifecycle and states of`Worker`objects, read[Work states](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/states).