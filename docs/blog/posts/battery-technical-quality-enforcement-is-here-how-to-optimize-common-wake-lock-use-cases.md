---
title: https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases
url: https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases

###### 8-min read

![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp) 04 Mar 2026 [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) [##### Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

###### Developer Relations Engineer

In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps. On **March 1st, 2026** , Google Play Store began rolling out the [wake lock technical quality treatments](https://android-developers.googleblog.com/2025/11/raising-bar-on-battery-performance.html) to improve battery drain. This treatment will roll out gradually to impacted apps over the following weeks. Apps that consistently exceed the "Excessive Partial Wake Lock" threshold in Android vitals may see tangible impacts on their store presence, including **warnings on their store listing** and exclusion from discovery surfaces such as recommendations.
![appDetails.png](https://developer.android.com/static/blog/assets/app_Details_281748ed83_Z18iW0j.webp)

*Users may see a warning on your store listing if your app exceeds the bad behavior threshold. *

This initiative elevated battery efficiency to a core vital metric alongside stability metrics like crashes and ANRs. The "bad behavior threshold" is defined as holding a non-exempted partial wake lock for at least **two hours** on average while the screen is off in more than **5% of user sessions** in the **past 28 days** . A wake lock is exempted if it is a system held wake lock that offers clear user benefits that cannot be further optimized, such as audio playback, location access, or user-initiated data transfer. You can view the full definition of excessive wake locks in our [Android vitals documentation](https://developer.android.com/topic/performance/vitals/excessive-wakelock).

As part of our ongoing initiative to improve battery life across the Android ecosystem, we have analyzed thousands of apps and how they use partial wake locks. While wake locks are sometimes necessary, we often see apps holding them inefficiently or unnecessarily, when more efficient solutions exist. This blog will go over the most common scenarios where excessive wake locks occur and our recommendations for optimizing wake locks. We have already seen measurable success from partners like [WHOOP](https://android-developers.googleblog.com/2026/03/how-whoop-decreased-excessive-partial.html), who leveraged these recommendations to optimize their background behavior.

## **Using a foreground service vs partial wake locks**

We've often seen developers struggle to understand the difference between two concepts when doing background execution: foreground service and partial wake locks.

A foreground service is a lifecycle API that signals to the system that an app is performing user-perceptible work and should not be killed to reclaim memory, but it does not automatically prevent the CPU from sleeping when the screen turns off. In contrast, a partial wake lock is a mechanism specifically designed to keep the CPU running even while the screen is off.

While a foreground service is often necessary to continue a user action, a manual acquisition of a partial wake lock is only necessary in conjunction with a foreground service for the duration of the CPU activity. In addition, you don't need to use a wake lock if you're already utilizing an API that keeps the device awake.

Refer to the flow chart in [*Choose the right API to keep the device awake*](https://developer.android.com/develop/background-work/background-tasks/awake) to ensure you have a strong understanding of what tool to use to avoid acquiring a wake lock in scenarios where it's not necessary.

## **Third party libraries acquiring wake locks**

It is common for an app to discover that it is flagged for excessive wake locks held by a third-party SDK or system API acting on its behalf. To identify and resolve these wake locks, we recommend the following steps:

- **Check Android vitals:** Find the exact name of the offending wake lock in the [excessive partial wake locks dashboard](https://play.google.com/console/developers/app/vitals/metrics/details?metric=EXCESSIVE_BACKGROUND_WAKELOCKS&days=28). Cross-reference this name with the [*Identify wake locks created by other APIs*](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls) guidance to see if it was created by a known system API or Jetpack library. If it is, you may need to optimize your usage of the API and can refer to the recommended guidance.
- **Capture a System Trace:** If the wake lock cannot be easily identified, reproduce the wake lock issue locally using a system trace and inspect it with the Perfetto UI. You can learn more about how to do this in the [*Debugging other types of excessive wake locks*section of this blog post](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html).
- **Evaluate Alternatives:** If an inefficient third-party library is responsible and cannot be configured to respect battery life, consider communicating the issue with the SDK's owners, finding an alternative SDK or building the functionality in-house.

## **Common wake lock scenarios**

Below is a breakdown of some of the specific use cases we have reviewed, along with the recommended path to optimize your wake lock implementation.

### User-Initiated Upload or Download

**Example use cases:**

- Video streaming apps where the user triggers a download of a large file for offline access.
- Media backup apps where the user triggers uploading their recent photos via a notification prompt.

**How to reduce wake locks:**

- Do not acquire a manual wake lock. Instead, use the [User-Initiated Data Transfer (UIDT) API](https://developer.android.com/develop/background-work/background-tasks/uidt). This is the designated path for long running data transfer tasks initiated by the user, and it is exempted from excessive wake lock calculations.

### **One-Time or Periodic Background Syncs**

**Example use cases:**

- An app performs periodic background syncs to fetch data for offline access.
- Pedometer apps that fetch step count periodically.

**How to reduce wake locks:**

- Do not acquire a manual wake lock. Use [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent) configured for one-time or periodic work. `WorkManager` respects system health by batching tasks and has a minimum periodic interval (15 minutes), which is generally sufficient for background updates.
- If you identify wake locks created by `WorkManager` or JobScheduler with high wake lock usage, it may be because you've misconfigured your worker to not complete in certain scenarios. Consider [analyzing the worker stop reasons](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/observe#stop-reason), particularly if you're seeing high occurrences of [STOP_REASON_TIMEOUT](https://developer.android.com/reference/androidx/work/WorkInfo#STOP_REASON_TIMEOUT()).

```
workManager.getWorkInfoByIdFlow(syncWorker.id)
  .collect { workInfo ->
      if (workInfo != null) {
        val stopReason = workInfo.stopReason
        logStopReason(syncWorker.id, stopReason)
      }
  }
```

- In addition to logging worker stop reasons, refer to our documentation on [debugging your workers](https://developer.android.com/develop/background-work/background-tasks/testing/persistent/debug). Also, consider collecting and analyzing [system traces](https://developer.android.com/topic/performance/tracing/on-device)to understand when wake locks are acquired and released.
- Finally, check out our [case study with WHOOP](https://android-developers.googleblog.com/2026/03/how-whoop-decreased-excessive-partial.html), where they were able to discover an issue with configuration of their workers and reduce their wake lock impact significantly.

### Bluetooth Communication

**Example use cases:**

- Companion device app prompts the user to pair their Bluetooth external device.
- Companion device app listens for hardware events on an external device and user visible change in notification.
- Companion device app's user initiates a file transfer between the mobile and bluetooth device.
- Companion device app performs occasional firmware updates to an external device via Bluetooth.

**How to reduce wake locks:**

- Use [companion device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) to pair Bluetooth devices to avoid acquiring a manual wake lock during Bluetooth pairing.
- Consult the* *[*Communicate in the background*](https://developer.android.com/develop/connectivity/bluetooth/ble/background) guidance to understand how to do background Bluetooth communication.
- Using `WorkManager` is often sufficient if there is no user impact to a delayed communication. If a manual wake lock is deemed necessary, only hold the wake lock for the duration of Bluetooth activity or processing of the activity data.

### Location Tracking

**Example use cases:**

- Fitness apps that cache location data for later upload such as plotting running routes
- Food delivery apps that pull location data at a high frequency to update progress of delivery in a notification or widget UI.

**How to reduce wake locks:**

- Consult our guidance to [*Optimize location usage*](https://developer.android.com/develop/sensors-and-location/location/battery/optimize). Consider implementing timeouts, leveraging location request batching, or utilizing passive location updates to ensure battery efficiency.
- When [requesting location updates](https://developer.android.com/develop/sensors-and-location/location/request-updates) using the FusedLocationProvider or LocationManager APIs, the system automatically triggers a device wake-up during the location event callback. This brief, system-managed wake lock is exempted from excessive partial wake lock calculations.
- Avoid acquiring a separate, continuous wake lock for caching location data, as this is redundant. Instead, persist location events in memory or local storage and leverage [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent) to process them at periodic intervals.

```
override fun onCreate(savedInstanceState: Bundle?) {
    locationCallback = object : LocationCallback() {
        override fun onLocationResult(locationResult: LocationResult?) {
            locationResult ?: return
            // System wakes up CPU for short duration
            for (location in locationResult.locations){
                // Store data in memory to process at another time
            }
        }
    }
}
```

### High Frequency Sensor Monitoring

**Example use cases:**

- Pedometer apps that passively collect steps, or distance traveled.
- Safety apps that monitor the device sensors for rapid changes in real time, to provide features such as crash detection or fall detection.

**How to reduce wake locks:**

- If using [SensorManager](https://developer.android.com/reference/android/hardware/SensorManager), reduce usage to periodic intervals and only when the user has explicitly granted access through a UI interaction. High frequency sensor monitoring can drain the battery heavily due to the number of CPU wake-ups and processing that occurs.
- If you're tracking step counts or distance traveled, rather than using SensorManager, leverage [Recording API](https://developer.android.com/health-and-fitness/guides/recording-api) or consider utilizing [Health Connect](https://developer.android.com/health-and-fitness/health-connect/features/steps) to access historical and aggregated device step counts to capture data in a battery-efficient manner.
- If you're registering a sensor with [SensorManager](https://developer.android.com/reference/android/hardware/SensorManager), specify a [maxReportLatencyUs](https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int)) of 30 seconds or more to leverage **sensor batching** to minimize the frequency of CPU interrupts. When the device is subsequently woken by another trigger such as a user interaction, location retrieval, or a scheduled job, the system will immediately dispatch the cached sensor data.

```
val accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)

sensorManager.registerListener(this,
                 accelerometer,
                 samplingPeriodUs, // How often to sample data
                 maxReportLatencyUs // Key for sensor batching 
              )
```

- If your app requires both location and sensor data, synchronize their event retrieval and processing. By piggybacking sensor readings onto the brief wake lock the system holds for location updates, you avoid needing a wake lock to keep the CPU awake. Use a worker or a short-duration wake lock to handle the upload and processing of this combined data.

### Remote Messaging

**Example use cases:**

- Video or sound monitoring companion apps that need to monitor events that occur on an external device connected using a local network.
- Messaging apps that maintain a network socket connection with the desktop variant.

**How to reduce wake locks:**

- If the network events can be processed on the server side, use [FCM](https://firebase.google.com/docs/cloud-messaging/android/receive-messages) to receive information on the client. You may choose to schedule an [expedited worker](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#expedited) if additional processing of FCM data is required.
- If events must be processed on the client side via a socket connection, a wake lock is not needed to listen for event interrupts. When data packets arrive at the Wi-Fi or Cellular radio, the radio hardware triggers a hardware interrupt in the form of a kernel wake lock. You may then choose to schedule a worker or acquire a wake lock to process the data.
- For example, if you're using [ktor-network](https://ktor.io/docs/server-sockets.html) to listen for data packets on a network socket, you should only acquire a wake lock when packets have been delivered to the client and need to be processed.

```
val readChannel = socket.openReadChannel()
while (!readChannel.isClosedForRead) {
    // CPU can safely sleep here while waiting for the next packet
    val packet = readChannel.readRemaining(1024) 
    if (!packet.isEmpty) {
         // Data Arrived: The system woke the CPU and we should keep it awake via manual wake lock (urgent) or scheduling a worker (non-urgent)
         performWorkWithWakeLock { 
              val data = packet.readBytes()
              // Additional logic to process data packets
         }
    }
}
```

## Summary

By adopting these recommended solutions for common use cases like background syncs, location tracking, sensor monitoring and network communication, developers can work towards reducing unnecessary wake lock usage. To continue learning, read our other technical blog post or [watch our technical video](https://youtu.be/-6mEvkLOlno) on how to discover and debug wake locks: [Optimize your app battery using Android vitals wake lock metric](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html). Also, consult our [updated wakelock documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock). To help us continue improving our technical resources, please share any additional feedback on our guidance in our [documentation feedback survey](https://forms.gle/8ejo49EUfee7jDMD9).

###### Written by:

-

  ## [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alice-yuan) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 20 Nov 2025 20 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow_forward](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey) The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  9 min read

- [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Android CLI and skills: Build Android apps 3x faster using any agent](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent) Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando), [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)