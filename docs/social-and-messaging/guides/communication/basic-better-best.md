---
title: https://developer.android.com/social-and-messaging/guides/communication/basic-better-best
url: https://developer.android.com/social-and-messaging/guides/communication/basic-better-best
source: md.txt
---

# Take your messaging to the next level — basic, better, and best

This document charts the optimal progression of a messaging app from a likely
starting place to best-in-class. It's designed to help you think about scaling
your app over time, and what features to implement when. While every media app
is different, consider these recommendations to achieve a best-in-class app.

## Basic messaging app

A basic messaging app provides users with a foundational text-based
communications experience, which may include:

- **Offline message support**   

  Ensure messages can be queued when offline, with strategies for local caching
  and retry attempts. UI cues such as 'sending...' or 'failed to send' indicators
  help manage user expectations.

  - [Save data in a local database using Room](https://developer.android.com/training/data-storage/room).
  - [Run background tasks using WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started).
- **Error handling**   

  Offer clear, informative feedback for different failure scenarios, like network
  issues or blocked recipients. Include actionable steps or explanations to reduce
  user frustration.

- **Notifications**   

  Provide notifications when messages are received in the background.

  - [Work with the Notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission).
  - [Create and manage notification channels](https://developer.android.com/develop/ui/views/notifications/channels).
- **Firebase Cloud Messaging (FCM)**   

  Leverage [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) to notify the app of new
  messages.

- **Spellcheck**   

  [Implement and access spell checking](https://developer.android.com/develop/ui/views/touch-and-input/spell-checker-framework#SpellCheckClient) in your app.

- **Accessibility**   

  [Follow Material Design guidelines to design and develop your app for
  accessibility](https://developer.android.com/guide/topics/ui/accessibility).

- **Sharing**

  - [Use the Android Sharesheet to share data and content with other apps and
    targets](https://developer.android.com/training/sharing/send#why-to-use-system-sharesheet).
  - [Support receiving](https://developer.android.com/develop/ui/views/touch-and-input/spell-checker-framework#SpellCheckClient) data and content [from other apps](https://developer.android.com/training/sharing/receive).

## Better messaging app

A better messaging app gives users more tools to enhance their communication and
provide self-expression, including:

- **Emoji**   

  Support [modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2).

- **Push notifications with Intent**   

  Use payloads with Firebase Cloud Messaging (FCM) to [direct users to specific
  conversations or sections of the app](https://developer.android.com/develop/ui/views/notifications/navigation) from the notification. This reduces
  the steps users have to take to reach important content. ()

- **Threaded conversations**   

  Implement replies to specific messages within group chats to maintain the
  context and flow of conversations. This feature is crucial for keeping group
  communications organized and understandable.

- **Image keyboards, drag and drop, and other rich content**   

  Receive [rich content](https://developer.android.com/develop/ui/views/receive-rich-content) such as images, videos, and audio files. The
  API includes support for image keyboards and being a drag-and-drop target
  to make it easy for users to add stickers, animations, and other media to
  their messages. Also, make sure your app works as a [drag-and-drop source](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop)
  to share content with other apps.

- **Search in conversations**   

  Enable [full-text search](https://developer.android.com/develop/ui/views/search/training/search) within conversations so that users can quickly
  find messages, images, links, and files. Support filtering by date, person, or
  type of content for efficient searching.

- **Media and file support**   

  Integrate seamless support for [sending and receiving images](https://developer.android.com/training/data-storage/shared/photopicker), videos,
  documents, and other files with inline previews and clear indicators for
  download and upload statuses.

- **Notifications**

  - [Wait to show the notification permission](https://developer.android.com/develop/ui/views/notifications/notification-permission#wait-to-show-prompt) until the user is familiar with your app. Trigger the permission from a user action if possible.
  - Support [notification badges](https://developer.android.com/develop/ui/views/notifications/badges).
  - Support [direct replies](https://developer.android.com/develop/ui/views/notifications/build-notification#reply-action) in notifications.
  - Make thoughtful use of [notification channels](https://developer.android.com/develop/ui/views/notifications/channels), potentially including custom [importance level](https://developer.android.com/develop/ui/views/notifications/channels#importance) and notification behaviors for notification channels.
  - Support [conversation notifications](https://developer.android.com/develop/ui/views/notifications/conversations#api-notifications) with [long-lived shortcuts](https://developer.android.com/develop/ui/views/notifications/conversations#api-shortcuts) so users can add people and group shortcuts to their homescreens.
- **Advanced Firebase Cloud Messaging (FCM)**   

  Make use of advanced [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) features such as
  data payloads to minimize latency and expensive server round trips.

- **Read receipts**   

  Provide the option for users to manage the visibility of read receipts. This
  could be a simple toggle in the settings, allowing users to choose privacy over
  acknowledgment.

## Best messaging app

The best messaging app builds on the previous recommendations to create a
seamless multidevice experience for users, along with more advanced expressive
capabilities, including:

- **Emoji picker**   

  Support the [emoji picker](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-picker).

- **Simplified login**   

  Invest in seamless identity across surfaces using [CredentialManager](https://developer.android.com/training/sign-in/passkeys) with
  either [Passkeys](https://developer.android.com/training/sign-in/passkeys#about-passkeys) or [federated sign-in](https://developer.android.com/training/sign-in/credential-manager).

- **End-to-end encryption**   

  Implement industry-standard encryption protocols to ensure that messages are
  secure and only readable by the intended recipient.

- **Add and edit rich content**   

  Add and edit [rich content](https://developer.android.com/training/sharing/send#adding-rich-content-previews) to text previews when sharing.

- **Synchronization across devices**   

  Enable users to access their conversations cohesively across multiple devices,
  ensuring that their communication experience is seamless, whether they're on
  their phone, tablet, or computer.

  Check out the [codelab to create a chat app with Firebase Realtime
  Database](https://firebase.google.com/codelabs/firebase-android).
- **Message reactions**   

  Allow users to react to messages with emoji or custom graphics, providing a
  quick and fun way to respond without typing out a message.

- **Message editing and deletion**   

  Give users control over their messages after sending, including editing and
  deletion within a specified time frame.

- **Customizable notifications**   

  Offer detailed customization options for notifications, including sounds,
  vibration patterns, and LED colors, on a per-conversation or per-contact basis.
  Check out
  [Create a custom notification layout](https://developer.android.com/develop/ui/views/notifications/custom-notification).

- **Conversation bubbles**   

  Support [bubbles for conversations](https://developer.android.com/develop/ui/views/notifications/bubbles).

- **Direct share targets**   

  Provide [direct share targets](https://developer.android.com/training/sharing/direct-share-targets) to allow your users to share directly with
  contacts within your app.

- **Animate the software keyboard**   

  [Control and animate the software keyboard](https://developer.android.com/develop/ui/views/layout/sw-keyboard) for extra polish.

- **Voice and video chat**   

  Incorporate high-quality, real-time voice and video communication capabilities.
  The [Jetpack Telecom Library](https://android-developers.googleblog.com/2023/11/alpha-release-of-telecom-library.html) includes helpful features like dedicated
  foreground service support, audio routing, and cross-device capabilities between
  phones, watches, cars, and more, while technologies like WebRTC can provide
  peer-to-peer connectivity.

- **Wear OS app**   

  Build a [Wear OS app](https://developer.android.com/wear/gallery/messaging) to help people stay connected from their smartwatch.