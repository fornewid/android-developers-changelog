---
title: https://developer.android.com/google/play/billing/provide-refund-and-chargeback-suggestions
url: https://developer.android.com/google/play/billing/provide-refund-and-chargeback-suggestions
source: md.txt
---

Google Play is dedicated to protecting developers and maintaining a fair
ecosystem for all users. When users request a refund or chargeback, Google Play
evaluates the request based on various signals. To help support chargeback
disputes with financial institutions, you can provide refund preference and
purchase usage to Google Play for consideration.

## Provide refund suggestions

- **Check for notifications:** When a user initiates a chargeback that
  requires developer review, Google Play sends the
  [`PendingRefundReviewNotification`](https://developer.android.com/google/play/billing/rtdn-reference#pending-refund-review) Real Time Developer Notification.

- **Collect evidence and respond:** Evaluate the user's request and respond
  within 24 hours of receiving the notification by calling the
  [`ReviewRefund`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund) API. Provide a refund preference and any relevant
  purchase usage evidence to help Google Play dispute the chargeback.
  Google Play records your first API call in response to a notification and
  ignores subsequent calls, while still returning an `OK` status.

For more information, see [Google Play Developer API Getting Started guide](https://developers.google.com/android-publisher/getting_started).

## ReviewRefund API reference

For detailed specifications of the request and response body, see
[ReviewRefund API Reference](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund). To test your integration with a test purchase,
see [Test user-initiated chargebacks](https://developer.android.com/google/play/billing/test#chargebacks).