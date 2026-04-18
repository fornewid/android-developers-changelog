---
title: https://developer.android.com/blog/posts/optimize-your-app-battery-using-android-vitals-wake-lock-metric
url: https://developer.android.com/blog/posts/optimize-your-app-battery-using-android-vitals-wake-lock-metric
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Optimize your app battery using Android vitals wake lock metric

###### 7-min read

![](https://developer.android.com/static/blog/assets/6m_Evk_L_Olno_HD_56e1732bf5_2enBUx.webp) 02 Oct 2025 [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) [##### Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

###### Developer Relations Engineer

Battery life is a crucial aspect of user experience and wake locks play a major role. Are you using them excessively? In this blog post we'll explore what wake locks are, what are some best practices for using them and how you can better understand your own app's behavior with the Play Console metric.

## Excessive partial wake lock usage in Android Vitals

The Play Console now monitors battery drain, with a focus on [**excessive partial wake lock usage**](https://play.google.com/console/developers/app/vitals/metrics/details?metric=EXCESSIVE_BACKGROUND_WAKELOCKS&days=28), as a key performance indicator.

This feature elevates the importance of battery efficiency alongside existing core metric stability indicators: excessive user-perceived crashes and ANRs. **We have** [**defined a bad behavior threshold for excessive wake locks**](https://android-developers.googleblog.com/2025/11/raising-bar-on-battery-performance.html)**. Starting March 1, 2026, if your title does not meet this quality threshold, we may exclude the title from prominent discovery surfaces such as recommendations. In some cases, we may display a warning on your store listing to indicate to users that your app may cause excessive battery drain.**
![warning.png](https://developer.android.com/static/blog/assets/warning_acc52c9e53_29d4gO.webp)

*The excessive wake lock warning in the *[*Android vitals overview*](https://play.google.com/console/developers/app/vitals/metrics/overview)*.*

For mobile devices, the Android vitals metric applies to non-exempted wake locks acquired while the screen is off and the app is in the background or running a foreground service. Android vitals considers partial wake lock usage excessive if:

- Wake locks are held for at least two hours within a 24-hour period.
- It affects more than 5% of your app's sessions, averaged over 28 days.

Wake locks created by [audio](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#media), [location](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#location), and [JobScheduler](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#jobs) user initiated APIs are exempted from the wake lock calculation.

## Understanding wake locks

A wake lock is a mechanism that allows an app to keep a device's CPU running even when the user isn't actively interacting with it.

A partial wake lock keeps the CPU running even if the screen is off, preventing the CPU from entering a low-power "suspend" state. A full wake lock keeps both the screen and the CPU running.

There are 2 methods partial wake locks are acquired:

- The app manually acquires and releases the wake lock using [PowerManager](https://developer.android.com/reference/android/os/PowerManager) APIs for a specific use case, often this is acquired in conjunction with a [Foreground Service](https://developer.android.com/develop/background-work/services/fgs) - a platform lifecycle API intended for user-perceptible operation.
- Alternatively, the wake lock is acquired by another API, and attributed to the app due to usage of the API, more on this in the best practices section.

While wake locks are necessary for tasks like completing a user-initiated download of a large file, their **excessive or improper use can lead to significant battery drain**. We've seen cases where apps hold wake locks for hours or fail to release them properly, leading to user complaints about significant battery drain even when they're not interacting with the app.

## Best Practices for Wake Lock Usage

Before we go over how to debug excessive wake lock usage, ensure you're following wake lock best practices.

Consider these four critical questions.

<br />

**1. Have you considered alternative wake lock options?**

Before considering acquiring a manual partial wake lock, follow this decision-making flowchart:
![wakelock.png](https://developer.android.com/static/blog/assets/wakelock_503e30ff8a_Zt4oMN.webp)

*Flowchart to decide when to manually acquire a wake lock*

1. Does the screen need to stay on?
   - Yes: Reference the [Keep Screen On](https://developer.android.com/develop/background-work/background-tasks/awake/screen-on) documentation instead
2. Is the application running a foreground service?
   - No: You don't need to manually acquire a wake lock.
3. Is it detrimental to the user experience if the device suspends?
   - No: For instance, updating a notification after the device wakes up doesn't require a wake lock.
   - Yes: If it's critical to prevent the device from suspending, like ongoing communication with an external device, proceed.
4. Is there already an API keeping the device awake on your behalf?
   - You can leverage the documentation [Identify wake locks created by other APIs](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls) to identify scenarios where wake locks created by other APIs to identify scenarios where wake locks are created by other APIs such as LocationManager.
   - If no APIs exist, proceed to the final question.
5. If you've answered all these questions and determined no alternative exists, you should proceed with manually acquiring a wake lock.

**2. Are you naming the wake lock correctly?**

When manually acquiring wake locks, proper naming is important for debugging:

- Leave out any Personally Identifiable Information (PII) in the name like email addresses. If PII is detected, the wake lock is logged as `_UNKNOWN`, hindering debugging.
- Don't name your wake lock programmatically using class or method names, as these can be obfuscated by tools like Proguard. Instead, use a hard-coded string.
- Do not add counters or unique identifiers to wake lock tags. The same tag should be used every time the wake lock runs to allow the system to aggregate usage by name, making abnormal behavior easier to detect.

**3. Is the acquired wake lock always released?**

If you're acquiring a wake lock manually, ensure the wake lock release always executes. Failing to release a wake lock can cause significant battery drain.

For example, if an uncaught exception is thrown during processingWork(), the release() call might never happen. Instead, you can use a try-finally block to guarantee the wake lock is released, even if an exception occurs.

Additionally, you can add a timeout to the wake lock to ensure it releases after a specific period, preventing it from being held indefinitely.

```
fun processingWork() {
    wakeLock.apply {
        try {
            acquire(60 * 10 * 1000) // timeout after 10 minutes
            doTheWork()
        } finally {
            release()
        }
    }
}
```

**4. Can you reduce the wake-up frequency?**

For periodic data requests, reducing how often your app wakes up the device is key to battery optimization. Some examples of reducing wake-up frequency include:

- **WorkManager:** Increase the periodic interval in [PeriodicWorkRequest](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest)s.
- **SensorManager:** Leverage batching by specifying [maxReportLatencyMs](https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int,%20int)) when registering the listener.
- **Fused Location Provider:**
  - Reduce location retrieval frequency by using [getLastLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#public-abstract-tasklocation-getlastlocation) for the most recent cached location.
  - Use [setPriority(PRIORITY_PASSIVE](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setpriority-int-priority)) for a less battery-intensive update method.
  - Also, you can leverage the location batching mechanism by setting a minimum update interval with [setMinUpdateIntervalMillis](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest.Builder#public-locationrequest.builder-setminupdateintervalmillis-long-minupdateintervalmillis).

You can view more details in the [wake lock best practices documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices).

## Debugging excessive wake lock usage

Even with the best intentions, excessive wake lock usage can occur. If your app is flagged in the Play Console, here's how to debug it:

**Initial identification with Play Console**

The Android vitals excessive partial wake lock dashboard provides breakdowns of non-exempted wake lock names associated with your app, showing affected sessions and durations. Reminder to use the [documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls) to help you identify if the wake lock name is app-held or held by another API.
![breakdowns2.png](https://developer.android.com/static/blog/assets/breakdowns2_987ee7d6f2_1HmfEt.webp)

*The Android vitals excessive partial wake lock dashboard scrolled down to the breakdowns section to view excessive wake lock tags.*

**Debugging excessive wake locks held by workers/jobs**

You can identify worker-held wake locks with this wake lock name:

`*job*/<package_name>/androidx.work.impl.background.systemjob.SystemJobService`

The full list of variations of worker-held wake lock names is available in [documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#wake_lock_names_6). To debug these wake locks, you can use Background Task Inspector to debug locally, or leverage getStopReason to debug issues in the field.

**Android Studio Background Task Inspector**
![taskinspector.png](https://developer.android.com/static/blog/assets/taskinspector_60a38ee510_Z1iDBkV.webp)

<br />

*Screen capture of the Background Task Inspector, where it has been able to identify a worker "WeatherSyncWorker" that has frequently retried and failed.*

For local debugging of `WorkManager` issues, use this tool on an emulator or connected device (API level 26+). It shows a list of workers and their statuses (finished, executing, enqueued), allowing you to inspect details and understand worker chains.

For instance, it can reveal if a worker is frequently failing or retrying due to hitting system limitations.

See [Background Task Inspector documentation](https://developer.android.com/studio/inspect/task) for more details.

**WorkManager getStopReason**

For in-field debugging of workers with excessive wake locks, use [`WorkInfo.getStopReason()`](https://developer.android.com/reference/androidx/work/WorkInfo#getStopReason()) on WorkManager 2.9.0+ or for JobScheduler, [`JobParameters.getStopReason()`](https://developer.android.com/reference/android/app/job/JobParameters#getStopReason()) available on SDK 31+.

This API helps log the reason why a worker stopped (e.g., `STOP_REASON_TIMEOUT`, `STOP_REASON_QUOTA`), pinpointing issues like frequent timeouts due to exhausting runtime duration.

```
backgroundScope.launch {
    WorkManager.getInstance(context)
        .getWorkInfoByIdFlow(workRequest.id)
        .collect { workInfo ->
            logStopReason(workRequest.id, workInfo?.stopReason)
        }
}
```

See [Optimize battery use for task scheduling APIs for more details](https://developer.android.com/develop/background-work/background-tasks/optimize-battery#why-stopped).

## Debugging other types of excessive wake locks

For more complex scenarios involving manually held wake locks or APIs holding the wake lock, we recommend you use system trace collection to debug.

**System trace collection**

**A system trace**is a powerful debugging tool that captures a detailed record of system activity over a period, providing insights into CPU state, thread activity, network activity, and battery-related metrics like job duration and wake lock usage.

You can capture a system trace using several methods:

- Utilizing the [system trace command line tool](https://developer.android.com/topic/performance/tracing/command-line)
- Using the [Android Studio CPU Profiler](https://developer.android.com/studio/profile)
- Using the [Perfetto UI](https://perfetto.dev/docs/getting-started/system-tracing)
- Recording a trace manually on the device [directly from the developer options](https://developer.android.com/topic/performance/tracing/on-device).

![powermgmt.png](https://developer.android.com/static/blog/assets/powermgmt_72d69d505f_1A6Uxu.webp)

*Enable "power:PowerManagement" Atrace category in the Perfetto UI under the Android apps \& svcs tab. *

Regardless of the chosen method, it's crucial to ensure that you are collecting the **"power:PowerManagement" Atrace category** to enable viewing of device state tracks.

**Perfetto UI inspection and SQL analysis**

System traces can be opened and inspected in the **Perfetto UI**. When you open the trace, you will see a visualization of various processes on a timeline. The tracks we will be focused on in this guide are the ones under "Device State".
![perfetto.png](https://developer.android.com/static/blog/assets/perfetto_d7ad363bc9_2vnHBF.webp)

<br />

*Pin the tracks under "Device State" such as "Top app", "Screen state", "Long Wake locks", and "Jobs" tracks to visually identify long-running wake lock slices.*

Each block lists the name of the event, when the event started, and when it ended. In Perfetto, this is called a slice.

For scalable analysis of multiple traces, you can use [**Perfetto's SQL analysis**](https://perfetto.dev/docs/analysis/perfetto-sql-getting-started). A SQL query can find all wake locks sorted by duration, helping identify the top contributors to excessive usage.

Here's an example query summing all the wake lock tags that occurred in the system trace, ordered by total duration:

```
SELECT slice.name as name, track.name as track_name,SUM(dur / 100000) as total_dur_ms
FROM slice
JOIN track ON slice.track_id = track.id
WHERE track.name = 'WakeLocks'GROUP BY slice.name, track.name
ORDER BY total_dur_ms DESC
```

**Use ProfilingManager for in-field trace collection**

For hard-to-reproduce issues, `ProfilingManager` (added in SDK 35) is a programmatic API that allows developers to collect system traces in the field with start and end triggers. It offers more control over the start and end trigger points for profile collection and enforces system-level rate limiting to prevent device performance impact.

Check out the [ProfilingManager documentation](https://developer.android.com/topic/performance/tracing/profiling-manager/overview) for further steps on how to implement in field system trace collection which include how to programmatically [capture a trace](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture), [analyze profiling data](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze), and use [local debug commands](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode).

The system traces collected using ProfilingManager will look similar to the ones collected manually, but system processes and other app processes are redacted from the trace.

## Conclusion

The excessive partial wake lock metric in Android vitals is only a small part of our ongoing commitment to supporting developers in reducing battery drain and improving app quality.

By understanding and properly implementing wake locks, you can significantly optimize your app's battery performance. Leveraging alternative APIs, adhering to wake lock best practices, and using powerful debugging tools such as Background Task Inspector, system traces and ProfilingManager are key to ensuring your app's success on Google Play.

###### Written by:

-

  ## [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alice-yuan) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) 15 Apr 2026 15 Apr 2026 ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boosting user privacy and business protection with updated Play policies](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)

  [arrow_forward](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies) Making Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)