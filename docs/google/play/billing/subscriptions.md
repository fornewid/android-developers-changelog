---
title: https://developer.android.com/google/play/billing/subscriptions
url: https://developer.android.com/google/play/billing/subscriptions
source: md.txt
---

This document describes how to handle subscription lifecycle events, such as
renewals and expirations. It also describes additional subscription features
such as offering promotions and allowing your users to manage their own
subscriptions.

If you haven't configured subscription products for your app, see [Create and
configure your products](https://developer.android.com/google/play/billing/getting-ready#products).

## Subscriptions overview

A *subscription* is a recurring transaction that grants specific entitlements to
users. The entitlements represent a set of benefits users can access during a
specified time period. For example, a subscription might entitle a user for a
premium access.

Through *base plans* and *offers*, you can create multiple configurations for
the same subscription product. For example, you can create an introductory offer
for users who have never subscribed to your app. Similarly, you can create an
upgrade offer for users who are already subscribed.

For a detailed overview of subscription products, base plans, and offers, see
the documentation in the [Play Console Help
Center](https://support.google.com/googleplay/android-developer/answer/12154973).

The Play Billing Library supports the following subscription types:

- Subscription - In this type, one item corresponding to one
  entitlement. For example, subscription to a music streaming service.

- Subscription with add-ons - In this type, one purchase can have several
  distinct entitlements bundled in a single purchase. For example,
  subscription to both music streaming service, and a video subscription. For
  information specific to subscription with add-ons, see [Subscriptions with
  add-ons](https://developer.android.com/google/play/billing/subscription-with-addons).

## Prepaid plans integration

Prepaid plans **do not** automatically renew upon expiration. To extend their
subscription entitlement without interruption, the user must *top-up* a prepaid
plan for the same subscription.

For top-ups, launch the billing flow as you would with the original purchase.
You don't need to indicate that a purchase is a top-up.

Prepaid plan top-ups always use the `CHARGE_FULL_PRICE` replacement mode, and
you don't need to set this mode explicitly. The user is immediately charged for
a full billing period, and their entitlement is extended by the duration
specified in the top-up.

After a top-up, the following fields in the
[`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase) result object
are updated to reflect the most recent top-up purchase:

- Order ID
- Purchase time
- Signature
- Purchase token
- Acknowledged

The following `Purchase` fields always contain the same data found in the
original purchase:

- Package name
- Purchase state
- Products
- Auto renewing

### Prepaid purchase acknowledgement

Similar to auto-renewing subscriptions, you must acknowledge prepaid plans after
purchase. Both the initial purchase and any top-ups need to be acknowledged. For
more information, see [Processing
purchases](https://developer.android.com/google/play/billing/integrate#process).

Due to the potential for short prepaid plan durations, it is important to
acknowledge the purchase as soon as possible.

Prepaid plans with a duration of one week or longer must be acknowledged within
three days.

Prepaid plans with a duration shorter than one week must be acknowledged within
half the plan duration. For example, developers have 1.5 days to acknowledge a
three-day prepaid plan.
| **Warning:** If a user on a prepaid plan purchases a top-up, and you do not acknowledge the purchase within the corresponding period, the top-up purchase is revoked, the remaining subscription is revoked and canceled, and the user is issued a refund.

## Installment subscriptions integration

An installment subscription is a type of subscription where users pay for the
subscription in multiple installments over a period of time, rather than paying
the entire subscription fee upfront.

Additional considerations for installment subscriptions:

- **Country availability**: Installment subscriptions feature is only available in Brazil, France, Italy, and Spain (check Console for latest availability).
- **Setting the price**: When setting the price for an installment subscription on the Console, the price represents the monthly payment amount. This, combined with the commitment period that is set, generates the total amount for the subscription in the purchase screen.
- **Commitment period**: The total duration of the initial subscription commitment, during which monthly payments are required. For example, if a base plan has a 15-month commitment period, the user will make 15 monthly payments over this period.
- **Renewals**: In the context of installment subscriptions, "renewal" signifies the conclusion of a commitment period, either initial commitment period or subsequent commitment period. Following the initial sign up, the first renewal occurs upon completion of the entire initial commitment period. Subsequent renewals occur after each subsequent commitment period is fulfilled. The renewal types for installment subscriptions can be "auto-renews monthly" or "auto-renews for the same duration". For "auto-renews monthly", there is no subsequent commitment and the plan behaves like a monthly subscription where each monthly subscription charge constitutes a renewal.
- **Billing period**: In the context of installment subscriptions, this refers to the recurring interval at which individual payments are made, as specified in the base plan.
- **Plan change vs. price change behaviors**: For price changes and cancellations, the commitment is firm. This means that if a user wants to cancel or a developer wants to change the price, the change takes effect at the end of a commitment period. For plan changes, the commitment is not firm. This means that the plan change does not have to wait until the end of a commitment period, it takes effect either immediately or on the next payment date based on the set replacement mode.
- **Same-subscription plan change**: Plan change from an installments base plan to a non-installments base plan of the same subscription product is not allowed.
- **Real-time developer notifications (RTDNs)** : A
  `SUBSCRIPTION_CANCELLATION_SCHEDULED` RTDN is sent immediately upon
  user-initiated cancellation when payments remain for the commitment period.
  The cancellation is pending and will only take effect at the end of the
  commitment period. Then, if not restored by the user,
  `SUBSCRIPTION_CANCELED` and `SUBSCRIPTION_EXPIRED` RTDNs are sent at the end
  of the commitment period.

- **Payouts / Revenue realization**: Developer payouts will happen as users
  make their monthly payments, subject to the same terms as all other
  subscriptions. Developers are not paid upfront when the user signs up for
  the installment subscription.

- **Missed payment collections**: If a user fails to make any installment
  subscription payments, neither Google nor Developer will attempt to collect
  any such missed or outstanding payments from the user, except that Google may
  periodically retry the payment during any applicable Grace Period or Account
  Hold period in accordance with its normal payment retry practices. Google
  won't be responsible to the Developer for any remaining unpaid installment
  payments.

- **Play Billing Library availability** : The `installmentDetails` field is
  only available for PBL 7 or later. For PBL 5 and later, the installment
  subscription is returned using `queryProductDetails()`, but the subscription
  won't include detailed installment information like committed payments count
  of the plan.

## Use deep links to allow users to manage a subscription

Your app should include a link on a settings or preferences screen that allows
users to manage their subscriptions, which you can incorporate into your app's
natural look and feel.

You can include a deep link from your app to the Google Play subscriptions
center for non-expired subscriptions, which you can determine using the
`subscriptionState` field of the [subscription resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2). Based on this,
there are several ways you can deep link into the Play Store subscriptions
center.

### Link to the subscriptions center

Use the following URL to direct users to the page that shows all of their
subscriptions, as shown in figures 1 and 2:

    https://play.google.com/store/account/subscriptions

![The Play Store subscriptions screen shows status for all of a user's Google Play-billed subscriptions.](https://developer.android.com/static/images/google/play/billing/sub_center_general.png) **Figure 1.** The Play Store subscriptions screen shows status for all of a user's Google Play-billed subscriptions.

<br />

![Tap on a subscription to see additional details.](https://developer.android.com/static/images/google/play/billing/sub_management_mock_general.png) **Figure 2.** Tap on a subscription to see additional details.

This deep link could be useful to help a user restore a canceled subscription
from the Play Store subscriptions center.

### Link to a specific subscription management page (recommended)

To directly link to the management page for a non-expired subscription, indicate
the package name and `productId` associated with the purchased subscription. To
programmatically determine the `productId` for an existing subscription, query
your app's backend or call [`BillingClient.queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) for a list
of subscriptions associated with a particular user. Each subscription contains
the corresponding `productId` as part of the subscription status information.
Each [`SubscriptionPurchaseLineItem`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem) object associated with a
subscription purchase contains the `productId` value associated with the
subscription that the user purchased in that line item.
| **Note:** You set the product ID in the Play Console when you define the subscription, or using the Google Play Developer API as part of the [`Subscription`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#resource:-subscription) object sent in [monetization.subscriptions.create](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/create) and [monetization.subscriptions.patch](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch).

Use the following URL to direct users to a specific subscription management
screen, replacing "your-sub-product-id" and "your-app-package" with the
`productId` and app package name respectively:

    https://play.google.com/store/account/subscriptions?sku=your-sub-product-id&package=your-app-package

The user is then able to manage their payment methods and access features
including cancellation, resubscription, and pause.

## Allow users to upgrade, downgrade, or change their subscription

You can provide existing subscribers with various options to change their
subscription plan to better meet their needs:

- If you sell multiple subscription tiers, such as "basic" and "premium" subscriptions, you can allow users to switch tiers by purchasing a different subscription's base plan or offer.
- You can allow users to change their current billing period, such as switching from a monthly to an annual plan.
- You can also allow users to switch between auto-renewing and prepaid plans.

You can encourage any of these changes by providing subscription offers to
provide a discount to eligible users. For example, you could create an offer
providing a 50% discount on the first year when switching from a monthly to an
annual plan, and limit this offer to users subscribed to a monthly plan who
haven't purchased this offer. More information on offer eligibility criteria is
available [in the Help Center](https://support.google.com/googleplay/android-developer/answer/12154973?sjid=13996822054844635277-NA#offer_eligibility)

Figure 3 shows an example app with three different plans:
![This app has three subscription tiers..](https://developer.android.com/static/images/google/play/billing/plan_change_inapp.png) **Figure 3.** This app has three subscription tiers.

Your app could show a screen similar to figure 3, giving users options to change
their subscription. In all cases, it should be clear to users what their current
subscription plan is, and what options they have for changing it.

When users decide to upgrade, downgrade, or change their subscription, you
specify a *replacement mode* that determines how the prorated value of the
current paid billing period is applied, and when any entitlement change occurs.

### Replacement modes

The following table lists available replacement modes and example usage, and
count of payments considered paid.
| **Note:** For installment subscriptions, all replacement modes are supported. Additionally, after a replacement occurs for installment subscriptions, it is possible that the first committed payment of the new plan will be recorded as paid depending on the replacement mode.

|---|---|---|---|
| Replacement mode | Description | Example usage | Committed payments recorded as paid (For installment subscription replacement) |
| `WITH_TIME_PRORATION` | The subscription item is upgraded or downgraded immediately. Any time remaining is adjusted based on the price difference, and credited toward the new subscription by pushing forward the next billing date. This is the default behavior. | Upgrade to a more expensive tier, without any immediate additional payment. | 0 |
| `CHARGE_PRORATED_PRICE` | The subscription item is upgraded immediately, and the billing cycle remains the same. The price difference for the remaining period is then charged to the user. **Note:** This option is available only for a subscription item upgrade, where the price per unit of time increases. | Upgrade to a more expensive tier, without changing the billing date. | 1 |
| `CHARGE_FULL_PRICE` | The subscription item is upgraded or downgraded immediately, and the user is charged full price for the new entitlement immediately. The remaining value from the previous subscription is either carried over for the same entitlement, or prorated for time when switching to a different entitlement. **Note:** If the new subscription has a free trial or introductory offer, the user is charged $0 or the price of the introductory offer, whichever applies, at the time of upgrade or downgrade. | Upgrade from shorter to longer billing period. | 1 (Note: 0 if the new subscription has a free trial.) |
| `WITHOUT_PRORATION` | The subscription item is upgraded or downgraded immediately, and the new price is charged when the subscription renews. The billing cycle remains the same. | Upgrade to a higher subscription tier while retaining any remaining free period. | 0 |
| `DEFERRED` | The subscription item is upgraded or downgraded only when the subscription renews, but the new purchase is issued immediately with the following two items: - The existing item with auto renew disabled and expiry time set to the end of current billing cycle. - The new entitlement which begins after the existing item expires. You can allow users to make additional changes if they want. For example, users can revert to the original plan or initiate a new deferred plan change. **Note:** For installment subscriptions, the plan change occurs at the start of the next payment date. | Downgrade to a less expensive tier. | 1 |
| `KEEP_EXISTING` | The payment schedule for the subscription item remains unchanged in the replacement. | Add or remove subscription item from a subscription with add-ons when a specific item should be unchanged. | N/A |

| **Note:** In Play Billing Library version 5 and lower, replacement modes were represented by `ProrationMode`. The new [`ReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode) enum includes equivalent modes for all proration modes. `ReplacementMode.DEFERRED` includes some improvements to make it simpler to manage deferred changes of plan. The user experience is exactly the same. Read the [Replacement examples and
| behaviors](https://developer.android.com/google/play/billing/subscriptions#replacement-examples) section to learn more.

To learn more about different upsell and winback applications of upgrade or
downgrade offers, read the offers and promotions guide.

#### Set the replacement mode for a purchase

You can use different replacement modes for different types of subscription
transitions, based on your preferences and business logic. This section explains
how to set a replacement mode for a change in a subscription and the limitations
that apply.

##### Resubscribe or switch plans within the same subscription

You can specify a default replacement mode in the Google Play Console. This
setting lets you choose when to charge current subscribers if they purchase a
different base plan or offer for the same subscription or resubscribe after a
cancellation. The available options are *Charge immediately* , equivalent to
`CHARGE_FULL_PRICE`, and *Charge at the next billing date* , equivalent to
`WITHOUT_PRORATION`. These are the only relevant replacement modes when
switching base plans within the same subscription.

For example, if you are implementing a winback offer for the same plan after the
user cancels but before the subscription ends, you can process the new purchase
as a regular purchase without indicating any values in
`SubscriptionUpdateParams`. The system uses the default replacement mode you
configured in the subscription and automatically handles the plan transition
from the old purchase to the new purchase.

##### Switch plans across subscriptions, or override the default replacement mode

If the user is changing subscription *products---purchasing* a different
subscription---or if you want to override the default replacement mode for any
reason, you specify the proration rate *at runtime* as part of the purchase flow
parameters.

To correctly provide
[`ReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode)
in `SubscriptionProductReplacementParams` or `SubscriptionUpdateParams` as part
of your runtime purchase flow configuration, note the following restrictions:

- When upgrading, downgrading, or initiating doing a same-subscription switch **to** a prepaid plan **from** either a prepaid plan, auto-renewing plan, or installment plan, the only allowed replacement mode is `CHARGE_FULL_PRICE`. If you specify any other replacement mode, the purchase fails and an error is shown to the user.
- When switching plans within the same subscription **to** an auto-renewing plan **from** either a prepaid plan or an auto-renewing plan, valid proration modes are `CHARGE_FULL_PRICE` and `WITHOUT_PRORATION`. If you specify any other proration mode, the purchase fails and an error is shown to the user.
- Switching plans within the same subscription product from an installments base plan to a non-installments base plan is not allowed.
- When using `KEEP_EXISTING` replacement mode in `SubscriptionProductReplacementParams` to keep an item's payment unchanged during replacement, the old product ID should be the same as the new product's product ID. The `KEEP_EXISTING` mode isn't supported in [`SubscriptionUpdateParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams).

### Replacement examples and behaviors

To understand how each proration mode works, consider the following scenario:

Samwise has a subscription to online content from the Country Gardener app. He
has a monthly subscription to the **Tier 1** version of the content, which is
text-only. This subscription costs him **$2 per month**, and it renews on the
first of the month.

On April 15, Samwise chose to upgrade to the annual version of the **Tier 2**
subscription, which includes video updates and costs **$36 per year**.

When upgrading the subscription, the developer selects a proration mode. The
following list describes how each proration mode affects Samwise's subscription:

`WITH_TIME_PRORATION`

Samwise's **Tier 1** subscription ends immediately. Because he paid for a full
month (April 1-30) but upgraded halfway through the subscription period, half of
a month's subscription ($1) is applied to his new subscription. However, because
that new subscription costs $36 per year, the $1 credit balance pays for only 10
days (April 16-25); so on April 26, he is charged $36 for a new subscription and
another $36 on April 26th of each year following.

You should call your app's [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) the moment the
purchase succeeds, and you are able to retrieve the new purchase as part of a
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) call. Your backend immediately receives a
`SUBSCRIPTION_PURCHASED` Real Time Developer Notification.

`CHARGE_PRORATED_PRICE`

This mode can be used because the **Tier 2** subscription price per time unit
($36/year = $3/month) is greater than the **Tier 1** subscription price per time
unit ($2/month). Samwise's **Tier 1** subscription ends immediately. Because he
paid for a full month but used only half of it, half of a month's subscription
($1) is applied to his new subscription. However, because that new subscription
costs $36/year, the remaining 15 days costs $1.50; so he is charged the
difference of $0.50 for his new subscription. On May 1st, Samwise is charged $36
for his new subscription tier and another $36 on May 1 of each year following.

You should call your app's [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) the moment the
purchase succeeds, and you are able to retrieve the new purchase as part of a
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) call. Your backend immediately receives a
`SUBSCRIPTION_PURCHASED` Real Time Developer Notification.

`WITHOUT_PRORATION`

Samwise's **Tier 1** subscription is immediately upgraded to **Tier 2** with no
extra charge, and on May 1st he is charged $36 for his new subscription tier and
another $36 on May 1 of each year following.

You should call your app's [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) the moment the
purchase succeeds, and you are able to retrieve the new purchase as part of a
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) call. Your backend immediately receives a
`SUBSCRIPTION_PURCHASED` Real Time Developer Notification.

`DEFERRED`

Samwise's **Tier 1** subscription continues until it expires on April 30. On May
1st, the **Tier 2** subscription takes effect, and Samwise is charged $36 for
his new subscription tier.

You should call your app's [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) the moment the
purchase succeeds, and you are able to retrieve the new purchase as part of a
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) call. Your backend immediately receives a
`SUBSCRIPTION_PURCHASED` Real Time Developer Notification. You should [process
the purchase](https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto) the same way you would process any other new purchase at that
point. In particular, make sure you acknowledge the new purchase. Note that the
`startTime` of the new subscription is populated at the moment the replacement
is effective, which happens when the old subscription expires. At that point,
you receive a `SUBSCRIPTION_RENEWED` RTDN for the new subscription plan. Read
more about the `ReplacementMode.DEFERRED` behavior in [Handle deferred
replacement](https://developer.android.com/google/play/billing/subscriptions#handle-deferred-replacement).

`CHARGE_FULL_PRICE`

Samwise's **Tier 1** subscription ends immediately. His **Tier 2** subscription
begins today and he is charged $36. Because he paid for a full month but used
only half of it, half of a month's subscription ($1) is applied to his new
subscription. Because that new subscription costs $36/year, he would get 1/36th
of a year added on to his subscription period (\~10 days). Therefore, Samwise's
next charge would be 1 year and 10 days from today for $36. After that, he is
charged $36 each year following.

When choosing a proration mode, be sure to review our [replacement
recommendations](https://developer.android.com/google/play/billing/subscriptions#replacement-recommendations).

`KEEP_EXISTING`

Samwise has a subscription to online content from the Country Gardener app. He
has a monthly subscription to the Plan 1 for basic content. This subscription
costs an introductory price of $2 per month for 3 months and then $4 per month.
Samwise purchased this on 1st of April. Country Gardener app offers Plan 2 as an
add-on speciality content for $3 per month. On April 15, Samwise added Plan 2 to
his subscription of Country Gardener app while keeping existing Plan 1.
Samwise's payment schedule is as follows:

- A prorated price of $1.50 for Plan 2, due on April 15.
- A price of $5.00 per month for the subsequent 2 months covering both introductory price for Plan 1 and the regular price for Plan 2.
- Thereafter, a consistent monthly payment of $7.00.

### Trigger subscription changes in-app

Your app can offer users an upgrade or downgrade using the same steps as with
[launching a purchase flow](https://developer.android.com/google/play/billing/integrate#launch). However, when upgrading or downgrading, you
need to provide details of the current subscription, the future (upgraded or
downgraded) subscription, and the replacement mode to use.

#### Use SubscriptionProductReplacementParams for replacement (preferred)

The following example shows how to update a subscription by using
`SubscriptionProductReplacementParams`.

- The [`BillingFlowParams.ProductDetailsParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams) object now
  has a `setSubscriptionProductReplacementParams()` method to specify
  product level replacement information.

- `SubscriptionProductReplacementParams` has two setter methods:

  - `setOldProductId:`This is the old product to be replaced by the product in current `ProductDetails.`
  - `setReplacementMode:`This is the item level replacement mode. The modes are essentially the same as `SubscriptionUpdateParams`, but the value mapping has been updated.
- The existing purchase level update params
  `BillingFlowParams.setSubscriptionUpdateParams()` should be constructed
  with `setOldPurchaseToken()`.

- Once `setSubscriptionProductReplacementParams()` is called for any
  of the `ProductDetailsParams`,
  `SubscriptionUpdateParams.setSubscriptionReplacementMode()`
  will have no effect.

The following code sample demonstrates how to change a subscription plan
from (`old_product_1`, `old_product_2`) to (`product_1`, `product_2`,
`product_3`). In this scenario, `product_1` replaces `old_product_1`,
`product_2` replaces `old_product_2`, and `product_3` is added to
the subscription immediately.

### Kotlin

```kotlin
val billingClient: BillingClient = ...
val replacementModeForBasePlan: Int = ...
val replacementModeForAddon: Int = ...

val purchaseTokenOfExistingSubscription: String = "your_old_purchase_token"

// ProductDetails instances obtained from queryProductDetailsAsync();

val productDetailsParams1 =
    ProductDetailsParams.newBuilder()
        .setProductDetails(productDetails1_obj) // Required: Set the ProductDetails object
        .setSubscriptionProductReplacementParams(
            SubscriptionProductReplacementParams.newBuilder()
                .setOldProductId("old_product_id_1")
                .setReplacementMode(replacementModeForBasePlan)
                .build()
        )
        .build()

val productDetailsParams2 =
    ProductDetailsParams.newBuilder()
        .setProductDetails(productDetails2_obj) // Required: Set the ProductDetails object
        .setSubscriptionProductReplacementParams(
            SubscriptionProductReplacementParams.newBuilder()
                .setOldProductId("old_product_id_2")
                .setReplacementMode(replacementModeForAddon)
                .build()
        )
        .build()

// Example for a third item without replacement params
val productDetailsParams3 =
    ProductDetailsParams.newBuilder()
        .setProductDetails(productDetails3_obj) // Required: Set the ProductDetails object
        .build()

val newProductDetailsList = listOf(
    productDetailsParams1,
    productDetailsParams2,
    productDetailsParams3
)

val billingFlowParams =
    BillingFlowParams.newBuilder()
        .setSubscriptionUpdateParams(
            SubscriptionUpdateParams.newBuilder()
                .setOldPurchaseToken(purchaseTokenOfExistingSubscription)
                .build()
        )
        .setProductDetailsParamsList(newProductDetailsList)
        .build()

// To launch the billing flow:
// billingClient.launchBillingFlow(activity, billingFlowParams)
```

### Java

```java
BillingClient billingClient = ...;

int replacementModeForBasePlan =...;
int replacementModeForAddon =...;
// ProductDetails obtained from queryProductDetailsAsync().
ProductDetailsParams productDetails1 =
  ProductDetailsParams.newBuilder()
      .setSubscriptionProductReplacementParams(
           SubscriptionProductReplacementParams.newBuilder()
               .setOldProductId("old_product_id_1")
               .setReplacementMode(replacementModeForBasePlan))
               .build();
ProductDetailsParams productDetails2 =
  ProductDetailsParams.newBuilder()
      .setSubscriptionProductReplacementParams(
           SubscriptionProductReplacementParams.newBuilder()
               .setOldProductId("old_product_id_2")
               .setReplacementMode(replacementModeForAddon))
               .build();
ProductDetailsParams productDetails3 = ...;

ArrayList newProductDetailsList = new ArrayList<>();
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails2);
newProductDetailsList.add(productDetails3);

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setSubscriptionUpdateParams(
          SubscriptionUpdateParams.newBuilder()
              .setOldPurchaseToken(purchaseTokenOfExistingSubscription)
             .build())
        .setProductDetailsParamsList(productDetailsList)
        .build();

billingClient.launchBillingFlow(billingFlowParams);
```

#### Set SubscriptionUpdateParams for replacement (deprecated)

| **Note:** Starting with the PBL 8.1 release, [`SubscriptionUpdateParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams) is deprecated. Alternately, use `SubscriptionProductReplacementParams` to specify the replacement parameters.

The following example shows how to update a subscription by using
`SubscriptionUpdateParams`.

### Kotlin

```kotlin
val offerToken = productDetails
        .getSubscriptionOfferDetails(selectedOfferIndex)
        .getOfferToken()

val billingParams = BillingFlowParams.newBuilder().setProductDetailsParamsList(
       listOf(
           BillingFlowParams.ProductDetailsParams.newBuilder()
               .setProductDetails(productDetails)
               .setOfferToken(offerToken)
               .build()
       )
       ).setSubscriptionUpdateParams(
           BillingFlowParams.SubscriptionUpdateParams.newBuilder()
               .setOldPurchaseToken("old_purchase_token")
               .setSubscriptionReplacementMode(
                 BillingFlowParams.ReplacementMode.CHARGE_FULL_PRICE
               )
               .build()
       ).build()

billingClient.launchBillingFlow(
    activity,
    billingParams
   )
// ...
```

### Java

```java
String offerToken = productDetails
    .getSubscriptionOfferDetails(selectedOfferIndex)
    .getOfferToken();

BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(
        ImmuableList.of(
            ProductDetailsParams.newBuilder()
                // fetched via queryProductDetailsAsync
                .setProductDetails(productDetails)
                // offerToken can be found in
                // ProductDetails=>SubscriptionOfferDetails
                .setOfferToken(offerToken)
                .build()))
    .setSubscriptionUpdateParams(
        SubscriptionUpdateParams.newBuilder()
            // purchaseToken can be found in Purchase#getPurchaseToken
            .setOldPurchaseToken("old_purchase_token")
            .setSubscriptionReplacementMode(ReplacementMode.CHARGE_FULL_PRICE)
            .build())
    .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
// ...
```

#### Replacement recommendations

The following table shows diferrent proration scenarios along with what we
recommend for each scenario:

| Scenario | Recommended replacement mode | Result |
|---|---|---|
| Upgrading to a more expensive tier | `CHARGE_PRORATED_PRICE` | The user receives access immediately while keeping the same billing period. |
| Downgrading to a less expensive tier | `DEFERRED` | The user already paid for the more expensive tier, so they keep access until the next billing date. |
| Upgrading while in a free trial, keeping the trial | `WITHOUT_PRORATION` | The user upgrades to a higher tier for the remainder of the trial period without extra charge. |
| Upgrading while in a free trial - ending access to the free trial | `CHARGE_PRORATED_PRICE` | The user receives access to the new tier immediately, the remaining value of the free trial is carried over. The carried over value is calculated based on base plan pricing. |
| Keeping payment schedule of some subscription items unchanged while adding or removing other subscription items from Subscription with add-ons. | `KEEP_EXISTING` | The user keeps paying the old price for the unchanged item. New items are added immediately. Other old items can be replaced by specifying a replacement mode or removed. |

### Handle subscription change purchases

Changes of plan are new purchases for all terms and purposes, and they should be
processed and acknowledged as such after the billing flow completes
successfully. In addition to processing the new purchase appropriately, you have
to retire the purchase that is being replaced.

The in-app behavior is the same as for any new purchase. Your app receives the
outcome of the new purchase in your [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener), and the
new purchase is available in [`queryPurchasesAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)).

The Google Play Developer API returns a `linkedPurchaseToken` in the
[subscription resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) when a purchase replaces an existing
one. You can check `itemReplacement` under `SubscriptionPurchaseLineItem` in
the new purchase to understand the item level replacement details.
Additionally, you can use the `offerPhase` field to identify the current offer
phase (such as a proration period or free trial) for the new subscription in order to provide customized user experiences. Be
sure to invalidate the token provided in the `linkedPurchaseToken` to
ensure that the old token is not used to gain access to your services. See
[Upgrades, downgrades, and resignups](https://developer.android.com/google/play/billing/lifecycle/subscriptions#upgrades-downgrades) for information on handling upgrade
and downgrade purchases.

When you receive the new purchase token, follow the same verification process as
with [verifying a new purchase token](https://developer.android.com/google/play/billing/integrate#process). Make sure to acknowledge these
purchases with [`BillingClient.acknowledgePurchase()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgepurchase) from the Google Play
Billing Library or [`Purchases.subscriptions:acknowledge`](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/acknowledge) from
the Google Play Developer API.

#### Handle deferred replacement

Deferred replacement mode lets you let a user use up the remaining entitlement
in their old plan before starting on the new plan.

When you use [ReplacementMode.DEFERRED](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode#DEFERRED) for a new purchase,
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) returns a new purchase token after the purchase
flow that remains associated with the old product until the deferred replacement
takes place on the next renewal date, after which the new product is returned.

In the past you could achieve this user experience with the deprecated
`ProrationMode.DEFERRED`, but `ProrationMode.DEFERRED` is deprecated with Play
Billing Library 6. See the following table to understand where the behavior
differs:

|---|---|---|
| Time | ProrationMode.DEFERRED (deprecated) | ReplacementMode.DEFERRED |
| Right after the purchase flow succeeds (app) | [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) is invoked after purchase with a status of whether the upgrade or downgrade was successful. Entitlement to the old plan continues until the next renewal date. To ensure that the app gives the right entitlement, [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) returns a Purchase object with the **original** purchase token and the **original** entitlement until replacement occurs. The new purchase token is not surfaced, so it can't be processed at this point. | [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) gets invoked after purchase with a status of whether the upgrade or downgrade was successful. [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) returns purchase with the **new** purchase token right away, and the **original entitlement** associated with it. The new purchase token is surfaced, so it should be [processed](https://developer.android.com/google/play/billing/integrate#process) at this point taking into account when the replacement is to take place. |
| Right after the purchase flow succeeds (backend) | SUBSCRIPTION_PURCHASED RTDN is **not** sent after the purchase flow. The backend is not made aware of the new purchase yet. | SUBSCRIPTION_PURCHASED RTDN with the old product_id is sent immediately after the purchase flow for the new purchase token. Calling the [purchases.subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method with the new purchase token returns a purchase having a 'startTime' indicating the purchase time with **two line items**: - One representing the **old** entitlement and has an 'expiryTime' in the future. The old entitlement will not be renewed and has a [DeferredItemReplacement](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#DeferredItemReplacement) containing the product of the **new** entitlement. This indicates a pending replacement of the old entitlement upon its expiration. - One representing the **newly purchased** entitlement. It has no value set for 'expiryTime'. SUBSCRIPTION_EXPIRED sent for the **old** purchase token. When calling the [purchases.subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method with the **old** purchase token, it appears as expired (the entitlement for the old plan is transferred to the new purchase for the remaining time). |
| On replacement - first renewal after the purchase flow (app) | [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) returns a new Purchase object with the **new** purchase token and entitlement. The new purchase token is now surfaced, so it should be [processed](https://developer.android.com/google/play/billing/integrate#process). | [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) returns purchase with the **new** purchase token right away, and the **new entitlement** associated with it. The new purchase should have been processed already when the purchase flow succeeded, so the app shouldn't take any special action apart from making sure the right entitlement is granted. |
| On replacement - first renewal after the purchase flow (backend) | The new purchase can now be processed and acknowledged when the first SUBSCRIPTION_RENEWED RTDN is sent. The `linkedPurchaseToken` in the subscription resource can be used to determine which user in your subscription backend, if applicable, should be updated with the new entitlement. | New purchase was processed and acknowledged when the SUBSCRIPTION_PURCHASED RTDN was sent for the new purchase token and recorded as the 'startTime'. With ReplacementMode.DEFERRED, first renewals follow the standard behavior of any other renewal and you don't need to handle special logic for replacements when this event happens. When calling the [purchases.subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method with the new purchase token returns a purchase with **two line items**: - One representing the **old** entitlement, with an \`expiryTime\` in the past and no set value for [DeferredItemReplacement](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#DeferredItemReplacement). - One representing the **new** entitlement, with an \`expiryTime\` in the future and the auto_renewing_enabled flag turned on. |

ReplacementMode.DEFERRED should be used from now on instead of the deprecated
ProrationMode.DEFERRED, as it presents the same behavior regarding entitlement
changes, but offers a way to manage the purchase that is more consistent with
behaviors for other new purchases.

## Customer management

Using Real-time developer notifications, you can detect in real time when a
user decides to cancel. When a user cancels, but before their subscription has
expired, you can send them push notifications or in-app messages to ask them to
resubscribe.

After a user has cancelled their subscription, you can try to win them back
either in your app, or through the Play store. The following table describes
various subscription scenarios along with associated winback actions and app
requirements.

|---|---|---|---|---|
|   | **Before subscription expiration** || **After subscription expiration** ||
|   | **In-app** | **In Play Store** | **In-app** | **In Play Store** |
| **Winback feature** | In-app subscription | Restore | In-app subscription | Resubscribe |
| **User goes through checkout flow** | Yes | No | Yes | Yes |
| **User subscription remains associated with the same SKU** | User can sign up for same or different SKU | Yes | User can sign up for same or different SKU | Yes |
| **Creates new purchase token** | Yes | No | Yes | Yes |
| **Enabled by default** | No | Yes, support required for all devs | No | Apps without Billing Library 2.0+: No Apps with Billing Library 2.0+: Yes. Devs can opt-out in Console. |
| **When user is charged** | If using same SKU: end of current billing period. If using different SKU: depends on proration mode. | End of current billing period | Immediately | Immediately |
| **Implementation required** | Provide a re-signup UI in your app | Detect change in subscription state Deep-link to Play Store | Provide a re-signup UI in your app | Handle out-of-app purchases |

### Before subscription expiration - in-app

For subscriptions that have been canceled but have not yet expired, you can
allow subscribers to restore their subscription within your app by applying the
same in-app product purchase flow as for new subscribers. Ensure your UI
reflects that the user has an existing subscription. For example, you might want
to display the user's current expiration date and recurring price with a
**Reactivate** button.

Most of the time, you will want to offer the user the same price and SKU they
were already subscribed to, as follows:

- Initiate a new subscription purchase with the same SKU.
- The new subscription replaces the old one and renews on the same expiration date. The old subscription is immediately marked as expired.
- As an example, Achilles has a subscription to Example Music App, and the subscription is due to expire on August 1. On July 10, he resubscribes to the one-month subscription at the same price per month. The new subscription is prorated with the remaining credit, is immediately active, and still renews on August 1.

If you would like to offer a different price---for example a new free trial or a
winback discount---you can instead offer a different SKU to the user:

- Initiate an [upgrade or downgrade](https://developer.android.com/google/play/billing/subscriptions#allow-users-change) with the different SKU using the replacement mode `WITHOUT_PRORATION`.
- The new subscription replaces the old one and renews on the same expiration date. The user is charged the price of the new SKU, including any introductory prices, on the original expiration date. If the old subscription was created using an obfuscated account ID, that same ID should be passed to the `BillingFlowParams` for upgrades and downgrades.
- As an example, Achilles has a subscription to Example Music App, and the subscription is due to expire on August 1. On July 10, he resubscribes to an annual subscription with an introductory price. The new subscription is immediately active, and the user is charged the introductory price on August 1.
- If you decide to include a free trial or intro price in your winback SKU, ensure that the user is eligible by unchecking the **Allow one free trial per app** box in the Google Play Console, which restricts the user to getting one free trial per app.

When you receive the purchase token, [process the
purchase](https://developer.android.com/google/play/billing/integrate#process) just as you would with a new
subscription. Additionally, the Google Play Developer API
returns a `linkedPurchaseToken` in the subscription resource. Be sure to
[invalidate the token](https://developer.android.com/google/play/billing/subs#upgrade-downgrade) provided in
the `linkedPurchaseToken` to ensure that the old token is not used to gain
access to your services.

### Before subscription expiration - in Play Store

| **Note:** Supporting restore is required for all developers.

While the subscription is canceled but still active, users can restore the
subscription in the Google Play subscriptions center by clicking
**Resubscribe** (previously **Restore**). This keeps the same subscription and
purchase token.
![subscriptions section in the google play store app showing a
cancelled subscription with a resubscribe button](https://developer.android.com/static/images/google/play/billing/resubscribe.jpg) **Figure 8.** *Account \> Subscriptions* section in the Google Play Store app showing a cancelled subscription with a **Resubscribe** button.

For more information on restoring subscriptions, see [Restorations](https://developer.android.com/google/play/billing/subscriptions#restore).

### After subscription expiration - in-app

You can allow expired subscribers to resubscribe within your app by applying the
same in-app product purchase flow as for new subscribers. Note the following:

- To offer users a discount, you might want to offer a product ID with special pricing for your subscription, also called a *winback SKU*. You can provide the offer in your app, or you can notify the user of the offer outside of the app, such as in email.
- To start a winback subscription, launch the purchase flow in your Android app using the Google Play Billing Library. This is the same process as with a new subscription, but you can determine the SKU that is available to the user.
- If you decide to include a free trial or intro price in your winback SKU, ensure that the user is eligible by unchecking the **Allow one free trial per app** box in the Google Play Console, which restricts the user to getting one free trial per app.
- If the user resubscribes to the same SKU, they are no longer eligible for free trials or introductory price. Ensure that your UI reflects this.

When you receive the purchase token, [process the
purchase](https://developer.android.com/google/play/billing/integrate#process) just as you would with a new
subscription. You won't receive a `linkedPurchaseToken` in the subscription
resource.

### After subscription expiration - in Play Store

| **Note:** Resubscribe from Play Store is only available to apps with Google Play Billing Library versions 2.0 and later.
| **Note:** All subscription SKUs for eligible apps have resubscribe enabled by default. You can opt out at any time by adjusting the SKU settings through the [Google Play Console](https://support.google.com/googleplay/android-developer/answer/140504).

If enabled, users can resubscribe to the same SKU for up to one year after
expiration by clicking **Resubscribe** in the Google Play subscriptions center.
This generates a new subscription and purchase token.
![subscriptions section in the google play store app showing a
cancelled and expired subscription with resubscribe and remove
buttons](https://developer.android.com/static/images/google/play/billing/resubscribe-remove.jpg) **Figure 9.** *Account \> Subscriptions* section in the Google Play Store app showing a cancelled and expired subscription with **Resubscribe** and **Remove** buttons.

Re-subscribing is considered an out-of-app purchase, so be sure to follow best
practices for [properly acknowledging them from your
backend](https://developer.android.com/google/play/billing/lifecycle/subscriptions#resubscribe_after_expiration).

## Promote your subscription

You can create promotion codes to give selected users an extended free trial to
an existing subscription. To learn more, see [Promo
codes](https://developer.android.com/google/play/billing/promo).

For free trials, Google Play verifies that the user has a valid payment method
before starting the free trial. Some users may see this verification as a hold
or charge on their payment method. This hold or charge is temporary and is later
reversed or refunded.

After the trial period ends, the user's payment method is charged for the full
subscription amount.

If a user cancels a subscription at any time during the free trial, the
subscription remains active until the end of the trial, and they aren't charged
when the free trial period ends.

## Cancel or revoke

You can use the
[Google Play Developer API](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions)
to
[cancel](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/cancel)
or
[revoke](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
a subscription. This functionality is also available in the [Google Play Console](https://support.google.com/googleplay/android-developer/answer/2741495).

- **Cancel** : Users can cancel a subscription on Google Play. You can also
  provide an option for users to cancel in your app or on your website. Your
  app should handle these cancellations as described in
  [Cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel).

- **Revoke** : When you revoke, the user immediately loses access to the
  subscription. This can be used if, for example, there was a technical error
  that prevented the user from accessing your product, and the user does not
  want to continue using the product. Your app should handle these
  cancellations as described in
  [Revocations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke).

The following table illustrates the differences between cancel and revoke.

|---|---|---|
|   | **Stops renewal** | **Revoke access** |
| **[Cancel](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/cancel)** | **Yes** | No |
| **[Revoke](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/revoke)** | **Yes** | **Yes** |

## Defer billing for a subscriber

You can extend the entitlement period for a subscription by
using the [`subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method. When you defer a subscription with add-ons, all items in the subscription are deferred by the same duration. During the deferral period, the user is subscribed to your content with full access but is not charged. The subscription renewal date is updated to reflect the new date.

For prepaid plans, you can use the defer billing API to defer the expiration time.

Deferred billing lets you do the following:

- Give users free access as a special offer, such as giving one week free for purchasing a movie.
- Give free access to customers as a gesture of goodwill.

Billing can be deferred by as little as one day and by as long as one year per
API call. To defer the billing even further, you can call the API again before
the new billing date arrives.

As an example, Darcy has a monthly subscription to online content for the
Fishing Quarterly app. She is normally billed £1.25 on the first of each month.
In March, she participated in an online survey for the app publisher. The
publisher rewards her with six free weeks by deferring the next payment until
May 15, which is six weeks after her previously scheduled billing date of April

1. Darcy is not charged for April or the beginning of May and still has access to the content. On May 15, she is charged the normal £1.25 subscription fee for the month. Her next renewal date is now June 15.

When deferring, you might want to notify the user by email or within the app to
notify them that their billing date has changed.

## Handling payment declines

If there are payment issues with a subscription renewal, Google will
periodically attempt to renew the subscription for some time before canceling.
This recovery period can consists of a grace period, followed by an account hold
period. During this time, Google sends the user emails and notifications
prompting them to update their payment method.

Upon payment decline, the subscription enters a [grace
period](https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period) if one is
configured. During the grace period, you should ensure the user still has access
to the subscription entitlements.

After any grace period has ended, the subscription enters an [account
hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold) period. During
account hold, you should ensure the user does not have access to the
subscription entitlements.

You can specify the length of each auto-renewing base plan's grace period and
account hold in the Google Play Console. Specifying lengths less than the
default values may reduce the number of subscriptions recovered from payment
declines.

To maximize the likelihood of subscription recovery during a payment decline,
you can inform your user of a payment issue and ask them to fix it.

You can either do this yourself, as described in the [grace
period](https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period) and [account
hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold) sections, or
you can implement the in-app messaging API, where Google shows a message to
users in your app.
| **Note:** You can use [Play Billing Lab Subscription State Transition](https://developer.android.com/google/play/billing/test#subscription-state-transition) feature to test payment decline scenarios.

### In-app messaging

If you've enabled in-app messaging with
[`InAppMessageCategoryId.TRANSACTIONAL`](https://developer.android.com/reference/com/android/billingclient/api/InAppMessageParams.InAppMessageCategoryId#TRANSACTIONAL),
Google Play will show users messaging during grace period and account hold once
per day and provide them an opportunity to fix their payment without leaving the
app.
![Snackbar notifying the user to fix their payment](https://developer.android.com/static/images/google/play/billing/subscriptions-in-app-messaging-snackbar.png) **Figure 20.** Snackbar notifying the user to fix their payment.

We recommend that you call this API whenever the user opens the app to determine
whether the message should be shown.

If the user successfully recovered their subscription, you will receive a
response code of
[`SUBSCRIPTION_STATUS_UPDATED`](https://developer.android.com/reference/com/android/billingclient/api/InAppMessageResult.InAppMessageResponseCode#SUBSCRIPTION_STATUS_UPDATED)
along with a purchase token. You should then use this purchase token to call the
Google Play Developer API and refresh the subscription status in your app.

#### Integrate in-app messaging

To show in-app messaging to user, use
[`BillingClient.showInAppMessages()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showInAppMessages).

Here is an example of triggering the in-app messaging flow:

### Kotlin

```kotlin
val inAppMessageParams = InAppMessageParams.newBuilder()
        .addInAppMessageCategoryToShow(InAppMessageCategoryId.TRANSACTIONAL)
        .build()

billingClient.showInAppMessages(activity,
        inAppMessageParams,
        object : InAppMessageResponseListener() {
            override fun onInAppMessageResponse(inAppMessageResult: InAppMessageResult) {
                if (inAppMessageResult.responseCode == InAppMessageResponseCode.NO_ACTION_NEEDED) {
                    // The flow has finished and there is no action needed from developers.
                } else if (inAppMessageResult.responseCode
                        == InAppMessageResponseCode.SUBSCRIPTION_STATUS_UPDATED) {
                    // The subscription status changed. For example, a subscription
                    // has been recovered from a suspend state. Developers should
                    // expect the purchase token to be returned with this response
                    // code and use the purchase token with the Google Play
                    // Developer API.
                }
            }
        })
```

### Java

```java
InAppMessageParams inAppMessageParams = InAppMessageParams.newBuilder()
        .addInAppMessageCategoryToShow(InAppMessageCategoryId.TRANSACTIONAL)
        .build();

billingClient.showInAppMessages(activity,
        inAppMessageParams,
        new InAppMessageResponseListener() {
            @Override
            public void onInAppMessageResponse(InAppMessageResult inAppMessageResult) {
                if (inAppMessageResult.responseCode
                        == InAppMessageResponseCode.NO_ACTION_NEEDED) {
                    // The flow has finished and there is no action needed from developers.
                } else if (inAppMessageResult.responseCode
                        == InAppMessageResponseCode.SUBSCRIPTION_STATUS_UPDATED) {
                    // The subscription status changed. For example, a subscription
                    // has been recovered from a suspend state. Developers should
                    // expect the purchase token to be returned with this response
                    // code and use the purchase token with the Google Play
                    // Developer API.
                }
            }
        });
```

## Handle subscription pending transactions

| **Note:** Pending transactions are only available for purchasing prepaid plan with Google Play Billing Library versions 7.0 and higher. You need to support and enable pending transactions **explicitly**.

[Pending transactions](https://developer.android.com/google/play/billing/integrate#pending) can happen in initial purchase, top-up, upgrade or
downgrade. The subscription purchase starts with the
`SUBSCRIPTION_STATE_PENDING` state before transitioning to
`SUBSCRIPTION_STATE_ACTIVE`. If the transaction is expired or canceled by the
user, it goes to `SUBSCRIPTION_STATE_PENDING_PURCHASE_EXPIRED`. You must and
should only update the user's entitlement after the transaction is completed.

Subscription state change for initial purchase with pending transactions is
straightforward. Your app receives a `Purchase` with `PENDING` state when the
user initiates a pending transaction. When the transaction is completed, your
app receives the `Purchase` again with state updated to `PURCHASED`. A
`SubscriptionNotification` message with type `SUBSCRIPTION_PURCHASED` is sent to
your RTDN client. Follow the normal process to verify the purchase, give the
user access to the content and acknowledge the purchase. If the transaction
expires or is canceled, a `SubscriptionNotification` message with type
`SUBSCRIPTION_PENDING_PURCHASE_CANCELED` is sent to your RTDN client. In such
cases, the user should never have gained access to the content.

Top-up, upgrade or downgrade with pending transactions involves state changes
for both the old and new subscriptions. When the user initiates a pending
top-up, upgrade or downgrade transaction, your app receives a `Purchase` for the
old subscription with a `PendingPurchaseUpdate` object. At this time, the user
is still owning the old subscription and has not gained the new subscription
yet. Calling `getProducts()` and `getPurchaseToken()` on the
`PendingPurchaseUpdate` object returns the product ids and purchase token of the
new subscription. When the transaction is completed, your app receives a
`Purchase` with the top-level purchase token set for the new subscription and
the state set to `PURCHASED`. A `SubscriptionNotification` message with type
`SUBSCRIPTION_PURCHASED` is sent to your RTDN client. Only at this time, you
should replace the old purchase token with the new purchase token and update the
user's access to the content. If the transaction expires or is canceled, a
`SubscriptionNotification` message with type
`SUBSCRIPTION_PENDING_PURCHASE_CANCELED` is sent to your RTDN client. In such
cases, the user should still have access to the content of the old subscription.