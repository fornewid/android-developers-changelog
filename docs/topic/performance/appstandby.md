---
title: https://developer.android.com/topic/performance/appstandby
url: https://developer.android.com/topic/performance/appstandby
source: md.txt
---

Android 9 (API level 28) and later support *App Standby Buckets* . App Standby
Buckets help the system prioritize apps' requests for resources based on how
recently and how frequently the apps are used. Based on app usage patterns, each
app is placed in one of five priority *buckets*. The system limits the device
resources available to each app based on which bucket the app is in.

## Priority buckets

The system dynamically assigns each app to a priority bucket, reassigning the
apps as needed. The system might rely on a preloaded app that uses machine
learning to determine how likely each app is to be used, and assigns apps to the
appropriate buckets.

If the system app isn't present on a device, the system defaults to sorting
apps based on how recently they are used. Apps that are more active are assigned
to buckets that give them higher priority, making more system resources
available to the app. In particular, the bucket determines how frequently the
app's jobs run and how often the app can trigger alarms. These restrictions
apply only while the device is on battery power. While the device is charging,
the system doesn't impose these restrictions.
| **Note:** Every manufacturer can set their own criteria for how non-active apps are assigned to buckets. Don't try to influence which bucket your app is assigned to. Instead, focus on making sure your app behaves well in whichever bucket it might be in. To find out which bucket your app is in, call [`UsageStatsManager.getAppStandbyBucket()`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#getAppStandbyBucket()).

The priority buckets are the following:

