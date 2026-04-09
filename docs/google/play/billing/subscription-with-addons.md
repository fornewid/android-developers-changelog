---
title: https://developer.android.com/google/play/billing/subscription-with-addons
url: https://developer.android.com/google/play/billing/subscription-with-addons
source: md.txt
---

Subscription with add-ons lets you bundle multiple subscription products
together that can be purchased, billed and managed together. Your existing
product catalog subscriptions can be seamlessly offered as add-ons without any
upfront specification or additional configuration. You can launch a
purchase flow with multiple existing subscription products, and sell them
as add-ons.

## Considerations

Consider the following points when using the subscription with add-ons feature:

- Subscription with add-ons is only supported for auto renewing base plans.

- All items in the purchase must have the same recurring billing
  period. For example, you can't have an annually billed subscription
  with monthly billed add-ons.

- You can have a maximum of 50 items in a subscription with add-ons purchase.

- This feature isn't available in the India (*IN* ) and
  South Korea (*KR*) regions.

## Integrate with Play Billing Library

This section describes how to integrate the subscription with add-ons
feature with the Play Billing Library (PBL). It assumes that you are
familiar with the initial PBL integration steps such as,
[adding the PBL dependency to your app](https://developer.android.com/google/play/billing/integrate#dependency), initializing the [BillingClient](https://developer.android.com/google/play/billing/integrate#initialize),
and [connecting to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play). This section focuses on the PBL integration
aspects that are specific to subscription with add-ons.

### Launch a purchase flow

To launch a purchase flow for a subscription with add-ons, do the
following steps:

1. Fetch all your subscription items by using the
   [`BillingClient.queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) method.

2. Set the [`ProductDetailsParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams#newBuilder()) object for each item.

   The item represented by the [`ProductDetailsParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams#newBuilder()) object, specifies
   both the [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) indicating the subscription item, and an
   [`offerToken`](https://developer.android.com/google/play/billing/subscriptions#offers) selecting a specific subscription [`base plan`](https://developer.android.com/google/play/billing/subscriptions#base-plans-and-offers) or
   [`offer`](https://developer.android.com/google/play/billing/subscriptions#offers).
   | **Note:** All items in the `ProductDetails` must be from the same app.
3. Specify the item details in the
   [`BillingFlowParams.Builder.setProductDetailsParamsList`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)) method. The
   [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) class specifies the details of a purchase flow.

   | **Note:** The first item in the list is referred to as the base item, and the remaining items are referred to as add-ons. And every item in this list must be unique. In other words, you can't set two [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) with the same [`productId`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails#getProductId()) in the list.

   The following sample shows how to launch the billing flow for a subscription
   purchase with multiple items:  

   #### Java

   ```java
      BillingClient billingClient = ...;

       // ProductDetails obtained from queryProductDetailsAsync().
       ProductDetailsParams productDetails1 = ...;
       ProductDetailsParams productDetails2 = ...;
       ArrayList productDetailsList = new ArrayList<>();
       productDetailsList.add(productDetails1);
       productDetailsList.add(productDetails2);

       BillingFlowParams billingFlowParams =
           BillingFlowParams.newBuilder()
              .setProductDetailsParamsList(productDetailsList)
              .build();
       billingClient.launchBillingFlow(billingFlowParams);
   ```
   | **Note:** An in-app purchase will still be represented by the [`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase) object. And the [`getProducts()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts()) method returns entitlements for all the items the user has from this purchase.

#### Rules applicable for items in the purchase

- To ensure add-on renewal dates eventually align with the base item, Google Play may insert a prorated charge after any trial or intro pricing phases.
- [Offer eligibility](https://support.google.com/googleplay/android-developer/answer/12154973) will be evaluated separately for each item.

## Process purchases

Processing subscription with add-ons is the same as processing of
a single subscription purchase as described in
[Integrate the Google Play Billing Library into your app](https://developer.android.com/google/play/billing/integrate#launch). The only
difference is that the user can receive multiple
entitlements with a single purchase. A purchase of subscription with add-ons
returns multiple items which can be retrieved using
[`Purchase.getProducts()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts) in the Google
Play Billing Library, and then the `lineItems` list in
[`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) of the [Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2).
| **Note:** For each call of the [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) API, there is a limit of 50 items (active items + new items). If the cart contains more than 50 items, Google Play blocks the purchase flow.

## Modify subscriptions with add-ons

Any changes to your subscription with add-ons, results in an upgrade or a
downgrade. For more information, see
[upgrade or downgrade subscriptions](https://developer.android.com/google/play/billing/subscriptions#upgrade-downgrade).

To change or restore an existing purchase of subscription with add-ons in your
app, you must call the [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) API with additional
parameters, and ensure the following:

- Always call `setOldPurchaseToken` with the purchase token of the current subscription purchase.
- To upgrade, downgrade, or crossgrade an item, call `SubscriptionProductReplacementParams.setReplacementMode` to specify how the plan change should be handled between the old and the new purchase item. Otherwise, there is no need to set `SubscriptionProductReplacementParams`.
- When the base item isn't changed, you can still call `SubscriptionProductReplacementParams.setSubscriptionReplacementMode` to apply a specific replacement behavior. For the applicable rules in this case, see [Resubscribe or switch plans within the same subscription](https://developer.android.com/google/play/billing/subscriptions#resubscribe_or_switch_plans_within_the_same_subscription).
- New add-ons will apply immediately with a prorated charge to align the next renewal date with the base item in the subscription.
- Removed add-ons will expire at the end of their current billing periods.
- When launching the billing flow, you will need to specify all active items in the subscription with add-ons excluding those to be removed, along with any new add-ons.

The following sample shows how to call the [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) API when
changing an existing purchase of subscription with add-ons:  

#### Java

```java
BillingClient billingClient = ...;

int replacementMode =...;

// ProductDetails obtained from queryProductDetailsAsync().
ProductDetailsParams productDetails1 = ...;
ProductDetailsParams productDetails2 = ...;
ProductDetailsParams productDetails3 = ...;

ArrayList newProductDetailsList = new ArrayList<>();
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails1);

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setSubscriptionUpdateParams(
          SubscriptionUpdateParams.newBuilder()
              .setOldPurchaseToken(purchaseTokenOfExistingSubscription)
              // No need to set if change does not affect the base item.
             .setSubscriptionReplacementMode(replacementMode)
             .build())
        .setProductDetailsParamsList(productDetailsList)
        .build();

billingClient.launchBillingFlow(billingFlowParams);
```

### Subscription modification scenarios

The following table lists the various modification scenarios for subscription
with add-ons, and the corresponding behaviour.

#### When using SubscriptionProductReplacementParams

| Existing items | Modified items | Do you need to set the replacement mode in SubscriptionProductReplacementParams? | Behavior |
|---|---|---|---|
| A (base item), B | A (base item) | Yes (use `KEEP_EXISTING`) | - Item B is scheduled for deferred removal. - Item A is retained. - Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A | A (base item), B | Yes (use `KEEP_EXISTING` for A) | - Item B is added immediately with a prorated charge. - Item A is retained. - Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A (base item), B | A (base item), C | Yes (use `KEEP_EXISTING` for A) | - B is scheduled for deferred removal. - C is added immediately with a prorated charge. - Item A is retained. - Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A (base item), B | B (base item) | No | A is scheduled for a deferred removal. |
| A (base item), B | C (base item) | Yes | - The replacement for A -\> C depends on `SubscriptionProductReplacementParams replacementMode` - B is scheduled for deferred removal. |
| A (base item), B | C (base item), B | Yes | - The replacement for A -\> C depends on `SubscriptionProductReplacementParams replacementMode`. - To keep item B unchanged, set its replacement mode as `KEEP_EXISTING`. |
| A (base item), B | C (base item), D | Yes | - The replacement for A -\> C depends on `SubscriptionProductReplacementParams replacementMode`. - B is scheduled for deferred removal. - D is added immediately with a prorated charge. |
| A (base item), B | A (base item), C | Yes | - The replacement for A -\> A and B -\> C depends on the replacement mode provided in `SubscriptionProductReplacementParams replacementMode` in each `ProductDetailsParams`. - To keep item A unchanged set its replacement mode as `KEEP_EXISTING`. |
| A (base item), B, C | D (base item), B, C | Yes | - The replacement for A-\>D and B-\>B, C-\>C depends on the replacement mode provided in `SubscriptionProductReplacementParams replacementMode` in each `ProductDetailsParams`. - To keep items B and C unchanged, set their replacement mode as `KEEP_EXISTING`. |

#### When using SubscriptionUpdateParams

| Existing items | Modified items | Do you need to set the replacement information? | Behavior |
|---|---|---|---|
| A (base item), B | A (base item) | No | - Item B is scheduled for deferred removal. - Item A's behaviour depends on the [Base plan and offer changes](https://support.google.com/googleplay/android-developer/answer/12154973) setting of the base plan. - The pricing for item A is updated to the latest price and users may lose any introductory payments they got during signup based on offer eligibility criteria. |
| A | A (base item), B | No | - Item B is added immediately with a prorated charge. - Item A's behaviour depends on the [Base plan and offer changes](https://support.google.com/googleplay/android-developer/answer/12154973) setting of the base plan. - The pricing for item A is updated to the latest price and users may lose any introductory payments they got during signup based on offer eligibility criteria. |
| A (base item), B | A (base item), C | No | - B is scheduled for deferred removal. - C is added immediately with a prorated charge. - Item A's behaviour depends on the [Base plan and offer changes](https://support.google.com/googleplay/android-developer/answer/12154973) setting of the base plan. |
| A (base item), B | B (base item) | No | A is scheduled for a deferred removal. |
| A (base item), B | C (base item) | Yes | - The replacement for A -\> C depends on [setSubscriptionReplacementMode](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)) (deprecated in PBL 8.1). - B is scheduled for deferred removal. |
| A (base item), B | C (base item), B | Yes | The replacement for A -\> C depends on [setSubscriptionReplacementMode](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)) (deprecated in PBL 8.1). |
| A (base item), B | C (base item), D | Yes | - The replacement for A -\> C depends on [setSubscriptionReplacementMode](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)) (deprecated in PBL 8.1). - B is scheduled for deferred removal. - D is added immediately with a prorated charge. |

## Real-time developer notifications

The `subscriptionId` field isn't provided in [RTDN](https://developer.android.com/google/play/billing/rtdn-reference) for purchases
of subscription with add-ons, which contain multiple item entitlements.
Instead, your can use the Play Developer APIs to get the purchase and
see the associated item entitlements.

## Price changes for existing subscribers

Changing subscription prices for existing subscribers of a subscription
with add-ons purchase is similar to
changing the prices of single subscription as described
in [Change subscription prices](https://developer.android.com/google/play/billing/price-changes). However, there are some
limitations and functional differences as described in this section.

### End a legacy price cohort

[Ending a legacy cohort](https://developer.android.com/google/play/billing/price-changes#end-legacy) also impacts subscription with add-on purchases.
The following rules apply:

- All outstanding opt-in price increases should have the same renewal time
  with the new price. If an item in a subscription with add-ons purchase
  has an opt-in price increase which is not yet confirmed by the user,
  any new opt-in price increase for other items in the purchase
  will be ignored unless it results in the same
  renewal time of new price application as
  the existing price increase in [OUTSTANDING](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pricechangestate) state. Once the user
  confirms the price increase any newer price changes would be registered.
  And users can only accept all unconfirmed opt-in price increases at once.

  Example:
  - Consider a subscription with add-ons (items A and B), renews on 7th of every month.
  - Item A has an ongoing price migration from $7 to $10, and the price increase is expected to be applicable on July 7.
  - A new price migration from $5 to $6, starts for item B on June 2. Since the opt-in price increase starts 37 days after migration, for earliest price increase for item B will be on Aug 7.

  In this scenario, until the user accepts the price change for
  item A (until it is in [CONFIRMED](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pricechangestate) state), price change for item B
  isn't registered for this subscription purchase,
  and [SubscriptionPurchaseV2](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) doesn't return
  price change details for item B. After the user confirms the
  price change for item A, the price change of item B starts. The user
  receives the item B opt-in price increase only after accepting
  the opt-in increase for item A.
- Google Play's email contains a list of all the items with price increases or
  decreases taking effect on the same day.

## Cancel subscription with add-ons

Users can cancel the entire purchase of a subscription with add-ons
on Play Subscription Center, and you can only cancel the entire purchase
of a subscription with add-ons by using the Google Play Developer API.

When a subscription purchase is canceled without being revoked, none of
the items in the purchase will auto-renew, but the user will continue
to have access to the entitled items, including any free trials, until the
corresponding billing periods end.

## Revoke and refund subscriptions with add-ons

The following are some of the guidelines for revoking and refunding
subscriptions:

- Use Play Console to issue an amount based refund for a specific Order
  without revoking access to the subscription.

- Call [`orders.refund`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund) to fully refund specific subscription payments
  the user has made without revoking access to the subscription.

  | **Note:** Don't call [`purchases.subscriptions.refund (deprecated)`](https://developer.android.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/refund) for a subscription with add-ons.
- Call [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) to immediately revoke access
  to all subscription items. With this API, you can:

  - Revoke access to all the items and provide a [prorated](https://developer.android.com/google/play/billing/manage-purchases#prorate_refunds) refund.

  - When revoking a subscription with add-ons using prorated refunds, a refund
    will be issued for the latest order of each item with a prorated
    amount based on the time remaining until the next renewal.

  - Revoke access for all the items and provide a [FullRefund](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke#revocationcontext).

  - [Revoke individual item's](https://developer.android.com/google/play/billing/subscription-with-addons#revoke-item) access with full refund on
    the item.

### Revoke individual item in a subscription with add-ons

To revoke individual subscription items in a subscription with
add-ons without revoking the entire purchase, call
[`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) with `ItemBasedRefund` field
set in the `RevocationContext`. The `productId` of the item that should
be revoked and refunded can be set in the `ItemBasedRefund` field.

The `ItemBasedRefund` field can be set for purchases with one or more
auto-renewing subscription items.

- If there are still active items remaining in the subscription purchase after revoking the item specified in `ItemBasedRefund`, only the item will be revoked, and fully refunded without interrupting the subscription status.
- If there are no active items remaining in the subscription purchase after revoking the item specified in `ItemBasedRefund`, the item is revoked, fully refunded, and the subscription is canceled.

#### Considerations

- When using the `ItemBasedRefund` only one item can be revoked at a time. The request can be called multiple times if different items need to be revoked.
- When the subscription purchase is in any of the payment declined states, or the item specified in `ItemBasedRefund` is not owned or expired, the item turn down is blocked.
- Item turn down isn't supported in prepaid subscription.

## Defer billing

You can advance the next billing date for a subscription with add-ons using
the [`Purchases.subscriptionsv2:defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method.

When you defer a subscription with add-ons, all items in the subscription are
deferred by the same duration. During the deferral period, the user retains
full access to all items but is not charged. The renewal date for all items is
updated to the new date.

This can be useful for promotions or customer goodwill gestures. Billing can be
deferred by as little as one day and up to one year per API call. You can call
the API multiple times to extend the deferral before the new billing
date arrives.

A `SUBSCRIPTION_DEFERRED` real-time developer notification is triggered when
this action is taken.

## Item expiration during payment decline

For a purchase of subscription with add-ons, certain renewals may only need
to extend a subset of item entitlements, without affecting items
with a future expiry date.

Regardless of which items are involved in a renewal, if the renewal payment is
declined, the overall subscription purchase will enter grace period and account
hold as described in the following documentation.

### Recovery period selection

As grace period itself still grants the user entitlement, upon a purchase
of subscription with add-ons, renewal payment is declined, the item
with the *minimum* grace period over all active items is selected, and its
grace period and account hold period as the recovery period is applied for
this renewal.

Active items includes items that were active in the purchase of a subscription
with add-ons just prior to the renewal attempt, excludes any newly added items
(which won't be entitled until after recovery), and excludes any items that are
no longer active due to removal or turndown.

The account hold setting of the item with the minimum grace period selected
is applied. If there are more than one items with the minimum grace period,
but different account hold periods, the longest account hold period is applied.

### Grace period

When a subscription renewal payment is declined, the subscription purchase will
enter grace period state. During the grace period, the user will continue to
have access to all active items from the previous renewal period. After the
grace period, if the payment method hasn't been fixed, the entire subscription
purchase goes into account hold. If any other items reach their renewal
date during grace period, a new charge attempt will be initiated for those items
once the subscription recovers from payment decline.

### Account hold

While the subscription purchase is in account hold, access to all subscription
items is suspended until payment recovers.

If the subscription in account hold is recovered, the subscription purchase
continues existing as is. If the subscription is not recovered, the items in
payment decline will expire, and access to the other items will be resumed for
the remainder of their billing periods.

Example:

- A user has a subscription *My Base Plan* renewing at the 1st of
  every month, then on Aug 15, adds a $10 per month
  *Add on plan* with a seven-day free trial. Neither of the items
  have grace period set, and they both have 30-day account hold period.

- On the Aug 22, the user is charged $2.90 (10\*9/31) to prorate until
  Aug 31, but the user's payment method expires before then, and the
  subscription falls into payment decline on Aug 22.

When the subscription enters account hold due to payment decline, the user
does not have access to any of the items in the subscription with add-ons.
The remaining time for the items that are not being renewed will
be given back to users when the subscription exits account hold, either
because payment has been recovered or canceled.

In the previous example, a subscription enters account hold on Aug 22.

- If the account is recovered on Aug 25, before the broader renewal date
  on Sep 1, the user regains access to both *My Base Plan* , and
  *Add on plan* the same day. Next billing date is changed to Sep 4.

- If the account isn't recovered after 30 days, the subscription is canceled
  on Sep 21 and the user loses access to the *Add on plan* , and resume access
  to *My Base Plan* until Sep 30.

In this example, you must get the updated `expiryTime` for ALL items in the
subscription with add-ons, as some items may resume their entitlement after
the grace period and account hold.

## Financial reporting and reconciliation

Use the [Earnings report](https://support.google.com/googleplay/android-developer/answer/6135870) to reconcile your active subscriptions with
transactions on Play. Each transaction line item has an order ID. With
purchases representing several items, the [Earnings and Estimated sales
reports](https://support.google.com/googleplay/android-developer/answer/2482017) will include separate rows for each transaction such as charge,
fee, tax, and refund, for each item involved.

For dashboards in the Play Console:

- The revenue statistics presented in the **Financial reporting** section of
  the console are broken down by items.

- Order management reflects purchase of subscription with add-ons, and show
  itemized lists of what was purchased. From order management, you may
  revoke, cancel or fully refund a user's purchase.