---
title: Deprecations  |  Play Billing  |  Android Developers
url: https://developer.android.com/google/play/billing/play-developer-apis-deprecations
source: html-scrape
---

**Reminder:** By Aug 31, 2026, all new apps and updates to existing apps must use Billing Library version 8 or later. If you need more time to update your app, you can request an extension until Nov 1, 2026. Learn about [Play Billing Library version deprecation](/google/play/billing/deprecation-faq).

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Monetization](https://developer.android.com/google/play/billing)

Send feedback

# Deprecations Stay organized with collections Save and categorize content based on your preferences.





This document lists the Google Play Developer APIs and the related
features which are in a deprecation period.

## Deprecation timeline - May 19, 2026 to August 31, 2028

The features and APIs in this section are deprecated as of May 19, 2026, and
will be shut down on August 31, 2028. For deprecated items, you may request
an extension until November 1, 2028 by submitting a support ticket through
the [Play Console > Help](https://play.google.com/console/u/0/developers/help-and-support).

**Note:** [Client libraries](https://developers.google.com/android-publisher/libraries) released after July 1, 2027, will no longer
include these features and APIs. However, existing libraries can still
access them until the shutdown date.

### Deprecated subscription APIs

This section lists the API deprecations.

| API | Available replacement |
| --- | --- |
| [subscriptions.cancel](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel) | [subscriptionsv2.cancel](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel) |
| [subscriptions.defer](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer) | [subscriptionsv2.defer](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) |
| [Order.lineItems.subscriptionDetails.offer\_phase](https://developers.google.com/android-publisher/api-ref/rest/v3/orders#Order) | [Order.lineItems.subscriptionDetails.offer\_phase\_details](https://developers.google.com/android-publisher/api-ref/rest/v3/orders#Order) |

## Deprecation timeline - May 21, 2025 to August 31, 2027

The features and APIs in this section are deprecated as of May 21, 2025, and
will be shut down on August 31, 2027. For deprecated
items, you may request an extension until November 1, 2027 by submitting a
support ticket through the [Play Console > Help](https://play.google.com/console/u/0/developers/help-and-support).

**Note:** [Client libraries](https://developers.google.com/android-publisher/libraries) released after July 1, 2026, will no longer
include these features and APIs. However, existing libraries can still
access them until the shutdown date.

### Deprecated subscription APIs

This section lists the API deprecations.

| API | Available replacement |
| --- | --- |
| [subscriptions.get](https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/get) | [subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) |
| [subscriptions.refund](https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/refund) | Call [subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) to get SubscriptionPurchaseLineItem. latest\_successful\_order\_id, and then call [Orders.refund](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund) to refund the orders. |
| [subscriptions.revoke](https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/revoke) | [subscriptionsv2.revoke](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) |
| [SubscriptionPurchaseV2. latestOrderId](https://developers.google.com/android-publisher/deprecated-apis/latestOrderId.subscription.purchasev2) | [SubscriptionPurchaseLineItem. latest\_successful\_order\_id](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem) |
| RealTimeDeveloperNotification. SubscriptionNotification.subscriptionId | No replacement |
| [RealTimeDeveloperNotification. SubscriptionNotification. notificationType SUBSCRIPTION\_PRICE\_CHANGE\_CONFIRMED](/google/play/billing/rtdn-reference#sub) | SUBSCRIPTION\_PRICE \_CHANGE\_UPDATED |

### SubscriptionPurchaseV2 fields for recurring subscriptions

`purchases.subscriptionv2` contains new fields that provide more detail
about new subscription objects. The following table shows how fields from
the legacy subscription endpoint map to corresponding fields in
`purchases.subscriptionv2`.

| SubscriptionPurchase | SubscriptionPurchaseV2 |
| --- | --- |
| `countryCode` | `regionCode` |
| `orderId` | `lineItems.latestSuccessfulOrderId`  You can get the pending order ID from `inGracePeriodStateContext.renewalDeclined.pendingOrderId` or `onHoldStateContext.renewalDeclined.pendingOrderId`. |
| `startTimeMillis` | `startTime` |
| `expiryTimeMillis` | `lineItems.expiryTime` (each subscription acquired in the purchase has its own `expiryTime`) |
| `autoResumeTimeMillis` | `pausedStateContext.autoResumeTime` |
| `autoRenewing` | `lineItems.autoRenewingPlan.autoRenewEnabled` |
| `priceCurrenceCode`, `priceAmountMicros` | `lineItems.autoRenewingPlan.recurringPrice` |
| `introductoryPriceInfo` | `lineItems.offerPhase.introductoryPrice`  This information can also be found in the `offer` for each of the subscriptions purchased. |
| `developerPayload` | (no equivalent field) developer payload has been deprecated |
| `paymentState` | (no equivalent field)  You can infer the payment state from `subscriptionState`:  * Payment is pending:   + `SUBSCRIPTION_STATE_PENDING` (new purchases     with pending transaction)   + `SUBSCRIPTION_STATE_IN_GRACE_PERIOD`   + `SUBSCRIPTION_STATE_ON_HOLD` * Payment has been received:   + `SUBSCRIPTION_STATE_ACTIVE` * Free trial:   + `lineItems.offerPhase.freeTrial` * Deferred upgrade / downgrade:   + `lineItems.deferredItemReplacement` |
| `cancelReason`, `userCancellationTimeMillis`, `cancelSurveyResult` | `canceledStateContext` |
| `linkedPurchaseToken` | `linkedPurchaseToken` (no change) |
| `purchaseType` | Test: through `testPurchase`  Promotion: `signupPromotion` |
| `priceChange` | `lineItems.autoRenewingPlan.priceChangeDetails` |
| `profileName`, `emailAddress`, `givenName`, `familyName`, `profileId` | `subscribeWithGoogleInfo` |
| `acknowledgementState` | `acknowledgementState (no change)` |
| `promotionType`, `promotionCode` | `signupPromotion` |
| `externalAccountId`, `obfuscatedExternalAccountId`, `obfuscatedExteranlProfileId` | `externalAccountIdentifiers` |






Send feedback