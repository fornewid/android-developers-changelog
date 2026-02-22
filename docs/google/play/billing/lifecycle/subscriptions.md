---
title: https://developer.android.com/google/play/billing/lifecycle/subscriptions
url: https://developer.android.com/google/play/billing/lifecycle/subscriptions
source: md.txt
---

Subscription purchases can go through several different states throughout their
lifecycle, depending on many factors including auto-renewal behavior, payment
decline situations, and developer management actions.

## Handle lifecycle for auto-renewing subscriptions

When a user's subscription state changes, your backend server receives a
[`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) message.
![subs-auto-renew-state](https://developer.android.com/static/images/google/play/billing/lifecycle/auto-renew-state-flow.svg) **Figure 1.** Lifecycle states and transition events for auto-renewing subscription purchases.

To update the state in your backend, call the
[`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)
API with the purchase token included in the notification. This endpoint provides
the latest subscription state given a purchase token and is considered the
source of truth for subscription management.

The purchase token is valid from subscription signup until 60 days after
expiration. After this date, the purchase token is no longer valid to use to
call the Google Play Developer API.
| **Note:** The [`purchases.subscriptions.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get) method is deprecated and present for backward compatibility reasons. This method shouldn't be used to obtain subscription states for new integrations. If you have an existing integration that uses this method, see [API deprecations](https://developer.android.com/google/play/billing/play-developer-apis-deprecations) for alternatives. Other methods in the `purchases.subscriptions` endpoint are still in use.

### New auto-renewing subscription purchases

When a user purchases a subscription, a `SubscriptionNotification` message with
type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client. Whether you receive
this notification or you register a new purchase in-app through
[`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener)
or [manually fetching purchases](https://developer.android.com/google/play/billing/integrate#fetch) in your
app's `onResume()` method, you should process the new purchase in your secure
backend. To do this, follow these steps:

1. Query the [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) endpoint to get a [subscription
   resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) that contains the latest subscription state.
2. Make sure that the value of the [`subscriptionState`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionstate) field is `SUBSCRIPTION_STATE_ACTIVE`.
3. [Verify the purchase](https://developer.android.com/google/play/billing/security#verify).
4. Give the user access to the content. The user account associated with the purchase can be identified with the [`ExternalAccountIdentifiers`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#externalaccountidentifiers) object from the subscription resource if identifiers were set at purchase time using [`setObfuscatedAccountId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)) and [`setObfuscatedProfileId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedProfileId(java.lang.String)).

The `offerPhase` field in the `SubscriptionPurchaseLineItem` provides details
about the current phase of the subscription, such as free trial or introductory
price.
| **Note:** If you don't acknowledge a new subscription purchase within three days, the user automatically receives a refund, and Google Play revokes the purchase.

The Play Billing Library also includes a method to acknowledge a subscription,
[`acknowledgePurchase()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgepurchase),
and a method to check acknowledgement status,
[`isAcknowledged()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#isacknowledged).
However, we recommend that you handle purchase processing in your backend for
better security.

The subscription resource for new purchases looks similar to the following
example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      "startTime": "2022-04-22T18:39:58.270Z",
      "regionCode": "US",
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      "latestOrderId": "GPA.3333-4137-0319-36762",
      "acknowledgementState": "ACKNOWLEDGEMENT_STATE_PENDING", // need to acknowledge new purchases
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": next_renewal_date,
          "autoRenewingPlan": {
            "autoRenewEnabled": true
          },
          "offerPhase": {
            "freeTrial": {}
          }
        }
      ],
    }

### Subscription renewals

For non-installment, auto-renewing subscriptions, a `SUBSCRIPTION_RENEWED`
notification is sent when the subscription renews. For installment
subscriptions, a `SUBSCRIPTION_RENEWED` notification is sent each time the
subscription is charged on its billing date. Make sure that the user is still
entitled to the subscription and then update the subscription state with the new
`expiryTime` provided in the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) returned from the Google Play
Developer API. The subscription resource looks similar to the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      "startTime": "2022-04-22T18:39:58.270Z",
      "regionCode": "US",
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      "latestOrderId": "GPA.3333-4137-0319-36762",
      "acknowledgementState": "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED",
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": next_renewal_date,
          "autoRenewingPlan": {
            "autoRenewEnabled": true
          },
          "offerPhase": {
            "basePrice": {}
          }
        }
      ]
    }

