---
title: https://developer.android.com/google/play/billing/external/integration
url: https://developer.android.com/google/play/billing/external/integration
source: md.txt
---

This guide describes how to integrate with the APIs to support external offers in eligible apps and regions. To learn more about the external offers program including eligibility requirements and geographic scope see[program requirements](https://support.google.com/googleplay/android-developer/answer/14372887).

## Play Billing Library setup

To use the external offers APIs,[add version 8.2.1 or higher of the Play Billing Library dependency](https://developer.android.com/google/play/billing/getting-ready#dependency)to your Android app. If you need to migrate from an earlier version, follow the instructions in the[migration guide](https://developer.android.com/google/play/billing/migrate-gpblv8)before you attempt to implement external offers.

## Connect to Google Play

The first steps in the integration process are the same as the ones described in the[billing integration guide](https://developer.android.com/google/play/billing/integrate), except you must call[`enableBillingProgram`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(int))to indicate that you want to use external offers when[initializing your`BillingClient`](https://developer.android.com/google/play/billing/integrate#initialize):

The following example demonstrates initializing a`BillingClient`with these modifications:  

### Kotlin

    val billingClient = BillingClient.newBuilder(context)
      .enableBillingProgram(BillingProgram.EXTERNAL_OFFER)
      .build()

### Java

    private BillingClient billingClient = BillingClient.newBuilder(context)
        .enableBillingProgram(BillingProgram.EXTERNAL_OFFER)
        .build();

After you initialize the`BillingClient`, you need to[establish a connection to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play)as described in the integration guide.

## Check availability

In order to confirm external offers are available to the current user, call[`isBillingProgramAvailableAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)).

This API returns`BillingResponseCode.OK`if external offers are available. See[response handling](https://developer.android.com/google/play/billing/external/integration#response-handling)for details on how your app should respond to other response codes.  

### Kotlin


    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_OFFER,
      object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
          billingResult: BillingResult,
          billingProgramAvailabilityDetails: BillingProgramAvailabilityDetails) {
            if (billingResult.responseCode !=  BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external offers unavailable, etc.
                return
            }

            // External offers are available. Continue with steps in the
            // guide.
          }
      })

### Java


    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_OFFER,
      new BillingProgramAvailabilityListener() {
        @Override
        public void onBillingProgramAvailabilityResponse(
          BillingResult billingResult,
          BillingProgramAvailabilityDetails billingProgramAvailabilityDetails) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external offers being unavailable, etc.
                return;
            }
            // External offers are available. Continue with steps in the
            // guide.
          }
      });

## Prepare an external transaction token

To report an external transaction to Google Play, you must have an external transaction token generated from the Play Billing Library. You can obtain this token by calling the[`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener))API. A new token must be generated immediately before directing the user outside the app for each external offer. Tokens must not be cached across transactions.  

### Kotlin

    val params =
      BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
        .build();

    billingClient.createBillingProgramReportingDetailsAsync(
      params,
      object : BillingProgramReportingDetailsListener {
        override fun onCreateBillingProgramReportingDetailsResponse(
          billingResult: BillingResult,
          billingProgramReportingDetails: BillingProgramReportingDetails?) {
            if (billingResult.responseCode !=  BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return
            }
            val externalTransactionToken =
                billingProgramReportingDetails?.externalTransactionToken
            // Persist the transaction token in your backend. You may pass it
            // to the external website when calling the launchExternalLink API.
        }
    })

### Java

    BillingProgramReportingDetailsParams params =
      BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
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
            // Persist the transaction token in your backend. You may pass it
            // to the external website when calling the launchExternalLink API.
          }
    });

Alternatively, you can query the suspend function[`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener))with[Kotlin extensions](https://developer.android.com/google/play/billing/integrate#dependency)so that you don't need to define a listener:  

      val createBillingProgramReportingDetailsResult =
        withContext(context) {
          billingClient
            .createBillingProgramReportingDetails(params)
        }
      // Process the result

## Launch external offer flow

To start an external offer flow, your eligible app must call the[`launchExternalLink()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener))API from your app's main thread. This API takes an input of an[`LaunchExternalLinkParams`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams)object. To create an`LaunchExternalLinkParams`object, use the[`LaunchExternalLinkParams.Builder`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.Builder)class. This class contains the following parameters:

