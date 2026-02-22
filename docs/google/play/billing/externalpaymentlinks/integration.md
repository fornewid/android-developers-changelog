---
title: https://developer.android.com/google/play/billing/externalpaymentlinks/integration
url: https://developer.android.com/google/play/billing/externalpaymentlinks/integration
source: md.txt
---

This document describes how to integrate the Play Billing Library APIs to
offer external payments in eligible apps. To learn more about this program,
see [program requirements](https://support.google.com/googleplay/android-developer/answer/16787536).

## Play Billing Library setup

[Add the Play Billing Library dependency](https://developer.android.com/google/play/billing/getting-ready#dependency) to your Android app. To use the
external payments APIs you need to use version 8.3 or higher. If you need to
migrate from an earlier version, follow the instructions in the
[migration guide](https://developer.android.com/google/play/billing/migrate-gpblv8) to upgrade before starting your integration.

## Initialize the billing client

The first steps in the integration process are the same as the ones
described in the [Google Play Billing integration guide](https://developer.android.com/google/play/billing/integrate), with a few
modifications when [initializing your BillingClient](https://developer.android.com/google/play/billing/integrate#initialize):

- You need to call a new [`enableBillingProgram(EnableBillingProgramParams)`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) method to indicate that you want to offer external payments.
- You need to register an [`DeveloperProvidedBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener) for handling cases where the user chooses to pay on your website or a payment app.

The following example demonstrates initializing a BillingClient with these
modifications:

### Kotlin

    val purchasesUpdatedListener =
        PurchasesUpdatedListener { billingResult, purchases ->
            // Handle new Google Play purchase.
        }

    val developerProvidedBillingListener =
        DeveloperProvidedBillingListener { details ->
            // Handle user selection for developer provided billing option.
        }

    val billingClient = BillingClient.newBuilder(context)
        .setListener(purchasesUpdatedListener)
        .enablePendingPurchases()
        .enableBillingProgram(
            EnableBillingProgramParams.newBuilder()
                .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
                .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
                .build())
        .build()

### Java

    private PurchasesUpdatedListener purchasesUpdatedListener = new PurchasesUpdatedListener() {
        @Override
        public void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
            // Handle new Google Play purchase.
        }
    };

    private DeveloperProvidedBillingListener developerProvidedBillingListener =
        new DeveloperProvidedBillingListener() {
            @Override
            public void onUserSelectedDeveloperBilling(
                DeveloperProvidedBillingDetails details) {
                // Handle user selection for developer provided billing option.
            }
        };

    private BillingClient billingClient = BillingClient.newBuilder(context)
        .setListener(purchasesUpdatedListener)
        .enablePendingPurchases()
        .enableBillingProgram(
            EnableBillingProgramParams.newBuilder()
                .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
                .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
                .build())
        .build();

## Connect to Google Play

After you initialize the `BillingClient`, connect to Google Play as described
in [Connect to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play).

## Check user eligibility

After you connect to Google Play, you can check if the user is eligible for
the external payments program by calling the
[`isBillingProgramAvailableAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) method. This method returns
[`BillingResponseCode.OK`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK()) if the user is eligible.
The following sample demonstrates how to check eligibility:

### Kotlin

    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_PAYMENTS,
      object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
          billingProgram: Int, billingResult: BillingResult) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external payments unavailable, etc.
                return
            }

            // External payments are available. Can proceed with generating an
            // external transaction token.
    })

### Java

    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_PAYMENTS,
      new BillingProgramAvailabilityListener() {
        @Override
        public void onBillingProgramAvailabilityResponse(
          int billingProgram, BillingResult billingResult) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external payments unavailable, etc.
                return;
            }

            // External payments are available. Can proceed with generating an external transaction token.
          }

        });