You don't need to acknowledge subscription renewals.
| **Note:** If a subscription is set to renew on the 29th, 30th, or 31st of the month going into February of a non-leap year, then the subscription renewal day is moved to the 28th of February and continues to renew on the 28th of each month for the duration of the subscription. Similarly, if a user starts a subscription on March 31st, the subscription renews on April 30th and continues to renew on the 30th of each month.

### Grace period

| **Note:** By default, all auto-renewing base plans have grace period enabled. You can adjust the grace period length or disable it from the [Google Play
| Console](https://support.google.com/googleplay/android-developer/answer/140504). Specifying a length less than the default value may reduce the number of subscriptions recovered from payment declines.

If there are payment issues with a subscription renewal, Google notifies the
user and periodically attempts to renew the subscription for some time before
the subscription expires. This recovery period can consist of a grace period
followed by an account hold period. During a grace period, the user should
still have access to their subscription entitlement.

The
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))
method continues to return purchases that are in the grace period. If your app
relies solely on `queryPurchasesAsync` to check whether a user is entitled to a
subscription, then your app should automatically handle grace periods, because
these subscriptions are shown as active through the Play Billing Library.

Synchronizing subscription state with your backend lets you to be more aware
of payment declines and gives you more context as you try to reduce involuntary
churn. Listen for
[`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) messages
with type `SUBSCRIPTION_IN_GRACE_PERIOD` to be notified when the user enters a
grace period. While the user is in a grace period, the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
contains `autoRenewEnabled = true`. Google Play dynamically extends the
`expiryTime` value until the grace period has expired because entitlement
should last until the user cancels or the grace period has lasted for its
maximum length. The value of the `subscriptionState` field during this period is
`SUBSCRIPTION_STATE_IN_GRACE_PERIOD`. The subscription resource looks similar to
the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_IN_GRACE_PERIOD",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": timestamp_in_future,
          "autoRenewingPlan": {
            "autoRenewEnabled": true
          }
        }
      ],
    }

Play informs users that are in a grace period that their payment was declined
and prompts them to fix their payment method issues in the Play Store. When a
user enters a grace period, you should also encourage the user to fix their
payment method in case the failure was involuntary. A straightforward way to do
this is to use the [In-App Messaging
API](https://developer.android.com/google/play/billing/subscriptions#in-app-messaging). If you call this API
when the user opens your app, they are shown a Play message in a temporary
snackbar informing the user that their payment has been declined. This message
also includes a deep link for the user to fix their payment method on Google
Play.

As soon as the user fixes their payment method, the subscription renews with its
original renewal date, and you can handle the renewal as described in
[Renewals](https://developer.android.com/google/play/billing/lifecycle/subscriptions#renewal).

If the user does not fix their payment method during the grace period, the
subscription enters [account hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold), and they lose entitlement.

#### Grace period access and recovery

Figure 2 shows a timeline for a subscription that enters into a grace period and
then recovers when the user fixes their payment method. After the grace period
ends, the user should lose subscription benefits and go into account hold.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/grace-period.png) **Figure 2.** Timeline for a subscription that enters a grace period and recovers before it ends.

It is important to remember the following points:

- During a grace period, the user should retain access to subscription benefits.
- When a subscription recovers during a grace period, the renewal date does *not* reset.
- If you increase the grace period---for example, from 7 days to 14 days---users who are in a grace period get extended access to subscription benefits.
- If you decrease the grace period, users who are far enough into the old grace period to exceed the new grace period have their subscription benefits revoked immediately. For example, if you decrease the grace period from 14 days to 7 days, users who are in days 8-14 of the old grace period have their subscription benefits revoked immediately.
- The subscription remains in an active state and you won't receive a grace period RTDN until the silent grace period ends

### Silent grace period

You can set a grace period of 0 days, but Play will wait a minimum of 1 day to
ensure sufficient time for payment retries. This silent grace period offers a
safety net for payment processing. During this 24‑hour period the
subscription remains in the
[`ACTIVE` state](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#state).

The best way for you to stay in sync with subscription state changes is to
listen and react to the real-time developer notifications (RTDN). Call the
[`purchases.subscriptionsv2.get()`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)
method at the RTDN time instead of the expiry time to get a more accurate
status of the subscription.

Depending on the subscription status after the 24‑hour silent grace
period, you should receive one of the following notifications:

- `SUBSCRIPTION_ON_HOLD` (if enabled)
- `SUBSCRIPTION_CANCELED` (if canceled)
- `SUBSCRIPTION_EXPIRED` (if expired)
- `SUBSCRIPTION_RENEWED` (if successfully renewed)

You can also call the `subscriptionV2.get()` method at any point after the
24‑hour silent grace period to get the latest status of the subscription.

### Account hold

| **Note:** By default, all auto-renewing base plans and installment plans have account hold enabled and the lengths are automatically calculated. The calculation will be 60 days minus any grace period duration. You can adjust the account hold length or disable it from the [Google Play Console](https://support.google.com/googleplay/android-developer/answer/140504). Specifying a length less than the default value may reduce the number of subscriptions recovered from payment declines.

If there are payment issues with a subscription renewal, after any [grace
period](https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period) has ended, an account hold period begins. When a
subscription enters account hold, you should block access to the subscription
entitlement.

During account hold, you should continue to handle any [cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel),
restorations, or [repurchases of your subscriptions](https://developer.android.com/google/play/billing/lifecycle/subscriptions#resubscribe) as needed,
because it's possible for the user to make these changes while the subscription
is on hold.

RTDNs notify you when the user enters the account hold period, so you can inform
them as soon as possible of why their access to the subscription was suspended.
A straightforward way to do this is to use the [In-App Messaging
API](https://developer.android.com/google/play/billing/subscriptions#in-app-messaging). Calling this API when
your user opens the app will show the user a message in a temporary snackbar
informing them that their payment has been declined. This message also includes
a deep link for the user to fix their payment method on Google Play.

If your users can access subscription content outside of your app, they might
discover that they have lost access on different surfaces. You might want to
send a push notification or an email to the user to let them know that their
subscription is no longer active due to payment decline.

The subscription is not returned by the
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))
method during account hold, so if your app relies on this method to display
existing purchases, you should support account hold by default.

With [real-time developer
notifications](https://developer.android.com/google/play/billing/getting-ready#configure-rtdn), you receive a
[`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) message
with type `SUBSCRIPTION_ON_HOLD` when a subscription enters account hold. Call
the
[`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)
method from your secure backend server to retrieve the new subscription
information. During account hold the `expiryTime` field of the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
is set to a past timestamp, and the `subscriptionState` field is set to
`SUBSCRIPTION_STATE_ON_HOLD`:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ON_HOLD",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": timestamp_in_past,
          ...
        }
      ],
    }

To restore access, users must fix their payment method. Play informs users in
account hold of their payment decline, and you should also encourage them to fix
their payment method.

After the user fixes their payment method, the subscription returns to an active
state, and you must then restore access to the subscribed content. In this case,
the purchase token is the same as it was before the account hold started because
the same purchase is recovering, and you receive an RTDN with type
`SUBSCRIPTION_RECOVERED`.

For installment subscriptions, payment declines and recoveries could occur for
any individual payment attempt.
| **Note:** If a subscription is recovered from account hold, the billing date moves to the date of recovery.

After recovery, the Play Billing Library returns the subscription again through
the `queryPurchasesAsync()` method. If you use this method to determine whether
a user is entitled to a subscription, then your app should automatically handle
the subscription recovering from account hold.

Listen for a
[`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) message
with type `SUBSCRIPTION_RECOVERED` to be notified when a subscription is
recovered and the user should regain access. If you query for a subscription
after receiving this notification, the `expiryTime` field is set to a timestamp
in the future and the `subscriptionState` field is set to
`SUBSCRIPTION_STATE_ACTIVE` again:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": next_renewal_date,
          ...
        }
      ],
    }

