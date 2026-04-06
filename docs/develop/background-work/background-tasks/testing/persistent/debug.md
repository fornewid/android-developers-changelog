---
title: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/debug
url: https://developer.android.com/develop/background-work/background-tasks/testing/persistent/debug
source: md.txt
---

If you notice that your workers run too often or not at all, here are some
debugging steps that can help you discover what is happening.

## Enable logging

To determine why your workers aren't running properly, it can be very useful to
look at *verbose* WorkManager logs. To enable logging, use [custom
initialization](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration).

First, disable the default `WorkManagerInitializer` in your
`AndroidManifest.xml` file by creating a new WorkManager provider with the
manifest-merge rule **`remove`** applied:

    <provider
        android:name="androidx.work.impl.WorkManagerInitializer"
        android:authorities="${applicationId}.workmanager-init"
        tools:node="remove"/\>

Now that the default WorkManager initializer is disabled, you can use [on-demand
initialization](https://developer.android.com/guide/background/persistent/configuration/custom-configuration#on-demand).
To do so, the `android.app.Application` class needs to provide an implementation
for `androidx.work.Configuration.Provider`:

### Kotlin

```kotlin
class MyApplication() : Application(), Configuration.Provider {
    override fun getWorkManagerConfiguration() =
        Configuration.Builder()
            .setMinimumLoggingLevel(android.util.Log.DEBUG)
            .build()
}
```

### Java

```java
public class MyApplication extends Application implements Configuration.Provider {
    @NonNull
    @Override
    public Configuration getWorkManagerConfiguration() {
        return new Configuration.Builder()
                .setMinimumLoggingLevel(android.util.Log.DEBUG)
                .build();
    }
}
```

When you define a custom WorkManager configuration, your WorkManager is
initialized when you call
[`WorkManager.getInstance(Context)`](https://developer.android.com/reference/androidx/work/WorkManager#getInstance(android.content.Context))
rather than automatically at application startup. See [Custom WorkManager
Configuration and
Initialization](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration)
for more information, including support for versions of WorkManager before
2.1.0.

With [`DEBUG`](https://developer.android.com/reference/android/util/Log#DEBUG) logging enabled, you
see a lot more logs with the log-tag prefix `WM-`.

## Use adb shell dumpsys jobscheduler

You can use `adb` to get more information about job scheduling on Android 6.0
(API level 23) or higher. If you are new to `adb`, see [Command-line
tools](https://developer.android.com/studio/command-line) for more details.

Once you have `adb` installed, run the following command to look at the list of
jobs that are attributed to your package:

    adb shell dumpsys jobscheduler

The output looks something like this:

    JOB #u0a172/4: 6412553 com.google.android.youtube/androidx.work.impl.background.systemjob.SystemJobService
      u0a172 tag=*job*/com.google.android.youtube/androidx.work.impl.background.systemjob.SystemJobService
      Source: uid=u0a172 user=0 pkg=com.google.android.youtube
      JobInfo:
        Service: com.google.android.youtube/androidx.work.impl.background.systemjob.SystemJobService
        Requires: charging=false batteryNotLow=false deviceIdle=false
        Extras: mParcelledData.dataSize=180
        Network type: NetworkRequest [ NONE id=0, [ Capabilities: NOT_METERED&INTERNET&NOT_RESTRICTED&TRUSTED&VALIDATED Uid: 10172] ]
        Minimum latency: +1h29m59s687ms
        Backoff: policy=1 initial=+30s0ms
        Has early constraint
      Required constraints: TIMING_DELAY CONNECTIVITY [0x90000000]
      Satisfied constraints: DEVICE_NOT_DOZING BACKGROUND_NOT_RESTRICTED WITHIN_QUOTA [0x3400000]
      Unsatisfied constraints: TIMING_DELAY CONNECTIVITY \[0x90000000\]
      Tracking: CONNECTIVITY TIME QUOTA
      Implicit constraints:
        readyNotDozing: true
        readyNotRestrictedInBg: true
      Standby bucket: RARE
      Base heartbeat: 0
      Enqueue time: -51m29s853ms
      Run time: earliest=+38m29s834ms, latest=none, original latest=none
      Last run heartbeat: 0
      Ready: false (job=false user=true !pending=true !active=true !backingup=true comp=true)

When using WorkManager, the component responsible for managing worker execution
is `SystemJobService` on API level 23 or higher. Look for instances of jobs
that are attributed to your package name and
`androidx.work.impl.background.systemjob.SystemJobService`.

For every job, the output from the command lists **required** , **satisfied** ,
and **unsatisfied** constraints. Check whether your worker's constraints are
fully satisfied.

The output also includes job history for recently executed jobs, so you can use
it to check whether `SystemJobService` was invoked recently.

    Job history:
         -1h35m26s440ms   START: #u0a107/9008 com.google.android.youtube/androidx.work.impl.background.systemjob.SystemJobService
         -1h35m26s362ms  STOP-P: #u0a107/9008 com.google.android.youtube/androidx.work.impl.background.systemjob.SystemJobService app called jobFinished

## Request diagnostic information from WorkManager 2.4.0+

On debug builds of your app, you can request diagnostic information from
WorkManager 2.4.0 and higher using the following command:

    adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p "<your_app_package_name>"

This provides information on:

- Work requests that completed in the last 24 hours.
- Work requests that are currently running.
- Work requests that are scheduled.

Here is what it could look like (the output is visible through `logcat`):

    adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p "androidx.work.integration.testapp"

    adb logcat
    ...
    2020-02-13 14:21:37.990 29528-29660/androidx.work.integration.testapp I/WM-DiagnosticsWrkr: Recently completed work:
    2020-02-13 14:21:38.083 29528-29660/androidx.work.integration.testapp I/WM-DiagnosticsWrkr: Id  Class Name   State  Unique Name Tags
        08be261c-2def-4bd6-a716-1e4410968dc4     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        48ce04f1-8df9-450b-96ec-6eceabb9c690     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        c46f4699-c384-440c-a10e-26d56ce02963     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        ce125372-046e-484e-949f-9abb35ce62c3     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        72887ddd-8ed1-4018-b798-fac218e95e16     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        dcff3d61-320d-4996-8644-5d97944bd09c     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        acab0bf7-6087-43ad-bdb5-be0df9195acb     androidx.work.impl.workers.DiagnosticsWorker    SUCCEEDED  null    androidx.work.impl.workers.DiagnosticsWorker
        23136bcd-01dd-46eb-b910-0fe8a140c2a4     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        245f4879-c6d2-4997-8130-e4e90e1cab4c     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        17d05835-bb61-429a-ad11-fe43fc320a54     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        e95f12be-4b0c-4e64-88da-8ee07a31e42f     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        431c3ec2-4a55-469b-b50b-4072d35f1232     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        883a388f-f911-4098-9143-37bd8fbc098a     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        b904163c-6822-4299-8d5a-78df49b7e53d     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
        453fd7b9-2b16-45b9-abc5-3d2ce7b6a4ba     androidx.work.integration.testapp.ToastWorker   SUCCEEDED  null    androidx.work.integration.testapp.ToastWorker
    2020-02-13 14:21:38.083 29528-29660/androidx.work.integration.testapp I/WM-DiagnosticsWrkr: Running work:
    2020-02-13 14:21:38.089 29528-29660/androidx.work.integration.testapp I/WM-DiagnosticsWrkr: Id  Class Name   State  Unique Name Tags
        b87c8a4f-4ac6-4e25-ba3e-4cea53ce468a     androidx.work.impl.workers.DiagnosticsWorker    RUNNING    null    androidx.work.impl.workers.DiagnosticsWorker
    ...