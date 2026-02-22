---
title: https://developer.android.com/training/cars/platforms/automotive-os/notifications
url: https://developer.android.com/training/cars/platforms/automotive-os/notifications
source: md.txt
---

# Notifications on Android Automotive OS

Notifications provide drivers with short, timely information about events from your app while it's not in use. Notifications can appear in the[Notification Center](https://developer.android.com/training/cars/platforms/automotive-os/notifications#nc), and some notifications can also appear as[*heads-up notifications*](https://developer.android.com/training/cars/platforms/automotive-os/notifications#hun)on the display. To create notifications for Android Automotive OS, you use the same[`NotificationBuilder`](https://developer.android.com/reference/android/app/Notification.Builder)API that you use for other devices. However, to help ensure the safety of drivers and minimize distraction,[some API methods and classes](https://developer.android.com/training/cars/platforms/automotive-os/notifications#api-changes)are restricted or behave differently.

## How notifications differ in cars

To create a safe driving environment that is free from distractions, notifications on Android Automotive OS differ from notifications on other devices in the following ways:

- Simplified user interaction
- UX restrictions based on drive state

### Simplified user interaction

To help ensure that drivers can focus on the road, notifications in the car have a simplified user interaction model with the following features:

No complex controls
:   Notifications don't allow complex controls, such as tapping to expand a notification, long-pressing a notification for additional options, or using controls based on swipe-length gestures.

Notification sounds
:   Notifications only play a sound if they trigger a heads-up notification.

Automatic play and mute buttons for messaging notifications

