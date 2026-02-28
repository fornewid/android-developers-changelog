---
title: https://developer.android.com/develop/ui/views/notifications/bubbles
url: https://developer.android.com/develop/ui/views/notifications/bubbles
source: md.txt
---

Bubbles make it easier for users to see and participate in conversations.
**Figure 1.** A chat bubble.

Bubbles are built into the notification system. They float on top of other app
content and follow the user wherever they go. Users can expand bubbles to reveal
and interact with the app content, and they can collapse them when they're not
using them.

When the device is locked, or the always-on-display is active, bubbles appear as
notifications normally do.

Bubbles are an opt-out feature. When an app presents its first bubble, a
permission dialog offers two choices:

- Block all bubbles from your app. Notifications aren't blocked, but they never appear as bubbles.
- Allow all bubbles from your app. All notifications sent with `BubbleMetaData` appear as bubbles.

## The notification Bubble API

Bubbles are created using the notification API, so send your notification as
normal. If you want your notification to display as a bubble, attach extra data
to it.

The expanded view of a bubble is created from an activity that you choose.
Configure the activity to display properly as a bubble. The activity must be
[resizeable](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity) and
[embedded](https://developer.android.com/guide/topics/manifest/activity-element#embedded). If it lacks
either of these requirements, it displays as a notification instead.

The following code demonstrates how to implement a bubble:

    <activity
      android:name=".bubbles.BubbleActivity"
      android:theme="@style/AppTheme.NoActionBar"
      android:label="@string/title_activity_bubble"
      android:allowEmbedded="true"
      android:resizeableActivity="true"
    />

If your app shows multiple bubbles of the same type, like multiple chat
conversations with different contacts, the activity must be able to launch
multiple instances. On devices running Android 10 and lower,
notifications aren't shown as bubbles unless you explicitly set
[`documentLaunchMode`](https://developer.android.com/guide/topics/manifest/activity-element#dlmode) to
`"always"`. Beginning with Android 11, you don't need to explicitly
set this value, as the system automatically sets all conversations'
`documentLaunchMode` to `"always"`.

To send a bubble, follow these steps:

1. [Create a notification](https://developer.android.com/training/notify-user/build-notification) as you normally do.
2. Call [`BubbleMetadata.Builder(PendingIntent,
   Icon)`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#Builder(android.app.PendingIntent,%20android.graphics.drawable.Icon)) or [`BubbleMetadata.Builder(String)`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#Builder(java.lang.String)) to create a `BubbleMetadata` object.
3. Use [`setBubbleMetadata()`](https://developer.android.com/reference/android/app/Notification.Builder#setBubbleMetadata(android.app.Notification.BubbleMetadata)) to add the metadata to the notification.
4. If targeting Android 11 or higher, make sure the bubble metadata or notification references a sharing shortcut.
5. Modify your app to **not** cancel notifications that appear as bubbles. To check if the notification activity is launched as a bubble, call [`Activity#isLaunchedFromBubble()`](https://developer.android.com/reference/android/app/Activity#isLaunchedFromBubble()). Canceling a notification removes the bubble from the screen. Opening a bubble automatically hides the notification associated with it.

These steps are shown in the following example:

### Kotlin

```kotlin
// Create a bubble intent.
val target = Intent(context, BubbleActivity::class.java)
val bubbleIntent = PendingIntent.getActivity(context, 0, target, 0 /* flags */)
val category = "com.example.category.IMG_SHARE_TARGET"

val chatPartner = Person.Builder()
    .setName("Chat partner")
    .setImportant(true)
    .build()

// Create a sharing shortcut.
val shortcutId = generateShortcutId()
val shortcut =
   ShortcutInfo.Builder(mContext, shortcutId)
       .setCategories(setOf(category))
       .setIntent(Intent(Intent.ACTION_DEFAULT))
       .setLongLived(true)
       .setShortLabel(chatPartner.name)
       .build()

// Create a bubble metadata.
val bubbleData = Notification.BubbleMetadata.Builder(bubbleIntent,
            Icon.createWithResource(context, R.drawable.icon))
    .setDesiredHeight(600)
    .build()

// Create a notification, referencing the sharing shortcut.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setBubbleMetadata(bubbleData)
    .setShortcutId(shortcutId)
    .addPerson(chatPartner)
```

### Java

```java
// Create a bubble intent.
Intent target = new Intent(mContext, BubbleActivity.class);
PendingIntent bubbleIntent =
    PendingIntent.getActivity(mContext, 0, target, 0 /* flags */);

private val CATEGORY_TEXT_SHARE_TARGET =
    "com.example.category.IMG_SHARE_TARGET"

Person chatPartner = new Person.Builder()
        .setName("Chat partner")
        .setImportant(true)
        .build();

// Create a sharing shortcut.
private String shortcutId = generateShortcutId();
ShortcutInfo shortcut =
   new ShortcutInfo.Builder(mContext, shortcutId)
       .setCategories(Collections.singleton(CATEGORY_TEXT_SHARE_TARGET))
       .setIntent(Intent(Intent.ACTION_DEFAULT))
       .setLongLived(true)
       .setShortLabel(chatPartner.getName())
       .build();

// Create a bubble metadata.
Notification.BubbleMetadata bubbleData =
    new Notification.BubbleMetadata.Builder(bubbleIntent,
            Icon.createWithResource(context, R.drawable.icon))
        .setDesiredHeight(600)
        .build();

// Create a notification, referencing the sharing shortcut.
Notification.Builder builder =
    new Notification.Builder(mContext, CHANNEL_ID)
        .setContentIntent(contentIntent)
        .setSmallIcon(smallIcon)
        .setBubbleMetadata(bubbleData)
        .setShortcutId(shortcutId)
        .addPerson(chatPartner);
```

> [!NOTE]
> **Note:** The first time you send the notification to display a bubble, make sure it's in a notification channel with [`IMPORTANCE_MIN`](https://developer.android.com/reference/android/app/NotificationManager#IMPORTANCE_MIN) or higher.

If your app is in the foreground when a bubble is sent, importance is ignored
and your bubble is always shown, unless the user blocks bubbles or notifications
from your app.

### Create an expanded bubble

You can configure your bubble to present it in expanded state automatically. We
recommend only using this feature if the user performs an action that
results in a bubble, like tapping a button to start a new chat. In this case,
it also makes sense to suppress the initial notification sent when a bubble is
created.

There are methods you can use to set flags that enable these behaviors:
[`setAutoExpandBubble()`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#setAutoExpandBubble(boolean))
and
[`setSuppressNotification()`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#setSuppressNotification(boolean)).

The following example shows how to configure a bubble to automatically present
in an expanded state:

### Kotlin

```kotlin
val bubbleMetadata = Notification.BubbleMetadata.Builder()
    .setDesiredHeight(600)
    .setIntent(bubbleIntent)
    .setAutoExpandBubble(true)
    .setSuppressNotification(true)
    .build()
```

### Java

```java
Notification.BubbleMetadata bubbleData =
    new Notification.BubbleMetadata.Builder()
        .setDesiredHeight(600)
        .setIntent(bubbleIntent)
        .setAutoExpandBubble(true)
        .setSuppressNotification(true)
        .build();
```

### Bubble content lifecycle

When a bubble is expanded, the content activity goes through the normal [process
lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle), resulting in the
application becoming a foreground process, if it isn't already.

When the bubble is collapsed or dismissed, the activity is destroyed. This might
result in the process being cached and later killed, depending on whether the
app has other foreground components running.

## When bubbles appear

To reduce interruptions for the user, bubbles only appear under certain
circumstances.

If an app targets Android 11 or higher, a notification doesn't
appear as a bubble unless it meets the [conversation
requirements](https://developer.android.com/guide/topics/ui/conversations). If an app targets
Android 10 or lower, the notification appears as a bubble only if
one or more of the following conditions are met:

- The notification uses [`MessagingStyle`](https://developer.android.com/reference/android/app/Notification.MessagingStyle) and has a [`Person`](https://developer.android.com/reference/android/app/Person) added.
- The notification is from a call to [`Service.startForeground`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification)), has a [`category`](https://developer.android.com/reference/android/app/Notification.Builder#setCategory(java.lang.String)) of [`CATEGORY_CALL`](https://developer.android.com/reference/android/app/Notification#CATEGORY_CALL), and has a `Person` added.
- The app is in the foreground when the notification is sent.

If none of these conditions are met, the notification is shown instead of a
bubble.

> [!NOTE]
> **Note:** Android 10 doesn't support Bubbles out-of-the-box. To see them appearing, you will need to enable [Developer Options](https://developer.android.com/studio/debug/dev-options), search for "bubbles" in the Settings menu, and enable the Bubbles settings.

## Launching activities from bubbles

When a bubble launches a new activity, the new activity will either launch
within the same task and the same bubbled window, or in a new task
in fullscreen, collapsing the bubble that launched it.

To launch a new activity in the same task as the bubble:
1. Use the activity context when launching intents,
`activity.startActivity(intent)`, and
1. Don't set the `FLAG_ACTIVITY_NEW_TASK` flag on the intent.

Otherwise, the new activity is started in a new task and the bubble is
collapsed.

Keep in mind that a bubble represents a specific conversation, so activities
launched within the bubble should be related to that conversation. Additionally,
launching an activity within the bubble increases the task stack of the bubble
and could potentially complicate the user experience, specifically around
navigation.

## Best practices

- Send a notification as a bubble only if it is important, such as when it is part of an ongoing communication or if the user explicitly requests a bubble for content. Bubbles use screen real estate and cover other app content.
- Make sure your bubble notification also works as a normal notification. When the user disables the bubble, a bubble notification is shown as a normal notification.
- Call `super.onBackPressed` when overriding [`onBackPressed`](https://developer.android.com/reference/android/app/Activity#onBackPressed()) in the bubble activity. Otherwise, your bubble might not behave correctly.

When a collapsed bubble receives an updated message, the bubble shows a badge
icon to indicate an unread message. When the user opens the message in the
associated app, follow these steps:

- [Update](https://developer.android.com/training/notify-user/build-notification#Updating) the `BubbleMetadata` to suppress the notification. Call [`BubbleMetadata.Builder.setSuppressNotification()`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#setSuppressNotification(boolean)). This removes the badge icon to indicate that the user interacted with the message.
- Set [`Notification.Builder.setOnlyAlertOnce()`](https://developer.android.com/reference/android/app/Notification.Builder#setOnlyAlertOnce(boolean)) to `true` to suppress the sound or vibration that accompanies the `BubbleMetadata` update.

## Sample app

The
[SociaLite](https://github.com/android/socialite)
sample app is a conversation app that uses bubbles. For demonstration purposes,
this app uses chatbots. In real-world applications, use bubbles for messages by
humans.