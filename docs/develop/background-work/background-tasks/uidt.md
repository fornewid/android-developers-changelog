---
title: https://developer.android.com/develop/background-work/background-tasks/uidt
url: https://developer.android.com/develop/background-work/background-tasks/uidt
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/background-tasks/llms.txt

If you need to perform a data transfer that may take a long time, you can create
a [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler.md.txt) job and identify it as a *user-initiated data
transfer (UIDT)* job. UIDT jobs are intended for longer-duration data transfers
that are initiated by the device user, such as downloading a file from a remote
server. UIDT jobs were introduced with Android 14 (API level 34).

User-initiated data transfer jobs are started by the user. These jobs require a
notification, start immediately, and may be able to run for an extended period
of time as system conditions allow. You can run several user-initiated data
transfer jobs concurrently.

User initiated jobs must be scheduled while the application is visible to the
user (or in one of the [allowed conditions](https://developer.android.com/develop/background-work/background-tasks/uidt.md.txt#conditions-that-allow-scheduling)). After all constraints are met,
user initiated jobs can be executed by the OS, subject to system health
restrictions. The system may also use the provided estimated payload size to
determine how long the job executes.

> [!NOTE]
> **Note:** If you're currently using [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) for network data transfer use cases that are short duration and interruptible, we recommend that you continue using WorkManager instead of changing to user-initiated data transfer jobs. To understand better if you should be using UIDT, see the [Data transfer background
> task options](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options) documentation.

## Schedule user-initiated data transfer jobs

To run a user initiated data-transfer job, do the following:

1. Make sure your app has declared the [`JobService`](https://developer.android.com/reference/android/app/job/JobService.md.txt) and associated
   permissions in its manifest:

   ```xml
   <service android:name="com.example.app.CustomTransferService"
           android:permission="android.permission.BIND_JOB_SERVICE"
           android:exported="false">
           ...
   </service>
   ```

   Also, define a concrete subclass of `JobService` for your data transfer:


   ```kotlin
   class CustomTransferService : JobService() {
       // ...
   }
   ```

   <br />

2. Declare the `RUN_USER_INITIATED_JOBS` permission in the manifest:

   ```xml
   <manifest ...>
       <uses-permission android:name="android.permission.RUN_USER_INITIATED_JOBS" />
       <application ...>
           ...
       </application>
   </manifest>
   ```
3. Call the [`setUserInitiated()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder.md.txt#setUserInitiated(boolean)) method when building a
   `JobInfo` object. (This method is available beginning with
   Android 14.) We also recommend that you offer a payload size
   estimate by calling [`setEstimatedNetworkBytes()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder.md.txt#setEstimatedNetworkBytes(long,%20long))
   while creating your job.


   ```kotlin
   val networkRequestBuilder = NetworkRequest.Builder()
       // Add or remove capabilities based on your requirements.
       // For example, this code specifies that the job won't run
       // unless there's a connection to the internet (not just a local
       // network), and the connection doesn't charge per-byte.
       .addCapability(NET_CAPABILITY_INTERNET)
       .addCapability(NET_CAPABILITY_NOT_METERED)
       .build()

   val jobInfo = JobInfo.Builder(
       jobId,
       ComponentName(mContext, CustomTransferService::class.java)
   )
       // ...
       .setUserInitiated(true)
       .setRequiredNetwork(networkRequestBuilder)
       // Provide your estimate of the network traffic here.
       .setEstimatedNetworkBytes(1024 * 1024 * 1024, 1024 * 1024 * 1024)
       // ...
       .build()
   ```

   <br />

4. While the job is being executed, call
   [`setNotification()`](https://developer.android.com/reference/android/app/job/JobService.md.txt#setNotification(android.app.job.JobParameters,%20int,%20android.app.Notification,%20int)) on the `JobService` object. Calling
   `setNotification()` makes the user aware that the job is running, both in
   the Task Manager and in the status bar notification area.

   When execution is complete, call `jobFinished()` to signal to the system
   that the job is complete, or that the job should be rescheduled.


   ```kotlin
   class CustomTransferService : JobService() {
       private val scope = CoroutineScope(Dispatchers.IO)

       @RequiresApi(Build.VERSION_CODES.UPSIDE_DOWN_CAKE)
       override fun onStartJob(params: JobParameters): Boolean {
           val notification = Notification.Builder(
               applicationContext,
               NOTIFICATION_CHANNEL_ID
           )
               .setContentTitle("My user-initiated data transfer job")
               .setSmallIcon(android.R.mipmap.sym_def_app_icon)
               .setContentText("Job is running")
               .build()

           setNotification(
               params, NOTIFICATION_ID, notification,
               JobService.JOB_END_NOTIFICATION_POLICY_DETACH
           )
           // Execute the work associated with this job asynchronously.
           scope.launch {
               doDownload(params)
           }
           return true
       }

       private suspend fun doDownload(params: JobParameters) {
           // Run the relevant async download task, then call
           // jobFinished once the task is completed.
           jobFinished(params, false)
       }

       // Called when the system stops the job.
       override fun onStopJob(params: JobParameters?): Boolean {
           // Asynchronously record job-related data, such as the
           // stop reason.
           return true // or return false if job should end entirely.
       }
   }
   ```

   <br />

5. Periodically update the notification to keep the user informed of the job's
   status and progress. If you cannot determine the transfer size ahead of
   scheduling the job, or need to update the estimated transfer size,
   use the new API, `updateEstimatedNetworkBytes()` to
   update the transfer size after it becomes known.

### Recommendations

To run UIDT jobs effectively, do the following:

1. Clearly define network constraints and job execution constraints to specify
   when the job should be executed.

2. Execute the task asynchronously in `onStartJob()`; for example, you can do
   this by using a [coroutine](https://developer.android.com/kotlin/coroutines.md.txt). If you don't run the task asynchronously, the
   work runs on the main thread and might block it, which can cause an ANR.

3. To avoid running the job longer than necessary, call
   [`jobFinished()`](https://developer.android.com/reference/android/app/job/JobService.md.txt#jobFinished(android.app.job.JobParameters,%20boolean)) when the transfer finishes, whether it
   succeeds or fails. That way, the job doesn't run longer than necessary. To
   discover why a job was stopped, implement the
   [`onStopJob()`](https://developer.android.com/reference/android/app/job/JobService.md.txt#onStopJob(android.app.job.JobParameters)) callback method and call
   [`JobParameters.getStopReason()`](https://developer.android.com/reference/android/app/job/JobParameters.md.txt#getStopReason()).

## Backward compatibility

There is currently no Jetpack library that supports UIDT jobs. For this reason,
we recommend that you gate your change with code that verifies that you're
running on Android 14 or higher. On lower Android versions, you
can use [WorkManager's foreground service implementation](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running.md.txt) as a
fallback approach.

Here's an example of code that checks for the appropriate system version:


```kotlin
fun beginTask() {
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
        scheduleDownloadFGSWorker(context)
    } else {
        scheduleDownloadUIDTJob(context)
    }
}

private fun scheduleDownloadUIDTJob(context: Context) {
    // build jobInfo.
    val jobScheduler: JobScheduler =
        context.getSystemService(Context.JOB_SCHEDULER_SERVICE) as JobScheduler
    jobScheduler.schedule(jobInfo)
}

private fun scheduleDownloadFGSWorker(context: Context) {
    val myWorkRequest = OneTimeWorkRequest.from(DownloadWorker::class.java)
    WorkManager.getInstance(context).enqueue(myWorkRequest)
}
```

<br />

## Stop UIDT jobs

Both the user and the system can stop user-initiated transfer jobs.

### By the user, from Task Manager

The user can stop a user-initiated data transfer job that appears in the [Task
Manager](https://developer.android.com/develop/background-work/services/fgs/handle-user-stopping).

At the moment that the user presses **Stop**, the system does the following:

- Terminates your app's process immediately, including all other jobs or foreground services running.
- Doesn't call `onStopJob()` for any running jobs.
- Prevents user-visible jobs from being rescheduled.

For these reasons, it's recommended to provide controls in the notification
posted for the job to allow gracefully stopping and rescheduling the job.

Note that, under special circumstances, the **Stop** button doesn't appear
next to the job in the Task Manager, or the job isn't shown in the Task Manager
at all.

### By the system

Unlike regular jobs, user-initiated data transfer jobs are unaffected by [App
Standby Buckets quotas](https://developer.android.com/topic/performance/power/power-details). However, the system still stops the job if any of
the following conditions occur:

- A developer-defined constraint is no longer met.
- The system determines that the job has run for longer than necessary to complete the data transfer task.
- The system needs to prioritize system health and stop jobs due to increased thermal state.
- The app process is killed due to low device memory.

When the job is stopped by the system for reasons *other than* low device
memory, the system calls `onStopJob()`, and the system retries the job at a time
that the system deems to be optimal. Make sure that your app can persist the
data transfer state even if `onStopJob()` isn't called, and that your app can
restore this state when `onStartJob()` is called again.

## Conditions allowed for scheduling user-initiated data transfer jobs

Apps can only start a user-initiated data transfer job if the app is in the
visible window, or if certain conditions are met:

- [If an app can launch activities from the background](https://developer.android.com/guide/components/activities/background-starts#exceptions), it can also launch user-initiated data transfer jobs from the background.
- If an app has an activity in the back stack of an existing task on the **Recents** screen, that alone doesn't allow a user-initiated data transfer job to run.

> [!NOTE]
> **Note:** The conditions for [launching a UIDT job from the background](https://developer.android.com/guide/components/activities/background-starts#exceptions) are **not** the same as the exemptions that allow an app to [start foreground
> services from the background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions).

If the job is scheduled to run at a time when the necessary conditions are not
met, the job fails and returns a `RESULT_FAILURE` error code.

## Constraints that are allowed for user-initiated data transfer jobs

To support jobs running at optimal points, Android offers the ability to assign
constraints to each job type. These constraints are available as of
Android 13.

**Note** : The following table only compares the constraints that vary between
each job type. See [JobScheduler developer page](https://developer.android.com/reference/android/app/job/JobInfo.Builder.md.txt) or [work constraints](https://developer.android.com/reference/androidx/work/Constraints.Builder.md.txt) for
all constraints.

The following table shows the different job types that support a given job
constraint, as well as the set of job constraints that WorkManager supports. Use
the search bar before the table to filter the table by the name of a job
constraint method.

These are the constraints allowed with user-initiated data transfer jobs:

- `setBackoffCriteria(JobInfo.BACKOFF_POLICY_EXPONENTIAL)`
- `setClipData()`
- `setEstimatedNetworkBytes()`
- `setMinimumNetworkChunkBytes()`
- `setPersisted()`
- `setNamespace()`
- `setRequiredNetwork()`
- `setRequiredNetworkType()`
- `setRequiresBatteryNotLow()`
- `setRequiresCharging()`
- `setRequiresStorageNotLow()`

## Testing

The following list shows some steps on how to test your app's jobs manually:

- To get the job ID, get the value that is defined upon the job being built.
- To run a job immediately, or to retry a stopped job, run the following
  command in a terminal window:

  ```bash
  adb shell cmd jobscheduler run -f APP_PACKAGE_NAME JOB_ID
  ```
- To simulate the system force-stopping a job (due to system health or
  out-of-quota conditions), run the following command in a terminal window:

  ```bash
  adb shell cmd jobscheduler timeout TEST_APP_PACKAGE TEST_JOB_ID
  ```

## See also

- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks.md.txt)
- [Data transfer background task options](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options.md.txt)

## Additional resources

For more information about user-initiated data transfers, see the following
additional resources:

- Case study on UIDT integration: [Google Maps improved download reliability by
  10% using user initiated data transfer API](https://android-developers.googleblog.com/2024/09/google-maps-improved-download-reliability-user-initiated-data-transfer-api.html)