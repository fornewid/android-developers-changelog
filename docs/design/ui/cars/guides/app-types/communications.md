---
title: https://developer.android.com/design/ui/cars/guides/app-types/communications
url: https://developer.android.com/design/ui/cars/guides/app-types/communications
source: md.txt
---

# Communication apps

Create messaging and calling experiences for Android Auto that drivers can control using either their car screen or their voice.

From basic notification-powered messaging experiences to richer messaging and calling experiences built using the templates from the Android for Cars App Library,[communication apps](https://developer.android.com/training/cars/communication)provide a variety of ways to help drivers stay connected while focusing on the road.
![Communication apps](https://developer.android.com/static/images/design/ui/cars/app-cuj/communications.png)Example of communication apps in Android Auto.

## Calling

The Android for Cars App Library lets you create apps with lists or grids of contacts that users can tap to initiate calls. Calls are smoothly integrated with the Android Auto calling experience using the[CallsManager APIs](https://developer.android.com/reference/androidx/core/telecom/CallsManager).

The in-call screen is provided by Android Auto with limited customization options.

For technical details, see[Build calling experiences for Android Auto](https://developer.android.com/training/cars/communication/calling).

**Note:** Calling experiences for communication apps are in beta, and can only be distributed to internal testing and closed testing tracks on the Play Store. To distribute your app more widely, you can[express interest in becoming an early access partner](https://forms.gle/VsXEdDEBidxw8q8u8).

Templates especially relevant for calling apps include:

- Sectioned item template
- Grid template
- List template
- Sign-in template
- Tab template

## Messaging

Android Auto's messaging experience consists of messaging notifications and in-app conversation history. Your app can post incoming message notifications, and users can choose when to respond. Your app can also implement templates for users to read and reply to conversations in your app. Options to play the message aloud and dictate an answer make it easier for users to respond while driving.

### Messaging notifications

Because the UI already exists within Android Auto, there is no UI work needed on the app end. The only design considerations relate to:

- **App icon:**Supply an app icon that will be easy for users to identify at a small size, in a badge on a notification.
- **Message ordering:**Make sure your app's messages are appropriately grouped and sequentially ordered.

See[Extend messaging notifications to Android Auto](https://developer.android.com/training/cars/communication/notification-messaging)to learn more.

### Templated messaging

Messaging apps can use the Android for Cars App Library to go beyond their notification-powered experience. This lets you create apps with lists of conversations. These conversations should match what a user sees in your mobile app experience, so they can easily find, read, and reply to those conversations. Unlike other templates, Conversation Item templates have less flexibility, and require specific pieces of information to be provided. With this, users will be able to easily read and reply to conversations using the Google Assistant.

See[Build templated messaging experiences for Android Auto](https://developer.android.com/training/cars/communication/templated-messaging)to learn more.

**Note:** Templated messaging experiences for communication apps are in beta, and can only be distributed to internal testing and closed testing tracks on the Play Store. To distribute your app more widely, you can[express interest in becoming an early access partner](https://forms.gle/VsXEdDEBidxw8q8u8).