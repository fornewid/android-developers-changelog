---
title: https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app
url: https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app
source: md.txt
---

# In-app integration guidance for alternative billing only

| **Note:** Manual reporting of alternative billing only is being sunset. Please find more details about migration deadlines[here](https://support.google.com/googleplay/android-developer/answer/13821247). To learn about what transactions need to be migrated and how to migrate see[Migrating from manual reporting](https://developer.android.com/google/play/billing/alternative/backend#migrating-manual)for more information.

This guide describes how to integrate the APIs to offer alternative billing only (i.e. without user choice) in eligible apps. To learn more about these programs including eligibility requirements and geographic scope see[About Alternative Billing](https://developer.android.com/google/play/billing/alternative).

## Play Billing Library setup

[Add the Play Billing Library dependency](https://developer.android.com/google/play/billing/getting-ready#dependency)to your Android app. To use the alternative billing APIs you need to use version 6.1 or higher.

## Connect to Google Play

| **Note:** When using alternative billing only, your app does not need to provide a`PurchasesUpdatedListener`which is used for listening to transactions made through Google Play's Billing system.

The first steps in the integration process are the same as the ones described in the[Google Play Billing integration guide](https://developer.android.com/google/play/billing/integrate), with a few modifications when[initializing your BillingClient](https://developer.android.com/google/play/billing/integrate#initialize):

- You need to call a new method to indicate that your app uses only an alternative billing system:[`enableAlternativeBillingOnly`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBillingOnly()).

The following example demonstrates initializing a`BillingClient`with these modifications:  

### Kotlin


    var billingClient = BillingClient.newBuilder(context)
        .enableAlternativeBillingOnly()
        .build()

### Java

    private BillingClient billingClient = BillingClient.newBuilder(context)
        .enableAlternativeBillingOnly()
        .build();

After you initialize the`BillingClient`, you need to[establish a connection to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play)as described in the integration guide.

## Checking Availability

| **Note:** See response handling section for instructions on how to handle errors from this API.

Your app should confirm alternative billing only is available by calling[`isAlternativeBillingOnlyAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isAlternativeBillingOnlyAvailableAsync(com.android.billingclient.api.AlternativeBillingOnlyAvailabilityListener)).

This API will return[BillingResponseCode.OK](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK)if alternative billing only is available. Refer to[response handling](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app#response-handling)for details on how your app should respond to other response codes.  

### Kotlin


    billingClient.isAlternativeBillingOnlyAvailableAsync(object:
        AlternativeBillingOnlyAvailabilityListener {
            override fun onAlternativeBillingOnlyAvailabilityResponse(
                billingResult: BillingResult) {
                if (billingResult.responseCode !=  BillingResponseCode.OK) {
                    // Handle failures such as retrying due to network errors,
                    // handling alternative billing only being unavailable, etc.
                    return
                }

                // Alternative billing only is available. Continue with steps in
                // the guide.
            }
        });

### Java


    billingClient.isAlternativeBillingOnlyAvailable(
        new AlternativeBillingOnlyAvailabilityListener() {
            @Override
            public void onAlternativeBillingOnlyAvailabilityResponse(
                BillingResult billingResult) {
                if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                     // Handle failures such as retrying due to network errors,
                     // handling alternative billing only being unavailable,
                     // etc.
                    return;
                }

                // Alternative billing only is available. Continue with steps in
                // the guide.
            }
        });

## Information dialog for users

| **Note:** See response handling section for instructions on how to handle errors from this API.
| **Note:** If you are offering alternative billing only through alternative billing APIs, the user experience requirements will be met by integrating with and using the client-side APIs. You will not need to separately follow the[interim user experience guidelines](https://developer.android.com/google/play/billing/alternative/interim-ux/alt-billing).

To integrate with alternative billing only, your eligible app must show an information screen which helps users understand that billing will not be managed by Google Play. The information screen must be shown to users by calling the[`showAlternativeBillingOnlyInformationDialog`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener))API before starting the alternative billing flow each time. If the user has already acknowledged the dialog, using this API will typically not result in the dialog being shown again. There may be times when the dialog is shown again to a user in situations such as if the user clears caches on their device.  

### Kotlin


    // An activity reference from which the alternative billing only information
    // dialog will be launched.
    val activity : Activity = ...;

    val listener : AlternativeBillingOnlyInformationDialogListener =
        AlternativeBillingOnlyInformationDialogListener { 
            override fun onAlternativeBillingOnlyInformationDialogResponse(
                billingResult: BillingResult) {
                // check billingResult
            }
    }

    val billingResult =
        billingClient.showAlternativeBillingOnlyInformationDialog(activity,
            listener)

### Java


    // An activity reference from which the alternative billing only information
    // dialog will be launched.
    Activity activity = ...;

    AlternativeBillingOnlyInformationDialogListener listener =
        new AlternativeBillingOnlyInformationDialogListener() {
            @Override
            public void onAlternativeBillingOnlyInformationDialogResponse(
                BillingResult billingResult) {
                    // check billingResult
                }
        };

    BillingResult billingResult =
        billingClient.showAlternativeBillingOnlyInformationDialog(activity,
            listener);

If this method returns[BillingResponseCode.OK](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK)then your app can proceed with the transaction. In the case of[BillingResponseCode.USER_CANCELED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED)your app should call showAlternativeBillingOnlyInformationDialog to show the dialog to the user again. For other response codes see the[response handling section](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app#response-handling).

## Reporting transactions to Google Play

| **Note:** See response handling for instructions on how to handle errors from this API.

All transactions made through an alternative billing system**must be reported to Google Play by calling the Google Play Developer API from your backend within 24 hours** , providing an`externalTransactionToken`which is obtained using the API described below. A new externalTransactionToken should be generated for each one-time purchase, each new subscription, and for any upgrade/downgrades to an existing subscription. To learn how to report a transaction once an`externalTransactionToken`is obtained see the[backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend).  

### Kotlin

    billingClient.createAlternativeBillingOnlyReportingDetailsAsync(object:
        AlternativeBillingOnlyReportingDetailsListener {
            override fun onAlternativeBillingOnlyTokenResponse(
                billingResult: BillingResult,
                alternativeBillingOnlyReportingDetails:
                    AlternativeBillingOnlyReportingDetails?) {
                if (billingResult.responseCode !=  BillingResponseCode.OK) {
                    // Handle failures such as retrying due to network errors.
                    return
                }

                val externalTransactionToken =
                    alternativeBillingOnlyReportingDetails?
                        .externalTransactionToken

                // Send transaction token to backend and report to Google Play.
            }
        });

### Java


    billingClient.createAlternativeBillingOnlyReportingDetailsAsync(
        new AlternativeBillingOnlyReportingDetailsListener() {
            @Override
            public void onAlternativeBillingOnlyTokenResponse(
                BillingResult billingResult,
                @Nullable AlternativeBillingOnlyReportingDetails
                    alternativeBillingOnlyReportingDetails) {
                if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                    // Handle failures such as retrying due to network errors.
                    return;
                }

                String transactionToken =
                    alternativeBillingOnlyReportingDetails
                    .getExternalTransactionToken();

                // Send transaction token to backend and report to Google Play.
            }
        });

## Response handling

The above methods`isAlternativeBillingOnlyAvailableAsync(),
showAlternativeBillingOnlyInformationDialog()`, and`createAlternativeBillingOnlyReportingDetailsAsync()`may return non-BillingResponseCode.OK responses in the case of errors. The recommended handling of the errors is described below:

- `ERROR`: This is an internal error. Don't proceed with the transaction. Retry again by calling`showAlternativeBillingOnlyInformationDialog()`to display the information dialog to the user the next time the user attempts to make a purchase.
- `FEATURE_NOT_SUPPORTED`: The alternative billing APIs are not supported by the Play Store on the current device. Don't proceed with the transaction.
- `USER_CANCELED`: Don't proceed with the transaction. Call`showAlternativeBillingOnlyInformationDialog()`again to display the information dialog to the user the next time the user attempts to make a purchase.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for alternative billing only and therefore shouldn't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be retried. In the case of`SERVICE_DISCONNECTED`re-establish a connection with Google Play before retrying.

## Test alternative billing

License testers should be used to test your alternative billing integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See[Test in-app billing with application licensing](https://support.google.com/googleplay/android-developer/answer/6062777)for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to[integrate your backend](https://developer.android.com/google/play/billing/outside-gpb-backend).