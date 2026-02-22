---
title: https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app
url: https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app
source: md.txt
---

# In-app integration guidance for alternative billing with user choice

| **Note:** Manual reporting of alternative billing with user choice is being sunset. Please find more details about migration deadlines[here](https://support.google.com/googleplay/android-developer/answer/13821247). To learn about what transactions need to be migrated and how to migrate see[Migrating from manual reporting](https://developer.android.com/google/play/billing/alternative/backend#migrating-manual)for more information.

This guide describes how to integrate the APIs to offer alternative billing with user choice in your app.

## Play Billing Library setup

[Add the Play Billing Library dependency](https://developer.android.com/google/play/billing/getting-ready#dependency)to your Android app. To use the alternative billing APIs you need to use version 5.2 or higher. If you need to migrate from an earlier version, follow the instructions in the[migration guide](https://developer.android.com/google/play/billing/migrate-gpblv5)before you attempt to implement alternative billing.

## Connect to Google Play

| **Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without user choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.

The first steps in the integration process are the same as the ones described in the[Google Play Billing integration guide](https://developer.android.com/google/play/billing/integrate), with a few modifications when[initializing your BillingClient](https://developer.android.com/google/play/billing/integrate#initialize):

- You need to call a new method to indicate that you want to offer the user a choice of billing options:[`enableUserChoiceBilling`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)).
- You need to register an[`UserChoiceBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener)for handling cases where the user chooses alternative billing.

The following example demonstrates initializing a`BillingClient`with these modifications:  

### Kotlin

    val purchasesUpdatedListener =
       PurchasesUpdatedListener { billingResult, purchases ->
           // Handle new Google Play purchase.
       }

    val userChoiceBillingListener =
       UserChoiceBillingListener { userChoiceDetails ->
           // Handle alternative billing choice.
       }

    val billingClient = BillingClient.newBuilder(context)
       .setListener(purchasesUpdatedListener)
       .enablePendingPurchases()
       .enableUserChoiceBilling(userChoiceBillingListener)
       .build()

### Java

    private PurchasesUpdatedListener purchasesUpdatedListener = new PurchasesUpdatedListener() {
        @Override
        public void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
            // Handle new Google Play purchase.
        }
    };

    private UserChoiceBillingListener userChoiceBillingListener = new UserChoiceBillingListener() {
        @Override
        public void userSelectedAlternativeBilling(
            UserChoiceDetails userChoiceDetails) {
            // Handle new Google Play purchase.
        }
    };

    private BillingClient billingClient = BillingClient.newBuilder(context)
        .setListener(purchasesUpdatedListener)
        .enablePendingPurchases()
        .enableUserChoiceBilling(userChoiceBillingListener)
        .build();

After you initialize the`BillingClient`, you need to[establish a connection to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play)as described in the integration guide.

## Display available products

You can[display available products to the user](https://developer.android.com/google/play/billing/integrate#show-products)in the same way as with a Google Play billing system integration. When your user has seen the products available for purchase and selects one to buy, launch the user choice billing flow as described in the following section.

## Launch the user choice billing flow

| **Note:** If you are offering user choice billing through alternative billing APIs, the user experience requirements will be met by integrating with and using the client-side APIs. You will not need to separately follow the interim user experience guidelines ([for South Korea](https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice),[for other eligible markets](https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice)).

Launch the user choice billing flow by calling`launchBillingFlow()`. This works the same as[launching a purchase flow](https://developer.android.com/google/play/billing/integrate#launch)with a Google Play billing system integration: you provide a`ProductDetails`instance and an`offerToken`corresponding to the product and the offer that the user wants to acquire. If the user chooses Google Play's billing system, this information is used to continue the purchase flow.

When developers call`launchBillingFlow()`, the Google Play billing system performs the following check:

- The system checks if the user's[Google Play country](https://support.google.com/googleplay/answer/7431675)is a country that supports alternative billing with user choice (i.e. a supported country). If the user's Google Play country is supported, Google Play checks whether alternative billing has been enabled based on the configuration of the`BillingClient`.
  - If alternative billing with user choice has been enabled, the purchase flow shows the[user choice UX](https://developer.android.com/google/play/billing/alternative#user-experience).
  - If alternative billing with user choice is**not**enabled, the purchase flow shows the standard Google Play billing system UX, without user choice.
- If the user's Google Play country is**not**a supported country, the purchase flow shows the standard Google Play billing system UX, without user choice.

|                                                               |    User's Play country is a supported country    |  User's Play country is not a supported country  |
|   enableUserChoiceBilling called during BillingClient setup   |             User sees user choice UX             | User sees standard Google Play billing system UX |
| enableUserChoiceBilling not called during BillingClient setup | User sees standard Google Play billing system UX | User sees standard Google Play billing system UX |
|---------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|

## Handle the user selection

How you handle the rest of the purchase flow differs depending on whether the user selected Google Play's billing system or an alternative billing system.

### When the user selects an alternative billing system

If the user chooses the alternative billing system, Google Play calls the`UserChoiceBillingListener`to notify the app that it needs to launch the purchase flow in the alternative billing system. In particular, the`userSelectedAlternativeBilling()`method is called.

The external transaction token provided in the`UserChoiceDetails`object represents a signature for the user's choice to enter the alternative billing flow. Use this token to report any transaction resulting from this choice as explained in the[backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend).

The`UserChoiceBillingListener`should perform the following actions:

- Get the product or products being purchased by the user so that they can be presented in the purchase flow in the alternative billing system.
- Collect the string received as the external transaction token and send it to your backend to persist it. This is used later to report the external transaction to Google Play if the user completes this specific purchase.
- Launch the developer's alternative purchase flow.

If the user completes the purchase using the alternative billing system,**you must report the transaction to Google Play by calling the Google Play Developer API from your backend within 24 hours** , providing the`externalTransactionToken`and additional transaction details. See the[backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend)for more details.

The following example demonstrates how to implement the`UserChoiceBillingListener`:
**Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without user choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.  

### Kotlin

    private val userChoiceBillingListener =
        UserChoiceBillingListener { userChoiceDetails ->
            // Get the products being purchased by the user.
            val products = userChoiceDetails.products

            // Send external transaction token to developer backend server
            // this devBackend object is for demonstration purposes,
            // developers can implement this step however best fits their
            // app to backend communication.
            devBackend.sendExternalTransactionStarted(
                userChoiceDetails.externalTransactionToken,
                user
            )

            // Launch alternative billing
            // ...
            // The developer backend handles reporting the transaction
            // to Google Play's backend once the alternative billing
            // purchase is completed.
        }

### Java

    private userChoiceBillingListener userChoiceBillingListener = new UserChoiceBillingListener() {
        @Override
        public void userSelectedAlternativeBilling(
               UserChoiceDetails userChoiceDetails) {
           // Get the products being purchased by the user.
           List<Product> products =
                  userChoiceDetails.getProducts();

           // Send external transaction token to developer backend server
           // this devBackend object is for demonstration purposes,
           // developers can implement this step however best fits their
           // app to backend communication.
           devBackend.sendExternalTransactionStarted(
                  userChoiceDetails.getExternalTransactionToken(),
                  user
           );

           // Launch alternative billing
           // ...
           // The developer backend handles reporting the transaction
           // to Google Play's backend once the alternative billing
           // purchase is completed.
        }
    };

### When the user selects Google Play's billing system

If the user chooses Google Play's billing system, they continue with the purchase through Google Play.

- See[Processing purchases](https://developer.android.com/google/play/billing/integrate#process)in the library integration guide for more information about how to handle new in-app purchases through Google Play's billing system.
- See[New subscriptions](https://developer.android.com/google/play/billing/subscriptions#new)in the subscription management guide for additional guidance for subscription purchases.

## Handle changes in subscription

| **Note:** Manual reporting of alternative billing with user choice is being sunset. Please find more details about migration deadlines[here](https://support.google.com/googleplay/android-developer/answer/13821247). To learn about what transactions need to be migrated and how to migrate see[Migrating from manual reporting](https://developer.android.com/google/play/billing/alternative/backend#migrating-manual)for more information.

For developers using alternative billing with user choice, purchases need to be either processed through Google Play's billing system or reported with an`externalTransactionId`, depending on the user's choice. Changes to existing subscriptions that were processed through the user choice flow can be made through the same billing system until expiration.

This section describes how to handle some common subscription change scenarios.

### Upgrade and downgrade flows

Subscription plan changes including upgrade and downgrade flows should be handled differently depending on whether the subscription was originally bought through Google Play's billing system or through an alternative billing system.

Add-ons that depend on an existing subscription, share the same payment method, and align recurring charges are handled as upgrades. For other add-ons, users should be able to choose which billing system they want to use. Initiate a new purchase experience by using`launchBillingFlow()`, as described in[Launch the user choice billing flow](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app#launch-user-choice).

#### Subscriptions bought through an alternative billing system

For subscriptions that were originally bought through the developer's alternative billing system after user choice, users requesting an upgrade or a downgrade should proceed through the developer's alternative billing system without going through the user choice experience again.

To do this, call`launchBillingFlow()`when the user requests an upgrade or a downgrade. Instead of specifying a`SubscriptionUpdateParams`object in the parameters, use`setOriginalExternalTransactionId`, providing the external transaction ID for the original purchase. This does**not** display the user choice screen, given that the user choice for the original purchase is preserved for upgrades and downgrades. The call to`launchBillingFlow()`in this case generates a**new external transaction token**for the transaction that you can retrieve from the callback.
**Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.  

### Kotlin

    // The external transaction ID from the current
    // alternative billing subscription.
    val externalTransactionId = //... ;

    val billingFlowParams = BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(
            listOf(
                BillingFlowParams.ProductDetailsParams.newBuilder()
                    // Fetched using queryProductDetailsAsync.
                    .setProductDetails(productDetailsNewPlan)
                    // offerIdToken can be found in
                    // ProductDetails=>SubscriptionOfferDetails.
                    .setOfferToken(offerTokenNewPlan)
                    .build()
            )
        )
        .setSubscriptionUpdateParams(
            BillingFlowParams.SubscriptionUpdateParams.newBuilder()
                .setOriginalExternalTransactionId(externalTransactionId)
                .build()
            )
        .build()

    val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

    // When the user selects the alternative billing flow,
    // the UserChoiceBillingListener is triggered.

### Java

    // The external transaction ID from the current
    // alternative billing subscription.
    String externalTransactionId = //... ;

    BillingFlowParams billingFlowParams =
        BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(
                ImmutableList.of(
                    ProductDetailsParams.newBuilder()
                        // Fetched using queryProductDetailsAsync.
                        .setProductDetails(productDetailsNewPlan)
                        // offerIdToken can be found in
                        // ProductDetails=>SubscriptionOfferDetails
                        .setOfferToken(offerTokenNewPlan)
                        .build()
                    )
                )
            .setSubscriptionUpdateParams(
                SubscriptionUpdateParams.newBuilder()
                    .setOriginalExternalTransactionId(externalTransactionId)
                    .build()
                )
            .build();

    BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

    // When the user selects the alternative billing flow,
    // the UserChoiceBillingListener is triggered.

When the upgrade or downgrade is completed in the alternative billing system, you need to[report a new transaction](https://developer.android.com/google/play/billing/alternative#report-new)using the external transaction token obtained through the previous call for the new subscription purchase.

#### Subscriptions bought through Google Play's billing system

Similarly, users that bought their current subscription through Google Play's billing system after user choice should be shown the[upgrade or downgrade flow in Google Play's billing system](https://developer.android.com/google/play/billing/subscriptions#change). The following instructions describe how you would launch the purchase flow for an upgrade or downgrade through Google Play's billing system:

1. Identify the`offerToken`of the selected offer for the new plan:

   ### Kotlin

       val offerTokenNewPlan = productDetailsNewPlan
            .getSubscriptionOfferDetails(selectedOfferIndex)
            .getOfferToken()

   ### Java

       String offerTokenNewPlan = productDetailsNewPlan
               .getSubscriptionOfferDetails(selectedOfferIndex)
               .getOfferToken();

2. Send the correct information to Google Play's billing system to process the new purchase, including the purchase token for the existing subscription:

   ### Kotlin

       val billingFlowParams =
           BillingFlowParams.newBuilder()
               .setProductDetailsParamsList(
                   listOf(
                       BillingFlowParams.ProductDetailsParams.newBuilder()
                           // Fetched using queryProductDetailsAsync
                           .setProductDetails(productDetailsNewPlan)
                           // offerIdToken can be found in
                           // ProductDetails=>SubscriptionOfferDetails.
                           .setOfferToken(offerTokenNewPlan)
                           .build()
                       )
               )
               .setSubscriptionUpdateParams(
                   BillingFlowParams.SubscriptionUpdateParams.newBuilder()
                       // purchaseToken can be found in
                       // Purchase#getPurchaseToken
                       .setOldPurchaseToken(oldToken)
                       .setReplaceProrationMode(BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_FULL_PRICE)
                       .build()
               )
               .build()

       val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

   ### Java

       BillingFlowParams billingFlowParams =
           BillingFlowParams.newBuilder()
               .setProductDetailsParamsList(
                   ImmutableList.of(
                       ProductDetailsParams.newBuilder()
                           // Fetched using queryProductDetailsAsync
                           .setProductDetails(productDetailsNewPlan)
                           // offerIdToken can be found in
                           // ProductDetails=>SubscriptionOfferDetails.
                           .setOfferToken(offerTokenNewPlan)
                           .build()
                   )
               )
               .setSubscriptionUpdateParams(
                   SubscriptionUpdateParams.newBuilder()
                       // purchaseToken can be found in
                       // Purchase#getPurchaseToken
                       .setOldPurchaseToken(oldToken)
                       .setReplaceProrationMode(BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_FULL_PRICE)
                       .build()
               )
               .build();

       BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

This purchase proceeds in Google Play's billing system, and your app receives the`PurchasesUpdatedListener.onPurchaseUpdated`call with the result of the purchase. If the purchase was successful, the`onPurchaseUpdated()`method also receives the new purchase information, and your backend receives a`SUBSCRIPTION_PURCHASED`Real Time Developer Notification. When pulling the status for the new purchase, a`linkedPurchaseToken`attribute links to the old subscription purchase so that you can retire it[as recommended](https://medium.com/androiddevelopers/implementing-linkedpurchasetoken-correctly-to-prevent-duplicate-subscriptions-82dfbf7167da).

### Subscription cancellations and restorations

Users should be able to[cancel](https://developer.android.com/google/play/billing/subscriptions#cancel)their subscription at any time. When a user cancels a subscription, the termination of the entitlement may be deferred until the paid period ends. For example, if a user cancels a monthly subscription halfway through the month, they may continue to access the service for the remaining \~2 weeks until their access is removed. During this period, the subscription is still technically active, so the user can use the service.

It is not uncommon that users decide to reverse the cancellation during this active period. In this guide, this is called a*restoration*. The following sections describe how to handle restoration scenarios in your alternative billing API integration.

#### Subscriptions bought through an alternative billing system

If you have an external transaction ID for a canceled subscription, it's not necessary to call`launchBillingFlow()`to restore the subscription, so it shouldn't be used for this type of activation. If a user restores their subscription while still in the active period of a canceled subscription, no transaction occurs at that time; you can just continue reporting renewals when the current cycle expires and the next renewal occurs. This includes cases where the user receives a credit or special renewal price as part of the restoration (for example, a promotion to encourage the user to continue their subscription).

#### Subscriptions bought through Google Play's billing system

Generally, users can restore subscriptions on Google Play's billing system. For canceled subscriptions that were originally purchased on Google Play's billing system, the user may choose to undo the cancellation while the subscription is active through Google Play's[Resubscribe](https://developer.android.com/google/play/billing/subscriptions#restore)feature. In that case, you receive a`SUBSCRIPTION_RESTARTED`Real Time Developer Notification in your backend, and a new purchase token is**not** issued---the original token is used to continue the subscription. To learn how to manage restoration in Google Play's billing system, see[Restorations](https://developer.android.com/google/play/billing/subscriptions#restore)in the subscription management guide.

You can also trigger a restoration in Google Play's billing system from the app by calling`launchBillingFlow()`. See[Before subscription expiration - in-app](https://developer.android.com/google/play/billing/subscriptions#before-in-app)for an explanation of how to do this. In the case of users that went through the user choice flow for the original purchase (which was canceled but is still active), the system automatically detects their choice and displays the user interface for restoring these purchases. They are asked to confirm their re-purchase of the subscription through Google Play, but they don't need to go through the user choice flow again. A new purchase token is issued for the user in this case. Your backend receives a`SUBSCRIPTION_PURCHASED`Real Time Developer Notification, and the`linkedPurchaseToken`value for the new purchase status is set as in the case of an upgrade or downgrade, with the old purchase token for the subscription that was canceled.

### Resubscriptions

If a subscription completely expires, whether it is due to cancellation or payment decline without recovery (an expired account hold), then the user must*resubscribe*if they want to restart the entitlement.

Resubscribing can also be enabled through the app by processing it similarly to a standard signup. Users should be able to choose which billing system they want to use.`launchBillingFlow()`may be called in this case, as described in[Launch the user choice billing flow](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app#launch-user-choice).

## Test alternative billing

License testers should be used to test your alternative billing integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See[Test in-app billing with application licensing](https://support.google.com/googleplay/android-developer/answer/6062777)for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to[integrate your backend](https://developer.android.com/google/play/billing/outside-gpb-backend).