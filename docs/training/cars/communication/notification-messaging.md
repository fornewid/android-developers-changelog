---
title: https://developer.android.com/training/cars/communication/notification-messaging
url: https://developer.android.com/training/cars/communication/notification-messaging
source: md.txt
---

Apps that support messaging can extend their messaging notifications to let
Android Auto consume them when it is running. These notifications are displayed
by Android Auto and let users read and respond to messages in a consistent,
low-distraction interface. And when you use the [`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle) API, you
get optimized message notifications for all Android devices, including Android
Auto. The optimizations include a UI that's specialized for message
notifications, improved animations, and support for inline images.

This guide shows you how to extend an app that displays messages to the user and
receives the user's replies, such as a chat app, to hand message display and
reply receipt off to an Android Auto. Through this integration, users can only
see message history from notifications received during their active Android Auto
session. To display messages from before their active Android Auto session
began, you can [build a templated messaging experience](https://developer.android.com/training/cars/communication/templated-messaging).

For related design guidance, see [Communications apps](https://developer.android.com/design/ui/cars/guides/app-types/communications) in the Design for Cars
hub.
| **Important:** New and existing messaging apps can't be directly installed as a driver-optimized app on Android Automotive OS. They can only be distributed through Android Auto. For more information, see [Supported app categories](https://developer.android.com/training/cars#supported-app-categories).

## Get started

To provide messaging service for Android Auto, your app must declare its
support for Android Auto in the manifest and be able to do the following:

- [Declare support for Android Auto](https://developer.android.com/training/cars/communication/notification-messaging#manifest-messaging)
- Build and send [`NotificationCompat.MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle) objects that contain reply and mark-as-read [`Action`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action) objects.
- Handle replying and marking a conversation as read with a `Service`.

### Concepts and objects

Before you start designing your app, it's helpful to understand how Android Auto
handles messaging.

An individual chunk of communication is called a *message* and is represented by
the class [`MessagingStyle.Message`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle.Message). A message contains a sender, the
message content, and the time the message was sent.

Communication between users is called a *conversation* and is represented by a
`MessagingStyle` object. A conversation, or `MessagingStyle`, contains a title,
the messages, and whether the conversation is among a group of users.

