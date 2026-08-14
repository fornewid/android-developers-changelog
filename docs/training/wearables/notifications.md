---
title: https://developer.android.com/training/wearables/notifications
url: https://developer.android.com/training/wearables/notifications
source: md.txt
---

Notifications on watches use the same APIs and have the same structure as notifications on phones.


Notifications can appear on a watch in two ways:

1. A mobile app creates a notification and the system [automatically bridges](https://developer.android.com/training/wearables/notifications/bridger) that notification to the watch.
2. A wearable app creates a notification.


For both scenarios, use the
`https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder`
class to create notifications. When you build notifications with the builder class, the system
takes care of displaying notifications properly. For example, when you issue a notification from
your mobile app, each notification appears as a card on the Notification Stream.


Review the following example to see how notifications display.
![notification-cards](https://developer.android.com/static/images/ui/notifications/wear_2x.png)

**Figure 1.** The same notification displayed on a phone and on a watch.


Use one of the
`https://developer.android.com/reference/androidx/core/app/NotificationCompat.Style`
subclasses for the best results.

**Note:**
Using `https://developer.android.com/reference/android/widget/RemoteViews`
strips notifications of custom layouts, and the wearable only displays the text and icons.

## Recommended notifications for wearables


Use expandable notifications as the starting point for all notifications, as they are
a great way to engage wearable users. The collapsed state displays in the notification
tray for a short, glanceable experience. If the user taps it, the notification expands,
revealing an immersive, scrollable experience of additional content and actions.


You can [Create an expandable notification](https://developer.android.com/training/notify-user/expanded)
the same way you would on mobile, using any of the `NotificationCompat.Style`
subclasses. For example, a standard notification using
`https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle`
looks like this:
![expandable-notification](https://developer.android.com/static/images/ui/notifications/expandable_noti.png)

**Figure 2.** Example of a `MessagingStyle` notification on Wear OS.


You can see the notification has multiple
[actions](https://developer.android.com/develop/ui/views/notifications/build-notification#Actions) stacked at the bottom of the
expanded state.


**Tip:** If your notifications include a "reply" action, such as for a messaging
app, you can enhance the behavior of the notification. For example, you can enable voice input
replies directly from the wearable or pre-defined text responses with
`https://developer.android.com/reference/androidx/core/app/RemoteInput.Builder#setChoices(java.lang.CharSequence[])`.
For more information, read
[Add the reply button](https://developer.android.com/training/notify-user/build-notification#add-reply-action).

## Avoid duplicate Notifications


By default, notifications are bridged from a companion phone app to any paired watches. This is a
great option if you don't have a wearable app installed.


However, if you build a standalone watch app and a companion phone app, the apps
create duplicate notifications.


Wear OS provides a way to stop duplicate notifications with the Bridging APIs. This is
particularly important for apps on devices that run Wear OS 5 or higher, because some
notifications that are dismissible on a mobile device aren't dismissible on the Wear OS device.
For more information, read
[Bridging options for notifications](https://developer.android.com/training/wearables/notifications/bridger).

## Add wearable-specific features to a notification


If you need to add wearable-specific features to a notification, you can use the
[`NotificationCompat.WearableExtender`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.WearableExtender) class to specify the options.
To use this API, do the following:

**Note:**
If you use the framework's `https://developer.android.com/reference/android/app/NotificationManager`,
some features from
`NotificationCompat.WearableExtender` don't work, so make sure to use
[`NotificationCompat`](https://developer.android.com/reference/androidx/core/app/NotificationCompat).


This example shows how to set a Wear-specific action on the notification and also set the
[dismissal ID](https://developer.android.com/reference/androidx/core/app/NotificationCompat.WearableExtender#setDismissalId(java.lang.String)). When the notification is dismissed, all other notifications with the same
dismissal ID are dismissed on the watch and on the companion phone. To retrieve a dismissal ID,
use [`getDismissalId()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.WearableExtender#getDismissalId()).

```kotlin
// This intent will be fired as a result of the user clicking the "Open on watch" action.
// However, it executes on the phone, not on the watch. Typically, the Activity should then use
// RemoteActivityHelper to then launch the correct activity on the watch.
val intent = Intent(context, LaunchOnWearActivity::class.java)
val wearPendingIntent = PendingIntent.getActivity(
    context,
    wearRequestCode,
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
)

val openOnWatchAction = NotificationCompat.Action.Builder(
    R.drawable.watch,
    "Open on watch",
    wearPendingIntent
)
    .build()

val wearableExtender = NotificationCompat.WearableExtender()
    // This action will only be shown on the watch, not on the phone.
    // Actions added to the Notification builder directly will not be shown on the watch,
    // because one or more actions are defined in the WearableExtender.
    .addAction(openOnWatchAction)
    // This synchronizes dismissals between watch and phone.
    .setDismissalId(chatId)

val notification = NotificationCompat.Builder(context, channelId)
    // ... set other fields ...
    .extend(wearableExtender)
    .build()
```

## Launch your phone app from a wearable device


If you are using bridged notifications, any notification automatically includes a button to launch
the app on the phone. However, if you are using a local notification, created on the watch, use
the following steps to create a button that launches the app on the phone:

1. Create a new `Activity` that extends [`ConfirmationActivity`](https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity).
2. Use [`RemoteActivityHelper`](https://developer.android.com/reference/androidx/wear/remote/interactions/RemoteActivityHelper) in the new `Activity` to launch the phone app.
3. When building the `Intent` to launch the `Activity` from the notification, set the [`EXTRA_ANIMATION_TYPE`](https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#EXTRA_ANIMATION_TYPE()) extra to [`OPEN_ON_PHONE_ANIMATION`](https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#OPEN_ON_PHONE_ANIMATION()).

This approach guides the user to interacting on their phone and follows the platform requirements for launching background processes.

<br />


**Note:** You can't use a `BroadcastReceiver` as the target
of the notification action.