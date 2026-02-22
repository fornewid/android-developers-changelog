---
title: https://developer.android.com/stories/apps/truecaller
url: https://developer.android.com/stories/apps/truecaller
source: md.txt
---

# Truecaller brings ~40% subscribers back with real time developer notifications

## Background

[Truecaller](https://play.google.com/store/apps/details?id=com.truecaller)is an app that offers caller identification, call blocking, chat messaging and organized inbox. The app has a basic offering and a premium version which is ad-free and has a variety of unlocked features like advanced spam blocking and call recording.

Truecaller discovered that 50% of subscribers of Truecaller Monthly Premium were cancelling within 60 days. 46% of cancellations were voluntary, and 54% involuntary due to payment issues.

## What did they do

Truecaller believed these cancellations happened because users were losing track of their subscriptions due to a lack of messaging, and utilized real time developer notifications (RTDN) to solve the problem. RTDN monitors state changes in subscriptions and lets the developer know when certain changes take place, allowing them to take action.

Enabling account hold and grace period, Truecaller was able to identify users whose payment had failed (and were on a temporary grace period) or who had put their subscription on hold. They took the following steps to bring them back.

Users were notified directly (e.g. via email and push notification) that their payment had failed. While using the app, red alert icons (which contrast with the blue UI) appeared on most pages directing users to their account page. The language used was carefully phrased - it contained key information such as the date the transaction failed and the time left to reactivate. Truecaller was also careful not to assume the worst, and encouraged users to simply "check that their account details were correct" in case the drop was a simple error.

In addition, using the SUBSCRIPTION_CANCELED notification, Truecaller was able to communicate directly with cancelled users. They pushed messages to canceled users when they started the app and on the subscription page. These notifications told the user how long they had left to restore their subscriptions and encouraged them to do so.

In all cases, Truecaller was careful not to overload the experience with messages.

## Results

Truecaller's use of RTDN enables them to communicate directly with different categories of users, sending personalized messages to users' phones which address their actual circumstances. This meant they could offer useful information, simple suggestions and helpful links and options that were relevant to individual cases. Many users reactivated their accounts or resubscribed to the premium service:

- For grace period and on-hold users, they recovered 40% of reactivated accounts versus 15% before using RTDN . They also saw users reactivating up to 3 weeks later.
- For cancelled users, a full 20% were now resubscribing to the premium service versus 3% earlier.

Using RTDN is a simple and elegant way to enhance subscription retention for our users leading to better monetisation for subscription apps. New RTDN types present additional ongoing opportunities to reduce subscriber churn. -- Manjunath Bharadwaj (Director of Growth Engineering, Truecaller).

## Get started

Send context-sensitive messages to your users using[real time developer notifications](https://developer.android.com/google/play/billing/realtime_developer_notifications)!