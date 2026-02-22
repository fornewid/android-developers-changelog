---
title: https://developer.android.com/google/play/billing/migrate-gpblv6
url: https://developer.android.com/google/play/billing/migrate-gpblv6
source: md.txt
---

# Migrate to Google Play Billing Library 6 from versions 4 or 5

This topic describes how to migrate from Google Play Billing Library 4 or 5 to Google Play Billing Library 6 and how to use new subscription capabilities.

For a full list of the changes in version 6.0.0, refer to the[release notes](https://developer.android.com/google/play/billing/release-notes).

## Overview

Google Play Billing Library 6 builds on the new subscription features introduced in version 5 and adds a few more improvements. These features allow you to sell subscriptions in more ways, reducing operational costs by eliminating the need to create and manage an ever-increasing number of SKUs.

For more information about the new features introduced with Play Billing Library 5, see[Recent changes to subscriptions in Play Console](https://support.google.com/googleplay/android-developer/answer/12124625).

## Backward-compatible Play Billing Library upgrade

All existing subscription products were automatically converted to this new paradigm as part of the May 2022 release of Play Billing Library 5 and the new subscriptions platform. This means that you don't have to make any subscription product configuration changes to have a catalog that is compatible with the new versions of the Play Billing Library. For more information on how subscription SKUs were converted into backward-compatible subscriptions, see the*Working with older subscriptions* section in the[Play Console Help article](https://support.google.com/googleplay/android-developer/answer/12124625).

### Older versions of your app still work

If you have a backward-compatible subscription catalog, all existing versions of your app should still work as intended for those products. One-time product purchases should also continue working without issues in older versions.

Versions of your app using deprecated methods (for example,[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))) won't be able to sell any base plans or offers that are not backward compatible. You can read about backward-compatible offers in the relevant[Play Console Help Center article](https://support.google.com/googleplay/android-developer/answer/12124625).

### Upgrade to Play Billing Library 5 or 6

Play Billing Library 5 and 6 include the deprecated methods`querySkuDetailsAsync`and`BillingFlowParams.Builder.setSkuDetails`that takes[`SkuDetails`](https://developer.android.com/reference/com/android/billingclient/api/SkuDetails)as a billing flow parameter. This means that you can gradually move to Play Billing Library 6 by planning different stages of migration.

As a first step to migration, you can just[update the library version](https://developer.android.com/google/play/billing/migrate-gpblv6#update-google), leave your catalog and backend as they are, and test your app while it still uses the deprecated methods. If you are not using`queryPurchases`,`launchPriceChangeFlow`, or`setVrPurchaseFlow`, it should still work as intended. Afterwards, you can iterate to fully adopt the[new subscription features released in May 2022](https://developer.android.com/google/play/billing/compatibility).

If you have previously adopted these features with a Google Play Billing Library 5 migration, you can proceed directly to the sections labeled[Update Google Play Billing Library](https://developer.android.com/google/play/billing/migrate-gpblv6#update-google)and[Change a user's subscription purchases](https://developer.android.com/google/play/billing/migrate-gpblv6#change-user-purchases). If you are starting from an earlier version or didn't fully adopt the new features yet, you can read the[full migration steps](https://developer.android.com/google/play/billing/migrate-gpblv6#steps)that follow to learn how to adopt them.

## Full migration steps

### Create new subscriptions in your backend product catalog

Using the Play Developer Console or the Play Developer API, you can now configure a single subscription with multiple base plans, each with multiple offers. Subscription offers have flexible pricing models and eligibility options. You can create offers across the subscription lifecycle using a variety of auto-renewing and prepaid plans.

We recommend creating new products following the entity structure in the new subscription platform for your Play Billing Library 6 integration before migrating your app. You can consolidate duplicate products in your old catalog representing the same entitlement benefits under a single subscription and use base plan and offer configurations to represent all the options that you want to offer. For more information about this recommendation, see the*Working with older subscriptions* section of the[Play Console Help article](https://support.google.com/googleplay/android-developer/answer/12124625).

We recommend that you don't modify the converted subscription products after the May 2022 release; you should leave them as they are to be sold with the versions of your app using deprecated methods (for example,[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))) without introducing changes that could affect these older builds.

The conversion process made the subscription products that were in your catalog before May 2022 read-only to avoid accidental changes that could result in issues with your existing integration. Making changes to these subscriptions is possible, but there would be implications that could affect your frontend and backend integrations:

- On the frontend, app versions using[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))to obtain subscription product details can only sell backward-compatible base plans and offers, and there can only be one backward-compatible base plan and offer combination, so if you add new plans or offers to the converted subscriptions, the new additional base plans or offers won't be able to be sold on these older versions of your app.

- On the backend, if you edit your converted subscriptions in the Play Console UI, you won't be able to manage them with the[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)endpoint, if you were calling the endpoint for this purpose. You should also migrate to the new subscription purchase status endpoint ([`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)) to manage purchases for these subscriptions, as the old purchase status endpoint ([`purchases.subscriptions.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get)) only returns the data necessary to handle backward-compatible base plans and offers purchases. Read the[Manage subscription purchase status section](https://developer.android.com/google/play/billing/migrate-gpblv6#manage-subscription-status)for more information.

### Manage your backend subscription catalog with the new API

If you manage your subscription product catalog automatically with the Google Play Developer API, you need to use the new subscription product definition endpoints to create and manage subscriptions, base plans, and offers. Read the[May 2022 subscription features guide](https://developer.android.com/google/play/billing/compatibility#managing-subscriptions)to learn more about the product catalog API changes for this release.

To migrate an automatic product catalog management module for Google Play Billing subscriptions, replace the[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)API with the new Subscription Publishing API to manage and publish your subscription catalog. There are three new endpoints:

- [`Monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)to manage subscription products.
- [`Monetization.basePlans`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans)to manage base plans for subscriptions.
- [`Monetization.offers`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers)to manage offers for base plans.

These new endpoints have all the necessary functionality to leverage all the new capabilities in your catalog: base plan and offer tags, regional targeting, prepaid plans, and more.

You should still use the[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)API to manage your in-app product catalog for one-time purchase products.
| **Note:** The[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)API for product management will continue to return subscription product details as before for converted subscriptions if you haven't made them editable in the Play Console. Once you start editing your subscriptions in the Console, the[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)API can no longer be used for subscriptions.

Versions of your app using deprecated methods (for example,[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))) won't be able to sell any base plans or offers that are not backward compatible. You can read about backward-compatible offers[here](https://support.google.com/googleplay/android-developer/answer/12124625).

### Update Google Play Billing Library

Once you have created your new subscription products catalog, you can migrate your app to Google Billing Library 5. Replace the existing Play Billing Library dependency with the updated version to your app's`build.gradle`file.  

    dependencies {
        def billingVersion = "6.0.0"

        implementation "com.android.billingclient:billing:$billingVersion"
    }

Your project should build right away, even if you haven't modified any calls to methods---Play Billing Library 6 is backward compatible. The concept of a SKU is considered deprecated, but still present to make porting apps a simpler, more incremental process.
| **Note:** If you are migrating from Play Billing Library 5, you can skip to the[Change a user's subscription purchases](https://developer.android.com/google/play/billing/migrate-gpblv6#change-user-purchases)section.

### Initialize the Billing Client and establish a connection to Google Play

The first steps to launch purchases from an Android app remain the same:

- [Initialize the Billing Client](https://developer.android.com/google/play/billing/integrate#initialize)
- [Establish a connection to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play)

### Show products available to buy

To obtain all offers a user is eligible to purchase:

- Replace`SkuDetailsParams`with`QueryProductDetailsParams`
- Switch the`BillingClient.querySkuDetailsAsync()`call to use`BillingClient.queryProductDetailsAsync()`

Note that query results are now`ProductDetails`instead of`SkuDetails`. Each`ProductDetails`item contains the information about the product (ID, title, type, and so on). For subscription products,`ProductDetails`contains a`List<ProductDetails.SubscriptionOfferDetails>`, which is the list of the subscription offer details. For one-time purchase products,`ProductDetails`contains a`ProductDetails.OneTimePurchaseOfferDetails`. These can be used to decide which offers to show to the users.

The following example shows how your app might look before and after making these changes:

**Before**  

### Kotlin

```kotlin
val skuList = ArrayList<String>()

skuList.add("up_basic_sub")

val params = SkuDetailsParams.newBuilder()

params.setSkusList(skuList).setType(BillingClient.SkuType.SUBS).build()

billingClient.querySkuDetailsAsync(params) {
    billingResult,
    skuDetailsList ->
    // Process the result
}
```

### Java

```java
List<String> skuList = new ArrayList<>();

skuList.add("up_basic_sub");

SkuDetailsParams.Builder params = SkuDetailsParams.newBuilder();

params.setSkusList(skuList).setType(SkuType.SUBS).build();

billingClient.querySkuDetailsAsync(params,
    new SkuDetailsResponseListener() {
        @Override
        public void onSkuDetailsResponse(BillingResult billingResult,
                List<SkuDetails> skuDetailsList) {
            // Process the result.
        }
    }
);
```

**After**  

### Kotlin

```kotlin
val productList =
    listOf(
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("up_basic_sub")
            .setProductType(BillingClient.ProductType.SUBS)
            .build()
    )

val params = QueryProductDetailsParams.newBuilder().setProductList(productList).build()

billingClient.queryProductDetailsAsync(params) {
    billingResult,
    productDetailsList ->
    // Process the result
}
```

### Java

```java
ImmutableList<Product> productList = ImmutableList.of(Product.newBuilder()
                                            .setProductId("up_basic_sub")
                                            .setProductType(ProductType.SUBS)
                                            .build());

QueryProductDetailsParams params = QueryProductDetailsParams.newBuilder()
    .setProductList(productList)
    .build();

billingClient.queryProductDetailsAsync(
        params,
        new ProductDetailsResponseListener() {
                public void onProductDetailsResponse(BillingResult billingResult, List<ProductDetails> productDetailsList) {
                    // Process the result
                }
        }
);
```

The callback for`queryProductDetailsAsync`returns a`List<ProductDetails>`. Each`ProductDetails`item contains the information about the product (ID, title, type, and so on). The main difference is that subscription products now also contain a`List<ProductDetails.SubscriptionOfferDetails>`that contains all offers available to the user.

Since previous versions of the Play Billing Library do not support the new objects (subscriptions, base plans, offers, and so on), the new system translates each subscription SKU into a single backward-compatible base plan and offer. Available one-time purchase products are also ported to a`ProductDetails`object. The offer details of a one-time purchase product can be accessed with the`getOneTimePurchaseOfferDetails()`method.

Rarely, some devices are unable to support`ProductDetails`and`queryProductDetailsAsync()`, usually due to outdated versions of[Google Play Services](https://support.google.com/googleplay/answer/9037938). To ensure proper support for this scenario, call[`isFeatureSupported()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isFeatureSupported(java.lang.String))for the[`PRODUCT_DETAILS`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.FeatureType#PRODUCT_DETAILS)feature before calling`queryProductDetailsAsync`. If the response is[`OK`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK), the device supports the feature and you can proceed with calling`queryProductDetailsAsync()`. If the response is[`FEATURE_NOT_SUPPORTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED), you can instead request the available backward-compatible products list with[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)). To learn more about how to use the backward compatibility features, see the[May 2022 subscription features guide](https://developer.android.com/google/play/billing/compatibility#play_billing_library_changes).

### Launch the offer purchase flow

Launching a purchase flow for an offer is very similar to launching a flow for a SKU. To start a purchase request using version 6, do the following:

- Instead of using`SkuDetails`for`BillingFlowParams`, use`ProductDetailsParams`.
- The offer(s) details, such as offer ID, base plan ID, and more can be obtained using the`SubscriptionOfferDetails`object.

To purchase a product with the user's selected offer, get the`offerToken`of the selected offer and pass it into the`ProductDetailsParams`object.

Once you've created a`BillingFlowParams`object, launching the billing flow with the`BillingClient`remains the same.

The following example shows how your app might look before and after making these changes:

**Before**  

### Kotlin

```kotlin
// An activity reference from which the billing flow will be launched.
val activity : Activity = ...
// Retrieve a value for "skuDetails" by calling querySkuDetailsAsync().
val billingFlowParams = BillingFlowParams.newBuilder()
                            .setSkuDetails(skuDetails)
                            .build()

val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

### Java

```java
// An activity reference from which the billing flow will be launched.
Activity activity = ...;
// Retrieve a value for "skuDetails" by calling querySkuDetailsAsync().
BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
        .setSkuDetails(skuDetails)
        .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

**After**  

### Kotlin

```kotlin
// An activity reference from which the billing flow will be launched.
val activity : Activity = ...;

val productDetailsParamsList = listOf(
    BillingFlowParams.ProductDetailsParams.newBuilder()
        // retrieve a value for "productDetails" by calling queryProductDetailsAsync()
        .setProductDetails(productDetails)
        // For One-time product, "setOfferToken" method shouldn't be called.
        // For subscriptions, to get the offer token corresponding to the selected
        // offer call productDetails.subscriptionOfferDetails?.get(selectedOfferIndex)?.offerToken
        .setOfferToken(selectedOfferToken)
        .build()
)

val billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build()

// Launch the billing flow
val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

### Java

```java
// An activity reference from which the billing flow will be launched.
Activity activity = ...;

ImmutableList<ProductDetailsParams> productDetailsParamsList =
    ImmutableList.of(
        ProductDetailsParams.newBuilder()
             // retrieve a value for "productDetails" by calling queryProductDetailsAsync()
            .setProductDetails(productDetails)
            // For one-time products, "setOfferToken" method shouldn't be called.
            // For subscriptions, to get the offer token corresponding to the selected
            // offer call productDetails.getSubscriptionOfferDetails().get(selectedOfferIndex).getOfferToken()
            .setOfferToken(selectedOfferToken)
            .build()
    );

BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build();

// Launch the billing flow
BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
```

### Process the purchases

Processing purchases with Google Play Billing Library 6 remains similar to previous versions.

To pull all active purchases owned by the user and query for new purchases, do the following:

- Instead of passing a`BillingClient.SkuType`value to`queryPurchasesAsync()`, pass a`QueryPurchasesParams`object that contains a`BillingClient.ProductType`value.

| **Note:** If you're migrating from version 4, note that the previously deprecated`queryPurchases`method has been removed in Play Billing Library 6. Use[`queryPurchasesAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))instead as shown below.

The following example shows how your app might look before and after making these changes:

**Before**  

### Kotlin

```kotlin
billingClient.queryPurchasesAsync(BillingClient.SkuType.SUBS) {
    billingResult,
    purchaseList -> {
        // Process the result
    }
}
```

### Java

```java
billingClient.queryPurchasesAsync(
    BillingClient.SkuType.SUBS,
    new PurchasesResponseListener() {
        public void onQueryPurchasesResponse(
                BillingResult billingResult,
                List<Purchase> purchases) {
            // process the result
        }
    }
);
```

**After**  

### Kotlin

```kotlin
billingClient.queryPurchasesAsync(
    QueryPurchasesParams.newBuilder()
        .setProductType(BillingClient.ProductType.SUBS)
        .build()
) { billingResult, purchaseList ->
    // Process the result
}
```

### Java

```java
billingClient.queryPurchasesAsync(
    QueryPurchasesParams.newBuilder().setProductType(ProductType.SUBS).build(),
    new PurchasesResponseListener() {
        public void onQueryPurchasesResponse(
                BillingResult billingResult,
                List<Purchase> purchases) {
            // Process the result
        }
    }
);
```

The steps to manage[out of app purchases](https://developer.android.com/google/play/billing/integrate#ooap)and[pending transactions](https://developer.android.com/google/play/billing/integrate#pending)haven't changed.

### Manage subscription purchase status with the new API in your backend

You should migrate your subscriptions purchase status management component in your backend to be ready to handle purchases of the new products created in previous steps. Your current subscriptions purchase status management component should work as usual for the converted subscription products you defined before the May 2022 launch, and it should suffice to manage purchases of backward compatible offers, but it doesn't support any of the new functionality.

You need to implement the new[Subscription Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)for your subscriptions purchase status management module, which checks the purchase status and manages Play Billing subscription entitlements in your backend. The[old version](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions)of the API doesn't return all the necessary details to manage purchases in the new platform. For details on changes from previous versions, see the guide to the[May 2022 new subscription features](https://developer.android.com/google/play/billing/compatibility#managing_subscription_status).

You would normally call the[Subscription Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)every time you receive a[`SubscriptionNotification`Real Time Developer Notification](https://developer.android.com/google/play/billing/rtdn-reference#sub)to pull the latest information about the subscription status. You need to replace your calls to[`purchases.subscriptions.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get)with the new version of the Subscription Purchases API,[`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get). There's a new resource called[`SubscriptionPurchaseV2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#resource:-subscriptionpurchasev2)that provides enough information to manage purchase entitlement for subscriptions in the new model.

This new endpoint returns the status for all your subscription products and all your purchases, regardless of the version of the app that sold them and when the product was defined (before or after the May 2022 release), so after the migration you will only need this version of your subscription purchase status management module.

### Change a user's subscription purchases

In Play Billing Library 5 and earlier,[`ProrationMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode)was used to apply changes to a user's subscription purchases, such as upgrades or downgrades. This has been deprecated and replaced with[`ReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode)in version 6.

### Handle subscription price changes

The previously deprecated`launchPriceConfirmationFlow`API has been removed in Play Billing Library 6. For alternatives, see the[price changes guide](https://developer.android.com/google/play/billing/price-changes).

### Handle Play Billing Library errors

In Play Billing Library 6, a new`NETWORK_ERROR`code has been added to indicate problems with the network connection between the user's device and the Google Play system. There were also changes to the codes`SERVICE_TIMEOUT`and`SERVICE_UNAVAILABLE`. For more information, see[Handle BillingResult response codes](https://developer.android.com/google/play/billing/errors).

### Handle pending transactions

Starting with version 6.0.0, the Play Billing Library does not create an order ID for pending purchases. For these purchases, the order ID is populated after the purchase is moved to the[`PURCHASED`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#PURCHASED)state. Make sure that your integration only expects an order ID after a transaction is fully completed. You can still use the purchase token for your records. For more information about handling pending purchases, see the Play Billing Library[integration guide](https://developer.android.com/google/play/billing/integrate)and the[purchase lifecycle management guide](https://developer.android.com/google/play/billing/lifecycle).