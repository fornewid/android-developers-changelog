---
title: https://developer.android.com/topic/performance/power/power-details
url: https://developer.android.com/topic/performance/power/power-details
source: md.txt
---

# Power management resource limits

The system prioritizes apps' requests for resources based on the device state, app state and the[app's standby bucket](https://developer.android.com/topic/performance/appstandby).

The Android system can enforce resource limits in two different ways. One way to optimize resource utilization is to defer the execution of work until the device has left a low power device state such as[doze mode](https://developer.android.com/training/monitoring-device-state/doze-standby). For example, regular jobs and inexact alarms are deferred so they execute after the device leaves doze mode.

Another way is to reduce how much the app can wake up the device and do work, based on the app's current standby bucket. The system can reduce both the*frequency* (how often the app wakes up the device) and the*total duration* (the amount of time the device stays awake). For example, if the app is in the*rare*standby bucket, the app can run scheduled jobs for a total period of 10 minutes in a rolling 24 hour period.

Note that WorkManager uses JobScheduler to schedule tasks when the app is not visible and workers are thus impacted by job resource limits.

You can understand the restrictions further by reading:

1. [Resource limits based on device state](https://developer.android.com/topic/performance/power/power-details#device-state)
2. [Resource limits based on app state](https://developer.android.com/topic/performance/power/power-details#app-state)
3. [Resource limits based on app standby bucket](https://developer.android.com/topic/performance/power/power-details#app-stdby-bucket)

Note that the device state and app state can supersede app standby bucket limits. For example, if the device is charging, the system allows apps in the*rare*standby bucket to execute jobs for longer than 10 minutes in a rolling 24-hour period.

There have been behavior changes that have also impacted resource limits. See[Android Behavior changes that impact resource limits](https://developer.android.com/topic/performance/power/power-details#changes)to learn more.

## Resource limits based on device state

The system can also exempt or enforce resource limits based on device state. For example, a device in the*charging*state is given unrestricted resource access regardless of its app standby bucket.

|-------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Device state                  | Jobs                                                                                                            | Alarms                                                                                                                                                  | Network access                                        | Firebase Cloud Messaging                                                                |
| Charging                      | No execution limits except for*restricted*standby bucket                                                        | No execution limits for all standby buckets and process states, except if user manually restricts app battery                                           | No restrictions                                       | No restrictions                                                                         |
| Screen on                     | Execution limits are enforced based on the standby bucket                                                       | Execution limits are enforced based on the app process and standby bucket                                                                               | Access depends on standby bucket or app process state | No restrictions                                                                         |
| Screen off and doze is active | Execution limits are enforced based on the standby bucket, and execution is deferred to doze maintenance window | Execution limits are enforced based on the standby bucket. Regular alarms: Deferred to doze maintenance window While-idle alarms: Limited to 7 per hour | Restricted during doze                                | High priority: No execution limits Normal priority: Deferred to doze maintenance window |

## Resource limits based on app state

Whether or not the system enforces the app standby bucket's resource limits depends on the app process importance. Check out[`ActivityManager.RunningAppProcessInfo.importance`](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo#importance)to understand the different levels of process importance.

The device user can also choose to[manually override](https://developer.android.com/topic/performance/background-optimization#bg-restrict)the app power management optimizations, which supersedes app standby bucket limits.

|-----------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------|
| App state                                     | Jobs                                                            | Alarms                                                    | Network                                          |
| App process is visible or in foreground state | No execution limits                                             | No frequency limits                                       | No restrictions                                  |
| App process is running a foreground service   | Execution limits are enforced based on the standby bucket\*\*\* | Frequency limits are enforced based on the standby bucket | No restrictions                                  |
| User manually restricts app battery           | Execution is restricted                                         | Execution is restricted                                   | Access depends on standby bucket behavior        |
| User manually unrestricts app battery         | Execution limit is generous\*\*\*                               | No execution limits                                       | Unrestricted unless device is in data saver mode |

\*\*\* Execution quota behavior for jobs[changed in Android 16](https://developer.android.com/topic/performance/power/power-details#changes-a16). Prior to Android 16 there was no execution limit when the app was running a foreground service or the user unrestricted the app battery.

## Resource limits based on app standby bucket

**Note**: The values in this table are not a guarantee of execution durations, as other device conditions or bucket changes can affect resource constraints. The values are also subject to change in future Android releases.

Regular jobs, expedited jobs, alarms and network access can be limited based on the app standby bucket. Understand how app standby buckets affect your app using these approximate power management limitations as a guideline. For optimal performance, adhere to the[app standby best practices](https://developer.android.com/topic/performance/appstandby)and[optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery).

Note that starting in[Android 13](https://developer.android.com/topic/performance/power/power-details#changes-a13), the app's standby bucket no longer determines how many high priority FCMs an app can use.

|--------------------|------------------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| App standby bucket | Regular jobs\*                                       | Expedited jobs\*\*                          | Alarms                                                                                                                                                                                          | Network         |
| Active:            | Up to 20 minutes in a rolling 60 minute period\*\*\* | Up to 30 mins in a rolling 24h period\*\*\* | No execution limits                                                                                                                                                                             | No restrictions |
| Working set:       | Up to 10 minutes in a rolling 4 hour period          | Up to 15 minutes in a rolling 24h period    | Limited to 10 per hour                                                                                                                                                                          | No restrictions |
| Frequent:          | Up to 10 minutes in a rolling 12 hour period         | Up to 10 minutes in a rolling 24h period    | Limited to 2 per hour                                                                                                                                                                           | No restrictions |
| Rare:              | Up to 10 minutes in a rolling 24 hour period         | Up to 10 minutes in a rolling 24h period    | Limited to 1 per hour                                                                                                                                                                           | Disabled        |
| Restricted:        | Once per day for up to 10 minutes                    | Up to 5 minutes in a rolling 24h window     | One alarm per day, either an[exact alarm](https://developer.android.com/training/scheduling/alarms#exact)or an[inexact alarm](https://developer.android.com/training/scheduling/alarms#inexact) | Disabled        |

\* Regular jobs describe jobs that are not using[`setUserInitiated(true)`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setUserInitiated(boolean))or[`setExpedited(true)`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setExpedited(boolean))flags in JobScheduler or[expedited workers](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#execute-expedited)in WorkManager.

\*\* Expedited jobs have a separate execution limit than regular jobs, they can be[configured in WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#quota_policies)to continue running using regular job execution limits once expedited limits are exhausted.

\*\*\* Execution quota behavior for jobs[changed in Android 16](https://developer.android.com/topic/performance/power/power-details#changes-a16). Prior to Android 16 there was no execution limit when the app is in the active standby bucket.

## Android behavior changes that impact resource limits

The following Android updates made changes to app resource limits.

### Android 16

[**JobScheduler quota optimizations behavior change**](https://developer.android.com/about/versions/16/behavior-changes-all#job-quota-opt)

Android has adjusted regular and expedited job execution runtime quota based on the following factors:

1. Which app standby bucket the app is in
2. If the job starts execution while the app is in a top state
3. If the job is executing while running a Foreground Service

### Android 13

[**High Priority Firebase Cloud Message (FCM) Quotas behavior change**](https://developer.android.com/about/versions/13/behavior-changes-all#fcm-quotas)

- [App Standby Buckets](https://developer.android.com/topic/performance/appstandby)no longer determine how many high priority FCMs an app can use.
- System now downgrades the high priority messages if it detects an app consistently sending high-priority messages that don't result in a notification
- For current guidelines on high priority messages, refer to[firebase documentation on set and manage message priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority).

### Android 9

[**App Standby Buckets feature is introduced**](https://developer.android.com/about/versions/pie/power#buckets)

Android 9 introduces a new battery management feature, App Standby Buckets. App Standby Buckets helps the system prioritize apps' requests for resources based on how recently and how frequently the apps are used. Based on the app usage patterns, each app is placed in one of five priority buckets. The system limits the device resources available to each app based on which bucket the app is in.