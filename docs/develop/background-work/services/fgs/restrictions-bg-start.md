---
title: https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start
url: https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start
source: md.txt
---

Apps that target Android 12 (API level 31) or higher can't start foreground
services while the app is running in the background, except for [a few special
cases](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions). If an app tries to start a
foreground service while the app runs in the background, and the foreground
service doesn't satisfy one of the exceptional cases, the system throws a
[`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).
| **Note:** If one app calls `Context.startForegroundService()` to start a foreground service that another app owns, these restrictions apply only if **both** apps target Android 12 or higher.

In addition, if an app wants to launch a foreground service that needs
*while-in-use* permissions (for example, body sensor, camera, microphone, or
location
permissions), it cannot *create* the service while the app is in the background,
even if the app falls into one of the exemptions from background start
restrictions. The reason for this is explained in the section [Restrictions on
starting foreground services that need while-in-use
permissions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions).

## Exemptions from background start restrictions

In the following situations, your app can start foreground services even while
your app runs in the background:

- Your app transitions from a user-visible state, such as an [activity](https://developer.android.com/guide/components/activities/intro-activities).
- Your app can [start an activity from the
  background](https://developer.android.com/guide/components/activities/background-starts), except for the case where the app has an activity in the back stack of an existing task.
- Your app receives a high priority message using [Firebase Cloud
  Messaging](https://firebase.google.com/docs/cloud-messaging).

  | **Note:** The system can downgrade the high priority
  | messages to normal priority if the app is not using the high priority messages
  | for surfacing time sensitive content to the user. If the message's priority is
  | downgraded, your app cannot start a foreground service and attempting to start
  | one results in a
  | [`ForegroundServiceStartNotAllowedException`](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).
  |
  | So, it's recommended to check the result of
  | [`RemoteMessage.getPriority()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getPriority())
  | and confirm it's
  | [`PRIORITY_HIGH()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#PRIORITY_HIGH())
  | before attempting to start a foreground service. For guidance on high priority
  | messages and when to use them, refer to
  | [`FCM's
  | documentation`](https://firebase.google.com/docs/cloud-messaging/android/message-priority).
- The user performs an action on a UI element related to your app. For example,
  they might interact with a [bubble](https://developer.android.com/guide/topics/ui/bubbles),
  [notification](https://developer.android.com/develop/ui/views/notifications),
  [widget](https://developer.android.com/guide/topics/appwidgets/overview), or activity.

- Your app invokes an [exact alarm](https://developer.android.com/training/scheduling/alarms#exact) to
  complete an action that the user requests.

- Your app is the device's current [input
  method](https://developer.android.com/guide/topics/text/creating-input-method).

- Your app receives an event that's related to
  [geofencing](https://developer.android.com/training/location/geofencing) or [activity
  recognition transition](https://developer.android.com/guide/topics/location/transitions).

- After the device reboots and receives the
  [`ACTION_BOOT_COMPLETED`](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED),
  [`ACTION_LOCKED_BOOT_COMPLETED`](https://developer.android.com/reference/android/content/Intent#ACTION_LOCKED_BOOT_COMPLETED),
  or [`ACTION_MY_PACKAGE_REPLACED`](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_REPLACED)
  intent action in a [broadcast receiver](https://developer.android.com/guide/components/broadcasts).

  | **Note:** If your app targets Android 14 or higher, there are restrictions on launching certain foreground service types from a `BOOT_COMPLETED` receiver. For more information, see [Restrictions on
  | `BOOT_COMPLETED` broadcast receivers launching foreground
  | services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).
- Your app receives the
  [`ACTION_TIMEZONE_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_TIMEZONE_CHANGED),
  [`ACTION_TIME_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_TIME_CHANGED),
  or
  [`ACTION_LOCALE_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_LOCALE_CHANGED)
  intent action in a broadcast receiver.

