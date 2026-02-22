---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker
url: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker
source: md.txt
---

ProfilingManager saves traces locally on the device. While you can retrieve
these files using ADB for local debugging, collecting field data requires
uploading them to a server.

Trace files can be large (often several MBs). To avoid negatively affecting the
user experience or consuming mobile data, you should schedule uploads to occur
in the background, preferably when the device is on an unmetered network
(Wi-Fi), charging and idle.

## Set up a WorkManager upload job

`ProfilingManager` is cloud-agnostic; you can upload traces to any
infrastructure you choose. The following example demonstrates how to use
[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started) to schedule an upload job that avoids user disruption.

## Code example to setup an upload job

Here's an example on how you can set up a job that is not disruptive to the user
to upload traces to your server.

### Add WorkManager dependencies

Besides your existing `ProfilingManager` dependencies, add these Jetpack
libraries to your `build.gradle.kts` file. `WorkManager` needs them.

### Kotlin

```kotlin
   dependencies {
       implementation("androidx.work:work-runtime:2.11.1")
   }
   
```

### Groovy

```groovy
   dependencies {
       implementation 'androidx.work:work-runtime:2.11.1'
   }
   
```

### Code snippet

This code shows how to set up a job for uploading traces. The job should be
setup when the `ProfilingResult` is received by your app. The profiling section
is omitted in this section but an example can be found in [Record a system
trace](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture#record-system-trace).

> [!NOTE]
> **Note:** The actual upload logic is not included. `ProfilingManager` works with any cloud platform. Use this setup as a starting point, then add the specific upload details for your app's cloud service.


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

The code does the following:

- **Define the worker** : Create a `TraceUploadWorker` class extending
  `Worker`. Implement the `doWork()` method to handle the actual file upload
  logic using your preferred backend SDK or HTTP client.

- **Request profiling** : Use `SystemTraceRequestBuilder` to configure the
  trace (duration, buffer policy) and `Profiling.requestProfiling` to start
  it.

- **Schedule the work**:

  - Create a `OneTimeWorkRequest` for your worker.

  - Set constraints: Use `setRequiredNetworkType(NetworkType.UNMETERED)`,
    `setRequiresDeviceIdle(true)` and `setRequiresCharging(true)` to ensure
    the upload only happens when the user is on Wi-Fi, charging and not actively
    using the device. This is important to avoid disruption to the user with the
    upload job.

  - Pass data: Use `setInputData` to pass the trace path to the worker.

  - Enqueue: Submit the request to WorkManager by calling
    `WorkManager#enqueue`.

## Next Steps

After uploading traces, you can analyze them individually or perform [bulk trace
analysis](https://developer.android.com/topic/performance/tracing/profiling-manager/bulk-trace-analysis). For guidance on setting up a scalable analysis pipeline, refer to
[Deploying Bigtrace on Kubernetes](https://perfetto.dev/docs/deployment/deploying-bigtrace-on-kubernetes).

> [!NOTE]
> **Note:** You can delete profile files from the device after uploading them if they are no longer needed, as `ProfilingManager` no longer manages these files.