---
title: https://developer.android.com/training/wearables/apps/power
url: https://developer.android.com/training/wearables/apps/power
source: md.txt
---

# Conserve power and battery

Power efficiency is especially important on Wear OS. The Wear OS[design principles](https://developer.android.com/design/ui/wear/guides/foundations/design-principles)focus significantly on device power usage because the watch is a small form-factor, meant for short interactions.

Compared to larger mobile devices, Wear OS devices have smaller batteries, so any battery drain is more noticeable. Furthermore, it takes the user more effort to charge a Wear OS device, compared to a mobile device. While users can charge their mobile devices at various intervals throughout the day, they need to detach a Wear OS device from their body before charging the device.

To improve your app's power efficiency, follow these design best practices:

- Your app's design should make good use of the Wear OS form factor. It shouldn't directly copy your mobile app.
- Use your existing mobile app to help with certain use cases. For example, internet and synchronization on the watch is expensive; consider whether the mobile device could do the heavy lifting, and the Wear OS device receives changes in data.
- Design your use cases for shorter interactions.
- Consider which[Wear OS events](https://developer.android.com/training/wearables/apps/power#events)do you use, and how often these events occur.
- Whenever possible, defer your app's work until the[watch is charging](https://developer.android.com/reference/androidx/work/Constraints.Builder#setRequiresCharging(kotlin.Boolean)). This especially applies to data-intensive tasks, such as syncing data, and organizing databases.

  If the device is charging and has a Wi-Fi connection, schedule jobs to prefetch data, images, and updates that the user likely wants to see in your app.

This power guide helps you understand when and how the system runs your app, and how you can limit your app's runtime and battery drain. To learn more about how particular actions are achieved---such as loading an app or scrolling through a list---visit guidance related to performance, such as the[Compose on Wear OS performance guide](https://developer.android.com/training/wearables/compose/performance).

## Monitor battery usage over time

To analyze the battery stats of a Wear OS device that runs your app, enter the following command in a terminal window on your development machine:  

    adb shell dumpsys batterystats

A library on GitHub features a[battery stats parser](https://gist.github.com/ithinkihaveacat/7e7d0f2f620cc27ad606d2df85d81fa5), which could be useful to run along with this command.

## Events that affect battery life

Before thinking about your app specifically, it's worth thinking more generally about the events that consumes power on a Wear OS device.

The following table shows the relative effect on battery life across several common events in Wear OS apps. The exact power drain varies among devices.

|                     Event                     | Impact on battery life |                                                                                                                 How to mitigate                                                                                                                 |
|-----------------------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access the network, including LTE and Wi-Fi   | Very high              | Defer non-essential network access until the device is charging.                                                                                                                                                                                |
| Turn the screen on and start interactive mode | High                   | Don't encourage the user to keep the screen on longer than necessary. Provide an experience that uses[always-on mode](https://developer.android.com/training/wearables/views/always-on#ambient-lifecycle-observer), also known as ambient mode. |
| Access the GPS sensor                         | High                   | If possible, wait until the user requests GPS access.                                                                                                                                                                                           |
| Keep CPU usage high                           | High                   | [Consume flows using Jetpack Compose](https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3).                                                                                                             |
| Access the heart rate sensor                  | Medium                 | Use the processor's awake time when receiving callbacks from the sensor API, such as when using[Health Services on Wear OS](https://developer.android.com/health-and-fitness/guides/health-services).                                           |
| Access another device over Bluetooth          | Medium                 | Keep sessions short.                                                                                                                                                                                                                            |
| Hold a wakelock                               | Medium                 | Reduce manual creation of wakelocks and use[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started).                                                                                  |

## Minimize screen-on time

In your Wear OS app, follow these screen usage principles:

- **Screen-on locks:** Avoid whenever possible. To test, turn off**Always-on display**in system settings, and observe whether the screen goes off within the timeout period.
- **Animations:**Minimize elaborate animations, and instead focus on brief transitions for a more professional look. In particular, avoid long-running animations and loops. If a loop is required, add a pause between loops that's at least as long as the animation itself.
- **Time awake in ambient mode:** Support[always-on](https://developer.android.com/training/wearables/always-on)if necessary, such as for fitness use cases. If your app requires always-on, follow these[recommendations for Ambient mode](https://developer.android.com/training/wearables/always-on#ambient-appearance).

## Minimize CPU usage

In your Wear OS app, follow these CPU usage principles:

- Keep usage short.
- Batch any related operations, to maximize the time that your app's process is idle.

## Minimize wakelocks

In most cases, avoid any operations that prevent your app from sleeping, such as[wakelocks](https://developer.android.com/develop/background-work/background-tasks/scheduling/wakelock). For example, in health \& fitness apps, long-running workouts don't need a wakelock. Use the processor's awake time when receiving callbacks from the sensor API, such as when using[Health Services on Wear OS](https://developer.android.com/health-and-fitness/guides/health-services).

There are some cases where it's OK to acquire a wakelock, such as when your app does one of the following:

- Plays media in the background.
- Uses[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)or[`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler). (The system holds a wakelock on your behalf when running the job in the background.)

[Battery Historian](https://developer.android.com/topic/performance/power/setup-battery-historian)lets you can see individual occurrences of long wakelocks, as well as summaries of the total number and duration of wakelocks being held. Inspect the number and duration of the wakelocks that your app holds, and compare this information to the interactive usage patterns of your app:

- Check for unexpected wakelocks.
- If the duration is longer than expected, consider whether the work is blocked on some dependency, such as availability of the network.

## Inspect how your app becomes inactive

Consider what the active app is doing when key device events occur, such as the following:

- The screen goes off and the device enters ambient mode.
- The app is[swipe-dismissed](https://developer.android.com/design/ui/wear/guides/components/swipe-to-dismiss).

  | **Note:** When the user swipe-dismisses an app, the system sometimes waits a few minutes before it kills the app's process.

To analyze app activity, use the tools shown in the following sections.

### Power Profiler

[Power Profiler](https://developer.android.com/studio/profile/power-profiler)is accessible in the Android Studio menu by selecting**View \> Tool Windows \> Profiler**:

1. Inspect the system trace as the screen goes off and the device enters ambient mode.
2. Look for any work that continues, and for the device's CPU usage level.

### Perfetto

[Perfetto](https://ui.perfetto.dev/)lets you record a trace and then inspect your app to see if there are any threads doing any work when either the screen turns off, the device enters ambient mode, or the user dismisses your app's activity.

Define[custom events](https://developer.android.com/topic/performance/tracing/custom-events)to mark your app's significant events, including domain-specific events. For a media app, this would include tasks like fetching playlists, downloading a specific media item, starting playback, and stopping playback. By defining these events, you can see them in Perfetto and compare their timing with your app's CPU and power usage.

## Analyze your app's scheduled jobs

Scheduled jobs, using[WorkManager](https://developer.android.com/guide/background/persistent/getting-started), let you perform background work in your app. Although some background work must be periodic, don't run jobs too frequently or for a long duration, because this can drain the device's battery.

Use[Battery Historian](https://developer.android.com/topic/performance/power/setup-battery-historian)to inspect the execution of Scheduled Jobs, both overall (**System stats \> Jobscheduler stats** ) and by app (**App stats \> Scheduled job**). Check the total count and the total duration:

- If a job runs very frequently, consider reducing this frequency.
- Check that the total execution time matches what you expect, and isn't significantly longer.

Also, inspect the Battery Historian graph, looking at each**JobScheduler**entry. When you hold the pointer over a particular entry, Battery Historian shows the owner of the executing job. Consider the following:

- For your app, the duration of execution should make sense.
- Consider whether the jobs happen while your app is running, or whether the jobs represent periodic background work.

## Sensors

Wear OS devices have many different sensors, such as GPS. In most cases, use[Health Services on Wear OS](https://developer.android.com/health-and-fitness/guides/health-services)instead of interacting directly with`SensorManager`. In many cases, Health Services intelligently batches data to improve battery performance.

To analyze sensor usage in your app, run the following command in a terminal window on your development machine:  

    adb shell dumpsys sensorservice

The results of this command show the following:

- Current and previous sensor registrations.
- Sensor configuration, including batching if set.
- Recently sampled data.

### Test unregistration from sensors

To check whether your app stops fetching sensor data as expected, test the following scenarios:

1. Swipe-dismiss your app.
2. Tap the screen with your palm. This either turns the screen off or places the screen in ambient mode.

Use the ADB command from the previous section to check whether the sensor correctly shows as unregistered.

## Data Layer

When using the[Data Layer API](https://developer.android.com/training/wearables/data/data-layer), each transmission uses some power. In particular, if you use this API to send data, your app must wake up to receive the data. For these reasons, be conservative with your usage of this API.
| **Note:** Consider sending and receiving some data at a later time, using a`WorkManager`sync operation, while the Wear OS device is charging.

Some additional best practices for using the Data Layer API include the following:

- Wait until your app is active before you set up a listener using[`WearableListenerService`](https://developer.android.com/training/wearables/data/data-layer#wearablelistenerservice).
- Transmit state changes instead of configuring rapid updates. These state changes let the Wear OS device perform local data calculations, such as when a workout session started.

  Only transmit state changes that update your UI. For example, if your activity screen only shows "kilometers ran" to one decimal place, don't send a state change to the Wear OS each time the user moves another meter forward.

To analyze Data Layer API usage in your app, run the following command in a terminal window on your development machine:  

    adb shell dumpsys activity service WearableService

The results of this command include the following:

- **RpcService:** Lets you see how often and which paths are being called using`MessageClient`.
- **DataService:** Lets you see how often data items are being set using`DataClient`.

## Health and Fitness apps

If you maintain a health and fitness app, use[Health Services](https://developer.android.com/health-and-fitness/guides/health-services)to optimize your app's use of sensors.

- For`ExerciseClient`, use[Battery Historian](https://developer.android.com/topic/performance/power/setup-battery-historian)to verify correct behavior in ambient mode. Check that your app doesn't wake up more frequently than every minute or two to receive`ExerciseUpdate`data.
- For all-day general health monitoring, use the`PassiveMonitoringClient`, as described in the guide on how to[monitor health and fitness data in the background](https://developer.android.com/health-and-fitness/guides/health-services/monitor-background).

## Tiles and complications

If your app supports a[tile](https://developer.android.com/training/wearables/tiles)or a[complication](https://developer.android.com/training/wearables/complications), follow these best practices:

- Disable automatic refresh, or increase the refresh rate to 2 hours or longer.
- Use[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging)or[appropriately scheduled jobs](https://developer.android.com/guide/background/persistent/getting-started)to send data updates. Take care to prevent a fast rate of updates, which can cause the system to schedule repeated work at a faster rate than the user or platform can access the data needed to perform that work.
- Don't schedule work for your tile or complication when the user isn't interacting with it.
- Use[offline-first approaches](https://developer.android.com/topic/architecture/data-layer/offline-first).
- Share a single database across your main app, tiles, and complications. This helps data stay consistent across UI surfaces, too.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Access location in the background](https://developer.android.com/develop/sensors-and-location/location/background)
- [Schedule alarms](https://developer.android.com/develop/background-work/services/alarms)
- [Create an advanced widget {:#advanced-widget}](https://developer.android.com/develop/ui/views/appwidgets/advanced)