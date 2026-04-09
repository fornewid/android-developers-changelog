---
title: https://developer.android.com/health-and-fitness/fitness/basic-app/good-better-best
url: https://developer.android.com/health-and-fitness/fitness/basic-app/good-better-best
source: md.txt
---

This document charts the optimal progression of a health and fitness app from a
likely starting place to best-in-class. It's designed to help you think about
scaling your app over time, and what features to implement. While every health
and fitness app is different, consider these recommendations to achieve a
best-in-class app.

## Basic health and fitness app

There are key elements that a basic health and fitness app requires in order to
provide a great foundational experience for users. Some of those key elements
include doing the following:

- Requesting only the necessary permissions to fulfill the experience that the user wants
- Offering tracking metrics that are customizable and understandable
- Offering in-app content browsing and discovery
- Offering in-app exercise controls
- If tracking an exercise session or other health-related long-running task, using a foreground service and declaring the [FOREGOUND_SERVICE_HEALTH](https://developer.android.com/about/versions/14/changes/fgs-types-required#health) permission in the manifest file.
- Integrating easy-to-use, [accessibility features](https://developer.android.com/guide/topics/ui/accessibility)

## Better health and fitness app

A better health and fitness app will start to grow its reach, once a user has
physically and mentally made progress along their health journey. A better app
also allows a user to register for a profile with the use of existing
social media credentials and their email.

Implementing more holistic improvements into your app is also an excellent way
to accelerate its growth. Consider these features as a way to further enhance
your app:

- Integrating second surfaces, such as Wear OS (using [Health Services on Wear
  OS](https://developer.android.com/training/wearables/health-services) for data collection). Use Bluetooth Low Energy (BLE) to send and receive data to and from peripheral devices
- If connecting peripheral devices, preserve battery usage. If you are periodically syncing data, use the [CONNECTED_DEVICE](https://developer.android.com/about/versions/14/changes/fgs-types-required#connected-device) foreground service type.
- Using [Jetpack Glance](https://developer.android.com/jetpack/compose/glance) to create app [widgets](https://developer.android.com/develop/ui/views/appwidgets/overview) on mobile to enable users to track progress in a glanceable way. Consider using dynamic color, optimizing across form factors, and taking advantage of in-app widget pinning APIs for better discoverability.
- If supporting Wear OS, supplying a [tile](https://developer.android.com/training/wearables/tiles) or [complication](https://developer.android.com/training/wearables/tiles/complications) to enable similar glanceable experiences on the watch.
- Offering creative ways to keep a user on track (such as notifications and nudges). Be sure to follow best practices for notifications, including [waiting to show the notification prompt](https://developer.android.com/develop/ui/views/notifications/notification-permission#best-practices) until the user has had time to familiarize themselves with the app, and using [notification bridging](https://developer.android.com/training/wearables/notifications/bridger) for paired phones and watches.
- Improving [accessibility](https://developer.android.com/guide/topics/ui/accessibility) for all, such as adding [subtitles](https://developer.android.com/guide/topics/media/exoplayer/media-items#sideloading-subtitle) for video content and optimizing for accessibility on any secondary surfaces, such as [Wear OS](https://developer.android.com/training/wearables/accessibility).
- Supporting playback to [Cast](https://developers.google.com/cast/docs/developers) devices for your fitness app's video content
- Using [Google Play Billing](https://developer.android.com/google/play/billing) to let users purchase subscriptions

## Best-in-class health and fitness app

A best-in-class health and fitness app builds on the previous recommendations to
create a seamless multi-device experience for users, which may include:

- Enabling sharing of workouts and accomplishments with [Sharesheet](https://developer.android.com/training/sharing/send)
- Optimizing for foldables by supporting the [`HALF_OPENED`](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables#foldable_postures) [state](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables#foldable_postures)
- Testing and refining voice assistant integrations on mobile, such as with [Google Assistant](https://developer.android.com/media/implement/assistant)
- Supporting [Better Together](https://www.android.com/better-together) use cases, such as [Nearby
  Connections](https://developers.google.com/nearby/connections/overview)
- Investing in seamless identity across surfaces such as [passkeys](https://developer.android.com/training/sign-in/passkeys), [One
  Tap](https://developers.google.com/identity/one-tap/android/overview), and [account linking](https://developers.google.com/identity/account-linking)
- Offering [frictionless subscriptions](https://www.youtube.com/watch?v=ARuf97ncE4w)