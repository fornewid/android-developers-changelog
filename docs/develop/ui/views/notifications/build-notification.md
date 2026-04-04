---
title: https://developer.android.com/develop/ui/views/notifications/build-notification
url: https://developer.android.com/develop/ui/views/notifications/build-notification
source: md.txt
---

Notifications provide short, timely information about events in your app while
it isn't in use. This document shows you how to create a notification with
various features. For an introduction to how notifications appear on Android,
see the [Notifications overview](https://developer.android.com/guide/topics/ui/notifiers/notifications). For sample code that uses notifications,
see the [SociaLite sample](https://github.com/android/socialite) on GitHub.

The code in this page uses the [`NotificationCompat`](https://developer.android.com/reference/androidx/core/app/NotificationCompat) APIs from the AndroidX
Library. These APIs let you add features available only on newer versions of
Android while still providing compatibility back to Android 9 (API level 28).
However, some features, such as the inline reply action, result in a no-op on
earlier versions.

## Create a basic notification

A notification in its most basic and compact form---also known as *collapsed
form*---displays an icon, a title, and a small amount of text content. This
section shows how to create a notification that the user can tap to launch an
activity in your app.

![](https://developer.android.com/static/images/ui/notifications/notification-basic_2x.png)

**Figure 1.** A notification with
an icon, a title, and some text.

<br />

For more details about each part of a notification, read about [notification
anatomy](https://developer.android.com/guide/topics/ui/notifiers/notifications#Templates).

### Declare the runtime permission

Android 13 (API level 33) and higher supports a runtime permission for posting
non-exempt (including Foreground Services (FGS)) notifications from an app.

The permission that you need to declare in your app's manifest file appears in
the following code snippet:

```xml
<manifest ...>
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
    <application ...>
        ...
    </application>
</manifest>
```

For more details about runtime permissions, see
[Notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission).

### Set the notification content

To get started, set the notification's content and channel using a
[`NotificationCompat.Builder`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder) object. The following example shows how to
create a notification with the following:

- A small icon, set by [`setSmallIcon()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setSmallIcon(int)). This is the only user-visible
  content that's required.

- A title, set by [`setContentTitle()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentTitle(java.lang.CharSequence)).

- The body text, set by [`setContentText()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentText(java.lang.CharSequence)).

- The notification priority, set by [`setPriority()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setPriority(int)). The priority
  determines how intrusive the notification is on Android 7.1 and earlier. For
  Android 8.0 and later, instead set the channel importance as shown in the
  next section.

### Kotlin

    var builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle(textTitle)
            .setContentText(textContent)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

### Java

    NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle(textTitle)
            .setContentText(textContent)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT);

The `NotificationCompat.Builder` constructor requires you to provide a channel
ID. This is required for compatibility with Android 8.0 (API level 26) and
later, but is ignored by earlier versions.

By default, the notification's text content is truncated to fit one line. You
can show additional information by creating an expandable notification.

![](https://developer.android.com/static/images/ui/notifications/notification-expanded_2x.png)

**Figure 2.** An expandable
notification in its collapsed and expanded forms.

<br />

If you want your notification to be longer, you can enable an expandable
notification by adding a style template with [`setStyle()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setStyle(androidx.core.app.NotificationCompat.Style)). For example,
the following code creates a larger text area:

### Kotlin

    var builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Much longer text that cannot fit one line...")
            <b>.setStyle(NotificationCompat.BigTextStyle()
                    .bigText("Much longer text that cannot fit one line..."))</b>
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

### Java

    NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Much longer text that cannot fit one line...")
            <b>.setStyle(new NotificationCompat.BigTextStyle()
                    .bigText("Much longer text that cannot fit one line..."))</b>
            .setPriority(NotificationCompat.PRIORITY_DEFAULT);

For more information about other large notification styles, including how to add
an image and media playback controls, see
[Create an expandable notification](https://developer.android.com/training/notify-user/expanded).

### Create a channel and set the importance

Before you can deliver the notification on Android 8.0 and later, register your
app's [notification channel](https://developer.android.com/training/notify-user/channels) with the system by passing an instance of
[`NotificationChannel`](https://developer.android.com/reference/android/app/NotificationChannel) to [`createNotificationChannel()`](https://developer.android.com/reference/android/app/NotificationManager#createNotificationChannel(android.app.NotificationChannel)). The
following code is blocked by a condition on the [`SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT) version:

### Kotlin

    private fun createNotificationChannel() {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is not in the Support Library.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = getString(R.string.channel_name)
            val descriptionText = getString(R.string.channel_description)
            val importance = NotificationManager.IMPORTANCE_DEFAULT
            val channel = NotificationChannel(CHANNEL_ID, name, importance).apply {
                description = descriptionText
            }
            // Register the channel with the system.
            val notificationManager: NotificationManager =
                getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

### Java

    private void createNotificationChannel() {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is not in the Support Library.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            CharSequence name = getString(R.string.channel_name);
            String description = getString(R.string.channel_description);
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, name, importance);
            channel.setDescription(description);
            // Register the channel with the system; you can't change the importance
            // or other notification behaviors after this.
            NotificationManager notificationManager = getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

Because you must create the notification channel before posting any
notifications on Android 8.0 and later, execute this code as soon as your app
starts. It's safe to call this repeatedly, because creating an existing
notification channel performs no operation.

The `NotificationChannel` constructor requires an `importance`, using one of the
constants from the [`NotificationManager`](https://developer.android.com/reference/android/app/NotificationManager) class. This parameter determines
how to interrupt the user for any notification that belongs to this channel. Set
the *priority* with `setPriority()` to support Android 7.1 and earlier, as shown
in the preceding example.

Although you must set the notification importance or priority as shown in the
following example, the system doesn't guarantee the alert behavior you get. In
some cases, the system might change the importance level based on other factors,
and the user can always redefine what the importance level is for a given
channel.

For more information about what the different levels mean, read about
[notification importance levels](https://developer.android.com/training/notify-user/channels#importance).

### Set the notification's tap action

Every notification must respond to a tap, usually to open an activity in your
app that corresponds to the notification. To do so, specify a content intent
defined with a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) object and pass it to
[`setContentIntent()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentIntent(android.app.PendingIntent)).

The following snippet shows how to create a basic intent to open an activity
when the user taps the notification:

### Kotlin

    // Create an explicit intent for an Activity in your app.
    <b>val intent = Intent(this, AlertDetails::class.java).apply {
        flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
    }</b>
    val pendingIntent: PendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE)

    val builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            // Set the intent that fires when the user taps the notification.
            <b>.setContentIntent(pendingIntent)</b>
            .setAutoCancel(true)

### Java

    // Create an explicit intent for an Activity in your app.
    <b>Intent intent = new Intent(this, AlertDetails.class);
    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);</b>
    PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);

    NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            // Set the intent that fires when the user taps the notification.
            <b>.setContentIntent(pendingIntent)</b>
            .setAutoCancel(true);

This code calls [`setAutoCancel()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setAutoCancel(boolean)), which automatically [removes the
notification](https://developer.android.com/develop/ui/views/notifications/build-notification#Removing) when the user taps it.

The intent flags in the preceding example preserve the user's expected
navigation experience after the user opens your app using the notification. You
might want to use it depending on the type of activity you're starting, which
can be one of the following:

- An activity that exists exclusively for responses to the notification.
  There's no reason the user navigates to this activity during normal app use,
  so the activity starts a new task instead of being added to your app's
  existing [task and back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack). This is the type of intent created in
  the preceding sample.

- An activity that exists in your app's regular app flow. In this case,
  starting the activity creates a back stack so that the user's expectations
  for the [Back and Up buttons](https://developer.android.com/design/patterns/navigation) are preserved.

For more about the different ways to configure your notification's intent, see
[Start an Activity from a Notification](https://developer.android.com/training/notify-user/navigation).

### Show the notification

To make the notification appear, call
[`NotificationManagerCompat.notify()`](https://developer.android.com/reference/androidx/core/app/NotificationManagerCompat#notify(int,android.app.Notification)), passing it a unique ID for the
notification and the result of [`NotificationCompat.Builder.build()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#build()). This
is shown in the following example:

### Kotlin

    with(NotificationManagerCompat.from(this)) {
        if (ActivityCompat.checkSelfPermission(
                this@MainActivity,
                Manifest.permission.POST_NOTIFICATIONS
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            // TODO: Consider calling
            // ActivityCompat#requestPermissions
            // here to request the missing permissions, and then overriding
            // public fun onRequestPermissionsResult(requestCode: Int, permissions: Array&lt;out String&gt;,
            //                                        grantResults: IntArray)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.

            return@with
        }
        // notificationId is a unique int for each notification that you must define.
        notify(NOTIFICATION_ID, builder.build())
    }

### Java

    if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
        // TODO: Consider calling
        // ActivityCompat#requestPermissions
        // here to request the missing permissions, and then overriding
        // public void onRequestPermissionsResult(int requestCode, String[] permissions,
        //                                        int[] grantResults)
        // to handle the case where the user grants the permission. See the documentation
        // for ActivityCompat#requestPermissions for more details.
        return;
    }
    NotificationManagerCompat.from(this).notify(NOTIFICATION_ID, builder.build());

Save the notification ID that you pass to `NotificationManagerCompat.notify()`,
because you need it when you want to [update](https://developer.android.com/develop/ui/views/notifications/build-notification#Updating) or
[remove the notification](https://developer.android.com/develop/ui/views/notifications/build-notification#Removing).

Additionally, in order to test basic notifications on devices running on Android
13 and higher, turn on notifications manually or create a dialog to request
notifications.

> [!NOTE]
> **Note:** Beginning with Android 8.1 (API level 27), apps can't make a notification sound more than once per second. If your app posts multiple notifications in one second, they all appear as expected, but only the first notification per second makes a sound.

## Add action buttons

A notification can offer up to three action buttons that let the user respond
quickly, such as to snooze a reminder or to reply to a text message. But these
action buttons must not duplicate the action performed when the user [taps the
notification](https://developer.android.com/develop/ui/views/notifications/build-notification#tap).

![](https://developer.android.com/static/images/ui/notifications/notification-basic-action_2x.png)

**Figure 3.** A notification with
one action button.

<br />

To add an action button, pass a `PendingIntent` to the [`addAction()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#addAction(androidx.core.app.NotificationCompat.Action))
method. This is like setting up the notification's default tap action, except
instead of launching an activity, you can do other things such as start a
[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) that performs a job in the background so that the
action doesn't interrupt the app that's already open.

For example, the following code shows how to send a broadcast to a specific
receiver:

### Kotlin

    val ACTION_SNOOZE = "snooze"

    <b>val snoozeIntent = Intent(this, MyBroadcastReceiver::class.java).apply {
        action = ACTION_SNOOZE
        putExtra(EXTRA_NOTIFICATION_ID, 0)
    }
    val snoozePendingIntent: PendingIntent =
        PendingIntent.getBroadcast(this, 0, snoozeIntent, 0)</b>
    val builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setContentIntent(pendingIntent)
            <b>.addAction(R.drawable.ic_snooze, getString(R.string.snooze),
                    snoozePendingIntent)</b>

### Java

    String ACTION_SNOOZE = "snooze"

    <b>Intent snoozeIntent = new Intent(this, MyBroadcastReceiver.class);
    snoozeIntent.setAction(ACTION_SNOOZE);
    snoozeIntent.putExtra(EXTRA_NOTIFICATION_ID, 0);
    PendingIntent snoozePendingIntent =
            PendingIntent.getBroadcast(this, 0, snoozeIntent, 0);</b>

    NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setContentIntent(pendingIntent)
            <b>.addAction(R.drawable.ic_snooze, getString(R.string.snooze),
                    snoozePendingIntent);</b>

For more information about building a `BroadcastReceiver` to run background
work, see the [Broadcasts overview](https://developer.android.com/guide/components/broadcasts).

If you're instead trying to build a notification with media playback buttons,
such as to pause and skip tracks, see how to [create a notification with media
controls](https://developer.android.com/training/notify-user/expanded#media-style).

> [!NOTE]
> **Note:** In Android 10 (API level 29) and later, the platform automatically generates notification action buttons if an app doesn't provide its own. If you don't want your app's notifications to display any suggested replies or actions, you can opt-out of system-generated replies and actions by using [`setAllowGeneratedReplies()`](https://developer.android.com/reference/android/app/Notification.Action.Builder#setAllowGeneratedReplies(boolean)) and [`setAllowSystemGeneratedContextualActions()`](https://developer.android.com/reference/android/app/Notification.Builder#setAllowSystemGeneratedContextualActions(boolean)).

## Add a direct reply action

The direct reply action, introduced in Android 7.0 (API level 24), lets users
enter text directly into the notification. The text is then delivered to your
app without opening an activity. For example, you can use a direct reply action
to let users reply to text messages or update task lists from within the
notification.

![](https://developer.android.com/static/images/ui/notifications/reply-button_2x.png)

**Figure 4.** Tapping the "Reply"
button opens the text input.

<br />

The direct reply action appears as an additional button in the notification that
opens a text input. When the user finishes typing, the system attaches the text
response to the intent you specify for the notification action and sends the
intent to your app.

### Add the reply button

To create a notification action that supports direct reply, follow these steps:

1. Create an instance of `https://developer.android.com/reference/androidx/core/app/RemoteInput.Builder` that you can add to your notification action. This class's constructor accepts a string that the system uses as the key for the text input. Your app later uses that key to retrieve the text of the input. \* {Kotlin} \`\`\`kotlin // Key for the string that's delivered in the action's intent. private val KEY_TEXT_REPLY = "key_text_reply" var replyLabel: String = resources.getString(R.string.reply_label) var remoteInput: RemoteInput = RemoteInput.Builder(KEY_TEXT_REPLY).run { setLabel(replyLabel) build() } \`\`\` \* {Java} \`\`\`java // Key for the string that's delivered in the action's intent. private static final String KEY_TEXT_REPLY = "key_text_reply"; String replyLabel = getResources().getString(R.string.reply_label); RemoteInput remoteInput = new RemoteInput.Builder(KEY_TEXT_REPLY) .setLabel(replyLabel) .build(); \`\`\`
2. Create a `PendingIntent` for the reply action. \* {Kotlin} \`\`\`kotlin // Build a PendingIntent for the reply action to trigger. var replyPendingIntent: PendingIntent = PendingIntent.getBroadcast(applicationContext, conversation.getConversationId(), getMessageReplyIntent(conversation.getConversationId()), PendingIntent.FLAG_UPDATE_CURRENT) \`\`\` \* {Java} \`\`\`java // Build a PendingIntent for the reply action to trigger. PendingIntent replyPendingIntent = PendingIntent.getBroadcast(getApplicationContext(), conversation.getConversationId(), getMessageReplyIntent(conversation.getConversationId()), PendingIntent.FLAG_UPDATE_CURRENT); \`\`\`

   > [!CAUTION]
   > **Caution:** If you reuse a `PendingIntent`, a user might reply to a different conversation than the one they intend. You must provide a request code that is different for each conversation or provide an intent that doesn't return `true` when you call `https://developer.android.com/reference/android/app/PendingIntent#equals(java.lang.Object)` on the reply intent of any other conversation. The conversation ID is frequently passed as part of the intent's extras bundle, but is ignored when you call `equals()`.

3. Attach the `https://developer.android.com/reference/androidx/core/app/RemoteInput` object to an action using `https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action.Builder#addRemoteInput(androidx.core.app.RemoteInput)`. \* {Kotlin} \`\`\`kotlin // Create the reply action and add the remote input. var action: NotificationCompat.Action = NotificationCompat.Action.Builder(R.drawable.ic_reply_icon, getString(R.string.label), replyPendingIntent) .addRemoteInput(remoteInput) .build() \`\`\` \* {Java} \`\`\`java // Create the reply action and add the remote input. NotificationCompat.Action action = new NotificationCompat.Action.Builder(R.drawable.ic_reply_icon, getString(R.string.label), replyPendingIntent) .addRemoteInput(remoteInput) .build(); \`\`\`
4. Apply the action to a notification and issue the notification. \* {Kotlin} \`\`\`kotlin // Build the notification and add the action. val newMessageNotification = Notification.Builder(context, CHANNEL_ID) .setSmallIcon(R.drawable.ic_message) .setContentTitle(getString(R.string.title)) .setContentText(getString(R.string.content)) .addAction(action) .build() // Issue the notification. with(NotificationManagerCompat.from(this)) { notificationManager.notify(notificationId, newMessageNotification) } \`\`\` \* {Java} \`\`\`java // Build the notification and add the action. Notification newMessageNotification = new Notification.Builder(context, CHANNEL_ID) .setSmallIcon(R.drawable.ic_message) .setContentTitle(getString(R.string.title)) .setContentText(getString(R.string.content)) .addAction(action) .build(); // Issue the notification. NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this); notificationManager.notify(notificationId, newMessageNotification); \`\`\`

The system prompts the user to input a response when they trigger the
notification action, as shown in figure 4.

### Retrieve user input from the reply

To receive user input from the notification's reply UI, call
[`RemoteInput.getResultsFromIntent()`](https://developer.android.com/reference/androidx/core/app/RemoteInput#getResultsFromIntent(android.content.Intent)), passing it the `Intent` received by
your `BroadcastReceiver`:

### Kotlin

    private fun getMessageText(intent: Intent): CharSequence? {
        return RemoteInput.getResultsFromIntent(intent)?.getCharSequence(KEY_TEXT_REPLY)
    }

### Java

    private CharSequence getMessageText(Intent intent) {
        Bundle remoteInput = RemoteInput.getResultsFromIntent(intent);
        if (remoteInput != null) {
            return remoteInput.getCharSequence(KEY_TEXT_REPLY);
        }
        return null;
     }

After you process the text, update the notification by calling
`NotificationManagerCompat.notify()` with the same ID and tag, if used. This is
necessary to hide the direct reply UI and confirm to the user that their reply
is received and processed correctly.

### Kotlin

    // Build a new notification, which informs the user that the system
    // handled their interaction with the previous notification.
    val repliedNotification = Notification.Builder(context, CHANNEL_ID)
            .setSmallIcon(R.drawable.ic_message)
            .setContentText(getString(R.string.replied))
            .build()

    // Issue the new notification.
    NotificationManagerCompat.from(this).apply {
        notificationManager.notify(notificationId, repliedNotification)
    }

### Java

    // Build a new notification, which informs the user that the system
    // handled their interaction with the previous notification.
    Notification repliedNotification = new Notification.Builder(context, CHANNEL_ID)
            .setSmallIcon(R.drawable.ic_message)
            .setContentText(getString(R.string.replied))
            .build();

    // Issue the new notification.
    NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);
    notificationManager.notify(notificationId, repliedNotification);

### Retrieve other data

Handling other data types works similarly with `RemoteInput`. The following
example uses image as input.

### Kotlin

      // Key for the data that's delivered in the action's intent.
      private val KEY_REPLY = "key_reply"
      var replyLabel: String = resources.getString(R.string.reply_label)
      var remoteInput: RemoteInput = RemoteInput.Builder(KEY_REPLY).run {
          setLabel(replyLabel)
          // Allow for image data types in the input
      // This method can be used again to
      // allow for other data types
          setAllowDataType("image/*", true)
          build()
    }

Call `RemoteInput#getDataResultsFromIntent` and extract the corresponding data.

### Kotlin

      import android.app.RemoteInput;
      import android.content.Intent;
      import android.os.Bundle;

      class ReplyReceiver: BroadcastReceiver()  {

          public static final String KEY_DATA = "key_data";

          public static void handleRemoteInput(Intent intent) {
              Bundle dataResults = RemoteInput.getDataResultsFromIntent(intent, KEY_DATA);
              val imageUri: Uri? = dataResults.values.firstOrNull()
              if (imageUri != null) {
                  // Extract the image
              try {
                      val inputStream = context.contentResolver.openInputStream(imageUri)
                      val bitmap = BitmapFactory.decodeStream(inputStream)
                      // Display the image
                      // ...
                  } catch (e: Exception) {
                      Log.e("ReplyReceiver", "Failed to process image URI", e)
                  }
          }
      }

When working with this new notification, use the context that's passed to the
receiver's [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent)) method.

Append the reply to the bottom of the notification by calling
[`setRemoteInputHistory()`](https://developer.android.com/reference/android/app/Notification.Builder#setRemoteInputHistory(java.lang.CharSequence%5B%5D)). However, if you're building a messaging app,
create a [messaging-style notification](https://developer.android.com/training/notify-user/expanded#message-style) and append the new message to the
conversation.

For more advice for notifications from a messaging apps, see the section about
[best practices for messaging apps](https://developer.android.com/develop/ui/views/notifications/build-notification#messaging-best-practices).

## Show an urgent message

Your app might need to display an urgent, time-sensitive message, such as an
incoming phone call or a ringing alarm. In these situations, you can associate a
full-screen intent with your notification.

> [!CAUTION]
> **Caution:** Notifications containing full-screen intents are substantially intrusive, so it's important to only use this type of notification for the most urgent, time-sensitive messages.

When the notification is invoked, users see one of the following, depending on
the device's lock status:

- If the user's device is locked, a full-screen activity appears, covering the lockscreen.
- If the user's device is unlocked, the notification appears in an expanded form that includes options for handling or dismissing the notification.

> [!NOTE]
> **Note:** If your app targets Android 10 (API level 29) or later, you must request the [`USE_FULL_SCREEN_INTENT`](https://developer.android.com/reference/android/Manifest.permission#USE_FULL_SCREEN_INTENT) permission in your app's manifest file for the system to launch the full-screen activity associated with the time-sensitive notification.

The following code snippet demonstrates how to associate your notification with
a full-screen intent:

### Kotlin

    val fullScreenIntent = Intent(this, ImportantActivity::class.java)
    val fullScreenPendingIntent = PendingIntent.getActivity(this, 0,
        fullScreenIntent, PendingIntent.FLAG_UPDATE_CURRENT)

    var builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            <b>.setFullScreenIntent(fullScreenPendingIntent, true)</b>

### Java

    Intent fullScreenIntent = new Intent(this, ImportantActivity.class);
    PendingIntent fullScreenPendingIntent = PendingIntent.getActivity(this, 0,
            fullScreenIntent, PendingIntent.FLAG_UPDATE_CURRENT);

    NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.notification_icon)
            .setContentTitle("My notification")
            .setContentText("Hello World!")
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            <b>.setFullScreenIntent(fullScreenPendingIntent, true);</b>

## Set lock screen visibility

To control the level of detail visible in the notification from the lock screen,
call [`setVisibility()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setVisibility(int)) and specify one of the following values:

- [`VISIBILITY_PUBLIC`](https://developer.android.com/reference/androidx/core/app/NotificationCompat#VISIBILITY_PUBLIC()): the notification's full content shows on the lock
  screen.

- [`VISIBILITY_SECRET`](https://developer.android.com/reference/androidx/core/app/NotificationCompat#VISIBILITY_SECRET()): no part of the notification shows on the lock
  screen.

- [`VISIBILITY_PRIVATE`](https://developer.android.com/reference/androidx/core/app/NotificationCompat#VISIBILITY_PRIVATE()): only basic information, such as the
  notification's icon and the content title, shows on the lock screen. The
  notification's full content doesn't show.

When you set `VISIBILITY_PRIVATE`, you can also provide an alternate version of
the notification content that hides certain details. For example, an SMS app
might display a notification that shows "You have 3 new text messages," but
hides the message contents and senders. To provide this alternative
notification, first create the alternative notification with
`NotificationCompat.Builder` as usual. Then, attach the alternative notification
to the normal notification with [`setPublicVersion()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setPublicVersion(android.app.Notification)).

Bear in mind that the user always has ultimate control over whether their
notifications are visible on the lock screen and can control them based on your
app's notification channels.

## Update a notification

To update a notification after you issue it, call
`NotificationManagerCompat.notify()` again, passing it the same ID you used
before. If the previous notification is dismissed, a new notification is created
instead.

You can optionally call [`setOnlyAlertOnce()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setOnlyAlertOnce(boolean)) so your notification
interrupts the user---with sound, vibration, or visual clues---only the
first time the notification appears and not for later updates.

> [!CAUTION]
> **Caution:** Android applies a rate limit when updating a notification. If you post updates to a notification too frequently---many in less than one second---the system might drop updates.

## Remove a notification

Notifications remain visible until one of the following happens:

- The user dismisses the notification.
- The user taps the notification, if you call `setAutoCancel()` when you create the notification.
- You call [`cancel()`](https://developer.android.com/reference/android/app/NotificationManager#cancel(int)) for a specific notification ID. This method also deletes ongoing notifications.
- You call [`cancelAll()`](https://developer.android.com/reference/android/app/NotificationManager#cancelAll()), which removes all notifications you previously issued.
- The specified duration elapses, if you set a timeout when creating the notification, using [`setTimeoutAfter()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setTimeoutAfter(long)). If required, you can cancel a notification before the specified timeout duration elapses.

## Best practices for messaging apps

Consider the best practices listed here when creating notifications for your
messaging and chat apps.

#### Use MessagingStyle

Starting in Android 7.0 (API level 24), Android provides a notification style
template specifically for messaging content. Using the
[`NotificationCompat.MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle) class, you can change several of the
labels displayed on the notification, including the conversation title,
additional messages, and the content view for the notification.

The following code snippet demonstrates how to customize a notification's style
using the `MessagingStyle` class.

### Kotlin

    val user = Person.Builder()
        .setIcon(userIcon)
        .setName(userName)
        .build()

    val notification = NotificationCompat.Builder(this, CHANNEL_ID)
        .setContentTitle("2 new messages with $sender")
        .setContentText(subject)
        .setSmallIcon(R.drawable.new_message)
        .setStyle(NotificationCompat.MessagingStyle(user)
            .addMessage(messages[1].getText(), messages[1].getTime(), messages[1].getPerson())
            .addMessage(messages[2].getText(), messages[2].getTime(), messages[2].getPerson())
        )
        .build()

### Java

    Person user = new Person.Builder()
        .setIcon(userIcon)
        .setName(userName)
        .build();

    Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
        .setContentTitle("2 new messages with " + sender)
        .setContentText(subject)
        .setSmallIcon(R.drawable.new_message)
        .setStyle(new NotificationCompat.MessagingStyle(user)
            .addMessage(messages[1].getText(), messages[1].getTime(), messages[1].getPerson())
            .addMessage(messages[2].getText(), messages[2].getTime(), messages[2].getPerson())
        )
        .build();

Starting in Android 9.0 (API level 28), It is also required to use the
[`Person`](https://developer.android.com/reference/kotlin/android/app/Person) class in order to get an optimal rendering of the notification
and its avatars.

When using `NotificationCompat.MessagingStyle`, do the following:

- Call [`MessagingStyle.setConversationTitle()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle#setConversationTitle(java.lang.CharSequence)) to set a title for group chats with more than two people. A good conversation title might be the name of the group chat or, if it doesn't have a name, a list of the participants in the conversation. Without this, the message might be mistaken as belonging to a one-to-one conversation with the sender of the most recent message in the conversation.
- Use the [`MessagingStyle.setData()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle.Message#setData(java.lang.String,android.net.Uri)) method to include media messages such as images. MIME types of the pattern image/\* are supported.

#### Use Direct Reply

Direct Reply lets a user reply inline to a message.

- After a user replies with the inline reply action, use [`MessagingStyle.addMessage()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle#addMessage(androidx.core.app.NotificationCompat.MessagingStyle.Message)) to update the `MessagingStyle` notification, and don't retract or cancel the notification. Not cancelling the notification lets the user send multiple replies from the notification.
- To make the inline reply action compatible with Wear OS, call [`Action.WearableExtender.setHintDisplayInlineAction(true)`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action.WearableExtender#setHintDisplayActionInline(boolean)).
- Use the [`addHistoricMessage()`](https://developer.android.com/reference/android/app/Notification.MessagingStyle#addHistoricMessage(android.app.Notification.MessagingStyle.Message)) method to provide context to a direct reply conversation by adding historic messages to the notification.

#### Enable Smart Reply

- To enable Smart Reply, call [`setAllowGeneratedResponses(true)`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action.Builder#setAllowGeneratedReplies(boolean)) on the reply action. This causes Smart Reply responses to be available to users when the notification is bridged to a Wear OS device. Smart Reply responses are generated by an entirely on-watch machine learning model using the context provided by the `NotificationCompat.MessagingStyle` notification, and no data is uploaded to the internet to generate the responses.

#### Add notification metadata

- Assign notification metadata to tell the system how to handle your app notifications when the device is in [`Do Not Disturb mode`](https://developer.android.com/guide/topics/ui/notifiers/notifications#dnd-mode). For example, use the [`addPerson()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#addPerson(androidx.core.app.Person)) or [`setCategory(Notification.CATEGORY_MESSAGE)`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setCategory(java.lang.String)) method to override the Do Not Disturb.