:   Android Automotive OS automatically adds**Play** and**Mute** buttons to all[car-compatible messaging notifications](https://developer.android.com/training/cars/platforms/automotive-os/notifications#messaging-requirements).

    - **Play:**reads the notification to the driver using the user's default digital assistant, such as the Google Assistant, or the vehicle's default text-to-speech system.
    - **Mute:**prevents heads-up notifications from appearing for any future messages in the conversation for the remainder of the drive. Message notifications from a muted conversation still appear in the Notification Center, and the driver can also unmute the conversation from the Notification Center.

      | **Note:** When a user mutes a conversation in Android Automotive OS, that conversation is not muted on the user's phone.

Simplified notification display options

:   [`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews)and custom content views are not supported. In addition, the following notification styles are not supported:

    - [`BigPictureStyle`](https://developer.android.com/reference/android/app/Notification.BigPictureStyle)
    - [`BigTextStyle`](https://developer.android.com/reference/android/app/Notification.BigTextStyle)
    - [`InboxStyle`](https://developer.android.com/reference/android/app/Notification.InboxStyle)
    - [`ProgressStyle`](https://developer.android.com/reference/android/app/Notification.ProgressStyle)

    If your app sends a notification to Android Automotive OS using one of these notification styles, only summary text is shown.

Simplified notification channel management

:   Android Automotive OS does not support notification channels and related UI affordances, to decrease the prevalence of rich management tasks in Automotive devices.

### UX restrictions based on drive state

Android Automotive OS includes a UX Restrictions Engine. Car manufacturers can use this engine to restrict notifications based on the car's drive state in the following ways:

- Truncating notification strings at a specific character length
- Hiding message summaries for[`CATEGORY_MESSAGE`](https://developer.android.com/reference/android/app/Notification#CATEGORY_MESSAGE)notifications
- Limiting the number of notifications that the Notification Center can display

### Supported resource types

By default, Android Automotive OS supports a limited subset of the resource types that can be used for notifications on other devices. This subset includes the following resource types:

- Drawables
- Icons
- Images

### Compatibility requirements for messaging notifications

To provide a consistent and minimally distracting user experience, messaging notifications have special requirements on Android Automotive OS.

A messaging notification is car-compatible if it fulfills the following requirements:

- It belongs to the[`CATEGORY_MESSAGE`](https://developer.android.com/reference/android/app/Notification#CATEGORY_MESSAGE)category.
- It uses the[`Notification.MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle)style.
- It includes only unread messages.
- It has a mark-as-read`Action`that fulfills the following requirements:

  - The semantic action is set to[`Action.SEMANTIC_ACTION_MARK_AS_READ`](https://developer.android.com/reference/android/app/Notification.Action#SEMANTIC_ACTION_MARK_AS_READ).
  - The`Action`indicates that it does not show any user interface when fired.
- If the notification has a reply`Action`, then the`Action`fulfills the following requirements:

  - The semantic action is set to[`Action.SEMANTIC_ACTION_REPLY`](https://developer.android.com/reference/android/app/Notification.Action#SEMANTIC_ACTION_REPLY).
  - The`Action`indicates that it does not show any user interface when fired.
  - The`Action`contains a single[`RemoteInput`](https://developer.android.com/reference/androidx/core/app/RemoteInput).

## Notification Center

Almost all notifications appear in the Notification Center, even if those notifications were also triggered as heads-up notifications. Notifications persist in the Notification Center for the duration of a drive.

Drivers can interact with notifications in the Notification Center. Depending on the car's manufacturer, drivers access the Notification Center in one or both of the following ways:

- Swiping down from the top of the screen, similar to the notification drawer on other devices.
- Tapping a button in the system interface.

### Grouped notifications

[Related notifications](https://developer.android.com/training/notify-user/group)are automatically grouped in the Notification Center, as in the notification drawer on other devices. However, when a driver taps the summary for a group in the Notification Center, instead of launching a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent), the group expands to show all of its notifications.

### Notifications that don't appear in the Notification Center

The following notifications don't appear in the Notification Center:

- [`Media playback`](https://developer.android.com/reference/android/app/Notification.MediaStyle)notifications. Android Automotive OS gathers information about ongoing media playback and displays it in a dedicated place in the user interface. Note that you must call[`setMediaSession`](https://developer.android.com/reference/android/app/Notification.MediaStyle#setMediaSession(android.media.session.MediaSession.Token))with a non-null token for the system to recognize the notification as media playback.
- Turn-by-turn navigation notifications for[`CATEGORY_NAVIGATION`](https://developer.android.com/reference/android/app/Notification#CATEGORY_NAVIGATION).
- Foreground service notifications for system privileged apps and apps that are signed with the platform key that have an importance level lower than[`IMPORTANCE_DEFAULT`](https://developer.android.com/reference/android/app/NotificationManager#IMPORTANCE_DEFAULT).

## Heads-up notifications

Heads-up notifications appear as a notification card on top of the screen. Because a heads-up notification draws the driver's attention, only trigger a heads-up notification when the information is drive-critical, time sensitive, and actionable. Only certain categories of notifications can trigger a heads-up notification.

Car manufacturers can decide whether to permit heads-up notifications to appear while the Notification Center is open.

### How apps trigger heads-up notifications

Apps have different requirements for triggering a heads-up notification depending on whether they have system privileges.

System-privileged apps and apps signed with the platform key
:   The app can trigger a heads-up notification by setting the notification channel importance to[`IMPORTANCE_HIGH`](https://developer.android.com/reference/android/app/NotificationManager#IMPORTANCE_HIGH)or higher.

All other apps

:   The app can trigger a heads-up notification by setting the notification channel importance to`IMPORTANCE_HIGH`or higher and verifying that the notification belongs to one of the following categories:

    - [`CATEGORY_CALL`](https://developer.android.com/reference/android/app/Notification#CATEGORY_CALL)
    - [`CATEGORY_MESSAGE`](https://developer.android.com/reference/android/app/Notification#CATEGORY_MESSAGE)
    - [`CATEGORY_NAVIGATION`](https://developer.android.com/reference/android/app/Notification#CATEGORY_NAVIGATION)
| **Note:** Some car manufacturers have a dedicated screen for navigation. In these cases, the manufacturer can configure Android Automotive OS so that`CATEGORY_NAVIGATION`heads-up notifications aren't displayed.

### Life of a heads-up notification

After an app triggers a heads-up notification, the notification appears immediately on the car's screen. If the driver takes no action, the heads-up notification dismisses automatically after 8 seconds, except in the following cases:

- Heads-up notifications for certain incoming calls cannot be dismissed, and the heads-up notification remains until either the driver accepts the call or the call is terminated. To qualify as an undismissable heads-up notification for an incoming call, a notification must fulfill the following requirements:

  - Belong to[`CATEGORY_CALL`](https://developer.android.com/reference/android/app/Notification#CATEGORY_CALL)
  - [Set a fullscreen intent](https://developer.android.com/reference/android/app/Notification.Builder#setFullScreenIntent(android.app.PendingIntent,%2520boolean))
  - Be marked as ongoing using the[`setOngoing()`](https://developer.android.com/reference/android/app/Notification.Builder#setOngoing(boolean))method
- Heads-up notifications remain if an app[updates the notification](https://developer.android.com/training/notify-user/build-notification#Updating)within the eight-second time window.

When a heads-up notification is dismissed, the notification is listed in the Notification Center, unless it is a[`CATEGORY_NAVIGATION`](https://developer.android.com/reference/android/app/Notification#CATEGORY_NAVIGATION)notification.

## Notification API changes and restrictions for cars

This section summarizes the differences for each class where the Notifications API behaves differently or has restrictions for Android Automotive OS.

### Notification.Builder

Tables 1 and 2 describe the API changes and restrictions in the[`Notification.Builder`](https://developer.android.com/reference/android/app/Notification.Builder)class.

**Table 1** . Changes to public methods for`Notification.Builder`

|                                                                                 Public methods                                                                                  |       Effect        |                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `addAction()`                                                                                                                                                                   | Conditional no-op   | `Notification.MessagingStyle`notifications must add the actions specified in the[compatibility requirements](https://developer.android.com/training/cars/platforms/automotive-os/notifications#messaging-requirements). Any additional actions that are added won't be rendered as Notification buttons.                                                                                                                                                                                               |
| `createBigContentView()` `createContentView()` `createHeadsUpContentView()` `setContent()` `setCustomBigContentView()` `setCustomContentView()` `setCustomHeadsUpContentView()` | No-op               | [`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews)and custom content views are not supported.                                                                                                                                                                                                                                                                                                                                                                         |
| `setBadgeIconType()` `setNumber()`                                                                                                                                              | No-op               | Notification badges are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `setChronometerCountDown()` `setUsesChronometer()`                                                                                                                              | No-op               | Countdown timers are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `setColorized()`                                                                                                                                                                | Constraints changed | **Platform-signed apps**: configurable; allowed by default. **System-privileged apps**: configured by platform; disallowed by default. **All other apps**: configured by platform; disallowed by default.                                                                                                                                                                                                                                                                                              |
| `setFullScreenIntent()`                                                                                                                                                         | Behavior changed    | Does not auto-launch the intent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `setLargeIcon()`                                                                                                                                                                | Behavior changed    | Large icons are shown on the righthand side of the notification.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `setLights()`                                                                                                                                                                   | No-op               | Android Automotive OS devices don't have LED indicator lights.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `setOngoing()`                                                                                                                                                                  | Behavior changed    | Behavior is different when the notification also triggers a heads-up notification. `setOngoing()`only makes the heads-up notification undismissable if the heads-up notification is for an incoming call. To qualify as an undismissable heads-up notification for an incoming call, a notification must fulfill[the defined requirements](https://developer.android.com/training/cars/platforms/automotive-os/notifications#hun-life). Drivers can dismiss all other types of heads-up notifications. |
| `setPublicVersion()` `setVisibility()`                                                                                                                                          | No-op               | Private mode is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `setSettingsText()`                                                                                                                                                             | No-op               | Notifications don't support affordances that link to app settings. Drivers access app settings through the app instead.                                                                                                                                                                                                                                                                                                                                                                                |
| `setTicker()`                                                                                                                                                                   | No-op               | Ticker text is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Table 2** . Changes to nested classes for`Notification.Builder`

|                                    Nested classes                                    |      Effect      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Notification.BigPictureStyle` `Notification.BigTextStyle` `Notification.InboxStyle` | Not used         | Only summary text shows. Detailed notifications for these styles are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Notification.BubbleMetadata`                                                        | Not used         | Bubbles are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Notification.MediaStyle`                                                            | Hidden           | Notifications with this style are hidden. Android Automotive OS manages user interface interactions for media notifications and playback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Notification.MessagingStyle`                                                        | Behavior changed | Notifications with this style have the following differences: - Notifications only show the last message from a conversation when using[`addMessage()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle#addMessage(androidx.core.app.NotificationCompat.MessagingStyle.Message)). Only unread messages are included, as specified in the[compatibility requirements](https://developer.android.com/training/cars/platforms/automotive-os/notifications#messaging-requirements). - Android Automotive OS automatically adds[Play and Mute buttons](https://developer.android.com/training/cars/platforms/automotive-os/notifications#play-mute-buttons)to[car-compatible messaging notifications](https://developer.android.com/training/cars/platforms/automotive-os/notifications#messaging-requirements). - Notifications must add the actions specified in the[compatibility requirements](https://developer.android.com/training/cars/platforms/automotive-os/notifications#messaging-requirements). Any additional actions that are added are not rendered as Notification buttons. |
| `Notification.CarExtender` `Notification.WearableExtender`                           | Not used         | Extenders are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Notification.Action.Builder

Table 3 describes the API changes and restrictions in the[`Notification.Action.Builder`](https://developer.android.com/reference/android/app/Notification.Action.Builder)class.

**Table 3** . Changes to public methods for`Notification.Action.Builder`

|       Public methods       |      Effect      |                                                                          Description                                                                          |
|----------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Public constructors        | Behavior changed | Icons specified in public constructors are ignored.                                                                                                           |
| `addRemoteInput`           | Behavior changed | To minimize driver distraction, a digital assistant, such as the Google Assistant, inserts the response to a message for the user. Users can't type messages. |
| `setAllowGeneratedReplies` | No-op            | Smart Reply is not supported.                                                                                                                                 |