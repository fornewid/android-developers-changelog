---
title: https://developer.android.com/google/play/billing/lifecycle
url: https://developer.android.com/google/play/billing/lifecycle
source: md.txt
---

When you sell digital products through your app, you must consider the entire user experience. In-app integration lets you launch purchase flows and manage the user experience, but it's crucial to keep your backend up-to-date on the entitlements that users are purchasing. This is important for tracking purchases and managing other aspects of the user experience, such as cross-platform entitlements.

To monitor purchase lifecycle events and respond quickly to changes in user entitlements, you should build a purchase status management system in your backend for both subscriptions and one-time purchases. This system ensures quick and secure purchase processing regardless of device status, maintains consistent user entitlements across all platforms, and provides the ability to consult purchase history and entitlement data in your backend.

Google Play offers[real-time developer notifications (RTDN)](https://developer.android.com/google/play/billing/rtdn-reference)to monitor purchase lifecycle events, and the Play Developer APIs for[Subscriptions and In-App Purchases](https://developers.google.com/android-publisher#subscriptions)can be used to take necessary actions based on these events. By using these tools and building a robust purchase lifecycle management system, you can provide a seamless user experience and manage purchases and entitlements efficiently.

![](https://developer.android.com/static/images/google/play/billing/lifecycle/overview.svg)

## Build a real-time developer notification client

Purchases made on Google Play's billing system can go through several entitlement changes throughout their lifecycle. Various actions can trigger these changes, including the following:

- Actions initiated by users in your app.
- Actions initiated by users through the Play Store app.
- Actions initiated directly from your backend systems.
- Actions that you initiate through the Google Play Console.

For example:

- A user canceling a subscription through the Play Store subscription center.
- A developer deferring subscription billing using the Google Play Developer API.
- A developer issuing a refund and revoking entitlement for a purchase through the Google Play Console.

It is crucial that your backend is aware of the different states a purchase can go through and that it takes all necessary measures to adjust the entitlement accordingly in a timely manner.

While it is possible to use the Google Play Developer API to check a purchase status manually, relying on periodic checks is a very inefficient way to track changes and it's prone to errors and delays. RTDNs can help you respond to changes immediately without having to build lifecycle tracking logic for your Google Play purchases.

This section discusses how to build a client for RTDNs. RTDN is a feature built using Google Cloud Pub/Sub, which sends your backend an instant notification when a user's entitlement state changes. The Pub/Sub system consists of a publisher that sends notifications and a client that subscribes to those notifications. By implementing RTDN, you can track all changes to the user's entitlement state in real time and respond to them promptly.

### RTDN publisher

Google Play's backend acts as the publisher for RTDNs. To set up RTDN for you app, follow the instructions in the[Setup](https://developer.android.com/google/play/billing/getting-ready)guide. These steps allow Google Play's billing system to act as the publisher for your app's RTDNs. To complete this setup, you should familiarize yourself with the Google Cloud Platform Console to set up a basic Pub/Sub configuration.

### RTDN subscriber

After setting up the publisher, you should prepare your backend to consume RTDNs. To do this, you need to build a client to receive Google Cloud Pub/Sub messages. Your RTDN client's basic function consists of receiving instances of[`PubSubMessage`](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage), either through HTTPS requests in a registered endpoint or by using the[Cloud Pub/Sub client libraries](https://cloud.google.com/pubsub/docs/reference/libraries). See the Pub/Sub documentation to learn about using a[push](https://cloud.google.com/pubsub/docs/push)or a[pull](https://cloud.google.com/pubsub/docs/pull)strategy, or the[RTDN setup documentation](https://developer.android.com/google/play/billing/getting-ready#create-sub)for guidelines on choosing the strategy that works best for your needs.

For each message you receive, your backend should do the following:

- Unpack the base-64-encoded`data`field, which contains the[RTDN object](https://developer.android.com/google/play/billing/rtdn-reference#encoding).
- Trigger any required backend processes related to the entitlement change notified by the RTDN event.

## Handle purchase state transitions

One-time purchases and subscription purchases have different lifecycles based on the different states and events that can affect them. Thanks to RTDN, you don't need to build logic to confirm state transitions. All you need to do is define what happens when your backend receives each type of notification.
| **Note:** For[pre-orders](https://developer.android.com/google/play/billing/multi-offer-one-time-product#pre-order), RTDN follows the same lifecycle as the one-time purchase.

See the following guides to learn more about these scenarios:

- [One-time purchase lifecycle](https://developer.android.com/google/play/billing/lifecycle/one-time)
- [Subscription purchase lifecycle](https://developer.android.com/google/play/billing/lifecycle/subscriptions)