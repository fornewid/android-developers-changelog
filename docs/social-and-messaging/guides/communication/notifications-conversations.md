---
title: https://developer.android.com/social-and-messaging/guides/communication/notifications-conversations
url: https://developer.android.com/social-and-messaging/guides/communication/notifications-conversations
source: md.txt
---

# About notifications and conversations

[Notifications](https://developer.android.com/develop/ui/views/notifications)provide timely, relevant updates from your app to the user that appear in places such as the status bar, notification drawer, and the lock screen. They inform users about relevant messages, updates, or events within your app --- particularly while your app isn't running in the foreground.

[Conversations](https://developer.android.com/develop/ui/views/notifications/conversations)are notifications for real-time messaging with people that get a dedicated prioritized section in the notification drawer. Conversations support[bubbles](https://developer.android.com/develop/ui/views/notifications/bubbles)and[share targets](https://developer.android.com/training/sharing/direct-share-targets). They make your messaging app feel well-integrated into the Android experience, enhance user engagement, and keep your app top of mind.

### Know key Android notification concepts

Using notifications effectively and correctly gives your app a great way to re-engage your users, but there is a lot to know. Here are some of the basics:

- [**Notification Runtime Permission**](https://developer.android.com/develop/ui/views/notifications/notification-permission)(**POST_NOTIFICATIONS** ): Starting in Android 13 (API level 33) and later, apps must request the[POST_NOTIFICATIONS](https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS)permission to send notifications, giving users direct control over which apps can send them notifications.
- [**Notification Channels**](https://developer.android.com/develop/ui/views/notifications/channels): Apps are required to use channels to post notifications, and channels have unique IDs and user-visible names. Users can fine-tune notification settings per channel, so you should categorize your notifications by type or priority in ways that users can understand (e.g., messages, alerts, updates).
- [**Notification Groups**](https://developer.android.com/develop/ui/views/notifications/group): Groups visually organize related notifications, and allow users to manage them as a unit.
- [**Notification Badge**](https://developer.android.com/develop/ui/views/notifications/badges): This small dot or number on an app's icon (depending on launcher support) indicates unread notifications. (You can choose to have your app provide a custom number instead).
- [**MessagingStyle**](https://developer.android.com/reference/android/app/Notification.MessagingStyle): A notification style that is used to represent conversations between different people or groups of people. Your notifications must be created with this style to use Android's[conversation features](https://developer.android.com/develop/ui/views/notifications/conversations).
- [**Notification Actions**](https://developer.android.com/develop/ui/views/notifications#Actions): Buttons at the bottom of a notification that perform an action on the data the notification represents, such as "Archive" or "Reply." Notifications can even allow users to directly type replies.

See[Notifications overview](https://developer.android.com/develop/ui/views/notifications)to learn about the basics of Android Notifications. See[Best practices for messaging apps](https://developer.android.com/develop/ui/views/notifications/build-notification#messaging-best-practices)for a more detailed overview of bringing your messaging app to the most Android surfaces. See[People and conversations](https://developer.android.com/develop/ui/views/notifications/conversations)to learn more about notifications and conversations best practices and fundamental tools.

### Level up your app

To help your messaging app meet and surpass user expectations and make your app feel fully integrated with Android, you'll want to take full advantage of the notification features Android has to offer:

- Support[conversation notifications](https://developer.android.com/develop/ui/views/notifications/conversations#api-notifications)with[long-lived shortcuts](https://developer.android.com/develop/ui/views/notifications/conversations#api-shortcuts)so users can add people and group shortcuts to their homescreens via widgets.
- Support[notification badges](https://developer.android.com/develop/ui/views/notifications/badges)in the launcher.
- Support[direct replies](https://developer.android.com/develop/ui/views/notifications/build-notification#direct-reply)so that users can respond to messages from within their notifications.
- Enable[smart replies](https://developer.android.com/develop/ui/views/notifications/build-notification#smart-reply)for wearable devices to make it easier for users to communicate from their wrist.
- Support[bubbles for conversations](https://developer.android.com/develop/ui/views/notifications/bubbles), so that people can keep conversations going easily while engaged with other tasks on their device.

The[full guide](https://developer.android.com/social-and-messaging/guides/communication/basic-better-best)has even more notification-related features to consider to take your social and messaging experience to the next level.