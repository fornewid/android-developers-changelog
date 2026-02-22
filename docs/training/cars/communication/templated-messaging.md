---
title: https://developer.android.com/training/cars/communication/templated-messaging
url: https://developer.android.com/training/cars/communication/templated-messaging
source: md.txt
---

Templated messaging experiences are in beta At this time, anyone can publish communication apps with templated messaging experiences to internal testing and closed testing tracks on the Play Store. Publishing to open testing and production tracks will be permitted at a later date. [Nominate yourself to be an early access partner →](https://forms.gle/VsXEdDEBidxw8q8u8) ![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

In addition to the basic notification-powered messaging experience for reading
and replying to messages, Android Auto supports richer messaging experiences
built using the [Android for Cars App Library](https://developer.android.com/training/cars/apps).

## Support notification-powered messaging experiences

All apps that support templated messaging experiences must also [extend
messaging notifications for Android Auto](https://developer.android.com/training/cars/communication/notification-messaging). This
integration allows users to read and reply to messages without having to open
the templated app.

## Build a templated messaging experience

Follow the guidance in [Use the Android for Cars App Library](https://developer.android.com/training/cars/apps) and [Add
support for Android Auto to your templated app](https://developer.android.com/training/cars/apps/auto) to get started
building your app's templated experience. Then, refer to the guidance on this
page to understand the specific requirements for templated messaging apps.

### Configure your app's manifest files

To inform Android Auto of your app's capabilities, your app must do the
following:

#### Declare category support in your manifest

Your app needs to declare the `androidx.car.app.category.MESSAGING` [car app
category](https://developer.android.com/training/cars/apps#supported-app-categories) in the intent filter of its
[`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService).

    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.MESSAGING"/>
          </intent-filter>
        </service>
        ...
    <application>

| **Note:** If your app supports both messaging and [calling](https://developer.android.com/training/cars/communication/calling), include both `androidx.car.app.category.CALLING` and `androidx.car.app.category.MESSAGING` `<category>` elements in the same intent filter.

#### Set the minimum car app API level

Because the [`ConversationItem`](https://developer.android.com/reference/androidx/car/app/messaging/model/ConversationItem) API is only supported on Car
API 7 or higher, you should also set the `minCarApiLevel` metadata to that
value. See [Car App API Level](https://developer.android.com/training/cars/apps#api-level) for more information.

    <application ...>
        ...
        <meta-data
            android:name="androidx.car.app.minCarApiLevel"
            android:value="7"/>
        ...
    </application>

#### Declare Android Auto support

In the `automotive_app_desc.xml` file that you use to [declare Android Auto
support](https://developer.android.com/training/cars/apps/auto#declare-android-auto-support), verify that both the `notification` and
`template` capabilities are declared:

    <automotiveApp>
        <uses name="notification" />
        <uses name="template" />
    </automotiveApp>

If your app can be set as the [default SMS handler](https://developer.android.com/reference/android/provider/Telephony#creating-an-sms-app),
make sure to include the following `<uses>` element. If you don't, a default
handler built-in to Android Auto will be used to handle incoming SMS/MMS
messages, which can lead to duplicate notifications.

    <automotiveApp>
        ...
        <uses name="sms" />
    </automotiveApp>

### Display conversations

To display an overview of a user's conversations, you can display a list of
[`ConversationItem`](https://developer.android.com/reference/androidx/car/app/messaging/model/ConversationItem) objects in a
[`ListTemplate`](https://developer.android.com/reference/androidx/car/app/model/ListTemplate) or
[`SectionedItemTemplate`](https://developer.android.com/reference/androidx/car/app/model/SectionedItemTemplate).

For a good user experience, we recommend providing at most the 5-10 most
recent or most important conversations, with no more than the 5 most recent
messages for each conversation. This helps improve loading performance, lets
users see the most relevant content, and reduces interaction time.

    class MyMessagingScreen() : Screen() {

        override fun onGetTemplate(): Template {
            val itemListBuilder = ItemList.Builder()
            val conversations: List<MyConversation> = // Retrieve conversations

            for (conversation: MyConversation in conversations) {
                val carMessages: List<CarMessage> = conversation.getMessages()
                    .map { message ->
                        // CarMessage supports additional fields such as MIME type and URI,
                        // which you should set if available
                        CarMessage.Builder()
                            .setSender(message.sender)
                            .setBody(message.body)
                            .setReceivedTimeEpochMillis(message.receivedTimeEpochMillis)
                            .setRead(message.isRead)
                            .build()
                    }

                itemListBuilder.addItem(
                    ConversationItem.Builder()
                        .setConversationCallback { /* Implement your conversation callback logic here */ }
                        .setId(/* Set conversation ID */)
                        .setTitle(/* Set conversation title */)
                        .setIcon(/* Set conversation icon if available */)
                        .setMessages(carMessages)
                        /* When the sender of a CarMessage is equal to this Person,
                        message readout is adjusted to "you said" instead of "<person>
                        said" */
                        .setSelf(/* Set self-sender */)
                        .setGroupConversation(/* Set if the message contains more than 2 participants */)
                        .build()
                )
            }

            return ListTemplate.Builder()
                .setTitle("Conversations")
                .setHeaderAction(Action.APP_ICON)
                .setSingleList(itemListBuilder.build())
                .build()
        }
    }

Each `ConversationItem` automatically displays actions for playing a message
and marking it as read as and for replying. Those actions are handled by the
[`ConversationCallbackDelegate`](https://developer.android.com/reference/androidx/car/app/messaging/model/ConversationCallbackDelegate) you supply when
building the `ConversationItem`.
| **Tip:** You can re-use the logic for marking messages as read and replying that enables your app's notification-powered experience.

If your app provides [conversation shortcuts](https://developer.android.com/develop/ui/views/notifications/conversations#api-shortcuts), verify
that the ID provided when building the `ConversationItem` is the same as the
ID for that conversation's shortcut.

#### Update conversations

As users send and receive messages, you should refresh your app's screens to
include the new messages by calling [`invalidate()`](https://developer.android.com/reference/androidx/car/app/Screen#invalidate()). See [Refresh
the contents of a template](https://developer.android.com/training/cars/apps#refresh-template).

For the best user experience, we recommend keeping refresh times to 500
milliseconds or fewer. If refreshing frequently takes longer, you can display a
loading state while you load the incoming messages.

#### Set notification importance appropriately

To reduce distractions, your app should lower the importance of incoming
notifications when a user is using your viewing a corresponding conversation
so the notifications don't appear as heads up notifications (HUNs).

You can track if a conversation is visible by observing the lifecycle of the
`Screen` that displays it. See [The lifecycle of a screen](https://developer.android.com/training/cars/apps#screen-lifecycle).

To prevent a notification from appearing as a HUN, set the priority to
[`IMPORTANCE_DEFAULT`](https://developer.android.com/reference/androidx/core/app/NotificationManagerCompat#IMPORTANCE_DEFAULT) or lower.

## Distribute templated messaging apps

Because apps that support templated messaging experiences can only be published
to Internal Testing and Closed Testing tracks on Google Play, you shouldn't
promote builds that include support to Open Testing or Production tracks, as
submissions containing builds on those tracks will be rejected.