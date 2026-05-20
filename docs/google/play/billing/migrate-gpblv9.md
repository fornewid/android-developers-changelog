---
title: https://developer.android.com/google/play/billing/migrate-gpblv9
url: https://developer.android.com/google/play/billing/migrate-gpblv9
source: md.txt
---

This document describes how to migrate from Google Play Billing Library (PBL) 7
or 8 to PBL 9 and how to integrate with the new features.

For a full list of the changes in version 9.0.0, refer to the [release
notes](https://developer.android.com/google/play/billing/release-notes#9-0-0).


**Important:** You can now use an agent skill to migrate
to the latest Play Billing Library (PBL) version. Explore the
[PBL migration skill on GitHub](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade).

<br />

## Overview

PBL 9 contains improvements to existing APIs along with the removal of
previously deprecated APIs. This version of the library also introduces richer error context through new sub-response codes.

## Backward-compatibility for PBL upgrade

To migrate to PBL 9, you need to update or remove some of your existing API
references from your app, as described in the [release notes](https://developer.android.com/google/play/billing/release-notes) and later
in this migration guide.

## Upgrade from PBL 7 or 8 to PBL 9

To upgrade from PBL 7 or 8 to PBL 9, do the following steps:

1. Update the Play Billing Library dependency version in your app's
   `build.gradle` file.

       dependencies {
         def billing_version = "9.0.0"
         implementation "com.android.billingclient:billing:$billing_version"
       }

   If you're using Kotlin, the Google Play Billing Library KTX module contains
   Kotlin extensions and coroutines support that enable you to write idiomatic
   Kotlin when using the Google Play Billing Library. To include these
   extensions in your project, add the following dependency to your app's
   `build.gradle` file as shown:

       dependencies {
         val billing_version = "9.0.0"
         implementation("com.android.billingclient:billing-ktx:$billing_version")
       }

2. (Applicable only for upgrade from PBL 7 to PBL 9). Update the
   implementation of the [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync) method.

   There is a change in the signature of the
   [`ProductDetailsResponseListener.onProductDetailsResponse`](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsResult) method, which
   requires changes in your app for the [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync)
   implementation. For more information, see
   [Show products available to buy](https://developer.android.com/google/play/billing/integrate#show-products).
3. Handle the removed APIs.

   > [!TIP]
   > **Tip:** To handle the removed APIs, you can use the [Play Billing Library Version Upgrade Skill](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade). The skill is tailored to streamline your migration from the retired patterns to the latest PBL standards. By automatically detecting outdated method calls, the skill provides precise recommendations for updating your implementation to the latest standards.

   The following table lists the APIs that are removed and the
   corresponding alternate APIs that you must use in your app.

   ### Upgrade from


   PBL 9 no longer supports the APIs listed in the following table.
   If your implementation uses any of these removed APIs,
   refer to the table for their corresponding alternate APIs.

   | Previously deprecated API removed | Alternate API to use |
   |---|---|
   | queryPurchaseHistoryAsync APIs | See [Query Purchase History](https://developer.android.com/google/play/billing/query-purchase-history). If you were using queryPurchaseHistoryAsync to determine eligibility for free trials, you should now use [ProductDetails.getSubscriptionOfferDetails()](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails#getSubscriptionOfferDetails()) to determine which offers a user is eligible for. |
   | BillingClient.SkuType | [BillingClient.ProductType](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.ProductType). The INAPP and SUBS product type constants remain functionally similar to the deprecated SKU type constants. |
   | SkuDetails | [ProductDetails](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails). This is the new data model that supports the one-time products. |
   | SkuDetailsParams | Use [QueryProductDetailsParams](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams) with [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)). |
   | SkuDetailsResponseListener | Use [ProductDetailsResponseListener](https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener) with [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)). |
   | QueryPurchaseHistoryParams | - Use [queryPurchasesAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)) for active or pending purchases. - Track consumed purchases on your backend servers. - Use the server-side [Voided Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases) for canceled or voided purchases. |
   | getSkuDetailsList and setSkuDetailsList | Use [BillingFlowParams.Builder.setProductDetailsParamsList](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)) |
   | querySkuDetailsAsync | [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) |
   | enablePendingPurchases() (API without parameters) | [enablePendingPurchases(PendingPurchasesParams params)](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases(com.android.billingclient.api.PendingPurchasesParams)) Note that the deprecated enablePendingPurchases() is functionally equivalent to `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`. |
   | queryPurchasesAsync(String skuType, PurchasesResponseListener listener) | [queryPurchasesAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)) |

   <br />

   ### Upgrade from


   The following table lists the APIs that are removed in PBL 9, and the
   corresponding alternate APIs that you must use in your app.

   | Previously deprecated API removed | Alternate API to use |
   |---|---|
   | BillingClient.SkuType | [BillingClient.ProductType](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.ProductType). The INAPP and SUBS product type constants remain functionally similar to the deprecated SKU type constants. |
   | SkuDetails | [ProductDetails](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails). This is the new data model that supports the one-time products. |
   | SkuDetailsParams | Use [QueryProductDetailsParams](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams) with [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)). |
   | SkuDetailsResponseListener | Use [ProductDetailsResponseListener](https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener) with [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)). |
   | QueryPurchaseHistoryParams | - Use [queryProductDetailsAsync](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) for active or pending purchases. - Track consumed purchases on your backend servers. - Use the server-side [Voided Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases) for canceled or voided purchases. |
   | getSkuDetailsList and setSkuDetailsList | Use [BillingFlowParams.Builder.setProductDetailsParamsList](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)) |

   <br />