- Your app receives the
  [`ACTION_TRANSACTION_DETECTED`](https://developer.android.com/reference/android/nfc/NfcAdapter#ACTION_TRANSACTION_DETECTED)
  event from `NfcService`.

- Apps with certain system roles or permission, such as [device
  owners](https://source.android.com/devices/tech/admin/managed-profiles#device_owners)
  and [profile
  owners](https://source.android.com/devices/tech/admin/managed-profiles#profile_owners).

- Your app uses the [Companion Device Manager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) and declares the
  [`REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)
  permission or the [`REQUEST_COMPANION_RUN_IN_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)
  permission. Whenever possible, use
  `REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND`.

- The user turns off battery optimizations for your app.

- Your app holds the
  [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
  permission.
  Note: If your app targets Android 15 or higher, it must have
  the `SYSTEM_ALERT_WINDOW` permission *and* the app must currently have a
  visible overlay window.

### Restrictions on starting foreground services that need while-in-use permissions

On Android 14 (API level 34) or higher, there are special situations to be aware
of if you're starting a foreground service that needs while-in-use permissions.

If your app targets Android 14 or higher, the operating system
checks when you create a foreground service to make sure your app has all the
appropriate permissions for that service type. For example, when you create a
foreground service of type
[microphone](https://developer.android.com/develop/background-work/services/fgs/service-types#microphone), the operating
system verifies that your app currently has the
[`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO)
permission. If you don't have that permission, the system throws a
[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

For while-in-use permissions, this causes a potential problem. If your app has a
while-in-use permission, it only has that permission *while it's in the
foreground* . This means if your app is in the background, and it tries to create
a foreground service of type camera, location, or microphone, the system sees
that your app doesn't *currently* have the required permissions, and it throws a
`SecurityException`.

Similarly, if your app is in the background and it creates a
health service that needs the `BODY_SENSORS` permission, the app
doesn't currently have that permission, and the system throws an exception.
(This doesn't apply if it's a health service that needs different permissions,
like `ACTIVITY_RECOGNITION`.) Calling
[`PermissionChecker.checkSelfPermission()`](https://developer.android.com/reference/androidx/core/content/PermissionChecker#checkSelfPermission(android.content.Context,java.lang.String))
does *not* prevent this problem. If your app has a while-in-use permission, and
it calls `checkSelfPermission()` to check if it has that permission, the method
returns `PERMISSION_GRANTED` even if the app is in the background. When the
method returns `PERMISSION_GRANTED`, it's saying "your app has this permission
*while the app is in use*."
| **Note:** On versions of Android lower than Android 14, if you tried to create a foreground service that needed while-in-use permissions while your app was in the background, the system would let you create the service, but the service wouldn't have access to the needed resources, and if it tried to use them, you'd get an exception. On Android 14 or higher, your app gets the exception as soon as it tries to create the foreground service.

For this reason, if your foreground service needs a while-in-use permission, you
must call `Context.startForegroundService()` or `Context.bindService()` while
your app has a visible activity, unless the service falls into one of the
[defined exemptions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions-exemptions).


#### Exemptions from restrictions on while-in-use permissions

In some situations, even if a foreground service is started while the app
[runs
in the background](https://developer.android.com/guide/background#definition), it can still access location,
camera, and microphone information while the app runs in the foreground
("while-in-use").

In these same situations, if the service [declares a foreground service
type](https://developer.android.com/develop/background-work/services/fgs/declare) of `location` and is started by an app that
has the [`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)
permission, this service can access location information all the time, even when
the app runs in the background.

The following list contains these situations:

- A system component starts the service.
- The service starts by interacting with [app
  widgets](https://developer.android.com/guide/topics/appwidgets/overview).
- The service starts by interacting with a notification.
- The service starts as a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) that is sent from a different, visible app.
- The service starts by an app that is a [device policy
  controller](https://developer.android.com/work/dpc/build-dpc) that runs in device owner mode.
- The service starts by an app which provides the `VoiceInteractionService`.
- The service starts by an app that has the `START_ACTIVITIES_FROM_BACKGROUND` privileged permission.

#### Determine which services are affected in your app

When testing your app, start its foreground services. If a started service has
restricted access to location, microphone, and camera, the following message
appears in Logcat:  

```
Foreground service started from background can not have \
location/camera/microphone access: service SERVICE_NAME
```