---
title: https://developer.android.com/google/play/billing/play-developer-apis-deprecations
url: https://developer.android.com/google/play/billing/play-developer-apis-deprecations
source: md.txt
---

This document lists the Google Play Developer APIs and the related
features which are in a deprecation period.

## Deprecation timeline - May 21, 2025 to August 31, 2027

The features and APIs in this section are deprecated as of May 21, 2025, and
will be shut down on August 31, 2027. However, you can avail an
extension for the deprecated items up to November 1, 2027.
| **Note:** [Client libraries](https://developers.google.com/android-publisher/libraries) released after November 1, 2025, will no longer include these features and APIs. However, existing libraries can still access them until the shutdown date.

### Deprecated subscription APIs

This section lists the API deprecations.

| API | Available replacement |
|---|---|
| [subscriptions.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get) | [subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) |
| [subscriptions.refund](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/refund) | Call [subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) to get SubscriptionPurchaseLineItem. latest_successful_order_id, and then call [Orders.refund](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund) to refund the orders. |
| [subscriptions.revoke](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke) | [subscriptionsv2.revoke](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) |
| [SubscriptionPurchaseV2. latestOrderId](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#resource:-subscriptionpurchasev2) | [SubscriptionPurchaseLineItem. latest_successful_order_id](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem) |
| [RealTimeDeveloperNotification. SubscriptionNotification.subscriptionId]() | No replacement |
| [RealTimeDeveloperNotification. SubscriptionNotification. notificationType SUBSCRIPTION_PRICE_CHANGE_CONFIRMED](https://developer.android.com/google/play/billing/rtdn-reference#sub) | SUBSCRIPTION_PRICE _CHANGE_UPDATED |

### SubscriptionPurchaseV2 fields for recurring subscriptions

`purchases.subscriptionv2` contains new fields that provide more detail
about new subscription objects. The following table shows how fields from
the legacy subscription endpoint map to corresponding fields in
`purchases.subscriptionv2`.

| SubscriptionPurchase | SubscriptionPurchaseV2 |
|---|---|
| `countryCode` | `regionCode` |
| `orderId` | `SubscriptionPurchaseLineItem.latest_successful_order_id` |
| (no equivalent field) | `lineItems.offerPhase` (identifies current phase: free trial, intro price, proration, base price) |
| (no equivalent field) | `lineItems` (list of SubscriptionPurchaseLineItem) that represents the products acquired with the purchase |
| (no equivalent field) | `lineItems.offerDetails.basePlanId` |
| (no equivalent field) | `lineItems.offerDetails.offerId` |
| (no equivalent field) | `lineItems.offerDetails.offerTags` |
| `startTimeMillis` | `startTime` |
| `expiryTimeMillis` | `lineItems.expiryTime` (each subscription acquired in the purchase has its own `expiryTime`) |
| (no equivalent field) | `subscriptionState` (indicates the state of the subscription) |
| (no equivalent field) | `pausedStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_PAUSED`) |
| `autoResumeTimeMillis` | `pausedStateContext.autoResumeTime` |
| (no equivalent field) | `canceledStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_CANCELED`) |
| (no equivalent field) | `testPurchase` (only present in licensed tester purchases) |
| `autoRenewing` | `lineItems.autoRenewingPlan.autoRenewEnabled` |
| `priceCurrenceCode`, `priceAmountMicros` | `lineItems.autoRenewingPlan.recurringPrice` |
| `introductoryPriceInfo` | `lineItems.offerPhase.introductoryPrice` This information can also be found in the `offer` for each of the subscriptions purchased. |
| developerPayload | (no equivalent field) developer payload has been deprecated |
| paymentState | (no equivalent field) You can infer the payment state from `subscriptionState`: - Payment is pending: - `SUBSCRIPTION_STATE_PENDING` (new purchases with pending transaction) - `SUBSCRIPTION_STATE_IN_GRACE_PERIOD` - `SUBSCRIPTION_STATE_ON_HOLD` - Payment has been received: - `SUBSCRIPTION_STATE_ACTIVE` - Free trial: - lineItems.offerPhase.freeTrial - Deferred upgrade / downgrade: - `SUBSCRIPTION_STATE_PENDING` |
| `cancelReason`, `userCancellationTimeMillis`, `cancelSurveyResult` | `canceledStateContext` |
| `linkedPurchaseToken` | `linkedPurchaseToken` (no change) |
| `purchaseType` | Test: through `testPurchase` Promotion: `signupPromotion` |
| `priceChange` | `lineItems.autoRenewingPlan.priceChangeDetails` |
| `profileName`, `emailAddress`, `givenName`, `familyName`, `profileId` | `subscribeWithGoogleInfo` |
| `acknowledgementState` | `acknowledgementState (no change)` |
| `promotionType`, `promotionCode` | `signupPromotion` |
| `externalAccountId`, `obfuscatedExternalAccountId`, `obfuscatedExteranlProfileId` | `externalAccountIdentifiers` |

### Other subscription management functions

While
[`purchases.subscriptions:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get)
has been upgraded to
[`purchases.subscriptionsv2:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get),
the rest of the developer subscription management functions remain
unchanged for now in the `purchases.subscriptions` endpoint,
so you can continue using
[`purchases.subscriptions:acknowledge`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge),
[`purchases.subscriptions:cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel),
[`purchases.subscriptions:defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer),
[`purchases.subscriptions:refund`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/refund),
and
[`purchases.subscriptions:revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke)
as you did before.