---
title: https://developer.android.com/social-and-messaging/guides/communication/receiving-messages
url: https://developer.android.com/social-and-messaging/guides/communication/receiving-messages
source: md.txt
---

# Receive messages reliably

Receiving messages reliably is the most critical feature of any Android messaging experience. It's also important to implement messaging with an eye on system health and battery life. This document guides you through the key strategies and tools to ensure your Android app receives messages consistently, efficiently, and reliably.

## Message delivery mechanisms

The best approach for reliable messaging depends on your app's specific requirements. Consider factors like:

- Current real-time needs
- Message frequency
- Battery constraints

### Foreground real-time messaging

When your app is in the foreground, the user typically expects a reasonably high volume of information, and wants to know things like:

- Is the person being messaged present on their device?
- Are they typing?
- Have they read the message?

The typical way to support this sort of real-time data exchange is to use a client-server protocol, such as[WebSockets](https://en.wikipedia.org/wiki/WebSocket). WebSockets enable persistent, full-duplex communication between your app and a server. The[OKHTTP library](https://square.github.io/okhttp/)includes an[implementation of the WebSocket protocol](https://square.github.io/okhttp/3.x/okhttp/okhttp3/WebSocket.html)that you can use in your Android client.

The[Firebase Realtime Database](https://firebase.google.com/docs/database)provides a prebuilt backend and client frontend that can handle this sort of communication on your behalf. It uses WebSockets internally for real-time communication between its client and server.

### Background real-time messaging

When your app is no longer in the foreground, it's critical to avoid doing things that adversely impact system health and battery life. Since it's still important to deliver message notifications reliably, we recommend making use of[Firebase Cloud Messaging (FCM)](https://firebase.google.com/products/cloud-messaging).

FCM is a cross-platform messaging solution that efficiently sends notifications and data messages to Android (and other) devices. It leverages the Android Transport Layer (ATL) for devices that have Google services, so that your app can be notified of changes when it is no longer running. The timeliness of message delivery depends on the state of the device, the priority of the message, and whether your app is subject to restrictions because of[doze](https://developer.android.com/training/monitoring-device-state/doze-standby#understand_doze)or[app standby](https://developer.android.com/training/monitoring-device-state/doze-standby#understand_app_standby).

- [Learn how to integrate FCM into your Android project](https://firebase.google.com/docs/android/setup)
- [Explore the FCM (server) API and its capabilities](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)

## Enhance message delivery reliability

To make your message delivery even more robust, consider these strategies:

- Use[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)to[periodically wake up your app](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#schedule_periodic_work)to check for new messages when the device has[network connectivity](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#work-constraints), and (ideally) when the device is connected to a charger.
- Get[insight into FCM delivery](https://firebase.google.com/docs/cloud-messaging/understand-delivery?platform=android)with tools such as the[Firebase console](https://firebase.google.com/console)and[Android SDK delivery metrics](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData)from the[FCM Data API](https://firebase.google.com/docs/reference/fcmdata/rest).
- Use logging mechanisms and tools like[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)to monitor and troubleshoot message delivery issues.