To notify users of updates to a conversation, such as a new message, apps post a
[`Notification`](https://developer.android.com/reference/android/app/Notification) to the Android system. This `Notification` uses the
`MessagingStyle` object to display messaging-specific UI in the notification
shade. The Android platform also passes this `Notification` to Android Auto, and
the `MessagingStyle` is extracted and used to post a notification on the car's
display.

Android Auto also requires apps to add [`Action`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action) objects to a `Notification`
to let the user reply to a message or mark it as read directly from the car's
display.

In summary, a single conversation is represented by a `Notification` object that
is styled with a `MessagingStyle` object. The `MessagingStyle` contains all the
messages within that conversation in one or more `MessagingStyle.Message`
objects. And, to be Android Auto compliant, an app must attach reply and
mark-as-read `Action` objects to the `Notification`.

### Messaging flow

This section describes a typical messaging flow between your app and Android
Auto.

1. Your app receives a message.
2. Your app generates a `MessagingStyle` notification with reply and mark-as-read `Action` objects.
3. Android Auto receives the "new notification" event from the Android system and finds the `MessagingStyle`, reply `Action`, and mark-as-read `Action`.
4. Android Auto generates and displays a notification in the car.
5. If the user taps the notification on the car's display, Android Auto triggers the mark-as-read `Action`.
   - In the background, your app must handle this mark-as-read event.
6. If the user responds to the notification using voice, Android Auto puts a transcription of the user's response into the reply `Action` and then triggers it.
   - In the background, your app must handle this reply event.

### Preliminary assumptions

This page doesn't guide you in creating an entire messaging app. The following
code sample includes some of the things your app needs before you start to
support messaging with Android Auto:

    data class YourAppConversation(
            val id: Int,
            val title: String,
            val recipients: MutableList<YourAppUser>,
            val icon: Bitmap) {
        companion object {
            /** Fetches [YourAppConversation] by its [id]. */
            fun getById(id: Int): YourAppConversation = // ...
        }

        /** Replies to this conversation with the given [message]. */
        fun reply(message: String) {}

        /** Marks this conversation as read. */
        fun markAsRead() {}

        /** Retrieves all unread messages from this conversation. */
        fun getUnreadMessages(): List<YourAppMessage> { return /* ... */ }
    }
    data class YourAppUser(val id: Int, val name: String, val icon: Uri)
    data class YourAppMessage(
        val id: Int,
        val sender: YourAppUser,
        val body: String,
        val timeReceived: Long)

## Declare Android Auto support

When Android Auto receives a notification from a messaging app, it checks that
the app has declared support for Android Auto. To enable this support, include
the following entry in your app's manifest:

    <application>
        ...
        <meta-data
            android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to another XML file, `automotive_app_desc.xml`, that
you need to create in your app module's [`res/xml` directory](https://developer.android.com/guide/topics/resources/providing-resources#ResourceTypes). In
`automotive_app_desc.xml`, declare the Android Auto capabilities your app
supports. To declare support for notifications, include the following:

    <automotiveApp>
        <uses name="notification" />
    </automotiveApp>

If your app can be set as the [default SMS handler](https://developer.android.com/reference/android/provider/Telephony#creating-an-sms-app), make sure to include the
following `<uses>` element. If you don't, Android Auto uses its built-in default
handler to handle incoming SMS/MMS messages when your app is set as the default
SMS handler, which can lead to duplicate notifications.

    <automotiveApp>
        ...
        <uses name="sms" />
    </automotiveApp>

## Import the AndroidX core library

Building notifications for use with Android Auto requires the [AndroidX](https://developer.android.com/jetpack/androidx) core
library. Import the library into your project as follows:

1. In the top-level `build.gradle` file, include a dependency on Google's Maven repository, as shown in the following example:

### Groovy

```groovy
allprojects {
    repositories {
        google()
    }
}
```

### Kotlin

```kotlin
allprojects {
    repositories {
        google()
    }
}
```

1. In your app module's `build.gradle` file, include the [AndroidX Core](https://developer.android.com/jetpack/androidx/releases/core) library dependency, as shown in the following example:

### Groovy

```groovy
dependencies {
    // If your app is written in Java
    implementation 'androidx.core:core:1.17.0'

    // If your app is written in Kotlin
    implementation 'androidx.core:core-ktx:1.17.0'
}
```

### Kotlin

```kotlin
dependencies {
    // If your app is written in Java
    implementation("androidx.core:core:1.17.0")

    // If your app is written in Kotlin
    implementation("androidx.core:core-ktx:1.17.0")
}
```

## Handle user actions

Your messaging app needs a way to handle updating a conversation through an
`Action`. For Android Auto, there are two types of `Action` objects your app
needs to handle: reply and mark-as-read. We recommend handling them using an
[`IntentService`](https://developer.android.com/reference/android/app/IntentService), which provides the flexibility to handle potentially
expensive calls *in the background*, freeing your app's main thread.
| **Warning:** Don't use an `Activity` or `Fragment` to handle an `Action`. They not only run in the foreground but also are known to cause UI issues that can cause your app to be blocked from Android Auto.

### Define intent actions

`Intent` actions are basic strings of your choosing that identify what the
`Intent` is for. Because a single service can handle multiple types of intents,
it's easier to define multiple action strings instead of defining multiple
`IntentService` components.

This guide's example messaging app has the two required types of actions: reply
and mark-as-read, as shown in the following code sample:

    private const val ACTION_REPLY = "com.example.REPLY"
    private const val ACTION_MARK_AS_READ = "com.example.MARK_AS_READ"

### Create the service

To create a service that handles these `Action` objects, you need the
conversation ID, which is an arbitrary data structure defined by your app that
identifies the conversation. You also need a remote input key, which is
discussed in detail later in this section. The following code sample creates a
service to handle the required actions:

    private const val EXTRA_CONVERSATION_ID_KEY = "conversation_id"
    private const val REMOTE_INPUT_RESULT_KEY = "reply_input"

    /**
     * An [IntentService] that handles reply and mark-as-read actions for
     * [YourAppConversation]s.
     */
    class MessagingService : IntentService("MessagingService") {
        override fun onHandleIntent(intent: Intent?) {
            // Fetches internal data.
            val conversationId = intent!!.getIntExtra(EXTRA_CONVERSATION_ID_KEY, -1)

            // Searches the database for that conversation.
            val conversation = YourAppConversation.getById(conversationId)

            // Handles the action that was requested in the intent. The TODOs
            // are addressed in a later section.
            when (intent.action) {
                ACTION_REPLY -> TODO()
                ACTION_MARK_AS_READ -> TODO()
            }
        }
    }

| **Tip:** Although `IntentService` is deprecated as of API 30, it still works for the Android Auto use cases described in this guide. Because the `IntentService` starts in response to a `PendingIntent` from a notification, the system puts your app on an allowlist that allows the background service to start and execute. See [Background Service Limitations](https://developer.android.com/about/versions/oreo/background#services) for more information.

To associate this service with your app, you also need to register the service
in your app's manifest, as shown in the following example:

    <application>
        <service android:name="com.example.MessagingService" />
        ...
    </application>

### Generate and handle intents

Other apps, including Android Auto, can't obtain the `Intent` that triggers the
`MessagingService` because intents are passed to other apps through a
[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent). Due to this limitation, create a [`RemoteInput`](https://developer.android.com/reference/android/app/RemoteInput)
object to let other apps provide reply text to your app, as shown in the
following example:

    /**
     * Creates a [RemoteInput] that lets remote apps provide a response string
     * to the underlying [Intent] within a [PendingIntent].
     */
    fun createReplyRemoteInput(context: Context): RemoteInput {
        // RemoteInput.Builder accepts a single parameter: the key to use to store
        // the response in.
        return RemoteInput.Builder(REMOTE_INPUT_RESULT_KEY).build()
        // Note that the RemoteInput has no knowledge of the conversation. This is
        // because the data for the RemoteInput is bound to the reply Intent using
        // static methods in the RemoteInput class.
    }

    /** Creates an [Intent] that handles replying to the given [appConversation]. */
    fun createReplyIntent(
            context: Context, appConversation: YourAppConversation): Intent {
        // Creates the intent backed by the MessagingService.
        val intent = Intent(context, MessagingService::class.java)

        // Lets the MessagingService know this is a reply request.
        intent.action = ACTION_REPLY

        // Provides the ID of the conversation that the reply applies to.
        intent.putExtra(EXTRA_CONVERSATION_ID_KEY, appConversation.id)

        return intent
    }

In the `ACTION_REPLY` switch clause within the `MessagingService`, extract the
information that goes into the reply `Intent`, as shown in the following
example:

    ACTION_REPLY -> {
        // Extracts reply response from the intent using the same key that the
        // RemoteInput uses.
        val results: Bundle = RemoteInput.getResultsFromIntent(intent)
        val message = results.getString(REMOTE_INPUT_RESULT_KEY)

        // This conversation object comes from the MessagingService.
        conversation.reply(message)
    }

You handle the mark-as-read `Intent` in a similar way. However, it doesn't
require a `RemoteInput`, as shown in the following example:

    /** Creates an [Intent] that handles marking the [appConversation] as read. */
    fun createMarkAsReadIntent(
            context: Context, appConversation: YourAppConversation): Intent {
        val intent = Intent(context, MessagingService::class.java)
        intent.action = ACTION_MARK_AS_READ
        intent.putExtra(EXTRA_CONVERSATION_ID_KEY, appConversation.id)
        return intent
    }

The `ACTION_MARK_AS_READ` switch clause within the `MessagingService` requires
no further logic, as shown in the following example:

    // Marking as read has no other logic.
    ACTION_MARK_AS_READ -> conversation.markAsRead()

## Notify users of messages

Once conversation action handling is complete, the next step is to generate
Android Auto compliant notifications.

### Create actions

`Action` objects can be passed to other apps using a `Notification` to trigger
methods in the original app. This is how Android Auto can mark a conversation as
read or reply to it.

To create an `Action`, start with an `Intent`. The following example shows how
to create a "reply" `Intent` using the `createReplyIntent()` method from the
previous section:

    fun createReplyAction(
            context: Context, appConversation: YourAppConversation): Action {
        val replyIntent: Intent = createReplyIntent(context, appConversation)
        // ...

Then, wrap this `Intent` in a `PendingIntent`, which prepares it for external
app usage. A `PendingIntent` locks down all access to the wrapped `Intent` by
only exposing a select set of methods that let the receiving app fire the
`Intent` or get the originating app's package name. The external app can't
access the underlying `Intent` or the data within it.

        // ...
        val replyPendingIntent = PendingIntent.getService(
            context,
            createReplyId(appConversation), // Method explained later.
            replyIntent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_MUTABLE)
        // ...

| **Important:** Using [`PendingIntent.FLAG_MUTABLE`](https://developer.android.com/reference/android/app/PendingIntent#FLAG_MUTABLE) is necessary to allow Android Auto to update the `PendingIntent` with the `RemoteInput` contents.

Before you set up the reply `Action`, be aware that Android Auto has three
requirements for the reply `Action`:

- The semantic action must be set to [`Action.SEMANTIC_ACTION_REPLY`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action#SEMANTIC_ACTION_REPLY).
- The `Action` must indicate that it won't show any user interface when fired.
- The `Action` must contain a single `RemoteInput`.

The following code sample sets up a reply `Action` that addresses the
requirements listed previously:

        // ...
        val replyAction = Action.Builder(R.drawable.reply, "Reply", replyPendingIntent)
            // Provides context to what firing the Action does.
            .setSemanticAction(Action.SEMANTIC_ACTION_REPLY)

            // The action doesn't show any UI, as required by Android Auto.
            .setShowsUserInterface(false)

            // Don't forget the reply RemoteInput. Android Auto will use this to
            // make a system call that will add the response string into
            // the reply intent so it can be extracted by the messaging app.
            .addRemoteInput(createReplyRemoteInput(context))
            .build()

        return replyAction
    }

Handling the mark-as-read action is similar, except there's no `RemoteInput`.
Android Auto therefore has two requirements for the mark-as-read `Action`:

- The semantic action is set to [`Action.SEMANTIC_ACTION_MARK_AS_READ`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action#SEMANTIC_ACTION_MARK_AS_READ).
- The action indicates that it won't show any user interface when fired.

The following code sample sets up a mark-as-read `Action` that addresses these
requirements:

    fun createMarkAsReadAction(
            context: Context, appConversation: YourAppConversation): Action {
        val markAsReadIntent = createMarkAsReadIntent(context, appConversation)
        val markAsReadPendingIntent = PendingIntent.getService(
                context,
                createMarkAsReadId(appConversation), // Method explained later.
                markAsReadIntent,
                PendingIntent.FLAG_UPDATE_CURRENT  or PendingIntent.FLAG_IMMUTABLE)
        val markAsReadAction = Action.Builder(
                R.drawable.mark_as_read, "Mark as Read", markAsReadPendingIntent)
            .setSemanticAction(Action.SEMANTIC_ACTION_MARK_AS_READ)
            .setShowsUserInterface(false)
            .build()
        return markAsReadAction
    }

When you generate the pending intents, you use two methods: `createReplyId()` and `createMarkAsReadId()`. These methods serve as the request codes for each
`PendingIntent`, which are used by Android to control existing pending intents.
The `create()` methods *must* return unique IDs for each conversation, but
repeated calls for the same conversation must return the unique ID already
generated.

Consider an example with two conversations, A and B: Conversation A's reply ID
is 100, and its mark-as-read ID is 101. Conversation B's reply ID is 102, and
its mark-as-read ID is 103. If conversation A is updated, the reply and
mark-as-read IDs are still 100 and 101. For more information, see
[`PendingIntent.FLAG_UPDATE_CURRENT`](https://developer.android.com/reference/android/app/PendingIntent#FLAG_UPDATE_CURRENT).

### Create a MessagingStyle

`MessagingStyle` is the carrier of the messaging information and is what Android
Auto uses to read aloud each message in a conversation.

First, you must specify the user of the device as a [`Person`](https://developer.android.com/reference/androidx/core/app/Person) object, as
shown in the following example:

    fun createMessagingStyle(
            context: Context, appConversation: YourAppConversation): MessagingStyle {
        // Method defined by the messaging app.
        val appDeviceUser: YourAppUser = getAppDeviceUser()

        val devicePerson = Person.Builder()
            // The display name (also the name that's read aloud in Android auto).
            .setName(appDeviceUser.name)

            // The icon to show in the notification shade in the system UI (outside
            // of Android Auto).
            .setIcon(appDeviceUser.icon)

            // A unique key in case there are multiple people in this conversation with
            // the same name.
            .setKey(appDeviceUser.id)
            .build()
        // ...

You can then construct the `MessagingStyle` object and provide some details
about the conversation.

        // ...
        val messagingStyle = MessagingStyle(devicePerson)

        // Sets the conversation title. If the app's target version is lower
        // than P, this will automatically mark the conversation as a group (to
        // maintain backward compatibility). Use `setGroupConversation` after
        // setting the conversation title to explicitly override this behavior. See
        // the documentation for more information.
        messagingStyle.setConversationTitle(appConversation.title)

        // Group conversation means there is more than 1 recipient, so set it as such.
        messagingStyle.setGroupConversation(appConversation.recipients.size > 1)
        // ...

Finally, add the unread messages.

        // ...
        for (appMessage in appConversation.getUnreadMessages()) {
            // The sender is also represented using a Person object.
            val senderPerson = Person.Builder()
                .setName(appMessage.sender.name)
                .setIcon(appMessage.sender.icon)
                .setKey(appMessage.sender.id)
                .build()

            // Adds the message. More complex messages, like images,
            // can be created and added by instantiating the MessagingStyle.Message
            // class directly. See documentation for details.
            messagingStyle.addMessage(
                    appMessage.body, appMessage.timeReceived, senderPerson)
        }

        return messagingStyle
    }

### Package and push the notification

After generating the `Action` and `MessagingStyle` objects, you can construct
and post the `Notification`.

    fun notify(context: Context, appConversation: YourAppConversation) {
        // Creates the actions and MessagingStyle.
        val replyAction = createReplyAction(context, appConversation)
        val markAsReadAction = createMarkAsReadAction(context, appConversation)
        val messagingStyle = createMessagingStyle(context, appConversation)

        // Creates the notification.
        val notification = NotificationCompat.Builder(context, channel)
            // A required field for the Android UI.
            .setSmallIcon(R.drawable.notification_icon)

            // Shows in Android Auto as the conversation image.
            .setLargeIcon(appConversation.icon)

            // Adds MessagingStyle.
            .setStyle(messagingStyle)

            // Adds reply action.
            .addAction(replyAction)

            // Makes the mark-as-read action invisible, so it doesn't appear
            // in the Android UI but the app satisfies Android Auto's
            // mark-as-read Action requirement. Both required actions can be made
            // visible or invisible; it is a stylistic choice.
            .addInvisibleAction(markAsReadAction)

            .build()

        // Posts the notification for the user to see.
        val notificationManagerCompat = NotificationManagerCompat.from(context)
        notificationManagerCompat.notify(appConversation.id, notification)
    }

## Additional resources

- [Google Design for Driving: Messaging apps](https://developers.google.com/cars/design/android-auto/apps/voice-messaging)
- [Notifications overview](https://developer.android.com/guide/topics/ui/notifiers/notifications)

## Report an Android Auto messaging notification issue

If you run into an issue while developing your messaging notifications for
Android Auto, you can report it using the [Google Issue Tracker](https://issuetracker.google.com/issues?q=status:open+componentid:192643). Be sure to
fill out all the requested information in the issue template.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192643)

Before filing a new issue, check whether it is already reported in the issues
list. You can subscribe and vote for issues by clicking the star for an issue in
the tracker. For more information, see [Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).