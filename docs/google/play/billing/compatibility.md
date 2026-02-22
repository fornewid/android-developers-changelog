---
title: https://developer.android.com/google/play/billing/compatibility
url: https://developer.android.com/google/play/billing/compatibility
source: md.txt
---

[Google Play's billing system](https://developer.android.com/google/play/billing) is a service that
allows you to sell digital products and content in your Android app.
With the May 2022 release, we've changed how subscription products are
defined, and this affects how they are sold in-app and managed on your
backend. If you are integrating with Google Play Billing for the first
time, you can start your integration by reading
[Getting ready](https://developer.android.com/google/play/billing/getting-ready).

If you were selling subscriptions with Google Play Billing before May 2022,
it's important to understand how to adopt new features while maintaining
your existing subscriptions.

**The first thing to know is that all of your existing subscriptions, apps,
and backend integrations function just as they did before the May 2022
release** . You don't need to make any immediate changes, and you can adopt
these new features over time. Each major release of the
[Google Play Billing Library](https://developer.android.com/reference/com/android/billingclient/classes)
is supported for two years after release. Existing integrations with the
[Google Play Developer API](https://developer.android.com/google/play/developer-api)
continue to function as before.

Here's an overview of the May 2022 updates:

- The new [**Google Play Console**](https://play.google.com/console) lets you create and manage subscriptions, base plans, and offers. This includes both new and migrated subscriptions.
- The [**Play Developer API**](https://developers.google.com/android-publisher) contains updates to support new Google Play Console UI functionality in API form. Notably, there is a new version of the [**Subscription Purchases API**](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2). Use this API to check subscription status and manage subscription purchases.
- The new [**Play Billing Library version 5**](https://developer.android.com/google/play/billing/release-notes) allows your app to benefit from all the new subscription features. When you're ready to upgrade to version 5, follow the guidance in the [migration guide](https://developer.android.com/google/play/billing/migrate-gpblv5).

## Subscriptions configuration

### Managing subscriptions via Google Play Console

As of May 2022, you will notice some differences in the Google Play Console.

A single subscription can now have multiple base plans and
offers. Previously-created subscription SKUs now appear in
the Play Console as these new subscription, base plan, and
offer objects. If you haven't already, see
[Recent changes to subscriptions in Play Console](https://support.google.com/googleplay/android-developer/answer/12124625)
for descriptions of the new objects, including their functionality and
configuration. All of your preexisting subscription products appear in the
Google Play Console in this new format. Each SKU is now represented by
a subscription object that contains a single base plan and backward-compatible
offer, if applicable.

Since older integrations expected each subscription to include a single offer,
represented by a
[`SkuDetails`](https://developer.android.com/reference/com/android/billingclient/api/SkuDetails) object,
each subscription can have a single backward-compatible base plan or offer.
The backward-compatible base plan or offer is returned as part of a SKU
for apps that are using the now-deprecated `querySkuDetailsAsync()` method.
For more information on configuring and managing backward-compatible
offers, see
[Understand subscriptions](https://support.google.com/googleplay/android-developer/answer/12154973)
Once your app is using only `queryProductDetailsAsync()`, and once there
are no older versions of your app still making purchases, you no longer
need to utilize a backward-compatible offer.

### Managing subscriptions via Subscriptions Publishing API

The [Play Developer API](https://developers.google.com/android-publisher#subscriptions)
contains new functionality for subscription purchases. The
[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
API for SKU management continues to work as before, including handling
one-time purchase products and subscriptions, so you don't need to
make any immediate changes to maintain your integration.

However, it's important to note that the Google Play Console uses only the new
subscription entities. **Once you start editing your subscriptions in the
Console, the
[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
API can no longer be used for subscriptions**.

If you have used the Publishing API prior to May 2022, to avoid any issues,
any existing subscriptions now appear as read-only in the
Google Play Console. If you try to make changes, you may get a warning explaining
this limitation. Before further editing subscriptions in the Console,
you should update your backend integration to use the new Subscription
Publishing endpoints. The new
[`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions),
[`monetization.subscriptions.baseplans`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans),
and
[`monetization.subscriptions.offers`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers)
endpoints allow you to manage all available base plans and offers. You can see
how the different fields map from the `InAppProduct` entity to
the new objects under `monetization.subscriptions` in the following
table:

| InAppProduct | Subscription |
|---|---|
| `packageName` | `packageName` |
| `sku` | `productId` |
| `status` | `basePlans[0].state` |
| `prices` | basePlans\[0\].regionalConfigs.price |
| `listings` | listings |
| `defaultPrice` | No equivalence |
| `subscriptionPeriod` | basePlans\[0\].autoRenewingBasePlanType.billingPeriodDuration |
| `trialPeriod` | basePlans\[0\].offers\[0\].phases\[0\].regionalConfigs\[0\].free |
| `gracePeriod` | basePlans\[0\].autoRenewingBasePlanType.gracePeriodDuration |
| `subscriptionTaxesAndComplianceSettings` | taxAndComplianceSettings |

This required API update only applies to the Publishing API (SKU management).

## Play Billing Library changes

To support gradual migration, the Play Billing Library includes all the
methods and objects available in previous versions.
[`SkuDetails`](https://developer.android.com/reference/com/android/billingclient/api/SkuDetails)
objects and functions like
[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))
still exist so you can upgrade to use
[new functionality](https://developer.android.com/google/play/billing/migrate-gpblv5)
without having to also immediately update existing subscriptions code.
You can also control which offers are available through these methods
by marking them as backward-compatible.

In addition to keeping legacy methods, Play Billing Library 5 now includes
a new `ProductDetails` object and a corresponding `queryProductDetailsAsync()`
method to handle new entities and functionality. Existing in-app products
(one-time purchases and consumables) are now also supported by
`ProductDetails`.

For a subscription, `ProductDetails.getSubscriptionOfferDetails()`
returns a list of all base plans and offers the user is eligible to purchase.
This means that you can access all base plans and offers eligible
for the user, regardless of backward-compatibility.
`getSubscriptionOfferDetails()` returns `null` for non-subscription
products. For one-time purchases, you can use
`getOneTimePurchaseOfferDetails()`.

Play Billing Library 5 also includes both new and legacy methods for
launching the purchase flow. If the `BillingFlowParams` object passed to
[`BillingClient.launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams))
is configured using a `SkuDetails` object, the system extracts the offer
information to sell from the backward-compatible base plan or offer that
corresponds to the SKU. If the `BillingFlowParams` object passed to
`BillingClient.launchBillingFlow()` is configured using
`ProductDetailsParams` objects, which include `ProductDetails` and a
`String` representing the specific offer token for the offer being
purchased, the system then uses that information to identify the
product being acquired by the user.

`queryPurchasesAsync()` returns all purchases owned by
the user. To indicate the requested product type, you can pass
in a `BillingClient.SkuType` value, as in older versions, or a
`QueryPurchasesParams` object that contains a
`BillingClient.ProductType` value that represents the new subscription
entities.

We recommend [updating your apps](https://developer.android.com/google/play/billing/migrate-gpblv5)
to version 5 of the library soon so you can start taking advantage
of these new subscription features.

## Managing subscription status

This section describes the primary changes to the backend components of
a Google Play billing system integration that need to be implemented for
migration to version 5.

### Real Time Developer Notifications

Soon the [`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub)
object will no longer contain a *subscriptionId* . If you are relying on
this field to identify the subscription product, you should update
to obtain this information from the subscription status by using
[`purchases.subscriptionv2:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
once you receive the notification. Each [`SubscriptionPurchaseLineItem`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem) element
in the *lineItems* collection that is returned as part of the purchase status
will include the corresponding *productId*.

### Subscriptions Purchases API: getting subscription status

In previous versions of the Subscriptions Purchases API, you could
query subscription status by using
[`purchases.subscriptions:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions).
This endpoint is unchanged and continues to work for backward-compatible
subscription purchases. This endpoint **does not** support any new
functionality released in May 2022.

In the new version of the Subscriptions Purchases API, use
[`purchases.subscriptionsv2:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
to obtain subscription purchase status. This API is compatible with
migrated subscriptions, new subscriptions (both prepaid and
auto-renewing), and purchases of all types. You can use this endpoint
to check for subscription status when receiving notifications. The
returned object, `SubscriptionPurchaseV2`, contains new fields,
but it still includes legacy data that is needed to continue supporting
existing subscriptions.

#### SubscriptionPurchaseV2 fields for prepaid plans

New fields have been added to support prepaid plans, which are extended by
the user instead of automatically renewing. All fields apply
to prepaid plans as they do for auto-renewing subscriptions,
with the following exceptions:

- **\[New field\] lineItems\[0\].prepaid_plan.allowExtendAfterTime**: denotes when a user will be allowed to buy another top-up to extend their prepaid plan, as a user is allowed to have only one unconsumed top-up at a time.
- **\[New field\] SubscriptionState** : specifies the subscription object state. For prepaid plans, this value is always either `ACTIVE`, `PENDING`, or `CANCELED`.
- **lineItems\[0\].expiryTime**: This field is always present for prepaid plans.
- **paused_state_context**: This field is never present, as prepaid plans cannot pause.
- **lineItems\[0\].auto_renewing_plan**: Not present for prepaid plans.
- **canceled_state_context**: Not present for prepaid plans, as this field applies only to users who actively cancel a subscription.
- **lineItems\[0\].productId** : This field replaces `subscriptionId` from previous versions.

#### SubscriptionPurchaseV2 fields for recurring subscriptions

`purchases.subscriptionv2` contains new fields that provide more detail
about new subscription objects. The following table shows how fields from
the legacy subscription endpoint map to corresponding fields in
`purchases.subscriptionv2`.

| SubscriptionPurchase | SubscriptionPurchaseV2 |
|---|---|
| `countryCode` | `regionCode` |
| `orderId` | `latestOrderId` |
| (no equivalent field) | `lineItems.offerPhase` (identifies current phase: free trial, intro price, proration, base price) |
| (no equivalent field) | `lineItems` (list of [SubscriptionPurchaseLineItem](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem)) that represents the products acquired with the purchase |
| (no equivalent field) | `lineItems.offerDetails.basePlanId` |
| (no equivalent field) | `lineItems.offerDetails.offerId` |
| (no equivalent field) | `lineItems.offerDetails.offerTags` |
| `startTimeMillis` | `startTime` |
| `expiryTimeMillis` | `lineItems.expiryTime` (each subscription acquired in the purchase has its own `expiryTime`) |
| (no equivalent field) | `subscriptionState` (indicates the [state of the subscription](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionstate)) |
| (no equivalent field) | `pausedStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_PAUSED`) |
| `autoResumeTimeMillis` | `pausedStateContext.autoResumeTime` |
| (no equivalent field) | `canceledStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_CANCELED`) |
| (no equivalent field) | `testPurchase` (only present in licensed tester purchases) |
| `autoRenewing` | `lineItems.autoRenewingPlan.autoRenewEnabled` |
| `priceCurrenceCode`, `priceAmountMicros` | `lineItems.autoRenewingPlan.recurringPrice` |
| `introductoryPriceInfo` | `lineItems.offerPhase.introductoryPrice` This information can also be found in the `offer` for each of the subscriptions purchased. |
| developerPayload | (no equivalent field) developer payload has been deprecated |
| paymentState | (no equivalent field) You can infer the payment state from `subscriptionState`: - Payment is pending: - `SUBSCRIPTION_STATE_PENDING` (new purchases with pending transaction) - `SUBSCRIPTION_STATE_IN_GRACE_PERIOD` - `SUBSCRIPTION_STATE_ON_HOLD` - Payment has been received: - `SUBSCRIPTION_STATE_ACTIVE` - Free trial: - `lineItems.offerPhase.freeTrial` - Deferred upgrade / downgrade: - `SUBSCRIPTION_STATE_PENDING` |
| `cancelReason`, `userCancellationTimeMillis`, `cancelSurveyResult` | `canceledStateContext` |
| `linkedPurchaseToken` | `linkedPurchaseToken` (no change) |
| `purchaseType` | Test: through `testPurchase` Promotion: `signupPromotion` |
| `priceChange` | `lineItems.autoRenewingPlan.priceChangeDetails` |
| `profileName`, `emailAddress`, `givenName`, `familyName`, `profileId` | [`subscribeWithGoogleInfo`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscribewithgoogleinfo) |
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

### Pricing API

Use the
[`monetization.convertRegionPrices`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization/convertRegionPrices)
endpoint to calculate regional prices as you would through the
Play Console. This method accepts a single price in any Play-supported
currency and returns converted prices (including the default rate of
tax where applicable) for all regions where Google Play supports purchases.