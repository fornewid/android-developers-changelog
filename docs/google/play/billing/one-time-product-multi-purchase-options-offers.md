---
title: https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers
url: https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers
source: md.txt
---

This document details the integration of your one-time products (OTPs) with the
Play Billing Library. It further explains how to integrate various purchase
options and offers related to your one-time products.

You can configure multiple purchase options and offers for your one-time
products. For example, you can configure a buy purchase option and a pre-order
offer for the same one-time product.

### Prerequisites

To configure multiple offers for one-time products, you must use the
[`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)) API. The deprecated `querySkuDetailsAsync()`
API isn't supported. For information on how to use
[`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)) and the version of [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams))
that takes [`ProductDetailsParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams) as input, see [migration steps](https://developer.android.com/google/play/billing/migrate-gpblv6#steps).

### Query the product details

If you have configured multiple offers or purchase options for your one-time
product, the [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) object returned by the
[`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)) method can have more than one available buy
and (or) rent purchase option per one-time product. To get the list of all the
eligible offers for each [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) object, use the
`getOneTimePurchaseOfferDetailsList()` method. Only offers and purchase options
for which the user is eligible will be returned as part of this list. Your code
in the [`onProductDetailsResponse()`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener#onProductDetailsResponse(com.android.billingclient.api.ProdctDetails.ProductDetailsResult)) method should handle the returned
offers.
| **Note:** If you continue to call the `getOneTimePurchaseOfferDetails()` method instead of the new `getOneTimePurchaseOfferDetailsList()` method, the backwards compatible purchase option offer is returned instead of all the eligible offers. By default, the first created buy purchase option is considered as backward compatible. However, if a backward compatible offer isn't available, the `QueryProductDetailsResult` will have an `UnfetchedProduct` object that has original requested product ID, product type, and the status code as `NO_ELIGIBLE_OFFER`.

## Launch the billing flow

To start a purchase request from your app, call the [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow)
method from your app's main thread. This method takes a reference to a
[`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object that contains the relevant [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails)
object obtained from calling [`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)). To create a
[`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object, use the [`BillingFlowParams.Builder`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder)
class. Note that you must set the offer token corresponding to the offer
selected by the user when creating the [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object.

The following sample shows how to launch the purchase flow for a one-time
product with multiple offers:

<br />

#### Java

```java
    
// An activity reference from which the billing flow will launch.
Activity activity = ...;
ImmutableList<ProductDetailsParams> productDetailsParamsList =
    ImmutableList.of(
        ProductDetailsParams.newBuilder()
             // retrieve a value for productDetails by calling queryProductDetailsAsync()
            .setProductDetails(productDetails)
            // to get an offer token, call
            // ProductDetails.getOneTimePurchaseOfferDetailsList() for a list of offers
            // that are available to the user
            .setOfferToken(selectedOfferToken)
            .build()
    );
BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build();
// Launch the billing flow
BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
    
    
```

<br />

The `offerToken` can be found as part of the `OneTimePurchaseOfferDetails`. When
you show the offer to the user, make sure you configure the billing flow
parameters with the correct offer token which you can get from the
`oneTimePurchaseOfferDetails.getOfferToken()` method.

## Purchase options and offers

A purchase option lets you define how the entitlement is granted to a user, its
price, and in which region the product is available. A single product can have
multiple purchase options, which can represent where and how you sell your
product.

Google Play supports the following purchase options for one-time products:

- Buy purchase option
- Rent purchase option

Offers refer to a pricing scheme that you can create for your one-time products.
For example, you can create a discount offer for your one-time product.

Google Play supports the following purchase offers for one-time products:

- Pre-order offer (supported only for the buy purchase option)
- Discount offer (supported for both buy and rent purchase options)

### Buy purchase option

A buy purchase option represents a standard, outright purchase of the one-time
product. It has an optional legacyCompatible field, indicating whether this
purchase option will be available in older Play Billing Library (version 7 or
older) flows that don't support the new model. For backwards compatibility, at
least one buy purchase option should be marked as legacy compatible.

The steps for integrating both the buy and the rent purchase options with PBL
are the same. To understand how to integrate the buy purchase option with PBL,
see [Integrate rent purchase option with PBL](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#integrate-pbl).

### Rent purchase option

The rent purchase option lets users access the one-time products for a specified
time duration. You can specify the rental period and it's expiration. This
document describes the steps to integrate the rent purchase option with the Play
Billing Library (PBL).
| **Note:** You must grant user entitlement for your one-time products available on rent. For more information, see [Grant entitlement to the user](https://developer.android.com/google/play/billing/integrate#granting-entitlement).

#### Integrate rent purchase option with PBL

This section describes how to integrate the rent purchase option with the Play
Billing Library (PBL). It assumes that you are familiar with the initial PBL
integration steps such as, [adding the PBL dependency to your app](https://developer.android.com/google/play/billing/integrate#dependency),
initializing the [BillingClient](https://developer.android.com/google/play/billing/integrate#initialize), and [connecting to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play). This
section focuses on the PBL integration aspects that are specific to the rent
purchase option.

To configure products available for rent, you will need to use the new
`monetization.onetimeproducts` service of the Play Developer API or the Play
Developer Console UI. To use the service, you can call the REST API directly, or
use the [Java client library](https://developer.android.com/reference/com/android/billingclient/api/BillingClient).

#### Launch a purchase flow for the rent option

To launch a purchase flow for a rental offer, do the following steps:

1. Fetch the rent purchase option metadata by using the
   [`ProductDetails.oneTimePurchaseOfferDetails.getRentalDetails()`]() method.

   The following sample shows how to get the rent purchase metadata:  

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
       for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
         for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
             productDetails.getOneTimePurchaseOfferDetailsList()) {
           // Checks if the offer is a rent purchase option.
           if (oneTimePurchaseOfferDetails.getRentalDetails() != null) {
             // process the returned RentalDetails
             OneTimePurchaseOfferDetails.RentalDetails rentalDetails =
                 oneTimePurchaseOfferDetails.getRentalDetails();
             // Get rental period in ISO 8601 format.
             String rentalPeriod = rentalDetails.getRentalPeriod();
             // Get rental expiration period in ISO 8601 format, if present.
             if (rentalDetails.getRentalExpirationPeriod() != null) {
               String rentalExpirationPeriod = rentalDetails.getRentalExpirationPeriod();
             }
             // Get offer token
               String offerToken = oneTimePurchaseOfferDetails.getOfferToken();
             // Get the associated purchase option ID
             if (oneTimePurchaseOfferDetails.getPurchaseOptionId() != null) {
               String purchaseOptionId = oneTimePurchaseOfferDetails.getPurchaseOptionId();
             }
           }
         }
       }
     }
   });
   ```
2. Launch the billing flow.

   To start a purchase request from your app, call the
   [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow) method from your app's main thread. This method
   takes a reference to a [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object that contains the
   relevant [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) object obtained from calling
   [`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)). To create a [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams)
   object, use the `BillingFlowParams.Builder` class. Note that you must set
   the offer token corresponding to the offer selected by the user when
   creating the [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object. If a user is eligible for the
   rent purchase option, they will receive an offer with RentalDetails and
   offerId in [`queryProductDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)).

   The following sample shows how to launch the billing flow:


   ### Kotlin

   ```kotlin
   // An activity reference from which the billing flow will be launched.
   val activity : Activity = ...;

   val productDetailsParamsList = listOf(
       BillingFlowParams.ProductDetailsParams.newBuilder()
           // retrieve a value for productDetails by calling queryProductDetailsAsync()
           .setProductDetails(productDetails)
           // Get the offer token:
           // a. For one-time products, call ProductDetails.getOneTimePurchaseOfferDetailsList()
           // for a list of offers that are available to the user.
           // b. For subscriptions, call ProductDetails.subscriptionOfferDetails()
           // for a list of offers that are available to the user.
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
               // Get the offer token:
               // a. For one-time products, call ProductDetails.getOneTimePurchaseOfferDetailsList()
               // for a list of offers that are available to the user.
               // b. For subscriptions, call ProductDetails.subscriptionOfferDetails()
               // for a list of offers that are available to the user.
               .setOfferToken(selectedOfferToken)
               .build()
       );

   BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
       .setProductDetailsParamsList(productDetailsParamsList)
       .build();

   // Launch the billing flow
   BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
   ```

   <br />

   The `offerToken` can be found as part of the `OneTimePurchaseOfferDetails`.
   When you show the offer to the user, make sure you configure the billing
   flow parameters with the correct offer token which you can get from the
   `oneTimePurchaseOfferDetails.getOfferToken()` method.

### Pre-order offer


| **EAP:** This product or feature is in the Early Access Program (EAP). Products and features in EAP are available "as is" and might have limited support. To access the EAP feature submit a request using the [One-time products EAP Interest Form](https://docs.google.com/forms/d/e/1FAIpQLSfBsxfQg4a8uC7Ct9O4ssn121KE6l8TC4qh3ZvA5tJpFLycqw/viewform?usp=dialog).

<br />

Pre-order lets you set up one-time products to be bought before the item is
released. When a user pre-orders your product, they agree to pay for the item
when the product is released, unless the user cancels the pre-order before the
release date. On the release date, a buyer is charged and Play will notify them
by email that the item is released.

This document describes the steps to integrate the pre-order purchase offer with
the Play Billing Library (PBL).

#### Integrate pre-order offer with PBL

This section describes how to integrate the pre-order offer with the Play
Billing Library (PBL). It assumes that you are familiar with the initial PBL
integration steps such as, [adding the PBL dependency to your app](https://developer.android.com/google/play/billing/integrate#dependency),
initializing the [BillingClient](https://developer.android.com/google/play/billing/integrate#initialize), and [connecting to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play). This
section focuses on the PBL integration aspects that are specific to the
pre-order offer.

#### Launch a purchase flow for a pre-order offer

To launch a purchase flow for a pre-order offer, do the following steps:

1. Fetch the pre-order offer metadata by using the
   [`ProductDetails.oneTimePurchaseOfferDetails.getPreorderDetails()`]()
   method. The following sample shows how to get the pre-order offer metadata:

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
       for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
         for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
             productDetails.getOneTimePurchaseOfferDetailsList()) {
           // Checks if the offer is a preorder offer.
           if (oneTimePurchaseOfferDetails.getPreorderDetails() != null) {
             // process the returned PreorderDetails
             OneTimePurchaseOfferDetails.PreorderDetails preorderDetails =
                 oneTimePurchaseOfferDetails.getPreorderDetails();
             // Get preorder release time in millis.
             long preorderReleaseTimeMillis = preorderDetails.getPreorderReleaseTimeMillis();
             // Get preorder presale end time in millis.
             long preorderPresaleEndTimeMillis = preorderDetails.getPreorderPresaleEndTimeMillis();
             // Get offer ID
               String offerId = oneTimePurchaseOfferDetails.getOfferId();
             // Get the associated purchase option ID
             if (oneTimePurchaseOfferDetails.getPurchaseOptionId() != null) {
               String purchaseOptionId = oneTimePurchaseOfferDetails.getPurchaseOptionId();
             }
           }
         }
       }
     }
   });
   ```

   <br />

2. Launch the billing flow.

   To start a purchase request from your app, call the `launchBillingFlow()`
   method from your app's main thread. This method takes a reference to a
   [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object that contains the relevant
   [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) object obtained from calling
   queryProductDetailsAsync(). To create a [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object, use
   the `BillingFlowParams.Builder class`. Note that you must set the offer
   token corresponding to the offer selected by the user when creating the
   [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) object. If a user is eligible for the pre-order
   offer, they will receive an offer with PreorderDetails and offerId in the
   `queryProductDetailsAsync()` method.

   The following sample shows how to launch the billing flow:  

   #### Java

   ```java
   // An activity reference from which the billing flow will launch.
   Activity activity = ...;
   ImmutableList productDetailsParamsList =
       ImmutableList.of(
       ProductDetailsParams.newBuilder()
            // retrieve a value for productDetails by calling queryProductDetailsAsync()
           .setProductDetails(productDetails)
           // to get an offer token, call
           // ProductDetails.getOneTimePurchaseOfferDetailsList() for a list of offers
           // that are available to the user
           .setOfferToken(selectedOfferToken)
           .build()
   );
   BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
   .setProductDetailsParamsList(productDetailsParamsList)
   .build();
   // Launch the billing flow
   BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
   ```

   <br />

   The `offerToken` can be found as part of the `OneTimePurchaseOfferDetails`.
   When you show the offer to the user, make sure you configure the billing
   flow parameters with the correct offer token which you can get from the
   `oneTimePurchaseOfferDetails.getOfferToken()` method.

### Discount offer

This section describes how you can configure discount offers for your one-time
products.

There are four different parameters you can configure in a one-time product
discount offer:

- Discounted offer price: Specifies details about either the percentage
  discounted off or absolute price off the original price.

- Countries or Regions eligibility: Specifies the availability of one-time
  product offers in a country or a region.

- Purchase limit (optional): Lets you to determine how many times a user can
  redeem the same offer. If a user exceeds the purchase limit, the user will
  be ineligible for the offer.

- Limited time (optional): Specifies the time period in which the offer is
  available. Outside of the time period, the offer is ineligible for purchase.

#### Retrieve discounted offer price information

For a discounted offer, you can retrieve the percentage of discount or the
absolute discount offered.

##### Example 1: Retrieve discounted offer's percentage discount

The following sample shows how to get the discounted offer's original full price
and its percentage discount. Note that the percentage discount information is
only returned for discounted offers.  

#### Java

```java
billingClient.queryProductDetailsAsync(
    queryProductDetailsParams,
    new ProductDetailsResponseListener() {
      public void onProductDetailsResponse(
          BillingResult billingResult, QueryProductDetailsResult productDetailsResult){
        // check billingResult
        // ...
        // process productDetailsList returned by QueryProductDetailsResult
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            long discountedOfferPriceMicros =
                oneTimePurchaseOfferDetails.getPriceAmountMicros();
            // process the returned fullPriceMicros and percentageDiscount.
            if (oneTimePurchaseOfferDetails.getFullPriceMicros() != null) {
              long fullPriceMicros = oneTimePurchaseOfferDetails.getFullPriceMicros();
            }
            if (oneTimePurchaseOfferDetails.getDiscountDisplayInfo() != null) {
              long percentageDiscount =
                  oneTimePurchaseOfferDetails
                      .getDiscountDisplayInfo()
                      .getPercentageDiscount();
            }
            // ...
          }
        }
      }
    });
    
