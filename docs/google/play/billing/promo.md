---
title: https://developer.android.com/google/play/billing/promo
url: https://developer.android.com/google/play/billing/promo
source: md.txt
---

# Promo codes

Promotions, or*promo codes*, enable you to give one-time products or trials to subscriptions free-of-charge to a limited number of users. The user enters a promo code, either in your app or in the Google Play Store app, and receives the item or subscription trial at no cost.

Within the Play Console, you can create the following types of promo codes:

- **One-time use codes**: These are automatically-generated unique codes that users can redeem only once. Users redeem these codes either directly from the Play Store or from within your app.
- **Custom codes**: You can specify custom codes that can be redeemed multiple times up to your predefined limit. Custom codes are available only for subscriptions and can be redeemed only by users who have not previously subscribed.

You can use promo codes in many ways to creatively engage with users, including the following:

- You might distribute cards with promo codes at an event, and users would enter their promo codes to unlock a special in-game item.
- You might give codes to employees so they can share them with their friends and family.
- You might send a promo code to people who buy your app during a certain period of time.

For subscriptions, note the following:

- Promo codes offer free trials to subscriptions and not free subscriptions.
- Promotions do not extend other free trials. If a subscription begins with a free trial without requiring a promo code, a promotion would override the original free trial length.
- Users who would otherwise not be eligible for free trials---for example, users who had purchased a subscription in the past but are no longer subscribed---are still eligible for a free trial through a promotion.
- You can create only one promo code per subscription product. That is, you can create a promo code only for a single base plan or offer.

Users can redeem promo codes in the Google Play Store up until a promotion end date that you specify in the Play Console. Promotions can last up to one year.

Before implementing a promotion, be sure to consider the following:

- For one-time products, you can create up to**500 promo codes per quarter** across all managed products in an app. You can use different combinations of promo codes that include one or more one-time products. Examples include the following:
  - 500 promo codes for a single one-time product.
  - 100 promo codes, each for five different one-time products.
- For subscription promotions, you can create up to**10,000*one-time use codes*per quarter per subscription product**. This limit does not count toward the limit of promo codes for one-time products.
- When creating a subscription promotion with custom codes, you can choose a redemption limit between 2,000 and 99,999.

| **Note:** Once you create a promotion, you can't change the number of promo codes in that promotion, and you can't switch those promo codes to a different type.
| **Note:** If you don't use all of your promo codes in a quarter, you lose access to them. Unused codes don't carry over to the next quarter.

## Creating and managing promotions

To learn how to set up and manage promotions, see[Create Promotions](https://support.google.com/googleplay/android-developer/answer/6321495).

## User redemption flow

Once a user has a promo code, they can redeem it in one of the following ways:

- **In your app:** The user can initiate the purchase by clicking the down arrow next to the form of payment in the Google Play purchase screen and then clicking the**Redeem**link to type in the code.
- **In the Play store:** The user can manually enter the code in the Google Play Store by clicking the Play Store left navigation menu and tapping**Redeem Code** .
  - The user can also skip manual code entry by instead following a[deep link](https://developer.android.com/google/play/billing/promo#deep-link)to the Google Play Store.

As an example, figure 1 shows a purchase screen for a subscription. To enter a promo code, tap the arrow next to the current payment method to show the**Payment methods** screen, as shown in figure 2. Next, tap**Redeem code** to go to the**Redeem a gift card or promo code** screen, as shown in figure 3. You can then enter your promo code on this screen and tap*Redeem*to finish.
![a subscription purchase dialog](https://developer.android.com/static/images/google/play/billing/promo-purchase-screen.png)**Figure 1.**A subscription purchase dialog.![screen that lists payment methods for an in-app purchase](https://developer.android.com/static/images/google/play/billing/promo-payment-methods.png)**Figure 2.**Screen that lists payment methods for an in-app purchase.![promo code screen](https://developer.android.com/static/images/google/play/billing/promo-redeem.png)**Figure 3.**Promo code screen.

For subscription promo codes, note the following:

- Custom codes can be redeemed only from within your app, while one-time codes can be redeemed through both your app and the Play store.
- After the user redeems the code, they still need to purchase the subscription with the code applied. A valid form of payment is required for the subscription, and the subscription will auto-renew at the end of the promo code free trial period.
- If using Billing Library version 2.0 or higher, a user who redeems a one-time code from the Play store is immediately asked to purchase the subscription through the Play store. This is an out-of-app purchase, so be sure that your app can[handle these purchases gracefully](https://developer.android.com/google/play/billing/integrate#ooap).
  - If your app does not yet support Billing Library 2.0, the user must download your app, navigate to the correct subscription, and then purchase the subscription from within your app to use the promotion code.

## Implementing promo codes

To ensure your app is ready to handle promo codes, your app needs to properly handle redemptions that occur outside of your app. To learn more, see[Processing purchases](https://developer.android.com/google/play/billing/integrate#process),[Fetching purchases](https://developer.android.com/google/play/billing/integrate#fetch), and[Handling purchases made outside of your app](https://developer.android.com/google/play/billing/integrate#ooap)in[Integrate the Google Play Billing Library into your app](https://developer.android.com/google/play/billing/integrate).

## Deep link

You can also share a promo code by generating a URL that sends the user to the Google Play Store and auto-populates the**Enter code**field. Use the following format for a promo code URL:  

    https://play.google.com/redeem?code=promo_code

Figure 4 shows the Google Play app's**Redeem Code**dialog:
![google play app's redeem code dialog](https://developer.android.com/static/images/google/play/billing/redeem-code-dialog.png)**Figure 4.** Google Play app's**Redeem Code**dialog.

After the user presses**Redeem**, if the latest version of your app is installed, the Google Play Store prompts the user to open the app. Otherwise, the Google Play Store prompts the user to update or download your app.

## Testing promo codes

To test your promo code implementation, see[Test promo codes](https://developer.android.com/google/play/billing/test#promo).