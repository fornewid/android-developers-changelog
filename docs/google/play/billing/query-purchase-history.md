---
title: https://developer.android.com/google/play/billing/query-purchase-history
url: https://developer.android.com/google/play/billing/query-purchase-history
source: md.txt
---

`queryPurchaseHistory()`was deprecated in Play Billing Library 7. This page describes the recommended alternatives for use cases your app may have relied on`queryPurchaseHistory()`for.

## Process Purchases

To retrieve purchases for processing, use[`queryPurchasesAsync(QueryPurchaseParams, PurchasesResponseListener)`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)).

See the[Processing Purchases](https://developer.android.com/google/play/billing/integrate#process)section of our integration guide for more details.

## Handle Voided Purchases

To fetch voided or cancelled purchases, use the[voided purchases](https://developers.google.com/android-publisher/voided-purchases)server developer API.

## Track Historical Purchases

If your app would like to track a user's purchase history your app should keep track of the history on your apps backend.