See the [response handling](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#response-handling) section for details on how your app should
respond to other response codes. If you're [using Kotlin extensions](https://developer.android.com/google/play/billing/integrate#dependency), you
can use Kotlin coroutines so you don't have to define a separate listener.

## Display available products

You can [display available products to the user](https://developer.android.com/google/play/billing/integrate#show-products) in the same way as with
a Google Play billing system integration. When your user has seen the
products available for purchase and selects one to buy, launch the external
payments flow as described in the
[launching the external payments flow section](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#launching-external).

## Prepare an external transaction token

To report an external transaction to Google Play, you must have an external
transaction token generated from the Play Billing Library. A new external
transaction token must be generated each time the user visits an external
website or app through the external payments API. This can be done by calling
the [`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)) API. The token should
be generated immediately before launchBillingFlow is called.

### Kotlin

    val params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .build()

    billingClient.createBillingProgramReportingDetailsAsync(
      params,
      object : BillingProgramReportingDetailsListener {
        override fun onCreateBillingProgramReportingDetailsResponse(
          billingResult: BillingResult,
          billingProgramReportingDetails: BillingProgramReportingDetails?) {
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
    })

### Java

    BillingProgramReportingDetailsParams params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .build();

    billingClient.createBillingProgramReportingDetailsAsync(
      params,
      new BillingProgramReportingDetailsListener() {
        @Override
        public void onCreateBillingProgramReportingDetailsResponse(
          BillingResult billingResult,
          @Nullable BillingProgramReportingDetails
            billingProgramReportingDetails) {
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

If you're [using Kotlin extensions](https://developer.android.com/google/play/billing/integrate#dependency), you can use Kotlin coroutines so you
don't have to define a separate listener.

## Launching the external payments flow

Launch the external payments flow by calling [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams))
similar to [launching a purchase flow](https://developer.android.com/google/play/billing/integrate#launch) with a Google Play billing
system integration but with an additional parameter
[`DeveloperBillingOptionParams`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams) provided indicating your app would like to
enable the external payments flow for this purchase.

`DeveloperBillingOptionParams` must contain the following:

- `billingProgram` set to `EXTERNAL_PAYMENTS` billing program
- `linkURI` set to the link destination
- `launchMode` set to [`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams.LaunchMode#LAUNCH_IN_EXTERNAL_BROWSER_OR_APP()) if Google Play should launch the link or [`CALLER_WILL_LAUNCH_LINK`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams.LaunchMode#CALLER_WILL_LAUNCH_LINK()) if your app will launch the link.

When your app calls `launchBillingFlow()` with
`DeveloperBillingOptionParams` provided, the Google Play billing system
performs the following check:

- The system checks if the user's [Google Play country](https://support.google.com/googleplay/answer/7431675) is a country that supports external payments (i.e. a supported country). If the user's Google Play country is supported, Google Play checks whether external payments is enabled based on the configuration of the BillingClient and whether `DeveloperBillingOptionParams` is provided.
  - If external payments have been enabled, the purchase flow shows the user choice UX.
  - If external payments are not enabled, the purchase flow shows the standard Google Play billing system UX, without user choice.
- If the user's Google Play country is not a supported country, the purchase flow shows the standard Google Play billing system UX, without user choice.

|---|---|---|
|   | User's Play country is a supported country | User's Play country is not a supported country |
| External payments enabled ([BillingClient setup](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#setup) and [launchBillingFlow](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#launching-external)) | User sees user choice UX | User sees standard Google Play billing system UX |
| External payments not enabled (either not enabled during BillingClient setup or DeveloperBillingOptionParams not provided to launchBillingFlow) | User sees standard Google Play billing system UX | User sees standard Google Play billing system UX |

The following snippet demonstrates how to construct
`DeveloperBillingOptionParams`:

### Kotlin

    val developerBillingOptionParams =
        DeveloperBillingOptionParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
            .setLaunchMode(
                DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
            .build()

### Java

    DeveloperBillingOptionParams developerBillingOptionParams =
        DeveloperBillingOptionParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
            .setLaunchMode(
                DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
            .build();

## Handle the user selection

How you handle the rest of the purchase flow differs depending on whether
the user selected Google Play's billing system or to pay on your website.

### When the user selects to pay on your website or on a payment app

If the user chooses to pay on your website, Google Play calls the
`DeveloperProvidedBillingListener` to notify the app that the user chose to
pay on your website or on a payment app. In particular, the
[`onUserSelectedDeveloperBilling()`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener#onUserSelectedDeveloperBilling(com.android.billingclient.api.DeveloperProvidedBillingDetails)) method is called.

If your app sets `launchMode` to `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP` then
Google Play will launch the link. If `launchMode` was set to
`CALLER_WILL_LAUNCH_LINK` your app is responsible for launching the link.
When linking users to a payment app, you are responsible for checking that
the user has the payment app already installed on their device.

Use this token to report any transaction resulting from this choice as explained
in the [backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend).

### When the user selects Google Play's billing system

If the user chooses Google Play's billing system, they continue with the
purchase through Google Play.

- See [Processing purchases](https://developer.android.com/google/play/billing/integrate#process) in the library integration guide for more information about how to handle new in-app purchases through Google Play's billing system.
- See [New subscriptions](https://developer.android.com/google/play/billing/subscriptions#new) in the subscription management guide for additional guidance for subscription purchases.

## Handle changes in subscription

For developers using external payments, purchases need to be either processed
through Google Play's billing system or reported with an
`externalTransactionId`, depending on the user's choice. Changes to existing
subscriptions that were processed through the developer's website can be
made through the same billing system until expiration.

This section describes how to handle some common subscription change
scenarios.

### Upgrade and downgrade flows

Subscription plan changes including upgrade and downgrade flows should be
handled differently depending on whether the subscription was originally
bought through Google Play's billing system or through the developer's
website.

Add-ons that depend on an existing subscription, share the same payment
method, and align recurring charges are handled as upgrades. For other
add-ons, users should be able to choose which billing system they want to
use. Initiate a new purchase experience by using `launchBillingFlow()`, as
described in [launching the external payments flow](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#launching-external).

### Subscriptions bought through the developer's website or a payment app

For subscriptions that were originally bought through the developer's website
or a payment app after user choice, users requesting an upgrade or a
downgrade should proceed through the developer's website or a payment app
without going through the user choice experience again.

To do this, call `launchBillingFlow()` when the user requests an upgrade or a
downgrade. Instead of specifying other params under the
`SubscriptionUpdateParams` object, use
[`setOriginalExternalTransactionId()`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String)), providing the external transaction
ID for the original purchase.

`DeveloperBillingOptionParams` must also be provided in this call. This does
not display the user choice screen, given that the user choice for the
original purchase is preserved for upgrades and downgrades. You must generate
a new external transaction token for this transaction as described [here](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#prepare-external).

When the upgrade or downgrade is completed using the developer's website or a
payment app, you need to [report a new transaction](https://developer.android.com/google/play/billing/outside-gpb-backend) using the external
transaction token obtained through the previous call for the new subscription
purchase.

### Subscriptions bought through Google Play's billing system

Similarly, users that bought their current subscription through Google Play's
billing system after user choice should be shown go through the
[standard Google Play Billing flow](https://developer.android.com/google/play/billing/subscriptions#change). `DeveloperBillingOptionParams` must
not be set in the call to `launchBillingFlow`.

### Subscription cancellations and restorations

Users should be able to [cancel](https://developer.android.com/google/play/billing/subscriptions#cancel) their subscription at any time. When a
user cancels a subscription, the termination of the entitlement may be
deferred until the paid period ends. For example, if a user cancels a
monthly subscription halfway through the month, they may continue to access
the service for the remaining \~2 weeks until their access is removed. During
this period, the subscription is still technically active, so the user can
use the service.

It is not uncommon that users decide to reverse the cancellation during this
active period. In this guide, this is called a restoration. The following
sections describe how to handle restoration scenarios in your external payments
API integration.

#### Subscriptions bought through the developer's website

If you have an external transaction ID for a canceled subscription, it's not
necessary to call `launchBillingFlow()` to restore the subscription, so it
shouldn't be used for this type of activation. If a user restores their
subscription while still in the active period of a canceled subscription, no
transaction occurs at that time; you can just continue reporting renewals
when the current cycle expires and the next renewal occurs. This includes
cases where the user receives a credit or special renewal price as part of
the restoration (for example, a promotion to encourage the user to continue
their subscription).

#### Subscriptions bought through Google Play's billing system

Generally, users can restore subscriptions on Google Play's billing system.
For canceled subscriptions that were originally purchased on Google Play's
billing system, the user may choose to undo the cancellation while the
subscription is active through Google Play's [Resubscribe](https://developer.android.com/google/play/billing/subscriptions#restore) feature. In
that case, you receive a SUBSCRIPTION_RESTARTED Real Time Developer
Notification in your backend, and a new purchase token is not issued---the
original token is used to continue the subscription. To learn how to manage
restoration in Google Play's billing system, see [Restorations](https://developer.android.com/google/play/billing/subscriptions#restore) in the
subscription management guide.

You can also trigger a restoration in Google Play's billing system from the
app by calling `launchBillingFlow()`. See
[Before subscription expiration - in-app](https://developer.android.com/google/play/billing/subscriptions#before-in-app) for an explanation of how to do
this. In the case of users that went through the user choice flow for the
original purchase (which was canceled but is still active), the system
automatically detects their choice and displays the user interface for
restoring these purchases. They are asked to confirm their re-purchase of the
subscription through Google Play, but they don't need to go through the user
choice flow again. A new purchase token is issued for the user in this case.
Your backend receives a SUBSCRIPTION_PURCHASED Real Time Developer
Notification, and the linkedPurchaseToken value for the new purchase status
is set as in the case of an upgrade or downgrade, with the old purchase token
for the subscription that was canceled.

### Resubscriptions

If a subscription completely expires, whether it is due to cancellation or
payment decline without recovery (an expired account hold), then the user
must resubscribe if they want to restart the entitlement.

Resubscribing can also be enabled through the app by processing it similarly
to a standard signup. Users should be able to choose which billing system
they want to use. `launchBillingFlow()` may be called in this case, as
described in [launching the external payments flow](https://developer.android.com/google/play/billing/externalpaymentlinks/integration#launching-external).

## Response handling

When an error occurs, the methods `isBillingProgramAvailableAsync()` ,
`createBillingProgramReportingDetailsAsync()`, `launchBillingFlow()` might
provide a `BillingResponseCode` other than `BillingResponseCode.OK`. Consider
handling these response codes as follows:

- [`BillingResponseCode.ERROR`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR()): This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling the API again.
- [`BillingResponseCode.FEATURE_NOT_SUPPORTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED()): The external payments APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- [`BillingResponseCode.DEVELOPER_ERROR`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#DEVELOPER_ERROR()): There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- [`BillingResponseCode.USER_CANCELED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED()): Don't proceed with opening the external website or app. Call `launchBillingFlow()` again to display the information dialog to the user the next time you attempt to direct the user outside of the app.
- [`BillingResponseCode.BILLING_UNAVAILABLE`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE()): The transaction is not eligible for external payments and therefore developer billing won't be available under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- [`BillingResponseCode.NETWORK_ERROR`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR()), [`BillingResponseCode.SERVICE_DISCONNECTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED()), [`BillingResponseCode.SERVICE_UNAVAILABLE`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE()): These are transient errors that should be handled with an appropriate retry policy. In the case of `SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external payments links

License testers should be used to test your external payments integration.
You won't be invoiced for transactions that have been initiated by license
tester accounts. See
[Test in-app billing with application licensing](https://support.google.com/googleplay/android-developer/answer/6062777) for more information on
configuring license testers.

## Next steps

After you've finished in-app integration, you're ready to [integrate your
backend](https://developer.android.com/google/play/billing/outside-gpb-backend).