If the user does not fix their payment method before the end of the account hold
period, you instead receive an RTDN with type `SUBSCRIPTION_CANCELED`. For
instructions on handling a cancellation, see [Cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel). When you
query for a subscription that was canceled in this way, the returned
`expiryTime` field is set to a past timestamp:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_CANCELED",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": timestamp_in_past,
          ...
        }
      ],
    }

Immediately after you are notified of the cancellation during account hold, you
will also receive an RTDN with type `SUBSCRIPTION_EXPIRED` because the user is
out of paid entitlement and the subscription has churned with the cancellation.
You can [handle this expiration](https://developer.android.com/google/play/billing/lifecycle/subscriptions#expiration) the way you normally would.

The user can regain access by repurchasing the same subscription plan or any
other plan that you offer through the app during their account hold period from
their original purchase. In that case, a new purchase token is issued and the
new value is returned as part of a `SUBSCRIPTION_PURCHASED` event that
represents this new instance.

#### Account hold access and recovery

Figure 3 shows a timeline for a subscription that enters into account hold and
then recovers when the user fixes their payment method.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/acct-hold-1.png) **Figure 3.** Timeline for a subscription that enters an account hold and recovers before it ends.

Similar to the previous example, Figure 4 shows a timeline for a subscription
that first enters into a grace period before entering account hold, and then
recovers while on hold.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/acct-hold-2.png) **Figure 4.** Timeline for a subscription that enters a grace period, then enters account hold, and finally recovers before the account hold ends.

