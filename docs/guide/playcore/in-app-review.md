---
title: https://developer.android.com/guide/playcore/in-app-review
url: https://developer.android.com/guide/playcore/in-app-review
source: md.txt
---

The Google Play In-App Review API lets you prompt users to submit Play Store
ratings and reviews without the inconvenience of leaving your app or game.

Generally, the in-app review flow (see figure 1) can be triggered at any time
throughout the user journey of your app. During the flow, the user has the
ability to rate your app using the 1 to 5 star system and to add an optional
comment. Once submitted, the review is sent to the Play Store and eventually
displayed.
| **Note:** To protect user privacy and avoid API misuse, there are strict guidelines that your app should follow about [when to request in-app reviews](https://developer.android.com/guide/playcore/in-app-review#when-to-request) and the [design of the review prompt](https://developer.android.com/guide/playcore/in-app-review#design-guidelines).

![In app review workflow for a user](https://developer.android.com/static/images/google/play/in-app-review/iar-flow.jpg)


**Figure 1.** In-app review flow for a user

<br />

## Device requirements

In-app reviews only work on the following devices:

- Android devices (phones, tablets, and TVs with Google TV) running Android 5.0 (API level 21) or higher that have the Google Play Store installed.
- ChromeOS devices that have the Google Play Store installed.

## Play Core library requirements

To integrate in-app reviews in your app, your app must use version 1.8.0 or
higher of the [Play Core library](https://developer.android.com/guide/playcore).

## When to request an in-app review

Follow these guidelines to help you decide when to request in-app reviews from
users:

- Trigger the in-app review flow after a user has experienced enough of your app or game to provide useful feedback.
- Don't prompt the user excessively for a review. This approach helps minimize user frustration and limit API usage (see the [section on quotas](https://developer.android.com/guide/playcore/in-app-review#quotas)).
- Your app shouldn't ask the user any questions before or while presenting the rating button or card, including questions about their opinion (such as "Do you like the app?") or predictive questions (such as "Would you rate this app 5 stars").

## Design guidelines

Follow these guidelines as you determine how to integrate in-app reviews in your
app:

- Surface the card as-is, without tampering or modifying the existing design in any way, including size, opacity, shape, or other properties.
- Don't add any overlay on top of the card or around the card.
- The card and the card's background should be on the topmost layer. Once the card has surfaced, don't programmatically remove the card. The card is removed automatically based on either the user's explicit action, or an internal Play Store mechanism.

## Quotas

To provide a great user experience, Google Play enforces a time-bound quota on
how often a user can be shown the review dialog. Because of this quota, calling
the `launchReviewFlow` method more than once during a short period of time (for
example, less than a month) might not always display a dialog.
| **Note:** The specific value of the quota is an implementation detail, and it can be changed by Google Play without any notice.

Because the quota is subject to change, it's important to apply your own logic
and target the best possible moment to request a review. For example, **you
should not have a call-to-action option (such as a button) to trigger the API**,
as a user might have already hit their quota and the flow won't be shown,
presenting a broken experience to the user. For this use case, redirect the user
to the Play Store instead.

## Integrate in-app reviews in your app

Learn how to integrate in-app reviews in your app, depending on your development
environment:

- [Kotlin or Java](https://developer.android.com/guide/playcore/in-app-review/kotlin-java)
- [Native (C++)](https://developer.android.com/guide/playcore/in-app-review/native)
- [Unity](https://developer.android.com/guide/playcore/in-app-review/unity)
- [Unreal Engine](https://developer.android.com/guide/playcore/in-app-review/unreal-engine)

## Terms of service and data safety

By accessing or using the Play In-App Reviews Library, you agree to the [Play
Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license). Read and understand all
applicable terms and policies before accessing the library.

## Data Safety

The Play Core libraries are your app's runtime interface with the Google Play
Store. As such, when you use Play Core in your app, the Play Store runs its own
processes, which include handling data as governed by the [Google Play Terms of
Service](https://play.google.com/about/play-terms/index.html). The following information describes how the Play Core libraries
handle data to process specific requests from your app.

### In-app Reviews

|---|---|
| Data collected on usage | User-entered data (rating and free-text review) |
| Purpose of data collection | The data collected is used to leave a review on the Play Store. |
| Data encryption | Data is encrypted. |
| Data sharing | The data collected is used in a public review on the Play Store or, if the app is in a closed test track, the data collected is shared privately with the app developer. |
| Data deletion | Users can delete their reviews in their Google Play Store account or Google Account. |

While we aim to be as transparent as possible, you are solely responsible for
deciding how to respond to Google Play's data safety section form regarding your
app's user data collection, sharing, and security practices.