- **linkUri**- The link to the external website where the digital content or app download is offered. For app downloads, this link must be registered and approved in the Play Developer Console.
- **linkType**- The type of content being offered to the user.
- **launchMode** - Specifies how the link is launched. For app downloads, you must set this to`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`.
- **billingProgram** - Set this to`BillingProgram.EXTERNAL_OFFER`.

When you call[`launchExternalLink()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)), it might show additional information dialogs to the user based on their user settings. Depending on the`launchMode`parameter, Play either launches the link URI in an external browser or returns the flow to your app to launch the URI. In most cases, you can use the[`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.LaunchMode#LAUNCH_IN_EXTERNAL_BROWSER_OR_APP())mode where Play will launch the URI for you. If you want to have more customized behavior, such as launching the URI in a webview or opening the URI in a specific browser, you can use the[`CALLER_WILL_LAUNCH_LINK`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.LaunchMode#CALLER_WILL_LAUNCH_LINK())mode. To protect user privacy, make sure no personally identifiable information (PII) is passed in the URI.
**Note:** Users might not return to your app after the link URI is opened in an external browser or app. Execute any necessary in-app tasks before calling[`launchExternalLink()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)).  

### Kotlin


    // An activity reference from which the external offers flow will be launched.
    val activity = ...;

    val params =
      LaunchExternalLinkParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
        // You can pass along the external transaction token from
        // BillingProgramReportingDetails as a URL parameter in the URI
        .setLinkUri(yourLinkUri)
        .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
        .setLaunchMode(
          LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
        .build()

    val listener : LaunchExternalLinkResponseListener =
      LaunchExternalLinkResponseListener {
          override fun onLaunchExternalLinkResponse(billingResult: BillingResult) {
        if (billingResult.responseCode == BillingResponseCode.OK) {
          // Proceed with the rest of the external offer flow. If the user
          // purchases an item, be sure to report the transaction to Google Play.
        } else {
          // Handle failures such as retrying due to network errors.
        }
      }
    }

    billingClient.launchExternalLink(activity, params, listener)

### Java


    // An activity reference from which the external offers flow will be launched.
    Activity activity = ...;

    LaunchExternalLinkParams params = LaunchExternalLinkParams.newBuilder()
      .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
      // You can pass along the external transaction token from  
      // BillingProgramReportingDetails as a URL parameter in the URI
      .setLinkUri(yourLinkUri)
      .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
      .setLaunchMode(
        LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
      .build();

    LaunchExternalLinkResponseListener listener =
      new LaunchExternalLinkResponseListener() {
        @Override
        public void onLaunchExternalLinkResponse(BillingResult billingResult) {
          if (billingResult.responseCode == BillingResponseCode.OK) {
            // Proceed with the rest of the external offer flow. If the user
            // purchases an item, be sure to report the transaction to Google
            // Play.
          } else {
            // Handle failures such as retrying due to network errors.
          }
        }
      }

    billingClient.launchExternalLink(activity, params, listener);

If you set`LaunchMode`to`CALLER_WILL_LAUNCH_LINK`, you should direct the user outside of the app only if`onLaunchExternalLinkResponse`provides`BillingResponseCode.OK`.

### Report transactions to Google Play

| **Note:** See[Enrolling in the external offers program](https://support.google.com/googleplay/android-developer/answer/14372887)for transaction reporting requirements.

You must report all external transactions to Google Play by calling the Google Play Developer API from your backend. When you report a transaction, you must provide an`externalTransactionToken`obtained from the[`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener))API. If a user makes multiple purchases, you can use the same`externalTransactionToken`to report each purchase. To learn how to report a transaction, see the[backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend).

## Response handling

When an error occurs, the methods`isBillingProgramAvailableAsync()`,`createBillingProgramReportingDetailsAsync()`, and`launchExternalLink()`might return responses other than`BillingResponseCode.OK`. Consider handling these response codes as follows:

- `ERROR`: This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling`launchExternalLink()`to display the information dialog to the user the next time you attempt to direct the user outside the app.
- `FEATURE_NOT_SUPPORTED`: The external offers APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- `USER_CANCELED`: Don't proceed with opening the external website. Call`launchExternalLink()`again to display the information dialog to the user the next time you attempt to direct the user outside of the app.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for external offers and therefore shouldn't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be handled with an appropriate retry policy. In the case of`SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external offers

License testers should be used to test your external offers integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See[Test in-app billing with application licensing](https://support.google.com/googleplay/android-developer/answer/6062777)for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to[integrate your backend](https://developer.android.com/google/play/billing/outside-gpb-backend).