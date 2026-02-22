---
title: https://developer.android.com/google/play/billing/play-developer-apis-release-notes
url: https://developer.android.com/google/play/billing/play-developer-apis-release-notes
source: md.txt
---

This document contains release notes for the Google Play Developer APIs.

## January 27, 2026

### New features

- **Subscription with add-ons deferral:** Previously, the Google Play
  Developer API allowed deferral of billing only for single subscriptions.
  The deferral functionality is now available for both single subscriptions
  and subscriptions with add-ons through the
  [`purchases.subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method. When you defer the billing
  date of a subscription with add-ons, the billing
  date for all items in the subscription are deferred by the
  specified duration.

- **OfferPhase** : The `OfferPhase` field is now available in
  the [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) API. This field provides the current offer
  phase of the subscription as one of prorated period, free trial,
  introductory price and base plan price.

## November 19, 2025

### New features

- [Enhanced Resubscribe handling](https://developer.android.com/google/play/billing/lifecycle/subscriptions#resubscribe_after_expiration).

  - The `outOfAppPurchaseContext` field is now available in [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get), which helps link resubscription purchases made from the Play Store by providing details from the expired subscription.
  - The [purchases.subscriptions.acknowledge](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge) method now accepts optional `externalAccountId` in the request body, which lets you associate the resubscription purchase with your user identifiers.
- `SubscriptionPurchaseLineItem.itemReplacement` field is now available in
  [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get), which offers details about the item being
  replaced, if applicable.

- The [Orders API](https://developers.google.com/android-publisher/api-ref/rest/v3/orders) now includes `offerPhaseDetails` field, which provides
  more detailed information on the orders funding a prorated period.

## Sep 11, 2025

### New features

- The [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) API now provides the [`cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel) method.

  This method provides an enhancement over the existing
  [purchases.subscriptions.cancel](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel) functionality by introducing support
  for the `cancellationType` parameter in client libraries.
- [Price step-up consent](https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-stepup-consent) features are available:

  - A new field is added in the [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get):
    `SubscriptionPurchaseLineItem.auto_renewing_plan.price_step_up_consent_details`.

  - A new real time developer notification type
    [SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED](https://developer.android.com/google/play/billing/rtdn-reference#sub) is available.

## June 30, 2025

### New features

- The new [ProductPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2) API that supports [multiple purchase options
  and offers for one-time products](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers) is available.

## May 21, 2025

### Deprecations

- Some of the subscription APIs are deprecated. For more information, see [Subscription API deprecation](https://developer.android.com/google/play/billing/play-developer-apis-deprecations#may21-api-deprecation).

### New features

- The following new fields are available in the [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get):

  - `SubscriptionPurchaseLineItem.latest_successful_order_id`
  - `PriceChangeState.CANCELED`
- The [`subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) method now provides the
  `item_based_refund` option.

- The [Orders](https://developers.google.com/android-publisher/api-ref/rest/v3/orders) API now provides the [`get`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/get) and [`batchGet`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/batchget)
  methods.

### Other changes

- The *subscriptionId* parameter is optional in the [purchases.subscriptions](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions) APIs.