---
title: https://developer.android.com/guide/components/activities/background-starts
url: https://developer.android.com/guide/components/activities/background-starts
source: md.txt
---

Android 10 (API level 29) and higher place restrictions on when apps can start
[activities](https://developer.android.com/guide/components/activities/intro-activities) when the app runs in
the background. These restrictions help minimize interruptions for the user and
keep the user more in control of what's shown on their screen.
| **Note:** For the purpose of starting activities, an app running a foreground service is considered to be in the background. For more information, see [foreground services](https://developer.android.com/develop/background-work/services/fgs).

This guide presents notifications as an alternative for starting activities from
the background. It also lists the specific cases where the restriction doesn't
apply.

## Display notifications instead

In nearly all cases, apps in the background must
[display time-sensitive notifications](https://developer.android.com/training/notify-user/time-sensitive) to
provide urgent information to the user instead of directly starting an activity.
Such notifications include handling an incoming phone call or an active alarm
clock.

This notification-based alert and reminder system provides several advantages
for users:

- When using the device, the user sees a heads-up notification that lets them respond. The user maintains their current context and has control over the content that they see on the screen.
- Time-sensitive notifications respect the user's [Do Not Disturb](https://developer.android.com/develop/ui/views/notifications#dnd-mode) rules. For example, users might permit calls only from specific contacts or from repeat callers when Do Not Disturb is enabled.
- When the device's screen is off, the full-screen intent launches immediately.
- In the device's **Settings** screen, the user can see which apps have recently sent notifications, including from specific notification channels. From this screen, the user can control their notification preferences.

## When apps can start activities

Apps running on Android 10 or higher can start activities when
one or more of the following conditions are met:
> | **Note:** Starting from Android 14, an [explicit opt-in](https://developer.android.com/guide/components/activities/background-starts#opt-in-required) is required in addition to meeting these conditions.

- The app has a visible window, such as an activity in the foreground.
- The app has an activity in the [back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack) of the foreground task.
- The app has an activity in the back stack of an existing task on the
  [Recents screen](https://developer.android.com/guide/components/activities/recents).

  | **Note:** When such an app attempts to start a new activity, the system places that activity on top of the app's existing task but doesn't navigate away from the currently visible task. When the user later returns to the app's task, the system starts the new activity instead of the activity that had previously been on top of the app's task.
- The app has an activity that started very recently.

- The app called [`finish()`](https://developer.android.com/reference/android/app/Activity#finish()) on
  an activity very recently. This applies only when the app had either an
  activity in the foreground or an activity in the back stack of the
  foreground task at the time `finish()` was called.

- The app has one of the following services that is bound by the system. These
  services might need to launch a UI.

  - [`AccessibilityService`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
  - [`AutofillService`](https://developer.android.com/reference/android/service/autofill/AutofillService)
  - [`CallRedirectionService`](https://developer.android.com/reference/android/telecom/CallRedirectionService)
  - [`HostApduService`](https://developer.android.com/reference/android/nfc/cardemulation/HostApduService)
  - [`InCallService`](https://developer.android.com/reference/android/telecom/InCallService)
  - [`TileService`](https://developer.android.com/reference/android/service/quicksettings/TileService) (Not applicable in Android 14 (API level 34) and higher)
  - [`VoiceInteractionService`](https://developer.android.com/reference/android/service/voice/VoiceInteractionService)
  - [`VrListenerService`](https://developer.android.com/reference/android/service/vr/VrListenerService).
- The app has a service that is bound by a different, visible app. The app
  bound to the service must remain visible for the app in the background to
  start activities successfully.

  > | **Note:** Starting from Android 14, if the app bound to the service is targeting Android 14 or higher, it no longer allows the app that has the service to start a background activity by default. The app has to pass the flag `Context.BIND_ALLOW_ACTIVITY_STARTS` to allow the bound service app to start background activities.
- The app receives a notification
  [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) from the system. In
  the case of pending intents for services and broadcast receivers, the app
  can start activities for a few seconds after the pending intent is sent.

- The app receives a `PendingIntent` that is sent from a different, visible
  app.

- The app receives a system broadcast where the app is expected to launch a
  UI. Examples include [`ACTION_NEW_OUTGOING_CALL`](https://developer.android.com/reference/android/content/Intent#ACTION_NEW_OUTGOING_CALL) and
  [`SECRET_CODE_ACTION`](https://developer.android.com/reference/android/provider/Telephony.Sms.Intents#SECRET_CODE_ACTION).
  The app can start activities for a few seconds after the broadcast is sent.

- The app is associated with a companion hardware device through the
  [`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager)
  API. This API lets the app start activities in response to actions that the
  user performs on a paired device.

- The app is a [device policy controller](https://developer.android.com/work/dpc/build-dpc) running in
  [device owner mode](https://developer.android.com/work/dpc/device-management). Example use cases include
  [fully managed enterprise devices](https://developers.google.com/android/work/requirements/fully-managed-device)
  as well as [dedicated devices](https://developer.android.com/work/dpc/dedicated-devices) like digital
  signage and kiosks.

- The app is granted the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) permission by the user.

  | **Note:** Apps running on Android 10 (Go edition) [cannot receive the `SYSTEM_ALERT_WINDOW` permission](https://developer.android.com/about/versions/10/behavior-changes-all#sysalert-go).

## Opt-In required when starting activities from PendingIntents

To avoid allowing accidental Activity starts based on the [listed
conditions](https://developer.android.com/guide/components/activities/background-starts#exceptions), starting with Android 14 there are explicit APIs that allow you
to opt in or out of granting an app permissions for Activity starts.

Apps targeting Android 15 or higher will default to no longer implicitly
granting background activity launch (BAL) privileges to `PendingIntents` they
create. Explicit opt-in is required, in order to do so, these are the options
depending if the app is sending or creating `PendingIntents`.
![Pending intents table](https://developer.android.com/static/guide/components/images/pending-intent-table.svg) Figure 1: Decision flow for background activity launches.

### By the Sender of the PendingIntent

Apps targeting Android 14 or higher that want to start a `PendingIntent` must

- fulfill the [listed conditions](https://developer.android.com/guide/components/activities/background-starts#exceptions) **and**
- opt in to allow background activity launch based on those exceptions

This opt-in should **only** happen if the app developer knows that the app is
going to start an Activity.

To opt in, the app should pass an `ActivityOptions` bundle with
`setPendingIntentBackgroundActivityStartMode(ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOWED)`
to the `PendingIntent.send()` or similar methods.
| **Note:** Starting with Android 16, the app can explicitly choose to allow Activity starts only when the app is visible (`ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOW_IF_VISIBLE`) or always (`ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOW_ALWAYS`).

### By the Creator of the PendingIntent

Apps targeting Android 15 or higher that create a `PendingIntent` must now
**explicitly** opt in to allow background activity launch if they want those
`PendingIntents` to be startable under the [listed conditions](https://developer.android.com/guide/components/activities/background-starts#exceptions).

In most cases, the app starting the `PendingIntent` should be the one to opt in.
However, if the creating app needs to grant these privileges:

- The `PendingIntent` can be started at any time the creating app is visible.
- The `PendingIntent` can be started at any time if the creating app has special privileges.

| **Important:** It is a good practice to **not** pass a `PendingIntent` with these privileges to an untrusted app and to cancel the `PendingIntent` when it should no longer be used.

To opt in, the app should pass an `ActivityOptions` bundle with
`setPendingIntentCreatorBackgroundActivityStartMode
(ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOWED)` to the
`PendingIntent.getActivity()` or similar methods.
| **Note:** Starting with Android 16, the app can explicitly choose to allow Activity starts only when the app is visible (`ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOW_IF_VISIBLE`) or always (`ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOW_ALWAYS`).

Read the relevant reference documentation for further details:

- [`ActivityOptions.setPendingIntentBackgroundActivityStartMode`](https://developer.android.com/reference/android/app/ActivityOptions#setPendingIntentBackgroundActivityStartMode(int))
- [`ActivityOptions.setPendingIntentCreatorBackgroundActivityStartMode`](https://developer.android.com/reference/android/app/ActivityOptions#setPendingIntentCreatorBackgroundActivityStartMode(int))

## Strict Mode

Starting with Android 16, the app developer can enable [Strict mode](https://developer.android.com/reference/android/os/StrictMode) to get
notified when an activity launch is blocked (or at risk of getting blocked when
the app's target SDK is raised).

Example code to enable from early in your Application, Activity, or other
application component's `Application.onCreate()` method:

     override fun onCreate(savedInstanceState: Bundle?) {
         super.onCreate(savedInstanceState)
         StrictMode.setVmPolicy(
             StrictMode.VmPolicy.Builder()
             .detectBlockedBackgroundActivityLaunch()
             .penaltyLog()
             .build());
         )
     }

Read the [Strict mode](https://developer.android.com/reference/android/os/StrictMode) documentation for more details.