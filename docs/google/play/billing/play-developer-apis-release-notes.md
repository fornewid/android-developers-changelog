---
title: https://developer.android.com/google/play/billing/play-developer-apis-release-notes
url: https://developer.android.com/google/play/billing/play-developer-apis-release-notes
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/billing/llms.txt

This document contains release notes for the Google Play Developer APIs.

## November 19, 2026

### New features

- **Retention offers** : You can now create [retention offers](https://developer.android.com/google/play/billing/retention-offers.md.txt) that Google
  Play shows to eligible subscribers when they try to cancel.

  - **Retention targeting** : To create or update a retention offer with the [`monetization.subscriptions.basePlans.offers.create`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/create), [`monetization.subscriptions.basePlans.offers.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/patch), or [`monetization.subscriptions.basePlans.offers.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/batchUpdate) method, set `retentionRule` in the offer's `targeting` field to a [`RetentionTargetingRule`](https://developer.android.com/google/play/billing/retention-offers.md.txt#retention-targeting-rule) object. Use the `scope`, `minDuration`, `allowMultipleClaims`, and `minOfferCooldownDuration` fields to define which subscribers are eligible and whether they can claim the offer more than once.
  - **Offer availability window** : The [`SubscriptionOffer`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers#SubscriptionOffer) resource now includes optional `startTime` and `endTime` fields that set when an offer, such as a retention offer, becomes available and when it stops being available.
  - **Per-user targeting** : To make a retention offer available only to specific subscribers, set `retentionPerUserRule` ([`RetentionPerUserTargetingRule`](https://developer.android.com/google/play/billing/retention-offers.md.txt#per-user-targeting)) in the offer's `targeting` field. To target the offer to a subscription, call the [`purchases.subscriptionsv2.activateOfferTargeting`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/activateoffertargeting) method with the `purchaseToken` and `offerId`. To remove the targeting, call the [`purchases.subscriptionsv2.deactivateOfferTargeting`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/deactivateoffertargeting) method. The [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) resource lists the offers that are targeted to each line item in the `developerTargetedOffers` field, including the `offerId` and `activateTime` of each offer.
  - **Plan transition notifications** : A new subscription RTDN type, [`SUBSCRIPTION_PLAN_TRANSITION_UPDATED`](https://developer.android.com/google/play/billing/rtdn-reference.md.txt#sub) (`21`), is sent when a subscriber accepts a retention offer.
  - **Plan transition details** : The [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) resource now includes a `planTransitionDetails` object in `autoRenewingPlan`. It identifies the accepted retention offer in `offerId`, and reports the transition state in `transitionInfo`.
- **ETag validation for subscription cancellation and revocation** : The
  [`purchases.subscriptionsv2.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel) and
  [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) methods now support an optional
  `etag` field in `CancellationContext` and `RevocationContext`. Use the
  `etag` field to prevent conflicts when multiple requests modify the same
  subscription at the same time. Get the `etag` value from the top-level
  `etag` field returned by your most recent
  [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) call.

## July 06, 2026

### New features

- **Updates to chargeback cost responsibility** : Google Play now
  supports a [collaborative chargeback](https://developer.android.com/google/play/billing/provide-refund-and-chargeback-suggestions.md.txt)
  dispute process.

  - **Pending refund review notifications** : A new real-time developer
    notification (RTDN) type, [`PendingRefundReviewNotification`](https://developer.android.com/google/play/billing/rtdn-reference.md.txt#pending-refund-review), is
    sent when a user requests a chargeback that requires your
    review. Pending reviews support only `CHARGEBACK` as the refund reason.

  - **ReviewRefund API** : You can evaluate these requests and respond within
    24 hours by calling the new [`orders.reviewrefund`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund) API. In the API
    call, you must provide a refund preference (such as `APPROVE`,
    `DECLINE`, or `NEUTRAL`) and any relevant purchase usage evidence (such
    as user IP address, cumulative consumption percentage, and coarse
    geographic location) to help Google Play dispute the chargeback.

## May 19, 2026

### New features

- **Pending order ID** : The [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) API now includes `onHoldStateContext` and `inGracePeriodStateContext` fields. These fields provide additional details, such as the pending or failed order ID, when a subscription enters the `ON_HOLD` or `IN_GRACE_PERIOD` state due to a declined renewal payment.

### Deprecations

- Some of the subscription APIs are deprecated. For more information, see [May
  2026 Subscription API deprecation](https://developer.android.com/google/play/billing/play-developer-apis-deprecations#may19-2026-api-deprecation).

## January 27, 2026

### New features

- **Subscription with add-ons deferral** : Previously, the Google Play
  Developer API allowed deferral of billing only for single subscriptions. The
  deferral functionality is now available for both single subscriptions and
  subscriptions with add-ons through the
  [`purchases.subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method. When you defer the billing
  date of a subscription with add-ons, the billing date for all items in the
  subscription are deferred by the specified duration.

- **OfferPhase** : The `OfferPhase` field is now available in the
  [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) API. This field provides the current offer phase
  of the subscription as one of prorated period, free trial, introductory
  price and base plan price.

## November 19, 2025

### New features

- [Enhanced Resubscribe handling](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#resubscribe_after_expiration).

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
- [Price step-up consent](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#price-stepup-consent) features are available:

  - A new field is added in the [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get):
    `SubscriptionPurchaseLineItem.auto_renewing_plan.price_step_up_consent_details`.

  - A new real time developer notification type
    [SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED](https://developer.android.com/google/play/billing/rtdn-reference.md.txt#sub) is available.

## June 30, 2025

### New features

- The new [ProductPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2) API that supports [multiple purchase options
  and offers for one-time products](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers) is available.

## May 21, 2025

### Deprecations

- Some of the subscription APIs are deprecated. For more information, see [Subscription API deprecation](https://developer.android.com/google/play/billing/play-developer-apis-deprecations.md.txt#may21-api-deprecation).

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