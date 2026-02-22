---
title: https://developer.android.com/training/wearables/notifications/bridger
url: https://developer.android.com/training/wearables/notifications/bridger
source: md.txt
---

By default, notifications are bridged, or shared, from an app on a phone to any paired watches. If
you build a watch app and your app also exists on a paired phone, users might receive duplicate
notifications---one generated and bridged by the phone app and one generated
by the watch app. Wear OS includes features to control how and when
notifications are bridged.

## Avoid duplicate notifications


When you create notifications from an external source, such as from
[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/), your
mobile app and your wearable app can each display its own notifications on the watch. To avoid
this sort of duplication, programmatically disable bridging in your wearable app.

### Use bridge tags


If you want to bridge some of the notifications created on your mobile app to the watch
when your wearable app is installed, set bridge tags.


Set a bridge tag on a notification by using the
`https://developer.android.com/reference/androidx/core/app/NotificationCompat.WearableExtender#setBridgeTag(java.lang.String)`
method, as shown in the following code sample:

```kotlin
val notification = NotificationCompat.Builder(context, channelId)
    // ... set other fields ...
    .extend(
        NotificationCompat.WearableExtender()
            .setBridgeTag("tagOne")
    )
    .build()
```

### Disable bridging

You can disable bridging for some notifications or for all notifications.
We recommend that you selectively disable bridging.

#### Disable bridging for *some* notifications


You can dynamically disable bridging and, optionally, permit some notifications
through based on their tag. For example, to disable bridging for all notifications except those tagged as
`tagOne`, `tagTwo`, or `tagThree`, use the
`https://developer.android.com/reference/androidx/wear/phone/interactions/notifications/BridgingConfig`
object as shown in the following example:

```kotlin
// In this example, bridging is only enabled for tagOne, tagTwo and tagThree.
BridgingManager.fromContext(context).setConfig(
    BridgingConfig.Builder(context, isBridgingEnabled = false)
        .addExcludedTags(listOf("tagOne", "tagTwo", "tagThree"))
        .build()
)
```

#### Disable bridging for *all* notifications (not recommended)


**Note:** Disabling bridging for all notifications is not recommended, because
the bridging configuration set in the manifest takes effect as soon as a watch app is installed.
This can lead to notifications being lost if the user needs to open and set up the watch app
before receiving notifications.


To prevent bridging of all notifications from a
phone app, use the `<meta-data>` entry in the manifest file of the watch app, as shown in the following example:

```xml
<!-- Beware, this can have unintended consequences before the user is signed-in -->
<meta-data
    android:name="com.google.android.wearable.notificationBridgeMode"
    android:value="NO_BRIDGING" />
```


**Note:** Specifying a bridging configuration at runtime overrides a bridging-related
setting in the Android manifest file.

### Set a dismissal ID to sync similar notifications


When you prevent bridging with the bridging mode feature, dismissals of notifications are not
synced across a user's devices.


However, if similar notifications are created on both the mobile device and the watch, you want both
notifications to be dismissed when the user dismisses either one of them.


In the
`https://developer.android.com/reference/androidx/core/app/NotificationCompat.WearableExtender`,
you can set a global unique ID so that when a notification dismisses, other notifications
with the same ID on paired watches are also dismissed.


The
`NotificationCompat.WearableExtender`
class has methods that let you use dismissal IDs, as shown in the following example:


When the notification dismisses, all other notifications with the same dismissal ID are
dismissed on the watch and on the phone. To retrieve a dismissal ID, use
`getDismissalId()`


In the following example, a globally unique ID is
specified for a new notification, so dismissals are synced:

```kotlin
val notification = NotificationCompat.Builder(context, channelId)
    // ... set other fields ...
    .extend(
        NotificationCompat.WearableExtender()
            .setDismissalId("abc123")
    )
    .build()
```


**Note:** Dismissal IDs work if a watch is paired to an Android phone, but not if a watch is
paired to an iPhone.

## When notifications aren't bridged


The following types of notifications are not bridged:

- Local-only notifications set using `https://developer.android.com/reference/android/app/Notification.Builder#setLocalOnly(boolean)`.
- Ongoing notifications set using `https://developer.android.com/reference/android/app/Notification.Builder#setOngoing(boolean)` or `https://developer.android.com/reference/android/app/Notification#FLAG_ONGOING_EVENT`.
- Non-clearable notifications set using `https://developer.android.com/reference/android/app/Notification#FLAG_NO_CLEAR`.
- Notifications where the counterpart wearable app has disabled notification bridging, as described previously.

## Best practices for bridged notifications


It takes time to push or remove bridged notifications from a wearable
device. As you design your notifications, make sure to avoid unexpected
behavior caused by this latency. The following guidelines help
ensure that your bridged notifications work with asynchronous notifications:

- If you cancel a notification on the phone, it may take some time to cancel the corresponding notification on the watch. During this time, the user might send one of the pending intents on that notification. For this reason, continue to receive pending intents in your app from notifications it has canceled: when canceling notifications, keep those notifications' pending intent receivers valid.
- Don't cancel and retrigger an entire stack of notifications at one time. Only modify or remove the notifications that have actually been modified. This avoids the latency on updating the wearable device and reduces your app's impact on battery life.

### Design considerations


Wear OS notifications have their own design guidelines. For more information,
review the [Wear OS Design Guidelines](https://developer.android.com/training/wearables/design).