```

##### Example 2: Retrieve discounted offer's absolute discount

The following example shows how to get the discounted offer's original full
price and its absolute discount in micros. Note that the absolute discount in
micros information is only returned for discounted offers. Either the absolute
discount or percentage discount must be specified for a discount offer.  

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
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            long discountedOfferPriceMicros =
                oneTimePurchaseOfferDetails.getPriceAmountMicros();
            // process the returned fullPriceMicros and absolute DiscountAmountMicros.
            if (oneTimePurchaseOfferDetails.getFullPriceMicros() != null) {
              long fullPriceMicros = oneTimePurchaseOfferDetails.getFullPriceMicros();
            }
            if (oneTimePurchaseOfferDetails.getDiscountDisplayInfo() != null) {
              long discountAmountMicros =
                  oneTimePurchaseOfferDetails
                      .getDiscountDisplayInfo()
                      .getDiscountAmount()
                      .getDiscountAmountMicros();
            }
            // ...
          }
        }
      }
    });
    
```

## Get the valid time window of an offer

You can use `OneTimePurchaseOfferDetails.getValidTimeWindow()` method to get the
valid time window for an offer. This object contains the time window start and
end time in milliseconds.

The following sample shows how to get the valid time window of an offer:

<br />

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
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            if (oneTimePurchaseOfferDetails.getValidTimeWindow() != null) {
              // process the returned startTimeMillis and endTimeMillis.
              ValidTimeWindow validTimeWindow =
                  oneTimePurchaseOfferDetails.getValidTimeWindow();
              long startTimeMillis = validTimeWindow.getStartTimeMillis();
              long endTimeMillis = validTimeWindow.getEndTimeMillis();
              // ...
            }
          }
        }
      }
    });
    
