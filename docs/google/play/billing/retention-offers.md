---
title: https://developer.android.com/google/play/billing/retention-offers
url: https://developer.android.com/google/play/billing/retention-offers
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/billing/llms.txt

Retention offers help you reduce voluntary churn by showing a discount to
subscribers at the moment they try to cancel their subscription in Google Play.

When an eligible subscriber starts to cancel, Google Play shows them a retention
offer that you configured, such as "Keep your subscription and get 50% off for
the next 2 months." If the subscriber accepts the offer, their subscription
isn't canceled. The discounted price starts on their next billing date.

This page explains how retention offers work, how to configure them, how to
handle the resulting events in your backend, and how to test them.

## Before you begin

Before you set up retention offers, make sure that you have done the following:

- Created a subscription with at least one [auto-renewing base plan](https://support.google.com/googleplay/android-developer/answer/140504). Retention offers can only be added to auto-renewing base plans.
- [Configured Real-time developer notifications](https://developer.android.com/google/play/billing/getting-ready.md.txt#configure-rtdn) (RTDN) and set up your backend to call the [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method. Your backend uses these to detect when a subscriber accepts a retention offer.

Because Google Play shows retention offers outside your app, you don't need to
change your app or update your Google Play Billing Library integration to
use them. All of the integration work happens in Google Play Console and
your backend.

## How retention offers work

Retention offers appear only in Google Play subscription management: the Google
Play Store app and Google Play on the web. They don't appear inside your app.
The Google Play Billing Library doesn't return retention offers in
`queryProductDetailsAsync()` results, so they aren't included in
`ProductDetails.getSubscriptionOfferDetails()`, and you can't sell them through
`launchBillingFlow()`. If your app uses [deep links](https://developer.android.com/google/play/billing/subscriptions.md.txt#use-deep) to send subscribers to
the Google Play subscriptions center or to a specific subscription so that they
can manage or cancel it, those subscribers can see your retention offer when
they start to cancel there.

The following steps describe what happens when a subscriber tries to cancel:

1. The subscriber opens their subscription in Google Play and starts to cancel it.
2. Google Play checks whether the subscriber is eligible for one of your
   retention offers, based on the
   [eligibility rules](https://developer.android.com/google/play/billing/retention-offers.md.txt#retention-targeting-rule) that you set for the offer,
   or on whether you [targeted the offer to that subscriber](https://developer.android.com/google/play/billing/retention-offers.md.txt#per-user-targeting).

3. If the subscriber is eligible, Google Play may show the retention offer as
   an alternative to canceling. Meeting your eligibility criteria doesn't
   guarantee that the offer appears, because Google Play also performs
   additional platform-level checks, such as regional compliance requirements.
   If Google Play shows the offer, the subscriber can do one of the following:

   - **Accept the offer**: The subscriber accepts with a single tap. The subscription stays active and auto-renewing. The subscriber isn't charged right away; the discounted price applies starting with the next billing period.
   - **Continue canceling** : The subscriber declines the offer and completes the standard cancellation flow. You receive the usual `SUBSCRIPTION_CANCELED` notification. For details, see [Cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#cancel).

If the subscriber leaves the cancellation flow without accepting the offer or
canceling, their subscription doesn't change. This applies to both the Google
Play Store app and Google Play on the web. Viewing a retention offer without
accepting it doesn't count toward the offer's claim limit or start the wait
period between offers. Google Play checks the claim limit when it shows the
offer and again when the subscriber accepts it. An accepted offer counts toward
the claim limit when the subscription renews at the discounted price. The wait
period between offers starts when the discount period of the previous retention
offer on the same base plan ends. The subscriber might see the offer again the
next time they try to cancel, provided they're still eligible.

### Scheduled plan transition

When a subscriber accepts a retention offer, Google Play models it as a
*scheduled plan transition* on the subscriber's existing purchase. This differs
from a [deferred replacement](https://developer.android.com/google/play/billing/subscriptions.md.txt#handle-deferred-replacement), which requires a new purchase flow and creates
a new purchase token. With a retention offer, the subscriber keeps the same
`purchaseToken`, and only the future billing terms change.

When the subscriber accepts the offer, Google Play does the following:

- Sends a `SUBSCRIPTION_PLAN_TRANSITION_UPDATED` (`21`) RTDN to your backend.
- Adds a `planTransitionDetails` object to the `autoRenewingPlan` field of the affected line item in the [`SubscriptionPurchaseV2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) resource.

For details on handling these events, see [Handle retention offer events in your
backend](https://developer.android.com/google/play/billing/retention-offers#backend).

### Eligibility requirements

A subscription can receive a retention offer at any time before its next
renewal, as long as all of the following are true:

- The subscription is active and auto-renewing. Subscriptions in a [grace
  period](https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period), on [account hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#account-hold), or [paused](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#pause) can't receive retention offers.
- The subscription is a single subscription. Retention offers aren't supported for [subscriptions with add-ons](https://developer.android.com/google/play/billing/subscription-with-addons.md.txt).
- The subscription doesn't use an installment base plan. Installment base plans aren't eligible for retention offers.
- The next payment is at the regular recurring base plan price. If the subscriber is in a free trial or introductory price phase, the offer is available only during the final billing period of that phase, when the upcoming renewal is at the regular price.
- The subscriber isn't in a discounted billing period of a previously accepted retention offer. A subscriber who is in the discounted phase of a retention offer can't claim another retention offer until the subscription renews at the regular base plan price.
- The subscription has no pending scheduled plan transition. A subscription can have at most one pending scheduled plan transition, which is a `planTransitionDetails` object in the `IN_PROGRESS` state. For example, a subscriber who already accepted a retention offer that hasn't taken effect yet can't receive another one.
- The subscription has no unconfirmed price change.
- The retention offer's discounted price is less than or equal to the subscriber's next base plan renewal price.
- The subscriber meets the eligibility rules that you configured for the offer. For a per-user retention offer, you activated targeting for the subscription with the `activateOfferTargeting` method.

## Configure retention offers

You can create retention offers in Google Play Console or by using the
Google Play Developer API. Each retention offer uses one of the following
targeting modes:

- **Rule-based targeting** : Google Play decides which subscribers are eligible, based on [eligibility rules](https://developer.android.com/google/play/billing/retention-offers.md.txt#retention-targeting-rule) that you set, such as a minimum paid subscription duration.
- **Per-user targeting** : Your backend decides which subscribers can see the offer by [targeting it to specific subscriptions](https://developer.android.com/google/play/billing/retention-offers.md.txt#per-user-targeting).

A base plan can have more than one active retention offer in the same country or
region. When a subscriber is eligible for more than one offer, Google Play shows
at most one retention offer in the cancellation flow. Google Play chooses the
offer in the following order:

1. **Targeting mode** : A per-user targeted offer (`retentionPerUserRule`) always takes precedence over a rule-based offer (`retentionRule`), even if the rule-based offer has a higher discount percentage.
2. **Discount percentage**: Among eligible offers that use the same targeting mode, Google Play shows the offer with the highest displayed discount percentage.
3. **Discounted price**: If offers have the same discount percentage, Google Play shows the offer with the lowest discounted price.
4. **Offer ID** : If offers are still tied, Google Play shows the offer whose `offerId` comes last in alphabetical order.

### Create a retention offer in Play Console

To create a retention offer in Google Play Console, do the following:

1. Go to **Monetize with Play \> Products \> Subscriptions**.
2. Select a subscription, and then select the base plan that you want to add the offer to.
3. Add an offer for **Existing subscribers trying to cancel**.
4. Choose either **Cohort-level retention offer** or **User-level retention
   offer**.

### Create a retention offer with the Play Developer API

You can also create and update retention offers programmatically. To create an
offer, call the [`monetization.subscriptions.basePlans.offers.create`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/create)
method. To update existing offers, call the
[`monetization.subscriptions.basePlans.offers.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/patch) or
[`monetization.subscriptions.basePlans.offers.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/batchUpdate) method. All
three methods support the `retentionRule`, `retentionPerUserRule`, `startTime`,
and `endTime` fields. In the [`SubscriptionOffer`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers#SubscriptionOffer) object, set the following
fields:

- `offerId`: Your unique retention offer ID.
- `targeting`: Set `retentionRule` to a `RetentionTargetingRule` object that defines who is eligible for the offer. For the available fields, see [Set
  retention eligibility rules](https://developer.android.com/google/play/billing/retention-offers#retention-targeting-rule). To choose eligible subscribers from your backend instead, set `retentionPerUserRule`. For details, see [Target retention offers to specific
  subscribers](https://developer.android.com/google/play/billing/retention-offers#per-user-targeting).
- `phases[]`: A retention offer supports only a single pricing phase. In that phase, set the following fields:
  - `recurrenceCount`: The number of billing periods that the discount lasts, from 1 to 52. If `recurrenceCount` is greater than 1, the phase `duration` must equal the billing period of the base plan.
  - `regionalConfigs[]`: Set `relativeDiscount` to the discount as a fraction greater than 0 and less than 1. For example, use `0.5` for 50% off. Retention offers support only `relativeDiscount`. Fixed-price (`price`), absolute discount (`absoluteDiscount`), and free (`free`) phases aren't supported.
- `startTime`: Optional. The time when the retention offer becomes available to eligible subscribers, as an RFC 3339 timestamp. Setting this field doesn't activate the offer. If you don't set this field, the offer becomes available based on its state.
- `endTime`: Optional. The time when the retention offer stops being available, as an RFC 3339 timestamp, regardless of the offer's state. If you don't set this field, the offer has no end date. If you set this field, it must be in the future and later than `startTime`.

The `monetization.subscriptions.basePlans.offers.create` method always creates
the offer in the `DRAFT` state, even if you set `startTime`. To make the offer
active, call the [`monetization.subscriptions.basePlans.offers.activate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/activate)
method.

#### Set retention eligibility rules

The `RetentionTargetingRule` object contains the following fields:

- `scope`: Required. The subscriptions that the rule considers. For retention offers, the only supported value is `thisSubscription`, the subscription in which the offer is defined. Set this field to `{"thisSubscription": {}}`.
- `minDuration`: Required. The minimum time that a user must have been a paid subscriber to be eligible, as an ISO 8601 duration in days, from `P0D` to `P1826D`. For example, use `P90D` for 90 days. To not require a minimum paid subscription time, set this field to `P0D`.
- `allowMultipleClaims`: Optional. Whether a subscriber can claim the offer more than once. If `false`, a subscriber who has ever claimed this offer is never eligible for it again. If `true`, a subscriber can become eligible again after the time in `minOfferCooldownDuration` has passed since the end of the previous retention offer's discount period. Defaults to `false`.
- `minOfferCooldownDuration`: Required if `allowMultipleClaims` is `true`. The minimum time that must pass after the previous retention offer's discount period ends before the subscriber is eligible again, as an ISO 8601 duration in days, from `P1D` to `P1826D`. For example, use `P180D` for 180 days. Don't set this field if `allowMultipleClaims` is `false` or not set.

> [!NOTE]
> **Note:** Both `minDuration` and `minOfferCooldownDuration` accept only durations in days, in the format `P<n>D`. Other time units, such as months (`P3M`), fail validation.

The following example shows the `startTime`, `endTime`, and `targeting` fields
of a `SubscriptionOffer` object for a retention offer that's available to
subscribers who have paid for at least 90 days, and that they can claim again
180 days after their previous retention discount ends:

```json
{
  "offerId": "retention-50off-2m",
  "startTime": "2026-12-01T00:00:00Z",
  "endTime": "2027-03-01T00:00:00Z",
  "targeting": {
    "retentionRule": {
      "scope": {
        "thisSubscription": {}
      },
      "minDuration": "P90D",
      "allowMultipleClaims": true,
      "minOfferCooldownDuration": "P180D"
    }
  }
}
```

### Target retention offers to specific subscribers

Instead of letting Google Play decide eligibility with a
`RetentionTargetingRule`, you can make a retention offer available only to the
subscribers that your backend chooses. For example, you might target an offer to
subscribers that your churn-prediction model flags as at risk, or to subscribers
who start a cancellation journey in your app.

Subscribers see a per-user retention offer in the same Google Play cancellation
flow as any other retention offer, and you handle acceptance the same way. For
details, see [Handle retention offer events in your backend](https://developer.android.com/google/play/billing/retention-offers.md.txt#backend).

To target retention offers to specific subscribers, do the following:

1. **Create a per-user retention offer.** When you call the
   [`monetization.subscriptions.basePlans.offers.create`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/create),
   [`monetization.subscriptions.basePlans.offers.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/patch), or
   [`monetization.subscriptions.basePlans.offers.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/batchUpdate) method, set
   `targeting` to a `retentionPerUserRule` object instead of a `retentionRule`
   object. The `RetentionPerUserTargetingRule` object has no fields. An offer
   can use either `retentionRule` or `retentionPerUserRule`, but not both.

   ```json
   {
     "offerId": "retention-peruser-30off",
     "targeting": {
       "retentionPerUserRule": {}
     }
   }
   ```

   Activate the offer before you target it to subscribers. If you call the
   `activateOfferTargeting` method for an offer that has never been activated,
   the call fails with an HTTP `400 Bad Request` status code and an
   `INVALID_ARGUMENT` error status. For details, see
   [Handle targeting errors](https://developer.android.com/google/play/billing/retention-offers.md.txt#per-user-targeting-errors). Even when the offer is active, Google Play
   shows it only to subscribers whose subscriptions you target in the next
   step.

   > [!NOTE]
   > **Note:** If you deactivate a per-user retention offer after you activate it, calls to the `activateOfferTargeting` method still succeed and add the offer to `developerTargetedOffers` for the subscription. However, Google Play shows the offer in the cancellation flow only while the offer is active in Play Console and the current time is between its `startTime` and `endTime`.

2. **Target the offer to a subscription.** Call the
   [`purchases.subscriptionsv2.activateOfferTargeting`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/activateoffertargeting) method with your
   app's package name, the subscription's `purchaseToken`, and the `offerId`
   of the per-user retention offer:

       POST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/purchases/subscriptionsv2/tokens/{purchaseToken}:activateOfferTargeting

       {
         "offerId": "retention-peruser-30off"
       }

   A successful call returns an HTTP `204 No Content` status code with no
   response body. Google Play stores the targeting with the subscription, so
   you don't need to call the API at the moment the subscriber cancels. The
   next time the subscriber starts to cancel in Google Play, Google Play can
   show the offer, as long as the subscription meets the
   [eligibility requirements](https://developer.android.com/google/play/billing/retention-offers.md.txt#requirements). Per-user targeting replaces only the
   eligibility rules that a `retentionRule` defines. All other eligibility
   requirements, and the platform-level checks that Google Play performs, such
   as regional compliance requirements, still apply.

   You can target more than one per-user retention offer to the same
   subscription. To do so, call the `activateOfferTargeting` method once for
   each offer. Google Play still shows at most one retention offer in the
   cancellation flow. For details about how Google Play chooses the offer, see
   [Configure retention offers](https://developer.android.com/google/play/billing/retention-offers.md.txt#configure).

   The `activateOfferTargeting` method is idempotent. If you call it for an
   offer that's already targeted to the subscription, the call succeeds and
   Google Play updates the offer's `activateTime` to the time of the latest
   request.
3. **Remove the targeting when needed.** If you no longer want a subscriber to
   receive the offer, for example because their churn risk changed, call the
   [`purchases.subscriptionsv2.deactivateOfferTargeting`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/deactivateoffertargeting) method with the
   same package name, `purchaseToken`, and `offerId`. A successful call
   returns an HTTP `204 No Content` status code with no response body.

   The `deactivateOfferTargeting` method is also idempotent. If the offer
   isn't targeted to the subscription, for example because you never activated
   the targeting, the call succeeds and has no effect.

Targeting applies to a single `purchaseToken` and doesn't expire while the
subscription is active and auto-renewing. It stays in place after the subscriber
sees, accepts, or declines the offer. Google Play removes it only when you call
the `deactivateOfferTargeting` method, or 60 days after the subscription
expires. If a plan change or resubscription creates a new `purchaseToken`, the
targeting doesn't carry over.

To check which per-user retention offers are targeted to a subscription, call
the [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method. The `developerTargetedOffers`
field of each line item lists the targeted offers. Each entry contains the
`offerId` and the `activateTime` when you activated the targeting:

```json
{
  "lineItems": [
    {
      "productId": "premium_monthly_sub",
      "developerTargetedOffers": [
        {
          "offerId": "retention-peruser-30off",
          "activateTime": "2026-12-03T15:04:05Z"
        }
      ]
    }
  ]
}
```

#### Handle targeting errors

When a call to the `activateOfferTargeting` or `deactivateOfferTargeting`
method fails, the response contains an HTTP status code and an error status
that describes the cause. The following table lists the HTTP status codes and
error statuses that these methods can return:

| HTTP status code | Error status | Methods | Cause |
|---|---|---|---|
| `404 Not Found` | `NOT_FOUND` | Both | The `purchaseToken` doesn't exist. |
| `400 Bad Request` | `INVALID_ARGUMENT` | `activateOfferTargeting` | The `offerId` doesn't exist on the subscription's current base plan, or the offer is still in the draft state and has never been activated. |
| `400 Bad Request` | `FAILED_PRECONDITION` | `activateOfferTargeting` | The offer's `targeting` isn't set to `retentionPerUserRule`. |
| `400 Bad Request` | `FAILED_PRECONDITION` | `activateOfferTargeting` | The subscription has already expired. |

The `activateOfferTargeting` method doesn't check whether a non-expired
subscription is eligible for the offer. For example, if the subscription is
canceled but hasn't expired yet, the call succeeds and Google Play stores the
targeting. Google Play
evaluates the subscription's eligibility when the subscriber enters the
cancellation flow.

## Handle retention offer events in your backend

When a subscriber accepts a retention offer, and later when the discounted
renewal happens, Google Play sends RTDNs to your backend. After you receive each
notification, call the [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) method with the
`purchaseToken` from the notification to get the latest subscription state.

Accepting a retention offer doesn't create a new purchase. The `purchaseToken`
stays the same, so you don't need to acknowledge the purchase again, and Google
Play doesn't generate a `linkedPurchaseToken`. Keep the subscriber's existing
entitlement in place. Process the discounted renewal order the same way as any
other subscription renewal.

| Notification type | When it's sent | What to do |
|---|---|---|
| `SUBSCRIPTION_PLAN_TRANSITION_UPDATED` (`21`) | When a subscriber accepts a retention offer in the cancellation flow. | Call the `purchases.subscriptionsv2.get` method and check `planTransitionDetails`. The `transitionState` is `IN_PROGRESS`. The subscription remains active and auto-renewing, so continue to grant access. |
| `SUBSCRIPTION_RENEWED` (`2`) | When the current billing period ends and the subscription renews at the discounted retention offer price. | Call the `purchases.subscriptionsv2.get` method, confirm that `offerDetails.offerId` is the retention offer ID and that `planTransitionDetails` is no longer present, and extend the subscriber's access to the new `expiryTime`. |

The `planTransitionDetails` object contains the following fields:

- `productId`: The product ID of the plan that the subscription transitions to. For a retention offer, this is the same product.
- `basePlanId`: The base plan ID of the plan that the subscription transitions to.
- `offerId`: The ID of the retention offer that the subscriber accepted. Use this field to identify which retention offer was redeemed.
- `transitionInfo.transitionState`: The state of the transition. For retention offers, the state is `IN_PROGRESS` while the transition is pending.
- `transitionInfo.expectedTransitionTime`: When the retention offer terms are expected to take effect.

Google Play includes `planTransitionDetails` only while the transition is
pending. When the subscription renews at the discounted retention offer price,
the transition completes and Google Play removes `planTransitionDetails` from
the `purchases.subscriptionsv2.get` response. From then on, the line item
itself shows the active retention discount:

- `offerDetails.offerId` is the ID of the accepted retention offer.
- `offerPhase` is `{"introductoryPrice": {}}` during the discounted billing periods. After the discounted billing periods end and the subscription renews at the regular base plan price, `offerPhase` changes to `{"basePrice": {}}`.

### Response after the subscriber accepts the offer

After the subscriber accepts the retention offer, the current billing period
continues unchanged. The `planTransitionDetails` object shows the scheduled
transition with a `transitionState` of `IN_PROGRESS`:

```json
{
  "lineItems": [
    {
      "productId": "premium_monthly_sub",
      "expiryTime": "2026-12-15T10:00:00Z",
      "offerDetails": {
        "basePlanId": "monthly-base"
      },
      "autoRenewingPlan": {
        "autoRenewEnabled": true,
        "planTransitionDetails": {
          "productId": "premium_monthly_sub",
          "basePlanId": "monthly-base",
          "offerId": "retention-50off-2m",
          "transitionInfo": {
            "transitionState": "IN_PROGRESS",
            "expectedTransitionTime": "2026-12-15T10:00:00Z"
          }
        }
      }
    }
  ]
}
```

### Response after the discounted renewal

After the renewal date passes and the subscriber is charged the discounted
price, `offerDetails.offerId` shows the retention offer, `offerPhase` shows
`introductoryPrice`, and the response no longer includes
`planTransitionDetails`:

```json
{
  "lineItems": [
    {
      "productId": "premium_monthly_sub",
      "expiryTime": "2027-01-15T10:00:00Z",
      "offerDetails": {
        "basePlanId": "monthly-base",
        "offerId": "retention-50off-2m"
      },
      "offerPhase": {
        "introductoryPrice": {}
      },
      "autoRenewingPlan": {
        "autoRenewEnabled": true,
        "recurringPrice": {
          "currencyCode": "USD",
          "units": "9",
          "nanos": 990000000
        }
      }
    }
  ]
}
```

> [!NOTE]
> **Note:** `recurringPrice` shows the base plan's recurring price and doesn't reflect the retention offer discount. To get the amount the subscriber paid, call the [Orders API](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/get) with the line item's `latestSuccessfulOrderId`.

### Lifecycle interactions

Keep the following behaviors in mind when you handle retention offers:

- **End of the discount** : After the discounted billing periods end, the subscription automatically renews at the regular base plan price. You receive a `SUBSCRIPTION_RENEWED` notification, as with any other renewal, and the line item's `offerPhase` changes to `{"basePrice": {}}`. The subscriber doesn't need to take any action.
- **Payment recovery after the discount** : If the renewal at the regular base plan price after the discount ends is declined and the subscription enters a [grace period](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#grace-period) or [account hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions.md.txt#account-hold), payment recovery charges the regular base plan price. Google Play doesn't apply the completed retention offer discount. If the payment for the first discounted renewal is declined, the pending transition is preserved, and the retention offer price applies when the payment recovers.
- **Deferred billing** : If you call the [`purchases.subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method while a retention offer transition is `IN_PROGRESS`, the pending transition is preserved and applies at the deferred renewal. To get the new renewal date, check the line item's `expiryTime`.
- **Plan change before the transition** : A retention offer applies only to the `purchaseToken` of the subscription where the subscriber accepted it. If the subscriber switches to a different base plan or subscription before the `expectedTransitionTime`, Google Play generates a new purchase token, cancels the scheduled transition, and clears `planTransitionDetails`. The pending retention offer doesn't apply to the new plan.
- **Cancellation and restore** : If a subscriber cancels the subscription after accepting a retention offer, the scheduled transition remains pending and `transitionState` stays `IN_PROGRESS`. If the subscriber restores the subscription before it expires, the retention offer discount still applies at renewal.
- **Expiration and resubscription**: If the subscription expires without being restored, Google Play cancels the pending transition. If the user resubscribes or signs up again later, Google Play creates a new subscription purchase, and the previously accepted retention offer doesn't apply.
- **Offer changes**: If you change the discount or billing periods of a retention offer, the change applies only to future redemptions. Subscribers who already accepted the offer keep the original terms.
- **Offer deactivation** : If you deactivate a retention offer, or the offer reaches its end date, subscribers who already accepted it keep the terms they agreed to. Subscribers with an `IN_PROGRESS` transition still receive the discount at their next renewal, and subscribers who are already in the discounted billing periods keep the discount for the full agreed duration.
- **Price changes** : Base plan price changes still apply. Google Play migrates a subscriber to a new price only when the subscriber is paying the regular price and has no pending retention offer transition. For more information, see [Change subscription prices](https://developer.android.com/google/play/billing/price-changes.md.txt).
- **Refunds** : You can refund a subscriber with the standard refund and revoke APIs, such as the [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) method. This refunds the most recent payment and ends the subscriber's access.

## Test retention offers

Google Play shows only active retention offers in the cancellation flow, and it
evaluates eligibility rules in real calendar time. To test retention offers with
a [license tester](https://developer.android.com/google/play/billing/test.md.txt#license-testers) account, use one of the following methods:

> [!NOTE]
> **Note:** For license testers, the discounted renewals and the retention offer's discount periods follow the accelerated [test renewal periods](https://developer.android.com/google/play/billing/test.md.txt#renewals). For example, a monthly test subscription renews every 5 minutes, so a retention offer with 3 monthly discount periods ends after about 15 minutes.

- [Test a per-user retention offer](https://developer.android.com/google/play/billing/retention-offers.md.txt#test-per-user) on a production base plan, without showing the offer to real subscribers.
- [Test a rule-based retention offer](https://developer.android.com/google/play/billing/retention-offers.md.txt#test-rule-based) in a test app or on a test base plan that production users can't access.

Before you use either method, go to **Settings \> License testing** in
Google Play Console and add the test Google Account as a license tester.

### Test a per-user retention offer

Google Play shows a per-user retention offer only to the subscriptions that you
target, so you can test it on a production base plan without exposing it to
real subscribers. To test a per-user retention offer, do the following:

1. Create a per-user retention offer under the base plan, and then activate it. In Google Play Console, choose **User-level retention offer** . With the Google Play Developer API, set `targeting` to a `retentionPerUserRule` object. For details, see [Target retention offers to
   specific subscribers](https://developer.android.com/google/play/billing/retention-offers#per-user-targeting).
2. If you just activated the offer, wait 10 to 15 minutes for the change to propagate, and then clear the Google Play Store app cache.
3. On the test device, sign in with the license tester account, and then purchase the base plan in your app.
4. From your backend, call the [`purchases.subscriptionsv2.activateOfferTargeting`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/activateoffertargeting) method with your app's package name, the license tester's `purchaseToken`, and the `offerId` of the retention offer.
5. In the Google Play Store app, go to **Payments \& subscriptions \>
   Subscriptions** , select the subscription, and tap **Cancel subscription**. The retention offer appears in the cancellation flow.
6. Accept the offer, and then confirm that your backend receives the `SUBSCRIPTION_PLAN_TRANSITION_UPDATED` RTDN and handles the discounted renewal.

### Test a rule-based retention offer

After you activate a rule-based retention offer, Google Play can show it to any
eligible subscriber on the base plan. To avoid exposing the offer to production
users, test it in a non-production test app or on a dedicated test base plan
that production users can't access. To test a rule-based retention offer, do the
following:

1. In your test app or on your test base plan, create a rule-based retention offer, and set `minDuration` to `P0D` (0 days). In Google Play Console, choose **Cohort-level retention offer** . With the Google Play Developer API, set `targeting` to a `retentionRule` object. For details, see [Set retention eligibility
   rules](https://developer.android.com/google/play/billing/retention-offers#retention-targeting-rule).
2. Activate the offer, wait 10 to 15 minutes for the change to propagate, and then clear the Google Play Store app cache.
3. On the test device, sign in with the license tester account, and then purchase the test base plan.
4. In the Google Play Store app, go to **Payments \& subscriptions \>
   Subscriptions** , select the subscription, and tap **Cancel subscription**. Because the offer doesn't require a minimum paid subscription duration, you can start the cancellation flow right after the purchase. The retention offer appears in the cancellation flow.
5. Accept the offer, and then confirm that your backend receives the `SUBSCRIPTION_PLAN_TRANSITION_UPDATED` RTDN and handles the discounted renewal.

After you verify the integration, create and activate the rule-based retention
offer on your production base plan.

### Troubleshoot retention offer testing

If the retention offer doesn't appear, check the following:

- The retention offer is active, and the current time is between its `startTime` and `endTime`, if you set them.
- For a per-user retention offer, the `developerTargetedOffers` field in the [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) response for the license tester's `purchaseToken` includes the offer.
- The subscription is a single subscription, not a subscription with add-ons.
- The subscription isn't in a grace period, on account hold, or paused.
- The subscription has no pending plan change or price change.
- The next renewal is at the regular base plan price. For free trials and introductory offers, the retention offer is available only during the final billing period of the trial or introductory phase.
- You waited 10 to 15 minutes after you activated or changed the offer, and you cleared the Play Store app cache.