---
title: https://developer.android.com/blog/posts/how-whoop-decreased-excessive-partial-wake-lock-sessions
url: https://developer.android.com/blog/posts/how-whoop-decreased-excessive-partial-wake-lock-sessions
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# How WHOOP decreased excessive partial wake lock sessions by over 90%

###### 4-min read

![](https://developer.android.com/static/blog/assets/whoop2_fcb73fdc54_bqwCk.webp) 04 Mar 2026 [![](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp)](https://developer.android.com/blog/authors/breana-tate) [##### Breana Tate](https://developer.android.com/blog/authors/breana-tate)

###### Developer Relations Engineer

Building an Android app for a wearable means the real work starts when the screen turns off. [WHOOP](https://www.whoop.com/us/en/) helps members understand how their body responds to training, recovery, sleep, and stress, and for the many WHOOP members on [Android](https://play.google.com/store/apps/details?id=com.whoop.android&pli=1), reliable background syncing and connectivity are what make those insights possible.

Earlier this year, Google Play [released a new metric in Android vitals](https://android-developers.googleblog.com/2025/11/raising-bar-on-battery-performance.html): Excessive partial wake locks. This metric measures the percentage of user sessions where cumulative, non-exempt wake lock usage exceeds 2 hours in a 24-hour period. The aim of this metric is to help you identify and address possible sources of battery drain, which is crucial for delivering a great user experience.

Beginning March 1, 2026, apps that continue to not meet the quality threshold may be excluded from Google Play discovery surfaces. A warning may also be placed on the Google Play Store listing, indicating the app might use more battery than expected.

According to Mayank Saini, Senior Android Engineer at WHOOP, this "presented the team with an opportunity to raise the bar on Android efficiency," after Android vitals flagged the app's excessive partial wake lock % as 15%---which exceeded the recommended 5% threshold.
![mayank.png](https://developer.android.com/static/blog/assets/mayank_0e8fbd512b_2vIyUQ.webp)

The team viewed the Android vitals metric as a clear signal that their background work was holding the CPU awake longer than necessary. Resolving this would allow them to continue to deliver a great user experience while simultaneously decreasing wasted background time and maintaining reliable and timely Bluetooth connectivity and syncing.

### **Identifying the issue**

To figure out where to get started, the team first turned to Android vitals for more insight into which wake locks were affecting the metric. By consulting the **Android vitals excessive partial wake locks dashboard** , they were able to identify the biggest contributor to excessive partial wake locks as one of their WorkManager workers (identified in the dashboard as `androidx.work.impl.background.systemjob.SystemJobService`). To support the WHOOP "always-on experience", the app uses WorkManager for background tasks like periodic syncing and delivering recurring updates to the wearable.

While the team *was* aware that WorkManager [acquires a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#workmanager) while executing tasks in the background, they previously did not have visibility into how all of their background work (beyond just WorkManager) was distributed until the introduction of the excessive partial wake locks metric in Android vitals.

With the dashboard identifying WorkManager as the main contributor, the team was then able to focus their efforts on identifying *which* of their workers was contributing the most and work towards resolving the issue.

### **Making use of internal metrics and data to better narrow down the cause**

WHOOP already had internal infrastructure set up to monitor WorkManager metrics. They periodically monitor:

1. Average Runtime: For how long does the worker run?
2. Timeouts: How often is the worker timing out instead of completing?
3. Retries: How often does the worker retry if the work timed out or failed?
4. Cancellations: How often was the work cancelled?

Tracking more than just worker successes and failures gives the team visibility into their work's efficiency.

The internal metrics flagged **high average runtime** for a select few workers, enabling them to narrow the investigation down even further.

In addition to their internal metrics, the team also used **Android Studio's** [**Background Task Inspector**](https://developer.android.com/studio/inspect/task) to inspect and debug the workers of interest, with a specific focus on associated wake locks, to align with the metric flagged in Android vitals.

### **Investigation: Distinguishing between worker variants**

WHOOP uses both [one-time](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#schedule_one-time_work) and [periodic](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#schedule_periodic_work) scheduling for some workers. This allows the app to reuse the same Worker logic for identical tasks with the same success criteria, differing only in timing.

Using their internal metrics made it possible to narrow their search to a specific worker, but they couldn't tell if the bug occurred when the worker was one-time, periodic, or both. So, they rolled out an update to use WorkManager's [setTraceTag method](https://developer.android.com/reference/androidx/work/WorkRequest.Builder#setTraceTag(kotlin.String)) to distinguish between the one-time and periodic variants of the same Worker.

This extra detail would allow them to definitively identify which Worker variant (periodic or one-time) was contributing the most to sessions with excessive partial wake locks. However, the team was surprised when the data revealed that neither variant appeared to be contributing more than the other.

Manmeet Tuteja, Android Engineer II at WHOOP said "that split also helped us confirm the issue was happening in *both* variants, which pointed away from scheduling configuration and toward a shared business logic problem inside the worker implementation."
![manmeet.png](https://developer.android.com/static/blog/assets/manmeet_c1cb74a185_iTAdN.webp)

### **Diving deeper on worker behavior and fixing the root cause**

With the knowledge that they needed to take a look at logic *within* the worker, the team re-examined worker behavior for the workers that had been flagged during their investigation. Specifically, they were looking for instances in which work may have been getting stuck and not completing.

All of this culminated in finding the root cause of the excessive wake locks:

### **A CoroutineWorker that was designed to wait for a connection to the WHOOP sensor before proceeding.**

If the work started with no sensor connected, `whoopSensorFlow`--which indicates if the sensor is connected-- was `null`. The `SensorWorker` didn't treat this as an early-exit condition and kept running, effectively waiting indefinitely for a connection. As a result, WorkManager held a partial wake lock until the work timed out, leading to high background wake lock usage and frequent, unwanted rescheduling of the `SensorWorker`.

To address this, the WHOOP team updated the worker logic to check the connection status before attempting to execute the core business logic.

If the sensor isn't available, the worker exits, avoiding a timeout scenario and releasing the wake lock. The following code snippet shows the solution:

```
class SensorWorker(appContext: Context, params: WorkerParameters): CoroutineWorker(appContext, params) {
   override suspend fun doWork(): Result {
      ...
      // Check the sensor state and perform work or return failure
       return whoopSensorFlow.replayCache
            .firstOrNull()
            ?.let { cachedData ->
                processSensorData(cachedData)
                Result.success()
            } ?: run {
                Result.failure()
            }
}
```

### **Achieving a 90% decrease in sessions with excessive partial wake locks**

After rolling out the fix, the team continued to monitor the Android vitals dashboard to confirm the impact of the changes.

Ultimately, WHOOP saw their **excessive partial wake lock percentage drop from 15% to less than 1%** just 30 daysafter implementing the changes to their Worker.
![partialWake.png](https://developer.android.com/static/blog/assets/partial_Wake_89e3b12fd0_Zlnd3b.webp)

As a result of the changes, the team has seen fewer instances of work timing out without completing, resulting in lower average runtimes.

The WHOOP team's advice to other developers that want to improve their background work's efficiency:
![sarthak.png](https://developer.android.com/static/blog/assets/sarthak_9546347d28_Z3nx8S.webp)

### **Get Started**

If you're interested in trying to reduce your app's excessive partial wake locks or trying to improve worker efficiency, view your app's excessive partial wake locks metric in [Android vitals](https://play.google.com/console/u/0/developers/app/vitals/metrics/overview), and review the [wake locks documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock) for more best practices and debugging strategies.

###### Written by:

-

  ## [Breana Tate](https://developer.android.com/blog/authors/breana-tate)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/breana-tate) ![](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp) ![](https://developer.android.com/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](https://developer.android.com/blog/authors/ben-trengrove)[![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](https://developer.android.com/blog/authors/ajesh-pai) 13 Mar 2026 13 Mar 2026 ![](https://developer.android.com/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose](https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose) TikTok is a global short-video platform known for its massive user base and innovative features.

  ###### [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove), [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](https://developer.android.com/blog/authors/mayuri-khabya) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow_forward](https://developer.android.com/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager) In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.

  ###### [Mayuri Khinvasara Khabya](https://developer.android.com/blog/authors/mayuri-khabya) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)