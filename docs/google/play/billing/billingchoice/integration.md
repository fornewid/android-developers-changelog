---
title: https://developer.android.com/google/play/billing/billingchoice/integration
url: https://developer.android.com/google/play/billing/billingchoice/integration
source: md.txt
---

This guide describes how to integrate your app with the Play Billing Library
APIs so that you can offer [billing choice](https://developer.android.com/google/play/billing/billingchoice) to your users.

## Integration with PBL

You can integrate billing choice with the PBL in four scenarios. The scenarios
differ based on who renders the choice screen and where the payment will happen.
The following table outlines the integration scenarios:

|---|---|---|---|
|   || Which billing choice screen do you want to render? ||
|   || Google Play's | Your own (in accordance with the UX guidelines) |
| Where does the payment happen? | In-app | **Scenario 1A** Google renders the choice screen and the **alternate billing is handled within your app**. | **Scenario 1B** App developer renders the choice screen and the **alternate billing is handled within your app**. |
| Where does the payment happen? | External web link | **Scenario 2A** Google renders the choice screen and the user is **linked outside of your app to your own websites** for purchases. | **Scenario 2B** App developer renders the choice screen and the user is **linked outside of your app to your own websites** for purchases. |

The following illustration elaborates the billing choice flow for each of these
scenarios:
![The billing choice flow showing the sequence of API calls and user interactions for the four integration scenarios.](https://developer.android.com/static/images/google/play/billing/billingchoice/billing-choice-3.png) **Figure 1.** Billing choice integration scenarios

![](https://developer.android.com/static/images/google/play/billing/billingchoice/billing-choice-3.png)

## PBL integration scenarios

Depending on your integration scenario, follow the steps in this section to
implement billing choice in your app.

### Handle scenario 1A

Google renders the choice screen and the **alternate billing is handled within**
your app. Do the following steps to enable the billing choice in this scenario:

1. Call [`enableBillingProgram`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) with [`EnableBillingProgramParams`](https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams) when
   constructing your BillingClient instance, and then start the connection. For
   example:

   ### Kotlin


       // Build the parameters to enable the Billing Choice program and assign the listener
       // to handle user selection of the developer-provided billing option.
       val params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
           .build()

       // Build the parameters to enable support for pending purchases.
       val pendingPurchasesParams = PendingPurchasesParams.newBuilder()
           .enableOneTimeProducts()
           .build()

       // Construct the BillingClient instance with the purchases updated listener,
       // pending purchases support, and the billing choice params.
       val billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases(pendingPurchasesParams)
           .enableBillingProgram(params)
           .build()

       // Establish a connection to Google Play
       val billingResult = suspendCancellableCoroutine { continuation ->
           billingClient.startConnection(object : BillingClientStateListener {
               // Called when the connection setup process completes.
               override fun onBillingSetupFinished(billingResult: BillingResult) {
                   // Resume the coroutine and pass back the BillingResult to the caller.
                   continuation.resume(billingResult)
               }

               // Called if the connection to the Play Store service is dropped.
               // This prevents the await or suspension point from hanging indefinitely.
               override fun onBillingServiceDisconnected() {
                   continuation.resume(
                       BillingResult.newBuilder()
                           .setResponseCode(BillingClient.BillingResponseCode.SERVICE_DISCONNECTED)
                           .setDebugMessage("Billing service disconnected during connection setup")
                           .build()
                   )
               }
           })
       }

   ### Java


       EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
               .build();

       BillingClient billingClient = BillingClient.newBuilder(context)
               .setListener(purchasesUpdatedListener)
               .enablePendingPurchases(
                       PendingPurchasesParams.newBuilder()
                               .enableOneTimeProducts()
                               .build()
               )
               .enableBillingProgram(params)
               .build();

2. Verify that the Google rendered billing choice is available for the user.

   Call [`isBillingProgramAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) to check the program
   availability, and then call [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) to show
   available products. For example:

   ### Kotlin


       val (billingResult, billingProgramAvailabilityDetails) = billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

       if (billingResult.responseCode == BillingResponseCode.OK) {
           val billingChoiceAvailabilityDetails = billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails
           if (billingChoiceAvailabilityDetails != null &&
               billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.GOOGLE_RENDERED
           ) {
               // Billing choice is available. Query products and proceed.

           } else {
               // Fallback to other available programs.
           }
       } else {
           // Fallback to other available programs.
       }


   ### Java


       // ...
       billingClient.isBillingProgramAvailableAsync(
           BillingProgram.BILLING_CHOICE,
           (billingResult, billingProgramAvailabilityDetails) -> {
               if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                   BillingChoiceAvailabilityDetails billingChoiceAvailabilityDetails =
                       billingProgramAvailabilityDetails.getBillingChoiceAvailabilityDetails();

                   if (billingChoiceAvailabilityDetails != null &&
                       billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.GOOGLE_RENDERED) {
                       // Billing choice is available. Query products and proceed.
                   } else {
                       // Fallback to other available programs.
                   }
               } else {
                   // Fallback to other available programs.
               }
           }
       );

   **Note** : `billingProgramAvailabilityDetails` tells you if Google
   rendered or Developer rendered billing choice screen is available.
3. Call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) to trigger the purchase flow when the user
   clicks Buy. If billing choice is available, pass
   [`DeveloperBillingOptionParams`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams) to [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams). For
   example:

   ### Kotlin


       val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .build()

       val billingFlowParams = BillingFlowParams.newBuilder()
           .setProductDetailsParamsList(productDetailsParamsList)
           .enableDeveloperBillingOption(developerBillingOptionParams)
           .build()

       val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

   ### Java


       DeveloperBillingOptionParams developerBillingOptionParams =
           DeveloperBillingOptionParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .build();
       BillingFlowParams billingFlowParams =
           BillingFlowParams.newBuilder()
               .setProductDetailsParamsList(productDetailsParamsList)
               .enableDeveloperBillingOption(developerBillingOptionParams)
               .build();

       BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

   **Note** : Parental control is displayed for [supervised users](https://support.google.com/families/answer/7106960).
4. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, the billing result is returned to the [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) registered in step 1.
   - If the user selects your alternative billing, the billing result is returned to the [`DeveloperProvidedBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener) registered in step 1. The returned [`DeveloperProvidedBillingDetails`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails) contains an `externalTransactionToken` in this case. The token will be used for transaction reporting.

### Handle scenario 1B

Developer renders the choice screen and the **alternate billing is handled
within** your app. Do the following steps to enable the billing choice in this
scenario:

1. Call [`enableBillingProgram`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) without the
   [`DeveloperProvidedBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener) in
   [`EnableBillingProgramParams`](https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams) when constructing a `BillingClient`
   instance, and then start the connection. For example:

   ### Kotlin


       // Build the parameters to enable the Billing Choice program.
       val params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .build()

       // Construct the BillingClient instance with the purchases updated listener,
       // pending purchases support, and the billing choice params.
       val billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases()
           .enableBillingProgram(params)
           .build()

       // Establish a connection to Google Play
       val billingResult = suspendCancellableCoroutine<BillingResult> { continuation ->
           billingClient.startConnection(object : BillingClientStateListener {
               // Called when the connection setup process completes.
               override fun onBillingSetupFinished(billingResult: BillingResult) {
                   // Resume the coroutine and pass back the BillingResult to the caller.
                   continuation.resume(billingResult)
               }

               // Called if the connection to the Play Store service is dropped.
               // This prevents the await or suspension point from hanging indefinitely.
               override fun onBillingServiceDisconnected() {
                   continuation.resume(
                       BillingResult.newBuilder()
                           .setResponseCode(BillingClient.BillingResponseCode.SERVICE_DISCONNECTED)
                           .setDebugMessage("Billing service disconnected during connection setup")
                           .build()
                   )
               }
           })
       }

   ### Java


       EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .build();

       BillingClient billingClient = BillingClient.newBuilder(context)
               .setListener(purchasesUpdatedListener)
               .enablePendingPurchases()
               .enableBillingProgram(params)
               .build();

2. Verify that the developer rendered billing choice is available for the user.

   Call [`isBillingProgramAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) to check the program
   availability, and then call [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) to show
   available products. For example:

   ### Kotlin


       val (billingResult, billingProgramAvailabilityDetails) =
           billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

       if (billingResult.responseCode == BillingResponseCode.OK) {
           val billingChoiceAvailabilityDetails =
               billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

           if (billingChoiceAvailabilityDetails != null &&
               billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.DEVELOPER_RENDERED
           ) {
               // Billing choice is available. Query products and proceed.
               // You can inspect details such as:
               // - billingChoiceAvailabilityDetails.choiceScreenType
               // - billingChoiceAvailabilityDetails.isExternalLinkAvailable
           } else {
               // Fallback to other available programs.
           }
       } else {
           // Fallback to other available programs.
       }

   ### Java


       // ...
       billingClient.isBillingProgramAvailableAsync(
           BillingProgram.BILLING_CHOICE,
           (billingResult, billingProgramAvailabilityDetails) -> {
               if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                   BillingChoiceAvailabilityDetails billingChoiceAvailabilityDetails =
                       billingProgramAvailabilityDetails.getBillingChoiceAvailabilityDetails();

                   if (billingChoiceAvailabilityDetails != null
                           && billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.DEVELOPER_RENDERED) {
                       // Billing choice is available. Query products and proceed.
                       // You can inspect details such as:
                       // - billingChoiceAvailabilityDetails.getChoiceScreenType()
                       // - billingChoiceAvailabilityDetails.isExternalLinkAvailable()
                   } else {
                       // Fallback to other available programs.
                   }
               } else {
                   // Fallback to other available programs.
               }
           }
       );

   **Note** : `billingProgramAvailabilityDetails` tells you if Google rendered
   or Developer rendered billing choice screen is available.
3. Call the `getBillingChoiceInfoAsync` method to get the Play Billing banner
   and loyalty information. For example:

   ### Kotlin


       // 1. Create the params required for the request
       val params = GetBillingChoiceInfoParams.newBuilder()
           .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
           .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
           .build()

       // 2. Call the suspend method on your billingClient instance
       val (billingResult, playBillingChoiceInfo) = billingClient.getBillingChoiceInfo(params)

       if (billingResult.responseCode == BillingResponseCode.OK && playBillingChoiceInfo != null) {
           // Access the URL of the image associated with the Play Billing Choice
           val imageUrl = playBillingChoiceInfo.playBillingChoiceImageUrl

           // Access the Play Loyalty string information, if available
           val loyaltyInfo = playBillingChoiceInfo.playBillingLoyaltyInfo

           // Populate your developer-rendered UI elements
           playBillingLoyaltyTextView.text = loyaltyInfo
           loadImage(imageUrl, playBillingImageView)
       } else {
           // Handle error scenarios
       }

   ### Java


       // 1. Create the params required for the request
       GetBillingChoiceInfoParams params = GetBillingChoiceInfoParams.newBuilder()
           .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
           .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
           .build();
       // 2. Call the method asynchronously on your billingClient instance
       billingClient.getBillingChoiceInfoAsync(params, (billingResult, playBillingChoiceInfo) -> {
           if (billingResult.getResponseCode() == BillingResponseCode.OK && playBillingChoiceInfo != null) {
             // Access the URL of the image associated with the Play Billing Choice
               String imageUrl = playBillingChoiceInfo.getPlayBillingChoiceImageUrl();
               // Access the Play Loyalty string information, if available
               String loyaltyInfo = playBillingChoiceInfo.getPlayBillingLoyaltyInfo();

               // Populate your developer-rendered UI elements
               playBillingLoyaltyTextView.setText(loyaltyInfo);
                 loadImage(imageUrl, playBillingImageView);
             } else {
                 // Handle error scenarios
             }
       });

4. Create an external transaction token with DeveloperBillingType set to
   **IN_APP**. For example:

   ### Kotlin


       // Build the parameters specifying the billing program and that the billing type is IN_APP.
       val params = BillingProgramReportingDetailsParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperBillingType(DeveloperBillingType.IN_APP)
           .build()

       // Call the suspending extension function to request the reporting details
       val (billingResult, billingProgramReportingDetails) =
           billingClient.createBillingProgramReportingDetails(params)
           
       if (billingResult.responseCode != BillingResponseCode.OK) {
           // Handle failures such as retrying due to network errors.
           return
       }

       // Extract the transaction token from the returned reporting details
       val transactionToken = billingProgramReportingDetails?.externalTransactionToken

       // Persist the external transaction token locally. Pass it to
       // DeveloperBillingOptionParams when launchBillingFlow is called.
       // It can also be used as part of your external website

   ### Java


       BillingProgramReportingDetailsParams params =
           BillingProgramReportingDetailsParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperBillingType(DeveloperBillingType.IN_APP)
               .build();

       billingClient.createBillingProgramReportingDetailsAsync(
           params,
           new BillingProgramReportingDetailsListener() {
               @Override
               public void onCreateBillingProgramReportingDetailsResponse(
                   BillingResult billingResult,
                   @Nullable BillingProgramReportingDetails billingProgramReportingDetails
               ) {
                   if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                       // Handle failures such as retrying due to network errors.
                       return;
                   }

                   String transactionToken =
                       billingProgramReportingDetails.getExternalTransactionToken();

                   // Persist the external transaction token locally. Pass it to
                   // DeveloperBillingOptionParams when launchBillingFlow is called.
                   // It can also be used as part of your external website
               }
           }
       );


5. When the user clicks Buy, call `showBillingProgramInformationDialog` to show
   an information dialog. For example, see [Information dialog for users](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app#information-dialog).
   **BillingProgram and transactionToken** from step 4 must be set in the
   request.

   **Note** : Parental control is displayed for [supervised users](https://support.google.com/families/answer/7106960).
6. Launch your alternative billing choice screen if the result from the
   previous step is `OK`.

7. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) following the [standard Play Billing guidance](https://developer.android.com/google/play/billing/integrate#launch). The billing result is returned to the [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) registered in step 1.
   - If the user selects your alternative billing, you must handle the transaction yourself and report it to Play using the token generated in step 4.

### Handle scenario 2A

Google renders the choice screen and the **alternate billing is handled
outside** your app. Do the following steps to enable the billing choice in this
scenario:

1. Call [`enableBillingProgram`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) with [`EnableBillingProgramParams`](https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams) when
   constructing your BillingClient instance, and then start the connection. For
   example:

   ### Kotlin


       // Build the parameters to enable the Billing Choice program and assign the listener
       // to handle user selection of the developer-provided billing option.
       val params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
           .build()

       // Build the parameters to enable support for pending purchases.
       val pendingPurchasesParams = PendingPurchasesParams.newBuilder()
           .enableOneTimeProducts()
           .build()

       // Construct the BillingClient instance with the purchases updated listener,
       // pending purchases support, and the billing choice params.
       val billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases(pendingPurchasesParams)
           .enableBillingProgram(params)
           .build()

       // Establish a connection to Google Play
       val billingResult = suspendCancellableCoroutine { continuation ->
           billingClient.startConnection(object : BillingClientStateListener {
               // Called when the connection setup process completes.
               override fun onBillingSetupFinished(billingResult: BillingResult) {
                   // Resume the coroutine and pass back the BillingResult to the caller.
                   continuation.resume(billingResult)
               }

               // Called if the connection to the Play Store service is dropped.
               // This prevents the await or suspension point from hanging indefinitely.
               override fun onBillingServiceDisconnected() {
                   continuation.resume(
                       BillingResult.newBuilder()
                           .setResponseCode(BillingClient.BillingResponseCode.SERVICE_DISCONNECTED)
                           .setDebugMessage("Billing service disconnected during connection setup")
                           .build()
                   )
               }
           })
       }

   ### Java


       EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
               .build();

       BillingClient billingClient = BillingClient.newBuilder(context)
               .setListener(purchasesUpdatedListener)
               .enablePendingPurchases(
                       PendingPurchasesParams.newBuilder()
                               .enableOneTimeProducts()
                               .build()
               )
               .enableBillingProgram(params)
               .build();

2. Verify the availability of the following:

   - Google rendered billing choice
   - External web link

   Call [`isBillingProgramAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) to check the program
   availability, and then call [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) to show
   available products. For example:

   ### Kotlin


       // Check the availability of the billing choice program asynchronously using coroutines
       val (billingResult, billingProgramAvailabilityDetails) =
           billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

       // Ensure the billing program query succeeded
       if (billingResult.responseCode == BillingResponseCode.OK) {
           // Retrieve the availability details specific to the billing choice program
           val billingChoiceAvailabilityDetails =
               billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

           // Check if billing choice is available, renders via Google Play, and external link is supported
           if (billingChoiceAvailabilityDetails != null &&
               billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.GOOGLE_RENDERED &&
               billingChoiceAvailabilityDetails.isExternalLinkAvailable
           ) {
               // Billing choice is available and external transaction links are supported. Query products and proceed.
           } else {
               // Fallback to other available programs.
           }
       } else {
           // Fallback to other available programs.
       }


   ### Java


       // ...
       billingClient.isBillingProgramAvailableAsync(
           BillingProgram.BILLING_CHOICE,
           (billingResult, billingProgramAvailabilityDetails) -> {
               if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                   BillingChoiceAvailabilityDetails billingChoiceAvailabilityDetails =
                       billingProgramAvailabilityDetails.getBillingChoiceAvailabilityDetails();

                   if (billingChoiceAvailabilityDetails != null
                           && billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.GOOGLE_RENDERED
                           && billingChoiceAvailabilityDetails.isExternalLinkAvailable()) {
                       // Billing choice is available and external transaction links are supported.
                       // Query products and proceed.
                   } else {
                       // Fallback to other available programs.
                   }
               } else {
                   // Fallback to other available programs.
               }
           }
       );


3. Call [`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)) to create an external
   transaction token when the user shows the intention to buy. For example:

   ### Kotlin


       // Build the parameters for creating reporting details
       val params =
           BillingProgramReportingDetailsParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
               .build()

       // Call the suspend function to create billing program reporting details
       val (billingResult, billingProgramReportingDetails) =
           billingClient.createBillingProgramReportingDetails(params)

       // Handle response failure cases
       if (billingResult.responseCode != BillingResponseCode.OK) {
           // Handle failures such as retrying due to network errors.
           return
       }

       // Retrieve the external transaction token
       val transactionToken =
           billingProgramReportingDetails?.externalTransactionToken

       // Persist the external transaction token locally. Pass it to
       // DeveloperBillingOptionParams when launchBillingFlow is called.
       // It can also be used as part of your external website

   ### Java


       BillingProgramReportingDetailsParams params =
           BillingProgramReportingDetailsParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
               .build();

       billingClient.createBillingProgramReportingDetailsAsync(
           params,
           new BillingProgramReportingDetailsListener() {
               @Override
               public void onCreateBillingProgramReportingDetailsResponse(
                   BillingResult billingResult,
                   @Nullable BillingProgramReportingDetails billingProgramReportingDetails
               ) {
                   if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                       // Handle failures such as retrying due to network errors.
                       return;
                   }

                   String transactionToken =
                       billingProgramReportingDetails.getExternalTransactionToken();

                   // Persist the external transaction token locally. Pass it to
                   // DeveloperBillingOptionParams when launchBillingFlow is called.
                   // It can also be used as part of your external website.
               }
           }
       );

4. Call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) to trigger the purchase flow when the user
   clicks Buy. If billing choice is available for the user, perform the
   following:

   1. Pass [DeveloperBillingOptionParams](http://DeveloperBillingOptionParams) to [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams).
   2. Pass the external transaction token from step 3 to `DeveloperBillingOptionParams`.

   For example:

   ### Kotlin


       // Build the developer billing option parameters with the external link URI,
       // the transaction token, and browser/app launch mode.
       val developerBillingOptionParams =
           DeveloperBillingOptionParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
               .setExternalTransactionToken(transactionToken)
               .setLaunchMode(
                   DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
               )
               .build()

   ### Java


       DeveloperBillingOptionParams developerBillingOptionParams =
           DeveloperBillingOptionParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
               .setExternalTransactionToken(transactionToken)
               .setLaunchMode(
                 DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
               .build();

   **Note** : Parental control is displayed for
   [supervised users](https://support.google.com/families/answer/7106960).
5. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) following the [standard Play Billing guidance](https://developer.android.com/google/play/billing/integrate#launch). The billing result is returned to the [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) registered in step 1.
   - If the user selects your alternative billing, the billing result is returned to the [`DeveloperProvidedBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener) registered in step
     1. The returned [`DeveloperProvidedBillingDetails`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails) contains the `externalTransactionToken` that was passed to `DeveloperBillingOptionParams` in step 4 if it is a valid token.

### Handle scenario 2B

Developer renders the choice screen and the **alternate billing is handled
outside** the app. Do the following steps to enable the billing choice in this
scenario:

1. Call [`enableBillingProgram`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) without the
   [`DeveloperProvidedBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener) in
   [`EnableBillingProgramParams`](https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams) when constructing a BillingClient
   instance, and then start the connection. For example:

   ### Kotlin


       // Build the parameters to enable the Billing Choice program.
       val params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .build()

       // Construct the BillingClient instance with the purchases updated listener,
       // pending purchases support, and the billing choice params.
       val billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases()
           .enableBillingProgram(params)
           .build()

       // Establish a connection to Google Play
       val billingResult = suspendCancellableCoroutine<BillingResult> { continuation ->
           billingClient.startConnection(object : BillingClientStateListener {
               // Called when the connection setup process completes.
               override fun onBillingSetupFinished(billingResult: BillingResult) {
                   // Resume the coroutine and pass back the BillingResult to the caller.
                   continuation.resume(billingResult)
               }

               // Called if the connection to the Play Store service is dropped.
               // This prevents the await or suspension point from hanging indefinitely.
               override fun onBillingServiceDisconnected() {
                   continuation.resume(
                       BillingResult.newBuilder()
                           .setResponseCode(BillingClient.BillingResponseCode.SERVICE_DISCONNECTED)
                           .setDebugMessage("Billing service disconnected during connection setup")
                           .build()
                   )
               }
           })
       }

   ### Java


       EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .build();

       BillingClient billingClient = BillingClient.newBuilder(context)
               .setListener(purchasesUpdatedListener)
               .enablePendingPurchases()
               .enableBillingProgram(params)
               .build();

2. Verify the availability of the following:

   - Google rendered billing choice
   - External web link

   Call [`isBillingProgramAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) to check the program
   availability, and then call [`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) to show
   available products. For example:

   ### Kotlin


       // Check the availability of the billing choice program asynchronously using a coroutine
       val (billingResult, billingProgramAvailabilityDetails) =
           billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

       // Ensure the response code is OK
       if (billingResult.responseCode == BillingResponseCode.OK) {
           // Retrieve the billing choice availability details
           val billingChoiceAvailabilityDetails =
               billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

           // Check if billing choice details are available, choice screen is developer-rendered,
           // and external transaction links are supported.
           if (billingChoiceAvailabilityDetails != null &&
               billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.DEVELOPER_RENDERED &&
               billingChoiceAvailabilityDetails.isExternalLinkAvailable
           ) {
               // Billing choice is available and external transaction links are supported.
               // Query products and proceed.
           } else {
               // Fallback to other available programs.
           }
       } else {
           // Fallback to other available programs.
       }

   ### Java


       // ...

       billingClient.isBillingProgramAvailableAsync(
           BillingProgram.BILLING_CHOICE,
           (billingResult, billingProgramAvailabilityDetails) -> {
               if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                   BillingChoiceAvailabilityDetails billingChoiceAvailabilityDetails =
                       billingProgramAvailabilityDetails.getBillingChoiceAvailabilityDetails();
                   if (billingChoiceAvailabilityDetails != null &&
                       billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.DEVELOPER_RENDERED &&
                       billingChoiceAvailabilityDetails.isExternalLinkAvailable()) {
                       // Billing choice is available and external transaction links are supported. Query products and proceed.
                   } else {
                       // Fallback to other available programs.
                   }
               } else {
                   // Fallback to other available programs.
               }
           }
       );

3. Call the `getBillingChoiceInfoAsync` method to get the Play Billing banner
   and loyalty information.

   ### Kotlin


       // 1. Create the params required for the request
       val params = GetBillingChoiceInfoParams.newBuilder()
           .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
           .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
           .build()

       // 2. Call the suspend method on your billingClient instance
       val (billingResult, playBillingChoiceInfo) = billingClient.getBillingChoiceInfo(params)

       if (billingResult.responseCode == BillingResponseCode.OK && playBillingChoiceInfo != null) {
           // Access the URL of the image associated with the Play Billing Choice
           val imageUrl = playBillingChoiceInfo.playBillingChoiceImageUrl

           // Access the Play Loyalty string information, if available
           val loyaltyInfo = playBillingChoiceInfo.playBillingLoyaltyInfo

           // Populate your developer-rendered UI elements
           playBillingLoyaltyTextView.text = loyaltyInfo
           loadImage(imageUrl, playBillingImageView)
       } else {
           // Handle error scenarios
       }

   ### Java


       // 1. Create the params required for the request
       GetBillingChoiceInfoParams params = GetBillingChoiceInfoParams.newBuilder()
           .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
           .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
           .build();
       // 2. Call the method asynchronously on your billingClient instance
       billingClient.getBillingChoiceInfoAsync(params, (billingResult, playBillingChoiceInfo) -> {
           if (billingResult.getResponseCode() == BillingResponseCode.OK && playBillingChoiceInfo != null) {
             // Access the URL of the image associated with the Play Billing Choice
               String imageUrl = playBillingChoiceInfo.getPlayBillingChoiceImageUrl();
               // Access the Play Loyalty string information, if available
               String loyaltyInfo = playBillingChoiceInfo.getPlayBillingLoyaltyInfo();

               // Populate your developer-rendered UI elements
               playBillingLoyaltyTextView.setText(loyaltyInfo);
                 loadImage(imageUrl, playBillingImageView);
             } else {
                 // Handle error scenarios
             }
       });

4. Call [`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)) to create an external
   transaction token when the user shows the intention to buy. For example:

   ### Kotlin


       // Build the parameters for creating reporting details
       val params =
           BillingProgramReportingDetailsParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
               .build()

       // Call the suspend function to create billing program reporting details
       val (billingResult, billingProgramReportingDetails) =
           billingClient.createBillingProgramReportingDetails(params)

       // Handle response failure cases
       if (billingResult.responseCode != BillingResponseCode.OK) {
           // Handle failures such as retrying due to network errors.
           return
       }

       // Retrieve the external transaction token
       val transactionToken =
           billingProgramReportingDetails?.externalTransactionToken

       // Persist the external transaction token locally. Pass it to
       // DeveloperBillingOptionParams when launchBillingFlow is called.
       // It can also be used as part of your external website

   ### Java


       BillingProgramReportingDetailsParams params =
           BillingProgramReportingDetailsParams.newBuilder()
               .setBillingProgram(BillingProgram.BILLING_CHOICE)
               .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
               .build();

       billingClient.createBillingProgramReportingDetailsAsync(
           params,
           new BillingProgramReportingDetailsListener() {
               @Override
               public void onCreateBillingProgramReportingDetailsResponse(
                   BillingResult billingResult,
                   @Nullable BillingProgramReportingDetails billingProgramReportingDetails
               ) {
                   if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                       // Handle failures such as retrying due to network errors.
                       return;
                   }

                   String transactionToken =
                       billingProgramReportingDetails.getExternalTransactionToken();

                   // Persist the external transaction token locally. Pass it to
                   // DeveloperBillingOptionParams when launchBillingFlow is called.
                   // It can also be used as part of your external website.
               }
           }
       );

5. Launch your alternative choice screen when the user clicks Buy.

6. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams))
     following the [standard Play Billing guidance](https://developer.android.com/google/play/billing/integrate#launch). The billing result
     is returned to the [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener) registered in step
     1.

     Parental control is displayed for [supervised users](https://support.google.com/families/answer/7106960).
   - If the user selects your alternative billing, call launchExternalLink.
     For example:

     ### Kotlin


         // An activity reference from which the purchase flow will be launched.
         val activity: Activity = ...

         val params = LaunchExternalLinkParams.newBuilder()
             .setBillingProgram(BillingProgram.BILLING_CHOICE)
             // You can pass along the external transaction token from
             // BillingProgramReportingDetails as a URL parameter in the URI
             .setLinkUri(yourLinkUri)
             .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_DIGITAL_CONTENT_OFFER)
             .setLaunchMode(
                 LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
             )
             .build()

         // Call launchExternalLink with a callback
         billingClient.launchExternalLink(activity, params) { billingResult ->
             if (billingResult.responseCode == BillingResponseCode.OK) {
                 // Proceed with the rest of the purchase flow. If the user
                 // purchases an item, be sure to report the transaction to Google
                 // Play.
             } else {
                 // Handle failures such as retrying due to network errors.
             }
         }

     ### Java


         // An activity reference from which the purchase flow will be launched.
         Activity activity = ...;

         LaunchExternalLinkParams params = LaunchExternalLinkParams.newBuilder()
             .setBillingProgram(BillingProgram.BILLING_CHOICE)
             // You can pass along the external transaction token from
             // BillingProgramReportingDetails as a URL parameter in the URI
             .setLinkUri(yourLinkUri)
             .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_DIGITAL_CONTENT_OFFER)
             .setLaunchMode(
                 LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
             .setExternalTransactionToken(transactionToken)
             .build();

         LaunchExternalLinkResponseListener listener =
             new LaunchExternalLinkResponseListener() {
               @Override
               public void onLaunchExternalLinkResponse(BillingResult billingResult) {
                 if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                   // Proceed with the rest of the purchase flow. If the user
                   // purchases an item, be sure to report the transaction to Google
                   // Play.
                 } else {
                   // Handle failures such as retrying due to network errors.
                 }
               }
             };

         billingClient.launchExternalLink(activity, params, listener);

   - Pass the external transaction token from step 4
     to [`LaunchExternalLinkParams`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams). If it returns OK, proceed
     with the transaction and report the transaction to Google Play.

     Parental control is displayed for
     [supervised users](https://support.google.com/families/answer/7106960).

### Billing choice during subscription replacement

For subscription replacement, the user choice screen shouldn't be shown given
that the user choice for the original purchase is preserved for upgrades and
downgrades.

If the **original purchase was processed through Google Play Billing** , you
should call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) with standard [Google Play Billing
subscription replacement](https://developer.android.com/google/play/billing/subscriptions#allow-users-change) information.

However, if the original purchase was **processed through an alternative
billing**, handling of subscription replacements slightly differ based on the
scenarios.

#### Subscription replacement in Scenario 1A

Users requesting an upgrade or a downgrade should proceed through the
developer's alternative billing system without going through the user choice
experience again.

To do this, call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) when the user requests an upgrade or a
downgrade. Use `setOriginalExternalTransactionId` inside the
`SubscriptionUpdateParams` object in the parameters to provide the external
transaction ID for the original purchase. This does not display the user choice
screen, given that the user choice for the original purchase is preserved for
upgrades and downgrades. The call to [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) in this case
generates a **new external transaction token** for the transaction that you can
retrieve from the callback.

### Kotlin


    // The external transaction ID from the current
    // alternative billing subscription.
    val externalTransactionId = //... ;

    val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingProgram.BILLING_CHOICE)
        .build()

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
        .enableDeveloperBillingOption(developerBillingOptionParams)
        .build()

    val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

    // When the user selects the alternative billing flow,
    // the DeveloperProvidedBillingListener is triggered.

### Java


    // The external transaction ID from the current
    // alternative billing subscription.
    String externalTransactionId = //... ;

    DeveloperBillingOptionParams developerBillingOptionParams =
        DeveloperBillingOptionParams.newBuilder()
            .setBillingProgram(BillingProgram.BILLING_CHOICE)
            .build();

    List<ProductDetailsParams> productDetailsParamsList = new ArrayList<>();
    productDetailsParamsList.add(
        ProductDetailsParams.newBuilder()
            // Fetched using queryProductDetailsAsync.
            .setProductDetails(productDetailsNewPlan)
            // offerIdToken can be found in
            // ProductDetails=>SubscriptionOfferDetails
            .setOfferToken(offerTokenNewPlan)
            .build());

    BillingFlowParams billingFlowParams =
        BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(productDetailsParamsList)
            .setSubscriptionUpdateParams(
                SubscriptionUpdateParams.newBuilder()
                    .setOriginalExternalTransactionId(externalTransactionId)
                    .build())
            .enableDeveloperBillingOption(developerBillingOptionParams)
            .build();

    BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

    // When the user selects the alternative billing flow,
    // the DeveloperProvidedBillingListener is triggered.


When the upgrade or downgrade is complete, you need to [report a new
transaction](https://developer.android.com/google/play/billing/alternative#report-new) using the external transaction token obtained through the
previous call for the new subscription purchase.

#### Subscription replacement in Scenario 1B

In this scenario, a new external transaction token must be generated. The only
difference from a normal purchase is that, in this scenario, user choice is
preserved, and you don't have to show the choice screen for upgrade or
downgrade. However you must show the one-time information dialog and the
parental acknowledgement.

For sample integration code, see [step 4 in Scenario 1B: Developer renders the
choice screen and the alternate billing is handled within your app](https://developer.android.com/google/play/billing/billingchoice/integration#scenario-1b).

When the upgrade or downgrade is complete, you need to [report a new
transaction](https://developer.android.com/google/play/billing/alternative#report-new) using the external transaction token obtained through the
previous call for the new subscription purchase.

#### Subscription replacement in Scenario 2A

For subscriptions that were originally bought through the developer's website or
a payment app after user choice, users requesting an upgrade or a downgrade
should proceed through the developer's website or a payment app without going
through the user choice experience again.

To do this, call [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) when the user requests an upgrade or a
downgrade. Instead of specifying other params under the
`SubscriptionUpdateParams` object, use [`setOriginalExternalTransactionId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String))(),
providing the external transaction ID for the original purchase.
`DeveloperBillingOptionParams` must also be provided in this call. This does not
display the user choice screen, given that the user choice for the original
purchase is preserved for upgrades and downgrades. For example:

### Kotlin


    val externalTransactionId = //... ;

    // 1. Construct DeveloperBillingOptionParams indicating the billing program
    val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
        .build()

    // 2. Build BillingFlowParams combining DeveloperBillingOptionParams and SubscriptionUpdateParams
    val billingFlowParams = BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(
            listOf(
                BillingFlowParams.ProductDetailsParams.newBuilder()
                    // Fetched using queryProductDetailsAsync.
                    .setProductDetails(productDetailsNewPlan)
                    // offerIdToken can be found in ProductDetails=>SubscriptionOfferDetails.
                    .setOfferToken(offerTokenNewPlan)
                    .build()
            )
        )
        .setSubscriptionUpdateParams(
            SubscriptionUpdateParams.newBuilder()
                .setOriginalExternalTransactionId(externalTransactionId)
                .build()
        )
        .enableDeveloperBillingOption(developerBillingOptionParams)
        .build()

### Java


    String externalTransactionId = //... ;

    // 1. Construct DeveloperBillingOptionParams indicating the billing program
    DeveloperBillingOptionParams developerBillingOptionParams =
        DeveloperBillingOptionParams.newBuilder()
            .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
            .build();

    // 2. Add ProductDetailsParams
    List productDetailsParamsList = new ArrayList<>();
    productDetailsParamsList.add(
        ProductDetailsParams.newBuilder()
            // Fetched using queryProductDetailsAsync.
            .setProductDetails(productDetailsNewPlan)
            // offerIdToken can be found in ProductDetails=>SubscriptionOfferDetails
            .setOfferToken(offerTokenNewPlan)
            .build());

    // 3. Build BillingFlowParams combining DeveloperBillingOptionParams and SubscriptionUpdateParams
    BillingFlowParams billingFlowParams =
        BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(productDetailsParamsList)
            .setSubscriptionUpdateParams(
                SubscriptionUpdateParams.newBuilder()
                    .setOriginalExternalTransactionId(externalTransactionId)
                    .build())
            .enableDeveloperBillingOption(developerBillingOptionParams)
            .build();


You must also generate a new external transaction token. For example:

### Kotlin


    val params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.BILLING_CHOICE)
            .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
            .build()

    billingClient.createBillingProgramReportingDetailsAsync(
        params,
        object : BillingProgramReportingDetailsListener {
            override fun onCreateBillingProgramReportingDetailsResponse(
                billingResult: BillingResult,
                billingProgramReportingDetails: BillingProgramReportingDetails?
            ) {
                if (billingResult.responseCode != BillingResponseCode.OK) {
                    // Handle failures such as retrying due to network errors.
                    return
                }
                val externalTransactionToken =
                    billingProgramReportingDetails?.externalTransactionToken
                // Persist the external transaction token locally. Pass it to
                // the external website using DeveloperBillingOptionParams when
                // launchBillingFlow is called.
            }
        }
    )