```

<br />

## Limited quantity at the discount offer level

You can specify the maximum quantity limit at the discount offer level, that is
applied only at the offer level. Here is an example to illustrate:

1. Super screensavers has 2 offers for the screensaver product: purchase option screensaver and discount screensaver.
   1. The purchase option screensaver doesn't have a limited quantity set up.
   2. The discount screensaver has the offer level maximum allowed quantity set to 3.
2. The screensaver product does not have product level maximum allowed quantity, so users can buy unlimited quantities of this product.
3. The user owns 1 discount screensaver, and they plan to buy another one with the discount screensaver.
4. When retrieving the available offers, the LimitedQuantityInfo for the purchase option screensaver is null and the remaining quantity value for the discount screensaver is 2.

The following sample shows how to get the limited quantity at the discount offer
level:

<br />

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
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            if (oneTimePurchaseOfferDetails.getLimitedQuantityInfo() != null) {
              // process the returned maximumQuantity and remainingQuantity.
              LimitedQuantityInfo limitedQuantityInfo =
                  oneTimePurchaseOfferDetails.getLimitedQuantityInfo();
              int maximumQuantity = limitedQuantityInfo.getMaximumQuantity();
              int remainingQuantity = limitedQuantityInfo.getRemainingQuantity();
              // ...
            }
          }
        }
      }
    });
    
```