It is important to remember the following points:

- Before a subscription enters into account hold, Google Play makes additional attempts to charge the payment method for up to 48 hours. The user retains subscription benefits during this period. After this retry period has elapsed, the subscription then enters into account hold, and the user should lose access to subscription benefits.
- The subscription enters into account hold directly when the subscription resumes from a paused state with a failed form of payment.
- When a subscription recovers from account hold, the renewal date resets.

### Expirations

Once a subscription expires, the user should lose access to the subscription. A
`SubscriptionNotification` message with type `SUBSCRIPTION_EXPIRED` is sent in
that case. When you receive this notification, query the Google Play Developer
API to get the latest [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2).
After you confirm that the `subscriptionState` is `SUBSCRIPTION_STATE_EXPIRED`,
remove the entitlement and register the purchase state as invalid in your
backend. The subscription resource looks similar to the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_EXPIRED",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": expiration_time_in_past,
          ...
        }
      ],
    }

### Cancellations

A user can voluntarily cancel a subscription from the Play subscriptions center
or have their subscription automatically canceled if they don't recover after
being in [account hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold). Developers can also trigger a
cancellation with
[`purchases.subscriptionsv2.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel)
When a subscription is canceled, the user retains access to the content until
the end of the current billing cycle. When the billing cycle ends, access should
be revoked.
| **Note:** For installment subscriptions, user-initiated cancellation takes effect at the end of the current commitment period. Developer-initiated cancellation, using the [`purchases.subscriptionsv2.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel) API, where the `cancellationType` request parameter is set to `USER_REQUESTED_STOP_RENEWAL`, takes effect at the end of the current commitment period. However, setting the `cancellationType` request parameter to `DEVELOPER_REQUESTED_STOP_PAYMENTS`, stops the next payment.

Canceling a non-installment, auto-renewing subscription triggers a
`SUBSCRIPTION_CANCELED` notification. When
you receive this notification, the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
returned from the Google Play Developer API has the `subscriptionState` field
set to `SUBSCRIPTION_STATE_CANCELED`, and the `expiryTime` field contains the
date when the user should lose access to the subscription. If that date is in
the past, then the user should lose entitlement immediately. This could happen,
for example, if a user cancels a subscription while on [account
hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold) due to a payment decline.

The subscription resource for a canceled purchase looks similar to the following
example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_CANCELED",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": expiration_time,
          ...
        }
      ],
    }

For installment subscriptions, a `SUBSCRIPTION_CANCELLATION_SCHEDULED`
notification gets sent upon a user-initiated cancellation when payments remain
for the commitment period. The cancellation is pending and takes effect at the
end of the current commitment period. When you receive this notification, the
subscription resource returned from the Google Play Developer API has the
subscriptionState field set to `SUBSCRIPTION_STATE_ACTIVE` because the
installment subscription is still active until the end of the commitment period.
However, there is an empty pendingCancellation object present.
A `SUBSCRIPTION_CANCELED` notification gets sent followed by a
`SUBSCRIPTION_EXPIRED` at the end of the commitment period.

