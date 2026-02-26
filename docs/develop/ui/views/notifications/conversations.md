---
title: https://developer.android.com/develop/ui/views/notifications/conversations
url: https://developer.android.com/develop/ui/views/notifications/conversations
source: md.txt
---

The people and conversations initiative is a multi-year Android initiative that
aims to elevate people and conversations in the system surfaces of the phone.
This priority is based on the fact that communication and interaction with other
people is still the most valued and important functional area for the majority
of our users across all demographics.

A number of features were introduced in Android 11 to support
the people and conversations initiative.

## Conversation space

<iframe width="560" height="315" src="https://www.youtube.com/embed/CKlVSvFyt3s" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br />

![The conversation space is a dedicated notification area for real-time
conversations between humans.](https://developer.android.com/static/images/guide/topics/ui/conversations-conv-space.png) **Figure 1**: The conversations space.

On handheld devices, there is a separate section on top of the notification
shade containing only real-time conversations with people (such as calls and
chat messages, including group chats). Notifications in this space
look and act differently from non-conversation notifications on many phones:

- The design is different, with a strong emphasis on the avatar representing people combined with the app carrying the conversation.
- A tap on the notification opens the conversation in the app (or [bubble](https://developer.android.com/guide/topics/ui/bubbles), if the conversation was previously bubbled), and a tap on the caret expands the new messages in the shade to full length with the full list of options.
- Conversation-specific actions are offered (some by long-pressing):
  - Mark this conversation as priority
  - Promote this conversation to bubble (only shown if the app supports bubbles)
  - Silence notifications for this conversation
  - Set custom sounds or vibrations for this conversation

## Conversations in Bubbles

![If a notification meets the conversation requirements, the platform
launches it as a bubble from the notification drawer.](https://developer.android.com/static/images/guide/topics/ui/conversations-bubble.gif) **Figure 2**: Notification being launched as a bubble from the notification drawer.

Beginning in Android 11,
[Bubbles](https://developer.android.com/guide/topics/ui/bubbles) can be
started from notifications in the Conversations section. Only notifications with
an associated shortcut are able to bubble. Conversations bubble automatically
if they are marked as important or are triggered to bubble in the notification
shade.

## Conversation Shortcuts

Shortcuts to conversations appear in the launcher and alongside
[long-lived](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived(boolean)),
[sharing shortcuts](https://developer.android.com/training/sharing/direct-share-targets) in the sharesheet.

## API guidelines

This section describes the APIs to add support in your app for the
system-provided space that shows people and conversations.

### Shortcuts for Conversations

In order to participate in this conversation-centric initiative, apps need
to provide the system with
[long-lived](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived(boolean))
shortcuts. We strongly recommend using long-lived
[sharing shortcuts](https://developer.android.com/training/sharing/direct-share-targets). If
necessary, you can use [dynamic
shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#dynamic) in
Android 11, but we may remove this option in the future.

To publish a [shortcut](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat) to the
conversation, call the
[`ShortcutManagerCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat) methods
[`setDynamicShortcuts()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#setDynamicShortcuts(android.content.Context,%20java.util.List%3Candroidx.core.content.pm.ShortcutInfoCompat%3E)),
[`addDynamicShortcuts()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#addDynamicShortcuts(android.content.Context,%20java.util.List%3Candroidx.core.content.pm.ShortcutInfoCompat%3E)),
or [`pushDynamicShortcut()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,%20androidx.core.content.pm.ShortcutInfoCompat))
(which automatically manages the shortcut limit for the developer). This shortcut must be
[long-lived](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived(boolean))
and have [`Person`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setPerson(androidx.core.app.Person))
data attached for one or more persons, identifying the other participants in the
conversation. We also recommend that you set the [`LocusIdCompat`](https://developer.android.com/develop/ui/views/notifications/conversations#api-in-app).

If a conversation no longer exists, the app can delete the shortcut with
[`removeLongLivedShortcuts()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#removeLongLivedShortcuts(android.content.Context,%20java.util.List%3Cjava.lang.String%3E));
doing so causes the system to delete all data associated with the conversation.
Although shortcuts are removable, apps **shouldn't remove cached shortcuts**
unless absolutely necessary; a shortcut is probably cached because the user
interacted with it to change their experience, and removing the shortcut will
undo those changes, leading to user frustration.

> [!NOTE]
> **Note:** If removing a cached shortcut removes a person-specific conversation notification channel, the deleted category count in **Settings** is incremented.

### Conversation Notifications

A notification is considered as a conversation notification if the following are true:

- The notification uses [`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle).

- **(Only if the app targets Android 11 or higher)** The
  notification is associated with a valid
  [long-lived](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived(boolean))
  dynamic or cached sharing shortcut. The notification can set this association by calling
  [`setShortcutId()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setShortcutId(java.lang.String))
  or [`setShortcutInfo()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setShortcutInfo(androidx.core.content.pm.ShortcutInfoCompat)).
  If the app targets Android 10 or lower, the notification doesn't
  have to be associated with a shortcut, as discussed in the
  [fallback options](https://developer.android.com/develop/ui/views/notifications/conversations#non-11) section.

- The user hasn't demoted the conversation from the conversation section via
  notification channel settings, at the time of posting.

### Use LocusIdCompat

On-device intelligence determines the conversations that the user is most likely
to be interested in. Among the most important signals are *recency* and
*frequency* of conversation sessions in each conversation. The system knows
about interactions with a conversation from Launcher shortcuts or within a
notification if they are properly tagged. However, the system doesn't know
about conversations that happened fully in the app unless those interactions are
also tagged. Thus, we strongly recommend that you [attach a `LocusIdCompat` to the
shortcut](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLocusId(androidx.core.content.LocusIdCompat))
and annotate the in-app activity or fragment with the
associated [`LocusIdCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLocusId(androidx.core.content.LocusIdCompat)). Use `LocusIdCompat`
to enable the suggestion system to properly rank the conversation, and to enable
the system to display the correct time of the user's last interaction (including
in-app interactions) with a conversation. If you use
[`setShortcutInfo()`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setShortcutInfo(androidx.core.content.pm.ShortcutInfoCompat))
to associate the conversation with a shortcut, the conversations system
automatically attaches the appropriate `LocusIdCompat`.

## Conversation space requirements for apps that target Android 10 or lower

If an app doesn't target Android 11, its messages can still be
surfaced in the conversation space. However, the app still must meet certain
requirements. This section describes the requirements for those apps, and the
fallback behavior if the app doesn't meet the requirements.

> [!NOTE]
> **Note:** If the app targets Android 11 or higher, it must follow the requirements described in [API guidelines](https://developer.android.com/develop/ui/views/notifications/conversations#api-guidelines) to have its messages appear in the conversation space.

The core requirement for participation in the messaging space is, the app must
implement [`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle)
notifications, and the notifications must reference
a **long-lived shortcut** from the notification that is published at the
time the notification is posted. Notifications that meet these requirements
appear in the conversation space with this behavior:

- Notification is displayed in **conversation style**
- **Bubble** button is offered, if implemented
- **Conversation specific** **functions** are offered inline

If the notification doesn't meet these requirements, the platform uses fallback
options to format the notification. If a notification meets the requirements of
either fallback case, the notification is displayed in the conversation space
with special formatting. If the notification doesn't qualify for either
fallback option, it isn't displayed in the conversation space.

### Fallback: If MessagingStyle is used but no shortcut is provided

If the app targets Android 10 or lower and a notification uses
[`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle)
but does *not* associate the message with a shortcut, the notification
is shown in the conversation space with this behavior:

- Notification is displayed in **conversation style**
- **No bubble button** is offered
- **No conversation-specific functions** are offered inline

### Fallback: If MessagingStyle isn't used, but the app is a recognized messaging app

If a notification doesn't use
[`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle)
but the app is recognized by the platform as a messaging app, and the notification's
[`category`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setcategory)
parameter is set to
[`msg`](https://developer.android.com/reference/androidx/core/app/NotificationCompat#CATEGORY_MESSAGE),
the notification is shown in the conversation space with this behavior:

- Notification is displayed in **old, pre-Android 11 style**
- **No bubble button** is offered
- **No conversation-specific functions** are offered inline

## Guidance, usage, and testing

This section provides general guidance on how to use and test the conversation features.

### When should I use conversations?

Conversation Notifications and related shortcuts are intended to improve the
user experience of **real-time conversations**. For example, SMS, text chats,
and phone calls are real-time conversations where users expect to communicate
quickly. Users don't have that expectation with emails and activities unrelated
to conversations.

We've given users the ability to remove a given conversation from the
conversation section if they don't feel it's in the right space.

### Best practices

To increase engagement and make it easier for your users to interact with people
and conversations around your app, we recommend the following best practices.

- To ensure that missed calls are surfaced in the prioritized conversation shade and appear correctly in the [conversion widget](https://developer.android.com/develop/ui/views/notifications/conversations#conversation-widgets), format missed call notifications as [`conversations`](https://developer.android.com/guide/topics/ui/conversations) with a category set to [`CATEGORY_MISSED_CALL`](https://developer.android.com/reference/android/app/Notification#CATEGORY_MISSED_CALL).
- Provide high-quality avatars (104dp) for users; otherwise, the system uses the person's initials, which is a less engaging experience.
- Don't [`cancel`](https://developer.android.com/reference/android/app/NotificationManager#cancel(int)) a conversation notification before the user has not seen the message. One example of this is canceling a notification when opening the app in a view where the user can't see or address the message. If the user isn't given the opportunity to read or address the message, a canceled notification and its associated bubble are removed, resulting in the loss of conversation context.
- Provide a [`data`](https://developer.android.com/reference/android/app/Notification.MessagingStyle.Message#setData(java.lang.String,%20android.net.Uri)) URI for MIME-related metadata associated with messages, which gives you the option of providing a richer experience in notifications.
- Use the [`Android 12 status`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setIsConversation()) API to make [conversation widgets](https://developer.android.com/develop/ui/views/notifications/conversations#conversation-widgets) more engaging.
- Adopt the following best practices for [conversation shortcuts](https://developer.android.com/guide/topics/ui/conversations#shortcuts).
  - Publish shortcuts for incoming and outgoing in-app conversations that do not push notifications. Incoming and outgoing messages for the same conversation should have the same shortcut ID. Use [`pushDynamicShortcut()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,%20androidx.core.content.pm.ShortcutInfoCompat)) to publish your shortcuts and report usage.
  - To avoid unintentional clipping of your shortcut avatar, provide an [`AdaptiveIconDrawable`](https://developer.android.com/reference/android/graphics/drawable/AdaptiveIconDrawable) for the shortcut's icon. See [Providing shortcut imagery](https://developer.android.com/training/sharing/receive#providing-shortcut-imagery) for more details.
  - To help the system promote your shortcut, follow [guidelines for getting the best ranking](https://developer.android.com/training/sharing/receive#get-best-ranking). Your shortcut is ranked in different system surfaces, including the Android sharesheet if it's a sharing shortcut.
  - Ensure that conversation shortcuts [`intents`](https://developer.android.com/reference/android/content/pm/ShortcutInfo.Builder#setIntent(android.content.Intent)) launch directly into the applicable conversation.
  - Use the compat libs to conveniently set your shortcuts as [`conversation`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setIsConversation()) related.

### Testing Conversation Notifications and shortcuts

![Long-pressing on a conversation opens a menu of
conversation-related actions.](https://developer.android.com/static/images/guide/topics/ui/conversations-testing.png) **Figure 3**: You can verify that a conversation notification is properly configured by long-pressing on it and checking that the conversation menu appears.

If you follow the conversation space [guidelines](https://developer.android.com/develop/ui/views/notifications/conversations#api-notifications),
conversations should automatically appear in the **conversation space**.
You can verify that the shortcut is properly integrated by long-pressing
on the notification. If the integration is done properly, the UI shows
conversation-related actions. If the notification isn't linked to a shortcut,
the UI shows text stating that the app doesn't support conversation features.

[Added shortcuts](https://developer.android.com/develop/ui/views/notifications/conversations#api-shortcuts) display on a long-press on the app launcher.
Be sure to test that the shortcuts take you to the correct place within your
app.

[Added sharing shortcuts](https://developer.android.com/training/sharing/direct-share-targets)
are shown in the sharesheet's direct share row when sharing content that
your sharing shortcut can receive.

### Conversation Widgets

![Conversations displayed in Conversation widgets](https://developer.android.com/static/images/guide/topics/ui/conversation-widgets.png) **Figure 1**: Conversations displayed in Conversation widgets.

In Android 12, the Conversation Widget feature builds on the people and
conversations feature [introduced in Android 11](https://developer.android.com/guide/topics/ui/conversations)
by allowing apps to display conversation status in Conversation widgets.

Conversation widgets promote user interaction by allowing them to easily open
chats on the home screen. These widgets are enhanced shortcuts that allow users
to efficiently get back to their conversations while showing snippets of their
conversation status or other relevant information.

#### Validate that your app supports conversation widgets

To validate that your app supports conversation widgets, you need to have at
least two Android devices (both running Android 12) and two user accounts
(one on each device) to exchange messages. For the purposes of this procedure,
we'll call the accounts "user A" and "user B."
![Widget picker UI to add a new conversation widget](https://developer.android.com/static/images/guide/topics/ui/widget-picker-conversation.png) **Figure 2**: Widget picker UI to add a new conversation widget.

Complete the following steps:

1. On user A's device, long-press on the launcher. In the widget picker, tap a new widget for a conversation as shown in figure 2.
2. Drag the widget to the home screen. A list of active or recent conversations from user A's app should be selectable.
3. Now, on user B's device, send a test message to user A.
4. Back on user A's device, verify that the widget is updated to reflect the notification of the message from user B.
5. Optional: have both user A and user B set the conversation to different status values to ensure that their widgets properly reflect them. For a list of status values, see [ConversationStatus](https://developer.android.com/reference/kotlin/android/app/people/ConversationStatus).