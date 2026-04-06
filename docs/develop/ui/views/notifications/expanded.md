---
title: Create an expandable notification  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/notifications/expanded
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create an expandable notification Stay organized with collections Save and categorize content based on your preferences.



A basic notification usually includes a title, a line of text, and actions the
user can perform in response. To provide more information, you can create large,
expandable notifications by applying one of several notification templates as
described in this document.

To start, build a notification with all the basic content as described in
[Create a notification](/training/notify-user/build-notification). Then,
call
[`setStyle()`](/reference/androidx/core/app/NotificationCompat.Builder#setStyle(androidx.core.app.NotificationCompat.Style))
with a style object and supply information corresponding to each template, as
shown in the following examples.

## Add a large image

To add an image in your notification, pass an instance of
[`NotificationCompat.BigPictureStyle`](/reference/androidx/core/app/NotificationCompat.BigPictureStyle)
to `setStyle()`.

### Kotlin

```
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_post)
        .setContentTitle(imageTitle)
        .setContentText(imageDescription)
        .setStyle(NotificationCompat.BigPictureStyle()
                .bigPicture(myBitmap))
        .build()
```

### Java

```
Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_post)
        .setContentTitle(imageTitle)
        .setContentText(imageDescription)
        .setStyle(new NotificationCompat.BigPictureStyle()
               .bigPicture(myBitmap))
        .build();
```

To make the image appear as a thumbnail only while the notification is
collapsed, as shown in the following figure, call
[`setLargeIcon()`](/reference/androidx/core/app/NotificationCompat.Builder#setLargeIcon(android.graphics.Bitmap))
and pass it the image. Then, call
[`BigPictureStyle.bigLargeIcon()`](/reference/androidx/core/app/NotificationCompat.BigPictureStyle#bigLargeIcon(android.graphics.Bitmap))
and pass it `null` so the large icon goes away when the notification is
expanded:

### Kotlin

```
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_post)
        .setContentTitle(imageTitle)
        .setContentText(imageDescription)
        .setLargeIcon(myBitmap)
        .setStyle(NotificationCompat.BigPictureStyle()
                .bigPicture(myBitmap)
                .bigLargeIcon(null))
        .build()
```

### Java

```
Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_post)
        .setContentTitle(imageTitle)
        .setContentText(imageDescription)
        .setLargeIcon(myBitmap)
        .setStyle(new NotificationCompat.BigPictureStyle()
                .bigPicture(myBitmap)
                .bigLargeIcon(null))
        .build();
```

![An image showing a collapsed notification and an expanded notification containing a blue image](/static/images/ui/notifications/template-image_2x.png)


**Figure 1.** A notification using
`NotificationCompat.BigPictureStyle`.

## Add a large block of text

Apply
[`NotificationCompat.BigTextStyle`](/reference/androidx/core/app/NotificationCompat.BigTextStyle)
to display text in the expanded content area of the notification:

### Kotlin

```
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_mail)
        .setContentTitle(emailObject.getSenderName())
        .setContentText(emailObject.getSubject())
        .setLargeIcon(emailObject.getSenderAvatar())
        .setStyle(NotificationCompat.BigTextStyle()
                .bigText(emailObject.getSubjectAndSnippet()))
        .build()
```

### Java

```
Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_mail)
        .setContentTitle(emailObject.getSenderName())
        .setContentText(emailObject.getSubject())
        .setLargeIcon(emailObject.getSenderAvatar())
        .setStyle(new NotificationCompat.BigTextStyle()
                .bigText(emailObject.getSubjectAndSnippet()))
        .build();
```

![An image showing a collapsed notification and an expanded notification using BigTextStyle](/static/images/ui/notifications/template-large-text_2x.png)


**Figure 2.** A notification using
`NotificationCompat.BigTextStyle`.

**Tip:** To add formatting in your text—such as bold, italic, line breaks, and
so on—you can [add styling with HTML
markup](/guide/topics/resources/string-resource#StylingWithHTML).

## Create an inbox-style notification

Apply
[`NotificationCompat.InboxStyle`](/reference/androidx/core/app/NotificationCompat.InboxStyle)
to a notification if you want to add multiple short summary lines, such as
snippets from incoming emails. This lets you add multiple pieces of content text
that are each truncated to one line, instead of the one continuous line of text
provided by `NotificationCompat.BigTextStyle`.

To add a new line, call
[`addLine()`](/reference/androidx/core/app/NotificationCompat.InboxStyle#addLine(java.lang.CharSequence))
up to six times, as shown in the following example. If you add more than six
lines, only the first six are visible.

**Tip:** You can distinguish the message's subject and message in each line by
[adding styling with HTML
markup](/guide/topics/resources/string-resource#StylingWithHTML), such as
bolding the subject.

### Kotlin

```
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.baseline_email_24)
        .setContentTitle("5 New mails from Frank")
        .setContentText("Check them out")
        .setLargeIcon(BitmapFactory.decodeResource(resources, R.drawable.logo))
        .setStyle(
                NotificationCompat.InboxStyle()
                .addLine("Re: Planning")
                .addLine("Delivery on its way")
                .addLine("Follow-up")
        )
        .build()
```

### Java

```
Notification notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.baseline_email_24)
        .setContentTitle("5 New mails from Frank")
        .setContentText("Check them out")
        .setLargeIcon(BitmapFactory.decodeResource(resources, R.drawable.logo))
        .setStyle(
                NotificationCompat.InboxStyle()
                .addLine("Re: Planning")
                .addLine("Delivery on its way")
                .addLine("Follow-up")
        )
        .build();
```

The result looks like the following figure:

![An image showing an expanded inbox-style notification](/static/images/ui/notifications/expanded_inbox_style_2.png)


**Figure 3.** An expanded inbox-style
notification.

**Note:** For more information about how to group multiple notifications, see
[Create a group of notifications](/develop/ui/views/notifications/group).

## Show a conversation in a notification

Apply
[`NotificationCompat.MessagingStyle`](/reference/androidx/core/app/NotificationCompat.MessagingStyle)
to display sequential messages between any number of people. This is ideal for
messaging apps, because it provides a consistent layout for each message by
handling the sender name and message text separately, and each message can be
multiple lines long.

To add a new message, call
[`addMessage()`](/reference/androidx/core/app/NotificationCompat.MessagingStyle#addMessage(androidx.core.app.NotificationCompat.MessagingStyle.Message)),
passing the message text, the time received, and the sender's name. You can also
pass this information as a
[`NotificationCompat.MessagingStyle.Message`](/reference/androidx/core/app/NotificationCompat.MessagingStyle.Message)
object, as shown in the following example:

### Kotlin

```
val message1 = NotificationCompat.MessagingStyle.Message(
        messages[0].getText(),
        messages[0].getTime(),
        messages[0].getSender())
val message2 = NotificationCompat.MessagingStyle.Message(
        messages[1].getText(),
        messages[1].getTime(),
        messages[1].getSender())
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_message)
        .setStyle(
                NotificationCompat.MessagingStyle(resources.getString(R.string.reply_name))
                .addMessage(message1)
                .addMessage(message2))
        .build()
```

### Java

```
NotificationCompat.MessagingStyle.Message message1 =
        new NotificationCompat.MessagingStyle.Message(messages[0].getText(),
                                                      messages[0].getTime(),
                                                      messages[0].getSender());
NotificationCompat.MessagingStyle.Message message2 =
        new NotificationCompat.MessagingStyle.Message(messages[1].getText(),
                                                      messages[1].getTime(),
                                                      messages[1].getSender());

Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(R.drawable.new_message)
        .setStyle(new NotificationCompat.MessagingStyle(resources.getString(R.string.reply_name))
                .addMessage(message1)
                .addMessage(message2))
        .build();
```

![An image showing a notification in messaging style](/static/images/ui/notifications/template-messaging_2x.png)


**Figure 4.** A notification using
`NotificationCompat.MessagingStyle`.

When using `NotificationCompat.MessagingStyle`, any values given to
[`setContentTitle()`](/reference/androidx/core/app/NotificationCompat.Builder#setContentTitle(java.lang.CharSequence))
and
[`setContentText()`](/reference/androidx/core/app/NotificationCompat.Builder#setContentText(java.lang.CharSequence))
are ignored.

You can call
[`setConversationTitle()`](/reference/androidx/core/app/NotificationCompat.MessagingStyle#setConversationTitle(java.lang.CharSequence))
to add a title that appears above the conversation. This might be the
user-created name of the group or, if it doesn't have a specific name, a list of
the participants in the conversation. Don't set a conversation title for
one-on-one chats, because the system uses the existence of this field as a hint
that the conversation is a group.

This style applies only on devices running Android 7.0 (API level 24) and later.
When using the compatibility library
([`NotificationCompat`](/reference/androidx/core/app/NotificationCompat)),
as demonstrated earlier, notifications with `MessagingStyle` fall back
automatically to a supported expanded notification style.

When building a notification like this for a chat conversation, [add a direct
reply action](/training/notify-user/build-notification#reply-action).

## Create a notification with media controls

**Note:** When using AndroidX Media3, the
[media notification is created automatically](/media/implement/playback-app#publishing_a_notification).

Apply
[`MediaStyleNotificationHelper.MediaStyle`](/reference/androidx/media3/session/MediaStyleNotificationHelper.MediaStyle)
to display media playback controls and track information.

Specify your associated
[`MediaSession`](/reference/androidx/media3/session/MediaSession) in the
constructor. This allows Android to display the right information about your
media.

Call
[`addAction()`](/reference/androidx/core/app/NotificationCompat.Builder#addAction(androidx.core.app.NotificationCompat.Action))
up to five times to display up to five icon buttons. Call `setLargeIcon()` to
set the album artwork.

Unlike the other notification styles, `MediaStyle` also lets you modify the
collapsed-size content view by specifying three action buttons that also appear
in the collapsed view. To do so, provide the action button indices to
[`setShowActionsInCompactView()`](/reference/androidx/media3/session/MediaStyleNotificationHelper.MediaStyle#setShowActionsInCompactView(int...)).

The following example shows how to create a notification with media controls:

### Kotlin

```
val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        // Show controls on lock screen even when user hides sensitive content.
        .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
        .setSmallIcon(R.drawable.ic_stat_player)
        // Add media control buttons that invoke intents in your media service
        .addAction(R.drawable.ic_prev, "Previous", prevPendingIntent) // #0
        .addAction(R.drawable.ic_pause, "Pause", pausePendingIntent) // #1
        .addAction(R.drawable.ic_next, "Next", nextPendingIntent) // #2
        // Apply the media style template.
        .setStyle(MediaStyleNotificationHelper.MediaStyle(mediaSession)
                .setShowActionsInCompactView(1 /* #1: pause button \*/))
        .setContentTitle("Wonderful music")
        .setContentText("My Awesome Band")
        .setLargeIcon(albumArtBitmap)
        .build()
```

### Java

```
Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
        // Show controls on lock screen even when user hides sensitive content.
        .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
        .setSmallIcon(R.drawable.ic_stat_player)
        // Add media control buttons that invoke intents in your media service
        .addAction(R.drawable.ic_prev, "Previous", prevPendingIntent) // #0
        .addAction(R.drawable.ic_pause, "Pause", pausePendingIntent)  // #1
        .addAction(R.drawable.ic_next, "Next", nextPendingIntent)     // #2
        // Apply the media style template.
        .setStyle(new MediaStyleNotificationHelper.MediaStyle(mediaSession)
                .setShowActionsInCompactView(1 /* #1: pause button */))
        .setContentTitle("Wonderful music")
        .setContentText("My Awesome Band")
        .setLargeIcon(albumArtBitmap)
        .build();
```

![An image showing a notification with media style](/static/images/ui/notifications/template-media_2x.png)


**Figure 5.** A notification using
`MediaStyleNotificationHelper.MediaStyle`.

**Note:** Notifications created with `MediaStyleNotificationHelper.MediaStyle` have their
category set to
[`CATEGORY_TRANSPORT`](/reference/androidx/core/app/NotificationCompat#CATEGORY_TRANSPORT())
unless you set a different category using
[`setCategory()`](/reference/androidx/core/app/NotificationCompat.Builder#setCategory(java.lang.String)).

## Additional resources

See the following references for more information about `MediaStyle` and
expandable notifications.

* [Using MediaStyle notifications with a foreground service](/media/implement/playback-app#implementing_a_mediasessionservice)
* [SociaLite sample app](https://github.com/android/socialite)