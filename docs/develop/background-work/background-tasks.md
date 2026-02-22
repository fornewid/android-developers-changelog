---
title: https://developer.android.com/develop/background-work/background-tasks
url: https://developer.android.com/develop/background-work/background-tasks
source: md.txt
---

# Background tasks overview

Apps frequently need to do more than one thing at a time. The Android APIs provide a lot of different ways to let you do this. Choosing the right option is very important; an option might be right for one situation but very wrong for another. Choosing the wrong APIs can hurt your app's performance or resource efficiency, which can drain the battery and degrade performance of the user's device as a whole. In some cases, choosing the wrong approach could prevent your app from being listed in the Play Store.

This document explains the different options available to you, and helps you choose the right one for your situation.

## Terminology

Some important terms related to background tasks might be used in multiple, contradictory ways. For this reason, it's important to define our terms.
| **Key Term:** An app is*running in the background* if none of its activities are visible to the user, and the app isn't running any[foreground services](https://developer.android.com/develop/background-work/services/fgs).

If an app is running in the background, the system puts a number of restrictions on it. (For example, in most cases,[an app in the background can't launch foreground services](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions).)

For the purposes of this document, we'll use the term "task" to mean an operation an app is doing outside its main workflow. To ensure alignment in understanding, we've put this into three main categories of types of tasks:[asynchronous work](https://developer.android.com/develop/background-work/background-tasks#asynchronous-work), the[task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks#background-work), and[foreground services](https://developer.android.com/develop/background-work/background-tasks#foreground-services).

## Choose the right option

In most scenarios, you can figure out the right APIs to use for your task by figuring out the category ([asynchronous work](https://developer.android.com/develop/background-work/background-tasks#asynchronous-work), the[task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks#background-work), or[foreground services](https://developer.android.com/develop/background-work/background-tasks#foreground-services)) the task falls under.

If you're still unsure, you can use the flow charts we provide which add more nuance to the decision. Each of these options is described in more detail later in this document.
| **Note:** In most cases, your best option for running background tasks is to use WorkManager. However, there are a few situations where another option is better. This page will help you understand which solution fits your needs best.

There are two main scenarios to consider for background tasks:

- [The task initiated by the user while the app is visible](https://developer.android.com/develop/background-work/background-tasks#user-initiated)
- [The task is initiated in response to an event, either internal or external](https://developer.android.com/develop/background-work/background-tasks#event-driven)

These two scenarios have their own decision trees.

## Asynchronous work

In many cases, an app just needs to do concurrent operations while it's running in the foreground. For example, an app might need to do a time-consuming calculation. If it did the calculation on the UI thread, the user wouldn't be able to interact with the app until the calculation finished; this might result in an ANR error. In a case like this, the app should use an*asynchronous work*option.

Common asynchronous work options include Kotlin coroutines and Java threads; you can find more information in the[asynchronous work](https://developer.android.com/guide/background/asynchronous)documentation. It's important to note that unlike the background task APIs, asynchronous work is not guaranteed to finish if the app stops being in a valid[lifecycle stage](https://developer.android.com/guide/components/activities/process-lifecycle)(for example, if the app leaves the foreground).

## Task scheduling APIs

The task scheduling APIs are a more flexible option when you need to do tasks that need to continue even if the user leaves the app. In most cases, the best option for running background tasks is to use[WorkManager](https://developer.android.com/guide/background/persistent), though in some cases it may be appropriate to use the platform[`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler)API.

WorkManager is a powerful library that lets you set up simple or complicated jobs as you need. You can use WorkManager to schedule tasks to run at specific times, or specify the conditions when the task should run. You can even set up chains of tasks, so each task runs in turn, passing its results to the next one. To understand all the options available, read through the[WorkManager feature list](https://developer.android.com/guide/background/persistent#workmanager-features).

Some of the most common scenarios for background tasks include:

- Fetching data from server periodically
- Fetching sensor data (for example, step counter data)
- Getting periodic location data (you must be granted[`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/training/location/receive-location-updates#request-background-location)permission on Android 10 or higher)
- Uploading content based on a content trigger, such as photos created by the camera

| **Note:** If a task is particularly urgent, you can mark it as*expedited* to instruct the system to prioritize the task to run as soon as possible. For more information, see[schedule expedited work](https://developer.android.com/guide/background/persistent/getting-started/define-work#expedited).

## Foreground services

Foreground services offer a powerful way to run tasks immediately that ought not to be interrupted. However, foreground services can potentially put a heavy load on the device, and sometimes they have privacy and security implications. For these reasons, the system puts a lot of restrictions on how and when apps can use foreground services. For example, a foreground service has to be noticeable to the user, and in most cases apps can't launch foreground services when the apps are in the background. For more information, see the[foreground services documentation](https://developer.android.com/develop/background-work/services/fgs).

There are two methods for creating a foreground service. You can declare your own[`Service`](https://developer.android.com/reference/android/app/Service)and specify that the service is a foreground service by calling[`Service.startForeground()`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification,%20int)). Alternatively, you can use WorkManager to create a foreground service, as discussed in[support for long-running workers](https://developer.android.com/guide/background/persistent/how-to/long-running). However, it's important to know that a foreground service created by WorkManager has to obey all the same restrictions as any other foreground service. WorkManager just provides some convenience APIs to make it simpler to create a foreground service.

## Alternative APIs

The system offers alternative APIs which are designed to perform better for more specific use cases. If an alternative API exists for your use case, we recommend using that API instead of a foreground service as it should help your app perform better. The[foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types)documentation notes when there's a good alternative API to use instead of a particular foreground service type.

Some of the most common scenarios for using alternative APIs are:

- Using[user-initiated data transfers](https://developer.android.com/develop/background-work/background-tasks/uidt)to do large downloads or uploads, instead of creating a data sync foreground service
- Using the[companion device manager](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing)for Bluetooth pairing and data transfer, instead of using a connected device foreground service
- Using[picture-in-picture mode](https://developer.android.com/develop/ui/views/picture-in-picture)to play video, instead of creating a media-playback foreground service

## Tasks initiated by the user

![Flowchart showing how to choose the appropriate API. This chart summarizes the material in the section 'Tasks initiated by the user'.](https://developer.android.com/static/images/develop/background-work/background-tasks/index/user-tasks-flowchart.svg)**Figure 1**: How to choose the right API for running a user-initiated background task.

If an app needs to perform background tasks, and the operation is initiated by the user while the app is visible, answer these questions to find the right approach.

### Does the task need to continue running while the app is in the background?

If the task does not need to continue running while the app is in the background, you should use[asynchronous work](https://developer.android.com/develop/background-work/background-tasks#asynchronous-work). There are a number of options for doing asynchronous work. The important thing to understand is that these options all stop operating if the app goes into the background. (They also stop if the app is shut down.) For example, a social media app might want to refresh its content feed, but it wouldn't need to finish the operation if the user left the screen.

### Will there be a bad user experience if the task is deferred or interrupted?

It's important to consider whether the user experience would be harmed if a task is postponed or canceled. For example, if an app needs to update its assets, the user might not notice whether the operation happens right away, or in the middle of the night while the device is recharging. In cases like this, you should use the[background work](https://developer.android.com/develop/background-work/background-tasks#background-work)options.
| **Note:** If a background work task takes longer than 10 minutes to complete, it's highly likely to be interrupted. You should try to find ways to break tasks like that into smaller sub-tasks. If you need to create a long-running task and you can't break it into subtasks, and you don't want the task to be interrupted, a[foreground service](https://developer.android.com/develop/background-work/background-tasks#foreground-services)may be the best option.

### Is it a short, critical task?

If the task cannot be delayed and it will complete quickly, you can use a[foreground service](https://developer.android.com/develop/background-work/background-tasks#foreground-services)with the type[`shortService`](https://developer.android.com/develop/background-work/services/fgs/service-types#short-service). These services are easier to create than other foreground services, and don't require as many permissions. However, short services must complete within three minutes.
| **Note:** Beginning with Android 12, most foreground services do not show notifications to the user until they've been running for 10 seconds.

### Is there an alternative API just for this purpose?

If the task is not invisible to the user, the correct solution may be to use a[foreground service](https://developer.android.com/develop/background-work/background-tasks#foreground-services). These services run continuously once started, so they're a good choice when interrupting the task would have a bad user experience. For example, a workout-tracking app might use location sensors to let users record their jogging route on a map. You wouldn't want to do this with a background work option, because if the task got paused, the tracking would immediately stop. In a situation like this, a foreground service makes the most sense.

However, because foreground services can potentially use a lot of device resources, the system puts a lot of restrictions on when and how they can be used. In many cases, instead of using a foreground service, you can use an[alternative API](https://developer.android.com/develop/background-work/background-tasks#alternative-apis)that handles the job for you with less trouble. For example, if your app needs to take an action when the user arrives at a certain location, your best option is to use the[geofence API](https://developer.android.com/develop/sensors-and-location/location/geofencing)instead of tracking the user's location with a foreground service.

## Tasks in response to an event

![Flowchart showing how to choose the appropriate API. This chart summarizes the material in the section 'Tasks in response to an event'.](https://developer.android.com/static/images/develop/background-work/background-tasks/index/event-tasks-flowchart.svg)**Figure 2**: How to choose the right API for running an event-triggered background task.

Sometimes an app needs to do background work in response to a trigger, such as:

- [Broadcast messages](https://developer.android.com/guide/components/broadcasts)
- [Firebase Cloud Messaging (FCM) messages](https://firebase.google.com/docs/cloud-messaging)
- [Alarms](https://developer.android.com/training/scheduling)set by the app

This might be an external trigger (like an FCM message), or it might be in response to an alarm set by the app itself. For example, a game might receive a FCM message telling it to update some assets.

If you can be sure that the task will finish in a few seconds, use[asynchronous work](https://developer.android.com/develop/background-work/background-tasks#asynchronous-work)to perform the task. The system will allow your app a few seconds to perform any such tasks, even if your app was in the background.

If the task will take longer than a few seconds, it may be appropriate to start a foreground service to handle the task. In fact, even if your app is currently in the background, it might be permitted to start a foreground service, if the task was triggered by the user and it falls into one of the approved[exemptions from background start restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions). For example, if an app receives a high-priority FCM message, the app is permitted to start a foreground service even if the app is in the background.

If the task will take longer than a few seconds, use the[task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks#background-work).