---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker
url: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker
source: md.txt
---

Whether you capture an [app-driven profile](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture.md.txt) or a [trigger-based profile](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture.md.txt),
`ProfilingManager` saves the completed file on the device and delivers a
`ProfilingResult` to your registered callback. Call
[`ProfilingResult.getResultFilePath`](https://developer.android.com/reference/android/os/ProfilingResult.md.txt#getResultFilePath()) to get the path of the saved profile:

- **During local testing** : [Pull the file to your computer using `adb`](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode.md.txt#retrieve-traces-adb).
- **In production** : Pass the path to a [`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started.md.txt) job that compresses and uploads the profile to your server.

> [!IMPORTANT]
> **Key Point:** Always use `ProfilingResult.getResultFilePath` to locate the file in code and other `ProfilingResult` APIs such as [`ProfilingResult.getTriggerType`](https://developer.android.com/reference/android/os/ProfilingResult.md.txt#getTriggerType()) or [`ProfilingResult.getTag`](https://developer.android.com/reference/android/os/ProfilingResult.md.txt#getTag()) to inspect profile metadata, rather than parsing filenames, because the underlying directory structure and filename format can change.

## Retrieve profiles from a device

This section describes where `ProfilingManager` stores profiles on the device,
how automatic file cleanup works, and how to pull files locally using `adb`.

### File locations and naming formats

`ProfilingManager` saves redacted profiles in your [app-specific storage
directory](https://developer.android.com/training/data-storage/app-specific) at `/data/user/0/<app>/files/profiling/`. The filename format
depends on how the profile was captured:

- **App-driven profiles**:

      profile_<tag>_<datetime>_uid-<uid>.<profile-type-ext>

  If no tag was provided when requesting the profile, `<tag>_` is omitted:
  `profile_<datetime>_uid-<uid>.<profile-type-ext>`.
- **Trigger-based profiles**:

      profile_trigger-type-<trigger_type>_<datetime>_uid-<uid>.<profile-type-ext>

Where:

- `<app>` is your app's package name.
- `<tag>` is up to the first 20 alphanumeric characters (and hyphens) of the caller-supplied tag configured with [`setTag`](https://developer.android.com/reference/kotlin/androidx/core/os/ProfilingRequestBuilder.md.txt#setTag(kotlin.String)) or passed to `requestProfiling`, converted to lowercase with any characters outside `a-z`, `0-9`, and `-` removed.
- `<trigger_type>` is the integer constant code for the trigger from [`ProfilingTrigger`](https://developer.android.com/reference/android/os/ProfilingTrigger.md.txt). Always call [`ProfilingResult.getTriggerType`](https://developer.android.com/reference/android/os/ProfilingResult.md.txt#getTriggerType()) in code instead of parsing the filename.
- `<datetime>` is the date and time the profile was recorded (`yyyy-MM-dd-HH-mm-ss-SSS`).
- `<uid>` is your app's Linux user ID (included on recent `Profiling` module versions).
- `<profile-type-ext>` is the file extension for the captured profile type:
  - `.perfetto-trace` for system traces
  - `.perfetto-java-heap-dump` for Java heap dumps
  - `.perfetto-heap-profile` for heap profiles
  - `.perfetto-stack-sample` for stack sampling profiles

### On-device storage and cleanup

To free up device storage promptly, **delete each profile file in your upload
worker immediately after a successful upload** (because automatic cleanup only
runs when `ProfilingManager` delivers results to your app, unuploaded files can
otherwise remain on disk if your app stops registering callbacks after ending a
campaign). As a fallback on recent `Profiling` module versions,
`ProfilingManager` also automatically deletes delivered files in your
app-specific storage directory that are older than 5 days when new results are
delivered.

> [!NOTE]
> **Note:** To pull profiles from a test device using `adb` during local testing, see [Pull profiles using ADB](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode.md.txt#retrieve-traces-adb) in [Debug commands for local profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode.md.txt).

## Upload profiles in production with WorkManager

Because profile files can be several megabytes in size, schedule production
uploads in the background when the device is on an unmetered network (Wi-Fi),
charging, and idle.

Before uploading, **compress the profile file** (for example, using
`GZIPOutputStream` or `ZipOutputStream`). Perfetto protobuf profiles and Java
heap dumps compress significantly, reducing network bandwidth and backend
storage costs.

### Add WorkManager dependencies

`ProfilingManager` is cloud-agnostic, so you can schedule the upload of profiles
to any backend using [`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started.md.txt). Add the `WorkManager` library to your
`build.gradle.kts` file:

### Kotlin

```kotlin
   dependencies {
       implementation("androidx.work:work-runtime:2.12.0")
   }
   
```

### Groovy

```groovy
   dependencies {
       implementation 'androidx.work:work-runtime:2.12.0'
   }
   
```

### Schedule an upload job

When your app receives a `ProfilingResult`, schedule the upload job. The
following example omits the initial profiling request; for a complete request
example, see [Record a system trace](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture.md.txt#record-system-trace).

> [!NOTE]
> **Note:** The actual network upload call is omitted because `ProfilingManager` works with any cloud platform. Use this setup as a starting point, then add compression and the upload logic for your backend service.


### Kotlin

```kotlin
class TraceUploadWorker(context: Context, workerParams: WorkerParameters) : Worker(context, workerParams) {
    override fun doWork(): Result {
        // Perform your uploading work here
        Log.d("ProfileTest", "Uploading trace: " + inputData.getString("PROFILE_PATH"))

        return Result.success()
    }
}

fun setupProfileUploadWorker(profileFilepath: String?) {
    val workMgr = WorkManager.getInstance(applicationContext)
    val workRequestBuilder = OneTimeWorkRequest.Builder(TraceUploadWorker::class)

    val constraints = Constraints.Builder()
        .setRequiredNetworkType(NetworkType.UNMETERED)
        .setRequiresDeviceIdle(true)
        .setRequiresCharging(true)
        .build()
    workRequestBuilder.setConstraints(constraints)

    val inputDataBuilder = Data.Builder()
    inputDataBuilder.putString("PROFILE_PATH", profileFilepath)
    workRequestBuilder.setInputData(inputDataBuilder.build())

    workMgr.enqueue(workRequestBuilder.build())
}
```

### Java

```java
public static class TraceUploadWorker extends Worker {

  public TraceUploadWorker(
      @androidx.annotation.NonNull Context context,
      @androidx.annotation.NonNull WorkerParameters workerParams) {
    super(context, workerParams);
  }

  @androidx.annotation.NonNull
  @Override
  public Result doWork() {
    // Perform your uploading work here
    Log.d("ProfileTest", "Uploading trace: " + getInputData().getString("PROFILE_PATH"));

    return Result.success();
  }
}

public void setupProfileUploadWorker(String profileFilepath) {
  WorkManager workMgr = WorkManager.getInstance(getApplicationContext());
  OneTimeWorkRequest.Builder workRequestBuilder = new OneTimeWorkRequest.Builder(
      TraceUploadWorker.class);

  Constraints constraints = new Constraints.Builder()
      .setRequiredNetworkType(NetworkType.UNMETERED)
      .setRequiresDeviceIdle(true)
      .setRequiresCharging(true)
      .build();
  workRequestBuilder.setConstraints(constraints);

  Data.Builder inputDataBuilder = new Data.Builder();
  inputDataBuilder.putString("PROFILE_PATH", profileFilepath);
  workRequestBuilder.setInputData(inputDataBuilder.build());

  workMgr.enqueue(workRequestBuilder.build());
}
```

<br />

### Code walkthrough

The preceding example performs the following steps:

- **Define the worker** : Create a `TraceUploadWorker` class extending `Worker`. Implement `doWork` to verify that the profile file still exists, compress and upload it using your backend SDK or HTTP client, and delete the local file once the upload succeeds.
- **Schedule the work** :
  - Create a `OneTimeWorkRequest` for your worker.
  - **Set constraints** : Use `setRequiredNetworkType(NetworkType.UNMETERED)`, `setRequiresDeviceIdle(true)`, and `setRequiresCharging(true)` so the upload only runs when the device is on Wi-Fi, charging, and idle.
  - **Pass data** : Use `setInputData` to pass the profile path from `getResultFilePath` to the worker.
  - **Enqueue** : Submit the request to `WorkManager` by calling `WorkManager.enqueue`.

## Next steps

After retrieving or uploading profiles, [visualize them in the Perfetto UI](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze.md.txt),
[query individual profiles with PerfettoSQL](https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles.md.txt), [analyze traces in bulk](https://developer.android.com/topic/performance/tracing/profiling-manager/bulk-trace-analysis.md.txt),
or [analyze profiles with AI](https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai.md.txt). For guidance on setting up a scalable
server-side analysis pipeline, see [Deploying Bigtrace on Kubernetes](https://perfetto.dev/docs/deployment/deploying-bigtrace-on-kubernetes).