The subscription resource for a installment subscription purchase that is
pending cancellation looks similar to the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      ...
      "lineItems": [
        {
          "productId": "sub_plan01",
          "expiryTime": expiration_time,
          "autoRenewingPlan": {
            "autoRenewEnabled": true,
            "recurringPrice": {
              "currencyCode": "USD",
              "units": "1",
              "nanos": 990000000
            },
            "installmentDetails": {
              "initialCommittedPaymentsCount": 6,
              "remainingCommittedPaymentsCount": 5,
              "pendingCancellation": {}
          ...
            }
          }
        }
      ],
    }

You can look at the `canceledStateContext` field in the subscription resource to
learn why the subscription was canceled (for example, whether the subscription
was canceled by the user, by the system, or by you). If the subscription was
canceled by the user, you can look at the `userInitiatedCancellation` field to
learn why the user canceled the subscription. This can help inform communication
strategies.

When a subscription is canceled but has not yet [expired](https://developer.android.com/google/play/billing/lifecycle/subscriptions#expiration), it is
still returned from
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)).
You might want to display a message in your app informing the user that their
subscription was canceled and giving them the date of expiration.
| **Warning:** Don't remove access to a subscription from Google Play while the user is still entitled to the content. Removing access to content that a user is entitled to is a violation of [Google Play's subscriptions
| policy](https://support.google.com/googleplay/android-developer/answer/9900533).

### Revocations

A subscription can be revoked for a variety of reasons, including your backend
revoking the subscription by using
[`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
or the purchase being charged back. In this situation, revoke the user's
entitlement immediately. A `SubscriptionNotification` message with type
`SUBSCRIPTION_REVOKED` is sent when this occurs. When you receive this
notification, the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
returned from the Google Play Developer API has the `subscriptionState` field
set to `SUBSCRIPTION_STATE_EXPIRED`.

The subscription resource for a revoked purchase looks similar to the following
example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_EXPIRED",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": expiration_time,
          ...
        }
      ]
    }

### Deferred subscriptions

There are a variety of reasons why you might want to extend a user's
entitlement. For example, you might want to offer users free access as a special
promotion, such as giving one week free for purchasing a movie or providing free
access to customers as a gesture of goodwill.

You can use the
[`purchases.subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) API to defer the billing date for subscriptions (including subscriptions with add-ons). When you defer a subscription with add-ons, all items in the subscription are deferred by the same duration.

When you defer a subscription, a `SubscriptionNotification`
message with type `SUBSCRIPTION_DEFERRED` is sent. During the deferral period,
the user is subscribed to your content with full access but is not charged. The
subscription renewal date is updated to reflect the new date.

For prepaid plans, you can use the defer billing API to defer the expiration
time.

The subscription resource for a deferred subscription looks similar to the
following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": timestamp_in_future,
          ...
        }
      ],
    }

### Paused subscriptions

