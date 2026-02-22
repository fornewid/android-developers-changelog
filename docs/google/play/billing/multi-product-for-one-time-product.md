---
title: https://developer.android.com/google/play/billing/multi-product-for-one-time-product
url: https://developer.android.com/google/play/billing/multi-product-for-one-time-product
source: md.txt
---

This document describes how you can integrate your app with the multi-product feature of Play Billing Library (PBL).

The multi-product for one-time product (OTP) feature lets you combine several one-time products into a single unit. These bundled products can then be purchased, billed, and managed collectively. You can also create[discount offers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#discount-offers.)for these bundled OTPs to incentivize product purchases.

## Considerations

When you create one-time product bundles, note the following considerations:

- You can't have subscriptions in a one-time product bundle.
- You can't have a combination of digital content and service in the same one-time product bundle.
- The bundled one-time products must be available for immediate download. For example, a one-time product bundle can't have a pre-order purchase because it's not available for immediate download.
- The multi-product for one-time products doesn't support the[rent purchase option](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#rent-option).

## Integrate with Play Billing Library

This section assumes that you are familiar with the initial PBL integration steps such as,[adding the PBL dependency to your app](https://developer.android.com/google/play/billing/integrate#dependency), initializing the[BillingClient](https://developer.android.com/google/play/billing/integrate#initialize), and[connecting to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play). This section focuses on the PBL integration aspects that are specific to the multi-product OTP purchases.

### Launch a purchase flow

To launch a purchase flow for multi-product one-time products, do the following steps:

1. Create a product list having all the one-time products by using the[QueryProductDetailsParams.Builder.setProductList](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams.Builder#setProductList(java.util.List%3Ccom.android.billingclient.api.QueryProductDetailsParams.Product%3E))method.

2. Fetch all your one-time products by using the[`BillingClient.queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener))method.

   The following sample shows how to fetch all your one-time products:  

   #### Java

   ```java
   billingClient.queryProductDetailsAsync(
   queryProductDetailsParams,
   new ProductDetailsResponseListener() {
     public void onProductDetailsResponse(
         BillingResult billingResult, QueryProductDetailsResult productDetailsResult) {
       // check billingResult
       // ...
       // process productDetailsList returned by QueryProductDetailsResult
       ImmutableList productDetailsList = productDetailsResult.getProductDetailsList();
       for (ProductDetails productDetails : productDetailsList) {
         for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
             productDetails.getOneTimePurchaseOfferDetailsList()) {
                // ...
         }
       }
     }
   });
   ```
3. Set the[`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams.Builder#setProductDetails(com.android.billingclient.api.ProductDetails))object for each one-time product.

   | **Note:** All one-time products in the`ProductDetails`must be from the same app.
4. Specify the one-time product details in the[`BillingFlowParams.Builder.setProductDetailsParamsList`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E))method. The[`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams)class specifies the details of a purchase flow.

   The following sample shows how to launch the billing flow for a multi-product OTP purchase:  

   #### Java

   ```java
   BillingClient billingClient =
      BillingClient.newBuilder()
       // set other options
       .build();
   // ProductDetails obtained from queryProductDetailsAsync().
   ProductDetails productDetails1 = ...;
   ProductDetails productDetails2 = ...;
   ArrayList productDetailsList = new ArrayList<>();
   productDetailsList.add(productDetails1);
   productDetailsList.add(productDetails2);
   BillingFlowParams billingFlowParams =
   BillingFlowParams.newBuilder()
       .setProductDetailsParamsList(productDetailsList)
       .build();
   billingClient.launchBillingFlow(billingFlowParams);
   ```
   | **Note:** An in-app purchase will still be represented by the[`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase)object, but this object will also be associated with all the products acquired in the transaction.

## Process purchases

Processing multi-product OTP purchases is the same as for existing single-item purchases as described in[Integrate the Google Play Billing Library into your app](https://developer.android.com/google/play/billing/integrate#launch). The only difference is that you need to grant entitlement for all products instead of only one for multi-product OTP purchases so that the user can receive multiple entitlements with a single purchase. A multi-product OTP purchase returns multiple items which can be retrieved by using[`Purchase.getProducts()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts())in the Google Play Billing Library, and then the`lineItems`list in[`purchases.products.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)of the[Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2).

## Real-time developer notifications

The`sku`field isn't provided in[RTDN](https://developer.android.com/google/play/billing/rtdn-reference)for multi-product OTP purchases. The multi-product OTP purchases represent more than one product. Therefore, you can use the Play Developer APIs to get the purchase data, and see all the items in it.

## Refunds

In a multi-product OTP purchase, users can't request refunds for individual items, and you too can't issue refunds for individual items. However, request and issue of refunds for the entire multi-product OTP purchase is permitted. If you are cancelling a multi-product OTP purchase for a user, all the entitlements associated with the purchase are cancelled.
| **Note:** Refunded multi-product OTP orders will be available in the[Voided Purchases API](https://developer.android.com/android-publisher/voided-purchases)and RTDN.

## Financial reporting and reconciliation

Use the[Earnings report](https://support.google.com/googleplay/android-developer/answer/6135870)to reconcile your active multi-product OTP purchases with Google Payoffs and transactions on Play. Each transaction line item has an Order ID. For a multi-product OTP purchase, the[Earnings and Estimated sales reports](https://support.google.com/googleplay/android-developer/answer/2482017)will include separate rows (with the same Order ID) for each transaction such as charge, fee, tax, and refund, for each item involved.

For dashboards in the Play Console:

- The revenue statistics presented in the**Financial reporting**section of the console are broken down by individual products.

- Order management reflects multi-product OTP purchases, and show itemized lists of what was purchased. From order management, you may revoke, cancel or fully refund a user's purchase.