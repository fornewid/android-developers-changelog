---
title: https://developer.android.com/google/play/billing/billing_rewarded_products
url: https://developer.android.com/google/play/billing/billing_rewarded_products
source: md.txt
---

| **Warning:** Rewarded products are no longer supported. For more information, see[Create a rewarded product](https://support.google.com/googleplay/android-developer/answer/9155268).

One method of unlocking in-app products and benefits for your users is to create*rewarded products*, or items that users receive after they watch a video advertisement. By providing rewarded products, you allow users to obtain in-app rewards and benefits without them having to make direct purchases.

This document explains how to implement functionality specific to rewarded products. The[workflow diagram](https://developer.android.com/google/play/billing/billing_rewarded_products#workflow-diagram)section of this page illustrates the process.

## Identify your app's rewarded products

Rewarded products have a[`SkuType`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.SkuType)of[`INAPP`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.SkuType#INAPP). To ensure users are able to watch multiple ads and get multiple rewards, the products need to be consumed.

Before you can offer a rewarded product to a user, you must obtain the[`SkuDetails`](https://developer.android.com/reference/com/android/billingclient/api/SkuDetails)for the product. To do this, call[`querySkuDetailsAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryskudetailsasync)with`SkuType.INAPP`as the product type.

## Declare age-appropriate ads

To help facilitate compliance with legal obligations related to children and to underage users, including the[Children's Online Privacy Protection Act (COPPA)](http://business.ftc.gov/privacy-and-security/childrens-privacy)and the[General Data Protection Regulation (GDPR)](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679), your app should declare which ads should be treated as child-directed in the United States and which ads are directed at users who are under[the applicable age of consent in their country](https://support.google.com/accounts/answer/1350409). The AdMob Help Center explains when you should tag your ad requests for[child-directed treatment](https://support.google.com/admob/answer/6219315)and when you should tag them for[under-the-age-of-consent treatment](https://support.google.com/admob/answer/9009425), as well as the effects of doing so.

As you create your app's billing client, consider whether the rewarded ad requests should be treated as child-directed or whether they should be directed at users who are under the age of consent. If the ad requests should have these restrictions in place, call the[`setChildDirected()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#setchilddirected)and[`setUnderAgeOfConsent()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#setunderageofconsent)methods, passing appropriate values into each method.

The following code snippet shows how to declare that video ads should be suitable for children or for users who are under the age of consent:  

### Kotlin

```kotlin
val billingClient = BillingClient.newBuilder(context)
        .setListener(this)
        .setChildDirected(ChildDirected.CHILD_DIRECTED)
        .setUnderAgeOfConsent(UnderAgeOfConsent.UNDER_AGE_OF_CONSENT)
        .build()
```

### Java

```java
BillingClient billingClient =
    BillingClient.newBuilder(context)
        .setListener(this)
        .setChildDirected(ChildDirected.CHILD_DIRECTED)
        .setUnderAgeOfConsent(UnderAgeOfConsent.UNDER_AGE_OF_CONSENT)
        .build();
```
| **Note:** After you've created a billing client, you cannot change the values for`childDirected`and`underAgeOfConsent`. If you need to use different values, such as when the user switches game accounts, disconnect your current billing client, make a new instance of the client, and connect that new instance to the Google Play Billing Library.

## Load video ads

Before showing your user an option to watch a video ad in order to receive a rewarded product, you need to load the video. To do so, create a[`RewardLoadParams`](https://developer.android.com/reference/com/android/billingclient/api/RewardLoadParams)object, associating it with the`SkuDetails`object that represents the rewarded product. Then, call your billing client's[`loadRewardedSku()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#loadrewardedsku)method, passing in the`RewardLoadParams`object and a[`RewardResponseListener`](https://developer.android.com/reference/com/android/billingclient/api/RewardResponseListener)object.
| **Note:** Video ads associated with rewarded products aren't always available for loading. Also, depending on the user's bandwidth, available videos could take some time to load.

The`RewardResponseListener`listener is notified when the video has finished loading. The listener is also notified if the video is unavailable or if another error, such as a server timeout, occurs.

To maintain device performance when loading the videos associated with your app's rewarded products, keep the following best practices in mind:

- Load at most three rewarded product SKUs at a time.
- Attempt to load the videos whenever the user enters your app. This step helps you check whether the videos are still loaded and available.
- When deciding when to load the videos, choose the balance between bandwidth usage and app responsiveness that works best for your use case:

  - At the earliest, load the videos after you call`getSkuDetails()`for the associated rewarded product. Your app remains very responsive, but you might waste network data loading a video that the user never watches.
  - At the latest, load the video when the user navigates to the page where the video is to be displayed. Your app rarely wastes bandwidth in this case, but the user might have to wait a few moments before the button for watching the video becomes clickable.

The following code snippet demonstrates the process for loading a video ad that plays before the user receives the rewarded product:

<br />

### Kotlin

```kotlin
if (skuDetails.isRewarded()) {
    val params = RewardLoadParams.Builder()
            .setSkuDetails(skuDetails)
            .build()
    mBillingClient.loadRewardedSku(params.build(),
            object : RewardResponseListener {
        override fun onRewardResponse(@BillingResponse responseCode : Int) {
            if (responseCode == BillingResponse.OK) {
                // Enable the reward product, or make
                // any necessary updates to the UI.
            }
        }
    })
}
```

### Java

```java
if (skuDetails.isRewarded()) {
    RewardLoadParams.Builder params = RewardLoadParams.newBuilder();
    params.setSkuDetails(skuDetails);
    mBillingClient.loadRewardedSku(params.build(),
        new RewardResponseListener() {
            @Override
            public void onRewardResponse(int responseCode) {
                if (responseCode == BillingResponse.OK) {
                      // Enable the reward product, or make
                      // any necessary updates to the UI.
                  }
            }
        });
}
```

<br />

## Give rewarded purchases to users

If the Google Play Billing Library successfully loads the video associated with a rewarded product---that is, if the`RewardResponseListener`receives a`responseCode`of[`BillingResponse.OK`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponse#OK)---you can launch the billing flow.
| **Caution:** Don't start the billing flow if the`responseCode`isn't`BillingResponse.OK`, which happens if the video ad isn't available. That way, you don't show extra error dialogs, which maintains a good user experience.

You start playing ads for a rewarded product by calling[`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow), as you do for[all other types of in-app products](https://developer.android.com/google/play/billing/billing_library_overview#Enable). Even though the user isn't making a direct purchase to receive a rewarded product, you still need to enable the billing flow so that the user is able to obtain and use the product.

## Consume the purchase

To notify your billing client that a user has received and consumed a rewarded product,[handle the purchase](https://developer.android.com/google/play/billing/billing_library_overview#HandlePurchase)in your billing client listener's[`onPurchasesUpdated()`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated)method. Note that rewarded purchases[need to be consumed](https://developer.android.com/google/play/billing/billing_onetime#indicate_a_one-time_product_has_been_consumed).

## Test your rewarded products

To test how your app loads video ads and provides users with rewarded products, make use of*licensed testers* , who by default get test ads instead of real ones. To learn how to set up accounts for these testers, see[User-test a Google Play Billing app](https://developer.android.com/google/play/billing/billing_testing#testing-purchases).

Another method of testing is for you to use the`android.test.reward`product ID. This specific product is a reserved name in Google Play Billing, so you don't need to add it to your list of in-app products in the Play Console.  
**Caution:** When testing your app's rewarded products,**don't use actual products**; otherwise, your account might be flagged as a spam or fraudulent account.

When you're done testing, however, make sure you replace`android.test.reward`with the product IDs for your actual rewarded products before you deploy your production app to end users.

## Diagram of rewarded product workflow

The following sequence diagram shows how the user, your app, and the Google Play Billing Library work together to show a video ad and grant the user access to a rewarded product:
![Sequence diagram showing rewarded products protocol](https://developer.android.com/static/images/in-app-billing/rewarded-products-workflow.svg)**Figure 1.**Steps for completing a rewarded product purchase using Google Play Billing