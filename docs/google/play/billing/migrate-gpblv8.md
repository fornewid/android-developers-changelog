---
title: Migrate to Google Play Billing Library 8 from versions 6 or 7  |  Android Developers
url: https://developer.android.com/google/play/billing/migrate-gpblv8
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Monetization](https://developer.android.com/google/play/billing)

Send feedback

# Migrate to Google Play Billing Library 8 from versions 6 or 7 Stay organized with collections Save and categorize content based on your preferences.




This document describes how to migrate from Google Play Billing Library (PBL) 6
or 7 to PBL 8 and how to integrate with the new optional subscription
capabilities.

For a full list of the changes in version 8.0.0, refer to the [release
notes](/google/play/billing/release-notes).

## Overview

PBL 8 contains improvements to existing APIs along with the removal of
previously deprecated APIs. This version of the library also includes new
APIs for one-time products.

## Backward-compatibility for PBL upgrade

To migrate to PBL 8, you need to update or remove some of your existing API
references from your app, as described in the [release notes](/google/play/billing/release-notes) and later
in this migration guide.

## Upgrade from PBL 6 or 7 to PBL 8

To upgrade from PBL 6 or 7 to PBL 8, do the following steps:

1. Update the Play Billing Library dependency version in your app's
   `build.gradle` file.

   ```
   dependencies {
     def billingVersion = 8.0.0
     implementation "com.android.billingclient:billing:$billingVersion"
   }
   ```
2. (Applicable only for upgrade from PBL 6 to PBL 8). Handle subscription
   related API changes in your app.

   The following table lists the subscription related APIs that are removed in
   PBL 8 and the corresponding alternate API that you must use in your app.

   | Previously deprecated API removed in PBL 8 | Alternate API to use |
   | --- | --- |
   |  |  |
   | --- | --- |
   | setOldSkuPurchaseToken | [setOldPurchaseToken](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken) |
   | setReplaceProrationMode | [setSubscriptionReplacementMode](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode) |
   | setReplaceSkusProrationMode | [setSubscriptionReplacementMode](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode) |
3. Update the implementation of the [`queryProductDetailsAsync`](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync) method.

   There is a change in the signature of the
   [`ProductDetailsResponseListener.onProductDetailsResponse`](/reference/com/android/billingclient/api/ProductDetailsResponseListener#onProductDetailsResponse(com.android.billingclient.api.BillingResult,java.util.List%3Ccom.android.billingclient.api.ProductDetails%3E)) method, which
   requires changes in your app for the [`queryProductDetailsAsync`](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync)
   implementation. For more information, see
   [Show products available to buy](/google/play/billing/integrate#show-products).
4. Handle the removed APIs.

   ### Upgrade from

   PBL 8 no longer supports the APIs listed in the following table.
   If your implementation uses any of these removed APIs,
   refer to the table for their corresponding alternate APIs.

   | Previously deprecated API removed in PBL 8 | Alternate API to use |
   | --- | --- |
   |  |  |
   | --- | --- |
   | queryPurchaseHistoryAsync APIs | See [Query Purchase History](/google/play/billing/query-purchase-history) |
   | querySkuDetailsAsync | [queryProductDetailsAsync](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) |
   | enablePendingPurchases() (API without parameters) | [enablePendingPurchases(PendingPurchaseParams params)](/reference/com/android/billingclient/api/BillingClient#enablePendingPurchases(com.android.billingclient.api.PendingPurchaseParams))   Note that the deprecated enablePendingPurchases() is functionally equivalent to `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`. |
   | queryPurchasesAsync(String skuType, PurchasesResponseListener listener) | [queryPurchasesAsync](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)) |
   | BillingClient.Builder.enableAlternativeBilling | [BillingClient.Builder.enableUserChoiceBilling](/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)) |
   | AlternativeBillingListener | [UserChoiceBillingListener](/reference/com/android/billingclient/api/UserChoiceBillingListener) |
   | AlternativeChoiceDetails | [UserChoiceDetails](/reference/com/android/billingclient/api/UserChoiceDetails) |

   ### Upgrade from

   The following table lists the APIs that are removed in PBL 8, and the
   corresponding alternate APIs that you must use in your app.

   | Previously deprecated API removed in PBL 8 | Alternate API to use |
   | --- | --- |
   |  |  |
   | --- | --- |
   | queryPurchaseHistoryAsync APIs | See [Query Purchase History](/google/play/billing/query-purchase-history) |
   | querySkuDetailsAsync | [queryProductDetailsAsync](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) |
   | enablePendingPurchases() (API without parameters) | [enablePendingPurchases(PendingPurchaseParams params)](/reference/com/android/billingclient/api/BillingClient#enablePendingPurchases(com.android.billingclient.api.PendingPurchaseParams))   Note that the deprecated enablePendingPurchases() is functionally equivalent to `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`. |
   | queryPurchasesAsync(String skuType, PurchasesResponseListener listener) | [queryPurchasesAsync](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)) |
5. (Recommended) Enable automatic service reconnection.

   The Play Billing Library can attempt to automatically re-establish the
   service connection if an API call is made while the service is
   disconnected. For more information,
   see [Enable automatic service reconnection](/google/play/billing/integrate#automatic-service-reconnection).
6. Optional changes.

   * Support pending purchases for prepaid plans. For more information, see
     [Handle Subscriptions and Pending Transactions](/google/play/billing/subscriptions#pending).
   * Virtual installment subscriptions. For more information, see
     [Installment Subscriptions Integration](/google/play/billing/subscriptions#installments).






Send feedback