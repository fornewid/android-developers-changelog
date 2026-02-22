---
title: https://developer.android.com/google/play/billing/price-changes
url: https://developer.android.com/google/play/billing/price-changes
source: md.txt
---

# Change subscription prices

You can change the prices of your subscription base plans and offers. For example, you might have digital products that need annual price adjustments, or you might change the set of benefits for a product and want to reflect these changes in the price.

For more information about changing subscription prices using the Play Console, see the documentation in the[Play Console Help Center](https://support.google.com/googleplay/android-developer/answer/140504).

To programmatically change the subscription base plan price, use the[`monetization.subscriptions.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch)method. This method receives a[`Subscription`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#resource:-subscription)object with the subscription product configuration that is being changed. Set the new price in the[`RegionalBasePlanConfig`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#regionalbaseplanconfig)object under the correct base plan in the subscription's`basePlans`collection. This can be very useful if you have a sizable catalog and you need to make updates to all of your products in a short period of time, or if you have a product catalog management system that automatically makes changes to your Google Play subscription products when changes occur.
| **Warning:** You should not change the price of a[Subscribe with Google](https://developers.google.com/news/subscribe)subscription.

It could be useful to visit your Play Console[change log](https://support.google.com/googleplay/android-developer/answer/6053184)to look up info about any price changes you have made in the past. The information you can find there includes when the prices were updated, who initiated the change, the regions that were updated, and more. This might assist you in cases where you need to review past price changes or review an accidental price change to assess next steps.

## Price changes for new subscription purchases

When you change the price of a base plan or offer, the new price takes effect within a few hours for all new purchases without you having to take any additional action.

## Price changes for existing subscribers

When you change subscription prices, existing subscribers are unaffected by default; they are placed into a legacy price cohort where they continue to pay their original base plan price when they renew.

If desired, you can move existing subscribers to the current base plan price. This is action is called[ending a legacy price cohort](https://developer.android.com/google/play/billing/price-changes#end-legacy). Changes to an offer's pricing phases cannot be applied to existing subscribers. For installment subscriptions, price changes for a legacy cohort happen at the end of the active commitment period. You cannot change the price currently being paid for a user who is in the middle of paying their installments.

## End a legacy price cohort

You can choose to end a legacy price cohort at any time. This can be done independently for each region. To end a legacy price through the Play Console, refer to the[Play Console Help Center](https://support.google.com/googleplay/android-developer/answer/140504).

### End a legacy price cohort with the Google Play Developer API

To programmaticaly end a legacy price cohort, use the[`monetization.subscriptions.basePlans.migratePrices`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans/migratePrices)method. This method migrates subscribers who are receiving a historical subscription price to the current base plan price for the specified regions. The method also triggers price change notifications to be sent to users who are currently receiving a historical price older than the supplied timestamp. When you send this request, you include a list of[`RegionalPriceMigrationConfig`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans/migratePrices#regionalpricemigrationconfig)objects in the request body to configure the price cohort migration.

For more information on using legacy price cohorts, see the[Play Console Help Center](https://support.google.com/googleplay/android-developer/answer/140504).

## Price decreases

When you end a legacy price cohort and the new purchase price is*lower*than the price that users in the cohort are paying, Google Play notifies the users by email and these subscribers begin paying the lower price the next time they pay for their base plan.

**Note:** [Payment authorization](https://support.google.com/googleplay/answer/2476088 "Payment authorization")may be placed up to 48 hours before the start of a user's next renewal period. However, for users in India or Brazil, this period extends to up to 5 days before the next renewal period. Users who have already been authorized at the higher price won't be immediately charged the lower price; they will renew at the lower price on their subsequent renewal.

[License testers](https://developer.android.com/google/play/billing/test)also receive email notifications for price decreases.

## Price increases

When ending a legacy price cohort and the new price is*higher*than the price that users in the cohort are paying, a price increase occurs. Price increases may or may not require user action.

By default, price increases are*opt-in*changes for existing subscribers. Users must explicitly accept the higher price before it is first charged, or Google Play automatically cancels their subscription. Users are charged the higher price the next time they pay for their base plan following an advance notification period of 37 days. Starting 30 days before this charge, Play notifies existing subscribers through email and push notifications.

During the first seven days after the cohort migration is triggered, no users receive notifications from Google Play. This means that you have seven days from when you initiate an opt-in price increase to notify your existing subscribers before Google Play begins notifying them directly. During this period, you can effectively cancel a pending price increase by making another price change back to the original price.

After that seven-day period, each user receives automatic notifications from Google Play 30 days before the first renewal with the new price.

In some cases when increasing prices for existing subscribers, you have the option to perform price increases with advance notification to users, but without requiring them to take any action. With this option, unless users*opt-out*by changing subscription plans or canceling their subscription, they'll be charged the new price the next time they pay for their base plan following an advance notification period. This period varies by country and is either 30 days or 60 days. Beginning that number of days before this charge, Play notifies existing subscribers through email and push notification.

Opt-out increases are only available in certain locations with limits on the increase amount and frequency, and are subject to certain developer requirements.

You can mark a legacy price cohort migration as an opt-out increase if it meets those criteria, as shown in figure 1.
![Google Play Console legacy price cohort migration with opt-out increase](https://developer.android.com/static/images/google/play/billing/opt-out-increase.png)**Figure 1.**Using Play Console to specify a legacy price cohort migration as an opt-out increase.

![](https://developer.android.com/static/images/google/play/billing/opt-out-increase.png)

## Communicate your price change to the user

| **Important:** This notice must be displayed on all device types where the app is available, including mobile, TV platforms, and streaming devices. The sole exception is watch devices, for which the notice is recommended but not required.

You should notify existing subscribers whenever you end their legacy price cohort.

For opt-out price increases, you should give users advance notification, and you must show users an in-app notice. Unlike opt-in price increases, there is no seven-day waiting period before Play starts notifying users directly.

For opt-in price increases, give users advance notification and inform them of the need to accept the price increase. When you initiate an opt-in price increase, you have seven days to notify your existing subscribers before Google Play begins to notify them directly. We recommend that you notify affected users in your app and provide a deep link to the Play Store subscription screen to help them easily review the new price. When users review an opt-in price increase on the Play Store subscription screen, a dialog similar to figure 2 is shown.
![Generic dialog notifying the user of a subscription price change](https://developer.android.com/static/images/google/play/billing/price-change-1.png)**Figure 2.**Example dialog notifying the user of a subscription price change.

## Handle user response to an opt-in price change

After you have notified existing subscribers of a price change and it's an opt-in increase, they may take action before the new price applies to accept or not accept the price increase. If they do, you will receive an RTDN informing you of the outcome. See the[purchase lifecycle guidance](https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-changes)to learn how to handle these notifications.

If the user doesn't act and they reach the first renewal that the opt-in price will apply to, their subscription is automatically canceled and expired on that renewal date.

## Accidental price increases

This section describes the various scenarios for handling an accidental price change.

- **Opt-in increase**- If you've accidentally initiated an opt-in price increase, reverse the change immediately by making another price change back to the original price.

  Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price decrease to the original price. Existing subscribers are not notified about the accidental price change if the price is reverted within seven days. If the price is reverted back to the old price after seven days, the price change will be canceled for any users who have not paid the new price. The price change is cancelled after the[payment authorization](https://support.google.com/googleplay/answer/2476088 "Payment authorization")period of up to five days. Based on renewal dates, some users may have already received the opt-in email notice.
- **Opt-out increase** - You can cancel an accidental opt-out increase by reverting the price back to the original price. Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price decrease to the original price. Depending on when the price is reverted if a user has not already paid the higher price, their price increase would be canceled after the[payment authorization](https://support.google.com/googleplay/answer/2476088 "Payment authorization")period of up to five days. Based on renewal dates, some users may have already received the price increase notice emails.

- **Price decreases**- You can cancel a price decrease by reverting the subscription's price back to its original value by using the Google Play Console. Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price increase to the original price. Developers can initiate either opt-in or opt-out (if eligible) to cancel the price decrease. If using opt-out, it would be counted toward the frequency. Google Play determines whether the cancellation is effective for a given user's next renewal based on the timing of this reversion relative to their individual renewal date.

  - A price decrease cancellation is valid if the period between reverting the price to its original value and a user's expected renewal time at the new price exceeds the relevant country-specific notification window (30 or 60 days). The user's next subscription renewal occurs at the original, higher price.

  - A price decrease cancellation is invalid if the period between reverting the price to its original value and a user's expected renewal time at the new price is shorter or equal to the relevant country-specific notification window (30 or 60 days). The user will instead go through the price increase process after being charged the lower price at least once upon the next renewal. The user will then get notified about a price increase. Depending on the mode selected during the price migration users would need to accept the price increase for opt-in price increase or would receive the notifications about an opt out increase. Any frequency and amount limitations for opt out increase would apply in this case.

## Handle overlapping price changes

Make sure that you only do one price change at a time. However, if you perform a price change multiple times, impacted users need to agree only to the latest price change. For example, if you've ended a legacy price cohort with an opt-in price increase, changed the price again, and then performed another opt-in price increase, affected users no longer need to respond to the first price increase because only the second price increase now applies. This behaviour applies for legacy price opt-in and opt-out price increases and price decreases.

When you start a new price migration for an item that has an older price migration in progress, Google Play handles it as follows:

- Old price migration is canceled.

  Google Play stops the old price migration. In the`SubscriptionPurchaseV2`API, you'll see the old price change details marked as`CANCELED`. You'll also receive a`SUBSCRIPTION_PRICE_CHANGE_UPDATED`RTDN.
- New Price Migration takes over.

  Immediately after, Google Play starts the new price migration. This will appear in`SubscriptionPurchaseV2`as either`OUTSTANDING`(for opt-in increases) or`CONFIRMED`(for opt-out increases or price decreases). You'll receive another`SUBSCRIPTION_PRICE_CHANGE_UPDATED`RTDN for the item.
- The user gets the new price.

  The user will now be moved to the new price migration, and they won't complete the previous price change. And the user receives the standard notification period for the new price.

## Test price changes

Don't change subscription prices for products owned by active subscribers for testing purposes.

You can use the[Play Billing Lab app](https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion)and license testers to test subscription price changes without affecting other active subscribers.

See the[testing guide](https://developer.android.com/google/play/billing/test#price-changes)to learn more about testing price changes.

## Examples

The examples in this section demonstrate how to apply best practices in different price change scenarios.  

### Opt-in price increase examples

#### Example 1: Monthly subscription opt-in price increase

On March 3, AltoStrat increases the price for AltoStrat Pro, their premium video streaming subscription, by ending a legacy price cohort. They move users in the legacy price cohort of $1 to the current base plan price of $2. The effective date of the price change is April 9 (37 days after March 3).

Alice is an existing subscriber whose next renewal is on March 5. The first renewal after the effective date is on May 5, so she renews on March 5 and on April 5 at the old price ($1). When she renews again on May 5, she is charged the new price ($2). Google Play starts notifying Alice of the price change on April 5, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-1.svg)**Figure 3.**Example price change timeline diagram of a monthly subscription with a March 5 renewal date.

Bob is an existing subscriber whose next renewal is on March 29. He renews on March 29 at the old price ($1) because the price change has not yet taken effect. When he renews again on April 29, he is charged the new price ($2). He starts receiving price change notifications on March 30, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-2.svg)**Figure 4.**Example price change timeline diagram of a monthly subscription with a March 29 renewal date.

#### Example 2: 3 month subscription opt-in price increase

On March 3, FindMyLove ends a legacy price cohort and increases the 3-month fee for FindMyLove Premium from $1 to the base plan price of $2. The effective date of the price change is April 9 (37 days after March 3).

Alice is an existing subscriber whose next renewal is on March 5. Alice renews at the old price ($1) because the price change has not yet taken effect. When she renews again on June 5, she is charged the new price ($2). She starts receiving notification of the price change on May 6, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-3.svg)**Figure 5.**Example price change timeline diagram of a 3 month subscription with a March 5 renewal date.

Bob is an existing subscriber whose next renewal is on April 11. Bob renews at the new price ($2) because it's after the effective date for the price change. He starts receiving notifications of the price change on March 12, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-4.svg)**Figure 6.**Example price change timeline diagram of a 3 month subscription with an April 11 renewal date.

#### Example 3: Weekly subscription opt-in price increase

On March 3, CutePetsNews ends a legacy price cohort triggering a price migration of weekly fee for Weekly Dog Alerts from $1 to $2. The effective date of the price change is April 9.

Alice is an existing subscriber whose next weekly renewal is on March 6. She renews on March 6, March 13, March 20, March 27, and April 3 at the old price ($1) because the price change has not yet taken effect. When she renews again on April 10, she is charged the new price ($2). She starts receiving notification of the price change on March 11, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-5.svg)**Figure 7.**Example price change timeline diagram of a weekly subscription with an April 6 renewal date.

#### Example 4: Monthly subscription with multiple opt-in price changes

This example demonstrates how multiple price changes are handled.

On March 3, AltoStrat triggers a price migration for AltoStrat Pro, their premium video subscription, increasing the price from $1 per month to $2. On March 10, the developer triggers a second price migration, increasing the price to $3 per month.

The effective date of the first price change is April 9 (37 days after March 3). The effective date of the second price change is April 16 (37 days after March 10).

Alice's next renewal is on March 5. The first renewal after the effective date is on May 5, so she renews on March 5 and on April 5 at the old price ($1). When she renews again on May 5, she is charged the newest price ($3). She only receives notifications about the second price change because the price changes happened within the 7-day freeze period. She starts receiving notification of the price change on April 5, which is 30 days before the first renewal date with the new price.
![](https://developer.android.com/static/images/google/play/billing/price-change-schedule-monthly-example-6.svg)**Figure 8.**Example price change timeline diagram of a monthly subscription with multiple price changes and a March 5 renewal date.

#### Example 5: 12-month installment subscription opt-in price increase

This example shows how price increases are handled for installment subscriptions.

On March 3, AltoStrat increases the price for AltoStrat Pro, their premium video streaming subscription, by ending a legacy price cohort. They move users in the legacy price cohort of $1 to the current base plan price of $2. The effective date of the price change is April 9 (37 days after March 3).

Alice is an existing subscriber who signed up for a 12-month installment plan followed by monthly auto-renewals on June 10 of the previous year. Her first renewal is on June 10 of the current year. Since Alice is in the middle of paying her installments, she continues to pay $1 on March 10, April 10, and May 10. She has her first renewal on June 10, where she is charged the new price ($2) and switches to a monthly auto-renewal cadence. Google Play starts notifying Alice of the price change on May 11, which is 30 days before the first renewal date with the new price.  

### Opt-out price change examples

#### Example 1: Monthly subscription opt-out price change

This example shows how opt-out price increases are handled.

AltoStrat needs to make their annual price adjustment to account for programming cost increases. On January 2, they change the price of AltoStrat Pro (their premium video streaming subscription) from $1 to $1.30. This price increase meets the criteria for an opt-out price migration. They immediately end the legacy price cohort, specifying an opt-out migration. Users in this cohort are in regions requiring a 30-day minimum opt-out notification period, so the new price is effective on February 1.

Alice is an existing subscriber, charged on the 14th of each month. Due to the 30-day minimum notification period, she pays the old price ($1) on January 14. Google Play starts notifying Alice of the price change on January 15, and she starts paying the new price ($1.30) on February 14.  

### Price step-up consent examples

The[price step-up consent](https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-stepup-consent)examples in this section are applicable only to the South Korea (KR) region.

#### Example 1: User consents to the price step-up during signup

On March 3, a user signs up for a subscription in South Korea with a free trial period of 10 days. The user consents to price step-up during signup. In this scenario, Play applies the price step-up on March 13.

#### Example 2: User doesn't consent to the price step-up during the free trial

On March 3, a user signs up for a subscription in South Korea with a free trial period of 10 days. The user didn't consent to the price step-up during the signup or the free trial. The following is the sequence of events in this scenario:
![](https://developer.android.com/static/images/google/play/billing/price-stepup-example-2.png)**Figure 9.**Example timeline diagram when a user doesn't consent to the price step-up during a free trial.A consent period can be for a maximum of 30 days before the step-up price takes effect. Therefore, in this scenario, if the free trial period is for 40 days, then the consent period would start on March 13 and end on April 12.

#### Example 3: User consents to the price step-up during the free trial

On March 3, a user signs up for a subscription in South Korea with a free trial period of 10 days. The user consents to the price step-up during the free trial. The following is the sequence of events in this scenario:
![](https://developer.android.com/static/images/google/play/billing/price-stepup-example-3.png)**Figure 10.**Example timeline diagram when a user doesn't consents to the price step-up during a free trial.

#### Example 4: User doesn't consent to the price step-up for an introductory offer

On March 3, a user signs up for a subscription in South Korea with an introductory price period of 60 days. The user doesn't consent to the price step-up during the signup. The following is the sequence of events in this scenario:
![](https://developer.android.com/static/images/google/play/billing/price-stepup-example-4.png)**Figure 11.**Example timeline diagram when a user doesn't consent to the price step-up during an introductory offer.

#### Example 5: User consents to the price step-up during both free trial and introductory offer

If you are offering a subscription for both free trial and an introductory offer, Play asks for user consent at the following events:

1. During the free trial period, Play asks for the user's consent to move from free trial to introductory price.
2. If the user consents during the free trial, then during the introductory price period, Play asks for the user's consent to move from the introductory price to the regular price.

For example, on March 3, a user signs up for a subscription in South Korea with a free trial period of 10 days and an introductory price period of 30 days. The user consents to the price step-up during both the free trial and the introductory offer. The following is the sequence of events in this scenario:
![](https://developer.android.com/static/images/google/play/billing/price-stepup-example-5.png)**Figure 12.**Example timeline diagram when a user consents to the price step-up during both free trial and an introductory offer.