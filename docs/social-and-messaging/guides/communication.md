---
title: About messaging and communication  |  Android social  |  Android Developers
url: https://developer.android.com/social-and-messaging/guides/communication
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Social & Messaging Dev Center](https://developer.android.com/social-and-messaging)
* [Guides](https://developer.android.com/social-and-messaging/guides)

# About messaging and communication Stay organized with collections Save and categorize content based on your preferences.




Communication is a critical part of social and messaging apps, and Android
continues to evolve APIs and services to make the user experience more
integrated and consistent. This page connects you to resources to both help you
get started and level up your app experiences.

## Know key Android messaging APIs and concepts

Because messaging is such a critical task for users, Android has created bespoke
APIs that you should know about to help make messaging more integrated and
efficient.

### Make the most of Android's messaging surfaces

Android has a built-in concept of people and conversations that provides more
surfaces for your app to interact with users. Examples of this include:

* A dedicated [notification area](/develop/ui/views/notifications/conversations) for chats
* [Bubbles](/develop/ui/views/notifications/conversations#bubbles) with people avatars for ongoing conversations
* [Launcher shortcuts](/develop/ui/views/notifications/conversations#api-shortcuts) for quick access to chats

### Receive messages in the background reliably

[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) ensures messages are sent and received
reliably, while minimizing the use of system resources, offering a robust
backend for real-time 1:1 and group chats.

The [full guide for receiving messages reliably](/social-and-messaging/guides/communication/receiving-messages) includes detail on how to
best handle real-time messages in the foreground, in the background, and how to
enhance delivery reliability.

## Level up your app

You'll want your app to support features that meet and surpass user
expectations. Messaging often includes embedded media support, so you might want
your app to include [media capture](/media/camera/camerax) and [playback](/media/media3/exoplayer). Other ways to help
your app stand out include:

* Rich emoji support through the [Emoji Picker](/develop/ui/views/text-and-emoji/emoji-picker)
* Support for [rich content](/develop/ui/views/receive-rich-content), including stickers and images through Android's
  Image Keyboard
* Support for browsing and selecting user photos and videos, either local or in
  the cloud, using Android's built-in [photo picker](/training/data-storage/shared/photopicker)
* Support for [sharing text and media](/training/sharing/send) directly to other apps and contacts

See the [full guide](/social-and-messaging/guides/communication/basic-better-best) for features to consider to take your social and
messaging experience to the next level, to help your app meet and surpass user
expectations.