4. (Recommended) Enable automatic service reconnection.

   The Play Billing Library can attempt to automatically re-establish the
   service connection if an API call is made while the service is
   disconnected. For more information,
   see [Enable automatic service reconnection](https://developer.android.com/google/play/billing/integrate#automatic-service-reconnection).
5. Handle new sub-response codes.

   The [BillingResult](https://developer.android.com/reference/com/android/billingclient/api/BillingResult) returned from [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) will now
   include a sub-response code field. This field will only be populated in some
   cases to provide a more specific reason for the failure. The sub-response
   field can have the following values:
   - `PAYMENT_DECLINED_DUE_TO_INSUFFICIENT_FUNDS` - Returned when the user's funds are less than the price of the item they are attempting to purchase.
   - `USER_INELIGIBLE` - Returned when the user doesn't meet the configured eligibility requirements for a subscription offer.
   - `NO_APPLICABLE_SUB_RESPONSE_CODE` - The default value, returned when no other sub-response code is applicable.

   **Migration step** : Update your `PurchasesUpdatedListener` or equivalent result handling to recognize and respond to these specific sub-response
   codes to provide a better user experience. For example, prompting to fix payment methods or showing a specific error message.
6. Error-code reclassification awareness.

   For instances where the Play Store app is blocked by the system
   (for example, in OEM-customized kids mode), the response code from PBL has
   changed from `ERROR` to `BILLING_UNAVAILABLE`.

   **Migration step**: Ensure your error handling logic accommodates this
   change and doesn't rely on receiving a generic error in these
   specific scenarios.

   > [!NOTE]
   > **Note:** For this feature to work, you need [AndroidX.core library](https://developer.android.com/jetpack/androidx/releases/core#core_and_core-ktx_version_190_2) version 1.9 or later.

7. Handle [`DeveloperProvidedBillingDetails.getLinkUri()`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()) nullability.

   If you use `DeveloperProvidedBillingDetails` as part of an external payments
   integration, `getLinkUri()` is now `@Nullable`.

   **Migration step** : To handle this change safely, ensure your
   integration code handles both `null` and empty string (`""`) values from the
   [`DeveloperProvidedBillingDetails.getLinkUri()`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()) method before parsing
   or launching browser intents. For example:

   ### Kotlin

       val linkUri = details.getLinkUri()
       if (!linkUri.isNullOrEmpty()) {
         val intent = Intent(Intent.ACTION_VIEW, Uri.parse(linkUri))
         context.startActivity(intent)
       }

   ### Java

       String linkUri = details.getLinkUri();
       if (!android.text.TextUtils.isEmpty(linkUri)) {
         Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(linkUri));
         context.startActivity(intent);
       }

8. Optional changes.

   - Support pending purchases for prepaid plans. For more information, see
     [Handle Subscriptions and Pending Transactions](https://developer.android.com/google/play/billing/subscriptions#pending).

   - Virtual installment subscriptions. For more information, see
     [Installment Subscriptions Integration](https://developer.android.com/google/play/billing/subscriptions#installments).