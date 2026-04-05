---
title: https://developer.android.com/develop/background-work/background-tasks/data-transfer-options
url: https://developer.android.com/develop/background-work/background-tasks/data-transfer-options
source: md.txt
---

Many apps need to transfer data in the background.
This guide outlines choices for reliable background data transfer, and provides
examples for how to implement them.

## Common background data transfer scenarios

This section describes some common situations where apps need to transfer
data to or from the device, and helps you choose the right tool for your
situation.

When selecting between APIs, you should consider the following questions:

- Is the transfer user-initiated?
- Is there an existing API that handles this transfer?
- Does the work need to run immediately?

| **Option** | **When to use** | **Timing** | **Examples** |
| [WorkManager](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-workmanager) | For scheduling tasks with duration less than 10 minutes that should execute when the app is not visible. | Deferrable: Can also be adjusted by constraints Immediate: Use [`setExpedited`](https://developer.android.com/guide/background/persistent/getting-started/define-work#expedited) if the work needs to run immediately | Periodically syncing data with a server Downloading or uploading media while on the network Background-initiated (not by the user) |
| [User-Initiated Data Transfer Job](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-uidt) | When the data transfer is triggered by the user and you need to keep the user informed about the transfer's progress. | Initiated by the user (i.e. button click) - starts immediately | Uploading a photo, downloading a file |
| [Foreground Service](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-other-fgs) | For short, critical tasks, or when WorkManager is not an option. A notification informs the user of the transfer's progress. | Starts immediately | [`connectedDevice`](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-connecteddevice): Syncing data with a connected device [`shortService`](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-shortservice): File processing under 3 minutes [`mediaProcessing`](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-mediaprocessing): Encoding or decoding a media file |
| [Specific API](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-specific-api) | Use if one exists for that particular operation. Can yield benefits such as optimized performance and improved system integration. | Varies | Syncing data with a connected device |
|---|---|---|---|

If your scenario is not listed under common scenarios, consult the following
sections to find the most appropriate API for your use case. It is likely that
WorkManager will be appropriate.

## Use the user-initiated data transfer job type

If your app needs to transfer data to a remote server, you may want to use a
user-initiated data transfer job. This job type is appropriate if the
following is true:

- The user began the data transfer
- You need to keep the user notified of the data transfer progress
- It is detrimental to user experience if the system interrupts the transfer

If any of these conditions is not satisfied, you should [use WorkManager](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-workmanager)
instead.

For example, a media app might let users download albums to play locally. If a
user wants to download a playlist and play it right away, you might want to use
the user-initiated data transfer job type. On the other hand, if the user wants
the downloaded playlist to update periodically in the background without user
initiation, WorkManager would be a better choice.

For more information, including how to create and run a user-initiated data
transfer job, see the documentation on [user-initiated data transfer jobs](https://developer.android.com/develop/background-work/background-tasks/uidt).

## Use WorkManager for data transfer

In most cases, WorkManager is the best option when you need to schedule work.
Keep in mind that you must design the tasks in such a way that they can be
interrupted or deferred by the system. For more information, see the
[WorkManager documentation](https://developer.android.com/develop/background-work/background-tasks/persistent).

Here are a few things to keep in mind as you use WorkManager for background
data transfer:

- If you need to run the work as soon as possible, you can [**schedule an
  expedited work request**](https://developer.android.com/guide/background/persistent/getting-started/define-work#expedited). This option is especially useful if you're scheduling the work in response to a broadcast, exact-alarm, or [high-priority FCM message](https://firebase.blog/posts/2025/04/fcm-on-android).
- If you need the work to run periodically, you can [**schedule periodic
  work**](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#schedule_periodic_work). A periodic work request lets you specify *roughly* how often the work will run, but does not guarantee a specific time. That allows the system to schedule work requests from different apps to balance the demands on the device.
- You should [**define work constraints**](https://developer.android.com/guide/background/persistent/getting-started/define-work#work-constraints) to specify the right circumstances to run your job. For example, if your app needs to download non-urgent resources, you might specify that the job should run while the device is charging and connected to an unmetered network. WorkManager can then run your job at a time that balances the load on the system.
- **WorkManager is free to cancel and retry a job if necessary** . For example, the user might turn off the device while a job is running; the system can then retry the job when the device is available again. Make sure you design and [test](https://developer.android.com/develop/background-work/background-tasks/testing/persistent/worker-impl) your workflow to make sure the cancel-and-retry cycle works properly.
- **Long running (foreground service) workers:** WorkManager can support work that takes longer than 10 minutes by creating a foreground service for your app. This means that it is subject to the same restrictions as a foreground service and jobs, including restrictions on launching from the background and execution limits (jobs taking longer than 10 minutes will be rescheduled by the system).

JobScheduler is an alternative option for scheduling background work. In
contrast to WorkManager, it requires you to do more configuration, but as an
advantage, you have access to APIs that are not currently available in
WorkManager, such as [`setPrefetch`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setPrefetch(boolean)), [`setUserInitiated`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setUserInitiated(boolean)), and
[`getPendingJobReasons`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReasons(int)).

## Use a specific API

Use a specific API if one is available (like the [companion device
manager](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing)); otherwise, [use a `connectedDevice` foreground
service](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-connecteddevice).


## AI Prompt

### Identify use-case specific APIs


This prompt asks for specific APIs for data transfer tasks.


    I want to transfer data from an Android mobile device to [device_type]. Is there a specific API available?

### Using AI prompts

AI prompts are intended to be used within Gemini in Android Studio.

Learn more about Gemini in Studio here: [https://developer.android.com/studio/gemini/overview](https://developer.android.com/studio/gemini/overview)
<button class="devsite-dialog-close">Close</button> <button class="button icon-button android-ai-prompt-help-button" data-modal-dialog-id="ai-prompt_help_modal__identify-use-case-specific-apis"> </button> <button class="button google-feedback" data-p="5207477" data-b="llm-prompts" data-context="identify-use-case-specific-apis"> Share your thoughts </button>

<br />

## Use a more specific foreground service type

If WorkManager and JobScheduler are not appropriate for the particular
background task, you may need to use a foreground service.

As always, when you're considering using a foreground service, you should
consider whether there's a better [alternative API](https://developer.android.com/develop/background-work/background-tasks#alternative-apis) tailored to your use
case.

### Use a short service foreground service

If your app needs to perform a short, critical task, a `shortService` foreground
service may be the best option. Here are some situations where a `shortService`
foreground service might be appropriate:

- The user initiates an action (like syncing data to the server) and you want to make sure the operation finishes even if the user immediately sends the app to the background.
- Saving in-memory information to persistent storage.
- Encrypting or decrypting information.

For full information, see the [`shortService` documentation](https://developer.android.com/develop/background-work/services/fgs/service-types#short-service).

> [!IMPORTANT]
> **Important:** There are a number of system restrictions on `shortService` foreground services, which are described in the service documentation. In particular, `shortService` services must complete their work quickly, in about three minutes. If you can't be confident the operation will finish that quickly, you should [use WorkManager](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options#use-workmanager).

### Use a connected device foreground service

If you need to transfer data to another local device, you may want to use a
[`connectedDevice` foreground service](https://developer.android.com/develop/background-work/services/fgs/service-types#connected-device). Here are some common situations
where you might need to do this:

- Communicating with a Bluetooth accessory, like headphones or a smart watch
- Transferring data to a locally connected device, by a USB connection, NFC, or a local internet connection

However, in these situations, you might be able to use the [companion device
manager](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) to connect with the device instead of using a foreground service.
As always, if a special-purpose API is available for your use case, that's
usually a better choice than using a foreground service.

### Use the new media processing foreground service

If you need to process media data, you can use the `mediaProcessing`
foreground service. This service type is available if your app targets Android
15 or higher. For example, this service type is appropriate if
your app needs to transcode media from one format to another for playback. For
more information, see the
[media processing foreground service documentation](https://developer.android.com/develop/background-work/services/fgs/service-types#media-processing).

> [!NOTE]
> **Note:** The system allows `mediaProcessing` services roughly 6 hours to complete their work.

## Additional resources

- [User-Initiated Data Transfer guidance](https://developer.android.com/develop/background-work/background-tasks/uidt)
- [Foreground services overview](https://developer.android.com/develop/background-work/services/fgs)