| **Note:** All subscriptions have pause enabled by default. You can disable pause from the [Google Play
| Console](https://support.google.com/googleplay/android-developer/answer/140504#pause).

You can reduce voluntary churn by enabling users to pause their subscription.
When you enable the pause feature, users can choose to pause their subscription
for a period of time between one week and three months, depending on the
recurring period. This temporarily suspends the subscription.

| Subscription recurrence | Weekly | Monthly | Three-month | Six-month | Annual |
|---|---|---|---|---|---|
| Available pause lengths^\*^ | 1 week 2 weeks 3 weeks 4 weeks | 1 month 2 months 3 months | 1 month 2 months 3 months | 1 month 2 months 3 months | N/A |

^\*^Subject to change at any time.

A subscription pause takes effect only after the current billing period ends.
While the subscription is paused, the user doesn't have access to the
subscription, and they don't pay the renewal price. At the end of the pause
period, the subscription resumes and Google attempts to renew the subscription.
If the resume is successful, the subscription becomes active again. If the
resume fails due to a payment issue, the user enters the account hold state as
shown in figures 5 and 6:
![](https://developer.android.com/static/images/google/play/billing/lifecycle/pause-1.png) **Figure 5.** A user pauses and then resumes their subscription. ![](https://developer.android.com/static/images/google/play/billing/lifecycle/pause-2.png) **Figure 6.** A user pauses their subscription and then enters account hold.

A user can also choose to manually resume a subscription at any time during the
pause period, as shown in figure 6. When a user resumes manually, the billing
date changes to the manual resume date.

When a user's subscription is paused, the Play Billing Library doesn't return
the subscription through the [`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)) method unless the
`includeSuspendedSubscriptions` parameter is set to true in the
`QueryPurchasesParams`. If the subscription is resumed, the
`queryPurchasesAsync()` method returns it again.

Listen for RTDNs to be aware of when a user pauses their subscription. These
notifications also allow you to notify your users in your app that they have
paused their subscription and don't have access to it. You should also provide a
way for the user to manually resume their subscription at any time by using a
[deep link to Google Play](https://developer.android.com/google/play/billing/subscriptions#deep-link).

A [`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) message
with type `SUBSCRIPTION_PAUSE_SCHEDULE_CHANGED` is sent when your user initiates
a pause of their subscription. At this time, the user should keep access to
their subscription until the next renewal date, and the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)
contains `autoRenewEnabled = true`. The value of the `subscriptionState` field
is `SUBSCRIPTION_STATE_ACTIVE` at this point.

A `SubscriptionNotification` message with type `SUBSCRIPTION_PAUSED` is sent when the
pause goes into effect. When this happens, the user should lose access to their
subscription, and the subscription resource contains `autoRenewEnabled = true`,
and the `subscriptionState` field is set to `SUBSCRIPTION_STATE_PAUSED`. You can
see when the subscription is expected to renew again by checking the
[`PausedStateContext`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pausedstatecontext)
object.

A `SubscriptionNotification` message with type `SUBSCRIPTION_RECOVERED` is sent if
the subscription is resumed either automatically at the end of the pause period
or if the user chose to manually resume the subscription.

A `SubscriptionNotification` message with type `SUBSCRIPTION_ON_HOLD` is sent if
there was a payment failure while trying to resume the subscription after pause.

Both situations should be handled as described in [Account hold](https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold).

### Resubscribe

For auto-renewing subscription base plans, the Google Play Store may display a
**Resubscribe** button. This button allows users to regain access
to a subscription. It may not appear for various reasons, for example
when a subscription expired a long time ago.
| **Note:** For license testers, the **Resubscribe** button is always enabled regardless of the setting in the Google Play Console. To test your app's behavior when resubscribe is disabled, use a non-license-tester account.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/restoration.png) **Figure 7.** *Account \> Subscriptions* section of the Google Play Store app showing a canceled subscription with a **Resubscribe** button.

Although the button is always labeled **Resubscribe**, its functionality depends
upon the subscription state.

While a subscription is canceled but not yet expired, the user is still
subscribed and receiving subscription benefits. If the user taps Resubscribe,
the cancelation is effectively undone, and the subscription continues to renew.
This action is known as *restore* in Play developer documentation and APIs.

After an auto-renewing subscription has expired, you can allow users to purchase
the same subscription base plan. This action is known *resubscribe* in
Play developer documentation and APIs. You can configure this option
for each base plan in the [Play Console](https://support.google.com/googleplay/android-developer/answer/140504#zippy=%2Ccreate-and-activate-a-base-plan)
or using the API.

#### Restore prior to expiration

| **Note:** All developer apps are required to support Restore.

If your app relies solely on the
[`queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))
method to determine whether a user is entitled to a subscription, then your app
should automatically handle restorations because the `queryPurchasesAsync()`
method continues to return canceled purchases before their expiration dates. A
restored subscription continues to renew as if it were not canceled.

If your app synchronizes subscription state with a backend, you should listen
for a [`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub)
message with the type `SUBSCRIPTION_RESTARTED`. After you receive this RTDN,
your app can respond to the notification, record that the subscription is now
set to renew, and stop displaying restoration messages in your app. The
subscription resource looks similar to the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": next_renewal_date
          ...
        }
      ],
    }

| **Note:** A restored subscription uses the same purchase token from when the subscription was canceled. All cancellation fields are cleared from the subscription resource.

#### Resubscribe after expiration

If an auto-renewing base plan is configured using the Google Play Console or API
to allow Resubscribe, users can re-purchase an expired subscription in the
Google Play Store.

