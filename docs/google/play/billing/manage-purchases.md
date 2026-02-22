---
title: https://developer.android.com/google/play/billing/manage-purchases
url: https://developer.android.com/google/play/billing/manage-purchases
source: md.txt
---

You may need to take management actions on subscriptions or one-time purchases
as part of day-to-day business. For example, your customer service may need to
issue total or partial refunds for users, or you might need to revoke
entitlements in certain cases. You can [manage orders from the Play Console](https://support.google.com/googleplay/android-developer/answer/2741495), or if
you want to manage them from your own system, you can do so by using the
[Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/orders).

## Cancel subscriptions

Subscription cancellations can be initiated by users or developers.

### User initiated cancellations

Users can cancel a Google Play subscription at any time using the Play Store. If
applicable, you must also provide an option for users to cancel their
subscriptions in your app and on your website.

The easiest way to enable users to cancel voluntarily is by [providing
deep links in your app to the
Play Store](https://developer.android.com/google/play/billing/subscriptions#use-deep), where they can view
and manage their subscriptions.

### Developer initiated cancellations

As a developer, you may also need to trigger cancellations from your backend.
The [`purchases.subscriptions.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel)
API lets you cancel a subscription purchase.
For example, you could use this method to turn down a legacy service.
Cancelling a subscription doesn't issue a refund, and the user retains access
until the end of their current billing period.

This method lets you specify the following types of cancellations in the
`cancellationType` request body parameter:

- **USER_REQUESTED_STOP_RENEWALS**: Cancels the subscription as if users
  have cancelled from the Play Store. Any installment payments
  will continue for the remainder of the current commitment period. From the
  Play Store, users may restore the subscription before it expires,
  or re-subscribe after it expires if enabled for the base plan.

- **DEVELOPER_REQUESTED_STOP_PAYMENTS**: Cancels the subscription and prevents
  any further payments. Users can't restore or re-subscribe to the subscription
  from the Play Store, however you can enable them to subscribe again
  within your app.

| **Note:** Specifying `cancellationType` is optional. If you don't specify the parameter in your [`purchases.subscriptions.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel) API request, by default, the default behavior is `DEVELOPER_REQUESTED_STOP_PAYMENTS`.

#### Enable users to restore unexpired subscriptions

In some scenarios, you may find it useful to allow users to restore unexpired
subscriptions from the Play subscription center after you have triggered the
cancellation as a developer. For example,
you may want to provide a customized in-app cancellation flow. Based on your
business logic, you can decide which cancellations triggered from your backend
are restorable by users.

To indicate that a user can restore the cancellation, issue a POST request
to the [`purchases.subscriptions.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel) API, and set the `cancellationType`
request parameter to the `USER_REQUESTED_STOP_RENEWAL` value.

Example:

- Purchase token of the subscription `1a2b3c4d5e6f7g8h9i0j`
- Application package name `com.your.app`
- Subscription ID `your-subscription-product`

HTTP POST request:

    https://androidpublisher.googleapis.com/androidpublisher/v3/applications/com.your.app/purchases/subscriptions/your-subscription-product/tokens/1a2b3c4d5e6f7g8h9i0j:cancel

Request body:

    {
      "cancellationType": "USER_REQUESTED_STOP_RENEWAL"
    }

#### Enable users to resubscribe expired subscriptions

To allow the resubscription of an expired subscription, you must [enable
the **Resubscribe** option](https://support.google.com/googleplay/%0Aandroid-developer/answer/140504) in the subscription's base plan and then
cancel the subscription by setting the `cancellationType` parameter to the
`USER_REQUESTED_STOP_RENEWAL` value.

#### Enable users to resubscribe only in your application

If you have set the `cancellationType` parameter to `DEVELOPER_REQUESTED_STOP
_PAYMENTS` or haven't set the `cancellationType` parameter, users can't
restore their subscription from the Play subscription center. However, users can
sign up again for the subscription through your app if required.

Taking this action triggers a `SUBSCRIPTION_CANCELED` Real-time developer
notification. Handle these cancellations as described in
[Cancellations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel).
| **Note:** If you cancel an installment subscription with the [`purchases.subscriptions.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel) API, setting the `cancellationType` parameter to `USER_REQUESTED_STOP_RENEWAL`, cancels only the next renewal of their installment, while the user still needs to finish the commitment. However, setting the parameter value to `DEVELOPER_REQUESTED_STOP_PAYMENTS`, stops the next payment.

## Defer billing

You can extend the entitlement period for a subscription by
using the [`subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method. When you defer a subscription with add-ons, all items in
the subscription are deferred by the same duration. During the deferral period, the user remains subscribed to your content though is not charged for the extra time. When you defer billing for a subscription, the status information is updated accordingly and you see it reflected in the `expiryTime` field in the
purchase status information:

- For active recurring subscriptions, deferred billing extends the next renewal date.
- For prepaid plans, deferred billing extends the expiration time.

Some examples on how you could use deferred billing are:

- Give users no-cost access as a special offer, such as giving one week free to existing subscribers for filling out a feedback survey.
- Give customers no-cost access as a customer-care action, for example after an extended outage that might have affected their ability to use your service.

Billing can be deferred by as little as one day and up to a year per API call.
To defer the end of the entitlement even further, call the API again
before the new expiration date arrives.

Taking this action triggers a `SUBSCRIPTION_DEFERRED` Real-time developer
notification. See [Defer billing for a subscriber](https://developer.android.com/google/play/billing/subscriptions#defer) in [About subscriptions](https://developer.android.com/google/play/billing/subscriptions) to learn how to handle these events.

Example:

1. FitnessGoals streaming service wants to run a promotion to
   encourage regular exercise in February.

2. They decide to offer an additional one month of service to any subscriber
   who exercises with FitnessGoals at least 10 times during the month of
   February.

3. They track the challenge's results, and on March 1st, they call the [subscriptionsv2.defer](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer) method for every active subscription purchase belonging to
   users that met the challenge in February.

4. These users get the benefit of an extra full month of regular exercise videos at no cost, and the users tell all their friends how FitnessGoals helps them stay healthy!

## Issue refunds and revocations

There are many situations where you may want to issue a refund for or revoke
access to a subscription or one-time purchase.

### Fully refund an order by order ID

With the [`orders.refund`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund)
API, you can issue full refunds for any order within three years of purchase.
The `orders.refund` method receives a revoke parameter indicating whether or not
access should be revoked in addition to providing the refund.

If you issue a revocation with the refund call for subscription purchase, the
subscription is immediately terminated and it triggers a`SUBSCRIPTION_REVOKED`
Real Time Developer Notification. Read the subscription lifecycle management
guide [Revocations section](https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke)
to learn how to handle these events.

Example:

1. To celebrate the beginning of the new world cup, the e-sports app
   Football-Not-Soccer decides to raffle off free virtual jerseys for all users
   who purchase new team kits in the first 24 hours.

2. Football-Not-Soccer uses the [`orders.refund`](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund)
   API without passing a revoke parameter to refund the jersey purchases to the
   winners.

| **Note:** Access to a subscription can only be revoked for subscriptions with current entitlement. When using the `revoke` parameter while refunding an order, make sure the order is the latest associated with the subscription. If it is not , the refund will be successful, but the subscription won't be revoked. If your use case requires revoking access to an active subscription, Use the [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) API with the purchase ID instead of the refund API with a revoke parameter.

### Revoke and refund a subscription by purchase token

For certain use cases you might need to revoke access to a user's subscription
and provide a refund. Play Billing offers revocation methods including full
refunds and prorated refunds through the [`subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
API. With this endpoint, you can specify [`revocationContext`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke#revocationcontext)
to determine how the refund is calculated.

Taking this action triggers a `SUBSCRIPTION_REVOKED` Real Time Developer
Notification. Your app should handle these cancellations as described in
[Revocations](https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke).

Example:

- Purchase with purchase token `1a2b3c4d5e6f7g8h9i0j`
- Application with the package name `com.your.app`
- Intent of issuing a prorated refund

HTTP POST request:

    https://androidpublisher.googleapis.com/androidpublisher/v3/applications/com.your.app/purchases/subscriptionsv2/tokens/1a2b3c4d5e6f7g8h9i0j:revoke

Request body:

    {
      "revocationContext": {
        "proratedRefund": {}
      }
    }

#### Full refunds

If you need to terminate a subscription and refund the full amount of the
current billing period, issue a full refund. Use the
[`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
function, and set `"fullRefund": {}` as the refund type.

Example:

1. Maria has an auto-renewing 30-day subscription to SuperMovies streaming
   monthly plan. Maria encountered some technical issues that prevent her from
   accessing the content. She contacts customer service on day 3 of her billing
   cycle stating that she never got access to the subscription.

2. Customer service locates Maria's subscription purchase details in
   their system and triggers a call to [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
   requesting a full refund.

3. Customer service tells Maria she should get 100% of her
   subscription price refunded and she is not subscribed to the plan anymore.

#### Prorate refunds

If you need to terminate a subscription and partially refund the remaining
entitlement time, issue a prorated refund. Use the
[`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
function, and set `"proratedRefund": {}` as the refund type.

Example:

1. Maria has an auto-renewing 30-day subscription to SuperMovies streaming
   monthly plan. She has happily used the service for some time.
   Maria contacts customer service on day 15 of her billing cycle stating that she
   is moving abroad and won't be able to use the service anymore starting the
   next day.

2. Customer service locates Maria's subscription purchase details in
   their system and triggers a call to [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke)
   requesting a prorated refund.

3. Customer service tells Maria she should get about 50% of her
   subscription price refunded and that access to the service terminated
   immediately.

| **Note:** The [`purchases.subscriptionsv2.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke) API is a replacement and improvement of the legacy [`purchases.subscription.revoke`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke). The main difference is that the new method allows partial refunds while the legacy is capable of only full refunds. Be aware that a user refund is based on the value of the latest order.