### Java


    BillingProgramReportingDetailsParams params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.BILLING_CHOICE)
            .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
            .build();

    billingClient.createBillingProgramReportingDetailsAsync(
        params,
        new BillingProgramReportingDetailsListener() {
          @Override
          public void onCreateBillingProgramReportingDetailsResponse(
              BillingResult billingResult,
              @Nullable BillingProgramReportingDetails billingProgramReportingDetails) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
              // Handle failures such as retrying due to network errors.
              return;
            }
            String transactionToken =
                billingProgramReportingDetails.getExternalTransactionToken();
            // Persist the external transaction token locally. Pass it to
            // the external website using DeveloperBillingOptionParams when
            // launchBillingFlow is called.
          }
        });

After generating the new token, you must call the [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams))
method to launch the purchase flow.

When the upgrade or downgrade is complete, you need to [report a new
transaction](https://developer.android.com/google/play/billing/outside-gpb-backend) using the external transaction token obtained through the
previous call for the new subscription purchase.

#### Subscription replacement in Scenario 2B

The steps to handle subscription replacement in this scenario are similar to the
steps described in **Subscription replacement in Scenario 2A** . The only
difference is that after generating the transaction token, instead of calling
the [`launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) method, you must call the launchExternalLink to
show the linkout disclaimer dialog. In this scenario, user choice is preserved,
and you don't have to show the choice screen for upgrade or downgrade.

For sample integration code, see [step 6 in Scenario 2B: Developer renders the
choice screen and the alternate billing is handled within your app](https://developer.android.com/google/play/billing/billingchoice/integration#scenario-2b).

When the upgrade or downgrade is complete, you need to [report a new
transaction](https://developer.android.com/google/play/billing/outside-gpb-backend) using the external transaction token obtained through the
previous call for the new subscription purchase.