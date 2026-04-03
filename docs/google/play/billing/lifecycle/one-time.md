---
title: https://developer.android.com/google/play/billing/lifecycle/one-time
url: https://developer.android.com/google/play/billing/lifecycle/one-time
source: md.txt
---

# One-time purchase lifecycle

One-time purchase products have a simpler lifecycle than subscription products, but there are still several states and transition events that your backend needs to be able to handle properly.
![](https://developer.android.com/static/images/google/play/billing/lifecycle/one-time-states.svg)**Figure 1**Lifecycle states and transition events for one-time purchases.

## New one-time product purchases

After the user completes the billing flow, your app can see information about the new purchase in one of the following ways:

- Setup[`Real-time developer notifications`](https://developer.android.com/google/play/billing/getting-ready#enable-rtdn "Real-time developer notifications")and enable`Get all
  notifications for subscriptions and one-time products`to receive updates on the status of purchases.
- Implement the[`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener)interface from`BillingClient`to automatically receive purchase updates.
- Call the[`BillingClient.queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))method.

After receiving the new purchase, use the[`getPurchaseState`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#getPurchaseState())method or[`purchases.productsv2.getproductpurchasev2 in Play Developer API`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2/getproductpurchasev2 "purchases.productsv2.getproductpurchasev2 in Play Developer API")

to determine the payment state of the new purchase.

### Real-time developer notifications

| **Note:** One-time purchase real-time developer notifications are only published if you have[opted into them while configuring real-time developer notifications](https://developer.android.com/google/play/billing/getting-ready#enable-rtdn "Real-time developer notifications").

When a user purchases or cancels the purchase of a one-time product, Google Play sends a[`OneTimeProductNotification`](https://developer.android.com/google/play/billing/rtdn-reference#one-time)message. To update your backend purchase state, use the purchase token provided in the`OneTimeProductNotification`object to call the[`purchases.productsv2.getproductpurchasev2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2)method. This method provides the latest purchase and consumption status given a purchase token.

When a pre-order is fulfilled and its purchase state changes to PURCHASED, an RTDN is sent to your client. After receiving the RTDN, process the pre-order purchase as described in[Process one-time product purchases in your backend](https://developer.android.com/google/play/billing/lifecycle/one-time#process).

You should handle transaction-related RTDNs in your secure backend.

### Handle completed transactions

When a user completes a one-time product purchase, Google Play sends a`OneTimeProductNotification`message with the type`ONE_TIME_PRODUCT_PURCHASED`. When you receive this RTDN, process the purchase as described in[Process one-time product purchases in your backend](https://developer.android.com/google/play/billing/lifecycle/one-time#process).

### Handle canceled transactions

When a one-time product purchase is canceled, Google Play sends a`OneTimeProductNotification`message with the type`ONE_TIME_PRODUCT_CANCELED`if you have configured to receive real-time developer notifications. For example, this can occur if the user doesn't complete payment within the required timeframe, or if the purchase is revoked by the developer or by customer request. When your backend server receives this notification, call the[`purchases.productsv2.getproductpurchasev2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2)method to get the latest purchase state, then update your backend accordingly, including user entitlements.

If a one-time product purchase in`Purchased`state gets refunded, you will also be made aware using the[Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases).

## Process one-time product purchases in your backend

Whether you have detected a new purchase using a`ONE_TIME_PRODUCT_PURCHASED`RTDN or you have been made aware in-app through[`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener)or[manually fetching purchases](https://developer.android.com/google/play/billing/integrate#fetch)in your app's`onResume()`method, you must process the new purchase. We recommend that you handle purchase processing in your backend for better security.

Follow these steps to process a new one-time purchase:

1. Query the[`purchases.productsv2.getproductpurchasev2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2)endpoint to obtain the latest one-time product purchase status. To call this method for a purchase, you need the corresponding`purchaseToken`either from your app or from the`ONE_TIME_PRODUCT_PURCHASED`RTDN.
2. Call[`getPurchaseState()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#getPurchaseState())and make sure that the purchase state is`PURCHASED`.
3. [Verify the purchase](https://developer.android.com/google/play/billing/security#verify).
4. Give the user access to the content. The user account associated with the purchase can be identified with the[`obfuscatedExternalAccountId`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2#ProductPurchaseV2)field from`purchases.productsv2.getproductpurchasev2`, if one was set using[`setObfuscatedAccountId()`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String))when the purchase was made.
   1. For non-consumable product purchases, acknowledge delivery of the content by calling the[`purchases.products.acknowledge`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge)method. Make sure that the purchase hasn't been previously acknowledged by checking the[`acknowledgementState`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2)field.
   2. If the product is consumable, mark the item as consumed by calling the[`purchases.products.consume`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume)method so that the user can buy the item again after they have consumed it. This method also acknowledges the purchase.

| **Note:** If you don't acknowledge a purchase within three days, the user automatically receives a refund, and Google Play revokes the purchase.

There are also purchase acknowledgement and consume methods available in the Play Billing Library that allow you to process purchases from you app, but we recommend that you handle processing in your backend if you have one for a more secure implementation.