<br />

When users use up the maximum quantity redemptions for an offer, the offer isn't
returned by the `getOneTimePurchaseOfferDetailsList()` method.

### Calculate redemption limit

The following example shows how to get the limited quantity information on a
certain discount offer. You can get the maximum allowed quantity and the
remaining quantity for the current user. Note that limited quantity feature is
applicable for both the consumable and non-consumable one-time product offers.
This feature is supported only at the offer level.

Google Play calculates the remaining quantity by subtracting the user's owned
quantity from the maximum allowed quantity you have set up. When counting the
user's owned quantity, Google Play considers consumed purchases or pending
purchases. Purchases that were canceled, refunded or charged-back don't count
towards the user's owned quantity. For example:

1. Super screensavers set up a discount offer with the maximum allowed quantity
   of one, so users can buy up to one discounted screensaver.

2. The user buys one of the discounted screensaver. If the user then tries to
   buy the second discounted screensaver, it will error out and the
   `PurchasesUpdatedListener` will get an ITEM_UNAVAILABLE response code.

3. The user asks for a refund of the originally purchased discounted
   screensaver, and successfully receives the refund. The user tries to buy one
   of the discounted screensaver, and the purchase will succeed.

## Country and region eligibility

You can choose the countries or regions where purchase option offer or discount
offer will be available to users. Google Play will evaluate user eligibility
based on Play country. When you configure regional availability for an offer, it
will only be returned as part of `getOneTimePurchaseOfferDetailsList()` if the
user is in a targeted country or region, otherwise it won't be part of the list
of offers returned when you call `queryProductDetailsAsync()`.
| **Note:** Country or regional eligibility for a user may change between you displaying the eligible products for them and launching the purchase flow in some rare cases. For example, the user could change their country. Such a change may make the previously returned offer ineligible in the user's new country or region. Google Play will double check the user's country eligibility when the billing flow is launched to make sure country eligibility is enforced. If the user is not eligible, the `PurchasesUpdatedListener` will get an `ITEM_UNAVAILABLE` response code.

## Offer tags

The following sample shows how to retrieve the offer tags associated with an
offer.

<br />

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
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            // process the returned offer tags.
            ImmutableList<String> offerTags =
                oneTimePurchaseOfferDetails.getOfferTagsList();
            // ...
          }
        }
      }
    });
    
    
```

<br />

### Inheritance of offer tags

You can set offer tags for either product, purchase option or discount offer.
Discount offers inherit the offer tags from its purchase option offer.
Similarly, if offer tags are specified at product level, both purchase option
offer and discount offers inherit the product offer tags.

For example, Super screensavers has two offers for the screensaver product;
purchase option screensaver and a discount screensaver.

- Super screensaver has the product offer tag `SSProductTag`.
- The purchase option screensaver has the offer tag `SSPurchaseOptionTag`.
- The discount screensaver has the offer tag `SSDiscountOfferTag`.

In this example, the `oneTimePurchaseOfferDetails.getOfferTagsList()` method for
the purchase option offer returns `SSProductTag` and `SSPurchaseOptionTag`. For
the discount offer, the method returns `SSProductTag`, `SSPurchaseOptionTag`,
and `SSDiscountOfferTag`.