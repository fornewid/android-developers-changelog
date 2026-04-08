---
title: Bridging options for notifications  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/notifications/bridger
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Bridging options for notifications Stay organized with collections Save and categorize content based on your preferences.



By default, the system *bridges*, or shares, notifications from a phone app to
any paired watches. If you build a watch app and your app also exists on a
paired phone, users might receive duplicate notifications—one that the phone app
generates and bridges, and one that the watch app generates. Wear OS includes
features to control how and when notifications are bridged.

## Avoid duplicate notifications

When you create notifications from an external source, such as from [Firebase
Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/), your phone app and your watch app can each display its own
notifications on the watch. To avoid duplication, programmatically disable
bridging in your watch app.

### Use bridge tags

To bridge some of the notifications that your phone app creates to the watch
when your watch app is installed, set bridge tags.

Set a bridge tag on a notification by using the
[`setBridgeTag(String)`](/reference/androidx/core/app/NotificationCompat.WearableExtender#setBridgeTag(java.lang.String))
method, as shown in the following code sample:

```
val notification = NotificationCompat.Builder(context, channelId)
    // ... set other fields ...
    .extend(
        NotificationCompat.WearableExtender()
            .setBridgeTag("tagOne")
    )
    .build()

BridgingConfiguration.kt
```

### Disable bridging

You can disable bridging for some notifications or for all notifications. We
recommend that you selectively disable bridging.

#### Disable bridging for only some notifications

You can dynamically disable bridging and, optionally, permit some notifications
through based on their tag. For example, to disable bridging for all
notifications except those tagged as `tagOne`, `tagTwo`, or `tagThree`, use the
[`BridgingConfig`](/reference/androidx/wear/phone/interactions/notifications/BridgingConfig)
object as shown in the following example:

```
// In this example, bridging is only enabled for tagOne, tagTwo and tagThree.
BridgingManager.fromContext(context).setConfig(
    BridgingConfig.Builder(context, isBridgingEnabled = false)
        .addExcludedTags(listOf("tagOne", "tagTwo", "tagThree"))
        .build()
)

BridgingConfiguration.kt
```

#### Disable bridging for all notifications (not recommended)

**Note:** We don't recommend disabling bridging for all notifications, because the
bridging configuration set in the manifest takes effect as soon as a watch app
is installed. This can lead to notifications being lost if the user needs to
open and set up the watch app before receiving notifications.

To prevent bridging of all notifications from a phone app, use the
`<meta-data>` entry in the manifest file of the watch app, as shown in the
following example:

```
<!-- Beware, this can have unintended consequences before the user is signed-in -->
<meta-data
    android:name="com.google.android.wearable.notificationBridgeMode"
    android:value="NO_BRIDGING" />

AndroidManifest.xml
```

**Note:** Specifying a bridging configuration at runtime overrides a
bridging-related setting in the Android manifest file.

### Set a dismissal ID to sync similar notifications

When you prevent bridging with the bridging mode feature, dismissals of
notifications are not synced across a user's devices.

However, if similar notifications are created on both the phone and the
watch, you want both notifications to be dismissed when the user dismisses
either one of them.

In the
[`NotificationCompat.WearableExtender`](/reference/androidx/core/app/NotificationCompat.WearableExtender),
you can set a global unique ID so that when a user dismisses a notification,
other notifications with the same ID on paired watches are also dismissed.

The `NotificationCompat.WearableExtender` class has methods that let you use
dismissal IDs, as shown in the following example:

When the user dismisses the notification, all other notifications with the same
dismissal ID are dismissed on the watch and on the phone. To retrieve a
dismissal ID, use `getDismissalId()`.

In the following example, a globally unique ID is specified for a new
notification, so dismissals are synced:

```
val notification = NotificationCompat.Builder(context, channelId)
    // ... set other fields ...
    .extend(
        NotificationCompat.WearableExtender()
            .setDismissalId("abc123")
    )
    .build()

BridgingConfiguration.kt
```

**Note:** Dismissal IDs work if a watch is paired to an Android phone, but not if a
watch is paired to an iPhone.

## Local-only notifications

To prevent duplicate notifications, you can also use [`setLocalOnly()`](/reference/android/app/Notification.Builder#setLocalOnly(boolean)) to
make notifications local to the phone.

However, use this method only if the notification must appear *only* on the
device that created it. This includes not only Wear OS devices, but other
wearables and any other connected devices. A local-only notification does not
bridge, even if your app is not installed on the watch.

When building a Wear OS and phone app that both create notifications, don't use
this approach to avoid duplicate notifications. Instead, use the bridging
options.

For example, use a local-only notification when a user downloads a file on a
phone and the notification indicates that the download is complete.

## When notifications aren't bridged

The system doesn't bridge the following types of notifications:

* Local-only notifications set using
  [`Notification.Builder.setLocalOnly(boolean)`](/reference/android/app/Notification.Builder#setLocalOnly(boolean)).
* Ongoing notifications set using
  [`Notification.Builder.setOngoing(boolean)`](/reference/android/app/Notification.Builder#setOngoing(boolean))
  or [`Notification.FLAG_ONGOING_EVENT`](/reference/android/app/Notification#FLAG_ONGOING_EVENT).
* Non-clearable notifications set using
  [`Notification.FLAG_NO_CLEAR`](/reference/android/app/Notification#FLAG_NO_CLEAR).
* Notifications where the counterpart wearable app has [disabled notification
  bridging](#disable-bridging).

## Implementation considerations for bridged notifications

It takes time to push or remove bridged notifications from a wearable device. As
you design your notifications, avoid unexpected behavior caused by
this latency. The following guidelines help ensure that your bridged
notifications work with asynchronous notifications:

* If you cancel a notification on the phone, it might take some time to cancel
  the corresponding notification on the watch. During this time, the user
  might send one of the pending intents on that notification. For this reason,
  continue to receive pending intents in your app from notifications it has
  canceled: when canceling notifications, keep those notifications' pending
  intent receivers valid.
* Don't cancel and retrigger an entire stack of notifications at one time.
  Only modify or remove the notifications that have actually been modified.
  This avoids the latency on updating the wearable device and reduces your
  app's impact on battery life.

### Design considerations

Wear OS notifications have their own design guidelines. For more information,
see the [Wear OS Design Guidelines](/training/wearables/design).