These are new purchases. Google Play issues a brand new purchase token, and your
backend receives an RTDN with type `SUBSCRIPTION_PURCHASED`. The purchase status
for this type of out-of-app purchase does not include a `linkedPurchaseToken`
associated with the original purchase in that case, because the original
subscription expired completely.

To ensure accurate user association for the re-purchased subscriptions and prevent automatic refunds for unacknowledged purchases, you must acknowledge the re-purchase on your backend server:

1. Call [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) with the new purchase token from the RTDN. The response for this type of out-of-app purchase includes the [`outOfAppPurchaseContext`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#OutOfAppPurchaseContext) field, present exclusively for unacknowledged resubscription purchases. This field provides:

   - `expiredExternalAccountIdentifiers`: An [`ExternalAccountIdentifiers`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#externalaccountidentifiers) object containing the `obfuscatedAccountId` and `obfuscatedProfileId` fields that were configured for the *previous* expired subscription, if they were set.
   - `expiredPurchaseToken`: The purchase token of the last expired subscription.

   Use either of these identifiers to look up and link the new purchase to the correct user account in your backend.
2. Call [`purchases.subscriptions.acknowledge`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge) to acknowledge the purchase.

   - Optionally, you can send the user's `obfuscatedAccountId` and `obfuscatedProfileId` if you had configured them using [`setObfuscatedAccountId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)) and [`setObfuscatedProfileId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedProfileId(java.lang.String)) during the in-app billing flow.

This server-side approach lets you acknowledge the purchase within three days from the date of purchase, even if the user doesn't open your app.

### Upgrades, downgrades, and resubscribe

When a user upgrades, downgrades, or [signs up after
cancellation from your app before the subscription expires](https://developer.android.com/google/play/billing/subscriptions#before-in-app), the old
subscription is invalidated and a [new subscription](https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto) is created with
a new purchase token.

In addition, the [subscription
resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions)
returned from the Google Play Developer API contains a `linkedPurchaseToken`
field that indicates the old purchase from which the user upgraded, downgraded,
or resubscribed. You can use the purchase token in that field to look up the old
subscription and identify the existing user account so that you can associate
the new purchase with the same account.

Before offering upgrade, downgrade, or resubscribe options to a user in your app,
you must acknowledge the existing subscription. Any plan change or resubscribe
is blocked if the existing subscription is still pending acknowledgement.

If the user successfully purchases the upgrade, downgrade, or resubscribe,
this is a new purchase which you must acknowledge. The recommended way
to do this is to use the [Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge).
The subscription resource looks similar to the following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      ...
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      "linkedPurchaseToken": old_purchase_token,
      ...
      "lineItems": [
        {
          "productId": "sub_variant_plan01",
          "expiryTime": next_renewal_date,
          "autoRenewingPlan": {
            "autoRenewEnabled": true
          }
        }
      ],
    }

### Price changes

See the [price change best practices guide](https://developer.android.com/google/play/billing/price-changes)
to learn about changing auto-renewing subscription prices and notifying users
when appropriate.

When a price change is added and for any updates to the price change status,
you will receive the `SUBSCRIPTION_PRICE_CHANGE_UPDATED` RTDN. You can query
the [purchases.subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) endpoint to get a
[subscription resource](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) which will contain price change details for each item
in the subscription.

When price changes are applied to existing subscribers as *opt-in*, you will
received an RTDN if the user takes action to confirm or reject the new price.

#### Handle user confirmation of an opt-in price change

When a user accepts your subscription price increase, you receive a
[SubscriptionNotification](https://developer.android.com/google/play/billing/rtdn-reference#sub) message with type
`SUBSCRIPTION_PRICE_CHANGE_UPDATED`.
| **Note:** For subscriptions without addons `SUBSCRIPTION_PRICE_CHANGE_CONFIRMED` notifications will also be sent. However, this notification is deprecated. For more information, see [Deprecations](https://developer.android.com/google/play/billing/deprecations).

#### Handle renewals after price change is applied

With a price decrease, or when the subscription price increase renews,
you will receive a `SubscriptionNotification` message with type
`SUBSCRIPTION_RENEWED`. Treat this notification like any other [renewal](https://developer.android.com/google/play/billing/lifecycle/subscriptions#renewal).

#### Handle cases where an opt-in price increase is not accepted

If a user hasn't accepted your opt-in price increase before they need
to renew at the higher price, they are automatically unsubscribed
and you receive a
[SubscriptionNotification](https://developer.android.com/google/play/billing/rtdn-reference#sub) message
with type `SUBSCRIPTION_CANCELED`. Handle this event as described in
[Cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel).

Users can also cancel their subscriptions for an opt-out price increase
following the same mechanism.

### Price step-up consent (applicable only for KR region)

Due to new South Korean (KR) regulations, subscription users in the KR region
must consent to any price step-ups that will occur after their free trial
or introductory period ends.

To help you comply with the regulation, Play will notify users in the KR region
about the consent requirement and will also store the consent response
from the users. Subscriptions are automatically canceled for users
who don't provide consent before the higher price takes effect. In addition
to the notifications sent from Play, you can also send your custom
price step-up notifications to your users, and can provide [link to
specific management page](https://developer.android.com/google/play/billing/subscriptions#link-specific) in your notifications.

When the consent period has begun or the user has provided
consent, you will receive a [SubscriptionNotification](https://developer.android.com/google/play/billing/rtdn-reference#sub) message with type
`SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED`.

#### Difference between price step-up and price change

A `price step-up` refers to an increase in the subscription price, due to a
transition from one offer phase to another. For
example, a subscription moving from a free trial to a regular price. You can use
the `offerPhase` field in the subscription resource to identify the current
phase of the subscription.

However, a `price change` refers to price updates initiated by you (developer)
for the base plan price for a subscription. For example,
opt-in price increase or opt-out price increase.

## Handle lifecycle for prepaid plans

As with auto-renewing subscriptions, you must acknowledge prepaid plans after
each [new purchase](https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto). In the case of prepaid plans, you must fully
process both the initial purchase and any top-ups, because the user has to go
through the purchase flow every time.

Due to the potential for short prepaid plan durations, it's important to
acknowledge the purchase as soon as possible. Prepaid plans with a duration of
one week or longer must be acknowledged within 3 days. Prepaid plans with a
duration shorter than one week must be acknowledged within half of the plan
duration. For example, developers have 1.5 days to acknowledge purchase of a
three-day prepaid plan.
| **Warning:** If a user on a prepaid plan purchases a top-up and you do not acknowledge the purchase within the corresponding timeframe, the top-up purchase is revoked, the remaining subscription is revoked and canceled, and the user is issued a refund.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/prepaid-states.svg) **Figure 8.** Lifecycle states and transition events for subscription purchases.

A [`SubscriptionNotification`](https://developer.android.com/google/play/billing/rtdn-reference#sub) message
with type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client whenever a
prepaid plan subscription is purchased, including every top-up. Call the
[`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)
method to check for the latest prepaid plan subscription state.

A new purchase token is issued for top-up purchases, and you receive the
previous purchase token in the `linkedPurchaseToken` field as part of the new
subscription purchase state. The purchase token is valid from subscription
signup until 60 days after expiration. After this date, the purchase token is
no longer valid to use to call the Google Play Developer API.

The subscription resource for a prepaid plan purchase looks similar to the
following example:

    {
      "kind": "androidpublisher#subscriptionPurchaseV2",
      "startTime": "2022-04-22T18:39:58.270Z",
      "regionCode": "US",
      "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
      "latestOrderId": "GPA.3333-4137-0319-36762",
      "acknowledgementState": "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED",
      "lineItems": [
        {
          "productId": "prepaid_plan01",
          "expiryTime": expiry_date,
          "prepaidPlan": {
            "allowExtendAfterTime": timestamp_after_which_topups_are_allowed
          }
        }
      ]
    }

You can see when the entitlement ends in the `expiryTime` field. Top-up
purchases increase the entitlement time by accumulating it. That means that if
the user tops up before their original entitlement ends, the new time is added
on top of their previous expiration date.

You might want to display a message in your app informing the user that their
prepaid subscriptions can be extended with a top-up. To know when a user will be
able to top-up, check the `allowExtendAfterTime` field in the subscription
resource.

Prepaid plans don't auto-renew, so they can't be canceled. If a user wants to
cancel a prepaid plan, they can let it reach its expiration date.

### SubscriptionPurchaseV2 fields for prepaid plans

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