- [Active](https://developer.android.com/topic/performance/appstandby#active-bucket): app is being used or was used very recently.
- [Working set](https://developer.android.com/topic/performance/appstandby#working-set-bucket): app is in regular use.
- [Frequent](https://developer.android.com/topic/performance/appstandby#frequent-bucket): app is often used but not daily.
- [Rare](https://developer.android.com/topic/performance/appstandby#rare-bucket): app isn't frequently used.
- [Restricted](https://developer.android.com/topic/performance/appstandby#restricted-bucket): app consumes a lot of system resources or might exhibit undesirable behavior.

In addition to these priority buckets, there's a special **never** bucket for
apps that are installed but never ran. The system imposes severe restrictions on
these apps.
| **Note:** Apps that are on the [Doze exemption list](https://developer.android.com/training/monitoring-device-state/doze-standby#exemption-cases) are exempted from the App Standby Bucket-based restrictions.

The following descriptions are for the non-predictive case. By contrast, when
the prediction uses machine learning to predict behavior, buckets are chosen in
anticipation of the user's next actions rather than based on recent usage. For
example, a recently used app might end up in the rare bucket because machine
learning predicts that the app might not be used for several hours.

### Active

An app is in the **active** bucket while it is used, is very recently used, or
when it does any of the following:

- Launches an activity.
- Runs a long running foreground service.
- Is tapped by the user from a notification.

If an app is in the active bucket, the system places minimal restrictions
on the app's jobs or alarms:

- Beginning with Android 16 (API level 36), background jobs have a generous runtime quota if they're started by an app in the active bucket. This includes jobs scheduled directly with [`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler), as well as jobs created by other libraries like [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent) or [`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager).

#### User interaction assigns apps as active

On Android 9 (API level 28) and higher, when the user interacts with your app in
certain ways, the system temporarily places your app into the active bucket.
After the user stops interacting with your app, the system places it into a
bucket based on usage history.

The following are examples of interactions that trigger this system behavior:

- The user taps on a notification that your app sends.

  | **Note:** If the user swipes away the notification without tapping on it, the system doesn't consider that action to be an interaction with your app.
- The user interacts with a foreground service in your app by tapping a [media
  button](https://developer.android.com/guide/topics/media-apps/mediabuttons).

- The user connects to your app while interacting with [Android Automotive
  OS](https://developer.android.com/training/cars#automotive-os), where your app uses either a foreground service or
  [`CONNECTION_TYPE_PROJECTION`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#CONNECTION_TYPE_PROJECTION).

### Working set

An app is in the **working set** bucket if it runs often but it isn't active.
For example, a social media app that the user launches almost daily is likely to
be in the working set. Apps are also promoted to the working set bucket if
they're used indirectly.

If an app is in the working set, the system imposes mild restrictions on its
ability to run jobs and trigger alarms. For details, see [Power management
resource limits](https://developer.android.com/topic/performance/power/power-details#app-stdby-bucket).

### Frequent

An app is in the **frequent** bucket if it is used regularly but not necessarily
every day. For example, a workout-tracking app that the user runs at the gym
might be in the frequent bucket.

If an app is in the frequent bucket, the system imposes stronger restrictions on
its ability to run jobs and trigger alarms. For details, see [Power management
resource limits](https://developer.android.com/topic/performance/power/power-details#app-stdby-bucket).

### Rare

An app is in the **rare** bucket if it isn't used often. For example, a hotel
app that the user only runs while staying at that hotel might be in the rare
bucket.

If an app is in the rare bucket, the system imposes strict restrictions on its
ability to run jobs and trigger alarms. The system also limits the app's ability
to connect to the internet. For details, see [Power management
resource limits](https://developer.android.com/topic/performance/power/power-details#app-stdby-bucket).

### Restricted

This bucket, added in Android 12 (API level 31), has the lowest priority and the
highest restrictions of all the buckets. The system considers your app's
behavior, such as how often the user interacts with it, to decide whether to
place your app in the restricted bucket.

On Android 13 (API level 33) and higher, unless your app qualifies for an
[exemption](https://developer.android.com/topic/performance/appstandby#restricted-bucket-exemptions), the system places your app in the restricted bucket in the
following situations:

- The user doesn't interact with your app for a specific number of days. On
  Android 12 (API level 31) and 12L (API level 32), the number of days
  is 45. Android 13 reduces the number of days to 8.

  | **Note:** Any duration that the device is off doesn't count towards the interactivity limit.
- Your app invokes an excessive number of [broadcasts](https://developer.android.com/guide/components/broadcasts) or [bindings](https://developer.android.com/guide/components/bound-services)
  during a 24-hour period.

If the system places your app in the restricted bucket, the following
restrictions apply:

- You can [run jobs](https://developer.android.com/topic/libraries/architecture/workmanager) once per day in a 10-minute batched session. During this session, the system groups your app's jobs with other apps' jobs.
  - Restricted jobs don't run by themselves. There must be at least one other job running or pending at the same time, which can include any other job.
- Your app can run fewer [expedited jobs](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#expedited), compared to when the system places your app in a less restrictive bucket.
- Your app can invoke one alarm per day. This alarm can be either an [exact
  alarm](https://developer.android.com/training/scheduling/alarms#exact) or an [inexact alarm](https://developer.android.com/training/scheduling/alarms#inexact).

| **Note:** Unlike other buckets, these power management restrictions apply to the restricted bucket even when the device is charging. However, restrictions are loosened when the device is charging, idle, and on an unmetered network.

#### Exemptions from the restricted bucket

The following types of apps are exempt from entering the restricted bucket and
bypass the inactivity trigger, even on Android 12 and higher:

- [Companion device](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) apps
- Apps running on a device in [Demo Mode](https://android.googlesource.com/platform/frameworks/base/+/master/packages/SystemUI/docs/demo_mode.md)
- [Device owner](https://source.android.com/devices/tech/admin/provision) apps
- [Profile owner](https://source.android.com/devices/tech/admin/managed-profiles) apps
- [Persistent](https://developer.android.com/guide/topics/manifest/application-element#persistent) apps
- VPN apps
- Apps that have the [`ROLE_DIALER`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_DIALER) role
- Apps that the user has explicitly designated to provide "unrestricted" functionality in system settings
- Apps with active [widgets](https://developer.android.com/guide/topics/appwidgets/overview)
- Apps that are granted at least one of the following permissions:
  - [`USE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)
  - [`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)

## Evaluate the priority bucket

To check which bucket your app is assigned to, do one of the following:

- Call [`getAppStandbyBucket()`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#getAppStandbyBucket()).

- Run the following command in a terminal window:

  ```bash
  adb shell am get-standby-bucket PACKAGE_NAME
  ```

  <br />

The system throttles your app whenever it's placed in an App Standby Bucket
whose value is greater than [`STANDBY_BUCKET_ACTIVE`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#STANDBY_BUCKET_ACTIVE) (10).

## Best practices

If your app is following best practices for Doze and app standby, the
later power management features aren't difficult. However, some app behaviors
which previously worked well might cause problems.

- Don't try to manipulate the system into putting your app into a certain bucket. The system's method of placing priority can change, and every device manufacturer might choose to write their own bucketing app with its own algorithm. Instead, make sure your app behaves appropriately no matter which bucket it's in.
- If an app doesn't have a launcher activity, it might never be promoted to the active bucket. Consider redesigning your app to have such an activity.
- If the users can't interact with app notifications, users are unable to
  trigger the app's promotion to the active bucket. In this case, consider
  redesigning some notifications that let users interact. For some guidelines,
  see the Material Design [Notifications design patterns](https://material.io/guidelines/patterns/notifications.html).

- If the app doesn't show a notification upon receiving a [high-priority
  Firebase Cloud Messaging (FCM) message](https://firebase.google.com/docs/cloud-messaging/android/message-priority#using_high_priority_messages_for_android), the user can't interact with
  the app and thus promote it to the active bucket. In fact, the only intended
  use for high priority FCM messages is to push a notification to the user, so
  this situation must not occur. On 12L (API level 32) and lower, if
  you inappropriately mark an FCM message as high priority when it doesn't
  trigger user interaction, it can cause future messages to be deprioritized.

  | **Note:** If the user repeatedly dismisses a notification, the system gives the user the option to block that notification in the future. Don't spam the user with notifications to try to keep your app in the active bucket.
- If apps are split across multiple packages, those packages might be in
  different buckets and have different access levels. Test these apps with the
  packages assigned to various buckets to make sure the app behaves properly.